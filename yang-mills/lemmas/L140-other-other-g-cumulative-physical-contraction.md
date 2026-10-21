# L140 — G is a negative scalar times an upper-cumulative physical heat form

## Hypotheses

Import exactly L104(1),(3)--(6)'s established K_(i,G), raw
tail-indexed symbols, cumulative h and physical V=v. Use SU(2), both
actual L010 probes i=3,6, the straight lower-rooted direction-1 forest,
D=(-4,4)^4 with all-face relative fixed links, tau=1/16, and the bare
small-coupling coefficient at fixed mesh before refinement. This
contracts an established continuum functional and takes no new mesh
limit. Retain every plane, both paths, both inverse weights, the
centered forward difference distinct from incidence, all real relative
exterior modes, both displacement sectors and the constant lower-prefix
mode. No outside factor 3 or additional color factor is included.

Use L080's f_k, lambda_k, A_k=f_k/sqrt(lambda_k), and
c_(i;kl)=exp[-(lambda_k+lambda_l)/16]q_i(A_k,A_l). Thus c is real
symmetric. All transverse indices below range over 2,3,4. Put
ell=x_1+4, F_(k,ab)=partial_a V_(k,b)-partial_b V_(k,a), and

    delta_(k,a)=sum_(b>a) partial_b F_(k,ab)
                              -sum_(b<a) partial_b F_(k,ba),
    h_(k,a)(x)=integral_(x_1)^4 delta_(k,a)(r,x_T) dr.

These are precisely L104's cumulative fields. Import L132's full-probe
norm bounds N_3=6050, N_6=1640736 and L081's coefficient, amplitude
and heat-sum method; the different cumulative amplitude is proved below.

## Conclusion

Define the real physical form

    B_(i,G)=sum_(k,l)c_(i;kl) integral_D ell u_1(x)
                                     h_k(x) dot V_l(x) dx.          (1)

For normalized torus measure, set X=4 sin^2(theta_2/2),
Y=4 sin^2(theta_3/2), Z=4 sin^2(theta_4/2), L=X+Y+Z, and

    g_G=-(1/4) integral X Y (X-Y)^2/L^2.                         (2)

Set the integrand to zero at L=0. Then

    -1/4<g_G<0,   K_(i,G)=g_G B_(i,G).                          (3)

Both the scalar integral and full exterior sum are absolutely
convergent. This is a strict sign for the universal scalar only;
B_(i,G) is signed and unevaluated for both probes. Its upper cumulative
tail is retained. No identification with L132's four forms or L134's
two forms, and no numerical interval for K_(i,G), is asserted.

For rectangular mode cutoff K>=1, define B_(i,G)^[K] by truncating
both labels in (1), including every permitted zero component index.
Put C_G=280665 and

    H_half(K)=2(4*16^4)(16*16^3)*1024/(9K)
                                           exp(-9K^2/2048).

The complete spectral omission bounds are

    |B_(i,G)-B_(i,G)^[K]|<=16 C_G N_i H_half(K),
    |K_(i,G)-g_G B_(i,G)^[K]|<4 C_G N_i H_half(K).           (4)

At K=144 these bounds are respectively below 1.863*10^-16 and
4.658*10^-17, hence below 10^-12 for both probes. They enclose omitted
modes only. Retained physical/torus integration and arithmetic remain
to be evaluated and enclosed. The exact finite tensor is specified in
proof section 4, with both physical inverse weights unchanged.

L124 adds this coefficient with a plus sign before its outside factor
3. R, the triplet transverse-H sign and the complete comparison
K_(i,oo)+4 gamma D_i remain unresolved. Finer powers/logarithm, other
response jets, finite matching, interacting error <=c_box/2, continuum
axioms, reflection positivity, infrared control and finite positive
mass remain independent gaps. No Yang--Mills candidate is supplied.

## Proof

### 1. Contract the raw symbols without dropping their phases

