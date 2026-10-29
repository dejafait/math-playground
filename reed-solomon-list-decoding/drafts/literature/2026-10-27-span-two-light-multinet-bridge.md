# Coefficient-span-two light-multinet bridge — proposed bounded target

TARGET: Test whether every nonconstant coefficient-span-two assignment on the pinned full affine sheet admits three complete direction classes whose dual evaluation-line maps are injective with pairwise-disjoint images, retaining all exceptional roots and coincident-line cases.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed quadratic-cone review records bounded searches for weak plane-net embeddings, light dual multinets, noninjective multinets and quadratic-polynomial nets; it reuses the earlier signed/common-root assessment and checks ATTEMPTS/031–032,109. No inspected statement supplies this exact collision-aware bridge; absence from this search does not establish novelty.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-10-27-quadratic-cone-sheet-rigidity.md for newly inspected Korchmaros–Nagy arXiv:1710.00172v1 Definition 2.1, Lemmas 2.2/2.4/2.5 and Proposition 4.5 with its distinctness argument; Bogya–Nagy arXiv:1810.00416v1 Introduction/Definition 5.1. Reuse drafts/literature/2026-10-27-affine-sheet-common-center-collapse.md for the signed/common-root inputs. No unread dual-net classification is an input to this bridge test.
COMPARISON: Light multinets permit extra incidences but require injective component maps, and the source introduction requires disjoint component images; weak embeddings remain injective and spanning. These are conditional geometric definitions/results, not the missing assertion for coefficient-span-two assignments. The bridge may fail through undefined or coincident restricted evaluation lines and must not be assumed.
GAP: Establish the stated three-complete-class bridge, prove that the relevant nonconstant span-two assignments cannot exist, or give an exact permitted nonconstant span-two assignment for which no such triple works. The coefficient-span-three rank problem and all retention/global-transfer gaps remain independent.
REASON: This target uses the newly inspected distinction between extra incidences and component collisions to isolate an independently testable two-dimensional obstruction; it does not repeat the parked universal residual-rank attack. A separate next-turn approval is required for this newly written assessment.
SCOPE: Only q=137, T={16,64,70,102,112,118,121}, E=F_65537, F=F_(65537^28), H=<19139> of order 1024, k=64, arbitrary actual 61-core C and bijection in L030; K=E or F, repeated messages allowed, coefficient-difference span exactly two. No deletion theorem, ordinary-net embedding, rank computation, numerical sample or RS-list bound is preapproved.

## Exact setup and intended test

Use L030 and the signed/common-root methods in L031/L047/L049, together
with the saved setup in `drafts/2026-10-27-affine-sheet-collapse-working.md`.
Its (W1)–(W5) are working reasoning, not audited canonical rank results.
For P=(u,v) in F_137², let g_P in K[X] have degree at most two, with
g_P(x_(t,y)) constant as P ranges over u+tv=y. All 959 actual labels
x_(t,y) in H minus C are pairwise distinct. Do not identify F_137 with
a subfield of K. The span in this target is
V=span_K{g_P-g_(0,0):P in F_137²}, of dimension exactly two.

The proposed objects are the level sets of evaluation at each actual
label, restricted to the affine coefficient plane g_(0,0)+V. Before
dualizing any such set, verify that it is a genuine affine line. An
identically zero restricted evaluation, coincident level sets, parallel
lines, repeated g_P and coincidences across direction classes all remain
cases to address. Selecting three **complete** direction classes must
not silently delete exceptional lines or labels. No injectivity,
separation, spanning, faithful translation action or group labeling is
already proved. If invoking a group-labeled definition later, explicitly
verify the auxiliary isotopy and all of its geometric hypotheses.

The source comparison is canonical in the preceding cone assessment.
The exact primary links are
[Korchmaros–Nagy v1](https://arxiv.org/pdf/1710.00172v1) and
[Bogya–Nagy v1](https://arxiv.org/pdf/1810.00416v1).
Their full classification is not needed to test this bridge, and no
classification specialization is approved here. Ordinary signed
equalities and the polynomial factor theorem are covered by the reused
full-sheet assessment; any reproof should be limited to the missing
degeneracy/selection argument.

## Relevance, duplicates and stopping test

The main unresolved claim is arbitrary-center 67/68 agreement safety.
This intermediate target could remove one obstruction in the span-two
case of full-sheet collapse by making a conditional light-multinet
comparison legitimate. It leaves span three, the threshold 1532496,
compatible laws and RS transfer unresolved. Even successful full-sheet
collapse would not imply a retained-family cap.

ATTEMPTS/109 remains the stop evidence for direct all-label rank.
The new test concerns collisions in restricted evaluation lines, not a
claim that additional incidences disappear. ATTEMPTS/031–032 show why
excluding full sheets alone cannot yield the cap; ATTEMPTS/106–108 remain
limitations of different overlap/translation routes. L031's realizable
four-support pattern does not refute or prove this full-sheet assertion.
No existing local proof was found for the precise bridge in the scoped
prior records; this is not a claim of global originality.

Continue only if the bounded attempt establishes the bridge for every
permitted labeling (including all exceptional evaluations), excludes
the entire nonconstant span-two case, or produces the exact permitted
obstruction specified above. A generic-label proof, an injectivity
assumption, an arbitrary geometric example without the actual H labels,
or success on a single sampled labeling does not pass. If degeneracies
remain, save the precise unresolved case and reassess rather than
repeating the universal matrix attack. A counterexample to the bridge
is not a counterexample to the RS target.

Mathlib full/supporting coverage is not checked. There is no
cross-notebook input, new lemma, mathematical script or candidate
solution. This assessment was written during a literature-only step;
the supervisor must approve it separately before the proposed research.
