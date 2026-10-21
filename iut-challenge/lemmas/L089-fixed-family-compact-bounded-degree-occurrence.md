# L089 — Compact bounded-degree occurrence in the fixed congruence family

## Hypotheses

Retain the entire fixed family of audited L086, before selecting a member.
In particular c,h=3^M,d_*,e_* are fixed integers, with M satisfying
L086's torsion and reduction precision. Write

    d=d_*+89h u, e=e_*+89h v, u,v in Z,
    E_(u,v): y^2=x^3+c x^2+d x+e,
    A=81d-27c^2, B=729e-243cd+54c^3,
    a=81*89h, b=729*89h, D=ab.

Use the algebraic closure Q-bar and the embedded local fields of L086.
Images at levels 120 and seven below mean images of the original curve
E_(u,v) over Q, with both coordinates of all torsion points retained.
They are not images of its Legendre descent over Q(t).

Let U=P^1_Q minus {0,1,infinity}, and let the standard Legendre map be

    J(t)=256(t^2-t+1)^3/(t^2(t-1)^2).

Define the two fixed domains, independent of R and of a family member,

    K_infinity={t in U(C): |J(t)|<=2000},
    K_2={t in U(Qbar_2): v_2(J(t))>=0},

where v_2(0)=+infinity and v_2(2)=1. Let K_V be the global parameter
set consisting of t in U(Q-bar) for which every complex conjugate lies
in K_infinity and every Q-to-Qbar_2 embedding of Q(t) sends t into K_2.
Its support is V={infinity,2}.

## Conclusion

These are allowed compact bounding domains in GenEll Example 1.3(ii),
including the requirement that each finite-local-extension intersection
be a compact domain. The domains themselves lie in U, as required by
IUT IV Remark 2.3.1(vi), and J(K_2) is contained in O_(Qbar_2).

There are infinitely many distinct rational j-values of members of this
unchanged family with both full images

    rho_120(G_Q)=GL_2(Z/120Z), rho_7(G_Q)=GL_2(F_7),

for which every ordered-root Legendre parameter belongs to K_V and
has degree at most six over Q. Consequently there are infinitely many
distinct such parameters in one fixed K_V. On each selected original
member all L086 local torsion, embedded H,N, split height-30 and
89-Frobenius conclusions remain valid for that same member.

This is an existential known-method specialization. It neither identifies
any new member with L087's member nor transfers L087–L088's field/native
conclusions. It is not a counterexample to Corollary 2.2 or an essential
IUT flaw. The separate step355 critical audit below validates this
specialization, with the source-version qualifications retained.

## Proof

### Imported results and their scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-20-corollary-2-2-compact-family-occurrence.md`.
Import Silverman, *The Arithmetic of Elliptic Curves*, second edition
(2009), III.1, p.45, and Proposition III.1.7(a)–(c) with its proof,
pp.49–50 ([primary book text](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf)):
the short-model invariant formula, the ordered-root Legendre
representation and the displayed J-map. These results concern geometric
isomorphism; they do not assert a Q(t)-defined comparison isomorphism.
The degree and domain verifications for these actual parameters are
given below, rather than inferred from a rational section of J.