Write e_a=exp(i theta_a), t_a=sin(theta_a),
eta_a=cos(theta_a/2), X_a=|1-e_a|^2, L=sum_a X_a.
For a plane a<b, L104(4)'s two paths give exactly

    (z_v tau)_(ab)=v_a(1+e_a)(1-e_b)
                                      -v_b(1+e_b)(1-e_a).           (5)

Indeed q tau=e_a-e_b and b tau=1-e_a e_b; substitute both
in z_v=(v_a+v_b)q-(v_b-v_a)b. This checks the sign and keeps
both paths. The circulation row has entries (1-e_b) and -(1-e_a).
Summing its adjoint over all incident planes, including those with
b<a, therefore gives

    (c^* z_v tau)_a=v_a(1+e_a)(L-X_a)
                    -(1-e_a)sum_(b!=a)v_b(1+e_b)(1-e_b^-1).

L104(5)'s endpoint-filtered centered difference is
w_a=-u_1(1+e_a)i t_a/2. Its adjoint satisfies

    w_a^*=u_1(1+e_a^-1)i t_a/2,
    (1+e_a)(1+e_a^-1)=4 eta_a^2,
    (1+e_a)(1-e_a^-1)=2i t_a,
    w_a^*(1-e_a)=u_1 t_a^2.

Consequently the full contracted row is

    w^*c^*z_v tau
       =2i u_1 sum_b v_b t_b
                      [eta_b^2(L-X_b)-sum_(a!=b)t_a^2]
       =(i u_1/2)sum_b v_b t_b
                                    sum_(a!=b)X_a(X_a-X_b).        (6)

The last equality uses t_a^2=X_a eta_a^2 and
eta_a^2=1-X_a/4. In particular it would fail for an unfiltered
incidence in place of the specified centered difference.

Multiply (6) by sigma_h=2i sum_r h_r t_r and retain L^-2.
The complete bilinear integrand, apart from u_1, is

    -sum_(r,b)h_r v_b t_r t_b
                           sum_(a!=b)X_a(X_a-X_b)/L^2.             (7)

Every factor except t_r t_b is even separately in each angle.
For r!=b, reflection of theta_r deletes precisely that off-diagonal
entry. For r=b its diagonal numerator is

    n_b=-X_b(1-X_b/4)sum_(a!=b)X_a(X_a-X_b).                   (8)

Permutation of the complete angle domain makes the three diagonal
integrals equal. Pairing the a,b and b,a contributions to sum_b n_b
gives the exact polynomial identity

    sum_b n_b=-(1/4)sum_(a<b)X_a X_b(X_a-X_b)^2.              (9)

Divide (9) by L^2, integrate, and use equality of the three
unordered-pair integrals. Each diagonal integral is exactly (2).
Thus the torus contraction is g_G u_1 h dot v, proving (3)'s
functional identity first at finite exterior cutoff.

All angle manipulations are legitimate for integrable functions.
For example |sum_(a!=b)X_a(X_a-X_b)|<=2L^2 and t_b^2<=X_b,
so (8)/L^2 is bounded and tends to zero as L tends to zero. The
off-diagonal terms in (7) have the same boundedness. The symmetrized
integrand in (2) is bounded by (X-Y)^2/4 and also tends to zero
at the corner. No singular point value or conditional parity
interchange is needed.

### 2. Strict scalar sign and analytic bounds

The integrand X Y (X-Y)^2/L^2 is nonnegative and positive on an
open set of angle triples. Hence g_G<0. Also XY/L^2<1/4 almost
everywhere, since Z>0 almost everywhere and (X+Y)^2>=4XY.
The independent single-angle means are integral X=2 and integral
X^2=6, by expanding X=2-2 cos(theta_2). Therefore

    integral (X-Y)^2=6+6-2*2*2=4,
    0<-g_G<(1/16)integral (X-Y)^2=1/4.

