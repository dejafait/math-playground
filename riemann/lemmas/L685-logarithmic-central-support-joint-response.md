# Lemma 685: a quantitative arc bound permits logarithmically growing central support

## Hypotheses

Use L666's exact family with integer q>=1, n=12q+3, M=n/3,
x=-d=-5/4, R=11/8, U=121/64, alpha=27/10 and t_j=j/n:

    Z_e={x} union {x+i*(alpha/n)*(m+1/2+e_m): -2q<=m<2q},
    e_m real, |e_m|<=1/8,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    F_(n,e)(u,z)=sum_(a in Z_e) W_a(u)/(R-a*z),
    V_(n,e)=max_(|u|=|zeta|=1) |F_(n,e)(u,zeta/32)|,
    D_(n,e)=mean_(|u|=1) sum_(a in Z_e) |W_a(u)|^2/(U-|a|^2).

The mean is normalized. All residues remain one, every product factor
including j=0 remains, and the same displacement vector is used at all
angles. Let L be an integer with 1<=L<=2q and impose only

    e_m=0 outside -L<=m<L.                              (1)

The remaining 2L displacements are independent, without symmetry.
Unlike L684, L is allowed to depend on n.

## Conclusion

For every admissible n and L satisfying

    n>=ceil(exp(4000)),      L<=log(n)/4000,             (2)

uniformly over all vectors in (1),

    V_(n,e) >= (64/181)*exp(-1500*L)
             >= (64/181)*n^(-3/8).                     (3)

With sigma^2=137/5000, the original diagonal satisfies

    V_(n,e)/[n*exp(-n/48)*sqrt(D_(n,e))]
       >= (64/181)*sqrt(3*sigma^2)*exp(-3)
                     *n^(-15/8)*exp(79*n/30000) > 1.   (4)

Thus the approved norm bound holds with c=1 and one absolute onset
on this growing-support subfamily. The onset is deliberately very
large and is not claimed optimal. The full cube permits L=2q~n/6;
(2) does not cover it. No full-cube lower bound or countersequence,
H/support result, actual-Xi realization, mixed-sign theorem or RH
candidate is claimed. This proof and the inherited L684 approximation
have not received a separate critical audit.

The quantitative input replacing L684's compactness argument is

    mu_L >= exp(-1500*L),       L>=1,                   (5)

where mu_L is its minimum of the limiting response on the fixed arc.
This is an elementary interpolation specialization within the approved
EXPLORE target, not certified originality beyond the sources checked.

## Proof

### 1. Scope, prior inputs and the cost that must be paid

Reuse the unchanged ready assessment
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
L669's audited fixed-angle cancellation allows order-dependent support
and onset; it does not exclude escape on a fixed angular arc. L682's
highest-moment stop, L649/L650's inverse/individual-dual stops and
L666's parked scalar-flow estimate are comparisons, not lower-bound
premises. The earlier fixed-angle and signed-angular source comparisons
supply no matching original-D estimate. No further source search or
novelty claim is made in this mathematical step.

Use L684's equations (9), (14)--(15), including their explicit constants,
not a uniform-in-L interpretation of its compactness limit. Put
r=1/32, delta=1/90000 and

    kappa(u)=alpha*integral_0^1
                   [1/(d+v*u)-v/(U*u+d*v)] dv,
    w(theta)=kappa(-exp(i*theta)),        |theta|<=delta,
    tau_m=m+1/2,
    Phi_e(w)=1+sum_(m=-L)^(L-1)
                  [exp(i*w*(tau_m+e_m))-exp(i*w*tau_m)],
    mu_L=min_e max_(|theta|<=delta) |Phi_e(w(theta))|.

The minimum is over the compact cube [-1/8,1/8]^(2L), as in L684.
For |u|=1 every allowed real frequency t satisfies |t|<=L. In particular
Phi_e is entire, Phi_e(0)=1, and

    |Phi_e(w)| <= (4*L+1)*exp(L*|w|).                   (6)

L684 proves |kappa(u)|<=6*alpha<17 for |u|=1. Its finite-n bound,
valid uniformly in e, |theta|<=delta and |z|<=r, is

    |F_(n,e)(u,z)-Phi_e(kappa(u))/(R-x*z)|
       <= epsilon_L(n)
        =1000*n*exp(-n/6000)+4*L*J_L/n,                (7)

provided n>=183, n>=8*alpha*L, n>=A_L and L<=2q, where

    A_L=20*alpha^2*L^2+(21/2)*alpha*L,
    E_L=A_L*exp(6*alpha*L+1),
    C_0=1/[R*(1-r)],
    C_1,L=r*alpha*L/[R^2*(1-r)^2],
    J_L=C_0*E_L+exp(6*alpha*L)*C_1,L.

