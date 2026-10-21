# Lemma 418: a capped rare component at the prescribed response, not a feasible full law

## Hypotheses

Use exactly the actual height/response graph, definitions and actual
critical triple X0(t) of L417, with uniform measure dt/H on [H,2H].
Write ell=log H, rho(t)=|X0(t)|, B(t)=Bcal(X0(t);t) and
D(t)=Delta(X0(t);t). Here D denotes normalized Delta. The response
and the envelope conversion, including curvature, are fixed at t.
Only the critical triple of an output state can change.

Import L390's actual fourth-moment bound, L406's actual absolute
third-moment bound, and the uniform polynomial bounds from L414's
conversion at L390's complete actual response:

    E rho^4=O(ell^4), E rho^3=O(ell^(9/4)),
    |Bcal(X;t)|<=C|X|, |Delta(X;t)|<=C|X|^2.

The last two bounds hold for every critical X at the actual response,
with one constant on the eventual ray: the exact converted response
and conversion coefficients are bounded. The actual response satisfies
the required annulus, Ccal lower bound and qualitative bounds. The
actual critical jets have the qualitative pointwise bounds of L414.
The actual 23 quartic moments have the coefficients recorded in L416.
No conditional moment or distributional limit is assumed.

Fix lambda>0 independently of H and put M=lambda ell^2. This is an
additional radial construction, not a restriction on all allowable
conditional laws in the approved step-150 SPECIALIZE assessment.

## Conclusion

There is an explicit supported subprobability kernel at every actual
height, of total integrated mass O(ell^(-4)), preserving all 23 actual
quartic observables exactly pointwise. It preserves the actual U^2
integrand as well. Its integrated critical second-moment matrix is
positive semidefinite with trace O(1); its first Delta and Bcal integrals
are respectively O(1) and O(ell^(-2)). Its two absolute power-three
integrals satisfy the required O(ell^(9/4)) bounds.

Every fiber has mass at most one. Completion by the zero critical
triple gives a measurable probability kernel with the exact uniform
height marginal and actual response, avoiding {Delta>0,Bcal<0} and
obeying every pointwise bound with fixed constants and one onset.
This completion does NOT satisfy the full moment list: it lacks the
leading second moments and the negative first Delta mean.

The rare component's cubic integral is exactly

    F_lambda(H)=E[ |D B| min(1,rho/(lambda ell^2)) ].       (1)

The construction proves only 0<=F_lambda(H)=O(ell^2), not the required
F_lambda(H)=beta_* ell^2+o(ell^2). Any complementary bulk supported
on |X|<=C_b sqrt(ell), for fixed C_b, adds only O(ell^(3/2)) to the
cubic. Thus this particular maximally oriented rare/bounded-bulk
implementation requires that equality in (1). It has not been proved.
This is a partial implementation and an unresolved calibration test,
not a full feasible law, a separator, an actual clipped statistic or
an RH consequence. The separate step-159 critical audit below validates
these partial assertions, without evaluating the missing cubic.

## Proof

This is the conditional rare/bulk test within the unchanged step-150
SPECIALIZE assessment. The capped construction is written out because
the inspected selection/purification results do not construct its
moments. POTENTIALLY_NEW records that limited comparison, not certified
originality or a new zeta-moment theorem. No general theorem from that
assessment is reproved or needed as an existence premise here.

### Kernel, exact support and fiber mass

For rho>0 set r=max(M,rho), n=X0/rho, p=(rho/r)^4, and

    s=1 if D B>=0, s=-1 if D B<0;  Y=s r n.

At rho=0 set p=0,Y=0. The rare kernel is p(t) delta_(Y(t)).
These are Borel functions of continuous actual data on a compact
interval; the definition at zero removes division by zero. In
particular 0<=p<=1, even where actual jets exceed M.

The conversion P(X;t) is linear in X at fixed t. Exactly, Bcal is
linear, Delta quadratic, omega linear, and U quadratic in X. Hence,
where rho>0,

    Bcal(Y;t)=s(r/rho)B, Delta(Y;t)=(r/rho)^2 D.

If D>0 the chosen sign makes output Bcal>=0. If D<=0 the output
Delta is nonpositive. Thus every rare state avoids the forbidden
joint sign, including both boundaries. All response derivatives and
q=(log A)'' are unchanged; these are exact homogeneity identities,
not leading-response replacements.

