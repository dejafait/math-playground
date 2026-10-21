# L045 — Four-column Gilbert certificates fall below the benchmark

## Hypotheses

Let Omega={0,...,8} times F_107, partitioned into nine labeled columns.
Let U be all nine-subsets meeting at most four columns. Let P be the
set of decreasing positive partitions of nine with at most four parts.
For a in P, let U_a contain every member of U with profile a, including
all placements on the labeled columns and all choices of points.
Two distinct blocks conflict exactly when their intersection has size
at least five. A closed neighborhood also contains its selected block.

The prescribed lower certificate for a universe V is the finite
Gilbert maximum-closed-neighborhood bound ceil(|V|/D_V), where D_V
is the greatest closed-neighborhood size within V. Test V=U and,
separately, each U_a. Adjoin the complete quartic graph baseline
imported in L043. The required ordinary total is strictly greater
than 19800269675. No two additional embedding points are used.

## Conclusion

For U the exact certificate is 36990891 additions. The largest of
the eighteen single-profile certificates is 233020777 additions,
attained at a=(3,2,2,2). With the imported baseline this guarantees
an ordinary packing of at least

\[
 107^5+233020777=14258538084,
\]

below the smallest passing total 19800269676 by 5541731592.
None of the nineteen approved certificates crosses the benchmark.
Park this maximum-neighborhood prescription. This is a lower-bound
shortfall, not an upper bound on packings or a refutation of the
construction route. No useful labeled cap, common-center RS list,
cross-core consistency or safety improvement follows.

## Proof

