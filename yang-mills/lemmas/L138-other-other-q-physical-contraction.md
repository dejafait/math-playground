# L138 — Positive Q subtraction from three already enclosed physical heat forms

## Hypotheses

Import L097(5)'s established continuum functional K_(i,Q), not a new
finite-mesh limit. The scope is SU(2), both actual L010 probes i=3,6,
the straight lower-rooted direction-1 forest, all-face relative fixed
links on D=(-4,4)^4, tau=1/16, and the bare small-coupling coefficient
at fixed mesh before refinement. Retain every relative exterior mode,
both displacement sectors, all plane paths and clover factors, the
physical lower prefix including its constant axial mode, and both
inverse weights. No outside group/color factor 3 is included here.

Use precisely L097's d, eta, lambda, P, S, z_v and
m_T=W_T+C_T S_6,T C_T. Write a,b,c for distinct transverse indices
in {2,3,4}, ell=x_1+4, V_k=v_k, and c_(i;kl) for its real symmetric
heat coefficients. Import L134(5)'s exact path identity and L008(6)'s
shear polarization. P_(i,D), P_(i,X), P_(i,A) denote exactly the
full physical heat forms in L132(1), with their complete spectral bounds.

For numerical conclusions only, import L133's full continuum intervals
for those three forms. These retain its certified-input and L039 IEEE
binary64 arithmetic model, underflow allowance and absence of formal
processor/BLAS verification. No new retained quadrature, midpoint
estimate or finite-mesh diagnostic is used as evidence.

## Conclusion

With normalized full-torus measure, define the universal scalar

    a_Q=4 integral eta_a^2 d_b^2/lambda,  a!=b.

Its value is independent of the distinct indices, and

    2/3<a_Q<1.

Then the complete established functional is exactly

    K_(i,Q)=a_Q P_(i,D)+(a_Q-1/6)P_(i,A)+P_(i,X)/12.       (1)

The shear constant in (1) is exact; the triplet scalar is bounded
analytically, not numerically evaluated. The full actual-probe values
obey the strict bounds, with L133's numerical qualifications,

    13590<K_(3,Q)<20768,
     2971<K_(6,Q)<4137.                                  (2)

Thus both Q values are positive. Their contribution in L124 is
**minus** K_(i,Q); the complete other/other coefficient has an additional
outside factor 3 applied once. Positivity of Q is not positivity of a
reflection norm or a sign of the complete cubic comparison.

Let K_(i,Q)^[K] be the right side of (1) with exactly L132's rectangular
cutoff forms, including both labels and the constant prefix. If
H(K),N_i have L132's definitions, then

    |K_(i,Q)-K_(i,Q)^[K]|<=154021014 N_i H(K).              (3)

At K=96 this error is strictly below 6*10^-12 for both probes.
This is a spectral omission bound only; (2) instead uses L133's
already enclosed full forms. No new weight or moment domain is needed.

ax,G,R and the triplet transverse-H sign remain unevaluated, so neither
K_(i,oo)+4 gamma D_i nor compensation with -12 gamma D_i is determined.
Other response jets, finer powers/logarithm, finite matching, interacting
error <=c_box/2, continuum field axioms, reflection positivity, infrared
control and finite positive mass remain unresolved. No candidate exists.
This is local standard-method REPRODUCTION, not a novelty claim or a
Yang--Mills resolution.

## Proof

### 1. Contract the projected paths without deleting the multiplier

Let Z have oriented plane rows -d_b e_a^T+d_a e_b^T and E=diag(eta).
Thus C=iZ, P=dd^T/lambda, S=ZZ^T/lambda. For lambda>0, L134(5)
gives exactly

    z_v d=f(v)=-2ZE v,
    z_v P=f(v)d^T/lambda,  S f(v)=f(v).

The last identity uses Z^T Z=lambda I-dd^T and Zd=0. Consequently
the full L097 integrand, with its original matrix order, is

    Tr[P z_v^* S m_T S z_h P]=f(v)^T m_T f(h)/lambda.      (4)

