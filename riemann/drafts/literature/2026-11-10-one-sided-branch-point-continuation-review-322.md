# One-sided branch continuation to the selected-parameter point — source assessment

TARGET: Assess source coverage for bounding C997c's value H_n^+(1+i/8;mu) by C*exp(-kappa*n)*||mu||_TV plus a subexponential multiple of its sup norm on [15/8,17/8], uniformly over finite complex slope measures.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step323 searched quantitative analytic continuation, Hardy upper-half-plane boundary extrapolation, exponential-type finite-interval stability and Laguerre/Fourier stability; inspected primary contracts and proof cases listed below and reused reviews312/318/320. No adequate exact-range theorem was found; no novelty inference.
SOURCE_EVIDENCE: Grabovsky–Hovsepyan CPAM74(2021), Theorem2.7/(2.20)-(2.22) pp149-150 and Section5 pp162-168; Trefethen BIT60(2020), Lemma2.1 p904 and Theorem5.2/proof p908; Demanet–Townsend MIT author manuscript, setup pp1-2, Theorem2 pp3-4 and Section6.3-6.4 pp20-22. C997c(1),(4)-(6) and audit322 provide the exact local range, not the proposed continuation.
COMPARISON: Primary continuation bounds require global Hardy or domain norms and give conditional power-law stability. They neither import the requested fixed-kappa/every-epsilon additive estimate nor exclude it on this structured slope range. Whole-class worst cases are not realized slope measures. Local recovery remains an audited input, not continuation.
GAP: Pay a global norm in original slope TV, retain the complete positive-frequency range and evaluate the resulting all-n rates at the specified point; alternatively realize a rate obstruction in that exact range. The inspected generic estimates alone do not decide this.
REASON: Essential source coverage is sufficient for one bounded mathematical test, but no new estimate or impossibility theorem was derived. A separate ready continuation assessment323 nominates that test for approval next turn; this completed source review is EXPLORATION/NOVELTY_UNCHECKED.
LITERATURE_REASON: The newly nominated off-window complex evaluation is not covered by the ready local branch audit; quantitative one-sided continuation contracts and their norm hypotheses require a separate source comparison.
SCOPE: Completed literature-only comparison of the exact point estimate below; no derivation, new filter, slope inversion, selected-response identity, rate claim or actual-Xi transfer was performed. Mathematical scope is limited to the separate assessment323.

## Exact proposed estimate

Keep C997c's complete finite integral (1), with n>=2 an integer,
I=[7/4,9/4], Gamma_in=[15/8,17/8], and every finite complex Borel
measure mu on I. Write V=||mu||_TV and use the same finite integral
at z_star=1+i/8. No unknown-zero realization is assumed.

The proposed test is whether fixed C<infinity and kappa>0 exist such
that for EVERY epsilon>0 there are finite C_epsilon and N_epsilon with

    |H_n^+(z_star;mu)| <= C*exp(-kappa*n)*V
          +C_epsilon*exp(epsilon*n)
                         *sup_(gamma in Gamma_in)|H_n^+(gamma;mu)|

for all integers n>=N_epsilon and every such mu. Constants may depend
on the stated fixed intervals and kernel, but not on n or mu. The
same fixed kappa and C must work for every epsilon. This is a proposed
inequality, not a claimed result or a consequence already derived here.

The imaginary displacement 1/8 is the difference between the competitor
cosh parameter 3/8 and the selected parameter 1/4 in C997a. It motivates
one concrete point to test, but no identity between this branch value
and C997a's full selected response is assumed. Both signs and the
remaining beta-reflected contributions would still require separate
justification before selected normalization. The lower interval and
K's -1 remain in this target, as does arbitrary complex mu.

## Relevance and continuation test

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing, with L984(H) unpaid. The audited C997c supplies local branch
information. A paid continuation estimate could make that information
useful for a later selected-response test. It would not itself solve
the original simultaneous suppression and subexponential slope-TV
assay, construct any slope measure, or establish positivity.

Reuse the ready source assessments for binomial/Fourier/measure tools;
do not repeat their discovery. Compare primary quantitative analytic
continuation and one-sided Fourier/Laplace estimates with the specified
structured range, complex measures, closed data band and nonreal target
point. Inspect hypotheses and load-bearing proof cases before deciding
whether import, specialization, bounded exploration or a source block
is appropriate. Identify any required global norm and pay its relation
to original slope TV. Counterexamples for arbitrary unrelated spectral
measures do not automatically occur in this range.

