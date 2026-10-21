# L080 — Exact conjugate fields and the recorded Frobenius nonseparation

## Hypotheses

Keep exactly the auxiliary witness, embedding and choices of L078
and audited L079. Write E=E_aux, and relabel its ordered roots
as e_1=r_i, e_2=r_j, e_3=r_k, so that

    D=e_2-e_1, s^2=D, t=(e_3-e_1)/D,
    K=Q(e_1,e_2,e_3)=Q(t),
    k=K(zeta_60), F_aux=k(E[15]),
    E_L: V^2=X(X-1)(X-t),
    G=K(iota,E_L[15]), iota=zeta_60^15.

Here s is still the chosen cross-residue root in H, not a new
choice of the curve or field. All division fields contain both
coordinates of every geometric torsion point. For every ordered
triple o=(a,b,c) of distinct indices in {1,2,3}, put

    D_o=e_b-e_a, t_o=(e_c-e_a)/D_o,
    E_o: V^2=X(X-1)(X-t_o), G_o=K(iota,E_o[15]).

Use the actual arithmetic Frobenius lift f at 89 from L073;
tau=f^2 fixes F_aux and negates every signed difference radical
by L074. Neither all root permutations nor independent radicals
are assumed to occur.

## Conclusion

For every actual sigma in Gal(Q-bar/Q), take the ordered triple
o determined by (sigma(e_1),sigma(e_2),sigma(e_3)), and any square
root q_sigma of sigma(D)/D in the fixed closure. Then

    sigma(G)=G_o,
    G sigma(G)=G(q_sigma).

Consequently G/Q is Galois exactly when q_sigma belongs to G for
every occurring ordered triple. The normal closure of G has degree
at most four over G; the required index for normality is one.
This upper bound does not decide that requirement.

In the finite Galois ambient field defined below, the cyclic image
C of the recorded f has order four, and its intersection with the
pointwise stabilizer of every G_o is the identity subgroup. Thus
no element of C fixes one G_o pointwise and moves a point of another.
This rules out a separator drawn solely from that recorded cyclic
image; it does not prove that f preserves G setwise or that G/Q
is normal or nonnormal.

This is a known-method specialization, not a result beyond the
literature checked. The separate step317 critical audit below validates
these conclusions. The normality verdict and original finite B>=A remain open.

## Proof

