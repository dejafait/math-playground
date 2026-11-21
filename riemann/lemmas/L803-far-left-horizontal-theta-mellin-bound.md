# Lemma 803: a standalone far-left horizontal theta-Mellin bound

## Hypotheses

Use L797's saddle, L798's phase and principal branches, L799's complete
theta series, and L802's outward left endpoint. Explicitly, put

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    c=9/4, F(z)=z(pi exp(2z)-c), F(x)=s, x=u+ih,
    q=pi exp(2x), Q=pi exp(2u), d=3/(16u),
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    A=2F'(x)/x, B=|A|, theta=Arg A, a=exp(-i theta/2),
    C=sqrt(2pi/A)=a sqrt(2pi/B),
    z_L=x-da=v_L+i y,  y=y_L,
    P(z)=sum_{n>=1}[4pi^2 n^4 exp(9z/2)
                    -6pi n^2 exp(5z/2)]exp(-pi n^2 exp(2z)).

All complex logarithms, arguments and square roots are principal. L797
supplies the unique saddle on all D, with u>3 and
|h|<pi/4-1/(4u). L798 supplies Re A>0,
B<(2801/600)Q and |C|=sqrt(2pi/B)>0. L799 proves normal convergence
of P on U={z: |Im z|<pi/4}; its local amplitude estimate is not used.

For 0<epsilon<u/2 define

    J_F(s;epsilon)=integral_epsilon^(u/2)
                      exp(2s Log(v+i y))P(v+i y) dv.

