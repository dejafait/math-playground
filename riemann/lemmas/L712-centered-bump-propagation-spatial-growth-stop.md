# Lemma 712: centered bump propagation stops sublinear spatial growth

## Hypotheses

Fix exactly one actual L703 profile, including its original nonnegative
even plateau bump eta, cutoffs and width w, before n varies. Retain the
complete L666 family as used in L706 and L710–L711:

    n=12q+3, q>=1, M=n/3, A=27/10, h=A/n,
    d=5/4, R=11/8, Y=9/20, s=65/64,
    a(v)=-d+i*v, v_m=h*(m+1/2+e_m),
    Z_n={-d} union {a(v_m): -2q<=m<2q},
    G_n(u,z)=sum_(a in Z_n) W_a(u)*sum_(k=0)^(M-1)(a*z/R)^k/R,
    S_(n,r)(u)=max_(|z|<=r)|G_n(u,z)|,
    B_sp(n)=integral_(|u|=1/2) log(S_(n,s)(u)/S_(n,1)(u))dmu(u).

The weights W_a are exactly those of L666/L710, with unit masses,
anchor weight one, the inverse angular variable and j=0 retained.
Both finite endpoints, the signed interior and all M moments remain.
The measure mu is normalized full-circle angular measure; its
restriction to an arc is not renormalized. L706 supplies nonzero
spatial slices and continuous finite coefficients on this circle.

Let delta=2*pi*w>0 be the ACTUAL fixed half-width. Put

    f(t)=eta(t/delta),
    E_n(y)=integral_(-delta)^delta f(t)*exp(-i*y*t/h)dt,
    b=sup supp(f), C=integral_R f(t)dt.

Thus 0<=f<=1, f=1 on [-delta/2,delta/2], f is continuous with compact
support, delta/2<=b<=delta and C>0. Do not assume b=delta, an
explicit endpoint shape, or a quantitative lower bound for its mass
near b. This E_n is precisely L710's centered positive-bump transform,
with no continuation of S_e to complex frequencies.

Use L710's fixed positive-radius closed disk D_* centered at

    y_* = X_*+i*c_* = -19/50+i/20,
    z(y)=-R/(d+Im(y)-i*Re(y)),

on which 1<|z(y)|<s. Here c_*=1/20 is a height in the y-plane,
not L703's frequency center. Intersect L710's and L711's fixed
positive-measure arcs about u=i/2. On a fixed smaller closed arc I,
L710 supplies uniformly for y in D_* and all sufficiently large n

    G_n(u,z(y))/W_-(u)
       = A_n(u,z(y))*E_n(y)-K_-(u,z(y))+epsilon_n(u,z(y)),
    W_-(u)=W_n(u,-Y) != 0,
    |A_n(u,z(y))|>=exp(n/5000),
    sup |K_-|<infinity, sup |epsilon_n| -> 0.              (H1)

L711 supplies, uniformly on I,

    n^(-1)*log(S_(n,1)(u)/|W_-(u)|) -> 0.                 (H2)

These are the local results proved in L710–L711, not additional
positivity hypotheses. Their reliance on L709 and their analytic
arguments was checked in the joined step-171 audit; the canonical
audit sections in L709--L711 record the signs, tails and certificates.

## Conclusion

For any fixed r>0 small enough that the closed disk D(y_*,r) lies
in D_* and 4r<c_*,

    liminf_(n=12q+3 -> infinity)
        n^(-1)*log max_(y in D(y_*,r)) |E_n(y)|
                        >= b*(c_*-r)/A > 0.             (1)

In particular the previously unpaid threshold is satisfied:

    max_(y in D_*) |E_n(y)| >= exp(-n/10000)              (2)

at one existential onset along the ENTIRE allowed sequence. Combining
this with the complete signed formula (H1) and unit maximum (H2) gives

    liminf_(n=12q+3 -> infinity) B_sp(n)/n
                                      >= mu(I)/5000 > 0. (3)

