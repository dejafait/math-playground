# Proposed full-phase deformation source review

TARGET: Assess whether an underdetermined elliptic deformation method can correct the L847 full phase equation on off-divisor coupled graph patches, with a quantitative right inverse and explicit compatibility conditions.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded McLean/calibrated-deformation, support-preserving underdetermined-elliptic and Banach-inverse searches; reused the inspected collar-linear-phase and actual-G graph assessments. Read Delay 1003.0535v4 primary hypotheses and essential proof cases. No exact actual-G nonlinear correction theorem was located; no novelty inference.
SOURCE_EVIDENCE: Delay 1003.0535v4 Definitions1.1-1.2, Theorems1.3/3.8/5.1, Proposition3.6, Section4, Section8 and Section9.1 inspected; Section9.6 is a model-specific nonlinear lead, not an imported general theorem. Reused Teixeira Theorem3 and Guillemin-Sternberg pullback differentiation from the collar assessment. McLean full text and Hamilton full text remain unread after access failures; neither is an essential input to the narrower linear test.
COMPARISON: Known results provide conditional linear right inverses with full adjoint compatibility and domain-dependent estimates. L850 already supplies the actual flux matrix and determinant identity; recomputing them would duplicate prior work. Neither off-divisor status alone nor a generic deformation-space theorem supplies the required nonlinear correction, seed or sign control.
GAP: Test the actual operator's ellipticity, adjoint kernel and supported norm bound on a specified compact patch; these are application obligations, not a missing general linear source. Nonlinear convergence, global compatibility, divisor extension, a global seed and sign margins remain unproved and outside the newly prepared linear test.
REASON: Source coverage now supports a bounded linear feasibility test before seeking a nonlinear theorem. Continue only at this narrower scope; no calibrated-deformation or nonlinear existence theorem is imported. New ready continuation requires separate next-turn approval.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from open ampleness to an equality-based PDE mechanism and lacked essential operator/right-inverse coverage; this turn fills that comparison without mathematics.
SCOPE: Source comparison for actual G,R,C,F and full L847 graph density. Prepared continuation tests the L850 linearization on compact off-divisor smooth patches with explicit boundary support and compatibility, allowing ellipticity to fail. No global seed, prescribed annular filling, divisor estimate, nonlinear theorem, exchange-preserving global graph or Xi sign is approved.

## Completed source comparison, 6 November 2026

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate purpose is a controlled local phase correction, potentially
usable in a later fixed r=2,k=1 contour construction. A local linear inverse
would still leave a nonlinear correction, an actual seed, global assembly,
divisor contacts, all other orders/shifts and the positivity transfer open.
This turn makes no new operator calculation or mathematical assertion about
its solvability. The outcome is source exploration, not a new lemma.

### Local overlap and retained failures

Used the supplied full PROOF/DAG first. Read L847 hypotheses, (1)-(5)
and the pullback/homotopy proof; L862 hypotheses and principal-slice
conclusion; L850 hypotheses, (2)-(5) and their full variation proof;
L851 hypotheses/conclusion and its residual-support argument; L852's
transition-zero and value-level discussion; L853 hypotheses/conclusion
and its input scope. Reused the completed collar-preserving-linear-phase
assessment and actual-G-radial-graph-full-phase assessment. The relevant
existing L850 identities, not new derivations here, are

    D(Im q)_u[v] = -div(M_u v),
    M_u = P I + Q adj(Du),
    det M_u = |F(Phi_u)|^2 - Q Im q_u.

L851 already gives an exterior lift and transition-supported residuals.
L852 retains forced transition form zeros; L853 supplies only finite
source jets. Thus this review must not rename that unresolved singular
global lifting problem as an elliptic one. The proposed next test concerns
compact off-divisor patches and must test the matrix rather than assume
invertibility from F!=0. L850's general identities are unaudited inputs;
their signs must be checked when applied, without replaying its separate
numerical certificate. L849/L851/L853 scalar analytic implicit-function
uses do not constitute a quantitative PDE inverse.

