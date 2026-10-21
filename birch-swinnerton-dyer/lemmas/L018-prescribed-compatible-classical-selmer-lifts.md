# L018 — Prescribed compatible classical Selmer lifts and divisible Sha

## Hypotheses

Retain C016a's hypotheses and actual arithmetic inputs: E/Q is non-CM,
p >= 5 is good ordinary and non-anomalous, E[p] is surjective, the
Manin and Tamagawa factors are prime to p, and E(Q_p)[p] = 0. The
fixed primes ell_1,ell_2 belong to P_(2,0); their product is a minimal
nonzero mod-p two-prime Kurihara index, with the normalizations and
coefficient-compatible systems used there. Also L(E,1) = 0.
Neither finite p-primary Sha nor positive rational rank is assumed.

Put D = Q_p/Z_p, S_m = Sel(Q,E[p^m]), and
S_infinity = Sel(Q,E[p^infinity]), with classical Kummer local
conditions. C016a supplies dim_F_p S_1 = 2, infinitude of S_infinity,
and its prescribed R_2-basis c_1,c_2 of S_2, where R_2 = Z/p^2 Z.
Write r = rank E(Q).

Use Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main
conjecture for elliptic curves*, author text dated 2025-05-12,
[Theorem 1.8, printed pp. 6--7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7).
Its hypotheses and nonzero Kurihara collection were matched in C016a.
Only the structural clauses are used, not the rational-rank clauses
that add finite Sha. This application is approved in
[the saved SPECIALIZE assessment](../drafts/literature/2026-10-04-central-vanishing-all-depth-classical-lifting.md).

## Conclusion

There are natural coefficient identifications

\[
j_m:S_m\xrightarrow{\sim}S_\infty[p^m],\qquad
j_m\rho_m=pj_{m+1},
\tag{1}
\]

where rho_m is induced by multiplication by p from E[p^(m+1)] to
E[p^m]. Moreover

\[
S_\infty\simeq D^2,\qquad S_m\simeq(\mathbf Z/p^m\mathbf Z)^2.
\tag{2}
\]

There exist bases x_1^(m),x_2^(m) of S_m for every m >= 2 with

\[
x_i^{(2)}=c_i,\qquad\rho_m(x_i^{(m+1)})=x_i^{(m)}.
\tag{3}
\]

These are choices of compatible classical lifts. They need not be
new prime-deletion components, and no higher P_(m,0) eligibility for
the fixed primes or canonical choice of lifts is asserted.

The remaining Sha obstruction is entirely divisible:

\[
\Sha(E/\mathbf Q)[p^\infty]\simeq D^{2-r},\qquad 0\le r\le2.
\tag{4}
\]

This subgroup lies in the radical of the Cassels--Tate pairing. With
downward coefficient maps, the inverse limit has the exact sequence

\[
0\longrightarrow E(\mathbf Q)\otimes\mathbf Z_p
\longrightarrow\varprojlim_{\rho_m}S_m\simeq\mathbf Z_p^2
\longrightarrow T_p\Sha(E/\mathbf Q)\simeq\mathbf Z_p^{2-r}
\longrightarrow0.
\tag{5}
\]

Thus the finite Sha quotient is zero. Rational membership of the whole
compatible basis is equivalent to T_p Sha = 0, or r = 2, which is
still missing. No rational-rank lower bound is obtained.

## Proof

**Natural coefficient identifications.** Surjectivity on E[p] gives
E(Q)[p] = 0. Every nonzero rational p-primary torsion point would have
a rational multiple of order p, so E(Q)[p^infinity] = 0. Apply global
Galois cohomology to

\[
0\longrightarrow E[p^m]\longrightarrow E[p^\infty]
\xrightarrow{p^m}E[p^\infty]\longrightarrow0.
\tag{6}
\]

The H^0 vanishing makes coefficient inclusion an isomorphism from
H^1(Q,E[p^m]) onto H^1(Q,E[p^infinity])[p^m]. At each place v, the
classical Kummer condition is the kernel of the natural coefficient
map to H^1(Q_v,E). Those maps commute with coefficient inclusion.
Consequently a finite-coefficient class is classical exactly when
its image is classical, proving the first assertion of (1).
Local H^0 need not vanish: no local coefficient injectivity is used.
This is the classical identification explicitly recorded in Kim's
[Section 5.3.1, printed p. 28](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28).

The maps E[p^(m+1)] to E[p^infinity] obtained by inclusion followed
by multiplication by p, or multiplication by p followed by inclusion
of E[p^m], agree. Their H^1 maps prove the second assertion of (1).
Downward maps are multiplication by p on S_infinity torsion; upward
coefficient inclusions are different maps.

**Eliminate the paired finite factors.** Import Kim's Theorem 1.8,
without reproof. It gives the structure

\[
S_\infty\simeq D^d\oplus
\bigoplus_{j=1}^{t}(\mathbf Z/p^{a_j}\mathbf Z)^2,
\qquad a_j\ge1,
\tag{7}
\]

with finitely many nontrivial finite factors. The theorem specifies
d and the exponents using its integral Kurihara collection. We do
not identify its first index with our mod-p minimal index.
By (1) and C016a, taking p-torsion in (7) gives

\[
2=\dim_{\mathbf F_p}S_1=d+2t.
\tag{8}
\]

