# L049 — Split cubic recovery excludes disjoint d-tag outside triples

## Hypotheses

Use exactly L043's gated tau=1 local setup over F=F_(97^20),
H the order-sixteen subgroup of F_97^*, k=8 and the pinned cell.
The nine labels are distinct, with

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B.

Keep arbitrary extension-field p,q,r,lambda and distinct original finite
gamma_i, lambda!=0 and p*q*(1-p-q)*r*(1-r)!=0. Suppose two distinct
nonuniversal candidate parameters pass L043 (4)–(7) with witnesses

    K={d} union S, K'={d} union S', S,S' subsets of O, |S|=|S'|=3.

Retain every quotient and finite gate, including mu,nu!=0,-1,
E(mu),E(nu)!=0. Do not impose recovered full weights from (9),
rational original chart, twelve-count equality or a finite universal lift.

## Conclusion

S and S' cannot be disjoint. Combined with audited L048, they intersect
in exactly one label s, which belongs to {w_1,w_2,w_3}. The three pairs
S minus {s}, S' minus {s}, {w_1,w_2,w_3} minus {s} are pairwise disjoint.
Thus every pair of distinct d-tagged candidates falls in L048's
single-intersection case. With full recovered weights, its conditional
recentered actual tau=1 triple follows.

The new disjoint exclusion depends on the complete exact finite
certificates below. It is uniform in the stated extension-field weights
and original parameters because its necessary label test is independent
of them. It is specific to this H; it is not a general MCA theorem.
It neither forces two d-tagged candidates nor bounds all nonuniversal
candidates by eleven. The global 11/q–16/q interval is unchanged.
The finite computation and independent verification completed on
2026-10-08. A separate critical proof/certificate audit on 2026-10-09
found no defect within these hypotheses; its full checks appear below.
POTENTIALLY_NEW is a literature-search classification, not certified originality.

## Proof

### The necessary simultaneous label test

Let f(X)=product_(x in S)(X-x), f'(X)=product_(x in S')(X-x),
and W(X)=product_(i=1)^3(X-w_i), all monic cubics in F_97[X].
The scoped audited full-moment input in L048 proves, for arbitrary
distinct d-tagged candidates (before any intersection assumption),
that there are u,u'!=0 in F such that

    -mu*f(y_i)=u*W(y_i),       f(z_i)=u*W(z_i),
    -nu*f'(y_i)=u'*W(y_i),     f'(z_i)=u'*W(z_i),  i=1,2.

These are consequences of all eight moments supplied by L043 (4)–(7),
not tests of only four moments. The recurrence input is the already
inspected specialization in L043 of Przemek Chojecki, *Shortening Bounds
for Reed–Solomon MCA*, live author TeX v9.2, July 17, 2026,
source lines 2785–2935, `drc:lem-locator-recurrence` (DR2) and
`drc:thm-exact-compiler` (DR6–DRC),
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The mutable source is not certified identical to ePrint 2026/1463.
We reuse L048's checked full-moment derivation and do not reprove the
standard recurrence theorem or assume the remaining unaudited L046 claims.

All values of f,f',W at y_i,z_i are nonzero: their roots lie in O,
disjoint from these four labels. Also mu,nu,u,u' are nonzero. Dividing
the two y-equations, and separately the two z-equations, gives

    f(y_1)/f(y_2)=f'(y_1)/f'(y_2)=W(y_1)/W(y_2),
    f(z_1)/f(z_2)=f'(z_1)/f'(z_2)=W(z_1)/W(z_2).       (1)

No h or d equation has been discarded as sufficient: (1) is only a
necessary condition. Dropping those equations enlarges the tested set,
so impossibility in this set is a valid obstruction to actual recovery.
No descent of the free weights is used.

The three root sets S,S',W are distinct. L048's scoped checked argument
excludes S=S' for distinct admitted parameters. If S=W, monicity gives
f=W, the z-equation gives u=1, and the y-equation gives mu=-1,
excluded by L043. The identical argument excludes S'=W. Hence (1)
places three distinct cubics in one ratio class.

### Normalization and the finite overapproximation

Normalize labels by x -> x/h, solely to compare them with the finite
certificate. Since h is a nonzero member of H, multiplication by h^-1
permutes H and sends h to 1. For a cubic f replace it by
h^-3*f(hX); this is monic with the normalized roots. Ratios at the
normalized y- or z-pair equal the original ratios, since the common
factor h^-3 cancels. Thus (1), distinctness and intersections are
preserved. This normalization imposes no change or rationality on the
original gamma_i, lambda,p,q,r or excluded affine direction.

