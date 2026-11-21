# Actual-prime adjacent-lobe signs — finite diagnostic scope

TARGET: Certify the signs of B_(n,j) for n=3,4,5,6 and even 0<=j<=n-3, stopping at the first positive actual-prime pair and retaining full prime-power endpoints and compensation.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step232's completed review231 searched actual von Mangoldt/Laguerre lobe cancellation and degree recurrence terminology, and the specific local Li/Laguerre and Polya-lobe records. No inspected theorem or completed local diagnostic covers this B-sign rule. This bounded search does not establish novelty; inaccessible leads are not evidence.
SOURCE_EVIDENCE: Live NIST DLMF18.5.12 (finite polynomial), 18.2(vi) (simple interior zeros), 18.16.9 (ordered positive Laguerre zeros), and18.9.1/Table18.9.1 inspected on 10 November2026. Canonical L981 defines the actual prime-power compensation; audited L982 confirms its normalization. Reuse review224's full-endpoint Abel coverage and review231's completed theorem comparisons; exact references below.
COMPARISON: Known polynomial formulas and root geometry suffice to formulate and rigorously evaluate these finite sums. No inspected theorem signs them against the centered prime measure. Fourier lobe-pairing criteria require unavailable monotonicity/convexity; they are not imported as an arithmetic sign theorem.
GAP: No value or sign of B has yet been calculated. A positive pair would refute the proposed universal nonpositive-pair rule; six nonpositive pairs would prove only finite signs, leaving uniform n and the complete retained head unpaid.
REASON: Test one actual signed arithmetic proposal before seeking an analytic pairing proof. This is independent of the parked prefix envelope and inaccessible-source routes. It is a bounded calculation, not a creative mechanism or evidence for RH.
SCOPE: Only n=3,4,5,6, even 0<=j<=n-3, ell_n=L_(n-1)^(1), actual Lambda including all prime powers, complete endpoint conventions, and compensation from the exact lower endpoint. No RH, zero data, asymptotic Laguerre approximation, random model, uniform sign, or tail bound is assumed.

## Proposed observable and downstream purpose

The main gap is L030-L032/C032a actual-Xi positivity and L966/L968's
signed Li forcing. L980 records the unpaid growing zero head. L981's
quantitative Cauchy tail and audited L982's fixed-index identity form
an interface, not a one-sided head estimate. The eventual desired
threshold is P_n(X_n)<=C_epsilon*exp(epsilon*n) for every epsilon>0,
uniformly in integers n>=2, X_n=exp(10000*(n+1)^4).

Let r_(n,0)=0 and let r_(n,1)<...<r_(n,n-1) be all positive zeros
of ell_n. The sole proposed pairing observable is

    B_(n,j)=sum_(exp(r_(n,j))<m<=exp(r_(n,j+2)))
                   Lambda(m)*ell_n(log m)/m
                   -integral_(r_(n,j))^(r_(n,j+2)) ell_n(u)du,

with j even and j+2<=n-1. The initial interval starts at0.
The test asks whether the rule B_(n,j)<=0 survives these six pairs:
(3,0),(4,0),(5,0),(5,2),(6,0),(6,2). These are definitions and a
proposed threshold, not an asserted identity or sign result.

A universal upper sign on such pairs could pay part of the oscillatory
head before absolute values. It would still leave any unmatched finite
lobe and the entire final lobe through X_n. No inference about those
pieces or about RH is licensed by the finite diagnostic. Actual prime
arithmetic distinguishes this test from generic envelope countermodels.

## Precise available inputs and qualifications

- [DLMF18.5.12](https://dlmf.nist.gov/18.5.E12) supplies a finite
  polynomial for nonnegative integer degree. Use degree n-1 and
  parameter1, as already justified in canonical L982. Polynomial
  antiderivatives and rational root brackets suffice; no asymptotics.
- [DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi) and
  [18.16.9](https://dlmf.nist.gov/18.16.E9) cover simple positive
  roots. Inspected [Table18.3.1](https://dlmf.nist.gov/18.3.T1):
  weight u^alpha*exp(-u) on (0,infinity), alpha>-1, so alpha=1
  is permitted. These statements do not sign a prime sum.
- L981 uses actual Lambda and full right endpoints. Its finite Abel
  formula, imported from Apostol1976 Thm4.2 with inspected real-endpoint
  proof in review224, may be reused if needed. Direct evaluation
  requires no PNT, infinite limit, or tail conclusion.
- L982 supplies normalization context only. L980/L966/L968 explain
  relevance; their conditional sign premises are not inputs here.

These are live DLMF pages read on 10 November2026, not a pinned old
edition. Reprove no special-function identity or PNT. The uncovered
difference is evaluation of this finite signed statistic; EXPLORE
does not certify originality.

## Discriminating test and certification requirements

Enumerate all actual prime powers p^k, including k>=2, at each upper
endpoint. Isolate the needed polynomial roots and enclose logarithms,
exponentials, finite sums and antiderivatives with rigorous errors.
Floating-point previews cannot certify signs. At a prime-power
logarithm equal to a root, use its exact zero weight and the specified
endpoint convention; otherwise certify the side. If computation is
used, save full reproducible certificates under scripts/li-prime-laguerre/;
print only sign intervals, threshold0, failures and paths. Do not add
a mathematical script during a literature approval turn.

Stop at the first interval strictly above0: that witness refutes the
universal nonpositive-pair rule. Preserve it canonically if obtained;
it is not a counterexample to RH, every pairing, or the full head bound.
If all six intervals are nonpositive, report only those finite signs;
continuation needs a distinct n-uniform signed arithmetic idea and
separate coverage. If an interval contains0, refine within this finite
scope or save an unresolved result; do not guess. No further mechanism
is preapproved.

## Overlap and process limits

See [completed review231](2026-11-10-signed-prime-laguerre-head-discovery-review-231.md).
Earlier Polya Fourier-lobe, prime-prefix variance and Xi-order stops
concern different observables. Review223's retracted cutoff source
and review224's unread Khalsa/kenan leads remain noninputs. No
inaccessible source is essential here; no cross-notebook input is
proposed. Full matching Mathlib coverage is unchecked.

This assessment was first prepared in literature step232. It needs
separate supervisor approval before invocation. No B value, lemma or
script was produced in step232. Route calculation/standard/high;
finite arithmetic certification must not be relabeled creative.
