# L088 — The global cubic norm makes the thirteen-adic filter redundant on T

## Hypotheses

Use L069's entire fields K and D=K tensor_Q F, where

    F=Q(t)=Q(theta), t³−t²+t+1=0, theta=8−14t+6t²,
    [K:Q]=12, [F:Q]=3, [D:Q]=36.

Let W_S be exactly L074's subgroup of D*/D*² with even normalized
valuations at every maximal prime outside 2,11 and square D/K norm.
Negative valuations and localized ideal-class lifts are allowed.
Let T be exactly L084's subspace, with its rational full-local tests
and its entire primitive dyadic condition. In the latter use L082's
fixed fields and generator:

    K tensor Q2=Q2 × H, H=Q2(pi), pi^11=2,
    C=Q2(theta), J=H(theta),
    loc_2(T) subset {(1,1),(1,xi)},
    xi=[64+4pi^5+4pi^10−theta] in J*/J*².

At thirteen use L064's entire unramified degree-twelve field
U=K tensor Q13 and L087's ordering of D tensor Q13=U³: alpha
is the rational root theta=8 modulo 13, followed by beta,gamma.
Write nu for the nonsquare unit class of U. Then L087's exact
primitive image is J13={1,(1,nu,nu)}. No class-group value in D,
global realization of an arbitrary class, or integer solution is assumed.

## Conclusion

Every [z] in T satisfies

    [N_D/F(z)]=1 in F*/F*²,
    loc_13([z])_alpha=1 in U*/U*²,
    loc_13(T) subset J13.

Thus the additional thirteen-adic primitive filter is redundant on T:
T intersect loc_13^(-1)(J13)=T. In fact the first conclusion holds
on the larger subgroup of W_S defined by the primitive dyadic
condition alone; neither rational eleven-adic test is needed.
This is a specialization of the assessed norm machinery, not a new
general norm theorem. It supplies no smaller dimension bound, rank
bound or integer exclusion. The bounds 13+dim ker(n_S) and fourteen
remain unchanged. Independent critical audit completed on 2026-10-17
confirms the result without a mathematical correction.

## Proof