With h=1, the two unordered y-labels have C(15,2)=105 choices and
the disjoint unordered z-labels have C(13,2)=78 choices. Ordering each
pair increasingly changes no equality in (1). Both y/z roles are retained;
no symmetry interchanging them is assumed. There are 8190 choices.
For each choice, let R=H minus {1,y_1,y_2,z_1,z_2}; |R|=11.
The actual S,S',W lie in R minus {d}, but the certificate deliberately
includes all C(11,3)=165 triples of R, without choosing d. This is an
overapproximation and cannot lose an actual configuration.

For each triple T of R let f_T be its monic root cubic. Group all 165
triples by the key

    (f_T(y_1)/f_T(y_2), f_T(z_1)/f_T(z_2)) in F_97^* x F_97^*.

All denominators are nonzero. The complete verified finite statement is:
**every two triples in a key group of size at least three intersect.**
Applying it to the three distinct cubics in (1) excludes disjoint S,S'.
L048 then gives their exact single-intersection and residual-pair claims.
Those claims become actual full-error recentering only under its
recovered-weight qualification; it is not removed here.

### Complete certificates and exact verification

Reproduce, from this notebook, in order:

    python3 scripts/simultaneous-recovery/disjoint_d_pair.py
    python3 scripts/simultaneous-recovery/verify_disjoint_d_pair.py

The complete grouping certificate is
`scripts/simultaneous-recovery/disjoint-d-pair-result.json`.
It records every Y/Z choice, every key and every triple in every group,
including singleton and two-element groups. The search computes cubic
values as products of root differences and groups using modular inverses.
Its h-recovery/weight-witness branch is not needed for this negative
certificate: no disjoint pair in a group of size at least three exists.
We rely on the independent checker for this stronger absence statement,
not on the search's candidate-filtered counter alone.

The independent full verification certificate is
`scripts/simultaneous-recovery/disjoint-d-pair-verification.json`.
The checker reconstructs H as all nonzero residues whose sixteenth power
is one, enumerates all 8190 Y/Z choices independently, and checks exact
equality of the saved and required choice sets, with no duplicates.
For each choice it constructs all required 165 triples and verifies that
the groups form exactly this partition, with no missing or repeated triple
and no repeated key. It evaluates each cubic independently by Horner's
method on coefficients (1,-a-b-c,ab+ac+bc,-abc), rather than the search's
product formula. It checks nonzero values and both key equalities by
cross multiplication, using no inverse-table grouping from the search.
It then checks the intersection of every pair in every group of size
at least three. Every operation is exact modulo 97; no tolerance,
random sampling, positive-only certificate or extension-field enumeration
is involved. Per-choice verification records are saved in full.

All 1,351,350 cubic memberships pass those partition and ratio checks.
The complete group-size histogram is

| Group size | Number of groups |
| --- | --- |
| 1 | 1,314,906 |
| 2 | 4,992 |
| 3 | 1,680 |
| 4 | 4,830 |
| 5 | 420 |

There are 6,930 groups of size at least three, containing 38,220 pairs;
all those pairs were checked and none is disjoint. The required threshold
for a surviving disjoint pair was one; the actual count is zero.
Both scripts terminated successfully, with no recorded failures.
The complete verifier `/summary`, search `/statistics` and both histogram
values were inspected, alongside the full `/first_large_group` value.
For example Y={8,12}, Z={18,70}, key=(3,43) has triples
{27,33,47}, {27,50,64}, {27,85,89}, illustrating an intersecting
large group; this example is not used in place of the complete checks.

The checker reads and verifies the complete grouping artifact. A bounded
JSON preview does not supply this evidence. The structural documentation
checker likewise does not validate the mathematical reduction or code.
The proof depends on these exact finite certificates and their stated
verification; the separate critical audit below checks the reduction,
completeness and implementations. No broader sharp count,
challenge solution, arbitrary triple extraction or general-domain claim
is inferred from the finite computation.

### Separate critical proof and certificate audit (2026-10-09)

The audit found no defect in the stated fixed-H exclusion. This validates
an existing local input; it is not a new count bound or certified novelty.
The original producer and verifier were read in full and replayed in
order with ordinary `python3` (assertions enabled). Both exited zero.
Their two complete output files are byte-for-byte identical to the saved
pre-audit artifacts, verified by SHA-256. The replay therefore validates
the existing certificate, rather than silently replacing a failed one.

For the mathematical reduction, the checked L048 full-moment argument
applies before its intersection assumption. In L043 notation, N_K has
an all-eight-moment representative omega on K, even if a coefficient
vanishes. The word n-omega is nonzero because its four singleton entries
are c_y*(-mu), c_z, all nonzero. Its moments vanish, and it vanishes at
the seven labels O minus S. L010's shifted-moment kernel is the degree
at most seven evaluation code. Thus its polynomial is a nonzero scalar
multiple of the product on O minus S. Multiplication by f at the five
labels B minus {d}, and the identity Q*W=product_(o in O)(X-o), give
exactly L048's equations. This rechecks the scoped input application,
not a reproof of the imported recurrence theorem. No unreviewed opposite-
tag conclusion of L046, L044 descent or L045 profile is required.

