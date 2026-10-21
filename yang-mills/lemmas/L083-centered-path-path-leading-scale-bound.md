# L083 — The centered path/path term is subleading at the a^-3 scale

## Hypotheses

Keep L074 section 5's complete direct centered path/path term for both
L010 probes i=3,6, SU(2), the straight lower-rooted forest, the relative
fixed-link box (-4,4)^4, admitted even N, a=8/N, and tau=1/16. The
small-coupling coefficient is taken at fixed mesh before refinement.
All coordinates and matrix norms below are ordinary dimensionless ones.
Retain every pinned row, transverse plane, axial level 1<=s<N, and
exterior heat index k,l. In exactly L074's notation set

    W_X=sqrt(N) G E_0^T A_0 I_T Sigma_T, H_X=G S^T,
    Lambda_l=bar B_3^T M_(t_l,1) bar B_2
                          -bar B_2^T M_(t_l,1) bar B_3,
    bar P_i=sum_(k,l)c_(i;kl) sqrt(N)
        Tr[G C_(r_k) G E_0^T A_0 I_T Sigma_T Lambda_l S].  (1)

Use the actual A_0=(L_0 K_a+K_a^T L_0)/2-Q_3-Q_6 and L078's
full relative Hodge covariance Sigma=Delta^-1, where
Delta=L_0+D_0 D_0^T and L_0=D_1^T D_1. In particular I_T inserts
transverse components and E_0 inserts the normalized constant axial
edge mode in component 1. No co-closedness of Lambda_l S is assumed.

For the signed comparison only, import L079–L080's circulation/path
limit and L082's enclosures with their stated IEEE arithmetic and
saved-table qualifications. The bound on (1) itself is analytic and
does not use those numerical assumptions.

## Conclusion

For both actual probes,

    |bar P_i| <= C_i N^2,       lim_(a->0) a^3 bar P_i=0.  (2)

Consequently the complete direct first pair in L074 satisfies

    lim_(a->0) a^3 F_i^dir = 2 gamma D_i < 0,             (3)

where gamma>0 is exactly L070(3)'s full-torus constant and D_i is
exactly L080's diagnostic. Thus the path/path limit 0 is unequal to
the required cancellation value -2 gamma D_i>0 for each probe. L082
gives D_3 in (-237.289643,-237.289642) and D_6 in
(-98.877430,-98.877429), with its qualifications retained.

This is the normalization of L064's first line, without a factor 6.
No coefficient is assigned to the full mixed response. The O(N^2)
bound does not give a path/path a^2 limit; L079 still has only an
o(N^3) leading-comparison error. Other placements, response jets,
the complete logarithm and interacting matching remain unresolved.
This is local REPRODUCTION using the ready SPECIALIZE assessment,
not a claim of mathematical novelty or a Yang–Mills candidate.

## Proof

### 1. Retain the full Hodge projection on an arbitrary path source

Since D_1 D_0=0, L_0(D_0 D_0^T)=(D_0 D_0^T)L_0=0.
Thus L_0 commutes with Delta and L_0^2=L_0 Delta. As Delta is
positive definite in the relative box, the finite matrix

    Pi=L_0 Sigma

is symmetric and Pi^2=L_0^2 Delta^-2=Pi. Hence ||Pi||<=1.
This is the finite orthogonal-projection identity, on the complete
relative complex including end rows, not a claim Pi I_T Z=I_T Z
for an arbitrary transverse source Z.

The full Hodge matrix is component diagonal. L075's complete axial
Dirichlet inverse gives Sigma I_T=I_T Sigma_T. Therefore, exactly,

    L_0 I_T Sigma_T=Pi I_T.                              (4)

Unlike L078's equality on its co-closed circulation source, (4) retains
Pi, including its component-1 output and all physical-boundary effects.
It is valid before applying Lambda_l S. No variable multiplier passes
through a covariance, residual or projection. No axial inverse is
replaced by its bulk-distance profile.

### 2. Use the curvature estimate before taking the trace norm

L009(16) states ||K_a A||_a<=C||d_a A||_a for the actual clover and
endpoint averages with bounded compact displacement. Passing to
ordinary coordinates cancels the common a^4 inner-product weight;
d_a=D_1/a. Scaling the link variable by a also cancels on both sides.
Thus the same generator in A_0 obeys, for every full link vector x,

    ||K_a x|| <= C a^-1 ||D_1 x||.                       (5)

This includes every output component. It uses the original bounded
coefficient multiplication in the generator, not a constant-coefficient
replacement or a derivative bound on rough input fields.

L078(5) gives E_0^T L_0 E_0=G^-1. Apply (5) to every column of
E_0 G and sum squares. With G symmetric,

    ||K_a E_0 G||_HS^2
       <= C a^-2 Tr[G E_0^T L_0 E_0 G]
        = C a^-2 Tr G.                                  (6)

Split W_X=W_X^lead+W_X^rem using
A_0=K_a^T L_0/2+A_rem, with A_rem=L_0 K_a/2-Q_3-Q_6.
Equation (4), without deleting Pi, gives

    W_X^lead=(sqrt(N)/2)(K_a E_0 G)^T Pi I_T,
    ||W_X^lead||_HS <= C sqrt(N) a^-1 sqrt(Tr G).         (7)

