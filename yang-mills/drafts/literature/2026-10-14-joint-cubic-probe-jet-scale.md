# Joint cubic probe-jet scale — completed coverage review

TARGET: Determine whether L011's joint cubic probe-jet response kappa_0(f_(i,1),r_1)-kappa_0(f_(i,1),r_0,S_3) has a finite a^3-scaled limit for both actual L010 probes.
CHECKED: 2026-10-14
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-14 searched cubic flow/probe Ward terms, maximal-tree and tree-gauge perturbation, and probe power divergences; compared the primary passages below and exact local f_(i,1) occurrences. No adequate match for the selected joint group was established; this is not a novelty claim.
SOURCE_EVIDENCE: Reused the combined-response, forest and cubic-residual/action assessments; rechecked Luescher–Weisz 1101.0963v2 secs. 7.1–7.4, 8.2, 8.4; Del Debbio–Patella–Rago 1306.1173v1 sec. 6 (6.1)–(6.16); Luescher 1006.4518v3 (2.28)–(2.33); inspected Ramos–Sint 1508.05552v1 secs. 3.1 and 3.4 (3.43)–(3.45).
COMPARISON: Renormalized full correlations and matched Ward responses do not cover this bare selected group; Ramos–Sint explicitly qualifies removal of total derivatives. L180 treats f_(i,0),r_1,S_3, while L020–L022 treat different flow contributions. None supplies the requested limit.
GAP: Obtain a complete signed joint reduction and a full-spectrum cubic bound/limit for both actual probes, retaining the nonlinear quadratic flow integral down to time zero and the cubic observable jet. No such estimate is imported.
REASON: The separate literature-only review now approves a bounded attempt on the unchanged target; essential comparison coverage is accessible. EXPLORE approves research, not a bound, limit, cancellation or originality.
LITERATURE_REASON: The changed f_(i,1) group had REVIEW_REQUIRED coverage and lay outside the ready residual/action audit assessment.
SCOPE: SU(2), all-face relative box D=(-4,4)^4, admitted even N and a=8/N, straight direction-1 lower-rooted forest, complete L008 displacement and both actual L010 probes at tau=1/16, fixed-mesh bare expansion before refinement; only the stated joint group and its cubic-scale test.

Reviewed scope: SU(2), all-face relative box D=(-4,4)^4, admitted even
N and a=8/N, straight direction-1 lower-rooted forest, both full actual
L010 probes at tau=1/16, and fixed-mesh bare expansion before refinement.
Keep the actual nonlinear flow and insertion jets, both probe sectors,
all forest compensations, physical faces, constant axial modes and heat sums.

Essential inputs for assessment are L008 L010 L011 L018 L019 L020 L021
L022 L028 L155 L180. L011(6) fixes the signs and term positions;
L019's full forest compensation and L022's failed termwise curvature
transfer must be checked rather than assumed to bound this group.
The source assessments below have now been compared for this changed
group. They supply context and reusable local inputs, not its bound.

Plausible downstream use: an independently established cubic limit or
zero limit for this joint group would constrain how remaining jets can
compensate the known selected action/residual coefficients. The full
f_(i,2),r_0 term, finer scales, finite matching, interacting reflected
error <=c_box/2 and continuum/infrared requirements remain independent gaps.
Continue after this separate coverage approval with an exact joint reduction or
controlled full-spectrum estimate; abandon termwise quotient transfer or
deletion of nonlinear flow jets. No bound, limit or novelty is claimed.

## Main gap and discriminating target

The main gap remains an ultraviolet-uniform interacting reflected
comparison with error <=c_box/2, together with the required continuum
observable theory and infinite-volume finite positive mass. The exact
intermediate question is whether a^3 times the TARGET group converges
to a finite real number for each i=3,6. Cubic boundedness alone would be
useful partial progress but would not answer convergence. A coefficient,
if established, could be compared with the selected action/residual
coefficients; it would not alone prove full compensation or matching.

## Local definitions, duplicates and recorded failures

Used the supplied full overview and ID-only DAG before targeted reads.
L010(2)–(4) fixes the different plaquette-trace and clover-product probes.
L011(6),(10)–(13) fixes both signs and the full coordinate-flow definition.
In particular its existing formula is

    f_(i,1)=D j_(i,2)(z_1(tau)) z_2(tau)+j_(i,3)(z_1(tau)),

