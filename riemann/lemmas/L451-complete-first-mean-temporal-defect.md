# Lemma 451: the unchanged complete first mean violates temporal transport

## Hypotheses

Use exactly L449's complete conditional law on its eventual ray of real
H, with L438's high and both signed intermediate components, remaining
mass w, translation m, full actual response and original L429 cutoff.
No probability, branch, integrated parameter or covariance is changed.
Write ell=log H, L(t)=log(2+t), E_H=H^(-1) integral_[H,2H], and

    M_H(t)=p(t)Y(t)+k_+(t)Z_+(t)+k_-(t)Z_-(t)+w(t)m(t).

This is the complete first mean, because the six-state bulk has mean m.
All H-dependent parameters are held fixed during temporal differentiation.
The ordinary trajectory coordinates obey x'=Ly. No actual critical-jet
crossing, regularity of selected atoms, or realization is assumed.

Use the response notation of L419 and L440:

    a+ih=R zeta(5/2+it)=rho exp(i alpha), c=1/(4pi),
    b0=zeta(3)/(4pi), m=d_H b/|b|^2,
    d_H=(-b0-J_R)/W_H, W_H=E_H w.

Here R is the unit gamma phase, not a rare second-moment matrix;
h is the imaginary response coordinate, not either cubic denominator.
The exact b includes curvature as in L419. The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-21-complete-first-moment-temporal-compatibility.md`.
This is a REPRODUCTION of the assessed occupation test and existing
response estimates specialized to this law, not a new general theorem.

## Conclusion

Define one fixed nonnegative C1 cutoff by

    eta(u)=960 (u-5/4)^2 (7/4-u)^2, 5/4<=u<=7/4,
    eta(u)=0 otherwise,
    phi_H(t)=eta(t/H) h(t)/L(t).

Then phi_H belongs to C_c^1((H,2H)), and the complete residual satisfies

    R_H:=E_H[phi_H'(M_H)_1+L phi_H(M_H)_2]
         =zeta(3) kappa+O(1/log H),                         (1)

where the fixed number

    kappa=(1/(2pi)) integral_0^(2pi)
       [sin(theta)^2-cos(theta)^2/8]/
       [(17/16)cos(theta)^2+sin(theta)^2] dtheta
       >=111/272>0.                                      (2)

Consequently R_H>=111 zeta(3)/544 for every sufficiently large real H.
In particular (M_H)_1'=L(M_H)_2 fails in distributions on each such
(H,2H). The conclusion concerns the complete sum, not isolated values
or jumps of a chosen atom. It does not claim that M_H has no AC
representative; even AC would not repair this nonzero residual.

This stops an eventual-ray realization with these complete means fixed,
including changes only to centered covariance. It leaves L449's selected
constraints valid. Other means or laws, the separate derivative-forced
covariance problem, actual clipping, capped nondegeneracy, L413's margin,
global mixed positivity and RH remain unresolved. The separate step-306
critical audit below validates this specialization; no RH candidate is asserted.

## Proof

### Imported identity and the law-specific specialization

The necessary occupation identity is J. B. Lasserre, D. Henrion,
C. Prieur and E. Trelat, *Nonlinear optimal control via occupation
measures and LMI-relaxations*, SIAM J. Control Optim. 47 (2008),
1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), printed pp. 3--5.
As in L443 (2), the finite-interval dynamics have x'=Ly. Use the
linear state test phi(t)x, with compact temporal support. On each
fixed interval the smooth response and bounded conditional states
permit finite compact boxes; no H-uniform box or converse is used.
Its derivative is phi'x+L phi y, and taking conditional expectations
gives the identity whose complete residual is (1).

Distributional derivatives use locally integrable representatives,
as in J. K. Hunter, *Notes on Partial Differential Equations*, revision
2014-06-18, [Definition 3.1, printed p. 47](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
We compute the residual directly and need no prior AC assertion.
The cited general identity is not reproved; the complete signed mean,
test, error bounds and nonzero coefficient below are the specialization
not supplied by that source. L445's raw-second regularity is a contrast,
not an inference about this first mean.

### Absolute control of every signed component

L449 retains all probabilities and the mean m exactly. Its changed
endpoint covariance and both basis selections contribute no further
term to M_H. L438 (9)--(12) give, uniformly through real H,

    E_H p=O(ell^-8), E_H[p|Y|^2]=O(ell^-2),
    E_H[k_+|Z_+|+k_-|Z_-|]=O(ell^-1),
    E_H(1-w)=O(ell^(-5/2)), J_R=O(ell^-1),
    W_H=1-O(ell^(-5/2)).                                  (3)

These are the full masses with F_H's two signed parts and both positive
h denominators. The high estimates include both r branches, its sign
rule and its zero convention. Cauchy--Schwarz with measure p dt/H gives

    E_H[p|Y|]<=sqrt((E_H p)(E_H[p|Y|^2]))=O(ell^-5).

Thus no sign orientation is needed to bound the high first mean.
L419's uniform lower bound for |b| and (3) imply

    d_H=-b0+O(ell^-1), ||m||_infinity<=C,
    E_H|M_H-m|
      <=E_H[p|Y|+k_+|Z_+|+k_-|Z_-|+(1-w)|m|]
       =O(ell^-1).                                      (4)

This retains the complete mass loss in w and the complete rare integral
J_R in d_H. The bounds hold without differentiating any of those terms.
In particular they do not assume that a jump is isolated, that switches
occur, or that signed cancellations fail at a particular point.

### Response probe, including its complete derivative

L440 (13), with its separate step-259 audit, gives

    0<rho_min<=rho<=rho_max, |rho'|<=C,
    alpha'=ell/2+O(1), |alpha''|<=C.                       (5)

These are uniform on [H,2H] for all sufficiently large real H. They
come from the absolute right-line series through two derivatives, its
Euler-product lower bound, and the gamma phase bounds; they involve no
critical-line division. Since L=ell+O(1), differentiating the exact
h=rho sin alpha gives

    h'/L=(rho' sin alpha+rho cos alpha alpha')/L
         =a/2+O(ell^-1).                                 (6)

No derivative of an asymptotic response error is taken.

The polynomial cutoff and its first derivative vanish at both ends of
[5/4,7/4], so its zero extension is C1 and its support is strictly
inside (1,2). Substitution v=u-5/4 gives
integral eta=960 integral_0^(1/2) v^2(1/2-v)^2 dv
=960 (1/2)^5/30=1. Put e_H(t)=eta(t/H). Exactly,

    phi_H'=e_H' h/L+e_H h'/L-e_H h L'/L^2,
    L phi_H=e_H h.                                       (7)

Here e_H'=eta'(t/H)/H and L'=1/(2+t). Equations (5)--(7)
therefore imply, uniformly on the whole interval,

    phi_H'=e_H a/2+O(ell^-1),
    ||phi_H'||_infinity+||L phi_H||_infinity<=C.           (8)

The support is contained in [5H/4,7H/4], so no endpoint contribution
is hidden. Combining (4) and (8) shows that replacing M_H by m in
the complete residual costs O(ell^-1), in absolute value.

### The bulk contribution and its signed angular mean

L419's complete response estimate gives

    b=b_*+O(ell^-1), b_*=c(a/4,-h,-a),
    |b_*|^2=c^2 D_*, D_*=(17/16)a^2+h^2.

Both |b| and |b_*| have fixed positive lower bounds. Boundedness of
b,b_* and the exact difference of their reciprocal squared norms
give b/|b|^2=b_*/|b_*|^2+O(ell^-1). Thus

    m_1=(d_H/c)a/(4D_*)+O(ell^-1),
    m_2=-(d_H/c)h/D_*+O(ell^-1).                         (9)

The curvature has not been discarded from the definition of m; its
contribution is contained in this uniform O(ell^-1) comparison.
Equations (7)--(9) and the absolute comparison above give

    R_H=(d_H/c) E_H[e_H g(alpha)]+O(ell^-1),
    g(theta)=[cos(theta)^2/8-sin(theta)^2]/
             [(17/16)cos(theta)^2+sin(theta)^2].          (10)

The response amplitude rho cancels exactly in this ratio. In particular
no independence of a prime phase and a gamma phase is asserted.

Apply the already proved zero-angle-mean bound L440 (14) to the fixed
smooth periodic function g-<g> and the amplitude e_H. Its value and
temporal derivative are uniformly bounded, as required there; (5)
supplies the needed phase speed and second derivative. Consequently

    E_H[e_H g(alpha)]=<g> E_H e_H+O(ell^-1)
                    =<g>+O(ell^-1).                    (11)

This uses the full actual response angle. It does not invoke a new
equidistribution theorem, add a test to L429's stages, or take a
subsequence of heights. For completeness the strict sign follows
without a numerical angular integral: the denominator in (10) lies
between 1 and 17/16, whence

    <g><=<cos^2>/8-(16/17)<sin^2>
         =1/16-8/17=-111/272.

Set kappa=-<g>. Since d_H=-b0+O(ell^-1) and b0/c=zeta(3),
(10)--(11) give exactly (1)--(2). Every error constant is fixed
independently of H and of the unchanged cutoff stage. Increasing one
onset makes its absolute error at most 111 zeta(3)/544, proving the
asserted positive lower bound for every real H beyond that onset.

### Distributional meaning and limitations

The full mean and L times its second coordinate are integrable on each
fixed interval by (3)--(4) and the fixed-H envelopes. If the weak
identity held, its test functional would vanish on every smooth compact
test. The C1 test phi_H can be mollified inside (H,2H), with both the
function and first derivative converging uniformly and support staying
compactly inside that interval. Integrability makes the residuals
converge. Hence a nonzero residual for phi_H also yields a nonzero
residual for some smooth compact test at that fixed H. This is a
distributional defect, unaffected by changing null-set values.

The achieved threshold is a fixed positive normalized residual against
the required exact zero, not merely a regularity observation or an
individual atom's jump. It persists for any law with these same complete
means, whatever centered covariance is used. Nothing here excludes
altering the means while preserving the older integrated constraints.
No trajectory sufficiency, actual clipping sign or RH implication follows.

### Separate critical audit — 2026-10-21, step 306

**Verdict and scope.** Equations (1)--(2), the positive eventual bound,
and the distributional fixed-mean obstruction pass under the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-21-complete-first-mean-defect-critical-audit.md`.
This is independent verification of a local known-tool specialization,
not a new general occupation theorem or an RH result. The following
checks retain the actual law; no rescue change to its means or probe is
made. The exact coefficient and error rate in the conclusion are unchanged.

