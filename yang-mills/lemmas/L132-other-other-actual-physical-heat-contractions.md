# L132 — Four actual physical heat contractions and their complete spectral tail

## Hypotheses

Import L128(1), including its absolute convergence, real symmetric
c_(i;kl), all five scalars and physical fields; L080's real relative
mode normalization; L120(2)'s lower-rooted prefix as specified in L128;
and L008(1),(6)'s actual full-displacement probe forms. The scope remains
SU(2), both L010 probes i=3,6, D=(-4,4)^4 with all-face relative
fixed-link conditions, direction-1 straight forest, flow time 1/16,
and bare fixed-mesh small-coupling coefficients before refinement.
No new mesh limit is taken. Retain both Psi_13 and Psi_24 sectors,
the transition region, constant axial edge mode, every physical prefix
and exterior heat label. Transverse indices run over 2,3,4 and ell=x_1+4.

Import L127(3), L130(1), L131(1)'s scalar bounds, and L081 proof
sections 2--4's explicit cutoff-derivative, mode-amplitude and Gaussian
sum estimates. The latter are specialized below to the full displacement
and new physical tensors; L081's diagnostic-specific tail is not simply
assigned to a different coefficient.

## Conclusion

Define four absolutely convergent real functionals, with all k,l summed:

    P_(i,D)=sum c_(i;kl) integral_D ell (div_T u)(V_l dot V_k),
    P_(i,X)=sum c_(i;kl) integral_D ell sum_(rho,m) partial_m u_rho
                      (V_(l,rho)V_(k,m)+V_(l,m)V_(k,rho)),
    P_(i,A)=sum c_(i;kl) integral_D ell sum_rho partial_rho u_rho
                                                V_(l,rho)V_(k,rho),
    P_(i,C)=sum c_(i;kl) integral_D ell sum_(rho,a)
                          u_rho V_(k,a)(curl_T V_l)_(rho a).       (1)

Then L128's entire retained transverse-H coefficient is exactly

    K_(i,tr)=(h_D+tau)P_(i,D)+(h_X-tau/2)P_(i,X)
                                 +h_A P_(i,A)+(xi+2tau)P_(i,C).  (2)

In particular no separately differentiated potential tensor is needed.
The coefficients satisfy

    207/1000<h_D+tau<31/100,
    19/200<h_X-tau/2<979/6000,
    -7/20<h_A<-1/4,
    3/100<xi+2tau<3/80.                                    (3)

For a rectangular cutoff K>=1 retaining every allowed mode index <=K,
let P_(i,s)^[K] be the exact finite sums, s=D,X,A,C. They have the
finite tensor/double-Laplace representation in proof section 2. Put

    C_D=C_A=20582100, C_X=1395445968, C_C=280665,
    N_3=6050, N_6=1640736,
    H(K)=2(4*12^4)(16*12^3)*512/(9K)*exp(-9K^2/1024).

The complete omitted-spectrum estimate is

    |P_(i,s)-P_(i,s)^[K]| <= C_s N_i H(K).                  (4)

At K=96 each of the eight errors is strictly below 5*10^-11. Using
(2) with these truncated sums gives |K_(i,tr)-K_(i,tr)^[96]|<5*10^-11.
These are bounds for omission of modes, not retained evaluation errors.
No actual-probe value/sign, full other/other comparison, compensation,
finer remainder/logarithm, interacting estimate or Yang--Mills candidate
is certified. The five other L124 coefficients E,ax,-Q,G,R remain.

## Proof

### 1. Complete spatial integration by parts, with its sign retained

For a finite symmetric coefficient sum set

    S_(rho,a)=sum c_(i;kl)V_(l,rho)V_(k,a),
    A_rho=sum c_(i;kl)V_(l,rho) div_T V_k,
    T_rho=sum c_(i;kl) sum_a V_(l,a) partial_a V_(k,rho),
    C_rho=sum c_(i;kl) sum_a V_(k,a)(curl_T V_l)_(rho a).

Symmetry under k,l exchange gives S_(rho,a)=S_(a,rho). Product
differentiation, with no assertion that div_T V_k is zero, gives

    sum_a partial_a S_(rho,a)=A_rho+T_rho,
    C_rho=(1/2)partial_rho tr S-T_rho.

