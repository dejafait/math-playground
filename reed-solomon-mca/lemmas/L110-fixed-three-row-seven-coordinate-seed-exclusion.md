# L110 — Fixed three-row seven-coordinate seed exclusion

## Hypotheses

Use F=F_(97^20), H the order-sixteen subgroup of F_97^*, dimension
eight, shifted moments and the pinned event on 1/4<=delta<5/16.
The actual D and every locator are nonzero polynomials. Both coefficient
syndromes belong to U_S with S={1,8,12,18,22,27,33}. In the equality
application assume sixteen original finite bad parameters and t=0 in
L104's notation. The original chart and extension-field weights are
arbitrary. Retain L109's and L086's inherited finite-certificate
qualifications. This is a computationally certified restricted exclusion;
the separate step-300 critical proof/program audit below found no defect.

Let J=H minus S. Fix the following three actual two-overlap supports,
written A_j=I_j union K_j:

| j | I_j | K_j |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,70} |
| 3 | {22,27} | {75,79} |

## Conclusion

No such t=0 equality pencil contains all three displayed supports.

More precisely, fix L109's three six-row blocks and append its block for
every I in binom(S,2), K in binom(J,2). The complete classification is:

| Stacked rank over F_97 | All fourth rows | Fourth rows pairwise linear with the seed |
| --- | ---: | ---: |
| 18 | 3 | 0 |
| 20 | 135 | 0 |
| 21 | 618 | 222 |
| Total | 756 | 222 |

There are no other ranks. All 138 lower-rank kernels are preserved in
the certificate, but every one fails pairwise linearity. This excludes
only the specified labeled seed. It supplies no universal seed extraction,
t=0 census, seven-coordinate fifteen bound or improved global interval.
The latter remains 11/q–16/q.

## Proof

### Exact finite support test

Use L109's matrix formula (1), increasing S-coordinate pairs, and the
least coordinate of S minus I as its quotient pivot. The fixed seed
stack has rank eighteen. Enumerate the 21 increasing pairs I and the
36 increasing pairs K, each exactly once. For each of the 756 pairs:

1. Compute the three integers |(I union K) intersect A_j|. Mark the row
   pairwise linear precisely when all three are at most one. The seed
   supports themselves are pairwise disjoint.
2. Construct the 24-by-21 matrix by appending the candidate block to the
   fixed stack. Perform exact row elimination modulo 97, recording the
   selected independent original row indices and the rank.
3. At rank 21, record the determinant residue of that 21-row minor. Each
   recorded residue is nonzero. At lower rank retain the full kernel
   basis, with 21 minus rank vectors, rather than one sampled tensor.

The complete finite sets, all dispositions, pivot columns, minor witnesses
and deficient kernels are in
`scripts/seven-coordinate/fixed-three-row-extensions.json`.
Reproduce from the notebook with
`python3 scripts/seven-coordinate/fixed_three_row_extensions.py`.
This is a finite check of this fixed seed, not generic rank or sampling.

The program also reconstructs every candidate quotient independently:
expand g_K as a polynomial and evaluate by Horner's rule, then use
w_x/g_K(x)-w_z/g_K(z), instead of the producer's product evaluations
and g_K(z)w_x-g_K(x)w_z. All g_K values on S are nonzero. Multiplication
by g_K(z)g_K(x) changes each ratio covector to its producer covector,
so the exterior rows differ by nonzero scalar factors and must have
the same kernel. A separate full Gauss–Jordan elimination computes the
rank, pivot columns and nullspace of this ratio stack for every case.
Every rank agrees with the original incremental elimination.

For each free column c, this RREF nullspace routine sets its c-coordinate
to one, the other free coordinates to zero, and its pivot coordinates
to minus the c-entries of the corresponding RREF rows. Therefore these
vectors are independent and span the complete kernel. All their residuals
are checked against every row of the original unnormalized matrix. At
rank 21, RREF independently gives zero nullity. The recorded original
minor residues give explicit nonzero witnesses in all 618 full-rank cases,
including all 222 pairwise-linear cases. Exact equality of the enumerated
support set with binom(S,2) times binom(J,2) is checked, not inferred from
the case count alone. The full classification in the conclusion is the
result, with no failed checks or pairwise-linear survivors.

These paths share Python, prime-field arithmetic and the support set.
The original matrix and minor routines are reused from L109's audited
producer; the ratio-polynomial construction and RREF routine are separate.
This supplies exact finite-computation evidence with those limitations,
not formal verification or a separate critical audit of this new program.

### Transfer to an equality pencil

Suppose a pencil satisfying the hypotheses contains the fixed seed.
L109's necessary equality conclusion gives r=12+n_0 in 12–14 actual
two-overlap rows and independent lift coefficients u,v. Thus the seed
has at least one further distinct actual two-overlap support A=I union K.
L086 applies to this same field, domain, polynomial nonpersistence and
sixteen-count original bad set. With its inherited audited computational
inputs it makes the entire actual support family pairwise linear.
In particular A is one of the 222 marked rows; no relabeling or symmetry
of H is assumed.

