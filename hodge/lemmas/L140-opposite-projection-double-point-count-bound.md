# L140 — Opposite ordered count from a projected double-point formula

## Hypotheses

Retain the conditional setting of audited L120, L121 and L137. Thus
B=S_1 and Y=S_2 are the identical marked smooth projective complex K3
surfaces at the common metric and real product polarization Omega.
The hypothetical holomorphic locally free Omega-slope-polystable bundle
F on B x Y has rank two, integral c_1(F)=0, and

\[
              \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

The full integral self-adjoint tensor and all L071/L118 hypotheses are
unchanged. Use L120's finite birational unramified normalization
nu:B -> Z of the original opposite reduced image. L121 gives the finite
reduced, possibly empty, original ordered coincidence scheme R_off.
Use L137's fixed original embedding j:Z -> P^N and set

\[
 u=j\nu,\qquad L=u^*O_{\mathbf P^N}(1),\qquad l=c_1(L),\qquad
 \delta=\int_B l^2=4k^2\ell^2q(D(H),D(H)).                    \tag{1}
\]

Here H, ell, k and N are precisely L137's choices, independent of F
and its unknown image Hilbert data. In particular L is ample,
l=2k ell D(H), and D(H) is an integral divisor of positive square.
Write P=length_C(R_off), and retain L139's comparison parameters

\[
 T_0=\frac{\delta(\delta+1)}2,\qquad
 U=2+\frac\delta2+\frac32\delta^{N-2}T_0^4,\qquad K=\lfloor U\rfloor.
                                                               \tag{2}
\]

No existence of F or collisions, point separation, normality or
Cohen--Macaulayness of Z, minimal gluing, coherent vanishing, or
contradictory lower count is assumed.

## Conclusion

If N>4, a nonempty Zariski open set of linear projections of P^N to
P^4 is defined on the whole original Z and gives a composite
a:B -> P^4 which is finite and unramified, with finite off-diagonal
coincidence scheme S_off. If N<=4, the same conclusions hold for u
followed by a linear inclusion P^N -> P^4. In either case
a^*O(1)=L. The residual scheme in Fulton's smooth-source double-point
formula is exactly S_off, away from the exceptional divisor, and

\[
 \boxed{\quad
 P\leq\operatorname{length}_{\mathbf C}(S_{\rm off})
       =\delta^2-10\delta+24=(\delta-4)(\delta-6)
       <K(K+1).
 \quad}                                                       \tag{3}
\]

Both orders of every original pair are retained, including all pairs
in arbitrary multiple fibres. The new projected pairs need not be
reduced. Empty original or auxiliary coincidence schemes are allowed.
The conditional hypotheses force the middle quantity to be nonnegative.

This is an ADVANCE / REPRODUCTION specializing the previously assessed
known tools. The separate critical audit below preserves it. It improves the fixed
upper bound, potentially ineffective through k and ell. It establishes
neither a contradictory lower count nor F, a collision, an algebraic
cycle or transverse transport. Universal primitive Hodge realization
remains unresolved.

## Proof

**Scope and named inputs.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-projection-double-point-bound.md`.
Reuse its primary-source coverage without another literature search.
L120 supplies the normalization and unramifiedness, L121 the original
finite reduced ordered scheme, L137 the actual original embedding and
pullback, and L139 the comparison bound. The scoped duplicate check
finds the registered source assessment and working source notes, with
no completed projection/count specialization. ATTEMPTS/070,073,078
remain in force in their recorded scopes; no minimal-defect equality,
coherent vanishing or middle-Hom Euler estimate is used.

Import W. Fulton, *Intersection Theory*, 2nd ed. (1998),
[Theorem 9.3 and proof, pp. 165–167; Corollary 9.2.3 and
Example 9.2.1, p. 163](https://djvu.online/file/8KbyCnh9POwWS).
For a morphism from a complete nonsingular n-fold to a nonsingular
m-fold, its double-point residual on Bl_Delta(B x B) has first-source
pushforward

\[
 a^*a_*[B]-\{c(a^*T_{\mathbf P^4})c(T_B)^{-1}\}_{m-n}\cap[B]. \tag{4}
\]

When the residual has expected codimension m it is its fundamental
cycle. The empty case gives zero. Here n=2 and m=4. This formula does
not require a smooth image or only ordinary double values. The related
primary reference is Fulton, *A note on residual intersections and the
double point formula*, Acta Math. 140 (1978), 93–101,
[Theorem 2, Remarks 2.1–2.5 and Section 3, pp. 94–98](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6234-11511_2006_Article_BF02392305.pdf).
Remark 2.4 retains six ordered contributions for three transverse
planes; Remark 2.5 warns that the residual dimension, rather than just
the image double locus, must be checked. We do that below, rather than
reprove the general residual formula.

For generic-fibre dimensions use
[Stacks 0B2L](https://stacks.math.columbia.edu/tag/0B2L) and
[05F7](https://stacks.math.columbia.edu/tag/05F7), with the following
explicit source-parametrized incidence. The tangent/secant methods in
[0B1Q](https://stacks.math.columbia.edu/tag/0B1Q) and
[0B1R](https://stacks.math.columbia.edu/tag/0B1R) are supporting coverage;
their embedded smooth-point conclusions are not applied to singular Z.

**A common open set of projection centres, N>4.** Put V=C^(N+1) and
G=Gr(N-4,V). A point W in G gives a quotient V -> V/W of dimension
five, with centre P(W). Write d=dim(G)=5(N-4). A fixed vector line
A in V is contained in a locus of W's of dimension d-5: it is
Gr(N-5,V/A). For a fixed vector two-plane E in V, the incidence of
a line A in E and a W containing A has dimension 1+d-5=d-4.
Its proper image contains exactly the W meeting E nontrivially.
Thus that locus has dimension at most d-4. This elementary count
also applies when N=5, where the first Grassmannian is a point.

The incidence of b in B and W containing the line u(b) has dimension
at most 2+d-5=d-3. Its image is closed since B is projective. Remove
it; then P(W) misses u(B)=j(Z), so the projection is defined on every
point of the original image.

Because u is unramified, each (b,[v]) in P(T_B), of dimension three,
defines a projective tangent line at u(b), equivalently a vector
two-plane E(b,[v]) in V. This varies algebraically: locally choose a
nonzero lift of u(b) and differentiate in direction v; their span
has rank two by injectivity of du. Changing the lift adds a multiple
of the first vector and rescales the second, leaving the span unchanged.
The two-plane incidence just counted therefore has dimension at most
3+d-4=d-1. Its image in G is closed, since P(T_B) is projective.
Remove this proper image too. For a remaining W, projection kills
no source tangent direction: with the point outside the centre, a
tangent direction is killed precisely when W meets its vector
two-plane. Hence the composite differential is injective at every
closed source point, including every original collision branch.

Now let A_0 be the open subset of B x B on which u(b)!=u(c).
Its dimension is at most four. The secant vector two-plane
E(b,c)=span(u(b),u(c)) varies algebraically on A_0. Its centre
incidence has dimension at most 4+d-4=d. There are finitely many
irreducible components. Remove the closures of the images of all
nondominating components. On each dominating component the generic
fibre has dimension at most zero; the generic-fibre dimension results
cited above allow a further nonempty open of G on which all these
fibres have dimension at most zero or are empty. This also applies
to the finite-type, possibly nonproper incidence over A_0. Intersect
these finitely many opens with the preceding tangent- and point-avoidance
opens. G is irreducible, so their intersection is nonempty.

Choose W there and identify P(V/W) with P^4. For distinct images
outside the centre, their projected images agree exactly when W
meets their secant two-plane: dependence of their quotient vectors
is equivalent to such an intersection. Consequently the new ordered
pairs in A_0 form a zero-dimensional finite-type scheme or the empty
scheme. They have finitely many underlying points. The remaining
off-diagonal pairs are the original ones, finite by L121. No
independence or genericity of the original multiple fibres is needed.

**The auxiliary map as an actual scheme morphism.** Injective closed-point
differentials imply unramifiedness by the equal-residue-field tangent
criterion, [Stacks 0B2G](https://stacks.math.columbia.edu/tag/0B2G).
The open unramified locus then contains all points: a nonempty closed
complement on a finite-type complex scheme would contain a closed
point. These are exactly the scheme criteria used in L120. The map
a is proper, since B is projective and P^4 separated; unramifiedness
makes it locally quasi-finite, so it is finite by
[02LS](https://stacks.math.columbia.edu/tag/02LS).

Let S=B x_{P^4} B. Its diagonal is open by
[02GE](https://stacks.math.columbia.edu/tag/02GE) and closed by
separatedness. Thus S_off is both open and closed in S. It is proper
over C, and has finite underlying set by the incidence proof and L121.
It is zero-dimensional and hence finite over C, again by 02LS.
No reducedness assertion is needed. A projection defined by the
quotient V -> V/W pulls back O(1) to O(1) on the complement of its
centre: the tautological point line maps isomorphically to its quotient
line. Pulling back along u proves a^*O(1)=L, including linear degeneracy
of the original image.

If N<=4, use a linear inclusion P^N -> P^4 instead. Then a is finite
and unramified by L120 and closed immersion of the targets, its fibre
product equals the original one, and S_off=R_off is already finite.
The hyperplane pullback is again L. N>=2 because the embedded Z is a
surface. This treats all low ambient dimensions without inventing a
projection centre or a smoothness hypothesis on Z.

**The whole blowup residual, including the exceptional divisor.** Write
pi:Bl_{Delta_B}(B x B) -> B x B and E for its exceptional divisor.
The blowup is a smooth fourfold, since B x B and its diagonal are
smooth. Since S_off is closed in B x B and disjoint from the diagonal,
there is an open neighborhood O of Delta_B with S intersect O exactly
Delta_B as schemes. The ideal pulled back from the target diagonal
is therefore precisely I_{Delta_B} on O. On pi^{-1}(O) its inverse
image is the invertible ideal O(-E). Dividing by that exceptional
ideal, as in the residual construction, gives the unit ideal. Thus
the residual scheme is empty on a neighborhood of E, with no embedded
or infinitesimal exceptional contribution. Away from E, pi is an
isomorphism and the residual is exactly S_off, with its full scheme
structure. It is finite and effective. If nonempty it has the required
codimension four; the empty case is covered by the same residual formula
with zero cycle. This checks the hypothesis missing in the residual
dimension failure cited above.

Every original pair is retained scheme-theoretically. Indeed
B x_Z B=B x_{P^N} B is a closed subscheme of S: equality before
projection implies equality after projection, also on schemes. This
can equally be checked in the open complement of the centre, on which
the projection is a morphism. Removing the source diagonal gives a
closed immersion R_off -> S_off. At each original pair its local
ring is C by L121, so the corresponding auxiliary Artinian local ring
surjects onto C and has length at least one. Summing gives
P<=length(S_off). A fibre with r original points supplies all
r(r-1) distinct ordered pairs, regardless of any extra projected
identifications or multiplicities. We never replace these by a count
of image values or by an unordered count.

**Degree of the known formula.** Put h_4=c_1(O_{P^4}(1)). In the Chow
group of P^4, a_*[B]=delta h_4^2, because its intersection with h_4^2
has degree integral_B l^2=delta by the proper projection formula.
Thus the degree of the first term in (4) is delta^2; no prior
generic-degree assertion for a is needed here. The projective tangent
Euler sequence, Fulton Example 3.2.11 and Appendix B.5.8, gives
c(a^*T_{P^4})=(1+l)^5 through the needed degrees. For a K3 surface,
c_1(T_B)=0 and integral_B c_2(T_B)=24; see Huybrechts,
*Lectures on K3 Surfaces*, author draft, Chapter 1, Section 2.4,
[equation (2.6) and the following Noether calculation, pp. 12–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=13).
Consequently

\[
 \int_B\{c(a^*T_{P^4})c(T_B)^{-1}\}_2
                   =10\delta-24.                            \tag{5}
\]

Subtracting (5) in (4) proves length(S_off)=delta^2-10delta+24.
The diagonal term is present even though the residual avoids E.
All equalities used for the numerical bound are degree equalities;
no replacement of arbitrary K3 zero-cycles by a common Chow point is
required. Positivity follows from the finite residual's actual scheme
length, not a sign assumption on the polynomial. Formula (3) permits
P=0; if S_off is empty its polynomial value is zero as well.

**Strict comparison with the saved threshold.** From L137, q(D(H),D(H))
is a positive integer and k,ell>=1; hence delta>=4 is an integer.
Also N>=2, so delta^{N-2}>=1, and T_0>=delta. It follows from (2) that

\[
 U\geq2+\delta/2+(3/2)\delta^4\geq\delta+1.
\]

For the second inequality, subtract delta+1: the result is
1-delta/2+(3/2)delta^4>0 for every integer delta>=1. Thus
K>=delta+1. For delta>=4, -10delta+24<0, giving

\[
 \delta^2-10\delta+24<\delta^2<K(K+1).                         \tag{6}
\]

This covers every admissible N, including N<=4 and linearly degenerate
embeddings. The continuation test succeeds: the controlled effective
residual yields a strictly smaller fixed ordered upper bound than
L139. It is a specialization of the cited double-point theorem, not
a discovery beyond those checked sources. A useful lower comparison,
F existence, collision existence, reconstruction, transport and the
universal Hodge target remain independent unresolved steps. No
mathematical script or numerical evidence is used. The separate audit
below checks the incidence, residual scheme and degree conventions.

**Separate critical audit, 2026-10-20 (step 439).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-projection-count-critical-audit.md`.
This is RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit.
The audit finds no substantive error, stronger bound or existence
conclusion. It reuses the inspected primary-source coverage above and
checks the specialization; it does not claim a fresh proof of Fulton's
theorem or a new discovery. The direct mathematical inputs remain
L120, L121, L137 and L139. Their retained L071/L118 assumptions are
conditional throughout.

First, L120's normalization is finite and unramified, and L137 embeds
the same original reduced image, without introducing compactification
boundary points. Consequently u is unramified. L137 gives exactly
l=2k ell D(H), with integral positive-square D(H), and the same fixed
delta and N appearing in L139. No replacement embedding, unknown
generic degree or projected-image polarization enters the comparison.
L121's fibre product over the stable moduli space equals B x_Z B
because Z -> M is a closed immersion. The embedding of Z in P^N
likewise identifies it with B x_{P^N} B.

For N>4 put r=N-4. Then dim Gr(r,N+1)=5r=d. Centres containing a
fixed vector line are Gr(r-1,N), of dimension 5(r-1)=d-5, also
when r=1. Allowing the line to vary in a fixed vector two-plane
adds one dimension, giving at most d-4. The closed rank condition
W intersect E nonzero is exactly this incidence image. Pulling it
back along the algebraic tangent-line map on P(T_B) therefore gives
dimension at most d-1. Both that base and B are projective, so the
tangent and point bad loci have closed proper images in G.
The rank-two tangent span is defined on every source branch by
injectivity of du, irrespective of the image tangent-space dimension.

The same rank condition over the distinct-image open A_0 has total
dimension at most d. For every dominating irreducible component, the
generic fibre over the irreducible d-dimensional G has dimension at
most zero by 0B2L. The finite-type dimension statement 05F7 then
supplies a nonempty open with zero-dimensional fibres. Nondominating
components are removed by deleting their proper closed image closures.
There are finitely many components, so all these opens and the point
and tangent avoidance opens have nonempty intersection. Properness
of the secant incidence is not used. Nilpotents do not affect this
dimension argument; it asserts finiteness of the underlying new-pair
set, not reducedness. Original off-diagonal equal-image pairs are
the separate finite set supplied by L121.

With the point line outside W, the quotient differential kills a
specified nonzero source direction exactly when W meets its tangent
two-plane. Thus the chosen projection has injective differentials at
all closed complex source points. The finite-type and equal-residue-
field hypotheses of 0B2G hold there. The unramified locus is open;
its closed complement must be empty because a nonempty closed subset
of the finite-type complex source contains a closed point. Properness
of a follows from projectivity of B and separatedness of P^4.
Unramifiedness implies local quasi-finiteness, so 02LS makes a finite.
Its self-fibre product S is closed in the projective B x B. Its
diagonal is open by 02GE and closed by separatedness, as schemes.
The closed complementary S_off is therefore proper with finite
underlying set, hence finite over C. Its length is well defined even
when it is nonreduced.

This scheme decomposition also validates the exceptional calculation,
which cannot be inferred just from pointwise tangent avoidance.
Since S_off is closed in B x B and disjoint from Delta_B, take
O=(B x B) minus its support. The restriction S|_O is precisely the
source diagonal as a closed subscheme. Its ideal, which is the image
ideal pulled back from Delta_{P^4}, equals I_{Delta_B}|_O. On the
blowup this becomes O(-E). The residual ideal is its quotient by
O(-E), hence the unit ideal on pi^{-1}(O); equivalently the ideal
quotient (O(-E):O(-E)) is the entire structure sheaf. There are no
exceptional embedded components. On the complement of E the blowup
is an isomorphism, so the residual is exactly S_off, including its
Artinian structures.

The blowup is smooth of dimension four. Near a residual point, the
pulled-back target diagonal is defined by four local equations,
since P^4 is smooth. The finite zero scheme has codimension four;
in the regular local ambient ring these equations form a system
of parameters and a regular sequence. Thus the expected-codimension
case of Fulton Theorem 9.3/Corollary 9.2.3 applies with the actual
fundamental zero-cycle, whose coefficients are the positive local
lengths. In the empty case its residual class is zero. No positivity
of an arbitrary excess-intersection class is being assumed.

The morphism Z -> P^4 induced by the chosen projection is separated,
as a morphism between separated complex schemes. Its relative
diagonal is closed. Pulling this diagonal back along the two maps
from B shows B x_Z B -> B x_{P^4} B is a closed immersion.
Equivalently the original equal-image equations contain the
projected equal-image equations. Restriction to the complements of
the same source diagonal gives the claimed closed immersion of
off-diagonal schemes. L121 makes every original local ring C.
Each corresponding projected local Artinian ring surjects onto it,
so contributes at least one, separately for each of the r(r-1)
ordered pairs over an original r-preimage value. The first-source
pushforward of the residual zero-cycle does not divide by two:
each ordered pair has its own degree-one complex residue field.
Extra projected pairs or thicker original pairs only increase
the auxiliary length.

The proper projection formula gives a_*[B]=delta h_4^2 by intersecting
with h_4^2, whether or not generic degree has been established
separately. Pullback and degree then give delta^2 for the first term.
The second-degree part of
(1+l)^5 c(T_B)^{-1} is 10l^2-c_2(T_B), since c_1(T_B)=0.
Its degree is 10delta-24. Subtraction therefore gives exactly
delta^2-10delta+24, with neither an unordered factor nor a lost
diagonal contribution. The Chern calculation concerns degrees only.

For N<=4 the target inclusion preserves the entire fibre product,
the injective differential and L. Thus the same residual and Chern
argument applies, with S_off=R_off, without projecting through a
nonexistent centre. Any impossible low-dimensional parameter case
is simply excluded by the conditional conclusions; its existence is
not needed. Empty coincidences and linear degeneracy remain covered.
Finally delta>=4 and N>=2 give T_0>=delta and delta^(N-2)>=1.
Hence U>=2+delta/2+(3/2)delta^4>=delta+1, so K>=delta+1.
The strict inequality -10delta+24<0 then proves (6). No effective
value of k or ell, or even existence of F, has been supplied.

The audit consequently preserves (3) with exactly its stated scope.
ATTEMPTS/070,073,078 remain untouched: no minimal gluing, coherent
vanishing or middle-Hom Euler estimate was needed. A contradictory
lower count, actual F, collision existence, cycle construction and
transverse transport remain unresolved. The universal primitive
Hodge realization gap is unchanged.

## Mathlib

Full matching Mathlib coverage for this conditional source projection,
residual double-point theorem and ordered-count specialization is
**not checked**. The proof imports the precisely cited classical and
Stacks results. Unknown availability is not evidence of absence;
this informal argument is not a Lean verification.
