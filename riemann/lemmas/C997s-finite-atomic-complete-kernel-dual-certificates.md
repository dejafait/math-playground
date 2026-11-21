# Corollary 997s: finite atomic lower certificates for the complete residual

## Hypotheses

Use the COMPLETE kernel of audited C997c(1),(4)-(6):

    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t) exp(izt)dt
                           -integral_n^(n+2) g_n(t) exp(izt)dt],
    g_n(t)=K_(n+2)(t) exp(-t/2) cosh(3t/8),
    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1).

Here n>=2 is an integer, I=[7/4,9/4], E=[15/8,17/8],
z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n, and B_n=exp(sqrt(n)).
The original COMPLEX coefficient cap and complete continuum objective are

    E_n=inf_(sum_j |A_j|<=B_n)
              sup_(c in I)|k_n(c,z_star)-sum_j A_j k_n(c,gamma_j)|.

No Haar property, nonvanishing of g_n, exact reconstruction, zero
simplicity or actual-Xi input is assumed. Both beta terms, both windows,
the constant subtraction and both closed endpoints are retained.

## Conclusion

For any finitely supported complex measure mu=sum_l w_l delta_(c_l)
on I with sum_l |w_l|<=1, set

    T=sum_l w_l k_n(c_l,z_star),
    d_j=sum_l w_l k_n(c_l,gamma_j).

Then the known weak support-function certificate specializes to

    E_n >= max{0, |T|-B_n max_j |d_j|}.                    (1)

For n=4,8,12,16, take c_l=7/4+l/(2(n+1)), 0<=l<=n+1,
and the EXACT rational complex weights saved in
`scripts/adaptive-slope/direct-kernel-atomic-371.json`,
`/runs/r/rational_weights`, in the listed n order (r=0,1,2,3).
The finite interval calculation described below gives these safe bounds:

| n | certified lower bound for E_n |
|---|---|
| 4 | >0.00015754 |
| 8 | >0.00000019683 |
| 12 | >0.0000000012461 |
| 16 | >0.0000000000036086 |

These are NONOPTIMAL finite lower certificates. The particular
certificates, multiplied by exp(n/64), are approximately
1.67703e-4, 2.23045e-7, 1.50311e-9, 4.63363e-12, respectively.
These numbers describe the computed certificates, NOT E_n itself.
They do not prove or disprove E_n=O(exp(-n/64)): that big-O assertion
has an unspecified uniform constant and concerns unbounded n.
In particular no unbounded-subsequence lower rate is established.

Step371, 11 November2026: RESEARCH / REPRODUCTION, outcome EXPLORATION,
under the unchanged pre-invocation EXPLORE review370. This is a finite
specialization and certificate computation, not a new mathematical
discovery or a resolution of the approved asymptotic test. Independent
conceptual audit remains pending. No RH candidate is proposed.

Step372, 11 November2026, tests paid band leakage on the denser grids
c_l=7/4+l/(8n), 0<=l<=4n, at n=16,32. Formula(1) is unchanged.
The rational witness at `/results/4/rational_weights` of
`scripts/adaptive-slope/direct-kernel-paid-leakage-16-372.json` gives

    E_16 > 0.00520444248,
    its certified lower score times exp(16/64) > 0.00668263642.

Its target action has modulus >0.01053829296 and its largest band
action has modulus <0.000097692880. The original budget exp(4) pays
the latter in full. At n=32, ALL six generated candidates have negative
pre-clipping scores; they yield only E_32>=0. In particular this says
nothing about the optimal E_32 or the existence of a better witness.
Full enclosures, all failed candidates and their scores are retained in
the matching `direct-kernel-paid-leakage-32-372.json` artifact.

This is RESEARCH / REPRODUCTION / EXPLORATION under unchanged review370.
The n=16 improvement compares different slope grids AND different
candidate rules; it does not isolate the effect of leakage alone.
The bounded test establishes no unbounded-n rate, optimizer or continuum
upper bound. The step373 conceptual audit below accepts formula(1) and
the step372 finite certificates, including the candidate-specific failures.

## Proof

### Known support-function input and its complex specialization

