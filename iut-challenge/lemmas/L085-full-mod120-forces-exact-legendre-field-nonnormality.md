# L085 — Full mod-120 image forces the exact Legendre field to be nonnormal

## Hypotheses

Retain exactly L080's auxiliary witness, ordered roots, field choices and
fixed algebraic closure. In its notation,

    E=E_aux/Q, D=e_2-e_1, s^2=D, t=(e_3-e_1)/D,
    K=Q(e_1,e_2,e_3)=Q(t), iota^2=-1,
    k=K(zeta_60), F_aux=k(E[15]),
    E_L: V^2=X(X-1)(X-t), G=K(iota,E_L[15]).

In particular s is the unchanged cross-residue root selected in L078;
no curve, equation, field or embedding is reselected. All division
fields contain both coordinates of every geometric torsion point.
Add the hypothesis

    rho_(E,120)(G_Q)=GL_2(Z/120Z).

This hypothesis is not a conclusion of L073 or the later auxiliary
construction. Its occurrence for this witness or within that family is
not established here. Field characteristic is zero throughout.

## Conclusion

Under the additional image hypothesis, G/Q is not normal. Its normal
closure G^nor in the fixed algebraic closure satisfies exactly

    [G^nor:G]=4,

where normality would require index one. More precisely, in L080's
finite Galois radical ambient field M, the full pointwise stabilizers
of the ordered Legendre fields have order eight. There are three
distinct such stabilizers, their pairwise intersections have order
four, and their common intersection has order two. Both scalar-sign
sectors of each full stabilizer are included.

This is a conditional known-method specialization, validated by the
separate step337 critical audit below. It screens maximal-image choices for this exact field
prescription. It does not demonstrate an essential IUT flaw, settle the
unconditional normality of the auxiliary G, or prove the original
finite B>=A. No existence or incompatibility verdict for the added
image hypothesis is claimed.

## Proof

