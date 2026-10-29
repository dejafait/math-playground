# L155 — Original disjoint-pair mixed-exterior bridge

## Hypotheses

Let E be any field extension of F_97, and fix L153's original sets

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

Use all 756 supports indexed by (I,K) in binom(S,2) times binom(J,2),
in L153's original order. Choose any original unordered pair a<b whose
four-element supports are disjoint; no permutation quotient is taken.
Put W=E^S in increasing coordinate order. For j=a,b use exactly L109's
map Q_j:W -> E^4, its kernel V_j, and its six-by-21 matrix N_j, with
z_j=min(S minus I_j) and increasing covector-pair order. In particular,

\[
 g_j(X)=\prod_{y\in J\setminus K_j}(X-y),\qquad
 c_{jx}(w)=g_j(z_j)w_x-g_j(x)w_{z_j},
 \quad x\in(S\setminus I_j)\setminus\{z_j\}.
\]

L109 gives dim V_j=3 and identifies N_j with the induced exterior-square
map. Use L153's audited rank twelve of every original stacked pair over
every E. Its finite-certificate qualifications are inherited; that census
is an input, not recomputed here. No equality-pencil hypothesis is needed
for the following linear assertion.

## Conclusion

For every such original pair and every E/F_97,

\[
 V_a\cap V_b=\{0\},\qquad
 \ker\begin{bmatrix}N_a\\N_b\end{bmatrix}
   =V_a\wedge V_b\ \subseteq\bigwedge^2 W.                 \tag{1}
\]

Here V_a wedge V_b means the **linear span** of all x wedge y with
x in V_a and y in V_b. It is not the set of single wedges. For any
bases a_1,a_2,a_3 and b_1,b_2,b_3 of the two kernels, the nine vectors
a_i wedge b_j form a basis of the common kernel.

The direct sum V_a direct-sum V_b has dimension six inside the
seven-dimensional W; a one-dimensional complement remains. This proves
the linear bridge only. It does not classify decomposable elements,
establish their recovery gates, identify any numeric extracted pair,
exclude twelve compatible rows or improve the frozen 11/q–16/q interval.

## Proof

### Imported exterior facts and the actual maps

