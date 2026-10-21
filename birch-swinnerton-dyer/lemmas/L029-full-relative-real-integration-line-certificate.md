# L029 — Conditional full-relative real-integration-line certificate

## Hypotheses

Let E/Q be non-CM and given by a global minimal equation, with conductor
N, and let f=sum_(n>=1) a_n q^n be its normalized weight-two newform.
In particular a_1=1 and all a_n are rational and real. Set

\[
M=M_2(\Gamma_0(N)),\quad V=M\otimes_{\mathbf Z}\mathbf Q,
\quad A(\{\alpha,\beta\})=2\pi i\int_\alpha^\beta f(z)\,dz,
\quad I=\operatorname{Re}A.
\]

M is the entire torsion-free relative symbol module, with paths oriented
from alpha to beta, as in L028 hypothesis 1. Grant an independently
certified complete integral presentation M=Z^s/R_sat, its identification
with relative cusp paths, a rational basis e_1,...,e_d of V (d>=1), and
exact coordinates c_i in Q^d of all integral generators g_i. In particular,
V_R identifies with H_1(X_0(N),Cusps;R); no absolute-only presentation or
unspecified lattice is substituted. The theorem does not construct this
evidence.

Grant a finite set P of primes ell not dividing N. For each ell in P,
certify independently both a_ell(E)=ell+1-#E(F_ell) and the rational matrix
H_ell of the following operator on the **entire** V:

\[
T_\ell\{\alpha,\beta\}
 =\{\ell\alpha,\ell\beta\}
  +\sum_{r=0}^{\ell-1}
    \{(\alpha+r)/\ell,(\beta+r)/\ell\}.
\tag{1}
\]

Grant also a certified rational matrix J of geometric reflection

\[
j\{\alpha,\beta\}=\{-\alpha,-\beta\},
\tag{2}
\]

induced by z -> -conjugate(z) with the path parameter orientation
preserved. Matrices act on columns: [T_ell x]=H_ell[x], [jx]=J[x].
Their certification must identify these operators on every basis vector
and respect the complete presentation, not merely verify eigenvalues on
one proposed vector. Rational-basis coordinates are not integral-generator
values. No software sign convention is an input in place of (2).

Form the rational matrix with vertically stacked blocks

\[
B=\begin{pmatrix}
J^{\mathsf t}-\mathrm{Id}_d\\
(H_\ell^{\mathsf t}-a_\ell(E)\mathrm{Id}_d)_{\ell\in P}
\end{pmatrix},\qquad K_{\mathbf Q}=\ker(B:\mathbf Q^d\to\mathbf Q^{(1+|P|)d}).
\tag{3}
\]

Grant exact full-space evidence dim_Q K_Q=1 and a nonzero v in K_Q.
For example Bv=0, one nonzero (d-1)-square minor of B, and v!=0 suffice;
for d=1 the required minor is the empty minor, with determinant 1.
Exact rational elimination with reversible row operations also suffices.
Approximate rank, sampled relations, or a rank computation restricted to
absolute cycles does not meet this hypothesis.

No condition on L(E,1), twist value, real period scale, Manin constant,
finite Sha, or generation of the full Hecke algebra by P is imposed.
The non-CM and minimality assumptions are retained to match L028; the
line argument below only uses the stated newform and certified module.

## Conclusion

Define phi in V^* by phi(x)=v^t[x]. Then there is a nonzero real beta with

\[
\boxed{I=\beta\phi\quad\hbox{on all of }V_{\mathbf R}.}
\tag{4}
\]

Thus U=Q phi is a certified full-relative real-integration line meeting
L028 hypothesis 2. Its exact integral-generator values are x_i=v^t c_i;
all relation and coordinate denominators must be retained. Neither beta
nor beta/Omega(E) is computed or assumed rational here. Independent q and
all the other premises of L028 remain necessary for its calibration.

The exact threshold is full relative kernel dimension one. A larger
kernel leaves this test inconclusive. No actual presentation, operator,
rank witness, q, C, b, coefficient, finite cutoff or termination guarantee
is produced by this conditional statement. It does not close the BSD
rank gap.

## Proof

