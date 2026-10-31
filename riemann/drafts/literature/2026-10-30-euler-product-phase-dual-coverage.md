# Finite Euler-product phase dual: completed source-scope review

TARGET: Assess whether |C_B(T)|>=c T(log T)^3 for some fixed c>0 along an unbounded sequence, where C_B(T)=integral_T^(2T) R_T(t) Re(B_T(t)/conjugate(B_T(t)))dt and B_T(t)=product_(p prime<=T^(1/1000))(1-p^(-1/2-it)), with the complete R_T of L477.
CHECKED: 2026-10-30
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed bounded searches for finite Euler-product complex moments, phase quotients, unimodular mollifiers, hybrid Euler--Hadamard splitting and twisted moments; inspected the primary statements and truncation cases below, including Heap's stronger result. Reused finite-polynomial and Hardy-space comparisons and the cubic stop. No matching signed correlation theorem was located; no novelty inference.
SOURCE_EVIDENCE: Gonek--Hughes--Keating math/0511182v1 Theorem 2, Section 3 Lemmas 2--3/(15)--(18), pp. 4,8--10; Heap 2102.02092v1 Theorems 1--2, Section 3 Lemmas 2--5/(17)--(20), pp. 3,10--13; Gonek 0704.3448v1 Theorem 3.3/(19)--(24), pp. 9--10; Bettin--Chandee--Radziwill 1411.7764v1 (1.1), Theorem 1, pp. 1--2. Primary URLs and applicability below; ready prime-block assessments reused.
COMPARISON: Inspected product moment/truncation theorems use polylogarithmic prime cutoffs and different observables; the stronger twisted theorem requires an already finite polynomial and smooth height weight. None supplies the fixed T^(1/1000) quotient with a full |R_T|-weighted replacement or the complete signed main term. This is a source-scope mismatch, not a bound on C_B.
GAP: Applicable finite-height phase-product replacement with a proved residual-weighted error and both signed phase contributions remains unavailable in the checked sources. No mathematical impossibility or persistent URL blocker is claimed.
REASON: Park the dependent full-correlation target. Nominate a separate Haar Fourier-support test of one global truncation implementation, independent of the missing actual-height input; its new assessment requires separate approval before calculation.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because growing-product truncation and complete signed finite-height coverage were essential and unassessed. Review this changed multiplier and reuse older adequate assessments without browsing for scheduling balance.
SCOPE: Exactly the displayed real-height statistic, fixed exponent 1/1000, both residual phases, full [T,2T], and all primes up to the cutoff. No RH, independent phases, Haar replacement, conjectural ratios formula, unproved approximation by full zeta, discarded exceptional mass, or implicit short product length.

## Relevance and bounded test

The main gap is actual-Xi all-degree positivity. This intermediate
target would test whether the exact fixed-square residual has a
full-scale L1 defect. The proposed multiplier is the real part of
a finite phase quotient: every factor defining B_T is nonzero
on the real axis, since p^(-1/2)<1. Its absolute value is at most
one. This specification avoids a cubic approximation to a saturation
function; it makes no estimate of the correlation.

A proved lower bound would transfer through L477 to reject the
particular square as a little-o approximation. It would not lower-
bound negative mass, prove a sign violation, resolve higher signs,
or disprove RH. A small correlation would stop this multiplier only.
Both signed components must be treated together: a bound on U_T
alone is not the target, and the complex quotient must not be
confused with a modulus square.

The choice of a growing prime set tests an arithmetic phase response
without assuming that an actual amplitude-weighted law is available.
The small fixed exponent is a specified test parameter, not a proof
that the full product or its reciprocal has short Dirichlet support.
The complete Fourier expansion can have uncontrolled length; that
obligation must be resolved or become the reason for stopping.

The source review should retrieve precise primary hypotheses and
essential proof cases for finite Euler-product phase twists or
applicable truncated prime-block methods. Reuse the already inspected
Heap--Soundararajan and Heap--Radziwill--Soundararajan passages where
their scope genuinely applies. Fixed-prime Haar averages, conjectural
ratios, full-zeta replacements and absolute moment inequalities alone
do not establish this statistic. No additional source lead is being
represented as an inspected theorem.

