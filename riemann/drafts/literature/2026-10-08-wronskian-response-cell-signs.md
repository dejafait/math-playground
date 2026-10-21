# Completed bounded response-cell localization source comparison

TARGET: Assess source coverage for a short-shift correlation test that forces both signs of the actual normalized Wronskian inside one interval between consecutive response zeros.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded shifted-Wronskian, Hardy sign/Gram-interval and microscopic shifted-moment searches on 2026-10-08; inspected primary Kösters and Christ–Kalpokas statements and relevant proof cases; reused Young/Bui–Hall and fixed-Gram-grid comparisons; specific local records contain no matching cell-local correlation theorem.
SOURCE_EVIDENCE: Kösters arXiv:0803.1141v1 (7 March 2008), Theorem 1.1 p. 3 and Section 2 pp. 5–9, especially (2.3)–(2.7); Christ–Kalpokas, JTNB 25(2) (2013), 285–305, DOI 10.5802/jtnb.836, (1.1), (2.2), (2.8), Proposition 3.1/contour opening pp. 294–296, Proposition 4.1/full proof pp. 301–302; reused previously inspected Young Lemmas 4–5 and Bui–Hall sign-set coverage.
COMPARISON: Unconditional microscopic shifts are covered on full dyadic intervals, and fixed Gram phases can be averaged exactly; neither supplies signed two-height Wcal correlation restricted to one cell of the variable response phase. Young does not admit the fast cutoff as a weight, and L381's unweighted contour estimate does not resolve its harmonics.
GAP: No source theorem or local argument establishes J_H>0 or a negative within-cell correlation. The fixed-cutoff short-shift test proposed separately leaves its full projection, response-phase harmonics, tails and boundary errors unresolved.
REASON: The bounded comparison isolates a concrete independently testable difference rather than a direct import; propose one fixed interior-cell correlation attempt, with separate next-turn approval and no mathematical application in this literature turn.
LITERATURE_REASON: Response-selected microscopic windows and two different heights lie outside the ready global signed-mass assessment; primary shift and phase-averaging comparisons are essential to the changed target.
SCOPE: Fixed actual F_0,G,A and Wcal of L366/L380/L382, ordinary real derivatives, eventual positive simple response zeros from L372; no RH, F_0 simplicity, noncoincidence, discriminant sign or common-zero-count assumption.

## Proposed target and discriminating test

The main gap remains global actual-theta mixed positivity and the total
L367 margin. The intermediate target is both signs of Wcal inside one
open interval between consecutive zeros of G, at arbitrarily large heights.
Such a test is directed at a noncommon Wronskian witness; it does not
assert a discriminant sign or any RH implication.

Essential input IDs for a later application: L366, L368, L372, L380,
and L382. L373 supplies the comparison obstruction, not a positive premise.
For consecutive eventual response zeros g_j,g_(j+1), propose the statistic

    J_H = sum over [g_j,g_(j+1)] contained in [H,2H] of
          (integral from g_j to g_(j+1) of W_+(t) dt)
          (integral from g_j to g_(j+1) of W_-(t) dt).

The threshold sought is J_H>0 for arbitrarily large H, or a precisely
stated short-shift criterion sufficient for the same within-cell opposite
signs. No asymptotic, lower bound or equivalence with a tractable moment
is asserted. Full endpoint and response-phase restrictions must be kept;
opposite signs separated by a response zero do not meet this target.

The completed source comparison below checks the shifted-Wronskian and
response-cell statement against unconditional short-shift joint moments
and phase averaging. Existing scalar, gamma and global-moment coverage is
reused; the parked sharp-discriminant source and failed absolute
response-grid margin are not reopened.

Continue only if inspected sources cover a concrete statistic and its
localization errors, or isolate a bounded, independently testable uncovered
difference. Abandon this implementation if it supplies only full-interval
signs, excludes no response crossing, or requires unproved common-zero
control/RH; record the precise mismatch. Any mathematical application needs
a saved ready assessment from a separate turn. Common-zero counts, global
positivity, low indices, heights above forty and endpoint margin remain
unresolved. Matching Mathlib coverage for this proposed target is not checked.

## Queries and primary comparisons actually inspected

Searches: `"zeta" "Wronskian" "short" shifts`;
`"Hardy" "sign changes" "Gram intervals" shifted moments`;
`"zeta" "shifted second moment" "log T" phase Gram`;
`"Riemann Zeta-Function and the Sine Kernel"`;
`"Hardy" "shifted" "sign" "Bui" "Hall"`;
`"zeta" "shifted Gram points" moments`;
`"zeta" "Wronskian" "response" zeros`;
`Hall Hardy function shifted correlation sign changes short intervals`;
`zeta Gram points shifted moments phase "Kalpokas"`.
Search snippets located leads only; they are not theorem evidence or
evidence of novelty.

