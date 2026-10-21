# Selected bad-place division fields — ramification scope proposal

TARGET: Assess whether Tate uniformization forces ell to divide e(D_w/Q_p) for selected bad-place completions D_w of D=F(E[ell]) under Dupuy–Hilado arXiv:2004.13228v1's prime-to-ell Tate-parameter valuation hypothesis.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Screened the packet-field-role and full-torsion assessments, L039/L040 and ATTEMPTS/022,025,026; searched Tate torsion/division fields, nonsplit reduction, normalized parameter valuation and inertia/ramification. Read Dupuy–Hilado's complete local transvection proof and author-hosted Milne theorem passages; no novelty inference from search failures.
SOURCE_EVIDENCE: Dupuy–Hilado arXiv:2004.13228v1, sections 2.4.2, 3.2, Definition 5.3.1(4),(5), Lemma 5.4.1 with complete proof, Definition 5.5.1 (printed pp. 7,9,26–28,30); Milne, Elliptic Curves, second edition (2021), author PDF, III.3, pp. 102–103, equations (24)–(26); Milne, Algebraic Number Theory v3.08 (2020-07-19), Corollary 7.42, Remark 7.43, Theorem 7.58(a) with proof, Propositions 8.10–8.11 with proofs (pp. 124,130–131,139–140).
COMPARISON: Known Tate theory already provides the geometric parameter and a full-torsion inertia transvection, including reduction through a degree-prime-to-ell splitting extension; the remaining work is a cited local-completion/valuation specialization to the selected D_w, not a new torsion theorem or IUT objection.
GAP: Separately check the source's field-of-moduli valuation against F_u, identify D_w/F_u as the full local torsion extension, and apply the cited inertia and ramification facts to the proposed divisibility test; no such application or packet exclusion is proved this turn.
REASON: Essential source coverage is ready for the unchanged target; using the directly inspected Lemma 5.4.1 avoids rebuilding Tate uniformization or treating an inaccessible Silverman chapter as read.
SCOPE: Exactly TARGET for v in the selected bad set of the inspected exposition, p odd, ell>=5, ell!=p, ell prime to ord_v(q_v) and [F:Q(j_E)], F/Q(j_E) Galois, D=F(E[ell]), w over v and u=w restricted to F. Approves only the subsequent known-theorem application; no native equivalence, tensor-component extension, changed field, lattice calculation, sufficient admissibility or original numerical conclusion.

LITERATURE_REASON: New Tate-parameter ramification mechanism needs its essential primary torsion theorem and exact valuation/splitting hypotheses, outside the ready full-30-torsion and finite-component coverage.

## Original bounded proposal (source-status statements superseded below)

Main gap: original finite B>=A with actual input/action and pilot transport.
After L040's audit, the exact enlarged-field individual and component
realizations remain stopped. The intermediate target asks about a
different necessary condition for selected bad-place division fields,
uniformly in the base field and eligible ell. Its downstream use is
to screen future replacement packets by source-required ramification
before deriving another auxiliary logarithm or radius result. No
ramification divisibility conclusion is asserted in this proposal.

Start from the recorded packet-field-role source passages. Retrieve
the primary conditions fixing the Tate parameter, the normalized
integer valuation, split versus nonsplit multiplicative reduction,
and the selected embedding F_v -> D_w. Then search the exact and
stronger standard torsion/ramification statements from Tate
uniformization and inspect their hypotheses and relevant proof cases.
Determine whether the inspected result concerns the full division
field or a cyclic subgroup, and whether a splitting extension is
required. Do not replace normalized integer valuation by v_p without
tracking ramification. Import a matching theorem by precise citation;
do not derive and approve the proposed divisibility claim in this
literature turn.

Essential local context: L039 and L040 identify the already stopped
root-of-unity mechanism; neither is assumed to prove this new test.
Their canonical statements and the packet-field-role assessment suffice
for duplication checks. L031/L032's field data would be needed only
for a later, separately assessed field specialization, not this review.
The main unresolved assumptions here are the exact Tate parameter's
field of definition, its normalized order, and the torsion theorem's
applicability to the selected local division-field role.

Continue to a separately assessed application only if primary coverage
gives a precise ramification consequence under the actual bad-place
hypotheses. A different normalization, splitting condition or weaker
conclusion requires narrowing; an essential unavailable source parks
this dependent target. This is not another search for the blocked
native pilot/formal-quotient or actual-ind3 inclusion in ATTEMPTS/006
and the 2026-10-05 ind3 review. Those stops remain preserved. A
necessary local condition will not supply global initial data, actual
input/action, pilot transport, essentiality or original finite B>=A.
Full matching and supporting Mathlib coverage is not checked.

