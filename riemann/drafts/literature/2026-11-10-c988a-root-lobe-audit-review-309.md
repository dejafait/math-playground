# Complete exact-root lobe formula — completed audit source gate

TARGET: Audit C988a's complete exact-root lobe formula and aggregate high-zero tail, including test admissibility, both pole terms, the trivial-zero correction, endpoint weights, multiplicities and the uniform constant.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step310 reused review308's exact-root search and reviews249/251/288; searched their precise endpoint, counting and source passages, read C988a and the relevant L985/L988 ranges, and compared recorded stops307/308. Reopened the primary contracts and essential proof cases below. No fresh broad search or novelty inference.
SOURCE_EVIDENCE: Reopened Montgomery-Vaughan, MNT I (2007), Theorem12.13/(12.20)-(12.22), pp410-411, inversion/pole passage p413 and Lemma12.14 with both origin cases pp414-416, https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf ; DLMF18.18.18/18.9.23/18.14.8; Hasanalizade-Shen-Wong arXiv2107.06506v1 definition p1, Cor1.2/(1.5) p2, Section2/(2.3) p3 and complete Cor1.2 proof p15. Reuse reviews249/251/288 for unchanged general-source coverage.
COMPARISON: The known theorems cover the general tools; C988a supplies the finite exact-root specialization, arithmetic normalization and explicit aggregate constant. An audit must independently check this application rather than infer its correctness from its source gate. No source or local result supplies the missing positive-lobe or low-zero signs.
GAP: Essential source coverage for the exact audit is adequate. Independent verification of C988a's test function, absolute convergence before identification, gamma/pole cancellation, exact endpoints, polynomial-degree lobe count and all-n bound remains undone. Low-zero and clipped-lobe limitations remain outside the claimed result.
REASON: Separate source approval is complete for one REPRODUCTION proof audit under SPECIALIZE. Source contracts cover its tools, while the exact application and constants still need checking. This literature turn neither validates C988a nor derives new mathematics.
SCOPE: Only C988a's displayed conclusions, integers n>=2, all actual nontrivial zeros with analytic multiplicities, exact roots of the original K_n, complete intervals wholly inside [n,2n], strict high cutoff H>=e. No RH, simplicity, nonempty-lobe assumption, clipped pieces, aggregate positive budget or infinite-degree exchange.
LITERATURE_REASON: Incoming REVIEW_REQUIRED required separate source approval of the new audit target; reuse the ready ingredient assessments and inspect only its precise contracts, rather than repeat discovery or begin the audit prematurely.


## Completed source comparison — step310, 10 November 2026

The unchanged TARGET is now source-ready. The completed task is
literature_comparison, outcome EXPLORATION, classification
NOVELTY_UNCHECKED: an audit-scope comparison and approval, with no
new estimate, independent validation or claim of originality.
No lemma or mathematical script was written. The mathematical
argument and DAG are unchanged.

### Primary explicit-formula contract

