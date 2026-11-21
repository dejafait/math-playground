# Coupled adjacent construction — nomination1064 / source review1065

TARGET: Critically audit C467v's coupled adjoints, including full-side incidence, crossing derivatives, the extended lower reference and corner germ, continuous vertex limits, all eight complex L1 products and both independent-cutoff identities.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate review1065 reads C467v for source scope, reuses reviews1063/1061's ODE/trace/input comparisons, rereads stops1058/1060, and follows two targeted crossing-flow searches to primary Kong et al. v3 and Burden et al. 2016 texts; queries and inspected cases below.
SOURCE_EVIDENCE: Reused Teschl April2012 Theorem2.5, Lemma2.14/Corollary2.15, Theorems3.9/3.12/6.1 and Conrad/Hunter; freshly read Iyer Proposition7/Remark8/Lemma9/Theorem10 proof/Remark11, Kong et al. arXiv2306.06862v3 Definitions1/2, (9)-(11), sectionIII-B/(16)-(30), sectionIII-C/(31)-(34), AppendicesA/B, and Burden et al. Definitions1/2 p1236, Theorem4/proof and Corollary5 p1242, section7.1.2/(60) p1251.
COMPARISON: Known chart and event-selected-flow results cover local positive-time tools including the standard saltation correction, but not the selected boundary pair, uniform degenerating estimates, corner gluing or eight original complex products. No source imports the full conclusion; stops1058/1060 retain their scopes.
GAP: Source coverage is ready for auditing the existing proof. Full-side incidence, directional crossing estimates, reference extension, corner compatibility, continuous limits, eight L1 bounds and independent cutoff identities remain unaudited mathematical claims.
REASON: This separate literature-only turn approves exactly the saved conceptual audit as SPECIALIZE/REPRODUCTION; no new lemma, construction, obstruction or correctness verdict is derived. No essential source is blocked; the next action defaults to the approved mathematical audit.
LITERATURE_REASON: The new target audits C467v's explicit corner-compatible boundary selection and crossing estimates, which did not exist when review1063 assessed construction. Reuse the inspected ordinary ODE/Stokes/DCT sources and check only essential applicability or missing proof-case coverage.
SCOPE: Exactly the original j=0/j=1 coupled component and C467v's proof, under its qualified external zero input, fixed possibly asymmetric bump, raw time, divisor and common minus sign; no upper-pair extension, additional interface or all-degree claim.

The original nomination was written after one RESEARCH / POTENTIALLY_NEW
attempt. Its gate is discharged by separate source review1065 below;
the mathematical audit remains unperformed.
The canonical statement and proof are in C467v; it remains unaudited.
The exact TARGET above is the sole proposed continuation. Its source gate
is next; a conceptual proof audit follows only after separate approval.

The main gap is L030–L032/C032a actual-Xi all-degree algebraic-square
positivity. C467v proposes one local assembly interface, retaining the
selected lower outer edge while changing the previously excluded lower
radial selection. Accept the construction only if every nominated
condition holds on one common time; otherwise isolate the first failed
claim and downgrade the conclusion. A gap in this construction is not
a nonexistence result for the joint class. Preserve stops1058/1060.

Essential local inputs are C467e/audit1017, C467k/audit1033,
C467p/o/audit1049, C467q/audit1053's graph, C467r/audit1056,
and C467t/u/audit1062. C467s's entire reflected construction remains
unaudited and is not an input to C467v. The hypotheses inherited through
C467u include L018/L021/L024 and C466a's finite-zero/first-zero
qualification; their underlying finite certificates were not replayed.
Retain n=3,R=1/4,a=1/16,T0=1/1920,X=1/256,b_*=1/4096,
H_*=1/128 and actual B/beta/H/H0/F. No normalized network operator,
single physical-vertex value or differentiability at t=0/r=0 is assumed.

The highest-risk checks are precise:

- C467v(9)–(14): all differentiated root remainders, the normal's sign
  on the whole radial side and fixed auxiliary radius, and the size of
  each field jump after the spatial change u=r sqrt(t).
- C467v(16)–(19): the derivative correction in both time directions,
  its radial row, the at-most-one-crossing claim and outer-hit estimates
  as the crossing time approaches zero.
- C467v(20)–(24): the forward extension of the selected lower reference,
  existence of the upper side-hit germ in both sign bands, its derivative
  bounds, and exact compatibility of boundary data near the corner.
- The smoothness argument at the characteristic from the outer corner,
  the continuous endpoint/vertex limits (25)–(26), and the gluing to exact
  constants near y=0 and outside the bump.
- The eight separate majorants (29), the complete complex signs/faces
  in (30), arbitrary independent cutoffs and exact shared-face cancellation.

