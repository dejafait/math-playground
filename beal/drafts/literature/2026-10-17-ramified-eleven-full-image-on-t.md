# Ramified eleven-adic full-image condition on T — source comparison

TARGET: Determine whether L084's T is contained in the full Kummer subgroup at L073's degree-ten eleven-adic place.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L073's full local generators, L074's supported-class definition, L084's exact T, L086's envelope and audited L088's norm conclusion; compared ATTEMPTS/033–039 and the ready primitive-eleven/global-norm assessments. Bounded exact-curve, local Kummer and norm/square-class searches found general machinery but no inspected theorem deciding this containment; queries and reads are below.
SOURCE_EVIDENCE: Milne ANT v3.08 (19 July 2020), Proposition 2.19/Corollary 2.20 pp.31–32 and Proposition 8.2/Corollary 8.4 p.136, statements and proofs; Clark ANT II, accessible 161-page notes, Theorem 2.24 p.73 and Theorem 2.36 pp.79–80, statements and proofs, plus Theorem 1.79 p.58 statement; reused BPT arXiv:2001.02263v3 Section 1/Lemma 1.3/Remark 1.4 pp.3–4 and Bruin–Stoll 14 March 2008 Section 6 pp.11–12 through the ready assessments identified below.
COMPARISON: Known full-image, norm/base-change and local square-class results permit a finite necessary-envelope comparison. Audited L088 supplies a global square D/F norm on every T-class, an input absent from the stopped five-probe test. No inspected source or notebook result already compares that norm constraint with the full ramified Kummer subgroup.
GAP: Separately construct the ordered local norm maps, including both conjugate quadratic embeddings, and test the entire resulting necessary envelope against L073's full subgroup. Neither containment nor an outside global class is established here; a failing envelope test would decide only this sufficient mechanism.
REASON: Essential source coverage now supports one bounded norm specialization for the unchanged target without a complete class backend, enlarged probe family or unit search. Import the general theorems and prove only the field-specific norm and subgroup comparison in a later research turn.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; the essential new comparison is between audited L088's D/F norm constraint and the full subgroup at the omitted ramified place, beyond the previous five-probe and thirteen-adic scopes.
SCOPE: Exactly TARGET for L084's unchanged T, L074's arbitrary supported classes and L073's entire ordered cubic over L; one necessary-envelope test using L088 and the already imposed rational eleven-adic images. No class computation, new global witness search, larger reciprocity probe family or integer-lifting claim is approved.

## Relevance and discriminating test

The main gap is positive primitive integer emptiness in the 54a1 branch
and the other residual signatures. Every transported primitive point
must satisfy the full Kummer condition at the degree-ten eleven-adic
place. L084 deliberately omits that condition from T. A certified
supported class in T outside this full subgroup would prove a further
necessary restriction; a proof of containment would retire this
particular condition. Either could guide the remaining dimension work,
but neither by itself gives a rank bound or integer emptiness.

Essential inputs are L073's entire split cubic over its fixed degree-ten
field L, L074's supported classes, L082's primitive dyadic image, L084's
exact T, L086's envelope obstruction and L088's now audited global norm
constraint. No full S-unit basis in D, localized class-kernel value,
weak-approximation globalization or integer lift is assumed. The
ordering of all three ramified components must be retained.

The completed review below approves a bounded sufficient norm test,
not a mathematical answer. A necessary envelope tuple alone cannot
certify a global class outside the subgroup. Accept a later containment
result only with a universal proof covering T, or strictness only with
an actual global supported-class witness satisfying every condition of T.
If the proposed norm envelope admits an outside tuple, stop this
sufficient test without promoting it to global noncontainment.

## Duplicates and route limits

The old primitive-eleven comparison assessment explicitly covers only
its five rational-cubic probes and assumes no extra full-local condition.
Its recorded witness in ATTEMPTS/038 defeats that sufficient proof of
the primitive diagonal condition; it is not a witness to the present
failure of full-local containment. No inference in either direction
is drawn here. ATTEMPTS/039 is now an audited stop for J13 on T.

ATTEMPTS/034–036 exhaust their specific affine, quotient and ideal-basis
searches. They are not reopened, expanded, or treated as global absence
proofs. ATTEMPTS/037's complete class-backend blocker remains in force;
a missing unconditional class certificate cannot be replaced by GRH
or by finite relation checking. The proposed source review must choose
a mechanism independent of those blocked computations. It may reuse
ready source coverage only where the exact hypotheses match.

## Primary results and applicability

Reuse the ready assessments
`2026-10-15-eleven-adic-even-valuation-containment.md`,
`2026-10-17-primitive-eleven-global-comparison.md`, and
`2026-10-17-thirteen-global-norm-filter.md`, all in this directory,
for the unchanged Kummer, support, reciprocity and norm interfaces.
The local conclusion needed here is already proved and audited in L073:
the full ramified image has four classes generated by the exceptional
images of its two stated two-torsion points. There is no need to rerun
a local point enumeration or reprove general descent theory.

- J.S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
  19 July 2020, Proposition 2.19 and Corollary 2.20, printed pp.31–32,
  give field norms from minimal polynomials and, for separable
  extensions, all embeddings. Proposition 8.2 and Corollary 8.4,
  p.136, identify the entire completion algebra and the product of
  local norms. The statements and complete proofs were read, including
  the general-degree case in 2.19 and the tensor-product determinant
  argument in 8.4. These require finite separability, not normality or
  a maximal polynomial order. Characteristic zero supplies separability
  for the fixed fields. They permit exact local norm matrices, while
  retaining distinct embeddings into isomorphic factors. No ramified
  norm matrix or implication for T is supplied by this citation.
