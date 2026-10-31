# Interval-local Hermite signed transfer: completed source comparison

TARGET: Compare interval Gram margins, coupled theta-integral remainders and real-jet angle estimates for a zero-compatible signed transfer from actual P_N to D(Xi) on [T,2T], N=ceil(16(T+1)^2), and nominate one bounded mechanism test.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared exactly the three saved leads; inspected Nie–Zhang v2 Section 4's interval representations and exactness proof, Teschl's regularity/nonvanishing and angle equations, and Romik's exact integral remainder before its absolute-value estimate. Reused existing Hermite/CD/Turan and actual-theta failure assessments; exact searches and access limits are recorded below. No matching signed actual-remainder theorem was found in these inspected sources; no novelty or impossibility inference follows.
SOURCE_EVIDENCE: Nie–Zhang arXiv:2404.17717v2 Section 4, (4.1)–(4.7), Theorem 4.1 and its complete short proof, Theorem 4.6 statement; Teschl, Ordinary Differential Equations and Dynamical Systems, author preliminary version, (5.43)–(5.45), printed p.153, (5.81)–(5.87), Lemma 5.14, pp.166–167; Romik arXiv:1902.06330v3 (2.20)–(2.22), with Theorem 2.1 and coefficient/derivative coverage reused from L564's assessments.
COMPARISON: Interval SOS exactness characterizes an already nonnegative polynomial and does not provide the actual margin. Pruefer nonvanishing uses a regular second-order ODE absent here; its full monotonicity needs an additional coefficient sign. Romik exposes the exact coupled remainder, then bounds it absolutely, without a sign theorem for its mixed discriminant contribution. None supplies automatic signed Xi transfer.
GAP: The actual first-variation remainder B_N=2P_N'R_N'-P_NR_N''-R_NP_N'' has no established sign. A coupled-integral nonnegativity proposal is nominated solely as a falsifiable intermediate target; interval D(P_N) margins, the quadratic remainder, multiple zeros and all higher signs remain independent gaps.
REASON: The bounded three-way comparison is complete and selects one genuinely different correlation test rather than another global SOS screen. Source coverage permits formulating and later attempting this test, not claiming its inequality. Newly written continuation coverage needs separate supervisor approval next turn.
LITERATURE_REASON: Changed target from the fixed finite global evaluation audit to interval-local, zero-compatible actual-Xi sign transfer; essential primary coverage for the three proposed mechanisms was missing at invocation.
SCOPE: Completed literature-only comparison of the three named leads. No new lemma, derived identity, numerical screen, mathematical script or manuscript audit. Detailed scope for the single nominated proof attempt is in 2026-10-31-hermite-coupled-first-variation-test.md.

The main gap is actual-Xi all-degree positivity. The proposed intermediate
direction concerns its first signed form D(f)=f'^2-f f''. Essential
inputs are L564's actual b_(2n), P_N, normalization and derivative errors,
and the scoped stops in L565, L566 and C567a. L567 describes the old
global cone only. No cross-notebook input is proposed.

Write R_N=Xi-P_N. The source question must retain the complete mixed
quantity 2P_N'R_N'-P_NR_N''-R_NP_N''+R_N'^2-R_NR_N'', not just a
bound for one derivative or one sign of a theta summand. This specifies
the object to compare; no bound, new identity theorem or sign conclusion
is asserted. The downstream use would be a rigorously sufficient signed
transfer combined with independently established interval information
about D(P_N). That interval information is not assumed available.

The three leads fixed at invocation were:

- An interval Gram margin for the complete actual-coefficient polynomial,
  strong enough for an explicit remainder budget. Generic nonnegative
  polynomial representation alone would not establish that margin.
- A coupled theta-integral remainder estimate preserving the correlations
  among P_N, R_N and their derivatives that separate absolute envelopes
  discard. Positivity of the kernel alone is insufficient.
