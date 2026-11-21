# C998q: A fixed spectral saving for the complete frozen residual

## Hypotheses

Use C999's complex Hilbert space H=L2(0,ell), ell=log(3)/2,
a=ell/2, form domain V, two-moment kernel H0 and projection P0.
Its selfadjoint B0 on H0 is represented on V0=V intersect H0 by
B_trial=D+S_app-delta I, delta=1/100, with m=286,J=14 and
beta=219999/1000000. Keep C999/audit650's strong domain and order,
C999k Section2's COMPLETE reference R=H_head on raw modes0:511 and
D/2 on all higher modes, R>=.239999 I. All original analytic response,
IEEE754/Decimal, source-to-Xi, whole-core and unreplayed c_* contracts
remain hypotheses. Neither their source computations nor the head
factor are replayed here. Inner products are first-slot-linear.

The three columns f_j,h_j,q_j are EXACTLY C998a(1),(6)'s columns:
C999y's full96-integer X, denominator2^24 and exact zero extension to
C^2044, followed by C999q's exact neutral completion; q_j uses all762
free dyadics in `scripts/separation-seven/frozen-reference-proposal-652.npz`,
SHA256 `2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
No saved rounded raw vector or original residual sample defines them.
Let F have columns P0(Tf_j+T*h_j), Q have columns q_j and

    r=F-B0Q,       Gamma=r*r,       S_ref=R-.02I.

Here r:C^3->H0 includes the entire forcing and projected B_trial
action. Use the complete response and both forcing orientations of
C744v/w/audit534; C999z/audit646's exact two-parity split, all four
products of every E_epsilon,l, and its smooth-kernel Lipschitz bound
H_s=303/16; and C998a/audit655's ||S_app||<24 and finite diagonal
bound |h(k_n)-delta|<21 for n<=255. These are qualified mathematical
inputs, not assertions inferred from a certificate preview.

Source scope is invocation-start assessment699, separately approved700
(SPECIALIZE). Import Behrndt--Hassi--de Snoo--Wietsma,
*Antitonicity of the inverse for selfadjoint matrices, operators, and
relations*, [arXiv:1403.5704v1](https://arxiv.org/pdf/1403.5704v1),
Proposition2.1 p4, Theorem3.4 nonnegative proof case p11 and
Corollary3.5 p12; Teschl, *Mathematical Methods in Quantum Mechanics*,
GSM99, [author version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorems2.13/2.18 pp71-72/77, spectral calculus Theorems3.1/3.2
pp90-92 and bounded perturbations Theorems6.4/6.24 pp135/150.
The inspected source hypotheses/proof cases are recorded in699/700.
No general inverse-order or spectral theorem is reproved. Neutral
shorting is optional and is NOT used in this sufficient estimate.

## Conclusion

Let P_b retain raw cosine modes512,...,1023, and write

    A_nj=<r_j,e_n>,
    w_n=beta^-1-(h(k_n)/2-.02)^-1,
    K_b=A*diag(w_n)A.                                  (1)

All512 weights are positive. On the frozen three-dimensional family,

    r*B0^-1r <= beta^-1 Gamma-K_b,
    K_b >= [63562617128340729/625000000000000000000] I3
        >= 10^-6 X*X.                                 (2)

The scalar lower bound in(2) exceeds .000101700187405345.
The complete coefficient, weight and nine matrix-entry enclosures and
exact rational PSD certificates are saved in
`scripts/separation-seven/shifted-finite-band-701.json`.
The column errors are respectively below .001618,.001357,.002072;
their combined operator error is at most .00295767446. These include
the full neutral correction, not a zero-moment approximation.

This is local REPRODUCTION/specialization under the retained contracts,
written701 and upheld by the separate conceptual audit703 in Section5. It supplies the
requested finite-band saving, not a complete numerical upper debt:
Gamma and the numerical matrix E, trial/remote pairings and signed S3
remain unpaid. Higher/mixed signs, C744q/H2, non-neutral coverage and
actual-Xi/global assembly remain independent gaps. No RH candidate or
progress beyond the checked general methods is claimed.

## Proof

### 1. Restricted order and the entire omitted spectral remainder

C999(7) says, on V0, b0>=R|V0-.02I=S_ref|V0.
S_ref is selfadjoint and closed on the full space, has form domain V
and satisfies S_ref>=beta I. Encode B0 by the selfadjoint relation
B_rel=B0 direct-sum the purely multivalued relation on H0-perp.
Its form domain is V0, and B_rel^-1=B0^-1P0. The cited form-order
definition checks both inclusion V0 subset V and the displayed form
inequality. Nonnegative inverse antitonicity therefore gives

    B0^-1P0 <= S_ref^-1                                (3)

as bounded operators on H. This is an inequality; it does not identify
a restricted inverse with an unrestricted inverse compression.

By spectral calculus, N=beta^-1 I-S_ref^-1 is bounded positive.
P_b reduces S_ref: it is outside the finite head and lies in the
diagonal D/2 complement. Hence it also reduces N, with
P_b N P_b=diag(w_n) on the band and
N-P_b N P_b=(I-P_b)N(I-P_b)>=0. This proves positivity of EVERY
omitted mode, including the entire head and infinite complement.
Applying(3) to rz in H0, for any z in C^3, proves the first line of(2).
No neutrality of P_b rz is needed: it is an ambient spectral piece,
not a trial vector in H0. No action of B0 on r_j is taken.

C999k's full complement has h(k_n)/2>3.07 for n>=512. Thus
h(k_n)/2-.02>3.05 and

    w_n>1000000/219999-20/61>4,       w_n<1/beta<5.     (4)

These bounds hold on the entire chosen band without an approximate
diagonal sign premise. They will also bound all weight/error products.

For the downstream ledger, every q_j lies in Dom(B0) by C999(3)
and exact neutrality. Expanding F=B0Q+r against the bounded positive
selfadjoint inverse gives, entry by entry,

    F*B0^-1F=Q*F+F*Q-Q*B0Q+r*B0^-1r.                 (5)

This verifies the needed C998e(14) finite-column identity, including
off-diagonal entries and both cross terms. In(5), B0 acts only on Q.
Replacing the last term by(2) is permitted; its remaining Gamma
charge has not been evaluated and cannot be deleted.

### 2. One fixed, complete coefficient service

The pre-evaluation prescription is preserved in
`drafts/2026-11-13-shifted-finite-band-attempt-701.md`.
The reference remains286/14, the band remains512:1023 and the witness
never changes. The auxiliary smooth integration grid is4096; E indices
14<=l<80 are evaluated and its entire suffix from80 is paid. The fixed
allowance is1/200 per band column, with1e-5 for new scalar/assembly
errors. No failed allocation, mesh tuning or band search occurred.

In each parity block C999z's bounded-operator identity gives EXACTLY

    S_app-S=h_286-h-sum_(l>=14) E_epsilon,l.            (6)

The complete original response S includes the Carleman term and every
response index, including0. Thus using(6) is a way of evaluating the
FULL singular action, not truncating it. On the band, Dq and delta q
vanish before projection, since q has support0:255. Therefore centers
for the unprojected g=Tf+T*h-B_trial q are formed as

    original response/forcing band
      - h_286 q + h_4096 q + sum_(14<=l<80)E_l q.      (7)

For a grid of M cells, h_M is C999z's midpoint kernel, with all M^2
products. Its action is computed using the exact cell integrals of
the finite cosine input and of each output cosine. In the t coordinate
these bases are Ue_n=sqrt(2)(-1)^n nu_n cos(k_n t) in their own parity
and zero in the other. A nonzero-frequency cell integral is
sqrt(2)(-1)^n nu_n[sin(k_n b)-sin(k_n c)]/k_n;
the zero-frequency integral is sqrt(2)nu_0(b-c).
Both parities are reconstructed with this same unitary normalization.

Only2M-1 distinct h values occur. They are evaluated at j*a/M,
1<=j<2M, from exp(-u/2)/(1-exp(-2u))-1/(2u), at80 Decimal digits.
There is no zero denominator: for M<=4096, u>=a/4096>1/16384.
The midpoint grid is for integration, and never changes S_app.
C999z's already proved smooth-kernel estimate gives

    ||h-h_4096|| <= (303/16)a^2/4096
                  < (303/16)(3/10)^2/4096 = eta_h.     (8)

The finite E sum in(7) includes all four products with their exact
even/odd denominator. For c=2l+1/2, e=exp(-ca), b=e^2 and a test
frequency k, put s=sin(ka),d=cos(ka),N=sqrt(2)(-1)^n nu_n. Its
two scalar integrals are

    p_n=N[c+e(-cd+ks)]/(c^2+k^2),
    z_n=N[e(cd+ks)-bc]/(c^2+k^2).                      (9)

Here s,d are exactly0,+1,-1 at ka=n*pi/2. The contribution is
[epsilon b p_n p_q+z_n z_q+epsilon p_n z_q+
epsilon z_n p_q]/(1-epsilon b), contracted with the SAME q
coefficients in every product. Formula(9) is direct finite integration;
no new transform theorem or asymptotic Fourier formula is imported.
The C999z suffix estimate, d0=1-exp(-a)>1/5 and
r0=exp(-2a)<2/3 imply

    ||sum_(l>=80)E_l|| <=18(2/3)^80=:eta_E.             (10)

It applies to the finite-cell correction in both parities, not to a
tail constant borrowed from the original residual in C999q Section5.
Equations(6)-(10) retain every forcing term and complete singular output.

### 3. Original entry errors, new arithmetic and exact projection

The script recomputes ALL512-by256 original S entries from C744w(11)
using its64-term digamma recurrence and full paid exponential suffix;
it computes both512-by18 forcing orientations, all16 shifts, and the
continuous prefix1:7 with its paid entire suffix. C744w/audit534's
full complementary analytic response error .000000181 bounds this
subrectangle in operator norm. Its elementary allowances are1e-7 per
S entry and2.1e-7 per T or T* entry, as in C999k(5).
All assembled entries are checked below400. Exact-neutral completions
are evaluated at80 Decimal digits then rounded; only their two low
coordinates can incur conversion error, whose total is below1e-12.
Every free dyadic and endpoint integer is read exactly. The script
checks each coefficient L1 norm below20 and each middle L2 norm below1.

Let s_f,s_h,s_q and n_f,n_h,n_q denote the saved rational upper
bounds for these coefficient L1 and L2 norms. They include1e-12 for
exact completion and norm conversion. Since sqrt(512)<23, the entire
original band error in column j is at most

    e_old=.000000181 n_q
       +23[1e-7 s_q+2.1e-7(s_f+s_h)]+.000001001.      (11)

The1e-6 covers every dot/addition under C744w's retained gamma ledger
(the current512 output rows are smaller than its65536-row allowance).
The extra1e-9 pays all exact-completion conversion through the bounded
operators; it exceeds(2*5+24.01)*1e-12. These are errors of the combined
response, not independent replacements of a repeated coefficient.

Here is an explicit ledger for the NEW arithmetic, rather than an
unpaid reserve. C744w(14)'s Taylor/range-reduction error bounds hold on
these smaller arguments. Normalization is below3, k_n>5 for n>0,
and the cell endpoint error is below1e-16. The difference-of-sines
formula above therefore has absolute error below1e-13 per basis-cell
integral: 3*2e-14(1+k_n)/k_n<=7.2e-14, with all remaining division,
normalization and input errors below1e-14. The zero mode satisfies the
same bound directly. Each h value has absolute error below1e-10 under
the retained Decimal contract; the minimum positive argument just
given controls both the denominator and removable-corner subtraction.
Its true magnitude is below12 by C999z(10) and a<.3.

For M=286 or4096 a computed input-cell integral has error at most

    d_M=21*10^-13+3*10^-12/M.

The first term pays all basis-integral errors times s_q<20. The second
pays completion conversion and the finite dot product, using
gamma_512<6e-14 and |Ue_n|<3. The sum of absolute exact input-cell
integrals is at most sqrt(a)n_q<.55, and its computed sum is below1.
The kernel action thus has per-cell error at most

    t_M=12M d_M+10^-10+2*10^-11.

Here gamma_(2M)<1e-12, and the absolute kernel dot sum is below12;
the last term dominates its rounding. Output-cell integral absolute
sums are below1, hence also below2 after rounding. True action
amplitudes are below12. The full512-coefficient smooth band error is
therefore at most

    b_M=23[2t_M+12M*10^-13+3*10^-11].                (12)

The last term pays the output dot product. The exact values are
b_286=868227/2500000000000 and
b_4096=12172497/2500000000000.

For(9), c<160,k<8192,c^2+k^2>800 and e,b<=1. Propagating
|delta k|<=8u k and the80-digit exponential conversion gives error
below1e-12 in each p_n,z_n, including the zero frequency; their
true magnitudes are below1 by the integral and Cauchy--Schwarz.
Each contraction against q has error below3e-11 (20*1e-12 plus
gamma_512 and completion conversion). For l>=14 the denominator
1-epsilon b>1/2, with b error below1e-14. Expanding all four
products gives per output/index error below5e-10: each product costs
at most(21*1e-12+3e-11) before division, and the denominator and
elementary arithmetic fit the remaining margin. Both signs are paid.
Thus all66 E indices cost at most23*66*5e-10 in band L2 norm.
The accumulation of66 terms and final additions cost less1e-8:
gamma_132<1.5e-14 against the coarse total absolute sum66*160,
followed by fewer than five additions of band values below1000,
gives less1e-8 after multiplication by23.

Consequently the ENTIRE new arithmetic allowance is bounded by

    b_286+b_4096+23*66*5e-10+1e-8
      =1870403/312500000000 <1e-5.                    (13)

This verifies the preset reserve; simply reserving it would not suffice.

It remains to pay the WHOLE projection. Let W span exp(x/2),exp(-x/2)
and G_w=[[exp(ell)-1,ell],[ell,1-exp(-ell)]]. For each band mode let
m_n be its exact pair of moments, from C999(8). The finite-rank
operator P_b(I-P0)=P_b W G_w^-1 W* has squared norm bounded by

    p^2=sum_(n=512)^1023 m_n*G_w^-1m_n.                (14)

Indeed this sum is its squared Hilbert--Schmidt norm, equivalently
the sum of ||(I-P0)e_n||^2. Each nonnegative summand is evaluated
from the exact2x2 inverse and moments with outward80-digit bounds;
det(G_w)>1/192 guarantees safe inversion. The saved rational square
root upper bound is p=412151/12500000000, larger than the exact
root. C998a's FULL operator norms give

    ||g_j|| <=5(n_f+n_h)+45n_q=:G_j.

Therefore the omitted projection from the unprojected center(7) costs
at most p G_j in the ENTIRE band. No moment is declared zero, no
tail of the projection is silently removed, and no new trial is formed.
Although this bound is deliberately conservative, it is small enough.

Combining(8),(10)-(14), the complete coefficient column error is

    epsilon_j=e_old+(eta_h+eta_E)n_q+pG_j+1e-5.         (15)

All exact rational terms are in the certificate's error_ledger.
They give epsilon_0<.001618,epsilon_1<.001357,
epsilon_2<.002072, each below the fixed1/200 allocation. In particular
the finite center Ahat satisfies ||A-Ahat||<=sqrt(sum epsilon_j^2)
<=147883723/50000000000=.00295767446=:e_op.
This bound includes all1536 coefficients simultaneously, all coefficient
couplings, full singular action, the forcing suffix and entire projection.

### 4. Weight and matrix enclosures; exact PSD test

The certificate saves EVERY Ahat entry as an exact binary64 dyadic,
each individual radius epsilon_j, and the stronger column L2 bounds
in(15). All512 weights are evaluated at80 digits with C999(19)'s
K=64 recurrence, analytic remainder sqrt(2)/[6(64.25^2+k_n^2/4)]
and outward elementary error. Monotonic inversion on the positive
denominator yields the two weight endpoints. Each saved center has
absolute error below1e-8, checked separately for all512 indices;
the complete individual radii are saved. Equation(4) independently
proves4<w_n<5 for error propagation and positivity.

The nine K center entries are formed EXACTLY as rational sums from
the stored coefficient and weight centers. With c_j>=||Ahat_j||,
their entry radii are

    10^-8 c_i c_j
      +5(c_i epsilon_j+c_j epsilon_i+epsilon_i epsilon_j). (16)

This expands the full coefficient error before taking absolute values;
it includes cross products and all weight errors. No eigenvalue sampled
from these entry centers is a premise of the sign certificate.

Instead use a stronger norm argument. Fraction arithmetic computes
the entire3x3 Ahat*Ahat from all512 rows and checks the three leading
principal minors of Ahat*Ahat-(1/125)^2 I strictly positive. Their
complete positive numerators/denominators are saved under
exact_PSD_certificate/center_gram_shifted_leading_minors; no rounded
determinant is used. Sylvester's criterion gives ||Ahat z||>=.008||z||
for complex z as well. Thus

    z*K_b z >=4||Az||^2
       >=4(.008-e_op)^2||z||^2
       =[63562617128340729/625000000000000000000]||z||^2.

The difference .008-e_op is strictly positive. Finally all96 integers
of X are used to compute X*X exactly, including its full zero extension.
The three leading principal minors of the rational matrix
4(.008-e_op)^2 I-10^-6 X*X are strictly positive. Its full matrix
and all three exact minors are saved under exact_PSD_certificate.
This proves the second line of(2), not merely a favorable numerical
eigenvalue or an entrywise-order comparison. The exact matrices and
minors were inspected in full for these load-bearing3x3 values.

Reproduce the fixed calculation with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/shifted-finite-band-701.py

It reads the entire pinned archive and witness, checks preservation of
every direct source artifact, and saves all coefficients, radii, weights,
nine matrix intervals, complete error ledgers and rational PSD evidence.
There are530 passing checks and no failures. The script verifies finite
arithmetic under the stated contracts; it does not audit the analytic
operator comparison or discharge the original source/core qualifications.
The separate critical review is recorded in Section5 below.

### 5. Separate conceptual audit — 13 November2026, step703

Invocation-start SPECIALIZE assessment702 covers this exact audit.
The primary inverse-order and spectral/representation cases in699/700,
and source comparison701/702, are reused without broadening their scope.
The fixed band, meshes, delta, beta, all762 free dyadics, all96 witness
integers and the complete reference are unchanged. Equations(1)-(16)
are upheld under their original qualifications. This is validation of
a local specialization, not a new bound beyond701 or a new general
theorem. Original source-to-Xi/core/operator contracts and c_* remain
unverified here.

**Order, domains and omitted pieces.** C999(3)/audit650 gives the
selfadjoint B0 on H0 and its strong-domain action. On H=H0 plus
H0-perp its graph direct-summed with {0} times H0-perp is selfadjoint;
its inverse is the everywhere-defined bounded B0^-1 P0. Its associated
form is b0 on V0. C999k Section2 defines the ENTIRE R, with form
domain V, including every diagonal complementary mode. Thus C999(7)
is precisely the form-domain inclusion and inequality required by
Behrndt et al. Proposition2.1 and the nonnegative inverse theorem.
The shift -.02 leaves lower bound beta>0. Inverting reverses the
order, giving(3), not the false identity with a compressed inverse.

The finite band is disjoint from the head and is a reducing spectral
subspace for S_ref. Functional calculus therefore makes N positive
on all H, and annihilates its cross blocks with this band. The
remaining operator (I-P_b)N(I-P_b) is positive on the head AND the
whole infinite complement. Applying this to rz requires only rz in
H0, not r_j in Dom(B0) or P_b r_j in H0. All q_j are finite exact
neutral cosine sums, hence strong-domain trials. Expanding F=B0Q+r
then proves(5) for every complex column combination with both cross
terms. C998e(14) is used only with this domain check; its full Gamma
term is still present.

**Full action and scalar formulas.** C999z/audit646 splits BOTH parity
operators into C_end/2+h+sum_(l>=0)E_l. Subtracting the fixed286/14
approximant gives(6); the singular term cancels in the difference,
while its entire action is already included in the original S
entries. The band has no unprojected (D-delta)q output. The unitary
image of e_n is sqrt(2)(-1)^n nu_n cos(k_n t) in its parity, so
integration against output and input cell indicators gives exactly
(7)'s h_M products, with no extra measure or factor of two.
Integrating exp(-ct)cos(kt) and exp[-c(2a-t)]cos(kt) gives(9).
The two cross products have the same epsilon sign and both are
present. The full suffix bound is C999z(4), with a<.3,
1-exp(-a)>1/5 and 1-exp(-2a)>1/3; its prefactor is below18.
It supplies(10) for both parities simultaneously.

The512-by256 original response rectangle uses C744w(11)-(13), lies
within its audited complementary rectangle, and contains no equal
frequency pair. Restriction cannot increase its .000000181 analytic
operator bound. All16 prime shifts and both signs of their delay
occur in the two forcing matrices. The continuous prefix1:7 and its
entire norm suffix are paid. Neither original-S tail constants nor
sampled residual values are substituted for the changed reference.

**Arithmetic audit, including correlated coefficients.** Let u=2^-53.
The exact moment-ratio completion from C999q is used for both
endpoints and the middle. Converting only its two base coordinates
has total L1 error below1e-12 for each column; all free coefficients
are exact dyadics. This was independently recomputed at100 digits.
The repeated q in every product is one vector: errors are bounded
by its full L1/L2 norm, never by assuming independent perturbations.
For the old matrix dots, three absolute dot sums total less24000
per row. gamma_512<6e-14, subsequent additions, and sqrt(512)<23
leave total error below1e-6. Completion conversion through S and
both T orientations costs less(24.01+5+5)1e-12<1e-9. This directly
justifies the rounding terms in(11) even with L1 norms up to20.

For the new sine integrals, grid endpoints in[0,.3] have error below
1e-16; |delta k|<=8u k and |x|<k*.3. The retained range-reduction
proof C744w(14) applies. After differencing, dividing by k>5 and
multiplying by normalization below3, its error plus all basic
operations is below1e-13. The zero mode is its constant integral.
The h scalars use u_grid>1/16384 and u_grid<.6; for example
1-exp(-2u_grid)>u_grid/2. Thus inverse denominators are below32768
and the removable-corner subtraction involves terms below16384.
At80 decimal digits, elementary propagation has error below1e-60
before binary64 conversion. Conversion of the result, of magnitude
below12, leaves ample room inside1e-10. Decimal precision alone is
not the justification: these denominator and absolute-size bounds
control its amplification, under the retained elementary contract.

For each parity separately, the exact input-cell absolute sum is
bounded by sqrt(a)||q||<.55 and the computed one by1. The per-cell
input error d_M in(12) pays basis errors with L1 mass<20; the dot
product costs at most gamma_512*60a/M<1.1e-12/M. Completion and
remaining basic operations fit its3e-12/M allowance. The kernel
dot has error at most12M d_M+1e-10+2e-11, since its absolute sum
is below12 and gamma_(2M)<1e-12. Output absolute sums are below2,
the exact action amplitude below12, and the final dot error below
3e-11. Combining the512 output rows proves exactly b_M in(12).
The direct sum of parities introduces no further factor of two.

For E indices14:79, c>=28.5 is exactly a half-integer,
c^2+k^2>800, k<8192 and the four trigonometric values are exact.
There is no range reduction at ka=n*pi/2. In(9), numerator absolute
term sums are bounded by2c+k, denominator relative errors by20u,
and normalization relative errors by8u. Allowing100u for all of
these effects gives an absolute error smaller than
100u*3(2c+k)/(c^2+k^2)+1e-60<3e-14, hence below1e-12.
The same bound covers z and the exponential/b conversion. Integral
Cauchy--Schwarz gives |p|,|z|<1 and their exact q contractions<1;
the more generous L1 bound20 proves the contraction error3e-11.
Expanding all four products with these errors, then using
1-epsilon b>1/2, gives less5e-10 per output/index, including the
denominator error. The accumulated66-term sum and final additions
satisfy the stated1e-8 band allowance. The rational sum(13) is
1870403/312500000000=0.0000059852896<0.00001.

**Projection, weights and independent finite evidence.** With the
first-slot-linear convention, the real moment formula C999(8) and
Gram matrix C998a(23) give exactly the summands in(14). They equal
||(I-P0)e_n||^2. Their sum bounds the squared operator norm of
P_b(I-P0), since its Hilbert--Schmidt norm squared is that same
trace. This pays the projection of the FULL g with C998a/audit655's
G_j, not merely its band or its smooth remainder. Each summand and
the total were recomputed independently; the prescribed p is an
upper bound. Weight denominators stay above3.05 throughout their
digamma remainder intervals. The scalar map t -> beta^-1-1/t is
increasing there, which verifies both interval endpoint directions.

Reproduce from the notebook with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/shifted-band-audit-703.py

The full audit is `scripts/separation-seven/shifted-band-audit-703.json`;
the unchanged calculation replay writes only
`scripts/separation-seven/shifted-finite-band-replay-703.json`.
It reproduces the entire701 JSON, not just the assertions. The
independent coefficient construction uses Machin pi,100-digit
Decimal scalars, direct neutral moment ratios, and a table of exact
phases n*j*pi/(2M) evaluated with45 Taylor terms after quadrant
reduction. This bypasses the original binary64 k*edge trigonometry.
It checks all149504 original S/T/T* entries, every basis-cell
integral on both grids, every E index and all1536 complete centers.
Column differences are below2.41e-15; this is a cross-check, not a
replacement for the analytic coefficient error ledger just audited.
All64 otherwise uncontracted powers3.**(-j) are checked against exact
rationals in the current runtime with relative error below2^-52.

All512 projection summands and weight intervals are recomputed at
100 digits with explicit1e-70 enlargements of the scalar intervals.
In these scalar expressions the smallest denominator is above1/192,
other divisions have denominators at least1/4 or3.05, intermediate
absolute values are below1e10, and fewer than10^4 operations occur
per row. Elementary propagation is below1e-80 under the retained
contract, so the enlargement dominates it. All18 rational input
norm bounds, every error-ledger term and all nine matrix intervals
are checked. The full3x3 matrices and all six exact positive minors
were inspected, with no truncated preview used as sign evidence.

Independent integer-scaled dot products reconstruct Ahat*Ahat,
the weighted K center and X*X; a recursive determinant computation
checks both triples of leading minors. The margin is exactly
1/125-e_op=252116277/50000000000>0. Thus the norm perturbation
and4<w_n give exactly the lower bound(2). For complex z the real
symmetric positive matrices act separately on Re(z) and Im(z),
so the real rational Sylvester checks imply the complex Hermitian
orders. Entrywise inequalities are never used for PSD. All1137
audit checks pass, no failures are recorded, and the original701
script/certificate and direct inputs retain their hashes.

This audit makes the fixed saving usable as a qualified input. It
does not evaluate Gamma, A_trial, a numerical upper debt E or the
signed remote term; it does not restore598, remove any previous
stop, or prove the full three-cell form. Independent higher/mixed
signs, C744q/H2, non-neutral coverage and actual-Xi transfer persist.

## Mathlib

Full matching coverage for the shifted non-dense restriction comparison
and this full frozen finite-band certificate has not been checked.
Closed-form representation, spectral calculus, Hilbert-space projections,
finite matrix algebra and the precisely cited inverse theorem are the
supporting mathematics. Unknown Mathlib coverage is not absence, and
neither formal verification nor a validated numerical runtime is claimed.
