# L133 — A three-shift packing obstruction for L131's fixed maps

## Hypotheses

Use precisely L131's q=137, T={16,64,70,102,112,118,121},
Q=F_137[Z]_{<=2}, subgroup labels h_e=19139^e in F_65537,
K={h_12,...,h_71}, a=h_0, b=h_10, C=K union {a},
C'=K union {b}, and its complete prescribed bijections sigma,sigma'.
In particular sigma(16,1)=b and sigma'(d_0)=a. Put

\[
 A_f=C\cup\sigma(B_f),\qquad D_g=C'\cup\sigma'(B_g).
\]

Let I_L,I_R be subsets of the separate copies of Q. Require
|A_f intersect D_g|<=63 whenever f in I_L, g in I_R and the
supports are distinct. Same-side packing is supplied by L030 and is
not an additional restriction needed for the bound below. Do not
replace either of L131's maps by another map in L130's sample space.

## Conclusion

The complete finite diagnostic produces matching sizes 1, 0 and
2571300 for the forbidden cross pairs (A_f,D_(f+c)), respectively
c=0,1,-1. Here a pair is forbidden only if its supports are distinct
and have intersection greater than 63. Consequently

\[
 |I_L|+|I_R|\le2571406,\qquad
 \min(|I_L|,|I_R|)\le1285703<1532496.
\]

Thus no cross-packed pair for these fixed maps reaches the retention
threshold 1532496 on both sides. The proposed independent-translation
rank-forcing implication has an empty packing premise for these maps.
No nonvacuous rank expansion, arbitrary-map bound, optimal matching,
balanced construction or RS list bound is established. The separate
critical audit below accepts this restricted computational result; it is not a
candidate resolution of the grand challenge.

## Proof

