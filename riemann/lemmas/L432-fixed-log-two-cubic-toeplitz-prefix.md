# Lemma 432: the first five fixed log-2 cubic moments pass the Toeplitz test

## Hypotheses

Use L406--L409's actual ordinary critical jets, complete response,
physical Delta and Bcal, and leading polynomials d and B0. In particular
c=1/(4pi), kappa=17c^3/20160, ell=log H and
E_H=H^(-1) integral_[H,2H]. Let beta>0 be L409's exact coefficient.
H tends to infinity through all sufficiently large real values. Each
harmonic j in {0,1,2,3,4} and each response head N is fixed before the
height limit. No RH, clipping, conditional critical law, cross-H
realization, growing-harmonic uniformity or regulator margin is assumed.

For a positive rational r, num(r) denotes its reduced numerator, and
A_u=u^(-2) sum_(a=1)^u gcd(a,u). Use L408's audited arbitrary-rational
coefficient interface, L430's audited explicit frequency bounds and
L431's audited prime-2 factorization. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-prime-power-cubic-positive-measure-test.md`.

## Conclusion

For j=0,1,2,3,4 the complete actual sharp means satisfy

    E_H[Delta Bcal cos(j t log 2)]=g_j ell^2+o_j(ell^2),        (1)
    g_j=(kappa/2) sum_(m,n,k>=1) (mn)^(-2) k^(-3)
       [2^(j/2) A_num(2^j mn/k)
                         +2^(-j/2) A_num(mn/(2^j k))].        (2)

These series are absolutely convergent, g_0=beta, and their normalized
values c_j=g_j/beta are exactly

    c_0=1,
    c_1=1161 sqrt(2)/1786,
    c_2=3504/4465,
    c_3=52201 sqrt(2)/114304,
    c_4=594309/1143040.                                      (3)

With c_(-j)=c_j, every nonempty principal minor of
T_4=(c_(a-b))_(0<=a,b<=4) is strictly positive. There is therefore a
positive symmetric probability measure on the circle with these first
four cosine moments. This is finite-prefix compatibility only. No sign
of a higher Toeplitz section, positive measure for the entire actual
sequence, bounded density, law implementation or actual clipping is
asserted. The approved search ends at harmonic 4.

This is a local REPRODUCTION specialization of the assessed analytic
interfaces and classical moment theorems. The arithmetic prefix is a
new local input; no originality beyond the sources checked is claimed.
The separate step-225 critical audit below validates this bounded claim.
The global mixed positivity,
actual/global realization, capped nondegeneracy and full-error regulator
margin gaps remain open; there is no RH consequence.

## Proof

The prior assessment checked the exact fixed-character source scope,
moment theorems, local duplicates and recorded failures. Reuse it.
L427/L428/L430's narrower stops and L431's one-harmonic construction are
preserved. The following is one bounded test, not an extension to higher
harmonics or a new counterlaw construction.

### Fixed-head coefficient and primary source applicability

For each j multiply L430's exact carrier identity by

    cos(j t log 2)=(2^(jit)+2^(-jit))/2.

For j=0 the two equal characters, each of weight 1/2, give weight one.
For a response triple put alpha=(mnk)^(-5/2). The single-carrier twists
are r=a0 mn/k, a0=2^j or 2^(-j), with prefactor alpha/2. The zero-carrier
twists are r=a0 mnk. All are positive fixed rationals at fixed N.

Import L408 (12), equivalently L430 (6), for r=u/v in lowest terms:

    S_(r,nu,w_(1,nu))
      =H ell^2 sqrt(r) A_u a_nu m_nu+o_(r,nu)(H ell^2),
    m_nu=(-1)^D product_(i=1)^3 p_i!/(D+2)!, D=sum p_i<=6.    (4)

