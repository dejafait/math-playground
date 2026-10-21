"""Step 207: validate parsing, then archive-only replay of preserved prefix 0.

Never reconstructs the Closure store, regenerates inputs/exports or modifies
old certificates. Every primitive record remains covered by audit.scan.
"""
import argparse
import copy
import gzip
import json
import random
import time
from pathlib import Path
import fast_syntax as f

h, a = f.h, f.h.audit
OUT, ROOT = h.OUT, h.ROOT
RUN_TAG = '207-strict'
VALIDATION = OUT / ('parser-validation-' + RUN_TAG + '.json')
DEST = OUT / ('replay-' + RUN_TAG + '-star-coordinate-0.json')
original_read = a.read


def strict_read(raw):
    row = original_read(raw)
    if isinstance(row, dict) and 'refs' in row:
        refs = row['refs']
        if not isinstance(refs, list) or len(refs) != 2 or any(
                type(k) is not int or k < 0 for k in refs):
            raise ValueError('both formats require literal nonnegative integer MP references')
    return row


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def scan(backend, *args, **kwargs):
    a.syntax = backend()
    a.read = strict_read if backend is f.FastSyntax else original_read
    try:
        return a.scan(*args, **kwargs)
    finally:
        if isinstance(a.syntax, f.FastSyntax): a.syntax.close()
        a.syntax = a.Syntax()
        a.read = original_read


