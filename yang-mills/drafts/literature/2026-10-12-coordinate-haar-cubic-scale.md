# Coordinate-Haar cubic-scale target — completed source assessment

TARGET: Determine whether L018's complete coordinate-Haar response has a vanishing a^3-scaled limit for both actual L010 probes in the straight lower-rooted forest.
CHECKED: 2026-10-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched exact coordinate-Haar/forest terminology, SU(2) measure vertices, axial/tree-gauge ultraviolet estimates and gradient-flow finiteness; inspected primary Haar formulas and renormalization proof cases below and reused the finite forest/Ward assessment.
SOURCE_EVIDENCE: Read Burgio–Feo–Peardon–Ryan hep-lat/0303005v1 sec. III.B (21)–(24), pp. 9–10; Lüscher–Weisz 1101.0963v2 secs. 7.2–7.4, pp. 21–23, and 8.4, p. 25; reused 2026-10-04-forest-compensated-ward-identity.md and 2026-09-27-fixed-box-one-loop-locality.md; inspected L018(1)–(7), L011(5)–(6), L026(1)–(5), ATTEMPTS/009 and ATTEMPTS/011.
COMPARISON: Known measure vertices and finite forest machinery cover the existing finite contraction, not its pinned-forest cubic asymptotic; full renormalized flowed-correlation finiteness cannot be assigned to one coordinate-dependent cumulant with an unflowed residual.
GAP: No inspected theorem gives a^3 Gamma^M_(i,F)->0 or a nonzero cubic coefficient for both specified probes; the exact signed trace with growing lower-rooted paths requires a separate bounded mathematical attempt.
REASON: Adequate bounded source comparison found no matching result and no essential access blocker; approve only the unchanged forest-specific scale test, with no novelty claim or presumption of a zero limit.
LITERATURE_REASON: Changed response group and cutoff asymptotic: L018's coordinate-Haar term is outside the ready no-upper cubic and finite compensator assessments.

This separate literature review approves EXPLORE for the exact TARGET.
No new mathematical result or calculation was produced. The finite
contraction is reused without reproof; no external result is imported as
an ultraviolet bound. The mathematical target and all qualifications
below are unchanged.

The group is exactly L018(4)'s Gamma^M_(i,F)=-kappa(f_(i,0),r0,M2),
including its minus sign, three colors and the exact forest covariance.
Use SU(2), both actual L010 probes at tau=1/16, all-face relative fixed
links on (-4,4)^4, a=8/N through admitted even meshes and bare
small-coupling expansion at fixed mesh before refinement. Retain all
pinned rows, lower-rooted prefixes, zero modes and exterior heat sums.
This target is restricted to that named forest and response term.

ATTEMPTS/009 stops assigning an isolated density term a
forest-independent ultraviolet meaning. The proposed limit does not
make that assignment: its use is to determine whether this same-forest
term can contribute at the cubic scale left by L147. This distinct
scaled test has a known exact trace and a concrete zero threshold.
ATTEMPTS/011 stops uniform raw-link O(1) bounds. Neither generic
forest invariance nor damping of an unflowed internal line may be
assumed. The separated trace order and signed residual must be kept.

Essential input IDs for any later mathematical attempt: L018 L011
L017 L026; L019 constrains coordinate/forest compensation. L147 L124
L084 supply the same-forest comparison, with L070 L079 L080 L082
retaining the constant, continuum diagnostics and sign qualifications.
The finite contraction is ready; its ultraviolet estimate is not.
L010's Haar-divergence insertion is a different term and is not added
or substituted for the coordinate density.

Continue after source approval if the exact trace yields a justified
zero limit, a finite nonzero coefficient or a discriminating obstruction.
Abandon a mechanism that only repeats an insufficient absolute raw-link
bound or assumes forest invariance for this isolated term. A zero limit
would eliminate one compensation source only; all other action,
insertion/observable/flow jets, finer powers/logarithm, interacting error
<=c_box/2, continuum axioms, reflection positivity, infrared control and
finite positive mass remain open. No candidate exists.

Full matching Mathlib coverage: not checked. Unknown is not absence.

## Search and primary-source comparison

Queries on 2026-10-12:

- `lattice gauge theory Haar measure term perturbation theory axial gauge tree gauge ultraviolet divergence flowed observables`
- `SU(2) Haar measure perturbation theory measure term quadratic lattice gauge Ward identities`
- `"coordinate Haar" "forest" gauge`
- `"Haar measure" "axial gauge" lattice perturbation ultraviolet`
- `"tree gauge" "gradient flow" measure perturbation`

