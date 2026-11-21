# Actual Mellin remainder: source-scope nomination after L797

TARGET: Assess paper23 v1 Lemma2 estimate (11) against uniform complex saddle-point theorems, using L797, and isolate one independently testable remainder bound that does not depend on unavailable supplements.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step511 searched uniform complex saddle explicit errors and complex Mellin moments, checked exact-title overlap, reused the named local saddle assessments and stops, and inspected the primary statements/proof cases below. No matching effective uniform (11) was imported; search failure is not novelty evidence.
SOURCE_EVIDENCE: paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(15); DLMF2.4(iii) hypotheses(a)–(c)/(2.4.11)–(2.4.16); O'Sullivan PJM298(2019),157–199, Assumptions1.1/Theorem1.2 pp159–160, (2-8) p165, (4-1)–(4-6) pp171–172, Corollary5.1/proof pp175–176; Temme1308.1547v1 Section4/4.1 (4.1)–(4.9). Links and access qualifications below.
COMPARISON: Fixed-data saddle expansions and parameter-uniform pole separation do not supply the source's moving-domain effective constant, endpoint continuation or global tails. L797 supplies geometry only. A precisely formulated finite-diameter local-phase audit is independent of the missing supplement; its inequality is not established by this comparison.
GAP: Full (11), amplitude control, horizontal/far-left/continued-endpoint contributions and their scaled monotonicities remain unverified. The local 1.1/Q term is separately testable from the printed phase and L797; no uniform remainder theorem automatically verifies its constants.
REASON: Completed source-scope NEGATIVE rejects automatic import of full (11) and parks its global assembly. Nominate one bounded local remainder audit with all data specified, for separate approval before mathematics; no new lemma or bound this turn.
LITERATURE_REASON: Changed hypothesis and conclusion: the existing ready assessment covers an elementary complex map, whereas estimate (11) concerns a uniform Mellin integral remainder and requires new source-level hypothesis comparison.
SCOPE: Completed literature-only review of the exact TARGET. SPECIALIZE records partial method coverage and the independently testable local component, not verification of (11). The original nomination below is retained as history. New local continuation has its own assessment and requires separate approval before research. No automatic real-zero transfer or supplement search is authorized by this assessment.

## Original purpose, bounded review and decision test

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is to determine whether the source's specified remainder claim admits
an independent, source-covered analytic test after L797. Its plausible
downstream use is a controlled actual Mellin quotient, which could
support assessment of a root-independent representation. Even a proved
remainder would leave inversion, finite certificates and the sufficient
sign bridge unresolved; no complete route is asserted.

Read the exact statement of (11) and the essential contour/local/global
proof cases before larger source extracts. Retain every additive term,
relative-error denominator, branch, endpoint and parameter qualification.
Compare a primary uniform saddle theorem only after matching these data;
a positive real saddle curvature is not a global tail estimate. Check
specific notebook-local duplicates and failures for the extracted claim,
without reopening the earlier zero-free or reciprocal-continuation routes.

Continue only if the accessible statements specify a finite, independently
testable remainder inequality with explicit hypotheses and a justified
relation to (11). Save its separate assessment for later mathematical
work. If an essential premise still depends on the unavailable supplement,
record the exact missing premise and park this dependent task; do not
repeat access searches or substitute a numerical grid. A source-scoped
negative is acceptable, and no new lemma is required.

## Essential inputs and preserved stops

L797 is the checked map input. L019/L021 supply the actual theta kernel
and moments; the step508 comparison records the source's P=K/2 and
M(s) conventions, which must be checked in the extracted formula before
any future application. L795/L796 are contrast and stop context only:
full-support common interlacing and a common Favard measure already fail.
Step507's multiple-orthogonality and ferromagnetic proposals still lack
specified actual representation data; ordinary B_J membership still lacks
a sufficient sign theorem. These facts do not ban other mechanisms, but
they do not justify relabeling this remainder review as creative work.

The supplement, evaluator provenance, finite enclosure inputs, inversion,
Levy integrability/signs and all-degree transfer remain unresolved. No
numerical certificates or cross-notebook theorems are inputs to this
review. Full matching Mathlib coverage remains unchecked. If a later
actual-coefficient computation is selected, L778/L791's analytic and
software contracts must be retained; they are not needed for this review.

