# Reverse reduced projection comparison — audit source comparison

TARGET: Critically audit L242's reduced identity and projection comparison for both actual reverse traces relative to its imported inputs.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L242, L085's layer hypotheses, L103 proof sections 2 and 4, L105's hypotheses/layer trace and energy passages, L106's hypotheses/conclusions and exterior comparison, and L107 proof section 2. Compared the ready reverse, middle-mass and axial-coefficient assessments, history 341 and scoped audit histories 349,351,353,355,357,359; read ATTEMPTS/028--032. Reused recorded primary searches; no independent completed L242 audit was identified in this scope.
SOURCE_EVIDENCE: Reused inspected Dowker 1207.2096v2 sections 2,7,8,10, (3),(5),(29)--(31),(34)--(36),(42)--(48), and the reverse assessment's Benzi--Simoncini 1501.07376v1 section 6.1 Theorem 6.1/Corollaries 6.2--6.3 and section 6.2. Finite spectral calculus, Laplace resolvent representation, Hilbert--Schmidt Cauchy--Schwarz and rectangular trace cyclicity supply standard tools; no new primary passage was retrieved.
COMPARISON: Existing scalar interval heat and finite trace coverage supports the framework, but no inspected theorem supplies L242's exact reduction or its middle-mass-uniform projection rate. L103's pinned shell/energy estimates, L085's relative identities and L105--L106's layer/exterior comparisons remain imported premises, not conclusions verified by this review.
GAP: Separately audit L242(3)--(6): every removed projection in both ordered words, the sole retained Q_delta, full two-circulation axial norm sum, energy order at eta=0, and separate L106 assembly with its positive-mass conditions.
REASON: No essential unread or inaccessible source is identified for this finite specialization audit. SPECIALIZE permits the later audit of these deductions relative to imports; it does not accept their proof or establish a new estimate.
LITERATURE_REASON: Gate-required first source comparison for the distinct L242 audit; L243's accepted audit imports L242 and cannot verify it. Reuse unchanged primary coverage without repeated browsing.
SCOPE: Relative all-face SU(2) cube, lower-rooted direction-1 forest, sufficiently large admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first order, probes 3 and 6, every source/end row, allowed constant index and heat label; exactly L242 relative to L085 L103 L105 L106 L107.

## Source applicability and limits

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It completes a
new target-specific comparison, not a mathematical audit, import of a
matching estimate or discovery. The official target/version record is
unchanged; no new construction route is selected. The main gap remains
the interacting reflected error <=c_box/2, ultraviolet construction,
continuum axioms and infrared control with finite positive mass.
Validating this projection input could support L243 and the reverse
component remainder; independent component rates and quantitative
L011 assembly remain unresolved.

