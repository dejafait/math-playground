# Growing-window signed mixed pairing: completed source gate

TARGET: Establish or refute a uniform O_(M0,M1,chi)(T^-2 log T) bound for the full Hermitian pairing of a unit cell-neutral u in F_(K(t),M0) with C744n's v_(t,w), w in F_(K(t),M1).
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step499 searched exact neutral/corrected Weil mixed pairings, low/high coupling and separated-frequency Sobolev estimates; compared L744/C744n, L745 and the two recorded scope stops. Read the primary statements and proof cases identified below. No full matching theorem was located in this bounded search; no originality inference.
SOURCE_EVIDENCE: Read Vasy Math172 Fourier notes pp1-2, Def1 p3, and Lem0.4/proof p13 (including page image); Zhu2608.24827v2 Thm1.1, Lem3.1/proof, Section4(12)-(13), Lem6.1/proof and its following paragraph; screened bramble_trace Paper143/v1 Thm1/(1)-(10). Reuse inspected DLMF5.11.2/5.11(ii), Rosser--Schoenfeld1962 Thm12/(3.35), and audited C744n quantitative estimates.
COMPARISON: The exact corrected two-profile statement is not a direct import from the inspected sources. Standard Fourier differentiation, Plancherel and Cauchy--Schwarz cover the analytic tools; L744/C744n cover the complete scalar, correction and entire arithmetic mass. Zhu's Legendre coupling and Paper143's restricted rational coupling families do not supply this mixed estimate. A standard-mechanism specialization is justified for a later bounded attempt, with no sign theorem inferred.
GAP: Prove or refute the stated uniform rate with both profiles varying, both signs, the full complex Hermitian pairing, all prime powers and no K-dependent constant. The weighted Fourier overlap and delay-pairing specialization remain unproved. Low-block signs, general profiles and assembly remain independent gaps.
REASON: This separate literature-only turn completes the gate for step498's unchanged target; all essential supporting inputs are accessible. No target estimate, new lemma, mathematical script or central-sign mechanism is derived or certified here. The future proof must supply the identified applicability work rather than reprove the named Fourier or arithmetic theorems.
SCOPE: Fixed finite M0,M1>=1 and chi as in C744n; ell=log(3)/2, T=|t|, K(t)=floor(log log T/ell)>=2, L=K(t)ell, both signs of t, complex smooth cell trains, original unweighted norms. No other support rate or all-frequency decomposition is nominated.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED for this new signed pairing; diagonal moving-window coverage did not assess its two-profile quantifiers or the applicable coupling proof cases. This turn is that required source comparison.

## Exact proposed test, not a result

Use F_(K,M) exactly as in L744(1) and C744n's unchanged correction
v_(t,w). In addition to u in F_(K(t),M0), require

    integral_0^ell e^(sigma s/2) u_j(s) ds = 0
    for every j and sigma in {+1,-1}.

Both u and w have unit L2 norm before the correction to w. Their
H2 bounds are fixed separately, and both may vary arbitrarily with t
within these constraints. Empty families make no existence assertion.
Define the full Hermitian polarization of L740's energy by

    mathcal E_L(a,b) = -( <A_L a,b> + <a,A_L b> )/2,

with the first-slot-linear inner product. On the diagonal this is
E_L(a). The proposed bound is: there exist C<infinity and T0,
depending only on M0,M1,chi (ell fixed), such that

    |mathcal E_(L(t))(u,v_(t,w))| <= C log(T)/T^2

for every admitted pair and every T=|t|>=T0, for both carrier signs.
This is a target, not a verified estimate, proof sketch or novelty claim.
No sign of E_L(u) is assumed for the estimate. Any later absorption
argument would need an independently proved lower margin for the low
block; no such input is supplied here. Full matching Mathlib coverage
is unchecked.

## Nomination-time source gate and retained discriminating test

At nomination, the next turn was literature-only (completed in step499
below). Its instructions were to reuse the parent's primary scalar
and arithmetic coverage, then compare the exact mixed statement with
standard separated-frequency Sobolev estimates and the complete-form
low/high coupling bounds in the cited Zhu source. Read the applicable
primary hypotheses and proof cases; a diagonal asymptotic or generic
Schur identity is not the requested mixed estimate. Check stronger
known conclusions, local duplicates and the specific stops below.
Classify any eventual application honestly as a known specialization
if that is what the sources support. Do not certify a new creative
mechanism merely because the target has not yet been checked.

A later authorized mathematical attempt would have to establish the
stated uniform rate for the whole signed pairing, or exhibit a precise
obstruction to it. Bounds for individual fixed u, a prime-only form,
constants growing with K, or a bound assuming the desired full-energy
positivity would not pass. A failure of this sufficient rate would
not be a negative Weil vector. A source match should be imported with
its necessary applicability argument rather than reproved.

