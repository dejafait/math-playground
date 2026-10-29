# L139 — A large repeated-message fiber forces full-sheet constancy

## Hypotheses

Use L030's labeling setup. Let q=137,
T={16,64,70,102,112,118,121}, E=F_65537,
F=F_(65537^28), and H=<19139> of order 1024. Let C be any
61-subset of H and let sigma be any bijection from
(T times F_137) disjoint union four dummies onto H minus C.
Write x_(t,y)=sigma(t,y). The 959 actual labels are pairwise distinct.

Let K be either E or F. For every P=(u,v) in G=F_137^2 let
g_P in K[X] have degree at most two, with repetitions allowed.
Assume that, for each (t,y), there is d_(t,y) in K such that

\[
 g_P(x_{t,y})=d_{t,y}\quad\text{whenever }u+tv=y.
 \tag{1}
\]

These are the full-sheet hypotheses also restated in L138. Its
translation-inclusion conclusion is not used, and no such inclusion
is assumed. There is no auxiliary-coordinate degree bound, injectivity
condition, coefficient-span restriction, or identification of the
auxiliary field with either coefficient field.

## Conclusion

If the messages are not all equal, then every message fiber

\[
 S_g=\{P\in G:g_P=g\}
\]

has size at most **243**. In particular, a message attained at more
than 272 auxiliary points forces all 18769 messages to equal it.
Neither numerical bound is claimed to be sharp.

This is a certificate-backed partial result awaiting a separate critical
audit. It does not prove the existence of a fiber larger than 243,
exclude nonconstant small-fiber sheets, establish retention or compatible
laws, or transfer to an RS list. The 955–957 bracket is unchanged.

## Proof

