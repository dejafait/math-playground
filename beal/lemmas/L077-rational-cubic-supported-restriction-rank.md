# L077 — The rational-cubic supported family has combined restriction rank two

## Hypotheses

Use L033's degree-twelve field K and curve E0, L069's degree-36 field
D=K[θ] with g(θ)=0, and L076's supported norm-square unit space V_S,
where

    g(X)=X³−4X²−160X−1264,     S={all primes above 2 and 11}.

Inside D use L071's specified rational cubic

    F=Q(t),     f(t)=t³−t²+t+1=0,     θ=8−14t+6t².

Write U=O_F[1/22]* and U_Q=Z[1/22]*. Let

    B=ker(N_F/Q:U/U² -> U_Q/U_Q²),
    B_D=image(B -> V_S).

The existence and properties of this last map are justified below;
injectivity is not assumed. Fix L046's rational dyadic base place of K
and BOTH rational eleven-adic base places of L041. At each place use
the whole cubic algebra, its same distinguished θ and the full local
Kummer subgroup H_v for Y²=g(X). Let ρ be the combined localization of
B_D into the three square-class groups modulo their H_v.

No global point, primitive integer solution, unit basis in D, class
group computation or GRH assumption is made.

## Conclusion

The full supported group U has generators

    −1, v=t²−t+1=−1/t, s=t+1,
    a=9−7t+5t²=f'(t)/s², b=−4−8t−t²=11/a².

Their norms, in that order, are −1,1,2,11,11. Their square classes
form a basis of U/U². The full norm-square kernel B has basis

    [v], [w],     w=ab=11/a=2−t−6t²,     N(w)=121.

Scalar extension is injective on B, so dim B_D=2. Its combined
restriction ρ has rank TWO and kernel zero. On this family the two
eleven-adic restrictions coincide under their canonical identifications;
they are not independent conditions. Identifying each one-dimensional
local quotient image with F2, the combined matrix, with columns v,w,
is

    rational dyadic:       1 1
    first rational 11:    0 1
    second rational 11:   0 1.

Thus these tests remove at least two independent directions from the
full sixteen-dimensional V_S, giving an upper bound fourteen on its
filtered subspace. This does not meet L076's required upper bound
eleven, compute the localized class-norm kernel, bound the rank of E0(K),
or exclude a Beal branch. This is a field-specific reproduction of the
assessed complete-unit and local-restriction methods, not a claim of
progress beyond those methods. The independent critical audit below
confirms this result without a mathematical correction.

## Proof

### Imported inputs and why the specialization is needed

