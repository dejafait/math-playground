# L025 — A rational cubic RM extension with a Kahler eigenvector

## Hypotheses

Let S be the very general cubic RM K3 surface of L006, with the
divisor classes and pairing of L019. Write N=NS(S)_Q, T=N^perp,
and q for the cup-product pairing. Thus H^2(S,Q)=T direct sum N,
the full Hodge endomorphism field of T is Q(U), and

\[
f(U)=0,\qquad f(z)=z^3+z^2-2z-1,\qquad
U\sigma=\lambda\sigma,\qquad \lambda=2\cos(2\pi/7)>0,
\]

where sigma spans H^(2,0)(S). In the rational basis (F,O,E,P) of N,
L019 gives

\[
G=\begin{pmatrix}
0&1&0&1\\
1&-2&0&0\\
0&0&-2&1\\
1&0&1&-2
\end{pmatrix}.
\]

All endomorphisms below are rational linear maps; no preservation
of NS(S) as an integral lattice is required. A Kahler class is allowed
to be irrational.

## Conclusion

There are a q-self-adjoint A in End_Q(N) and a Kahler class
omega in N_R such that

\[
A\omega=\lambda\omega.
\]

Consequently B=U direct sum A on T direct sum N is a rational
q-self-adjoint Hodge endomorphism and is multiplication by lambda
on the positive real three-plane spanned by Re(sigma), Im(sigma)
and omega. One can choose A with characteristic polynomial z f(z).
The extra one-dimensional block is essential to this construction;
no identity f(A)=0 on all of N is asserted.

This settles the saved common-metric compatibility prerequisite.
It constructs no vector bundle or transverse deformation of a cycle.
The algebraic span remains 21-dimensional on the original family,
and the established representatives still reach three RM directions
against four required. The universal Hodge conjecture remains open
in this notebook.

## Proof

