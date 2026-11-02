# Corollary 673b: exponential cost of a normalized strict-action repair

## Hypotheses

Use L673's exact admissible phase-aligned displacement sequence, not a
rounding of it. Explicitly, q>=1, n=12q+3, N=2q, h=27/(10n),
x=-d=-5/4, U=121/64, and t_j=j/n for all 0<=j<n. For 0<=k<N,

    s_k=k+1/2+atan(1/(10*s_k))/pi,    k+1/2<s_k<k+5/8,
    y_k=h*s_k,    a_(+k)=x+i*y_k,    a_(-k)=x-i*y_k.

Keep L666's full rational angular functions

    W_a(u)=(x/a) product_(1<=j<n)
       [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)], |u|=1.

The original residues remain one. L673's auxiliary positive coefficients
and residual are

    ell_k=(1/2) product_(0<=l<N,l!=k) y_l^2/(y_l^2-y_k^2),
    b_(+k)=b_(-k)=|ell_k|*sqrt(1+100*s_k^2)*exp((3/5)*n*y_k^2),
    R_q=1+sum_(a!=x) b_a W_a,
    ||R_q||_2<=14*exp(18)*n^2*exp(-n/200).                 (1)

All norms and means are normalized on the angular unit circle. Let
Pi_(2n) be orthogonal Fourier projection to the frequencies -2n,...,2n,
put sigma_a=||Pi_(2n)W_a||_2, and use the real pairing

    ell_p(f)=Re mean(conj(p)*f).

No sampled Fourier coefficients, numerical signs, singular values,
mass cap or favorable Gram estimate are assumed.

## Conclusion

There is an absolute q_0 such that for every q>=q_0 and every Laurent
polynomial v of degree at most 2n in each direction satisfying

    ell_v(1)=0,    ell_v(W_a)>=sigma_a for every a!=x,

one has

    ||v||_2>=exp(11*n/1000).                              (2)

Existence of such v is not asserted. More generally, if p has the same
degree restriction, ell_p(1)=1 and ell_p(W_a)>=tau*sigma_a for all a!=x,
where tau>=0, then

    ||p||_2>=tau*exp(11*n/1000).                          (3)

Consequently the fully paid repair budget

    ||p0||_2+epsilon*||v||_2<=exp(n/100)*n^C, epsilon>0,

requires epsilon<=n^C*exp(-n/1000) for all q>=q_0. Likewise a separator
p with ||p||_2<=exp(n/100)*n^C requires its uniform normalized strict
margin tau to be at most n^C*exp(-n/1000). No fixed positive margin or
margin bounded below by c*n^(-A), with fixed c>0,A, can satisfy that
budget along this allowed sequence. This includes a fixed slack floor
of 10^(-8), if it is imposed on exact normalized actions at every n.

This is an obstruction to fixed or polynomial strict slack, not to
nonnegative actions with tau=0, exponentially shrinking slack, or the
rate-1/100 cone bound itself. In a decomposition p=p0+epsilon*v,
failure of the sum-of-norms budget alone does not exclude cancellation
between p0 and epsilon*v. Equation (3) concerns the final margin and
does not use that triangle estimate. The onset q_0 is existential.
No H bound, unit-residue cancellation, Xi realization or mixed sign
is established. This corollary has not had a separate critical audit.

## Proof