def validation():
    assert not VALIDATION.exists(), 'preserve parser validation'
    result = dict(complete=False, failures=[], syntax_cases=[], libraries={},
                  complete_cases=[], rejections=[])
    save(VALIDATION, result)
    try:
        old, new = a.Syntax(), f.FastSyntax()
        rng = random.Random(207)
        terms = ['A', 'A_0', '9', 'x' * 1024, '(A>A)', '(~A)']
        for depth in range(1, 80): terms.append('(~' * depth + 'A' + ')' * depth)
        for _ in range(400):
            left, right = rng.choice(terms[:100]), rng.choice(terms[:100])
            terms.append('(' + left + '>' + right + ')')
        for t in terms:
            i, j = old.parse(t), new.parse(t)
            assert old.stats[i] == new.stats[j]
            assert all(old.text(i, image) == new.text(j, image) for image in (False, True))
        # Includes wrong connectives, unmatched syntax, whitespace, Unicode,
        # trailing text/NUL and invalid ASCII payloads.
        bad = ['', '()', '(A)', '(~)', '(A|B)', '(A>B', '(~A))',
               'A B', 'é', 'A\x00', '(A> B)', 'a-b', '(A>B)C', '((~A)|B)']
        for t in bad:
            for backend in (old, new):
                try: backend.parse(t)
                except (ValueError, AssertionError, UnicodeError): pass
                else: raise AssertionError('malformed syntax accepted: ' + repr(t))
        result['syntax_cases'] = dict(valid=len(terms), rejected=len(bad),
                                      exact_native_image_stats=True)
        new.close()
        initial = json.loads((OUT / 'certificate-202.json').read_text())
        for name, entry in initial['library'].items():
            native = ROOT / entry['native']['path']
            image = ROOT / entry['not-or']['path']
            with gzip.open(native, 'rb') as stream: goal = a.read(stream.readline())['goal']
            x = scan(a.Syntax, native, goal, image)
            y = scan(f.FastSyntax, native, goal, image)
            for k in ('measurements', 'node_sums', 'depths', 'name_bytes', 'references'):
                assert x[k] == y[k], ('parser differential', name, k)
            result['libraries'][name] = y['measurements']
            save(VALIDATION, result)
        print('PASS all 15 fixed-law pairs: complete differential replay', flush=True)
        d = json.loads((OUT / 'star-205.request.json').read_text())
        tables = h.ep.request(d)
        cases = [(OUT / ('star-205-local-' + str(v) + '.native.jsonl.gz'),
                  h.ep.e.c.serialize(tables['local'][v]), None) for v in range(d['N'])]
        empty = json.loads((OUT / 'empty.request.json').read_text())
        goal = h.ep.e.c.serialize(h.ep.request(empty)['closed'][0])
        cases.append((OUT / 'empty-coordinate-0.native.jsonl.gz', goal,
                      OUT / 'empty-coordinate-0.not-or.jsonl.gz'))
        for native, goal, image in cases:
            x, y = scan(a.Syntax, native, goal, image), scan(f.FastSyntax, native, goal, image)
            for k in ('measurements', 'node_sums', 'depths', 'name_bytes', 'references'):
                assert x[k] == y[k], ('complete differential', native.name, k)
            result['complete_cases'].append(y['measurements'])
            save(VALIDATION, result)
        # Small three-record genuine ax1/MP proof; mutate each load-bearing field.
        native = OUT / ('parser-' + RUN_TAG + '-valid.native.jsonl.gz')
        image = OUT / ('parser-' + RUN_TAG + '-valid.not-or.jsonl.gz')
        t = '(A>(B>A))'
        rows = [dict(f=t, rule='ax1', subs=dict(A='A', B='B')),
                dict(f='(' + t + '>(C>' + t + '))', rule='ax1', subs=dict(A=t, B='C')),
                dict(f='(C>' + t + ')', rule='mp', refs=[0, 1])]
        syntax = a.Syntax()
        def translate(row):
            out = copy.deepcopy(row)
            out['f'] = syntax.text(syntax.parse(out['f']), True)
            if 'subs' in out:
                out['subs'] = {k: syntax.text(syntax.parse(v), True) for k, v in out['subs'].items()}
            return out
        images = [translate(row) for row in rows]
        def write(path, mode, rs, goal=None, duplicate=False):
            with gzip.open(path, 'wt') as stream:
                stream.write(json.dumps(dict(format=mode, goal=goal or rs[-1]['f'])) + '\n')
                for i, row in enumerate(rs):
                    raw = json.dumps(row)
                    if duplicate and i == 0: raw = raw[:-1] + ',"rule":"ax1"}'
                    stream.write(raw + '\n')
        write(native, 'native', rows); write(image, 'not-or', images)
        scan(f.FastSyntax, native, rows[-1]['f'], image)
        tests = [
            ('bad_native_formula', False, lambda rs: rs[0].update(f='A')),
            ('bad_substitution', False, lambda rs: rs[0]['subs'].update(A='B')),
            ('wrong_rule', False, lambda rs: rs[0].update(rule='axiom')),
            ('missing_substitution', False, lambda rs: rs[0]['subs'].pop('A')),
            ('future_reference', False, lambda rs: rs[-1].update(refs=[0, 3])),
            ('bool_reference', False, lambda rs: rs[-1].update(refs=[False, 1])),
            ('wrong_mp', False, lambda rs: rs[-1].update(refs=[1, 0])),
            ('image_formula', True, lambda rs: rs[0].update(f='A')),
            ('image_substitution', True, lambda rs: rs[0]['subs'].update(A='B')),
            ('extra_field', False, lambda rs: rs[0].update(assumption=True)),
            ('malformed_native_syntax', False, lambda rs: rs[0]['subs'].update(A='(A|B)'))]
        for name, in_image, mutate in tests:
            rs = copy.deepcopy(images if in_image else rows); mutate(rs)
            target = OUT / ('parser-' + RUN_TAG + '-' + name + '.jsonl.gz')
            write(target, 'not-or' if in_image else 'native', rs,
                  images[-1]['f'] if in_image else rows[-1]['f'])
            for backend in (a.Syntax, f.FastSyntax):
                try:
                    scan(backend, native if in_image else target, rows[-1]['f'],
                         target if in_image else image)
                except (ValueError, AssertionError, KeyError, TypeError): pass
                else: raise AssertionError('malformed record accepted: ' + name)
            result['rejections'].append(dict(name=name, both_backends=True))
        # The legacy scanner's image equality treats bool/float values as the
        # corresponding integers. Preserve the diagnostic; the new adapter
        # rejects these fields before comparing records. No source proof rule
        # or ordinary-Frege grammar is changed.
        for name, ref in [('image_bool_reference', False), ('image_float_reference', 0.0)]:
            rs = copy.deepcopy(images); rs[-1]['refs'][0] = ref
            target = OUT / ('parser-' + RUN_TAG + '-' + name + '.jsonl.gz')
            write(target, 'not-or', rs, images[-1]['f'])
            scan(a.Syntax, native, rows[-1]['f'], target)
            try: scan(f.FastSyntax, native, rows[-1]['f'], target)
            except ValueError: pass
            else: raise AssertionError('typed image reference accepted')
            result['rejections'].append(dict(name=name, legacy_accepted=True,
                                             strict_adapter_rejected=True))
        for name, mode, goal, duplicate in [
            ('duplicate_field', 'native', rows[-1]['f'], True),
            ('wrong_header', 'native', 'A', False),
            ('wrong_format', 'not-or', rows[-1]['f'], False),
            ('wrong_last_goal', 'native', rows[0]['f'], False)]:
            target = OUT / ('parser-' + RUN_TAG + '-' + name + '.jsonl.gz')
            write(target, mode, rows, goal, duplicate)
            for backend in (a.Syntax, f.FastSyntax):
                try: scan(backend, target, rows[-1]['f'] if name != 'wrong_last_goal' else goal, image)
                except (ValueError, AssertionError, KeyError, TypeError): pass
                else: raise AssertionError('malformed header accepted: ' + name)
            result['rejections'].append(dict(name=name, both_backends=True))
        result['complete'] = True
        save(VALIDATION, result)
        print('PASS three full local inputs, one full empty prefix pair,',
              len(result['rejections']), 'record rejections, including two repaired legacy acceptances;',
              VALIDATION.relative_to(ROOT), flush=True)
    except BaseException as exc:
        result['failures'].append(type(exc).__name__ + ': ' + str(exc))
        save(VALIDATION, result)
        raise


