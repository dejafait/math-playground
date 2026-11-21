# Poisson add-one contact representation — completed source comparison

TARGET: Assess whether Pitman-Yor2003's Poisson representation supports a nonnegative squared-add-one-difference representation of -Phi for L874's actual-theta d=2 contact flux at lambda=1/16.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step2144 checked exact theta/Poisson/contact and stronger Mehler, covariance, Gibbs-change-of-measure and Papangelou terms; read the primary fixed-point, marking and covariance statements/proof cases below; reused the BPY weight and recorded score/node-mass failures. The source-overlap check located the already-assessed unconditional real-zero regime containing the fixed slice. No novelty or general impossibility inference.
SOURCE_EVIDENCE: Pitman-Yor2003 Section6.3 Proposition12(ii)/(119), (i)=>(ii) and (ii)=>(iii)/(124), pp318-319; Last-Penrose, Lectures on the Poisson Process, version21August2017, Definition5.3/Theorem5.6 pp40-42 and Chapter20 pp211-217, especially Theorems20.2-20.4 with proofs; Platt-Trudgian2020v1 Section3.4 Corollary2; Polymath2019v2 (4), transition paragraph and Theorem1.1; reused L488(11) and reopened Choi2026v1 Lemma3.4/Theorem4.1/(19) and the following Hankel formulas with relevant proofs.
COMPARISON: The inspected Poisson covariance is bilinear under a base Poisson law, with a square for variance and an FKG sign under explicit monotonicity. It supplies neither the weighted flux square nor its correction-term sign. Separately, the saved lambda=1/16 target already lies in the known lambda>=1/20 real-zero regime; strict H2 contact exclusion requires a separately checked specialization, not a new probabilistic sign mechanism.
GAP: No inspected theorem identifies -Phi with a nonnegative squared-add-one integral after the joint weight/null constraints. Weighted-domain verification and signed remainders are unpaid. The source-backed reciprocal-zero/Hankel formulas cover a distinct follow-up strictness audit; that audit has not been performed here.
REASON: Park this automatic Poisson-square mechanism at the source-scope test: no signed kernel was supplied, and the selected slice overlaps known all-real-zero coverage. Select a separate known-result strict-contact-exclusion audit to repair target selection before any lower-time creative mechanism; do not repeat the finite closure, generic covariance or score derivations.
SCOPE: Completed source comparison only. EXPLORE records limited search coverage and does not approve a repeat Poisson sign attempt; reopening requires an explicit new signed kernel and full weighted domain. The next strictness audit has its own SPECIALIZE assessment.

## Completed comparison — 21 November 2026, step2144

Main gap: L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The intermediate target was exactly the saved squared
add-one representation of -Phi at the conditional full-degree d=2
contact. Its plausible use was one boundary-sign input; it would leave
initialization, other degrees, lower time and endpoint continuation
open. The continuation test required a specified nonnegative kernel
without an uncontrolled signed correction. The inspected sources do
not pass that test. This is a source-scope decision, not a theorem
that no such representation exists, or a proof of the opposite sign.

### Primary construction and domains actually inspected