### Imported inputs and why a specialization remains

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-19-full-mod120-conditional-legendre-normality.md`.
Use L080's audited field identifications, full twist stabilizers and
conjugate-field description. In particular its finite Galois ambient
field is

    M=F_aux(A,B,C), A=s, B^2=e_3-e_1, C^2=e_3-e_2,

and k is contained in every ordered-model field G_o. This M is a proof
ambient field, not a proposed replacement for G.

Import Jeffrey Yelton, *A note on 8-division fields of elliptic curves*,
[arXiv:1704.06190v2, 2 August 2017](https://arxiv.org/pdf/1704.06190v2),
degree-three setup and Theorem 1(a), printed pp.1–2, with its general
specialization justification in Lemma 3, Steps 1–4, pp.2–3. For a
monic separable cubic in characteristic different from two it gives

    Q(E[4])=K(iota,A,B,C).

Yelton's cyclic radicals differ from these by signs and factors of
iota, already in the right side. The original cubic is monic and
separable by L080's hypotheses, so the general theorem applies.
No generic radical independence is imported; independence will follow
from the added joint image and this field-generation theorem.

Reuse the inspected determinant/cyclotomic compatibility in
[Zywina, MaximalGalois, section 1.1, pp.1–2](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf):
on full m-torsion the determinant is the action on mu_m. Reuse
[Milne, Fields and Galois Theory, v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(b–d) and Remark 3.18(a,b), pp.39–40, for degrees, conjugate
subfields, subgroup intersections and normal closure. L080 already
imports and checks the full-coordinate twist formula, which is used
unchanged below. These general results are cited, not reproved. The
remaining task is their exact embedded-field and subgroup application.

### Identify the full ambient group

First M=Q(E[60]). Indeed the displayed 4-division formula and the
presence of K,iota in F_aux give

    M=F_aux Q(E[4]).

The Weil pairing puts all mu_60 in Q(E[60]), hence the specified
zeta_60 there. Also E[2],E[4],E[15] are subgroups of E[60]. Thus
F_aux and Q(E[4]) are contained in Q(E[60]), proving one inclusion.
Conversely M contains Q(E[4]) and Q(E[15]). For every P in E[60],
the points [45]P and [16]P belong respectively to E[4] and E[15],
and their sum is [61]P=P. Scalar multiplication and addition are
Q-defined morphisms. Both coordinate sets in M therefore give
P in E(M). This proves the opposite inclusion, including all
coordinates and the origin.

The Chinese remainder decomposition identifies the level-120 module
with its level-8 and level-15 parts. Reduction GL_2(Z/8) to GL_2(Z/4)
is onto: any lift of an invertible mod-four matrix has odd determinant
and is invertible mod eight. The added surjectivity consequently gives

    Gal(M/Q)=GL_2(Z/4) x GL_2(Z/15).

This is the action of the actual joint representation restricted to M,
not a product inferred from unrelated marginal images. Compatible bases
are used on the torsion factors. Write an automorphism as (a,b).

Fixing K is equivalent to a mod 2 being the identity, since the three
nonzero 2-torsion points are (e_j,0). Fixing zeta_60 is equivalent to
both det(a)=1 mod 4 and det(b)=1 mod 15 by determinant compatibility.
Thus the full subgroup fixing k is

    U=Gal(M/k)=P_4 x S_15,
    P_4={a in GL_2(Z/4):a mod 2=Id, det(a)=1},
    S_15={b in GL_2(Z/15):det(b)=1}.

Explicitly, every element of P_4 is uniquely

    a=Id+2X, X in M_2(F_2), tr(X)=0.

The determinant identity is det(Id+2X)=1+2tr(X) mod 4.
There are three free binary entries, so |P_4|=8. Multiplication
corresponds to addition of X, since its cross term is divisible by
four. In particular P_4 is an elementary abelian group of order eight.

### Derive all radical signs from the actual restrictions

Each a in P_4 fixes K and iota and hence the squares of A,B,C. It
therefore gives three signs

    chi_A(a)=a(A)/A, chi_B(a)=a(B)/B, chi_C(a)=a(C)/C.

These are characters on P_4, defined through its faithful action on
Q(E[4]). Their combined map

    chi:P_4 -> {+1,-1}^3

is injective: an element in its kernel fixes K,iota,A,B,C and hence
all of Q(E[4]) by Yelton's formula, so its full 4-torsion action is
the identity. Domain and codomain both have order eight, making chi
bijective. This establishes every independent sign pattern without
assuming a matrix-to-radical labelling. In particular it proves
radical independence in this application from the added hypothesis.

For h=(a,b) in U the radical signs depend only on a, as all three
radicals belong to Q(E[4]). Full joint image means that every such
(a,b) with a in P_4 and b in S_15 actually occurs. In particular
Gal(M/F_aux)=P_4 x {Id}, and its action realizes all eight sign patterns
over F_aux. The single recorded Frobenius was insufficient for this
assertion; it is not being used to infer it.

### Evaluate the complete ordered-model stabilizers

For the original ordered row, L080's exact full stabilizer formula is

    H_A=Gal(M/G)={(a,b) in U:b=chi_A(a)Id}.

For rows whose denominator differences are respectively plus or minus
B^2 and C^2, that same formula gives

    H_B={(a,chi_B(a)Id):a in P_4},
    H_C={(a,chi_C(a)Id):a in P_4}.

Changing the sign of a difference multiplies its chosen radical by
plus or minus iota. Since U fixes iota, this does not change its
character or full stabilizer. These are therefore all six rows,
paired according to the three unordered root pairs. Both Id and -Id
belong to S_15 and are distinct. Each character takes each sign on
four elements of P_4, by bijectivity of chi. Consequently each H has
exactly eight elements, four with b=Id and four with b=-Id. No
additional b is possible by the displayed full twist-kernel formula.

For two different types, for example A and B,

    H_A intersect H_B
      ={(a,chi_A(a)Id):chi_A(a)=chi_B(a)}.

Exactly four of the eight sign triples have their A and B signs equal;
two have both plus and two both minus. This proves intersection order
four for this pair and, by the same count on the other two pairs,
for every pair. The common intersection of all three has exactly
the two elements corresponding to sign triples (+,+,+) and (-,-,-),
with b respectively Id and -Id. In particular H_A,H_B,H_C are distinct.

The mod-two image is all GL_2(F_2), acting as S_3 on the three
nonzero 2-torsion points. Every ordered-root permutation is therefore
realized by an actual Q-automorphism of M. L080 identifies the
conjugates of G with the corresponding actual row fields. Thus the
conjugates of H_A in Gal(M/Q) are exactly H_A,H_B,H_C, and their
intersection, the core of H_A, has order two. The fixed field of
this core is the compositum of all conjugates of G, namely its
normal closure; M/Q is already finite Galois. Galois correspondence
gives

    [G^nor:G]=[H_A:core(H_A)]=8/2=4.

This proves nonnormality and the exact claimed index.

An explicit sign certificate also checks the changing-conjugate test.
Choose a in P_4 with signs (+,-,+), whose occurrence was proved
above. Then h=(a,Id) fixes G pointwise but sends B/A to -B/A.
This nonzero radical is not in G. An actual permutation interchanging
e_2 and e_3 has sigma(D)/D=(e_3-e_1)/(e_2-e_1)=t and
q_sigma=plus or minus B/A. L080's compositum criterion therefore
gives G sigma(G)=G(B/A) strictly larger than G, in agreement with
the full core calculation.

### Qualifications, threshold and remaining gap

The achieved normal-closure index is exactly four under the additional
full-image hypothesis, against the required index one. This is a
conditional obstruction to this exact auxiliary construction's normality;
it is not a contradiction in IUT and not a disproof of an unconditional
normality assertion about the witness. The added joint image has not
been established or shown realizable; discriminant–cyclotomic
entanglement must still be respected in any future occurrence question.
No occurrence question is undertaken here. All input choices, the exact
G and local H,N are unchanged. The ambient M is used only for Galois
correspondence. ATTEMPTS/034's stopped cyclic mechanism is preserved.

Independent initial data, retained-witness questions, native input/action,
marked all-image factorization, pilot transport, essentiality and the
original finite B>=A remain unresolved. The calculation reproduces the
assessed Galois/twist method in this conditional case; it claims no
certified originality or result beyond the known methods checked. The
separate audit below validates exactly this conditional conclusion.

### Separate critical audit — 2026-10-19, step337

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-19-full-mod120-normality-critical-audit.md`.
The full L085 argument and full audited L080 were checked, reusing the
approved primary-source coverage. All mathematical claims pass under
the stated extra hypothesis. The citation above now explicitly includes
Milne Theorem 3.17(b), the degree/index clause; this is a citation
clarification, not a repair of the mathematical argument. The following
checks supply a complete finite-case certificate without a script.

