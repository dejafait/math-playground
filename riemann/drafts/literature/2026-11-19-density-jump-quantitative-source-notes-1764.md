# Quantitative density-jump source comparison1764

19 November 2026. Literature only; assessment1763's exact saved review.
Main gap: L030-L032/C032a actual-Xi all-degree positivity. The intermediate
aim is finite separation of C033i's mu from C033l's entire signed mass-one
TV<=2 width class. A certificate would quantify an existing range exclusion;
cancellation, moments, unrestricted variation and Xi realization stay open.

## Primary evidence actually read

**Gaver.** D. P. Gaver, Jr., *Observing Stochastic Processes, and
Approximate Transform Inversion*, Operations Research14(3) (1966),
444-459, DOI [10.1287/opre.14.3.444](https://doi.org/10.1287/opre.14.3.444).
Read reproduced original pp448-451, (13)-(29), in this
[university-hosted compilation](https://blasingame.engr.tamu.edu/z_zCourse_Archive/P620_09C/P620_09C_Lectures/P620_09C_Lec_05_Mod1_ML_05_LaplaceTrans.pdf).
For a>0, integer m>=1,n>=0, (13) is a normalized positive kernel;
(17)-(20) give its transform and exact cumulant sums. The approximate
mean/variance expressions are not exact bounds. Equation (23) gives
its distribution through binomial probabilities. Equations (24)-(26)
express kernel integration as a finite alternating sum of positive-argument
transform values, by binomial expansion. Read the concentration discussion
and opening Taylor case. Neither signed deconvolution nor a width-uniform
error bound is supplied. Continuity on an unbounded interval does not
itself imply boundedness, despite the wording after (29); any needed bound
must be proved independently. No extrapolation theorem is imported.

**Post-Widder comparison.** D. Belomestny, H. Mai and J. Schoenmakers,
*Generalized Post-Widder inversion formula with application to statistics*,
J. Math. Anal. Appl.455(1) (2017), 89-104,
DOI [10.1016/j.jmaa.2017.05.042](https://doi.org/10.1016/j.jmaa.2017.05.042),
[author manuscript, 16 May 2017](https://www.wias-berlin.de/people/schoenma/BelomestnyMaiSchoenmakers_16_05acc.pdf).
Read Definition2.1, Propositions2.2/2.3/2.5, pp2-3, and full proofs
Sections5.1-5.3, pp9-11. The rate assumes a locally Lipschitz probability
density and curve c with limsup c(y)^2/y finite; c=0 includes the real
axis. It gives O_x(N^(-1/2)), with unspecified constants/onset, using
transform derivatives. The kernel proof separates local regularity and
tails. This is not an explicit bound for atom-bearing signed remainders;
C033j continuity is weaker than its hypothesis. No direct rate application.

**Acceleration comparison.** A. Kuznetsov, *On the convergence of the
Gaver-Stehfest algorithm*, [arXiv:1305.0715v2](https://arxiv.org/pdf/1305.0715v2),
11 July 2013 arXiv label; served header 29 October 2018;
SIAM J. Numer. Anal.51(6) (2013), 2984-2998,
DOI [10.1137/13091974X](https://doi.org/10.1137/13091974X).
Read (1)-(6), pp2-3, and Theorem1/Corollary1, p4. For real locally
integrable functions with transforms at every positive argument, local
bounded variation or its Dini condition gives convergence without a rate.
Base Gaver kernels differ from accelerated sums. The full Theorem1 proof
was not read or imported. Its warning about growing alternating
acceleration coefficients prevents inferring convergence from base
convergence alone; no family-specific obstruction follows.

A. Kuznetsov and J. Miles, *On the rate of convergence of the
Gaver-Stehfest algorithm*, [arXiv:2005.05813v1](https://arxiv.org/pdf/2005.05813v1),
12 May 2020, manuscript dated 13 May 2020: Theorems1-2, p2, give
exponential convergence for local analyticity and o(n^(-floor((m-3)/2)))
for m>=5 derivatives. Read the statements and transform hypotheses;
proofs were not imported. Constants are unspecified and no width-uniform
bound follows from continuity. Acceleration is not the selected test.

**Heat input for the narrower prerequisite.** S. Sra, *On some positivity
properties of the Riemann Xi function*,
[2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Lemma2.1 and complete convergence proof p4; PropositionB.1 and complete
proof p17. Reused notes1740's j=0,1 coverage and inspected the fixed-j
counting/displacement proof for j=2: separate errors relative to Gaussian
main integrals are O(t^(-j)log(1/t)) and O(t^(1/2-j)log(1/t)).
These are not differentiated O remainders. Local Gaussian domination
permits fixed heat derivatives. Numerical constants/onsets are absent.
This covers ingredients, not a differentiated width-convolution bound.
Reuse notes1740's November-v1 Proposition3.1/C.1 Gaussian identity and
beta-integral/dominated-convergence tools under unchanged qualifications.
No source-wide preprint or zero-data verification is claimed.

## Comparison, obligations and discriminator

Read C033j's full proof/audit, C033l's hypotheses and finite-coordinate
assembly, C033o's support/application proof, C032s and notes1740/1748/
1756. C033j controls TV(R_sigma) and gives jointly continuous r_sigma
away from zero, retaining its zero atom. Its C_0,K_0,C_b are finite
without numerical effectivity. Lambda has a density jump at1; an
unspecified modulus does not specify finite separator data. C033l
gives qualitative existence; C033n rational stability is conditional
on finite data and a margin; C033o evaluates support for a given payoff.

The unaccelerated Gaver kernel is the selected finite-sample lead.
Adapting it remains mathematics: obtain uniform local density variation;
bound integration outside the local interval against the full signed
measure, retaining atoms; track inverse-transform multipliers and
coefficient-amplified evaluation errors. Kernel tail probability alone
does not bound integration against an arbitrary signed measure. C033j's
exact transform division is not a bounded inverse-convolution theorem.
No signed extension, error bound, finite data, margin or runtime is
derived here. Rational arguments still require C033n's error budget.

Full conversion stays parked until a usable uniform modulus is proved.
Assessment1764 separately nominates a spatial Lipschitz test on
[3/4,5/4], uniform over sigma in[1,2], for next-turn approval. Its
success threshold is an explicitly parameterized finite bound with
every constant labeled effective or existential. A result in unspecified
heat constants is partial regularity progress, not a numerical modulus.
Any differentiation of singular convolutions needs its own integrable
uniform majorant. Failure of that majorant parks this derivative route;
it does not refute continuity or finite separation. No derivation now.

## Search, duplicates and preserved failures

Queries: `Post Widder inversion formula convergence rate Lipschitz density
Belomestny Mai Schoenmakers theorem`; `Post Widder finite differences
Laplace inversion quantitative error signed measures density`;
`Kuznetsov Gaver Stehfest algorithm convergence theorem 1 bounded variation
pdf`; `Gaver 1966 observing stochastic processes approximate transform
inversion formula pdf`; `site.dlmf.nist.gov numerical differentiation
finite differences error`. Search hits were leads only. Mattner1993's
primary PDF timed out and remains uninspected; it is unnecessary for the
selected prerequisite. No essential access blocker remains. Additional
prerequisite queries were `"convolution exponential" "density" "derivative"
signed measures`; `"convolution powers" "weakly singular" derivatives beta`;
`compound poisson density local Lipschitz convolution singular density
derivatives`. Hits concerning estimation, local limits and asymptotics
of positive compound-Poisson densities are unread leads, not theorem
coverage for this signed continuum. The approved source ingredients
remain the directly inspected heat proof and reused beta/dominance tools;
no general compound-Poisson smoothness theorem is silently imported.

Scoped searches in the named November19 residual/signed/density reviews
and November18 width/dual stops found no quantitative modulus or Gaver
conversion. This is no originality claim. Read stops1571/1576 in full:
coarse independent boxes and literal common-disk evaluator costs remain
parked. Changing test construction does not erase their evidence or
authorize another dictionary solve. No mathematical script or lemma edit.

Decision: partial coverage supports SPECIALIZE for the narrower modulus
prerequisite; no ready quantitative-separator theorem was found.
Outcome EXPLORATION: source comparison plus a testable remaining
interface, no new bound or informative mathematical negative.
Full matching Mathlib coverage is unchecked and unknown.
Creative priority considered: this is established-route regularity,
without an independent central signed-height/Xi sign input; discovery1747's
parked batch is not relabeled creative.
