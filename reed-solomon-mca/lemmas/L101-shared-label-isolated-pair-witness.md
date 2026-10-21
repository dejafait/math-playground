# L101 — Two full isolated recoveries through one shared triangle label

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
embedded in F, and let C=RS[F,H,8]. Use L010's shifted moments
sigma_j(e)=sum_(x in H)e(x)x^j for 1<=j<=8 and the pinned radius
cell 1/4<=delta<5/16. Use L041's local converse and L057's triangle
notation, without any equality or high-count hypothesis. All explicit
numbers below are residues modulo 97, embedded in F. The conclusion
is existential: it makes no claim that arbitrary original charts or
arbitrary normalized weights descend to this prime subfield.

## Conclusion

Two full isolated additional recoveries through the **named shared
label a=1** can coexist with the three gated triangle base errors,
with all five supports pairwise linear. An explicit choice is

    a=1, b=27, c=75,
    Y={8,12}, Z={18,70}, W={47,96},
    (p,q,r)=(2,14,75), (gamma_0,gamma_1,gamma_2)=(0,1,2), lambda=1.

The two additional supports are K={1,22,50,79} and L={1,47,85,89},
with isolated scalars mu_K=42, mu_L=6 and original finite parameters
T_K=75, T_L=73. Every recovered weight is nonzero. These are actual
same-support bad parameters for a single original affine pencil,
not merely projected candidates. Thus a uniform exclusion of the
approved local pair is false. This rules out that shortcut only:
no sixteen-count completion, uniform additional-recovery bound,
global interval improvement or challenge resolution follows. The
separate critical audit on 2026-10-17 found no defect in this local
existence claim; it supplies no stronger count statement.

## Proof

### Imported framework and an explicit original pencil

