# Finite-point adjoint obstruction component — source-covered test

TARGET: Assess whether L116's actual finite-point projection of the adjoint Yoneda bracket vanishes on its full global section space.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 541 searched derived cup/base-change, relative Yoneda obstruction and K3 split moment-map statements; inspected the primary passages below and compared L094/L109/L111/L115/L116 with ATTEMPTS/016,/069,/089,/090,/091. The finite-point composite is not evaluated in these local results; no inspected theorem directly supplies its vanishing.
SOURCE_EVIDENCE: Inspected live Stacks 36.30.4 (0B91), 20.31.1/3/7/8 (0FKU,0FP6,0H99), including the composition proof and full base-change diagram; Arbarello--Sacca, Advances in Mathematics 329 (2018), Proposition 6.1 and full proof, pp. 680-681, with (5.5), p. 675; Kaledin--Lehn--Sorger math/0504202v1, Section 2.7/(2.3), pp. 5-6. Reuse L094's inspected real-Kahler slice/moment coverage and the saved L109/L111/L116 framework.
COMPARISON: Derived cup compatibility covers a concrete comparison of the actual finite-point projection with the split-fibre quadratic obstruction; no multiplicative Leray splitting or K spectrum is required. Sources identify the obstruction operation, not its value on the full global section image. The real-Kahler case uses L094's existing analytic coverage, not an unverified extension of a polarized moduli theorem.
GAP: In one separate mathematical attempt compare the actual a and j with derived fibre restriction and the trace-free polarized Yoneda obstruction, then test its restriction to the full section image. Ordinary middle base change, annihilation of that image and a bracket value remain unproved; no essential unread source blocks this comparison.
REASON: Approve exactly the unchanged TARGET for one bounded RESEARCH / REPRODUCTION specialization. The available explicit cup/base-change comparison passes the source threshold; approval asserts no vanishing, nonvanishing, exclusion or new lemma. Stop the mathematical test if the comparison leaves an essential section-evaluation pairing uncontrolled.
SCOPE: Exactly L071/L116's common-metric identical marked K3 product and hypothetical locally free Omega-polystable rank-two F with integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P; V=End_0(F), C=Rp_*V, full M_0,W_0, actual j,a and full H=H^0(B,M_0), with t and the finite split set unknown.

LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED and added essential product/base-change and local stabilizer coverage beyond step 540; this separate turn fills that coverage while reusing adequate analytic and linear assessments.

## Proposed map and relevance

The question concerns only the specified composite

    Sym^2 H -> H^2(X,V) -> H^0(B,W_0),
    (u,v) |-> H^2(a)([j_1u,j_1v]).

Here the second arrow is induced by L116's actual truncation projection
after derived global sections. This defines the question; no zero,
nonzero value, comparison formula or new result is asserted.

The main gap is primitive Hodge realization, with even existence of F
unproved. A controlled finite-point obstruction could distinguish
quadratic deformations preserving the split fibres from those detected
there, without knowing K or the remaining component in H^2(X,V).
It supplies no exclusion, section bound, transport or cycle by itself.
The empty split set and t=0 must be retained as vacuous cases.

## Invocation-start approval obligations and stopping test

Read only relevant L094 split stabilizer-pairing and L109/L111 actual
local-complex passages through L116, and search the exact projected
statement, stronger moment-map/base-change results and recorded failures.
L108,L109,L111,L115 remain incorporated through L116; L071 supplies
the connection. Use L163 only as contrast to the abandoned spectral
mechanism. No cross-notebook input is proposed.

In particular distinguish ordinary W_0 from a derived fibre degree-two
space and distinguish L116's zero global transgression from the quadratic
obstruction. A splitting of C as an object is not a Lie or associative
splitting. L111's quadratic condition on the two actual base tangent
directions must not be extended to all global sections without proof.

Continue only if the separate review finds an applicable theorem or a
concrete source-covered comparison for this composite and confirms that
it is not already settled locally. Park it if it needs unknown section
values, an unsupported multiplicative splitting, or the same uncontrolled
global bracket. No new lemma, mathematical script, Mathlib match or
approved mathematical attempt is created here.

## Completed comparison — step 541

2026-10-25. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. The preceding proposal and stopping evidence are
preserved; the completed decision above supersedes its approval gate.
No computation of the composite was performed. Source-coverage progress
is local process progress, not a mathematical advance or a result beyond
the inspected literature. PROOF.md and DAG.md are unchanged.

### Primary statements, proof cases and applicability

1. Stacks, live HTML inspected 2026-10-25:
   [Lemma 36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91).
   Proper finite presentation, flat morphism and perfect coefficient
   imply perfect pushforward commuting with arbitrary base change. Read
   both alternatives and the reduction to Lemma 36.30.1. Here p is the
   smooth projective product projection and V is locally free. This
   covers the derived fibre, without asserting ordinary R^1 base change.

