# Actual-G real-zero interval construction — audit coverage

TARGET: Audit L845's all-r nonzero stationary-point construction for the unchanged actual-G angular density, checking zero enumeration, exact normalization, every boundary face, constant phase and all complex partial derivatives.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-target searches, primary-source inspection and duplicate/failure comparison in drafts/literature/2026-11-06-actual-g-real-zero-interval-stationarity.md; no changed mathematical hypothesis or additional source search is proposed.
SOURCE_EVIDENCE: Conrey (1989), Theorem 1 p.4 and (11) p.3, https://www.maths.dur.ac.uk/users/herbert.gangl/morethan2_5.PDF#page=4; Lebl Basic Analysis I v6.3, Theorem 7.5.6 p.290 and Lemma 4.2.2 pp.162–163, https://www.jirka.org/ra/realanal.pdf#page=290; Basic Analysis II v6.3, Theorem 8.3.7 p.38, https://www.jirka.org/ra/realanal2.pdf#page=38; Guide to Cultivating Complex Analysis v1.10, Proposition 2.1.4 p.28 and Theorem 2.4.7 p.49, https://www.jirka.org/ca/ca.pdf#page=28. Direct PDFs reopened 2026-11-06; prior detailed source assessment reused.
COMPARISON: The prior SPECIALIZE assessment covers every theorem used in this finite-r construction. The next task is an independent check of those applications and exact algebra, not a new existence, Hessian or contour theorem.
GAP: Independently verify or repair L845's all-r construction, including all zero-ordering, endpoint, phase and coordinate-transfer hypotheses. No critical audit has yet been completed.
REASON: This reuses unchanged source coverage for a narrowly specified proof audit. It nominates a ready continuation for separate next-turn approval; it does not approve L845's mathematical correctness.
SCOPE: Only L845's stated nonzero stationary points for the original H_r with r>=2 and k=r-1, using L018/L775/L844. No effective location, simplicity of all real zeros, nondegeneracy, thimble, measure change or minor sign is covered.

## Exact reuse and bounded audit

The source assessment
`drafts/literature/2026-11-06-actual-g-real-zero-interval-stationarity.md`
contains the primary theorem hypotheses, inspected passages, versions
and failed/unused leads. It was already SPECIALIZE at the start of the
mathematical attempt. The construction in
`lemmas/L845-actual-g-real-zero-interval-stationary-points.md` uses only
those inputs. This new assessment adds no source finding, and its
readiness is confirmed by the source-only repair below; mathematical correctness remains for the separate audit turn.

Check that Conrey's positive-ordinate result and L018 supply infinitely
many distinct positive real Xi zeros without asserting all endpoints
simple. Verify local finiteness, ordering and separation. Replay (4)–(5)
with the exact k+r-1 denominator, powers of 4 and 8, and no Jacobian.
Check continuity on every face and face intersection, interior
nonvanishing and the single real sign adjustment. Then verify the
coordinatewise Fermat step and each nonzero multiplier in (6)–(7),
including the sign in the angular lift. This is an ordinary finite-
dimensional applicability and algebra audit; no asymptotic interchange
is involved.

Pass only if every r>=2 is covered with H_r!=0 and every original
complex partial equal to zero. A missing phase or coordinate condition
must be repaired or the result weakened/retracted with its failure
preserved. Do not replace the target by modulus stationarity or an
altered density. The next audit must leave Hessian nonsingularity,
contour participation, phase sums, signed remainders and the main
L030–L032/C032a positivity gap unresolved unless separately covered.

L775's complement obstruction, L844's eventual collar exclusion and the
automatic-contour source stop remain at their original scope. No cross-
notebook input is used. Full and supporting Mathlib coverage remains
unchecked. A successful audit would validate a local specialization of
known results, not establish progress beyond the inspected sources.

## Direct-source recovery review — 6 November 2026

The supervisor reported that a ready assessment requires a direct source
URL. SOURCE_EVIDENCE now contains all four direct PDF URLs, with page
anchors. All four resolved on this turn. The author-textbook title pages
match the recorded versions: Basic Analysis I/II v6.3, 15 May 2026,
and Complex Analysis v1.10, 5 November 2026. Conrey's scan identifies
the 1989 journal article. Printed pages equal PDF page numbers here.

Rechecked the extracted Conrey (11) positive-ordinate simple-zero count
on p.3 and Theorem 1 on p.4, the compact real-valued extremum theorem,
Fermat's interior differentiability hypotheses and its maximum/minimum
cases, the chain-rule source location, complex differentiability versus
real differentiation, and the analytic identity theorem's domain and
nonidentity qualifications. The detailed statement/proof-case review in
the stationarity assessment remains the source record; no source proof
is newly audited. No new exact-target search or theorem application was
needed. No essential source blocker was found.

DECISION remains SPECIALIZE for exactly the unchanged TARGET. This
confirms source readiness only. L845 is still unaudited; the finite-r
normalization, all faces, phase and complex partials must be checked in
the next research turn. Reuse the recorded duplicate and failure
comparison; L775's complement stop, L844's collar exclusion and the
automatic-contour stop keep their scope. Mathlib coverage stays unchecked.

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready audit assessment; this bounded accessibility/version check repairs that process defect without repeating discovery or changing the target.