The target is exactly the one in the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-far-left-horizontal-segment-test.md`.
The source comparison is bramble_trace, *A continuum certificate for
the decreasing Levy factor associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section 3, Lemma 2, (10)–(14). Its printed far-left
allowance motivates the threshold below, but it does not specify this
split at u/2. Neither its global-contour claim nor its uninspected
supplementary derivations is an input. The source-method assessment
and precise inspected hypotheses are retained in
`drafts/literature/2026-11-05-mellin-far-left-horizontal-segment-scope.md`.

## Conclusion

For every s in D the improper integral is absolutely convergent, and

    T_F(s):=|lim_(epsilon down to 0) J_F(s;epsilon)|
                  /|4pi^2 exp(S_s(x)) C|
       <56u^(5/2)sqrt(47Q/(20pi))exp(-Q/8)
       <600u^(5/2)sqrt(47Q/(20pi))
                    (1+10u/Q)exp(-Q/(20u)).                    (1)

This is a known-method specialization for the independently specified
segment. No novelty beyond the sources checked is asserted. The proof
was completed in step531 and passed the independent conceptual audit
in step533 below without a mathematical correction. It is a partial
component, not an RH candidate: the vertical
endpoint, global contour identity and complete budget, quotient and
inversion estimates, certificates and sufficient actual-Xi signs remain
unresolved. L800/L801 are possible downstream context only.

## Proof

### Geometry, branches and the actual improper endpoint

The following inequalities and identities are proved in L802:

    u-d<=v_L<u,  u/2<v_L,
    |y|<pi/4-13/(112u),
    cos(2y)>1287/(5600u)>1/(5u),
    Re(q-c)>Q/(4u)-c>0.                               (2)

For h>0 it also proves y=h+d sin(theta/2)>h>0. At h=0 it
proves theta=y=0 and s=u(Q-c)>0. For h<0, the quantities are
the conjugates of the corresponding ones for conjugate(s): in
particular y<h<0. These statements use the actual saddle and the
outward height, not a freely chosen horizontal contour.

For h!=0 the closed segment {v+i y: 0<=v<=u/2} is contained
in U and avoids the nonpositive real axis, including at its nonzero
purely imaginary endpoint. The principal Log and P are holomorphic
on a neighborhood of this compact segment. Its integral therefore
exists and is absolutely convergent, including at v=0.

For h=0, P is holomorphic near the compact real interval [0,u/2]
by L799. Since s=u(Q-c)>0 is real, exp(2s Log v)=v^(2s)
for v>0 and tends to zero at zero. Multiplication by the bounded
continuous P(v) gives a continuous extension with value zero.
This proves absolute convergence of the improper integral in this
case as well. It uses no analytic continuation of an originally
divergent Mellin integral. Uniform payment as h tends to zero is
proved below, separately from this pointwise existence argument.

### Monotonicity of the modulus of the Mellin power

First let h>0 and write s=sigma+i t. The saddle identity gives

    t=uQ sin(2h)+h(Q cos(2h)-c)>0,                    (3)

since 0<h<pi/4 and Re(q-c)>0. Put

    W(v)=|exp(2s Log(v+i y))|.

This retains the full angular factor: explicitly
W(v)=exp(2sigma log|v+i y|-2t Arg(v+i y)). For 0<=v<=u/2,
ordinary real differentiation, valid also at v=0 since y>0, gives

    (log W)'(v)=2Re(s/(v+i y))
               =2(sigma v+t y)/(v^2+y^2).             (4)

If sigma>=0, then sigma v+t y>0 by (3). If sigma<0, use v<=u
and y>=h to obtain

    sigma v+t y>=sigma u+t h
        =Re(s conjugate(x))=|x|^2 Re(q-c)>0.           (5)

Thus W is increasing on the whole far-left interval. This argument
does not assume sigma>=0 throughout D and makes no concavity claim
for the full phase before u/2. At h=0, W(v)=v^(2s) is increasing
for v>0 and its continuous extension is zero at zero. For h<0,
conjugation preserves the principal Log on the segments in question,
P has real coefficients in its defining exponential series, and L797
and the endpoint formulas respect conjugation. Thus W has the same
values as for conjugate(s), and the same monotonicity follows.
In all cases, with the extension just specified,

    0<=W(v)<=W(u/2),  0<=v<=u/2.                     (6)

### A complete-series Gaussian majorant

We need bounds valid for every real tau>0, because the lower endpoint
theta parameter can shrink as u increases. The decreasing positive
function exp(-tau r^2/2) satisfies

    sum_{n>=1} exp(-tau n^2/2)
       <=integral_0^infinity exp(-tau r^2/2) dr
       =sqrt(pi/(2tau)).                             (7)

The comparison follows by integrating on each [n-1,n] and then
taking the increasing limit of the nonnegative partial sums. The
integral is the standard gamma-integral specialization
[NIST DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1), with mu=2,
nu=1, z=tau/2>0 and Gamma(1/2)=sqrt(pi). Its hypotheses
Re(nu)>0, mu>0, Re(z)>0 and principal powers hold; only a real
Gaussian integral is being evaluated. This is the same standard
Gaussian integral used in L798, not a new moment theorem.

For k=1,2, maximizing r^k exp(-tau r/2) on r>=0 gives
the value (2k/(e tau))^k, at r=2k/tau. Multiplying this
bound at r=n^2 by exp(-tau n^2/2) and using (7) yields

    sum_{n>=1} n^2 exp(-tau n^2)
       <=(2/e)sqrt(pi/2)tau^(-3/2)<2tau^(-3/2),
    sum_{n>=1} n^4 exp(-tau n^2)
       <=(16/e^2)sqrt(pi/2)tau^(-5/2)<4tau^(-5/2).    (8)

For the strict constants, e>2, e^2>7 and pi<4 give
sqrt(pi/2)<3/2, so the first coefficient is <3/2<2
and the second is <24/7<4. These elementary exponential bounds
are established in L797. The argument controls every term of
the infinite sums, without a large-tau restriction.

Put K=cos(2y), so 0<K<=1 and K>1/(5u) by (2). For
z=v+i y and 0<=v<=u/2 set tau=pi K exp(2v)>0. L799's
normal convergence justifies taking the triangle inequality in the
complete series; (8) gives

    |P(v+i y)|/(4pi^2)
      <=exp(9v/2) sum_{n>=1} n^4 exp(-tau n^2)
          +(3/(2pi))exp(5v/2) sum_{n>=1} n^2 exp(-tau n^2)
      <pi^(-5/2)K^(-5/2)(4+3K)exp(-v/2)
      <=7(pi K)^(-5/2)exp(-v/2)
      <28u^(5/2)exp(-v/2).                           (9)

Indeed pi K>3/(5u), and (5/3)^(5/2)<4 because
5^5=3125<3888=16*3^5. The bound is uniform even when K tends
to zero, with its full cost recorded as u^(5/2). No sign is assigned
to a complex theta summand. No series/integral interchange is needed;
if one integrates the absolute summand bounds, (6) and (9) provide
an integrable majorant for their sum, including the improper endpoint.

### Paying the phase loss at u/2

Let z_0=u/2+i y, tau_0=Re(pi exp(2z_0))=Q exp(-u)K,
and phi_0=Re(S_s(z_0)-S_s(x)). The left tangent inequality
proved in L802, (16), applies at its lower endpoint v=u/2 and gives

    phi_0<=-(85/48)Qd^2-kappa(v_L-u/2),
    kappa=(105/256)Q/u.                              (10)

We use this inequality only at u/2, within its proved interval.
No extension of that phase concavity or its theta-amplitude bound
to smaller v is used. The definition of S_s gives the exact identity

    W(u/2)/exp(Re S_s(x))
        =exp(phi_0-9u/4+tau_0).                      (11)

In particular the removed theta exponential is paid with its positive
sign +tau_0; the angular factor in W has not been discarded. Since
v_L>=u-d, K<=1 and u>3, (10) implies

    phi_0-9u/4+tau_0
      < -kappa(u/2-d)+Q exp(-u)
      = -Q[(105/256)(1/2-3/(16u^2))-exp(-u)].        (12)

Here only negative terms were dropped. For all u>3,

    (105/256)(1/2-3/(16u^2))>805/4096,
    exp(-u)<1/14,
    805/4096-1/14=3587/28672=1/8+3/28672>1/8.       (13)

The first inequality uses 1/2-3/(16*9)=23/48, and the
second uses exp(3)=e*e^2>2*7=14. Thus (11)–(13) prove

    W(u/2)/exp(Re S_s(x))<exp(-Q/8).                 (14)

### Normalization and all-domain payment

Using absolute convergence, (6) and (9), and integrating the
nonnegative scalar majorant, we obtain

    |lim_(epsilon down to 0)J_F(s;epsilon)|/(4pi^2)
       <=integral_0^(u/2) W(v)|P(v+i y)|/(4pi^2) dv
       <28u^(5/2)W(u/2) integral_0^(u/2)exp(-v/2) dv
       <56u^(5/2)W(u/2).                            (15)

The scalar integral is 2(1-exp(-u/4))<2. The exact denominator
has modulus 4pi^2 exp(Re S_s(x))sqrt(2pi/B). Also

    B<(2801/600)Q<(47/10)Q,
    1/|C|=sqrt(B/(2pi))<sqrt(47Q/(20pi)),             (16)

where 47/10-2801/600=19/600>0. Dividing (15) by the
remaining factors of the denominator and applying (14)–(16)
proves the first bound in (1). Finally 56<600,
1+10u/Q>1 and 1/8>1/(20u) for u>3 prove its second bound.
All inequalities are strict on the closed D, since the saddle and
endpoint inequalities used from L797–L802 hold there directly.
Both |s|=6000 and the curved left boundary are included, as are
both signs of h, h=0 and the unbounded range u>3. The constants
do not depend on a fixed nonzero h, so no additional assumption is
introduced as h tends to zero.

This direct specialization is needed because the inspected primary
sources supply Gaussian/gamma methods and the nominated source
allowance, but no proved statement matching this chosen split,
moving angle and normalization. The elementary complete-series
majorant and actual saddle monotonicity above supply those specific
obligations. They do not prove a global contour equality or any
sufficient Xi sign inequality. No numerical evidence is used.

### Independent conceptual audit, 5 November 2026 — step533

The exact target had prior SPECIALIZE coverage in
`drafts/literature/2026-11-05-mellin-far-left-horizontal-segment-audit.md`.
Independent reconstruction verifies absolute convergence and both
inequalities in (1), with no change to their hypotheses or constants.
This establishes reviewed local input, not new mathematics beyond the
sources checked. The audit uses analytic estimates throughout; no
finite sample or uninspected source allowance is evidence for (1).

**Input scope and endpoint.** L797 supplies its saddle and strict
clearance directly on the closed D, together with conjugation and
Re A>0. L798's proof (6)–(7) supplies B<(2801/600)Q and exactly
C=a sqrt(2pi/B); its phase-disc decrement is used by L802. L799's
normal convergence is on every compact subset of U, not just on the
local diameter: its summable majorant is
C_E(n^4+n^2)exp(-delta n^2), delta>0. Thus its holomorphy conclusion
applies along the entire new segment. No local amplitude bound is
extended to that segment.

L802 gives u/2<v_L<u, |y|<pi/4-13/(112u) and
K=cos(2y)>1287/(5600u)>1/(5u), since 1287>1120.
Its outward-height sign and Re(q-c)>0 have the same saddle and
branches as here. For h!=0, y has the sign of h, so v+i y never
meets zero or the nonpositive real axis even at v=0. The compact
segment has a neighborhood in U and in the principal-Log domain.
For h=0, y=0 and s=u(Q-c)>0 is real. Boundedness of P near
[0,u/2] and v^(2s)->0 give a continuous zero extension of the
integrand. These arguments prove pointwise absolute convergence in
every case; the parameter-uniform bound is a separate calculation.

**The angular factor and monotonicity.** For h>0,
t=uQ sin(2h)+h Re(q-c)>0 and y>h. Direct differentiation of
2sigma log|v+i y|-2t Arg(v+i y) gives precisely
2(sigma v+t y)/(v^2+y^2). If sigma>=0 its numerator is positive,
including at v=0. If sigma<0, then

    (sigma v+t y)-(sigma u+t h)
        =sigma(v-u)+t(y-h)>=0,
    sigma u+t h=Re(s conjugate(x))=|x|^2 Re(q-c)>0.

Both signs in the first line are essential: v<=u/2<u, whereas
y>=h. This proves the required increasing modulus without discarding
the factor exp(-2t Arg(v+i y)) or assuming Re s>=0 on D.
At h=0 the real power increases from its zero extension. For h<0,
principal Log commutes with conjugation on these segments; the saddle,
A, a and y conjugate with the stated signs. The complete series for
P also respects conjugation. Consequently W and the integral modulus
reduce to the h>0 case. No concavity assertion before u/2 is used.

**All-parameter control of the complete series.** For every tau>0,
exp(-tau r^2/2) decreases on [0,infinity), so its integral on
[n-1,n] is at least its value at n. Summing and taking monotone
limits proves (7). The imported DLMF 5.9.1 specialization has
mu=2, nu=1 and z=tau/2>0; its hypotheses are satisfied here.
For k=1,2, differentiation of r^k exp(-tau r/2) gives its global
maximum at r=2k/tau, including the zero and infinite endpoints.
Exponent splitting at r=n^2 therefore proves (8) for the entire
infinite sums, without tau>1 or tau>3. The strict coefficient checks
are (2/e)sqrt(pi/2)<3/2<2 and
(16/e^2)sqrt(pi/2)<24/7<4.

Substitution of tau=pi K exp(2v) into the two terms of P gives,
respectively, the factors
4pi^(-5/2)K^(-5/2)exp(-v/2) and
3pi^(-5/2)K^(-3/2)exp(-v/2) after division by 4pi^2.
Their sum is exactly the bound with coefficient 4+3K in (9).
Because 0<K<=1, pi K>3/(5u), and
(5/3)^5=3125/243<16, its coefficient is strictly below
28u^(5/2). This accounts for the full shrinking-clearance cost;
it never replaces K by a positive constant independent of u.
Normal convergence licenses the pointwise triangle inequality.
Integration uses the resulting scalar majorant, not an unstated
interchange of a conditionally convergent series and an integral.

**Endpoint phase payment.** L802's (16) is valid on [u/2,v_L].
Taking its real logarithm at u/2 gives (10) with
kappa=(105/256)Q/u. The audit uses this estimate nowhere to the
left of u/2. Since Re z_0=u/2, the exact relation between W and
S_s is

    log W(u/2)-Re S_s(x)=phi_0-9u/4+tau_0,
    tau_0=Q exp(-u)K>0.

Thus the removed theta exponential costs +tau_0, not -tau_0.
Using v_L>=u-d, dropping only negative terms, and K<=1 gives
the strict upper bound in (12). For every u>3 the resulting loss
coefficient exceeds

    (105/256)(23/48)-1/14
       =805/4096-1/14
       =3587/28672=1/8+3/28672.

Here 23/48=1/2-3/(16*9), and exp(-u)<1/14 follows from
exp(3)=e*e^2>14. Hence the claimed exp(-Q/8) payment holds
over the full unbounded range, with no numerical threshold check.

**Measure, normalization and boundary cases.** The horizontal
parameterization has dz=dv, so there is no rotated factor a in its
measure. Monotonicity gives W(v)<=W(u/2). The absolute integral
is bounded by 28u^(5/2)W(u/2) times
2(1-exp(-u/4))<2, yielding (15). The exact denominator modulus
is 4pi^2 exp(Re S_s(x))sqrt(2pi/B), strictly positive. The bound
on B has the right direction for its reciprocal square root, and
47/10-2801/600=19/600>0. These facts prove the first inequality
in (1), including its coefficient 56. The second follows from
56<600, 1+10u/Q>1 and 1/8>1/(20u).

The strict input estimates hold on both closed boundaries of D.
The proofs above include h=0 and both signs of h, and impose no
upper cutoff on u or lower bound on |h|. They supply one uniform
parameter estimate; no limit under the integral as h->0 or u->infinity
is needed. L797, L798, L799 and L802 are exactly the direct local
inputs used, so the existing ID-only DAG row requires no change.
No global contour identity, meromorphic vertical endpoint, combined
error budget, quotient/inversion estimate, certificate or sufficient
Xi sign theorem is inferred. Those remain independent open steps.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
The standard real Gaussian integral is imported with its hypotheses
above; normal convergence, the principal-root identity and endpoint
geometry are supplied by the stated local inputs. No specific Mathlib
declaration or formal verification is asserted. The complete argument
is an informal proof that passed the conceptual audit above; it is
not a Lean formalization or a claim of formal verification.

