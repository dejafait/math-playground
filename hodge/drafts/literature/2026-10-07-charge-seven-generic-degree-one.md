# Conditional charge-seven image — generic-degree source coverage ready

TARGET: Assess whether L064's finite unramified classifying map has generic degree one onto its scheme-theoretic image, using L062's nonzero family two-form.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior local screening; read L064 and relevant L062 material, the family-form assessment, history 129 and ATTEMPTS/041--045; searched finite unramified normal-target covers, K3 image normalization, Mukai coarse-moduli forms and finite-etale Euler multiplicativity; followed primary statements and relevant proofs below.
SOURCE_EVIDENCE: Inspected Stacks 035Q(4), 035S, 0359, 0BQ3, 0GS8--0GS9, 0BQJ's normalization-cover proof, 05B5, 03GN, 0BVH and 02UO; Huybrechts--Lehn (1997) 10.3.3--10.3.5 and 10.4.1--10.4.3, pp. 224--225, 227--228; Debarre (2024-04-15) Proposition 2.5(c), p. 6; Huybrechts's author-hosted K3 draft 15.4.3(ii), p. 330; accessed 2026-10-07.
COMPARISON: Known normalization, normal-target etaleness and coarse-moduli family-form results cover a bounded application followed by the standard Euler test; no inspected source states this full conditional charge-seven conclusion, and no novelty is inferred.
GAP: Apply the cited criteria to the actual normalization factor and compare its Euler characteristic using the pulled-back coarse form; those specialized passages and the generic degree remain unproved in this literature turn.
REASON: Essential coverage missing at startup is now supplied; approve one mathematical specialization next turn and import the general theorems rather than reprove them.
SCOPE: L062--L064's unchanged conditional F on B x Y, the same H-stable numerical-class moduli target and actual reduced image Z; normalization/finite-etale and Euler tests only, with no assumed F existence, image normality, flatness, injectivity, embedding or inverse.

## Proposed threshold and use

The universal primitive Hodge gap remains open. Generic degree one
would constrain reconstruction of the parameter surface from its image.
This completed step supplies source coverage only. It proves no new
lemma and does not compute the degree. The startup REVIEW_REQUIRED
decision is superseded by the inspected comparisons below.

The continuation test is to justify the actual normalization factor's
finite, surjective and unramified properties, meet the normal-target
etaleness hypotheses, and obtain a nonzero two-form by pullback from
the stable coarse space. Then test the degree by the known finite-etale
Euler identity. If an essential bridge fails, retain that precise
failure and abandon this degree argument; do not replace it by assumed
image regularity. Generic degree one still permits identifications over
singular image points and is not an embedding or reconstruction result.

Essential local inputs are L064 (finite unramified maps and reduced
image), L062 (actual nonzero family form), and L063 (actual algebraic
classifying family and one H), carrying L044 and conditional L060.
F existence, inverse/reconstruction and transverse transport remain
unresolved. ATTEMPTS/041--045 and the parked flat-source blocker are
preserved; this does not reopen their stopped index tests. No duplicate
generic-degree result was found in the targeted local material.

## Normalization and the cover theorem

