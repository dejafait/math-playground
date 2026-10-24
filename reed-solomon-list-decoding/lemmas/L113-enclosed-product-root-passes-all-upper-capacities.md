# L113 — Enclosed product root passes every upper capacity

## Hypotheses

Use L021's canonical positive rational vector a_i and L098's fixed pairs
on the 68-subsets of a 1024-point set, with half-distance i(A,B)=|A\B|:

    N=floor(65537^28/2^128)+1, H=binomial(1024,68),
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i) for 5<=i<=68.

Use exactly the positive rational box of L112 and its enclosed positive
root x of the 64 distinct-edge contraction equations. No root outside
this box is asserted to be enclosed. Preserve every actual source orbit,
including its t-s, repetitions and null edges, as in L098 and L109.
L110's actual side-class criterion and saved class enumeration are used
only for coverage comparison, not its different equilateral allowance.

## Conclusion

Every vector in L112's unchanged original-coordinate box satisfies, on
every permitted actual triangle with half-distances i,j,h>=5,

    0 < x_i*x_j*x_h/min(c_i,c_j,c_h) <= B < 108/10^13 < 1.    (1)

Here B is the exact maximum upper endpoint ratio saved in
`scripts/finite-support/enclosed-root-all-capacities-verification.json`
at `maximum_upper.ratio`; its side class is (5,5,6), and
107/10^13 < B < 108/10^13. All 28,215 actual permitted side classes
pass; there are no rejected or straddling classes.

In particular L112's enclosed root gives a shared nonnegative triangle
weighting satisfying simultaneously every distinct-edge demand

    sum_(Z distinct from A,B) z_(A,B,Z)=(N-2)c_i(A,B),
    0<=z_(A,B,Z)<=min(c_i,c_j,c_h).

Set z=x_i*x_j*x_h on permitted triangles and z=0 on other distinct
triangles. Null edges have zero demand. Restore the endpoint repetitions
with value c_i and the coincident row as in L112 to recover all 69
original contractions. Thus this fixed-pair upper-capacitated triangle
relaxation has a feasible point, using L112's root-existence input.

This is a local REPRODUCTION of assessed interval/scalar methods, with
no originality claim. Boolean lower scalar rows, a full feasible source
assignment, PSD, a representing distribution, a packing and an RS list
are not conclusions. Global positive-root uniqueness is not claimed.
The 955–957 bracket is unchanged. The separate joint critical proof
review below retains L112 and this extension. It supersedes L112's
historical pending-review sentence without changing that hashed input.

## Proof