The three-dimensional pinned spectrum has Tr G<=C N^3, as proved
by the full shell sum in L078 section 4. Since a=8/N, (7) is O(N^3).
In particular no co-closed path identity is needed to gain this power.

### 3. Keep the reverse placement and both curvature subtractions

L078(15), proved with pinned axial summation by parts and the actual
curvature forms, supplies

    R_rem=G^(1/2) E_0^T A_rem I_T Sigma_T^(1/2),
    ||R_rem||<=C.                                       (8)

Its proof is an operator estimate independent of the source Z_l;
only L078's separate leading-placement cancellation required a
co-closed column. Thus (8) applies to the present path source.
Retaining its order,

    W_X^rem=sqrt(N) G^(1/2) R_rem Sigma_T^(1/2).

The complete relative gap gives ||Sigma_T^(1/2)||<=C N.
This also follows directly from L075's tensor spectrum: the positive
axial Dirichlet eigenvalue alone is at least 4/N^2. Hence

    ||W_X^rem||_HS <= C sqrt(N) sqrt(Tr G) N <= C N^3.

Together with (7),

    ||W_X||_HS <= C N^3.                                (9)

The improved norm is for this left-weighted direct row. It does not
assert a bounded full whitened residual, in conflict with neither
L064's coarser estimate nor the transverse norm obstruction in L066.

### 4. Bound the complete ordered path/path trace and heat sum

The two-link centered paths have uniformly bounded norms: each uses
a fixed number of actual edge evaluations, and each edge occurs in
a bounded number of transverse plaquettes. Subtracting D/2 preserves
this property. Pinned zero rows and all axial levels do not increase
that multiplicity. Put

    bar W_b=W_X bar B_b^T, H_b=H_X bar B_b^T, b=2,3.

Equation (9) gives ||bar W_b||_HS<=C N^3. Also, with S_s=sT,

    ||S G||_HS^2=sum_(s=1)^(N-1) s^2 Tr[G T^T T G]
                =sum_s s^2 Tr G <= C N^6,

so ||H_b||_HS<=C N^3. Here T is the pinned transverse incidence;
its sign convention has no effect on T^T T=G^-1. Both estimates
already sum every level, end edge, and upper vertex.

The skew matrix C_r=E_v^T M_r T-T^T M_r E_v has
||C_r||<=C||r||_infinity, since endpoint evaluation and incidence
have bounded norms on these fixed-degree grids. L074 section 5's
exact finite scalar identity for (1), for a fixed exterior product, is

    bar P_kl=sum_p t_l,1(p) [bar W_2(p)^T C_(r_k) H_3(p)
                           -bar W_3(p)^T C_(r_k) H_2(p)].

Thus it includes both original upper endpoint placements. Matrix
Cauchy–Schwarz, with the t_l,1 multiplier kept in its column position,
gives

    |bar P_kl| <= C ||t_l,1||_infinity ||r_k||_infinity
                  (||bar W_2||_HS ||H_3||_HS
                   +||bar W_3||_HS ||H_2||_HS)
                <= C a^4 p(k)p(l) N^6
                 = C' N^2 p(k)p(l).                     (10)

The actual circulation and upper-curvature coefficient bounds are
L064(3), also retained in L074(5). Their complete heat majorant
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i proves (2). No external or internal
mode cutoff has been used. Since a^3 N^2=512/N, the scaled term
vanishes with this explicit order bound.

### 5. Compare in the original normalization and retain limitations

L074(9) is an exact identity F_i^dir=bar P_i+bar F_i^circ, not an
asymptotic replacement of the full first pair. By L079–L080,
a^3 bar F_i^circ tends to 2 gamma D_i. Combine with (2), L070's
gamma>0, and L082's qualified strict signs to obtain (3).
For both probes the cancellation target -2 gamma D_i is strictly
positive while the path/path coefficient is zero.

No extra color or placement factor is inserted; L064 states that the
factor 6 occurs only in assembling the complete response. The axial
prefix and other placements must be restored in any such assembly.
The projection estimate has not evaluated their coefficients here.
L074's O(N^2) centering defect, the path/path N^2 coefficient, and
L079's finer remainder remain. Subleading powers and logarithms are
not removed by (2). The shared quartic still must be subtracted once.
An interacting error <=c_box/2, limiting field axioms, reflection
positivity, infrared control and finite positive mass remain unproved.

The source assessment is
`drafts/literature/2026-10-08-centered-path-path-leading-scale.md`.
This proof specializes its permitted finite incidence/trace algebra
and the previously proved generator and residual estimates. It neither
reproves nor assigns this coefficient using the general flow/Ward
theorems compared there. No new numerical calculation is required.

## Mathlib

Full matching coverage of this specialized path/path estimate:
**not checked**. Supporting orthogonal-projection identities, finite
matrix Hilbert–Schmidt inequalities and incidence algebra: **not
checked**. No theorem-absence or formal-verification claim is made.
