# L072 — Ordinary units and the all-finite-even norm-square space

## Hypotheses

Let K be the entire degree-twelve field of L033, and let

    D=K[X]/(X³−4X²−160X−1264).

L069 proves that D is a field and [D:K]=3. Use maximal integer rings,
ordinary fractional ideal class groups C_F=Cl(O_F), and ordinary units
U_F=O_F*. For F=K,D define

    H_F={ [alpha] in F*/F*² : v_p(alpha) is even at EVERY finite prime p },
    W=ker(N_D/K: H_D -> H_K),
    V=ker(N_D/K: U_D/U_D² -> U_K/U_K²).

All valuations are normalized ideal exponents. Norm-square means the
element norm belongs to K*². There is no positivity condition, narrow
class group, exceptional finite support, or assumption on class numbers.
No primitive solution is assumed. In particular, containment of the full
elliptic Kummer image in H_D is **not** a hypothesis asserted here.

## Conclusion

Element norm induces ordinary ideal-class norm
n_C:C_D[2] -> C_K[2]. There is a canonical exact sequence of F2-spaces

    0 -> V -> W -> ker(n_C) -> 0,

where the last map sends [alpha] to [a] for the unique fractional ideal
a with (alpha)=a². Consequently the following conditions are equivalent:

1. Every class of W is represented by an ordinary unit, equivalently W=V.
2. ker(n_C)=0, equivalently n_C is injective on C_D[2].
3. Extension of ideals C_K[2] -> C_D[2] is surjective.
4. dim_F2 C_D[2]=dim_F2 C_K[2].

The norm map n_C is always surjective here; extension is its section on
two-torsion. In particular,

    dim W = 12 + dim C_D[2] − dim C_K[2].

Every class in W has a representative of exact norm one; for V such a
representative can be chosen to be a unit. This representative assertion
is proved below, rather than identifying square norm with norm one by
definition. No actual class group, class norm kernel, unit exhaustion,
Selmer dimension, rank or integer exclusion is computed or asserted.

## Proof

### Imported ideal-square sequences and compatible norms

