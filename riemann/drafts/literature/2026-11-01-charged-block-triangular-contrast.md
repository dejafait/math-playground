# One fixed full-complex pair test: charged lattice versus horizontal collapse

TARGET: Evaluate the full BGST triangular-test pair-sum difference between L612's microscopic lattice and its horizontal collapse, and compare it with the O(T sqrt(log T)) fixed-test error.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact BGST/lattice and horizontal/Fejer/collapse searches plus scoped local duplicate/failure searches found the known transform and pair theorem, but no evaluated version of this precise finite contrast. This is bounded source coverage, not a novelty claim.
SOURCE_EVIDENCE: BGST https://arxiv.org/html/2306.04799v1 Lemma 5/(3.3)–(3.4) with proof, (4.3) triangular Fourier pair, Lemma 3 square integral; BGST https://arxiv.org/html/2501.14545v3 MT and cumulative correction (3.2)–(3.5); corrected L612, C464c charge and L018 coordinates. Complete interface and qualifications in 2026-11-01-charged-block-pair-statistic-scope.md.
COMPARISON: The source evaluates actual-zeta complete pair sums, not artificial lattices. Its triangular transform is known and must be cited. The uncovered difference is the full finite horizontal contrast with the exact Cauchy weight, simultaneous T-dependent lattice parameters and a uniform bound relative to the source error.
GAP: No contrast asymptotic or source-scale separation is proved. Neither finite model is assumed to satisfy the full form factor or zeta zero-count asymptotics. Charge conversion, Xi realization, other tests, exceptional heights and signs remain open.
REASON: This diagnostic isolates horizontal sensitivity while preserving the ordinate multiset; it avoids an irrelevant contradiction from L612's missing zeta normalization. It is independently testable and does not depend on inaccessible spectral-stability sources or on dropping mixed pair terms.
SCOPE: Exactly the two finite multisets and fixed triangular test below; full ordered pairs with multiplicity, diagonal/partner/all cross terms, w intact, log(2T) normalization, integer floors and slab endpoints. No all-test compatibility, source theorem for artificial zeros, new density theorem or all-displacement union bound is approved.

## Exact proposed calculation — no result asserted

Use all the hypotheses and parameters of corrected L612: T>=2H0,
L=log T, d=1/L, h=4/L, n=floor(T/h), gamma_j=T+jh for 0<=j<=n.
Only the positive-ordinate blocks enter the BGST statistic. Define

    R_T={1/2+d+i gamma_j, 1/2-d+i gamma_j : 0<=j<=n},
    R_T^0={two copies of 1/2+i gamma_j : 0<=j<=n}.

R_T^0 is a horizontal collapse for comparison, not a source zero set.
Retain its multiplicity two. Both sets have 2(n+1) members with identical
ordinate multisets, including gamma_0=T and any gamma_n=2T. In the
cumulative source convention use H=2T, L_H=log(2T) and 0<gamma<=H,
not the dyadic convention (T,2T] which would omit the first ordinate.

Import BGST v1 (4.3): for r(alpha)=(1-|alpha|)_+,
rhat(z)=(sin(pi z)/(pi z))² with its removable value at zero. Put

    Phi_H(u)=rhat(i u L_H/(2pi)) 4/(4-u²),
    Delta_T=sum_(rho,rho' in R_T) Phi_H(rho-rho')
             -sum_(rho,rho' in R_T^0) Phi_H(rho-rho').

These are algebraic squares, not modulus squares. Retain all ordered
pairs, both horizontal signs and every multiplicity product. Prove
reality if used. The finite sums have no infinite-product issue; an
integral representation, geometric-series step, infinite lattice limit
or sum/integral interchange introduced in a solution still needs a full
justification. In particular cancellation of a few partner terms is
not an evaluation of Delta_T. No quantitative conclusion is supplied
by this nomination.

The meaningful threshold is the actual fixed-test source error,
H sqrt(log H), equivalently its T-scale version in TARGET. A proof
Delta_T=o(T sqrt(log T)) would show lack of robust horizontal separation
at that error scale for these two families and this test. A proof of a
signed contrast whose magnitude divided by T sqrt(log T) tends to
infinity would justify investigating additional model normalization
and a charge-conversion inequality. A bound only O(T sqrt(log T)) is
inconclusive because the source constant is unspecified. Neither a
large contrast nor compatibility of this one contrast proves a
constraint for the full collection of tests or an actual-Xi saving.

## Use, limits and stopping test

The main gap is actual-Xi all-degree signs at unbounded heights. This
finite diagnostic tests a materially additional complete-pair observable
before investing in a charged-union argument. L612's T/3 union obstruction
and both original count constraints remain intact. No attempt to derive
o(T) from those counts alone is reopened. A refined source-sensitive
observable could eventually help isolate exceptional centers; actual-Xi
normalization, conversion to a union, microscopic uniformity and initial
signs would still be separate gaps.

Perform one analytic evaluation/bound of Delta_T. Continue only on proved
source-scale discrimination; otherwise park this fixed contrast with its
actual bound, or preserve a precise unresolved estimate. A numerical
preview is not an asymptotic certificate. If a script is useful in the
later research turn, it must save complete evidence and print only the
relevant results, bounds, failures and paths. No mathematical script or
calculation was made in this literature review.

No substantial theorem reproof is needed: cite the triangular transform
and source error; justify only the new finite calculation. This is
ordinary calculation, not proof_attempt/creative. A new central creative
mechanism remains unprepared because no positive charge conversion with
controlled complete-pair remainder has been identified. Full and
supporting Mathlib coverage are not checked. This newly written ready
continuation receives separate approval next turn.

## Direct-source gate repair and approval — 2026-11-01

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs
in this ready assessment; the mathematical target and scope are unchanged.

Inspected [BGST v1, Lemma 5 and its complete proof, (3.3)–(3.4),
and (4.3)](https://arxiv.org/html/2306.04799v1#S3): the test must be
real, even, integrable, supported in [-1,1], and Lipschitz at zero.
The fixed triangle satisfies these requirements. Equation (4.3) supplies
its squared-sinc transform; the removable value is understood by continuity.
The proof treats the peak at zero using Lipschitz continuity. The theorem
concerns the complete ordered actual-zeta sum with multiplicities and the
complex weight; it does not evaluate the proposed artificial multisets.
No reproof of this imported transform is requested.

Inspected [BGST v3, Section 3 MT, correction footnote, and complete
cumulative proof (3.3)–(3.5)](https://arxiv.org/html/2501.14545v3#S3).
The corrected cumulative formula has an additive O(H sqrt(log H))
remainder for 1<=x<=H. The footnote expressly preserves the earlier
Lemma 5 and Lemma 7 applications. Thus the saved fixed-test error
benchmark remains appropriate. This does not supply uniformity over
varying tests, justify removing complex weights, or authorize a dyadic
subtraction omitting cross pairs. The cumulative convention H=2T is
retained. The current HTML header labels v1 as 7 June 2023 and v3 as
1 September 2026; their displayed manuscript dates differ. The precise
version URLs and equation identifiers, rather than those dates, identify
the inspected statements.

Reused the existing scope comparison and its duplicate/failure search;
read L612's hypotheses/conclusion and the direct-transfer stop. No changed
claim calls for another broad search. The independent finite contrast
remains EXPLORE, with the same error-scale continuation/parking test.
This review approves its source coverage only. No Delta_T bound, new lemma,
mathematical script, charge-union implication or source-compatibility claim
was produced. Mathlib coverage remains not checked. Recovery repairs an
explicit citation defect and is reported STALLED, not mathematical progress.
