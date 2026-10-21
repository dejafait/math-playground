# L111 — Third-support variation with two fixed seven-coordinate rows

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*, dimension
eight, L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. Assume actual D and every locator are nonzero
polynomials and both coefficient syndromes lie in U_S, where
S={1,8,12,18,22,27,33}. For the equality application assume sixteen
original finite bad parameters and t=0 in L104's notation. Extension-field
weights and the original finite chart are arbitrary. Retain L109's and
L086's inherited finite-certificate qualifications.

Fix two actual two-overlap supports
A1={1,8,47,50} and A2={12,18,64,70}. Write J=H minus S and
A3=I3 union K3, with I3 in binom(S,2), K3 in binom(J,2), and require
A3 disjoint from A1 and A2. This is a computationally certified partial
classification; the separate step-302 critical audit below found no defect.

## Conclusion

There are exactly thirty such labeled choices for A3. Twenty-six cannot
occur with A1,A2 in a t=0 equality pencil. The four exceptions to this
rank-only exclusion, with the ranks of all pairwise-linear fourth rows,
are exactly:

| I3 | K3 | Rank 19 | Rank 20 | Rank 21 |
| --- | --- | ---: | ---: | ---: |
| {22,33} | {79,89} | 9 | 92 | 121 |
| {22,33} | {85,89} | 0 | 55 | 167 |
| {27,33} | {79,96} | 0 | 55 | 167 |
| {27,33} | {85,96} | 0 | 55 | 167 |

For each of the other twenty-six third rows, all 222 pairwise-linear
fourth rows have rank 21. Each third row has 756 fourth choices in total.
The 266 linear deficient occurrences above have complete saved kernels;
they are not asserted to be distinct four-support families or actual
pencils. Rank alone does not exclude these four seeds. The result does
not assert that any equality pencil contains the two fixed supports or
a third support disjoint from them. The seven-coordinate fifteen bound,
universal representation and global interval 11/q–16/q remain unresolved.

## Proof

### Reused mathematical inputs

Use the complete support-only matrix and necessary direction of audited
L109. For a support A=I union K, set
g_K(X)=product_(y in J minus K)(X-y), let z be the least label in
S minus I, and use the four covectors
c_x(w)=g_K(z)w_x-g_K(x)w_z for x in (S minus I) minus {z}.
Take their six exterior rows, with columns the 21 increasing pairs of
the increasing S. Denote this six-by-21 block by N_A.
It depends only on the labels. L109 establishes that at equality the
lift coefficients are independent and their nonzero wedge is in the
kernel of the stack for any selected actual rows. Thus a rank-21
substack is impossible, also over F: its nonzero base-field minor
remains nonzero in every field extension.

