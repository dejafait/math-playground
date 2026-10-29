"""Safe boundary reloads: temporary code and fake exec, no inference."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from reloader import Reloader


class ReloadTests(unittest.TestCase):
    def test_reload_preserves_argv_and_environment_without_touching_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            code = root / 'routing.py'
            code.write_text('VALUE = 1\n')
            state = root / 'state.json'
            state.write_text('{"retry_at": 12345, "next_problem": "beal"}')
            reloader = Reloader(root)
            with patch('reloader.os.execv') as execute, patch('reloader.sys.argv', ['runner.py', '--problem', 'beal']), patch('reloader.sys.executable', '/python'):
                self.assertFalse(reloader.check(Mock()))
                execute.assert_not_called()
                code.write_text('VALUE = 2\n')
                self.assertTrue(reloader.check(Mock()))
                execute.assert_called_once_with('/python', ['/python', 'runner.py', '--problem', 'beal'])
            self.assertEqual(state.read_text(), '{"retry_at": 12345, "next_problem": "beal"}')

    def test_invalid_update_is_deferred_then_corrected_update_reloads(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            code = root / 'runner.py'
            code.write_text('VALUE = 1\n')
            reloader = Reloader(root)
            announce = Mock()
            with patch('reloader.os.execv') as execute:
                code.write_text('def broken(\n')
                self.assertFalse(reloader.check(announce))
                self.assertFalse(reloader.check(announce))
                execute.assert_not_called()
                announce.assert_called_once()
                code.write_text('VALUE = 3\n')
                self.assertTrue(reloader.check(announce))
                execute.assert_called_once()

    def test_test_data_does_not_trigger_reload_but_added_runtime_module_does(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reloader = Reloader(root)
            (root / 'test_something.py').write_text('invalid(\n')
            (root / 'telemetry.json').write_text('{}')
            with patch('reloader.os.execv') as execute:
                self.assertFalse(reloader.check(Mock()))
                (root / 'new_runtime.py').write_text('VALUE = 1\n')
                self.assertTrue(reloader.check(Mock()))
                execute.assert_called_once()

    def test_reload_does_not_repeat_explicit_research_budget_renewal(self):
        for option in (['--resume-research', 'beal'], ['--resume-research=beal']):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                code = root / 'runner.py'
                code.write_text('VALUE = 1\n')
                reloader = Reloader(root)
                code.write_text('VALUE = 2\n')
                with patch('reloader.os.execv') as execute, patch('reloader.sys.argv', ['runner.py', *option, '--problem', 'beal']), patch('reloader.sys.executable', '/python'):
                    reloader.check(Mock())
                execute.assert_called_once_with('/python', ['/python', 'runner.py', '--problem', 'beal'])
