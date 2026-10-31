# Nullvector arithmetic slope: completed bounded source screen

TARGET: Discover one arithmetic-specific, independently testable estimate for L522's signed prime sum at a nullvector, comparing at most three mechanisms against the recorded Abel, nodal, transport, multiplier and resolvent stops.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Screened exactly three mechanisms: archimedean Sonin domination, finite-Euler transport, and actual increasing-prime Sonin increments. Searched exact slope/nullvector terminology and pole-compensated increments; checked narrow local Weil assessments and the recorded Abel, nodal, transport, multiplier and resolvent stops. Queries and inspected primary passages are recorded below; search failure establishes no novelty.
SOURCE_EVIDENCE: Read Connes--Consani author PDF dated 4 July 2021, Theorem 1 p.2; Connes--Consani--Moscovici arXiv:2310.18423v2 Sections 4.6--4.8, Theorem 4.6 and full proof; Connes--Consani EMS Surv. Math. Sci. 9 pp.464--469, Proposition 4.3/Lemma 4.4 with proof, Theorem 4.6 and (20)--(24); bramble_trace paper 2 v2 (16 October 2026), (6.1)--(6.3), Theorem 6.5 and full displayed proof (6.17)--(6.26), Theorem 7.1 and full proof (7.1)--(7.4). Source manuscripts and upstream proofs are not independently audited.
COMPARISON: The archimedean theorem has incompatible support/vanishing hypotheses; Euler transport changes the inner product and leaves a compact unsigned defect. Paper 2 Theorem 6.5 gives an uncorrected Sonin increment O_h(p^(-1/2)(log p)^(9/10)) against arithmetic scale 2p^(-1/2)log(p)||h||_2^2. Its pole-compensated projection is outside that theorem, and its corrected-overlap theorem is fixed-test only. No matching nullvector slope inequality was established.
GAP: S<=P-H remains open. Test separately whether the explicit pole phase changes the leading critical-prime Sonin increment; no source inspected supplies that changed-projection estimate. Its connection to L522 nullvectors and any collective signed bound remains independent work.
REASON: New source-level obstruction evidence parks automatic uncorrected-Sonin absorption without banning actual-nullvector estimates. A distinct common-phase, padded-support projection test is nominated in a separate assessment, subject to separate supervisor approval. No new theorem, lemma or mathematical script is derived here.
LITERATURE_REASON: The target changes from auditing an interior Green correction to finding a nullvector-specific arithmetic slope input; essential source coverage for that new mechanism is missing. This is not further browsing on the ready L525 target.
SCOPE: Completed literature-only discovery on the exact TARGET, three screened mechanisms. The original nomination instructions below are retained as history; completed evidence and the separately reviewed nomination follow. New continuation coverage is in 2026-10-30-pole-compensated-sonin-increment-test.md and still needs separate supervisor approval before research.

The exact benchmark is L522's finite sum

    S = sum_(n>=2,log(n)<=2A) [Lambda(n)/sqrt(n)] log(n)
          integral [f(y+log(n))-f(y-log(n))] Df(dy) <= P-H.

Here f=Eu is the continuous BV zero extension of L522's real normalized
nullvector. Preserve that statement's conditional hypotheses, including
0<a<A, ell=2a>log(2), the nonzero left trace and nonresonance assumption
log(2)!=ell-log(n) for positive-weight cutoff atoms. The nonzero trace
is a contradiction hypothesis, not a fact about an existing vector.
H and P have exactly L516's centered definitions. Any candidate that
dispenses with these hypotheses must explicitly assess its wider scope.
L515 supplies bounded u and G_Iu, L521 the BV input, and L522 the
individual limits. Both shifts, equality atoms, nu_rho, c=log(2pi),
the signed pole and the full-Weil import qualification remain.

The benchmark is openly the missing zero-eigenvalue upper bound in
L516, not an established lemma. A useful intermediate input may be
strictly weaker if its downstream connection is specified and testable.
The family O(lambda) rate, branch/support law, collars and Xi transfer
would still require independent work even after a zero-eigenvalue result.

Read primary statements and essential proof cases for the best concrete
candidate, comparing exact assumptions with the local model. The next
step must either nominate a bounded mathematical test with a numerical
or signed threshold and a discriminating failure condition, or record
new source/overlap evidence ruling out the screened candidates. Merely
rewriting S<=P-H, repeating a generic identity, or repeating an old stop
does not count as an informative result. Do not search unrelated
notebooks or reopen the one-cusp audit as a substitute.

If a genuinely new central mechanism becomes adequately specified,
recommend proof_attempt/creative with the precise obstruction and
bounded test in NEXT_ESCALATION. At this nomination no such mechanism
is ready, so creative mathematics is not yet authorized. Mathlib
coverage is unchecked; no cross-notebook result is proposed.

## Completed comparison, 2026-10-30

