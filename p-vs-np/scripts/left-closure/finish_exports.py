"""Complete preserved diamond inputs; fully expanded exports and full replay.

Only lossless compression and spelling-cache policy differ from run.py.
No proof pruning, new inference rule, or supplied-record shortening occurs.
"""
import gzip
import hashlib
import json
from collections import OrderedDict
from functools import lru_cache
import run as h

OUT, ROOT = h.OUT, h.ROOT
DEST = OUT / 'certificate-203.json'


class Spelling:
    def __init__(self, image):
        self.image = image
        self.cache = OrderedDict()
        self.bytes = 0
        self.limit = 32 * 1024 * 1024

    def text(self, f):
        key = id(f)
        if key in self.cache:
            held, value = self.cache.pop(key)
            assert held is f
            self.cache[key] = held, value
            return value
        if isinstance(f, str):
            value = f
        elif f[0] == 'n':
            value = '(~' + self.text(f[1]) + ')'
        else:
            assert f[0] == 'i'
            a, b = self.text(f[1]), self.text(f[2])
            value = '((~' + a + ')|' + b + ')' if self.image else '(' + a + '>' + b + ')'
        if len(value) <= self.limit:
            while self.cache and (self.bytes + len(value) > self.limit or len(self.cache) >= 32768):
                _, (_, old) = self.cache.popitem(last=False)
                self.bytes -= len(old)
            self.cache[key] = f, value
            self.bytes += len(value)
        return value


def write(self, path, image=False):
    spelling = Spelling(image)
    digest = hashlib.sha256()
    size = 0
    with gzip.open(path, 'wb', compresslevel=1) as stream:
        def put(row):
            nonlocal size
            raw = (json.dumps(row, separators=(',', ':')) + '\n').encode('ascii')
            size += len(raw)
            digest.update(raw)
            stream.write(raw)
        put({'format': 'not-or' if image else 'native',
             'goal': spelling.text(self.p.rows[self.root][0])})
        for index, (f, rule, refs, subs, deps) in enumerate(self.p.rows):
            assert not deps
            row = {'f': spelling.text(f), 'rule': rule}
            if rule == 'mp':
                row['refs'] = list(refs)
            else:
                row['subs'] = {k: spelling.text(v) for k, v in subs.items()}
            put(row)
            if (index + 1) % 250000 == 0:
                print(path.name, 'fully written records', index + 1, flush=True)
    result = dict(lines=len(self.p.rows), bytes=size, sha256=digest.hexdigest(),
                  storage_bytes=path.stat().st_size)
    path.with_name(path.name + '.writer.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


class ReplaySyntax(h.audit.Syntax):
    # Same complete parser/reconstructor, larger bounded spelling caches.
    parse = lru_cache(4096)(h.audit.Syntax.parse.__wrapped__)
    text = lru_cache(16384)(h.audit.Syntax.text.__wrapped__)


def fixture(name, lib):
    assert name == 'diamond-203'
    source = OUT / 'diamond-small-input.request.json'
    d = json.loads(source.read_text())
    (OUT / (name + '.request.json')).write_text(json.dumps(d, indent=2) + '\n')
    return d, [OUT / ('diamond-small-input-local-' + str(v) + '.native.jsonl.gz')
               for v in range(d['N'])]


def library(initial):
    lib = {}
    for name, goal in dict(h.b.ep.fixed(), close_cancel=h.ep.cancellation()).items():
        if name == 'close_cancel':
            path = OUT / 'close_cancel.native.jsonl.gz'
        elif name in ('zeroR', 'zeroL', 'prod_zero'):
            path = OUT.parent.parent / 'backward-zero' / 'output' / (name + '.native.jsonl.gz')
        else:
            location = 'balanced-distribution' if name in ('dist', 'prod_cong') else 'balanced-slot'
            path = OUT.parent.parent / location / 'output' / (name + '.native.jsonl.gz')
        lib[name] = h.b.aggregate.load(path, h.ep.e.c.serialize(goal))
        assert lib[name]['measurement']['sha256'] == initial['library'][name]['native']['sha256']
    return lib


def main():
    initial = json.loads((OUT / 'certificate-202.json').read_text())
    cert = dict(step=203, library=initial['library'], constants=initial['constants'],
                reused_complete_empty_evidence='scripts/left-closure/output/certificate-202.json',
                reused_rejections='scripts/left-closure/output/rejections-202.json',
                cases=[], failures=[], complete=False)
    h.DEST = DEST
    h.save(cert)
    try:
        lib = library(initial)
        # Check the changed writer's two spellings against the original writer
        # on every complete fixed library record and every substitution field.
        for image in (False, True):
            spell = Spelling(image)
            for package in lib.values():
                for f, rule, refs, subs in package['rows']:
                    for term in [f] + list((subs or {}).values()):
                        assert spell.text(term) == h.p.text(term, image)
        cert['writer_fixed_field_comparison'] = True
        h.lc.Closure.write = write
        h.audit.syntax = ReplaySyntax()
        h.fixture = fixture
        d, paths, obj, record = h.test_case('diamond-203', lib, cert)
        assert obj.tables['beta'] == [[0], [1], [1], [1]]
        assert obj.tables['K'][0][3] == 0 and sum(obj.tables['K'][0]) == 3
        assert obj.tables['G'][0][0][3] == 1
        cert['discriminators'] = dict(two_constant_paths_cancel=True,
            surviving_beta=True, variable_after_constant_closure=True,
            nonpower_selection=True, repeated_names=True, deep_unused_input=True)
        cert['complete'] = True
        h.save(cert)
        print('PASS four complete nontrivial native/image export pairs;', DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc))
        h.save(cert)
        raise


if __name__ == '__main__':
    main()
