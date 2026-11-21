# Signed cumulative forcing — completed source comparison

TARGET: Assess a triangular cumulative-forcing route to a one-sided subexponential lower bound for Q_{eta_n}(n), retaining the first two index values, all multiplicities and the complete moving-eta error.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step201 searched Li/Fejer/triangular signed power sums and discrete Taylor/summation-by-parts terminology; reused step192/197 recurrence coverage and read local L040/L044/L046 and parameter/convexity stops. Primary DLMF finite summation and MIT Fejer hypotheses were inspected; no matching unconditional complex-Xi cumulative estimate was found. Failed search implies no novelty.
SOURCE_EVIDENCE: DLMF2.10.9-10 and 2.10.11-18, 1.15.15-17, 18.5.1 and 18.12.7-10, web edition accessed 2026-11-10; MIT18.102 Spring2021 Lecture16, Proposition173 and its real-square proof, Theorem174 and proof, printed pp83-86. Reused Xiao2006.13103v1 Theorem3.2/Corollary3.3 and L968's inspected Lagarias2007 Theorem2.4(2)/(2.21). Michigan Bombieri-Lagarias PDF remains an unread, nonessential lead after broken extraction.
COMPARISON: Finite summation by parts is an identity, not a sign estimate. Inspected oscillatory asymptotics require real nonresonant frequency; Fejer positivity/convergence concern the real circle. L973's complex nodes and weights have no established unconditional real-phase or positive circle-measure representation. No inspected theorem pays the main cumulative forcing bound.
GAP: Independent unconditional signed forcing control remains missing. Isolate a polynomial-budget test for the complete common-terminal-eta error, including both initial values; it would pay regularization only and leave the unregularized signed forcing lower bound unresolved.
REASON: Close direct Fejer/real-frequency import as an unsupported mechanism without banning signed accumulation. Standard finite summation and existing Cauchy/node bounds cover tools for a distinct aggregate eta-error test; no such estimate is derived here. The new continuation assessment requires separate next-turn approval.
LITERATURE_REASON: Startup target was REVIEW_REQUIRED and changed scope from conditional convexity audit to unconditional cumulative signed control; primary summation and Fejer hypotheses had not been compared for it.
SCOPE: Literature-only comparison. SPECIALIZE covers finite-sum tools and the aggregate regularization nomination below, not the desired all-epsilon lower bound, a real spectrum, an independent cancellation theorem or an unsmoothing argument.

The original nomination below records step200's scope. Its pending-source
statements are superseded by step201's completed comparison at the end.

## Proposed mechanism and relevance

The main gap remains L030-L032/C032a positivity and L966's unpaid
R_n<=N_n. The nomination asks whether summing signed index forcing
with triangular weights n-k, retaining the first two index values,
can support a lower bound of the form

    for every epsilon>0 there is C_epsilon>0 such that
    Q_{eta_n}(n)>=-C_epsilon exp(epsilon*n), for all n>=1.

This is a desired threshold, not an established intermediate result.
A sufficient bound would be relevant through L968's audited one-sided
comparison and its precise Lagarias citation. The criterion's strength
must be acknowledged: rewriting it as cumulative forcing does not
prove it. The useful intermediate objective for source comparison is
to identify an independent cancellation estimate with an explicitly
testable remainder, not to name this missing bound as a new lemma.

The intended structural change is to allow negative second differences
and retain their signed cumulative contribution. It abandons the
all-index convexity forcing stopped by L973. No finite Green identity,
complex-phase bound, successful cancellation or initial margin is
derived here. L973's uniform real cosine bounds are RH-conditional
and cannot be used for this unconditional purpose.

## Inputs, failure screen and bounded gate

Essential local inputs are L024/L026 for the actual node law,
L964(5)-(6),(9) for the unconditional analytic normalization, L973(2)
for the common-parameter difference, L966 for the complete theta
representation, L968 for the downstream comparison, and L972 for
the scope of fixed-index parameter loss. Retain all multiplicities
and algebraic squares. In a fixed terminal-n cumulative expression,
use u=eta_n=1/(64*9^n) at every inner index; movement to a different
terminal n is a separate error. Exact first and second values at
that common u must be retained, without assuming a uniform positive
margin for off-diagonal parameters.

Reuse the step192 comparison: L040's signed Newton recurrence and
L044/L046's moment/logarithmic obstructions do not sign an accumulated
remainder. The L967 distant-h allocation and L971 reflected-prefix
stops concern different payment rules, neither of which is reopened.
The parameter-only stop remains: L972's A/9 loss per transition is
not a summable budget. L973's conditional oscillation obstruction
is preserved and is not a ban on methods allowing signed forcing.

In one literature-only turn, compare primary discrete Green/Fejer or
signed power-sum results against this exact family, starting with their
hypotheses and the essential complex-frequency case. Reuse the ready
Li recurrence and criterion coverage. Continue only if a source or a
clearly specified uncovered estimate supplies a bounded, independently
testable cancellation mechanism; list its unpaid initialization,
regularization and unsmoothing requirements. Abandon this candidate
if the available mechanism only assumes real phases/RH, discards
the negative forcing, or renames the full desired lower bound.
Unread leads are not approvals, and failed search is not novelty.

