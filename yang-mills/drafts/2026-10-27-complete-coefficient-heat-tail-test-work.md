# Complete coefficient heat-tail test — work saved before the long estimate

Approved target and assessment: `drafts/literature/2026-10-27-complete-coefficient-dyadic-shell-test.md` (unchanged EXPLORE, supplied at startup). This is one mathematical attempt, not a new source review.

Main gap: quantitative control of the exact reflected correction beyond L291's o(N^2). Intermediate target: the complete signed dyadic increments and base/infrared terms of a source-dependent proper-time covariance. If they were uniformly bounded, O(log(eN)) increments would give a logarithmic coefficient bound. Higher remainder, interacting lower bound, nonzero continuum sector and positive mass remain separate.

Inputs inspected: L279(20)--(27), L280(1)--(7),(16)--(28), L291's statement, and ATTEMPTS/047--049. The saved literature assessment is reused; no renormalization or finite-range theorem is imported. Existing uncommitted work is preserved.

Formulation being tested: on the fixed relative transverse space H, let A(s,t)=Q* C* diag(1-sh_--th_+) C Q and G_r(s,t)=Q A(s,t)^(-1) exp(-r A(s,t)) Q*. Apply L280(19)'s complete polynomial, with its unchanged affine T(s,t), U(s,t) and complete density D, to G_r. Differentiate both sources after forming that polynomial. At r=0 this is exactly kappa_a; at infinity it is zero at every fixed mesh. No longitudinal replacement or source freezing is allowed.

Discriminating idea (UNPROVED at this checkpoint): at a long infrared time r_N of order N^2 log N, the density response may retain an uncanceled contribution. The smallest relative transverse eigenvalue is lambda_0=12 sin^2(pi/(2N)); its one-color eigenspace has four modes, with the next eigenvalue at least (4/3)lambda_0. Setting r_N lambda_0=(3/2)log N makes its density response potentially of order N^(1/2)(log N)^2. L282's audited strong limit D_N -> d_* I on smooth relative modes has d_*<0. Both reflected nonnegative source matrices have the same nonzero compression to the ground space. This needs a complete mixed-source spectral calculation, with the rest of the spectrum controlled, before a sign or growth assertion.

Necessary competing estimates: retain all differentiated heat covariances. An elementary Duhamel estimate may bound their G-relative norms by powers of log(eN) times exp(-c r_N lambda_0), with c arbitrarily close to one. The first covariance derivative also needs a sharper entry bound using one heat-smoothed leg. This would make the full quartic response negligible. L287's exact curl energy argument may bound the differentiated cubic response by O(N^4 polylog(N) exp(-3c r_N lambda_0)), also negligible at c>7/9. Neither estimate is yet established here.

Continue only after proving the endpoint identity, the full density asymptotic and bounds on all other signed terms. A surviving complete infrared power rejects this bare heat-tail formulation, not logarithmic growth of kappa_a and not every possible scale organization. A selected-group divergence alone is insufficient. If these estimates do not close, retain the precise residual and report EXPLORATION without a sign/divergence claim.

L282 and L287 are additional local inputs on the same hypotheses, not new cross-notebook inputs. L282's strong-density statement and L287's weighted-vertex applicability must be justified in the final proof. L294--L295 are not used to replace any face or boundary stratum.

## Completed disposition

The unfinished obligations above are resolved in the canonical
[L296 proof](../lemmas/L296-bare-heat-tail-infrared-obstruction.md),
including the full high-spectrum trace remainder, both source
derivatives inside the cutoff, the sharper first-derivative entry
bound, the bounded-weight specialization of L287 and all Wilson terms.
No mathematical script or numerical evidence is used. The complete
signed infrared coefficient and a complete ordinary dyadic increment
are unbounded; the uncut coefficient remains unresolved.

Outcome: NEGATIVE, RESEARCH / POTENTIALLY_NEW in the limited assessed
sense, actual task proof_attempt. This is one informative negative
mathematical attempt, not a mathematical EXPLORATION turn and not
certified novelty. The bare path is stopped in ATTEMPTS/050, pending
separate conceptual audit. The new audit assessment is REVIEW_REQUIRED;
it is not approved in this research turn. Existing work is preserved.
