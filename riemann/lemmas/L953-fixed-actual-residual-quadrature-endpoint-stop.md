# Lemma 953: the fixed actual-residual endpoint quadrature is inconclusive

## Hypotheses

Use exactly L938's continuous actual density v, all34 signed rows,
twelve labelled factors, factorials and M_0^12 normalization. Retain
its degree256 rational kernel polynomial p,257 interpolation nodes,
theta cutoff8,precision200,grid10^-120 and complete residual bound
epsilon. Put k(x)=K(sqrt(x)) and r=k-p. Use L948's exact first
variation, its saved exact derivative prefixes through J=1411 and
its full second-order remainder. L952 supplies the pointwise payment
for every response degree1412 through2816 and the full polynomial
endpoint, with its original qualifications.

Numerical statements assume the inherited theta inclusion, exact-integer
derivative-prefix and full-polynomial execution, and L938's directed
Decimal/basic-operation/correctly-rounded-exponential contracts.
All contexts have precision200. Invalid operations, overflow, underflow,
subnormal arithmetic and zero-containing divisors are rejected.
Square-root bounds are checked by exact rational squaring. No residual
sign, independence, actual density sign, interval sign, tail onset,
all-degree mixed positivity or RH premise is assumed.

Use one fixed first-kind Gauss-Chebyshev rule with4096 integration
nodes and ellipse parameter3/2. These nodes do not change the257
original interpolation nodes. No parameter refinement is made.

## Conclusion

Subject to these contracts, the complete fixed calculation gives

    -1.235726925326931e-59 <= v(8) <= 1.260344965137188e-59.       (1)

The enclosure contains zero. The signed quadrature interval has radius
R_q satisfying

    1.248035930108511e-59 <= R_q <= 1.248035930108512e-59,
    101.3919824427741 <= R_q/v_(p,-) <=101.3919824427742,        (2)

where v_(p,-)>0 is L952's exact lower endpoint for v_p(8).
This prescribed endpoint test does not certify a sign and stops without
refinement. Its uncertainty radius is not a lower bound on the actual
residual response. It neither rejects positivity at8 nor refutes RH.
This is specialization of the assessed quadrature/approximation methods,
not a mathematical discovery beyond those methods.

## Proof

### Weight and normalization

Retain L948's f_(k,l), put t_(k,l)=8^l f_(k,l), and define

    Q_J(8,y)=sum_(k=0)^6 sum_(l=0)^1411
                   t_(k,l)y^(l+6-k)(1-y)^k,
    A(t)=y^11 r(8(1-y))Q_J(8,y),  y=(1+t)/2.

Every exponent l+6-k is nonnegative. L948(5)'s beta weight equals
y^11/sqrt(y(1-y)). The substitution t=2y-1 satisfies
dy/sqrt(y(1-y))=dt/sqrt(1-t^2), with no remaining factor2. Therefore

    J_prefix=pi^5*8^17 integral_-1^1 A(t)/sqrt(1-t^2) dt.        (3)

