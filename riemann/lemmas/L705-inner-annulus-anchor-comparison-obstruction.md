# Lemma 705: the anchor cannot dominate the complete inner-annulus contours

## Hypotheses

Fix one actual L703 profile e before n. Use L666's exact family and
L657's complete K,Q, with

    n=12q+3, q>=1, M=n/3, J=n-1, h=A/n,
    d=5/4, x=-d, R=11/8, U=121/64, A=27/10, Y=9/20,
    a_m=x+i*h*(m+1/2+e_m), -2q<=m<2q,
    T_M(v)=sum_(k=0)^(M-1) v^k,
    G_n(u,z)=R^(-1)*[T_M(x*z/R)+sum_m W_(a_m)(u)*T_M(a_m*z/R)].

Retain the anchor, unit masses, j=0 factor, inverse denominator angle,
both endpoints and every spatial moment. The profile properties used
below are |e_m|<=1/8 and e_m->0 as |m|->infinity, supplied by L703.
Neither reflection nor an approximation to the Picard solution is used.
Put

    A_n(z)=T_M(x*z/R)/R, V_n(u,z)=G_n(u,z)-A_n(z),
    K_0(u,z)=Q(u)*A_n(z), r0=1/4, r1=1/2.

All spatial and angular means are normalized. For either r in {r0,r1},
define, with an integrable logarithmic singularity at t=U*r/d,

    Phi_r(y)=integral_0^1 {log|(d-t*r)/(d-t*r-i*y)|
                 +log|(d*t-U*r-i*t*y)/(d*t-U*r)|}dt,
                                       0<=y<=Y.             (1)

The value at y=0 is zero. These fixed rational radii have no angular
denominator pole on their circles: U*r*n/d is respectively 121n/320
or 121n/160, never an integer because n is odd.

## Conclusion

For either of these two radii, with the same fixed actual profile,

    mean_(|z|=1) log|V_n(-r,z)|=n*Phi_r(Y)+O(log n),
    mean_(|z|=1) log|G_n(-r,z)|=n*Phi_r(Y)+O(log n),
    Phi_r(Y)>3/40.                                         (2)

The means are finite for all sufficiently large allowed n. Constants
and onset may depend on the fixed profile. In contrast,

    mean_(|z|=1) log|A_n(z)|=-log R.                        (3)

Consequently, for every sufficiently large n, a nonempty open set of
spatial points on |z|=1 violates

    |K(-r,z)-K_0(-r,z)|<|K_0(-r,z)|.                       (4)

Thus the proposed uniform anchor Rouche comparison fails on BOTH
complete comparison contours |u|=1/4 and |u|=1/2. This is an
informative obstruction to that sufficient nested-radius mechanism
for the actual profile, not a counterexample to Z_n^(1/2)>=P_n^(1/2)-o(n).
No angular logarithmic lower bound, reduction of the inner-charge
deficit, zero-pairing assertion, H/support bound or Xi realization is
proved. An alternative comparison retaining the endpoint terms is
not excluded. The separate conceptual audit in Section 6 accepts this
local specialization and its restricted obstruction; no originality
beyond the inspected sources is claimed.

## Proof

