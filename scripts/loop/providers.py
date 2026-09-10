"""CLI adapters and conservative local checks against metered authentication.

No credentials are copied, printed, or persisted. Account-side extra usage must
also be disabled by the user; a local process cannot enforce remote billing.
"""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

VENDORS = ('codex', 'claude', 'gemini', 'grok')
BILLING_ENV = (
    'OPENAI_API_KEY', 'CODEX_API_KEY', 'OPENAI_BASE_URL', 'OPENAI_API_BASE',
    'ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'ANTHROPIC_BASE_URL',
    'CLAUDE_CODE_USE_BEDROCK', 'CLAUDE_CODE_USE_VERTEX', 'CLAUDE_CODE_USE_FOUNDRY',
    'GEMINI_API_KEY', 'GOOGLE_API_KEY', 'GOOGLE_GENAI_USE_VERTEXAI',
    'XAI_API_KEY', 'GROK_API_KEY', 'GROK_MODELS_BASE_URL', 'GROK_MODELS_LIST_URL',
    'GROK_XAI_API_BASE_URL',
)


def json_file(path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except (ValueError, OSError) as exc:
        raise RuntimeError(f'Cannot read configuration {path}; check its format.') from exc


def reject_config(path, pattern):
    if path.exists() and re.search(pattern, path.read_text(), re.I | re.M):
        raise RuntimeError(f'Possible metered/custom-provider configuration in {path}. Use subscription login with the standard provider.')


def check(vendor, root):
    executable = shutil.which(vendor)
    if not executable:
        raise RuntimeError(f'{vendor} is not installed. See README.md for setup.')
    for name in BILLING_ENV:
        if os.environ.get(name) and os.environ[name].lower() not in ('0', 'false'):
            raise RuntimeError(f'{name} is set. Unset it before using subscription-only loops (value not displayed).')
    # Gemini can auto-load .env files; reject credential assignments before launch.
    if vendor == 'gemini':
        for directory in [root, *root.parents, Path.home()]:
            for path in (directory / '.env', directory / '.gemini' / '.env'):
                reject_config(path, r'^\s*(?:export\s+)?(?:GEMINI_API_KEY|GOOGLE_API_KEY|GOOGLE_GENAI_USE_VERTEXAI)\s*=')
    home = Path.home()
    if vendor == 'codex':
        codex_home = Path(os.environ.get('CODEX_HOME', home / '.codex'))
        for path in [codex_home / 'config.toml', root / '.codex/config.toml']:
            reject_config(path, r'^\s*\[model_providers\.')
        result = subprocess.run([executable, 'login', 'status'], capture_output=True, text=True, timeout=30)
        if result.returncode or 'logged in using chatgpt' not in (result.stdout + result.stderr).lower():
            raise RuntimeError('Codex needs ChatGPT login: run codex login. API-key login is not accepted.')
    elif vendor == 'claude':
        claude_home = Path(os.environ.get('CLAUDE_CONFIG_DIR', home / '.claude'))
        for path in [claude_home / 'settings.json', root / '.claude/settings.json', root / '.claude/settings.local.json']:
            reject_config(path, r'"(?:apiKeyHelper|ANTHROPIC_API_KEY|ANTHROPIC_AUTH_TOKEN|ANTHROPIC_BASE_URL|CLAUDE_CODE_USE_(?:BEDROCK|VERTEX|FOUNDRY))"\s*:')
        result = subprocess.run([executable, 'auth', 'status', '--json'], capture_output=True, text=True, timeout=30)
        try:
            auth = json.loads(result.stdout)
        except ValueError:
            auth = {}
        if result.returncode or not auth.get('loggedIn') or (auth.get('authMethod') != 'claude.ai' or auth.get('apiProvider') != 'firstParty' or auth.get('subscriptionType') not in ('pro', 'max')):
            raise RuntimeError('Claude needs subscription login: run claude auth login, then claude auth status. Console/API authentication is not accepted.')
    elif vendor == 'gemini':
        selected = None
        system = Path('/Library/Application Support/GeminiCli/settings.json' if os.sys.platform == 'darwin' else '/etc/gemini-cli/settings.json')
        system = Path(os.environ.get('GEMINI_CLI_SYSTEM_SETTINGS_PATH', system))
        paths = [home / '.gemini/settings.json', root / '.gemini/settings.json', system]
        for path in paths:
            config = json_file(path)
            auth = config.get('security', {}).get('auth', {})
            if auth.get('selectedType'):
                selected = auth['selectedType']
            if auth.get('enforcedType') not in (None, 'oauth-personal'):
                raise RuntimeError(f'{path} enforces non-Google-login authentication; this loop requires Google login.')
            reject_config(path, r'"(?:apiKey|apiKeyHelper|GEMINI_API_KEY|GOOGLE_API_KEY)"\s*:')
        if selected != 'oauth-personal':
            raise RuntimeError('Run gemini interactively and choose Sign in with Google before starting this loop.')
    else:
        grok_home = Path(os.environ.get('GROK_HOME', home / '.grok'))
        for path in [grok_home / 'config.toml', root / '.grok/config.toml']:
            reject_config(path, r'^\s*(?:\[model\.|(?:api_key|env_key|base_url|extra_headers)\s*=)')
        # Grok has no documented auth-status subcommand. Cached browser login is
        # used without API credentials; missing/expired login is a fatal CLI error.
    return executable


def command(vendor, executable, prompt):
    """Return argv and stdin. Grok supports a direct prompt-file argument."""
    if vendor == 'codex':
        return [executable, '-a', 'never', 'exec', '--sandbox', 'workspace-write',
                '-c', 'model_provider="openai"', '-c', 'forced_login_method="chatgpt"',
                '--json', '-'], prompt
    if vendor == 'claude':
        return [executable, '-p', '--output-format', 'stream-json', '--verbose',
                '--permission-mode', 'acceptEdits', '--permission-prompts', 'none',
                '--allowedTools', 'Read,Write,Edit,Glob,Grep,Bash(python3 *),Bash(rg *),Bash(git status *),Bash(git diff *),WebSearch,WebFetch'], prompt
    if vendor == 'gemini':
        return [executable, '--output-format', 'stream-json', '--sandbox',
                '--approval-mode', 'auto_edit', '--allowed-tools',
                'run_shell_command(python3),run_shell_command(rg),run_shell_command(git status),run_shell_command(git diff)'], prompt
    return [executable, '--no-auto-update', '--sandbox', 'workspace',
            '--always-approve', '--prompt-file', 'PROMPT.md', '--output-format', 'streaming-json'], None
