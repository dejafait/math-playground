# Five-support shift and core extension — source comparison

TARGET: Assess extension of L040's five-support prohibition to multiplicative subgroup shifts and arbitrary disjoint 59-cores/private points.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 109 searched the specific five-support proofs, assessments, working notes and histories for shifts/arbitrary 59-cores, and read ATTEMPTS/019–021,023–025; no completed local duplicate was found. External intersection-matrix/scaling, affine-evaluation and exact-subgroup queries found supporting algebra and generic results, but no inspected matching extension; queries and unread leads are recorded below.
SOURCE_EVIDENCE: Retrieved AGL arXiv:2304.09445v3 Definition 2.5/Lemma 2.7 and full proof, printed pp. 7–8, and Theorem 2.9's generic-field statement; ST arXiv:1911.01502v1 Lemma 4.3 and its common-root proof case, pp. 11–12, and Section 5's characteristic-two assumption. Inspected official Mathlib eval_comp, comp_assoc, comp_C_mul_X_coeff, comp_C_mul_X_eq_zero_iff, natDegree_comp and dvd_iff_isRoot, with selected source proofs and immutable source revisions below.
COMPARISON: Known signed equality constraints, factor-theorem division and polynomial composition cover the required tools over E and F. L040 supplies the audited unshifted rank input; L031 already treats arbitrary admissible cores/private points for four messages. Neither inspected literature nor L031 states this full five-support extension; generic rank and arbitrary label permutations do not supply it.
GAP: Prove the specialization for all s in H and all admissible C,W_i: verify signed-system transport, strict reduced degree and every tuple row without descent or projection. The extension itself remains unproved; no 59-core transfer, family cap or safety result is covered.
REASON: The changed quantifiers now have adequate essential source coverage for one later REPRODUCTION proof attempt. Import the standard algebra and L040's audited certificate, and justify only their application; do not reprove generic rank or repeat the finite elimination.
SCOPE: Common multiplicative shift s in H of precisely L040's ten lexicographically assigned overlap pairs; every disjoint 59-subset core and five distinct private singletons inside H; strict row degree less than 64 over F, one ambient-field center and every m>=1, allowing extra agreements.
COVERED_TARGET: Prove L040's equality conclusion for every multiplicative subgroup shift and every admissible 59-core/private-singleton choice.

## Proposed exact scope, not an established theorem

Retain E=F_65537, F=F_(65537^28), H of order 1024, h=19139,
k=64 and m>=1. In the lexicographic edge order of L040, indexed
r=0,...,9, propose overlap pairs

\[
 U_{ij}=s\{h^{2r},h^{2r+1}\},\qquad s\in H.
\]

Take any 59-subset C of H disjoint from all twenty overlap points and any
five mutually distinct singleton private sets W_i in H disjoint from C and
all overlap points. The proposed supports are
S_i=C union W_i union the four incident overlap pairs.
The desired conclusion is L040's stronger equality assertion: any five
polynomial m-tuples of strict row degree less than 64 agreeing with one
center on those supports are equal. Extra agreements are allowed; messages
and the center need not descend to E. This paragraph only fixes the
statement to be assessed. It does not assert or derive the conclusion.

## Relevance, comparison obligations and test

The main gap remains arbitrary-center 67/68-agreement safety with
955<=t_star(m)<=957. A uniform extension could broaden the available
five-support restrictions for a later 59-core family certificate. Unlike
the established 60-core model, that prospective certificate would retain
this five-support information. A sound transfer, a useful cap, cross-core
consistency and common-center realization remain independent unresolved
steps. No bound, transfer or quantitative usefulness is asserted here.

Essential local inputs are L040's complete fixed-label proof and audited
rank certificate, C001a's instance, and L031's signed-kernel methodology.
L034 supplies a possible transfer comparison, not this extension.
The source comparison below checks standard change-of-evaluation-variable
results, common-root division, fixed-label rank qualifications, duplicates
and recorded failures. Reuse primary coverage where it matches; retrieve
only essential additional theorem statements/proof cases. AGL's generic
rank result is not automatic fixed-label coverage. No full matching
Mathlib extension theorem is established; supporting algebra coverage
is recorded below.

