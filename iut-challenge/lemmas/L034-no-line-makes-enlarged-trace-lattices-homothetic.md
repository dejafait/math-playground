# L034 — No line makes the enlarged trace lattices homothetic

## Hypotheses

Let L=Q_3(zeta_20,pi), where zeta_20 has order 20 and pi^27=3,
theta=zeta_20^4, O=O_L, J=log(O^times), V=ker(Tr_(L/Q_3)),
C=O intersect V and M=J intersect V. Use the genuine complete ordinary
unit logarithm. L031 supplies the audited integral coordinate basis
theta^a pi^r, 0<=r<=26, 0<=a<=3, indexed by 4r+a, and the full
rank-108 Z_3-basis J=(B_int/9)Z_3^108. Its complete integer matrix is
`/integer_basis_matrix` in `scripts/cyclotomic-log/enlarged-basis.json`.
No O_U-module structure on J is imposed.

For the source-line application only, use L032's admitted presentation:
its actual y_1 is a primitive element of M. No coordinates of y_1 are
prescribed, and no converse realization of an arbitrary line is assumed.

Import **John Voight, Quaternion Algebras**, Springer GTM 288 (2021),
chapter 9, section 9.3, **Theorem 9.3.9**
([primary chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_9))
for simultaneous relative lattice factors. Over the DVR Z_3 its
fractional-ideal factors are integral powers of 3; nesting is unnecessary.
Import **Peter Bürgisser, Avinash Kulkarni and Antonio Lerario,
Nonarchimedean integral geometry**, Selecta Mathematica **32:10 (2026)**,
version of record 5 January 2026, **section 2.2**, pp. 13–14,
**Lemmas 3.1.4(1–3)/3.1.5**, pp. 21–23, and **Proposition 4.1.2**,
pp. 35–36
([primary publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)).
These supply full intersection/quotient lattices and quotient-only
singular-value interlacing, sigma_i>=sigma''_i>=sigma_(i+d) when
the target is quotiented by a d-dimensional subspace. Their local
scalar field here is Q_3 and their valuation ring is Z_3.
These statements are imported, not reproved. The specific exact factors
and their application to this pair are the required specialization.

## Conclusion

There is **no** primitive rank-one Z_3-submodule F of M and no
a in Q_3^times such that, in the same rational quotient,

    q_F(C)=a q_F(M),    q_F: V -> V/(Q_3 F).

In fact no rational line in V gives such equality. The relative Smith
exponents of the identity from (V,C) to (V,M), in increasing order, are

    -1 (36 times), 0 (48 times), 1 (16 times), 2 (7 times).

Thus the actual fixed line of L032 cannot make this projected container
homothetic to the projected logarithm lattice. This is a local
**REPRODUCTION** by known methods, validated by the separate critical audit below.
It is neither a container-noninvariance theorem nor a numerical radius
bound, an actual input/action realization or an essential IUT flaw.
The original finite B>=A gap remains open.

## Proof

### Complete trace intersections

Trace transitivity and the roots of X^27-3 give
Tr_(L/U)(pi^r)=0 for 1<=r<=26, and Tr_(L/U)(1)=27,
where U=Q_3(theta). Indeed the embeddings over U send pi to
pi times all twenty-seventh roots of unity, whose r-th powers sum to
zero for these r. The conjugates of theta are all four primitive fifth
roots, so Tr_(U/Q_3)(theta^a)=-1 for a=1,2,3, and Tr(1)=4.
Consequently the trace functional in the complete field coordinates is
27 tau, with

    tau=(4,-1,-1,-1,0,...,0).

Writing e_i for the coordinate vectors, the 107 columns
e_0+4e_1, e_0+4e_2, e_0+4e_3, e_4,...,e_107 form a Z_3-basis
C_0 of C. They have trace zero. Conversely tau(z)=0 says
z_0=(z_1+z_2+z_3)/4, so the first three basis coefficients are
z_1/4,z_2/4,z_3/4, which are in Z_3 since 4 is a unit; all remaining
coordinates are unrestricted. This proves the full intersection,
not a rational span or finite-index sublattice.

Set t=tau B_int, an integer row. The exact certificate stores integer
108-by-108 matrices A and A_inv with

    A A_inv=A_inv A=I_108,    t A=(1,0,...,0).

