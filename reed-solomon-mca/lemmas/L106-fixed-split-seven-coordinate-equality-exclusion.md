# L106 — Fixed two-triple split excludes seven-coordinate equality

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*,
C=RS[F,H,8], L010's shifted moments and pinned same-support event
at 1/4<=delta<5/16. The actual Hankel determinant D and every actual
coordinate locator are nonzero polynomials. Both coefficient syndromes
belong to U_S, where

\[
 P=\{1,8,12\},\quad Q=\{18,22,27\},\quad c=33,
 \qquad S=P\sqcup Q\sqcup\{c\}.
\]

Let f be the unique affine lift supported on S. Suppose two distinct
original finite bad parameters have actual errors equal to f at those
parameters, and their zero sets within S are P and Q, respectively.
The original chart, coefficients and weights may be arbitrary over F.

The proof uses L105's reduction, including its L104 and audited L103
inputs and their finite-certificate qualifications. The separate step-292
critical audit found no defect in L104/L105 or this proof and completely
replayed the prime-field table specified below. The computational
qualifications remain and are not
silently replaced by a documentation checker or by selected examples.

## Conclusion

Under these hypotheses, the entire original bad set has size at most
fifteen. More precisely, L105's full support-seed reconstruction for
this fixed split has maximum three distinct eligible two-overlap
scalars before deleting the original omitted projective point. Equality
would require at least six, so this split cannot occur at equality.

This is a restricted class exclusion, not a uniform seven-coordinate
bound. Other splits and the t=0,1 cases for a specified seven-set remain
open. No sixteen-event survivor, complete challenge candidate, improved
global interval or general-field theorem is asserted.

## Proof

### Reduction and scope of the finite test

L010 gives |B|<=16, including lower-weight and singular events. Suppose
|B|=16. L105 applies to the two equal-lift parameters and the specified
zero triples. In particular all seven coordinates are active, there
are exactly two equal-lift events, and at least six full two-overlap
events have supports {x,y} union K, x in P, y in Q, K a two-subset
of J=H minus S. There are two such events with distinct P labels,
distinct Q labels and distinct outside pairs K. L105 proves that these
support seeds alone uniquely reconstruct the normalized rational lift

\[
 w(\mu)|_P=\mu p,\qquad w(\mu)|_Q=q,\qquad
 w(\mu)_c=\mu U-V,
 \quad p_1=q_{18}=1,\quad U,V\in\mathbb F_{97}^*.
\]

Its two tree-ratio systems, distinct seed scalars, endpoint gates U,V!=0
and all full seed-weight gates are necessary. There are eighteen
unordered pairs of overlap edges sharing neither endpoint. Lexicographically
order each pair, and independently assign K_1,K_2 among the thirty-six
outside pairs, retaining K_1!=K_2. This gives exactly 18*36*35=22,680
seeds. No additional incidence, support-disjointness or coordinate-degree
filter is imposed: allowing these extra cases only enlarges the upper
test. Duplicate reconstructed lifts are identified by their unique
normalized eight-entry key (p_1,p_8,p_12,q_18,q_22,q_27,U,V).

For each retained lift test all 3*3*36=324 cross-triple supports by
L105 (4)–(6). Count distinct mu, retaining all full-weight gates.
These rational scalars are nonzero and finite. L105 proves the original
chart deletes at most its one omitted point, which may be nonrational;
it cannot increase this count. There are no extension-field-only row
parameters omitted by this table, because each row's nonzero P/Q values
fix mu uniquely in F_97. No zero/one-overlap or other error shape is
claimed to have been enumerated; equality needs the six rows just named.

### Complete certificate and independent replay

Run from the active notebook:

```sh
python3 scripts/seven-coordinate/fixed_split_table.py
python3 scripts/seven-coordinate/verify_fixed_split_table.py
```