Thus B_sp(n)=o(n) fails for this same fixed family, with the local
assembly accepted by the separate audit in Section 5. This is an informative stop for
the sufficient sublinear-spatial-growth mechanism. L707's inequality
J_sp<=constant*B_sp goes in the upper-bound direction: (3) gives NO
positive lower bound for J_sp and does not disprove J_sp=o(n).
It does not refute RH. Amplitude/full charge, L657 accounting,
H/support, Xi realization and actual-Xi positivity remain open.

The step-171 audit accepts this result. Its bump propagation is a specialization
of a standard named theorem, not a claim of a new general transform
theorem. The full fixed-family comparison was not established by
the saved literature assessment; this is not certified originality.
No effective onset, explicit angular width, pointwise noncancellation
at y_*, or lower bound at every point of D_* is asserted.

## Proof

### 1. Source reuse and the endpoint normalization

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`
and its parent comparison. The local interpolation, absolute-envelope,
pole-free-extension and two-arc completion stops do not control this
complex-disk bump maximum. No profile is changed in response to n.

Import Hadamard's three-circles theorem from K. Ramachandra,
*On the Mean-Value and Omega-Theorems for the Riemann Zeta-Function*,
TIFR Lectures 85, Springer (1995),
[Theorem 1.5.2 and complete proof, printed p.27, PDF p.37](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=37).
The saved assessment inspected the theorem and proof. It requires
analyticity near the closed annulus, with 0<r1<r2<r3, and yields

    M(r2)^log(r3/r1) <= M(r1)^log(r3/r2)*M(r3)^log(r2/r1).

Zeros in or on the annulus are allowed. We apply it to entire
functions on translated disks at radii r,2r,4r; the maximum-modulus
principle equates circle and disk maxima. This gives
M(2r)^2<=M(r)*M(4r). The general theorem is not reproved. No
entire-function indicator, saddle asymptotic or unassessed
quantitative unique-continuation result is imported.

Define the normalized entire function

    P_n(y)=exp(i*b*y/h)*E_n(y)/C
          =C^(-1)*integral_R f(t)*exp(i*y*(b-t)/h)dt.      (4)

Compact support permits differentiation under this integral on every
compact complex set: each derivative has a fixed finite power of
(b-t)/h and a bounded exponential on that set for each n. Hence it
is entire and P_n(0)=1, so it is never identically zero. Since t<=b
on the support and f>=0, for Im y>=0

    |P_n(y)| <= C^(-1)*integral f(t)*exp(-Im(y)*(b-t)/h)dt
             <=1.                                      (5)

The normalization uses the actual support endpoint, not the nominal
width. This is what supplies a common upper bound on all disks used
below, without paying a positive linear growth rate at each step.

For every fixed epsilon>0, set

    m_epsilon=integral_(b-epsilon)^b f(t)dt >0.            (6)

To justify strict positivity, b is the supremum of the support and
f is nonzero and continuous. There is a point in (b-epsilon,b) where
f is positive; continuity gives a subinterval of positive integral.
If there were no such point, the supremum of the support would be
at most b-epsilon. Values at the endpoint alone cannot form the
support of a nonzero continuous function. Flatness or gaps in f
near the endpoint do not invalidate this reasoning.

At y=i*c_* the integral (4) is real and positive. Equations (5)–(6)
give, for every n and every fixed epsilon>0,

    1 >= P_n(i*c_*)
      >= (m_epsilon/C)*exp(-c_*epsilon*n/A).              (7)

First take the lower limit of n^(-1)log in (7) for fixed epsilon,
then let epsilon decrease to zero. This proves

    n^(-1)*log P_n(i*c_*) -> 0.                          (8)

The endpoint mass can be arbitrarily small; it is constant in n.
No effective onset or exchange of a moving epsilon with n is used.

### 2. A finite horizontal chain of disk maxima

Fix r as in the conclusion, and set

    J=ceil(|X_*|/r),
    z_j=(j/J)*X_*+i*c_*, 0<=j<=J,
    M_j(a)=max_(|y-z_j|<=a)|P_n(y)|.

Here J is a positive integer fixed before n, and z_J=y_*.
All radius-4r disks are strictly in the upper half-plane, since
4r<c_*. Thus (5) gives M_j(4r)<=1. Every M_j(a)>0 because P_n
is entire and not identically zero. Consecutive centers have
distance |X_*|/J<=r, so the previous radius-r disk is contained in
the next radius-2r disk. Three-circles at the next center gives

    M_(j-1)(r) <= M_j(2r) <= sqrt(M_j(r)*M_j(4r))
                              <= sqrt(M_j(r)).

Consequently, by finite iteration,

    1>=M_J(r)>=M_0(r)^(2^J)>=P_n(i*c_*)^(2^J).           (9)

This is a maximum bound, not a pointwise lower bound. Interior or
boundary zeros cause no difficulty. The large but fixed factor 2^J
preserves (8); dividing log (9) by n proves

    n^(-1)*log M_J(r) -> 0.                             (10)

For an explicit quantifier check, given alpha>0 choose a fixed
epsilon with 2^J*c_*epsilon/A<alpha/2. Then choose n large enough
that 2^J*|log(m_epsilon/C)|/n<alpha/2. Equations (7),(9) yield
M_J(r)>=exp(-alpha*n). The disk, chain, bump and profile have not
varied with n. This holds for every sufficiently large integer n,
so in particular for the entire permitted subsequence.

Choose a maximizer y_n of |P_n| on the compact final disk. Equation
(4) and Im y_n>=c_*-r give

    max_(D(y_*,r)) |E_n|
       >= |E_n(y_n)|
       = C*exp(b*Im(y_n)*n/A)*M_J(r)
       >= C*exp(b*(c_*-r)*n/A)*M_J(r).                  (11)

Taking the lower limit and using (10) proves (1), hence (2).
Only this maximum is needed. Evenness and Gevrey regularity are
properties of the actual bump, but this argument uses just its
nonnegativity, continuity, positive plateau and compact support.
No substitute bump or new assertion about the Picard solution is
introduced.

### 3. The full signed spatial comparison

Let e_n=max_(y in D(y_*,r))|E_n(y)| and choose a point attaining it.
It depends on n but not on u; all the estimates in (H1) are uniform
in that whole disk and in I. By the triangle inequality applied to
the exact signed reduction, for all u in I,

    S_(n,s)(u)/|W_-(u)|
       >= exp(n/5000)*e_n - sup|K_-| - sup|epsilon_n|.    (12)

The first term grows exponentially by (1), or already by (2), so
the right side is at least one half of that term at one uniform
onset. In particular

    log(S_(n,s)(u)/S_(n,1)(u))
       >= n/5000+log e_n-log 2
                           -log(S_(n,1)(u)/|W_-(u)|).   (13)

The last logarithm divided by n tends uniformly to zero by (H2).
Since (1) implies liminf n^(-1)log e_n>=0, (13) yields

    liminf_n inf_(u in I)
       n^(-1)*log(S_(n,s)(u)/S_(n,1)(u)) >= 1/5000.      (14)

We have weakened away the additional positive term in (1).
No cancellation between the leading residue and the bounded endpoint
term can survive the uniform exponential separation in (12).
The remaining signed interior, both physical tails, all real-frequency
tails, comb samples and the finite M-moment remainder are included
through (H1); their analytic validity is inherited from L710, not
established by the elementary propagation argument.

For each n, continuous finite coefficients and nonzero slices from
L706 make both maxima positive and continuous on the compact angular
circle. Their logarithmic ratio is therefore finite and integrable.
It is nonnegative everywhere because the spatial disks are nested.
Integrate (13) over I and discard the nonnegative complement.
Uniformity in (14), with the full-circle measure of I, proves (3).
No limit/integral interchange or control on the other angles is needed.

### 4. Verification and scope of the negative result

The mathematical checks here are exact inequalities (5),(7),(9),
the fixed-parameter order following (10), the uniform triangle
inequality (12), and the direction of the final integration. No
numerical sample, symbolic script or new arithmetic certificate is
needed for the original step 169. In that step L709–L711 certificates
were not replayed or treated as analytic audits, and their separate
critical review remained essential. The later joined audit is in Section 5.

The achieved lower threshold is mu(I)/5000>0, whereas the tested
mechanism requires B_sp/n -> 0. This stops that sufficient mechanism
for the original fixed profile. It does not infer the reverse of
L707's growth-to-defect transfer, establish the sign of the
complementary Jensen defect, or settle any actual-Xi sign.

### 5. Separate conceptual audit — 3 November 2026, step 171

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-fixed-profile-spatial-growth-stop-audit.md`.
The audit accepts (1)--(3) and the same-family route stop. It checks
the following analytic argument in addition to the complete L709--L711
audit; the arithmetic replays alone could not establish this result.