[Montgomery and Vaughan, *Multiplicative Number Theory I: Classical
Theory*, Cambridge, 2007, Section12.2, Theorem12.13, pp410-411](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf#page=14)
requires a measurable test with exponentially weighted L1 norm and
weighted total variation finite for a fixed positive delta_0, midpoint
values at every jump, and the stated O(|x|) symmetric origin condition.
It uses the full complex zero in its transform, symmetric height
summation, primitive characters, two pole terms, prime-power samples
and a gamma integral. Evenness and RH are not hypotheses. The principal
modulus1 specialization is within this contract. The p411 decay
constants depend on the test; the source does not supply the claimed
degree-uniform tail constant. Its p413 inversion and residue passage
retain both poles. These are imported general results, not results
to reprove in the audit.

[Lemma12.14, pp414-416](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf#page=18)
requires fixed positive gamma parameters and an L1 bounded-variation
test with linear origin control. Its proof first treats zero origin
value, using a near-origin split and variation estimates away from
zero; reflection supplies the other sign. The nonzero-origin case
subtracts a Gaussian and then removes that subtraction. Both cases
and their completion were reread. The audit may use this theorem
without a smooth-test replacement. It must check the proposed test
and normalization, rather than infer them from availability of the
source. The PDF is the 2007 book with Cambridge online copyright2010;
no different edition or corrected theorem is being substituted.

### Polynomial and zero-count contracts

Reopened [DLMF18.18.18](https://dlmf.nist.gov/18.18.E18), the finite
Laguerre connection used in L985; [18.9.23](https://dlmf.nist.gov/18.9.E23),
the exact derivative identity attributed to Szego (1975), (5.1.14);
and [18.14.8](https://dlmf.nist.gov/18.14.E8), the global bound for
nonnegative degree, alpha>=0 and real argument x>=0, attributed to
Koornwinder (1977), Remark4.1. The first derivative is used only at
positive degree; constant derivatives need their explicit small-degree
case. Parameter and degree changes, the subtracted constant and
normalizing denominator are audited application details. Review249
records DLMF version1.2.8 (15September2026); live formula text and
attributions were read here, without independently verifying a new
release identifier. No asymptotic differentiation or root-spacing
input is licensed or needed.

[Hasanalizade, Shen and Wong, *Counting zeros of the Riemann zeta
function*, arXiv2107.06506v1, 14July2021](https://arxiv.org/pdf/2107.06506v1),
Corollary1.2/(1.5), p2, is stated for every real T>=e, with error
0.1038 log T+0.2573 log log T+9.3675 around the displayed main term.
The p1 definition uses 0<beta<1 and 0<gamma<=T; Section2/(2.3), p3,
uses the argument principle and the symmetric count, giving the
analytic-multiplicity interpretation. The contour initially avoids
zeros; the corollary's stated scope includes all real cutoffs. The
complete corollary proof on p15 combines Theorem1.1/Table2 above
30610046000 with (1.7)/(2.7) on the bounded range. Those published
numerical inputs are imported; no independent replay is claimed.
This supports the counting contract already audited in L988, without
RH, simplicity or a separation margin. Strict high-cutoff shell
bookkeeping and C988a's aggregate constant remain audit obligations.

### Scope comparison, stops and decision

The original exact-root searches are adequate while the target and
hypotheses are unchanged. This step checked the actual primary
statements and relevant proof cases, not search snippets. No new
search was needed. C988a was read in full for audit scope; only
L985's finite-connection passage and L988's derivative/counting and
prior audit passages were loaded. Review288's different Gaussian
reconstruction target is not imported as a theorem here: only its
inspected general explicit-formula coverage is reused.

Recorded stops307/308 were read narrowly. Their unpaid centered
energy and positive-lobe resource do not refute this representation
or tail question; conversely the named explicit formula and global
absolute bounds do not pay those signed resources. Preserve
stops233/235/243/302/305/306/307 and their evidence. No sharper
absolute-tail target or automatic endpoint-restoration claim is
being opened. No inaccessible essential source or uninspected
optional lead is relied on. Full matching Mathlib coverage remains
unchecked and unknown; no cross-notebook theorem is used.

The bounded next test is exactly the saved audit: independently
validate all C988a conclusions or isolate an error and state the
surviving formula/bound. Passing would make a technical representation
available for a future signed low-zero study; it would not establish
low-zero signs, clipped-lobe bounds, either complement or L984(H).
The independent audit takes precedence over creative scheduling.
There is still no concrete justified signed aggregation mechanism
with a discriminating test; none is invented here. Ready coverage
now defaults to mathematics, with proof_audit/routine_audit,
standard/high routing. The preserved specification below fixes the
remaining obligations and pass/fail test.

## Preserved audit specification and reuse

The exact mathematical inputs are L985's finite connection and audited
L988's derivative and multiplicity-shell bounds. L981/L982 describe
the intended arithmetic endpoint conventions but their quantitative
tail assertions are not inputs. The explicit formula is imported
from Montgomery-Vaughan, not obtained by differentiating a pointwise
psi limit across prime-power jumps. Reuse the ready primary theorem
assessment; no new general source is currently identified as essential.
If the audit moves beyond these hypotheses it needs a revised gate.

Check the scale and orientation u=-2*pi*x in F and Phi, compact
support, continuity and weighted variation at the root endpoints,
midpoint values and behavior near0. Check the modulus1 principal
character specialization. Retain Phi(0), Phi(1), the F(0) term and
the gamma integral before collecting them; then check the sign and
exponent in V. A hypothetical prime-power endpoint must have exactly
the prescribed arithmetic weight, even though its kernel sample
vanishes. Check full prime powers rather than primes alone.

Independently replay the two finite integrations by parts, retaining
both derivative endpoint terms. Verify absolute convergence at fixed
n before identifying or rearranging the symmetric zero sum. Check
bounded-height finiteness, actual analytic multiplicity, the strict
height cutoff even at zero ordinates, n=2, repeated roots and an empty
collection. Check the number of consecutive distinct-root intervals,
the polynomial leading coefficient, the aggregate constants and the
comparison with 100*(n+2)^6 for every n>=2. A finite preview or
asymptotic estimate alone cannot validate the all-n conclusion.

Pass only if all claimed representation and high-tail statements
survive. A failure must identify the exact surviving formula/bound
and leave any unaffected partial result intact. Passing pays no
signed low-zero estimate, positive-part budget, clipped pieces,
both logarithmic complements or L984(H). Preserve stops233/235/243/307;
the audit does not reopen their exhausted automatic-payment claims.

This is a routine hypothesis/calculus/source-normalization audit,
not a creative central proof attempt or a complete-candidate audit.
Subsequent proof_audit/routine_audit standard/high is now suitable
under this completed source approval. A genuinely new signed aggregation mechanism is
still needed before creative escalation; no such target is asserted
merely to satisfy routing cadence. Full matching Mathlib coverage
is unchecked and unknown. No cross-notebook input.
