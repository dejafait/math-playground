# Lemma 826: logarithmic-theta confluent minor endpoint signs

## Hypotheses

Use exactly K of L019, m_0>0 of L021, H(v)=e^v K(e^v)/m_0,
and Q_3 with the increasing-tuple translation convention of L821.
Put u=e^v, D=u d/du, c=pi exp(2u), and

    c_(2j)=K^(2j)(0)/((2j)! K(0)),  1<=j<=4.

Ordinary superscripts on K denote u derivatives. Superscripts on H,
and D on any function of u, denote v derivatives. The endpoint claims
are eventual statements; no explicit finite onset is asserted.

## Conclusion

As v tends to minus infinity (u tends to zero from above),

    Q_3(v)=C_6 u^6+C_8 u^8+O(u^10),
    C_6=-256 c_2 c_4 in (90000,91000),
    C_8=768 c_2(c_2 c_4-3c_6).                         (1)

As v tends to plus infinity (u tends to infinity),

    Q_3(v)/(128 c^3 u^6) -> 1.                       (2)

At each endpoint there is a neighborhood on which Q_3>0, with the
error from its displayed leading term at most half that term. This
does not specify the neighborhoods or bridge their intervening gaps
to L821's compact domain. It proves neither global TN3 nor any
nonconfluent minor, lower oscillation, mixed/shifted Xi sign or RH.
The proof is a known-method specialization under the step633 approved
SPECIALIZE assessment, not a claim of a new general theta theorem.
The independent step636 audit below accepts exactly these endpoint
claims and qualifications, without a domain extension.

## Proof

**Inputs and regularity.** L821(1) gives, with ell=log H,

    Q_3=(D^3 ell)^2-(D^2 ell)(D^4 ell)-2(D^2 ell)^3.    (3)

Here D^j ell means derivatives in v, with ell understood as a function
of u and the term v=log u included. The normalization m_0 cancels;
only its positivity and finiteness are needed from L021. L019 gives
the actual, positive series

    K(u)=exp(u/2) sum_(n>=1) p(pi n^2 exp(2u))
                               exp(-pi n^2 exp(2u)),
    p(a)=8a^2-12a.                                   (4)

The standard parity/analyticity input is recorded in George Csordas,
*Fourier Transforms of Positive Definite Kernels and the Riemann
xi-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
(4.2) and Theorem 4.1(ii),(iii), printed p10: K(u)=4 Phi(u/2).
The factor and coordinate follow by substituting t=u/2 in that
displayed series. Its analyticity strip becomes |Im u|<pi/4.
No qualitative derivative-decay assertion there is used as a relative
error bound here. The originating CNV proof has not been audited.

For clarity, the existing L016 input also justifies precisely the
local facts used here without needing that originating proof. The
series (4) converges normally on each compact subset of |Im u|<pi/4:
Re(pi exp(2u)) has a positive minimum there, and every differentiated
summand is bounded by a fixed polynomial in n times exp(-alpha n^2).
It therefore defines a holomorphic function there. L016's modular
identity, applied with x=exp(2u), gives

    A(-u)=A(u)+sinh(u/2).

The already defined operator 2 d^2/du^2-1/2 annihilates this last term,
so K(-u)=K(u) near zero (indeed on the real axis). This is only the
coordinate specialization of the standard modular/parity input, not
a replacement theorem offered as a discovery. Positivity of K(0)
follows from (4); a quantitative enclosure below also verifies it.

**Origin derivatives and their complete certificate.** Define rational
polynomials in one variable by

    P_0(a)=8a^2-12a,
    P_(r+1)(a)=(1/2-2a)P_r(a)+2a P_r'(a).             (5)

Direct differentiation of an individual summand of (4) proves

    K^(r)(0)=sum_(n>=1) P_r(pi n^2) exp(-pi n^2),
    deg P_r=r+2.                                     (6)

