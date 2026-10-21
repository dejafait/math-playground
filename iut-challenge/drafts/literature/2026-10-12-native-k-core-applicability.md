# Native K-core applicability — completed source review

TARGET: Assess the native K-core hypothesis for the unchanged once-punctured elliptic curve X_F and identify a checkable applicability criterion.
CHECKED: 2026-10-12
DECISION: IMPORT
SEARCH_EVIDENCE: Scoped native assessments, foundations/02, packet-field-role assessment and history/167 leave K-coricity unresolved. Targeted K-core/CanLift/punctured-hemi-elliptic/exceptional-j searches found CanLift Proposition 2.7 and Sijsling arXiv:1707.01158v2, section 3.1 Table 4; this is known coverage, not a novelty search result.
SOURCE_EVIDENCE: Read CanLift section 2 defining categories, Definition 2.1, Remarks 2.1.1–2, Proposition 2.3 statement/proof and Definition 2.6/Proposition 2.7 statement/full proof, author PDF pp.8–11,14–15; Sijsling v2 introduction, Lemma 1.1.1 and section 3.1/Table 4, PDF pp.1–4,10–11 and experimental HTML for exponents; native May 2020 IUT I Definition 3.1(c,d), reproduced p.62. Details and access qualifications: drafts/2026-10-12-native-k-core-source-notes.md.
COMPARISON: The native object is C_K=[X_K/{±1}], not X_K itself. Known punctured-hemi-elliptic and base-field criteria plus Sijsling's complete four-class table provide a finite j-exception test; L048 already records the needed local j-valuation. L051's reduction and L050's descent contrast neither replace nor obstruct this criterion.
GAP: Source coverage now supplies a checkable criterion, but its application to the retained curve and descent to its actual division field remain unperformed. Covering/cusp/full selected data and original finite B>=A are independent gaps.
REASON: Import exact known criteria and exceptional models; propose their routine applicability argument separately, without redoing classification, Belyi computation, curve selection or reduction audit.
LITERATURE_REASON: The newly proposed K-core target has essential unread defining sources and criterion hypotheses; the ready reduction assessment does not cover them.
SCOPE: Exactly TARGET: source criterion identification for the unchanged X_F and native quotient; no new K-core application, reselection, covering, field extension or numerical comparison is performed.

The main gap is original finite B>=A. This intermediate target seeks
an exact criterion for an unverified native initial-data hypothesis.
Its downstream use is to decide whether the retained arithmetic packet
supports further native constructions or has an independent obstruction.

Essential inputs: L051,L045,L048, with L044–L047,L042 through them;
L049 is background and L050 contrast only. Keep the same existential
E_0,F=Q(zeta_60,E_0[30]),X_F=E_F minus origin,Omega,u,H,N,
M>=max(M_tors,31),v_3(3)=1,v_3(q_0)=30, without q_0=3^30.
A criterion requiring unprovided effective coefficients does not
automatically apply to this existential curve.

Extract the exact K-core terminology and references from the qualified
May 2020 native source, then primary theorem hypotheses and essential
proof cases before larger passages. Reuse the earlier predicate and
reduction coverage. Do not equate an orbicurve model with an elliptic
descent by analogy. The earlier AbsTopIII retrieval failure neither
settles accessibility of a K-core criterion nor refutes this curve.

Continuation test: approve a separate mathematical application only
if an inspected criterion gives a checkable test for unchanged X_F,
listing all unresolved assumptions. Record any source-supported
obstruction precisely, without claiming an IUT flaw. If essential
coverage remains inaccessible or no criterion is obtained, record the
limited result and select an independently testable target instead of
repeating the completed reduction audit. No K-core conclusion is
derived or approved by this proposal.

Covering/cusp/full selected-place data, actual inputs/actions, pilot,
essentiality and finite B>=A remain open. Preserve ATTEMPTS/022,025,
026,027,028 and the native reproduction qualification. Full matching
Mathlib coverage remains unchecked.

## Completed review — 2026-10-12

The preceding proposal records the turn-start scope; the fields above
and this completion supersede its missing-source verdict. Primary
statements, proof cases, versions and retrieval limits are recorded in
the [source notes](../2026-10-12-native-k-core-source-notes.md).

The exact criterion uses CanLift Proposition 2.7, Proposition 2.3(i,ii)
and Sijsling section 3.1 Table 4. Check the same elliptic curve's
j-invariant against the four printed values, retain the stack quotient
and justify base-field transfer. This is an applicability task for
known results; no classification reproof is justified. The existing
L048 proof, section “The changed curve's geometric parameter”, explicitly
records v_3(j(E_0))=-30, so the existential coefficients need not be
computed for that future test.

No exclusion comparison or K-core conclusion for E_0 is made here.
The independently required level-cover/cusp structure in Definition
3.1(d–f) is outside this assessment. The newly saved application
assessment must receive separate next-turn approval before invocation.
This is useful local source progress, with no progress beyond the
classification checked and no demonstrated IUT flaw.
