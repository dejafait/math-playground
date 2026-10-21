# L074 — Ordinary seven/seven scalar rows retain L073's fixed completion

## Hypotheses

Use L053's original singleton normalization on the 68-subsets of a
1024-point ground set:

    N=binomial(1024,68), U=binomial(1024,64)/binomial(68,64),
    M=(U+1)/2, rho=M/N>0.

Retain L021's entire rational vector (a5,...,a68), defined by its
64-by-64 system Ax=1, and the original pairs

    p0=1, p1=...=p4=0,
    p_h=a_h/[2 binomial(68,h) binomial(956,h)] for 5<=h<=68.

Retain exactly L073's included-anchor five/six/seven matrix, every old
L062 moment, L065's original RREF column at u=0,v=v_dagger,w=w_star
from L068/L072, all 28 forced seven/seven entries and all 36 completed
coordinates. The completed vector z is uniquely defined by L073's
36 original defining rows; no new optimization or retuning is allowed.
Use its original positive valency scaling, not z itself as a moment.
The 3708 inherited scalar rows remain required.

Add the ordinary scalar rows at every presentation of every seven/seven
type, including reanchored presentations whose incident distances are
outside {5,6,7}. This tests scalar rows only at those anchors. The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-16-maximizer-seven-seven-ordinary-scalars.md`.

## Conclusion

The unchanged completion satisfies all 1152 new scalar rows: 64 types,
384 ordered presentations, three rows per presentation. Together with
the inherited rows, the same assignment satisfies 4860 scalar rows on
270 types and 1620 presentations and retains L073's PSD matrix.
The new presentations split into 6 Boolean, 84 forbidden and 294
permitted distinct cases. Their minimum scalar slack is exactly zero.
The maximum new permitted distinct ratio satisfies

    211/10^12 <= max y/min(p_a,p_b,p_h) < 212/10^12 < 10^(-9) < 1.

Here y is the actual triple moment divided by rho and a,b,h are the
three half-distances. A maximizing type is (l,m,i,j)=(7,7,1,6).
Thus ordinary scalar rows on this entire represented domain do not
exclude this fixed completion. This is a local REPRODUCTION of assessed
methods, without a source-level novelty claim. Other/excluded-anchor
matrices, unrepresented triples, compatible global moments, measures,
packings and RS realization remain unresolved. Arbitrary-center safety
at 67/68 agreements and the 955–957 bracket are unchanged. The separate
critical review below retains this strengthened scalar conclusion.

## Proof

**Imported theorem and applicability.** Import Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE TIT 51 (2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p.7, including the explanation after (65).
Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved Semidefinite
Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December 2012,
Remark 11 and III.B (31)–(35), conditions (i)–(iv), pp.8–9. The code
hypotheses even d>=4 and d<2w<=n hold for d=10,w=68,n=1024.
Reuse foundations/04's qualifications and L062/L069's normalization.
Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and its complete indicator proof,
p.2, gives the union interpretation, with foundations/12's constant-weight
qualification. These general results are imported, not reproved. None
supplies this fixed assignment's scalar verdict, so finite substitution
is necessary. No stronger source inequality or labeled averaging is used.

For an actual source orbit (a,b,t,s) put h=a+b-t-s. Its conditional
ordered-pair multiplicity is

    O=68!*956!/product_(mask=0)^7 atom_mask! > 0.

There are N*O ordered ground-set triples. The assigned invariant moment
is rho*y, so the normalized source coefficient is
(N*O*rho*y)/(M*O)=y. Consequently the three scalar slacks are precisely

    y, p_a-y, 1+y-p_a-p_b.

All six orders impose every pair upper and lower row. Boolean repetitions
use the original pair coordinate. Impossible orbits and the suspect
complement prefactor in Schrijver (61) are unused.

**Exact pair and witness imports.** Expand

    (1-Z)^j sum_(s=0)^(68-j) binomial(68-j,s)binomial(956-j,s) Z^s

for every j=1,...,64. Its coefficient of Z^h divided by
binomial(68,h)binomial(956,h) is L021's q_jh. Substitution of the complete
saved primal vector gives 1+sum_h q_jh*a_h=0 in all 64 equations.
This verifies the original pair input, preserving L053's factor two.
In particular the extra input is exactly

    a14=136188345662330137488768632668073280/7,
    p14=2825730193896494219/198754391512280403438773149400.

All pairs through p13 agree with L073/L069, and 0<=p_h<=p5 for
1<=h<=14, where p5=1/68881143660. Original rho is retained exactly.

Recover w_star and v_dagger from the rational objective matrices in
L068/L072 and reconstruct all 49 column coordinates from L065's
unchanged augmented RREF, with nonpivots (27,33,42)=(0,v_dagger,w_star).
Every original compatibility equation and all 49 weighted whole-base
kernel residuals vanish. Solve L073's original 36 defining rows by
full rational Gauss–Jordan elimination. The recovered z agrees in every
coordinate with its complete saved witness and independently verified
original-basis solution, including the sole zero z_(7,0).
Check every original 64-mode inequality, its original matrix and right
side, and all 306 saved reduced-block principal minors against L073's
verifier. Thus the scalar test uses precisely the PSD assignment of
L073, whose complete decomposition and critical audit are imported.
No new matrix or a separately chosen scalar witness is substituted.

**Complete new domain and source equalities.** At l=m=7 and
0<=i,j<=7, the full atom tuple in mask order 0,...,7 is

    (942+j,7-j,7-j,j,i,7-i,7-i,54+i).

Its entries are nonnegative, sum to 1024 and give three supports of
size 68. Conversely L073's atom-bijection description exhausts the
seven/seven entries. The third distance is 14-i-j, so distances 0,...,14
occur and p14 is required. For r=7-i,q=7-j retain exactly

    y=p7                             if r+q=0;
    y=0                              if 1<=r+q<=4;
    y=Y_(r+q,7,q,r)                  if r+q=5 or 6;
    y=p7*z_(r,q)/V_(r,q)             if r+q>=7,
    V_(r,q)=binomial(7,r)binomial(61,r)binomial(7,q)binomial(949,q)>0.

These are all 28 forced and 36 completed entries of L073.

For each type construct actual supports D,E,G and all six orders.
Direct set counts give a=|A\B|, b=|A\C|, h=|B\C|,
t=|A\(B union C)|, s=|(B intersection C)\A|. Independently permuting
the atom bits agrees at every order. The full ordered tuple reconstructed
from these source indices is

    (956-a-b+s,b-s,a-s,s,t,a-t,b-t,68-a-b+t).

Compute O both by the factorial expression and by

    binomial(68,t)binomial(68-t,a-t)binomial(68-a,b-t)
    *binomial(956,s)binomial(956-s,a-s)binomial(956-a,b-s).

They agree and are positive in every presentation. Thus every row uses
an actual nonzero source orbit and the stated normalization.

Minimizing the full tuple over the six orders gives one unordered key.
Every coincident key across all 270 types has the same y, including
overlaps with the old and column dictionaries. Grouping by
(sorted(a,b,h),t-s) gives the same keys and values. Completeness follows
from t+s=a+b-h: for an ordered distance triple and fixed t-s, t and s
and hence all eight atoms are unique. This checks exactly the source
permutation equalities rather than imposing distance-only equality.

**All scalar cases.** There is one Boolean type, i=j=7; its six orders
have y=p7. Substituting incident pairs (p7,p7), (1,p7) or (p7,1)
gives nonnegative slacks, including zero upper/lower slacks. The
14 forbidden types have 1<=14-i-j<=4 and y=0; all their 84 orders
pass. They are distinct-support cases, so their lower row is at least

    1-2p5=34440571829/34440571830>0.

The remaining 49 types give 294 distinct permitted presentations.
Exact substitution into every upper row gives the displayed maximum
ratio interval, attained at (7,7,1,6). Equivalently its exact value is

    z_(6,1)/[binomial(7,6)binomial(61,6)binomial(7,1)binomial(949,1)],

with z uniquely fixed by L073's original basis. This full rational
value is saved as `summary.maximum_distinct_upper_ratio` in the
certificate below. All moment signs are nonnegative. Therefore every
pair upper row passes, and every distinct lower row is at least
1-2p5>0. Together with the Boolean cases the minimum new slack is zero.
The complete 3708 inherited scalar slacks are also regenerated and
agree entrywise with L073's unchanged verifier at this maximizer.

Run, from the notebook,

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_maximizer_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/maximizer_seven_seven_scalars.py

The first rerun passes all 4793 original checks. The new exact test
passes 10537 checks with no failed presentation. Its complete artifact
`scripts/finite-support/maximizer-seven-seven-scalars-results.json`
contains input hashes, all pair-system residuals, parameters, the entire
original RREF column, kernel residuals, all 36 recovered coordinates,
all raw Y entries, every atom/source index/orbit multiplicity and all
4860 rational scalar slacks, extrema and empty failure lists. All
load-bearing entries are consumed and compared by the calculation;
bounded metadata previews do not supply its verification. Use
`PYTHONINTMAXSTRDIGITS=0` with the shared JSON inspector for this artifact,
whose exact integer entries can exceed Python's default digit limit.

This parks only ordinary scalar exclusion of this same represented
assignment. ATTEMPTS/055's matrix stop and L067/L071's different fixed
obstructions remain intact. No full SDP feasibility or unsafe list follows.

**Separate critical proof review — step 258, 2026-10-16.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-16-maximizer-seven-seven-scalar-critical-audit.md`.
The review retains this theorem without changing a hypothesis, moment,
source condition or matrix. This is verification of a local reproduction,
not a new mathematical construction or source-level novelty claim.

