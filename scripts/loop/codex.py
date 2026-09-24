"""Codex command and local checks for ChatGPT subscription authentication."""
import os
from pathlib import Path
import re
import shutil
import subprocess

BILLING_ENV = ('OPENAI_API_KEY', 'CODEX_API_KEY', 'OPENAI_BASE_URL', 'OPENAI_API_BASE')


def reject_config(path, pattern):
    if path.exists() and re.search(pattern, path.read_text(), re.I | re.M):
        raise RuntimeError(f'Possible metered/custom-provider configuration in {path}. Use subscription login with the standard provider.')


def check(root):
    executable = shutil.which('codex')
    if not executable:
        raise RuntimeError('Codex is not installed. See README.md for setup.')
    for name in BILLING_ENV:
        if os.environ.get(name) and os.environ[name].lower() not in ('0', 'false'):
            raise RuntimeError(f'{name} is set. Unset it before using the subscription-only Codex loop (value not displayed).')
    home = Path.home()
    codex_home = Path(os.environ.get('CODEX_HOME', home / '.codex'))
    for path in [codex_home / 'config.toml', root / '.codex/config.toml']:
        reject_config(path, r'^\s*\[model_providers\.')
    result = subprocess.run([executable, 'login', 'status'], capture_output=True, text=True, timeout=30)
    if result.returncode or 'logged in using chatgpt' not in (result.stdout + result.stderr).lower():
        raise RuntimeError('Codex needs ChatGPT login: run codex login. API-key login is not accepted.')
    return executable


def command(executable, prompt):
    """Return Codex argv and literal prompt text for stdin."""
    return [executable, '-a', 'never', 'exec', '--sandbox', 'workspace-write',
            '-c', 'model_reasoning_effort="max"',
            '-c', 'model_provider="openai"', '-c', 'forced_login_method="chatgpt"',
            '--json', '-'], prompt