The zero critical triple also lies in the allowed support. Therefore

    nu_t=p(t) delta_(Y(t))+(1-p(t)) delta_0

is an explicit measurable probability kernel. Its fiber mass is one,
so integrating against dt/H retains precisely that height marginal.
No selection, purification or atomic-replacement theorem is needed.
The framework from the saved assessment is reused without reproof.

### Quartics, smaller moments and absolute bounds

For every homogeneous polynomial Q of degree four in the critical
coordinates, at this same fixed response,

    p Q(Y;t)=Q(X0;t).                                  (2)

Indeed the four powers of s cancel and p(r/rho)^4=1. At rho=0 both
sides vanish. Apply (2) to Delta^2, Delta Bcal^2 and all 21 products
Delta omega_i omega_j, including their signed off-diagonal entries.
This preserves their exact actual integrands, not merely the limits
or a selected submatrix. It also applies to U^2=|X|^4.

Let unnormalized rare integrals mean E[p times the indicated output
quantity]; do not divide by E p. Direct calculation gives

    E p <= E rho^4/M^4 = O(ell^(-4)),
    Q_ij:=E[p Y_i Y_j]=E[(rho^2/r^2) X0_i X0_j],
    tr Q=E[rho^4/r^2] <= E rho^4/M^2=O(1),
    E[p Delta(Y;t)]=E[(rho^2/r^2)D]=O(1),
    E[p Bcal(Y;t)]=E[s(rho/r)^3 B]=O(ell^(-2)).       (3)

For the last two bounds use |D|<=C rho^2, |B|<=C rho
and respectively r>=M, r^3>=M^3. The second matrix is positive
semidefinite because it is an integral of nonnegative multiples of
X0 X0^T. Each of its entries has absolute value at most its trace.
None of (3) asserts that its two odd entries meet the tiny final
errors: a later bulk would have to cancel those entries accurately.

Furthermore

    E[p |Y|^3]=E[rho^4/r]<=E rho^3=O(ell^(9/4)),
    E[p |Bcal(Y;t)|^3]<=C E[p |Y|^3].                (4)

Thus both required absolute power-three envelopes hold; E U^2 is
exactly the actual O(ell^4). The zero completion adds nothing to any
of these observables. Every moment is absolutely integrable for each
fixed H: actual data are bounded on the compact interval and the
constructed output norm is at most max(M,sup rho).

### Fixed pointwise bounds

On rho>=M the output is s X0, so the critical physical-jet absolute
bounds equal the actual ones. On 0<rho<M its norm is M. Bounded
alpha,q and L>=1 make L414's conversion matrix uniformly bounded,
so |P_j(Y;t)|<=C_lambda ell^2 there. Uniformly for H<=t<=2H,

    ell^2 L(t)^j/T(t)^(1/2) -> 0, j=0,1,2.

These small-jet branch bounds therefore meet the qualitative bounds
after one onset, with constants enlarged once if needed. At the zero
state they hold trivially. Response coordinates, jets, annulus, error
bounds and Ccal remain the actual ones on both branches. All constants
may depend on fixed lambda, but not on H. This proves the stated
pointwise and uniform claims for every sufficiently large real H.

### The missing cubic and bulk obligations

The chosen sign satisfies s D B=|D B|, whence exactly

    E[p Delta(Y;t) Bcal(Y;t)]
       =E[(rho/r)|D B|]=F_lambda(H).

Its upper bound follows from |D B|<=C rho^3 and r>=M:

    F_lambda(H)<=C E[rho^4/r]<=C E rho^4/M=O(ell^2).

Neither this inequality nor L409's sourced signed cubic E(DB)=beta_*
ell^2+o(ell^2) evaluates (1). The multiplier rho/r is correlated with
the actual jets. It cannot be removed using a conditional independence
assumption or the known unweighted second/fourth moments. No lower
asymptotic or separating gap for this actual integral is asserted.

For any proposed complementary probability kernel mu_t, supported
on |X|<=C_b sqrt(ell), the unnormalized bulk is (1-p)mu_t. Uniform
polynomial bounds give |Delta(X;t)Bcal(X;t)|<=C|X|^3. Therefore its
integrated cubic absolute value is at most C C_b^3 ell^(3/2), which
is o(ell^2). Its quartic absolute contributions are O(ell^2), so such
a bulk would preserve (2)'s quartic leading coefficients. It cannot
repair a missing leading coefficient in (1). Its second-moment,
first-Delta and first-Bcal calibrations are also not supplied here.

