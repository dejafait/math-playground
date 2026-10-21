# Retained rank-one algebraic cover — critical-audit coverage

TARGET: Critically audit L053's retained rank-one algebraic cover, cusp decomposition and point-group calculation without assuming native graph identification.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused construction/isogeny/Tate assessments and their inspected proof-case records; searched Stacks finite-etale Galois monodromy, henselian finite-etale residue correspondence and quotient-stack equivariant squares; read the precise primary statements and relevant proofs listed below. Checked L053, relevant L045/L048 hypotheses, ATTEMPTS/030 and histories/177–179; no duplicate audit of this limited result was found in those records.
SOURCE_EVIDENCE: Reused Sutherland Lecture 5 (2023-09-26) Theorems 5.11,5.25, pp.5–6,14, https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf ; Milne EC2 (2021) II.1.7,II.6.3,III.3, pp.49,70,102–103, https://www.jmilne.org/math/Books/EC2.pdf ; Kedlaya fall-2004 Tate Theorem 1, pp.2–4, https://kskedlaya.org/18.727/tate-curve.pdf ; newly inspected Stacks Theorem 58.6.2 (0BND), Section 58.7 (03SF), Lemma 10.153.7 (04GK), Proposition 95.15.3/Situation 95.15.1 (04UV), Lemmas 100.3.1 (04ZP),100.3.3 (04XD) and Section 100.3 (04XB), direct tag URLs below, accessed 2026-10-12.
COMPARISON: Standard results cover the quotient/factorization and Tate inputs, finite-etale monodromy, split henselian fibers, quotient-stack torsor description and descent of representability/finite-etale properties. They provide audit criteria rather than a verdict on the selected global subgroup, all rational fiber points, stack square or point-group formula. No native graph theorem is needed for the actual limited statement.
GAP: The later audit must check L053's precise field of definition, kernel/degrees, geometric surjectivity, entire cusp decomposition image, torsor equivalence including arrows, descent and exact point-group boundary; no audit verdict or new mathematical result is supplied in this review.
REASON: Essential monodromy/henselian/stack coverage was missing from the proposed audit assessment and is now supplied by precise primary references; existing isogeny/Tate coverage remains adequate without fresh native retrieval.
SCOPE: Only the unchanged limited L053 statement over its retained global fields and local embedding; no native graph identification, graph label, new curve/field, theta cover, complete selected data or numerical comparison.

LITERATURE_REASON: The independent L053 audit needs precise previously
uncited finite-etale monodromy, full cusp-decomposition and quotient-stack
applicability sources; this is not additional browsing of the ready
construction target or another attempt to retrieve the blocked native graph text.

## Reused evidence and qualifications

Reuse `drafts/literature/2026-10-12-native-rank-one-cover-cusp-application.md`
and `drafts/2026-10-12-native-cover-cusp-source-notes.md` for the already
inspected isogeny statements and proof cases. Sutherland's quotient proof
is a sketch; import the known theorem rather than claim a full reproof.
Milne's inseparable group-scheme qualification is retained; the audit
must verify characteristic zero and separability in this application.

Reuse `drafts/literature/2026-10-10-split-tate-compatible-local-packet.md`
and the retained L048 assessment for Tate uniformization. The author
handout's Theorem 1 is Galois-equivariant over each finite extension,
with nonzero parameter of absolute value less than one; it defers the
surjectivity proof to Silverman. Import the named Tate theorem, not a
new proof from the handout. Use the standard coefficients fixed by Milne,
not the handout's known displayed coefficient discrepancy. Silverman's
full chapter remains an unread, nonessential lead. The changed q_0 is
not the old rational q; no fresh coefficient or curve computation is needed.

## Newly inspected primary coverage

The Stacks Project live tag pages below were read on 2026-10-12; no
repository commit or byte identity is asserted. The explicit theorem
hypotheses and the indicated proof cases, not search snippets, are the
coverage basis. Search queries were `site.stacks.math.columbia.edu
fundamental group finite etale Galois cover connected`, `site.stacks.math.columbia.edu
henselian local ring finite etale residue fields`, `site.stacks.math.columbia.edu
quotient stack equivariant morphism cartesian square`, and the narrower
representable-morphism descent query. Secondary results were not imported.

