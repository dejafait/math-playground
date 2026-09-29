# Resolved-parameter Hilbert-cube deformation — literature assessment

TARGET: Review whether a lift from a smooth resolution of Bl_{J O_S}(S) to S^[3] can deform in the fourth RM direction when both the parameter surface and the map may vary.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched simultaneous deformations of holomorphic maps, deformations of blowups, K3/Hilbert-cube surface maps and RM correspondences; followed the map-deformation and semiregularity references and inspected the primary statements listed below. No inspected statement decides this resolved lift's fourth-direction test.
SOURCE_EVIDENCE: Iacono, arXiv:0705.4532v2 (3 April 2008), Theorems 5.5 and 5.11, Remark 5.12 equation (7), PDF pp. 9,12,14--15, https://arxiv.org/pdf/0705.4532v2#page=9; Ekedahl--Skjelnes, Annals 179 (2014), Proposition 7.27 and Corollary 7.28, printed pp. 835--837, https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=31; Stacks Lemma 31.33.5 (0806), https://stacks.math.columbia.edu/tag/0806; Fantechi, Compositio 98 (1995), introduction and Theorem 0.3, pp. 205--206, https://www.numdam.org/item/CM_1995__98_2_205_0.pdf#page=2; the inspected narrower semiregularity statements and versions are identified below.
COMPARISON: Simultaneous source/target/map deformation is covered by known theory. Central principalization and smoothness of the relative Hilbert cube do not assert smoothness of its map-deformation functor. L009 treats a flat embedded union and L042 the original parameter S; neither covers all maps from a varying resolution B.
GAP: Verify the chosen central B and f, then evaluate the cited tangent map with the target restricted to Hilbert cubes of the prescribed RM deformations, allowing all source motions. The fourth-direction image and subsequent descent to a correspondence on the same deformed S remain unknown.
REASON: Import the general deformation and blowup inputs without reproof and reserve the geometry-specific image calculation for a separate research turn. No essential source for that first-order framework remains unread. Keep the exact saved target; no central lift, transverse family, action or new mathematical exclusion is derived in this review.

## Hypotheses

Retain S, g:S -> S^{(3)}, the actual norm ideal J, and
K=J O_S from L042. B denotes the proposed smooth projective
resolution of Bl_K(S), with p:B -> S. The proposed map
f:B -> X=S^[3] must satisfy rho f=g p on the central fibre.
No choice of resolution, exceptional charts or lifted
family is constructed here. Keep Yoshioka's general-H
hypothesis if translating to stable sheaves.

The target is the fourth direction of the existing
NS-fixed RM deformation space: kappa in V_RM outside V_D.
Allow the abstract parameter surface B and f to vary;
do not require a fixed exceptional configuration or an
unchanged factorization through a relative blowup. The
Hilbert-cube target must be X_A=S_A^[3] for the prescribed
deformation S_A, rather than an arbitrary deformation of X.

The plausible downstream use remains a universal-sheaf
representative with non-scalar action beyond the Dickson
locus. Even a positive map-deformation test would leave
the passage from B_A to the same S_A, correspondence
pushforward and action, higher-order lifting and actual
transverse coverage unresolved. Arbitrary primitive
fourfold classes and the universal Hodge gap also remain.

Rechecked Deligne's [primary rational formulation, section 1,
p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2)
on 2026-10-03. It retains smooth projective complex varieties
and rational linear combinations of algebraic cycle classes,
as in foundations/01. The parameter change does not alter
that target.

## Conclusion

The assessment is ready as SPECIALIZE. It supplies a
known first-order framework for the unchanged target,
not an answer for this f. The next execution of the
target can use the cited criterion rather than repeat
the source search. This is one literature exploration
turn, with no mathematical advance or negative outcome
for the changed parameter source.

The attained span stays 21 on the Dickson family, with
three attained RM directions against four required.
No stable family on B, additional algebraic class,
transverse surface or complete informal candidate is
produced. Originality of a later specialization is not
decided by this bounded review.

## Proof

This section records inspected statements and their scope;
it contains no proof or computation for the proposed lift.

### Central lifting and the relative target

