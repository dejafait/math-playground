# Relative Coulomb representation: completed source comparison

TARGET: Assess whether L279's fixed-mesh source functional R(s,t) admits an exact local relative-Coulomb-slice representation through order g^2, retaining the gauge determinant, coordinate-density jets and every boundary normal link.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched lattice local Landau gauge, boundary Faddeev-Popov determinants, and finite-dimensional local quotient integration; inspected Polyak math/0406251v1 section 3.1 and Reshetikhin 1008.1411v1 sections 6.1–6.4, and compared the lattice boundary construction in hep-lat/9207009v1 section 6. Local duplicate and failure checks are recorded below; no exact published box coefficient was located and no novelty is inferred.
SOURCE_EVIDENCE: Polyak section 3.1, pp. 11–13, especially Remarks 3.1–3.2 and their change-of-variables argument; Reshetikhin Theorem 3, pp. 28–30, (31)–(34), and local qualifications on pp. 31–33; Luscher–Narayanan–Weisz–Wolff section 6, pp. 33–38, (6.1)–(6.23); Vassilevich hep-th/9709182v1 section 2, pp. 2–3, (4)–(8) and footnote 1. Direct links and access limits follow.
COMPARISON: General finite-dimensional local quotient integration covers the mechanism, provided a transverse local chart and its full pulled-back Haar density are verified. The slab formula has different boundary gauge freedom and is not an import for this cube. L003's quadratic curvature-law equality and L212's observable retraction do not supply the nonlinear measure identity.
GAP: Specialize the local inverse-function and quotient formulas to all-face pinned links; compute the complete density jet through degree two; retain both insertion jets and prove equality of the g^2 source coefficient with L279(22). These are explicit mathematical applicability obligations, not inaccessible essential source premises.
REASON: Ready general finite-dimensional coverage permits a separate mathematical specialization; no local slice, determinant jet or coefficient equality is derived in this literature-only step. The inaccessible 1986 lattice paper and unread 1988 lectures are not needed premises for the proposed direct local-coordinate proof.
SCOPE: Fixed even N, SU(2), a=8/N, L003's all-face relative cube, real f_*, all variable normal links, the exact two bare plaquette insertions and a local chart near the flat orbit. No global gauge fixing, nonlinear Hodge transport, uniform mesh estimate or continuum conclusion is covered.

## Exact scope and discriminating test

Essential local inputs are L003 and L279, especially (20)–(22) and
(31)–(34); L011 is only the already recorded expansion method. Keep
SU(2), real f_*, even N, a=8/N, the finite physical cube, all boundary-
contained links pinned and normal links variable. The proposed slice
is a *local near-identity* nonlinear gauge-coordinate construction
whose tangent condition is the relative d* condition. No global gauge
slice or absence of Gribov copies is assumed. No replacement of higher
jets by their linear Hodge transport is permitted.

First inspect primary hypotheses for local lattice gauge fixing and its
Jacobian, comparing the all-face relative boundary condition. Determine
whether a finite-mesh equality of the complete g^2 source coefficient
can be imported or specialized, including the gauge determinant and
each density/observable correction. Approval requires a concrete
formula and explicit applicability obligations, not the phrase gauge
independence. Missing hypotheses remain missing. A source on a periodic
box or a time-boundary slab needs an explicit comparison, not automatic
transfer. Reuse earlier source coverage only where its hypotheses match.

Plausible downstream use: replace long forest-coordinate internal lines
by a representation with local elliptic covariance, while retaining
exactly the same coefficient. Such an identity alone would not prove
its logarithmic bound: cancellations, boundary estimates, the uniform
higher remainder, a physical trajectory, continuum axioms, nonzero
physical sector and finite positive infinite-volume mass remain open.
The coverage review should park the target if an essential determinant
or boundary premise cannot be justified, and preserve the stopped
contraction evidence. This review approves only a future specialization
attempt under the obligations below. It proves no representation.
Mathlib coverage of the complete representation is not checked.

## Sources actually inspected

