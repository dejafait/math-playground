# L072 — Conditional joint scalar excludes the retained Legendre radicals

## Hypotheses

Retain L071's same nonsingular monic cubic E_0/Q: y^2=g(x),
ordered roots r_1,r_2,r_3 in the retained Q-bar, and fields

    K=Q(zeta_60,r_1,r_2,r_3), F=Q(zeta_60,E_0[30])=K(E_0[15]).

Here K is not the native field K_glob. Put a=r_2-r_1 and
b=r_3-r_1; the three differences a,b,b-a are nonzero. Use full
point-coordinate division fields and the retained embeddings. Keep
all of L045/L048's curve choices, M>=max(M_tors,31), completions
H,N, places u,w and changed q_0 with v_3(q_0)=30 unchanged.

Let rho_(E_0,120) denote the actual torsion representation of G_K.
Assume, conditionally, that its image contains the element whose
actions on E_0[8] and E_0[15] are respectively -Id and Id.
These actions specify an element through the coprime decomposition
of the 120-torsion module; occurrence in the actual image is an
additional hypothesis, not a consequence of CRT. Scalar actions
are independent of the choice of torsion bases.

## Conclusion

Under this extra image hypothesis, none of a,b,b-a is a square in F.
Equivalently, none of K(sqrt(a)), K(sqrt(b)), K(sqrt(b-a)) is
contained in L071's J=K(E_0[4]) intersect F. Consequently none of
L071's six specified ordered-root Legendre F-models has all of its
geometric 15-torsion F-rational, or is pointed F-isomorphic to E_0.

This conditional implication does not establish its image hypothesis
for the retained curve. It gives no unconditional membership verdict,
no counterexample under the retained hypotheses alone, no native
T/model identification, no exact-generation result and no IUT flaw
or original finite B>=A conclusion. The separate step 283 critical
audit below validates this conditional implication only.

## Proof

### Imported theorem and applicability

Use the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-scalar-120-radical-test.md`.
Import Jeffrey Yelton, *A note on 8-division fields of elliptic curves*,
[arXiv:1704.06190v2, 2 August 2017](https://arxiv.org/pdf/1704.06190v2),
degree-three definitions on printed p.1 and **Theorem 1(a),(b),
pp.1–2**. For a monic separable cubic over any field of characteristic
different from two, define cyclic radicals A_i by
A_i^2=r_(i+1)-r_(i+2). Part (a) places them in the full 4-division
field. Part (b) implies that any Galois element acting as -Id on
the 8-torsion sends each A_i to its negative. We use this part of
the theorem only; its further assertions about other generators
are unnecessary. No generic surjectivity proposition is imported
or reproved.

The base field here is the actual number field K, of characteristic
zero. L071 retains the same nonsingular monic cubic, so its three
roots are distinct and the degree-three theorem applies after base
change to K. In fact all roots already lie in K. Choose the source's
primitive fourth root to be i=zeta_60^15 in K and choose a primitive
eighth root above it in Q-bar if needed for its notation. Containment
of that eighth root in K is not a theorem hypothesis. No independence
of the A_i, or nontriviality of their individual extensions, is assumed.

### One actual fixing element

By the image hypothesis there exists sigma in G_K with both
rho_8(sigma)=-Id and rho_15(sigma)=Id. This is one element, not two
independently chosen lifts from marginal images. The second equality
means that sigma fixes each geometric 15-torsion point and therefore
both coordinates of every such point. It also fixes K. Since L071
identifies F exactly with K(E_0[15]) inside this Q-bar, sigma fixes F
pointwise: sigma belongs to G_F. This uses the full-coordinate
pointwise kernel, rather than preservation of the torsion set or
x-coordinates alone.

Apply Yelton's theorem to this same sigma and to roots ordered as
r_1,r_2,r_3. Choose the radicals in Q-bar. Their squares are

    A_1^2=r_2-r_3=-(b-a),
    A_2^2=r_3-r_1=b,
    A_3^2=r_1-r_2=-a.

The theorem gives sigma(A_j)=-A_j for j=1,2,3. Since sigma fixes i,
the elements

    s_a=A_3/i, s_b=A_2, s_(b-a)=A_1/i

have squares a,b,b-a respectively and each satisfies
sigma(s_c)=-s_c. They are all nonzero. If any s_c belonged to F,
pointwise fixing of F would give s_c=-s_c, impossible in
characteristic zero. Hence none of these chosen roots lies in F.
The only other root of each polynomial X^2-c is -s_c, and it
belongs to F exactly when s_c does. Thus none of the three c is
a square in F. In particular if one were already a square in K,
this would contradict the conditional image hypothesis rather than
invalidate the argument or require defining a nontrivial character.
Coincidences between quadratic extensions likewise cause no issue.

L071 puts each K(s_c) in R=K(E_0[4]) and identifies membership in
J=R intersect F with being a square in F. Its six-row criterion
then gives the stated failure for every row: each of the three
classes occurs twice, and every row passes precisely when its
class is trivial. We do not infer independence, [R:K]=8, or an
exact value of J from the simultaneous negation.

### Relevance and limits

The fixed-group and three-sign checks pass the continuation test.
The proof is an applicability argument for the imported general
theorem, not a reproof of its braid or generic calculations. It
provides local conditional progress beyond L071's unevaluated tests,
with no claim of progress beyond the checked mathematical sources.
A future independently verified actual joint-image certificate could
activate this sufficient test. An abstract matrix, determinant
compatibility, separate marginal images or agreement at one completion
would not supply that certificate. Exact coefficients and actual image
generators remain unavailable. Native descent, minimal generation,
independent initial data, source-marked all-image factorization,
pilot transport, essentiality and the original finite B>=A remain open.
ATTEMPTS/027,028,031,032 and unfinished work are preserved.

### Separate critical audit — 2026-10-17, step 283

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-joint-scalar-critical-audit.md`.
This audit tests the specialization, importing Yelton's general theorem
at the precise citation above. It does not reprove the theorem or
assess an actual image. The direct mathematical input remains L071;
its retained L045/L048 conventions have been checked without changing
the curve, fields, embeddings or approximation precision.

