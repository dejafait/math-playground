# Integrated adjoint payment with an amplitude bound — nomination1002

TARGET: Assess source coverage for an integrated adjoint payment with 0<=eta<=1, C467b's prescribed initial bump and common compact support, requiring nonnegative spatially integrated full signed flux through T_0.
CHECKED: 2026-11-15
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1003 completed bounded integrated-flux/amplitude-cap, bathtub and density-constrained-duality searches; compared exact local current records and stops961/968/979/1000. Queries and inspected primary cases below; no matching theorem or novelty conclusion.
SOURCE_EVIDENCE: Reuse ready998/review998 and ready1001 for unchanged analysis; newly inspected Lieb–Loss Analysis Theorem1.14 p28 https://www.math.utoronto.ca/almut/MAT1000/LL-1.pdf and author errata 18November2016 p1 https://loss.math.gatech.edu/other/2ndedition/errata161118.pdf ; Cardaliaguet–Meszaros–Santambrogio 19July2016 Sections2–3, Proposition3.3, Lemma3.5/proof pp4–8 https://cvgmt.sns.it/media/doc/paper/2733/20160719_carmessan_final.pdf ; precise scope and nonimports below.
COMPARISON: Static capped-weight optimization does not construct a smooth time-dependent test; density-constrained transport duality optimizes the density/flux rather than a capped test against this fixed current, and permits weak potentials. Reused real-flow/boundary comparisons leave their previous unmatched hypotheses. No checked theorem decides this actual integrated condition.
GAP: Construct or rule out exactly the prescribed capped smooth compact test through T_0 with nonnegative spatially integrated complete flux a.e. No new feasibility criterion, mass estimate or incompatibility is proved; global assembly, all degrees and Xi transfer remain independent.
REASON: Changed integral-and-cap hypotheses required this literature-only review. Essential coverage is sufficient to nominate one bounded mathematical attempt, classified EXPLORE rather than IMPORT/SPECIALIZE; its new ready continuation needs separate next-turn approval. No mathematical exploration budget spent or reset.
SCOPE: Source comparison only for C467b's actual B,H_x,H_0,n=3,R=1/4,a=1/16,T_0=1/1920, first lifetime, fixed buffer cutoff and eta_0, with C467a's complete A,Bij,G and the exact test and inequality below. No new boundary data, restart, global real velocity, lifetime regularity, stopped-set inverse or raw terminal slice may be assumed.

The following nomination is preserved as proposed at step1002; its source
status is superseded by completed review1003 below.

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. A successful integrated payment could preserve a positive
initial tested mass on this one actual chart despite signed local flux.
Its connection to global assembly and actual-Xi positivity would remain
unproved. This nomination is a proposed research direction, not a claim
that this local comparison suffices for the main gap.

The test to assess is real, nonnegative, spatially smooth and C1 in time
on [0,T_0] times I, with continuous bounded first derivatives and one
compact spatial support K strictly inside I, as in C467b, now additionally
0<=eta<=1. Its initial value is exactly C467b(3), and the required payment
is, for almost every t in (0,T_0),

\[
 \operatorname{Re}\left[-i\int_I
  \{\eta_t A+\eta G-\eta_1B_{23}+\eta_2B_{13}-\eta_3B_{12}\}\,du
 \right]\ge0.
\]

Keep the full expression in source comparison; C467b proves G=0 for this
actual buffered cutoff. Its tested representative and positive initial
mass are established inputs, with raw positive-time slices identified
only almost everywhere and no claimed raw slice at T_0. No claim about
existence of this new test is made. In particular the previously proved
characteristic obstruction uses a pointwise inequality, which is absent
here; neither that argument nor scalar amplitude rescaling decides the
capped integral target without further work.

