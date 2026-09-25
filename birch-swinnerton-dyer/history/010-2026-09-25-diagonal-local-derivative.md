# 2026-09-25 — The Coleman series leaves the ordinary derivative undetermined

Resumed and preserved the unfinished
[localization draft](../drafts/2026-09-25-strict-diagonal-localization.md).
The active notebook initially had no uncommitted changes; existing
changes in other notebooks were left untouched. Rechecked the current
Clay page and Wiles's page-2 rank assertion; the scope is unchanged.

[L010](../lemmas/L010-diagonal-local-derivative-and-coleman-kernel.md)
finishes the audit of the actual diagonal family's first-order local
conditions. It identifies the strict derivative with half the
anti-invariant pair formed from the ordinary derivative u. The exact
threshold is vanishing of the full localization modulo T^2. The
source's theta double zero supplies only vanishing of its scalar
Coleman image modulo T^2. A fixed full scalar series still permits
arbitrary u locally; the explicit first-order diagram also respects
the one zero localization and conjugation. No global arithmetic
realization of that freedom, or actual value of u, is asserted.

The [source audit](../foundations/09-cm-diagonal-deformation.md) retains
Theorem 3.6, Corollary 3.7, Theorem 3.4, Proposition 4.3, Lemma 4.4,
and the Section 5.5 bounds with direct links. The publisher's HTML
settled the prime labels lost in PDF text. Checked coefficient
specialization, absence of local H^0/H^2 corrections, the nonzero
augmentation factors, the ordinary kernel, and the factor 1/2 and
minus sign in averaging. The module ambiguity is proved algebraically;
no numerical computation or library lookup was needed. Mathlib
coverage remains explicitly not checked.

Decision: stop the inference from scalar Coleman vanishing to strict
lifting, as recorded in [the attempt](../ATTEMPTS/008-coleman-double-zero-strict-lift.md).
This changes the research decision without resolving q(kappa) = 0.
The achieved bound r <= 2 remains short of r >= 2. The reason for
changing to strict/relaxed duality is to test necessity for rational
Kummer classes before pursuing more formulas for the unknown u.
Analytic nonvanishing, auxiliary existence, and the universal rank
comparison remain separate gaps. No complete candidate exists.

PROOF.md records the refined obstruction, and the new DAG row uses
only L009 as a direct notebook input. The scalar reciprocity and
height-filtration bounds are named external inputs. PROGRESS.md is
the sole current checkpoint and concrete next-action record.

Step BSD-2026-09-25-010-diagonal-local-derivative is NEGATIVE.
STATUS remains IN_PROGRESS. Exploration turns without an advance
or informative negative result remain 0 of 3.
