# L122 — Exact disjoint-pair line enumeration reduction

## Hypotheses

Use L020's field E=F_65537 and subgroup H of order n=1024. Write
q=65537 and N=binomial(n,2)=523776. Let P be the set of unordered
two-element subsets of H; repeated endpoints within a pair are forbidden.
For A={a,b} in P put s(A)=a+b and t(A)=ab, with arithmetic in E.
Let T be the number of **ordered** triples (A,B,C) in P^3 such that
the three pairs are pairwise disjoint and their (s,t) points are collinear.
This is L020's determinant-zero predicate with six distinct endpoints;
no common core or selected support family is fixed here.

Choose one representative from each multiplicative coset of H in E^*;
call the resulting set R. It has 64 elements. For s,u,v in E define

\[
 V_s=|\{A\in P:s(A)=s\}|,\qquad
 R_{u,v}=|\{A\in P:t(A)-u s(A)=v\}|.
\]

For an integer r>=0, write f(r)=r(r-1)(r-2), with f(r)=0 for r<3.
The symbol R_{u,v} denotes an occupancy, not the representative set R.

## Conclusion

The following is an exact finite reduction, with no genericity condition:

\[
 T=\sum_{s\in E} f(V_s)
   +\sum_{v\in E} f(R_{0,v})
   +1024\sum_{u\in R}\ \sum_{\substack{v\in E\\v\ne-u^2}}
                  f(R_{u,v}).                                      \tag{1}
\]

In particular, vertical and antipodal cases are retained. One can evaluate
(1) by generating N pair images, making exactly 66N=34569216 histogram
updates and scanning 66q=4325442 histogram bins. A packed-array
implementation described below uses 4522245 bytes for its main arrays,
plus bounded scalar/loop overhead. These are operation/storage bounds,
not measured run times or a claim that the full count has been computed.

Two explicit contributions are

\[
 f(V_0)=f(512)=133432320,\qquad
 \sum_v f(R_{0,v})=512\{f(511)+f(512)\}=136234398720.    \tag{2}
\]

The remaining vertical sums and the nonzero-slope sum are not evaluated
here. This reduction establishes neither uniformity after deleting a core
nor any bound on an RS list or on arbitrary-center 67/68 safety.

## Proof

**Scope and known inputs.** The prior EXPLORE assessment
`drafts/literature/2026-10-24-labeled-count-enumeration-reduction.md`
covers this exact target. L020 supplies the individual determinant
predicate and the fixed subgroup, including h=3^64 mod 65537 of order
1024. The elementary arguments below supply the endpoint-label and orbit
specializations missing from the inspected incidence sources. The general
second-moment identity is imported by precise citation below, not reproved.
There is no claim of originality beyond the sources checked.

**Pair image and line multiplicities.** The map A -> (s(A),t(A)) is
injective: its coordinates determine the monic polynomial
X^2-s(A)X+t(A)=(X-a)(X-b), whose distinct roots recover A.
Thus distinct pair objects give distinct affine points. Any two distinct
points determine a unique line: equal s-coordinates give a vertical line;
otherwise their difference quotient determines its slope and intercept.
Consequently each collinear triple of distinct pair objects belongs to
exactly one affine line. A line with r pair images has f(r) ordered triples
of distinct pairs before imposing endpoint disjointness. The ordering of
the three pairs is counted by f(r); the two endpoints of each pair have
already been made unordered in P, so there is no further factor of 2^3.

**Vertical lines.** On s=s_0, a pair containing a must have b=s_0-a.
There is at most one such pair. Fixed points b=a were excluded from P.
Hence different pairs on every vertical line have disjoint endpoints,
and its contribution is f(V_s0), including when s_0=0.

**All nonvertical collision cases.** On t=u*s+v, a pair satisfies

\[
 ab-u(a+b)=v,\quad\text{equivalently}\quad
 (a-u)(b-u)=u^2+v.                                    \tag{3}
\]

