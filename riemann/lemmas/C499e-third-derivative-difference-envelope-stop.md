# C499e — Third-derivative and single-difference envelope stop

## Hypotheses

Retain exactly C499d's hypotheses, rational parameters, canonical cutoff,
full epsilon_1, inherited reserve r0 and analytic-source qualifications.
In particular t=.16836, X=6000284561421.5, n=691004, N=691260,
Y=4*pi*(N^2-t/16), and x ranges over the whole closed [X,Y].
The old n model is only a finite comparison; the true remainder freezes
its canonical q(x) at each centre, including entry equality.

Use the one global third-derivative enclosure below, Arias de Reyna's
Theorem 11 with d=3 and Theorem 7 with every integer H<=L, applying
his Lemma 5 and the absolute cap to each single difference. Retain
C499d's decreasing-weight Abel and full-resultant triangle interface.
This specifies one estimator, not every third-derivative method.

## Conclusion

For every integer prefix length 1<=L<=256, this optimized d=3 estimate
and every tested finite single-difference estimate give no improvement
over the absolute cap L. The resulting all-prefix cap is M=256.
Consequently the complete uniform sufficient envelope satisfies

    .00072254689054510978 < B_unif+U_s,unif+U_r,unif
                           < .00072254689054510979,
    r0 < .000422493815870544,
    (B_unif+U_s,unif+U_r,unif)-r0 > .00030005307467456650.

The prescribed strict budget fails at adequate precision. The one
calculation covered all 256 prefixes, 32640 nonempty shifted cases and
32896 (L,H) pairs within the cumulative 2^25 scalar-operation allowance.
Park this estimator. This is a negative result for an evaluated sufficient
bound, not a lower bound on an actual sum, increment or collision cost.
It neither contradicts C499c nor proves RH or an off-line zero.
The manuscript saddle/base-phase inputs remain unaudited. The independent
audit in Section 5 accepts the local specialization and complete saved
arithmetic, with a 48-charge output-accounting correction; the cap holds.

## Proof

### 1. One derivative range, including all shifted domains

C499d proves the closed analytic domain, all canonical floor cells and
the exact integer-phase identity for

    f_x(u)=-a_x*log(u)-u*(u-1)/2,
    n^2-dmax<a_x<(N+1)^2,  dmax>=7*t/(8*pi*X),
    0<dmax<10^(-12).

Here dmax is the outward upper rational endpoint of 7*t/(8*pi*X),
not a sampled value. The derivative formulas concern u, with x fixed.
For g_x=-f_x, direct differentiation gives

    g_x'''(u)=2*a_x/u^3,
    0<lambda=2*(n^2-dmax)/N^3
       <=g_x'''(u)<=Lambda=2*(N+1)^2/n^3,  n<=u<=N.

The certificate encloses lambda between
.000002891124788659806773214336 and
.000002891124788659806773214337, and Lambda between
.000002896492591979200986242150 and
.000002896492591979200986242151. The phases are real smooth functions
on a neighborhood of this positive u interval. Conjugating every term
of a prefix changes its sum to the complex conjugate and preserves its
modulus, so estimates for g_x apply to the original primitive phases.

