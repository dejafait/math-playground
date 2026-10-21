# L081 — Redistributed-H t=0 root fails its own-input H guard

## Hypotheses

Use L055's indexed 25-row pair table, replacing only H_0=40 by 39
and H_24=32670621 by 32670622, as specified in L079. Keep literal
order and set a_i=2 for 0<=i<24 and a_24=166504412=2+18*9250245.
Use exactly the constraints of L051 (1)–(4), with natural logarithms.
No feasible junction tuple or integer/parity/valuation realization is
assumed. Only this allocation (t=0) is considered.

Write kappa=23/11 and define the exact rational quantities

\[
c_i=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i}},\qquad
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},
\]
\[
C_i=\prod_{j<i}c_j,\quad C_0=1,\qquad
R=\sum_{i=0}^{24}\frac{\eta_i}{C_i},\qquad
n_0=\frac{R}{2^N/3^K-1},
\]
\[
n_i=C_i\left(n_0+\sum_{j<i}\frac{\eta_j}{C_j}\right),
\quad s_i=n_i+\kappa,\quad h_i=\log s_i.
\tag{1}
\]
The denominator's positivity and the root's uniqueness are established
below, rather than assumed as feasibility premises.

## Conclusion

The unique cyclic endpoint root (1) violates the own-input strict
H guard at indexed row 18. Precisely, with J_18=693015 and H_18=3295208,

\[
h_{18}+J_{18}\log(27/16)-H_{18}\log2
< -\frac{457745289}{50000000000}<0,
\tag{2}
\]

