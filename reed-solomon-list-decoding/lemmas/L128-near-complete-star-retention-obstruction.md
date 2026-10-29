# L128 — Near-complete retained common stars still force a two-core size obstruction

## Hypotheses

Let H be a set of size 1024, let K be a 60-subset, and let a,b be
distinct points outside K. Put C=K union {a} and C'=K union {b}.
Use exactly L030's polynomial construction over F_q with

\[
q=137,\qquad T=\{16,64,70,102,112,118,121\},\qquad
\Omega=(T\times\mathbb F_q)\sqcup D_0,\quad |D_0|=4.
\]

Let V be all polynomials of degree at most two, including zero, and
put B_p={(t,p(t)):t in T}. Choose arbitrary bijections
sigma:Omega -> H minus C and sigma':Omega -> H minus C', with
sigma^{-1}(b)=(16,y_0). Define full families of actual 68-subsets

\[
F_L=\{C\cup\sigma(B_p):p\in V\},\qquad
F_R=\{C'\cup\sigma'(B_r):r\in V\}.
\]

Let A_L subset F_L and A_R subset F_R be retained subfamilies.
Their retained common-star families are required to be equal:

\[
W=\{S\in A_L:b\in S\}=\{S\in A_R:a\in S\},
\qquad s=|W|\ge18633.                                      \tag{1}
\]

Equivalently their selection indicators agree for every 68-subset
containing K union {a,b}. Every two distinct supports in A_L union
A_R must intersect in at most 63 points. Equal supports are identified
in that union and are allowed. No full-star retention, probability
law, independence, column-preserving labeling or RS realization is
assumed.

## Conclusion

The retained sizes satisfy

\[
18633\le s\le18769,\qquad
|A_L|+|A_R|\le2552584+2s\le2590122,
\qquad \min(|A_L|,|A_R|)\le1276292+s\le1295061.             \tag{2}
\]

Thus both sizes cannot be at least 1532496. Writing d=18769-s,
where 0<=d<=136, the same bound is 2590122-2d for the sum and
1295061-d for the smaller size. No sharpness or attainability is
asserted.

The separate critical audit of 2026-10-26 below accepts this restricted
intermediate result. It extends the full-star-retention obstruction
only to the specified near-complete common-star hypothesis. It is not
a main-challenge candidate or a universal local cap. Lower overlap,
unequal retained indicators, other distinguished columns, arbitrary
local families or laws, global compatibility and actual RS lists
remain outside this statement. The bracket 955–957 and arbitrary-center
67/68 safety are unchanged.

## Proof

**Scope and previously established inputs.** The prior SPECIALIZE
[assessment](../drafts/literature/2026-10-25-near-complete-star-retention.md)
approves exactly this changed-hypothesis test. L030 supplies the
construction. L127's separately audited statement supplies ambient
equality from ambient overlap. L126's separately audited proof supplies
the structural correspondence and explicit nonstar matching under
ambient-star equality. We use those parts of L126, not its conclusion
with its full-retention hypothesis suppressed. The necessary changes
are transfer of (1) to ambient overlap and counting retained stars
rather than complete stars. No external theorem is reproved: the
finite-group stability input is already part of L127, and the present
count only sums explicit disjoint conflict inequalities, requiring no
maximum-matching/minimum-cover theorem.

**Retained overlap implies ambient equality.** Let

\[
\mathcal S_L=\{S\in F_L:b\in S\},\qquad
\mathcal S_R=\{S\in F_R:a\in S\}.
\]

Every member of W belongs to both ambient stars, since (1) is equality
of actual support families, not just equality of their sizes. Thus
W subset S_L intersect S_R, so their intersection has at least 18633
members. These are exactly the stars of L127: the left condition is
p(16)=y_0, and the right condition is a in sigma'(B_r), with the
same H,K,a,b,T, bijections and left distinguished column. All L127
hypotheses are therefore satisfied. It gives

\[
\mathcal S_L=\mathcal S_R=\mathcal S,\qquad
|\mathcal S|=q^2=18769.                                  \tag{3}
\]

In particular s<=q^2. This argument does not identify W with S;
only W subset S is justified. Positive overlap also ensures that
sigma'^{-1}(a) is an active-column point, since dummy points occur in
no B_r.

**The pairing needs only ambient equality.** L126's structural
subargument, using L125's audited exact-star rigidity, starts from
equality of the full ambient stars after removing K,a,b. Equation (3)
is precisely that equality. Its column and symbol recovery and finite
840-map classification impose no condition on which star members
are retained. Consequently sigma'^{-1}(a)=(16,y_1) for some y_1,
and there exist lambda in F_q^* and u_0,v_0 in F_q such that