**Source and scope.** The pre-invocation EXPLORE assessment is
[the completed large-fiber comparison](../drafts/literature/2026-10-29-large-message-fiber-propagation.md).
Import Keith Conrad, *Counting Roots of Polynomials*, undated
[author-hosted note](https://kconrad.math.uconn.edu/blurbs/ringtheory/countroots.pdf),
version retrieved 2026-10-29, Theorem 1 and Lemma 2, pp. 1–2:
a nonzero nonconstant polynomial over a field has at most its degree
many distinct roots. A nonzero constant has no roots. This applies
directly over both K fields; the root theorem is not reproved.
The affine-blocking and projective-percolation results compared in that
assessment are not inputs. The additional argument is the specific
seven-direction propagation, its complete finite certificates, and
the incidence count below. No novelty beyond the checked sources is
asserted.

**1. A fiber is closed under three incident active lines.** For t in T
and y in F_137 write

\[
 A_{t,y}=\{(u,v):u+tv=y\}.
\]

Call this line active for S if it meets S. Fix a message g with
nonempty fiber S=S_g. If A_(t,y) is active, (1) at a fiber point
gives d_(t,y)=g(x_(t,y)). Consequently, at any point P on three
distinct active lines, g_P-g vanishes at their three distinct actual
labels. The root theorem, including the nonzero constant case, implies
g_P=g. Thus such a P belongs to S. Equivalently, every exterior
point lies on at most two active lines.

In the rest of the proof, a *closed* set means a subset of G with this
three-line property. Starting from any seeds in a closed set, one can
repeatedly add a point on at least three already active lines; every
added point remains in the original set. Activating a line means only
that it meets the current point set, not that all its points are added.
There is exactly one incident line of each selected direction at a
point, so the three active lines necessarily have distinct directions.

The affine maps P -> P_0+lambda P, for lambda in F_137^*, preserve
these seven parallel classes and the closure rule. This invariance
is purely auxiliary combinatorics. It does not relabel or identify
actual coefficients, actual field labels, or the assignment (1).

**2. A rigorous finite stopping certificate.** Let S be proper and
closed, let m_t count its active direction-t lines, and put M=sum_t m_t.
Take any exterior point. At least five of its seven lines are inactive;
choose one, L=A_(t,y). Every point of L is exterior because L is
inactive. Each of its 137 points is on at most two active lines, and
each active line of a different direction intersects L exactly once.
It follows that

\[
 M-m_t\le 2\cdot137=274.
\]

Since L is inactive, m_t<=136. Therefore

\[
 M\le410 \quad\text{for every proper closed set}. \tag{2}
\]

Thus a valid forced-addition trace activating at least 411 distinct
lines cannot be contained in any proper closed set. This proves the
stopping rule used below; it is not an empirical truncation or an
application of a different percolation model.

**3. Complete collinear seed and coloring certificates.** Put
e_t=(-t,1) in G. For each of the seven t and every r in F_137,
test the seed set {0,e_t,r e_t}. The full certificate has all
7*137=959 cases, including r=0,1 with their duplicate seed removed.
Let B_t be the set of parameters whose closure is proper in this
certificate. For every r outside B_t, the saved trace reaches the
411-line threshold in (2). For every r in B_t, its saved terminal
point set is checked to be closed, not merely to stop at a time limit.

Here is the complete small summary; the trace and coloring data, rather
than this summary alone, certify the entries.

| t | Full seed cases | Size of B_t | Graph vertices | Graph edges | Colors c_t | R_t=2+c_t |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 75 | 62 | 60 | 252 | 5 | 7 |
| 64 | 66 | 71 | 69 | 504 | 6 | 8 |
| 70 | 75 | 62 | 60 | 378 | 8 | 10 |
| 102 | 54 | 83 | 81 | 1206 | 12 | 14 |
| 112 | 63 | 74 | 72 | 735 | 8 | 10 |
| 118 | 81 | 56 | 54 | 180 | 4 | 6 |
| 121 | 78 | 59 | 57 | 249 | 5 | 7 |

The graph for t has vertex set B_t minus {0,1}. For two distinct
vertices r<s, where the ordering is their integer representatives,
include an edge exactly when both

\[
 s/r\in B_t,\qquad (s-1)/(r-1)\in B_t. \tag{3}
\]

The divisions are in F_137, and their denominators are nonzero by
the vertex definition. The certificate contains every vertex, every
edge and a partition into c_t color classes. The verifier independently
constructs (3) by checking multiplication against all elements of B_t,
then checks that the classes partition the vertex set and that every
edge has differently colored endpoints. Only valid colorings are
needed; no optimal chromatic-number or clique-number claim is used.

All certificate paths and commands here are relative to the notebook.

- `scripts/finite-support/large-fiber-collinear-traces.u16` contains
  every ordered trace. The point (u,v) is encoded as u+137v. Each
  record is little-endian uint16: direction index, parameter r, full
  flag, trace length, then all trace point codes. Records are ordered
  by direction in the displayed T order and then r=0,...,136. Its
  SHA-256 is
  `f4b9d32cfb7dff39adf6ebb9f585000fda50549e3a82defe12e301cf4fb11c00`.
- `scripts/finite-support/large-fiber-collinear-results.tsv` records
  the status, trace length and active-line count for every case.
- `scripts/finite-support/large-fiber-collinear-graphs.json` contains
  all B_t, vertices, edges and color classes, plus the exact rational
  incidence bounds. Its SHA-256 is
  `1f7f3d481d2b4e2f9172597849edb4c1f8e73a89f5d9c1e7e16271b8211e4737`.
- `scripts/finite-support/large-fiber-certificate-verification.json`
  records the complete verification, with an empty failures list.

The independent trace-checking algorithm does not call the production
closure queue. It reads each entire record, checks its initial seed
list and distinct point codes, and processes the trace in order.
For each later point it checks directly that at least three of the
seven lines (t,u+tv) were already activated by previous trace points.
It then activates all seven of that point's lines. A full trace must
end with at least 411 active lines. For a proper trace it enumerates
every point on every active line and checks that the set of points
with at least three incident active lines is exactly the trace set.
It checks all 959 records, their TSV entries, all graph edges and all
color memberships, and rejects trailing or short binary data. Thus no
sampled preview or uninspected omitted case is used for the bound.

The production code may discover extra queued points beyond the
processed prefix of a full trace. They are not needed in its certificate.
Its recorded active-line count stops at 411; the verifier activates all
seven lines of the last processed point and may count slightly more.
This only strengthens the same stopping test. Proper traces include
the whole queue and must pass the exhaustive closure check.

**4. A proper closed set has line occupancies at most R_t.** Let S be
any proper closed set, and let L be a selected-direction-t line.
If |S intersect L|<=1, the claimed bound is immediate. Otherwise,
choose two of its points P_0 and P_1. Their difference is alpha e_t
for a nonzero alpha in F_137. Apply P -> alpha^(-1)(P-P_0) to
the entire set. The resulting set S' is proper and closed, and its
points on the transformed line have the form r e_t, with 0,1 present.

Every other parameter r lies in B_t: otherwise its three-seed trace
from step 3, contained in S', would activate 411 lines and contradict
(2). For any two additional parameters r<s, S' contains both triples
{0,r e_t,s e_t} and {e_t,r e_t,s e_t}. Normalize the first by scaling
by r^(-1) and the second by translation by -e_t and scaling by
(r-1)^(-1). Each normalized set is still proper and closed.
Their third parameters are exactly those in (3), so both belong
to B_t. Therefore the additional parameters form a clique in the
certified graph. Its proper coloring gives at most c_t such parameters.
Adding the two normalized points yields

\[
 |S\cap A_{t,y}|\le R_t,
 \quad (R_{16},R_{64},R_{70},R_{102},R_{112},R_{118},R_{121})
 =(7,8,10,14,10,6,7). \tag{4}
\]

No assumption that arbitrary normalized sets arise as actual message
assignments is made: the implication uses the closure property alone.

**5. The asymmetric incidence bound.** Suppose S is nonempty, proper
and closed, and put s=|S|. For each selected direction, its m_t active
lines partition S into nonempty sets of size at most R_t, so
m_t>=s/R_t. Choose any active direction-16 line L, and put
r=|S intersect L|. By (4), 1<=r<=7.

Each of the r fiber points on L lies on all six active lines of the
other directions. Each of the remaining 137-r points is exterior;
since L itself is active and exterior points lie on at most two
active lines, it is on at most one further active line. Each active
line of another direction intersects L at exactly one point. Counting
these intersections, with their direction multiplicities, gives

\[
 \sum_{t\ne16}m_t\le 6r+(137-r)=137+5r\le172. \tag{5}
\]

On the other hand, (4) yields

\[
 \sum_{t\ne16}m_t
 \ge s\left(\frac18+\frac1{10}+\frac1{14}
                 +\frac1{10}+\frac16+\frac17\right)
 =\frac{593}{840}s.
\]

Consequently

\[
 s\le\frac{172\cdot840}{593}=\frac{144480}{593}<244,
\]

where 593*244=144692>144480. Since s is an integer, s<=243.
An empty fiber satisfies this bound trivially. If the sheet is
nonconstant, every nonempty message fiber is proper and hence has this
bound. Conversely, a fiber of size greater than 272 is nonempty and
cannot be proper, so it is all of G. This proves the conclusion.

**Reproduction and qualifications.** Run:

```sh
cc -O3 -std=c11 -Wall -Wextra -Werror scripts/finite-support/large_fiber_closure.c -o scripts/finite-support/large-fiber-closure-bin
scripts/finite-support/large-fiber-closure-bin
scripts/finite-support/large-fiber-closure-bin collinear
python3 scripts/finite-support/large_fiber_collinear_graphs.py
python3 scripts/finite-support/verify_large_fiber_certificates.py
```

The first production invocation preserves an unsuccessful diagnostic:
for the fixed pair 0,e_16, 7538 of 18769 arbitrary third points have
proper closure, far above 272. Its entire binary trace and TSV are
verified too, but this diagnostic is not an input to (4) or (5).
The proposed uniform occupancy bound eight also fails for the saved
colorings: their largest bound is fourteen. It is essential to retain
the unequal bounds in (5). The successful proof neither calls those
failed diagnostic thresholds true nor treats any proper combinatorial
closure as a full-sheet coefficient assignment.

The argument covers all allowed C and sigma, both coefficient fields,
and repeated messages. Distinct actual labels supply the root argument;
no field-size estimate, translation-inclusion hypothesis, general
incidence theorem, auxiliary polynomial-degree bound, or omitted
off-fiber equation is substituted for (1). The conclusion is only a
necessary restriction on a nonconstant full sheet. No such sheet is
constructed, and none is excluded when all its fibers are small.

## Mathlib

Full matching coverage and supporting theorem names were not checked
in this step or its reused assessment. No absence claim is made.
The polynomial-root input is the precisely cited standard field theorem;
the finite propagation and coloring certificates are not Lean proofs.
Separate critical mathematical and certificate audit remains pending.