[Pitman-Yor](https://doi.org/10.4153/CJM-2003-014-x), published
Canad.J.Math.55(2)(2003),292-330, Section6.3 Proposition12, pp318-319:
X is nonnegative with mean2/3; the iid marks X_i have its law, and
the Poisson locations M_i in (0,1) have intensity2m^(-2)(1-m)dm.
Equation(119) is sum_i M_i^2 X_i =_law X. Read both directions
relevant to that representation: (i)=>(ii) compares cumulants with
(98); (ii)=>(iii) uses the nonnegative Laplace functional, Fubini,
the Levy density(124), and its Laplace derivative. The proof explicitly
distinguishes a finite-moment cumulant argument from the general
finite-mean characterization. It is not a covariance/sign theorem
for a positive squared-log weight.

[Last-Penrose](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf),
author version21August2017 of *Lectures on the Poisson Process*:
Definition5.3, pp40-41, and Theorem5.6 with proof, p42, cover
independent marking of a proper Poisson process by a probability
kernel. For the intended independent S2 marks this identifies the
base marked intensity as 2m^(-2)(1-m)dm nu(dy). This is a direct
source applicability description, not a construction or domain proof
for the weighted law. The intensity is sigma-finite, not finite;
finite-total-intensity shortcuts cannot be assumed.

Chapter20, pp211-217, fixes a proper Poisson process eta on a measurable
space with sigma-finite intensity rho. Its D_z is the add-one
difference; eta_t is independent t-thinning; P_t also superposes an
independent process of intensity(1-t)rho. Theorem20.2/(20.13) requires
F,G in L2(P) and DF,DG in L2(P tensor rho) and states

    Cov_P(F,G)=E_P integral_0^1 integral D_zF (P_t D_zG) rho(dz)dt.

Theorem20.3/(20.16)-(20.17) requires only F,G in L2(P) and states

    Cov_P(F,G)=E_P integral_0^1 integral
        E_P[D_zF|eta_t] E_P[D_zG|eta_t] rho(dz)dt.

Read the full relevant proofs: Theorem20.2 uses the L2 contraction
to justify absolute Fubini and the Fock isometry; Theorem20.3 first
uses independence of the split Poisson processes, then approximation
by the dense test class, local L1 convergence of differences and L2
completion. This matters: the weaker symmetric domain must not be
replaced by an unproved add-one-energy bound. Theorem20.4, p217,
assumes both observables increase on a specified measurable B and
decrease on its complement. Its sign follows from that hypothesis,
not from arbitrary sign-changing tests. The square case F=G supplies
variance, not a sign for two prescribed unequal observables.

The same distinction was cross-checked in Last, *Stochastic analysis
for Poisson processes*, arXiv:1405.4416v1, Section8 Theorems8.1-8.5,
pp25-27, including the complete symmetric-domain proof. No separate
import from that survey is needed.

### Applicability comparison; no new weighted formula derived

Use C874e's already-audited weight
w(x)=exp(u(x)^2/16+u(x)/2), u(x)=log(x/(2/pi))/2, normalizer
Z=2F(1/16,0), and even pushforward. The relevant total in(119)
is the argument of the joint weight. Independence in the unweighted
marked construction does not authorize factoring that weight among
marks, or applying the base-Poisson covariance/FKG theorem under its
changed probability law. No theorem inspected asserts that this law
remains Poisson. Alternatively retaining the base law requires
explicit weighted observables and normalization corrections. Neither
their complete L2 domain nor a nonnegative completion with the null
constraints is supplied by the cited theorem. This review derives no
such correction formula, kernel or sign. Even a valid bilinear
representation would need additional structure to become the requested
square. L874's mean/null identities alone are not an inspected source
for that structure. C874b's auxiliary atomic law is not the marked
process or the physical u-law.

Reuse the source assessments of steps2139/2140 and
`2026-11-06-actual-theta-contact-score-pairing.md`, with the latter's
older L874-audit label corrected by the subsequent November9 record.
Their raw-moment, node-mass, score, GHS-cone and absolute-covariance
stops remain intact. C874e is an audited finite-closure stop, not a
universal nonlocal-operator obstruction. Searches in the named local
contact files found no already-approved weighted Poisson-square
theorem. Older prime-Poisson covariance records concern harmonic
Poisson kernels, a different object, and were not used as inputs.

### Known-regime overlap changes the next target

The reused `2026-11-09-low-time-h2-contact-exclusion-review.md`
already records the published cutoff. Reopened
[Platt-Trudgian](https://arxiv.org/html/2004.09765v1), Section3.4
Corollary2 and its supporting paragraph: Lambda<=0.2, using their
Theorem1 and Polymath's conditional table. This is a rigorous
published computational theorem being cited, not a new replay of its
computation. [Polymath](https://arxiv.org/html/1904.12438v2), (4) and
the following transition statement, defines H_t and states all-real
zeros for t>=Lambda; Theorem1.1 already gives Lambda<=0.22.
L488(11)'s audited identity is F(lambda,z)=8H_(4lambda)(2z).
Thus the selected lambda=1/16 corresponds to t=1/4, beyond either
published bound. This is a known-result scope comparison, not a new
zero-free region or a claim about lambda=0.

Reopened [Choi v1](https://arxiv.org/html/2611.04359v1), an unreviewed
preprint dated3November2026: (5)-(10) fix its kernel K as local K/4
and a as local lambda; Lemma3.4 and its full proof give the deformed
Hadamard product, reciprocal-square summability and infinitely many
distinct zeros; Theorem4.1's unconditional a>=0.05 branch and the
Hankel formulas following(19) cover the corresponding known-regime
structure. Read the relevant product, local-log convergence, Gram
and distinct-support proof cases. These are useful source coverage,
not peer-reviewed validation of the preprint. A separate audit must
check the exact local H2 indexing and strictness at its confluent
coefficients: positivity of a distinct-node divided-difference matrix
alone does not establish that strict confluent limit. No strict H2
exclusion lemma is derived or accepted in this source-only step.

This overlap makes another square-sign attempt at this fixed slice a
poor next task. The separate assessment
`2026-11-21-known-regime-h2-strictness-audit-2144.md` prepares a
known-result strictness audit, preserving the conditional target and
the main lower-time gap. A creative attempt remains blocked by the
absence of an independent signed mechanism below the established
cutoff; the strictness audit is expressly not creative mathematics.

### Search record, limitations and decision

Queries included `Poisson covariance identity Mehler formula Last
Penrose Theorem covariance add one difference`, `Poisson Gibbs change
of measure covariance identity Papangelou intensity squared differences`,
`Last Penrose Lectures Poisson Process pdf covariance identity
Theorem20.2`, `"Pitman" "Yor" "Poisson" "covariance" "theta"`,
`"theta" "Poisson" "squared" "Hankel" covariance`, and
`"Poisson" "weighted covariance" change measure identity`.
Followed the author-hosted monograph and survey, not search snippets.
Generic Gibbs/Papangelou and Poisson-Dirichlet search hits remained
uninspected leads; none is an imported weighted sign theorem.
Direct shell PDF downloads failed DNS; readable browser text supplied
the essential statements and full relevant proof cases. Screenshot
calls supplied no usable visual evidence. This is not a persistent
essential source-access blocker. Full matching/supporting Mathlib
coverage is not checked; unrelated third-party search hits are not
evidence of Mathlib inclusion.

Outcome NEGATIVE, literature, NOVELTY_UNCHECKED: the new useful
evidence is the theorem-scope mismatch plus known-regime overlap,
which changes routing. No mathematical lemma, counterexample or RH
advance is claimed. Park automatic Poisson-square transfer; reopening
requires a materially specified signed kernel/domain repair. Retain
all existing unfinished work and canonical results. PROOF.md and DAG.md
are unchanged because no mathematical argument was added.

## Original nomination — step2143, retained

## Exact proposed scope and relevance

The main gap remains L030-L032/C032a, actual-Xi all-degree algebraic
mixed positivity. This nomination concerns only a conditional d=2
contact sign at the fixed lambda=1/16. Read the precise Poisson
representation in Pitman-Yor, *Infinitely divisible laws associated
with hyperbolic functions*, Canad. J. Math. 55(2) (2003), 292-330,
Section6.3 Proposition12(ii) and its relevant proof, particularly
(124), DOI https://doi.org/10.4153/CJM-2003-014-x. Then locate a
primary add-one/covariance theorem appropriate to that construction.
The proposed sign representation is a testable question, not a
claimed consequence of either theorem. Do not reconstruct missing
Poisson hypotheses from the scalar distributional identity.

Use L019/L058's actual law, L874's definition of R and Phi, C874b's
single-extension premise, and C874e's checked weight and domain as
the named local inputs. Specifically, take c=(c0,c1,c2) with c2!=0,
H3 positive semidefinite, H2 c=0, and S_2>0 at the fixed slice. Then
the proposed observable is Phi=E_mu[u^2 R(u)], where R is precisely
L874's degree-twelve polynomial and E_mu R=E_mu[u R']=0. This
states the existing target; it does not assume such a contact exists.
Use the full log law when applying BPY, and the half-line law only
through the justified even pushforward. A tilt of a Poisson functional
need not remain Poisson, and its increments need not be independent.

The bounded source test is whether a cited covariance identity can
be specialized, with explicit hypotheses, to a representation of
-Phi by squares of add-one differences against a nonnegative kernel
after the stated null constraints. The kernel and any correction
terms must be specified before approving a later proof attempt.
If the source leaves an uncontrolled signed bilinear remainder,
requires an unproved association property of the tilted process,
or merely recovers the existing scalar BPY/score identity, record
that mismatch and abandon this sufficient mechanism unless a
materially new, independently testable repair is identified.

## Reuse, failures and unresolved assumptions

Reuse the BPY/Pitman-Yor probability-law assessment and C874e's audit;
do not repeat the finite-closure test. Compare with C874b's positive
formal-flux examples and the prior assessment's recorded ordinary-
moment, node-mass and score failures. Those examples do not realize
the actual theta law. A positive variance identity alone cannot
pay the signed observable. No auxiliary mass bound, Poisson
association, contact existence or universal operator impossibility
is licensed here.

Even a successful fixed-slice sign representation would leave
S_2=0 and lower-degree cases, other lambda, initialization, tangency,
higher degrees, endpoint continuation and the main RH gap unresolved.
Full matching and supporting Mathlib coverage are unchecked. This
is a literature-only continuation until a separate ready assessment
exists; no new formula or sign lemma has been derived or approved.

LITERATURE_REASON: The target changes from the audited direct BPY operator to a Poisson two-observable covariance/sign representation; the exact point-process construction and an applicable weighted add-one theorem are essential missing coverage.
