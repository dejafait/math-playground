# L110 — Complete equilateral contributions do not certify scaling capacities

## Hypotheses

Let V be the 68-subsets of a 1024-point set and i(A,B)=|A\B|.
Use L021's exact positive rational vector a_i and L098's fixed pairs:

    N=floor(65537^28/2^128)+1, U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i), alpha=2(N-1)/(U-1),
    c_0=1, c_1=...=c_4=0, c_i=alpha*a_i/(2g_i) (5<=i<=68).

Thus N>2, c_i>0 on 5,...,68 and sum_i g_i*c_i=N.
Conditionally assume positive real distance factors f_i for 5<=i<=68,
put x_i=c_i*f_i, and assign to each unordered distinct triangle
z=x_i*x_j*x_h when its three half-distances i,j,h are at least five.
Give weight zero to triangles with a distance in {1,2,3,4}. Assume,
only conditionally, that sum_(Z distinct from A,B) z_(A,B,Z) equals
d_i=(N-2)c_i on every distinct edge A,B. No existence of these factors
is asserted. Keep every actual source index and multiplicity from L109.
The upper capacity of a triangle is b=min(c_i,c_j,c_h).

## Conclusion

For 5<=i<=68 let

    E_i=sum_(t=max(0,2i-68))^i
        binomial(i,t)^2 binomial(68-i,i-t)binomial(956-i,t).

The assumptions imply x_i^3<=d_i/E_i. Consequently each permitted
actual triangle satisfies z<=b*R_(i,j,h), where

    R_(i,j,h)^3=(N-2)^3*c_i*c_j*c_h/(E_i*E_j*E_h*b^3).

The maximum of this particular allowance over all actual permitted
triangles is attained at (5,5,5) and equals exactly

    R_max=(N-2)/89469195005112,
    238*10^80 <= R_max < 239*10^80.

The required test, every R<=1, therefore fails. Park this sufficient
certificate only. This neither proves an actual capacity violation nor
rejects scaling or capacitated primal feasibility. Factor existence,
Boolean lower rows, the full source lift, PSD and RS realization remain
unresolved; the 955–957 bracket is unchanged. This is a local
REPRODUCTION of positive-sum bounds and existing orbit counting, with
no originality claim. The separate critical audit below retains this
conditional certificate failure.

## Proof

**Inputs and source scope.** L098 gives the normalized cardinality
contraction sum_Z y_(A,B,Z)=N*c_i. At A distinct from B the two
endpoint repetitions Z=A,B each have coefficient one and value c_i;
removing precisely those two leaves d_i. At i=0 they coincide and
the row is only the objective. No zero pair is divided out. L109 gives
the actual triangle capacity and fixed-edge coefficient

    D(i,j,t,s)=binomial(i,t)binomial(68-i,j-t)
              binomial(i,s)binomial(956-i,j-s),

for 0<=i,j<=68, max(0,i+j-68)<=t<=min(i,j),
max(0,i+j-956)<=s<=min(i,j), h=i+j-t-s. Its eight-atom construction
realizes every such orbit, and its permutation argument preserves t-s
and all six presentation multiplicities. These results are reused.

The scalar source is Schrijver, *New code upper bounds from the
Terwilliger algebra and semidefinite programming*, IEEE TIT **51**
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p.7. The cardinality source is
Raghavendra–Tan, [arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1),
Section 3, Definitions 3.1,3.3 p.7 and its conditional-cardinality
display pp.8–9. The hypotheses and qualifications remain as recorded
in foundations/04,12,13 and the local specializations: actual orbits
only, no use of Schrijver's qualified (61) prefactor, and no inference
of a global representing measure. No entropy-scaling or convergence
theorem is invoked. Reuse the prior EXPLORE assessment
`drafts/literature/2026-10-23-equilateral-scaling-capacity-test.md`.
The finite allowance evaluation, rather than a reproof of a general
source theorem, is the work needed here.

**Complete equilateral count and conditional bound.** At a fixed
distance-i edge, equilateral third supports have j=h=i, hence s=i-t.
The actual source ranges are exactly max(0,2i-68)<=t<=i; the outside
lower bound is zero since 2i<=136<956. Substitution in D gives E_i.
Each Z occurs in exactly one t class. All distances are positive,
so neither endpoint repetition occurs. The t=i summand is
binomial(956-i,i)>0. L108's exhibited orbit is only this one summand.

Independently, the four fixed-edge regions have sizes 68-i,i,i,956-i.
Write r=|Z intersection (A intersection B)|. Equal distances force
b=68-i-r points in each pair-only part and o=68-r-2b outside the union.
For every 0<=r<=68-i with 0<=b<=i and 0<=o<=956-i there are

    binomial(68-i,r)*binomial(i,b)^2*binomial(956-i,o)

