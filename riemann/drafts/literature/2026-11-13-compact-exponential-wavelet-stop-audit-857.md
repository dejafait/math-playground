# C998 rejecting-pair audit — source approval858

TARGET: Critically audit C998's compact exponential-wavelet rejecting pair, including source normalization, exact moments, H2 extension, analytic Gauss disks and complete-Q tail enclosures.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate review858 reuses855/856's unchanged exact wavelet/Weil and local failure comparison and ready804's verification assessment; new narrow searches/readings locate the Cauchy/Gauss remainder and actual Decimal-operation guarantees. Queries, inspected statements and nonessential access failures are below.
SOURCE_EVIDENCE: Reuse Khalidov-Unser2006 III-V/(3)-(9)/Proposition2/Property2, Unser-Blu2005 PartI Theorem1/Proposition2, L744(6)/(8) and supported mollification. Newly read NIST DLMF3.5(v)/(18)-(21), Purdue MA425/525 Lecture7 Theorem9 and its derivative-formula proof, DLMF5.2(i)/5.5.2/5.11(ii), Python3.15.2 Decimal/Context methods and IBM Decimal Arithmetic1.70 square-root rules; details below.
COMPARISON: The construction, quadrature remainder and enclosure operations are known machinery. None imports C998's physical specialization, disk constants, actual intervals or rejecting ratio; these remain a conceptual audit of a local reproduction, with no full-metric or RH consequence.
GAP: Essential source coverage is ready; verify the exact source-to-physical map, both pole moments, H2 passage, real Gauss applicability and panel rescaling, every complex disk/Mstar, all31 delays, outward arithmetic, artifact identity and complete infinite tails. No audit pass or replay is asserted in858.
REASON: This separate literature-only approval completes nomination857 without deriving new mathematics or changing the fixed test; one RESEARCH/REPRODUCTION conceptual audit is now covered. Retain857's completed negative pending that audit.
SCOPE: Only the exact C998 proof, rational pair and existing857 artifacts at the two fixed scales; necessary verification/repair of its proof is covered, but no changed roots, origin, threshold, generator, coefficient search, retuning or alternate Q.
LITERATURE_REASON: Nomination857 was REVIEW_REQUIRED for this newly written proof's essential analytic/error hypotheses;855/856 did not give precise Cauchy/Gauss citations or implementation-specific Decimal coverage. This separate gate supplies them and reuses all unchanged coverage.
COVERED_TARGET: Assess source and hypothesis coverage for a critical audit of C998's compact exponential-wavelet rejecting pair, including source normalization, exact moments, H2 extension, analytic Gauss disks and complete-Q tail enclosures.

## Original nomination857; pending statements below are historical

The following nomination was supplied before review858. Its final
pending sentence records that earlier stage; the separate approval
below and current fields supersede its gate, without accepting its proof.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. A sound negative can prevent further use of this particular
interscale half budget; it neither disproves positivity nor closes that
gap. A useful review must test the actual source filter rather than a
similar compact wavelet, both exact pole moments, zero-extension and
form passage, source-to-physical units, support/lattice selection,
signed arithmetic normalization, node/weight enclosure, complex-disk
holomorphy and Mstar, and the full infinite-frequency tails.

Essential local mathematical inputs are L744 and C998. L741 supplies
definitions and scope only, not a sign at this length. Essential artifacts
are scripts/exponential-wavelet/two-scale-certificate-857.py and its JSON,
plus witness-857.json. Diagnostic full blocks are selection evidence,
not a sign premise. The final certificate uses only the already covered
first-order DLMF remainder, not a higher Bernoulli expansion.

Continue if the exact pair has two positive Q values and rigorously
4H^2-Q(u)Q(v)>0 after all errors. Reject or repair the local claim if
normalization, moments, analytic disks or enclosure arithmetic fail;
an unverified numerical near-unit ratio does not replace that evidence.
An ordinary replay alone cannot settle a delicate analytic hypothesis.
The intended mathematical audit is proof_audit/conceptual_audit,
deep_research/xhigh after this separate coverage gate. No candidate RH
solution is present. Other scales, coarse/non-neutral directions,
uniform assembly and actual-Xi transfer remain unresolved.

