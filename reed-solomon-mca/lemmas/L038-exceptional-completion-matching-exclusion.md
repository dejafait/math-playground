# L038 — The exceptional union-six completion is impossible

## Hypotheses

Retain L033's complete hypotheses: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, C the degree-less-than-eight evaluation code on H,
the pinned cell 1/4<=delta<5/16, all eight shifted moments, nonzero
polynomial Hankel determinant D and every nonzero coordinate-locator
polynomial. There is an explicit union-six affine lift with three
distinct original finite parameters and actual full-weight four-errors.
Assume N_3=0 and N_ext=13, so L010/L033 give sixteen-count equality.

Use L035's notation: U is the selected six-set, J=H minus U, the
twelve additional overlapping supports are {z} union K_(z,i),
z in U and i=1,2, and K_0 is the unique additional four-support
disjoint from U. Each K_(z,i) is an actual outside triple in J,
not an abstract incidence supplied in place of a moment-compatible
error. All sixteen parameters are distinct and finite in the original
chart; every support carries its four nonzero actual error weights.

## Conclusion

For every z in U,
\[
 K_{(z,1)}\cap K_{(z,2)}=\varnothing.                 \tag{1}
\]
In particular L035's exceptional intersecting-tag alternative is
impossible, for every H-labeling and arbitrary extension-field weights.
No quartic-compatibility or shared-coordinate relaxation is needed.

Equivalently, under L033's hypotheses and N_3=0, if two additional
overlapping errors have the same U coordinate and intersect outside U,
then N_ext<=12. The all-disjoint alternative in (1) remains open;
this is not the twelve-incidence bound for every union-six pencil,
a universal extraction theorem, or the global fifteen bound.
The conditional exclusion awaits a separate critical audit.

## Proof

### An exceptional completion would give disjoint edge partitions

