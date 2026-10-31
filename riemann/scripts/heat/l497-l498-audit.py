#!/usr/bin/env python3
"""Preserved-input, full fixed-corner audit. Run prepare, C++ replay, finish.

No producer routines are imported. The separately reviewed prefix consumer
is reused at its finer grid; all audit output goes in mass-audit/.
"""
from pathlib import Path
from fractions import Fraction as F
import csv
import gzip
import hashlib
import importlib.util
import json
import math
import struct
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'mass-audit'
Q = 1 << 56
N, H, T = 691004, 110560640, 31720474772
checks = 0


def require(ok, label):
    global checks
    checks += 1
    if not ok:
        raise ValueError(label)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def read(name):
    return json.loads((ROOT / name).read_text())


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')


def prepare():
    require(sys.flags.optimize == 0, 'Python assertions enabled')
    OUT.mkdir(exist_ok=True)
    names = sorted(p.name for pattern in ('finite-prefix-*', 'complementary-mass*')
                   for p in ROOT.glob(pattern) if p.is_file())
    before = {name: sha(ROOT / name) for name in names}
    write('original-artifacts.json', before)
    # Redirect the existing independent consumer, preserving original outputs.
    for name in ('finite-prefix-certificate.json', 'finite-prefix-certificate.py',
                 'finite-prefix-certificate-initial.tsv.gz',
                 'finite-prefix-certificate-coefficients.tsv.gz'):
        dest = OUT / name
        if not dest.exists():
            dest.symlink_to('../' + name)
        require(dest.resolve() == (ROOT / name).resolve(), 'input symlink target')
    spec = importlib.util.spec_from_file_location('prefix_consumer', ROOT / 'finite-prefix-verify.py')
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    lib.ROOT = OUT
    lib.main()
    prefix = read('finite-prefix-certificate.json')
    oldver = read('finite-prefix-verification.json')
    fresh = json.loads((OUT / 'finite-prefix-verification.json').read_text())
    require(fresh == oldver, 'complete prefix replay exactly matches retained evidence')
    require(fresh['all_checks_passed'] and not fresh['failures'], 'prefix full replay')
    # Additional prime/radius and stage metadata, not just totals.
    primes = [p for p in range(2, 308) if all(p % d for d in range(2, math.isqrt(p)+1))]
    require(len(primes) == 63, 'complete 63 primes')
    require(prefix['computation']['stages'] == [{'p': p, 'updates': N//p} for p in primes], 'every stage')
    require(prefix['computation']['coefficient_updates'] == sum(N//p for p in primes), 'prefix updates')
    radius_meta = next(c['actual'] for c in prefix['checks'] if c['name'] == 'all_euler_radii')
    seed = read('complementary-mass-seeds.json')
    ell = F('24.18022820120389')
    require(seed['Q'] == Q and seed['N'] == N and seed['H'] == H and F(seed['ell0']) == ell, 'seed parameters')
    require(seed['exp_floor'] == T, 'seed split floor')
    for key in ('seeds', 'config', 'source_ledger'):
        require(sha(ROOT / seed[key]['path']) == seed[key]['sha256'], 'seed hash ' + key)
    require(seed['source_ledger']['rows'] == N, 'seed source rows')
    # Independent finer-grid positive exponential from audited degree-32 routine.
    v = lib.inv(lib.exponential(lib.rat(-ell/2)))
    v = lib.times(v, v)
    coarse = list(map(int, seed['exp_ell_grid30']))
    require(coarse[0]*10**10 <= v[0] <= v[1] <= coarse[1]*10**10, 'independent exp containment')
    require(v[0]//lib.Q == v[1]//lib.Q == T and H < T, 'independent split floor')
    fac = list(map(int, seed['two_over_ell_grid56']))
    require(F(fac[0], Q) <= 2/ell <= F(fac[1], Q), 'exact 2/ell enclosure')
    config = [list(map(int, line.split())) for line in (ROOT / 'complementary-mass-config.txt').read_text().splitlines()]
    require(config[0] == [Q, N, H, T, *fac], 'config header')
    require([r[0] for r in config[1:]] == primes and all(len(r) == 5 for r in config[1:]), 'config rows')
    prime_rows = {r[0]: r[1:] for r in config[1:]}
    def convert(a, b):
        return a*Q//10**30, -((-b*Q)//10**30)
    max_seed = 0
    with gzip.open(ROOT / 'finite-prefix-certificate-initial.tsv.gz', 'rt') as source, (ROOT / 'complementary-mass-seeds.bin').open('rb') as binary:
        require(next(source).strip() == 'n\tlog_lower\tlog_upper\ta_lower\ta_upper', 'seed source header')
        for n in range(1, N+1):
            row = list(map(int, next(source).split()))
            require(len(row) == 5 and row[0] == n, 'seed source index')
            _, ll, lh, al, ah = row
            require(0 <= ll <= lh and 0 <= al <= ah, 'positive seed source')
            wanted = (*convert(al, ah), *convert(ll, lh))
            raw = binary.read(32)
            require(len(raw) == 32 and struct.unpack('<qqqq', raw) == wanted, 'every outward seed conversion')
            max_seed = max(max_seed, *wanted)
            if n == 1:
                require(wanted == (Q, Q, 0, 0), 'empty weight/log')
            if n in prime_rows:
                require(tuple(prime_rows[n]) == wanted and 0 < wanted[0] <= wanted[1] < Q, 'every config prime row')
                require([str(al), str(ah)] == radius_meta[str(n)], 'prefix radius metadata')
        require(source.read() == '' and binary.read() == b'', 'both seed EOFs')
    require((ROOT / 'complementary-mass-seeds.bin').stat().st_size == N*32, 'binary seed length')
    oldreport = read('complementary-mass-verification.json')
    for record in oldreport['evidence']:
        require(sha(ROOT / record['path']) == record['sha256'], 'retained report hash ' + record['path'])
    # Expected moments are only comparisons; replay derives them independently.
    moments = read('complementary-mass-moments.json')
    with (OUT / 'expected-moments.txt').open('w') as f:
        for k in ('A_N', 'B_N', 'R', 'Rlog', 'enumerated_R', 'enumerated_Rlog',
                  'residual_R', 'residual_Rlog', 'clipped_tail', 'far_tail', 'positive_tail'):
            f.write(k + ' ' + ' '.join(moments[k]) + '\n')
        f.write('counts ' + str(moments['divisors_le_T']) + ' ' + str(moments['divisors_le_H']) + '\n')
        f.write('depth ' + ' '.join(map(str, moments['depth_counts'])) + '\n')
    require(all(sha(ROOT/name) == h for name, h in before.items()), 'originals unchanged')
    write('preparation.json', dict(complete=True, checks=checks, failures=[],
          prefix_comparisons=fresh['comparisons'], seed_rows=N, grid=str(Q),
          independent_exp_grid40=list(map(str, v)), exp_floor=T,
          max_seed_endpoint=str(max_seed), required_exp_floor=T, python_optimization=sys.flags.optimize,
          byteorder=sys.byteorder, int64_bytes=struct.calcsize('q'),
          original_manifest_sha256=sha(OUT/'original-artifacts.json'),
          audit_script_sha256=sha(Path(__file__))))
    print(f'Audit preparation complete: {checks} checks, {N} full seed rows; exp floor={T}; failures=0', flush=True)
    print('Full evidence: scripts/heat/mass-audit/preparation.json', flush=True)


def finish():
    prep = json.loads((OUT / 'preparation.json').read_text())
    replay = json.loads((OUT / 'replay.json').read_text())
    require(prep['complete'] and replay['complete'], 'complete executions')
    require(not prep['failures'] and not replay['failures'], 'no computation failures')
    require(prep['audit_script_sha256'] == sha(Path(__file__)), 'same audit driver')
    for name, h in json.loads((OUT / 'original-artifacts.json').read_text()).items():
        require(sha(ROOT / name) == h, 'original artifact preserved ' + name)
    original_moments = read('complementary-mass-moments.json')
    require(replay['moments'] == {k: original_moments[k] for k in replay['moments']}, 'every moment')
    require(replay['depth_counts'] == original_moments['depth_counts'], 'all 64 depth counts')
    require(replay['divisors_le_T'] == original_moments['divisors_le_T'] and
            replay['divisors_le_H'] == original_moments['divisors_le_H'], 'complete divisor counts')
    old = read('complementary-mass-result.json')
    for key in ('edge', 'positive_tail', 'complement_majorant', 'rows', 'channel_updates',
                'positive', 'negative', 'straddling', 'max_coefficient_width'):
        require(replay[key] == old[key], 'complete edge result ' + key)
    require(replay['rows'] == H-N and replay['blocks_checked'] == 110, 'every edge output')
    # Every original block statistic has already been compared in C++.
    # Independent hash-stream records attest full output traversal, not truth alone.
    with (OUT / 'coefficient-blocks.tsv').open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    require(len(rows) == 110 and sum(int(r['count']) for r in rows) == H-N, 'all replay block records')
    prefix = F(int(read('finite-prefix-certificate.json')['result']['prefix_interval_grid'][1]), 10**30)
    threshold = F('.301408572679396256667379418689')
    upper = F(int(replay['complement_majorant'][1]), Q)
    require(1-prefix == threshold, 'exact prefix/complement threshold identity')
    require(upper < threshold, 'complement strict threshold')
    require(prefix+upper < F('.999577507'), 'full strict threshold')
    require(1-prefix-upper > F('.00042249'), 'strict reserve')
    require(upper < F('.30098607886352571339'), 'printed complement decimal')
    require(int(old['threshold_floor_grid']) == (threshold*Q).__floor__(), 'provisional floor constant')
    require(old['provisional_pass'] == (upper*Q < (threshold*Q).__floor__()), 'provisional flag')
    evidence = [p for p in OUT.iterdir() if p.is_file() and not p.is_symlink() and p.name != 'audit.json']
    evidence += [Path(__file__), ROOT / 'l497-l498-replay.cpp']
    write('audit.json', dict(complete=True, checks=checks, failures=[],
          task='Independent numerical replay after mathematical code audit; fixed corner only',
          prefix_upper=str(prefix), complement_upper=str(upper), required_complement_strict_upper=str(threshold),
          full_upper=str(prefix+upper), required_full_strict_upper='.999577507',
          reserve_lower=str(1-prefix-upper), required_reserve_strict_lower='.00042249',
          prefix_comparisons=prep['prefix_comparisons'], seed_rows=N, divisor_rows=replay['divisors_le_T'],
          edge_rows=replay['rows'], channel_updates=replay['channel_updates'], blocks=replay['blocks_checked'],
          qualifications=['No charge/transport/collision/RH conclusion', 'No historical binary build provenance inferred',
                          'Coefficient checksums record traversal; enclosure validity follows from audited algorithms',
                          'Source and base-phase/saddle imports are not audited'],
          evidence=[dict(path=str(p.relative_to(ROOT)), sha256=sha(p)) for p in sorted(evidence)]))
    print(f'Complete fixed-corner audit: complement <= {upper} < {threshold}; failures=0')
    print(f'Full mass <= {prefix+upper} < .999577507; reserve > .00042249')
    print(f'{replay["divisors_le_T"]} divisors, {replay["rows"]} edge outputs, {replay["channel_updates"]} signed updates')
    print('Full certificate: scripts/heat/mass-audit/audit.json')


if __name__ == '__main__':
    try:
        {'prepare': prepare, 'finish': finish}[sys.argv[1]]()
    except Exception as exc:
        OUT.mkdir(exist_ok=True)
        write('failure.json', dict(complete=False, checks=checks, failure=repr(exc)))
        raise
