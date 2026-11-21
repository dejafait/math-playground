# First-odd two-width output sign: source comparison1562

18 November 2026. Literature only. Assessment1561's exact target is
retained. No coefficients, actual-law derivative signs, density, tail
expansion or new mathematical result are derived in this review.

## Local comparison and relevance

Read C032j, C032q's hypotheses/conclusion, complete C032u and C032l,
C032m's lift definitions and regularity input, C032s's endpoint statement
and source hypotheses, notes1551/1552, and stops1302/1551. Reuse the
audited finite-activity comparison and finite-mixture obstruction. The
bounded duplicate search covered positive-output/finite-Levy assessments,
smoothed/signed-law and odd-kernel ATTEMPTS. No exact sign decision for
this first-odd constraint was found in those paths; no archive-wide
absence or novelty claim is made.

Main gap: actual-Xi all-degree positivity, with continuum cancellation
and unsmoothed realization unpaid. The intermediate target asks whether
one odd constraint is compatible with positive output for widths 1,2.
A positive example could test a constrained building block; a negative
example would eliminate only this pair. C032l already excludes full
finite-family cancellation and any positive exponential moment. It does
not decide this weaker question. C032u supplies a sufficient range,
without optimality or the odd constraint.

## Primary statements and proof coverage

**Sharp domination.** Gilles Blanchard, Gyemin Lee and Clayton Scott,
*Semi-Supervised Novelty Detection*, JMLR **11** (2010), 2973-3009,
[Proposition 5, p2984; complete Appendix A.2, p3001](https://www.jmlr.org/papers/volume11/blanchard10a/blanchard10a.pdf).
For probabilities P0,PX on a measurable space, decompose
PX=f*P0+PX_perp relative to P0. The greatest removable proportion of
P0 is a=ess_inf_(P0) f=inf_(A:P0(A)>0) PX(A)/P0(A), attained.
The equal-law case has a=1. The proof retains the singular part,
constructs the residual at a, and uses sets avoiding the singular part
where f is near its essential infimum. No Lebesgue density is required.
Scott, *A Rate of Convergence for Mixture Proportion Estimation*,
[AISTATS2015, Proposition 2, p840](https://proceedings.mlr.press/v38/scott15.pdf),
was used only to locate this original proof. Statistical estimation,
irreducibility rates and sampling guarantees are not imported.

**Necessary transform signs.** Ante Mimica, *Laplace transform*,
Dresden course, 27 April-1 May 2015,
[Proposition 1.4(i)-(ii), pp6-7; Definition 2.3 and Theorem 2.4, pp14-16](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Read the complete proofs. For a positive half-line measure whose
transform L is finite at every s>0,
(-1)^n L^(n)(s)=integral x^n exp(-s*x) dmu(x)>=0.
The finite endpoint derivative criterion characterizes finite moments.
The proof uses exponential domination at s>0 and monotone convergence
at zero. Bernstein-Hausdorff-Widder characterizes such transforms by
complete monotonicity. Its proof retains the atom at zero, then handles
the unbounded case by exponential shifts. Only necessity is needed for
the proposed diagnostic; no signed-moment endpoint interchange is
licensed. Source typos in some auxiliary displays do not affect this
direct necessary derivative formula. Uniqueness coverage is reused
from notes1552, not freshly re-audited.

**Signed Tauberian conditions.** Martin Herdegen, Gechun Liang and Osian
Shelley, *A continuity theorem for generalised signed measures with an
application to Karamata's Tauberian theorem*,
[arXiv:2205.13075v2, 29 March 2023](https://arxiv.org/pdf/2205.13075v2),
Definitions 1.1/2.3, Theorem 3.2(a), Remark 3.3 and complete proof of
part (a), pp6-7. For x>0 write F_mu(x)=mu([0,x]); Psi_mu is its transform.
For a generalized signed Radon measure with all positive exponential
weights integrable against total variation, rho>=0 and nonzero
Psi_mu near zero, the Tauberian implication additionally requires

    liminf_(tau->0) |Psi_mu(tau)|/Psi_|mu|(tau)>0,
    limsup_(h->0+) limsup_(tau->0+)
      |F_mu((x+h)/tau)-F_mu(x/tau)|/|Psi_mu(tau)|=0 (x>0).

Together with Psi_mu(tau*lambda)/Psi_mu(tau)->lambda^(-rho), these
give F_mu(t)~Psi_mu(1/t)/Gamma(1+rho). The proof normalizes dilates;
the first condition bounds weighted variation, the second gives right
equicontinuity for the signed continuity theorem. This concerns
cumulative asymptotics, not positivity on arbitrary Borel sets. Part
(b) and the paper's full correctness are not imported or certified.

**Convolution expansions.** Philippe Barbe and William P. McCormick,
*Asymptotic expansions of convolutions of regularly varying
distributions*, J. Aust. Math. Soc. **78** (2005), 339-371,
[doi:10.1017/S1446788700008570](https://doi.org/10.1017/S1446788700008570),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6716AAB6A11ED687EA88826D5914B895/S1446788700008570a.pdf/asymptotic-expansions-of-convolutions-of-regularly-varying-distributions.pdf).
Read Section 2's asymptotic-smoothness definition, Theorems 2.2/2.5,
pp342-345, and Lemma 5.6 with proof and the complete Theorem 2.5
proof, pp368-370. Theorem 2.2 requires tail indices greater than one,
asymptotic smoothness, right-tail dominance and finite first moments
of the negative parts. Theorem 2.5 treats positive-half-line distributions with indices
below one, but still requires asymptotic smoothness. Its proof spends
that condition in the endpoint estimate and uses regular-variation
bounds. It supplies a convolution-tail expansion, not automatic sign
control of a signed linear mixture. The unverified higher-order
convolution algebra is not imported.

## Applicability, stopping test and next scope

The domination theorem applies to either ordered pair of C032j's Borel
probabilities, without a density. It leaves the actual essential-infimum
inequality entirely to be established. Once coefficients are determined,
the required comparison is the positive coefficient times its probability
minus the magnitude of the negative coefficient times its probability,
on every Borel set. No coefficient or comparison direction is determined
here. C032u must not be called sharp merely because its zero-jump
factor is exact. Neither a stochastic-order bound nor a tail-probability
ratio on its own proves this all-Borel inequality.

The two tail sources provide no immediate shortcut. The actual
post-cancellation remainder has not been supplied with the signed
variation/right-equicontinuity conditions above, or with the asymptotic
smoothness and controlled remainder required by a convolution expansion.
Applying a first-order equivalent separately and then subtracting it
does not settle that missing remainder. The signed theorem applied
directly to a mass-one finite law would concern its cumulative mass;
it would not by itself isolate its first cancelled tail. Even a proved
eventual tail sign would leave arbitrary bounded Borel sets unresolved.
Park automatic tail-sign and optimal-domination imports. This is a
source-scope limitation, not proof of a negative output or impossibility
of obtaining the missing estimates by another mechanism.

Mimica's necessary derivative formula has no missing density hypothesis
if the proposed output is assumed positive for contradiction. C032q
already defines the signed output and its bounded Laplace integrals;
C032m supplies entire lifts and controlled complex differentiation.
These are ready inputs for a bounded local test of derivative orders one
and two, using the Taylor series of the entire lift, with its analytic
remainder controlled before changing variables s=w^2. No tail inversion
or differentiation of an arbitrary real big-O error is authorized.

The next mathematical attempt must determine whether the two linear
constraints even specify a unique law, then test those two derivative
signs for sufficiently small positive s. A certified violation disproves
positivity for that law only. If both necessary tests pass, or their
actual constants cannot be controlled, stop this diagnostic as
inconclusive. Do not automatically add widths, raise derivative order,
claim all-Borel positivity or reopen full finite cancellation. That test
and its ready assessment are prospective; no part is executed here.

Retain C032j's actual divisor/multiplicity, zero-ordinate exclusion,
strip/counting, verification through100, first-zero/tail, heat and
fixed-v1 qualifications. No RH, profile positivity, law density,
exponential moments, full J_eta=0 or Xi realization is added. No concrete
central creative mechanism is justified by these criteria: a continuum
witness or controlled approximation to -1 in C032q's cone is still
absent. This local diagnostic is a known-theorem specialization.

## Search/access and coverage limits

Queries: signed mixtures cancelling leading regularly varying tails;
Barbe McCormick asymptotic convolution expansions; Bernstein functions
complete monotonicity; mixture proportion essential-infimum criterion;
Blanchard Lee Scott2010 original proof. Primary statements/proof ranges
above, rather than snippets, support the comparison. A nonexistent v3
HTML URL failed; v2 PDF supplied the signed theorem. Australian-society
fetches timed out; the publisher PDF supplied the selected proof cases.
There is no persistent essential access blocker. Generalized signed
measure definitions were read; no distribution-specific application of
that theorem was made. No absence of a matching result beyond this
bounded search is claimed. Full matching Mathlib coverage remains
unchecked and unknown. No lemma or mathematical script was written.