**Actual endpoint and fixed propagation.** The positive bump in
L703 is exactly eta((v-omega_*)/delta); the negative bump is disjoint
from v>=0. Thus L710's transform is the E_n in the hypotheses, with
the original fixed eta and delta. Its support endpoint is b, not
presumed delta. Continuity and the definition of support imply positive
mass in every interval (b-epsilon,b); otherwise f would vanish on
that interval and, by continuity, at b as well, contradicting the
endpoint definition. The plateau gives b>=delta/2>0 and C>0.
Compact support justifies each complex derivative under the integral
for fixed n. Equation (5) follows from b-t>=0 on the support and
nonnegativity. Equations (7)--(8) take n to infinity with epsilon
fixed before letting epsilon decrease. No quantitative endpoint mass
or special Gevrey endpoint shape is required.

The cited three-circles theorem applies to entire P_n on each
translated closed annulus. It permits zeros; P_n(0)=1 ensures every
disk maximum is positive. The radii r,2r,4r are strictly ordered,
and all their disks lie in Im y>0. The containment of the previous
r-disk in the next 2r-disk gives exactly M_j(r)>=M_(j-1)(r)^2.
The integer J and hence 2^J are fixed before n. The explicit
epsilon-then-n choice after (10) proves the claimed rate even if
J is very large. Choosing a maximum on the final disk and undoing
the exponential normalization yields (11), with the lower height
c_*-r>0 and the sign +b*Im(y)/h. This is a disk-maximum result,
not a pointwise noncancellation statement.