**Sources and scope.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-enclosed-root-all-upper-capacities.md`.
Import interval inclusion from Siegfried M. Rump, *Verification methods:
Rigorous results using floating-point arithmetic*, Acta Numerica **19**
(2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5, (5.16)–(5.17), author p.28. Its endpoint enclosure includes
arithmetic expressions with repeated variables; overestimation is allowed.
L112 already specializes the root criterion, Theorem 13.3 and its full
proof, author p.89. We consume its certified box and root without a new
nonlinear solve or a reproof of that theorem. The inspected source and
qualifications are retained in foundations/14.

The scalar upper bounds and permutation convention come from Alexander
Schrijver, *New code upper bounds from the Terwilliger algebra and
semidefinite programming*, IEEE TIT **51** (2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65) and the justification following (65), manuscript p.7.
L109 specializes these to the minimum of the three fixed pair capacities;
foundations/04 retains the actual-orbit and unused-(61) qualifications.
L098 supplies cardinality necessity and normalization, with the primary
framework recorded in foundations/13. Upper capacities alone are only
one part of those necessary source conditions. No source theorem
asserting their sufficiency for PSD or code realization is imported.

**Unchanged endpoints in original coordinates.** Write Q=10^70 and
r=10^25. Let q_k be the saved `point[k]`, and p_k the saved
`scale_powers[k]`, with k=i-5. Precisely as in L112, put

    l_i=10^(p_k)*(q_k-r)/Q,
    u_i=10^(p_k)*(q_k+r)/Q,       5<=i<=68.                (2)

All endpoints are positive rational numbers. The complete certificate
`scripts/finite-support/positive-factor-enclosure.json.gz` and its prior
independent verification are SHA-256 bound to this calculation. Both new
scripts independently reconstruct (2), its scaling, the canonical c_i,
the exact N and the objective sum_i g_i*c_i=N. The earlier verification's
root-certificate hash, all 64 positive inclusion margins and completed
status must agree. These checks preserve that prior input; they do not
constitute a dedicated audit of its root argument.

For each actual permitted side class set b=min(c_i,c_j,c_h)>0. The exact
rational endpoint ratios are

    L_(i,j,h)=l_i*l_j*l_h/b,
    U_(i,j,h)=u_i*u_j*u_h/b.                              (3)

Positivity and interval inclusion give L<=x_i*x_j*x_h/b<=U throughout
the entire box. This remains valid when indices repeat. Checking (3)
is the necessary finite specialization; no independent coordinates or
uniformity of general source variables are assumed.

**All actual source orbits.** The constructor traverses every original
0<=i,j<=68 and

    max(0,i+j-68)<=t<=min(i,j),
    max(0,i+j-956)<=s<=min(i,j), h=i+j-t-s,
    D=binomial(i,t)binomial(68-i,j-t)
      binomial(i,s)binomial(956-i,j-s).

It retains each original D and t-s. Per permitted sorted side class it
saves the number of original entries, sum D, sum g_i*D and an actual
representative, together with both full rational ratios (3). The
independent verifier does not import constructor routines. Instead, for
each fixed edge i it chooses the third support using region occupancies

    0<=r0<=68-i, 0<=a,b<=i,
    o=68-r0-a-b, 0<=o<=956-i,
    j=68-r0-a, h=68-r0-b, t=i-a, s=b,
    D=binomial(68-i,r0)binomial(i,a)binomial(i,b)
      binomial(956-i,o).

These parameters are bijective with the original ranges, by the inverse
r0=68-i-j+t, a=i-t, b=s, o=j-s. All atom sizes are checked against
L109's original eight-atom formula. For all six presentations the verifier
checks preserved t-s and equal full normalized count g_i*D, even when
distance keys repeat. Fixed-edge contractions are never divided by six.

The two enumerations agree class by class on every saved count and both
D aggregates. Their source partition is exactly 1,500,625 entries:
205 repetitions, 10,220 distinct null-edge entries and 1,490,200
permitted distinct entries. Every shell's full coefficient sums are g_j.
For i>0 the two repetitions are (j,t,s)=(0,0,0),(i,i,i), with D=1.
At i=0 all entries are repeated with D=g_j; the row is the unchanged
objective. Null-edge triangle weights and demands are zero. The verifier
also reconstructs all 81,355 nonzero aggregated polynomial coefficients
and compares them with L112's complete system. Thus the capacity test
uses exactly that root's equations and original source coverage.

For an independent class exhaustion, L110's criterion says a sorted
side triple is actual precisely when, writing v=i+j-h,

    max(0,i+j-68,v-min(i,j)) <= min(i,j,v-max(0,i+j-956)).

This is the intersection of the original t range with the s range after
s=v-t, so no formal but unrealizable triangle is introduced. Both
enumerations, this criterion and L110's saved class table have the same
28,215 permitted side classes and the same original-entry multiplicities.
Grouping is legitimate for products under this explicit ansatz; it does
not identify arbitrary source variables at different t-s.

**Complete exact comparisons and consequence.** Run from this notebook:

    python3 scripts/finite-support/enclosed_root_all_capacities.py
    python3 scripts/finite-support/verify_enclosed_root_all_capacities.py

The complete constructor certificate is
`scripts/finite-support/enclosed-root-all-capacities.json.gz`.
It saves every class, both full fractions (3), all class source data,
all rejected/straddling classes, the endpoint extrema and input/code
hashes. Its 1,567,627 checks pass with no failures.

The independent certificate is
`scripts/finite-support/enclosed-root-all-capacities-verification.json`.
It binds the constructor, all inputs and its own code by SHA-256,
reconstructs every endpoint product from integer numerators and
denominators, checks the full reduced fractions, and compares unreduced
integers to determine each sign against one. It reconstructs both global
endpoint maxima over the complete class set. All 3,153,044 checks pass
with no failures. The verification records a hash for every fully checked
class record. No preview or decimal calculation supplies any comparison.

Every upper ratio is strictly below one. The largest is at (5,5,6),
approximately 1.07178856220521422*10^-11; this decimal is descriptive
only. Its full rational value B is saved at `maximum_upper.ratio` in
both certificates and satisfies the exact cross-multiplied bounds
107/10^13 < B < 108/10^13. The maximum lower ratio is at (5,5,5).
Both complete extremal fractions were inspected. In particular all
28,215 upper comparisons pass, with zero rejections and zero straddles.

Inequality (1) now follows throughout the box. Apply it to L112's root,
whose equations already give each positive-edge demand. Null cases and
the restored repetitions follow from the preserved normalization above.
This supplies one feasible point of L109's upper-capacitated triangle
relaxation. It gives no Boolean lower-row, full source, PSD or
RS-realization conclusion and changes no safety/unsafety boundary.

**Separate joint critical review (2026-10-23, step 424).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-23-l112-l113-critical-audit.md`.
This review retains the two conclusions, with their existing scope.
It finds no mathematical inference requiring repair. The source theorem
and exact application are distinguished below; this is a reproduction
and verification of assessed methods, not a claim beyond those sources.