Here v,h are real physical columns at the same x; d^T d=lambda gives
the denominator in (4). The imaginary path terms cancel in z_v d,
rather than being discarded from an unprojected symbol. Both clovers
in m_T remain. All expressions below are bounded on the torus for
fixed strains and v,h, since |f(v)|<=2 sqrt(lambda)|v|. The scalar
integrands are also bounded. Setting their value arbitrarily at the
single lambda=0 point changes no integral; continuity there is not
asserted for a_Q. Absolute integrability justifies the parity operations.

### 2. Full triplet contraction and its one universal scalar

The oriented plane row is

    f_(ab)(v)=-2(d_a eta_b v_b-d_b eta_a v_a).

Insert the diagonal W_T entries w_a+w_b into (4). Every off-diagonal
physical entry has a factor d_a d_b for distinct indices, times a
function even in each angle, so its integral is zero by reflection
of angle a. The surviving diagonal terms are

    integral sum_a [4 eta_a^2/lambda
                    sum_(b!=a) d_b^2(w_a+w_b)] v_a h_a.

Permuting the entire torus shows that each distinct-index coefficient
is a_Q. Since sum_(b!=a)(w_a+w_b)=w_a+div_T u, the integrated
triplet expression is

    a_Q sum_a (w_a+div_T u)v_a h_a.                       (5)

No divergence-free condition for V is used in (5). Inserting ell and
summing the original c_(i;kl) gives a_Q(P_(i,A)+P_(i,D)).

To bound a_Q, set X=d_a^2,Y=d_b^2,Z=d_c^2,L=X+Y+Z and
I=integral XY/L. Each independent angle has integral X=2 and
eta_a^2=1-X/4. Permutation symmetry gives integral Y/L=1/3,
so

    a_Q=4/3-I.

Since L<12 and XY>0 almost everywhere, I>integral XY/12=1/3.
On the other hand X^2+Y^2+Z^2>=L^2/3, strictly off X=Y=Z.
After division by L and integration, symmetry gives
integral X^2/L>2/3. Also integral X^2/L+2I=integral X=2.
It follows that I<2/3 and therefore 2/3<a_Q<1. These bounds cover
the complete torus; no singular-angle cutoff or numerical integral
enters the argument.

### 3. Both clovers, the exact shear constant and polarization

For a<b, only alpha=c contributes to the transverse restriction of
L008's shear form. By antisymmetric extension this contribution is
s_ab F_ac F_bc, regardless of the positions of c in the ordered plane
list. Its symmetric bilinear polarization has the factor 1/2 from
L008(6). The clovered row in (4) is, for any distinct a,c,

    g_ac(v)=eta_a eta_c f_ac(v)
           =-2 eta_a eta_c(d_a eta_c v_c-d_c eta_a v_a).

Expand [g_ac(v)g_bc(h)+g_ac(h)g_bc(v)]/(2 lambda).
Every term except the v_a h_b and v_b h_a terms contains d_a d_b,
d_a d_c or d_b d_c and integrates to zero by separate-angle parity.
The complete surviving expression is

    [4 eta_a^2 eta_b^2 eta_c^2 d_c^2/lambda]
                                     (v_a h_b+v_b h_a)/2.

For J_c=integral eta_a^2 eta_b^2 eta_c^2 d_c^2/lambda,
coordinate permutation makes J_c independent of c, and

    3J_c=integral product_j eta_j^2=(1/2)^3=1/8.

Thus J_c=1/24, and the integrated shear is exactly

    (1/12)sum_(a<b) s_ab(v_a h_b+v_b h_a).                (6)

In particular the coefficient in the quadratic expression v=h is
1/6; each polarized matrix entry in (6) has coefficient 1/12.
This keeps both off-diagonal polarization orders.

