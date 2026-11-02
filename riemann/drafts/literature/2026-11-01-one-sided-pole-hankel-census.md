# One-sided pole geometry and the growing census — completed source comparison

TARGET: Assess source coverage for a half-exponent Hankel lower bound with all poles on the anchor's left side and total positive residue M<=C*n for arbitrary fixed C>0.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded changed-scope searches listed below; compared primary one-sided SPF and segment Cauchy-transform statements and relevant proof cases, reusing the saved general operator assessment. No matching quantitative theorem or counterfamily was found among the inspected sources; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Reuse BCQ (2016) Sections 2–5.2 and Chunaev–Danchenko 1907.07437v1 Theorem 1/(8) as assessed in 2026-11-01-full-pole-hankel-boundary-mechanism.md; newly inspected Chunaev–Danchenko 1611.03485v2 (9 January 2018), Theorems 3.1, 4.4 and 5.2 with relevant proofs, pp.7,12–13,15, https://arxiv.org/pdf/1611.03485v2 ; Yattselev, J. Operator Theory 61:2 (2009), Theorem 2.1 and Lemma B/proof use, pp.243–249, https://jot.theta.ro/jot/archive/2009-061-002/2009-061-002-002.pdf .
COMPARISON: C645g's half-exponent bound retains the small census coefficient. The newly inspected one-sided and phase-variation results do not evaluate the exact inverse-grid-weighted circle Hankel norm at arbitrary fixed C; general rational norm comparisons still need a controlled nonzero value. No inspected result resolves the proposed family.
GAP: Establish or refute the displayed uniform lower bound for the exact complex-weighted family with Re(a)<=x and M<=C*n; actual-Xi selection, census, clearance, realization, upper bounds and signs remain independent gaps.
REASON: Essential changed-scope source coverage is now sufficient for one bounded directional-functional or counterfamily attempt. Do not reprove general operator identities or replace the complex amplitudes by positive residues.
LITERATURE_REASON: The newly imposed directional support and arbitrary fixed linear census coefficient were outside the reusable general-operator assessment; this turn supplies that missing comparison.
SCOPE: Only the exact one-sided synthetic rational-symbol question below, including arbitrary close distinct poles and integer simple-pole residues; no actual-Xi theorem, higher-order poles or general positivity criterion is approved.
COVERED_TARGET: Test the one-sided half-exponent Hankel bound for the exact C645g symbol with Re(a)<=x and M<=C*n, by a directional functional or an admissible asymptotic counterfamily.

The original nomination below is preserved as context. The completed
comparison at the end supersedes its former unread-source status;
PROGRESS.md records the current continuation.

## Proposed bounded mathematical question

Retain C645g's fixed 0<delta<1/2, 0<eta<delta/2,
d=3/2-delta, R=3/2-delta/2, x=-d, n>=5 and t_j=j/n.
Retain its exact complex B_n and q in (1)--(2), including the factor
1/R, normalized circle measure, domain H2 and strictly negative
codomain modes. The set Z is finite and distinct, contains x, lies
in |a|<=R-eta, and avoids the grid. Every r_a is a positive integer
residue of a simple pole, and M=sum r_a.

The proposed changed geometry is

    Re(a)<=x for every a in Z,       M<=C*n,

where C>0 is any fixed constant, rather than the particular small
kappa_delta in C645g. For each fixed delta, eta and C, the question is
whether there exist c_(delta,eta,C)>0 and an integer N_(delta,eta,C)
such that every admissible family with n>=N_(delta,eta,C) satisfies

    ||H_q|| >= c_(delta,eta,C) exp(-delta*n/8).

No assertion of this claim, its negation, a witness construction or
even a better bound is made here. The old general estimate with a
census-dependent exponential cost does not by itself answer this
question at arbitrary C. The proposed new ingredient is directional
pole support, potentially tested through a one-sided Cauchy-transform
or residue functional while retaining the inverse-grid phases. Merely
changing the constant in the old absolute estimate is not a new test.

## Relevance, inputs and failure comparison

Main gap: actual-Xi signs at unbounded heights/all-degree mixed
positivity. C645h's verified synthetic boundary transfer makes the
very small census coefficient a concrete bottleneck: an O(log height)
count alone is insufficient at n=floor(log height). A successful
one-sided estimate might permit ordinary linear census constants for
a suitably selected rightmost pole, before attempting a boundary
upper-bound comparison. This is a plausible conditional use, not an
assertion that such a selection or useful upper bound is available.

