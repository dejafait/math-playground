# L028 — An above-threshold shared lift on every core

## Hypotheses

Use exactly L027's sets V_C, pair graph G_C, labeled hypergraph J_C,
link vertex sets W_A, shared feasible set K_C and maximum beta_C.
In particular C is any 61-subset of H, |H minus C|=963, vertices
are all seven-subsets, pair conflicts have intersection at least three,
and every hyperedge has empty triple intersection and pair intersections
of size two. Retain all determinant-zero triples as nonedges. No core
transitivity, generic-label hypothesis or relation between the auxiliary
field below and the problem's field is assumed.

## Conclusion

For every core C there is an exact rational shared lift in K_C with

\[
 \sum_{A\in V_C} f_A=137^3=2571353>1532496.
 \tag{1}
\]

Thus the proposed uniform cap is false. Even L027's nonuniform
certificate using the sum of floor(beta_C) cannot meet its threshold.
This is a limitation of the precise relaxation, not an actual
J_C-independent family of this size, an unsafe list, or a disproof of
68-agreement safety. The 955–957 bracket remains unchanged.

## Proof

**Assessed scope and known inputs.** This is the above-threshold feasible
lift abandonment test explicitly allowed by the prior EXPLORE
[assessment](../drafts/literature/2026-10-06-core-theta-uniform-cap.md).
We test the unchanged model, not a new hierarchy. Use the polynomial
root argument of L001 in an auxiliary prime field. For graph links,
import IND(J) subset TH(J) and convexity from Castro-Silva, de Oliveira
Filho, Slot and Vallentin, *A Recursive Theta Body for Hypergraphs*,
Combinatorica 43 (2023), 909–938, DOI 10.1007/s00493-023-00040-9,
[Theorem 2.1 and proof, pp. 915–916](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf).
The exact source hypotheses are retained in
[the source note](../foundations/07-core-conditioned-theta-source.md).
No theta theorem is reproved. The work below supplies a particular
finite packing, its averaged matrix and direct link applicability;
these are not numerical optimization or an imported extremal optimum.
The assessed search found no matching certificate; POTENTIALLY_NEW is
only that process classification, not a claim of originality.

**Auxiliary packing.** Put q=137, a prime: none of 2,3,5,7,11 divides
137, and these are all primes at most its square root. On the abstract
963-point set

\[
 \Omega=(\{0,1,\ldots,6\}\times\mathbb F_{137})\sqcup D_0,
 \qquad |D_0|=4,
\]

take the family P of all blocks

\[
 B_p=\{(x,p(x)):x=0,1,\ldots,6\},
 \quad p\in\mathbb F_{137}[X],\quad\deg p\le2,
\]

including the zero polynomial. There are L=q^3 distinct blocks:
equality of two blocks implies agreement on seven distinct field
elements, hence equality by L001's root argument. Distinct blocks
intersect in at most two points. This uses only the auxiliary field;
the 963 abstract points will be mapped to actual labels without
preserving any field operation.

For a fixed p let d_i count other blocks meeting B_p in exactly i
points. Translation p' minus p shows these numbers are independent
of p. A nonzero quadratic vanishing at a prescribed pair of the seven
evaluation elements is a(X-u)(X-v) with a nonzero, and has no other
root. Thus

\[
 d_2=\binom72(q-1)=2856.
\]

At a prescribed evaluation element there are q^2-1 nonzero
polynomials of degree at most two vanishing there (one nontrivial
linear equation in three coefficients, with zero removed).
Counting polynomial/root incidences gives

\[
 d_1+2d_2=7(q^2-1),\qquad
 d_1=125664,\qquad
 d_0=q^3-1-d_1-d_2=2442832.
 \tag{2}
\]

**One shared matrix with pair zeros.** Fix any C and put X=H minus C.
Choose a uniformly random bijection sigma: Omega -> X. Let z_sigma be
the indicator, indexed by V_C, of the seven-subset family sigma(P).
Define

\[
 f=\mathbb E_\sigma z_\sigma,\qquad
 F=\mathbb E_\sigma z_\sigma z_\sigma^t.
 \tag{3}
\]

This is a finite rational average, so it specifies every entry exactly.
The diagonal of F is f since all indicators are zero or one, and

\[
 R(F)=\mathbb E_\sigma
       (1,z_\sigma)^t(1,z_\sigma)\succeq0.
 \tag{4}
\]

Indeed, its quadratic form on (a,u) is the average of the nonnegative
squares (a+u^t z_sigma)^2. On every pair conflict F_AB=0 since none
of the families sigma(P) contains two distinct blocks intersecting in
at least three points. All entries use the same average and matrix.
No claim that sigma(P) is independent in J_C is needed or made.

For clarity an explicit compressed description of every entry is
available. Write v=binomial(963,7), rho=L/v and

\[
 N_i=\binom7i\binom{956}{7-i}\quad(0\le i\le2).
\]

