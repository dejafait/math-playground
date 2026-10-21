# Reverse middle-mass coarsening — audit source comparison

TARGET: Critically audit L243's middle-mass coarsening for both actual reverse traces relative to its imported inputs.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L243 and L106, L103 proof sections 2 and 4, L242 hypotheses through proof section 2, the saved middle-mass attempt and history 342; searched histories 340--357 for L243/middle-mass/coarsening and compared the ready reverse, boundary and axial-coefficient assessments. Reused the reverse assessment's six recorded primary searches; no independent completed L243 audit was identified in this scope.
SOURCE_EVIDENCE: Reused inspected Dowker 1207.2096v2 sections 2,7,8,10, (3),(5),(29)--(31),(34)--(36),(42)--(48), via the axial-coefficient assessment, and Benzi--Simoncini 1501.07376v1 section 6.1 Theorem 6.1/Corollaries 6.2--6.3 and section 6.2 via the reverse assessment. Finite spectral calculus, the Laplace resolvent formula, Hilbert--Schmidt Cauchy--Schwarz and rectangular trace cyclicity are standard named inputs; no primary passage was freshly retrieved.
COMPARISON: Existing scalar interval heat and finite trace tools cover the framework; none supplies L243's ordered mass difference, one-circulation block sum or complete response rate by citation. L103's shell/energy bounds, L106's covariance-only step at middle mass zero and L242's reduced/projection identities remain explicit imported premises for a separate specialization audit.
GAP: Audit L243(1)--(2) through its energy-ordered factorization, full one-circulation axial sum, both rectangular trace differences and covariance-only/exterior-circulation assembly at middle mass zero; source adequacy is not mathematical acceptance.
REASON: No essential inaccessible or unread theorem is needed for this finite spectral audit. SPECIALIZE permits checking only the identified deductions relative to their imports; no new mechanism or broader source claim is approved.
LITERATURE_REASON: Gate-required first comparison for the newly selected L243 audit, distinct from L244 boundary transfer; existing framework coverage is reused without repeating unchanged browsing.
SCOPE: Relative all-face SU(2) cube, straight lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first order, probes 3 and 6, all source/end rows, constant indices and heat labels; precisely L243 relative to L103 L106 L242.

## Sources and limits of applicability

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It completes
source comparison, not a proof audit, source import, or new deduction.
The official target/version audit is unchanged; no construction route
is selected. The main gap remains interacting reflected error <=c_box/2,
ultraviolet construction, continuum axioms and infrared control with
finite positive mass. A verified middle-mass estimate could support
L244's sublinear polynomial localization and the quantitative reverse
component, leaving independent component rates and L011 assembly open.