For integers 1<=a<H<=L<=256 and u in (n,n+L-a], let
h_a(u)=g_x(u+a)-g_x(u). The fundamental theorem of calculus gives

    h_a''(u)=integral_0^a g_x'''(u+v) dv,
    a*lambda<=h_a''(u)<=a*Lambda.

Every argument satisfies n<u+v<=n+L<=N, including the upper endpoint;
the shifted length L-a is at least one. Thus there is no excluded
short/resonant/end case. H=1 has no shifts. Empty primitive prefixes
are zero. These bounds hold for every x in [X,Y], independently of
the floor; one may use the subset of prefixes ending at q(x). No
derivative of q is taken, and no spatial sample represents an interval.

### 2. Exact imported bounds and the finite screen

J. Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*,
[arXiv:2407.02094v1, 2 July 2024, Section 5, Theorem 11,
(15)–(16), PDF pp.10–13](https://arxiv.org/html/2407.02094v1#S5),
applies for integer d>=3, floor(L)>d and a real C^d phase with positive
lower/upper d-th derivatives. For d=3 its normalized bound is

    max{A3*(Lambda/(lambda*L))^(1/4),
        B3*(Lambda^2/lambda)^(1/6),
        C3*(lambda*L^3)^(-1/4)},
    A=2*(1+sqrt(1+3*pi/8))/sqrt(pi), B=2+2*sqrt(2),
    A3=B*sqrt(2),
    B3=B*((81/8)*(2/3)^6*4*A^2/B^2)^(1/6),
    C3=B*sqrt(8*A/B).

These are exact formulas, not rounded table constants. Apply only at
L=4,...,256; smaller lengths retain their absolute bounds. Already
the first term is at least A3/4>1, because Lambda>=lambda and
L<=256, whereas A3=4+2*sqrt(2)>4. Thus the optimized bound cannot
improve any of these absolute caps. All three terms are still recorded
and evaluated; none is dropped from the maximum.

[Theorem 7, (8), Section 4, PDF pp.7–8](https://arxiv.org/html/2407.02094v1#S4)
gives, for natural H<=L, with e(v)=exp(2*pi*i*v),

    |L^(-1)*sum_(n<j<=n+L)e(g_x(j))|
       <=B*max{H^(-1/2), B^(-1/2)*T1^(1/2)},
    T1=(L*H)^(-1)*sum_(a=1)^(H-1)
                       |sum_(n<j<=n+L-a)e(h_a(j))|.

There is no first-derivative nonresonance premise. [Section 2, Lemma 5,
PDF p.4](https://arxiv.org/html/2407.02094v1#S2) and Section 1 give
the valid shifted-sum upper cap

    V_(L,a)=min{L-a, A*(a*Lambda*(L-a)+2)/sqrt(a*lambda)}.

Every one of the 32640 rows has the second expression strictly greater
than L-a, with its outward lower endpoint above L-a. The full exact
operands, global shift constants and selected caps are stored in the
certificate. Hence each V_(L,a)=L-a. In particular the evaluated upper
formula for T1 is exactly

    T1_cap=(H-1)/H * (1-H/(2*L)).

This describes the bound used, not the actual correlation size. For H=1
the first branch is B>1. For H>=2, H<=L implies T1_cap>=1/4 and
B*T1_cap>=B/4>1. Squaring the nonnegative normalized bound gives
max{B^2/H,B*T1_cap}, so it exceeds one in every case. The certificate
evaluates all 32896 cases as well; its smallest raw normalized bound
occurs at L=H=11 and lies in (1.48146535638109,1.48146535638110).
Taking minima over H, the optimized bound and the absolute cap still
gives L for each prefix, hence M=256. No improvement of the author's
inequality or of its constants is asserted or rederived.

### 3. Abel weights, full resultant and both charges

C499d Sections 3–4 prove, uniformly in x, that the actual heat weight
w_x(u) and log(u)*w_x(u) are positive decreasing on [n+1,N]. They
decrease in x, since sigma(x)>=sigma(X). The certificate also checks
sigma(X)-t*log(N)/2>0 and
log(n+1)*(sigma(X)-t*log(N)/2)>1. Write h=log(n+1) and
w_first=exp(t*h^2/4-sigma(X)*h). Finite Abel summation, retaining
its endpoint, gives S_cap=M*w_first, L_cap=M*h*w_first.

C499d's exact finite reconstruction at the actual phases is

    DeltaZ=rho*exp(i*Theta)*DeltaS,
    DeltaW=rho*exp(i*Theta)*(DeltaL-J*DeltaS),
    DeltaG=DeltaZ-DeltaW/ell+conj(DeltaW)/ell.

All squarefree channels, products of prime heat weights, logarithmic
terms, coincident outputs and conjugate terms remain in that identity.
Using only its proved positive envelopes R0,J0,D0 and ell>ell0 gives

    B_unif=R0*(S_cap+2*(L_cap+J0*S_cap)/ell0).

Independently use absolute primitive mass 53/3+256*w_first, not a
cancellation cap, for the full logarithmic support. Put

    Hlog=log(N)+sum_(p<=307)log(p),
    K=R0*(53/3+256*w_first)*Hlog,
    QX=X*(X^2+5)/(1+X^2)^2, CX=(7*X^2-5)/(1+X^2)^2,
    U_s,unif=t*(QX+CX)*K/ell0,
    U_r,unif=R0*epsilon/2+2*(D0*epsilon+R0*epsilon_1)/ell0.

These are C499d's already justified whole-interval envelopes: both
saddle corrections, product derivative and full frozen-index entering-
pair/Cauchy allowance remain charged. The old coefficient mass damps
in x and gives the inherited lower bound r0 without a fall credit.
The evaluated bounds are

    .00070171640076552016 < B_unif < .00070171640076552017,
    U_s,unif < 1.254886146337842e-11,
    U_r,unif < .000020830477230729.

Their sum and strict excess over r0 have the enclosures in the
conclusion. A small upper bound for a primitive sum would not itself
have paid this budget; here not even the prefix caps improved.

### 4. Certificate, resource bound and verification limits

Reproduce from the notebook with

    python3 scripts/heat/third-derivative-entry-budget.py

The complete certificate is `scripts/heat/third-derivative-entry-budget.json`.
This is the reproduction command, not authorization to repeat the capped
search. The invocation executed it once, with no precision refinement.
It imports only definitions before `def run()` in the retained endpoint
producer, checks its hash against C499c's audit, and checks every retained
input hash in C499d's certificate. It does not execute earlier producers.

The 10^(-60) outward rational arithmetic, logarithm/exponential series
and square-root enclosures are those justified in C499c and reused by
C499d. New fourth/sixth roots use the following exact method: for a
nonnegative rational endpoint v and G=10^60, integer bisection finds
r=floor((floor(v*G^k))^(1/k)). Then r/G<=v^(1/k)<(r+1)/G.
Monotonicity permits lower and upper endpoint evaluation. Bisection
starts below and strictly above the integer root and preserves that
bracket; all powers and comparisons are exact. All coefficients in
the theorem formulas are positive, so interval minima/maxima and these
roots enclose the exact candidate bounds. Reused transcendental tails
and every root-dependent candidate endpoint are retained.

The completed operation ledger is 31768440<=33554432. It uses explicit
conservative scalar rational/endpoint charges, not CPU time: fixed
formula work is charged 4096; interval add/negate/subtract/multiply/
divide are charged 32/8/8/48/32, with nested calls counted again;
square roots 64, k-th-root bisection iterations 16*k, and separate
root setup, comparisons, minima/maxima, log and exp overheads are
charged as recorded. These charges also cover the small exact caller
operand formulas: in particular a*Lambda*(L-a)+2 in a shifted
multiplication, and the integer L*H in a division. Their at most eight
extra scalar operations fit the conservative method allowance.
Integer bit complexity, file serialization and hashes are not counted
as enclosure operations. The report includes the final subtraction
in its total count. This is accounting under that stated convention,
not an optimal complexity claim or an independent resource audit.

All 21 implementation/domain/coverage/width comparisons pass; the
mathematical budget is explicitly ENVELOPE_FAIL. Total enclosure
width is below 10^(-30). Complete selected domain, constants, final
prefix, checks, envelopes and operation fields were inspected with
the scoped JSON inspector; previews alone are not used as proof.
Exhaustive row generation and the displayed formulas supply the finite
calculation, not an independent certificate audit. No original bound
beyond the inspected source method is claimed. Other estimators,
later intervals/times, H1, zero time and all-height signs remain open.

### 5. Independent saved-evidence audit, 1 November 2026

The prior SPECIALIZE assessment
`drafts/literature/2026-11-01-c499e-independent-audit-scope.md`
covers this audit. No producer was imported or executed, and no H range,
precision, spatial partition or cap was enlarged. This is verification
of a known-method specialization and its estimator-specific negative,
not new cancellation mathematics or an RH conclusion.

**Analytic specialization.** Differentiating g_x=a_x*log(u)+u*(u-1)/2
gives g_x'''=2*a_x/u^3. C499d's exact alpha identity, positive delta
and closed floor cells imply n^2-dmax<a_x<(N+1)^2 uniformly; n>0
gives precisely the displayed positive lambda,Lambda, including u=N.
Conjugation preserves the primitive modulus at every integer. For
1<=a<H<=L, all u+v in the integral for h_a'' belong to (n,n+L],
and L-a>=1, so Lemma 5's real C^2, length and derivative hypotheses
hold on every shortened interval. Theorem 11 is invoked only for
integer L>=4, with its d=3 constants exactly as in (15)–(16).
Lengths 1–3 use absolute bounds; H=1 has no correlations. Theorem 7's
normalization is unchanged. With the verified absolute shift caps,
sum_(a=1)^(H-1)(L-a)=(H-1)*L-H*(H-1)/2, giving the stated T1.
For H>=2 the two factors in T1 are at least 1/2, whereas B/4>1.
For H=1 the first branch is B>1. Thus no signed-correlation,
resonance or short-length case was omitted. A3/4>1 independently
checks the optimized-bound stop.

