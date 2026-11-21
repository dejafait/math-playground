# Corollary C033e: fixed rational gamma-node approximation

## Hypotheses

Let sigma be real with1<=sigma<=2 and w complex with|w|<=2.
Fix precisely C033b's n=4096, h=1/256 and

    v_j=(j+1/2)/256=(2j+1)/512, j=0,...,4095.

For positive real v use its exact integrand

    G(v)=exp(-sigma*v^2-v/2), C(v)=cosh(w*v)-1,
    D(v)=v*(1-exp(-2v)), I(v)=G(v)*C(v)/D(v).

Set N=2336 and P(z)=sum_(k=0)^N z^k/k!. Define the fixed expression

    Gtilde_j=P(-sigma*v_j^2-v_j/2),
    Ctilde_j=(P(w*v_j)+P(-w*v_j))/2-1,
    Dtilde_j=v_j*(1-P(-2*v_j)),
    Q(sigma,w)=(1/256)*sum_(j=0)^4095 Gtilde_j*Ctilde_j/Dtilde_j. (1)

Every operation in(1) means exact arithmetic. This claim concerns
the compact mathematical sum, without a floating-point stability or
runtime claim. It requires no RH or information about zeros.
Any later use as a divisor/probability-law gamma component retains
all qualifications recorded in C033b: the inherited normalization,
multiplicities, no-ordinate-zero, strip/counting and finite-zero,
heat and fixed-v1 hypotheses are not independently verified here.

