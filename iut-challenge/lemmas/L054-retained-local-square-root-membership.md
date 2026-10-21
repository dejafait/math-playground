# L054 — Square-root membership in the unchanged local packet

## Hypotheses

Retain the same reselected E_0/Q and embeddings of L045 and L048.
Thus Omega is an algebraic closure of Q_3,
H=Q_3(zeta_60) subset N=Q_3(zeta_420,3^(1/7)) inside Omega,
where zeta_60 is primitive of exact order 60. Set
F=Q(zeta_60,E_0[30]) and K=F(E_0[7]); the induced embedded
completions are F_u=H and K_w=N. Full geometric 30-torsion is
F-rational. The fixed original-cubic precision is
M>=max(M_tors,31). The same pointed curve E_0 over Q_3 is
Q_3-isomorphic to the standard Tate curve E_(q_0), with q_0 in
Q_3, 0<|q_0|_3<1 and v_3(q_0)=30 in the normalization v_3(3)=1.
Neither q_0=3^30 nor equality of the global K and its completion N
is assumed.

For the field-predicate specialization below, write K_glob=K and
K_loc=K_w=N to distinguish the global number field from EtTh's
local base field. Fix X_F=(E_0 over F) minus its origin, and
X_loc=X_F base-changed along F -> K_glob -> K_w. Interpret only
the field definitions in Mochizuki's EtTh, December 2008 author
version, and the local base-curve convention in IUT I, May 2020
author version, Definition 3.1(e). No complete selected-place set,
stable-log construction, graph cover or theta datum is assumed.

## Conclusion

There exist s,i in H (hence in unchanged N) such that

s^2=q_0 and i^2=-1.

In particular N(q_0^(1/2))=N and N(sqrt(-1))=N for either choice
of these roots in Omega. For this fixed once-punctured base curve,
the EtTh field definitions specialize to

q_X=q_0, (K_loc)_2=N(-1,q_0^(1/2))=N,
and K_loc=double-dot K_loc=(K_loc)_2.

Thus the unindexed native local base-field equality holds, and the
separate sqrt(-1) membership also holds. This does not establish
the hypotheses of an EtTh cover or theta theorem, a native graph
type, graph-generator label, compatible splitting, selected/theta
data or the original finite B>=A comparison. The separate audit
below validates the two root memberships; the subsequent separate
field-specialization audit validates only the dictionary and field predicates.
No progress beyond the checked known results is claimed.

## Proof

