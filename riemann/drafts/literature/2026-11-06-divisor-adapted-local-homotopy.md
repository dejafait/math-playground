# Divisor-adapted neighborhood correction: completed source comparison

TARGET: Assess a divisor-adapted local homotopy for solving L850's phase equation on a full neighborhood of an L853 transverse crossing, retaining finite multiplicity and separating J(p)=0.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded singular-volume/Moser, relative-Poincare, multiplicity/division and radial-graph searches; checked the named local phase assessments and transition failure records. Inspected Cardona-Miranda Section3 and Domitrz-Janeczko-Zhitomirskii Section2; reused the existing holomorphic-Moser and Morse-Bott comparisons, inspecting the latter's local Euler-homotopy proof for the newly relevant factor issue. No matching constrained neighborhood theorem located; no novelty inference.
SOURCE_EVIDENCE: Cardona-Miranda arXiv:1812.03800v3 Lemmas3.1-3.4/Theorem4 and proof, PDF pp4-6; Domitrz-Janeczko-Zhitomirskii Illinois J.Math.48(2004), Definitions2.1-2.2/2.5, Theorems2.3/2.6 and Lemma2.4 with proofs, pp807-808; Volk-Khesin published2026 Definition1.1/Theorem1.2 and Section3 local/complementary proof. Precise primary links, hypotheses and limitations below.
COMPARISON: Relative exactness supplies a primitive, not its membership in L850's real contraction image or multiplicity-preserving division. Folded and Morse-Bott equivalence theorems have different real-density and vanishing hypotheses; holomorphic Moser requires nondegeneracy. None supplies the requested real radial variation, including J(p)=0. L853 finite jets and L863 off-divisor bounds remain insufficient.
GAP: Construct or obstruct a full-neighborhood primitive with a smooth real L850 flux lift, retaining arbitrary finite n in F=w^nK and distinguishing J(p)=0. No such lift, estimate or range obstruction is established in this literature turn.
REASON: Essential comparison is now complete enough for one bounded EXPLORE attempt; ordinary exactness is available, while the real flux-image and multiplicity problem remains uncovered by the sources checked. The distinct prepared test needs separate next-turn approval; no new mathematics is invoked here.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target adds a singular full-neighborhood homotopy beyond the ready off-divisor and finite-jet scopes; primary relative-primitive and vanishing-factor proof coverage was essential and missing.
SCOPE: Source comparison for the exact fixed L853 crossing of the original cutoff graph, with L847 full form, L850 linearization, finite multiplicity, inherited actual-G qualifications and no assumption J(p)!=0. A local linear correction is not a nonlinear new positive germ, global supported solution or Xi sign theorem.

This target was nominated as a source review and has now received the
comparison below. Its essential local inputs are L847's full form,
L850's general phase derivative, L853's actual transverse coordinate
and finite multiplicity, and L863 only as the contrasting off-divisor
bound. The qualification of the actual crossing data in L853 must be
retained; no simple-zero hypothesis or nonvanishing complex Jacobian
J=1-det Du-i tr Du may be silently added.

The proposed distinct mechanism is a local homotopy adapted to the
vanishing factor of the closed form, rather than inversion of its
degenerate flux matrix. Source comparison must determine whether known
singular-volume-form homotopies, division results or local PDE results
actually provide a *real radial graph variation* v satisfying
D(Im q)_u[v]=-Im q_u on a full open neighborhood. A change of ambient
coordinates or an unrestricted complex vector field is not that result.
These were the nominated search directions; the inspected results and
their limitations are recorded below.

The finite-jet stop in ATTEMPTS/2026-11-06-transition-finite-jets-do-not-solve-range.md
remains valid. Reopening is proposed only for an all-orders neighborhood
mechanism with a different discriminator. Continue toward a bounded
creative test only if source review supplies a precise applicable
construction or a definite uncovered local claim with testable
compatibility conditions. Otherwise park this proposal; do not iterate
jets or rename the elliptic inverse. Even a successful conditional germ
would leave singular patch assembly, a global seed, nonlinear convergence,
density signs and actual-Xi all-degree positivity unresolved.