where L051 (3) requires this margin to be strictly positive. Consequently
there is no full L051 (1)–(4) solution for these fixed ordered parameters.
One failed necessary constraint suffices; the other individual guards
are not classified here. This is local REPRODUCTION under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-t0-real-feasibility.md`,
not a new general theorem beyond the inspected affine/analytic machinery.
The separate critical audit below found no defect within this exact scope.

This verdict gives an earlier real-system obstruction for t=0 than
its already recorded arithmetic exclusion. It does not test t=1, other
allocations, orders or tables, and supplies no universal eventual descent.
Both original rational witnesses, the independent changed-table integer
and actual-word exclusions, and Attempts 026–031 remain valid.

## Proof

### Exact root and the unchanged total counts

The changed H entries cancel in the total, but not in any nonempty
proper prefix starting at row 0. Fresh summation gives

\[
\sum J_i=66061058,\quad\sum H_i=199390205,
\quad\sum a_i=166504460,
\]
\[
K=397573379,\quad L=232565518,\quad N=630138897.
\tag{3}
\]

All integer parameter bounds and tail congruences hold. The choice
d=1, K_0=K>225640000 and L_0=L>0 satisfies the explicit scaling
requirements, and direct rational comparison gives
N<(8/5)K+1725/1034. No primitive integer orbit is inferred from this
choice; these are solely the real system's numerical requirements.

The analytic certificate described below freshly encloses

\[
0<\lambda_-:=10584/10^{14}<
\Lambda=N\log2-K\log3<10585/10^{14}=: \lambda_+<1.
\tag{4}
\]

For each row, 0<eta_i<kappa: both bases in the subtractions lie
strictly between 0 and 1, so their sum is strictly below
12/11+1=kappa and is positive. Thus R>0. Also C_25=3^K/2^N,
so 2^N/3^K-1=exp(Lambda)-1>0. Formula (1) gives positive
rational coordinates, every recurrence n_(i+1)=c_i(n_i+eta_i),
and n_25=C_25(n_0+R)=n_0. On substituting s_i=n_i+kappa,
these are exactly all L051 (4) equations, including the closing tail.
Conversely any cyclic endpoint solution must satisfy
n_0=C_25(n_0+R), so the nonzero denominator makes (1) unique.

The formal affine fixed-point input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite nonempty formal word here has N letters and K odd letters;
(4) checks the nonzero denominator hypothesis. The displayed algebra
matches the local shifted coordinates. No general coding theorem is
reproved and no integer-realization converse is used. L078/L080's
arithmetic root is at this same normalized unshifted row-0 cut, but
neither arithmetic nonintegrality nor actual-word exclusion is a premise
of the present real-system argument.

### Fresh normalized upper bound at the changed root

All first 24 tails are 2. The changed first row has

\[
c_0=3^{63}/2^{73}>10^8.
\]

For 1<=i<24, positivity of alpha=log(27/16) and beta=log(3/2),
or simply the two bases greater than 1, gives

\[
c_i=(27/16)^{J_i}(3/2)^{H_i}/4
\ge (27/16)^2(3/2)^3/4=19683/8192>2.
\]

It follows that C_i>10^8*2^(i-1) for 1<=i<=24, while C_0=1.
Thus every C_i>=1 for 0<=i<=24 and

\[
0<R<\kappa\left(1+\frac{2}{10^8}\right)
=\frac{1150000023}{550000000}=:R_+.
\tag{5}
\]

The finite inverse-prefix sum is bounded by the geometric sum
sum_(j>=0)2^(-j)=2. Since exp(Lambda)-1>Lambda>lambda_-,
for every 0<=i<=24 the exact formula (1) implies

\[
\frac{s_i}{C_i}
=n_0+\sum_{j<i}\frac{\eta_j}{C_j}+\frac{\kappa}{C_i}
<\frac{R_+}{\lambda_-}+R_++\kappa
=\frac{435606069410390910013}{22050000000}
<20000000000<e^{24}.
\tag{6}
\]

The last comparison is certified by
20000000000<sum_(k=0)^40 24^k/k!<exp(24), with exact rational
terms. In particular h_i<24+log C_i for all these input indices.
This is a fresh upper bound for the changed table; no old root,
minimum, J margin or H margin was transferred. For positivity of the
logarithm arguments, n_i>0 was already proved. Establishing the
remaining domain, minimum or seed requirements is unnecessary to a
rejection by a failed H guard.

### The strictly failed necessary constraint

Summing the changed prefix rows 0,...,17 gives exactly

\[
C_{18}=3^{6078923}/2^{6862840}.
\tag{7}
\]

This includes H_0=39; the H_24 increase belongs to the closing
product, not this prefix. Combining (6), (7) with the own row-18
parameters gives

\[
\begin{aligned}
h_{18}+J_{18}\log(27/16)-H_{18}\log2
&<24+(6078923+3\cdot693015)\log3\\
&\qquad-(6862840+4\cdot693015+3295208)\log2\\
&=24+8157968\log3-12930108\log2.
\end{aligned}
\tag{8}
\]

Use the certified strict bounds
log3<1098612288669/10^12 and log2>693147180559/10^12.
The positive/negative coefficient signs in (8) therefore yield

\[
24+8157968\log3-12930108\log2
<\frac{24000000000000+8157968\cdot1098612288669
                -12930108\cdot693147180559}{10^{12}}
=-\frac{457745289}{50000000000}<0.
\]

This proves (2), with a strict negative separation. There is no boundary
or equality ambiguity. Since every endpoint solution is the unique root
already used, this rejects the fixed full system, without needing any
of its other guards to pass or fail.

### Analytic certification and scope

The prior assessment inspected [DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4)
and [4.5.1](https://dlmf.nist.gov/4.5.E1), version 1.2.8 (2026-09-15),
and L055/L065/L079's finite remainder methods. Reuse L079's unrounded
rational scheme: for x=2,3 put z=(x-1)/(x+1), m=100 and

\[
A(x)=2\sum_{k=0}^{99}\frac{z^{2k+1}}{2k+1},\quad
E(x)=\frac{2z^{201}}{201(1-z^2)},\quad U(x)=A(x)+E(x).
\]

Here 0<z<=1/2, and the positive omitted series terms give
A(x)<log x<U(x) by bounding all omitted denominators below by
201 and summing the geometric powers. This is the already assessed
remainder method. Use N A(2)-K U(3) and N U(2)-K A(3) for the
Lambda interval, retaining the amplified errors in both products.
Exact comparisons give (4) and the grid bounds used in (8).
No floating-point preview is used as evidence.

Reproduce with
`python3 scripts/postspell-word-count/certify_redistributed_h_t0_real_feasibility.py`.
Full exact operands, both 100-term logarithm sums/remainders, all
25 changed rows and incoming prefixes, the exp(24) partial sum,
root bounds and the row-18 guard certificate are retained in
`scripts/postspell-word-count/redistributed-h-t0-real-feasibility-certificate.json`.
All 150 certification checks pass. The rigorous mathematical failure is
the necessary H guard, distinct from a failed certification check.
The full selected root and failed-guard certificate fields were inspected.
This calculation is a reproduction specialization within the saved scope,
not an independent critical audit or a claim of originality. Published
integer-cycle computations are not applied to arbitrary real junctions.

### Separate critical audit — 2026-10-18

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-t0-failure-critical-audit.md`.
It independently checks the complete proof against L051 (1)–(4), L055's
indexed table and L079's two changed H entries. It finds no defect.
The general affine and analytic inputs are imported from the precise
Halbeisen–Hungerbuehler and DLMF references above; this is verification
of their finite specialization, not a reproof or an originality claim.

