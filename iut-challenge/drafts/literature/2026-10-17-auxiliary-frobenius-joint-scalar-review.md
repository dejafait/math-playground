# Auxiliary Frobenius condition — completed source review

TARGET: Assess whether one auxiliary good-reduction Frobenius condition can force L072's joint scalar within L046/L048's approximation family while preserving the local 210-torsion and mod-7 requirements.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step284 searched good-reduction torsion/Frobenius, trace-zero scalar powers, explicit j=0 reductions and fixed-level image exceptions; compared L046/L048/L072, step280's intersection assessment, step281 and ATTEMPTS/027,028,031,032. No local auxiliary-prime certificate was found. Searches do not establish novelty.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), II.6 Corollary 6.2/proof pp.70–71, IV.9 Theorem 9.4/proof p.150, V.7 (46)/Proposition 7.5 p.217 and V.8 Propositions 8.1/8.3 and reduction proofs pp.220–221; Zywina, author-hosted 15-page MaximalGalois.pdf, section 1.1 pp.1–2, Definition 5.1 p.6 and Proposition 5.7/proof p.8; MIT 18.783 Spring 2019 Problem Set 1, Problem 5(a), p.4. Exact theorem/proof passages read, with Zywina's deeper sieve coverage reused from the existing L046 assessment.
COMPARISON: Primary reduction/Frobenius and endomorphism identities cover the scalar-power mechanism; L046 already supplies the fixed-level exceptional bound and coordinate/count framework. Neither source proves the extra congruence-family specialization or decides the already selected E_0. An exact finite point count can replace inaccessible supersingular-classification leads.
GAP: No p=89 point count, scalar-power congruence certificate, G_K fixing check, nonempty refined coefficient lattice or preservation proof has been executed. The retained E_0's joint image, native descent, exact generation and original finite B>=A remain unknown.
REASON: Essential source coverage for one concrete prospective test is now available. Derive only the explicit finite-field/congruence/family specialization in a separately approved mathematical step; import the general theorems without reproof.
SCOPE: Prospective refinement of L046's fixed-c two-parameter family at fixed M>=max(M_tors,31), using p=89 and reduction y^2=(x+c/3)^3+1 over F_89. Existing E_0,F,K_glob and every retained global field stay unchanged; any witness uses new curve-dependent notation.
LITERATURE_REASON: Step283 proposed this distinct actual-occurrence mechanism; prior Yelton/intersection coverage supplied only a conditional consequence and lacked good-reduction Frobenius coverage.

## Gap, relevance and decision test

