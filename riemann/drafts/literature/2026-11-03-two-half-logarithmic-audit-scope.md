# Source scope for the two-half logarithmic audit

TARGET: Audit L691's two-half-displacement logarithmic bound, checking the split contour, uniform annular limit, nonidentity, logarithmic convergence through circle zeros, and complete charge accounting.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 99 reused step 97's independent-shift homotopy comparison and steps 93/95's full-circle source readings; read all of L691, L690 Sections 2–4/7, L657's exact statement/source scope, L666's admissibility/path passages and the relevant failure comparisons. Direct primary theorem/case retrieval is recorded below; no repeated discovery search or novelty inference.
SOURCE_EVIDENCE: Mathews--Howell online Sections 8.1 Theorems 8.1.5/8.1.7 and 6.2 Theorems 6.2.11/6.2.18/6.2.19; NIST DLMF 1.10(iv) Rouche statement and 1.10(v) maximum-modulus principle; Brunault--Zudilin Propositions 1.4–1.5 pp.6–7, including the complex-analytic boundary-root proof. Direct URLs, hypotheses and reuse limits follow below. L657's Issa--Lalin v1 Remark 3.8/Theorem 4.1 s=1 reading remains adequate and was not refreshed.
COMPARISON: The inspected sources supply finite contour/root tools, including boundary-root means, but do not prove the growing-degree annular limit or compact-parameter lower bound. L690 audits common shifts only; L691's single-interface specialization requires its own analytic audit. L665's absolute-transfer and L666's signed-energy stops concern different quantities; L663's integer lattice has a different census.
GAP: Independently audit L691's family-specific hypotheses and limit/zero-factor arguments before relying on its O(1) loss. No essential source is inaccessible; mathematical uniformity and nonidentity remain unverified. Full-cube shifts, effective onset, H/support, actual-Xi realization and signs remain outside this audit.
REASON: The invocation-start REVIEW_REQUIRED gate is completed by a separate source-only comparison. SPECIALIZE permits exactly the stated conceptual audit and necessary applicability checks; it neither accepts L691 nor authorizes a new full-cube mechanism. The newly ready continuation is submitted for the supervisor's separate next-turn approval.
LITERATURE_REASON: The saved continuation explicitly required source coverage for the new annular-limit/circle-zero audit; this changed proof mechanism was not covered by the common-shift audit. Reused ready assessments avoid another general Mahler-measure search.
SCOPE: L691's exact L666 subfamily: q>=1, n=12q+3, unit residues, fixed anchor x=-5/4, R=11/8, independent alpha,beta in [-1/8,1/8] constant within each half, all spatial moments, j=0 factor and denominator angle 1/u. Audit its existential absolute constants/onset and simultaneous straight-path claim; preserve complete L657 charges and circle zeros. No full-cube theorem, effective onset, independent interval backend or source-manuscript audit is included.

## Completed source-review task and relevance

The invocation-start target was: “Assess source coverage for a conceptual
audit of L691's two-half-displacement logarithmic bound, especially its
uniform annular limit and logarithmic convergence through unit-circle zeros.”
This literature-only step completes that task; TARGET now names the exact
separate audit it prepares. No lemma, mathematical script or proof overview
was changed, and no derivation or certificate replay was performed.

The main gap is actual-Xi all-degree mixed positivity and unbounded-height
signs. L691 claims only a two-half partial logarithmic bound within the
independent-displacement route. If validated, it could combine L690's base
with the original-D envelope to support that restricted route; it supplies
neither arbitrary independent shifts nor Xi realization. The source test
was to identify sufficient standard tools or a precise essential unread
hypothesis. The former is available; whether L691 meets those hypotheses
is the subsequent research task.

## Primary statements and reading limits

**Finite contours.** J. H. Mathews and R. W. Howell, *Complex Analysis*,
online edition, retrieved 3 November 2026:
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
Read the finite residue theorem and its disjoint-small-circle proof,
and the simple-pole limit rule. The contour is simple, closed and
positively oriented in a simply connected ambient domain; only finitely
many isolated singularities may occur inside, with analyticity on the
contour. This covers the type of finite rectangle identity used by L691,
provided its complete pole census and boundary clearances are checked.
It does not establish their values or the central-edge orientation.

[Section 6.2, Theorems 6.2.11, 6.2.18–6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html)
supplies contour parameterization, the absolute-value integral inequality
and the ML bound for a continuous integrand on a finite contour. Read
the parameterization statement, orientation-reversal formula (6.2.8)
and the proofs of the two inequalities. It does not supply uniform
majorants on an expanding interval. The later audit must check L691's
own radial derivative estimates and central-tail bound before using a
limit theorem. No improper-integral interchange is imported here.