### Imported theorem and applicability

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-12-retained-local-square-root-membership.md`.
Milne, *Elliptic Curves*, second edition (2021),
[III.3, pp.102–103, the finite-extension statement following (26)](https://www.jmilne.org/math/Books/EC2.pdf),
gives the named Tate uniformization as a group identification
E_q(L)=L^*/q^Z for every finite extension L/Q_p when
q in Q_p^* and |q|_p<1. Kedlaya,
[*Introduction: the Tate curve*, fall 2004, Theorem 1, p.3](https://kskedlaya.org/18.727/tate-curve.pdf),
states the Galois-equivariant surjection and kernel q^Z, including
finite extensions. Import this theorem; do not reprove uniformization
or use the warned coefficient display in the handout. L048 puts
q_0 in Q_3 with the required strict absolute value and supplies a
pointed Q_3-isomorphism. H is a finite extension of Q_3, so the
same-field group identification applies to E_0(H).

Milne, the same book, II.6, Proposition 6.3, pp.70–71, states that
geometric n-torsion has rank two over Z/nZ for n prime to field
characteristic. Here characteristic is zero, so geometric 2-torsion
has exactly four points. The elementary representative and root-order
calculations below are the required specialization, not a reproof of
either imported theorem.

### All geometric 2-torsion is H-rational

For every geometric point P with 2P=0, one has
30P=15(2P)=0. L045's full geometric 30-torsion rationality
therefore gives F-rationality of every geometric 2-torsion point.
Its embedded completion F_u=H retains these coordinates. L045's
global/local full-torsion-set identification ensures this covers all
points over Omega, not just an injected subset. Hence E_0(H)[2]
has exactly four points. The pointed Tate isomorphism transports
the group law and all four points to E_(q_0)(H)[2].

### Same-field representative and its exponent

Write [z] for the class of z in H^*/q_0^Z. Such a class is
2-torsion precisely when z^2=q_0^m for an integer m. This uses
same-field surjectivity: each of the four rational torsion points
has a representative z in H^*, rather than only a Galois-fixed
geometric class.

If m=2r is even, then (z/q_0^r)^2=1. Characteristic zero implies
z/q_0^r is 1 or -1, so [z] is [1] or [-1]. These are distinct:
if -1=q_0^a for an integer a, valuation gives 0=30a, whence
a=0 and -1=1, a contradiction. Thus classes represented by an
even m account for exactly two of the four 2-torsion classes.
At least one remaining class has z in H^* with z^2=q_0^(2r+1)
for some integer r. Put s=z/q_0^r in H. Then s^2=q_0.

The parity test is independent of representative choice: replacing
z by z q_0^a changes m to m+2a. All powers used are integral
powers of the nonzero element q_0 and belong to H, including for
negative r. No rationality of an arbitrarily chosen geometric
representative has been assumed.

### Square root of minus one

Put i=zeta_60^15 in H. For a primitive root of order 60, the
order of its fifteenth power is 60/gcd(60,15)=4: explicitly,
i^a=1 if and only if 60 divides 15a, equivalently 4 divides a.
Thus i^2 has exact order two. In this characteristic-zero field
the polynomial X^2-1=(X-1)(X+1) has only the roots 1 and -1;
the root of exact order two is -1. Therefore i^2=-1.

Since H subset N, both roots already belong to the unchanged
embedded N. The other roots are -s and -i, also in H; adjoining
either choice does not enlarge N. No reduction modulo 3, Hensel
computation, replacement of q_0 by 3^30 or global-field membership
claim is used. ATTEMPTS/027 and ATTEMPTS/030 remain intact.

### Separate critical audit — 2026-10-13

**Verdict and scope.** The two memberships pass under the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-12-retained-local-square-root-critical-audit.md`.
The audit reuses the precisely cited torsion and same-field Tate
theorems above and checks their application independently. No new
uniformization, descent or native-graph assertion is used. No mathematical
correction or additional direct lemma input is required: L045 supplies
the full torsion and embedded completion, while L048 ensures that these
belong to the same reselected split Tate curve and changed parameter.

**The same curve and all four points.** L048 fixes the precision before
reselection and applies L045 to that very E_0, with F_u=H inside Omega.
For that equation, L045's inclusion of global into local geometric
30-torsion is bijective: the inclusion is injective on coordinates and
both sets have 30^2=900 points by Milne II.6 Proposition 6.3. Every
point of E_0(Omega)[2] lies in this local 30-torsion set because
30P=15(2P)=0. It therefore comes from the global list whose
coordinates lie in F, and hence in H under the retained embedding.
The same cited theorem at n=2 gives exactly 2^2=4 distinct points,
including the origin. The count uses characteristic zero, not a
hypothesis on residue characteristic. This verifies full 2-torsion
rationality rather than rationality of a selected cyclic subgroup.

L048's split-reduction application of the named Tate theorem supplies
an isomorphism of elliptic curves over Q_3, preserving their origins.
After extension to H it remains a group isomorphism, so it carries all
four points to E_(q_0)(H)[2]. Its parameter is the changed q_0 in Q_3,
with 0<|q_0|_3<1 and v_3(q_0)=30; no step replaces it by 3^30.

**Representatives, parity and exhaustion.** H/Q_3 is finite, and q_0
belongs to Q_3^*. Thus Milne III.3, the statement after (26), applies
over H itself and identifies E_(q_0)(H) with H^*/q_0^Z. Surjectivity
over H is the essential input: taking fixed points of a geometric
quotient without this theorem would not supply the representatives.
For each of the four classes choose z in H^*. Being killed by two
means exactly z^2 in q_0^Z. The exponent m with z^2=q_0^m is unique,
since q_0^a=1 implies 30a=0 and a=0. Changing representative to
zq_0^a changes m to m+2a, so its parity is well defined on a class.