The primary arithmetic input is A. Fazzari, *A Voronoi summation
formula for the shifted triple divisor function*,
[arXiv:2306.15553v1, (3.5)](https://arxiv.org/html/2306.15553v1#S3),
with additive numerator -v and modulus u. Coprimality holds after
reduction; the complete classes 1,...,u include nonunits and the zero
class. The residue-one pole in [DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i)
gives u^(-3) sum_(a,b,c=1)^u exp(-2pi i vabc/u)=A_u. Thus the
coalesced leading coefficient depends on the numerator u, not the
denominator v. [DLMF 25.11.5](https://dlmf.nist.gov/25.11.E5),
Apostol (1976), (25), p. 269, supplies continuation for the positive
progression parameters and the Re s>0 derivative disks away from 1.
L408's smooth-first Mellin argument and absolute endpoint majorants,
rather than an indicator inserted in a Schwartz-weight formula, supply
the sharp transfer in (4). These imported arguments apply to every
fixed r here; no growing-modulus claim is used.

The exact ordinary-jet weights, including all phase derivative terms,
are unchanged: the characters are inside r, not differentiated weights.
They obey |w|<=C ell^(-D), |w'|<=C ell^(-D)/H on the contour rectangle.
L408's complete signed polar sum is sum_nu a_nu m_nu=17/20160;
monomials with zero leading weights retain their lower-order errors.
Every fixed zero-carrier integer resonance is O_(r,nu)(H); other
fixed zero-carrier frequencies have no resonance. The sharp connectors
are o_N(H ell^2). Hence the finite-head leading coefficient is (2)
restricted to m,n,k<=N, using alpha sqrt(r)=sqrt(a0)(mn)^(-2)k^(-3).
All leading coefficients are real, so the exact final real projection
does not change them. This already reproduces L409 at j=0 and L430
at j=1; it remains to justify the full response at the changed twists.

### Complete tails, sharp connectors and denominator-2^j resonances

Use a=21/20, delta=11/20 and eta=1/100, exactly as in L409/L430.
On the shifted rectangle tau=t-iq, 0<=q<=delta, |r^(s-1/2)|=r^q.
The response sums converge normally on a neighborhood, since their
power exponents remain summable for -3/2<q<3/2. Each fixed character
preserves this normal convergence. Both sharp connectors are bounded
by C(1+r^delta)H^(71/120) for the single carrier and
C(1+r^delta)H^(1/2) for the zero carrier, before multiplication by
alpha. These are summable for each fixed a0. Constants can depend
on j, but not on N or H.

The imported frequency kernel is M. B. Milinovich and N. Ng,
*Lower bounds for moments of zeta'(rho)*,
[Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
for x>0 and fixed 0<kappa0<=a<=2. Its primitive main term is
1_(x<=V/(2pi)) exp(-2pi i x), and its error is

    O(x^(-a)[V^(a-1/2)
                  +V^(a+1/2)/(|V-2pi x|+sqrt(V))]).

Its saddle, endpoint and exterior cases are supplied by S. M. Gonek,
*Mean values of the Riemann zeta-function and its derivatives*, Invent.
Math. 75 (1984),
[section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
The prior assessment inspected these hypotheses/cases. Apply the same
kernel at x=l/r, subtract the primitives at both sharp endpoints, and
integrate by parts against the exact analytic weight. L430 (11)--(12)
give for every positive real r the weighted kernel error

    C[H^(11/20)r^(11/20)
       +H^(1/100)r^(-49/100)(1+log_+r)^D
       +H^(51/100)ell r^(51/100)(1+log_+r)^D]                 (5)

and absolute arithmetic main bound

    C H sqrt(r) ell^2(1+log_+r)^(D+2).                       (6)

These frequency bounds, including the nearest endpoint saddle and
both connectors, precede any response summation. The underlying
fixed-strip subconvex/Cauchy bound is already part of audited L407/L409;
its primary input is Bourgain, JAMS 30 (2017),
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
No arbitrary r-dependent fixed-head error is being summed.

For r=a0 mn/k,

    alpha r^q=a0^q m^(-5/2+q)n^(-5/2+q)k^(-5/2-q).

All exponents q in (5) lie inside (-3/2,3/2). Also
1+log_+(a0 mn/k)<=C_j(1+log m+log n). Thus the errors (5)
sum to o_j(H ell^2), uniformly over every subset of response tuples.
After alpha multiplication (6) has a fixed-j summable majorant

    C_j H ell^2 (mn)^(-2)k^(-3)(1+log m+log n)^8.             (7)

Its tail over max(m,n,k)>N tends to zero.

For the zero carrier r=2^j mnk or mnk/2^j, put h=2^(-j).
Both lie on the fixed grid h Z with r>=h. The first twist is an
integer and always has l=r as its resonance. The second has that
resonance exactly when 2^j divides mnk. At a resonance the exact
term, not dropped, is

    r^(-1/2) C_nu(r) integral_[H,2H] w_(0,nu)(t-i delta)dt.

The audited coefficient bound |C_nu(l)|<=C l^eta log(2l)^D
makes its absolute value at most C H r^(-49/100)log(2+r)^D.
This is summable against alpha for each fixed a0, so all resonances
together contribute O_j(H), including r=l=1.

Away from resonance the unweighted primitive is bounded by

    2r^delta sum_(l!=r) |C_nu(l)|l^(-a)/|log(r/l)|.           (8)

Outside r/2<l<2r use |log(r/l)|>=log 2 and the absolutely
convergent coefficient series, giving C r^delta. Inside this interval
use |log(r/l)|>=|l-r|/(2r). Nonzero distances are at least h;
grouping positive/negative distances into unit intervals gives inverse
distance sum <=C_j log(2+r). This bound also covers the finitely sized
range h<=r<1 and empty interiors. Applying the same coefficient bound
gives an interior bound C_j r^(51/100)log(2+r)^(D+1).
Partial summation costs at most C ell^(-D)<=C and retains both
endpoints. Since alpha r^q=a0^q(mnk)^(-5/2+q) for this carrier,
the nonresonant bounds for q=11/20,51/100 sum to O_j(1).
Together with the connectors and resonances the entire zero carrier
is O_j(H). No denominator-2^j near-resonance is omitted.

Consequently (7) supplies

    limsup_(H->infinity)
      |E_H[(d B0-d_N B0_N)cos(j t log 2)]|/ell^2
        <=C_j epsilon_N, epsilon_N -> 0.                    (9)

Since 0<A_u<=1, the coefficient series (2) converges absolutely and
its heads tend to g_j. Given a tolerance, first choose N controlling
(9) and the coefficient tail, then take H large at that fixed N.
This proves (1) for d B0 on the whole real-H ray. Finally L406's
absolute physical replacement has error O(ell^(5/4)); multiplication
by cosine preserves it. Thus (1) holds for the complete physical
product, including curvature and all response derivatives. An already
integrated signed tail was never multiplied by a bounded function.

### Exact local factor, without numerical odd-prime truncation

Use L431's multiplicativity of A and its formula
A_(2^e)=2^(-e)(1+e/2) for every integer e>=0. Write
m=2^a m_o, n=2^b n_o, k=2^v k_o with odd subscripts and s=a+b.
For each s there are s+1 ordered pairs (a,b). Define

    T_odd=sum_(m_o,n_o,k_o odd) (m_o n_o)^(-2)k_o^(-3)
                                       A_num(m_o n_o/k_o),
    B_j=sum_(s,v>=0)(s+1)4^(-s)8^(-v)
                              A_(2^max(s+j-v,0)).             (10)

All terms are nonnegative and bounded by convergent power sums, and
T_odd>=1. Tonelli and unique 2-adic decomposition give

    g_j=(kappa T_odd/2)[2^(j/2)B_j+2^(-j/2)B_(-j)],
    beta=kappa T_odd B_0.                                   (11)

Thus no odd Euler product needs numerical evaluation or formal
division: the finite positive common factor cancels exactly.

Here is a closed convergent-tail evaluation covering all j used.
Put x=1/4, y=z=1/8, D0=31/32, and L=max(0,-j), M=max(1,j).
By L431's difference-variable calculation, the weight of d=s-v>=0
is x^d(1+D0 d)/D0^2, and that of d=-h<0 is y^h/D0^2. Set

    S0(L)=z^L/(1-z),
    S1(L)=z^L[L/(1-z)+z/(1-z)^2],
    S2(L)=z^L[L^2/(1-z)+2Lz/(1-z)^2+z(1+z)/(1-z)^3].

They are exactly sum_(d>=L) z^d, d z^d and d^2 z^d;
differentiating the geometric series is valid for |z|<1. Splitting
the two signs at the points where max(d+j,0) changes gives

    D0^2 B_j = sum_(d=0)^(L-1) x^d(1+D0 d)
      +2^(-j)[(1+j/2)S0(L)
                +(D0(1+j/2)+1/2)S1(L)+(D0/2)S2(L)]
      +sum_(h=1)^(M-1) y^h 2^(-(j-h))(1+(j-h)/2)
      +y^M/(1-y).                                         (12)

Empty sums are zero. Equality d+j=0 may be included in the second
term because its A-factor is exactly 1; equality j-h=0 belongs to
the last tail with the same value. Thus (12) also covers j=0 and
both transition cases without a missing boundary term.

Exact rational substitution gives:

| j | B_j |
|---|---|
| -4 | 668748/329623 |
| -3 | 666440/329623 |
| -2 | 658944/329623 |
| -1 | 635904/329623 |
| 0 | 571520/329623 |
| 1 | 425088/329623 |
| 2 | 283776/329623 |
| 3 | 177700/329623 |
| 4 | 213561/659246 |

The entries at -1,0,1 reproduce audited L431. Substituting this table
in (11) gives all five values (3), including its audited first ratio.
This evaluates only the requested finite prefix.

### Every principal minor and the imported finite moment theorem

Form T_4 from (3), using differences of indices, not sums. The complete
exact calculation in
`scripts/discriminant/prime_power_cubic_toeplitz.py` evaluates (12)
and enumerates all 2^5-1=31 nonempty principal subsets. Each determinant
is computed by the Leibniz formula in Q(sqrt(2)), with rational pairs
and sqrt(2)^2=2. Independently, congruence by
D=diag(1,sqrt(2),1,sqrt(2),1) makes D T_4 D rational. For each
subset S, exact rational Gaussian elimination agrees with the first
determinant after division by 2^(number of odd indices in S).
This positive congruence scaling preserves every sign. These are finite
exact arithmetic checks, without floating point or infinite truncation.

The complete certificate, including every index set and determinant, is
`scripts/discriminant/prime_power_cubic_toeplitz_certificate.json`.
Its 31 complete entries and exact minima were inspected. For each size
the smallest principal minor is:

| Size | Number checked | Minimum determinant |
|---|---|---|
| 1 | 5 | 1 |
| 2 | 10 | 246977/1594898 |
| 3 | 10 | 362020232/17803048925 |
| 4 | 5 | 17385983222402879/6511871053834240000 |
| 5 | 1 | 41743885318401109179553/119093265429995035033600000 |

Every numerator and denominator is positive. In particular all leading
principal minors are positive, so the real symmetric matrix T_4 is
positive definite by Sylvester's criterion. All principal minors were
tested, as the approved semidefinite obstruction test requires.

Import Zai Yang and Lihua Xie, *Frequency-Selective Vandermonde
Decomposition of Toeplitz Matrices with Applications*,
[arXiv:1605.02431v3, section 2, Theorem 1, (5)--(15)](https://arxiv.org/html/1605.02431v3#S2).
Its finite Hermitian Toeplitz PSD criterion yields a positive atomic
circle measure realizing precisely this finite prefix. Its mass is
c_0=1. Their negative Fourier sign is harmless here because c_j are
real and even. More explicitly, symmetrizing any representing measure
under theta -> -theta preserves its mass and cosine moments and makes
its complex moments exactly c_j for |j|<=4. Conversely a measure with
the specified cosine moments can be symmetrized first, and its Toeplitz
quadratic forms are integrals of squared trigonometric polynomials.
Thus the symmetric-measure specialization is justified without assuming
that the actual sine-weighted cubic coefficients vanish.

For the infinite question import the classical Herglotz/trigonometric
moment theorem as stated and proved in J. W. Helton and M. Putinar,
*Positive Polynomials in Scalar and Matrix Variables, the Spectral
Theorem, and Optimization* (2007),
[section 3.1, Theorem 3.3, pp. 245--246](https://mathweb.ucsd.edu/~toal/READ07/hpSurvey07.pdf#page=17).
For c_0>0 and conjugate symmetry it requires every finite Toeplitz
section to be PSD. The single section checked here cannot establish
that hypothesis for the full actual sequence. Neither general moment
theorem is reproved, and neither supplies the arithmetic coefficients.

### Relevance and stopping qualification

For the proposed intermediate positive-mass mechanism, the unchanged
high component has E_H[p|D(Y)B(Y)|]=O(ell) by L421 (4). The complete
translated bulk, with L429's covariance and mean corrections retained,
obeys E_H[w |E_mu DB|]=O(ell) by L430 (17) and its proof. Thus their
contributions remain lower order after any fixed cosine multiplier.
The latter bound concerns the absolute value of the conditional signed
expectation, not the expectation of |DB|. It does not authorize an
absolute-cubic bound that has not been proved.

If a nonnegative intermediate mass were to supply all the normalized
cosine coefficients, reflection would give a positive circle measure
and every Toeplitz principal minor would have to be nonnegative.
A strictly negative tested minor would therefore stop that mechanism.
All tested minors are instead positive, so this bounded attempt supplies
no such stop. The finite representing measure does not implement a new
law, guarantee other moment tolerances or decide the infinite sequence.
No higher cutoff is tested. Actual/global realization, actual clipping,
capped nondegeneracy, L413's full-error margin and global mixed positivity
remain independent gaps. This is not a positivity theorem for RH.

### Separate critical audit — 2026-10-18, step 225

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-prime-power-cubic-toeplitz-critical-audit.md`.
The inspected primary-source records and audited L406--L409/L430/L431
interfaces are reused. The audit tests only j=0,...,4; it neither
enlarges the finite section nor constructs a law.

**Fixed twists and full physical normalization.** The exact L407
identity has response phases (mn/k)^(it) and (mnk)^(it). Multiplying
its real projection by cosine produces the two characters of weight
1/2, also at j=0 where they coincide. Continuing these characters as
2^(+/-ij tau) puts them inside r^(s-1/2); it does not discard a
derivative from an analytic weight. The ordinary jets and all their
phase derivatives are unchanged. For reduced r=u/v, summing the third
residue class in the primary progression formula gives u precisely
when u divides ab, because v is coprime to u. Summing the remaining
classes gives sum_a gcd(a,u). This verifies A_u and the numerator
convention for both twists, including u=1 and all nonunit classes.
The imported smooth-first sharp transfer therefore applies at each
fixed r. The unchanged signed polar sum is 17/20160; multiplying
alpha sqrt(r)/2 gives exactly the prefactor in (2). The real projection
does not halve this real leading coefficient a second time. This
recovers beta at j=0 and L430/L431's coefficient at j=1.

**Full contour, errors and endpoints.** For tau=t-iq the response
series have absolute terms n^(-5/2-q) and n^(-5/2+q). Their normal
convergence holds on a neighborhood of 0<=q<=11/20; no off-line
complex conjugation is used. On that interval r^q<=1+r^(11/20).
For the single carrier, each of q=11/20,-49/100,51/100 in (5)
lies strictly between -3/2 and 3/2. Thus both exponents
-5/2+q and -5/2-q are strictly below -1, even after fixed logarithmic
powers. Fixed 2^(+/-j) changes only the constant. The summed error
is O_j(H^(11/20)+H^(1/100)+H^(51/100)ell), and the two
connectors cost O_j(H^(71/120)); each is o(H ell^2).
The primitive kernel includes the nearest lattice points at both sharp
endpoints, including equality with a saddle. Its integration by parts
uses |w(2H-i delta)|+integral |w'|, so neither an endpoint nor weight
variation is omitted. These are frequency-level bounds, not a sum of
arbitrary fixed-r asymptotic constants.

For the zero carrier, r=2^j mnk is always integral and r=mnk/2^j
is integral exactly when 2^j divides mnk. At l=r the right-line
amplitude is r^(21/20-1/2)r^(-21/20)=r^(-1/2), so the exact
resonance formula and its O_j(H) sum are correct. Away from it the
grid h Z, h=2^(-j), gives |l-r|>=h. In a unit distance interval
there are at most a fixed number of integers l; the first interval
costs O(1/h), and later intervals give a harmonic sum. Thus the
inverse-distance bound is O_j(log(2+r)), also for h<=r<1.
Combining this with the coefficient bound gives the interior exponent
11/20+(1/100-21/20)+1=51/100 in (8). The exterior exponent is
11/20. Both are response summable for the product twist; the zero
carrier's connectors cost O_j(H^(1/2)). Its entire contribution is
therefore O_j(H), not a missing leading coefficient. This includes
l=r=1 and all denominator-2^j near resonances.

The absolute arithmetic majorant (7) is summable, with vanishing cube
complements. Consequently (9) follows before taking a head limit.
For any tolerance choose a fixed N controlling this tail and the
coefficient tail, then use its fixed-N asymptotic for all H beyond
one onset. This verifies the H-first sequential limit with j fixed.
Finally |cos|<=1 applies to L406's absolute physical error
O(ell^(5/4))=o(ell^2), not to an already integrated signed error.
The complete physical product, including curvature, is covered.

**Exact infinite local tails.** The odd part of the reduced numerator
is identical for both twists even when the odd indices have common
factors. Unique 2-adic decomposition and nonnegative convergent sums
justify (11), with 1<=T_odd<infinity. For d=s-v>=0, summing v
gives x^d[(d+1)/(1-xy)+xy/(1-xy)^2]
=x^d(1+D0 d)/D0^2. For d=-h<0, summing s gives y^h/D0^2.
For nonnegative d, the A-factor is one below L=max(0,-j), and
is 2^(-j-d)(1+(j+d)/2) at and above L. Expanding its product
with 1+D0 d yields exactly the three coefficients of S0,S1,S2
in (12). For negative d=-h the nontrivial range is 1<=h<j;
from M=max(1,j) onward the factor is one. Equality at d=-j or
h=j has A_1=1 in either expression. These disjoint partitions cover
every pair s,v, with no truncated infinite tail. Differentiated
geometric series are valid at z=1/8. This checks (12) for all nine
requested j, including both boundary transitions.

**Certificate and moment conclusion.** Inspected the complete script,
replayed `python3 scripts/discriminant/prime_power_cubic_toeplitz.py`,
and inspected all nine local factors, five coefficients, all 31 full
principal-minor records, all exact size minima and every check field
using the JSON inspector. The factors and coefficients agree with
(3) and the tables; the j=-1,0,1 factors agree with audited L431.
The conversion of 2^(-j/2) for odd j uses
2^(-floor(j/2)-1)sqrt(2), so the inverse square-root factor is retained.
The script enumerates every nonempty subset once, forms index
differences, and uses exact Fraction arithmetic. Its Leibniz signs
count inversions. The second algorithm uses rational elimination after
congruence by diag(1,sqrt(2),1,sqrt(2),1), then divides determinants
by 2 to the number of odd indices. That is exactly det(D_S)^2;
it is positive and accounts for the scaling of every subset.

Actual count=required count=31; positive count=31; failures=[].
All determinants have zero sqrt(2) component, and their rational
numerators and denominators are positive. The full determinant is
41743885318401109179553/119093265429995035033600000>0.
Every size minimum agrees with the table. The complete evidence is
`scripts/discriminant/prime_power_cubic_toeplitz_certificate.json`.
The computations verify finite arithmetic; the preceding convergent
sum identities, not a finite numerical sample, justify the coefficients.

Yang--Xie's cited Theorem 1 applies also in the full-rank case, without
uniqueness. Its mass is c_0=1. Reflecting a representing measure and
averaging preserves every cosine integral and removes its sine
integrals. Conversely a measure with those cosine integrals gives
this Toeplitz matrix after that reflection. No claim about the actual
sine-weighted physical product is used. Helton--Putinar's cited
infinite theorem requires all finite sections and therefore supplies
no additional conclusion here.

For relevance, the high cubic is nonnegative by L421's orientation,
so its signed O(ell) bound is also its absolute bound. The translated
bulk instead uses L430's absolute value of its complete conditional
signed expectation, including all mean and covariance corrections.
That O(ell) bound suffices for any fixed cosine multiplier; replacing
it by an absolute third moment would be unjustified and is not done.

No defect or missing direct mathematical input was found. The audit
validates finite-prefix compatibility only. The canonical argument and
DAG inputs are unchanged. This is independent validation of a local
known-tool specialization, not a new theorem beyond the checked sources,
an infinite measure, a new law, or an RH advance. The harmonic-4 stop
and all independent realization, clipping and regulator gaps remain.

## Mathlib

Full matching coverage of these physical cubic coefficients, the exact
prime-2 specialization, and this trigonometric moment application was
not checked. The cited primary moment theorems and analytic interfaces
are the inputs; unknown Mathlib availability is not evidence of absence.
