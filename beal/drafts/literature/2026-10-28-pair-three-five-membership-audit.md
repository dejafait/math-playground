# Source gate for the new local-membership critical audit

TARGET: Assess source coverage for a critical audit of L147's complete 3/5-adic images, all-place Selmer membership and rank bound 2+c<=4.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L147 with L135/L138/L139/L145, history/529 and ATTEMPTS/065; reused the odd-model, eleven-adic, dyadic and supported-dimension assessments and their duplicate/failure searches. Queries "67760" "1581228000" Jacobian and "Stoll" "Lemma 4.4" "bad" "2-descent" supplied no inspected exact-instance replacement. Search failure is not novelty evidence.
SOURCE_EVIDENCE: Refreshed Stoll's publisher PDF, 33 pages, Section 4 pp.249–253: Lemmas 4.1/4.3/4.4, Proposition 4.2, Proposition 4.6 with both discriminant cases and Corollary 4.7; equation (1.1) p.245. Refreshed Clark's 161-page author notes, Proposition 2.20/full proof p.72, Exercise 2.11 and Theorem 2.24/full proof p.73. Reused prior complete Section 6 and supported-group source assessments; precise qualifications below.
COMPARISON: Named theory covers the exact odd-model representation, bad-odd-prime image dimensions, ramified odd-residue square classes, outside-support membership and torsion subtraction. It does not certify L147's ideals, residues, masks, simultaneous quotient independence or selected products. Those are the bounded instance audit, not a new general descent theorem.
GAP: Source coverage is ready; separate critical mathematical review of L147 and its complete load-bearing certificates remains pending. No Selmer equality, actual rank or pairing is supplied by the literature.
REASON: Completes the distinct source gate for the new L147 audit by matching its hypotheses and interfaces; approves a later critical review, without executing that review or deriving mathematics here.
LITERATURE_REASON: The new L147 critical-audit target requires a separate comparison of its ramified local coordinates, simultaneous quotient argument and all-place membership with the previously inspected general theory; unchanged method coverage is reused.
SCOPE: Only source assessment and critical audit of the existing L147 on L138's actual Jacobian and L145's fixed 39 witnesses; no new local filter, global basis, covering construction or point search.
COVERED_TARGET: Critically audit L147's complete 3/5-adic images, all-place Selmer membership and rank bound 2+c<=4.

## Gap, target and discriminating test

The main gap remains exclusion of all residual primitive Beal solutions.
The intermediate target is reliability of L147's partial rank bound and
two asserted Selmer classes. Acceptance would provide a stronger baseline
for further descent and eventual point control. Even the claimed bound
four exceeds the sufficient bound one by three; integer recovery and all
other residual signatures remain independent obligations.

Continue with the covered audit only if every theorem hypothesis, actual
local coordinate map and load-bearing certificate survives independent
review. Correct or withdraw any affected claim on a precise discrepancy;
an arithmetic replay is evidence, not that conceptual review. No new
mathematical calculation, lemma or script is authorized by this literature
step. A later audit may replay the existing certificates as needed.

