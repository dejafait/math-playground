# Collective corrected-carrier bound: completed source comparison

TARGET: Assess whether a uniform complete-energy lower bound for arbitrary finite separated-carrier spans of L744's corrected profiles is covered by existing finite-band or nonharmonic Fourier results.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 290 compared the exact saved target with primary continuous separated-frequency estimates and the previously assessed finite-band reduction; exact queries, inspected passages and limitations are below. No matching complete corrected-span theorem was found; no novelty follows.
SOURCE_EVIDENCE: Montgomery--Vaughan, Hilbert's inequality (1974), Theorem 2 and Corollary 2, pp.74-75, proof p.82; author-hosted Multiplicative Number Theory II draft, Theorems G.3/G.14 and proofs, pp.399-400/422-425. Reused and narrowly rechecked Zhu 2608.24827v2 Theorem 1.1, Section 4 and Lemma 6.1/proof; reuse L744's audited DLMF specialization without browsing it again.
COMPARISON: Continuous frame normalization has standard source coverage; the exact smooth weight, finite-rank cell correction and collective logarithmic deficit still require a local specialization. Zhu's generic reduction does not itself bound leakage of this supported span. Import the standard inputs; do not reproduce a generic finite-band theorem or claim a new sign mechanism.
GAP: The proposed complete-energy inequality remains unproved. Uniform corrected normalization and collective Fourier leakage, with no cardinality or maximum-carrier dependence, are the remaining application obligations. Bounded-frequency signs and support enlargement remain independent.
REASON: The source screen resolves the previously missing continuous-frame scope and distinguishes a useful paid trial-space estimate from the already available reduction. One bounded specialization is justified, subject to separate approval of its new continuation assessment; no mathematical derivation was performed this turn.
SCOPE: Fixed K,chi and one fixed smooth unit cell train w; all finite real Delta-separated carrier sets outside [-T,T], arbitrary complex coefficients, both signs, unbounded maximum carrier. Source comparison only; no lemma or mathematical script writes.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED: exact continuous frame hypotheses and collective leakage coverage had not been inspected. This is the required missing-coverage review, not a refresh of L744's ready individual-modulation assessment.

## Original nomination, preserved as the pre-review target

The following proposal and questions were recorded before step 290; their
then-pending source status is superseded by the completed comparison below.

## Exact proposed test, not a theorem

Fix K>=2, ell=log(3)/2, L=K ell, chi and a single
w in L744's family (1). Fix w and its finite H2 norm before any
limit. Use exactly v_(t,w) from L744 (3), including its complex-linear
cell correction. Let {t_r} be any finite real carrier set satisfying
|t_r|>=T and |t_r-t_s|>=Delta for r!=s. For arbitrary complex
coefficients form V=sum_r c_r v_(t_r,w).

The proposed statement to assess is the existence of Delta0 and,
for each fixed Delta>=Delta0, T0 and epsilon(T)>=0 tending to zero,
depending only on K,w,chi,Delta, such that every such finite set and
every nonzero V satisfy, for T>=T0,

    E_L(V)/||V||_2^2 >= log(T/(2pi)) - Cprime - epsilon(T),
    Cprime = 2 sum_(2<=n<exp(L)) Lambda(n)/sqrt(n).

Uniformity in the number of carriers, their maximum magnitude and
the coefficients is essential. No claim is made that the unmodulated
envelope of V has a bounded H2 norm; applying L744 with an envelope
bound that grows with the carrier set would not prove this statement.
Every V retains the exact cell moment constraints by linearity, but
that fact alone supplies no energy lower bound or lower norm bound.
The all-complex pole and full-prime conventions of L744 (6) must be
retained throughout any future specialization.

## Source comparison and decision test

First compare this exact scope with the already inspected Zhu finite-band
reduction in
[the parent comparison](2026-11-04-joint-energy-mechanism-nomination.md).
Determine whether it already covers the needed uniform supported-span
estimate. Inspect primary continuous nonharmonic Fourier/Riesz-sequence
statements only as needed for the remaining normalization and leakage
questions; discrete angular-sampling theorems are not automatically
applicable. Their coverage is presently unassessed. No source is claimed
inaccessible, so this is not a repeated access-recovery task.

The materially changed quantity is the entire corrected span with
unbounded finite dimension, rather than the L2 arithmetic supremum or
one modulated test. The existing generic finite-band reduction is a
possible stronger input, not a new mechanism to reproduce. Preserve
the prime-only Rayleigh stop and the generic-source normalization stop;
neither is overturned. Do not use L742's RH-conditional spectral
conclusion or an unreplayed source positivity computation.

Continue to mathematics only if primary coverage resolves the exact
frame/normalization hypotheses and leaves a concrete necessary
specialization with plausible use as a paid trial-space component in
a finite-window lower certificate. Import a matching or stronger theorem
instead of rederiving it. Park the proposed development if it merely
duplicates an available reduction without an additional application,
or if its useful version requires an unproved sign or a growing-support
claim. A bound whose constants depend on the number of carriers fails
the stated test. This is one bounded source comparison, not approval
for either a new proof or an expanded discovery program.

Essential local inputs for a later attempt would be L740's complete
generator, L741's smooth normalization, L743's fixed moment inverse and
L744's audited formulas. The proposed collective estimate is unresolved.
Even if obtained, bounded-frequency signs, moment complements, arbitrary
envelopes and uniform support enlargement remain independent gaps.
No justified creative central-sign mechanism is currently identified:
this paid high-frequency question does not sign the unresolved low-energy
block. Do not label a standard Fourier specialization creative. Full
matching Mathlib coverage has not been checked.

