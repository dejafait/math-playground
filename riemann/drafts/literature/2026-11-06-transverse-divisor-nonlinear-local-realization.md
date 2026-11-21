# Transverse divisor and nonlinear local realization — completed source comparison

TARGET: Determine whether the full L847 form admits a smooth local real radial graph through a fixed L853 crossing pair, transverse to its multiplicity-n G(z_1) zero, with G(z_2)(z_1-z_2) nonzero nearby and q_u strictly positive on a punctured neighborhood, allowing a complex-Jacobian zero at the crossing.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for isolated complex points, arbitrary-index graph models, positive pullbacks of holomorphic forms with zeros, and radial graphs; reused the full-phase/collar comparisons and targeted transition failure records. Exact queries, primary reading scope and limitations appear below; no matching actual-form realization theorem was located and no novelty is inferred.
SOURCE_EVIDENCE: Inspected Forstneric AIF37(1)(1987), Section2 Definition2/Lemma8 with determinant proof and monomial example pp14-16; Forstneric JGA13(2003), Section1 pp78-79 and Theorems2.1-2.2/cancellation discussion pp82-83; Lebl SCV v4.4 Theorem1.2.1 and proof pp20-21; Chaperon 9January2007 Section1 Corollary1 and real/complex justification p2. Precise citations and applicability boundaries below.
COMPARISON: The inspected arbitrary-index examples prevent a generic elliptic/hyperbolic dichotomy from excluding all allowed degeneracies. The isotopy/Stein conclusions do not impose the specified full-form phase or angular graph condition. Standard analytic coordinate tools and explicit complex-point models suggest a bounded construction test, not an imported actual-G positive germ. Prior nonvanishing-volume and fixed-base linear comparisons remain insufficient for an automatic existence import.
GAP: Actual nonlinear realization or an obstruction retaining arbitrary multiplicity, radial angular projection and the full oriented density remains unproved. No index identity for this density, holomorphic normal form for it, or positive germ is established here. L853 remains unaudited and must be checked before using its particular crossings as established data.
REASON: Essential source comparison now distinguishes general complex-point models from this exact local positive-density problem; no essential access blocker persists. Recovery selects a concrete primitive/monomial construction at an explicitly hypothesized pair, independent of the exhausted fixed-cutoff linear-range mechanism and of L853's provenance. Its separate assessment is saved for next-turn approval.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identified a changed nonlinear target and essential unread complex-tangency/index coverage; this review supplies that comparison without a new mathematical derivation.
SCOPE: Exact TARGET, with all original qualifications and arbitrary n retained. EXPLORE records adequate comparison, not theorem applicability or permission to repeat fixed-cutoff linear-range tests. The newly selected construction target is recorded separately in 2026-11-06-primitive-monomial-local-germ.md.

## Completed review and source-level negative evidence

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The local germ could remove one possible local obstruction to a future
global contour construction. It cannot supply global extension, sign,
exchange compatibility, other orders/shifts or that main positivity.
The original nomination is retained below as its scope record; its
source-required status is superseded by this completed comparison.

Read L847(1)–(5), including the full oriented pullback, and L853's
hypotheses and crossing argument through (12) and its local-coordinate
check. That reading identifies the target, not an audit of L853 or a
replay of its inherited numerical inputs. Reused the full-phase,
exchange-diagonal exact-collar and collar-linear-phase assessments.
Read the characteristic-barrier and finite-source-jet ATTEMPTS records.
The former's third-exploration stop remains in force for that mechanism;
the latter supplies no nonlinear neighborhood. Targeted searches in
these actual-G/collar assessment and transition failure paths found no
existing solution of the local nonlinear target. This is a bounded
duplicate check, not a novelty certificate.

### Primary sources actually inspected

