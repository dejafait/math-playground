# Complete-column variable determinant — quantitative attempt nomination

TARGET: Test the complete-column division-free Wronskian adjoint with a Boman cutoff and conjugated target response for actual-L1 action at exp(-n/64).
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse completed review378/step379's scoped duplicate/failure search and primary-source comparison for this same complete-kernel variable-coefficient density class. No matching growing-n normalized action theorem was identified; no originality claim.
SOURCE_EVIDENCE: Bostan–Dumas Theorems1-2/Lemmas1-3 pp1-4 https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf ; Kasman(1998) equation(3), following paragraph and Lemma3.1/proof p1484 https://kasmana.people.charleston.edu/spec-solitons.pdf ; Dyatlov version2026-11-02 Definition9.1/(9.1)-(9.4) pp97-98 and Definition7.12/Proposition7.14 pp84-85 https://math.mit.edu/~dyatlov/18.155/155-notes.pdf ; reused Boman Lemma1 pp272-273 https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7017-11512_2007_Article_BF02591127.pdf and audited C997s; scope and proof-case inspection in review378/379 and review373.
COMPARISON: Standard determinant numerators avoid division by a vanishing Wronskian, and the smooth-coefficient transpose retains all product derivatives. No inspected result estimates this kernel-specific actual-L1 action. C997t's quadratic mandatory-root obstruction is confined to constant coefficients; order alone gives no improvement here.
GAP: Establish nontriviality or degeneracy for this proposed family and obtain a paid bound on its scaled normalized target action with all coefficient derivatives retained; neither determinant nonvanishing nor the desired rate is assumed.
REASON: Essential formal and finite-order cutoff contracts are available. Step380 separately approves source scope and repairs direct source URLs for this unchanged bounded target; the proposed kernel application and quantitative rate remain research, with no construction or local identity proved in this review.
SCOPE: Integer n>=2; complete C997c/C997s kernel, I=[7/4,9/4], E=[15/8,17/8], z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n; original complex cap exp(sqrt(n)); all n+1 columns, all zeros and closed endpoints. No global inverse Wronskian, Haar or zero-simplicity assumption.

## Proposed single family and test

The main gap is L030-L032/C032a actual-Xi positivity, L966/L968
signed forcing and unpaid L984(H). This intermediate question tests
C997s's fixed-grid point bridge. An unbounded scaled exact-null action
would rule out its exp(-n/64) error at the original coefficient cap;
a family-specific stop would redirect that bridge search. Neither
conclusion settles the main gap or general band duals.

For the proposed later attempt, write f_j(c)=k_n(c,gamma_j) and
h_n(c)=k_n(c,z_star), with the COMPLETE kernel of C997s(2).
The candidate differential expression P_n is the division-free
augmented Wronskian of f_0,...,f_n and its argument, expanded along
the argument column. This is a research recipe using the published
numerator construction, not an asserted application or local lemma.
Use a Boman cutoff chi_(n+1), equal to one near E and compactly
supported inside I, and propose

    phi_n = chi_(n+1) * conjugate(P_n h_n),
    v_n = P_n^t phi_n,
    proposed normalized density = v_n / integral_I |v_n(c)| dc.

These definitions nominate a family to test, without presuming
v_n!=0, full-column independence, a positive target pairing or any
rate. The conjugated response is intended to avoid an arbitrary
oscillatory choice of test phase; its claimed benefit must be proved
in the research turn. Fix the seed cutoff and mollifier with support
margins independent of n, as allowed by the reused Boman contract.
Record their choice before estimates, rather than optimizing silently.

The attempt must justify the exact endpoint polynomial-exponential
specialization and determinant orientation, identify the transpose
with ordinary derivatives, and verify the pairings including the
coefficient derivatives. It must explicitly handle an identically
zero determinant or density and every pointwise Wronskian zero.
There is no permission to divide by g_n or by the Wronskian. If a
rank-reduced construction is desired after a degeneracy failure,
that would be a refined mechanism requiring a new stated target.