The producer writes every seed disposition, the complete candidate keys,
every candidate's 324 first-failed-gate/success codes and every successful
row/scalar to `scripts/seven-coordinate/fixed-split-table.json`.
The full certificate SHA-256 is
`5277acfc642f451283720220f16f2cfb916edc392fa6e5153fa8a0b1aeb43cfd`.
The verifier has no producer imports and writes
`scripts/seven-coordinate/fixed-split-table-verification.json`.
The completed counts are:

| Test | Complete result |
| --- | ---: |
| Seed cases, actual / required | 22,680 / 22,680 |
| Equal seed scalars rejected | 244 |
| U=0 rejected | 276 |
| V=0 rejected after U gate | 276 |
| Seed overlap-weight failures | 672 |
| Retained seeds | 21,212 |
| Distinct retained lifts | 21,182 |
| Support tests, actual / required | 6,862,968 / 6,862,968 |
| First failed P ratio | 6,667,992 |
| First failed Q ratio | 149,231 |
| Failed c equation after ratios | 3,363 |
| Zero overlap weights after all row equations | 0 |
| Successful full support rows | 42,382 |
| Lifts with exactly two distinct scalars | 21,164 |
| Lifts with exactly three distinct scalars | 18 |
| Lifts with at least six distinct scalars | 0 |
| Replay failures, actual / required | 0 / 0 |

The verifier reconstructs the full seed index set independently, solves
the normalized tree equations by 3-by-3 inverses rather than propagation,
checks every seed rejection and candidate reference, verifies all candidate
keys are distinct and every candidate has a retained seed, and checks
every first-failed row gate using cross products. All thirty-six degree-seven
generator evaluations have zero shifted moments 1 through 8 (288 checks).

In addition, row completeness is checked by a different linear-algebra
path. For A={x,y} union K, form the eight-by-four matrix with entries
z^j, j=1,...,8 and z in A. Invert its first four rows, which are a
Vandermonde matrix times nonzero diagonal entries. For each of the seven
coordinate vectors on S this determines its possible A-supported
weights from the first four moments. The remaining four moment
residuals give a four-by-seven matrix R_A. Writing the two normalized
coefficient vectors as w_0=(0,q,-V), w_infty=(p,0,U), the necessary
and sufficient equations for any finite projective direction are

\[
 R_A w_0+\mu R_A w_\infty=0.
\]

The verifier checks R_A w_infty!=0 for every candidate and row; hence
there is at most one solution over any extension, obtained from a
nonzero rational pivot. It tests the other three residuals and all four
recovered weights. Every success agrees with the producer's row/scalar,
and its recovered error is replayed against all eight moments, for all
42,382 successes. Every rejected row is also checked by this residual
criterion, not merely by a list of successful examples. The scalar sets
and all eighteen maximizers are reconstructed completely. The two
implementations share Python and arithmetic modulo 97; this is an
explicit remaining implementation qualification, not an independent
formal verification or a separate critical audit.

For a concrete maximizer, candidate 3542 has normalized key
(1,25,53,1,38,22,94,56) and scalar set {44,73,77}. Its complete
324-row record is in the certificate. This selected example is not
the upper-bound evidence; the complete replay is essential.

### Applying the threshold and known traps

The table therefore bounds the enlarged predeletion scalar set by three,
whereas L105 requires at least six distinct actual original finite
two-overlap parameters at equality. Injectivity of the projective chart
preserves distinctness, and deleting its omitted point cannot restore
the deficit. This contradicts |B|=16. The integer bound from L010
then gives |B|<=15 for the hypotheses stated here.

Equality is invoked before fullness, coordinate balance or the forced
six-row threshold. No original chart is rationalized, no extension-field
weights are sampled, no vanishing endpoint or overlap weight is divided
out, and repeated witnesses are not counted as different parameters.
The table is complete only for this split's L105 candidates; it is
neither a census of seven-sets nor a test of all original bad events.
There are no six-row survivors requiring a total coordinate-degree
check. No coordinate-degree gate was used to reduce the maximum three.