The first next-turn routing is literature_comparison / standard / high,
limited to source adequacy for this new audit target. If approved, the
appropriate audit is proof_audit / conceptual_audit / deep_research /
xhigh: the logical issue is simultaneous corner smoothness and continuity
through a degenerating interface, not numerical replay. No candidate_audit
or RH-resolution escalation is warranted. Upper-pair continuation,
other interfaces, exterior payment, realization, all degrees and Xi
transfer remain independent unresolved obligations. Full matching
Mathlib coverage remains unchecked.


## Separate source review1065 — 16 November 2026

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, actual task
literature_comparison. The exact TARGET and SCOPE are unchanged.
The preceding nomination's requested source gate is discharged here;
its future-tense routing describes the original nomination. The full
C467v proof was read for source scope, without issuing a proof verdict.
Source readiness is local process progress, not mathematical progress
beyond the sources or toward RH.

### Reuse, duplicates and failures

Reuse [review1063](2026-11-16-coupled-adjacent-trace-nomination-1062.md)
for this joint-selection class and
[review1061](2026-11-16-adjacent-incidence-obstruction-audit-nomination-1060.md)
for ordinary ODE hypotheses and the qualified finite-zero/product inputs.
Read review1063 in full and review1061's characteristic comparison.
Read C467v's entire statement/proof/Mathlib qualification to locate its
actual tools; its remainders, jumps and limits remain unaudited.
Review1063's weak-network and fixed-edge semigroup comparisons are
reused without repeating their searches. They supply neither this
pointwise coupled conclusion nor a class obstruction.

Reread [stop1058](../../ATTEMPTS/2026-11-16-adjacent-conjugate-matching-inconclusive-1058.md)
and [stop1060](../../ATTEMPTS/2026-11-16-fixed-adjacent-radial-match-stop-1060.md).
The former fails an independent conjugate selection; the latter excludes
the fixed C467r radial value under C467t/u's qualified inputs. C467v
changes that interior selection while retaining the lower outer edge.
Neither failure settles this changed class. Changing the class itself
establishes no assertion. Do not assume C467s's full construction,
C467q's stronger single physical-vertex condition, or an upper pair.
The new proof-specific tool to compare is the event-time derivative
correction in C467v(16), used in (17)-(19). No uniform estimate or
at-most-one-crossing assertion is verified by this literature turn.

### Primary source comparison

Queries were `saltation matrix hybrid systems transversality
differentiability flow event surface Kong Payne Zhu Johnson 2024
tutorial` and `"Event-Selected Vector Field Discontinuities Yield
Piecewise-Differentiable Flows" arxiv`. Followed primary arXiv text
and the author's published PDF. Search snippets and other hits supply
no mathematical evidence. The two inspected sources below close the
specific crossing-variation coverage question; no generic new network
search was needed.