The next turn should compare exact and stronger literature results on
integrated transport tests with amplitude constraints and positivity of
tested currents, check duplicates in the named local current records,
and inspect primary hypotheses and essential proof cases only where
needed. Reuse ready998/review998 and completion1001 for unchanged tools;
do not repeat generic flow or Sobolev discovery. No new mathematical
attempt is approved in this nomination. A useful assessment must retain
the initial datum, cap, common support and complete flux; a theorem that
changes any of them leaves an explicit difference.

Continue toward a later bounded mathematical test only if coverage is
IMPORT, SPECIALIZE or EXPLORE for this exact condition, with source
applicability resolved. A known incompatibility or an essential unmatched
hypothesis must be recorded precisely; a failed ansatz is insufficient.
Persistent source obstruction requires a different independent target,
not repeated approval of C467b. Full matching Mathlib coverage for the
changed target has not been checked.


## Completed source review1003 — 15 November 2026

This is one literature-only step on the invocation-start TARGET. The
main gap, proposed intermediate test, downstream use and exact inequality
above are unchanged. Read C467b (1)–(11) and audit1002's full balance and
endpoint case, C467a (1)–(7), ready998/review998, ready1001 and the named
local stop records. No new lemma, mathematical script or test is derived.

### Search and local overlap

Queries used:

- `continuity equation duality test functions constraint 0 1 compact support mass monotone signed flux`;
- `bathtub principle Lieb Loss Theorem 1.14 bounded density optimization pdf`;
- `continuity equation state constrained optimal control duality density upper bound test function`;
- `Lieb Loss Analysis errata Theorem 1.14 bathtub principle sigma finite`;
- `"integrated" "adjoint" "test" "amplitude" transport positivity`;
- `"On the Transport of Currents" theorem superposition normal currents vector field hypotheses`;
- `"Lieb" "Loss" "Analysis" "pdf" "1.14" site:edu`;
- `"bathtub principle" "Proof of Theorem 1.14"`;
- `Cardaliaguet Meszaros Santambrogio first order mean field games density constraints duality theorem 2016 pdf`.

Targeted searches of the 14–15 November actual-h current assessments,
current histories and the named attempts found only nomination1002 for
the changed integrated, capped target. This is a bounded duplicate check,
not an assertion about the entire archive. C467a establishes a fixed-test
balance, and C467b establishes the time-dependent balance and positive
initial mass, but its obstruction requires pointwise payment. Stop1000
therefore remains valid without deciding this changed condition.
Stop968 warns against inferring a sign from a weak current identity;
stop979 closes an unchanged modulus audit; stop961 concerns an earlier
outer-exit defect in a broader class. None imports the new payment or
prohibits this buffered, integrated target. Prior unfinished work remains.

### Primary statements and essential cases actually inspected