L086 imports Zywina, *Elliptic curves with maximal Galois action on their
torsion points*, Bull. London Math. Soc. 42 (2010), 811–826,
[author-hosted version](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
Proposition 5.7 and proof, p.8, and the Q-case determinant criterion in
Lemma 2.4's proof, p.5. Reuse its assessed fixed-level cases at 120 and
seven. In particular, in the entire nonsingular integral short-coefficient
box max(|A|,|B|)<=R the union of the two exceptional sets has size at
most C R^(3/2) log R for fixed C and all sufficiently large R. A pair
outside that union has both full images over Q. No equidistribution in
the subrectangle or independence of the two images is imported or needed.

The domain conventions are imported from Mochizuki, *Arithmetic Elliptic
Curves in General Position*, Math. J. Okayama Univ. 52 (2010),
Example 1.3(i),(ii), pp.5–6
([journal PDF](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf)).
A compact domain equals the closure of its interior. At 2 this is tested
in every finite extension of Q_2; compactness of Qbar_2 is not asserted.
The open-U qualification is from IUT IV, April 2020, Remark 2.3.1(vi),
p.56, as inspected in the
[87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Author-byte and journal-version identity remain unverified; this is the
same qualified version as the source assessment. For local topology use
Milne, *Algebraic Number Theory*, v3.08 (19 July 2020), Proposition 7.46
and Corollary 7.47, p.126
([author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf)).
These known results are cited without reproof. The remaining argument
checks the constrained specialization, which none of them alone states.

### A positive count after the parity restriction

Restrict, for real R>=2, to

    R/2<=A<=R, -R<=B<=R, B odd.                 (1)

L086's exact affine lattice is

    (A,B)=(A_*,B_*)+(a u,-243c*89h u+b v).

Both a and b are positive, and b is odd since h is a power of three.
For every fixed u, therefore, exactly one residue class of v modulo
two makes B odd. There is no parity restriction on the permitted u.
The resulting B values, for that u, form a progression of step 2b,
with a center that may depend on u.

The A interval in (1) gives an interval of u of length x=R/(2a).
Let S be its number of integers. Then |S-x|<=2. For each of those u,
the permitted v progression in the B interval has count T_u satisfying
|T_u-y|<=2, with y=R/b. These interval error bounds hold for every
translation, including endpoints. The parameter map is injective by
L086's triangular lattice formula. Thus the count P(R) satisfies

    |P(R)-xy|
      <= sum_u |T_u-y|+y|S-x|
      <= 2S+2y <= 2x+2y+4,

and in particular

    P(R)>=R^2/(2D)-R/a-2R/b-4.                (2)

Every family member is nonsingular by L086's unit discriminant at 89;
also A>0 in (1) makes 4A^3+27B^2 positive. All counted pairs are in
the whole box to which the cited exceptional bound applies. The number
S_good(R) with both full images is therefore at least

    R^2/(2D)-R/a-2R/b-4-C R^(3/2)log R.        (3)

A sufficient strict threshold for positivity is

    C log R/sqrt(R)+1/(aR)+2/(bR)+4/R^2 < 1/(2D).   (4)

With every family constant fixed, the left side tends to zero and
the required right side is positive. In fact, by taking it at most
1/(4D), (3) gives S_good(R)>=R^2/(4D) for all sufficiently large R.
This compares the actual lower count and the required exceptional
threshold, without an effective R or a limit in h. The original
pointed Q-isomorphism of L086 transfers both full short-model images
to each original member counted by S_good(R).

All original congruences persist, since (1) only removes parameters.
L086's universal local-retention argument therefore applies separately
to each of these original members, with its own Tate parameter and
Frobenius lift. No old witness or previously constructed field is
renamed and no common Frobenius element for different curves is claimed.

### Uniform invariant bounds

The imported invariant formula gives, for every pair in (1),

    j=1728*4A^3/(4A^3+27B^2).

Since A>0 and B is a nonzero odd integer, 0<j<1728. In particular
j is neither exceptional value 0 nor 1728. At 2 the denominator
4A^3+27B^2 is odd. Therefore

    v_2(j)=8+3v_2(A)>=8.                       (5)

There is no cancellation issue: the valuation is computed on the
displayed rational quotient. These are bounds on the rational invariant
of each original curve. Every conjugate of any of its Legendre
parameters has this same invariant, so they give all-conjugate bounds,
not merely bounds at the selected embedding into Omega.

### The bounding domains in every required topology

The J-map extends to a morphism P^1->P^1 of degree six, given in
homogeneous coordinates [T:S] by

    [256(T^2-TS+S^2)^3 : T^2(T-S)^2 S^2].

The two entries have no common zero in characteristic zero. Its pole
fiber is exactly {0,1,infinity}; thus preimages of bounded finite-value
sets avoid every deleted point.

Over C the closed disk |z|<=2000 is closed in P^1(C), and P^1(C)
is compact. Its inverse image K_infinity is consequently compact and
contained in U(C). It is nonempty because J(-1)=1728, with strict
inequality, and proper because J has a pole at 0. It is invariant
under complex conjugation because J has rational coefficients. Points
with |J|<2000 are interior points. At a point with |J|=2000 the
holomorphic open mapping theorem applies to the nonconstant J on any
sufficiently small neighborhood avoiding its poles. Its image meets
|z|<2000, so every such neighborhood meets the interior of K_infinity.
This proves K_infinity equals the closure of its interior in U(C)
(and in P^1(C), since it is compact and avoids the deleted points).

Now fix any finite extension K/Q_2, embedded in Qbar_2. By Milne's
cited compactness result O_K is compact. The two continuous images
of O_K under z->z and z->1/z cover P^1(K), interpreting 1/0 as
infinity. Hence P^1(K) is compact. Also O_K is closed and open in
P^1(K): it is compact in a Hausdorff space, and its unit-radius
valuation ball is open in the affine chart. The morphism J induces
a continuous map on K-points. Consequently

    K_2 intersect U(K)=J^(-1)(O_K) subset P^1(K)

is compact, closed and open, and avoids {0,1,infinity}. Being open
and closed, it equals the closure of its interior. It is nonempty
for every K because -1 belongs to it and v_2(J(-1))=v_2(1728)=6.
It is proper for every K because t=32 has v_2(J(32))=8-10=-2.
The use of v_2 here is the extended absolute valuation; replacing it
by the surjective K-valuation does not change the integral condition.

The set K_2 is stable under Gal(Qbar_2/Q_2), since J is Q_2-defined
and the unique extended valuation is invariant under that group.
The same rational examples show K_2 itself is nonempty and proper.
This checks all finite extensions, rather than a single completion,
and supplies the exact uniform condition J(K_2) subset O_(Qbar_2),
with the integer N=0 in the cited corollary's condition. Thus the
two domains give one fixed allowed compactly bounded K_V with support
containing 2. No literal compactness of K_2 in Qbar_2 is used.

### Bounded degree and infinitely many moduli

For a counted original member let r_1,r_2,r_3 be its distinct roots
in Q-bar. Each ordered-root parameter

    t=(r_3-r_1)/(r_2-r_1)

belongs to its cubic splitting field, whose degree over Q is at most
|S_3|=6. Distinctness of the roots gives t!=0,1. The imported
ordered-root Legendre formula gives J(t)=j of that original member;
the possible extra square root needed for a geometric pointed
isomorphism is not adjoined to define t and does not enlarge Q(t).
For any embedding into C or Qbar_2, J of the image remains the same
rational j. The bounds above put every such image in its prescribed
domain. This proves t in K_V and [Q(t):Q]<=6 for every ordering.
The six-degree bound concerns t, not a later torsion field F.

Finally, equations must not be counted as distinct geometric moduli.
Fix any finite set F_j of rational numbers and let s be its size.
For one fixed j_0 with 0<j_0<1728 the invariant equation is

    27 j_0 B^2=4(1728-j_0) A^3.                (6)

For each integer A in [R/2,R], (6) permits at most two integer B.
Thus at most 2(floor(R)+1) pairs in (1) have that fixed j_0.
Values outside (0,1728) contribute no pairs. A union bound gives at
most 2s(floor(R)+1) pairs with j in F_j. This linear bound cannot
contain the quadratic number S_good(R)>=R^2/(4D) for arbitrarily
large R. Hence all good pairs together have infinitely many distinct
rational j-values. Any choice of an ordered-root parameter per such
member has infinitely many distinct values, since equal parameters
have equal J-values. This rules out repetitions and quadratic twists
as an explanation of the entire surviving count.

The proposed mechanism passes its bounded test: the required count
dominates both fixed-level exception sets, both local domains meet
every condition, and distinct moduli of degree-at-most-six parameters
occur in one common K_V. Its plausible downstream use is finite-set
avoidance in that same domain. Applying the native field screen to
later members, checking the corollary's full antecedent and choice
quantifiers, source-version authentication, possible field repairs,
essentiality and original finite B>=A all remain separate unresolved
tasks. No result beyond the checked source methods is claimed.

### Separate critical audit — 2026-10-20, step355

**Verdict and scope.** The conclusion passes the invocation-start
SPECIALIZE scope in
`drafts/literature/2026-10-20-compact-family-critical-audit-scope.md`.
The complete proof above and L086's family, retention and step341
audit were checked against the reused step351/338 source assessments.
No mathematical correction, new theorem, new hypothesis or new direct
lemma input is needed. The audit verifies the constrained application
of the cited results; it does not reprove their general statements.

**Parity, errors and the actual surviving members.** The congruence
for odd B is

    B_* -243c*89h u+b v = 1 mod 2.

Because b is odd, it has exactly one solution class for v for each
integer u, regardless of the parity of c or the offsets. Restricting
v to that class changes the B step to 2b and introduces no condition
on A. The A interval has u-length R/(2a), while the B interval of
length 2R has progression count R/b plus an error of absolute value
at most two, uniformly in its translated center. Thus, writing
x=R/(2a), y=R/b, the complete error is at most
2(x+2)+2y=R/a+2R/b+4, including the error in the number of rows.
This is exactly (2), not a density assertion within a moving sector.

All pairs are distinct by the triangular map and nonsingular by the
unchanged reduction at 89 (also by A>0). Both exceptional sets in
L086 concern the whole nonsingular short-coefficient box containing
this rectangle. Subtracting their union gives (3). After division by
R^2 its error is precisely the left side of (4); it tends to zero
with a,b,D,C fixed. Taking that error at most 1/(4D) proves the stated
lower bound R^2/(4D). Neither constants uniform in h nor an effective
threshold are required. L086's pointed Q-map and inverse transfer the
two full images to each original monic curve. Every counted member
retains the original congruences modulo h and 89; the universal local
210-module, embedded-field, split-reduction, height and Frobenius
arguments in L086 therefore apply to each separately. This invokes
no downstream field construction or common Frobenius lift.

**Invariant bounds and all conjugates.** Positive A and nonzero odd B
give 0<j<1728. The denominator 4A^3+27B^2 is odd, and the numerator
1728*4A^3 has 2-valuation 8+3v_2(A). Since A is a positive integer,
this is at least eight. The bounds concern the rational j itself,
so every embedding of every ordered-root parameter has that same J
value. There is no need to select a favorable conjugate or completion.

**Every domain condition.** The homogeneous numerator and denominator
of J have degree six and no common zero: the denominator vanishes only
at T=0, S=0 or T=S, where the numerator is nonzero. Hence the only
poles are the three deleted cusps. Over C the inverse image of the
closed disk is closed in compact P^1(C) and avoids those cusps. The
rational coefficients give conjugation stability. J(-1)=1728 is a
strict interior value and approaching the pole at zero gives points
outside the domain. At any boundary point, J is holomorphic and
nonconstant on a small connected disk without poles. The open mapping
theorem makes the image of every smaller such disk meet |z|<2000,
so the boundary point lies in the closure of the interior. Closedness
gives the reverse containment. This also verifies the topology in U.

For any finite K/Q_2, the cited theorem makes O_K compact. The affine
chart z and the reciprocal chart 1/z map O_K continuously into P^1(K)
and cover it, including infinity; thus P^1(K) is compact. The integral
ball is open in its affine chart and closed in the Hausdorff projective
line. The continuous J-map therefore has compact, open-and-closed
inverse image J^(-1)(O_K), entirely in U(K). It equals the closure of
its interior both in U(K) and in P^1(K). The rational points -1 and
32 give, respectively, valuations 6 and -2 of J, proving nonemptiness
and properness for every K, including K=Q_2. The unique extension of
v_2 is Galois invariant, which verifies local Galois stability on
Qbar_2. This checks the entire finite-extension quantifier; it never
asserts compactness of Qbar_2 or of K_2 itself. The bound on J(K_2)
is exactly integrality, so the required bound can use N=0. Both
domains and the support {infinity,2} were fixed before counting.

**Degree and genuinely distinct parameters.** A characteristic-zero
nonsingular cubic is separable. Its splitting-field Galois group acts
faithfully on its three roots, so the field degree is at most six.
The displayed root ratio belongs to this field and differs from zero
and one. Silverman's geometric formula identifies its J-value with
the original curve's j; the coordinate square root used for the
geometric isomorphism is not part of the parameter field. This proves
the degree and all-embedding claims for each of the six orderings.

For a fixed j_0 in the allowed interval, equation (6) has at most two
integer B for each integer A. There are at most floor(R)+1 possible
A in the rectangle. Thus any fixed s rational j-values account for
at most 2s(floor(R)+1) coefficient pairs, even before enforcing the
family congruences. For R sufficiently large this is less than
R^2/(4D), contradicting finiteness of all the good j-values. This
argument does not require the rectangles to be nested. Equal parameters
have equal J-values, so infinitely many distinct j-values yield
infinitely many distinct parameters. Repeated equations and twists
cannot exhaust the survivors.

The audit makes L089 a checked occurrence input for later finite-set
avoidance in the same fixed domains. It adds no conclusion beyond the
known methods used here. In particular, the April 2020 IV reproduction
remains unauthenticated against author/journal bytes. L087–L088 are
not transferred to later members or their fields, and all independent
initial-data, native-choice, field-repair, essentiality and original
finite B>=A obligations remain unresolved. No complete-solution
candidate, numerical certificate or formal verification is claimed.

## Mathlib

Full matching and supporting Mathlib coverage for this constrained
occurrence and these exact domains has not been checked. Unknown
coverage is not absence. The proof imports the named invariant,
Legendre, fixed-level exceptional and local compactness results with
the qualifications above. No numerical experiment, mathematical script
or formal verification is used.
