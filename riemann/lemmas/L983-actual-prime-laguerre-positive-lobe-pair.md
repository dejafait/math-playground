# Lemma 983: a positive compensated actual-prime Laguerre lobe pair

## Hypotheses

Let Lambda be the actual von Mangoldt function: Lambda(p^k)=log p
for primes p and integers k>=1, and zero otherwise. For integers n>=2 put
ell_n(u)=L_(n-1)^(1)(u). Write its positive roots in increasing order
as r_(n,1),...,r_(n,n-1), and put r_(n,0)=0. For even j>=0 with
j+2<=n-1 define

    B_(n,j)=sum_(exp(r_(n,j))<m<=exp(r_(n,j+2)))
                Lambda(m)*ell_n(log m)/m
              -integral_(r_(n,j))^(r_(n,j+2)) ell_n(u)du.

The lower endpoint is excluded and the upper endpoint fully included.
This is the finite compensated observable proposed in review232;
L981/L982 supply notation and normalization context only, not theorem
inputs. No RH, PNT, zero data, n-uniform estimate or sign is assumed.

## Conclusion

The actual-prime pair at n=6,j=2 satisfies

    0.000387466780 < B_(6,2) < 0.000387466781.        (1)

Consequently the proposed rule B_(n,j)<=0 for every complete even
lobe pair is false. This refutes only that sign rule: it is neither a
disproof of RH nor an obstruction to bounds allowing positive pairs,
aggregate cancellation, or other compensation. No estimate for the
full growing Li head is obtained.

This is a local, computer-assisted finite negative result from step233,
10 November2026. Review232's bounded search did not locate this
diagnostic; originality beyond the sources checked is not certified.

## Proof

### Cited polynomial and exact root isolation

