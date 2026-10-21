# L043 — Exact Tate curve excluded from geometric number-field realization

## Hypotheses

Let C_3 be the completion of the fixed algebraic closure of Q_3 in
L042, with |3|_3=1/3. Retain L042's H=Q_3(zeta_60), q=3^30 and
standard untwisted split Tate curve E_q/H, and extend this curve to C_3.
A proposed realization consists of a number field F, a field embedding
iota:F -> C_3, and an elliptic curve E/F, with an isomorphism of elliptic
curves E tensor_(F,iota) C_3 congruent to E_q tensor_H C_3 over C_3.

## Conclusion

j(E_q) is transcendental over Q. No proposed realization with these
hypotheses exists, even after geometric base extension to C_3.
This stops globalization of this exact curve only. It does not exclude
a different curve having an isomorphic local torsion coordinate field,
or demonstrate an essential IUT flaw. The conclusion is a known-theorem
application, not a new transcendence result. The separate 2026-10-11
critical audit below validates this exact exclusion.

## Proof

### Imported theorem and normalization

Import the p-adic Mahler–Manin theorem in M. Waldschmidt,
*Transcendance et indépendance algébrique de valeurs de fonctions
modulaires*, CNTA5 Carleton, August 1996, 23-page author version,
[Theorem 1, p.2](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/CNTA5.pdf).
On pp.1–2 its field C is either the complex field or C_p. For
0<|q|<1, the theorem states that q and J(q) cannot both be algebraic
over Q. Here J=Q^3/Delta, Delta=(Q^3-R^2)/1728, with Q and R the
normalized weight-four and weight-six Eisenstein series: this is the
full series J(q)=q^(-1)+744+196884q+..., not j/1728, a truncation or
the leading term alone. The saved literature assessment inspected the
proof on pp.3–8, including the explicit p-adic cases on pp.7–8.
No reproof of this theorem is needed or claimed.