## Preserved interim source-review checkpoint (superseded below)

Primary Dupuy–Hilado v1 Definition 5.3.1(4),(5) was inspected directly:
the bad place v belongs to Q(j_E), and ord_v(q_v) is measured there,
not in the selected division-field completion. Section 2.4.2 fixes
integer uniformizer valuation. Section 3.2 identifies q as the geometric
Tate parameter obtained from the integer power series in 1/j_E.
Lemma 5.4.1 and its complete proof were read: its local hypothesis is
ord_L(j_E)<0 with ell not dividing that integer, and its conclusion
is an inertia transvection on a full torsion basis. The proof reduces
via L(sqrt(gamma),zeta_ell), of degree dividing 2(ell-1), before
using the split Tate torsion description. This is existing source
mathematics, not a new local conclusion. Independent exact Tate
uniformization and local ramification theorem coverage is still
being checked; no ramification application has been performed.

Book-PDF web access returned internal errors for the previously used
Silverman mirror and two alternate textbook mirrors. The versioned
Dupuy–Hilado PDF and author-hosted Milne ANT PDF are accessible.
No lemma or mathematical script was written.

## Completed primary-source comparison

The exact target text is retained. The main gap is still original finite
B>=A with actual input/action, global data, marked pilot transport and
essentiality. This review supplies source coverage for a necessary local
ramification screen of future replacement packets, independently of the
already stopped root-of-unity realizations. It establishes no new
divisibility result and creates no lemma or mathematical script.

### Fields, integer valuation and selected places

