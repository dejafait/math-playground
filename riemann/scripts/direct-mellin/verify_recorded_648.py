"""Exact-rational verification of every recorded cell and sign propagation.

This checks arithmetic in the saved enclosures, not the transcendental
backend's implementation; that contract and the analytic bounds are in L829.
"""
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
SOURCE = BASE/'fixed-laguerre-certificate-648.json'
OUT = BASE/'recorded-arithmetic-verification-648.json'


def pair(v):
    a,b = map(F,v)
    assert a <= b
    return a,b


def add(a,b):
    return a[0]+b[0], a[1]+b[1]


def mul(a,b):
    v = [x*y for x in a for y in b]
    return min(v),max(v)


def square(a):
    return (0 if a[0] <= 0 <= a[1] else min(x*x for x in a), max(x*x for x in a))


def contains(a,b):
    return a[0] <= b[0] <= b[1] <= a[1]


def main():
    cert = json.loads(SOURCE.read_text())
    result = dict(status='INCOMPLETE',failures=[],stages=[],
                  scope='Exact recorded-cell widths/sums and final propagation; exp backend and analytic bounds require their stated contracts',
                  source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    try:
        assert not cert['failures']
        program = BASE/'fixed_laguerre_648.py'
        assert hashlib.sha256(program.read_bytes()).hexdigest() == cert['program_sha256']
        for s in cert['stages']:
            n = s['boxes']
            h = F(21,n)
            q = s['quadrature']
            assert pair(q['width']) == (h,h)
            cells_path = ROOT/q['cells_path']
            assert hashlib.sha256(cells_path.read_bytes()).hexdigest() == q['cells_sha256']
            sums = [(F(0),F(0)) for _ in range(3)]
            count = 0
            with gzip.open(cells_path,'rt') as data:
                for k,line in enumerate(data):
                    c = json.loads(line)
                    assert c['k'] == k
                    assert pair(c['t']) == (F(-20)+k*h,F(-20)+(k+1)*h)
                    for j in range(3):
                        cell = pair(c['integrals'][j])
                        assert contains(cell,mul((h,h),pair(c['ranges'][j])))
                        sums[j] = add(sums[j],cell)
                    count += 1
            assert count == n
            totals = [pair(v) for v in q['integral_enclosures']]
            assert all(contains(totals[j],sums[j]) for j in range(3))
            b = s['bounds']
            js = [pair(v) for v in s['evaluation']['J']]
            for j in range(3):
                eps = F(b['theta_integrated_absolute_uppers'][j])+F(b['infinite_tail_absolute_upper'])
                assert contains(js[j],add(add(totals[j],pair(b['endpoint_enclosures'][j])),(-eps,eps)))
            assert js[0][0] > 0
            inverse = (1/js[0][1],1/js[0][0])
            r1,r2 = mul(js[1],inverse),mul(js[2],inverse)
            r1s = square(r1)
            variance = (r2[0]-r1s[1],r2[1]-r1s[0])
            p2 = square(pair(b['pi']))
            scalar = (p2[0]/2-4*variance[1],p2[1]/2-4*variance[0])
            reported = pair(s['evaluation']['scalar'])
            assert contains(reported,scalar)
            decision = ('NEGATIVE' if reported[1] < 0 else
                        'PASS_NECESSARY_ONLY' if reported[0] >= 0 else 'INCONCLUSIVE')
            assert decision == s['evaluation']['decision']
            assert all(c['passed'] for c in s['checks'])
            result['stages'].append(dict(boxes=n,all_cells_checked=count,
                                          exact_width_sums_and_propagation=True,
                                          scalar=s['evaluation']['scalar'],decision=decision))
        assert result['stages'][-1]['decision'] == cert['status'] == 'PASS_NECESSARY_ONLY'
        assert F('0.0548') < F(result['stages'][-1]['scalar'][0])
        assert F(result['stages'][-1]['scalar'][1]) < F('0.1226')
        result['status'] = 'PASS'
    except Exception as exc:
        result['failures'].append(type(exc).__name__+': '+str(exc))
        raise
    finally:
        OUT.write_text(json.dumps(result,indent=2)+'\n')
        print('Recorded arithmetic:',result['status'],'failures:',result['failures'],
              'certificate:',OUT.relative_to(ROOT))
        print('Required scalar threshold: 0; certified enclosing bounds: 0.0548, 0.1226')


if __name__ == '__main__':
    main()