Check the manuscript against foundations/04,12 and the canonical recipes
in L021,L053,L061,L062,L065,L068,L069,L072,L073. The source hypotheses
hold with d=10,w=68,n=1024. In particular the coefficient is the moment
divided by rho, not a completed z coordinate or an unnormalized count.
The identity N*rho=M and positive conditional multiplicity justify
(N*O*rho*y)/(M*O)=y algebraically, without assuming a measure. Boolean
repetitions retain pairs. No complementary prefactor or labeled averaging
is invoked.

Independently evaluate L021's direct alternating binomial sum, rather
than the construction's polynomial expansion, in all 64 defining
equations. All residuals vanish for the complete original primal vector;
L021 supplies uniqueness of that solution. Its signs and sum U-1 also
agree. Reconstruct all 69 pairs with L053's factor two. In particular
the manuscript's full a14 and p14 fractions agree exactly, all pairs
through p14 are retained, and every nonzero-distance pair used here is
at most p5. Original rho is positive and unchanged.

Recover w_star and v_dagger from the original objective matrices and
all 49 coordinates from L065's augmented RREF. Every original column
equation holds. Recover the 86 positive orbit weights independently from
the four-region binomials, including the anchor of weight one; all 49
weighted whole-kernel residuals vanish. Every column coordinate, weight
and parameter agrees with L073's completed step-254 critical certificate.
The full 36-coordinate completion equals that audited z. Check its exact
35 defining mode rows and e_28, all 64 original inequalities, 36 signs,
the complete original source blocks and all 306 recorded principal minors.
The audited nonzero basis pivots and L073's uniqueness proof identify
this as exactly its original completion. Rebuild all 28 forced entries
and all 36 raw moments using the original positive valencies. All agree.
Thus the reviewed full decomposition, singular ranges and PSD implication
of L073 apply to this same matrix. This review imports that PSD proof;
it does not claim a fresh independent spectral-decomposition audit.