### 1. Approved comparison, source imports and the unpaid signed term

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-gevrey-inner-disk-complete-charge-scope.md`.
The attempt tests its signed nested-radius comparison for the full
fixed-profile family. L704's partial payment is preserved, not rescaled
or optimized. L700/L701's scalar stops and L702's unit-circle endpoint
stop are contrasts, not premises at these different radii. The
endpoint summation method resembles L701; its moving microscopic
coordinate and scalar subsequence conclusion are not imported here.

Import the complete polynomial root formula, including boundary roots,
from F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, [Propositions 1.4-1.5, pp.6-7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
For product logarithmic integrability use Z. Issa and M. Lalin,
*A generalization of a theorem of Boyd and Lawton*,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, p.7](https://arxiv.org/pdf/1203.5379v1),
s=1, as already specialized in L657. No degree-uniform continuity or
small-value constant is imported.

Use Poisson--Jensen for analytic functions with boundary zeros from
R. B. Ash and W. P. Novinger, *Complex Variables*,
[Theorem 4.8.3 and Lemma 4.8.4, printed pp.33-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
with kernel mass one from Corollary 4.7.4, printed p.27. The saved
step-149 assessment inspected these exact boundary cases; the
evaluation here is real, 0 or 1/2, within the recorded symmetry
qualification. These are imported theorems, not reproved results.

The usual sufficient anchor-dominance condition is discussed in
J. H. Mathews and R. W. Howell, *Complex Analysis*,
[Section 8.7, Remark 8.7.13 following Theorem 8.7.11 and Corollary 8.7.12](https://complexanalysis.org/web/sec_argument-rouche.html),
already inspected in the source assessment. The theorem's symmetric
strict condition is broader. We show only the proposed condition
|K-K_0|<|K_0| fails; we neither refute every Rouche comparison nor
apply the theorem to obtain a zero count.

For context, the root formula at any 0<r<d gives exactly

    A(r):=mean_(|u|=r,|z|=1) log|G_n(u,z)|
                          =m_0+Z_n^(r)-P_n^(r).           (5)

Indeed K(r*v,z) is a nonzero polynomial and Q(r*v) has integrable
logarithm; all A_b factors of Q have zeros outside |u|<d. The finite
spatial set where K(0,z)=0 is omitted only from the almost-everywhere
root identity. Boundary factors have zero weight, cancelled factors
remain in K and Q, and the cited absolute integrability justifies
Fubini. For r0<r1 the same identity becomes

    A(r1)-A(r0)=integral_(r0)^(r1)
                    [mean_z N_K(t,z)-N_P(t)]dt/t,          (6)

where N_K counts ALL K zeros in |u|<t with multiplicity and
N_P(t)=#{1<=j<n: d*j/(U*n)<t}. Formula (6) follows root by root from
logarithmic weights and Tonelli for the nonnegative zero-count
increment, followed by subtraction of the finite pole integral.
Boundary radii do not affect this integral. Numerator monotonicity
alone leaves the pole increment unpaid. Equations (5)-(6) are known
accounting, not a new lower bound or the claimed outcome of this step.

The proposed stronger test was to compare K to K_0 on nested circles.
K_0 has exactly the Q zeros for each |z|=1, since A_n never vanishes
there. Strict domination would compare unweighted counts on the tested
circles; more radial information would still be needed for charge.
We now disprove the uniform domination premise itself.

### 2. Strict growth of the actual negative-radius endpoint modulus

For real y, L666's exact continuation gives

    W_(r,n)(y):=W_(x+i*y)(-r)
       =d/(d-i*y)*product_(j=1)^J
          [(d-t_j*r)/(d-t_j*r-i*y)]
          *[(d*t_j-U*r-i*t_j*y)/(d*t_j-U*r)].              (7)

All denominators are nonzero at these radii and real y. For y>0
all numerators are nonzero as well. Also W_(r,n)(-y) is the
complex conjugate of W_(r,n)(y).

Differentiating the integral (1) for y>0 yields

    Phi'_r(y)=integral_0^1
        [y/((d-U*r/t)^2+y^2)-y/((d-t*r)^2+y^2)]dt.         (8)

At t=0 the first integrand is defined by its zero limit. Differentiation
is justified on every compact positive y interval because the original
numerator modulus has no zeros there; the denominator logarithm is
independent of y. Set c=U*r and a=d-c>0. Under v=d-c/t the first
integral has weight c/(d-v)^2 on -infinity<v<=a. Its portion on
[-a,a] is at least

    (2*c/d^2)*integral_0^a y/(v^2+y^2)dv
                         =(2*c/d^2)*arctan(a/y).          (9)

Here (d-v)^(-2)+(d+v)^(-2)>=2/d^2 for 0<=v<=a<d,
by convexity or direct multiplication. The subtracted integral in
(8) is at most y*integral_0^1(d-t*r)^(-2)dt
=y/[d*(d-r)]. Therefore, for 0<y<=Y,

    Phi'_r(y)>=(2*U*r/d^2)*arctan((d-U*r)/Y)
                                      -Y/[d*(d-r)].      (10)

The required strict rational margins need no numerical approximation:

* For r=1/4, (d-U*r)/Y=995/576. Since pi>3 and 576/995<3/5,
  arctan(995/576)=pi/2-arctan(576/995)>9/10. The right side
  of (10) exceeds (121/200)*(9/10)-9/25=369/2000>1/6.
* For r=1/2, (d-U*r)/Y=65/96 lies strictly between 2/3 and
  7/10. The integral of 1/(1+t^2)>=1-t^2 gives
  arctan(65/96)>2/3-(7/10)^3/3=1657/3000. Hence (10)
  exceeds (121/100)*(1657/3000)-12/25
  =56497/300000>1/6.

The function Phi_r is continuous at zero. In (1) the only issue is
the logarithm near t=c/d; its nonnegative numerator change is bounded
by C+log(1+C/|t-c/d|), an integrable function, and tends pointwise
to zero. The other factors are uniformly continuous. Consequently

    Phi_r(y2)-Phi_r(y1)>=(y2-y1)/6,
                         0<=y1<=y2<=Y,                  (11)

with strict inequality for distinct endpoints. In particular
Phi_r(Y)>Y/6=3/40.

### 3. Uniform product estimates and both actual endpoint sums

We need estimates for the finite products, not merely (1).
Uniformly for 3*A/(8*n)<=y<=Y, elementary Riemann comparison gives

    log|W_(r,n)(y)|=n*Phi_r(y)+O(log n).                  (12)

Here is the uniformity at the small ordinate and angular pole. The
first product logarithm in (7) and its t derivative are uniformly
bounded because d-t*r>=d-r>0. For the second numerator, its squared
modulus is

    (d*t-c)^2+y^2*t^2,
    min_(t in R) [(d*t-c)^2+y^2*t^2]=c^2*y^2/(d^2+y^2).

Thus its logarithm is bounded below by -C-log n in the stated
y range, is bounded above, and has at most one turning point in t.
Its total variation is O(log n); cellwise Riemann comparison has
sum error bounded by this variation and endpoint terms, hence
O(log n). For log|d*t-c| exclude the at most two cells adjacent
to c/d. The distance |j/n-c/d| is at least 1/(320n) or 1/(160n).
The excluded sampled terms and n times their absolute integrals are
O(log n). On the remaining intervals monotonic comparison gives the
same error. Finally log|d/(d-i*y)| is bounded. These facts prove
(12), including y=Y and every actual nonzero ordinate. No uncontrolled
Riemann sum across a pole has been used.

On Y/2<=y<=Y logarithmic differentiation of (7) gives, uniformly,

    n^(-1)*W'_(r,n)(y)/W_(r,n)(y) -> L_r(y),
    L_r(y)=integral_0^1 [i/(d-t*r-i*y)
                         -i*t/(d*t-c-i*t*y)]dt,
    Re L_r(y)=Phi'_r(y)>1/6.                             (13)

The integrands and their t derivatives are uniformly bounded here,
so the first convergence has error O(1/n). The j=0 derivative is
O(1/n) after normalization. In particular, eventually
d log|W_(r,n)(y)|/dy>=n/12 on this whole interval.
Let

    lambda_r=L_r(Y), z_r=exp(-A*lambda_r),
    b_r=z_r/(1-z_r), a_+=x+i*Y, a_-=x-i*Y.

Then |z_r|<1 and b_r!=0. No phase limit for W_(r,n)(Y) is needed.

Count the positive nodes from the outer endpoint by k=2q-1-m.
Their exact ordinates are

    y_(n,k)^+=Y-A*(k+1)/n+A*e_(2q-1-k)/n,
                                      0<=k<2q.          (14)

The absolute ordinates of the negative nodes, indexed by m=-2q+k,
are

    y_(n,k)^-=Y-A*(k+1)/n-A*e_(-2q+k)/n.                 (15)

For each fixed k, n*(y_(n,k)^+/- -Y)->-A*(k+1), because the
fixed profile tends to zero at both ends. Integrating (13) along
the segment from Y to that ordinate, without selecting a logarithm
across a zero, proves

    W_(r,n)(y_(n,k)^+)/W_(r,n)(Y)->z_r^(k+1),
    W_(r,n)(-y_(n,k)^-)/conjugate(W_(r,n)(Y))
                                  ->conjugate(z_r)^(k+1). (16)

For y_(n,k)^+/- >=Y/2, the derivative bound following (13) and
Y-y_(n,k)^+/- >=A*(k+7/8)/n give the summable majorant

    |W_(r,n)(+/-y_(n,k)^+/-)|/|W_(r,n)(Y)|
                         <=exp[-A*(k+7/8)/12].           (17)

For the remaining nodes, (11)-(12) bound the ratio by
n^C*exp(-n*Y/12). Their total is at most n times this quantity and
tends to zero. This split justifies first summing (16) over a fixed
initial block and then letting the block grow; it does not exchange
an uncontrolled signed limit and a growing sum.

All actual nodes satisfy |a_m|<=sqrt(d^2+Y^2)<R. Thus T_M(a_m*z/R)
is uniformly bounded for |z|<=1. For each fixed endpoint index k it
converges uniformly on this disk to (1-a_+*z/R)^(-1) on the positive
side, and to (1-a_-*z/R)^(-1) on the negative side. The geometric
remainder and these limits retain every M=n/3 moment. Equations
(16)-(17) and the interior bound therefore imply, uniformly for
|z|<=1,

    V_n(-r,z)/|W_(r,n)(Y)| = H_(theta_n)(z)+o(1),
    H_theta(z)=R^(-1)*[b_r*exp(i*theta)/(1-a_+*z/R)
                +conjugate(b_r)*exp(-i*theta)/(1-a_-*z/R)],
    exp(i*theta_n)=W_(r,n)(Y)/|W_(r,n)(Y)|.               (18)

The anchor A_n is uniformly bounded on this spatial disk and
|W_(r,n)(Y)|=exp(n*Phi_r(Y)+O(log n)) tends to infinity.
Consequently (18) holds for G_n as well. Both signed endpoint
amplitudes are retained. Exact reflection of the shifted finite
family is unnecessary: the two endpoint limits follow separately
from (14)-(15).

### 4. Paying the whole spatial logarithm despite endpoint cancellation

Neither scalar value in (18) is assumed nonzero for every phase.
Write B=b_r*exp(i*theta)=s+i*t. The numerator of R*H_theta,
after multiplying its two displayed denominators, is

    2*s+2*(d*s-Y*t)*z/R.                                (19)

If H_theta(0)=H_theta(1/2)=0, (19) gives s=t=0, contradicting
|B|=|b_r|>0. The denominators have no zeros on |z|<=1.
By compactness of theta modulo 2*pi there are c_r>0 and C_r>=1
such that

    max{|H_theta(0)|,|H_theta(1/2)|}>=c_r,
    sup_(|z|<=1)|H_theta(z)|<=C_r                         (20)

for every theta. These constants are independent of n and its phase.

Let F_n denote either normalized polynomial in (18), using V_n or
G_n. Uniform convergence in (18) gives, eventually, sup|F_n|<=C_r+1
on the spatial disk and max{|F_n(0)|,|F_n(1/2)|}>=c_r/2. In
particular F_n is nonzero and its boundary logarithm is integrable.
If the first value is at least c_r/2, ordinary Jensen yields
mean log|F_n|>=log(c_r/2). Otherwise apply the cited Poisson--Jensen
inequality at the real point 1/2. Its unit-disk Poisson kernel has
mass one and minimum 1/3. Subtracting this minimum and using the
upper bound log(C_r+1) on the whole boundary gives

    log|F_n(1/2)| <= (1/3)*mean log|F_n|
                                     +(2/3)*log(C_r+1).

Hence in this case

    mean log|F_n|>=3*log(c_r/2)-2*log(C_r+1).             (21)

The upper bound is log(C_r+1). Boundary zeros are allowed by the
imported theorem; no spatial exceptional set is discarded and no
degree-uniform small-value estimate is assumed. Equations (12) and
(21) prove both full spatial statements in (2).

Finally T_M(x*z/R) has constant coefficient 1 and all its zeros have
modulus R/d>1 (M>=5). The root formula proves (3) exactly. If
|V_n(-r,z)|<=|A_n(z)| held almost everywhere on the spatial circle,
integrating logarithms would contradict (2)-(3) for large n. Thus
strict reverse inequality holds at some point, and by continuity
on a nonempty open set. Q(-r)!=0 because its C_x roots avoid this
radius and all its A_b roots are exterior. Multiplication by Q
therefore gives the violation (4), without deleting cancelled factors.

### 5. Scope of the negative outcome

This failure concerns a complete comparison contour and a positive-
measure spatial set for the same actual fixed profile. It is not
based on a favorable scalar sample, a numerical Picard approximation,
or the old microscopic pole pairing obstruction. The required inner
charge is still P_n^(1/2)-o(n), with P_n^(1/2)/n->121/160; no new
lower bound on that charge is obtained here. The retained signed
endpoint terms could contribute favorably to compensation, but (2)
concerns negative-real angular points, not their angular integral.
Controlling transition regions and singular logarithms in a different
comparison remains necessary. This stops uniform anchor domination,
not the aggregate route or RH research.

No mathematical script is needed: the two derivative margins are
369/2000>1/6 and 56497/300000>1/6, and the resulting exponent threshold
is Y/6=3/40. All other estimates are analytic and asymptotic. The
argument and existential-onset qualifications are accepted by the
separate critical review below; no effective onset is obtained.

### 6. Separate conceptual audit — 3 November 2026, step 153

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-03-inner-annulus-anchor-obstruction-audit-scope.md`.
This is the first separate audit of (2)--(4). It reuses the primary
theorem readings recorded there and checks their local applications;
it is not an independent audit of every source manuscript. No new
profile, stronger charge, symmetry, simple-root hypothesis or numerical
certificate is introduced.