**Common arc and signed assembly.** L710 supplies a fixed D_* and
a fixed angular arc with a strictly positive 1/5000 coefficient
rate. L711 supplies its rate-zero unit maximum on another fixed arc,
independent of the bridge width. Both contain i/2 in their relative
interiors, so a common closed arc I with positive full-circle measure
can be fixed once. Pick r>0 inside D_* before n. The maximizer of
E_n depends only on n, and every estimate in (H1) holds uniformly
at that point for all u in I. Its leading modulus grows at rate at
least 1/5000+b*(c_*-r)/A, while K_- is bounded and epsilon_n->0.
The reverse triangle inequality gives (12) at one uniform onset.
Dividing by the unit maximum and using (H2) leaves a uniform lower
limiting logarithmic ratio at least 1/5000; no cancellation or
exchange of limiting extrema is hidden in this deduction.

L706's nonzero-slice argument retains all M moments and W_x=1.
Thus both disk maxima are positive and continuous on the full angular
circle for every n, even when the actual spatial degree drops. Their
ratio is at least one everywhere. Integrating the uniform bound on
I and dropping the nonnegative complement proves (3) with the
full-circle measure mu(I), without renormalizing I or interchanging
a limit with an uncontrolled integral.

No substantive error was found. The joined arithmetic audit replayed
all 62 comparisons and 1520 cells/segments; its complete evidence is
`scripts/one-sided-hankel/spatial-growth-audit-171.json` and the three
full replay files named there. The proof checks above are distinct
from those auxiliary certificates. The result remains an informal
fixed-family obstruction, with existential arc and onset, no J_sp
lower bound and no actual-Xi realization or positivity conclusion.

## Mathlib

Full matching coverage for this fixed-family bump propagation and
positive averaged spatial-growth rate has not been checked. The
standard named three-circles input is imported by the precise citation
above; no Mathlib theorem or formal verification is claimed. Unknown
coverage is not evidence of absence. The bump specialization and
signed assembly remain informal; Section 5 records their separate
conceptual audit without claiming formal verification.