Normal convergence just proved justifies all these derivatives.
We compute every r=0,...,8, not fitted Taylor data. If A_r is the
sum of the absolute rational coefficients of P_r, then, for a>=1,
|P_r(a)|<=A_r a^(r+2). Since 3<pi<4, the omitted n>=9 tail in (6)
is bounded in absolute value by

    2 A_r 4^(r+2) 9^(2r+4) exp(-243).                 (7)

Indeed consecutive terms of n^(2r+4) exp(-3n^2), for n>=9,
have ratio at most (10/9)^20 exp(-57)<1/2. This last strict inequality
is also enclosed by the exact arithmetic certificate. Thus (7)
bounds all nine derivative tails, including the four even derivatives
needed through order eight. No odd coefficient is presumed small:
all odd Taylor coefficients vanish exactly by parity.

Reproduce the calculation with

    python3 scripts/log-theta/endpoints_634.py

The full certificate is `scripts/log-theta/endpoints_634.json`. It
stores P_0,...,P_8, their exact coefficient norms, all 72 finite-term
intervals, their sums, nine tail bounds and full derivative intervals,
normalized even coefficients, formal logarithm/Q_3 polynomials and
every pass/failure field. It verifies the strict rational enclosures

    1<K(0)<2,       -10<c_2<-9,       37<c_4<39,
    90000<-256 c_2 c_4<91000.                         (8)

These are exact integer comparisons of interval endpoints with the
displayed rational bounds. The printed decimal previews are not used
to prove (8). All checks pass, with no omitted or unresolved case.

The program imports the already independently audited integer-lattice
arithmetic of `scripts/log-theta/confluent_compact_audit_614.py`, whose
full containment proof is canonical in L821. In brief, endpoints are
integer multiples of 2^(-1024); all basic operations round integer
quotients outward. Exponentials use range reduction to |z|<=1, 240
Taylor terms with remainder <=2/241!, reciprocal for a negative
argument, and repeated squaring. Pi is enclosed by the exact rational
alternating arctangent sums in Machin's identity (120 and 40 terms).
These proofs and constants apply to the present finite arguments;
no machine floating-point transcendental evaluation is used. The
program imports definitions only, so it neither invokes nor overwrites
the earlier compact replay/certificates. Usual trust in the stated
integer/rational program and execution remains; this is not formal
verification. Independent verification of this calculation is recorded
in the step636 audit below.

**Origin cancellation and differentiated error.** Put t=u^2. Even
analyticity and K(0)>0 give an analytic logarithm near zero, real on
the real axis, and

    log K=log K(0)+a_2 t+a_4 t^2+a_6 t^3+a_8 t^4+O(u^10),
    a_2=c_2,
    a_4=c_4-c_2^2/2,
    a_6=c_6-c_2 c_4+c_2^3/3,
    a_8=c_8-c_2 c_6-c_4^2/2+c_2^2 c_4-c_2^4/4.       (9)

All four D derivatives of the remainder are O(u^10). To justify this
without differentiating an unqualified scalar O-bound, choose R>0
so the logarithm is holomorphic on a neighborhood of the closed disk
|u|<=R, with maximum modulus M there. Cauchy's coefficient estimates
give an absolute bound M R^(-n) for each Taylor coefficient.
For |u|<=R/2, the D^j derivative of the tail n>=10 is at most

    M (|u|/R)^10 sum_(m>=0)(m+10)^j 2^(-m),  0<=j<=4.

Each sum is finite. This supplies all four differentiated estimates
with an actual common neighborhood. Positivity prevents a logarithm
denominator problem. The term v in log H contributes zero to j>=2.

Substitute D^j log K=sum_(k=1)^4 (2k)^j a_(2k)t^k+O(u^10)
in (3). The t^2 term cancels, as do the constant and t terms.
The t^3 coefficient is

    -256 a_2 a_4-128 a_2^3=-256 c_2 c_4.

