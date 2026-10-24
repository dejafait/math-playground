# L031 — Independent total-period ratio for the twist by five

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x. Let E^5 be its global minimal
quadratic twist by positive 5. On either minimal curve set
Omega=integral over the full real locus of the absolute Neron differential.
Let f=sum a_n exp(2 pi i n z) be the normalized newform of E.

Use L030's independently audited arithmetic only: the displayed base
equation is globally minimal, Delta=N=389, and its invariants are
c_4=112 and c_6=-856. Neither its integration functional nor its unknown
scalar enters this proof. The named source inputs below are imported;
their applicability is justified explicitly. No BSD, Sha finiteness,
rational or analytic rank, twist nonvanishing, or additive-twist Manin
constant is a hypothesis.

The complete finite arithmetic evidence is
`scripts/twist-five/certificate.json`, SHA256
`7547b371d675441190256195270c9282213e888cdb666451ae21a062896e4415`.
Its independent complete replay is `scripts/twist-five/verification.json`.
Reproduction from the active notebook directory:

```bash
python3 scripts/twist-five/certify.py
python3 scripts/twist-five/verify.py
python3 scripts/twist-five/audit.py
```

The verifier does not import the construction program. Source theorems
are mathematical inputs, not theorems proved by the finite verifier.

## Conclusion

The independently determined Fricke eigenvalue of f is epsilon_N=-1;
the twist has root number +1. The reduced denominator of
q=L(E^5,1)/Omega(E^5) is at most B=2. The finite certificate proves

\[
\boxed{q=4\ne0.}
\]

At D=2^48=281474976710656, the complete outward ratio interval is

\[
\frac{[1125899587641796,\ 1125900221348759]}D,
\qquad
\text{width}=\frac{633706963}{281474976710656}<\frac14=\frac1{B^2}.
\tag{1}
\]

Existence and uniqueness of a rational of denominator at most B in (1)
are verified exactly below. This supplies L028's independent nonzero-q
input for this curve and ell=5, with its good ordinary p>=5, p!=5
restriction still retained in any later application. No calibration,
C, b, quadratic coefficient, Selmer-defect removal, rational membership,
complex-order comparison or BSD conclusion is obtained here.
This is a fixed-input reproduction of a known rational-recovery algorithm.

## Proof

