# C040a — Uniform shifted five-support equality with arbitrary cores

## Hypotheses

Use C001a's E=F_65537, F=F_(65537^28), order-1024 subgroup
H<=E^*, k=64 and any integer m>=1. Use L040's generator h=19139.
Order the ten edges ij, 1<=i<j<=5, as
12,13,14,15,23,24,25,34,35,45, indexed by r=0,...,9.
For any common s in H put

\[
 U_{ij}=\{s h^{2r},s h^{2r+1}\}.
\]

Choose any C subset H of size 59 disjoint from all U_ij, and singleton
sets W_1,...,W_5 subset H mutually disjoint and disjoint from C and
all U_ij. Define

\[
 S_i=C\cup W_i\cup\bigcup_{j\ne i}U_{\min(i,j),\max(i,j)}.
\]

Let P_1,...,P_5 be polynomial m-tuples over F, with each row of strict
degree less than 64, and let Y:H -> F^m satisfy P_i(x)=Y(x) for
every x in S_i. The tuples need not be pairwise distinct; extra
agreements are allowed. Neither P_i nor Y need descend to E.
The choices C,W_i need not be shifts of L040's fixed choices.

## Conclusion

P_1=P_2=P_3=P_4=P_5 as polynomial tuples. Consequently these supports
cannot be selected agreement supports of five distinct candidates at
one center, for any stated s,C,W_i or tuple width m.

This is a necessary support restriction, not a family-size bound.
It leaves 955<=t_star(m)<=957 unchanged; no 59-core transfer, useful
cap, cross-core consistency, large RS list or 67/68-agreement safety
is established. The separate critical audit below retains the specialization
without a substantive correction.

## Proof

**Known inputs and reason for specialization.** Reuse the prior
[SPECIALIZE assessment](../drafts/literature/2026-10-08-five-support-uniform-extension-proof.md).
L040 supplies the audited signed unshifted 20-by-20 matrix M over E
and its inverse T, with TM=MT=I_20. Its fixed-core equality conclusion
alone is not applied to the new core: only this core-independent matrix
identity is imported. Its finite elimination and determinant audit are
not repeated here. C001a supplies the finite instance and threshold
qualifications.

The signed equality framework is Alrabiah–Guruswami–Li,
*Randomly punctured Reed–Solomon codes achieve list-decoding capacity
over linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/html/2304.09445v3#S2.SS3),
26 July 2023, Definition 2.5 and Lemma 2.7, printed pp. 7–8.
Import the common-root division proof step of Shangguan–Tamo,
*Combinatorial list-decoding of Reed–Solomon codes beyond the Johnson
radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Lemma 4.3, printed pp. 11–12. Only that factor-theorem
step is used, not its scalar decoding-radius conclusion or Section 5's
characteristic-two unsigned matrix. The supporting polynomial evaluation
and composition declarations are cited in Mathlib below. These inputs
cover the tools; the changed core and shift quantifiers require the
application proof that follows. This is REPRODUCTION of assessed tools,
without a claim of originality or a generic-rank reproof.

**Incidences and arbitrary-core division.** L040 establishes that h
has exact order 1024. Its twenty powers with exponents 0,...,19 are
distinct. Multiplication by s is injective and preserves H, so the
shifted U_ij are disjoint two-point sets. The assumed disjointness of
C and the five private points gives |S_i|=59+1+4*2=68,
S_i intersect S_j=C union U_ij, and every intersection of at least
three distinct supports equals C. Each private point has only one
owner. There are 1004 points outside the overlaps, so admissible core
and private choices exist; the argument below applies to every such
choice, not merely to one example.

Put G(X)=product_(c in C)(X-c) in E[X], also viewed in F[X]. It is
monic of degree 59. Fix any row a in {1,...,m}. All five P_i,a agree
with Y_a on C, so each P_i,a-P_5,a vanishes there. Common-root division
gives unique g_i,a in F[X] for i=1,...,4 with

\[
 P_{i,a}-P_{5,a}=G g_{i,a},\qquad \deg g_{i,a}\le4
 \quad\text{when }g_{i,a}\ne0.
\]

