# Degree-one tame normalizer on the specialized complete moment — source coverage

TARGET: Determine whether L126's degree-one tame normalizer induces a scalar action on the complete A-specialized CM norm moment, with compatible tower maps and a correctly normalized eigenvalue.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 527 searched exact full-level normalizer, local newvector/epsilon-factor and quaternionic sign terminology; inspected Schmidt and Jacquet–Langlands and compared Fornea's actual tower/projection. Prior step-518/521 and step-523/525 assessments and failures are reused; queries and access qualifications are in drafts/source-notes/2026-10-27-degree-one-normalizer-scalar-coverage.md.
SOURCE_EVIDENCE: Schmidt, Some remarks on local newforms for GL(2), JRMS 17 (2002), 115–147, https://sites.math.unt.edu/~schmidt/papers/gl2.pdf, Theorem 1.2.1, Section 3.1 and Theorem 3.2.2 with relevant proof cases; Jacquet–Langlands, LNM 114 (1970), IAS edition https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2-rpl_1.pdf, Theorems 4.2/4.3(i)/15.1 with the one-dimensional proof case; Fornea v2 https://arxiv.org/html/2603.28327v2, Sections 2.1.2/2.2, Theorem 2.20, Corollary 2.21, Section 2.4, Lemmas 3.2–3.6, Lemma 4.12, (63), Corollary 4.19 and relevant proofs; prior audited Voight/L123/L124/L126 inputs reused.
COMPARISON: Local sources now cover conductor-level signs at split prime powers and the division-side special representation without extending the square-free global formula. Fornea supplies tower/control machinery, but its good spherical eigenspace statement does not assert W-equivariance. Assembly through the actual coefficient maps remains a specialization, not an imported scalar identity.
GAP: Identify the actual W local operators and A newvector lines, then prove compatibility with pullbacks, normalized ordinary pushdowns, auxiliary good-Hecke normalization, localization, diamond invariants and pr_A; retain CM-list inversion and determine the correctly normalized eigenvalue only in the later mathematical attempt.
REASON: Essential theorem statements are accessible and inspected; a bounded known-source specialization is justified. No scalar identity or map compatibility is derived in this literature turn. The first precise failure in that chain is an acceptable stopping result; unchanged assumptions require no source-access recovery or additional browsing.
SCOPE: All L123/L124/L126 hypotheses and original n, CM list, W, coefficient module and maps; no rationality, finite-local-condition, nonvanishing or general BSD conclusion.
LITERATURE_REASON: The newly audited degree-one replacement removes the old fiber issue but requires essential unassessed normalizer-action/eigenvalue coverage at the actual full levels; additional browsing must address that gap, not repeat the earlier branch search.
Step 527 completes the separate source review requested at step 526.
The exact TARGET is unchanged. This assessment permits a later attempt,
not its conclusion. Primary hypotheses, proof cases, versions, search,
normalizations and duplicate comparisons are in
[the source record](../source-notes/2026-10-27-degree-one-normalizer-scalar-coverage.md).
No reproof of local newform theory or Jacquet–Langlands is needed.

Local inputs include squared split conductor and division-character
transfer. Their applicability to L126's particular W still needs proof.
Normalizing K_m does not by itself establish preservation of every bad-U
eigensummand. Gonzalez–Rotger Theorem 5.4 retains its square-free-N
restriction and ramified sign correction; the general local transfer is
the available input for the proposed division-prime specialization.

Compare the finite-level geometric action and coefficient endomorphism
through all actual maps. Track the auxiliary-Hecke unit denominator in
(22), pullbacks and normalized ordinary pushdowns in Corollary 2.21.
Treat I as the source's localization, not an immediate elliptic quotient.
Only complete diamond-invariant integrals enter (63). The A summand and
covariant right-translation convention require an applicability argument;
the good spherical eigenstatement alone does not supply it.

Retain L123/step-515 audit, L124/step-520 audit and L126/step-526 audit.
The inverted representatives h_t^(-1) in J_W must be compared with the
original CM list using the audited complete-moment contract. They are not
automatically the same raw cells. L125 and ATTEMPTS/060 are failed-route
motivation only. No scalar, Sha or Kummer premise is supplied.

The later bounded test is b_W=epsilon b with compatible tower maps and
normalization, or the first precise failed operator, domain or hypothesis.
Through L124/L126 a successful comparison would give
R=(1+epsilon)loc_p(b), conditionally; this does not evaluate R. Stop that
inference at a failed compatibility. Repetition after failure requires
materially new evidence or a refined mechanism. No full-fiber or shallow
substitution, pointwise pr_A or rationality inference is authorized.

For rank-two use, analytic order two and a nonzero central twist value
remain extra assumptions. Rationality/nonvanishing, second-factor finite
local membership, a multiplicative-prime rank criterion, suitable K,p and
the general rank/order comparison remain independent. Mathlib coverage
of the complete action is not checked. No proof or calculation for this
target was performed in steps 526 or 527. A central creative mechanism is
not prepared by this review; eligible next work is established-route
specialization, not a relabeled creative turn.
