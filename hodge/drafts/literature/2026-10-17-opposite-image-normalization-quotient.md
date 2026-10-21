# Opposite image normalization quotient — completed source comparison

TARGET: Assess whether L121's reduced image has normalization quotient of length r_m-1 at each r_m-branch collision, retaining possible linear dependence among three or more tangent lines.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the opposite point-separation comparison, read L121 and L120's exact hypotheses/conclusion, checked ATTEMPTS/046 and searched seminormal/multicross in local assessments, attempts and history; searched primary normalization, seminormal union and isolated-nonnormal delta results, with statements and relevant proofs inspected below.
SOURCE_EVIDENCE: Leahy--Vitulli, Nagoya Math. J. 82 (1981), Theorem 2.2 and Propositions 2.18--2.23, pp. 40--41, 46--50; their Nagoya Math. J. 83 (1981), Lemma 3.4, sequence (3.3) and Theorem 3.5 with proofs, pp. 140--144; Vitulli's 1987 correction, pp. 148--149, 157; Verbitsky alg-geom/9703016v1, Theorem 4.7 and normalization proof; Greuel--Pfister (2022), Definition 6 and Lemma 10.
COMPARISON: Known criteria require simultaneous gluing, equivalently the stated weak-normality condition in the regular-branch setting; their printed quotient sequence covers that case. L121 records pairwise tangent disjointness only. No inspected theorem removes the simultaneous condition or supplies length r_m-1 for the actual conditional image.
GAP: Actual image weak normality/seminormality and its normalization quotient remain unproved; the tangent test is against the preceding union, not just individual branches. No failure of the formula for the full F hypotheses is established.
REASON: Park automatic minimal defect from reduced pairwise coincidences. The known criteria cover a bounded local-model specialization testing this inference; a separate ready continuation records exactly that test, without deriving it here.
SCOPE: Unchanged conditional rank-two locally free Omega-polystable F of L118/L120/L121, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D, identical marked metrics/triples, B=S_1 and Y=S_2; only the normalization quotient at an actual image collision.

## Decision and relevance

The main gap is universal primitive rational Hodge realization. The
intermediate target was the exact local length r_m-1 for Q at every actual
collision, including all multiple collisions. Such a defect could later
enter coherent cohomology; this review supplies no global constraint.
The threshold is not established. The new source-scope evidence changes
the route: retain the simultaneous-gluing condition instead of importing
the proposed formula from L121. This is NEGATIVE / LITERATURE /
REPRODUCTION, a comparison with known results, not new mathematics.

## Primary statements and proof cases read

