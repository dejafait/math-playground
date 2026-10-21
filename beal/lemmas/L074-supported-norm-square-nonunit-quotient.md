# L074 — The non-unit quotient with support above two and eleven

## Hypotheses

Let K be the entire degree-twelve field specified in L033, and let

    D=K[θ]=K[X]/(X³−4X²−160X−1264).

L069 proves that D is a field and [D:K]=3. No solution of a generalized
Fermat equation is assumed. For F=K,D let S_F consist of ALL maximal-ring
primes above 2 and 11, and put

    R_F=O_F[1/22],     U_{F,S}=R_F*,     C_{F,S}=Cl(R_F),
    H_{F,S}={ [alpha] in F*/F*² : v_P(alpha) is even for P outside S_F },
    W_S=ker(N_D/K: H_{D,S} -> H_{K,S}),
    V_S=ker(N_D/K: U_{D,S}/U_{D,S}² -> U_{K,S}/U_{K,S}²).

Valuations are normalized maximal-ideal exponents; negative exponents
are allowed. Square norm means element norm in K*². There are no sign
restrictions and no narrow class groups. Unit square classes are viewed
inside field square classes by the injection proved below. No claim of
full Kummer containment in W_S is assumed or established.

## Conclusion

Relative ideal norm induces n_S:C_{D,S}[2] -> C_{K,S}[2], and the natural
localized ideal-square map gives a canonical exact sequence

    0 -> V_S -> W_S --pi_D--> ker(n_S) -> 0.

Thus the requested quotient W_S/V_S is canonically ker(n_S). The
S-unit norm-lifting obstruction vanishes modulo squares, by scalar
inclusion and degree three; no surjectivity on unsquared S-units is
asserted. Extension of ideals gives a section j_S of n_S on two-torsion.
In particular,

    dim_F2(W_S/V_S)=dim_F2 C_{D,S}[2]−dim_F2 C_{K,S}[2],

and S-units exhaust W_S exactly when n_S is injective. No value of these
dimensions or either class group is computed. The two-torsion here is
that of the actual localized class groups, not an assumed image of
ordinary class-group two-torsion. This is a specialization of the known
supported ideal-square structure, with no rank or integer exclusion.

## Proof

### Imported structure and the localized rings

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
Section 1.2, Proposition 1.3, printed pp.8–9, supplies the description
of square classes with even valuations outside a finite support by
S-unit square classes and S-class two-torsion. Its S includes infinite
places, which we include without imposing signs. The S-class group is
the ordinary class group modulo the supported prime classes. We use
this result, not a new descent theorem. Its abstract splitting is not
assumed to respect norms. The natural maps and the required compatibility
are checked here because that is the difference needed for this target.