Read the recorded full-phase-two-period and nongraph-fixed-chart-annular
stops. The former found compatible periods, not a graph; the latter
excludes specified collars in a fixed chart with positive angular rank.
Neither local linear solvability nor deleting a divisor would undo these
statements. L862's open-ample obstruction remains intact.

### Primary linear theorem and estimate inspected

Erwann Delay, *Smooth compactly supported solutions of some
underdetermined elliptic PDE, with gluing applications*, published in
Comm. PDE 37 (2012), 1689-1716, DOI10.1080/03605302.2012.711794.
The inspected version is [arXiv:1003.0535v4, 17 November 2011](https://arxiv.org/pdf/1003.0535v4),
with internal title-page date 17 May 2011; no equality with the journal
version is asserted. Read pp2-3 Definitions1.1-1.2/Theorem1.3 and proof
outline, p5 weighted-space definitions, pp6-10 estimate/isomorphism and
boundary-extension arguments, pp12-14 basic example/divergence, and
pp19-20 nonlinear-example scope. The following is the theorem comparison,
not an application to the actual graph:

On a smooth Riemannian manifold, take a relatively compact smooth-boundary
domain and a smooth linear operator of order m on tensor bundles, with
surjective principal symbol for every nonzero real covector. Its formal
adjoint must satisfy both kernel boundary regularity (KRC: kernel
sections extend with C^(m-1) regularity to the boundary) and the weighted
asymptotic Poincare inequality (API) of Definition1.2. Theorem1.3 solves
a smooth compactly supported source orthogonal to every adjoint-kernel
section. It does not replace that condition by one scalar integral.

The quantitative mechanism is Proposition3.6 and Theorem3.8, pp7-8:
coercivity on the weighted orthogonal complement of the adjoint kernel,
then invertibility of the projected weighted PP* operator. Here the
weights are phi=x^2, psi=x^(2a-n) exp(-s/x), with x a boundary defining
function, a a nonnegative integer and s!=0; zero-extension uses s>0.
Section4, (4.1), supplies the weighted regularity estimate; Theorem5.1
and its whole proof, pp9-10, remove the kernel projection by integration
by parts and source orthogonality. The resulting field vanishes to all
orders at the boundary and extends smoothly by zero. This flat boundary
vanishing should not be silently strengthened to support separated from
the original domain boundary. Constants are operator/domain/weight
dependent, not uniform in a degenerating family.

Read Section8's essential cases: the adjoint's full highest-derivative
coefficient is injective up to the boundary; Lemma8.1 proves API by a
uniform lower bound and absorption near the boundary; Lemma8.2 obtains
KRC through a finite first-order system and its boundary-normal ODE.
Those hypotheses must be checked for the actual coefficient matrix.
Section9.1 uses constants as the divergence adjoint kernel. This is
consistent with, and does not improve on, the previously inspected
Teixeira support-preserving divergence theorem. Section6's gluing
requires matching fluxes against the entire adjoint kernel. No automatic
nonlinear gluing statement follows.

Section9.6 is specifically a Weyl-connection operator with a zeroth-order
quadratic term. It refers onward for nonlinear arguments and uniform
inverse estimates. We do not import it for the graph equation, whose
coefficients depend on the graph and its derivative. In particular this
review does not assert a Banach or tame nonlinear correction theorem.

### Sources reused, access limits and unimported leads

The [collar comparison](2026-11-06-collar-preserving-linear-phase-correction.md)
already inspected Teixeira 1608.06213v7 Theorem3/Remark3 and proofs,
pp8-10: bounded connected smooth planar domain, prescribed collar,
signed C^(r,alpha) data vanishing there and of zero integral yield a
bounded linear divergence solver in C^(r+1,alpha), zero on that collar.
The operator is independent of regularity indices. Its constants depend
on the domain, collar and regularity. These precise support estimates,
and the Guillemin-Sternberg pullback formula inspected there, can be
reused. They solve ordinary divergence, leaving the actual matrix
lifting, norms and adjoint identification for the next mathematical test.

The actual-G graph assessment already inspected Lotay-Pacini CAG28(2020)
Section9.1 Lemmas9.2-9.4 and proofs: its nonzero ambient form and totally
real hypotheses do not provide a graph-existence theorem here. No new
calibration theorem is asserted. McLean's 1998 full text returned403
at the publisher and archive endpoints; the Duke primary index exposed
a PostScript preprint, unsupported by the web reader. Only the index
was read; Theorem3.6 and its proof remain unread, not theorem evidence.
Hamilton's 1982 AMS full text also returned403; it is an unimported
Banach-inverse lead. Hintz's indexed underdetermined-PDE PDF returned404
and is not used. These blockers are nonessential to the linear test;
park their dependent nonlinear/calibrated imports instead of repeating
access attempts. Shell downloading also failed DNS. PDF screenshot calls
returned no readable images; no screenshots count as inspected evidence.

Searches included `McLean Deformations of calibrated submanifolds 1998
theorem 3.6 pdf`, `underdetermined elliptic operator right inverse compact
support Delay`, `Erwann Delay smooth compactly supported solutions`,
`totally real special totally real deformations elliptic volume form`,
and `Hamilton inverse function theorem Nash Moser 1982 Banach`.
Retrieved theorem text, rather than snippets or secondary summaries,
supports the Delay comparison. No failure to find a theorem establishes
novelty or impossibility. Full matching Mathlib coverage is unchecked.

### Prepared continuation and discriminator

The separate [linear patch test assessment](2026-11-06-off-divisor-linear-patch-inverse-test.md)
records the exact proposed mathematical target. It asks for the actual
symbol, full adjoint compatibility and a norm bound under explicit patch
hypotheses, or a scoped failure. It must use L850 rather than rediscover
its matrix, and cite the ready divergence solver rather than reprove it.
Required versus available constants must remain explicit. Merely saying
that F!=0 or that total imaginary flux is zero is insufficient.

Continue only with a genuine controlled inverse on a stated class, or
an informative degeneracy/compatibility obstruction. An entirely
duplicate conclusion supplies no advance. No positive global seed is
known. A creative central-gap construction remains premature until the
operator feasibility and a seed mechanism are specified. The next task
is therefore a routine specialization/calculation, not labeled creative.
No lemma, script, DAG edge or PROOF argument changed this literature turn.

## Original nomination, retained as historical scope

## Purpose and discriminator

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
Controlled phase correction could help turn a specified near-positive
contour into a genuine fixed-order sign contour. It would still need
an actual seed, global compatibility, divisor handling and sign control;
higher orders, other shifts and all-degree transfer are separate.
No such seed or small residual is assumed available.

The existing equation to assess is
Im(F(Phi_u)det(I-iDu))=0, retaining Re>=0 and the entire coefficient.
On a compact patch off F=0, a strict sign margin may be proposed as a
hypothesis for a deformation theorem; no actual global margin is asserted.

Read primary theorem statements and essential proof cases for the most
relevant deformation/right-inverse result first. Compare ambient
symplectic, Lagrangian, calibrated, regularity, boundary, compactness
and cohomology assumptions with this angular graph problem. If a
theorem requires a preexisting exact contour or unknown global sign,
record that limitation. A generic deformation-space theorem does not
supply a quantitative correction theorem here.

Continue only if the review supports one bounded mathematical test of
the actual principal symbol and compatibility/right-inverse conditions,
with required versus available estimates specified. Otherwise retire
this proposed import and seek a different mechanism. Patchwise estimates
away from the divisor cannot establish uniform control at the divisor.
No calculation is preapproved by this file.

## Stops retained

L862's rank-one half-plane obstruction remains intact. The L847 periodic
weighted identities supply no missing estimate. Product, fixed-cutoff,
scalar-flux and nongraph fixed-chart annular failures retain their scopes.
In particular, local ellipticity is not asserted to glue prescribed
collars or remove their boundary-moment obstructions. L861's conditional
cycle and unresolved realization are not assumed as a seed.

The local duplicate search found only analytic implicit-function uses;
compare these more closely if the source lead survives. Search failure
is not novelty evidence. Full Mathlib matching coverage is unchecked.
The next turn is literature-only: do not derive and approve a previously
uncovered correction theorem in the same turn.