Suppose (1) fails. L035 gives a unique exceptional tag x and supports
\[
 B_1=\{x,p,a,b\},\quad B_2=\{x,p,c,d\},\quad
 K_0=\{a,b,c,d\}.
\]
Apply L037 to these actual errors and the original cluster, with its
notation U'={x,p,a,b,c,d}, V=U minus {x}, V'=U' minus {x}, and
E=H minus (U union U'). Each of V,V',E has five labels, and the
three sets are pairwise disjoint. This uses L037's completion statement,
whose proof constructs the second actual lift with the same moments and
original finite chart. No independently chosen second pencil is used.

The ten remaining supports are exactly
\[
 S_e=\{z_e,z'_e\}\cup e\quad
 (e\text{ an unordered two-subset of }E),             \tag{2}
\]
where z_e belongs to V and z'_e belongs to V'. Each z in V occurs on
exactly two disjoint edges of E; these five two-edge matchings partition
all ten edges. Call this partition P. The tags in V' similarly define
a partition P' into five two-edge matchings.

We now prove the restriction that was not asserted in L037: P and P'
cannot have a common matching. If a matching {e,f} belonged to both,
the two supports S_e,S_f would have the same tags z in V and z' in V'.
Their outside triples relative to U would be
\[
 \{z'\}\cup e,\qquad \{z'\}\cup f.
\]
They intersect at z' (the edges e,f are disjoint). These are the two
additional errors tagged by z. L035 proves that every same-tag pair
other than the exceptional pair tagged by x is disjoint outside U.
But z is in V=U minus {x}, a contradiction. Thus
\[
                        P\cap P'=\varnothing.       \tag{3}
\]
This deduction retains the outside tag z'; looking only at the two
disjoint E edges would miss the intersection. It establishes, rather
than assumes, the prohibition of repeated ordered tag pairs.

### Complete five-label obstruction

Here is a direct exhaustive proof that (3) is impossible. Label the
five vertices of E by 0,1,2,3,4 solely for this finite-set argument.
Write ij for the unordered edge {i,j}, and ij|kl for a matching of
two disjoint edges. No field value, cyclic symmetry of H, weight, or
parameter is assigned by these auxiliary names.

In any partition of the ten edges into five two-edge matchings, the
four edges through 0 lie in four different matchings. The remaining
matching avoids 0, so is one of 12|34, 13|24, 14|23. Fix first
12|34. The partner of 01 must be 23 or 24: the only other disjoint
edge is 34, which is already used. Swapping 3 and 4 interchanges
these two cases while preserving 12|34, so analyze partner 23.
The partner of 04 must then be 13: its alternatives 12 and 23 have
already been used. The remaining edges are 02,03,14,24. The edge
02 can only be paired with 14, forcing the last matching 03|24.
This gives one partition and, after swapping 3 and 4, exactly one
other. Relabeling 1,2,3,4 carries either other matching avoiding 0
to 12|34, so each has exactly two completions as well.

The resulting six partitions are displayed in full. Columns after
the first matching are ordered by their edge through 0.

| Partition | Matching avoiding 0 | Contains 01 | Contains 02 | Contains 03 | Contains 04 |
| --- | --- | --- | --- | --- | --- |
| P1 | 12\|34 | 01\|23 | 02\|14 | 03\|24 | 04\|13 |
| P2 | 12\|34 | 01\|24 | 02\|13 | 03\|14 | 04\|23 |
| P3 | 13\|24 | 01\|23 | 02\|34 | 03\|14 | 04\|12 |
| P4 | 13\|24 | 01\|34 | 02\|14 | 03\|12 | 04\|23 |
| P5 | 14\|23 | 01\|24 | 02\|34 | 03\|12 | 04\|13 |
| P6 | 14\|23 | 01\|34 | 02\|13 | 03\|24 | 04\|12 |

Each row visibly covers every edge once, consists of disjoint-edge
pairs, and is distinct. The preceding exhaustive branching permits
only six rows, so this table omits no partition. Every two rows share
a matching. For completeness the witnesses for all fifteen distinct
row pairs, grouped by the smaller row index, are
\[
\begin{array}{c|ccccc}
 &P2&P3&P4&P5&P6\\\hline
P1&12|34&01|23&02|14&04|13&03|24\\
P2& &03|14&04|23&01|24&02|13\\
P3& & &13|24&02|34&04|12\\
P4& & & &03|12&01|34\\
P5& & & & &14|23
\end{array}
\]
Identical rows share all five matchings. Hence any two partitions have
a common matching, contrary to (3). This proves (1).

The reformulation without assuming N_ext=13 follows from L010/L033:
when N_3=0, |B|=3+N_ext<=16, hence N_ext<=13. If N_ext>12,
it equals thirteen, so all preceding equality hypotheses hold and
an intersecting same-tag pair is impossible. Thus the existence of
such a pair forces N_ext<=12. No absence of lower weights was inferred
from abstract supports; it remains an explicit hypothesis here.

### Verification, source scope, and limitations

The complete arithmetic-free proof is the finite branching and table
above. An independent exact check is recorded in
`scripts/exceptional-five-label/matching-obstruction-result.json`;
reproduce with
`python3 scripts/exceptional-five-label/matching_obstruction.py`.
The script forms all fifteen two-edge matchings, checks every five-set
of them for exact coverage of the ten edges, and compares the result
with a separate recursion pairing the least uncovered edge. Both give
exactly the six displayed partitions. All fifteen distinct partition
pairs have one common matching; a completion requires zero. There are
no failed checks. The full partition table and intersection matrix were
inspected using the shared JSON inspector at `/partitions` and
`/intersection_matrix` with `--full`. The proof does not depend on a
sample or on trusting an asserted computational maximum.

The input is the actual-support packing of L035 and the completion
shape of L037, both used only after L010/L033 equality. Their proofs
were inspected for these uses; this is not their separate critical
audit. The standard coding and shortening inputs already assessed in
L033 retain exactly their existing hypotheses. No new external theorem,
changed shortening specialization, or uninspected graph classification
is imported. The tiny finite graph fact is proved here to make the
conditional obstruction checkable; no originality is claimed for it.
The unchanged EXPLORE assessment for the twelve-incidence target
authorizes this intermediate exclusion. POTENTIALLY_NEW records the
unmatched application in the sources checked, not certified novelty.

L036's involution and L037's quartic/shared-coordinate equations remain
valid conditional restrictions, but are unnecessary to the contradiction.
In particular this excludes every exceptional labeling, including any
that passed those tests. L037's previous decision not to assert distinct
tag pairs is strengthened here using L035; it was not a proved assertion
that repeats occur. Historical labeled tests are preserved. Nothing in
this proof classifies or excludes the remaining all-disjoint packings,
uses L015, changes the original excluded projective point, or counts
projective incidences as actual finite errors. The global interval
11/q–16/q, universal extraction, ABF26 identification, stronger-source
overlap and separate critical audits remain unresolved.

## Mathlib

Coverage of the full conditional exclusion and the finite partition
fact is **not checked**. Supporting finite-set, matching and coding
results have not been looked up here. This is neither an absence claim
nor a formal verification claim; the complete elementary proof is above.