Continue to a separately approved mathematical attempt only with
adequate coverage for this exact inequality or an exact-range obstruction
test. A successful rate must have fixed kappa>0 and subexponential
amplification in the quantifier sense above. If a certificate retains
an unpaid positive exponential amplification rate, record that precise
limitation; do not call it an impossibility theorem for every operator.

Compare stops293/316/317 and trials314/315/318 without weakening them.
The new input is C997c's audited local positive branch; the proposed
test is one nonreal point of that same branch. It is not a repetition
of the full-quartet whole-boundary truncation or an equidistant dual fit.
No new continuation identity or mathematical estimate was attempted
in step322. This nomination receives its own review next turn.

Essential inputs: L997(4), C997a(1)-(2), C997c and its step322 audit.
Unresolved independently: selected normalization and both-sign transfer,
original slope-assay feasibility, actual reconstruction, signed recovery,
infinite-zero complements, regulator uniformity, L993 and L984(H).
Mathlib matching coverage is unchecked and unknown. No cross-notebook
input, RH candidate or novelty claim is proposed.

## Completed source review — step323, 10 November 2026

The TARGET is unchanged. The preceding nomination records the pre-review
state. This section completes one literature-only comparison; it does not
derive a specialization, test a mathematical construction, or settle the
displayed inequality. No lemmas or mathematical scripts were changed.

### Primary theorem contracts actually inspected

