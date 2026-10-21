# Canonical global class against five/eleven filters — coverage ready

TARGET: Test whether the canonical fiber at j=9261/8 supplies one global K(S,5) class satisfying L061's five-adic class list and L044's eleven-adic valuation filter simultaneously.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched canonical fiber X0(11), 54a1 five-isogeny class, 9261/8 descent, Schaefer–Stoll Proposition 4.6 and global/local localization; inspected primary sources below and compared L033–L034, L036, L041, L044–L045, L047, L061 and ATTEMPTS/013,025–028. No inspected source states this combined local-filter test; this is not a novelty claim.
SOURCE_EVIDENCE: Rechecked FNS June 10, 2019 manuscript Section 7.2 pp.25–27, entire-fiber paragraph, model, Table 5 and (7.4); Schaefer–Stoll June 13, 2001 manuscript Lemmas 4.3–4.5/Proposition 4.6 pp.6–7, Section 5 pp.8–9 including the localization diagram, and Section 9 opening pp.21–22; Stacks Lemma 26.17.2/tag 01JQ with tensor-product proof. Reused the ready audited local interfaces.
COMPARISON: Sources cover unconditional canonical-fiber data and restriction of one global connecting class; audited local results cover complete membership and valuation filters. Their bounded same-point application remains to be written, and no exact combined witness was found in the inspected records.
GAP: No essential source gap remains for this bounded test; verify the scalar hypotheses, specify a single global point/class intrinsically or in exact coordinates, and carry its fixed identification to both whole local algebras. Full eleven-adic units and integer lifting are outside coverage.
REASON: Approve one REPRODUCTION application of known inputs, distinct from exhausted generator searches; a witness could retire emptiness of this necessary intersection without a complete class/unit basis. Approval concerns coverage, not a proved witness.
SCOPE: Exactly TARGET, including an intrinsic fiber-field witness and theorem-based membership certificate; no full eleven-adic unit image, all-place intersection, class-group computation, rational power lifting or integer solution.
LITERATURE_REASON: Changed global same-class scope required the separate comparison now completed, especially Section 5's commutative restriction diagram; unchanged local coverage was reused.

## Relevance and scope comparison

The main gap is an unconditional global emptiness argument for ordered
(3,4,11), including the 54a1 branch, within the much larger unresolved
Beal target. The intermediate target is one certified global class in
the intersection of the named necessary filters. Nonemptiness would
decide whether these two filters alone can supply that emptiness test;
it would not provide a positive primitive integer solution.

L047 already identifies the rational canonical scalar and entire fiber,
but its proved power witnesses are three-adic. L033's group-containment
argument applies to every E0(K)-point, whereas its transported-solution
conclusion assumes an integer solution. Reuse the former without assuming
the latter. L061's exact list and L044's vector image are audited in
their canonical files; their pending-audit wording in the supplied
overview does not override those completed audits. L045's unevaluated
ideal criterion supplies context, not an extra premise.

The finite boxes in ATTEMPTS/013 and the prescribed principal/mixed
lists in ATTEMPTS/027–028 cannot disprove a fiber-based witness.
ATTEMPTS/025–026 retain their implementation/source limitations; this
application need not invoke their ideal backend. Preserve those stops.
No matching global witness is established by the inspected local proofs.

## Primary source statements and applicability

Freitas, Naskręcki and Stoll, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019, Section 7.2, pp.25–27: the fiber at the canonical j(E)
is the twelve-subgroup Galois set, irreducible of degree twelve for the
five listed curves. The 54a1 polynomial in Table 5 matches L033.
The GRH premise enters the separate Selmer computation. Import the
field identification; do not import the adjacent Selmer dimension or
conditional classification. No new coordinate conversion is supplied
by this review.