If v!=-u^2, an endpoint a cannot equal u; it determines its unique partner
b=u+(u^2+v)/(a-u). This partner may fail to belong to H or may equal a,
in which case it gives no element of P. Every actual pair is therefore
an edge of a matching on H. In particular all different pairs on this
line are disjoint, and its contribution is f(R_u,v).

If v=-u^2, equation (3) says a=u or b=u. When u belongs to H the line
consists of exactly n-1 pairs {u,b}, b in H\{u}; otherwise it has no
pairs at all. In either case it has no three pairwise disjoint pairs,
so its contribution is zero, regardless of its potentially large
occupancy. These are the only excluded lines. Equivalently, if two
distinct pairs {a,b} and {a,c} share a, their sum/product points have
slope a and intercept -a^2; this is precisely the excluded line. This
accounts for shared endpoints as well as the separate exclusion of
repeated pair objects in f(r).

For u=0 the exceptional intercept is v=0 and its occupancy is zero,
because H contains no zero. Thus the entire horizontal contribution
is sum_v f(R_0,v), without an additional correction. Summing the preceding
cases over **all** nonzero slopes, horizontal lines and vertical lines
already counts exactly T, with no overlaps between the line classes.

**Subgroup orbit multiplicities.** For h in H, multiplying both endpoints
by h permutes P and maps a point (s,t) to (hs,h^2 t). A line with slope
u and intercept v maps to slope hu and intercept h^2 v. Therefore

\[
 R_{u,v}=R_{hu,h^2v}.                                 \tag{4}
\]

For u!=0 the map h -> hu is a bijection from H to the coset uH;
in particular it has no stabilizer except h=1. For each h, the intercept
map v -> h^2v is a bijection of E and takes the excluded value -u^2
to the excluded value -(hu)^2. Thus the full eligible contribution for
each of the 1024 slopes in uH equals that for u. Multiplying the latter
by 1024 and summing over the 64 disjoint cosets proves (1). No division
by a line-orbit size, or freeness assumption at slope zero, is used.
In particular h=-1 can stabilize a horizontal line; that fact has no
effect on (1), since all horizontal and vertical lines are counted
directly rather than by this orbit weighting.

**Antipodal and horizontal cases.** Since h^512=-1, H is closed under
negation. The pairs on s=0 are exactly {a,-a}. The characteristic is odd
and a!=0, so there are exactly 512 distinct such pairs, proving the
first value in (2). None is omitted through division by its zero sum.
Every antipodal pair also enters each nonvertical histogram according
to the same equation (3); no nonzero-sum restriction is imposed there.

For a horizontal line t=v, its occupancy is zero unless v belongs to H.
For v in H, a can be any of the 1024 subgroup elements and determines
b=v/a. The forbidden equal-endpoint cases solve a^2=v: there are two
if v lies in H^2 and zero otherwise, since H is cyclic of even order
1024 and E has odd characteristic. Exchanging the two distinct endpoints
is a free two-element orbit, so R_0,v=511 on the 512 elements of H^2
and R_0,v=512 on the other 512 elements of H. This proves (2).

**Concrete finite implementation and resource bounds.** List H by the
powers of L020's h. To obtain R without an unproved primitive-root choice,
scan the residues 1,...,65536; whenever an unmarked u is found, retain it
and mark every uh for h in H. Multiplication by u is injective and distinct
cosets are disjoint, so each stage marks exactly 1024 new residues.
There are exactly 64 stages, covering all 65536 nonzero residues. Taking
the smallest unmarked residue gives 1 as the representative of H.

Generate each pair once, by indices i<j in the list H, and store its s,t
in two uint32 arrays of length N. Use one uint32 array of length q as a
histogram, resetting it between passes. First histogram the s array to
compute the vertical term. Next histogram the t array for the horizontal
term. For each u in R, histogram t-u*s modulo q over these same N
images, then sum f(r) over every bin except v=-u^2. Multiply the total
from the 64 representatives by 1024. This procedure includes bins of
occupancy 0,1,2 correctly and never lists pair triples or six-tuples.