Indeed each nonzero difference has degree at most 63, so the quotient
has degree at most 63-59=4; a zero difference has the zero quotient.
Put g_5,a=0. For x in U_ij, both messages agree with Y_a at x, and
x is not in C. Thus G(x) is nonzero in F and
g_i,a(x)-g_j,a(x)=0. The core enters only through this division and
nonvanishing, not through the reduced evaluation matrix. The private
points impose no pair equalities, and additional agreements do not
invalidate any selected equality.

**Signed-system transport.** Order the twenty reduced coefficients
by i=1,...,4 and then d=0,...,4, as in L040. Let M_s be the matrix
with rows evaluating g_i-g_j at s h^(2r) and s h^(2r+1), in the stated
edge and point order, retaining the signs +1 and -1 and g_5=0.
Thus M_1=M. Set

\[
 B_s=\operatorname{diag}(1,s,s^2,s^3,s^4,
                         1,s,s^2,s^3,s^4,
                         1,s,s^2,s^3,s^4,
                         1,s,s^2,s^3,s^4).
\]

For an unshifted row point x and a coefficient of degree d in message
ell<=4, the corresponding entry of M_s is +(s x)^d if ell=i,
-(s x)^d if ell=j, and zero otherwise. The same entry of M B_s is
respectively +x^d s^d, -x^d s^d or zero. The statements also cover an
edge incident to message 5, whose coefficient block is absent.
Every entry therefore satisfies

\[
 M_s=M B_s.                                      \tag{1}
\]

This is substitution g(X) -> g(sX): its coefficient vector is B_s v
and its value at x is g(sx). The substitution direction is s, not
s^{-1}; the inverse scaling is used only when inverting B_s.
Because s belongs to H<=E^*, B_s is invertible over E, with diagonal
entries s^{-d} in its inverse. L040's inverse gives the identity

\[
 (B_s^{-1}T)M_s=B_s^{-1}(TM)B_s=I_{20}.          \tag{2}
\]

Both (1) and (2) remain identities over F under the fixed embedding
E -> F. In particular ker_F M_s=0, without a rank-genericity claim,
an arbitrary-label permutation, a new elimination or any assumption
on the coefficients' descent.

**Equality in every tuple row.** The coefficient vector v_a of the
four g_i,a satisfies M_s v_a=0 by all twenty selected overlap
equalities proved above. Multiplying by B_s^{-1}T gives v_a=0.
Thus every g_i,a is zero, and P_i,a=P_5,a for all i. The argument
holds independently for every a, proving equality of the full
polynomial tuples. It requires neither distinct tuples nor a scalar
projection preserving distinctions. Zero differences, arbitrary
extension-field rows and extra agreements were included throughout.

**Test outcome and scope.** The universal symbolic transport and
row-wise necessity succeed for all parameters in the hypotheses.
The only finite rank evidence used is L040's already audited inverse;
no fresh arithmetic verification of that input is claimed. The result
can provide a further necessary restriction in a prospective 59-core
family certificate. Such a transfer and a useful family cap remain
unproved. L034's 60-core criterion does not apply. Independent edge
shifts, arbitrary label bijections and changed overlap assignments
are outside this statement. The stops in ATTEMPTS/019–021,023–025
remain intact. This local progress is not progress beyond the assessed
polynomial tools or a candidate resolution of the main challenge.

**Independent critical audit (2026-10-10, step 113).** Under the separately
approved [audit assessment](../drafts/literature/2026-10-10-uniform-five-support-critical-audit.md),
the complete proof was checked with C001a's instance and L040's matrix
definition and audited inverse as inputs. No finite elimination was rerun.
The following checks retain the conclusion for every stated parameter;
they do not establish an additional restriction or a cardinality bound.

First, multiplication by the nonzero s maps H bijectively to itself,
so all twenty overlap points remain distinct. After choosing any 59
of the 1004 remaining points for C, 945 points remain for five distinct
private choices. This verifies nonvacuity as well as the asserted
incidences: every noncore point has precisely its one or two assigned
owners, and a point in three supports must lie in C. No step requires
C or the private points to be translates of the original choices.

