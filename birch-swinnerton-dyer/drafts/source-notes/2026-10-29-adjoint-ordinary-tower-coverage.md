# Step 545 — adjoint ordinary tower source comparison

2026-10-29. Literature-only work; no new lemma or mathematical
calculation. The source comparison below concerns the held L128
interface, not a proposed resolution of BSD.

## Saved scope and local evidence

The main gap remains rational rank versus analytic order for arbitrary
E/Q. The intermediate target is a legitimate integral comparison of
the dual coefficient tower, including its level-two-to-level-one
transition. Its downstream use would be a relation test for L128's
conditional scalar calculation; it would not supply rationality,
nonvanishing, strictness, or the other held steps.

Read L123 hypotheses and coefficient construction, L127 hypotheses
and conclusion, L128 hypotheses/Step 1/step-534 action audit, L129
hypotheses/conclusion and step-539 integral/control audit, and
ATTEMPTS/061--063. Reused the step-535 source note
`drafts/source-notes/2026-10-28-l128-covariant-transfer-coverage.md`
for integral Betti--Tate and correspondence comparisons. The current
audit of L130 is motivation, not a tower-test input. Existing work
was inspected only inside this notebook and is preserved.

The continuation/abandonment test is the actual integral transition
square with all labels and factors retained. An unchanged covariant
forgetting pushdown on L129's C_m is already obstructed. A different
adjoint summand or degeneracy transition needs its own identification;
neither a rational isomorphism nor a formal reversed word is sufficient.

## Primary sources inspected