Reuse the [middle-mass assessment](2026-10-20-reverse-crossed-middle-mass-audit.md)
and [axial-coefficient assessment](2026-10-20-reverse-crossed-axial-coefficient-audit.md)'s
inspected Dowker, [*Heat-kernels on the discrete circle and interval*](https://arxiv.org/pdf/1207.2096v2),
v2, 31 August 2012, sections 2,7,8,10, printed pp. 1--2,10--12,14--16,
with the equation ranges in SOURCE_EVIDENCE. Its scalar nearest-neighbor
operator has diagonal 2 and off-diagonal -1; the Dirichlet interval
has pinned values at 0,N. The image/eigenfunction formulas include the
endpoint cases. Neumann kernels retain a constant mode separately;
section 10 uses mass 4 sinh^2(gamma). L242 uses the finite pinned axial
heat factor, not a whole-line substitute. The transverse vector space
is a different tensor factor; this source does not assign scalar
Dirichlet conditions to normal links. Its formulas support the scalar
framework but do not prove L242(5)'s summed joint operator norm.
No reproof of an external heat-kernel theorem is needed. Checking
L242's short exponential-series argument for interval substochasticity
and its two-circulation specialization belongs to the later audit.

Reuse the [reverse assessment](2026-10-19-reverse-crossed-quantitative-remainder.md)'s
inspected Benzi--Simoncini, [*Decay bounds for functions of matrices with banded or Kronecker structure*](https://arxiv.org/pdf/1501.07376v1),
v1, 29 January 2015, printed pp. 12--15, section 6.1 Theorem 6.1 and
Corollaries 6.2--6.3. Banded Hermitian positive-semidefinite tensor
factors and bounded spectra are essential; the heat-product proof
retains both distance/time regimes. Section 6.2 (6.3)--(6.4) and Remark
6.6 integrate heat products retaining the spectral lower bound. This
supports the tensor functional-calculus framework, not a uniform
projection replacement in the present signed relative trace. No decay
or localization theorem is needed as a new premise for L242's audit.
The same assessment's inspected Ginovyan--Sahakyan 1405.3568v1,
Theorem 2, printed p. 6 and proof pp. 8--9, concerns real symmetric
scalar circle symbols in Lip(p,gamma), Lip(q,gamma), 0<gamma<=1,
1/p+1/q<=1/2 and a normalized trace-of-square rate. It does not cover
these rectangular relative-space words with separate coefficient
levels and triangular axial weights. It is a scope exclusion, not a
matching theorem. Unread leads remain unread and provide no premises.

Finite-dimensional spectral calculus and the Laplace resolvent formula
apply to self-adjoint positive operators with positive total spectrum
for inversion. Hilbert--Schmidt trace duality and the operator ideal
property require compatible maps; rectangular cyclicity holds for
compatible finite-dimensional products. These standard named inputs
need no new source extraction. Their ordered use is precisely what
remains to audit. Positivity concerns the scalar axial heat majorant,
not the signed response or arbitrary entries of Q. L103(16) already
records the full pinned vertex shell estimate and L107(6) its projection
specialization. Neither is a new external Weyl-law assumption. L103(13)
and L105's filtered W energy bound remain explicit local imports.
Full matching and supporting Mathlib coverage is **not checked**;
unknown coverage is not evidence of absence.

## Separate audit obligations

| L242 passage | Available framework | Required later check |
| --- | --- | --- |
| (7)--(8), (3) at delta=0 | L085 relative Hodge identities, L105(3),(5), finite rectangular cyclicity | Exact signs, transposes, coefficient a, both E/F domains, each removed Q and the single retained Q; move no multiplier through an inverse. |
| (9)--(12), (5) | Pinned scalar interval heat, spectral calculus, Laplace formula | Every s,t pair including both ends, full transverse spectrum and circulation singular values; both heat endpoints and logarithmic epsilon dependence before any schedule. |
| (13)--(17), (4) | L103(13)--(16), L105 energy/heat normalization, L107(6), trace ideal inequalities | Pinned vertex multiplicities and shell threshold, original energy order for U_t at eta=0, sole Q_delta difference, N^3 layer rank and full heat envelope. |
| Section 4, (6) | L106(2) and section 4 | Separate covariance/middle-inverse and exterior errors, all positive-mass conditions, original triangular half, no additional outside factor 3. |

The discriminating test is exact equality (3) with the circulation-only
trace at delta=0, followed by the quoted uniform (4) error
C_i N^3 delta^(3/4)log(e/epsilon) for 0<epsilon,delta<=1,
0<=eta<=1 and N sqrt(delta)>=1. Delta=0 is an identity case, not an
instance of the positive-delta shell condition. Eta=0 belongs to (4);
(6)'s combined L106 estimate requires positive eta and its separate
spectral condition. The later audit must verify (5)'s complete axial
sum and the (6) schedule epsilon=N^-1, eta=N^-2, delta=N^(-2/3),
whose claimed comparison is O(N^(5/2)log(eN)). These are recorded
targets, not deductions or approvals in this literature step.
Continue only if the exact order, hypotheses and full-row/heat counts
support them. If one fails, isolate the first unsupported assertion
and withhold that conclusion without inferring signed growth or
introducing an unassessed repair.

History 341 records the original attempt. The scoped downstream audit
histories retain upstream qualifications; history 359 explicitly leaves
L242 for separate audit. No matching independent audit was found in
this scope. Preserve ATTEMPTS/028--032: failed reverse operator gain,
termwise projection commutation, varying-mass use of a qualitative
limit, adjoint norm gain and factorwise first absolute moments. The
present joint finite heat/energy audit tests a different sufficient
mechanism, without reopening those shortcuts or asserting novelty.

Essential continuation IDs: L085 L103 L105 L106 L107 L242.
Unresolved imports are relative Hodge identities, pinned shell/energy
estimates, actual layer/heat normalization and the inverse/exterior
comparisons. L107 fixes the eventual subtraction but supplies no
quantitative theorem for L242. All faces, normal end rows, allowed
constant modes, both original coefficient levels and full heat labels
remain. No cross-notebook input, new lemma, mathematical script, DAG
or PROOF change is made. Mathematical exploration usage stays zero
of three. Next is the separate audit of exactly TARGET, after approval
of this newly completed source assessment.

## Original registration — preserved context

The source gap in this historical registration is completed above;
its mathematical test remains pending.

The main gap remains interacting reflected error <=c_box/2, removal
of the ultraviolet cutoff with the required continuum axioms, and
infrared control with finite positive mass. This intermediate audit
could validate the remaining qualified projection input to L243 and
the downstream reverse-component comparison. Independent component
rates and quantitative L011 assembly remain unresolved.

Essential input IDs: L085 L103 L105 L106 L107 L242. Preserve the
relative all-face SU(2) cube, lower-rooted direction-1 forest, admitted
even N, a=8/N, tau=1/16, stored coordinates, bare-first order, probes
3 and 6, all relative source/end rows, allowed constant indices and
full heat labels. No cross-notebook input is proposed.

The eventual discriminating test is L242(3)'s equality at delta=0
with the circulation-only reverse trace, and (4)'s uniform error
C_i N^3 delta^(3/4)log(e/epsilon), including eta=0 and
N sqrt(delta)>=1. Verify the literal rectangular order, every removed
Q, the single retained Q_delta, and all n^2 axial pairs before their
heat sum. Check (6)'s separate use of L106 and the registered schedule
epsilon=N^-1, eta=N^-2, delta=N^(-2/3). These are quoted audit targets,
not newly established estimates. Accept only relative to the stated
imports; isolate the first unsupported assertion if a hypothesis,
operator order or full-row count fails, without inferring signed
growth or introducing an unassessed repair.

Unresolved imported assumptions include L085's relative Hodge
identities, L103's pinned shell/energy estimates, L105's actual
layer trace and heat normalization, and L106's inverse/exterior
comparison. L107 specifies the unchanged eventual subtraction;
its limit is not a quantitative comparison theorem. Preserve
ATTEMPTS/028--032 and all existing audit qualifications.

Next turn is literature-only for this exact TARGET. Reuse the existing
reverse and middle-mass assessments where their hypotheses match;
fresh retrieval needs an essential unread case or specific new lead.
Full matching and supporting Mathlib coverage is not checked.
