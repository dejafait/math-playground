"""Ordered notebook registry and restart-safe, per-problem scheduling state."""
import json
import re

RESEARCH_KEYS = ('no_progress', 'exploration_turns', 'stalled_turns',
                 'research_step_id', 'research_outcome', 'research_halt', 'unknowns')


def registry(root):
    rows = json.loads((root / 'scripts/loop/problems.json').read_text())
    if not isinstance(rows, list) or not rows:
        raise RuntimeError('Problem registry must be a nonempty list.')
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError('Every registry entry must be an object.')
        slug = row.get('id', '')
        if not isinstance(slug, str) or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in seen:
            raise RuntimeError('Invalid or duplicate problem ID.')
        seen.add(slug)
        if type(row.get('enabled')) is not bool:
            raise RuntimeError('Every problem requires a boolean enabled field.')
        directory = root / slug
        if directory.resolve().parent != root.resolve():
            raise RuntimeError('Problem directory must be directly inside the repository.')
        for name in ('GOAL.md', 'PROGRESS.md', 'PROOF.md', 'DAG.md'):
            if not (directory / name).is_file():
                raise RuntimeError(f'Missing {slug}/{name}.')
    return rows


def migrate(state):
    """Keep quota fields global; preserve legacy RH research state once."""
    if 'problems' not in state:
        state['problems'] = {'riemann': {k: state.pop(k) for k in RESEARCH_KEYS if k in state}}
    if not isinstance(state['problems'], dict):
        raise RuntimeError('Invalid per-problem state.')
    for local in state['problems'].values():
        if not isinstance(local, dict):
            raise RuntimeError('Invalid per-problem counters.')
        for key in ('no_progress', 'exploration_turns', 'stalled_turns', 'unknowns', 'turns', 'elapsed_seconds'):
            value = local.get(key, 0)
            if not isinstance(value, (int, float)) or not 0 <= value < 1e12:
                raise RuntimeError('Invalid per-problem numeric field.')
    state.setdefault('next_problem', 'riemann')
    return state


def choose(rows, state, resolved, only=None):
    ids = [row['id'] for row in rows]
    start = ids.index(state['next_problem']) if state.get('next_problem') in ids else 0
    for offset in range(len(ids)):
        i = (start + offset) % len(ids)
        slug = ids[i]
        if only and slug != only:
            continue
        if (rows[i]['enabled'] and not state['problems'].get(slug, {}).get('research_halt')
                and not resolved(slug)):
            return slug, ids[(i + 1) % len(ids)]
    return None, None
