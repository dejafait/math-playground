# Fixed atomic complete-tail/inertia calculation — audit nomination

TARGET: Critically audit L784's complex-root exhaustion, quantitative contour bound, exact complete-tail cancellation and full residual inertia for the fixed atomic law.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step454 reused the exact-target searches and failure comparisons in 2026-11-05-fixed-atomic-cosh-residual-index-test.md and 2026-11-05-reciprocal-quartic-inertia-test.md; checked L784 in full for source scope and the fixed-model/quartic stop records. No repeated discovery search or novelty inference.
SOURCE_EVIDENCE: Step454 reused inspected DLMF hyperbolic/logarithm and de Boor/Duits/Sylvester theorem/proof cases from steps449/452; additionally read DLMF 1.10(i), equation1.10.1 and Zeros, and 1.10(iii), equations1.10.6–7 through removable singularities, at https://dlmf.nist.gov/1.10 on 2026-11-05.
COMPARISON: L784 specializes known methods to one fixed measure and radius, with analytic complete-tail evaluation replacing numerical truncation; the source interfaces do not themselves certify its root enumeration, contour bound, cancellation or signs.
GAP: Independent verification of the complete L784 argument and exact interval certificate remains undone; no actual-Xi or generic positive-mixture sign follows even if this audit passes.
REASON: The separate source comparison now covers the proposed conceptual audit; its model-specific analytic cancellations and arithmetic remain to be independently checked. Source approval does not certify L784.

This is a proposed separate conceptual audit, not another model experiment.
The exact law remains mu=(delta_1+delta_3)/2+2delta_2, r=3,R=8,k=2,
sigma=9/8. Do not tune the measure, radius, projection, node grouping,
coefficient offset or target index, and do not repeat the closed diagnostic
as an exploration turn. First reuse the existing exact-model source
assessment, retrieving an additional primary interface only if essential
coverage is actually missing. The original nomination required separate approval; step454 below supplies
that source approval without performing the audit.

For the later audit, read L784 in full and inspect the selected complete
certificate values under `scripts/fixed-atomic-cosh/`. Essential inputs
are the primary identities cited in L784 and its own exact arithmetic;
L777/L782 are method/convention comparisons, L783 a contrast, and no
actual-Xi model entries are inputs. Check exhaustive logarithm branches,
the y-to-w multiplicity identification, both contour-lower-bound cases,
the R=8 derivative and residue signs, one-based beta_4/alpha^3 projection,
and convergence before all divided-difference limits.

In particular B=P^2/g=P/F is holomorphic after root removal, whereas
the uncancelled inverse 1/g has a smaller Taylor disk. Formula(6) is
finite jet extraction near0, and formula(7) must evaluate the complete
analytic tail, not continue the uncancelled inverse series. Verify the
identity b'(alpha_i)=1/d_i and cancellation against J_ii/E_ii^2 before
certifying inertia. Outward dyadic rounding must enclose all exact
operations, including negative powers; strict LDL pivots must pay both
index and nullity. A check preview alone is insufficient.

Continue only if every load-bearing hypothesis and interval comparison
survives. Correct a defect locally if possible; otherwise withdraw only
the unsupported claim and preserve its evidence. A passing audit validates
this fixed known-method specialization only. It leaves the missing
independent signed inequality, global grouping and actual-Xi signs open.
Matching Mathlib coverage remains unchecked. No creative mechanism is
approved: finite-jet cancellation alone offers no independently paid sign.


## Separate source approval — step454, 2026-11-05

LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED; the
newly written complete-tail cancellation needed its own source-scope
comparison before mathematical audit. This is that separate turn.
SCOPE: Exactly the TARGET above, unchanged law, r=3,R=8,k=2,sigma=9/8;
one REPRODUCTION conceptual audit, including necessary local repairs of
identified defects. No parameter search, generic index theorem or Xi sign.

The calculation assessment and its primary theorem/proof-case coverage
are reused, rather than searched again. The quartic assessment supplies
precise de Boor Example2/(10), Proposition25/(26), pp.49,53–54; Duits
DPP2 Lemmas66/69 pp.51–52; and Berkolaiko–Kuchment (2022), Theorem2.7
and proof pp.88–91. Its direct links remain the primary references.
De Boor supplies the quotient and repeated-node interface, not convergence
of a nonpolynomial series. Duits supplies finite-rank determinant
restriction with the recorded inner-product convention qualification,
not selfadjointness. Sylvester supplies invariance under invertible
congruence, not a residual sign estimate. No new application is proved.

For the changed analytic presentation, the primary NIST DLMF HTML
[1.10(i)](https://dlmf.nist.gov/1.10.i), equation1.10.1 and the following
Zeros paragraph, was read through the simple-zero definition. Analyticity
on the entire stated open disk is required for its Taylor expansion;
zero multiplicity is determined by the first nonzero local coefficient.
[1.10(iii)](https://dlmf.nist.gov/1.10.iii), equations1.10.6–7 and the
following singularity paragraphs, was read through the removable-limit
case. The annular hypotheses, strict interior coefficient contour,
positive orientation and absolute uniform convergence on compact subsets
are retained. The source is the live HTML accessed 2026-11-05; the prior
assessment identifies its DLMF version as1.2.8. No new version claim was
independently checked.

These interfaces cover the intended distinction in L784: a disk Taylor
statement about B after removability is established, and an annular
Laurent statement about b. They do not warrant evaluating the local
inverse series of g outside its convergence disk. The audit must check
that the six local jets identify the relevant coefficients of B, that
the asserted complete-tail identity follows on its claimed domain, and
that all node evaluations and diagonal derivatives occur there. This is
an audit obligation, not an assertion that those checks have passed.
The new source passage removes a scope ambiguity; no new identity,
coefficient, estimate or sign has been derived in this literature turn.

L784 uses no quadrature, so Johansson's optional integration interface
from step452 is unnecessary here. No Hadamard product, Böttcher–Widom
prefactor, infinite-dimensional selfadjointness or Schur index theorem
is needed for the stated finite-model audit. If a repair requires such
an additional theorem beyond the covered methods, record the uncovered
target for separate review rather than silently extending approval.

The local duplicate/failure comparison remains decisive: L783's quartic
has no established positive-cosh-mixture realization, and L773's Turan
grid is a different exhausted diagnostic. The fixed-law stop record
closes parameter experimentation; it does not forbid independent
verification of L784. Reading L784 for source scope and these stop
records does not constitute its mathematical audit. The prior reported
22 checks and inertia are not independently certified in this turn.

Continue with one audit only if the cited interfaces suffice. Verify
all branches, contour cases, residues, one-based projection, convergence,
complete-tail cancellation and interval implementation against the full
load-bearing evidence. A failure calls for a justified repair or withdrawal
of the affected claim, preserving evidence; a pass validates only this
fixed model. No actual-Xi positivity or general positive-mixture index
bound follows by citation. Full matching Mathlib coverage stays unchecked.

DECISION is SPECIALIZE, classification REPRODUCTION for the next audit.
This source review imports standard analytic interfaces only and approves
the unchanged target; it neither performs nor certifies the audit.