This file records no mathematical derivation. The completed source review
prepares the separate bounded test in
`drafts/literature/2026-11-06-divisor-weighted-real-flux-test.md`;
that newly written assessment requires separate approval before invocation.
Full matching Mathlib coverage is unchecked. No cross-notebook input.

## Completed review, 6 November 2026

The main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target could help only the singular linear stage of a
later fixed r=2,k=1 contour construction. It leaves the global seed,
patch compatibility, nonlinear convergence, nonnegative density, and
all-degree/shift transfer unresolved. This is source exploration, not
progress beyond the inspected literature or a new local solvability result.

### Local overlap and failures checked

Read L847's full form, graph identity and closed-form argument; L850's
general derivative and flux discussion; L853's hypotheses, crossing
factorization, complete finite-jet construction and applicable audit
scope; L863's hypotheses/conclusion. Reused the named collar-preserving,
off-divisor and transverse-divisor source comparisons. Read
`ATTEMPTS/2026-11-06-transition-finite-jets-do-not-solve-range.md` and
`ATTEMPTS/2026-11-06-collar-transition-inverse-stop.md`, and checked the
characteristic-barrier record. No existing neighborhood lift was found
in these specific paths. The primitive/monomial assessment instead
changes the graph derivatives and asks nonlinear punctured positivity;
it does not solve the linear equation about the fixed L853 cutoff graph.

Retain L850's existing signs: the required equation is div(Mv)=sigma,
where sigma=Im q_u. Its real primitive convention is
alpha=(Mv)_1 ds-(Mv)_2 dt. Mere existence of an ordinary primitive
was already known. Finite jets do not certify an identity on an open
neighborhood; failure of a chosen primitive to lift does not exclude
other primitives. A bump localization of a germ creates new residuals.
No old stop is upgraded to a global ban or erased.

### Primary source hypotheses and proof cases

