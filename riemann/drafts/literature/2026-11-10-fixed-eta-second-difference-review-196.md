# Fixed-parameter second difference — completed source comparison

TARGET: Test whether Q_{eta_n}(n+1)-2Q_{eta_n}(n)+Q_{eta_n}(n-1)>=0 for every n>=2, with eta_n=1/(64*9^n), the same eta_n in all three terms, and the actual Xi paired nodes with all multiplicities.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step197 searched Li/Keiper convexity, regularized convexity, second differences, almost periodicity and sign changes; reused step192's recurrence comparison and the scoped L967/L971/parameter-only stops. No inspected theorem establishes the target or its negation; this bounded search does not establish novelty.
SOURCE_EVIDENCE: Reused Xiao arXiv:2006.13103v1 Theorem3.2/(3.10), Corollary3.3 with proof and Conjecture3.4, pp4-5; inspected Batchenko-Gesztesy arXiv:math/0506138v2 Section3/(3.6)-(3.8), Theorem3.1(ii),(iii),(viii), and following Hypothesis3.2; inspected DLMF18.5.1 and18.9.1/Table18.9.1; read L972's definition/convergence, L964's unconditional identity/analytic bounds, L966's representation passages and L968's statement.
COMPARISON: Xiao supplies an ordinary-Li signed identity and an RH-conditional absolute bound, with convexity conjectural. Discrete almost-periodic positivity of mean supplies a possible obstruction tool, not an identified Xi second-difference theorem. Neither source treats eta_n in the complete three-term observable.
GAP: Derive and justify the complete index difference, then test whether an almost-periodic obstruction survives prescribed regularization; applicability, nonzero mean-zero spectral structure, integer nonresonance, recurrent sign margins and regularization error remain unproved. No target sign, formula or counterexample is asserted here.
REASON: Essential source coverage now supports one bounded proof-or-obstruction attempt for the unchanged target, beginning with compatibility under an explicitly labeled RH diagnostic. This is a proposed application of inspected tools, not a theorem import or completed specialization; the newly completed assessment receives separate next-turn approval.
LITERATURE_REASON: Startup was REVIEW_REQUIRED: changing polynomial indices at common eta_n lay outside the prior fixed-index moving-eta assessment, and exact convexity/obstruction coverage was missing. Step197 completes that comparison without mathematical derivation.
SCOPE: Actual Xi nodes and all multiplicities, algebraic squares, n>=2, eta_n common to all three terms. Coverage permits the finite-index difference, complete-sum justification and an RH-conditional almost-periodic obstruction test with regularization retained. No off-RH exponential-asymptotic proof, ordinate replacement without a labeled RH premise, or assumed off-diagonal theta formula is approved.

## Relevance and decision — step197

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity, with L966(16)'s R_n<=N_n unproved. The intermediate target
is exactly the displayed fixed-parameter second difference. Its
plausible downstream use is signed index forcing in a later recurrence;
even a successful sign test leaves initialization, parameter movement
and cumulative recurrence margins unpaid. L972 pays one fixed-index
parameter change only; it supplies no index convexity.

The search suggests testing a spectral obstruction before seeking a
positive forcing inequality. This is a proposed test, not its result.
No target-level sign or identity has been derived, and no lemma or
mathematical script has been written. The original nomination is saved
in `history/2026-11-10-fixed-eta-second-difference-nomination-196.md`.

## Primary evidence and exact limitations

