# C998e: Full residual-Gram representation and a first-order diagonal setup stop

## Hypotheses

Use exactly C998a's three real columns f_j,h_j,q_j, j=0,1,2, exact
neutral completion from C999q and witness X from C999y. The free middle
dyadics are in `scripts/separation-seven/frozen-reference-proposal-652.npz`,
SHA256 `2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
Retain ell=log(3)/2, a=ell/2, delta=.01, m=286, J=14 and C999's
restricted selfadjoint B0>=beta I, beta=.219999. No parameter is retuned.
All analytic-response, arithmetic, source-to-Xi, whole-core and unreplayed
c_* contracts remain. Inner products are first-slot-linear.

Write U for the exact unitary parity/reflection map in C998a(4), and
v_epsilon,j=(Uq_j)_epsilon. Let C_end v(t)=integral_0^a v(s)/(t+s)ds.
In particular both blocks have coefficient 1/2. Use C744v's complete
T,T*, including all sixteen translations and the smooth infinite kernel,
and C999z's h_m and all four products of every E_epsilon,l, 0<=l<14.
No old floating action or approximate neutrality defines these functions.

The invocation-start SPECIALIZE assessment662/comparison663 covers this
full-product ledger attempt. Import Folland, *Real Analysis*, 2nd ed.
(1999), Section2.5, Theorem2.37 and proof pp67-68, finite products p65,
and completed-measure version Theorem2.39 p68,
[textbook extract](https://people.math.sc.edu/girardi/m7034/1617/hw/FollandRA2edProdMsr.pdf).
Finite Lebesgue intervals are sigma-finite; we use Borel representatives.
Every multiple integral below has its own absolute majorant. No general
Fubini or quadrature theorem is reproved. McCafferty's half-line square
is only the comparison in assessment662, not an input for this cell.

For the cost assertion prescribe one particular scalar implementation:
evaluate each USED diagonal h(k_n), n<=255, once, shared across all three
columns, by the direct term-by-term recurrence C999(19). Accept its
analytic remainder only if

    R_n(K)=sqrt(2)/[6((K+1/4)^2+k_n^2/4)] <= 2^-45.       (1)

The elementary and rounding allowance is an additional 2^-47 per diagonal.
Thus the total diagonal-value error is at most d=2^-45+2^-47. This is a
sufficient absolute-error prescription, not a necessary accuracy condition
for the true Gram. The rule is the already assessed specialization of
[DLMF5.11.2 and Section5.11(ii)](https://dlmf.nist.gov/5.11#ii) in C999;
no higher Bernoulli terms or new sector remainder are used here.

One scalar work unit is one real addition, subtraction, multiplication,
division, comparison or scalar assignment at the chosen finite precision.
Special functions must be expanded into charged operations. The lower
bound below counts ONLY mandatory real divisions, so omits even the cost
of precision/register management. It holds under this generous convention
at every precision. Algebraic acceleration of the recurrence is outside
this prescription; repeated columns are already cached.

## Conclusion

Equations(3)-(8) below give the ENTIRE coefficient-coupled projected3x3
Gram, including both Carleman cross terms, the finite-cell square and the
exact two-moment correction. They are absolutely convergent identities.
Explicit output-edge and forcing-suffix losses are each below1e-14 per
Gram entry. The conditional error allocations in Sections4-5 suffice
for entry error<=1e-8 and numerical inverse-upper-comparison uncertainty
below1e-4. They do not establish the size of the residual or inverse debt.

The prescribed first-order diagonal setup fails the work test BEFORE
quadrature: all254 free modes are used, and (1) requires K>=2800001 for
every one. Therefore this setup alone needs at least

    254*2800001 = 711200254 divisions > 100000000.          (2)

This stops that direct recurrence/absolute-envelope ledger. It proves
neither a lower bound for all direct Gram methods, necessary complexity,
large residuals nor a negative actual signed form. The representation is
a local standard-method REPRODUCTION, written664 and not separately
audited. No complete Gram, inverse-pairing, S3 sign or RH candidate is
certified. Interior quadrature, scalar enclosures, interface strips and
the full work ledger remain unpaid; no large batch is run.

## Proof

### 1. Full bounded action, coefficients and fixed norm envelopes

Suppress epsilon,j only within individual formulas. Define

    A_epsilon,j(t) = [U(Tf_j+T*h_j-(D-delta)q_j)]_epsilon(t)
                    -(h_m v_epsilon,j)(t)
                    -sum_(l=0)^13 (E_epsilon,l v_epsilon,j)(t),
    g_epsilon,j(t) = A_epsilon,j(t)-(1/2)C_end v_epsilon,j(t). (3)

Thus (g_+,j,g_-,j)=Ug_j for C998a(1), and r_j=P0g_j. Formula(3)
includes all coefficients of the finite diagonal, both orientations of
every zero-extended translation, every h_m cell integral, all four E
products including l=0, and the complete K and K* series. The bounded
action A has its exact indicator domains, not a putative ordinary kernel
for translations. Splitting these indicators at C998a's603 interfaces
is permitted but creates no orthogonality. The midpoint uses the exact
unitary on the two open halves; it is not removed by setting an odd trace
to zero. This is also an expansion of the whole sigma+J+R, not its three
separate squares.

The exact rational envelopes of C998a(7), checked654 and replayed655,
give, in every column,

    F+H<26, V<14, ||g_j||<G:=760,
    ||P0(Tf_j+T*h_j)||<130, ||q_j||<14, ||B0q_j||<630. (4)

For example ||g_j||<=5(F+H)+45V<760. Projection is a contraction.
The two last bounds follow from the same full-operator bounds, not from
saved residual samples. The script below reads the complete rational
values and all762 dyadics, not a JSON preview.

Pointwise |v_epsilon,j|<14. The full-cell forcing is bounded by
17(F+H): each of sixteen shifts has weight<1, and the entire smooth
kernel has supremum<1. The finite diagonal has amplitude<=21V.
U amplifies a full-cell supremum by at most sqrt(2)<3/2.
C998a's half-cell h_m and E amplitudes are <=3.5V and18V. Hence

    |A_epsilon,j| <= (3/2)[17(F+H)+21V]+21.5V <1500.

Put L(t)=log(1+a/t), 0<t<=a. Then

    |g_epsilon,j(t)| <=1500+7L(t).                       (5)

All arrays retain their repeated coefficients: (3) is a linear action
on the SAME f,h,q everywhere. Independent copies of a coefficient are
not substituted in different products. The real fixed columns define
a complex-linear three-column map when coefficients are complex.

### 2. Finite-cell product and every cross term

For s,u>0 define

    K_tau(s,u)=integral_tau^a dt/[(t+s)(t+u)], 0<=tau<a.

If s!=u, direct partial fractions give

    K_tau(s,u) = {log[(a+s)/(tau+s)]
                        -log[(a+u)/(tau+u)]}/(u-s);
    K_tau(s,s) = 1/(tau+s)-1/(a+s).                     (6)

These are FINITE-cell formulas. For tau>0 the integral representation
also gives the continuous value when s or u is zero and near s=u.
It provides a definition without subtracting close logarithms; it is
not yet an implemented stable evaluator. At tau=0 the axes are a null
set and need not be assigned the divergent boundary values.

For any two columns, set I_ij=<g_j,g_i>. Then unitarity gives

    I_ij = sum_epsilon {
      integral_0^a A_epsilon,j(t) conjugate(A_epsilon,i(t)) dt
      -(1/2) integral_(0,a)^2
          [v_epsilon,j(s) conjugate(A_epsilon,i(t))
           +A_epsilon,j(t) conjugate(v_epsilon,i(s))]/(t+s) ds dt
      +(1/4) integral_(0,a)^2
          v_epsilon,j(s) conjugate(v_epsilon,i(u)) K_0(s,u) ds du }.
                                                               (7)

Both mixed products are necessary, including their conjugations. In
particular the last term alone is not the requested residual Gram.

Here are absolute majorants for the actual interchanges. The A-square
is bounded by1500^2 on a finite interval. Each mixed multiple integrand
is bounded by1500*14/(t+s), whose integral is
1500*14*2a log2<infinity. Before integrating t in the singular-square
term its absolute triple integrand is bounded by
14^2/[(t+s)(t+u)]. Tonelli gives its integral as
14^2 integral_0^a L(t)^2 dt <=14^2*5a, using
L(t)<=log(2a/t) and the exact log-squared integral from C998a(14)-(15).
Folland's Fubini theorem therefore applies to the complex products,
not just nonnegative formal kernels. Formula(6) then evaluates the
inner t integral. Products involving the smooth forcing series have
summable absolute uniform bounds from C998a(18), multiplied by the
integrable majorants just given; thus those series can also be expanded
or integrated. Finite h_m/E/translation products need no limit exchange.
This covers the coincident corner of the two Carleman factors.

Let w_+,w_- be the full-cell moment representers and write
omega_c,epsilon=(Uw_c)_epsilon. Their absolute values are below3:
|w_c|<=exp(ell/2)<exp(.3)<2 and sqrt(2)<1.5. Set

    mu_c,j = sum_epsilon {integral_0^a A_epsilon,j(t) omega_c,epsilon(t)dt
             -(1/2)integral_(0,a)^2
                v_epsilon,j(s) omega_c,epsilon(t)/(t+s)ds dt},
    G_w = [[exp(ell)-1,ell],[ell,1-exp(-ell)]],
    Gamma_ij = I_ij-mu_i^* G_w^-1 mu_j.                  (8)

The moment interchange has majorant3*14/(t+s), so is also justified.
mu_j is the exact column of two moments of g_j. C999(21)'s orthogonal
projection identity, or its two-variable expansion, gives (8).
With first-slot-linear inner products Gamma_ij=<r_j,r_i>, so Gamma is
the usual matrix R*R for Rz=sum_j z_j r_j. Since the fixed data are
real, it is real symmetric and also equals the entry convention with
i first. Complex column combinations still retain every off-diagonal
term. G_w is the SAME positive moment Gram as C998a(23); it is not a
projected inverse of B0 or a saved approximate nullspace.

### 3. Explicit edge and complete forcing-suffix allowances

Take tau=a*2^-80. Compute (7) only with outer t in[tau,a], replacing
K_0 by K_tau, and compute the moments with this same outer cutoff.
The s,u input integrals remain over[0,a]. Thus the discarded region is
exactly the two output ends, not an unpaid interior or input corner.
Write L_tau=log(2a/tau)=81log2<81 and A0=1500+7*81=2067.
The whole unprojected Gram omission is bounded entrywise by

    e_I = 2tau[A0^2+14A0+98].                           (9)

Indeed integrate (1500+7log(2a/t))^2 on each of the two ends; the
integrals of1,-log u,(-log u)^2 on(0,1) are1,1,2. This also bounds
all absolute cross terms before cancellation. Each moment component
loses at most

    e_mu=6tau(A0+7),

using both parities and |omega|<3. C998a gives ||G_w^-1||<384 and
||mu_j||<=sqrt(2)G. The vector moment loss has norm<=sqrt(2)e_mu.
Expanding the two moment products therefore bounds the projected
Gram loss by

    e_edge = e_I+384(3040 e_mu+2e_mu^2) < 1e-14.        (10)

The exact check uses tau<(3/10)2^-80. No smallness of g_j is assumed.
In particular merely bounding its discarded L2 norm and multiplying
by a global norm would unnecessarily lose the L1 moment control here.

Next retain forcing indices1<=l<12 and omit l>=12 in K,K*. C998a(18)
supplies the uniform suffix bound

    S_N=3(1/64)^N[N/(1-1/64)+(1/64)/(1-1/64)^2], N=12.

The forcing action error in each full-cell column is <=e=26 S_12,
since ell<1. Projection is a contraction, so the complete Gram change,
including one-suffix and two-suffix products, is at most

    e_suffix=(1520+e)e < 1e-14.                          (11)

The same amplitude/norm bounds apply to the prefix: its nonnegative
kernel has row/column sums bounded by the complete kernel's sums in
C744v, and the shift part is unchanged. Thus (10) can be applied to
the prefix without silently changing G. Estimates(10)-(11) combine
by the triangle inequality in either order. They do not omit suffix
cross terms or an infinite output.

### 4. Conditional scalar/projection ledger and inverse-pairing use

The following are numerical REQUIREMENTS, not already computed balls.
For the chosen prefix/cutoff let I,mu denote its exact integrals. Suppose
their numerical values satisfy entry error e_i<=1e-9 in I and vector
error e_m<=1e-16 in each mu column. Suppose also that a numerical inverse
of the explicit two-by-two G_w has operator error e_g<=1e-16.
Because sqrt(2)*760<1075, (8) then has error at most

    e_i+384(2150 e_m+e_m^2)+e_g(1075+e_m)^2 <2e-9.       (12)

This pays the moment SOLVE as well as the moment integrals. It follows
by inserting the exact G_w^-1 in the approximate product, expanding its
two perturbed vectors, then bounding the remaining inverse perturbation.
The positive determinant bound>1/192 from C998a makes the solve meaningful;
no numerical solve is actually supplied here.

If the diagonal-value errors satisfy d=2^-45+2^-47, the corresponding
action error is at most14d in each column by orthonormality of e_n and
||q_j||<14. Using the projection contraction, its whole-Gram contribution
is at most

    e_diag=(1520+14d)14d <1e-9.                          (13)

Reserve a further3e-9 entrywise for the remaining coefficient, elementary,
interface-strip and assembly errors. These require actual simultaneous
coefficient enclosures, certified interface ordering/strips and evaluator
bounds. They are NOT established by reserving an allowance. Combining
(10)-(13) and this reserve gives a conditional total below4.955e-9,
hence below1e-8. Error propagation must follow the same exact coefficients
through (3),(7),(8); interval overestimation is allowed, deleting products
or assuming independent errors is not.

For combining these estimates use the order: forcing suffix, output
cutoff, diagonal perturbation, numerical integrals/moment solve. The
cutoff is a contraction on g before applying P0, so(13) still uses the
unperturbed bound760. After the diagonal perturbation the moment norm
is at most sqrt(2)(760+14d)<(99/70)(760+14d)<1075, as checked exactly.
Thus(12) retains its stated constant; no error is propagated through an
unpaid new norm bound. The amplitude margin in(5) also exceeds14d.

There is a useful way to allocate the Gram uncertainty without taking
a poorly controlled square root near zero. Let F:C^3->H0 have columns
b_j=P0(Tf_j+T*h_j), Q have columns q_j, and R=F-B0Q. All Q columns
are in Dom(B0), by C999's strong-domain theorem. The inverse is bounded,
positive and selfadjoint on H0. Expanding F=B0Q+R gives exactly

    F*B0^-1 F = A_trial+R*B0^-1R,
    A_trial=Q*F+F*Q-Q*B0Q,
    0 <= R*B0^-1R <= beta^-1 Gamma.                     (14)

This is finite-column algebra using C999(2)-(4), not a new inverse/domain
theorem. B0 is applied only to Q in its strong domain. In particular (14)
is a ONE-SIDED inverse upper comparison with a possibly large residual
debt. A small numerical uncertainty in Gamma does not make that debt small.

To show that the required precision is sufficient for its intended
downstream use, require each numerical representative of b_j,q_j,B0q_j
to have L2 error<=u=1e-10, and each of the three scalar pairings forming
an A_trial entry to have additional integration/rounding error<=1e-9.
The norms130,14,630 in(4) imply entry error

    e_A <= 28u+890u+14u+3u^2+3e-9 =932u+3u^2+3e-9.

For example each Q*F term costs14u+130u+u^2, and Q*B0Q costs
14u+630u+u^2. No unbounded-operator perturbation is inferred: B0q is
separately represented. Symmetrizing the computed matrix preserves these
entry bounds. A3x3 Hermitian matrix with entry errors<=e has operator
error<=3e by the row-sum bound (or finite Cauchy--Schwarz).
Thus the numerical radius for the ideal upper matrix in(14) is at most

    rho=3e_A+3*10^-8/beta <4.25e-7 <1e-4.               (15)

Using the center plus rho I gives a rigorous upper matrix IF all preceding
enclosures have been supplied. Its excess over the exact ideal upper
matrix is at most2rho<1e-6. Both the radius and this outward padding fit
the diagnostic budget. This is only an allocation check: A_trial, Gamma,
their actual residual debt, signed remote U and the .000999 X*X comparison
are uncomputed. Higher/mixed endpoints, H2 and actual-Xi assembly remain
independent gaps.

### 5. Discriminating cost check and stop

The assessed direct recurrence for the diagonal is

    psi(z)=log(z+K)-1/[2(z+K)]
           -sum_(j=0)^(K-1)1/(z+j)+E,
    z=1/4+ik_n/2, |E|<=R_n(K).

For the real part its jth reciprocal is
(j+1/4)/[(j+1/4)^2+k_n^2/4]. Every direct evaluation contains a
division; even caching every shared j-square and reusing each frequency
across all columns leaves one division per(n,j). The frozen arrays use
EVERY free n=2,...,255, verified exactly below. The low modes0,1 can be
ignored for this lower count.

C998a gives k_n<2040. Since sqrt(2)>7/5, for every K<=2800000 and
every n<=255,

    R_n(K) > (7/30)/[(2800000+1/4)^2+1020^2] > 2^-45.  (16)

The final comparison is exact rational arithmetic. Thus none of those
shifts satisfies the declared certificate(1). Conversely K=3000000
does satisfy its analytic part: sqrt(2)<3/2 gives
R_n(K)<1/[4(K+1/4)^2]<2^-45 even at n=0. This confirms the source rule
is effective; it does not pay elementary evaluation or make it affordable.
Equation(2) follows. It already exceeds the ENTIRE100000000-operation
budget, before elementary constants, neutral coefficients, quadrature,
projection, caching/storage or output work are charged.

There is therefore no reason to run an interior batch or claim the
conditional ledger is certified. The prescription stops here. Its
conservative raw-norm envelope, absolute diagonal allowance and first-order
remainder are explicit restrictions. Sharper coefficient-coupled error
analysis, higher-order certified diagonal formulas or a different action
representation are not ruled out. Nor does an upper remainder bound that
fails(1) prove an actual numerical error lower bound. No assertion about
all direct integration costs follows.

Reproduce the finite checks with

    python3 scripts/separation-seven/direct-gram-ledger-664.py

The full certificate is `scripts/separation-seven/direct-gram-ledger-664.json`.
It pins the archive, compares all762 exact trial dyadics with654, reuses
the complete654/655 rational data with their checked pin, and verifies
all254 used modes. It saves all exact edge/suffix/projection/diagonal and
inverse-radius bounds, the failed work threshold, and the unpaid items.
All27 checks pass with no failures. This script does not verify Fubini,
the source contracts, an analytic quadrature evaluator or any actual Gram.
The new mathematical argument still requires a separate critical audit.

## Mathlib

Full matching coverage for this fixed finite-cell residual-Gram ledger and
its prescription-specific cost result was not checked. Unknown coverage
does not mean absence. Product-measure integration, finite Gram projection,
selfadjoint inverse bounds and elementary rational inequalities are
supporting mathematics; the precise imported interchange result and the
local specializations are recorded above. No formal proof is claimed.