These are finite inequalities for every eligible pair (n,L), so they
may be used for growing L once their onsets and errors are paid. No
fixed-L limit is interchanged with a growing-dimensional minimum.
The original family is admissible by L666, so D is finite and positive.

For the interpolation below import the standard residue theorem in
R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
already inspected in the L664/L684 source records. Its application is
to a finite circle with explicitly listed simple poles and an entire
numerator. The residue computation is included to fix the constants
and complex observation geometry; no general interpolation, Turan or
rational-sampling theorem is reproved or assumed.

### 2. Quantitative separation of the phase arc

The defining integrand is holomorphic on d/U<|u|<d, with denominators
uniformly nonzero on compact subannuli. Differentiation under its finite
integral is justified there as in L684. On |u|=1,

    |kappa'(u)|
      <= (alpha/2)*[1/(d-1)^2+U/(U-d)^2]
       = (27/20)*(16+7744/1681) < 30,
    |kappa''(u)|
      <= alpha*[2/(3*(d-1)^3)+U^2/(U-d)^3]
       = (27/10)*(128/3+937024/68921) < 170.            (8)

For the last two comparisons, 7744/1681<5 and 937024/68921<14
suffice. The derivatives follow by differentiating the two summands;
the factors integral_0^1 v dv=1/2 and integral_0^1 v^2 dv=1/3
are retained. Consequently |w''(theta)|<200.

At u=-1, put A=d-v and B=U-d*v, both positive on [0,1]. Then

    -kappa'(-1)=alpha*integral_0^1 v*(1/A^2-U/B^2) dv.

The bracket is positive because B-R*A=(R-d)*(R+v)>0. For
3/4<=v<=1, specifically,

    B-R*A>=17/64,       B+R*A>=63/64,
    A^2*B^2 <= (1/4)*(61/64)^2,
    1/A^2-U/B^2 >= 4284/3721 > 1.

It follows that -kappa'(-1)>alpha*(7/32)=189/320>1/2.
Since w'(0)=-i*kappa'(-1), equations (8) give

    Im w'(theta) >= 1/2-200*delta > 1/4.

Integrating this real inequality between any two arc parameters yields

    |w(theta)-w(phi)| >= |theta-phi|/4.                 (9)

Thus these observation points have a controlled projection separation;
nonconstancy alone is not used as a quantitative estimate.

### 3. A finite residue interpolation bounds the minimum

Fix any e in the cube and write f=Phi_e. Take N=80*L equally spaced
parameters theta_j=-delta+2*delta*j/(N-1), 0<=j<N, and put
w_j=w(theta_j). All |w_j|<17. By (9) they are distinct and

    |w_j-w_k| >= s_* |j-k|,    s_*=delta/[2*(N-1)].     (10)

If some w_j=0, then the arc maximum is at least |f(0)|=1 and the
required bound follows immediately. Otherwise define

    p(w)=product_(j=0)^(N-1)(w-w_j),
    ell_j(0)=product_(k!=j)(-w_k)/(w_j-w_k).

On the positively oriented circle |w|=68, the integrand
f(w)*p(0)/[w*p(w)] has precisely the simple poles 0,w_0,...,w_(N-1)
inside, and no boundary poles. Their residues are f(0) and
-f(w_j)*ell_j(0), respectively. Hence

    f(0)-sum_j f(w_j)*ell_j(0)
      =(1/(2*pi*i))*integral_(|w|=68) f(w)*p(0)/[w*p(w)] dw.
                                                               (11)

Using (6), |w_j|<17 and |w-w_j|>51, the absolute value of (11) is
at most

    (4*L+1)*exp(68*L)*3^(-80*L)
      < (4*L+1)*exp(-12*L) < 1/2.                    (12)

Here exp(1)<3, and 4L+1<=5^L for integer L>=1 by induction;
exp(12)>2^12 makes the last comparison immediate. The contour
length cancels the factor |w|=68 in (11). No derivative remainder
for nonreal interpolation nodes is being assumed.

On the other hand, (10) gives

    sum_j |ell_j(0)|
      <= (17/s_*)^(N-1)*sum_(j=0)^(N-1) 1/[j!*(N-1-j)!]
       = [68*(N-1)/delta]^(N-1)/(N-1)!
      <= (68*exp(1)/delta)^(N-1)
       < B_*^(N-1),             B_*=204/delta=18360000. (13)

The factorial inequality m!>=(m/exp(1))^m follows by summing log k
and comparing with integral_1^m log t dt; here m=N-1>=79. The
binomial sum in (13) is exactly 2^(N-1)/(N-1)!. Since f(0)=1,
(11)--(13) imply

    max_(|theta|<=delta) |f(w(theta))|
                         >= 1/[2*B_*^(80*L-1)].        (14)