Every evaluation divided by in (1) is nonzero, since all cubic roots
are outside B. Distinct original parameters give distinct quotient
scalars: T=gamma_0+g*rho/[rho+(rho-1)mu] has nonzero numerator and
nonzero denominator slope. If f=f', the z-equations force u=u', then
the y-equations force mu=nu. If f=W, a z-equation gives u=1 and a
y-equation gives mu=-1. Both contradictions use retained gates, and
apply equally to f'. Thus the group really contains three distinct
triples; a pair-only test would not suffice. Ratios are prime-field
values regardless of extension-field p,q,r or original chart.

Multiplication by h^-1 sends H bijectively to H and each root cubic to
h^-3*f(hX). It preserves ratio equalities and disjointness. Sorting
within either pair replaces a ratio by its reciprocal if necessary;
it preserves equality among all three cubics. Y and Z remain separate
roles. Every normalized actual configuration appears among the 8190
choices: h=1 is removed, then the two disjoint pairs. All actual cubic
roots avoid d, but permitting d among the eleven remaining labels only
adds triples. Thus dropping d, the h equation, recovered-weight gates
and all other sufficiency conditions cannot remove an actual witness.
There is no assumption that these extra tuples are realizable pencils.

The verifier constructs its required choices and all 165 triples per
choice independently of the supplied keys. It enforces choice membership
and uniqueness, equality of complete choice sets, triple membership and
uniqueness, equality of each complete triple set, and key uniqueness.
For every triple its Horner evaluation of the expanded monic cubic
checks all four values nonzero and both ratio equations by cross
multiplication. Since denominators are nonzero, the key is uniquely
determined. Consequently equal-key triples cannot be separated across
different groups, and differently keyed triples cannot enter one group.
It enumerates every unordered pair in every group of size at least three,
without mu, weight, h-recovery or d-availability filters. Its zero failure
list proves the needed stronger statement. The producer's filtered
`disjoint_pairs_tested=0` would not prove it alone. The producer's unused
positive-witness branch and its preliminary docstring are not evidence
for the negative conclusion; completeness comes from the verifier.

The complete saved per-choice verification records were also checked
against all grouping cases by

    python3 scripts/simultaneous-recovery/audit_disjoint_d_records.py

This supplementary check reads both entire artifacts, checks every
per-case count and all summary/histogram totals, and compares replay
hashes with `drafts/2026-10-09-disjoint-d-audit-before.json`. Its full
record is `scripts/simultaneous-recovery/disjoint-d-critical-audit.json`.
It verifies that the listed H has sixteen distinct roots of X^16-1
and an element generating all of them; the root bound identifies it
with the full root set and hence the required subgroup. This is also
consistent with the verifier's exhaustive residue construction of H.
The supplementary script checks recorded evidence; the preceding full
verifier replay supplies every membership and pair check.

Actual and required choice counts agree at 8190, and membership counts
agree at 1,351,350. The full histogram is the table above; its 6930
large groups contain exactly 38,220 pairs. All pairs were checked;
actual disjoint pairs are zero, while one is required for a surviving
configuration. The consistency check reports no failures. No selected
example, preview, printed summary or structure checker substitutes for
this complete computation.

Finally audited L048 supplies at most one common root and, when there
is one, its membership in W and the three disjoint residual pairs.
The new exclusion eliminates only the zero-intersection alternative.
Recentered actual errors still require both recovered words to be full.
Existence of two d-tags, exclusion of their surviving intersection,
other tags and B-disjoint candidates, both twelve profiles, eleven,
arbitrary-support extraction and ABF26 identification remain unresolved.
The argument and direct mathematical inputs are unchanged, so the DAG
requires no new edge. This is a scoped informal audit with exact finite
certificates, not a Lean proof or general-domain theorem.

## Mathlib

The full fixed-H disjoint-d exclusion and finite certificate: **not
checked** for matching Mathlib coverage. No absence claim or Lean
formalization is made. The standard supporting factor and root bounds
and their field hypotheses are already documented in audited L048:
`Polynomial.dvd_iff_isRoot` and `Polynomial.mul_divByMonic_eq_iff_isRoot`
in [Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean),
and `Polynomial.card_roots`, `Polynomial.mem_roots` and
`Polynomial.card_le_degree_of_subset_roots` in
[Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean).
Those source inspections were of mutable master, without a pinned commit.
Here the required polynomial facts are reused through L048, and (1) and
normalization use field arithmetic. The new load-bearing finite grouping
has not been imported from Mathlib or claimed to be known mathematics.
