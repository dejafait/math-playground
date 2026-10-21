# Pair-only quotient — critical audit coverage

TARGET: Critically audit L109's pair-only quotient, genera, proper forgetful maps and normalized minus-three lifting.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the construction assessment's exact-polynomial, unordered-pair, Belyi and Putz searches and duplicate comparison; compared L109's full proof with its covered methods and checked history/374 plus ATTEMPTS/046-minus-three-joint-factor-at-seven.md and ATTEMPTS/048-rational-factor-direct-scaling-quotient.md; narrow Stacks searches for finite-etale base change and normality supplied 58.5.2 and 58.11.2.
SOURCE_EVIDENCE: Reused the inspected Debes–Fried, Putz, Milne v2.21 and Stacks cover/genus sources in drafts/literature/2026-10-20-forget-distinguished-root-quotient.md; retrieved current primary Stacks 39.23.9 (03BM), 53.2.6 (0BY1), 59.28.1 (03PK), 15.116.2 (09EV), 58.5.2 (0BL6) and 58.11.2 (0BQL), reading statements and the relevant quotient, extension, unit-root, DVR, base-change and normality proof cases.
COMPARISON: The general quotient, cover, curve-model, tame-genus and Kummer methods cover this audit; 58.5.2 and 58.11.2 explicitly cover the proper-pullback normality step once etaleness and connectedness are verified. No inspected source directly certifies L109's particular models, constants, genera or certificate.
GAP: Independently verify all instance-specific scheme identifications, rational twist and constants, degrees, boundary etaleness, proper Cartesian assertion, complete ramification and incidence indices, geometric z orders and both normalized residue-lifting cases; the critical audit itself remains unperformed.
REASON: Exact audit-scope comparison is now complete and essential source coverage is available; perform the unchanged critical audit in a separate research invocation without repeating general browsing or treating source readiness as verification.
SCOPE: Exactly TARGET on L109's specified opens and smooth proper normalizations, with audited L106/L107 as inputs and the full forget-root certificate as evidence to audit; excludes point enumeration, hyperelliptic models, other twists and integer-system elimination.
LITERATURE_REASON: The saved audit target was REVIEW_REQUIRED and not a preapproved construction subtarget; this separate coverage turn reuses adequate sources and supplies explicit support for the proper Cartesian and local-normalization obligations.

## Gap, intended use and decision test

The main Beal gap remains exclusion of all positive primitive integer
solutions in residual signatures. On this route the independent gaps are
rational-point control, degree-nine rational-root recovery, remaining-factor
compatibility and both L095 integer power/gcd/positivity systems.
The intermediate target is a critical audit of L109, not another construction.
If it passes, its smaller necessary genus-two image may support a later
point method. A favorable genus alone supplies no point or integer bound.

Continue if the scheme identifications, full constants, proper maps,
all normalization indices and both residue cases survive the independent
audit, with the same diagnostic 2<38 and at most 990 labels against the
1000 cap. Identify and repair or withdraw defective assertions if they
fail. Do not infer the audit result from its construction certificate's
reported check count. No certificate was rerun or verified this turn.

## Reused literature and duplicate/failure comparison

The ready construction assessment
`drafts/literature/2026-10-20-forget-distinguished-root-quotient.md`
contains the exact searches, source versions, page numbers, applicability
and inspected proof cases. Reuse its Debes–Fried, Pacific J. Math. 190
(1999), Sections 1.4–1.6 pp.51–52, especially (1.11), and Putz thesis
(2024), Section 4.3.2 pp.134–135, (4.3)–(4.5), Proposition 4.18.
Their examples concern different maps; neither genus nor rational-point
classification is imported. No new exact-instance search is justified
by changing construction into audit. Unread leads recorded there remain
unread and are not premises. No novelty is inferred from search failure.

Reuse Milne, *Lectures on Etale Cohomology*, v2.21 (22 March 2013),
Theorems 3.1 and 21.3, pp.27,130–131, and Stacks 58.6.2 (0BND),
53.12.2/4 (0C1B), 53.8.2 (0BY6), 53.18.2 (0CE0) and
21.4.2–3 (03AG), with the covered characteristic-zero hypotheses.
Their primary statements were assessed previously, not reread this turn.
They do not certify the actual pair-label counts, transitivity or twist:
those are audit obligations using L106/L107 and L109's complete proof.