Every fixed seven-subset occurs with probability rho. The permutation
action is transitive on ordered pairs of seven-subsets with prescribed
intersection size i: bijections can be chosen separately on the common,
two unique and outside portions. There are v N_i ordered pairs in
this orbit, whereas any sigma(P) contains exactly L d_i such pairs.
Taking expectations and summing their indicators therefore gives

\[
 f_A=\rho,\quad F_{AA}=\rho,\qquad
 F_{AB}=
 \begin{cases}
  \rho d_i/N_i,& A\ne B,\ |A\cap B|=i\le2,\\
  0,& A\ne B,\ |A\cap B|\ge3.
 \end{cases}
 \tag{5}
\]

This averaging computes the matrix; it is not an automorphism reduction
of the labeled feasible set. Its link constraints are verified next
on the actual labels for each core.

**Every graph-link row is feasible.** If B belongs to W_A, some
hyperedge contains both A and B. By L027's definition |A intersect B|=2.
Consequently (5) gives the same normalized row value on all of W_A:

\[
 \frac{F_{AB}}{f_A}=\tau
  =\frac{d_2}{N_2}
  =\frac{136}{\binom{956}{5}}
  =\frac1{48419392161}.
 \tag{6}
\]

Here f_A=rho>0; there is no division by a potentially zero variable.
For each of the 21 pairs U subset A set

\[
 I_U=\{B\in W_A:A\cap B=U\}.
\]

These parts partition W_A, and each is independent in the graph
(J_C)_A. In fact two vertices of the same part have U contained in
their triple intersection with A, whereas a graph-link edge requires
that triple intersection to be empty. This proof does not depend on
the determinant values. Some parts or the entire link may be empty.

We have 0<21 tau=1/2305685341<1. Even without computing the exact
denominator, binomial(956,5)>=binomial(15,5)=3003>21*136=2856
suffices. Hence on a nonempty link the constant vector tau is the
explicit convex combination

\[
 \tau\boldsymbol1_{W_A}
   =\sum_{U\in\binom A2}\tau\boldsymbol1_{I_U}
       +(1-21\tau)\boldsymbol1_\varnothing
   \in\operatorname{IND}((J_C)_A)
   \subseteq\operatorname{TH}((J_C)_A).
 \tag{7}
\]

Weights are nonnegative and sum to one, also when some I_U are empty.
Multiplying (7) by f_A proves exactly L027's scaled row condition.
Empty links impose no constraint and are harmless. This verifies all
rows, without replacing actual labels or deleting allowed singular or
antipodal triples. Together (4), the pair zeros and (7) prove (f,F) in
K_C. Since v rho=L, its objective is (1).

**Threshold consequence and qualifications.** Construction (3) works
for each of the 61-cores, without identifying their maxima. Thus
floor(beta_C)>=L on every core. Use N,D,M from L027. Its exact largest
successful uniform integer cap is b_*=1532495, so
N*1532496>=D(M+1). Therefore

\[
 \sum_C\lfloor\beta_C\rfloor\ge N*2571353
   >N*1532496\ge D(M+1).
\]

This violates the necessary and sufficient strength test for L027's
first upper certificate; the unrounded certificate fails as well.
The obstruction is stronger than failure of one attempted dual bound:
no valid upper certificate for the unchanged K_C can prove the
requested cap or make this nonuniform core sum sufficient.
It does not address a strengthened model with additional constraints.
The huge theta-feasible independent parts in (7) need not satisfy
pair packing themselves; their only role is to certify graph-link
membership. Requiring additional packing inside each conditional
link would change the model and requires separate assessment.

No family sigma(P) has been shown to satisfy the labeled determinant
restriction, and the averaged matrix is not asserted to be a convex
combination of actual joint-independent families. In particular it is
not an RS realization at a common received word. Arbitrary-center
safety at 67 or 68 agreements, full earlier SDP feasibility, exact
list maxima and ABF equivalence remain unresolved.

**Exact checks.** Run
`python3 scripts/finite-support/core_theta_obstruction.py`.
It writes `scripts/finite-support/core-theta-obstruction-results.json`.
The script enumerates all monic polynomials of degrees zero, one and
two over F_137 and counts their roots in {0,...,6}; multiplication
by 136 accounts for all nonzero polynomials uniquely. The monic
histogram is (17962,924,21) at root counts (0,1,2), independently
confirming (2). All eleven checks pass, including primality, the
packing size, root incidences, link-mixture weights and the strict
objective comparison. The complete histogram, neighbor counts, link
certificate and checks were inspected. This is an arithmetic check;
PSD and every-core applicability follow from the exact proofs above,
not a numerical matrix test or a preview of a huge certificate.

## Mathlib

Full matching averaged-packing obstruction for L027: **not checked**.
Supporting finite-field polynomial root, finite averaging, PSD and
convex hull coverage: **not checked**. Graph independent-indicator
inclusion is imported from the precise Theorem 2.1 citation above.
Unknown Mathlib coverage is not evidence of absence. This is local
negative progress on the assessed relaxation; novelty beyond the
sources checked is not established.