Reuse the [axial-coefficient assessment](2026-10-20-reverse-crossed-axial-coefficient-audit.md)'s
inspected primary coverage of Dowker,
[*Heat-kernels on the discrete circle and interval*](https://arxiv.org/pdf/1207.2096v2),
v2, 31 August 2012, sections 2,7,8,10, printed pp. 1--2,10--12,14--16,
(3),(5),(29)--(31),(34)--(36),(42)--(48). The scalar nearest-neighbor
operator has diagonal 2 and off-diagonal -1; interval Dirichlet values
are at 0,N. Neumann cases have their own constant mode, and section
10 uses mass 4 sinh^2(gamma). The inspected image/eigenfunction formulas
and Laplace-transform cases support finite scalar axial kernels.
L243 needs the finite pinned interval heat kernel already used in
L242(9)--(10), not a whole-line replacement or a uniform decay theorem.
The transverse relative edge space is a different factor: this source
does not impose scalar Dirichlet conditions on every gauge component.
No reproof of the scalar kernel is needed. Checking the local heat
norm specialization is legitimate audit work, not missing literature.

Reuse the [reverse assessment](2026-10-19-reverse-crossed-quantitative-remainder.md)'s
inspected Benzi--Simoncini,
[*Decay bounds for functions of matrices with banded or Kronecker structure*](https://arxiv.org/pdf/1501.07376v1),
v1, 29 January 2015, section 6.1 Theorem 6.1 and Corollaries 6.2--6.3,
printed pp. 12--15. They assume banded Hermitian positive-semidefinite
factors with bounded spectra; their proofs factor heat exponentials
and retain both distance/time regimes. Section 6.2 (6.3)--(6.4) and
Remark 6.6 integrate heat products with spectral lower bounds retained.
This supports the tensor spectral framework. It supplies neither a
middle-mass-uniform signed response estimate nor the sum of every
axial block norm with only one adjacent circulation. Those are L243's
specific assertions. Its finite estimates cannot be imported from a
fixed-mass localization theorem. This source is supporting comparison,
not a new load-bearing theorem for the present audit.

The same reverse assessment inspected Ginovyan--Sahakyan,
[*On the trace approximations of products of Toeplitz matrices*](https://arxiv.org/pdf/1405.3568v1),
v1, 14 May 2014, Theorem 2, printed p. 6, proof pp. 8--9. Its real
symmetric scalar circle symbols in Lip(p,gamma), Lip(q,gamma),
0<gamma<=1 and 1/p+1/q<=1/2 yield a normalized trace-of-square rate.
It does not cover these relative rectangular matrix words, triangular
axial selector and separate coefficient levels. It is a scope exclusion,
not a matching theorem or evidence against the requested estimate.
No inspected stronger theorem removes the need to check the ordered
specialization. Unread leads in prior assessments remain unread.

Finite-dimensional spectral calculus and the Laplace resolvent formula
apply to self-adjoint positive operators, with strictly positive total
mass or spectrum for the inverse. Hilbert--Schmidt trace duality and
the bounded-operator ideal property require compatible domains;
rectangular cyclicity requires the corresponding products to be
trace class, automatic for these finite spaces. These are standard
named tools, not a result asserting L243's rate. Positivity may be
used for scalar heat/spectral majorants, not the signed response.
The local pinned vertex shell bound and W energy estimate are imports
L103(13),(16), not new external spectral asymptotics. Unknown full
matching or supporting Mathlib coverage remains **not checked**.

## Separate audit obligations and test

| L243 passage | Reusable framework | Required later audit |
| --- | --- | --- |
| (4)--(8) | L103(13),(16), positive spectral calculus | Exact middle energy order, pinned vertex spectrum, eta=0 endpoint, uniform shell bound for N sqrt(h)>=1, W coefficient on its original side. |
| (9)--(12) | L242(9)--(10), scalar interval heat and Laplace formula | One adjacent circulation in the second word; every s,t source/end row; integrability at both heat endpoints; epsilon dependence before any schedule. |
| (13)--(17) | Finite rectangular trace cyclicity and Hilbert--Schmidt inequalities | Both actual words on E,F, N^3 rank product, a prefactor, n-level heat count, all filters, separate s,t coefficients and full mode polynomial envelope. |
| Section 4 and (2) | L106 section 2 (8) and section 4, L242(3)--(4) | Covariance-only use with original middle G, exterior comparison at eta=0, exact reduced trace and projection comparison at eta=0; do not invoke L106's combined positive-eta conclusion at zero. |

Continue only if a separate audit verifies the stated uniform
N^3 h^(3/4)[log(e/epsilon)+epsilon^(-1/2)] error for
0<=eta<=h<=1, 0<epsilon<=1, 0<=delta<=1 and N sqrt(h)>=1,
and the complete assembly under its additional spectral conditions.
The registered schedule is epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3),
with required error O(N^(5/2)log(eN)). These are targets quoted from
L243, not newly checked deductions. Retain S_st and its diagonal half.
If an order, source hypothesis or count fails, isolate the first
unsupported assertion and withhold only that conclusion; do not infer
signed growth or introduce an unassessed repair mechanism.

History 342 contains the original attempt. Scoped histories 340--357
and ready assessments contain qualified downstream uses rather than
an independent L243 audit. Preserve ATTEMPTS/028--032: reverse-block
operator gain, termwise commutation, uncontrolled varying-mass
substitution, adjoint norm gain and separate first absolute moments
are failed shortcuts, not global bans. This finite ordered energy/heat
audit does not reopen them. Search failure establishes no novelty.

Essential continuation IDs: L103 L106 L242 L243. Unresolved imports
are L103's shell/energy estimates, L106's covariance-only and exterior
bounds at middle mass zero, and L242's reduced identity/projection
comparison. L244's accepted boundary transfer does not audit these.
No cross-notebook input, mathematical script, new lemma, or change to
the argument/DAG is made. Mathematical exploration usage stays zero
of three. Next is separate critical audit of exactly TARGET.

## Original registration — preserved

The registration below is historical; its coverage gap is completed
above, while its mathematical acceptance test remains pending.

The main gap remains the interacting reflected error <=c_box/2,
ultraviolet construction, continuum axioms and infrared control with
finite positive mass. This intermediate audit could verify the input
that permits L244's sublinear polynomial range, and thereby one premise
of the quantitative reverse-component estimate. Independent component
rates and the complete quantitative L011 assembly remain open.

Essential input IDs are L103 L106 L242 L243. Keep exactly the relative
SU(2) cube, lower-rooted direction-1 forest, admitted even N, a=8/N,
tau=1/16, stored coordinates, bare-first order, probes 3 and 6,
all constant indices, source/end rows and the complete heat labels.
No cross-notebook input is proposed.

After the separate coverage step, the discriminating test is the
uniform estimate in L243(1) for 0<=eta<=h<=1 and its assembly (2):
N^3 h^(3/4)[log(e/epsilon)+epsilon^(-1/2)], with no inverse eta
loss and N sqrt(h)>=1. Check the literal energy factorization, the
full axial block sum with one adjacent circulation, both distinct
trace orders, original S_st and the full mode envelope. At
epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3), the claimed complete
comparison is O(N^(5/2)log(eN)). This records a target, not a proof.

Unresolved assumptions include L103's complete transverse energy and
shell bounds, L106's covariance-only and exterior-circulation estimates
at middle mass zero, and L242's qualified reduced identity/projection
comparison. Accept only the audited specialization relative to its
imports. If a source hypothesis, operator order or full-row count fails,
isolate the first unsupported assertion; do not infer signed growth or
switch to a new repair mechanism in the audit. Preserve ATTEMPTS/028--032.

The next turn is literature-only for this exact target. Existing ready
assessments should be reused where their hypotheses actually match;
further browsing needs an essential missing theorem case or specific
new lead. No new result has been derived or approved here. Full matching
and supporting Mathlib coverage is not checked; unknown is not absence.