\[
\sigma(t,z)=\sigma'\bigl(t,
\lambda z+(t-16)(u_0t+v_0)+y_1-\lambda y_0\bigr)
\quad(t\in T\setminus\{16\},\ z\in\mathbb F_q).           \tag{4}
\]

This is L126 (1), with exactly its arbitrary-label hypotheses.
Neither retained nonstar blocks nor retained star blocks occur in
(4). The other distinguished-column labels and dummy labels remain
unrestricted.

For clarity the resulting ambient pairing and its domain are explicit:

\[
V_L^*=\{p\in V:p(16)\ne y_0\},\quad
V_R^*=\{r\in V:r(16)\ne y_1\},\qquad
\Phi(p)(X)=\lambda p(X)+(X-16)(u_0X+v_0)+y_1-\lambda y_0. \tag{5}
\]

The degree is at most two, and its inverse on V is
lambda^{-1}(r(X)-(X-16)(u_0X+v_0)-y_1+lambda*y_0).
Moreover Phi(p)(16)-y_1=lambda(p(16)-y_0). Thus (5) is the same
bijection V_L^* -> V_R^* proved in L126; the restriction is onto
in both directions, with no retention hypothesis. Both sets have

\[
N=q^3-q^2=2552584
\]

elements. Evaluation at 16 has q^2 polynomials in each fiber, and
the whole space V has q^3 elements. Polynomial-to-support maps on
each side are injective, since agreement at all seven distinct
arguments forces two degree-at-most-two polynomials to be equal.

For every p in V_L^*, (4) identifies the six residual labels with
arguments t!=16 in the two supports
S_p=C union sigma(B_p) and R_p=C' union sigma'(B_{Phi(p)}).
Those labels are distinct and outside K,a,b, by the bijections and
the distinguished-coordinate restrictions. Hence their intersection
contains K and six further points and has size at least 66.
But S_p contains a and excludes b, whereas R_p contains b and
excludes a. They are distinct actual supports, so the upper
intersection bound 63 forbids retaining both. This also checks that
the equal-support exception cannot invalidate any edge of the pairing.

**Counting the retained parts.** Each retained family partitions into
its star part W of size s and its nonstar part. Tag the two sides when
counting their sizes. The polynomial injections and the bijection (5)
partition all ambient nonstar vertices on both sides into N disjoint
forbidden pairs. For each p in V_L^*, the two indicators satisfy

\[
\mathbf1_{S_p\in A_L}+\mathbf1_{R_p\in A_R}\le1.
\]

Summing over every p in V_L^* gives a retained nonstar size sum of
at most N. This inequality holds even when either or both endpoints
of many pairs are deleted. Each support in W contributes once to
|A_L| and once to |A_R|. It must therefore contribute twice to this
sum even though it is identified in the union. There are no other
retained star members by (1), and no nonstar support can occur on
both sides by the a/b distinction. We obtain

\[
|A_L|+|A_R|\le N+2s\le N+2q^2=q^3+q^2=2590122.
\]

Since N=2552584 is even, at least one retained size is at most
N/2+s=1276292+s<=1295061. Substituting s=q^2-d gives (2)'s
equivalent d-bounds. Twice the requested size is
2*1532496=3064992, exceeding the maximum sum bound by 474870;
the maximum smaller-size bound is 237435 below 1532496.
Thus the approved exclusion threshold is met. At s=18633 the sum
bound is 2589850 and the smaller-size bound is 1294925; this is an
endpoint of the displayed bound, not an asserted realizable packing.

**Verification and limitations.** The proof is symbolic and uses the
audited constants q^2=18769, q^3=2571353 and N=2552584 from L126;
no new mathematical script or numerical search is needed. Its essential
new checks are the subset transfer W subset S_L intersect S_R, ambient
applicability of (4) and (5), and the contribution 2s rather than 2q^2.
The separate audit below verifies those implications and the exact hypotheses.
The elementary count does not claim that the matching contains all
conflicts, that any bound is sharp, or that these polynomial families
arise from a common RS center. L030's single-core obstruction and all
independent gaps listed in the conclusion remain intact.