[Leahy--Vitulli, *Seminormal rings and weakly normal varieties*,
Nagoya Math. J. 82 (1981), 27--56](https://doi.org/10.1017/S0027763000019279),
Theorem 2.2, pp. 40--41, identifies relative seminormalization for a finite
integral extension of reduced affine rings over an algebraically closed
characteristic-zero field with functions constant on every fibre. Its
proof checks all primes and residue fields, not just closed-point
bijectivity. Proposition 2.23, pp. 49--50, assumes subvarieties X_i with
common set-theoretic pairwise intersection Y, weakly normal Y, and, in
part (2), smooth Y. Weak normality of the union requires weak normality
of each X_i and

\[
 T_{X_i,y}\cap T_{X_1\cup\cdots\cup X_{i-1},y}=T_{Y,y}
 \quad(i=2,\ldots,n).
\]

Read the complete ideal/Mayer--Vietoris argument in Propositions
2.18--2.23, pp. 46--50: the preceding union is essential. This does not
state a pairwise-tangent criterion. Their terminology identifies weak
normality with seminormality in this characteristic-zero setting.

[Leahy--Vitulli, *Weakly normal varieties: The multicross singularity
and some vanishing theorems on local cohomology*, Nagoya Math. J. 83
(1981), 137--152](https://doi.org/10.1017/S0027763000019450), Lemma 3.4,
pp. 141--143, uses the completed local ring R, minimal primes P_i,
regular R/P_i, common prime radical sqrt(P_i+P_j)=P, and regular R/P.
It equates weak normality, the multicross property, and the simultaneous
identities P_i+intersection_{j!=i} P_j=P. Read its conductor argument
and the entire completed-kernel construction. Under these conditions
the printed sequence (3.3) is

\[
 0\longrightarrow R\longrightarrow\prod_{i=1}^{r}R/P_i
 \longrightarrow\prod_{i=1}^{r-1}R/P\longrightarrow0,
\]

where the last map takes differences with the first branch. It supplies
the sought quotient for a multicross with point intersection; it does
not grant its hypotheses for Z. Theorem 3.5, pp. 143--144, requires smooth
normalization above the point, smooth nonnormal locus with etale inverse
image, unramified normalization, **and weak normality at the point**.
Read the full converse through the conductor and completed minimal
primes. The last condition is not discarded.

[Vitulli, *Corrections to “Seminormal rings and weakly normal
varieties”*, Nagoya Math. J. 107 (1987), 147--157](https://doi.org/10.1017/S0027763000002592),
pp. 148--149, preserves the fibre-constant description of seminormalization.
The original Zariski-continuity definition of c-regularity is insufficient;
it is not used here. Page 157 explicitly retains the original paper's
results following the incorrect Proposition 2.14, covering the union
criteria used above. This correction was checked rather than assuming
the old function-theoretic definition.

[Verbitsky, *Hypercomplex varieties*, alg-geom/9703016v1,
12 March 1997](https://arxiv.org/pdf/alg-geom/9703016v1#page=19),
Theorem 4.7 (printed p. 19), describes quaternionic linear components of
the reduced tangent cone. Proposition 6.1 and Theorem 6.2, printed
pp. 26--27, give smooth normalization with compatible hypercomplex
structure. Their inspected proof separates smooth local components and
glues structures on their disjoint union. It neither asserts simultaneous
tangent independence nor identifies the original local ring with a
residue-field gluing. The earlier point-separation assessment is reused;
no intrinsic hypercomplex structure on the actual algebraic Z is proved
or assumed during this comparison.

[Greuel--Pfister, *The delta invariant and fiberwise normalization for
families of isolated non-normal singularities*, Journal of Singularities
25 (2022), 173--196](https://www.journalofsing.org/volume25/greuel-pfister.pdf),
Definition 6 and Remark 7, pp. 176--177, identify delta with the
normalization-quotient dimension for a reduced positive-dimensional
local ring. Lemma 10, p. 178, proves finiteness for finite normalization
with an isolated nonnormal point and finite residue field over the base.
Read its support/Artinian proof. This is terminology and finiteness
coverage, not a value determined by branch count.

## Comparison, duplicates and bounded continuation

L118/L120/L121 retain smooth local immersed branches, finite unramified
birational normalization and finite reduced off-diagonal coincidences.
They do not assert the simultaneous ideal identities or tangent condition
in the union criterion. Smooth normalization alone is consequently not
an applicability check for the quoted sequence. This identifies a precise
missing condition; it proves neither that it holds nor that it fails for
the actual image. No new local algebra computation is made here.

The notebook search `seminormal|multicross|simultaneous (branch )?gluing`
in drafts/literature, ATTEMPTS and history found no earlier seminormality
assessment or matching quotient computation. The older support gluing
calculations concern a different support and are not imported.
ATTEMPTS/046's Hom-jump limitation and the opposite point-separation
assessment remain in force. The present source comparison does not
reopen either stopped mechanism.

External queries included `seminormal isolated nonnormal singularity
normalization functions equal residue fields multiple branches quotient`,
`seminormality arrangement linear subspaces tangent spaces independent`,
`Seminormality of unions of planes`, and `Leahy Vitulli multicross`.
Dayton--Roberts' chapter *Seminormality of unions of planes* and
Yuzvinsky's subspace-arrangement work remain unread leads, not inputs.
The primary texts above supply the essential coverage. A PDF-screenshot
timeout and failed shell download did not block reading the relevant
primary text and complete proof cases through the web tool. No novelty
is inferred from search results. Full matching Mathlib coverage is not
checked.

The separately scoped [three-line continuation](2026-10-17-three-quaternionic-lines-gluing-test.md)
proposes an independently testable flat model to distinguish pairwise
from simultaneous gluing. Its source criteria are ready, subject to the
supervisor's separate next-turn approval. It calculates no actual F
invariant and gives no global nonexistence implication. Continue only
with a complete local-ring/normalization comparison; abandon this model
as evidence if it fails the retained local geometric conditions. Even a
successful model test would leave actual image gluing unresolved.

## Initial proposal retained (superseded as routing)

Use nu:B -> Z for L120's normalization of the integral reduced image.
For a closed image point m, let r_m count the distinct points of
nu^{-1}(m). The proposed object is Q=nu_*O_B/O_Z. Review whether its
stalk has complex length r_m-1 under these exact geometric hypotheses.
This specifies a threshold to investigate, not an assertion about Q.

The main gap remains universal primitive Hodge realization. The plausible
downstream use is to translate residual identifications into a local
normalization defect that could later enter global coherent cohomology.
No global cohomological constraint on Z or exclusion follows from this
proposal; F existence and transverse transport remain open.

Inspect primary results on normalization quotients and several smooth
branches meeting in isolated points. Compare any required seminormality,
tangent-independence or local-ring hypotheses. The previously inspected
Verbitsky, *Hypercomplex varieties*, alg-geom/9703016v1, Theorem 4.7 and
Proposition 6.1/Theorem 6.2, is a named lead on branch structure, not a
quotient-length theorem imported here. Assess applicability to the actual
algebraic image; retrieve relevant statements and proof cases before
broader passages.

L121 does not prove joint linear independence of three or more tangent
lines or prescribe the image's completed local ring. Keep those fibres
in scope. Distinguish a reduced pairwise intersection from simultaneous
gluing of every branch. A generic local model without the full F
hypotheses could refute an inference from local data, but would not
refute existence of this F.

Continue only if primary coverage yields an applicable formula or a
concrete separately assessable missing local condition. If the formula
needs unsupported independence or gluing, record that obstruction and
park it; do not assume binary collisions or identify a model with the
actual image. No local calculation, new lemma or mathematical script is
authorized by this REVIEW_REQUIRED proposal. Mathlib coverage is not
checked.
