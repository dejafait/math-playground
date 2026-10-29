# L121 — Absolute conductor-389 5-adic point heights and strict determinant

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x, on the globally minimal equation
[0,1,1,-2,0], and let p=5. Put P=(0,0), Q=(1,0). Use Harvey's
quadratic height q_H and the ordinary cyclotomic conventions of L119,
including its audited MST replacement. Accept the published computational
arithmetic imported in L120; those original executions remain unreplayed.
For the characteristic-order and higher-layer conclusions use exactly
L119's classical Selmer/control conventions. No BSD, whole-Sha finiteness
or regulator nondegeneracy is assumed.

This is a fixed-input reproduction of known algorithms and arithmetic,
with complete finite witnesses below. The separate step-508 critical
audit passes at output exponent 6, with L120's original arithmetic
executions still unreplayed. It is not a general BSD candidate.

## Conclusion

With v_5(5)=1, the absolute height balls are

\[
\begin{aligned}
 q_H(P)&\in1000+5^6\mathbf Z_5,\\
 q_H(Q)&\in14355+5^6\mathbf Z_5,\\
 q_H(P+Q)&\in3275+5^6\mathbf Z_5,\qquad P+Q=(-2,-1).
\end{aligned}
\]

In the retained sign and half-polarization of L119, the representative
matrix, determinant and absolute determinant exponent are

\[
 \widehat H=\begin{pmatrix}-1000&6040\\6040&-14355\end{pmatrix},
 \quad D_0=-22126600,\quad B_0=6.
\]

Here a=0, N=6, k=2 and v_5(D_0)=2<6, so det H belongs to
D_0+5^6 Z_5 and is nonzero. Applying L119 with L120's b=2,t=0 gives
rank E(Q)=2, Sha(E/Q)[5^infinity]=0, nonzero full ordinary regulator,
h=2, delta=0, TM=0, M isomorphic to (A/(T))^2 and V_j=0 for j>=2.
These are local consequences of known inputs, not new arithmetic beyond
the sources checked. No comparison with arbitrary complex analytic order,
whole Sha finiteness, uniform producer, refined BSD or correction of the
printed Stein--Wuthrich sigma convention follows.

## Proof

### Imported algorithms and finite evidence

