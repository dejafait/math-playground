# Direct-product signed truncation: completed separate source review

TARGET: Test whether truncating L471 (6) to all Xi zeros with |t-gamma|<=h, h=(log T)^(-1/4), changes its amplitude-weighted negative-part integral by O(T(log T)^(5/2)), with zero-safe extension and all multiplicities.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the separate exact-target comparison using L471, L467, L464 Section 3, the saved negative-part/signed-background assessments and displacement-mass stop; bounded web searches below found no matching weighted clipped integral theorem. Inspected the new Najnudel--Nikeghbali v1 Theorem 1.1 lead and distinguished its statistic; no novelty inference.
SOURCE_EVIDENCE: Reused the saved primary inspections and local application audits; reopened Csordas arXiv:1309.0055v2 Definition 1.1 and Proposition 2.2 proof (2.3), Bui--Hall arXiv:2304.05178v1 definition/(1), and Bellotti--Wong arXiv:2412.15470v2 Theorem 1.1/Section 5. Read Najnudel--Nikeghbali arXiv:2609.15862v1 Section 1/Theorem 1.1 only for comparison, not import.
COMPARISON: The exact series, unconditional multiplicity-counted closed unit-shell count and zeroth Hardy moment cover the inputs to a direct tail test; L464 already treats both fixed-radius reciprocal-square tails. A shrinking cutoff, its amplitude weight and clipping are the remaining specialization, not a new claimed source theorem. The projected-ordinate first-power Cauchy-law result does not cover this statistic.
GAP: Essential source coverage is ready for this bounded specialization; the O(T(log T)^(5/2)) error, zero-safe truncated expression and uniform cutoff treatment remain unproved mathematical tasks. No control of N_h(T), individual signs, higher signs or RH is approved.
REASON: This separate literature turn approves exactly the saved test for a later RESEARCH / REPRODUCTION calculation. Cite the known inputs and prove only their changed-cutoff/application steps; do not reprove the sources or differentiate Selberg's remainder. No new estimate, lemma or mathematical script is produced here.
SCOPE: Actual Xi; L018/L024/L465 through L471, L467 and L471's zeroth Hardy moment; L464 Section 3 supplies a reusable fixed-radius shell comparison. Retain all zeros, multiplicities and the exact amplitude. No RH, simplicity, separation, density saving, fixed-half-plane premise, short-interval asymptotic or differentiated remainder. This separate approval covers only the exact TARGET above.
LITERATURE_REASON: This exact target was outside the completed microscopic Selberg comparison; the invocation-start REVIEW_REQUIRED nomination required this separate overlap/source approval. The missing comparison is now completed, so the next turn defaults to mathematics.

## Original nomination and retained test

The following nomination is retained as the test specification; its
requests for approval are discharged by the completed review below.

The main gap is the unproved actual-Xi initial signs at unbounded
heights and all-degree mixed positivity. The intermediate target is
the displayed approximation error at a scale strictly below T(log T)^3.
Its plausible downstream use is an explicit signed local expression
for a later arithmetic cancellation test. It does not produce that test.

To fix the nomination precisely, use L471's notation and let z run
over all Xi zeros, with multiplicity nu_z and gamma=Re z. For T large,
set h=(log T)^(-1/4) and propose

    K_h(t)=sum_(|t-Re z|<=h) nu_z/(t-z)^2,
    N_h(T)=integral_T^(2T) (-Xi(t)^2 K_h(t)/A(t)^2)_+ dt.

Conjugate zeros must be selected together. At a real zero the
product Xi(t)^2 K_h(t), rather than K_h(t) alone, needs a justified
continuous extension. The proposed threshold is

    |N(T)-N_h(T)| <= C T(log T)^(5/2)

for one height-independent C beyond an absolute onset. This is a
target, not a proved inequality or an assumed bound. Closed cutoff
endpoints, negative-ordinate zeros, multiple zeros and both tails
must be handled, with no assertion of microscopic spacing.

The review should first reuse the saved exact product, count and
zeroth-moment coverage and check whether this statement is already
recorded or follows by a fully covered specialization. Only missing
essential evidence warrants further external reading. It must not
approve arithmetic cancellation, a smaller window, or an all-degree
positivity claim by association.

The later mathematical continuation test is the precise error bound
above. If only the full T(log T)^3 scale is supported, or a required
uniform/zero-safe step fails, preserve that evidence and park this
localization regime. If it passes, record only an approximation input;
the sign problem for N_h remains an independent gap requiring its own
bounded mechanism and source gate. This is routine specialization,
not proof_attempt/creative. A creative central-gap nomination needs
a concrete arithmetic cancellation test not currently supplied by
Selberg's expansion or the existing moment laws.

Mathlib: full matching coverage is unchecked. No mathematical script,
canonical lemma, DAG edge or new mathematical result is created here.

## Completed separate comparison, 29 October 2026

Verdict: SPECIALIZE, ready for the exact TARGET. Outcome EXPLORATION,
LITERATURE / NOVELTY_UNCHECKED. This establishes source scope, not the
proposed estimate or progress beyond the checked sources. The ensuing
calculation should be classified REPRODUCTION. No lemma, mathematical
script, DAG or PROOF.md change is made in this review.

