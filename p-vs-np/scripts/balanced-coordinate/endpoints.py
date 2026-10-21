"""Request endpoints and literal translation, independent of the emitter."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'balanced-slot'))
import checker

def neg(a): return ('not', a)
def imp(a, b): return ('imp', a, b)
def xor(a, b): return imp(imp(a, b), neg(imp(b, a)))
def equiv(a, b): return neg(xor(a, b))
def balanced(ts):
    if len(ts) == 1: return ts[0]
    k = len(ts)//2
    return xor(balanced(ts[:k]), balanced(ts[k:]))
def image(t):
    if isinstance(t, str): return t
    if t[0] == 'not': return neg(image(t[1]))
    return ('or', neg(image(t[1])), image(t[2]))
def goal(us, vs, mode='native'):
    if len(us) != len(vs) or len(us) < 2 or len(us) & (len(us)-1):
        raise checker.Invalid('equal perfect lists of size at least two required')
    tree = equiv(balanced([checker.parse(u, 'native')[0] for u in us]),
                 balanced([checker.parse(v, 'native')[0] for v in vs]))
    if mode == 'not-or': tree = image(tree)
    elif mode != 'native': raise checker.Invalid('unknown format')
    return checker.serialize(tree)
def coordinate(u, v):
    return checker.serialize(equiv(checker.parse(u, 'native')[0], checker.parse(v, 'native')[0]))
def stats(t):
    if isinstance(t, str): return (1, 0, len(t))
    ss = [stats(a) for a in t[1:]]
    return (1+sum(s[0] for s in ss), 1+max(s[1] for s in ss), max(s[2] for s in ss))
