# Fixed p_5 pole-residue screen — nomination2026

TARGET: Test whether the monic ratio (U_6/l_6)/(120p_5) has at most one positive simple-pole residue at the fixed zeros of p_5, using C029n's existing enclosures and certifying every pole and residue sign.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery2026 compared exactly three source-backed candidates and checked fixed Pollaczek/residue/Nevanlinna duplicates; no actual-family residue-sign theorem was found and no novelty is inferred. drafts/literature/2026-11-20-fixed-pollaczek-residue-discovery-2026.md
SOURCE_EVIDENCE: Kuznetsov CMB51(2008),561–569, (2)/(4)/(13), pp563/566 and weighted passage pp568–569, https://doi.org/10.4153/CMB-2008-055-0 ; de Snoo–Winkler–Wojtylak arXiv1011.2081v1, (1.1)–(1.4), Theorem2.2 statement and full Corollary2.3 proof p5, https://arxiv.org/pdf/1011.2081v1 ; Langer–Luger–Matsaev Acta77(2011), Definition1.1/(1.2)–(1.3), pp426–427, https://acta.hu/download.phtml?id=3148 . Direct primary text checked in approval2027; C029n's audited finite inputs reused.
COMPARISON: Generic zero theory is known; its actual-family residue hypotheses are unpaid. This application checks a fixed-basis coefficient condition and its signs, without computing U_6's inertia, fitting poles, using the stopped affine quotient or reinstating C029n's identity bulk.
GAP: All five residue signs are uncomputed. No uniform family sign law or eventual index bound follows from a finite pass. The finite kernel orientation/application must be justified before using the cited N_0/N_1 facts.
REASON: A bounded known-method specialization can discriminate a materially different sufficient coefficient restriction relevant to C029m. No general theorem reproof or creative uniform-mechanism claim is proposed.
SCOPE: Approved in separate literature step2027 after direct primary-source verification and URL repair; exact target unchanged. N=6 and denominator 120p_5 only, with existing fixed enclosures; no degree campaign, fitted poles or precision escalation.

## Exact object and necessary application

Use C029m's full Jensen-weighted T_6, including every odd coefficient,
and C029n's U_6=T_6/S, S=sin(pi/8)/sqrt(2)>0. Set l_6=[t^6]U_6,
already certified negative in C029n/C029q. Define Q=U_6/l_6 and
P=120p_5 from the exact Pollaczek recurrence. Verify their monic
degrees six and five in the application, rather than inferring them
from names. The denominator is fixed before evaluating Q.

For each real root lambda_j of P define

    r_j=Q(lambda_j)/P'(lambda_j),

the coefficient of (z-lambda_j)^(-1) in Q/P. The source convention
1/(s-z) makes favorable simple-pole residues nonpositive in this
notation. The sought restriction is at most one strictly positive
r_j. This is a proposed screen, not an established actual-family law.

Supply the finite divided-difference kernel applicability check,
including the linear polynomial part and every residue term, before
using the zero theorem. Use its cited definition to bound negative
squares under the proposed sign condition; distinguish N_0 from N_1.
Do not assume numerator simplicity or reprove Theorem2.2. Explain why
real-denominator cancellations cannot hide a nonreal numerator zero.
This routine finite algebra fixes sign/orientation; it was not derived
as a new theorem in the literature turn.

## Fixed bounds and decisive evidence

Reconstruct P exactly over Q. Seek its five roots only on the rational
grid j/16, -256<=j<=256. Keep an exact grid root as a singleton;
otherwise retain sign-changing neighboring intervals, without double
counting root endpoints. Certify five disjoint roots by exact
evaluation and the intermediate value theorem, then use degree five
to certify completeness and simplicity. Stop if five roots cannot be
certified; do not widen the grid. Refine each nonsingleton bracket
by at most 30 exact rational bisections, retaining sign/endpoint
evidence. This isolates only the fixed reference polynomial, not U_6.

Evaluate Q and P' on every complete bracket by exact rational interval
arithmetic and C029n's unchanged 60-decimal pi/sqrt(2) bounds. Every
reciprocal needs a denominator separated from zero. Reuse the audited
coefficient formulas while checking the conversion to Q. No ordinary
floating approximation, installation, runtime search or transcendental
precision escalation is part of this test.

Save all coefficients, source-input hashes, grid values, bracket
refinements, derivative/nonzero checks, full rational residue
enclosures, signs and failures under scripts/pollaczek/. Print only
actual/required counts, failures and certificate paths. Inspect full
load-bearing endpoints, using the JSON inspector for selected values
if needed. A preview is not sign evidence. A zero-containing enclosure
is unresolved, not an exact cancellation or a nonpositive residue.

