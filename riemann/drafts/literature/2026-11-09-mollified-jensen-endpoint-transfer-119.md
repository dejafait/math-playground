# Linear-mollifier displacement-to-endpoint test

TARGET: Test whether Young's linear mollifier with theta=1/4 proves W_T<=T/4 for all sufficiently large T, where W_T sums m(rho)(beta-1/2) over beta>1/2 and T-1<=gamma<=2T+1, and yields a real endpoint in [T,2T] outside every closed Xi Jensen disk.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step119's completed weighted-displacement comparison in 2026-11-09-xi-weighted-jensen-endpoints-review-118.md, including exact searches, scoped Kim/mollifier duplicate checks and the November1 charged-block failure. No exact endpoint theorem was located; no originality inference.
SOURCE_EVIDENCE: Young, Arch.Math.95(2010),539–548, https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf : definitions pp539–540, smoothing pp540–541, Lemma3/(3.1)–(3.3) p541 and zero-shift extension pp544–545; Simonic https://arxiv.org/pdf/1910.08274v2 Section4.2 pp29–30 general Littlewood identity and Section4.4 pp31–32 argument-estimation method; L018 coordinates and Kim definitions/Theorem1 coverage reused from step114. Versions and qualifications in the completed parent review.
COMPARISON: The exact known mollified moment is a stronger quantitative input than unspecified O(T) displacement, but is not an endpoint theorem. Specialize the differing-mollifier Littlewood transfer, smoothing/logarithm/boundary treatment and disk geometry; do not reprove the arithmetic moment or assume the budget.
GAP: The W_T bound and endpoint are unproved. Uniform o(T) boundary remainders for this F, critical-line logarithms, limiting rectangles and closed-interval multiplicity counting must be justified. Critical counts, mixed signs and global transfer remain independent gaps.
REASON: Step119 found an inspected exact-moment input for one bounded established-method test; strip geometry and unspecified density constants do not suffice. This newly ready continuation receives separate source/scope approval next turn before mathematics.
SCOPE: Actual zeta/Xi without RH or simplicity; theta=1/4, P(u)=u, one fixed mollifier per height scale, full multiplicities and every 0<beta-1/2<1/2; a non-effective sufficiently-large-T conclusion. No effective onset or all-height signs.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity. A
positive result could supply Kim's endpoint premise at unbounded heights.
It would not bound his sign-sensitive critical count or prove RH.

## Exact test and applicability obligations

Use the parent review's full Young statement and scope. At scale S
comparable to T, set X=S^(1/4) and

    M_X(s)=sum_{n<=X} mu(n)(log(X/n)/log X)n^(-s),
    F_X(s)=zeta(s)M_X(s).

Check identification with psi(sigma0+it) and Lemma3 at zero shifts,
without an R-to-zero limit of Theorem1 or evaluation of separate singular
diagonal terms. Evaluate its main-term formula only in the research
turn. The candidate coefficient is log(5)/(4pi), not a proved estimate
in this nomination. W_T<=T/4 leaves room for the proposed losses.

Keep X fixed during each rectangle and endpoint perturbation. Construct
permitted smooth majorants for the padded window and justify the sharp
unweighted moment, including weight mass and O(S/log S) errors. Do not
use a moment with one global mollifier at unrelated dyadic scales.

Apply the general Littlewood identity, not Simonic's final optimized-
mollifier constants. Check holomorphy near positive-height rectangles,
choose a right edge with a controlled analytic logarithm, and retain
both horizontal argument integrals and the right vertical log integral.
Section4.4 supplies an inspected method, not an argument theorem about
this M_X: prove its uniform remainder from Jensen/argument-principle
bounds with the actual growth, coefficients and nonzero normalization.
Do not assume absence of mollifier zeros; retain nonnegative product
zero orders before dropping terms by an inequality.

Real zeta zeros lie on the intended left edge. Justify its limiting
position and local log|F_X| integrability, including multiple zeros;
top/bottom perturbations must include the closed padded window. Retain
domination/local factorization for every limit. Source continuity for
another mollifier is not this proof. The pole at1 is outside the
positive-height rectangles, but that does not resolve boundary zeros.

Use L018's one-right-zero-per-Xi-conjugate-pair convention, not two
independent disks. Prove all disks meeting [T,2T] occur in the padded
W_T window and compare their closed interval lengths against T with a
strict gap. Retain multiplicities, coincident disks and boundary contact.
Prove a point outside the closed union; if needed avoid independent real
Xi zeros as well. Negative endpoints require a later symmetry argument.

Continue only if W_T<=T/4 eventually and the endpoint are proved with
all error terms o(T). Otherwise preserve partial reasoning, identify the
failed estimate and park the specialization. An unspecified O(T) bound
is insufficient, and failure of this implementation does not disprove
actual endpoints. L612's abstract density model has no mollified-moment
input and neither supplies nor obstructs this proposed transfer.

This is established-method specialization, not a creative central
mechanism. No new derivation, lemma, script or arithmetic reproof is
included here. Full/supporting Mathlib coverage is unknown.