Pass the review only if it identifies a concrete bounded mathematical
test: evaluate the complete correlation at the stated scale, or prove
an informative obstruction for this specified multiplier/expansion.
Any truncation must retain its full |R_T|-weighted error and both
endpoints. A formal expansion plus an unspecified tail does not pass.
If essential coverage remains missing, park this dependent target;
do not repeat the cubic or sign-boundary searches under this name.

## Duplicate and stop comparison

The unsuccessful five-range dual test is recorded in
`../../ATTEMPTS/2026-10-30-weighted-cubic-five-range-dual.md`.
It constrains the saturation approximation and does not evaluate
this phase quotient. The prior sign-adapted leakage assessment
concerns sgn(U_T) and its uncontrolled sign-boundary terms; this
new multiplier has an explicit prime-product definition and requires
its own quantitative expansion analysis. Neither change alone is
evidence that the new correlation is large.

The statement of L398 was checked narrowly: it uses a squared finite
Mobius mollifier and a fixed response head for another jet mean.
It is not an imported input here. The historical endpoint small-prime
phase attempt was also checked: L337 supplies a positive completion
for partially assigned Liouville phases in an endpoint Laguerre sum.
This proposal makes no assignments to actual prime phases and invokes
no recurrence mechanism. Preserve that stop; no L337 theorem is used
in the proposed residual argument. No completed duplicate was found
by this narrow local check, which is not a novelty assessment.

## Prospective routing, conditional on source approval

Essential mathematical inputs would be L477's complete residual and
transfer error, L481's actual theta and finite-polynomial interface,
and whichever primary phase-product input passes the new comparison.
All distribution, truncation and signed-cancellation assumptions remain
unproved. Mathlib matching is unchecked.

If the review yields a justified new arithmetic mechanism, nominate
proof_attempt / creative / deep_research / max. Its escalation is
precise: a bounded phase twist must capture a nonzero T(log T)^3
correlation with U+Re(exp(2i theta)V), despite the stopped unbounded
resonator, interpolation and amplitude-saturation implementations.
The bounded test is the fixed cutoff and exact C_B above, with a
proved error smaller than a proposed main term, or an informative
upper bound/expansion obstruction. This is prospective routing only;
missing source coverage blocks a creative invocation now. No new
mathematics, readiness approval or originality claim is supplied here.

## Completed comparison, 30 October 2026

The nomination and prospective routing above are preserved. The top
fields supersede their pending-review language. This literature-only
turn produced no new lemma, coefficient formula, correlation estimate
or mathematical script. L477's Hypotheses/Conclusion and L481's
Hypotheses/Conclusion and finite mean-square interface were checked.
The cubic five-range failure remains preserved.

### Primary statements and essential cases inspected