They are obtained by extended-gcd column operations, each with integer
inverse. The complete identities are checked entry by entry, and the
recorded gcd is 1. Since trace on J coordinates is 3t, the integral
trace kernel is exactly the span of columns 1,...,107 of A (numbering
from zero). Thus the 108-by-107 matrix

    M_0=(B_int/9) A_(columns 1,...,107)

is a full Z_3-basis of M. This is the full integral kernel, which is
saturated: invertibility of A gives both containments and no hidden index.

### Exact relative factors

The certificate stores the full rational 107-by-107 matrix R with

    M_0 R=C_0.

The verifier checks this identity in all 108 field coordinates. Therefore
R is the matrix of the identity with domain C-basis C_0 and target
M-basis M_0. The complete 277 elementary row/column operations take R
to the stored diagonal D. Every swap has a unit determinant. Every
addition has coefficient in Z_3, checked by its exact rational
3-adic valuation, and has its inverse obtained by negating that
coefficient. Hence these operations give U_R,V_R in GL_107(Z_3)
with U_R R V_R=D. The verifier replays every operation on all entries
and checks the full diagonal equality, not just determinant or rank.
All diagonal entries are nonzero. Their valuations, ordered increasingly,
are exactly the 107 exponents in the conclusion. Dividing each diagonal
entry by its indicated power of 3 gives a Z_3-unit, which can be removed
by a unit row scaling; thus these are precisely the relative Smith
factors of the cited simultaneous normal form.

Full evidence, including both kernel transforms, both complete lattice
bases, R, all operations and D, is in
`scripts/cyclotomic-log/projected-container-homothety.json`.
It pins the unchanged L031 input by SHA256
`ad5ea1741a5cc54d5413ab679fd4fba387e8a2aafc8d9c7c2b6d31e799159102`.
Reproduce and then independently replay the saved evidence with

    python3 scripts/cyclotomic-log/projected_container_homothety.py
    python3 scripts/cyclotomic-log/projected_container_homothety.py --verify

Both runs have zero failures. The verifier does not invoke the builder's
Smith or kernel algorithms: it checks the saved full identities and
every invertible operation. Its complete checks and zero-failure record
are in `scripts/cyclotomic-log/projected-container-homothety-verification.json`.
L031's audited complete-unit and infinite-tail proofs remain the analytic
input; this rational calculation does not replace them.

### Exclusion for every line and scalar

Equip V with the lattice norms defined respectively by C and M. If
alpha_1<=...<=alpha_107 are the exponents just calculated, the singular
values of the identity are sigma_i=3^(-alpha_i), in descending order.
For any rational line W, apply the cited quotient-only Proposition
4.1.2 with target subspace W and quotient lattice q(M). The projected
map has rank 106; the cited quotient-lattice results identify its 106
nonzero factors with those of q(C) relative to q(M).

If q(C)=a q(M), write k=v_3(a). Its unit factor preserves q(M),
so all 106 projected singular values equal |a|_3=3^(-k).
Interlacing therefore requires, for every i=1,...,106,

    alpha_i <= k <= alpha_(i+1).

At i=1 this forces k<=alpha_2=-1; at i=106 it forces
k>=alpha_106=2. No real number, and hence no integer valuation k,
can satisfy both. This excludes every rational line, without a
sufficiency assumption or enumeration of possible coordinates.
Every primitive F in the question defines such a rational line, and
M/F identifies with q_F(M); thus the approved target is settled.
L032's actual primitive line is included as a specialization.

No field valuation is placed on V/W. The argument uses only Q_3-lattice
norms and same-space equality of quotient images. It does not assert
that arbitrary primitive lines arise from source presentations, that
C is Gamma-invariant, or that failure of homothety already implies a
source action escaping a numerical container. Such downstream work
requires its own hypotheses and review. Fixed-line/numerical control,
actual/native input and action compatibility, packet/global realization,
pilot transport and essentiality remain unresolved.

### Separate critical audit, 2026-10-08

The independent audit validates the stated relative factors and all-lines
exclusion. It found no mathematical error requiring a changed conclusion
or hypothesis. The earlier phrase "nonsaturated integral kernel" has been
corrected above: the kernel of a map from a free Z_3-module into the
torsion-free Q_3 is saturated. This wording repair changes no matrix,
lattice or proof step. No new general theorem or IUT flaw is claimed.

