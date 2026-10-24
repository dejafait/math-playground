# L111 — Local base-field predicate at every selected completion

## Hypotheses

Retain L107,L109,L110's same member, ordering o, prime ell>=7,
literal curve and fields in their fixed algebraic closure:

    E_o: V^2=X(X-1)(X-t_o),  t_o!=0,1,
    G_o=Q(t_o)(iota,E_o[15]),  iota^2=-1,
    G_o subset C_o subset K_C=C_o(E_o[ell]).

The division fields use both coordinates of the complete torsion.
Keep the one fixed U, complementary psi and L108's section s.
For each p in Sigma=S minus {ell}, where
S={p:v_p(j(E_o))<0}, use the actual completion embedding
i_w:K_C -> k=(K_C)_w, w=s(p). Such p is odd and distinct from ell.
L109 supplies q_w in this k, 0<|q_w|<1, and a pointed
k-isomorphism f_w:E_(q_w) -> (E_o)_k. L110 supplies the original
stable formal log one-gon with this specified pointed generic fiber.

Interpret the local field definitions in Mochizuki's published EtTh
(PRIMS 45 (2009)), section 1, and only the field portions of its
Theorem 1.10 and Definition 2.5(i). The inherited IUT reproduction,
authentication and def= qualifications remain. No complete initial
theta-data, III situation, common cusp sign or compatible splitting
is a premise. No old completion N or old parameter q_0 is used.

## Conclusion

For every p in Sigma and its unchanged k=(K_C)_(s(p)), the original
curve's EtTh parameter is q_X=q_w and there exist a_w,b_w in k with

    a_w^2=q_w,   b_w^2=-1.

For either choice of these roots in an algebraic closure of k,

    k_2=k(zeta_2,q_X^(1/2))=k,
    k=double-dot k=k_2,    k(sqrt(-1))=k.

These are the unindexed field predicate and the separate square-root-
of-minus-one membership, at every already selected completion. They
do not assert equality of all indexed radical fields, identify a native
marking, or establish all hypotheses of either cited EtTh result.
Together with L110 they supply only independent field and graph
prerequisites. Common sign/splitting, independent native data/III/P7,
exact generation/full repair and relative factor-four excess, actual
input/action/factorization/pilot, essentiality and original finite B>=A
remain unresolved. The separate step451 critical audit below validates
this specialization; no complete candidate or progress beyond the
checked known methods is claimed.

## Proof

