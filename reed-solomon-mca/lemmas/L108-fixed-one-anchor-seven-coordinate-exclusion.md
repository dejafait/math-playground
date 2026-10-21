# L108 — Fixed seven-set one-anchor equality profile is excluded

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8]. Use L010's shifted moments and the pinned same-support
event on 1/4<=delta<5/16. For the actual original input words a,b,
assume D and every coordinate locator are nonzero polynomials. Suppose
both coefficient syndromes belong to U_S, where

\[
 S=\{1,8,12,18,22,27,33\},\quad P=\{1,8,12\},\quad
 R=\{18,22,27,33\}.
\]

Let f(T) be their unique affine lift supported on S. Assume there is
exactly one original finite bad parameter gamma_0 whose actual sparse
error equals f(gamma_0), and its zero set within S is P. Coefficients,
weights and the original chart may be arbitrary over F. Retain L107's
audited reduction and its inherited L103 finite-certificate qualifications.

This result additionally depends on the complete exact computations
specified below. The separate step-296 critical proof/program audit
found no defect and reproduced all complete artifacts unchanged; the
shared-runtime and inherited finite-certificate qualifications remain.

## Conclusion

The entire original bad set has at most fifteen parameters. More
specifically, the complete necessary fixed-(S,P) t=1 seed filter has
maximum four distinct full two-overlap scalars before original-point
deletion, where equality requires at least nine.

Only this seven-set and this zero triple are covered. No symmetry between
seven-sets or zero triples is asserted. Other t=1 profiles, t=0, other
t=2 splits, arbitrary seven-coordinate representation and challenge
qualifications remain open. The global interval stays 11/q–16/q.

## Proof

### Necessary filter and extension-field completeness

L010 bounds the entire bad set by sixteen, retaining lower-weight and
singular original events. Suppose equality held. L107 applies with t=1
and the given S,P. Inactive lift coordinates are already excluded there
by audited L103. All actual errors are then full and pairwise linear,
and there are at least nine actual two-overlap errors. Each overlap is
PP or PR, with P and R as above.

L107 extracts two disjoint PR edges I_1,I_2 and a third overlap I_3
avoiding both their R labels. Their outside pairs K_1,K_2 differ.
Fix the lexicographic order of the first two PR edges, normalize their
scalars to 0,1, and normalize p_1=1. These three support rows uniquely
reconstruct a lift with

\[
 w(\mu)|_P=p,\qquad w(\mu)_z=A_z\mu+B_z\ (z\in R),
 \qquad p_x,A_z\in\mathbb F_{97}^*,\ B_z\in\mathbb F_{97}.
\]

The third scalar theta is neither 0 nor 1; the base is infinity and is
full on R. Every actual equality lift appears among the
36*36*35*9*36=14,696,640 support seeds. This is L107's proved descent
from arbitrary extension-field coefficients, not sampling those coefficients.

For every retained lift test all 15*36=540 possible PP/PR overlaps I
and outside pairs K. L107's equations (6) and (12) fix the nonzero
multiplier c and unique possible scalar mu; all unused observation
equations and both overlap weights are tested. Nonzero R slopes prove
that any successful extension-field scalar already belongs to F_97.
The two outside weights are -c*g_K(k), nonzero on K. No additional
incidence, coordinate-degree or original-chart filter is used. Extra
seeds incompatible with equality are harmless for this necessary upper
test. Original infinity deletes at most one finite scalar, possibly
nonrational, and cannot increase the predeletion count.

The source comparison reuses the unchanged ready EXPLORE assessment
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
L107 already checks the specialization of J. I. Hall, *Notes on Coding
Theory*, GRS chapter, Theorem 5.1.1, pp. 63–64, and the seven successive
shortenings from Marquez-Corbella–Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, FFAA 40 (2016), section 5,
pp. 7–8, DOI 10.1016/j.ffa.2016.04.004. No standard theorem is reproved
here. The new work implements and verifies L107's previously unevaluated
finite filter; L106's different t=2 table does not supply this count.

### Complete certificate and independent replay

Run from the active notebook:

```sh
c++ -O3 -std=c++17 scripts/seven-coordinate/one_anchor_table.cpp -o /private/tmp/mca-one-anchor-table
/private/tmp/mca-one-anchor-table
python3 scripts/seven-coordinate/verify_one_anchor_table.py
```

The producer records every seed in
`scripts/seven-coordinate/one-anchor-seeds.bin`: one four-byte
little-endian word, either a zero-based candidate ID or high-bit-set
first-failed-gate number. In gate order, numbers 1 through 8 mean:
P consistency; either common R slope zero; theta=0 or 1; third-row
common-R consistency; either reconstructed missing slope zero; remaining
seed observation inconsistency; first overlap weight zero; second overlap
weight zero. Code zero counts seeds passing all gates. The vector is