[Dupuy–Hilado, arXiv:2004.13228v1](https://arxiv.org/pdf/2004.13228v1)
is the 35-page version labeled 28 April 2020; its manuscript date is
29 April 2020. The regenerated versioned HTML displays a 2026 date;
the PDF's version label, text and printed pagination are the anchors
here. Relevant PDF passages were checked against HTML. Sections 2.4.2
and 3.2 are printed pp. 7 and 9. Definition 5.3.1 is p. 26;
Lemma 5.4.1 and its proof occupy pp. 27–28; Definition 5.5.1 is p. 30.
These correct the older assessment's imprecise page ranges without
editing or discarding its historical record.

Write F_0=Q(j_E), v in S, u a place of F above v, and w the selected
place of D above v with restriction u. Condition 5.3.1(5)(b) concerns
the geometric q_v and integer ord_v in F_{0,v}. It concerns neither
ord_w(q_v) nor the pilot root q_v^(1/(2ell)). Conditions (5)(a),(c),(d)
retain p!=ell, ell>=5 and ell prime to [F:F_0]; condition (2) retains
F/F_0 Galois. Definition 5.5.1 retains the full D=F(E[ell]) and a
selection of places over F_0. It does not replace D by the selected
cyclic subgroup's field. The later application must explicitly pass
from F_{0,v} to F_u; the degree condition cannot simply be omitted.

Section 3.2 states the uniqueness and integer power-series description
of the geometric q for a finite extension of Q_p. The supporting
[Milne, Elliptic Curves, second edition (2021), author PDF](https://www.jmilne.org/math/Books/EC2.pdf#page=107),
III.3, subsection “A p-adic analogue: the Tate curve”, printed
pp. 102–103, equations (24)–(26), gives the integer coefficient series
and j(E_q)=q^(-1)+744+196884q+..., with q expressed in 1/j. Its displayed
uniformization discussion starts with q in Q_p, so it is not imported
as a general-local-field torsion theorem. The general-local-field
coverage is the inspected Dupuy–Hilado section and lemma; the integer
series identity supports their parameter normalization. Any valuation
consequence of that identity belongs in the subsequent applicability
argument, including convergence and the leading term; none is derived
as a new claim here.

### The full-torsion theorem and essential proof cases

Import **Dupuy–Hilado v1, Lemma 5.4.1**, with its complete proof,
printed pp. 27–28. It assumes a finite p-adic field H, an elliptic
curve with ord_H(j_E)<0, and a prime ell>=3 prime to this integer.
It states existence of an element of absolute inertia and a basis
P_1,P_2 of the full E[ell] on which it acts by

    P_1 -> P_1,  P_2 -> P_1+P_2.

Both proof cases were inspected: in the split case the Galois-equivariant
Tate uniformization identifies torsion with the classes generated by
zeta_ell and Q=q^(1/ell); the Kummer generator sends Q to zeta_ell Q.
The general case first passes to H(sqrt(gamma),zeta_ell), gamma=-c_4/c_6,
whose degree divides 2(ell-1), and uses the stated valuation scaling
and inclusion of inertia groups. Thus one need not assume split
multiplicative reduction over F_u or assert q^(1/ell) belongs to the
unchanged D_w in the nonsplit coordinates. The source's explanatory
calculation for P_1 has a misplaced omission of phi; use its stated
Galois-module identity and theorem, not the ill-typed intermediate
equality. The present target also imposes ell!=p, so it makes no use
of the statement's wider residue-characteristic scope.

This is a direct import of an inspected existing theorem. The source
attributes it to Silverman, Advanced Topics, Chapter V. The original
Silverman V.3.1/V.5 material remains an unread lead: Springer chapter
DOI 10.1007/978-1-4612-0851-8_6 exposes metadata and paid access only,
while three textbook mirrors failed and a direct download failed DNS.
Silverman's author-hosted errata pp. 18–20 were checked for the
identified Chapter V material, including the V.3.1 scope clarification;
the errata are not substituted for the unread theorem. This is not an
essential blocker to importing the complete primary lemma above. No
reproof of uniformization or the Kummer/inertia result is authorized.
The separate canonical-subspace discussion following Lemma 5.4.1 is
not needed and is not imported as an untwisted nonsplit assertion.

### Supporting local/global ramification inputs

Use [Milne, Algebraic Number Theory, version 3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
166-page author-hosted PDF. Corollary 7.42, printed p. 124, states
[L:H]=e f for a finite extension of a complete discretely valued
field in the preceding theorem's characteristic-zero setting.
Remark 7.43 gives ord_L restricted to H as e(L/H) ord_H and describes
the extended value group. Theorem 7.58(a), pp. 130–131, for a finite
Galois extension with separable residue extension, identifies the
inertia fixed field with the maximal unramified subextension and
the quotient with the residue Galois group. Read its complete (a)
proof: the maximal unramified field is Galois and the kernel of residue
action is inertia. Finite p-adic residue fields meet the separability
hypothesis. Proposition 8.10, p. 139, identifies a number-field
decomposition group with the completion's Galois group; its full proof
and alternate restriction proof were read. Proposition 8.11 and the
adjacent diagram, pp. 139–140, identify the totally ramified inertia
stage and its e. These are the standard cited inputs for the pending
local degree, inertia-image and ramification application. The absolute
extension D_w/Q_p is not assumed Galois; the Galois statement must be
used over the included F_u. Tower ramification must be tracked.

The secondary numerical paper, arXiv:2004.13108v2, sections 3.4–3.5,
was inspected only for field/parameter roles. Section 3.4 identifies
the full torsion field with the kernel of the torsion representation;
section 3.5 records q in Q_p(j_E). Its sentence equating |j|>1 with
multiplicative reduction is too broad without a potential-reduction
qualification; do not use it. No conductor or discriminant theorem
from that section is imported for this test.

### Comparison, stops and bounded continuation

L039 and L040 and ATTEMPTS/022,025,026 were inspected in the necessary
statement/proof ranges. They stop particular root-of-unity field
realizations; no Tate-parameter ramification result occurs there. The
ready packet-field-role assessment is reused for full division-field
roles, not treated as prior approval of the new ramification mechanism.
No cross-notebook input or L031 logarithm certificate is needed. The
strongest relevant inspected torsion conclusion is the inertia
transvection above; the proposed divisibility conclusion is a pending
specialization of it and local field theory, not a new discovery.

The next mathematical step may test the unchanged TARGET using these
imports, retaining F_0,v,F,u,D,w and every congruence condition. Its
obligations are normalization, full local torsion-field identification,
the finite inertia image and the tower to Q_p. Continue only if all are
checked and the proposed necessary divisibility is justified. A failed
applicability check narrows or abandons that application; passing it
does not construct globally admissible data or repair any actual/native
input/action, pilot or essentiality bridge. No exact auxiliary field or
finite tensor component is tested in this turn. The original finite
B>=A gap remains open. Full matching and supporting Mathlib coverage
is not checked, and no formal verification is claimed.

Queries included `Tate curve torsion division field q 1/n Silverman
Advanced Topics V theorem 3.1 ramification`, `Tate ramification q division
field elliptic multiplicative`, `Tate curve unramified quadratic torsion
Silverman`, and `local fields inertia group order ramification index
theorem Milne ANT`; exact theorem and j-series searches followed the
identified references. Search hits without inspected statements
(including function-field torsion papers, unrelated ramification papers,
and Frobenius/rigid-geometry notes) are not inputs or novelty evidence.
The official announcement at https://zen.ac.jp/news/0ul6zqed9-0 was
rechecked on 2026-10-10: its dated 2023-07-07 inherent-flaw challenge
remains the scope, independently of adjudication. This concludes one
literature-only step; no divisibility proof has been performed.