### Imported inputs and exact scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-18-auxiliary-exact-legendre-field-galois.md`.
Import [Antieau–Meier, arXiv:1608.00851v3, 5 May 2020](https://arxiv.org/pdf/1608.00851v3),
Proposition 4.5/Corollary 4.6, pp.14–15, and the corrected torsor
action and Lemma 4.7 with proof, pp.15–16. The permutation changes
the square-root torsor by the ratio of the new root difference to
the old one. We compute that ratio on the actual transformed
ordered tuple below; a coarse Legendre action alone is insufficient.

Import the number-field quadratic-twist representation formula in
[Gonzalez-Jimenez–Lozano-Robledo–York, arXiv:2408.04159v1](https://arxiv.org/pdf/2408.04159v1),
Lemma 3.4 proof, pp.12–13, and the full-coordinate kernel convention
in [Sutherland, Lecture 20, 1 May 2024, section 20.1, pp.1–2](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf).
Use only the formula, not Lemma 3.4(2)'s uncertified stronger field
equality. The short-equation hypothesis is available by pointed
translation in characteristic zero, as checked in L074. All D_o
are nonzero, all t_o avoid 0,1, and the level is 15>2.

Import [Milne, Fields and Galois Theory, v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(c,d) and Remark 3.18(a,b), pp.39–40, for finite
Galois correspondence, conjugate subfields and normal closure.
L073 supplies the same witness and actual f, L074 supplies its
six coordinate maps and radical signs, L078 supplies the exact
G and k subset G, and L079 supplies K=Q(t). Their proofs and
source qualifications are retained. No general theorem is reproved.

### A finite Galois ambient field

Choose square roots A,B,C_0 of respectively

    e_2-e_1, e_3-e_1, e_3-e_2

in the same Q-bar, with A=s. Set

    M=F_aux(A,B,C_0).

It contains roots of all six signed differences, since iota lies
in F_aux. L074 makes every such root nonzero and negated by tau;
the sign choices of A,B,C_0 do not affect M. F_aux/Q is finite
Galois by L073. Every Q-embedding of M into Q-bar maps F_aux to
itself, permutes the e_m, and sends each of A,B,C_0 to a root
of a signed difference. Those roots are all in M. Hence the
embedding maps M into M, and its image is M by equality of finite
Q-dimensions. Characteristic zero gives separability, so M/Q is
finite Galois. This does not assume F_aux(s)/Q is Galois.

Every E_o[15] is transported from E[15] by L074's complete map

    phi_o(x,y)=((x-e_a)/D_o, y/(D_o s_o)), s_o^2=D_o.

All these coefficients lie in M. Both directions are pointed
isomorphisms, so they cover the whole geometric torsion sets.
Thus every G_o, including G, is contained in M. By L078's
Weil-pairing argument, applied to each E_o over its own G_o,
G_o contains all mu_15. Together with iota and K this gives
k subset G_o. This use concerns field characteristic zero;
the prime 3 causes no exception.

Let U=Gal(M/k) and fix a Z/15Z-basis of E[15]. Its full action
is R:U -> GL_2(Z/15Z). For h in U set

    chi_o(h)=h(s_o)/s_o in {+1,-1}.

These are well-defined characters because h fixes every D_o.
In the basis transported by phi_o, the imported twist formula is

    rho_o(h)=chi_o(h) R(h).

Indeed h fixes e_a,D_o and changes the y-denominator by this
sign; its reciprocal is the same sign. This checks the formula
on both coordinates of every torsion point, throughout U.
Since k subset G_o, the full pointwise stabilizer in Gal(M/Q) is

    H_o=Gal(M/G_o)={h in U : R(h)=chi_o(h) Id}.

Write H for the row (1,2,3). No abstract matrix-image equality
or restriction merely to Gal(Q-bar/F_aux) replaces this subgroup.

### Actual conjugates and their composita

Take an actual sigma in Gal(Q-bar/Q), also writing sigma for its
restriction to M. Its transformed coefficients are exactly those
of the row o defined in the Conclusion. Applying sigma to every
full torsion point gives every geometric E_o[15] point, since
sigma is bijective and respects the multiplication equations.
Also sigma(K)=K and sigma(iota)=+iota or -iota. Therefore
sigma(G)=G_o as embedded fields.

Take s_o=sigma(s); a different sign gives the same character
and field. Then q_sigma=s_o/s lies in M and has square
sigma(D)/D. For h in U,

    h(q_sigma)/q_sigma=chi_o(h)/chi_(123)(h).

For h in H, R(h)=chi_(123)(h) Id, so the displayed exact
subgroup formulas give

    h in H_o  iff  h(q_sigma)=q_sigma.

Thus H intersect H_o is exactly the subgroup fixing both G and
q_sigma. The finite Galois correspondence identifies its fixed
field both with G G_o and with G(q_sigma), proving the compositum
identity. Because G_o and G are Q-conjugate they have equal
degree. Hence G_o=G iff their compositum is G iff q_sigma is
in G. This proves both directions of the normality criterion.

For clarity, here are all possible transformed tuples and ratios;
only rows realized by actual Q-conjugation are imposed:

| Transformed indices | D_o/D |
| --- | --- |
| (1,2,3) | 1 |
| (1,3,2) | t |
| (2,1,3) | -1 |
| (2,3,1) | t-1 |
| (3,1,2) | -t |
| (3,2,1) | 1-t |

This checks the torsor correction on actual tuples, without
identifying a named cycle with a left action when the source
uses a right action: the new denominator is literally
sigma(e_2)-sigma(e_1). The complete forward map is phi_o;
its inverse is (X,V) -> (e_a+D_o X,D_o s_o V).
In particular the comparison phi_o phi_(123)^(-1) has

    X_o=(e_1+D X-e_a)/D_o,
    V_o=(D s)/(D_o s_o) V.

These formulas retain precisely the radical ratio from the table.
Because iota belongs to G, opposite signs of the table entries
give the same square-root membership test. The compositum of
all actual conjugates is therefore contained in
G(sqrt(t),sqrt(t-1)), of degree at most four over G. Equality
with this upper field is not asserted when some rows do not occur.

### The exact missing information

The preceding criterion needs the memberships of the occurring
ratios in G, equivalently the values of chi_o/chi_(123) on

    {h in U : R(h)=chi_(123)(h) Id}.

In particular both scalar possibilities +Id and -Id must be
retained. One also needs to know which of the table's nontrivial
rows occur; full mod-two image has not been assumed.

There is a useful necessary screen, with a converse only for the
larger field F'=F_aux(s). For D'=sigma(D),

    sqrt(D'/D) in F'  iff  D'/D is a square in F_aux.

To verify it, write a proposed root in F' uniquely as x+y s,
x,y in F_aux; uniqueness uses L074's D nonsquareness. Squaring
and comparing the s coefficient gives 2xy=0. If y=0 the ratio
is a square in F_aux. If x=0, the equality D'/D=y^2 D makes
D'=(yD)^2, contrary to L074 for every signed difference D'.
The converse is the immediate inclusion F_aux subset F'.
Since G subset F', a nonsquare ratio in F_aux would therefore
give a genuine changing conjugate. A square ratio in F_aux
alone does not establish its root's membership in G.

L074 excludes the individual difference radicals from F_aux;
it does not evaluate these even ratios. In fact tau negates both
numerator and denominator radicals, so it fixes every q_sigma.
No inference of their membership from this one element is valid.

### All powers of the recorded Frobenius

Let c be the restriction of L073's f to M. Its square is the
restriction of tau. Tau fixes F_aux and negates A,B,C_0, so
tau is nonidentity on M and tau^2 fixes M pointwise. Therefore
c has order exactly four, and C=<c> consists of 1,c,c^2,c^3.

Every G_o contains all mu_15 as established above. The actual
arithmetic Frobenius f acts on mu_15 by zeta -> zeta^89.
For completeness, reduction at the chosen place above 89 is
injective on mu_15: if eta is such a root with residue 1 and
eta!=1, then 0=1+eta+...+eta^14 would reduce to 15!=0 in
characteristic 89, a contradiction. All roots are units, so
equality of reductions identifies the action of f with its
89-power residue action on these roots. Since 89=-1 mod 15,
each of c and c^3 inverts a primitive fifteenth root and thus
does not fix any G_o pointwise.

For c^2=tau, L074 gives action -Id on the entire transported
E_o[15] for every row. It moves a point of exact order 15,
since such a point cannot equal its negative. Thus c^2 also
does not fix any G_o pointwise. The identity fixes all rows.
This proves exactly

    C intersect H_o={1} for every ordered triple o.

Equality of these restricted kernels supplies no equality of
the full H_o. In particular it does not test whether conjugation
by c normalizes H; a pointwise-fixing separator could lie outside
C. What it excludes is obtaining such a separator merely by
taking further powers of this recorded Frobenius. The required
mixed radical/15-torsion kernel information remains uncomputed.

### Qualifications and relevance

The achieved bound on the normal-closure index is at most four;
normality requires exactly one. No such index or radical
membership has been evaluated. The negative result concerns
only the cyclic-subgroup separator test, not the normality
question as a whole. No coefficients are selected, no normal
closure replaces G, and no extra radical is adjoined to the
initial-data field. M is only an ambient field for the proof.

This isolates a missing part of one independent initial-data
prerequisite. Other independent initial data, retained-witness
memberships/scalar occurrence, actual input/action and marked
all-image factorization, pilot transport, essentiality and original
finite B>=A remain open. Retained and auxiliary curves and
parameters stay distinct; H,N and the embedding are unchanged.
The source-version qualifications of foundations/05 step272
and the existing route stops are preserved. No IUT flaw or
complete candidate resolution is claimed.

### Separate critical audit — 2026-10-18, step317

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-exact-legendre-normality-reduction-critical-audit.md`
covers precisely this audit. The complete proof passes with unchanged
hypotheses and conclusions. This verifies a known-method input; it does
not evaluate a new radical membership or establish normality. Rechecked
Milne Theorem 3.17(c,d), including both directions, and Remark 3.18(a,b),
pp.39–40, and the cited Lemma 3.4 coordinate formula, p.12, directly.
The source versions match the citations above. The other imported inputs
reuse the approved coverage; no additional classification result or the
uncertified stronger twist-field equality is needed.

**Ambient field and all row stabilizers.** L073 gives the same finite
Galois F_aux, and L074 gives all signed radicals and their tau actions.
L079 is needed for K=Q(t): L078 alone gives the cyclotomic inclusion,
not that root-field equality. Combining them yields exactly the k in
this proof inside G. For each other row, its definition already includes
K, while full rational 15-torsion gives mu_15 by the same pairing theorem.
Writing alpha=zeta_60^4, the identity alpha^4/iota=zeta_60 places the
specified cyclotomic root in that row. Thus k is contained in every G_o.

Every embedding of M sends its F_aux subfield onto itself, and sends a
radical generator to one of the two roots of a signed difference; both
are in M because iota is present. Finiteness makes this embedding onto,
and characteristic zero gives separability. Normality of M therefore
precedes every use of the finite Galois correspondence. Both directions
of phi_o identify all torsion points, so G_o is contained in M. No
Galois assertion for F' or G was used to construct this ambient field.
The symbol M here is L080's radical ambient field, not L078's global
seven-division field; likewise U,H,C are the groups defined in this
proof, not a local field or a previously named curve.

For h in U, its action fixes e_a,D_o and changes only the radical
coefficient of phi_o. Applied to each point of the transported basis,
this gives rho_o(h)=chi_o(h)R(h), also for a trivial chi_o. Since the
basis spans the full (Z/15Z)^2, identity on it is equivalent to fixing
both coordinates of every torsion point. Conversely any pointwise
fixer of G_o fixes k and hence lies in U. Consequently the displayed
H_o is the full stabilizer in Gal(M/Q), with both scalar signs retained.

**Compositum and actual conjugations.** A Q-automorphism permutes the
roots and the complete torsion equations; it fixes K as a field and
sends iota to a sign of itself. This proves sigma(G)=G_o for its actual
row, without surjectivity onto S_3. For h in H, the equality
R(h)=chi_(123)(h)Id makes h belong to H_o exactly when
chi_o(h)=chi_(123)(h). Their quotient is h(s_o/s)/(s_o/s).
Thus the full intersection H intersect H_o, not a cyclic restriction,
is Gal(M/G(q_sigma)). It is also Gal(M/G G_o), proving the exact
identity by Galois correspondence. All Q-embeddings of the number field
G extend to the chosen algebraic closure, so testing all actual sigma
covers normality. Equal degrees of G and G_o justify that containment
G_o subset G is equality. The six literal denominator differences are
D, Dt, -D, D(t-1), -Dt, D(1-t). Dividing each by D gives the
six ratios whose square roots lie respectively in G, G(sqrt(t)),
G, G(sqrt(t-1)), G(sqrt(t)), G(sqrt(t-1)) after
multiplying by iota where necessary. Thus the normal-closure degree
bound four follows, with no equality assertion or occurrence assumption.

**Quadratic screen, including the degenerate coefficient cases.** D is
nonsquare in F_aux by L074, so {1,s} is a basis of F' over F_aux.
For z=x+ys satisfying z^2=D'/D, comparing coefficients gives 2xy=0.
If y=0, the ratio equals x^2. If x=0, it gives D'=(yD)^2, impossible
because every signed difference D' is nonsquare in F_aux. The joint
case x=y=0 is impossible since D' and D are nonzero. Conversely a
square ratio has its roots in F_aux and therefore in F'. This proves
the screen as stated; the reverse implication into G is not available.
Even for D'=D or -D the valid y=0 branch is retained. All sign choices
of the root give the same membership question. The action of tau fixes
every ratio of two negated radicals, and hence cannot decide this test.

**Every cyclic case.** On F_aux, tau is identity; on each of A,B,C_0
it is negation. Therefore tau is nonidentity on M, its square is identity
on every generator, and c^2=tau|M has exact order two. Thus c has exact
order four. The reduction argument for mu_15 is valid for roots of any
order dividing 15: for eta!=1 its geometric sum of length 15 is zero,
whereas residue eta=1 would make that sum 15!=0 in characteristic 89.
Apply this also to quotients of two roots to get injectivity. The actual
Frobenius lift has 89-power residue action, giving inversion on mu_15.
Its first and third powers therefore move a primitive root in each G_o.
Its second power acts as -Id on every E_o[15] by L074; an order-15
point is moved because it is not killed by 2. Its zeroth power fixes
all rows. These exhaust C and prove C intersect H_o={1} for every row.
They make no assertion about conjugation-normalization of H by c.

**Verdict and boundary.** All load-bearing cases pass, with no repair
of the argument or change of direct inputs. The audit validates the
exact reduction and the narrow stop in ATTEMPTS/034, not a new failure
of normality. Occurring ratio memberships, the full mixed kernel and
independent initial-data requirements remain unresolved. The index
bound is still four against the necessary value one. This canonical
audit supersedes pending-audit wording in the unchanged overview;
PROOF.md and DAG.md need no argument or dependency change. There is
no result beyond the checked methods, no original finite B>=A conclusion
and no complete candidate demonstration of an essential IUT flaw.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
specialization has not been checked. This makes no absence or
formal-verification claim. The general torsor action, full-torsion
twist formula and finite Galois correspondence are imported with
precise citations; the same-witness conjugate and cyclic-subgroup
calculations are the explicit application validated by the separate
audit above. No formal verification is claimed.
