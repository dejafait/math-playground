# Actual Hermite discriminant: leading CD-cone diagnostic

TARGET: Test the diagonal Christoffel–Darboux cone certificate for the complete discriminant of Romik's P_N at large N by determining its highest two kernel coefficients from the actual b_(2N) and b_(2N-2), using Theorem 2.7 only through its stated relative error.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: The primary mixed-sum comparison and scoped duplicate/failure checks are recorded in drafts/literature/2026-10-31-actual-hermite-signed-cross-term-review.md. The checked CD/Turan statements do not decide this actual-coefficient cone test; no novelty is inferred. This is the single nominated diagnostic, not an additional completed calculation.
SOURCE_EVIDENCE: Romik v3 https://arxiv.org/html/1902.06330v3#S2 (2.1)–(2.3), Theorem 2.7/(2.23), (2.11), Appendix A.2; NIST DLMF https://dlmf.nist.gov/18.2.E12 and https://dlmf.nist.gov/18.2.E13, https://dlmf.nist.gov/18.3#T1, https://dlmf.nist.gov/18.9.E25, https://dlmf.nist.gov/18.18.E23; O'Sullivan v2 https://arxiv.org/html/2007.13582v2#S2 explicit Hermite formula. Direct primary pages and theorem statements rechecked 2026-10-31; prior Romik proof-case assessment reused.
COMPARISON: Standard kernels are positive on the diagonal, but neither their identity nor single-Hermite Turan signs controls the complete weighted discriminant. The nominated finite coefficient condition must be derived and tested for actual Xi; it is stronger than asking whether the discriminant is nonnegative.
GAP: The exact highest two cone coefficients and their eventual signs are uncomputed. No cone membership, signed margin, all-height transfer or higher sign is established.
REASON: One explicit coefficient obstruction can reject this particular positive-kernel certificate at arbitrarily large cutoffs without assuming RH, real-rootedness or the desired sign. The inspected source tools suffice for this bounded calculation; no original result is derived in the approval record.
SCOPE: Ready coverage for the exact TARGET; finite polynomial algebra and adjacent-index asymptotic comparison only. Direct-URL recovery completed in a separate literature turn; no new identity, coefficient, sign, lemma or mathematical script was derived.

## Objects and exact scope

Use actual Xi normalization L018–L020 and L564:

    P_N(t)=sum_(n=0)^N (-1)^n b_(2n)H_(2n)(t),
    b_m=integral_R u^m exp(-u^2/4)Phi_R(u)du/(2^m m!),
    D(P_N)=P_N'^2-P_N P_N'',
    K_j^H(t,t)=sum_(ell=0)^j H_ell(t)^2/(2^ell ell!).

Proposed certificate: an identity

    D(P_N)(t)=sum_(j=0)^(2N-1) lambda_(N,j) K_j^H(t,t)

with every lambda_(N,j)>=0. The next step must justify the degree,
existence/uniqueness of this coefficient expansion and which mixed
terms contribute to its two highest coefficients. The identity and
those coefficient formulas have not been established here. Do not
substitute a diagonal-only approximation for D(P_N).

The task is to derive those two exact coefficients for variable
integer N>=2, then decide their eventual signs from the actual
b_(2N)/b_(2N-2) behavior. Reuse Romik's (2.23) with its relative
error and the exact Lambert-W relation; do not differentiate a big-O
term or use the logarithmic asymptotic (2.24) alone for adjacent
ratios. All asymptotic onsets remain existential unless separately
effectivized. No numerical coefficient sampling is required.

Source scope for Romik's coefficient asymptotic and proof cases is
already ready in `2026-10-31-hermite-moving-degree-first-sign-review.md`.
The parent comparison checks standard kernel/product/derivative
normalizations and O'Sullivan's explicit polynomial formula. Its
stronger coefficient asymptotic is unnecessary and is not approved
as a new essential input. Turan's unread Theorem IV is also unused.

## Relevance, decision test and limits

The main gap is actual-Xi all-degree positivity. This test concerns
one proposed first-sign certificate whose nonnegative kernel weights
could supply an independent truncation sign and later a margin.
L564 applies at N=ceil(16(T+1)^2); eventual obstruction for all large
N would also address that unbounded moving-cutoff route.

Abandon this cone certificate if one leading coefficient is rigorously
negative for all sufficiently large N, or on an unbounded subsequence
of the prescribed moving cutoffs. Preserve that evidence; it does
not refute positivity of D(P_N). Passing the two coefficients only
justifies a later review of the remaining coefficient condition;
it is not a sign theorem or authorization for an unbounded search.

The next turn should stop after this leading-coefficient diagnostic.
For any eventual positive transfer, retain the full L564 perturbation
error, require a quantitative margin, and handle zeros/multiplicities
without division by Xi. Initial cutoffs, bounded-height overlap and
all higher mixed forms remain independent. Essential input IDs are
L018–L020 and L564; L233/C233a motivate the gap only. No
cross-notebook theorem is used. Mathlib coverage is unknown/not checked.

This is a standard calculation using known source inputs. It is not
nominated as a protected creative proof attempt. The completed
literature outcome remains separate from approval of this new target.

## Direct-source gate repair (2026-10-31)

LITERATURE_REASON: The supervisor requires direct source URLs in this ready
assessment; the previous SOURCE_EVIDENCE supplied identifiers and delegated
links to parent reviews. This turn repairs that essential source record,
without repeating discovery or changing the target.

The linked Romik v3 §2.1 definition and Theorem 2.1 were rechecked against
the saved P_N; §2.4 Theorem 2.7/(2.23) states a multiplicative
1+O(log log n/log n) error as n tends to infinity, not a differentiated
error or an effective onset. Its exact positive-real Lambert W convention
and proof-case coverage remain those of the ready moving-degree review.
That earlier review's left/central/right saddle and remaining-theta cases
are reused; this is not an independent manuscript audit.

The linked DLMF diagonal/off-diagonal statements, Hermite table row,
derivative and product formulas were inspected. Their hypotheses use
orthogonal polynomials with positive norms, real arguments for the kernel,
and nonnegative integer indices; use the derivative formula for n>=1
and the constant polynomial separately. The physicists' normalization is
H_n with weight exp(-x^2), not He_n or Hermite functions. The proposed
K_j^H is sqrt(pi) times the tabulated normalized kernel, as already
recorded in the parent comparison. O'Sullivan v2 §2's explicit finite
Hermite formula was inspected directly; its stronger coefficient
asymptotics remain unnecessary. No retrieved theorem supplies the
complete discriminant's unknown cone weights or their signs.

Duplicate/failure evidence is reused from the parent comparison's named
local checks: automatic CD/Turan transfer, parity and moment/Pollaczek
obstructions have different scopes. No source blocker or new overlap
was found here; no novelty claim follows. The exact target remains
EXPLORE and ready for its bounded calculation. Mathlib coverage remains
not checked. PROOF.md and DAG.md need no change because no argument or
mathematical input changed.
