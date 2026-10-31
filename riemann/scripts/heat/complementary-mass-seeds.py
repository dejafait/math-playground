#!/usr/bin/env python3
"""Outward rescaling of the complete L497 input ledger; no floating math."""
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json
import struct

ROOT = Path(__file__).resolve().parent
Q = 1 << 56
NAME = 'complementary-mass'


def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('prefix_intervals', ROOT/'finite-prefix-certificate.py')
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    cert = json.loads((ROOT/'finite-prefix-certificate.json').read_text())
    initial = ROOT/'finite-prefix-certificate-initial.tsv.gz'
    expected = next(e['sha256'] for e in cert['evidence'] if e['path'] == initial.name)
    assert sha(initial) == expected
    assert cert['scalars']['N'] == 691004 and not cert['failures']
    assert F(2, 3**71)*F(9, 71*8) < F(1, lib.Q)
    import math
    assert F(1, 2**27*math.factorial(27))*F(56,55) < F(1, lib.Q)
    ell = F('24.18022820120389')
    # exp(ell/2) is the reciprocal of exp(-ell/2). The latter's
    # scaled positive argument ell/64 is <1/2, as required by L497.
    assert ell/64 < F(1, 2)
    eh = lib.reciprocal(lib.exp_negative(lib.point(-ell/2)))
    e = lib.mul(eh, eh)
    Tfloor = e[0]//lib.Q
    assert e[1]//lib.Q == Tfloor and 160*691004 < Tfloor
    factor = lib.point(2/ell)
    def rescale(a):
        lo, hi = map(int, a)
        assert 0 <= lo <= hi
        return lo*Q//lib.Q, -((-hi*Q)//lib.Q)
    primes = [s['p'] for s in cert['computation']['stages']]
    assert len(primes) == 63 and primes[-1] == 307
    radii = {}
    path = ROOT/(NAME+'-seeds.bin')
    with gzip.open(initial, 'rt') as f, path.open('wb') as out:
        assert f.readline().strip() == 'n\tlog_lower\tlog_upper\ta_lower\ta_upper'
        count = 0
        for line in f:
            n, ll, lh, al, ah = map(int, line.split())
            count += 1
            assert n == count
            a, logn = rescale((al, ah)), rescale((ll, lh))
            out.write(struct.pack('<qqqq', *a, *logn))
            if n in primes:
                radii[n] = (*a, *logn)
        assert count == 691004
    config = ROOT/(NAME+'-config.txt')
    fac = rescale(factor)
    config.write_text(f'{Q} 691004 {160*691004} {Tfloor} {fac[0]} {fac[1]}\n'+
                      ''.join(f'{p} '+ ' '.join(map(str, radii[p]))+'\n' for p in primes))
    manifest = dict(scope='Complete outward L497 seeds for fixed-corner complement only',
                    Q=Q, N=691004, H=160*691004, ell0=str(ell),
                    exp_ell_grid30=list(map(str,e)), exp_floor=Tfloor,
                    two_over_ell_grid56=list(map(str,fac)),
                    source_ledger=dict(path=initial.name, sha256=expected, rows=count),
                    source_qualification='L497 full proof/code awaits separate critical audit',
                    seeds=dict(path=path.name, sha256=sha(path), format='<qqqq per n: a_lo,a_hi,log_lo,log_hi'),
                    config=dict(path=config.name, sha256=sha(config)), failures=[])
    out = ROOT/(NAME+'-seeds.json')
    out.write_text(json.dumps(manifest, indent=2)+'\n')
    print(f'All {count} rows rescaled outward; H={160*691004}<floor(exp(ell0))={Tfloor}; failures=0')
    print(f'Full seed certificate: {out.relative_to(ROOT.parent.parent)}')


if __name__ == '__main__':
    main()
