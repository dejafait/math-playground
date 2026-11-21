# C999k: A complete reference metric pays the fixed546 inverse correction

## Hypotheses

Use the exact real f,g,h of C744z Section8, with ell=log(3)/2,
offsets0,7ell,14ell and denominator2^40. Their free integer arrays are
`scripts/separation-seven/response-prefix-direction-546.json`, SHA256
`f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013`.
Keep the original complete D,S,T,U, the moment map C, H0=ker(C), its
orthogonal projection P0, the form domain V and V0=V intersect H0,
and the restricted operator A0 from C744z Sections1-3. Write
W0=S+256C*C, L=D+W0, and b=P0Tf+K*h, K=P0T|H0.

The inherited analytic response identity and IEEE754/Decimal contracts
of C744v/w, the fixed-data audit in C744z Section9, and C999j's
particular strong-domain audit remain hypotheses. The neutral core and
restricted construction have not received an independent audit as a
whole; the original c_*=8.9e-18 source computation remains unreplayed.
This calculation does not replay that computation or replace the actual
inverse by a scalar c_* bound. The finite reconstruction estimate below
is used only to verify a finite head solve.

Import, without reproof, Behrndt–Hassi–de Snoo–Wietsma,
[*Antitonicity of the inverse for selfadjoint matrices, operators, and
relations*, arXiv:1403.5704v1](https://arxiv.org/pdf/1403.5704v1),
Sections2.1-2.3, Proposition2.1 p4 and Corollary3.5 p12 (including
Theorem3.4's nonnegative proof case p11). Nonnegative selfadjoint
relations admit inverse antitonicity in form order, including non-dense
form domains. For closed-form representation use Teschl,
[*Mathematical Methods in Quantum Mechanics*, GSM99, 12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorems2.13/2.18 pp71-72/77. The bounded Schur precedent is
[Dritschel–Rovnyak, arXiv:0903.3639v1](https://arxiv.org/pdf/0903.3639v1),
LemmaA.1 pp28-29; the elementary form comparison needed here is checked
explicitly below, rather than applying that bounded theorem directly
to an unbounded diagonal. These sources and this exact allocation were
approved in assessment553 before this research turn.

## Conclusion

Let P retain raw cosine modes0,...,511, Q=I-P, and Kcut=65536.
There is a completely specified positive reference form R, with head
H and complementary diagonal QDQ/2, such that R<=L on V. For the
full lifted residual rho=Tf+T*h-Lg,

    P0rho=r=b-A0g,
    <A0^-1r,r> <= <R^-1rho,rho> < .023083550 < .093538.       (1)

The complete fixed-trial energy, with the original remote U retained,
is in (.093538,.094207) by C744z's audited result. Consequently the
energy minimized over the whole neutral middle form domain satisfies

    Q_min(f,h) > .070454450 > .070454.                       (2)

This is a local REPRODUCTION/specialization, audited in Section6 under
the retained contracts, not a new general inverse theorem. It settles
only this fixed endpoint comparison
under the inherited contracts. Uniform endpoint signs, C744q margin,
strict H2 slack/existence, non-neutral coverage and RH remain open.
The earlier scalar/prefix stops are unaffected. This is not a complete
RH candidate. Section6 upholds (1) within exactly these qualifications.

## Proof

### 1. Exact moments, domains and the restricted relation

Write k_n=n*pi/ell, nu_0=ell^-1/2, nu_n=sqrt(2/ell) for n>0.
For c=+/-1/2, direct integration gives

    C_c(e_n)=nu_n c[(-1)^n exp(c ell)-1]/(1/4+k_n^2).

Within parity p=n mod2, the ratio C_c(e_n)/C_c(e_p) is

    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2),

independent of the choice of c. The exact definitions
u_p=-sum_(n>=2,n mod2=p) r_n u_n, for u=f,g, annihilate both
moments separately. Reflection h_n=(-1)^n f_n preserves neutrality;
all odd coefficients of g are exactly zero. These are algebraic
identities, not conclusions drawn from a small rounded moment residual.
In particular Cg=0, including every output of C*Cg.

The boundedness of S and C gives Dom(L)=Dom(D) and closed form
domain V, by the cited representation theorem and bounded perturbation.
The finite cosine g is in Dom(D) and V0. For v in V0,

    a0(g,v)=<Dg+Sg,v>=<P0(Dg+Sg),v>.

C999j's applicability check therefore gives g in Dom(A0) and
A0g=P0(Dg+Sg). T and T* are bounded; rho is in L2, and Cg=0
proves P0rho=P0Tf+P0T*h-A0g=r. Indeed K*=P0T*|H0 by the
definition of the adjoint of a compression. P itself need not preserve
neutrality, and no such claim is used.

Encode the restricted operator on the full separable L2 space by the
selfadjoint relation

    Arel={(v,A0v+w): v in Dom(A0), w in H0-perp}.

This is the orthogonal sum of the selfadjoint A0 on H0 and the purely
multivalued selfadjoint relation on H0-perp. Its nonnegative closed
form has domain V0 and value a0. Its inverse, defined on all L2, is
the bounded operator Arel^-1 y=A0^-1P0y: the H0 component determines
v uniquely, while w=P0-perp y. Thus

    <Arel^-1rho,rho>=<A0^-1r,r>.

Once R is proved positive below, its form domain V contains V0 and
its form value on V0 is at most that of L, which equals a0 there.
Proposition2.1 gives 0<=R<=Arel in relation form order, and
Corollary3.5 gives 0<=Arel^-1<=R^-1. This proves the first
inequality in(1) on the actual lifted rho. It is not an identity
between a restricted inverse and a projected unrestricted inverse.

### 2. Complete operator-order data and the fixed reference

Let Mhat and Chat be the exact dyadic matrices stored as `m0` and
`cov00` in the audited `scripts/separation-seven/complete-covariance-532.npz`.
Both are exactly symmetric; their pins agree with audit534. Chat
approximates B0*B0 for B0=Q_<W0P on rows512,...,65535, including
the response, moment penalty and their cross covariance.

C744w(12)-(16) gives

    ||PLP-Mhat|| < .000184+512*10^-7=.0002352<.00024,
    ||B0-B0hat|| <= e0
       =.000000181+sqrt((65536-512)*512)*10^-7
       <.000577175697,
    ||B0hat|| <= ||B0hat||_F < .586.

The complete covariance multiplication error is less10^-6 by the
audited blocked dot-product ledger. C744w(6),(8) gives for the ENTIRE
remaining W0 factor, including the penalty,

    ||Q_>=W0P|| < .062501+.000000906=.062501906.

The square of this sum bounds all its response/penalty cross terms.
Only the orthogonal output ranges Q_< and Q_>= allow exact splitting
of covariance. Consequently, in operator order,

    M_lower=Mhat-.00024 I <= PLP,
    (QW0P)*(QW0P) <= G_upper=Chat+.0046 I,               (3)

because the complete covariance error is at most

    (2*.586+e0)e0+10^-6+(.062501906)^2
       < .004584271302 < .0046.

Norm bounds on Hermitian differences imply(3); entrywise order is
never substituted for operator order.

With d0=6.14, define the exact rational head and reference by

    H=M_lower-(2/d0)G_upper
      =Mhat-.00024 I-(100/307)(Chat+.0046 I),
    R=H on P L2, and R=QD Q/2 on Q L2.                 (4)

No off-diagonal block belongs to R. Its form domain is V. For
x=Px,y=Qy in V, positivity of W0 and the audited raw complementary
bound QDQ>=d0 Q give

    <L(x+y),x+y>
      >=<PLP x,x>+2Re<QW0Px,y>+<Dy,y>
      >=<PLP x,x>-(2/d0)||QW0Px||^2
                         +<Dy,y>-(d0/2)||y||^2
      >=<Hx,x>+(1/2)<Dy,y>.

The middle line is the elementary squared-norm/Young inequality;
every term exists on V because W0 is bounded. This proves R<=L
on the full form domain, not merely on finite vectors.

For positivity, the script proposes a binary64 triangular F for
H-.24I and checks its full reconstruction. Its observed Frobenius
residual is below5.94e-14, ||F||_F^2<2806, max|F_ij|<20 and
max|Hhat_ij|<400. Under the inherited arithmetic contract, including
assembly of H from its exact dyadic/rational definition, the exact
reconstruction error is below10^-6. Hence H>=.239999 I. This is
a verified finite factor statement, not a sampled eigenvalue. The
complement has h(k_n)/2>3.07 for all n>=512. R is therefore closed,
positive with bounded inverse, and (4) gives its inverse by the
finite H inverse and diagonal weights2/h(k_n). The finite number
.239999 is used solely in the error bound for that finite solve;
no replacement scalar bound for A0^-1 is used or claimed.

### 3. Complete finite residual and verified head inverse action

Use the exact coefficient intervals from the algebraic formulas in
Section1. The new script encloses pi by Machin's formula with80 terms,
ell by widened Decimal ln, and all operations at70 directed digits.
Each rounded coefficient vector has L1 conversion error<10^-14;
the exact coefficient L1 norms are each<10. Their sharper values are
approximately3.630312,3.483220,3.630312 for f,g,h.

The head residual center is

    rhohat_P=(Mc+Mg)fhat+(Mc+Mg)^t hhat-Mhat ghat.

For every complementary row512<=n<65536, regenerate the complete
W0,Wc,Wg entries by C744w's audited formulas and use

    rhohat_n=[(Wc+Wg)fhat+(Wc-Wg)hhat-W0 ghat]_n.

Here Wc=(T+T*)/2,Wg=(T-T*)/2. Both distinct orientations occur.
The response uses its full digamma-based sum, its retained exponential
part and the paid analytic remainders; it is not S_32. The true moment
penalty vanishes, but all rounding in its evaluated entries is paid.
Dg has no complementary coefficient. Every combined output is formed
before squaring. No covariance between its three terms is omitted.

Put s_u=||u||_1 in coefficient space and n_u=||u||_2. The entry
contracts and the head/response operator bounds give

    ||P rho-rhohat_P|| <= delta_P
      =.00024 n_g+sqrt(512)*2.1e-7(s_f+s_h)+10^-6
      <.000377785216,
    ||Q_<rho-rhohat_<|| <= delta_<
      =.000000181 n_g+sqrt(65024)
          [10^-7 s_g+2.1e-7(s_f+s_h)]+10^-6
      <.000478882900.                                  (5)

The first head term bounds the full matrix error for g. The other
terms follow by bounding each row against the coefficient L1 norms,
then taking the L2 norm; the complementary analytic response error
uses its audited Frobenius/operator norm. These are bounds on the
combined residual error, so its unknown mixed terms are retained by
the triangle inequality.

For explicit arithmetic control of the added10^-6: all stored/generated
W0,Wc,Wg entries have modulus<400, checked in every row block. Thus
each entry of Wc+/-Wg is at most800 in modulus before its addition
roundoff. The absolute dot-product sums over all three terms in one
row are below20000.1, since s_u<10 and conversion errors<10^-14.
The standard gamma_1024<1.2e-13 gives row error<2.401e-9. Coefficient
conversion, forming Wc+/-Wg and adding the three dot products contribute
less4e-11 per row. Multiplication by sqrt(65536)=256 is below6.3e-7,
hence below10^-6 for either range. This allowance is separate from
the entry errors in(5); no unverified BLAS accuracy is presumed.

Similarly the factor-product gamma bound is at most
gamma_1024||F||_F^2<1.2e-9, even with the coarse upper bound10000.
Rational H assembly and reconstruction subtraction add less10^-8 in
Frobenius norm using512 by512 entries bounded by400. Norm-evaluation
roundoff is smaller. Together with the observed residual<10^-7,
this justifies the deliberately loose10^-6 reconstruction allowance
used in Section2.

Let y be the stored proposed finite solution Hhat y=rhohat_P. Its
correctness is not assumed: calculate the exact rational H times y
entry by entry with directed Decimal intervals. The full solve
residual satisfies

    e=||rhohat_P-Hy|| <2.397e-16.

For the actual p=P rho, finite square completion gives

    <H^-1p,p>=2Re<y,p>-<Hy,y>
                    +<H^-1(p-Hy),p-Hy>.

Using (5) and the verified finite reconstruction bounds this by

    2<y,rhohat_P>-<Hy,y>+2||y||delta_P
                     +(e+delta_P)^2/.239999
      < .018353622422.                                 (6)

All scalar pairings in(6), including H's exact rational action, are
accumulated outward. No floating Cholesky success or solve success
alone certifies this inverse action.

### 4. Every weighted complementary output and the infinite tail

For all n>=512, C744v's digamma bound gives

    h(k_n)>=d_n=log(n/(2ell))-2ell^2/(9n^2)>6.14.

The lower comparison d_n is increasing: its derivative as a real
function is1/n+4ell^2/(9n^3)>0. With the complete combined residual
rows, compute by directed arithmetic

    W=sum_(512<=n<65536) 2|rhohat_n|^2/d_n.

The actual reference inverse action on this output range is at most

    [sqrt(W)+sqrt(2/6.14)delta_<]^2 < .000496932349.     (7)

This is the weighted L2 triangle inequality, including the mixed
product of the center and error. The certificate saves every row
center in its binary artifact and every lower diagonal endpoint in
its JSON; all65024 positive-denominator checks pass.

For the entire remaining output n>=Kcut, C744w(6)-(7)'s entry bounds
give, for m<512,

    |S_nm| <=1/n+B/n^2,
    |J_nm|,|J*_nm| <=2a/[pi(n-511)],
    B=4ell[1+(3/2)3^(-1/4)]/pi^2,
    a=sum_(p^j in P7) log(p)/sqrt(p^j)<7.653879.

Opposite-parity S entries are zero; using the displayed bound for
all entries only enlarges it. Integral comparison gives
sum_(n>=Kcut)n^-2<=1/(Kcut-1) and
sum_(n>=Kcut)(n-511)^-2<=1/(Kcut-512). For the whole continuous
part of T and T*, use the same complete norm kappa from C744v(2),
not a truncated continuous kernel. Thus

    ||Q_>=rho|| <= t
      =(2a/(pi sqrt(Kcut-512)))*(s_f+s_h)
       +((1+B/Kcut)/sqrt(Kcut-1))*s_g+kappa(n_f+n_h)
      < .152557058938.                                 (8)

The prime, response and continuous contributions are separately less
.138739036289, .013606530469 and .000211492181. The total bound in(8)
uses their full directed intervals before rounding these three displays.

Here Dg has exactly zero output, and Cg=0 removes the true penalty
identically. Its covariance in the reference construction has not
been removed. Squaring the SUM in(8) bounds all cross terms between
the two prime orientations, both continuous orientations and Sg;
it is not a sum of their squared norms. Consequently the full
remaining weighted action satisfies

    sum_(n>=Kcut) 2|rho_n|^2/h(k_n)
      <=2t^2/d_Kcut < .004232994969,
    d_Kcut >10.9963070613268.                           (9)

The three output ranges are orthogonal for R^-1, which has no
head/complement cross block and a diagonal complement. Adding the
full directed bounds(6)-(9), before rounding their displays, gives

    <R^-1rho,rho> <= .023083549738960240411711935367578756797
                   < .023083550.

The displayed longer endpoint is rounded upward. C999j's residual
identity says Q_actual-Q_min=<A0^-1r,r>. Combine the relation
comparison, this bound and C744z's strict Q_actual>.093538 to get
Q_min>.0704544502610397595, proving(1)-(2). The full U pairing is
included in Q_actual; its absence from rho is because it has no
middle variable, not because its energy is discarded.

### 5. Reproduction and limitations

From the notebook run

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/fixed-block-metric-555.py

Full certificate: `scripts/separation-seven/fixed-block-metric-555.json`.
Full factor, proposed solution, head approximation and all65536 residual
centers: `scripts/separation-seven/fixed-block-metric-555.npz`.
The JSON includes exact direction/source pins, every coefficient interval,
complete H times y, all output block checks, diagonal lower endpoints,
tail and arithmetic allowances, thresholds, qualifications and failures.
There are65175 passing checks and no failures. The three upper
contributions, total, exact solve residual, reference-order debt and
complete tail were inspected in full at their selected JSON fields.
These are upper-bound expressions, not two-sided enclosures of the
actual inverse correction. The lower endpoint of an interval for such
an expression is not a lower bound on that correction.

The finite reconstruction and vector arithmetic use precisely the stated
IEEE754 contract; directed elementary operations use the retained Decimal
contract. Successful execution is not formal verification of either
runtime. All earlier artifacts are preserved. No separation, trial,
fraction, penalty or cutoff was retuned. Independent conceptual review
of the relation direction, form domains, complete covariance, tails and
numerical ledger was the next requirement at step555; Section6 records
its separate completion.

### 6. Independent conceptual audit — 12 November2026, step557

**Scope and result.** The approved assessment555 is reused unchanged.
The complete fixed546 upper bound in(1) is upheld. This is verification
of a local standard-method specialization, not a new inverse theorem,
endpoint-uniform sign or RH candidate. N512/K65536, fraction1/2,
penalty256, the direction hash, and all original artifacts are unchanged.
The inherited response, IEEE754/Decimal, whole-core and unreplayed c_*
qualifications remain; the audit does not silently promote them to
independently verified results.

**Relation and form domains.** The two exponential moments have the
same coefficient ratio separately in each parity, proving the exact
neutrality used in Section1. Reflection preserves their common kernel.
Finite g lies in Dom(D)=Dom(L); testing against all V0 gives its
representing vector P0(Dg+Sg), without requiring invariance of H0 under
D+S. Cg=0 and the compressed adjoint identity therefore give P0rho=r.
The orthogonal relation sum in Section1 is selfadjoint and nonnegative;
its inverse is defined everywhere because A0 is uniformly coercive on
H0. Solving its graph equation gives exactly A0^-1P0, including its
zero action on H0-perp. The inverse pairing is thus the required
restricted pairing, not an unrestricted inverse substitution.

For R the domain is V; for Arel it is V0 subset V. On V0 the moment
penalty is zero. Section2's full-domain Young estimate has coefficient
2/d0 on ||QW0Px||^2 and consumes only d0||y||^2/2. Since QDQ>=d0Q,
it leaves at least half the full complementary diagonal. Positivity of
W0 supplies the omitted nonnegative QW0Q term. Thus R<=Arel in exactly
the cited Proposition2.1 form-order sense. Corollary3.5 reverses this
order for inverses. No closed-range assumption on raw P or preservation
of H0 by P is inserted. These are applicability checks of the cited
theorems, not reproofs of them.

**Complete covariance and residual.** The finite covariance is for
W0=S+256C*C, with its response/penalty cross products present. If Bhat
has error e0 and norm below .586, expansion of B*B-Bhat*Bhat gives
operator error at most (2*.586+e0)e0. Add the complete stored-product
allowance and the squared SUM of the two far-tail norm bounds. The
result remains below .004584271302<.0046. Orthogonality is used only
between the two output ranges. Together with the head allowance
.0002352<.00024 this proves both operator orders in(3).

The head uses T and its transpose; every other finite row uses Wc+Wg
and Wc-Wg separately. Both correspond to the exact signed translation
formulas in C744w, including their continuous parts. All residual terms
are combined before squaring. Equation(5)'s matrix/operator errors and
coefficient L1 errors dominate the complete row errors. The arithmetic
allowance also checks out: with entries bounded by400 and each L1 norm
below10, the three absolute dot sums are below20000.1; the gamma_1024
bound and conversion/addition charges give a total norm error below
6.3e-7<10^-6 over at most65536 rows. These statements retain the stated
binary64 contract. The finite inverse-error floor is used only for H.

**Independent arithmetic evidence.** Reproduce from the notebook with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/fixed-block-metric-audit-557.py

Full certificate: `scripts/separation-seven/fixed-block-metric-audit-557.json`.
The separate90-digit replay has basename `fixed-block-metric-replay-557`
and saves its py/json/npz/log in that directory. It regenerates every
residual row and all original checks; the full head, factor, solution
and65536 residual centers agree bit for bit. Every source/binary pin
and original file hash is checked before and after the audit.

The independent arithmetic reuses audit552's110-place integer outward
interval implementation, whose operations were read. Its ell uses the
positive atanh(1/2) series with its complete geometric remainder, pi
uses Machin's alternating series, and square roots use integer isqrt.
The complete1536 coefficient intervals nest in the original enclosures;
all coefficient conversion allowances are independently checked.
For logarithms the audit retains the correctly rounded Decimal contract:
130-digit endpoint logarithms are widened by one neighbor and converted
outward to the integer grid. Input conversion here is exact, since the
finite decimal arguments have fewer than130 significant digits.

The exact rational head is independently reconstructed as

    H=Mhat-(100/307)Chat-[6671/(307*12500)]I.

All512 entries of Hy are accumulated with exact integer dot products
over common dyadic/rational denominators and lie in the original saved
enclosures. The solve residual remains below2.397e-16. Every entry of
FF^t is also accumulated as an exact integer dot product. Squaring and
summing the full rational reconstruction residual gives

    ||H-.24I-FF^t||_F < 4.49e-14 < 10^-6.

This verifies H>=.239999I without trusting Cholesky success or a
floating reconstruction. Its squared numerator, common denominator and
the complete exact Hy numerator vector are saved. The finite square
completion and error terms in(6) are then independently enclosed.

All65024 complementary denominators are checked individually against
their saved lower endpoints and6.14, and the complete weighted sum
is reaccumulated. The output-block ranges partition512,...,65535
exactly. In the far tail, the translation bound applies to each
orientation, the response bound covers both parities, Dg vanishes,
and exact Cg=0 removes the true penalty. The entire continuous norm
is charged twice through n_f+n_h. Integral comparison from K-1 and
K-512 covers every n>=K. Squaring the total t before applying2/d_K
retains all mixed terms. Monotonicity of d_n justifies that common
tail weight. Independent enumeration checks all16 separation7 powers.

The independent upper bounds are, rounded outward,

    head < .018353622422,
    modes512,...,65535 < .000496932349,
    entire n>=65536 tail < .004232994969,
    total < .023083549738960240411711935367578756797.

The total is checked using full endpoints, not the sum of these rounded
displays; it is at most the original saved upper endpoint and strictly
below .023083550<.093538. All67152 audit checks pass, with no failures.
Full selected summary/head/tail/reconstruction evidence was inspected.
Intervals for upper-bound expressions are checked by upper domination,
not misinterpreted as two-sided enclosures of the actual correction.

Finally U is retained in C744z's audited Q_actual. It has no middle
variable and therefore no residual term. The residual identity gives
Q_min>.070454450 for these endpoints and the entire neutral middle
form domain. No uniform endpoint bound, C744q margin, H2 control,
non-neutral sign or global assembly follows. The fixed audit is complete;
changing its endpoint family or comparison mechanism requires its own
assessment.

## Mathlib

Full matching coverage for this non-dense relation comparison and the
fixed complete inverse-error certificate has not been checked. Closed
forms, Hilbert-space inequalities, finite matrix algebra and the named
source theorems are supporting mathematics; no full Mathlib formalization
or verified numerical runtime is asserted. Unknown coverage is not
evidence of absence.
