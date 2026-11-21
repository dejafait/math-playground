# Lemma 713: an absolute horizontal contour cannot isolate the proposed spatial residue

## Hypotheses

Fix one actual L703 profile, including its nonnegative even plateau
bump and its width before n varies. Use the COMPLETE L666 family,
with n=12q+3, q>=1, M=n/3, unit masses and the fixed anchor. Put

    d=5/4, R=11/8, U=121/64, A=27/10, Y=9/20, h=A/n,
    u_*=(3+4i)/10=p+i*b, p=3/10, b=2/5,
    a(y)=-d+i*y, y_m=h*(m+1/2+e_m),
    Q_t(u,y)=(d+t*u)*(U*u+d*t-i*t*y)
                         /[(U*u+d*t)*(d+t*u-i*y)],
    W_n(u,y)=product_(j=0)^(n-1) Q_(j/n)(u,y),
    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)].

The j=0 factor is d/(d-i*y), and W_n(u,0)=1. Set c_0=R-d=1/8
and z_0=-1. Its spatial-resolvent pole is y=i*c_0. L708's exact
width and real-frequency conclusions for this same profile give

    delta=2*pi*w in (0,1/3000),
    chi(v)=chi_w(v/(2*pi)),
    supp(chi) intersect (0,infinity) subset [omega-delta,omega+delta],
    0<=chi<=1,  chi(v)=1 if |v-omega|<=delta/2,
    S_e(v)=sum_m [exp(i*v*(m+1/2+e_m))-exp(i*v*(m+1/2))]
          =-chi(v), |v|<3*pi/4,
    |S_e(v)|<=E*|v|, E=sum_m|e_m|<infinity.

For EACH FIXED c>c_0 define the actual signed shifted integral and
its absolute-integral envelope by

    p_n^c(v)=(2*pi*h)^(-1) integral_R
       W_n(u_*,X+i*c)/(c_0-c+i*X)*exp(-i*(X+i*c)*v/h)dX,
    R_n(c)=integral_0^infinity chi(v)*p_n^c(v)dv,
    U_n(c)=(2*pi*h)^(-1) integral_0^infinity chi(v)*exp(c*v/h)
       *integral_R |W_n(u_*,X+i*c)/(c_0-c+i*X)|dX dv,
    P_n=-W_n(u_*,i*c_0)/h
                         *integral_0^infinity chi(v)*exp(c_0*v/h)dv.

These integrals are absolutely convergent for each n,c. P_n is
nonzero, and |R_n(c)|<=U_n(c). U_n is an envelope, NOT the modulus
of the signed remainder. No rate from the i/2 arc is assumed here.

## Conclusion

Along the entire allowed sequence,

    limsup n^(-1)*log|P_n| < 1/5000,
    liminf n^(-1)*log U_n(c) > 7/1000,      every fixed c>1/8,
    liminf n^(-1)*log(U_n(c)/|P_n|) > 17/2500 > 3/500.   (1)

Consequently NO such fixed horizontal line makes this absolute
remainder envelope subdominant to the proposed positive-bump residue.
The triangle-inequality lower certificate based on |P_n|-U_n(c)
is eventually negative, even before the other complete-family terms
are charged. This stops that specific certificate at the nominated
center and boundary point.

It does NOT bound the signed R_n(c) from below, prove cancellation
in it, give an asymptotic for G_n(u_*,-1), or establish either
J_sp=o(n) or a positive lower limit for J_sp/n. It does not exclude
deformed contours, signed integration, other spatial peaks or other
angular centers. No n-dependent choice of c is asserted. The proof
retains an exact expression for every other term, but does not pay
its size. Actual-Xi positivity, amplitude/full charge, H/support and
realization remain independent. This family-specific obstruction was
not supplied by the checked sources; originality is not certified.
The analytic argument has not yet received a separate critical audit.

## Proof

