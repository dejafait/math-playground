"""One approved complete two-block census; no higher-row or recovery tests.

Reuse L109's direct block builder and L125's incremental elimination.
The separate verifier imports neither. Run from the notebook with python3.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import json

import zero_anchor_support_filter as direct
from new_pair_filter import eliminate

HERE = Path(__file__).resolve().parent
OUT = HERE / 'all-disjoint-pair-census'


def write(path, value):
    raw = (json.dumps(value, separators=(',', ':')) + '\n').encode()
    path.write_bytes(raw)
    return sha256(raw).hexdigest()


def run():
    OUT.mkdir(exist_ok=True)
    s, h, j = direct.S, direct.H, direct.J
    universe = list(product(combinations(s, 2), combinations(j, 2)))
    supports = [set(i + k) for i, k in universe]
    blocks = [direct.block(*key) for key in universe]
    # Direct unordered enumeration: no subgroup or coordinate symmetries.
    pairs = [(a, b) for a, b in combinations(range(len(universe)), 2)
             if supports[a].isdisjoint(supports[b])]
    required = comb(7, 2) * comb(5, 2) * comb(9, 2) * comb(7, 2) // 2
    assert len(universe) == len(set(universe)) == 756
    assert len(pairs) == len(set(pairs)) == required
    groups = {}
    for a, b in pairs:
        groups.setdefault((universe[a][0], universe[b][0]), []).append((a, b))
    summaries, ranks = [], Counter()
    vectors = residual_entries = 0
    bindings = [dict(name='L110', keys=[[[1, 8], [47, 50]],
                                     [[12, 18], [64, 70]]]),
                dict(name='L125', keys=[[[1, 8], [47, 50]],
                                     [[12, 18], [64, 75]]])]
    for binding in bindings:
        binding['pair'] = [universe.index((tuple(i), tuple(k)))
                           for i, k in binding['keys']]
    for number, (key, members) in enumerate(sorted(groups.items())):
        records, local = [], Counter()
        for a, b in members:
            stack = blocks[a]['matrix'] + blocks[b]['matrix']
            record = dict(pair=[a, b], **eliminate(stack))
            records.append(record)
            local[record['rank']] += 1
            vectors += len(record['kernel_basis'])
            residual_entries += sum(map(len, record['kernel_residuals']))
            for binding in bindings:
                if [a, b] == binding['pair']:
                    binding['record'] = record
                    binding['stack_sha256'] = sha256(
                        json.dumps(stack, separators=(',', ':')).encode()).hexdigest()
        path = OUT / f'batch-{number:03d}.json'
        digest = write(path, dict(overlap_pairs=key, records=records))
        summaries.append(dict(path=path.relative_to(HERE).as_posix(),
                              sha256=digest, count=len(records),
                              overlap_pairs=key, rank_histogram=dict(local)))
        ranks.update(local)
        if (number + 1) % 15 == 0:
            print(f'Producer checkpoint: {number + 1}/{len(groups)} batches', flush=True)
    assert all('record' in b for b in bindings)
    summary = dict(actual_pairs=len(pairs), required_pairs=required,
                   universe_size=len(universe), batches=len(summaries),
                   rank_histogram=dict(sorted(ranks.items())),
                   complete_kernel_vectors=vectors,
                   original_residual_entries=residual_entries,
                   exclusion_rank_required=21, failures=[])
    master = dict(modulus=97, H=h, S=s, J=j,
                  scope='All unordered disjoint two-overlap pairs; no higher-row gates',
                  column_pairs=[[s[a], s[b]] for a, b in direct.PAIRS],
                  universe=[[list(i), list(k)] for i, k in universe],
                  blocks=blocks, batches=summaries, prefix_bindings=bindings,
                  summary=summary)
    path = HERE / 'all-disjoint-pair-census.json'
    write(path, master)
    print(json.dumps(summary, sort_keys=True), flush=True)
    print(f'Full certificates: {path.relative_to(HERE.parent.parent)} and '
          f'{OUT.relative_to(HERE.parent.parent)}/batch-*.json', flush=True)


if __name__ == '__main__':
    run()
