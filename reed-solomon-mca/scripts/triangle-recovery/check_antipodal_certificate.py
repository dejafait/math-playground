"""Compare complete producer/replay summaries and recover the maximal fiber.

The packed certificate is checked row by row by the C++ replay. This
additional checker compares every assignment maximum and independently
recovers the displayed three-scalar fiber by seven-column moment inversion.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
from verify_fixed_union_table import invert, mul

ROOT = Path(__file__).parent
F = 97


def main():
    producer = json.loads((ROOT/'antipodal-anchor-sweep.json').read_text())
    replay = json.loads((ROOT/'antipodal-anchor-verification.json').read_text())
    fields = ('actual_pair_cases', 'required_pair_cases', 'actual_assignments',
              'required_assignments', 'actual_support_rows', 'required_support_rows',
              'certificate_bytes', 'maximum_isolated_disjoint_P',
              'required_four_anchor_threshold', 'row_counts', 'maximum_witness',
              'fiber_histogram', 'maximum_by_assignment', 'failures')
    for field in fields:
        assert producer[field] == replay[field], field
    assert replay['actual_assignments'] == len(replay['maximum_by_assignment']) == 30240
    assert max(replay['maximum_by_assignment']) == 3
    assert replay['all_eight_moment_tests'] == replay['row_counts'][4] == 15367752
    assert replay['zero_fourth_weight_rows_retained'] == 3568320
    assert not replay['failures']
    H = tuple(x for x in range(1,F) if pow(x,16,F)==1)
    witness = replay['maximum_witness']
    P = tuple(witness['P'])
    Y,Z,W = (tuple(witness['S_Y_Z_W'][i:i+2]) for i in (0,2,4))
    p,q,r = witness['weights']
    U = set(P+Y+Z+W)
    cx = {}
    for x in U:
        v = 1
        for h in H:
            if h not in U:
                v = v*(x-h) % F
        cx[x] = v
    moments = [[sum(cx[x]*pow(x,j,F) for x in pair) % F
                for j in range(1,9)] for pair in (Y,Z)]
    observed = []
    for K in combinations([x for x in H if x not in P],4):
        labels = (*K,*P)
        matrix = [[pow(x,j,F) for x in labels] for j in range(1,9)]
        inv = invert(matrix[:7])
        sy,sz = (mul(inv, m[:7]) for m in moments)
        ry,rz = [(m[7]-mul(matrix[7:],s)[0]) % F
                 for m,s in zip(moments,(sy,sz))]
        if not ry or not rz:
            continue  # The witness claim concerns isolated rows only.
        mu = rz*pow(ry,-1,F) % F
        if mu not in witness['scalars']:
            continue
        d = [(z-mu*y) % F for y,z in zip(sy[4:],sz[4:])]
        weights = ((1+d[0]*pow(cx[P[0]],-1,F))*pow(1+mu,-1,F) % F,
                   d[1]*pow(mu*cx[P[1]] % F,-1,F) % F,
                   -d[2]*pow(cx[P[2]],-1,F) % F)
        if weights != (p,q,r):
            continue
        omega = [(z-mu*y) % F for y,z in zip(sy[:4],sz[:4])]
        coeff = {x:-mu*cx[x] % F for x in Y}
        coeff.update({x:cx[x] for x in Z})
        coeff.update({P[0]:cx[P[0]]*(1-(1+mu)*p) % F,
                      P[1]:-mu*cx[P[1]]*q % F,P[2]:cx[P[2]]*r % F})
        residual = [(sum(v*pow(x,j,F) for x,v in zip(K,omega))-
                     sum(v*pow(x,j,F) for x,v in coeff.items())) % F
                    for j in range(1,9)]
        assert not any(residual)
        E = (2+mu) % F  # gamma=(0,1,2), g=1, rho=2, lambda=1.
        assert E and mu not in (0,96)
        T = 2*pow(E,-1,F) % F
        assert T not in (0,1,2)
        observed.append({'K':K,'mu':mu,'omega':omega,'full_weight':all(omega),
                         'residual8':residual,'E':E,'original_T':T,
                         'actual_weights':[v*pow(E,-1,F) % F for v in omega]})
    assert sorted(set(row['mu'] for row in observed)) == witness['scalars']
    assert len(observed) == 3 and all(row['full_weight'] for row in observed)
    packed = ROOT/'antipodal-anchor-rows.bin'
    digest = hashlib.file_digest(packed.open('rb'),'sha256').hexdigest()
    assert packed.stat().st_size == replay['certificate_bytes'] == 108108000
    result = {'compared_fields':fields,'complete_assignment_maxima_compared':30240,
              'packed_certificate_sha256':digest,'packed_certificate_bytes':108108000,
              'maximum_isolated_disjoint_P':3,'required_four_anchor_threshold':4,
              'witness':witness,'original_chart':{'gamma':[0,1,2],'lambda':1},
              'witness_rows':observed,'failures':[],
              'scope':'antipodal singleton pairs only; no arbitrary-pair triangle bound'}
    path = ROOT/'antipodal-anchor-summary-check.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('Complete summary comparison: 30240/30240 assignments; failures 0/0')
    print('Isolated maximum / required anchors: 3/4; three full witness rows recovered')
    print(f'Certificate: {path}')


if __name__ == '__main__':
    main()