When m=2r, the equation (zq_0^(-r))^2=1 in the field H forces
zq_0^(-r)=1 or -1. Conversely both [1] and [-1] are killed by two
and have even exponent. They are distinct: an equality would imply
-1=q_0^a, whose valuation forces a=0, contradicting -1!=1. Hence
there are exactly two even classes. Since there are four classes in
total, an odd class exists. For its same-field representative write
m=2r+1 with r an integer. Then s=zq_0^(-r) is in H^* and
s^2=q_0. Negative integers r are permitted because q_0 is nonzero.
There is no implicit extraction of a root in this normalization:
only integral powers of an element already in H are used. This
establishes the claimed root without any enlargement of H or N.

**Exact cyclotomic order and the endpoint fields.** The retained
zeta_60 has exact order 60 in Omega and belongs to H. For any integer
a, (zeta_60^15)^a=1 is equivalent to 60 dividing 15a, which is
equivalent to 4 dividing a. Thus i=zeta_60^15 has exact order four,
i^2 has order two, and the field factorization X^2-1=(X-1)(X+1)
forces i^2=-1. No residue-field reduction is used; such reduction
could lose part of a root's order and is unnecessary here.

Both s and i are in the fixed H subset N. The roots of X^2-q_0
in Omega are exactly s,-s, and those of X^2+1 are i,-i: the
factorizations and characteristic zero rule out any further roots.
Consequently every choice of either root lies in N, proving both
asserted unchanged-field adjunction equalities. This is a local
statement; it does not infer that q_0 or its square root lies in the
global number field K merely because it lies in K_w=N.

All four advertised tests pass. This validates a limited input by
known methods, not a result beyond the inspected sources or a
demonstration of an IUT flaw. The native May 2020 source qualifications,
parked graph/label bridge, complete native base-field and selected/theta
conditions, actual input/action/pilot/essentiality, and original finite
B>=A remain unresolved. ATTEMPTS/027,030 are not reopened. No numerical
certificate or mathematical script is needed for the finite counting,
integer parity and exact-order checks. Full matching Mathlib coverage
remains unchecked.

### Native local field-predicate specialization — 2026-10-13