1. **S. M. Gonek, C. P. Hughes and J. P. Keating, _A Hybrid
   Euler-Hadamard Product Formula for the Riemann Zeta Function_,
   arXiv:math/0511182v1, 7 November 2005.**
   [Primary version](https://arxiv.org/pdf/math/0511182v1).
   Theorem 2, p. 4, gives absolute moments of
   P_X(s)=exp(sum_(n<=X) Lambda(n)/(n^s log n)) for real k,
   fixed 1/2<=c<1, epsilon>0, c<=sigma<=1, and
   X=O((log T)^(1/(1-c+epsilon))). Section 3, Lemmas 2--3,
   pp. 8--10, uses P_X^*, with a prime-square correction,
   rather than the sharp product alone. The smooth-number Rankin
   tail before (16) needs that cutoff restriction before the
   short-polynomial mean value (17)--(18). At c=sigma=1/2 this
   polylogarithmic range excludes the proposed fixed power cutoff.
   These real absolute moments do not evaluate the phase quotient
   or signed residual. Neither dropping the correction nor inserting
   complex moment parameters is licensed by the statement.
   No specialization or reproof is made.

2. **W. Heap, _On the Splitting Conjecture in the Hybrid Model for
   the Riemann Zeta Function_, arXiv:2102.02092v1, 3 February 2021.**
   [Primary version](https://arxiv.org/pdf/2102.02092v1).
   Theorem 2, p. 3, extends unconditional second/fourth splitting
   to X<=10^(-4)(log T)^2(log log T)^2. Theorem 1's general-order
   comparison assumes RH; its range is still a fixed power of log T.
   Section 3, pp. 10--13, sets V_0=log_2 T log_3 T and treats
   both real and imaginary prime-sum exceptional sets. Lemma 2
   requires x^m<=T/log T. Lemmas 3--4 give exponential exceptional
   bounds in their stated cutoff ranges. Lemma 5 approximates
   P_X^k on the good set by D(t,k), supported on
   n<=X^(20|k|V_0), with error O(exp(-19|k|V_0)) and real k.
   Both good-set and exceptional-set cases were inspected.
   These hypotheses do not give the requested cutoff, phase quotient
   or residual-weighted exceptional integral. The stronger result
   does not close the source mismatch. A failed v2 URL was resolved
   by retrieving v1; source access is not the reason for parking.

3. **S. M. Gonek, _Finite Euler Products and the Riemann
   Hypothesis_, arXiv:0704.3448v1, 26 April 2007.**
   [Primary version](https://arxiv.org/pdf/0704.3448v1).
   Theorem 3.3, pp. 9--10, assumes RH and, for its multiplicative
   zeta approximation, sigma>=1/2+1/log X and |s-1|>=1/10.
   Its argument formula (21) retains RH and a remainder. The
   proof estimates the zero factor using (22)--(24). This does
   not identify the critical-line sharp product's phase with the
   actual Hardy phase unconditionally. No replacement by full
   zeta is licensed for the present target.

4. **S. Bettin, V. Chandee and M. Radziwill, _The Mean Square of
   the Product of the Riemann Zeta-Function with Dirichlet Polynomials_,
   arXiv:1411.7764v1, 28 November 2014.**
   [Primary version](https://arxiv.org/pdf/1411.7764v1).
   Rechecked (1.1) and Theorem 1, pp. 1--2; reuse the inspected
   collision cases in `2026-10-16-response-modulus-weighted-second-moment.md`.
   The theorem assumes smooth phi supported in [1,2],
   A(s)=sum_(n<=N)a_n n^(-s), a_n<<_epsilon n^epsilon,
   N=T^vartheta, vartheta<17/33. Its error is
   O(T^(3/20+epsilon)N^(33/20)+T^(1/3+epsilon)). It treats
   |zeta A|^2, not R_T times this quotient. It neither constructs
   the required polynomial nor supplies weighted truncation or
   sharp-endpoint transfer. No application to C_B is asserted.

Reuse the ready Heap--Soundararajan Section 5/(14) interface and
Heap--Radziwill--Soundararajan good/bad-block comparison from
`2026-10-29-bounded-short-resonator-dual-correlation.md`, and the
finite-height qualifications in
`2026-10-29-fixed-square-residual-hardy-l1-coverage.md`.
Their unchanged absolute-moment scope was not reopened.

### Search record and decision

Queries included `finite Euler product complex moments imaginary powers
critical line truncated Euler product unconditional`, `Euler product
phase mollifier zeta`, `Gonek Hughes Keating hybrid Euler Hadamard
product theorem Euler moments`, `Heap On the splitting conjecture X
log T`, and `Euler product unimodular zeta`. Search snippets,
secondary discussions and random models are not theorem evidence.
No exhaustive-search or originality claim follows.

SOURCE_BLOCKED records missing essential source scope, not an
inaccessible webpage or a proved failure of the multiplier. The exact
full-correlation target is parked. Reopening requires an applicable
finite-height replacement or a new mechanism removing that obligation;
more absolute moments alone do not suffice. No upper or lower bound
for C_B, E(T), negative mass or Xi signs has been obtained.

The independent nomination in
`2026-10-30-euler-phase-haar-support-obstruction.md` tests the exact
real multiplier's Fourier support under normalized Haar measure.
It can test one global truncation implementation without the missing
actual-height input. A complex-only calculation must not replace the
real-part target. No Haar bound transfers to [T,2T] or |R_T| without
another theorem. The new source-ready nomination needs separate
next-turn approval; no calculation has been performed. This is an
ordinary finite-factor calculation, not a justified creative attack
on the central RH gap. Mathlib matching remains unchecked.
