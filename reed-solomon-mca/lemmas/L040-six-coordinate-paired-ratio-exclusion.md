# L040 — Complete paired-ratio test excludes union-six equality

## Hypotheses

Retain all of L033's hypotheses: F=F_(97^20), H the subgroup of order
sixteen in F_97^*, C the degree-less-than-eight evaluation code on H,
the pinned cell 1/4<=delta<5/16, eight shifted moments, nonzero polynomial
Hankel determinant D and every nonzero coordinate-locator polynomial.
There is an explicit affine lift supported on
U=Z_1 disjoint union Z_2 disjoint union Z_3, with each |Z_i|=2,
f_z(T)=c_z(T-gamma_i) for z in Z_i, c_z in F^*, and three distinct
original finite parameters gamma_i with actual full-weight four-errors.
Assume N_3=0. Counts and finite incidences mean exactly L033's valid
full-weight additional errors in the original chart, with same-support
badness, not merely intersections of projective lines.

## Conclusion

With the complete finite checks specified and independently audited below,
N_ext<=12, and therefore |B(a,b)|<=15. If N_3>0 instead, L010/L033
already give |B(a,b)|<=15, so every L033 union-six pencil has that bound.

The separate critical audit of 2026-10-07 found no defect in this
conditional bound, both finite certificates, or the essential newer
inputs to L039. The initial unverified candidate has therefore passed
this local informal audit. It does not prove that an arbitrary
sixteen-count pencil has a union-six triple. The global interval
11/q–16/q, the arbitrary-family gap, and the challenge-level definition
and parameter qualifications remain unresolved. The result is specific
to the stated subgroup, although the argument retains arbitrary F-valued
weights, parameters and original excluded point [v].

## Proof

### Reduction to one paired evaluation ratio

L010 and L033 give N_ext<=13. Suppose it is thirteen. Only now do we
invoke sixteen-count equality and L039. In its notation, J=H minus U
has a unique disjoint support K_0 of size four, and W=J minus K_0 has
size six. The other twelve additional supports are {x} union K, with
two for every x in U. Every K is {a,w,t}, where a is in K_0 and
{w,t} is an edge of the perfect matching M_a on W. These four
matchings are pairwise edge-disjoint. All errors, tags and parameters
here are those of the original equality pencil.

Fix one selected omission pair Z_i={p,q}. Exactly eight of the twelve
outside triples have tags outside this pair. For any such triple K at
its actual parameter tau, L033 gives
f_z(tau)=lambda g_K(z) for z in U minus its tag, where lambda is nonzero
and g_K(X)=prod_(y in J minus K)(X-y). In particular

    g_K(p)/g_K(q) = f_p(tau)/f_q(tau) = c_p/c_q.

The canceled factor tau-gamma_i is nonzero: tau is additional, rather
than selected. Define h(X)=prod_(y in J)(X-y) and
Q_K(X)=prod_(y in K)(X-y). Since p,q are in U, all evaluations in these
ratios are nonzero, and g_K=h/Q_K at these labels. Consequently

    Q_K(p)/Q_K(q) = rho := (h(p)/h(q))/(c_p/c_q).       (1)

The scalar rho is initially in F^*. There is at least one such triple,
and its left side is in F_97^*, so rho belongs to F_97^*. This does not
require rational individual slopes, affine parameters, or the point [v].
For every label z outside {p,q}, put b_z=(p-z)/(q-z), a nonzero element
of F_97. Then (1) for K={a,w,t} is precisely

    b_a b_w b_t = rho.                               (2)

Thus at least eight edges in the four colored perfect matchings satisfy
(2). Tags on the remaining four triples are unrestricted in this
relaxation; imposing their constraints can only remove configurations.
No inference from necessary ratios to a sufficient moment pencil is used.

### Complete normalization and a finite obstruction

Multiply every label by p^(-1), which belongs to H. This permutes H,
preserves all set sizes and disjointness, sends p to 1, and preserves
b_z exactly because both numerator and denominator acquire the same
factor p^(-1). Thus all possible cases are covered by

* q in H minus {1}: fifteen choices;
* W a six-subset of H minus {1,q}: binom(14,6)=3003 choices;
* K_0 a four-subset of the remaining eight labels: seventy choices;
* rho in F_97^*: ninety-six choices.

The unused four labels are allowed to be arbitrary. In a real pencil
they are U minus {p,q}, but imposing no further selected pairs enlarges
the test domain. The normalization concerns only equation (2) and the
abstract matching incidence; it asserts no invariance of actual weights
or of the original affine parameter chart.

For each fixed q,W,rho and candidate a outside W,{1,q}, define

    E_a = {{w,t} subset W : b_a b_w b_t = rho},
    m_a = |E_a|.