with z_2 given by L011(11)'s integral from 0 to tau. Both summands
belong to the target. No replacement by a restricted forest Hessian,
left-frame nonlinear flow coefficient or quadratic-only probe is allowed.
This is a citation of L011, not a new jet calculation.

Read L008's displacement/probe hypotheses, L018(1)–(4)'s covariance
conventions, L019(1)–(5) and its connected-IBP proof, L020's selected
radial hypotheses, L021's complete selected conclusion, L022's
hypotheses/conclusion and proof section 3, L028's residual-consistency
statement and stencil comparison, L155(1)–(5), and L180's qualified
conclusion. These identify reusable inputs without transferring estimates
between different tensors. Searches for the exact f_(i,1) notation and
joint-group wording in local lemmas, histories and literature assessments
found its definition and proposal, but no completed bound for this group.

L020–L021 estimate a radial Q_3 contribution in f_(i,2), not Q_2 in
f_(i,1). L022's zero-linear-curvature test establishes a deterministic
cancellation in f_(i,2), not a cumulant estimate for this group. L155
contracts a quadratic probe with r_1 and S_3, and L180 evaluates that
different complete term. Their color and pairing conclusions cannot be
assigned to the cubic probe without examining its full tensor.

ATTEMPTS/009 and L019 preserve the need for full nonlinear forest
compensation; this chosen two-term group is not asserted invariant under
a change of forest. ATTEMPTS/010 preserves L022's failed termwise
curvature transfer. ATTEMPTS/011 preserves the growing raw covariance,
which precludes an O(1) raw-link-loop shortcut, not a signed-response
bound. ATTEMPTS/038 and history/214 preserve the audited isolated-term
nonvanishing; they are not a ban on investigating other jets. No failed
route is reopened here and no unfinished mathematical work is discarded.

## Literature reuse and bounded discovery

Reused [the combined-response assessment](2026-09-26-current-target.md),
[the forest assessment](2026-10-04-forest-compensated-ward-identity.md),
and [the residual/action assessment](2026-10-12-cubic-residual-action-cubic-scale.md).
Their general inputs remain adequate within their original hypotheses;
this review compares their scope to the new group rather than repeating
their general proofs. Queries were:

- `Yang Mills gradient flow nonlinear observable cubic Taylor jet lattice translation Ward identity one loop forest gauge`
- `"gradient flow" "maximal tree" perturbation boundary`
- `"gradient flow" "1306.1173" renormalization probes lattice`
- `"gradient flow" "cubic" "Ward" lattice perturbative`
- `"gradient flow" "tree gauge" renormalization`
- `"gradient flow" "probe" "power divergences"`

Relevant flow and improvement papers were read as below. Results about
quark operator mixing, two-dimensional topology and numerical scale
setting were screened as different targets; their snippets supply no
theorem evidence here. The stronger-match search is bounded, not an
exhaustive originality review. No essential source blocker remains for
the proposed local attempt.

## Inspected primary coverage

