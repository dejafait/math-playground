"""Exact approved pair screen. Finite checks do not establish convergence."""

import json
from pathlib import Path


def parameters(j, h, a):
    return (3 ** (3*j+h),
            23 * 3**h * ((27**j-16**j)//11) + (3**h-2**h)*16**j,
            4*j+h+a)


def word(p):
    j, h, a = p
    return "OOEO"*j + "O"*h + "E"*a


def coding(w):
    # The inspected one-bit finite-word coding construction.
    A, C, r = 1, 0, 0
    for i, letter in enumerate(w):
        q = 1 << i
        assert (A*r+C) % q == 0
        if ((A*r+C)//q) % 2 != (letter == "O"):
            r += q
        if letter == "O":
            A, C = 3*A, 3*C+q
    return A, C, r


def crt(r, q, b=20, odd_modulus=27):
    n = r + q * ((b-r)*pow(q, -1, odd_modulus) % odd_modulus)
    return n if n else q*odd_modulus


def replay(n, w):
    states = [n]
    for letter in w:
        x = states[-1]
        assert x > 0 and x % 2 == (letter == "O")
        states.append((3*x+1)//2 if letter == "O" else x//2)
    return states


def valuation(x, p):
    assert x > 0
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def check():
    first = [(j,h,a) for j in range(2,13) for h in range(3,13)
             for a in (2,20) if a < j+h+(2-j-h)%18]
    second = [(j,h,a) for j in range(2,13) for h in range(3,13)
              for a in (2,20)]
    counts = dict(pairs=0, first_never_overshoots=0,
                  noncontracting_composition=0, compensating=0,
                  all_positive_roots_margin=0, positive_CRT_lifts_needed=0)
    rows = []
    replays = 0
    for p1 in first:
        A1,C1,D1 = parameters(*p1)
        for p2 in second:
            counts['pairs'] += 1
            A2,C2,D2 = parameters(*p2)
            A,C,D = A2*A1,A2*C1+(1<<D1)*C2,D1+D2
            q, delta = 1<<D, (1<<D)-A
            w = word(p1)+word(p2)
            Ac,Cc,r = coding(w)
            assert (Ac,Cc,len(w)) == (A,C,D)
            n0, period = crt(r,q), 27*q
            # Minimal strict final-descent lift, if one can exist.
            k = max(0, (C-delta*n0)//(delta*period)+1) if delta > 0 else 0
            n = n0+k*period
            overshoot = (A1-(1<<D1))*n+C1 > 0
            descent = delta*n > C
            category = ('first_never_overshoots' if (1<<D1)-A1 > C1
                        else 'noncontracting_composition' if delta <= 0
                        else 'compensating')
            counts[category] += 1
            if category == 'compensating':
                assert A1 > (1<<D1) and overshoot and descent
                counts['all_positive_roots_margin'] += (delta > C)
                counts['positive_CRT_lifts_needed'] += (k > 0)
            elif category == 'first_never_overshoots':
                assert p1[2] == 20 and not overshoot
            else:
                assert not descent
            # Check the joint word even on rejected cases, and a second lift
            # when the proof asserts an unbounded compensating family.
            lifts = (n,n+period) if category == 'compensating' else (n0,)
            for root in lifts:
                states = replay(root,w)
                x,y = states[D1],states[-1]
                assert root % 27 == x % 27 == y % 27 == 20
                assert (1<<D1)*x == A1*root+C1
                assert q*y == A*root+C
                assert (x > root) == ((A1-(1<<D1))*root+C1 > 0)
                assert (y < root) == (delta*root > C)
                if category == 'compensating':
                    assert root < x and y < root and y < x
                    assert valuation(states[4*p1[0]+p1[1]],2) == p1[2]
                replays += 1
            rows.append(dict(first=p1,second=p2,category=category,A=A,C=C,
                             D=D,delta=delta,CRT_root=n0,first_lift=k))
    assert len(first) == 120 and len(second) == 220
    assert counts['pairs'] == 26400 and counts['first_never_overshoots'] == 2200
    # Minimal-parameter joint witness; impose an odd final endpoint too.
    p1,p2 = (2,3,2),(2,3,20)
    w = word(p1)+word(p2)
    A,C,D = parameters(*p1)[0]*parameters(*p2)[0], 0, len(w)
    Ac,Cc,r = coding(w+'O')
    q = 1<<(D+1)
    nstar = crt(r,q,47,59049)
    witness_members = []
    for t in (0,1,2):
        n = nstar+59049*q*t
        states = replay(n,w)
        x,y = states[len(word(p1))],states[-1]
        assert x > n > y > 0 and y % 2 == 1
        assert n % 59049 == 47 and x % 27 == y % 27 == 20
        assert valuation(n+7,3) == valuation(4*n+1,3) == 3
        assert valuation(128*n-157,3) == 3
        assert n % 19683 != 4529 and n % 59049 != 17813
        assert valuation(states[11],2) == 2
        assert valuation(states[24],2) == 20
        witness_members.append(dict(t=t,root=n,first_endpoint=x,final_endpoint=y))
    A1,C1,D1 = parameters(*p1)
    A2,C2,D2 = parameters(*p2)
    C = A2*C1+(1<<D1)*C2
    assert Ac == 3*A and Cc == 3*C+(1<<D)
    assert (1<<D)-A > C and A1 > (1<<D1)
    result = dict(result='PASS',scope='approved bounded pair screen',counts=counts,
                  guarded_replays=replays,failed_checks=0,
                  witness=dict(first=p1,second=p2,A=A,C=C,D=D,
                               delta=(1<<D)-A,root_period=59049*q,
                               first_endpoint_period=59049*(1<<(D+1-D1))*A1,
                               final_endpoint_period=2*59049*A,
                               members=witness_members),pairs=rows)
    path = Path(__file__).with_name('result.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(result='PASS',counts=counts,guarded_replays=replays,
                         failed_checks=0,witness=result['witness'],artifact=str(path)),indent=2))


if __name__ == '__main__':
    check()
