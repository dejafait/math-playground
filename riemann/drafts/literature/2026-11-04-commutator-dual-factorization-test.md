# Commutator-assisted Fourier dual factorization — nominated bounded attempt

TARGET: Seek a commutator-based factorization of the boundary-cancelled Fourier dual row that avoids a global inverse-gap estimate, with a rigorous norm-ratio test at lambda=sqrt(13), N=120, z=i/4.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step362's completed exact dual-residual, normalized eigenvector and displacement-rank searches in drafts/literature/2026-11-04-boundary-cancelled-dual-residual.md; no matching controlled preimage estimate was located. No new search or novelty claim is attached to this nomination.
SOURCE_EVIDENCE: CCM v1 https://arxiv.org/html/2511.22755v1 Lemmas5.1-5.4, Corollary5.6, Proposition5.9/(5.25), Theorem5.10 normalization; Greenbaum--Li--Overton published https://cs.nyu.edu/~overton/papers/pdffiles/EigVecPert.pdf Theorem2/(5)-(8), sections3.3-3.4/(26)-(30); Connes--van Suijlekom v1 https://arxiv.org/html/2511.23257v1 Lemmas5.1-5.3/AppendixA; Embree--Ionita https://personal.math.vt.edu/embree/embree_ionita.pdf section4/(12)-(13). Step363 resolves all four URLs and rechecks the load-bearing statements; full citations and previous proof inspection remain in the parent review.
COMPARISON: Source identities cover the Fourier row and one normalized odd-direction commutator relation; standard sensitivity retains R. Structured inverse algorithms retain inverse factors and have different pencil hypotheses. Merely reproducing these formulas or computing a dual norm is known mathematics; a controlled transform-specific preimage would be the identified extra step.
GAP: Find or refute an explicit preimage whose proved norm beats the full-gap estimate without hiding R, an equivalent inverse, an unproved ground-vector bound or a boundary-overlap denominator in a constant.
REASON: One bounded mechanism is justified by the shared rank-two generators and Fourier row, which is a frequency-resolvent row. This is a proposal for subsequent mathematics, not a derived factorization, approved bound, beyond-source result or RH candidate.
SCOPE: One factorization attempt for the exact finite matrix of audited L759 at z=i/4, with any complete structural counterexample identified separately as a mechanism obstruction. All 241 coefficient directions, both parity sectors, exact normalization and interval uncertainties must be retained. No parameter sweep, all-N/lambda assertion or trial/Xi comparison is covered. Newly written ready coverage requires separate supervisor approval next turn.

LITERATURE_REASON: Supervisor recovery requires direct source URLs in this exact-target assessment; step363 repairs that omission and verifies access without expanding the target or repeating discovery.

## Direct-source recovery, step363

All four SOURCE_EVIDENCE URLs resolved on 4 November 2026. Rechecked
CCM section5.2 normalization cases and Lemma5.4(i) proof, Proposition5.9
with its complete proof, and Theorem5.10 statement; Greenbaum--Li--Overton
p.467/(5)-(8) and its separation bound; Connes--van Suijlekom
Lemmas5.1-5.2 with proofs; Embree--Ionita section4 pp.8-9/(12)-(13).
These agree with the parent comparison: the commutator identity has
eta-overlap normalization, perturbation retains the reduced resolvent,
and the Loewner formula retains inverse factors. No new bound follows
from this access check. Earlier proof-case, normalization-change,
duplicate and failure assessments are reused unchanged from the parent.
This is a process repair, not new mathematical evidence or a new search.
The exact target, EXPLORE decision and bounded test remain unchanged;
no source blocker remains. Mathlib coverage remains unchecked.

## Proposed test, not an established result

Essential local input: audited L759. Use its exact arithmetic matrix A,
epsilon=min spec(A), T=A-epsilon I, and boundary-normalized xi with
b(xi)=1, b=eta*/sqrt(L). Let P be orthogonal projection off xi and R
the inverse of T on that complement, zero on xi. Set

    q_z = ell_z - ell_z(xi)b,
    ell_z(v)=2 L^(-1/2)sin(zL/2) sum v_j/(z-2 pi j/L).

The proposed mechanism is to seek an explicit row h_z, built using the
source's diagonal frequency resolvent, eta, beta and normalized ground
data, satisfying

    h_z T = q_z,       h_z(xi)=0,

with a useful proved norm bound. No formula for h_z, existence argument
or norm estimate is derived or claimed in this literature turn.
Simply defining h_z=q_z R P, rewriting an inverse as another singular
solve, or changing from the Euclidean to the T quotient norm does not
pay the desired estimate. Imported standard identities must be cited;
only the missing cancellation/norm step is the exploratory target.

The bounded discriminator is at lambda=sqrt(13), N=120, z=i/4 only.
Let g be the ACTUAL distance from epsilon to the remaining spectrum.
Seek a rigorous enclosure of the diagnostic ratio

    rho = g ||q_z R P||_2 / ||q_z||_2

and an algebraic bound explaining a material gain, with rho<=1/10 as
the continuation threshold. This is a research decision threshold,
not a theorem or a necessary RH condition. Enclose ||q_z|| away from
zero; if it vanishes exactly, handle that case explicitly. Enclose
g on both sides to prevent a loose certified lower bound from creating
an artificial gain. L759's g>5e-56 alone is insufficient for that
relative comparison. Retain ground-vector, epsilon, boundary evaluation
and entry uncertainty; an approximate eigensolver is a diagnostic only.
The eta-normalized x=xi/sqrt(L) is used in T D x=-beta; do not drop
the normalization factor or the odd part of q_z at nonreal z.

Continue toward a later family estimate only if both the rigorous gain
and a commutator-based explanation are established. Stop this mechanism
if the factorization merely reinstates the same inverse, the estimate
requires the missing eigenfunction comparison/overlap as a premise,
or certified evidence gives rho>1/10 without a new exploitable structure.
An enclosure straddling 1/10 is inconclusive; preserve partial reasoning
and do not relabel it a positive result. If a structural counterexample
is obtained, distinguish it from a failure of the arithmetic cell.
Even a successful cell leaves general simplicity/parity, quantitative
boundary overlap, actual trial residuals, both limits and locally uniform
nonzero Xi transfer unresolved. Mathlib coverage unchecked.

## Purpose and routing

Nominate proof_attempt/creative: the work is the proposed algebraic
cancellation at the missing ground-eigenfunction comparison, with one
finite falsification test. This designation does not apply to standard
resolvent specialization or a raw norm calculation alone. The precise
obstruction is that current control spends the entire inverse spectral
gap, while the desired Fourier observable might have a specially
controlled preimage. No previous failed creative invocation is needed;
the current literature review supplies coverage, not a solution. No
mathematics on this new target is invoked in step362.