J.S. Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[author PDF](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 4.3, printed p.70, gives the Minkowski ideal-class bound;
Theorem 5.11 and its valuation-map proof, printed p.90, give the
S-unit structure. Keith Conrad, *Dirichlet's Unit Theorem*,
[27-page author PDF](https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf),
Corollary 4.6, printed p.9, states that in a cubic order with exactly
one real embedding a positive real unit v>1 is fundamental if
4v^(3/2)+24<=|disc(O)|. We import this criterion and do not reprove
its Artin inequality (Theorem 4.4, pp.8–9).

These theorems do not supply this field's complete generators or its
restriction rank. The necessary specialized maximality, prime
generators, norms and comparisons are proved here. Completeness cannot
be replaced by a search for small elements. For the local groups use
the already certified full images in L071 and L073. Their underlying
Kummer conventions are Denis Simon, *Computing the rank of elliptic
curves over number fields*, LMS J. Comput. Math. 5 (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.1,
Propositions 1.1–1.2, p.8. Their exact cardinalities use Barrera
Salazar–Pacetti–Tornaría, [arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Lemma 1.3 and Remark 1.4, p.4. No new point sample
is substituted for those complete images.

### Maximal order, class number and the complete ordinary unit

The polynomial discriminant of f is −44. Its derivative
3T²−2T+1 is everywhere positive over R, so F has signature (1,1).
L071's translate f(s−1)=s³−4s²+6s−2 is Eisenstein at two and
identifies O_(F⊗Q2) with Z2[s]=Z2[t]. Thus two does not divide the
global index [O_F:Z[t]]. The discriminant-index identity permits no
other prime in that index: its square divides 44. Hence

    O_F=Z[t],     disc(F)=−44.

For this cubic the Minkowski bound is

    (3!/3³)(4/pi) sqrt(44)=8 sqrt(44)/(9pi)<2.

Indeed sqrt(44)<27/4 and pi>3 give the strict inequality. Every ideal
class therefore has an integral representative of norm one and is
principal. This proves ordinary class number one; it is not an
uncertified backend assertion.

Since f(−3/5)<0<f(−1/2), its unique real root satisfies
−3/5<t<−1/2. The equation t(t²−t+1)=−1 gives an integral unit
v=−1/t with 5/3<v<2. Hence

    4v^(3/2)+24 < 4 sqrt(8)+24 <36<44.

Conrad's corollary applies to the now certified maximal order and makes
v a positive fundamental unit. F has a real embedding, so its only
roots of unity are ±1. Consequently O_F*={±v^n:n in Z}. This proves
completeness, not only that v is a small unit.

### All supported primes and complete supported generation

Let R be the unique prime above two. Total ramification gives
(2)=R³, residue degree one. The exact norm N(s)=2 implies (s)=R.
At eleven,

    f(T)=(T−6)(T−3)² modulo 11.

Because Z[t] is maximal, Dedekind factorization applies at eleven:
there are exactly Q=(11,t−6) and P=(11,t−3), both of norm eleven,
with

    (11)=Q P².

Exact reductions in Q[t]/(f) give

    a=9−7t+5t²,       a s²=f'(t),       N(a)=11,
    b=−4−8t−t²,       a² b=11,         N(b)=11.

Both a,b are integral. The residue of a at t=3 is zero, whereas its
residue at t=6 is nonzero. Since its absolute norm is the prime eleven,
(a)=P. The identity a²b=11 then gives (b)=Q. These are the entire
maximal-ring primes, not polynomial-order substitutes.

For any supported unit z, let its valuations at R,P,Q be k,l,m.
Then z/(s^k a^l b^m) has valuation zero at EVERY finite prime and is
an ordinary unit. Thus −1,v,s,a,b generate the full U, including
arbitrary negative valuations and torsion. Conversely a multiplicative
relation modulo squares first has even s,a,b exponents by those three
valuations; the remaining relation lies in the ordinary unit group.
The fundamental unit and −1 are independent there modulo squares.
If an ordinary unit is a square in F, its root has zero finite
valuations and is an ordinary unit, so no extra field-square relation
appears. Hence these five classes form a basis of U/U². The same
argument shows U/U² injects into F*/F*².

### Exact norm-square kernel and transport to D

The norms of −1,v,s,a,b are respectively −1,1,2,11,11. The target
U_Q/U_Q² has independent basis −1,2,11. Thus for exponents in F2,

    N((−1)^e v^i s^k a^l b^m) is square
      iff e=0, k=0 and l=m.

It follows that B has exactly the four classes 1,v,w,vw with
w=ab=2−t−6t² and norm 121. There is no omitted supported prime or
ordinary-unit direction.

L071 gives the invertible rational coordinate change between θ and t,
and L069 proves g irreducible over K. Therefore D is precisely the
base change K⊗Q F, with the same distinguished generator. The
determinant norm commutes with this base change (Stacks Project,
[Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)).
Every element of U and its inverse are integral over Z[1/22]; their
images and inverses are in O_D[1/22]. Their D/K norms are the same
rational numbers as their F/Q norms. In particular the images of
v,w lie in V_S, with norms 1 and 11², respectively. Norm squares here
are squares of supported units, as required. Injectivity of their
square classes is still to be proved; even degree [D:F]=12 does not
justify it.

### Both rational eleven-adic restrictions, including the zero entry

Under either rational base embedding K -> Q11 the entire cubic
D⊗_K Q11 is canonically F⊗Q Q11, preserving t and θ. Its factors
are Q11 (the prime Q) and M=Q11(sqrt(−11)) (the prime P), with
respective maximal-DVR valuations. This follows also by the local
factorization in L073; t=6 gives θ=8 modulo eleven and t=3 gives
θ=9 modulo eleven, matching its ordering. The field M has residue
F11 and ramification index two.

L073's full image is H11={1,h11}, with

    h11=[(g'(α),α−β)],     α=8 modulo 11,
    residues (1,10) in Q11 × M.

Both entries are units. In an odd residue characteristic complete
discretely valued field, a unit is a square exactly when its residue
is a square: necessity is reduction; sufficiency is simple-root
Hensel applied to Z²−u with a nonzero residue root. This applies to
both fields here. The local residues of v=t²−t+1, ordered Q,P, are

    (9,7).

The nonzero squares in F11 are {1,3,4,5,9}. Thus v's first component
is square and its second is nonsquare, exactly the class h11. In
particular ρ_11(v)=0, not just an assertion about even valuations.
Both full local images have the same generator and are respected by
the canonical identifications above; their restrictions on B coincide.

On the other hand, (w)=P Q by its exact generators, so its component
valuations in Q11 × M are (1,1). This uses ord_P, not the rationally
normalized valuation ord_11. Every class of H11 has even component
valuations. Hence w, and also vw, are outside H11; the rational-factor
valuation modulo two gives their nonzero quotient coordinate.
The local image of B in this quotient has precisely dimension one,
with row (0,1). This reasoning applies to each rational base place;
it gives two identical rows, not a second eleven-adic direction.

### The complete dyadic comparison

L071 identifies the full cubic with L=Q2[s], with maximal ring
Z2[s] and s³=4s²−6s+2. Its full Kummer image is H2={1,[h]}, where

    h=5−θ=−23+26s−6s².

Here v is the inverse of L071's u=−t and hence has the same square
class. The proved nonmembership in L071 gives ρ_2(v) nonzero. For
completeness the new products in this same maximal basis are

    v=3−3s+s²,          vh=−29+15s−3s²,
    w=−3+11s−6s²,      wh=−87+209s−86s²,
    vw=1+2s²,          vwh=−15−22s+36s².

All are units (their constant coefficients are odd). For any integral
square (A+Bs+Cs²)² the s coefficient is
2AB−12BC−22C², which is even. Thus v,vh,w,wh are all nonsquares.
This independently confirms w is also outside H2.

There is nevertheless an exact square-class relation: vwh is a
square in L. Indeed with r=1+s², a unit,

    r²=9−22s+12s²,
    vwh−r²=24(s²−1) in 8 O_L.

For the polynomial Z²−vwh, at r the valuation of the error is at
least 9 and that of the derivative 2r is 3, with ord_L(s)=1.
Thus 9>2·3 and Hensel–Newton gives an actual root in O_L. We use
Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, printed p.58 in the inspected 161-page version; this
is the already assessed Hensel theorem. No claim of root existence is
based only on a residue sample.

Consequently [vw]=[h], so ρ_2(v)=ρ_2(w) is nonzero and ρ_2(vw)=0.
The dyadic row on this family is exactly (1,1). In particular a
nonzero eleven-adic row cannot be inferred independent merely from a
different local nonmembership witness; its zero on v was essential.

### Injectivity, combined rank and the remaining threshold

If v^i w^j is square in D for i,j in F2, localizing at a rational
eleven-adic base place forces j=0 by its rational-factor valuation.
Localizing at the fixed rational dyadic place then forces i=0 because
v is nonsquare there. Hence scalar extension on B is injective. The
three quotient maps are well-defined on B_D because squares in D
localize to squares, and each H_v is a Kummer subgroup. Their actual
matrix is the one in the conclusion. Its first two rows have determinant
one over F2. Therefore rank ρ=2 and ker ρ=0 on the full family.

The same combined map on the full V_S has rank at least two by this
restriction to B_D, so its kernel has dimension at most 16−2=14.
L076 requires at most eleven even before the uncomputed localized
class contribution of L074. Two certified removed directions are
therefore progress toward that necessary test, not a sufficient
descent bound. Other S-units, class-norm kernel, other local conditions
and global point/primitive integer lifting remain independent gaps.
ATTEMPTS/032–033 retain their stated obstructions; we neither keep
all unit classes nor delete eleven from support.

### Arithmetic certificate and qualifications

Run `python3 scripts/rational-cubic-supported/check_rank.py`. Its full
certificate is `scripts/rational-cubic-supported/rank-certificate.json`:
23/23 checks pass. It records exact rational multiplication, norms,
all 32 supported square-class exponent choices and the four-element
norm kernel, all 256 unit residues modulo eight and their squares,
all relevant local residues and the complete restriction matrix.
The proof above, rather than the finite table alone, supplies
maximality, unit completeness, actual Hensel lifting and the local
image theorems. For the only positive dyadic square claim the explicit
root approximation r and error valuation are given above; the complete
table is supporting reproducible arithmetic.

The initial certificate, preserved at
`scripts/rational-cubic-supported/initial-rank-certificate.json`, has
20/22 checks passing. Its failed provisional expectation was that w
itself belonged to H2; the associated rank-output check consequently
also failed. The corrected full computation proves w outside H2 and
vw inside H2. Rank two does not require w in H2. This was a corrected
local expectation within the calculation, not a hidden source failure
or a negative rank result. No result depends on Python sympy, GP or
Sage, which were unavailable in the attempted environments.

### Independent critical audit — 2026-10-16

The audit uses the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-16-rational-cubic-supported-rank-audit.md`.
It accepts the entire statement, including generation and both local
quotient coordinates. General theorems remain imported; the following
checks certify their specialization and the finite arithmetic. This is
independent verification of a notebook input, not a new general theorem.

**Completeness and exact support.** The resultant calculation gives
disc(f)=−44. The translate f(s−1) is monic Eisenstein at two, with
constant −2; Clark's Proposition 2.9/Corollary 2.10 gives the full
local integer ring Z2[s]. Milne, *Algebraic Number Theory*, v3.08,
Remark 2.25, p.34, gives the squared-index discriminant identity.
An index prime would therefore have to be two, which the local
maximality excludes. Thus Z[t] is the maximal global order. The
negative discriminant and positive derivative give the signature
(1,1); the unique real root lies between −3/5 and −1/2, with
endpoint polynomial values −22/125 and 1/8. The unit v=−1/t is
therefore between 5/3 and 2. Conrad's Corollary 4.6 applies with
4v^(3/2)+24<36<44. Its positive fundamental unit, together with −1,
is the full ordinary unit group. The real embedding excludes additional
roots of unity. Milne's Theorem 4.3 also proves class number one because
8sqrt(44)/(9pi)<2, although the explicit prime generators already suffice
for the supported generation argument.

Milne's Theorem 3.41 and proof, pp.62–63, applies to the now maximal
monogenic order, including the repeated factor at eleven. The exact
coefficient factorization is (T−6)(T−3)^2 modulo eleven. Thus the full
support is R,P,Q with (2)=R^3 and (11)=P^2 Q. The determinants give
N(s)=2 and N(a)=N(b)=11. The residues of a at t=3,6 are 0,4,
so (a)=P; a^2b=11 implies (b)=Q, and (s)=R. Negative valuations
are allowed. Dividing any supported unit by its corresponding powers
of s,a,b leaves an ordinary unit. Conversely each supported valuation
separates its generator modulo squares, and an ordinary unit that is a
field square has an ordinary-unit square root. This verifies both
generation and independence of all five classes, without inferring a
basis from the S-unit rank alone.

**Kernel and transport.** All 32 products of the actual norms were
recomputed. Precisely the four exponent vectors (0,i,0,j,j) have square
norm, giving 1,v,w,vw. The coordinate identities identify the same F
and theta as L071; L069's rational five-adic place excludes a root of
g over K, so D=K tensor_Q F is the whole degree-36 field. Both an
S-unit and its inverse remain integral over Z[1/22] after inclusion in
D. Determinant norm base change then gives norms 1 and 121 in K,
squares of supported units. Thus this is the actual V_S of L076,
not a group with a different support or a scalar quotient. This
argument alone does not assert square-class injection.

**Whole local images and the two rows.** The relevant L041 and L046
proofs supply the actual rational base embeddings, via simple Hensel
roots, and retain all complementary factors. Tensoring at any such
embedding preserves the specified t and theta. L071 and L073 supply
full Kummer images, proved using the cited image-size theorem and
nontrivial exact point classes; their previous canonical audits were
checked at these load-bearing arguments. The two rational eleven-adic
algebras have ordered factors Q11 and M, of residues t=6 and t=3.
Here v has residues (9,7), while h11 has residues (1,10). Both
components of v/h11 have square residue: 9 and 7/10=4 modulo eleven.
The unit derivative in the odd-prime square-root Hensel test proves
[v]=h11 in the full product, rather than merely equality of valuations.
The exact ideals give w valuations (1,1); both full H11 classes have
even valuations. The eleven-adic quotient row is therefore (0,1).
The two base embeddings induce the same map on F and the same curve,
so both rows coincide. They are not counted as two independent tests.

At two, the full maximal ring has basis 1,s,s^2 and ord(s)=1,
ord(2)=3. The six monomials in a general square were independently
expanded; its s coefficient is always even. The four elements v,vh,w,wh
have odd s coefficients, so none is a square. A root of a unit must
itself be an integral unit, which justifies applying this coefficient
obstruction to all possible roots. For the positive claim the audit
checks r=1+s^2, r^2=9−22s+12s^2, and
vwh−r^2=24(s^2−1). Both r and s^2−1 are units. The error therefore
has exact valuation nine and the derivative 2r exact valuation three.
Clark's Theorem 1.79 applies with 9>6 and produces a genuine square
root. Thus [vw]=[h] and the dyadic quotient row is (1,1). A finite
square residue is never used as a substitute for this lifting step.

If v^i w^j became square in D, the rational eleven-adic component
valuation would force j=0; the rational dyadic nonsquare then forces
i=0. This verifies scalar-extension injection without an unjustified
even-degree preservation rule. The quotient maps are well-defined and
linear. Independent elimination on the full matrix gives rank two.
Its restriction to B_D therefore forces rank at least two on V_S;
L076's verified dimension sixteen gives the stated upper bound fourteen.

**Complete evidence and limits.** Run
`python3 scripts/rational-cubic-supported/audit_rank.py`.
The full certificate is
[scripts/rational-cubic-supported/audit-certificate.json](../scripts/rational-cubic-supported/audit-certificate.json).
All 43 checks pass. The implementation uses polynomial long division
and permutation determinants, imports no original checker code and
neither executes nor overwrites either original certificate. It compares
every one of their 256 square-table records, every saved target and
root match, all generator/norm/kernel/residue fields and the final
matrix and thresholds with independent arithmetic. SHA-256 hashes of
both source certificates are retained. All 32 norm choices, the exact
Hensel values, matrix and initial failure fields were also inspected
in full. Symbolic identities and theorem applicability above supply
the infinite and completeness claims; these are not success-flag claims.

The initial 20/22 record really failed `w_in_full_H2` and the dependent
matrix check, leaving its rank unset. Its underlying arithmetic agrees
with the replay. The final 23/23 record correctly changes the relation
to vw in H2; neither historical file is discarded. There is no correction
to the final mathematical argument and no new DAG input. The verified
rank is two against the second-direction target two, while the filtered
unit upper bound fourteen still exceeds eleven. The localized class
kernel, remaining unit directions, useful rank and primitive integer
lifting remain unresolved. ATTEMPTS/032–033 remain valid in their
original scopes; no complete Beal candidate or branch exclusion follows.

## Mathlib

The complete matching supported-generation and combined restriction-rank
result, and coverage of the supporting maximal-order, Minkowski,
fundamental-unit, S-unit, local-square and Kummer theorems: **not
checked**. No absence is inferred. The precise cited inputs above
and L071/L073's full local images are used as informal mathematics;
no Lean verification or new general theorem is claimed.