Franc Forstnerič, *Analytic disks with boundaries in a maximal real
submanifold of C2*, Ann. Inst. Fourier **37**(1) (1987), 1–44,
DOI10.5802/aif.1076, [Section2, Definition2, Lemma8 and example,
pp14–16](https://users.fmf.uni-lj.si/forstneric/papers/1987Ann.Inst.Fourier.pdf#page=15).
For a C1 graph w=g(z) over an open neighborhood of the closed unit
disc, with g_bar_z nonzero off the origin, Lemma8 computes the local
index by its boundary winding. Its proof uses the determinant of the
real tangent frame. The following models w=z^k conjugate(z)^l have
index k-l+1; positive integers k,l with l>1 already give every integer.
The quadratic comparison gives +1 for elliptic and -1 for hyperbolic
points under the stated nondegeneracy assumptions. Arbitrary indices
remain possible without those assumptions. These are known model and
index facts; no index bound for L847 follows. The source gives no
specified positive pullback, angular graph or actual-G realization.

Franc Forstnerič, *Stein domains in complex surfaces*, J. Geom. Anal.
**13**(1) (2003), 77–94,
[Section1 pp78–79; Theorems2.1–2.2 and discussion pp82–83](https://users.fmf.uni-lj.si/forstneric/papers/2003J.Geom.Anal.pdf#page=6).
The local graph index uses an isolated zero of g_bar_z. Theorem2.1
approximates an immersion of a closed real surface into a complex
surface by regularly homotopic immersions with special complex points;
the oriented nonpositive-index condition permits removal of elliptic
points. The embedding case uses isotopy. Read the cancellation argument:
opposite indices, and the same orientation sign when oriented, are
required; the modification agrees near the chosen disc boundary.
Theorem2.2 assumes the special hyperbolic models and gives regular
Stein neighborhoods. These results constrain neither the phase of the
specified vanishing form nor radial angular projection. No isotopy or
Stein theorem is imported to assert our germ. Its references to the
original cancellation proof are therefore nonessential unread leads.

Forstnerič, *Intersections of analytic and smooth discs*, Contemporary
Mathematics **137** (1992), 235–244,
[p237, local-index definition](https://users.fmf.uni-lj.si/forstneric/papers/1992Contemp.Math.pdf#page=3),
was checked for terminology and agrees with the graph winding
description. Its analytic-disc intersection theorem is not an input:
no analytic disc with the stipulated common boundary is supplied here.

Jiří Lebl, *Tasty Bits of Several Complex Variables*, version4.4,
31May2026, [Theorem1.2.1 and proof, pp20–21](https://www.jirka.org/scv/scv.pdf#page=20):
a function holomorphic on a polydisc and continuous on its closure has
a power series there, uniformly absolutely convergent on compact
subsets; conversely such a series is holomorphic. Read the Cauchy-kernel
expansion, uniform convergence and converse cases. Use a smaller closed
polydisc within any proposed holomorphic neighborhood. This provides a
coordinate-construction tool, not a normal-form or positivity theorem.

Marc Chaperon, *On the Cauchy-Kowalevski theorem*, 9January2007,
[Section1, Corollary1 and justification, p2](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2):
an analytic local map of real or complex Banach spaces has analytic
inverse when its derivative is invertible; the analogous invertible
partial derivative gives an analytic implicit function. The complex
case uses the C-linear inverse derivative, the real case complexification.
This supports both a holomorphic coordinate change and a real angular
reparametrization only after their distinct derivatives are checked.
Neither derivative condition is established in this literature step.

Reuse Lebl CA v1.10 Theorem2.4.7's isolated-zero/Taylor-factorization
coverage from the product-obstruction audit; the actual G is entire
and G(0)>0. Additionally read [CA Corollary3.2.12 and its segment-primitive
proof via Proposition3.2.11, pp67–68](https://www.jirka.org/ca/ca.pdf#page=67).
It assumes a holomorphic function on an open star-like plane domain.
A parameter-dependent coordinate still requires joint holomorphicity;
this one-variable primitive result alone does not assert it. No reproof
of these standard results is needed in the later application.

### Recovery comparison: three distinct mechanisms

1. **Generic complex-point exclusion.** A proposed universal exclusion
   using only elliptic/hyperbolic indices is unsupported at arbitrary
   retained multiplicity: the inspected models include higher indices.
   Retire that proposed automatic import, not the local target.
2. **Stein isotopy/cancellation.** The primary hypotheses and conclusions
   above do not preserve the full density or angular graph condition.
   This is no automatic positive-germ theorem. Do not pursue a chain
   of isotopy-source approvals to replace the missing phase calculation.
3. **Primitive coordinate and explicit monomial germ.** Select a bounded
   nonlinear construction test under explicitly hypothesized local pair
   data. It uses a known model rather than an index-only exclusion and
   need not solve a fixed-cutoff PDE, match its first derivative, or rely
   on unaudited L853. The remaining actual-form and angular-orientation
   specialization is mathematical work reserved for a later turn.

The selected test and its exact input/threshold boundary are in
`2026-11-06-primitive-monomial-local-germ.md`. This is materially different
from the parked linear-range/finite-jet sequence. No normal-form identity,
local existence proof, index cancellation for the actual form, or new
lemma has been derived here. The source-level negative evidence changes
the selected mechanism; it does not obstruct an actual germ or RH.

### Searches, access and remaining limitations

Queries included `complex points real surfaces C2 index isolated complex
tangency Bishop Forstneric Lai`, `degenerate holomorphic volume form real
positive totally real submanifold divisor special totally real`,
`Forstneric Analytic disks with boundaries Lemma 8`, `holomorphic volume
form zeros local normal form w^k dz dw real surface complex tangent`,
`holomorphic volume form divisor normal form local real surface`,
`complex tangency positive holomorphic volume`, and `radial graph complex
tangent`. Stronger global Stein results were compared, not applied.
Aggregator/forum hits supplied no theorem evidence. No exact realization
result was identified; this failure to find one is not evidence of novelty.

The publisher AIF PDF returned403; the author-hosted primary PDF worked.
Screenshot calls returned no readable images; no visual inspection is
claimed. The graph/index statement, determinant proof, examples and both
nondegenerate comparison cases were read in primary indexed text and
cross-checked against the 2003 definitions. There is no persistent
essential source blocker. Mathlib coverage of the full result and of
these supporting tools was not checked. No cross-notebook input.

## Scope of the proposed test

Fix one of L853's qualified sufficiently narrow crossings p, with
z_1(p)=zeta an actual G zero of finite multiplicity n>=1 and
G(z_2(p))(z_1(p)-z_2(p)) nonzero. The new local graph is required
to retain this pair of values at p, but may change its derivatives.
Transversality means that theta -> z_1(theta) has real rank two at p.
After shrinking a neighborhood, the other G factor and the collision
factor must remain nonzero. The full original angular orientation is
used, and q must be a strictly positive real scalar at every other
point of the neighborhood. An identically zero pullback is excluded.

The question deliberately allows J=det(I-iDu)=0 at p, retaining the
entire complex Jacobian. It does not assume its index, sign, multiplicity,
or realizability. A theorem about nondegenerate totally real surfaces
must not be applied at p without checking its scope. Neither a formal
jet nor an arbitrarily small residual meets this local smooth target.
No matching of the cutoff's first derivative, a global exchange law,
or a global collar extension is demanded of this germ; these would be
additional downstream obligations. The exchange partner can only be
considered after the local result and its compatibility are understood.

This is a materially different test from pointwise inverse failure,
finite linear source jets, or closed flux barriers. It studies the
nonlinear local geometry of a proposed positive contour. Success would
identify a possible local model for a later global construction;
an obstruction would exclude only such transverse crossings, since a
global deformation might change or remove them. Neither outcome alone
settles the all-degree mixed-positivity gap L030–L032/C032a.

## Required comparison and continuation limits

Reuse the actual-form definitions in L847, the retained actual-G inputs
L775 and L778(2)–(5)/step433, and the relevant L848/L849/L853 arguments.
L853 and the new L854 are unaudited; check L853's transversality and
other-factor nonvanishing before substantively using its chosen pair.
L854 motivates the route decision but is not a mathematical premise
of this local target. Preserve every multiplicity and input qualification.

Search exact local statements and standard terminology, including
complex points of real surfaces in complex dimension two, local
complex-tangency indices, and real or positive pullbacks of holomorphic
volume forms with a divisor. These are leads, not imported theorems.
Read primary statements and the essential positive/negative index,
regularity, orientation and isolated-degeneracy proof cases before
declaring coverage. Compare with the existing full-phase assessment
without treating its undeleted zeros as approval of every local theorem.

The discriminating mathematical test, only after separate source
approval, is an actual smooth germ with the stated punctured positivity
or a precise obstruction retaining the allowed J zero and multiplicity.
No numerical script, local theorem, proof of an index identity, or new
lemma is authorized by this nomination. Full matching Mathlib coverage
is unchecked; no cross-notebook input is proposed.
