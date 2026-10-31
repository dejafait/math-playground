# Lemma 506: finite-obstacle top-envelope cost diverges

## Hypotheses

Fix R>0 and a real T>exp(1). Use L504's definitions

    L=log T, a=log L/pi, b=a/4, B=L/(4pi),
    lambda=pi/(2a), K(x)=1-(sin(pi x)/(pi x))^2,
    K(0)=0, eta_R=1/(8R+2),
    k_R=inf_{|x|>=eta_R} K(x), A_R=2/k_R.

In particular 0<b<B, a>0 and 0<k_R<=1. For H>max(B,1), set

    X_H=H^2+a+B+2,
    O=[-a,a] times [b,B],
    Omega_H=((-X_H,X_H) times (0,H)) minus O.

On the top boundary let chi_H(x)=1 for |x|<=X_H/2 and
chi_H(x)=2-2|x|/X_H for X_H/2<|x|<=X_H. Prescribe chi_H
there and zero on the other outer edges and on the obstacle boundary.
Write h_H for the continuous Dirichlet solution on this bounded domain.
Define the prescribed envelope cost

    J_H=2R A_R exp(2pi R H) integral_0^b exp(-lambda y)
                              [h_H(a,y)+h_H(-a,y)]dy.       (1)

Existence and uniqueness of h_H, including its boundary values, are
justified below rather than assumed as an unbounded-domain theorem.
The general standard inputs are the bounded regular-domain Dirichlet
theorem, bounded-domain comparison and the planar disk Harnack
inequality. Precise source: T. Schmidt, *Partial Differential Equations
I*, version 15 January 2026, Section 2.4, printed pp. 22--23
(bounded-domain comparison), Section 2.8, printed p. 50 Remark (3)
(sharp ball Harnack bound, with the Poisson theorem/proof on p. 48),
and Section 2.10, printed pp. 62--67, especially the main Dirichlet
theorem on p. 66 and exterior-cone Remark (2) on p. 67:
[source PDF](https://www.math.uni-hamburg.de/home/schmidt/lectures/PDE.pdf).
The inspected source statements and proof cases are recorded in
`drafts/literature/2026-10-30-finite-rectangle-negative-part-barrier.md`.
Only their finite-domain conclusions are used. The separated solution
and quantitative specialization below are supplied explicitly; they
are not attributed to a printed source theorem.

## Conclusion

For every such fixed R,T the solution exists uniquely, 0<=h_H<=1,
and J_H/a tends to positive infinity as H tends to infinity. More
precisely, put

    W=1/R, k=pi R,
    H_0=max(B+1,b+1,sqrt(2(a+2W+b+1))),
    N=ceil(36W/b+4),
    C_(R,T)=(2R A_R/3) 3^(-N) sinh(kb/4)
                                      exp(kb/4-pi/12)>0.

Then for every real H>=H_0,

    J_H/a >= C_(R,T) exp(pi R H).                    (2)

This excludes a bounded top cost for exactly (1), namely the
continuous tapered portion of the uniform ambient-bandwidth
exponential boundary majorant along these expanding rectangles.
It does not lower-bound an actual negative part or show that an
admissible function attains the envelope. It supplies no counterexample
to Q_a(f)<=C_R a M(f) on H_a. It does not exclude finite-height
optimization, another exhaustion or sharper function-dependent
boundary data. Sides, bottom kernel, T-uniform estimates, H_a
realization, actual-Xi transfer and all-degree signs remain separate.
The separate critical audit of 30 October 2026 passes as recorded below.
It is a reproduction of standard comparison methods, not a claim
of progress beyond the literature checked.

## Proof

### Finite-domain solvability and regularity

For L>1, 0<log L<L, so b>0 and b<B. The closed obstacle lies
strictly inside the outer rectangle, since X_H>a and 0<b<B<H.
The domain Omega_H is bounded and connected: the channels to either
side of the obstacle connect its lower and upper channels. Its
boundary consists of two disjoint polygonal curves.

Every boundary point has an exterior cone. Along the obstacle's edges
one can take a cone directed into O. At an obstacle corner, where the
domain has interior angle 3pi/2, the complementary quadrant inside O
contains an open cone of angle, for example, pi/4 with that vertex
and sufficiently small positive height. Along an outer edge or at an
outer corner a cone lies outside the outer rectangle. The finite
Dirichlet theorem and its exterior-cone regularity criterion therefore
apply. No smooth-boundary assumption is needed.

The prescribed datum is continuous on the complete boundary: chi_H
vanishes at the outer top corners, agrees continuously at |x|=X_H/2,
and the obstacle carries constant zero data on its separate component.
The theorem gives a unique harmonic h_H in Omega_H continuous on its
closure. Comparison with the constants zero and one gives
0<=h_H<=1. Reflection x to -x preserves the domain and all boundary
data, so uniqueness also gives h_H(-x,y)=h_H(x,y). In (1) use the
continuous boundary values at y=0 and y=b; the integrals are finite.

### A corridor whose width is fixed before H grows

Fix W=1/R and k=pi/W=pi R as above. For H>=H_0, we have H>b
and

    X_H/2 >= H^2/2 >= a+2W+b+1 > a+2W.             (3)

The open corridor

    C_H=(a+W,a+2W) times (b/4,H)

is contained in Omega_H; its top edge lies in the plateau chi_H=1.
On its closure consider

    v_H(x,y)=sin(k(x-a-W))
                         sinh(k(y-b/4))/sinh(k(H-b/4)).    (4)

The denominator is positive. The x second derivative of (4) is
-k^2 v_H and its y second derivative is k^2 v_H, so v_H is harmonic.
It vanishes on the two vertical sides and the bottom, and its top
value is sin(k(x-a-W)), between zero and one. On the corridor's
artificial sides and bottom h_H>=0; on its top h_H=1. Both functions
are continuous up to all four corners. Bounded-domain comparison
therefore gives h_H>=v_H in C_H.

At the fixed point p=(a+3W/2,b/2), which lies in the corridor,

    h_H(p) >= sinh(kb/4)/sinh(k(H-b/4))
            >= c_0 exp(-kH),
    c_0=2sinh(kb/4)exp(kb/4)>0.                    (5)

The last inequality uses sinh(s)<=exp(s)/2 for s>0. Every parameter
in c_0 is fixed before H tends to infinity.

### Transfer below the obstacle, with a uniform constant

Set r=b/24 and I=[b/3,2b/3]. For y in I, connect p horizontally
to (a,b/2) and then vertically to q_y=(a,y). This polygonal path
has length at most 3W/2+b/6. Split it by arclength into m pieces
of length at most r, where

    m<=ceil((3W/2+b/6)/r)=N.

All centers on this path have a<=x<=a+3W/2 and
b/3<=y<=2b/3. The closed disk of radius 2r=b/12 about any center
has heights between b/4 and 3b/4. Thus it stays strictly below O
and above the outer bottom. Its horizontal coordinates lie between
a-b/12>0 and a+3W/2+b/12<X_H by (3). It is consequently compactly
contained in Omega_H, uniformly for H>=H_0.

Use the standard planar disk Harnack inequality in its radius-ratio
1/2 form: if h is nonnegative harmonic on a neighborhood of the
closed disk of radius 2r centered at c, then h(q)>=h(c)/3 whenever
|q-c|<=r. The factor is (2r-r)/(2r+r); it is the usual planar
Poisson-kernel ball estimate. This is only a fixed-radius
specialization of the cited Harnack input, not a new general Harnack
theorem. Applying it successively on these m disks to h_H gives

    h_H(a,y)>=3^(-m)h_H(p)
              >=3^(-N)c_0 exp(-kH)  for every y in I.       (6)

No Harnack constant for the moving domain Omega_H is presumed.
The disk radii, length bound, count N and factor 3 are explicit and
independent of H. Reflection gives the same lower bound at (-a,y).

### Cost, threshold and scope

Restrict the nonnegative integral in (1) to I, of length b/3. On I,
exp(-lambda y)>=exp(-2lambda b/3). Equations (5)--(6) imply

    J_H/a >= (4R A_R b/(3a)) 3^(-N)c_0
                  exp(-2lambda b/3) exp((2pi R-k)H).

Since a=4b, lambda b=pi/8 and k=pi R, this is exactly (2).
All divisions are by positive quantities. The lower constant may be
very small and depends on T as well as R; fixed-T divergence needs
neither its uniformity in T nor an effective asymptotic onset beyond
the displayed H_0. The required bounded O_R(a) cost already fails
for each fixed T in this specified envelope/exhaustion test.

For clarity about the ambient-envelope relation, an arbitrary f in
L504's V_R has Schwartz real trace and Fourier coefficient satisfying
|phi(v)|<=N(f). Directly integrating its support [-R,R] gives

    |Re f(x+iy)|<=|f(x+iy)|
          <=2R exp(2pi R|y|) N(f)
          <=2R A_R exp(2pi R|y|) M(f).              (7)

The last step is L504's ambient-R weight conversion, whose proof
uses only membership in V_R, not slow dilation or H_a positivity.
It is valid at all y and all T under consideration. For an f in H_a,
continuity gives Re f>=1 on the entire obstacle boundary. Its
negative part is continuous and subharmonic, zero there, and on the
top is bounded above by the scalar in (7) with y=H. Replacing the
unknown top values by this uniform scalar is a possible majorization,
not an equality with those values.

One precise way to see the cost's role is to solve the finite
Dirichlet problem with top datum
2R A_R exp(2pi R H) M(f) chi_H and zero elsewhere. By uniqueness
its harmonic extension is that scalar times h_H, and its weighted
two-side integral is M(f) J_H. This tapered datum is at most the
constant top envelope. Any nonnegative harmonic comparison with
boundary liminf at least that constant on the open top and at least
zero on the remaining boundary dominates this tapered extension by
bounded-domain comparison. At outer top corners the tapered value
is zero, so no discontinuous-corner datum is needed for this
comparison. In a positive decomposition of a larger envelope
majorant, adding bottom or side costs cannot cancel this portion.

This explains the failure of the prescribed uniform-envelope removal
certificate only. Inequality (7) is an upper bound on actual growth;
divergence of its harmonic cost cannot turn it into a lower bound
on max(0,-Re f), imply the existence of any f in H_a, or refute the
original positive-class Q inequality. No passage to an unbounded
Dirichlet solution or unproved exchange of limits was used.

### Separate critical audit, 30 October 2026

The audit replays the full proof under the separately approved
`drafts/literature/2026-10-30-l506-top-envelope-audit.md` scope.
No change to (1), (2), H_0, N or C_(R,T) is needed. The exact
sharp-Harnack citation above replaces the earlier imprecise Section 2.6
citation; this is a source-reference correction, not a stronger bound.

First, T>exp(1) gives L>1 and 0<log L<L, hence 0<b<B.
H_0>=B+1>max(B,1) ensures that the asserted quantitative range
lies in the original domain of definition. The obstacle boundary and outer
boundary are disjoint compact polygonal curves. The inner reentrant
corners have complementary quadrants, so the exterior-cone criterion
really does cover them. The top taper is continuous also at the outer
corners. These facts meet the finite Dirichlet theorem's hypotheses;
no boundary smoothness or assertion at infinity is substituted.

Second, H_0^2/2>=a+2W+b+1 puts the entire closed corridor top
inside the plateau. Its sides lie at x>a, so neither vertical side
meets the obstacle even when b<=y<=B. At p the sine is exactly one,
and k(H-b/4)>0 justifies the reciprocal-sinh lower bound in (5).
For the transfer, r=b/24 gives

    (3W/2+b/6)/r=36W/b+4.

The closed disks have lower height b/4>0 and upper height 3b/4<b,
strictly below the obstacle and below H. Their leftmost coordinate
is a-b/12=47a/48>0. For the rightmost coordinate, (3) gives
a+3W/2+b/12<a+2W+b+1<=X_H/2<X_H.
Thus every disk is compactly inside Omega_H. Schmidt's planar
point-to-center bound at radius ratio 1/2 gives exactly 1/3,
including a step of length r; iteration uses at most N steps.
The argument also permits a nonnegative harmonic function, so it
requires no unproved strictly positive minimum.

Third, the two reflected gap intervals supply the factor 2, the
interval length is b/3 and the smallest weight there is
exp(-2lambda b/3). Consequently the constant before exp(pi R H) is

    (4R A_R b/(3a)) 3^(-N)
             2sinh(kb/4)exp(kb/4)exp(-2lambda b/3)
      =(2R A_R/3) 3^(-N)sinh(kb/4)exp(kb/4-pi/12).

Every factor is strictly positive at fixed R,T. No T-uniform lower
bound on this constant is claimed or needed.

Finally, L504's ambient conversion uses only smooth Fourier support:
|phi|<=N and sup_R |f|<=2R N imply
4R eta_R N<N/2 and M>=k_R N/2. It therefore applies to every f
in V_R, independently of the supplementary dilation hypothesis.
For f in H_a, continuity extends (H) to the whole closed obstacle,
making its negative part zero on that boundary. The tapered top datum
is bounded above by the uniform envelope, not by a proved lower
bound on the actual negative part. In the comparison with a general
nonnegative harmonic envelope majorant g, the difference between the
tapered extension and g is harmonic and bounded above (the extension
is bounded and g>=0). Its boundary limsup is nonpositive, including
the corners where the taper vanishes. Bounded-domain comparison
therefore applies even if g has no continuous corner values. This
checks the precise domination assertion used in the certificate stop.
It neither constructs an admissible f attaining the envelope nor
establishes a lower bound for its negative part. No new edge beyond
L504 is used. The source manuscripts and matching Mathlib coverage
have not been independently audited here.

## Mathlib

Full matching coverage for this obstacle-domain Dirichlet construction
and explicit envelope-divergence specialization has not been checked.
The finite Dirichlet theorem, comparison and planar Harnack inequality
are named standard supporting results with the source given above.
No matching Mathlib theorem name or absence claim is asserted.
