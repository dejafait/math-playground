# 2026-10-02 — Uniform obstruction to CM half twists on inherited copies

STEP_ID: 2026-10-02-hodge-063-direct-sum-cm-half-twist-obstruction.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint, whole
proof overview and ID-only DAG; the working tree was initially clean.
Reused the exact saved SPECIALIZE assessment without changing it.
The companion van Geemen--Izadi section 1.5 was reread to confirm
the imported criterion and sign convention; no new gate was cleared.

The gap was an effective weight-one auxiliary structure for an
abelian realization of the cubic action. The screened target retained
all finite multiplicities, all CM fields and all embeddings into
M_m(E), including fields not containing E. The continuation test was
zero forbidden top-piece support. A successful half twist would
still leave algebraic comparison cycles unresolved. L035 treated
only its fixed scalar action; the older Clifford/Prym obstructions
did not answer this matrix-action question.

[L036](../lemmas/L036-direct-sum-cm-actions-have-no-effective-half-twist.md)
gives the full proof: the top representation has real matrices,
and coefficient conjugation within that piece pairs the embedding
multiplicities. Any action requires even m, and every CM type has
forbidden dimension exactly m/2>0 against zero required. This closes
the entire inherited direct-sum recipe. The
[attempt record](../ATTEMPTS/027-direct-sum-cm-half-twists.md)
preserves its scope and stopping reason.

The half-twist criterion is imported; the matrix-support application
is reproduced. This is an informative negative notebook result,
without an originality claim or an assertion of progress beyond
the checked literature. Mathlib is not checked. No computation or
new mathematical script is needed for this uniform argument.

The bounded window ends after one literature exploration and this
informative negative step. The attained cycle span stays 21 and
the attained RM directions stay three against four required. Both
Kuga--Satake algebraicity inputs, arbitrary primitive fourfold
classes and the universal target remain unresolved. STATUS stays
IN_PROGRESS; no complete informal candidate appears.

The proposed different direction is a source review of the two
Kuga--Satake quadratic forms q and q_a. The existing audit supplies
a polarization-twisting lead, but no mixed algebraic comparison
has been established. Its
[REVIEW_REQUIRED assessment](../drafts/literature/2026-10-02-cubic-rm-polarization-comparison.md)
records the exact pending target and noncircularity test. No
calculation for that new target is undertaken here.

The overview and compact checkpoint record the scoped exclusion.
L036 uses the stated Hodge data and named criterion independently
of L035; its new DAG row has no earlier lemma inputs. All prior
lemmas, programs and the completed assessment are preserved.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 37 nodes and 83 edges. The shared literature validator
accepted RESEARCH / REPRODUCTION, the unchanged prior SPECIALIZE
assessment and the exact new target with REVIEW_REQUIRED. Baseline
hashes confirmed no deleted file or modified prior lemma, program,
assessment or history. Mathematical review checked the two distinct
conjugations, zero multiplicities and the m=2 consistency case;
these checks are not a computational certificate for the main target.
