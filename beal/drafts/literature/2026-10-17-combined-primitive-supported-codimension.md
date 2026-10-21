# Combined primitive supported-space codimension: source comparison

TARGET: Determine whether combining L077's three full-local tests with L082's primitive dyadic filter gives codimension at least three in L075's W_S, using L083's fixed point class.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready support, supported-pruning and fixed-point assessments; inspected L074–L077 definitions and relevant proofs, audited L082/L083 statements and application ranges, history/270 and ATTEMPTS/014,034–037; bounded exact-curve and primitive-local-image searches found general filtering methods but no inspected theorem giving this combined bound.
SOURCE_EVIDENCE: Bruin–Stoll, Two-cover descent on hyperelliptic curves, author manuscript 14 March 2008, Section 6 pp.11–12, FakeSelmerSet steps 7–17 and complete explanation, freshly inspected; Barrera Salazar–Pacetti–Tornaría arXiv:2001.02263v3 (17 September 2020), Section 1 p.3, general-field Kummer exact-sequence construction and evaluation, freshly inspected; Simon (2002) Propositions 1.1–1.4 pp.8–9 reused through the ready support and quotient assessments.
COMPARISON: Known localization/intersection and Kummer-homomorphism results cover the general machinery; L082 already explicitly proves its particular restricted image is an order-two subgroup. No inspected source states the three-witness rank in this W_S. A separate field-specific assembly is required; general restricted point images need not be subgroups.
GAP: Coverage is ready for checking the exact combined quotient, witness membership and independence. No combined subspace theorem, rank-three conclusion, new unit exclusion or class-kernel value is proved in this literature turn.
REASON: Approve one separate mathematical specialization of the unchanged TARGET using the existing witnesses and known linear algebra, without a new local enumeration or class backend.
LITERATURE_REASON: The newly proposed target combines a primitive restricted image with three full-image quotients, outside the separately assessed calculations; the supervisor requires separate source comparison. Reuse unchanged coverage and retrieve only the general filtering and homomorphism interface.
SCOPE: Exactly TARGET with L074–L076's fixed K,D,theta and full support, L077's three full-local tests, audited L082's two-element dyadic subgroup and audited L083's same beta_sigma. REPRODUCTION is approved for a separate proof attempt; no assertion of originality or full Mordell–Weil rank bound is approved.

## Exact proposed scope

Use the same K, D=K[theta], support above two and eleven, W_S and
V_S of L074–L076. The three full-local tests are exactly L077's
rational dyadic place and its two rational eleven-adic places,
quotiented by their full local Kummer subgroups. The additional
condition is localization of the whole dyadic pair in L082's exact
set {(1,1),(1,xi)}. The proposed filtered set is the intersection of
these four conditions in W_S. No other local place is silently added.

The proposed witnesses are L077's v,w and L083's beta_sigma, with
L062's fixed sigma and point unchanged. Essential inputs are L074,
L075, L076, L077, L082 and L083, retaining their underlying fixed
field and Kummer conventions. No cross-notebook input is proposed.
Source review must reuse the ready support, local-image and Kummer
assessments, checking any genuinely new linear-algebra/interface scope.
No new class-group computation or general descent reproof is requested.

The main gap remains positive primitive integer emptiness. The
intermediate target is codimension at least three in W_S, not a third
removed direction in V_S. Its plausible downstream use is an explicit
dimension bound for the supported space of candidate primitive point
classes, with the unknown localized class contribution retained.
L076's ambient formula supplies the baseline for that comparison;
no numerical bound for the class kernel is proposed or assumed.

Continuation test: establish that the combined admissible set is a
linear subspace, all three witnesses belong to the same W_S, and their
images in the combined quotient have rank at least three. If any
membership, subgroup or independence premise fails, isolate it and
withhold the bound. These are proposed tests, not results of this
audit turn. Do not infer V_S membership of beta_sigma from its global
point origin or from supported valuations alone.

Even success would not bound the full Mordell–Weil rank: the additional
primitive filter explicitly removes an actual global point. It would
not give unit upper bound eleven, determine localized class groups,
exclude all candidate classes, lift integers, handle other branches
or settle Beal. Preserve L062/L065's distinct five-isogeny survivor.

ATTEMPTS/014 and 034–037 remain stopped on their recorded evidence.
This proposal uses the audited point exclusion and existing witnesses,
not another affine search, a larger ideal-basis search, or a repeat
class-backend probe. The earlier mathematical exploration budget is
not renewed. Mathlib coverage of this exact assembly is not checked.
No new lemma or mathematical derivation occurs in this proposal.

## Source evidence and comparison completed on 2026-10-17

The ready [supported-containment assessment](2026-10-15-supported-kummer-containment.md)
records Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Sections 1.1–1.2,
Propositions 1.1–1.4, pp.8–9, including the denominator cases in the
support proof. Reuse that inspected source coverage rather than reprove
support. The [supported-quotient audit assessment](2026-10-15-supported-norm-square-quotient-audit.md)
and [supported-pruning assessment](2026-10-16-rational-cubic-supported-pruning.md)
cover the unchanged localized groups and local tests. L075's audited
statement applies to every E0(K) point, without a primitive-solution
premise; the proposed application to beta_sigma still must be written
in the separate attempt. V_S membership is neither supplied nor needed
as an assumption for a target in W_S.