### Imported results and applicability

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-thirteen-global-norm-filter.md`.
Import William Stein, *A Brief Introduction to Classical and Adelic
Algebraic Number Theory*, May 2004,
[author PDF](https://wstein.org/papers/ant/ant.pdf), Section 5.2,
Corollary 5.2.3, p.28 (tower transitivity of element norm).
Import J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
norm definition and Proposition 4.1, pp.68–69 (principal ideal norm
and residue-degree weights), Proposition 8.2 and Corollary 8.4,
p.136 (entire completion algebra and localized norm). The fields
here have characteristic zero and are finite separable extensions;
no normality is required. Stacks Project
[Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
gives determinant norm compatible with base change, applicable to
these finite free field algebras, including their full tensor products.

For the unit norm reduction diagram use Milne, *Class Field Theory*,
v4.03, 6 August 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
III Proposition 1.2, Lemmas 1.3–1.5 and proof, p.98. For its finite
residue norm formula use Keith Conrad, *Finite fields*,
[author PDF](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf),
Theorem 4.6 and proof, pp.9–10, version accessed 2026-10-17.
Use the already assessed strict Hensel inequality from Pete L. Clark,
*Algebraic Number Theory II: Valuations, Local Fields and Adeles*,
[161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, p.58: v(P(a))>2v(P'(a)) gives a root. It applies
below in the complete dyadic field C, and at thirteen with unit
derivative. These general results are cited without reproof. The
specific norm comparison, support reduction and square tests below
are the difference not supplied by a general theorem.

### The norm of every supported class reduces to four possibilities

Take any representative z in D* of a class in W_S and put e=N_D/F(z).
For every finite prime p of F outside 2,11, the ideal norm identity is

    ord_p(e)=sum_{P over p} f(P/p) ord_P(z).

Every summand is even. This uses all extending primes and works for
negative exponents as well as positive ones. Form the fractional ideal
a of F with exponent ord_p(e)/2 outside 2,11 and exponent zero at
the supported primes. L077 proves ordinary class number one for the
maximal ring O_F, so a=d O_F for some d in F*. Then e/d² is an
S_F-unit. This does not require z to be an S_D-unit or its associated
localized ideal class to vanish.

Write N_D/K(z)=b² with b in K*. The two norm towers give

    N_F/Q(e)=N_D/Q(z)=N_K/Q(b)².

Dividing e by d² preserves this rational norm-square condition and
every local square class of e. L077's COMPLETE supported-unit kernel
therefore gives precisely the necessary possibilities

    [e] in {1,[v],[w],[vw]}, v=−1/t, w=2−t−6t².       (1)

This is an upper set, not an assertion that all four are D/F norms.
L077 retains the sign generator −1 and all primes over 2,11 in its
unit basis; no sign or supported valuation is lost in (1).

### The norm of the nontrivial primitive dyadic generator is square

L077 identifies O_C=Z2[s], s=t+1, with

    s³=4s²−6s+2, ord_C(s)=1, ord_C(2)=3,
    theta=28−26s+6s².

The three terms in theta have valuations 6,4,5, respectively. Put
kappa=64−theta. Then ord_C(kappa)=4. L082 proves kappa square in
J, using the order-five point 3T=2(4T). It is also square in C:
if r²=kappa in J, then [J:C]=11 and

    kappa=(N_J/C(r)/kappa^5)².

Thus this square descent uses an explicit odd-degree norm identity,
not a claim that nonsquares survive arbitrary even extensions.

Set zeta=pi^5 and c=4/kappa. Then zeta^11=32 and
pi=zeta^9/16, so J=C(zeta). Since [J:C]=11, the powers
1,zeta,...,zeta^10 are a basis. We have ord_C(c)=2 and

    N_J/C(kappa+4pi^5+4pi^10)
       =kappa^11 det(multiplication by 1+c*zeta+c*zeta²).       (2)

Here is a complete bound on that determinant, without a truncated
series or a sampled local point. In column j, 0<=j<=10, its three
entries have shifts d_j=0,1,2 and row j+d_j modulo 11. A positive
shift contributes c and crossing the last row contributes 32.
For a nonzero determinant term these rows form a permutation. Let
r count its positive shifts and k count its crossings. Equality of
the row and column sums gives

    sum_j d_j=11k, r<=11k<=2r.

The sole r=0 term is the diagonal term 1. Otherwise k is 1 or 2.
If k=1, r>=6, and the term ±c^r 32^k has valuation
2r+15k>=27. If k=2, necessarily r=11 and the valuation is 52.
All nonconstant terms are thus in the 27th maximal-ideal power of C.
Consequently the determinant is 1+e_C with ord_C(e_C)>=27.
Applying Hensel to X²−(1+e_C) at 1, with

    27>2 ord_C(2)=6,

shows that it is a square in C. The case e_C=0 is immediate.
Since kappa is square, (2) proves N_J/C(xi)=1 on square classes.

The entire dyadic base change for D/F is C × J. For a class with
localization (1,1) or (1,xi), its norm class is the product of the
first class and N_J/C of the second. Both products are 1. Hence

    [e]_C=1 for every [z] in T.                         (3)

No assertion about norm transfer of arbitrary Kummer classes is used.

### The four-element supported family injects at the dyadic place

In the same maximal basis L077 gives the exact expressions

    v=3−3s+s², w=−3+11s−6s², vw=1+2s².

All three are units. The square of any putative unit root A+Bs+Cs²,
where A is odd and A,B,C belong to Z2, has s coefficient
2AB−12BC−22C², which is even. Its s² coefficient modulo four is
B²+2C(A+C)=B² modulo four, hence is zero or one. These formulas
follow by reducing s³ and s⁴=10s²−22s+8. A square root of a unit
must itself be an integral unit, so these tests cover every root.
The odd s coefficients exclude v,w; the s² coefficient 2 excludes
vw. Thus only the identity in (1) can satisfy (3), proving

    [N_D/F(z)]=1 for every [z] in T.                     (4)

The argument in fact used only the primitive dyadic condition on W_S.
It imposed no new full-local condition at eleven.

### Accounting for the other finite and infinite places

The ideal argument covered EVERY prime outside support. At every
prime p over 2 or 11 the same norm and completion formulas retain
all factors, with no restriction on their normalized valuations.
At two both C and J were used explicitly. At eleven L086 records
the seven completions: (Q11,M), (Q11,M), (L,L,L), where
M=Q11(sqrt(−11)) and [L:Q11]=10. Regrouping by the places of F
gives Q11,Q11,L over its rational place, and M,M,L,L over its
quadratic place, with both embeddings of M in L retained. Their
norms multiply in the respective F completion. No factor is deleted
or required to lie in a Kummer subgroup: (1) already allows arbitrary
supported valuations, and the dyadic comparison alone forces (4).

For completeness F has signature (1,1) and K signature (2,5).
Over F's real place the complete D algebra is R² × C^5. At each
of the two real places of K the D/K norm is a real component times
a positive complex norm. Its being b² forces that real component
positive. Thus the D/F norm at the real place is positive. At F's
complex place the full algebra is C^12 and all classes are square.
This agrees with (1)'s rational norm-square sign restriction, and
no narrow-class or omitted-sign assumption enters the proof.

### The rational-root component at thirteen and the full filter

At the rational place of F above thirteen, theta maps to alpha.
The entire D/F completion there is U/Q13, not a chosen subfield
of U. By base change and (4), if z_alpha is the corresponding
component then N_U/Q13(z_alpha) is square in Q13. Support in W_S
makes its valuation 2m for an integer m, possibly negative. Write
z_alpha=13^(2m) u with u a unit of U. Its rational norm differs
from N(u) by the square 13^(24m).

The actual extension U/Q13 is unramified of degree twelve by L064.
The cited norm reduction diagram and finite-field formula give

    chi_13(N(bar u))
       = (bar u^((13^12−1)/(13−1)))^((13−1)/2)
       = bar u^((13^12−1)/2)=chi_(13^12)(bar u).

The left side is +1 because N(u) is a square. Hence bar u is a
square in the residue field. Odd-characteristic Hensel, with a
nonzero residue root and unit derivative, makes u square in U.
This proves [z_alpha]=1. Notice that a norm preserves this unit
quadratic character even in degree twelve; scalar restriction in
even degree would be a different map.

Both remaining components also have even valuation by support.
The D/K norm-square condition, localized to the entire U³, says
that their product with z_alpha is square. There are exactly two
unit square classes in U, so their two classes are equal. The
three-component class is therefore 1 or (1,nu,nu), exactly L087's
J13. All embeddings are retained: permutations induced by changing
the U-identification fix alpha and at most exchange beta,gamma.
Over F's quadratic thirteen-adic completion the corresponding full
norm is the product from the two U factors; no extra condition from
that tower is needed or assumed. This proves the stated containment
and redundancy, with no assumption that a T-class is a point class.

### Arithmetic evidence and limitations

Run `python3 scripts/thirteen-global-norm/check_norm.py`. It inspects
all 3^11 determinant choices, retaining all 201 nonzero permutation
terms in `scripts/thirteen-global-norm/norm-certificate.json`. All
nine checks pass. The complete formal determinant, with zeta^11=q, is

    1+q*(−11c^6+55c^7−77c^8+44c^9−11c^10+c^11)+q²*c^11.

The canonical proof above establishes the valuation bound for every
term independently of this collected polynomial. The certificate also
checks the diagnostic rational-root residues t=11, theta=8, v=7,
w=6 modulo thirteen. Both v,w are nonsquares there and vw is square;
the decisive result is their prior elimination as possible global
norms, not this residue comparison alone. The complete determinant
coefficient list was inspected. No numerical approximation is used.

This resolves the approved sufficient norm test positively but retires
J13 as an additional filter on the unchanged T. It does not compute
T itself, its S-unit intersection, the localized class kernel, the
eleven-adic image, or any integer lift. L086's five-probe obstruction
at eleven and the distinct five-isogeny survivor of L064 remain intact.
No complete Beal candidate follows. The completed classification is
REPRODUCTION; the independent critical audit below confirms this scope.

### Independent critical audit — 2026-10-17

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-global-cubic-norm-redundancy-audit.md`.
The audit confirms the conclusion without a mathematical correction.
It is a reproduction and verification of the field-specific application,
not an additional restriction or a new general norm theorem. The cited
Stein, Milne, Stacks, Conrad and Clark results above remain imported
inputs under the hypotheses checked here.