The imported Rump Theorem 13.3 applies on D=R^64: F is the square
polynomial (1) of L112, a is its rational point, E is the closed symmetric
box of radius 10^-45 containing zero in its interior, and R is the full
64-by-64 rational matrix. The entire translated box lies in D. Its
positivity is additionally needed for the product comparisons, not for
polynomial differentiability. The interval J contains every derivative
throughout the box. No nonsingularity of a numerical inverse, iteration
convergence, entropy uniqueness, or global positive-root uniqueness is
assumed. The strict inclusion invokes the cited theorem directly.
L111's existence proof is compatible context; the enclosed root's
existence also follows directly from this verified local application.

The canonical pair vector is exactly L021's saved rational primal vector
with L098's singleton normalization. All demands (N-2)c_i, i>=5, and
all diagonal scales are strictly positive. Multiplying the normalized
polynomial rows by these demands and substituting u_i=x_i/s_i recovers
L111's equation (7) term for term. In a fixed-edge contraction Z is
counted once, so no factor six belongs in that equation. Sorting the two
nonfixed indices only combines identical monomials, including both
ordered contributions; it never deletes an actual t-s class or imposes
a quotient on arbitrary source variables.

The original-orbit/occupancy bijection in this proof exhausts all
1,500,625 entries. The 205 repeated entries, 10,220 distinct null entries
and 1,490,200 permitted distinct entries are disjoint and exhaustive.
The full fixed-edge counts sum to g_j for each i,j. For a distinct edge,
the only repetitions are Z=A,B with coefficient one; at i=0 the
endpoints coincide and the entire row instead sums g_j*c_j=N. Every
permuted eight-atom partition is an actual triple with the same t-s
and full count H*g_i*D. All six presentations, including repeated side
indices, agree. Thus a product assignment on unordered distinct triples
is genuinely shared across every original source presentation. Null
edges require no division, and their contractions are zero identities.
The source's unused complement-prefactor qualification is not invoked.

