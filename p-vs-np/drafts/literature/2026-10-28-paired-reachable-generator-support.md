# Paired reachable-space generator support — bounded source comparison completed

TARGET: Test whether the paired reachable space K_N=span_F₂{(alpha_A M_A^ell,alpha_B M_B^ell):ell>=0} of L122's original dyadic endpoints has O(N) total expanded-support generators, using the exact N=4 dimension and complete weight-at-most-four span as the first discriminant.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 548 reused step-541/545 primary comparisons and inspected L122 §2, L125 §2, L126's stated scope/parameter matching/audit and Attempts 056–059. New paired-reachable/Krylov, fixed-code sparsest-basis, LDGM and Pascal-code queries established no adequate exact-family match; full submitted queries and access qualifications are in drafts/2026-10-28-paired-reachable-support-source-review-work.md. This bounded search does not certify novelty.
SOURCE_EVIDENCE: Reuse Ésik–Maletti, Simulation vs. Equivalence, 2010 author manuscript Definition 3.1/Theorem 4.2, pp.2–3 (https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf) and step-541/545 proof reads. New primary reads: Mazumdar–Chandar–Wornell, IEEE JSAC 32(5) (2014), §III Theorems 3/5, pp.979–980 (https://sia.mit.edu/wp-content/uploads/2015/04/2014-mazumdar-chandar-wornell-jsac.pdf); Dodunekov, Probl. Peredachi Inf. 26(2) (1990), sole §1 theorem p.101 and §§2–3 proof pp.102–103 (https://www.mathnet.ru/eng/ppi611); Grigorescu–Kaufman, Explicit Low-Weight Bases for BCH Codes, author manuscript Theorem 1, Definitions 3/5, Lemma 6/Claim 7, Corollary 8 and full main proof, pp.2–6 (https://cs.uwaterloo.ca/~elena-g/papers/bch5.pdf).
COMPARISON: The paired reachable common-source theorem supplies no expanded-support budget. Coding results give parameter-dependent fixed-code row bounds or sparse bases for specified code families; none inspected establishes the required bound for this original-coordinate K_N. Code replacement preserving only parameters is insufficient. The audited full-E_N lower bound still requires full parameter spanning and cannot be transferred without proof.
GAP: Determine the actual K_N and its expanded-support generator cost, beginning with exact N=4 Krylov dimension and complete weight-at-most-four span; no equality with E_N, parameter-block surjectivity, code-family identification or uniform asymptotic extrapolation is assumed. Sparse shift and graph realization are separate.
REASON: The changed quantified space now has a completed bounded source comparison, retaining its known qualitative downstream use and the old full-relation stop. No essential source blocker remains and no adequate quantitative import was established; the exact saved target is ready for a later mathematical attempt, without a novelty or success claim.
LITERATURE_REASON: The target changes from generators spanning full E_N to generators spanning the paired reachable K_N. The previous ready assessments explicitly exclude this scope; reuse their qualitative primary proof reads and compare only the missing quantitative statement.
SCOPE: F₂; N=2^k; L122's original endpoint coordinates, literal graphs, right-closed alpha and M and S=16N+20; expanded scalar support. No coordinate quotient, compressed XOR cost, general field, arbitrary-chain lower bound or P versus NP conclusion is covered.

Step 547 proposed this continuation without mathematical approval.
Step 548 completes its separate literature-only comparison. The exact
target is now ready for a later research invocation; no dimension,
support bound or new lemma was derived during either source-gate step.

The plausible downstream use is to test the map-support obligation for
a common source built from the known paired reachable-row construction.
Sparse induced shift, acyclic singleton realization, both boundary
equations and all complete reception/resource obligations remain separate.
A negative result for K_N alone must not be asserted for every larger
boundary-receiving space or every chain without a further argument.

Essential local inputs: L122 §2's complete endpoint actions and boundaries;
L125 §2's full original-coordinate parametrization; L126 §§1–4 and the
step-547 audit in §7, with its precise full-spanning limitation. Reuse
`drafts/2026-10-28-residual-relation-source-review-work.md` for the primary
simulation proof and `drafts/2026-10-28-full-relation-audit-source-review-work.md`
for the support-product comparison. New primary source statements,
proof cases, comparison limits and unread leads are recorded in
`drafts/2026-10-28-paired-reachable-support-source-review-work.md`.
Attempts 056/057/058/059 remain
recorded failures with their original scopes. No cross-notebook theorem
is needed and no new claim of Mathlib coverage or absence is made.

After coverage is ready, the bounded discriminant is the complete N=4
space with every original coordinate retained: exact Krylov-span
dimension and exhaustive weight-at-most-four membership/span data.
Continue only if that evidence exposes a concrete uniform support
mechanism or a defensible necessary-bound argument. A low-weight rank
deficit by itself does not prove superlinear asymptotics; finite full
span does not prove an O(N) family. A proven superlinear generator bound
would stop this exact linear-support proposal. A failed finite search
without completeness is unfinished, not a nonexistence result.