**Upper-half-plane boundary continuation.** Y. Grabovsky and N. Hovsepyan,
*Optimal error estimates for analytic continuation in the upper half-plane*,
Communications on Pure and Applied Mathematics 74 (2021), 140–170,
[author-hosted published text](https://sites.temple.edu/yury/files/2023/06/general_curve.pdf),
Theorem2.7, pp149–150. For complex f in H2(H+), with global H2 norm
at most one and L2(-1,1) norm at most delta in (0,1),

    |f(z)| <= rho(z)*delta^gamma(z), z=x+i*y, y>0,
    gamma(z)=-arg((z+1)/(z-1))/pi in (0,1),
    rho(z)^(-2)=(y/9)*(arctan((x+1)/y)-arctan((x-1)/y)).

Here ||f||_H2=sup_(v>0)||f(.+iv)||_L2(R); arg is principal. Sharpness is up to constants
independent of delta, in the unrestricted Hardy class. Inspected Section5,
pp162–168: strict/non-strict data constraints, boundary L2 convergence,
uniformly bounded resolvents, truncated-Hilbert spectral solution and the
explicit extremizer's global/data norms. This is not an operator on our
slope measures. Its extremizer has not been realized by C997c. H2 membership,
the global norm cost, affine change of interval and conversion from local
sup data must be justified before application. No such specialization was
derived. The interior theorem's conjectured spectral asymptotics are not used.

**Bounded-domain propagation.** L. N. Trefethen,
*Quantifying the ill-conditioning of analytic continuation*, BIT Numerical
Mathematics 60 (2020), 901–915,
[author-hosted published text](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf),
Lemma2.1 p904 and Theorem5.2/proof p908. The latter assumes a connected
open domain, a bounded nonempty continuum whose closure encloses no
remaining domain points, piecewise smooth data boundary, analyticity
through that set, and global sup norm at most one. Data bound delta gives
|g(z)|<=delta^alpha for a geometry-dependent alpha in (0,1).
Read the bounded-strip Phragmen–Lindelof argument and the connecting-arc
conformal reduction. This supports conditional propagation, not a paid
global norm or the required additive rates. Neither unrestricted Runge
examples nor the paper's general no-Lipschitz discussion is imported as
an obstruction on our range.

**Polynomial extrapolation comparator.** L. Demanet and A. Townsend,
*Stable extrapolation of analytic functions*,
[MIT author manuscript](https://math.mit.edu/icg/papers/stable-extrapolation.pdf),
31-page unversioned copy accessed 10 November2026; setup pp1–2,
Theorem2 pp3–4, Section6.3–6.4 pp20–22. For a complex function bounded
by Q in a Bernstein ellipse E_rho, rho>1, the theorem treats N+1 equally
spaced samples with errors <=delta and a REAL target
1<=x<(rho+rho^(-1))/2. Oversampling requires
log(Q/delta)/log(rho)<sqrt(N)/2. It gives a fractional-power error,
up to polylogarithmic factors, with exponent
-log((x+sqrt(x^2-1))/rho)/log(rho); the undersampled case is separate.
Read both cases and the Chebyshev-tail lower construction in Proposition3.
The real-target and ellipse-norm hypotheses do not directly cover our
nonreal point. No extension of this theorem or its minimax lower bound
is assumed. It is a comparator, not an input to an asserted estimate.

### Exact-range comparison and reuse

C997c(4)–(6) already identify H_n^+ as H_U+H_L, Fourier transforms of
finite complex measures on two positive compact t intervals, and pay
their spectral TV in the original V. Those facts are reused; no new
Hardy norm, demodulated norm or complex-point bound is calculated here.
An arbitrary finite Fourier measure is not automatically an L2 density.
If a later use of H2 relies on the particular densities in (4), that
property and its quantitative norm must be checked for every finite
complex slope measure, including endpoint atoms. Plancherel may be
imported in its standard named form; it does not remove this verification.

The source norm is global. A bound in terms of ||H_n^+||_H2 or a domain
supremum cannot be silently relabeled a bound in V. In particular the
upper-band TV bound in C997c(5) contains exp(9n/32); it is an available
upper bound, not a lower bound and not a proof of instability. A
fractional-power data estimate is not already the requested additive
inequality with one fixed kappa for every positive epsilon. Any conversion
has to account for all constants and quantifiers. No rate conversion has
been attempted in this review.

The positive branch and nonreal point are material changes from trial318.
Reuse review312 for its inspected Kovrijkine lemma, named Hahn–Banach
and measure representation tools, and the original assay. Reuse
review318 for its sampling/sign-approximation scope comparisons, and
review320 plus C997c's audit322 for local recovery. Additional browsing
of those unchanged tools was unnecessary. No new selected-response
identity is inferred: C997a(8)'s extra term and both-sign transfer remain
independent obligations.

Read stops293/316 and audit317, plus trials314/315/318. The fixed bump's
endpoint leakage and prescribed Chebyshev normalization cost are audited
subclass obstructions. Equidistant dual interpolation and full-quartet
whole-boundary truncation missed their displayed rate thresholds; they
are not all-measure impossibility results. The present point question
uses the newly audited positive branch and is independently testable.
It does not erase those stops, reset exploration counters or authorize
repeating their failed certificates.

### Search and access record

Queries: `Trefethen Quantifying ill-conditioning analytic continuation
theorem strip 2020 pdf`; `Grabovsky Hovsepyan analytic continuation upper
half plane Hardy space optimal error estimates theorem`; `Demanet
Townsend stable extrapolation analytic functions theorem pdf`;
`"one-sided" "analytic continuation" "exponential type" interval stability`;
`"Laguerre" "analytic continuation" "stability" Fourier measure`;
`bandlimited analytic continuation upper half plane finite interval sharp
error compact spectral support`. The bounded search established no
matching theorem or exact-range obstruction. This is not evidence of
novelty. NIST's Dienstfrey–Greengard finite-interval continuation paper,
the RKHS companion paper arXiv:1907.13325, and older Carleman references
are unread leads; no claim from them is used or needed for the bounded
test nominated here.

The initial faculty.cst.temple.edu PDF endpoint timed out. Both the
arXiv v2 and the author-hosted published copy were accessible. This is
not a persistent source blocker. Primary extracted text, including
theorems and relevant proof cases, was read; no screenshot inspection
or independent audit of those publications is claimed. Notebook-local
search output was initially too broad and truncated; it was used only
to locate exact paths. The named canonical definitions, proof ranges,
source assessments and stop files above were then read directly. No
conclusion relies on that truncated search output.

### Decision

EXPLORE: adequate coverage for one bounded upper-half-plane continuation
attempt on the exact inequality, without a claim that it is true or
false. Missing quantitative specialization is mathematical work, not an
essential inaccessible theorem. The separate assessment
[continuation323](2026-11-10-one-sided-point-paid-continuation-test-323.md)
specifies the single proposed test. It receives separate approval next
turn before invocation; this completed source review remains valid.

No new lemma, rate, counterexample, selected-response implication or RH
result was established. Full matching Mathlib coverage is unchecked
and unknown; no availability or absence is inferred. Actual-Xi positivity,
signed recovery, original slope-assay feasibility, actual reconstruction,
infinite-zero complements, regulator uniformity, L993 and L984(H) remain
unpaid. PROOF.md and DAG.md are unchanged because no argument or
mathematical input was added to their assembly.