### Reused primary coverage and exact hypotheses

1. [Csordas, arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/html/1309.0055v2),
   Definition 1.1 and Proposition 2.2 proof, (2.3), printed pp. 3--4.
   Reopened the product definition and the logarithmic-derivative
   identity. The displayed proposition additionally requires f(0)!=0,
   strip width one and a zero-free real-part interval longer than two;
   those sign hypotheses are not inputs to the identity application.
   L471 Section 1 already justifies its actual-Xi use from L024,
   including inverse-square convergence, zero quadratic parameter,
   conjugate pairing and zero orders. Reuse that local justification
   and its recorded application audit. The source supplies no weighted
   clipped truncation integral.

2. [Bellotti--Wong, arXiv:2412.15470v2, 7 July 2025](https://arxiv.org/pdf/2412.15470v2),
   Theorem 1.1, printed p. 1; Section 5, printed pp. 23--24.
   Rechecked the unconditional bound for every height >=e against
   L467's citation. Its first envelope is
   0.10076 log t+0.24460 log log t+8.08344 about
   t log(t/(2pi e))/(2pi). Reuse L467's audited all-height closed
   unit-shell specialization with constant 18, multiplicities and
   endpoint conventions. The source's computations/full manuscript
   are not independently rerun. This is a unit-shell input, not an
   assumption of proportional counts in intervals of length h.

3. [Bui--Hall, arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1),
   introduction's definition of Hardy Z and equation (1).
   Rechecked its fixed nonnegative derivative-order formula, using
   only orders (0,0) here; it is unconditional. L471 (8) already
   records the dyadic zeroth moment with the exact completion
   normalization supplied by L465. No shifted fourth moment,
   short-interval formula, quotient moment, derivative-error control
   or zero-conditioned moment is needed for the proposed tail test.
   The general moment proofs remain cited inputs, not independently
   audited here.

L464 Section 3, (6)--(9), was read specifically as a duplicate and
implementation comparison: it already sums fixed-radius positive and
negative ordinate reciprocal-square tails with multiplicities. Its
coefficient-tail conclusion is a different result. The present target
changes the cutoff to a shrinking window and asks about a clipped,
amplitude-weighted integral. This difference merits a local application
proof rather than a new claim about the standard shell method.

### Bounded discovery and stronger-result comparison

Queries actually used:

- `Riemann xi logarithmic derivative reciprocal square zeros truncation Hardy Z mean square`
- `"zeta" "zeros" "truncation" "logarithmic derivative" "unconditional"`
- `"xi" "negative part" "truncation" zeros`
- `"zeta" "reciprocal squares" "zeros" truncation`
- `"Hardy" "weighted" "zeros" "truncation" moment`

No matching theorem for the specified weighted negative-part error
was located in this bounded search. Nonprimary search hits were not
used as mathematical inputs. No absence or originality claim follows.

The new relevant primary lead was Joseph Najnudel and Ashkan Nikeghbali,
[*Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes
transforms*, arXiv:2609.15862v1, 14 September 2026](https://arxiv.org/html/2609.15862v1).
Read Section 1 through Theorem 1.1 and its definitions. For L=log T,
t uniform on [T/L,T], it uses projected ordinates
u=(gamma-t)L/(2pi) and the symmetric first-power sum over
0<|u|<=L^2, with multiplicities, proving an unconditional Cauchy limit.
Its comparison with the actual critical-line logarithmic derivative
requires H(T)=o(T), where H sums right-hand zero displacements through
height 2T. Neither that added hypothesis nor its limiting-distribution
statistic covers our unconditional weighted reciprocal-square clipped
integral. No result from this manuscript is imported. Sections 4, 7,
8 and Appendix A remain unread leads, unnecessary for this bounded
specialization because the required identity/count/moment inputs are
already available; no derivative of its truncation theorem is assumed.

### Failure comparison and remaining application obligations

The displacement-mass stop in
`ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`
concerns summing an entire pair-divided quotient after ordinary-moment
substitution. This target instead retains the signed local expression
and tests only the discarded tail. L475's global disk envelope and the
Selberg differentiated moving-cutoff remainder are also different
implementations. Their failures stay recorded and are not disproved
or repaired by this approval. L251/L472/L473 remain comparison
obstructions, not mathematical inputs to the tail test.

The next calculation must supply the uniform shrinking-cutoff tail
estimate from closed unit shells, explicitly include negative ordinates
and the remote positive tail, apply only the covered zeroth moment,
and justify clipping after amplitude multiplication. It must justify
the central-zero extension with arbitrary multiplicity. The hard
cutoff can switch membership elsewhere; do not demand or assert global
continuity across cutoff switches. Establish the needed measurability,
integrability and endpoint treatment instead. These are proof tasks,
not assertions established in this source review.

The retained continuation/abandonment test is precisely the proposed
O(T(log T)^(5/2)) bound above with one height-independent constant.
Success supplies only an approximation input for a later cancellation
test; a full-scale-only bound or failed extension parks this regime.
The independent estimate for N_h(T) remains absent. No concrete new
arithmetic cancellation mechanism has emerged from the inspected
sources, so discovery scheduling does not justify labeling this routine
specialization creative. Full matching Mathlib coverage remains unchecked.
