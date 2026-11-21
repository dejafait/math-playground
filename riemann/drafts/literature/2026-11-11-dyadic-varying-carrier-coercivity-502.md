# Dyadic varying-carrier coercivity: completed source comparison

TARGET: Establish or obstruct a uniform weighted coercivity bound for dyadic corrected carrier mixtures with varying H2 envelopes on the common growing window.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step503 performed bounded collective almost-orthogonality, varying-envelope Gabor and stronger complete-Weil-form searches; inspected primary statements and relevant proof passages listed below; reused L745's continuous-frame comparison and the carrier-span/joint-energy/summability/IMS stops. No matching full corrected weighted inequality was located in this checked scope; no novelty follows.
SOURCE_EVIDENCE: Montgomery--Vaughan author-hosted Multiplicative Number Theory II draft, Theorem G.3/proof pp399-400; Hilbert's inequality (1974), Theorem2/Corollary2 p74 and proof p82; Tao (2011), Cotlar--Stein Lemma1 (11)-(13) and complete finite proof; Doerfler--Matusiak arXiv:1112.5262v1, Theorem3.3/proof pp8-9, Corollary3.4 p10 and Proposition3.6/proof pp12-13; Li paper45 v2 (9 November2026), Theorem1.1/(1.1), (2.1) and stated scope. Retain prior Vasy/DLMF/Rosser--Schoenfeld imports without refreshing them.
COMPARISON: Standard finite-matrix Schur control permits arbitrary profile-dependent entries once their normalized row/column sums are paid. The continuous exponential theorem has scalar coefficients; the inspected Gabor frame results require extra covering/decay or an existing frame and do not assert this synthesis lower bound. Fixed-window complete-form positivity also does not give the growing-window logarithmic coefficient floor. None directly imports the target; one standard Fourier/Sobolev and matrix specialization is justified.
GAP: The exact inequality remains unproved: common-window diagonal use, logarithmically normalized high/high overlap and the whole correction synthesis must be paid uniformly in R,J and the profiles. These are application obligations, not missing essential theorem access. Independent low-block signs, non-neutral coverage and full-space assembly remain open.
REASON: First source review of the changed collective hypotheses is complete. Reuse the ready scalar/arithmetic tools and import the matrix theorem; derive only the quantitative application in a later research turn after separate approval of this changed assessment. This turn establishes no coercivity estimate or obstruction.
SCOPE: Exactly the finite-family inequality below, with fixed M,chi, K_R=floor(log log R/ell), t_j=2^j R, arbitrary w_j in F_(K_R,M), original complete energy and unchanged corrections. No infinite mixture, all-window positivity or low-block sign is covered.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target adds independently varying envelopes, logarithmic coefficient weights, an arbitrary finite carrier count and a common growing window beyond L745 and the ready pairwise assessment. Only that missing collective coverage was reviewed.

## Original nomination, step502

The nomination and its then-missing coverage below are preserved. The
completed step503 comparison supersedes their source-status statements;
the mathematical target and all its quantifiers are unchanged.

## Proposed mathematical target, not a result

Fix ell=log(3)/2, a finite M>=1 and the same fixed chi as in C744n.
For a base R>=e^3 put K_R=floor(log log R/ell) and L_R=K_R ell.
For each finite J>=1, let t_j=2^j R for 0<=j<J and choose arbitrary
w_j in L744(1)'s F_(K_R,M). Use the unchanged complex-linear
cellwise correction of C744n(1), on this common window, to define
v_j=e^(it_j x)w_j-h_(t_j,w_j). For arbitrary complex coefficients
c_0,...,c_(J-1), put g=sum_j c_j v_j.

The exact proposed threshold is one R_*(M,chi)<infinity such that
for every R>=R_*, every finite J, all admitted profiles and all c,

\[
 E_{L_R}(g)\ \ge\ \frac18\sum_{j=0}^{J-1}
                                  \log(t_j)|c_j|^2.
\]

