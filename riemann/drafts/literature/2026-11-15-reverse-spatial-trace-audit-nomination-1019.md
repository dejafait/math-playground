# Reverse spatial majorant and trace — nomination1019 / source review1020

TARGET: Critically audit C467h's original reverse spatial majorant and t=0 L1 trace, including the coefficient determinant, Vandermonde cancellation and diagonal measurability.
CHECKED: 2026-11-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1020 reuses nomination1017/completion1018's exact/stronger-target searches and primary comparisons; read all of C467h, the relevant C467f-g reconstruction/variational passages and audit1017, and scoped histories1017-1019 and stops948/1009. No prior C467h audit was found in these records. No new external discovery search or novelty finding is claimed.
SOURCE_EVIDENCE: Reuse review1018 and source reviews992/994/1016: Teschl author-hosted April2012 Lemma2.14/Corollary2.15 pp52-53, Theorem3.9 p81, Lemma3.11(3.91)/proof p83 and Theorem6.1/proof pp189-190; Hunter undated Chapter4 Theorem4.24/proof and Section4.6 pp49-50; ABEM author version17September2011 AppendixA(A.5) p40. Precise links, hypotheses and limits are below; no fresh primary retrieval was needed.
COMPARISON: The written C467h uses the same ODE, coefficient-Jacobian, real symmetric spectral and DCT tools already assessed for its derivation. Its audit adds no changed flow, parameter domain, measure or theorem hypothesis. These sources cover supporting tools only, leaving the stated determinant/weight cancellation and uniform estimates to independent mathematical review.
GAP: C467h's correctness remains unresolved: audit its physical-time determinant bound, centered scaling/orientation, complete complex weight cancellation, constants, diagonal measurability and sequential L1 limit for every distinct initial triple. No audit outcome or new bound is established in this literature turn.
REASON: Separate source-scope comparison for the new audit is complete; SPECIALIZE permits exactly the saved TARGET after supervisor approval of this changed assessment. No essential source blocker remains and no general theorem requires reproof. Do not repeat literature work for the unchanged target.
LITERATURE_REASON: Nomination1019 newly requested independent critical review, outside review1018's listed derivation target. This mandatory literature-only step maps the now-written proof to that ready coverage; it does not refresh unchanged sources to fill a quota.
SCOPE: Exactly C467h's original unnormalized A=F(Y)det_C(D_uY/i), n=3,R=1/4,a=1/16,T_0=1/1920,I=(-a,a)^3, fixed physical time and raw reversed flat metric; arbitrary unequal distinct initial triples and zero extension on the initial diagonals, with completed Lebesgue measure. No divided K_-, smooth diagonal extension, spacetime current, interface/payment, global/all-degree or Xi conclusion.

## Original nomination1019 — checklist, not a completed audit

The canonical result is
`lemmas/C467h-actual-h-reverse-spatial-l1-trace.md`.
Keep n=3, R=1/4, a=1/16, T_0=1/1920, I=(-a,a)^3, the actual
normalized B,H,H_0,F and the original flat reversed field. The target
is the unnormalized spatial coefficient; no divided K_- bound,
smooth diagonal extension or spacetime current is part of this audit.

Essential established inputs are C467e/audit1017 for survival and the
background/radial bounds, C467f/audit1017 for imaginary ordering and
the exact coefficient/physical determinant reconstruction, and
C467g/audit1017 for the full-horizon Hessian and tangent estimates.
C466z/audit988 and C466/audit993 supply the normalization and complex
analytic bound through those inputs; preserve C466a's external
density qualifications. C467h is the result to test, not an established
premise for its own audit.

The discriminating audit must check the complete complex identity (10)
before its modulus estimate, including Delta(u)/Delta(q), the canceled
scale L^-6, all three pair factors and det(I-iZ). Check that Liouville
uses the continuous coefficient system in original physical time and
that its bound does not require uniform initial spacing. Verify real
symmetry of Z from the established reconstruction, each constant in
(6)-(14), and the initial orientation i^6=-1. Then check local smooth
dependence, zero extension on the null diagonals, measurability and all
dominated-convergence hypotheses for an arbitrary time sequence.
This lists checks; it does not perform or approve them.

Accept the local result only if the full majorant and trace survive
this review. A defect requires a precise repair or preserved failure,
not rejection of the reverse route based solely on an optional bound.
Spacetime minors/current, interfaces, payment, global assembly, all
degrees and actual-Xi transfer remain unresolved even on success.
Stops948/1009 retain their original scopes.

Next-turn routing is literature_comparison, standard/high, for separate
scope approval using ready source evidence. If approval finds the
coverage adequate, the subsequent audit is proof_audit/conceptual_audit,
deep_research/xhigh: the issue is the singular-coordinate cancellation
and analytic L1 passage, not just arithmetic replay. No new central
creative target is selected while this essential local input awaits
review. Mathlib supporting DCT names retain review1018's scope; full
matching coverage remains unchecked.

## Completed source-scope comparison1020 — 15 November 2026

The original nomination above is preserved as the proposed mathematical
test. This completion assesses its source coverage only. Read the full
C467h, including its source uses and Mathlib qualifications, before
comparing the relevant established input passages: C467f hypotheses,
conditional reconstruction (18)-(19), and C467g hypotheses, Riccati/
variational reconstruction and audit1017. These agree in their stated
parameters and intended physical-time coefficient chart. Agreement of
scope is not verification of the formulas in C467h.

### Reused primary inputs and exact applicability obligations

