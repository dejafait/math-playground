# First-coefficient-drop adjacent-swap margin — research nomination

TARGET: Test a uniform adjacent-swap descent-margin certificate for first-coefficient-drop parity words, deriving the exact swap comparison and searching lengths at most 24 for a counterexample.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step534's bounded three-mechanism screen and its exact parity-swap/least-representative queries are recorded in 2026-10-28-size-dependent-descent-discovery.md; scoped local searches found no completed comparison of this margin. No inspected theorem supplies it; no novelty claim.
SOURCE_EVIDENCE: Read Rozier–Terracol arXiv:2502.00948v2 Definition1.2, Definition2.2, Lemma2.1 and full two-step/common-suffix proof, Theorem2.2 and both extremes; Rozier INTEGERS19(2019)A8 Lemma1 and affine/inverse proof pp.2–3. Compared Niu arXiv:2605.13886v1 Theorems2,4,7 and reused the October3 modular assessments; their scopes do not establish the proposed comparison.
COMPARISON: Adjacent swaps order the known additive remainder; finite parity coding determines the exact integer class. The unproved extension compares their combined descent margin at the least class member >=2. No known theorem will be reproved, and the CST conjecture is not assumed.
GAP: Determine the sign of M(w')-M(w) under a single admissible 01-to-10 swap; then falsify the proposed nonpositive sign within length24 or report a complete bounded screen. Uniform validity, sorting connectivity, base-family positivity and finite coefficient-drop existence remain unresolved.
REASON: Nominate one new, independently testable arithmetic mechanism at the pointwise descent gap. This newly written assessment needs a separate supervisor approval before any mathematical derivation or script execution.
SCOPE: Exactly TARGET: positive integer shortcut map, full finite parity words, exact rational/integer arithmetic and one directed margin comparison. No infinite-word realization, density-to-pointwise inference, coefficient-drop existence, universal descent claim or post-failure coefficient search.

## Exact conjectural intermediate claim

This section specifies a proposed claim, not a derivation or result.
No word, margin or swap has been calculated this turn.

Use T(n)=n/2 for even n and (3n+1)/2 for odd n. Let
w=(w_0,...,w_{j-1}) be a binary word of length j>=1, with q ones,
and let q_k=sum_{i<k}w_i, including q_0=0. Call w a first-drop word when

\[
3^{q_k}\ge 2^k\quad(0\le k<j),\qquad 3^q<2^j.
\]

For each such word let rho(w) be the smallest integer n>=2 with
parity vector w. The known finite parity bijection guarantees this
representative; exclude n=1 by using the next class member when needed,
not by deleting that entire parity class. Write the sourced affine form

\[
T^j(n)=\frac{3^q n+A(w)}{2^j}
\]

on that class, where A(w)=2^j E(w) is the integer numerator constant.
Define the proposed integer margin

\[
M(w)=(2^j-3^q)\rho(w)-A(w).
\]

The threshold of interest is M(w)>0, the exact descent comparison at
rho(w); M(w)=0 must not be counted as strict descent. The speculative
sorting certificate is the following single-edge inequality:

> If w=u01v and w'=u10v have the same length and are both first-drop
> words, then M(w')<=M(w).

This assertion is unproved, and a violation is plausible because rho
changes by a modular least-representative operation. Neither the
nonpositive sign nor the effect on rho follows from remainder ordering.
Treat both first-drop conditions as explicit guards; do not assume them
from a graph picture or an unproved closure property.

## Downstream use and independent gaps

A uniform inequality could support a reduction from arbitrary
first-drop words to a sorted base family, if that reduction is shown
to stay in the guarded language and the base margins are proved
strictly positive. This would address the gap between coefficient
contraction and actual integer descent. Existence of a finite coefficient
drop for every n>=2 is a separate unproved obligation; finite words do
not settle it. Even proving the proposed order would therefore leave
independent gaps toward Collatz.

This test is not a fixed universal horizon: 24 limits a prospective
falsification search, not an asserted stopping-time bound. It uses
neither paired suffix minima nor forced zero runs, first-return strict
descent or a coalescence clock. L001/L003 and Attempts001–004,009–010,
016,020 delimit those previous routes; no mathematical result from them
is needed to evaluate a word or edge here. No cross-notebook input.

## Bounded continuation/abandonment test

After separate approval, derive only the one-swap comparison needed to
expose the residue/carry term; cite the known finite coding and affine
identities rather than reproving them. Enumerate both guarded endpoints
for lengths 1 through24 in exact arithmetic. Stop at the first edge
with M(w')>M(w). Save the complete word pair, swap index, prefix guards,
rho values, A values, margins and direct integer-iteration verification.
An exact violating edge rejects this unrestricted sorting certificate;
do not silently weaken it or start a new variant in the same turn.

If no violation is found, save complete counts by length and the checked
minimum of M(w)-M(w'), including all representative wrap cases. A finite
pass is EXPLORATION, not proof of the uniform inequality, CST or Collatz.
Recommend further development only with a specific structural explanation
for the exact comparison; otherwise park this mechanism. A resource
interruption must record completed lengths and leave the remainder open.
Scripts, if later authorized, must write full evidence to disk and print
only bounds, failures and artifact paths, as required by the shared goal.

## Sources, qualifications and Mathlib

- [Rozier–Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v2, 2025-02-13](https://arxiv.org/html/2502.00948v2): Definition2.2/Lemma2.1 and Theorem2.2 are the remainder-order input, not the new M comparison. Definition1.2 permits infinite coefficient stopping time. Essential swap proof cases were inspected.
- [Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers and Euclidean Embedding*, INTEGERS19(2019), A8, Lemma1, pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2): finite class and affine formulas, inspected with proof. Specialization is to finite positive representatives >=2; no assertion about a positive realization of an infinite word.

The nomination needs only these finite facts. Newer indexed Jxiv3096
and a related author-hosted parity-vector paper remain uninspected
leads because of 404/timeouts, as recorded in the parent assessment.
They are not assumed or used to claim novelty. Full matching Mathlib
coverage is not checked. Unknown coverage does not mean absence.