This proves the strict bounds without torus quadrature. The negative
scalar does not give a sign for the signed actual-probe form (1).

### 3. Keep the upper cumulative field and control the full mode sum

The transverse curl of V equals that of A: the lower prefix is a
transverse gradient, whose mixed derivatives commute. Thus on a
component-1 label delta=h=0 exactly. On a transverse input component
alpha, V=A has that one component, and

    delta_a=partial_a div_T A-Delta_T A_a.

In particular delta_alpha=-sum_(b!=alpha)partial_b^2 A_alpha;
for a!=alpha it is partial_a partial_alpha A_alpha. Here Delta_T
denotes sum_b partial_b^2, with its nonpositive differential sign.
No gauge-divergence condition on these component-labeled modes is used.

Such a label has k_1>=1. Set kappa_j=pi k_j/8. Its axial factor
is v_(k_1)=sin(kappa_1(x_1+4))/2, whose exact upper primitive is

    j_n(x_1)=[cos(kappa_n(x_1+4))-(-1)^n]/(2 kappa_n), n>=1. (10)

It vanishes at 4, and j_n'=-v_n. The constant (-1)^n is retained:
it is the actual upper-tail endpoint, not an adjustable primitive.
Each transverse product amplitude is <=1/8. Since |j_n|<=1/kappa_n,
the preceding delta rows imply, for every a and normalized mode,

    |h_(k,a)|<=sqrt(lambda_k)/(8 kappa_1)
                      =|k|/(8 k_1)<=|k|/8.                   (11)

For off-diagonal rows kappa_a kappa_alpha<=lambda_k/2 even gives
the stronger bound |k|/(16 k_1). Zero frequencies give zero
derivatives, so they need no separate exception. Component-1 modes
already have h=0; their full constant lower prefix still occurs in V_l.

L081/L132 give |V_(l,a)|<=1/2, |u_1|<=165, support volume
<=1296 and ell<=7 on that support. Thus the absolute physical pair
integral in (1) is at most

    1296*7*165*3*|k|/16=C_G |k|.                         (12)

Import |c_(i;kl)|<=N_i exp[-(lambda_k+lambda_l)/16]
from L132. Since lambda_k/16>9|k|^2/1024, and

    s exp(-9s^2/2048)<=16  for every s>=0,

(the maximum is sqrt(1024/9) exp(-1/2)<16), the product of
(12) and the two heat weights is bounded by

    16 C_G N_i exp[-9(|k|^2+|l|^2)/2048].                 (13)

This summable majorant proves absolute convergence and passage from
finite cutoffs in section 1 to the full functional identity. It also
keeps both actual probe sectors, all lower-prefix terms and the upper
primitive constant. No physical axial integration by parts or boundary
term deletion was used.

For completeness, let c=9/2048. The decreasing Gaussian satisfies
sum_(n>=0)exp(-c n^2)<=1+sqrt(pi)/(2sqrt(c))<16: use
pi<22/7<(15/8)^2 and sqrt(2)<3/2, which bound the latter
expression by 1+10 sqrt(2)<16. Thus the complete single-label sum
is at most 4*16^4. Its rectangular-cutoff complement is at most

    (16*16^3)*1024/(9K) exp(-9K^2/2048),

by integrating each omitted coordinate above K and using
integral_K^infinity exp(-c x^2)dx<=exp(-cK^2)/(2cK).
The union of the two omitted-label sets has heat weight bounded by
H_half(K). Combining with (13) proves the first bound in (4);
|g_G|<1/4 proves the second.

At K=144 the exponent is 729/8>90. The positive Taylor series
through degree 8 gives exp(3)>20, so exp(-729/8)<20^-30.
With the larger N_6, the resulting exact rational bounds are

    35532189/190734863281250000000000 <1.863*10^-16,
    35532189/762939453125000000000000 <4.658*10^-17.

These bounds cover the entire omitted spectrum, not a preview or
retained numerical evaluation. The smallest necessary cutoff was
not optimized.