Expand L132's P_(i,X) before any integration by parts. Its diagonal
entries contribute 2P_(i,A). For a<b the two ordered derivative
entries combine to s_ab(V_(l,a)V_(k,b)+V_(l,b)V_(k,a)). Therefore
ell times (6), summed against the same symmetric c, is exactly
(P_(i,X)-2P_(i,A))/12. Combining with (5) proves (1).

The calculation can first be made on each finite rectangular exterior
cutoff. L132's mode amplitudes, bounded form coefficients and complete
Gaussian heat sum dominate all three physical forms absolutely.
They justify the full-mode passage and equality with L097's absolutely
convergent series. No finite-mesh coefficient is refrozen here.

### 4. Reuse the full heat enclosures and their exact scope

Equation (1) uses exactly the existing three L132 forms. Their weights
are ell*div_T u, ell*w_a and ell*partial_m u_rho; both probe sectors,
the lower prefix, constant mode, two inverse weights and tensor
normalizations coincide. Hence L133's full intervals apply unchanged.
No cumulative weight, new axial moment, numerical table substitution
or transfer of a different coefficient's tail is involved.

Write (1) as a_Q(P_D+P_A)-P_A/6+P_X/12. L133's intervals give

    21529.1<P_(3,D)+P_(3,A)<21529.3,
    -3492.3<P_(6,D)+P_(6,A)<-3492.1.

Using 2/3<a_Q<1 and the remaining signed intervals, exact endpoint
arithmetic encloses the values within

    271819/20<K_(3,Q)<498421/24,
    11887/4<K_(6,Q)<496321/120.

The first interval is contained strictly in (13590,20768), the second
strictly in (2971,4137). This proves (2), conditionally on precisely
L133's stated numerical inclusion model. Using a shared a_Q in the
rewritten formula respects the dependence between its two occurrences.
The minus sign in L124(1) is unchanged.

For (3), L132 gives C_D=C_A=20582100 and C_X=1395445968.
The coefficient bounds in (1) are |a_Q|<1,
|a_Q-1/6|<5/6 and 1/12, so the triangle inequality gives

    C_Q=C_D+(5/6)C_A+C_X/12=154021014.

At K=96 L132's proved bound H(96)<2717908992/20^27 and
N_i<=1640736 imply

    C_Q*1640736*2717908992/20^27<6*10^-12.

This reuses the spectral bound only after identifying the exact forms;
the retained errors and full-tail intervals in (2) are already covered
by L133.

### 5. Complete exact algebra checks

Reproduce from the active notebook:

    python3 scripts/combined-ward-response/check_q_physical_reduction.py

The script saves all 72 polynomial comparisons, before-parity
numerators, exact differences, shear averages, full-tail arithmetic
and endpoint records in
`scripts/combined-ward-response/q-physical-reduction-certificate.json`.
It constructs each b*d and q*d directly from L097's real/imaginary
paths, then checks all three physical columns in every plane. It
checks all nine physical matrix entries for each of the three triplet
strain coefficients and each of the three oriented transverse shears.
The parity selector retains every monomial whose d exponents are
even; eta is even under angle reflection. Antisymmetric plane signs
and both shear polarization orders are explicit. All 72 exact checks,
the 1/6 quadratic and 1/12 matrix constants, the full-tail comparison
(approximately 5.118*10^-12 upper rounding for reporting), and both
strict endpoint tests pass, with no failures. The certificate uses
rational/integer arithmetic for these algebraic checks; the analytic
integration and inequalities are proved above. It does not independently
reverify L133's processor model or its physical integrals.

The standard symmetry and finite-matrix methods specialize imported
L097/L134 expressions; no new general Ward/flow theorem or source-based
finiteness assumption is invoked. The unchanged ready assessment is
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.

## Mathlib

Full matching actual-probe Q contraction and enclosure: **not checked**.
Supporting finite-matrix trace, parity/change of variables, symmetric
polarization, product integration and dominated-convergence coverage:
**not checked**. Unknown availability is not evidence of absence.