Reuse `2026-11-10-prescribed-q-index-recurrence-review-191.md` for its
inspected normalization, hypotheses and complete relevant proof cases.
H. Xiao, *Recurrence relations of Li coefficients*,
[arXiv:2006.13103v1, 23 June 2020](https://arxiv.org/pdf/2006.13103v1),
Theorem3.2/(3.10), p4, gives an ordinary-Li recurrence with signed zero
sum. Corollary3.3 and its complete proof, pp4-5, use RH for an absolute
bound. Conjecture3.4, p5, asserts convexity rather than proving it.
The arXiv landing page checked this turn still lists only v1. No proof
of that conjecture or matching regularized-Q theorem was inspected.
Cite the published recurrence if used; do not rederive it as a new result.
Maslanka's computational recurrence comparison from step192 is also
reused and supplies no sign theorem.

V. Batchenko and F. Gesztesy, *On the spectrum of Jacobi operators
with quasi-periodic algebro-geometric coefficients*,
[arXiv:math/0506138v2, 30 November 2005, Section3](https://arxiv.org/html/math/0506138v2#S3),
(3.6)-(3.8) and Theorem3.1(ii),(iii),(viii), provide the discrete input:

    f in AP(Z), f real, f>=0, f not identically zero => <f> > 0,
    <f> = lim_(N->infinity) (2N+1)^(-1)
                   sum_(k=n0-N)^(n0+N) f(k).

The source states the restriction characterization using Bohr functions
on R and the algebra/translation properties. These are recalled
standard results with references, not proved there. The following
Hypothesis3.2's Toda/curve assumptions do not apply to Theorem3.1.
Read the preceding definitions and full relevant theorem; no Jacobi
spectral theorem is imported. HTML was accessible despite failed PDF
fetches. Corduneanu, *Almost Periodic Functions*, second edition,
Chelsea1989, p47/ChapterI, is a cited but uninspected book lead.

The future application must establish AP membership, reality, mean and
nontriviality for its own sequence. A sign only for n>=2 also requires
justified translation/recurrence before applying a theorem on Z.
No Xi specialization is performed here.

[NIST DLMF18.5.1](https://dlmf.nist.gov/18.5.E1) gives
T_k(cos(theta))=cos(k theta)=(w^k+w^(-k))/2 with
cos(theta)=(w+w^(-1))/2. The inspected
[18.9.1/Table18.9.1](https://dlmf.nist.gov/18.9.i) retain T_0=1,
T_1=x and the three-term recurrence. These identities do not supply a
sign. Complex arguments require justified polynomial/rational
specialization; real phases require the explicit diagnostic RH premise.
The earlier Cauchy/Taylor coverage is reused. DLMF1.10(ii)'s analytic
continuation statement was additionally viewed, but no new continuation
is asserted or needed for the first bounded test.

## Bounded test for a later research invocation

Keep TARGET unchanged. Obtain the entire three-index expression from
L964(5) and L972(1) at common positive eta_n. Use the published identity
where applicable, deriving only the regularized difference missing
from it. Justify complete sums using L024's finite absolute node mass
and the existing analytic bounds. A finite identity does not license
an n-uniform interchange. Any off-diagonal theta representation would
need justification and every distant-h subtraction.

The discriminating first test is **compatibility under RH**, explicitly
an additional diagnostic assumption, not a premise for proving RH.
Test whether the corresponding unregularized difference admits a real,
nontrivial almost-periodic extension to Z with zero mean, and whether
the complete eta_n error tends to zero tightly enough to preserve a
strictly negative recurrent margin. Establish or reject each condition;
none is asserted here. Integer sampling requires excluding constant
frequencies modulo 2pi, not just nonzero real frequencies. Retain all
multiplicities and prove absolute/uniform tail bounds where required.
If using standard AP closure/recurrence facts, cite the standard named
theorem or give the necessary elementary finite-head/uniform-tail
argument; no new general AP theorem is the target.

Continue only with a complete signed estimate or a rigorous obstruction
whose assumptions are explicit. A strict recurrent negative margin
exceeding a rigorously vanishing regularization error would decide the
conditional test. An RH-conditional failure would limit the proposed
RH sign-forcing mechanism; it would not certify an unconditional
negative actual-Xi value or disprove RH. Label generic node countermodels
as such. If the spectral conditions or complete error bound cannot be
justified, record the shortfall and end the bounded attempt. A finite
positive prefix, shifted onset or deleted charge cannot establish the
all-n claim. This test may retire a proposed sufficient mechanism while
leaving the exact actual-Xi sign question unresolved.

## Duplicates, searches and access

Read the full failure records
`ATTEMPTS/2026-11-10-li-theta-boundary-spreading-stop-168.md`,
`ATTEMPTS/2026-11-10-complete-bell-reflected-prefix-stop-189.md`, and
`ATTEMPTS/2026-11-10-moving-eta-only-induction-unpaid-196.md`.
Their specific payment rules remain stopped; none signs this scalar
index difference. L972 is a successful component, not reopened.
Reuse step192's L040 Newton-recurrence, L044/L046 model and theta-heat
duplicate assessments. Narrow searches in November10 Li/Q assessments
and stops found no completed local AP second-difference test. No claim
of originality follows from that search.

Queries included `Li coefficients convexity Xiao conjecture 3.4 second
difference negative`, `"2006.13103" convexity`, `"Li coefficients"
"second" "difference"`, `"Li coefficients" "almost periodic"`,
`"Keiper" "convexity"`, `"Li coefficients" "regularized" "convexity"`,
`"Li coefficients" "sign changes" "difference"`, and
`"almost periodic sequences" "mean" "zero"`. Exact-title follow-up
located Batchenko-Gesztesy's primary preprint. Many hits were irrelevant;
no novelty or nonexistence conclusion follows.

Li-Huang, *Almost periodic functions on time scales and their
properties*, Open Mathematics22(2024),20240107, surfaced as a lead.
Its search-visible mean lemma omits the discrete nonresonance exclusion
needed for this use; it is not selected as an input. Secondary summaries,
claimed RH proofs and computational lists are unused leads. The older
Coffey blocker stays parked and is nonessential here. No essential
source blocker remains for this bounded test.

Full matching Mathlib coverage is unchecked and unknown. L024/L026 give
node geometry/mass; L964/L972 give definitions; L966/L968 give downstream
context. No new DAG edge or PROOF argument is warranted. Outcome:
EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. This supplies source coverage
and a test design, with no mathematical progress beyond the sources.
The newly completed assessment receives separate approval next turn.
