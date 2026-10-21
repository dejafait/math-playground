# L163 — The first Hodge trace's upper action-column jump is subcubic

## Hypotheses

Keep L161's full-link SU(2) conventions on the relative cube (-4,4)^4,
a=8/N through sufficiently fine admitted even meshes, straight lower-rooted
direction-1 forest, complete compact displacement and both actual L010
probes at tau=1/16. Expand at fixed mesh before refinement. Use
Sigma, h_k=R v_k, c_(i;kl), and the colored symmetric matrices
M=T_R(h_k t_c,.,.), N=T_S(h_l t_c,.,.) of L161(2).
All matrix entries and transposes are in ordinary stored coordinates.
Both residual insertion subtractions and every action plaquette remain;
full tensors are formed before forest restriction. Hats denote the
three-color diagonal extensions.

Let J_top be the diagonal full-link selector of variable direction-1
edges with tail at axial level N-1, and set

    j_l=J_top h_l,       h_l^b=h_l-j_l,
    N_top=T_S(j_l t_c,.,.),       N_b=T_S(h_l^b t_c,.,.).    (1)

This is a split of the action's exterior column only, not a truncation
of either rough covariance, the action sum, or the residual column.
Define its contribution to L161(3)'s first trace by

    W_(i,top)=-36 sum_(k,l,c) c_(i;kl)
                        Tr(M Sigmahat N_top Sigmahat).    (2)

## Conclusion

For both actual probes, with constants independent of N,

    |W_(i,top)|<=C_i N^2,       a^3 W_(i,top)->0.          (3)

Consequently that first complete trace equals its version with N_b
in place of N plus O_i(N^2). This statement preserves the original
-36 coefficient and the complete exterior heat sum. No cubic bound
or scaled limit for the N_b trace, the other three unresolved ordered
traces, or the full E,E sector follows. L158–L159's mixed branches
still lack limits, and no complete-response vanishing or compensation
coefficient is established. Other jets, finer powers/logarithm, finite
matching, reflected error <=c_box/2, continuum axioms and infrared
finite mass remain unresolved. This is a local standard-method
specialization, not a claim of progress beyond the sources checked.

## Proof

### 1. The complete upper vertex forces two different rough components

L026's prefix identity makes h_l vanish on all direction-1 forest
edges, namely levels 0,...,N-2 at interior transverse vertices.
The remaining variable axial edges are exactly those selected by
J_top. L157(15), or directly the bound of N prefix samples of size
C a p(l) with Na=8, gives

    ||j_l||_infinity<=C p(l),                            (4)

for a fixed polynomial p. This includes the constant axial mode;
no O(a) estimate is used for j_l.

An action plaquette containing a selected edge is a (1,mu) plaquette
in the last axial layer. In its traversal order write its four link
variables as (x,z,-y,0), where x,y are the two positive normal axial
links, z is the positive transverse link at level N-1, and the zero
is the transverse link lying in the upper face. Possible additional
fixed links at transverse faces are also zero. Cyclic starting-point
or orientation choices can change this presentation without changing
the following component conclusion. L155(8)'s full action cubic on
this plaquette is exactly

    -(1/2) x dot (z cross (-y))=(1/2) x dot (z cross y). (5)

Because j_l has only axial components, inserting it into one slot
of the symmetric trilinear tensor of (5) leaves one normal axial
rough link and one transverse rough link at level N-1. Therefore

    (N_top)_(uv) != 0  implies that u,v have
    components (1,mu) or (mu,1), with mu in {2,3,4}.      (6)

They lie on the same upper plaquette. There is no normal/normal
entry. If another link is fixed, restriction of all three slots of
(5) removes that plaquette's cubic entirely; nothing is added at a
boundary strip. Thus the conclusion includes all action faces and
normal end edges.

There are O(N^3) upper plaquettes and a fixed number of tensor entries
per plaquette. Each entry receives only boundedly many placements.
Equations (4)–(5), including the fixed color dimension, yield

    #(nonzero entries of N_top)<=C N^3,
    |(N_top)_(uv)|<=C p(l).                            (7)

The full residual matrix has support in a fixed compact interior
region in each index. L161, proof section 3, bounds its entries using
the complete residual cubic and the actual interior exterior column:

    #(nonzero entries of M)<=C N^4,
    |M_(ab)|<=C p(k).                                  (8)

Both insertion subtractions are included in (8). Choose a fixed axial
separation delta>0 from that entire residual support to the top face,
including its finite stencil enlargement, for all sufficiently fine N.

### 2. Undifferenced relative Green columns have unequal boundary scales

We specialize the exact inverse columns in L041(7)–(8), rather than
use its circulation estimate for an undifferenced normal source.
For an observation link e in the residual support and a top-layer
source link f, the componentwise covariance of L026 satisfies

    |Sigma_(ef)|<=C_delta N^-2   if f is normal axial,
    |Sigma_(ef)|<=C_delta N^-3   if f is transverse
                                            at level N-1. (9)

