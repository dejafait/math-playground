# Complete correction: bounded complex-ball calculation nomination

TARGET: Certify the sign of C999i's complete Q on [1,3/2] x [40,45] with the full continued-zeta product and outward complex balls, using the fixed 105-point witness grid and at most 4096 covering boxes at 256/512 bits; report a uniform strict sign, two certified opposite-sign witnesses, or an inconclusive enclosure.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed source comparison and exact search/duplicate/failure record in drafts/literature/2026-11-11-complete-correction-signed-enclosure-review-437.md, step438. No computation or additional sign search was made for this nomination; no originality claim.
SOURCE_EVIDENCE: Johansson arXiv:1309.2877v1 Section2/(5)–(14), Theorem1 and proof pp2–4, Section3.1 p5, https://arxiv.org/pdf/1309.2877v1 ; Arb2.23.0 using.html Ball semantics, acb.html complex rectangles/powers/gamma/zeta, acb_hypgeom.html Gamma function, acb_dirichlet.html Riemann zeta function; python-flint0.9.0 acb/arb/global-context documentation. Exact links and qualifications are in review437. Lagarias–Rains math/0104176v5 Theorem5.1/(5.1), p24, proof pp26–27, is reused for C999i's source function.
COMPARISON: Imported continued-zeta and complex-ball contracts supply error-controlled evaluation on points and input rectangles; the remaining task is implementing and checking them for the complete fixed product and finite cover. The sources supply neither a sign nor a successful width guarantee. No reproof of the zeta/gamma algorithms is justified.
GAP: No numerical certificate or runtime backend is present. C999i has only a source-alignment check, not a separate full critical audit. A Q interpretation retains that qualification until its local identity is checked; combined residual, curvature and RH remain open.
REASON: This independently testable component could reject a uniform-Q-sign shortcut or furnish one later signed-budget input. It does not repeat the exhausted uniform-G_w comparisons. Newly written readiness is submitted for separate supervisor approval before research invocation.
SCOPE: Original rectangle, C999i(2) exactly, the grid/cover and precision caps below. One bounded calculation; no event search, new kernel, changed rectangle, adaptive parameter sweep, generator/determinant import, relative curvature bound or full residual sign.

Main gap: L030–L032/C032a actual-Xi positivity, L966/L968 forcing,
L984(H) and C997s's capped bridge remain independent. Essential local
inputs: C999i, C999h(1),(3), C999g and inherited L018/L019. C999f is
not an input. Reviews435/436 and stops427/429/430/436 retain their scopes.
No cross-notebook input is authorized or needed.

Before treating a certificate as evidence for Q, check the C999i
normalization, half-line/pole matching and source domain. Preserve its
pending independent-audit qualification if this is only an applicability
check. If that identity check fails, preserve the exact discrepancy
and do not certify Q from the product. No new formula is proposed here.

Use C999i(2) literally: retain both complex factors 1-2^(1+s/2)
and 1-2^(1-s/2), both completed zeta values and the final real part,
with s=w/2+i*t. The rational term is already absorbed. Do not append
it again, replace the product by absolute values, or use an uncontinued
Dirichlet series. Gamma is the full meromorphic evaluator; powers use
positive real bases. No division by zeta or curvature is involved.

Proposed bounded test:

1. Establish an actual Arb/FLINT backend covered by the cited contracts;
   record wrapper and library versions. Default python3 has no
   python-flint installed. Any task-local installation must stay inside
   the notebook or allowed temporary directory, use no API key, and
   preserve existing work. If unavailable, record that concrete blocker;
   do not silently substitute ordinary floating point or invent a bound.
2. Enclose exact points w=1+j/8, j=0,...,4, t=40+k/4, k=0,...,20,
   in fixed lexicographic order. Use 256 bits, retry only undecided or
   nonfinite results once at512 bits. Stop if two strict opposite signs
   are certified. A positive or negative midpoint is insufficient.
3. If the point test has no opposite witnesses, evaluate the closed
   cover [1+i/64,1+(i+1)/64] x [40+5*j/128,40+5*(j+1)/128],
   i=0,...,31, j=0,...,127. This is at most4096 boxes, each at256 bits
   with only one512-bit retry for undecided/nonfinite outputs. Construct
   endpoints, centers and radii from exact integer/dyadic data and
   check outward containment. Keep every box's real enclosure.
4. Accept a uniform strict sign only when every box has that same
   strict sign, including all edges, with an outward positive margin
   from zero. Opposite strictly signed boxes certify opposite signs
   at their exact dyadic centers. Otherwise report inconclusive; stop
   at the fixed cover/precision caps. Interval zero containment neither
   proves a zero nor excludes one. Do not enlarge the budget this turn.

Save full point/box intervals, exact coordinates, arithmetic/version
metadata, nonfinite/undecided cases, coverage checks and outcome under
scripts/complete-correction-sign/. Serialize exact binary balls or
outward decimal enclosures, never rounded midpoint/radius guesses.
The concise output must state actual/required margins, failures and
certificate paths. Inspect the complete decisive witnesses or all
load-bearing covering evidence; a preview is insufficient. No code,
certificate, lemma or Q sign was produced in this literature turn.

Continue only if a strict-sign certificate survives the formula/domain
and outward-arithmetic checks. Opposite witnesses stop this uniform-sign
shortcut alone; inconclusiveness parks this finite enclosure attempt
without claiming that Q has either sign pattern. A uniform sign is one
component, not an eventwise residual or G_w*G_tt theorem. Far-jump sign,
curvature, event existence, nondegeneracy, multiplicities, initialization,
other heights and global transport remain unresolved. A new mechanism
needs separate source scope; no creative central-gap attempt is justified
merely by scheduling. Full matching Mathlib coverage remains unknown.