This nomination prioritizes a possible new central mechanism, but
essential source comparison and an independent quantitative test
are missing. It therefore does not yet justify proof_attempt/creative
routing. If the source gate identifies such a mechanism, its later
nomination should name the exact obstruction, bounded test and
decisive evidence before requesting that route. No Mathlib match for
the proposed cumulative estimate has been checked; availability is
unknown. No cross-notebook input is contemplated.

## Completed comparison — step201, 10 November 2026

The principal gap is unchanged. The desired all-epsilon lower bound for
Q_{eta_n}(n) is sufficient for RH by L968's one-sided comparison and its
inspected Lagarias criterion. A triangular rewriting therefore needs an
estimate independent of that desired conclusion. No such estimate, new
identity, lemma or mathematical script was produced in this source turn.

### Inspected statements and essential domains

[NIST DLMF2.10(ii), equations2.10.9-10](https://dlmf.nist.gov/2.10.ii)
states finite summation by parts with U_j=sum_{r=1}^j u_r. Finite complex
entries present no obstruction to the identity. Its example2.10.11-18
instead assumes real alpha,beta and exp(i beta)!=1. The finite geometric
sum2.10.13 retains numerator exp(i j beta)-1 and denominator exp(i beta)-1.
The asymptotic is for a fixed real frequency, not a uniform complex one.
Importing bounded numerator size or discarding the denominator would
change those hypotheses. No Xi Green specialization was derived here.

[DLMF1.15.15-17](https://dlmf.nist.gov/1.15.iii) gives the real-circle
Fejer kernel, normalization and decay away from the real origin.
[MIT18.102, Spring2021, Lecture16](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/eb44436072623f60f8f416875d4b2c11_MIT18_102s21_lec16.pdf),
Proposition173, printed pp83-85, supplies the normalized kernel and proves
positivity by a real sine square. Theorem174, pp85-86, assumes a continuous
2pi-periodic function on the real interval and proves uniform convergence
of Cesaro Fourier means. Its proof uses positivity, unit mass and a real
near/far split. It does not estimate complex spectral nodes or arbitrary
individual coefficients. The notes have typographical slips, including
an infinite integration interval in the initial property list; the proof
uses one period, as does DLMF1.15.16. No infinite-period mass is imported.

[DLMF18.5.1](https://dlmf.nist.gov/18.5.E1) and
[18.12.7-10](https://dlmf.nist.gov/18.12) were read with their variable
domains. Laurent-polynomial identities are usable through L973's existing
complex identity; the displayed real-x generating-series domains do not
justify unit-disk convergence at unknown complex nodes. A generating
function is unnecessary for the proposed bounded component test.

The actual x(beta)=(1-beta/4)/(1+beta/4) and rational weights in L973(2)
are potentially complex. L973(7)'s real-phase description assumes RH.
Thus neither inspected Fejer positivity nor the fixed-real-frequency
estimate supplies the unconditional bound. This is a source applicability
failure, not a proof against all complex signed cancellation mechanisms.

### Reuse, duplicates and decision

Reuse step192/197/199's primary Xiao/Chebyshev comparison. Xiao's identity
retains signed forcing and its second-difference bound assumes RH. L040's
Newton identity, L044's logarithmic-moment countermodel and L046's variance
identity do not give this cumulative estimate. The L972 parameter-only
and L973 convexity attempt records were read. L967's distant-h allocation
and L971's reflected-prefix stops remain distinct. The older
`ATTEMPTS/2026-11-03-triangular-prefix-growth-source-stop.md` concerns a
different observable and is not transferred to this family.

Reject direct real-phase Fejer import as the independent payment. Keep
signed summation as bookkeeping. The prior A/9-per-transition concern
addressed sign induction; the present downstream threshold tolerates
polynomial losses. That changed tolerance motivates a distinct bounded
aggregate-regularization test, without asserting its answer.

The test is specified in `2026-11-10-triangular-eta-error-review-201.md`.
It asks for an explicit polynomial budget for the complete eta-error
block and both initial terms, without assuming a sign for the remaining
Li forcing. Standard finite-sum/Cauchy tools cover this specialization.
Success pays only one error; actual-Xi cumulative forcing stays open.
Abandon if it merely renames the desired lower bound, assumes RH or hides
exponential loss. No creative central mechanism is ready: the inspected
sources provide bookkeeping rather than independent cancellation.

### Search and access record

Queries included `Li coefficients Fejer kernel second differences Chebyshev
complex zeros`, `Fejer sums Li coefficients Riemann hypothesis negative
exponential power sums triangular`, `Li coefficients Fejer summation
complex zeros power sum Turan Bombieri Lagarias`, `discrete Taylor formula
second differences sum n k initial values finite calculus`, and
`summation by parts site.dlmf.nist.gov`. Primary statements, not search
snippets, support the comparison above. No failed search implies novelty.

Gressman/Chamizo author-note pages returned403/502; MIT and DLMF replaced
the essential Fejer coverage. The Michigan author copy of Bombieri-Lagarias,
*Complements to Li's criterion*, JNT77(1999),274-287, has garbled PDF text;
screenshots exposed no readable image and local retrieval failed DNS.
Search excerpts are not counted as an inspected primary theorem. This
is an optional lead, not an essential input or reason to repeat retrieval.
Reused Lagarias coverage suffices for the downstream criterion. Coffey
and other summatory-Li leads were not inspected or imported. Full matching
Mathlib coverage is unchecked/unknown. No cross-notebook input.