**H. Kösters**, *The Riemann Zeta-Function and the Sine Kernel*,
[arXiv:0803.1141v1](https://arxiv.org/pdf/0803.1141v1), 7 March 2008.
Theorem 1.1, p. 3, fixes real μ,ν and gives

\[
\lim_{T\to\infty}\frac1{T\log T}\int_T^{2T}
\zeta\!\left(\tfrac12+i(t+2\pi\mu/\log t)\right)
\zeta\!\left(\tfrac12-i(t+2\pi\nu/\log t)\right)dt
=e^{-i\pi(\mu-\nu)}\frac{\sin\pi(\mu-\nu)}{\pi(\mu-\nu)}.
\]

The coincident-shift value is the continuous value one. Read Section 2's
scalar approximation, off-diagonal integration by parts (both index
orderings), moving-cutoff endpoints, diagonal freezing and the zero-shift
case, pp. 5–9. The cutoff is t/(2π sqrt(log t)); the summed off-diagonal
error is O(T sqrt(log T)). The p. 4 scaling remark permits log T in
place of log t. Theorem 1.3's statement was inspected only; its proof is
not imported. Theorem 1.1 has no right-line factor, jet error uniform on
complex-shift circles, or response-phase restriction. Its sine kernel
cannot be assigned to the real Wronskian or differentiated without
further justification. It is a scale/method comparison, not an import.

**Thomas Christ and Justas Kalpokas**, *Lower bounds of discrete moments
of the derivatives of the Riemann zeta-function on the critical line*,
[JTNB 25(2) (2013), 285–305](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.836.pdf),
DOI 10.5802/jtnb.836, published version. Their grid solves
Δ(1/2+it)=exp(2iφ) with fixed φ. Proposition 4.1, pp. 301–302, for
real k≥0 and integer l≥0 at sufficiently large T, identifies
the continuous |ζ^(l)|^(2k) moment weighted by θ'(t) with its discrete
Gram-phase moment integrated over φ∈[0,π). Read the complete proof,
including incomplete endpoint intervals. It is change of variables,
not signed two-height information. Inspected Proposition 3.1, p. 294,
with polynomials (2.8) of lengths X,Y≤T, and its contour opening
pp. 294–296: the denominator is Δ(s)−exp(2iφ), with a constant φ and
geometric expansion (2.2). The remainder of that proof and its referenced
discrete second-moment proof are not imported. Uniformity in constant φ
does not license substituting the t-dependent Euler phase of L372.
These statements supply no correlation of actual Wcal within response cells.

**Reused coverage.** Young's *A short proof of Levinson's theorem*,
[Arch. Math. 95 (2010), 539–548](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
Lemma 5 and (2.1)–(2.3), and Bui–Hall's Theorems 1–2/sign-set deduction
are already inspected in
`drafts/literature/2026-10-08-actual-wronskian-noncommon-zeros.md` and
`drafts/literature/2026-10-08-wronskian-second-moment.md`.
Young allows complex critical-line shifts O(1/log T), integer rational
twists hk≤T^(2θ), θ<1/2, and a smooth weight with derivatives
O_j((T/log T)^(-j)). An interior response-phase cutoff oscillates on
the microscopic scale and is outside these weight conditions. A later
application must separate it rather than rename it a smooth weight.
Bui–Hall supplies global sign-set measure, not within-cell transitions.

Read L381's complete same-height contour argument (17)–(20) narrowly:
its holomorphic extension and three edge estimates concern the
unweighted C(t)^2 integral. Multiplying by the phase cutoff, moving
the second height, or introducing either sign of a phase harmonic
changes the integrand. None of these modified contour estimates is
asserted here. L381's ready complex-shift jet and full-tail coverage
is reusable where its hypotheses actually apply; no refresh is needed.

## Duplicates, bounded decision and continuation

The specific local searches and omitted assessment reads found no prior
cell-restricted correlation calculation. Reuse the fixed-Gram-grid and
nonvanishing comparisons in
`drafts/literature/2026-10-08-actual-common-zero-count-bound.md`:
they leave the varying response grid and exact coincidences uncontrolled.
L380's first-mean error, L382's global signed masses, L373's common-only
resets, and L379's absolute-grid margin failure remain valid stops for
those implementations. None forbids the different within-cell test.

Among full-interval correlation, exact response-cell correlation and
fixed-angle Gram sampling, only the second retains the requested
localization. The first loses the response crossing; the third changes
the grid and repeats an already recorded mismatch. The proposed single
bounded attempt therefore fixes one microscopic shift and one interior
phase cutoff, with the actual same-cell indicator retained. Its exact
definition, sought threshold and abandonment test are in
`drafts/literature/2026-10-08-wronskian-cell-correlation-test.md`.
That newly written EXPLORE proposal requires separate next-turn approval.
This review proves no localization criterion, correlation asymptotic or
sign, and imports no theorem into the main argument. No essential source
blocker remains for this bounded test; its missing estimates are
mathematical obligations, not inaccessible theorem premises.

Unread/nonessential leads: the Rochester shifted-Gram distribution
manuscript endpoint returned an internal error; researchgate summaries,
CUE predictions, and conditional pair-correlation leads are unused.
Shell downloads failed DNS, but the two primary PDFs above were readable
through the web tool. No missing source is silently treated as coverage.
Matching Mathlib coverage remains **not checked**. Completed outcome is
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, without an RH range change.