Searches did not establish an exact match; this is not evidence of novelty.
Secondary snippets were discovery aids only. No source is inaccessible
that is essential to the present bounded trace test.

**G. Burgio, A. Feo, M. Peardon and S. M. Ryan, *Gauge Theories on a
2+2 Anisotropic Lattice*, [hep-lat/0303005v1](https://arxiv.org/pdf/hep-lat/0303005v1),
6 March 2003, section III.B, printed pp. 9–10, (21)–(24).**
The Wilson SU(N_c) lattice expansion uses exponential link fields and
adjoint generators. Equations (21)–(22) give the Haar Jacobian and its
negative logarithm. Equation (23) gives the quadratic measure action
N_c sum(phi^a phi^a)/24. For N_c=2 and dimensionless link angle phi=gx,
this agrees with L011's positive g^2 M2 and hence a negative density
insertion. Equation (24) is the corresponding two-leg measure vertex.
This comparison checks normalization only; it adds no result to L011.
The momentum-space covariant-gauge setup, with additional ghost terms
in III.C, does not give this boundary-rooted forest's signed cumulant,
probe matrices or refinement estimate. A local measure vertex does not
make the internal forest covariance local or bounded.

**M. Lüscher and P. Weisz, *Perturbative analysis of the gradient flow
in non-abelian gauge theories*, [1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
JHEP 02 (2011) 051, sections 7.2–7.4, printed pp. 21–23,
(7.6)–(7.8); section 8.4, p. 25.**
The pure SU(N) argument uses dimensional regularization on continuum
spacetime and already renormalized four-dimensional fields/parameters.
Its flow half-space boundary is t=0, not a physical cube face. Section
7.2 excludes additional bulk counterterms through directed flow trees;
7.3 restricts possible flow-boundary counterterms by dimension and
symmetries; 7.4 uses the BRS identity to force both coefficients to zero.
Section 8.4 discusses lattice extension as an expectation based on exact
symmetries. The finiteness claim concerns full renormalized correlations,
not an individual measure contribution. Neither physical relative faces,
a forest-coordinate insertion nor this unflowed residual is covered by
a matching trace theorem. No vanishing cubic limit follows by citation.
This recheck serves the changed isolated-density scope, rather than a
new review of already-ready full-response machinery.

The ready finite forest assessment is reused for Freidel–Livine's tree
path map/change-of-tree measure statement and Ligterink–Walet–Bishop's
retained path derivatives; their precise references and inspected ranges
remain in that assessment. The fixed-box locality assessment already
records why Adams–Lee's momentum-integral theorem and slab/corner
results cannot be applied without additional finite-kernel hypotheses.
No reproof or repeated broad source audit is needed here.

Unread leads, not theorem evidence: Balaban, CMP 102 (1985), 255–275,
[primary repository PDF](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46460/220_2005_Article_BF01229380.pdf?sequence=1),
was returned for small-field axial-gauge Haar densities; its hypotheses
and estimates have not been inspected in this review. Modified-axial-gauge
Hamiltonian sources and recent claimed mass-gap preprints were also
returned but are not inputs or evidence for this exact trace. Any future
use requires its own theorem-level comparison. None is needed to state
the finite Gaussian attempt, which uses already-proved local inputs.

## Target version and decision test

Rechecked the current [Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
and its linked Jaffe–Witten *Quantum Yang–Mills Theory*,
[14-page official description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
section 4, printed p. 6, on 2026-10-12. It retains every compact simple
group, nontrivial R^4 theory, the stated axiomatic strength and finite
positive mass. The scope recorded in foundations/01 is unchanged.

Approve one mathematical attempt using L018(4) as an exact input,
with L011, L017 and L026 supplying its conventions, compensated
residual and covariance constraints. L019 remains a warning about full
forest compensation, not a premise of isolated invariance. Comparison
with L147 uses L124/L084 and their L070/L079/L080/L082 qualifications.
A justified o(a^-3) bound proves the sought zero threshold; a finite
nonzero coefficient or a precise obstruction is also informative. An
O(a^-3) absolute bound alone leaves the threshold unresolved. Stop any
mechanism resting only on disproved uniform raw-link bounds, final-time
damping of the internal line, or a forest-independent interpretation.
A result concerns this one response term only; it leaves the other jets,
finer asymptotics and every nonperturbative construction gap open.

Mathlib coverage of the full matching asymptotic and supporting trace
estimates: not checked. No absence or matching library theorem is claimed.