**Supported representatives and completeness.** L074 permits arbitrary
field representatives with even valuations outside the full support;
its norm condition means an actual element square in K. For each prime
of F outside support, every extending D-prime also lies outside support,
so the complete residue-degree weighted valuation sum is even. The
fractional ideal with these half-exponents has finite support, including
when some exponents are negative. Its principality follows from the
ordinary class number of F alone. Dividing by the square of a generator
leaves a supported unit and preserves both its field square class and
its rational norm-square property. No ideal class of D or K is killed
by assumption. The two tower equalities concern the same element z.

L077's maximality argument was checked: the translated polynomial is
Eisenstein at two, its local integral basis excludes index two, and the
square of any remaining global index must divide 44. The strict
Minkowski bound below two makes every ideal class principal. Its real
unit v is between 5/3 and 2 and satisfies the cited Conrad Corollary 4.6
criterion. The complete unit group is therefore generated by -1,v;
the three principal supported primes have generators s,a,b. Their
valuations and norms give the five independent supported square classes
and precisely the kernel {1,v,w,vw}. In particular sign and prime-eleven
classes are retained. No class-number or unit calculation in D is used.

**The square kappa and every dyadic norm factor.** L082's Kummer map
is the full [4x-theta] map, so its value at 3T=(16,60) is kappa.
L033's group law gives 4T=(5,-6) and 2(4T)=3T; thus the homomorphism
kills this double. The value is nonzero, since theta has valuation 44
in J while 64 has valuation 198. L069's field degrees and L082's
entire algebras give [J:C]=11. Taking the norm of a square root yields
exactly kappa=(N(r)/kappa^5)^2, proving squareness in C without an
even-degree square-descent assumption. In the maximal C-basis the
three valuations of theta are 6,4,5; hence ord_C(kappa)=4 and
ord_C(4/kappa)=2. Since pi^11=2, zeta=pi^5 satisfies zeta^11=32
and zeta^9/16=pi, so its eleven powers form the stated C-basis.