The generic input is S. Boyd and L. Vandenberghe, *Convex Optimization*,
Cambridge UP,2004, Examples3.24/3.26, pp92-93,
[author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=106),
whose indicator/support-function and norm-dual statements were inspected
in review369 step370. The following is the necessary realification,
not a new proof of a minimax theorem. Regard C^(n+1) as R^(2n+2),
retaining the norm sum|A_j|, and use the real pairing Re sum A_j d_j.
Its support function on that ball is B_n max|d_j|: the modulus bound
gives <=, and for a nonzero maximizing d_j, the single coefficient
A_j=B_n conjugate(d_j)/|d_j| attains equality. For all d_j=0 it is zero.
The ball is a closed bounded convex set in finite real dimension.
No replacement by sum(|Re A_j|+|Im A_j|) is made.

For a chosen A, finite summation gives the residual pairing exactly as
T-sum A_j d_j. The kernel is continuous in c: its integrand is entire
in t, its moving endpoints are continuous, and all integrations are on
finite compact intervals. Thus its residual has a finite continuum
supremum, and

    |T| <= |T-sum A_j d_j|+B_n max|d_j|
         <= sum|w_l| ||residual||_C(I)+B_n max|d_j|.

Taking the infimum over A proves (1), also when its right side before
max is negative. Equivalently one can rotate the measure to make T
real nonnegative. There is no interchange of infinite integrations,
no strong-duality assertion and no continuum discretization. Atoms at
the endpoints are legitimate tests of the closed-interval supremum.

### Exact kernel evaluation and enclosures

Write P(t)=K_(n+2)(t). Its coefficient of t^j is

    p_j=(-1)^j binomial(n+3,n+1-j)/(j!(n+1)), 0<=j<=n+1,

with 1/(n+1) subtracted from p_0. This is the defining finite Laguerre
polynomial formula; the second computation below instead uses its
three-term recurrence. Expanding the cosh, the EXACT kernel is

    -exp(-cn/4) sum_(a in {-1/8+iz,-7/8+iz})
        [integral_(cn)^(c(n+2)) P(t)exp(at)dt
                         -integral_n^(n+2) P(t)exp(at)dt].  (2)

For every a used here, Im(a)>0, so a!=0. Put q_(n+2)=0 and recursively
q_j=(p_j-(j+1)q_(j+1))/a for j=n+1,...,0. The polynomial Q=sum q_j t^j
then satisfies Q'+aQ=P coefficient by coefficient. The interval integral
in (2) is therefore exp(ab)Q(b)-exp(aa_0)Q(a_0), with endpoints a_0,b.
No large-t estimate or numerical quadrature is used.

`scripts/adaptive-slope/direct-kernel-atomic-371.py` implements (2)
with 240-digit real Decimal intervals and complex rectangles. Each
real arithmetic operation uses separate ROUND_FLOOR/ROUND_CEILING
contexts; multiplication takes extrema of the four endpoint products.
Reciprocation requires exclusion of zero. Complex division uses
(x+iy)/(u+iv)=((xu+yv)+i(yu-xv))/(u^2+v^2), with its denominator checked.
Integers are exact and rational conversion is rounded outwards.

For exp(z), repeatedly divide by 2 until |Re z|+|Im z|<=1/8, sum its
series through degree128, and enlarge BOTH coordinates by

    2/(8^129 * 129!).                                    (3)

The tail modulus is bounded by (3): its first term is at most
1/(8^129*129!), and the subsequent term ratios are <=1/8, whose
geometric sum is <2. Repeated interval squaring then encloses the
original exponential. All finite sums and products are outward-rounded.
The budget exp(sqrt(n)) is enclosed by bounding sqrt(n) between
floor(10^80 sqrt(n))/10^80 and that rational plus 10^-80, using exact
integer square root before exponential enclosure.

### Rational witnesses and the finite certificate

A midpoint elimination of the n+1 band columns on the first n+1
slope atoms, with last weight one, merely GENERATES a candidate.
No rank, conditioning or exact-nullspace claim is inferred from it.
The candidate is scaled, truncated to integer real/imaginary numerators
at 120 decimal places, and divided by the integer sum of their absolute
values. The final stored weights are rational and satisfy EXACTLY

    sum_l (|Re w_l|+|Im w_l|)=1,

so their complex measure TV is <=1. This is a sufficient norm bound
on the witness; it does not alter the original complex coefficient cap.
The actual nonzero band leakage after rounding is retained in (1).
The finite enclosures give max|d_j|<3e-121 in every listed case.