Reconstruct the source domain independently of the saved record list.
For each l<=m in {5,6,7}, fix D, choose E by deleting l points X of D
and adjoining l points Y outside D. Choose G by deleting i points of X
and m-i points of D\X, then adjoining j points of Y and m-j points
outside D union Y. All choices with 0<=i,j<=l exist since the four
region sizes are l,68-l,l,956-l. Conversely every layer-m support has
exactly these four intersection counts. Permutations within the four
regions identify precisely one type for each (i,j). Hence the generated
36+36+36+49+49+64=270 types exhaust the retained domain; seven/seven
has exactly 64 types. Direct membership counts for every point of the
1024-point set and all six support orders recover every saved atom,
source index, third distance and t-s. The complete unordered keys agree
with L073's audited keys. The source-key partition by sorted distances
and t-s agrees, including every overlap across old, column and new types.
Since t+s=a+b-h, this also verifies completeness of source equalities.

For each presentation, count B first relative to A and then choose C
in its four regions. This independently gives

    O=C(68,a)C(956,a)C(a,t)C(68-a,b-t)C(a,s)C(956-a,b-s).

It equals the full factorial quotient and the saved positive multiplicity
in all 1620 presentations. All actual slacks are recomputed and compared
entrywise with L074's complete certificate. Each of the 4860 signs passes.
All 3708 inherited slacks also equal L073's reviewed slacks, allowing for
its different presentation order. Direct support equality identifies
the six new Boolean cases; 84 forbidden cases have y=0; all remaining
294 presentations are distinct and permitted. Every distinct lower
slack is at least 1-2p5>0. Boolean rows account for minimum slack zero.

The complete rational maximum agrees with the manuscript's z_(6,1)
formula and is attained at (7,7,1,6). Exact integer comparisons retain
211/10^12<=maximum<212/10^12<1. The full numerator and denominator
were inspected, and the entire ratio array is recomputed rather than
inferred from a rounded summary. All relevant input hashes, complete
saved scalar records and same-assignment coordinates are consumed.

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_maximizer_seven_seven.py

The standard-library-only audit imports no notebook implementation and
uses no floating arithmetic or optimization. All 15892 checks pass;
the full report is
`scripts/finite-support/maximizer-seven-seven-critical-audit.json`.
It stores original pairs and residuals, parameters, columns, weights,
kernel residuals, completed coordinates, every reconstructed presentation
and scalar slack, exact maximum and input hashes. The complete summary
and empty failure list were inspected. No failed mathematical check or
changed witness is suppressed. Original construction artifacts remain
unchanged. Only ATTEMPTS/056's ordinary scalar diagnostic is parked;
ATTEMPTS/055 and L067/L071's distinct obstructions remain intact.
Other/excluded anchors, unrepresented rows, global moments and RS
realization remain unproved, and the boundary is unchanged.

## Mathlib

Full matching ordinary constant-weight scalar theorem, mixed-layer PSD
specialization and this exact finite certificate: not checked. Supporting
finite-set and rational-arithmetic coverage: not checked. Unknown coverage
is not evidence of absence. No Lean verification is claimed.
