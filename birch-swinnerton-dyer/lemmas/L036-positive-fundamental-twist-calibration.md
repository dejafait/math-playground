# L036 — Conditional positive fundamental-twist calibration

## Hypotheses

Let E/Q be non-CM, given by a global minimal Weierstrass equation, with
minimal discriminant Delta_E and conductor N. Let p>=5 be good ordinary,
and let f be its normalized weight-two newform. Retain the primitive
untwisted trivial branch and kappa(gamma)=1+p used in L028 and L027.
Write Omega(E)=integral_(E(R)) |omega_E| for the **total** real Neron
period of the minimal differential.

Grant the following certified data, as in L028, with the changed twist
conductor in item 3.

1. A complete finite integral presentation of the entire torsion-free
   relative weight-two modular-symbol module M=M_2(Gamma_0(N)),
   with oriented integral Manin generators g_1,...,g_s and all relations:
   M=Z^s/R_sat, where R is the full Manin relation module and
   R_sat={v in Z^s: kv in R for some integer k>=1}. The identification
   includes every cusp path {a,b}, oriented from a to b, and certifies
   every coordinate change and relation witness.
2. A nonzero rational functional phi on M_Q, with exact rational values
   x_i=phi(g_i) satisfying all relations. A certified line U=Q phi in the
   **full relative dual** has real extension containing
   I({a,b})=Re(2 pi i integral_a^b f(z) dz), on all of M. No scalar between
   I and phi is supplied, and no rationality of that scalar is assumed.
   An absolute-cycle line, software plus label or sampled eigenvalues
   does not meet this hypothesis.
3. An odd positive fundamental discriminant D>1, with gcd(D,p Delta_E)=1,
   and the primitive quadratic character chi_D of conductor D. Grant an
   exact rational q with an independent proof that
   q=L(E^D,1)/Omega(E^D) != 0. Here E^D is the minimal positive quadratic
   twist, L is its **full** Hasse--Weil L-function, and its total period
   uses the minimal differential. The certificate for q must not use the
   unknown scalar of phi.

Values in rational-basis coordinates must be converted exactly to values
on every integral generator, retaining all coordinate denominators. Full
presentation and real-line certification and independent q production
are substantial granted inputs. No BSD assertion, finite Sha, positive
rational rank, optimality, Manin constant one or L(E,1)!=0 is assumed.

## Conclusion

With chi=chi_D, extended by zero on nonunits, define

\[
G_D=\sum_{a=0}^{D-1}\chi(a)\{\infty,a/D\}\in M,
\qquad d=\phi(G_D)\in\mathbf Q.
\]

Then d!=0, and on the **entire relative module** the exact normalized map is

\[
\boxed{F=\frac{q}{d}\phi=\frac{I}{\Omega(E)}.}\tag{1}
\]

In particular S(r)=F({infinity,r}) is L027's total-real-Neron-normalized
plus symbol for every rational r. Let y_i=(q/d)x_i and put

\[
\boxed{C=\max\bigl(\{0\}\cup
       \{-v_p(y_i):y_i\ne0,\ 1\le i\le s\}\bigr).}\tag{2}
\]

This is a finite nonnegative integer, F(M) is contained in p^(-C) Z_p,
and v_p(S(r))>=-C for **every** rational r, including every level and
both argument families in L027.

This extends the applicability of L028's conditional certificate; it
constructs no actual q, line, presentation, numerical C or coefficient.
The later coefficient test still requires
min(n-1-C,M_prec-C)>v_p(b), with M_prec the unit-root residual precision
in L027. No claim that this strict threshold is met follows here.

## Proof

