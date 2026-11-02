# Full-theta Stein premise: proposed specialization scope

TARGET: Verify the reciprocal-hazard specialization of Csordas Theorem 4.2(b) and Bagnoli--Bergstrom Corollary 2 for the normalized full L019 theta Stein kernel, including coordinate constants, tails and the endpoint zero.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed discovery in 2026-10-31-theta-stein-monotonicity-transfer-review.md and exact application comparison in 2026-10-31-actual-theta-stein-premise-scope.md; the target introduces no new density or Fourier-sign assertion.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2, https://arxiv.org/pdf/1309.0055v2, (4.2), Theorems 4.1 and 4.2(b), pp. 10-11; Bagnoli--Bergstrom 4 March 2004 manuscript, https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf, Theorem 3/Corollary 2, p. 4, and Appendix 8.2 Remark 4/concave case of Lemma 4, p. 25, directly read in the completed scope comparison. Saumard v3 Section 2 (6), https://arxiv.org/pdf/1804.03926v3, supplies the Stein-ratio definition already used in C233b/L604.
COMPARISON: Known square-root-coordinate theta log-concavity and hazard monotonicity supply the source inputs. The local kernel matches K(u)=4 Phi(u/2). The weighted full-line Stein tail still needs an explicit identification with reciprocal hazard; this is specialization, not a new sign theorem.
GAP: Write and check the change of variables and constants, auxiliary normalization, open-support regularity, finite tails, centered full-line applicability and continuity at zero. No resulting Stein monotonicity is proved in this literature turn.
REASON: Resolves one independent actual-kernel premise needed by a possible future transfer; C233b and L604 do not decide it. A brief canonical specialization is justified because neither cited theorem is stated in the local Stein coordinates.
SCOPE: Only nonincrease on u>0 with extension to u=0 for the full normalized even L019 kernel. No first Fourier sign, L604 integrated remainder estimate, higher signs, model variation or RH claim.

This assessment is newly written and requires a separate literature approval
before mathematical invocation. It records source scope, not an accomplished
specialization. The next approval should reuse the inspected evidence rather
than repeat the discovery search.

Use L019 for the exact kernel and tails. L233 supplies the downstream
first-sign connection only. C233b and L604 are contrasts, not affirmative
mathematical inputs. There is no cross-notebook input. Keep named imported
results in the canonical proof with their exact hypotheses and qualifications.
Full-result Mathlib coverage is not checked.

The auxiliary density is proportional to Phi(sqrt(s)) on (0,infinity),
not the square of a random variable with full theta density. Verify the
weighted-tail substitution and every scale factor explicitly; no Stein
integration-by-parts or Fourier-sign theorem is needed for this premise.
If any identity, normalization or endpoint condition fails, preserve the
failure and stop the proposed application. A successful check establishes
only this premise; transfer to the first Xi sign and all higher signs remain
unresolved. Reproof of the named shape theorems is unnecessary.

The hazard manuscript's final concave-case line on p. 25 has an apparent
sign/reference typo. Use its correctly signed preceding inequality and
Remark 4, consistent with the theorem/corollary. The 1988 original theta
proof remains unread; import Csordas v2's precise theorem statement without
claiming an independent audit of that original proof. Access details remain
in the completed comparison.
