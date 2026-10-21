"""Literal request reconstruction, independent of emitter and rewrite planner."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'balanced-slot'))
import checker

def n(a): return ('not', a)
def i(a, b): return ('imp', a, b)
def x(a, b): return i(i(a, b), n(i(b, a)))
def e(a, b): return n(x(a, b))
def p(a, b): return n(i(a, n(b)))

def image(t):
    if isinstance(t, str): return t
    if t[0] == 'not': return n(image(t[1]))
    return ('or', n(image(t[1])), image(t[2]))

def encode(t, mode):
    if mode == 'not-or': t = image(t)
    elif mode != 'native': raise checker.Invalid('unknown mode')
    return checker.serialize(t)

def fixed(mode):
    a, b, c = 'A', 'B', 'C'
    return {k: encode(v, mode) for k, v in {
        'dist': e(p(a, x(b, c)), x(p(a, b), p(a, c))),
        'prod_cong': i(e(b, c), e(p(a, b), p(a, c))),
    }.items()}

def goal(factor_text, slot_texts, mode):
    a = checker.parse(factor_text, 'native')[0]
    ts = [checker.parse(t, 'native')[0] for t in slot_texts]
    m = len(ts)
    if m < 2 or m & (m-1): raise checker.Invalid('nonperfect slot request')
    def balanced(seq):
        if len(seq) == 1: return seq[0]
        k = len(seq)//2
        return x(balanced(seq[:k]), balanced(seq[k:]))
    return encode(e(p(a, balanced(ts)), balanced([p(a, t) for t in ts])), mode)