For these four actual rows L109 gives a nonzero decomposable tensor
u wedge v in the kernel of their 24-by-21 matrix. This requires rank
at most twenty. The complete table gives rank twenty-one for every
eligible A, a contradiction. Rank over F agrees with rank over F_97
because these matrices have base-field entries and rank is detected by
minors. Therefore arbitrary extension weights, nonrational original
charts or remaining full-weight gates cannot restore a rejected row.

Decomposability and all other L109 gates remain necessary for every
lower-rank kernel; none is inferred from rank alone. Here pairwise
linearity excludes all such kernels before those gates are needed.
The three seed supports alone are not declared unrealizable as local
moment recoveries. It is their occurrence in an equality pencil, which
would supply further linear rows, that is contradicted. No assertion
about t=1, t=2, other labeled seeds or arbitrary seven-sets follows.

The unchanged ready source assessment is
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is REPRODUCTION of L109's exact support filter with a complete fixed
extension test, not a claim of originality or progress beyond the sources
checked. Standard distance and shortening are imported through L109 and
L086, with their precise Hall Theorem 5.1.1 and Marquez-Corbella–Pellikaan
section 5 citations and checked specializations; no reproof is needed.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-300-fixed-three-row-critical-audit checked the complete
proof, producer and all 756 certificate cases. The complete L109 proof
and canonical audit, L086 proof and canonical audit, and L104's equality
balance and audit were inspected. The unchanged ready seven-coordinate
assessment covers this reproduction. No new mathematical premise or
defect was found. Inherited finite certificates in L086/L109 are reused
with their qualifications, not independently recertified here.

The equality transfer uses actual full errors before invoking pairwise
linearity. L109 gives independent u,v and 12<=r<=14 distinct two-overlap
supports, so at least one is outside the three fixed supports. L086 has
exactly the retained F, H, code, event, actual polynomial nonpersistence
and sixteen original finite parameters. Hence the further support meets
each seed support in at most one coordinate. The nonzero wedge must
annihilate all four blocks. Base-field rank 21 contradicts this over F
because a nonzero base-field minor stays nonzero in an extension. Neither
rational weights, a changed original chart, a universal disjoint triple
nor a full-weight converse is used. Lower-rank kernels are excluded by
their actual incidence failure, not by an untested decomposability claim.

Independent complete replay command:
`python3 scripts/seven-coordinate/verify_fixed_three_row_extensions.py`.
This verifier imports no producer module or routine. It generates H from
powers of 8 and checks equality with the full root set of X^16-1. It
reconstructs the g_K values by a different identity: differentiating

\[
 X^{16}-1=g_K(X)\prod_{y\in S\cup K}(X-y)
\]

at each x in S gives

\[
 g_K(x)=\frac{16x^{15}}
 {\prod_{y\in(S\cup K)\setminus\{x\}}(x-y)}.
\]

All denominators and values are nonzero because H consists of distinct
nonzero labels and 97 does not divide 16. This identity justifies the
independent evaluation implementation; no additional theorem is assumed.
The ratio covectors w_x/g_K(x)-w_z/g_K(z), multiplied in each exterior
row by g_K(z)^2 g_K(x)g_K(y), reproduce the original matrix convention,
including its column order and signs. Column-oriented elimination then
checks every rank and every saved pivot-column profile, separately from
the producer's row reductions. Exact support-set equality and absence
of duplicates are verified, as are all intersection counts and flags.

For every one of the 618 full-rank cases, including all 222 linear ones,
the verifier evaluates the saved 21-row minor by fraction-free integer
elimination with column pivoting and checked exact divisions. Reduction
of that integer determinant modulo 97 equals its saved nonzero residue.
This differs from the producer's modular determinant path. For every one
of the 138 deficient cases, all saved kernel vectors have the required
length, their free-coordinate submatrix is the identity, and their
residuals against the full reconstructed 24-row matrix vanish. Together
with the independently established rank, this proves that the saved basis
is complete. All 144 vectors and all 3,456 residual entries are checked;
none of these deficient cases is pairwise linear.

The full rank histogram is again {18:3,20:135,21:618}, with exactly
222 linear cases, all at rank 21, and no linear survivor. All saved
summary fields and metadata agree. The original producer completes
successfully and reproduces its entire certificate byte for byte.
The complete audit records, exact integer minor determinants, all kernel
bases and residuals, checks and replay hashes are saved in
`scripts/seven-coordinate/fixed-three-row-critical-audit.json`.
There are no failed checks. Both paths still share Python and exact
residue arithmetic; this is not proof-assistant verification.

This validates only the stated fixed labeled t=0 exclusion, with no
new bound beyond the reproduced input. The original three local
recoveries are not excluded by themselves. Other third-row seeds,
seven-sets, equality profiles, universal representation and challenge
qualifications remain open. This canonical audit supersedes pending-audit
wording in the unchanged overview; the argument and DAG inputs are
unchanged, so PROOF.md and DAG.md are not edited for audit status alone.

## Mathlib

Full matching fixed-seed classification and exclusion: **not checked**.
Supporting matrix-rank, kernel, finite-field and GRS coverage: **not
checked anew**. The input results retain their own qualifications.
Unknown library coverage is not evidence of absence. The new classification
retains its finite-computation dependence after the separate audit above.
