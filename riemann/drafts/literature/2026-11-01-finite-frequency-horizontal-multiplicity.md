# Finite-frequency horizontal-multiplicity interface — source review

TARGET: Assess whether finite logarithmic-frequency averaging of the full complex BGST form factor can control equal-ordinate multiplicity without thin-box or zero-spacing assumptions.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched horizontal multiplicity with finite-frequency averaging, unconditional frequency, squared kernel, Lamzouri, energy and equal real parts; checked the local charged-pair scope review and L613 stop. Newly followed arXiv:2503.15449v4 beyond unread-lead status; no inspected theorem supplies unconditional count extraction under the nominated hypotheses.
SOURCE_EVIDENCE: Read BGST arXiv:2501.14545v3 Theorem 3, Sections 2.3–2.4, MT/(3.1)–(3.5), Lemmas 3–5/(5.6)–(6.1); GLSS arXiv:2503.15449v4 Sections 4–8 and complete Proposition 1 proof in Section 9; rechecked Lamzouri arXiv:2609.02882v1 Proposition 2.1/(2.4), proof through (2.21), and reused the existing fixed-test application assessment.
COMPARISON: BGST extraction needs thin-box positivity and complex-weight removal; GLSS's unconditional ordinate average retains an unknown nonzero-gap integral, whereas its sharp count result assumes PCC. Lamzouri controls the simple-real deficit by a full algebraic squared-kernel energy, not the equal-ordinate second moment. These are inspected hypothesis mismatches, not a universal impossibility theorem.
GAP: No C<2 upper bound for equal-ordinate multiplicity is supplied without additional aggregate domination, strip/tail control, or ordinate-pair information. All-height Xi signs and displacement-to-charge conversion remain independent gaps.
REASON: Park direct extraction by citing these sources alone; their precise missing hypotheses identify an independently testable aggregate-energy strengthening. No new result, count bound or universal obstruction is proved in this literature turn; the next finite target has separate explicit coverage.
SCOPE: Source comparison only for actual-zeta cumulative or dyadic conventions used consistently; no thin box, RH, simple zeros, minimal ordinate spacing, arbitrary frequency extension or theorem application to artificial models.

## Motivation and bounded assessment

Main gap: actual-Xi all-degree signs at unbounded heights. A stronger
bound on the number of off-line zeros could help control the microscopic
charged centers left open by the count-only route. The inspected BGST
horizontal-multiplicity result relates an equal-ordinate moment to
simple-critical counts. It does not by itself estimate that moment.
Even an improved count leaves displacement-to-union conversion, exceptional
centers and initial coefficient signs unresolved.

The intended independent test concerns the full form factor rather than
the difference between two artificial families. Put y=log x. The available
estimate has a finite y range. A proposed averaging argument must retain
exp((beta-beta')y) as well as exp(i(gamma-gamma')y); it cannot silently
replace the complex statistic by its ordinate-only version. Near-equal
but unequal ordinates must not be identified with the exact equal-ordinate
count. Any use of y beyond the proved range needs an additional source.
No inequality, limit interchange or count conclusion is derived here.

Continuation/abandonment test for the source review: identify an inspected
finite-frequency inequality with explicit hypotheses and error sufficient
to isolate a nontrivial equal-ordinate count bound, or identify the precise
extra spacing, strip, frequency-range or arithmetic input it would need.
An unquantified infinite-frequency projection does not pass. If no such
interface is supported, park that inference and retain its obstruction;
do not repeat the triangular calculation or the blocked stability-source
retrieval. A later mathematical target must be separately specified and
gated; this nomination supplies no ready creative proof attempt.

## Existing evidence and recovery comparison

Inputs for the next review are the source scope in
`2026-11-01-charged-block-pair-statistic-scope.md`, BGST v3 Theorem 3,
Sections 2.3–2.4 and Section 3 MT, and the canonical finite results L612
(corrected counts only) and L613 (audited fixed-contrast stop). No
cross-notebook input is involved. Precise primary version:
https://arxiv.org/html/2501.14545v3 . Actual-zeta realization is not
inferred from either finite result.

Three candidates were compared at route selection: reducing the error
for the same fixed contrast has no newly supplied stronger source;
enlarging Fourier support exceeds the available theorem; extracting
horizontal multiplicity uses a different count observable and has an
independently testable finite-frequency interface. The third is selected
only for assessment. Coverage of its exact inequality remains incomplete,
so REVIEW_REQUIRED is intentional. Full/supporting Mathlib coverage is
not checked. No additional literature discovery, new lemma or mathematical
script on this target was performed during the L613 audit.


## Completed primary comparison, 2026-11-01

The preceding motivation records the nomination made during the L613
audit. This section records the present source review. No canonical
lemma or mathematical script was changed, and no mathematical attempt
on the new energy inequality was performed.

### BGST: the exact sign and weight gates

Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh,
*Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions
of Simple Zeros and Critical Zeros*,
[arXiv:2501.14545v3](https://arxiv.org/html/2501.14545v3),
version header 1 September 2026 (displayed manuscript date 8 June 2026).
Theorem 3/(1.5), with multiset pairs in (T,2T], requires
N^circledast(T)<=(C+o(1))T log(T)/(2pi); part (i) gives the
simple-critical proportion 2-C. Thus C<2 is a useful count threshold.
The H=1,2,3 cases and the full proof in Section 2.4 were read.

MT/(3.1)–(3.5) controls the FULL sum of
x^(rho-rho')4/(4-(rho-rho')^2) for 1<=x<=T, with additive
O(T sqrt(log T)); it does not discard beta-beta'. In y=log x this
is the finite range 0<=y<=log T. Lemma 3/(5.6) gives a positive
real part only for |beta-beta'|<b/log T. Lemma 4 removes W with
O(T) cost under the all-zero thin-box hypothesis. Lemma 5 then
discards unequal ordinates and bounds the remaining kernel on the
imaginary axis from below. These proof cases were inspected.

