# Planar-face mixed-sector defect — completed bounded source comparison

TARGET: Evaluate the signed planar-face defect in the G_-+ action-plus-density sector for a frozen normal external field, and decide whether it can generate an N-order correction.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Checked the local planar/half-space and BRST assessments, L280(4),(16)–(20), L282 hypotheses and (3)–(6), L283 section 2, L287(1)–(6), L289 hypotheses/conclusions and ATTEMPTS/007,047–049; searched the lattice half-space, boundary self-energy and signed Wilson surface terminology below. No inspected matching theorem was found; this is not a novelty claim.
SOURCE_EVIDENCE: Newly inspected Cornean–Garde–Jensen 2211.01974v3, Assumptions 2.1/3.1, Lemma 2.2, section 2.3, Theorem 3.2 and both proof cases, and the complete appended corrigendum; Luescher–Narayanan–Weisz–Wolff hep-lat/9207009v1 sections 4.4–4.5 and 6.5; Christiansen Murguizur–Manzo–Pisani 2604.05082v2 section 5, (5.1)–(5.5) and footnote 3. Reused the prior versioned bulk, scalar and relative-boundary readings below.
COMPARISON: Corrected scalar half-space resolvent convergence has a boundary-weight qualification and excludes the zero spectral parameter; slab improvement and continuum heat traces do not compute this relative-Coulomb lattice sector. The audited local o(N^2) limits do not determine a surface coefficient. No theorem supplies the proposed signed defect or its summability.
GAP: Define the relative half-space transverse/density contractions from the actual finite-domain matrices, justify the normal-field and massless limits, and prove depth summability with a value or an informative failure. Passage to actual source fields, other groups and an o(N) full-box error remains independent.
REASON: Complete the missing geometry/scale comparison and permit a bounded Wilson-specific test from the exact finite definitions, without assuming an unread theorem, a half-space identity or a surface expansion. This literature turn derives no mathematical result; the newly changed ready assessment receives separate approval before research.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and changes both geometry and error scale beyond the ready bulk audit. Reused adequate earlier coverage rather than repeating those searches.
SCOPE: Exactly TARGET: SU(2), even N>=2, a=8/N, all-face relative cube, boundary-contained pins and fixed gauges, all variable normal links/colors/source orders, L002's exact product bump through L282 and L280's real source domain; a frozen normal-field local test of the complete G_-+ action-plus-density selection only. Its half-space construction and convergence are research obligations, not imported premises.

## Proposed intermediate target and its use

The main gap is the interacting continuum construction with a nonzero
physical sector and finite positive mass. The audited leading
cancellation kappa_a=o(N^2) supplies no quantitative subleading bound.
This proposal tests a possible boundary obstruction to obtaining one,
rather than repeating the forest integration-by-parts, global absolute
norm or generic gauge-identity mechanisms stopped in ATTEMPTS/047–049.
The latter evidence remains in force for its original claims. The
completed bounded comparison below supplies no matching theorem and
makes no assertion of novelty or absence of duplicates.

The finite object to retain is exactly the part of L280(20) with one
G_-+ line:

\[
 \operatorname{Tr}(DG_{-+})
 -\tfrac14\mathcal U(U;G_{-+},G)
 +\tfrac14\mathcal B(T,T;G_{-+},G,G).
\]

This is a selection of already defined summands, not a new equality
for the full coefficient. Keep the complete density and the full
cubic derivative, including its external-curl part unless its error
is controlled at the new scale. L287's o(N^2) reduction error alone
is insufficient at order N. No face term is asserted to exist.

The proposed local test freezes the two external fields normal to one
planar face and compares the corresponding relative half-space
contraction with its bulk value. The depth sum of the signed
difference, its convergence or divergence, and any boundary identity
must be defined and checked before giving it a surface coefficient.
In particular do not transfer finite-box bounds to the half-space
without a limiting argument. Half-space zero modes, the gauge
quotient, density and normal endpoint rows are essential source-scope
questions. The completed comparison below retains the relevant
boundary theorem hypotheses and proof cases; none proves this defect.

Essential local starting inputs are L280's exact jets/density and
source decomposition, L282's actual strong fields, L283's quartic
mixed-covariance term, and L286–L289's audited cubic estimates and
bulk tensor. L291's accepted cancellation motivates the subleading
question but cannot prove a boundary estimate. Retain SU(2), the
even relative cube with a=8/N, every variable normal link, all colors
and both source orders, the exact L002 product bump through L282,
and (|s|+|t|)||f_*||_infinity<eta<1 with derivatives at zero.
There is no extra a^4 in the original plaquette sums and no nonlinear
transport from a forest slice.