The second identity follows by expanding curl_T V_l and exchanging
k,l in its transport term. Therefore

    A_rho-T_rho=sum_a partial_a S_(rho,a)
                                  -partial_rho tr S+2 C_rho.   (5)

Multiply by ell u_rho, sum rho, and integrate. The compact support
of u removes every transverse boundary term, and partial_a ell=0
for transverse a. The first derivative in (5) contributes
-integral ell sum_(rho,a)(partial_a u_rho)S_(rho,a)=-P_(i,X)/2.
The negative trace derivative contributes +P_(i,D), with a positive
sign. The remaining term contributes +2P_(i,C). Thus the original
tau contraction is P_(i,D)-P_(i,X)/2+2P_(i,C), proving (2).
L128's polynomial mode/heat majorants dominate each derivative here,
so finite-cutoff identities pass to the full sums absolutely.

This integration by parts changes the H coefficients explicitly.
It does not contradict L127's obstruction with H held fixed or delete
the nonzero anisotropy. Substituting the imported strict scalar bounds
gives (3), by ordinary endpoint arithmetic.

### 2. Exact actual-probe finite tensor, including both inverse factors

Write r=rho and f(x)=x rho(x). The full displacement has components

    u_1=f tensor r tensor f' tensor r,
    u_2=r tensor f tensor r tensor f',
    u_3=-f' tensor r tensor f tensor r,
    u_4=-r tensor f' tensor r tensor f.

All strains are their actual derivatives. No coordinate-swap deletion
of a probe sector is invoked. Let L map a smooth one-form to its
transverse forest lift V=A_T-grad_T integral_(-4)^(x_1) A_1.
For ordinary relative product modes f_k, define M_(s,K) by the
symmetric polarization of the integral in (1) with V=L f.
Define Q_(i,K)_(kl)=q_i(f_k,f_l), with q_i polarized exactly as in
L008(1),(6), and F_K diagonal with entries exp(-lambda_k/16)/lambda_k.
Since both A_k=f_k/sqrt(lambda_k) exterior factors occur in both the
probe and physical form, their exact finite contraction is

    P_(i,s)^[K]=Tr(M_(s,K) F_K Q_(i,K) F_K).               (6)

The following instructions specify every tensor factor in (6).
A curvature row in plane mu nu has the two signed component products
+partial_mu f_nu and -partial_nu f_mu. Q_3 pairs this row with itself
and weight w_mu+w_nu. Q_6 pairs F_mu alpha and F_nu alpha with
weight s_mu nu and half in each polarization order; alpha outside
{mu,nu} suffices because the other rows are zero.

The transverse lift V_a has its direct input-component-a product and
negative input-component-1 product, whose axial factor is

    p_0(x_1)=(x_1+4)/sqrt(8),
    p_n(x_1)=sin(n pi(x_1+4)/8)/(2 n pi/8), n>=1,

and whose transverse factor in direction a is v'_n. Every other
factor is the ordinary mode factor. Its transverse curl equals the
curl of f_T exactly, since mixed derivatives of the scalar prefix
commute; this statement does not set div_T V to zero. For D,X,A
pair the complete lift rows with weights in (1); for C pair lift
and curl rows, taking half in both polarization orders. Attach ell
to the axial coefficient in each physical form. The p_0 row is
retained and no upper-face value is imposed on this interior prefix.

Each signed separable coefficient produces a component-block tensor
product of matrices

    I_j(m,n)=integral_(-4)^4 weight_j(x) left_(j,m)(x)
                                             right_(j,n)(x) dx,

where weight_j is a derivative factor of the displayed displacement,
and for physical M the axial factor also contains x+4. This is a
finite exact expansion of (6). Insert
exp(-lambda/16)/lambda=integral_(1/16)^infinity exp(-t lambda)dt
on both sides of Q. The least eigenvalue is >=3 pi^2/64, so each
matched component-block term is the absolutely convergent integral

    coefficient * integral_(1/16)^infinity integral_(1/16)^infinity
     product_(j=1)^4 Tr[M_j E_(beta,j)(t) Q_j E_(alpha,j)(s)] dt ds.

This reuses L081's finite tensor/Laplace algebra but supplies the
different full-displacement physical factors, rather than reusing its
boundary diagnostic or its cancelled sector.

