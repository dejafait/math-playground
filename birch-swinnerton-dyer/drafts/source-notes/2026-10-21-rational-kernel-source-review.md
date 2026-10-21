# Rational finite kernels: source coverage, step 398

2026-10-21. Literature only. The outcome is source readiness for a
bounded proof attempt, not a proved integration plan or an evaluated
kernel. No lemma or mathematical program was written.

## Relevance and reused evidence

The main gap is rank E(Q)=ord_(s=1)L(E,s) for arbitrary curves of
analytic order at least two. The intermediate target is a rational
finite-integration certificate for L101's 128 kernels on [1,128], at
unchanged M=Y=128, each with radius at most 2^-50. Its downstream use
would be independent fixed-case complex upper-bound evidence alongside
audited L099. L035 already imports this curve's analytic order: success
would change provenance, not establish a new BSD case.

Reuse the analytic assessment and duplicate search in
`2026-10-21-complex-derivative-sources.md`, audited L101's identity,
tails and finite-error contract, and L031's elementary interval rules.
Read L101's hypotheses/conclusion, imported-source applicability and
finite integration/error sections, and L031's elementary-function
enclosure section. No further analytic-tail research is needed.
ATTEMPTS/043 concerns a different general comparison; ATTEMPTS/045
records the order-table adaptation failure; ATTEMPTS/046 parks the
unavailable FLINT implementation. None establishes an obstruction to
rational Taylor integration. The two derivative assessments and
history/392 contain no already completed rational-kernel plan.

## Inspected primary inputs

NIST DLMF online version 1.2.8, released 2026-09-15, inspected
2026-10-21. Equation numbers below identify the actual statements;
the referenced books were not separately read.

* [1.4.35--37](https://dlmf.nist.gov/1.4.vi): for f in C^(d+1)[a,b],
  the degree-d Taylor polynomial about a has Lagrange remainder
  f^(d+1)(xi)(x-a)^(d+1)/(d+1)!, a<xi<x, and the stated integral
  remainder. Read both remainder cases and the smoothness hypothesis.
  These are finite remainders, not just convergence assertions.
* [1.4.26](https://dlmf.nist.gov/1.4.E26) gives the fundamental theorem
  for a continuous integrand with a primitive;
  [1.4.28](https://dlmf.nist.gov/1.4.E28) gives change of variable for a
  continuous or piecewise continuous derivative; and
  [1.4.29](https://dlmf.nist.gov/1.4.E29) gives the first integral mean
  value theorem for continuous f and nonnegative integrable weight.
  These supply polynomial integration and integration of a uniform
  continuous-error enclosure. They do not supply a numerical tolerance.
* [4.2.19](https://dlmf.nist.gov/4.2.E19) gives the exponential series;
  the following text states entirety.
  [4.7.7--8](https://dlmf.nist.gov/4.7.ii) give its derivative identities.
  L031's existing small-positive-argument alternating enclosure is an
  available elementary constant-evaluation input; its hypothesis must
  be checked after any argument reduction.
* [4.6.1](https://dlmf.nist.gov/4.6.E1) gives log(1+z)'s alternating
  series for |z|<=1, z!=-1.
  [4.6.4](https://dlmf.nist.gov/4.6.E4) gives
  log z=2 sum_(j>=0) ((z-1)/(z+1))^(2j+1)/(2j+1), Re z>=0, z!=0.
  These identities alone are not certified truncation errors.
* [4.7.3](https://dlmf.nist.gov/4.7.E3) gives
  (d/dz)^k log z=(-1)^(k-1)(k-1)! z^(-k) for positive integer k.
  [4.7.10](https://dlmf.nist.gov/4.7.E10) supplies power derivatives.
  They support Taylor remainder applications to log and reciprocal
  on positive closed intervals.
* [4.8.2](https://dlmf.nist.gov/4.8.E2) gives principal-log additivity
  with its phase-sum condition. Positive real arguments meet it.
  [1.2.11](https://dlmf.nist.gov/1.2.E11) gives the finite geometric
  sum for ratio !=1. These cover the algebraic ingredients for positive
  logarithm argument reduction and explicit geometric tail comparisons.

The applicability check is limited but complete at theorem level:
every panel stays in [1,128], exp is entire, log and reciprocal are
smooth on the positive axis, and y=1 is a regular endpoint with log 1=0.
No principal-log branch is crossed. All later panel changes of variable
must retain positive endpoints. Rational coefficients and endpoint
arithmetic can use L031's exact four-product/min-max and directed
floor/ceiling rules. Rounding errors must remain in the certificate.
No floating-point transcendental evaluation is imported.

## Comparison and source-access qualifications

The previously assessed Johansson/FLINT integration theorem is stronger
ready-made validated numerical machinery, but its concrete backend
remains unavailable. Elementary finite Taylor remainders provide a
different way to establish containment without that binary. They do
not assert the proposed degree, panel count or arithmetic precision is
sufficient. That fixed error comparison is the remaining specialization.

Queries included "validated integration Taylor polynomial remainder
rational arithmetic logarithm exponential Taylor models rigorous
quadrature", targeted DLMF Taylor-remainder searches, and the exact
title "Computation and Application of Taylor Polynomials with Interval
Remainder Bounds" with integration/arithmetic terms. Berz--Hoffstatter,
Reliable Computing 4 (1998), 83--97, DOI 10.1023/A:1009958918582, was
a stronger-method lead. The author-hosted Cornell PDF's ordinary text
extract was corrupt; screenshot retrieval supplied no readable pages,
and a local download failed at DNS. A search extract displayed a Taylor
remainder passage, but is not a substitute for inspecting the paper's
integration/arithmetic cases. Those cases are **unread and not imported**.
The BM dynamics alternate URL was inaccessible. ODE Taylor-model papers
and the AutoBound search result are also unread leads, not dependencies.
These optional access failures do not block the independently inspected
DLMF inputs. No absence or novelty claim follows from the search.

## Proposed bounded continuation, not an estimate

One proof-only test is proposed: the fixed partition with endpoints
1+j/8, j=0,...,1016; panel polynomial degree at most 256; scalar series
at most 256 terms; at most sixteen exponential squarings; and outward
dyadic arithmetic on the 2^-256 grid. These are proposed caps, not
achieved error or runtime bounds. No parameter value or panel sum was
evaluated, and no choice is asserted sufficient.

The later proof must specify factor polynomials and scalar argument
reduction, derive every remainder from the cited results, propagate
constant, product/truncation and rounding errors, integrate the full
panel errors, and compare the total with 2^-50 for every n=1,...,128
and rational c_* in [3/10,1/2]. Retain all polynomial cross terms or
bound every discarded term. It must also describe independent replay
and a finite arithmetic-operation bound before implementation. A
symbolic error-budget attempt uses no numerical integration backend.

Continue only if that entire stated plan obtains the threshold within
its caps. Otherwise preserve the failed inequality/cost and park this
plan, without increasing degree, panels or precision in that attempt.
This is a known-method specialization, with no reproof of Taylor's
theorem or claim of new numerical analysis. Implementation and actual
kernel evaluation require their own later covered target and resource
limits; this review grants neither. A later derivative test still needs
actual c endpoints, all exact coefficients and signed rational summation,
using L101's B=2^-43+200*delta+4*sum(|a_n|/n)e_n when eta=0.
Zero containment remains inconclusive. Mathlib coverage was not checked.