The audit script is
`scripts/finite-support/critical_audit_l112_l113.py`. It first replays both
independent verifiers to new output files, preserving all old artifacts:
`scripts/finite-support/l112-critical-reverification.json` and
`scripts/finite-support/l113-critical-reverification.json`.
All 4,100,192 and 3,153,044 checks pass, respectively. Every replayed
certificate field agrees with its prior certificate, except elapsed
time. These are complete reconstructions, not sampled record checks.
The first replay verifies every coefficient enclosure, every rounded
product, all residual/Jacobian entries, every preconditioned product,
the complete defect matrix and all 64 Krawczyk images. For integer v
and positive Q, v//Q is floor(v/Q) and (v+Q-1)//Q is ceil(v/Q), also
for negative v. The four endpoint products therefore enclose each
multiplication, regardless of sign; addition is exact in Q-units.
Repeated variable occurrences are separately differentiated.

An additional, different calculation collects each monomial's exponent
multiplicities e_k. Its exact residual contribution is b*product a_k^e_k,
and its derivative in coordinate k is

    b*e_k*product_m u_m^(e_m-1_(m=k)).

Every coefficient is positive and the whole box is positive. Thus each
of these derivative monomials is coordinatewise nondecreasing, so its
exact extrema occur at the common lower and upper corners. Summing the
exact rational corner values encloses every derivative value. These
bounds lie inside every one of the 4,096 saved Jacobian intervals; all
64 exact unrounded residuals likewise lie in their saved intervals.
The 81,355 monomials comprise 64 cubes, 6,324 terms with multiplicities
(2,1), and 74,967 with multiplicities (1,1,1). Consequently this second
calculation checks the complete product rule and repeated-factor cases
without relying on the sequential rounded evaluator. It does not
replace or refine the fixed box, preconditioner or Krawczyk certificate.

All 64 strict inclusion margins agree exactly; their minimum is
9999999999999999999196016 in units 10^-70, against the required positive
margin. The largest defect row bound is exactly
21421458450760567325986134/10^70<1. Both are the manuscript quantities,
not decimal surrogates. The positivity, polynomial identity, full
Jacobian enclosure and strict inclusion establish the claimed local
root and local uniqueness by the imported theorem.

For upper capacities the second replay independently regenerates every
actual class, D aggregate and polynomial coefficient. The additional
audit reconstructs every original-coordinate endpoint product with
exact fractions and checks strict inequalities, including repeated side
indices. All 28,215 classes pass. Both complete extremal fractions agree
with both prior certificates; the maximum upper class is (5,5,6), with
107/10^13<B<108/10^13<1, while the maximum lower class is (5,5,5).
L112's separate distance-five fractions agree as well. The canonical
0<=c_i<=1 check retains the upper bounds for Boolean repetitions;
null distinct triangles have value and capacity zero. This is an upper
bound check only, not a test of the source's Boolean lower rows.

All stored input hashes and constructor/verifier bindings are checked.
The audit additionally binds the complete input artifacts, current
verification code and replay outputs. Its full certificate is
`scripts/finite-support/l112-l113-critical-audit.json`, containing all
64 exact residual fractions, all 4,096 exact derivative corner intervals,
extremal fractions, hash bindings, check counts and any failures.
The additional 113,761 checks pass with zero failures. Both full extrema
were inspected, and every load-bearing array was consumed in full by
the checked reconstruction; previews are not verification.

Reproduce this audit without rerunning candidate generation:

    python3 scripts/finite-support/critical_audit_l112_l113.py

The `--reuse-replays` option consumes the complete separate replay files
and rechecks their full mathematical contents against the originals.
L112's text is preserved because it is hash-bound into the capacity
certificate; the present canonical joint review supersedes its earlier
pending-review qualification. No DAG edge changes: all mathematical
inputs are already direct inputs of L112 or L113. The different stops in
ATTEMPTS/082,093 remain valid. The retained conclusion is exactly shared
upper-capacitated triangle feasibility at these fixed pairs. Boolean
lower rows, full source feasibility, PSD, a representing measure, packing,
RS realization and global root uniqueness remain unresolved. No boundary
improvement or complete candidate follows.

## Mathlib

Full matching finite fixed-box upper-capacity theorem/application: not
checked. Supporting rational inequalities, interval inclusion and finite
subset/orbit enumeration: not checked. Unknown coverage is not absence;
no uninspected Mathlib result is used.