Let W denote the normalization of Z for the proposed application.
[Stacks Lemma 29.55.5(4), Tag 035Q](https://stacks.math.columbia.edu/tag/035Q)
factors a map from a normal scheme when every source component dominates
a target component. Read the statement and the integral-closure proof,
including its reduced-target passage and local fraction-field map.
It does not require the original target to be normal. The next proof
must check irreducibility of the actual reduced Z, dominance and
normality of B before invoking this factorization.

[29.55.11, Tag 035S](https://stacks.math.columbia.edu/tag/035S)
gives finite normalization for Nagata schemes; its proof uses finite
integral closures on affines. [29.18.2(1), Tag 0359](https://stacks.math.columbia.edu/tag/0359)
covers schemes locally of finite type over a field. These apply to the
scope of L064; finiteness of B -> W still needs its own justification.
Reuse the already inspected separated-factor finite criterion 035D and
the differential sequence 01UX with criterion 02G5. Neither the
factor's surjectivity nor its unramifiedness is asserted here.

[37.37.2, Tag 0GS9](https://stacks.math.columbia.edu/tag/0GS9)
requires an integral geometrically unibranch target, a connected source,
a dominating source component and an unramified morphism. It concludes
etaleness. Read its complete proof and the preceding
[37.37.1, Tag 0GS8](https://stacks.math.columbia.edu/tag/0GS8):
the dominant specialization gives an injective local-ring map; the
etale locus contains that component, and connectedness finishes the
global argument. [28.16.2, Tag 0BQ3](https://stacks.math.columbia.edu/tag/0BQ3)
supplies geometric unibranchness from normality. The appropriate
proposed target is W, not Z.

[58.11.1, Tag 0BQJ](https://stacks.math.columbia.edu/tag/0BQJ)
also equates unramified, etale and finite-etale normalization covers of
an integral normal scheme in a finite field extension. Read its direct
proof: after an etale base change the cover splits into closed
immersions; normality and dominance make them isomorphisms. This is
supporting comparison only. Using 0GS9 avoids separately identifying
B as the integral closure in the function-field extension.

[35.14.5, Tag 05B5](https://stacks.math.columbia.edu/tag/05B5)
descends smoothness from a smooth source through a surjective flat
locally finitely presented map. Its proof descends finite presentation,
flatness and smoothness of fibres. [29.42.9, Tag 03GN](https://stacks.math.columbia.edu/tag/03GN)
descends universal closedness through a surjection; a separated locally
finite-type target is then proper. Read the base-change proof. These
cover the proposed smooth/proper normalization passage only after the
factor properties are established. For projective hypotheses, reuse
Z's inclusion in L063's quasi-projective stable target and the inspected
[37.49.1--37.49.2, Tag 0B41](https://stacks.math.columbia.edu/tag/0B41),
including closure under composition and quasi-finite separated maps.

## Coarse two-form and its natural pullback

[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
1997, Lemmas 10.3.3--10.3.4, Definition/Theorem 10.3.5,
pp. 224--225; Proposition 10.4.1, Corollary 10.4.2 and Theorem
10.4.3, pp. 227--228](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=235).
Read the relevant proofs: the family pairing is KS/Yoneda/trace;
tensoring by a parameter bundle scales it by that bundle's rank;
normalization by quasi-universal similitude makes the coarse form
independent of the choice. For a smooth projective surface with
trivial canonical bundle the stable moduli space is smooth symplectic.
This theorem covers the stable locus, without requiring a generic
polarization or a fine moduli space. Restrict to L063's numerical-class
part. Reuse the prior Kuznetsov--Markushevich Theorem 2.2 and family
formula assessment and L064's natural differential bridge.

The next application must compare the coarse form's pullback with
L062's ordered pairing. Only a fixed nonzero scalar is needed; no exact
printed Serre-trace normalization is newly assumed. Pulling the ambient
form along W -> Z -> M is the proposed construction. It does not assume
that a form descends from B to the singular scheme Z.

## Euler comparison and obstruction screening

[Stacks Section 49.3, Tag 0BVH](https://stacks.math.columbia.edu/tag/0BVH)
constructs trace for a finite locally free morphism; its composite with
the unit is multiplication by its locally constant degree. Over C this
covers a normalized trace retraction once finite etaleness is proved.
Its coherent-cohomology application must retain the finite/affine
pushforward comparison; an arbitrary finite unramified map to Z has
not been shown locally free.

Import the named Hirzebruch--Riemann--Roch theorem. Its smooth proper
structure-morphism statement is given in
[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO),
which states the theorem without a proof. For finite-etale Euler
multiplicativity, also read [Debarre, *On rationality problems*,
15 April 2024, proof of Proposition 2.5(c), p. 6](https://perso.imj-prg.fr/olivier-debarre/wp-content/uploads/sites/34/2024/04/On-rationality-problems.pdf#page=6).
That proof explicitly invokes the identity for a connected finite
etale cover. Import only that general identity, not the rationally
connected hypotheses or conclusions of the proposition. The future
test must establish smoothness/properness and compute the target's
coherent invariants from the actual form and trace, without importing
a target K3 classification or assuming its Euler characteristic.

A known obstruction to a degree-one inference from unramifiedness
alone is the K3 cover of an Enriques surface. Read
[Huybrechts, *Lectures on K3 surfaces*, author-hosted prepublication
draft, Section 15.4.3(ii), printed p. 330](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=330):
the fixed-point-free involution quotient is Enriques and has no
holomorphic two-form. Thus a K3 source and a cover criterion alone
cannot supply the proposed degree conclusion; the actual coarse-form
pullback is essential. The source version is this 449-page draft,
not silently the published edition. This is a recorded known example,
not a new counterexample to L064's conditional target.

## Search limits and decision

Queries included `finite unramified dominant morphism normal integral
scheme etale`, `K3 surface finite unramified morphism holomorphic
symplectic image normalization degree one`, `Mukai symplectic form
moduli stable sheaves K3 trace Yoneda`, and `finite etale Euler
characteristic Hirzebruch`. Nonprimary search hits were discovery aids
only; none is used as theorem evidence. No full matching conditional
charge-seven theorem was identified. Coverage supports REPRODUCTION
of the identified specialization, not a claim of originality.

Direct shell PDF retrieval failed with DNS resolution; the browser
provided the needed primary text and the proof passages were read.
No essential source remains blocked and no mathematical script ran.
General normalization, etaleness, moduli-form and HRR theorems should
be cited, not reproved. The needed local work is checking their exact
hypotheses and assembling the conditional degree test next turn.

## Mathlib

Coverage of the full specialized generic-degree statement: **not
checked**. No matching declaration or absence is asserted. Primary
coverage above approves a mathematical attempt; it is not a proof of
the target and not a Lean verification.
