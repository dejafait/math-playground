# Actual even operator — one interior residual-norm test

TARGET: Test whether a single centrally supported even concentrating bump family makes ||f||_{L-infinity(-1/4,1/4)}/||(A_e+16I)f||_2 unbounded for C759a's complete operator, retaining both poles and all five prime shifts.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step829's exact Weil/uniform-eigenfunction, logarithmic graph-norm, generalized Fourier-weight embedding and residual searches, recorded in assessment828's completed comparison. Narrow graph-norm/concentrating-bump searches in local literature, ATTEMPTS and lemmas found no matching actual-Q certificate; assessment729 concerns quadrature compression instead. No novelty or exhaustive absence claim.
SOURCE_EVIDENCE: C759a(5)-(6),Proof1 and C759h Proof1-2 specify the local full operator/domain. Direct primary source https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf (Teschl, second edition2014, GSM157), Section7.1, equation7.3, Lemmas7.1/7.2/7.6 and Theorem7.5, printed pp187-190, inspected830 with relevant proofs. Assessment828 supplies reused boundary/eigenspace comparison; no unread embedding theorem is a premise.
COMPARISON: The inspected spectral estimates control Hilbert norms; boundary regularity is for bounded solutions and does not supply the required norm conversion. General logarithmic-smoothness intuition is not a theorem for this compressed operator. The local difference to test is full-operator action on one concentrating family, including every bounded arithmetic and pole term.
GAP: Establish or fail to establish divergence of the stated ratio, with valid domain membership and complete Fourier-tail estimates. No divergence, residual estimate, graph embedding failure, eigenfunction error or sign is asserted by this assessment.
REASON: This independently testable prerequisite needs no positive ground state, full spectral gap, boundary regularity theorem or ordinary kernel. It can determine whether unrestricted L2-residual-to-interior-uniform conversion is a viable ingredient before spending work on a weighted sign enclosure.
SCOPE: One real even family f_epsilon(x)=h(x/epsilon), h(t)=(max(1-t^2,0))^2, 0<epsilon<1/8, extended by zero. Fixed half-width1, full A_e from C759a/C759h, shift16, interior interval(-1/4,1/4). No spectral projection, eigenvalue computation, fixed-pair repeat, forcing solve, parameter/basis sweep or actual-Xi bridge.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. Direct positive simple even ground-state certification is
one possible partial input; parity, other windows and Xi realization
remain unresolved independently. This test addresses only the error
norm needed by an unrestricted residual method, not the ground-state
claim itself. The original weighted-sign implementation remains parked.

## Exact bounded test and qualifications

Use precisely C759a(1),(5)-(6),Proof1 and C759h Proof1-2. The latter
already justifies action on H1_0 trials and the resolvent at-16; cite
those results rather than recomputing a floor or identifying the operator
with a different logarithmic Dirichlet realization. Both poles and all
n=2,3,4,5,7 terms must remain. No smoothing or sign assumption is allowed.

For the single family specified in SCOPE, determine whether

    lim_(epsilon down to0)
    ||f_epsilon||_(L-infinity(-1/4,1/4)) /
       ||(A_e+16I)f_epsilon||_2 = infinity.

This displayed limit is the requested test, not an established fact.
Check the numerator, H1_0 membership, zero-extension action and the
complete denominator. Use the exact logarithmic multiplier information
in C759a(5), not merely C759h's deliberately coarse derivative bound.
Keep the transformed low-frequency region and the entire Fourier tail;
an asymptotic slogan or sampled residual is insufficient. The finite
prime and pole contributions must be bounded explicitly, not dropped
because their supports are displaced. No mathematical script is needed
unless it materially verifies a load-bearing bound.

Continue only if rigorous estimates decide this limit. Divergence
would obstruct a uniform L2-residual-to-interior-sup bound on the full
domain. It would not disprove eigenfunction positivity, a conversion
on a restricted spectral/error class, or an estimate using stronger
residual norms. A global weighted enclosure has further endpoint and
isolation requirements; do not call this a theorem about them without
stating an appropriate weight hypothesis. If the concentration estimate
fails or remains inconclusive, record its exact failed inequality and
stop this family; do not infer the converse embedding or start a sweep.

This is ordinary Fourier/operator specialization, not creative work
or an originality claim. The direct calculation is justified because
whole-space weighted-space embeddings do not by themselves check support
restriction and the actual complete arithmetic/pole terms. No generic
embedding theorem is reproved. EXPLORE permits a later REPRODUCTION
attempt at this exact target. Separate literature review830 approves
this unchanged target with the direct primary citation below. Neither
review829 nor830 supplies the concentration result. No cross-notebook input. Full matching Mathlib coverage is
unchecked, not asserted absent.


## Separate source approval830 — 13 November2026

LITERATURE_REASON: Supervisor recovery requires a direct primary URL in
the ready assessment; the target and its hypotheses are unchanged.

Inspected Gerald Teschl, *Mathematical Methods in Quantum Mechanics*,
second edition (2014), GSM157,
[author-hosted primary PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf),
Section7.1, printed pp187-190 (PDF pages198-201, zero based).
Equation7.3 fixes the unitary normalization. Lemma7.1 is stated on
Schwartz functions and proved by integration by parts; Lemma7.2(7.7)
states dilation for positive scale on that class, with proof left as
an exercise. Theorem7.5 extends the transform unitarily to L2. Its
norm argument uses identity7.10 and density. Lemma7.6 identifies this
extension with the integral on L1 intersect L2; its full proof uses
bounded-support approximation followed by truncation. Those cases,
not the unrelated Fourier-spectrum assertion, were inspected.

Applicability boundary: the notebook uses the unnormalized transform,
so the future calculation must keep its dt/(2pi) convention. The trial
is not Schwartz; do not apply Lemma7.1 or7.2 to it without justification.
Lemma7.6 allows checking dilation by substitution in its integrable
transform; derivative and tail control still require a valid argument
for this particular piecewise polynomial. C759h already supplies the
H1_0 action criterion. No such bump estimate is derived in this review.

A narrow primary-source query was `site.mat.univie.ac.at teschl
Mathematical Methods Quantum Mechanics Fourier transform Plancherel
theorem pdf`. Read the resulting author-hosted second edition directly;
do not transfer its numbering to C759h's separate first-edition
resolvent citation. Exact-target search and failed-route comparison
from829 remain adequate and are reused, including stops822/823/826
and the nonmatching quadrature target729. This review repairs source
traceability, not mathematical novelty or evidence for divergence.
EXPLORE remains appropriate: the cited general Fourier tools do not
state the actual compressed-operator norm ratio. No essential source
is now missing for the one-family direct test; its complete estimates
and domain verification remain the next mathematical obligation.
Mathlib full-match coverage remains unchecked.