Import Keith Conrad, *Exterior Powers*, undated 47-page author PDF
inspected 2026-10-25,
[Theorem 4.2, printed pp. 11–12, and Theorem 5.1, pp. 15–16](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
The former gives the ordered exterior basis of a finite free module;
the latter gives the induced map, sending x wedge y to Q(x) wedge Q(y).
The same source's Theorem 5.6 and Corollary 5.9, p. 18, justify viewing
exterior powers of vector subspaces as subspaces of the ambient exterior
power. All modules used here are finite-dimensional vector spaces over
E, so the noninjectivity caveat for general module inclusions is irrelevant.
These standard theorems are imported, not reproved. The remaining basis
comparison is the needed local specialization, not a source theorem
asserting the original labeled identity.

Each g_j(z_j) is nonzero since its roots lie in J whereas z_j lies in S.
The four covectors c_jx are independent: on their four x-coordinates
they form the diagonal matrix with entry g_j(z_j). Thus Q_j is surjective,
with three-dimensional kernel as in L109. No scalar division or change
of quotient is introduced. In the increasing coordinate bases, the
coefficient of the x,y target wedge in the image of e_r wedge e_s is

\[
 c_{jx,r}c_{jy,s}-c_{jx,s}c_{jy,r}\qquad(r<s,\ x<y).
\]

This is exactly L109's N_j entry, with its original sign and order.
Consequently the kernel of the stacked matrix is the intersection of
the kernels of exterior-square(Q_a) and exterior-square(Q_b), as subspaces
of exterior-square(W). All of these statements hold over E with the
original coefficients embedded from F_97.

### Do not assume that the quotient kernels are disjoint

Write A=V_a, B=V_b, T=A intersect B and t=dim T, so 0<=t<=3.
Choose complements A_0 of T in A and B_0 of T in B. The sum
T+A_0+B_0 is direct. Indeed, if u+a+b=0 with u in T, a in A_0,
b in B_0, then b=-(u+a) lies in A intersect B=T, hence b=0;
then u+a=0 forces both remaining terms to vanish. Complete this sum
to a decomposition

\[
 W=T\oplus A_0\oplus B_0\oplus C,
 \quad \dim A_0=\dim B_0=3-t,\quad \dim C=1+t.            \tag{2}
\]

Choose an ordered basis respecting (2). As Q_a has kernel
A=T direct-sum A_0, its restriction to B_0 direct-sum C is an
isomorphism onto E^4. The images of a basis of B_0 direct-sum C
therefore form a basis, and their pairwise exterior products form a
basis of exterior-square(E^4), by the imported exterior-basis theorem.
It follows that exterior-square(Q_a) annihilates exactly the span of
adapted basis wedges with at least one basis factor in T or A_0.
There can be no cancellation among the other basis wedges, because
their images are a basis. Likewise exterior-square(Q_b) annihilates
exactly the span of basis wedges with at least one factor in T or B_0.

Both kernels are thus coordinate subspaces in the same exterior basis.
Their intersection is spanned by precisely the basis wedges in both
lists: all wedges having a factor in T, and the wedges having one
factor in A_0 and the other in B_0. This proves the direct decomposition

\[
 \ker\begin{bmatrix}N_a\\N_b\end{bmatrix}
       =(T\wedge W)\oplus(A_0\wedge B_0).                \tag{3}
\]

The first summand has binom(t,2)+t(7-t) basis wedges, counting those
internal to T and those between T and its complement. The second has
(3-t)^2 different basis wedges. Hence the dimension in (3) is the
integer

\[
 \binom t2+t(7-t)+(3-t)^2
       =9+\frac{t(t+1)}2.                               \tag{4}
\]

These are counts of basis elements, not divisions in the coefficient
field. They give dimensions 9,10,12,15 for t=0,1,2,3 respectively.

L153 gives rank twelve of this same original stacked matrix over E.
Since dim exterior-square(W)=binom(7,2)=21, rank-nullity gives its
kernel dimension exactly nine. Comparing with (4) forces t=0. In
particular literal support disjointness was used to invoke L153;
it was not mistaken for quotient-kernel disjointness.

### Equality, uniformity and limitations

With t=0, (2) becomes W=A direct-sum B direct-sum C and (3) becomes
exactly (1). It proves both inclusion and exhaustion: the nine mixed
basis wedges survive in the common kernel, while every other exterior
basis coordinate is forbidden by at least one of the two quotient maps.
Any chosen bases of A and B can be completed by a basis of C, proving
the stated nine-vector basis assertion without a preferred normalization.

The argument used an arbitrary original pair and an arbitrary extension
E. L153's nonzero original minors supply rank twelve in each such E;
no extension-field samples, algebraic closure, rational descent or
identification of two different labeled kernels is involved. No new
finite census or mathematical script is necessary. The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-10-25-pair-mixed-exterior-bridge-review.md`.
This is REPRODUCTION of the assessed exterior-basis mechanism with its
local applicability bridge, not a claim of mathematical originality or
progress beyond the checked sources.

For prospective coding use retain L109/L153's q=97^20, k=8, pinned
1/4<=delta<5/16 cell, coefficient syndromes in U_S, nonzero actual D
and locators, t=0 equality with sixteen original finite events,
arbitrary weights and original chart, and the inherited L056/L069/L040
and L051/L055 qualifications. Here that coding parameter t is distinct
from the temporary intersection dimension used in (2)–(4).
All Plucker, projection-rank, nonzero-lambda, full-weight and finite-chart
gates remain separate obligations. In particular a general linear
combination of the nine mixed wedges need not be decomposable. C152a's
arbitrary-pair extraction is prospective relevance, not an input to
this proof. L151's label limits, L104's survivors and ATTEMPTS/041–043,
/048–049 remain unchanged. Universal representation and challenge
identification are independent unresolved gaps.

### Separate critical audit — step 484, 2026-10-25

The first independent mathematical review used the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-l155-mixed-exterior-critical-audit-review.md`.
It checked this entire proof against L109's actual map/kernel argument
and L153's original domain, rank proof and completed step-480 audit.
The inspected Conrad results and source-hypothesis comparison were reused;
no new source theorem, finite census or certificate replay was needed.
No defect or additional mathematical input was found. The following
checks certify the stated linear identity, conditional on the existing
audited finite input; they do not strengthen it to a locus theorem.

First, the coefficients and coordinate conventions agree exactly.
For each original support, the four x-coordinates are distinct and
exclude z_j, so the corresponding four-by-four submatrix of Q_j is
g_j(z_j) times the identity. The seven roots of g_j are in J, while
z_j is in S; all these are distinct embedded F_97 elements. Thus this
minor is nonzero in every E. The coefficient on e_r wedge e_s is
c_{jx,r}c_{jy,s}-c_{jx,s}c_{jy,r}, identical to L109 (1) by commutativity
of scalar multiplication. Increasing x<y and r<s fix the signs. The
stack is precisely N_a above N_b for the original a<b; no relabeling,
row normalization or transport from another pair is used. Changing to
the adapted basis in the proof is a single invertible change of domain
basis for both maps, not a substitution of the original matrices.

Second, the simultaneous-basis argument has no cancellation gap.
In (2), B_0 plus C has dimension (3-t)+(1+t)=4 and meets A only
in zero, so Q_a restricts to an isomorphism there. Similarly Q_b
restricts to an isomorphism on A_0 plus C. Each quotient may use its
own image basis: the two target copies of exterior-square(E^4) need
not share a basis. In each copy the six surviving domain wedges have
linearly independent images. Consequently all their coefficients must
vanish in that map's kernel. A vector in both kernels can have nonzero
coordinates only on their common allowed wedges. These are exactly
the wedges meeting T, together with A_0 wedge B_0. Their two lists are
disjoint subsets of the same exterior basis, proving both the directness
in (3) and absence of extra linear combinations.

All possible intersection dimensions, including coincident kernels,
give the following complete check of (4):

| t | dim A_0 = dim B_0 | dim C | dim(T wedge W) | dim(A_0 wedge B_0) | common kernel dimension |
| --- | --- | --- | --- | --- | --- |
| 0 | 3 | 1 | 0 | 9 | 9 |
| 1 | 2 | 2 | 6 | 4 | 10 |
| 2 | 1 | 3 | 11 | 1 | 12 |
| 3 | 0 | 4 | 15 | 0 | 15 |

For t=3, A=B=T and the common kernel is the single quotient's
fifteen-dimensional kernel; the proof does not omit this case. The
entries count basis vectors as integers, so reducing a dimension formula
modulo 97 is neither used nor permitted. L153's original nonzero
twelve-by-twelve minor remains nonzero under the injective field map
F_97 -> E, and twelve rows bound rank above by twelve. Rank-nullity
therefore gives dimension nine over E and rules out every t>0 case.

Finally, when t=0, every a_i wedge b_j maps to zero under both exterior
maps because one factor is killed by each. These nine wedges are
independent in an exterior basis completed by any one-dimensional C.
The common kernel has dimension nine, so this verifies exhaustion as
well as inclusion independently of any tensor being a single wedge.
The proof works for any chosen bases of A and B and over every extension
E; it never chooses a base-field representative of an extension-field
plane. All 79,380 original pairs are covered through the quantified
L153 input, with no sampling or symmetry assumption.

Audit verdict: pass for (1) and the nine-vector basis assertion, with
L109 and L153 as the only direct mathematical inputs. The source
citations and field hypotheses are adequate for the imported exterior
facts. This is REPRODUCTION and verification of an existing partial
result, not a new theorem beyond the previously written argument or
progress beyond the checked sources. No decomposable-locus classification,
projection-rank claim for that locus, recovery-gate removal, twelve-row
exclusion, radius improvement or challenge identification was audited
or proved. Further repetition of this passed audit needs a specific
defect; ATTEMPTS/048–049 remain in force.

## Mathlib

Full matching original-pair mixed-exterior bridge: **not checked**.
Supporting exterior-basis, induced-map, finite-dimensional complement,
rank-nullity and scalar-extension coverage: **not checked anew**.
The precise standard exterior inputs are cited above; L109 and L153
retain their original qualifications. Unknown Mathlib availability is
not evidence of absence. The separate informal critical audit is recorded
above; no formal proof-assistant verification is claimed.