Import positive Gaussian weights and degree2n-1 exactness from
[NIST DLMF3.5.18-20_1](https://dlmf.nist.gov/3.5#E18), and the
first-kind Chebyshev nodes/weights from
[3.5.22-23](https://dlmf.nist.gov/3.5#E22), inspected in assessment104.
The Jacobi exponents are both-1/2>-1. The integer power y^11 belongs
in A; the original unweighted amplitude need not be bounded.
At n=4096 the nodes t_j=cos((2j+1)pi/8192) are interior and every
weight is pi/4096. The density-scale finite rule is exactly

    J_rule=pi^6*8^17/4096 *sum_(j=0)^4095 A(t_j).               (4)

Both endpoint neighborhoods are retained through the exact weight.
No ordinary bounded-integrand routine is applied at a singular endpoint.

### Complete analytic error

On the filled Bernstein ellipse rho=3/2, |t|<=13/12, hence
|y|,|1-y|<=25/24=:a. The argument8(1-y)=4(1-t) belongs to L938's
energy ellipse. L938 proves k is analytic on a neighborhood of the
filled ellipse, resolving the square root at zero by evenness, with
|k|<10^9. Write p(x)=sum_(l=0)^256 d_l T_l(x/4-1), with unchanged
rational coefficients. On the boundary,
T_l((w+w^-1)/2)=(w^l+w^-l)/2 gives |T_l|<=rho^l. The maximum-modulus
principle gives the same bound throughout the interior. Consequently

    P=sum_(l=0)^256 |d_l|rho^l,
    |r(4(1-t))|<=10^9+P.

No complex residual bound epsilon is assumed. Let B_k be rational upper
bounds for sum_(l=0)^1411 |t_(k,l)|a^l. Since each response monomial
is bounded by |t_(k,l)|a^(l+6), a complete analytic majorant is

    |A(t)|<=M:=a^17(10^9+P)sum_(k=0)^6 B_k.                  (5)

All retained degrees and all seven signed rows enter before this
absolute coefficient bound. No sampled ellipse maximum is used.

Import Trefethen, *Approximation Theory and Approximation Practice*,
Chapter8, Theorems8.1-8.2, equations8.1-8.3 and proofs,
[author's chapter](https://raw.githubusercontent.com/chebfun/ATAP/master/chap8.m),
version inspected9November2026 in assessment104 (commit not pinned).
For analytic A bounded by M, its degree8191 Chebyshev projection has
uniform error delta=2M rho^(-8191)/(rho-1) on[-1,1]. Gaussian exactness
applies to that entire projection. Positivity and the full mass pi pay
both the integral error and finite-rule error by pi delta each. Thus

    |J_prefix-J_rule|<=U_quad:=2pi_+^6*8^17 delta,
    4.488295806202826e-1236<=U_quad<=4.488295806202827e-1236.    (6)

Degree8191 is exactly2*4096-1. The projection need not be computed.
The two-sided display encloses the computed upper allowance, not the
actual integration error. The amplitude is analytic; an absolute-value
function is not substituted into the analytic approximation theorem.

### Full finite evaluation

With h=17-k+l and O_h=product_(s=1)^h(2s-1), the exact coefficients are

    t_(k,l)=d_(k,l)2^(h+3l)/[2C^11(2k)!O_h].

This follows from L948's4^h h!/(2h)!=2^h/O_h. All9884 rational
coefficient inclusions are checked at precision200. Their absolute
upper endpoints, evaluated by positive directed Horner at an interval
for a, yield B_k in(5). Nonnegative operands make each upper Horner
step an upper bound for the entire exact absolute sum, by induction.
P and the remaining scalars in(5)-(6) are evaluated as exact rationals.

Each node angle uses the inherited positive pi interval. Cosine uses
the degree256 Taylor polynomial and complete4^258/258! remainder
from L938, with every angle in[0,4]. The full node interval propagates
through y,x=8(1-y), and the square root. Exact rational squaring checks
both square-root endpoints and0<u<3. L019's eight theta terms are
evaluated with directed exponentials, then enlarged by L938(14)'s full
omitted positive tail tau=256*9^4*10^6/20^81.

The original rational p is evaluated by interval Clenshaw at-z,
where z encloses the node cosine. With zero terminal values,
b_l=d_l+2(-z)b_(l+1)-b_(l+2) gives p=d_0+(-z)b_1-b_2.
Interval induction encloses its exact value, including overestimation
from repeated uncertain arguments. Subtraction retains both complete
kernel and polynomial intervals; no residual midpoint replaces them.

Each F_k(y)=sum_l t_(k,l)y^l is evaluated by directed Horner. As y>=0,
a lower accumulator L uses y_- when L>=0 and y_+ when L<0, with
downward rounding. An upper accumulator U uses y_+ when U>=0 and y_-
when U<0, with upward rounding. Adding enclosing coefficient endpoints
preserves inclusion at every step. All seven F_k are combined with
y^(6-k)(1-y)^k, then multiplied by the full residual and y^11.
The signed sum and scale(4) retain every finite-evaluation error.
The resulting complete finite interval satisfies

    -1.248035930108512e-59<=J_rule<=1.248035930108512e-59.      (7)

Its center is about-5.054e-78; this midpoint is not a sign certificate.
At the saved widest amplitude node j=127, x is about0.01911103.
The residual is sharply positive near3.87845e-58, while the response
interval straddles zero near[-6.72203e-19,6.72203e-19]. This is concrete
evaluation-overestimation evidence in this execution, not an actual
response magnitude or an obstruction to every other evaluator.

### Every remaining payment and the endpoint comparison

L952's pointwise complement retains(l+17)!, first omitted degree1412,
and ratio256/1430, paying every response degree through2816. Its
actual-density allowance and the unchanged L948/L952 remainder are

    U_tail=epsilon*pi_+^6*T_8,
    1.403015658127793e-112<=U_tail<=1.403015658127794e-112,
    U_2=66 epsilon^2 8^10*pi_+^6 Z*8^17,
    Z=(293/540)/(2^36*17!),
    1.512354696858995e-67<=U_2<=1.512354696858996e-67.          (8)

All terms with at least two residual factors are paid. The bounded
interpolating amplitudes and positive simplex beta parameters are
exactly those in L948, including every singular face. No integrated
cell allowance or exp(4/5) enters this pointwise ledger.
L952's full3073-coefficient endpoint gives [v_(p,-),v_(p,+)], with
1.230901990512815e-61<=v_(p,-)<=1.230901990512816e-61.
For the full finite interval[q_-,q_+] in(4),

    v(8) belongs to
    [v_(p,-)+q_--U_quad-U_tail-U_2,
     v_(p,+)+q_++U_quad+U_tail+U_2].                          (9)

Exact rational comparisons give(1)-(2). The finite-evaluation radius
exceeds the polynomial endpoint by over101; the tiny external payments
cannot repair the achieved inclusion. No lower bound on actual error
has been proved. Zero inclusion ends this fixed test without changing
the evaluator, precision, nodes, prefix, kernel or polynomial.

### Reproduction and replay scope

Run in order:

    python3 scripts/heat/l938-actual-residual-signed-integration-106.py
    python3 scripts/heat/check-l938-actual-residual-signed-integration-106.py
    python3 scripts/heat/summarize-l938-actual-residual-106.py

Full certificates are `scripts/heat/l938-actual-residual-signed-integration-106.json`,
`scripts/heat/l938-actual-residual-signed-integration-check-106.json`, and
`scripts/heat/l938-actual-residual-diagnostic-106.json`. All4096 node,
kernel, polynomial, residual, seven response-row, amplitude and running-sum
intervals are saved in `scripts/heat/l938-actual-residual-nodes-106.json`.
The producer passes22188 checks with no arithmetic failures.

The separate replay passes36880 checks with no failures. It consumes all
nodes, checking their angle/affine/root/residual/response/amplitude
contractions by exact rational comparisons. It independently sums every
saved amplitude endpoint, checks every partial sum, the pi and energy
scale, both Gaussian error masses, all payments and both final endpoints.
All11 diagnostic outward-display comparisons pass. Input hashes bind
reused artifacts to inherited reports. Complete final comparisons and
all check flags are consumed; previews are not used as verification.

The replay does not independently produce theta/cosine values, node
Clenshaw/Horner values, B_k absolute sums, derivative prefixes or the
full density polynomial. Their analytic/code arguments and execution
contracts remain explicit above; this is not a separate conceptual
audit of those implementations. The actual sign, interval coverage,
infinite join, outer mass, head/global variation, independent mixed
signs, contacts, initialization and realization remain unresolved.

## Mathlib

Full or supporting Mathlib coverage for this specialized certificate
has not been checked; unknown availability is not absence. Imported
methods are positive weighted Gaussian exactness and analytic Chebyshev
projection error, with the local beta/Taylor/theta qualifications retained.
No inspected source guarantees the favorable sign or execution accuracy.