**Imported definitions and scope.** Reuse the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-13-retained-native-base-field-application.md`
and its completed source comparison. Mochizuki,
[*The Etale Theta Function and its Frobenioid-theoretic Manifestations*,
December 2008 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
section 1 opening, printed p.10, and the definitions on pp.12,16,
uses a finite p-adic base field and the q-parameter q_X of the
elliptic curve underlying the original X. For a positive integer n
its fields are K_n=K(zeta_n,q_X^(1/n)) and double-dot K_n=K_(2n);
the unindexed double-dot K is double-dot K_1=K_2. These are
definitions, not an all-radicals closure or a theorem to reprove.
Theorem 1.10, pp.27–28, separately assumes sqrt(-1) in the base
field; the membership below verifies only that field hypothesis,
not the theorem's curve, theta-orbit or group-isomorphism hypotheses.

Mochizuki, [*Inter-universal Teichmuller Theory I*, May 2020 author
PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(e), printed p.63, uses the local base change of X_F
and explicitly attributes the EtTh local base-field condition to
rational 2-torsion from (b). This confirms the defining scope; it
is not used to assume the remaining initial-data conditions.

**The local field and original curve.** L045 supplies the induced
completion of the actual global K_glob=F(E_0[7]) at w as the
embedded N, a finite extension of Q_3 inside Omega. Accordingly
the p-adic base field for this local application is K_loc=N.
It is not an identification of the number field K_glob with N,
and no assertion that w is part of completed selected data is
needed for evaluating this field definition. The embedding
F -> K_glob -> N is the retained one. As E_0 and its origin are
defined over Q, base change of X_F along this embedding is exactly
X_loc=(E_0 over N) minus its origin. The original curve in the
field definition is this base X_loc. L053's degree-seven source
and any subsequent level/theta covering are not substituted for it.
This identifies the underlying algebraic curve only; a complete
stable-log object or a native cover of it has not been constructed
in this specialization.

**The same changed parameter.** L048's pointed Q_3-isomorphism
E_0 ≅ E_(q_0) base-changes along Q_3 -> N to a pointed
N-isomorphism of those same equations and origins. Its parameter
is still q_0, with 0<|q_0|_3<1. The named Tate parameter theorem
cited in L048 (Kedlaya, Theorem 2, p.4) applies also over the
finite extension N and characterizes the geometric parameter
uniquely for |j|_3>1. Here j is unchanged under base change and
v_3(j)=-30 by L048, so q_0 is that parameter over N as well.
By the inspected EtTh definition, q_X is the parameter of this
underlying elliptic curve. Hence q_X=q_0. Neither puncturing the
origin nor extending its coefficient field replaces the elliptic
curve by an isogenous one; no parameter of the degree-seven cover
or the old value 3^30 enters this assignment. The absolute
normalization remains v_3(3)=1.

**Substitution into the field definitions.** In characteristic zero,
a primitive second root of unity is zeta_2=-1, which already lies
in N. The root s proved above satisfies s^2=q_0 and belongs to
H subset N; either choice of square root in Omega is s or -s
and is therefore in N. Consequently

(K_loc)_2=K_loc(zeta_2,q_X^(1/2))=N(-1,s)=N.

The imported definition double-dot K_loc=(K_loc)_2 now gives
K_loc=double-dot K_loc=(K_loc)_2. Independently i=zeta_60^15
is in H subset N and has square -1. This fourth root of unity
is not the primitive second root zeta_2; the two predicates have
distinct roles in the source. No enlargement of N, new root
calculation or additional direct lemma input is needed.

**Limit of the conclusion.** The dictionary and substitution pass
the approved test, removing the native local field-equality
ambiguity for the retained base curve. This is an application of
known definitions and the audited root inputs, not new mathematics
beyond the checked sources. EtTh Definition 1.7's separate
non-arithmeticity and curve-type assumptions, Definition 2.5(i)'s
graph factorization and compatible splitting, the local cusp label,
complete selected/theta data, actual input/action, pilot transport,
essentiality and original finite B>=A remain unresolved here.
No full EtTh theorem or complete IUT initial-data verdict follows.
ATTEMPTS/027,030 retain their original stops. The cited author
versions and printed pages are retained; byte identity with the
journal or prior reproduction files is unchecked. The May 2020
qualification excluding the old even-level Remark 2.2.1 remains
in force. The separate critical audit below checks this application,
distinct from the earlier membership audit.

### Separate native field-specialization critical audit — 2026-10-13

**Verdict and scope.** The completed specialization passes under the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-13-retained-native-field-specialization-critical-audit.md`.
This audit checks the last application above, rather than repeating the
root-membership proof as its entire task. It validates evaluation of the
field definitions on the retained underlying curve; it does not supply an
EtTh stable-log object or invoke a native cover or theta theorem. No
mathematical correction, new root calculation or additional direct lemma
input is needed. L045 and L048 remain the direct inputs.

