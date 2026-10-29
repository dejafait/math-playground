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

    def nominated(self, task='proof_attempt', role='deep_research', effort='high', purpose=None, obstruction=None):
        text = report('next', 'EXPLORATION') + (f'NEXT_TASK_TYPE: {task}\nNEXT_MODEL_ROLE: {role}\n'
                f'NEXT_EFFORT: {effort}\nNEXT_ROUTING_REASON: Need a uniform analytic estimate\n')
        if purpose:
            text += f'NEXT_REASONING_CLASS: {purpose}\n'
        if obstruction:
            text += f'NEXT_ESCALATION: {obstruction}\n'
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

    def test_creative_max_needs_obstruction_but_no_prior_failure_or_share_budget(self):
        state = self.nominated(purpose='creative')
        self.assertEqual(self.route(state)['effort'], 'xhigh')
        state['next_route']['escalation'] = 'A new signed cancellation is needed to close the main uniform tail gap'
        state['routing_history'] = [{'effort': 'max', 'model': 'gpt-6-astra'}] * 10
        result = self.route(state)
        self.assertEqual((result['model'], result['effort'], result['reasoning_class']),
                         ('gpt-6-astra', 'max', 'creative'))
        self.assertEqual(self.route(state, ready=False)['model'], 'gpt-6.1-sol')
        self.assertEqual(self.route(state, ready=False)['effort'], 'medium')
        self.assertIsNone(self.route(state, ready=False)['reasoning_class'])

    def test_separate_audit_difficulty_and_candidate_scrutiny(self):
        state = self.nominated('proof_audit')
        self.assertEqual((self.route(state)['model'], self.route(state)['effort']), ('gpt-6.1-sol', 'high'))
        state['next_route']['reasoning_class'] = 'conceptual_audit'
        self.assertEqual((self.route(state)['model'], self.route(state)['effort']), ('gpt-6-astra', 'xhigh'))
        state['next_route']['reasoning_class'] = 'candidate_audit'
        self.assertEqual(self.route(state)['effort'], 'xhigh')
        state['next_route']['escalation'] = 'Independently check a possible complete proof, especially the limiting step'
        self.assertEqual(self.route(state)['effort'], 'max')

    def test_wrong_class_and_stale_target_cannot_allocate_creative_max(self):
        state = self.nominated('implementation', purpose='creative', obstruction='central gap', effort='max')
        self.assertIsNone(self.route(state)['reasoning_class'])
        self.assertEqual(self.route(state)['effort'], 'high')
        state = self.nominated(purpose='creative', obstruction='central gap')
        state['next_route']['target'] = 'obsolete'
        self.assertEqual(self.route(state)['model'], 'gpt-6.1-sol')

    def test_discovery_reminder_requires_accepted_turns_and_resets_on_creativity(self):
        state = {'routing_history': [{'validation': 'not_accepted'}] * 10}
        self.assertEqual(routing.planning_instruction(state), '')
        state['routing_history'] = [{'validation': 'accepted'}] * 4
        self.assertIn('prioritize a bounded new mechanism', routing.planning_instruction(state))
        state['routing_history'].append({'validation': 'accepted', 'outcome': 'success', 'reasoning_class': 'creative'})
        self.assertEqual(routing.planning_instruction(state), '')

    def test_development_is_protected_from_old_share_limit(self):
        state = self.nominated()
        state['routing_history'] = [{'model': 'gpt-6-astra'}] * 4
        self.assertEqual((self.route(state)['model'], self.route(state)['effort']), ('gpt-6-astra', 'xhigh'))
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
        self.assertIn('model_reasoning_effort="xhigh"', argv)
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

    def test_creative_route_reaches_cli_and_records_actual_purpose(self):
        import sys
        state_dir = self.root / 'scripts/loop-codex'
        state_dir.mkdir()
        state = self.nominated_creative_state()
        (state_dir / 'state.json').write_text(json.dumps({'problems': {'riemann': state}}))
        review_fixture(self.root / 'riemann', 'SPECIALIZE')
        def run(*args):
            self.assertIn('gpt-6-astra', args[0])
            self.assertIn('model_reasoning_effort="max"', args[0])
            self.assertIn('Current settings: gpt-6-astra, max.', args[1])
            (args[-1] / 'PROGRESS.md').write_text(report('creative', 'NEGATIVE').replace(
                'STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace('NOVELTY_UNCHECKED', 'REPRODUCTION'))
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--once', '--problem', 'riemann']), patch('routing.available', return_value=CATALOG), patch.object(runner, 'run_process', side_effect=run):
            runner.main()
        row = self.state()['problems']['riemann']['routing_history'][-1]
        self.assertEqual((row['model'], row['effort'], row['reasoning_class']), ('gpt-6-astra', 'max', 'creative'))

    def nominated_creative_state(self):
        return {'next_route': {'target': 'test', 'task_type': 'proof_attempt', 'role': 'standard',
                              'effort': 'high', 'reason': 'New central cancellation mechanism',
                              'reasoning_class': 'creative', 'escalation': 'Test the missing main-tail cancellation'},
                'routing_history': [{'model': 'gpt-6-astra', 'effort': 'max'}] * 10}

    def test_code_update_reloads_only_after_invocation_state_is_saved(self):
        import sys
        from reloader import Reloader
        code = self.root / 'scripts/loop/routing.py'
        code.write_text('VALUE = 1\n')
        reloader = Reloader(code.parent)
        calls = []
        def run(*args):
            calls.append('invoked')
            code.write_text('VALUE = 2\n')
            (args[-1] / 'PROGRESS.md').write_text(report('completed', 'ADVANCE'))
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--problem', 'riemann']), patch.object(runner, 'Reloader', return_value=reloader), patch.object(runner, 'run_process', side_effect=run), patch('reloader.os.execv', side_effect=SystemExit(42)) as execute:
            with self.assertRaises(SystemExit) as caught:
                runner.main()
        self.assertEqual(caught.exception.code, 42)
        execute.assert_called_once()
        self.assertEqual(calls, ['invoked'])
        self.assertEqual(self.state()['outcome'], 'success')
        self.assertGreater(self.state()['retry_at'], 0)
        self.assertEqual(self.state()['problems']['riemann']['turns'], 1)

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
            self.assertIn('model_reasoning_effort="xhigh"', args[0])
            prompt = args[1]
            self.assertEqual(prompt.count(routing.INSTRUCTION), 1)
            self.assertLess(prompt.index(routing.INSTRUCTION), prompt.index('Active problem:'))
            self.assertLess(prompt.index('END VERBATIM DAG.md'), prompt.index('BEGIN VERBATIM PROGRESS.md'))
            self.assertLess(prompt.index('END VERBATIM PROGRESS.md'), prompt.index('Literature gate:'))
            self.assertIn('Current settings: gpt-6-astra, xhigh.', prompt)
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