L057 already specializes the following standard inputs, whose inspected
coverage is reused from the saved assessment
`drafts/literature/2026-10-17-shared-label-isolated-pair-test.md`.
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, author TeX
v9.2, July 17, 2026, lines 2785–2935, DR2
(`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), in the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
give the fixed-support recurrence for distinct weighted Vandermonde
columns, nonzero multipliers and support size t<R, including zero
directions. Here R=8, t=4, multiplier x and eta_j=s_(j+1).
This mutable source is not certified identical to ePrint 2026/1463.
J. I. Hall, *Notes on Coding Theory*, Theorem 5.1.1, printed pp. 63–65
of the [GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
provides the distinct-evaluation, nonzero-multiplier GRS framework;
n=16,k=8 satisfies its hypotheses over F. L041's local converse and
L057's fully restored criterion are the existing local inputs. No
recurrence or general distance theorem is reproved. The additional
work here is an exact simultaneous specialization not supplied by
those single-support statements; the literature search establishes
no originality claim.

For these nine base labels,

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    H minus U={22,33,50,64,79,85,89}.

Let Q(X)=product_(h in H minus U)(X-h). Its needed evaluations are

| x | 1 | 27 | 75 | 8 | 12 | 18 | 70 | 47 | 96 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| c_x=Q(x) | 18 | 29 | 14 | 82 | 27 | 22 | 12 | 94 | 46 |

They are nonzero. The three alpha_i are (96,2,96), so L041's
weights lambda*c_x*b_(i,x)/alpha_i give the first three rows below.
Each list of weights is in the displayed support order; all other
coordinates are zero.

| Error | Parameter | Ordered support | Actual weights |
| --- | ---: | --- | --- |
| e_0 | 0 | (1,27,8,12) | (61,79,15,70) |
| e_1 | 1 | (1,75,18,70) | (88,40,11,6) |
| e_2 | 2 | (27,75,47,96) | (86,66,3,51) |
| e_K | 75 | (1,22,50,79) | (61,39,49,13) |
| e_L | 73 | (1,47,85,89) | (92,74,75,92) |

The normalized gate p(1-p)q(1-q)r(1-r)!=0 holds, since none of
2,14,75 is 0 or 1. Choose the actual words a_*=e_0 and b_*=e_1-e_0.
Their syndrome pencil is s(T)=s_0+T d, where

    s_0=(50,16,29,23,54,29,58,91),
    d  =(67,16,52,21,90,47,42,20).

Direct evaluation of all eight defining moment sums yields

| Error | sigma_1,...,sigma_8 = s_0+T d |
| --- | --- |
| e_0 | (50,16,29,23,54,29,58,91) |
| e_1 | (20,32,81,44,47,76,3,14) |
| e_2 | (87,48,36,65,40,26,45,34) |
| e_K | (31,52,49,46,14,62,7,39) |
| e_L | (91,20,42,4,28,65,20,96) |

These are finite exact equalities in F_97, hence also in F. In
particular the first three rows verify the actual local converse,
and both additional errors satisfy the full moments. The two
syndrome directions are independent: the first two coordinates of
s_0,s_0+d have determinant 50*32-16*20=19!=0 modulo 97.
No extension-field root, interpolation at an unlisted parameter,
or numerical approximation is a premise.

### Isolated classification and finite gates

It remains essential to check that these full errors belong to the
**isolated** branch of L057. This does not follow merely from their
moment identities. For R=K,L let f_R(X)=product_(x in R)(X-x) and
write F_R(n)=(sum_(j=0)^4 f_(R,j)n_(i+j))_(i=1)^4 for the
recurrence of an eight-moment vector. Let C_R have columns
F_R(v_b),F_R(v_c). These are precisely the missing shared-label
columns because both R contain a and omit b,c.

The following are the columns and the two raw recurrence vectors
F_R(Y),F_R(Z), with Y,Z denoting their c-weighted moment vectors
as in L057:

| R | F_R(v_b) | F_R(v_c) | F_R(Y) | F_R(Z) |
| --- | --- | --- | --- | --- |
| K | (91,32,88,48) | (56,29,41,68) | (90,82,81,53) | (2,96,11,94) |
| L | (78,69,20,55) | (64,47,33,50) | (12,56,65,95) | (78,51,7,85) |

The first-two-row determinants of C_K,C_L are 71 and 26, both
nonzero. For a vector v, subtract C_R times the unique solution
matching its first two rows, then keep the last two rows. This is
a quotient map with kernel exactly im C_R. The subtracted coefficient
pairs and resulting quotient vectors are

| R | coefficients for Y; Z | quotient Y; quotient Z | mu |
| --- | --- | --- | ---: |
| K | (24,70); (18,47) | (46,58); (89,11) | 42 |
| L | (48,69); (8,43) | (29,19); (77,17) | 6 |

Both quotient vectors in each row are nonzero, and quotient Z
equals mu times quotient Y. This quotient and L057 (5) have the
same kernel and dimension two, so nonzeroness, proportionality
and the ratio mu are unchanged by their invertible change of
quotient basis. Thus both recoveries are isolated, with distinct
mu in F_97 minus {0,-1}. This calculation does not identify a
both-zero quotient as an intersection or discard restored equations.
The full moment table has already verified their lift.

Here g=1,rho=2, so L057's finite denominator is E=2+mu. Its values
are 44 and 8, both nonzero; T=rho/E gives 75 and 73. The five
original parameters 0,1,2,75,73 are pairwise distinct and finite.
The numerator weights omega=E*e_R, in the support orders above, are
(65,67,22,87) and (57,10,18,57). All eight are nonzero. Thus the
fourth-weight and original finite-chart gates are retained, without
needing a rationality assumption on an externally prescribed chart.
These particular allowed chart and weights suffice for existence.

### Linearity, nonpersistence and the pinned bad-support event

Write A_i=supp(e_i). The ten actual pair intersections are

    A0 intersect A1={1},  A0 intersect A2={27},
    A0 intersect K ={1},  A0 intersect L ={1},
    A1 intersect A2={75}, A1 intersect K ={1},
    A1 intersect L ={1},  A2 intersect K =empty,
    A2 intersect L ={47}, K  intersect L ={1}.

This checks all five-support linearity gates. In particular a is
the specified label shared by A0,A1, not a relabeled singleton.
The first three supports have empty common intersection and all
their weights are full. L041's local converse therefore supplies
nonzero D and every nonpersistent coordinate locator. Alternatively,
at a full four-error parameter L010's Hankel factorization has
nonzero determinant; and for any coordinate x some base support
omits x, where the actual locator is nonzero. These facts concern
the original pencil defined above, without equality completion.

L010's kernel identity now makes a_*+T b_*-e_R a codeword at each
listed parameter, so it agrees on the same twelve-coordinate
complement H minus R. To check input failure on that complement,
suppose b_* restricted there were a restricted codeword. Then
sigma(b_*) would belong to the span of its four moment columns.
As s(T) belongs to that span, so would s(0) and s(1). L010's
uniqueness of weight-at-most-four representatives would force both
e_0 and e_1 to be supported on R, hence A0=A1=R by their full
weights. This contradicts the displayed distinct supports.
Thus the input fails on the same support where agreement is
witnessed, including at the two additional parameters. This is
the pinned bad event, not just closeness.

The explicit tables prove existence independently of a complete
search. The discovery enumerator stopped on a projected candidate
after 155,829 triangle assignments and 11,998,813 support tests;
this prefix is no census or bound. Reproduce discovery with

    clang++ -std=c++17 -O3 scripts/triangle-recovery/shared_label_pair_search.cpp -o /private/tmp/mca-shared-label-pair-search
    /private/tmp/mca-shared-label-pair-search

The candidate is saved in
`scripts/triangle-recovery/shared-label-pair-candidate.json`.
Run `python3 scripts/triangle-recovery/verify_shared_label_pair.py`
for independent first-four Gaussian recovery followed by all eight
moment equations and a separate recurrence-column elimination.
Its full positive certificate is
`scripts/triangle-recovery/shared-label-pair-verification.json`.
The replay checks 40/40 moment equations, 5/5 full errors, 2/2
isolated additional recoveries, 5/5 distinct finite parameters,
10/10 linear intersections and 5/5 same-support input failures,
with zero failures. All load-bearing values in that certificate
were inspected. This is verification during construction, not
the later independent critical audit.

### Separate critical audit (2026-10-17, step 275)

The audit checked the complete proof, both programs and all load-bearing
positive-certificate values against L010's kernel/uniqueness and
pointwise locator facts, L041's local converse, and L057's exact criterion.
No mathematical defect was found. The existing verifier was rerun and
reproduced its certificate byte for byte (SHA256
`d730421bd9248129cca2dfd55ae508f631dc09c73fe355bf14fb51593dab7d04`).
The incomplete discovery prefix was inspected but not rerun or used as
negative or exhaustive evidence. This validates the local counterexample;
it establishes no originality beyond the previously checked coverage.

In particular, the quotient identification can be made fully explicit.
Here J={27,75}, and G_J(X)=X^2-(b+c)X+bc. On the four recurrence
entries, L057's quotient rows are (bc,-(b+c),1,0) and
(0,bc,-(b+c),1). They annihilate the two columns C_R. After subtracting
the first-two-row solution, a residual is (0,0,u,v), so these rows give
(u,v-(b+c)u)=(u,v-5u). The resulting change from the displayed eliminated
quotient has determinant one. The two nonzero L057 vectors and the
restored coefficients are therefore explicitly:

| R | L057 y; z | beta^Y_b,beta^Y_c | beta^Z_b,beta^Z_c | beta^Z-mu beta^Y |
| --- | --- | --- | --- | --- |
| K | (46,22); (89,51) | (73,27) | (79,50) | (20,80) |
| L | (29,68); (77,20) | (49,28) | (89,54) | (86,80) |

The beta entries are the negatives of the earlier subtracted coefficients,
as required by L057 (6). In both rows the last pair equals
(-mu*c_b*q,c_c*r), exactly the missing-label equations (10). There is
no equation for a because a belongs to each additional support. Direct
evaluation of L057 (13), using Lagrange polynomials rather than Gaussian
recovery, gives the two displayed omega rows. The denominators consist
only of distinct nonzero labels, their differences, E=44 or 8, and
g=lambda=1. All normalized and full-weight gates hold. Thus the original
full-moment computation and the restored isolated criterion agree,
including the sign of beta and the unchanged scalar mu.

For an independent same-support check, the audit interpolates the actual
word a_*+T*b_*-e at eight H nodes and verifies its degree-at-most-seven
polynomial at all sixteen nodes for each of the five errors. For b_* on
each twelve-node complement, its unique degree-at-most-seven interpolant
on the first eight sorted nodes disagrees at all four remaining nodes.
An interpolant over F would have the same coefficients by uniqueness,
so this proves restricted-input failure over F, not only F_97. These
checks independently confirm the analytic uniqueness argument above.

Direct determinant expansion gives D at the five listed parameters as
(78,41,7,8,90), all nonzero, and verifies L(T,x)=D(T)f_R(x) for every
x in H at every listed T. Each x is omitted by a base support, so these
pointwise checks certify every nonpersistent locator without invoking
equality. The ten displayed intersections and all finite parameters
were checked exhaustively for this five-error witness.

Reproduce this bounded audit with

    python3 scripts/triangle-recovery/audit_shared_label_pair.py

The full certificate is
`scripts/triangle-recovery/shared-label-pair-critical-audit.json`.
It records 40/40 moments, 5/5 full errors, 2/2 isolated recoveries,
4/4 restored missing-label equations, 10/10 intersections, 5/5 distinct
finite parameters, 80/80 residual-codeword evaluations, 5/5 same-support
failures and 16/16 nonpersistent locators, with zero audit failures.
The new check path imports no producer or verifier helpers; all paths
still share exact residue arithmetic and the stated local mathematical
framework. No arbitrary-chart descent, H-label symmetry, completion,
projected MDS hypothesis or improved global bound is inferred.

## Mathlib

Coverage of this exact simultaneous witness and L057's triangle
criterion has not been checked. No full matching formal theorem
is claimed; unknown coverage is not evidence of absence. The
finite tables and complete field-arithmetic replay are informal
evidence, not a Mathlib formalization.