The unchanged prior EXPLORE assessment is
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is a REPRODUCTION of the ready reconstruction and finite-field
verification mechanism, without claiming originality beyond the checked
sources. L105 imports Hall, *Notes on Coding Theory*,
[GRS chapter, Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and Marquez-Corbella–Pellikaan,
*A characterization of MDS codes that have an error correcting pair*,
FFAA 40 (2016), 224–245,
[accepted manuscript February 29, 2016, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following shortening formula,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004).
Their unchanged field,
distinct-label, nonzero-multiplier and positive-dimension hypotheses
are verified in L104/L105; no reproof or changed source theorem is needed.
The new local evidence is the complete maximum for this fixed split,
not rational descent, a new general theorem or challenge resolution.

### Separate critical proof/program audit, 2026-10-17

Step 2026-10-17-mca-292-seven-coordinate-fixed-split-critical-audit
read L104/L105 in full, checked their L010/L103 inputs, and read both
complete programs before rerunning the two reproduction commands above.
It found no proof or program discrepancy. The two canonical upstream
audit sections record the six-row threshold, exact seed coverage,
extension-field completeness and arbitrary original-chart passage.
Their mathematical statements and the argument here are unchanged.

The producer's tree propagation and the verifier's normalized 3-by-3
inverses implement the same nonzero ratio equations by different paths.
Both enumerate all eighteen eligible overlap-edge pairs and every
ordered pair of distinct outside pairs, with no incidence filter.
Every failed seed gate is replayed before candidate references are
accepted. Normalized keys identify the same projective lift because
its P and Q endpoint directions and their normalizations are fixed;
all retained keys are reached and pairwise distinct.

For all 324 supports per candidate, the verifier independently solves
the first four moment equations and imposes the remaining four. Its
matrix is invertible: the support labels are four distinct nonzero
elements, so it is Vandermonde times a nonzero diagonal. The transpose
used to assemble the four-by-seven weight map and the residual powers
5 through 8 have been checked against the definitions. The asserted
nonzero infinity residual is checked in every row, making the finite
scalar pivot complete over any extension. All four weights are checked,
including both overlap weights, and all eight original moments are
recomputed at every success. Every rejected row also receives this
residual test. Thus success-only checks and prime-field sampling are
not the upper-bound evidence.

The regenerated producer certificate has unchanged SHA-256
`5277acfc642f451283720220f16f2cfb916edc392fa6e5153fa8a0b1aeb43cfd`;
the regenerated verifier report is also unchanged, SHA-256
`782897efc496c78e7381edc9ccfb9a4312b54b7b63f7ef5e21f7a641e89a823e`.
Audit hashes, complete actual/required counts and qualifications are in
`scripts/seven-coordinate/fixed-split-critical-audit.json`.
All 22,680 seeds, 21,182 lifts and 6,862,968 rows were replayed, with
288 generator moment checks, 42,382 full eight-moment successes and
zero discrepancies. The complete histogram remains 21,164 lifts with
two scalars and eighteen with three; there are no six-scalar survivors.

The maximum three is below the required six before any coordinate-degree
filter or original-point deletion. Equality therefore fails for precisely
the fixed split in the hypotheses, and L010 gives the integer bound
fifteen for its entire original bad set. Other splits and t=0,1 remain
unresolved; no global bound improves. This is a separate informal
critical audit with complete replay, not formal verification. Both
programs still share Python and arithmetic modulo 97, and the audited
L103 inputs retain their original computational qualifications.

## Mathlib

Full matching fixed-split reconstruction table and equality exclusion:
**not checked**. Supporting finite-field arithmetic, matrix inverses,
GRS shortening and projective-coordinate coverage: **not checked**.
Unknown coverage is not absence. This is an informal result with explicit
finite-computation dependence; its separate step-292 critical audit
found no defect, subject to the qualifications recorded above.