The plausible use is quantitative control of an actual interaction
between a paid high-carrier class and a separate low block. It leaves
that low block's sign, non-neutral components, arbitrary-profile
coverage and the sum of many interactions unresolved. It does not
reopen the false nonnegative corrected-IMS defect in L750 or the
RH-conditional absolute summability obstruction in L742.

The concrete new input for reconsidering the old carrier-span scope
limit is C744n's audited uniformity in K(t), together with the proposed
uniform H2 restriction on the other profile. The old stop itself is
preserved in `ATTEMPTS/2026-11-04-carrier-span-general-sign-scope-limit.md`.
The complete-form comparison is retained in
`drafts/literature/2026-11-04-joint-energy-mechanism-nomination.md`.
No general-sign inference from the carrier span is proposed.

This nomination is not protected creative work: the likely oscillatory
mechanism is standard, pending comparison. No independently justified
new mechanism for the central low-block sign has emerged from this
bounded audit. The exact mixed estimate is selected as an independent
assembly gap rather than repeating the completed C744n audit. A genuinely
new central mechanism should be prioritized if the source comparison
identifies one with a bounded test; none is approved in this document.

## Completed comparison — 11 November 2026, step499

This is the separate literature gate for the unchanged TARGET above.
Its decision is SPECIALIZE, authorizing a later bounded attempt, not
certifying the rate. The main gap remains L030-L032/C032a actual-Xi
positivity. The intermediate target pays one actual signed interaction;
its plausible use is a later low/high certificate with an independently
proved low-block margin. Neither that margin nor a general decomposition
is supplied. The completed work is a source comparison, not a mathematical
advance or a claim of originality.

### Primary comparisons and applicability

