# L158 — Exact loci for three eligible four-row tests

## Hypotheses

Let E be any field extension of F_97, in particular its algebraic closure.
Use L109's original maps on W=E^S, with

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

For a row (I,K), set O=S minus I, z=min O,
g(X)=product_(y in J minus K)(X-y), and

    (Qw)_x=g(z)w_x-g(x)w_z, x in O minus {z},

in increasing x-order. Let N=exterior-square(Q), with increasing
coordinate pairs in S and increasing pairs of target coordinates.
Consider exactly the following three ordered quadruples (a,b,c,d):

| Case | a: (I,K) | b: (I,K) | c: (I,K) | d: (I,K) |
| --- | --- | --- | --- | --- |
| 1 | (1,8;47,50) | (12,18;64,79) | (1,12;70,75) | (8,18;85,89) |
| 2 | (1,8;64,96) | (12,18;79,89) | (1,12;47,85) | (8,18;50,70) |
| 3 | (1,8;47,50) | (12,18;64,79) | (1,22;70,75) | (8,27;85,89) |

Each displayed pair before/after the semicolon is I/K, respectively.
All labels are original. In the 756-label lexicographic order, a<b
and c<d. Both designated support pairs are disjoint, and all six
support intersections have size at most one. No coding realization,
genericity, weight condition or prescribed chart is assumed.

## Conclusion

The set of two-dimensional E-subspaces L of W satisfying
rank(Q_j restricted to L)=1 for all four rows has cardinality exactly
2, 2 and 0 in cases 1, 2 and 3, respectively. In both nonempty cases
the complete set is

    span(e_1,e_18), span(e_8,e_12).

These are exact extension-field loci, not base-field samples. None
of the three predeclared attempts yields an infinite family. This
does not establish universal four-row finiteness or twelve-row
exclusion. The calculation is a local reproduction of the original
kernel/Plucker method; no source-level novelty is claimed. It has
same-step exact verification, not a separate critical audit.

## Proof

### Reused tools and exact input

Use L109's identification N_j=exterior-square(Q_j), its decomposability
equations, and its original quotient formula. These linear identities
apply to the stated maps over any E; no equality-pencil assumption is
needed for them. A nonzero elementary wedge u wedge v belongs to all
four exterior kernels exactly when every restricted quotient has rank
at most one. Rank zero must still be excluded below.

For standard finite-dimensional linear algebra import A. I. Kostrikin
and Yu. I. Manin, *Linear Algebra and Geometry*, Gordon and Breach,
1997 paperback, ISBN 90-5699-049-7, Chapter 1 Theorem 3.12, pp. 20–21,
and sections 6.2–6.9, pp. 44–46, from the
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
The ready assessment `drafts/literature/2026-10-25-four-row-finiteness-review.md`
records the inspected arbitrary-field tools and the limitations of
generic/complex transversal results. Only kernel dimension and linear
independence are used here, over E; no finiteness theorem is imported
or reproved. The finite calculations below are necessary because the
existing fixed-label loci do not identify these original matrices.

In cases 1 and 2 the six support-intersection sizes in the order
ab,ac,ad,bc,bd,cd are (0,1,1,1,1,0). In case 3 they are
(0,1,1,0,0,0). This follows directly from the table: all four K-pairs
are mutually disjoint in each case. The four I-pairs are distinct;
their lexicographic order gives both required label inequalities.

### Complete linear certificates

Stack the four original six-row matrices N_j into M with 24 rows
and 21 columns, using zero-based indices. In cases 1 and 2 use the
19-by-19 minor with row and column sets

    rows: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20
    cols: 0,1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20.

With all matrix entries represented by residues 0 through 96, the
integer determinants, and hence their residues in F_97, are

    case 1: 7894757018913989585459133197352960 = 28 mod 97,
    case 2: 6616377667226626862112159105024 = 43 mod 97.

In each case the two coordinate wedges
p_1=e_1 wedge e_18 and p_2=e_8 wedge e_12 belong to the kernel.
Indeed each of their coordinate pairs has exactly one coordinate in
every I_j, so Q_j kills that factor and the exterior image vanishes.
They are independent (their nonzero columns are respectively 2 and
6). The nonzero minor gives rank at least 19 and these two vectors
give rank at most 19. Thus the complete kernel, over every E, is
exactly E*p_1 direct-sum E*p_2. This proves exhaustion without a
rational-point enumeration or generic-rank assumption.

For case 3 use all 21 columns and rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21.

The integer determinant is

    227761032004793473582820103368673853440 = 27 mod 97.

Consequently M has rank 21 and zero kernel over every E. A plane
would give a nonzero wedge in that kernel, so its locus is empty.

All original Q/N entries, the selected minors, their integer
determinants, complete kernel bases and original residuals are in
`scripts/seven-coordinate/four-row-finiteness-probe.json`.
Reproduction command:
`python3 scripts/seven-coordinate/four_row_finiteness_probe.py`.
The program reuses the inspected original builder and incremental
elimination; a separate fraction-free integer determinant calculation
checks each minor residue, with exact divisions. The kernel basis
has an identity submatrix in its free columns, and all residuals
are checked. These arithmetic paths share Python and the matrix
construction; they are not a separately audited implementation.

### Decomposability and all four exact ranks

In either nonempty case every nonzero kernel element has the unique
form p=s*p_1+t*p_2, where (s,t) is not (0,0). The Plucker equation on
the ordered coordinates (1,8,12,18) is

    p_(1,8)*p_(12,18)-p_(1,12)*p_(8,18)+p_(1,18)*p_(8,12)=s*t.

Hence decomposability requires st=0. Conversely, when st=0 the
nonzero vector is a scalar multiple of one of the two displayed
elementary wedges, so it is decomposable. All other 34 equations
vanish identically on this two-dimensional kernel; their complete
coefficient records are saved and were inspected. Over any field,
st=0 forces s=0 or t=0. Projectivizing therefore leaves exactly the
two stated distinct points and their uniquely determined planes.

For completeness Q_j(e_i)=0 if i belongs to I_j, and Q_j(e_i) is
nonzero if i does not. In the latter case, if i is not z_j its
x=i entry equals g_j(z_j), which is nonzero. If i=z_j, its entries
are -g_j(x), all nonzero. The g_j values on S are nonzero because
their roots are in J. Each plane's two coordinate labels meet
each of the four I_j in exactly one label. Thus one basis image
vanishes and the other does not: all four ranks are exactly one,
not zero or two. The certificate records all eight restrictions
for each of the two nonempty cases and their ranks. No recovery
direction, weight, finite chart or coding-field descent is inferred.

The result closes only these local locus computations. In particular,
the vanishing of every coordinate-plane candidate in the third case
does not imply that other quadruples have no noncoordinate family.
The three tests supply neither the universal assertion nor its negation.

## Mathlib

Full matching coverage for these three exact original-map loci: not
checked. Supporting finite-field determinants, exterior powers and
Plucker equations: not checked. Unknown coverage is not absence, and
the arithmetic certificate is not proof-assistant verification.
