#!/usr/bin/env python3
"""Independent fixed-prefix C874d audit; no original calculation imports."""
from fractions import Fraction as Q
from math import factorial, lcm
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'contact-joint-eighth-audit-2138.json'
N = 8


def coefficient(n, weights, exponential):
    """Enumerate weighted multiplicities, not a differential recurrence."""
    total = Q(0)

    def visit(k, remaining, count, term):
        nonlocal total
        if k > N:
            if remaining == 0:
                if exponential:
                    total += term
                elif count:
                    total += (-1)**(count+1)*factorial(count-1)*term
            return
        for r in range(remaining//k+1):
            visit(k+1, remaining-k*r, count+r,
                  term*weights[k]**r/factorial(r))

    visit(1, n, 0, Q(1))
    return total


def bareiss(matrix):
    """Integer fraction-free determinant, checking every exact division."""
    a = [[int(x) for x in row] for row in matrix]
    assert all(Q(x).denominator == 1 for row in matrix for x in row)
    previous, sign = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k+1, len(a)) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = pivot*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def main():
    original = json.loads((HERE/'contact-joint-eighth-2136.json').read_text())
    failures, cases = [], []

    def check(label, condition):
        if not condition:
            failures.append(label)
        return bool(condition)

    # Transcribed independently from the canonical lemma, not its certificate.
    printed_moments = [
        [1,32,3048,480480,105369600,29540367360,10069614213120,
         4037455266324480,1859834232358502400],
        [1,32,3036,474720,102814320,28336815360,9451312960320,
         3689859436623360,1646693332245561600]]
    printed_minors = [
        [[1,2024,47818387968,32047441048690659164160,
          1113320215666725432364725174570634444800],
         [32,6085056,22170797473628160,3171834202320787053983721062400]],
        [[1,2012,45759617664,27742027033267458785280,
          792393220741088901384242612269586841600],
         [32,5973744,20391579281571840,2526910082682282506355690700800]]]
    printed_ranges = [
        ([-4515752751821095680,192518530198606080,-1857734766859104,
          5721433136496],5164225291),
        ([-10943217259009823932489936080,475499290956877065938028480,
          -4697270560306343513497752,14878444773974024956464],
         13878122568316374391)]

    for index, s2 in enumerate((2,3)):
        name = ('rank_one','rank_two')[index]
        source = original['cases'][index]
        s = [Q(0),Q(16),Q(s2)]+[Q(2)]*6
        weights = [Q(0)]+[-s[k]/k for k in range(1,N+1)]
        a = [coefficient(n,weights,True) for n in range(N+1)]
        m = [(-1)**j*factorial(2*j)*a[j] for j in range(N+1)]
        logarithm = [Q(0)]+[coefficient(n,a,False) for n in range(1,N+1)]
        recovered = [-k*logarithm[k] for k in range(1,N+1)]
        for field, value in [('S_1_through_S_8',s[1:]),('coefficients',a),
                             ('independent_product_coefficients',a),('moments',m),
                             ('logarithm_coefficients',logarithm),
                             ('recovered_S_1_through_S_8',recovered)]:
            check(name+'/'+field, value == list(map(Q,source[field])))
        check(name+'/printed complete moment tuple',m == printed_moments[index])
        check(name+'/prescribed finite logarithm',recovered == s[1:])
        check(name+'/printed a8',a[8] == (Q(4000066,45),Q(453331207,5760))[index])
        matrices = {}
        for j,(label,size,shift) in enumerate((('A_4',5,0),('B_3',4,1))):
            matrix = [[m[i+k+shift] for k in range(size)] for i in range(size)]
            minors = [bareiss([row[:r] for row in matrix[:r]]) for r in range(1,size+1)]
            old = source['matrices'][label]
            check(name+'/'+label+'/all entries',matrix == [list(map(Q,row)) for row in old['matrix']])
            check(name+'/'+label+'/symmetry',all(matrix[i][k]==matrix[k][i]
                  for i in range(size) for k in range(size)))
            check(name+'/'+label+'/certificate minors',minors == list(map(Q,old['leading_minors'])))
            check(name+'/'+label+'/printed minors',minors == printed_minors[index][j])
            check(name+'/'+label+'/strict threshold',all(d>0 for d in minors))
            matrices[label] = dict(matrix=matrix,leading_minors=minors,required_strict_lower_bound=0)
        b, v = matrices['B_3']['matrix'],m[5:9]
        determinant = bareiss(b)
        numerators = []
        for j in range(4):
            replaced = [[v[i] if k==j else b[i][k] for k in range(4)] for i in range(4)]
            numerators.append(bareiss(replaced))
        q = [Q(x,determinant) for x in numerators]
        denominator = lcm(*(x.denominator for x in q))
        common_numerators = [int(x*denominator) for x in q]
        residual = [sum((b[i][j]*q[j] for j in range(4)),Q(0))-v[i] for i in range(4)]
        check(name+'/range column',v == list(map(Q,source['even_range_column'])))
        check(name+'/Cramer solution',q == list(map(Q,source['range_solution'])))
        check(name+'/printed numerators and denominator',
              (common_numerators,denominator)==printed_ranges[index])
        check(name+'/complete range residual',residual == [Q(0)]*4 == list(map(Q,source['range_residual'])))
        cases.append(dict(name=name,S=s[1:],coefficients=a,moments=m,
            logarithm_coefficients=logarithm,recovered_S=recovered,matrices=matrices,
            range_column=v,Cramer_determinant=determinant,Cramer_numerators=numerators,
            range_solution=q,common_numerators=common_numerators,
            common_denominator=denominator,range_residual=residual))

    report = dict(step='2138',method='multiplicity sums; integer Bareiss; Cramer rule',
        cases=cases,strict_minors_checked=18,failures=failures,all_checks_pass=not failures,
        scope='two fixed finite prefixes only; theorem and analytic interpretation audited in C874d')
    OUT.write_text(json.dumps(encode(report),indent=2)+'\n')
    for c in cases:
        print(f"{c['name']}: m8={c['moments'][8]}, recovered S8={c['recovered_S'][7]}")
        for label,data in c['matrices'].items():
            print(f"  {label} minors={data['leading_minors']}; required each >0")
        print(f"  range residual={c['range_residual']}; required zero")
    print(f"strict minors=18; failures={failures}; certificate={OUT}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
