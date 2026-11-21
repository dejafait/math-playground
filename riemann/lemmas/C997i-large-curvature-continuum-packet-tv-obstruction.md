# Corollary 997i: large curvature forces an exponential packet cost

## Hypotheses

Use the COMPLETE response H_n^+(z;mu) of C997c(1),(4)-(6), including
both beta terms, both integration intervals and K_(n+2)'s subtraction
of 1. Let n>=2 be an integer and set

    J=[15/8,17/8], z_star=1+i/8, r=1/256,
    A_crit=100/r^2=6553600, eta=1/1024,
    theta=arctan(1/32)/pi.

Fix ONE A>=max{A_0,A_crit} before n, where A_0 is C997e's existential
admissibility threshold. For any complex polynomial P of degree<=n put

    dmu_P(c)=1_J(c)*exp(-An(c-2)^2)*P(c)
                         *exp(in(phi(c)-c))dc,
    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2,
    V=||mu_P||_TV=integral_J exp(-An(c-2)^2)*|P(c)|dc,
    H(z)=H_n^+(z;mu_P), F=||H||_L2(J).

The phase is real on J. These are hypothetical slope packets, not
actual zeta data. A may not depend on n. Constants below may depend
on this fixed A, but not on n or the coefficients of P.

## Conclusion

There is a finite C_A>0 such that every such polynomial satisfies

    |H(z_star)| <= C_A*(n+2)*exp(-eta*n)
                              *[V^(1-theta)*F^theta+V].       (1)

At each feasible index let P_n be the EXACT continuum minimizer of
C997h, with its original TV V_n=M_n/Kcal_n and F_n=Kcal_n^(-1/2).
Then

    1 <= C_A*(n+2)*exp(-eta*n)
                 *[V_n^(1-theta)*Kcal_n^(-theta/2)+V_n].       (2)

In particular, at every sufficiently large feasible index with Kcal_n>=1,

    V_n >= exp(eta*n)/(2*C_A*(n+2)).                         (3)

Thus C997h(5)'s simultaneous positive exponential Kcal_n growth and
subexponential original TV are impossible for EACH fixed
A>=max{A_0,6553600}, including on unbounded integer subsequences.
More generally no target-one polynomial in this curvature range can
have both V<=exp(o(n)) and F<=exp(o(n)). Uniform exponential suppression
on the closed J would imply the latter condition, so is also excluded.

This is a partial stop of the approved continuum selection. It does
NOT decide fixed admissible A<6553600, if any exist. It does not assert
that the actual Gram kernel grows, that the minimizing TV always grows
at the rate in (3), or that arbitrary slope measures obey (1). The
kernel hypothesis in (3) is essential. The constant 6553600 is a
sufficient, deliberately loose threshold, not a transition value.

Step337, 11 November 2026: RESEARCH / REPRODUCTION, outcome NEGATIVE,
under the unchanged pre-invocation EXPLORE review334. This is a local
quantitative obstruction obtained by specializing known norm and Hardy
continuation tools; it is not a claim of originality beyond those tools.
This specialization was unaudited at step337. The independent step339
audit below accepts (1)-(3) with their existing qualifications. It is
neither an RH candidate nor a solution of the entire packet test.

## Proof

### Reused source contracts and the new quantitative input