**Complete mean, branches and bounds.** L449's audited construction
changes only centered covariance. Each pair m+xi_i,m-xi_i has mean m,
including both equality and strict-straddling choices at both basis
selection stages. Thus its complete mean is exactly the sum in the
hypotheses, independently of endpoint peaks or basis discontinuities.
L443 uses these same means and the dynamics x'=Ly; it does not impose
an additional drift on x from the normalization of y.

Tracing L438 (9)--(12) back to its retained high kernel gives, for
rho0=|X0|>0, p=(rho0/r)^4 and |Y|=r, with
r=max(ell^3,2^(1/4)rho0). Consequently p|Y|^j=rho0^4/r^(4-j)
for j=0,1,2; the zero branch contributes zero. The inherited actual
fourth-moment bound gives the absolute costs ell^-8, ell^-5 and
ell^-2, respectively. These include the saturated branch p=1/2,
the equality boundary, and both choices of its sign orientation.
No uniform smallness of p is needed. This also verifies directly the
Cauchy--Schwarz first-moment estimate used in (4).

For both signed intermediate parts, |Z_s|=ell^(3/2),
k_s=ell^(-5/2)(F_H)_s/h_s, and h_s has a fixed positive lower
bound at the exact response. L438's uniform bound on F_H therefore
gives total first absolute cost O(ell^-1) and total mass
O(ell^(-5/2)), even at response projection zeros, F_H zeros and
direction-selection ties. Boundedness of the exact b gives
|J_R|=O(ell^-1) for the complete signed sum. Hence
W_H=1-O(ell^(-5/2)) and

    d_H+b0=(-J_R+b0(W_H-1))/W_H=O(ell^-1).