Freshly inspected primary passages:

- Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic curves*,
  Math. Comp. **78** (2009), 2347–2370,
  [author manuscript dated 14 March 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
  Section 6, printed pp.11–12: FakeSelmerSet steps 7–17 and its complete
  explanation, particularly ad 4, ad 7 and ad 16. The algorithm imposes
  a norm condition and intersects localization preimages; odd degree
  uses full algebra square classes. Localization can be computed on
  generators by linear algebra. The text distinguishes supported
  square classes from supported units and allows partial local testing
  to give an overestimate. This supports the construction method,
  not the specialized witness rank or replacement of a full local
  image by an arbitrary restricted subset. No reproof of this algorithm
  or assertion of fake-Selmer equality for our primitive filter is needed.
- Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
  *On 2-Selmer groups and quadratic twists of elliptic curves*,
  [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
  Section 1, printed p.3, including the multiplication-by-two exact
  sequence and Kummer construction through the invertible affine
  evaluation. It assumes a field of characteristic different from two
  and a monic square-free cubic. It supplies a group morphism into
  norm-square algebra classes, with affine evaluation x−T when
  invertible. K, Q2, H and the two Q11 places lie within this scope;
  g has the recorded nonzero discriminant. The same origin-preserving
  X=4x model and distinguished theta must be retained. This coverage
  supports full-image subgroup and localization conventions; it does
  not make primitive point subsets into groups.

The standard first isomorphism theorem and rank–nullity theorem are the
only abstract linear-algebra inputs proposed beyond these sources.
No source extraction or reproof of them is needed. Their applicability
requires actual subspaces and well-defined quotient homomorphisms;
that verification and the particular rank test belong to the next turn.

The literature distinction is substantive: L082's Conclusion explicitly
states that its displayed set is an order-two subgroup, justified by
its exact two classes. Thus the proposed subgroup premise has a precise
canonical input, rather than an inference from restricted-image size.
L077's rank-two statement concerns its full-local quotients; it does
not already state the primitive combined rank. L083 is an exclusion
under two-descent, not an S-unit assertion. These comparisons complete
source scope without performing the new assembly.

## Bounded search, duplicates and failures

Fresh external queries were `"two descent" "primitive" "local images" subspace`,
`"X0(11)" "codimension" descent`, and
`"Two-cover descent on hyperelliptic curves" "linear algebra"`.
They located the primary Bruin–Stoll method and unrelated curve/software
results, not a matching combined-codimension theorem. Only the primary
passages specified above are imported. Search snippets and unrelated
hits are not evidence of a theorem or novelty. The ready exact-curve
and stronger-result searches are retained in the linked assessments;
they were not repeated wholesale. No essential unread lead remains for
this bounded assembly; no claim about literature-wide absence is made.

Narrow searches of the 2026-10-17 assessments and histories 263–270
found this proposal and its two separate local inputs, but no completed
combined-rank argument. ATTEMPTS/014 concerns the different five-isogeny
map. ATTEMPTS/034–036 exhaust specified supported-unit searches;
ATTEMPTS/037 parks an uncertified class backend. None establishes an
obstruction to the proposed W_S witness test, and none is reopened.
The earlier three-turn mathematical exploration allowance stays spent.

## Approved continuation and abandonment test

The target remains exactly TARGET. In one separate RESEARCH attempt,
use the exact proposed intersection of the three L077 full-local
conditions and the whole dyadic pair condition in L082. Define each
ambient square-class group and quotient, and check compatibility of
all generators, fixed places and theta. Use L082's proved subgroup
statement explicitly. Check v,w in V_S inside W_S and beta_sigma in
W_S from the same global point and L075; never assume beta_sigma is
an S-unit. Verify the proposed three witness images are independent
in the combined quotient, retaining the kernel of the three full-local
tests as a distinct object. Do not count three test rows as three
independent conditions or replace full local classes by valuations.

Continue this assembly only if all membership, subgroup and quotient
premises hold and the rank test certifies at least three. Otherwise
identify the failed premise or dependence and withhold that bound;
an incomplete certificate is not a rank-at-most-two proof. No new
search box, arithmetic backend or local point enumeration is authorized
by this assessment. Record any proof and qualifications canonically
in a separate lemma only after the mathematical attempt establishes it.

Possible success would bound a space containing candidate primitive
point classes, with the localized class term of L076 still explicit.
It would not bound the full Mordell–Weil image, since the added filter
removes the actual point of L083. It does not by itself improve the
unit bound to eleven, establish integer emptiness, cover other classes
or twists, or affect L062/L065's five-isogeny survivor. Mathlib coverage
of this combined statement and the supporting linear algebra is not
checked. This turn completes source comparison only: no specialized
codimension or witness-independence result has been derived, and no
lemma, mathematical script, DAG or argument overview has been changed.
