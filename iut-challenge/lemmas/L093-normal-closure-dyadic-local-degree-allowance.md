# L093 — The normal closure retains the dyadic local degree allowance

## Hypotheses

Fix any survivor of audited L089, retaining its original curve E/Q,
fixed c,h,d_*,e_*, both domains and the fixed algebraic closure.
Use audited L090's full-coordinate fields, for any of its six orderings:

    T=F_tpd=Q(E[2]),
    G_o=Q(t_o)(iota,E_o[15]), C_o=G_o^nor,
    T subset C_o subset M=Q(E[60]).

Let v be any actual place of T above two and w any place of C_o
above v. Completions use these places and compatible embeddings.
Keep d=6 and epsilon_d=1 in L092's qualified numerical context.

## Conclusion

Uniformly in the survivor, ordering and these actual places,

    v_2([ (C_o)_w : T_v ]) <= 10 = v_2(C_0),
    C_0=46080.

More strongly, for every place P of M above w,

    v_2([M_P:T_v]) <= 10.

Here v_2 on an integer is its exponent of two, not a valuation of a
local field element. This proves one sufficient degree input; it
neither proves a different estimate nor a complete normal-closure
repair. The result is a known-method specialization (REPRODUCTION).
The separate step372 critical audit below validates this bound, with
no claimed progress beyond the checked source methods or essential
IUT flaw.

## Proof