**Named inputs and their domains.** Import Stein, *Modular Forms, a
Computational Approach*, online v0.1, General Modular Symbols,
[Proposition 1.38, Theorem 1.42 and Remark 1.41](https://www.wstein.org/books/modform/modform/modular_symbols.html).
Integration is well-defined on relative symbols and is adjoint to
compatible double-coset operators. The printed theorem uses Gamma_1(N);
the remark permits other finite-index groups and finite double cosets.
For Gamma_0(N) at ell not dividing N use exactly the representatives
in (1). The path normalization is fixed by Cremona, *Algorithms for
Modular Elliptic Curves*, corrected second edition (1997),
[Section 2.4, equation (2.4.1), pp. 18--19](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=12).
Import real-period duality from the same book,
[Section 2.1.2--2.1.3, equations (2.1.3)--(2.1.4), pp. 10--12](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=4).
It is nondegenerate on real-coefficient forms and geometric-plus absolute
homology. Only nonvanishing on cycles is needed from this last input;
full-relative uniqueness will instead come from (3). These standard
results are not reproved.

**Full-relative Hecke membership.** At weight two the polynomial factor
is constant. For a positive-determinant matrix D=(a b;c d), the cited
path identity uses

\[
(f\mid D)(z)=\frac{\det D}{(cz+d)^2}f(Dz),\qquad
\int_\alpha^\beta(f\mid D)(z)\,dz
 =\int_{D\alpha}^{D\beta}f(w)\,dw.
\tag{5}
\]

This is a cusp-to-cusp identity, with no requirement that the path be a
cycle. For the representatives diag(ell,1) and (1 r;0 ell), the form
sum is ell f(ell z)+(1/ell)sum_r f((z+r)/ell), the good-prime T_ell in
the cited normalization. Thus Gamma_0(N), trivial character, k=2, and
ell not dividing N satisfy the imported hypotheses. Since
T_ell f=a_ell(E)f, (5) and (1), multiplied by 2 pi i, give
A(T_ell x)=a_ell(E)A(x) on every relative symbol and hence on V_R.
The eigenvalue is real, so

\[
I(T_\ell x)=a_\ell(E)I(x).
\tag{6}
\]

Well-definedness also removes torsion: an additive map to C annihilates
a torsion class. We therefore use the exact torsion-free relative module
in the hypotheses, not an extension inferred from an absolute eigenline.

**Geometric reflection and sign.** The matrix diag(-1,1) normalizes
Gamma_0(N): it replaces b,c by -b,-c. Reflection consequently acts on
the same quotient and preserves its cusp set. Real Fourier coefficients
give f(-conjugate(z))=conjugate(f(z)). For a path z(t), 0<=t<=1, its
reflected path w(t)=-conjugate(z(t)) has the same direction of its
parameter and w'(t)=-conjugate(z'(t)). Therefore

\[
2\pi i f(w(t))w'(t)
 =-2\pi i\,\overline{f(z(t))z'(t)}
 =\overline{2\pi i f(z(t))z'(t)}.
\]

Integrating and passing to cusp endpoints (the cusp form has convergent
cusp integrals) proves A(jx)=conjugate(A(x)) and hence I(jx)=I(x).
There is no endpoint interchange in (2). In Stein's equations (11)--(12)
and Remark 1.43 the weight-two star is -j; a matrix certified as that
star must be negated to obtain J. Equivalently its dual equation would
have eigenvalue -1. The asserted plus sign is specifically geometric
reflection with differential 2 pi i f(z) dz.

**I is nonzero even at a zero central value.** Gamma_0(N) is of real
type by the normalization calculation just made. The normalized form f
is nonzero and belongs to S_2(Gamma_0(N))_R. The cited duality (2.1.4)
therefore supplies h in H_1(X_0(N),R)^+ for which
integral_h 2 pi i f(z) dz is a nonzero real number. Absolute homology
injects into relative homology here: in the exact sequence of the pair
(X_0(N),Cusps), the preceding group H_1(Cusps;R) is zero because the
cusp set is finite. Under the granted identification with V_R, the
image of h has the same integral. Thus I(h)!=0. This does not require
h to be integral, nor the special path {infinity,0} to have a nonzero
integral. In particular L(E,1)=0 does not invalidate this argument.
We use duality for all forms and cycles, not the unnecessary assertion
that a single form detects the plus/minus type of every individual cycle.

**The entire dual kernel and scalar extension.** Let u=(I(e_1),...,I(e_d))^t.
For x with coordinate column c, I(x)=u^t c. Equation (6) for all c gives
H_ell^t u=a_ell(E)u; reflection gives J^t u=u. Hence Bu=0 and u!=0.
This establishes membership on the entire relative space before using
its dimension. It is not only a collection of eigenvalue checks on phi.

For completeness the required rational linear algebra has a direct
finite proof. With entries in Q, the rank of B is the largest size of
a nonzero minor. Each such determinant is the same rational number
when viewed in R, so rank_R B=rank_Q B=d-1. The real nullspace is
therefore one-dimensional. The nonzero rational v remains nonzero over
R and satisfies Bv=0, so ker_R B=R v. Equivalently this verifies
K_Q tensor_Q R=ker_R B with the specified coordinates, without an
assumption of scalar-extension compatibility for an unknown operator.
As u is nonzero in this kernel, u=beta v with beta in R\{0}, proving (4).
For the example of rank evidence in the hypotheses, Bv=0 bounds rank
above by d-1 and the minor bounds it below by d-1; both inequalities
are required.

Finally phi(g_i)=v^t c_i is rational for every integral generator.
The functional on V automatically annihilates R_sat because the
coordinates come from the complete presentation. These values determine
phi on all of M, supplying precisely the full-relative line requested
by L028. No integral coordinate is inferred from a rational basis, and
no division by a period or a central/twist L-value enters this step.

**Scope of the advance.** This is the convention-sensitive specialization
and rational linear algebra authorized by the saved SPECIALIZE assessment.
The Hecke and period inputs are imported mathematics; no new multiplicity
one, nonvanishing, or algorithmic termination theorem is claimed. The
full-space dimension witness replaces L028's assumed line identification
conditionally; producing that witness and an independent q remains work.
Even an actual instance would supply no uniform BSD comparison, rational
Kummer membership, or removal of the possible divisible Sha contribution.

## Mathlib

Full matching relative-line finite certificate: not checked. Supporting
modular-symbol integration, relative Hecke operators, geometric reflection,
real-period duality and rational-to-real matrix-kernel coverage: not
checked. Unknown coverage is not absence. The full source inputs are
cited above; this proof only specializes their domains and conventions
and supplies the finite rational linear-algebra argument.