Essential local inputs for a later test are C645g's exact symbol and
audited bound; C645h's principal-part application supplies the downstream
interpretation. L645 is only the conditional finite-Pick realization
context. No hypothesis that the actual K_n is positive is proved.
C645d's exact scalar cancellation must remain a comparison: one-sided
support must not simply be asserted to remove its mechanism, and
complex amplitudes must not be replaced by positive residues. C645b's
envelope stop is also retained. No positive scalar sum, full spectral
bound, actual-Xi realization or novelty is inferred from this nomination.

Unresolved actual-Xi assumptions include selection of an anchor
rightmost among all poles in the relevant disk at its own height,
boundary clearance, a complete census with a usable fixed coefficient,
interpolation from any temporary positivity premise, and a strictly
smaller independent boundary upper bound. A zero maximizing its real
part in an unrelated rectangle does not automatically meet the disk
selection requirement. No global maximum of zero real parts is assumed.

## Next review and later discriminating test

The next turn is a source comparison, reusing the ready general theory
and retrieving only needed primary one-sided support results and proof
cases. Search both operator terminology and positive-residue simple
partial fractions/Cauchy transforms. Compare the exact complex weights,
circle norm, arbitrary close poles, integer residues and dependence on
C, delta, eta and n. Record a matching known theorem as an import;
an unevaluated norm identity is not a quantitative answer. Unknown
Mathlib coverage remains unknown. No cross-notebook input is required.

If coverage is sufficient and leaves a concrete mathematical gap,
nominate one subsequent proof_attempt/creative: use the directional
support constraint to prove the displayed half-exponent statement or
construct a family at some fixed delta, eta, C with
exp(delta*n/8)||H_q|| tending to zero. The latter would decisively stop
that universal claim. Finite numerical samples, failure of the old
absolute estimate and scalar cancellation alone do not decide it.
Require a materially refined mechanism after an unsuccessful attempt.

The reason for that potential creative routing is precise: replacing
the restrictive census coefficient by geometric information could
remove one obstacle to applying the verified residual detector at
logarithmic grid size. It needs a new directional functional or a
counterfamily, rather than another audit or a reproof of Nehari/AAK.
Essential changed-scope coverage was the blocker at nomination. The
completed review below now supports the precise COVERED_TARGET for a
later invocation, subject to the supervisor's separate approval of this
newly completed assessment. No mathematical attempt occurred here.

## Completed source comparison — 1 November 2026

### Search scope and local failures

Queries actually issued:

- `simple partial fractions poles half plane lower norm positive residues Danchenko weighted Blaschke`
- `Hankel operator Cauchy transform measure complex weight segment lower bound rational approximation`
- `"Quadrature formulas with variable nodes" Chunaev Danchenko arxiv`
- `"simple partial fractions" "half-plane" "norm" Blaschke Chunaev`
- `"Hankel" "Cauchy transform" "half-plane" positive measure lower bound`
- `"Hankel" "Blaschke" "positive residues" lower bound`
- `"simple partial fractions" "weighted" "half-plane" lower estimates`

Read C645g's exact definitions and census-cost proof (1)–(21), C645h's
hypotheses/transfer conclusion, C645d's hypotheses and construction
scope, C645b's envelope conclusion, and L645's conditional Pick
context. Reused the completed full-pole and sparse-census assessments.
The targeted local search did not identify another assessment of this
directional family. C645d and its recorded inverse-Blaschke stop do
not establish the new support condition or disprove an operator bound.
C645g already avoids scalar cancellation but pays exp(-A_delta*m);
merely reusing that estimate at larger C does not answer this target.
The C645b upper-envelope stop remains a separate downstream obstacle.
No cross-notebook input was used.

### Newly inspected primary results