## Precise imports and applicability

Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, Acta Arith. **98** (2001), 245–277,
[DOI 10.4064/aa98-3-4, publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
accessed 2026-10-28, 33 pages. Section 4 assumes monic integral squarefree
odd-degree f. Lemma 4.1 and Proposition 4.2 identify the full norm-kernel
representation and all-place membership; Lemma 4.3 gives point/branch
evaluation and factor-count torsion. Lemma 4.4(1) gives local image
dimension m−1 at odd primes, including bad reduction. Its proof refers to
Schaefer [16, Proposition 2.4] or Milne [11, Lemma I.3.3]; these underlying
proofs were not independently retrieved. Proposition 4.6 equates the image
with the valuation kernel when p is odd and p² does not divide disc(f).
Both its good-reduction and discriminant-valuation-one proof cases were
read. Corollary 4.7 gives sufficient finite support. Equation (1.1), p.245,
gives the rank upper bound after subtracting rational two-torsion dimension.

L138's already audited model and discriminant are precisely the inputs
needed for this source scope. The audit must bind those data to L147,
rather than assume that field discriminant and polynomial discriminant
are interchangeable. At 3 and 5 use Lemma 4.4, not Proposition 4.6.
Outside infinity,2,3,5,11 the latter proposition is the relevant criterion.
No scalar quotient appears in Section 4's odd-model representation.
Reuse Section 6's actual-divisor and dimension-saturation coverage from
`2026-10-26-pair-eleven-adic-filter.md` and
`2026-10-27-pair-two-adic-kummer-filter.md` in this directory. L147 uses
dimension saturation, so exhaustive source-disk recursion is not required.
The audit must authenticate the asserted generators before saturation.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author-hosted notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161 pages, accessed 2026-10-28, revision date unidentified. Proposition
2.20 and its full proof, printed p.72, split a discretely valued field's
multiplicative group into units and valuation after choosing a uniformizer.
Theorem 2.24 and its full Hensel proof, p.73, put 1+4*pi*R among squares
over a Henselian discretely valued field of characteristic different from
two. Exercise 2.11(a) states the odd-residue square-class dimension; it
is an exercise, not an inspected proof. Import the standard named Hensel
square criterion for odd residue characteristic, as in the earlier
eleven-adic audit. No tame-ramification hypothesis occurs. The wild cubic
at 3 is therefore within source scope, conditional on authenticating the
actual complete field and normalized valuation. Residue characteristic
two must retain L145's separately audited coordinates.

Reuse `2026-10-25-pair-genus-two-odd-model-support.md` and
`2026-10-26-pair-supported-norm-dimension-audit.md` for the unchanged
ordinary supported-group framework. Reuse
`2026-10-26-pair-eleven-adic-audit.md` and
`2026-10-27-pair-two-adic-kummer-audit.md` for accepted interfaces.
No reproof of the imported descent or unit/class theorems is justified.
Full matching Mathlib coverage is not checked; no absence is asserted.

## Bounded critical-audit obligations

Essential inputs are L135/L138/L139/L140/L141/L145/L147. Read the complete
relevant evidence in `scripts/pair-genus-two/odd-membership-35-certificate.json`
and `odd-membership-35-verification.json` in that directory, both existing
implementations, and the exact dependency evidence needed to bind their
inputs. A bounded preview cannot establish these claims.

1. Check that the maximal-order prime lists are complete at 3 and 5;
   bind their indices, ideal products, both lattice containments and
   determinants to the actual field. Check each uniformizer and the
   ramification/residue data before counting local algebra factors.
2. Check exact valuation/residue normalization for integral elements and
   denominator clearing, retaining the class of rational p in ramified
   components. Verify multiplicativity and the rational factor. Read all
   relevant saved rows, including failed point tests and depth/cap handling.
3. Authenticate the branch sign and every displayed genuine local point,
   the full product evaluations, nonzero components and generator ranks.
   Only then compare with the sourced full-image dimension. Reaching that
   dimension must cover all Jacobian classes, not only sampled curve points.
4. Audit all 39 witness columns, support and norms, the previous joint
   kernel and the simultaneous new quotient map. Check L147's three
   witnesses are in the old kernel and independent in the joint quotient.
   Their global coefficient map need not be injective or surjective;
   neither dimension 31 nor independent formal coefficients are a Selmer
   dimension or a global basis. Check the exact rank-nullity inference on
   the full supported filtered group and rational two-torsion subtraction.
5. Audit both selected products, norms, every required local membership,
   and the outside-support valuation implication. Check that their full
   localization tuples certify global independence in the unsimplified
   odd-model square-class group. No assertion of Mordell–Weil membership,
   positive rank or nonzero Cassels–Tate value follows from Selmer membership.

These are audit obligations, not verified conclusions of this review.
The claimed arithmetic masks and dimension losses have not been recalculated.

## Overlap, stopped route and decision

The prior Cassels–Tate assessment already covered the general membership
methods; this step adds the explicit critical-audit comparison and boundary,
not another general-method search or an originality claim. L135/L138/L139
and L145 provide ready accepted inputs, not duplicates of L147's instance
claims. History/529 separates arithmetic replay from independent review.
ATTEMPTS/065 parks the raw covering construction and supplies no input
to L147; do not enlarge its box or repeat backend probes. Earlier stopped
local-image refinements remain preserved. No cross-notebook input is used.

Decision: the covered conceptual audit is ready as a known-method
specialization. Source access is not blocked. No justified new creative
central mechanism is prepared; the pending essential audit takes priority.
If that audit accepts the result, a materially different, source-assessed
mechanism is still needed for further rank or point-control progress.
