# Full logarithmic gcd form at the critical coefficient — source comparison

TARGET: Assess whether L737's full logarithmic gcd form satisfies F_(2 log N)(c)>=-C Q(c) for one absolute C>=0, all integers N>=2 and all complex c, identifying a matching theorem or one bounded spectral discriminator.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step225 searched exact logarithmic gcd quadratic forms, logarithmic derivatives, weighted gcd spectra and log-type GCD sums; narrow local searches found L737 and its November4 assessment but no duplicate resolution. Primary statements and relevant proofs were compared below; no novelty inference follows from the search.
SOURCE_EVIDENCE: Reuse the November4 BCR/Lindqvist-Seip/Altinisik-Buyukkose assessment unchanged; newly inspected bramble_trace paper41v3 Section5 eqs(19)-(27a), Lemmas4/5/5a and complete proofs; Yang arXiv:2201.12968v3 Theorems1.1/1.2 p1 and Sections4.2-4.3 p9, plus Mathematika68(2022) Proposition2 p488; Bindel CS6210 2025-11-03, Hermitian/generalized Rayleigh sections and Cholesky reduction.
COMPARISON: No inspected result supplies the absolute additive lower bound for the signed linear-log form at A=2 log N. Positive-shift relative estimates, N^epsilon global/inverse losses, and log-type extrema at different exponents do not settle that endpoint. Standard Hermitian variational theory does cover a bounded diagnostic of the exact finite form.
GAP: The universal C and any unbounded negative sequence remain unproved. No eigenvalue or trial quotient was computed. Only the finite diagnostic in COVERED_TARGET is ready for separate approval; numerical trends cannot resolve the universal claim.
REASON: Essential comparison is now complete for one finite diagnostic, using L737's existing identities and a named spectral theorem. A new arithmetic inequality needs a later mathematical attempt; reproving known moment or gcd factorization results is unnecessary.
SCOPE: Exact TARGET and the single COVERED_TARGET below, retaining N>=2, all complex c, natural logarithms, full gcd/log terms and Q normalization. No theta contact calculation, longer-dictionary projection result, new moment theorem, zero-free assertion, or actual-Xi sign. This is bounded source coverage, not a claim to exhaust the literature.
COVERED_TARGET: Run one bounded spectral discriminator for L737's inequality F_(2 log N)(c)>=-C Q(c), using N=2^j for 1<=j<=9 and interval-certified rational trial quotients, to decide whether an explicit scalable negative family is justified for further study.

## Invocation-start nomination (preserved)

The following nomination described the state before step225. Its
REVIEW_REQUIRED statements are historical; the completed comparison
below replaces that source-readiness decision, without supplying a
mathematical result.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This is an intermediate arithmetic-norm question. A sharper coefficient-
uniform coercivity threshold could determine whether arithmetic multipliers
can support microscopic observer realization beyond L737's short range.
It supplies no realization or sign by itself. Source moment errors,
coefficient conditioning, localized numerators, signed observer transfer
and all-degree signs remain independent gaps. Do not infer that replacing
4 by 2 in one main-term estimate resolves any of them.

The finite quantities are exactly L737's (5)--(6), with natural logarithms:

    F_A(c)=sum_(m,n<=N) c_m conjugate(c_n) gcd(m,n)/sqrt(m*n)
                 *[A+2 log gcd(m,n)-log m-log n],
    B_d=sum_(k<=N/d) c_(dk)/sqrt(dk),
    Q(c)=sum_(d<=N) phi(d)|B_d|^2.

Here phi is Euler's totient and c is any complex N-vector. These are
existing definitions, not a new reduction. The source review should
test the universal constant statement in TARGET, including c=0 and
every N, and distinguish it from asymptotics for a fixed vector or
an unweighted gcd spectrum. The proposed coefficient 2 is a target,
not a proved or conjecturally optimal threshold. No finite eigenvalue
has been computed in this nomination.

Exactly three mechanisms were compared for continuation after step224:

1. L923's fixed density floor: the audited interface is retained, but
   actual D<=epsilon is unpaid. Reuse the step222 ATTEMPTS record;
   there is no new actual-theta input justifying reopening it.