### 1. Source scope and the full signed identity at the new center

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-fixed-profile-spatial-jensen-defect.md`.
Its direct signed-response scope permits this bounded test of the
same defect. The earlier local arc payments and the stopped outer
growth criterion do not imply the present obstruction. No source
search or changed assessment is needed for this attempt.

Reuse the inspected Fourier inputs recorded in L708: J. Kallsen and
P. Kruehner, *On uniqueness of solutions to martingale problems —
counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1), Appendix A,
Lemma A.1(6),(9)–(11),(14), pp.29–30; and the absolutely convergent
exponential transform
[DLMF (1.14.17)–(1.14.18)](https://dlmf.nist.gov/1.14.iii).
We use finite-complex-measure convolution, Fourier inversion with
the stated integrability, and Cauchy's residue theorem on a finite
rectangle. We do not reprove these general results. The new-center
hypotheses and the numerical specializations are checked below;
neither a saddle theorem nor nonreal values of S_e are imported.

At u=u_*, write lambda_t=d+t*u and r_t=t*(d+t*u)/(U*u+d*t).
Then

    Q_t(u,y)=r_t+(1-r_t)*lambda_t/(lambda_t-i*y).

Re lambda_t>=d, and U*u+d*t never vanishes. Each factor is the
Fourier transform of the finite complex measure
r_t*delta_0+(1-r_t)*lambda_t*exp(-lambda_t*v)1_(v>=0)dv.
Their convolution, scaled by h, has finite first absolute moment
and is atom-free because the t=0 factor is an exponential density.
The negative-halfline resolvent at z_0 has density
exp(c_0*v/h)1_(v<=0)/h. Convolving produces a continuous density
p_n with finite first absolute moment. Continuity follows also
directly by moving the endpoint in the convolution integral against
the atom-free measure. The rational transform is

    k_n(y)=W_n(u_*,y)/(c_0+i*y)=O(|y|^(-2)).

Thus Fourier inversion, equivalently its Gaussian regularization
followed by dominated convergence, gives

    p_n(v)=(2*pi*h)^(-1) integral_R k_n(y)*exp(-i*y*v/h)dy.

The Q_t poles are t*Im(u_*)-i*(d+t*Re(u_*)), all below the real
axis. Shifting to height c>c_0 crosses only y=i*c_0. The vertical
integrals vanish because their rational part is O(|Re y|^(-2))
and v,c are fixed. The residue is -i*W_n(u_*,i*c_0)*exp(c_0*v/h).
With the counterclockwise orientation this gives

    p_n(v)=p_n^c(v)+W_n(u_*,i*c_0)*exp(c_0*v/h)/h.       (2)

We use (2) only on the compact positive bump. It is not an estimate
on either infinite frequency tail. In particular the signed R_n(c)
is independent of the fixed choice c>c_0; only its envelope changes.
Equation (2) implies exactly

    -integral_0^infinity chi(v)*p_n(v)dv=P_n-R_n(c).      (3)

Here is the connection to the COMPLETE finite response, without
discarding unestimated terms. Define

    B_n=sum_(m in Z) k_n(h*(m+1/2)),
    V_n=integral_(v<0 or v>=9/4) S_e(v)*p_n(v)dv,
    L_n^-=sum_(m<=-2q-1) k_n(y_m),
    L_n^+=sum_(m>=2q) k_n(y_m),
    T_n=sum_(a in Z_n) W_a(u_*)*(-a/R)^M/(R+a).

Every lattice sum is absolutely convergent by the O(|y|^(-2))
bound. The frequency difference pairing is legitimate because
E*integral |v*p_n(v)|dv is finite. On 0<v<9/4 the only nonzero
correction is the positive bump, since 9/4<3*pi/4 and its support
ends before 543/500. The unshifted comb is kept as B_n; no zero or
nonzero comb sample is silently omitted. The anchor contributes
k_n(0)=1/c_0=8. The exact shifted-minus-unshifted identity and the
finite geometric series therefore yield

    G_n(u_*,-1)=P_n-R_n(c)
                 +[8+B_n+V_n-L_n^--L_n^+-T_n].          (4)

This includes both physical endpoints and all M moments. Nothing
in (1) estimates the square bracket. Bounding R_n by U_n already
prevents a positive |P_n|-U_n lower certificate; making additional
triangle-inequality deductions for the bracket cannot repair it.

### 2. Continuous product rates and complete auxiliary certificates

Let Phi_c(X)=integral_0^1 log|Q_t(u_*,X+i*c)|dt. For D=d+c,

    |Q_t|^2 = [((d+p*t)^2+b^2*t^2)*((U*p+D*t)^2+(U*b-X*t)^2)]
              / [((U*p+d*t)^2+(U*b)^2)*((D+p*t)^2+(b*t-X)^2)]. (5)

All factors are nonzero at the points and intervals used below.
For fixed c>=c_0 and compact real X intervals, uniform Riemann
summation consequently gives

    log|W_n(u_*,X+i*c)|=n*Phi_c(X)+O(1),                (6)

uniformly in X. The O(1) follows from a bounded t derivative on
the compact set. This is a real logarithm of a modulus, with no
branch choice.

The exact certificate proves

    Phi_(1/8)(0)+(omega+1/3000)/(8*A) < 1/5000,
    Phi_(1/8)(-1/5)+omega/(8*A) > 7/1000,
    d/dc [Phi_c(-1/5)+c*omega/A] > 1/100,
                                               all c>=1/8. (7)

For completeness the analytic reduction to every finite check is
as follows. At c=1/8 and X=0 or -1/5, the four affine t factors
in the logarithm of (5) have lower moduli d,U/2,U/2,R and slope
moduli at most 1/2,d,7/5,1/2. For the third lower bound both its
real and imaginary components increase from those of U*u_*.
Differentiating log of an affine factor four times gives the bound

    6*[(1/(2d))^4+(d/(U/2))^4
                       +((7/5)/(U/2))^4+(1/(2R))^4] < 400.

Composite Simpson with N=64 even subintervals has error at most
400/(45*N^4). This conservative bound follows by expanding to
degree three at each two-cell midpoint: the integral and quadrature
remainders total at most 2*K/(45*N^5), and there are N/2 panels.
For rational logarithms use integer-directed rounding at scale 2^100,
40 terms of 2*sum z^(2k+1)/(2k+1), and the full geometric tail;
range reduction puts 0<=z<=1/3. The implementation allows the
larger z<=1/2 tail 8/[3*(81)*2^81]. Arithmetic helper definitions
are read from the existing step-166 script without running it,
and their source hash is stored. The same log enclosure evaluates
the explicit omega. No floating-point number decides a check.

For the third inequality in (7), direct differentiation gives,
at X=-1/5,

    partial_c log|Q_t|
      = t*(U*p+D*t)/[(U*p+D*t)^2+(U*b+t/5)^2]
          -(D+p*t)/[(D+p*t)^2+(b*t+1/5)^2].             (8)

Partition [1/8,3/2] into 176 closed cells and [0,1] into 256
closed cells. On a rectangle t in [l,r], D in [D_l,D_r], all
components are positive, and a LOWER bound for (8) is exactly

    l*(U*p+D_l*l)/[(U*p+D_r*r)^2+(U*b+r/5)^2]
       -(D_r+p*r)/[(D_l+p*l)^2+(b*l+1/5)^2].            (9)

Round each (9) down at scale 2^100, sum with weight 1/256,
and add the lower enclosure for omega/A. This covers all 45056
rectangles, including their boundaries. The minimum resulting
lower bound is greater than 1/100 (its preview is 0.0277666).
For c>=3/2 the first term in (8) is nonnegative and the second
term's modulus is at most 1/(D+p*t)<=1/(d+3/2). Thus the remaining
halfline is paid by

    omega/A-1/(d+3/2)>1/100.

This proves (7) on its full unbounded range; no sampled monotonicity
or untested tail is used. It follows that for every c>=1/8,

    Phi_c(-1/5)+c*omega/A > 7/1000.                    (10)

Reproduce with
`python3 scripts/one-sided-hankel/spatial-boundary-peak-rates-173.py`.
The full certificate is
`scripts/one-sided-hankel/spatial-boundary-peak-rates-173.json`.
All seven exact comparisons pass. The script stores every cell
lower bound and the complete rate intervals, with actual/required
bounds and an empty failures list. The earlier
`scripts/one-sided-hankel/spatial-boundary-peak-diagnostic-173.json`
is a floating-point screen only and supplies no proof evidence.

### 3. Compare the residue with its absolute contour envelope

Positivity and fixed compact support of chi give

    0<integral_0^infinity chi(v)*exp(c_0*v/h)dv
                           <=2*delta*exp(c_0*(omega+delta)/h).

The factor W_n(u_*,i*c_0) is nonzero by (5). Equation (6) at
X=0, the bound delta<1/3000, and the first strict bound in (7)
prove the first inequality of (1). The factor 1/h costs only
O(log n) after taking logarithms. No lower transform bound or
choice of support endpoint is needed.

Now fix ANY c>c_0 and epsilon>0. By continuity choose a small
fixed real interval J about -1/5 such that
Phi_c(X)>=Phi_c(-1/5)-epsilon on J. The resolvent denominator
|c_0-c+i*X| is bounded above and bounded away from zero there.
Use (6) and restrict U_n(c) to X in J and
v in [omega,omega+delta/2], where chi=1. This gives

    U_n(c)>=C_(c,epsilon)*h^(-1)
       *exp(n*[Phi_c(-1/5)+c*omega/A-epsilon]),          (11)

with C_(c,epsilon)>0 independent of n. The entire double integral
is nonnegative, so restricting it is valid. Its finiteness follows
from the O(|X|^(-2)) rational decay and compact frequency support.
Taking a lower limit, then letting epsilon decrease to zero,
proves the second bound in (1) by (10). Subtract the upper limit
for log|P_n| to obtain the third bound. All limits are for the
same fixed actual profile, and c is chosen before n.

An exponentially large envelope is not an exponentially large
signed integral. Equation (4) makes the precise limitation visible:
only this absolute-integral certificate has failed. A future signed
analysis would have to evaluate R_n itself and the other terms,
and any averaged-defect conclusion would still need angular and
spatial positive-measure control. This proof supplies none of those
unproved extensions and makes no RH claim.

## Mathlib

Full matching coverage is not checked. No formalization is claimed
for the actual profile, the signed contour identity, the exact rate
certificate or its fixed-c asymptotic comparison. Standard convolution,
residue and Riemann-sum support would not by itself establish (1).
