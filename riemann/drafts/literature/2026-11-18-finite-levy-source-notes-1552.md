# Finite Levy-difference source comparison1552

18 November 2026. Literature only. No difference estimate, convolution
comparison for the actual laws, or signed positive output is proved here.

## Inspected primary coverage

Jean Bertoin, *Subordinators, Levy processes with no negative jumps, and
branching processes*, Maphysto 2000 course,
[fixed course PDF](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
Read Section1.1 pp3-4 (Poisson counts and exponential formula), Theorem1.2
pp7-8 with its full converse construction, and Proposition1.3 and the
finite-activity discussion p9. The representation requires a positive
measure Pi on (0,infinity) with integral min(1,t) dPi finite, and
nonnegative killing and drift. The converse constructs the jump sum;
the exponential formula identifies its transform. With zero drift/killing
and finite intensity M, the jump count at time one is Poisson(M), hence
the zero-jump probability is exp(-M). The finite-activity case is explicitly
included here; the source excludes it only in subsequent sections.
This supplies a possible atom of a comparison factor, not a zero atom
of either original law. Measure domination and a signed coefficient range
for the actual pair still require a specialization; no general stochastic
ordering theorem is being substituted for domination on every Borel set.

Steven P. Lalley, *Levy processes, stable processes, and subordinators*,
[author course PDF](https://galton.uchicago.edu/~lalley/Courses/385/LevyProcesses.pdf),
undated version accessed today, Definition5.1 and (5.2)-(5.4), p12.
Read the definition and complete conditioning argument: jumps are iid,
independent of a Poisson count, and conditional on n jumps the sum has
the n-fold convolution of the jump law. This is supplementary coverage
of the finite-activity case, not a claim about the actual heat kernel.

Ante Mimica, *Laplace transform*, Dresden course, 27 April-1 May 2015,
[author PDF](https://web.math.pmf.unizg.hr/~amimica/lt.pdf),
Proposition1.4(iv) and proof pp6-7, Proposition1.8 and proof pp9-10.
The first identifies the transform of convolution for positive half-line
measures; the second gives uniqueness for finite measures. Prior notes1539
covered the uniqueness statement; the inversion proof was now inspected.
It uses Poisson kernels, off-diagonal concentration, and dominated
convergence at positive continuity points, sufficient for uniqueness.
Do not import the displayed inversion formula at x=0 without qualification:
its half-atom expression requires separate endpoint treatment. Also the
proof's first display prints lambda in place of n and its final display
omits a summation. The standard uniqueness conclusion for finite positive
measures, not these typos, is the intended import. No signed inversion or
moment assumptions are needed for that conclusion.

Suvrit Sra, *Some positivity properties of Riemann Xi under smoothing*,
[2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1).
Read Proposition3.1 pp5-6 and its entire proof in C.1/p21; A.7's
hypotheses pp16-17 and full proof p17; Theorem4.1/proof p9.
The Gaussian has variance 2sigma. The exact transformation is
H_sigma(t)=H(t/(1+4sigma*t))/sqrt(1+4sigma*t), ell_sigma=H_sigma/t.
The proof controls the complex-zero summands absolutely before exchange.
A.7 identifies the nonnegative Levy density when H_sigma>=0, with no
killing or drift. Theorem4.1's proof gives ell_sigma(t) asymptotic to
sqrt(pi)*p_sigma(0)*t^(-3/2) at infinity, with p_sigma(0)>0.
The width-persistence statements in Section3.1 and C.1 concern positivity
of profiles/cumulatives and do not assert ordering of H_2-H_1. Individual
Levy integrability is weaker than finite total mass of a difference.

Sra, *On some positivity properties of the Riemann Xi function*,
[2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
PropositionB.1 and complete proof, p17. Read (B.2), (B.3), counting-error,
complex-displacement and large-time cases. It gives
H(t)=[log(1/t)-gamma_E-2log(4pi)]/(8sqrt(pi*t))+O(log(1/t))
and fixed-j derivative equivalents
(-1)^j H^(j)(t) ~ Gamma(j+1/2)/(8pi)*t^(-j-1/2)*log(1/t)
at zero. Its proof bounds counting and complex-displacement errors
separately. The large-time expansion isolates the first real zero using
verification through 100, the strip and counting inputs. These retain
C032j's source qualifications. Leading equivalents alone do not justify
subtracting cancelling terms at two nearby transformed times; the
research step must control that subtraction rather than differentiate
an unqualified big-O remainder.

## Applicability comparison and unpaid work

Use precisely C032j's actual divisor, multiplicity, heat and fixed-v1
qualifications, and C032m/q's width interval and signed-kernel interface.
No assumption of RH, realness of every zero, density of nu_sigma,
positivity of p_sigma, finite exponential moments or eta>=0 is licensed.
The proposed independent test is the density difference
D(t)=ell_2(t)-ell_1(t), or its negative. Its nonnegativity for all t>0
and finite integral are desired conclusions, not imported premises.
The source formulas permit a bounded analytic attempt. At infinity the
individual tails are covered; at zero a cancellation estimate remains
unproved. Neither sign direction is decided by this review.

If a nonzero finite positive difference is established later, the
research may specialize the cited jump law, convolution and uniqueness
theorems and check the resulting domination and permissible signed
coefficient range explicitly. No such specialization is performed now.
M=0 must be treated separately. A sign failure or divergent mass stops
that direction only; neither decides C032q's entire output-positive cone.

Stop1302 (C032l) excludes finite signed mass-one combinations satisfying
the stronger full cancellation/exponential-moment requirement. This test
imposes neither; it therefore does not reopen the stopped route or
promise all-degree positivity. Stop508 concerns a different actual-Xi
Mellin/Bernstein sufficient class. Existing identifiability/certificate
mismatches1551 and PDE/compact-transform stops remain intact.

## Search and access record

Narrow local searches: C032j/m/q and finite-Levy nominations; notes1551;
ATTEMPTS signed/smoothed and Levy filenames. Reused notes1539 and the
finite-law stop1302, without reading unrelated proofs.
Queries: `finite Levy measure difference compound Poisson convolution
domination zero atom subordinators`; `"Sra" "smoothing" "Levy" "difference"`;
`"Riemann" "heat sum" "monotonicity" smoothing`;
`"compound Poisson" "domination" "Levy" measure zero`.
No inspected theorem states the actual ordered difference result.
Search results about convex/stochastic ordering and unrelated reflecting
processes were not used; their proofs were not inspected. No novelty
claim follows. Bertoin's source and both fixed-v1 PDFs were read via web
text. Shell downloads failed DNS; a screenshot timeout did not block the
subsequently retrieved complete relevant proof text. No API keys used.

Full matching Mathlib coverage was not checked and remains unknown.
The literature-only outcome prepares a test; it establishes no new
mathematical result and no conclusion beyond the inspected sources.
