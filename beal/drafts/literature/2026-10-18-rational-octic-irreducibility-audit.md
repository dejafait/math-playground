# L097 critical audit — source coverage

TARGET: Critically audit L097's Eisenstein certificate, homogeneous passage and system-II scaling, and verify the exact scope of the rational-descent stop.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused 2026-10-18-rational-octic-factor-descent.md and its exact-coefficient and binary-form searches; narrowly searched the rational-octic assessments and histories 324–325 for duplicate audits, and read ATTEMPTS/043–044. No completed independent L097 audit was found in those records; no novelty inference is made.
SOURCE_EVIDENCE: J. S. Milne, Fields and Galois Theory v5.10 (September 2022), Propositions 1.13 and 1.16, printed pp.12–13 (PDF indices 11–12), complete statements and proofs inspected on the author-hosted PDF; prior factor-descent comparison reused for scope, not expanded to other descent methods.
COMPARISON: The cited elementary criterion covers univariate rational irreducibility without a monicity assumption. It does not by itself certify the transcription from L095, the homogeneous passage, the system-II substitution, the certificate's implementation or any Diophantine consequence; these are the precise input-specific audit tasks.
GAP: Independent comparison of all nine coefficients and complete seven-check certificate with L095; proof review of coordinate-factor exclusion and rational scaling; verification that the stop concerns only direct rational polynomial factor-by-factor cube descent.
REASON: Essential source coverage is sufficient for the unchanged audit target. Specialize the inspected criterion and audit the existing elementary arguments in a later research turn; no new lemma, calculation or audit verdict is supplied here.
LITERATURE_REASON: The new independent-audit target had REVIEW_REQUIRED status; reuse the ready factorization assessment while resolving its exact audit scope, rather than repeat discovery or execute the audit in a literature-only turn.
SCOPE: Exactly TARGET. Permits independent exact arithmetic replay and proof review of L097 using L095, Gauss/Eisenstein, graded polynomial arguments and invertible rational coordinate changes. Excludes nonlinear substitutions, number-field descent, cube-value classification and integer emptiness.

## Main gap and intermediate purpose

The main gap is global integer elimination in both L095 simultaneous
systems, with other algebra factors and residual signatures unresolved.
The intermediate target is the independent audit of the recorded
irreducibility obstruction. Its downstream use is a trustworthy decision
whether to retire the direct rational factor-by-factor mechanism, so that
later work can select a materially different test rather than repeat it.
This does not make the audit a route to integer emptiness by itself.

## Primary theorem and specialization boundary

[Milne's author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, Proposition 1.13 on printed p.12 gives integral nonconstant
factors from rational reducibility. Proposition 1.16 is stated on p.12
and proved on p.13: a prime must avoid the leading coefficient, divide
all lower coefficients, and its square must avoid the constant term.
The conclusion is irreducibility over Q. The proof uses Gauss's lemma,
then propagates divisibility through one proposed factor until its
leading coefficient contradicts the hypothesis. Both complete proofs
were read; no reproof is needed. The existing p.13 citation points to
the proof; the audit should retain the complete pp.12–13 locator.

The audit must distinguish this imported criterion from L097's own
homogeneous and coordinate-change arguments. Those are already written
out in L097 and were within the prior approved elementary scope; checking
them is permitted without proposing a new theorem. No source theorem
about absence of cube values is available or required for this limited
stop. Full matching Mathlib coverage remains not checked.

## Exact future evidence and discriminating test

Essential inputs: L095's displayed H and both simultaneous systems;
L097's complete proof; scripts/rational-factor/check_octic_irreducibility.py
and the complete scripts/rational-factor/octic-irreducibility-certificate.json.
The script was read only to establish evidence scope; it was not run and
the certificate was not verified in this source review. Its factor-degree
field is a theorem-based assertion, not an independent factorization
oracle. A later audit must inspect every relevant certificate field,
compare against L095 rather than only the hard-coded array, and check
the unbounded proof separately from its finite arithmetic.

Continue with the recorded stop only if the complete arithmetic and
proof review pass. A coefficient, boundary, scaling or scope failure
requires an explicit correction and reassessment; a successful audit
cannot certify integer emptiness. Irreducibility does not rule out cube
values, factors after nonlinear substitution or larger-field descent.
ATTEMPTS/043 records an independent eleven-adic local-existence stop;
ATTEMPTS/044 records the current direct rational-factor stop. Preserve
both, and do not infer a global prohibition from either. No cross-notebook
input, new lemma, mathematical script edit or candidate resolution is
part of this turn. L097 remains unaudited pending the next research step.