## Discriminating test and later routing

A convergent nonzero signed face defect would be evidence for a
potential N-order term in this sector, but attribution to the full
coefficient would still require the actual source-field pairing,
all faces, edges/corners, the other cubic/quartic groups and an o(N)
error. A proven zero face defect would remove only this candidate
obstruction; it would not establish a logarithmic bound. A failure
of the depth sum to converge is itself a concrete obstruction to
this proposed surface expansion. An essential inaccessible source
requires parking the dependent calculation, not another generic
gauge-identity argument or an unproved half-space substitution.

The completed task is literature_comparison (standard/high), with
STEP_CLASSIFICATION NOVELTY_UNCHECKED. Recommend a later
proof_attempt/creative (deep_research/max) after separate approval of
this changed assessment: test this one normal-field face defect before
attempting a full expansion. The escalation is the presently
uncontrolled boundary contribution below the cancelled bulk scale;
the bounded decisive evidence is a justified convergent defect with
its sign/zero, or a proved failure of the defining depth sum. No such
mathematical attempt was carried out in this source review.

## Primary statements and exact scope

### Discrete scalar half-space theorem, including its correction

H. Cornean, H. Garde and A. Jensen, *Discrete approximations to
Dirichlet and Neumann Laplacians on a half-space and norm resolvent
convergence*, Studia Math. **271** (2023), 225–236,
[2211.01974v3, 27 November 2024](https://arxiv.org/pdf/2211.01974v3),
original pp. 2–7 and appended corrigendum pp. 1–3 (PDF pp. 12–14).
Theorem 3.2 assumes d>=2, 0<h<=1, compact K in C\\[0,infinity),
and Assumptions 2.1/3.1: an L2 reflection-even generator with
orthonormal integer translates, essentially bounded Fourier transform
supported in [-3pi/2,3pi/2]^d and bounded below on [-pi/2,pi/2]^d.
With its embedding/discretization maps it gives O(h^2) resolvent
convergence. Both proof cases use scalar reflection intertwining
and the full-space estimate.

The corrigendum repairs Neumann intertwining/isometry: include n_1=0
with half weight, change the maps, and double the forward normal
difference there. Dirichlet is unaffected. This is not automatically
our counting-measure, staggered normal-edge convention. Zero-energy
uniformity and depth-summed transverse Wilson contractions are not
conclusions. No specialization is claimed; lattice identification
and massless passage must be justified in the later test.

### Gauge slab calculation and boundary improvement

M. Luescher, R. Narayanan, P. Weisz and U. Wolff,
*The Schroedinger Functional — a Renormalizable Probe for Non-Abelian
Gauge Theories*, Nucl. Phys. B **384** (1992), 168–228,
[hep-lat/9207009v1, 9 July 1992](https://arxiv.org/pdf/hep-lat/9207009v1).
New reading: sections 4.4–4.5, printed pp. 27–29, (4.20)–(4.26),
and 6.5, pp. 38–40, (6.26)–(6.28). Spatial directions are periodic;
temporal tangential links are prescribed and normal links variable.
Background-dependent constant diagonal modes have exceptional
boundary conditions. Equation (4.20)'s asymptotic series is suggested
by Symanzik analysis, not proved with a uniform remainder. O(a)
improvement retains electric and magnetic boundary plaquette terms.

Thus absence of additional divergent counterterms cannot be used as
absence of boundary cutoff effects. Neither the selected coefficient
nor its N-order term is evaluated: geometry, sources, gauge slice and
normalization differ. No background-specific zero-mode exception,
action weight or boundary term is silently changed here.

### Continuum images: reuse and an orientation check

Reuse [the transverse coverage](2026-10-25-transverse-complete-coefficient-log-growth.md)
for S. Christiansen Murguizur, L. Manzo and P. Pisani,
*Worldline Images for Yang-Mills Theory within Boundaries*,
[2604.05082v2, 21 October 2026](https://arxiv.org/html/2604.05082v2),
sections 2–4: continuum relative/absolute vector and ghost operators,
the spectral qualification on gauge parameters, image construction
and the first three heat coefficients. Their heat-trace surface
cancellation is not this source-dependent lattice coefficient.
New reading of section 5, (5.1)–(5.5) and footnote 3 checks the
stronger lead: its constant chromoelectric field is tangential, with
absolute boundary conditions; a normal electric field is deferred.
Neither is an identification of a frozen normal external potential
in our relative-Coulomb bilinear sector. No gauge-minus-ghost
determinant replaces L280's complete quotient-Haar density.

## Reuse, duplicates and failures

The [upstream cubic assessment](2026-10-26-upstream-cubic-critical-audit.md)
and [complete cubic comparison](2026-10-26-complete-cubic-quadratic-asymptotic.md)
remain adequate for Luescher–Weisz hep-lat/9502017v2's bulk scalar
subtractions, Bode–Weisz–Wolff hep-lat/9809175v1's different slab,
and the delimited Dowker, Lawler–Limic and Michta–Slade statements.
Those are supporting citations only; retain the recorded
inverse-square/zero-mode restrictions. Reuse Benzi–Razouk for
polynomial locality, not uniform inversion at a closing gap.

The [older physical-boundary comparison](2026-09-27-physical-boundary-remainder.md)
distinguishes interior heat bounds, physical boundary interactions and
truncation of already renormalized scalar correlators. None computes
this signed defect. The [boundary BRST comparison](2026-10-03-boundary-brst-counterterms.md),
ATTEMPTS/007 and L012 stop the stated unrestricted off-shell domain
shortcut; spectral Gaussian kernels remain distinct. ATTEMPTS/047–049
stop the forest rearrangement, global absolute norm and generic orbit
identity respectively. The present test instead retains the actual
local Wilson vertices and signed boundary contractions. Those stops
are preserved, not reset or disproved.

Local inspection found no completed signed face calculation. L282,
L283 and L289 discard boundary layers only at the N^2 scale. In
particular L287(5)'s O_f(N sqrt(log(eN))+log(eN)) reduction error
cannot simply be dropped at order N: retain its external-curl part
in this test. This is a comparison with existing statements, not a
new estimate. The density is L280(16), including all-link Haar and
both determinant contributions, not a scalar heat-trace count.

## Search record and uncovered obligations

Queries on 2026-10-26 included:

- `lattice gauge theory half space boundary propagator relative boundary conditions one loop surface Symanzik`
- `discrete half space Green function Dirichlet Neumann lattice boundary asymptotics method images`
- `"Wilson" "boundary" "Haar" "Schrödinger functional"`
- `"lattice" "gauge" "half-space" "one-loop"`
- `"lattice gauge" "boundary" "self-energy"`
- `"Schrödinger functional" "surface" "mass term"`
- `"planar" "boundary" "Wilson" "one-loop" gauge defect`
- `"half-space" "gauge" "normal" "lattice" propagator`

Exact-title searches followed the discrete half-space and worldline
papers to primary statements. The worldline publisher endpoint
failed, but versioned arXiv resolved. A publisher search also exposed
*Small coupling (low temperature) expansions of nonabelian Yang-Mills
fields on a lattice in temporal gauge*, Ann. Phys. **133** (1981),
240–285, [DOI 10.1016/0003-4916(81)90251-7](https://doi.org/10.1016/0003-4916(81)90251-7).
Only its publisher abstract was exposed; full text returned 403.
This is an unread temporal-gauge/infrared lead, not an assessed theorem
or input. The bounded test assumes no temporal-gauge subtraction or
conclusion from it. Kennedy–Sint's surface-renormalization proceedings
and discrete surface-potential scattering results were screening leads
only. No essential external premise is hidden behind these leads:
the half-space construction itself is to be tested from the exact
finite relative matrices. A general surface-renormalization claim
would require additional source review.

Before giving a face coefficient, the later attempt must specify
finite-volume or infrared regularizations of the frozen normal field
(which is not a square-summable half-space test), its boundary
placement/counting measure, and the order of limits. It must justify
the half-space covariance/projection and complete density, every
normal-link endpoint, the two-vertex cubic sums and signed bulk
subtraction. A regulated or fixed-depth value alone is insufficient:
establish depth summability uniform in the needed limits, or a precise
failure. None is asserted here. Their possible failure is the purpose
of the bounded test, not permission to assume them.

Continue on a justified zero/nonzero convergent defect or an
informative obstruction. An undefined subtraction, unmatched boundary
convention or uncontrolled regulator limit stops that inference and
must be saved. Even success needs actual L282 source pairings, all
faces/edges/corners, other groups, and o(N) errors before any
full-coefficient conclusion. A zero frozen test does not prove a
logarithmic bound or the interacting c_box/2 threshold.

The [current Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
was checked on 2026-10-26 and still links the same 14-page
[Jaffe–Witten description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
section 4, printed p. 6, including finite positive mass. Retain the
precise scope in foundations/01-target-and-scope.md. This step does
not advance continuum existence or the mass-gap construction.

Mathlib coverage of this full target and supporting half-space
specialization: **not checked**. No full matching result, new lemma,
mathematical script or mathematical argument change is claimed.
EXPLORE records completed bounded source coverage, not certified
novelty or a mathematical solution.
