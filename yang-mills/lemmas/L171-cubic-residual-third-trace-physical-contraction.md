# L171 — Third trace reduces to the R physical form and one universal scalar

## Hypotheses

Keep all L170 hypotheses: SU(2), D=(-4,4)^4 with all-face relative
fixed-link conditions, a=8/N through admitted even meshes, straight
direction-1 lower-rooted forest, L008's complete compact displacement,
both actual L010 probes at tau=1/16, and the bare fixed-mesh expansion
before refinement. Import L170's established cubic limit K_(i,Z), with
its complete frozen force/vector tensor, exact P^0 B_E F^- M^0 order,
actual lower half-line and coefficient -6. Its two insertion
subtractions and upper action contributions have been estimated before
removal. No new mesh limit is taken here.

Use L170's c_(i;kl), V_k and V_l and L145's absolutely convergent form

    B_(i,R)=sum_(k,l)c_(i;kl) integral_D u_1 V_k dot V_l dx.

H,E below are spatially constant transverse exterior vectors, with
H_1=E_1=0. Rough link slots still run through all four directions and
all three colors. Put t_c=i sigma_c/2 and J_c v=[t_c,v].

## Conclusion

With normalized measure on T^3, set

    X_j=4 sin^2(theta_j/2), j=2,3,4,
    lambda=X_2+X_3+X_4, S_m=sum_(j=2)^4 X_j^m,
    n=lambda(5 S_2-3 lambda^2)/36
          +(3 lambda S_3+S_2^2-4 S_4
                               +4 lambda X_2 X_3 X_4)/144,
    z_Z=18 integral_(T^3) n/lambda^2.                    (1)

The integrand is extended by zero at the origin. It is bounded and
absolutely integrable. The exact reduction for both probes is

    Xi(u,H,E)=-(z_Z/6) u_1 H dot E,
    K_(i,Z)=z_Z B_(i,R),             i=3,6.              (2)

The universal scalar's value, sign and possible vanishing remain
unevaluated. In particular z_Z is not assigned L145's different scalar
g_G. Once z_Z is controlled, L146's already enclosed physical form can
be reused through the exact match (2). This establishes a coefficient
reduction, not zero or nonzero response. Both mixed branches still lack
scaled limits; the complete response's cubic limit and vanishing, other
jets, full compensation, finer powers/logarithm, finite matching,
interacting error <=c_box/2 and continuum/infrared requirements remain
open. This is local standard-method REPRODUCTION, without a novelty
or candidate-solution claim.

## Proof

### 1. Full force/vector axial row

Use component-center phases and put d_j=2 sin(theta_j/2),
eta_j=cos(theta_j/2), so X_j=d_j^2. Write the color block of
M^0(u,H,c) as m_(mu nu) J_c. This follows from L155's alternating
degree-three color tensor; for c=1 in one-based color notation,
J_1[2,3]=1. L170 defines the full symmetric combined-index tensor by
the third derivative divided by 6. At theta_1=0 its axial row is

    m_(11)=0,
    m_(1 nu)=u_1 [
       H_nu eta_nu/24 sum_(b != nu) X_b(X_b-3X_nu)
       +sum_(h != nu) H_h eta_h d_h d_nu(2X_h-X_nu)/12 ],
                                            nu=2,3,4. (3)

There is no u_2,u_3,u_4 contribution to this row. Crucially, (3) is
computed with axial rough inputs restored. Setting axial link variables
to their forest values before polarization would give the wrong row.

Here are the full finite-expansion specification and verification of
(3). For each positive force link (z,mu), both generator endpoints,
and rho != mu, expand G_(mu,1) X_(mu,2)+G_(mu,2) X_(mu,1) by
L149(4)--(6). The generator has spacing 1 and endpoint coefficient
1/2. Collect cyclic trace words of length three with coefficient
-2 times the force and generator coefficients. No direction is
omitted. In each word choose, in all six ways, an exterior slot of
color 1 and direction h != 1, an axial rough slot of color 2, and
the remaining rough slot of color 3 and direction nu. Since

    Tr(t_a t_b t_c)=epsilon_(abc)/4,

