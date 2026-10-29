# L116 — Interval-pole exclusion: conditional budget and height-only obstruction

## Hypotheses

Retain L101's unchanged L089–L090 family, fixed domains, finite
exceptions before member selection, one member and ordering, literal
F=G_o, and actual all-place heights. In particular, by L101,

    h_v=e(F_v/Q_p)n_p, n_p=max(0,-v_p(j(E))),
    H=sum_p n_p log p, s=sqrt(H)>xi>=5,
    delta=3317760, L=log(2 delta H), U=10 delta s L.

Here xi is the absolute constant in the cited finite-set prime theorem.
All logarithms are natural. L089's retained split height-30 property
gives n_3=30, as also recorded in L098's hypotheses. Put S={p:n_p>0},
and use exactly the source sets

    S1={primes p:p<=s},
    S2={primes dividing some nonzero h_v},
    S3={p:some v above p has h_v>=s}, A=S1 union S2 union S3,
    S_I=S intersect (s,U], A'=A union S_I,
    T=sum_(p in S_I minus A) log p.

The numerical relaxation in conclusion (3) has separate, weaker
hypotheses: finite nonnegative integer heights over Q with the same
H formula, delta, xi and sets. It does not satisfy or purport to
satisfy all the actual-family hypotheses above.

## Conclusion