For a complex rectangle, max of the two coordinate distance-to-zero
lower bounds is a lower bound for its modulus; the sum of the two
coordinate absolute upper bounds is an upper bound for its modulus.
Apply these respectively to T and every d_j. Subtract the outward
upper bound B_n max|d_j| from the lower bound for |T|, rounding down.
This proves the safe bounds in the table from (1). In these four cases
the resulting scores are positive. Nothing asserts witness optimality.

Reproduction commands, relative to this notebook, are

    python3 scripts/adaptive-slope/direct-kernel-atomic-371.py
    python3 scripts/adaptive-slope/direct-kernel-atomic-check-371.py

The first JSON stores ALL rational weights, kernel rectangles, target
and band pairings, budget bounds and downward-rounded lower scores.
The second script reads the exact saved weights and re-evaluates every
kernel entry and pairing; all matched, and the stated safe thresholds
passed. Full checking evidence is in
`scripts/adaptive-slope/direct-kernel-atomic-check-371.json`.

It also compares 40 selected kernel entries by a SECOND integral
formula: generate P by (j+1)L_(j+1)^(2)=(2j+3-t)L_j^(2)-(j+2)L_(j-1)^(2),
L_0=1, L_1=3-t; expand P about each interval midpoint; integrate its
product with the degree128 exponential series termwise. For half-length
h and M=(|Re a|+|Im a|)h, the omitted exponential is bounded by
2 M^129/129! whenever M/130<1/2, which is checked. Multiply this by
2h sum_j |p_shift,j| h^j and the enclosing midpoint exponential.
All 40 resulting rectangles overlap the antiderivative enclosures.
These comparisons check independent integral/normalization formulas;
they are not an all-n theorem or independent conceptual audit.

### Scope of the unsuccessful mechanism

For these chosen atoms, near-exact annihilation makes the target pairing
tiny along with the band pairing. The scaled certified scores decrease
over the four tested degrees. This supports parking this exact-null
construction pending a quantitative new input; it does NOT establish
an asymptotic upper bound on its scores, or exclude better atomic or
continuous witnesses. In particular the experiment scarcely uses the
coefficient cap: a witness allowing paid band leakage could retain
more target action. That tradeoff was untested in step371; step372's
bounded test follows.

### Step372: paid leakage with exact complex-TV normalization

The kernel and antiderivative enclosure(2)-(3) are reused without a
changed hypothesis. On each 4n+1 point slope grid, the generator
`scripts/adaptive-slope/direct-kernel-paid-leakage-372.py` encloses every
band and target entry. The full matrices are saved separately as
`scripts/adaptive-slope/direct-kernel-paid-leakage-matrix-16-372.json`
and the corresponding `matrix-32-372.json`. There is no continuum mesh
error to pay for a LOWER bound: each rational atomic measure tests the
actual complete kernel on I, including atoms at both endpoints.

Two finite-dimensional heuristics propose weights: projected complex
saddle iteration for Re(v* target)-B_n||M* v||_infinity with ||v||_1<=1,
and residuals of projected coefficient-constrained least squares. Here
M has the band columns, star denotes Hermitian transpose, and the
atomic weights are conjugate(v_l). The complex l1 projections use the
Euclidean modulus of each coordinate. Kernel entries are first divided
by a common Frobenius norm only for numerical candidate generation;
ALL certificate calculations use the original, unscaled kernel and cap.
There are 100000 iterations per generator per degree, with candidates
retained at iterations1000,10000,100000. No convergence, optimality,
Haar property or small-singular-value assertion is used. In particular,
the least-squares fit is not a continuum upper certificate. No spectral
cutoff, scalar representer damping or Taylor ansatz is introduced.

For each proposed vector, divide numerically by its largest coordinate
modulus, form integer numerators x_l,y_l by truncating the resulting
floating real/imaginary coordinates after multiplication by10^30, and set

    D=sum_l (isqrt(x_l^2+y_l^2)+1),
    w_l=(x_l+i y_l)/D.

The integer isqrt means the exact floor of the nonnegative square root.
Since sqrt(x_l^2+y_l^2)<isqrt(x_l^2+y_l^2)+1, these EXACT rational
weights have sum|w_l|<1. Floating iteration and rounding need satisfy
no other condition; only the final rational vector enters(1).

To avoid the previous coordinate-max/l1 modulus losses when leakage
is paid, step372 also encloses Euclidean moduli. For a nonnegative
rational or exact Decimal x, put

    r=isqrt(floor(10^200*x))/10^100.

