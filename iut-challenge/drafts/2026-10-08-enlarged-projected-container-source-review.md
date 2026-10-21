# Enlarged projected-container homothety — completed source comparison

Literature-only review of the exact target in
`literature/2026-10-08-enlarged-projected-container-homothety.md`.
No projected-lattice verdict or new theorem has been derived.

The primary gap remains the original finite B>=A comparison. The bounded
intermediate target asks whether any primitive line of the genuine M
makes the images of C and M scalar-homothetic in the same rational quotient.
A negative answer could support a later invariant-container test for the
actual source line; a positive answer stops the line-independent shortcut.
Actual inputs/actions, fixed-line control, numerical application and
global/pilot compatibility remain independent gaps.

## Local checks completed

Read L031's hypotheses, exact field model and complete-basis conclusion,
L032's hypotheses and integral trace-kernel conclusion, and the reused
stable-lattice-source passage in the quotient review. The basis matrix is
the complete 108-column Z_3-basis, not an O_U-basis. No determinant or
projected numerical conclusion follows just from the recorded covolume.

Targeted searches of the relevant October 6–8 assessments, histories and
ATTEMPTS/022–024 found supporting Smith-normal-form/intersection-lattice
coverage, but no completed existential projected-homothety test.
ATTEMPTS/024's whole-kernel stop persists. No sibling notebook was read.

## Discovery and primary source evidence

Initial queries: `invariant factors quotient lattices common line interlacing
discrete valuation ring`; `Thompson 1979 invariant factors rank one
perturbation interlacing theorem`; `p adic lattices projection quotient line
homothetic elementary divisors`.

Additional queries: `"Nonarchimedean integral geometry" Bürgisser Kulkarni
Lerario arxiv`; `"invariant factors" "submatrix" "Thompson" interlacing`;
`"lattices" "quotient" "homothetic" "line"`; `"lattices" "elementary
divisors" "projection" homothety`. These found general tools, not an
inspected result deciding the exact field/lattice pair. This is not a claim
of novelty. Search snippets, forums and unrelated complex-lattice results
are not mathematical inputs. An incorrectly entered arXiv identifier
2206.01074 opened an unrelated paper; it supplies no evidence.

**Simultaneous normal form.** Read John Voight, *Quaternion Algebras*,
Springer GTM 288 (2021), chapter 9, section 9.2 setup and section 9.3,
Definitions 9.3.1/9.3.3, Lemma 9.3.5 with proof, Theorem 9.3.6 with proof,
and **Theorem 9.3.9** ([primary chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_9),
DOI 10.1007/978-3-030-56694-4_9), inspected 2026-10-08.
For two full lattices over a Dedekind domain in the same fraction-field
space, Theorem 9.3.9 supplies a common pseudobasis and unique ordered
relative fractional-ideal factors. The book refers to O'Meara, 81:11,
for that theorem; O'Meara was not read. Here the scalar ring is Z_3,
a DVR/PID, and the ambient space is V over Q_3. Neither nesting of C and
M nor O_U-linearity is required. The author-hosted full-book URL failed;
the primary chapter statement was accessible. No reproof is needed.

