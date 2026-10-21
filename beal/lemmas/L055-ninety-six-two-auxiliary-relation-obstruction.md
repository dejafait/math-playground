# L055 — The two available auxiliary fields do not cover L96

## Hypotheses

Use L050's canonical identification of the twelve embeddings of K96
with the lines of E96[11] as a G_Q-set. Use L051's exact models

    m(U)=U^12-4U^11-264U^7+66U^6-132U^5-2112U^4
         -1320U^3-660U^2-6240U-8007,
    h(T)=T^3-4T^2-160T-1264,
    K96=Q(U), L96=K96(T), [K96:Q]=12, [L96:Q]=36.

Use L052's audited prime of K96 above 3 with ramification index eleven.
Use L054's cubic field F=Q(T) inside the same L96, with [F:Q]=3,
and its cited ramification tower and finite-Galois degree formulas.
No GRH-dependent arithmetic or normality of K96, F or L96 is assumed.

The canonical field identification is the unconditional structural
input of Freitas–Naskręcki–Stoll, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Mathematica **156** (2020), 77–113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019, Section 7.2, printed pp.25–28, Table 5.
The adjacent conditional class/Selmer computations are not inputs.

Import Fabrice Etienne, *Computing class groups by induction with
generalised norm relations*,
[arXiv:2411.13124v2](https://arxiv.org/pdf/2411.13124v2),
April 23, 2025, Definition 2.9 (printed p.15), Proposition 2.7
(pp.12–15), and Proposition 1.3, Definitions 1.8 and 1.10,
Lemmas 1.11–1.12 and Proposition 1.13 (pp.5–9).
These identify all composita with double cosets and all equivariant
permutation-module maps with their orbital incidence matrices.
Proposition 2.7 permits arbitrarily many copies of auxiliary modules.
Algorithm 4.1 and Theorem 4.2 (pp.23–24) implement the same full-map
test. Only that permutation criterion is used here.

## Conclusion

L96 admits no generalized norm relation over Q using only K96 and F,
including all conjugate composita and arbitrary map multiplicities.
The sum of the images of **all** auxiliary permutation-module maps
has dimension 14, whereas the target has dimension 36.

The complete compositum degrees over L96 are [1,11] for K96 and
[1,2] for F; the corresponding absolute degrees are [36,396] and
[36,72]. These are certified embedding-orbit degrees, not guessed
polynomial factorizations. This parks precisely this auxiliary pair.
It supplies no class/unit certificate, descent image, integer branch
exclusion, or Beal resolution. The independent critical audit below
confirms the obstruction without a mathematical correction.

## Proof

### The projective field action

Let M be the splitting field of m, and Gamma=Gal(M/Q) acting faithfully
on its twelve roots. L050 identifies this action with a subgroup of
PGL2(F11) on P1(F11); it is transitive since K96 is a field of degree
twelve. This uses the entire rational canonical fiber, not the local
twisted comparison or a polynomial-generator coordinate identification.

Choose a prime of M over L052's index-eleven prime of K96. Tower
multiplicativity makes its absolute ramification index divisible by
eleven. The Galois degree formula makes that index divide [M:Q].
The hypotheses and precise imported sources for these formulas are
in L054: Sutherland, 18.785 Fall 2021, Lecture 5, Lemmas 5.28 and
5.30, and Milne, *Algebraic Number Theory* v3.08, Theorem 3.34.
They apply here to the maximal integral rings and the finite Galois
extension M/Q. Thus eleven divides |Gamma|. Cauchy's theorem gives
an element of order eleven.

Such an element of PGL2(F11) is nontrivial unipotent. Indeed distinct
eigenvalues would lie in F121 and their ratio would have order dividing
120, which cannot give projective order eleven. A repeated eigenvalue
lies in F11 (it is half the trace); a nontrivial Jordan block has a
unique rational fixed line. Conjugate that line to infinity. The
cyclic order-eleven subgroup is then the entire translation group
U={x -> x+a : a in F11}. Transitivity supplies an element sending
infinity to a finite b. Conjugating U by it and translating b to zero
gives the entire lower-unipotent group V fixing zero. Unipotents fixing
zero have matrices, up to scalar, (1,0;c,1), so this is all V, not a
chosen proper subgroup.

The two elementary matrices u=(1,1;0,1), v=(1,0;1,1) generate
PSL2(F11). The certificate enumerates their generated permutations,
compares them with **every** square-determinant projective matrix, and
gets equality, with 660 elements. Hence Gamma contains PSL2(F11).
All projective matrices number 1320, so Gamma is PSL2 or PGL2.
This bounded exact verification is needed to certify this field's
image; no general subgroup classification or guessed closure group
is imported or reproved.

PSL2(F11) is perfect in this explicit action. With D=diag(2,6) in
SL2(F11), the commutators [D,u] and [D,v] are respectively u(3) and
v(2), because 2^2=4 and 6^2=3 modulo eleven. Each nonzero parameter
generates its full order-eleven root group. The certificate checks
both commutator identities and generation of all 660 elements by
them. Therefore the commutator subgroup contains all PSL2(F11).

### The actual common splitting field

L051's polynomial discriminants satisfy the exact identities

    disc(m)=-11*(5290873826226085383521697792)^2,
    disc(h)=-11*1936^2.

Both polynomials are separable. The Vandermonde product of their
roots squares to their discriminant and transforms by the sign of
the root permutation. Thus each sign character cuts out exactly
Q(sqrt(-11)). This is a polynomial discriminant argument; no
maximal-order discriminant or index is needed.

The certificate checks that the sign of every projective permutation
of twelve lines is its determinant square-class sign. In particular
PSL2(F11) acts by even permutations. Since disc(m) is nonsquare,
Gamma cannot be PSL2. Hence Gamma=PGL2(F11), and its sign kernel
is PSL2(F11). The irreducible cubic h has nonsquare discriminant,
so its splitting field N has group S3: its transitive group contains
a three-cycle, and the nontrivial sign supplies a transposition.

The intersection D0=M intersect N is Galois over Q. Its Galois group
is a quotient of PGL2(F11) and a quotient of S3. The image of the
perfect subgroup PSL2(F11) in this quotient is perfect. A quotient
of S3 has no nontrivial perfect subgroup: the subgroups of S3 are
trivial, C2, C3 and S3, whose derived subgroups are respectively
trivial, trivial, trivial and C3. Thus that image is trivial, and
the common quotient has order at most two. Both splitting fields
contain Q(sqrt(-11)), so D0 is exactly that quadratic field.

Milne, *Fields and Galois Theory*, v5.10 (September 2022),
[primary notes](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Proposition 3.21, printed pp.41–42, now identifies
Gal(MN/Q) with the full fiber product

    G={(g,s) in PGL2(F11) x S3 : sign(g)=sign(s)}.

Restriction is injective, and the compositum degree formula for two
Galois extensions gives its order 1320*6/2=3960, equal to the full
fiber-product order. Thus no element of that fiber product is missing.
All fields under consideration lie in this finite Galois overfield.

### Complete compositum maps and their images

Write A=P1(F11), B={0,1,2}. Since L96=K96F has degree
12*3=36, restriction of embeddings identifies its full embedding
set with X=A x B; the injection has equal finite cardinalities.
G acts on each coordinate through its two projections.

A G-equivariant linear map from Q[A] to Q[X] is a matrix constant
on G-orbits in X x A; similarly maps from Q[B] correspond to
orbits in X x B. This follows directly by applying equivariance
to matrix entries. The full certificate enumerates every such orbit
using all 3960 elements. There are two in each case, explicitly

    K96: a=a' and a!=a', with sizes 36 and 396;
    F:   b=b' and b!=b', with sizes 36 and 72.

There is also a direct completeness check: G contains
PSL2(F11) x A3. The first factor is doubly transitive on A, since
the translations in an infinity stabilizer act transitively on all
eleven finite points; lower unipotents supply transitivity on A.
The A3 factor is transitive on B. For X x A this gives exactly the
equal and unequal a-orbits. For X x B the A3 action gives equal b
and the two oriented unequal b-orbits; an odd element of the S3
projection interchanges the latter two. This gives precisely the
four orbital incidence maps above, with none omitted.

For a fixed target embedding, dividing each orbital size by 36
gives the stabilizer-orbit lengths [1,11] and [1,2]. By the imported
compositum/double-coset correspondence these give all factor degrees
over L96, with the specified embeddings, including both unequal
conjugate cases. Their absolute degrees are the orbital sizes.
The certificate saves every orbit pair and every incidence matrix.

The equal-a map sends f in Q[A] to the function (a,b) -> f(a).
The unequal-a map sends it to (a,b) -> sum_(a'!=a) f(a'), still a
function of a alone. The two b-maps similarly have images consisting
of functions of b alone. Their total image is consequently

    W={w(a,b)=f(a)+g(b) : f in Q[A], g in Q[B]}.

The two function spaces have dimensions twelve and three, and their
intersection is the one-dimensional space of constant functions.
Thus dim(W)=12+3-1=14. The equal maps already span W, so this is
the actual rank, not an upper bound from a selected set of maps.
For example the nonzero functional

    w(0,0)-w(0,1)-w(1,0)+w(1,1)

annihilates every image and does not annihilate the target basis
vector at (0,0). Equivalently the row-and-column sum-zero complement
has dimension (12-1)(3-1)=22. No irreducibility claim about that
complement is needed for the complete-map obstruction.

Every equivariant map from any number of copies of the two auxiliary
modules is a sum of maps just described. Its image is contained in W,
so it cannot surject onto the 36-dimensional target Q[X]. Apply
Etienne Proposition 2.7 and Definition 2.9 to obtain the conclusion.
This accounts for arbitrary multiplicities and all conjugate composita;
it is not a dimension comparison of the two displayed embedded fields.

Reproduce the finite arithmetic with

    python3 scripts/ninety-six-generalized-relation/coverage.py

Full evidence is in
`scripts/ninety-six-generalized-relation/coverage-certificate.json`.
It records every normalized projective matrix and action, all joint
group elements, complete orbits and maps, the exact rational row
reduction and annihilator, actual rank 14 versus required rank 36,
and an empty failures list. The field-to-group proof above is essential;
the finite certificate alone would not identify the actual fields.

This is REPRODUCTION under the prior SPECIALIZE assessment: an exact
application of the known full-map criterion, with field-specific finite
checks. No originality beyond the inspected sources is asserted.
The independently unresolved auxiliary arithmetic, saturation, torsion
lifts, support and norm maps, descent compatibility and full-disk
disjointness are not discharged. Alternative auxiliary fields remain
unassessed, rather than forbidden by this negative result.

### Independent critical audit — 2026-10-11

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-ninety-six-two-auxiliary-obstruction-audit.md`
covers precisely this audit. It confirms the stated obstruction; it
adds no stronger mathematical restriction or new auxiliary field.

**Actual fields.** L050's hypotheses and global fiber paragraph identify
the rational twelve-point Galois set, not merely its restriction to G_Q2.
FNS Section 7.2, printed p.25 and Table 5, supplies this unconditional
structural input; the local twisted-module argument alone would not
suffice. L051's degree 36 implies that h remains irreducible over K96,
hence over Q, as L054 proves. No irreducibility is inferred from a
discriminant. L052's coefficient valuations at 3 give the full Newton
polygon with vertices (0,1),(11,0),(12,0); its degree-eleven block has
root valuation 1/11, forcing ramification index eleven. The prime
is thus in the maximal ring, independently of the index of Z[U].
Lifting it to M and applying the Galois degree formula legitimately
forces 11 to divide |Gamma|.

For an order-eleven projective element with distinct eigenvalues,
their nonzero ratio lies in F121^* of order 120, a contradiction.
With repeated eigenvalue, invertibility and characteristic eleven
give a nonzero rational eigenvalue and a unique rational eigenline.
After moving that line to infinity the full order-eleven subgroup
is the upper root group. Transitivity moves its fixed line to b;
an upper translation by -b then moves that line to zero. The resulting
order-eleven subgroup is the entire lower root group. These operations
take place within Gamma after the initial change of coordinates.
The independently checked generation of PSL therefore applies to the
actual field group. D has determinant one, so both displayed
commutators lie in the derived subgroup of PSL itself. Their generation
of all 660 elements verifies perfectness, without assuming simplicity.

The audit recomputes both discriminants from the full polynomials
by exact rational elimination on their derivative Sylvester matrices.
They equal the stated nonzero -11 times squares, with the stated
square roots. Cycle parity independently agrees with determinant
square class on every normalized projective matrix. The Vandermonde
sign character therefore excludes PSL as Gamma and identifies its
quadratic subfield as Q(sqrt(-11)). The transitive cubic group is S3.
Any common Galois quotient of M and N is a quotient of S3, hence has
no nontrivial perfect subgroup. The image of PSL is perfect and must
be trivial; the quotient thus has order at most two. The shared
quadratic subfield gives equality. Milne Proposition 3.21 applies to
the two splitting fields in the same algebraic closure and yields the
full sign fiber product, of order 3960. No linear-disjointness claim
over Q or guessed closure group is substituted for this intersection.

**Complete actions and maps.** The 36 distinct embeddings of L96
restrict injectively to the 12 times 3 ordered pairs of embeddings of
K96 and F, since these two subfields generate L96. Equality of sizes
makes restriction bijective and G-equivariant. To check the saved
finite evidence independently, the audit constructs the joint action
by generator closure from

    (u,id), (v,id), (diag(2,1),(01)), (id,(012)).

The nonsquare determinant of diag(2,1) matches the transposition sign.
The generated set equals every one of the 3960 saved fiber-product
elements. Generator traversal, independently of the original all-group
orbit enumeration, recovers every pair in X times A and X times B,
their complete incidence matrices, and sizes 36,396 and 36,72.
It checks all concatenated matrix entries, pivot columns, full rational
reduced row-echelon matrix and annihilator. No JSON preview or selected
minor is used as verification of this full evidence.

There is also a direct check of orbit completeness: PSL is doubly
transitive on A and A3 transitive on B. For X times A their product
already has exactly the equality and inequality orbits. For X times B
it has one equal and two oriented unequal orbits; an element with odd
S3 projection interchanges the latter while its projective component
permutes A. Hence the four maps exhaust both Hom spaces. All their
columns are functions of just one coordinate. The equal maps contain
the entire spaces of such functions, whose intersection consists
exactly of constants: fixing b forces any equality f(a)=g(b) to be
constant in a, and then in b. The resulting exact rank is 14, while
the target dimension is 36. Arbitrarily many copies only sum these
same images and cannot surject. Etienne Proposition 2.7 applies in
the finite Galois overfield MN with precisely these stabilizers.
Its group-theoretic criterion has no class-completeness or GRH premise.

Run the independent check with

    python3 scripts/ninety-six-generalized-relation/audit_coverage.py

Full independently reconstructed evidence and comparison failures are
saved in `scripts/ninety-six-generalized-relation/audit-certificate.json`.
All checks pass, with actual rank 14 versus required 36 and zero
failures. The program imports neither the original program nor its
arithmetic routines; canonical field identifications remain cited
inputs, not conclusions of the finite program. The original certificate
is preserved. The only citation clarification is the explicit Milne
Proposition 3.21 locator; no mathematical correction or changed direct
lemma input is required. The pair-specific stop is confirmed. Other
auxiliary fields and all unconditional arithmetic/descent obligations
remain unresolved. This canonical audit supersedes the overview's
pending-review wording; the mathematical assembly in PROOF.md is unchanged.

## Mathlib

Full matching field-specific generalized-relation obstruction:
**not checked**. Supporting projective actions, finite groups,
Galois correspondence and permutation-module results: **not checked**.
Unknown coverage is not evidence of absence. Primary citations and
the complete finite certificate support this informal specialization.