The t^4 coefficient is

    -2304 a_2 a_6-1536 a_2^2 a_4
       =768 c_2(c_2 c_4-3c_6).

The exact multivariate rational series calculation in the certificate
checks every coefficient through t^4, including zeros, without
substituting numerical approximations for the c_j. Products of the
four differentiated remainders are controlled because every displayed
log jet is O(u^2). All remaining terms in Q_3 are O(u^10).
This proves (1). By (8), dividing its remainder C_8u^8+O(u^10) by
C_6u^6 tends to zero; it is eventually at most 1/2 in absolute value.

**Exact full-first-summand comparison at infinity.** Take u>=1 and
c=pi exp(2u)>3. Put q=3/(2c), so 0<q<1/2. The exact logarithm of
H formed with the whole n=1 summand is

    ell_0=v+9u/2-c+log(8pi^2)-log m_0+g(u),
    g(u)=log(1-q).                                   (10)

Thus the polynomial prefactor has not been discarded. Define

    A=2u+4u^2,
    B=2u+12u^2+8u^3,
    C=2u+28u^2+48u^3+16u^4,       d=9u/2,
    S_2=u g'+u^2 g'',
    S_3=u g'+3u^2 g''+u^3 g''',
    S_4=u g'+7u^2 g''+6u^3 g'''+u^4 g'''',

where these g primes are ordinary u derivatives. Their exact values are

    g'=2q/(1-q),                  g''=-4q/(1-q)^2,
    g'''=8q(1+q)/(1-q)^3,
    g''''=-16q(1+4q+q^2)/(1-q)^4.                    (11)

The exact base observable, before any asymptotic truncation, is

    L_2=d-cA+S_2,   L_3=d-cB+S_3,   L_4=d-cC+S_4,
    Q_0=L_3^2-L_2 L_4-2L_2^3.                       (12)

For example its part with all S_j zero is exactly

    dc(A+C-2B)+c^2(B^2-AC)-2d^3+6d^2cA-6dc^2A^2+2c^3A^3.

Equation (12), with (11), specifies the full rational expression;
no sign or zero-location property of a reference Fourier transform
is assumed. Bounds from (11) give

    |g'|<=4q, |g''|<=16q, |g'''|<=96q, |g''''|<=832q,
    |S_j|<=2048(1+u)^j q,     j=2,3,4.

In particular |d+S_j|<=2053(1+u)^j and
|L_j|<=2200 c(1+u)^j. Put

    C_0=2*2200^2+2*2053*(2200^2+2200*6+36).

The two quadratic terms of (12) and the difference of its cubic
from 2c^3A^3 then give the explicit bound

    |Q_0-2c^3A^3|<=C_0 c^2(1+u)^6.                  (13)

For the cubic, use x^3-y^3=(x-y)(x^2+xy+y^2), with x=L_2,
y=-cA, |x-y|<=2053(1+u)^2 and |y|<=6c(1+u)^2.
Since A=4u^2(1+1/(2u)), (13) already identifies the leading
128c^3u^6 for the complete first summand. It remains essential to
control differentiated actual-theta errors, which we now do.

**All four differentiated actual-tail bounds.** Use the same exact
R_j recurrence as L821(3), with R_0=p(a), but replace its compact
constants. Its u-degree is at most j and its total (a,c)-degree at
most j+2. The sum of absolute coefficients has the majorant

    A_0^*=20,   A_(j+1)^*=(3j+8) A_j^*,
    (A_0^*,...,A_4^*)=(20,160,1760,24640,418880).     (14)

Indeed the four recurrence contributions are at most j, 2(j+2),
and 2+2 times the preceding coefficient norm. For a>=c>=1,

    |R_j(u,a,c)|<=A_j^*(1+u)^j a^(j+2).

Write B_tail=sum_(n>=2) p(n^2c) exp(-(n^2-1)c), and
rho=B_tail/p(c)>=0. Every derivative series through order four
converges locally uniformly, by the same polynomial-times-Gaussian
bound as in L821, now at each u>=1. For 0<=j<=4,

    |D^j B_tail|
      <=A_j^*(1+u)^j c^(j+2)
                     sum_(n>=2) n^(2j+4) exp(-(n^2-1)c)
      <=A_j^* 2^(2j+5)(1+u)^j c^(j+2) exp(-3c).     (15)

The consecutive-term ratio in this sum is at most
(3/2)^12 exp(-5c)<(3/2)^12 exp(-15)<1/2.
For an elementary strict check, exp(15)>15^3/3!>2(3/2)^12.
Thus its sum is at most twice its n=2 term, proving (15).
These are bounds for every required derivative, with explicit u,c
dependence, not a differentiated scalar asymptotic.

Set X=(1+u)c and E_0=160. Recursively, for 1<=j<=4, set

    E_j=A_j^* 2^(2j+3)
          +sum_(k=1)^j binom(j,k)(A_k^*/4) E_(j-k).  (16)

Then for every 0<=j<=4,

    |D^j rho|<=E_j X^j exp(-3c).                     (17)

To check (17), p(c)=8c^2-12c>=4c^2>0. Moreover
D^k p(c)=R_k(u,c,c), so |D^k p|/p<=(A_k^*/4)X^k.
Apply D^j to p rho=B_tail, solve for D^j rho and use (15)
and induction. This proves (16)–(17), including j=0, without
assuming differentiated relative errors beforehand.

The exact actual logarithm is ell=ell_0+log(1+rho).
Because rho>=0, all denominators 1+rho are at least one. The
explicit second, third and fourth logarithmic derivative formulas
give, with delta_j=D^j log(1+rho),

    |delta_j|<=F_j X^j exp(-3c),  j=2,3,4,
    F_2=E_2+E_1^2,
    F_3=E_3+3E_1E_2+2E_1^3,
    F_4=E_4+4E_1E_3+3E_2^2+12E_1^2E_2+6E_1^4.      (18)

For example delta_2=rho_2/(1+rho)-rho_1^2/(1+rho)^2;
the higher formulas are precisely the log-jet formulas of L821
with B replaced by 1+rho. A product of k derivative errors has
exp(-3kc)<=exp(-3c), which proves all terms in (18).
No smallness assumption on rho or unproved denominator limit is used.

Finally |L_j|<=2200X^j for j=2,3,4. Expanding (3) at the exact
base jets (12), (18) therefore gives

    |Q_3-Q_0|<=C_* X^6 exp(-3c),                    (19)
    C_*=4400F_3+F_3^2+2200(F_2+F_4)+F_2F_4
         +6*2200^2 F_2+6*2200 F_2^2+2F_2^3.

The first two terms bound the square, the next three bound the
bilinear product, and the last three bound twice the cubic
difference. All powers of X have degree six; this accounts for
every nonlinear error and possible cancellation.

Combining (13) and (19), using (1+u)^6/u^6<=64, proves

    |Q_3/(128c^3u^6)-1|
      <=(1+1/(2u))^3-1+C_0/(2c)+(C_*/2)c^3 exp(-3c).

Each term tends to zero as u tends to infinity. Hence this entire
bound is eventually at most 1/2, proving (2) and its strict positive
sign with the required relative error. No assertion about the
intervening finite domain follows.

The bounded test has succeeded at both endpoints, so a negative
endpoint cannot exclude this proposed TN3 mechanism. This provides
only a local necessary-condition check beyond the inspected source
statements; the independent global/minor and sign-transfer gaps
remain unresolved. No Fourier zero location is inferred.

**Independent proof and complete-certificate audit (step636).**
The hypotheses, domain and conclusions are retained. This audit uses
L016/L019/L021 only for the actual kernel, modular parity, regularity
and positive finite normalization, and L821 for the normalized signed
confluent formula and arithmetic contract. No zero-location, common
interlacing, inverse-variation or sign-transfer premise is imported.
The previously approved source comparison remains adequate. Simon's
Section 3(7) supplies necessity only; Csordas's Theorem 4.1 is not a
relative-error theorem. L016's modular argument is the independent
local route to the regularity used here, so the unread originating
CNV proof is not an essential premise.

The increasing-column signs are 1,-1,1. Removing the linear logarithmic
term by triangular derivative transformations leaves determinant
ell''ell''''+2ell''^3-ell'''^2 before those signs. This verifies (3),
including its minus sign and division by H^3. The factor m_0 cancels;
the log u term contributes no derivative of order at least two.
The normal-convergence bound in the stated strip applies on every
compact subset and to each fixed derivative. The modular identity
gives exactly A(-u)-A(u)=sinh(u/2), annihilated by 2d^2/du^2-1/2.
Thus parity is exact. Since K(0)>0, continuity gives a complex disk
with no zeros; on a smaller closed disk there is a holomorphic logarithm.
This, rather than real positivity alone, justifies the complex logarithm
used in (9). Cauchy's estimates in that disk give the displayed common
D^j remainder bound for all 0<=j<=4. Each jet starts at u^2, so the
truncated products have no unaccounted term below u^10.