Use David Harvey, *Efficient computation of p-adic heights*,
[arXiv:0708.3404v1](https://arxiv.org/pdf/0708.3404v1), Theorems 1--3,
pp.1--2; Section 2.1 equation (2), Section 2.2 equation (3);
Section 3, pp.4--5; Section 4, Propositions 4--6 and equations (6)--(7),
pp.5--8; Section 5, pp.11--12, including Lemma 8. The standing
hypotheses are good ordinary p>=5, integral coefficients and the given
invariant differential. We use exact rational point multiplication,
not the large-p modular-coordinate shortcut of Proposition 9.
Import the integral sigma function, its defining normalized differential
equation and the height formula; do not reprove their arithmetic theory.

For the Frobenius input use Mazur--Stein--Tate, *Computation of p-Adic
Heights and Log Convergence*, Documenta Math., Extra Volume Coates (2006),
577--614, [Section 3.2, Algorithm 3.2, pp.590--591](https://ems.press/content/book-chapter-files/27479).
For the lift, reduction identities and denominator bound use Kedlaya,
*Counting Points on Hyperelliptic Curves using Monsky--Washnitzer
Cohomology*, [arXiv:math/0105031v2](https://arxiv.org/pdf/math/0105031v2),
Section 3, pp.3--5, especially Lemma 2, p.4, and Section 4, Steps 1--2,
pp.6--7. Only Lemma 2 is needed for the omitted negative-power tail;
the finitely many positive-power terms are reduced exactly. Its genus-one
hypotheses require an odd prime and squarefree cubic reduction.

The assessment predating this step is
`drafts/literature/2026-10-26-conductor389-five-adic-height-production.md`.
Reproduction is necessary to supply pointwise absolute certificates
matching L119, rather than import a displayed regulator. The following
are implementation-specific finite identities and precision accounting,
not a reproof of the imported algorithms.

Full evidence: `scripts/conductor389-height/step-506/certificate.json`.
It contains exact rational polynomial numerators, Q-adic decompositions,
every vertical and horizontal reduction, formal series, point-addition
chains, logarithm partial sums and final determinant. Full finite checking
is in `scripts/conductor389-height/step-506/verification.json`, with 5219
passing checks and no failures. Reproduction commands are

```bash
python3 scripts/conductor389-height/produce.py
python3 scripts/conductor389-height/check_certificate.py
```

The checker reads every finite witness. Its sparse-polynomial identities,
symbolic sigma uncertainty and modular logarithm calculation do not import
the producer. Counts and diagnostic trace/determinant agreement are not
substitutes for the bounds proved below. Integers 1000000000 in precision
fields denote exact rational data; no finite precision claim of that size
is made. A first run encountered Python's integer-to-string display guard
while serializing an exact logarithm fraction; allowing serialization of
these fixed exact integers completed production without changing precision
or arithmetic parameters. This was not a mathematical failed certificate.

### Eligibility and model transport

L030 supplies Delta=389, c_4=112, c_6=-856 and global minimality. L120
supplies good ordinary reduction at 5, #E(F_5)=9 and a_5=-3. At the only
bad prime 389, v(Delta)=1 and c_4 is a unit. The multiplicative exit of
Tate's algorithm, already cited in L030, has type I_1; its geometric
component group has order one, so the rational component group and the
Tamagawa number are one. Thus n_2=1, n=lcm(9,1)=9 and v_5(n)=0.
All rational points already have the bad-prime identity-component
condition. Exact rational arithmetic gives P+Q=(-2,-1). All three points
and their multiples [9]R are nonzero and on the curve, as the full chains
verify. No sigma evaluation occurs at the identity.

For [9]R=(alpha/d^2,beta/d^3), with d>0 and both fractions reduced, the
exact data are:

| R | alpha | beta | d |
|---|---:|---:|---:|
| P | 33046084324 | -55777095075809107 | 496035 |
| Q | 47905643486138021 | -12083247015143325974529269 | 124991065 |
| P+Q | -57353920736485559036133114886474 | -2867676652929653665722531257867839120115008484176 | 12278804002050455 |

In every row v_5(d)=1 and alpha,beta are units, so
t=-d alpha/beta=-x/y has valuation one. The checker also verifies the
nonsingular bad-prime reduction directly (or the smooth identity if a
denominator is divisible by 389). The source height formula applies.

Use X=x+1/3, Y=y+1/2, giving the short model

\[
 Y^2=\mathcal Q(X)=X^3-\tfrac73X+\tfrac{107}{108}.
\]

The transformation is defined over Z_5, with dX/(2Y)=dx/(2y+1), so the
invariant differential is preserved. The short discriminant is 389/16,
a 5-adic unit; hence the cubic is squarefree modulo 5. The computed
ordered basis dX/Y, X dX/Y is exactly that used in MST Algorithm 3.2.
Both basis vectors are twice their invariant-differential versions;
this common basis scalar does not change the Frobenius matrix. We apply
the algorithm's stated output convention for the preserved invariant
differential; no E_2 scale factor is inferred from that basis scalar.

### Frobenius truncation with an absolute tail bound

Put Delta_Q=Qcal(X^5)-Qcal(X)^5. Its coefficients have valuation at
least one and its degree is 13. For i=0,1 the imported lift gives

\[
 F^*(X^i dX/Y)=
 \sum_{j\ge0}5\binom{-1/2}{j}
 X^{5(i+1)-1}\Delta_Q^j\,dX/Y^{10j+5}.
\]

The binomial coefficient equals (-1)^j binom(2j,j)/4^j and is 5-integral.
Expand each numerator in powers of the monic cubic Qcal. This introduces
no 5-adic denominators, and each remainder polynomial has degree at most
2. A Qcal^s piece is A(X)dX/Y^(2m+1), m=5j+2-s. For j>=1 the numerator
degree is at most 13j+9, so s<=floor((13j+9)/3)<=5j+2 and m>=0.
Every such A has coefficient valuation at least j+1. Lemma 2 therefore
puts its reduced coefficient valuations at least

\[
 b(j)=j+1-\lfloor\log_5(10j+5)\rfloor.
\]

For j>=8, b(8)=7, and the floor-logarithm increases by at most one when
j increases by one, since (10j+15)/(10j+5)<5. Thus b(j)>=7 throughout
the omitted tail; also b(j) tends to infinity. The reduced tail converges
and belongs entrywise to 5^7 Z_5. This is a bound for *every* omitted
term, not a numerical scan. The finite j=0,...,7 terms, including the
possible m<0 piece at j=0, are reduced over Q with no rounding.

For explicit verification, write A=C Qcal+B Qcal'. At m>=1 the exact
differential identity for B/Y^(2m-1) replaces A at m by
C+2B'/(2m-1) at m-1. The certificate saves A,B,C and the next polynomial
at every use. At m=0 reduce high degree using
d(X^rY)=(r X^(r-1)Qcal+X^r Qcal'/2)dX/Y. These saved identities are all
checked exactly, so no intermediate finite-ring division or hidden
precision loss occurs. These are the cited reduction rules with their
individual arithmetic substitutions checked.

The resulting left-acting matrix is

\[
 F\equiv\begin{pmatrix}10550&27387\\42310&67572\end{pmatrix}
       \pmod {5^7}.
\]

Its trace is -3 and determinant is 5 modulo 5^7; the first column is
divisible by 5. These are diagnostics only. Exact reduction witnesses
and the preceding tail bound, rather than trace/determinant alone,
certify the matrix. Taking the second column (B,D) of F^6 gives D a
unit. MST Algorithm 3.2 then yields

\[
 E_2(E,\omega)\equiv-12B/D\equiv10008\pmod {5^6}.
\]

Matrix multiplication is integral and preserves the available absolute
exponent; inversion of the unit D does likewise. Internal exponent 7
is working precision for this fixed output task, not a raised point-height
target. No unit-root direction is inferred from the characteristic
polynomial alone.

### Sigma coefficients and their absolute errors

Use the original model parameter t=-x/y, not the short-model parameter.
The integral formal solution w=-1/y satisfies
w=t^3+t^2w+w^2-2tw^2. Put u=w/t^3 and A=u^(-1), so x=t^(-2)A and
y=-t^(-3)A. Then

\[
 \omega(t)=\frac{2A-tA'}{2A-t^3}.
\]

The coefficient recurrences for these identities are integral and have
unit leading coefficients. Exact w through degree 11 and A through
degree 8 determine the displayed omega through degree 7; substituting
the saved series verifies these truncation orders exactly. Terms outside
these ranges cannot affect the coefficients below.

Write c=(4-E_2)/12, theta=sigma/t. Harvey Section 4 equation (7) gives

\[
 \theta'/\theta=h(t)=-1/t-\omega(t)\int(x(t)+c)\omega(t)dt.
\]

Here the integration has zero constant term and its extra constant
a_1/2 is zero. The t^(-1) term cancels, and there is no logarithmic
integration term. The oddness normalization gives theta(0)=1 and
sigma's t^2 coefficient zero. Compute theta_k recursively from
k theta_k=sum_(j=0)^(k-1) h_j theta_(k-1-j). Exact differentiation,
integration and division by each k<=5 are retained, including the
possible loss at k=5. No Brent-iteration parameter or asymptotic
complexity claim is used for this small exact recurrence.

The full coefficients of h_0,...,h_4 at the center E_2=10008 are
0, 2504/3, 3/2, 9983/9, 12535/6. To verify the uncertainty independently,
the checker sets E_2=10008+5^6 z with an arbitrary z in Z_5 and computes
these recurrences as exact polynomials in z. Nonconstant coefficients
of the sigma coefficients below all have valuation at least 6;
constant rows have no uncertainty. Thus the following conservative
profile, also produced by ordinary absolute-ball propagation, is valid:

| sigma degree | rational center | absolute exponent | required for I_7 |
|---:|---:|---:|---:|
| 1 | 1 | exact | 6 |
| 2 | 0 | exact | 5 |
| 3 | 1252/3 | 6 | 4 |
| 4 | 1/2 | exact | 3 |
| 5 | 3144991/36 | 6 | 2 |
| 6 | 1253/2 | 5 | 1 |

The symbolic polynomials are fully saved in verification.json under
`symbolic_sigma`; this covers every possible E_2 in its certified ball,
not just a differential-equation residual at the center. Imported sigma
integrality controls *all* coefficients from degree 7 onward. For our
valuation-one t, the omitted theta terms from degree 6 contribute in
5^6 Z_5. Every retained coefficient error multiplied by its theta power
t^(degree-1) also belongs to 5^6 Z_5. Consequently the computed theta(t)
is certified to absolute exponent 6 at each admissible [9]R.

### Unit logarithms, heights and application

With the exact reduced coordinates above,
sigma(t)/d=(-alpha/beta) theta(t). The factor is a 5-adic unit, and so
this unit is known to absolute exponent 6. Its representative residues
modulo 15625 are respectively 10557, 8759 and 7326.
For any chosen rational center U of one of these balls, let z=U^4-1.
Then v_5(z)>=1, and use the Iwasawa logarithm

\[
 \log_5 U=\tfrac14\sum_{k\ge1}(-1)^{k+1}z^k/k.
\]

Keep k=1,...,7 exactly. For k>=8 the omitted term valuation is at least
k-v_5(k)>=k-floor(log_5 k)>=7: the last bound holds at k=8 and is
nondecreasing, since the floor-logarithm rises by at most one per step.
The valuations tend to infinity, so in particular the tail lies in
5^6 Z_5. Perturbing a unit by 5^6 Z_5 changes its logarithm by 5^6 Z_5,
by Harvey Lemma 8 (or the convergent log(1+epsilon/U) series). Thus this
calculation includes uncertainty in U as well as logarithm truncation.

Harvey's retained normalization gives q_H(R)=2 log_5(U)/9^2. Since
2/81 is a 5-adic unit, division loses no absolute digits here, in
agreement with M'=6+2v_5(9)=6 in Theorem 3. Exact partial sums and an
independent modular summation give respectively 1000,14355,3275
modulo 5^6, establishing the asserted balls. No Sage sign convention
or printed SW sigma equation is used.

Now L119 equations (3)--(6) give the displayed matrix. All its entries
and their absolute errors are integral, so a=0, N=B_0=6. Its determinant
is -22126600=25*(-885064), and -885064 is not divisible by 5. Hence the
strict inequality is 2<6. In particular the entire determinant ball
excludes zero; this is stronger than a numerical center being nonzero.
L120 supplies the full Selmer threshold b=k+t=2 and t=0. All remaining
L119 hypotheses have been checked above, so its full local conclusion
applies, with its audited canonical-height normalization and no further
independence or integral saturation assumption on P,Q.

This supplies the fixed-curve producer, accepted by the separate
step-508 critical audit below. The general rational-rank/complex-order comparison is
untouched. Published conductor-389 regulator and Sha computations already
exist; their overlap is explicitly assessed, so this is not claimed as a
new BSD case. ATTEMPTS/032/034/057 remain valid evidence for their own
routes, and no prior failed inclusive-cap or source-provenance obligation
on the distinct analytic route is repaired by this computation.

### Separate critical audit, 2026-10-26 (step 508)

**Verdict: PASS at absolute output exponent 6.** This accepts the stated
fixed input to the already audited L119, not a new height theorem or BSD
case. The source scope was SPECIALIZE before this invocation. The audit
read both complete scripts and replayed every finite reduction, formal
series identity, point chain and modular logarithm using the sparse
checker, which does not import the producer. The additional audit runner
is `scripts/conductor389-height/audit_508.py`; its full certificate is
`scripts/conductor389-height/step-508/audit.json` and its finite replay
output is `scripts/conductor389-height/step-508/finite-replay.txt`.
Run the audit with

```bash
python3 scripts/conductor389-height/audit_508.py
```

All 5219 original checks and the supplemental checks pass, with no
failures. The supplemental checks anchor the exact coefficient vector,
p, output exponent, n1,n2,n, three point labels, completeness of the
16 Frobenius terms, saved matrix power, sigma profile, all exact saved
logarithm fractions and the final precision metadata. They also check
that each actual chord/tangent branch is defined and every horizontal
primitive is polynomial. The original certificate and verification
files have identical SHA-256 hashes before and after replay. Hashes of
both scripts and this audit runner are retained. This is finite evidence;
the following checks of infinite bounds are independent prose reasoning.

**Eligibility and transport.** The invariants and Tate specialization of
L030 give minimal discriminant 389 and type I_1 at the only bad prime.
Its component group is trivial, so n2=1; L120 gives n1=9 and ordinary
p=5. The exact nine-step chains remain affine and nonzero. Their reduced
denominators all have valuation one, with unit alpha and beta, so the
original t=-x/y has valuation one. The bad-prime nonsingularity checks
pass. The substitution X=x+1/3,Y=y+1/2 gives the stated short cubic
and preserves dx/(2y+1). Its polynomial discriminant is 389/16, a unit
at 5. MST Section 3.2, Algorithm 3.2, pp.590--591, explicitly uses the
monic short model with a4=-c4/48=-7/3 and a6=-c6/864=107/108, the basis
dX/Y,X dX/Y, left action and the second column of F^6. The code places
the two reduced images in columns in precisely that convention. Relative
to the invariant basis dX/(2Y),X dX/(2Y) both vectors are scaled by 2;
Frobenius fixes this scalar over Z_5, so the matrix is unchanged. No
rescaling of the returned E2 is introduced.

**Infinite Frobenius tail.** Kedlaya Lemma 2 (math/0105031v2, p.4)
applies after dividing each cubic-adic numerator by 5^(j+1): the quotient
is integral, has degree at most 2 and m=5j+2-s is nonnegative for j>=1.
Indeed s<=floor((13j+9)/3)<=5j+2. Also m<=5j+2, so its denominator loss
is at most floor(log_5(10j+5)). The monic cubic-adic divisions preserve
integrality. Thus every reduced j term has valuation at least b(j).
At j=8 this is 7. The ratio (10j+15)/(10j+5)<5 makes successive
floor-log increments at most one, so b(j) never decreases; its linear
term dominates the logarithm, so it tends to infinity. Each j has only
finitely many cubic-adic pieces; finite sums lose no digits. Hence the
reduced omitted series converges in the rank-two cohomology lattice and
lies in 5^7 times that lattice. This is the reduction of the imported
Kedlaya Frobenius expansion, not an extrapolation from finitely many
indices. The sole possible positive-power exception is in j=0 and was
checked exactly by the saved polynomial differential reductions. Lemma
3's omitted proof is unnecessary. Exact finite reductions followed by
this tail give F modulo 5^7; integral matrix powering preserves that
exponent. The saved sixth power has unit bottom-right entry. MST's
algorithm therefore certifies E2=10008 modulo 5^6 without inferring its
direction from trace/determinant diagnostics.

**Sigma normalization, uncertainty and tail.** Harvey equations (6)--(7),
p.7, give the retained negative sign and C=a1/2=0. Formal oddness is
sigma(i(t))=-sigma(t), and fixes the t^2 coefficient; it is not ordinary
parity in t. The w equation has a unique t^3-leading solution by its
coefficient recurrence. Its saved degrees 3 through 11 determine A
through degree 8 and omega through degree 7. In particular h through
degree 4 uses only A through degree 6 and omega through degree 5: the
leading exponent in the integrand is -2, and its primitive starts at
-1. Higher omitted coefficients cannot enter this computation. The
t^(-1) integrand coefficient vanishes, so there is no formal logarithm.
Solving k theta_k=sum h_j theta_(k-1-j) over Q[z] gives exactly the
saved symbolic polynomials with E2=10008+5^6 z. Every nonconstant
coefficient in these six theta coefficients has valuation at least 6;
the profile's exponent 5 in its final row is conservative. A sentinel
10^9 occurs here only when that polynomial is constant, as additionally
checked, so it introduces no spurious finite uncertainty. Division by
k=5 is included in the exact symbolic calculation. The actual imported
integral sigma supplies every omitted coefficient of sigma from degree
7 onward. Integrality of the entire series is asserted for the true E2,
not for all arbitrary z in its ball. Since v(t)=1, the omitted theta
tail has exponent at least 6; each retained coefficient error has
exponent at least (6-k)+k=6 on evaluation. The unit factor -alpha/beta
loses no precision. This establishes the full I_7 evaluation contract.

**Logarithms and final handoff.** For each exact rational unit center,
the audit verifies z=U^4-1 and the entire seven-term saved partial sum,
not just its displayed residue. Since v(z)>=1, k>=8 gives
v(z^k/k)>=k-floor(log_5 k)>=7; this bound is nondecreasing and tends to
infinity. The convergent logarithm tail is therefore in 5^7 Z_5, and
division by 4 loses no digits. For epsilon in 5^6 Z_5, every term of
log(1+epsilon/U) has valuation at least 6, so perturbing U preserves
the required absolute exponent. The unit multiplier 2/81 likewise
loses none. The resulting residues are exactly 1000,14355,3275, each
with absolute exponent 6 after multiplication/division. All three
L119 equation (2) inputs are therefore met, including exact sum and
nonzero admissible multiples. Its equations (3)--(6) give the displayed
matrix, a=0, N=B0=6 and D0=25*(-885064), with valuation 2<6. Its
determinant ball excludes zero, rather than merely having a nonzero
center. L120's full Selmer b=2,t=0 meets b=k+t, and the already audited
L119 implication supplies exactly the local conclusions stated here.
No saturation, finite whole Sha or unproved nondegeneracy is added.

The published L120 arithmetic and the imported height/cohomology
theorems remain cited inputs, not original executions or proofs audited
here. ATTEMPTS/032/034/057 retain their original scope; the disputed SW
formula and separate analytic production failures remain unresolved.

## Mathlib

Full matching coverage for this exact curve's certified ordinary
5-adic point heights, sigma/Frobenius producer and the resulting
characteristic-order specialization: **not checked**. Supporting exact
elliptic-curve group law, rational polynomial and valuation results:
**not checked**. No absence claim is made. This is an informal known-method
calculation with finite rational witnesses and explicitly imported
arithmetic theorems; it is not a formal Mathlib proof.