### Imported inputs and why a specialization is needed

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-20-normal-closure-local-two-degree-test.md`
and its completed source readings in
`drafts/literature/2026-10-20-normal-closure-local-two-degree-scope.md`.
Import Silverman, *The Arithmetic of Elliptic Curves*, second edition
(2009), VII.5.5, pp.197–199, with the residue-characteristic-two case
A.1.3/A.1.4(b), pp.412–413: integral j is equivalent to potential
good reduction. Import VII.7.1 and VII.7.3, pp.201–202: the
Neron–Ogg–Shafarevich criterion for a prime different from the residue
characteristic, and the finite-inertia criterion for potential good
reduction. These primary-book statements and relevant proof cases
were read at the [book reproduction](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves).
They are not reproved here. Their complete discrete valuation and
perfect-field/residue-field hypotheses hold for every finite extension
of Q_2 used below. E remains a nonsingular elliptic curve after each
base change, since it is such a curve over Q by L089.

Import Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
7.50–7.54, pp.127–129, and 7.58(a), p.131, for unramified extensions,
finite cyclic residue groups and the inertia quotient, and 8.10/8.13,
pp.139–141, for actual completions, decomposition groups and restriction
in towers ([author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf)).
Use finite Galois correspondence as in Milne, *Fields and Galois
Theory*, v5.10, Theorem 3.17/Remark 3.18, pp.39–40
([author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf)).
For the determinant use Silverman III.8.1(c,d)/Corollary 8.1.1,
pp.94–96, the Weil-pairing result already imported in L090.

These results do not state the displayed changed-field bound. The
small congruence-kernel and matrix-order arguments below check the
finite-level implementation for this tower. This is not a reproof of
the reduction criteria or reliance on the unread Serre–Tate scan.
No additional literature search, classification theorem, or numerical
experiment is needed.

### Actual completed fields and potential good reduction

Choose P above w, and put K=T_v, inside M_P through the actual tower.
L090 gives M=T(E[4],E[15]). Its completion is therefore exactly

    M_P=K(E[4],E[15])=K(E[60]).                 (1)

Indeed all coordinate images belong to M_P, as does K, giving one
inclusion. Conversely the right side is a finite extension of the
complete field K, hence complete and closed, and contains the image
of M. It therefore contains its completion M_P. All torsion points
here are the original E's full geometric torsion sets, transported
by the same embedding into an algebraic closure of K. No comparison
isomorphism with E_o over K is required for (1).

L089 gives v_2(j(E))>=8; in particular j(E) is integral in K.
Silverman's criterion gives potential good reduction over K. Put

    L_3=K(E[3]), L=K(E[15]) subset M_P.

These are finite Galois extensions, since the full coordinate sets
are stable under the absolute Galois group. Write I_K for absolute
inertia and rho_l for the representation on the free rank-two
l-adic Tate module of E over K. Potential good reduction implies
that Phi_3=rho_3(I_K) is finite.

### Three-torsion detects the joint odd-torsion inertia

We first verify that reduction modulo three is injective on Phi_3.
The kernel 1+3M_2(Z_3) has no nonidentity finite-order element.
For a nonidentity element write A=1+3^a B with a>=1 and at least
one entry of B a unit. The minimum entry valuation of A-1 is a.
If u is a positive integer prime to three, binomial expansion gives

    A^u=1+3^a(uB+3^a B'), B' in M_2(Z_3),

so its nonzero difference from 1 has the same minimum valuation a.
For any such matrix the cubing identity is

    (1+3^a B)^3
      =1+3^(a+1)(B+3^a B^2+3^(2a-1)B^3).

The parenthesis reduces to B modulo three. Thus cubing increases
that minimum by exactly one and does not give 1. For any proposed
finite order n=3^s u, apply first the u-power and then cube s times:
the difference has finite minimum a+s, contradicting A^n=1.
Every element of finite Phi_3 has finite order, proving injectivity.

Absolute inertia for L_3 is I_K intersect G_(L_3): both inertia
groups are kernels of the action on the same algebraic residue
closure, with the latter Galois group restricted to L_3. Its image
under rho_3 reduces to 1 modulo three by the definition of L_3.
The preceding injectivity makes that image trivial. By
Neron–Ogg–Shafarevich, E has good reduction over L_3. Applying the
same criterion at l=5 shows rho_5(I_(L_3)) is trivial as well.

Let D=Gal(L/K), viewed faithfully through the joint action as a
subgroup of GL_2(F_3) times GL_2(F_5). Its inertia subgroup I is
the image of I_K under this joint action, by local Galois restriction.
If an element of I has identity three-component, choose an inertia
lift g in I_K. That lift fixes E[3], so belongs to I_(L_3).
It acts trivially on E[5] by the preceding paragraph, and hence
its joint image is identity. Projection I -> GL_2(F_3) is injective.
This checks the common kernel; two unrelated bounds on inertia
at three and five would not establish it.

The determinant on E[3] is the mod-three cyclotomic character.
All third roots of unity are unramified over K. To see the applicable
local hypothesis explicitly, its residue field has size q=2^f.
Some finite residue extension has 3 dividing q^m-1. The corresponding
unramified extension of K has all three distinct residue roots of
X^3-1; their simple-root Hensel lifts are all its characteristic-zero
roots, since three is a unit. Inertia therefore fixes mu_3.
Consequently the injective projection has image in SL_2(F_3), and

    |I| divides |SL_2(F_3)|=24, v_2(|I|)<=3.    (2)

For completeness |GL_2(F_3)|=(9-1)(9-3)=48 by choosing independent
columns; determinant surjects onto F_3^* of order two, giving 24.
This retains the cyclotomic restriction, instead of using 48.

### The cyclic residue quotient, with both CRT factors checked

For q=3 or 5, every element of GL_2(F_q) has 2-primary order at
most eight. To verify this, let a matrix have order 2^s u with u
odd and raise it to u. The resulting matrix B has order 2^s and
is diagonalizable over the algebraic closure: its minimal polynomial
divides X^(2^s)-1, which is separable in odd characteristic.
The eigenvalues of a two-by-two matrix over F_q lie in F_(q^2)
(its characteristic polynomial has degree two). Both eigenvalues
therefore have orders dividing q^2-1. Diagonalizability makes the
order of B their least common multiple, so 2^s divides q^2-1.
Here

    v_2(3^2-1)=v_2(8)=3,
    v_2(5^2-1)=v_2(24)=3.

The order of an element of the product is the least common multiple
of its two component orders, whose 2-valuation is consequently at
most three. In particular this holds for every element of D.

The residue quotient D/I is cyclic of order f(L/K), since K and L
have finite residue fields. Choose any lift a in D of a generator
of this quotient. Then f(L/K) divides the order of a. The product
matrix bound proves v_2(f(L/K))<=3. Combining this with (2), and
the exact local degree identity [L:K]=|I| f(L/K), gives

    v_2([L:K])<=3+3=6.                         (3)

This does not multiply independently chosen unramified degrees for
three and five, and does not replace a local degree by ramification.

### The full four-division tower over the actual T_v

All E[2] is K-rational because T=Q(E[2]). It remains L-rational.
The faithful representation for L(E[4])/L therefore has image in
the reduction kernel

    ker(GL_2(Z/4) -> GL_2(F_2))
      ={1+2X : X in M_2(F_2)}.

There are exactly sixteen such matrices. Each is invertible (its
determinant is odd), and multiplication adds X modulo two. Thus
[L(E[4]):L] divides sixteen. Equation (1), followed by the actual
finite extension tower, yields

    v_2([M_P:K])
      =v_2([M_P:L])+v_2([L:K])<=4+6=10.       (4)

Finally K subset (C_o)_w subset M_P are the compatible actual
completions. The degree [(C_o)_w:K] divides [M_P:K] by the tower
formula, so (4) implies the claimed bound. There is no division by
the order-two global core: its membership in a decomposition group
is neither asserted nor needed. L092 supplies C_0=2^10*3^2*5,
so the achieved bound meets the specified threshold exactly.

The proof used only integral j, full two-torsion over T, and the
actual ambient containment from L090. All hold for every survivor
and ordering, and the argument allowed every v,w and extending P.
It assumes no equality of completions across places or orderings.

### Limits and known traps

This passes the bounded degree test and weakens the proposed local
obstruction to a normal-closure repair. It does not restore L092's
failed relative global allowance, establish sharpness, or show that
the source's complete different hypotheses hold. No lower-bound
witness, field-generation equality for the repair, alternate-prime
substitution or counterexample to a theorem is claimed.

Original finite B>=A, other primes, full different estimates, the
exact field prescription, repairs, height-selected prime, independent
initial data, native input/action/factorization/pilot and essentiality
remain unresolved. IV April-reproduction authentication/current-version
and the def= boundary retain their existing qualifications. This is
not a complete-solution candidate. The separate audit below validates
only this specialization, not the independent downstream hypotheses.

### Separate critical audit — 2026-10-20, step372

The invocation-start assessment
`drafts/literature/2026-10-20-normal-closure-local-two-critical-audit.md`
approves exactly this audit. The complete proof above was checked
against the already inspected theorem statements and proof cases in
the degree-scope assessment. No new source coverage, classification
or unread Serre–Tate result is used. The audit passes without changing
the statement, its proof mechanism or its direct mathematical inputs.

**Reduction hypotheses and actual fields.** L089's positive integral
A and odd B make the denominator of its rational j-expression odd;
1728*4 has two-adic valuation eight. Thus the same rational j is
integral at every place of T above two, not just the retained place
above three. Every K=T_v is a finite extension of Q_2, so it is
complete discretely valued, has characteristic zero and finite perfect
residue field. These hypotheses persist over L_3 and L. The cited
residue-two potential-good criterion is applicable; an odd-residue
Legendre criterion is unnecessary.

L090 establishes T=Q(E[2]) and T subset C_o subset M=Q(E[60])
for the same original E and every ordering. For a chosen actual P,
all fields are embedded in M_P. The finite field generated over K
by the full E[4] and E[15] coordinates is closed there and contains
the dense image of M. It is therefore M_P itself. Conversely those
coordinates and K lie in M_P. This checks both directions of (1),
without identifying the original E with a Legendre equation over K.
The compatible completion (C_o)_w is an intermediate field in this
same tower. No normality assumption on a randomly embedded subfield
or equality between different completions is being used.

**Finite inertia and the common kernel.** For a nonidentity matrix
1+3^a B, choose a to be its minimum entry valuation, so B is nonzero
modulo three. For every positive u prime to three, the first binomial
term uB remains nonzero modulo three and all subsequent terms vanish
there after factoring 3^a. In the cubing formula, a>=1 implies both
3^a and 3^(2a-1) are divisible by three. Its new leading matrix is
again B modulo three. Iteration therefore cannot yield the identity
at any positive finite exponent. This proves precisely the required
injectivity on the finite group rho_3(I_K); it makes no claim that
the entire three-adic representation has finite image.

Inside one local separable closure, I_(L_3)=I_K intersect G_(L_3):
both kernels require identity on the algebraic residue closure, not
merely identity on the finite residue field of L_3. Every element
of this intersection fixes E[3], so injectivity kills its entire
three-adic action. Silverman VII.7.1 then gives good reduction over
the complete field L_3. Applying it with Tate prime five, still
distinct from residue two, kills that same inertia group's five-adic
action. Thus any joint-inertia element with trivial three-component
has trivial five-component as well. This proves the claimed faithful
projection of I, rather than just separate bounds on its projections.

**Determinant and cyclic quotient.** The Hensel argument for mu_3
uses the finite residue field of K and a unit derivative, so its
roots lie in an unramified extension even if K/Q_2 is ramified.
The Weil pairing therefore gives determinant one on the three-part
of inertia. Its order divides 24 and contributes at most 2^3.
No determinant-one restriction is imposed on the whole group D.

For the two matrix-order checks, taking the odd-part power leaves
exact order 2^s. Its minimal polynomial is squarefree because
X^(2^s)-1 has nonzero derivative in characteristics three and five.
Its eigenvalues lie in F_(q^2), including the split and repeated-root
cases; hence its order divides q^2-1. The two valuations are three,
and the product uses a least common multiple, not a product. The
finite Galois inertia quotient D/I is cyclic. Every lift of a quotient
generator has order divisible by the quotient's order, whether or
not the extension of groups splits. This gives at most 2^3 for
the residue degree and at most 2^6 for [L:K].

**Four-division and the final bound.** Full E[2] is rational over
the actual K and therefore over L. The representation of
Gal(L(E[4])/L) on full E[4] is faithful, and its reduction is the
action on 2E[4]=E[2], which is trivial. The kernel has exactly
2^4 elements: 1+2X is invertible for each of the sixteen matrices X,
and distinct X give distinct matrices modulo four. Lagrange's
theorem bounds this extension degree by a divisor of sixteen.
The tower identities then give the achieved upper valuation
4+6=10, equal to the required allowance v_2(46080)=10. The
intermediate completion's degree divides the ambient degree.
The order-two global core is never cancelled locally.

All of these arguments apply to the arbitrary survivor and all
v,w,P in the hypotheses. Thus the uniform upper bound is certified;
neither sharpness nor a violating place is asserted. This audit
establishes availability of the local degree input, not progress
beyond the assessed known methods. It leaves the global relative
degree excess, normalized different estimates, exact generation,
source-version qualifications and the original finite B>=A gap open.

## Mathlib

Full matching and supporting Mathlib coverage for this completed local
specialization have not been checked. Unknown availability is not
absence. The proof imports the named reduction, pairing and local
Galois results with the precise hypotheses above. No mathematical
script, numerical certificate or formal verification is claimed.
