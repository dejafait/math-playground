# L115 — Exterior products cross the joint bulk energy at cubic cost

## Hypotheses

Use exactly L114's R_bulk,sc,Pbulk for both actual L010 probes i=3,6,
SU(2), the straight lower-rooted direction-1 forest, all-face relative
fixed-link box (-4,4)^4, sufficiently fine admitted even N, a=8/N and
tau=1/16. Take the bare small-coupling coefficient at fixed mesh before
refinement. All norms and traces use ordinary stored coordinates.
Retain every interior axial level, transverse end row, both generator
orientations, both exterior coefficient levels and every heat mode.

Import L111's infinite-grid stencils, compact displacement b_(r,t),
and E_j; L113's finite path maps S_alpha and clamped real scalar
coefficients phi_(k,alpha,t); and L114's zero extensions J_1,J_2 and
P_bulk=J_1^* P_inf J_1. The latter is a compression of an orthogonal
projection, hence has norm at most one. It is not treated as a finite
orthogonal projection. Introduce the notation

    A_r=D T_r C_r,
    X_(r;t,j)=J_2^* A_r E_j M^2_(b_(r,t)) J_2,
    psi_(kl;alpha,beta;st)=phi_(l,alpha,s) phi_(k,beta,t).   (1)

A_r is a fixed infinite-grid plaquette-to-plaquette stencil, including
its original component filters. Superscripts 1 and 2 on scalar
multipliers mean edge and plaquette arrays at the common lower-vertex
index. A multiplier between finite operators is its restriction to
those finite rows; otherwise it uses the globally clamped extension.
No edge or plaquette field is smoothly extended across a pinned face.

## Conclusion

Define the following real scalar, retaining all finite compressions:

    R_prod = a sum_(k,l,s,t,alpha,beta,r) c_(i;kl,a) min(s,t)
      Tr_edge[P_bulk S_beta J_2^* A_r E_(t-s)
            M^2_(b_(r,t) psi_(kl;alpha,beta;st)) J_2 S_alpha^T]. (2)

For both probes,

    |R_bulk,sc,Pbulk - R_prod| <= C_i N^3.                (3)

All three scalar coefficients are now on the input side of E_(t-s).
Their product retains its exact s,t dependence and is compactly
supported because b_(r,t) is. All S_alpha, S_beta and A_r filters
remain on their original sides of P_bulk; none is commuted through it.

The error is only cubic-bounded and may contribute to the a^3 limit.
Equation (3) does not bound R_prod itself or prove the transverse H
limit. Finite compressions and the signed frozen-trace transfer remain
uncontrolled. L110/L111/L113's earlier cubic errors also remain. The
complete other/other limit and its comparison with -12 gamma D_i,
other unevaluated functionals, other response jets, finer powers and
logarithm, matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass remain
unresolved.

## Proof

### 1. Bounds and an exact finite-compression identity

In this proof fix k,l,alpha,beta,s,t,r and write psi for (1), b for
b_(r,t), j=t-s, X=X_(r;t,j). L113(3) and the elementary product
identity give, on every integer index,

    ||psi||_infinity <= C p(k)p(l),
    |psi(x)-psi(y)| <= C a p(k)p(l) |x-y|_1.             (4)

The fixed polynomial p may be enlarged as in L111/L113; its full heat
sum remains uniformly finite. Both coefficient levels in (4) are kept.
The displacement has uniformly bounded supremum by L111. Scalar
multiplication commutes exactly with zero extension or restriction on
the same component grid. In particular,

    M^2_(psi,finite) J_2^* = J_2^* M^2_(psi,infinite).    (5)

Define the finite rectangular operator

    Y = M^1_psi S_beta X
          - S_beta J_2^* A_r E_j M^2_(b psi) J_2.         (6)

It maps finite plaquettes to finite edges. Let

    B_beta = M^1_psi S_beta-S_beta M^2_psi.

In B_beta both multipliers are finite. In the following brackets they
are infinite-grid plaquette multipliers. Using (5), adding and
subtracting S_beta J_2^* M^2_psi A_r E_j M^2_b J_2, and using the
commutativity of two scalar multipliers on that grid gives exactly

    Y = B_beta X
       + S_beta J_2^* ([M^2_psi,A_r] E_j
                           + A_r [M^2_psi,E_j]) M^2_b J_2.       (7)

The E_j operator is bounded by L110's full symbol estimate, and the
clamped scalar is bounded, so the infinite commutators in (7) are
well-defined bounded operators. Every extension and restriction stays
where it appears in (7). This identity neither replaces a finite
path map by its full-grid version nor assumes that X has compact
output. No projection occurs inside its commutators.

### 2. Bound the finite rectangular error with the joint kernel

Let W_j and Q_j be the unweighted and first quadratic spatial kernel
norms of L111(8) and L110(2), respectively. Those full-spectrum results
state

    W_j <= C(1+|j|)^(-5/2),
    Q_j <= C(1+|j|)^(-3/2),
    sum_(j in Z)(W_j+Q_j) < infinity.                    (8)

A nonzero entry of S_beta connects indices separated by a fixed
stencil range. By (4), its contribution to B_beta has coefficient at
most C a p(k)p(l). Its row and column multiplicities are bounded,
including at retained end rows. The finite matrix Schur bound gives

    ||B_beta|| <= C a p(k)p(l).                          (9)

For clarity, the Schur bound used here is
||B|| <= (sup_x sum_y |B_xy| sup_y sum_x |B_xy|)^(1/2).
No smoothness of zero-extended fields is involved.

