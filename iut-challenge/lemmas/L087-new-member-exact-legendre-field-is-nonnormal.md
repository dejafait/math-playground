# L087 — A new-member exact Legendre field retains H,N and is nonnormal

## Hypotheses

Choose one member E=E_star/Q supplied by audited L086, once and for
the whole argument. Retain its original monic integer equation

    y^2=g(x)=x^3+c x^2+d x+e,

the fixed algebraic closure Omega of Q_3 and its subfield Q-bar of
elements algebraic over Q, and the specified roots of unity defining

    H=Q_3(zeta_60), N=Q_3(zeta_420,3^(1/7)).

L086 gives full mod-120 and mod-seven images over Q, full H-rational
30-torsion, H(E[7])=N, and split multiplicative reduction of this
original model with its own parameter q_star of valuation 30. All
global fields below are subfields of this Q-bar; places are induced
by its inclusion in Omega. Division fields always use both coordinates
of every geometric torsion point, not only x-coordinates or a cyclic
subgroup. No old witness or its fields are identified with E.

## Conclusion

The roots can be ordered r_1,r_2,r_3 with respective residues -1,0,0
in H. For this ordering there is an actual s in H with

    D=r_2-r_1=s^2, t=(r_3-r_1)/D,
    E_L: V^2=X(X-1)(X-t), iota=zeta_60^15.

The resulting exactly specified number field

    G_star=Q(t)(iota,E_L[15])

satisfies, at the induced places u,w,

    Q(t)=Q(r_1,r_2,r_3)=Q(E[2]),
    (G_star)_u=H, (G_star(E_L[7]))_w=N,
    [G_star^nor:G_star]=4.

Here G_star^nor is its normal closure over Q in the fixed closure.
Thus G_star/Q is nonnormal, against the normality threshold one.
The assertion holds for either sign of the chosen s. It supplies a
nonvacuous new-member instance of L085's assessed mechanism, not a
verdict about the old G. The separate step345 critical audit below validates this specialization.
It establishes neither an essential IUT flaw nor finite B>=A.

## Proof

### Imported inputs and exact scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-19-new-member-exact-legendre-field-application.md`.
L086 is the occurrence and local-retention input; L085 supplies the
audited finite-group method. L085's fixed-witness conclusion is not
applied by renaming its fields. The intervening hypotheses and the
complete stabilizers are established below for this E.

Import the following general results without reproof, at the versions
and locations inspected in that assessment:

- Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
  [Proposition 7.31, pp.119–120; section 8 and Propositions 8.1–8.2,
  pp.135–136](https://www.jmilne.org/math/CourseNotes/ANT.pdf): simple-root
  Hensel over a complete DVR, and the induced completion identity
  for finite separable adjunctions A(alpha), namely A-hat(alpha)
  with the chosen root image. The latter iterates over finite lists.
- Milne, *Elliptic Curves*, second edition (2021),
  [II Theorem 2.4(b), pp.52–53](https://www.jmilne.org/math/Books/EC2.pdf):
  pointed Weierstrass changes and group-law compatibility.
- Silverman, *The Arithmetic of Elliptic Curves*, second edition
  (2009), [III Proposition 8.1(c,d) and Corollary 8.1.1,
  pp.94–96](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf),
  and Milne, *Fields and Galois Theory*, v5.10 (September 2022),
  [Proposition 5.8, pp.64–65](https://www.jmilne.org/math/CourseNotes/FT.pdf):
  full rational m-torsion in characteristic prime to m supplies all
  m-th roots of unity, and these form a cyclic group.
- Antieau–Meier, [arXiv:1608.00851v3 (5 May 2020), Proposition 4.5
  and Corollary 4.6, pp.14–15](https://arxiv.org/pdf/1608.00851v3):
  over an algebraically closed field of characteristic different from
  two, the ordered full two-torsion parameter is
  (r_3-r_1)/(r_2-r_1), and equal parameters give an isomorphism of
  the ordered objects. The Legendre section's nonequivariance is
  retained; the application is geometric, not a descent assertion.
  Use also the nonexceptional-j automorphism classification in
  [Sutherland, Lecture 21 (6 May 2024), section 21.2,
  p.2](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf).
- Yelton, [arXiv:1704.06190v2 (2 August 2017), degree-three setup
  and Theorem 1(a), pp.1–2; Lemma 3, pp.2–3](https://arxiv.org/pdf/1704.06190v2):
  for an arbitrary monic separable cubic in characteristic different
  from two, its full four-division field is generated over its root
  field by iota and the three cyclic difference radicals. The
  general specialization theorem, not generic radical independence,
  is used.
- Determinant/cyclotomic compatibility in [Zywina, *Elliptic curves
  with maximal Galois action on their torsion points*, section 1.1,
  pp.1–2](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
  the full-coordinate twist formula in [Gonzalez-Jimenez–Lozano-Robledo–York,
  arXiv:2408.04159v1, Lemma 3.4 proof,
  pp.12–13](https://arxiv.org/pdf/2408.04159v1), and
  [Milne FT, Theorem 3.17(b–d), Remark 3.18,
  pp.39–40](https://www.jmilne.org/math/CourseNotes/FT.pdf).
  Only the twist action formula is imported, not the twist paper's
  stronger field-equality claim. Its short-equation convention is
  available by x-translation in characteristic zero. The formula is
  also checked directly on the actual coordinates below.

These known results cover the general mechanisms. The purpose of the
following proof is their same-member application, with no transfer of
independent global hypotheses from the old construction.

### Actual roots and the cross-residue choice

L086's original-model congruences and its audited invariant calculation
give c=1,d=e=0 modulo 3, unit c4 and v_3(Delta)=30. In particular
g is separable and v_3(j(E))=-30. Every (r_m,0) is a nonzero
two-torsion point, so full H-rational 30-torsion places all roots in
H. Since g is monic integral they are integral: if v_3(r)<0,
r^3 has strictly smaller valuation than every other nonzero term of
g(r), preventing their sum from being zero. Reducing its full split
factorization in the residue field k_H gives

    product_m (X-bar(r_m))=X^2(X+1).

Thus exactly one actual root has residue -1 and two have residue 0.
Order them as in the conclusion. D is a nonzero unit with residue 1.
The polynomial Z^2-D over the complete DVR O_H has simple residue
root 1, since its derivative is 2 in characteristic three. Hensel's
theorem supplies s in O_H with s^2=D. It is a unit and is algebraic
over Q, because D is; hence it lies in our Q-bar. Either sign lies
in H and is nonzero. No double root of the reduced cubic was lifted.
Distinctness also gives t!=0,1.

### Full pointed coordinate maps and the exact global field

Set F_star=Q(zeta_60,E[30]) and F'_star=F_star(s). These are
number fields inside H, since L086 puts every indicated coordinate
and the chosen s in H. Their embedded completions are H: each
contains Q(zeta_60), whose completion is H, and the completion
theorem adjoins only further elements already in H.

All roots, D and t belong to F_star. The actual maps are

    phi(x,y)=((x-r_1)/D,y/(Ds)),
    phi^(-1)(X,V)=(r_1+DX,Ds V).

Substitution gives g(r_1+DX)=D^3 X(X-1)(X-t) and (Ds)^2=D^3.
On projective cubics these maps are the invertible linear changes

    [x:y:z] -> [(x-r_1 z)/D:y/(Ds):z],
    [X:V:Z] -> [r_1 Z+DX:Ds V:Z].

Their composites are identities, and they fix [0:1:0]. The cited
pointed theorem (u=s, translation r_1) makes them group isomorphisms
over F'_star and over H. Consequently they biject the entire
geometric n-torsion sets for each n, including 15 and seven.
In particular all E_L[15] coordinates lie in F'_star: apply phi
to every F_star-rational E[15] point; the inverse proves exhaustion.
The origins are rational. Hence the literal G_star in the conclusion
is a number field with

    Q(t) subset G_star subset F'_star subset H,

and E_L has full G_star-rational 15-torsion by definition. The maps
need not be defined over G_star. Changing s to -s composes phi
with inversion and changes neither E_L nor any full coordinate field.

### Coefficient field equals the root field

Write K=Q(r_1,r_2,r_3). An automorphism sigma of Q-bar/Q fixing
all roots fixes t. Conversely suppose sigma(t)=t. The ordered
objects (E;(r_1,0),(r_2,0),(r_3,0)) and
(E;(sigma(r_1),0),(sigma(r_2),0),(sigma(r_3),0)) have that same
geometric full-level-two parameter. Antieau–Meier therefore gives
a pointed automorphism of the same Q-defined E carrying the first
ordering to the second. Here j(E)!=0,1728: its valuation is -30,
whereas v_3(1728)=3. Thus its pointed automorphisms are exactly
{+1,-1}. Both fix every two-torsion point, so sigma fixes all roots.
Since K/Q is the finite Galois splitting field of g and t lies in K,
apply this argument to each element of Gal(K/Q), extended to Q-bar.
The stabilizer of t in Gal(K/Q) is trivial. The cited finite Galois
correspondence therefore gives

    Q(t)=K=Q(E[2])

as embedded fields. The comparison takes place over Q-bar; no
rational equivariance of a Legendre section or rational isomorphism
over K has been assumed. Only this coefficient/root-field statement,
not a new native moduli claim, is needed here.

### Both required completions

Apply the Weil-pairing corollary to E_L/G_star at m=15 in field
characteristic zero. It puts all mu_15 in G_star, including the
specified alpha=zeta_60^4. Also iota=zeta_60^15 is a defining
generator of G_star. The identity alpha^4/iota=zeta_60 proves
Q(zeta_60) subset G_star in this embedding. Let S_15 be the full
finite list of affine E_L[15] coordinates. Then

    G_star=Q(zeta_60)(t,S_15).

Every entry of the list and t is in H by the earlier upper inclusion.
Successive finite separable adjunctions at the induced place give
(G_star)_u=H(t,S_15)=H. The lower cyclotomic inclusion is essential;
an upper inclusion in H alone would not establish this equality.

Both phi and phi^(-1) have all coefficients in H. The forward map
sends all E[7] coordinates into H(E[7]) and covers E_L[7], proving
H(E_L[7]) subset H(E[7]). Its inverse sends all E_L[7] coordinates
into H(E_L[7]) and covers E[7], proving the reverse inclusion.
Therefore L086 gives H(E_L[7])=H(E[7])=N as actual subfields of
Omega. With S_7 the complete finite coordinate list of E_L[7],
the same induced completion theorem gives separately

    (G_star(E_L[7]))_w=(G_star)_u(S_7)=H(E_L[7])=N.

The global and local torsion lists agree: the same characteristic-zero
division scheme is finite etale over Q(t), so all its geometric points
are already algebraic over that number field and lie in our Q-bar.
These two equalities do not use global normality or degree comparisons.

### Establish the new member's full ambient group

Choose A=s, B^2=r_3-r_1 and C^2=r_3-r_2 in Q-bar. Put

    k=K(zeta_60), M_star=F_star(A,B,C).

All signed difference radicals lie in this field, since iota is in
F_star. Yelton's general formula applies to the monic separable g
and gives Q(E[4])=K(iota,A,B,C), with signed cyclic differences
converted by iota. Consequently M_star=F_star Q(E[4])=Q(E[60]).
For the last equality, all displayed generators lie in Q(E[60]),
including zeta_60 by the Weil pairing; conversely, for P in E[60],
[45]P is in E[4], [16]P is in E[15], and their sum is P.
The Q-defined group law therefore places both coordinates of all
E[60] in M_star. The same argument at level 30, using 15+16=31,
gives F_star=k(E[15]). M_star is finite Galois over Q, being
the full division field of the Q-defined curve.

L086's one joint level-120 image, CRT and the surjection from
GL_2(Z/8Z) to GL_2(Z/4Z) yield the actual group

    Gal(M_star/Q)=GL_2(Z/4Z) x GL_2(Z/15Z).

Surjectivity of reduction follows by lifting entries: a lift of an
invertible mod-four matrix still has odd determinant. These are joint
restrictions, not a product inferred from separate marginal images.
In compatible bases write an element (a,b). Fixing K is exactly
a=Id modulo two. Fixing zeta_60 is exactly det(a)=1 modulo four
and det(b)=1 modulo 15 by cyclotomic determinant compatibility.
Thus the full subgroup fixing k is

    U=P_4 x SL_2(Z/15Z),
    P_4={Id+2X:X in M_2(F_2),tr(X)=0}.

P_4 is elementary abelian of order eight: multiplication adds X,
and det(Id+2X)=1+2tr(X) modulo four. Each a fixes the roots and
iota, so its three radical signs define characters chi_A,chi_B,chi_C.
If all signs are positive, it fixes every generator of Q(E[4])
and is the identity on E[4]. Hence the sign map from P_4 to
{+1,-1}^3 is injective and, by the equal orders, bijective. All
eight sign patterns occur jointly with every allowed b. This is the
needed specialized independence; generic independence and the single
89-Frobenius play no role in obtaining it.

### Complete stabilizers and the exact normal-closure index

For each ordered tuple o=(a,b,c) of distinct root indices let
D_o=r_b-r_a, t_o=(r_c-r_a)/D_o, s_o^2=D_o, and
G_o=K(iota,E_o[15]), with literal E_o:V^2=X(X-1)(X-t_o).
Each s_o can be chosen among plus or minus A,B,C and their iota
multiples, so all corresponding pointed maps are defined over M_star.
They put all G_o inside M_star. Pairing at level 15 and the same
cyclotomic identity put k inside every G_o. Thus no pointwise
stabilizer of a G_o in Gal(M_star/Q) lies outside U.

For h=(a,b) in U the actual phi_o coordinate formula, in its
transported torsion basis, is

    rho_o(h)=chi_o(a)b, chi_o(a)=h(s_o)/s_o.

Indeed h fixes r_a,D_o and multiplies the y-denominator by that
sign; inverse signs are equal, and inversion is scalar -Id on
the full 15-torsion. This verifies the imported twist formula on
all coordinates. Therefore the entire fixing subgroup is

    H_o=Gal(M_star/G_o)={(a,b) in U:b=chi_o(a)Id}.

This excludes nonscalars and CRT scalars with different signs at
three and five. Both uniform scalar signs occur and are distinct.
The six tuples give exactly the three types H_A,H_B,H_C: reversing
a difference multiplies its radical by iota, which U fixes.

Apply L085's audited finite sign-count calculation to these established
data. For completeness its full count is determined by the eight
triples (chi_A,chi_B,chi_C): each H has one element for each triple,
with b its own column sign. For any pair of columns exactly four
triples agree; all three agree only at (+,+,+) and (-,-,-).
Thus each subgroup has order eight, each pairwise intersection has
order four, and their common intersection has order two. The subgroups
are distinct, with four elements in each scalar-sign sector.

Every root permutation actually occurs: reduction of the full image
modulo two gives GL_2(F_2)=S_3 on the three nonzero two-torsion
points. For any actual sigma in Gal(M_star/Q), applying sigma to
the coefficients and every full torsion point gives precisely the
row G_o determined by its root permutation. K is preserved and
sigma(iota)=plus or minus iota, so no extra generator occurs.
Conversely every Q-conjugate arises this way, since M_star/Q is
Galois. Thus all conjugates of H_A are exactly H_A,H_B,H_C.
Their intersection is the full core, of order two. Finite Galois
correspondence identifies its fixed field with G_star^nor and gives

    [G_star^nor:G_star]=[H_A:core(H_A)]=8/2=4.

As an attained changing-conjugate check, choose the actual a with
signs (+,-,+) and b=Id. This element fixes G_star but negates
B/A. A root permutation interchanging r_2 and r_3 yields the row
with denominator B^2; its stabilizer is H_B, distinct from H_A.
Thus this is a genuine nonnormality verdict using full stabilizers,
consistent with, and independent of, the exhausted cyclic separator.

### Relevance, qualifications and remaining gaps

All tests pass for this same newly chosen E and its fields: actual
cross-residue lift, both full pointed transports, coefficient/root
field, both embedded completions, the actual joint image and every
full stabilizer. The exact index is four rather than the required
one. This is local progress by assessed known methods, with no claim
of a new general theorem or progress beyond the checked sources.
No effective coefficients or formal verification are supplied. The
normal closure is a proof object; replacing G_star by it is not
part of the construction and would require separate assessment.

No old witness is renamed, and none of its independent reduction,
image, covering, cusp, height or native-data conclusions is transferred
to G_star. In particular this does not exclude every other auxiliary
choice. Independent initial data, native moduli fiber and input/action,
retained radical/scalar tests, all-image factorization, marked pilot
transport, essentiality and original finite B>=A remain unresolved.
This is not a candidate solution of the IUT challenge. The separate
critical audit below validates only this combined specialization.

### Separate critical audit — 2026-10-19, step345

**Verdict and scope.** The combined conclusion passes the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-19-new-member-exact-legendre-critical-audit.md`.
The full proof and both canonical audited inputs L085,L086 were checked.
The primary results listed above are reused at their inspected versions;
no new general theorem or changed witness is required. The coefficient/
root-field paragraph now uses finite Galois correspondence inside K,
which is already among the cited inputs, in place of an unnecessary
infinite-Galois reference. This clarifies the justification without
changing the claim or adding a mathematical hypothesis.

**One member, actual roots and maps.** All uses of occurrence and local
retention concern the one original monic E from L086. Its audited
congruences give c=1,d=e=0 modulo three, v_3(Delta)=30 and unit c4.
Thus g is separable and j has valuation -30. Because E[2] is a
subgroup of its H-rational E[30], all three actual roots lie in H.
For a hypothetical negative-valuation root, the valuations of cx^2,
dx,e are at least 2v_3(x),v_3(x),0, all strictly greater than
3v_3(x); the unique lowest term cannot cancel. Hence every root is
integral. Reduction of the complete factorization then forces exactly
the multiset {-1,0,0}, not merely the existence of some residue roots.
Choosing r_1 with residue -1 makes D=r_2-r_1 a unit of residue one.
The simple root one of Z^2-D has nonzero derivative two in k_H.
The complete-DVR Hensel theorem applies even though H is ramified;
no simple-root claim is made for the cubic's double residue root.
Both signs of its algebraic unit root s belong to the fixed H.

With the two displayed projective changes, direct substitution gives

    V^2 Z-X(X-Z)(X-tZ)
      =D^(-3)(y^2 z-product_m(x-r_m z)).

The forward matrix has determinant 1/(D^2 s), which is nonzero,
and its displayed inverse composes to the identity on projective
space. Both send [0:1:0] to itself, so the cited pointed-isomorphism
theorem supplies group compatibility on the entire smooth cubic.
Every geometric n-torsion point is transported in both directions,
including the origin, for n=15 and seven. This is stronger than
matching x-coordinates or comparing the sizes of two torsion sets.
The coefficients lie in the same F'_star and H in both directions.
No assertion that the maps descend to G_star is used. Replacing s by
-s is inversion on the target and leaves the complete coordinate
fields unchanged.

**Coefficient field and both embedded completions.** Inside the finite
Galois root field K, an element fixing t makes the two ordered geometric
two-torsion objects have the same parameter. The inspected ordered-level
classification gives a pointed automorphism of E between them. Since
j is neither zero nor 1728, its only pointed geometric automorphisms
are plus and minus one; both act trivially on E[2]. Consequently that
element fixes all three roots and is the identity of Gal(K/Q).
Since t is already in K, finite Galois correspondence gives Q(t)=K.
This argument neither uses full mod-two image nor assumes a rational
Legendre section; the full image is needed later for occurring conjugates.

Full 15-torsion of E is F_star-rational. Applying the actual map gives
all E_L[15] in F'_star, with the inverse ensuring exhaustion. Thus
G_star is contained in F'_star and hence in H. In the other direction,
the pairing on the full geometric 15-torsion of E_L gives all mu_15
inside G_star. In characteristic zero, a primitive fifteenth root
generates this entire group, so this includes the specified
alpha=zeta_60^4, not just an unspecified isomorphic group. Together
with the defining iota=zeta_60^15, the identity alpha^4/iota=zeta_60
gives the embedded lower cyclotomic inclusion. The completion of
Q(zeta_60) at this embedding is Q_3(zeta_60)=H. Successively adjoining
t and the finite complete 15-torsion coordinate list, all already in H,
therefore gives exactly (G_star)_u=H by the cited induced-completion
theorem. An inclusion G_star subset H alone would not suffice.

For seven-torsion, the forward map gives
H(E_L[7]) subset H(E[7]); the inverse gives the reverse inclusion.
L086 identifies the latter embedded field with N. Applying the same
completion theorem to G_star's own full seven-torsion coordinate list
then gives (G_star(E_L[7]))_w=N. The geometric torsion points used
locally and globally are the same points in Omega: finite torsion over
the number field Q(t) is algebraic over Q and therefore belongs to the
chosen Q-bar. Neither completion equality uses normality of G_star,
a comparison of degrees, a field isomorphism chosen after the fact,
or local rationality inferred from global point counts.

**The ambient group and exhaustive signs.** Yelton's arbitrary monic
separable-cubic theorem applies to this g in characteristic zero.
Its signed cyclic radicals generate K(iota,A,B,C), since iota converts
each reversed difference. Thus the actual M_star equals
F_star Q(E[4]). Every generator belongs to Q(E[60]), including zeta_60
by the pairing. Conversely [45]P and [16]P, for P killed by 60,
are killed by four and fifteen and sum to P. The Q-defined group law
therefore puts every such full point in M_star. This proves
M_star=Q(E[60]) as an embedded finite Galois field. Likewise for
P killed by 30 the points [15]P and [16]P are killed by two and
fifteen and sum to P, proving F_star=k(E[15]).

L086 gives the full joint level-120 image for this very E. CRT and
surjective reduction modulo four give the full product at levels four
and fifteen; there is no inference from separate marginal images.
Fixing K requires a=Id modulo two, and fixing zeta_60 requires
determinant one on both factors. These conditions are both necessary
and sufficient to fix k. The full fixing group is therefore exactly
U=P_4 times SL_2(Z/15Z). The matrices Id+2X with tr(X)=0 in F_2
are precisely P_4, with eight elements and additive multiplication
in X. An element with all three radical signs positive fixes every
generator of Q(E[4]), so is the identity on that field and on E[4].
The sign map is thus faithful; equal orders make it bijective. The
radicals belong to the four-division field, so their signs depend only
on a. All eight sign triples occur with every permitted b in U.
This supplies the actual independence needed here, without a generic
independence assumption or any use of the recorded cyclic Frobenius.

**All fixing groups, conjugates and the threshold.** For each ordered
row, t_o generates the same K by the preceding ordered-level argument.
The full torsion maps put its field G_o inside M_star, and its pairing
puts k inside G_o. Hence its entire pointwise stabilizer lies in U.
For h=(a,b) in U, applying h to the map changes only the square-root
y-denominator by chi_o(a). In the transported full 15-torsion basis
this gives exactly chi_o(a)b. Pointwise fixing is therefore equivalent
to b=chi_o(a)Id. This retains both uniform signs and excludes both
nonscalars and CRT scalars with opposite signs modulo three and five.
Both uniform signs have determinant one and are distinct modulo 15.
Replacing a denominator difference by its negative multiplies its root
by iota, fixed by U, so the six rows yield exactly H_A,H_B,H_C.

The complete sign triples are

    +++, ++-, +-+, +--, -++, -+-, --+, ---.

For each triple there is exactly one element of each H, with b forced
by its respective column. Each column is positive four times and
negative four times. For any chosen pair of columns, equality leaves
their common sign and the third sign free, giving four triples.
All three columns agree only for +++ and ---, giving two triples.
Thus |H_o|=8, all pairwise intersections have order four, and the
triple intersection has order two. This is the entire finite count,
including the negative scalar sector, not a sample of the fixing group.

Reduction of the actual full image modulo two realizes all S_3 root
permutations. Applying an automorphism of M_star to every coefficient
and every torsion point gives exactly its corresponding row field:
K is invariant, and iota goes to plus or minus iota. The sign or other
image of a chosen s does not create a new row because the literal
Legendre equation depends only on t_o. Every Q-embedding of G_star
extends to the algebraic closure and preserves M_star, which is normal.
Consequently these rows exhaust all conjugates, and all three different
fixing groups actually occur. Their intersection is the core in the
whole ambient Galois group, not merely in U.

The fixed field of this order-two core is the compositum of all those
conjugates, hence G_star^nor. The tower gives [M_star:G_star]=8 and
[M_star:G_star^nor]=2, so the required relative index is 8/2=4.
An actual element with radical signs (+,-,+) and b=Id fixes G_star
but negates B/A; the transposition of r_2 and r_3 realizes H_B rather
than H_A. Thus nonnormality is attained, in agreement with the core
calculation. No normal closure is substituted for the literal G_star.

**Result and limitations.** The combined specialization and its two
embedded completions are validated; there is no failed mathematical
claim or new direct input. The achieved normal-closure index is four,
where normality requires one. This establishes the reliability of a
local known-method screen, not progress beyond the checked general
sources and not a demonstration of an essential IUT flaw. In particular,
this audit does not newly identify native moduli/tripodal fields or
apply a native field hypothesis to this changed member. Independent
initial data, actual native input/action, all-image factorization,
pilot transport, essentiality, the old witnesses' questions and the
original finite B>=A remain open. ATTEMPTS/034 is preserved.
The argument assembly and direct mathematical inputs remain L085,L086;
no PROOF or DAG change is needed. This canonical verdict supersedes
the overview's pending-audit wording for L087 only.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
specialization has not been checked. Unknown coverage is not absence.
The named general inputs are imported with precise citations above;
the explicit same-member applicability and finite Galois calculation
are informal proofs, not machine-checked certificates.