Then r<=sqrt(x)<r+10^-100. Convert these rational bounds outward to
Decimal intervals. For a complex rectangle z, the sum of the squared
coordinate distances to zero is a lower bound on |z|^2. Outward
interval evaluation of (Re z)^2+(Im z)^2 gives an upper bound. Applying
the integer-root bounds to these two nonnegative numbers encloses |z|.
Use the lower endpoint for the target modulus, the largest upper
endpoint for band leakage, the outward upper exp(sqrt(n)) for the
budget, and downward subtraction for the pre-clipping score. Negative
scores are recorded before replacing them by the trivial lower bound0.
The same root enclosure bounds sqrt(n) in the budget calculation.

All twelve rational candidates, pairings and scores are saved in the
two degree-specific certificates `direct-kernel-paid-leakage-16-372.json`
and `direct-kernel-paid-leakage-32-372.json` under `scripts/adaptive-slope/`.
At n=16, the positive certified scores, rounded down, are
0.00434317868 (saddle100000), 0.00520444248 (least-squares10000), and
0.00380232699 (least-squares100000). The other three scores are negative.
At n=32, all six are negative; the largest pre-clipping score is between
-0.00566889857 and -0.00566889855 (least-squares100000). This is failure
of THESE bounded candidate searches, not an upper estimate for the
optimal weak certificate or E_32. No rank or optimization success is
inferred from the increasing iteration counts.

Reproduction commands, relative to this notebook, are

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/adaptive-slope/direct-kernel-paid-leakage-372.py
    python3 scripts/adaptive-slope/direct-kernel-paid-leakage-check-372.py

The checker successfully replays all 5556 kernel entries, all 12 rational
vectors and all pairings/scores. It also verifies TV<=1 independently with exact rational
upper bounds on each coordinate modulus at resolution10^-80, and
compares 18 selected kernels against the independent Laguerre-recurrence
and midpoint-integral formula described above. These cases include both
slope endpoints and the center, both band endpoints and the target,
at both degrees. Its complete result is saved in
`scripts/adaptive-slope/direct-kernel-paid-leakage-check-372.json`.
This is arithmetic replay and independent-formula comparison, not an
independent conceptual audit or an all-n theorem.

The n=16 finite improvement does not supply an asymptotic witness and
the n=32 search has no positive certificate. Park further iteration or
degree extensions of these two numerical generators without a new
quantitative input. The step373 audit below verifies these certificates
before analytic reuse. Formula(1) and its
fixed-grid/budget scope are neither strengthened nor stopped globally.

C997a(8), selected/both-sign transfer, assay/reconstruction, complements,
regulators, L993, unpaid L984(H), L966/L968 forcing and actual-Xi
positivity remain open. Prior Gaussian, Taylor, exact-chain and spectral
stops are neither reproved nor broadened by these finite certificates.

### Step373: independent conceptual audit of (1) and step372

11 November2026. RESEARCH / REPRODUCTION / ADVANCE, proof_audit under
unchanged EXPLORE review370. ADVANCE denotes local verification of an
existing finite input, not an asymptotic result or a discovery beyond
the checked sources. The step371 table was not separately replayed in
this audit; its own checking evidence and audit qualification remain.

**Complex pairing and scope.** The real functional is Re(sum A_j d_j),
with no conjugation in the displayed complex bilinear sum. Its support
function is exactly B_n max|d_j| by the single maximizing coefficient
given above; this is the stated realification of the cited Boyd--
Vandenberghe input, not a new minimax theorem. The generator's Hermitian
notation is compatible because its stored weights are conjugate(v_l).
The proof of (1) uses only the triangle inequality and a finite sum of
point evaluations. All atoms lie in the closed slope interval, so no
slope mesh error is missing. The band grid is the definition of this
particular E_n; it does not represent all possible band measures.
Endpoint atoms, complex phases and zeros of g_n cause no division or
regularity problem. No strong duality, Haar property, attained minimum
or infinite interchange is needed.