**Imported method and baseline.** The turn-start SPECIALIZE assessment
`drafts/literature/2026-10-10-four-column-gilbert-certificate.md`
covers precisely this test. Import the standard finite Gilbert greedy
method as used in Wang, Wei, Shangguan and Ge,
*New bounds and constructions for multiply constant-weight codes*,
[arXiv:1512.08220v1](https://arxiv.org/pdf/1512.08220v1),
27 December 2015, Section IV, printed p. 8, the forbidden-ball display
and first inequality in the proof of Theorem 4.4. Its equal-weight
product volume does not count this mixed-profile universe. No
asymptotic estimate or effective matching theorem is imported.
The brief finite-graph applicability argument below supplies the
nonconstant-neighborhood specialization; it does not reprove the
source's asymptotic theorem. L043 imports Xu–Chen v4 Proposition 2.2
with (q,w,r)=(107,9,5), giving 107^5=14025517307 quartic graphs.
Every added block meets each graph in at most four points, since the
graph occupies one point per column. Added blocks are distinct from
graphs. Thus any independent set in one tested universe can be
adjoined to that baseline without a new conflict.

**Exact universe counts.** Write m_v(b) for the multiplicity of part
v in a positive decreasing profile b. For h columns and a profile b
of length l<=h, define

\[
 C_h(b)=\frac{h!}{(h-l)!\prod_v m_v(b)!}
                   \prod_{i=1}^l\binom{107}{b_i}.             \tag{1}
\]

Set C_h(())=1 and C_h(b)=0 if l>h. Binomial coefficients outside
their usual range are zero. To count a block of profile b, inject
its parts into h labeled columns and choose that many points in each.
Only assignments exchanging equal parts are redundant, giving (1).
In particular |U_b|=C_9(b). All eighteen profiles appear in the table
below; a profile with all parts at most two cannot sum to nine in
four parts. No column placement is omitted.

**Exact closed neighborhoods.** Fix A of profile a=(a_1,...,a_s),
with its occupied columns indexed 1,...,s. For B record u_i=|B in
column i| for these s columns. Let c be the decreasing profile of B
on the other 9-s columns. Sum over u_i>=0, |u|<=9, and every c
partitioning 9-|u|, including the empty partition, subject to

\[
 \#\{i:u_i>0\}+\ell(c)\le4,
 \quad \ell(c)\le9-s,
 \quad \operatorname{sort}(u_i:u_i>0,\ c)=b.
\]

For a given occupied column the intersection generating polynomial is

\[
 P_{a_i,u_i}(z)=\sum_{j=0}^{\min(a_i,u_i)}
        \binom{a_i}{j}\binom{107-a_i}{u_i-j}z^j.              \tag{2}
\]

Choose the j common points from A and the remaining points from its
complement in that column. Choices across columns are independent;
the other columns cannot contribute to the intersection. Therefore
the number H_(a,b,j) of B in U_b with |A intersect B|=j is exactly

\[
 H_{a,b,j}=\sum_{u,c}\ C_{9-s}(c)
                  [z^j]\prod_{i=1}^s P_{a_i,u_i}(z).         \tag{3}
\]

Every B has a unique u and outside profile c; the placement factor
in C counts all its outside columns exactly once. Conversely each
counted choice produces such a B. Thus there is no overlap or
omission in (3). The formula also counts j=9: H_(a,a,9)=1,
and H_(a,b,9)=0 when b differs from a, retaining the selected block.

Permuting columns and permuting the 107 points independently in each
column preserves U, every U_b and intersection sizes, and is
transitive on U_a. Thus (3) applies to every A of profile a. This
symmetry is used only to count the full auxiliary universe; no
symmetry of a selected packing or actual subgroup labels is assumed.

Define

\[
 N_{a,b}=\sum_{j=5}^9H_{a,b,j},\quad
 D_a=\sum_{b\in P}N_{a,b},\quad D=\max_{a\in P}D_a.         \tag{4}
\]

The maximum for U is D. For U_a it is exactly N_(a,a), since that
universe is transitive. All cross-profile conflicts are included
before taking the union maximum. Self contributions are included
before either maximum or division.

**Finite specialization and rounding.** In any nonempty finite
conflict graph, repeatedly choose a remaining vertex and remove its
remaining closed neighborhood. The selected vertices are independent:
later vertices survive the removal of every earlier closed
neighborhood. If D_V bounds all original closed neighborhoods, each
selection removes at most D_V vertices. On termination k selections
have covered V, so |V|<=k D_V, and k>=ceil(|V|/D_V). Here D_V>=1
because each neighborhood contains its vertex. This proves the
stated integer rounding, including a possible final partial removal.
The tested single-profile bounds are alternatives, not mutually
compatible families whose guaranteed sizes can be summed.

**Exact values.** Here |U|=117532919075133063255 and
D=3177347687695, attained at profile (9). Their quotient rounded
up is 36990891. The table gives every input for every tested bound;
profiles are written as tuples of column sizes.

| Profile a | C_9(a) | D_a in U | N_(a,a) | ceil(C_9(a)/N_(a,a)) |
|---|---:|---:|---:|---:|
| (9) | 32269016025675 | 3177347687695 | 468095335 | 68937 |
| (8,1) | 2511116156179800 | 2405999362745 | 7899167560 | 317897 |
| (7,2) | 10647132502202352 | 2018824522595 | 6079203943 | 1751403 |
| (7,1,1) | 75233040039146808 | 1725212627795 | 42157694747 | 1784563 |
| (6,3) | 25827202604352240 | 1852249300670 | 3864593985 | 6683032 |
| (6,2,1) | 552702135733137936 | 1389526516670 | 51636784699 | 10703652 |
| (6,1,1,1) | 1115832613649919984 | 1155945952695 | 102607269031 | 10874792 |
| (5,4) | 39500427512538720 | 1796509844170 | 5167241590 | 7644394 |
| (5,3,1) | 1137916161803519280 | 1248562707745 | 37376324425 | 30444839 |
| (5,2,2) | 861565093936950312 | 1079451818545 | 17700098283 | 48675724 |
| (5,2,1,1) | 10436316798255133968 | 886186299945 | 176693030587 | 59064678 |
| (4,4,1) | 718102432206104400 | 1211670595045 | 23546178875 | 30497621 |
| (4,3,2) | 2927648377455656400 | 957335353420 | 39633001525 | 73868955 |
| (4,3,1,1) | 17731606210627654800 | 784315612445 | 151664069225 | 116913692 |
| (4,2,2,1) | 26850717976093305840 | 655519768620 | 147362794185 | 182208258 |
| (3,3,3) | 656844187249666500 | 872111000995 | 8102105095 | 81070806 |
| (3,3,2,1) | 36145197275510219400 | 590541193820 | 184292408900 | 196129605 |
| (3,2,2,2) | 18244718624781348840 | 481991127620 | 78296531610 | 233020777 |

The maximum lower certificate is the last row, exceeding the union
certificate but below the required 5774752369 additions. Baseline
plus this maximum is 14258538084. The exact shortfall to a strict
passing total is 19800269676-14258538084=5541731592. This proves
the conclusion about the prescribed certificates, not about the
maximum possible packing size.

**Complete exact evidence and independent checks.** Run from the
active notebook:

```text
python3 scripts/finite-packing/four_column_gilbert.py
python3 scripts/finite-packing/audit_four_column_gilbert.py
```

The first program implements (1)–(4) with integer arithmetic and
saves all profiles, all 324 intersection histograms (including
0,...,9), every neighborhood contribution, every certificate and
every comparison in `scripts/finite-packing/four-column-gilbert-results.json`.
For each ordered profile pair, its entire intersection histogram
sums to C_9(b), and undirected balance gives
C_9(a)N_(a,b)=C_9(b)N_(b,a). All 690 checks pass.

The independent audit imports no functions from that program.
It regenerates universe sizes by all 9705 labeled occupancy vectors
of sum nine with at most four positive entries. For conflicts it
chooses the complete intersection with A first, with column sizes
j_i and total J>=5, then distributes 9-J points across the column
complements. An intersection choice contributes product C(a_i,j_i),
and a complement occupancy r contributes product C(107-a_i,r_i),
where a_i=0 in unoccupied columns. The resulting B profile is the
sort of j_i+r_i. This independently reconstructs all 1620 histogram
cells at intersection sizes 5,...,9 and all 324 N_(a,b), without
using the generating-polynomial or outside-profile aggregation.
All 1102 audit checks pass, with empty final failures, in
`scripts/finite-packing/four-column-gilbert-audit-results.json`.
The complete neighborhood matrix, conflict histograms, profile
table and benchmark comparison were inspected using selected
`--full` pointers, not inferred from previews.

Five small parameter cases (columns,q,weight,max-columns,conflict)
are (4,2,4,3,3), (4,3,5,3,3), (3,3,4,2,2), (3,2,3,2,1),
and (3,2,3,2,3). Independent direct intersections check every vertex
and every target profile, including all intersection sizes. The
case sizes are 54,468,45,12,12: in total 591 vertices and 224253
ordered pairs. Every histogram agrees. Each small case also runs
a genuine greedy selection and checks all selected pairs. The audit
separately regenerates every small universe by binary masks and
checks every saved histogram against complete direct intersections.
These checks validate the implementation; the combinatorial proof
of (1)–(4) establishes applicability at 107.

The initial audit had five failed small-universe checks because it
compared combination order with increasing mask order. That run is
preserved in `scripts/finite-packing/four-column-gilbert-audit-initial-order-failures.json`.
All histograms and large-instance counts already agreed. Sorting
the vertex list before comparing sets repairs the checker only;
the final rerun has no failures. This is not an additional critical
review of the whole proof.

**Scope and interpretation.** L041/L042 motivate the benchmark only;
they are not mathematical inputs to the count or greedy argument.
The induced packing guaranteed here has 963 points and embeds in
965 without using the other two points. Its size is insufficient
to trigger the downstream cap-route obstruction. The earlier L043
resource nonexclusion and L044 quoted-bound shortfall remain intact.
This is a local REPRODUCTION of the imported finite method with an
explicit mixed-profile specialization, not certified originality or
progress beyond the inspected sources. Actual-label transfer,
cross-core consistency, common-center realization, 67/68 safety and
the ABF definition comparison remain open. No complete candidate
resolution is asserted.

## Mathlib

Full matching coverage and supporting finite graph, finite set and
counting results were **not checked**. Unknown availability is not
absence. The integer certificates are informal verification, not a
formal Mathlib proof.
