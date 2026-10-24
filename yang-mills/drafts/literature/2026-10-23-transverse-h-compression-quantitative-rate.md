# Transverse-H finite compression — quantitative test coverage

TARGET: Determine whether L116's complete finite-compression difference satisfies |R_prod-R_inf| <= C_i N^(5/2)log(eN)^2 for both actual probes.
CHECKED: 2026-10-23
DECISION: EXPLORE
SEARCH_EVIDENCE: The parent transverse-H comparison searched local compression/rate/eta_N/q_j(N) matches, read history/142 and the original compression draft, and performed four bounded external queries. No inspected matching quantitative compression theorem or duplicate local rate was found; no novelty claim follows.
SOURCE_EVIDENCE: Lawler--Limic, Random Walk: A Modern Introduction (Cambridge, 2010), author-hosted 289-page text https://www.math.uchicago.edu/~lawler/srwbook.pdf , section 1.1 printed pp. 9--11, Theorem 4.3.1 printed pp. 81--83 and Corollary 4.3.3 printed p. 84; direct source access and theorem/corollary locations rechecked 2026-10-23. Reuse the parent assessment's inspected proof cases and applicability record, and its recorded local L110--L124 reads; those proofs were not reread in this repair.
COMPARISON: L110 supplies an axially summable quadratic first moment and L116 supplies the complete finite comparison C_i N^3 eta_N with eta_N tending to zero. The source supplies scalar Green asymptotics/differences, but neither the matrix-entry identification nor a quantitative all-offset tail bound for L116 is established by those existing local statements.
GAP: Quantify L116(10)'s exact squared tail uniformly in N, including every matrix entry and integer axial offset, and apply L116's existing complete trace count without changing its compression order. The requested trace rate is a test, not an imported theorem.
REASON: Accessible scalar inputs and the exact finite comparison make one bounded standard-method specialization source-ready, subject to separate continuation approval. No new kernel estimate is derived or approved as correct in this literature turn.
SCOPE: Only Delta_C=R_prod-R_inf of L116(2)--(3), relative SU(2) cube, admitted sufficiently fine even N, a=8/N, tau=1/16, lower-rooted direction-1 forest, bare-first order and stored coordinates; retain both probes, both coefficient levels and orientations, all filters, both output compression defects, all normal/end rows, constant modes and full heat sums.
LITERATURE_REASON: The complete transverse-H source comparison isolated this previously unassessed quantitative subtarget; the old compression assessment covered only o(N^3).

The separate literature approval on 2026-10-23 repaired the missing
direct primary-source URL and retains EXPLORE for this exact target.
This approval does not derive or verify the proposed rate; the present
step remains literature-only. The parent assessment is
`2026-10-23-transverse-h-quantitative-remainder.md`; its primary versions,
theorem hypotheses, essential proof cases, queries and source limitations
are reused without repeating the search. No essential source is blocked.

The main gap remains an interacting continuum Yang--Mills construction
with the required axioms, a nonzero physical sector and finite positive
infinite-volume mass. This intermediate estimate could remove one
comparison error from the quantitative transverse-H assembly. The four
coefficient remainders in L120--L123, full quantitative L011 assembly,
upstream audit qualifications and interacting control remain independent.

The essential starting results are L110, L111, L113, L114, L115 and
L116; L118 supplies the exact zero comparison and L124 fixes its place
in the complete telescope. L109 is a failure contrast, not a bound.
Import their finite identities and moment/heat envelopes as stated;
this is not an upstream critical audit. Preserve all original conditions.

In L116(10), for its fixed support-clearance constant c>0, the sequence
is exactly

    eta_N = sum_(j in Z)
        (sum_(|z|>=cN) |z|^2 ||e_j(z)||_F^2)^(1/2).

L116(3) already reduces its complete compression difference to
C_i N^3 eta_N. One sufficient test is therefore an explicit bound
eta_N<=C N^(-1/2)log(eN)^2. This states the required modulus; it
does not establish it. A sharper estimate or a direct complete trace
comparison is allowed only for this same Delta_C.

The first source-specialization obligation is the exact identification
of L110's full matrix kernel with correctly normalized and shifted
four-dimensional scalar Green differences. Check every mixed entry,
including j=0 and small spatial distances; do not silently replace
mixed differences by repeated-coordinate bounds. Cite the standard
scalar theorem instead of reproving it, and write out only the necessary
specialization and all-offset squared-tail calculation. No finite
relative covariance is replaced by scalar Dirichlet Green here: e_j is
the separately defined full-grid kernel already present in L116.

Continue on a complete finite bound meeting the threshold with constants
uniform in heat labels before their original sum, or on informative
evidence of a failed specific comparison. Reassess if only fixed-offset
convergence, a discarded matrix component, an uncontrolled all-j sum or
an above-budget allowance is obtained. Do not infer signed growth from
an inadequate upper bound. Do not move a component filter through P_inf,
delete either output selector, assume compact kernel output or use the
failed first absolute moment from L109. No mass schedule or mathematical
script is needed unless a later attempt specifically justifies one.

The existing L116 proof is imported rather than reproduced. Full matching
and supporting Mathlib coverage is not checked; unknown is not absent.
No cross-notebook input is used. This source-ready test spends zero of
three mathematical exploration turns; the usual two-unproductive-turn
reassessment applies after mathematical attempts begin.

## Direct-source recovery record — 2026-10-23

[Lawler--Limic, author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf#page=81)
is the primary source, rather than an indirect reference to the parent
assessment. Direct retrieval returned the complete 289-page PDF; the
Theorem 4.3.1 and Corollary 4.3.3 locations were checked. Reuse the
parent's section 1.1 hypothesis and proof-case inspection: symmetric,
finite-range irreducible walks in dimension at least three, including
the bipartite case. The corollary supplies first and repeated-coordinate
second differences, not an explicit matching matrix-kernel theorem.
The four-dimensional nearest-neighbor applicability and normalization
record remain as in the parent; no reproof is needed. Mixed-entry
identification and the all-offset tail remain research obligations.

The parent's recorded bounded searches and history/142's qualitative
compression comparison are reused for duplicate/failure coverage.
No new search or new mathematical evidence is claimed. L109's failed
absolute-moment route remains a contrast; the squared-tail target is
unchanged. This is a STALLED metadata repair that makes the saved ready
assessment directly source-linked, not progress beyond the inspected
sources and not a mathematical exploration-budget reset.