**Polyak.** M. Polyak, *Feynman diagrams for pedestrians and
mathematicians*, [math/0406251v1](https://arxiv.org/pdf/math/0406251v1),
12 June 2004, section 3.1, printed pp. 11–13. The free, proper,
isometric action and invariant measure are explicit. For a local section,
Remarks 3.1–3.2 identify the quotient Jacobian as the determinant of
the section/orbit tangent map, or the orbit derivative of the constraint
in the delta-function formulation. The accompanying proof changes
variables along an orbit. The polar-coordinate example checks the
normalization and warns about multiple intersections. This gives a
concrete finite-dimensional density prescription, rather than permission
to discard a determinant.

**Reshetikhin.** N. Reshetikhin, *Lectures on quantization of gauge
systems*, [1008.1411v1](https://arxiv.org/pdf/1008.1411v1),
8 August 2010, sections 6.1–6.4, printed pp. 28–33.
Theorem 3 and its proof, (31)–(34), assume a free action, invariant
volume, a section meeting each orbit once, and an invertible matrix
\(L^b_a=e_a\phi^b\). The local discussion on pp. 31–32 permits
sections near critical orbits for asymptotic coefficients. Equation
(38) retains \(\det L\,\delta(\phi)\). The explicit section 6.3
calculation checks the semiclassical determinant; higher-order diagram
independence is left as an exercise. Consequently the proposed proof
must use an actual local change of variables, not cite that exercise
as a proved all-order identity. The oscillatory expansion is not a
Laplace-remainder theorem for this notebook.

**Boundary lattice comparison.** M. Lüscher, R. Narayanan, P. Weisz
and U. Wolff, *The Schrödinger functional — a renormalizable probe for
non-abelian gauge theories*, [hep-lat/9207009v1](https://arxiv.org/pdf/hep-lat/9207009v1),
9 July 1992, section 6, printed pp. 33–38. The gauge group is the
boundary stabilizer modulo a constant Cartan subgroup. In (6.3) its
infinitesimal fields have a constant diagonal lower-boundary value,
zero upper-boundary value and spatial periodicity. Equations
(6.10)–(6.18) specify the gauge function and ghost determinant;
(6.16) includes its variation through second order in the coupling.
The integral is restricted to a neighborhood of the background,
neglecting exponentially small terms. Equation (6.19)'s uncomputed
\(O(g_0^2)\) Haar correction cannot be dropped for L279's coefficient.
Section 6's basic-lemma reference [47] is Lüscher's *Selected Topics
in Lattice Field Theory* (1988 lectures), not the 1986 paper below.

**Boundary warning.** D. V. Vassilevich, *The Faddeev–Popov trick in
the presence of boundaries*, [hep-th/9709182v1](https://arxiv.org/pdf/hep-th/9709182v1),
25 September 1997; published *Phys. Lett. B* 421 (1998), 93–98,
DOI 10.1016/S0370-2693(98)00008-2. Section 2, printed pp. 2–3,
requires preservation of a common field boundary domain and unique
gauge-parameter solution with the same ghost boundary domain for
both gauges. Footnote 1 restricts the argument to linearized gauge
transformations. This supports the boundary checklist; it does not
prove a nonlinear lattice slice or transfer smooth-boundary continuum
domains to cubical cochains.

## Applicability obligations for a later mathematical attempt

The selected mechanism is ordinary finite-dimensional local quotient
integration, with the analytic inverse function theorem and ordinary
change-of-variables theorem as standard named inputs. A second proof
of general Faddeev-Popov theory is unnecessary. The specialization is
needed because none of the inspected sources writes the following
box-specific density and source coefficient. This is a proposed proof
specification, not a result established in this turn.

1. Use the product group of transformations at interior vertices,
   identity at every boundary vertex. Use the product of Haar measures
   on every variable link, including normal end links. Verify a free
   action and preservation of the pinned link constraints. Do not
   import the slab's Cartan quotient or its boundary ghost row.
2. Let \(H=\ker d^*\) in the full relative link space, with the
   positive-adjoint convention of L003. Test the local product map
   \(\Psi(v,h)=h\cdot\exp v\), for \(v\in H\) small and \(h\)
   in the boundary-fixed gauge group. Verify its derivative is an
   isomorphism using L003's relative decomposition and positive
   Dirichlet zero-cochain Laplacian. Establish local orbit uniqueness;
   a merely infinitesimal complement is not a global section. Here
   relative Coulomb means the full four-dimensional \(d^*\) condition,
   not the spatial-only Coulomb gauge.
3. Obtain the quotient density from \(\Psi^*(\prod_e dU_e)\) relative
   to \(dv\,dh\), with Haar on the gauge group. Equivalently use
   the cited orbit-derivative determinant with the full coordinate
   density and the constraint-volume factor. Fix the determinant
   orientation or absolute value and every normalization; only a
   constant independent of the sources can be suppressed. Compute
   both degree-one and degree-two density contributions or prove
   that a degree-one contribution vanishes. The forest \(M_2\)
   cannot simply be reused on all links, and the nonlinear determinant
   cannot be replaced by its value at identity.
4. Apply the exact local change of variables to the gauge-invariant
   source-deformed action \(\mathcal S-sH_{h_-}-tH_{h_+}\).
   Use L003's quotient minimum and compact-complement gap, with
   explicit control of the small-source domain, to justify localization
   at fixed mesh. Keep the whole normalized source functional;
   equality of individual action or Haar summands is not sought.
5. Expand this localized integral by the already audited L279 method,
   retaining action jets through degree four, both insertion jets and
   the full density jet. Compare the \(g^2\) logarithmic coefficient
   with exactly \(R(s,t)\) in L279(22), allowing only explicitly
   identified source-independent normalization constants. Take the
   mixed source derivative only after this equality is justified.
   No uniform source-asymptotic differentiation is presumed.

The density prescription in item 3 and the cited finite-dimensional
formulas are sufficient source coverage to attempt these obligations.
Failure of local invertibility, orbit uniqueness, normal-link retention
or density matching stops the specialization. Success supplies a
different representation of the same coefficient, not a logarithmic
estimate. No derivation of any of items 1–5 was performed here.

## Duplicate and failure comparison

L003 section 1 transports only the quadratic curvature law. L279(7),
(20)–(34) and its audit fix the source and density to be reproduced.
L212(4) retracts a complete quartic flowed observable with finite gauge
jets; its statement expressly concerns initial arguments of that
observable, not a nonlinear interacting measure. L198's exterior
gauge-slice cancellation likewise does not construct a quotient density.
Their relevant statements were inspected, without loading unrelated
proofs. Neither is the proposed representation already proved.

ATTEMPTS/047 preserves two unproductive direct-contraction attempts.
The 2026-10-04 compact-BRST assessment is reused for the distinction
between global compact normalization and a local weak-field chart.
Its historical stop is not a ban on the present local construction.
No new global BRST integral or field-dependent measure is introduced.
The source version and exact target recorded in foundations/01-target-and-scope.md
were reused; no route change requires another Clay statement search.

## Bounded search and access record

Queries included `lattice gauge theory local Landau gauge Faddeev Popov
determinant Dirichlet boundary perturbation theory`, `Balaban lattice
gauge fixing local gauge transformations boundary conditions theorem`,
the exact Lüscher–Weisz 1986 title and DESY-85-075 report number, and
`finite dimensional Faddeev-Popov determinant slice theorem`.
The last search led to the inspected finite-dimensional arguments.

M. Lüscher and P. Weisz, *Efficient numerical techniques for perturbative
lattice gauge theory computations*, *Nucl. Phys. B* 266 (1986), 309–356,
[DOI 10.1016/0550-3213(86)90094-5](https://doi.org/10.1016/0550-3213(86)90094-5),
DESY-85-075: only the publisher abstract and
[DESY record](https://bib-pubdb1.desy.de/record/324626) were available.
The record labels PDFs restricted; its PDF link and the DESY report
index's KEK link failed through the browser. No theorem or boundary
hypothesis from this paper was inspected. Lüscher's 1988 lectures and
Bałaban's 1985 gauge-fixing paper remain unread leads, not premises.
An initial mistaken arXiv identifier 1008.1418 resolved to an unrelated
paper and was discarded; the inspected Reshetikhin version is 1008.1411v1.

The 1986 access failure therefore does not block this bounded direct
specialization. Should the proposed proof require a stronger lattice
theorem than the inspected finite-dimensional formulas, stop and
record new missing coverage rather than silently importing an unread
lead. This review establishes neither novelty nor a mathematical
representation, and changes no lemma, mathematical script or DAG edge.