## Completed comparison: 4 November 2026, step 290

The main gap is unconditional actual-Xi mixed positivity. The exact
intermediate target above would pay a whole high-carrier trial space,
rather than isolated vectors, in a finite-window lower certificate.
It would still leave the signed low-frequency block, moment complements,
and control as K grows unpaid. The target has not been weakened to a
fixed number of carriers or a bounded maximum carrier.

### Primary continuous normalization input

[H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*,
J. London Math. Soc. (2) 8 (1974), 73-82,
DOI 10.1112/jlms/s2-8.1.73](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
Theorem 2 (1.6), Corollary 2 (1.8), pp.74-75, applies to any finite
set of distinct real frequencies with minimum gap delta>0 and arbitrary
complex coefficients. It gives

    integral_0^U |sum_r a_r exp(i lambda_r x)|^2 dx
      = (U + 2*pi*theta/delta) sum_r |a_r|^2,  |theta|<=1.

Here U>0; hence a positive lower constant requires U>2*pi/delta.
No sign or magnitude restriction is placed on the frequencies. Read
the complete Section 4 argument on p.82: the real-line theorem follows
by scaling, and the corollary uses two Hilbert-form bounds. This is a
continuous, cardinality-independent input, not discrete sampling.
Its theorem does not include our weight w or cell correction.

For hypothesis matching, a nonzero fixed smooth w has an interval on
which its modulus stays away from zero. The source interval requirement
can therefore be met by choosing a sufficiently large fixed Delta.
This identifies applicable hypotheses; no weighted or corrected norm
estimate is proved here. Import the theorem in a later canonical proof,
rather than reprove Ingham's inequality.

The [same authors' *Multiplicative Number Theory II*, author-hosted
draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
accessed 4 November 2026 (undated draft; no publication status assumed),
Theorem G.14, printed p.422, confirms the uniform-gap Hilbert bound
pi/delta for complex coefficients; its proof was read through p.425.
Theorem G.3, pp.399-400, gives the finite rectangular matrix norm bound
by the square root of the product of maximum absolute row and column
sums, with its Cauchy--Schwarz proof. These support normalization and
collective Gram estimates; they do not assert the continuous logarithmic
leakage bound. Passing to any integral-kernel variant must be justified,
not attributed to a finite-matrix theorem without explanation. No use
of the draft's variable-gap optimal-constant discussion is needed.

### Comparison with the known stronger reduction

Reuse [the parent comparison](2026-11-04-joint-energy-mechanism-nomination.md).
Narrowly rechecked [Zhu, arXiv:2608.24827v2, 2 September 2026](https://arxiv.org/html/2608.24827v2),
Theorem 1.1 (4), complete Section 4, and Lemma 6.1 with proof and
following paragraph. It gives a finite-band lower reduction for compact
support, with an explicit tail floor, retained-block requirement and
paid coupling; parity retains the negative odd pole and complex tests.
Our length-L support corresponds to source half-width L/2. The new
question is whether this particular supported corrected span has a
small normalized low-frequency deficit. Large carrier labels are not
an exact Fourier cutoff, and the reduction supplies no such estimate.
Thus the proposed trial-space estimate is not a direct theorem import,
although its high-frequency floor is already standard. No source
positivity computation was replayed or used.

### Scope decision and bounded continuation

L744 (3)/(6)/(8)/(12)-(13) are the exact local conventions inspected.
One cannot sum its individual Rayleigh lower bounds: cross terms and
the denominator belong to the entire span. A total logarithmic norm
bound involving the largest carrier would also miss the stated
uniformity. A possible proof organization is to estimate only the
positive part of the deficit below log(T/(2*pi)), rather than control
the entire unbounded positive energy. This is a proposed application
obligation, not an estimate established or approved by this review.

The source coverage is adequate for one standard-mechanism
specialization. Its separate [continuation assessment](2026-11-04-collective-corrected-carrier-span-specialization.md)
keeps the exact inequality, all quantifiers, local inputs and the
continuation/abandonment test. It is newly written and requires the
supervisor's separate approval before research. No claimed discovery
beyond the checked sources, new central-sign mechanism or RH candidate
results. Full matching Mathlib coverage is not checked.

Scoped duplicate/failure check: reused the parent's search and read
the generic-source scope stop and prime-only Rayleigh stop in ATTEMPTS.
L743's audited arithmetic supremum equality is unchanged. Neither a
moment-only arithmetic saving nor an unknown complement sign is used.
The signed Gram-dual/slope failures remain contrasts, not inputs.

Queries actually run included `Ingham 1936 non harmonic Fourier series
separated frequencies theorem 2 pi gap integral`, `nonharmonic Fourier
Riesz sequence weighted smooth window separated frequencies Ingham
logarithmic energy`, `Montgomery Vaughan Hilbert inequality 1974 pdf
separated real numbers integral`, `"modulations" "Riesz sequence"
"window" separated`, `"separated" "logarithmic" "Fourier" "Ingham"`,
`"corrected" "carrier" "Weil" "span"`, and narrower smooth-weight/
Corollary 2 searches. Survey, Gabor-frame and discrete-sampling hits
are leads only; no theorem from them is imported. The original Ingham
paper was not inspected and is unnecessary because the primary
continuous result above suffices. Publisher access and a local PDF
download failed; the author-hosted primary PDF and corroborating
author draft were readable, so no essential source is blocked.

PROOF.md and DAG.md are unchanged: this review changes coverage and
routing, not the mathematical argument.
