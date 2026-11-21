# Simplex-majorization discriminator — source coverage completed in step55

TARGET: Assess source coverage for a Schur-concavity obstruction test of L938's fully symmetrized twelve-factor polynomial on the positive energy simplex.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step55 searched the exact coefficient 371319795000 with Schur-concavity, Schur-concavity with Hankel determinants/Newton sums/cosine cumulants, and symmetric-polynomial majorization criteria; no inspected result settles this exact polynomial. Scoped local checks and L915/L916/L937 plus the fixed-cell stop show different objects. Search failure is not novelty evidence.
SOURCE_EVIDENCE: Inspected Ostrowski (1952), section II no.12 and section III Theorems VII-VIII/no.17-21, pp262-263,268-272; corroborated the OCR-missing derivative formula with Klemes arXiv:1002.3938v2 section3 equation(9), pp13-15, and Tao (6 August 2017), Theorem1/proof including its general criterion argument. Inspected Klemes's nearby index-set theorem and examples; sources and access qualifications below.
COMPARISON: The standard criterion validates the proposed algebraic discriminator for a smooth symmetric polynomial. The inspected positive index-set families and complete homogeneous polynomials do not settle the signed 34-row combination. L939 is tail-only; neither it nor the stopped contact/score/cell mechanisms supplies the proposed global order input.
GAP: The exact pairwise derivative sign, normalized symmetrization identity and actual-theta ordering/finite-energy variation implication are unproved. No inspected source gives their conclusion for this polynomial; the next bounded algebraic attempt may fail without resolving any analytic transfer.
REASON: Essential source coverage is now adequate for one exact obstruction test, retaining the original research target. This literature-only step performs no symmetrization, derivative evaluation, new lemma or mathematical script; newly changed ready coverage remains subject to the supervisor's separate approval.
LITERATURE_REASON: Changed target from a variable-data Laplace tail audit to a global symmetric-polynomial order test; essential majorization theorem coverage is missing.
SCOPE: Covers the source review and the single bounded algebraic test specified below; preserve all 34 rows, twelve factors, factorials and M_0^12 normalization. No compact-cell refinement, degree sweep, score-correction relaxation, effective tail-onset calculation or theta-ordering proof is covered.
COVERED_TARGET: Test L938's fully symmetrized twelve-factor polynomial for a Schur-Ostrowski obstruction on the positive energy simplex.

## Original proposed mechanism, retained with the step55 source comparison below

Use the labelled homogeneous polynomial P of L939(4), which is the
polynomial from L938's exact density. Define the candidate symmetric
polynomial Pbar as the arithmetic average of P over the twelve label
permutations. The proposed domain is t_i>0, sum t_i=1. Before any
research, inspect a primary version of the Schur-Ostrowski criterion
and check its domain/differentiability hypotheses. Also verify whether
existing symmetric-polynomial results already settle this exact Pbar.
Do not replace arithmetic averaging by summing permutations, which
would change the normalization. Integral preservation and any use of
majorization must be justified, not assumed from a suggestive name.

The proposed first mathematical discriminator is the exact inequality

    (t_i-t_j)(partial_i Pbar(t)-partial_j Pbar(t)) <= 0

throughout the positive simplex for all i,j. An exact positive value
at one rational interior tuple would abandon this global
Schur-concavity sufficient mechanism. A proof or a matching known
result would retain only this intermediate input. There is no claim
that the inequality is true, or that checking finitely many tuples
would prove it. No symmetrized polynomial or derivative was computed
in step54.

The plausible downstream use is to compare the signed amplitude under
more-balanced simplex distributions as energy grows. A successful
algebraic test would still need an actual-theta ordering theorem,
normalization and a rigorous implication for finite-energy variation.
Neither ordinary log-concavity nor L939's eventual concentration alone
supplies that theorem. This independent missing step is explicit; it
need not be solved to make the algebraic discriminator informative.
The central L030–L032/C032a all-degree gap is further away: H2 variation
alone does not provide endpoint signs, contacts, other degrees,
initialization, realization or global continuation.

## Scope comparison and routing purpose