**Exact inputs and pole avoidance.** L666 (6), evaluated at u=-r
and a=-d+i*y, gives (7) directly: x/a=d/(d-i*y), the first ratio
is (d-t_j*r)/(d-t_j*r-i*y), and the second ratio is
(d*t_j-U*r-i*t_j*y)/(d*t_j-U*r). This checks both the j=0 factor
and the inverse denominator angle. The second denominator vanishes
only if j=(121/320)n or j=(121/160)n. Both fractions are reduced
and n=12q+3 is odd, so neither is an integer. In particular the
grid distance to c/d is at least 1/(320n) or 1/(160n), respectively.
The A_b factors in L657's complete Q have all roots of modulus
|b|/t_j>d; C_x has precisely the j=1,...,n-1 roots p_j.
Thus the tested circles contain no Q boundary zero, and Q(-r)!=0.
The counted pole range in (6) has been made explicit above.

L703 is used only for one real profile fixed before n, its cap and
decay at both ends. Its weighted summability implies that decay; its
Fourier gap, reflection properties and iteration rate are not used.
The cap gives nonzero ordinates of magnitude at least 3A/(8n).
All node moduli are at most sqrt(d^2+Y^2), strictly below R because
R^2-d^2-Y^2=201/1600. This verifies the full spatial geometric bound
without discarding any of the M=n/3 moments. L701 and L704 supply
comparisons only, not mathematical premises of this audit.