1. Gerald Teschl, [*Ordinary Differential Equations and Dynamical
   Systems*, author-hosted April2012 preliminary version](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
   Source review992 in
   `2026-11-14-actual-h-full-pullback-cone-audit-scope-991.md`
   inspected Lemma2.14/Corollary2.15 and proofs, printed pp52-53;
   Theorem3.9/proof p81; Lemma3.11(3.91)/proof p83; and
   Theorem6.1/proof pp189-190. Review1018 reused exactly these cases.
   Smooth autonomous fields have smooth local dependence on the open
   maximal-flow domain; continuation requires an interior compact set.
   The linear-system statements require continuous coefficients, and
   Abel-Liouville does not presume a nonzero determinant. The future
   audit must check C467h(5)'s coefficient system and initial matrix,
   its continuity along each fixed distinct trajectory, and the claimed
   trace/norm estimate in original physical time. For measurability it
   must check local parameter dependence at each surviving trajectory,
   including the closed time endpoints. These theorems supply neither
   uniform separation from the divisor nor a common parameter chart.

2. John K. Hunter, [*Measure Theory*, Chapter4, Theorem4.24/proof
   and Section4.6, printed pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11),
   undated author-hosted chapter. Reviews994 and1018 inspected the
   complete theorem, Fatou argument, complex-valued and a.e. cases.
   Measurability, a.e. convergence and one integrable absolute majorant
   are essential; the limit's measurability cannot be omitted on a
   noncomplete measure space. C467h chooses completed Lebesgue measure
   and a sequence of nonnegative absolute differences. That is within
   the assessed tool's scope; its hypotheses still require checking.
   The audit must establish the zero extension's measurability,
   identify the initial value and orientation, validate G and domination
   by 2G, and justify why arbitrary time sequences give the asserted
   real-time L1 limit. No Sobolev trace, Fubini theorem, current or
   time-slice representative theorem is an additional premise here.

3. Athreya-Bufetov-Eskin-Mirzakhani,
   [*Lattice Point Asymptotics and Volume Growth on Teichmüller Space*,
   author version17September2011, AppendixA(A.5), printed p40](https://www.math.uchicago.edu/~eskin/final_final.pdf#page=40).
   Review1018 inspected the monic-polynomial root/coefficient
   Vandermonde Jacobian and its antisymmetry/degree justification.
   This is supporting coverage, not a theorem about our centered and
   scaled coefficient flow. The established specialized reconstruction
   is C467f, completed by C467g/audit1017. C467h(8)-(10) still needs
   its own audit of coordinate order, the constant scale factors, local
   chain rule, ordering signs, all three pair factors and det(I-iZ).
   No source permits a smooth inverse root chart on the discriminant.
   The named real symmetric spectral theorem covers the determinant
   estimate only after Z's real symmetry and norm bound are justified.

The de Boor2005 Sections8-9 interpolation coverage from review1016
supports already audited C467f-g. No new divided difference formula
is introduced in C467h. Do not rederive those inputs or reopen the
normalization C466z/audit988 and analytic bound C466/audit993 without
a specific defect; preserve C466a's external density qualifications.
No general ODE, determinant or integration theorem needs reproof.

### Duplicate/failure comparison and decision

Reuse review1018's recorded exact-statement and stronger-result
searches. Its inspected Hall-Ho2025 Proposition3.1 concerns polynomial
heat evolution and a holomorphic inverse-gap root system, unlike the
prescribed conjugate-dependent reverse field with its background.
It supplies no automatic majorant or audit certificate for C467h.
The uninspected historical references remain leads, not assumptions.
No changed dynamics or stronger claim in C467h requires reopening that
comparison. No new broad search or theorem import is warranted merely
because a written proof now awaits independent review.

Fresh scoped local reads of stops948 and1009, including the latter's
audit1011 update, confirm their different targets: a smooth divided
collision-extension screen and the original prescribed forward cap/
initial family. Neither is a reverse spatial L1 counterexample. The
prior cone audit1017 explicitly leaves the majorant and trace unpaid;
history1019 explicitly leaves C467h's independent audit pending. These
records contain no duplicate completed audit. This is a scoped finding,
not a novelty claim or an assertion about all notebook literature.

SPECIALIZE covers the exact TARGET at the top. A citation alone cannot
validate C467h's compensation identity or constants. The separate
mathematical turn must examine the entire original complex identity
before majorizing it, without imposing equal or separated initial gaps.
Retain the result only if the uniform bound and L1 trace both survive;
otherwise identify a precise defect and repair or withdraw the affected
claim while preserving the failed calculation. Failure of an optional
estimate does not establish failure of the reverse route. Even success
provides only a local initial spatial trace for a possible later signed
deformation: spacetime minors/current, payment/interfaces, global
assembly, all degrees and actual-Xi transfer remain open.

Mathlib: reuse review994/1018's inspected supporting DCT names,
`MeasureTheory.tendsto_integral_of_dominated_convergence` and
`MeasureTheory.tendsto_integral_filter_of_dominated_convergence`, in
the [generated DominatedConvergence documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
The recorded hypotheses include a.e. strong measurability, integrable
norm domination and a.e. convergence, plus countable generation for
the filter version. No fresh Mathlib inspection, full matching theorem,
absence claim or Lean verification is asserted.

Outcome: LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. This completes
a previously missing audit-scope comparison, not a mathematical audit
or a new result beyond the checked sources. The next action is unchanged
and is routed proof_audit/conceptual_audit, deep_research/xhigh after the
supervisor's separate approval of this changed assessment. Its difficulty
is the singular-coordinate cancellation and analytic L1 passage, not
arithmetic alone. This essential pending audit blocks selection of an
unassessed creative mechanism; no creative target is invented here.
