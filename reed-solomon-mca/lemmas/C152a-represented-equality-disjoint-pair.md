# C152a — Disjoint actual two-overlap errors in the represented equality class

## Hypotheses

Let F=F_(97^20), let
H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96} be the
order-sixteen subgroup of F_97^*, and put
S={1,8,12,18,22,27,33}, J=H minus S and C=RS[F,H,8] with unit
evaluation multipliers. Use the pinned same-support event at
1/4<=delta<5/16, the original finite bad-parameter set B(a,b), and
the shifted syndrome sigma_j(z)=sum_(x in H) z_x x^j, 1<=j<=8.
Assume the actual Hankel determinant D(T) and every actual locator
ell_x(T) are nonzero polynomials, and |B(a,b)|=16.

Assume sigma(a),sigma(b) belong to
U_S={sigma(z):supp(z) subset S}. Let f(T)=u+Tv be the unique lift
supported on S with sigma(f(T))=sigma(a)+T sigma(b), as in L109.
For each gamma in B use its unique actual error e_gamma. Assume
t=|{gamma in B:e_gamma=f(gamma)}|=0, with equality of vectors on H.
All coefficients, actual weights and the original affine chart are
arbitrary over F.

Retain L086's audited L069 universal five-set bound and L056 complete
gated full-bad-set bound, including L051/L055 counting qualifications.
Retain also L109's L104/L103 smaller-class exclusion, with its audited
L040/L069 finite-certificate qualifications. These inherited finite
computations are inputs, not newly replayed or formally verified here.

## Conclusion

There exist distinct original finite parameters gamma,eta in B(a,b)
such that their actual error supports A_gamma,A_eta are disjoint and
each has exactly two labels in S and two in J. Both errors are full
of weight four.

This is conditional extraction in this represented t=0 class. It
does not identify a particular numeric support pair, transfer any
label-specific moment exclusion, prove a seven-coordinate fifteen
bound, or improve the frozen-model interval 11/q–16/q. Universal
representation and identification with the grand challenge remain open.

## Proof

Apply L086 to the original a,b, determinant, locators, finite chart
and entire B(a,b). Its field, subgroup, dimension, event, nonvanishing,
equality and computational hypotheses are precisely retained above.
Consequently the actual supports A_gamma, gamma in B, are sixteen
distinct full four-sets. Any two intersect in at most one label, and
each label of H belongs to exactly four of these sixteen supports.
The errors and their finite parameters are the original ones.

Define the actual subfamily

    E_2={A_gamma:gamma in B(a,b), |A_gamma intersection S|=2}.

The coefficient-syndrome, equality and t=0 hypotheses are exactly those
of L109's equality clause, at this fixed S and in the same original
chart. Thus L109 gives r=12+n_0 with 0<=n_0<=2 for these actual
two-overlap supports. Here n_0 counts the actual errors other than
equal-lift errors whose supports have no labels in S; t=0 leaves no
equal-lift exceptions. L109's full-activity conclusion uses L104's
smaller-class reduction through L103: if the lift had at most six
active coordinates, its coefficient syndromes would lie in the image
of a six-set and the retained bound would contradict |B|=16. We import
that established reduction with its finite-certificate qualifications;
full activity is not inferred from syndrome membership alone.

Distinctness from L086 makes gamma -> A_gamma injective on the
selected events. Therefore E_2 consists of exactly r distinct sets,
where 12<=r<=14; no relaxed kernel row is counted as an event. Each
member is a four-set and has two labels in S by definition. Since
H=S disjoint union J, its other two labels are in J. For any distinct
A,B in E_2, the same pair is in L086's full family, so |A intersection
B|<=1. For every x in H,

    |{A in E_2:x in A}|
       <= |{A_gamma:gamma in B(a,b), x in A_gamma}| = 4.

Thus the degree relative to E_2 is at most four. It need not be four,
and some labels may be isolated. This restriction changes neither the
ambient H nor S. The displayed H matches the complete /H field of
L109's audited input `scripts/seven-coordinate/zero-anchor-support-filter.json`;
its existing audit generates the subgroup by powers. Reading that field
identifies the saved ambient labels; it is not a new subgroup or
certificate verification.

These are every hypothesis of L152 for this same E_2: the specified
H and S, 12–14 distinct four-sets, the two-plus-two partition,
linearity and maximum degree at most four. L152 therefore supplies
distinct A,B in E_2 with A intersection B empty. Each was selected
from an actual original event, and injectivity gives distinct original
finite parameters gamma,eta realizing them. Their errors were already
full by L086. This proves the conclusion without reconstructing a
kernel vector, invoking a converse, changing the chart or selecting
new weights.

### Sources, reuse and limitations

This is a REPRODUCTION specialization under the prior SPECIALIZE
assessment `drafts/literature/2026-10-25-l152-equality-pencil-applicability-review.md`.
It imports the canonical L086, L109 and independently audited L152;
it does not reprove their coding or general incidence inputs. In
particular the fixed four-row minor in L109 and L151's fixed-pair
exclusion are not premises. No symmetry or moment-exclusion theorem
for the extracted pair follows. The stopped stronger incidence routes
in ATTEMPTS/016,017,027 retain their recorded scope.