**Primitive-character input and removal of the auxiliary period.** Import
Bertolini--Darmon, *Hida families and rational points on elliptic curves*,
Invent. Math. 168 (2007), 371--431,
[Section 1.1, Proposition 1.3 and preceding definitions, author PDF
pp. 6--8](https://www.math.mcgill.ca/darmon/pub/Articles/Research/42.Hida-families/paper.pdf).
It applies to a normalized cusp form of even weight k>=2, a primitive
quadratic character of conductor m, a critical integer 1<=j<=k-1, and
chi(-1)=(-1)^(j-1) w_infinity. Take g=f, k=2, j=1, m=D and
w_infinity=+1; our chi is primitive and even. The polynomial is 1.
In its notation, with auxiliary Shimura period Omega_f^+, the formula is

\[
\frac{\tau(\chi)L(f,\chi,1)}{\Omega_f^+}
 =\sum_{a\bmod D}\chi(a)
   \frac{\widetilde I_f^+(\{\infty,a/D\})(1)}{\Omega_f^+}.
\tag{3}
\]

Multiply by this nonzero auxiliary period. It is cancelled, **not**
identified with Omega(E). On these paths the plus component is the real
part of A(r)=2 pi i integral_infinity^r f(z) dz: the reflection sends
r to -r, and A(-r)=conjugate(A(r)) since f has real coefficients.
This is the orientation/conjugation calculation in L028, independent
of its prime-twist identity. Thus the right side after cancellation
is I(G_D), with no extra half-projection of G_D in the integral lattice.
The standard positive quadratic Gauss-sum convention is
tau(chi_D)=sqrt(D)>0; import its stated convention from
Stein--Wuthrich, *Algorithms for the arithmetic of elliptic curves using
Iwasawa theory*, Math. Comp. 82 (2013),
[Section 3.7, p. 1768](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=12).
Consequently

\[
I(G_D)=\sqrt D\,L(f,\chi_D,1).\tag{4}
\]

There is no prime-conductor assumption in Proposition 1.3. Its sum
includes all residues; chi(a)=0 for every nonunit, including a=0.
These zero terms are retained in the definition rather than replaced by
an imprimitive character. We import the theorem, including the
composite-conductor case, without attempting a new Gauss-sum proof or
interchanging a Fourier series with an endpoint integral. Its displayed
orientation is already infinity to a/D, so no conversion from zero to
a/D and no subtraction of an untwisted central value is needed.

**Full finite Euler factors.** Import the coprime-conductor comparison
in Wiersema--Wuthrich, *Integrality of Twisted L-Values of Elliptic Curves*,
Documenta Math. 27 (2022), 2041--2066,
[Section 1, pp. 2042--2043 and Section 7, pp. 2058--2059](https://ems.press/content/serial-article-files/29303).
It identifies the full motivic twist with the coefficient-twisted
automorphic L-series when the character conductor is prime to N;
complex conjugation of the character has no effect for our quadratic chi.
Here gcd(D,Delta_E)=1 implies good reduction at every prime dividing D,
so gcd(D,N)=1. To make its applicability at every finite prime explicit,
write l for such a prime, different from any auxiliary Tate-module prime.

- If l does not divide ND, both representations are unramified. The local
  polynomial is 1-a_l chi(l) l^(-s)+l^(1-2s), since chi(l)^2=1.
- If l divides N, it does not divide D. The character is unramified, and
  twisting commutes with taking inertia invariants. The multiplicative
  local polynomial becomes 1-a_l chi(l) l^(-s); at additive reduction the
  invariant space is zero and the factor remains 1. This includes l=2 or
  3 with wild additive reduction. An unramified extension does not remove
  that ramification.
- If l divides D, E has good reduction and chi is nontrivial on inertia,
  since its primitive quadratic conductor contains l. The twist of the
  unramified two-dimensional space has no inertia invariants, so its
  factor is 1. The coefficient twist also has factor 1, since chi(l)=0.

These exhaust the finite primes. In particular 2 lies outside odd D and
falls into the first or second case, and p is in the first case. The
quadratic twist's Tate module is the quadratic-character twist of that
of E; minimalization changes the model, not this representation. Thus
the cited comparison gives

\[
L(f,\chi_D,s)=L(E,\chi_D,s)=L(E^D,s),\tag{5}
\]

with **all** finite factors present. No incomplete Clay series is used in
q. The source's additive-place correction factors arise outside our
coprime hypotheses and are not silently discarded. As an orientation
and normalization cross-check, its equation (6), p. 2048, together with
lambda(r)=2 pi i integral_infinity^r f from equation (2), p. 2045, gives
L^a(E,chi,1)=tau(chi)/D sum_a chi(a)A(a/D). With tau(chi)=sqrt(D), this
agrees with (4). We use none of its Manin-constant integrality theorems.

**Minimal total period and calibration.** An odd positive fundamental
discriminant is square-free and D=1 modulo 4. Import Pal, *Periods of
quadratic twists of elliptic curves*,
[arXiv:1012.0094v2 (21 January 2011), Corollary 2.6 and Theorem 3.2](https://arxiv.org/pdf/1012.0094v2).
For minimal E and positive square-free d, its total-real-period formula
is Omega(E^d)=u_tilde Omega(E)/sqrt(d). Under d=1 modulo 4 and
gcd(d,Delta_E)=1, Corollary 2.6 gives u_tilde=1. Hence

\[
\Omega(E^D)=\frac{\Omega(E)}{\sqrt D},\qquad
\frac{I(G_D)}{\Omega(E)}
 =\frac{L(E^D,1)}{\Omega(E^D)}=q.\tag{6}
\]

Both real components, when present, are included on each side. No
least-positive-period substitution, arbitrary minimalization factor,
negative-twist period or Manin constant is assumed.

Equation (6) and q!=0 imply I is nonzero. The granted full-relative line
therefore gives I=beta phi on M_R for some nonzero real beta. Evaluating
at G_D yields beta d/Omega(E)=q. Thus d!=0 and
beta/Omega(E)=q/d, proving (1) on all of M, and also proving the
rationality of the normalized scale rather than assuming it.
Every path in G_D has an integral continued-fraction expression in the
complete presentation, so d can be computed exactly from the x_i.
Changing expressions preserves d because all relations vanish under phi.
For the plus-symbol convention, L028's orientation calculation gives
Re A(r)=-pi i (integral_r^(i infinity) f +
integral_(-r)^(i infinity) f)=lambda^+(r). Therefore
S(r)=lambda^+(r)/Omega(E)=F({infinity,r}) for every r, also when
L(E,1)=0. This use of L028 is independent of its prime calibration.

**Entire integral lattice and denominator bound.** Import Stein,
*Modular Forms, a Computational Approach*,
[General Modular Symbols, Definition 1.23, Proposition 1.24 and
Theorem 1.25](https://www.wstein.org/books/modform/modform/modular_symbols.html)
at the finite-index group Gamma_0(N) and weight two. These identify the
full relative module with the Manin presentation after torsion removal
and give integral continued-fraction generation of every cusp path.
Completeness is cited and certified in hypothesis 1; a rational basis
or selected paths would not suffice.

The denominator argument in L028 needs no prime twist; it depends only
on the calibrated generator values. Explicitly, if kv lies in R then
k phi(v)=0 in Q and hence phi(v)=0. Thus a rational row annihilating
R also annihilates R_sat. For any x in M choose an integral representative
(z_1,...,z_s); (1) gives F(x)=sum_i z_i y_i. Nonzero rational y_i have
integer p-adic valuations, and there are finitely many generators, so
(2) is a finite nonnegative integer. Each nonzero summand satisfies
v_p(z_i y_i)>=v_p(y_i)>=-C. The nonarchimedean inequality, with zero
assigned valuation infinity, proves

\[
v_p(F(x))\ge-C\quad(x\in M).\tag{7}
\]

Every {infinity,r} is integral in M, so (7) proves the required bound
at all rational arguments. There is no dependence on a cusp denominator,
continued-fraction length or number of terms in its expression. Every
rational-coordinate denominator is accounted for in the exact y_i;
sampling cannot replace this all-generator calculation.

**Qualifications and continuation test.** Scaling phi by a nonzero
rational scales d identically and preserves F, all y_i and C. Reversing
the specified calibration orientation alone would negate d and violate
(6). The independent proof of q prevents circular recovery of the
unknown scale. The full-relative line prevents an uncontrolled boundary
functional, but is not produced here. No new primitive-character identity,
period theorem, nonvanishing or integral-generation result is claimed:
the local work is only their applicability and finite certificate
bookkeeping. This is reproduction of a known mechanism under explicit
premises, beyond L028's prime-only scope but not beyond the source inputs.

The conditional test succeeds: (6) is nonzero, (1) is an exact rational
scale on the full module, and (2)--(7) give finite all-argument C. Producing
the premises and meeting L027's strict error threshold remain separate
tasks. Uniform twist supply, coefficient nonvanishing, rational Kummer
membership, divisible Sha and arbitrary complex-order comparison are
unresolved. This is not a BSD candidate. The separate critical audit
below passes for precisely these conditional hypotheses.

**Separate critical audit, 2026-10-08.** The statement and argument survive
review without a changed mathematical input. This verifies a known-source
specialization, not production of the granted data. The following checks
are part of the verification; the citations above retain their exact scope.

1. In Bertolini--Darmon Section 1.1, the local setup is a normalized form
   on Gamma_0(N); the multiplicative-reduction setting in the introduction
   is not a hypothesis of Proposition 1.3. With k=2 and j=1, both polynomial
   exponents are zero and the prefactor (j-1)!/(-2 pi i)^(j-1) is one.
   The selected involution acts on the constant polynomial trivially and
   sends the endpoints to their negatives. Hence its plus component is
   (A(r)+A(-r))/2=Re A(r). Cancelling the same nonzero Shimura period on
   both sides of (3) is valid without identifying it with a Neron period.
   The source's representatives 1,...,D may be replaced by 0,...,D-1:
   the differing endpoint terms both have character value zero. Primitivity
   is supplied by the fundamental discriminant, not by square-freeness
   of an arbitrary chosen character modulus. The imported positive Gauss
   sum gives (4); no incomplete nonunit-frequency proof is used.
2. The comparison is of full finite products. Outside ND the determinant
   term stays l^(1-2s), because the quadratic character squares to one.
   At a bad prime outside D, inertia and its invariant dimension are
   unchanged; the one-dimensional multiplicative factor changes by chi(l),
   and the zero-dimensional additive factor stays one. At a prime dividing
   D the original good representation is unramified; some inertia element
   acts on its twist by -1, which forces its invariant space to be zero
   over the characteristic-zero coefficient field. Thus both factors are
   one there, also when l=3. At 2 the character is unramified because D is
   odd; good, multiplicative and wild additive cases are already covered.
   The auxiliary Tate-module prime can be chosen separately away from
   each l. Wiersema--Wuthrich use the dual Tate module and inverse arithmetic
   Frobenius: replacing chi by its inverse leaves this quadratic character
   unchanged. Their equation (6) gives the same oriented identity, since
   sqrt(D)/D=1/sqrt(D). No integrality or Manin-constant premise is imported.
3. D is positive, square-free and 1 modulo 4. Pal v2 Corollary 2.6's
   proof gives each odd-prime minimalization factor one by coprimality
   with Delta_E, including at 3; Proposition 2.5 case 2(a) gives the factor
   one at 2. Theorem 3.2's positive case compares the entire real loci,
   not just their identity components. Its formula therefore gives (6)
   with no component-count correction, even when Delta_E is positive.
   Changing a minimal differential's sign does not affect these absolute
   total periods. Negative or even discriminants are not covered here.
4. Since Omega(E)>0 and q!=0, (6) forces I(G_D)!=0. The granted full
   real line then forces beta!=0 and d!=0 before any division by d.
   Equality on the entire module follows from the line hypothesis,
   not from equality at the calibration path alone. Rationality of q/d
   is now justified. An independent certificate for q is indispensable;
   calibration itself supplies no such certificate.
5. G_D is integral: character values are 0 or +/-1 and each oriented
   cusp path is an integral symbol. The rational row kills saturation,
   because Q has no additive torsion. Every element has an integral
   generator expression even if its coordinates in a chosen rational
   basis have denominators. Thus bounding every exact y_i bounds every
   sum of integral multiples. Zero y_i cause no exception; nonzero y_i
   give integer valuations and their finite maximum in (2) is sufficient.
   No projection of an integral path by (1+j)/2 is required. This checks
   every generator in the conditional statement; it does not pretend
   that a numerical list of generators or valuations was supplied.

The required and achieved audit threshold is the exact identity (1) and
finite bound (2) under all granted hypotheses. The distinct numerical
threshold min(n-1-C,M_prec-C)>v_p(b) is untested. No concrete composite q,
C, b, rank comparison or uniform nonvanishing has resulted. L028 remains
the sole direct local mathematical input (orientation and lattice);
the audit adds no DAG edge. Full Mathlib coverage remains unchecked.

## Mathlib

Full matching primitive fundamental-twist calibration on the relative
integral module, positive minimal-twist total-period formula and
all-argument certificate: not checked. Supporting character, modular-symbol,
Euler-factor, integral-presentation and valuation coverage: not checked.
Unknown coverage is not evidence of absence. Named source results are
imported by the citations above; their specialized conventions and
full-lattice denominator implication are justified here.
