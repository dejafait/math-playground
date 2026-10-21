#!/usr/bin/env python3
"""L058 fixed audit: unchanged isolated replay, ceiling paths, integer sums."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import sys
import traceback
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path('scripts/conductor36-quadratic-seven')
BASE = Path('scripts/conductor36-table')
OUT = ROOT/'critical-audit'
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ.pop('PYTHONOPTIMIZE', None)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def save(p, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2)+'\n')


def module(p, name):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))


def mul(x, y):
    a,b,c,d = x
    e,f,g,h = y
    return [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]


def inv(x):
    a,b,c,d = x
    assert a*d-b*c == 1
    return [d,-b,-c,a]


def cusp(a, b):
    if not b:
        assert a
        return [1,0]
    x = Q(a,b)
    return [x.numerator,x.denominator]


def valuation(x):
    x = Q(x)
    if not x:
        return 'infinity'
    n,d,v = x.numerator,x.denominator,0
    while n % 7 == 0:
        n //= 7
        v += 1
    while d % 7 == 0:
        d //= 7
        v -= 1
    return v


def main():
    assert sys.flags.optimize == 0
    OUT.mkdir(parents=True, exist_ok=True)
    cert = read(ROOT/'certificate.json')
    original_files = {p for p in ROOT.iterdir() if p.is_file() and p.name != 'audit.py'}
    # Preserve every upstream file, including old reports/failures and all term
    # files, not only the direct certificate bindings. Bytecode is not evidence.
    for folder in [BASE, Path('scripts/nonunitary-cusp')]:
        original_files.update(p for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    original_files.update(Path(p) for p in cert['input_sha256'])
    original_files.add(Path('scripts/general-relative/verify_certificate.py'))
    manifest_path = OUT/'pre-replay-manifest.json'
    if manifest_path.exists():
        manifest = read(manifest_path)
        assert set(manifest) == {str(p) for p in original_files}
        assert all(sha(p) == h for p,h in manifest.items())
    else:
        manifest = {str(p): sha(p) for p in sorted(original_files)}
        save(manifest_path, manifest)
    report = {'program_sha256': sha(__file__), 'manifest': str(manifest_path),
              'original_files': len(manifest), 'checks': {}, 'failures': [],
              'external_theorems_verified_by_script': False}

    def check(name, condition):
        report['checks'][name] = bool(condition)
        assert condition, name

    try:
        for p in sorted(original_files):
            if p.parent == ROOT:
                dest = OUT/'originals'/p.name
                if dest.exists():
                    assert sha(dest) == manifest[str(p)]
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(p.read_bytes())
        check('all_bound_input_hashes', all(manifest[p] == h for p,h in cert['input_sha256'].items()))
        check('retained_initial_binding_failure', bool(read(ROOT/'initial-binding-failure.json')['failures']))
        check('only_two_reached_depths', [a['n'] for a in cert['attempts']] == [2,3])
        builder = module(OUT/'originals/build_certificate.py', 'l058_preserved_builder')
        builder.ROOT = OUT/'rebuild'
        log = io.StringIO()
        with contextlib.redirect_stdout(log):
            builder.main()
        (builder.ROOT/'command.txt').write_text(log.getvalue())
        check('isolated_rebuild_identical_certificate_bytes', sha(builder.ROOT/'certificate.json') == manifest[str(ROOT/'certificate.json')])
        verifier = module(OUT/'originals/verify_certificate.py', 'l058_preserved_verifier')

        def execute(data, directory):
            directory.mkdir(parents=True, exist_ok=True)
            save(directory/'certificate.json', data)
            seed = read(ROOT/'verification.json')
            seed['audit_stale_success_sentinel'] = True
            save(directory/'verification.json', seed)
            verifier.ROOT = directory
            log, code = io.StringIO(), 0
            print('starting complete replay', directory, flush=True)
            try:
                with contextlib.redirect_stdout(log):
                    verifier.main()
            except SystemExit as error:
                code = error.code
            finally:
                (directory/'command.txt').write_text(log.getvalue())
            fresh = read(directory/'verification.json')
            assert 'audit_stale_success_sentinel' not in fresh
            print('finished replay', directory, 'exit', code, 'failures', fresh['failures'], flush=True)
            return code, fresh

        code, fresh = execute(cert, OUT/'replay')
        check('complete_replay', code == 0 and fresh['failures'] == [] and len(fresh['checks']) == 11 and all(fresh['checks'].values()))
        old = read(ROOT/'verification.json')
        comparable = copy.deepcopy(fresh)
        comparable['upstream_replays'] = old['upstream_replays']
        check('full_replay_report_equal_except_output_paths', comparable == old)
        structure = read(OUT/'replay/coefficient-upstream-structure.json')
        table = read(OUT/'replay/coefficient-upstream-table.json')
        check('full_fresh_upstream_reports_equal_originals', structure == read(ROOT/'coefficient-upstream-structure.json') and table == read(ROOT/'coefficient-upstream-table.json'))
        check('all_structure_domains', not structure['failures'] and all(structure['actual'][k] == v for k,v in structure['required'].items()) and structure['actual']['segments'] == 626)
        expected_checks = {'primitive_records': 98, 'Fourier_terms': 476280,
            'zero_coefficient_terms_retained': 423360, 'cosine_Taylor_steps': 149760,
            'attenuation_brackets': 16, 'uncombined_signed_occurrences': 1316,
            'signed_quotient_endpoints': 288, 'integer_isolations': 72,
            'source_relations': 144, 'saturated_columns': 59,
            'quotient_coordinates': 13, 'generator_reconstructions': 72}
        check('all_table_replay_counts', table['checks'] == expected_checks and table['replay_passed'] and table['table_complete'] and not table['failures'])
        check('630_paths_3375_segments_336_terms', fresh['results'] == {'paths':630,'required_paths':630,'segments':3375,'required_segment_occurrences':3375,'strict_bound':True,'selected_n':3} and [a['actual_terms'] for a in fresh['attempts']] == [42,294])
        report['upstream'] = {'structure': {'actual':structure['actual'],'required':structure['required']}, 'table_checks':table['checks']}
        report['replay_report'] = str(OUT/'replay/verification.json')

        base, tab = read(BASE/'presentation.json'), read(BASE/'table_certificate.json')
        pr = base['presentation']
        coords, lifts = pr['generator_coordinates'], base['cosets']['lifts']
        K, head = pr['K']['entries'], pr['head']['entries']
        f = list(map(Q, tab['relations']['quotient_values']))
        values = [Q(r['value']) for r in tab['generators']]
        assert len(lifts) == len(coords) == len(K) == 72 and len(head) == 59 and len(f) == 13
        assert all(len(r) == 13 for r in coords) and all(len(r) == 59 for r in K) and all(len(r) == 72 for r in head)

        def project(raw):
            return [sum(raw[i]*coords[i][j] for i in range(72)) for j in range(13)]

        alternatives, count = {}, 0
        for key, original in cert['paths'].items():
            r = Q(key)
            assert r > 0 and r.denominator % 7 == 0
            a,b = r.numerator,r.denominator
            digits, reductions = [], []
            while b:
                k = -((-a)//b)
                rem = k*b-a
                assert 0 <= rem < b
                reductions.append([a,b,k,rem])
                digits.append(k)
                a,b = b,rem
            reconstructed = Q(digits[-1])
            for k in digits[-2::-1]:
                assert reconstructed
                reconstructed = k-1/reconstructed
            assert reconstructed == r
            p0,q0,p1,q1 = 0,-1,1,0
            raw,chain,segments = [0]*72,[[1,0]],[]
            for k in digits:
                p2,q2 = k*p1-p0,k*q1-q0
                assert q2 > 0 and p2*q1-p1*q2 == -1
                start,end = cusp(p1,q1),cusp(p2,q2)
                h = [-p2,p1,-q2,q1]
                inv(h)
                assert cusp(h[1],h[3]) == start == chain[-1] and cusp(h[0],h[2]) == end
                hits = [(i,mul(h,inv(g))) for i,g in enumerate(lifts)]
                hits = [(i,gamma) for i,gamma in hits if gamma[2] % 36 == 0]
                assert len(hits) == 1
                i,gamma = hits[0]
                inv(gamma)
                assert mul(gamma,lifts[i]) == h
                raw[i] += 1
                segments.append({'start':start,'end':end,'lift':h,'coset':i,'Gamma0_reduction':gamma})
                chain.append(end)
                p0,q0,p1,q1 = p1,q1,p2,q2
            assert chain[-1] == original['argument'] and chain[1] != original['segments'][0]['end']
            delta = [x-y for x,y in zip(raw,original['raw'])]
            witness = [dot(row,delta) for row in head]
            quotient = project(raw)
            assert quotient == original['coordinates'] and project(delta) == [0]*13
            assert [dot(row,witness) for row in K] == delta
            value = dot(raw,values)
            assert value == dot(quotient,f) == Q(original['value']) and (12*value).denominator == 1
            alternatives[key] = {'original':original, 'euclidean_reductions':reductions,
                'negative_cf':digits,'chain':chain,'segments':segments,'raw':raw,
                'coordinates':quotient,'difference':delta,'saturated_coefficients':witness,
                'value':str(value),'value12':int(12*value)}
            count += len(segments)
        save(OUT/'alternative-paths.json', alternatives)
        check('all_630_distinct_ceiling_chains_full_quotient_witnesses', len(alternatives) == 630)
        report['alternate_paths'] = {'actual':len(alternatives),'required':630,'segments':count,
            'distinct_raw_vectors':sum(v['raw'] != v['original']['raw'] for v in alternatives.values()),
            'certificate':str(OUT/'alternative-paths.json'),'sha256':sha(OUT/'alternative-paths.json')}

        attempts, used = [],set()
        for saved in cert['attempts']:
            n,M = saved['n'],saved['M']
            q = 7**n
            roots = [[w for w in range(d,q,7) if (w**6-1) % q == 0] for d in range(1,7)]
            assert all(len(xs) == 1 for xs in roots)
            roots = [xs[0] for xs in roots]
            candidates = [u for u in range(3,7**M,7) if (u*u+4*u+7) % 7**M == 0]
            assert candidates == [304]
            u = candidates[0]
            assert u*u+4*u+7 == 93639 and valuation(93639) == 4 and (2*u+4)%7 == 3
            totalA = totalB = 0
            rows,terms,residues = [],[],[]
            for d,w in enumerate(roots,1):
                rowA = rowB = 0
                for j in range(7**(n-1)):
                    r = w*pow(8,j,q)%q
                    ak,bk = str(Q(r,q)),str(Q(r,7**(n-1)))
                    A12,B12 = alternatives[ak]['value12'],alternatives[bk]['value12']
                    weight = sum(range(j))
                    A,B = Q(A12,12),Q(B12,12)
                    term = Q(weight*(u*A12-B12),12*u**(n+1))
                    record = {'d':d,'j':j,'r':r,'binomial':weight,'A_path':ak,'B_path':bk,'A':str(A),'B':str(B),'term':str(term)}
                    assert record == saved['terms'][len(terms)]
                    terms.append(record)
                    rowA += weight*A12
                    rowB += weight*B12
                    used.update([ak,bk]); residues.append(r)
                rows.append([rowA,rowB]); totalA += rowA; totalB += rowB
            assert sorted(residues) == [k for k in range(q) if k % 7]
            b = Q(u*totalA-totalB,12*u**(n+1))
            assert b == sum((Q(t['term']) for t in terms),Q(0)) == Q(saved['b'])
            assert Q(totalA,12) == Q(saved['sum_A']) and Q(totalB,12) == Q(saved['sum_B'])
            N,v = min(n-1,M),valuation(b)
            assert v == 1 and saved['valuation_b'] == v and saved['N'] == N and saved['strict_bound'] == (N>v)
            attempts.append({'n':n,'M':M,'u':u,'root_residual':93639,'root_precision':4,
                'roots':roots,'row_integer_sums':rows,'sum_A12':totalA,'sum_B12':totalB,
                'terms':terms,'actual_terms':len(terms),'required_terms':6*7**(n-1),
                'b':str(b),'valuation_b':v,'C':0,'N':N,'strict_bound':N>v})
        check('all_independent_integer_sums', [(a['sum_A12'],a['sum_B12']) for a in attempts] == [(0,-420),(-27972,82908)] and used == set(alternatives))
        check('L057_strict_threshold_only_at_depth_three', [(a['N'],a['valuation_b'],a['strict_bound']) for a in attempts] == [(1,1,False),(2,1,True)])
        save(OUT/'integer-sums.json', attempts)
        report['coefficient'] = [{k:v for k,v in a.items() if k != 'terms'} for a in attempts]

        report['rejections'] = {}
        for name in ['gamma','path_coordinate','root_residual','weighted_term']:
            bad = copy.deepcopy(cert)
            if name == 'gamma':
                bad['instance']['gamma'] = 7
                expected_line = "assert cert['instance'] =="
            elif name == 'path_coordinate':
                bad['paths'][next(iter(bad['paths']))]['coordinates'][12] += 1
                expected_line = "assert integer_row(saved['coordinates'], 13) == quotient"
            elif name == 'root_residual':
                bad['attempts'][0]['unit_root']['residual'] += 7**3
                expected_line = "assert a['unit_root'] =="
            else:
                terms = bad['attempts'][1]['terms']
                index = next(i for i,t in enumerate(terms) if t['j'] > 2 and Q(t['term']))
                terms[index]['term'] = str(Q(terms[index]['term'])+1)
                expected_line = "assert rational(term['term']) == value"
            directory = OUT/'rejections'/name
            code,rejected = execute(bad,directory)
            check('intended_fresh_rejection_'+name, code == 1 and rejected['results'] == {} and rejected['failures'] == ['AssertionError: '] and expected_line in rejected['traceback'])
            report['rejections'][name] = {'report':str(directory/'verification.json'),
                'certificate_sha256':sha(directory/'certificate.json'), 'intended_assertion':expected_line,
                'exit':code,'failures':rejected['failures']}
    except (Exception,SystemExit) as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
        report['traceback'] = traceback.format_exc()
    finally:
        report['changed_original_files'] = [p for p,h in manifest.items() if not Path(p).exists() or sha(p) != h]
        report['original_bytes_preserved'] = not report['changed_original_files']
        if report['changed_original_files']:
            report['failures'].append('original bytes changed')
        save(OUT/'audit.json', report)
    print('audit checks',len(report['checks']),'alternate paths',report.get('alternate_paths'),
          'bounds',[(a['n'],a['N'],a['valuation_b']) for a in report.get('coefficient',[])],
          'preserved',report['original_bytes_preserved'],'failures',report['failures'],
          'report',OUT/'audit.json',flush=True)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