The underlying imported standard results retain their precise sources:
J. I. Hall, *Notes on Coding Theory*, GRS chapter, Theorem 5.1.1 and
proof, pp. 63–64 ([primary chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf));
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245, accepted
manuscript 2016-02-29, section 5, Definitions 5.1–5.2, Lemma 5.3 and
following GRS shortening formula, pp. 7–8
([primary manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf));
and Z. Furedi, *Maximum degree and fractional matchings in uniform
hypergraphs*, Combinatorica 1(2) (1981), 155–162, Corollary 3 p. 158,
with plane parameters p. 157
([published scan](https://www.renyi.hu/~furedi/PUBS3/furedi_007_cca1981_fractional_matchings.pdf)).
L086/L109 already specialize the arbitrary-field GRS statements to
sixteen distinct labels, nonzero unit multipliers and dimension eight;
seven shortening deletions leave dimension one and nonzero retained
multipliers. L152 already treats the four-uniform incidence theorem,
its active-vertex plane exception and the partition-sensitive boundary.
This application changes none of those source hypotheses and needs
only the same-family checks above. No advance beyond the sources
checked or mathematical originality is claimed. The separate critical
audit below validates this conditional application at its stated scope.

### Independent critical audit — 2026-10-25

Verdict: **PASS for conditional extraction in the stated represented
t=0 equality class**. Step `2026-10-25-mca-471-c152a-critical-audit`
uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-c152a-critical-audit-review.md` and is
RESEARCH / REPRODUCTION. No missing implication or mathematical repair
was found. This makes the existing application available as an audited
local input; it establishes no result beyond the checked sources.

**Original objects and inherited premises.** L086 has exactly the same
field, subgroup, dimension, pinned radius cell, original a,b and finite
B, with actual D and all locators nonzero as polynomials. Nonvanishing
at every field parameter is not assumed. Its audited conclusion supplies
full actual errors, support injectivity, pairwise linearity and degree
four for the entire sixteen-event family. The L069 universal five-set
bound and L056 complete gated bound, including L051/L055 counting
qualifications, remain inputs. C152a does not substitute a selected
subfamily for B when applying either equality conclusion.

L010's eight-column injectivity applies to the seven supported
coordinates, so coefficient-syndrome membership determines u and v
individually. It gives a single affine lift f on S with the same syndrome
polynomial, not a separately chosen lift at each event. If its active
set had at most six elements, choose a six-set containing that set.
Both u and v are supported there, hence both original coefficient
syndromes lie in its image. L103 permits inactive coordinates, constants,
dependent syndromes and arbitrary extension-field weights and chart.
With the original D, locators and B unchanged, it gives |B|<=15,
contradicting sixteen. Thus L104's full-activity premise is justified;
its L040/L069 finite-certificate qualifications are expressly retained.
This argument requires neither a new representation nor independence
of u and v.

**Identity and completeness of the counted family.** For each original
gamma, sigma(f(gamma))=sigma(e_gamma). The definition of t tests equality
of vectors on all H, so t=0 makes f(gamma)-e_gamma a nonzero codeword for
every gamma in B. L104's distance-nine argument therefore applies to
every one of the sixteen events: with m=|S intersection A_gamma|,
its support is contained in S union A_gamma, of size 11-m, giving
9<=11-m and m<=2. This upper bound uses the fixed S and remains valid
when lift coordinates vanish or cancel against error coordinates.
It never applies distance to the zero codeword. Equal-lift errors
would have been separate exceptions; t=0 removes precisely those.

Consequently the n_m of L104/L109 partition these same sixteen actual
parameters into m=0,1,2, with no additional rows. Degree four on each
of the seven S labels gives the two exact integer balances

    n_0+n_1+n_2=16,       n_1+2n_2=28.

They give n_2=12+n_0 and n_1=4-2n_0. Nonnegative integer counts force
0<=n_0<=2, hence 12<=n_2<=14. This checks L109's count at the actual
event level without using its matrix kernel, converse, fixed minor or
positive control. Since L086 makes gamma -> A_gamma injective, n_2
is also exactly the number of distinct sets in E_2.

**All incidence hypotheses and return to the chart.** The complete
selected certificate field was inspected using
`python3 ../scripts/loop/inspect_json.py scripts/seven-coordinate/zero-anchor-support-filter.json --pointer /H --full`.
It is exactly the displayed H; the default preview alone was not used
as evidence. S is the same seven-set in C152a and L152, with J its
complement in this H. Full four-supports with overlap two have precisely
two labels in each part. Linearity applies to each pair in E_2 because
it already applies in the full actual family. Restriction can decrease
each label's degree from four to any integer between zero and four;
L152 permits these isolated labels and requires no regularity.
Thus every L152 hypothesis holds simultaneously for E_2, with no
edge replacement or ambient-label permutation. Its conclusion selects
two distinct disjoint members of E_2. Each has a unique preimage in
the original finite B by injectivity, and these preimages are distinct.
The original weights are already full, and no direction or chart is
reconstructed, rationalized or omitted.

The direct mathematical inputs remain L086, L109 and L152. The L104,
L103 and L010 checks above inspect inherited implications; they add
no independent premise. The ID-only DAG is unchanged. The earlier
stops in ATTEMPTS/016,017,027 concern stronger or different incidence
implications and remain preserved. The primary distance, shortening
and incidence inspections and the completed L152 audit are reused;
no general theorem or finite certificate was reproved or replayed.
This is an informal applicability audit, not formal verification.
In particular it does not identify either of the label-specific pairs
already excluded elsewhere. Uniform exclusion for the extracted pair,
universal representation and challenge identification remain open.

## Mathlib

Full matching coverage for this conditional coding application:
**not checked**. Supporting coverage for the imported local results
and standard coding/incidence inputs is not checked anew; their
canonical qualifications remain. No library absence or formal
verification is claimed.