**Embedded fields and actual restriction.** Yelton's general theorem,
not its generic independence argument, applies to the unchanged monic
separable cubic. Its three cyclic radicals generate the same field as
A,B,C after adjoining iota: reversing a difference multiplies a root
by a sign of iota. Thus M=F_aux Q(E[4]). The inclusion in Q(E[60])
uses both coordinate fields and the Weil pairing on all 60-torsion.
In the reverse direction, [45]P is killed by 4 and [16]P by 15, and
their sum is P for every P killed by 60. The Q-defined group law makes
this a field-of-definition assertion for each full point, including
the origin, not an x-coordinate or degree comparison. Hence M=Q(E[60]).
The normality of M is also established independently in L080.

Restriction of the actual surjective level-120 representation to
E[4] and E[15] is onto the asserted product: reduction from level 8
to 4 is onto and CRT permits the independent level-15 matrix. Its
kernel fixes exactly M because M contains every coordinate at level
60. Fixing the roots means fixing all E[2]; fixing the specified
zeta_60 means determinant one on both factors. This proves the full
group U=P_4 x S_15, not merely an inclusion. Conversely those
conditions fix every generator of k. L080's k subset G_o for every
row excludes pointwise stabilizers outside U, even if such elements
preserve G_o setwise. All these assertions concern the same embedded
fields; no normality of G or F_aux(s) has been assumed.

**Faithfulness before independence.** The matrices Id+2X of trace-zero
X over F_2 are exactly P_4, with eight elements and additive
multiplication in X. Each fixes the roots and iota. If its three radical
signs are all positive, it fixes every generator of Q(E[4]), and so is
the identity matrix on E[4]. This proves injectivity of the sign map;
equal finite orders then prove its surjectivity. Since the radicals
are in the level-four coordinate field, the level-15 component cannot
change their signs. Thus every sign triple occurs jointly with each
chosen b in S_15, including each scalar sign. Neither the recorded
Frobenius nor generic independence is needed.