**Derivative, rational margins and the singular Riemann comparison.**
For y bounded away from zero the two differentiated logarithms give
(8), with the stated signs. The substitution v=d-c/t has derivative
dt/dv=c/(d-v)^2 and range (-infinity,d-c]; here 0<d-c<d.
Restriction to the symmetric interval [-(d-c),d-c] therefore gives
the positive lower bound in (9). The removed denominator contribution
is at most y/[d(d-r)]. The two rational lower bounds in (10) exceed
1/6 by 107/6000 and 6497/300000, respectively. They are uniform
for 0<y<=Y. Near t=c/d, the only new positive logarithm is
one half of log(1+t^2*y^2/(d*t-c)^2); the integrable majorant
stated in Section 2 permits y down to zero. Thus (11), its strict
endpoint version and Phi_r(Y)>3/40 are justified.

For (12), set f_y(t)=log|d*t-c-i*t*y|. On
3A/(8n)<=y<=Y its maximum is bounded, its minimum is at least
-log n-C, and its derivative changes sign at most once. Hence its
total variation on [0,1] is O(log n), uniformly in y. Comparing
each grid value to the integral over its grid cell bounds the
unscaled sum error by this variation, together with bounded endpoint
terms. For f_0(t)=log|d*t-c|, delete the cell or adjacent cells
meeting c/d. Their sampled logarithms are O(log n) by the rational
distance bound; n times their absolute integrals is O(log n).
On each remaining side monotonicity bounds the sum error by the
endpoint variations, again O(log n). The first ratio in (7) has
uniformly bounded variation, and its j=0 factor has bounded logarithm.
This proves the required n-uniform estimate, including at every
actual node; a smooth Riemann estimate through the pole is not used.

