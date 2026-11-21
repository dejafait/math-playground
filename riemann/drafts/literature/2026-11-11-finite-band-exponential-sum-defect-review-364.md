# Finite-band exponential sums with a controlled defect — completed source comparison

TARGET: Assess source coverage for equispaced finite-band exponential sums with O(n) atoms satisfying C997q's exp(-n/64) weighted defect and boundary bounds at subexponential original TV.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step365 searched quantitative superoscillation, equispaced exponential sums, coefficient variation and minimum-energy/periodic constructions; read the four primary contracts and relevant proof cases below. No matching simultaneous original-TV/weighted-error theorem was established; no novelty inference.
SOURCE_EVIDENCE: Aharonov et al. arXiv:1511.01938v1 Proposition3.1.7/Theorem3.1.8 and proof(3.3); Karmakar–Jordan arXiv:2306.03963v1 SectionIII.1(24)-(29); Ferreira–Kempf IEEE TSP54(2006) Theorem2 pp3736-3738; Tang–Garg–Kempf arXiv:1512.00109v1 Section4(26)-(52), including both propositions and the explicit conjecture qualification. Local inputs remain C997c and unaudited C997q.
COMPARISON: Known finite-sum least squares and periodic minimum-coefficient-l2 interpolation cover construction tools, not simultaneous moving-window weighted defect/boundary rates at subexponential original l1. Real-line finite-energy interpolation does not directly cover atomic measures; its worst-direction energy upper bound is not an all-data lower bound. The inspected periodic asymptotic is conjectural.
GAP: For ONE fixed equispaced O(n)-atom family, establish both complete C997q weighted estimates and original coefficient-l1 cost, or a rigorous obstruction within that family. Existing normal equations, fixed-compact convergence, numerical fits and condition numbers do not settle these thresholds.
REASON: Essential source access/comparison is now adequate for one bounded mathematical test, with no new construction, specialization or bound derived in this literature-only step. A separately nominated continuation receives approval next turn before research; no further browsing is needed merely to repeat this comparison.
LITERATURE_REASON: Changed ansatz and specific new source lead: quantitative finite-band superoscillation/exponential-sum approximation with coefficient variation control, rather than exact moving-window or diagonal-zero inversion.

## Step364 nomination, preserved with its original mathematical target

Keep integer n>=2, I=[7/4,9/4], E=[15/8,17/8], z_star=1+i/8,
and the complete C997c kernel. The proposed later family has distinct
equispaced frequencies gamma_(j,n)=15/8+j/(4m_n), 0<=j<=m_n,
where m_n=ceil(kappa*n) for one fixed kappa>0. Complex coefficients
are to be chosen. No coefficients, permissible kappa, construction,
asymptotic or lower bound have been derived or approved in this turn.

The source question is whether known results produce or obstruct ONE
such family of finite measures lambda_n, with original TV measured by
the sum of the absolute coefficients, satisfying

    ||lambda_n||_TV <= C_epsilon exp(epsilon*n) for every epsilon>0,
    exp(-a/4)|Delta_n| <= C_B exp(-n/64),
    sup_(x in [a,b]) exp(-x/4)|D_n(x)| <= C_D exp(-n/64).

Here a=7n/4, b=9n/4, D_n and Delta_n are the COMPLETE expressions in
C997q. Constants must be independent of n. The two latter conditions
are sufficient for the original slope residual by C997q(2), whose
unaudited proof must be checked before relying on it. They are not
claimed necessary, so an obstruction to this stronger criterion has
only that scope. A mere approximation on a fixed time interval, an
unweighted L2 estimate, a coefficient norm without a TV conversion,
or an uncontrolled number/spacing of frequencies does not settle it.

First inspect primary theorem hypotheses and the proof cases governing
degree, window length, absolute error and coefficient cost. Compare the
target with review322's already-inspected ambient continuation bounds
and C997j/k's restricted dual records; do not rederive them. The stopped
C997i/m/p packet families are not reopened. Retain the original g_n,
its zeros and the lower window. This review may approve a bounded test
or expose a scoped obstruction; it must not derive new lemmas or run
mathematical scripts while coverage is missing.

The intended downstream use remains the positive-branch point bridge
for signed slope selection. C997a(8), selected/both-sign transfer,
original assay and reconstruction, recovery/complements/regulators,
L993 and L984(H), and L030–L032/C032a actual-Xi positivity and
L966/L968 forcing remain open. No cross-notebook input. Mathlib full
matching coverage is unchecked/unknown. No candidate solution of RH.

## Completed comparison — step365, 11 November 2026