**Crossing correction.** Nathan J. Kong, J. Joe Payne, James Zhu and
Aaron M. Johnson, *Saltation Matrices: The Essential Tool for Linearizing
Hybrid Dynamical Systems*, Proceedings of the IEEE112(6) (2024),585-608,
DOI10.1109/JPROC.2024.3440211;
[arXiv2306.06862v3, 30 August2024](https://arxiv.org/html/2306.06862v3).
Read Definitions1/2, (9)-(11), sectionIII-B/(16)-(30), sectionIII-C/
(31)-(34), and AppendicesA/B, including both early and late perturbations.
The update uses differentiable guards/resets, transverse events and
locally unchanged event sequence. Its identity-reset stationary-hyperplane
case is the standard correction referenced by C467v(16), conditionally
on the actual field hypotheses. It supplies no uniform grazing-limit
bound or intersecting-guard solution. Early/late perturbations are not
a check of backward travel in the actual fields. AppendixA is read as
an instantaneous-event derivation, not a finite-time Jacobian formula.
The local normal bounds, jumps, radial row and zero-time limits remain
for the audit. No reproof of the standard saltation formula is needed.

**Stronger local flow tool.** Samuel A. Burden, S. Shankar Sastry,
Daniel E. Koditschek and Shai Revzen, *Event-Selected Vector Field
Discontinuities Yield Piecewise-Differentiable Flows*, SIAM J. Applied
Dynamical Systems15(2) (2016),1227-1267, DOI10.1137/15M1016588;
[author-hosted published PDF](https://faculty.washington.edu/sburden/_papers/BurdenSastry2016siads.pdf).
Read Definitions1/2 p1236, Theorem4/proof and Corollary5 p1242,
and section7.1.1-2/(58)-(60) p1251. Event-selectedness requires smooth
event functions with derivatives along the field bounded below by a
positive constant on an open neighborhood, and C^r extensions of all
sign-region fields. Theorem4 gives a piecewise-C^r local flow; its proof
uses the assembled branch flow and its almost-everywhere differential
equation. Corollary5, when hypotheses hold throughout the domain, gives
a unique maximal flow with inverse time maps. Equation(60) is the
single-surface saltation update; section7.1.1 treats reverse time by
reversing the field. These are local regularity tools, without a
uniform bound at vanishing transversality or smooth boundary-data gluing.

For applicability the later audit may compare the augmented positive-time
field (1,b_j) with this theorem and use signed z as event function.
It must first check actual chart extensions, common orientation and
nonzero normals on the neighborhoods used. This names hypotheses to
test, not an established specialization. No source theorem has been
verified at t=0. It must not be cited as already giving C467v's common
working time, uniform crossing bounds or corner-compatible scalar test.
Using ordinary chart ODEs plus the cited single-event correction is
also permitted; reproving the general event-selected theorem is not
needed for the nominated audit.

**Corner compatibility.** Gautam Iyer, *Method of Characteristics*,
[2026 course notes](https://www.math.cmu.edu/~gautam/c/2026-632/notes/moc.html),
Proposition7/Remark8, Lemma9, Theorem10/proof and Remark11 were freshly
read. Admissible boundary jets and nonzero normal characteristic
derivative give a local inverse characteristic chart. The proof recovers
the gradient from the zero tangential error; Remark11 requires compatible
data at multiple boundary hits. This supports a regular positive-time
chart germ, without supplying a quantitative shrinking collar or equality
of all jets from equality at a corner. C467v's claim of agreement with
one smooth transport germ near each switching characteristic still
needs checking in both sign bands.

**Ordinary charts and cutoff limits, reused.** Teschl's April2012
*Ordinary Differential Equations and Dynamical Systems*,
[Theorem2.5/proof pp40-41; Lemma2.14/Corollary2.15 pp52-53;
Theorems3.9/3.12 pp81-84; Theorem6.1/proof pp189-190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
retains reviews1061/1063's coverage for regular-chart existence,
dependence, continuation and variation. Smoothness in sqrt(t) does
not give smooth physical-time dependence at zero. Local limits require
their own estimates.

Reuse Brian Conrad, *Math396. Stokes' theorem with corners*,
[Theorem1.1/proof pp1-3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf),
and John K. Hunter, *Measure Theory*,
[Chapter4 Theorem4.24 pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11),
as assessed in review1063 and cited in C467v. Stokes on positive-cutoff
boxes requires the asserted test regularity first. DCT needs fixed
integrable majorants and pointwise limits for the relevant terms;
real-part cancellation is insufficient for complex absolute bounds.
Eight products, boundary faces, induced signs and arbitrary independent
cutoffs still need auditing. No rereading of these unchanged standard
tools is necessary. Full matching Mathlib coverage remains unchecked;
unknown availability is not evidence of absence.

### Approved continuation and bounded test

SPECIALIZE now covers exactly TARGET, permitting a later REPRODUCTION
audit of the existing C467v argument and its known supporting tools.
This is the separate approval of nomination1064; no new target is
nominated. No essential source is blocked or identified as unread.
Another generic literature turn on this scope is not justified.
The gate supplies neither a construction verdict nor a nonexistence
result and certifies no originality.

Carry C467e/audit1017, C467k/audit1033, C467p/o/audit1049,
C467q/audit1053's graph, C467r/audit1056, C467t/u/audit1062 and
C467v's existing proof. L018/L021/L024/C466a's external finite-zero/
first-zero qualification remains unreplayed. Keep n=3,R=1/4,a=1/16,
T0=1/1920,X=1/256,b_*=1/4096,H_*=1/128, actual B/beta/H/H0/F,
fixed possibly asymmetric f, raw time, divisor and common minus sign.
Impose no single physical-vertex value or vertex differentiability.

Audit all nominated links: differentiated root remainders, full auxiliary
side incidence, both directional crossing corrections, reference extension,
corner germ, continuous limits, constant-region gluing, eight separate
complex products and both complete independent-cutoff identities.
Preserve partial findings. Accept a complete component only if every
condition holds on one common time. Isolate and downgrade any failed
link; failure of this proof is not nonexistence in the joint class.
No construction repair or further interface is preapproved here.

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
A valid component could pay one local assembly interface; upper pair,
other interfaces, exterior payment, realization, all degrees and Xi
transfer remain unpaid. Route the exact next action to proof_audit/
conceptual_audit, deep_research/xhigh: this is a delicate simultaneous
smoothness and continuous-limit argument at a degenerating interface.
No RH candidate or candidate-audit escalation is warranted.
