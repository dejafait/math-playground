# Global opposite Hom Euler-count test — bounded source coverage

TARGET: Test whether the global relative Hom Euler identity yields a finite upper bound on L121's ordered off-diagonal coincidence count.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed targeted relative-Ext/diagonal/Euler and modular-sheaf stability searches; compared L135, L118/L121, the prior Hom and opposite-character assessments and ATTEMPTS/046, 073. Inspected primary Markman diagonal and modular-stability statements and the relevant base-change, duality, spectral-sequence and absolute-HRR sources below; no applicable count inequality was found in these inspected results.
SOURCE_EVIDENCE: Markman math/0009109v4 Theorem 1, Remark 3(2), proof through (11), Lemma 4 and Section 3 opening, printed pp. 2–6,12; Markman 1608.05798v1 Section 1.1, Theorem 1.2, Section 1.2, Assumption 1.3 and Theorem 1.4, pp. 1–3; live Stacks 0B91, 0G81, 0FLJ Lemma 20.29.1/Example 20.29.3 and 02UO. Reuse the saved local coefficient/minimal-complex and full-character coverage cited below.
COMPARISON: The universal diagonal theorem has incompatible rank/codimension hypotheses here, and universal modular stability supplies no pullback or Euler-sign theorem for this ordinary middle sheaf. General perfectness, hypercohomology and absolute HRR cover a bounded sufficiency test retaining all ordinary cohomology sheaves; local L135 multiplicities alone give no count inequality.
GAP: A later mathematical attempt must identify the actual diagonal top-sheaf data, evaluate the whole coefficient Euler index and determine whether justified middle-sheaf constraints bound the off-diagonal length. No diagonal identification, specialized numerical identity, sign, inequality or count bound is established in this literature turn.
REASON: Approve only the concrete bounded test below using known tools, classified REPRODUCTION; if the identity leaves an uncontrolled middle Euler term, park this index mechanism. This is coverage for testing sufficiency, not approval of a missing positivity assertion.
LITERATURE_REASON: Changed global scope introduces the diagonal component and uncontrolled middle-sheaf Euler contribution, outside the ready local-stalk assessment.
SCOPE: Exact L071/L118 equality-kernel hypotheses, the actual two-family full Hom complex on B times B from L135, diagonal included; L120/L121 finite normalization and reduced ordered off-diagonal coincidences; no ordinary Ext-sheaf pullback, IT, image-cohomology vanishing or middle-sheaf stability is assumed.

The main gap remains universal primitive rational Hodge realization.
The intermediate target is a useful finite upper bound on the number N
of ordered distinct pairs with isomorphic opposite fibres, using the
actual global relative Hom complex of L135. Such a bound could combine
with local normalization-defect controls in a future global comparison;
neither that comparison nor an exclusion of F is known. This registration
does not assert an Euler formula, a decomposition of the top sheaf, or
a sign for any term.

Retain L071's full equality-kernel hypotheses, L118's all-stable actual
opposite family, L120's finite normalization map, L121's finite reduced
coincidence locus, and audited L135's length-one off-diagonal stalks.
F is a hypothetical locally free Omega-polystable rank-two bundle with
integral c_1=0 and ch_2=-14e_1-21e_2-tau_D on the identical marked K3
factors. The off-diagonal locus may be empty. The global test must treat
the entire B times B, including its diagonal; L135 alone identifies
neither the diagonal stalks nor their global line-bundle data.

The source comparison authorizes one later bounded mathematical test of
whether the whole identity and its justified constraints suffice. It
does not authorize a new positivity theorem, an unassessed singular
instanton extension theorem, or a search for arbitrary higher corrections.
If the identity merely trades N for an uncontrolled Euler characteristic,
record that failure and park this index mechanism. No new lemma or
mathematical script is written in this literature turn.

ATTEMPTS/046 rules out interpreting injective Hom first variation as
separation. ATTEMPTS/073 parks automatic H^1(O_Z) vanishing for the
singular image; this proposed test does not assume or rederive that
vanishing. Preserve ATTEMPTS/061--063 and the parked order-five evidence.
The global coefficient-index test is a distinct proposed mechanism,
not a reopening of those conclusions under a new name. Full matching
Mathlib coverage is not checked, rather than asserted absent.