\[
 (121833,9514152,114672,459996,4456540,2267,0,6631,20549).
\]

The TSV `scripts/seven-coordinate/one-anchor-candidates.tsv` stores every
distinct key (p_1,p_8,p_12,A_18,A_22,A_27,A_33,B_18,B_22,B_27,B_33),
all 540 ordered row dispositions, and its sorted distinct successful
scalars. Rows list PP pairs first, then PR pairs, each lexicographically,
and lexicographic two-subsets K of increasing J=H minus S. Seed ordering
is lexicographic unordered disjoint PR edge pairs, then K_1,K_2 with
K_1!=K_2, then the nine allowed I_3 and all K_3. The binary has exactly
58,786,560 bytes, with no missing or extra seed records.

| Complete test | Actual / required or result |
| --- | ---: |
| Seed cases | 14,696,640 / 14,696,640 |
| Passing seeds | 121,833 |
| Distinct retained lifts | 121,776 |
| Support rows | 65,759,040 / (121,776*540) |
| P-consistency rejections | 50,548,192 |
| R-consistency rejections | 14,845,243 |
| Zero-overlap-weight rejections after consistency | 0 |
| Full row successes | 365,605 |
| Lifts with three distinct scalars | 121,499 |
| Lifts with four distinct scalars | 277 |
| Maximum / necessary threshold | 4 / 9 |
| Independent discrepancies | 0 |

The verifier imports no producer code. It solves each normalized P tree
by a 3-by-3 Gaussian inverse, interpolates missing coordinates from their
two observed scalar values, replays every first-failed seed gate, checks
every reconstructed key against its recorded candidate, and verifies
complete coverage, uniqueness and first-encounter candidate ordering.

For each support A=(I,K), independently form the 8-by-4 moment matrix
M_A with entries z^j, 1<=j<=8. Its first four rows are invertible:
the labels are distinct and nonzero, so this is a Vandermonde matrix
times a nonsingular diagonal matrix. Solve those four equations for
error weights as an explicit linear map of the seven lift values.
Subtract their contributions from moments five through eight. This
gives four residual equations r_0+mu*r_infty=0. In every tested row
r_infty is nonzero, so any compatible mu over any extension is uniquely
-r_0[j]/r_infty[j] at a nonzero pivot; all four residual equations
are then checked. There is no whole-line branch silently omitted.
Recover the weights and retain the row exactly when all four are nonzero.
Every compatible row, 365,605 in total, is checked again in all eight
original moments. Thus the direct moment test independently agrees with
every producer acceptance and rejection, rather than checking only its
success list. All eight moments of each of the 36 generators g_K are
also checked. Distinct supports at a successful scalar cannot coexist
by L010 uniqueness; the verifier checks scalar deduplication explicitly.

The producer summary is `scripts/seven-coordinate/one-anchor-table.json`.
The full replay and artifact hashes are in
`scripts/seven-coordinate/one-anchor-table-verification.json`, with
the raw replay in `one-anchor-table-verification-raw.json` in the same
directory. Selected SHA-256 values are:

```text
one-anchor-table.json
1b14bd10e91e2fa5f554b3eb14d91f0b256d3d5cce61f997eb532e8ee216807a
one-anchor-seeds.bin
8ba78a0dd336e213b90caa0b60f2f1491a92c65e5fbe66d8b6a28595bcc5f82f
one-anchor-candidates.tsv
b1987862c41422f6914e23b33c865aedeb691ebc090199f9bac39b4c31d57136
```

Both implementations use C++ and prime-field arithmetic and share a
compiler/runtime; independence concerns their reconstruction and row-test
paths, not disjoint trusted computing bases. The separate critical audit
below passed. The preserved `.partial-startup` binary and TSV are
unfinished earlier artifacts and are not inputs to the completed bound.

### Contradiction and exact scope

For an equality pencil the extracted seed must pass and match one of
the enumerated lifts, and its at least nine full two-overlap parameters
must occur among that lift's successful scalar rows after original-point
deletion. The complete maximum before deletion is four. Since 4<9,
equality is impossible. L010's integer upper bound then gives at most
fifteen for the entire original bad set, including all lower-weight
and singular events. These events were not discarded to obtain a bound
outside equality: equality itself supplied fullness before this filter.

No assertion is made that each retained lift has t=1, is an equality
profile, or supplies every other bad-support shape. Such additional
filters could only decrease the necessary count. This is local progress
within the assessed model, not progress beyond the sources checked or
a verified challenge solution. Completed classification: REPRODUCTION.

### Separate critical proof/program audit, 2026-10-17