Use Franz Lemmermeyer, *Selmer Groups and Quadratic Reciprocity*,
Abh. Math. Sem. Univ. Hamburg **76** (2006), 279–293,
[arXiv:1108.5674v1](https://arxiv.org/pdf/1108.5674v1), August 29, 2011,
Sections 2.1–2.2, manuscript pp.2–3: the number-field ideal-square group
(called Sel(F) there, not an elliptic Selmer group) has exact sequence

    0 -> U_F/U_F² -> H_F --pi_F--> C_F[2] -> 0.

The map pi_F sends [alpha] to [a] with (alpha)=a². The ideal a exists
and is unique because all finite valuations are even and the fractional
ideal group is free on finite primes. Replacing alpha by alpha d²
replaces a by a(d), so its class is independent of the representative.
This is the imported ordinary sequence, with all finite primes retained.
Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.2,
Proposition 1.3, printed pp.8–9, supplies the corresponding S-unit
description with S consisting just of infinite places. We do not choose
its abstract splitting or assume such a splitting commutes with norm.

Relative ideal norm and its compatibility with principal ideals are
imported from J.S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
July 19, 2020, Chapter 4, Proposition 4.1(a),(c), printed pp.68–69.
In particular N(P)=p^{f(P/p)}, N((alpha))=(N(alpha)), and
N(b O_D)=b³ for ideals b of K. These apply to this separable extension
without normality. Extend them to fractional ideals multiplicatively:
define N(a b^{-1})=N(a)N(b)^{-1}; equality of two such expressions
can be cleared of denominators, so this is well-defined and preserves
the cited identities.

Thus (alpha)=a² implies

    (N(alpha))=N(a)².

In particular norm maps H_D into H_K and maps C_D[2] into C_K[2].
The preceding equality proves pi_K(N[alpha])=n_C(pi_D[alpha]).
Norms of units are units (apply integrality to a unit and its inverse),
and the maps on units commute with inclusion in H. These give the
commuting diagram of the two imported exact sequences. Unit-square
classes embed in field-square classes: if u=d² is a unit, then every
finite v(d)=0 and d is a unit. This also identifies the kernel of norm
on units with V inside W, without any integral-order assumption.

### The lift obstruction vanishes in degree three

Scalar inclusion of U_K/U_K² into U_D/U_D² is a section of norm:

    [N(u)]=[u³]=[u].

This is precisely the odd-degree unit-square argument used in Barrera
Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic twists of
elliptic curves*, [arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
September 17, 2020, Lemma 2.14, printed pp.12–13, and in L069.
Their separate global Selmer bounds and positivity/class hypotheses
are not being used. On the present diagram the possible cokernel of
unit norm is zero. The following explicit lift checks the resulting
kernel surjectivity and all choices.

Take c in ker(n_C), choose a fractional ideal a representing it, and
choose alpha with a²=(alpha). Since [N(a)]=0 in C_K, write N(a)=(b)
for b in K*. Then

    epsilon=N(alpha)/b² in U_K.

Indeed its principal fractional ideal is trivial. Define, using scalar
inclusion of epsilon into D,

    beta=alpha/epsilon.

Its ideal is still a², and

    N(beta)=N(alpha)/epsilon³=(b/epsilon)².

Thus [beta] lies in W and pi_D[beta]=c. No norm equation on unsquared
units has been assumed. This proves surjectivity W -> ker(n_C).

Changing b to bq with q in U_K changes epsilon to epsilon/q² and beta
to beta q², leaving its square class unchanged. Replacing a by a(d)
and alpha by alpha d² permits b to be replaced by b N(d); epsilon
is then unchanged and beta changes by d². For a fixed ideal a, changing
its chosen generator alpha to alpha eta, with eta in U_D, changes beta
by the unit eta/N(eta), whose norm is N(eta)^{-2}. Hence this last
ambiguity lies in V. Combined, these operations cover every
choice of ideal representative, generator and norm-ideal generator.

Conversely, compatibility shows pi_D(W) lies in ker(n_C). The kernel
of pi_D restricted to W consists exactly of unit classes whose norm
is square in K*. Unit-square injection for K identifies these with V.
This proves the asserted exact sequence; its quotient identification
is canonical even though no section of it is chosen.

### Ideal extension and dimensions

Let j:C_K[2] -> C_D[2] extend ideals. The cited formula for the norm
of an extended ideal gives

    n_C(j(c))=c³=c                 (c in C_K[2]).

Extension preserves two-torsion because it preserves principal ideals.
Therefore n_C is surjective, j is injective, and

    C_D[2]=j(C_K[2]) direct-sum ker(n_C).

For example c in C_D[2] decomposes as j(n_C(c)) times
c j(n_C(c))^{-1}; the second factor has trivial norm and the two
summands have trivial intersection. This proves equivalence of
conditions 2–4. The exact sequence proves condition 1 equivalent to
condition 2. Class groups of number fields are finite, so all these
two-torsion dimensions are finite. L069 supplies dim V=12, giving the
displayed formula for dim W. This is a size formula for the specified
ambient space, not for an elliptic Selmer group or the Mordell–Weil group.

### Exact norm-one representatives and scope

For any [beta] in W choose b in K* with N(beta)=b². Put

    gamma=beta³/b².

Since the scalar b has norm b³,

    gamma/beta=(beta/b)²,       N(gamma)=b⁶/b⁶=1.

Thus gamma represents the same D-square class, so it retains even
valuations at every finite prime. If beta is a unit, b² is a K-unit,
whence b is a K-unit by finite valuations and gamma is a D-unit.
This eliminates a further representative obstruction in this cubic
case; it makes no assertion about norms on all unsquared units.

The short compatibility and lift argument is the required specialization
of the cited exact sequences. It does not reprove general descent theory
or establish new class-group values. In particular, neither odd class
number of D nor zero relative two-torsion has been established. Equal
two-ranks would suffice for unit exhaustion even if both groups have
nonzero two-torsion, but that equality is also unresolved.

Simon Proposition 1.4, printed pp.8–9, allows exceptional finite support
in actual Kummer classes. Nothing here proves all-finite-even containment
for E0/K, especially at the bad or dyadic primes. Without that separate
input W cannot be used as a containing space for the full Kummer image.
Even if containment and W=V were later proved, L071's one removed unit
would not alone certify all local conditions or integer emptiness.
ATTEMPTS/032's unfiltered-unit obstruction is unchanged. The present
result meets the criterion test only; it is not a complete Beal candidate.

### Independent critical audit (2026-10-15)

The audit confirms the statement without correction, using the prior
SPECIALIZE assessment in
`drafts/literature/2026-10-15-even-valuation-criterion-audit.md`.
The imported statements and their source qualifications above suffice;
no further theorem, class computation or arithmetic script is needed.
This is a proof audit of the specialization, not an independent reproof
of the cited general ideal-square or ideal-norm theorems.

First, all maps are maps of the stated square-class spaces. For a
fractional ideal a, the exponents in N(a) are the sums of its prime
exponents weighted by residue degrees, including negative exponents.
Consequently N(a²)=N(a)² without a normality or unramifiedness premise.
Compatibility with principal ideals then puts N(H_D) in H_K and makes
the class-square diagram commute. The unique ideal square root of
(alpha) changes by (d) under alpha -> alpha d². Thus pi_D is a
well-defined homomorphism on field-square classes, not just on chosen
elements. Units inject into these classes in both fields because a
square root of a unit has valuation zero at every finite prime.

The kernel and surjectivity tests can be checked directly. If
[alpha] is in W and pi_D([alpha])=0, write its ideal square root as
(d). Then alpha/d² is a unit with square norm. The unit-square
injection over K places this unit in V. Conversely every element of
V has trivial ideal class. For any c in the class-norm kernel, its
two-torsion property supplies a²=(alpha), while trivial class norm
supplies N(a)=(b). These are independent uses of the two hypotheses.
The quotient epsilon=N(alpha)/b² has trivial principal ideal, hence
is an ordinary unit, with no sign restriction. Division by this scalar
does not change a² and gives N(alpha/epsilon)=(b/epsilon)². Thus
every c is reached. In particular no principal representative for a
itself, odd class number, or surjectivity on unsquared units is assumed.

For a simultaneous arbitrary change of all choices write

    a'=a(d),  alpha'=alpha d² eta,  b'=b N(d) q,
    eta in U_D,  q in U_K,  d in D*.

These forms are exhaustive: equality of ideal classes gives d, and
equality of principal ideals makes the two remaining ratios units.
Direct substitution gives

    epsilon'=epsilon N(eta)/q²,
    beta'/beta=d² q² eta/N(eta).

The first two factors in the last expression are D-squares. The last
is a D-unit of norm N(eta)^(-2), so it represents an element of V.
This verifies the combined change, including fractional representatives,
and proves that the inverse lift to W/V is independent of every choice.
It does not give a canonical lift to W itself.

For the class section, N(b O_D)=b³ gives n_C j=1 specifically on
two-torsion; it would not be the identity on the full class group.
The decomposition c=j(n_C(c)) times c/j(n_C(c)) has its second
factor in ker(n_C), and applying n_C shows the intersection is zero.
Class-number finiteness makes dimension equality equivalent to zero
kernel. Together with exactness this proves all four equivalences.
L069 supplies the entire cubic extension and the full unit dimensions
19 and 7, whose norm difference is twelve. Thus the dimension formula
uses complete groups, rather than a subgroup of discovered units.
L033 is used for its unconditional field input only; its hypothetical
primitive solution and GRH-dependent source computations are not inputs.

Finally, if N(beta)=b² then beta³/b² differs from beta by
(beta/b)² and has norm b⁶/(b²)³=1. The two choices of square root b
give the same expression. When beta is a unit, b is a unit by every
finite valuation, so the normalized representative remains a unit.
This proves both exact-norm assertions without replacing the definition
of W or imposing positivity.

The audit therefore accepts the conditional criterion only. Every
finite prime, including those above two and eleven, is retained in H_D;
the cited exceptional-support theorem does not assert that actual
Kummer classes belong to this group. The class kernel, that containment,
further local conditions and integer lifting remain unresolved. The
unfiltered obstruction in ATTEMPTS/032 remains valid. No argument or
direct mathematical dependency changes, and no rank bound follows.

## Mathlib

The full ordinary ideal-square norm-kernel sequence, this explicit field
specialization and the class-group criterion: **not checked**. Supporting
relative ideal norms, class groups, unit-square injections and exact
sequence declarations: **not checked**. No absence is inferred. This
step is classified REPRODUCTION of the assessed known machinery, with
no claim of progress beyond the sources checked.