This inequality is unproved. Empty profile families assert no
existence. All norms and energies are the original complete ones;
all prime powers and exact poles must be retained. Only positive
dyadic carriers are nominated here. No density or limit in J is
assumed, and no positive low block is an input.

## Why this target and its bounded test

The main gap is L030-L032/C032a actual-Xi positivity. A uniform
collective high-block bound could replace individually positive
trial vectors by a controlled finite trial space when paying
interactions with an independently positive low block. It would
still not supply that missing low-block sign or a decomposition
covering all tests. The growth in support and independently varying
envelopes distinguish this target from L745's recorded fixed-family
scope. This is established-route development, not a claim of a new
creative central-sign mechanism.

The discriminating calculation, only after source approval, is the
complete finite Gram matrix normalized by sqrt(log(t_i)log(t_j)).
Seek a lower bound at least 1/8 independent of R>=R_*, J and the
profile choices, including the correction pairings. A uniform
off-diagonal operator estimate together with a justified diagonal
lower bound is a possible sufficient test, not an available theorem
of this nomination. A bound growing with J, uncontrolled derivatives
or K fails the proposed mechanism. An admissible sequence at
R tending to infinity with normalized Rayleigh quotients below 1/8
would refute the exact eventual target. Failure to close the estimate
alone is inconclusive and would require a refined mechanism before
repetition; neither outcome would resolve RH.

Essential local inputs for the continuation are L744, C744n, C744o
and the exact scope of L745. C744n's individual conclusion uses
its own prescribed window for each carrier; a common-window use
must be justified from its pre-substitution bounds, not assumed.
C744o cannot simply be applied with u replaced by an arbitrary
high carrier: that replacement changes the fixed H2 budget. The
collective weighted overlap and correction cost therefore require
their own theorem comparison and later proof. No such extension
has been derived in step502.

## Failure comparisons and source-review boundary

L742 stops a particular absolute summability claim for spatial
translations under RH; no spatial-translation summability is proposed
here. L750 stops the specified corrected two-window IMS inequality;
no IMS sign is assumed. The retained carrier-span and generic Schur
stops prohibit promoting a paid trial space to general positivity
without a complement and coverage theorem. Those stops are preserved.

The next source review should reuse the retained Fourier, scalar and
arithmetic imports and search only for the missing collective
almost-orthogonality statement and stronger matching complete-form
results. Check their hypotheses on varying envelopes, logarithmic
weights, finite-family size, common support and correction operators.
Inspect essential theorem statements and relevant proof cases before
approving a mathematical attempt. Additional literature is justified
by these changed hypotheses; it is not another review of C744o.

No justified creative low-block mechanism emerged from the approved
audit: C744o is an upper bound on coupling and supplies no lower
sign margin. This is the concrete blocker to a creative nomination,
not a global ban on such work. The newly nominated collective test
must pass its separate gate; no result or novelty is certified here.

## Completed source review: 11 November 2026, step503

The main gap remains L030-L032/C032a actual-Xi positivity. This target
would pay a collective high-frequency trial block, potentially useful
with C744o after an independent low-block margin. It leaves that margin,
the non-neutral complement and coverage of arbitrary tests unresolved.
This is a literature-only review: no target inequality, counterexample,
new auxiliary estimate or mathematical script has been produced.

### Primary matrix input and the upper/lower distinction