**Quotient and interlacing tools.** Read Peter Bürgisser, Avinash Kulkarni
and Antonio Lerario, *Nonarchimedean integral geometry*, Selecta
Mathematica **32, article 10 (2026)**, published online **5 January 2026**,
[version of record](https://doi.org/10.1007/s00029-025-01120-y)
and [84-page primary publication PDF](https://d-nb.info/1395945926/34).
Inspected section 2.1's scalar setup; **section 2.2**, pp. 13–14;
**Definition 3.1.1, Lemmas 3.1.4(1–3)/3.1.5**, pp. 21–23;
**Propositions 4.1.1/4.1.2**, pp. 35–36, including both minimax proof
cases and the complete interlacing proof. Lemma 3.1.4's proof is left
to the reader; Lemma 3.1.5 has its Smith-form proof. For a local scalar
field and full lattices, subspace intersections and quotient images are
full lattices. For a linear map, quotienting its target by a d-dimensional
subspace gives singular values satisfying

    sigma_i >= sigma''_i >= sigma_(i+d).

The proof treats restriction by minimax and passes to quotient by duality.
Only this quotient assertion, with d=1, is needed. These are absolute
Smith factors for lattice norms, not the field norm on L.

The proof's reference to its own Proposition 4.1.2 for the minimax formula
is a numbering mismatch: the displayed formula is Proposition 4.1.1.
Corollary 4.1.3 concerns simultaneous row and column deletion and is not
imported. No correction or new theorem about that corollary is attempted.

**Independent standard comparison, not an additional premise.** Read
Eduardo Marques de Sá, *On the diagonals of integral matrices*,
Czechoslovak Mathematical Journal **30 (105) (1980), 207–212**,
the PID setup on p. 207 and the stated submatrix criterion **(3)–(4)**
on p. 208 ([primary publication](https://dml.cz/bitstream/handle/10338.dmlcz/101672/CzechMathJ_30-1980-2_4.pdf)).
The criterion for deleting p rows and q columns is
alpha_i divides beta_i divides alpha_(i+p+q), with zero tails.
It is attributed to earlier papers, not proved there. Its one-row case
is relevant; it does not decide the common-line question in our field.
The paper's separate triangular-diagonal proof is outside this target.
R. C. Thompson, *Interlacing inequalities for invariant factors*,
Linear Algebra and its Applications **24 (1979), 1–31**,
DOI [10.1016/0024-3795(79)90144-7](https://doi.org/10.1016/0024-3795(79)90144-7),
was inspected at publisher abstract only, not theorem/proof level.
It and the earlier Sá paper remain unread leads. Endomorphism similarity
invariants must not be substituted for Smith factors over Z_3.

## Applicability and the remaining specialization

The scalar field in the inspected lattice theorems is Q_3, not L.
L031 supplies the complete full lattices J_L and O_L in L; L032 supplies
the rank-107 full M in V. The cited subspace theorem covers C=O_L intersect
V and the two rational-quotient images. A later calculation must use the
actual trace kernel and complete matrix, not the determinant alone or a
sampled logarithm span. Primitivity of F must be retained when identifying
the integral quotient with M/F. No field valuation is put on that quotient.

For Proposition 4.1.2 the proposed map is the identity from the copy of V
with domain lattice C to the copy of V with target lattice M. Its target
subspace is Q_3 F and its target quotient lattice is q_F(M). A subsequent
research turn may apply the cited inequality to the projected map and test
compatibility with scalar homothety. No hypothesis requires the identity
to map C into M; section 2.2 permits negative Smith exponents. All
106 nonzero projected factors must be accounted for. This review does not
derive a necessary-and-sufficient existential-line criterion or calculate
any of the relative factors for this pair.

The essential difference from the sources is the exact pair C,M and the
common rational line, including possible sufficiency and construction if
an interlacing obstruction does not settle nonexistence. A necessary
inequality passing is not an existence proof. A positive result requires
one primitive F and an exact same-space equality of full projected lattices;
a negative result must exclude every primitive line and every scalar.
If the necessary test passes and no verified construction is available,
save that precise unresolved obligation rather than assert a verdict.

Reuse Sehanobish section 3.1, Corollary 3.1.9, pp. 26–28 and Stacks 00DV
with the inspection qualifications in the prior quotient source review.
They are not essential to this target's lattice calculation. Any later
stable-lattice application uses the actual fixed line Z_3 y_1, L033's
residual action, and full bounded closed quotient lattices; compactness
and same-space scalar homothety must be checked. An arbitrary primitive
line is not asserted to be source-realizable or Gamma-stable.

## Scope, decision and next invocation

Coverage is **SPECIALIZE** for exactly the saved target. The known normal
form, full quotient-lattice and quotient-only interlacing inputs suffice
for a bounded exact-lattice test in a separate research invocation.
Only their field-specific application and any required common-line
argument are approved; a short specialization would be **REPRODUCTION**,
not a new discovery. No new lemma, calculation, mathematical script or
projected-homothety verdict has been produced in this literature turn.

Essential continuation inputs are L031 and L032; L033 motivates downstream
use only. Preserve ATTEMPTS/022–024, no O_U-linearity, no prescribed y_1,
no extra shear/exponent twist and no converse presentation realization.
Negative existence supports later projected-container noninvariance;
positive existence stops that presentation-independent shortcut and leaves
the actual line to be determined. Fixed-line and numerical control,
actual/native input/action compatibility, packet/global realization,
pilot transport, essentiality and original finite B>=A remain open.
Full matching and supporting **Mathlib coverage are not checked**.

The [original announcement](https://zen.ac.jp/news/0ul6zqed9-0), dated
7 July 2023, and the [current English prize page](https://zen.ac.jp/en/lp/icp)
were accessed 2026-10-08 at the substantive prize passages. The former
retains the inherent-flaw requirement; the latter specifies an essential
flaw. These match the existing challenge scope; adjudication remains
separate. No shared infrastructure or argument overview was changed.
