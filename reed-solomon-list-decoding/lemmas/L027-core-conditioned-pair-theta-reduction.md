# L027 — Core-conditioned shared pair/theta lift and exact threshold transfer

## Hypotheses

Use C001a's fixed instance: E=F_65537, F=F_(65537^28), the
order-1024 subgroup H of E^*, strict message degree less than k=64,
interleaving width any integer m>=1, and simultaneous column agreement
with one received array. The closed 956/1024 ball consists of tuples
having at least 68 agreement columns. Put

\[
 T=65537^{28}/2^{128},\quad M=\lfloor T\rfloor,\quad
 N=\binom{1024}{61},\quad D=\binom{68}{61}=\binom{68}{7}.
\]

For each C in the 61-subsets of H define V_C to be all 7-subsets of H\C.
Define a graph G_C on V_C by joining distinct A,B exactly when
|A intersect B|>=3. Define a 3-uniform hypergraph J_C on the same
vertices as follows. A triple {A,B,B'} is an edge exactly when its
triple intersection is empty, all three pair intersections have size
two, and the matrix with columns (p_ij,-s_ij,1)^t is nonsingular over E,
where s_ij and p_ij are the sum and product of the two points in the
corresponding pair intersection. Vertex names are only labels; the
sum/product computation uses the actual points of H. Permuting the
three columns changes at most the sign of the determinant, so this is
a well-defined unordered edge condition. Determinant-zero triples
are not edges.

Use TH and the link convention of Castro-Silva et al., Definition 1.1,
as stated in [the source note](../foundations/07-core-conditioned-theta-source.md).
For a vertex A let W_A be the vertices occurring with A in some edge
of J_C, and let (J_C)_A be the graph with edges e such that
e union {A} is an edge of J_C. An empty link imposes no row constraint.

Let K_C be the set of pairs (f,F), where F is a real symmetric matrix
indexed by V_C, f=diag(F), and all the following hold on this same F:

\[
 R(F)=\begin{pmatrix}1&f^t\\f&F\end{pmatrix}\succeq0,
 \qquad F_{AB}=0\quad(\{A,B\}\in E(G_C)),
 \qquad F_A[W_A]\in f_A\,\mathrm{TH}((J_C)_A)\quad(A\in V_C).
 \tag{1}
\]

No division by f_A is used. Set
\(\beta_C=\max_{(f,F)\in K_C}\sum_{A\in V_C}f_A\).
The proof below establishes that this maximum exists. No value of it,
no automorphism reduction, and no tractable optimization implementation
is assumed.

## Conclusion

Every actual 956/1024 list, after selecting one 68-subset of agreement
columns for each tuple, induces independent sets for both G_C and J_C
whose indicators have a shared lift in K_C, for every C and every m>=1.
In particular,

\[
 B_m(956/1024)\le
 \left\lfloor\frac{\sum_{C\in\binom H{61}}\lfloor\beta_C\rfloor}{D}\right\rfloor
 \le \left\lfloor\frac{\sum_C\beta_C}{D}\right\rfloor.       \tag{2}
\]

The first upper certificate in (2) meets T if and only if

\[
 \sum_C\lfloor\beta_C\rfloor<D(M+1),                         \tag{3}
\]

equivalently its integral left side is at most D(M+1)-1.
This is a test of this certificate's strength, not a necessary condition
for actual safety. The second certificate meets T exactly when
\(\sum_C\beta_C<D(M+1)\).

For uniform integer local upper bounds b, the largest b for which
the resulting certificate \(\lfloor Nb/D\rfloor\) meets T is

\[
 b_* =\left\lfloor\frac{D(M+1)-1}{N}\right\rfloor=1532495.
 \tag{4}
\]

Thus proving beta_C<1532496 for every core is sufficient, by flooring
each local maximum. It is not the only sufficient possibility:
nonuniform local bounds satisfying (3) also suffice. If instead one
uses a uniform real bound u directly without local flooring, its exact
test is \(u<D(M+1)/N\); the stronger closed test \(u\le TD/N\)
also suffices.

The shared model alone already implies

\[
 \beta_C\le K=\frac{\binom{963}{3}}{\binom73}
              =\frac{148379361}{35},\qquad
 \lfloor\beta_C\rfloor\le4239410.                            \tag{5}
\]

Substituting this ordinary cap at every core does not meet (3)'s
threshold; this does not show that the actual beta_C fail it.
Without local flooring, the ordinary cap's global transfer is exactly
L001's support ratio:

\[
 \frac{NK}{D}=\frac{\binom{1024}{64}}{\binom{68}{64}}.
 \tag{6}
\]

Its ratio to T lies strictly between 2.766 and 2.767. Flooring K before
transfer still gives an upper certificate strictly above T. No improved
local maximum or safety at 68 agreements is established here.

## Proof

**Known input and specialization.** Import the independent-indicator
lift in Theorem 2.1, together with the recursive definition and the
independent-set upper-bound consequence of Corollary 2.3, from Davi
Castro-Silva, Fernando Mário de Oliveira Filho, Lucas Slot and Frank
Vallentin, [A Recursive Theta Body for Hypergraphs](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf),
Combinatorica 43 (2023), 909–938, DOI 10.1007/s00493-023-00040-9,
final version: Definition 1.1, p. 912; Theorem 2.1 and full proof,
pp. 915–916; Corollary 2.3 and proof, p. 917. These exact passages
have been inspected and recorded in the source note. They hold for
finite uniform hypergraphs without regularity or transitivity, and
include IND(J) in TH(J). We do not reprove the recursive theorem.

The prior [SPECIALIZE assessment](../drafts/literature/2026-10-06-core-conditioned-pair-theta-reduction.md)
approves only the shared-lift applicability and the exact finite
counting/strength test. The differences from the source are the added
pair equations on the same lift, the selected RS tuple supports, and
the summation over cores. The following proof supplies those
differences; it neither computes an optimum nor assumes a generic
point configuration.

**Actual lists and their local independent sets.** Fix one center Y
and its list L. For each tuple P choose any 68-subset S_P of its
simultaneous agreement set. For distinct tuples P,Q, L001's
k-column uniqueness proves |S_P intersect S_Q|<=63. In particular
the selected supports are distinct, so the support family has exactly
|L| elements, even when some tuples have extra agreements.

For a fixed C define I_C={S_P\C: C subset S_P, P in L}.
All its vertices have size seven and the support-to-residual map is
injective at this core. Distinct residual vertices intersect in at
most 63-61=2 points. Thus I_C is independent in G_C.

Suppose three members formed an edge of J_C. Their full supports
would have common intersection exactly C, because the residual
triple intersection is empty. Their pair-only overlaps would be
the three residual pair intersections, each of size two and disjoint
from the other two. Each full support has the required three unique
points: its seven residual points comprise two disjoint incident
pairs and three remaining points. These selected supports belong to
three distinct tuples sharing Y. L020, including its extension-field
and tuple necessity argument, therefore forces their determinant to
vanish. This contradicts the edge definition. Hence I_C is also
independent in J_C. No singular triple, including L020's realizable
antipodal example, has been excluded by this argument.

**A shared lift, including empty and zero cases.** Write z=1_(I_C).
The indicator lift supplied in the proof of the imported Theorem 2.1
is F=zz^t, f=z, with R(F)=(1,z)^t(1,z). It satisfies the recursive
row conditions. On a G_C edge at most one endpoint belongs to I_C,
so the same F also satisfies F_AB=z_A z_B=0. This proves feasibility
of the joint lift, rather than merely separate membership of z in
two projected bodies.

To specify the source applicability at the boundary, if z_A=1 the
restricted row is the indicator of I_C intersect W_A, an independent
set in the graph (J_C)_A. If z_A=0 the row is zero and belongs to
0 TH((J_C)_A)={0}; the link body is nonempty because it contains
the empty-set indicator. Empty links impose no conditions. The
empty I_C itself gives f=0,F=0 and is feasible. These are checks of
the imported indicator lift, not a new recursive-theta theorem.

For an arbitrary feasible lift, the 2-by-2 principal minor of R(F)
on its first coordinate and A implies 0<=f_A<=1. The 2-by-2
principal minors of F imply |F_AB|^2<=f_A f_B. If f_A=0,
its entire row of F is therefore zero, consistent with the scaled
row requirement. Nothing is divided by a zero diagonal, and no
positive-diagonal approximation is required.

K_C is nonempty by the zero lift. It is bounded since 0<=f_A<=1
and |F_AB|<=1. It is closed: PSD and edge equations are closed;
for each nonempty link, the imported Theorem 2.1 makes TH((J_C)_A)
compact. The set of (a,ag) with 0<=a<=1 and g in that body is a
compact continuous image. The condition (f_A,F_A[W_A]) in this set
is closed, including a=0. There are finitely many vertices, so the
intersection of these constraints is closed. Consequently K_C is
compact in finite-dimensional real matrix space and the continuous
objective attains beta_C. Cardinality of the actual local set is
at most beta_C, hence at most floor(beta_C).

**Clique rows and ordinary strength.** For each 3-subset U of H\C,
let Q_U be all vertices containing U. Any distinct two in Q_U form
a G_C edge. With s=sum_(A in Q_U) f_A, the corresponding principal
block F[Q_U] is diagonal. PSD of R(F), evaluated on the vector
(-s,1_(Q_U)), gives s-s^2>=0. Since s>=0, it follows that s<=1,
including s=0. Thus all explicit 3-subset packing rows
sum_(A containing U) f_A<=1 are justified and redundant; adding
them would preserve the actual lifts and the value of beta_C.

Sum these rows over all binomial(963,3) choices of U. Each vertex
contains binomial(7,3)=35 such subsets. This gives
35 sum_A f_A<=binomial(963,3), proving (5). The proof uses
unit weights and exact incidences, without an edge-induced measure.

**Core-incidence transfer.** Count all pairs (S_P,C) with
C subset S_P and |C|=61. Each selected size-68 support occurs
exactly D times. At each core the number of incidences is exactly
|I_C| by injectivity. Therefore

\[
 D|L|=\sum_{C\in\binom H{61}}|I_C|
       \le\sum_C\lfloor\beta_C\rfloor\le\sum_C\beta_C.
\]

Divide by the positive integer D and floor because |L| is integral.
The same labeled caps apply to every center and every m>=1, so
maximizing over centers proves (2). In particular no representative
core is substituted for the whole sum. Uniformity would be an
additional property of a future cap, not of the actual local families.

**Exact threshold test.** For any real U, the integral certificate
floor(U/D) is at most T exactly when it is at most M, exactly when
U<D(M+1). This proves both forms of (3), including the strict
inequality at the upper endpoint. If U=Nb for integral b, then
Nb<D(M+1) is equivalent to Nb<=D(M+1)-1. Positive integer
division gives (4). In particular b_*+1 fails this certificate test;
that failure is no lower bound on actual lists.

For a uniform real bound u, take U=Nu to obtain the stated open
test. If u<=TD/N, then Nu/D<=T, which proves the conservative
closed test. Local flooring allows beta_C<1532496 to supply the
integer bound b_* even though this condition alone need not satisfy
the direct unrounded real-cap test.

**Finite values and ordinary-cap comparison.** The counts are

\[
 D=969443904,\quad
 N=1351784971152043422444481951622837254275545242606322734350595980321304252307554394912155112917816320,
\]

and

\[
 M=2136899816051353757057904852229805411030924365970844208573659527927004771612162841121670742371611.
\]

Using these integers in (4) yields b_*=1532495. For completeness,
binomial(963,3)=148379361 and binomial(7,3)=35, so flooring their
ratio yields 4239410. The identity

\[
 \binom{1024}{61}\binom{963}{3}
 =\binom{1024}{64}\binom{64}{61},\qquad
 \binom{68}{61}\binom{7}{3}
 =\binom{68}{64}\binom{64}{61}
\]

follows by choosing a 64-subset and then its distinguished 61-subset
in either order (and likewise within a 68-set). Cancelling the common
positive factor proves (6). This is why ordinary local packing alone
reproduces L001, before local integer rounding. Exact arithmetic
also checks floor(N*4239410/D)>M, whereas
floor(N*1532495/D)<=M<floor(N*1532496/D).

**Verification and limitations.** Run
`python3 scripts/finite-support/core_theta_threshold.py` from the
notebook. It writes the full integer and rational certificate to
`scripts/finite-support/core-theta-threshold-results.json`, including
counts, threshold quotient/remainder, both local real thresholds,
global transfers, exact ratio and all eleven arithmetic checks.
The complete local_caps, global_transfer and checks fields were
inspected. All eleven checks pass; the factorial count checks,
combinatorial identity and strict adjacent-cap tests complement the
symbolic argument. This script neither builds the enormous labeled
graphs nor optimizes any theta body. Its certificate is arithmetic
evidence, not an improved upper bound.

The useful result is a sound finite upper-certificate specification
and its quantitative threshold. A sufficient improved cap, practical
certificate, actual packing/list realization, exact maxima, any
67-agreement transfer and exact t_star(m) remain unproved. Full-SDP
feasibility of the older witnesses is unrelated to the soundness of
this new shared lift. The unavailable ABF comparison remains qualified.

## Mathlib

Full matching shared pair/recursive-theta reduction and its labeled
RS specialization: **not checked** in Mathlib. The recursive theta
input is imported by the precise source citation above; supporting
PSD-minor, finite-incidence and compactness coverage is **not checked**.
Unknown coverage is not evidence of absence. This is REPRODUCTION
of assessed tools with local applicability/counting progress, not a
claim of progress beyond the sources checked or a solution of the
grand list-decoding challenge.
