# L078 — Seed-free affine-plane cross-ratio obstruction

## Hypotheses

Let k=F_97, H its order-sixteen multiplicative subgroup, and F=F_(97^20).
Fix any bijection lambda from L072's abstract points to H, and use its
sixteen selected blocks. Suppose they are the full supports of an L010
equality pencil, so that L077's pairwise distinct syndrome directions
and all its 48 cross-ratio identities hold. The conclusion also applies
whenever those distinct directions and identities exist, without assuming
that they suffice for moment realization. The direct L077 input and this reduction passed the separate L079
audit. The rank-27 application through L073–L076 remains unaudited.

For abstract labels p,q,r,s write

    chi_lambda(p,q,r,s)
      = (lambda(r)-lambda(p))(lambda(s)-lambda(q))
        /((lambda(s)-lambda(p))(lambda(r)-lambda(q)).

Define the following four elements of k:

    A = chi_lambda(y_1,z_2,w_1,d_1),
    B = chi_lambda(y_2,c,d_6,d_5),
    C = chi_lambda(b,z_1,d_2,d_7),
    D = chi_lambda(a,d_4,d_3,w_2).

Each tuple consists of four distinct labels. Thus all four ratios are
nonzero and different from one; all their denominators are nonzero.
These tuples are the four singleton sets occurring among quadrilaterals
through V0, with exactly the displayed orders.

## Conclusion

Put

    U = A+B-AB-AC,
    V = A+C-AC-BC,
    R(A,B,C,D) = (U-DV)^2 + 4BCD(1-A)(1-B).

Every such equality realization must satisfy R(A,B,C,D)=0 in k.
This condition contains no syndrome-direction seed and holds for every
bijection and arbitrary original extension-field weights and chart.
For any fixed admissible A,B,C there are at most two admissible D in k
satisfying it. This gives the upper bound 2*95^3=1,714,750 on necessary
ordered ratio tuples, against the unrestricted 95^4=81,450,625. These are
bounds on ratio tuples, not labelings or actual pencils; no census is
claimed and zero or one admissible root is possible.

For example, the explicit row-major labeling displayed below has
(A,B,C,D)=(74,39,24,24) and R=7, so is excluded. This single regression
demonstrates the condition's applicability, not a uniform family decision.
R=0 is only necessary: it does not establish distinct reconstructed
directions, all 48 identities, a nonzero original alternating kernel,
full moment recovery or any L010 equality gate. No global improvement
of 11/q–16/q, uniform triangle twelve or challenge resolution follows.
This restriction passed the separate critical audit recorded below.

## Proof

### Twelve equations through one block

Use only L077's quadrilaterals whose vertical block is V0. Their
syndrome directions are pairwise distinct. A projectivity of the syndrome
line sends t_V0 to infinity, t_M0D0 to zero and t_M1D0 to one. It exists
since these three directions are distinct. This normalizes only the
syndrome line; it neither replaces the original affine input chart nor
assumes its excluded point is rational. All other fifteen directions
are finite in this normalization, since none equals t_V0. Write

    h_j = t_M0Dj, d_j = t_M1Dj, e_j = t_M2Dj (0<=j<4),
    h_0=0, d_0=1.

The scalar h,d,e coordinates may initially lie in F. For finite h,d,e,
L077's convention gives chi(infinity,h,d,e)=(e-h)/(d-h), with d-h
nonzero. Thus an identity with right side r is equivalent to

    e = (1-r)h + r d.                                      (1)

For four distinct points, rotating the last three slots of chi gives
r, 1/(1-r), (r-1)/r. For instance, after taking the first three points
to infinity, zero, one, the fourth is r; direct evaluation at
(infinity,1,r,0) and (infinity,r,0,1) gives the other two values.
Cross-ratio invariance proves these formulas before normalization too.

The following complete table of twelve equations follows from L077's
incidence formula or the displayed L072 blocks. It lists the horizontal,
slope-one and slope-u indices and the singleton ratio, in that order.

| j | k | l | r in e_l=(1-r)h_j+r d_k |
|---|---|---|---|
| 0 | 1 | 3 | A |
| 0 | 2 | 1 | B |
| 0 | 3 | 2 | C |
| 1 | 0 | 2 | 1/(1-B) |
| 1 | 2 | 3 | D |
| 1 | 3 | 0 | (A-1)/A |
| 2 | 0 | 3 | 1/(1-C) |
| 2 | 1 | 0 | (B-1)/B |
| 2 | 3 | 1 | (D-1)/D |
| 3 | 0 | 1 | 1/(1-A) |
| 3 | 1 | 2 | 1/(1-D) |
| 3 | 2 | 0 | (C-1)/C |

These are every j,k with k!=j; L077 fixes l in each case. All
ratios and all cleared factors are nonzero as required. The first
three equations and the three with k=0 give, without losing a branch,

    e_3=A d_1, e_1=B d_2, e_2=C d_3,
    h_1=(1-(1-B)C d_3)/B,
    h_2=(1-(1-C)A d_1)/C,
    h_3=(1-(1-A)B d_2)/A.                                 (2)

The equations with j,k=(1,2),(2,3),(3,1) then give

    AB d_1 - BD d_2 + (1-D)(1-B)C d_3 -(1-D)=0,
    (1-C)A d_1 + CBD d_2 - C(D-1)d_3 -1=0,
    A d_1 + D(1-A)B d_2 - A(1-D)C d_3 -D=0.              (3)

The remaining three equations prescribe the same e_0:

    e_0=(h_1+(A-1)d_3)/A
       =(h_2+(B-1)d_1)/B
       =(h_3+(C-1)d_2)/C.

Equate the first expression with each of the other two and substitute
(2). Clearing the nonzero factors yields two further equations

    [A^2(1-C)-AC(B-1)]d_1
      + C[B(A-1)-C(1-B)]d_3 +(C-A)=0,
    [B^2(1-A)-AB(C-1)]d_2
      + [BC(A-1)-C^2(1-B)]d_3 +(C-B)=0.                   (4)

The derivation retains every projective branch: only V0 was sent to
infinity, the other directions were thereby finite, and all divisions
were by nonzero label ratios or their complements. It does not use
prime-field descent of the syndrome plane.

### Exact elimination

Equations (3)–(4) say M(d_1,d_2,d_3,1)^transpose=0, where

    M =
    [ AB             -BD                 (1-D)(1-B)C                   -(1-D) ]
    [ (1-C)A          CBD                -C(D-1)                       -1     ]
    [ A               D(1-A)B            -A(1-D)C                      -D     ]
    [ A^2(1-C)-AC(B-1) 0                 C[B(A-1)-C(1-B)]               C-A    ]
    [ 0               B^2(1-A)-AB(C-1)   BC(A-1)-C^2(1-B)              C-B    ].

Number its rows 0,...,4. Its kernel contains a nonzero vector whose
last coordinate is one, so every four-by-four minor must vanish over F.
Direct determinant expansion, with column order as displayed, gives

| Rows | Determinant |
|---|---|
| 0,1,2,3 | ABCD R |
| 0,1,2,4 | ABC R |
| 0,1,3,4 | ABC(1-B) R |
| 0,2,3,4 | ABC(1-A) R |
| 1,2,3,4 | ABC(1-C) R |

Here R is exactly the polynomial in the conclusion. In particular,
the expansion of det M_(0,1,2,4), grouped by powers of D, is

    ABC [ U^2 + (-2UV+4BC(1-A)(1-B))D + V^2 D^2 ].         (5)

Expanding U=A+B-AB-AC and V=A+C-AC-BC in (5) is the determinant
expansion; it verifies the displayed factorization without division.
The other four expansions have the factors in the table. Only (5)
is needed for necessity. Since ABC!=0, its vanishing implies R=0
in F and hence in k, because all four ratios and coefficients lie in k.
We do not reverse the implication: vanishing maximal minors can still
leave an incompatible affine system or forbidden direction collisions.

For fixed A,B,C, R is a polynomial in D of degree at most two. If
V!=0 its leading coefficient V^2 is nonzero, so it has at most two
roots. If V=0 its coefficient of D is 4BC(1-A)(1-B), which is nonzero
in characteristic 97. It is then a nonconstant linear polynomial,
so has at most one root. In particular it can never be identically
zero for admissible A,B,C. A degree-d nonzero polynomial over a field
has at most d roots, by successive division by X-r at distinct roots.
This proves the bound, including all degree-drop branches. It is a
restriction on labels, independent of any original chart or weights.

### Exact reproducible algebra and one obstruction regression

`python3 scripts/triangle-incidence/affine_plane_ratio_elimination.py`
expands all five determinants in the polynomial ring k[A,B,C,D],
compares them coefficient by coefficient with the table, and saves
all matrix entries, all five full expanded minors, R, the five factors
and the complete difference polynomials in
`scripts/triangle-incidence/affine-plane-ratio-minors.json`.
All five differences are exactly zero, not pointwise sampled tests.
The determinant and polynomial operations are explicit in that script;
the proof is the finite distributive expansion (5), rather than an
inference from its numerical regression.

For that regression map the row-major L072 point table to increasing H:

    (a,b,y_1,y_2,c,d_1,d_2,d_3,z_1,d_4,d_5,w_1,z_2,d_6,w_2,d_7)
      -> (1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96).

Substitution gives (A,B,C,D)=(74,39,24,24). Then U=10 and V=5,
so U-DV=84 in k, and 4BCD(1-A)(1-B)=32. Thus R=72+32=7 in k.
The exact augmented matrix stored in the certificate has rank four,
consistent with (5); ABC is nonzero. This excludes precisely this
labeling by the necessary condition. No random labeling, maximal rank
census or general inference from positive-only samples is used.

The remaining concrete closure test is simultaneous enforcement of
this seed-free condition and the other quadrilateral equations for all
bijective H-labelings, retaining all collision and infinity cases.
A passing ratio tuple alone supplies none of the original moment gates.
L077's two-seed reconstruction is still available for surviving labelings;
its alternative rank-27 input chain remains unaudited. L079 separately
excludes this family using the direct equality-pencil identities. Independent support extraction and challenge-definition gaps
remain unresolved. The ready EXPLORE assessment is reused for this
uniform elimination step; the sources checked do not certify originality.

The separate October 12 L079 audit found no defect in this direct
necessary reduction: it checked every elimination pivot, both e0
comparisons, all five exact determinant identities and the linear
degree-drop case. The complete original-system and incidence-table
replays are recorded in L079. The rank-27 chain remains outside scope.

## Mathlib

Coverage of this exact four-ratio elimination and family-specific
obstruction is not checked. No Mathlib theorem is used; unknown
availability is not absence. L077 supplies the established local
cross-ratio identities and their hypotheses; its primary incidence
source is imported through L072. The elementary determinant identity
and degree-two root bound are written out above. No general design,
MDS theorem or previously inspected source theorem is reproved.