**Auxiliary zero contours.** NIST DLMF, live online text retrieved
3 November 2026, [Section 1.10(iv)](https://dlmf.nist.gov/1.10#iv),
equations (1.10.8)–(1.10.9) and the Rouché paragraph: analytic f,g on
and inside a simple closed contour with |g|<|f| everywhere on it give
equal interior zero counts for f and f+g. Multiplicity is retained;
the argument-principle contour excludes zeros and poles. Also read
[Section 1.10(v)](https://dlmf.nist.gov/1.10#v)'s boundary maximum-modulus
statement, requiring a bounded domain, holomorphy inside and continuity
on its closure. The proposed uses are L691's auxiliary disks and
holomorphic quotients, not a zero-free assumption on the unit circle.
The audit must check that the selected disks stay in the analytic
domain and include every relevant zero. A transient fetch timeout was
resolved by direct retrieval; it leaves no source blocker.

For the proof case behind zero counting, reused and retrieved
[Mathews--Howell Section 8.7](https://complexanalysis.org/web/sec_argument-rouche.html),
Theorem 8.7.11/proof, Corollary 8.7.12 and Remark 8.7.13. The text's
meromorphic formulation compares zero-minus-pole counts with strict
boundary hypotheses. Its proof uses a quotient avoiding a ray; only
the ordinary analytic perturbation form above is needed by L691.
No derivative of roots at a crossing is licensed by either source.

**Boundary-root means.** F. Brunault and W. Zudilin, *Many Variations
of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4–1.5, printed pp.6–7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
Read Proposition 1.4 and all three modulus cases of its complex-analytic
proof, including the boundary indentation error tending to zero as
epsilon*|log epsilon|; read the polynomial extension and Proposition 1.5.
The normalized one-root mean is log max(1,|root|), including circle
roots. For a nonzero polynomial retain the actual leading coefficient
and all roots with multiplicity. This is enough for the finite root
means used in L691's proposed local factorization. The alternate
Riemann-sum proof is unnecessary at boundary roots. These propositions
do not themselves assert annular logarithmic convergence for functions
of growing degree or uniformity in a parameter square; those are
precisely claims to audit, not results imported by this assessment.

**Unchanged integrability and variation coverage.** Reuse
[the spatial-angular assessment](2026-11-03-spatially-averaged-angular-zero-charge.md)
and [the homotopy assessment](2026-11-03-independent-shift-mahler-homotopy.md).
L657's input from Issa--Lalin, arXiv:1203.5379v1, Remark 3.8 and
Theorem 4.1/proof p.7, s=1, concerns absolute logarithmic integrability
of a nonzero complex polynomial on the product torus for each fixed
polynomial. Its exact [primary URL](https://arxiv.org/pdf/1203.5379v1)
and proof-case reading were already assessed. It gives no uniform
degree estimate and no differentiation across torus zeros. Boyd's
fixed-degree continuity and the quantitative coefficient/term-count
results reviewed in step 97 remain inadequate substitutes for L691's
new analytic argument. No essential new version or changed hypothesis
requires refreshing them. Identity, open mapping, dominated convergence
and Fubini are standard named tools; their local hypotheses must be
checked rather than importing a family-specific consequence.

## Exact local evidence and prior failures

Read L691 in full. Read L690 Sections 2–4 and 7 for the inherited
fixed-rectangle bound, finite-product error, moving sides, kernel
clearances and the completed common-shift audit. Reuse that audit's
arithmetic evidence; source-scope approval does not require replaying
unchanged derivative certificates. Read L657's exact definitions,
complete accounting and source qualifications, and L666's family
admissibility and straight-path qualification. No sibling notebook was
used. L661 is downstream context, not an input needed to prove L691.

The certificate inspector read L691's exact `scope`, `unverified_here`
and `failures` fields. They explicitly separate rational clearances
from the split-contour identity, dominated limit, nonidentity,
singular-log convergence, onset value and full cube. The root preview
was used only to locate fields, not as analytic evidence. No rational
calculation was rerun and the recorded eleven checks are not promoted
to validation of the proof. The later audit must inspect complete
load-bearing checks if it relies on them.

Reuse step 97's duplicate/failure comparison: L665 stops its specified
absolute transfer for outward pairs; L666 parks its insufficient scalar
signed-energy bounds; L670/L671 and the later sparse/dual/Taylor records
stop their stated certificates. None establishes failure of L691's
complete two-circle mean. The L663 full-circle ATTEMPTS record was
read: its n=6q+3 integer lattice differs from L666's n=12q+3
half-shifted lattice plus anchor. That countersequence remains intact.
L690's common shift is a genuine overlapping special case; it does
not settle independent halves. No claim of originality follows.

## Separate audit and continuation/abandonment test

Audit the exact conclusion of L691, not a stronger cube claim. Check
the right-half residue census and central-edge sign; analytic domain
and radial/mixed-derivative clearances; domination on the entire moving
central segment; uniform Riemann sums and the order of limits for g;
holomorphy and parameter continuity of F; its value at zero and the
open-mapping/identity argument. Check smaller-annulus selection,
strict auxiliary Rouché contours, all multiplicities, quotient
convergence, boundary-root means and the compact-parameter subsequence
argument. Finally check the spatial Jensen/Fubini step and complete
L657 zero/pole accounting with unchanged P_n and controlled m_0.
No proof of any of these family-specific claims is supplied here.

Accept the restricted O(1) loss only if all essential analytic and
accounting claims pass. Otherwise record the exact failed hypothesis
or implication and retain only the justified restricted conclusions;
a failure would not refute RH or even the full homotopy target.
An essential source outside this scope would require a new explicit
source gate, rather than assuming it. Constants/onset remain existential.

This next task is proof_audit/conceptual_audit, deep_research/xhigh:
compactness, nonidentity and singular logarithms are delicate analytic
claims. It is neither a fresh creative attempt nor another finite
screen. The supervisor separately approves the newly ready assessment
next turn; the completed step 98 result remains preserved and unaudited.
After that approval, mathematical audit is the default continuation.

Mathlib: reuse only the qualified univariate supporting results in
L657/L690/L691, including
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`.
Full matching annular-convergence and family-specific coverage remains
unchecked; no absence claim or formal verification is made.
