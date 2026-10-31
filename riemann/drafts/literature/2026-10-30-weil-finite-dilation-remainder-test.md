# Complete Weil form: proposed one-sided finite-dilation test

TARGET: Test a one-sided finite-dilation weak pairing for complete localized Weil eigenvectors, preserving logarithmic boundary contributions and isolating a signed remainder criterion for |tau_L(u)|^2+|tau_R(u)|^2<=C lambda near a hypothetical simple first zero.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the bounded logarithmic Pohozaev, signed-convolution dilation, corrected/withdrawn and general-multiplier searches recorded in 2026-10-30-weil-dilation-flux-coverage.md; narrow Weil literature/ATTEMPTS checks found no duplicate finite-dilation arithmetic remainder test. No adequate theorem for the proposed signed logarithmic weak limit was established; no originality is certified.
SOURCE_EVIDENCE: Ros-Oton–Serra https://arxiv.org/html/1207.5986 Proposition 1.6 and (1.9)–(1.10) provide the inspected positive-order weak dilation precedent, not its logarithmic extension; Grubb https://web.math.ku.dk/~grubb/JDE16.pdf Theorem 4.7 has 0<a<1; arXiv:2411.15985 https://arxiv.org/abs/2411.15985 is withdrawn for a Pohozaev proof error. bramble_trace paper 67 v1 https://rstation.ai/problems/riemann_hypothesis/papers/67 (2.1)–(2.8), (3.4)–(3.5) and Section 9 supply the complete form, conditional support comparison and expressly missing arithmetic bound. Full reading scope and later-paper check are in the completed comparison.
COMPARISON: The known support law already identifies boundary flux with a simple eigenvalue's support derivative; reproducing it is not the target. The uncovered part is a justified finite-dilation weak limit with an explicit signed arithmetic remainder that could control this flux relative to lambda. The withdrawn logarithmic identity and a formal s->0 passage are unavailable shortcuts.
GAP: Test existence and boundary normalization of the one-sided weak limit at logarithmic regularity, then expose rather than bound away the signed pole and prime-power correlations; identify the precise additional estimate needed for C independent of lambda. Neither the limit nor a favorable remainder sign is established.
REASON: This independently testable formulation avoids the failed import and generic absolute-bound stop, while retaining the original relative-flux goal. A successful identity alone is an intermediate result; arithmetic signs, multiple branches and all-support/Xi transfer remain unresolved. This newly written ready nomination needs separate next-turn source approval; no mathematical attempt or approval of a derived identity occurs in its creation turn.
SCOPE: Complete L512 form on I_a=(-a,a), a in a fixed range [a_0,A) with a_0>0, A finite; hypothetical normalized real simple eigenvectors u_a with 0<lambda(a)<=lambda_0 and lambda(a)->0 as a->A. Retain every pole and prime-power term including activation endpoints. L513–L515 give fixed-model bounded data and traces; full-Weil realization and paper 67's collar/support statements remain explicit source assumptions unless separately discharged. No uniform spectral gap or H1 regularity is granted.

## Bounded mathematical nomination, not a derived identity

The main gap remains actual-Xi all-degree positivity. The intermediate
target is one rigorous signed weak-dilation formula, or a precise
obstruction to this formula on the stated data. A formula exposing the
necessary arithmetic cancellation could inform the missing near-null
flux estimate and later support continuation; it need not settle
independent realization, collar, multiplicity or Xi-transfer gaps.

As a proposed test family only, start with inward L2-normalized
dilations u_r(x)=sqrt(r)u(rx), r>1, of the zero extension, and the
complete weak eigen-equation. Determine which one-sided difference
quotients actually exist before differentiating. Compare with source
paper 67's support law only conditionally on its retained assumptions.
No pairing formula, domain differentiability, trace convergence or
commutator is asserted here. In particular, a smooth-core computation
must include a justified passage retaining the actual boundary
contribution; form-norm convergence alone is not a trace argument.

Retain the digamma multiplier, signed pole, and every prime-power
autocorrelation. Do not replace moving atoms by a density derivative,
discard newly active terms, or assume that bounded convolution permits
its derivative to act on these eigenvectors. The two source identities
of positive order are precedents only. Do not use the withdrawn identity.

Continue only if the weak limit and boundary coefficient are justified
and the resulting signed remainder gives a concrete additional
inequality sufficient for flux<=C lambda uniformly on the range.
If one obtains only absolute trace bounds, a formal identity requiring
unavailable H1/differentiability, or the already-known support law with
no arithmetic criterion, record that obstruction and park this version.
An identity without the signed inequality does not prove the relative
bound. The scalar-shift contrast is a required check against any claim
based solely on general logarithmic regularity. One coherent test only;
preserve incomplete calculations and name every extra assumption.

The comparison is in [the completed source review](2026-10-30-weil-dilation-flux-coverage.md).
Existing support-propagation and rank-trace stops keep their original
scopes. No source import or reproof is needed merely to increase lemma
count. Mathlib matching coverage remains unchecked; no cross-notebook
input is used.