class ProgressStream:
    def __init__(self, stream, callback):
        self.stream, self.callback = stream, callback
        self.lines = 0

    def readline(self): return self.stream.readline()
    def __iter__(self): return self
    def __next__(self):
        raw = next(self.stream)
        self.lines += 1
        # Native stream read precedes checking the paired record, so only the
        # PREVIOUS record count is saved as completed. No certified prefix.
        if self.lines % 25000 == 0: self.callback(self.lines - 1)
        return raw
    def close(self): self.stream.close()


def replay(coordinate=0, dest=DEST, paths=None, step=207):
    DEST = dest
    ready = json.loads(VALIDATION.read_text())
    assert ready['complete'] and not ready['failures'], 'validate parser before replay'
    assert not DEST.exists(), 'preserve previous replay certificate'
    cert = dict(step=step, complete=False, failures=[], verified_exports=[],
                parser_validation=str(VALIDATION.relative_to(ROOT)), progress_records=0,
                pending=['full coordinate-' + str(coordinate) + ' replay', 'other coordinates',
                         'whole-star aggregate/argument implementation checks'])
    save(DEST, cert)
    started = time.monotonic()
    try:
        source = json.loads((OUT / 'certificate-205-star.json').read_text())
        prior = source['cases'][0]
        d = json.loads((ROOT / prior['request']).read_text()); tables = h.ep.request(d)
        cert['finite_tables'] = {k: tables[k] for k in ('K', 'beta', 'G')}
        assert all(tables[k] == prior['tables'][k] for k in ('K', 'beta', 'G'))
        inputs, imports = [], []
        a.syntax = f.FastSyntax()
        a.read = strict_read
        for v, path in enumerate(prior['inputs']):
            checked = a.scan(ROOT / path, h.ep.e.c.serialize(tables['local'][v]))
            inputs.append(checked); imports.append((ROOT / path, len(checked['rows'])))
        cert['local_inputs'] = [i['measurements'] for i in inputs]
        # Independently write the displayed original-input ledger; avoid using
        # measured output lengths or iterating bounds in derived packages.
        N = d['N']; hlog = (2 + N + d['n'] - 1).bit_length()
        V, H = 2**(3*hlog + 6), 9*hlog + 30
        G = (source['constants']['L'] + 1) * 10000 * N * V**2 * (H + 1)**2
        I = sum(len(x['rows']) for x in inputs); J = I + G
        frame = 256 + 64 * (J + 1).bit_length()
        bound = dict(h=hlog, V=V, H=H, elementary_operations=10000*N*V**2*(H+1)**2,
                     generated_records=G, imported_records=I, lines=J,
                     aggregate_lines=N*J, formats={})
        audit206 = json.loads((OUT / 'audit-206.json').read_text())
        assert audit206['constants']['actual'] == audit206['constants']['required'] == source['constants']
        # Library auxiliary name bound is measured by full library replay in
        # validation, not by a source hash or writer sidecar.
        library_names = 1
        for name, entry in ready['libraries'].items():
            with gzip.open(ROOT / entry['native']['path'], 'rb') as stream:
                next(stream)
                for raw in stream:
                    row = a.read(raw)
                    for s in [row['f']] + list(row.get('subs', {}).values()):
                        library_names = max(library_names, a.syntax.stats[a.syntax.parse(s)][4])
        for mode, factor, off in [('native', 3, 0), ('not-or', 6, 2)]:
            ts = [a.syntax.stats[a.syntax.parse(s)] for s in d['suffixes'] + d['letters'] +
                  ['(' + d['q'] + '>' + d['q'] + ')', '(~(' + d['q'] + '>' + d['q'] + '))']]
            t, depth, names = max(s[off] for s in ts), max(s[off+1] for s in ts), max(s[4] for s in ts)
            K = sum(x['node_sums'][mode] for x in inputs)
            delta = max(x['depths'][mode] for x in inputs)
            B = max(1, names, library_names, *(x['name_bytes'] for x in inputs))
            Dlib, S = source['constants'][mode]['D'], source['constants'][mode]['S']
            P = 8*4**(H+1)*(t+1)
            size = (B+4)*(K+(G+1)*S*P) + (J+2)*frame
            bound['formats'][mode] = dict(lines=J, depth=max(delta, Dlib+factor*H+depth),
                record_nodes=max(K, S*P), bytes=size, bits=8*size, aggregate_bytes=N*size,
                aggregate_bits=8*N*size, argument_nodes=P, argument_depth=factor*H+depth,
                input_term_nodes=t, input_term_depth=depth, imported_nodes=K,
                imported_depth=delta, payload_bytes=B)
        assert bound == prior['uniform_ledger'], 'independent ledger mismatch'
        cert['uniform_ledger'] = bound
        save(DEST, cert)
        if paths is None:
            paths = [OUT / ('star-205-coordinate-0.' + mode + '.jsonl.gz')
                     for mode in ('native', 'not-or')]
        root = json.loads(paths[0].with_name(paths[0].name + '.writer.json').read_text())['lines'] - 1
        expected = h.ep.e.c.serialize(tables['closed'][coordinate])
        original_open = a.gzip.open
        def callback(completed):
            cert['progress_records'] = completed
            save(DEST, cert)
            print('full paired primitive replay checked', completed, 'records;',
                  'unverified until final endpoint/EOF/hash/ledger checks', flush=True)
        def progress_open(path, *args, **kwargs):
            stream = original_open(path, *args, **kwargs)
            return ProgressStream(stream, callback) if Path(path) == paths[0] else stream
        a.gzip.open = progress_open
        try:
            checked = a.scan(paths[0], expected, paths[1], {root: expected}, imports)
        finally:
            a.gzip.open = original_open
        out = dict(coordinate=coordinate, root=root, complete_input_retention=True,
                   exact_endpoint=True, literal_image=True, proofs={})
        for mode, path in zip(('native', 'not-or'), paths):
            measured = checked['measurements'][mode]
            writer = json.loads(path.with_name(path.name + '.writer.json').read_text())
            assert all(writer[k] == measured[k] for k in ('lines', 'bytes', 'sha256'))
            checks = h.ledger.check(measured, bound['formats'][mode])
            assert checked['depths'][mode] <= bound['formats'][mode]['depth']
            out['proofs'][mode] = dict(measurement=measured, uniform_checks=checks,
                                      full_field_depth=checked['depths'][mode], writer_matches=True)
            print(mode, 'lines actual/required', measured['lines'], '/', bound['lines'],
                  'bytes actual/required', measured['bytes'], '/', bound['formats'][mode]['bytes'],
                  'depth actual/required', checked['depths'][mode], '/', bound['formats'][mode]['depth'],
                  'record nodes actual/required', measured['max_record_nodes'], '/',
                  bound['formats'][mode]['record_nodes'], flush=True)
        cert['verified_exports'] = [out]
        cert['progress_records'] = len(checked['rows'])
        cert['complete'] = True
        cert['pending'].remove('full coordinate-' + str(coordinate) + ' replay')
        cert['scope'] = 'One prefix pair only; whole-star export and argument checks remain open'
        save(DEST, cert)
        print('PASS star coordinate', coordinate, 'pair;', DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc))
        save(DEST, cert)
        raise
    finally:
        cert['elapsed_seconds'] = round(time.monotonic() - started, 3)
        save(DEST, cert)
        if isinstance(a.syntax, f.FastSyntax): a.syntax.close()
        a.read = original_read


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['validate', 'replay'])
    args = parser.parse_args()
    validation() if args.action == 'validate' else replay()