2. L727's local signed margin: its tail-only stop and the November6
   local-pair source stop separate a pointwise center-dependent margin
   from complete-pair averages. The earlier signed-real-zero allocation
   assessment already covers the one-pair/two-neighbor model. No new
   center-sensitive arithmetic premise was found, so do not repeat that
   model or its source campaign.
3. The full logarithmic gcd spectral threshold: selected. It retains
   signed divisor correlations and changes to an independently defined
   arithmetic main-term norm. L737's proof uses a coarse absolute Schur
   estimate; its cited spectral comparisons explicitly leave the full
   logarithmic form uncovered. This is the precise new quantity to
   assess, not evidence that it is new in the literature or true.

Before mathematics, search the exact quadratic-form inequality, stronger
weighted gcd spectral estimates and logarithmic derivatives of gcd
matrices; retrieve the relevant primary theorem hypotheses and proof
cases. Reuse the named twisted-moment assessment only within its actual
scope. It does not authorize a new length exponent or a sharp spectral
claim. Essential prospective local input is L737's finite form;
L637 defines the intended observer application and is not an assumed
signed-realization theorem. No cross-notebook input is proposed.

Continue if a matching theorem can be imported with its precise
normalization, or if sources leave a concrete finite spectral test whose
decisive quantity is F_(2 log N)(c)/Q(c). A theorem disproving a uniform
lower bound, or an independently justified family on which that ratio
tends to minus infinity, abandons this proposed threshold. A few finite
values cannot establish or refute the existence of some absolute C.
If no source-covered discriminator can be specified, park this target
without deriving and approving uncovered mathematics in one turn.

This is not ready coverage. Newly accessed essential sources belong to
the next literature step. No general theorem is reproved, no mathematical
attempt on this form is made, and no exploration budget is reset here.
Full matching Mathlib coverage is unchecked. No creative mathematical
invocation is nominated before this exact source comparison is complete.

## Completed source review — 9 November 2026, step225

### Scope, local comparison and search record

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is precisely the absolute-C bound
in TARGET. A sharper arithmetic norm could inform which multiplier
lengths deserve study for microscopic observer realization. Even a
positive answer would leave coefficient conditioning, charged moment
remainders, localized numerators, realization and signed transfer unpaid.

Read L737 in full, including its separate audit: equations (5)-(7)
define the full form and divisor coordinates, (8)-(10) give the coarse
Schur bound, and (11) retains the coefficient-conditioning loss. Reuse
the complete November4 source assessment above. L637's observer scope
is comparison context, not an imported realization theorem. A narrow
search of local assessments and ATTEMPTS for logarithmic gcd,
critical coercivity and divisor spectra found no duplicate threshold
result. The short-dictionary exclusion and step222 fixed-floor stop
remain in force within their hypotheses; neither decides this target.
No sibling notebook was read.

Queries included `"gcd matrix" "logarithmic" eigenvalues`,
`"gcd sums" "log" "derivative" quadratic form`,
`"logarithmic" "greatest common divisor" quadratic form`,
`"gcd sums" "logarithmic weights"`,
`"logarithmically weighted" "GCD" sums`,
`"logarithmic derivative" "gcd" matrices`,
`"log-type GCD sums" arbitrary coefficients`,
`"gcd" "2 log N" "form"`,
`"gcd" "log(mn" "matrix"`, and
`"Selberg" "quadratic form" "log" "gcd" lower bound`.
Searches also compared endpoint/smallest-eigenvalue terminology.
Generic logarithmic heights and the kernel log gcd are different
objects. Searches locate leads; only the primary passages identified
below are evidence for the comparison. Failure to locate a match is
not a priority or originality claim.

### Shifted gcd-form comparison