L107 retains the distinguished root and is not a duplicate pair-only
audit. History/374 records construction with audit pending. The L101
scaling stop in ATTEMPTS/048 reimposes the original power tests and is
not reopened. L105's exact seven-adic witness in the minus-three
ATTEMPTS/046 stops standalone local exclusion at seven, not this global
curve audit. L108's unfinished nonrational boundary work is independent,
preserved and not used. No cross-notebook input was read.

## Primary theorem hypotheses and audit obligations

All following primary HTML was retrieved on 2026-10-20. The narrow queries
were `site:stacks.math.columbia.edu etale morphism normal scheme normal 03`
and `site:stacks.math.columbia.edu finite etale base change normal scheme`.
Search snippets were followed to the primary statements and proofs.

1. [Proposition 39.23.9, 03BM](https://stacks.math.columbia.edu/tag/03BM)
   assumes an affine groupoid, finite locally free source and target,
   and an equivalence relation. It identifies the invariant-ring fppf
   quotient and its relation fiber product. Its proof uses flat
   base change of invariants and faithful flatness. The audit must
   check the actual free swap and invariant algebra on the specified
   open, rather than assuming a quotient for arbitrary projective equations.

2. [Theorem 53.2.6, 0BY1](https://stacks.math.columbia.edu/tag/0BY1)
   identifies transcendence-degree-one function fields with normal
   proper curves and nonconstant morphisms; its proof extends rational
   maps uniquely. Verify the function-field inclusions, geometric
   integrality and constants before using this to identify proper models.
   An open Cartesian square by itself does not establish the proper one.

3. [Lemma 58.5.2, 0BL6](https://stacks.math.columbia.edu/tag/0BL6)
   gives exact base change on finite-etale covers for every scheme map;
   its finite-limit proof treats fiber products. The proper pullback
   argument may use this only after the lower double cover is proved
   finite etale at every boundary point, not just on the open.

4. [Lemma 58.11.2, 0BQL](https://stacks.math.columbia.edu/tag/0BQL)
   assumes a normal integral base and a connected finite-etale cover.
   It identifies the cover with the normalization in its function field.
   The proof establishes normality, domination by every component and
   decomposition into integral normal components, then uses connectedness.
   This supplies the source for the proper pullback identification and
   for the unit-root normalization step. The audit must still check
   connectedness through the actual incidence open and the matching
   generic quadratic extension; this lemma does not supply either fact.

5. [Lemma 59.28.1, 03PK](https://stacks.math.columbia.edu/tag/03PK)
   requires n invertible. Its proof constructs the finite free rank-n
   root algebra of a unit and checks its etale derivative. Reuse at n=2,
   after verifying the actual rational twist. In the DVR chart the unit
   condition must be justified after the even-order normalization.
   Both split and nonsplit residue algebras must be retained.

6. [Lemma 15.116.2, 09EV](https://stacks.math.columbia.edu/tag/09EV)
   treats adjoining an nth root of a uniformizer to a DVR: the root ring
   is the integral closure, a DVR with ramification index n. Its proof
   checks the maximal ideal and normality; tame assertions additionally
   require n prime to residue characteristic. This is not a theorem
   about arbitrary unit radicals. The normalized unit chart uses 03PK
   and normality as above. Do not substitute 09EV for that separate case.

The audit must inspect every branch, including infinity, and all actual
leading coefficients and normalized orders, keeping geometric branch
counts separate from rational residue-field classifications. The minus-three
Q-form must be checked before geometric label methods are applied.
The finite certificate's representatives determine conjugacy types only;
actual monodromy is supplied by audited L106. No reproof of these general
source theorems is justified; the needed work is their instance-specific
application and independent arithmetic review.

## Continuation and limitations

Essential inputs: audited L106 polynomial/monodromy/branch data and
L107 invariant incidence curves. L109 is the audit object, together with
`scripts/global-fiber-genus/forget-root-certificate.json` and its producer
`scripts/global-fiber-genus/forget_root.py`. Read/replay complete relevant
evidence during the later audit, not a bounded preview as verification.

All rational-point, rational degree-nine lifting, remaining-factor,
L095 power/gcd/positivity and minus-eleven gaps remain open. No lemma,
mathematical script, genus calculation or new proof was produced here.
Mathlib full matching and supporting coverage were not checked; no
absence or formal verification is claimed. This review approves method
coverage only and does not certify L109 or a complete Beal candidate.