For common-root division, enumerate the distinct core points c_1,...,c_59.
After removing the first j linear factors from a difference P_i,a-P_5,a,
evaluation at c_(j+1) gives the product of j nonzero factors times the
remaining quotient. This product is nonzero in F, so that quotient still
vanishes at c_(j+1). Successive use of the cited factor theorem removes
all 59 factors. F[X] is an integral domain and G is nonzero, giving
uniqueness, zero quotient for a zero difference, and degree at most four
for a nonzero quotient. At each overlap x, all factors x-c are nonzero.
Thus cancellation of G(x) is valid over F for every core and row,
including differences whose coefficients lie outside E.

Here is the explicit sign check in the stated edge order. Write
q(x)=(1,x,x^2,x^3,x^4); each table row represents each of the two
evaluation points belonging to its edge, with four message blocks:

| Edge | Block 1 | Block 2 | Block 3 | Block 4 |
| --- | --- | --- | --- | --- |
| 12 | q(x) | -q(x) | 0 | 0 |
| 13 | q(x) | 0 | -q(x) | 0 |
| 14 | q(x) | 0 | 0 | -q(x) |
| 15 | q(x) | 0 | 0 | 0 |
| 23 | 0 | q(x) | -q(x) | 0 |
| 24 | 0 | q(x) | 0 | -q(x) |
| 25 | 0 | q(x) | 0 | 0 |
| 34 | 0 | 0 | q(x) | -q(x) |
| 35 | 0 | 0 | q(x) | 0 |
| 45 | 0 | 0 | 0 | q(x) |

These are exactly L040's rows, with no block for g_5=0. In every block
and for both points of every edge, q(sx)=q(x)diag(1,s,s^2,s^3,s^4).
Negative blocks retain their signs in characteristic 65537. Hence the
entire signed matrix, including all reference-message edges, is M B_s.
The coefficient of X^d in g(sX) is s^d times that in g(X), which
independently checks the substitution direction. Since s is nonzero,
B_s is invertible; associativity gives (B_s^(-1)T)(M B_s)=I using
the imported TM=I. No determinant transformation is needed.

The embedding E into F preserves these matrix products, their identity
entries and the nonzero inverses s^(-d). It therefore supplies a left
inverse on F^20, not merely on vectors over E. For an arbitrary fixed
row a, each of its twenty overlap equalities gives the corresponding
zero entry of M_s v_a. Applying this left inverse sets all twenty
coefficients to zero. Repeating the same argument for each a proves
equality of polynomial tuples; it never selects a common distinguishing
row or projects tuples. Equal messages, zero differences and extra
agreements cause no exception. The center is used only for these
necessary equalities; no converse or center construction is needed.

Every universal obligation passes this symbolic audit. The mathematical
inputs remain C001a and L040; L031 and L034 are comparisons only here.
The existing DAG row requires no change. Full matching Mathlib coverage
remains unchecked, with supporting citations retained below. This is a
REPRODUCTION audit with no substantive error found, no new mathematical
bound and no progress beyond the assessed tools. The next quantitative
gap is still a sound 59-core transfer and a useful cap, not another
audit of the same matrix transport.

## Mathlib

A full matching universal five-support theorem is **not checked** in
Mathlib; this is not an assertion of absence. Supporting declarations
were inspected in the reused source assessment:

- `Polynomial.eval_comp` and `Polynomial.comp_assoc`, over a
  commutative semiring, at
  [Eval/Defs.lean, 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Eval/Defs.lean).
- `Polynomial.comp_C_mul_X_coeff` over a semiring and
  `Polynomial.comp_C_mul_X_eq_zero_iff` for a non-zero-divisor
  multiplier, at
  [Eval/Degree.lean, 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Eval/Degree.lean).
- `Polynomial.natDegree_comp` over a semiring with no zero divisors
  and `Polynomial.natDegree_C_mul` for a nonzero multiplier, at
  [Degree/Lemmas.lean, 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Degree/Lemmas.lean).
- `Polynomial.dvd_iff_isRoot`, over a commutative ring, at
  [Div.lean, 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Div.lean).

E and F meet these field/ring hypotheses, and s is a nonzero element
and hence a non-zero-divisor in both. The zero polynomial is handled
explicitly in the quotient step; the substitution preserves the
degree-at-most-four coefficient space. These declarations support
the algebra and do not supply the signed finite matrix or any cap.
