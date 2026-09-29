# 2026-09-27 — Cubic Kuga--Satake divisor supply excluded

STEP_ID: 2026-09-27-hodge-050-cubic-rm-divisor-tensor-obstruction.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared and local goals, shared prompt, checkpoint, whole
proof overview and ID-only DAG, and inspected existing changes.
The exact saved target had a prior SPECIALIZE assessment; it was
reused unchanged. Reopened the already assessed primary statements
for their group and embedding conventions, without changing the
target or performing a new-target review. Preserved earlier work.

The gap was a cycle representative for the missing fourth cubic
RM direction. The proposed intermediate supply was beta_U in the
full divisor algebra on A^4. Membership would discharge one input
to the conditional transfer, with algebraic kappa still missing.
The test was invariance under the full polarization centralizer,
not the smaller Hodge group or a dimension comparison. Earlier
support/sheaf/bundle failures did not decide this different test.
Saved an [interim record](../drafts/2026-09-27-cubic-rm-divisor-tensor-test.md)
before completing the proof.

[L031](../lemmas/L031-cubic-kuga-satake-tensor-outside-divisor-algebra.md)
gives a negative certificate: an element fixing all divisor classes
multiplies a nonzero projected component of beta_U by four. Its
volume-element argument retains the full Clifford space, arbitrary
auxiliary v_0 and polarization, and the four distinct Kunneth
factors. Injectivity of the selected vector block and vanishing
of the other two projected eigenspaces prevent cancellation.
Scalar extension suffices for a negative invariant test; no
rational automorphism or descended projector is assumed.

Milne's criterion, Schlickewei's RM spin group and the standard
Clifford embedding are imported known inputs. The tensor calculation
is their specialization, recorded as REPRODUCTION with no originality
claim. The checked sources did not directly answer this exact
membership question. The result is informative negative evidence
for a construction, not a disproof of the Hodge conjecture or of
beta_U's algebraicity. The required membership threshold fails even
with every mixed divisor allowed.

The divisor window closes on its third turn, after two exploration
reviews and this negative result. There is no unanswered exploration
carried past the limit; the consecutive exploration count is zero.
The full Kuga--Satake route remains unresolved. The previous
doubled-source stop is preserved. The attained span is still 21,
the attained directions still three against four required, and
arbitrary primitive fourfold classes and higher dimensions remain
open. STATUS stays IN_PROGRESS; there is no complete candidate.

The new direction compares published exceptional algebraic-cycle
supplies, including Schoen's Weil constructions and any applicable
extensions. This is motivated by the certificate and leaves kappa
separate. The exact new action has a
[REVIEW_REQUIRED assessment](../drafts/literature/2026-09-27-cubic-rm-exceptional-weil-cycles.md).
No mathematical work or source assessment on that target was
performed in this turn.

Added the proof, small exact check and scoped failed-attempt record;
updated the overview, current checkpoint and DAG. L031 imports its
standard inputs directly and defines its tensor under the stated
very-general hypotheses, so it has no earlier local lemma inputs.
Mathlib coverage is not checked; cited framework is distinguished
from a match for the complete exclusion.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 32 nodes, 80 edges, valid local links and compact overviews.
The saved-context literature validator accepted RESEARCH under the
unchanged SPECIALIZE assessment and the exact new REVIEW_REQUIRED
target. SHA-256 comparisons confirmed all preexisting lemmas, scripts,
assessments and other artifacts unchanged except PROGRESS, PROOF and
DAG. Tracked and edited-file whitespace checks passed.

`python3 scripts/cubic-kuga-satake/check_divisor_tensor.py` passed:
exact Clifford relations and normalized volume signs, rank-six
vector block, a nonzero inverse-pairing tensor with 24 nonzero entries,
and the three-factor dual-pair/weight checks. The full proof also
checks equivariance, injectivity and noncancellation, rather than
deducing the theorem from that split model. These checks do not
verify the universal Hodge conjecture.