The independent executable is

    python3 scripts/log-theta/endpoints_audit_636.py

It preserves the original script/certificate, replays every original
field into `scripts/log-theta/endpoints_replay_636.json`, and writes the
full independent evidence to `scripts/log-theta/endpoints_audit_636.json`.
All original fields agree exactly. Program and source-certificate hashes
are recorded. No earlier compact certificate is regenerated or changed.

For an independent construction of (6), the coefficient of t^r in

    exp(t/2)[8a^2 exp(4t)-12a exp(2t)]
                          exp(-a(exp(2t)-1))

multiplied by r! is P_r(a). This follows by shifting an individual
summand by ordinary coordinate t and factoring out exp(-a) at zero.
Exact rational series multiplication through degree eight independently
reproduces every coefficient of all nine P_r and every coefficient norm.
It does not call recurrence (5). The independent arithmetic reuses the
proved integer-lattice operations, with scale 2^1536, Taylor degree 320
and Machin sums of 160 and 60 terms. The containment proof in L821 applies
verbatim: the Taylor tail is now at most 2/321!, directed integer
division is unchanged, and both arctangent remainders are bounded by
their first omitted terms. Every exponential's reduced argument is
checked in [0,1]. No floating-point value enters a proof comparison.

Direct monomial evaluation, independently of the original Horner code,
encloses all 72 finite terms, all nine sums and all nine full derivatives.
Each of these and the pi, tail-ratio, four normalized coefficients and
two final coefficients lies wholly inside its original saved interval:
98 complete containment comparisons pass. All nine independently
recomputed tail upper bounds are at most their saved upper bounds.
The geometric ratio is strictly less than 1/2, K(0)'s denominator is
positive, and every strict bound in (8) passes using integer endpoints.
In particular the full leading interval is contained in (90000,91000);
its decimal value near 90795.6224 is only a preview.

