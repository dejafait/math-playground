"""Reuse completed positive replays; finish the rejection harness separately."""
import copy
import gzip
import json
import run as r

h, p, OUT, ROOT = r.h, r.p, r.OUT, r.ROOT

def corrupt(path, destination, edit):
    touched = False
    with gzip.open(path, 'rb') as source, gzip.open(destination, 'wb', compresslevel=1) as target:
        for index, raw in enumerate(source):
            row = json.loads(raw)
            if not touched and edit(index, row):
                touched = True
                raw = (json.dumps(row, separators=(',', ':')) + '\n').encode('ascii')
            target.write(raw)
    assert touched

def primitive_rejections(cert):
    e = r.verify.e
    chosen = cert['cases'][3]
    original = json.loads((ROOT / chosen['input']).read_text())
    source, request = original['source'], original['request']
    expected = r.verify.contract(source, original['edges'], request)[0]
    S = [r.verify.c.parse(t, 'native')[0] for t in request['suffixes']]
    y, z = e.imp(source['q'], source['q']), e.neg(e.imp(source['q'], source['q']))
    terms = [e.prod(x, e.choose(request['Eb'][a][0], S, z)) for a, x in enumerate(source['letters'])]
    assert len(terms) == 3
    # Three positions require four-slot right padding, not this unpadded tree.
    wrong_sum = e.xor(terms[0], e.xor(terms[1], terms[2]))
    wrong_rhs = e.xor(z, e.xor(e.choose(request['E0'][0], S, z), wrong_sum))
    wrong_endpoint = r.verify.c.serialize(e.eq(S[0], wrong_rhs))
    assert wrong_endpoint != expected
    native = ROOT / chosen['vertices'][0]['measures']['native']['path']
    image = ROOT / chosen['vertices'][0]['measures']['not-or']['path']
    def bad_header(index, row):
        if index == 0: row['goal'] = wrong_endpoint; return True
        return False
    def bad_mp(index, row):
        if row.get('rule') == 'mp': row['refs'][0] = index - 1; return True
        return False
    def bad_image_sub(index, row):
        if row.get('rule') in ('ax1', 'ax2', 'ax3'):
            row['subs']['A'] = 'wrong'; return True
        return False
    jobs = [('wrong-padding-endpoint', native, bad_header, None),
            ('forward-MP-reference', native, bad_mp, None),
            ('literal-image-substitution', image, bad_image_sub, native)]
    for label, original_path, edit, paired_native in jobs:
        target = OUT / ('reject-212-' + label + '.jsonl.gz')
        assert not target.exists()
        corrupt(original_path, target, edit)
        r.audit.syntax = r.audit.Syntax()
        try:
            if paired_native: r.audit.scan(paired_native, expected, target)
            else: r.audit.scan(target, expected)
        except (AssertionError, ValueError) as error:
            cert['rejections'].append(dict(label=label, rejected=True, path=str(target.relative_to(ROOT)),
                reason=str(error) or ('exact header' if 'padding' in label else 'strictly earlier MP references')))
        else: raise AssertionError('accepted full-stream corruption ' + label)
        r.save(cert)

def main():
    prior = OUT / 'certificate-212-repaired.json'
    cert = json.loads(prior.read_text())
    assert len(cert['cases']) == 5 and all(case['complete'] for case in cert['cases'])
    assert cert['failures'] == ['Invalid: actual suffix/table/order/constant mismatch']
    cert['preserved_rejection_harness_failure'] = dict(path=str(prior.relative_to(ROOT)), failures=cert['failures'],
        repair='Catch the independent contract module Invalid class, rather than its separately loaded namesake.')
    cert['failures'] = []; cert['complete'] = False; cert['rejections'] = []
    cert['reused_positive_replays'] = str(prior.relative_to(ROOT))
    r.DEST = OUT / 'certificate-212-complete.json'
    assert not r.DEST.exists(); r.save(cert)
    try:
        original = json.loads((ROOT / cert['cases'][4]['input']).read_text())
        data = h.construct(original['source'])
        r.rejections(original['source'], data, cert)
        primitive_rejections(cert)
        # Exact repeated source occurrences, independently of equal name positions.
        lib = r.library(cert); packages, paths = r.extras()
        source = dict(tree=['add', ['var', 0], ['var', 0]], letters=['q'], q='q', delete_zero=False)
        r.test('repeated-subtree-212', source, lib, packages, paths, cert)
        cert['complete'] = True; r.save(cert)
        print('PASS', sum(len(case['vertices']) for case in cert['cases']),
              'complete local native/image pairs;', len(cert['rejections']), 'rejections;',
              r.DEST.relative_to(ROOT), flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__ + ': ' + str(error)); r.save(cert)
        raise

if __name__ == '__main__': main()
