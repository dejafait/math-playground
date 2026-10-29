# L105 triangle exclusion — critical-audit source scope approved

TARGET: Critically audit L105's d35 row0/row1/row24 triangle exclusion over all integers m,u>=1 with m+u<=9250245, including its shifted endpoints, cut2 prefixes, imported denominator and row2 guard contradiction.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step497 reused step495 exact-support discovery and duplicate comparison; searched L105/triangle/cut2 in its saved assessment, history496 and Attempt032. Read the full construction assessment and L105 proof; no completed independent triangle audit was identified in this scoped record. No novelty inference.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section2 definitions, equations(2)–(4), Lemmas1/2 and complete printed induction pp.228–229; DLMF4.5.8/4.5.9/4.5.11 with real nonzero-argument qualifications; MathPrize statement. Read L055 table/root and L104 full independent-audit section; reused step495 log-series and stronger-cycle coverage.
COMPARISON: Known finite-affine and positive-real machinery covers the audit methods, not the triangle verdict. L105 is the construction being audited; C104a has u=0 and a different cut1 comparison. L104 supplies only an audited enclosure for its exact K,N; C103a requires b0=0 and L098 changes H data.
GAP: No essential source gap remains for exactly TARGET. Independent verification of the shift, complete cut2 prefix coefficients, denominator operand matching, uniform cap, exact closure and own-input J28 comparison remains mathematical work.
REASON: Approve exactly TARGET for a separate RESEARCH/REPRODUCTION critical audit using assessed machinery, with no general coding reproof or assumed extension of the cut1 edge bound.

The main gap remains universal descent. The completed construction is
recorded in `lemmas/L105-d35-row0-row1-row24-triangle-exclusion.md`;
this proposal neither rejects it nor supplies a second mathematical
attempt. No new calculation, audit result or source retrieval is asserted.

Essential inputs for the proposed audit are L055's literal table and
finite-affine method, L104's audited enclosure for exactly
K=397573379,N=630138897, and L105's full statement/proof and construction
certificate `scripts/postspell-word-count/d35-row0-row1-row24-certificate.json`.
L104's denominator result may be reused only after exact total matching.
C104a is a scope comparison only, not an input to L105's uniform cap.

Retain r25,d35,H0=5,H24=32670656,B=9250245,kappa=23/11,
b0=m,b1=u,b24=B-m-u,others0,integer m,u>=1,m+u<=B,
a_i=2+18b_i and the original chronological tuple. Keep all25 endpoints,
closure, s_i>=540/11, own-input non-strict J/strict H, closing tail2,
coincident coordinates and repeated periods. No minimum, seed,
integer-realization or primitive-period premise may be introduced.

The proposed discriminating audit must independently verify the shift,
all cut2 prefixes in order2,...,24,0,1, the exact complementary-prefix
identities before rows0/1, uniform bounds from m,u>=1, the positive
fixed denominator, the root's exact closure and its comparison with
row2's own J28 guard. Check the complete finite operands rather than
saved success flags; the uniform proof cannot be inferred from vertices.
Retain the result only if these load-bearing claims survive, or record
and repair a precise defect. The endpoint-only tuple is not asserted
to satisfy the other domains/guards. This may validate one restricted
support input; it supplies no order/support exhaustion, entry,
actual-word transfer, divergence exclusion or universal descent.
Full matching Mathlib coverage remains unchecked.

Before this audit, the next invocation must separately compare the exact
audit scope against reusable primary coverage and set an appropriate
ready decision if justified. No newly uncovered mathematics is approved
here. Preserve Attempt032, both d0 witnesses and all unfinished work.


## Separate source-scope comparison — step497, 2026-10-26

LITERATURE_REASON: The new REVIEW_REQUIRED continuation asks for independent critical verification of the completed triangle construction, outside the previous feasibility-attempt target; this turn separately compares that exact audit scope with reusable coverage.
SCOPE: Exactly TARGET under the full retained hypotheses in the original proposal above; all25 endpoints, original chronological indices, own-input guards, closing tail2, coincident values and repetitions remain included. No minimum, seed, integer realization or primitive-period premise.

This separate review supersedes the pending-source wording in the original
proposal, preserved above as history. It approves methods for a later audit;
it does not perform that audit, validate the construction certificate or
establish a new bound. The main gap is universal eventual descent. The
intermediate target is independent verification of L105, potentially usable
as a restricted positive-row0 support input. Support/order exhaustion,
entry, actual-word transfer and divergence remain independent open gaps.