1. **Relative primitives.** W. Domitrz, S. Janeczko and M. Zhitomirskii,
   *Relative Poincare lemma, contractibility, quasi-homogeneity and vector
   fields tangent to a singular variety*, Illinois J. Math. **48**(3)
   (2004), 803-835, DOI10.1215/ijm/1258131054;
   [Definitions2.1-2.2/2.5, Theorems2.3/2.6 and Lemma2.4 with proofs,
   pp807-808](https://pages.mini.pw.edu.pl/~domitrzw/poincare-ijm48%283%29.pdf#page=5).
   In smooth or analytic germs, a contraction to N preserving N supplies
   primitives for closed forms whose full coefficients vanish on N;
   the primitive has that same vanishing property. Read the homotopy
   proof and its piecewise-contraction extension, including the endpoint
   pullback argument. This is stronger than vanishing pullback to N,
   but does not state preservation of the nonreduced factor w^n or
   membership in the real image of M. The theorem is a cited primitive
   input only, not a theorem solving the graph equation. Verifying a
   chosen contraction and any stronger weighted property remains an
   application obligation; no specialization is proved here.

2. **Folded real volumes.** Robert Cardona and Eva Miranda,
   *On the volume elements of a manifold with transverse zeroes*,
   Regular and Chaotic Dynamics **24**(2) (2019), 187-197,
   DOI10.1134/S1560354719020047. Inspected
   [arXiv:1812.03800v3, 18December2018, Section3, Lemmas3.1-3.4,
   Theorem4 and its proof, PDF pp4-6](https://arxiv.org/pdf/1812.03800v3#page=4);
   no identity with the published text is asserted. In the standing
   compact oriented setting, the theorem compares two real top forms
   transverse to zero, with the same oriented zero hypersurfaces and
   matching ordinary/relative classes. Its Moser proof uses a common
   defining function, a nonvanishing real interpolant and a suitably
   vanishing primitive. Those hypotheses are not supplied by the
   complex factorization F=w^nK, nor does the theorem restrict its
   vector field to radial graph variations. Read the primitive and
   contraction steps, rather than importing the abstract alone. No
   automatic higher-multiplicity division claim from Lemma3.4 is
   adopted, and no new proof or correction of that lemma is attempted.

3. **Morse-Bott real volumes.** Luke Volk and Boris Khesin,
   *Morse-Bott Volume Forms*, Arnold Math. J. **12**(1) (2026),
   [Definition1.1, Theorem1.2 and Section3 proof](https://armj.math.stonybrook.edu/Articles/250611-Khesin/index.html),
   DOI10.56994/ARMJ.012.001.005. Reuse the earlier theorem comparison:
   compact connected oriented M, common oriented zero submanifold,
   nonnegative real densities with nondegenerate quadratic minima,
   equal relative classes. The conclusion is diffeomorphism equivalence
   fixing that submanifold. Here the newly relevant proof detail is
   local Euler contraction: after matching the quadratic factors,
   it constructs a primitive containing the common real factor and
   cancels that factor against a nonvanishing interpolant. The later
   complementary correction is supported away from the zero set.
   Read both stages. Their common-factor mechanism motivates a test;
   it is not an application to an arbitrary complex finite-order zero,
   an unknown sign, or the permitted radial variation. Reality and
   positivity cannot be assumed to obtain reality and positivity.

The holomorphic comparison is unchanged: Soldatenkov-Verbitsky,
arXiv:2109.00935v2, Definition2.1/Lemma2.4/Theorem2.5 and proofs,
already inspected in the collar assessment, requires nondegeneracy
and appropriate primitives. It does not extend across the present
vanishing form. Teixeira v7 Theorem3 remains an ordinary supported
divergence input; L863 does not remove its separate matrix inverse.

### Search and access record

Queries included `singular volume forms Moser theorem zeros relative
Poincare lemma Martinet`, `isochore singularity holomorphic volume form
Moser homotopy vanishing divisor real graph`, `singular volume form
relative Poincare lemma homotopy Euler divisor logarithmic vector fields`,
`holomorphic volume form zero divisor normal form Moser x^k dx dy`,
`"relative Poincare" "ideal" "multiplicity"`,
`"Moser" "vanishing" "multiplicity" "volume forms"`,
`"divergence" "complex" "Moser" "radial" graph`, and
`"phase" "graph" "holomorphic volume form" "divisor" deformation`.
The exact-constraint searches found no applicable matching theorem;
this bounded search does not establish novelty or nonexistence.

Generic isochore/Gauss-Manin, logarithmic-derivation and Mizohata results
are unread leads, not inputs. The near-symplectic PDF's opening definition
concerns a real 2-form on a 2n-manifold with codimension-three degeneracy;
its later theorems were not inspected or used. No broad survey is needed
to import any unverified conclusion from these leads.

Primary theorem/proof text was accessible through the web tool. Shell
PDF downloads failed DNS; no downloaded-source replay or image inspection
is claimed. This is not an essential access blocker. Mathlib coverage
of the full constrained result and supporting relative-homotopy theorem
was not checked; unknown coverage is not absence.

### Bounded continuation and stop test

The prepared test uses the full source on a disk in L853's w-coordinate,
a contraction preserving its center, and the freedom to adjust a
primitive by an exact real one-form. It must establish a smooth real
flux lift on the whole disk, not merely formal divisibility or jets.
Keep arbitrary finite n, K(p)!=0 and the qualified actual crossing;
separate J(p)=0, where the leading source may vanish to higher order.
No source above supplies that last lift. An explicit neighborhood
construction or a rigorously delimited obstruction to this weighted
homotopy mechanism is decisive evidence. Failure of one primitive alone
is only failure of that choice. If only finite jets or an uncontrolled
flat remainder emerge, stop this bounded mechanism and retain the
unfinished work; do not reset the earlier singular-route budget.