Reuse the [stable-lifting assessment](2026-10-03-degree-three-support-stable-lifts.md)
and reread Ekedahl--Skjelnes, *Recovering the good component
of the Hilbert scheme*, **published version**, Proposition
7.27 and Corollary 7.28 with their proofs,
[printed pp. 835--837, PDF pp. 31--33](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=31).
For a smooth separated relative surface, these assert
smoothness of the relative Hilbert scheme and identify it
with the blowup in the ideal of norms. The scheme structure
of that ideal is retained. These are supporting inputs,
not a deformation theorem for a surface mapping into it.

[Stacks Lemma 31.33.5, Tag 0806](https://stacks.math.columbia.edu/tag/0806),
statement and proof reread on 2026-10-03, supplies the
universal property under the effective-Cartier inverse-image
hypothesis. [Lemma 31.33.2, Tag 0804](https://stacks.math.columbia.edu/tag/0804)
supplies affine Rees-algebra charts. These cover the central
lifting framework after its hypotheses are checked on B;
they give no relative deformation of g or f. Principalizing
K cannot be counted as reaching the fourth RM direction.

Read Fantechi, *Deformation of Hilbert schemes of points on
a surface*, Compositio 98 (1995), 205--217,
[introduction and Theorems 0.1--0.3, pp. 205--206](https://www.numdam.org/item/CM_1995__98_2_205_0.pdf#page=2).
The relative Hilbert scheme gives a natural map from surface
deformations to Hilbert-scheme deformations. Theorem 0.3's
identification requires H^0(O_S(-K_S))=0, which fails for a
K3 surface. Thus unrestricted target deformation cannot
replace deformation induced by S_A. This is a hypothesis
comparison, not a new deformation calculation.

### Simultaneous source, target and map deformation

Read Iacono, *L-infinity Algebras and Deformations of
Holomorphic Maps*, **arXiv:0705.4532v2, 3 April 2008**,
[Definitions 5.1--5.3 and Theorem 5.5, pp. 8--9](https://arxiv.org/pdf/0705.4532v2#page=8),
[Theorem 5.11, p. 12](https://arxiv.org/pdf/0705.4532v2#page=12),
and [Remark 5.12, equation (7), pp. 14--15](https://arxiv.org/pdf/0705.4532v2#page=14).
For a holomorphic map f:B -> X of compact complex manifolds,
both manifolds and f may deform. The cited Dolbeault complex is

\[
\mathcal B_f^q=A^{0,q}(B,T_B)\oplus A^{0,q}(X,T_X)
                  \oplus A^{0,q-1}(B,f^*T_X),
\]

with the differential of Theorem 5.5. Its H^1 parametrizes
first-order deformations; its H^2 contains obstructions.
Equation (7) gives the forgetful-map segment

\[
H^1(\mathcal B_f^\bullet)\longrightarrow
H^1(B,T_B)\oplus H^1(X,T_X)
\xrightarrow{\,df-f^*\,}H^1(B,f^*T_X).
\]

These are imported statements. Their maps are not evaluated
here. Smooth projective B and X meet the compact-manifold
scope once the central lift has been supplied. No immersion
or finite-image hypothesis is required by this framework.

### Stronger-looking deformation results and their limits

Read Iacono, *A semiregularity map annihilating obstructions
to deforming holomorphic maps*, **arXiv:0707.2454v2,
22 June 2010**, [Proposition 4.6, p. 8](https://arxiv.org/pdf/0707.2454v2#page=8)
and [Theorem 4.13 and Corollary 4.14, pp. 11--13](https://arxiv.org/pdf/0707.2454v2#page=11).
These place obstructions in a semiregularity kernel for
**fixed codomain**. They neither compute that kernel here
nor supply the required varying-codomain lift. Vanishing
of a Hodge-theoretic obstruction image is insufficient.

Followed its Ran reference and read Ran, *Hodge theory and
deformations of maps*, Compositio 97 (1995), 309--328,
[section 3, Proposition 3.1 and Corollaries 3.2 and 3.4,
pp. 317--320](https://www.numdam.org/item/CM_1995__97_3_309_0.pdf#page=10).
Corollary 3.2 bounds equations using a contraction-map rank;
no rank for f is given. Corollary 3.4 treats q-Lagrangian
immersions. A surface in the six-dimensional symplectic
Hilbert cube does not meet the half-dimensional condition
of its q=2 case. No other q-Lagrangian structure is supplied.

Reread Nishinou, *Deformation of pairs and semiregularity*,
**arXiv:2009.01651v1, 3 September 2020**,
[introductory hypotheses, Theorem 1 and Definition 5,
pp. 1--3](https://arxiv.org/pdf/2009.01651v1#page=1),
also covered in the [earlier assessment](2026-09-26-current-target.md).
Its relative lifting theorem requires an immersed divisor
image and semiregularity. It does not match the proposed
surface map to a sixfold. The more general definition of
semiregularity is not a theorem removing those hypotheses.

### Geometry-specific continuation test

Let iota(kappa) denote the Kodaira--Spencer class of
S_A^[3] induced by kappa. The proposed specialization of
the quoted exact sequence is to test a pair
(eta,iota(kappa)), with eta ranging over all of H^1(B,T_B).
Seek kappa in V_RM outside V_D whose pair lies in the
kernel of the cited df-f^* map. This only names the input
and test; no value, rank, kernel or new equivalence is proved.

First verify the chosen central lift and the induced target
class. Then retain exceptional loci and all global gluing
data in the test. Setting eta=0 would test a fixed source
and could not stop the target that allows B to vary.

Continue if there is a transverse first-order deformation
under these hypotheses, or an informative bounded calculation
of its remaining obstruction. Stop this specified resolved
lift if all allowed source motions still leave its attainable
RM target classes inside V_D. Failure for one chosen source
motion, or for a more constrained resolution diagram, is
not that stop threshold. Apply the shared three-turn limit.

A positive result still needs a map from B_A to the same
S_A for the intended self-product pushforward; deformation
to a different birational K3 source is not automatically
that identification. Flatness of an embedded image, recovery
of U after subtracting the diagonal, higher orders and
algebraization must be justified separately. No descent,
action equality or embedded lift is asserted in this review.

### Redundancy and source access

Read the full overview, DAG, L042 and L009's hypotheses and
conclusion, the saved placeholder, recent history and stopped
attempt. L009 concerns flat embedded deformations of the
reduced C union Delta in the same deformed self-product;
a varying source map is not such a lift without further work.
L042's noninvertible ideal stops the original S recipe, not
this changed parameter source. The earlier fixed-point and
boundary-contained supplies remain stopped. Repeating their
calculations or proving the general map complex again would
be redundant.

Queries actually used included:

- "deformations of holomorphic maps" "both" Iacono source target
- "deformations" "blow-up" surface morphism varying source target deformation
- K3 Hilbert scheme maps surface deformation semiregularity correspondence real multiplication
- Iacono "L-infinity" "deformations of holomorphic maps" arxiv
- Iacono "Differential graded" "deformations of holomorphic maps" arxiv
- Ran "semiregularity" "maps" deformation
- K3 real multiplication "correspondences" "deformations" Hilbert scheme
- K3 Hilbert scheme symplectic surface "deformations" maps source
- "blowup" "K3" "deformations" "morphism"
- "Deformation of Hilbert schemes of points on a surface" Fantechi numdam
- "K3" "real multiplication" "Hilbert" "deformation" correspondence
- "Hilbert cube" "maps" "deformations" surface

The essential Iacono formulas and relative-Hilbert statements
were readable through the primary PDF text. The version
headers and arXiv histories were inspected. Fantechi's and
Ran's published Numdam copies identify the journal versions.
Some scanned Ran equations were absent from extracted text;
Corollary 3.3's omitted hypothesis is not imported or used.
The readable Corollary 3.4 and the fully readable Iacono
framework suffice for the stated comparison. A local curl
download failed DNS resolution; it did not block web reading.

Iacono's 2007 thesis, original Horikawa/Namba references,
Burns--Wahl and blowup-deformation forum discussions remain
unread leads, not theorem evidence. The Charles--Markman
standard-conjecture and other K3/Hilbert hits were discovery
leads only. None is claimed to resolve this map problem.
The search is bounded, not an exhaustive novelty assessment.

## Mathlib

Coverage: **not checked** for the full resolved-lift target,
the simultaneous deformation complex, its tangent maps or
the supporting Hilbert--Chow and semiregularity results.
The direct links and named theorems above match the identified
framework parts; none matches the computed fourth-direction
answer or a Mathlib theorem. No library absence or progress
beyond the checked literature is claimed.