Approve a narrowly specified mathematical continuation only if known inputs
cover the change of variables and altered core/private hypotheses, with
the precise remaining specialization recorded. If the scope is already
covered by a stronger theorem, IMPORT it. If essential coverage is missing,
retain literature-only status. A later mathematical test must verify the
transformed signed system and tuple necessity for every stated parameter,
or save a counterconfiguration; it must not infer a family cap from a
prohibition. Do not reopen the stopped local models or coordinate-replacement
avoidance constructions by renaming them. No mathematics on this extension
was performed during the repeated L038 audit.

## Completed primary comparison, step 109

The changed quantifiers justify this literature turn despite ready coverage
of the earlier fixed configuration. This review establishes adequate tools
for a later specialization, not the proposed extension. In particular,
the five tuples in the equality assertion need not be pairwise distinct:
the later proof must establish equality from the selected agreements alone.

Alrabiah–Guruswami–Li, *Randomly punctured Reed–Solomon codes achieve
list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/html/2304.09445v3#S2.SS3),
26 July 2023, Definition 2.5 and Lemma 2.7, printed pp. 7–8:
the definition uses signed Vandermonde blocks for any prime-power field
and any message count. The lemma assumes distinct scalar RS codewords;
its complete proof subtracts the last coefficient vector to obtain a
nonzero specialized kernel vector. Its scalar distinctness hypothesis
does not license a projection of arbitrary tuples. The signed equations
are the applicable framework. Theorem 2.9, printed p. 9, assumes weak
partition connectivity and concludes rank over a rational-function field;
it does not settle prescribed subgroup labels. These exact passages were
retrieved; no new generic-rank proof was needed.

Shangguan–Tamo, *Combinatorial list-decoding of Reed–Solomon codes
beyond the Johnson radius*,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Lemma 4.3, printed pp. 11–12:
the scalar list-two failure hypothesis is at radius (2/3)(1-R).
Its inspected proof divides message differences by the product of
distinct common roots and retains strict reduced degree and residual
overlap zeros. Import only that factor-theorem step, with its common
root set arbitrary; its decoding conclusion is not this extension.
Section 5 assumes characteristic two, so its unsigned matrices remain
inapplicable. The previously assessed generic/random higher-order-MDS
comparison is reused from the fixed-five assessment; no changed generic
hypothesis is claimed here.

## Supporting algebra and Mathlib coverage

The following are inspected primary theorem statements, not derived
five-support claims. Official documentation was retrieved on 2026-10-08;
the linked source revisions are immutable.

- Over a commutative semiring, `Polynomial.eval_comp` gives
  evaluation of a composition as successive evaluation;
  `Polynomial.comp_assoc` gives associativity of composition.
  [Statements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.eval_comp)
  and [source at 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Eval/Defs.lean).
  The complete `eval_comp` source proof was inspected; it uses polynomial
  induction. No reproof is needed.