**Exhaustion of the complete stabilizers.** In L080's transported
basis, h fixes the full row field if and only if chi_o(h)b=Id on
the full free rank-two Z/15Z-module. It follows that b=chi_o(h)Id.
Besides excluding nonscalar matrices, this excludes CRT scalars
whose signs at 3 and 5 differ: the single radical character has the
same sign on both primary torsion parts. Both b=Id and b=-Id are
permitted, have determinant one, and are distinct. Replacing a radical
by its negative or by iota times it does not change its character on
U. Thus the six rows give precisely H_A,H_B,H_C.

Here + and - in the three b-columns denote the full scalars Id and
-Id modulo 15. Each row labels the unique a in P_4 with the indicated
signs. The last column is the action of the element (a,chi_A(a)Id)
of H_A on (B/A,C/A).

| (chi_A,chi_B,chi_C) | b in H_A | b in H_B | b in H_C | ratio signs |
| --- | --- | --- | --- | --- |
| (+,+,+) | + | + | + | (+,+) |
| (+,+,-) | + | + | - | (+,-) |
| (+,-,+) | + | - | + | (-,+) |
| (+,-,-) | + | - | - | (-,-) |
| (-,+,+) | - | + | + | (-,-) |
| (-,+,-) | - | + | - | (-,+) |
| (-,-,+) | - | - | + | (+,-) |
| (-,-,-) | - | - | - | (+,+) |

This exhausts every element of every stabilizer, since its b is
uniquely forced once a is fixed. Each stabilizer has eight elements,
four in each scalar sector. For any two columns, four rows agree;
all three agree only in the first and last rows. The pairwise
intersection orders are therefore four and the triple order is two.

**All conjugates and the degree orientation.** Surjectivity modulo
two gives every permutation of the three roots; each has a lift in
Gal(M/Q). L080's conjugate-field formula shows that any lift gives
its indicated row field, regardless of its radical signs or action
on iota. Conversely every Q-conjugate of G comes from an embedding
extending to the fixed algebraic closure and hence from such an
automorphism of M. There are no extra conjugate stabilizers: the six
rows, paired by signed denominator difference, exhaust them. Their
intersection is the core in the entire Gal(M/Q), not just in U.

With H_A=Gal(M/G) and C_core the intersection, the normal closure
is M^(C_core). Applying Milne 3.17(b) in the tower gives
[M:G]=8 and [M:G^nor]=2, hence [G^nor:G]=8/2=4.
The required index for normality is one. As an independent check on
the two-radical step, the last column of the table is onto
{+,-}^2 and has a kernel of order two. Thus the subgroup fixing
G(B/A,C/A) is exactly C_core. Both nontrivial denominator types
actually occur, so L080 identifies this compositum with G^nor.
In particular neither a missing conjugate nor a dependence between
the two ratio tests can lower the computed relative degree.

Finally, the (+,-,+) row with b=Id is an actual element fixing G
and negating the nonzero B/A. The actual root transposition of
e_2,e_3 has radical ratio a sign of B/A. It therefore supplies the
claimed strict changing conjugate. This tests full pointwise kernels,
and leaves ATTEMPTS/034's exhausted cyclic test untouched.

**Verdict and limits.** The conditional nonnormality and exact index
four are validated; no additional hypothesis, field change or new
direct mathematical input is needed. This verifies a local reproduction
of the checked methods, not a new result beyond those sources or an
IUT flaw. Occurrence or compatibility of the additional full-image
hypothesis remains unproved; the audit does not certify a nonvacuous
instance. Independent initial data and the original finite B>=A remain
open. This canonical audit supersedes pending-audit wording in the
unchanged overview. There is no argument or DAG change requiring an
overview or dependency update.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
conditional field-normality specialization has not been checked. This
is not evidence of absence. The cited 4-division generation, determinant
compatibility and finite Galois results are the standard inputs; the
complete field identifications, sign-map and stabilizer counts above
are the informal application. No formal verification is claimed.