Application verdict: neither the thin box nor a signed-complement
bound has been supplied. Global nonnegativity of the complete form
factor is insufficient justification for that deletion. No weight-free
or ordinate-only estimate is substituted for MT. Cumulative (3.5) and
dyadic (3.2) are kept distinct; no subtraction ignoring cross pairs is
used. This identifies the failure of this particular import, not a
counterexample to another aggregate method.

### GLSS: unconditional averaging retains the close-pair term

Goldston–Lee–Schettler–Suriajaya,
*Pair Correlation Conjecture for the zeros of the Riemann zeta-function I:
simple and critical zeros*,
[arXiv:2503.15449v4](https://arxiv.org/html/2503.15449v4),
version header 30 March 2026 (displayed manuscript date 24 August 2026).
Use its cumulative convention 0<gamma<=T and L=log(T)/(2pi),
not L=log T. The multiset includes all horizontal multiplicities.
Proposition 1/(5.3)–(5.5) splits the triangular ordinate sum into
U N^circledast(T)+2 int_0^U N(T,u)du. Its Section 9 proof retains
endpoint and cross-boundary contributions with O(L^2) error.
Proposition 2/(5.6) quotes Fujii's unconditional second moment for
0<U<=1. Section 6/(6.2), for 0<lambda<=sqrt(L), states

    N^circledast(T) + (2/lambda) int_0^lambda Ncal(alpha)dalpha
      = TL [lambda + log(2+lambda)/(pi^2 lambda)
            + O(sqrt(log(2+lambda))/lambda)].

Here Ncal(alpha) counts 0<(gamma'-gamma)L<=alpha. Theorems 1–2
assume PCC and HMH respectively; Section 8/(8.1)–(8.2) uses PCC
to determine this integral, including its small-gap part. That proof
and Proposition 1's complete proof were read. Fujii's original proof
was not independently audited.

Application verdict: the unconditional formula supplies a different
interface but not an inspected C<2 count bound. At fixed lambda its
unspecified error cannot certify that threshold; its stated large-lambda
asymptotic retains the unknown integral. The PCC step cannot be imported
from BGST's full-complex finite-range theorem. No effective moving-range
PCC error or spacing hypothesis is supplied here. This newly inspected
lead therefore changes the route without establishing a mathematical
nonimplication theorem.

### Aggregate alternative and its exact remaining difference

Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the
Riemann zeta function are simple and on the critical line*,
[arXiv:2609.02882v1](https://arxiv.org/html/2609.02882v1),
Proposition 2.1/(2.4): for a nonempty finite conjugation-invariant
multiset Z and real-even eta in L2 with compact support inside
(-lambda,lambda), int eta^2=1, put K=Fourier(eta^2). It proves
E_K(Z)>=2|Z|-s_real(Z), where E_K=sum_(z,s in Z) K(z-s)^2
and s_real counts simple real elements. Its proof through (2.21)
handles repeated real elements and nonreal conjugate pairs, including
empty subspace ranges. In particular (2.10) is a norm identity for
the complete energy. The square is algebraic. No equal-real-part
second-moment bound is stated.

The ready charged-pair scope assessment already checked the fixed-test
weight-removal application in Lemma 3.2; it is reused. No varying test,
support enlargement, stability theorem or improved error is imported.
This review reopens neither the blocked stability retrieval nor L613's
fixed contrast. The old finite diagnostic cannot establish the proposed
energy inequality or refute it: it compares two different configurations
against an error scale rather than energy against a count in one set.

Application verdict: whole-energy control is a materially different
mechanism from dropping signed pair terms. A bound for the horizontal
second moment requires a separate proof or counterexample. Its finite
source comparison is in `2026-11-01-aggregate-horizontal-energy-test.md`.
No proof of that strengthening is claimed here.

## Search record, limits and decision

Queries included `"horizontal multiplicity" zeros "pair correlation"`,
`"2501.14545" finite multiplicity average`,
`"horizontal multiplicity" "unconditional" "frequency"`,
`"horizontal multiplicity" "kernel" "square"`,
`"Lamzouri" "horizontal multiplicity" "energy"`, and
`"conjugation" "multiset" "equal real parts" kernel multiplicity`.
Only the primary arXiv statements above support the comparison;
search snippets, surveys, and external research notebooks were not
used as theorem evidence. No novelty conclusion follows from the search.
The old assessment's unread GLSS lead is now inspected. The inaccessible
stability source stays parked and is not needed for this decision.

The achieved result is a source-level negative: these named interfaces
do not license the nominated direct count inference under its allowed
hypotheses. No new lemma, new bound for zeta, all-test impossibility,
or progress beyond the cited theorems is asserted. Mathlib full and
supporting coverage remains unchecked. The main RH gap, exceptional
centers, charge conversion, initial signs and actual-Xi transfer remain.
