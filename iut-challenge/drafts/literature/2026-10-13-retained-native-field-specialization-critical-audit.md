# Native local field specialization — ready critical-audit coverage

TARGET: Critically audit L054's native local field-predicate specialization, checking the completion/base-curve/parameter dictionary, unindexed K=K-double-dot=K_2 equality and separate sqrt(-1) hypothesis without asserting full native initial data.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed native definition/application assessments; checked the new L054 section, relevant L045/L048 citation and completion/parameter passages, history/185–187 and ATTEMPTS/027,030. Direct primary reads of Kedlaya Theorem 2 and Milne section 8 resolve audit-specific coverage; no new theorem-discovery query was needed.
SOURCE_EVIDENCE: Reuse inspected EtTh December 2008 author PDF pp.10,12,16,27–28 and IUT I May 2020 author PDF Definition 3.1(e), p.63; newly read Kedlaya, Introduction: the Tate curve (fall 2004), Theorem 2(a),(b), printed p.4 and proof/reference; Milne, Algebraic Number Theory v3.08 (2020), section 8 before Proposition 8.1, printed p.135, and Propositions 8.1–8.2, p.136.
COMPARISON: The named Tate theorem explicitly covers finite p-adic extensions and unique geometric parameter; the completion source uses the induced absolute value and embedded generator. Existing native definitions distinguish original base curve, unindexed K_2 and separate sqrt(-1). This is adequate coverage for auditing the existing application, not an audit verdict.
GAP: The later mathematical audit must verify that L054 actually matches these hypotheses for the same curve and embedding and limits its conclusion to field definitions. Stable-log/native cover construction and all independent numerical bridges remain unproved.
REASON: Exact completion and parameter-uniqueness hypotheses are now inspected and the defining clauses already have adequate reusable coverage. Approve one bounded audit of the completed specialization; no new lemma, root proof or native theorem application is approved.

Main gap: original finite B>=A and actual input/action/pilot/essentiality.
A successful audit would validate this narrow prerequisite for a later
native-data check; it would not resolve independent graph or theta gaps.

Essential inputs: L054 with L045,L048 and established L042,L044–L047.
Retain the same E_0/Q, F=Q(zeta_60,E_0[30]), global
K_glob=F(E_0[7]), Omega,u,w, F_u=H subset K_w=N,
M>=max(M_tors,31), full rational 30-torsion, and the pointed
Q_3 Tate isomorphism with changed q_0 in Q_3, v_3(q_0)=30,
v_3(3)=1. Original X is the once-punctured base E_0, not the
rank-one cover. Neither K_glob=N nor q_0=3^30 is assumed.

For the later audit, check whether the imported local convention justifies K_loc=N and
whether the base-changed pointed Tate isomorphism fixes q_X=q_0
without an additional hypothesis. Verify exact unindexed K_2 scope
and the separate sqrt(-1) clause. If coverage is adequate, approve
one later critical audit; if an essential clause is missing, state it
precisely and withhold approval. Do not perform the mathematical
audit or approve new mathematics during this coverage step.

Stable-log construction, native graph/label, compatible splitting,
complete selected/theta data and all numerical bridges remain open.
Preserve ATTEMPTS/027,030 and December 2008/May 2020 byte-identity
and even-level correction qualifications. L051–L053 are background,
not extra premises of this field specialization. Full matching
Mathlib coverage remains unchecked.


## Completed audit-level source comparison

LITERATURE_REASON: The new application audit requires the precise finite-extension uniqueness hypothesis and embedded-completion statement; the earlier root audit did not check this dictionary.
SCOPE: Exactly TARGET; audit the existing last proof section of L054 using L045,L048 and the already audited root memberships. No stable-log construction, graph quotient, label, compatible splitting, full selected/theta verdict or numerical comparison is covered.

The coverage step at invocation start was: Assess source coverage for a
separate critical audit of L054's native local field-predicate
specialization, including the completion/base-curve/parameter dictionary
and both distinct field hypotheses. That review is completed here;
the pending-review instructions above describe its selection history.
No mathematical audit or new derivation was performed.

### Primary hypotheses and proof cases inspected

[Kedlaya, fall 2004 handout](https://kskedlaya.org/18.727/tate-curve.pdf),
Theorem 2, printed p.4, assumes a finite extension K/Q_p and an
elliptic curve with |j(E)|>1. Part (a) gives a unique nonzero q in K
with |q|<1 for geometric isomorphism to E_q. Part (b) characterizes
isomorphism over K itself by split multiplicative reduction. The proof
of (a) uses inversion of the j-series; (b) cites Silverman, Advanced
Topics, Theorem V.5.3. These are imported theorem clauses, not rederived
here. The audit must check N's finite-extension role, the unchanged
j-value, and the actual base-changed pointed isomorphism recorded in
L048/L054. The theorem's geometric uniqueness is stronger than a choice
of uniformizing representative and is not an assertion about a cover's
parameter. No handout coefficient formula is used.

[Milne, Algebraic Number Theory v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
section 8, printed p.135, treats a field K with an archimedean or discrete
nonarchimedean absolute value, a finite separable extension L=K[alpha],
and a chosen extension of that absolute value to L. It identifies its
completion with K-hat[alpha] in the corresponding completion diagram;
the stated reason is completeness of the finite extension and containment
of L. Proposition 8.1 records the correspondence with irreducible factors;
Proposition 8.2, p.136, gives the product of completions and describes the
canonical maps. This covers an induced embedded completion, not merely
an abstract degree match. The audit should reuse L045's established
embedded closures and finite torsion coordinate lists rather than attempt
to prove a new completion theorem. No new applicability result is asserted
in this coverage review.

For the local convention and indexed definitions reuse the full inspected
comparison in `drafts/literature/2026-10-13-retained-native-base-field-predicate.md`
and the ready application assessment. Their direct author-PDF evidence is
[EtTh](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
printed pp.10,12,16,27–28, and
[IUT I](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(e), p.63. Those clauses fix q_X from the elliptic curve
underlying original X, define K_n and double-dot K_n, identify the
unindexed double-dot K with K_2, and place sqrt(-1) separately in
Theorem 1.10. IUT I uses local base change of X_F and explicitly relates
rational 2-torsion to the EtTh base-field assumption. No fresh native
extraction is claimed: web open returned metadata, subsequent text/find
calls failed, and screenshots returned references without visible images.
Adequate unchanged inspected coverage is reused, so this transient access
failure is not an essential source blocker and does not justify another
literature turn. Byte identity with journal or prior reproduction files
remains unchecked. Retain the May 2020 even-level correction qualification.

### Audit decision and boundaries

The exact target now has SPECIALIZE coverage. A later research audit may
check only the completed dictionary/substitution, cite known definitions
and theorems, and record REPRODUCTION. No reproof is needed. In particular,
it must distinguish global K_glob from K_w, the original punctured base
from a level cover, and zeta_2 from sqrt(-1). It must check the imported
uniqueness and completion hypotheses instead of merely accepting their
citation labels. Existing root proofs are audited inputs, not a reason
to repeat their audit as the entire task.

Continue if every dictionary and substitution obligation passes with
unchanged N and changed q_0; otherwise identify and repair or withhold
the precise failing assertion in a later research audit. Never infer full
EtTh or IUT initial data from a pass. ATTEMPTS/027,030 retain their distinct
exact-curve and rank-two-cover stops; neither blocks this limited audit.
No duplicate completed dictionary audit was found in the targeted records.
Full matching Mathlib coverage remains unchecked. Source readiness is
local process progress by known methods, not an advance beyond the sources
checked or evidence of an essential IUT flaw.