**Coverage and standard input.** The invocation-start EXPLORE
[assessment](../drafts/literature/2026-10-26-packing-assisted-independent-translations.md)
covers exactly the three shifts and this sufficient matching test.
It reuses the primary inspection of Denes Konig, *Graphs and matrices*,
authorized translation of the 1931 paper,
[arXiv:2009.03780v1](https://arxiv.org/pdf/2009.03780v1), unnumbered
main theorem p. 3 and complete graph proof pp. 1–2. The needed input
is only that a vertex cover meets every edge of a matching in distinct
vertices; neither optimality nor matching/cover duality is required.
The explicit application below is included to justify the exact
threshold, rather than to reprove the stronger named theorem.
The sources do not supply these finite instance counts. This is a
local reproduction of the standard certificate method, with no claim
of progress beyond the mathematical methods in the sources checked.

**Supports and distinct tagged vertices.** Each core has size 61 and
is disjoint from its map's image. Each graph has size seven, so all
supports have size 68. All A_f contain a. By sigma'(d_0)=a and the
injectivity of sigma', no graph label has right image a; also a is
outside C'. Thus no D_g contains a, and every cross pair is distinct,
even when f=g. In particular the exception for equal supports never
admits a pair with intersection 68 in this instance.

Within either side, distinct degree-at-most-two polynomials cannot
agree at all seven elements of T by the polynomial root bound. Their
graphs and, by injectivity and disjointness from the core, their
supports are distinct. This is also L030's graph-family argument.
Hence the indices are actual distinct vertices, not a list with
repeated supports. The two sides remain separately tagged.

**Complete finite enumeration.** Write f=u+vZ+wZ^2 and index it by
i(f)=((137w)+v)137+u, using representatives 0,...,136. The scanner
`scripts/finite-support/three_shift_conflicts.c` reads the graph-label
map exponents in the exact order (side,t,y). For every (w,v,u), without
omissions, it evaluates y_t=(u+vt+wt^2) mod 137. It constructs A_f
as a 1024-bit set by adjoining the seven left images to exponent set
{0,12,...,71}. For each of the three c it constructs D_(f+c) by
adjoining the seven right images at (t,y_t+c mod 137) to
{10,12,...,71}. It counts the intersection of these entire supports,
not independent row agreement or intersection only at matching
auxiliary columns. Every possible cross-column image coincidence
therefore contributes. All arithmetic intermediates are below 2^31;
all bit shifts are unsigned and have shift count at most 63.

The resulting full histogram is:

| Intersection size | c=0 | c=1 | c=-1 |
| ---: | ---: | ---: | ---: |
| 60 | 2476739 | 2531504 | 2 |
| 61 | 92931 | 39694 | 2 |
| 62 | 1670 | 155 | 0 |
| 63 | 12 | 0 | 49 |
| 64 | 1 | 0 | 2025 |
| 65 | 0 | 0 | 43330 |
| 66 | 0 | 0 | 467647 |
| 67 | 0 | 0 | 2058298 |
| 68 | 0 | 0 | 0 |

There are no smaller intersections since K is common. Each column
sums to N=137^3=2571353. In the c=-1 scan exactly 53 pairs are
nonqualifying; their sizes are 60 twice, 61 twice and 63 forty-nine
times. Thus exactly 2571300 pairs have intersection 64,...,67.
The other two matching counts are 1 and 0 as stated.

**Full certificate and independent replay.** Run
`python3 scripts/finite-support/three_shift_conflicts.py`.
It compiles the C source, runs all three scans and performs a complete
Python replay. The canonical manifest and all checks are in
`scripts/finite-support/three-shift-conflicts/certificate.json`.
That directory also holds `map-exponents.txt`, one
`shift-<c>-intersections.u8` file per shift with exactly N bytes,
and `shift-<c>-conflicts.u32` files. Each intersection byte has the
above index; every qualifying edge is stored as three little-endian
uint32 values (i(f),i(f+c),intersection), in increasing left index.
The manifest records the paths, lengths and SHA-256 hashes of all six
files. In particular the c=-1 edge file has 30855600 bytes, retaining
all 2571300 edges and their exact intersections.

Before enumeration the Python program reconstructs every subgroup
element by multiplication recurrence and independently reconstructs
the full two maps from L131's ordered signature prescription, including
all dummies and fixed assignments. It compares all 1926 entries,
the complete source supports, cores and parameters with the read-only
L131 embedding certificate. The C input uses these reconstructed maps;
both scripts and the input certificate/map file are hashed in the
manifest. Thus exponent coordinates encode equality of the original
actual labels via a bijection; no field-map or rank invariance is used.

The replay constructs the full supports using Python integers as
1024-bit sets, Horner evaluation ((wt+v)t+u) mod 137, and complete
constant-coefficient lines. It computes all N comparisons separately
for each c and checks every stored intersection byte, totaling 7714059
comparisons with zero mismatches. Both computations check every support
size. The Python program then reads every edge record, compares its
full triple with the corresponding independently replayed entry, checks
that no qualifying entry is missing and that no extra record exists,
and marks both endpoints in separately tagged arrays. All endpoint
counts, histogram entries and record sizes agree. All 66 checks pass
with an empty failure list. This is full finite evidence and a full
replay, not inference from a preview, sampled comparison or optimality
report. The subsequent independent critical audit is recorded below.

**Matching and threshold.** For fixed c, f -> f+c is a permutation
of Q. Therefore every edge in that shift's qualifying subcollection
has a different left endpoint and a different right endpoint. The
record checks confirm this for the actual stored edges. We use only
c=-1; taking the union of different shift lists need not be a matching.

Let E be its 2571300-edge matching. For each edge at least one endpoint
is outside I_L or I_R, since retaining both violates the packing
hypothesis. The endpoints of different edges are disjoint. Assigning
one absent endpoint to each edge therefore gives

\[
 (N-|I_L|)+(N-|I_R|)\ge |E|=2571300.
\]

Rearranging gives |I_L|+|I_R|<=2N-2571300=2571406 and hence the
smaller-side bound 1285703. Alternatively simultaneous threshold
retention permits at most N-1532496=1038857 deletions on each side,
at most 2077714 in total. A matching of size at least 2077715 suffices
to contradict this; the actual matching is larger by 493585 than that
required integer, or by 493586 than the maximum allowed deletions.
These inequalities are sufficient bounds, with no assertion of
sharpness or existence at equality.

**Decision and remaining gap.** This meets the assessed success test
for excluding the fixed-map packing premise, and the abandonment test
for using these maps as a nonvacuous rank-expansion instance. No ranks
or additional shifts were tested. L131's prescribed four supports
still form its valid small packed obstruction; this result concerns
large simultaneous retention and does not alter that construction.
Other labelings, nonvacuous witness forcing and global RS transfer
remain unresolved. It does not refute the RS target or improve the
955–957 bracket.

**Separate critical audit (2026-10-26, step 518).** The invocation-start
SPECIALIZE [audit assessment](../drafts/literature/2026-10-26-l133-critical-audit-coverage.md)
covers exactly this statement and all three complete certificate files
of each kind. The audit accepts the stated restricted bound without
changing hypotheses, counts or mathematical inputs. Run
`python3 scripts/finite-support/critical_audit_l133.py`.
The full read-only-input certificate is
`scripts/finite-support/l133-critical-audit.json`; all 68 checks pass,
with an empty failure list. This is verification of a local input, not
a new matching theorem or certified novelty beyond the checked sources.

The auditor reconstructs every actual subgroup label by modular
exponentiation and the four original supports using the explicit edge
order 12,13,14,23,24,34. It reconstructs the complete maps by ordered
signature queues, including the fixed images and dummies. All 1926
saved map entries, all 1918 graph-image exponents, the complete C input
text, original source parameters, supports and cores agree. Bijectivity
and the entire right inverse image of a, consisting only of d_0, pass.
All four input-file paths and hashes match the production manifest.
Thus both production algorithms use exactly the stated actual-label
maps, including exceptional assignments; neither a field-map nor a
rank-invariance assumption is involved.

For the independent full replay, write each support as K union its
eight actual extra labels (its distinguished point and seven graph
images). The auditor checks on every generated support that these
eight labels are distinct and avoid K. Therefore the full intersection
is 60 plus the cardinality of the two extra sets' intersection. This
uses ordinary sets of actual F_65537 labels, rather than either
production bitset implementation. For every coefficient triple and
each of c=0,1,-1 it reconstructs both sets, including u+c modulo 137,
and compares their intersection with the stored byte. All 7714059
bytes agree, with no equal cross supports. Every qualifying pair's
little-endian triple agrees with its independently reconstructed
(i(f),i(f+c),intersection). There are exactly 1,0,2571300 edge records,
no missing or extra records and no repeated tagged endpoint in any
single shift. Every histogram entry agrees with the table above.
Every field of the C-scan, replay and shift manifests, all six complete
binary-file sizes and hashes, the limitations and all 66 original
check outcomes are checked. Agreement of the two production programs
alone is not used as evidence for any of these conclusions.

Code inspection also checks the complete loop ranges, support equality
predicate, signed wraparound, bit shifts and byte ordering. The maximum
C polynomial-evaluation intermediate is 2007768, below 2^31; exponents
are 0,...,1023 and unsigned shifts are 0,...,63. The all-coefficient
enumeration covers zero and lower-degree polynomials as well as
quadratics. Within-side support distinctness follows from the
injective graph maps and the degree-two polynomial root bound, as in
the proof above; it is not inferred from file indices. Distinct
tagged endpoints plus f -> f-1 bijectivity justify using only that
shift's matching. The audited arithmetic is N=2571353, deletion budget
1038857, required matching 2077715, actual matching 2571300, size-sum
bound 2571406 and smaller-side bound 1285703. No converse, sharpness,
balanced construction, arbitrary-map extension or RS transfer follows.

## Mathlib

Full matching fixed-map theorem and supporting finite enumeration,
bitset, polynomial-root and matching results: **not checked**. No
absence is asserted. The named matching source and the elementary
specialization used here are stated in the proof; no general duality
theorem or new rank result is reproved.