### 3. Explicit amplitude constants and full spectral tail

L081(7) gives |r|<=1, |r'|<=18, |f|<=3, |f'|<=55,
|f''|<=11394. Each full-displacement component has |u_rho|<=165.
Each diagonal strain has absolute value <=3025. Since div u=0,
div_T u=-partial_1 u_1, whose absolute value is <=3025. For any
transverse rho,m the displayed separated components give
|partial_m u_rho|<=34182: same-coordinate differentiation gives
3025; the f-to-f'' possibility gives 3*11394=34182; a derivative
of an r factor gives at most 3*18*55=2970.

The full probe operator is the sum of its two displacement-sector
operators. Coordinate permutation preserves L081's bounds 3025 and
820368 for each sector, so the triangle inequality gives
||B_i||<=N_i for L080's normalized probe operator B_i.
In particular |c_(i;kl)|<=N_i exp[-(lambda_k+lambda_l)/16].

For each normalized A_k, L081's mode calculation gives |V_(k,a)|<=1/2.
The transverse curl of V_k is that of A_k. A one-component mode has
only one possible nonzero derivative in any curl row, with amplitude
<=1/16. The support of u and its derivatives has volume <=1296
and ell<=7 there. Thus each normalized double-label physical integral
in (1) has absolute value bounded respectively by

    1296*7*3025*3/4=C_D,
    1296*7*34182*9*2/4=C_X,
    1296*7*3025*3/4=C_A,
    1296*7*165*6/(2*16)=C_C.

The six in the last line counts all ordered rho!=a entries; zero
diagonal curl entries are the only entries omitted. These bounds use
the entire length-eight prefix and all mode labels.

L081(9)--(10)'s complete one-label heat sum is <=4*12^4 and its
rectangular-cutoff complement is <=16*12^3*512/(9K)*exp(-9K^2/1024).
The union where either of two labels is omitted gives H(K). Multiplying
by the preceding amplitude and probe bounds proves (4). This includes
all larger corners, with no restriction to low physical modes.

At K=96, H's exponential is exp(-81) and its prefactor is 2717908992.
The largest C_s is C_X and the largest N_i is 1640736. The positive
Taylor series gives e^3>20, hence exp(-81)<20^-27. The common upper
bound for all eight errors is therefore strictly less than

    1395445968*1640736*2717908992 / 20^27
      =362215299406149/7812500000000000000000000 < 5*10^-11.

Finally (3)'s sum of coefficient absolute upper bounds is
31/100+979/6000+7/20+3/80<1. Applying (2) proves the claimed full
transverse-H omitted-spectrum bound.

### 4. Diagnostic evaluation and what remains unverified

Reproduction commands from the active notebook:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/check_physical_h_contractions.py --cutoff 2 --space-degree 96 --time-degree 16 --label K2-s96-t16-final
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/check_physical_h_contractions.py --cutoff 96 --space-degree 144 --time-degree 24 --label K96-s144-t24

The script saves every primitive matrix, quadrature rule, signed tensor
term and trace contribution in matching certificate JSON and factor NPZ
files under scripts/combined-ward-response/. The small-cutoff run checks
the original differentiated tau contraction against (5) for both probes,
and every retained physical tensor against dense diagonal inverse
weights. It does not independently validate the spatial integrals.

The preliminary sign error in the D contribution is preserved in
physical-h-K2-s96-t16-certificate.json, whose two IBP checks fail.
Equation (5) proves the corrected positive sign; subsequent corrected
and final checks pass. A second K=96 quadrature resolution changes the
eight diagnostic values by less than 2*10^-6, but this is not an error
enclosure. Full retained spatial/time quadrature and machine arithmetic
inclusion remain missing. Neither numerical refinement nor (4) supplies
those errors or establishes an actual-probe sign. The four exact
contractions and (4) are local REPRODUCTION progress under the unchanged
ready EXPLORE assessment; no mathematical novelty claim is made.

## Mathlib

Full matching actual-probe reduction and spectral-tail bound: **not checked**.
Supporting spatial integration by parts, finite tensor products/traces,
Laplace identities and Gaussian tail sums: **not checked**. Unknown
availability is not evidence of absence.