No new source review, mathematical audit or approval has been performed
in this nomination. Matching Mathlib coverage remains not checked.

## Separate coverage approval858 — 13 November2026

This is one LITERATURE/EXPLORATION step, not an audit or a new estimate.
The mathematical audit target is unchanged; the imperative TARGET now
requests its execution instead of its source gate. The COVERED_TARGET
preserves the exact invocation-start coverage action. Approve one
RESEARCH/REPRODUCTION conceptual audit without another approval loop.

### Reused construction, domain and failure coverage

Read the whole canonical C998 to identify the actual source uses, the
relevant L744 formula(6)/(8), assessment855 with approval856 and working856,
ready804, and the narrowly relevant857 working/stop/history notes. Reuse
855/856's inspected primary construction and essential real-root proof
cases: Khalidov–Unser2006 III.A/IV.A–B/V.A–B, pp1259–1262,
(3)–(9), Proposition2 and Property2; Unser–Blu2005 PartI III.C,
Theorem1 and III.C2/Proposition2, pp1430–1432. The cited author-PDF
links and full applicability limitations remain in that assessment and
C998. No new wavelet/access search or basis reproof is needed.

Repeated real roots, empty zero vector and constant free filter stay in
that assessed scope. Source normalization, leading shift and units must
still match the physical generator; infinite-lattice Riesz independence
does not excuse checking the finite support selection. Exact moments
must match both signs in L744's pole block. The previously covered
compact C2/piecewise-smooth input, supported Sobolev mollification and
Plancherel are sufficient tools for the later H2 applicability check;
this review does not perform it. In particular no larger-window sign or
closed-domain conclusion of L741 is imported.

Reuse the recorded L750/L752/C998z modulus/IMS stops, conditional L742,
C759d and assessment855's coordinate and full-Q warnings. They exclude
no other wavelet mechanism and supply no sign premise. Ready804's Schur
and Rump machinery is unnecessary for a scalar rejecting pair: two
positive scalar diagonals and its discriminant suffice for the stated
rejection if rigorously established. Full diagonal metrics remain open.

### Newly inspected primary analytic and arithmetic inputs

