"""All-record audit of L082 inputs/coverage/aggregation; no second BLAS proof.

Recompute new moments, exact rules and all heat enclosures. Spatial matrix
and tensor inclusion still rely on the generator's arithmetic induction.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import enclose_continuum_first_pair as en

I, S, rat, sr, sw, ar = en.I, en.S, en.rat, en.sr, en.sw, en.ar
ROOT = Path(__file__).parent


def main():
    path = ROOT/'continuum-first-pair-enclosure-certificate.json'
    d = json.loads(path.read_text())
    source = ROOT/'stored-fourier-enclosure-certificate.json'
    saved = json.loads(source.read_text())
    assert d['input_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert d['script_sha256'] == hashlib.sha256(Path(en.__file__).read_bytes()).hexdigest()
    assert (d['K'], d['degree'], int(d['scale'])) == (96,28,S)
    pi, omega = en.read(d['pi']), en.read(d['pi'])/rat(8)
    expected_pi = rat(16)*sw.arctan_enclosure(F(1,5))-rat(4)*sw.arctan_enclosure(F(1,239))
    assert pi.lo <= expected_pi.lo <= expected_pi.hi <= pi.hi
    zero = en.read(d['zero_norm']); assert 8*zero.lo**2 <= S*S < 8*zero.hi**2
    table = {(r['h'],r['n']):r for r in d['moments']}
    assert len(table) == len(d['moments']) == 1156
    expected_keys = {(h,n) for h in (0,1) for n in range(-192,193)} | {(h,n) for h in (2,3) for n in range(-96,97)}
    assert set(table) == expected_keys
    for row in saved['transforms']:
        h,n = row['h'],row['n']
        if abs(n)>192: continue
        eps = rat({0:F(1565,10**16),1:F(3333,10**16)}[h]).hi
        for key,out in [('stored_real_hex','real'),('stored_imag_hex','imag')]:
            z = rat(F(float.fromhex(row[key]))); actual = en.read(table[h,n][out])
            assert actual.lo <= z.lo-eps <= z.hi+eps <= actual.hi
    nodes = [(en.read(z['x']),en.read(z['weight'])*en.read(z['rho'])) for p in saved['positive_panels'] for z in p['nodes']]
    eps = F(348,10**16); dt,dc = F(2*3**36,3*4**84),F(2*3**179,3*4**284)
    for n in range(97):
        vals = {2:rat(0),3:rat(0)}
        for x,wr in nodes:
            si,co = sw.sin_cos(rat(n)*omega*x)
            xx=x*x
            vals[2] = vals[2]+rat(2)*wr*xx*co
            vals[3] = vals[3]+rat(2)*wr*xx*x*si
        for h in (2,3):
            allowance = 2*3**h*(eps+(1+eps)*dt)+10*F(5,2)**h*dc
            er = rat(allowance).hi; v = I(vals[h].lo-er,vals[h].hi+er)
            for signed in ((0,) if n==0 else (n,-n)):
                rr,ii = (v,rat(0)) if h==2 else (rat(0),v if signed>=0 else -v)
                for key,z in [('real',rr),('imag',ii)]:
                    actual = en.read(table[h,signed][key])
                    assert actual.lo <= z.lo <= z.hi <= actual.hi
        if n%48 == 0: print(f'Audited all new moments through {n}/96',flush=True)
    sw.DEGREE = 28
    roots,weights = [],[]
    for row in d['roots']:
        z,w = en.read(row['root']),en.read(row['weight'])
        assert sw.sign_at(z.lo) != sw.sign_at(z.hi)
        assert not roots or roots[-1].hi < z.lo
        p,pm = sw.legendre(z); dp=rat(28)*(pm-z*p)/(rat(1)-z*z)
        expected = rat(2)/((rat(1)-z*z)*dp*dp)
        assert w.lo <= expected.lo <= expected.hi <= w.hi and w.lo>0
        roots.append(z); weights.append(w)
    assert len(roots) == 28
    panels = [(F(0),F(1,2**14))]+[(F(2)**j,F(2)**(j+1)) for j in range(-14,8)]
    assert len(d['mapped_rule']) == 644 and len(d['heat']) == 644
    archive_path = ROOT/d['factor_archive']
    assert d['factor_archive_sha256'] == hashlib.sha256(archive_path.read_bytes()).hexdigest()
    archive = np.load(archive_path)
    assert len(d['spatial_keys']) == 26
    for name in archive.files:
        arr=archive[name]; assert np.all(np.isfinite(arr))
        if name.endswith('_r'): assert np.all(arr>=0)
    assert set(archive.files) == {f'spatial_{j}_{side}' for j in range(26) for side in ('c','r')} | {'heat_c','heat_r','weights_c','weights_r'}
    for ix,row in enumerate(d['mapped_rule']):
        ip,ir = divmod(ix,28); a,b=panels[ip]
        assert (row['panel'],row['root']) == (ip,ir)
        t = rat(F(1,16)+(a+b)/2)+rat((b-a)/2)*roots[ir]
        w = rat((b-a)/2)*weights[ir]
        for key,z in [('time',t),('weight',w)]:
            actual=en.read(row[key]); assert actual.lo<=z.lo<=z.hi<=actual.hi
        assert tuple(sr.midpoint_radius(en.read(row['weight']))) == (archive['weights_c'][ix],archive['weights_r'][ix])
        assert len(d['heat'][ix]) == 97
        for n,record in enumerate(d['heat'][ix]):
            expected=ar.exp_negative(t*(omega*omega*rat(n*n))); actual=en.read(record)
            assert actual.lo<=expected.lo<=expected.hi<=actual.hi
            assert tuple(sr.midpoint_radius(actual)) == (archive['heat_c'][ix,n],archive['heat_r'][ix,n])
        if ix%161 == 0: print(f'Audited rule and all heat inputs through row {ix}/644',flush=True)
    terms=d['component_terms']; assert [len(terms[k]) for k in ('M','Q3','Q6')] == [12,24,96]
    expected_pairs=set()
    for probe in (3,6):
        for im,(a,b,c) in enumerate(terms['M']):
            for iq,(qa,qb,cq) in enumerate(terms[f'Q{probe}']):
                if (qa,qb)==(b,a): expected_pairs.add((probe,im,iq,F(c)*F(cq)))
    actual_pairs={(r['probe'],r['M'],r['Q'],F(r['coefficient'])) for r in d['tensor_terms']}
    assert actual_pairs==expected_pairs and len(d['tensor_terms'])==len(actual_pairs)==100
    def frac(z): return F(int(z['numerator']),int(z['denominator']))
    m=28
    from math import factorial
    rq=F(factorial(m)**4,(2*m+1)*factorial(2*m)**3)*(1+22*factorial(2*m+1))
    rt=ar.exp_negative(rat(108)).absolute_upper()
    assert frac(d['relative_quadrature_error'])==rq and frac(d['relative_time_tail'])==rt
    results=[]
    for row in d['results']:
        probe=row['probe']; vals=[r for r in d['tensor_terms'] if r['probe']==probe]
        assert len(vals)==row['terms']=={3:28,6:72}[probe]
        lo=hi=F(0)
        for v in vals:
            c,r=(F(float.fromhex(v['integral'][key])) for key in ('center_hex','radius_hex'))
            assert r>=0; lo+=c-r; hi+=c+r
        c,r=(F(float.fromhex(row['retained'][key])) for key in ('center_hex','radius_hex'))
        assert c-r<=lo<=hi<=c+r
        rel=rq+rt; te=F(1296*1155*3,32)*{3:3025,6:820368}[probe]*(4*12**4)**2*(2*rel+rel*rel)
        error=r+te+F(4,10**15)
        assert frac(row['time_error'])==te and frac(row['total_error'])==error
        assert frac(row['lower'])==c-error and frac(row['upper'])==c+error<0 and error<1
        results.append(dict(probe=probe,lower=en.rational(c-error),upper=en.rational(c+error),total_error=en.rational(error)))
    assert not d['failures'] and len(results)==2
    out=dict(status='PASS',certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),moments=1156,
             spatial_matrices=26,rule_nodes=644,heat_entries=644*97,tensor_terms=100,results=results,failures=[],
             qualification='Recomputed every new moment, rule/heat enclosure and aggregate. Matrix/tensor multiplication inclusion relies on generator induction under L039 IEEE model; not independently rerun.')
    outpath=ROOT/'continuum-first-pair-enclosure-audit.json';outpath.write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS; all input and aggregation records audited; failures 0; full audit {outpath}',flush=True)


if __name__=='__main__': main()