Primary source: bramble_trace, *Generalized Laguerre positivity at
growing orders*, paper41 **v3**, 23 October 2026,
[Section5](https://rstation.ai/problems/riemann_hypothesis/papers/41/v3).
Read definitions (5), (19)-(22) and complete proofs of Lemmas4,5,5a,
equations (23)-(27a). This is an unreviewed manuscript comparison;
none of its new estimates is imported as an established input here.

Its G_y(h,k)=exp(-(1/2+y)D(h,k)), D=log(hk/gcd(h,k)^2),
has the same unweighted endpoint kernel as Q. Lemma4's relative
derivative bound requires Re y>=delta for a fixed 0<delta<1;
the constant depends on delta. Lemma5 includes real c=0 but is an
inverse estimate with N^epsilon loss. Lemma5a controls the full form
globally with exponent max(0,-2 Re y)+epsilon. Read both real-part
cases in that proof and the comparison using Lemma5. These are not
an absolute additive derivative bound at zero. Shrinking delta,
differentiating a big-O estimate, or replacing N^epsilon by O(1)
is unjustified. This source does not settle TARGET.

### Log-type gcd sums comparison

D. Yang, *A note on log-type GCD sums and derivatives of the Riemann
zeta function*, [arXiv:2201.12968v3](https://arxiv.org/pdf/2201.12968v3),
5 July 2023. Read Theorems1.1/1.2 on printed p1, definitions there,
and complete proofs in Sections4.2-4.3 on p9. Also read Proposition2
and its hypotheses on p488 of *Extreme values of derivatives of the
Riemann zeta function*, Mathematika68(2022),486-510,
[DOI10.1112/mtk.12130, primary PDF](https://tugraz.elsevierpure.com/ws/portalfiles/portal/49282848/mathematika_yang_22_12130.pdf).

Theorem1.1 bounds extrema over sets of cardinality N for the kernel
gcd/lcm multiplied by the product of equal powers of the two reduced
logarithms. Theorem1.2 allows complex coefficients but is an upper
spectral estimate with exponent tending to 1, not the required 1/2
endpoint relative to Q. The p9 proofs bound logarithmic weights by
small powers and use positive set sums. The 2022 proposition gives
a lower extremal bound for the product-log set sum. None states a
coefficient-uniform lower bound for our signed linear-log form.
Their proofs do not justify transferring entrywise inequalities to
arbitrary signed/complex coefficients. No result is imported from
either paper, and no RH-conditional argument is used.

### Source-covered finite discriminator

D. Bindel, *CS6210: Matrix Computations — Theory for SEP and SVD*,
3 November 2025,
[Symmetric eigenvalue basics / Variational approaches](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-03.html).
Read the Hermitian hypotheses, complete Rayleigh weighted-average
argument, generalized positive-definite-denominator statement and
Cholesky reduction. This is the standard Hermitian spectral/Rayleigh
variational theorem, not a new arithmetic theorem. L737 supplies the
finite Hermitian numerator and a positive denominator for nonzero c,
including its inversion check; thus the finite diagnostic has no
assumed inverse-Gram estimate. No spectral reduction is derived here.

The exact COVERED_TARGET is a later bounded calculation, after its
separate approval. At N=2^j, 1<=j<=9, use L737's original form or
existing divisor coordinates without deleting kappa or cross terms.
Floating spectra may select trial directions only. Save explicit
trial vectors and interval-certified F/Q values, with Q's positive
lower endpoint. Rational vectors in the original coordinates are
permitted; rational b coordinates may instead be used with the exact
relation c_n=sqrt(n)b_n. Retain every component and evaluate the
same F and Q. No approximate eigenvalue is a certified lower bound
for the entire spectrum. A negative certified trial tests C=0 only.

Record finite values against the required threshold inf_(N,c!=0)
F/Q>-infinity. Continue beyond the pilot only with a specific analytic
bound or an explicit scalable coefficient pattern and a new bounded
test of it. A proved sequence with quotient tending to -infinity
abandons the proposed absolute-C inequality. Stable, positive, or
negative finite values alone establish neither alternative. Without
a justified pattern or bound, report the pilot as inconclusive and
park this numerical mechanism; do not renew it by enlarging the grid.

The essential finite identities are already canonical in L737. No
new lemma, spectral claim, theorem reproof or mathematical script is
written in this literature step. Matching Mathlib coverage for the
critical inequality is unchecked; the generic spectral reference does
not establish it. No essential source-access blocker remains for the
finite test. Selberg-sieve optimization and other search-only leads
are unread and are not premises or required inputs to that test.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. This completes
one bounded comparison and prepares a diagnostic; it does not prove
or disprove TARGET, improve a known arithmetic bound, or resolve an
actual-Xi sign. PROOF.md and DAG.md do not change.