### 1. Scope and an exact positive-witness cost inequality

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`
covers this quantitative test of the prescribed affine nonnegative
cone. L672's complex-span stop, C673a's fixed-gauge barrier and the
step-41 floating vectors are comparisons, not proof inputs. L673's
separately audited exact coefficients and continuous bound (1) are
the mathematical positive-witness input; its rate is only 1/200.
No new general projection or separation theorem is needed.

Set

    S_q=sum_(a!=x) b_a*sigma_a,
    E_q=14*exp(18)*n^2*exp(-n/200).

By positivity of the b_a and the hypotheses on v,

    S_q<=ell_v(R_q)<=||v||_2*||R_q||_2<=||v||_2*E_q.    (4)

For p as in (3), the same calculation gives

    1+tau*S_q<=ell_p(R_q)<=||p||_2*E_q.                (5)

These are finite sums and the standard Cauchy--Schwarz inequality in
the real Hilbert structure of complex L2. Thus it suffices to prove

    S_q/E_q>=exp(11*n/1000) eventually.                (6)

This requires an actual lower bound for projected column norms;
using an unprojected norm in place of sigma_a would not suffice.

### 2. One coefficient at a fixed limiting offset

Let k=k_q=floor(n/54). It lies in {0,...,N-1} for every q>=1 and

    k/n -> 1/54,    N/n -> 1/6,    y_k -> y_*=1/20.

Compare ell_k with the exactly uniform-node weight ell_k^0, obtained
by replacing every s_l by l+1/2. Write e_l=s_l-l-1/2, so 0<e_l<1/8.
The numerator of each factor in |ell_k| is at least the uniform one,
while for l!=k,

    |s_l-s_k|<=|l-k|+1/8,
    s_l+s_k<=l+k+1+1/4.

Using log(1+t)<=t gives

    log|ell_k|>=log|ell_k^0|
      -(1/8) sum_(l!=k)1/|l-k|-(1/4) sum_(l!=k)1/(l+k+1)
      >=log|ell_k^0|-(1/2)H_N,                       (7)

where H_N=sum_(1<=j<=N)1/j<=1+log N. There is no uncontrolled
near-node denominator in this comparison.

The uniform product evaluates exactly to

    P_N=product_(0<=l<N)(l+1/2)=(2N)!/(4^N*N!),
    |ell_k^0|=P_N^2/[(k+1/2)*(N-1-k)!*(N+k)!].       (8)

For example the two denominator products before cancellation are
k!*(N-1-k)! and (N+k)!/[k!*(2k+1)], which proves (8), including
k=0. For the asymptotic evaluation it is enough to use
log(m!)=m log m-m+O(log(m+1)). This follows directly by bounding
the increasing sum of log j between its integrals over [1,m] and
[1,m+1]. This elementary finite-product evaluation is included to
control the specific weights; no general interpolation theorem is
being reproved.

Applying that estimate to (8), all n log n and linear terms cancel
after division by n. Since 1/6=(10/27)*(9/20) and
1/54=(10/27)*(1/20), (7) yields

    liminf_q (log b_(+k))/n >= beta,
    beta=(10/27)*[2r log r-(r-y_*)log(r-y_*)
                              -(r+y_*)log(r+y_*)]+(3/5)*y_*^2,
    r=9/20.                                           (9)

The factor sqrt(1+100*s_k^2) is at least one; its logarithm divided
by n tends to zero. The positive quadratic factor contributes the
last term in (9). The exact computation in section 5 proves

    beta>-3/5000.                                    (10)

### 3. Paying for the degree-2n Fourier projection

For a=x+i*y with |y|<=3/50, W_a is holomorphic on the closed annulus
9/10<=|u|<=11/10 and a neighborhood thereof. Its common interior
poles have modulus less than d/U=80/121; its exterior poles have
modulus at least d=5/4. All full-product factors, including j=0,
are retained. For r_0 in {9/10,11/10}, integrate the logarithmic
derivative of the first ratio in the imaginary parameter and use
|x+i*s-t*u|>=d-t*r_0. For the second ratio use the triangle
inequality and log(1+t)<=t. This gives

    log|W_(x+i*y)(u)|
       <=|y| sum_(0<=j<n) [1/(d-t_j*r_0)+t_j/(U*r_0-d*t_j)]
       <=n*|y|*A(r_0),                                (11)
    A(r_0)=(1/r_0)log(d/(d-r_0))
            +(U*r_0/d^2)log(U*r_0/(U*r_0-d))-1/d.

All denominators are positive. Both functions of t in the sum are
increasing, so their left Riemann sums are at most their integrals;
integrating them gives the stated A. Section 5 verifies A(r_0)<3
at both radii. Thus the annulus boundary bound is exp(9n/50).

Write W_a(u)=sum_(m in Z) c_m u^m on this annulus. The standard
Laurent Cauchy coefficient estimate gives, for m>=1,

    |c_m|<=exp(9n/50)*(10/11)^m,
    |c_(-m)|<=exp(9n/50)*(9/10)^m.

Consequently the absolutely convergent omitted tails on |u|=1 obey

    ||W_a-Pi_(2n)W_a||_infinity
       <=exp(9n/50)*[10*(10/11)^(2n)+9*(9/10)^(2n)]
       <=19*exp(-n/100).                              (12)

The last inequality uses log(11/10)>19/200 and log(10/9)>1/10,
both enclosed exactly in section 5. No sample aliases or floating
Fourier coefficients enter (11)--(12).

### 4. A projected column with positive exponential growth

Take the single angular point u_*=(-24+7i)/25 and a=x+i*y_k from
section 2. Eventually |y_k|<=3/50. The full logarithmic product is
a Riemann sum for a continuous function on [0,1] times a compact
neighborhood of y_*. No denominator or numerator vanishes there:
|a|>=d>1 and U>|a|. Uniform continuity, y_k->y_*, and the retained
j=0 term therefore give

    (1/n)log|W_(x+i*y_k)(u_*)| -> F_*,
    F_*=integral_0^1 log|[(x-t*u_*)/(x+i*y_*-t*u_*)]
                           *[(U*u_*-t*(x+i*y_*))/(U*u_*-t*x)]| dt.

Section 5 proves F_*>7/1000. Equation (12) is exponentially smaller
than this growing value. Hence eventually

    |(Pi_(2n)W_(x+i*y_k))(u_*)|>=|W_(x+i*y_k)(u_*)|/2.

Fourier orthogonality and finite Cauchy--Schwarz give

    |(Pi_(2n)W_a)(u_*)|<=sqrt(4n+1)*sigma_a.

In particular the selected sigma is strictly positive eventually and

    liminf_q (log sigma_(+k))/n>=F_*>7/1000.           (13)

No positivity claim about every other projected norm is required:
they are nonnegative by definition. Using the selected term in S_q,
(9), (13) and the explicit E_q imply

    liminf_q (1/n)log(S_q/E_q)
       >=beta+F_*+1/200>57/5000>11/1000.              (14)

The bounds on the right concern fixed quantities and do not depend
on the choice of v or p. Thus (6) holds beyond one absolute onset.
Equations (4)--(5) prove (2)--(3), and division by their lower bound
gives the stated necessary bounds on epsilon and tau.

### 5. Exact constants and verification scope

Run from the notebook directory:

    python3 scripts/one-sided-hankel/positive-cone-repair-cost-certificate.py

The complete certificate is
`scripts/one-sided-hankel/positive-cone-repair-cost-certificate.json`.
All 11 checks pass with no failures. Its outward rational enclosures
include

    7143140627/10^12 <=F_*<=7143140629/10^12,
    -561867988/10^12 <=beta<=-561867987/10^12,
    11581272640/10^12 <=F_*+beta+1/200<=11581272641/10^12.

For completeness, the evaluation method is fully specified here.
For complex v with |v|<=4/5 let

    S(v)=sum_(m>=1) Re(v^m)/[m*(m+1)].

Uniform absolute convergence permits integrating the power series
for log|1-tv|. With a_*=x+i*y_* the resulting identity is

    F_*=(1/2)log(d^2/(d^2+y_*^2))
       +S(u_*/a_*)-S(u_*/x)+S(x/(U*u_*))-S(a_*/(U*u_*)).

All four arguments are rational complex numbers with squared modulus
at most 16/25, as the script checks before evaluation. Each series
is evaluated by exact rational multiplication through degree 100.
Its absolute omitted tail is at most
(4/5)^101/[101*102*(1-4/5)]. All terms and endpoints are stored.

For a positive rational v, reduce v=2^j*w with 1<=w<=2. With
z=(w-1)/(w+1), the first 12 terms of
2*sum_(m>=0)z^(2m+1)/(2m+1) lower-bound log w; the positive omitted
tail is at most 2*z^25/[25*(1-z^2)]. Apply the same enclosure to
log 2 and multiply intervals with the sign of j retained. This
encloses every logarithm in beta and A and the two decay logarithms.
All final intervals are rounded outward to multiples of 10^(-12).
No floating number enters a bound or pass/fail decision.

The separate six-point continuum diagnostic
`scripts/one-sided-hankel/positive-cone-repair-cost-screen.json`
suggested u_*; it is not a proof input. Its initial missing-mpmath
import was replaced by standard-library floating midpoint evaluation,
with that execution failure retained in its history. The exact script
has no dependency on that diagnostic. The certificate verifies the
constants, not the analytic product asymptotic or the logic of (4).
Those arguments are supplied above and remain subject to later audit.

## Mathlib

Full matching coverage of this family-specific strict-action cost has
not been checked; no absence or novelty claim is made. Cauchy--Schwarz,
Fourier orthogonality, Laurent Cauchy coefficient bounds and elementary
logarithmic series are standard supporting inputs. They do not supply
the positive witness or its evaluated quantitative cost by themselves.
