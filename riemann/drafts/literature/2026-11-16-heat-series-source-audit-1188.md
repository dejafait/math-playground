# Heat-series source audit — nomination1188

TARGET: Audit Polson v24 Lemma 5.2's absolute locally uniform heat-series convergence and termwise differentiation on Re t>0 using unconditional zero-strip and zero-counting inputs.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1189 reused assessments1107/1108 and1184/1185, checked C030a/C030c/C030e and L018/L026, and compared the distinct heat-route stops and class-bridge1181. New exact heat-trace/locally-uniform/termwise/holomorphic queries, zero-counting-title searches and Weierstrass theorem searches located the primary references detailed below; no novelty claim follows.
SOURCE_EVIDENCE: Read Polson1708.02653v24 Definition5.1/(4) p8 and Lemma5.2/full proof p9; Hasanalizade-Shen-Wong2107.06506v1 (14July2021), Corollary1.2/(1.5) p2 and Section2/(2.1)-(2.3) p3; Sutherland MIT18.785 Fall2025 Lecture16 (13November2025), Definition16.18/Theorems16.17/16.19 pp11-12; NIST DLMF25.10(i). Direct primary links and access limits below.
COMPARISON: Polson states and proves the entire requested complex-time conclusion. C030a already establishes real-time smoothness and the same normalization from stronger local inputs, so reproduce neither as a new result. The remaining audit checks the source's complex-compact majorant and multiplicity-weighted summability using independent named counting and Weierstrass inputs; citation alone imports the conclusion but does not independently validate its proof.
GAP: Essential source coverage is complete for one separate REPRODUCTION audit; no pass verdict is supplied here. Check the complex-time inequality, convergence of every fixed-order derivative majorant, finite exceptions, reflection normalization and conjugate reality. No essential access blocker remains.
REASON: Review1189 completes the required gate for the unchanged saved target, extending the old import-only assessments to the exact independent audit. SPECIALIZE is justified by reliability of C030e's retained source input, not mathematical novelty or a central sign mechanism.
LITERATURE_REASON: Nomination1188 was REVIEW_REQUIRED; the independent complex-time/counting audit was expressly outside assessment1184's assembly scope. This turn supplies its missing primary interfaces instead of repeating ready coverage.
SCOPE: Only the convergence/differentiation input retained by C030e on Re t>0; exclude the source's large-time/first-zero assertion, far-time block positivity, finite zero verification and any all-degree or RH conclusion.

The following nomination paragraphs are retained as the pre-review scope;
the completed review1189 below supersedes their coverage status.

The main gap remains L030-L032/C032a actual-Xi positivity for every
real polynomial. A successful heat-series audit could remove one more
source-proof qualification from the existing near-zero assembly. It
would leave the explicit formula, far-time estimates, actual arithmetic
signs, theta signing and realization unresolved.

Essential prospective local input is C030e's exact half-spectrum
normalization and retained hypotheses, with Polson Definition5.1/(4)
and Lemma5.2. Inspect only those source passages and the necessary
standard normal-convergence and zeta-zero hypotheses before expanding
the review. Search existing convergence results/failed attempts in
specific local paths; do not assume absence from this nomination.

The bounded test is a proof valid on every compact subset of Re t>0
for the heat series and all derivative orders actually used, with
multiplicity, off-line zeros, reflection pairing, and any finite
exceptional zeros handled explicitly; alternatively identify a failed
hypothesis or unjustified interchange and its effect on C030e.
This paragraph specifies future obligations and proves none of them.

No new signed arithmetic input has emerged from the scalar audit.
Thus a justified creative target at the central gap is not yet available;
discovery1121's unpaid arithmetic-to-square bridge and stops1117/1181
remain relevant. This nomination does not repeat that discovery,
certify an all-degree route, or spend a mathematical exploration turn.
Full matching Mathlib coverage for the prospective audit is unchecked.

## Completed source comparison1189 — 16 November 2026