The [official announcement dated 2023-07-07](https://zen.ac.jp/news/0ul6zqed9-0)
was rechecked on 2026-10-17, including its Challenger Prize statement
and judging/publication paragraphs. Its inherent-flaw scope matches
foundations/01; prize adjudication remains separate from correctness.

The main gap is still the original finite B>=A comparison. The
intermediate target is an occurrence mechanism for the joint scalar
in L072, inside a prospective refined approximation family. Its
possible downstream use is a qualified family witness for failure
of all six L071 ordered-root models' full-15-torsion tests. This
would not decide the unchanged retained curve, identify native T,
prove exact field generation or establish an essential IUT flaw.

The proposed concrete reduction is p=89 with

    y^2=(x+c/3)^3+1 over F_89,

where c is L046's already fixed integer quadratic coefficient and
3 is inverted only in this finite field. This is a test specification,
not a verified reduction for any existing curve. The separate attempt
must check nonsingularity and exact point count, the Frobenius-square
matrix on all E[120], its restriction to the precise K, and existence
of a full-rank congruence subfamily surviving the mod-7 exceptional
bound. Continue only if all these checks pass. Abandon this specified
condition if the scalar/fixing test fails or the family has no positive
two-dimensional leading count. No such pass or failure is asserted now.

## Primary inputs and exact hypotheses

[J.S. Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II.6 Corollary 6.2, printed pp.70–71, gives an actual quadratic
endomorphism identity; IV.9 Theorem 9.4's proof, p.150, identifies
the Frobenius polynomial by degree and rational point count.
V.7 (46)/Proposition 7.5, p.217, give determinant and trace on the
prime-to-characteristic Tate module. V.8 Propositions 8.1 and 8.3,
pp.220–221, identify unramified torsion and arithmetic Frobenius
with the reduction action for a Q-curve at a good prime p, with
Tate prime different from p. Their complete relevant reduction
arguments were read. Use the actual identity or Cayley–Hamilton,
rather than identifying a matrix with a scalar from its trace and
determinant. Here the prospective level is 120; its prime factors
must all be different from the chosen reduction prime. The finite
point count and its application to the proposed cubic remain future
work, not imported as an already proved p=89 example.

[David Zywina, Elliptic curves with maximal Galois action on their
torsion points](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
Bull. London Math. Soc. 42 (2010), 811–826,
[DOI 10.1112/blms/bdq039](https://doi.org/10.1112/blms/bdq039),
author-hosted 15-page version retrieved 2026-10-17. Section 1.1,
pp.1–2, defines the nonsingular integral coefficient boxes and
states det rho equals the cyclotomic character. Definition 5.1,
p.6, and Proposition 5.7/proof, p.8, give the fixed-level bound
for failure of SL_2 containment, including k=Q. Reuse L046's
prior assessment for the sieve inputs and Q-case full-image criterion.
Theorem 1.3's exclusion of Q is not a restriction on Proposition 5.7.
No theorem asserts the extra congruence subfamily is nonempty: that
is the new applicability obligation. Keep M and auxiliary modulus
fixed in the growing real box; do not claim uniformity in either.

The [MIT 18.783 Spring 2019 Problem Set 1](https://math.mit.edu/classes/18.783/2019/ProblemSet1.pdf),
Problem 5(a), p.4, was inspected as a primary pedagogical lead for
y^2=x^3+1 and vanishing Frobenius traces. It asks for a criterion;
it supplies no proved trace formula used here. A finite exact count
at the single proposed prime is an independently checkable alternative.

## Access limits, duplicates and specialization obligations

Galbraith's author-hosted extended chapter 9 and exercise solutions
were located at https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch9.pdf
and https://www.math.auckland.ac.nz/~sgal018/crypto-book/solns.pdf.
Indexed extracts suggest Exercise 9.10.4 and its solution, but subsequent
passage retrieval timed out; screenshot responses exposed no readable
image, and shell download failed DNS. Treat these as UNREAD LEADS,
not theorem evidence. The author's book page warns that extended
numbering differs from the printed book. Do not repeat access attempts
or depend on a general supersingular classification for the finite test.
This is not an essential source blocker for the inspected general
Frobenius theorem plus an elementary exact point count.

L046 already establishes the unrefined affine-lattice count and
imports the exceptional bound O(R^(3/2) log R). L048 retains the
original cubic precision and the changed Tate parameter valuation.
The new work must impose the auxiliary condition on that original
fixed-c family, before transporting to short coefficients; display
the full-rank sublattice and its positive quadratic leading count.
CRT alone is neither a scalar-occurrence theorem nor the required
counting comparison. No generic adelic-surjectivity or Chebotarev
existence theorem is needed for this proposed approach.

For any prospective witness use E_aux, K_aux=Q(zeta_60,E_aux[2])
and F_aux=K_aux(E_aux[15]); K_aux is not native K_glob. Show one
and the same arithmetic Frobenius lift has a power with both torsion
actions, fixes zeta_60 and all full-coordinate E_aux[2], and hence
belongs to G_(K_aux). Marginal images alone do not suffice. Any
later use of L071/L072 must explicitly apply their statements to
that witness, not substitute new fields for the retained F silently.
Reapply L044/L045/L046/L048 as required to retain the full local
210-torsion, embedded H,N and v_3(q_aux)=30; do not assert equality
q_aux=q_0 or identity of old and new global fields or places.

Essential inputs for the continuation are L044,L045,L046,L048,L071,L072.
ATTEMPTS/027 (exact-curve globalization), 028 (broad model reading),
031 (unverified marked coordinates) and 032 (surviving native enclosure)
are preserved. None supplies or forbids this separate auxiliary test.
Independent initial data, native T/model, exact generation, marked
all-image factorization, pilot transport and essentiality remain open.

The prepared exact continuation is recorded in
`2026-10-17-auxiliary-89-frobenius-family-test.md` for separate
next-turn approval. No new lemma, calculation, mathematical script,
PROOF.md argument or DAG edge was written. Full matching/supporting
Mathlib coverage is unchecked, not absent. This is source coverage
and a concrete test proposal, with no result beyond the checked sources.