the word coefficient contributes epsilon/24 to the polarized matrix
entry, after multiplying by the collected trace coefficient. Translate
the axial slot to tail 0; if the other slot has displacement delta,
its raw-tail symbol is exp(i theta dot delta). This finite prescription
is exactly L170(4), including its 1/6 and all positive force edges.
It includes the exponential-coordinate correction through the full
left-frame force identity, rather than through X_2 alone.

At theta_1=0, let e_j=exp(i theta_j). For u_1 H_h the raw axial row
has the following two entries, with b ranging over transverse indices:

    R_(hh)=(e_h^-2+e_h)/16 sum_(b != h)(2-e_b-e_b^-1)
        +(1+e_h^-1)/48
                    sum_(b != h)(e_b^2+e_b^-2-e_b-e_b^-1),
    R_(h nu)=(e_h^-2-e_h^2)(e_nu^-1-1)/12
        +(e_h^-1-e_h)
                       (-e_nu^-2-e_nu^-1+1+e_nu)/24,
                                         nu != h.      (4)

The entries for other displacement components, and the axial/axial
entry, are zero. These are complete Laurent identities, rather than
pointwise tests. Multiplying R_(h nu) by exp(i theta_nu/2) changes to
component-center phases. In the diagonal entry use
cos(3 theta_h/2)=eta_h(1-X_h) and
e_b^2+e_b^-2-e_b-e_b^-1=X_b^2-3X_b. This gives the diagonal part
of (3). For the other entry use

    exp(i theta_nu/2)(e_nu^-1-1)=-i d_nu,
    exp(i theta_nu/2)(-e_nu^-2-e_nu^-1+1+e_nu)
                                      =4i sin(theta_nu)eta_nu.

It gives eta_h d_h d_nu(2X_h-X_nu)/12, proving the remaining part.

The exact finite calculation is reproducible with

    python3 scripts/combined-ward-response/contract_third_trace_frozen.py

Its full certificate is
`scripts/combined-ward-response/third-trace-frozen-contraction-certificate.json`.
The code enumerates the finite compositions of word degree, retains
all link directions and repeated variables, and performs the extraction
just specified using exact rational arithmetic. It saves all 792
nonzero full axial-row coefficients and all zero-axial-frequency rows.
All 48 displacement/exterior/output coefficient comparisons with (3)
have zero exact discrepancy, including zero rows. A separate SU(2)
matrix-series convolution checks every force-direction/displacement/
endpoint case on two full-color packets (48 comparisons, zero error).
Those packet comparisons check implementation; the exhaustive Laurent
coefficient comparison establishes the finite identity. No packet or
numerical sample is substituted for the actual probes.

### 2. Actual prefix, parity and color normalization

L164(10)'s complete frozen reflection identity, summed over force
edges, makes the component-centered M^0 real and even under simultaneous
angle reversal. Its value at zero is zero: on an entirely constant
link field G_1=X_1=0, so the cubic Q^0 is zero for every constant
color field, and its polarization gives M^0(0)=0. Analyticity of
the finite stencil and evenness consequently imply

    ||M^0(theta)||<=C|u||H| lambda_4(theta),
    lambda_4=sum_(j=1)^4 d_j^2.                         (5)

The co-closed projection P^0 and centered endpoint row
2 eta_nu E_nu J_c are real and even. Hence the closed scalar/color
factor in P^0 B_E M^0/lambda_4 is real, even and bounded. Its
possible singularity at the origin is controlled by (5).

Damp L170's actual prefix summand j by rho^j, 0<rho<1. In these
phases the prefix multiplier is exactly L169(10),

    p_rho=exp(-i theta_1/2)/(1-rho exp(-i theta_1)).

For fixed rho the row F_rho has square-integrable symbol p_rho/lambda_4
after pairing with M^0: (5) makes their product bounded. Fourier
diagonal pairing with the bounded projection/endpoint symbol is thus
legitimate. Equivalently both paired symbols are in L2 on the compact
torus; no L2 claim for the undifferenced Green kernel is made.
L170(7)--(8)'s absolutely summable complete kernel product dominates
the damped prefix uniformly: the scalar Green is nonnegative and
rho^j<=1. Dominated convergence therefore returns the actual undamped
kernel density as rho increases to 1.