**Scope of the specialization.** Use the odd-degree transfer functional
from Bayer-Fluckiger--Lenstra, *Forms in Odd Degree Extensions and
Self-Dual Normal Bases* (1990), [proof of Proposition 1.2, p. 362](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1990e/art.pdf#page=5).
The prescribed-form interpretation is also the one in Hanselka,
*Characteristic Polynomials of Selfadjoint Matrices* (2015),
[Lemma 3.10 and Remark 3.12, pp. 64--66](https://d-nb.info/1112605010/34#page=68).
The remaining work is the explicit identification with this divisor
form, the choice of the correct real eigenvalue, and entry into the
actual Kahler cone. This is an application of those known tools,
classified as REPRODUCTION. A general transfer theorem is not
reproved, and no originality claim is made.

**Exact rational form identification.** Put K=Q[a]/(f(a)). Let s:K -> Q
be the linear functional with s(1)=1 and s(a)=s(a^2)=0, and use
b(x,y)=-2s(xy). The relation a^3=-a^2+2a+1 gives s(a^3)=1 and
s(a^4)=-1. Thus, in the basis (1,a,a^2), the Gram matrix is

\[
G_K=\begin{pmatrix}-2&0&0\\0&0&-2\\0&-2&2\end{pmatrix}.
\tag{1}
\]

Let W be the rational span of F,O,E. The map

\[
\psi:K\longrightarrow W,\qquad
1\longmapsto E,\quad a\longmapsto 2F,\quad
a^2\longmapsto -O-2F
\tag{2}
\]

is an isometry: the displayed images have exactly the Gram matrix
(1), as follows directly from G. L019 gives the orthogonal complement

\[
N=W\mathbin{\perp}\mathbb Q v,\qquad
v=P-O-2F+E/2,\qquad q(v,v)=-7/2.
\tag{3}
\]

In particular this is a rational isometry certificate, stronger than
matching dimension, determinant and real signature alone.

Multiplication by every element of K is b-self-adjoint because
b(cx,y)=-2s(cxy)=b(x,cy). Use specifically multiplication by
p(a)=a^2-2 on W via psi, and zero on Qv. Call the resulting map A_0.
Its matrix in (F,O,E,P) is

\[
A_0=\begin{pmatrix}
1&2&-2&5\\
1/2&0&-1&3/2\\
1/2&0&-2&2\\
0&0&0&0
\end{pmatrix},\qquad A_0^{\mathsf T}G=GA_0.
\tag{4}
\]

The polynomial identity

\[
f(z^2-2)=f(z)(z^3-z^2-2z+1)
\tag{5}
\]

shows that f(p(a))=0. Since f is irreducible over Q, as proved in
L006, the minimal and characteristic polynomials of multiplication
by p(a) on this three-dimensional space are both f. Equation (3)
therefore gives characteristic polynomial z f(z) for A_0.

**The positive eigenline has the specified eigenvalue.** The three
real roots of f are in the disjoint intervals

\[
r_-\in(-2,-3/2),\qquad r_0\in(-1/2,0),\qquad
r_+\in(1,3/2).
\tag{6}
\]

The endpoint signs give one root in each interval, exhausting the
degree. In K tensor R, the idempotent associated to a root r is

\[
e_r=\frac{f(a)}{(a-r)f'(r)}.
\]

Here f(a)/(a-r) means evaluation at a of the polynomial quotient
f(z)/(z-r), followed by passage to K tensor R; it is not division
of the zero element by a-r. Its evaluations at the three roots are
1 at r and 0 at the others. Its constant coefficient is
1/(r f'(r)), so

\[
b(e_r,e_r)=-2s(e_r)=-\frac{2}{r f'(r)}.
\tag{7}
\]

For the smallest root r_-, f'(r_-)=(r_--r_0)(r_--r_+)>0,
whereas r_-<0. Hence (7) is positive. Moreover,
p(r_-)=r_-^2-2>1/4. By (5) this is a root of f, so it is the
unique positive root r_+=lambda. Consequently

\[
\xi=\psi(e_{r_-})\in N_{\mathbb R},\qquad
q(\xi,\xi)>0,\qquad A_0\xi=\lambda\xi.
\tag{8}
\]

This root permutation is needed: multiplication by a itself assigns
the positive eigenline to r_-, which is not U's eigenvalue on sigma.

**Move the eigenvector into the actual ample cone.** Fix an ample
class h in N and put

\[
h_0=\sqrt{q(\xi,\xi)/q(h,h)}\,h.
\]

Choose the sign of xi in the component containing h. Since N_R has
signature (1,3), the orthogonal complements of xi and h_0 are
negative definite. Extending their normalized vectors to orthogonal
bases gives a real isometry g_0 with g_0 xi=h_0. If necessary,
compose with a reflection fixing h_0 to obtain det(g_0)=1.

Peters--Sterk, *Symmetric and Quadratic Forms*, June 2024 version,
[Proposition A.3.3, printed p. 424](https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf#page=431),
implies that SO(N,q)(Q) is dense in SO(N_R,q), by taking only the
real place. The ample cone is open in N_R and contains h_0; it is
the intersection of the Kahler cone with N_R. See Huybrechts,
*Lectures on K3 Surfaces*, [chapter 8, section 5.1 and Theorem 5.2,
printed pp. 163--164](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=163).
Thus the set of g with g xi in the ample cone is an open
neighborhood of g_0. It contains a rational g in SO(N,q).

Set omega=g xi and A=g A_0 g^(-1). Rationality and self-adjointness
of A follow from those of A_0 and the rational isometry g, and
A omega=lambda omega. This proves membership in the actual cone;
it does not replace all curve inequalities by a finite sample.
Approximation is applied to the group, so no rationality of
q(xi,xi) is needed. The conjugating map need not preserve the
integral lattice or arise from an automorphism of S.

**Extend over the transcendental part.** The q-adjoint U^dagger is
a rational Hodge endomorphism of T, since q pairs complementary
Hodge types. Write U^dagger sigma=mu sigma. Adjointness and the
nonzero pairing of sigma with its conjugate give

\[
\lambda q(\sigma,\bar\sigma)
=q(U\sigma,\bar\sigma)
=q(\sigma,U^\dagger\bar\sigma)
=\bar\mu q(\sigma,\bar\sigma).
\]

Thus mu=lambda. The injection of the full field End_Hdg(T) into C
given by its action on sigma, established in L006, implies
U^dagger=U. The orthogonal direct sum B=U direct sum A is therefore
q-self-adjoint. It is a Hodge endomorphism because N is of type
(1,1) and U preserves the Hodge structure. Its stated action on the
positive three-plane follows from the real eigenvalue lambda and
(8) after conjugation. This finishes the exact saved target.

The exact matrix and polynomial certificates are checked by
`python3 scripts/cubic-kahler/check_eigenvector_certificate.py`.
That check does not prove cone openness or rational approximation;
those are the cited inputs applied above.

## Mathlib

Coverage of the full statement: **not checked**. No full matching
Mathlib declaration or absence from checked Mathlib sources is
claimed. Bayer-Fluckiger--Lenstra Proposition 1.2 and Hanselka
Lemma 3.10/Remark 3.12 are supporting transfer references;
Peters--Sterk Proposition A.3.3 and Huybrechts chapter 8,
section 5.1/Theorem 5.2 support the chamber argument. Their direct
links appear above. None is cited as a full match for this cubic
divisor-form specialization. The closest quadratic-RM precedent is
Schlickewei, *Hodge classes on self-products of K3 surfaces* (2009),
[Proposition 1.2.3.3, printed pp. 29--30](https://d-nb.info/1000464202/34#page=31);
its quadratic hypothesis is not silently replaced by the cubic one.