[Theorem 58.6.2, tag 0BND](https://stacks.math.columbia.edu/tag/0BND)
requires a connected scheme and geometric basepoint. It identifies
finite-etale covers with finite fundamental-group sets, records basepoint
change up to inner conjugation, and makes pullback compatible with the
induced homomorphism. Read its proof, especially part (3)'s fiber-functor
compatibility. [Section 58.7, tag 03SF](https://stacks.math.columbia.edu/tag/03SF)
gives the connected-cover/simple-transitivity criterion and the normal
open subgroup description of Galois covers. These cover the audit's
arithmetic/geometric monodromy comparison; the audit still has to check
connectedness after geometric base change and the actual deck action.

[Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK)
assumes a henselian local ring and gives equivalence between its finite
etale algebras and those of its residue field. Read the decomposition,
full-faithfulness and essential-surjectivity proof cases. For the proposed
cusp check the relevant residue field is K at the origin of the global
curve, not the residue field of the 3-adic valuation. The audit must
check that the extended cover is finite-etale there and that its entire
closed fiber is split over K. Killing only inertia is insufficient;
the comparison must address the whole decomposition action on the
punctured henselian neighborhood, using pullback compatibility above.

[Situation 95.15.1 and Proposition 95.15.3, tag 04UV](https://stacks.math.columbia.edu/tag/04UV)
allow a group algebraic space acting on an algebraic space over the
same base. The quotient stack is equivalent to the stack of fppf
torsors with equivariant maps. Read the objects/arrows, trivial-object
functor, full-faithfulness through Isom sheaves and local essential
surjectivity. This supplies the exact definition needed to audit L053's
2-fiber-product argument. It imposes no freeness of inversion. Section
78.22 (04M8) was an orientation lead only: its defining groupoid square
is not cited as a theorem asserting L053's distinct equivariant square.

[Lemma 100.3.1, tag 04ZP](https://stacks.math.columbia.edu/tag/04ZP)
checks representability by algebraic spaces after a surjective flat
locally finitely presented algebraic-space cover. Read its faithfulness
proof. [Lemma 100.3.3, tag 04XD](https://stacks.math.columbia.edu/tag/04XD)
then checks base-change-stable, target-fppf-local properties on such a
cover; read its test-scheme/fppf pullback proof. [Section 100.3, tag 04XB](https://stacks.math.columbia.edu/tag/04XB)
explicitly includes finite, etale and finite locally free among those
properties. The audit must first justify the quotient atlas and the
claimed fiber product, then verify rank seven on that atlas. The
source supports representability by algebraic spaces; coarse quotients
and scheme representability are not silently substituted.

## Approved audit and stopping test

The main gap remains original finite B>=A and actual input/action/pilot/
essentiality. The intermediate target is independent critical validation
of L053's limited partial input. A validated algebraic cover can later
be used in a separately covered native-cover comparison; passing here
would not identify the tempered graph quotient or the native cusp label.

Essential inputs remain L053,L045,L048, with L044–L047,L042 through the
established inputs. Retain E_0/Q,F=Q(zeta_60,E_0[30]),K=D=F(E_0[7]),
Omega,u,w,H,N,l=7,M>=max(M_tors,31),K_w=N,F_u=H,v_3(3)=1 and
v_3(q_0)=30. Neither K=N nor q_0=3^30. L051,L052 are separate
prerequisites, not direct inputs to this audit. Native May 2020 and
byte-identity qualifications remain unchanged. Full matching Mathlib
coverage is not checked; unknown availability is not absence.

ATTEMPTS/030 stops literal rank-two full-multiplication substitution,
not this rank-one factor. History/179 preserves the native-source
blocker and explicitly limits Phi to point groups. No failed route is
reopened and no cross-notebook theorem is used.

SPECIALIZE approves exactly TARGET for a separate research turn using
known methods (REPRODUCTION). Verify every stated limited conclusion
and the hypothesis checks above. An error requires repair or narrowing;
a missing essential theorem outside this coverage requires a separate
REVIEW_REQUIRED target. Passing validates only this partial input.
Graph factorization/label, local base-field predicates, full selected/
theta data and original finite B>=A remain open. No new lemma, proof,
mathematical script or mathematical audit verdict was produced here.