The imaginary part of p_rho integrates to zero by simultaneous
inversion. Its real part is L169(11)'s positive approximate identity,
with normalized mass tending to 1/2. At each nonzero transverse angle
the remaining bounded factor is continuous at theta_1=0. Bound (5)
and dominated convergence also give continuity of its transverse
integral there. The approximate identity therefore selects half the
zero-axial-frequency contraction. This retains the actual half-line's
endpoint contribution, rather than keeping only odd principal-value
parity.

At theta_1=0, P^0 has transverse block delta_(nu j)-d_nu d_j/lambda.
F^- selects only the axial row of M^0. With sum_c Tr(J_c^2)=-6,
the prefix half-weight and endpoint factor 2 give

    Xi=-6 integral_(T^3) sum_(nu,j)
           m_(1 nu)(delta_(nu j)-d_nu d_j/lambda)
                                      eta_j E_j/lambda. (6)

Here m includes u,H but no color factor. The coefficient -6 in (6)
is the color trace times the prefix and endpoint factors; the separate
outside -6 defining K_(i,Z) in L170 has not yet been applied.

### 3. Project first, then reduce the physical tensor

For a fixed H_h, (3) makes m_(1h) even in each transverse angle,
while m_(1nu), nu != h, contains d_h d_nu times an even function.
The projected row has the same parity. Multiplication by eta_j E_j
therefore makes its integral zero for h != j, by reflecting theta_h
or theta_j. For h=j all three integrals are equal by transverse
coordinate permutation. The u_T rows already vanish in (3).

For u_1 H_j=1, (3) gives explicitly

    sum_nu m_(1nu)d_nu
                 =eta_j d_j/24 sum_(b != j) X_b(X_j-X_b).

Define the numerator with the full endpoint factor 2 by

    n_j=2 eta_j [lambda m_(1j)-d_j sum_nu m_(1nu)d_nu]
       =(1-X_j/4)/12 sum_(b != j)
          X_b[(lambda+X_j)X_b-X_j(3lambda+X_j)].         (7)

Thus the integrated contraction in (6) is half the integral of
n_j/lambda^2, multiplied by u_1 H_j E_j. Average (7) over the three
j. Expanding this finite polynomial gives

    (1/3)sum_j n_j
       =lambda(5 S_2-3lambda^2)/36
          +(3lambda S_3+S_2^2-4S_4
                              +4lambda X_2 X_3 X_4)/144=n. (8)

The complete 22-coefficient polynomial identity (8), including its
reconstruction as the 123-coefficient symmetrized raw Laurent
numerator, is checked exactly in the saved certificate. For a manual
expansion, its degree-three coefficients are 1/18 on each X_j^3,
-1/9 on each X_j^2 X_b, j != b, and -1/2 on X_2 X_3 X_4.
Its degree-four coefficients are 1/48 on each X_j^3 X_b,
1/72 on each X_j^2 X_b^2, j<b, and 1/36 on each X_j^2 X_b X_c
with j,b,c distinct. These exhaust the polynomial.

Equations (6)--(8) now give

    Xi=-3 [integral n/lambda^2] u_1 H dot E.

Every X_j lies in [0,4], S_m<=lambda^m for m>=1, and
X_2 X_3 X_4<=lambda^3. Consequently n=O(lambda^3)+O(lambda^4);
n/lambda^2 tends to zero at the origin and is bounded on the torus.
This also justifies every transverse reflection and permutation above.
Multiply by L170's outside -6 exactly once to obtain z_Z=18 integral
n/lambda^2 and restore the physical integral and full heat coefficients.
L170's absolute convergence permits this substitution term by term.
The physical form is exactly B_(i,R), proving (1)--(2).

The torus numerator has both signs; no pointwise positivity or value
has been established. A finite exact coefficient extraction is not a
torus enclosure, and neither z_Z nor the complete response is evaluated.

## Mathlib

Full matching theorem and supporting lattice-prefix coverage:
**not checked**; unknown is not absence. Reuse the unchanged ready
assessment `drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
No new external theorem is imported or reproved. L149/L155 give the
finite word and tensor conventions, L164 the full frozen inversion,
L170 the established absolutely convergent limit and exact order,
L169 the actual prefix/approximate-identity argument, and L145 the
matching physical form. The specialized finite row is computed here
because the simpler action row and older forest-restricted quartic
words do not cover its axial rough slots. Fourier pairing, dominated
convergence and finite polynomial algebra have their hypotheses and
normalizations explicitly checked above.