Besides N pair-generation steps, this is (64+2)N=34569216 bin increments
and (64+2)q=4325442 bins to scan (and the same number to reset if desired).
Coset construction uses 65536 products and one scan of the field residues.
The stored pair arrays occupy 8N=4190208 bytes; the histogram occupies
4q=262148; byte coset marks occupy q=65537; and uint32 storage for H
and the 64 representatives occupies 4(1024+64)=4352. Their sum is
4522245 bytes, less than 5 million. This bound refers to explicitly packed
arrays, not Python object storage or an implemented full-count program.

Use widened integer intermediates for products such as u*s: even the
product of the two largest residue representatives can equal 2^32.
Normalize residues modulo q before indexing, and evaluate f(r) as zero
for r<3 before unsigned subtraction. On eligible lines r<=512, and
even the exceptional star occupancy is only 1023; uint32 counters suffice.
Use uint64 or arbitrary-precision accumulators. The final count is at most
N(N-1)(N-2)<2^57, since it counts a subset of all ordered distinct pair
triples; (1) sums nonnegative terms for disjoint sets of such triples, so
its partial sums also fit in uint64. The weighted representative subtotal
and the individual falling-factorial products fit as well. No floating
point arithmetic, probabilistic test or asymptotic constant is required.

**Independent diagnostics and their limits.** Import Brendan Murphy and
Giorgis Petridis, *A Point-Line Incidence Identity in Finite Fields, and
Applications*, [arXiv:1601.03981v3](https://arxiv.org/pdf/1601.03981v3),
20 February 2016, Lemma 1, printed p.2, full proof in Section 2, p.5.
Its hypothesis is any subset of F_q^2 and its sum includes every affine
line. Apply it to the injective pair image of size N. Before excluding
star lines, a full occupancy computation must satisfy

\[
 \sum_s V_s^2+\sum_v R_{0,v}^2
  +1024\sum_{u\in R}\sum_v R_{u,v}^2=N^2+qN.          \tag{5}
\]

The analogous first-moment check is (q+1)N, since each point lies on q+1
affine lines. These are consistency checks, not substitutes for the
endpoint and orbit proofs; (5) cannot determine T.

Run `python3 scripts/finite-support/l122_enumeration_reduction_check.py`.
It writes `scripts/finite-support/l122-enumeration-reduction-check.json`.
The four small analogues (q,n)=(17,8),(17,16),(41,8),(97,16) exhaustively
compare (1) with independently tested collinearity and six-endpoint
distinctness for every unordered triple of pair objects, multiplying by
6 for ordering. The ordered results are respectively 240, 51744, 240,
10272 for both methods. Every affine-line occupancy and every nonzero
brute-force line contribution is retained, and the program checks
line-by-line multiplicities, every representative orbit transport,
both moments, all star occupancies and (2). It also checks H and the
64-coset partition in the actual field and saves the resource bounds;
it does **not** construct actual-field pair histograms or evaluate T.
There were no reported failures. The general argument above, rather
than these small-field checks, proves exactness on the required instance.

The reduction meets the approved continuation test. A certified full-H
count, any core-uniform estimate, a supersaturation/threshold-saving
transfer and actual RS list bounds remain separate unproved work.
The qualified ABF comparison and C001a's 955–957 bracket are unchanged.

## Mathlib

Full matching labeled enumeration reduction: **not checked** in Mathlib.
Supporting finite-field line, subgroup/coset and finite-counting results:
**not checked**. Murphy–Petridis Lemma 1 is the precisely cited known
second-moment input, not a claim of a matching Mathlib theorem. The
research classification is POTENTIALLY_NEW only in the limited sense
that the saved bounded search did not establish matching source coverage;
this elementary specialization is not asserted to be new mathematics.
