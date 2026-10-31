# Nonlocal complete sum — small-y transfer audit nomination

TARGET: Audit the fixed-x y-to-zero transfer of Planat 202608.1692 v1 Theorem 3 to L233, retaining the complete residual and specifying the missing uniform signed estimate needed for an all-height first sign.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed source search and theorem-level comparison in drafts/literature/2026-10-31-nonlocal-paired-tail-remainder-comparison.md. Exact local objects were checked in L018, L019, L020 and L233; L559 checks the retained endpoint terms. No claim of an unsearched new positivity theorem or novelty is made.
SOURCE_EVIDENCE: Planat, DOI 10.20944/preprints202608.1692.v1, https://www.preprints.org/manuscript/202608.1692 , Proposition 1 (16), Theorem 3 (31)--(37) with full proof, and Lemma 7/Theorem 5 with full proofs were read this turn. L018 supplies entire real Xi; L019--L020 supply the exact local theta-series/cosine normalization; L233 supplies the exact first-associated-kernel identity. Holomorphic Taylor expansion is the standard named analytic input for the proposed specialization.
COMPARISON: The source supplies the exact complete growth identity and a fixed-y absolute bound. L233 fixes the real-axis derivative expression. Only the fixed-x small-y coefficient and its normalization are to be audited; the source does not supply uniform signed control or an all-height first sign.
GAP: Calculate the exact proportionality between the first nonzero y-coefficient of the complete growth identity and Xi'(x)^2-Xi(x)Xi''(x), including its sign and x factor; distinguish this pointwise identity from any unproved uniform lower bound. No exchange of an infinite block sum with a limit is authorized.
REASON: This is an independently testable normalization/limit specialization, not renewed suppression or block positivity. It may identify precisely what a future signed remainder must bound. No reproof of the source's large-x asymptotics is needed. This newly written ready nomination requires separate supervisor approval next turn.
SCOPE: Fixed real x>0 and y tending to zero through positive values; the complete I defined by the source, not differentiated individual sectors. Use the entire Xi expression to take the limit. No uniform-in-x limit, sectorwise differentiation, extrapolation from fixed y, or first-sign proof is assumed.

Essential inputs: L018, L019, L020, L233, L559; the source's exact
Theorem 3 and Proposition 1. L559 is used to prevent replacing the
complete residual by an endpoint-free quantity, not as a positivity
premise. No cross-notebook input.

The main gap is still actual-Xi all-degree positivity. The intermediate
target is only a verified transfer to the first sign. Its downstream
use is to state the required signed estimate in the actual notebook's
normalization; it supplies no such estimate itself.

Continue if the fixed-x coefficient can be identified from the entire
identity with all constants and the full residual retained. Abandon
any positivity inference that requires a uniform estimate absent from
the sources. Report even a successful transfer as a reproduction of
known analytic structure, and keep the sign gap explicit. A bounded
negative result about the applicability of the fixed-y bound is useful;
no lemma is required merely to document an already recorded failure.
Do not re-audit L559 or the local negative-block theorem.

The proposed work is proof_audit/routine_audit, standard/high: an exact
Taylor/normalization and hypothesis check using the complete entire
quantity, with no nested-integral limit interchange. If a sectorwise
or all-height analytic claim becomes essential, stop at that uncovered
claim and nominate a separate conceptual audit. Creative work is not
justified by relabeling this specialization. Mathlib coverage is not
checked and its absence is not claimed. No derivation of this new
coefficient was carried out in the source-review turn.