choices. The change r=68-2i+t gives b=i-t and o=t, recovering every
summand of E_i. This complete second count is checked for all 68
positive distances, not inferred from a single orbit or a total preview.

Every equilateral weight at distance i is x_i^3 by the explicit
distance-factor hypothesis. All other marginal terms are nonnegative,
so E_i*x_i^3<=d_i. Multiply the three resulting inequalities for
i,j,h, allowing repeated distances, and use z=x_i*x_j*x_h. Divide
by the positive b^3 and take the increasing nonnegative cube root.
This proves the bound. Null-capacity distinct triangles already have
weight zero and need no division. If every R were at most one this
would certify all upper capacities, conditionally on the assumptions.

**Exact finite verdict and completeness.** Run

    python3 scripts/finite-support/equilateral_capacity_allowance.py

The full certificate is
`scripts/finite-support/equilateral-capacity-allowance.json`.
Only L021's canonical rational primal vector from
`scripts/finite-support/delsarte-lp-results.json` is imported as
numerical input. The script reconstructs the frozen N,c_i and checks
their objective and signs. It saves all equilateral terms and both
count forms, original input hashes, its code hash and all checks.

It exhausts all 1,500,625 original source entries. There are 205
repeated entries, with their D coefficients and the two endpoints
of every distinct edge checked; 10,220 distinct null-capacity entries
have zero incident weight; and 1,490,200 entries have all three
distances at least five. These disjoint counts exhaust the source.
Forbidden repetitions remain in the repeated category. Source entries
retain their original t,s rather than being replaced by formal sides.

For a second exhaustion check, a sorted side triple (i,j,h) is actual
precisely when, writing u=i+j-h, the following integer interval is
nonempty:

    max(0,i+j-68,u-min(i,j)) <= t
       <= min(i,j,u-max(0,i+j-956)).

Indeed this is exactly the intersection of the source t range and
the source s range after s=u-t. Conversely any such t yields an
actual orbit by the nonnegative-atom construction. Independently
generating this side set agrees with the full source pass: 28,215
permitted side classes. Grouping evaluates a bound under the stated
distance ansatz, not a quotient of arbitrary source assignments or
a multiplicative averaging theorem.

Let q be the common denominator and P_i=q*c_i. Every ratio cube is
evaluated exactly as

    (N-2)^3*P_i*P_j*P_h/(E_i*E_j*E_h*min(P_i,P_j,P_h)^3).

The q factors cancel. Independent evaluation through the original
rational c_i agrees in every class. The certificate saves all P_i,E_i,
every side class, its source-entry count, an actual representative and
its exact comparison with one. These factored data specify every full
ratio without decimal truncation. There are 2,902 ratios below one,
25,313 above one and none equal to one. Exact rational maximization
over the complete side set yields (5,5,5). An additional integer
cross-multiplication pass through every saved factored ratio confirms
the maximum and agrees on all comparisons.

That saved-table verification is reproducible by

    python3 scripts/finite-support/equilateral_capacity_verify_saved.py

All 112,867 checks pass without failures. The complete per-class check
record and exact rational maximum allowance are saved in
`scripts/finite-support/equilateral-capacity-saved-verification.json`,
with hashes binding it to the construction certificate and verifier.
This construction pass verifies the saved ratios; it does not independently
establish the source geometry. The separate audit below checks that geometry.

For the load-bearing distance five, the six equilateral terms at
t=0,...,5 are respectively

    7028847, 14161935375, 1793845147500,
    27907525327500, 53339383085625, 6414272480265.

Their sum is E_5=89469195005112. At equal sides the c_5 factors cancel
from R^3, so R=(N-2)/E_5. The exact frozen integer comparisons are

    238*10^80*89469195005112 <= N-2
       < 239*10^80*89469195005112.

One maximizing actual orbit is (i,j,t,s)=(5,5,0,5), with h=5,
t-s=-5 and D=binomial(63,5)=7028847. Index the atoms by membership
bits with A in bit 0, B in bit 1 and Z in bit 2. Their sizes are
(951,0,0,5,0,5,5,58). Thus there are three pair-only five-sets and
a 58-point common core, with 951 outside points. Each support has
68 points, every pair has distance five, and all are distinct. Full
actual sets and all six presentations are saved and checked; every
presentation has that same orbit and positive D. The maximum is
therefore on actual triangles, not impossible formal sides.

All 41,314 construction checks pass without failures. Complete selected
E_5 and maximum records were inspected in full, and all saved ratios
were checked rather than inferred from previews. These are finite
construction checks, not a separate critical proof audit.