The formal Q_3 calculation is also independent of the logarithmic-jet
route. Write f(t)=1+c_2t+c_4t^2+c_6t^3+c_8t^4 modulo t^5. The coefficients
of H^(k)/(K(0)u/m_0) are (2j+1)^k times those of f, for t=u^2.
The program forms the ordinary three-by-three derivative determinant
by all six permutations, negates it for the column signs, and divides
by f^3 using exact formal inversion. Its complete coefficients through
t^4 agree with the saved Q_3 series: 0,0,0,-256c_2c_4, and
768c_2^2c_4-2304c_2c_6. Independently integrating the formal series f'/f
reproduces every logarithm coefficient in (9). Thus the cancellations,
normalization and signed lower bound do not rely only on replay of the
original polynomial implementation.

At infinity the full n=1 term is exactly (10); its polynomial factor
contributes 4u+log(8pi^2)+log(1-q), not just a constant. Differentiating
q gives q'=-2q and verifies all four formulas (11). For 0<q<1/2 the
successive absolute bounds are 4q,16q,96q,832q. The largest coefficient
sum needed in S_4 is 4+7*16+6*96+832=1524<2048; those for S_2,S_3
are smaller. Since the coefficient sums of A,B,C are 6,22,94,
|d+S_j|<=2053(1+u)^j and |L_j|<=2200c(1+u)^j follow for every u>=1.
The two quadratic terms and the factorized cubic difference therefore
give (13) with exactly the stated C_0=19937067016.

