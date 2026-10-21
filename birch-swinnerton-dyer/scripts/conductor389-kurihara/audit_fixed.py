#!/usr/bin/env python3
"""Fixed L064 replay and distinct grouped integer check; preserve originals."""
import copy
import hashlib
import json
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path('scripts/conductor389-kurihara')
OUT = ROOT/'critical-audit-2026-10-15'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(path.read_text())


def save(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def replay(cert, terms, name):
    report = OUT/(name+'-report.json')
    log = OUT/(name+'-stdout.txt')
    with log.open('w') as stream:
        run = subprocess.run([sys.executable, str(ROOT/'verify_certificate.py'),
                              '--certificate', str(cert), '--terms', str(terms),
                              '--out', str(report),
                              '--replay', str(OUT/(name+'-replay.jsonl'))],
                             stdout=stream, stderr=subprocess.STDOUT)
    return run.returncode, read(report)


def main():
    assert not OUT.exists(), 'Use a fresh audit destination; preserve existing evidence'
    originals = sorted(p for p in ROOT.rglob('*') if p.is_file())
    cert = read(ROOT/'certificate.json')
    originals += [Path(p) for p in cert['input_sha256']]
    before = {str(p): sha(p) for p in originals}
    OUT.mkdir()
    save(OUT/'preservation-before.json', before)
    result = {'checks': {}, 'failures': [], 'original_files': len(before),
              'scope': 'fixed p=7 depth-one 113*281; no alternate paths or new index'}
    try:
        code, fresh = replay(ROOT/'certificate.json', ROOT/'terms.jsonl', 'complete')
        old = read(ROOT/'verification.json')
        assert code == 0 and fresh == old and fresh['failures'] == []
        assert fresh['result']['terms'] == fresh['result']['required_terms'] == 31360
        assert fresh['result']['segments'] == 319804
        assert fresh['replay_sha256'] == sha(ROOT/'replay.jsonl')
        result['checks']['complete_fresh_replay_matches_original'] = True
        result['complete_result'] = fresh['result']
        print('Complete replay: terms 31360/31360, segments 319804/319804; failures []', flush=True)

        # New accumulation uses the individual segment values, then groups by
        # the 49 logarithm classes before multiplying their integer totals.
        values = [Fraction(x) for x in read(Path('scripts/calibrated-symbols/certificate.json'))[
            'integral_generator_values']]
        doubled = []
        for x in values:
            assert (2*x).denominator == 1
            doubled.append((2*x).numerator)
        inverse = [{pow(3, k, ell): k % 7 for k in range(ell-1)} for ell in (113, 281)]
        assert [len(t) for t in inverse] == [112, 280]
        bins = {(i, j): {'count': 0, 'value_twice_sum': 0} for i in range(7) for j in range(7)}
        count = segments = prefix = zeros = 0
        rational = Fraction(0)
        with (ROOT/'terms.jsonl').open() as terms, (ROOT/'replay.jsonl').open() as old_stream, \
                (OUT/'complete-replay.jsonl').open() as new_stream, \
                (OUT/'integer-check.jsonl').open('w') as output:
            for a in range(1, 31753):
                if a % 113 == 0 or a % 281 == 0:
                    continue
                term = json.loads(next(terms))
                assert term['a'] == a
                multiplicities = Counter(seg['coset'] for seg in term['segments'])
                value2 = sum(doubled[i]*n for i, n in multiplicities.items())
                value = Fraction(term['value'])
                assert 2*value == value2
                i, j = inverse[0][a % 113], inverse[1][a % 281]
                assert term['logs'] == [i, j]
                bins[i, j]['count'] += 1
                bins[i, j]['value_twice_sum'] += value2
                contribution = value2*i*j
                prefix += contribution
                rational += value*i*j
                expected = {'a': a, 'value_twice': value2, 'logs': [i, j],
                            'contribution_twice': contribution, 'prefix_twice': prefix}
                assert json.loads(next(old_stream)) == expected
                assert json.loads(next(new_stream)) == expected
                assert term['term'] == (4*contribution) % 7
                output.write(json.dumps(expected, separators=(',', ':'))+'\n')
                count += 1
                segments += len(term['segments'])
                zeros += contribution % 7 == 0
            assert terms.read() == old_stream.read() == new_stream.read() == ''
        # CRT makes every log-residue bin have (112/7)*(280/7)=640 units.
        assert all(b['count'] == 640 for b in bins.values())
        grouped = sum(i*j*b['value_twice_sum'] for (i, j), b in bins.items())
        assert count == 31360 and segments == 319804 and zeros == 13342
        assert grouped == prefix == 2*rational == -2730 and rational == -1365
        assert (4*grouped) % 7 == 0
        result['checks']['every_retained_and_fresh_replay_prefix'] = True
        result['checks']['distinct_49_bin_integer_and_rational_accumulation'] = True
        result['integer_sum'] = {'terms': count, 'required_terms': 31360,
                                 'segments': segments, 'required_segments': 319804,
                                 'bins': [{'logs': list(k), **v} for k, v in bins.items()],
                                 'required_count_per_bin': 640, 'weighted_twice': grouped,
                                 'weighted_exact': str(rational), 'scalar': 0,
                                 'zero_mod7_terms': zeros,
                                 'full_term_check_sha256': sha(OUT/'integer-check.jsonl')}

        with (ROOT/'terms.jsonl').open() as stream:
            prefix_rows = [json.loads(next(stream)) for _ in range(3)]
        altered = copy.deepcopy(prefix_rows)
        altered[0]['term'] = (altered[0]['term']+1) % 7
        cases = [('missing-second-term', [prefix_rows[0], prefix_rows[2]], 'unit ordering a=2', 1),
                 ('duplicate-first-term', [prefix_rows[0], prefix_rows[0], prefix_rows[2]], 'unit ordering a=2', 1),
                 ('altered-contribution', altered, 'altered contribution a=1', 0),
                 ('ineligible-pair', prefix_rows, 'selected pair is not the certified first eligible pair', 0)]
        recorded = read(ROOT/'rejection-checks.json')
        assert recorded['originals_unchanged'] and recorded['failures'] == []
        assert all(before[p] == h for p, h in recorded['original_sha256'].items())
        result['rejections'] = []
        for name, rows, message, completed in cases:
            cp = ROOT/'rejections'/(name+'-certificate.json')
            tp = ROOT/'rejections'/(name+'-terms.jsonl')
            assert [json.loads(line) for line in tp.read_text().splitlines()] == rows
            expected_cert = copy.deepcopy(cert)
            expected_cert['terms_sha256'] = sha(tp)
            if name == 'ineligible-pair':
                expected_cert['selected_pair'] = [29, 113]
            assert read(cp) == expected_cert
            code, report = replay(cp, tp, name)
            assert code == 1 and report == read(ROOT/'rejections'/(name+'-report.json'))
            assert report['failures'] == ['AssertionError: '+message]
            assert report['completed_terms'] == completed
            old_replay = ROOT/'rejections'/(name+'-replay.jsonl')
            new_replay = OUT/(name+'-replay.jsonl')
            if old_replay.exists():
                assert new_replay.read_bytes() == old_replay.read_bytes()
            else:
                assert not new_replay.exists() and name == 'ineligible-pair'
            assert completed < len(rows)
            result['rejections'].append({'case': name, 'failure': message,
                                         'completed_terms': completed, 'fixture_terms': len(rows),
                                         'intended_failure_before_missing_suffix': True})
        result['checks']['all_four_retained_prefix_failures_replayed'] = True
    except Exception as error:
        result['failures'].append(f'{type(error).__name__}: {error}')
    after = {str(p): sha(p) for p in originals}
    save(OUT/'preservation-after.json', after)
    result['checks']['all_original_bytes_preserved'] = before == after
    if before != after:
        result['failures'].append('Original bytes changed')
    save(OUT/'audit.json', result)
    print('Integer sum', result.get('integer_sum', {}).get('weighted_twice'),
          'required -2730; intended rejections', len(result.get('rejections', [])),
          '/4; preserved', before == after, 'failures', result['failures'],
          'report', OUT/'audit.json', flush=True)
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
