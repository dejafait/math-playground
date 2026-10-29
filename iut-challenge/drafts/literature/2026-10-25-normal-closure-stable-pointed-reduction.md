# Same-member normal closure — stable pointed reduction source comparison

TARGET: Determine whether L098's unconditional all-place semistability supplies stable one-pointed reduction of the unchanged E_o over every finite C_o-completion, as required by IUT I Definition 3.1(b).
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step470 compared L098 unconditional reduction and its audit, L090/L105 actual member statements, full L082 and completed audit, L078/L081 hypotheses, both 18 October pointed assessments, the 15 October predicate assessment and 12 October duality record; checked ATTEMPTS/031,033–035. Reused recorded discovery searches; no identical E_o/C_o pointed-model conclusion found in these scoped records.
SOURCE_EVIDENCE: Reinspected Conrad (21 November 2015), section 2 p.2, Theorem 5.5 and complete proof pp.14–15, small-characteristic/splitness discussion pp.15–16; Hassett math/0205009v1 section 2 printed pp.3–4. Reuse inspected minimality/Milne II.3 pp.59–61, Stacks statements and proof cases in the 12/18 October records, and qualified May 2020 IUT I Definition 3.1(b) pp.61–62 inspected on 15 October.
COMPARISON: L082 concerns different E_L/G, so its conclusion is not directly imported. Its audited general-DVR method has no curve-presentation, normality, splitness or residue-characteristic restriction excluding E_o/(C_o)_w. L098 supplies unconditional all-place semistability; L090/L105 retain the pointed curve and number field.
GAP: Essential source coverage is ready; the separate E_o/C_o applicability argument remains unwritten. No stable model or new mathematical result is derived in this literature turn.
REASON: SPECIALIZE the already audited local-family method to the unchanged member; import general theorems and reuse universal calculations under their exact hypotheses, rather than transfer L082 curve-specific conclusions or reprove known results.

The following proposal records invocation-start obligations; the completed
comparison below approves coverage, not the application.
Main gap remains original finite B>=A. The intermediate sought is only
stable one-pointed reduction for the same E_o/C_o at every finite place;
a positive result could discharge the all-place stable-reduction part of
initial-data clause (b). It would not establish the remaining clauses,
directed (*), III/P7, exact generation/full repair or essentiality.

Essential inputs for the comparison: L098's unconditional semistability
argument and qualifications, L090's literal curve/field dictionary and
L105's unchanged member; L082 with L078,L081 and its two 18 October
assessments as possible existing coverage. L062's older method is a
secondary lead only if the exact-G assessment requires it. Check exact
hypotheses and recorded audits before loading additional detailed proofs.
L098's extra ell-integrality premise must not be silently assumed: the
candidate continuation uses only its separately identified unconditional
all-place reduction statement. L113 step469 and L114 supply context,
not a stable-model theorem.

Pass the source gate only if the existing result or inspected general
theorems cover the actual pointed generic curve over every unchanged
completion, including small residue characteristics and nonsplit nodes.
If already covered literally, import that result and give only the
applicability argument; do not repeat its equations or count a duplicate
as discovery. If a needed hypothesis is missing, identify it and narrow
or abandon this target. Do not enlarge C_o, assume a single global minimal
equation, replace pointed stability by regularity, or claim a new lemma
before the separate review. Full Mathlib coverage is unchecked.

All inherited source authentication/def= qualifications and ATTEMPTS/031,
035 remain. No source retrieval is requested merely to repeat approval
of the completed L113 audit. The next turn compares this different target
with recorded coverage; it does not reopen the blocked directed-module
extraction or authentication. No cross-notebook input is proposed.

## Completed comparison — 25 October 2026, step470

LITERATURE_REASON: The saved REVIEW_REQUIRED target changes E_L/G to E_o/C_o; this step resolves that scope comparison, not a refresh of ready assembly coverage.
SCOPE: Exactly TARGET and origin O, every unchanged finite C_o-completion, including 2,3 and nonsplit multiplicative fibers; only L098's unconditional semistability passage. No field extension, ell-integrality, global minimal equation or full initial-data assertion.

The main gap remains original finite B>=A in III Corollary 3.12
(xi-f). The intermediate and downstream use are the all-finite-place
stable pointed-reduction requirement of clause (b). Independent
initial-data and directed-module gaps remain.

### Primary source scope