A pass requires every sign resolved and at most one positive residue.
Two rigorously positive residues reject this baseline condition even
if other signs remain unresolved; retain all five attempted enclosures.
Fewer positives with unresolved signs is inconclusive. Neither result
authorizes N=7, a precision campaign or deleting coefficients.

## Purpose and limitations

The plausible use is eventual uniform control of the fixed-reference
residues, providing a negative-square route to C029m's one-pair premise.
A finite pass does not establish that control. Failure stops this
baseline version, not an eventual-only statement or RH; reopening
requires materially new eventual sign structure, not a new degree.
Actual degree N eventually, or a justified actual-degree reference,
also remains unpaid. Initialization, general degree/singular/
cancellation cases and qualified compact convergence/upstream[9]
are independent open steps. L030–L032/C032a remains unresolved.

Essential inputs: C029m exact family/conditional context; C029n exact
coefficients, normalization and rational bounds; C029o conventions;
C029p audited baseline and C029q stop as contrasts, not sign premises;
review2001 and discovery2026 sources. No cross-notebook input. Full
matching Mathlib coverage unchecked. A future finite application is
REPRODUCTION, not discovery beyond the inspected theory. No residue,
kernel proof, lemma or mathematical script was produced this turn.

## Separate source approval2027 — 20 November 2026

This is the separate literature approval of the step2026 nomination.
The missing direct URLs are now in SOURCE_EVIDENCE itself. The
SPECIALIZE decision and exact target are retained; no residue signs
or finite kernel identity were calculated or established here.

Primary text was reopened at the URLs above. In de Snoo–Winkler–Wojtylak,
version 1 dated 9 November 2010, (1.1) requires real symmetry,
meromorphy off the real axis and exactly one negative square for N_1;
N_0 has no negative squares. The introduction identifies upper-half-plane
zeros as generalized zeros of nonpositive type and states uniqueness.
Theorem 2.2, manuscript p5, states the factorization into an N_0 function
and one of three rational factors, distinguishing finite and infinite
GZNT/GPNT cases; it refers to [3–5] for the theorem rather than giving
its proof. The complete displayed Corollary 2.3 proof on p5 uses this
factorization at an upper-half-plane zero to prove a nonzero derivative.
Thus no numerator simplicity is an input. Import the stated theorem;
no independent verification of [3–5] is claimed. The earlier phrase
“with complete proof” applies to the corollary, not Theorem 2.2.

Langer–Luger–Matsaev, printed pp426–427, Definition 1.1, explicitly
requires an upper bound for every finite kernel matrix and attainment
for at least one matrix. Equation (1.2) records the rational-factor
characterization, with reduced rational degree and normalization
qualifications; (1.3) preserves the index under -1/f. These are general
inputs, not an actual-family sign law. No convergence theorem from
this paper is needed or approved for varying reference denominators.
The finite application must still check the linear part, all residues,
and whether its kernel is in N_0 or N_1 before invoking zero theory.

Kuznetsov's publisher PDF linked in discovery2026 was reopened:
recurrence (2), printed p563, agrees with C029n; finite formula (13),
p566, and its generating-function explanation are the coefficient
source. The Jensen multiplier and exact weighted family appear on
p568, with the weighted compact-convergence assertion there and only
numerical root observations continuing on p569. This does not supply
residue signs. Reuse the existing source extraction and C029n finite
normalization; do not reprove general zero theory or weighted convergence.
The qualified weighted-limit/upstream[9] issue remains independent.

Duplicate/failure comparison is reused from discovery2026, whose exact
target has not changed: C029n's identity-bulk stop and C029q's affine
quotient stop do not evaluate fixed-reference residues. Local reads of
C029m hypotheses/analytic input, C029n normalization and C029q hypothesis/
conclusion confirmed these scope distinctions. No new discovery search
or novelty claim is needed for this repair. Mathlib matching coverage
remains unchecked. Web PDF text was usable; screenshot calls yielded
only reference labels, and a shell download failed DNS resolution.
Neither failure blocks the inspected theorem text; no visual verification
or local downloaded copy is claimed.

Proceed only with the saved bounded finite screen. All five poles and
signs are required for a pass; two positive residues reject this baseline,
and unresolved signs are inconclusive. No new uniform assertion, next
degree campaign, or RH candidate is approved by this source review.
