# L071 — Sign-reversed rank-two necessity region at the common metric

## Hypotheses

Use L044's marked projective cubic-RM K3 surface S, its final real
Kähler class h=omega_c, and the identical hyperkähler metric on both
factors of X=S x S. Put Omega=p_1^*h+p_2^*h, s=q(h,h)>0,
e_1=eta tensor 1, e_2=1 tensor eta and P=e_1e_2, where
integral_S eta=1. Retain the **full integral** mixed class tau_D of
L044 and L049, with q-self-adjoint correspondence operator D,

\[
D|_N=2A_c+4\pi_K,\quad D|_T=2U,\quad
Dh=2\lambda h,\quad D\sigma=2\lambda\sigma.
\]

Here sigma is a nonzero holomorphic two-form, lambda is the positive
root of f(z)=z^3+z^2-2z-1, and L047 gives 1<lambda<5/4.
On the metric's positive three-plane D is scalar 2lambda and
preserves its orthogonal complement. L048 gives tau_D^2=156P,
including the transcendental contribution 120P.

For arbitrary integers a,b write p=a+4, t=b+4 and prescribe

\[
c_1=0,\qquad \operatorname{ch}_2=\beta_-=p e_1+t e_2-\tau_D.
\tag{1}
\]

Higher characters and the initial K-class are unrestricted.
The topological test concerns complex rank-two bundles on the
underlying smooth manifold, with trivial determinant. The conditional
holomorphic tests concern locally free rank-two bundles F on X,
slope-polystable at the actual real class Omega. No F, compatible
connection, stable restriction, presentation or transport is assumed
to exist.

## Conclusion

The exact individual filters and their intersection are as follows.

1. Rank two and c_1=0 force
   \[
   \operatorname{ch}_3=0,\qquad
   \operatorname{ch}_4=\frac{pt+78}{6}P,
   \qquad \chi(X,F)=8+2(p+t)+\frac{pt+78}{6}.             \tag{2}
   \]
   The Euler expression is integral exactly when 6 divides pt.
2. The real-class Bogomolov test passes exactly when
   \[
   a+b\leq-4.                                           \tag{3}
   \]
3. An actual topological rank-two SU(2) bundle with these lower
   characters exists exactly when
   \[
   (a+4)(b+4)\equiv6\pmod{12}.                           \tag{4}
   \]
   It has the forced full rational character (2). This is finite-rank
   topological existence, with no holomorphic or connection claim.
4. Every hypothetical holomorphic F in the stated category is stable
   on X and has slope-polystable locally free restrictions to every
   factor fibre at h. Their charges are m=-p and n=-t. For either
   charge c, the stable surface Euler test admits c>=4; the split
   alternative has exactly c=14r^2 for r in Z, including c=0.

Thus the **non-exclusion set for precisely these tests** is

\[
\boxed{a,b\leq-9,\qquad (a+4)(b+4)\equiv6\pmod{12}.}   \tag{5}
\]

It is infinite and contains no symmetric pair. Its largest total
correction is -19, attained exactly at (-9,-10) and (-10,-9).
Each charge-five or charge-six restriction there would be stable.
The final set coincides arithmetically with L052's positive-tensor
factor-filter set, but (3) differs from its Bogomolov cutoff. This
does not import L070's positive-tensor obstruction into (1).
Passing (5) establishes neither holomorphic realization nor transverse
transport nor progress beyond the general theorems checked. This
step is a REPRODUCTION/specialization of those theorems.

## Proof

**Characters and integrality.** L049 verifies integrality of the full
tau_D without an integral NS/T splitting, so (1) and u=-beta_- are
integral. The only sign change is in the mixed term. By factor degree,
e_i tau_D=0, e_i^2=0 and e_1e_2=P. Therefore

\[
\beta_-^2=(2pt+156)P.                                  \tag{6}
\]