Schaefer and Stoll, *How to do a p-descent on an elliptic curve*,
Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
June 13, 2001, Proposition 4.6, p.7: S contains primes above p and
places where either Tamagawa number is divisible by p. Lemmas 4.3–4.5
handle the unramified local images away from p. Section 5, pp.8–9,
requires global/local cohomology injectivity and a known cohomological
image; good-divisor evaluation then realizes the connecting map. Its
displayed restriction diagram commutes. L033 verifies these requirements
for the dual toward E0, with p=5 and singleton {T}; both discriminants
are supported at eleven, so its S includes all required places.
The general diagram covers one class at every completion without a
global-point/Selmer equality. Section 9, pp.21–22, distinguishes that
equality's additional Sha hypotheses. Reuse the normalized f and all
exceptional evaluations; no general descent reproof is justified.

[Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ),
live version inspected 2026-10-12: for affine X=Spec(A), Y=Spec(B) and
S=Spec(R), the fiber product is Spec(A tensor_R B). The full proof
was read. It covers both completions of the same finite rational fiber;
use its universal maps with a fixed rational field identification.

The precise target formulation was rechecked on
[Mauldin's primary page](https://sites.math.unt.edu/~mauldin/beal.html):
positive integer bases/exponents, exponents greater than two, and a
prime common to all bases. No revision date was identified. The nominated
AMS page again failed retrieval; its contents and prize administration
are not claimed checked. This unchanged statement check does not block
the independent mathematical application.

## Search evidence and limits

Queries included `"Freitas" "Naskręcki" "Stoll" "canonical" fiber 11 54a1`,
`"Schaefer" "Stoll" "Proposition 4.6" p descent`,
`"9261/8" "X0(11)" descent`, `"54a1" "X0(11)" "5" descent`,
`"How to do a p-descent" "local" "global" isogeny natural`,
`"54a1" "5-isogeny" "class"`, `"canonical fiber" "X0(11)" "descent"`,
and `"Schaefer" "Stoll" "5-descent" "localization"`.
Direct primary passages, rather than snippets, supply the imports.
The searches distinguish the conductor-54 curve from the conductor-11
modular curve carrying the five-isogeny. They establish no originality.

*Local points on twists of X(p)*, arXiv:2509.04294, and
*Revisiting the equation x^2+y^3=z^p*, arXiv:2512.10781, remain
unread theorem leads; neither is an input. Existing canonical-fiber and
local-domain coverage suffices for this unchanged bounded application.
No new claim about those papers is used.

## Approved application and stopping test

Use L033, L034, L036, L041, L044, L047 and L061; L045 supplies only
downstream context. No cross-notebook theorem is needed.

1. Specify the entire rational fiber at the saved scalar, its coordinate
   field, and its universal E0-point. Use L047's cited field identification
   with K, explaining the contravariant Spec map. An intrinsic witness
   in that exact fiber field is sufficient; an explicit power-basis
   conversion is optional, not a prerequisite for existence.
2. Define one global connecting class from that point. Check the support
   and normalization using L033's unconditional group-containment proof.
   Retain exceptional charts and good divisors. Do not infer this class
   from separately selected local image elements.
3. Tensor the same field identification at five and eleven. Check the
   saved scalar's exact hypotheses for the local power domains; L036
   and L041 have different residue-characteristic assumptions. Use
   the universal whole-fiber point on every factor. L061 retains all
   eleven unramified embeddings; L041 orders eleven-adic primes by
   k-residues 8,2,10, and L044 retains both rational permutations.
4. Certify the two memberships by the existing exact-image theorems,
   or give explicit labels/valuations with those fixed identifications.
   A theorem-based certificate must verify every hypothesis, even if
   it does not compute a basis-vector representative. A conjugacy orbit
   is not a choice of unrelated local classes.

One witnessed simultaneous membership meets the bounded continuation
test; then stop. Failure rejects this canonical candidate only, and
requires recording the exact failing interface rather than enlarging
a search. Full eleven-adic unit compatibility, all-place intersection,
other twists, rational power conditions and integer lifting remain
independent. No witness, residue calculation, new lemma or mathematical
script has been produced during this literature turn.

## Mathlib

Full canonical-fiber/simultaneous-class theorem: not checked. Supporting
scheme base change, connecting maps, Kummer localization and local
power-domain coverage: not checked. Unknown coverage is not absence.
Use the cited standard inputs and existing audited local proofs.