L109 imports the distance and shortening inputs through L104:
J. I. Hall, *Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript, section 5, Definitions 5.1–5.2, Lemma 5.3 and the following shortening formula, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The field, distinct labels, nonzero multipliers, dimension eight and
the seven shortened coordinates J minus K are unchanged; the shortened
dimension is one with nonzero retained multipliers. No new distance or
shortening result is needed or reproved. The unchanged ready assessment
is `drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is REPRODUCTION of the assessed finite filter, without an originality
claim or progress beyond the sources checked.

### Complete finite calculation

Disjointness from A1 union A2 requires
I3 in binom({22,27,33},2) and K3 in binom({75,79,85,89,96},2).
Their product has 3*10=30 elements. One is the audited L110 seed
I3={22,27}, K3={75,79}; its complete classification is imported, not
recalculated. The new program checks the prior certificate's identity,
its audit hash and agreement of their complete summary fields.

For each of the other 29 third rows, enumerate all 21*36=756 fourth
supports A4=I4 union K4, checking exact case-set equality and no
duplicates. The fourth row is marked pairwise linear when all three
intersection sizes with A1,A2,A3 are at most one. Build the 24-by-21
stack of their four blocks. The program performs these checks:

1. Construct every one of the 756 distinct blocks by direct products
   and independently by the differentiated identity
   X^16-1=g_K(X) product_(y in S union K)(X-y). At x in S this gives
   g_K(x)=16x^15/product_(y in (S union K) minus {x})(x-y).
   The denominator and numerator are nonzero: the labels are distinct
   and nonzero and 97 does not divide 16. Ratio covectors
   w_x/g_K(x)-w_z/g_K(z), rescaled in each exterior row by
   g_K(z)^2 g_K(x)g_K(y), give precisely the direct-product block.
   All entries of every block agree, with the same column signs/order.
2. Compute every stack rank by incremental row elimination and
   independently by column-oriented elimination. All ranks agree.
   At rank 21 retain 21 independent original row indices, calculate
   their minor modulo 97, and independently calculate its exact integer
   determinant by fraction-free elimination with column pivoting and
   checked exact divisions. Every residue agrees and is nonzero.
3. At rank less than 21 use a third, polynomial/Horner ratio-block path
   and Gauss–Jordan elimination to retain the complete kernel basis.
   Its pivot columns agree with the independent column computation.
   It has 21 minus rank vectors, with identity free-coordinate submatrix.
   All 24 residuals of every vector vanish against the independently
   rebuilt original stack. Rank, nullity and this independent basis
   together prove completeness, over F_97 and after scalar extension.

The exact routines are reused from the previously audited L109/L110
implementations. This is independent construction and arithmetic evidence
inside the new calculation, not a separate critical audit of L111.
The paths share Python and exact residue arithmetic; formal verification
is not claimed. Exact integer determinants and every deficient basis
and residual are preserved with all dispositions in
`scripts/seven-coordinate/third-row-variation.json`.
Reproduce with `python3 scripts/seven-coordinate/third_row_variation.py`.

The 21,924 new cases have rank histogram
{18:87,19:54,20:4683,21:17100}. All 17,100 full-rank minor witnesses
pass both determinant paths. All 4,824 deficient kernels, containing
5,052 basis vectors in total, pass completeness and residual checks.
Of the 6,438 new pairwise-linear cases, exactly 9 have rank 19,
257 have rank 20, and 6,172 have rank 21. All 266 linear deficient
occurrences lie in the four table rows. The other 25 new seeds have
222 linear cases each, all at rank 21; L110 adds the twenty-sixth
excluded seed. There are no failed checks.

For a completely specified residual example, choose
A3={22,33,79,89} and A4={1,12,75,79}. The three intersection sizes
of A4 with the seed are (1,1,1). The stack has rank 20 and its kernel
is generated, in increasing S-pair order, by

\[
 (11,35,21,53,27,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0).
\]

All 24 residuals vanish; the sole free column is column 5 (zero-based),
where the displayed vector is one. The independent rank computation
and this normalized vector specify the complete kernel. No projected
rank, full-weight, finite-chart or additional-event feasibility is
concluded from this example.

### Equality transfer and limitations

If a retained equality pencil contains A1,A2,A3, L109 supplies
r=12+n_0 in 12–14 distinct actual two-overlap rows. There is therefore
an actual fourth support distinct from the three fixed rows. Audited
L086 applies to this same field, domain, event, polynomial nonpersistence
and sixteen original finite parameters, with its inherited audited
computational inputs. It makes this support pairwise linear with all
three fixed supports. For each of the 26 excluded seeds, the exhaustive
calculation (or L110 for its audited seed) gives rank 21 for every such
support. This contradicts L109's nonzero kernel tensor. This proves
exactly the claimed restricted exclusions.

For the other four seeds the complete deficient kernels remain subject
to L109's nonzero decomposable tensor, rank-one projected restrictions,
nonzero lambda and both overlap weights, and prescribed original
finite-direction gate. Further equality events and coordinate balance
are also required. No gate is inferred from a rank drop, and no descent
of arbitrary extension weights or the original chart is assumed.
The rank-only uniform extrapolation is stopped on this explicit evidence.
This does not contradict L110, exclude or realize the four residual
seeds, improve the global bound, or resolve challenge qualifications.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-302-third-row-critical-audit checked this complete
proof, producer and its three imported computation modules. It inspected
L109's necessary filter, all feasibility gates and canonical audit,
L110's transfer and canonical audit, L104's equality balance, and L086's
exact hypotheses and canonical audit. The unchanged ready seven-coordinate
assessment covers this REPRODUCTION audit. The inspected standard-source
citations above and inherited computational inputs are reused with their
qualifications; their underlying certificates are not all rerun here.
No mathematical error or changed dependency was found.

At equality, the actual errors are full and distinct before incidence is
used. L109 gives independent lift coefficients and 12<=r<=14 actual
two-overlap supports, so the three fixed supports have a distinct fourth.
L086 applies to precisely the same F, H, k, event, actual nonpersistent
D and locators, and sixteen original finite bad parameters. This fourth
support therefore lies in the enumerated pairwise-linear class. The
nonzero wedge of the lift coefficients must lie in the four-block kernel;
a rank-21 minor contradicts it over every extension of F_97. This uses
neither rational weights nor a replacement of the original chart. The
claim is conditional on the fixed A1,A2 and selected disjoint A3; no
universal extraction or assertion that the three local rows alone are
infeasible is made. At a rank drop the full list of gates remains open.

Run the standalone verifier with
`python3 scripts/seven-coordinate/verify_third_row_variation.py`.
It imports no producer module. It reconstructs the complete subgroup from
powers of 8 and checks the full root set of X^16-1, label partitions and
column signs/order. Each g_K is rebuilt by polynomial coefficient
multiplication and Horner evaluation, then its covectors and exterior
block are formed directly. Ordinary forward Gaussian elimination with
row pivoting checks every rank and pivot-column profile, independently
of the producer's incremental row and column-oriented implementations.
All 756 blocks have rank six. Exact set equality and absence of duplicates
check all thirty third rows and all 756 fourth rows for each new seed;
all intersection counts, linearity flags and survivor indices agree.

Every one of the 17,100 saved full-rank minors is evaluated as an exact
integer determinant by fraction-free elimination with row pivoting and
checked exact divisions, rather than the producer's column pivoting.
The complete integer values, not only their residues, agree with the
source certificate, and every residue modulo 97 is nonzero. Every one
of the 4,824 deficient cases has the independently computed rank,
21-rank saved vectors and an identity free-coordinate submatrix. All
5,052 vectors have 21 canonical residue entries; all 121,248 residual
entries against the full reconstructed 24-row matrices vanish and match
the saved residuals. Rank-nullity and independence thus certify complete
bases, including all 266 pairwise-linear deficient occurrences. This
statement is stable under scalar extension; no rational descent of a
feasible plane is inferred.

The reused L110 source and audit match both hashes recorded in L111's
certificate. Its audit's before/after source hashes agree with the current
source, its producer exited successfully, and its complete summary and
all successful check records agree. All 756 reused case records are
compared for support labels, ranks, pivot columns, incidence flags,
complete kernel bases, residuals and nonzero minor witnesses. Thus this
reuse is tied to the already audited artifact, not merely its summary.
The L110 audit and source remain unchanged throughout this replay.

Every aggregate and per-seed summary and the complete residual index
lists agree. In particular the four table rows have exactly the stated
rank histograms, the other 26 seeds have 222 linear full-rank extensions
each, and the explicit rank-20 example has exactly the displayed sole
normalized basis vector, free column 5 and 24 zero residuals. The producer
completed and reproduced its entire certificate byte for byte, with
SHA-256 `34d6bb68537b8e5b153552801426c2f37266c96fa1446bb8ec89ae03885f85c2`.
All checks passed; the full per-case records, determinants, bases,
residuals, hashes and replay output are preserved in
`scripts/seven-coordinate/third-row-critical-audit.json`.

Both implementations share Python and exact integer/residue arithmetic,
and this is not proof-assistant verification. The audit validates the
restricted classification and ATTEMPTS/041's rank-only route obstruction,
not a new theorem beyond the assessed inputs or an improved global bound.
The four residual seeds still require decomposability, rank-one
projections, nonzero lambda and overlap weights, the prescribed finite
chart and enough additional equality events. Arbitrary profiles,
seven-sets, universal representation and challenge qualifications remain
open. This canonical audit supersedes pending-audit wording in the
unchanged overview; the mathematical argument and DAG inputs are
unchanged, so PROOF.md and DAG.md are not edited for audit status alone.

## Mathlib

Full matching third-seed classification and restricted exclusion:
**not checked**. Supporting finite-field, matrix, exterior-square and
GRS coverage is **not checked anew**; the imported canonical inputs
retain their own qualifications. Unknown coverage is not absence.
This result explicitly depends on the complete exact finite certificate
after the separate critical proof/program audit above.
