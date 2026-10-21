"""Approved finite chain minima; no infinite-length inference.

Finite coding is imported as documented in L020/L021 and the ready review.
Every row retains exact coefficients, parity residue, CRT root and endpoints.
"""

import json
from pathlib import Path


def parameters(j, h):
    return (3 ** (3*j+h),
            23 * 3**h * ((27**j-16**j)//11) + (3**h-2**h)*16**j,
            4*j+h+2)


def word(j, h):
    return 'OOEO'*j + 'O'*h + 'EE'


def coding(w):
    A, C, r = 1, 0, 0
    for i, letter in enumerate(w):
        q = 1 << i
        assert (A*r+C) % q == 0
        if ((A*r+C)//q) % 2 != (letter == 'O'):
            r += q
        if letter == 'O':
            A, C = 3*A, 3*C+q
    return A, C, r


def crt(r, q):
    n = r + q*((20-r)*pow(q, -1, 27) % 27)
    return n if n else 27*q


def replay(n, chain):
    states, ends, tails = [n], [], []
    for j, h in chain:
        for i, letter in enumerate(word(j, h)):
            x = states[-1]
            assert x > 0 and x % 2 == (letter == 'O')
            if i == 4*j+h:
                tails.append(x)
            states.append((3*x+1)//2 if letter == 'O' else x//2)
        ends.append(states[-1])
    assert all(x % 27 == 20 for x in [n]+ends)
    assert all(x % 2 == 1 for x in ends[:-1])
    assert all(t == 4*e for t, e in zip(tails, ends))
    assert all(e > x for x, e in zip([n]+ends[:-1], ends))
    return states, ends, tails


def main():
    alphabet = [(j, h) for j in range(2, 5) for h in range(3, 6)]
    single = {}
    for p in alphabet:
        A, C, D = parameters(*p)
        Ac, Cc, r = coding(word(*p))
        assert (A, C, D) == (Ac, Cc, len(word(*p)))
        assert A > (1 << D) and C > 0
        single[p] = A, C, D, r

    levels, minima = [], []
    previous = [dict(chain=[], A=1, C=0, D=0, parity_residue=0)]
    checks = dict(chains=0, whole_word_codings=0, guarded_replays=0,
                  compared_repeat_baselines=0, failed_checks=0)
    for k in range(1, 6):
        rows = []
        for old in previous:
            A0, C0, D0, r0 = (old[x] for x in ('A','C','D','parity_residue'))
            q0 = 1 << D0
            assert (A0*r0+C0) % q0 == 0
            endpoint0 = (A0*r0+C0)//q0
            for p in alphabet:
                Ai, Ci, Di, ri = single[p]
                qi = 1 << Di
                t = (ri-endpoint0)*pow(A0, -1, qi) % qi
                r = r0+q0*t
                A, C, D = Ai*A0, Ai*C0+q0*Ci, D0+Di
                q = 1 << D
                chain = old['chain']+[list(p)]
                w = ''.join(word(*x) for x in chain)
                assert coding(w) == (A, C, r)
                checks['whole_word_codings'] += 1
                n = crt(r, q)
                assert 0 < n <= 27*q and n % q == r and n % 27 == 20
                states, ends, tails = replay(n, chain)
                assert q*states[-1] == A*n+C
                checks['guarded_replays'] += 1
                # Also verify the next root in the complete positive CRT class.
                states_lift, ends_lift, _ = replay(n+27*q, chain)
                assert q*states_lift[-1] == A*(n+27*q)+C
                checks['guarded_replays'] += 1
                rows.append(dict(chain=chain, A=A, C=C, D=D,
                                 parity_residue=r, CRT_period=27*q,
                                 minimum_root=n, endpoints=ends,
                                 lifted_endpoints=ends_lift,
                                 final_endpoint_odd=bool(ends[-1] % 2)))
                checks['chains'] += 1
        assert len(rows) == 9**k
        best = min(rows, key=lambda row: row['minimum_root'])
        attaining = [row for row in rows if row['minimum_root'] == best['minimum_root']]
        assert len(attaining) == 1
        states, ends, tails = replay(best['minimum_root'], best['chain'])
        checks['guarded_replays'] += 1
        repeated = next(row for row in rows if row['chain'] == [[2,3]]*k)
        baseline_holds = best['minimum_root'] >= repeated['minimum_root']
        checks['compared_repeat_baselines'] += 1
        minima.append(dict(K=k, chains=len(rows), minimum_root=best['minimum_root'],
                           chain=best['chain'], A=best['A'], C=best['C'],
                           D=best['D'], parity_residue=best['parity_residue'],
                           CRT_period=best['CRT_period'], states=states,
                           endpoints=ends, pre_tail_states=tails,
                           final_endpoint_odd=best['final_endpoint_odd'],
                           repeated_minimum_parameters_root=repeated['minimum_root'],
                           repeated_baseline_holds=baseline_holds))
        levels.append(dict(K=k, rows=rows))
        previous = rows
    assert checks['chains'] == sum(9**k for k in range(1,6)) == 66429
    # This tests an implication, not an assumed assertion: a violation is evidence.
    violations = [dict(K=x['K'], achieved=x['minimum_root'],
                       proposed_lower_bound=x['repeated_minimum_parameters_root'])
                  for x in minima if not x['repeated_baseline_holds']]
    result = dict(result='PASS', scope='K=1,...,5; 2<=J<=4; 3<=H<=5; E^2',
                  checks=checks, minima=minima, repeat_baseline_violations=violations,
                  levels=levels,
                  limitations=['No uniform divergence for arbitrary J,H or K proved.',
                               'Final endpoint parity is not constrained.',
                               'No Collatz convergence conclusion.'])
    path = Path(__file__).with_name('result.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(result='PASS', checks=checks,
                         minima=[{key:x[key] for key in ('K','chains','minimum_root',
                                 'chain','final_endpoint_odd',
                                 'repeated_minimum_parameters_root',
                                 'repeated_baseline_holds')} for x in minima],
                         repeat_baseline_violations=violations,
                         required_uniform_bound='n>=F(K), F(K)->infinity for all J>=2,H>=3',
                         achieved_bound='Exact five finite minima only',
                         artifact=str(path)), indent=2))


if __name__ == '__main__':
    main()
