# L029 — Conditional pair conflicts do not exclude the averaged lift

## Hypotheses

Use L027's fixed instance and definitions of C, V_C, A, J_C and W_A,
and L028's unchanged outer vector f and matrix F. Thus C is any
61-subset of the actual order-1024 subgroup H, A is any seven-subset
of H minus C, and X=H minus (C union A) has 956 points.
Every B in W_A has |A intersect B|=2. On the original vertex set W_A,
let Q_(C,A) be the finite simple graph whose edges are the union of
those of (J_C)_A and all distinct pairs B,B' with |B intersect B'|>=3.
Do not enlarge W_A. Determinant-zero triples remain nonedges of J_C;
pair conflicts independently supply edges of Q_(C,A).

## Conclusion

For every actual C,A the constant vector

\[
 h=\tau\boldsymbol1_{W_A},\qquad
 \tau=\frac{136}{\binom{956}{5}}=\frac1{48419392161},
\]

belongs to IND(Q_(C,A)), hence to TH(Q_(C,A)). Consequently L028's
unchanged f,F satisfies every strengthened row condition

\[
 F_A[W_A]\in f_A\,\mathrm{TH}(Q_{(C,A)}).
\]

All its outer PSD and pair-zero conditions remain satisfied, and its
objective remains 2571353 on every core. Adding these conditional
pair-conflict edges therefore does not exclude this witness or permit
a local cap below 1532496. This tests the specified witness only;
no actual RS list, safety result or general assembled-model soundness
claim is established.

## Proof

**Assessed scope and imported input.** The prior EXPLORE assessment is
[drafts/literature/2026-10-06-conditional-pair-link-obstruction-test.md](../drafts/literature/2026-10-06-conditional-pair-link-obstruction-test.md).
Import independent-set inclusion and convexity from Castro-Silva,
de Oliveira Filho, Slot and Vallentin, *A Recursive Theta Body for
Hypergraphs*, Combinatorica 43 (2023), 909–938,
DOI 10.1007/s00493-023-00040-9, equation (2), p. 911, and Theorem 2.1
with proof, pp. 915–916 ([primary published PDF](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf)).
These apply to every finite simple graph, including the specified
edge union. The source theorem is not reproved. The difference supplied
here is an explicit independent-set mixture for this particular row;
no matching certificate was found in the assessed sources. The affine
intersection calculation below verifies this finite construction and
is not a claim of a new general design theorem.

**An auxiliary family avoiding both edge types.** The integer 191 is
prime: trial division by 2,3,5,7,11,13, all primes at most sqrt(191),
leaves respective nonzero remainders 1,2,1,2,4,9. Let

\[
 \Omega=(\{0,1,2,3,4\}\times\mathbb F_{191})\sqcup\{*\}.
\]

Its size is 956. Assign to each of the 21 pairs U in binomial(A,2)
a distinct slope s_U in F_191; this is possible since 21<=191.
For b in F_191 define the five-subset

\[
 R_{U,b}=\{(x,s_Ux+b):x=0,1,2,3,4\}\subset\Omega.
\]

For fixed U and distinct b,b', these sets are disjoint: equality of
points would give the same x and then b=b'. For U!=U', equality
of points requires

