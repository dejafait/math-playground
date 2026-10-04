"""Best-effort command audit; not a sandbox or a shell parser."""
import json
import re
from pathlib import Path


def notebooks(cwd):
    try:
        rows = json.loads((Path(cwd).parent / 'scripts/loop/problems.json').read_text())
        if isinstance(rows, dict):
            rows = rows.get('problems', [])
        return [r['id'] for r in rows]
    except (OSError, ValueError, KeyError, TypeError):
        return []


def audit(arguments, active, slugs):
    """Store labels/counts only, never full commands or source contents."""
    text = arguments if isinstance(arguments, str) else json.dumps(arguments)
    siblings = [s for s in slugs if s != active and re.search(r'(?:\.\./|/)' + re.escape(s) + r'/', text)]
    read_command = bool(re.search(r'\b(?:cat|sed|rg|head|tail|read_text|read_bytes|open|glob)\b', text))
    broad = read_command and bool(re.search(r'\*/(?:PROGRESS|PROOF|GOAL)\.md|glob\([^\n]*\*/|\brg\b[^\n;]*\s\.\.(?:\s|["\x27)]|$)', text))
    orientation = {}
    if read_command:
        for name in ('GOAL.md', 'PROMPT.md', 'PROGRESS.md', 'PROOF.md', 'DAG.md'):
            count = len(re.findall(r'(?<![A-Za-z0-9_-])' + re.escape(name) + r'(?![A-Za-z0-9_-])', text))
            if count:
                orientation[name] = count
    return dict(sibling_notebooks=siblings if read_command else [], broad_read=bool(broad),
                orientation_read_mentions=orientation)