For an explicit simple exponential, exp(1)>8/3 follows from its
positive series, so exp(3)>18 and
exp(18)>18^6=34012224>B_*. Also log 2<1. Therefore the right
side of (14) exceeds exp(-1440*L+17), and in particular exceeds
exp(-1500*L). This bound is independent of e, proving (5).
It controls a maximum over the fixed arc, not a common good angle
for every displacement vector.

### 4. The full error is paid for growing support

For L>=1 the explicit constants in (7) satisfy

    A_L<175*L^2,     C_0<1,     C_1,L<L,
    J_L<600*L^2*exp(17*L).                              (15)

Indeed 20*alpha^2+(21/2)*alpha=174.15<175;
E_L<525*L^2*exp(6*alpha*L) since exp(1)<3, and
6*alpha=16.2<17. The remaining summand in J_L is bounded by
L*exp(6*alpha*L), so 526<600 pays it.

Let s=log n>=4000 and L<=s/4000. The onsets for (7) hold:
8*alpha*L<s<=exp(s)=n, and
A_L<175*s^2/4000^2<s^2/2<=exp(s)=n; also n>=183.
The condition L<=2q remains in the hypotheses. From (7) and (15),

    exp(1500*L)*epsilon_L(n)
      <= 1000*exp((11/8)*s-exp(s)/6000)
         +2400*(s/4000)^3*exp(-2483*s/4000) < 1/4.     (16)

For completeness, each summand is less than 1/8 for all s>=4000.
The second decreases there because its logarithmic derivative is
3/s-2483/4000<0. At s=4000 it is 2400*exp(-2483)<1/8,
using exp(1)>2 and 2^15>19200. The first also decreases there:
its logarithmic derivative is 11/8-exp(s)/6000<0. The positive
exponential series gives exp(4000)>=4000^3/6>36000000, so at
s=4000 its exponent is less than 5500-6000=-500. Thus it is
less than 1000*exp(-500)<1/8, since 2^13>8000. This proves
(16) on the complete half-line, not just at the stated onset.

At the permitted spatial boundary point z=r, put
A_*=R+d*r=181/128<2. Using (5), (7) and (16),

    V_(n,e) >= max_(|theta|<=delta) |F_(n,e)(-exp(i*theta),r)|
             >= mu_L/A_*-epsilon_L(n)
             >= exp(-1500*L)/(2*A_*)
              = (64/181)*exp(-1500*L).

In the last step, 1/4<1/(2*A_*) pays the error in (16).
Finally exp(-1500*L)>=exp(-3*s/8)=n^(-3/8), proving (3).

### 5. Comparison with the original diagonal and scope

Apply L661's audited envelope (3) to this L666-admissible family.
There are M=n/3 original unit residues, so with kappa_env=91/5000,

    D_(n,e)<=n*exp(2*kappa_env*n+6)/(3*sigma^2).

The exact rate difference is 1/48-kappa_env=79/30000. Combining
this bound with (3) proves the non-strict inequality in (4).
To verify its final strict inequality at the same absolute onset,
its constant exceeds 1/324: use 64/181>1/3,
sqrt(3*sigma^2)>1/4 and exp(-3)>1/27. For s=log n>=4000,

    (79/30000)*n-(15/8)*log n
       > exp(s)/400-2*s
      >= s^2/800-2*s >= 12000.

The last quadratic is increasing on this half-line and takes the
value 12000 at 4000. Since exp(12000)>324, (4) is strictly greater
than one. These bounds preserve the defining D rather than replacing
it with the anchor or a positive surrogate for the signed response.

This pays all errors uniformly for the explicitly growing support
in (2). For L proportional to n, (7) and (15) do not make the error
smaller than (5); the present certificate therefore does not extend
to the full cube. This failure of the available comparison is not an
upper bound for the actual response or a counterexample to the norm
target. Sharpening fixed numerical constants alone does not remove
its 1/n approximation barrier. No conclusion contradicts L669's
fixed-angle cancellation or the recorded scalar and highest-moment
stops. L683 is only a possible downstream transfer, remains unaudited,
and is not a premise of this proof. H/support, realization and actual
Xi signs remain independent unresolved questions.

## Mathlib

Full matching coverage of the quantitative phase-arc interpolation,
this growing-support family and its original-D norm comparison has
not been checked. The supporting mathematics is the residue theorem,
elementary differentiation under a uniformly holomorphic finite
integral, finite interpolation and exponential/factorial inequalities.
No specific Lean theorem or formalization is claimed. L684/L661 retain
their existing coverage and audit qualifications; unknown full coverage
is not evidence of absence. No numerical experiment or mathematical
script is a premise of the proof.