P. Chunaev and V. Danchenko, *Quadrature formulas with variable nodes
and Jackson–Nikolskii inequalities for rational functions*, J. Approx.
Theory **228** (2018), 1–20,
[DOI 10.1016/j.jat.2017.12.004](https://doi.org/10.1016/j.jat.2017.12.004).
Inspected version: [arXiv:1611.03485v2](https://arxiv.org/pdf/1611.03485v2),
9 January 2018. Page references here refer to this 18-page version.
Theorem 4.4/(4.6)–(4.7), pp.12–13, treats an unweighted SPF
rho_L=sum_(k=1)^L 1/(z-z_k), all poles strictly in one half-plane;
repeated locations are allowed. At p=2 its stated ratio satisfies

    1/L <= 2*pi*||rho_L||_infinity / ||rho_L||_2^2 <= 2.

Read its proof's upper/lower cases and sharpness examples. The key
identity uses Im(rho_L) with one sign. Theorem 5.2/(5.2), p.15,
assumes poles in a sector |arg(z_k)-pi|<alpha<pi/2 and controls norms
on the positive ray with weight x^(-1/2); its proof uses aligned real
parts. Neither statement allows the weights in our q. Theorem
3.1/(3.1), p.7, covers arbitrary rational functions without circle
poles: a boundary value divided by its pole-density factor bounds
the circle integral from below. Its proof selects one positive
quadrature summand. It supplies no uniform nonzero boundary value.
These are source comparisons, not new applications or proofs.

M. Yattselev, *On the multiplicity of singular values of Hankel operators
whose symbol is a Cauchy transform on a segment*, J. Operator Theory
**61:2** (2009), 239–251,
[journal PDF](https://jot.theta.ro/jot/archive/2009-061-002/2009-061-002-002.pdf).
Read the measure definition and Theorem 2.1/(2.6), pp.243–244,
Lemma B/(3.2), p.246, and the proof use (4.12)–(4.22), pp.248–249.
The theorem assumes infinitely supported complex measure on (-1,1)
with argument of bounded variation, plus a rational summand without
circle poles. It bounds singular-value multiplicities, not sizes.
The proof uses orthogonality and argument variation on a real interval.
Our finite planar support and n-dependent complex weights do not meet
these hypotheses. Treating all of q as the rational summand supplies
no bound on its norm. This result therefore provides no import of the
desired inequality.

### Applicability and decision

The saved BCQ/AAK assessment remains adequate for the operator
convention, finite rational model and norm/distance identity. The
saved Gorin comparison remains adequate for unweighted real-line
lower bounds. No reproof or repeated general-theory search is needed.

For the exact target, the points a range over a two-dimensional disk
cap, not a real segment. Positive integers r_a specify simple-pole
residues before division; q has residues r_a*B_n(x)/(R*B_n(a)).
The new support hypothesis does not itself assert that these numbers
are positive or lie in a fixed phase sector. Establishing a useful
phase-sensitive functional is precisely a possible later task, not
a consequence imported from a source. A rotation or circle-to-line
map would also need its weights and norm transformed and controlled;
no such specialization has been justified here.

There is consequently no inspected quantitative conclusion with the
required joint uniformity: fixed delta,eta,C; all large n; no lower
bound on pairwise pole distances; arbitrary positive integer residues
with M<=C*n; and the exact normalized H2-to-H2_minus operator norm.
This is a bounded coverage finding, not proof that no matching theorem
exists. No new lemma, numerical calculation or mathematical script was
produced, and no norm inequality beyond the cited sources was derived.
Full matching Mathlib coverage is not checked.

Additional search leads were Borodin's unbounded-domain SPF approximation,
alternance/weighted-ray estimates, and derivative-density papers.
They were not inspected as theorem inputs and are not claimed to
settle this fixed-clearance weighted circle problem. None is an
identified essential missing dependency for the bounded test. Their
titles/snippets are discovery leads only.

Decision: EXPLORE for the exact COVERED_TARGET, with a separate
supervisor approval before research. Try the directional support
mechanism while retaining inverse-grid phases, rather than repeating
the absolute census-cost proof. A rigorous uniform lower bound at
exp(-delta*n/8), or a fixed-delta,eta,C asymptotic family violating
it, is decisive evidence. If neither emerges, save partial reasoning
as EXPLORATION and require a refined mechanism before repeating.
Scalar cancellation, a small least singular value, a finite numerical
sample, or failure of a candidate functional alone is not a disproof
of the largest-singular-value claim. The actual-Xi gaps listed above
remain open even if this synthetic test succeeds.