[Montgomery and Vaughan, *Multiplicative Number Theory II: Primes and
Sieves*, author-hosted draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
undated version retrieved 11 November 2026, Theorem G.3, printed
pp399-400 (PDF pp411-412), states for every finite complex M by N matrix A

    ||A||_(2->2) <= sqrt((max_i sum_j |a_ij|)(max_j sum_i |a_ij|)).

Its complete Cauchy--Schwarz proof and the following qualification about
near-diagonal matrices were inspected. This retained input has no
restriction on how entries depend on envelope choices. It is the
appropriate theorem to import for an estimated finite normalized Gram
remainder; it does not supply those entry estimates or a diagonal lower
bound. Its constants introduce no dimension factor if both maxima are
bounded uniformly. No new matrix theorem should be reproved.

[Terence Tao, *The Cotlar-Stein lemma*, 25 May 2011](https://terrytao.wordpress.com/2011/05/25/the-cotlar-stein-lemma/),
Lemma1 (11)-(13), treats finite bounded maps T_i:H->H' between complex
Hilbert spaces. Both row sums of ||T_i T_j*||^(1/2) and
||T_i* T_j||^(1/2) must be at most one common constant B; then
||sum_i T_i||<=B. The finite power-method proof was read through its
limit in the power, not just the statement. This is an upper norm
theorem. It provides neither a positive synthesis lower bound nor
positivity of the complete energy. Applying it here would still require
the relevant product estimates; finite Schur control is sufficient as
a source tool for the proposed scalar Gram test. No infinite-series
extension or unproved Hilbert norm from an indefinite energy is used.

### Continuous exponentials and varying windows

Reuse the continuous theorem assessment in
[the fixed-profile comparison](2026-11-04-collective-corrected-carrier-span.md).
The primary [Montgomery--Vaughan, *Hilbert's inequality*, JLMS (2)8
(1974), 73-82](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
Theorem2 (1.6), Corollary2 (1.8), p74, and the real-line limiting
argument/corollary proof on p82 were retrieved. They control finite
exponential polynomials with distinct real frequencies, minimum gap
delta>0 and arbitrary complex scalar coefficients on an interval.
L745 already gives their precise continuous normalization and necessary
fixed-weight application. Here w_j(x) varies with both j and x: it is
not a scalar coefficient, and no common nonvanishing weight is given.
Thus the previous fixed-weight lower argument is not a matching import.
No new Ingham theorem or reproof of this result is justified.

The primary variable-window comparison is [Monika Doerfler and Ewa
Matusiak, *Nonstationary Gabor Frames — Existence and Construction*,
arXiv:1112.5262v1, 22 December 2011](https://arxiv.org/pdf/1112.5262v1).
Numbering here is v1: Theorem3.3 pp8-9, Corollary3.4 p10,
Proposition3.6 pp12-13. The first requires windows in W(L-infinity,l1),
two-sided pointwise square-sum bounds A0<=sum_k|g_k|^2<=B0 with A0>0,
and polynomial decay about delta-separated centers with uniform positive
constants and exponents in a compact interval with lower endpoint >2.
It constructs sufficiently dense modulation parameters giving an L2
frame. Corollary3.4 states the frequency-domain counterpart with the
same covering and decay requirements. Proposition3.6 starts with an
existing nonstationary Gabor frame, bounded positive modulation
parameters and a quantified small polynomially localized perturbation.
Theorem3.3's Walnut/diagonal-versus-remainder proof and Proposition3.6's
perturbation proof were inspected. None asserts the present weighted
complete-energy synthesis lower bound. Its covering/decay hypotheses
are not supplied by this target; none is silently added. These results
are scope comparisons, not imported inputs or independently audited
frame theorems. No inference from an analysis frame lower bound to
independence of arbitrary synthesis coefficients is licensed.

### Stronger complete-form claims and retained local coverage

Reuse the generic finite-band comparison already retained in the
fixed-profile assessment; it does not identify these supported carriers
with an exact high Fourier subspace. Also inspect [Hongmin Li,
*Cutoff-free positivity of localized Weil forms through the (log11)/2
threshold*, paper45 v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Theorem1.1/(1.1), Section1 limitations and normalization (2.1).
The stated strict positivity concerns its complete Friedrichs form for
support radius 0<a<=(log11)/2. This is a fixed finite support range;
the nominated supports grow without bound. It also supplies no stated
logarithmic coefficient lower floor for our varying carriers. Its
certificate and normalization transfer were not audited here; no part
of that positivity claim is imported, and no new all-support result is
inferred. The changed version is recorded rather than presumed covered
by an older source review. Following its unrelated all-scale leads is
outside this target and not an essential prerequisite for this attempt.

Retain the inspected Fourier, digamma and prime-mass imports recorded
in [the ready mixed-pairing review](2026-11-11-growing-window-mixed-pairing-498.md).
The relevant full local passages read were L744(1)-(9),
C744n(1)-(10), L745(1)-(17), and C744o(1)-(12), including the whole
correction and delay treatment. Their exact conclusions are not
extended during this review. C744n's pre-window estimates explicitly
state their K-independence; its conclusion still uses its own K(t).
C744o controls a neutral bounded-H2 profile against one corrected
carrier, not a carrier against another uniformly bounded-H2 input.
L745's common-profile constants depend on that profile and support.
These distinctions are the quantitative work remaining, not reasons
to rerun completed audits.

### Bounded research scope after separate approval

SPECIALIZE permits one attempt on the unchanged TARGET, classified
REPRODUCTION if obtained through these standard mechanisms. Import the
source tools and reuse the scalar/arithmetic specializations; do not
reprove generic frame or matrix results. The additional work is:

- Justify each diagonal lower bound on the common K_R window from
  the pre-substitution estimates, keeping the original normalization.
- Estimate the logarithmically normalized full high/high Gram entries
  and their finite-matrix operator cost for independently varying H2
  profiles. Do not assume disjoint Fourier supports, stronger uniform
  derivatives, or substitute a high carrier into C744o's fixed budget.
- Include both carrier/correction pairings and correction/correction
  pairings, every prime-power delay, the exact complex poles and the
  collective normalization. Pay the whole finite family before taking
  any supremum in J; no infinite synthesis limit is required.

These are unproved application obligations, not new lemmas or asserted
estimates. The exact continuation test remains the proposed coefficient
floor 1/8 with one R_*(M,chi) independent of J and all profiles.
An uncontrolled J or K cost fails this sufficient mechanism; an
admissible counterexample sequence with R tending to infinity and
weighted Rayleigh quotient below 1/8 refutes the eventual target.
An unsuccessful estimate alone does not refute it. Save partial
reasoning and require refined input before repeating an unproductive
attempt. Empty families assert no existence.

The carrier-span, generic-joint-energy, conditional summability and
fixed-corrected-IMS ATTEMPTS records were read in this review. Their
obstructions remain: no density, low-block margin, prime-only saving
or sign-preserving localization is assumed. Historical route stops do
not ban this independently testable common-window weighted question.
No justified creative central-sign target emerged: neither the imported
upper norm tools nor the paid trial vectors supply the independent
low-block margin. This is established-route development, not a creative
mechanism relabeled to meet a scheduling target.

Queries actually run: `Cotlar Stein almost orthogonality lemma theorem
operators sum square roots norm pdf university`; `Ingham nonharmonic
Fourier series inequality separated frequencies varying amplitudes
Sobolev envelopes almost orthogonality`; `"varying" "envelopes"
"almost orthogonality" Sobolev`; `"Weil" "quadratic form" "high
frequency" positivity`; `"nonstationary" "Gabor" "molecules" Bessel
Riesz sequence Sobolev`; `Dorfler Matusiak nonstationary Gabor frames
existence construction arxiv 1112 theorem 3.4`. Exact source URLs above
were opened; this bounded search is not a novelty certification.
Other survey, molecule and operator-generalization hits remain unread
leads and are unnecessary to this finite Schur-based attempt. No
essential source is blocked. Full matching Mathlib coverage is not
checked; supporting Fourier results do not constitute the full target.

Outcome: EXPLORATION, a completed first source comparison with a ready
SPECIALIZE scope, not a mathematical advance or informative coercivity
counterexample. The changed ready assessment is submitted for separate
approval next turn. No lemmas, mathematical scripts, PROOF.md or DAG.md
were changed by step503.