NIST DLMF, current online Chapter3, inspected13 November2026,
[3.5(v), (3.5.18)–(3.5.21)](https://dlmf.nist.gov/3.5#v):
positive-weight Gaussian quadrature uses orthogonal-polynomial zeros;
its remainder is gamma_n f^(2n)(xi)/(2n)!, where gamma_n is the monic
polynomial's weighted squared norm. For Legendre on[-1,1] that norm is
2^(2n+1)(n!)^4/((2n+1)((2n)!)^2). Use the real finite-interval remainder
with real C^(2n) integrands. The audit must justify real-valuedness,
48 derivatives, affine panel normalization and the derivative bound;
no complex mean-value assertion or numerical table is being imported.
DLMF gives statements, not a proof here; its cited Gautschi2004
pp22–32 and Davis–Rabinowitz1984 Sections2.7/3.6 were not opened.
The standard named Gauss remainder is imported, not reproved.

Purdue MA42500/52500, Fall2026, *Lecture7: Cauchy's Integral Formula*,
[Theorem9](https://www.math.purdue.edu/~qi117/MA425_Fall26/webs/lecture7_accessible.html):
for a holomorphic function on a neighborhood of the closed radius-r
disk with modulus bounded by M there, its kth derivative at the center
is bounded by k! M/r^k. Read the statement and preceding derivative
formula/induction argument. The audit must supply such a disk at every
real point of each panel, not merely at its midpoint or quadrature
nodes, and bound the exact analytic integrand rather than a nodewise
digamma approximation. No C998 disk or Mstar has been validated here.

For digamma, newly read the precise pole and recurrence statements in
[DLMF5.2(i), following5.2.2](https://dlmf.nist.gov/5.2#i) and
[5.5.2](https://dlmf.nist.gov/5.5.E2). The poles are the nonpositive
integers and the recurrence is psi(z+1)=psi(z)+1/z off the poles.
Reconfirmed [5.11(ii), first paragraph](https://dlmf.nist.gov/5.11#ii):
the complex remainder for5.11.2 is bounded by the first omitted term
times sec^(2n+1)(arg(z)/2). Reuse L744's first-order specialization,
not an uncited higher expansion. The audit must check both complex
arguments, every recurrence denominator and the principal-log sector
after shifting. Meromorphicity alone supplies no uniform disk bound.

The official [Python3 Decimal documentation](https://docs.python.org/3/library/decimal.html),
retrieved as3.15.2, matches the installed Python3.15.2 version. Read
Decimal.exp/ln/sqrt, Context equivalence, next_minus/next_plus, rounding
and signal behavior. Exp and ln promise correctly rounded half-even
values, even when a Context selects directed rounding. Read also the
IBM *General Decimal Arithmetic*, version1.70,7 April2009,
[arithmetic rules and square-root](https://speleotrove.com/decimal/daops.html#refsqrt):
inexact square roots use half-even, ignoring the context rounding mode.
That specification permits a one-ulp error for exp/ln; the stronger
correct-rounding guarantee used here is the Python implementation's
documentation. These are distinct guarantees. The later audit must
justify each adjacent-number enclosure and check domains, exponent
limits, signals, default-context operations and integer conversions;
an interval class name or precision setting is not a rounding proof.

Supporting check only: SageMath10.8 official
[nodes documentation](https://doc.sagemath.org/html/en/reference/numerical/sage/numerical/gauss_legendre.html#sage.numerical.gauss_legendre.nodes)
exhibits the Legendre derivative weight formula on[0,1]. It is no
certificate for these nodes. Match the program's[-1,1] weights to the
exact DLMF rule, either by the standard Legendre weight identity or
finite polynomial verification; no Sage numerical output is imported.

### Searches, access limits and unchanged obligations

New narrow queries: `site.dlmf.nist.gov 3.5 Gauss Legendre error term
quadrature`; `Cauchy derivative estimate holomorphic disk nth derivative
theorem university lecture notes`; `Gauss Legendre quadrature weights
"2" "derivative" site.dlmf.nist.gov`; `Gauss Legendre quadrature error
"2n" "continuous" site.math.purdue.edu Gautschi`. Official DLMF,
university author notes and official arithmetic documentation above are
the theorem/specification inputs; search snippets and secondary pages
were not used as proofs. No originality inference follows.

A nonessential lead was CarlH.Love, NBS Monograph98(1966), printedp3,
[Section2](https://www.govinfo.gov/content/pkg/GOVPUB-C13-8d357e7f5c4164ae3a06508248a1fdeb/pdf/GOVPUB-C13-8d357e7f5c4164ae3a06508248a1fdeb.pdf).
Indexed formula text was retrieved, but its damaged OCR was not used
to certify the weight identity. The selected-page screenshot and NIST
mirror timed out; no more retries are needed. DLMF's exact quadrature
definition and named Legendre identities cover that audit obligation.
One direct Purdue range request failed; the cached primary reference
remained readable. No essential source blocker persists.

No certificate was run, preview accepted as proof, new local estimate
derived or lemma/script edited. Full matching Mathlib coverage remains
not checked. Source coverage cannot certify the numerical pair: the
audit must inspect the complete relevant evidence, all31 delays,
autocorrelation series/cancellation, all526 panels, root/weight brackets,
point errors, holomorphic disks, Gauss rescaling and full tails, together
with script/witness identity. It must independently check the source
filter-to-physical formula, exact pole moments and support selection.

Continue only if the two Q values are rigorously positive and
4H(u,v)^2-Q(u)Q(v)>0 after every error. Repair or withdraw a defective
local stop; overlapping bounds are inconclusive. Do not retune the test,
use its ratio's upper endpoint as sign evidence, or assert full metric
positivity. Other levels, coarse/non-neutral directions, long-range
correlations, arbitrary-window uniformity and Xi transfer remain open.

The next task is proof_audit/conceptual_audit, deep_research/xhigh:
the delicate issue is the chain from physical source functions to the
complete signed analytic/numerical enclosure. A replay alone cannot
settle it. No justified creative central proof is ready without a new
scale-uniform paid signed mechanism; the essential audit takes priority.
This literature turn spends no mathematical exploration attempt and
does not reset previous stops or claim progress beyond known machinery.