## Primary theorem comparison

[Markman, *Generators of the cohomology ring of moduli spaces of sheaves
on symplectic surfaces*, J. reine angew. Math. 544 (2002), 61–82,
math/0009109v4, 21 April 2001](https://arxiv.org/pdf/math/0009109v4),
Theorem 1, pp. 2–3, identifies the full moduli diagonal by the degree-m
Chern class of minus the relative Ext class, where m=dim M; completeness
is unnecessary. Remark 3(2) states that relative Ext^2 is a line bundle
on that diagonal. The proof through (11), pp. 4–6, retains Ext^1 and
warns that the terminal degeneracy map is not regular. Lemma 4 requires
smooth support of pure codimension m, both terminal cokernels line
bundles there, and alternating middle rank m-2. Section 3, p. 12,
uses local universal families when a global one is absent.

For comparison, L135 already records generic middle rank 76, and L121
places both tangents in moduli dimension 78. The present parameter is
B times B, of dimension four, with the diagonal of codimension two and
possible isolated off-diagonal support. Those are not Lemma 4's pure
support and rank hypotheses. Substituting parameter dimension for m
would change the theorem. Its universal Chern-class formula is not a
degree-four count formula for this family. This is a source-applicability
comparison, not an evaluation of any pulled-back Chern class.

The additional primary lead was
[Markman, *Naturality of the hyperholomorphic sheaf over the cartesian
square of a manifold of K3^[n]-type*, 1608.05798v1, submitted
20 August 2016](https://arxiv.org/pdf/1608.05798v1), Section 1.1 and
Theorem 1.2, pp. 1–2. It assumes a primitive Mukai vector and a smooth
compact stable moduli space of dimension 2n>=4, and proves stability of
its rank-(2n-2) reflexive relative Ext^1 sheaf for every product Kähler
class. Section 1.2, Assumption 1.3/Theorem 1.4, pp. 2–3, requires the
specified locally free transform on the diagonal blowup, with exceptional
restriction ell-perp/ell, on an irreducible holomorphic symplectic X of
dimension greater than two. These statements were read in full; their
long proofs are unnecessary for rejecting a hypothesis mismatch.

Here B is a K3 surface of dimension two, not that full moduli space;
the actual ordinary middle sheaf has not been identified with an
ordinary pullback of the universal one, and L118 does not assert a
compact ambient stable space. Neither theorem states preservation of
stability under this family map or an upper bound for the ordinary
middle-sheaf Euler characteristic. No such conclusion is imported.
This stronger lead therefore does not repair the missing count inequality.

## Applicable general tools and the approved bounded test

Reuse the coefficient, minimal-complex, stable-Hom and reverse-Serre
coverage in `2026-10-20-opposite-off-diagonal-relative-hom-stalk.md` and
`2026-10-20-opposite-hom-stalk-critical-audit.md`. The actual algebraic
families and tangent conclusions are in L118/L121; the complete L135
definition, support and minimal-presentation passages were inspected.
This changes global scope but no coefficient hypotheses.

[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91)
assumes a proper flat morphism of finite presentation and perfect
coefficient; perfect pushforward and arbitrary derived base change
apply. Its statement and reduction proof were read. Here the projection
from Y times B times B has those properties and the Hom coefficient
is locally free. Derived base change is available; ordinary middle-sheaf
base change is not a consequence. If local universal charts are used,
the last-row cokernel and base-line twists must be checked explicitly.

[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81),
statement and trace-adjunction proof read, supplies perfect derived
duality from a perfect coefficient pairing to the relative dualizing
complex. Here use forward and reverse full Hom and the chosen fibre
two-form, with relative dimension two. It does not identify the middle
sheaf with its ordinary dual through its singular support.

[Stacks 20.29, Lemma 20.29.1 and Example 20.29.3,
0FLJ](https://stacks.math.columbia.edu/tag/0FLJ), including the filtered
injective proof and bounded-below case, gives

    E_2^(i,j)=H^i(T,H^j(K)) => H^(i+j)(T,K).

For bounded coherent K on proper T its terms are finite-dimensional
and finite in the relevant range, so the standard alternating Euler
identity retains every H^j(K). No degeneration is required. This is
the imported general identity; its specialized terms are not evaluated
here. The spectral sequence supplies no positivity for an Euler sum.

[Stacks 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO)
states absolute HRR for a finite locally free coefficient on a smooth
proper variety. Use the absolute form on the smooth projective
sixfold Y times B times B. This avoids the page's locally-free-higher-
images hypothesis in its restricted relative formulation. For full
GRR and Chern bookkeeping reuse the inspected Fulton, *Intersection
Theory*, second edition (1998), Theorem 15.2, pp. 286–287 and Example
15.2.8, pp. 291–292, as recorded in
`2026-10-17-opposite-global-normal-character.md`; do not reprove HRR.
L071's rank-two full-character inputs, not just the fibre Euler -76,
are required for any ensuing absolute evaluation.

One later RESEARCH / REPRODUCTION attempt is covered, with this exact
TARGET unchanged:

1. Work with L135's K on all of T. Prove the actual ordinary H^0
   assertion, and identify the entire diagonal part of H^2 including
   its coefficient line and any thickness. Use actual identity/trace,
   a justified top-degree base-change comparison or the already
   assessed two-family coefficient mechanism. A one-dimensional
   derived top fibre is not a diagonal sheaf calculation. Keep L135's
   off-diagonal multiplicities and the possibility N=0.
2. Evaluate the absolute coefficient Euler integral using the full
   rank-two character, both parameter Todd factors and fibre Todd
   factor. Then apply the general Euler identity above, retaining the
   ordinary M=H^1(K). No numerical index is supplied by this review.
3. Isolate exactly what upper control on the remaining middle-sheaf
   Euler contribution would yield a bound for N. Test only constraints
   justified by the imported spectral sequence, reverse derived duality
   and existing local data. If they do not give that control, state
   the uncontrolled term and park this route. A formal compatibility
   test may disprove sufficiency of those constraints, but realizes
   neither M nor F. Stop rather than append an unassessed sheaf
   stability, singular metric extension or vanishing assertion.

This is an evaluable bounded sufficiency test rather than a promised
inequality. An obstruction in the actual diagonal comparison is also
a stopping result; do not replace it by the desired diagonal model.
No new lemma, family specialization, numerical integral or mathematical
script has been derived in this review. Conditional existence of F,
collision existence, useful normalization-defect comparison and
transverse transport remain independent gaps.

## Discovery, overlap and source limitations

Queries included `Markman generators cohomology ring moduli sheaves
symplectic surfaces Ext diagonal 0009109 Euler characteristic`,
`K3 stable sheaves relative Ext sheaf diagonal pullback immersion self
intersection Euler coincidence count bound`, `Markman modular sheaf
Ext1 reflexive hyperholomorphic stable diagonal K3 moduli sheaves`,
`hyperholomorphic higher direct images cohomology jumping index theorem
quaternionic instanton IT condition relative Ext`, `"relative Ext"
"Euler characteristic" "self-intersection" K3`, and Stacks searches
for the Euler spectral sequence and HRR. Search snippets and nonprimary
aggregators were discovery only. No absence or novelty claim follows.

The saved `2026-10-08-sign-reversed-six-charge-preservation.md` provides
the inspected Bartocci–Bruzzo–Hernandez Ruiperez Theorem 3 and its IT
hypotheses. That bundle-preservation theorem cannot be assumed for
this jumping full Hom coefficient: L135 records endpoint Ext on the
diagonal. No fresh transform theorem is needed for the bounded test.
The previously unread Mukai Proposition 4.10 lead remains unimported;
the approved method does not require its special relative-Ext vanishing.

The earlier Hom assessment already excluded using the parameter
dimension in Markman's full-moduli theorem. The new comparison retains
that failure, adds the stronger modular-stability lead and completes
the global Euler/diagonal/middle-sheaf source scope. It does not repeat
L066's first-order separation test, nor assume ATTEMPTS/073's stopped
H^1(O_Z) vanishing. The source result is LITERATURE / EXPLORATION /
NOVELTY_UNCHECKED: coverage is ready for one known-tool sufficiency
test, but no count bound or mathematical advance has been established.
