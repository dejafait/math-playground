# L745: A complete-energy floor for a separated corrected-carrier span

## Hypotheses

Fix an integer K>=2, ell=log(3)/2, L=K ell, and one complex smooth
cell train w from L744 (1), with ||w||_2=1. Fix chi as in L744 (3).
All supports, K, w and chi are fixed before any frequency limit.
Use exactly L744's complex-linear correction h_t=h_(t,w) and
v_t=exp(itx)w-h_t, including both moments on every cell. All functions
are extended by zero. Write

    F_f(xi) = integral_R f(x) exp(-i xi x) dx,
    dmu(xi) = dxi/(2*pi),
    m(xi) = Re psi(1/4+i xi/2) - log(pi),
    Cprime = 2 sum_(2<=n<exp(L)) Lambda(n)/sqrt(n).

E_L is L744's complete finite-window energy; B_L is its Hermitian
arithmetic operator, including every prime power and the factor two.
The inner product is linear in its first argument. L744 (6)-(8)
give, for every smooth test on this fixed window,

    E_L(f) = integral m |F_f|^2 dmu
           + 2 Re(F_f(i/2) conjugate(F_f(-i/2))) - <B_L f,f>,
    <B_L f,f> <= Cprime ||f||_2^2.                         (1)

The external normalization input is H. L. Montgomery and R. C. Vaughan,
*Hilbert's inequality*, J. London Math. Soc. (2) 8 (1974), 73-82,
[Theorem 2 (1.6), Corollary 2 (1.8), pp.74-75; proof p.82](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
DOI 10.1112/jlms/s2-8.1.73. For any finite real delta-separated
frequencies and arbitrary complex a_r, it states

    (U-2*pi/delta) sum |a_r|^2
      <= integral_0^U |sum a_r exp(i t_r x)|^2 dx
      <= (U+2*pi/delta) sum |a_r|^2,   U>0.              (2)

The already inspected continuous theorem is imported, not reproved.
The fixed weight and correction are absent from its statement; the
application below is necessary to obtain this notebook's target.
The only further analytic inputs are Plancherel, smooth integration
by parts, Cauchy--Schwarz and L744's audited symbol estimates. The
latter specialize [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) with
the complex remainder in [5.11(ii)](https://dlmf.nist.gov/5.11#ii).
No source positivity computation or RH-conditional L742 assertion is used.

## Conclusion

There is Delta0>0 such that, for each fixed Delta>=Delta0, there are
T0 and a nonnegative epsilon(T)=O_(K,w,chi,Delta)(T^(-1/2)) tending
to zero, for which the following holds. For every T>=T0, every finite
real carrier set satisfying

    |t_r| >= T,    |t_r-t_s| >= Delta for r != s,

and every nonzero complex coefficient vector c, the function
V=sum c_r v_(t_r,w) is nonzero and

    E_L(V)/||V||_2^2 >= log(T/(2*pi)) - Cprime - epsilon(T). (3)

The lower norm constant relative to ||c||_ell2^2 and the normalized
error are independent of carrier count, maximum carrier magnitude
and the coefficients. Both signs of carriers are
allowed. Explicit constants and a permissible T0 appear below.
This is a standard Fourier specialization/REPRODUCTION, written on
4 November 2026, step 292. The separate conceptual audit in step 294
below accepts (3) without changing its hypotheses or bound. It supplies only the stated
trial-space floor, not a low-frequency, complement, arbitrary-profile
or support-uniform sign theorem, and not an RH candidate.

## Proof

### 1. Pay the uncorrected synthesis norm by the cited theorem

Since w is continuous and nonzero, choose a closed interval I inside
one of its open cells, of length U>0, and alpha>0 such that |w|>=alpha
on I. These choices are fixed. Put

    Delta0 = 4*pi/U,
    a = alpha^2 U/2,
    b = ||w||_infinity^2 (L+2*pi/Delta).

For S_c(x)=sum c_r exp(i t_r x) and f=w S_c, apply (2) on I.
Translation of I just multiplies each coefficient by a unit complex
number, so its squared coefficient norm is unchanged. Since
Delta>=Delta0, U-2*pi/Delta>=U/2. Applying the upper half of (2)
on (0,L) also gives

    a ||c||_ell2^2 <= ||f||_2^2 <= b ||c||_ell2^2.       (4)

The frequencies in (2) may have either sign and have no maximum-size
restriction. All its hypotheses therefore hold for the present set.
No new frame theorem, or assertion of a bounded demodulated H2 norm,
is required for (4).

### 2. Pay the entire correction map

Use M=||w||_H2 in L744 (12)-(13), and define its fixed constants

    Rchi = ||G^(-1)|| (||b_+||_H2^2+||b_-||_H2^2)^(1/2),
    H = Rchi sqrt(33 ell exp(ell)/8) M.

L744 proves ||h_t||_H2 <= H |t|^(-2) for nonzero real t. It also
proves the exact cellwise moment cancellation of v_t. Set

    s(T) = 2 T^(-4) + 2/(3 Delta T^3),
    R(T) = H sqrt(s(T)),
    CDelta = 2 + 2/(3 Delta).

Order the positive carriers increasingly. The j-th, counting from
j=0, is at least T+j Delta. The absolute values of the negative
carriers obey the same bound in increasing order. Thus, using the
integral comparison for a decreasing positive function,

    sum_r |t_r|^(-4)
      <= 2 sum_(j>=0) (T+j Delta)^(-4)
      <= 2 T^(-4) + 2 integral_0^infinity (T+u Delta)^(-4) du
      = s(T).                                             (5)

Empty half-lines cause no problem. Although only finite carrier sets
are used, the convergent infinite majorant makes (5) independent of
their cardinality and extent. For h=sum c_r h_(t_r), the triangle
inequality and scalar Cauchy--Schwarz now give

    ||h||_H2 <= sum |c_r| ||h_(t_r)||_H2
              <= H ||c||_ell2 (sum |t_r|^(-4))^(1/2)
              <= R(T) ||c||_ell2.                         (6)

This is a collective synthesis estimate; it does not sum individual
Rayleigh inequalities. In particular, with V=f-h,

    (sqrt(a)-R(T)) ||c||_ell2 <= ||V||_2
                           <= (sqrt(b)+R(T)) ||c||_ell2. (7)

The lower bound will be used only when its left coefficient is positive.
For T>=1, s(T)<=CDelta T^(-3). Hence the explicit choice

    T0 = max{4, (4 H^2 CDelta/a)^(1/3)}                    (8)

ensures R(T)<=sqrt(a)/2 for every T>=T0. Thus
||V||_2^2>=a ||c||_ell2^2/4, in particular V!=0 when c!=0.

### 3. Bound the bounded deficit, not the whole logarithmic energy

Let c_T=log(T/(2*pi)) and D_T(xi)=[c_T-m(xi)]_+. L744 (8) states

    |m(xi)-log(|xi|/(2*pi))| <= 2/xi^2 for |xi|>=1,
    |m(xi)| <= A+log(2+|xi|),
    A = 2+8 sqrt(2)/3+log(4*pi).                          (9)

For |xi|<=1 this gives m>=-A-log3, and for |xi|>=1 it gives
m>=-log(2*pi)-2. Consequently, with the convenient constants

    B = A+log3+log(2*pi)+2,
    M_T = B+log T,

we have 0<=D_T<=M_T for T>=4. Define the finite seminorm

    ||g||_(D_T)^2 = integral D_T(xi)|F_g(xi)|^2 dmu(xi).

It is well defined for all L2 functions by Plancherel, obeys the
triangle inequality, and is at most M_T ||g||_2^2 after squaring.
The actual energy integral remains finite for every present test,
since it is a finite smooth compactly supported sum.

Let q=sqrt(T), J_T={xi: |xi|<T-q}, and

    eta_T = 2/sqrt(T) + 8/T^2.

Outside J_T, |xi|>=T-q>=T/2>=2. The first estimate in (9) yields

    D_T(xi) <= log(T/(T-q)) + 2/(T-q)^2 <= eta_T.       (10)

For the last inequality, use -log(1-z)<=2z for 0<=z<=1/2,
with z=T^(-1/2). This bound also covers arbitrarily large |xi|:
the displayed positive upper bound dominates the positive part of
log(T/|xi|)+2/xi^2. No upper carrier bound has entered.

### 4. Collective leakage into the inner interval

The zero extension of w is smooth and compactly supported. Put

    C = 4 (||w||_1+||w''||_1),    g(u)=|F_w(u)|.

The L1 Fourier bound for |u|<=1 and twice integrating by parts for
|u|>=1 show

    g(u) <= C/(1+|u|)^2.                                 (11)

There are no cell-endpoint boundary terms. Indeed w and all its
derivatives vanish in neighborhoods of all the finitely many cell
endpoints. For |u|>=1, (1+|u|)^2/u^2<=4; for |u|<=1,
(1+|u|)^2<=4. These observations verify the same C in both regions.

For each xi in J_T and every carrier, |xi-t_r|>=q. Order the carriers
on either side of xi by their distance from xi. Each side's j-th
distance is at least q+j Delta. From (11) and integral comparison,

    sum_r g(xi-t_r)
      <= 2C [(1+q)^(-2) + 1/(Delta(1+q))] =: P(q).     (12)

For each fixed r, changing variables u=xi-t_r gives

    integral_(J_T) g(xi-t_r) dmu(xi)
      <= (C/(2*pi)) integral_(|u|>=q) (1+|u|)^(-2) du
      = C/(pi(1+q)) =: Q(q).                            (13)

Here the row sum and column integral are paid separately. To justify
the continuous-kernel step directly, at each xi apply the triangle
inequality and weighted Cauchy--Schwarz to the finite sum:

    |F_f(xi)|^2 = |sum c_r F_w(xi-t_r)|^2
      <= (sum |c_r|^2 g(xi-t_r)) (sum g(xi-t_r)).

Integration and (12)-(13) give

    integral_(J_T) |F_f|^2 dmu <= J(q) ||c||_ell2^2,
    J(q) = P(q)Q(q)
         = (2 C^2/pi)[(1+q)^(-3)+Delta^(-1)(1+q)^(-2)]. (14)

All sums originally integrated are finite and nonnegative, and their
majorants are integrable. Thus no passage from a finite matrix norm
theorem to an unproved integral-operator estimate is implicit in (14).
This is the needed weighted application bound, not merely pairwise
control whose cost could grow with dimension.

Combine (4), (10), (14), and D_T<=M_T on J_T. The result is

    ||f||_(D_T)^2 <= p(T) ||c||_ell2^2,
    p(T) = b eta_T + M_T J(sqrt(T)).                     (15)

For the entire correction, (6) and boundedness of D_T give
||h||_(D_T)<=sqrt(M_T) R(T)||c||_ell2. Its frequency support need
not be high. The seminorm triangle inequality therefore yields

    ||V||_(D_T)^2
      <= [sqrt(p(T))+sqrt(M_T)R(T)]^2 ||c||_ell2^2.     (16)

This treats the cross term and the full correction within the
nonnegative deficit. No norm weighted by the largest carrier, or
uniform bound for the entire positive logarithmic energy, is assumed.

### 5. Normalize and retain the full energy

Pointwise m>=c_T-D_T, so for N=||V||_2^2,

    integral m |F_V|^2 dmu >= c_T N - ||V||_(D_T)^2.

By linearity of the exact moments in L744 (3)/(7), each local moment
of V vanishes, and hence F_V(i/2)=F_V(-i/2)=0. Both complex pole
terms in (1) vanish exactly; neither is dropped by a sign estimate.
Using the full arithmetic bound in (1), followed by (7) and (16),
proves (3) with

    epsilon(T) = [sqrt(p(T))+sqrt(M_T)R(T)]^2
                     / (sqrt(a)-R(T))^2,   T>=T0.       (17)

Every constant in (17) depends only on K,w,chi,Delta and the interval
and alpha chosen once from w. To check the required threshold,

    eta_T = O(T^(-1/2)),  J(sqrt(T)) = O_(w,Delta)(T^(-1)),
    M_T = O(log T),       R(T) = O_(K,w,chi,Delta)(T^(-3/2)).

Thus p(T)=O(T^(-1/2)+log(T)/T)=O(T^(-1/2)), and, using
(x+y)^2<=2x^2+2y^2, the numerator in (17) is O(T^(-1/2)).
The denominator is at least a/4 by (8). This proves the asserted
nonnegative vanishing error with coefficient one on log(T/(2*pi)).
One may define epsilon(T)=0 below T0, where no inequality is asserted.

The conclusion remains fixed-window and fixed-profile. It does not
show that these separated carriers span the full neutral space, give
a sign for their moment complement, control coupling to low-frequency
tests, or bound constants as K or the profile changes. Eventual
positivity on this space requires log(T/(2*pi))>Cprime+epsilon(T).
The prime-only supremum obstruction and generic-source scope stop
remain unchanged.

### Separate conceptual audit (4 November 2026, step 294)

The exact assertion (3) passes under the prior SPECIALIZE assessment
`drafts/literature/2026-11-04-collective-corrected-carrier-span-audit.md`.
This is independent verification of the written specialization, not a
new external theorem or a sign result beyond this trial space. No
mathematical correction was needed. The source statement and proof-scope
assessment of Montgomery--Vaughan are reused; their theorem is not
reproved. The direct local input remains audited L744.

1. **All coefficient vectors and both carrier signs.** A continuous
   nonzero w has a positive lower modulus on a nondegenerate closed
   interval contained in one open cell. Translation in (2) replaces
   c_r by c_r exp(i t_r x_0), preserving each modulus, also for negative
   t_r. The fixed gap Delta>=4*pi/U gives the lower constant a>0.
   Since |w|<=||w||_infinity and its support is in (0,L), the same
   source upper bound gives b. No bound on the degree, largest frequency
   or derivatives of S_c is used. The actual norm depends on c; it is
   the constants in its two-sided comparison (4) that are uniform.

2. **Collective correction and the threshold before squaring.**
   L744 (12)-(13) applies with the fixed M=||w||_H2. Its right inverse
   acts on complex moments linearly, and its basis is not modulated.
   The two carrier half-lines separately give T+j Delta in (5); their
   union costs exactly the displayed factor two. Cauchy--Schwarz bounds
   the finite synthesis map by H times the square root of that summable
   inverse-fourth-power majorant. For T>=1 its square is at most
   H^2 CDelta T^-3. The choice (8) therefore implies R<=sqrt(a)/2,
   before (7) is squared, and N>=a||c||_ell2^2/4. This checks the
   denominator for every nonzero c without an independence assumption
   on the corrected functions; their independence follows from it.

3. **Global deficit, including frequencies near zero.** On |xi|<=1,
   (9) gives m>=-A-log3; on |xi|>=1 it gives
   m>=-log(2*pi)-2. These imply 0<=D_T<=B+log T for T>=4 with the
   stated B. No logarithmic approximation is used at zero. On the
   complement of J_T, T-sqrt(T)>=T/2>=2 and the digamma remainder is
   at most 8/T^2. With z=T^-1/2<=1/2, -log(1-z)<=2z gives (10).
   The positive part remains bounded by eta_T even when |xi|>T, where
   log(T/|xi|) is negative. The deficit multiplier is bounded and
   nonnegative; its seminorm and triangle inequality hold on all L2.

4. **Continuous leakage with the correct measure.** The finite cell
   train has smooth zero extension, so two integrations by parts have
   no boundary terms and give exactly (11). For xi in J_T, each carrier
   lies at distance at least sqrt(T). On each side of xi these distances
   are Delta-separated. Integrating the decreasing majorant on each
   half-line gives P(q), without a cardinality factor. For one carrier
   the translated inner interval is a subset of {|u|>=q}; integration
   of both tails with measure du/(2*pi) gives Q(q)=C/[pi(1+q)].
   Weighted Cauchy--Schwarz and then this column integral prove (14).
   Only finite sums are integrated; the infinite sums are convergent
   positive bounds. Hence neither a missing integral-operator theorem
   nor an uncontrolled finite-to-infinite interchange is needed.

5. **Complete correction and normalized rate.** Inside J_T use
   M_T times (14); outside use eta_T times the upper norm in (4).
   This proves (15). Plancherel bounds the entire correction in the
   deficit norm by sqrt(M_T)R||c||, and its triangle inequality includes
   all mixed terms in (16). In particular no full positive logarithmic
   energy is bounded uniformly in maximum carrier. For T>=T0, (17) is
   also bounded above by (8/a)[p(T)+M_T R(T)^2]. Here
   p=O(T^-1/2+log(T)/T)=O(T^-1/2) and
   M_T R^2=O(log(T)/T^3); all constants have only the allowed fixed
   dependencies. This proves the claimed rate with a nonnegative loss.
   The lower denominator is used only on that loss, never to change
   the coefficient of c_T, so the argument also covers negative c_T.

6. **Poles, arithmetic and scope.** For each cell and each sigma,
   linearity gives integral e^(sigma s/2)V(s+j ell)ds=0. Multiplication
   by e^(sigma j ell/2) and the finite cell sum cancel F_V(sigma i/2)
   exactly. Both factors in the complex pole product are therefore
   zero. The Hermitian prime bound is applied to V itself after forming
   the whole span, with every prime power and the factor two from (1).
   Its sign is E=Q_m-<B_L V,V> once the poles vanish. This gives (3).
   All tests remain finite smooth compact sums in L744's domain.
   L740/L741/L743 enter through L744's audited normalization; no
   RH-conditional conclusion of L742 is an input.

The audit establishes only this fixed-K,w,chi,Delta trial-space floor.
No completeness of the separated span, moment-complement sign, low-block
sign, signed coupling estimate or uniformity as support grows follows.
The eventual positivity condition remains the one stated above.

## Mathlib

Full matching Mathlib coverage of (3), including the complete operator,
smooth cell correction and cardinality-independent logarithmic deficit,
has not been checked. No formal verification or absence claim is made.
Plancherel and Fourier differentiation are standard supporting inputs;
the imported separated-frequency theorem is cited precisely above.
These supporting facts are not a full matching theorem. The weighted
normalization, collective correction and deficit specialization are
proved explicitly here and pass the separate informal audit above.