The map z -> (1-z)/(q-z) is injective on these labels: equality of its
values gives (1-q)(z-z')=0, and q!=1. Therefore each E_a is itself a
matching: two edges sharing w would force their other endpoints to have
the same b-value. Different a also give different edge-product values,
so their E_a cannot share an edge. For any four matchings M_a the
number of good edges is at most sum_(a in K_0) m_a. Taking the four
largest m_a among the eight candidate a gives an upper bound independent
of K_0 and of the matching completions.

The complete first check, not a sample, gives maximum eight for this
upper bound over all 45045 pairs (q,W) and all ninety-six rho. Exactly
twenty (q,W) cases attain eight; all have q=96. All other cases have
upper bound at most seven. The distribution of these per-(q,W) maxima is

| Maximum | Number of cases |
| --- | --- |
| 2 | 24 |
| 3 | 4338 |
| 4 | 29890 |
| 5 | 9287 |
| 6 | 1462 |
| 7 | 24 |
| 8 | 20 |

Among the twenty cases, the complete second check tests all rho and all
seventy K_0 choices. There are exactly seventy-two choices with
sum m_a>=8. Every one has sum m_a=8 and m_a=2 for each of the four a.
Hence reaching eight good edges requires M_a to contain both edges of
E_a. Those two edges are disjoint, leaving exactly two W vertices;
the third edge of M_a is uniquely forced. In every one of the seventy-two
cases these four forced completions repeat an edge (in fact two).
They cannot be pairwise edge-disjoint, contradicting L039.

For a completely displayed arithmetic case, take q=96,
W=(8,18,22,27,75,85), K_0=(12,70,79,89), rho=22. The b-values on W
are (87,6,22,91,75,10), and on K_0 they are (68,16,81,29), respectively.
The good edges and forced third edges are

| a | E_a | Forced third edge |
| --- | --- | --- |
| 12 | {8,75}, {22,85} | {18,27} |
| 70 | {18,75}, {22,27} | {8,85} |
| 79 | {18,22}, {27,75} | {8,85} |
| 89 | {8,22}, {75,85} | {18,27} |

For example, 68*87*75=22 modulo 97. All row edges satisfy the same
product equation; the repeated forced edges are explicit. The complete
seventy-two-row table, rather than this example alone, is essential.
Its q,W,K_0,rho values, all eight good edges, all four forced edges and
repeated-edge witnesses are stored in the certificate below. Edge codes
use the displayed sorted W positions, so the compact table loses no
label or matching data. Its complete load-bearing table and all twenty
critical six-sets were inspected with --full, not through previews.

### Reproduction and finite-check coverage

Run, in this notebook,

```bash
python3 scripts/four-matching-ratio/paired_ratio.py
python3 scripts/four-matching-ratio/complete_threshold.py
```

The first writes `scripts/four-matching-ratio/paired-ratio-result.json`.
It constructs H as all x in {1,...,96} satisfying x^16=1 modulo 97,
checks its sixteen elements, and enumerates every q,W described above.
For each case it constructs all fifteen W edges and groups them by
b_w b_t. For each of eight candidate a, multiplying a class value by
b_a places its size in the corresponding rho slot. Thus the 96-by-8
integer table contains exactly every m_a, without rounding or a guessed
field extension. Sorting each row and summing its largest four entries
is exactly the relaxed bound. The output stores the maximum for every
one of the 45045 cases, the full histogram and an extremal witness.
The scope and actual eight versus required eight are printed; zero
check failures were recorded. This maximum alone does not exclude equality.

The second writes `scripts/four-matching-ratio/threshold-completion-result.json`.
It first verifies the first certificate has exactly the expected q,W
case keys, without duplicates or omissions. On all twenty cases at
eight, it directly recomputes every E_a for every rho, enumerates all
K_0 four-subsets, and retains every choice whose sum m_a is at least
eight. Perfect matchings are generated by pairing the first remaining
vertex with each other vertex recursively; all fifteen matchings on W
are obtained. It enumerates all completions containing the good edges,
records each full completion and every repeated edge, and records any
edge-disjoint survivor as a failure. There are seventy-two retained
choices, seventy-two unique completions, zero edge-disjoint completions
and zero failures. It also asserts that every retained count profile is
(2,2,2,2) and stores the full compact forced-edge table. No row is dropped
by a positivity-only test, and no condition on arbitrary F weights is
replaced by testing sampled weights.

The finite proof depends on the complete first enumeration and the
complete second threshold test. It is not an enumeration of pencils,
or an abstract support construction claiming actual moments. The exact
implication is: every hypothetical extension-field equality pencil gives
one case of this necessary rational-label test, and every such case is
excluded. Certificate completeness and the mathematical reduction were
independently checked in the critical audit below. Reproduction commands
and table formats provide concrete review material, not formal verification.

The contradiction excludes N_ext=13. Since L010/L033 already give
N_ext<=13, it proves the stated conditional N_ext<=12. If N_3>0,
L010's multiplicity bound already excludes sixteen and gives at most
fifteen; this separate case uses neither the matching test nor an equality
hypothesis. The original finite chart, actual full weights and same-support
badness are retained through L010/L033 throughout.

### Sources, qualification and review status

Direct mathematical inputs are L010, L033 and L039: the first two supply
finite accounting and the exact overlap formula, and the third supplies
four edge-disjoint perfect matchings under equality. The essential portions
of L039's newer conditional inputs are included in the separate audit below;
their optional involution, quartic and abstract-converse claims are not
certified by this audit.
The standard shortening formula is I. Marquez-Corbella and R. Pellikaan,
*A characterization of MDS codes that have an error correcting pair*,
Finite Fields and Their Applications 40 (2016), 224–245,
DOI [10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
accepted manuscript dated February 29, 2016, section 5, Lemma 5.3 and
its following GRS formula, printed pp. 7–8
([primary manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf)).
L033 already checked its iteration on seven deleted distinct labels with
nonzero multipliers and positive remaining dimension over F. The standard
distance input is J. I. Hall, *Notes on Coding Theory*, GRS chapter,
Theorem 5.1.1, printed pp. 63–64
([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)),
already specialized to n=16,k=8 and distance nine in L010/L033. No new
source hypothesis is asserted and neither known theorem is reproved.

The unchanged prior EXPLORE assessment authorizes the twelve-incidence
attempt and an intermediate uniform obstruction. Classification is
POTENTIALLY_NEW only in its stated bounded-search sense, not certified
originality or progress beyond unread stronger sources. This completes
one coherent paired-ratio attempt with a finite threshold refinement.
It supplies a candidate conditional bound and does not resolve the grand
MCA challenge. In particular there is no universal cluster extraction,
new global error bound, rational original infinity, or ABF26 identification.

### Separate critical audit, 2026-10-07

This is a REPRODUCTION audit under the separately saved EXPLORE scope,
not a new twelve-bound derivation or a claim of progress beyond the
sources checked. It found no defect in the essential symbolic chain or
either complete finite certificate. The preceding attempt's candidate
description is historical; the local conditional bound has now passed
this audit. The challenge remains IN_PROGRESS.

L010's eight shifted moments, kernel, distance-nine uniqueness, locator
factorization, lower-weight multiplicities and same-support arguments
were checked, reusing the existing L032/L033 audits. On the pinned cell
the agreement threshold is twelve. A weight-four parameter has
D(gamma)=det(V)^2 product(e_x x)!=0; a weight-w parameter for w<=3 costs
at least 16(4-w) coordinate-root multiplicities. Thus equality forces
sixteen distinct full-weight supports and degree four at each coordinate,
including possible singular parameters in the preceding bound. Failure
on the complement of the actual error support follows from nonzero
polynomial D and locators; it is not replaced by closeness.

The L033 accounting and overlap formula were checked with all eight
moments, actual weights, cancellations and the original excluded [v].
The six-coordinate lift has weight six away from the three selected
parameters. Distance nine forces any extra four-error to meet U in at
most one coordinate, and shortening on J minus K gives dimension two
or one with precisely the signs and factors displayed in L033. Lower
weights at most two are impossible, and a weight-three error already
excludes equality. Consequently N_ext=13, N_3=0 gives sixteen-count
equality before any later balance argument.

L034's distribution is exact: each U coordinate already occurs twice,
so twelve additional U incidences, each in a different overlapping
support, leave one disjoint support. Its rational-descent proof was also
checked: the paired ratios use tau-gamma_i!=0, rational overlap vectors
give two distinct projective points, and rational linear elimination
gives the remaining direction and normalized weights. L040 uses only
the distribution and proves its required rational ratio directly.
No step requires rationality of the affine chart or original infinity.

L035's packing proof survives every tag case. For any two tags, including
equal tags, some selected four-support contains both. Two outside
triples sharing at least two labels then give union size seven or eight,
forbidden by L032. The same argument excludes triples contained in K_0.
The leave degrees are 9-2d, namely three on K_0 and one on W, and pair
counts give (n_0,n_1,n_2)=(t,12-2t,t), 0<=t<=3. For an intersecting
same-tag pair, any used cross pair between its two exclusive pairs
would produce a forbidden eight-union. The four exclusive labels
therefore have leave degree at least two and must exhaust K_0. This
forces t=2 and makes that tag the unique exceptional tag. These arguments
use distinct actual errors, never arbitrary supports as replacements.

L036's essential alternate lift is legitimate: the actual supports
B_1,B_2,K_0 have union U' of size six, so L032 constructs f' with the
same affine syndrome and its actual values at the three original finite
parameters. U and U' meet only at x. Their difference vanishes on the
five-label complement of their union; the assessed shortening formula
gives residual degree at most two, with parameters [16-j,8-j] at stage
j and next-deletion condition 15-j>=8-j. All retained multipliers are
nonzero. This checks the essential construction and source use without
invoking the later involution or specified-label tests.

L037's completion-shape proof legitimately reapplies L033/L034 to this
actual f'. The unique disjoint supports are already present for both
clusters, and x has exhausted its four incidences. Every remaining
support therefore has exactly one tag in each exclusive five-set and
two labels in their common five-label complement E. L035 forbids reuse
of an E pair, so the ten supports use all ten pairs. Every exclusive tag
occurs twice, with disjoint E edges: the exceptional tag for either
cluster is x. No assertion of independent parameters or weights is used.

L038 then excludes a common two-edge matching in the two tag partitions:
it would repeat an ordered tag pair and create a second intersecting
same-tag pair relative to U, contrary to L035. Its written enumeration
of five-label edge partitions is exhaustive: one matching avoids vertex
0, there are three choices for it, and its two possible partners for
01 force the rest. Each of the six displayed rows covers all ten edges
once; all fifteen displayed intersection witnesses check directly.
Equal rows also intersect. This arithmetic-free proof needs no reliance
on its optional supplementary script.

L039's forward reduction is sound. Two two-K_0 triples give a seven-
or eight-union with K_0 whether their tags agree or differ. If exactly
one such triple remains, its W label cannot occur in a one-K_0 triple
without another forbidden eight-union; its total degree would be at
most two instead of four. Hence every triple has one K_0 label.
Pair packing makes each color's three W edges a perfect matching and
makes distinct colors edge-disjoint. No abstract converse or witness
enumeration is needed for this forward implication.

For L040 exactly eight overlapping supports have tags outside the chosen
omission pair. At their additional parameters the common factor
tau-gamma_i and both g_K values are nonzero. The ratio rho is rational
because Q_K(p)/Q_K(q) from any one actual triple belongs to F_97^*.
Scaling by p^(-1) preserves b_z and permutes H, without transforming
the affine pencil. Fifteen q, 3003 six-sets, seventy residual four-sets
and ninety-six nonzero ratios therefore include every possible
extension-field case. Each E_a is a matching by injectivity of b;
the largest-four sum of its sizes bounds every real K_0 choice.

The independent check is reproducible by

```bash
python3 scripts/four-matching-ratio/audit_certificates.py
```

It preserves both original certificates and writes
`scripts/four-matching-ratio/independent-audit-result.json`, including
their SHA-256 values. It constructs H from sixth powers of the verified
primitive element 5, uses Fermat inverses and direct products for all
120 colored edges of each pair/six-set, and recomputes all 96 relaxed
maxima. It compares every saved case maximum, verifies the exact case
domain without duplicates, and checks the full histogram and witness.
The certificate retains every case's 96 maxima, not only positive cases.
All 45045 cases and 4324320 ratio cases agree. The maximum is eight,
and exactly the recorded twenty six-sets attain it.

On those twenty cases the independent check tests all 134400 choices
of rho and K_0, yielding precisely the saved seventy-two threshold rows.
It generates perfect matchings independently as three-edge subsets with
six distinct endpoints, obtaining all fifteen. Each threshold profile
is (2,2,2,2), so attaining eight requires including every good edge and
forces one completion for each color. All seventy-two full completions
repeat edges; zero edge-disjoint completions survive, whereas equality
would require at least one. Every saved row, all good edges, all full
matchings, all repeated-edge witnesses and the complete compact table
were compared for exact equality. No original threshold shortcut for a
zero count is used; there are no such profiles. No failures were found.

The complete twenty-case and seventy-two-row compact values were read
with the JSON inspector's --full option. The new full summary, source
hashes and empty failure list were likewise inspected. The exhaustive
recomputation and whole-row comparisons, rather than these summaries or
the single displayed arithmetic example, supply the certificate audit.
Its independent source code was checked against the finite domains above.

The existing Hall Theorem 5.1.1 and Marquez-Corbella–Pellikaan section 5
citations and saved primary extracts were reused with unchanged
arbitrary-field hypotheses. No further external theorem, L015 finite
maximum, universal cluster extraction or Mathlib coverage is asserted.
The direct inputs remain L010, L033 and L039; no DAG edge changed.
This validates the local bound |B|<=15 for the stated union-six pencils,
not the unrestricted error maximum or the grand MCA challenge.

## Mathlib

Coverage of the full conditional twelve-incidence theorem, the finite
paired-ratio obstruction and its exact subgroup specialization is **not
checked**. Supporting finite-field, finite-set and matching coverage is
also not checked. No absence or formal-verification claim is made.
