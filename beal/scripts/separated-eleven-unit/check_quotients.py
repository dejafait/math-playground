"""Exact bounded quotient certificates; no complete S-unit generation claim."""
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path
from check_affine import M, F, norm, relative_norm, strip

BASE = Path(__file__).resolve().parent
def main():
    source_path = BASE/'affine-certificate.json'
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes)
    rows = source['all_tests']
    assert len(rows) == 1774 and source['field_k_ascending'] == M
    assert source['field_t_ascending'] == F
    assert len({tuple(r['abc']) for r in rows}) == 1774
    for r in rows:
        assert r['relative_norm_k_ascending'] == relative_norm(*r['abc'])
        assert norm(r['relative_norm_k_ascending'], M) == r['absolute_norm']
        assert r['absolute_norm'] == r['other_absolute_norm']
        assert strip(r['absolute_norm']) == (r['outside_support_factor'],
                                             r['exponents_2_11'])
    groups = {}
    for i, r in enumerate(rows):
        groups.setdefault(r['outside_support_factor'], []).append(i)
    pairs, tested = [], 0
    for i, j in combinations(range(len(rows)), 2):
        tested += 1
        if rows[i]['outside_support_factor'] == rows[j]['outside_support_factor']:
            pairs.append((i, j))
    assert tested == comb(1774, 2) == 1572651
    assert len(pairs) == sum(comb(len(g), 2) for g in groups.values())
    print(f'Norm screen: {tested} pairs, {len(pairs)} survivors', flush=True)
    # No quotient reaches support/norm-correction/valuation certification.
    # Preserve any future nonempty screen as a failure of this bounded replay,
    # rather than silently accepting an unchecked quotient.
    assert not pairs, 'A survivor requires a separate exact support certificate'
    summary = dict(pair_cap=1572651, actual_pairs=tested,
                   norm_screen_survivors=len(pairs),
                   localized_order_supported=0,
                   unresolved_support_or_valuation_pairs=[],
                   required_separating_witnesses=1,
                   certified_separating_witnesses=0, witnesses=[],
                   distinct_outside_factors=len(groups),
                   all_outside_factor_groups_singleton=all(len(v) == 1 for v in groups.values()),
                   arithmetic_failures=[], input_norms_replayed=1774)
    output = dict(source_sha256=hashlib.sha256(source_bytes).hexdigest(),
                  summary=summary,
                  outside_factor_partition=[dict(factor=k, indices=v) for k, v in groups.items()],
                  surviving_pairs=[],
                  qualification='Norm screen is necessary only; failed localized-order '
                  'support is unresolved, not proof of maximal-ring nonsupport.')
    path = BASE/'quotient-certificate.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('Certificate:', path.relative_to(BASE.parent.parent))


if __name__ == '__main__':
    main()