Import the finite polynomial formula
[NIST DLMF18.5.12](https://dlmf.nist.gov/18.5.E12), degree n-1,
parameter1. Its full specialization was checked in L982 and in the
pre-existing reviews231/232. At n=6 it gives, for every real u,

    ell_6(u)=6-15u+10u^2-(5/2)u^3+u^4/4-u^5/120.
    A(u)=120*ell_6(u)=720-1800u+1200u^2-300u^3+30u^4-u^5.

No Laguerre asymptotics or new special-function identity is used.
One may isolate this particular polynomial directly: put S=10^50.
Its five disjoint root brackets are (a_i/S,(a_i+1)/S), where

    i  a_i                                                   endpoint signs of A
    1  61703085327827039571434125908990247582755211936207       + -
    2  211296595857852415114143230335529919752495121067050      - +
    3  461083315101753241368336105082561652567227838524380      + -
    4  839906697120484219047673404665030139501260394839781      - +
    5  1426010306592083084898413134007888040596261433632578     + -

These signs are exact integer checks: at a/S the sign is the sign of
sum_(h=0)^5 A_h*a^h*S^(5-h), and similarly at (a+1)/S, using the
integer coefficient vector (720,-1800,1200,-300,30,-1). Both supplied
scripts check all five pairs. The intermediate value theorem supplies
a root in each open bracket. Since A has degree5 and the brackets are
disjoint and positive, these exhaust its roots, each with multiplicity1.
Thus the second and fourth brackets select exactly r_(6,2),r_(6,4),
without an unverified root ordering or a numerical root finder.

### Rigorous logarithms, endpoints and complete arithmetic sum

Here is the error rule used for all logarithms, including endpoints.
For an integer m>=1, let k=floor(log_2 m), t=2^k and
z=(m-t)/(m+t), so 0<=z<1/3. Then

    log m=k*log2+2*sum_(h=0)^(R-1) z^(2h+1)/(2h+1)+rho_R(z),
    0<=rho_R(z)<=2*z^(2R+1)/[(2R+1)*(1-z^2)].       (2)

For log2 itself use z=1/3 and k=0 in the atanh expansion.
Formula(2) follows by integrating the finite geometric expansion of
1/(1-z^2); the residual is bounded by its nonnegative geometric
majorant. All sums and error bounds in the independent checker use
exact rational arithmetic, with R=50. They are rounded outward to
multiples of 1/Q, Q=10^30. The producer instead uses R=70 and
outward integer intervals of scale S, with the uniform tail bound

    rho_70(z)<=9/[4*141*3^141]<=1/S,  0<=z<=1/3.

The last inequality is an integer check. Every interval addition,
product and positive-integer division rounds its lower endpoint down
and its upper endpoint up. For multiplication use the minimum and
maximum of all four endpoint products; this handles either sign of
the polynomial and each summand. The two implementations share no
interval or logarithm code. Ordinary floating point is not used.

Applying(2) at 8,9,4442,4443 and comparing with the isolated root
brackets gives the strict, independently checked inequalities

    log8 < r_(6,2) < log9,
    log4442 < r_(6,4) < log4443.                     (3)

Thus exp(r_(6,2)) is strictly between8 and9, and exp(r_(6,4))
strictly between4442 and4443. The entire arithmetic range is exactly
9<=m<=4442. Neither endpoint is an integer, so no equality case or
half-weight convention arises. The certificate retains the exact
logarithm bounds proving(3).

The producer sieves every prime p<=4442 and enumerates p,p^2,...
until exceeding4442, retaining precisely the powers at least9. The
independent checker factors each integer9,...,4442 by exhaustive
trial division and keeps exactly those with one distinct prime factor.
It compares this full ordered list with every producer record. There
are637 retained powers, each uniquely represented as p^k. For each,
evaluate ell_6(k*log p) and multiply by log p/p^k using the bounds(2).
The identity log(p^k)=k*log p is exact. All637 log, polynomial and
summand enclosures from the producer are checked against the
independent, wider enclosures. The files preserve every term; no
truncated prime list, omitted higher power or preview is evidence.

### Compensation and the certified gap above zero

Use the polynomial antiderivative with zero constant

    F(u)=6u-(15/2)u^2+(10/3)u^3-(5/8)u^4+u^5/20-u^6/720.

Differentiation gives exactly ell_6. Evaluate F on the full rational
root intervals above, with outward interval Horner arithmetic.
This is the compensation from the exact lower root, not from0 or
from an integer. Define T as the full prime-power sum and
I=F(r_(6,4))-F(r_(6,2)). The independent certificate establishes
the following integer enclosures, all with common denominator Q:

    Q*T in [-11832505848542015561260854019139,
            -11832505848542015561260854017774],
    Q*I in [-11832893315322459101756645400398,
            -11832893315322459101756645400397],
    Q*(T-I) in [387466780443540495791381258,
                387466780443540495791382624].        (4)

The last interval is obtained by subtracting the upper bound for I
from the lower bound for T, and conversely for the upper endpoint.
It is strictly positive and lies strictly inside the interval in(1).
Thus(4) proves(1), with no appeal to sampling or floating-point signs.

### Reproduction and complete evidence

Run from the active notebook directory:

    python3 scripts/li-prime-laguerre/lobe_pair_233.py
    python3 scripts/li-prime-laguerre/verify_lobe_witness_233.py

The producer writes
scripts/li-prime-laguerre/lobe-pair-certificate-233.json;
the independent checker writes
scripts/li-prime-laguerre/lobe-witness-independent-233.json.
Both completed successfully with empty failure lists. The latter
checks every load-bearing root, endpoint and term of the positive
witness, not a JSON preview. The exact selected values in(4) and the
producer's finer B interval were also inspected directly.

The approved order was (3,0),(4,0),(5,0),(5,2),(6,0),(6,2).
The producer certified the first five negative before reaching(1):

    pair   outward decimal B interval
    3,0    [-1.220371280117, -1.220371280116]
    4,0    [-1.374912878987, -1.374912878986]
    5,0    [-1.452820967510, -1.452820967509]
    5,2    [-0.004186504155, -0.004186504154]
    6,0    [-1.489945470804, -1.489945470803]

Their full arithmetic certificates are retained; these negative
signs are auxiliary, not premises for the rejection. Computation
stopped at the first positive pair, exactly as approved. The
independent calculation here is verification of the same witness,
not a second research mechanism or a claim of external peer review.

The main gap in L030-L032/C032a and the signed forcing in L966/L968
remain unresolved. Even before rejection, the pair rule would have
left unmatched and terminal lobes unpaid. No n-uniform conclusion or
bound for P_n(X_n) is inferred from these finite signs.

## Mathlib

Full matching Mathlib coverage of this compensated finite statistic
has not been checked and is unknown. DLMF18.5.12 is the cited external
polynomial input. Exact integer/rational arithmetic in these Python
certificates is not Lean verification; no absence claim about Mathlib
or theorem beyond the finite statement is made.