- Over a semiring, `Polynomial.comp_C_mul_X_coeff` states
  `(p.comp (C r * X)).coeff n = p.coeff n * r^n`.
  `Polynomial.comp_C_mul_X_eq_zero_iff` additionally assumes
  `r` belongs to `nonZeroDivisors R` and says the composition is zero
  exactly when `p` is zero.
  [Statements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Degree.html#Polynomial.comp_C_mul_X_coeff)
  and [source at 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Eval/Degree.lean).
  Both complete source proofs were inspected: coefficient expansion,
  then coefficientwise cancellation using the non-zero-divisor hypothesis.
- Over a semiring with no zero divisors, `Polynomial.natDegree_comp`
  states `natDegree (p.comp q) = natDegree p * natDegree q`.
  `Polynomial.natDegree_C_mul` requires a nonzero constant multiplier
  and preserves natural degree.
  [Statements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Lemmas.html#Polynomial.natDegree_comp)
  and [source at 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Degree/Lemmas.lean).
  The complete composition-degree proof was inspected, including its
  constant-inner-polynomial and zero-outer-polynomial cases.
- Over a commutative ring, `Polynomial.dvd_iff_isRoot` states
  `X - C a` divides `p` exactly when `a` is a root of `p`.
  [Statement](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.dvd_iff_isRoot)
  and [source at 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Div.lean).
  The declaration was checked; no full proof audit of this theorem was
  needed. ST's inspected proof case supplies the finite common-root use.

E and F are commutative fields, so the ring, semiring and no-zero-divisors
hypotheses hold. A shift s in H is nonzero and a non-zero-divisor in
both fields. This checks the supporting algebra's hypotheses; applying
it to the twenty signed constraints and the changed core remains the
next proof obligation. No full matching five-support theorem was found
in the inspected Mathlib passages; full-library coverage is not checked.
The supporting declarations do not supply a list-size cap.

## Bounded search, duplicates and leads

Queries actually issued included:

- `Reed Solomon intersection matrix common intersection polynomial factor affine transformation evaluation points five codewords`
- `"Reed-Solomon" "intersection matrix" "scaling"`
- `"Reed-Solomon" "65537" "five" list decoding`
- `Reed Solomon codes automorphism affine evaluation scaling primary theorem`
- `"Reed-Solomon" "59" "five" "subgroup"`
- `"intersection matrix" "consecutive" "Reed-Solomon" subgroup`
- Official-Mathlib searches for `eval_comp`, `natDegree_comp` and common-root divisibility.

No inspected result gives the exact changed statement. The automorphism
search returned Dür's *The automorphism groups of Reed–Solomon codes*
(1987) and Joyner–Ksir–Traves, arXiv:0801.4007; their theorem statements
and proofs were not read or used. A secondary affine-equivalence article
was a lead only. The elementary primary composition declarations above
cover the essential change-of-variable tools, so those classification
leads are unnecessary for this bounded attempt. No novelty conclusion
follows from unsuccessful exact searches.

The scoped duplicate check read the full L040 proof/audit and the fixed
assessment, the relevant L031 proof and C001a statement, L034's exact
60-core hypotheses, the five-support working notes and histories 104–107.
Neither L040 nor those records completes this extension. L031's arbitrary
core/private conclusion concerns four supports and is supporting
methodology, not the five-support premise. The inspected stops in
ATTEMPTS/019–021 forbid further strengthening of the unchanged old local
model; ATTEMPTS/023 and 025 refute specific auxiliary cubic families;
ATTEMPTS/024 stops a stricter anchored-neighborhood cap. They neither
decide this target nor justify reopening those mechanisms.

## Ready continuation and bounded test

One later REPRODUCTION proof attempt is covered by SPECIALIZE, with exact
scope in [the continuation assessment](2026-10-08-five-support-uniform-extension-proof.md).
Use L040's audited unshifted full-rank input; no repeated elimination or
enumeration of 1024 shifts is needed to reassess the existing certificate.
The later proof must verify the transported signed equations for every
s in H, the arbitrary-core division and private-point incidence hypotheses,
and equality row by row over F for every m. Do not assume the core or
private points are shifts of the original choices. Do not assume tuple
descent, a distinguishing scalar projection or arbitrary-label rank symmetry.

Continue if all those universal claims can be proved from the imported
tools and audited input. Abandon or narrow the proposed extension if a
valid counterconfiguration appears; if a proof obligation remains
inconclusive, save it explicitly without claiming the extension. No
59-core family transfer, useful cardinality cap, cross-core consistency,
large common-center realization, 67/68 safety or ABF equivalence is
established. This review is EXPLORATION in source comparison, not a
mathematical advance. No lemma, script or rank certificate was written
or verified in step 109. The new ready continuation receives the
supervisor's separate approval next turn.
