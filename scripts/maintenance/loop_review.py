#!/usr/bin/env python3
"""Read-only recap of recorded activity; recorded state is not proof of liveness."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parents[2]


def stamp(value):
    return datetime.fromtimestamp(value, timezone.utc).isoformat(timespec='seconds')


def read_rows(root, since):
    rows, seen = [], set()
    for path in (root / 'scripts/loop-codex').glob('*/routing.jsonl'):
        for line in path.read_text().splitlines():
            try:
                row = json.loads(line)
            except ValueError:
                continue
            start = row.get('started_at')
            key = (row.get('thread_id'), start)
            if isinstance(start, (int, float)) and start >= since and key not in seen:
                rows.append(row)
                seen.add(key)
    return sorted(rows, key=lambda r: r['started_at'])


def summarize(rows):
    daily = defaultdict(list)
    for row in rows:
        daily[stamp(row['started_at'])[:10]].append(row)
    counted = [r for r in rows if isinstance(
        r.get('accounting', {}).get('tokens', {}).get('input_tokens'), int)]
    def total(key):
        return sum(r['accounting']['tokens'].get(key, 0) or 0 for r in counted)
    gaps = []
    for previous, current in zip(rows, rows[1:]):
        end = previous['started_at'] + (previous.get('elapsed_seconds') or 0)
        hours = (current['started_at'] - end) / 3600
        if hours >= 3:
            gaps.append(dict(hours=round(hours, 2), after=stamp(end),
                             before=stamp(current['started_at']), previous_outcome=previous.get('outcome')))
    return dict(attempts=len(rows), problems=dict(Counter(r.get('problem') for r in rows)),
                execution=dict(Counter(r.get('outcome') for r in rows)),
                validation=dict(Counter(r.get('validation') for r in rows)),
                accepted_outcomes=dict(Counter(r.get('research_outcome') for r in rows
                                               if r.get('validation') == 'accepted')),
                models=dict(Counter((r.get('actual_model') or r.get('model') or '?') + '/' +
                                    (r.get('actual_effort') or r.get('effort') or '?') for r in rows)),
                tasks=dict(Counter(r.get('actual_task_type') for r in rows)),
                active_elapsed_hours=round(sum(r.get('elapsed_seconds') or 0 for r in rows)/3600, 2),
                daily={day: dict(attempts=len(values), execution=dict(Counter(r.get('outcome') for r in values)))
                       for day, values in sorted(daily.items())},
                accounting_samples=len(counted),
                cached_input_percent=round(100*total('cached_input_tokens')/max(1, total('input_tokens')), 2),
                median_startup_bytes=statistics.median(
                    [r['initial_prompt_bytes'] for r in counted if r.get('initial_prompt_bytes')])
                    if any(r.get('initial_prompt_bytes') for r in counted) else None,
                compactions=sum(r.get('accounting', {}).get('compactions', 0) for r in rows),
                gaps_over_three_hours=sorted(gaps, key=lambda g: -g['hours'])[:15],
                latest=[{k: r.get(k) for k in ('step_id', 'validation', 'evidence')} for r in rows[-8:]])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--days', type=float, default=14)
    parser.add_argument('--inventory', type=Path)
    args = parser.parse_args()
    if args.inventory:
        paths = [ROOT / p.decode() for p in args.inventory.read_bytes().split(b'\0') if p]
        sizes = [(p.stat().st_size, str(p.relative_to(ROOT))) for p in paths if p.is_file()]
        print(json.dumps(dict(files=len(sizes), bytes=sum(s for s, _ in sizes),
                              largest=sorted(sizes, reverse=True)[:20],
                              size_bands={label: dict(files=sum(lo <= size < hi for size, _ in sizes),
                                  bytes=sum(size for size, _ in sizes if lo <= size < hi))
                                  for label, lo, hi in [('under_1MB', 0, 1000000),
                                      ('1_to_10MB', 1000000, 10000000),
                                      ('10_to_100MB', 10000000, 100000000),
                                      ('100MB_plus', 100000000, float('inf'))]},
                              by_top_level=dict(Counter(p.split('/')[0] for _, p in sizes))), indent=2))
        return
    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=args.days)).timestamp()
    rows = read_rows(ROOT, since)
    result = dict(snapshot=now.isoformat(timespec='seconds'), since=stamp(since), **summarize(rows))
    state_path = ROOT / 'scripts/loop-codex/state.json'
    if state_path.exists():
        state = json.loads(state_path.read_text())
        result['recorded_state'] = {k: v for k, v in state.items() if k != 'problems'}
    log = ROOT / 'scripts/loop-codex/riemann/stdout.log'
    if log.exists():
        result['stdout_age_seconds'] = round(now.timestamp() - log.stat().st_mtime)
        lines = log.read_text().splitlines()
        result['latest_events'] = []
        for line in lines[-5:]:
            try:
                event = json.loads(line)
            except ValueError:
                continue
            item = event.get('item', {})
            result['latest_events'].append(dict(type=event.get('type'),
                item_type=item.get('type'), status=item.get('status'),
                detail=str(item.get('text', item.get('command', '')))[:500]))
    numeric = [r.get('accounting', {}).get('allowance_observation') for r in rows
               if (r.get('accounting', {}).get('allowance_observation') or {}).get('primary')]
    result['last_numeric_quota_observation'] = numeric[-1] if numeric else None
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
