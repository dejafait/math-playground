# Full signed angular energy — exponential comparison attempt

Invocation-start target and coverage: the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`
covers the uniform angular Hankel bound at exponent 1/32. No new source
gate or source import is needed for a Fourier/residue attempt.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate test: retain the complete constant-input energy E_n and
test E_n >= c exp(-n/16) D_single,n, with uniform c and onset. The
anchor contribution to D_single,n is at least 64/21. Such a bound
would give the synthetic detector. Xi layer isolation, other poles,
census/clearance, simultaneous realization and matching upper bounds
and signs would still be independent gaps.

Essential inputs: C645g's normalization and H_q 1=q, and C645o's exact
energy identity. Retain n>=5, x=-5/4, R=11/8, eta=1/100, distinct common
poles Re(a)=x, |a|<=R-eta, x in Z, positive integer simple-pole residues,
sum r_a<=n/3, no separation or symmetry, and the conjugated angle in
the Blaschke denominator. No weighted-amplitude positivity is assumed.

Scoped checks: C645o's negative cross entry, C645n's full-inner-input
rate deficit, C645q's full signed energy, L646's exact-output stop and
L647's constant-grouping obstruction were inspected at their relevant
proof ranges. L647 is a contrast, not a lower-bound input. Its loss is
subexponential and its absolute energy grows, so it does not decide
the current test. Existing notebook changes are preserved.

Bounded mechanism under investigation: use angular analytic structure
and positivity of the original residues to control cancellation over
an angular region, rather than posit entrywise Gram positivity. Any
calculation must keep the full signed vector or a justified test of it.
Continue with a uniform proved bound, an admissible obstruction at the
specified exponential rate, or a quantitatively refined mechanism.
Finite screens and a relative o(1) construction do not settle the test.

This is an unfinished checkpoint. No exponential comparison has yet
been established, and no lemma is claimed at this point.

## Candidate reflection test (unfinished)

Let B_u^sharp(z)=conjugate(B_u(2*x-conjugate(z))). Its zeros
2*x-t_j/u lie outside the closed radius-R disk because 2*d-t_j>3/2>R.
Thus f_u(zeta)=1/B_u^sharp(R*zeta) is analytic there. On the common
pole line, B_u^sharp(a)=conjugate(B_u(a)). The finite-pole projection
identity from C645n would therefore give

    H_q f_u = B_u(x) sum_a r_a /[|B_u(a)|^2 (R*zeta-a)].

All displayed output weights are positive. In particular the first
spatial coefficient has modulus at least 1/(R |B_u(x)|). The remaining
question is quantitative: can the angular or best-angle norm cost
|B_u(x)| ||1/B_u^sharp(R*zeta)||_2 meet exp(n/32)? This is a different
test of the same approved detector, not a proof of the earlier proposed
comparison E_n >= c exp(-n/16) D_single,n. It uses no additional
theorem beyond the assessed finite rational projection and residue scope.
The full signed-energy comparison remains unresolved. A diagnostic
will compare the exact continuous product-rate expression with 1/32;
it is not a rigorous certificate or a detector counterexample.

## Completed bounded attempt

The reflected-input mechanism fails its discriminating test. The full
proof is canonical in [L648](../lemmas/L648-line-reflected-positive-input-rate-stop.md).
On the admissible anchor-only family its normalized complete output
is at most C sqrt(n) exp(-n/25), uniformly in u for n>=11, while
the actual operator is at least 8/sqrt(21). The exact radial lower
bound is 2125341605/52856645184>1/25>1/32; 12 constant checks passed.
The sampled continuum rate about 0.05282498 remains diagnostic only.

Outcome NEGATIVE stops this particular reflected positive-output
input. The original exponential comparison and the detector are
unresolved, and no off-line zeta zero or sign claim is supplied.
The next proposed mechanism uses mass-sensitive noncancellation;
its quantitative source and nonlinear-weight transfer are uncovered.
The new source assessment is REVIEW_REQUIRED, with no mathematical
approval or derived exponential-sum reduction. Its exact next action
and routing are recorded only in PROGRESS.md.

## Source-review update, 2 November 2026

The historical REVIEW_REQUIRED nomination above has now received its
bounded [source comparison](literature/2026-11-02-positive-mass-angular-propagation.md).
Biro's anchored pure-power theorem is relevant to integer mass, but an exact
full-weight transfer remains unproved. The review derives no representation
or lower bound. C645y's existing P'/P identity and initial-prefix stop must
be preserved in any later test. Current continuation metadata is solely in
PROGRESS.md; this note preserves the earlier unfinished reasoning.