\[
 (s_U-s_{U'})x=b'-b.
\]

The coefficient is nonzero, so there is exactly one possible field
value of x, and at most one in {0,1,2,3,4}. Therefore distinct-slope
sets intersect in at most one point, including the case b=b'.

For any bijection sigma:Omega -> X form the 4011 seven-subsets

\[
 \mathcal I_\sigma=
 \{U\cup\sigma(R_{U,b}):U\in\tbinom A2,\ b\in\mathbb F_{191}\}.
\]

They are distinct: intersection with A determines U; for fixed U,
the outside sets are nonempty and disjoint for distinct b. They all
belong to V_C and meet A in exactly two points. Two vertices using
the same U intersect in exactly the two points of U. Two vertices
using distinct U,U' intersect in at most |U intersect U'|+1<=2.
There are therefore no pair-conflict edges inside this family.

Consider a possible determinant-link edge between two of its vertices
B,B'. Such an edge requires A intersect B intersect B' to be empty,
so their U,U' must be disjoint. In that case B intersect B' is exactly
the intersection of their outside sets, of size at most one. This
contradicts the required pair intersection size two for a hyperedge
{A,B,B'} of J_C. If U,U' are not disjoint, the triple intersection
is already nonempty, again preventing a hyperedge. This argument
excludes the requisite incidence pattern before using any determinant;
it applies to every actual labeling, including singular and antipodal
configurations. It does not declare singular triples forbidden.

It follows that I_sigma=mathcal I_sigma intersect W_A is independent
in Q_(C,A). Restriction only deletes vertices and is performed on the
original W_A for every sigma; no assertion that every two-intersection
vertex lies in W_A is needed.

**Exact constant marginal and mixture.** Choose sigma uniformly among
all bijections Omega -> X. Fix B in W_A and write uniquely
U=A intersect B and T=B minus A, with |T|=5. For each b, the image
sigma(R_(U,b)) is uniform among the binomial(956,5) five-subsets of X:
each possible image admits exactly 5!951! bijections. For different b,
the events sigma(R_(U,b))=T are disjoint, since those outside sets
are disjoint and T is nonempty. Thus

\[
 \mathbb P(B\in I_\sigma)=\frac{191}{\binom{956}{5}}.
\]

Restriction to W_A has no effect on this probability for the fixed
B already in W_A. Therefore the finite average of the independent-set
indicators gives the constant vector with this coordinate in IND(Q).
Since 0<136/191<1, its convex mixture with the empty-set indicator is

\[
 \frac{136}{191}\,\mathbb E_\sigma\boldsymbol1_{I_\sigma}
  +\frac{55}{191}\boldsymbol1_\varnothing
  =\frac{136}{\binom{956}{5}}\boldsymbol1_{W_A}.
\]

The two nonnegative weights sum to one. This proves membership in
IND(Q) and, by the imported theorem, TH(Q). If W_A is empty, every
restricted set is empty and the same formula is the unique empty
vector; L027's empty-link convention is respected.

**Application to the fixed outer lift.** L028 proves f_A=rho>0 and
F_AB/f_A=tau for every B in W_A. Multiplying the proved membership
by this positive f_A proves the strengthened scaled-row condition.
The outer f,F is unchanged, so L028's single shared PSD lift, diagonal,
pair zeros and objective apply without any new averaging of that
outer matrix. The auxiliary F_191 construction supplies only each
link certificate; it is unrelated to the problem field, and its
bijections are not claimed to be automorphisms of the labeled graph.
No compatibility of different link lifts beyond the prescribed outer
rows is required by the tested conditions or established here.

This fixed witness has no zero diagonal, so no division by a zero
variable occurs. Soundness for arbitrary feasible vectors with zero
scaled rows and any stronger model coupling different link matrices
are separate questions. Although every link row is certified by actual
independent sets of that link, these separate mixtures do not exhibit
a joint independent family on V_C or an RS list. The objective remains
strictly above L027's sufficient local threshold; the 955–957 bracket,
67-agreement question, full earlier SDP feasibility and unavailable
ABF comparison remain unchanged.

**Verification.** Run `python3 scripts/finite-support/conditional_pair_link.py`.
The full certificate is `scripts/finite-support/conditional-pair-link-results.json`.
It builds all 4011 abstract vertices and checks all 8042055 unordered
pairs, retaining the complete histogram of the two intersection sizes.
All 12 checks pass. The available coordinate is 191/binomial(956,5),
whereas the required coordinate is 136/binomial(956,5); their ratio
is 191/136 and the thinning weight is 136/191. Complete relevant
certificate fields were inspected. These finite checks support the
construction; the proof of all actual cores and links is the symbolic
restriction and averaging argument above, not numerical optimization.

## Mathlib

Full matching conditional-link certificate: **not checked**. Supporting
finite-field, finite averaging, independent-set and PSD coverage:
**not checked**. Independent-set inclusion in the theta body is imported
by the precise published citation above. Unknown coverage is not evidence
of absence. POTENTIALLY_NEW records the assessed search classification
only; novelty beyond the checked sources is not established. This is an
informative negative result for one repair, not progress on the numerical
safe-radius bracket.