**Complex phases and independent endpoints.** On [Y/2,Y] every
denominator in the integrand of L_r and in its t derivative is
bounded away from zero, uniformly in t. At t=0 the second one is
-c, and elsewhere its imaginary part excludes a zero. Ordinary
Riemann comparison and the bounded j=0 derivative therefore give
W'/W=n*L_r+O(1), uniformly there, with Re L_r=Phi'_r>1/6.
The eventual n/12 modulus derivative bound follows. Integrating this
logarithmic derivative along a real y segment is legitimate because
W has no zero on it; the exponential of the integral is the ratio
of endpoint values and requires no global logarithm choice.

The exact equality nY/A=2q+1/2 verifies (14)--(15). Their distances
from Y are A(k+1-e_(2q-1-k))/n and A(k+1+e_(-2q+k))/n.
For fixed k, the two indices tend separately to opposite infinities,
so both shifts tend to zero. The positive limit is
exp(-A*lambda_r*(k+1)); conjugation of the exact product gives the
negative limit in (16). Since Re lambda_r>1/6, |z_r|<1 and the
endpoint sum is exactly z_r/(1-z_r), not 1/(1-z_r).

For endpoints still in [Y/2,Y], integration of the n/12 bound and
the cap give (17). Nodes below Y/2 have, by (11)--(12), relative
modulus at most n^C*exp(-nY/12), and there are fewer than n of
them. The tail of the former bound is a convergent geometric series
independent of n. Splitting first at a fixed k cutoff, then taking
n to infinity and finally the cutoff to infinity proves the whole
signed sum limit. In particular no rate of decay of e_m, uniform
over choices of profile, is required.