**Weights, full support and qualifications.** The checked positive
margin sigma(X)-t*log(N)/2 and its product with log(n+1)>1 prove
both weight derivatives negative. Finite Abel summation retains the
terminal term: for a decreasing v_j>0 and partial sums |A_j|<=M,
|A_k*v_k+sum_(j<k)A_j*(v_j-v_(j+1))|<=M*v_first.
Monotonic sigma makes the X weights uniform. C499c's finite product
identity applies at each centre with its actual phase and canonical
q(x); differentiating E in nu gives +E*J and hence Elog=-E*J.
No output or coincident channel is removed. Absolute primitive mass
53/3+256*w_first, rather than a cancellation estimate, pays the full
logarithmic support. Decreasing prime radii, the positive denominators
1-r_p, and decreasing positive Q,C justify all anchor replacements.
The full epsilon_1 is used at each separately frozen canonical index,
including every equality. Old |beta_m|m^(-sigma) decreases even for
negative coefficients and m>n; the unit constant term and
|1-u|+u=max(1,2u-1) give the same r0 without any fall credit.
These checks reuse L494–L496/L499's exact qualified inputs, not the
unverified manuscript proofs or a derivative of the floor. The
symbolic equality Y/(4*pi)+t/16=N^2 fixes the final floor exactly;
interval rounding does not decide that equality.