- Pete L. Clark, [*Algebraic Number Theory II: Valuations, Local Fields and Adeles*](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
  accessible 161-page version, revision date unidentified, Theorem 2.24
  (Local Square Theorem), p.73, and Theorem 2.36, pp.79–80. Both
  statements and proofs were read. The former treats Henselian discrete
  valuation fields of characteristic different from two. The latter
  assumes a normalized Henselian discrete valuation, finite residue
  field, and power exponent prime to the field characteristic; its
  proof includes both directions for the higher-unit power map and
  the valuation decomposition. These cover all finite extensions of
  Q11 here and certify exhaustive finite square-class coordinates.
  Theorem 1.79, p.58, was also read at its strict Hensel–Newton
  statement, consistent with the ready lifting coverage. No unit
  derivative at two or unramified norm formula is transferred to a
  ramified extension. Import these theorems; the future basis labels
  and exact norm calculations remain specialization obligations.
- Barrera Salazar–Pacetti–Tornaría, [arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
  17 September 2020, Section 1, pp.3–4, Lemma 1.3 and Remark 1.4,
  supply the full cubic Kummer realization and finite-local image size.
  The image-size statement was reopened; reuse the complete comparison
  and exceptional-point coverage in the eleven-adic assessment above.
  It has no later unit-containment hypothesis. Here L073 already
  supplies its exact application; odd residue characteristic alone
  does not imply all-even valuations, as ATTEMPTS/033 records.
- Bruin–Stoll, [*Two-cover descent on hyperelliptic curves*, 14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
  Section 6, pp.11–12, FakeSelmerSet and ad 4/8/11/16, are reused
  through the ready primitive-eleven assessment. The global-generator
  bottleneck and early local-redundancy passage were reopened. Partial
  local tests give an overestimate; a complete global set requires
  class contributions. This supports a necessary-envelope comparison,
  not realization of arbitrary local tuples.

The ready global comparison also records the matching FNS Section 7.2
Selmer calculation as GRH-conditional. It is not an unconditional
answer for this T and is not imported. Complete D S-unit generation
and the localized class kernel remain unavailable; no source blocker
is essential to the bounded norm test. Broader local-duality theory
is unnecessary for this selected mechanism and is not newly assessed.

## Bounded certificate for the separate research turn

1. Fix the same theta and the ordered roots alpha,beta,gamma of L073.
   Use its two exact exceptional generators for the full subgroup;
   do not replace it by its valuation image or by primitive J11.
2. Use L088's already audited square N_D/F conclusion for every class
   in T. Localize that conclusion at **every** place of F above eleven
   by Milne 8.2/8.4. Construct the full D/F factor maps from the existing
   K and F decompositions. Keep the two conjugate M-algebra structures
   on ramified factors distinct: an abstract field identification alone
   does not identify norm coordinates. No extra full-local condition
   at L is to be imposed on T while constructing this envelope.
3. Choose exhaustive valuation-parity/unit square-class coordinates in
   Q11, M and L using the cited local results. Compute norms of their
   basis representatives by the exact minimal-polynomial or determinant
   formula, and account for the action of quadratic conjugation.
   Do not assume that norm equals scalar restriction, that an even
   degree preserves nonsquares, or that odd-degree norm is an
   isomorphism without checking the required basis maps.
4. Form a finite necessary envelope using the two rational Kummer
   conditions already in T, the D/K square-norm condition at L, and
   the localized D/F square-norm conditions. Exhaust the finite
   square-class coordinates by linear algebra or a complete table;
   prove that every T-class maps into it, including supported nonunit
   class lifts. This uses existing universal norms, not a replacement
   of W_S by exhibited S-units or presumed local globalization.
5. Test its ramified projection for containment in L073's full subgroup.
   A positive sufficient test must include the complete kernel/image
   calculation and the universal applicability argument. An outside
   envelope tuple stops this norm certificate only; it establishes
   neither a global witness nor strictness on T. Preserve all prior
   stops and require separate source coverage for a different follow-up.

If a script is useful in that research turn, save its full basis maps,
embedding conventions, finite table or matrix, and failing rows on disk;
print only dimensions, containment result, checks and certificate path.
A symbolic exact proof may instead suffice. No numerical local sample,
complete global basis, new backend, new norm-vanishing theorem or
lengthy unbounded search is part of this plan.

## Search record and limits of this review

Queries included `elliptic curve 2 descent split multiplicative local
Kummer image odd residue characteristic norm square classes`,
`local fields odd degree extension norm square classes isomorphism
quadratic Hilbert symbol`, `Barrera Salazar Pacetti Tornaria
2001.02263 Lemma 1.3`, `site.jmilne.org "square classes" "local"`,
`"odd degree" "norm" "square classes" local fields`, and
`"X0(11)" "norm" "2-descent"`. Relevant primary matches were BPT
and Milne; Clark's cited local statements were then inspected directly.
Other search results concerned general quadratic forms, finite fields,
or unrelated curves. They are not theorem inputs. No novelty is
inferred from failure to locate an exact matching theorem.

This literature-only step establishes coverage and a bounded test,
not containment, noncontainment, a norm matrix, a new local image,
a global witness or an improved dimension. It writes no lemma or
mathematical script. Full and supporting Mathlib coverage is not
checked. Essential continuation inputs are L033/L069 for the common
fields, L073/L074, audited L082/L084/L086, and audited L088. Independent
gaps remain actual T and its localization, k_S, complete supported-unit
arithmetic, other primitive classes and rational/integer lifting. T
still cannot bound the full Mordell–Weil image, and Beal is IN_PROGRESS.
