# C998v: Audited zero-inclusive Gaussian compression; implementation cost stop

## Hypotheses

Use C998u's unchanged kernel and error-transfer contract

    a_j=2j+1/2, G(r)=sum_(j>=0)exp(-a_j r)/a_j^2,
    B=2^23, ell=log(3)/2, ||Dh||_TV<B.

For the eventual scalar retain all of C998u's hypotheses: the exact
C998r witness, C999l completion, all334 shifts, identity2187,512 modes,
full K14, exact P0, analytic-response/neutral-core and IEEE754/Decimal
qualifications and unreplayed c_*. None is strengthened here. The
approximation itself is a statement about this explicit scalar G and
does not need a numerical value of h. No inverse estimate, RH,
positivity of the full form or cross-notebook result is assumed.

The invocation-start assessment726/comparison727 is SPECIALIZE for
the exact block-construction test. Import, rather than reprove:

- Yohei M. Koyama, *Exponential sum approximations of finite completely
  monotonic functions*, [arXiv:2301.08931v3](https://arxiv.org/pdf/2301.08931v3),
  Lemma2.2/proof p3, Lemma2.6 p5, Theorem2.14(48)/proof pp7-8 and
  AppendixC.1(C.1)-(C.3) pp41-42. For a bounded positive Stieltjes
  measure on [a,b],0<a<b, with at least m+1 support points, linear
  spectral parametrization gives positive m-node Gaussian weights and
  interior nodes, exactness through degree2m-1, mass exactness, and
  uniform exponential error at most (16/pi)rho^(-2m)f(0) for r>=0,
  rho=(1+sqrt(a/b))/(1-sqrt(a/b)). Discrete measures are allowed;
  no density assumption from the numerical examples is imported.
- G.H. Golub and J.H. Welsch, *Calculation of Gauss Quadrature Rules*,
  Math.Comp.23(106)(1969),221-230,
  [published paper](https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf),
  Section2/(2.1)-(2.6),pp222-223 and Section4/(4.1)-(4.3),pp226-227.
  Only the positive-inner-product orthogonal-polynomial Gaussian
  construction is used. The finite algebra applies to our discrete
  measures because their moment forms are positive definite below.
- [DLMF2.10.1](https://dlmf.nist.gov/2.10.E1), the exact
  Euler--Maclaurin formula including its periodic-Bernoulli remainder,
  and [DLMF24.4.9](https://dlmf.nist.gov/24.4.E9), finite power sums.
  The explicit telescoping implementation below is finite algebra
  specializing the latter, not an asymptotic approximation.

These sources do not establish our finite precision or cost. The local
specialization and arithmetic evidence below address the approximation;
the complete operation/storage ledger remains unresolved. The need for
this specialization is the unchanged discrete, unbounded spectrum and
its absolute tolerance including r=0. No novelty beyond checked
Gaussian/moment methods is claimed.

## Conclusion

There is a positive1171-term exponential sum Gtilde, explicitly
specified below and by the finite-decimal coefficients in
`scripts/separation-seven/spectral-block-compression-728.json`, such that

    B^2 sup_(r>=0)|G(r)-Gtilde(r)| < 7.353*10^-9 < 10^-7.       (1)

In particular the estimate includes r=0 and [0,ell]. By C998u Section2
the same number bounds the absolute error in the full signed-measure
pairing; it does not replace the density by atoms.

The construction run uses256-digit directed Decimal arithmetic. All67
compressed blocks have17 sign-isolated real nodes and positive weights;
a separate exact Fraction replay passes4764 finite checks. The first
100-digit implementation failed already at the first compressed block;
its certificate is preserved. The successful approximation is a local
REPRODUCTION/specialization. Separate conceptual audit729 in Section5
upholds it, including independent moment/recurrence regeneration.

**The728 Python implementation fails the full-work gate.** Under the
explicit source-operation convention in Section5, its mandatory root
bisections alone require at least113,912,529 operations>10^8. This counts
arithmetic, comparisons, assignments and loop control, as required by
the all-work contract; it is not an arithmetic-only count or a lower
bound for other algorithms. There is still no working-memory bound.
No scalar, density quadrature, S3 sign, H2 or RH conclusion follows.
Remaining9e-7 and all later costs stay unpaid.

## Proof

### 1. Disjoint blocks, infinite tail and Gaussian budget

Keep j=0 and blocks j=2^k,...,2^(k+1)-1 for k=0,...,4 exactly.
Together these are precisely j=0,...,31, with their exact positive
rational weights1/a_j^2 and rates a_j. For k=5,...,71 let J=2^k
and put the atoms j=J,...,2J-1 into the artificial interval[2J,4J].
Indeed 2J<a_j=2j+1/2<4J. No atom lies on an artificial boundary;
the j-index intervals are disjoint and cover32,...,2^72-1 exactly.

Each compressed block has J>=32>17 support points, so the cited
m=17 theorem applies. Its linear parametrization gives

    a/b=1/2, rho=3+2sqrt(2)>5.

Let Gstar use these exact Gaussian rules and retain the32 original
atoms. For j>=1, decreasing-function comparison gives

    sum_(j>=1)a_j^-2 <= (5/2)^-2+integral_1^infinity(2x+1/2)^-2 dx
                       =4/25+1/5<1.

Thus G(0)<5. Sum the uniform block errors, using16/pi<6, positivity
of all block masses and their total mass<G(0): the Gaussian part has
error<30*5^-34. For N=2^72, C998u's decreasing integral estimate gives
the uniform omitted tail<=1/(4N-3). This remains valid at zero;
no differentiation of G or positive separation is assumed. Therefore

    B^2 sup|G-Gstar|
      < 30*2^46/5^34 + 2^46/(4*2^72-3)
      =16167367974709495237421575724286869504
        /2199023255551999999999650754034519195556640625
      <7.353*10^-9.                                      (2)

The rank is32+67*17=1171. This analytic existence/rank bound alone
would not certify coefficients, precision or affordability.

### 2. Finite moments without visiting the original enormous prefix

For each block define x_j=(j+1/4)/J in(1,2), t_j=2x_j-3 in(-1,1),
and the positive measure nu_J=(1/J)sum_j x_j^-2 delta_(t_j).
The original spectral block is

    (1/(4J)) integral exp[-J(t+3)r] dnu_J(t).             (3)

A nonzero polynomial of degree<=17 cannot vanish at all J>=32
distinct points. Its squared norm is positive, proving the required
moment-matrix positive definiteness, not just numerical nonsingularity.

The constructor encloses moments through degree34. Before the t
change of variable, let mu_p=(1/J)sum x_j^(p-2). For J<256 it
enumerates at most128 atoms using exact Fractions. For larger J set
u=J+1/4, v=2J+1/4. Write S_q=sum_(j=J)^(2J-1)(j+1/4)^q.
The exact telescoping identity yields

    S_q=[v^(q+1)-u^(q+1)
           -sum_(l<q)binom(q+1,l)S_l]/(q+1),
    mu_(q+2)=S_q/J^(q+1), q=0,...,32.                  (4)

Thus positive powers require no loop of length J. The remaining
moments are mu_0=J sum(j+1/4)^-2 and mu_1=sum(j+1/4)^-1.
Apply the cited exact Euler--Maclaurin formula on the integer j
interval[J,2J], then remove the right endpoint. For f_s(j)=(j+1/4)^-s,
s=1,2, its main terms are respectively

    sum f_1 = log(v/u)+(u^-1-v^-1)/2
       +sum_(r=1)^63 (B_(2r)/(2r))*(u^(-2r)-v^(-2r))+R_1,
    sum f_2 = u^-1-v^-1+(u^-2-v^-2)/2
       +sum_(r=1)^63 B_(2r)(u^(-2r-1)-v^(-2r-1))+R_2. (5)

Both endpoints and the signs of the odd derivatives are retained.
Let C=|B_128|+sum_(l=0)^128 binom(128,l)|B_l|. The Bernoulli
polynomial formula bounds |B_128-Btilde_128(y)|<=C for all real y
using its fractional part in[0,1]. The absolute derivative integrals,
extended to infinity only to enlarge the bounds, give

    |R_1|<=C u^-128/128,  |R_2|<=C u^-129.            (6)

This follows directly by inserting f_1^(128)=128!(j+1/4)^-129
and f_2^(128)=129!(j+1/4)^-130 into DLMF2.10.1's remainder.
All Bernoulli numbers and the bounds in(6) are exact Fractions.

For the logarithm, z=(v-u)/(v+u) lies in(0,1/3). The constructor
uses2 sum_(i=0)^255 z^(2i+1)/(2i+1), adding a nonnegative remainder
bounded by2/(513*3^513)*(9/8). This is the integrated geometric
series with its explicit positive remainder, evaluated by intervals.
Finally the t moments are the finite binomial transformation

    integral t^n dnu_J=sum_(q=0)^n binom(n,q)2^q(-3)^(n-q)mu_q.

All potentially severe cancellation is retained in outward intervals.
This specifies an effective moment recipe, not an empirical smooth
density replacement or use of an asymptotic Euler--Maclaurin series.

### 3. Orthogonal polynomials, isolated roots and weights

Use monic polynomials p_0=1, h_n=integral p_n^2 dnu_J and

    alpha_n=integral t p_n^2 dnu_J/h_n,
    beta_n=h_n/h_(n-1),
    p_(n+1)=(t-alpha_n)p_n-beta_n p_(n-1),             (7)

with the beta term omitted at n=0. These are the cited positive
inner-product construction. To fix the normalization/sign without
using the suspect intermediate recurrence line noted in assessment727:
symmetry of the inner product eliminates degrees<=n-2 from t p_n;
its coefficient along p_(n-1) is h_n/h_(n-1), since t p_(n-1) is
monic of degree n. Its coefficient along p_n is alpha_n. This gives(7).

The code evaluates every displayed integral using moments, preserving
all coefficient uncertainties. Every computed norm interval has a
strictly positive lower bound. Positive discrete support and Gaussian
quadrature give17 simple interior roots of the exact p_17. Numpy
provides initial guesses only. Around each guess the constructor
requires opposite **interval-certified** signs at real endpoints,
then bisects with sign certification to width<=10^-40. The67 sets
each have17 mutually disjoint intervals inside(-1,1), hence contain
all roots, exactly one each. No accuracy of a floating root guess
is used as evidence; failure of sign certification stops the block.

For an exact root t_i, its Gaussian nu_J weight is

    lambda_i=1/[sum_(n=0)^16 p_n(t_i)^2/h_n].         (8)

This is finite algebra from the imported polynomial exactness: if
ell_i is the degree16 cardinal polynomial at the17 Gaussian nodes,
exactness on ell_i p_n says its coefficient in the orthogonal p_n
basis is lambda_i p_n(t_i)/h_n. Evaluate that expansion at t_i,
where ell_i(t_i)=1, to obtain(8). This does not import an additional
unassessed numerical eigensolver or a quadrature formula for a density.

Evaluate(8) by intervals over each entire root bracket and divide by
4J, as required by(3), to enclose the original spectral weight w_i.
All weight enclosures are strictly positive. Their midpoint output
wtilde_i is a positive exact finite decimal; likewise ttilde_i is
the exact finite-decimal bracket midpoint. Output rate
atilde_i=J(ttilde_i+3)>0 is exactly representable at the working
precision and checked as an exact rational in the replay.

For each saved bracket define delta_t=max|t_i-ttilde_i| from its
two endpoints and delta_w similarly from the weight enclosure.
For r>=0 the derivative of exp[-J(t+3)r] in t has modulus
Jr exp[-J(t+3)r]<=Jr exp(-2Jr)<=1 throughout these brackets.
The mean-value theorem therefore gives the uniform bound

    |w_i exp[-J(t_i+3)r]-wtilde_i exp[-atilde_i r]|
       <=delta_w+wtilde_i delta_t.                  (9)

The constructor sums(9) outward; the replay sums the reported bounds
as exact Fractions. Across all1139 Gaussian nodes, after multiplying
by B^2, that contribution is<3*10^-25. The32 exact atoms have zero
coefficient error. Equations(2) and(9) prove(1), with the looser
7.353*10^-9 rounded upward only after the exact comparison.

### 4. Evidence and limits of the effective claim

Run, from the notebook directory:

    python3 scripts/separation-seven/spectral-block-compression-728.py
    python3 scripts/separation-seven/spectral-block-compression-replay-728.py

The constructor's JSON retains every transformed moment, orthogonal
polynomial, norm, root bracket, positive weight enclosure, output
rate/weight and block error bound. The exact Fraction replay reads
all67 blocks and re-evaluates every endpoint sign and Christoffel
weight enclosure, checks output constants, disjointness, full root
counts and the uniform coefficient budget. All4764 checks pass.
It does **not** independently regenerate the moment intervals or
orthogonal recurrence, prove the source theorems, or certify work.
Those analytic justifications are above; separate audit remains due.

The preserved first-pass JSON records failure at100 digits: interval
propagation in(7), including cancellation and small positive norms,
made the first p_17 root brackets undecidable. Increasing to256 digits
and the specified256-term logarithm rule resolved this particular
failure. This is evidence of conditioning cost for this implementation,
not a proof of a minimum necessary precision or a source obstruction.

The successful constructor reports31,149,701 directed Decimal basic
operations,19,229,836 selected Decimal comparisons and122,819
high-level Fraction calls. These are **subtotals**: they exclude
integer algorithms inside Fraction, numpy guesses, host control,
allocation/output and the separate replay; not all assignments or
guards are counted. In particular, summing these numbers does not
establish the<=10^8 all-work condition. The saved constructor JSON is
10,038,511 bytes, an observed file size, not a peak-memory bound.
There is no certified construction or storage upper bound yet.

At the end of attempt728 the original acceptance test remained unfinished.
If a complete ledger exceeds10^8, stop this implementation while
retaining(1). If an essential construction step remains unpaid, do not
declare affordability. Passing a later ledger would pay only kernel
preparation; density/mixed interactions, h preparation, local term,
rounding in the scalar, other entries/endpoints, S3,H2 and actual-Xi
global assembly remain independent open tasks. Preserve all prior
raw-prefix and other implementation stops; none excludes this
different kernel approximation.

### 5. Separate conceptual audit729 and a mandatory-work lower bound

The prior SPECIALIZE assessment726/comparison727 is reused for this
same construction test. No new general approximation theorem is asserted.
Audit729 checks the original proof and both728 scripts, including the
previously unreplayed moment and orthogonalization link.

The block partition puts exactly j=0,...,31 into the exact part and
j=32,...,2^72-1 into the67 Gaussian blocks. Each discrete positive
measure has at least32 support points, so its squared-polynomial
inner product is positive through degree17. Thus the imported Gaussian
existence, simple interior roots and polynomial exactness apply without
a density assumption. Both inverse-moment remainders in(6) have the
correct derivative factors: integration divides the128th derivative
of f_1 by128 and that of f_2 by129, cancelling the extra129 in the
latter. The right endpoint in(5) is subtracted once. The power-sum
telescoping and t=2x-3 transformation are exact finite identities.
The256-term logarithm remainder starts at exponent513 and is positive.

The independent audit implementation recomputes all35 moments in each
block at320 Decimal digits. For the small blocks it uses exact rational
powers directly. For the other blocks it sums the Euler--Maclaurin
corrections as exact rationals, adds the exact rational remainder bounds,
and encloses the logarithm separately. Thus it does not use the728
moment intervals as mathematical premises. Every regenerated moment
interval is contained in the corresponding saved interval. A separately
implemented monic recurrence then regenerates all17 positive norms,
all coefficients of p_0,...,p_16 and the final p_17, and checks containment
in the saved intervals. Interval dependency can widen these enclosures;
it cannot invalidate inclusion of the exact inner products and recurrence.
This closes the link omitted by the728 finite-root replay, subject to
the inherited correctly directed Decimal contract.

The exact Fraction root/weight replay is run again into a separate729
artifact. Its4764 checks pass. They use the now-validated polynomial
and norm intervals:17 disjoint sign changes enclose all degree17 roots,
and(8) gives their positive weights with the normalization1/(4J).
The two contributions in(9) use the output weight in the exponential
perturbation and the exact weight difference in the other term, so
no missing cross term is required. All root brackets lie inside(-1,1),
which supplies the claimed uniform exponential derivative bound.
The exact total, including coefficient errors, is less than7.353e-9;
the audit checks this stronger rounded bound, not merely1e-7.

For cost, fix the following **source-operation convention**: each
scalar arithmetic operation or comparison, explicit variable binding
or attribute store, and successful loop advance costs at least one
unit. This includes the control and assignment work expressly left
unpaid728. Count no function calls, attribute reads, allocations, failed
loop tests, integer internals, numpy work, reporting or replay. Such
omissions only decrease a lower bound in this convention. It is not a
claim about measured time, CPU instructions, a compiled optimization,
or a convention counting only high-level numerical arithmetic.

In `roots`, each of67*17 roots begins with a bracket of width at least
2e-7. It must reach width<=1e-40. On(-1,1), the two256-digit directed
midpoint operations together err by less than1e-254. Consequently a
child width is at least half its parent's width minus1e-254. After110
steps the width is at least

    (2e-7)/2^110 - 2e-254 > 1e-40.

Thus at least111 iterations are mandatory, independent of guess quality
and without assuming exact midpoint arithmetic. The saved final widths
also all equal(2e-7)/2^111. Each iteration evaluates p_17 by17 Horner
steps. Count only the following operations in ONE such step, directly
from `evaluate`, `I.__mul__`, `I.__add__` and `I.__init__`:

| Operation | Units | Source accounting |
| --- | ---: | --- |
| Directed Decimal arithmetic | 10 | Eight endpoint products and two endpoint sums. |
| Decimal comparisons | 8 | Three for min, three for max, and one constructor order check in each of the product and sum intervals. |
| Explicit bindings/stores | 22 | Product: b(1), comprehension x/y bindings(12), lows/highs(2), constructor endpoints(2); sum: b(1), constructor endpoints(2); Horner: a and value(2). |
| Successful loop advances | 13 | Two product comprehensions each have two outer and four inner advances; the Horner loop has one. |

The comparison and store counts refer to distinct executed source
operations. There are no charges here for the counter instrumentation
or for a Decimal operation's internal work. The constructor's initial
endpoint evaluations and final endpoint checks are also omitted.
Therefore this mandatory subtask alone costs at least

    67*17*111*17*(10+8+22+13)
      = 2,149,293*53 = 113,912,529 > 100,000,000.       (10)

This is enough to reject the728 implementation under its all-work
contract before costing moment preparation, root guesses, weights,
validation or storage. The old31,149,701 arithmetic subtotal is not
contradicted: it omits the source work now counted. The positive
approximation(1) survives; no lower bound on the work of a different
quadrature construction, residual verifier or optimized implementation
is established. Reopening needs a concrete different prescription with
its own paid preparation and validation, not free reuse of expensive
candidate generation or removal of control costs from this ledger.

Reproduce the audit from the notebook directory:

    python3 scripts/separation-seven/spectral-block-compression-audit-729.py

The full regenerated interval evidence, source hashes,15020 audit
checks, exact error comparison and work calculation are saved in
`scripts/separation-seven/spectral-block-compression-audit-729.json`.
The separate full4764-check root/weight replay is
`scripts/separation-seven/spectral-block-compression-enclosure-replay-729.json`.
No728 artifact is overwritten. All checks pass; the cost inequality
is an informative negative result for this implementation. Storage
and all density/scalar/sign/global obligations remain unpaid; after
the strict cost failure an upper bound for those costs is unnecessary
to reject this prescription. No complete-solution candidate results.

## Mathlib

The full matching zero-inclusive compression, its finite discrete
Gaussian construction, and the effective certificate have not been
checked in Mathlib. No absence claim is made. The informal proof uses
the precise primary inputs above and the local finite evidence, not
a claimed formalization. The construction/cost distinction remains
part of the conclusion.
