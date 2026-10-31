# Lemma 502: Harnack cost of an everywhere-positive analytic detector

## Hypotheses

Let T be real, L=log T>=32pi, and set

    delta=log L/L, B=L/(4pi), a=delta L/pi, b=delta L/(4pi),
    K(x)=1-(sin(pi x)/(pi x))^2, with K(0)=0.

Let f be even entire and real on R. Use the Fourier convention

    f(z)=integral_R phi(v) exp(2pi i v z) dv,

where phi is C-infinity with compact support in [-R,R] for some R>0.
In a family, R may be fixed independently of T as in the approved
detector class; the conclusion below is independent even of R.
Assume the following inequalities on open horizontal strips:

    Re f(x+iy)>=0     for every real x and |y|<B,
    Re f(x+iy)>=1     for |x|<=a and b<|y|<B.             (H)

The only external mathematical input is disk Harnack: S. Axler,
P. Bourdon and W. Ramey, *Harmonic Function Theory*, second edition
(Springer, 2001), Theorem 3.4 and equation (3.5), printed pp. 47--48,
[author PDF dated 17 July 2020](https://axler.net/HFT.pdf#page=54).
For a positive harmonic function h on D(0,r) and |z|<=s<r,

    (r-s)/(r+s) h(0) <= h(z) <= (r+s)/(r-s) h(0).       (Ha)

The cited proof includes the open-disk case. Harnack is imported,
not reproved. The disk choice and weighted integration below are the
quantitative specialization covered by the prior source assessment.
No local lemma, zeta estimate or unproved positivity criterion is used.

## Conclusion

The integral is absolutely convergent, and uniformly over this class,

    integral_R f(x) K(x) dx >= L/(128pi).                (1)

In particular, no such family for every sufficiently large T can also
satisfy, for fixed C,c>0,

    integral_R f_T(x) K(x) dx
        <= C delta L exp(-c delta L)
         = C log L L^(-c).                             (2)

This rules out the stated everywhere-positive strip detector at the
stated scale. It does not rule out signed analytic detectors, positivity
only at actual zero coordinates, other strip/window scales, the desired
weighted off-line-count bound, or RH. Evenness and the full rectangle
are retained hypotheses of the intended class; the necessary bound
uses only nonnegative harmonicity and its required value at one point.
The specialization and its stated scope passed critical audit on
2026-10-30; the audit adds no stronger bound or arithmetic conclusion.

## Proof

### Integrability and nonnegativity

Compact smooth Fourier support implies absolute integrability of f on
the real axis. Explicitly, f is bounded there by integral_R |phi|.
Twice integrating by parts, with no boundary terms because phi is
globally smooth and compactly supported, gives for x!=0

    |f(x)| <= (2pi |x|)^(-2) integral_R |phi''(v)| dv.

The bounded estimate on [-1,1] and this estimate outside that interval
give f in L1(R). These bounds are required only for each T; no uniform
Fourier derivative bound for a moving family is assumed or obtained.
Since |sin t|<=|t|, the continuous kernel satisfies 0<=K<=1.
Thus fK is absolutely integrable. From (H) at y=0 and the reality of f
on R, f(x)>=0 for all real x. Consequently fK>=0 everywhere on R,
which will justify restricting the integral to a subset of R.

### Uniform interior geometry and Harnack comparisons

Put u(z)=Re f(z), a harmonic function. Choose

    r=3B/4, q=B/4=L/(16pi), z_*=iq.

The closed disk |z|<=r lies strictly inside |Im z|<B, so u>=0
on a neighborhood of that disk. Also L>=32pi>16. The function
log L/L is decreasing for L>e, and log(16)<4; hence

    0<delta<1/4, b=delta B<q<B, a>0.

Thus z_* satisfies the strict vertical rectangle cutoff in (H), with
real coordinate 0 lying in [-a,a]. In particular u(z_*)>=1.
There is no limiting appeal to either rectangle boundary.

For every epsilon>0, u+epsilon is positive harmonic on D(0,r).
Apply (Ha) with s=q. Since q/r=1/3, its upper and lower constants
are 2 and 1/2. Letting epsilon decrease to zero in these finite
pointwise inequalities gives

    u(z_*)<=2u(0),
    u(x)>=u(0)/2           for all real |x|<=q.

The same r and s work for every such x. Therefore

    u(0)>=1/2, f(x)=u(x)>=1/4   for |x|<=q.             (3)

This deals explicitly with weak strip positivity. It assumes neither
positive boundary data nor a global upper bound for u.

### Kernel integration and the required threshold

Because L>=32pi, q>=2. On

    E=[-q,-1] union [1,q]

we have K(x)>=1-1/(pi^2 x^2)>=1-1/pi^2>=1/2.
The measure of E is 2(q-1)>=q. Using (3) and the global
nonnegativity already proved,

    integral_R f(x)K(x)dx
        >= integral_E f(x)K(x)dx
        >= (1/4)(1/2) 2(q-1)
        >= q/8 = L/(128pi).

This proves (1), including the common onset log T>=32pi and the
absolute constant c_*=1/(128pi), independently of f and R.
For fixed C,c>0, the ratio of the proposed upper bound (2) to this
lower bound is

    128pi C (log L)/L^(c+1) -> 0      as L -> infinity.

Indeed, on writing v=log L this is 128pi C v exp(-(c+1)v),
which tends to zero by elementary exponential growth. Thus (1) and
(2) contradict each other beyond an onset allowed to depend on C,c.
This is an incompatibility of detector requirements, with no theorem
application to a moving-test zeta statistic and no zero-count claim.

### Critical audit: 2026-10-30

The independent replay passes with the hypotheses as stated. The imported
dimension-two open-disk theorem applies to u+epsilon without boundary
data. Both comparisons use the same r=3B/4 and s=q=B/4; taking
epsilon to zero is pointwise, so no uniform limiting assertion is needed.
The strict inequalities delta<1/4 and q<r<B put iq inside the required
rectangle and both comparison points inside the disk. At the included
endpoint L=32pi, q=2, so the final measure bound still holds with equality.
The Fourier integrations by parts have vanishing boundary terms even
when the support reaches +/-R, since phi is smooth on all of R and
vanishes outside its compact support. Its derivative bounds need not be
uniform in T. Reality and strip positivity make restriction to E valid;
the kernel lower bound is used only where |x|>=1. The resulting constant
is exactly (1/4)(1/2)L/(16pi)=L/(128pi). The comparison with (2) is
uniform over the stipulated class for fixed C,c; its eventual onset may
depend on those constants. No local mathematical input or additional
zeta hypothesis enters. This validates the necessary bound and class
stop, with no change to the proof or to the unresolved arithmetic gaps.

## Mathlib

Full Mathlib coverage of disk Harnack and this specialization has not
been checked. Unknown coverage is not evidence of absence. The precise
analytic input is the cited disk theorem; all geometry, weak-positivity
limits, integrability and kernel estimates used here are written above.