For the differentiated tail, u-degree and total (a,c)-degree increase
by at most one at each recurrence step. The two a/c derivative terms
together contribute at most 2(j+2) to the coefficient-norm factor;
u partial_u contributes j, and the two multiplication terms contribute
4. Their sum is 3j+8. Independently generated exact R_j norms are
20,136,1240,13720,176312, below all five majorants (14). The locally
uniform Gaussian estimates justify every derivative through order four,
and the decreasing consecutive-term bound starts at n=2. The strict
rational comparison 15^3/6>2(3/2)^12 verifies the geometric-series step.
Thus (15) holds separately for j=0,1,2,3,4 on the stated half-line.

On a=c the exponential factor is one and the drift term vanishes;
the remaining derivatives follow the diagonal a=c. Consequently
D^k p(c)=R_k(u,c,c), as needed for the quotient induction. Because
p(c)>=4c^2 and c>=1, division of (15) by p(c) yields precisely its
A_j^*2^(2j+3) coefficient. Leibniz's rule then gives (16) with no
uncontrolled derivative of a quotient. The five E_j values are

    160, 11520, 1217280, 174881280, 32353098240.

All are finite positive constants. Positivity of every tail summand
gives rho>=0, so the second, third and fourth logarithm formulas have
denominators at least one. Their respective absolute coefficient lists
are (1,1), (1,3,2), and (1,4,3,12,6); hence (18) accounts for every
product, using exp(-3kc)<=exp(-3c) for k>=1. There is no differentiated
scalar big-O assumption or hidden small-denominator estimate.

Finally c>=1 gives |L_j|<=2200X^j. Expansion of the square, bilinear
term and cubic has respectively two, three and three error terms,
with total X-degree six in every case. Their coefficients give exactly
(19); the independently computed C_* is 28827973257419919612057600.
Dividing (13) and (19) by 128c^3u^6, with (1+u)^6/u^6<=64, yields
the three displayed relative-error terms. Each tends to zero:
u tends to infinity, c=pi exp(2u) tends to infinity, and
c^3 exp(-3c) tends to zero. This verifies eventual error at most 1/2
without claiming an explicit onset. At the other endpoint the proved
positive C_6 and analytic O(u^10) remainder give the same domination
after division by C_6u^6. Both endpoint conclusions therefore pass.

No defect or additional mathematical hypothesis was found. The audit
validates a previously unaudited local input; it proves no new global
theorem and claims no novelty beyond the inspected sources. The full
evidence has no unresolved arithmetic case. Usual trust in Python's
integer/rational execution remains, and the analytic proof is informal.
Global confluence, nonconfluent minors, lower oscillation and the
all-degree mixed/shifted Xi transfer are still unpaid.

## Mathlib

Full matching coverage of this Q_3 endpoint statement is unchecked.
No absence or novelty claim is made. L016 records supporting Poisson
summation and smooth-series theorem links; those are not the full
nonlinear endpoint result. L821 records the necessary confluence
specialization of Simon arXiv:1305.1173v1, Section 3(7), printed
pp6–7; it is not a sufficient global TN3 theorem. The Csordas
numbered citation above supplies standard regularity only. Neither
the exact rational certificate nor the analytic error estimates are
claimed formalized in Mathlib.