## Completed source review — step511, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
was source coverage for the uniform Mellin remainder. Its plausible use
is controlled cancellation in the actual Mellin quotient, followed by
separately assessed inversion and a sufficient sign mechanism. The
decision test asks for a finite inequality with explicit independent
inputs. The full remainder has not passed; the local component below
meets the specification test only. No mathematical estimate was proved.

### Exact source data and unpaid cases

bramble_trace, [paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section3 Lemma2, defines the following objects:

    D = {s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    F(z)=z(pi exp(2z)-9/4),  x=x(s)=u+ih,  F(x)=s,
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    A(s)=2F'(x)/x,  Q=pi exp(2u),  d=3/(16u),
    L(s)=4pi^2 exp(S_s(x)) sqrt(2pi/A(s)).

Log and square root are principal. Its exact (11) is

    |M(s)/L(s)-1| <= 4.5/Q,  s in D.

M initially means the integral of z^(2s)P(z) over positive real z,
Re(s)>-1/2, and elsewhere its Taylor-subtracted meromorphic continuation.
The step508 comparison and L019/L021 identify P=K/2 and
M(n)=M_(2n)/2. No factorial or Jacobian may be inserted into (11).
In particular, the original integral is not a definition on all of D.

The proposed contour uses theta=Arg A and

    H_L=h+d sin(theta/2), H_R=h-d sin(theta/2):
    0 -> i H_L -> x-d exp(-i theta/2)
      -> x+d exp(-i theta/2) -> infinity+i H_R.

The body asserts strip analyticity, a circle majorant
400 cos(2H)^(-5/2) for H<pi/4, and a meromorphic vertical-endpoint
formula assigned to Derivation87. For Im(s)>=0 it states
0<=theta<=2h and uses the strip clearance. It also asserts, on the
saddle disc, |S_s'''|<=10Q, |S_s''''|<=19Q, a quadratic decrement
at least 1.54Qv^2, and a relative local-phase cost at most 1.1/Q.
These numerical claims have not been audited here.

Retaining all six terms, the printed majorant (14) is

    eta = (1/2)exp(-2u+3/(8u)) + 20exp(-3Q/(5u)),
    Ecal(u) = 1.1/Q + 1.24eta
      + (2.35u/sqrt(Q))exp(-1.65Qd^2)
      + (14u/sqrt(Q))exp(-1.54Qd^2)
      + 600u^(5/2)sqrt(4.7Q/(2pi))(1+10u/Q)exp(-Q/(20u))
      + exp(-Q/2).

The source assigns these to local phase, amplitude, missing Gaussian,
horizontal tails, far left, and continued vertical endpoint. It reports
Q Ecal(3)<4.359006<4.5 and decreasing scaled majorants, with horizontal
concavity, two endpoint regimes and monotonicities assigned to
Derivations42/43/65. None follows merely from checking u=3. Those
derivations remain unread; no access search was repeated. This turn
neither certifies nor refutes these claims.

The important missing hypotheses are a legitimate continued-endpoint
identity throughout the left part of D, full-contour deformation with
the prescribed branches, uniform amplitude and tail inequalities, and
uniform scalar reduction. L797 verifies branch/image/clearance and
positive real curvature, but does not establish these. Even (11) alone
would not establish (13): (15) needs logarithmic differences over the
translated discs and explicit saddle-ratio expansions. Those and the
later inversion/certificates remain outside this review's conclusion.

### Primary theorem comparison and essential proof cases

[DLMF2.4(iii)–(iv)](https://dlmf.nist.gov/2.4#iii), accessed
5 November 2026, hypotheses(a)–(c), (2.4.11)–(2.4.16): analytic
phase/amplitude near the path, specified continuous branches, a finite
endpoint expansion with Re(lambda)>0 and mu>0, uniform absolute
convergence at the other endpoint, and strict real-phase domination
with a uniform gap there. The angular sector has width less than pi.
The interior-saddle case splits the path, keeps distinct root branches
and cancels odd contributions. These are asymptotic statements, not an
effective 6000-onward remainder. A moving saddle and shrinking clearance
need additional uniform controls; positivity of Re A alone supplies no
global domination hypothesis.

Reused the comparison in
[the vanishing-amplitude assessment](2026-10-31-vanishing-amplitude-saddle-review.md),
and checked the official published primary text of C. O'Sullivan,
*Revisiting the saddle-point method of Perron*, Pacific J. Math.
298(1) (2019),157–199, [DOI10.2140/pjm.2019.298.157, PDF](https://msp.org/pjm/2019/298-1/pjm-v298-n1-p08-s.pdf).
Assumptions1.1 and Theorem1.2, pp159–160, fix a bounded piecewise C1
path, neighborhood, holomorphic nonconstant phase, amplitude and saddle
independently of positive N. The phase has a nonzero leading coefficient
of positive integer order mu, and the whole path obeys strict real-phase
domination. Corollary5.1, pp175–176, covers opposite sectors with even
mu and has absolute error exp(Np(z0)) O(K_q N^(-(2M+1)/mu)).
Its constant is independent of q and N, not of phase or geometry.

Inspected the localization proof (2-8), p165: its exponential saving
depends on the complementary phase gap and path length. The local
inverse construction (4-1)–(4-6), pp171–172, shrinks a neighborhood,
avoids other derivative zeros and bounds a Cauchy remainder there.
Corollary5.1's proof cancels odd indices between the opposite sectors.
These cases explain which constants a parameter-uniform specialization
must pay. No such specialization or new inequality is derived here.
ArXiv HTML requests timed out; the published PDF supplied these cases,
so that access failure is not an essential blocker.

N. M. Temme, [*Uniform Asymptotic Methods for Integrals*,
arXiv:1308.1547v1](https://arxiv.org/html/1308.1547v1), 7 August 2013,
Section4/4.1, (4.1)–(4.9), explicitly treats the effect of extra
parameters. Its Gaussian simple-pole case assumes Re(omega)>0 and
analytic f in a strip; the pole starts on one side of the contour,
with deformation/residues when crossing. Subtracting f(i alpha) leaves
an analytic divided difference. The expansion is uniform for the pole
in a domain properly inside the analytic strip. This does not establish
a theta contour approaching its strip boundary, or any paper23 constant.
The exact pole-splitting proof case was read; no blanket uniform-saddle
theorem is attributed to this survey.

Boyd, *Error bounds for the method of steepest descents*, Proc. Roy.
Soc. A440(1993),493–518, DOI10.1098/rspa.1993.0030, was located through
DLMF and the author's institutional bibliography. Its theorem body was
NOT inspected and supplies no imported estimate here. Olver/Wong leads
in the inspected sources likewise supply no independently read stronger
uniform theorem in this step. Missing this optional stronger lead does
not block a direct audit of an explicit finite integral.

### Reuse, search scope and route decision

Queries included `uniform complex saddle point explicit error bounds
theorem parameter dependent phase moving saddle analytic`, `Riemann xi
Mellin transform saddle point asymptotic complex moments remainder`,
`"A continuum certificate" "4.5" "Mellin"`, and the Boyd title/author.
Search hits alone were not used as theorem evidence. The recent
Michalowski hit was compared with the existing
[uniform moment-tube assessment](2026-11-05-uniform-moment-tube-saddle-audit.md);
its far-right parameter tube is not (10), and it does not discharge the
continued left endpoint. No certificate or alternate normalization was
silently transferred. The step507/508 representation stops were reused,
not reopened; ordinary class membership still lacks a sufficient sign
theorem. No cross-notebook input was read.

The source-scope negative changes the route from a possible automatic
global import to a finite local remainder audit. Full (11)'s assembly is
parked pending independent global estimates; inaccessible supplements
are not accepted as premises or repeatedly searched. One local-phase
inequality is specified in
[the continuation assessment](2026-11-05-mellin-local-phase-remainder-audit.md).
It retains the full complex D, finite diameter, Gaussian normalization
and 1.1/Q threshold. It omits neither an error term from a claimed full
bound nor a failed case: it makes no full bound claim at all.

This continuation uses the established saddle method and is a
reproduction audit, not a creative central-sign mechanism. No specified
new actual representation or sufficient sign test has emerged from
step507/508, so the central creative-routing blocker persists. A later
local pass would leave amplitude, tails, inversion, finite certificates
and mixed positivity unresolved. Full matching Mathlib coverage is
unchecked. No lemmas, mathematical scripts, DAG or PROOF assembly changed.
