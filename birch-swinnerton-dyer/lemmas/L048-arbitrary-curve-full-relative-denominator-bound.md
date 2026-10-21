# L048 — Effective full-relative denominator bound for an arbitrary minimal curve

## Hypotheses

Let E/Q be given by a global minimal Weierstrass equation, with minimal
Neron differential omega_E and independently certified exact conductor
N. Let f be its associated normalized weight-two newform on Gamma_0(N),
with rational integer coefficients. CM and additive reduction are allowed.
Write

\[
 A_f(\{a,b\})=2\pi i\int_a^b f(z)\,dz,\qquad
 F(\{a,b\})=\frac{\operatorname{Re}A_f(\{a,b\})}{\Omega(E)},
 \qquad \Omega(E)=\int_{E(\mathbf R)}|\omega_E|.
\]

Paths are oriented from a to b. Work in the entire integral relative
weight-two symbol module M for Gamma_0(N), modulo torsion. Integral
generators mean actual cusp paths, or integral combinations of such
paths; rational-basis coordinates must not replace this lattice. The
conventions agree with L028 and the structural presentation in L038,
but neither lemma's non-CM arithmetic application nor any conditional
calibration is used as an input here.

No optimal equation, isogeny map, differential scalar, normalized symbol
value, twist value, rational point, Sha hypothesis or BSD assertion is
supplied. The exact conductor and newform association remain hypotheses.

## Conclusion

Define the following finite integer data independently of F. Set

\[
 \delta=\prod_{q\mid N}q^{\lfloor v_q(N)/2\rfloor},\qquad
 k=\max\bigl(1,\min\{j\ge0:N\le2^j\}\bigr),\qquad
 D=2^{Nk^2},\qquad A=6\cdot163D=978D.
\tag{1}
\]

Enumerate the first two distinct primes ell_1,ell_2 satisfying
ell_i>2, ell_i not dividing N, and ell_i=1 modulo delta. The congruence
is vacuous when delta=1. Compute exact point counts on the reductions
of the given target E, and put