**Fourier tools.** Andras Vasy, *Math 172: The Fourier Transform — Basic
Properties and the Inversion Formula*,
[author-hosted notes](https://math.stanford.edu/~andras/172-4.pdf),
undated version retrieved 11 November 2026: printed pp1-2 define the
transform with phase exp(-ix xi), prove its L1-to-L-infinity bound and
derive F(partial_j f)=i xi_j F(f) by integration by parts. The stated
derivative hypotheses there are C1 and polynomial decay of f and its
first derivatives of exponent exceeding the dimension. Definition1,
p3, identifies the Schwartz class. Lemma0.4 and its proof, printed p13,
give the complex Plancherel identity with measure dxi/(2pi) in dimension
one. The page image confirms the conjugations lost in text extraction.
These hypotheses cover each smooth compactly supported zero extension
in the proposed target. They do not impose a constant support length
or prescribe a profile-dependent convergence rate.

These are imported supporting identities, not a theorem of the exact
mixed rate. The later application must use only the prescribed global
H2 norms, not unspecified higher Schwartz seminorms or L1 norms growing
with the support. No reproof of Plancherel or Fourier differentiation
is justified. Product differentiation and Cauchy--Schwarz are standard
supporting rules; their quantitative use for translated products is
part of the unproved specialization.

**Complete-form coupling comparison.** Xuefeng Zhu,
[*Weil positivity in compact windows: a finite reduction, certified
two-sided bounds, and a Landau–Widom decay law*, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
arXiv version dated 2 September 2026, Theorem1.1 requires positive
beta*=log(Tsharp/(2pi))-1/Tsharp-A_a for support [-a,a].
Section4(12)-(13) bounds the coupling from retained Legendre orders to
their discarded tail by explicit row and column sums. Its estimates
depend on a,Tsharp and the Legendre cut; they do not concern arbitrary
bounded-H2 profiles and their carrier separation. Lemma3.1/proof is
a one-sided symbol envelope, insufficient for an absolute mixed form.
Lemma6.1/proof and the paragraph following it retain the negative odd
pole and explain complex tests. Our interval length corresponds to
2a. These inspected cases support the normalization comparison but do
not give the TARGET or its simultaneous quantifiers. No computational
certificate or theorem of all-window positivity is imported.

**A newer stronger-looking mixed-Gram lead.** The search returned
bramble_trace's [Paper143/v1, *Rational Schur sources for the Weil prime
operator: uniform image and mixed Gram bounds*](https://rstation.ai/problems/riemann_hypothesis/papers/143/v1),
10 November 2026. Read Theorem1 and definitions (1)-(10); this is
statement screening, not a proof audit. It requires prime support
endpoints P, common rational degree d and pole gap 1-kappa for every
linear combination, with N>=P^(3+eta)d^6/(1-kappa)^3. Its mixed Gram
is for those finite coupling-source images and weighted sequence norms.
The present arbitrary complex smooth H2 cell trains are not identified
with those rational images, and the floor cutoff is not restricted to
prime endpoints. The theorem therefore supplies no direct import here.
Its proof and cited rational derivative theorems are not used; no
coverage or sign conclusion is inferred from the title or author review.

**Reused essential coverage.** The parent's inspected DLMF5.11.2 and
5.11(ii) remainder applies on z=1/4+i xi/2, in the right half-plane;
L744(8) already records its global scalar majorant without a spurious
logarithmic singularity at zero. C744n(4)-(5) already records the
K-independent H2 correction cost; its (7)-(8) bounds the full arithmetic
mass using Rosser--Schoenfeld1962 Theorem12/(3.35), printed p71, and
finite Abel summation, including all prime powers and the factor two.
Reuse those exact estimates and their citations, rather than a new
asymptotic import or a repeated source-computation audit. No new
zero-free region, arithmetic improvement, or RH premise is needed.

### Remaining specialization obligations, not derived estimates

The sources make a standard-mechanism attempt appropriate; they do not
settle whether it succeeds. Its work is confined to the exact TARGET.

- Polarize the complete L744(6) on the actual smooth domain and check
  the first-slot-linear convention. Verify both exponential moments in
  the mixed pole term; do not replace complex poles by a modulus square
  or infer mixed cancellation solely from one diagonal identity.
- Establish the logarithmically weighted Fourier overlap for two
  varying H2 envelopes. These envelopes are not band-limited: a theorem
  assuming disjoint Fourier supports does not apply. Frequencies near
  zero and tails beyond the carrier must be retained with constants
  independent of K and both profile choices.
- Estimate both translated pairings in every prime-power delay using
  the zero extensions and only derivatives through order two. An L2
  operator-norm bound alone omits the requested carrier decay. Endpoint
  delay and cell boundaries must produce no unaccounted terms. Sum the
  full coefficients only after a bound uniform in the delay is justified.
- Retain the whole correction in the scalar and arithmetic pairings,
  using its already proved K-independent estimate. All estimates must
  precede the stipulated K(t) substitution and hold for t of both signs.
  A fixed-profile Riemann–Lebesgue limit is insufficient.

No intermediate inequality in this list is asserted or proved here.
The precise continuation/abandonment test remains the displayed
O_(M0,M1,chi)(T^-2 log T) bound for every admitted pair after one
parameter-dependent onset. A fixed-K result, dependence on uncontrolled
derivatives, a prime-only estimate or use of low-block positivity fails
the test. An obstruction to the sufficient rate would not refute RH or
produce a negative Weil vector. Preserve partial reasoning if a bounded
attempt cannot close the estimate; require a materially refined input
before repeating a failed mechanism.

### Duplicate and failure check; search limits

Read the retained joint-energy comparison and the generic-source and
carrier-span ATTEMPTS records named above. L744's scalar/correction
cross terms concern one profile and its correction. L745(15)-(17) pay
finite separated carriers from one fixed profile at fixed K, with
constants depending on that profile and support. Neither is the proposed
arbitrary low-profile pairing. C744n supplies the newly audited support
uniformity for its own diagonal class, not a mixture sign. These are
useful inputs and scope boundaries, not reasons to redo their audits.
L742's conditional summability and L750's corrected-IMS stops remain
retained contrasts; no claim here removes either obstruction.

Exact queries included `"Weil" "quadratic form" "mixed" "Sobolev"`,
`"separated frequencies" "Sobolev" bilinear logarithmic multiplier`,
`"Weil" "modulation" "mixed" "form"`,
`"Weil" "neutral" "pairing"`,
`"Fourier transform" "W^{2,1}" decay integration parts`,
`"Weil quadratic form" "low" "high" "coupling"`, and
`"Weil" "Sobolev" "modulation" logarithmic`.
The neutral-pairing query mostly returned elliptic-curve material,
which is irrelevant. General PDE bilinear estimates and the
scale-resolved-Weil GitHub result remain unread leads, not theorem
inputs or certified comparisons. Two Gressman author-page requests
returned HTTP403; Vasy's accessible notes supplied the required primary
Fourier statements, so there is no essential source blocker and no
reason to repeat access attempts. This bounded search does not certify
novelty or exclude other treatments.

Full matching Mathlib coverage remains unchecked; the supporting Fourier
identities do not formalize this entire corrected-family estimate.
No lemma, script, DAG row or PROOF.md argument changes in this turn.
No justified creative central-sign mechanism emerged: the missing
independent low-block margin still blocks that nomination. Route the
unchanged, now assessed target to one standard-mechanism mathematical
attempt, classified REPRODUCTION if established by this specialization.
