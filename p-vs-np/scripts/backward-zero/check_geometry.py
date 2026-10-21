"""Step 193: bounded geometry only; this emits no primitive Frege proof.

Exercise the actual Rewrite.split recursion, saving every rotation. Independent
restriction/filtering checks are not a substitute for the all-size proof.
"""
import json
from functools import lru_cache
from pathlib import Path
import build as b

OUT = Path(__file__).resolve().parent / 'output' / 'geometry-193.json'


@lru_cache(None)
def shapes(n, offset=0):
    if n == 1:
        return (b.atom((1, offset), 'v' + str(offset)),)
    return tuple(b.X(a, c) for k in range(1, n)
                 for a in shapes(k, offset) for c in shapes(n-k, offset+k))


def ids(t):
    return [t[1][1]] if t[0] == 'a' else ids(t[1]) + ids(t[2])


def restrict(t, lo, hi):
    if t[0] == 'a':
        return t if lo <= t[1][1] < hi else None
    a, c = restrict(t[1], lo, hi), restrict(t[2], lo, hi)
    if a is None:
        return c
    if c is None:
        return a
    return b.X(a, c)


def encode(t):
    if t[0] == 'a':
        return t[1][1]
    return [encode(t[1]), encode(t[2])]


class Geometry(b.Rewrite):
    def __init__(self, tree, height_bound):
        # Deliberately omit Store/native proofs: only split's geometry is used.
        self.tree = tree
        self.bound = height_bound
        self.events = []
        self.max_height = b.height(tree)

    def rotate(self, path, direction):
        before = self.tree
        t = b.at(before, path)
        if direction == 'right':
            new = b.X(t[1][1], b.X(t[1][2], t[2]))
        elif direction == 'left':
            new = b.X(b.X(t[1], t[2][1]), t[2][2])
        else:
            raise AssertionError('unknown direction')
        self.tree = b.replace(before, path, new)
        assert ids(before) == ids(self.tree)
        height = b.height(self.tree)
        assert height <= self.bound, (height, self.bound)
        self.max_height = max(self.max_height, height)
        self.events.append({'path': list(path), 'direction': direction,
                            'before': encode(before), 'after': encode(self.tree),
                            'height': height, 'required_height': self.bound})


def single(tree, cut):
    n, h = len(ids(tree)), b.height(tree)
    run = Geometry(tree, h+1)
    run.split((), cut)
    expected = b.X(restrict(tree, 0, cut), restrict(tree, cut, n))
    assert run.tree == expected
    assert len(run.events) <= h
    return {'kind': 'single', 'source': encode(tree), 'cut': cut,
            'result': encode(run.tree), 'events': run.events,
            'actual_height': run.max_height, 'required_height': h+1,
            'actual_rotations': len(run.events), 'required_rotations': h}


def match(tree, target):
    h, g = b.height(tree), b.height(target)
    n = len(ids(tree))
    run = Geometry(tree, h+g+1)
    entries = []

    def visit(path, want):
        interval = ids(want)
        lo, hi = interval[0], interval[-1]+1
        current = b.at(run.tree, path)
        expected = restrict(tree, lo, hi)
        assert current == expected
        entries.append({'path': list(path), 'interval': [lo, hi],
                        'current': encode(current), 'restriction': encode(expected)})
        # Independently check composition for this interval and all its cuts.
        for mid in range(lo+1, hi):
            assert restrict(current, lo, mid) == restrict(tree, lo, mid)
            assert restrict(current, mid, hi) == restrict(tree, mid, hi)
        if want[0] == 'a':
            assert current == want
            return
        run.split(path, len(ids(want[1])))
        visit(path+(1,), want[1])
        visit(path+(2,), want[2])

    visit((), target)
    assert run.tree == target
    assert len(run.events) <= (n-1)*h
    return {'kind': 'match', 'source': encode(tree), 'target': encode(target),
            'entries': entries, 'events': run.events,
            'actual_height': run.max_height, 'required_height': h+g+1,
            'actual_rotations': len(run.events), 'required_rotations': (n-1)*h}


def main():
    cert = {'complete': False, 'proof_stream_check': False,
            'scope': 'all source shapes/cuts through 8 leaves; all source/target pairs through 6; larger shallow and pruned-prefix cases',
            'failures': [], 'cases': []}
    try:
        for n in range(2, 9):
            for tree in shapes(n):
                for cut in range(1, n):
                    cert['cases'].append(single(tree, cut))
        for n in range(1, 7):
            for tree in shapes(n):
                for target in shapes(n):
                    cert['cases'].append(match(tree, target))
        for n in (7, 8, 15, 16, 31, 32, 63, 64, 127, 128):
            leaves = [b.atom((1, i), 'v'+str(i)) for i in range(n)]
            target = b.balanced(leaves)
            source = b.X(b.balanced(leaves[:n//3]), b.balanced(leaves[n//3:]))
            cert['cases'].append(match(source, target))
            for count in (1, n//2+1, n-1):
                cert['cases'].append(match(restrict(source, 0, count),
                                          restrict(target, 0, count)))
        cert['complete'] = True
    except Exception as exc:
        cert['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
        raise
    finally:
        OUT.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
        cases = cert['cases']
        witness = max(cases, key=lambda a: a['actual_height']) if cases else None
        summary = {'complete': cert['complete'], 'cases': len(cases),
                   'rotations_checked': sum(a['actual_rotations'] for a in cases),
                   'largest_height_case': ({k: witness[k] for k in
                       ('kind', 'actual_height', 'required_height', 'actual_rotations', 'required_rotations')}
                       if witness else None), 'failures': cert['failures'],
                   'certificate': str(OUT.relative_to(Path(__file__).resolve().parents[2])),
                   'qualification': 'geometry only; no primitive proof strings emitted or checked'}
        OUT.with_name('geometry-193-summary.json').write_text(json.dumps(summary, indent=2)+'\n')
        print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