2. Stacks [20.31.1/3, 0FKU](https://stacks.math.columbia.edu/tag/0FKU),
   [20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6), and
   [20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99).
   These identify cup with derived tensor of class maps, compare naive
   and derived cups, and give compatibility with composition and a
   commutative base-change square. Read the adjunction/counit proofs
   and entire square; 20.31.8's proof is explicitly omitted. Apply to
   p followed by global sections and the closed-point fibre square,
   with the coefficient Lie bracket. This is functoriality, not a
   multiplicative splitting of C. Import it without reproof.

3. E. Arbarello and G. Sacca, *Singularities of moduli spaces of sheaves
   on K3 surfaces and Nakajima quiver varieties*, Advances in Mathematics
   **329** (2018), 649-703, DOI 10.1016/j.aim.2018.02.003,
   [Proposition 6.1, pp. 680-681](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=32),
   with the moment map (5.5), p. 675. For a polarized K3 and a direct
   sum of distinct stable factors with multiplicities, equivariant Ext
   identifications carry the quadratic Kuranishi term to the doubled
   quiver moment map. The proof constructs these identifications from
   the stable-factor Ext spaces. Its general scope is explicitly broader
   than the paper's pure-dimension-one main theorem. It does not state
   that all tangent vectors annihilate the quadratic term.

   The fixed h here is real. Do not import this as an exact-h moduli
   chart or silently change h. Use the already assessed analytic input
   in L094 for that hypothesis; the algebraic theorem is the stronger
   related obstruction model, not a theorem evaluating our section image.

4. D. Kaledin, M. Lehn and C. Sorger, *Singular symplectic moduli spaces*,
   [math/0504202v1, 10 April 2005, Section 2.7 and (2.3), pp. 5-6](https://arxiv.org/pdf/math/0504202v1#page=5).
   Read the quadratic term and stable-factor Serre pairing description;
   these express the obstruction using opposite Ext blocks and their
   compositions. The paper's general polarization/Mukai hypotheses are
   not verified for a global application here. Its factoriality and
   resolution theorems are not inputs. The author-hosted PDF returned
   403; the arXiv primary text resolved this nonessential mirror failure.

5. Reuse, without repeating discovery, the inspected primary coverage
   in `2026-10-12-split-equality-tangent-critical-audit.md` and
   `2026-10-14-equality-split-line-analytic-integration.md`.
   Buchdahl--Schumacher, Complex Manifolds **9** (2022), 78-113,
   DOI 10.1515/coma-2021-0131,
   [Lemma 2.5/Proposition 2.6, pp. 83-84, and Corollary 5.3/(5.1), pp. 92-93](https://d-nb.info/1262812674/34),
   treat compact Kahler manifolds and a polystable central bundle at
   the actual real form. L094 already supplies the split stabilizer
   and necessary quadratic ASD term with its Dolbeault comparison.
   That established tangent-plane calculation says nothing about all
   global sections. No exact quadratic ASD chart is needed or imported.

### Duplicate/failure comparison and bounded specialization

L116 proves an additive derived splitting and zero transgression, not
a Lie splitting. L111 computes the ordinary free middle module of rank
50 and the reduced top point term, retaining a derived degree-one fibre
of dimension 52. Its use of L094's two actual base directions cannot
replace the image of the full H in this review. L115 controls the normal
connection and trivial summand; it supplies no computed Yoneda pairing.
These distinctions leave a concrete actual-map specialization to test.

ATTEMPTS/016 concerns different rotation sheaves and transverse lifts.
ATTEMPTS/069 stops an unevaluated scalar cup; /089 is a numerical spectrum
filter; /090 retains compatible quartic cup assignments; /091 records
mixed-power sign cancellation. None evaluates this untwisted finite-point
projection. Step 540's ready formality assessment is reused only for its
scope warning: quadraticity leaves the cohomological bracket unevaluated.
The present test has no eigenspaces or Green-operator input.

Searches included `site.stacks.math.columbia.edu derived base change cup
product cohomology perfect complex`, `site.stacks.math.columbia.edu "cup
product" "base change" derived`, `"relative Yoneda" "base change"`,
`"relative" "Yoneda" "obstruction" "R^2" K3 family`, and K3 polystable
Kuranishi moment-map queries, followed by primary-title retrieval.
Several exact-phrase searches returned irrelevant results, not evidence
of novelty. No inspected exact/stronger result gives the target value.

The next attempt must compare actual arrows, retain the full section
image and trace-free polarization, and distinguish top degree base
change from invalid middle degree base change. It may establish a
comparison before deciding whether vanishing follows. Do not assume
that a section is an integrable deformation, or that L094's KS-plane
condition holds on H. If section-image pairings remain essential and
uncontrolled, record that precise obstruction and park this mechanism;
do not prolong it by invoking formality again. Empty W_0 and t=0 are
vacuous, and a controlled point projection would still leave the other
global obstruction component, F existence and Hodge realization open.
Full matching Mathlib coverage was not checked; no absence is claimed.