\[
 T=\gcd\bigl(\#E(\mathbf F_{\ell_1}),
             \#E(\mathbf F_{\ell_2})\bigr),\qquad
 \boxed{B(E)=2AT=1956DT.}
\tag{2}
\]

Every F(x), for x in M, is rational, and its positive reduced denominator
is at most B(E). In particular this holds for every integral generator,
every oriented cusp pair, and every rational argument at every level.
The denominator of zero is one.

A size bound alone does not say that B(E) clears these values. A separate
computable common clearing integer is

\[
 \boxed{K(E)=2T\operatorname{lcm}(1,2,\ldots,A),\qquad
        K(E)F(M)\subseteq\mathbf Z.}
\tag{3}
\]

For a prime p this implies the all-argument valuation bound

\[
 v_p(F(x))\ge-C_p,\qquad
 C_p=v_p(2T)+\max\{j\ge0:p^j\le A\}.
\tag{4}
\]

These are terminating, possibly enormous bounds, not practical runtime
estimates. They supply a denominator input for possible independent exact
normalization recovery. They do not supply any exact F-value, certified
integration enclosure, nonzero coefficient, rational direction, rank or
Sha assertion, or complex-order comparison. L027 still needs exact
normalized values and its other hypotheses. The separate critical audit
below passes; no BSD candidate is asserted.

## Proof

**Imported results and their scope.** The prior source assessment is
[the arbitrary-curve specialization assessment](../drafts/literature/2026-10-11-arbitrary-curve-denominator-specialization.md),
with its complete source comparison. The following inputs are imported,
not reproved; only the assembly and period bookkeeping below are derived.

1. Modularity over Q gives the rational newform and canonical elliptic
   quotient E_f=J_0(N)/I_f J_0(N), Q-isogenous to E, and the normalized
   parametrization phi_0:X_0(N)->E_f with phi_0(infinity)=O. Use von Kanel,
   *Integral points on moduli schemes of elliptic curves*, Trans. London
   Math. Soc. 1 (2014), 85--115,
   [Section 5.2, Lemma 5.1(i) and its proof](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003).
   For a normalized weight-two exact-level N newform with rational integer
   coefficients, its modular degree m_f=deg(phi_0) satisfies
   log(m_f)<=N(log N)^2/2. This bounds the canonical quotient, not an
   arbitrary target map, and assumes no Manin constant one.
2. The named Mazur--Kenku classification of rational cyclic isogenies,
   applied to a minimal-degree Q-isogeny between Q-isogenous elliptic
   curves, gives degree at most 163. Use the complete argument in
   [von Kanel, Section 4, proof of Lemma 4.1](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003),
   importing Kenku, J. Number Theory 15 (1982), 199--202, Theorem 1.
   Minimality makes the kernel cyclic, as explained there. Kenku's
   original proof was not inspected; the standard named classification
   and the inspected specialization are the source input. CM is not
   excluded. This is an existence bound, not a constructed map.
3. Cesnavicius--Neururer--Saha, *The Manin constant and the modular degree*,
   author PDF dated 28 January 2022,
   [Theorems 1.2 and 7.2, pp.3,45--46](https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=45),
   applies to any surjective parametrization at the target's exact
   conductor, in particular from X_0(N). Its minimal differential
   pullback is c_phi omega_f, for a nonzero integer c_phi, and
   c_phi divides 6 deg(phi). Retain the unrestricted factor six; do not
   use the sharper conclusion without its additional conductor conditions.
4. Manin--Drinfeld makes cusp differences torsion in J_0(N). The cusp
   field and torsion-reduction argument is imported from Wuthrich,
   *Numerical modular symbols for elliptic curves*,
   [arXiv:1608.06423v2, 23 March 2017, Proposition 1 and complete proof,
   pp.3--4](https://arxiv.org/pdf/1608.06423v2#page=3).
   Every cusp of X_0(N) is defined over Q(zeta_delta), for delta in (1).
   Images relative to the rational infinity cusp are consequently torsion
   over that field under any Q-parametrization. At a good prime ell>2
   splitting completely in this field, torsion reduction is injective,
   including ell-primary torsion: its local ramification index is one,
   less than ell-1. The proof cites Silverman, *The Arithmetic of Elliptic
   Curves*, second edition, VII.3.4. Wuthrich's displayed formula assumes
   c_0=1 and includes source/target period ratios; that displayed conclusion
   is not imported here. We retain the arbitrary target scalar instead.
5. For the full minimal period lattice Lambda_E in C, stable under
   conjugation, Cremona, *Algorithms for Modular Elliptic Curves*, corrected
   second edition (1997),
   [Section 2.8, p.30, following (2.8.9)](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=24),
   gives Re(Lambda_E)=(Omega(E)/2)Z for either real-lattice type. Integral
   relative generation is Stein, *Modular Forms, a Computational Approach*,
   GSM 79 (2007), [Propositions 3.10--3.11 and Theorem 3.13,
   pp.42--44](https://wstein.org/books/modform/stein-modform.pdf).
   Weight two and trivial character are precisely the present setting.

**Bounded existential parametrization.** Choose, only for the proof,
a minimal-degree Q-isogeny psi:E_f->E. Its degree d satisfies 1<=d<=163.
The composition phi=psi phi_0 is defined over Q, has phi(infinity)=O,
and has degree d m_f. No coefficients of either map or equation for E_f
are used to compute (1)--(2).

Since N<=2^k and 0<log 2<2,

\[
 \log m_f\le\frac{N(\log N)^2}{2}
 \le\frac{Nk^2(\log2)^2}{2}
 \le Nk^2\log2=\log D.
\]

Thus m_f<=D. Apply the unconditional Manin theorem to phi and the
specified minimal differential of E:

\[
 \phi^*\omega_E=c\,2\pi i f(z)\,dz,
 \qquad c\in\mathbf Z\setminus\{0\},\qquad
 |c|\le6\deg\phi\le6\cdot163D=A.
\tag{5}
\]

Changing an orientation or differential sign changes c's sign, which
does not affect the bound. The theorem's hypotheses use E's independently
certified exact conductor N; no inferred optimality of E is needed.

**Computable torsion annihilator at every cusp.** Let
L=Q(zeta_delta). Dirichlet's theorem on primes in reduced residue
classes supplies infinitely many primes 1 modulo delta when delta>1;
for delta=1 infinitude of primes suffices. Removing the finitely many
primes at most two or dividing N leaves two primes, so the enumeration
terminates. Such primes are unramified and split completely in L.

Each P_a=phi(a), for any cusp a, lies in E(L)_tors: the divisor
(a)-(infinity) is torsion by Manin--Drinfeld, and the map induced on
the Jacobian sends it to phi(a)-phi(infinity)=P_a. This includes all
cusp orbits, not merely infinity, zero or unitary cusps. Choose a prime
of L above each ell_i. Its residue field is F_(ell_i), the target has
good reduction because ell_i does not divide N, and the cited injectivity
applies. By Lagrange's theorem, #E(F_(ell_i)) kills every P_a. A Bezout
combination of the two counts shows that T kills every P_a. Consequently

\[
 T(P_b-P_a)=O
\tag{6}
\]

for every ordered pair of cusps, including equal endpoints. The counts
are positive integers and can be obtained by exhaustively evaluating the
given minimal equation over each finite field, including the point at
infinity. Trial division factors N and tests the enumerated primes, so
all input computations in (1)--(2) are finite and independent of F.

**Full relative paths and both real-lattice cases.** Under the complex
uniformization E(C)=C/Lambda_E for omega_E, the image of the oriented
path {a,b} has Abelian integral c A_f({a,b}), by (5); its class modulo
Lambda_E is P_b-P_a. Cusp integrals converge because f is a cusp form.
Equation (6) therefore implies

\[
 T c A_f(\{a,b\})\in\Lambda_E.
\tag{7}
\]

This argument uses both endpoints and applies to a relative path before
any restriction to absolute cycles. Taking real parts in (7) gives

\[
 \boxed{2Tc F(\{a,b\})\in\mathbf Z.}
\tag{8}
\]

For clarity, the full-lattice period convention retains the component
factor in each case. If the lattice is rectangular, generated by a
positive real period omega_1 and a purely imaginary period, then E(R)
has two components, Omega(E)=2omega_1 and Re(Lambda_E)=omega_1 Z.
If it is nonrectangular, take generators omega_1>0 and
omega_1/2+i b with b>0. Then E(R) has one component,
Omega(E)=omega_1 and Re(Lambda_E)=(omega_1/2)Z. Both give precisely
Re(Lambda_E)=(Omega(E)/2)Z and (8). Using only a purely real lattice
generator would miss this uniform factor two in the connected case.

Integration is the usual additive functional on the integral relative
symbol module. It kills torsion, since its values lie in a characteristic
zero vector space. Stein's integral generation theorem expresses every
element of M as an integral combination of cusp paths, so (8) holds for
every x in M. Equivalently, it already holds on every actual Manin
generator, and integral linear combinations preserve it. No rational
change-of-basis denominator, discarded boundary or sampled subset is used.

Put a=|c|. Equation (8) implies that F(x) is rational with reduced
denominator dividing 2Ta. Since 1<=a<=A, that denominator is at most
2TA=B(E), proving (2). We have not asserted that a divides A or that
2Ta divides B(E); this is a size comparison only. Separately, every
integer a in [1,A] divides lcm(1,...,A), so (8) proves (3). The exponent
of p in this lcm is the greatest j with p^j<=A, proving (4), including
zero values with valuation infinity. This also shows why finite integral
sums cannot undermine the all-argument bound: they share one actual,
though unknown, clearing factor 2Ta.

**Applicability and limitations.** The computation of B(E), K(E) or
C_p never calls for the existential maps, c, an optimal model or period
ratios. Modularity, the classification, the factor-six theorem and cusp
torsion are the known inputs, and the result is their specialization,
not new mathematics beyond the checked sources. The denominator
criterion passes the stated continuation test. Its usefulness for exact
recovery still requires independently certified integration/period
enclosures; none is constructed here. Denominator bounds do not imply
nonvanishing, and CM allowance here does not extend the non-CM downstream
hypotheses of L027. All rank, Sha and complex-order gaps remain separate.

**Separate critical audit, 2026-10-11.**
BSD-2026-10-11-161-arbitrary-denominator-critical-audit checks the entire
statement and proof under the unchanged approved audit assessment.
The audit passes without changing the hypotheses or numerical bounds.
This is validation of the known-source specialization, not a result
beyond the inspected literature. The independent checks are as follows.

* The degree theorem concerns precisely the canonical quotient E_f.
  The bounded Q-isogeny has source E_f and target E; composing in that
  direction gives degree d m_f. In the logarithmic estimate the last
  inequality is equivalent to log(2)<=2, so the integer majorant D is
  valid. The unrestricted Manin theorem applies to this composite at
  the target's exact conductor. Integrality and nonzeroness of c are
  essential: a mere rational scalar with bounded absolute value would
  not prove the denominator conclusion. The imported theorem supplies
  both, and divisibility by 6 deg(phi) gives |c|<=978D. No isogeny
  differential, optimal equation or period ratio is used computationally.
* Every cusp is rational over the same field L, and phi(infinity)=O.
  Thus Manin--Drinfeld applies to each endpoint individually under the
  induced Jacobian map. At either selected prime the completion of L
  is Q_ell: splitting gives residue degree one and ramification index
  one. Since ell>2, the imported torsion-injectivity criterion e<ell-1
  holds, including ell-primary torsion. Each full target point count
  annihilates every endpoint image; their gcd does too. It is not merely
  a bound on a prime-to-ell part, and no coprimality of the two point
  counts is assumed. Subtracting the two endpoint images proves (6),
  also for coincident endpoints and paths with nontrivial absolute part.
* Pullback and complex uniformization identify the same c A_f with the
  path integral on E, modulo the full period lattice. Multiplication
  by T closes its endpoint difference, proving (7). For a rectangular
  lattice the least positive real projection is omega_1 and the total
  real period is 2 omega_1. For the nonrectangular lattice the real
  projections are generated by omega_1/2 and the total real period is
  omega_1. Consequently (8) has exactly the required uniform factor
  two. Replacing real projection by intersection with the real axis
  would fail in the second case; the proof makes no such replacement.
* The quantifiers are one fixed c for every x, not a separately chosen
  scalar for each generator. Integration descends to relative homology
  and kills torsion; integral generation therefore preserves the single
  clearing factor 2T|c|. This checks arbitrary integral sums as well as
  cusp paths. Rational arguments at all levels mean cusp paths such as
  {infinity,a/p^n} on X_0(N), not arbitrary rational multiples in
  M tensor Q; no bounded-denominator claim is made for the latter.
  With a=|c|, each reduced denominator divides 2Ta, hence is <=2TA.
  This does not imply divisibility by 2TA. The separate lcm is divisible
  by this same a and proves (3); its exact p-exponent is the greatest
  j with p^j<=A, proving (4). Zero has denominator one and valuation
  infinity, consistent with every conclusion.
* Factoring the supplied integer N, forming integer powers, enumerating
  and testing primes, counting points, and taking gcd/lcm all terminate.
  The required progression contains infinitely many primes, and only
  finitely many are excluded. The counts use the given minimal target
  itself. None of these computations queries F, c or phi. The bound is
  effective without a promised practical runtime. CM and additive
  reduction are not excluded by any of the imported bounds; chosen
  reduction primes remain good. Downstream non-CM restrictions remain.

The original Kenku proof and Manin's presentation-injectivity proof remain
unread, as recorded in the approved coverage; their named results are
imported, not independently reproved by this audit. Only Stein's integral
generation is needed here. The audit used the saved primary statements
and inspected-source qualifications; no new source claim or numerical
certificate is substituted for a proof. Independent integration and
total-period enclosures, exact recovery and all BSD gaps remain open.

## Mathlib

Full matching arbitrary-curve effective full-relative denominator theorem:
not checked. Supporting modularity/optimal quotient, Mazur--Kenku,
effective modular degree, Manin constant, cusp torsion and torsion reduction,
total real periods and integral Manin generation: not checked. Basic
integer bounds, gcd/Bezout and lcm support: not checked. No absence claim
follows. The named theorem imports above and their precise specializations
are the mathematical evidence; no software experiment is used as proof.