L419's exact curvature-inclusive b stays bounded away from zero.
It follows that m is uniformly bounded and that (4) includes every
rare contribution and the entire term (w-1)m. No covariance correction
enters this calculation. The estimates use only fixed uniform bounds
on F_H and the response, not a rate for its finite-height Gram limit.

**Probe, normalization and sign.** The cutoff has integral one,
because integral_0^d v^2(d-v)^2 dv=d^5/30 with d=1/2.
Its function and first derivative vanish at its two support endpoints.
Equation (7) includes both the derivative of eta(t/H) and the derivative
of L. L440 (13) supplies h'/L=a/2+O(ell^-1) with positive sign:
the full angle has alpha'=ell/2+O(1), and the separate rho' term is
O(ell^-1). Thus the error caused by (4) is at most
(||phi_H'||_infinity+||L phi_H||_infinity)E_H|M_H-m|
=O(ell^-1). This step never differentiates the rare components.

With b_*=c(a/4,-h,-a), its squared norm is c^2((17/16)a^2+h^2).
The reciprocal-norm comparison is uniform because both norms have
fixed positive lower bounds. The numerator from phi'_H m_1 is
a^2/8; that from L phi_H m_2 is -h^2. Their sum is exactly g in
(10) after cancelling rho^2. The positive a/2 derivative sign and
negative second coordinate of b_* are both essential here.

The function g is smooth and fixed, its denominator lies in [1,17/16],
and e_H has uniformly bounded value and derivative. These meet every
hypothesis of the already audited L440 (14). Its angular primitive is
bounded independently of H; no prime/gamma independence is used.
Pointwise, cos^2/(8D)<=cos^2/8 and -sin^2/D<=-16 sin^2/17.
Averaging therefore gives <g><=1/16-8/17=-111/272.
Multiplying by d_H/c=-zeta(3)+O(ell^-1) proves precisely (1).
The required trajectory residual is exactly zero, whereas the proved
lower bound is 111 zeta(3)/544 beyond one fixed onset.

**Distributional test class and all real heights.** For fixed H the
finite-height envelopes bound every atom; their Borel branches are
measurable. In particular M_1 and L M_2 are integrable. Extend phi_H
by zero to the real line. It is C1 with support in [5H/4,7H/4].
Use a nonnegative smooth unit-mass mollifier supported in [-epsilon,
epsilon], with epsilon<H/8. Hunter, *Notes on Partial Differential
Equations*, revision 2014-06-18, Section 1.9 (1.5)--(1.8), Theorem
1.28 and its proof, printed pp. 11--12 at the cited PDF, supplies
smooth convolution and its differentiation formula. The specialization
to C1 convergence does not follow just from the theorem's Lp statement:
uniform continuity of each compactly supported function phi_H and
phi_H' bounds its convolution error by its modulus of continuity at
epsilon. Both sup-norm errors therefore tend to zero, and the smoothed
support remains strictly inside (H,2H).

For the corresponding smooth test psi, the residual difference is at
most

    E_H|M_1| ||psi'-phi_H'||_infinity
      +E_H|L M_2| ||psi-phi_H||_infinity.

Thus some smooth compact test retains the strict positive residual at
each fixed H. No approximation rate uniform in H is required to refute
the distributional identity separately on each interval. The ensemble
occupation identity is only necessary; no converse is imported.

The asymptotic bound itself is uniform in H: the fourth-moment constants,
direction margins, bound on F_H, response annulus and derivative bounds
all precede H. No estimate differentiates j(H), d_H or an integrated
parameter in H, nor uses continuity across stage thresholds. Taking
the maximum of their finitely many onsets proves the stated result for
every sufficiently large real H, including those thresholds. This audit
neither assumes nor proves AC of the complete mean. It validates the
fixed-mean stop without settling the independent forced covariance
block, changing a selected constraint, or excluding changed means.

## Mathlib

Full matching coverage for this constructed law and temporal defect has
not been checked. The occupation and weak-derivative inputs are imported
by the precise citations above; the response and angular estimates are
the local results explicitly used in the proof. No absence claim or
formal verification is asserted.