### Primary theorem coverage and specialization obligations

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica78 (1997),227–239,
DOI10.4064/aa-78-3-227-239,
[section2, equations(2)–(4) and Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
was reopened at its hypotheses and complete printed proof. For a finite
nonempty binary word, the theorem gives the real affine composition with
slope 3^ones/2^length and its fixed point when the denominator is nonzero.
The induction checks length1 and appended0; appended1 is printed as
analogous. Only finite composition/fixed-point machinery is imported.
The shifted blocks and cyclic cut must be matched locally; the theorem
does not establish their guard inequalities or integer realization.
Neither Lemma1's odd-denominator parity conclusion nor a minimal-period
claim is needed. Repeated words may be retained. No general coding
reproof is warranted; direct verification of changed offsets and
coefficients is essential specialization and independent verification.

[NIST DLMF4.5.8](https://dlmf.nist.gov/4.5.E8),
[4.5.9](https://dlmf.nist.gov/4.5.E9) and
[4.5.11](https://dlmf.nist.gov/4.5.E11) were reopened with their common
real x!=0 qualification; the upper rational majorants additionally require
x<1. These cover L105's requested positive-small-Lambda comparisons only
after the audit checks the stated interval and exact operands. The
construction uses weak upper bounds where the source is strict; that
weakening needs no new theorem. The previously recorded DLMF version is
1.2.8; this retrieval does not independently verify the release version.
Reuse step495 and step487's inspected DLMF4.6.4 log-series coverage and
finite positive-tail/error-amplification method rather than reprove it.
L104's independent-audit section states an enclosure for exactly
K=397573379,N=630138897. Its enclosure is reusable only after independent
total matching; neither its fixed-case root cap nor its cut1 prefix
estimates are triangle inputs. Reading that audit is source-scope review,
not a new certification of its saved numerical flags.

Reuse step495's stronger-result comparison with Simons–de Weger,
*Theoretical and computational bounds for m-cycles of the 3n+1-problem*,
Acta Arithmetica117 (2005),51–70, sections1.2,2.1–2.2 and Lemmas4/6/7,
pp.52,56–59. The real relaxation lacks the integer-orbit minimum and
height hypotheses used there. No such hypothesis is introduced and no
fresh retrieval of that paper is claimed. The source is a comparison,
not an input to the audit. Full matching Mathlib coverage remains
unchecked; supporting affine/log facts are not a matching triangle result.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
dated2021-07-07, was rechecked on2026-10-26. It still asks for eventual
arrival at1 from every positive integer under even halving and odd3n+1,
agreeing with the local target. Adjudication contributes no premise.

### Duplicates, failures and bounded continuation

The construction itself is the local triangle result awaiting review,
not an independent confirmation. Step495 already distinguished C104a's
u=0 edge, C103a's b0=0 restriction and L098's different H data. No new
external exact-support search is necessary for this unchanged triangle;
the assessment reuses that discovery without claiming exhaustiveness.
Attempt032's complete WHY IT FAILS was read: its failure of a sufficient
support datum does not establish feasibility or invalidate an exact-root
guard test. Preserve it, both original-H d0 witnesses and all unfinished
work. No cross-notebook input was read. No essential unread source was
identified; no source blocker remains for this audit.

Approve one separate RESEARCH/REPRODUCTION audit on exactly TARGET.
Essential inputs are L055's literal table/affine method, L104's audited
enclosure subject to exact total matching, L105's complete proof and its
construction certificate at the path above. Verify every load-bearing
identity and rational operand independently, with complete cut2 prefix
records and a symbolic argument over all m,u, including the whole edge
m+u=B. Vertex checks or saved pass counts cannot establish uniformity.
The endpoint-only tuple is not asserted to meet its other guards.

Continuation test: retain L105 only if the unchanged shifted equations,
exact closure, imported denominator, complementary prefixes, uniform s2
cap and own-input J28 contradiction survive. Otherwise identify the
precise false identity, bound or missing hypothesis and record/repair it;
no failed sufficient estimate supplies feasibility. No audit verdict is
asserted in this literature-only step. The completed construction remains
preserved and pending critical audit.

Completed LITERATURE/EXPLORATION/NOVELTY_UNCHECKED: source-scope approval
only, with no new mathematical result or progress beyond inspected
sources. Mathematical exploration usage is unchanged at0.
