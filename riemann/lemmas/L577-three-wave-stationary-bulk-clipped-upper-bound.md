# Lemma 577: the equal-amplitude three-wave bulk misses the clipped threshold

## Hypotheses

Let U_1,U_2,U_3 be independent uniform variables on [-1/2,1/2],
and B_1,B_2,B_3 independent uniform variables on [0,2pi], all six
mutually independent. For real x set

    S(x)=sqrt(2/3) sum_(i=1)^3 cos(U_i x+B_i),
    J=(S(0),S'(0),S''(0),S(1),S'(1),S''(1)),
    Q(J)=(S(0)S''(0)-S'(0)^2)_+.

Derivatives are ordinary x derivatives and the paired norm is Euclidean.
The comparison matrix is exactly L473 (6), with r,s in {0,1} and
j,k in {0,1,2}:

    K_((r,j),(s,k))
      =integral_(-1/2)^(1/2) (iw)^j(-iw)^k exp(i(r-s)w) dw.

Only this explicit matrix is used from L473. No arithmetic moment,
actual Hardy sampling, Xi realization, RH or real-zero premise is used.
The nonlinear upper bound below is computer assisted, with exact
integer summation and rational enclosures, rather than sampled evidence.

## Conclusion

The joint derivative process through order two is stationary under every
real shift, has real analytic bounded paths, and satisfies

    E J=0, E JJ^T=K,
    sup_(x in R)|S^(j)(x)|<=sqrt(6)/2^j, j=0,1,2,
    |J|^2<=63/4,
    0<=E Q(J)<=470333750554794227838685/149944580564076974825275392
              <13/4000<1/288.                                  (1)

For ell=log H>0, F_H=sqrt(ell) S has paired covariance ell K and
paired norm at most ell^2 whenever ell^3>=63/4. Its four tight
same-height odd second entries in L473 vanish exactly. Nevertheless
E Q(F_H)<ell/288, so it cannot supply the nominated bulk lower bound.
No fourth-moment constraints of L473 are verified. No other stationary
process or actual-Hardy negative-mass conclusion follows.

## Proof

### Covariance, stationarity and support

For fixed w and uniform b, write the j-th ordinary derivative as
Re((iw)^j exp(i(wx+b))). The phase integrals E exp(ib)=E exp(2ib)=0
give zero means and

    E_b [Re((iw)^j exp(i(wr+b)))
         Re((iw)^k exp(i(ws+b)))]
       =(1/2) Re((iw)^j(-iw)^k exp(i(r-s)w)).                    (2)

Cross-wave terms vanish by independent centered phases. The factor
(2/3)*3*(1/2)=1 yields exactly every entry of K, including all nine
cross-height entries. The integral is real by conjugation and w -> -w.
At r=s its odd-total-order entries vanish, including (j,k)=(0,1)
and (1,2) at both heights. No independence of the two jets is assumed.

Conditional on the three frequencies, replacing B_i by B_i+U_i h
modulo 2pi preserves the independent uniform conditional phase law,
which is independent of those frequencies. This represents translation
of the whole process and its derivatives by h, and proves joint
finite-dimensional stationarity for every real h. Finite cosine sums
have real analytic paths. For every outcome and x,

    |S^(j)(x)|<=sqrt(2/3) sum_i |U_i|^j<=sqrt(6)/2^j.

Hence |J|^2<=2*6*(1+1/4+1/16)=63/4. All polynomial observables
are integrable. Scaling multiplies the squared paired norm by ell;
(63/4)ell<=ell^4 under the stated sufficient onset. It multiplies
Q by ell because ell>0 and Q is homogeneous of degree two.

### Integral and coordinate curvature bounds

One may replace each signed frequency by u_i=|U_i|, uniform on
[0,1/2]. When U_i<0 also replace B_i by -B_i modulo 2pi. This
preserves the entire cosine path and the independent conditional uniform
phase law. At x=0 put c_i=cos B_i, s_i=sin B_i, and

    X=sum_i c_i, Y=sum_i u_i s_i, Z=sum_i u_i^2 c_i,
    D=-(2/3)(XZ+Y^2), q=max(D,0).                              (3)

Thus E Q is the normalized integral of q over
[0,1/2]^3 x [0,2pi]^3. There are no singularities at zeros of S,
coincident frequencies or zero frequencies.

For one coordinate v, call f M-semiconvex if f(v)+Mv^2/2 is
convex with the other coordinates fixed. A smooth function with
second derivative >=-M has this property. If D has this property,
max(D,0) does too: after adding Mv^2/2 it is the maximum of the
two convex functions D+Mv^2/2 and Mv^2/2. This observation handles
the nondifferentiable clipping boundary without assuming smoothness of q.

Direct differentiation of (3) gives

    d^2 D/du_i^2=-(4/3)(X c_i+s_i^2)
               =-(4/3)(1+c_i sum_(j!=i)c_j)>=-4.              (4)

For phase derivatives expand, without dividing by any coordinate,

    D=-(2/3)[sum_i u_i^2+
       sum_(i<j)((u_i^2+u_j^2)c_i c_j+2u_i u_j s_i s_j)].       (5)

The absolute value of each bracketed pair is <=u_i^2+u_j^2.
Indeed it is the bilinear form between the two unit vectors
(c_i,s_i),(c_j,s_j), with diagonal matrix
diag(u_i^2+u_j^2,2u_i u_j), whose operator norm is u_i^2+u_j^2.
It follows that

    d^2 D/dB_i^2 >= -M_i(u),
    M_i(u)=(2/3)(2u_i^2+sum_(j!=i)u_j^2),
    sum_i M_i(u)=(8/3)sum_i u_i^2.                             (6)

These are coordinate bounds on the whole compact domain. No mixed
curvature or joint convexity is asserted or needed.

### One-sided tensor quadrature error

On a panel [a,b] of length h, semiconvexity implies

    f(v)<=linear_interpolant(f(a),f(b))(v)
                  +(M/2)(v-a)(b-v).

This follows by applying the defining convex inequality to
f(v)+Mv^2/2 and subtracting Mv^2/2. Integration yields composite
trapezoid upper error at most M h^2/12 for the normalized integral
on any interval with equal panels. It applies to the continuous clipped
function q. Iterating the one-coordinate inequalities with positive
integration/trapezoid operators adds their error bounds; all functions
here are bounded on compact rectangles, so Fubini is valid.

First hold u fixed and integrate all three phases, with N_B panels in
each phase. Periodicity makes each normalized phase trapezoid the
uniform average on the N_B distinct nodes 2pi*m/N_B. Equations (6)
give phase error <=h_B^2*(8/3)sum_i u_i^2/12, h_B=2pi/N_B.
Average this error over the actual frequency law. Since
E sum_i u_i^2=3*(1/12)=1/4, it is at most

    h_B^2/18=2*pi^2/(9*N_B^2).                                (7)

Next apply frequency trapezoids to the finite phase average of q.
Positive phase averaging preserves (4)'s coordinate semiconvexity.
With N_U frequency panels, h_U=1/(2N_U), its total upper error is
3*4*h_U^2/12=1/(4N_U^2). If G denotes the full tensor average at
the exact trigonometric nodes, then

    E Q<=G+1/(4N_U^2)+2*pi^2/(9N_B^2).                         (8)

The phase error in (7) was integrated exactly before frequency
quadrature; it was not silently replaced by an average on the frequency
grid. This order accounts for all six coordinates.

### Rational trigonometry and exact finite sum

Use N_U=16, N_B=48, M=2^24. For every m=0,...,47 the certificate
gives integers C_m,S_m in [-M,M] such that

    |cos(2pi*m/48)-C_m/M|<=1/M,
    |sin(2pi*m/48)-S_m/M|<=1/M.                                (9)

The complete enclosures are in `scripts/three-wave/certificate.json`.
Here is their rigorous construction, implemented with Python Fraction.
For a=atan(1/5), b=atan(1/239), use 32 terms of each alternating
power series and error at most x^65/65. Machin's identity gives
pi=16a-4b. To check this identity, tan(2a)=5/12, tan(4a)=120/119,
and tan(4a-b)=(120*239-119)/(119*239+120)=1;
0<4a-b<4/5<pi/2 selects 4a-b=pi/4. Thus the rational pi enclosure
is justified, and exact comparisons also prove its upper endpoint <22/7.

Reduce each phase to [-pi,pi], use its rational midpoint argument,
and evaluate the degree-79 sine/cosine Taylor polynomial with error
<=|x|^80/80!. For cosine the degree-79 coefficient is zero.
The uncertainty of the argument adds at most its radius because real
sine and cosine are 1-Lipschitz. Round enclosing endpoints outward to
denominator 2^50, and choose the displayed integers at scale M.
For all 96 trigonometric values, exact rational comparisons verify (9)
and |C_m|,|S_m|<=M. No library floating-point trigonometry is used.

For the grid approximations Xhat,Yhat,Zhat in (3), (9) gives

    |X-Xhat|<=3/M, |Z-Zhat|<=3/(4M), |Y-Yhat|<=3/(2M).

Both exact and approximate X,Z,Y are bounded in absolute value by
3,3/4,3/2, respectively. Consequently
|XZ-Xhat Zhat|<=9/(2M) and |Y^2-Yhat^2|<=9/(2M).
Equation (3) and the 1-Lipschitz positive-part map imply a uniform
grid-value error <=6/M. It remains valid after every normalized positive
quadrature average.

The frequency nodes are k/(2N_U), k=0,...,N_U. Set w_k=1 at the
two endpoints and w_k=2 otherwise. Their normalized weights are
w_k/(2N_U), whose sum is one. At a grid node with frequency indices
(i,j,k) and phase indices (a,b,d), define the exact integer

    R=-(C_a+C_b+C_d)(i^2 C_a+j^2 C_b+k^2 C_d)
                          -(i S_a+j S_b+k S_d)^2.

If T is the sum of w_i w_j w_k max(R,0) over all these nodes, the
rounded full tensor average is

    Ghat=2T/[3*(2N_U)^5*M^2*N_B^3].                            (10)

`scripts/three-wave/tensor_sum.cpp`, generated by
`scripts/three-wave/certify.py`, enumerates all
17^3*48^3=543338496 nodes and gives

    T=1891247392706538463615488,
    Ghat=1231280854626652645583/1020031160299843366158336.

The certificate retains every outer-frequency slice and checks their
sum. All evaluations of R are signed 64-bit integer operations:
|R|<=18*N_U^2*M^2=1297036692682702848<2^63, with each product
and intermediate sum also within that bound. The positive weighted
aggregate is accumulated in signed 128-bit integers and bounded by
8*(543338496)*18*N_U^2*M^2<2^127. There is no overflow or rounding
in this sum; all subsequent comparisons are exact rational arithmetic.

Combining (8)--(10), the pi upper bound and the rounding error gives

    E Q <= Ghat+3/8388608+1/1024+121/127008
         =470333750554794227838685/149944580564076974825275392
         <13/4000<1/288.                                      (11)

The exact difference between 1/288 and the bound is
50307154181584156971299/149944580564076974825275392>0.
Thus this is an upper-bound certificate deciding the required threshold,
not a Monte Carlo confidence statement or a numerical preview.

Reproduce with `python3 scripts/three-wave/certify.py` (Python 3 and
a C++17 compiler with signed 128-bit integer support). It writes the
complete rational certificate and generated source, prints all error
terms and the required/actual bounds, and checks the finite sums,
enclosures, overflow bounds and final strict inequalities. The printed
decimal values are convenience previews only. Inspect the exact fields
with `python3 ../scripts/loop/inspect_json.py scripts/three-wave/certificate.json --pointer /bounds --full`.
The initial exploratory sample is not an input anywhere in this proof.

### Source specialization and limits

The prior EXPLORE assessment is
`drafts/literature/2026-10-31-three-wave-stationary-bulk-review.md`.
For covariance it reuses Ali Rahimi and Benjamin Recht, *Random Features
for Large-Scale Kernel Machines*, Advances in NIPS 20 (2007), Section 3,
Theorem 1, equation (2), subsequent real random-phase formula and
Algorithm 1, PDF pp. 2--4,
[author PDF](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf).
The probability spectral measure here is uniform on [-1/2,1/2]; the
normalization and all derivative/cross-height entries were verified in
(2). These direct elementary checks specialize the known covariance
construction. They are needed to identify the full K and the support
bound, not to reprove an arithmetic moment result. The nonlinear
certificate is the bounded comparison not supplied by the sources
inspected; no certified originality claim follows.

L576 is a contrast and motivation, not an input: its two-wave exact-zero
factorization is not used for the three-wave upper bound. L471 supplies
motivation only. This failure stops this specific equal-amplitude
three-wave choice. It does not disprove stationary moment feasibility,
the 126 fourth constraints, actual-Hardy negative-mass saving or RH.
Rare paths, derivative-preserving corrections and transfer of any
constructed law to actual Hardy samples remain independent gaps.
The separate audit below verifies the application and complete certificate;
it does not audit an arithmetic source or establish a stronger bound.

### Independent application and certificate audit, 2026-10-31

The ready assessment was
`drafts/literature/2026-10-31-l577-independent-certificate-audit.md`.
Rechecked (2) against every index in L473 (6): conjugation of the second
derivative factor supplies the sign (-iw)^k, and the independent phases
remove only cross-wave terms, not cross-height terms. Conditional phase
translation proves stationarity of the derivative process, not just its
covariance. The deterministic squared norm and scaled onset are as stated.
Only the exact matrix definition in L473 is used; its arithmetic moment
theorems are not premises of this audit.

Rechecked both coordinate curvatures directly from (3). In particular
X c_i+s_i^2=1+c_i sum_(j!=i)c_j, so the frequency lower curvature is
-4. The phase-pair operator norm is u_i^2+u_j^2 because
2u_i u_j<=u_i^2+u_j^2 on [0,1/2]^2. Adding the quadratic before
taking the maximum proves semiconvexity even on the clipping boundary.
Each coordinate error is a uniform bound in the other phase coordinates.
The phase errors are therefore additive under the positive tensor
operators. Integrating their frequency-dependent bound over the actual
frequency law gives (7), before frequency quadrature is applied to the
phase-node average. The frequency errors then give (8). This checks all
six coordinates without a mixed-derivative or smooth-clipping premise.

For the trigonometric certificate, the alternating-series remainder and
Taylor's degree-79 remainder used above are valid, including cosine's
zero degree-79 coefficient. For the branch in Machin's identity,
a>1/5-1/375=74/375 and b<1/239 give 4a-b>0; also
4a-b<4/5<pi/2. Thus the tangent computation selects exactly pi/4.
The 1-Lipschitz argument for the uncertain phase is on the real axis.

`scripts/three-wave/audit.py` independently encloses pi using 40
alternating terms with one-sided remainder intervals and checks these
against the stored 32-term symmetric enclosure. It then uses degree-99
Taylor polynomials at the tighter rational midpoint, with remainder
|x|^100/100! and the phase-radius error. Endpoints are rounded outward
to denominator 2^80. For each of all 96 sine/cosine values, exact
comparisons check that this independent enclosure lies inside the
stored enclosure, and that the stored rounding error and |C_m|,|S_m|
bounds hold. All complete enclosures and comparisons are retained in
`scripts/three-wave/audit.json`; no floating trigonometry is used.

The same audit compiles and completely replays the original C++ sum
with undefined-behavior sanitization and no recovery. It separately
generates `scripts/three-wave/audit_tensor_sum.cpp`, which traverses
phase triples first and frequencies in reverse order, with all
polynomial products and totals in signed 128-bit integers. Its
independent expansion is

    R=-(i^2 A+j^2 B+k^2 C+ij AB+ik AC+jk BC),
    A=C_a^2+S_a^2+C_a C_b+C_a C_d,
    B=C_b^2+S_b^2+C_b C_a+C_b C_d,
    C=C_d^2+S_d^2+C_d C_a+C_d C_b,
    AB=2 S_a S_b, AC=2 S_a S_d, BC=2 S_b S_d.

These are exact polynomial identities for the rounded integers; in
particular C_a^2+S_a^2 is not replaced by M^2. In this implementation
the sum of the absolute values of its six frequency terms is at most
(3*4+3*2)N_U^2 M^2=18N_U^2 M^2. Thus both its intermediate arithmetic
and the aggregate have safe 128-bit bounds. For the original code,
|Xraw|<=3M, |Zraw|<=3N_U^2 M and |Yraw|<=3N_U M imply each product
is at most 9N_U^2 M^2, and the subtraction is at most
18N_U^2 M^2<2^63. Each partial sum is bounded by the sum of the
absolute summands. The factor w_i w_j w_k is at most eight and is
promoted to 128-bit before multiplication by R; its aggregate bound
is 5637839726872271765177892864<2^127. Counters fit unsigned 64-bit.

Both complete enumerations agree with every one of the 17 stored
outer-frequency slices, all 543338496 nodes, 32925456 positive nodes
and T=1891247392706538463615488. This checks the full sum, not sampled
slices. The normalized frequency weights sum to one. Substituting
u=i/(2N_U) in (3) contributes 2/[3(2N_U)^2 M^2], and the three
normalized frequency weights and three phase averages contribute
1/[(2N_U)^3 N_B^3], giving exactly (10). Rechecked the uniform 6/M
grid error using separate bounds for both factors of XZ and Y^2,
and rechecked all three rational errors, (11), and its positive exact
margin from 1/288. No defect or changed hypothesis was found.

Reproduce this independent audit with
`python3 scripts/three-wave/audit.py`. It reports 415 exact checks,
both exhaustive replay results, the actual/required exact bounds,
failures and the full certificate path. The certificate includes all
96 independent rational enclosures, both complete slice arrays, source
hashes, every class of original 64-bit intermediate bound and exact
normalization/error comparisons. The original certificate and generator
are preserved unchanged. This verifies the specified rejection only;
all fourth-moment and actual-Hardy transfer limitations remain in force.

## Mathlib

Full matching coverage for this stationary paired law, coordinate
semiconvex quadrature argument and explicit clipped certificate was not
checked. No absence claim is made. No Mathlib result is an essential
input; the phase integral, elementary convexity argument and exact
integer/rational computation are given above.