**Complete kernel and arithmetic.** Expanding cosh gives the two
exponents -1/8+iz and -7/8+iz with the factor -1 in (2). Subtracting
z's imaginary part in the real exponent is therefore correct for
z_star=1+i/8. The derivative of exp(at)Q(t) is exp(at)(Q'+aQ), and the
stated coefficient recursion gives Q'+aQ=P at every coefficient,
including the leading and constant ones. Here Im(a) is either 1 or a
positive gamma_j, so all primitive divisions are legitimate. Both
window endpoints and the subtraction from p_0 are present in the code.
Exact Fraction polynomial recurrence and binomial coefficients agree
at both degrees; neither computation removes any zero of P.

The Decimal interval operations use directed endpoint arithmetic;
reciprocal intervals reject zero and complex division encloses its
real squared-modulus denominator. Generic interval multiplication
across zero can give a negative square lower bound, but step372's
modulus code correctly replaces that lower bound by the sum of squared
coordinate distances. For x>=0 and integer s>0, set
r=isqrt(floor(s^2*x)). Then r^2<=s^2*x<(r+1)^2: the upper inequality
uses integrality of (r+1)^2. Hence r/s<=sqrt(x)<(r+1)/s, including x=0
and perfect squares. This justifies both the modulus and budget roots.
The integer normalization D strictly exceeds sum sqrt(x_l^2+y_l^2),
so every nonzero stored vector has complex TV<1. No floating proposal
or convergence assertion enters the proof after rationalization.

For the exponential enclosure, reduction to complex l1 radius 1/8
controls every point in the input rectangle. The degree128 tail is
bounded by (3); expanding both coordinates and interval squaring
preserve enclosure. In the alternate midpoint-integral calculation,
the polynomial expansion is finite and exact. The exponential tail
ratio after degree128 is at most M/130<1/2 in every checked case, so
the stated majorant controls the whole integral before multiplication
by its midpoint exponential. The eighteen overlaps corroborate a
second integration formula; they are not alone a proof of correctness
or independent verification of the shared exponential routine.

**Fresh replay and independent rational scores.** Re-ran the step372
checker: all 5556 kernel entries, all twelve rational witnesses, all
pairings and all eighteen alternate integrals passed. The additional
script `scripts/adaptive-slope/direct-kernel-conceptual-audit-373.py`
then recomputes all witness pairings from the complete saved kernel
rectangles using exact Fraction arithmetic. Each resulting rectangle
is contained in its saved Decimal pairing rectangle. It bounds TV and
complex moduli by exact integer square roots at resolution10^-120.
For the budget and exp(n/64), it uses an independent integer fixed-point
exponential with scale10^260: reduce a nonnegative input by64, sum
through degree128 with every integer quotient rounded outwards, add
the nonnegative tail upper bound (3), and square six times outwards.
The reduced upper endpoint is checked to be <=1/8. This enclosing
budget lies inside the original budget interval; the kernel exponential
itself remains verified by the preceding code and mathematical audit,
not by an independently implemented full kernel library.

Write [t_-,t_+] for the resulting target-modulus interval, [b_-,b_+]
for the budget interval and [d_(j,-),d_(j,+)] for each band modulus.
The EXACT score S=|T|-exp(sqrt(n))*max_j|d_j| satisfies

    t_- - b_+ max_j d_(j,+) <= S <= t_+ - b_- max_j d_(j,-). (4)

All quantities are nonnegative before the subtraction. The maximum
therefore preserves the band bounds, and the product endpoints have
the stated direction. Checking only a negative lower bound would not
prove S<0; this audit also checks its upper bound. Every stored lower
score is below the new exact-rational lower endpoint. At n=16 the
best stored candidate, index4, passes all four displayed thresholds
for target, leakage, E_16 and the scaled lower score. Its finite
conclusion E_16>0.00520444248 is accepted unchanged.

At n=32, (4) has a strictly negative upper endpoint for ALL six stored
vectors. Their largest exact score is between -0.00566889857 and
-0.00566889855. Thus each of these particular weak witnesses gives
only the trivial clipped lower bound. This proves no upper bound on
the optimal weak score or E_32 and excludes no other measure. The
script stores every rational pairing, modulus interval, two-sided
score, exact TV bound and input hash in
`scripts/adaptive-slope/direct-kernel-conceptual-audit-373.json`;
there are no failed assertions. Reproduce by running the step372
checker followed by the step373 audit script, from this notebook.

The finite bounds and formula(1) are accepted with their original
hypotheses. Optimality, any unbounded-subsequence lower rate, any
eventual continuum upper bound, and all listed actual-Xi/transfer
assumptions remain unpaid. This audit does not justify extending the
two numerical generators without new quantitative input.

## Mathlib

Full matching coverage for this complete-kernel finite certificate is
not checked and remains unknown. No Mathlib theorem is an input here.
The support-function result is imported by the precise external citation
above; the interval certificate is an executable informal calculation,
not a Lean proof or a formal verification of Python/Decimal.