**Original tower.** Michele Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
levels after (6), Section 2.1.2/(15), Definitions 2.3/2.8,
Proposition 2.9, Remark 2.12 and Section 2.4 through Corollary 2.23.
Read Proposition 2.9's good/tame-Hecke, diamond and both intermediate
p-level proof cases. It concerns coefficient pullback, with the
original right-translation U represented by diag(1,p). Remark 2.12
supplies Kummer and universal coefficients. The control theorem uses
an inverse system labeled by forgetting pushdowns. The
[PDF](https://arxiv.org/pdf/2603.28327v2), PDF pages 17--18
(zero-based 16--17), supplies its omitted control diagram and labels.
These are separate systems; none of these statements identifies the
proposed p-level transport with the original physical coefficient action.

**General adjoint/Atkin--Lehner construction.** Dmitrii Krekov,
*Poincare duality in Hida families*,
[arXiv:2608.23844v1, 24 August 2026](https://arxiv.org/html/2608.23844v1),
Section 1.4 and Sections 2.1--2.6;
[PDF](https://arxiv.org/pdf/2608.23844v1), pp.4--14.
Its hypotheses include a connected reductive rational group with
reductive Z_p model, a Borel and torus, neat tame level as specified
in Section 2.1, and the Iwahori-decomposed levels of Section 2.3.
Read Lemmas 2.19--2.24 with their proofs: w tau normalizes the chosen
level and transports the coefficient sheaf; the integral coefficient
normalization is p^{<eta,lambda>}(w tau)^{-1}. Definition 2.27 uses
trace limits. Remark 2.28 retains Weyl-conjugated torus actions;
Remark 2.36 retains t -> w_0(t^{-1}) in the pairing. Read Definition
2.37 and Lemma 2.38's double-coset/normalization argument for ordinary
versus anti-ordinary projectors. Also inspected the moment diagrams
and proofs in Lemma 2.31 and Theorem 2.35 in PDF pp.11--13.

This is primary evidence for a *twisted*, level-sensitive construction.
It does not supply an identification with Fornea's particular finite
levels and physical lattices. In particular, neither neatness nor
cofinality nor integral descent from an auxiliary tame level has been
verified here. They are not added assumptions of L123. No full theorem
of Krekov is imported onto the original tower. Its printed proof of
Lemma 2.38 ends with a primed operator on both sides although the
stated conclusion exchanges projectors; the preceding conjugation
formula and both operator definitions were read. Do not silently fix
that line or use it to skip the independent finite double-coset test.
No claim that the theorem is false follows from this observation.

**Classical comparison, with its scope retained.** Alexandre Maksoud,
*A canonical generator for congruence ideals of Hida families*,
Research in the Mathematical Sciences **13**, article 18 (2026),
[published 29 January 2026](https://doi.org/10.1007/s40687-026-00598-y),
Sections 2.1--2.3, Proposition 6 and Theorem 8/(13).
For X_1(Np^r), p odd, (N,p)=1 and r>=1, Proposition 6 states an
integral ordinary-to-anti-ordinary Atkin--Lehner isomorphism. Its
proof is a reference to Hida, *Modules of congruence of Hecke algebras
and L-functions associated with cusp forms*, Amer. J. Math. **110**
(1988), 323--382, Corollary 3.2 and (2.4), p.347; that original proof
was not inspected. The surrounding Poincare comparison explicitly
matches homological T_n and diamonds with cohomological T_n^* and
inverse diamonds. Theorem 8's finite pairing retains (T_p^*)^r,
W_{Np^r}, inverse diamonds and (Np^r)^{2-k}.

This inspected account corroborates the distinction in L128's audit;
it is not a quaternionic integral-control theorem. Neither Proposition
6 nor Theorem 8 is imported to Fornea's tower. Ohta's 1999 Compositio
paper was inspected only at its publisher's abstract: its stated
projector excludes finite characters 0 and -1. It therefore supplies
no ready theorem for the required trivial finite-diamond summand.
The [1999 publisher statement](https://www.cambridge.org/core/journals/compositio-mathematica/article/ordinary-padic-etale-cohomology-groups-attached-to-towers-of-elliptic-modular-curves/6C6C1E540EF2C3FE4E3B0A66E78AC7BC)
was the only passage read there. Its proof and the original 1995 pairing proof remain unread leads,
not essential premises of the finite test below.

## Comparison decision and bounded continuation

The decision is SPECIALIZE **only for a necessary finite transition
test**, not IMPORT of a full intertwiner or control repair. Fornea's
actual levels, pointwise correspondences, both pullback proof cases
and ordinary idempotents, together with the already assessed integral
comparison/transfer inputs in step 535, suffice to *calculate* such
a test on the original smooth proper curves. Krekov and Maksoud
explain why an adjoint summand, inverse labels and a changed transition
must be tracked. Their global control/pairing conclusions are not
needed to define or compute that necessary condition. This restriction
avoids an unproved neat-level descent or a reproof of Hida theory.

The proposed test uses, at levels m=1,2 only, the p-component
w_m=[[0,-1],[p^m,0]], with identity away from p. This is a candidate
suggested by the cited Atkin--Lehner matrices, not a proved simultaneous
intertwiner. Determine whether it normalizes the *actual* K_m, then
compare its diamond and U_p conjugations with the adjoints obtained
from the integral evaluation pairing. Compute the transition obtained
by transporting the dual of coefficient pullback, including any
degeneracy correspondence and all multiplicities. Specify each source
and target lattice, composition order and ordinary projector. No
formula for that transported transition is asserted in this review.

Passing means an exact integral finite square with the correct
adjoint labels and a transition different from the unchanged
obstructed identification, together with the precise remaining control
obligation. Merely conjugating a matrix or identifying rational spaces
does not pass. Failing means the first normalizer, label, summand or
transition discrepancy; preserve it and stop this candidate. If the
square forces the original covariant pi_* on L129's C_m and claims
surjectivity at its nonzero controlled target, L129 already rules it
out. No p^{-1} transition is allowed without proved divisibility and
compatibility. Even passing this necessary test would leave all-level
control, relation transfer to N_0, L128's later steps and the independent
arithmetic gaps unproved.

This is a known-method finite specialization, not a creative central
BSD mechanism. The new input is source coverage and a sharper,
independently falsifiable test; no mathematical result beyond the
checked sources is claimed. A protected creative route is not justified
by merely renaming this diagnostic. Mathlib coverage is not checked.

## Search evidence and limits

Discovery queries included `Shimura ordinary Atkin-Lehner adjoint
pairing tower`, `Hida ordinary cohomology adjoint Atkin Lehner Shimura
curves tower pairing U star transition Ohta`, `Shimura curves adjoint
Atkin pairing ordinary`, and `Shimura Atkin-Lehner Rosati ordinary`.
They led to the versioned Krekov primary paper and Maksoud's published
article; the relevant statements and proof cases above were read,
not inferred from abstracts or search snippets. Hida's author
bibliography located the 1988 reference but was not theorem evidence.
Moakher's level-lowering paper, Chida--Hsieh, Disegni and other search
hits were not followed to applicable primary statements and are not
inputs. No absence or novelty conclusion follows from this search.

Targeted local searches found no previous assessment of Krekov,
Maksoud or a p-level adjoint intertwiner in the L128/L129 assessments,
source note and critical drafts inspected. ATTEMPTS/061's tame bad-U
exchange, /062's inverse-action failure and /063's unchanged-pushdown
obstruction remain in force. No mathematical script, new lemma,
PROOF overview, DAG, shared infrastructure or scheduler state changed.

## Step 546 retrieval repair (2026-10-29)

The assessment itself now includes the versioned direct primary URLs.
Reopened the cited Fornea Proposition 2.9 proof cases and Krekov
normalization/projector passages; reopened Maksoud Proposition 6 and
Theorem 8/(13) at the accessible publisher URL
https://link.springer.com/article/10.1007/s40687-026-00598-y.
The DOI-resolver open failed in this tool; the publisher article succeeded.
No scope expansion, new source theorem, mathematical calculation or
change to the existing comparison decision results. Step 545's source
coverage is reused; the completed step is a stalled metadata recovery,
not a repeated mathematical advance.
