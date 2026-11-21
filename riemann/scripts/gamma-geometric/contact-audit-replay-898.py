#!/usr/bin/env python3
"""Replay every certificate896 cell using a separate Fraction interval backend.

The inspected analytic formulas are reused from generator896. Arithmetic is
reimplemented using exact rational endpoint operations before dyadic rounding.
This is not an independent derivation of the analytic remainder estimates.
The original certificate and generator are never overwritten.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as R
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERATOR = HERE / 'contact-certificate-896.py'
CERTIFICATE = HERE / 'contact-certificate-896.json'
OUT = HERE / 'contact-audit-replay-898.json'
spec = importlib.util.spec_from_file_location('certificate896', GENERATOR)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
S = 2**512


class RationalInterval:
    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = int(lo), int(hi)
        else:
            v = R(lo)*S
            self.lo = v.__floor__()
            self.hi = v.__ceil__()
        assert self.lo <= self.hi

    @classmethod
    def hull(cls, values):
        values = [R(v)*S for v in values]
        return cls(min(values).__floor__(), max(values).__ceil__(), True)

    @classmethod
    def box(cls, a, b):
        assert a <= b
        return cls.hull([a, b])

    def ends(self):
        return (R(self.lo, S), R(self.hi, S))

    def __add__(self, other):
        other = lift(other)
        return self.hull([a+b for a in self.ends() for b in other.ends()])
    __radd__ = __add__

    def __neg__(self):
        return self.hull([-a for a in self.ends()])

    def __sub__(self, other):
        return self + -lift(other)

    def __rsub__(self, other):
        return lift(other) + -self

    def __mul__(self, other):
        other = lift(other)
        return self.hull([a*b for a in self.ends() for b in other.ends()])
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = lift(other)
        assert not other.lo <= 0 <= other.hi
        return self.hull([a/b for a in self.ends() for b in other.ends()])

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result, base = type(self)(1), self
        while n:
            if n % 2:
                result = result*base
            n //= 2
            if n:
                base = base*base
        return result

    def scale(self, r):
        return self.hull([a*R(r) for a in self.ends()])

    def sqrt(self):
        assert self.lo >= 0
        lower = isqrt(self.lo*S)
        upper = isqrt(self.hi*S)
        if upper**2 != self.hi*S:
            upper += 1
        assert lower**2 <= self.lo*S < (lower+1)**2
        assert (upper == 0 or (upper-1)**2 < self.hi*S) and self.hi*S <= upper**2
        return type(self)(lower, upper, True)

    def data(self):
        return [str(self.lo), str(self.hi)]


def lift(x):
    return x if isinstance(x, RationalInterval) else RationalInterval(x)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source = json.loads(CERTIFICATE.read_text())
    assert source['bits'] == 512 and source['order'] == 16
    assert source['exponential_terms'] == 48 and source['large_argument_terms'] == 160
    assert source['status'] == 'COMPACT_CERTIFIED_ENDPOINT_JOIN_OPEN'
    assert len(source['segments']) == 2 and len(source['endpoints']) == 2
    g.I = RationalInterval
    g.lift = lift
    output = {'status':'IN_PROGRESS', 'bits':512,
              'scope':'All saved cells and endpoints replayed with an independent Fraction arithmetic backend; inspected analytic formulas reused from generator896.',
              'generator_sha256':sha(GENERATOR), 'certificate_sha256':sha(CERTIFICATE),
              'ledger_sha256':sha(HERE / 'contact-certificate-ledger-check-896.json'),
              'segments':[], 'endpoints':[], 'failures':[]}

    def save():
        OUT.write_text(json.dumps(output, indent=2)+'\n')

    save()
    try:
        for old, x, lo, hi in zip(source['endpoints'], [R(139,32), R(35,8)],
                                  [R(5694,10**9), R(-2495,10**9)],
                                  [R(5695,10**9), R(-2494,10**9)]):
            assert R(old['x']) == x
            f,z,zp = g.evaluate(g.center_jets(x)[:6])
            row = {'x':str(x), 'F':f.data(), 'Z':z.data(), 'Zprime':zp.data()}
            assert all(row[k] == old[k] for k in row)
            assert lo < R(z.lo,S) <= R(z.hi,S) < hi
            row['identical_to_saved'] = True
            output['endpoints'].append(row)
        save()
        count = 0
        for oldseg, left, right, mode in zip(source['segments'],
                [R(139,32),R(1,32)], [R(35,8),R(139,32)], ['decreasing','positive']):
            assert oldseg['interval'] == [str(left),str(right)] and oldseg['mode'] == mode
            assert oldseg['complete'] and not oldseg['failures'] and not oldseg['unprocessed']
            seg = {'interval':[str(left),str(right)], 'mode':mode, 'complete':False,'cells':[]}
            output['segments'].append(seg)
            cursor = left
            for old in oldseg['cells']:
                a,b = R(old['left']),R(old['right'])
                assert a == cursor and a < b
                c,delta = (a+b)/2,(b-a)/2
                assert delta <= c/256
                tilt,jets = g.tilt_jets(g.center_jets(c))
                q = g.cell_jets(c,delta,jets,tilt)
                f,z,zp = g.evaluate(q)
                assert q[0].lo > 0
                row = {'left':str(a),'right':str(b),'tilt':str(tilt),
                       'Q_tilt':q[0].data(),'F':f.data(),'Z':z.data(),'Zprime':zp.data()}
                assert all(row[k] == old[k] for k in row)
                if mode == 'positive':
                    assert R(z.lo,S) > R(1,4000000)
                else:
                    assert R(zp.hi,S) < R(-213,1000000) < R(-1,5000)
                row['identical_to_saved'] = True
                row['threshold_passed'] = True
                seg['cells'].append(row)
                cursor = b
                count += 1
                if count % 20 == 0:
                    save()
                    print('Replayed',count,'cells; all exact matches; through',b,flush=True)
            assert cursor == right and seg['cells']
            seg['complete'] = True
            save()
        zmin = min(int(c['Z'][0]) for c in output['segments'][1]['cells'])
        zpmax = max(int(c['Zprime'][1]) for c in output['segments'][0]['cells'])
        assert str(zmin) == source['summary']['minimum_prefix_Z_lower']
        assert str(zpmax) == source['summary']['maximum_contact_Zprime_upper']
        ledger = json.loads((HERE / 'contact-certificate-ledger-check-896.json').read_text())
        assert ledger['status'] == 'PASS' and ledger['certificate_sha256'] == sha(CERTIFICATE)
        assert all(s['all_cells_checked'] and not s['failures'] for s in ledger['checked'])
        assert [s['cells'] for s in ledger['checked']] == [len(s['cells']) for s in output['segments']]
        output['summary'] = {'cells_replayed':count, 'all_exact_matches':True,
            'minimum_prefix_Z_lower':str(zmin), 'maximum_contact_Zprime_upper':str(zpmax),
            'actual_prefix_bound':'>1/4000000', 'required_prefix_bound':'>0',
            'actual_contact_bound':'<-213/1000000', 'required_contact_bound':'<-1/5000',
            'endpoint_enclosures':['(5694,5695)/1e9','(-2495,-2494)/1e9'],
            'analytic_endpoint_join':'Requires C466d(30)-(39), checked separately in audit898.',
            'actual_Xi_transfer':False}
        output['status'] = 'PASS'
    except Exception as exc:
        output['status'] = 'FAILED'
        output['failures'].append({'type':type(exc).__name__,'message':str(exc)})
        save()
        raise
    save()
    print('PASS:',count,'cells and both endpoints; all exact interval matches.')
    print('Actual prefix Z > 1/4000000; required > 0.')
    print('Actual contact Zprime < -213/1000000; required < -1/5000.')
    print('Failures: none. Full replay:', OUT)


if __name__ == '__main__':
    main()