**Theorem applicability.** The displayed equation remains monic of
degree three over the number field K, with distinct roots. Thus its
characteristic is zero and it satisfies the degree-three setup of
Theorem 1. Theorem 1(b) is stated for an actual G_K element with
the specified mod-eight action; it is not restricted to a generic
curve. The primitive eighth root in that setup is chosen in the
algebraic closure, not required in K. We can choose it with square
i=zeta_60^15, since a square root of an order-four element has order
eight. Theorem 1(a) puts all A_j in the full 4-division field.
No independent-radical or maximal-image hypothesis has been added.

**One lift and the exact fixing field.** Coprime torsion decomposition
identifies E_0[120] with the direct sum E_0[8] plus E_0[15] equivariantly.
The additional hypothesis is membership of the specified pair in the
actual joint image, so its definition supplies a single sigma in G_K
with both prescribed actions. Two separate marginal-image statements
would not do this. Identity on the full 15-torsion means pointwise
fixing of both coordinates. L071's equality F=K(E_0[15]) therefore
puts this very sigma in G_F. Conversely, an element of G_K fixing F
acts trivially on E_0[15], so the fixing condition is exact. Neither
setwise stabilization of F nor x-coordinate rationality is substituted.

**All cyclic and row signs.** The fixed fourth root has i^2=-1 and
sigma(i)=i. Hence the cyclic definitions give

    (A_3/i)^2=a, A_2^2=b, (A_1/i)^2=b-a.

Each element is nonzero and is negated by the same sigma, by Theorem
1(b). The following explicitly checks every signed row difference;
the chosen root in the third column is negated in every row.

| Ordering | d_ij | Chosen square root of d_ij |
| --- | --- | --- |
| (1,2,3) | a | A_3/i |
| (1,3,2) | b | A_2 |
| (2,1,3) | -a | A_3 |
| (2,3,1) | b-a | A_1/i |
| (3,1,2) | -b | i A_2 |
| (3,2,1) | a-b | A_1 |

For example (i A_2)^2=-b and sigma(i A_2)=-i A_2;
the other negative differences are already cyclic squares. Changing
any chosen radical to its negative preserves its transformation rule.
No nonzero radical in this table can lie in F, because sigma fixes F
and characteristic zero excludes s=-s. If its radicand had another
square root in F, that root would be s or -s, again a contradiction.
The field-containment equivalence follows from K(s) subset R together
with K subset F: containment in R intersect F is precisely containment
in F. This uses actual embedded fields, not just isomorphism classes.

**Trivial and dependent cases.** If one radical is already in K, or
becomes rational over F, its being both fixed and negated rules out
the extra image hypothesis. It does not expose an exception to the
conditional implication. Equal quadratic classes also cause no conflict:
when s_1=t s_2 for t in F, simultaneous negation preserves that
relation. More generally, for any product P of the three nonzero
chosen radicals with exponents epsilon_j in {0,1}, multiplicativity
gives sigma(P)=(-1)^(sum epsilon_j) P. If P is in F and the sum is
odd, the image hypothesis is impossible; if the sum is even, the
relation is respected. This includes dependencies that would preclude
simultaneous negation, rather than assuming those dependencies absent.
The argument does not require or conclude that R/K has degree eight.

**Every row consequence.** L071's audited criterion applies to these
same six models. Its nonexceptional-j hypothesis comes from the
retained v_3(j)=-30, excluding both 0 and 1728. For each row the
comparison map uses the radical in the table, up to sign. On a basis
of the row's 15-torsion transported from E_0[15], this sigma acts as
-Id: it fixes the original points and negates the comparison radical.
It moves each transported basis point, whose exact order is 15.
Thus every row fails full F-rational 15-torsion. L071's equivalence
also excludes pointed F-isomorphism for every row; an alternative
pointed comparison cannot remove the nontrivial quadratic character.

**Verdict and scope.** The conditional statement passes this separate
audit with no correction to its hypotheses, conclusion or DAG row.
The explicit six-row signs and dependency checks complete the stated
test. This is validation of a known-result specialization, not an
unconditional radical verdict or a new theorem beyond the checked
sources. Actual scalar occurrence and the exact intersection remain
unestablished. Native T/model, exact generation, independent initial
data, source-marked all-image factorization, essentiality and the
original finite B>=A gap remain open. No completion calculation,
generic image, new coefficient choice or field enlargement replaces
those missing inputs. ATTEMPTS/027,028,031,032 remain unchanged.

## Mathlib

Full matching and supporting Mathlib coverage of this conditional
joint-image/radical specialization has not been checked. No absence
or formal-verification claim is made. The cited general theorem is
imported; the same-element fixing and sign specializations are written
out above. No numerical evidence or mathematical script is used.