In fact the zero completion has E x^2=O(1), inconsistent with
ell+O(1), and E Delta=O(1), inconsistent with -a_* ell+o(ell).
It is explicitly not the desired full law. Allowing other rare
orientations, critical directions or only integrated quartic
preservation is outside this ansatz, but remains within the approved
general feasibility problem. L417's sign-only failure and L416's
different-response construction are not superseded.

This bounded attempt ends without evaluating (1) or constructing the
bulk. It gives no actual/global critical realization, clipped estimate,
regulator margin, common-zero control or mixed positivity.

### Separate critical audit — 2026-10-16, step 159

This REPRODUCTION proof_audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-16-prescribed-response-rare-critical-audit.md`.
All stated partial assertions pass. This supplies independent local
verification, not a new moment theorem, an evaluated cubic coefficient
or a full feasible law. L419's previous audit checked the rare inputs
it used; here the entire statement, including zero completion, both
cap branches and all noncubic bounds, is checked in its own scope.

**Imported bounds and normalization.** L390's actual fourth-moment
input is the fixed-order Hardy bound from H. M. Bui and R. R. Hall,
*On the derivatives of Hardy's function Z(t)*, Bull. Lond. Math. Soc.
55 (2023), 2304--2323,
[arXiv:2304.05178v1, Theorem 3 and its defining asymptotic](https://arxiv.org/html/2304.05178v1),
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859).
The audited application in L390 gives E|f^(j)/L^j|^4=O(ell^4)
for j=0,1,2 on the sharp interval. Since
rho^4<=3(x^4+y^4+z^4), choose fixed C4 and H4 such that
E rho^4<=C4 ell^4 for every real H>=H4.

For the absolute third moment, import L406's audited application of
M. J. Curran and A. Heycock, *Sharp bounds for joint moments of the
Riemann zeta function*,
[arXiv:2403.00902v1, Theorem 1.1/(2), Sections 3.1 and 4](https://arxiv.org/html/2403.00902v1).
Its unconditional n=2, k=3/2 cases, with all h_j zero or one
h_j=3/2, j=1,2, give the three exponents 9/4,21/4,33/4.
The equality endpoint sum h_j=k is allowed. L406's ordinary-jet
identities include both phase derivatives before division by L^j;
the corresponding divisors remove 3j from these exponents. Thus
E rho^3<=C3 ell^(9/4) with fixed C3 on a common eventual ray.
There is no negative power of zeta, conditional law assumption or
integer-height restriction. These source results are reused rather
than reproved. They apply to the actual input X0; all statements
about output moments require the scaling calculation below.

**Exact degrees and curvature.** Set e=q/L^2 at the actual height.
Expanding L414's conversion cancels alpha exactly and gives

    ell_F=y^2-xz-e x^2,
    Ccal=v_1^2-v_0 v_2-e v_0^2,
    Bcal=2y v_1-x v_2-z v_0-2e x v_0,
    Delta=Bcal^2-4 ell_F Ccal.

Here e and the whole response triple are fixed coefficients, not
resampled variables. Consequently ell_F and Delta have degree two
in X, Bcal and each omega_i have degree one, and U has degree two.
The response is uniformly bounded, including its derivative errors;
bounded alpha,q and L>=1 give fixed constants CB,CD with
|Bcal(X;t)|<=CB|X| and |Delta(X;t)|<=CD|X|^2 for every X.
The response annulus also bounds every coefficient of omega. Thus
all degree-four observables below have absolute value <=C|X|^4.
Nothing replaces the physical response by its leading carrier.

**Every branch, fiber and quartic.** On 0<rho<M, the multiplier
k=r/rho=M/rho is finite, p=k^-4 and |Y|=M. On rho>=M,
k=1, p=1 and Y=sX0; the formulas agree at equality. At rho=0,
p=0,Y=0 and every critical observable under consideration vanishes.
The sign convention is Borel, including DB=0. For every Borel set
of critical triples, p times its indicator evaluated at Y is Borel;
the same holds for the zero atom. Hence these formulas define kernels,
despite a possible discontinuity of Y at zero. The completed fiber has
mass p+(1-p)=1, so its pushforward to height is exactly dt/H and its
response is the actual deterministic response at that height.

If D>0, sB=|B|, including B=0. If D<=0, output Delta=k^2 D<=0
regardless of B. At D=0 the adopted s=1 is harmless. Thus all atoms,
including zero, have the asserted allowed support.

For any one of the degree-four observables Q4, homogeneity gives
p Q4(s k X0;t)=k^-4 s^4 k^4 Q4(X0;t)=Q4(X0;t).
At zero both sides are zero. This checks separately Delta^2,
Delta Bcal^2, the six diagonal and fifteen off-diagonal entries
Delta omega_i omega_j, and U^2. In particular no absolute value is
inserted into a signed off-diagonal quartic. Curvature and every
response derivative stay unchanged in this pointwise identity.

**Unnormalized moments.** Write Q for the integrated rare second
matrix and keep all integrals with their factor p. The exact identities
in (3), and r>=M=lambda ell^2, imply

    E p <= C4 lambda^-4 ell^-4,
    tr Q=E[rho^4/r^2] <= C4 lambda^-2,
    |E[p Delta(Y;t)]| <= CD C4 lambda^-2,
    |E[p Bcal(Y;t)]| <= CB C4 lambda^-3 ell^-2.

For any fixed vector u,
u^T Q u=E[(rho^2/r^2)(u.X0)^2]>=0, so Q is positive
semidefinite. Also |Q_ij|<=sqrt(Q_ii Q_jj)<=tr Q.
These bounds neither divide by the rare mass nor certify the tiny
odd-second-moment tolerances. Those need L419's separate cancellation.
The absolute third-power bounds follow, on both nonzero branches, from

    p|Y|^3=rho^4/r<=rho^3,
    p|Bcal(Y;t)|^3<=CB^3 rho^4/r.

They integrate to at most C3 ell^(9/4) and CB^3 C3 ell^(9/4),
respectively. Exact U^2 preservation gives its fourth-power bound.
Zero completion contributes zero to all these integrals. Conversely,
its E x^2<=tr Q=O(1) cannot equal ell+O(1), and its first Delta
integral O(1) cannot equal -a_* ell+o(ell) since a_*>0. Thus it
really fails the selected full list, not merely an optional condition.

**Pointwise constants, integrability and real H.** On rho>=M,
linearity gives P_j(Y;t)=sP_j(X0;t), preserving the actual absolute
physical-jet bounds. On 0<rho<M the bounded conversion gives
|P_j(Y;t)|<=C lambda ell^2. For each j<=2,

    sup_(H<=t<=2H) ell^2 L(t)^j/T(t)^(1/2)
        <=ell^2 log(2+2H)^j/(1+H)^(1/2) -> 0.

This permits fixed E_j after one onset, enlarged to include the actual
branch. Response bounds, annulus, errors and Ccal lower bound are the
unchanged actual ones. At each fixed H the output norm is at most
max(M,sup rho), so every signed observable is absolutely integrable.
The finite maximum of the inherited and newly required onsets works
for every sufficiently large real H, with lambda fixed throughout.
No uniformity for lambda tending to zero or infinity is asserted.

**Cubic identity and downstream limit.** On rho>0,
p Delta(Y;t) Bcal(Y;t)=k^-1 sDB=(rho/r)|DB|; at zero it is
zero. Therefore (1) is exact and
0<=F_lambda<=CB CD C4 lambda^-1 ell^2. L409 concerns E(DB),
not this correlated absolute integral, so it gives no equality here.
A bulk with |X|<=C_b sqrt(ell) has absolute cubic at most
CB CD C_b^3 ell^(3/2)=o(ell^2) and every absolute quartic
O(ell^2)=o(ell^4), even after multiplication by 1-p. This verifies
the stated necessary cubic condition for the maximally oriented ansatz.
L419 supplies its own sharper O(ell) signed bulk correction; it is
a downstream result, not a premise of this proof.

No false bound, missing direct input or lack of uniformity was found.
This audit changes neither the argument nor the direct inputs. The
fixed-moment stop in L420 remains evidence about that certificate only.
The capped asymptotic, full feasibility, actual clipping, regulator
margin and global mixed positivity remain unresolved. No output kernel
is asserted to arise from a single global critical function.

## Mathlib

Full matching coverage for this conditional prescribed-response
construction has not been checked. The homogeneity and elementary
integral estimates above are written out for this specialization;
no formal verification or absence of supporting Mathlib results is
claimed. No numerical evidence or mathematical script is used.
