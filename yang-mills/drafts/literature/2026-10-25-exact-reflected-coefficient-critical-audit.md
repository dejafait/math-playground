# Exact reflected coefficient — critical-audit coverage

TARGET: Critically audit L279's exact fixed-mesh reflected coefficient, checking both insertion jets, moving means, Wilson and quotient-Haar terms, quadratic-only Hodge identification, and the o_a(g^2) remainder after division by g^4.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the parent exact-reflected-coefficient assessment's documented searches and duplicate/failure comparison; inspected L279's complete statement and proof, L003 proof section 1, L011 proof sections 1–2, the production work record and history/478, and ATTEMPTS/046. The audit changes no observable, boundary convention, gauge slice or asymptotic regime, so no broader discovery search was needed.
SOURCE_EVIDENCE: Reopened Kirwin arXiv:0810.1700v2 (5 June 2010), Theorem 2.1 and (2.1)–(2.4), printed pp. 4–5; Lemma 2.3 and the signed-amplitude reduction at its proof opening, p. 7; section 3.2, pp. 14–15; compared Theorem 1.1 and (1.3), p. 3. Reused the parent assessment's previously inspected source cases; no essential unread source remains for this audit scope.
COMPARISON: The parent SPECIALIZE coverage supplies the fixed-dimensional asymptotic mechanism for the same four uncentered amplitudes used by L279. The proposed audit checks that specialization and its connected bookkeeping; it requires neither a new asymptotic theorem nor a Ward-to-reflection identification. Ready coverage permits an independent mathematical audit, not automatic acceptance of L279.
GAP: Perform the separate mathematical review of the exact matrix jets, normalized moments and cumulant signs, remainder orders and leading-law identification. No full audit, repair, mesh-growth bound or uniform reflected-error estimate is completed here.
REASON: The newly registered critical-audit obligations fall within the inspected parent source scope, including signed amplitudes and finite higher-order remainders. The remaining task is verification of the local application of known mathematics.
LITERATURE_REASON: This is the supervisor-required separate approval of the newly registered audit target; the bounded source reopening resolves its precise hypothesis and remainder coverage, without refreshing an unchanged ready target for quota purposes.
SCOPE: Fixed positive even N, a=8/N, SU(2) relative cube, real f_*, ordinary two-dimensional trace, pinned boundary-contained links and variable normal links, exact rooted forest quotient, bare 4/g^2 insertions. No ultraviolet uniformity, physical coupling trajectory, new gauge choice, operator mixing theorem or continuum claim.
COVERED_TARGET: Critically audit L279's exact fixed-mesh reflected coefficient, checking both insertion jets, moving means, Wilson and quotient-Haar terms, quadratic-only Hodge identification, and the o_a(g^2) remainder after division by g^4.

## Primary result and essential cases

William D. Kirwin, *Higher Asymptotics of Laplace's Approximation*,
Asymptotic Analysis 70 (2010), 231–248,
[DOI](https://doi.org/10.3233/ASY-2010-1016),
[version actually inspected](https://arxiv.org/pdf/0810.1700v2).
Theorem 2.1 requires an interior unique zero minimum, separation from
zero away from it, positive radial phase order and leading coefficient,
finite radial expansions, and convergence of a weighted amplitude
integral. Equation (2.3) gives a little-o remainder. Lemma 2.3's proof
permits signed amplitudes by reference to Fulks–Sather, pp. 188–189;
that reference was not newly inspected. The theorem itself treats real
amplitudes, so no independent claim about arbitrary nonsmooth signed
amplitudes is needed here. Section 3.2 handles positive Hessians by a
linear coordinate change and explains odd-coefficient vanishing.
The displayed bound (1.3) is weaker than the needed little-o statement;
(2.3), not that display alone, is the appropriate audit input.

## Comparison with the saved audit obligations

The [parent assessment](2026-10-25-exact-reflected-coefficient-coverage.md)
already covers exactly the local phase and uncentered amplitudes now
listed in L279 (14): density alone, density times either H, and density
times their product. The audit must check the cutoff, smoothness,
absolute integrability and fixed dimension against those actual
functions. L003 section 1 supplies the compact forest-quotient minimum,
positive Hessian and exterior action gap. These are imported local
premises to inspect; this source review does not certify their proofs.
A physical lattice boundary must not be confused with a boundary minimum
in the exponential-coordinate chart.

L279 section 2 requests an expansion after the common volume factor
through degree six. This is a finite order within the parent's smooth
Laplace coverage; there is no source restriction to just a leading
Gaussian term. The mathematical audit must verify the chosen radial
orders and smoothness, partition-function division, claimed vanishing
orders of H and its product, the single-moment errors used in multiplying
the moving means, and the surviving error after g^(-4). This review
approves checking those claims; it does not derive or accept them.

L011 sections 1–2 provide the existing exact quotient-Haar density and
finite-moment connected-expansion method. They do not give the value
of L279's coefficient by citation: the observable pair differs. Checking
L279 (8)–(19), including both insertion jets, every normalization term,
the two cubic vertices and the density sign, is a necessary local
reproduction, rather than a reason to reprove the general Laplace theorem.
L003's curvature-law identification is linear and quadratic only; the
audit must reject any transfer of higher forest jets to a nonlinear
Hodge measure without a separate theorem.

## Duplicates, failures, relevance and test

The existing parent comparison records L004's scalar-only obstruction,
L011's different Ward covariance and the ultraviolet-normalization
warning. ATTEMPTS/046 records why the inspected stability theorem cannot
supply the physical-trajectory error threshold. Those failures remain
in force; none rules out an audit of this finite-dimensional coefficient.
No exact source match for the coefficient was established by the reused
searches, and no novelty claim follows. The production rational check
is algebraic evidence only, not an independent analytic proof or a box
evaluation. No scripts were run or modified during this literature turn.

The main gap is still an interacting continuum theory with a nonzero
physical sector and finite positive infinite-volume mass for every
compact simple group. The intermediate target is an independently
checked fixed-mesh coefficient, useful for identifying terms whose mesh
growth and mixing might later be bounded. Continue if all explicit jets,
connected signs and remainder obligations pass. Stop acceptance of the
coefficient at the first omitted term, unsupported remainder or nonlinear
Hodge substitution; register any changed repair for separate coverage.
Even a successful audit leaves mesh-uniform higher errors, the c_box/2
comparison, a physical trajectory, composite mixing and the continuum
and infrared construction unresolved.

Essential continuation inputs are L279, L003, L011 and the cited Kirwin
theorem; L004 is a scope warning, not a mathematical premise. The next
turn should be RESEARCH / REPRODUCTION. Mathlib coverage of the full
specialization and supporting high-order Laplace and cumulant results
remains not checked; no library absence is asserted. Canonical proofs
remain in lemmas/ and no argument or DAG change is made by this review.