**Induced completion, not a global-field identification.** L045 uses
the places induced by the fixed embedding into Omega. For the same
E_0 supplied by L048, its full level-seven coordinate list S_7 satisfies
K_glob=F(S_7), F_u=H and H(S_7)=N. The absolute value at w is the
restriction of the one on N; its restriction to F is u. In the
embedded-completion statement of Milne, *Algebraic Number Theory*,
v3.08 (19 July 2020),
[section 8 before Proposition 8.1, pp.135–136](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
the extension is finite separable with the chosen extended absolute
value. These hypotheses hold: all coordinate lists are finite, field
characteristic is zero, and the absolute value is precisely the induced
one. L045 verifies the statement's embedded realization: F is dense in
the complete H, K_glob is contained in N, and its closure contains both
H and S_7. Thus its closure contains H(S_7)=N and is contained in N.
This establishes K_w=N for this embedding, rather than an isomorphism
inferred from equal degrees. N/Q_3 is finite by its displayed algebraic
generators. Taking K_loc=N therefore meets the local finite-p-adic-field
condition; it does not assert K_glob=N or a completed selected-place set.

**Original underlying curve and uniqueness over the finite extension.**
The retained embedding restricts to the usual inclusion of Q in Q_3.
The coefficients and origin of E_0 are Q-defined, so the base change
of X_F is exactly E_0 over N with that origin removed. Its underlying
elliptic curve is E_0 over N. Neither the rank-one degree-seven source
nor a level cover occurs in this assignment. L048 applies L045 to the
same reselected curve at the fixed precision M>=max(M_tors,31);
there is no second curve selection in this audit.

Kedlaya, *Introduction: the Tate curve*, fall 2004,
[Theorem 2(a),(b), printed p.4](https://kskedlaya.org/18.727/tate-curve.pdf),
assumes a finite extension of Q_p and |j(E)|>1. Part (a) supplies a
unique nonzero parameter of absolute value less than one giving the
geometric Tate isomorphism; part (b) characterizes an isomorphism over
the base field by split multiplicative reduction. Over Q_3, L048 has
already checked these hypotheses and supplied its pointed isomorphism
with E_(q_0). Extending that isomorphism to N preserves the origin and
the equations. With the extended absolute value, j is unchanged and
v_3(j)=-30, hence |j|>1 also over N. The element q_0 remains nonzero
and has v_3(q_0)=30>0. It is therefore an eligible parameter for the
same geometric isomorphism over N, and uniqueness in part (a) identifies
it with the parameter defined there. No new split-reduction proof is
needed over N because an N-defined pointed Tate isomorphism is already
obtained by base change.

EtTh's inspected opening convention and field definitions, December
2008 author PDF,
[printed pp.10,12,16](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
take q_X from the elliptic curve underlying original X. IUT I, May
2020 author PDF,
[Definition 3.1(e), printed p.63](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
uses the local base change of X_F. These clauses match the assignment
above, so evaluating this field definition gives q_X=q_0. This use of
the underlying curve does not certify the separate stable-log hypotheses
in EtTh's opening setup. The parameter is the changed q_0, not the old
3^30; the valuation remains absolute, with v_3(3)=1.

**Unindexed equality and the independent fourth root.** The cited
definitions give K_n=K(zeta_n,q_X^(1/n)), double-dot K_n=K_(2n),
and double-dot K=double-dot K_1=K_2. At n=2, a primitive zeta_2
is -1 in this characteristic-zero field and already lies in N.
The separately audited root membership gives s in H subset N with
s^2=q_0; the only choices in Omega are s and -s, both in N.
Substitution therefore gives (K_loc)_2=N(-1,s)=N, and the unindexed
definition gives K_loc=double-dot K_loc=(K_loc)_2. This asserts no
equality at all higher levels and no equality of the associated covers.

The separate Theorem 1.10 hypothesis, EtTh printed pp.27–28, asks for
sqrt(-1) in the base field. Its verified witness i=zeta_60^15 lies
in H subset N with i^2=-1. It has order four and is distinct from
zeta_2 of order two. Neither predicate is silently substituted for
the other. The full hypotheses of that theorem are not inferred.

**Limits and decision.** All approved dictionary and substitution
tests pass, using known definitions, the cited completion and Tate
theorems, and the previously audited roots. This establishes a usable
local field prerequisite, not mathematics beyond the checked sources
or a candidate demonstration of an IUT flaw. Stable-log construction,
native graph factorization and label, compatible splitting, complete
selected/theta data, actual input/action, pilot transport, essentiality
and original finite B>=A remain unresolved. ATTEMPTS/027,030 and the
December 2008/May 2020 version, unchecked byte-identity and even-level
correction qualifications are retained. No script or numerical
certificate is appropriate for this theorem-application audit. Full
matching Mathlib coverage remains unchecked, not asserted absent.

## Mathlib

Full matching coverage of this retained-field specialization, its
native field-definition application and Tate uniformization has not
been checked in Mathlib. No absence
claim is made. The canonical proof imports the precisely cited known
theorems and supplies their elementary applicability calculations.
No mathematical script or numerical certificate is required.
