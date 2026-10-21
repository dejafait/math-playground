# Retained native base-field predicate — completed source review

TARGET: Determine the complete EtTh local base-field predicate K=K-double-dot=K_2 for the retained completion N and identify precisely which obligations remain after L054, without invoking graph factorization or theta splitting.
CHECKED: 2026-10-13
DECISION: IMPORT
SEARCH_EVIDENCE: Reused native-cover and Tate assessments; checked L054 and hypotheses/conclusions of L048,L051, targeted cover histories and ATTEMPTS/027,030. Queries: site:kurims.kyoto-u.ac.jp/~motizuki "K_2" "Theta"; site:kurims.kyoto-u.ac.jp/~motizuki "base field" "2-torsion" "Definition 2.5". Direct author PDFs supply the evidence; search results add no theorem.
SOURCE_EVIDENCE: Mochizuki, EtTh, December 2008 author PDF (112 pages), section 1 opening p.10, K_n p.12, J_n p.13, double-dot definitions p.16, Definition 1.7 and preceding conditions p.25, Definition 1.9/Theorem 1.10 and proof pp.27–28, section 2 opening/Definition 2.1 pp.32–33, Proposition 2.2 and proof pp.34–35, Definition 2.5(i) p.36; IUT I May 2020 author PDF (186 pages), Definition 3.1(c)–(f) pp.62–63, especially the explicit 2-torsion/base-field assertion in (e).
COMPARISON: The equality predicate is K=K_2 with K_2=K(zeta_2,q_X^(1/2)); double-dot K is defined as K_2, not an all-radicals extension. The square root of -1 is a separate Theorem 1.10 hypothesis. L054 covers the memberships once the original once-punctured E_0 and its local Tate parameter are matched; graph and splitting conditions remain separate.
GAP: No defining clause for the field equality remains unread. A later application must justify the local symbol assignment and same underlying curve/parameter; this review does not perform that specialization or establish any native cover type, selected-place section or theta splitting.
REASON: Primary definitions and IUT I's explicit rational-2-torsion assertion settle the source-scope uncertainty. A bounded field-predicate application is covered; no graph theorem, new root calculation or reproof is needed.

LITERATURE_REASON: Scope changed from two root memberships to the complete native field predicate; the previous shorthand omitted the indexed radical-field distinction and precise q_X assignment.

This file proposes one source comparison only. It neither approves a
mathematical application nor asserts that the complete predicate holds.
Reuse the existing inspected source record where adequate; extract only
missing essential defining clauses and referenced hypotheses. Record
LITERATURE_REASON for the changed scope from two field memberships to
the entire native predicate. Do not retry the blocked graph theorem or
derive a new root-membership lemma merely to enlarge the local record.

The main gap remains original finite B>=A and the actual
input/action/pilot/essentiality bridge. The intermediate target would
clarify whether the audited memberships discharge an entire local
prerequisite or only part of it, and identify a precise later application
or obstruction. It cannot establish sufficient initial data on its own.

Essential inputs: L054 with L045,L048 and their established
L042,L044–L047 inputs; retain the same E_0/Q,
F=Q(zeta_60,E_0[30]), global K=F(E_0[7]), Omega, u,w,
F_u=H=Q_3(zeta_60) subset K_w=N=Q_3(zeta_420,3^(1/7)),
M>=max(M_tors,31), full rational 30-torsion, pointed Q_3 Tate
isomorphism and v_3(q_0)=30 with v_3(3)=1. L053 is background
only; its point-group quotient is not a native graph identification.
Neither K=N nor q_0=3^30 is assumed. Matching the native symbols to
these objects is an obligation, not an established identification.

Continuation/abandonment test: obtain a complete, cited list of defining
conditions and a theorem-level comparison with the retained inputs.
Approve a narrowly stated later application only if essential coverage
is present. If the definition needs extra structure, name that exact
obligation and withhold the full-predicate claim. If essential text is
persistently inaccessible, park this dependent target and select a
different independently testable mechanism; do not repeat the graph
source-access route. No native verdict is computed in this proposal.

Preserve the December 2008/May 2020 version and byte-identity
qualifications, ATTEMPTS/027,030, graph/label and selected/theta gaps,
and the original numerical gap. Full matching Mathlib coverage remains
unchecked, not asserted absent.

## Completed comparison, superseding the proposal status above

This is a literature-only import of definitions and an existing source
assertion. No new mathematical lemma or retained-packet verdict is supplied.
The proposal paragraphs remain selection history; their pending source
status is superseded here.