Use J.S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Propositions 3.4–3.5, printed p.48, Proposition 3.23, p.55, and
Proposition 4.1(a),(c), pp.68–69: localization preserves the Dedekind
property; fractional ideals are freely described by the surviving
primes; ideal norm uses residue degrees, preserves principal ideals,
and sends an extended ideal to its extension-degree power. These norm
statements do not require a normal extension. The Stacks Project,
[Lemma 10.36.11, Tag 0307](https://stacks.math.columbia.edu/tag/0307),
accessed October 15, 2026, says integral closure commutes with localization.

The integral closure of O_K in D is O_D. Indeed integrality over O_K
implies integrality over Z by transitivity, and every algebraic integer
of D is already integral over Z, hence over O_K. Tag 0307 therefore
identifies the integral closure of R_K in D with R_D. Inverting 22
removes precisely all primes over 2 and 11. Consequently both R_F are
Dedekind domains and their fractional ideal groups are free on the
primes outside S_F. This uses maximal rings, not polynomial orders.

For a surviving prime P of D above p of K, set N(P)=p^{f(P/p)}.
Extend this multiplicatively, including negative exponents, to
fractional R_D-ideals. It is well-defined on the free ideal group.
It also equals ordinary fractional ideal norm after forgetting supported
prime factors: the norm of every discarded prime is supported at S_K.
The imported principal and extension identities therefore descend to

    N(alpha R_D)=N_D/K(alpha) R_K,     N(b R_D)=b³,

where b is any fractional R_K-ideal. No fractional ideal is assumed
integral or principal. In particular norms of S_D-units are S_K-units,
by the first identity applied also to their inverses. Scalar inclusion
sends S_K-units to S_D-units.

### The natural sequences and norm diagram

For either F, if [alpha] belongs to H_{F,S}, its localized principal
ideal has a unique square root a: the exponent at each surviving prime
is half the exponent of alpha. Define pi_F([alpha])=[a] in C_{F,S}[2].
Replacing alpha by alpha d² replaces a by a(d R_F), so the map is
well-defined and multiplicative. Conversely a class c in C_{F,S}[2]
has a fractional ideal representative a with a²=alpha R_F for some
alpha in F*, giving an element of H_{F,S} mapping to c.

If pi_F([alpha]) is trivial, write a=d R_F. Then alpha/d² is an
S_F-unit. If an S_F-unit is a square d² in F*, its square root has
zero valuation at every prime outside S_F, so d is also an S_F-unit.
This proves the injection of unit square classes and identifies the
kernel, giving the natural form of Simon's structure:

    0 -> U_{F,S}/U_{F,S}² -> H_{F,S} --pi_F--> C_{F,S}[2] -> 0.

Norm maps H_{D,S} to H_{K,S}: at each p outside S_K its valuation is
the sum of even valuations at P above p, weighted by f(P/p), hence even.
Ideal norm preserves principal ideals and therefore induces n_S on
localized classes and their two-torsion. If alpha R_D=a², then

    N(alpha) R_K=N(a)²,

so uniqueness of ideal square roots gives
pi_K([N(alpha)])=n_S(pi_D([alpha])). Norm on unit square classes
commutes with their inclusion in H as well. These statements are the
commutative norm diagram on the two natural exact sequences; no
abstract choice of section enters it.

### The lifting obstruction and all choices

Norm on unit square classes is surjective: for epsilon in U_{K,S},
scalar inclusion gives N(epsilon)=epsilon³ and thus
[N(epsilon)]=[epsilon] modulo U_{K,S}². This is the same odd-degree
scalar argument used in Barrera Salazar–Pacetti–Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
September 17, 2020, Lemma 2.14, pp.12–13, here applied to S-units.
Their separate class/positivity hypotheses and Selmer bounds are not
used. The verification just given is necessary because ordinary units
and S-units are different groups.

Explicitly let c belong to ker(n_S). Choose a fractional R_D-ideal a
representing c and alpha with a²=alpha R_D. Since n_S(c)=0, choose
b in K* with N(a)=b R_K. Then

    epsilon=N(alpha)/b² in U_{K,S},
    beta=alpha/epsilon,     beta R_D=a²,
    N(beta)=N(alpha)/epsilon³=(b/epsilon)².

The unit assertion follows from equality of localized principal ideals,
not from any ordinary integrality assertion at supported primes. Thus
[beta] belongs to W_S and maps to c. This explicitly eliminates the
possible S-unit norm cokernel obstruction. It does not solve an exact
norm equation with prescribed unsquared units.

To check every choice simultaneously, another representative and its
generators have the form

    a'=a(d R_D),     alpha'=alpha d² eta,     b'=b N(d) q,
    d in D*,        eta in U_{D,S},          q in U_{K,S}.

These are exhaustive: equality of localized classes gives d, and
equality of the corresponding principal ideals makes the remaining
ratios units of the localized rings. Substitution yields

    epsilon'=epsilon N(eta)/q²,
    beta'/beta=d² q² eta/N(eta).

The first two factors are D-squares. The last is an S_D-unit and its
norm is N(eta)^{-2}, a square in U_{K,S}. Hence it represents a class
in V_S. The lift to W_S/V_S is independent of every choice, even though
no canonical lift to W_S itself has been chosen.

Conversely norm compatibility puts pi_D(W_S) in ker(n_S). If a class
in W_S maps to zero, its ideal square root is principal; division by
that generator squared represents it by an S_D-unit with square norm
in K*. A square root of that norm is an S_K-unit by its valuations
outside S_K. The class therefore lies in V_S, and every V_S class is
in this kernel. This proves exactness and the canonical quotient.

### Class section and limitations

Extension of localized fractional ideals preserves principal ideals and
two-torsion. Its map j_S satisfies n_S(j_S(c))=c³=c on C_{K,S}[2].
Thus n_S is surjective, j_S is injective, and each c in C_{D,S}[2]
has the unique decomposition into j_S(n_S(c)) and
c/j_S(n_S(c)), the latter lying in ker(n_S). Their intersection is
trivial by applying n_S. Each localized class group is a quotient of
the finite ordinary class group, so its two-torsion is finite. The
dimension formula and unit-exhaustion criterion follow.

This does not replace C_{F,S}[2] by the image of Cl(O_F)[2]. Quotienting
an abelian group by supported prime classes can create two-torsion from
classes not originally of order two. Nor may L069's ordinary-unit
dimension twelve be substituted for dim V_S. No S-unit basis or
supported class data are supplied here.

L072 is the ordinary-support comparison, not a premise of this proof.
Audited L073 explains why the present question retains eleven; it
does not assert that its odd local class is globally realized. The
stops in ATTEMPTS/032–033 remain unchanged. A later filtered descent
must still justify full Kummer containment, control both V_S and this
class kernel under simultaneous local conditions, and obtain a useful
rank bound; rational-point and primitive integer lifting are further
independent gaps. The achieved quotient is a conditional structural
input, not an arithmetic value or a complete Beal candidate. The separate
critical application audit below confirms this statement only.

### Independent critical application audit (2026-10-15)

The audit confirms the statement without correction under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-15-supported-norm-square-quotient-audit.md`.
It reuses the inspected Simon, Milne, Stacks and BPT inputs cited above;
it does not independently reprove those theorems or compute class groups.
No mathematical script is needed for these exact ideal and norm checks.

The field hypotheses are unconditional: L033 specifies the entire K
independently of a primitive solution, and L069 proves irreducibility
of this same cubic over K using its rational five-adic place. Thus the
extension degree in every scalar and ideal norm identity really is three.
Neither the hypothetical solution in L033 nor FNS's GRH-dependent
computations enter this argument. Characteristic zero supplies separability;
normality is unnecessary for the cited ideal-norm identities.

For the support check, P lies above a removed prime p precisely when
both lie above 2 or 11. Thus forgetting the removed prime factors
commutes with both ideal norm and ideal extension. In particular, for
an arbitrary fractional ideal with surviving exponents a_P, the exponent
of its norm at a surviving p is the integer sum

    sum_{P over p} f(P/p) a_P.

This remains valid for negative a_P; all P over a surviving p survive.
Doubling these exponents commutes with norm. For an extended ideal the
identity sum e(P/p) f(P/p)=3 yields its norm cube. Principal norms
are inherited from the ordinary maximal rings, and Tag 0307 identifies
the correct integral closure after localization. No supported valuation
is accidentally required to vanish, and no polynomial order is used.

The two natural rows are exact on the groups stated in the hypotheses.
Even exponents give a unique fractional ideal square root. Multiplying
an element by d² changes that root by d R_F, so its ideal class is
well-defined. A two-torsion class has a principal square, giving
surjectivity. Triviality of that class makes alpha/d² an S-unit.
Conversely, an S-unit with a field square root has that root in R_F*,
since 2v_P(d)=0 at every surviving prime. This proves the unit injection
over BOTH fields, including the identification of square norm in K*
with trivial norm in U_{K,S}/U_{K,S}². The principal norm identity and
uniqueness of ideal square roots establish the commuting right square;
the left square is the same element norm restricted to units.

For surjectivity on norm kernels, c in C_{D,S}[2] gives
a²=alpha R_D, while n_S(c)=0 separately gives N(a)=b R_K.
These imply epsilon=N(alpha)/b² is an S_K-unit, even when its ordinary
valuations at removed primes are nonzero. Scalar inclusion preserves
this unit property and has norm epsilon³. Hence beta=alpha/epsilon
preserves a² and has norm (b/epsilon)². Every c in ker(n_S) is reached.
This checks the possible lifting obstruction explicitly; no assertion
about surjectivity of the unsquared unit norm has been smuggled in.

All representative changes are accounted for simultaneously by
a'=a(d R_D), alpha'=alpha d² eta and b'=b N(d) q with eta and q in
the respective S-unit groups. The displayed formulas in the proof give
beta'/beta=d² q² eta/N(eta). Its square-class difference is the S-unit
eta/N(eta), whose norm is N(eta)/N(eta)³=N(eta)^(-2).
This is a square of an S_K-unit. The difference is therefore in V_S;
there is a choice-independent lift to W_S/V_S, without a claimed
canonical lift to W_S. Conversely, a W_S class with trivial pi_D is
represented by an S_D-unit, and the unit injection over K makes its
norm trivial in unit square classes. This verifies exactness at W_S.

Finally n_S j_S=[3] on localized ideal classes becomes the identity
on their two-torsion, not on arbitrary ideal classes. Extension preserves
two-torsion, so j_S is genuinely a section with image intersecting
ker(n_S) trivially. Finite ordinary class groups have finite localized
quotients, justifying the stated dimension subtraction. This calculation
uses two-torsion AFTER localization; it neither assumes a lift from
ordinary two-torsion nor substitutes the ordinary unit dimension for V_S.

The audit therefore accepts the canonical quotient and its section as
an application of known structure. The direct mathematical inputs remain
L033 and L069; L072 and the stops in ATTEMPTS/032–033 are comparisons,
not additional premises. Full Kummer containment, S-unit and S-class
arithmetic, simultaneous local restrictions and the rank threshold remain
unresolved. In particular no class value, global realization of L073's
odd local class, rank bound or primitive integer exclusion was verified.

## Mathlib

The full supported norm-kernel sequence, this field specialization,
localized ideal norms, S-unit square classes and S-class two-torsion:
**not checked**. No absence is inferred. The proof is REPRODUCTION of
the assessed known machinery, with no claim of progress beyond the
sources checked.
