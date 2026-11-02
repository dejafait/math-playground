# C499d — Uniform quadratic-curvature envelope misses the reserve

## Hypotheses

Retain L494's exact heat normalization and full frozen-index remainder
bounds, L495's literal resultant and two charges, L496's uniform phase
floor, and L499's accepted old coefficient mass and positive envelopes
R0,J0,D0. Use C499c's finite increment factorization, without promoting
its endpoint numerical values to uniform bounds. Set exactly

    t=.16836, X=6000284561421.5, n=691004, N=691260,
    Y=4*pi*(N^2-t/16), P={primes<=307},
    q(x)=floor(sqrt(x/(4*pi)+t/16)), X<=x<=Y,
    ell0=24.18022820120389,
    epsilon=6e-7,
    epsilon_1=((6e-7+1.3e-6)*8.770232)/.14142,
    r0=14176540015048665224252705167939023
       /33554432000000000000000000000000000000.

Each decimal is rational. Every true remainder derivative freezes q(x)
at its own centre, including cutoff equality. No derivative of the floor
is taken. Manuscript saddle/base-phase proofs retain their unaudited
qualification. This is a computational specialization of known estimates,
not an independent audit or a new cancellation theorem.

## Conclusion

The following particular sufficient envelope is valid uniformly:

    |G_tilde_q(x)(x)-G_tilde_n(x)| <= B_unif,
    L495's saddle charge <= U_s,unif,
    L495's remainder charge <= U_r,unif.

The separately justified scalar envelopes satisfy

    .00070171640076552016 < B_unif < .00070171640076552017,
    U_s,unif < 1.254886146337842e-11,
    U_r,unif < .000020830477230729,
    .00072254689054510978
      < B_unif+U_s,unif+U_r,unif
      < .00072254689054510979,
    r0 < .000422493815870544.

Thus this envelope cannot pay the required strict r0 budget. Its
quadratic reduction, followed by one smooth initial piece and an
absolutely charged terminal piece, gives no improvement over the
trivial uniform unweighted prefix bound. All 255 nonempty smooth-piece
choices are tested; their best raw full-prefix upper-bound formula is
in (428.69210856300946,428.69210856300947), exceeding 256. Even
the sharper endpoint version tested below exceeds 428.6525.

These comparisons concern evaluated upper-bound formulas. They are
not lower bounds for the actual increment, its supremum, or a primitive
sum. They do not prove a collision, obstruct every exponential-sum
method, invalidate C499c, or establish any all-height/zero-time claim.
The particular curvature/absolute-tail/Abel envelope is parked.

## Proof

### 1. Closed cells and the reduced phase

The rational certificate verifies

    C_n<=X<C_(n+1), C_j=4*pi*(j^2-t/16),
    Y>X, t*(log(X/(4*pi))+(Y-X)/X)<5.17.

Since log(x/X)<=(x-X)/X, L494–L496 apply on the entire closed
interval. Its canonical cells are [X,C_(n+1)), [C_q,C_(q+1))
for n<q<N, and the singleton {Y} for q=N. At each left equality
the new index is used. The old n model is just a finite comparison.
L496 gives ell>ell0, nonzero Euler factors and |nu'|<.500000000001
throughout; these are bounds on the actual phases in L495.

From the exact alpha in C499c, with a=pi/2-atan(1/x),

    eta=x/2+(t/2)*(a/2-3*x/(1+x^2)),
    eta/(2*pi)=x/(4*pi)+t/16-delta(x),
    delta(x)=t*atan(1/x)/(8*pi)+3*t*x/(4*pi*(1+x^2)).

For x>=X, 0<atan(1/x)<1/x and x/(1+x^2)<1/x give

    0<delta(x)<7*t/(8*pi*X)<=dmax<10^(-12),

where dmax is the outward rational upper endpoint evaluated in the
certificate. At any centre in cell q, writing a_x=eta/(2*pi),

    q^2-dmax < a_x < (q+1)^2.

For a real variable u>0 let

    f_x(u)=-a_x*log u-u*(u-1)/2.

For integer j, j*(j-1)/2 is an integer, so
exp(2*pi*i*f_x(j))=exp(-i*eta*log j) exactly. This uses the
integer binomial coefficient and trigonometric periodicity, not an
approximate phase reduction. Its residual curvature is

    f_x''(u)=a_x/u^2-1.

At an entry equality it is negative at u=q, so a positive-curvature
estimate must not be used through that point. There is no assumed
separation of f_x' from integers.

### 2. All prefixes, tail costs and the explicit curvature test

