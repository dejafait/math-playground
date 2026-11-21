# C759i: The fixed even quartics obstruct all-times positivity preservation

## Hypotheses

Use C759a(1),(5)-(6) and Proof1: the complete, unneutralized real
closed semibounded form Q on zero-extended L2(-1,1), restricted to
the even subspace H_e. Let A_e be its self-adjoint form operator.
In the Fourier convention F_f(t)=integral f(x)exp(-itx)dx, write

\[
\begin{split}
Q(f)&=q_m(f)+2F_f(i/2)F_f(-i/2)
       -2\sum_{n\in\{2,3,4,5,7\}}a_n C_f(\log n),\\
q_m(f)&=\int_{\mathbb R}m(t)|F_f(t)|^2\frac{dt}{2\pi},\quad
m(t)=\Re\psi(1/4+it/2)-\log\pi,\\
C_f(d)&=\int_{\mathbb R}f(x+d)f(x)dx,\qquad
a_n=\Lambda(n)/\sqrt n.
\end{split}                                                    \tag{1}
\]

This is the H1 specialization of Suzuki, *Weil's quadratic form via
the screw function*, [arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2#S2.SS4),
Section2.4, (2.7) and the following complete-form passage; its closed
realization and core are imported as in C759a (Theorem1.1,
Corollary1.2, Sections3.2,4.1-4.2,4.5). No source positivity theorem
or certificate is used. C759a justifies this normalization and the
closed domain at half-width1. The five terms in (1) are the entire
overlapping prime-power list, since log7<2<log8 and Lambda(6)=0.

Take exactly C759h's fixed pair, with no parameter variation:

\[
h(s)=(\max\{1-s^2,0\})^2,\quad
u(x)=h(40(x-1/5))+h(40(x+1/5)),\quad
v(x)=h(40(x-4/5))+h(40(x+4/5)).                         \tag{2}
\]

The imported order theorem is Manavi–Vogt–Voigt, *Domination of
semigroups associated with sectorial forms*, J. Operator Theory54
(2005),9–26, [author manuscript](https://user.math.uni-bremen.de/hvogt/papers/mvv01.pdf),
Section2, Theorem2.1, Corollary2.6 and Remark2.7, manuscript pp3–7.
Only necessity of the real symmetric Beurling–Deny criterion is used:
a positivity-preserving semigroup associated with a densely defined
closed semibounded real form on a Hilbert lattice must satisfy
q(f^+,f^-)<=0 (and the modulus inequality) on its real form domain.
This is a REPRODUCTION under assessment824, with no originality claim.

## Conclusion

For the complete form (1) and the single pair (2),

\[
\boxed{\Delta_e:=Q(u+v)-Q(u-v)>\frac{32}{5625}>0.}       \tag{3}
\]

Both u-v and its modulus u+v are in the even form domain. Thus the
semigroup family exp(-tA_e), t>=0, cannot preserve the pointwise
positive cone for every t>0. Equivalently, preservation fails at some
positive time; no particular time is specified. Adding any real scalar
shift to the form does not repair this obstruction.

This does not decide positivity at the single resolvent parameter-16,
existence or sign of a ground state, simplicity, parity ordering,
actual-Xi realization, all-degree mixed positivity or RH. It does not
assert Q(u-v)<0. The result is a scoped negative test of this order
mechanism, not a verified complete solution or new general theory.

The scoped conclusion passed the independent conceptual audit in
Proof6 (13 November 2026, step828). No bound or conclusion was enlarged.

## Proof

### 1. Domain, supports and scalar cancellations

The zero extension of each bump in (2) is C1 and piecewise polynomial:
both (1-s²)² and its first derivative vanish at s=±1. Its weak first
derivative is square integrable, with no jump term. Thus u,v and
u±v belong to H1_0(-1,1), hence to C759a's closed form domain; this
also agrees with C759h Proof2's stronger operator-domain statement.
They are even and nonnegative where asserted. Each bump has radius
1/40 and the u and v supports are disjoint, so

\[
(u-v)^+=u,\quad (u-v)^-=v,\quad |u-v|=u+v,\quad
\|u+v\|_2^2=\|u-v\|_2^2.                              \tag{4}
\]

For d>0 define the nonnegative mixed correlation

\[
H(d)=\int[u(x+d)v(x)+v(x+d)u(x)]dx.
\]

Expansion before applying any kernel gives

\[
C_{u+v}(d)-C_{u-v}(d)=2H(d).                           \tag{5}
\]

In particular both self-correlations C_u(d)+C_v(d) cancel exactly.
The four positively oriented cross pairs have center separations
3/5,3/5,1,1: respectively -4/5 to -1/5, 1/5 to4/5,
-4/5 to1/5, and -1/5 to4/5. Their radii add to1/20. Consequently

\[
\operatorname{supp}H\subset
[11/20,13/20]\ \cup\ [19/20,21/20].                   \tag{6}
\]

This treats both difference and sum separations from reflection.
Endpoint contacts contribute zero; the bumps themselves vanish there.

### 2. Every arithmetic term in the difference is exactly zero

Here are elementary strict logarithm bounds, avoiding rounded values.
For 0<t<1, j!>=2*3^(j-2) for j>=2 gives

\[
e^{13/20}\le1+13/20+
 \frac{(13/20)^2}{2(1-13/60)}=\frac{3609}{1880}<2.
\]

Also e^(19/20)>1+19/20+(19/20)²/2=1921/800>2. Hence
13/20<log2<19/20. For j>=3, j!>=6*4^(j-3), with strict inequality
from j=5, gives e<5/2+(1/6)/(1-1/4)=49/18. The exponential series
also gives e^(1/20)<20/19. Therefore

\[
e^{21/20}<\frac{49}{18}\frac{20}{19}
 =\frac{490}{171}<3,\qquad \log3>21/20.               \tag{7}
\]

The complete delay check is thus:

| n | Location relative to the two cross bands | H(log n) |
|---|---|---|
| 2 | 13/20<log2<19/20 | 0 |
| 3 | log3>21/20 | 0 |
| 4 | log4>log3>21/20 | 0 |
| 5 | log5>log3>21/20 | 0 |
| 7 | log7>log3>21/20 | 0 |

Using (5), the complete arithmetic difference in (1) is
-4 sum_n a_n H(log n)=0. No prime-power tail has been dropped.
This does not declare each individual C_{u±v}(log n) zero:
in particular a v self-interaction near log5 must not be excluded.
Every self term cancels by (5), before the delay check or any limit.

### 3. Full gamma and polar difference on these H1 tests

Use the imported regularized digamma identities of L741(7),(13),(16)-(17)
and L744 Proof1,(5)-(6). Their analytic source is the digamma integral
[DLMF5.9.13](https://dlmf.nist.gov/5.9.E13), with real part1/4 in the
present argument. Put

\[
k(d)=\frac{2e^{-d/2}}{1-e^{-2d}},\quad
r(d)=k(d)-e^{-d}/d\in L^1(0,\infty),\quad c=\log(2\pi).
\]

On real smooth compact tests these identities give
q_m(f)=-Re<(B+cI+R)f,f>, where R is causal convolution by r and

\[
B_\epsilon f=\int_\epsilon^\infty\frac{e^{-d}}d
 [f(\cdot-d)-f]dd\ \longrightarrow\ Bf\text{ in }L^2.
\]

Apply this first to any smooth separated approximations of u and v.
In the difference at their sum and difference, (4) cancels the c
term and the subtraction -f in B_epsilon **before** taking a limit.
Equation(5) then gives -2 integral e^(-d)H(d)/d from B and
-2 integral r(d)H(d) from R, so the gamma difference is

\[
q_m(u+v)-q_m(u-v)=-2\int_0^\infty k(d)H(d)dd.          \tag{8}
\]

Here is the precise extension of that calculation to (2). Mollify
u and v by the same nonnegative even smooth approximate identity
of radius epsilon<1/100. The approximants are even smooth compact
tests in (-1,1), with disjoint u/v supports and cross separations
in the common compact interval [1/2,11/10]. They converge in H1(R).
C759a(5) bounds |m(t)| by a constant times 1+log(1+t²), and hence
by a constant times 1+t². Plancherel therefore gives convergence
of q_m at their sums and differences by weighted Cauchy–Schwarz.
The smooth correlations H_epsilon converge to H in L1(0,infinity):
extend to the whole line and apply the L1 convolution inequality
to the two product differences. Compactly supported H1 convergence
implies the required L1 convergence of u_epsilon and v_epsilon.
Since k is bounded on that common interval, the integrals in (8)
converge as well. This proves (8) for the actual quartics, without
calling them smooth or assuming a universal lattice-domain property.
The regularization parameter in B is taken to zero at the smooth
stage; the separated supports eliminate its singular neighborhood.

For either sign, finite-square Fubini in the two polar functionals
of (1) gives

\[
2F_f(i/2)F_f(-i/2)
 =4\int_0^\infty\cosh(d/2)C_f(d)dd.
\]

Indeed symmetrizing exp((x-y)/2) gives cosh((x-y)/2), and the two
half-squares agree. Thus (5) yields the polar difference
8 integral cosh(d/2)H(d)dd. Both poles have been retained. Also,
because u,v are even, F_{u±v}(i/2)=F_{u±v}(-i/2)=c_u±c_v,
where c_u=integral u(x)cosh(x/2)dx and similarly for c_v; the
same difference is 8c_uc_v. This checks the polarization factor.
All these finite-support integrals are absolutely convergent.
Combining (8), the poles and the exact arithmetic cancellation gives

\[
\Delta_e=2\int_0^\infty[4\cosh(d/2)-k(d)]H(d)dd.        \tag{9}
\]

### 4. Exact strict sign certificate

For d>=11/20, the positive exponential series gives

\[
e^{2d}\ge e^{11/10}>
 \sum_{j=0}^{5}\frac{(11/10)^j}{j!}
 =\frac{36015101}{12000000}>3.
\]

Consequently 1-e^(-2d)>2/3 and e^(-d/2)<1, whence k(d)<3.
Since cosh(d/2)>=1, the bracket in (9) is strictly greater than1
throughout (6). One single bump has the exact positive mass

\[
A=\frac1{40}\int_{-1}^1(1-s^2)^2ds
 =\frac1{40}\left(2-\frac43+\frac25\right)=\frac2{75}.
\]

Nonnegative Fubini, partitioning the cross square by the two
orientations, gives
integral_0^infinity H(d)dd=(integral u)(integral v)=4A².
Equivalently the four oriented bump pairs each contribute A².
Equations(6),(9) therefore yield
Delta_e>2*4A²=32/5625, proving (3). Strictness follows from the
strict kernel bound and the positive H mass. This is a complete
analytic certificate; no numerical quadrature or mathematical script
is required, and the required threshold was zero.

### 5. Ordered even space and the necessary criterion

The map U:H_e -> L2((0,1),dx), (Uf)(x)=sqrt(2)f(x), is an onto
real Hilbert-lattice isometry: ||Uf||²=2 integral_0^1|f|²=||f||²,
its inverse is (U^(-1)g)(x)=g(|x|)/sqrt(2), and U|f|=|Uf|.
No Dirichlet condition at0 is imposed. Transport Q and its domain
by U. C759a's reflection-invariant closed dense domain makes the
transported form densely defined, closed, real symmetric and
semibounded. These are the cited theorem's hypotheses. They do not
assert that the entire form domain is stable under modulus.

For this particular f=u-v, domain admissibility of f,|f|,f^+,f^-
was established in Section1. Real bilinear polarization gives
q(u,v)=Delta_e/4>8/5625>0, contradicting the necessary condition
q(f^+,f^-)<=0 if the semigroup were positive for all t>0. Equivalently
Q(|f|)>Q(f) contradicts its symmetric modulus consequence.

For any real shift mu, (4) makes the norm contribution to Delta_e
zero, and <u,v>=0 leaves q(u,v) unchanged. If nonnegativity is
desired in the theorem, C759h's A_e>=-10I permits mu=10;
exp(-t(A_e+mu I))=exp(-mu t)exp(-tA_e), with a positive scalar
factor. Thus the semibounded version and its shifted version give
the same obstruction. One failed necessary inequality supplies no
affirmative statement about other positivity or spectral properties.

### 6. Independent conceptual audit, 13 November 2026, step828

This is a REPRODUCTION audit under the unchanged, separately approved
`drafts/literature/2026-11-13-even-fixed-quartic-obstruction-audit-826.md`.
The full proof above and the prescribed ranges of C759a, C759h, L741
and L744 were checked. The inspected primary-theorem coverage in
assessments823/824 is reused; the cited source theorems are imported,
not independently reproved. No mathematical correction was needed.

**Realization and admissibility.** C759a(5)-(6), Proof1, identifies
the closure of the smooth form with the supported Fourier space of
weight 1+log(1+t²)/2. The weight differs from m by a bounded function;
the finite shifts and finite-interval pole functionals are bounded in
L2. Thus the closed dense semibounded realization and its reflection
restriction used here have the required hypotheses. This uses neither
L741's length-log3 sign theorem nor Suzuki's small-window positivity.
H1_0 is contained in that form domain by the weight comparison.
The value and first derivative of each quartic vanish at its two
endpoints, so zero extension introduces no distributional jump in its
first derivative. All four parts f, |f|, f^+, f^- for f=u-v are the
specific admissible H1 functions in (4). No assertion about modulus
on the entire form domain is needed for this negative test.

**Supports, delays and cancellation.** Enumerating the centers
-4/5,-1/5,1/5,4/5 gives precisely the four u/v ordered pairs in
Proof1, two at separation3/5 and two at1. Each pair's radius sum is
1/20. The other center differences are self-pairs and cancel in (5).
In particular, the v self-pair at8/5 may interact with log5 in either
individual energy; declaring it absent would be wrong, but the proof
does not do so. The rational exponential bounds replay as
3609/1880<2, 1921/800>2 and 490/171<3. They place log2 strictly
between the two cross bands and log3 strictly after the second band.
Monotonicity covers4,5,7. C759a's complete delay list excludes all
n>=8 by log8>2; Lambda(6)=0. Hence the entire arithmetic difference
vanishes, without dropping a tail or a self-interaction.

**Regularization and the H1 limit.** For a smooth separated pair,
L741(7),(13),(16)-(17) gives the full-line symbol of -Re(B+cI+R),
equal to m; L744 Proof1 explicitly permits this identity at arbitrary
fixed interval length. Translation or restriction of the pairing
introduces no boundary term because the test is zero extended.
For each cutoff delta in B, the equal squared norms cancel both the
cI term and its subtractive scalar term. The remaining difference is
-2 integral_delta^infinity e^(-d)H(d)/d dd minus
2 integral_0^infinity r(d)H(d) dd. For sufficiently small delta,
H vanishes on the removed neighborhood, so this equals
-2 integral_0^infinity k(d)H(d) dd. This justifies taking that
cutoff limit before mollification is removed.

For completeness, let f_j be either u_j+v_j or u_j-v_j for the
smooth approximants, with limit f=u+v or u-v. Set W(t)=1+t² and
||G||_W²=integral W(t)|G(t)|²dt/(2pi). Since |m|<=M W for some
finite M, weighted Cauchy--Schwarz gives

\[
 |q_m(f_j)-q_m(f)|
 \le M\|F_{f_j}-F_f\|_W
             (\|F_{f_j}\|_W+\|F_f\|_W)\longrightarrow0.
\]

Plancherel identifies this convergence with H1 convergence. For the
correlation side, write check(v)(x)=v(-x). Each mixed correlation is
a convolution of one function with the reflection of the other. For
example Young's L1 inequality bounds the difference by

\[
 \|(u_j-u)*\check v_j\|_1+
 \|u*(\check v_j-\check v)\|_1
 \le \|u_j-u\|_1\|v_j\|_1+\|u\|_1\|v_j-v\|_1\to0.
\]

The reversed term has the same bound. Common finite support gives
the L1 convergence from L2 convergence. The approximants' cross
supports lie in [1/2,11/10], where k is bounded, so the integrals
converge. These estimates verify the complete passage to (8), rather
than just convergence of sampled or pointwise Fourier values. The
finite shifts and the two pole functionals are L2-continuous as well.

**Both poles and the exact margin.** Finite-square symmetrization
gives 2F_f(i/2)F_f(-i/2)=4 integral cosh(d/2)C_f(d) dd for real f.
Combining it with (5) gives the factor8 in the polar difference;
the even identity 8c_uc_v checks the same factor independently.
The gamma factor is -2, so (9) has exactly the bracket4cosh-k.
The exponential partial sum in Proof4 is exactly
36015101/12000000=3+15101/12000000>3. Therefore k(d)<3 and
4cosh(d/2)-k(d)>1 on both cross bands. Each bump mass is2/75.
Integrating H over positive d partitions the u-v product square
into its two orientations; the diagonal has measure zero. It gives
4(2/75)²=16/5625, including all four pairs. Thus Delta_e>32/5625,
against the required threshold0, and q(u,v)>8/5625. No numerical approximation,
external positivity certificate or unresolved spectral sign enters.

**Order theorem and scope.** The displayed map U is onto, preserves
the L2 norm, and commutes with positive and negative parts as well
as modulus. The even real space is consequently the required Hilbert
lattice, while the transported form is closed, dense, symmetric and
semibounded. Manavi--Vogt--Voigt Corollary2.6/Remark2.7, with its
Theorem2.1 necessity argument, applies to this form. If all exp(-tA_e)
preserved the cone, it would impose q(u,v)<=0 on the particular
admissible parts of f. Real polarization instead gives
q(u,v)=[Q(u+v)-Q(u-v)]/4>0. No converse or unverified full-domain
lattice property is used. Orthogonality of u and v makes every scalar
shift irrelevant. Abstract semiboundedness already supplies a sufficient
shift; the optional explicit shift10 in Proof5 also follows from
C759h Proof1 using C759a's audited prime bound C<313/100.

The accepted conclusion is that positivity preservation fails for
some positive time. It is not failure at every time, a sign assertion
at parameter-16, a negative value of Q, or a theorem about a ground
state. The main positivity, ground-state sign/simplicity, parity and
Xi-realization gaps remain. This audit establishes a usable scoped
obstruction, not progress beyond the imported general order theory.

## Mathlib

Full matching theorem and supporting theorem coverage were not checked.
No absence or formal-verification claim is made. The imported results
are the cited complete-form/closed-realization and regularized digamma
identities, and Manavi–Vogt–Voigt's necessary semigroup-order criterion.
The support, H1 specialization, polarization and rational sign bound
above are the local reproduction, independently checked in Proof6.
Mathlib matching and supporting coverage remain unchecked after that
informal audit; no formal verification is claimed.
