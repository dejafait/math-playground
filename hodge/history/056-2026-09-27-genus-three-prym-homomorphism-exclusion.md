# 2026-09-27 — Genus-three Prym homomorphism exclusion

STEP_ID: 2026-09-27-hodge-056-genus-three-prym-homomorphism-exclusion.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint, the
whole proof overview and ID-only DAG. Inspected the existing
changes, L032, the stopped small-factor recipe and both recent
Prym reviews; preserved all prior work. The saved exact-target
assessment was already SPECIALIZE, so this invocation performs
its single bounded homomorphism test.

The gap is algebraic beta_U beyond the Dickson locus, with algebraic
kappa separate. A genus-three Prym map could transfer determinant
classes already in degree four, subject to a qualifying source
and the whole tensor-image certificate. The discriminating test
was a common constituent under one joint Hodge group. Total Prym
dimension is unrestricted, so L032 alone did not answer it.

[L033](../lemmas/L033-genus-three-prym-homomorphisms-vanish.md)
proves vanishing of every homomorphism in either direction with
powers of A. Invariant character spaces have dimension four,
whereas the target's complete spin representation has irreducible
constituents of dimension 64, also after restriction through the
surjective joint-group projection. The proof checks both arrow
directions, all eight target types, rational descent, source
endomorphisms, non-equivariant maps, products and isogenies. The
required nonzero-map threshold is not attained. No generic-source
assumption or total-dimension cutoff is substituted for this test.

Reused the ready [assessment](../drafts/literature/2026-09-27-genus-three-prym-homomorphisms.md)
and reread its primary passages: Patel--Zhang v2, Theorem 2.4,
Example 2.5 and Lemma 2.9--Corollary 2.10; Borovoi's Proposition
(a),(d); Moonen--Zarhin section 3.1; Moonen's Corollary 4.5 and
Lemma 4.6. The character formula excludes the invariant summand.
The known tools are imported, not reproved; their scoped application
is REPRODUCTION without an originality claim. No new source search
or target assessment was needed to execute this reviewed step.
Mathlib coverage is not checked.

Stop the genus-three homomorphism channel, recorded in
[the attempt](../ATTEMPTS/023-genus-three-prym-homomorphism-transfer.md).
The distinction from the previous failure is explicit: even large
Pryms in this genus cannot supply these maps. Higher-genus sources
have determinant classes in higher degree, and transferring those
with algebraic degree-lowering is a different untested operation.
Its [pending assessment](../drafts/literature/2026-09-27-higher-genus-prym-lefschetz-transfer.md)
is REVIEW_REQUIRED; no calculation or literature screening of
that new image target was performed here.

The previous bounded window ends on its third turn with this
informative negative result and route decision. Consecutive
exploration count is now zero. No new algebraic class or transverse
surface is supplied: the span stays 21 on the known family, with
three attained RM directions against four required. Arbitrary
primitive fourfold classes and higher dimensions remain unresolved;
STATUS stays IN_PROGRESS and no complete candidate appears.

PROOF records the narrowed transfer route and its qualifications.
DAG adds only the genuine input of L032 to L033; earlier branches
and identifiers are unchanged. PROGRESS contains the sole compact
current checkpoint and exactly one concrete pending target.

Validation: python3 ../scripts/docs/check_structure.py --problem hodge
passed with 34 nodes and 81 edges, valid links and compact overviews.
Metadata checks confirmed the exact completed target, the prior
SPECIALIZE/REPRODUCTION pairing, all eight assessment fields and
the new Next action's exact match to its REVIEW_REQUIRED assessment.
Whitespace checks passed. SHA-256 comparison confirmed preservation
of all 52 existing lemma/script files and the prior assessment;
only the three overview/checkpoint files changed, with the four
recorded additions. The mathematical check was the written
joint-group argument in both directions, including projector
invariance and contravariance; no computational experiment was
needed or mathematical script changed. Structural validation does
not certify the mathematics or resolve the main conjecture.