**Imported optimality and denominator inputs.** Cremona's appendix to
Agashe--Ribet--Stein, *The Manin constant*,
[Theorem 5.2](https://wstein.org/papers/ars-manin/html/node13.html),
identifies curve number one as the optimal quotient at N<60000,
except 990h. The exact primary
[ecdata allcurves row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999),
inspected 2026-10-07, is `389 a 1 [0,1,1,-2,0] 2 1`.
The [Table One column conventions](https://johncremona.github.io/ecdata/)
identify the model and last-column torsion order one. The rank column
is not used. Since 389<60000 and this is not 990h, the exact model is
the new optimal elliptic quotient of J_0(389).

Import Cesnavicius, *The Manin constant in the semistable case*,
[arXiv:1703.02951, Theorem 2.13, printed p. 9](https://arxiv.org/pdf/1703.02951).
For a new elliptic optimal quotient at level n, with
Gamma_1(n) contained in H contained in Gamma_0(n), it gives zero
p-adic valuation of the Manin constant whenever p^2 does not divide n.
Take H=Gamma_0(389). Since the conductor is squarefree, this applies
at every prime. The positive rational Manin constant is therefore one.
Cremona's Theorem 5.2 also supplies this conclusion in the present range.
Neither theorem is applied to the additive twist.

Import Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, 23 March 2017, Proposition 1, pp. 3--4](https://arxiv.org/pdf/1608.06423v2).
In its convention lambda(r)=2 pi i integral_infinity^r f(z) dz and
[r]^+=Re(lambda(r))/Omega_+, where Omega_+ is the least positive real
Neron period. Under the strong-Weil Manin-constant-one hypothesis, a
unitary cusp has [r]^+ in c_infinity/(2 #E(Q)_tors) Z.
Here c_infinity=2 because Delta>0, and torsion has order one.
For each a=1,2,3,4, the cusp a/5 is unitary: gcd(5,N)=1, so in
the source's definition M=1 and Q=N are coprime. Consequently

\[
[a/5]^+\in\mathbf Z.                                      \tag{2}
\]

Let chi be the quadratic character modulo 5. Import Cremona,
*Algorithms for Modular Elliptic Curves*, corrected second edition
(1997), [Chapter 2, Section 2.11, pp. 38--39, character-cycle identity
preceding (2.11.4)](https://johncremona.github.io/book/fulltext/chapter2.pdf).
For this odd prime away from N, chi(-1)=1 and its positive Gauss sum
is sqrt(5). The oriented character cycle has period sqrt(5)L(E^5,1).
Since sum chi(a)=0, replacing {0,a/5} by {infinity,a/5} leaves its
period unchanged. Thus

\[
\sqrt5 L(E^5,1)=\Omega_+\sum_{a=1}^4\chi(a)[a/5]^+.
\tag{3}
\]

The total real period is Omega(E)=2 Omega_+: the real locus has two
components, and translation carries one component to the other while
preserving the invariant differential and its absolute integral.
Use Pal, *Periods of quadratic twists of elliptic curves*,
[arXiv:1012.0094v2, Corollary 2.6 and Theorem 3.2, pp. 6--8](https://arxiv.org/pdf/1012.0094v2).
The hypotheses d=5>0 squarefree, d=1 modulo 4 and gcd(d,Delta)=1
give minimalization factor one and
Omega(E^5)=Omega(E)/sqrt5=2 Omega_+/sqrt5. Substituting into (3) proves

\[
q=\frac12\sum_{a=1}^4\chi(a)[a/5]^+\in\frac12\mathbf Z.
\tag{4}
\]

This proves B=2 before rational isolation. It is a conservative bound;
no sharper pairing of the cusps is needed. Equations (3)--(4) use the
same oriented paths and total-period convention as L028, but do not
invoke its conditional normalization conclusion or grant its q.

**Exact Fricke case and independent coefficients.** Import Cremona,
[Chapter 3, Section 3.9, p. 102, traces of Frobenius](https://johncremona.github.io/book/fulltext/chapter3.pdf):
the coefficient at a prime is p+1 minus the point count on the reduced
minimal equation, including the bad-reduction case. For odd p, completing
the square shows that the number of y for a fixed x is
1+Legendre(1+4(x^3+x^2-2x),p). The certificate saves this character
at every x for every prime p<=256 and also p=389; p=2 is exhaustive
direct counting. The verifier independently exhausts all y for each x.
There is one point at infinity in every reduced projective equation.
At 389 it obtains 388 affine points and 389 total, so a_389=1.

Wuthrich, cited above, Section 4.1, p. 9, gives epsilon_N=-a_N
at the present single semistable bad prime. Thus epsilon_N=-1.
Since -389=1 modulo 5, chi(-N)=1=-epsilon_N. Cremona
[Chapter 2, Proposition 2.11.2, p. 38](https://johncremona.github.io/book/fulltext/chapter2.pdf)
now gives the non-forced-zero branch

\[
L(E^5,1)=2\sum_{n\ge1}\frac{\chi(n)a_n}{n}r^n,
\qquad r=\exp\left(-\frac{2\pi}{5\sqrt{389}}\right).
\tag{5}
\]

Its Fricke eigenvalue is chi(-N)epsilon_N=-1, hence root number +1.
This sign alone supplies no nonvanishing. The coefficients a_n for
n<=256 are recovered from the counted a_p by the elliptic L-series
Euler factors: a_1=1, multiplicativity for coprime indices, and
a_(p^k)=a_p a_(p^(k-1))-p a_(p^(k-2)) at good p. Every prime involved
in these coefficients is good. All factorizations, prime-power values
and coefficients are saved and independently replayed. Modularity
(already used in L030) identifies these L-series coefficients with f.

Use the all-n coefficient bound |a_n|<=n and geometric-tail estimate
in Wuthrich, Lemma 4 and its proof, pp. 6--7. For T=256 the omitted
part of (5) has absolute value at most

\[
2\sum_{n>T}r^n=\frac{2r^{T+1}}{1-r}.                       \tag{6}
\]

Finite verification of |a_n|<=n only checks the computed coefficients;
the imported theorem, not that finite check, controls the infinite tail.

**Certified elementary functions and finite errors.** Every stored
interval [l,u] denotes [l/D,u/D], with D=2^48. All operations use
integers or exact rational numbers. For addition and subtraction use
endpoint sums/differences. For multiplication use the min and max of
the four endpoint products. For division use the four quotients and
require a positive denominator interval. Rounding an exact rational
endpoint v downward or upward means floor(Dv) or ceil(Dv).
These rules enclose all signs and all finite arithmetic errors.
For square roots of a nonnegative interval, the integer bounds satisfy
l_root^2<=l D and u_root^2>=u D; the integer square-root operation and
one upward adjustment produce them exactly.

For pi, use Machin's identity
pi=16 atan(1/5)-4 atan(1/239). The double-angle formula twice gives
tan(4 atan(1/5))=120/119, and the tangent subtraction formula gives
tan(4 atan(1/5)-atan(1/239))=1. This angle is positive and less than
4/5<pi/2, so it is pi/4. For positivity, atan(1/5)>1/5-(1/5)^3/3
and atan(1/239)<1/239 suffice. Adjacent alternating partial sums of
atan x=sum (-1)^k x^(2k+1)/(2k+1) enclose it when 0<x<1;
this also follows by integrating the finite geometric-series remainder
of 1/(1+x^2). The certificate uses 24 terms and the next term at each
argument, saving their exact rational bounds and the resulting pi bounds.

The square-root rule encloses sqrt389, hence h=2 pi/(5 sqrt389).
The verified h interval lies strictly in (0,1). For each endpoint x,
adjacent partial sums S_32(x), S_33(x) of exp(-x) enclose exp(-x),
because its alternating terms x^k/k! decrease to zero. Monotonicity
of exp(-x) reverses the h endpoints. The exact rational Taylor bounds
are stored before outward dyadic rounding, yielding an interval for r.
This replaces, rather than assumes, a numerical library's working error.
Wuthrich's floating-point Lemma 6 need not be applied to this exact
rational interval implementation.

Successive outward products enclose r^n, and each signed rational term
2 chi(n)a_n/n is multiplied by that interval before summation. This
retains every finite rounding error and does not use cancellation in
(6). A further product encloses r^(257). If r<=r_upper<1, then
2r^257/(1-r)<=2 power_upper/(1-r_upper). The recorded tail upper
bound is 705731467/D. Adding and subtracting it from the finite sum
gives the complete interval

\[
L(E^5,1)\in[2507731718015227,\ 2507733129479385]/D.          \tag{7}
\]

**Total minimal period with finite AGM brackets.** The completed-square
equation is (y+1/2)^2=x^3+x^2-2x+1/4. Let e1<e2<e3 be its
three real roots. The polynomial H(x)=4x^3+4x^2-8x+1 changes signs
on each of [-3,-2], [0,1/4], [1/4,1]; endpoint values are respectively
(-47,1), (1,-11/16), (-11/16,1). These three disjoint interiors have
one root each, exhaust the cubic's roots, and certify their order.
Exact bisection preserves each sign-changing bracket; every midpoint
and its sign is saved and replayed until its width is at most 1/D.

Import Cremona [Chapter 3, Section 3.7, equation (3.7.1) and the
positive-discriminant case, pp. 97--98](https://johncremona.github.io/book/fulltext/chapter3.pdf):
with positive square roots the least positive real period is

\[
\Omega_+=\frac\pi{\operatorname{AGM}(\sqrt{e3-e1},\sqrt{e3-e2})}.
\tag{8}
\]

The differential is dx/(2y+1) on our minimal model, which is exactly
the differential used in this completed-square formula; no model scale
is inserted. Import the positive AGM and its common-limit integral
formula from [DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i).
For positive exact inputs A_0,G_0, iterate A_(j+1)=(A_j+G_j)/2 and
G_(j+1)=sqrt(A_j G_j). The arithmetic-geometric inequality puts both
new values between min(A_j,G_j) and max(A_j,G_j). Their common limit
therefore lies between min(A_j,G_j) and max(A_j,G_j) at every finite
stage. Starting with the root-derived intervals and applying the outward
rules inductively encloses the exact iterates. Thus, after 12 steps,
min of the two lower endpoints and max of the two upper endpoints
enclose the AGM limit, even if rounding prevents further contraction.
No approximate convergence cutoff is used.

The saved limit bracket is [355102103693472,355102103693487]/D.
Equations (8) and Omega(E^5)=2 Omega_+/sqrt5, with every division
and square root outward, give

\[
\Omega(E^5)\in[626933107243881,\ 626933107243911]/D.          \tag{9}
\]

This includes both real components and Pal's minimal-model comparison.

**Exact isolation, replay and scope.** Dividing (7) by the strictly
positive interval (9) with the four-quotient outward rule gives (1).
For b=1, the integer range
ceil(b q_lower)<=a<=floor(b q_upper) is exactly [4,4].
For b=2 it is exactly [8,8], whose sole member is not coprime to b.
Hence 4/1 is in the interval and is its only reduced rational of
denominator at most two. Also 4D=1125899906842624 lies strictly
between the two ratio endpoints. By (4), the actual q is one of these
rationals, so q=4. Width<1/B^2 is checked independently; width alone
was not used to assert existence. Only the first precision evaluation
was needed, out of the permitted schedule of at most three.

The independent verifier reads the entire certificate. It checks the
full prime list, every point count by an independent y-exhaustion,
every factorization and Euler coefficient, all exact Taylor brackets,
every finite power and partial sum, the complete tail, every bisection
sign, all AGM steps, both period factors and exhaustive denominator
ranges. Its seven grouped checks all pass with no failures. It does
not replace the named source inputs.

**Separate critical audit, 2026-10-07.** The written specialization and
the entire construction and verification programs were checked against
the previously inspected primary statements cited above. The exact
model/optimal-label match, squarefree base level, torsion order one,
all four unitary cusps, positive Gauss sum, minimalization factor one
and two real components meet their hypotheses. The bad-prime count
selects the correct Fricke branch; the infinite coefficient estimate
is an imported all-n theorem, not an extrapolation from finite counts.
No additional source hypothesis or mathematical defect was found.

The complete finite replay passes again on the stated certificate hash.
A complementary audit in `scripts/twist-five/audit.py` reads the complete
certificate without importing either original program. It checks the
base invariants and complete primality trials and binds the previously
audited L030 reports to the unchanged base-certificate hash. Only the
base arithmetic enters this proof; its relative operators are not used.

For an independent enclosure check let l,u be the stored rational
endpoints for r. For each 1<=n<=256 the audit computes l^n,u^n exactly,
without intermediate dyadic rounding. Since 0<l<=r<=u<1, these enclose
r^n. It multiplies by the signed rational weight 2 chi(n)a_n/n,
orders the two resulting endpoints, and accumulates exact endpoint
sums. It checks that every stored power and partial-sum interval
contains the resulting exact interval. Finally it uses the exact
upper tail 2u^257/(1-u), which is valid by (6) and monotonicity, and
checks containment in (7). The report `scripts/twist-five/audit.json`
saves all 256 pairs of power/sum containment witnesses as nonnegative
lower bounds for endpoint slack, in units of 1/D, together with the
tail and final-sum slack bounds. These supplement the complete original
certificate; they do not stand in for its coefficient or period proof.

The period audit retains the exact root signs and all 13 AGM states.
The intervals widen slightly after iteration four because of rounding;
this does not invalidate a finite enclosure. At every state the exact
arithmetic and geometric iterates enclose their common limit between
their minimum and maximum. Inductive outward containment therefore
justifies the final bracket without requiring numerical contraction.
The positive denominator in (9), both total-period factors, and the
exact reduced-rational enumeration pass. The audited conclusion remains
q=4 with width 633706963/281474976710656<1/4 and no failures. This is
verification of a fixed known-algorithm specialization, not a new
general theorem or a BSD candidate.

No Manin constant for E^5 or BSD formula is inferred. Numerical output
by itself is not the argument: (4), the full tail, outward elementary
errors, finite AGM bracketing and exact isolation make the finite
evidence load-bearing. This proves one independent input for a fixed
curve; all higher-rank uniformity and rational-membership gaps remain.

## Mathlib

Full matching independent elliptic twist-value certificate: not checked.
Coverage of optimality, unitary-cusp denominators, Gauss-sum twist
identities, minimal total periods, elliptic Euler factors, positive AGM
and exact interval arithmetic: not checked. Unknown coverage is not
evidence of absence. Named arithmetic inputs are imported by the precise
citations above; only their fixed-input specialization and finite
arithmetic/error/isolation bookkeeping are reproduced here.