Infinitude of S_infinity forces d > 0, since the second summand is
finite. The only integer solution of (8) is d = 2,t = 0. This proves
(2). The even contribution here is from finite paired Selmer factors;
no assertion of even rational rank r is used.

**Fix the prescribed basis in the whole tower.** Choose one isomorphism
alpha:S_infinity to D^2. Define coordinates

\[
\theta_m:S_m\xrightarrow{\sim}(\mathbf Z/p^m\mathbf Z)^2,
\qquad \alpha j_m(s)=p^{-m}\theta_m(s)\pmod{\mathbf Z_p^2}.
\tag{9}
\]

The right side uses any integral representatives. By (1), theta_m
rho_m is reduction modulo p^m of theta_(m+1). This identifies the
transition maps, not just each separate group's isomorphism type.

Let A_2 have columns theta_2(c_1),theta_2(c_2). It is in GL_2(R_2)
because c_1,c_2 are a basis. Lift its entries to a matrix A over Z_p.
The determinant is nonzero modulo p, hence a unit, so A is in
GL_2(Z_p). For standard coordinate vectors epsilon_i, set

\[
x_i^{(m)}=\theta_m^{-1}(A\epsilon_i\bmod p^m).
\tag{10}
\]

These are bases, equal c_i at depth two, and satisfy (3) by (9).
They require no higher-depth auxiliary-prime construction.

**Keep divisible Sha explicit.** The infinite Kummer sequence, obtained
from the finite sequences as in C016a, is

\[
0\longrightarrow E(\mathbf Q)\otimes D
\longrightarrow S_\infty
\longrightarrow\Sha(E/\mathbf Q)[p^\infty]\longrightarrow0.
\tag{11}
\]

Finite generation identifies the left term with D^r. The quotient
of D^2 in (11) is divisible and p-primary. Taking p-torsion in (11)
is right-exact because multiplication by p on D^r is onto: adjust
an arbitrary lift of a p-torsion quotient class by an element of
D^r to make it p-torsion. Its p-torsion dimension is therefore 2-r.
The standard classification of divisible abelian groups identifies
a divisible p-primary group of this dimension with D^(2-r), proving
(4). In particular this deduction gives no lower bound on r.

Milne, *Elliptic Curves*, second edition (2021),
[Theorem IV.5.4 and Remark 5.2, printed p. 130](https://www.jmilne.org/math/Books/EC2.pdf#page=135),
give the Cassels pairing and its divisible kernel. The subgroup in
(4) is divisible as an abelian group: multiplication by primes other
than p is also invertible. It lies in that kernel. Zero pairing
values therefore do not certify rational membership.

**Compute the inverse-limit quotient.** At each depth,

\[
0\longrightarrow E(\mathbf Q)/p^mE(\mathbf Q)
\longrightarrow S_m\longrightarrow\Sha(E/\mathbf Q)[p^m]
\longrightarrow0.
\tag{12}
\]

The downward maps are reduction on the point quotient and
multiplication by p on Sha, as in Milne's
[Chapter IV diagram, printed p. 129](https://www.jmilne.org/math/Books/EC2.pdf#page=134).
With no rational p-primary torsion, the inverse limit of the left
term is E(Q) tensor Z_p. By (9), the middle limit is Z_p^2. The
right limit is T_p Sha by definition, and is Z_p^(2-r) by (4).

Surjectivity onto that last limit can be checked directly. Given
compatible Sha elements b_m, choose a lift s_1 in S_1. Having chosen
s_m, lift b_(m+1) arbitrarily to u in S_(m+1). Compatibility puts
rho_m(u)-s_m in E(Q)/p^mE(Q). Lift that difference using surjective
reduction E(Q)/p^(m+1)E(Q) to E(Q)/p^mE(Q), and subtract its Kummer
class from u. This gives s_(m+1) with rho_m(s_(m+1)) = s_m.
The kernels are identified coordinate by coordinate in (12).
This proves (5) without an unstated limit-exactness assumption.

The two compatible columns (10) form a Z_p-basis of the middle term
of (5). Both belong to its rational Kummer submodule exactly when
the quotient is zero, equivalently r = 2. The same obstruction
survives after tensoring with Q_p, with dimension 2-r. Possibilities
r = 0,1,2 allowed by this structural calculation are not asserted
to have arithmetic realizations under the retained hypotheses.

The all-depth lifting continuation test is met: no finite factor
survives and the prescribed basis lifts compatibly. The remaining
rationality obstruction is divisible Sha, not a later finite
coefficient obstruction. The required lower bound r >= 2, production
of the two-prime premise from m(E) = 2, analytic comparison and higher
ranks remain missing. This is a REPRODUCTION by specialization of
the assessed known structure and Kummer results; no progress beyond
the checked literature or complete BSD candidate is claimed.

## Mathlib

Full coverage of this prescribed compatible lifting and quotient
statement: **not checked**. Supporting coefficient cohomology,
classical Selmer conditions, divisible-group classification, matrix
lifting, Kummer sequences and inverse limits: **not checked**.
Kim's Theorem 1.8 matches the paired structural input (7), while
Section 5.3.1 supplies the classical coefficient identification.
Milne's diagram supports the transition maps, and Theorem IV.5.4
identifies the pairing's divisible radical. These are precise
supporting arithmetic citations, not a full-statement Mathlib match.
No absence or originality inference is made.