**Separate critical audit (2026-10-23, step 414).** Reused the prior
SPECIALIZE assessment `drafts/literature/2026-10-23-l110-critical-audit.md`
and the precise source inputs above. The conditional positive-sum
argument is valid: its equilateral terms are distinct third supports,
the factor ansatz makes all their weights equal, and all omitted terms
are nonnegative. Multiplying three inequalities is valid even when
two or three side indices coincide. No capacity bound or existence
claim is used to obtain that inequality. The two removed repetitions
are exactly those in L098's homogeneous identity; the distance-zero
row is treated separately. The three upper scalar rows follow from
the three anchors of an actual orbit. Boolean lower scalar rows are
not asserted by this upper-capacity calculation.

The independent audit imports no constructor routines. Run

    python3 scripts/finite-support/critical_audit_l110.py

Its complete certificate is `scripts/finite-support/l110-critical-audit.json`.
It reconstructs binomials by Pascal recurrence and the frozen pairs from
L021's canonical rational vector. It then enumerates every third support
class by occupancies (r,p,v,o) in the four fixed-edge regions of sizes
(68-i,i,i,956-i), with o=68-r-p-v. The resulting indices are

    j=68-r-p, h=68-r-v, t=i-p, s=v,
    D=binomial(68-i,r)binomial(i,p)binomial(i,v)binomial(956-i,o).

This is a bijection with the source ranges: its inverse is
r=68-i-j+t, p=i-t, v=s, o=j-s. Thus the enumeration misses no source
entry and counts each exactly once. At every entry it verifies the
eight nonnegative atoms, the original D, and all three anchored values
of g_i*D. Swapping the two nonanchor supports leaves G unchanged by
its symmetric multinomial formula; these three anchor checks therefore
cover all six presentation multiplicities, including coincident keys.
The singleton-minus-opposite-pair identity proves t-s invariance, also
checked at all three anchors. The full coefficient sum at each fixed
i,j is g_j; summing over j gives H. All 205 repetitions, 10,220
distinct null-capacity entries and 1,490,200 permitted entries agree
with the original certificate. No division by a zero pair is used.

Both complete equilateral records agree term by term for all 68
positive distances (1,224 terms); the source enumeration independently
recovers each E_i. A separate side-exhaustion test parametrizes the
common triple intersection k. For prescribed sides i,j,h its interval is

    max(0,68-i-j,68-i-h,68-j-h) <= k
       <= min(68-i,68-j,68-h,1024-i-j-h).

Indeed the three pair-only atoms are 68-i-k,68-j-k,68-h-k,
the three singleton atoms are i+j+k-68,i+h+k-68,j+h+k-68,
and the outside atom is 1024-i-j-h-k. Nonnegativity is exactly
the stated interval, and these atoms construct all supports. For
each sorted side key the number of source entries is the interval's
integer length times the number of distinct permutations of (i,j,h).
This count concerns index keys, not the number of orders of an actual
triangle, which remains six even when distances repeat. It agrees
with the independently enumerated count in every one of the 28,215
classes, with no extra or missing class.

Every saved representative, minimum-pair index, class multiplicity
and ratio comparison is reconstructed from the rational c_i and
independent E_i. All 112,867 assertions in the original saved-table
verification are checked in full; its input/code hashes also agree.
The unique maximizing side class is (5,5,5). The six original E_5
terms sum to 89469195005112, and the exact maximum and its printed
bracket agree. All saved maximizing supports, their eight atoms and
six actual presentations are independently reconstructed. There are
again 2,902 ratios below one and 25,313 above one, with no equality.

All 4,683,180 audit checks pass without failures. The new certificate
retains complete equilateral records, all fixed-edge coefficient sums,
every reconstructed side record, exact maximum, input hashes and
check/failure counts. Original construction evidence is unchanged.
This is independent verification of the existing local specialization,
not a result beyond the inspected sources. It retains precisely the
conditional stop; the excessive allowance need not be attained.

**Scope of the failure.** Other positive terms in each marginal can
make the actual factors much smaller than these equilateral-only
bounds. An allowance exceeding capacity permits but does not force a
violation, and need not be attained by factors satisfying all marginals.
Only this sufficient certificate fails. L105's independent-row pass,
L109's two-distance dual stop and ATTEMPTS/082's parked solve retain
their distinct scopes. No true capacity verdict, scaling existence,
source/PSD feasibility, packing, RS list or boundary change follows.

## Mathlib

Full matching conditional equilateral-capacity diagnostic: not checked.
Finite binomial identities, nonnegative finite sums, rational comparisons
and monotonicity of cubing on nonnegative reals would be supporting
tools, not a matching theorem. Unknown coverage is not evidence of
absence; no Mathlib theorem is assumed.