### 4. Exact finite tensor and the remaining evaluation obligation

Define the linear maps on smooth one-forms

    L_F A=A_T-grad_T integral_(-4)^(x_1)A_1,
    J_T A=integral_(x_1)^4
                       (grad_T div_T A_T-Delta_T A_T)(r,x_T)dr.

The second formula uses only A_T; it is exactly h on the normalized
component modes by the curl cancellation in section 3. At rectangular
cutoff K, let

    (M_G,K)_kl=integral_D ell u_1 (J_T f_k) dot (L_F f_l),
    (Q_i,K)_kl=q_i(f_k,f_l),
    (F_K)_kk=exp(-lambda_k/16)/lambda_k.

Then symmetry of Q_i,K and direct expansion of the trace give

    B_(i,G)^[K]=Tr(M_G,K F_K Q_i,K F_K).                   (14)

M_G,K may be unsymmetric; both labels are summed and c is symmetric.
There is no factor 2 from optional symmetric polarization. Both
inverse weights follow because each physical form and probe contains
one normalized A factor on each label.

Here are complete row instructions for M_G,K. For input alpha=1,
J_T f_k is zero. For alpha transverse, replace its axial v_n factor
by j_n from (10). In output alpha, sum the terms obtained by
replacing each transverse factor in b!=alpha by minus its second
derivative. In output a!=alpha, replace the transverse factors in
a and alpha by their first derivatives. Leave every other factor
unchanged. Pair these rows with L_F f_l's direct component-a product
and negative component-1 prefix product from L132, including
p_0=ell/sqrt(8) and p_n=sin(kappa_n ell)/(2 kappa_n).
Use weight ell u_1=(ell f) tensor r tensor f' tensor r, with
r=rho and f(x)=x rho(x). Each resulting signed term is a product
of four exact one-dimensional moment matrices. The upper j_n row
retains both its cosine and constant summands.

Use L132 proof section 2's full-curvature row instructions for Q_i,K,
with both displacement sectors retained. Insert the elementary
Laplace identity exp(-lambda/16)/lambda=
integral_(1/16)^infinity exp(-t lambda)dt on both sides of Q.
The gap lambda>=3pi^2/64 gives an absolutely convergent double
integral of the four one-dimensional tensor traces, as in L081(6).
This is an exact finite evaluable form; no already certified moment
table or physical interval is assigned to its new upper-primitive rows.
Their retained integration/arithmetic and the scalar (2) still need
enclosure before determining the actual G values.

### 5. Verification and scope of the advance

From the active notebook run

    python3 scripts/combined-ward-response/check_g_physical_reduction.py

The script writes full exact rational Laurent records to
scripts/combined-ward-response/g-physical-reduction-certificate.json.
All 31 raw path, complete contraction, separate-reflection, pair-square
and mean identities pass with zero coefficient differences. It retains
the pre-reflection polynomials, required expressions and full tail
rational arithmetic. The complete tail record and failure/status fields
were inspected; the certificate is support for the explicit proof, not
a replacement for sign, convergence or hypothesis checking.

This is one RESEARCH / calculation / REPRODUCTION attempt under the
unchanged prior EXPLORE complete-other/other assessment. L104's limit
is imported, not reproved. Reproduction is limited to its different
raw cumulative symbol and physical rows, which the E,Q,ax reductions
do not cover. No known general Ward/flow theorem is rederived or used
to assign an isolated coefficient. The reduction is local progress
without a claim of mathematical originality beyond the sources checked.
No complete compensation, actual-probe G sign or interacting conclusion
is obtained.

## Mathlib

Full matching cumulative G contraction and complete spectral-tail bound:
**not checked**. Supporting Laurent/Fourier algebra, separate-reflection
and permutation symmetry, finite tensor traces, elementary Gaussian
tails, Laplace transforms and dominated convergence: **not checked**.
Unknown availability is not evidence of absence.
