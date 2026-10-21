"""All-entry spatial and full coverage/aggregation audit of the L134 E enclosure.

Recomputes all added moments and new integer spatial entries. Tensor
BLAS inclusion relies on L039's arithmetic induction, not an independent
processor proof. Exact dyadic aggregation checks every signed term.
"""
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import numpy as np
import enclose_e_heat_forms as ph

ROOT = Path(__file__).parent
en, rat, sr = ph.en, ph.rat, ph.sr


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    path = ROOT/'e-heat-enclosure-certificate.json'
    data = json.loads(path.read_text())
    source_path = ROOT/data['moment_source']
    source = json.loads(source_path.read_text())
    assert data['moment_source_sha256'] == sha(source_path)
    assert data['script_sha256'] == sha(Path(ph.__file__))
    old_factor = ROOT/source['factor_archive']
    assert data['imported_factor_sha256'] == source['factor_archive_sha256'] == sha(old_factor)
    assert data['template_source_sha256'] == sha(ROOT/data['template_source'])
    assert (data['K'], int(data['scale'])) == (96, ph.S)
    assert not data['failures'] and not source['failures']
    saved_path = ROOT/'stored-fourier-enclosure-certificate.json'
    assert source['input_sha256'] == sha(saved_path)
    spatial = ph.Spatial(source)
    assert data['cumulative_source_sha256'] == sha(ROOT/data['cumulative_source'])
    old_h = json.loads((ROOT/'physical-h-enclosure-certificate.json').read_text())
    assert old_h['script_sha256'] == sha(Path(ph.ph.__file__))
    assert source['script_sha256'] == sha(Path(en.__file__))
    factor_path = ROOT/data['factor_archive']
    assert data['factor_archive_sha256'] == sha(factor_path)
    archive, old = np.load(factor_path), np.load(old_factor)
    keys, M, Q = ph.templates()
    assert [row['key'] for row in data['spatial_matrices']] == json.loads(json.dumps(keys))
    assert len(keys) == 30
    expected_names = {f'spatial_{j}_{part}' for j in range(30) for part in ('c', 'r')}
    expected_names |= {'heat_c','heat_r','weights_c','weights_r'}
    assert set(archive.files) == expected_names
    for name in archive.files:
        assert np.all(np.isfinite(archive[name]))
        if name.endswith('_r'):
            assert np.all(archive[name] >= 0)
    for name in ('heat_c','heat_r','weights_c','weights_r'):
        assert np.array_equal(archive[name], old[name])

    matrix_audit, total_entries = [], 0
    indices = {'E': range(97), 'V': range(1,97)}
    for ix, (left, weight, right, ell) in enumerate(keys):
        center, radius = archive[f'spatial_{ix}_c'], archive[f'spatial_{ix}_r']
        rows, cols = len(indices[left[0]]), len(indices[right[0]])
        assert center.shape == radius.shape == (rows, cols)
        assert (data['spatial_matrices'][ix]['rows'], data['spatial_matrices'][ix]['cols']) == (rows,cols)
        assert data['spatial_matrices'][ix]['max_radius_hex'] == float(np.max(radius)).hex()
        for ni, n in enumerate(indices[left[0]]):
            for mi, m in enumerate(indices[right[0]]):
                z = spatial.entry(left, weight, right, ell, n, m)
                c, r = F(float(center[ni,mi])), F(float(radius[ni,mi]))
                assert c-r <= F(z.lo, ph.S) <= F(z.hi, ph.S) <= c+r
        total_entries += rows*cols
        matrix_audit.append(dict(index=ix, entries=rows*cols, containment='PASS'))
        if (ix+1) % 5 == 0:
            print(f'Audited all entries of spatial matrices {ix+1}/30', flush=True)
    assert data['used_moments'] == [list(k) for k in sorted(spatial.used)]
    assert data['used_cumulative_moments'] == [list(k) for k in sorted(spatial.used_cumulative)]

    # Independent constant-prefix integral formulas; no derivative-mode shortcut.
    p0 = ('E','prefix')
    f0,f1,f2,f3 = (spatial.moments[h,0][0] for h in range(4))
    explicit = {'R': rat(F(56,3))*f0-f2/rat(2),
                'f': (f3+rat(8)*f2+rat(16)*f1)/rat(8),
                'fp': -(f2+rat(4)*f1)/rat(4)}
    for weight,expected in explicit.items():
        actual = spatial.entry(p0,weight,p0,False,0,0)
        difference = actual-expected
        assert difference.lo <= 0 <= difference.hi

    # Unchanged full-probe Q, matched by actual keys rather than matrix IDs.
    old_keys = [r['key'] for r in old_h['spatial_matrices']]
    for probe,rows in Q.items():
        actual = [[a,b,str(c),[json.loads(json.dumps(keys[x])) for x in mm]] for a,b,c,mm in rows]
        expected = [[a,b,c,[old_keys[x] for x in mm]] for a,b,c,mm in old_h['tensors'][f'Q_{probe}']]
        assert actual == expected
    assert {name:len(rows) for name,rows in M.items()} == {'U':12,'W':12}
    assert {probe:len(rows) for probe,rows in Q.items()} == {3:48,6:192}
    actual_templates = {label: [[a,b,str(c),mm] for a,b,c,mm in rows]
                        for label,rows in [(f'M_{s}',r) for s,r in M.items()]
                        + [(f'Q_{i}',r) for i,r in Q.items()]}
    assert data['tensors'] == actual_templates
    expected_terms, expected_features = set(), set()
    types = lambda a: tuple('E' if j == a else 'V' for j in range(4))
    for probe in (3,6):
        for name, rows in M.items():
            for im,(a,b,c,mm) in enumerate(rows):
                for iq,(qa,qb,cq,qq) in enumerate(Q[probe]):
                    if (qa,qb) != (b,a):
                        continue
                    expected_terms.add((probe,name,im,iq,c*cq))
                    expected_features.update((mid,qid,types(a)[j],types(b)[j])
                                             for j,(mid,qid) in enumerate(zip(mm,qq)))
    actual_terms = {(r['probe'],r['tensor'],r['M'],r['Q'],F(r['coefficient'])) for r in data['tensor_terms']}
    assert actual_terms == expected_terms and len(actual_terms) == len(data['tensor_terms']) == 384
    actual_features = {(r['M_matrix'],r['Q_matrix'],r['left_type'],r['right_type']) for r in data['coordinate_features']}
    assert actual_features == expected_features and len(actual_features) == len(data['coordinate_features']) == len(expected_features)

    m=28
    rq=F(factorial(m)**4,(2*m+1)*factorial(2*m)**3)*(1+22*factorial(2*m+1))
    rt=en.ar.exp_negative(rat(108)).absolute_upper()
    rel=rq+rt
    assert ph.fraction(data['relative_time_error']) == rel
    partial=sum((F(3**j,factorial(j)) for j in range(9)),F(0))
    assert partial>20
    tail=2*(4*12**4)*(16*12**3)*F(512,9*96)/20**27
    counts={(3,'U'):48,(3,'W'):48,(6,'U'):144,(6,'W'):144}
    assert Counter((r['probe'],r['tensor']) for r in data['tensor_terms']) == counts
    table, results = {}, []
    for row in data['results']:
        key = row['probe'],row['tensor']
        assert key not in table
        table[key]=row
        terms=[r for r in data['tensor_terms'] if (r['probe'],r['tensor'])==key]
        assert len(terms) == row['terms'] == counts[key]
        ll=hh=F(0)
        for term in terms:
            c,r=(F(float.fromhex(term['integral'][key])) for key in ('center_hex','radius_hex'))
            assert r>=0
            ll+=c-r; hh+=c+r
        c,r=(F(float.fromhex(row['retained'][key])) for key in ('center_hex','radius_hex'))
        assert c-r<=ll<=hh<=c+r
        probe,name=key
        te=ph.AMPLITUDE[name]*ph.NORM[probe]*(4*12**4)**2*(2*rel+rel*rel)
        st=ph.AMPLITUDE[name]*ph.NORM[probe]*tail
        error=r+te+st
        assert ph.fraction(row['time_error'])==te and ph.fraction(row['spectral_tail'])==st
        assert st<F(5,10**11) and ph.fraction(row['total_error'])==error<1
        assert error < F(309,10**9)
        assert ph.fraction(row['lower'])==c-error and ph.fraction(row['upper'])==c+error
        # Outward tenths for a readable conclusion, compared in exact rationals.
        lower=F((10*(c-error)).numerator//(10*(c-error)).denominator,10)
        upper=F(-((-10*(c+error)).numerator//(-10*(c+error)).denominator),10)
        assert lower<c-error<c+error<upper
        results.append(dict(probe=probe,tensor=name,lower_decimal=str(float(lower)),upper_decimal=str(float(upper)),
                            total_error_upper_decimal=sr.display(error,12)))
    assert set(table)==set(counts)
    bounds={'U':(F(-903,1000),F(-871,1000)), 'W':(F(-178,1000),F(-143,1000))}
    combined=[]
    for row in data['combined']:
        probe=row['probe']; lo=hi=F(0)
        for name,(sl,sh) in bounds.items():
            ll,hh=(ph.fraction(table[probe,name][key]) for key in ('lower','upper'))
            ends=[ll*sl,ll*sh,hh*sl,hh*sh]
            lo+=min(ends); hi+=max(ends)
        assert ph.fraction(row['lower'])==lo and ph.fraction(row['upper'])==hi
        sign='positive' if lo>0 else ('negative' if hi<0 else 'unresolved')
        assert sign==row['sign']
        coarse = (-5184,-4342) if probe == 3 else (471,702)
        assert F(coarse[0]) < lo < hi < F(coarse[1])
        combined.append(dict(probe=probe,lower=en.rational(lo),upper=en.rational(hi),
                             containing_interval=list(coarse),sign=sign))
    out=dict(status='PASS',certificate_sha256=sha(path),matrix_entries=total_entries,
             matrix_checks=matrix_audit,cumulative_moments=len(spatial.cumulative),constant_prefix_IBP_checks=3,
             coordinate_features=len(expected_features),tensor_terms=384,results=results,combined=combined,failures=[],
             qualifications=['Replayed every cumulative moment and new integer spatial entry; checked all dyadic containments and signed aggregation.',
                             'L082 primitive inputs are imported, not independently rederived.',
                             'Tensor BLAS inclusion relies on L039 qualified IEEE induction, not a second processor/tensor verification.'])
    outpath=ROOT/'e-heat-enclosure-audit.json'
    outpath.write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS: {total_entries} spatial entries, 579 cumulative moments, 3 constant-prefix identities, 384 signed terms; failures 0; full audit {outpath}',flush=True)
    for r in results:
        print(f'Probe {r["probe"]} {r["tensor"]}: ({r["lower_decimal"]}, {r["upper_decimal"]}), total error <= {r["total_error_upper_decimal"]}, required <1',flush=True)


if __name__=='__main__':
    main()
