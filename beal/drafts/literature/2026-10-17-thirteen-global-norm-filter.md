# Global norm test for the thirteen-adic filter — source comparison

TARGET: Test whether the global norm from L069's D to Q(theta) forces the rational-root component of loc_13(T) to be square, with T as in L084.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L069/L074/L077/L084/L086/L087 and ATTEMPTS/029/038; searched norm/corestriction two-descent, the defining cubics, norm towers and completion compatibility. Read the primary statements and proof cases below; reused existing supported-class and reciprocity assessments.
SOURCE_EVIDENCE: Stein, A Brief Introduction to Classical and Adelic Algebraic Number Theory (May 2004), Section 5.2 Corollary 5.2.3 p.28; Milne ANT v3.08 (19 July 2020), norm definition and Proposition 4.1 pp.68–69, Proposition 8.2 and Corollary 8.4 p.136; Stacks Lemma 31.18.6 tag 0BD2; Milne CFT v4.03 (6 August 2020), III Proposition 1.2, Lemmas 1.3–1.5 and proof p.98; Conrad Finite fields, Theorem 4.6 and proof pp.9–10, accessed 2026-10-17.
COMPARISON: General norm, support and local compatibility results are known, while L077 supplies complete supported-unit arithmetic in the rational cubic. None of the inspected theorems decides this norm image on T or the rational-root condition. The field-specific application remains to be proved; no general norm theorem needs reproof.
GAP: Bound the norm image of every class in T, including localized class lifts, and compare its localization at the rational thirteen-adic root with the original component. No such bound, component-square conclusion, strictness or independence is established here.
REASON: Essential source coverage now permits one bounded norm specialization separately from this literature turn. Preserve the target and test only this sufficient mechanism before choosing further work.
LITERATURE_REASON: The scope changed from L087's local image audit to a global norm from D to its rational cubic subfield; transitivity, ideal support and all-completion compatibility were essential unread inputs for this target.
SCOPE: The exact saved target on L084's unchanged T with support at all primes above 2 and 11; general supported square classes, not just exhibited units or point classes. No full-local condition at the degree-ten eleven-adic place is added.

## Gap, target and decision test

The main gap is positive primitive integer emptiness, even for the
remaining 54a1 branch of ordered (3,4,11), and ultimately for every
residual Beal signature. The intermediate target is the displayed
rational-root component test at thirteen. A universal square constraint
would certify redundancy of that component on T. A certified global
class in T with nonsquare component would instead prove strictness of
that component test. Neither conclusion is obtained in this review.

Continue the sufficient method only if its proved norm constraints
force the required square for every possible norm class. If the
necessary norm envelope still permits a nonsquare component, record
failure of that envelope and stop this sufficient method. An envelope
element is not a global counterexample. A successful component test
must explain what remains before any claim about the full J13 of L087.
Bounds 13+dim ker(n_S) and fourteen are unchanged; neither is the desired
eleven, and T does not bound the full Mordell–Weil rank.

## Local inputs, duplicates and recorded failures

L077 identifies F=Q(theta)=Q(t), t^3-t^2+t+1=0,
theta=8-14t+6t^2, inside L069's D, with D=K tensor_Q F. Its audited
arithmetic proves class number one for F, complete supported-unit
generators and their norms. Its supported norm-square unit classes
are exactly 1,v,w,vw, where v=-1/t and w=2-t-6t^2. This is an existing
input, not a result of this turn. Establishing that an arbitrary D/F
norm can be compared with that list remains an applicability obligation.

L074 defines support by even normalized valuations outside S, allowing
negative valuations and nonunit representatives. L084 fixes T and warns
that it excludes an actual global point class. L087 orders the cubic
factors over the entire U=K tensor_Q Q13 by the rational root alpha,
then beta,gamma, and proves J13={1,(1,nu,nu)}. These exact interfaces
are not a norm-image computation.

L077's primal rank-two restriction and L086's dual five-probe envelope
do not already perform the proposed D/F norm comparison. Preserve
ATTEMPTS/038: its nonglobal tuple defeats those five equations at
eleven. Do not merely evaluate those probes again. ATTEMPTS/029's
five-isogeny survivor at thirteen remains valid and is distinct from
this two-descent test. Exhausted affine searches and uncertified class
backends are not reopened. FNS's GRH-dependent degree-36 Selmer
dimensions remain outside the unconditional inputs, as assessed in
2026-10-17-primitive-eleven-global-comparison.md.

## Primary statements actually inspected