**Separate critical audit, 2026-10-26.** The pre-existing SPECIALIZE
[audit assessment](../drafts/literature/2026-10-26-l128-critical-audit-coverage.md)
approves exactly this verification. Verdict: accepted under the stated
hypotheses, with no strengthened conclusion or claim of sharpness.
The audit reuses the separately audited L126 structural result and
L127 theorem; it does not re-audit their external and finite-computation
inputs or import L126's full-retention conclusion. No new source result
or general theorem is proved. The following checks verify the complete
applicability and counting argument, rather than just its integers.

First, (1) is equality of actual retained support families. For S in W,
membership in the left family gives S in F_L and b in S, and membership
in the right gives S in F_R and a in S. Hence W is a subset of the
intersection of the two ambient stars. This uses both memberships,
not equality of cardinalities. Positive overlap excludes a right dummy
distinguished point. L127 applies with precisely the same field, T,
cores, arbitrary bijections and left column 16; it assumes no retention
or intersection bound on the full ambient families. Its conclusion is
ambient equality and size q^2. It gives no assertion that W is complete.

Second, L126's structural proof uses equality of those ambient stars
after removing K,a,b. Removal preserves equality because all these
supports contain K,a,b. The column and symbol reconstruction and the
accepted exact-star classification are properties of the full stars.
They do not use survival of their members, survival of any nonstar
member, or the retained packing inequality. Thus their conclusion (4)
holds here with nonzero lambda and right distinguished column 16.
This isolates exactly the reusable part of L126 from its later count
of fully retained stars. No unproved column-preserving assumption is
substituted for arbitrary labelings.

Third, (5) and its displayed inverse compose to the identity on V in
both orders. All added terms have degree at most two. Evaluation at 16
annuls the (X-16) term, giving the nonzero-scalar identity for the two
distinguished-value differences. This proves a bijection on both
nonstar complements, including zero and constant polynomials whenever
they belong to a complement. Each evaluation fiber has q^2 elements:
the quadratic and linear coefficients are free and the constant is
uniquely determined. No scalar quotient or exceptional fiber is used.
Within a side, removing its core and undoing its bijection recovers
seven polynomial values; the degree-two root bound proves injectivity.

Fourth, for each of the six t different from 16, (4) identifies the
left label with the right label evaluated at Phi(p)(t). They are
distinct because their left preimages have different first coordinates.
They are outside K,a by the range of sigma and outside b because b
has its unique left preimage in column 16. The right range and its
distinguished preimage give the same exclusions. The intersection
therefore has at least 60+6=66 points. The left support excludes b and
contains a; the right excludes a and contains b. They are distinct,
so the allowed equal-support exception cannot rescue either endpoint
pair. The unrestricted distinguished-column and dummy labels cannot reduce
this guaranteed intersection.

Finally, the bijection and the two support injections partition every
ambient nonstar vertex into exactly one side-tagged pair. At most one
endpoint of each pair survives by the distinct-support bound 63.
Summing these inequalities proves the bound N on the two retained
nonstar sizes without requiring any particular endpoint to survive.
Equation (1) identifies each retained star part with W itself, so their
contribution is exactly 2s. Identifying common supports in the union
does not identify their separate contributions to the sum of sizes.
Thus the bound is N+2s, not N+s and not a count of fully retained stars.
Evenness of N gives the stated integer smaller-size bound directly.

The supplementary complete arithmetic certificate is
`scripts/finite-support/l128-critical-audit-arithmetic.json`.
It checks all 137 integers 18633<=s<=18769, both d-form identities,
both strict threshold comparisons, all endpoint constants, the ambient
and support sizes, and the guaranteed forbidden intersection. Its full
summary and failure list were inspected; all row checks were evaluated,
with no failures. The largest sum bound is 2590122 against required
3064992, and the largest smaller-size bound is 1295061 against required
1532496, with respective shortfalls 474870 and 237435. At the lower
endpoint the bounds are 2589850 and 1294925. This arithmetic supplements,
and does not replace, the universal symbolic checks above.

This audit is REPRODUCTION: local validation of the existing restricted
argument, not discovery beyond the sources checked. It supersedes the
pending-audit qualification in the overview. No mathematical implication
or direct input changes, and no lower-overlap, unequal-indicator,
arbitrary-law, global-extension or RS conclusion is inferred.

## Mathlib

The full near-complete retained-star obstruction: **not checked**.
Supporting polynomial interpolation, finite bijections, indicator sums
and cardinality inequalities: **not checked**. L127 and L126 are local
audited inputs, not assertions of Mathlib coverage. Unknown availability
is not evidence of absence. POTENTIALLY_NEW records only the prior
assessment's failure to establish coverage of this specialization;
neither the imported inputs nor the elementary matching count are
claimed as new general mathematics or certified originality.
