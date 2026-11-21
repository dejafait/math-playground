# Full-theta recurrence comparison: working record1935

Approved target: Determine whether the full-theta monic recurrence satisfies max_(1<=j<=n) beta_j / sum_(j=1)^n beta_j -> 0, without assuming a recurrence asymptotic.

Research / reproduction under the pre-existing SPECIALIZE assessment1933,
completed by source review1934. This records the unfinished argument before
further work. Main gap: actual-Xi all-degree positivity and C028b's
H_d=o(d); plausible use is diffuse-base control for C028w's two-site
shape problem. That transfer and all norm-weighted rates remain open.

Use L019/L021's full measure. Proposed chain, not yet certified here:

1. Compare K(|x|) globally with w_*=exp(-2Q_*), where
   Q_*=pi*(cosh(2x)-1)-(9/4)*log(cosh x). Bound the entire positive
   theta series relative to its first term, retaining its exponential
   prefactor. The comparison constants must be independent of degree.
2. With Q_0=2*pi*sinh(x)^2 and alpha=1-9/(16*pi), try
   alpha*Q_0<=Q_*<=Q_0 and alpha*Q_0'<=Q_*'<=Q_0' for x>0.
   Verify every Definition1.2(a)-(e) hypothesis, including both tails
   and the origin limits, rather than applying the theorem to theta.
3. Establish model MRS numbers a_n comparable to log(n+1).
   Source Theorem1.3 concerns W^2 with W=exp(-Q_*), and its A_n joins
   degrees n,n+1. Thus model beta_j=A_(j-1)^2; retain that shift.
4. Transfer both extremal monic squared norms separately, then divide.
   If actual beta_j is bounded above and below by fixed multiples of
   log(j+1)^2, sum over the upper half of the indices for the limit.

Continue only if this gives the exact zero limit. An unrepairable class
hypothesis or degree-dependent comparison stops this mechanism, not the
theta claim. No new source search or unassessed method is authorized.
The already inspected primary manuscript pp2-5 was reopened to verify
the notation and general-interval hypotheses; no new theorem is used.
No source theorem is reproved. C028o/p's earlier floors and ATTEMPTS1933
remain unchanged. No actual recurrence asymptotic, monotonicity, real
actual zeros, compact sites, or two-atom update asymptotic is assumed.

Completion1935: the chain was proved in canonical C028x. It gives
two-sided log(j+1)^2 bounds and max beta_j/sum beta_j<=8*B/(b*n).
The working obligations above record their pre-proof state; they are
not additional assumptions of the completed argument. See
[C028x](../lemmas/C028x-full-theta-recurrence-concentration.md) for the
full proof and citations. No mathematical script or numerical evidence
was needed. Independent audit remains pending, as recorded in PROGRESS.