The determinant matrix has precisely the three entries per column
used in the proof. A permutation term has total shift 11k and at most
two row crossings; its positive shifts satisfy r<=11k<=2r. The sole
constant term is 1. For k=1 the minimum r is six; for k=2 every shift
is two, giving r=11. Thus every nonconstant term has valuation at
least 27 (or 52 in the latter case), before any cancellation. Clark's
strict inequality is 27>6, with derivative 2 at the unit 1. The full
D/F completion is C times J, of total C-dimension twelve. The first
square class is the identity and the second has square norm, so their
product is square. No degree-eleven factor substitutes for this whole
norm, and no local point approximation enters it.

**Injectivity and other places.** The maximal ring Z2[s] ensures that
every square root of a unit is A+Bs+Cs^2 with integral coefficients
and A odd. Reduction of its square gives s-coefficient
2AB-12BC-22C^2 and s^2-coefficient B^2+2AC+8BC+10C^2.
The latter is B^2 modulo four, since C(A+C) is even. Thus v and w
fail the first parity condition, and vw=1+2s^2 fails the second.
All three possible nonidentity global norm classes are excluded.
The argument uses no restriction at supported eleven-adic factors;
the regrouping of all seven factors in the proof accounts for degrees
12 over each F-completion. At a real K-place, the real factor times
a positive complex norm is a nonzero square, forcing the real factor
positive. Both real factors above F's real place are therefore positive;
all its complex factors have trivial square class. No narrow class
assumption or omitted sign is needed.

**Thirteen and the exact domain.** L064's audited irreducibility of
its full degree-twelve residual polynomial implies residue degree
twelve and ramification index one, so the relevant norm is the entire
unramified U/Q13 norm. L087 fixes the rational root alpha and the
remaining conjugate pair. Every component of any supported class has
even valuation at thirteen, allowing division by 13^(2m), even when
m is negative. Norming this divisor contributes 13^(24m), a square.
For the resulting unit the residue norm identity gives
chi_13(N(u))=chi_(13^12)(u). A square norm therefore forces a square
residue, and unit-derivative Hensel gives an actual square in U.
This is a norm statement, not scalar restriction into an even-degree
field. The other norm, D/K, then forces equality of the remaining
two square classes. Thus the entire class lies in {1,(1,nu,nu)},
under every permitted identification. Only the primitive dyadic
condition on W_S was needed; no ramified eleven-adic full-image
condition was added to L084's T.

**Complete arithmetic replay.** Run
`python3 scripts/thirteen-global-norm/audit_norm.py`.
The standard-library audit imports no construction code. It enumerates
all admissible row matchings, compares every field of all 201 stored
term records, and independently evaluates the matrix by exact Bareiss
elimination at 36 pairs (c,q). The determinant has degree at most eleven
in c and at most two in q (only the last two columns can contain q),
so the 12-by-3 grid also proves the collected polynomial identity.
Exact cubic arithmetic checks the generator identities, norms and
square-obstruction residues. All 22 checks pass, with the full evidence
in `scripts/thirteen-global-norm/audit-certificate.json`; the minimum
term bound is 27 against the required strict bound 6, with no failures.
The original nine success flags alone were not treated as verification.
The proof of supported completeness, the torsion/Kummer input and the
Hensel and norm implications are the mathematical checks above, rather
than conclusions inferred from that finite computation.

The audit accepts the specific redundancy stop in ATTEMPTS/039.
It does not compute T, its unit intersection, the localized class kernel
or loc_11(T), and changes neither dimension bound. The distinct
five-isogeny survivor and the five-probe obstruction remain intact.
There is no Beal candidate or integer exclusion.

## Mathlib

The full field-specific norm vanishing and redundancy result: **not
checked**. Supporting norm, completion, ideal and finite-field theorem
coverage: **not checked**. No absence or formal verification is claimed.