The square includes both the divisor and transcendental terms; sign
reversal does not change either squared contribution. Import rank
truncation from Fulton, *Intersection Theory*, 2nd ed., Theorem 3.2(a),
pp. 50--52 (also [Stacks Tag 02TZ](https://stacks.math.columbia.edu/tag/02TZ)),
and the character polynomials from
[Stacks Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
For rank two c_3=c_4=0; with c_1=0 they give ch_2=-c_2,
ch_3=0 and ch_4=c_2^2/12. This proves the character part of (2)
afresh, rather than retaining a former virtual class's higher terms.

Use smooth proper HRR, [Stacks Tag 02UO](https://stacks.math.columbia.edu/tag/02UO),
and the Todd expansion, [Tag 02UN](https://stacks.math.columbia.edu/tag/02UN).
On this K3 product td(X)=1+2(e_1+e_2)+4P. Substitution of (6)
gives the Euler expression in (2); its fractional part is pt/6.
This formal consistency is not K-class realization. For completeness,
the product-line index computation in L049 changes only its linear
mixed term: with A=q(x,x)/2, B=q(y,y)/2 and k=q(Dx,y), all integral,

\[
\chi(F\otimes L(x,y))-χ(F)
=2AB+4A+4B+pB+tA-k\in\mathbb Z.                       \tag{7}
\]

Thus all such indices add no obstruction to the untwisted one.
This records the changed linear sign, not a new independent filter.

**Bogomolov at the unchanged real metric.** Import Perego,
*Kobayashi-Hitchin correspondence for twisted vector bundles*,
[arXiv:1910.01867v1, Corollary 6.42, p. 118](https://arxiv.org/pdf/1910.01867v1#page=118),
with trivial twisting and B-field. For a semistable rank-r bundle on
a compact Kähler n-fold it states
integral ((r-1)c_1^2-2r c_2) Omega^(n-2)<=0. The degree is at the
real metric (Definition 4.7, p. 59); Omega need not be rational.
Here c_2=-beta_-, r=2 and n=4, so the required sign is
integral beta_- Omega^2<=0.

For the even-degree tensor convention, integral tau_D(h tensor h)
=q(h,Dh)=2lambda s. Also Omega^2=s(e_1+e_2)+2h tensor h. Hence

\[
\int_X\beta_-\Omega^2=(p+t-4\lambda)s.                \tag{8}
\]

Since 4<4lambda<5, an integer p+t satisfies p+t<=4lambda
exactly when p+t<=4. This is (3). Equality cannot occur for rational
p,t: the cubic has no rational root (the only candidates are +/-1),
so lambda is irrational. For admitted integral pairs the contraction
is strictly negative. The minus sign in (8) is the changed-data effect.

**Finite-rank topology.** Import Čadek--Crabb--Vanžura,
*Obstruction theory on 8-manifolds*, author's manuscript dated
5 December 2007, corrected 8 July 2008,
[Corollary 8.4, p. 13](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=13).
On a connected closed smooth spin-c eight-manifold M, with integral
l reducing to w_2(TM), a coefficient-line quaternionic line of
second Chern class u exists precisely when

\[
\operatorname{Sq}^2\rho_2(u)=\rho_2(lu),\qquad
\frac14\langle p_1(TM)u+2u^2-l^2u,[M]\rangle
\equiv0\pmod{12}.                                     \tag{9}
\]

The theorem supplies an actual quaternionic line, of complex rank
two, rather than only stable rank four. Its general proof is imported.
L050 checks that X is connected, closed, smooth, eight-dimensional
and spin, so the trivial coefficient line l=0 is allowed. L050 also
proves Sq^2 vanishes on the whole H^4(X,F_2): the pure point classes
vanish by dimension, and the mixed generators vanish by the Cartan
formula, zero odd cohomology and evenness of the full K3 lattice.
This whole-domain proof includes rho_2(-beta_-); no sign-specific
numerical region is needed. Finally p_1(TX_R)=-48(e_1+e_2).

For the changed u=-p e_1-t e_2+tau_D, factor degree and (6) give

\[
\langle p_1(TX_R)u,[X]\rangle=48(p+t),\quad
\langle u^2,[X]\rangle=2pt+156.
\]

Thus the integer in (9) is J=12(p+t)+pt+78. Its residue is pt+6
modulo 12, giving exactly (4), with necessity and sufficiency.
An ordinary quaternionic line has group Sp(1)=SU(2) and trivial
complex determinant. Conversely determinant-trivial complex rank
two bundles admit that reduction. Rank truncation forces (2) for
any resulting bundle; no prescribed initial K-class or uniqueness
is asserted. In particular (4) implies the earlier 6-divisibility.

**Stable product and factor passage with the changed sign.** A
polystable rank-two locally free F is stable or a sum of two line
bundles of the same slope. In the latter case their first classes
are opposite, and ch_2(F)=c_1(L)^2. By Künneth and H^1(S)=0,
c_1(L)=x tensor 1+1 tensor y for divisor classes x,y. Its mixed
character is 2x tensor y and acts by zero on sigma. In (1) the mixed
action is -2lambda sigma, nonzero. Thus F must be stable. This
does not assume invariance of the individual line classes.

Under the cup-product tensor identification, diagonal SU(2) rotation
acts on mixed tensors by conjugation of their operators. L044's D
commutes with this action, so -D does also: a negative scalar on
the positive three-plane is still a scalar. Both pure top classes
are invariant. Consequently c_1(F) and c_2(F)=-beta_- are invariant.
Import Verbitsky, *Hyperholomorphic connections on coherent sheaves
and stability*, [arXiv:math/0107182v10, Theorem 3.9,
pp. 13--14](https://arxiv.org/pdf/math/0107182v10#page=13).
It supplies the stable F with a compatible hyperholomorphic unitary
connection. Definition 2.1, p. 9 includes this product metric;
invariance, not positivity of D, is the Chern-class hypothesis.

For every factor embedding j_y(z)=(z,y) or k_x(z)=(x,z), its tangent
map commutes with I,J,K. As in L051, naturality pulls the invariant
curvature back to an invariant endomorphism-valued surface two-form.
Verbitsky's Proposition 3.7 and Lemma 3.8, p. 13 give zero Kähler
contraction, coefficient by coefficient. The restricted unitary
connection is compatible with the restricted holomorphic bundle and
is Hermite--Einstein with constant zero. Kobayashi--Hitchin, e.g.
Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication,
[Chapter 9, Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
therefore gives slope-polystability at h. This proves the passage;
ordinary stability under restriction was not invoked. The mixed
term pulls back to zero, so all first-factor charges are m=-p and
all second-factor charges are n=-t.

**Exact factor filter and intersection.** Reuse the metric-dependent
zero-slope line lattice proved in L052:
NS(S) intersect h-perp=Z k, k=(-4,-2,1,2), q(k,k)=-14.
The unchanged surface RR and dual-stability inputs are Huybrechts,
[Chapter 1, (2.5)--(2.6) and Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and [Chapter 9, Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
A stable rank-two factor E of slope zero and c_1=0 has H^0(E)=0:
a section gives, after saturation, an effective determinant of
nonnegative h-degree, contrary to strict stability. The dual is
stable, so Serre duality gives H^2(E)=0. Surface RR gives
4-c=chi(E)=-h^1(E)<=0. Thus c>=4; c=4 is retained as a boundary
with no RR contradiction. This is only a necessary stable test.

A nonstable polystable factor is L direct sum L^{-1}: Pic^0(S)=0
and Picard torsion-freeness identify the second line. Both slopes
are zero, so its charge is -c_1(L)^2=14r^2. Conversely the two
line bundles of classes +/-rk give an actual polystable split
factor with this charge, including O_S^2 at r=0. Hence the union
of the numerical factor tests is {0} union {c in Z:c>=4}.

Intersect with mn=pt=6 mod 12. Zero is impossible. Charge four
is impossible because four times any integer cannot be 2 mod 4.
It follows that m,n>=5. Conversely every pair m,n>=5 with
mn=6 mod 12 passes the stable RR tests and the topological criterion,
and p+t=-m-n<=-10 automatically passes (8). This proves (5)
over the infinite integer domain, without assuming factor existence
for all admitted charges or compatible gluing on X.

Squares modulo 12 are 0,1,4,9, so m=n cannot pass. The least
possible charge sum is ten, where (5,5) fails; sum eleven gives
exactly (5,6) and (6,5), both passing. Since a+b=-m-n-8,
the maximal total is -19. Infinitely many examples are
(m,n)=(5,6+12j), j>=0. Charges five and six are not split values
14r^2, so any such factor is stable. The unchanged final region
is arithmetic compatibility only, with no F or transverse cycle.

Run `python3 scripts/cubic-kahler/check_sign_reversed_necessity.py`.
The bounded exact check and its full certificate are recorded in
`scripts/cubic-kahler/sign_reversed_necessity_certificate.json`.
It checks all 144 congruence pairs, exact rational root endpoints
and the minimal boundary; the preceding argument, not finite
enumeration, proves the infinite-region and topological assertions.

**Separate critical audit, 2026-10-08.** The approved audit found no
substantive error, additional exclusion or existence conclusion.
The following checks preserve the statement and its qualifications.

The integral class used in the finite-rank theorem is
u=-p e_1-t e_2+tau_D. Integrality comes from the actual integral
cycle and divisor correction in L044, via L048--L049, not from
separate integral realizations of the rational N and T projections.
For the full square, L048's trace calculation has divisor eigenvalues
2lambda_i and 4, and six copies of each 2lambda_i on T. Vieta gives
sum lambda_i^2=5, hence 4(5)+16+4(6)(5)=156. The even degree of
each tensor factor supplies no exterior sign; replacing D by -D
leaves this square unchanged. The tangent class is -48(e_1+e_2),
so the linear term in u remains 48(p+t), with no mixed contribution.
Thus the audited characteristic number is indeed
12(p+t)+pt+78, not its negative or a stable-rank surrogate.

All hypotheses of the corrected Čadek--Crabb--Vanžura Corollary 8.4
cited in (9) hold: X is a connected closed smooth spin eight-manifold,
l=0 is an integral lift of w_2, and u is integral. L050's complete
Künneth/Cartan argument proves Sq^2=0 on the entire mod-two degree-four
group, including classes with integral N/T gluing. The corollary's
finite-rank sufficiency, justified there through Proposition 8.2
and the splitting of a quaternionic summand when the Euler class
vanishes, supplies an actual quaternionic line. It is legitimate
to force the resulting rank-two character afterwards; no former
virtual K-class or stable representative is silently prescribed.

For the geometric passage, a locally free rank-two polystable
product bundle has only the stable and two-line alternatives.
The latter's mixed character annihilates sigma, whereas -tau_D
acts on it by -2lambda, so the stable hypothesis of Verbitsky's
Theorem 3.9 is established first. On H^2 the rotation representation
is the positive three-plane plus a trivial orthogonal complement.
Both D and -D commute with it. This verifies invariance of the full
c_2 without imposing positivity of the scalar or invariance on
unavailable line summands. The cited Definition 2.1 includes the
product hyperkähler metric, so irreducibility of X is unnecessary.

At every factor embedding j, equivariance of its tangent map gives
j^*(g R)=g(j^*R) for every quaternionic rotation g and the actual
curvature R. The action is on the form arguments; endomorphism
coefficients are unchanged. Thus each coefficient of j^*R is an
invariant surface two-form. The cited contraction result applies
to that surface form and yields Lambda_h(j^*R)=0. Compatibility
with the pulled-back holomorphic structure and the real-metric
Hermite--Einstein correspondence give polystability on every fibre,
including reducible ones. This uses neither restriction stability
nor a deduction from ambient zero contraction alone.

The unchanged exact-metric lattice in L052 was also checked against
L044's h and its integral divisor basis. Its three rationally
independent coefficients force (x,y,z,w)=r(-4,-2,1,2), with square
-14r^2. The factor alternatives therefore retain c=0 in the split
branch and c=4 in the stable Euler branch before intersecting with
mn=6 modulo 12. That congruence removes both values, and nothing
else in the tail c>=5 is removed by these particular tests. For
m,n>=5 the changed Bogomolov inequality is automatic. The minimal
sum eleven and the absence of symmetric pairs follow over all
integers as above; a finite scan is not their proof.

The existing checker was rerun: all 144 residue pairs, 20 passing
residue pairs and 1681 bounded intersection cases passed, with
minimum charge sum 11 and maximal correction total -19. Its full
certificate is at the path above. These checks corroborate the
arithmetic only. The audit is REPRODUCTION of the covered tools
and an EXPLORATION outcome with no substantive repair; the general
Hodge gap, holomorphic existence, gluing and transport remain open.

## Mathlib

Full sign-reversed specialization and finite-rank realization:
**not checked**. No matching Mathlib theorem or absence is asserted.
The precise primary theorems above and the canonical full-lattice
and exact-metric inputs supply the informal proof. Topological
SU(2) realization is distinct from a hyperholomorphic connection;
the latter passage is conditional on an actual stable holomorphic F.