1. The exact extra cost is theta(A')=theta(A)+T. A sufficient
   condition, using the inspected source bounds, for a prime ell
   outside A' in the unchanged P1+ interval is

       T<=M(H), M(H)=3 delta s L-(delta+2)s-xi.          (1)

   Such a prime would satisfy P2, P3 and v_ell(j(E))>=0 for this
   same member and field. The available scalar height bound is

       0<=T<=H-30 log 3.                               (2)

2. For every H>=10^24 under the hypotheses, the cap in (2)
   exceeds M(H), with explicit sufficient-bound deficit

       D(H)=H-30 log 3-M(H) > (998/1000)H.              (3)

   This is a deficit of the proposed upper estimate, not an estimate
   from below on actual T. The family has unbounded H, so its
   retained hypotheses do not impose a uniform upper-height window
   that repairs this estimate.
3. Even the interval-restricted finite-set benchmark can fail in
   the numerical relaxation: there are finite integer-height arrays
   with n_3=30, n_2=0, s>xi and rational 0<j<1728 for which A'
   contains every prime <=U. In these arrays

       2(theta(A')+xi)-U >= U/3+2xi > 0.                (4)

   Thus restricting the added set to the interval does not by itself
   turn the scalar numerical hypotheses into a sufficient theorem.

No actual L089 member has been shown to fail (1), no actual-family
nonexistence is established, and no ell-integrality premise is
discharged. This stops the automatic height-only enlargement, not
an enlargement using additional arithmetic information. No full
initial-data repair, IUT flaw or finite B>=A claim follows.

## Proof

### Imported theorem, scope and relevance

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-selected-prime-pole-exclusion-budget.md`.
Reuse its inspected statements from Mochizuki,
*Inter-universal Teichmuller Theory IV*, April 2020,
[87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf):
Proposition 2.1(ii), printed p.40, and the Corollary 2.2(ii) proof,
pp.44–45. For every finite rational-prime set B they give

    some prime outside B is <=2(theta(B)+xi),
    (2/3)x<=theta(x)<=(4/3)x for x>=xi,
    theta(A)<=(delta+2)s+2 delta s log(2 delta H).        (5)

The final display is the source's uncoarsened S1–S3 upper bound.
No new prime-distribution theorem or stronger effective estimate
is asserted. Current author/journal-byte authentication and L101's
explicit Legendre-adjunction qualification remain unchanged.

The main gap is original finite B>=A. This bounded test addresses
only L098's extra integrality premise. Its plausible use is to
choose a prime outside all rational poles while retaining L101's
same interval and P2/P3. A passing sufficient budget would permit
that application; failure of the retained scalar bounds stops this
automatic deduction. The source theorem is imported by citation;
the necessary new work is accounting for the changed exclusion set.
The inspected stronger-result comparison does not cover that cost.

### Exact union cost and sufficient condition

Both A and S_I are finite. Partition their union into A and
S_I minus A to obtain the exact cost identity, counting every
overlap once. Write B0=(delta+2)s+2 delta s L for the upper
bound in (5). Then

    2(theta(A')+xi)<=2(B0+T+xi)<=U

whenever T<=U/2-B0-xi=M(H). Apply the finite-set theorem
with B=A'. The resulting prime is <=U and, since S1 is a
subset of A', is strictly greater than s>5. It is therefore
>=7. Its exclusion from S2 and S3 gives P2 and P3 at every
actual F-place. If it were in S, its interval membership would
put it in S_I, a contradiction. Thus v_ell(j(E))>=0 and L098's
extra premise would hold. This is a conditional application, not
an actual selection asserted by this lemma.

For every p contributing to T, n_p is a positive integer, so
log p<=n_p log p. The prime 3 belongs to S1 since s>5, and
contributes 30 log 3 to H but nothing to T. All remaining terms
of H are nonnegative. This proves (2). In particular the added
cost contains only interval-relevant poles outside A; (2) can
overestimate it by counting other poles, and must be interpreted
as an upper estimate only.

### Explicit deficit of this upper estimate

For s>=10^12 the function

    log(2 delta s^2)/s

has derivative (2-log(2 delta s^2))/s^2<0. At s=10^12,
log(6635520*10^24)<72. Hence, for all these s,

    3 delta L/s <=3*3317760*72/10^12
                 =716636160/10^12 <1/1000.

For the logarithm bound, e>sum_(k=0)^5 1/k!=163/60 gives
e^3>20. Thus e^72>20^24=16777216*10^24>6635520*10^24.
Consequently M(H)<3 delta s L<H/1000. Also
30 log 3<60<H/1000 for H>=10^24, so H-30 log 3>999H/1000.
Subtracting proves (3). The upper estimate for the finite-set
benchmark overshoots U by exactly 2D(H); the actual benchmark
need not overshoot at all. No actual T lower bound is inferred.

The exact rational constant checks can be reproduced with
`python3 scripts/pole-budget/check_step475_arithmetic.py`; their full
certificate is `scripts/pole-budget/step475-arithmetic-certificate.json`.
They support these arithmetic comparisons, not an actual pole-cost claim.

L089 supplies infinitely many distinct rational j in (0,1728).
For any fixed H_max, writing j=a/b in lowest terms gives
b<=exp(H_max) when H<=H_max, and 0<a<1728b. There are only
finitely many such integer pairs. Thus H is unbounded on the
actual family. This does not show every member has large H,
or exclude a useful member in a bounded window. It shows that
the existing existential, finite-exception selection cannot be
replaced by a uniform upper-height assertion from these inputs.
In particular finitely many low-height parameters can be included
in the prescribed exceptions, as in L101.

### Interval saturation in a numerical relaxation

This separate example checks that an interval cutoff alone does
not cure the numerical insufficiency. It is not a construction
of a curve or of its literal torsion fields.

Fix delta and xi as above, and choose a real X sufficiently large
that X>max(10,2xi) and, on setting

    V=20 delta X log(4 delta X^2),

one has V>=xi and

    30 log 3+(4/3)V < X^2/2.

Such X exist because log(X)/X tends to zero. Let P be the finite
set of all primes in (X/2,V], and W=sum_(p in P) log p.
By (5), W<=theta(V)<=(4/3)V. Neither 3 nor 5 lies in P.
Define the nonnegative integer

    N=floor((X^2-30 log 3-W)/log 5)

and set n_3=30, n_5=N, n_p=1 for p in P, and all other
n_p=0. The chosen inequality makes N positive. With h_p=n_p
at the finite places of Q, the degree bound 1<=delta and
integer-height conditions of the numerical selection argument
hold, and

    H=30 log 3+N log 5+W,
    X^2-log 5 < H <= X^2.

In particular s>X/2>xi, and monotonicity of sqrt(H) and
log(2 delta H) gives

    U<=10 delta X log(2 delta X^2)<V.

Every prime <=s lies in S1. Every prime in (s,U] lies in
(X/2,V], hence in P and in S_I. Therefore A' contains all
primes <=U, regardless of any additional S2/S3 overlaps or
primes outside the interval. Since U>=xi, (5) gives
theta(A')>=theta(U)>=(2/3)U, proving (4). Indeed in this
relaxation no prime in the interval avoids S.

The number j=1/(3^30*5^N*product_(p in P)p) is rational,
has n_3=30, n_2=0 and lies in (0,1728), so the height identity
is genuine for this rational number. This example does not meet
the fixed-family invariant formula, prescribed field, geometric
or Galois-image requirements. Its purpose is only to separate a
failure of the interval benchmark in the scalar numerical model
from a supposed actual-family counterexample. Additional
arithmetic information could still make T small on actual survivors.

## Mathlib

Matching coverage for the full interval-budget statement, numerical
relaxation and supporting finite-set prime bound has not been checked.
No absence claim or Lean verification is made. The prime theorem is
imported by the precise source citation above; the cost identities,
inequalities and their qualifications are proved here informally.