The quantitative objective for nonzero v_n is

    R_n = exp(n/64) * |integral_I v_n(c) h_n(c) dc|
                       / integral_I |v_n(c)| dc.

Seek an explicit lower bound proving R_n unbounded on an unbounded
integer subsequence, or a rigorous upper bound showing this family
cannot attain that threshold. A successful lower certificate may use
a lower numerator bound and an upper norm bound; an upper norm bound
alone never proves failure. Pay all growing-order cofactor and cutoff
costs, target cancellations and any choice of n-dependent constants.
No unspecified fixed-n constant counts as a uniform estimate.

Continue only with a quantitative asymptotic comparison or a new
informative degeneracy/normalization obstruction. If the bounded
attempt produces only formal annihilation, fixed-n nonzero action,
small-n certificates or unpaid derivative costs, save the reasoning
and park this family; do not repeat the same recipe without a new
input. Any numerical check is diagnostic, not an unbounded-n result.
If exact band nullity fails, charge the actual leakage by the full
exp(sqrt(n)) allowance before making any lower-bound claim.

## Inputs, qualifications and routing

Use audited C997c(1),(4)-(6), including its g_n bound, C997s(1)-(2)
and the step373 weak-certificate audit. Use audited C997t only as a
constant-coefficient comparison. Retain both beta terms, four upper
endpoint exponentials, the lower window, K's -1 and every zero.
No new primitive or truncated kernel replaces the complete one.

The sources establish generic identities and cutoffs; the normalized
ratio is unpaid local research. Do not reprove those generic inputs
as discoveries. A later RESEARCH classification may be
POTENTIALLY_NEW only in the limited sense of this documented search;
it does not certify originality. Mathlib matching coverage is not
checked. No cross-notebook result or RH candidate is involved.
C997a(8), selected/both-sign transfer, assay/reconstruction,
complements/regulators, L993, L984(H), L966/L968 forcing and Xi signs
remain open. Preserve all earlier stops and unfinished work.

Recommend proof_attempt/creative, deep_research/max after separate
approval. The precise obstruction is the constant-coefficient
quadratic root cost in audited C997t; the proposed variable determinant
changes that mechanism but may merely move the cost into its
cofactors. The bounded test is the actual ratio R_n above, with a
paid uniform lower growth bound or family-specific upper/degeneracy
obstruction as decisive evidence. No mathematics has been attempted
or approved during the source turn, and no counters are reset.

## Separate source approval and URL recovery — step380 (2026-11-11)

The preceding nomination is preserved as the step379 record. This
literature-only step completes its requested separate approval. Direct
primary URLs now occur in SOURCE_EVIDENCE itself, rather than only
in the linked predecessor assessment. DECISION remains EXPLORE for
the identical TARGET and SCOPE; it does not approve a mathematical claim.

Reopened the three primary URLs above successfully. Rechecked
Bostan–Dumas Theorem1 on manuscript p1: analytic independence gives
nonidentical Wronskian vanishing only. Rechecked Kasman pp1483-1484,
especially equation(3), its next paragraph and Lemma3.1/proof: the
numerator has polynomial-exponential coefficients; denominator clearing
in a factorization supplies no normalized-action estimate. Rechecked
Dyatlov's dated title page and Definition9.1/(9.1)-(9.4) pp97-98:
smooth coefficients are allowed and the transpose differentiates the
whole coefficient-test product. These agree with the previously
inspected contracts. Boman's unchanged finite-order cutoff coverage
and the prior duplicate/failure search are reused, not retrieved again.

No new theorem search, mathematical derivation, kernel specialization,
lemma, script or norm certificate was attempted. No source blocker
remains for this bounded attempt. Independence, nonzero density,
cofactor derivatives and the scaled actual-L1 rate are still unpaid.
Mathlib matching coverage remains not checked. The single-family
continuation/abandonment test above is unchanged; C997t's stop and
all transfer gaps remain in force on their stated scopes. This is
a process repair (STALLED), not mathematical or additional literature
progress. The next turn defaults to the nominated mathematical test.