- William Stein, *A Brief Introduction to Classical and Adelic Algebraic
  Number Theory*, May 2004, [author PDF](https://wstein.org/papers/ant/ant.pdf),
  Section 5.2, Corollary 5.2.3, printed p.28, and complete proof
  (also [author HTML](https://www.williamstein.org/papers/ant/html/node15.html)).
  For a tower of number fields, element norms compose. The proof counts
  all extending embeddings and assumes no Galois condition.
- J.S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
  19 July 2020: norm definition and Proposition 4.1, pp.68–69, including
  the nonnormal proof case; Proposition 8.2 and Corollary 8.4 with their
  complete proofs, p.136. Ideal norm sends P to p raised to its residue
  degree and respects principal ideals. The finite separable completion
  algebra is the product over all extending places; element norm
  localizes to the product of their local norms. These general hypotheses
  hold for the characteristic-zero number fields here.
- Stacks Project, [Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2),
  statement and full proof, accessed 2026-10-17. A finite locally free
  morphism of positive degree has its determinant norm, compatible with
  arbitrary base change. The field extensions and their entire tensor
  algebras qualify. Choosing one convenient tensor factor would not
  give this theorem's norm.
- Milne, [*Class Field Theory*, v4.03](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
  6 August 2020, III Proposition 1.2, Lemmas 1.3–1.5 and complete proof,
  p.98. A finite unramified local extension has surjective unit norm.
  The proof gives the commuting residue-norm diagram, then handles
  higher unit filtrations and convergence. Verify the actual completion
  and unramified hypotheses before using this diagram. Unit-norm
  surjectivity alone is not the requested component criterion.
- Keith Conrad, [*Finite fields*](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf),
  Theorem 4.6 and complete proof, printed pp.9–10, accessed 2026-10-17
  (no version date identified). For F_(p^n)/F_p the nonzero norm is
  a -> a^((p^n-1)/(p-1)); the proof sends a multiplicative generator
  to a generator. This provides the formula for a later thirteen-adic
  square-character comparison, not that specialization itself.

Reuse the inspected supported-class coverage in
2026-10-15-supported-norm-square-nonunit-quotient.md (Simon Proposition
1.3 and Milne localized ideal arithmetic), and local lifting coverage
in 2026-10-17-primitive-thirteen-two-descent-image.md. If a Hilbert
product is needed, reuse Milne reciprocity as assessed in
2026-10-17-primitive-eleven-global-comparison.md. Its omitted-place
argument for five probes does not automatically delete places for a
different probe. Direct norm transport can instead retain places
through the ideal and completion formulas.

## Bounded continuation approved for a later turn

Apply the cited theorems to an arbitrary representative of a class in
T. Establish its D/F norm's support and rational norm-square condition
before reducing to L077's cubic data. Control every finite prime outside
support by its normalized valuation; retain all places above two and
eleven and both archimedean types, including signs and negative
valuations. Do not assume the representative is an S-unit, a Kummer
class or a realized point. If class-number-one in F permits square
correction, justify it and preservation of the tested square class.

Compute only the necessary cubic norm constraints from the conditions
actually defining T. Keep every local factor, including ramified
eleven-adic ambient classes not restricted by a full Kummer condition
in T. Specialize the completion norm at thirteen using L087's fixed
rational root and L064's full U; test whether this information forces
that component square. Do not replace norm by scalar restriction or
infer squareness from an even extension degree. If extra reciprocity
is required, justify every omitted finite and infinite contribution.

No field-specific norm identity, envelope, pairing, residue computation
or new lemma is derived here. Known results cover the general machinery;
SPECIALIZE permits the stated applicability and finite comparison work,
classified as REPRODUCTION unless a later assessment supports different
scope. Full/supporting Mathlib coverage is not checked. No novelty
claim follows from this bounded discovery search.

Queries included `"norm" "corestriction" "2-descent" elliptic curves
number fields`, `"t^3-t^2+t+1" norm Selmer`, `site.jmilne.org math ANT
norm tower completions product local norms`, `"X³−4X²−160X−1264" norm`,
and `"two-cover descent" "norm" "local" subfield`. Matches about
quadratic-extension Selmer transfer and unrelated twists do not supply
this T-specific claim; their full theorems were not imported. No direct
matching theorem was established by the search. No essential source
blocker remains for the bounded norm test.

Continuation inputs: L033, L064, L069, L074, L077, L082, L083, L084,
L086 and audited L087. No cross-notebook input. Complete S-unit data in
D, the localized class kernel, actual global norm-image realization,
independence, integer lifting and other Beal signatures remain
unresolved. Approval is for a later mathematical turn; this review
changes no lemma, mathematical script, DAG edge or main argument.