- An angle estimate for the real vector (P_N,P_N') and its Xi limit,
  assessed with both derivatives and without division by P_N alone.
  A zero vector at a multiple zero is an explicit obstruction; do not
  assume simplicity or silently exclude it.

The completed comparison below retains the exact hypotheses and selects
one independently testable intermediate assertion. It establishes no
signed inequality. Independent finite interval signs, multiplicities
and higher forms remain unresolved.

The creative proof attempt is deferred until that exact target has
adequate saved coverage. If comparison exposes a decisive mismatch,
retain it and select a materially different test; do not extend the
three finite outside-interval screens or repeat the old diagonal/four-
coefficient diagnostics. This is preparation for a central mechanism,
not a claim that any one of these leads already works. Mathlib coverage
for the proposed signed transfer is unknown/not checked.


## Primary statements and exact applicability

**Interval Gram margins.** Jiawang Nie and Linghao Zhang,
*Polynomial Optimization Over Unions of Sets*,
[arXiv:2404.17717v2, Section 4](https://arxiv.org/html/2404.17717v2#S4),
(4.1)–(4.7), treats real univariate polynomials on a finite union of
compact intervals with a_l<b_l. For h of degree at most 2d_0,
nonnegative on [a_l,b_l], (4.3) states

    h=p^2+(x-a_l)(b_l-x)q^2,
    deg p<=d_0, deg q<=d_0-1.

The odd-degree case (4.2) uses the two endpoint factors instead.
Theorem 4.1's complete short proof uses the representation of
f-f_min and weak duality; (4.6)–(4.7) give the even-degree Gram/moment
version, and Theorem 4.6 states attainment/equality in both parities.
Only that theorem's statement was assessed, not its representing-measure
proof. The source itself attributes the interval representation to
Lukacs/Markov/Polya–Szego/Powers–Reznick. No reproof is needed.

**Inference from these hypotheses:** applying exactness to D(P_N)
minus a proposed numerical budget would characterize that budget's
validity; it would not establish it. This is stronger than a restricted
bandwidth cone but gives no coefficient-specific lower bound. C567a's
outside-interval evaluations do not prevent such a representation on
[T,2T]. Park automatic margin import, not interval certificates.

**Coupled theta remainder.** Dan Romik,
*Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3, (2.20)–(2.22)](https://arxiv.org/html/1902.06330v3#S2.SS3),
uses the full-line theta Fourier integral and the Hermite generating
function. Equation (2.21) is an exact integration-kernel expansion;
(2.22) retains the integral remainder before replacing every summand
by its absolute value. The ensuing bound uses fixed compact K and
Lemmas 2.4/2.6. The saved moving-degree review already inspected both
integral regions and the coefficient proof cases; they are reused.
L564 has since supplied explicit derivative tails. No new interchange
or differentiated coupled identity is asserted in this review.

This is the exact actual coefficient sequence and normalization, so it
is an applicable starting representation. Neither that proof nor the
stronger coefficient/root comparisons in the saved actual-cross-term
assessment supplies the sign of B_N. Retaining its signed integral
before absolute values is a distinct test; mere kernel positivity,
compact convergence and adjacent-Hermite inequalities do not prove it.

**Real-jet angles.** Gerald Teschl, *Ordinary Differential Equations
and Dynamical Systems*, AMS GSM 140 (2012),
[author preliminary version](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
printed pp.153,166–167, (5.43)–(5.45), (5.81)–(5.87), Lemma 5.14.
His regular real equation is -(pu')'+qu=lambda r u, with p in C^1,
q,r continuous, p,r>0 on [a,b]. The nontrivial solution has nonzero
(u,pu') by initial-value uniqueness. His polar convention is
u=rho sin(theta), pu'=rho cos(theta). Equation (5.85) gives

    theta'=cos(theta)^2/p+(lambda r-q)sin(theta)^2.

The source makes full positivity conditional on lambda r-q>0;
(5.87) ensures positive crossing specifically at u=0. Read the
nonvanishing argument, branch-continuation passage and both sign cases.

**Inference:** no regular equation and coefficient sign have been
provided for the actual Xi or P_N. Simultaneous vanishing of Xi,Xi'
cannot be ruled out using that uniqueness theorem. Angle comparison
also needs radius control and derivative information, absent from
absolute compact convergence. Thus no unconditional phase monotonicity
or multiplicity-compatible transfer is imported. This does not rule
out a separately justified, non-ODE angle estimate.

## Local overlap, queries and source limits

Read L564's complete tail proof/application audit and the relevant
statements of L565, L566 and C567a. Reused the saved actual-Hermite
cross-term comparison and moving-degree review, and the precise
L565/L566/global-SOS failure records. L565 stops its diagonal-CD cone;
L566's top-four test is inconclusive at moving cutoffs; C567a stops
three complete global certificates outside the target intervals.
None assesses the proposed sign of the actual truncation remainder.
The named Hermite drafts/assessments/failure records were searched for
angle, Pruefer, coupled remainder, quadratic loss, B_N and monotone
truncation. No duplicate test appeared in those paths; this is not an
exhaustive novelty search.

Reused the actual-theta quartic residual assessment and its failure
record: integrated-frequency Wronskian constraints give no pointwise
frequency localization. The Dimitrov–Xu phase-audit scope was read as
an additional warning, not as an imported identity or completed audit.
The present proposal uses Romik's actual finite remainder and does not
reuse the suspect printed correlation interface. No cross-notebook
input is used.

Queries included `polynomial nonnegative interval Markov Lukacs theorem
sum of squares matrix margins`, `Powers Reznick Polynomials that are
positive on an interval sums squares theorem pdf`, `Polynomial
Optimization Over Unions of Sets arxiv`, `Riemann xi function phase
plane Pruefer angle Laguerre inequality Hermite truncation`, `Pruefer
transformation angle derivative nonvanishing solution Sturm Liouville
theorem`, `Romik Riemann xi Hermite expansion remainder Laguerre
inequality`, `"Riemann xi" "Hermite" "remainder" "integral"`,
`"Hermite" "Laguerre" "partial sums" "monotone"`,
`"Romik" "signed" "remainder"`, `"Xi" "Hermite" "cross term"`,
and `"Hermite" "truncation" "discriminant"`.
Only the primary mathematical passages specified above are theorem
evidence. Unrelated search hits and model-generated RH pages were not
used. Powers–Reznick's original PDF attempts (author guessed path,
AMS and CiteSeer) failed; its abstract/index text was not substituted
for a theorem. Nie–Zhang's accessible research paper supplies the
needed precise interval statement and exactness comparison, so this
optional original-source blockage does not block the selected target.
Historical inaccessible Turan originals are not reopened.

## One nominated mechanism and its bounded test

Let R_N=Xi-P_N, with L564's exact actual coefficients. The proposed
intermediate assertion is the sign of the **linear part** of the
complete mixed remainder already fixed in this assessment:

    B_N(t):=2P_N'(t)R_N'(t)-P_N(t)R_N''(t)-R_N(t)P_N''(t)>=0,
    T>=1, T<=t<=2T, N=ceil(16(T+1)^2).

This is a proposed inequality, not a derived result. It asks whether
actual theta correlations can suppress negative loss of first order
in the tail. No positivity of P_N, no simplicity, no division by a jet
and no generic preservation theorem is assumed. The remaining
quadratic term R_N'^2-R_NR_N'' must still be bounded in a later transfer,
and D(P_N) must have a sufficient independently proved margin. Higher
forms remain separate. Thus even success would not settle RH.

The first bounded test is T=1, N=64, t in [1,2]. Seek a sign-preserving
symmetrization of Romik's exact remainder and test the five fixed
rational points 1,5/4,3/2,7/4,2 for a rigorous negative witness if
needed. A strictly negative certified upper bound for B_64 at any
one of them rejects the proposed all-T nonnegativity mechanism.
If samples pass, they do not establish interval positivity: continuing
requires an analytic interval certificate retaining all theta and
Hermite indices, or a concrete new signed decomposition that can be
tested. No certificate or calculation is performed in this turn.

At an actual multiple zero the proposed bound must be checked as
written, not extended by dividing by Xi or its jet; it may fail there.
Algebraic freedom from division does not guarantee a sign at those
points. A finite interval success cannot resolve their all-height
behavior. The test's purpose is to assess a transfer mechanism, not
reproduce the already known low-height Xi signs from L466.

The exact continuation and source scope are saved separately in
`2026-10-31-hermite-coupled-first-variation-test.md`. This is the only
nominated mechanism. It requires separate approval before research.
Mathlib coverage for the interval representation, phase interface and
full signed-transfer target is not checked; unknown is not absent.
Outcome: EXPLORATION, a completed source comparison and proposed test,
with no mathematical advance or sign conclusion beyond checked sources.