L915's stop is conditional multiple crossing of a one-variable contact
residual; L916 refutes convexity of an inverse score. L937 excludes a
fixed degree-eleven score correction on a finite relaxation. The
fixed-cell stop in `ATTEMPTS/2026-11-09-actual-h2-fixed-energy-cell-inconclusive-48.md`
precludes simply refining that experiment without a new mechanism.
The proposed object is instead an exact symmetric polynomial on an
eleven-dimensional simplex; the earlier stops remain intact. These
comparisons do not substitute for the next source review.

The source review should decide whether this concrete discriminator
is already settled, viable for a bounded attempt, or mismatched to
the proposed downstream use. If it prepares a genuinely new mathematical
attempt, its purpose is creative: finite-energy sign variation is the
obstruction, and the exact pairwise derivative sign or counterexample
is the decisive test. Immediate creative invocation is blocked by the
missing coverage, not by a quota or by the completed tail audit.
No proof-purpose routing is asserted for the present literature target.

Essential local inputs for that review are L938 and L939; consult the
stated L915/L916/L937 stops only for comparison. No cross-notebook
input, Decimal premise or BKR access is required. Mathlib coverage for
the proposed criterion and its specialization is unchecked.

## Step55: inspected primary criterion and its scope

Alexandre Ostrowski, *Sur quelques applications des fonctions convexes
et concaves au sens de I. Schur*, Journal de mathematiques pures et
appliquees, series 9, 31 (1952), 253-292,
[original article](https://www.numdam.org/item/JMPA_1952_9_31__253_0.pdf).
Section II no.12 (pp262-263) defines the product domain D_J for an open
interval J and the doubly stochastic order. Section III Theorem VII,
no.17 (p268), assumes symmetry and continuous first partial derivatives
on D_J and gives the necessary and sufficient pairwise derivative
criterion for Schur-convexity; applying it to the negative function
gives Schur-concavity. The proof (pp268-272) treats binary mixing for
necessity, strict sufficiency via Theorem VIII and block decomposition,
then removes strictness by a positive quadratic perturbation. These
are inspected source arguments, not a new local proof.

The extracted text omits formula (48), and screenshot calls exposed no
usable image content (two also timed out). Its exact modern formula
was therefore checked in the next two sources rather than guessed
from OCR. The two repository copies of Marshall-Olkin-Arnold timed
out; Springer's chapter page exposed only metadata/abstract. That
book's theorem numbering is not claimed to have been directly read.
These access failures do not block this test because the original
theorem hypotheses/proof and independent readable formula are available.

Ivo Klemes, *Symmetric polynomials and l^p inequalities for certain
intervals of p*, [arXiv:1002.3938v2](https://arxiv.org/pdf/1002.3938v2),
9 January 2011, section3, pp13-15, equation (9), states for smooth
symmetric Phi the Schur-concavity condition

    (partial_i Phi-partial_j Phi)/(x_j-x_i) >= 0,  x_i != x_j.

The same section's Theorem A reproduces Proschan-Sethuraman:
for a downward-closed index set S under majorization among nonnegative
integer vectors of a fixed sum, H_S(x)=sum_(p in S) product_i x_i^p_i/p_i!
is Schur-concave on the nonnegative orthant. Examples1-2 use capped
exponents or a minimum support size. This is a sufficient structured
family, not a theorem for arbitrary signed combinations. No matching
representation of the L938 object is established here. The original
Proschan-Sethuraman source was not read and is not an essential input
to the obstruction test. Klemes's earlier
[arXiv:0806.2686v1](https://arxiv.org/pdf/0806.2686v1), section4 p11,
equation (18) and Proposition2, supplies the same nearby comparison;
no separate new conclusion is imported from it.

Terence Tao, *Schur convexity and positive definiteness of the even
degree complete homogeneous symmetric polynomials*,
[author's exposition, 6 August 2017](https://terrytao.wordpress.com/2017/08/06/schur-convexity-and-positive-definiteness-of-the-even-degree-complete-homogeneous-symmetric-polynomials/),
Theorem1(iii) and proof, gives the product-form derivative condition
with >=0 for Schur-convexity and proves the general C^1 symmetric
criterion by induction on dimension: permutahedron faces split into
lower-dimensional cases, and an interior point follows a balancing
direction to a face. His complete-homogeneous-polynomial identity (2)
is a different polynomial family. No equality or strictness clause
from the degree-zero case is needed or imported.

### Applicability and remaining proof obligations

The proposed object must mean the **average over all 12! elements of
S_12**, not an average over twelve selected permutations. In the next
attempt it is to be defined exactly by

    Pbar(t)=(1/12!) sum_(sigma in S_12) P(t_sigma(1),...,t_sigma(12)),

with P exactly L939(4), obtained from L938's table. This definition
falls within the criterion's polynomial/symmetry hypotheses; it does
not require nonnegative coefficients or positivity of Pbar. Distinguish
Schur-concavity under equal-sum vector majorization from ordinary
concavity, Schur-function expansion positivity, and weak majorization.
None of those substitutes is being approved.

For application to the fixed-sum simplex, the next proof must either
justify the relative-domain version using sum-preserving mixing or
justify passage to the positive orthant using the polynomial's
homogeneity. It must use ambient partial derivatives before restricting
to sum t_i=1; arbitrary derivatives in eleven eliminated coordinates
cannot simply be inserted in the displayed criterion. At equal
coordinates the product form has no division singularity.

Before claiming an implication for v(E), the next write-up must justify
preservation of L938's integral under each coordinate permutation:
retain its simplex measure, the symmetric weight product t_i^(-1/2)
K(sqrt(E t_i)), absolute integrability at all faces, and the factor
1/12!. The source criterion alone does not prove this integral identity.
An algebraic obstruction can be recorded independently of that later
analytic use, with this limitation explicit. These are applicability
requirements for future mathematics, not completed derivations today.

### One bounded test covered for the next research attempt

After the supervisor's separate approval of this changed assessment,
test only the exact rational two-block tuples with m coordinates
q/(m q+12-m) and 12-m coordinates 1/(m q+12-m), where

    m in {1,2,3,4,5,6},
    q in {1/16,1/8,1/4,1/2,2,4,8,16}.

For each of these 48 positive unit-sum tuples, use one coordinate in
each block to test

    D_ij=(t_i-t_j)(partial_i Pbar-partial_j Pbar).

The required obstruction threshold is **D_ij>0 exactly**. A rational
witness with complete row/multiplicity/factorial verification stops
this global Schur-concavity sufficient mechanism. No positive witness
in this bounded set is an inconclusive exploration, not a proof of
Schur-concavity and not permission to expand the grid or start a new
relaxation. Save any full certificate, all tested exact signs and
failed checks to disk; print only a concise result and its path.
Efficient orbit aggregation is permitted only with a proof that it
computes the full arithmetic average and its derivative. A floating
point screen, sampled sign or unsigned bound is not decisive evidence.

The plausible downstream use remains comparison of the signed amplitude
under more-balanced energy-simplex laws. Even a future proof of global
Schur-concavity would leave the actual-theta ordering of those laws
and its implication for finite-energy variation unpaid. L939 supplies
eventual positive tails, not this ordering. L915/L916/L937 and the
fixed-cell stop retain their original scopes and are not reopened.
The main L030-L032/C032a all-degree gap additionally retains signs,
contacts, other degrees, initialization, realization and continuation.

### Discovery record and Mathlib

Searches included "Schur Ostrowski criterion symmetric differentiable
function majorization Marshall Olkin Arnold theorem 3 A 4 pdf",
"Schur concavity symmetric homogeneous polynomial monomial symmetric
functions criterion signed coefficients", "Schur Hankel Newton sums
concavity polynomial", "Schur concavity Hankel determinant",
"Schur concavity cosine cumulants", and "Schur-concave 371319795000".
Sources inspected are distinguished above from search leads. Sra's
elementary/complete-symmetric ratio concavity paper and general Schur
expansion results appeared as unread leads; no identified statement
matches the signed L938 polynomial, and none is used as a premise.
This bounded search does not certify originality or exhaust all
possible symmetric-polynomial representations.

The local search of L9xx lemmas and November9 literature/ATTEMPTS found
no previous test of this precise Pbar; earlier majorization hits are
analytic domination. L915/L916/L937 conclusions and the fixed-cell
stop were read for comparison; their detailed proofs were unnecessary
to the source criterion. No cross-notebook input was read.

A targeted Mathlib documentation web search did not identify a full
matching Schur-Ostrowski theorem. Coverage remains **not established**;
this is not evidence of absence, and a queueboard lead is not a
merged theorem. No Lean result is an input to this step.