Import T. Bloom, N. Levenberg, V. Totik and F. Wielonsky,
*Modified logarithmic potential theory and applications*,
[arXiv:1502.06925v2](https://arxiv.org/pdf/1502.06925v2),
Theorem4.13/(4.15), its proof and Example4.14, printed pp21-23;
definitions and (4.8) are on pp12-13,16-18. These primary contracts
were inspected in review329/step330. For any fixed nondegenerate compact
interval K, Lebesgue measure, ordinary degree<=n complex polynomials
and Q=0, the theorem gives, for each epsilon>0,

    ||P||_K <= C_(K,epsilon)*exp(epsilon*n)*integral_K |P|.  (4)

To specialize its function class, take f=g=identity, one polynomial
factor equal to 1, and choose a disk containing K in its holomorphic
domain. An interval is strongly regular; Lebesgue measure has the
required uniform small-ball mass lower bound, including at endpoints.
The field Q=0 is continuous. No whole-line Freud theorem, constant-sharp
quadratic-field extremizer or varying-A uniformity is used.

Import Y. Grabovsky and N. Hovsepyan, *Optimal error estimates for
analytic continuation in the upper half-plane*, CPAM74(2021),140-170,
[published author copy](https://sites.temple.edu/yury/files/2023/06/general_curve.pdf),
Theorem2.7/(2.20)-(2.22), pp149-150, with its boundary-case proof in
Section5, pp162-168. Reuse the inspection in reviews322/323. For complex
f in H2 of the upper half-plane with ||f||_H2<=1 and
0<delta<1 bounding ||f||_L2(-1,1), it states

    |f(w)|<=rho(w)*delta^gamma(w), w=x+iy, y>0,
    gamma(w)=-arg((w+1)/(w-1))/pi,
    rho(w)^(-2)=(y/9)*[arctan((x+1)/y)-arctan((x-1)/y)].

Here ||f||_H2=sup_(y>0)||f(.+iy)||_L2(R). The primary general
theorem is imported, not reproved. No unrestricted Hardy extremizer is
claimed to belong to the slope range. Also use the standard named
maximum modulus principle, Fourier-Plancherel theorem and finite
complex-measure Fubini theorem, with the latter measure contracts
already justified in audited C997c.

The new local input is an original-TV concentration estimate for ALL
degree<=n polynomials at large fixed curvature. It pays a narrower
upper support before continuation. This is materially different from
C997d's parked broad-support envelope; that stop is preserved. C997d's
unaudited local conclusion is not a mathematical input here. The proof
below verifies the complete-response norm, lower interval and tail
costs afresh using C997c. Reuse of assessed tools requires no new source
discovery and does not change review334's approved packet target.

### Concentration with the ORIGINAL weighted L1 normalization

Let s=A^(-1/2), so 0<s<=r/10 and [2-s,2+s] is contained in J.
For this fixed interval apply (4) with epsilon=1. Its weighted norm
comparison is

    S:=sup_(|x|<=s)|P(2+x)|
       <=C_s*exp(n)*integral_(2-s)^(2+s)|P(c)|dc
       <=C_s*exp(2n)*V,                                  (5)

since An(c-2)^2<=n there. This step bounds the polynomial on a
small fixed interval by its actual weighted L1 norm; it makes no
assumption about the minimizer's coefficients.

The elementary interval Bernstein-Walsh bound gives, for real |x|>=s,

    |P(2+x)| <= S*(|x|/s+sqrt((x/s)^2-1))^n
              <=S*(2*|x|/s)^n.                           (6)

For clarity the scale and degree in this standard bound can be checked
directly, without a weighted extremal identification: the expression
u^n P(2+(s/2)(u+u^(-1))) is a polynomial in u because deg(P)<=n.
On |u|=1 its modulus is at most S. The maximum modulus principle
therefore bounds it by S on the disk. For each real |x|>=s take
the solution of x=(s/2)(u+u^(-1)) with |u|<=1; its inverse modulus
is |x|/s+sqrt((x/s)^2-1). This proves the exact special case (6)
and explains the needed factor 2; it is not a reproof of the general
Bernstein-Walsh theorem.

For |x|>=r put u=sqrt(A)*|x|>=10. Equations (5)-(6) imply

    exp(-An*x^2)*|P(2+x)|
       <=C_s*V*exp(n*[2-u^2+log(2u)]).

The bracket decreases for u>=10, because its derivative is -2u+1/u<0.
At u=10 it is -98+log(20)<-94: log(20)<4 follows already from
e>5/2 and (5/2)^4>20. Integration over the portion of J with
|c-2|>r therefore gives

    ||mu_out||_TV <= C_A*exp(-94n)*V,                     (7)

where mu_in is the restriction to [2-r,2+r] and
mu_out=mu_P-mu_in. Endpoint choices have no effect for this density.
Also ||mu_in||_TV<=V. Every constant in (7) is independent of P and n;
its dependence on fixed A comes from C_s. No limit involving A is taken.

### The narrow upper response has a paid Hardy norm

For mu_in, split C997c's exact Fourier density as h_U+h_L, where

    h_U(t)=-2*g_n(t)*integral exp(-cn/4)
                              *1_{cn<=t<=c(n+2)}dmu_in(c),
    h_L(t)=2*g_n(t)*1_{n<=t<=n+2}
                                      *integral exp(-cn/4)dmu_in(c).

Its support satisfies

    supp h_U subset [(2-r)n,(2+r)(n+2)],
    supp h_L subset [n,n+2].                              (8)

These densities are bounded and compactly supported, hence in L1
and L2, even if the two spectral intervals overlap at a small n.
No disjointness is needed. C997c supplies the exact bound
|g_n(t)|<=2(n+2)exp(3t/8), including both beta terms and K's -1.
For a single slope c in [2-r,2+r], its upper density has interval
length 2c and magnitude at most

    4(n+2)*exp(cn/8+3c/4).

Its L2 norm is consequently at most
4*sqrt(2c)*(n+2)*exp(cn/8+3c/4). Integrating against the original
variation measure (or using Cauchy-Schwarz followed by nonnegative
Fubini) gives

    sqrt(2pi)*||h_U||_2
           <=C*(n+2)*exp((2+r)n/8)*V.                    (9)

Here C is fixed: 2-r<=c<=2+r and r is fixed. With

    H_U(z)=integral exp(izt)h_U(t)dt,
    G(z)=exp(-i*(2-r)n*z)*H_U(z),

(8) shifts the density to nonnegative frequencies. Plancherel with
this Fourier convention gives
||G(.+iy)||_2=sqrt(2pi)||exp(-yt)h_shifted(t)||_2.
Thus G is in H2 and (9) bounds ||G||_H2. Compact support also
justifies its analyticity and all finite-integral interchanges.
This carrier is legal for the restricted upper density; no such shift
is asserted for the lower interval or the removed slope tail.

### The boundary theorem, with the continuum L2 norm retained

If a nonzero entire G in H2 has ||G||_H2<=M, M>0, let

    f(w)=G(2+w/8)/(2*sqrt(8)*M).

Then ||f||_H2<=1/2 and
delta=||f||_L2(-1,1)=||G||_L2(J)/(2M) lies in (0,1/2].
The boundary norm is at most the global norm by Plancherel; it is
nonzero by the identity theorem. All hypotheses of the imported
boundary theorem hold. At w_star=8(z_star-2)=-8+i,

    (w_star+1)/(w_star-1)=(64-2i)/82,
    gamma(w_star)=theta,
    rho(w_star)=3/sqrt(pi*theta).

Undoing the rescaling gives, with C_theta=2^(5/2-theta)*rho(w_star),

    |G(z_star)|<=C_theta*M^(1-theta)*||G||_L2(J)^theta.     (10)

For G identically zero this inequality is immediate. On J the carrier
has modulus one; at z_star,
|H_U(z_star)|=exp(-(2-r)n/8)|G(z_star)|. Inserting (9) in (10)
therefore proves

    |H_U(z_star)|<=C*(n+2)^(1-theta)*exp(b*n)
                                *V^(1-theta)*F_U^theta,
    F_U=||H_U||_L2(J),
    b=((2+r)*(1-theta)-(2-r))/8
      =r/4-(2+r)*theta/8.                                (11)

Here theta>1/128. Indeed arctan(1/32)>32/1025>1/33, by integrating
the decreasing function 1/(1+t^2); pi<22/7 then gives
theta>7/726>1/128. Hence

    b < 1/1024-513/262144
       =-257/262144 < -1/1024=-eta.                       (12)

The negative sign comes from the paid concentration (7), not from a
change of normalization or an illegal global carrier.

### Pay the complete lower interval and the removed slope tail

Set d=1/8-r/4=127/1024. Directly from the lower density above and
its support in [n,n+2],

    sup_(x in R)|H_L(x)| <= C*(n+2)*exp(-d*n)*V,
    |H_L(z_star)| <= C*(n+2)*exp(-(d+1/8)*n)*V.            (13)

For the first inequality use
8*exp(3/4)*(n+2)*exp((3/8-c/4)n) at each slope c>=2-r.
For the second retain the additional factor exp(-t/8)<=exp(-n/8).
The plus sign and entire lower interval from C997c are preserved.

Let H_out be the complete response to mu_out, not an upper-only
approximation. C997c(5)-(6), with its broader interval I, bounds its
combined spectral variation by C*(n+2)*exp(9n/32)*||mu_out||_TV.
Its spectral support is positive, so the same bound applies both on
the real line and at z_star. Equation (7), and 94-9/32>93, give

    sup_(x in R)|H_out(x)|+|H_out(z_star)|
                       <=C_A*(n+2)*exp(-93n)*V.           (14)

Linearity of the COMPLETE response gives H=H_U+H_L+H_out. Since
|J|=1/4, (13)-(14) and the L2 triangle inequality yield

    F_U<=F+C_A*(n+2)*(exp(-d*n)+exp(-93n))*V.              (15)

For nonnegative x,y,z and 0<theta<1, concavity implies
(x+y+z)^theta<=x^theta+y^theta+z^theta. Substitute (15) into
(11), then add the point bounds (13)-(14). The resulting terms are
bounded by a constant times

    (n+2)^(1-theta)*exp(b*n)*V^(1-theta)*F^theta,
    (n+2)*exp((b-d*theta)*n)*V,
    (n+2)*exp((b-93*theta)*n)*V,
    (n+2)*exp(-(d+1/8)*n)*V,
    (n+2)*exp(-93n)*V.

All four pure-V exponents are at most -eta, by (12), d>0 and
d+1/8=255/1024>eta. Also (n+2)^(1-theta)<=n+2.
Absorbing finitely many fixed constants proves (1). P=0 gives V=0
and H=0 directly, so it was harmless to use nonzero norms above.

### The exact minimizer and the rate contradiction

C997h proves injectivity and the exact minimization formulas; its
eventual feasibility uses C997e's target asymptotic. At a feasible index,
substitute H(z_star)=1, F_n=Kcal_n^(-1/2) and V_n=M_n/Kcal_n
in (1). This proves (2), without replacing the continuum objective
or original weighted L1 norm by a sampled or coefficient norm.

Let n be large enough that 2*C_A*(n+2)*exp(-eta*n)<1. If Kcal_n>=1
and V_n<=1, (2) is impossible. Thus V_n>1; then
V_n^(1-theta)*Kcal_n^(-theta/2)<=V_n, and (2) proves (3).
In particular

    liminf_(n in S) log(V_n)/n >= eta

on any unbounded feasible subsequence S with Kcal_n>=1 eventually.
This conflicts with log^+(V_n)=o(n). The stronger required kernel
growth in C997h(5) certainly implies Kcal_n>=1 eventually. Separately,
if target-one packets had V<=exp(a_n), F<=exp(b_n), with
a_n,b_n>=0 and a_n/n,b_n/n->0, (1)'s right side would tend to zero.
This proves the last assertion without relying on C997h's interpolation.

### Scope and remaining gaps

No actual value of A_0 is needed: choosing any fixed A at least both
thresholds is legitimate. The result does not rule out an admissible
smaller A, and increasing the nominal A_0 must not be used to erase
that undecided range. The tail restriction is an estimate on the
original density, not a replacement family or an n-dependent curvature.
The full n-jet, positive-binomial, atomic and P=1 stops keep their
previous scopes; no exact derivative constraints are used here.

The step339 audit below verifies this inequality and C997h's needed
minimization input within their stated scopes. No numerical
conditioning calculation, finite-grid preview or asymptotic saddle
remainder supports the argument. The point bridge, selected/both-sign
transfer, C997a(8), original assay, reconstruction, signed recovery,
complements, regulators, L993, L984(H) and L030-L032/C032a remain open.

### Independent conceptual audit — step339

11 November 2026. RESEARCH / REPRODUCTION under the unchanged,
pre-invocation SPECIALIZE review337 (completed step338). The audit
accepts (1)-(3) without changing their hypotheses or numerical bounds.
It establishes the reliability of this scoped obstruction, not a new
general theorem or progress beyond the cited tools. C997h's separate
step339 audit checks exactly the minimizer input used here; its
higher-order interpolation and rate reduction are not needed.

**Fixed interval and original TV.** Rechecked the already assessed
Bloom-Levenberg-Totik-Wielonsky
[arXiv1502.06925v2](https://arxiv.org/pdf/1502.06925v2),
Theorem4.13 and full proof, Example4.14, pp21-23, with the source
conditions recorded in review337. On the fixed nondegenerate interval
[2-s,2+s], s=A^(-1/2), Lebesgue measure has
mu(B(x,t))>=t>=t^2 for 0<t<=min{2s,1}, including endpoints.
The interval is strongly regular; identity maps are nonconstant and
entire, and a disk containing it satisfies (4.8). Taking one polynomial
factor equal to 1 and Q=0 gives (4) for every complex degree<=n
polynomial. Any finitely many initial degrees can be absorbed in C_s
by finite-dimensional norm equivalence. No constant is required to
be uniform as s tends to zero: A is fixed first.

The source supplies only the unweighted comparison. The local weight
cost is explicitly exp(n), since An(c-2)^2<=n on this interval;
with epsilon=1 this gives S<=C_s exp(2n)V. For degree d<n the
expression u^n P(2+(s/2)(u+u^(-1))) still has no negative powers:
its smallest possible power is n-d>=0. On |u|=1 it has modulus at
most S, so maximum modulus proves (6) for complex coefficients as
well. For |x|>=r, the variable sqrt(A)|x|>=10 and
2-u^2+log(2u) is decreasing. Its value at 10 is less than -94.
Integrating the resulting pointwise bound over a subset of J, whose
length is 1/4, proves (7) with a constant independent of P and n.
This is the tail of the ORIGINAL absolute density. Phase cancellation,
polynomial coefficient norms and a lower bound for the minimizer's
coefficients are not used. P=0 is included by direct evaluation.

**Legal carrier and paid global norm.** C997c(4)-(6) and its step322
audit apply to the restricted complex measures mu_in and mu_out by
linearity. Both are finite, with variations <=V and <=C_A exp(-94n)V.
For each c in [2-r,2+r] the upper t-density has length 2c and sup
norm at most 4(n+2)exp(cn/8+3c/4). Minkowski's L2 inequality,
equivalently Cauchy-Schwarz against |mu_in| followed by Fubini, gives
the displayed sqrt(2c) factor in (9). All integrals are on a fixed-n
compact rectangle with absolutely integrable densities. This pays the
actual L2 Fourier density, rather than merely its total variation.

Let ell=(2-r)n. The shifted density is h_shift(t)=h_U(t+ell),
supported in [0,(2+r)(n+2)-ell]. Then
G(z)=integral_0^infinity exp(izt)h_shift(t)dt is entire and

    ||G(.+iy)||_2^2=2pi*integral_0^infinity
                                  exp(-2yt)|h_shift(t)|^2 dt.

This is bounded uniformly for y>0, and tends to 2pi||h_U||_2^2
as y decreases to zero. Thus the H2 norm and its boundary norm are
paid by (9). Only h_U is shifted. The lower interval, which begins
at n<ell, is explicitly left outside this Hardy carrier; possible
overlap of the two supports for small n is immaterial.

**Boundary normalization and strict decay.** Rechecked
Grabovsky-Hovsepyan, *Optimal error estimates for analytic continuation
in the upper half-plane*, CPAM74(2021),140-170,
[Theorem2.7/(2.20)-(2.21), pp149-150](https://sites.temple.edu/yury/files/2023/06/general_curve.pdf),
with norm (2.1), reusing reviews322/323/337's Section5 proof-case
inspection. Its boundary case has no interior spectral conjecture.
For M>0 bounding ||G||_H2, the affine map w -> 2+w/8 changes
each whole-line squared norm by a factor 8, and changes the local
squared norm by 8 times the integral on J. Therefore
f(w)=G(2+w/8)/(2sqrt(8)M) has H2 norm <=1/2 and local norm
delta=F_U/(2M)<=1/2. If G is nonzero, its entire extension ensures
delta>0 by continuity and the identity theorem. If G=0 the desired
point inequality holds directly. The theorem is thus applied with
0<delta<1, never to an unnormalized or zero-data nonzero function.

At w_star=-8+i the ratio in the source is (64-2i)/82. Its principal
argument is -arctan(1/32), giving theta as stated. The arctangent
difference in rho is arctan(9)-arctan(7)=arctan(1/32), so
rho=3/sqrt(pi theta). Undoing the factor 2sqrt(8) gives exactly
2^(5/2-theta)rho M^(1-theta)F_U^theta. The carrier contributes
exp(-ell/8) at z_star and unit modulus on J. Hence (11)'s exponent
is exactly b=r/4-(2+r)theta/8.

The strict scalar margin can be checked entirely rationally:
arctan(1/32)>32/1025>1/33 and pi<22/7 imply
theta>7/726>1/128. Since 2+r=513/256,

    b < -257/262144 = -eta-1/262144.

This is a strict improvement over the required -eta, not a numerical
preview. The inequalities follow from integrating 1/(1+t^2) on
[0,1/32], and from the displayed rational comparisons. No scalar
script or numerical certificate is needed.

**Every complete-response error.** For the inner lower interval,
3/8-c/4<=-d with d=127/1024, and its length is 2. C997c's exact
Laguerre bound therefore gives (13), including the plus sign of that
density and the extra exp(-n/8) at z_star. For mu_out the ENTIRE
C997c response has combined spectral variation at most
C(n+2)exp(9n/32)||mu_out||_TV and positive spectral support. Thus
the real-axis and target bounds both follow from (7):
-94+9/32=-2999/32<-93. No extra assumption about the tail's phase,
endpoint vanishing, or upper-branch dominance has entered.

Consequently H=H_U+H_L+H_out is an exact identity. Multiplying
each real-axis error bound by sqrt(|J|)=1/2 and applying the L2
triangle inequality proves (15). The elementary subadditivity of
x^theta for nonnegative x and 0<theta<1 retains all three terms
in that inequality. Its substitution into (11), followed by the
two target errors, yields precisely these five rates:

    b, b-d*theta, b-93*theta, -(d+1/8), -93.

The first is below -eta by the strict margin above; the next two
are smaller, and d+1/8=255/1024>eta. The mixed polynomial factor
is (n+2)^(1-theta)<=n+2; each data-error contribution has the full
factor (n+2) because 1-theta+theta=1. Absorbing their fixed constants
proves (1) with one C_A for all n>=2 and all P. Both beta terms
remain in g_n, K's -1 remains in its exact bound, both slope endpoints
are included in J, and the lower interval and removed slopes are paid.

**Qualified minimizer consequence.** The audited part of C997h gives
F_n=Kcal_n^(-1/2), V_n=M_n/Kcal_n and H_(P_n)(z_star)=1 at every
feasible index. Substitution proves (2). Set
q_n=C_A(n+2)exp(-eta n); eventually 2q_n<1. With Kcal_n>=1,
V_n<=1 would make the right side of (2) at most 2q_n<1. Hence
V_n>1, and V_n^(1-theta)Kcal_n^(-theta/2)<=V_n proves (3).
This argument gives no lower bound of this size when Kcal_n<1.
Along any unbounded feasible subsequence with Kcal_n>=1 eventually,
log V_n/n has liminf at least eta, contradicting log^+V_n=o(n).
For general target-one packets the same contradiction follows directly
from (1) if both V and F have subexponential upper bounds. Neither
argument uses the unaudited interpolation in C997h(4)-(5).

No bound required correction. Constants and onsets can depend on fixed
A; A_0 remains existential. The audited stop excludes only the stated
large-curvature range. It cannot be extended by increasing A_0 to
erase possibly admissible smaller A, or by replacing Kcal_n>=1 with
unproved kernel growth. Stops293/316/327/331/332 keep their scopes;
C997d is a contrast, not an input. No whole-measure, point-bridge,
selected/both-sign, complement, regulator or actual-Xi claim is obtained.

## Mathlib

Full matching coverage for this polynomial concentration and complete
response-TV obstruction has not been checked and remains unknown.
Exact formal coverage of the Bernstein-Markov and Hardy boundary
contracts above has not been checked. Maximum modulus, Plancherel and
complex-measure Fubini are named informal inputs here, not a claim of
a completed Lean proof or of absent Mathlib support.