### Exact definitions and hypotheses

[EtTh, December 2008 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
printed pp.10,12–13,16, starts with a finite extension K/Q_p, an algebraic
closure, and a stable log curve of type (1,1) with singular split special
fiber and smooth algebraized generic fiber. Its q_X is the q-parameter of
the elliptic curve underlying the original X, not a later level/theta
cover. Rename the paper's integer index n to avoid our field N:

K_n = K(zeta_n,q_X^(1/n));
J_n = K_n(a^(1/n) : a in K_n);
double-dot K_n = K_(2n);
double-dot J_n = double-dot K_n(a^(1/n) : a in double-dot K_n);
double-dot K = double-dot K_1 = double-dot J_1 = K_2.

These defining formulas take roots in the fixed algebraic closure.
The unindexed double-dot field imposes no closure under radicals at
every level. Primitive zeta_2 means -1 in characteristic zero, distinct
from sqrt(-1). Double-dot Y=Y_2 also names a covering; base-field
equality does not identify the coverings.

Definition 1.7's preceding discussion, p.25, assumes the field equality
and non-arithmeticity of X separately for its type-(1,mu_2) construction.
Definition 2.5, p.36, returns to section 1 and requires odd l, odd residue
characteristic and K=double-dot K. Part (i) also requires the Definition
2.1 rank-one quotient to factor through the completed tempered graph
quotient, and the Proposition 2.2(ii) splitting defining the further
theta cover to respect Theorem 1.10(iii)'s {+1,-1}-structure. None of
these cover requirements changes the definition of the field equality.

Theorem 1.10, pp.27–28, concerns type-(1,mu_2)_± curves over finite
p-adic fields containing sqrt(-1), a topological-group isomorphism, and
preservation of the specified theta-class orbit by its induced map.
Part (iii) additionally retains odd residue characteristic and standard
type. Definition 1.9, p.27, defines standard type by requiring the
maximal-valuation unit value in a standard set to equal +1 or -1.
The whole proof was read: (i),(iii) reduce to (ii), which invokes the
cited tempered-anabelian theorem and dual graphs for decomposition-group
transport. No such transport application, standard type or compatible
splitting is inferred for this packet here.

### Dictionary and remaining application work

Keep global K=F(E_0[7]) distinct from EtTh's local K. The proposed
assignment is K_EtTh=K_w=N, with original X the once-punctured base
curve E_0 over N, not L053's degree-seven source or a theta cover.
L048's pointed Q_3 Tate isomorphism supplies the available justification
for the same underlying curve's parameter after base change. Matching
that parameter with q_X is a later application obligation, not a new
result here. L051 supplies the stable pointed cubic at H; using its
extension to N must justify stable/log base change, without replacing
it by the regular I_30 polygon.

[IUT I, May 2020 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(e), printed p.63, explicitly says (b)'s rational 2-torsion
implies EtTh's local base-field assumption. Its local X notation is
base change of X_F, consistent with this proposed dictionary. It imposes
the graph type separately, and (f) imposes the cusp label. This source
assertion is useful scope evidence, not a verification of all initial
data. No complete place section V or selection of w is supplied here.

After L054, the unindexed field definition indicates no further radical
membership obligation. The remaining application is symbol/curve
matching followed by substitution, with sqrt(-1)'s separate role kept
explicit. It needs no uniformization reproof or new membership lemma.
Record that narrow continuation separately for supervisor approval.

Graph factorization/label, compatible theta splitting, all-place
selection, actual input/action, pilot transport, essentiality and
original finite B>=A remain open. L053's point-group exponent supplies
no graph identification. ATTEMPTS/027's exact old-curve exclusion and
ATTEMPTS/030's rank-two-cover stop remain unchanged. Targeted local
searches found summaries and L054's narrower memberships, not a completed
native specialization; no novelty follows from the search.

Continue with a correctly matched same-curve field-predicate application;
abandon any inference of full Definition 2.5(i) from memberships alone.
Primary web PDF text was readable, so essential coverage is not blocked.
Shell PDF download failed at DNS resolution; screenshot calls returned
references only and are not visual verification. Author versions and
printed page numbers above were inspected; byte identity with the prior
reproduction or journal files is unchecked. Retain May 2020's correction
excluding the old even-level Remark 2.2.1. Full matching Mathlib coverage
remains unchecked; no absent-theorem or beyond-source progress is claimed.