The original result is K. Barré-Sirieix, G. Diaz, F. Gramain and
G. Philibert, *Une preuve de la conjecture de Mahler-Manin*,
Inventiones mathematicae 124 (1996), 1–9,
[DOI 10.1007/s002220050044](https://link.springer.com/article/10.1007/s002220050044).
Its original proof was not inspected. The imported statement is also
confirmed by the inspected coauthor restatement F. Gramain,
*Transcendance et fonctions modulaires*, JTNB 11(1) (1999),
[pp.73–74](https://www.numdam.org/item/JTNB_1999__11_1_73_0.pdf),
which explicitly includes the p-adic analogue. Its subsequent complex
exposition is not used as a p-adic proof.

For the standard Tate curve import J.S. Milne, *Elliptic Curves*,
second edition (2021), III.3, equations (24)–(26),
[pp.102–103](https://www.jmilne.org/math/Books/EC2.pdf).
These identify j(E_q) with the same full modular series J(q), with
identities valid p-adically, in particular for this rational parameter.
Milne II.2.1(c), pp.50–51, gives j-invariance under geometric
isomorphism in characteristic different from 2 and 3. These standard
facts and the transcendence theorem have ready source coverage in
drafts/literature/2026-10-10-exact-tate-curve-number-field-exclusion.md.

### Exact specialization and contradiction

L042 specifies the exact parameter q=3^30 and the standard curve;
none of its torsion-field degree calculations is needed here.
The parameter is a nonzero rational number, hence algebraic over Q,
and in C_3 satisfies |q|_3=3^(-30), strictly between zero and one.
Every hypothesis of the imported p-adic theorem holds. Thus J(q)
is transcendental over Q. The Tate identity gives j(E_q)=J(q),
so j(E_q) is transcendental over Q as asserted.

Suppose the proposed realization exists. In characteristic zero E
admits a short Weierstrass equation y^2=x^3+Ax+B over F with
4A^3+27B^2 nonzero. Its invariant
j(E)=1728*4A^3/(4A^3+27B^2) belongs to F (Milne II.2.1).
Base extension gives j(E tensor_(F,iota) C_3)=iota(j(E)).
Every field embedding of number fields into C_3 fixes Q: it fixes
1, hence integers and rational inverses. A nonzero polynomial over
Q annihilating j(E) therefore also annihilates iota(j(E)). This
value is algebraic over Q, regardless of the particular embedding.
Geometric isomorphism and j-invariance now give
iota(j(E))=j(E_q)=J(3^30), contradicting its transcendence.
Consequently no such F, embedding and curve exist.

### Scope and remaining gaps

Algebraicity here is over Q, not over Q_3. The j-value belongs to
H (indeed Q_3), which is fully consistent with transcendence over Q.
No assertion that a local curve automatically descends to a number
field was used. Geometric isomorphism is enough for the contradiction;
a twist cannot remove it because it retains the same j-value.
The exact rational q has been kept fixed, rather than replaced by
a nearby parameter. A local field isomorphism fixing Q_3 also fixes
this q and the j-value in Q_3.

L042's local full-torsion and degree pass remains valid. A different
curve sharing its local torsion field is outside this argument.
Global F/F_0 and degree conditions, global full 30-torsion,
selected places, native/actual input and action, marked pilot transport,
essentiality and the original finite B>=A comparison remain unresolved.

### Separate critical audit — 2026-10-11

The unchanged IMPORT assessment authorizes this application audit.
Waldschmidt's Theorem 1, p.2, explicitly uses the field convention
C=C_p from p.1. Its conclusion concerns transcendence over Q, not
over Q_p. With p=3, the exact nonzero rational q has norm 3^(-30)<1;
the alternative that q itself is transcendental is therefore excluded.
Neither algebraicity of the Tate coefficients nor any global model
is a premise of this theorem. The previously inspected proof coverage
is reused; the original Inventiones proof is still not claimed read.

The full normalization can be checked without extrapolating from
three initial coefficients. Milne III.3 (24) writes
b2(q)=5 sum_(n>=1) n^3 q^n/(1-q^n). Thus 1+48b2(q) is exactly
Waldschmidt's Q(q), defined on p.2. Milne (25)-(26) gives
j(E_q)=(1+48b2(q))^3/[q product_(n>=1)(1-q^n)^24].
Waldschmidt p.3 identifies that same product with his Delta, so
the ratio is his full Q(q)^3/Delta(q)=J(q). Milne p.103 explicitly
retains these identities for q in Q_p with |q|<1, which suffices
here before base extension to H and C_3. The denominator is nonzero:
the imported discriminant formula belongs to the nonsingular Tate
curve. This check uses the standard coefficients of (23)-(24), not
the differing handout coefficient noted in L042. The primary
formulas and Theorem 1 were checked directly again for this audit;
no new transcendence theorem or analytic continuation is invoked.

For a proposed E/F, characteristic zero is the hypothesis needed
by Milne II.2.1; residue characteristic 3 does not violate it.
Nonsingularity makes the displayed denominator of j(E) nonzero,
so an embedding preserves both the rational expression and its
definedness. Every embedding fixes Q, hence carries a nonzero
annihilating polynomial over Q to that same polynomial. Consequently
iota(j(E)) is algebraic over Q even if iota is not chosen through
any specified place of F. The supposed C_3-isomorphism identifies
this value with J(3^30), contradicting Theorem 1. No continuity
assumption on iota, converse classification by j, or choice of twist
is required.

The audit passes the exclusion as stated. Its only local lemma input
is L042's identification of the parameter and standard curve; the
coordinate-field degrees are not used to infer transcendence.
Membership of J(3^30) in Q_3 is compatible with the conclusion.
Changing the curve while preserving finite torsion data is outside
the isomorphism hypothesis, so this proof supplies no obstruction
to that different problem. ATTEMPTS/027 is accepted only for exact
curve globalization. No original IUT hypothesis is contradicted,
and the original finite B>=A gap remains open.

## Mathlib

Full matching coverage of p-adic Mahler–Manin transcendence and this
geometric realization exclusion has not been checked in Mathlib.
No absence claim is made. The named mathematical sources above are
the imported inputs; no Mathlib theorem is needed for this application.