Import the analytic Taylor remainder from *Complex Analysis*,
[Section7.2, Theorem7.2.3](https://complexanalysis.org/web/sec_taylor-series.html),
proof(7.2.3)-(7.2.7), including Lemma7.2.2: for an analytic f on a
domain containing D_R(0), |z|<=r<rho<R, the degree-N Taylor remainder
has modulus at most

    M*rho/(rho-r)*(r/rho)^(N+1), M=max_(|zeta|=rho)|f(zeta)|. (2)

The complete relevant proof and hypotheses were inspected in
source-notes1699 under assessment1698; this theorem is imported,
not reproved. NIST DLMF v1.2.8,
[4.2.19](https://dlmf.nist.gov/4.2.E19),
[4.2.22](https://dlmf.nist.gov/4.2.E22) and
[4.28.2](https://dlmf.nist.gov/4.28.E2) supply respectively the
exponential factorial series, |exp z|=exp(Re z), and the complex
cosh exponential identity. Source coverage is reused unchanged.

## Conclusion

Every Dtilde_j is a positive rational number greater than2^-24.
Thus(1) is a fixed rational-coefficient expression defined on the
entire stipulated closed domain. In fact its denominators are
constant rational numbers, so Q is a polynomial in sigma,w with
rational coefficients. Uniformly on that domain,

    |Q(sigma,w)-h*sum_(j=0)^4095 I(v_j)|<=2^-135<1/64.   (3)

All4096 nodes and the original panel count are retained, with no
adaptive panels, parameter samples or unstated working precision.
This is a local specialization/reproduction of standard Taylor
approximation, not a mathematical discovery beyond the checked
sources. Separate critical audit1703 below accepts this specialization
without changing its formula, degree, nodes or parameter domain.

It supplies only the node-approximation component. Quadrature, tail
recombination, coefficient amplification, other evaluator terms,
the variation-2 residual<1/2 and unsmoothed Xi realization are separate
obligations. No all-degree positivity or RH conclusion is claimed.

## Proof

### 1. One explicit remainder for all elementary factors

Put eps=2^-256. The exponential is entire, so in(2) take r=520,
rho=1040 and any R>1040. Its Taylor polynomial is exactly P.
On the circle |zeta|=1040, the cited modulus identity gives
|exp zeta|<=exp(1040). The elementary e<3 bound already proved in
C033b gives exp(1040)=e^1040<4^1040=2^2080. Consequently

    |exp z-P(z)| <= 2*exp(1040)*2^-2337
                  < 2^(1+2080-2337)=eps, |z|<=520.      (4)

We may use the non-strict bound eps below. This is a complex-disk
estimate from the imported theorem, without a complex mean-value point.

At all stipulated nodes, 1/512<=v_j= (2j+1)/512 <16. The closed
parameter bounds imply

    |-sigma*v_j^2-v_j/2|<=2*16^2+16/2=520,
    |w*v_j|<=32, |-w*v_j|<=32, |-2*v_j|<=32.

Thus(4) applies to every argument of P in(1). For any one of these
nodes, suppress its subscript. The cosh identity and the triangle
inequality yield

    |Gtilde-G|<=eps, |Ctilde-C|<=eps,
    |Dtilde-D|<=v*eps<=16*eps.                          (5)

The two exponential errors defining Ctilde are averaged, so no
extra factor2 occurs. These uniform estimates include w=0, the
boundary circle|w|=2 and both sigma endpoints.

### 2. Denominator separation at every node

C033b proves, for real v>=0,

    B(v)=(1-exp(-2v))/(2v)>=1/(1+2v), v>0.

Since v<=16 and v>=1/512, the exact positive denominator satisfies

    D(v)=2*v^2*B(v)>=2*(1/512)^2/33
                        =1/(33*2^17)>2^-23,            (6)

where the last comparison is33<64. P has real rational coefficients
and -2v is rational, so Dtilde is real rational. By(5)-(6),

    Dtilde>=D-16*eps>2^-23-2^-252>2^-24.               (7)

The final inequality follows from2^-252<2^-24.
This proves a common positive separation including the smallest
node. It uses no zero assumption or numerical evaluation of P.
As each v is a fixed rational, all Dtilde are constant nonzero
rationals, which also proves the coefficient assertion about Q.

### 3. Full product, quotient and sum error

Here 0<G<=1 because sigma,v are positive. The cosh identity gives
|cosh(wv)|<=exp(|wv|)<=exp(32)<2^64, again using e<3<4.
Consequently

    |C|<=2^65, |Gtilde|<=1+eps<=2.

Write U=G*C and Utilde=Gtilde*Ctilde. The exact identity

    Utilde-U=(Gtilde-G)*C+Gtilde*(Ctilde-C)

and(5) imply

    |U|<=2^65,
    |Utilde-U|<=(2^65+2)*eps<=2^66*eps.                (8)

For the quotient use

    Utilde/Dtilde-U/D
         =(Utilde-U)/Dtilde + U*(D-Dtilde)/(Dtilde*D).

Equations(5)-(8) give, at every node and uniformly in the parameters,

    |Utilde/Dtilde-U/D|
       <=2^66*eps*2^24 + 2^65*16*eps*2^24*2^23
       =(2^90+2^116)*eps <=2^117*eps.                 (9)

All quotient factors have now been controlled before summation.
There are precisely4096 summands and their weights are h=1/256>0,
whose total is16=2^4. The triangle inequality and(9) therefore yield

    |Q-h*sum_j I(v_j)|<=2^4*2^117*2^-256=2^-135<2^-6.

This proves(3). When w=0, P(0)=1, so Ctilde=C=0 exactly and Q=0;
there is no division by w. No endpoint of the stipulated parameter
domain is excluded. The singular integration endpoint v=0 is not a
node and has not been deleted from the quadrature rule; the unchanged
rule's endpoint regularity belongs to C033b, not to a new node choice.

### 4. Exact arithmetic check and limits

Run, from the active notebook,

    python3 scripts/gamma-midpoint/node-rational-certificate-1700.py

It writes the complete rational comparison certificate to
scripts/gamma-midpoint/node-rational-certificate-1700.json and prints
the actual/required error bounds, denominator separation, failures and
artifact path. It checks the node range, Taylor exponent and every
rational comparison in(6)-(9). It does not evaluate a sampled function,
certify floating-point evaluation or replace the analytic proof above.

The degree2336 and extremely loose envelope are sufficient for
existence of this fixed expression. Computational practicality has
not been investigated. Coefficient-weighted accuracy in a complete
evaluator is not implied by the component budget1/64. Other gamma
errors, independent evaluator terms, signed upper bounds and the
main RH-equivalent positivity gap remain open.

### Critical audit1703 — 19 November2026

Under the preexisting SPECIALIZE assessment1700 (separately approved1701,
source URLs repaired1702), this independent audit accepts (1)-(3).
The imported Taylor theorem and elementary identities are reused with
their exact hypotheses; no new theorem or source discovery is claimed.
The audit is REPRODUCTION, and establishes only this local evaluator
component. The following checks are analytic, separately from arithmetic.

**Taylor indexing and closed domain.** The exponential is analytic on
the whole plane, so its domain contains D_R(0) for any R>1040. The
circle of radius1040 lies strictly inside it, and520<1040. The cited
degree-N remainder contains N+1=2337, not2336. Its prefactor is
1040/(1040-520)=2; |exp(zeta)|<=exp(1040)<2^2080 gives
the strict error <2^(1+2080-2337)=2^-256. The argument at the
center has zero remainder. Hence the estimate holds on the closed
disk, including |z|=520. The largest stipulated node is8191/512<16,
and the smallest is1/512. For every node the G argument has modulus
at most2v^2+v/2<520, while the three other argument moduli are
at most2v<32. These comparisons use the full closed sigma interval
and closed complex w disk; they do not exclude their boundaries.
The half-sum defining cosh averages two errors, so its error is eps,
and multiplication by v bounds the denominator error by16eps.

**Denominator and polynomial claim.** C033b's positive-real inequality
applies at each node with no spectral assumptions. It yields
D>=2v^2/(1+2v)>=2*(1/512)^2/33=1/(33*2^17).
The comparison to2^-23 clears to64>33. Both D and Dtilde are real,
so |Dtilde-D|<=16eps implies
Dtilde>2^-23-2^-252>2^-24. The last strict comparison clears to
2^-24>2^-252. Thus every denominator is positive, including that
at the smallest node. Each is a constant rational, independent of
sigma,w. The two numerator factors are polynomials in those variables
with rational coefficients; division by these constant nonzero
rationals preserves that property, as does the finite rational sum.
No claim about numerical stability follows from this separation.

**Product and quotient propagation.** Positivity of sigma and v gives
0<G<=1. For z=wv, each exponential in the cosh identity has modulus
at most exp(|z|), so |cosh(wv)|<=exp(32)<2^64. Hence
|C|<2^64+1<=2^65 and |Gtilde|<=1+eps<=2. The two-term
product identity in (8) therefore bounds its error by
(2^65+2)eps<=2^66eps. The quotient identity has precisely the
denominator product Dtilde*D in its second term. Using their positive
lower bounds gives coefficients2^(66+24)=2^90 and
2^(65+4+24+23)=2^116. Their sum is at most2^117.
The original weights sum to4096/256=16; the resulting error is
at most2^(4+117-256)=2^-135<2^-6=1/64. Thus no node,
weight, factor of two or quotient contribution is omitted. The
unrounded bound in construction1700's certificate is
2^-136+2^-162, which also lies below2^-135.

**Independent finite replay.** Running the original certificate reports
16/16 exact rational comparisons and no failures. Independently run

    python3 scripts/gamma-midpoint/node-rational-audit-1703.py

This script neither imports construction1700 nor reads its certificate.
It enumerates all4096 distinct rational nodes and verifies their argument
ranges. For each node it independently compares the sharper lower bound
2v^2/(1+2v)-v*eps to2^-24; the minimum in that finite list is at j=0.
For propagation it clears powers of two before comparing integer error
coefficients, retaining2^65+2 in the numerator-error factor. Its resulting
weighted error is2^-136+2^-163+2^-227<=2^-135. All13 checks pass.
The complete rational evidence is in
scripts/gamma-midpoint/node-rational-audit-1703.json. The complete
load-bearing values, checks and empty failure lists of both certificates
were inspected with the shared JSON inspector, not inferred from previews.
Neither script proves the analytic Taylor or modulus estimates above,
nor evaluates sampled parameter values or approximates the rational P.

**Boundary cases and scope.** At w=0, both cosh expressions minus1
are exactly zero since P(0)=1, so the claimed error is zero; denominators
remain positive. The estimates above already include |w|=2 and sigma=1,2.
The integration endpoint v=0 is not a midpoint and needs no new division;
its regularity and unchanged quadrature remain in C033b. The direct
mathematical input remains C033b, so no DAG edge changes. No tail has been
added to (3), and no coefficient-weighted gamma error or full residual
has been certified. Inherited spectral qualifications in the statement,
independent evaluator terms, signed theta upper control and unsmoothed
Xi realization remain unresolved. Full matching Mathlib coverage is
still unknown. This audit supplies no RH or all-degree positivity result.

## Mathlib

Full matching coverage of this exact4096-node, degree2336 uniform
specialization is unchecked and unknown. The precise imported
complex Taylor bound and elementary-function identities are cited
above; no full matching Mathlib theorem or formalization is asserted.
Unknown coverage is not evidence of absence.