For a prefix n<j<=k<=q, set m=k-n. The empty prefix is zero.
Choose an integer terminal length 1<=r<m. Pay its r terms absolutely.
On the remaining interval (n,k-r], of length L=m-r>=1,

    0<lambda_r=(N^2-dmax)/(N-r)^2-1
      <=f_x''(u)<=Lambda=(N+1)^2/n^2-1.

Indeed k<=q<=N gives
(q^2-dmax)/(k-r)^2-1 >= (q^2-dmax)/(q-r)^2-1.
The last function decreases in q: its derivative is
-2*(q*r-dmax)/(q-r)^3<0. The upper bound uses u>n and
a_x<(q+1)^2. Positivity of every lambda_r is checked exactly.
The phase is real C^2 on this interval. The uncharged cutoff endpoint
and any residual curvature degeneracy lie in the paid terminal piece.

Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*,
[arXiv:2407.02094v1, Section 2, Lemma 5, PDF p.4](https://arxiv.org/html/2407.02094v1#S2),
states for L>=1 and 0<lambda<=f''<=Lambda that

    |sum_(a<j<=a+L) exp(2*pi*i*f(j))|
      <= A*(Lambda*L+2)/sqrt(lambda),
    A=(2/sqrt(pi))*(1+sqrt(1+3*pi/8)).

Its hypotheses do not exclude integer first-derivative resonances;
the complete Lemmas 4–5 proof is covered by the prior assessment.
No reproof, ineffective transform error, omitted stationary term or
negative-curvature application is used here. Accordingly our candidate
prefix bound is

    min(m, F_r(m)),
    F_r(m)=r+A*(Lambda*(m-r)+2)/sqrt(lambda_r).

The certificate evaluates F_r(256) for every r=1,...,255; each
lower endpoint exceeds 256. For fixed r, F_r(m)-m is affine in m.
At m=r it equals 2*A/sqrt(lambda_r)>0, and at m=256 it is
positive. Thus it is positive for every r<=m<=256. These uniform
curvature choices improve none of the trivial prefix caps m; the
empty/singleton cases are covered by 0/1 directly. Paying all m
terms is always available. Hence every prefix has bound M=256.

For a tighter diagnostic at Y, use Lambda_Y=N^2/n^2-1 in place
of Lambda, retaining the same valid lower lambda_r. Every raw
F_r(256) still exceeds 256; the least tested value is in
(428.65251605740534,428.65251605740535). These endpoint rows also
test every smooth initial length L=1,...,255. The difference of its
curvature formula from L equals F_(256-L)(256)-256>0. Adding any
nonnegative absolute terminal cost therefore gives no saving for
any endpoint prefix by this particular split. The full smooth length
256 fails the positive-curvature hypothesis at Y. This does not
rule out finer spatial subdivision, signed terminal treatment, other
partitions in j, or a different exponential-sum input.

### 3. Uniform heat weights and complete resultant

Put h_a=log(n+1), h_N=log N, sigma0=sigma(X), and

    w_x(u)=exp(t*(log u)^2/4-sigma(x)*log u),
    w_a=exp(t*h_a^2/4-sigma0*h_a).

L496 proves sigma(x)>=sigma0. The certificate checks
d=sigma0-t*h_N/2>0 and h_a*d>1. For n+1<=u<=N,

    d(log w_x(u))/du=(t*log(u)/2-sigma(x))/u<0,
    d(log(u)*w_x(u))/du
       =w_x(u)/u * [1-log(u)*(sigma(x)-t*log(u)/2)]<0.

Both weights are positive and decreasing in u, and decrease in x.
Finite Abel summation with all prefix sums bounded by M gives
|sum a_j v_j|<=M*v_first for any such decreasing positive weight:
the terminal term and variation telescope to v_first. This is precisely
the finite interface in [DLMF 2.10.9–10](https://dlmf.nist.gov/2.10.E9)
and Tracy, [*Abel Partial Summation Formula*, 28 January 2012,
pp.1–2](https://www.math.ucdavis.edu/~tracy/courses/AbelSummation.pdf),
with the endpoint retained. Thus, for the actual primitive phases,

    |DeltaS(x)|<=S_cap=256*w_a,
    |DeltaL(x)|<=L_cap=256*h_a*w_a.

In cell n these increments vanish. No full-block sum is substituted
for the required prefix control, and weights at Y are not used as
uniform upper bounds.

C499c's finite algebra applies separately at every x and its actual q:

    DeltaZ=rho*v*DeltaS,
    DeltaW=rho*v*(DeltaL-J*DeltaS),
    DeltaG=DeltaZ-DeltaW/ell+conj(DeltaW)/ell,
    v=exp(i*Theta(x)), J=sum_p log(p)*A_p/(1-A_p).

This includes all squarefree channels, the exact product of PRIME heat
weights, every logarithmic term and the conjugate term. Finite
distributivity permits coincident outputs without truncation. L496/L499
give rho<=R0, |J|<=J0, |E_prod'|<=D0 throughout, by decreasing
prime radii and their positive denominators. Keeping the literal
actual phases and ell in the identity, triangle inequality therefore
gives the uniform envelope

    B_unif=R0*(S_cap+2*(L_cap+J0*S_cap)/ell0).

The identity has not replaced ell by an unrelated phase. Replacing
its positive denominator by ell0 and bounding |v|=1 are sufficient
inequalities for this conservative estimate. The result retains no
signed cancellation between DeltaZ and the two DeltaW terms; this
loss is part of the tested method, not an estimate of the actual cost.

### 4. Independent uniform charge envelopes and inherited reserve

The old primitive positive sum decreases from X and is <=53/3 by
L499. New primitive weights have sum <=S_cap independently of
cancellation. With H=log N+sum_p log p, every output has log(d*j)<=H.
Finite positive product expansion gives

    |L_hat_q(x)(x)|<=K=R0*(53/3+S_cap)*H.

No output beyond a previous cutoff is removed. L495's positive
Q(x)=x*(x^2+5)/(1+x^2)^2 and C(x)=(7*x^2-5)/(1+x^2)^2
decrease for x>=X: their derivative numerators are respectively
5-12*x^2-x^4 and 2*x*(17-7*x^2), both negative. Consequently

    U_s,unif=t*(Q(X)+C(X))*K/ell0,
    U_r,unif=R0*epsilon/2
              +2*(D0*epsilon+R0*epsilon_1)/ell0.

Both saddle corrections, the complex Euler-product derivative, rho,
and L494's full entering-pair/Cauchy allowance remain charged.
Each true remainder uses its own frozen canonical q, even at equality.
No estimate for DeltaG replaces this independent absolute logarithmic
norm. These envelopes are justified on the whole interval from X.

For the old finite comparison, each coefficient has the form
beta_m*m^(-sigma(x)), with real beta_m independent of x.
Increasing sigma damps its absolute value even for negative beta_m
and m>n. L499's accepted complete mass therefore continues to bound
the old model's h_ell0 mass by 1-r0. Its m=1 term has modulus one;
|1-u|+u=max(1,2*u-1)<=h_ell0(m), u=log(m)/ell, gives
|G_tilde_n(x)|>=r0 exactly as in C499c. A strict comparison
B_unif+U_s,unif+U_r,unif<r0 would thus suffice for qualified
exclusion. The computed envelope does not meet that threshold.

### 5. Complete rational certificate and limits

Reproduce from the notebook:

    python3 scripts/heat/uniform-quadratic-curvature-budget.py

The full certificate is `scripts/heat/uniform-quadratic-curvature-budget.json`.
It checks the unchanged arithmetic producer against C499c's completed
audit and L499's retained corner/input hashes. It executes only the
producer's arithmetic definitions before `def run()`, not its endpoint
calculation or output code. Exact Fraction arithmetic, outward 10^(-60)
rounding, integer square-root bounds, logarithm and exponential series
are reused with the proofs and qualifications in C499c Sections 5–6.
All new elementary evaluations and tails are stored. This reuse is
not a new independent audit. No binary floating-point value enters
the mathematical certificate. Earlier floating-point diagnostics in
the working process were not used in any certified comparison.

All 780 implementation/provenance/domain/curvature/weight/width checks
pass. The mathematical strict-budget predicate fails, explicitly
reported as ENVELOPE_FAIL, separately from implementation failures.
All 255 split rows and their exact operands are saved. Complete exact
best-row, weight and envelope endpoints were inspected. The total-cost
width is <10^(-30); no precision refinement is needed. In particular

    total-r0 > .00030005307467456650.

This is adequate-precision failure of a sufficient bound, not evidence
of a large actual increment or a counterexample. C499c remains an
endpoint result; intermediate/later cells, other times, H1, zero time,
source audits and actual-Xi all-degree signs remain unresolved.

## Mathlib

Full matching coverage is unchecked and unknown. Supporting mathematics
includes finite Abel summation, integer binomial coefficients and
periodicity, elementary differentiation, finite products and exact
rational enclosures. No Mathlib formalization of this effective
derivative theorem, heat/resultant application or certificate is claimed.
Unknown availability is not absence.