### Imported results, duplicate screen and bounded test

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-selected-completion-base-field-predicate.md`.
Its source comparison covers these arbitrary finite p-adic bases and
these changed objects. L054 is a duplicate method on different objects,
not a root-membership input. The targeted recorded failures in
ATTEMPTS/029,030,031,034,035 remain in their original scopes; this
argument neither retries authentication nor assumes a marked covering
coordinate. Import the following results and definitions:

- Tate uniformization, in Kedlaya, [*Introduction: the Tate curve*,
  fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf), Theorem 1
  and its finite-extension clause, p.3, with the proof discussion
  pp.3–4; Theorem 2, p.4. These give the group isomorphism
  E_q(k)=k^times/q^Z for q in the finite p-adic base with 0<|q|<1,
  as well as uniqueness of the small geometric parameter. The cited
  underlying references are Silverman, *Advanced Topics in the
  Arithmetic of Elliptic Curves*, V.3.1/V.4 and V.5.3. Import the
  theorem, including same-field surjectivity; do not infer it by
  taking fixed points of a geometric quotient. No coefficient display,
  inertia claim or coprimality hypothesis from Proposition 3 is used.
- Milne, [*Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
  II.6 Proposition 6.3, pp.70–71: geometric n-torsion is a rank-two
  Z/n-module when n is prime to field characteristic. Here n=2 and
  the field characteristic is zero, regardless of residue characteristic.
- Mochizuki, [*The Etale Theta Function and its Frobenioid-theoretic
  Manifestations*, PRIMS 45 (2009), 227–349](https://ems.press/content/serial-article-files/41069?nt=1),
  section 1 opening p.237 and parameter/field definitions p.239,
  double-dot definitions p.243, Theorem 1.10 pp.255–256, and
  Definition 2.5(i) p.265. For the original underlying elliptic
  curve's parameter q_X the definitions are

      k_n=k(zeta_n,q_X^(1/n)),
      double-dot k_n=k_(2n),
      double-dot k=double-dot k_1=k_2.

  Theorem 1.10 separately assumes sqrt(-1) in the base field.
  Definition 2.5(i) has other graph and splitting requirements;
  the displayed field formulas do not imply those requirements.
  The retained reading of IUT I, May 2020, Definition 3.1(e), p.63,
  uses the original base curve and attributes this field condition
  to rational 2-torsion. The published EtTh definitions suffice here;
  no fresh IUT source authentication is asserted.

The main gap remains original finite B>=A. The bounded test is to
verify full 2-torsion, same-field representatives and the original
parameter assignment at every actual selected completion, then check
iota independently. Failure of any premise would require withholding
the universal assertion. Passing can support only the independent
local field prerequisite for later clause-(e) work; no uniformization
reproof or new field adjunction is needed.

### Full 2-torsion of the literal curve in each actual field

Fix any p in Sigma, w=s(p) and k=(K_C)_w. This is a finite
extension of Q_p because K_C is a number field. Put t=i_w(t_o).
The completion embedding is injective, so t!=0,1. The equation of
(E_o)_k is exactly V^2=X(X-1)(X-t). On this Weierstrass equation
the inverse of an affine point (X,V) is (X,-V). Consequently

    O, (0,0), (1,0), (t,0)

are four distinct k-rational points killed by two: the three affine
points are fixed by inversion, and O is the group identity. Milne's
cited theorem gives exactly four geometric 2-torsion points in
characteristic zero. Thus these exhaust the geometric 2-torsion and
E_o(k)[2] has order four. This uses the literal Legendre equation;
odd 15-torsion rationality alone would not imply this conclusion.
The inverse of L109's pointed k-isomorphism preserves the group law
and carries all four points to E_(q_w)(k)[2].

### Same-field representatives force the square root

Write q=q_w. The imported Tate theorem applies over this actual k,
since q is in k and 0<|q|<1. Hence the four rational 2-torsion
points correspond to four classes in k^times/q^Z. A class [z],
with z in k^times, is killed by two precisely when

    z^2=q^m   for some integer m.

Such m is unique, since |q|<1 implies q has infinite order.
Replacing z by zq^a changes m to m+2a, so parity of m is
well-defined on a class. If m=2r, then (zq^(-r))^2=1.
The field has characteristic zero, so zq^(-r)=1 or -1, and
[z] is [1] or [-1]. Conversely these two classes have even
exponent and are killed by two. They are distinct: an equality
would give -1=q^a, whose absolute value forces a=0, then -1=1,
a contradiction. Thus precisely two classes have even exponent.

There are four classes in total, so an odd class exists. Take its
same-field representative z in k^times and write m=2r+1. Then

    a_w=zq^(-r) in k^times,    a_w^2=q.

The integer r may be negative; only integral powers of the nonzero
q already in k were used. No Galois-fixed geometric class was
presumed to have a fixed representative: that representative is
supplied by the imported same-field surjectivity. Both roots of
T^2-q in the algebraic closure are a_w and -a_w and belong to k.

### Original parameter and the unindexed field equality

In L110 the original pointed model is C=T_1(q_w), completed with
its fixed log structure. Its generic fiber is E_(q_w), identified
by f_w with (E_o)_k; the original punctured curve removes its
origin. Thus EtTh's original curve is this once-punctured base
curve, whose underlying elliptic curve is (E_o)_k. L109's unique
small geometric Tate parameter for that elliptic curve is q_w.
Accordingly q_X=q_w. In particular the complementary source
B_k, represented in L110 by the generic fiber E_(q_w^ell) of
D=T_ell(q_w), does not replace this original base curve.

Since zeta_2=-1 is already in the characteristic-zero field k,
and either square root of q_X=q_w is in k by the preceding
argument, substitution into the cited definitions gives

    k_2=k(-1,a_w)=k,
    double-dot k=double-dot k_1=k_2=k.

This uses exactly the unindexed equality. It does not assert
k_n=k for every n or identify any theta covering or splitting.

### Separate embedding of the square root of minus one

By the fixed full-coordinate field prescription,
iota belongs to G_o subset C_o subset K_C and satisfies
iota^2=-1. Under the same completion embedding put
b_w=i_w(iota). A unital field embedding preserves the equation,
so b_w^2=-1 in k. Its two roots b_w,-b_w both belong to k;
therefore k(sqrt(-1))=k for either root choice. This membership
uses iota, independently of the fact zeta_2=-1 in the preceding
field formula; the latter alone would supply no square root of -1.

The place p was arbitrary in the already fixed Sigma. Each proof
uses its own q_w and actual completion embedding, with no need to
choose a common root, common local parameter or new section. Thus
every selected completion satisfies both advertised field tests.
No enlargement of k or K_C, change of U, downstairs splitness,
ell-integrality or normality of K_C/Q enters the proof. The local
field prerequisite is now proved by the checked known methods;
the independent gaps listed in the conclusion remain open.

### Separate critical audit — 2026-10-24, step451

**Scope and source use.** This is the REPRODUCTION audit authorized by
the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-selected-completion-field-predicate-critical-audit.md`.
The complete proof above is checked against L107's literal equation and
field prescription, L109's same-field comparison and step443 audit,
and L110's original-model construction and step447 audit. L108 fixes
the actual section and inherited objects. Reuse the inspected primary
theorem statements and cases recorded in the source comparison: Tate
uniformization over the finite p-adic base itself, Milne II.6.3 in
field characteristic zero, and EtTh's original-curve parameter and
unindexed field definitions at the precise locations cited above.
No fresh source retrieval, source authentication or uniformization
reproof is claimed. L054's result on the old N is not an input.

