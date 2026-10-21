# L089 — The two norm conditions do not certify the ramified full image

## Hypotheses

Use L069's fields D=K tensor_Q F, F=Q(theta), and L073's curve and
fixed cubic

    E: Y²=g(X), g(X)=X³−4X²−160X−1264.

Let W_S and T be exactly L074's supported norm-square space and L084's
subspace. In particular T imposes the two rational eleven-adic full
Kummer conditions and the entire primitive dyadic condition, but NOT
the full Kummer condition at the degree-ten eleven-adic place.
Representatives may have negative valuations and nontrivial localized
ideal-class contributions. L088 proves N_D/F(T)=1 on square classes.

Write Q=Q11 for this proof, and use L073's entire ordered algebras

    K tensor Q11 = Q × Q × L,       L=Q(r), r^10=−55,
    F tensor Q11 = Q × M,          M=Q(z), z²=−11,
    D tensor Q11 = (Q × M) × (Q × M) × (L × L × L).

Choose s in Q with s²=5 and s=4 modulo 11. In L set

    d=16·11² r^5/(s g'(alpha)),
    beta=(4−alpha+d)/2, gamma=(4−alpha−d)/2,

where alpha is the unique root of g congruent to 8 modulo 11.
The last three factors are ordered alpha,beta,gamma. Identify M with
the quadratic factor of F tensor Q11 by
theta=(4−alpha+16·11² z/g'(alpha))/2. Then its embeddings into the
beta and gamma factors of L are respectively

    i_+(z)=r^5/s,       i_−(z)=−r^5/s.

Write u for the class of −1 in each local square-class group; it is a
nonsquare unit in all three fields. In formulas 1 means the square
class identity, not a prescribed representative of a global class.

## Conclusion

The necessary eleven-adic envelope E_11 obtained from the two rational
full Kummer images, the square D/K norm, and the localized square D/F
norm has exactly sixteen elements. With e1,e2,b,m in F2, they are
precisely

    y1=(1,u^e1), y2=(1,u^e2),
    A=u^(e1+e2+m),
    B=u^b r^m,
    C=u^(b+e1+e2+m) r^m.                         (1)

Here (A,B,C) is the ramified ordered triple and y1,y2 are the rational
base-place classes. Every class of T localizes into E_11. The ramified
projection of E_11 has eight elements and dimension three. L073's
full ramified Kummer subgroup is exactly

    H_L={(1,h,h): h in L*/L*²},                    (2)

of size four and dimension two. In particular the envelope element

    y1=(1,u), y2=(1,1), (A,B,C)=(u,1,u)          (3)

lies outside H_L. It may be paired with identity at both dyadic factors
without violating any of the conditions used to construct this norm
envelope.

Thus this sufficient norm certificate for loc_L(T) subset H_L fails.
This does NOT decide that containment: (3) is not proved to be the
localization of any global supported class, let alone a class of T.
No bound on T or its unit intersection improves, and no rank bound,
integer exclusion or complete Beal candidate follows.

## Proof

### Imported results, relevance and scope

The assessment saved before this research invocation is
`drafts/literature/2026-10-17-ramified-eleven-full-image-on-t.md`,
DECISION SPECIALIZE. Its approved test is the necessary norm-envelope
comparison on the unchanged T, retaining both quadratic embeddings.
The intended downstream use is to decide whether this condition can
be retired or still requires independent global arithmetic. An outside
envelope tuple stops only this sufficient mechanism.

Import J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Proposition 2.19 and Corollary 2.20, pp.31–32, for norms from minimal
polynomials and embeddings; Proposition 8.2 and Corollary 8.4, p.136,
for complete tensor decompositions and products of local norms.
The extensions here are finite and separable in characteristic zero;
normality is not required. Import Pete L. Clark, *Algebraic Number
Theory II: Valuations, Local Fields and Adeles*,
[161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
revision date unidentified, Theorem 2.24, p.73, and Theorem 2.36,
pp.79–80, for the local square theorem and multiplicative power classes.
These complete discretely valued fields all have residue field F11,
and the power exponent two is prime to its characteristic.

L073 already supplies the full Kummer generators, including exceptional
evaluations and exhaustiveness by Barrera Salazar–Pacetti–Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Section 1, Lemma 1.3 and Remark 1.4, pp.3–4.
No new local point enumeration or reproof of these general theorems
is needed. The work below is the field-specific norm and subgroup
calculation not supplied by those sources. It is classified
REPRODUCTION, without a claim of originality beyond inspected sources.

### Exhaustive local coordinates and the two distinct norm maps

The nonzero squares of F11 are {1,3,4,5,9}, so −1 is nonsquare and
s (residue 4) is square in Q by the local square theorem. The maximal
uniformizers are 11 in Q, z in M and r in L; the latter two assertions
follow from the Eisenstein polynomials Z²+11 and R^10+55. For each
of these fields every square class has a unique expression u^a pi^v,
a,v in F2: divide off a uniformizer power and apply the unit residue
square test. This includes negative valuations. It describes the full
field group, not just integral units or a polynomial order.

In the ordered coordinates (unit bit, uniformizer bit), with source
uniformizer r, the complete norm maps are

    N_L/Q:       (a,v) -> (0,v),
    N_+:L -> M:  (a,v) -> (a,v),
    N_−:L -> M:  (a,v) -> (a+v,v).                (4)

For the first map, the minimal polynomial gives N_L/Q(r)=55, of Q
class [11] because 5 is square, while N_L/Q(−1)=1. For N_+ and N_−
the M-algebra structures are respectively i_+ and i_−, not a common
unlabelled copy of M. They have degree five since [L:Q]=10 and
[M:Q]=2. The respective minimal polynomials of r are

    R^5−s z,       R^5+s z.

Their degree is five because r generates L over either image of M.
Taking the negative constant term gives norms s z and −s z. As s is
square, their classes are [z] and u[z], respectively. In both cases
the norm of −1 is −1. These prove every basis image in (4).

For clarity N_M/Q sends (a,v) to (0,v): N(z)=11 and N(−1)=1.
Conjugation of M sends z to −z and acts on its square classes by
(a,v)->(a+v,v). This explains, and does not erase, the difference
between N_+ and N_−. All norm formulas here are determinant norms,
not scalar restriction; no assertion that an even-degree extension
preserves nonsquares is used.

### All factors in the universal norm equations

At each of the two rational K places, L073 gives the entire image
{(1,1),(1,u)} in Q × M. Write the choices as yj=(1,u^ej).
Their D/K norms are already square since N_M/Q(u)=1. At the ramified
place, the same norm condition for arbitrary classes (A,B,C) is

    A B C=1 in L*/L*².                            (5)

Regroup the ENTIRE D/F completion by the two places of F. Above its
rational place it is Q × Q × L, with degrees 1+1+10=12. Above its
quadratic place it is M × M × L_+ × L_−, with degrees 1+1+5+5=12.
The first two quadratic factors use the same distinguished theta
and the same M identification specified in the hypotheses; the last
two use i_+ and i_−. These are all seven factors, of total Q-dimension
36. Milne's completion norm formula and L088 consequently give

    N_L/Q(A)=1,
    u^(e1+e2) N_+(B) N_−(C)=1 in M*/M*².         (6)

Equations (5)–(6), together with the two rational choices, define E_11.
They are necessary for every T-class because its D/K norm is square
by L074 and its D/F norm is square by L088. These statements concern
any representative in D*, including nonunit localized class lifts;
no complete unit basis or class-group value is substituted. Localization
and norms preserve square-class equalities for all such representatives.

At two the defining T condition is L082's I_prim, as retained in
L084, and L088 has already shown its D/F norm square for both choices.
Thus I_prim × E_11 is a necessary combined envelope. This product
does not assert independent global realizability of its local entries.
In particular choosing identity at two in (3) respects every dyadic
condition being used. No new ramified full-local premise is imposed.

### Solving the complete finite equations

Write A=u^a r^ell, B=u^b r^m, C=u^c r^n. With all exponents in F2,
(4)–(6) give exactly

    a+b+c=0,       ell+m+n=0,      ell=0,
    e1+e2+b+c+n=0,                 m+n=0.         (7)

The last equation is implied by the second and third. Conversely (7)
is equivalent to

    ell=0, n=m, a=e1+e2+m, c=b+e1+e2+m.

There are no further equations. The free parameters e1,e2,b,m give
all sixteen distinct envelope elements in (1), since they can each
be recovered from the tuple. The equation system has rank four in
eight bits. In the projection, a,b,m are arbitrary: choose e1+e2=a+m.
It therefore has precisely eight triples

    (u^a, u^b r^m, u^(a+b) r^m), a,b,m in F2.     (8)

Each has two preimages in E_11. This is an exhaustive symbolic
kernel/image calculation, not a finite-precision sample. It also
accounts for every possible valuation parity and unit character.

### Comparison with the exact full Kummer subgroup

By L073 the full subgroup is generated by the two exceptional classes

    h_alpha=[(g'(alpha), alpha−beta, alpha−gamma)],
    h_beta=[(beta−alpha, (beta−alpha)d, d)].

The residues are g'(alpha)=1, alpha−beta=alpha−gamma=−1, and
beta−alpha=1 modulo 11. Thus h_alpha=(1,u,u). For h_beta we must
retain the unit part of d, not only its odd valuation 25. Exactly

    d/r^25 = 16/(25 s g'(alpha)),

since r^20=25·11². Its residue is 16/(25·4)=5 in F11, which is
square. Consequently [d]=[r^25]=[r]. Also beta−alpha is a square
unit. Hence h_beta=(1,r,r). These two generators yield exactly (2),
by L073's already established full-image size four.

In (8), membership in H_L is precisely a=0. There are four such
projected triples and four outside; eight of the sixteen E_11 tuples
project into H_L and eight do not. The required containment threshold
fails: the projected dimension is three, whereas H_L has dimension
two. This is a dimension comparison for a local envelope ONLY.

The particularly simple outside tuple (3) corresponds to
e1=1,e2=0,b=m=0. Its D/K norm is u·1·u=1, its rational D/F norm
is N_L/Q(u)=1, and its quadratic D/F norm is
u·N_+(1)·N_−(u)=u·1·u=1. But its first ramified component is the
nonsquare u, whereas every member of H_L has first component 1.
All seven eleven-adic components and both possible conjugate embeddings
have therefore been checked exactly on this witness.

### Decision, known traps and remaining gap

The achieved result is NEGATIVE for this sufficient norm mechanism.
It neither proves nor disproves loc_L(T) subset H_L. An actual class
outside H_L would require a global supported representative satisfying
every condition defining T; (3) is not such a representative. Conversely
global constraints missing from this envelope could still force the
containment. No globalization, weak approximation with controlled
support, class-kernel vanishing, or S-unit completeness is assumed.

This is distinct from L086's five-probe obstruction to the primitive
diagonal filter, and from L088's proved redundancy at thirteen. Those
stops remain intact. The new test uses L088 but does not expand the
old probe family or reopen exhausted affine/ideal searches. Preserve
ATTEMPTS/033–039. A new mathematical mechanism would require separate
coverage and a discriminating test. Independent critical review of the
present norm maps and the exact subgroup comparison is recorded below.
The bounds dim T<=13+dim ker(n_S) and the unit upper bound fourteen
remain unchanged, with actual T, its localization, class arithmetic,
other point classes and rational/integer lifting unresolved. T is not
a containing space for all Mordell–Weil point classes. No branch or
signature has been excluded by this result.

### Independent critical audit — 2026-10-17

The separately saved SPECIALIZE assessment is
`drafts/literature/2026-10-17-ramified-eleven-norm-envelope-audit.md`.
This audit confirms the limited obstruction without a mathematical
correction. It reuses the cited general norm and local square theorems;
the computation below independently verifies the specialization, not
the imported general theory. Classification is REPRODUCTION.

**Common generator and complete norm factors.** L069 specifies the same
g and D, and the audited L073 factorization gives the unique simple root
alpha=8 and the quadratic discriminant -256·11^5/g'(alpha)^2.
The chosen root of that quadratic is the displayed image of theta in M.
Substitution z=r^5/s gives beta, while z=-r^5/s gives gamma; thus the
ordering and the two M-algebra structures really agree with the fixed
generator. Because r generates L over Q, it also generates L over
either copy of M. Degree five therefore proves that R^5-sz and R^5+sz
are the respective minimal polynomials. The odd-degree constant-term
rule gives norms sz and -sz, not the same norm in both coordinates.
Their unit parts differ by u. The even-degree polynomial R^10+55 gives
N_L/Q(r)=55; Z^2+11 gives N_M/Q(z)=11. Norms of -1 are respectively
1,-1,-1,1 for L/Q, L/M(+), L/M(-), M/Q. Since 5 and the residue 4
of s are squares, these recover every basis image in (4). Both norm
towers send (a,v) to (0,v), and conjugation sends (a,v) to (a+v,v).

Eisenstein gives residue field F11 for both M and L. Hence the cited
unit residue criterion and valuation parity give all four square
classes in each field, including elements of negative valuation. No
integral-basis claim for theta, or preservation of nonsquares under
an arbitrary even-degree extension, is needed.

The rational F-place collects the alpha coordinates from both Q-base
places and the L-base place: dimensions 1+1+10. The quadratic F-place
collects both M coordinates and the beta and gamma coordinates with
their distinct structures: dimensions 1+1+5+5 over M. These account
for all 36 Q-dimensions. The two rational Kummer first components are
square, leaving precisely N_L/Q(A). The other product is precisely
u^(e1+e2) N_+(B) N_-(C). In particular neither ramified norm is a
scalar-restriction map.

**Universal domain.** L074 defines W_S using an element square D/K
norm, not merely a principal ideal norm. L084's T supplies both
rational eleven-adic full-image conditions and the primitive dyadic
condition. Audited L088 supplies an element square D/F norm for every
such class. Localizing squares and applying the complete determinant
norm identities therefore proves (5)-(6) for all of T. Negative
valuations and localized two-class lifts obey these same identities;
no unit-generation or class-number hypothesis enters. At two, identity
belongs to I_prim, satisfies the rational full-image test and has square
norm. Taking it with the eleven-adic witness is consistent with the
selected necessary equations, without asserting that a supported
global representative realizes these simultaneous choices.

**Exceptional unit parts and the full subgroup.** Independently,
g'(8)=-32=1 modulo 11, beta=gamma=9 modulo the maximal ideal, and
the alpha differences have residue 10, whereas beta-alpha has residue
1. Furthermore r^20=25·11^2 proves the exact identity
d/r^25=16/(25 s g'(alpha)). Its residue is 16/(25·4)=5 in F11,
which is square. Thus the two exceptional classes are exactly
(1,u,u) and (1,r,r), including their unit parts. They are independent
by valuation parity, and L073's audited image-size application proves
that their four products exhaust the full image. Infinity is the
identity and all other exceptional points are already included.

**Independent exhaustive finite replay.** The script
`python3 scripts/ramified-eleven-norm/audit_envelope.py` imports no
construction script. It evaluates the three actual square-class norm
products on every one of the 256 choices of
(e1,e2,a,ell,b,m,c,n), then compares the accepted set with (1).
The first norm forces c=a+b and n=ell+m; the rational D/F norm
forces ell=0; the quadratic norm then forces a=e1+e2+m. These are
four independent binary constraints, with exactly four free bits.
The complete replay gives 16 accepted tuples, eight projected triples,
and two preimages per triple. Exactly four projected triples, and eight
envelope tuples, lie outside the full subgroup. All 17 checks pass;
the full table, basis maps, accepted set, outside set and checks are in
`scripts/ramified-eleven-norm/audit-certificate.json`. The program's
finite replay supplements the exact field justifications above; it
does not establish those field facts by numerical approximation.

For the particular witness (3), the three norm products are respectively
u^2, N_L/Q(u)=1, and u N_-(u)=u^2. Its first ramified component is
u, whereas every full-image first component is square. This independently
confirms failure of the required containment: eight possible projected
classes versus the four allowed classes, with an explicit nonmember.

The audit accepts the sufficient-certificate stop in ATTEMPTS/040.
This is new verification evidence for that previously provisional stop,
not a global noncontainment theorem or progress beyond the assessed
methods. Actual loc_L(T), the supported-class kernel and integer lifting
remain unresolved, and both dimension bounds are unchanged. The direct
mathematical inputs in DAG.md are unchanged; no new lemma is introduced.

## Mathlib

Full matching norm-envelope comparison and these ordered local fields:
**not checked**. Supporting norm, completion, local square-class and
Kummer theorem coverage: **not checked**. Unknown coverage is not absence.