Step 2026-10-17-mca-296-fixed-one-anchor-table-critical-audit found no
mathematical or program defect. It read both complete C++ programs and
the Python comparison wrapper, checked L107's full reconstruction and
L010's event/equality argument, and reused audited L103/L104 and their
qualified source applications. No additional theorem or direct input
was needed. This validates a restricted reproduced result, not a new
global bound or progress beyond the sources checked.

The hypotheses imply L107's exact t=1 premises after supposing sixteen
original bad parameters. Inactive coordinates are excluded by L103;
fullness, distinct supports and incidence balance follow from equality,
not from the finite search. The two disjoint PR edges can be ordered
lexicographically without loss because their distinct actual scalars
can be normalized to 0 and 1 in that order. On P their complement
edges form a tree with nonzero generator ratios. On R the nonzero base
values imply nonzero normalized slopes even for constant original lift
coordinates. Thus all divisions used by the programs are justified for
every actual equality seed. The third row may be PP as well as PR.

Both loops enumerate exactly the 36 unordered disjoint PR edge pairs,
36*35 ordered distinct outside pairs, nine allowed third overlaps and
36 third outside pairs. The test on the second endpoint of I_3 is
sufficient: in the stored ordering PP has both endpoints below index
three and PR has its R endpoint second. The first two R indices are
at least three, so exactly the forbidden R endpoints are removed.
The normalization propagation in the producer terminates in two passes
on the three-vertex tree; the verifier instead solves its three linear
equations by Gaussian inversion. Every first-failed gate is replayed
in order. Generic two-observation interpolation independently reproduces
both missing slopes and intercepts, including all zero-slope rejections.
All three seeds' unused observations and both overlap weights are checked.

The eleven-entry key retains every normalized lift coefficient; exact
key deduplication cannot merge distinct lifts. The verifier rejects
duplicate keys, checks each passing seed against its recorded key, and
checks first-encounter IDs and that every candidate is reached. It reads
the entire binary with no missing or extra record and the entire TSV
with exactly 540 disposition characters and its complete scalar list.
The 540-row loops cover all three PP and twelve PR pairs and all 36
outside pairs, including the seed rows. They impose no additional
incidence pruning that could accidentally exclude an equality pencil.

For independent row coverage, write the four residual moment equations
after inverting moments one through four as r_0+mu*r_infty=0. The
verifier checks r_infty!=0 on every one of the 65,759,040 rows, before
accepting or rejecting it. A nonzero rational pivot forces the unique
possible mu into F_97 even over F_(97^20); all remaining residuals are
then tested. A failed residual excludes compatibility over the entire
extension, while a consistent row has its four weights recovered and
all eight original moments checked. Fullness is imposed only after
compatibility. All 365,605 compatible rows are full in this table.
The shortening-based gate test agrees with this direct moment test on
every acceptance and rejection, including its scalar on acceptance.
The nonzero outside weights follow from c!=0 and distinct generator
roots; zero overlap weights are explicitly tested. Infinity is the
separate R-supported base, never a PP/PR recovery. Distinct scalars
are counted as a set; the no-duplicate-support-scalar check also passes.

All arithmetic operands are reduced modulo 97; the largest unreduced
dot products in these routines have at most sixteen products of two
residues, bounded by 16*96^2=147456, safely within signed 32-bit range.
Counts use 64-bit storage, candidate IDs fit below the binary high-bit
flag, and the stated compile command does not disable producer asserts.
The verifier uses explicit runtime checks. Its Python wrapper compares
all aggregate fields and the complete maximizer-ID list, not a preview.

Both complete programs were rerun. All eight tracked source/output
files, including both replay JSON files, retained their SHA-256 hashes
and byte sizes. The audit certificate is
`scripts/seven-coordinate/one-anchor-critical-audit.json`; the pre-run
baseline is `drafts/2026-10-17-fixed-one-anchor-audit-before.json`.
The replay confirms 121,833 passing seeds, 121,776 distinct lifts,
121,499 scalar sets of size three and 277 of size four; every seed
disposition and all 65,759,040 row dispositions agree. The generated
replay's old "no separate critical audit" qualification records its
creation status; this canonical section records the subsequent audit.

Finally, original-point deletion cannot increase four to the required
nine. L010 includes lower-weight and singular events before equality
is assumed, so ruling out equality proves the stated full-B bound.
No property of the other support shapes or other zero triples is
inferred from this filter. The argument and its direct mathematical
inputs are unchanged; the overview and DAG were therefore preserved.

## Mathlib

Full matching fixed-(S,P) seven-coordinate count and computational
certificate: **not checked**. Supporting finite-field, Vandermonde,
matrix-inverse and GRS-shortening coverage: **not checked**. Unknown
availability is not absence. L107's audited analytic reduction and its
inherited finite-certificate qualifications remain essential.