**Static cap.** Lieb–Loss, *Analysis*, second edition, Theorem1.14,
printed p.28, [chapter scan](https://www.math.utoronto.ca/almut/MAT1000/LL-1.pdf#page=28).
The theorem minimizes the integral of a real measurable function against
a measurable weight between zero and one with a prescribed total integral;
sublevel sets must have finite measure. The text leaves the proof as an
exercise. [Author errata, 18November2016, p.1](https://loss.math.gatech.edu/other/2ndedition/errata161118.pdf#page=1)
adds sigma-finiteness and finite infimum for its uniqueness claim.
This single-time theorem has no smoothness or time-compatibility
conclusion. Our test has no prescribed unweighted spatial integral.
No optimizer, relaxation equivalence or dynamic construction is imported.
The first full-book mirror failed; the university chapter and author
errata were accessible, so this is not a persistent source blocker.

**Dynamic density cap.** Cardaliaguet–Meszaros–Santambrogio,
*First order Mean Field Games with density constraints: Pressure equals
Price*, [author version 19July2016](https://cvgmt.sns.it/media/doc/paper/2733/20160719_carmessan_final.pdf),
published SIAM J.Control Optim.54(5),2672–2709(2016), DOI10.1137/15M1029849.
Inspected (H1)–(H4), pp.4–5; Problems3.1/3.2 and Proposition3.3, p.7;
Lemma3.5 and its full proof, p.8; relaxed class at pp.8–9.
The periodic model uses a probability initial density strictly below a
cap greater than one by a positive margin, C1 terminal data, a continuous
convex differentiable Hamiltonian with two-sided superlinear growth,
and continuous nondecreasing coupling. Proposition3.3 gives duality and
an attained density/flux minimum; its proof is omitted by reference.
It optimizes both density and flux. The cap concerns density, not the
Hamilton–Jacobi test. The following compactness proof gives BV/Lr
potential bounds, using the strict initial margin and coercivity; it
does not assert a C1 minimizer. Our current is fixed and our capped test
has a prescribed initial bump and common interior support. Consequently
this theorem is not imported, and its omitted duality proof is not an
essential missing input for the proposed direct attempt.

**Other inspected comparison, not an input.** Graber–Meszaros,
*Sobolev regularity for first order mean field games*, Ann.IHP AN35(2018),
1557–1576, [Section2.2, Theorem2.5 and displayed proof, pp.1562–1564](https://ems.press/content/serial-article-files/15935?nt=1#page=6).
Read the continuity/HJ optimization and terminal-data classes and
Fenchel–Rockafellar proof setup. This also varies density and flux on
a torus, assumes positive continuous probability initial density and
Lipschitz terminal potential, and has no cap on that potential. No
specialization or convex-duality equality for our test class is asserted.

**Unchanged tools reused.** Ready998/review998 already inspected
Ambrosio–Crippa April2013 Section2 Proposition6/Remark7 and Boyer
Theorem4.1, Lemma4.2 and Proposition4.1, including the negative-part
boundary proof. Their real velocity, regularity/growth and ordered
inflow/source hypotheses are not newly established for this zero-
extended current. They supply no automatic common-support smooth test
or integrated payment with a cap. Ready1001's scalar representative,
Fubini/DCT and local ODE coverage is unchanged. No repeat generic
transport search or additional theorem import is needed.

Search results also located *Optimal Control of Continuity Equations*
(arXiv:1506.08932), *State-constrained optimal control of the continuity
equation and infinite-dimensional viscosity solutions* (arXiv:2604.01768)
and current-transport papers (arXiv:2207.03922,2303.03218). Their primary
theorem statements/proofs were not inspected here; they are unread leads,
not evidence or dependencies. No conclusion rests on their titles or
search snippets. The selected direct fixed-current test does not invoke
those control or current-representation results. Matching Mathlib
coverage for the integrated capped test remains unchecked.

### Decision and bounded continuation

Three comparisons were tested at source level: reuse pointwise
transport; optimize a static capped weight; use density-constrained
transport duality. The first retains unpaid extension/support premises;
the second does not join tests in time; the third changes the optimized
objects and regularity class. No inspected result settles the target,
and a failed search establishes neither novelty nor incompatibility.

Decision EXPLORE: nominate one bounded direct actual-data attempt at
exactly the test above, using the audited current and balance. A later
proof may cite standard assessed tools without reproof. Any use of a
static optimizer must justify the missing fixed-data, smoothness and
time conditions; no sufficiency of a per-time relaxation is approved.
A new essential theorem outside this scope requires another review.
There is no essential inaccessible source for this direct attempt.

Continue on a construction only with every cap, initial, regularity,
common-support and full-flux condition proved throughout [0,T_0].
Abandon this condition only on an actual-data incompatibility proof.
An ansatz failure or numerical sample is inconclusive; preserve its
precise residual and require a refined mechanism or new input before
repeating. The required full integrated payment has not been proved
or refuted. A useful local payment would still leave signed global
assembly, all-degree positivity and actual-Xi transfer unresolved.

The new continuation is
[ready1003](2026-11-15-actual-h-integrated-adjoint-payment-ready-1003.md).
It requires separate next-turn approval. This completed review is
EXPLORATION, not a new mathematical result, an informative obstruction
or an RH candidate; mathematical exploration usage is unchanged.
