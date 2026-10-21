# Changed pair prescription at the unsafe integer threshold — source comparison

TARGET: Test exact global pair feasibility at T=floor(65537^28/2^128)+1 using independently thinned L030 moments, with all Johnson eigenspaces and the augmented constant coordinate retained.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reviewed L051, L030's complete pair computation, L021's statement, C001a's threshold and ATTEMPTS/011,021,022,033; searched independent thinning factorial moments, constant-weight thinning, prescribed Johnson distance distributions and exact 2571353 terms; no inspected theorem decides this changed slice.
SOURCE_EVIDENCE: Reuse foundations/09 and the ready 2026-10-07 global-pair assessment; freshly read Brouwer–Polak arXiv:1709.02195v1 Section 2 equation (1) and averaging, p. 2, https://arxiv.org/pdf/1709.02195v1; Polak v1 Proposition 1.1 and complete indicator proof, p. 2, https://arxiv.org/pdf/1703.05171v1; foundations/11 records Last–Penrose's non-Poisson marking/thinning definitions and complete product-integral proof, pp. 40–43, https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf.
COMPARISON: Known independent thinning supports the changed diagonal and distinct-pair scaling, and the known order-two Johnson/Schur framework supports an exact test; neither provides global feasibility or infeasibility for these specified coordinates. L051's fixed-moment exclusion cannot be imported for this slice.
GAP: Produce a complete exact rational feasibility certificate or an exact infeasibility certificate for this prescription only; other moments, global representing measures, quantitative list bounds and RS realization remain unresolved.
REASON: Essential changed-scope coverage is complete; one finite specialization is justified after separate supervisor approval, without claiming a new general theorem or repeating the exhausted unthinned test.
SCOPE: Real symmetric augmented pair matrices on all 68-subsets of a 1024-set; the exact rational theta and coordinates below; all nonnegative free entries and 69 eigenspaces; singular PSD allowed; no higher moments or labeled determinant constraints.
LITERATURE_REASON: The gate requires this changed singleton/distinct-pair prescription to be compared separately; the new essential lead is independent non-Poisson thinning, while unchanged Johnson coverage is reused.

## Reviewed action and precise subsequent target

The completed task was: Assess source coverage for global pair feasibility
at the smallest unsafe integer mass using independently thinned L030 moments.
This was a literature-only turn. TARGET now names the subsequent bounded
mathematical test; its newly written ready continuation receives separate
approval next turn. No feasibility calculation ran here.

Keep H and V from L051, and set M=binomial(1024,68), L=137^3=2571353,
v=binomial(963,7), rho=L/v, tau=65537^28/2^128, T=floor(tau)+1,
and theta=T/(M*rho). Keep N_h=binomial(7,h)binomial(956,7-h) and
(d_0,d_1,d_2)=(2442832,125664,2856). Seek a real symmetric F on V
with f_S=F_SS=theta*rho, all entries nonnegative, and
[[1,f^t],[f,F]] PSD. For distinct supports S,U impose
F_SU=theta^2*rho*d_h/N_h at intersection 61+h (h=0,1,2), and zero
at intersections 64–67. Entries at intersections 0–60 remain free.

T is a singleton-objective mass, not a claim that every sampled family
has exactly T members or that a code of size T exists. The main gap is
arbitrary-center safety at 68 agreements and independently 67 agreements;
the bracket remains 955–957. The intermediate target tests compatibility
of changed pair data at the smallest integer above the actual threshold.
Its downstream use is to discriminate between a fixed-prescription
obstruction and one persisting nearer the threshold. Even a negative
answer leaves a uniform bound over other assignments as an independent gap.

## Source applicability and limits

The thinning input is canonical in
[foundations/11](../../foundations/11-independent-thinning-source.md).
Its finite discrete specialization fits each L030 distribution: the
points being retained are residual seven-subsets, not evaluation-domain
points. The diagonal and distinct-pair factors match the proposal.
L030's hereditary independence conditions are compatible with block
deletion. This interpretation concerns local distributions only. There
is no unthinned global distribution to thin: L051 excludes even its pair
relaxation. Thus a thinning citation cannot construct the changed global F.

The retention parameter must be in [0,1]. L051's recorded comparison
puts M*rho between 1.677*tau and 1.678*tau, and C001a records tau>2^320.
Those strict bounds suffice for theta to be strictly between zero and
one even with the upward integer rounding. The subsequent certificate
must reconstruct T and verify this comparison exactly; no changed-moment
arithmetic was performed here. Independent thinning controls expected
size and does not impose deterministic global cardinality.

