# L125 — A positive-mass obstruction to the two-core full-law coupling

## Hypotheses

Let H be a set of size 1024, let K have size 60, and choose distinct
a,b outside K. Write C=K union {a}, C'=K union {b}, and
Y=H minus (K union {a,b}). Use exactly L030's construction, with
q=137,

\[
T=\{16,64,70,102,112,118,121\}\subset\mathbb F_{137},\qquad
\Omega=(T\times\mathbb F_{137})\sqcup D_0,\quad |D_0|=4,
\]

and the family P={B_p: p in F_137[X], deg p<=2}, where
B_p={(x,p(x)):x in T}; the zero polynomial is included. On C's side
sample a uniform bijection sigma:Omega -> H minus C and output
F_C={C union sigma(B_p):p in P's polynomial index set}.
On C' use an independently specified marginal of exactly the same
form, with a uniform bijection sigma':Omega -> H minus C'. No
independence between the two sides of a proposed coupling is imposed.

The required relation between the output families is:

1. For every 68-subset S containing C union C', its selection
   indicators in F_C and F_C' are equal.
2. Any two distinct supports in F_C union F_C' have intersection
   at most 63. Equal supports are identified, not forbidden.

These are full pushforward marginal laws, not uniform distributions
on distinct outputs and not just prescribed moments. L030 supplies
their separate local feasibility. In the RS application the bound 63
is the support-packing restriction explained in L001 and L027; here
it is an explicit hypothesis of the proposed relation.

## Conclusion

No coupling of these two full laws is supported on that relation.
In fact, the set E of left output families that have a representing
bijection with sigma^{-1}(b)=(16,y_0) for some y_0 has probability
at least 137/963, and no member of E has an allowed right partner.
This is an exact positive-mass Hall-event obstruction.

This excludes only this prescribed two-core law. It does not exclude
other local laws, bound all support packings, realize a received word,
or decide arbitrary-center 67/68 safety. The bracket 955–957 remains
unchanged. The separate critical audit below accepts this restricted
obstruction; it is not a complete challenge candidate.

## Proof

**Source scope and why a specialization is necessary.** The unchanged
pre-invocation [SPECIALIZE assessment](../drafts/literature/2026-10-25-two-core-full-law-compatibility.md)
covers the two-core laws, common-support events and one symbolic
cross-intersection refinement. The finite supported-coupling criterion
is Koperberg, *Couplings and Matchings: Combinatorial notes on
Strassen's theorem*, [arXiv:2202.02092v1](https://arxiv.org/pdf/2202.02092v1),
4 February 2022, Theorem 1, p. 2, and Proposition 4, pp. 5–6,
as recorded in [the primary source note](../foundations/16-finite-supported-coupling-source.md).
It applies to the finite sets of output families and their pushforward
probabilities, with the required relation above. We do not reprove
that theorem. It does not decide this instance: the difference proved
below is that N(E) is empty although P(E)>0. The elementary rigidity
argument concerns this exact polynomial star and is written in full;
no classification theorem for arbitrary orthogonal arrays is assumed.
L051's all-core obstruction is only a contrast and is not used.

**The distinguished-point projection.** Each point (t,y) of the
959-point active part of Omega lies in q^2=18769 blocks: fixing
p(t)=y is one nonzero linear equation on three coefficients. Each
point of D_0 lies in none. Therefore the degree of b in the residual
family on C's side has distribution

\[
\Pr(d_b=0)=4/963,\qquad
\Pr(d_b=18769)=959/963.
\]

The same distribution holds for d_a on the other side. Common-support
indicator equality forces d_b=d_a. The counts alone do not obstruct
coupling. We now use the entire common star and one cross-family
intersection refinement.

Fix a left output in E and one representing sigma with
sigma^{-1}(b)=(t_0,y_0), t_0=16. A proposed right partner must have
sigma'^{-1}(a)=(t_1,y_1) in the active part: the right common star
has the same positive degree. Put S_i=T minus {t_i}. The shared
68-supports, with K,a,b removed, are exactly the same family of
six-subsets of Y on both sides:

\[
\{\sigma(B_p\setminus\{(t_0,y_0)\}):p(t_0)=y_0\}
=
\{\sigma'(B_r\setminus\{(t_1,y_1)\}):r(t_1)=y_1\}.       \tag{1}
\]

**Recovering columns from the common star.** Its used points are
precisely the six columns S_i times F_q, after the respective labeling.
For each x!=t_i and each value z, the equations p(t_i)=y_i and
p(x)=z have q solutions, so all these points occur. Any two points
in different columns occur in exactly one star block, by unique
quadratic interpolation at the three distinct arguments t_i,x,x'.
Two distinct points in the same column never cooccur. Consequently
the six column classes are intrinsic to the common family: among its
used points, a point together with all its non-cooccurring points is
exactly its column. Equation (1) therefore induces a permutation of
the six columns and bijections of their q individual symbols.

Normalize a used point (x,z) on side i by replacing its symbol with
(z-y_i)/(x-t_i). Since p(t_i)=y_i exactly when
p(X)=y_i+(X-t_i)(uX+v), the normalized star is

\[
\mathcal A(S_i)=\{\{(x,ux+v):x\in S_i\}:(u,v)\in\mathbb F_q^2\}.
\tag{2}
\]

The identity on the actual used labels in Y, viewed from left to
right, is thus an isomorphism from A(S_0) to A(S_1) of the form
(s,z) -> (tau(s),f_s(z)), where tau:S_0 -> S_1 is a bijection and
each f_s is a permutation of F_q. There is a bijection Phi on F_q^2
of coefficient pairs satisfying

\[
f_s(us+v)=u'\tau(s)+v',\qquad (u',v')=\Phi(u,v).            \tag{3}
\]

**All the symbol permutations in (3) are affine.** Choose three
distinct s_1,s_2,s_3 in S_0, and write t_j=tau(s_j). Set
X=us_1+v, Z=us_2+v. These are independent coordinates because
s_1!=s_2. Define

\[
A=\frac{s_2-s_3}{s_2-s_1},\quad B=\frac{s_3-s_1}{s_2-s_1},
\qquad
A'=\frac{t_2-t_3}{t_2-t_1},\quad B'=\frac{t_3-t_1}{t_2-t_1}.
\]

All four coefficients are nonzero and A+B=A'+B'=1. Equation (3)
implies, for every X,Z,

\[
f_{s_3}(AX+BZ)=A'f_{s_1}(X)+B'f_{s_2}(Z).                 \tag{4}
\]

Subtract values at zero, writing h_j(w)=f_{s_j}(w)-f_{s_j}(0).
The zero instance of (4) makes the constants cancel. Setting Z=0
or X=0 gives h_3(AX)=A'h_1(X), h_3(BZ)=B'h_2(Z). Substitution
back in (4), and the nonzero A,B, give
h_3(U+V)=h_3(U)+h_3(V) for every U,V in F_137. Since this is the
prime field, repeated addition gives h_3(w)=c w, where c=h_3(1)
is nonzero because h_3 is a permutation. The two preceding identities
make h_1,h_2 nonzero scalar maps. For any other s in S_0 the same
interpolation equation using s_1,s_2,s, with Z=0, shows that f_s is
affine with nonzero slope. This covers all six symbols; no continuity
or unjustified linearity of an arbitrary permutation is used.

Write f_s(z)=alpha_s z+beta_s. Taking the two coordinates s_1,s_2
in (3) shows

\[
\Phi(u,v)^t=M(u,v)^t+d
\]

for an invertible 2-by-2 matrix M over F_q and a column d. Invertibility
follows also from Phi's bijectivity. Comparing linear and constant
parts of (3) yields

\[
\alpha_s(s,1)=(\tau(s),1)M,\qquad
\beta_s=(\tau(s),1)d.                                    \tag{5}
\]

Writing M=(m_ij), the second component of the first equation is
alpha_s=m_12 tau(s)+m_22 !=0. Hence

\[
g(t)=\frac{m_{11}t+m_{21}}{m_{12}t+m_{22}}
\quad\hbox{satisfies}\quad g(\tau(s))=s.                   \tag{6}
\]

This is an invertible projective map, finite at all points of S_1,
mapping S_1 onto S_0. The prime-field step is essential; no assertion
for arbitrary extension-field symbol permutations is being made.

**The exact finite rigidity test.** For this T and t_0=16 the only
invertible projective map taking T minus {t_1} onto T minus {16},
for any t_1 in T, is the identity with t_1=16. The complete certificate
is `scripts/finite-support/two-core-star-rigidity.json`, reproduced by
`python3 scripts/finite-support/two_core_star_rigidity.py`.
The enumeration and its completeness are as follows.

For each of the seven choices of t_1, take the first three elements
x_1,x_2,x_3 of the sorted source six-set. An invertible projective map
must send them to an ordered triple of distinct points in the target
six-set: 6*5*4=120 possibilities. Such a triple determines the map
uniquely. Explicitly, the matrix

\[
H(x_1,x_2,x_3)=
\begin{pmatrix}
x_2-x_3&-x_1(x_2-x_3)\\
x_2-x_1&-x_3(x_2-x_1)
\end{pmatrix}
\]

maps those three points to 0,1,infinity and is invertible. A map
with target triple y_1,y_2,y_3 is represented by
H(y_1,y_2,y_3)^{-1}H(x_1,x_2,x_3). Uniqueness follows because an
invertible projective map fixing 0,infinity is a nonzero scaling,
and fixing 1 forces that scale to one. Every map under consideration
is therefore one of exactly 7*120=840 enumerated candidates.

For each candidate the program independently solves the three linear
equations A x_i+B-y_i C x_i-y_i D=0 by modular elimination. It checks
rank three, equality of the two matrices after normalization by the
first nonzero entry, nonzero determinant and all three anchor images.
It then evaluates all six source points, retaining poles explicitly as
null, and tests exact equality with the destination set. Full matrices,
all six images, the checks and the acceptance decision are saved for
every candidate. The exact result is:

| Removed t_1 | Candidates | Accepted matrices, normalized |
| --- | ---: | --- |
| 16 | 120 | (1,0,0,1) |
| 64 | 120 | none |
| 70 | 120 | none |
| 102 | 120 | none |
| 112 | 120 | none |
| 118 | 120 | none |
| 121 | 120 | none |

All 840 candidates pass both-construction and anchor checks, with zero
failures. The sole accepted record has source and images
(64,70,102,112,118,121), determinant 1, and matrix (1,0,0,1) by both
methods. Its complete record and the empty failure list were inspected.
The computation examines every potential map, not random isomorphisms
or a factorial family state space. The preceding symbolic argument is
necessary to infer rigidity of the original arbitrary star isomorphism.

**The forced cross-family conflict.** Applying the test to (6) gives
t_1=t_0=16, tau(s)=s and M=lambda I for some lambda!=0. Write
d=(u_0,v_0)^t. Thus the normalized symbol correspondence from left
to right is

\[
z\longmapsto\lambda z+u_0s+v_0.                            \tag{7}
\]

Choose any polynomial p of degree at most two with p(16)!=y_0,
for example the constant y_0+1. Define

\[
r(X)=\lambda p(X)+(X-16)(u_0X+v_0)+y_1-\lambda y_0.        \tag{8}
\]

This is a polynomial of degree at most two and
r(16)-y_1=lambda(p(16)-y_0)!=0. By undoing the normalization in
(7), the actual six labels sigma(s,p(s)), for s in T minus {16},
are precisely sigma'(s,r(s)). Both corresponding full supports
therefore contain K and these six labels. The left support contains
a but not b, and the right contains b but not a, so they are distinct.
Their intersection has at least 60+6=66 points, exceeding the required
63. The remaining residual point on either side lies outside the
used six-column star; whether those two points coincide can only
increase this intersection, and is immaterial. This contradicts
the allowed relation for every proposed right partner.

**The full-law obstruction, retaining all output probabilities.** For
a uniform left bijection, sigma^{-1}(b) is uniform on Omega. The event
that it lies in {16} times F_137 has probability exactly 137/963.
Its image under the output-family map is E. Thus the pushforward
probability of E is at least 137/963; representations need not be
unique, so no uniform-output assumption or equality of probabilities
is needed. The preceding argument starts with any such representation
of any family in E and excludes every right output family in the
prescribed marginal support. It proves N(E)=empty. Finite Strassen's
necessary inequality would require P(E)<=Q(N(E))=0, whereas
P(E)>=137/963>0. This completes the incompatibility proof without
enumerating or changing the full marginal laws.

This is stronger for this particular witness than the non-discriminating
degree projection, and uses only the one approved cross-intersection
refinement. It is not an assertion that two arbitrary L030-moment
representations, or two actual RS core restrictions, have this rigid
star. The all-core moment obstruction and earlier local-cap stops
retain their separate meanings.

**Independent critical audit, 2026-10-25.** The pre-existing
[SPECIALIZE audit assessment](../drafts/literature/2026-10-25-l125-critical-audit-coverage.md)
covers this review. The accepted L030 construction supplies the exact
seven-column family and the uniform-bijection marginal; its moment
formulas and L051's all-core obstruction are not substitutes for that law.
No new external theorem, hypothesis or general classification is used.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_l125.py`.
The complete independent certificate is
`scripts/finite-support/l125-critical-audit.json`.
For each of the seven source six-sets and each ordered triple of distinct
target points, the audit forms the three rows
`(x_i,1,-x_i*y_i,-y_i)`. It computes their four 3-by-3 minors by the
six signed permutation terms. The alternating minor vector is in the
kernel by determinant expansion with a repeated row. At least one minor
is nonzero in every case, so the rank is three and the projective solution
is unique. Normalization uses the first nonzero entry and Fermat inversion;
137 is prime (none of 2 through 11 divides it). Thus this reconstruction
does not use either original matrix solver. The audit then executes both
original solvers and compares them with the independently reconstructed
matrix, verifies nonzero determinant and the three anchors, and evaluates
all six source coordinates, explicitly retaining poles.

All 840 entire records match, including source sets, ordered anchor
images, both matrices, determinants, six images, every check and each
acceptance flag. All 11 top-level fields match, with no extra keys;
the certificate also records hashes of both original inputs, all minors,
kernel residuals and both replayed matrices. The counts of candidates
having a pole, in the order of T, are (4,0,2,2,1,1,2). Each case has
120 candidates. The only survivor is the identity with removed point 16;
there are no arithmetic, completeness or input-comparison failures.
The full records were compared programmatically, and the complete case
summaries, field checks, survivor and empty failure list were inspected.
This is an exact exhaustive comparison, not an inference from a preview
or from a summary flag. The original certificate is preserved unchanged.

The independent symbolic review checks the following load-bearing points.
A shared 68-support necessarily contains both a and b, so deleting K,a,b
is injective on those supports and gives exactly (1). Distinct quadratic
polynomials give distinct six-point star blocks: their difference cannot
vanish at six distinct arguments unless it is zero. Every point in a
remaining column occurs, and the two-point cooccurrence criterion is
intrinsic even under arbitrary ground-set labels; unused points do not
enter the column classes. Hence the common family really induces the
six column bijections and the bijection Phi on coefficient pairs.

In (4), the zero equation cancels constants. Nonzero A and B let AX
and BZ vary independently through the field, so the obtained additivity
holds on the entire field, rather than on a subset of symbols. Primality
makes every additive map scalar multiplication; permutation bijectivity
excludes zero slope. The two independent evaluation coordinates determine
an affine Phi with invertible linear part. Equation (5) consequently
gives a projective map from the **right** six-set to the **left** six-set,
with denominator alpha_s nonzero at every right coordinate. These are
exactly the direction, domain and pole conditions exhaustively tested.
The sole identity survivor forces t_1=16, tau(s)=s and M=lambda I,
with lambda nonzero. No semilinear extension-field assertion is needed.

Undoing both normalizations in (7) gives precisely polynomial (8).
Its degree is at most two and its value at 16 differs from y_1.
Choosing p(16) different from y_0 therefore gives a left support without
b and a right support without a. Both contain the six identical used
labels, disjoint from K,a,b, as well as K. Thus they are distinct and
have intersection at least 66, regardless of the two unused-column
labels. This exceeds 63 and excludes every right partner; the other
six choices of t_1 were excluded by the complete finite test, while a
dummy distinguished point has an empty star and cannot be a partner.

Finally, E is an event in the finite space of output families, defined
by existence of a representing bijection. Its preimage contains the
latent event of mass 137/963; equality of those events is not required.
For each output in E, fix one qualifying representation. Every proposed
right output has some representation by the specified construction, and
the preceding argument excludes all of them, without conditioning or
changing either marginal. Thus N(E) is empty in the support of the right
law. The cited finite Strassen necessary inequality applies to the tagged
finite output spaces and their pushforward probabilities and is violated.
There is no uniform-distinct-output or independence assumption.

The audit finds no gap in L125. It accepts a previously unaudited local
input, with no stronger conclusion or claim of mathematical novelty.
Alternative laws, thinned families, RS realization, arbitrary-center
67/68 safety and the bracket 955–957 are unresolved. The canonical
assembly and DAG dependencies remain unchanged; this dated audit
supersedes the earlier overview's pending-audit qualification.

## Mathlib

Full matching two-core full-law incompatibility and six-column star
rigidity: **not checked**. Supporting finite-field interpolation,
prime-field additive maps, projective matrices and finite coupling:
**not checked**. Unknown coverage is not absence. The general finite
coupling criterion is imported by the precise citation above. The
assessed search did not establish prior coverage of this particular
specialization; POTENTIALLY_NEW records that limited comparison, not
a certified originality claim.
