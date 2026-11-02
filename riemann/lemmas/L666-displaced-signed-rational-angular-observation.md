# Lemma 666: exact rational angular observation for the displaced family

## Hypotheses

Use L649's conventions x=-d=-5/4, R=11/8, U=R^2=121/64,
eta=1/100, and t_j=j/n for 0<=j<n. Let q>=1 be an integer,
n=12q+3, M=4q+1=n/3, J=n-1, and H_0=27/(10n). For each
integer -2q<=m<2q choose an independent real e_m with |e_m|<=1/8.
The original poles, all of residue one, are

    Z={x} union {x+i*H_0*(m+1/2+e_m): -2q<=m<2q}.

The anchor is fixed; no symmetry is assumed. This is exactly the
delta=1/4 displaced family, with h=2H_0 and |epsilon_m|<=h/16.
Keep the full product and its conjugated denominator angle:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_(a in Z) W_a(u)*(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k,
    D=mean_u sum_(a in Z) |W_a(u)|^2/(U-|a|^2),
    E_0=mean_u |c_0(u)|^2,
    H=max_u mean_zeta log|G(u,zeta)|.

Both circle means are normalized. In particular D is the original
squared-residue diagonal, and G retains all M spatial moments.
For the angular rational quadrature define the interior completion

    S={0} union {p_j=t_j*x/U: 1<=j<n}
          union {t_j/conjugate(a): a in Z\{x}, 1<=j<n},
    K=1+MJ,
    Bcal(u)=product_(z in S) (u-z)/(1-conjugate(z)*u),
    mu(u)=sum_(z in S) (1-|z|^2)/|u-z|^2,       |u|=1.

The letter Bcal denotes the quadrature Blaschke product, not B_u(v).

## Conclusion

The family is L649-admissible. S consists of exactly K distinct points
of modulus less than 4/5. For any fixed real phi there are exactly
2K distinct circle solutions u_l of Bcal(u_l)^2=exp(i*phi). Set

    w_l=1/(2*mu(u_l)).

Then the following are exact, with every signed cross term retained:

    sum_l w_l=1,
    E_0=R^(-2) sum_l w_l |sum_(a in Z) W_a(u_l)|^2,       (1)
    D=sum_l w_l sum_(a in Z) |W_a(u_l)|^2/(U-|a|^2).     (2)

The weights and sample count incur only polynomial size factors:

    1/[2*(1+9MJ)] <= w_l <= 1/[2*(1+MJ/9)],
    2K=2+2M(n-1).                                      (3)

Moreover E_0>0, and L664's full-root Jensen bridge gives

    H >= log max_l |c_0(u_l)| >= (log E_0)/2.            (4)

Thus, for an absolute c>0 and a uniform onset, the still-unproved
signed sample inequality

    [R^(-2) sum_l w_l |sum_a W_a(u_l)|^2]
      /[sum_l w_l sum_a |W_a(u_l)|^2/(U-|a|^2)]
                         >= c^2*n^2*exp(-n/16)          (5)

would imply H >= (log D)/2-n/32+log n+log c, and hence L658's
paid-arc estimate with an absolute constant. Equations (1)--(3)
are not a lower bound in (5): positive quadrature weights do not
make the complex off-diagonal terms nonnegative. Nor is (5) necessary
for a lower bound obtained from the angular maximum or other moments.

This is a specialization of a known quadrature theorem and a reduction
of the approved test, not a new coercivity bound or progress beyond that
source theorem. The finite diagnostic below proves neither (5) nor its
failure. General support, Xi realization and all-degree signs remain
open. The specialization has not received a separate critical audit.

The subsequent analytic test in Section 6 keeps (5) unresolved. It
proves only that along any allowed straight displacement path the
original diagonal changes by a factor between exp(-17/4) and exp(17/4).
The exact signed-energy derivative remains uncontrolled at the required
rate. This auxiliary comparison is not a lower bound for E_0/D.

## Proof

### 1. Source scope and family qualifications

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-displaced-signed-angular-sampling.md`.
It covers this exact rational observation test with unit original
residues, independent shifts and the c_0 Jensen bridge. C645o's negative
cross entry, L649's ambient deweighting stop, L650's separate pole-dual
stop and L665's displacement stops are comparisons, not premises of
this identity. No exponential surrogate or unproved positivity is used.

Import V. I. Danchenko and L. A. Semin, *Sharp quadrature formulas
and Nikol'skii type inequalities for rational functions*,
[arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1), 22 March 2015,
Section 1.1, Theorem 2, PDF pp.1--2; its proof is on PDF pp.6--7.
For a finite distinct interior set containing 0 and its circle-reflected
completion, a rational F has ordinary pole orders at most s and combined
orders at 0 and infinity at most 2s-1. The theorem gives

    integral_(|u|=r) |F(u)|^2 |du|
      =(pi*r/s) sum_(Bcal(u_l)^(2s)=exp(i*phi)) |F(u_l)|^2/mu(u_l).

We use only r=s=1. The prior source review inspected this statement
and the complete proof of Theorem 2, including reflected factors and
polynomial parts; Theorem 1's underlying proof was not independently
audited. The present work verifies the precise finite rational pole
membership. It does not reprove the general quadrature theorem.

The Jensen input already used in L664 Section 5 is F. Brunault and
W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
including every root modulus and boundary roots. L658 supplies the
full spatial logarithmic localization and its inherited integrability.

Ordered nonanchor ordinates have successive gaps at least 3H_0/4.
Each has distance at least 3H_0/8 from zero. Their largest absolute
value is at most H_0*(2q-3/8)<2qH_0=27q/(5n)<9/20.
Thus they are all distinct and nonzero, and

    |a|^2 < (5/4)^2+(9/20)^2=353/200 < (273/200)^2=(R-eta)^2.

There are exactly M poles, all on Re(a)=x, with unit original
residues. This verifies every family hypothesis required from L649
and L658. It also makes U-|a|^2 strictly positive in (2).

### 2. All angular poles, reflections and orders

For u on the circle, exact division of all product factors gives
the rational continuation

    W_a(u)=(x/a) product_(1<=j<n)
                    [(x-t_j*u)/(a-t_j*u)]
                    *[(U*u-t_j*a)/(U*u-t_j*x)].         (6)

The j=0 factor is x/a and has not been omitted. For a=x this is
the constant one, with all apparent poles cancelled. For nonanchor a
the only possible angular poles are p_j=t_j*x/U and a/t_j.
The p_j are distinct negative real numbers; the a/t_j have modulus
greater than d>1 and are distinct for fixed a. There is no coincidence
between these two lists. Each possible pole in a single term is simple;
a finite sum can cancel poles but cannot increase their orders.
Equation (6) also has finite values at 0 and infinity, both x/a.

The reflection across the angular unit circle of a/t_j is
t_j/conjugate(a), exactly as recorded in S. Reflections of the p_j,
and infinity as the reflection of 0, are allowed completion points;
F is not required to have a pole at every allowed point. Possible
cancellations cause no violation of an upper bound on pole orders.
All W_a and their sum c_0 therefore have poles only in the completed
set, with ordinary orders at most one and combined orders at 0 and
infinity equal to zero, which is at most 2*1-1.

To count S, note that p_j is real while t_j/conjugate(a) is nonreal
for nonanchor a, and none is zero. If
t_j/conjugate(a)=t_k/conjugate(b), then
t_j*conjugate(b)=t_k*conjugate(a). Comparing real parts, using
Re(a)=Re(b)=x!=0, gives t_j=t_k, and then a=b. The p_j are also
distinct. Hence |S|=1+J+(M-1)J=K. Their moduli obey

    |p_j|<d/U=80/121<4/5,
    |t_j/conjugate(a)|<1/|a|<=1/d=4/5.

In particular all source interior-set and no-boundary-pole conditions
hold for the same completion S for every F in question.

### 3. Normalization, sample nodes and exact signed sums

On the unit circle each factor of Bcal has modulus one and continuous
angular argument derivative (1-|z|^2)/|u-z|^2. This follows by
differentiating its logarithm; its denominator never vanishes there.
Thus the argument derivative of Bcal is mu>0 and its total increase
is 2*pi*K. For example, for z!=0 the factor's argument is
theta+2*arg(1-z*exp(-i*theta)), with the second argument continuous
and periodic because |z|<1. The same formula holds at z=0 with
zero second term. Consequently the equation for Bcal^2 has exactly
2K distinct roots on one circle, with no endpoint double counting.

Divide the imported formula by 2*pi. With r=s=1 the weight is
exactly 1/(2*mu), rather than 1/mu. Apply it first to F=1 to get
sum_l w_l=1. Apply it to the single combined rational function
F=c_0, not to its summands separately, to obtain (1). Apply it to
each W_a, multiply by the positive constant 1/(U-|a|^2), then
sum finitely over a, to obtain (2). All original residues remain one;
the w_l are angular observation weights only. In particular (1)
retains the complete complex sum before the modulus square.

For |z|<4/5 the Poisson factor is between 1/9 and 9, by the bounds
(1-|z|)/(1+|z|) and (1+|z|)/(1-|z|). The factor from z=0 is
exactly one. Adding all K factors and taking positive reciprocals
proves (3). Neither this polynomial bound nor the normalization of
the weights controls cancellation in (1).

### 4. Nonzero response and the full spatial Jensen bridge

The rational continuation at infinity gives

    c_0(infinity)=(x/R) sum_a 1/a,
    Re c_0(infinity)=(1/R) sum_a d^2/(d^2+(Im a)^2)>0.

Thus c_0 is not the zero rational function. It is continuous on the
circle and has at most finitely many circle zeros, so E_0>0. By (1)
and sum w_l=1, at least one observation has
|c_0(u_l)|>=sqrt(E_0)>0. For every such observation the full
polynomial G(u_l,.) has nonzero constant coefficient. The cited
root formula yields

    mean_zeta log|G(u_l,zeta)| >= log|c_0(u_l)|.

Indeed each root factor contributes log max(1,|alpha|), which is
at least log|alpha|. The leading factor, all M prescribed moments,
any actual degree drop and boundary roots are retained. Maximizing
over angles proves (4). L658's hypotheses and inherited integrability
were verified in section 1; in particular its maximum H and its
localized arc remain valid even when other slices have boundary zeros.

If (5) held, take half its logarithm in (4). This gives the asserted
bound for H. Substitution into L658's exact paid expression gives

    log mu_arc(I)+2 mean_(I x T) log|G|-log D+n/16
                               >= 2log c-32*pi^2/9.

Here mu_arc denotes normalized arc length, not the quadrature weight
function mu. This is a conditional implication; (5) remains open.

### 5. Bounded diagnostic and its limits

Run `python3 scripts/one-sided-hankel/displaced-signed-angular-sampling.py`.
The full floating-point diagnostic is
`scripts/one-sided-hankel/displaced-signed-angular-sampling.json`.
It uses n=27,51,99, two starts per n, and 60 projected iterations
on independent permitted displacements, minimizing the sampled E_0/D.
The selected shifts are rounded to rational multiples of H_0 with
denominator 10^8, and every numerator is stored. No symmetry is imposed;
a minimizer reached from the zero start may have symmetry.

After selection, the script evaluates 4096 uniform angles and all
470, 1702, and 6470 nodes, respectively, of the common quadrature.
It retains the complete rational products and signed sums. Its
quadrature rows contain every computed angle, mu, weight, c_0 and
diagonal. The observed normalized L2 ratios

    sqrt(E_0)/[n*exp(-n/32)*sqrt(D)]

are approximately 0.00530155, 0.00765720, and 0.01240776.
The corresponding sampled-maximum ratios are approximately
0.01035775, 0.01128412, and 0.02643436. These numbers neither
verify nor falsify an unspecified uniform c and onset in (5).

The analytic directional gradient and a centered finite difference
agree within 3.4*10^(-10); dense-grid and quadrature E_0,D values
agree to relative error below 1.9*10^(-15). The recorded diagnostic
failure list is empty. These checks concern a floating implementation,
not interval enclosures, global optimization, an angular supremum,
or an unbounded-n theorem. No numerical value is a premise of
(1)--(4). No admissible countersequence or sufficient uniform lower
bound was obtained. Further repetition of finite screens alone would
not settle the remaining signed inequality.

### 6. Analytic signed-flow test — 2 November 2026

This continues the same invocation-start EXPLORE assessment, with no
new theorem import or numerical screen. The target is still (5), not
an absolute-error comparison with the inherited anchor. The exact
product and quadrature above, L664's audited baseline and L661's
audited general diagonal envelope are the inputs. The older C645p
zero-evaluation and L665 absolute-transfer stops were compared; they
do not supply a relative signed estimate here. The following elementary
differentiation is written out to keep the attempted rate comparison
checkable; it is not claimed as a new general sampling theorem.

For any allowed final vector epsilon_m=H_0*e_m, set

    a_m(s)=x+i*(H_0*(m+1/2)+s*epsilon_m),  0<=s<=1,
    c_s(u)=R^(-1) sum_a W_a(s,u),
    E_s=mean_u |c_s|^2,
    D_s=mean_u sum_a |W_a(s,u)|^2/(U-|a_m(s)|^2).

The anchor remains x and has epsilon_x=0. Section 1 proves admissibility
along the whole path, since |s*epsilon_m|<=H_0/8. In this section
E_s,D_s carry a path subscript; E_{s=0} is the undisplaced energy,
whereas E_0 elsewhere in the lemma denotes the zeroth spatial energy
of the family under consideration. No original residue is changed.

Every W_a is nonzero on the angular circle. Define its logarithmic
derivative by its quotient, without choosing a logarithm:

    V_a(s,u)=(d_s W_a)/W_a
       =-i*epsilon_a sum_(0<=j<n)
           [1/(a_m(s)-t_j*u)+t_j/(U*u-t_j*a_m(s))].       (F1)

The j=0 term is included. The numerator and denominator clearances
are at least d-1=1/4 and U-273/200=841/1600>1/2, respectively.
Since |epsilon_a|<=27/(80n),

    |V_a(s,u)| <= (27/(80n))*6n=81/40.                 (F2)

Also |Im a|<9/20 and
U-|a|^2>U-353/200=201/1600. Direct differentiation of the diagonal
weight therefore gives

    |d_s log(1/(U-|a|^2))|
       =|2 Im(a)*epsilon_a/(U-|a|^2)|
       <=162/(67n).

Each positive summand in D_s has logarithmic derivative bounded in
absolute value by 81/20+162/(67n). All sums are finite, and for each
fixed n the integrands and their derivatives are continuous on the
compact path times circle, with the clearances just displayed. Thus
differentiation under the normalized mean is valid. Summing and then
integrating the differential bound yields

    |D'_s| <= (81/20+162/(67n))*D_s,
    exp(-17/4) <= D_s/D_t <= exp(17/4),  0<=s,t<=1.      (F3)

Here n>=15 and 81/20+162/(67*15)<17/4. No symmetry or sign of a
complex cross term is used. This proves the auxiliary diagonal claim.

Section 4 proves E_s>0 at every s. With
c'_s=R^(-1) sum_a V_a W_a the exact relative derivative is

    d_s log(E_s/D_s)
       =2 Re mean_u(c'_s conjugate(c_s))/E_s-D'_s/D_s.   (F4)

The first term contains all mixed pairs. In particular (F2) cannot
be used as a bound of 81/20 for that term: the V_a depend on a and
cannot be pulled out of the signed sum.

For clarity, the actual available rate margin can be computed without
an asymptotic model. At s=0, L664 gives |c_s(-1)|>=1/(2R) beyond
one absolute onset. In (1) choose phi so that -1 is a quadrature
node. Its weight is at least 1/[2*(1+9M(n-1))]. Consequently

    E_{s=0} >=1/[8R^2*(1+9M(n-1))] >=1/(24R^2*n^2).

Import only L661's diagonal envelope, with kappa=91/5000 and
sigma^2=137/5000. Unit residues give

    D_{s=0} <= n*exp(2*kappa*n+6)/(3*sigma^2),
    E_{s=0}/D_{s=0} >= C_0*n^(-3)*exp(-2*kappa*n),
    C_0=sigma^2*exp(-6)/(8R^2)>0.                      (F5)

Define the signed logarithmic loss

    Lambda=-integral_0^1 2 Re mean(c'_s conjugate(c_s))/E_s ds
           =log(E_{s=0}/E_{s=1}).

There is no singularity in this integral: for each fixed displacement
vector, E_s is continuous and positive on the compact path. Equations
(F3)--(F5) imply

    E_{s=1}/D_{s=1}
       >=C_0*exp(-17/4)*n^(-3)*exp(-2*kappa*n-Lambda).

Thus a uniform estimate

    Lambda <=261*n/10000-5log n+B                      (F6)

for an absolute B would suffice for (5), because
1/16-2*kappa=261/10000. In particular, any uniform bound
Lambda<=gamma*n+B with fixed gamma<261/10000 would eventually suffice.
These are conditional sufficient estimates, not established bounds
or necessary conditions for (5).

The attempted closure of (F4) by the available product estimates fails
to retain the needed relative control. In detail, weighted
Cauchy--Schwarz and U-|a|^2<=U-d^2=21/64 give

    ||c'_s||_2
       <=(81/(40R))*sqrt(M*21/64)*sqrt(D_s)
       =A*sqrt(n*D_s),       A=81*sqrt(7)/440.

Therefore the absolute estimate for the signed part of (F4) is only
2A*sqrt(n*D_s/E_s). Integrating the corresponding norm bound, using
(F3), gives

    sqrt(E_{s=1}/D_{s=1})
      >=max(0, exp(-17/8)*sqrt(E_{s=0}/D_{s=0})-A*sqrt(n)).

Substitution of the proved baseline lower bound (F5) supplies only
zero on the right for large n. This is an insufficiency of these
estimates. It does not prove that the actual signed derivative is
large, that Lambda violates (F6), or that the final response is small.
Replacing the signed term by this absolute estimate is the discarded
fallback, not a reopening of L665's stopped absolute-transfer route.

No upper bound for Lambda, lower bound in (5), or admissible
countersequence was obtained. Outcome: EXPLORATION, the second
unproductive mathematical attempt on scalar signed sampling. The
new diagonal stability and exact margin accounting isolate the missing
quantity but do not solve it. The scalar mechanism is parked pending
materially new input; the proposed full-spatial alternative requires
its own source review. These statements and constants have not had a
separate critical audit. No new numerical evidence is asserted.

## Mathlib

Full matching coverage for Danchenko--Semin's rational quadrature and
this displaced-family specialization has not been checked. Unknown
availability is not evidence of absence. The reused source assessment
records supporting
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`. They support the root-formula step;
they are not the missing signed sample coercivity theorem.
Full matching coverage for Section 6's parameter differentiation and
family-specific constants has not been checked. Its elementary
Cauchy--Schwarz and compact differentiation steps are justified above;
no formal verification or new library absence claim is made.