Put rho_0=sqrt(d^2+Y^2)/R<1. On |z|<=1, every T_M is bounded
by (1-rho_0)^(-1), and its infinite-series remainder by
rho_0^M/(1-rho_0). For a fixed endpoint index its limiting resolvent
is consequently uniform on that disk. Multiplying the preceding
summable endpoint bounds by this common spatial bound proves (18)
uniformly on the closed disk. All moments and both endpoint signs
are retained. The anchor is bounded by 1/[R(1-d/R)], while
|W(Y)| grows at rate n*Phi_r(Y)+O(log n), so the same limit holds
for normalized G. The phase theta_n need not converge.

**Whole spatial mean and boundary zeros.** Multiplying the two
resolvents by their common denominator gives (19) exactly.
The map from (s,t) to its numerator values at 0 and 1/2 has matrix

    [ 2          0   ]
    [ 2+d/R    -Y/R ],

whose determinant is -2Y/R!=0. The denominators at both points
are fixed and nonzero. Thus the continuous two-point vector cannot
vanish when s^2+t^2=|b_r|^2; compactness gives a strictly positive
c_r independent of phase. The uniform upper bound also follows from
rho_0<1. Either normalized polynomial consequently has a nonzero
evaluation of size at least c_r/2 at one of these two points, for
all sufficiently large n, even if the other evaluation is zero.

Every such F_n is a nonzero polynomial, analytic beyond the closed
spatial disk; the imported logarithmic-integrability and boundary-zero
Poisson--Jensen results apply for each actual degree. At z=1/2 the
kernel is (3/4)/|exp(i*theta)-1/2|^2, has mass one and minimum
1/3. Writing it as 1/3 plus a nonnegative function of mass 2/3
gives precisely the upper bound for the Poisson integral used in
(21), hence the stated lower bound for the ordinary mean. At zero
ordinary Jensen applies instead. Both arguments use the uniform
boundary upper bound, not convergence of negative logarithms.
They bound the normalized mean above and below by constants
independent of n. Adding log|W(Y)| proves both assertions in (2),
including the O(log n) error and finiteness; possible spatial
boundary roots, multiple roots and degree drops cause no exception.

**Complete accounting and the limited obstruction.** L657's complete
polynomials give (5) after angular rescaling, with center-zero slices
omitted only in the almost-everywhere root identity. K(0,z) is a
nonzero polynomial and both K(r*v,z) and Q(r*v) have integrable
logarithms, even at boundary roots. Thus Fubini and the nonnegative
root-count increments justify (6). No cancelled factor is removed.
The anchor has constant term 1/R and all its spatial roots at
modulus R/d=11/10; this proves (3). A hypothetical almost-everywhere
inequality |V|<=|A_n| would contradict their finite logarithmic
means for large n. A strict reverse inequality at one spatial point
extends to a nonempty open subset by continuity. Since Q(-r)!=0,
it transfers to the complete K without a lost factor.

The spatial subset may depend on n and on which radius is tested;
neither a common subset nor a uniform lower bound on its measure
is claimed. A single negative-real angular point on each circle
refutes the uniform anchor condition there. It gives no lower bound
for an angular mean, no charge deficit and no exclusion of the
broader symmetric Rouche condition. The earlier source sentence is
clarified accordingly. No substantive mathematical error or new
premise was found. This first audit establishes the scoped local
input, not a stronger estimate or progress beyond the cited general
tools. The o(n) deficit, annular compensation, H/support and actual-Xi
realization and signs remain unresolved.

## Mathlib

Full matching coverage for this profile-specific endpoint asymptotic
and contour obstruction is unchecked. L657 records supporting results
in [Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. They are supporting root/mean tools,
not a formalization of (2) or (4). Coverage of the Poisson and uniform
endpoint applications was not checked; unknown is not absence.