This is a literature-only comparison, not a convergence proof or an
audit pass. The TARGET and its half-plane are unchanged. The outcome
records new source coverage and overlap information; no progress beyond
the inspected known results is claimed.

### Exact source statement and proof cases

[Nicholas G. Polson, *On Hilbert's 8th Problem*, arXiv:1708.02653v24,
11 September2026](https://arxiv.org/pdf/1708.02653v24#page=8),
Definition5.1/(4), printed p8, uses one exponent per reflection pair,
with multiplicity. Lemma5.2, printed p9, explicitly states absolute
locally uniform convergence on Re(t)>0, holomorphy, termwise
differentiation and reality on positive real time. These are the full
requested conclusions, not assertions restricted to RH.

The relevant proof case was read completely. Writing rho=b+i*y,
a=-(rho-1/2)^2, the source uses

    Re(a)>=y^2-1/4, |Im(a)|<=|y|, |a|<=y^2+1/4,
    |a|^j |exp(-a*t)|
      <=(y^2+1/4)^j exp(-epsilon*y^2+M*|y|+B/4)

on a compact set with Re(t)>=epsilon>0, |Im(t)|<=M,
Re(t)<=B. This is a transcription for the future audit, not a newly
derived inequality. The proof invokes N(r)=O(r log r) for summability
and conjugation for reality. It separately treats origin bounds and
large-time decay; neither belongs to this target. In particular the
finite first-zero verification is used in that separate large-time case,
not in the convergence paragraph being audited.

### Independent standard inputs and precise applicability

Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros of
the Riemann zeta function*, J. Number Theory235(2022),219-241,
[DOI10.1016/j.jnt.2021.06.032](https://doi.org/10.1016/j.jnt.2021.06.032).
The author-hosted published PDF opened through the beginning of
Corollary1.2, p221, but follow-up requests timed out. The complete
statement was recovered in the authors' primary
[arXiv:2107.06506v1, 14July2021, Corollary1.2/(1.5), p2](https://arxiv.org/pdf/2107.06506v1#page=2):

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
      <=0.1038*log(T)+0.2573*log(log(T))+9.3675, T>=e.

Here N counts all nontrivial zeros with 0<Im(rho)<=T, with no
critical-line restriction. Section2/(2.1)-(2.3), p3, identifies its
symmetric count with the argument-principle count of the entire
completion. Thus its count uses zero multiplicities despite the
set-cardinality shorthand in the introduction. This source interface
was inspected; its full explicit-constant proof and Maple computations
were not replayed. The next audit needs only the stated coarse
O(T log T) consequence, not sharp constants. Values below e and any
finite exceptional occurrences must be addressed in that audit.

[NIST DLMF25.10(i)](https://dlmf.nist.gov/25.10.i) states the open
critical-strip localization and reflection/conjugation symmetry without
RH. L018 already supplies those facts, exact Xi correspondence and
multiplicity preservation locally; L026 rules out zero ordinate.
These are available inputs, not new derivations of this review.
No recent narrower zero-free half-plane is used, so this target does
not reopen L330/L331 or require the quasi-RH baseline reassessment.

Andrew V. Sutherland, MIT18.785 Number theory I, Fall2025,
[Lecture16, 13November2025, pp11-12](https://math.mit.edu/classes/18.785/2025/LectureNotes16.pdf#page=11):
Definition16.18 specifies normal convergence by summability of the
supremum norms. Theorem16.19 (Weierstrass M-test) gives absolute local
uniform convergence from local normal convergence; for holomorphic
summands it also gives a holomorphic sum and locally normal convergence
of the derivative series. Theorem16.17 gives the corresponding local
uniform limit/derivative conclusion on an open set. Its hypotheses and
the whole Theorem16.19 statement, including the end across the page
break, were read. The notes cite Busam-Freitag, *Complex Analysis*,
2nd edition(2009), TheoremsIII.1.3 and III.1.6; these book passages
were not separately read. The named standard theorems may be imported;
their application to this exponential series remains the next audit.

The prospective summands are entire in t; the time domain is open.
The source explicitly permits every fixed nonnegative j. C030e needs
orders at most2N-1 for each fixed N, with no demand for one bound
uniform as j,N tend to infinity or as Re(t) tends to zero. The audit
must preserve this order of quantifiers. It must not discard off-line
zeros or replace complex exponents by positive real nodes.

### Searches, overlap, exclusions and decision

Queries actually used included `"heat trace" "Riemann" "locally
uniformly"`, `"zeta" "heat trace" "termwise" "convergence"`,
`"zeta" "heat trace" "holomorphic" "half plane"`, `"Counting the
zeros of the Riemann zeta function" "Theorem 1.1"`,
`Hasanalizade Shen Wong Counting zeros Riemann zeta arxiv 2021 0.1038`,
and `site:edu complex analysis Weierstrass theorem locally uniform
derivatives holomorphic series notes theorem`. Several spectral-zeta
hits concern a different trace and were not used.

The first search also located Yuichi Kamiya and Masatoshi Suzuki,
[*An asymptotic formula for a sum involving zeros of the Riemann
zeta-function*, Publ. Inst. Math.76(90)(2004),81-88](https://doiserbia.nb.rs/img/doi/0350-1302/2004/0350-13020476081K.pdf).
Its Theorem1.1(i), pp81-82, was inspected: it gives real u down to0
asymptotics for the all-zero sum exp(u*rho^2-v*rho) for v=u or0,
with multiplicity. It does not state the present complex-time,
all-fixed-derivative normal-convergence audit; no further proof passages
or endpoint conclusions were imported. Search also surfaced improved
zero-count constants in arXiv2412.15470; that is an unread lead,
unnecessary for the coarse bound. No failed search establishes novelty.

C030a's full convergence subsection already proves real-time
derivative convergence of all fixed orders and the half-spectrum
normalization, using L024/L026. Reuse it as overlap, not as a new
smoothness lemma. C030c's admissible-test shell argument is a distinct
use of zero counting, not a complex-time trace audit. Assessments1107/
1108 and1184/1185 import Lemma5.2 but explicitly leave independent
source validation outside their scopes. The scoped search found no
completed audit of the remaining complex-time/counting step; this is
not a claim of an exhaustive archive search.

Inspected stops `ATTEMPTS/2026-11-01-heat-time-semiconcavity-source-scope-stop.md`
and `ATTEMPTS/2026-09-20-heat-fourier-relevance-audit.md` concern,
respectively, logarithmic potentials through collisions and an unpaid
global Fourier/height comparison. They are not convergence obstructions
for this trace. The retained finite-block stop1117 and class-bridge1181
still prevent an all-degree conclusion; normalization and holomorphy
pay neither missing sign/class hypothesis. No stopped mechanism is
reopened by this coverage approval.

SPECIALIZE licenses one subsequent REPRODUCTION audit of exactly
TARGET. A direct citation already suffices to import its conclusion.
Independent reproduction is justified solely to check reliability of
C030e's load-bearing heat-series input, particularly complex compact
sets, multiplicity and arbitrary fixed derivative orders. Do not reprove
C030a's real-time transfer or create a new endpoint/asymptotic target.

Continue if the compact majorants, multiplicity-weighted sums, finite
exceptions, differentiation and reflection/reality conventions all
pass; otherwise isolate the precise failed bound or interchange and
its effect on C030e. The prospective downstream use is removal of
that retained source-proof qualification only. The explicit formula,
far-time estimates, actual arithmetic all-degree signs, theta signing
and graph realization remain independent gaps. No newly justified
central creative mechanism follows from these convergence tools;
discovery1121's arithmetic-to-square bridge is still unpaid.

Full matching Mathlib coverage is unchecked. No lemma, mathematical
script, proof graph or argument overview was changed. Screenshot calls
returned no visible image, and the local curl fallback failed DNS;
neither is counted as proof evidence. Complete primary PDF text supplies
the statements above. This gate changes coverage, not mathematical
truth status or the exploration allowance.
