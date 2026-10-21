# L042 — The nine-union common-coordinate locator never persists

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
and use C=RS[F,H,8], the pinned cell 1/4<=delta<5/16, and L010's
eight shifted moments and determinant locator L(T,X).
Take the **local converse** of L041 in its tau=1 row, without assuming
sixteen-count equality or coordinate-locator nonvanishing. Thus three
distinct original finite parameters gamma_0,gamma_1,gamma_2 and
three full-weight four-error words e_i have syndromes s(gamma_i)
for an affine pencil s(T). Their union has nine labels. After renaming
the errors, their supports are
\[
 A_0=\{h,d,y_1,y_2\},\quad A_1=\{h,d,z_1,z_2\},\quad
 A_2=\{h,w_1,w_2,w_3\},                              \tag{1}
\]
where all nine displayed labels are distinct elements of H.

In particular retain L041's alpha_i=gamma_j-gamma_k, nonzero
lambda and c_x, and all its normalized weight gates. More explicitly,
write the normalized weights at h as p,q,1-p-q and at d as r,1-r.
Require p*q*(1-p-q)!=0 and r*(1-r)!=0; all seven singleton weights
are the prescribed nonzero lambda*c_x/alpha_i. Weights, lambda and
parameters range over F, and the excluded original direction [sigma(b)]
is unrestricted. These are local moment-compatible triples, not presumed
completions to sixteen errors.

## Conclusion

For every such gated choice,
\[
                    L(T,h)\ne0\quad\hbox{in }F[T].       \tag{2}
\]
Thus the exact persistence criterion on this full-weight local domain
has no solutions. It is independent of p,q and holds for every allowed
r, every nonzero lambda, every labeling and every original finite
parameter triple. In fact all sixteen coordinate locators are nonzero
polynomials, and D is nonzero at the three selected parameters.

This closes L041's remaining local nonpersistence gate. It gives no
sixteen-count completion, no universal triple extraction, no improved
global count and no identification with ABF26. A separate critical audit
on 2026-10-08 found no defect within these hypotheses; its checks appear
below. This is a verified local input, not a complete challenge argument.

## Proof

### Exact modified-moment determinant

For 1<=j<=7 define
\[
 r_j(T)=s_{j+1}(T)-h s_j(T).
\]
In the five-by-five determinant defining L(T,h), number the columns
0,...,4. For j=4,3,2,1 in that order, replace column j by
column j minus h times column j-1. These operations preserve the
determinant and use the original preceding column. The bottom row
becomes (1,0,0,0,0). Its column-zero cofactor has sign
(-1)^(5+1)=1, so expansion gives the exact identity
\[
 L(T,h)=\det\bigl(r_{i+j+1}(T)\bigr)_{0\le i,j\le3}.   \tag{3}
\]
No assumption on D(T) or a decoder convention enters this identity.
For an error e with moments s_j=sum_x e(x)x^j, its modified moments
are sum_x e(x)(x-h)x^j. In particular the weight at h contributes
zero. This elementary identity is the only modified-syndrome formula
used here.

The supporting puncturing convention is J. I. Hall, *Notes on Coding
Theory*, Modifying Codes chapter, section 6.2, Theorem 6.2.1 and
Proposition 6.2.2 with proof, printed pp. 82–83, and the J-syndrome
algorithm, printed p. 84 of the undated
[author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/Mod.pdf),
inspected 2026-10-08 in the prior assessment. Deleting h adjusts dual
multipliers by x-h and leaves seven syndrome entries: 15 retained
distinct points, dimension 8, nonzero original multipliers and nonzero
x-h at retained labels meet its hypotheses. One erasure and three
errors satisfy 1+2*3<=16-8. The source does not assert the persistence
criterion. Equation (3) is needed to connect this convention precisely
to L010's nonreciprocal determinant locator; the argument below is the
remaining local specialization, not a reproof of the puncturing theorem.

### All five Cauchy–Binet terms

Put g=gamma_1-gamma_0!=0 and t=(T-gamma_0)/g. Substituting
T=gamma_0+g*t is an F-algebra isomorphism F[T] to F[t], so
polynomial vanishing is equivalent before and after this substitution.
This is only a calculation of the same locator polynomial: the original
finite parameters and excluded direction have not been replaced by a
projectively normalized model.

