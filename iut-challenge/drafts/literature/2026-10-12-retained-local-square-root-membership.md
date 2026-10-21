# Retained local square-root membership — completed source comparison

TARGET: Test whether the unchanged completion N contains a square root of q_0 and a square root of -1, without asserting native graph type or complete native base-field conditions.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready split-Tate packet and rank-one audit assessments; searched local square-root/q_0 occurrences and relevant ATTEMPTS/027,030 and history/181. External query: Tate curve rational two torsion q square uniformization Galois equivariant. Inspected author-hosted theorem and rational-point statements; nonprimary search hits are not evidence.
SOURCE_EVIDENCE: Kedlaya, Introduction: the Tate curve, fall 2004, Theorem 1 printed p.3 and group-law/surjectivity discussion pp.3–4, https://kskedlaya.org/18.727/tate-curve.pdf; Milne, Elliptic Curves, second edition (2021), III.3 pp.102–103, especially the finite-extension rational-point statement following (26), https://www.jmilne.org/math/Books/EC2.pdf; reuse previously inspected geometric torsion coverage EC2 II.6 Proposition 6.3 pp.70–71.
COMPARISON: Named Tate uniformization covers same-field representatives and Galois-equivariant group transport for nonzero q_0 in Q_3 with |q_0|_3<1; standard torsion and primitive-root inputs cover the proposed membership test. The exact retained-field verdict requires an elementary specialization, not a new uniformization theorem.
GAP: Next research must justify full geometric 2-torsion rationality for the same changed curve, the passage from a torsion class to a square-root representative and its field membership, and the exact order of the proposed cyclotomic root. No verdict is derived here; graph/label, complete base-field and selected/theta conditions and finite B>=A remain open.
REASON: Essential representative/descent coverage is now inspected and adequate for the unchanged target. Import the named Tate theorem and specialize only these two field predicates; do not retry the parked graph route.

LITERATURE_REASON: Changed target from a limited algebraic-cover audit to
local square-root membership for the changed parameter; reuse existing
Tate coverage and inspect only any essential missing descent case.

The main gap remains original finite B>=A and actual input/action/pilot/
essentiality. This intermediate target tests two local field predicates
that may later help check the native hypotheses in the source notes.
It does not require a graph theorem or identify all double-dot conditions.

Essential inputs: L045,L048; their established L044–L047,L042 inputs
remain retained. Keep E_0/Q,F=Q(zeta_60,E_0[30]),K=F(E_0[7]),
F_u=H=Q_3(zeta_60),K_w=N=Q_3(zeta_420,3^(1/7)), the fixed embedding
in Omega, M>=max(M_tors,31), v_3(3)=1 and v_3(q_0)=30. Retain the
full rational 30-torsion and pointed Q_3-defined Tate isomorphism.
Neither K=N nor q_0=3^30 is assumed. L053 is motivation, not an
additional input needed for this field-membership test.

Continuation/abandonment test: after approval, establish or refute each
membership in the same N. Required enlargement of N fails this test;
a theorem gap requires narrowing or source review. Passing establishes
only these memberships, not graph type, generator label, complete native
base-field predicates, all selected places, theta data or a numerical bound.

No test, new lemma or derivation for this target is supplied here.
The proposal-status sentences above are preserved selection history;
the completed source comparison below supersedes their pending status.
Mathlib matching coverage remains unchecked. Native source-version and
byte-identity qualifications and all historical stops are preserved.

## Completed comparison and approved scope

SCOPE: Exactly TARGET, retaining L045/L048's same curve, embeddings and fields; permits a geometric 2-torsion Tate-class membership argument and an elementary primitive-root order check in H subset N. No field enlargement, curve reselection, graph identification, native-label argument or proof of all native base-field predicates is approved.

The main gap is original finite B>=A and actual input/action/pilot/
essentiality. The intermediate target is the two same-N membership
predicates. Their plausible downstream use is a limited local-prerequisite
check, not completion of the parked graph route.

### Inspected theorem scope and proof qualifications

[Kedlaya's author handout](https://kskedlaya.org/18.727/tate-curve.pdf),
fall 2004, Theorem 1, printed p.3, applies over a finite p-adic field
with nonzero parameter of absolute value less than one. It states
Galois-equivariant surjectivity with kernel q^Z, also over finite
extensions. Read the group-law discussion and the surjectivity
deferral on p.4: the handout is a summary, not a complete proof.
It refers to Silverman, *Advanced Topics in the Arithmetic of
Elliptic Curves* (1994), V.3.1 and V.4. That chapter remains unread;
it is unnecessary to reprove the named theorem. Retain the previously
recorded displayed-coefficient discrepancy: standard coefficients
come from Milne, rather than this handout's a4 display.

[Milne EC2](https://www.jmilne.org/math/Books/EC2.pdf), second edition
(2021), III.3, printed pp.102–103, fixes the standard equation and
states after (26) the group identification E_q(L)=L^*/q^Z for every
finite extension L/Q_p when q belongs to Q_p^* and |q|<1. This is
stronger than merely identifying Galois-fixed quotient classes.
L048's q_0 belongs to Q_3 and its pointed Q_3-isomorphism matches
this scope; the finite fields H and N are permitted extensions.
The book cites the named Tate theorem, rather than proving it here.
The retained II.6 Proposition 6.3 torsion-count coverage uses FIELD
characteristic zero; residue characteristic 3 does not restrict order 2.

### Exact remaining applicability obligations

Use L045's full rational 30-torsion and L048's pointed Tate
isomorphism for the same reselected E_0. A research proof must explain
why these inputs control all geometric 2-torsion, then handle the
representative ambiguity modulo q_0^Z explicitly. Galois-fixed classes
must not silently be treated as fixed representatives. Same-field
surjectivity above is an available route; a geometric representative
argument must instead check its possible q_0-power ambiguity.
The primitive zeta_60 retained in H permits a separate elementary
root-order test; this requires no Hensel computation or new theorem.
These are approved proof obligations, not completed derivations or
membership verdicts.

No exact local membership result is duplicated in the searched records.
L053's point-group exponents and stack cover do not decide this test.
ATTEMPTS/027 excludes globalization of the old exact q=3^30 curve;
this test retains the changed q_0 and does not reopen that stop.
ATTEMPTS/030 excludes rank-two multiplication as the native basic cover;
it neither rules out nor establishes these local predicates. Existing
source notes motivate them but do not authorize a complete native
base-field conclusion. No novelty claim follows from the search.

Continue if each membership can be adjudicated inside the same embedded
N; required enlargement fails the test. A missing essential theorem
would require another narrow source review, not dependent mathematics.
Passing proves only these predicates. Essential inputs are L045,L048,
with their established L042,L044–L047 assumptions retained, including
M>=max(M_tors,31), v_3(3)=1, v_3(q_0)=30 and full rational 30-torsion.
Neither q_0=3^30 nor K=N is assumed. Native May 2020 source qualifications,
all-place selection, theta data, graph/label and the original numerical
comparison remain unresolved. Full matching Mathlib coverage is not
checked; no mathematical script, lemma or reproof is needed this turn.