**Independent arithmetic.** Reproduce only the consumer with

    python3 scripts/heat/c499e-certificate-audit.py

Its separate complete evidence is
`scripts/heat/c499e-certificate-audit.json`. Independent rational
endpoint arithmetic reconstructs every field of all 255 shift-parameter
rows, 32640 shift rows, 32896 difference rows and 256 prefix rows,
including ordering/coverage, all maxima/minima, best choices and
outward endpoints. Every root has its complete operand and enclosure
saved: 33664 root enclosures in all. Square roots use integer isqrt;
fourth/sixth roots use an independent integer Newton iteration.
For each endpoint v the consumer checks r^k<=floor(v*G^k)<(r+1)^k
and (r/G)^k<=v<((r+1)/G)^k, G=10^60. This verifies the
rounding and scaling, not merely agreement of rounded decimals.
The five complete log/exp records, including all series sums, last
terms and geometric tails, are reconstructed using Section 4's
identities and domain restrictions. Every stored check field, all
quoted numeric endpoints, input hashes, exact parameters/reserve,
and the complete reconstructed envelope agree. The already audited
corner inputs and their linkage are reused; expensive earlier
producers and their source proofs are not rerun. The consumer's
initial interval-versus-range-dictionary schema mismatch was corrected
by exact canonical encoding comparison; it revealed no producer
arithmetic discrepancy.

**Resource qualification.** The independently reconstructed method
charges and binary-search control-path lengths reproduce all recorded
categories, summing to 31768440 through certificate assembly, including
the saved final excess. The producer then recomputes total-r0 in its
print-list construction after serialization. This additional subtraction
charges 8 directly, 8 for its nested negation and 32 for its nested
addition: 48 more. The whole enclosure execution therefore has the
corrected upper charge 31768488<33554432, leaving 1785944 charges.
The earlier statement of 31768440 as the *completed* execution total
is narrowed to certificate assembly. The original pre-assembly cap
predicate also precedes these final subtractions; the audited complete
total, not that predicate alone, certifies the cap. No producer file or
saved producer evidence was changed.

The convention counts rational endpoint operations, comparisons and
integer-root work, with rational normalization and integer powers
treated at that scalar level; it does not claim bit complexity.
For add/multiply/divide, their 32/48/32 charges cover endpoint rational
work, rounding, ordering comparisons and small exact caller operands;
division additionally charges its nested multiplication. In particular
multiplication uses four endpoint products, six extrema comparisons,
two roundings and ordering, leaving room for at most eight scalar
caller operations; division's sign test, two reciprocals, rounding and
ordering leave the same slack. Setup/loop work is paid by the fixed,
shift and third-derivative allowances; log reductions and series tail
formulas by their overheads. Root setup is at most 64*k and each
binary iteration at most 16*k for k=4,6, including exact powers and
comparisons. Min/max costs 8 per argument cover both endpoint choices.
Serialization, hashes and decimal formatting are outside this enclosure
convention; the extra interval subtraction is included. There was no
precision refinement. The audit consumer's own cost is not charged
to the historical calculation.

All independent checks pass after that qualification. In particular
the total remains strictly above r0 by >.00030005307467456650 with
width <10^(-30). This accepts only the recorded sufficient-envelope
failure. It does not lower-bound any true correlation, primitive sum,
resultant increment or collision cost. The earlier quadratic/spatial
stops and the manuscript, later-cell/time, H1, zero-time and all-height
gaps remain as qualified before. No mathematical input or DAG edge
changes in this audit.

## Mathlib

Full matching coverage is unchecked and unknown. Supporting mathematics
is elementary differentiation, conjugation, the fundamental theorem of
calculus, finite sums, monotone roots and finite Abel summation. No
matching Mathlib theorem for this effective derivative estimate,
heat/resultant application or complete rational certificate is claimed.
Unknown availability is not absence.