Only equal components have nonzero covariance. Here is the full-mode
justification, including the distinct boundary conditions.

For component 1 the three transverse coordinates are Dirichlet
vertices, with normalized product modes psi_q and eigenvalue lambda_q.
For a transverse component mu, coordinate mu is an edge cosine
coordinate, including index zero, and the other two transverse
coordinates are Dirichlet vertices. In both cases
|psi_q(y) psi_q(y')|<=8 N^-3. Put

    lambda_q=4 sum_(j=2)^4 sin^2(pi q_j/(2N)),
    eta_q=2 asinh(sqrt(lambda_q)/2).

The allowed q have at least two positive indices. Uniformly over
all their values, c|q|/N<=eta_q<=C|q|/N, and N eta_q>=c>0.
These inequalities follow from the sine bounds in L026 and the
bounded range 0<lambda_q<=12. The exact axial last columns are

    R_E(r,N-1;lambda_q)
       =cosh((r+1/2)eta_q)
                       /[2 sinh(eta_q/2) sinh(N eta_q)],
    R_D(s,N-1;lambda_q)=sinh(s eta_q)/sinh(N eta_q).       (10)

L041 verifies their recurrences and unit source, with respectively
Neumann edge and Dirichlet vertex endpoints. The former includes
the constant axial edge mode. Since observations are separated from
the upper face, their absolute values are bounded by

    C N |q|^-1 exp(-c_delta |q|),
    C exp(-c_delta |q|),                                (11)

respectively. The half-step in the first numerator is retained; the
fixed separation bounds N-r-1/2 below by a positive multiple of N.
Multiply (11) by the two transverse mode values and sum. The sums
of |q|^-1 exp(-c_delta |q|) and exp(-c_delta |q|) over the allowed
three-dimensional integer orthants are finite. Extending the finite
mode set to these positive summable majorants proves (9) uniformly
in every source's transverse position. Cosine endpoint values satisfy
the same bound; fixed tangential rows are zero. No source boundary
collar or low frequency is removed. In particular the first bound is
N^-2, not the N^-3 estimate for a normal-source difference in L041.

### 3. Bound the signed trace in its original order

Expand one trace in (2) exactly as

    Tr(M Sigmahat N_top Sigmahat)
        =sum_(a,b,u,v) M_(ab) Sigmahat_(bu)
                                 (N_top)_(uv) Sigmahat_(va). (12)

For each nonzero N_top entry, (6) forces one covariance factor in
(12) to have a normal source and the other to have a transverse
source at level N-1. Both observation indices are in the compact
support of M. Component diagonality of Sigma (and color diagonality
of Sigmahat) either makes the product zero or lets (9) bound its
absolute value by C N^-5. Consequently (7)–(8) give

    |Tr(M Sigmahat N_top Sigmahat)|
         <=C p(k)p(l) N^4 N^3 N^-5
         =C p(k)p(l) N^2.                              (13)

This uses no positivity, multiplier commutation, frozen coefficient,
or approximation to either covariance. L156(8) gives uniform absolute
summability of sum_(k,l) |c_(i;kl)|p(k)p(l) for each actual probe.
Sum (13) over the entire spectrum and three exterior colors, retaining
-36 once, to obtain (3). Linearity of T_S gives N=N_b+N_top exactly,
which proves the stated replacement of the first trace only.

The extra Dirichlet factor in (9) is essential for this estimate.
Bounding both columns by N^-2 would yield only O(N^3) from the same
entry count. That weaker bound would not justify removing the jump.
The argument does not apply automatically to the other trace orders,
which retain F=Phi Sigma and gauge-identity operators.

### 4. Exact algebra checks and their limitations

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_hodge_upper_jump.py`.
The complete certificate is
`scripts/combined-ward-response/cubic-hodge-upper-jump-certificate.json`.
It checks the upper-plaquette cubic tensor by independent polarization
of (5), all possible rough component blocks for exterior normal
columns in all three colors, and additional fixed-link restrictions.
Rational masses separately check both full last-column recurrences
in (10), retaining their different endpoints. These finite checks
verify the algebra and the imported inverse specialization, not an
actual-probe value or an asymptotic estimate. All 486 polarization
entries, 18 additional fixed-link cases and 24 inverse-column cases
pass with maximum rational error zero and no failures. Equations
(9)–(13) and the full heat sum establish the all-mesh bound analytically.

## Mathlib

Full matching result: **not checked**. Supporting finite tensor
polarization, relative product spectra and Green recurrences: **not
checked**. Unknown coverage is not absence. Reuse the unchanged
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. L041's exact inverse
columns are specialized to separate undifferenced normal and tangential
sources because its previously contracted circulation bound cannot be
assigned to both of them. This distinction closes the upper-jump
error for this trace without assuming smoothness across the upper pin.
