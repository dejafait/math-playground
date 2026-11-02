#!/usr/bin/env python3
"""Reconstruct observed allowance counters, not invoices or exact quota costs."""
import argparse
import csv
import json
from pathlib import Path


def segment(points):
    """A changed plan/deadline starts an observed episode, not a proven reset."""
    groups = []
    for point in sorted(points, key=lambda p: p['time']):
        previous = groups[-1][-1] if groups else None
        if (previous is None or point['plan'] != previous['plan']
                or point['minutes'] != previous['minutes']
                or abs(point['reset'] - previous['reset']) > 120
                or point['used'] < previous['used'] - 5):
            groups.append([])
        groups[-1].append(point)
    return groups


def reconstruct(root):
    points, stops, seen = [], [], set()
    malformed = 0
    for path in sorted((root / 'scripts/loop-codex').glob('*/routing.jsonl')):
        for line in path.read_text().splitlines():
            try:
                row = json.loads(line)
            except ValueError:
                malformed += 1
                continue
            started = row.get('started_at')
            if not isinstance(started, (float, int)):
                continue
            key = (row.get('thread_id'), started)
            if key in seen:
                continue
            seen.add(key)
            timestamp = started + (row.get('elapsed_seconds') or 0)
            observation = row.get('accounting', {}).get('allowance_observation') or {}
            if row.get('outcome') == 'quota':
                stops.append({'time': round(timestamp), 'limit': observation.get('limit_id')})
            primary = observation.get('primary') or {}
            used, reset = primary.get('used_percent'), primary.get('resets_at')
            if not isinstance(used, (float, int)) or not isinstance(reset, (float, int)):
                continue
            if not 0 <= used <= 100:
                continue
            points.append(dict(time=round(timestamp), used=used, reset=reset,
                               minutes=primary.get('window_minutes'),
                               plan=observation.get('plan_type')))
    groups = segment(points)
    episodes, plot = [], []
    for index, group in enumerate(groups):
        episodes.append(dict(index=index, start=group[0]['time'], end=group[-1]['time'],
                             first_used=group[0]['used'], last_used=group[-1]['used'],
                             max_used=max(p['used'] for p in group), plan=group[-1]['plan'],
                             reset=group[-1]['reset'], minutes=group[-1]['minutes'],
                             samples=len(group)))
        # Keep percentage changes, episode endpoints and at least hourly samples.
        last = None
        for j, point in enumerate(group):
            if (last is None or point['used'] != last['used']
                    or point['time'] - last['time'] >= 3600 or j == len(group) - 1):
                plot.append([point['time'], point['used'], index])
                last = point
    return dict(episodes=episodes, points=plot, stops=sorted(stops, key=lambda p: p['time']),
                samples=len(points), malformed=malformed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output or args.root / '.generated/subscription-history'
    document = reconstruct(args.root)
    if not document['points']:
        parser.error('No numeric allowance observations found.')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'quota-history.json').write_text(json.dumps(document, indent=2) + '\n')
    with (output / 'quota-episodes.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(document['episodes'][0]))
        writer.writeheader()
        writer.writerows(document['episodes'])
    template = Path(__file__).with_name('quota-history.html').read_text()
    assert template.count('/*QUOTA_DATA*/null') == 1
    (output / 'quota-history.html').write_text(
        template.replace('/*QUOTA_DATA*/null', json.dumps(document, separators=(',', ':'))))
    print(f"{document['samples']} samples; {len(document['episodes'])} observed counter episodes")
    print(output / 'quota-history.html')


if __name__ == '__main__':
    main()
