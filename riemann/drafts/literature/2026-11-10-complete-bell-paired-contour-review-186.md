# Complete Bell sum: completed paired-contour source comparison

TARGET: Assess source coverage for a paired-contour representation of L966's complete Bell sum, retaining the h-resolvent, and specify one n-uniform signed-cancellation test that avoids the L967/L969 pointwise stops.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step187 searched Li/Bell logarithmic-derivative contours, regularized resolvents, paired contours, angular prefixes and reflection positivity; scoped L966/Q_eta duplicate search found the existing representation, payment and audit assessments but no matching contour-prefix result. No novelty inference follows.
SOURCE_EVIDENCE: NIST DLMF v1.2.8, 1.9.30-31 and 2.4(iii)-(iv)/(2.4.10)-(2.4.16); Voros math/0404213v2 Sections2-3/(6)-(9) and the following RH-true hypothesis paragraph, and 2204.01036v2 Sections2.2-2.3/(13)-(20). Reused step159/164 Cauchy/product coverage and step171's precise Lagarias one-sided criterion assessment. Relevant primary hypotheses and conditional cases inspected as detailed below.
COMPARISON: Cauchy supplies finite coefficient extraction on a locally zero-free contour, not a sign. Voros's contours concern ordinary Li coefficients with different kernels; their deformations retain off-line-zero residues and their positive asymptotic branch assumes RH. Neither conjugate pairing nor the inspected saddle theorem supplies L966(16), the h-subtraction, or the proposed prefix inequality.
GAP: Specialize coefficient extraction to the full d_k-weighted logarithmic-derivative sum on a fixed safe circle, retaining -d_1G(h), then investigate a genuinely signed angular comparison. No prefix estimate or uniform saving has been proved or imported.
REASON: Essential representation tools are accessible and already largely covered; the new comparison rules out an unconditional sign import from the inspected Li contour asymptotics. A precisely defined reflected-prefix test is nominated separately for approval; this literature-only step derives no identity or lemma.
SCOPE: Actual F(x)=Xi(i sqrt(x)), G=F'/F; all paired nodes/multiplicities and L966 coefficients; eta(n)=1/(64*9^n), b=1/4, h=64*9^n. Fixed circle |x-b|=1/2 only; no contour enlargement, new zero-free estimate, positive Stieltjes law, numerical zero premise or RH.

## Completed comparison — step187

The main gap is L030-L032/C032a actual-Xi positivity. On this route
all-index L966(16), R_n<=N_n, remains unpaid; L968 supplies the audited
conditional downstream implication. L970 signs n=2 only. The target
reviewed here keeps the entire Bell sum together instead of paying
each block or each theta coordinate pointwise.

### Primary results and exact limitations

