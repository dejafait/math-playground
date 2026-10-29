"""Supplement L141's complete replay with printed-value and quotient audits.

No new witnesses, local places or point searches. All evidence is saved.
The primary local-field/Kummer hypotheses are checked in the lemma audit.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'eleven-adic-filter-audit.json'
A = dict(completed=False, failures=[], checks=[], bindings={})


def load(name):
    raw = (ROOT / name).read_bytes()
    A['bindings'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def check(label, actual, required):
    A['checks'].append(dict(label=label, actual=actual, required=required,
                            passed=actual == required))
    assert actual == required, label


def main():
    d = load('eleven-adic-filter-certificate.json')
    v = load('eleven-adic-filter-verification.json')
    old = load('eleven-adic-filter-preaudit-verification.json')
    real = load('real-kummer-certificate.json')
    check('entire replay unchanged', v == old, True)
    check('producer completed without failure', [d['completed'], d['failures']], [True, []])
    check('replay completed without failure', [v['completed'], v['failures']], [True, []])
    check('replay check count', v['checks'], 12335)
    for name, digest in d['bindings'].items():
        raw = (ROOT / name).read_bytes()
        check('actual input hash ' + name, hashlib.sha256(raw).hexdigest(), digest)
    check('replay bound to producer', v['bindings']['eleven-adic-filter-certificate.json'],
          A['bindings']['eleven-adic-filter-certificate.json'])
    check('complete source witness records',
          [r['source'] for r in d['witnesses']] == real['witnesses'], True)
    check('complete replay witness order', [r['id'] for r in v['verified']],
          [r['id'] for r in d['witnesses']])
    check('complete replay product order', [r['coefficients'] for r in v['products']],
          d['real_kernel']['kernel'])

    # Check the small printed arithmetic independently of either field engine.
    check('H(r) factorization', 3**5 * 5**6 * 11**7, d['branch']['H_at_root'])
    check('H(r) rational unit', Q(d['branch']['H_at_root'], 11**7), Q(3796875))
    check('H(r) unit residue', 3796875 % 11, 5)
    check('9075 scalar', 75 * 11**2, 9075)
    check('quartic branch normalized residue', (75 * 10**2 * 45) % 11, 9)
    squares = sorted({x*x % 11 for x in range(1, 11)})
    check('complete nonzero residue squares', squares, [1, 3, 4, 5, 9])
    check('inverse norm of 2', Q(1, 2**4), Q(d['obstruction']['pair']['rational']['value']))
    check('inverse norm residue', pow(16, -1, 11), 9)
    check('2 is a nonsquare residue', 2 in squares, False)
    check('single rational-2 coefficient', d['obstruction']['coefficients'], 1 << 35)
    check('rational-2 source', real['witnesses'][35]['id'], 'rational-2')
    check('rational-2 actual representative', d['obstruction']['pair']['quartic']['u_coefficients'],
          [2, 0, 0, 0])
    check('rational-2 real signs', real['witnesses'][35]['sign_bits'], [0]*5)

    # In F*/F*2 the classes of u and 2 form a basis by the odd-residue
    # square criterion. N(u)=49500 has rational bits (1,0); N(2)=16
    # is a square. The product norm has bits (a+c,b) in the stated order.
    check('uniformizer norm', d['field']['shifted'][0], 11 * 4500)
    check('uniformizer norm unit residue', 4500 % 11, 1)
    cases = []
    for mask in range(16):
        a, b, c, e = [(mask >> i) & 1 for i in range(4)]
        norm_bits = [a ^ c, b]
        cases.append(dict(mask=mask, norm_bits=norm_bits,
                          norm_kernel=norm_bits == [0, 0],
                          branch_span=mask in (0, 5), quotient=e))
    kernel = [r['mask'] for r in cases if r['norm_kernel']]
    zero = [r['mask'] for r in cases if r['norm_kernel'] and not r['quotient']]
    check('full norm kernel', kernel, [0, 5, 8, 13])
    check('quotient kernel is complete branch span', zero, d['local_image_span'])
    check('quotient surjective', sorted({r['quotient'] for r in cases if r['norm_kernel']}), [0, 1])
    A['local_squareclass_cases'] = cases
    check('every witness norm class', all(r['pair']['mask'] in kernel for r in d['witnesses']), True)
    check('every product norm class', all(r['pair']['mask'] in kernel for r in d['products']), True)
    check('every saved quotient is the linear residue bit',
          [r['local_quotient'] for r in d['products']],
          [(r['pair']['mask'] >> 3) & 1 for r in d['products']])

    A['dimension_cases'] = [dict(c=c, ambient=11+c, real_filtered=9+c,
                                 combined=8+c, rank_bound=7+c,
                                 sufficient_bound=1, shortfall=6+c) for c in range(3)]
    check('unconditional upper bound', max(r['rank_bound'] for r in A['dimension_cases']),
          d['result']['unconditional_rank_upper_bound'])
    check('worst bound shortfall', max(r['shortfall'] for r in A['dimension_cases']),
          d['result']['shortfall'])
    A['actual_required'] = dict(witnesses=[len(d['witnesses']), 39],
                               products=[len(d['products']), 37],
                               local_squareclasses=[len(cases), 16],
                               class_dimension_cases=[len(A['dimension_cases']), 3],
                               rank_bound=[9, 1])
    A['producer_bounds'] = d['bounds']
    A['replay_bounds'] = v['bounds']
    for name, bounds in [('producer', d['bounds']), ('replay', v['bounds'])]:
        for value, limit in [('field_operations', 'field_operations_cap'),
                             ('max_rational_bits', 'rational_bits_cap'),
                             ('max_absolute_valuation', 'valuation_cap')]:
            check(name + ' within ' + limit, bounds[value] <= bounds[limit], True)
    A['completed'] = True


def encode(x):
    if isinstance(x, Q):
        return x.numerator if x.denominator == 1 else str(x)
    raise TypeError(type(x).__name__)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        A['failures'].append(str(exc))
        A['traceback'] = traceback.format_exc()
    OUT.write_text(json.dumps(A, indent=2, default=encode) + '\n')
    print(json.dumps(dict(completed=A['completed'], checks=len(A['checks']),
                          actual_required=A.get('actual_required'),
                          producer_bounds=A.get('producer_bounds'),
                          replay_bounds=A.get('replay_bounds'), failures=A['failures'],
                          certificate=str(OUT))))
    if not A['completed']:
        raise SystemExit(1)