**Endpoint specialization and uniqueness.** With n_i=s_i-kappa, L051
(4) becomes n_(i+1)=2^(-a_i)[G_i(n_i+kappa)-(12/11)(3/2)^H_i-1].
Since c_i=2^(-a_i)G_i and
G_i eta_i=G_i kappa-(12/11)(3/2)^H_i-1, this is exactly
n_(i+1)=c_i(n_i+eta_i). Dividing by C_(i+1)=c_i C_i gives
n_(i+1)/C_(i+1)=n_i/C_i+eta_i/C_i. The finite sum therefore yields
(1) for every index through 25, without any parity or guard premise.
The independently recomputed total exponents are (K,N)=(397573379,
630138897), including a_24=166504412, so C_25=exp(-Lambda).
The certified positive Lambda makes 1-C_25 positive. Closure determines
the single root n_0=C_25 R/(1-C_25). Every eta_i is strictly positive
and below kappa, so R and every n_i are positive; logarithms are taken
only after this is established. This proves existence and uniqueness
of the endpoint root, not existence of a full-system solution.

**Complete incoming-prefix cap.** The changed row 0 gives
c_0=3^63/2^73>10^8 by exact integer comparison. For rows 1,...,23
the tails are exactly 2, and the parameter floors give
c_i>=19683/8192>2. Consequently C_0=1 and
C_i>10^8*2^(i-1) for every 1<=i<=24. This assertion does not
include C_25, which is below 1. All 25 terms of R are retained; the
last term uses C_24, while the closing multiplier remains in the root
denominator. Bounding their positive eta factors and the finite inverse
prefix sum gives exactly (5). For each input i<=24, the partial sum
in s_i/C_i is at most R and kappa/C_i<=kappa. The strict inequality
exp(Lambda)-1>Lambda>lambda_- then gives (6), without assuming
domain, minimum, seed, or any J/H guard. Independent rational arithmetic
reproduces its cap 435606069410390910013/22050000000<20*10^9.
Every term of the 41-term exponential partial sum is recomputed by
t_0=1, t_(k+1)=24 t_k/(k+1). Their sum exceeds 20*10^9; positivity
of the remaining exponential series proves the strict exp(24) bound.
Thus h_i<24+log C_i for all and only the needed incoming indices.

**Changed prefix and strict own-input sign.** Direct sums over rows
0,...,17 independently give exponents (6078923,6862840). Adding the
own row-18 contributions gives the positive log3 coefficient 8157968
and the negative log2 coefficient -12930108. The H_24 change is not
in this prefix, but is included in the total product already checked.
The H_0 change is included in both prefix exponents. The strict upper
substitution uses the upper log3 bound and lower log2 bound because
of these coefficient signs. Its exact result is
-457745289/50000000000, strictly below zero, whereas L051 (3)
requires the actual own-input margin to be strictly positive.
All endpoint solutions equal the root just bounded. One failed
necessary guard therefore excludes the full fixed system even if the
minimum, domain, seed or other guards were separately to fail.

**Independent finite verification.** The audit script
`scripts/postspell-word-count/audit_redistributed_h_t0_real_feasibility.py`
reads the original complete certificate but imports none of its generator
code. It reconstructs every changed row and all incoming prefixes from
the canonical L055 table, adding the closing product independently.
It recomputes all 200 saved logarithm terms, both remainders and every
exponential term, and reconstructs both operands, relation, difference
and pass flag of all 150 original checks. In addition, independent
120-term positive-series intervals strictly nest inside the saved
100-term intervals. Both Lambda and the expression in (8) use outward
substitution with full errors: respectively N E_2+K E_3 and
12930108 E_2+8157968 E_3, where E_x is the 120-term remainder bound.
No rounded interval or unchecked preview is evidence for these signs.

All 171 audit checks pass. Complete rational intervals, amplified
errors, comparison thresholds and check results are saved in
`scripts/postspell-word-count/redistributed-h-t0-real-feasibility-audit-certificate.json`.
The full root and failed-guard fields of the original certificate and
the full independent Lambda/upper-expression intervals were inspected;
all saved terms and check operands were compared exactly in the audit.
The failed mathematical guard is distinct from a failed certificate
check, of which there are none. The displayed algebra supplies the
root and endpoint justification that a script rerun alone would not.

**Scope and traps.** This validates the existing t=0 real exclusion;
it neither tests t=1 nor invokes L078, L080 or C080b as a premise.
No minimum-location, integer, seed, primitive-orbit or actual-word
realization assumption is used. Both original rational witnesses,
independent arithmetic/actual-word exclusions and Attempts 026–031
remain valid. The main argument and direct mathematical inputs are
unchanged, so PROOF.md and DAG.md are unchanged; this canonical audit
supersedes their pending-audit wording for L081. Universal eventual
descent remains unresolved.

## Mathlib

Full matching coverage of this particular finite changed-table exclusion
was not checked. Supporting affine, rational and analytic machinery may
be available; unknown availability is not evidence of absence. No Lean
build or formal verification is claimed.
