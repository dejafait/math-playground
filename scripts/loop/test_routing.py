"""Routing decisions, escalation budgets and active-profile evidence."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

import codex
import routing
import runner
import test_portfolio
from test_loop import review_fixture
from test_research import report

CATALOG = {m: set(routing.EFFORTS) for m in routing.MODELS.values()}


class RoutingTests(unittest.TestCase):
    def route(self, local=None, ready=True, catalog=CATALOG):
        return routing.select(report('start', 'EXPLORATION'), local or {}, ready, catalog)

    def nominated(self, task='proof_attempt', role='deep_research', effort='high'):
        text = report('next', 'EXPLORATION') + (f'NEXT_TASK_TYPE: {task}\nNEXT_MODEL_ROLE: {role}\n'
                f'NEXT_EFFORT: {effort}\nNEXT_ROUTING_REASON: Need a uniform analytic estimate\n')
        return {'next_route': routing.recommendation(text)}

    def test_bootstrap_and_gate_defaults(self):
        self.assertEqual(self.route()['model'], 'gpt-6.1-sol')
        self.assertEqual(self.route()['effort'], 'high')
        self.assertEqual(self.route(ready=False)['effort'], 'medium')
        self.assertEqual(self.route(self.nominated(), ready=False)['model'], 'gpt-6.1-sol')

    def test_task_recommendation_and_stale_target(self):
        state = self.nominated('source_extraction', 'routine', 'low')
        self.assertEqual(self.route(state)['model'], 'gpt-6-luna')
        state['next_route']['target'] = 'stale'
        self.assertEqual(self.route(state)['model'], 'gpt-6.1-sol')
        self.assertIsNone(routing.recommendation(report('x', 'ADVANCE')))

    def test_max_requires_specific_obstruction_and_prior_attempt(self):
        state = self.nominated(effort='max')
        self.assertEqual(self.route(state)['effort'], 'high')
        state.update(last_outcome='success', research_outcome='EXPLORATION',
                     last_route={'target': 'test', 'model': 'gpt-6-astra', 'effort': 'high'})
        self.assertEqual(self.route(state)['effort'], 'high')
        state['next_route']['escalation'] = 'Uniform tail bound survived the high-depth attempt'
        self.assertEqual(self.route(state)['effort'], 'max')
        state['routing_history'] = [{'effort': 'max'}] * 2
        self.assertEqual(self.route(state)['effort'], 'high')

    def test_expensive_share_and_downgrade(self):
        state = self.nominated()
        state['routing_history'] = [{'model': 'gpt-6-astra'}] * 4
        self.assertEqual(self.route(state)['model'], 'gpt-6.1-sol')
        state = self.nominated('implementation', 'standard', 'high')
        self.assertEqual(self.route(state)['model'], 'gpt-6.1-sol')

    def test_availability_and_supported_effort_fallback(self):
        state = self.nominated()
        result = self.route(state, catalog={'gpt-6.1-sol': {'low', 'medium'}})
        self.assertEqual((result['model'], result['effort']), ('gpt-6.1-sol', 'medium'))
        with self.assertRaises(RuntimeError):
            self.route(catalog={'unknown-model': {'high'}})
        self.assertEqual(self.route(catalog={})['availability'], 'unverified')

    def test_cli_passes_explicit_settings_literally(self):
        argv, stdin = codex.command('codex', 'literal $() text', self.route(self.nominated()))
        self.assertIn('gpt-6-astra', argv)
        self.assertIn('model_reasoning_effort="high"', argv)
        self.assertEqual(stdin, 'literal $() text')

    def test_profile_cache_and_actual_session_telemetry(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / 'models_cache.json').write_text(json.dumps({'models': [
                {'slug': 'gpt-6-astra', 'supported_reasoning_levels': [{'effort': 'high'}]}]}))
            self.assertEqual(routing.available(home), {'gpt-6-astra': {'high'}})
            with sqlite3.connect(home / 'state_5.sqlite') as db:
                db.execute('CREATE TABLE threads (id TEXT, model TEXT, reasoning_effort TEXT)')
                db.execute("INSERT INTO threads VALUES ('active','gpt-6-astra','high')")
            result = routing.telemetry('active', home)
            self.assertEqual(result['actual_model'], 'gpt-6-astra')
            self.assertEqual(result['actual_effort'], 'high')
            self.assertEqual(result['allowance'], 'unavailable')
            self.assertIsNone(routing.telemetry(None, home)['actual_model'])


class RoutingRunnerTests(unittest.TestCase):
    setUp = test_portfolio.PortfolioTests.setUp
    tearDown = test_portfolio.PortfolioTests.tearDown
    state = test_portfolio.PortfolioTests.state
    run_step = test_portfolio.PortfolioTests.run_step

    def test_accepted_turn_routes_following_invocation(self):
        import sys
        def first(*args):
            review_fixture(args[-1], 'SPECIALIZE')
            text = report('review', 'EXPLORATION') + ('NEXT_TASK_TYPE: proof_attempt\n'
                'NEXT_MODEL_ROLE: deep_research\nNEXT_EFFORT: high\nNEXT_ROUTING_REASON: Nontrivial proof gap\n')
            (args[-1] / 'PROGRESS.md').write_text(text)
            return 'success', None, 0
        def second(*args):
            self.assertIn('gpt-6-astra', args[0])
            self.assertIn('model_reasoning_effort="high"', args[0])
            (args[-1] / 'PROGRESS.md').write_text(report('proof', 'NEGATIVE').replace(
                'STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace('NOVELTY_UNCHECKED', 'REPRODUCTION'))
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--once', '--problem', 'riemann']), patch('routing.available', return_value=CATALOG):
            with patch.object(runner, 'run_process', side_effect=first):
                runner.main()
            with patch.object(runner, 'run_process', side_effect=second):
                runner.main()
        history = self.state()['problems']['riemann']['routing_history']
        self.assertEqual(history[-1]['model'], 'gpt-6-astra')
        self.assertEqual(history[-1]['validation'], 'accepted')
        self.assertIsNone(history[-1]['actual_model'])


if __name__ == '__main__':
    unittest.main()