**M. Luescher and P. Weisz, *Perturbative analysis of the gradient flow
in non-abelian gauge theories*, JHEP 02 (2011) 051,
[1101.0963v2](https://arxiv.org/pdf/1101.0963v2), 10 February 2011.**
Read secs. 7.1–7.4, printed pp. 20–23, (7.1)–(7.8), and secs. 8.2,
8.4, pp. 24–25. Assuming ordinary four-dimensional renormalization,
directed flow trees exclude bulk counterterms; the remaining two
zero-flow-time counterterms are excluded by their BRS-weighted diagram
comparison. Positive-time gauge-invariant composites need no additional
renormalization. Section 8.4 presents the lattice extension as an
expectation. SU(2) is included by setting the source's color rank to two.
Its flow-time boundary is not a physical cube face. These results concern
renormalized complete correlations, not the isolated bare TARGET.

**L. Del Debbio, A. Patella and A. Rago, *Space-time symmetries and the
Yang–Mills gradient flow*, JHEP 11 (2013) 212,
[1306.1173v1](https://arxiv.org/pdf/1306.1173v1), 5 June 2013.**
Rechecked sec. 6, printed pp. 13–16, (6.1)–(6.16). Equations
(6.11)–(6.13) represent and normalize the complete flowed-probe
translation response; (6.15)'s residual removal additionally assumes
continuum translation restoration and matched stress coefficients.
The source's particular clover transformation differs from L010's
endpoint-averaged transported generator with its nonzero divergence.
Its full-response statements give no separate estimate for the two
Taylor cumulants selected here. Import the framework within its scope;
neither source normalization nor full-response finiteness is a substitute
for this group-specific calculation.

**M. Luescher, *Properties and uses of the Wilson flow in lattice QCD*,
JHEP 08 (2010) 071 with erratum,
[1006.4518v3](https://arxiv.org/pdf/1006.4518v3), 27 January 2014.**
Rechecked (2.28)–(2.33), printed pp. 7–8. The flowed energy-density
example retains poles in the bare-coupling coefficient and cancels them
after coupling conversion. It concerns the complete one-point observable
in dimensional regularization, not the present joint group. Retain the
bare/renormalized distinction; no conversion or coefficient is inferred
for either actual box probe.

**A. Ramos and S. Sint, *Symanzik improvement of the gradient flow in
lattice gauge theories*,
[1508.05552v1](https://arxiv.org/pdf/1508.05552v1), 23 August 2015.**
Read sec. 3.1, printed pp. 7–9, (3.1)–(3.6), and sec. 3.4,
pp. 14–15, (3.43)–(3.45) and the qualifications between them. The
Symanzik expansion concerns full expectations. Total derivatives remain
in higher correlations and with boundaries that break translation
symmetry. The subsequent simplification assumes translation invariance;
it supplies no bound for our selected box group. Retain these derivatives.

**Official target version.** On 2026-10-14 the
[Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
still links the 14-page Jaffe–Witten
[*Quantum Yang–Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Section 4, printed p. 6, still requires a nontrivial theory on R^4 for
every compact simple group, the stated axiomatic strength and finite
positive mass. The target recorded in foundations/01 is unchanged.

## Approved continuation and stopping test

This review permits a bounded mathematical attempt on the exact TARGET:
start from L011's complete cubic probe jet and the signed joint
cumulants, using existing residual/action definitions and Gaussian
connected identities by citation. A necessary local specialization is
their actual forest-coordinate contraction with the nonlinear flow
integral retained. Reproving general flow renormalizability or matched
Ward finiteness would not answer it. Neither a new reduction nor a
limit is derived or approved as a mathematical result in this turn.

Essential continuation inputs are L008 L010 L011 L018 L019 L020 L021
L022 L028 L155 L180, with L026's recorded covariance-growth obstruction
retained. Keep both actual probe sectors, all insertion subtractions,
physical faces and corners, constant axial modes, full heat sums and
flow times arbitrarily close to zero. Do not assume that the selected
group is forest invariant, that its separate terms converge, or that
their joint cubic coefficient vanishes.

Continue the mechanism if a complete signed reduction yields a
mesh-uniform cubic estimate and a controlled approximation whose errors
can be removed in the stated order; a finite reduction alone is an
honest partial result. Abandon a proposed estimate if it requires the
disproved termwise curvature transfer, an O(1) raw forest covariance,
dropped total derivatives or an unbounded flow-time interchange. A
rigorous stronger power or failure of convergence for an actual probe
would also settle this intermediate test negatively. An insufficient
absolute upper bound would not. Keep independent unresolved
f_(i,2),r_0 compensation, finer asymptotics, finite matching, reflected
error <=c_box/2 and continuum/infrared requirements visible.

## Mathlib and outcome qualification

Coverage of the exact joint-group limit and supporting nonlinear flow,
perturbative renormalization and lattice Ward theorems: **not checked**.
No matching Mathlib theorem or absence claim is made. Precise primary
citations above are coverage evidence; no new canonical lemma is needed
for this literature-only step. This is EXPLORATION / NOVELTY_UNCHECKED:
it supplies a completed scope comparison and research approval, not a
new mathematical input, coefficient, informative cutoff obstruction or
progress beyond the inspected results. The mathematical exploration
counter is unchanged. No lemmas or mathematical scripts were modified.