**Archimedean domination.** Connes--Consani, *Weil positivity and Trace
formula, the archimedean place*, Selecta Mathematica 27 (2021), 77,
[author PDF dated 4 July 2021](https://alainconnes.org/wp-content/uploads/Selecta.pdf),
Theorem 1, printed p.2, assumes smooth multiplicative g supported in
[2^(-1/2),2^(1/2)] and its multiplicative Fourier transform vanishing
at i/2 and 0. It bounds W_infinity(g*g*) below by a scaling trace
compressed to the archimedean Sonin space with gap 1. Read definitions
(1)--(6) and the theorem, not its 55-page proof. L522 assumes ell>log 2,
a BV eigenvector and no such transform zeros. Its signed pole cannot
be silently removed. The theorem is not a slope bound for this model.

**Euler transport.** Connes--Consani--Moscovici, *Zeta zeros and prolate
wave operators: Semilocal adelic operators*,
[arXiv:2310.18423v2, 4 May 2024](https://arxiv.org/html/2310.18423v2#S4.SS7),
Theorem 4.6, assumes any finite place set S containing infinity and
gap parameter lambda>0. Its theta_S is an isomorphism of archimedean
and semilocal Sonin spaces. Read Section 4.6 Definition 4.5, (57) and
its complete one-prime proof; Section 4.7 (58)--(59), Theorem 4.6 and
its complete orthogonality proof; and Section 4.8's inner-product
qualification. The Euler multiplier is the product of
(1-p^(-1/2-is)); the map has bounded inverse but is not an isometry
in the unchanged norm. An orthogonal trace inequality or derivative
therefore does not follow merely by transporting the space.

The primary [Connes--Consani survey](https://ems.press/content/serial-article-files/37042?nt=1),
*BC-system, absolute cyclotomy and the quantized calculus*, EMS Surv.
Math. Sci. 9 (2022), 447--475, DOI 10.4171/EMSS/64, published 2023,
Sections 4.2--4.4, pp.464--469, explicitly distinguishes exact
triangularity in Proposition 4.3/Lemma 4.4 from quasi-innerness in
Theorem 4.6. Read the block proof and the discussion through (24).
The latter leaves a compact defect; compactness supplies no sign.
The underlying quasi-inner theorem's proof was not independently
audited. This parks an automatic import, not Euler methods generally.

**Increasing-prime increments.** bramble_trace,
[*Sharp Schatten asymptotics and Sonin trace localization for
semilocal Fourier cutoffs*, paper 2 v2, 16 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/2),
Theorem 6.5, (6.17)--(6.19), takes fixed h in C_c^infinity(R),
p tending to infinity through primes, L=log p, r=p^(-1/2),
f_L=h+V_Lh with V_Lh(x)=h(x-L), and the actual predecessor projection
S_<p for every prime smaller than p. For L>diam(supp h), it states

    Delta T(f_L)=O_h(r L^(9/10)),
    Delta(T-q)(f_L)=2r L ||h||_2^2+O_h(r L^(9/10)).

Here q is its archimedean plus finite-prime form, in its trace
normalization, not L522's operator by an assumed identification.
The proof cases read were: weighted evaluations outside a shrinking
frequency window; uniform omission of the endpoint prime; the
rank-two Toeplitz-kernel commutator argument; all three frequency
regions in (6.23)--(6.26); and the exact inverse Gram operator
G=(1+r)^2I-rS(2I+V_L+V_L*)S in the final projection formula.
No replacement of G^(-1) by I is permitted. The source's critical
prime contribution is -2rL||h||_2^2. Its uncorrected Sonin increment
is subleading, so it cannot absorb that term by itself. This source
conclusion concerns one prescribed test family and one increment,
not a negative complete Weil form, a nullvector, or RH. The complete
upstream Burnol evaluation, prime estimates and Toeplitz proofs have
not been independently audited; the site's acceptance report is not
such an audit. This is source-level negative evidence, not a new
canonical local theorem.

The same paper's Theorem 7.1 and full proof specify the explicit phase

    chi_M(t)=4 integral_0^M cosh(v/2) sin(tv)/v dv.

Multiplying the scattering symbol by exp(i chi_M) adds the pole on
the stated support class if every visible prime power is included.
Its overlap estimate o(exp(M/2)) is for a fixed smooth test. Its
Hilbert--Schmidt perturbation assertion holds at fixed M. Neither is
a bound on the new Sonin projection's moving-test increment. The
full proof retains compact-frequency cancellation, global domination,
the second-derivative bound and the fixed-M symbol-tail argument.
No stronger rate or uniformity is imported. A two-packet test has
diameter log p+diam(supp h); setting M=log p without padding would
violate the support bound in the pole theorem. This is a genuine
changed-hypothesis question, not a specialization of Theorem 6.5.

## Failure comparison, decision and limits

Reused the saved Abel assessment and read the ATTEMPTS for L517,
nodal L523, transport L524, weighted multipliers and generic pole
resolvents. Arbitrary smooth countertests are not nullvectors; the
nodal constraint can be vacuous; stationarity and absolute bounds
give no upper slope sign. The present arithmetic projection evidence
does not reopen those implementations. Narrow searches found no
local assessment of the pole-compensated increment counterpart.

Park automatic uncorrected-Sonin absorption. A separately nominated
test changes the projection by the explicit pole phase, keeps that
phase identical on both sides of a prime addition and pads the test
support. It asks whether the increment remains subleading or has a
negative contribution of the required arithmetic size. Even a useful
answer would leave collective comparison, rough-nullvector transfer,
L522's slope bound and all-support/Xi transfer unproved. The exact
test and thresholds are in
`2026-10-30-pole-compensated-sonin-increment-test.md`. Its mathematical
answer has not been derived or approved this turn.

Queries included `Connes Consani Weil positivity semilocal trace
inequality primes Sonin space theorem`; `Weil quadratic form
eigenfunctions prime shifts Euler product nullvector positivity
derivative`; `"Weil" "prime powers" "autocorrelation" positivity`;
`"Sonin" "pole" "increment"`; `"Sonin" "compensation"
"covariance"`; `"Weil" "pole" "Sonin" "nullvector"`;
`"Sonin" "pole-compensated" trace increment`; `"Sonin" "common"
"pole" prime trace`; and `"Sonin" "compensated" "projection" prime`.
Only inspected primary passages above support this decision. Discussion
post 3 appeared as a lead; its informal compensated-rate/RH comparison
is not imported as a theorem. No zero-free-rate estimate is proposed.
Unrelated hits and snippets establish neither coverage nor novelty.
Full Mathlib matching coverage is unchecked. No cross-notebook input.