[NIST DLMF 1.9.30-31](https://dlmf.nist.gov/1.9#E31), version1.2.8
(released15 September2026; homepage version inspected), gives Cauchy's
integral formulas for a function continuous on the closed interior of
a simple contour and analytic inside, evaluated strictly inside, with
positive orientation. Apply the formula to the logarithmic derivative,
not a global logarithm. L966's local product argument already gives a
zero-free neighborhood |x-b|<1. Thus the proposed circle of radius1/2
has a neighborhood inside that established domain. F is entire and its
positive real value at h is covered by L966. This applicability check
uses no enlargement of a zero-free region. The finite combination and
conjugate pairing still require their explicit normalization check in
the later mathematical attempt. Cauchy gives no cancellation bound.

A. Voros, [*A sharpening of Li's criterion for the Riemann Hypothesis*,
arXiv:math/0404213v2](https://arxiv.org/html/math/0404213v2),
15 April2004, Sections2-3, (6)-(9) and the following RH-true hypothesis paragraph, supplies an exact finite sum and
residue contour for ordinary Li coefficients. In(7), its contour encloses
only poles1,...,n of a gamma-ratio times a secondary zeta function;
this is not the x-plane resolvent observable of L966. Section3 explicitly
qualifies its saddle assertions. Its RH-false case includes complex
conjugate saddle contributions; its RH-true case uses real zero
parameters. Those cases cannot supply unconditional positivity by
keeping only a favorable real saddle. No saddle estimate from this
note is imported.

The primary later account, Voros,
[*From asymptotic to closed forms for the Keiper/Li approach to the
Riemann Hypothesis*, arXiv:2204.01036v2](https://arxiv.org/html/2204.01036v2),
23 September2022, Sections2.2-2.3, (13)-(20), was inspected through both
conditional cases. Equations(14),(17) use small coefficient contours;
expanding toward the unit circle in(18) includes residues from possible
off-line zeros. Equation(19)'s counting-function integral, and hence
the positive asymptotic(20), use RH. Keiper and Li normalizations differ
by n. The paper supplies neither the d_k weights nor the h-resolvent
in this notebook. Conjugation makes a paired contribution real but
does not make it nonnegative. An infinite asymptotic zero expansion
is not imported as an absolutely convergent identity at fixed n.

[NIST DLMF 2.4(iii)-(iv)](https://dlmf.nist.gov/2.4#iv), same version,
(2.4.10)-(2.4.16) and the intervening hypotheses, treats analytic phase
and amplitude on a domain containing the path, compatible local
expansions/branches, uniform endpoint convergence and separation in
real phase. The simple-saddle expansion requires the relevant interior
minimum and a nondegenerate saddle. The discussion also notes
cancellation of endpoint expansions when the interior point is not a
saddle. These tools neither construct a deformation avoiding unknown
zeros nor establish uniform error for n-dependent amplitudes/weights.
Consequently a formal saddle or conjugate symmetry is insufficient.
No saddle theorem is presently applicable to an identified L966 saddle.

Reuse the inspected finite-chain/product coverage in
[step164](2026-11-10-regularized-li-theta-representation-review-163.md)
and the one-sided criterion comparison in
[step171](2026-11-10-prescribed-eta-li-detection-review-170.md).
The latter already identifies Lagarias AIF57(5)(2007), Theorem2.4(2),
(2.21), pp.1702-1703, in the correct normalization. No new growth
criterion, contour-to-Li substitution or reproof is needed here.

### Local duplication, failure checks and scope of the nomination

Read L966(2)-(4),(8)-(16) and its convergence/local-product proof,
L967's hypotheses, complete n=2,3 tensors and stated escape obstruction,
L969's statement and complete replacement factors, and C969a's
statement and full contraction setup. The supplied overview/DAG and
step164/171 assessments were reused. The step168 attempt's WHY IT
FAILS was inspected. This is source comparison, not a new audit of
those complete proofs.

L967/L969/C969a exclude their specified pointwise tensor/marginal
payments. They do not exclude integration of a signed angular density.
Conversely, replacing these payments by a Cauchy identity alone gives
no sign gain. No existing source assessment found in the scoped
L966/Q_eta search covers reflected angular prefixes. L970's finite
moment certificate remains preserved; the next test is not further
finite-index Q positivity accumulation.

The concrete nomination is in
[the reflected-prefix assessment](2026-11-10-reflected-prefix-contour-test-review-187.md).
It fixes a zero-safe circle, the entire weighted coefficient kernel,
a reflection pairing and a quantitative inequality on a proper part
of the angular domain. Its definitions and inequalities are proposed
test specifications, not derived identities or established bounds.
It allows signed cancellation before an estimate. Success would pay
one prescribed share of the h-subtraction; the complementary angular
share and all-degree signs remain independent gaps. A certified failure
at a single prescribed index/prefix would reject this fixed rule,
not L966 positivity or contour methods generally. New coverage receives
separate approval next turn; no mathematical attempt was run now.

### Search/access record and unused leads

Queries actually used included `Li criterion contour integral generalized
Li coefficients Voros asymptotic Riemann hypothesis`, `Li coefficients
Bell polynomials contour integral logarithmic derivative Riemann xi`,
`"Li" "coefficients" "contour" "regularized" resolvent`,
`"Li coefficients" "Bell" "inequality" contour`,
`"Li coefficients" "contour" "paired" inequality`,
`"Li coefficients" "partial integrals" positivity`,
`"Li coefficients" "angular" "prefix" inequality`,
`"Li" "theta" "1/(64" resolvent`, and
`"Li coefficients" "contour" "reflection" positivity`.
No matching primary prefix theorem was located. This is bounded
coverage, not proof of novelty or nonexistence.

Search hits for Coffey, eigenvalue-density/formal-Li arguments, claimed
RH proofs, unrelated resolvent papers and other notebooks/web projects
were not used as theorem evidence. The previously blocked Coffey
publisher retrieval was not repeated; it is not essential to this
fixed-contour test. No external passage is silently treated as read
through a snippet. Full matching Mathlib coverage is unknown; it is
not needed to establish source scope. No cross-notebook input was used.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. No new lemma,
mathematical script, proof correction, sign bound or RH candidate.
PROOF.md and DAG.md require no argument change.

## Preserved step186 nomination (historical scope, before this review)

## Proposed purpose and discriminator

The main gap is all-degree actual-Xi positivity, with all-index
R_n<=N_n in L966 as the present route's sufficient missing input.
The proposal is to keep the complete signed Bell combination together
on a coefficient contour and investigate pairing conjugate arcs,
rather than pay its even blocks separately or require a pointwise
theta kernel to be nonnegative. This is a research lead, not a formula,
claimed saving, ready theorem application or novelty assertion.

The source review should compare the exact generating/coefficient
observable with known Li coefficient contours, signed saddle methods
and recorded notebook stops. It must not replace this observable by
ordinary Li coefficients or import an RH-equivalent eventual sign.
It should choose one bounded creative test only after specifying the
contour and a quantitative cancellation threshold. Continue toward
a creative proof attempt only if the test retains every negative
term and its contour hypotheses can be justified without RH. Reject
or refine the proposal if zero avoidance, an absolute error estimate,
or the claimed signed saving already assumes the missing positivity.
No further finite-index certificate is proposed.

Essential inputs for later work are L966(2)-(4),(12),(14) and its
prescribed eta(n)=1/(64*9^n), with L019 and inherited L018/L024/L026.
L967/L969/C969a are contrasts; L968 is downstream only. Full all-index
signs, contour hypotheses and any n-uniform remainder remain unresolved.
No cross-notebook theorem, zero table, simplicity, Stieltjes law or
RH-dependent premise is supplied. Mathlib matching coverage is unknown.

If a new mechanism survives source comparison, its later creative
escalation should name the exact paired-arc inequality and one bounded
test. At this nomination stage missing source coverage blocks that
escalation; ordinary literature comparison is the appropriate next turn.