Reuse [the prior assessment](2026-10-07-global-pair-marginal-extension.md)
and [foundations/09](../../foundations/09-global-pair-johnson-source.md)
for Johnson eigenvalues, common orthogonal decomposition, constant
projector J/M and Schur congruence. Precise primary inputs remain
Brouwer–Cioabă–Ihringer–McGinnis arXiv:1709.09011v2, Section 3 p. 10,
and Brouwer–Haemers' author preprint, Section 11.2 pp. 162–163 and
Theorem 2.7.1(i), p. 36. No reproof is needed.

The unchanged universe has n=1024,w=68, n>=2w and binary minimum
distance 10. Relation i is intersection 68-i: relations 1–4 vanish,
5–7 have the changed coordinates, and 8–68 are free. Global valencies
binomial(68,i)binomial(956,i) differ from local N_h. All specified
pair-only coordinates are permutation invariant, so averaging preserves
them; no averaging of actual-label higher constraints is licensed.

Brouwer–Polak's equation (1), with moment parameter 2, matches the
constant/singleton augmented matrix and nonnegative pair variables.
Nonempty D gives scalar conditions. Polak's indicator proof supplies
necessity, not a representing-measure theorem; retain its displayed
constant-weight qualification already recorded in foundations/09.
The Schur congruence uses only [1], with lower matrix
F-(theta*rho)^2 J. Retain all nonconstant eigenspaces and the separate
constant condition, including singular cases. L051's zero-variance
identity and triangular reconstruction are not approved inputs for the
changed moments. Any new necessary equations or LP reduction belong in
the subsequent mathematical turn.

## Duplicate and failure checks

ATTEMPTS/033 excludes exactly the unthinned prescription. ATTEMPTS/021
stops local higher-moment exclusions; ATTEMPTS/022 is a historical process
park. Neither decides the changed slice. ATTEMPTS/011 and L021 stop
unrestricted basic-LP optimization as a safety certificate; L021's
feasible optimum does not supply the present fixed coordinates.
The individual SDP diagnostics in L022–L026 stay parked. Preserve
ATTEMPTS/031–032's local deletion obstructions. L050's audit was already
completed in step 158 and is not a new continuation.

Scoped searches of the earlier global-pair and cross-core notes found no
completed threshold-thinning test. Impossibility of the unthinned slice
alone does not imply impossibility after both kinds of coordinates change.

## Search evidence

External queries on 11 October 2026:

- `independent thinning point process factorial moment measures p squared Last Penrose lecture Poisson process thinning`
- `"constant weight" "prescribed" "distance distribution" semidefinite`
- `"2571353" thinning Johnson`
- `"constant-weight codes" "thinning"`
- `"Johnson scheme" "prescribed" "distance distribution"`
- `"constant-weight codes" "pair moments" feasibility`

Fresh primary reading was exactly the passages in SOURCE_EVIDENCE and
foundations/11, including the complete conditional-product proof and
empty case. Screenshot calls returned labels without images; browser
text was used and no visual inspection is claimed. Older spectral
coverage was reused. Gijswijt's matrix-algebra thesis and other general
packing/point-process hits are unread, unused leads. Exact-number hits
were irrelevant. No inspected theorem settles these coordinates;
failed searches do not establish novelty. There is no essential source
blocker. Full matching Mathlib and supporting thinning coverage: not checked.

## Bounded continuation and decision rule

Essential inputs: L051, L030, L021, C001a and foundations/09,11. After
separate continuation approval, test exactly TARGET. A positive answer
needs full exact rational free entries, all fixed coordinates,
nonnegativity, all 69 spectral inequalities and the constant Schur test.
A negative answer needs an exact Farkas/dual certificate or complete
proved obstruction. Save the full certificate and report actual and
required mass, failures and paths. Solver status and previews are not
proof; failed rational reconstruction leaves the slice unresolved.

Feasibility parks this pair-only exclusion diagnostic. Infeasibility parks
only this changed assignment; either outcome may motivate a separately
assessed target. Neither supplies a packing, common-center RS list, safety
bound, higher-order extension or boundary improvement. If no certificate
is obtained, save unfinished reasoning and continue only with a concrete
independently testable repair. No new lemma, mathematical script, novel
result or complete candidate was produced in this review.