The analytic input remains audited L031. Its complete unit reduction
uses all four residue directions at all thirteen shallow depths and all
80 residue roots; the deep ideal is pi^14 O, with 14/27>1/2. The
uniform omitted-term bound starts at pi-valuation 108>=14 and increases
to infinity. Both complete integral-span identities identify B_int/9
with the genuine J. Thus using that pinned basis here assumes neither
O_U-stability nor an approximation to the logarithm image. L032 is used
only to identify its actual y_1 as primitive in this same M.

For C, trace transitivity applies in the finite separable tower L/U/Q_3.
The 27 conjugates over U give zero trace for every pi^r with 1<=r<=26,
and the four fifth-root conjugates give the stated constant trace row.
Every vector of C has the unique coordinates z_1/4,z_2/4,z_3/4 and
z_4,...,z_107 in C_0; 4 is a Z_3-unit. For M, write any J vector as
(B_int/9) A u with u in Z_3^108. The verified tA=(1,0,...,0)
then gives its trace as 3u_0. Its trace vanishes exactly when u_0=0,
which proves the full intersection and rank 107. No rational saturation
or finite-index replacement is hidden in either computation.

Run the independent saved-certificate audit with

    python3 scripts/cyclotomic-log/audit_projected_container.py

It imports no builder or original-verifier code. It checks the pinned
L031 hash, all matrix shapes and integer entries, both full inverse
identities for A, the complete trace row and its gcd 1, both full bases,
and M_0 R=C_0 in all 108 coordinates. It reads all 277 operations with
strict index/arity checks and verifies every addition coefficient is
3-integral. It accumulates their left and right matrices separately,
then checks U_R R V_R=D as a full matrix identity. Independently reversing
every operation takes D back to R. Each elementary inverse is integral;
hence these are GL_107(Z_3) changes, not rational basis changes that
could alter the relative factors. All 107 nonzero diagonal entries,
their ordered valuations and all unit parts are checked. The original
saved-evidence verifier also passes after inspection of its code.

The independent evidence, including the full left/right matrices,
every operation's integrality check, the complete diagonal and all 106
interlacing intervals, is saved in
`scripts/cyclotomic-log/projected-container-independent-audit.json`.
There are 857 named finite checks and zero failures. These checks verify
the exact finite certificate; the analytic and quotient arguments remain
the mathematical proofs given here, not conclusions from that count.

For clarity about the projected factors, fix any rational line W in V.
The imported quotient-lattice theorem makes q(M) and q(C) full lattices
of rank 106. The surjection q:(V,C)->(V/W,q(M)) has rank 106. Its
rectangular Smith form therefore has 106 nonzero diagonal factors and
one zero domain column. Integral domain and target basis changes do not
change its image lattice, which is exactly q(C). Thus its nonzero
factors are precisely those of q(C) relative to q(M). This uses the
cited Smith and quotient results, not a new quotient theorem; no
simultaneous deletion of domain and target is being substituted for
target-only interlacing.

If q(C)=a q(M), writing a=3^k u with u in Z_3^times gives all those
factors the same absolute value 3^(-k). The cited Proposition 4.1.2
applies over Q_3/Z_3, with d=1, to the identity on the original
107-dimensional V, irrespective of whether C lies in M. Converting
sigma_i>=sigma''_i>=sigma_(i+1) by the decreasing function 3^(-x)
gives alpha_i<=k<=alpha_(i+1), in the stated orientation. The full
interval intersection has lower endpoint max_(1<=i<=106) alpha_i=2
and upper endpoint min_(1<=i<=106) alpha_(i+1)=-1. It is empty even
over the reals, so excludes every scalar and every rational line.
For primitive F in M, M intersect Q_3 F=F, giving the claimed integral
quotient identification. L032's source line meets this hypothesis.

Only the inherited primary normal-form and quotient-only interlacing
coverage is used. Its minimax cross-reference is understood as
Proposition 4.1.1; Corollary 4.1.3 is not invoked. No new field-valued
norm on V/W, stable-lattice/noninvariance conclusion, numerical estimate
or original-IUT applicability has been introduced. Those obligations
remain separate from this validated local exclusion.

## Mathlib

Full matching enlarged-field trace-lattice exclusion and quotient-only
Smith interlacing: **not checked**. Supporting lattice normal forms,
trace transitivity, quotient lattices and exact matrix identities:
**not checked**. Precise primary citations and the complete specialization
are given above; unknown coverage is not evidence of absence, and no
formal verification is claimed.
