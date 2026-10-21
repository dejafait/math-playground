# Lemma 450: width-one forced-cross remainder and interior pass regions

## Hypotheses

Use exactly L449's width-one family, original cutoff and eventual ray
of real H. Put ell=log H, L(t)=log(2+t) and I=[H,2H]. Keep its rare
components, probabilities, w, bulk mean m and both raw second diagonals
fixed. All height-integral parameters are constant in t. Use L449
(9)--(12), with its scalar tau, u=|X0|^2, intermediate matrix M,
intermediate mass k, endpoint bump a and weighted recentering mu:

    S=ell g_H+(A_H)11+m1^2+a-mu,
    A=ell g_H+(A_H)11+a-mu,
    C=ell g_H/12+(A_H)22+(a-mu)/12,
    D0=sqrt(A C).

D0 denotes the positive block budget, not the physical discriminant.
Define the third ordinary normalized jet v3=f'''/L^3, with f=F_0/A_env
and A_env the original positive gamma envelope. This v3 is not one of
the response coordinates. No moment estimate or smallness assumption
on v3 is made globally. The exact actual f is smooth by L445.

This is a REPRODUCTION under the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-20-width-one-endpoint-forced-cross.md`, within
its complete centered-block test. There is no change of law or cutoff,
new zeta input, assertion of originality or converse realization claim.

## Conclusion

There are constants C0 and H0, independent of the original cutoff stage,
such that for every real H>=H0, the complete forced centered cross obeys
almost everywhere on I

    B_for/D0 = V_H + eps_H(t), |eps_H(t)|<=C0 ell^(-3/8),   (1)

where eps_H(t) is a scalar error function and

    V_H = [tau'(x0^2-2tau S)/(2Lw)+a'/(2L)]/D0.           (2)

Thus both intermediate components, their mass derivatives, the complete
Poisson derivative and bulk translation together are uniformly smaller
than the fixed PSD budget, including inside the endpoint layers. Neither
term in (2) is omitted or separately signed.

In particular, for all sufficiently large H the centered x,y block is
positive definite at almost every t in [H+1,2H-1] satisfying either

    u(t)>=ell^6/sqrt(2),                                 (3)

or

    |X0(t)|+|v3(t)|<=ell^(3/2).                          (4)

On the union of these regions its determinant is at least (3/4)AC.
On (3), |B_for|/D0=O(ell^(-3/8)); the same bound holds on (4).
No measure or eventual coverage assertion for their union is made.

For a fixed 0<epsilon<1 and sufficiently large H depending on epsilon,
|V_H|<=1-epsilon implies a positive definite block a.e. on that set;
|V_H|>=1+epsilon implies a strictly negative determinant a.e. on that
set. This is a quantitative test, not a claim that either set covers I
or that the latter has positive measure for the actual family.

The width-one PSD verdict remains open: possible failure is localized
to the endpoint layers and to the unsaturated interior outside (4).
L449's selected-constraint preservation is retained. The separate
step-300 audit below validates (1)--(15), using the stated L449 inputs;
it does not audit all of L449 or decide the remaining regions. This
partial comparison supplies no all-temporal
feasible law, other occupation identity, mean transport, inter-H/global
realization, actual clipping, capped nondegeneracy, L413 full-error
regulator margin, global mixed positivity or RH consequence.

## Proof

### The fixed diagonal budget

Set b_H(t)=ell g_H(t)+a(t), which is positive. L438 (13)--(15),
unchanged in L449, and L449 (1) give uniformly

    (1/2)ell^(7/8)+a <= b_H <= 2ell^(9/8)+a,
    ||A_H||=O(sqrt(ell)), |m|=O(1), mu=O(H^(-2/3)).     (5)

Consequently

    A=b_H+O(sqrt(ell)), C=b_H/12+O(sqrt(ell)),
    D0=(b_H/sqrt(12))(1+O(ell^(-3/8))),
    D0>=c b_H>=c'ell^(7/8), |S|<=C b_H.                (6)

For example the relative errors in the first line are bounded by a
constant times sqrt(ell)/ell^(7/8)=ell^(-3/8). After one onset both
relative errors have modulus below 1/2. Taking the square root of
their positive product proves the second line by the mean-value theorem
on a fixed compact positive interval. This verifies the constants in
(6) even if the endpoint amplitude is much larger than any log power.
The finite covariance corrections have zero diagonal by L449 (4).

### Uniform control of both intermediate branches and translation

We use the quantitative actual-response derivatives already established
in L448's subsection “A coarse uniform modulus for the old density,”
through its response formulas following (8). They give bounded response
values, first derivatives O(ell), and uniformly nonzero denominators
in m, n_-, h_+ and h_-. These estimates precede any use of the narrow
endpoint layer in L448 and concern exactly the unchanged data here.
That proof imports gamma recurrence and sector-qualified Stirling/
Cauchy estimates: [DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1),
[5.11(i)--(ii)](https://dlmf.nist.gov/5.11) and
[1.9.30--31](https://dlmf.nist.gov/1.9.E31). Its right-line Dirichlet
derivatives are absolutely convergent and its gamma arguments stay
in their stated sector. No extension of its derivative order or new
critical-line estimate is needed for the present remainder bound.

Here are the specific branch consequences, so that no atom derivative
or omitted mass is hidden in this application. Write F_+,F_- for the
positive and negative parts of L438's F_H(theta(t)). L438 (6) and
L445's fixed smooth torus functions give bounded values and a uniform
O(1) temporal Lipschitz constant for these two scalars. The finite
calibration coefficient is bounded and constant in t. L445 (2)--(4)
give the exact formulas, including their tie and zero conventions,

    k=ell^(-5/2)(F_+/h_++F_-/h_-),
    M11=sqrt(ell)[(4/9)F_+/h_++F_-(n_-)_1^2/h_-].       (7)

The reciprocals 1/h_+,1/h_- are uniformly bounded and O(ell)-Lipschitz.
For the positive branch this follows from the exact maximum of the two
absolute projections, rather than differentiating its discontinuous
selected direction. For the negative branch n_- is bounded and has
derivative O(ell); its squared first coordinate has the same bound.
Products in (7) therefore yield a.e.

    |k'|<=C ell^(-3/2), |M11'|<=C ell^(3/2).            (8)

Both matrices k_s Z_s Z_s^T are positive semidefinite, with norm
sqrt(ell) F_s/h_s. Their norms are O(sqrt(ell)), so

    |M12|<=C sqrt(ell).                               (9)

This holds pointwise even at projection ties; no derivative of M12
or of either selected atom has been taken. Also m=d_H b/|b|^2 has
|m|<=C and |m'|<=C ell, since d_H is bounded and constant in t,
the exact response vector b is bounded with derivative O(ell), and
|b| has a uniform positive lower bound. Thus

    |m1*m1'/L-m1*m2|<=C.                              (10)

All estimates are valid with the original high component retained in w;
its derivative is not assigned to (8).

### Poisson derivative and the complete relative error

L444 (17), whose cutoff calculation is separately audited there,
applies to this unchanged product and normalization:

    ||g_H'||_infinity<=C ell^(3/8)log ell.               (11)

Specifically L440's finite-product comparison gives the largest retained
prime y<=ell^(1/4). Logarithmic differentiation of that finite positive
product gives |(log P_j)'|<=C y log(2+y), and P_j<=ell^(1/8).
The unchanged N_H is bounded below and constant in t. These are exactly
the original cutoff assumptions; no H derivative or faster cutoff is
introduced.

Subtract the two terms displayed in (2) from L449's exact (12). The
remaining centered cross is precisely

    R_rem=(M11'-k'S-2L M12)/(2Lw)
                   +ell g_H'/(2L)+m1*m1'/L-m1*m2.      (12)

This identity retains the full translation, both intermediate raw
seconds, both intermediate mass derivatives and the actual normalization.
Using w>=1/4, ell<=L<=2ell, (8)--(11) and (6) gives

    |R_rem|<=C[sqrt(ell)+ell^(-5/2)|S|
                                      +ell^(3/8)log ell+1],
    |R_rem|/D0<=C[ell^(-3/8)+ell^(-5/2)
                                      +ell^(-1/2)log ell+ell^(-7/8)]
                 <=C0 ell^(-3/8).                    (13)

The last inequality holds after one onset because log ell=o(ell^(1/8)).
In particular the mass-loss term involving the possibly large endpoint
value S has been bounded relative to that same large diagonal budget,
not by an inappropriate interior bound. Set eps_H(t)=R_rem/D0 to obtain
(1). The main high-probability derivative and a' remain exactly in (2).

### Actual interior pass regions and the unresolved part

On [H+1,2H-1], a=a'=0 because the fixed cutoff is supported in (-1,1).
L449 gives tau'=0 a.e. on u>=ell^6/sqrt(2), including the equality
set. Thus V_H=0 a.e. on (3), proving its bound directly from (1).

For (4), set d(t)=L'(t)/L(t)^2. The exact ordinary differentiation
identities are

    X0'/L=(y0,z0-d y0,v3-2d z0).

Here d is bounded (and tends uniformly to zero), and hence

    |u'|/L=|2 X0.X0'|/L
                  <=C |X0|(|X0|+|v3|)<=C ell^3.       (14)

On (4), u<=ell^3<ell^6/sqrt(2) eventually, so
tau=u/ell^6<=ell^-3 and |tau'|<=C L ell^-3.
On the interior, (5) gives |S|<=C ell^(9/8), while x0^2<=ell^3.
It follows that

    |tau'(x0^2-2tau S)/(2Lw)|
          <=C ell^-3[ell^3+ell^-3 ell^(9/8)]<=C.      (15)

Thus |V_H|<=C ell^(-7/8) there. Combined with (1), this proves the
claimed O(ell^(-3/8)) relative cross bound on (4). This is a conditional
pointwise region statement about the actual jets, not an assertion of
an actual third-jet bound at every height or a source-derived measure
estimate. Smoothness suffices for the computation (14).

Finally import the scalar Schur-complement test from Boyd--Vandenberghe,
*Convex Optimization*, 2004, corrected seventh printing 2009,
[Appendix A.5.5, pp. 650--651, (A.13)--(A.14)](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=664).
Since A,C>0, the block is PSD precisely when |B_for|/D0<=1,
and its determinant is AC[1-(B_for/D0)^2]. The established relative
bound is at most 1/2 on (3) and (4) after a common onset, giving
determinant >=(3/4)AC. In general choose H so that C0 ell^(-3/8)
<epsilon/2 and apply the two triangle inequalities to (1). This gives
the stated fixed-epsilon pass and failure tests without making a
measure assertion about their actual occurrence.

Neither this argument nor L449 controls (2) on the remaining
unsaturated interior or the endpoint layers. A positive-measure
failure must still be proved for the actual fixed law, or a uniform
a.e. comparison must cover those regions, to decide the approved
PSD target. The former narrow-layer contradiction is not reused as
evidence of failure here. The independent realization and RH gaps
listed in the conclusion remain unchanged.

### Bounded continuation: the available pointwise envelope is inconclusive

Step 295 tests the remaining expression (2) with the already covered
order-three Cauchy input. This does not extend the conclusion or its
pass regions. All data and hypotheses above remain fixed. Write
b=ell g_H+a and V_H=P_H+E_end, where P_H is the first term in (2)
and E_end=a'/(2L D0).

On the unsaturated set u<ell^6/sqrt(2), the exact derivative identities
in (14), before imposing the small-jet condition, give

    |u'|/L <= C sqrt(u)(sqrt(u)+|v3|).

Since tau=u/ell^6, x0^2<=u, w>=1/4, |S|<=Cb and D0>=cb,
the complete high-component term satisfies

    |P_H| <= C (u^2+u^(3/2)|v3|)
                         [1/(ell^6 b)+1/ell^12].     (16)

Indeed the first bracket contribution bounds tau' x0^2/(2LwD0),
and the second bounds tau' (2tau S)/(2LwD0). Thus the mass-loss
part, including a possibly large endpoint value of S, is retained.
On the saturated set P_H=0 a.e. as before. The inequality is an
upper bound after a triangle inequality, not an estimate from below
for the signed sum.

L448's proof of (7)--(8), in its subsection on the old density's
modulus, gives |v3|<=C H^(1/6). Its application at order three uses
the pole-free radius-1/ell zeta disks already established in L391,
the Cauchy derivative formula and the differentiated gamma phase;
it concerns unchanged actual jets and precedes any use of the
H^-10 endpoint width. The precise underlying scalar citation is
Bourgain, *JAMS* 30 (2017), 205--224,
[arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
with epsilon=1/168; the analytic derivative tool is
[DLMF 1.9.30--31](https://dlmf.nist.gov/1.9.E31).
No third-derivative moment or relative jet estimate is imported.
Using u<=ell^6 and b>=c ell^(7/8) in (16) therefore yields only

    |P_H| <= C[ell^(41/8)+H^(1/6)ell^(17/8)
                                      +1+H^(1/6)ell^-3]. (17)

The two terms in the first pair arise respectively from u^2 and
u^(3/2)|v3| divided by ell^6 b; the second pair comes from ell^12.
This certified majorant grows, whereas a fixed margin below one
for |V_H| is required. It does not prove that P_H is large anywhere.

The endpoint term admits a sharper estimate than using ||rho'||
alone, but it still does not resolve the test. Set M=||rho''||_infinity,
which is a finite positive constant for the unchanged compactly
supported cutoff. For every real s,h, Taylor's formula gives

    0<=rho(s+h)<=rho(s)+rho'(s)h+(M/2)h^2.

Taking h=-rho'(s)/M proves |rho'(s)|^2<=2M rho(s).
This is a direct applicability calculation for the given nonnegative
smooth cutoff, not a new cutoff choice or a reproof of its existence.
There is at most one active endpoint, with a=alpha rho(s) and
|ds/dt|=1. Thus |a'|<=sqrt(2M alpha a), including at a=0.
For each fixed t put b0=ell g_H(t)>0. The elementary identity
(sqrt(a)-sqrt(b0))^2>=0 gives
sqrt(a)/(b0+a)<=1/(2sqrt(b0)). Equations (5)--(6) now imply

    |E_end| <= C sqrt(alpha)/(ell sqrt(b0))
           <= C sqrt(alpha) ell^(-23/16)
           <= C H^(1/6) ell^(-23/16).                 (18)

The last line uses precisely L449's alpha=O(H^(1/3)), not an
assertion that such amplitudes occur. The estimate holds on both
endpoint layers, with either sign of a', and is zero off them.
It keeps the endpoint's contribution to the diagonal budget.

Combining (17), (18) and (1) supplies no bound below the PSD
threshold one. Conversely, none is a lower bound on |P_H+E_end|:
cancellation between these terms, or smaller actual jets and
amplitudes, remains possible. No positive-measure violating set is
established. This bounded envelope attempt is therefore EXPLORATION,
not an informative negative verdict on the width-one law and not
an extension of the pass theorem. Further work on this same target
needs signed actual-jet control or an actual violating interval;
repeating the same absolute Cauchy envelopes cannot certify either
outcome. L449's selected constraints, the stated pass regions and
all independent realization and RH limitations are unchanged.

### Bounded continuation: a signed interval test without a third-jet envelope

Step 296 keeps all data fixed and tests a different certificate. No
occurrence of the intervals described below is asserted. Let J=[s,t]
be any nondegenerate closed subinterval of I, and define

    I_J=integral_J [tau'(x0^2-2tau S)+w a'],
    T_J=integral_J 2Lw D0 > 0,
    delta_H=C0 ell^(-3/8).                            (19)

All derivatives in this subsection are the a.e. fixed-H derivatives.
Every integrand is integrable: the scalar functions concerned are
Lipschitz on I, or bounded measurable, and L,w,D0 are positive with
the bounds already proved. Multiplying (1)--(2) by 2Lw D0 gives

    |integral_J 2Lw B_for-I_J|<=delta_H T_J.           (20)

Consequently |I_J|>(1+delta_H)T_J certifies negative determinant
on a positive-measure subset of J. Indeed, if the block were PSD
a.e. there, the imported scalar Schur-complement criterion would
give |B_for|<=D0, hence |integral_J 2Lw B_for|<=T_J,
contradicting (20). More precisely, a strict excess with orientation
sigma in {1,-1} gives integral_J 2Lw(sigma B_for-D0)>0;
since 2Lw>0, the set where sigma B_for>D0 has positive measure.
Failure of this signed-integral test gives no pointwise PSD verdict:
oppositely signed excursions can cancel in I_J.

The numerator has the following exact expression using only the
ordinary critical jets through order two and derivatives of the
already controlled bulk mean and Poisson weight:

    I_J=[tau x0^2-tau^2 S]_s^t
          -2 integral_J L tau x0 y0
          +integral_J tau^2(ell g_H'+2m1 m1')
          +integral_J (1-k)a'.                       (21)

Here [h]_s^t=h(t)-h(s), with the actual continuous endpoint values.
To verify (21), apply the AC product and integration-by-parts rules
imported in L449 from J. K. Hunter, *Notes on Partial Differential
Equations*, revision 18 June 2014,
[Definition 3.1 pp. 47--48 and Theorems 3.60, 3.62--3.63 pp. 79--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
and Jordan Bell, *Sobolev spaces in one dimension and absolutely
continuous functions*, 21 October 2015,
[Section 1, Theorem 1](https://jordanbell.info/LaTeX/mathematics/sobolev1d/).
Their
hypotheses hold for tau,x0,S,a and w at this fixed H. In particular
(x0^2)'=2L x0 y0, so integrating tau'x0^2 gives its boundary product
minus 2 integral L tau x0 y0. Integrating -(tau^2)'S gives the
second boundary product plus integral tau^2 S'. Substitute
S'=ell g_H'+2m1 m1'+a' and tau^2+w=1-k to obtain (21).
This proof includes every saturation boundary: tau is Lipschitz,
and the AC product rule introduces no singular boundary measure.
On an unsaturated J, tau=u/ell^6 may be substituted throughout.
The expression is an identity, not a sign estimate for its boundary
terms or its signed low-jet integral. It does not evaluate I_J for
an actual interval.

For clarity about the actual-data threshold, one sufficient interior
excursion can be quantified without a third-jet bound. There are
fixed constants C_S,C_T such that on [H+1,2H-1]

    |S|<=C_S ell^(9/8), 2LwD0<=C_T ell^(17/8).

These follow directly from (5)--(6), a=0 there, L<=2ell and w<=1.
Fix c in (0,1]. Suppose an actual nondegenerate interval J=[s,t] in
this interior has u monotone with {u(s),u(t)}={U,2U},
with U>0 and 2U<ell^6/sqrt(2),
and x0^2>=c u throughout J. Either orientation is permitted.
For sufficiently large H depending on c, 2C_S ell^(-39/8)<=c/2,
so on J

    x0^2-2tau S >= u(c-2C_S ell^(-39/8)) >= (c/2)u.

Let sigma=1 on an increasing crossing and -1 on a decreasing one.
Monotonicity of the smooth u implies sigma u'>=0, and a'=0 on J.
The AC chain rule gives

    sigma I_J >= c/(2ell^6) integral_J sigma u'u
                =3c U^2/(4ell^6),
    T_J<=C_T ell^(17/8)|J|.

It follows that the concrete length condition

    |J|<= c U^2/(4 C_T ell^(65/8))                    (22)

would give sigma I_J>=3T_J. After delta_H<1, (20) would then
certify positive-measure negative determinant on this actual J.
For example, at a proposed length bound |J|<=K/ell with fixed K>0,
(22) follows if U^2>=4C_T K ell^(57/8)/c; the jet magnitude at the
lower level is sqrt(U), of scale ell^(57/32). This is only an
algebraic comparison of required and available scales. It is not a
large-value theorem, a relative derivative bound, or a claim that
any monotone crossing with x0^2>=cu occurs at that scale.

The bounded attempt stops at that distinction. The inspected local
inputs provide upper jet envelopes, moment averages, the exact
fixed-H density, and pass regions. None of the results used here
asserts a monotone unsaturated crossing satisfying (22) with its
coordinate condition, or supplies an evaluated strict excess in
(19). Even a large value of u alone would leave its x0 proportion,
crossing duration, monotonicity and possible saturation unresolved.
Neither (21) nor the prior moment constraints sign the complete
boundary and integral expression on an actual component. No interval
or positive-measure violating set is certified, and no coverage of
the existing pass regions is added. The outcome is EXPLORATION,
not a new covariance verdict or a mathematical advance beyond the
checked sources. Further application of (22) needs separate source
coverage of an actual excursion input; this turn imports no such
input. The endpoint layers and all independent realization and RH
gaps also remain open. Repeating the pointwise absolute envelopes
or the unevaluated identity (21) would not resolve this bottleneck.

### Separate conditional critical audit — 2026-10-21, step 298

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-21-width-one-signed-test-critical-audit.md`.
It validates only (19)--(22), conditional on (1)--(6), L449 (9)--(12)
and L445's fixed-H regularity. It does not certify the earlier uniform
remainder proof, all of L449/L450, or occurrence of an actual excursion.
The endpoint-attainment wording above makes explicit the meaning of
the original U-to-2U crossing; mere containment U<=u<=2U is insufficient.

**Integrability and the signed test.** At a fixed sufficiently large H,
tau,x0,S,a,w are Lipschitz on the closed I. Their derivatives are
bounded a.e.; no bound uniform in H is needed for this calculus step.
The positive continuous A,C in (6) make D0=sqrt(AC) positive and
bounded on I. Thus all integrands in (19)--(21) are integrable and
W=2Lw is continuous and strictly positive, with T_J=integral_J W D0>0.
In particular, (1) makes B_for a bounded measurable a.e. function at
this fixed H. Multiplying (1)--(2) gives exactly

    W B_for=tau'(x0^2-2tau S)+w a'+W D0 eps_H.

The integral triangle inequality and |eps_H|<=delta_H give (20)
with its stated constant; there is no extra w or D0 factor missing.
If |I_J|>(1+delta_H)T_J, set sigma=sign(I_J). Then

    integral_J W(sigma B_for-D0)
        >= |I_J|-(1+delta_H)T_J > 0.

An integrable function nonpositive a.e. cannot have positive integral.
Since W>0, E={sigma B_for>D0} consequently has positive Lebesgue
measure, after discarding all null sets where derivatives or (1) fail.
On E, A C-B_for^2<0. This applies the positive-diagonal case of
Boyd--Vandenberghe, *Convex Optimization* (2004, corrected seventh
printing 2009), Appendix A.5.5, pp. 650--651, (A.13)--(A.14), cited
above. No continuity of B_for or determinant, singular Schur-complement
case, actual occurrence, or positive-measure set of H is asserted.

**Boundary and saturation check.** The AC product/integration rules in
Hunter, revision 18 June 2014, Definition 3.1 pp. 47--48 and Theorems
3.60, 3.62--3.63 pp. 79--80, with Bell, 21 October 2015, Section 1
Theorem 1, have precisely the fixed-H hypotheses verified above. For
P=tau x0^2-tau^2 S their product rule gives a.e.

    P'=tau'(x0^2-2tau S)+2L tau x0 y0-tau^2 S'.

Integrate from s to t, use the actual continuous endpoint values, and
insert S'=ell g_H'+2m1 m1'+a'. Adding integral_J w a' leaves the
coefficient tau^2+w=1-k of a', proving every sign and term in (21).
A_H,mu and ell are constant in t. Neither M12 nor any selected atom
is differentiated. The minimum defining tau is Lipschitz, including
u=0 and u=ell^6/sqrt(2), so its AC derivative has no singular part.
The equality set has tau'=0 a.e. as explained in L449; no additional
interface endpoint terms are permitted or needed in this product rule.

**Excursion constants and quantifiers.** In the interior a=a'=0;
(5)--(6), w<=1 and L<=2ell give fixed positive C_S,C_T with the two
displayed bounds preceding (22), uniformly in the original stage.
Fix c>0 before increasing H. Since tau=u/ell^6 on the assumed
crossing, the lower bound for its signed factor is

    x0^2-2tau S >= u(c-2C_S ell^(-39/8)) >= c u/2

as soon as ell^(39/8)>=4C_S/c, in addition to the earlier onsets.
Smooth monotonicity gives sigma u'>=0, including any flat portions.
The endpoint values, not just a range restriction, then give

    integral_J sigma u'u=|u(t)^2-u(s)^2|/2=3U^2/2,
    sigma I_J>=3cU^2/(4ell^6).

Under (22), T_J<=cU^2/(4ell^6), because 65/8-17/8=6. Hence
sigma I_J>=3T_J>(1+delta_H)T_J once delta_H<1. This proves the
claimed positive-measure failure in either crossing orientation.
At duration K/ell the sufficient comparison is exactly
U^2>=4C_T K ell^(57/8)/c; sqrt(U) consequently has threshold scale
ell^(57/32) for fixed c,K,C_T. These are sufficient conditional
thresholds only. If c varies with H, the stated fixed-c onset does
not supply uniformity without its explicit inequalities being checked.

The scoped audit passes without changing a coefficient, inequality,
argument or direct input. It independently validates a reusable local
conditional certificate by known calculus and matrix tools; it supplies
no mathematical progress beyond those sources, actual violating
interval, new pass coverage, width-one verdict or RH consequence.
The unsupported actual-excursion application remains parked. Earlier
remainder bounds, other temporal/mean identities, endpoint layers,
global realization, clipping and the regulator margin remain open.

### Separate remainder/pass critical audit — 2026-10-21, step 300

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-21-width-one-remainder-pass-critical-audit.md`.
This audit validates (1)--(15) for the unchanged width-one family.
It uses L449's endpoint amplitude/recentering bounds and exact scalar
formulas as stated inputs; it is not an audit of that lemma's full
selected-constraint construction. The response derivative proof cases
in L448 used here precede its narrow-layer argument and contain no
endpoint-width dependence. The older conditional audit of (19)--(22)
did not validate the present estimates; the following check does so.

**Uniform inputs and the full diagonal.** All constants below are
independent of the original stage and of t in [H,2H], after one common
onset on the original real-H ray. L438 (12)--(15) give w>=1/4,
1/2<=N_H<=2, bounded d_H, ||A_H||<=C sqrt(ell) and the bounds on
g_H in (5). The old occupation repairs and L449's recomputed correction
F have zero diagonal; the endpoint field (a-mu)K is retained explicitly.
Write b=ell g_H+a and

    A=b+e1, C=b/12+e2,
    e1=(A_H)11-mu, e2=(A_H)22-mu/12.

L449 (1) gives |e1|+|e2|<=C sqrt(ell), while b>=ell^(7/8)/2
because a>=0. Thus |e1/b|+|12e2/b|<=C ell^(-3/8). Increase H
so both ratios have modulus at most 1/2. Both diagonals are positive,
and taking the square root of

    AC=(b^2/12)(1+e1/b)(1+12e2/b)

gives precisely (6), with one uniform constant. Also S=A+m1^2,
and bounded m implies |S|<=C b. No upper log-power bound on a was
used: this is why the estimate remains valid at an arbitrarily large
allowed endpoint peak. The small weighted recentering mu is included.

**Quantitative branch check.** L448's response calculation uses
U=Gamma(1/4+it/2)/|Gamma(1/4+it/2)| times pi^(-it/2) and
G/A_env=Re[P2 U zeta(5/2+it)], with the stated quadratic P2.
Its disks of radius 1/8 have positive real part and eventually lie
in |arg z|<=3pi/4. The log-gamma/psi expansions and complex remainder
in [DLMF 5.11.1--2 and 5.11(ii)](https://dlmf.nist.gov/5.11),
[Cauchy's formula 1.9.30--31](https://dlmf.nist.gov/1.9.E31) and
[gamma recurrence 5.5.1](https://dlmf.nist.gov/5.5.E1) therefore apply.
As checked there, U^(j)=O(ell^j) through j=3, and every needed
right-line derivative is bounded by sum_n (log n)^j n^(-5/2)<infinity.
Consequently (G/A_env)^(j)=O(H^2 ell^j) through j=3. In particular,
for the response coordinates (distinct from the critical v3),

    v_j'=(G/A_env)^(j+1)/(T^2 L^j)
                         -v_j(2/T+j L'/L), j=0,1,2,

is O(ell). The same gamma calculation controls e'. L445's exact
polynomial response coefficients b and C consequently have derivatives
O(ell), with bounded values. This uses no third critical-jet moment,
critical-line lower bound, or derivative in H.

For the positive branch, use M=max(|b.c1|,|b.c2|) and
h_+=(M^2-4C E_*)M from L445 (2). The scalar M is O(ell)-Lipschitz
across both same-sign and opposite-sign projection ties. Bounded
coefficients, E_*=-1/3-4e/9 and h_+>=h_min>0 show that h_+ and
its reciprocal have Lipschitz constants O(ell). The two candidates
have identical first-coordinate square 4/9, including after reversal.
No derivative of their selected first coordinate is required.

For the negative branch write U_-=(a+h,(a-h)/2,-(a+h)/4), using
the response carrier a+ih, unrelated to the endpoint bump a(t).
L445 gives |U_-|>=zeta(5/2)^(-1)/sqrt(2). The carrier derivative
is O(ell), so differentiation of n_-=U_-/|U_-| gives
n_-'=(Id-n_-n_-^T)U_-'/|U_-|=O(ell). The exact polynomial forms
for D,B and the strictly positive h_- margin give the same reciprocal
bound for h_-. Thus neither branch hides division by a projection
that could vanish.

The smooth torus functions in F_H=beta W_3+a_H^T phi are fixed.
L438 (6) gives a_H->0, so their temporal C^1 norms are uniformly
bounded; the velocities log 2, log 3 and log 5 are fixed. Taking
positive/negative parts preserves the Lipschitz bound, including
their zero sets. Applying the product rule a.e. to (7) now gives
|k'|<=C ell^(-3/2) and |M11'|<=C ell^(3/2), with both masses
included. Since each n_s is a unit vector, its full intermediate
raw matrix has norm sqrt(ell) F_s/h_s. This proves (9) at every
tie as well, without differentiating M12. Finally bounded d_H and
|b|>=b_min give

    m'=d_H[b'/|b|^2-2b(b.b')/|b|^4]=O(ell).

Together with L>=ell this verifies the full translated expression
(10), not just the derivative of m1^2.

**Cutoff and exact subtraction.** L444 (17) and its separate audit
apply to the same finite product: y<=ell^(1/4), P_j<=ell^(1/8).
Each positive denominator is at least (1-1/sqrt(2))^2, so
|(log P_j)'|<=C y log(2+y). Division by the t-constant N_H>=1/2
gives ||g_H'||<=C ell^(3/8)log ell. This bound uses every retained
prime and is valid even when H is exactly a stage threshold; only t
is differentiated. It is a finite-product calculation, not a limiting
Euler-product assertion.

Directly from L449 (9), at almost every t,

    q'=tau' x0^2+2L tau x0 y0+M11'
                              +(-2tau tau'-k')S+wS'.

Subtract R12=tau x0 y0+M12 after dividing q' by 2L, then divide
by w and subtract m1 m2. Substituting S'=ell g_H'+2m1 m1'+a'
leaves exactly (2) and (12). In particular, the high mass derivative
has coefficient -2tau S and remains in (2); both intermediate mass
derivatives have coefficient -S and remain in (12). Neither the
normalization, translation nor the endpoint derivative is lost.

Using the bounds just verified, the four kinds of remainder divided
by D0 are respectively at most

    C ell^(1/2)/b,
    C ell^(-5/2)|S|/b,
    C ell^(3/8)log ell/b,
    C/b.

Here the first includes both M11'/(2Lw) and -M12/w. With
b>=ell^(7/8)/2 and |S|<=C b these become
C[ell^(-3/8)+ell^(-5/2)+ell^(-1/2)log ell+ell^(-7/8)].
Since ell^(-1/8)log ell is bounded eventually, (13) and hence (1)
follow with a stage-independent C0. Large endpoint amplitudes cancel
in the second ratio instead of being replaced by an interior estimate.

**Interior regions and quantifiers.** The fixed bump has a=a'=0
throughout [H+1,2H-1], including its two boundary points. The Lipschitz
minimum tau is constant on the open saturated set. At nonisolated
points of the equality set a differentiable u has u'=0; isolated
points are countable. The Lipschitz chain rule therefore gives
tau'=0 a.e. on the entire set (3), with no singular derivative mass.
Thus V_H=0 there. This uses the fixed-H AC calculus of Hunter,
revision 18 June 2014, Definition 3.1 pp. 47--48 and Theorems 3.60,
3.62--3.63 pp. 79--80, cited above, and the explicit branch formulas.

For (4), ordinary quotient differentiation gives exactly

    (f'/L)'/L=f''/L^2-(L'/L^2)(f'/L),
    (f''/L^2)'/L=f'''/L^3-2(L'/L^2)(f''/L^2).

Thus (14) has the correct ordinary third jet and both moving-scale
terms. On this region |u'|/L<=C ell^3 and u<=ell^3, so eventually
tau<=ell^-3 and |tau'|/L<=C ell^-3. The interior bound
|S|<=C ell^(9/8) gives

    |tau'(x0^2-2tau S)/(2Lw)|
                 <=C[1+ell^(-39/8)]=O(1).

This verifies (15). Dividing by D0>=c ell^(7/8), and adding (13),
gives the asserted relative cross bound on (4). No upper bound on the
actual third jet outside this condition, measure estimate for the
condition, or assertion that it ever holds has entered the proof.

For both regions one common eventual onset makes |B_for|/D0<=1/2.
The positive-diagonal scalar criterion of Boyd--Vandenberghe,
*Convex Optimization*, corrected seventh printing 2009, Appendix
A.5.5 pp. 650--651 (A.13)--(A.14), cited above, then gives determinant
AC[1-(B_for/D0)^2]>=3AC/4>0. For the fixed-epsilon tests, choose
C0 ell^(-3/8)<epsilon/2; the ordinary and reverse triangle
inequalities give the two strict conclusions with the stated a.e.
qualification. There is no singular-diagonal case here.

The audit passes without changing the argument, coefficients or direct
mathematical inputs. It removes the earlier-remainder assumption from
the step-298 local certificate, relative to the stated L449 inputs.
This is critical validation of a known-tool specialization, not a new
theorem beyond the sources checked. The full L449 construction still
needs its own audit. Actual crossings, coordinate proportions and
duration, all remaining layers, other temporal/mean identities and
global realization remain unresolved. Neither PSD of the full 3-by-3
covariance nor a width-one verdict, clipping, regulator margin, global
mixed positivity or an RH consequence follows.

## Mathlib

Full matching coverage of this law-specific relative remainder and
interior block comparison has not been checked. The named analytic
and Schur-complement results support the proof; no formalization of
the complete conditional law is asserted. Matching coverage of the
step-295 envelope calculation and step-296 signed-interval specialization
is also unchecked. Unknown coverage is not
evidence of absence. No numerical test or mathematical script is used.
Matching formal coverage of the scoped step-298 conditional audit is
also unchecked; the precise supporting AC and matrix citations above
are informal inputs, not a claim of a matching Mathlib theorem.
Matching formal coverage of the scoped step-300 audit is also unchecked.
