"""Interpret CLI failures without treating quoted tool output as a quota error."""
import json
import re
import time
from datetime import datetime

QUOTA = re.compile(r'quota|rate.?limit|usage.?limit|hit.{0,20}limit|out of.{0,20}usage|limit.{0,30}(?:reached|exceeded)|resource.?exhausted|too many requests|\b429\b', re.I)
AUTH = re.compile(r'not logged in|not authenticated|authentication|unauthorized|invalid.api.key|login required|sign in|log in|token.{0,20}expired|\b401\b', re.I)
CONFIG = re.compile(r'unknown (?:option|argument|flag)|unrecognized (?:option|argument)|invalid (?:option|argument|model)|permission.denied|sandbox.{0,40}(?:unavailable|failed|not found)|command not found|subscription required', re.I)
TRANSIENT = re.compile(r'overloaded|temporar|capacity|timed? ?out|timeout|connection|network|econn|enotfound|eai_again|service unavailable|\b50[0234]\b', re.I)


def reset_time(data, text, now):
    """Only parse explicit epochs/offset-aware ISO times or relative durations.

Ambiguous human calendar dates/time zones use backoff instead of a guessed reset.
"""
    times = []
    def walk(value):
        if isinstance(value, dict):
            for key, item in value.items():
                normalized = key.lower().replace('_', '').replace('-', '')
                if normalized in ('resetsat', 'resetat', 'resettime', 'retryat'):
                    try:
                        stamp = float(item)
                        if stamp > 1e12:
                            stamp /= 1000
                        times.append(stamp)
                    except (ValueError, TypeError):
                        try:
                            parsed = datetime.fromisoformat(str(item).replace('Z', '+00:00'))
                            if parsed.tzinfo:
                                times.append(parsed.timestamp())
                        except ValueError:
                            pass
                elif normalized in ('retryafter', 'retryafterseconds', 'resetafterseconds'):
                    try:
                        times.append(now + float(item))
                    except (ValueError, TypeError):
                        pass
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)
    walk(data)
    for match in re.finditer(r'(?:retry|try again|resets?)\s+(?:after|in)\s+((?:\d+(?:\.\d+)?\s*(?:seconds?|secs?|s|minutes?|mins?|m|hours?|hrs?|h|days?|d)\s*)+)', text, re.I):
        seconds = 0
        for amount, unit in re.findall(r'(\d+(?:\.\d+)?)\s*([a-z]+)', match[1], re.I):
            seconds += float(amount) * {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[unit[0].lower()]
        times.append(now + seconds)
    for match in re.finditer(r'(?:resets?|retry)\s+(?:at\s+)?(\d{4}-\d\d-\d\dT[\d:.]+(?:Z|[+-]\d\d:\d\d))', text, re.I):
        try:
            times.append(datetime.fromisoformat(match[1].replace('Z', '+00:00')).timestamp())
        except ValueError:
            pass
    # Both weekly and short-window exhaustion may be reported together.
    return max((stamp for stamp in times if now < stamp < now + 32 * 86400), default=None)


class Events:
    def __init__(self):
        self.failures = []
        self.stderr = ''
        self.succeeded = False
        self.terminal_failure = False

    def line(self, line, stderr=False):
        if stderr:
            self.stderr = (self.stderr + line)[-65536:]
        try:
            event = json.loads(line)
        except ValueError:
            return
        if not isinstance(event, dict):
            return
        kind = event.get('type', '')
        failed = (kind in ('error', 'turn.failed') or
                  kind == 'end' and event.get('stopReason') not in ('end_turn', 'stop') or
                  kind == 'result' and (event.get('is_error') or event.get('status') in ('error', 'failed') or event.get('error')))
        success = kind == 'turn.completed' or kind in ('result', 'end') and not failed
        if failed:
            self.failures.append(event)
            self.failures = self.failures[-16:]
            self.terminal_failure = kind in ('turn.failed', 'result', 'end')
            self.succeeded = False
        elif success:
            self.succeeded = True
            self.terminal_failure = False
            self.failures.clear()  # A successfully recovered transient warning is not a failure.

    def outcome(self, returncode, now=None):
        now = time.time() if now is None else now
        if returncode == 0 and self.succeeded and not self.terminal_failure:
            return 'success', None
        text = json.dumps(self.failures) + '\n' + self.stderr
        reset = reset_time(self.failures, text, now)
        if QUOTA.search(text):
            return 'quota', reset
        if AUTH.search(text) or CONFIG.search(text) or returncode in (2, 42, 126, 127):
            return 'fatal', None
        if TRANSIENT.search(text):
            return 'transient', reset
        return 'unknown', None
