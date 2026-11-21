# Formally collected Diamond–Steinig coefficient-rate test

TARGET: Test whether the formally collected Diamond-Steinig coefficient mass C_n defined in review297 has zero exponential limsup rate at nu=n, retaining both ordered partition families and all factorial weights.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step297's completed review296 searched exact collected-coefficient/norm/cancellation terminology and compared review295, L998, stop296 and the fixed-order/centered-Vaughan limits; no inspected theorem decides this exact rate. No novelty inference.
SOURCE_EVIDENCE: https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf — Ramaré, On Bombieri's asymptotic sieve, author preprint28 October2009, Section2/(12)-(18)/Lemma4 pp8-9 and Lemmas5-7 with proofs pp10-11; Lemma18 p15 and Section5.1/(23)-(25) pp20-21 show continued use of unmerged estimates. Tao2014 Notes1 https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/ Proposition60 and Exercise64 do not supply this norm theorem (reused review296). Read details and links are in completed review296.
COMPARISON: The finite signed summands are known. Only their full-vector formal collection and the resulting rate are to be tested. Formula(18) itself states no canonical collected norm or subexponential theorem; L998's unmerged lower rate does not decide this target.
GAP: Determine zero versus strictly positive limsup of log(max(1,C_n))/n. No favorable collection, exact asymptotic, signed arithmetic saving or interface to L984(H) is established.
REASON: This quantitatively specializes an inspected finite identity using a different order of collection and absolute values. A decisive coefficient test precedes any new arithmetic budgets; no general identity or sieve theorem needs reproving.
SCOPE: Integers n>=1, exactly the formal coefficient collection defined below at nu=n. Finite rational arithmetic and elementary coefficient/factorial bounds only; no optimized representation, zeta estimate, arithmetic correlation or RH assumption. Newly written ready continuation; separate next-turn approval is required before research.

## Exact proposed observable

Use K_n,H_n,c,w with their complete hypotheses and weights as in
L998, imported from Ramaré(12)-(16). In particular K_n has weighted
sum 2n and positive length at most n. H_n consists of ORDERED pairs
of positive-length vectors, EACH of weighted sum n, with total
length at most n. Extend their coordinates by zero through 2n.

Here is a definition of the proposed observable, not a new theorem.
In commuting FORMAL variables Y_1,...,Y_(2n), form the finite polynomial

    T_n(Y) = 2n sum_(k in K_n) c(k)w(k) Y^k
       + n^2 sum_((k',k'') in H_n)
               c(k')c(k'')w(k')w(k'') Y^(k'+k''),
    Y^k = product_(j=1)^(2n) Y_j^(k_j).

Define b_n(ell)=[Y^ell]T_n and

    C_n = sum_(ell occurring in T_n) |b_n(ell)|.

Sum ALL contributions to the same exponent vector before taking
absolute values, including contributions from both families. Ordered
pairs remain ordered in the second sum; do not divide by two or
discard coincident pairs. Keep 2n, n^2, all component factorials,
and all j! weights. Empty H_1 is included. Zero coefficients add zero.
No use is made of evaluation at any Y_j or of a functional relation
among actual log convolution factors. The mu multiplicity attached
to ell is its length; retain that information when interpreting the
definition. Do not merge by total log degree alone, introduce
zero-degree factors, cancel mu*1, or optimize over identities.
Establish the elementary bookkeeping needed for any claimed
arithmetic interpretation during the research test, not by invoking
an unproved uniqueness assertion about Ramaré's shorthand a(ell).

## Bounded decision and downstream limits

Decide whether limsup_(n->infinity) log(max(1,C_n))/n=0.
A rigorous positive lower rate along an explicit unbounded sequence
is enough to reject it; an exact asymptotic is unnecessary. Otherwise
prove C_n<=K_epsilon*exp(epsilon*n) for every epsilon>0 and all n>=1,
with finite K_epsilon. Do not infer the answer from finite samples.
Import Ramaré's unmerged upper bound when useful; any bound on this
new observable requires its own explicit applicability argument.
L998's lower bound cannot be reused without checking the FULL signed
coefficient. No claimed rate is preapproved by this assessment.

A positive rate parks automatic subexponential overhead for this
particular collected representation. A zero rate warrants only a
separately reviewed arithmetic-error interface toward L984(H).
An inconclusive result saves partial reasoning and requires a
materially refined test before repetition. Do not substitute an
arbitrary different representation or derive an arithmetic interface
within this one test. Preserve L998 and all prior route stops.

Essential inputs are Ramaré's explicit finite coefficients and L998's
definitions/obstruction. L984(H), L981/L982's cutoff and compensation,
and L993's conditioning are downstream context, not paid assumptions.
Actual factor norms, signed correlation, Laguerre reconstruction,
full prime powers, endpoints, compensator, both complements and
regulator/infinite-zero control remain open. No cross-notebook or
RH input. Mathlib matching coverage is unchecked and unknown.

Expected research classification: REPRODUCTION under SPECIALIZE,
calculation, standard/high. Any local coefficient bound is a
quantitative specialization, not a claimed new prime estimate.

## Source-link recovery — step298, 10 November 2026

The ready assessment now contains direct source URLs in SOURCE_EVIDENCE.
Reopened the [primary author PDF](https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf#page=8),
confirmed its 28 October 2009 date, and read Section2, (12)-(18),
Lemma4, printed pp8-9, and Lemmas5-7 with proofs, pp10-11.
The two weighted-sum conditions in (15), the total-length restriction,
and the separate factorial products in (14)/(16) match the saved
observable. The two slots of H are retained; no symmetry quotient
is supplied. Equation(18) is expressly shorthand. Lemma7 bounds
the two absolute sums separately. No source theorem deciding C_n's
rate was located in these passages.

Reuse review296's discovery, Tao comparison and recorded-failure
screen; they are unchanged. No new theorem, rate calculation,
arithmetic interpretation or novelty claim is made. This repairs
citation traceability only. The exact TARGET, SPECIALIZE decision,
formal definition and bounded test remain unchanged. Mathlib matching
coverage remains unchecked. No essential source is blocked.