**Literal curve and full torsion.** For each arbitrary p in Sigma,
K_C is the same finite number field, so k=(K_C)_(s(p)) is a finite
extension of Q_p and its completion map is injective. L107's literal
parameter has t_o!=0,1, and these inequalities persist in k. The
Legendre cubic is nonsingular: its three finite roots are distinct,
and its projective origin is smooth. The inverse formula on this
equation is (X,V) -> (X,-V). Thus the displayed three distinct
affine points and O are killed by two. Milne's geometric torsion
cardinality theorem applies to n=2 in characteristic zero and gives
exactly four points, so none is missing. The inverse of f_w, not f_w
in its displayed direction, transports these points from E_o to E_q.
The proof's wording now makes this direction explicit. It changes no
claim or hypothesis and uses neither rational odd torsion nor any
old-curve 2-torsion assertion as a substitute for this check.

**Same-field representatives and all exponent cases.** L109 constructs
q=q_w in this very k, with 0<|q|<1, and descends the pointed
comparison over k. Its character argument uses full local ell-torsion
and the nonzero exponent quotient; it does not assume splitness over
C_o or a rational radical. Consequently the same-field part of the
imported Tate theorem applies before any representative is selected.
It is a group isomorphism k^times/q^Z -> E_q(k), so there are exactly
four killed-by-two classes in this quotient. For every representative
z of any such class there is a unique integer m with z^2=q^m:
membership in the kernel gives existence and |q|<1 gives uniqueness.
Every alternative representative is zq^a with a in Z, changing m
by 2a. This covers positive, zero and negative exponents.

If m is even, division by q^(m/2), an element of k^times, puts z
at +1 or -1. These yield two different classes, since -1=q^a
would force a=0 by absolute values and then contradict characteristic
zero. Conversely each has even exponent, so there are exactly two
even classes. Of the four total classes, the remaining two are odd;
one suffices. For m=2r+1 the element zq^(-r) squares to q in k.
No limiting step, valuation-parity substitute or inference from fixed
geometric classes to fixed representatives is used. The complete
root set is {a_w,-a_w}, both in k; changing representative cannot
alter this membership conclusion.

**Original object and exact field definition.** L110 constructs
C=T_1(q_w) over O_k with generic fiber E_(q_w), specified pointed
comparison f_w to E_o, smooth origin marking and stable split nodal
special fiber. Its tautological fs log and formal completion satisfy
EtTh section 1's hypotheses by the construction and separate audit
there. Puncturing removes this origin. The underlying elliptic curve
of the original X is therefore E_o over k; uniqueness of its small
geometric Tate parameter gives q_X=q_w. The complementary source
D=T_ell(q_w), with generic parameter q_w^ell, is a different
object and does not supply q_X. Neither a change of pointed
comparison by inversion nor the log completion changes this parameter.
The graph-kernel conclusion itself is not used to infer root membership.

EtTh defines double-dot k=double-dot k_1=k_2 and
k_2=k(zeta_2,q_X^(1/2)). Here zeta_2=-1 belongs to k and both
choices of q_X^(1/2) belong to k by the previous calculation.
Substitution proves precisely k=double-dot k=k_2. This does not
assert k=k_n for every n, equality of the corresponding covers,
standard theta type or a compatible splitting.

**Separate iota and universal quantifier.** The actual inclusions
G_o subset C_o subset K_C place the specified iota in K_C before
completion. Its image b_w under the same injective unital field map
satisfies b_w^2=-1. Characteristic zero gives the two roots b_w,-b_w,
both in k, proving the separate membership for either root choice.
The element -1 used as zeta_2 would not alone prove this assertion.
All arguments apply to arbitrary p in the already fixed Sigma with
its own q_w and completion embedding. They require no uniform root
choice, new section, global square root of q_w, change of U or field
extension. L108 supplies odd p distinct from ell as required by the
native context; no ell-integrality or K_C/Q normality is introduced.

**Verdict.** L111 passes this separate critical audit with the same
hypotheses, conclusion and direct inputs L107,L109,L110. The only
clarification is the direction of the pointed isomorphism used to
transport torsion. This validates the independent local field
prerequisite by previously checked methods; it is not a new theorem
beyond those sources or a demonstrated IUT flaw. This canonical
verdict supersedes the pending-audit wording for L111 in the unchanged
overview. Common cusp sign, compatible theta splitting, independent
initial-data/III/P7, exact generation/full repair, the relative
factor-four excess, actual input/action/factorization/pilot, inherited
authentication/def= qualifications, essentiality and original finite
B>=A remain unresolved. There is no complete candidate.

## Mathlib

Full matching Mathlib coverage of the same-field Tate uniformization,
this stable-log/original-curve dictionary and EtTh field predicate is
unchecked. The characteristic-zero torsion and explicit inversion
facts are supporting mathematics, not a claim of a formalized proof
of this complete specialization. No mathematical script or numerical
certificate is needed for this exact four-point and parity argument.
The separate step451 informal audit adds no Mathlib coverage or formal
verification claim.
