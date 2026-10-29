"""Critical L148 formula audit, using literal power-basis arithmetic only.

This supplements the independent maximal-order replay. It imports neither
producer nor replay and uses no numerical root proposal or factorization.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'branch-annihilator-audit.json'
R = dict(completed=False, checks=0, failures=[], bindings={}, evidence={})
A = list(map(Q, [-109375, -32500, 150, 64, 1]))


def ck(ok, name):
    R['checks'] += 1
    assert ok, name


def load(name):
    raw = (ROOT / name).read_bytes()
    R['bindings'][name] = sha256(raw).hexdigest()
    return json.loads(raw)


def multiply(a, b):
    out = [Q(0)] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    for k in range(6, 3, -1):
        for j in range(4):
            out[k - 4 + j] -= out[k] * A[j]
    return out[:4]


def from_order(w):
    a, b, c, d = map(Q, w)
    return [a+c/2+Q(31, 30)*d, b+Q(7, 25)*c+Q(179, 750)*d,
            c/50+Q(239, 18750)*d, d/18750]


def value(p, x):
    return sum(Q(c)*x**j for j, c in enumerate(p))


def interval(p, lo, hi):
    # I is negative; each monomial is monotone there. Sum exact enclosures.
    ck(lo < hi < 0, 'negative ordered interval')
    pairs = [[Q(c)*lo**j, Q(c)*hi**j] for j, c in enumerate(p)]
    return [sum(map(min, pairs)), sum(map(max, pairs))]


def valuation(q, p):
    q, v = Q(q), 0
    ck(q != 0, 'nonzero valuation input')
    while q.numerator % p == 0:
        q /= p
        v += 1
    while q.denominator % p == 0:
        q *= p
        v -= 1
    return v


def main():
    C = load('branch-annihilator-certificate.json')
    V = load('branch-annihilator-verification.json')
    M = load('odd-membership-35-certificate.json')
    U = load('odd-membership-35-audit.json')
    for name, doc in [('producer', C), ('replay', V), ('input', M), ('input audit', U)]:
        ck(doc['completed'] and not doc['failures'], name+' completed without failures')
    for doc in [C, V, U]:
        for name, digest in doc['bindings'].items():
            ck(sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'complete bound input '+name)
    ck(sha256((ROOT/'branch_annihilator.py').read_bytes()).hexdigest() == C['source_sha256'], 'producer source binding')
    ck(C['alpha_polynomial'] == A, 'actual A')
    H = list(map(Q, [52615361700000000, -15306287040000, 1581228000, -67760, 1]))
    ck(list(map(Q, M['model']['H'])) == H, 'actual quartic H')
    branch = from_order([-8085, -220, 440, -1320])
    eta = [Q(9075)-branch[0]] + [-x for x in branch[1:]]
    ck(multiply(eta, [Q(-50), Q(1), Q(0), Q(0)]) == [Q(-907500), 0, 0, 0], 'literal eta inverse formula')
    ck(from_order(M['model']['eta_O']) == eta, 'accepted actual eta')
    h = Q(73990352390625)
    ck(value(H, Q(9075)) == h == 3**5*5**6*11**7, 'branch evaluation and factorization')
    ck(Q(C['branch']['rational']) == h and list(map(Q, C['branch']['quartic_power'])) == branch, 'producer actual branch')
    q1, q2 = Q(1, 2405700000000000000), Q(1, 26730000000000)
    w1, w2 = [458232, 67632, 251664, -472680], [-73548, -2988, -56376, 138360]
    b1, b2 = from_order(w1), from_order(w2)
    for rec, mask, q, w, detection in zip(M['selected_pair'], [165,132102], [q1,q2], [w1,w2], [1713291454,1713217696]):
        ck(rec['coefficients'] == mask and Q(rec['rational']) == q and list(map(Q, rec['quartic_O'])) == w, 'literal fixed Selmer representative')
        ck(rec['local_detection'] == detection, 'accepted nonzero localization tuple')
    ck(1713291454 != 1713217696 and 1713291454 and 1713217696, 'nonzero distinct accepted tuples')
    t = Q(13341611250000000)
    s = from_order([Q(10519,1500), Q(67,225), Q(5471,4500), Q(-947,375)])
    printed = list(map(Q, ['225497/45000','6653/187500','-73819/9375000','-947/7031250']))
    ck(s == printed == list(map(Q, C['comparisons'][0]['quartic_root_power_ascending'])), 'both printed root bases and certificate')
    s2 = multiply(s, s)
    ck(s2 == list(map(Q, ['301578101/12656250','33593417/421875000','-300309097/7031250000','-45107557/63281250000'])), 'all printed square coefficients')
    ck(t*t*q1 == h and multiply(s2, b1) == branch, 'both direct positive component identities')
    ck(valuation(h, 3) == 5, 'nonzero branch square class')
    ck(s != [0]*4 and b1 != [0]*4 and branch != [0]*4 and t != 0, 'nonzero field components')
    lo, hi = Q(-3105933,65536), Q(-776483,16384)
    endpoints = [value(A, lo), value(A, hi)]
    ck(endpoints == list(map(Q, ['1222606091777206673/18446744073709551616','-40592557146770991/72057594037927936'])), 'printed A endpoints')
    ck(endpoints[0] > 0 > endpoints[1], 'root existence by strict sign change')
    ni, di = interval(branch,lo,hi), interval(b2,lo,hi)
    ck(ni == list(map(Q, ['-166956019462677687/687194767360000','-10684080015131015449/43980465111040000'])), 'printed branch interval')
    ck(di == list(map(Q, ['404687349923679358827/43980465111040000','6324542858191440901/687194767360000'])), 'printed eta-class interval')
    ck(ni[1] < 0 < di[0], 'negative ratio in actual real embedding')
    real = V['real_nonsquare']
    ck(list(map(Q,real['alpha_interval'])) == [lo,hi] and list(map(Q,real['A_end_values'])) == endpoints, 'replay exact real embedding')
    ck(list(map(Q,real['branch_interval'])) == ni and list(map(Q,real['eta_class_interval'])) == di, 'replay exact enclosures')
    product_ratio = h/(q1*q2)
    ck(product_ratio == 4757902330643963015625000000000000000000000000, 'printed product rational ratio')
    ck(valuation(product_ratio,3) == 17 == V['product_rational_3_valuation'], 'printed odd product valuation')
    ck(Q(C['comparisons'][1]['rational']['value']) == h/q2 and C['comparisons'][1]['rational']['is_square'], 'eta rational ratio')
    ck(Q(C['comparisons'][2]['rational']['value']) == product_ratio, 'producer exact product ratio')
    for rec, label, denominator in zip(C['comparisons'], ['epsilon','eta_class','epsilon*eta_class'], [b1,b2,multiply(b1,b2)]):
        ck(rec['denominator'] == label and multiply(list(map(Q,rec['quartic_ratio_power_ascending'])),denominator) == branch, 'all four coordinates of '+label+' ratio')
    ck([rec['equal'] for rec in C['comparisons']] == [True,False,False], 'all three certified decisions')
    R['evidence'] = dict(branch_rational=h, branch_power=branch, epsilon_root_Q=t,
        epsilon_root_power=s, epsilon_root_square=s2, real_interval=[lo,hi],
        A_end_values=endpoints, branch_interval=ni, eta_class_interval=di,
        product_rational_ratio=product_ratio, product_3_valuation=17)
    R.update(completed=True, actual_comparisons=3, required_comparisons=3,
             arithmetic_correction_needed=False,
             qualification='Pairing theorem and proper-model hypotheses are reviewed in L148; arithmetic replay alone does not verify them.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        R['failures'].append(dict(message=str(error), traceback=traceback.format_exc()))
    R['source_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(R, indent=2, default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'], checks=R['checks'],
        failures=[e['message'] for e in R['failures']],
        actual=R.get('actual_comparisons'), required=3, path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