[Conrad, *Minimal models for elliptic curves*, 21 November 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
section 2 p.2, begins with an arbitrary DVR and elliptic curve over
its fraction field. The integral general Weierstrass equation has a
specified generic isomorphism preserving the origin. Theorem 5.5,
pp.14–15, identifies the minimal model's smooth locus with the Neron
identity open subgroup and good/multiplicative reduction with smooth/
geometrically nodal special cubics. The complete proof's minimality
comparison and geometric compactification cases were read. The discussion
pp.15–16 treats small characteristics and distinguishes splitness from
geometric nodality. Neither split branches nor residue characteristic
greater than three is required. Reuse minimality/existence coverage
in section 2 p.6 and Milne, *Elliptic Curves*, second edition (2021),
II.3 pp.59–61, as inspected in the 18 October assessment; no fresh
Milne retrieval or general-theorem reproof is claimed.

[Hassett, *Moduli spaces of weighted pointed stable curves*,
math/0205009v1, 1 May 2002](https://arxiv.org/pdf/math/0205009v1),
section 2, printed pp.3–4, was reinspected through the complete family
and stability definitions: noetherian base, proper flat family of
connected nodal geometric fibers of fixed arithmetic genus, smooth
markings and relative log-canonical ampleness. Weight one is ordinary
pointed stability; no residue characteristic is excluded. Earlier local
records cite pp.2–3, but this retrieved v1 starts section 2 on printed
p.3 and continues the conditions on p.4. This corrects pagination,
not the imported statement. No moduli-existence theorem is needed.

Reuse the precise statements and essential proof cases read in
`drafts/literature/2026-10-12-native-all-place-critical-audit.md`,
sections “Relative-duality hypotheses and inspected proof cases” and
“Genus and ampleness inputs”, and the two 18 October assessments.
These give direct primary links and hypotheses for Stacks 0A9W
(48.15.1), 0A9X (48.9.7), 0AA4 (48.14.2), 0ATX (48.16.3),
0E6N (109.19.1/Definition 109.19.2), 0E6R (109.19.3), 01XT
(30.8.1), 01VG (29.38.2) and 01PT (28.27.2). Covered cases are
proper composition, pseudo-coherent effective Cartier immersions,
relative curve duality, Gorenstein base change, projective cohomology
and positive-power ampleness. They require neither regular total
space nor smooth special cubic. Retain their recorded live-version
qualification; no fresh Stacks retrieval or pinned revision is claimed.
L082's full audited verification is reusable method context, not an
identification of E_L with E_o.

Reuse the complete-clause inspection in
`drafts/literature/2026-10-15-everywhere-stable-pointed-reduction.md`:
Mochizuki, IUT I, May 2020 reproduction, Definition 3.1(b), printed
pp.61–62, requires stable reduction of the type-(1,1) curve at every
finite place. Selected-place multiplicativity is separate. Retain
unverified author/reproduction byte identity and journal-version
equivalence; ATTEMPTS/035's authentication route remains parked.
The current review neither changes the recorded challenge version
nor selects a new challenge route or adjudication claim.

### Scope difference, justified work and discriminating test

The input objects are L090/L105's actual E_o and C_o, not L078's
auxiliary witness and H,N equalities. L098's “Full torsion and
semistability at every actual completion” and step393 audit supply
semistability without the displayed extra ell-integrality assumption.
Only that unconditional passage is proposed as input: neither its
conditional support conclusion nor integral j at ell is imported.
The pointed elliptic curve, number-field completions and reduction
premises match the general sources' scope. This comparison does not
construct stable models or assert the desired conclusion for them.

L082's stated conclusion cannot simply be applied to this other curve.
Its audited local-family calculations, however, use arbitrary complete
number-field DVRs and semistable pointed elliptic curves, independently
of parameter, torsion, field normality and its special H,N data.
SPECIALIZE therefore approves a separate REPRODUCTION applicability
argument, reusing those universal calculations explicitly under their
hypotheses. Do not copy the full proof as a new result or reprove the
general sources. An existence citation alone does not check the actual
pointed family and whole-DVR marked ampleness.

The application must check the pointed generic identification over each
original completion, minimal general integral equation, proper flat
finite-presentation family, geometric nodality/genus, smooth Cartier
origin, whole-DVR divisor identity, relative-duality hypotheses/shifts
and relative marked ampleness. L082's audited universal computations
can be reused after checking their base and input hypotheses. Retain
general a1,a3 at 2,3; geometric nodality does not demand split branches.
Neither a regular polygon nor a global minimal equation is required.

Continue if the argument works over every unchanged completion; if
an essential hypothesis fails, identify the failed case and narrow or
abandon this same-field assertion, without enlarging C_o. An uncovered
replacement needs REVIEW_REQUIRED. ATTEMPTS/031 and 033–035 concern
actual marked-coordinate normalization, classification/Frobenius tests
and authentication; none supplies an input or obstruction here, and
all remain preserved. Full initial data/III/P7, directed (*), generation/
full repair, factor-four excess, action/factorization/pilot, def=,
essentiality and finite B>=A remain open. Full matching and supporting
Mathlib coverage is unchecked, without an absence claim.

This step clears essential source coverage locally; it claims no
mathematics beyond the checked methods. No lemma, mathematical script,
PROOF.md or DAG.md is changed. No new external discovery lead remains
essential or is presented as an inspected theorem.