Each row of the convolution A_r E_j has l2 norm at most C W_j,
because A_r is a fixed finite sum of component selectors and shifts.
There are at most C N^3 output rows after J_2^*. Bounded input
multiplication by b and input restriction preserve the resulting
bound:

    ||X||_HS <= C N^(3/2) W_j.                          (10)

Thus the first term of (7) is at most
C a p(k)p(l) N^(3/2) W_j in Hilbert--Schmidt norm.

For the second term of (7), expand A_r into its finite shifts. An
entry of [M^2_psi,A_r] contains a difference psi(x)-psi(x+h) with h
in a fixed finite list. Its absolute value is at most
C a p(k)p(l). Each resulting shifted component row of E_j has l2
norm at most W_j. Counting the O(N^3) rows selected by J_2^*, and
then using bounded S_beta, M_b and J_2, gives

    ||S_beta J_2^* [M^2_psi,A_r] E_j M^2_b J_2||_HS
                       <= C a p(k)p(l) N^(3/2) W_j.     (11)

Finally, the finite range of A_r means that J_2^* A_r only samples
rows of [M^2_psi,E_j] in a fixed enlargement Lambda_N of the finite
plaquette indices. This set has at most C N^3 indices, whether or
not they lie in the displacement support. On those rows the exact
commutator kernel is

    (psi(x)-psi(y)) e_j(x-y), x in Lambda_N, y in Z^3.

Equation (4) and L110's quadratic moment, with equivalence of l1
and Euclidean distance in dimension three, yield

    ||R_Lambda [M^2_psi,E_j]||_HS
                         <= C a p(k)p(l) N^(3/2) Q_j.   (12)

Both circulation factors remain inside e_j. Multiplication by the
bounded finite stencils and b, and input restriction by J_2, give
the same bound for the last term of (7). In particular (12) includes
all infinite input rows before restriction, and thus every boundary
input row afterwards. Combining (9)--(12) proves

    ||Y||_HS <= C a p(k)p(l) N^(3/2)(W_j+Q_j).           (13)

This uses the already proved quadratic kernel norm, not a first
absolute moment of either projected alternating factor. The latter
shortcut is ruled out by L109 and is not needed here.

### 3. Insert the error in the exact trace and sum every level and mode

L113's a^2 in Z and L111's outside a^-1 give the outside a in (2).
L114's definition of R_bulk,sc,Pbulk and cyclicity of finite rectangular
traces give exactly

    R_bulk,sc,Pbulk
      = a sum_(k,l,s,t,alpha,beta,r) c_(i;kl,a) min(s,t)
          Tr_edge[P_bulk M^1_psi S_beta X_(r;t,t-s) S_alpha^T]. (14)

Subtract (2) from (14); each trace difference is
Tr_edge[P_bulk Y S_alpha^T]. The relative edge space has at most
C N^3 rows, ||P_bulk||<=1, and ||S_alpha||<=C. Therefore

    ||S_alpha^T P_bulk||_HS <= C N^(3/2).

For finite rectangular matrices, the Hilbert--Schmidt Cauchy--Schwarz
inequality for the trace of a product, together with (13), gives

    |Tr_edge[P_bulk Y S_alpha^T]|
                    <= C a p(k)p(l) N^3 (W_(t-s)+Q_(t-s)).       (15)

The path and generator label lists have fixed finite length. For
each fixed t the sum over s is bounded by the complete offset sum
in (8). Keeping the original weight and using min(s,t)<=N,

    sum_(s,t=1)^(N-1) min(s,t)(W_(t-s)+Q_(t-s)) <= C N^2. (16)

L111/L113 provide sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i for both actual
probes. Equations (15)--(16), with the outside a in (14), prove

    |R_bulk,sc,Pbulk-R_prod| <= C_i a^2 N^5
                             =64 C_i N^3,

which is (3). Absolute majorization by the complete heat sum justifies
the regroupings if the heat expansion is written as an infinite series;
at finite mesh its original spectral sum is finite. Both generator
orientations already present in the imported trace are retained.
The complete other/other outside factor 3 is not applied again.

### 4. Scope and downstream use

The factors b_(r,t), phi_(l,alpha,s) and phi_(k,beta,t) have been
collected on one side of the joint covariance. Their product is compact
in transverse space through b. This is a statement about the input
multiplier in (2), not about the output support of A_r E_j. The finite
compressions J_1 inside P_bulk and J_2 next to E_j still prevent simply
substituting a full-grid diagonal symbol. Controlling those compressions
is a separate obligation before any frozen cancellation can be used.
Different path labels and the two axial levels have not been equated.

L111 moved the generator's coefficient in a different original order;
L113 combined exterior scalars across the finite projection; L114
controlled the projection's boundary comparison. None supplied (7)
for the remaining product. The specialization above is necessary to
verify this exact placement with all those restrictions retained.
The proof imports their kernel estimates and finite reductions and
uses standard finite-stencil and Hilbert--Schmidt inequalities. This
is local standard-method progress, RESEARCH / REPRODUCTION under the
unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`,
without a novelty claim beyond the sources checked. No general Ward
or flow finiteness theorem is used for this isolated bare action group.
No numerical comparison is made; any later use of D_i retains
L084/L082's numerical qualifications.

## Mathlib

Full matching exterior-product energy-placement theorem: **not checked**.
Supporting Schur bounds, finite rectangular trace cyclicity,
Hilbert--Schmidt Cauchy--Schwarz and Fourier kernel identities:
**not checked**. Unknown availability is not absence. The full energy
moment is imported from L110/L111 rather than rederived.