The section above preserves the step364 nomination and its then-missing
coverage. This section completes that comparison. The TARGET is unchanged.
No coefficients, new bounds, lemma, mathematical script or specialized
normal equation was derived in this LITERATURE-only turn.

### Primary statements and relevant proof cases actually read

**Fixed-compact binomial sequence.** Y. Aharonov, F. Colombo, I. Sabadini,
D. C. Struppa and J. Tollaksen, *The mathematics of superoscillations*,
[arXiv:1511.01938v1](https://arxiv.org/html/1511.01938), 5 November 2015,
Section3.1, Proposition3.1.7 and Theorem3.1.8 with proof(3.3)-(3.4).
For fixed real a>1, the sequence

    F_m(x,a)=(cos(x/m)+i*a*sin(x/m))^m

has m+1 equispaced real frequencies in [-1,1], with explicit binomial
coefficients in Proposition3.1.7(2), and converges uniformly to exp(i*a*x)
on each fixed [-M,M]. Read the modulus/phase error identity and the
proof's restriction m>2M/pi. This does not give a moving M=O(m)
error estimate. The theorem assumes real a, whereas our nonreal target
also has damping. Its coefficient formula is not a paid original-TV
estimate for our target. No complex-parameter extension, moving-window
specialization or coefficient-cost calculation was performed. A direct
import therefore does not settle the proposed pair of weighted bounds.

**Finite-sum least squares.** T. Karmakar and A. N. Jordan,
*Beyond superoscillation: General theory of approximation with bandlimited
functions*, [arXiv:2306.03963v1](https://arxiv.org/html/2306.03963),
identifier dated 6 June 2023; HTML header also displays 24 August 2026.
Record this version as served, not an assumed later revision.
Read SectionIII.1(24)-(29), including the normal-equation derivation
and ill-conditioned/pseudoinverse case. Equations(28)-(29) treat a finite
sum with frequencies (1-2j/N)*2pi and minimize squared integral error on
a finite interval. Their matrix has an explicit sinc/exponential entry;
the right side depends on the target. This directly overlaps finite
equispaced approximation tools. It provides no original coefficient-l1
bound, uniform weighted-defect bound, boundary condition, or all-N rate
for our oscillatory kernel. Equations(24)-(27) instead use spherical
Bessel functions; they must not be relabeled atomic band measures.
An unquantified pseudoinverse and its finite numerical figures are not
the requested cost/error certificate. No specialization was derived.

**Real-line energy and interpolation.** P. J. S. G. Ferreira and A. Kempf,
*Superoscillations: Faster Than the Nyquist Rate*, IEEE Transactions on
Signal Processing54(10) (2006), 3732-3740,
[author-hosted published PDF](https://sweet.ua.pt/pjf/PDF/Ferreira2006a.pdf),
DOI10.1109/TSP.2006.877642. Read SectionIII pp3736-3737 and
SectionIV/Theorem2 pp3737-3738, including the least-energy sinc
interpolant and the equality case. For finite-energy functions with a
fixed real bandlimit, prescribed real amplitudes at distinct real times
have a minimum-energy interpolant. Its energy is a quadratic form in
the inverse sinc Gram matrix, bounded ABOVE by squared data norm divided
by its smallest eigenvalue. Equality requires the corresponding data
direction. The paragraph immediately after Theorem2 explicitly warns
that this is an upper bound, not a lower bound. The small-spacing
asymptotic is not imported as a uniform growing-dimension estimate.
Our atomic exponential sums are not automatically in this real-line
L2 class; the paper does not pay their original measure variation or
our defect/boundary functionals. Thus its energy discussion cannot be
used as an all-measure impossibility theorem here.

**Periodic coefficient norms.** E. Tang, L. Garg and A. Kempf,
*Scaling Properties of Superoscillations and the Extension to Periodic
Signals*, [arXiv:1512.00109v1](https://arxiv.org/html/1512.00109v1),
1 December 2015; subsequently J. Phys. A49(2016), 335202,
DOI10.1088/1751-8113/49/33/335202. Read Section4(26)-(52), both
unnumbered propositions, their Vandermonde/pseudoinverse proofs, the
N<=2M+1 versus overdetermined cases, and the final numerical qualification.
For 2pi-periodic trigonometric polynomials with modes -M,...,M,
equations(30)-(32) give normalized period energy equal to coefficient
l2 squared and minimum-coefficient-norm interpolation by T^+a.
Require distinct PHASE nodes exp(i*t_k) in the Vandermonde argument;
distinct real t_k alone does not rule out periodic coincidences.
Equations(46)-(47) give the inverse-Gram quadratic form and a
worst-direction energy upper bound. The proposed eigenvalue asymptotic
(50)-(52) is explicitly called conjectural at the end of Section4.
It is neither a proved growing-dimension rate nor our data-direction
lower bound. Original coefficient l1 still requires a justified norm
conversion and rate control; the complete weighted constraints are
not ordinary point interpolation. No periodic specialization is asserted.

### Comparison at the actual thresholds

Source tools cover finite-dimensional approximation and coefficient
norm minimization. The unresolved work is their quantitative use for
the SAME original measure on E, both complete functionals, and every
large integer n. No inspected theorem supplies this combination.
No existence or impossibility conclusion is drawn from that gap.

The original windows move with n and retain a separate lower-window
boundary. A theorem about approximating exp(i*z_star*t) itself is not
automatically a theorem about D and Delta: g_n, endpoint dilation,
the weights and boundary must be accounted for. We did not choose or
derive a new approximation objective during this source review.
Likewise a generic energy cost, condition number or least singular
value does not decide this structured target's cost without its actual
direction and norm relation. Fixed-window convergence and a finite
fit alone are inconclusive. Both inequalities remain sufficient, not
necessary, for the original point-residual question.

Read the full relevant C997q identities and proof, and C997c definitions,
spectral measures and variation bounds. C997q remains UNAUDITED: reading
it for scope is not a critical audit. Check its (1)-(2) against C997c
before relying on the sufficient implication in a later attempt.
No independent full proof of a primary theorem is attempted or needed
in this source-only comparison. Mathlib full matching coverage remains
unchecked/unknown; no formal theorem identifier or absence is claimed.

### Local overlap and preserved failures

Reused review322's completed primary continuation comparison; no new
ambient continuation search is needed. Read C997j/k's hypotheses and
conclusions: scalar Gram damping and a target spectral cutoff leave
their own costs/tails open and do not decide finite atomic defect
approximation. Read stops314/315 and364. Earlier equidistant full-quartet
dual interpolation missed its certified rate, so another uncertified
fit is not a new mechanism. The proposed test instead uses the
positive branch and explicit weighted nonzero defect; it must produce
new uniform evidence. C997i/m/p's recorded scoped stops remain intact.
No source estimate or packet mechanism is silently reopened, and no
historical stop is broadened to a ban on general finite band measures.

### Search and access evidence

Queries included: `superoscillations exponential sums coefficient cost
approximation interval length quantitative theorem`; `superoscillations
equispaced frequencies binomial coefficients uniform convergence
expanding intervals`; `superoscillations minimum energy exponential
number oscillations Ferreira Kempf 2006 pdf`; `superoscillating
trigonometric polynomials coefficient l1 lower bound interval
approximation exponential`; `"finite exponential sums" "total variation"
superoscillation approximation`; `"superoscillations" "coefficient"
"norm" lower bounds interval`; `"superoscillations" "Laguerre"
approximation`; `"Scaling Properties of Superoscillations" periodic
signals arxiv`. Only the primary sources above support the comparison.
No exact match was established; this is not a novelty finding.

The Karmakar–Jordan /html/2306.03963v2 URL returned404; the unversioned
HTML served v1 and its relevant formulas were accessible. Ferreira's
PDF text loses mathematical glyphs: the hypothesis/equality/direction
prose was read, and the energy-upper-bound display was cross-checked
against Tang et al.(5). Screenshot calls returned text placeholders;
no visual inspection is claimed. Direct shell retrieval failed DNS.
No missing-glyph numerical formula is used. These do not leave an
essential source blocker for the bounded finite-sum test.

The 2011 *Some mathematical properties of superoscillations* PDF was
opened only near its introduction/physics discussion; its mathematical
contracts were not assessed or used. Other generalized-function,
Fock-space, arbitrary-template and optical leads were search results,
not inspected theorem inputs. No claim from them is imported.
The initial notebook-scoped git listing was overly broad and truncated;
it served only to note preexisting edits. All claim-bearing local files
above were read at their exact paths. Existing work was preserved.

### Decision and single continuation

EXPLORE: adequate source coverage for one bounded finite-band test;
no new result or rate is established. The simultaneous original-TV,
defect and boundary estimates remain mathematical gaps, not missing
source access. Review365 nominates the m_n=n subfamily for separate
approval next turn. Failure there would stop only that family or its
particular certificate. Further literature requires a changed hypothesis
or specific new essential source, not another repetition of this review.

The main positivity/forcing gaps and all independent transfer,
realization and regulator assumptions listed in the preserved nomination
remain open. PROOF.md and DAG.md are unchanged because no argument
changed. No mathematical exploration attempt, quota/counter reset,
progress beyond the sources checked, or RH candidate is claimed.