Because s is affine, its value at T is
(1-t)*sigma(e_0)+t*sigma(e_1). Set
\[
 u_x=e_0(x)x(x-h)\quad(x\in\{d,y_1,y_2\}),\qquad
 v_x=e_1(x)x(x-h)\quad(x\in\{d,z_1,z_2\}).             \tag{4}
\]
Every displayed u_x and v_x is nonzero: the original weights are
nonzero, H has no zero label, and these labels differ from h.
For W={d,y_1,y_2,z_1,z_2}, let
\[
 a_d(t)=(1-t)u_d+t v_d,\quad
 a_{y_i}(t)=(1-t)u_{y_i},\quad a_{z_i}(t)=t v_{z_i}.
\]
For 0<=j<=6 we then have
\[
 r_{j+1}(\gamma_0+g t)=\sum_{x\in W}a_x(t)x^j.         \tag{5}
\]
The four-by-four matrix in (3) is therefore
V*diag(a_x(t))*V^tr, where V has columns (1,x,x^2,x^3)^tr
for x in W. Apply the standard named **Cauchy–Binet formula** over
the commutative ring F[t]: Chris Godsil, *More Linear Algebra*, version
26/11/2021, section 7.3, Theorem 7.3.1 and complete proof, printed
pp. 83–84 (PDF pp. 93–94),
[author-hosted text](https://www.math.uwaterloo.ca/~cgodsil/quagmire/linalg2/pdfs/LA2.pdf).
The theorem takes two 4-by-5 matrices over a commutative ring; use
A=V and B=V*diag(a_x(t)), so A*B^tr is exactly the matrix above.
Its corresponding-column minors give the squared Vandermonde times
the product of the four selected a_x. No invertibility of an a_x(t)
or characteristic-zero assumption is required. This imports the formula;
only its local specialization is proved here. The primary statement and
proof were inspected in the prior approved audit assessment.
For a four-element subset S of W put
Delta(S)=det((x^i)_(0<=i<=3,x in S)), choosing any order;
Delta(S)^2 is independent of that order. Distinct labels imply
Delta(S)!=0 by the Vandermonde determinant formula. The complete
sum consists of the five subsets obtained by omitting one label:
\[
 L(\gamma_0+g t,h)=\sum_{|S|=4}\Delta(S)^2\prod_{x\in S}a_x(t)
                  =t(1-t)R(t),                         \tag{6}
\]
where
\[
 R(t)=K t(1-t)+a_d(t)\bigl(M t+N(1-t)\bigr),           \tag{7}
\]
and, with Delta squared written on the indicated label set,
\[
\begin{aligned}
 K={}&\Delta(\{y_1,y_2,z_1,z_2\})^2
           u_{y_1}u_{y_2}v_{z_1}v_{z_2},\\
 M={}&v_{z_1}v_{z_2}\bigl(
        u_{y_1}\Delta(\{d,y_1,z_1,z_2\})^2+
        u_{y_2}\Delta(\{d,y_2,z_1,z_2\})^2\bigr),\\
 N={}&u_{y_1}u_{y_2}\bigl(
        v_{z_1}\Delta(\{d,y_1,y_2,z_1\})^2+
        v_{z_2}\Delta(\{d,y_1,y_2,z_2\})^2\bigr).
\end{aligned}                                        \tag{8}
\]
To check that (6) retains every term, omitting d gives
K*t^2*(1-t)^2. Omitting y_1 or y_2 gives exactly the two
terms a_d*t^2*(1-t) in M, with the other y-label retained.
Omitting z_1 or z_2 gives exactly the two terms
a_d*t*(1-t)^2 in N, with the other z-label retained. There are
no other subsets. In particular K!=0, while M,N may vanish and
are never divided out.

### Nonvanishing, including cancellation cases

Suppose L(T,h) were the zero polynomial. The substitution is invertible,
and t(1-t) is nonzero in the integral domain F[t]; hence (6) forces
R=0. Evaluating this polynomial identity at 0 and 1 gives
\[
                   0=u_d N,\qquad 0=v_d M.
\]
Full weight at the double-only coordinate d gives u_d,v_d!=0,
so N=M=0. But then (7) reads R(t)=K*t(1-t), a nonzero
polynomial because K!=0. This is a contradiction. The argument
does not assume nonvanishing of M or N, divide by a parameter
root, or exclude a singular intermediate value of a_d(t).
The two free normalized weights at h disappear in (5), and
the r!=0,1 gates are exactly what preserves u_d,v_d in this
contradiction. No rationality of those weights was used.

Finally L041, using L010's pointwise formula, gives
D(gamma_i)!=0 and
L(gamma_i,X)=D(gamma_i)*product_(x in A_i)(X-x).
For every x!=h at least one A_i omits x, so L(gamma_i,x)!=0
for that i. Together with (2) this proves nonvanishing of every
coordinate locator. This conclusion uses the third error only to
exclude persistence away from h; the proof of (2) itself used the
first two full-weight errors and their specified intersection.
These conclusions verify a local gate, without counting any
additional bad parameters or assuming equality.

### Separate critical audit (2026-10-08)

The audit independently checked the determinant definition in L010,
L041's local converse and each step above. No mathematical defect or
missing premise was found in the stated scope. The load-bearing checks
are recorded here rather than treating a sample calculation as proof.

With top-row index i=0,...,3 and surviving column index j=1,...,4,
the descending column operation leaves entry
s_(i+j+1)-h*s_(i+j)=r_(i+j). Reindexing j by j-1 gives exactly
r_(i+j+1) in (3). The bottom row is (1,0,0,0,0); removing its first
column has positive sign. Since the lowest modified moment is r_1,
the weights for a Vandermonde starting at exponent zero must be
e(x)*x*(x-h), as in (4), not just e(x)*(x-h).

Write Delta_S^2 for the squared Vandermonde on S. Independently listing
the five selected-column subsets gives the following full contributions
before division by the polynomial factor t(1-t):

| Omitted label | Contribution to L(gamma_0+g*t,h) |
| --- | --- |
| d | Delta_(W minus d)^2 u_(y_1)u_(y_2)v_(z_1)v_(z_2) t^2(1-t)^2 |
| y_1 | Delta_(W minus y_1)^2 a_d u_(y_2)v_(z_1)v_(z_2) t^2(1-t) |
| y_2 | Delta_(W minus y_2)^2 a_d u_(y_1)v_(z_1)v_(z_2) t^2(1-t) |
| z_1 | Delta_(W minus z_1)^2 a_d u_(y_1)u_(y_2)v_(z_2) t(1-t)^2 |
| z_2 | Delta_(W minus z_2)^2 a_d u_(y_1)u_(y_2)v_(z_1) t(1-t)^2 |

Thus both retained-label indices in M and N are correct, and no sign
or multiplicity is missing: the two rectangular minors have the same
column order, so their Vandermonde signs cancel. All five terms are
polynomials over F, including when a_d vanishes at an intermediate t.
Distinct labels and full weights make K nonzero. In the polynomial
domain F[t], identity (6) implies R=0 if the locator is zero; it does
not rely on division by t or 1-t at an endpoint. Evaluating R, rather
than the original determinant, gives u_d*N=0 and v_d*M=0. The gates
r!=0,1 and the nonzero lambda,c_d,alpha_0,alpha_1 give u_d,v_d!=0.
Both M=N=0 are permitted, but then K*t(1-t) is a nonzero polynomial.
This covers cancellation in either sum and every possible a_d root.

All actual weights include the factors lambda*c_x/alpha_i. None is
replaced by its normalized parameter alone. Scaling lambda by a nonzero
factor scales every entry of the modified moment matrix by that factor,
and scales its determinant, K and the full expression (7) by its fourth
power. Thus the proof neither loses a scaling branch nor needs to fix
lambda for an externally specified pencil. The two weights at h vanish
from the modified moments without any restriction beyond L041's gates.

The substitution T=gamma_0+g*t has inverse t=(T-gamma_0)/g because
the original parameters are distinct. It checks a polynomial identity
for the given affine pencil and fixes its point at infinity; no assertion
that [sigma(b)] or a parameter is rational over F_97 is used. The third
finite parameter is not needed in the common-locator contradiction.
It is needed for the last step: the intersection of the three supports
is exactly {h}, so every other coordinate is omitted at a witnessed
full-weight parameter. L010's factorization at such a parameter uses
only its actual four nonzero weights and distinct nonzero labels, not
the global nonpersistence hypothesis. It gives D(gamma_i)!=0 and a
nonzero locator value at each omitted label without circular reasoning.

The audit imports Godsil's ring-valued Cauchy–Binet formula and reuses
the already assessed coding inputs; it verifies the local specialization,
not a new determinant or decoding theorem. No fixed L016 count, rational
descent, equality assumption or additional-parameter bound enters it.

## Mathlib

The full local nonpersistence specialization: **not checked** in
Mathlib. The prior approved source assessment inspected the official
[determinant documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html):
`Matrix.det_mul`, `Matrix.det_transpose` and `Matrix.det_diagonal`
are supporting square-matrix results, not a matching rectangular formula
or formal proof of this lemma. Matching rectangular Cauchy–Binet,
Vandermonde, column-operation, affine-substitution and polynomial-domain
declarations remain **not checked** here. The precise Godsil and Hall
citations are informal standard inputs. No absence claim or Lean
verification is asserted.
