# C999p: Full middle residual payment for the frozen original trial

## Hypotheses

Use exactly C999n's frozen endpoint free integers on modes512:1023,
divided by2^40, and C999o's archived `middle_free_dyadic` on free
modes2:1023. All other free endpoint coefficients vanish. Define the
two low coefficients of EACH vector by C999m(1)'s exact moment ratios,
not by its saved rounded lows. The archive specifying the trial is
`scripts/separation-seven/original-galerkin-586.npz`, SHA256
`44f97e4dfd0b51ee97e907abb6f6cd9432d288f65165b255319f7a16a87c407d`.
Both endpoint integer arrays are checked against C999n's original
manifest and frozen archive. No endpoint, trial or dimension is chosen
again in this calculation.

Use ell=log(3)/2, k_n=n*pi/ell, and the complete D,S,T,T*,U and
moment map C of C744v/w/z. Put L=D+S+256C*C, H0=ker(C),
V0=V intersect H0, and let A0 be the restricted closed-form operator.
The reference R is EXACTLY C999k's: raw head0:511 equal to its
specified rational H, diagonal h(k_n)/2 on modes n>=512, with no
off-diagonal block. The output split stays K=65536. In particular
H>=.239999 I, R is positive with bounded inverse, and R<=L on V.

Retain C744v/w's analytic response and IEEE754/Decimal contracts,
C744z's whole-neutral-core qualification, and its unreplayed
c_*=8.9e-18 source computation. C999o's separately audited original
energy enclosure is an input. No RH, H2, uniform endpoint sign,
quarter allocation or new scalar bound for A0 is assumed.

The standard inputs are imported, without reproof, from Teschl,
*Mathematical Methods in Quantum Mechanics*, GSM99 author version,
12February2009, Theorems2.13/2.18, printed pp71-72/77,
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
and Behrndt–Hassi–de Snoo–Wietsma, *Antitonicity of the inverse for
selfadjoint matrices, operators, and relations*, arXiv:1403.5704v1,
Proposition2.1 p4, Theorem3.4's complete nonnegative case p11 and
Corollary3.5 p12,
[primary PDF](https://arxiv.org/pdf/1403.5704v1).
Their applicability to the unchanged reference and arbitrary finite
neutral trials is C999k Sections1/6 and C999l(5). Assessment588,
separately approved589, licenses this fixed SPECIALIZE calculation,
classified REPRODUCTION. No source-level novelty is claimed.

## Conclusion

**Step592 conceptual audit:** Section6 upholds the step590 calculation
under the unchanged stated contracts. The complete lifted residual

    rho=Tf+T*h-Lg

satisfies

    <R^-1rho,rho> < .000760912 < .42328427.                 (1)

For these same frozen endpoints, minimizing over the ENTIRE complex
neutral middle form domain gives

    inf_(v in V0) Q_actual(f,v,h) > .42252335.              (2)

This local comparison extends the finite-middle calculation to unrestricted
neutral middles for ONE endpoint pair. Other endpoint directions, an
all-direction endpoint complement, C744q margin, H2 slack/existence,
non-neutral coverage and global actual-Xi positivity remain open.
This is an audited local REPRODUCTION, neither a full RH candidate nor
a new general inverse theorem.

## Proof

### 1. Exact vectors, strong residual and inverse comparison

Let nu_0=ell^(-1/2), nu_n=sqrt(2/ell) for n>0. For p=n mod2 set

    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2),
    u_p=-sum_(2<=n<=1023, n mod2=p) r_n u_n,

for each u=f,g,h. Integrating against exp(c x), c=+/-1/2,
gives C_c(e_n)=nu_n c[(-1)^n exp(c ell)-1]/(1/4+k_n^2).
The ratio of this to C_c(e_p) is r_n for BOTH c. Thus every
vector is exactly neutral, with no symmetry relation between endpoints
and no parity restriction on g. In particular Cg=0 algebraically.
All three vectors have finite raw support0:1023 and belong to Dom(D)
and V0. The strong-trial argument of C999j gives

    g in Dom(A0), A0g=P0(D+S)g,
    P0rho=P0Tf+P0T*h-A0g.

It uses the closed-form pairing against every v in V0 and bounded S;
neither invariance of H0 nor causal-generator domain membership is needed.
Bounded T,T* implies rho is in L2. C999k's relation-order comparison,
equivalently C999l(5)'s arbitrary strong-trial specialization, gives

    Q_min(f,h) >= Q_actual(f,g,h)-<R^-1rho,rho>.            (3)

Here Q_min is the infimum on V0; inherited coercivity also ensures its
minimizer. The inverse relation encodes A0 on H0 and the multivalued
part H0-perp. Its inverse is A0^-1 P0, not a projected unrestricted
inverse identity. The positive R comparison has form domain V containing
V0, so the cited nonnegative inverse antitonicity applies. It requires
no Galerkin equation for this g.

### 2. New rectangular entry and coordinate bounds

The pinned C999o archive supplies the complete local M=D+S and both
T orientations on raw0:1023. Its audited bounds are .0001 per local
entry and .000001 per cross entry. For outputs1024:65535, regenerate
the complete response and both T orientations by C744w(11)-(14),
using ALL input columns0:1023. There is no equal-index case outside
the saved square. At zero input frequency b(0)=0. Opposite-parity
response entries vanish. Both delay signs use their respective shift
formula. Include the seven continuous terms, with their entire remaining
operator norm charged as in C744w. No U calculation is needed here:
its full signed energy is already retained in C999o's energy input.

Here is an explicit new-range error bound, rather than a transfer of
any old512-column operator norm. For distinct n,m in this rectangle,

    (n^2+m^2)/|n^2-m^2|
       <=(1024^2+1023^2)/(1024^2-1023^2)<1024.

For fixed larger n the ratio increases with m; for fixed m it decreases
with n. For the saved square the maximum distinct pair is1023,1022,
which has a smaller ratio. Thus this covers the entire rectangle.
Its largest output frequency and shift argument are no larger than
C744w's originals: |k_n delta|<207000 and |n-m|>=1. All constants,
recurrence length, elementary polynomials and scalar normalization
bounds are unchanged. Consequently C744w Section4's ELEMENTARY
entry allowance1e-7 continues to apply; its accumulated matrix norms
do not transfer. New exponential constants are generated at80 Decimal
digits and rounded once, as required by that ledger.

For the analytic response error, let

    rmax=sqrt(2)/(6*64.25^2)<.000057097552.

C744w(12) gives r(k)<=rmax. For unequal frequencies its normalized
error is at most

    nu_n nu_m [k_n r(k_n)+k_m r(k_m)]/|k_n^2-k_m^2|
       <=(2/ell) rmax/|k_n-k_m|
       <=2 rmax/pi < .000036349431.                       (4)

The zero-frequency case satisfies the same inequality; opposite parity
only decreases it. Equal indices are confined to the saved square.
With Jdiag=65536 and c=131072.5, C744w's equal-index remainder is

    c^-2+2 k_1023^2[(6c^3)^-1+c^-4]<5.125617e-9.

Normalization2nu_n^2<8 bounds its contribution. D's analytic error
is at most rmax; D occurs only in that saved square. Adding these
nonnegative bounds and the elementary allowance yields

    epsilon_local <= rmax+2rmax/pi+8*5.125617e-9+1e-7
                   < .000093587987 < .0001.

The overestimate also covers symmetrization of the saved local matrix.
Both complete T orientations retain the .000001 entry allowance:
all sixteen prime shifts have the same scalar cancellation/argument
bounds and the same seven continuous terms/full suffix as C744w.
No old accumulated Frobenius allowance is used for1024 inputs.

Directed70-digit intervals using the80-term Machin enclosure for pi
and widened Decimal ln enclose the exact moment ratios and all
coefficients. The exact coefficient L1 norms obey

    s_f<1.441497349, s_h<1.441499682, s_g<.511202650.

Conversion L1 errors against the pinned raw centers are respectively
<2.883e-23, <1.428e-23, <1.560e-22. The proof uses the looser
<1e-14 for each. The exact free middle dyadics are unchanged.

### 3. Complete finite residual and the verified head inverse action

On outputs0:1023 form

    rhohat=That fhat+Tshat hhat-Mhat ghat.

This includes the ACTUAL Dg on512:1023. The comparison lower diagonal
is not substituted for D. On1024:65535 use the newly generated S,T,T*
entries; Dg is then zero. Since Cg=0, no true penalty remains on any
output, though the penalty remains in R's construction. Combine all
three terms in each row before squaring.

All saved/generated entries are finite and bounded in modulus by400,
checked in every block. With s_f+s_h+s_g<6, a dot-product ledger has
absolute product sum<2400 per row. Gamma_2048<2.3e-13 bounds the
1024-term dots and the final three-term addition. Coordinate conversion
adds at most400 times the sum of the three L1 errors. Including
an extra1e-11 per row, multiplication by sqrt(65536)=256 gives
norm error<1e-6. Thus the complete residual errors on the orthogonal
raw head P=0:511 and complement Q_<=512:65535 obey

    delta_P=sqrt(512)[.0001 s_g+.000001(s_f+s_h)]+1e-6
            <.001222954328,
    delta_<=sqrt(65024)[.0001 s_g+.000001(s_f+s_h)]+1e-6
            <.013771725913.                                (5)

These bounds combine all entry errors before use, paying every unknown
cross term by the norm triangle inequality.

Let y be the saved dyadic proposed solution to Hhat y=rhohat_P.
H remains EXACTLY m0-.00024 I-(100/307)(cov00+.0046 I), using
C999k's audited exact dyadic m0,cov00. Evaluate its full action on
y entry by entry with directed Decimal rational arithmetic. This gives

    e=||rhohat_P-Hy||<7.046e-20, ||y||<6.787e-7.

The full reconstruction check for the unchanged reference factor
also agrees with C999k: observed error<5.941e-14 and factor norm
squared<2806. C999k's complete rounding allowance<1e-6 gives the
finite floor H>=.239999 I. A solve success flag is not evidence of
inverse accuracy. The exact square completion gives

    <H^-1P rho,P rho>
       <=2<y,rhohat_P>-<Hy,y>+2||y||delta_P
                         +(e+delta_P)^2/.239999
       < .000006233438.                                    (6)

The center quadratic and every scalar in this inequality are evaluated
outward, including H's exact rational action.

### 4. Every complementary output and the entire infinite tail

For all n>=512, C744v gives h(k_n)>=

    d_n=log(n/(2ell))-2ell^2/(9n^2)>6.14.

The comparison d_n is increasing, since its derivative is
1/n+4ell^2/(9n^3)>0. Every finite denominator is checked positive.
Directed accumulation of the complete combined rows gives

    W=sum_(512<=n<65536) 2|rhohat_n|^2/d_n
       < .000021511664.

The weighted triangle inequality therefore proves

    sum_(512<=n<65536) 2|rho_n|^2/h(k_n)
       <=[sqrt(W)+sqrt(2/6.14)delta_<]^2
       < .000156200153.                                    (7)

For n>=K=65536 and EVERY m<=1023 the response argument in
C744w Section2 still gives |S_nm|<=1/n+B/n^2, where

    B=4ell[1+(3/2)3^(-1/4)]/pi^2<.476363475.

Indeed discard c_j^2/(c_j^2+k_m^2)<=1 in the non-exponential sum,
and bound the exponential addition by its geometric sum; this bound
is independent of m. Opposite parity gives zero and is safely included.
For either delay sign the full normalized prime-shift entry is at
most2/[pi(n-m)] by C744w's overlap antiderivative, so it is at
most2/[pi(n-1023)]. Put a=sum_(p^j in P7) log(p)/sqrt(p^j)
<7.653878168. Integral comparison now gives

    sum_(n>=K)(n-1023)^-2 <=1/(K-1024),
    sum_(n>=K)n^-2 <=1/(K-1).

Using the same COMPLETE continuous norm
kappa=1/[2187 sqrt(3)(5/2)(1-1/729)] for each orientation, we obtain

    ||Q_>=rho|| <= t
      =2a(s_f+s_h)/(pi sqrt(K-1024))
          +(1+B/K)s_g/sqrt(K-1)+kappa(||f||+||h||)
      < .057363107981.                                     (8)

The three contributions are respectively<.055307701463,
<.001996915100 and<.000058491419. Their unrounded directed SUM
is used before squaring. Dg has zero tail output and Cg=0 exactly;
no hidden penalty tail is discarded. Both T orientations, their
continuous tails, Sg and every cross term are paid by this one norm
bound. Since d_K>10.9963070613268,

    sum_(n>=K) 2|rho_n|^2/h(k_n) <=2t^2/d_K
       < .000598478406.                                    (9)

Only the three DISJOINT output ranges allow orthogonal addition for
R^-1. Adding the directed, unrounded bounds(6)-(9) gives

    <R^-1rho,rho>
      <=.0007609119949026642043418172708431
       <.000760912.

The longer displayed endpoint is rounded upward. C999o's audited
full original energy is strictly greater than .42328427. It includes
all sixteen separation7 powers and334 separation14 powers, U's exact
zero shift2187, both orientations and entire continuous responses.
U is absent from rho because it contains no middle variable, not
because any endpoint energy is omitted. Equation(3) consequently gives

    Q_min(f,h)>.42328427-.0007609119949026642043418172708431
             >.42252335,

as asserted. C999n's negative reference-minus-quarter result and the
earlier scalar/symbol/quarter stops are unchanged.

### 5. Reproduction and audit boundary

From the notebook run

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/frozen-full-residual-590.py

Full certificate: `scripts/separation-seven/frozen-full-residual-590.json`.
Every combined finite output, proposed head solution and factor are in
`scripts/separation-seven/frozen-full-residual-590.npz`. The certificate
saves all exact coefficient intervals, every positive diagonal bound,
each full H-action interval, complete scalar debts, all checks, pins
and failures. All65188 checks pass. This is supporting evidence for
the written bounds, not a substitute for their hypotheses or proof.

The initial successful executable is preserved as
`frozen-full-residual-initial-590.py` in that same script directory.
Before finalization its floating integer-power constants were replaced
by80-digit Decimal constants rounded once, to implement the stated
elementary contract explicitly. This is no parameter or trial change.
The final enclosure above uses that corrected implementation; its scalar
bounds agree with the initial run's reported output. Extra copies named
`frozen-full-residual-final-snapshot-590.json/.npz` are final-artifact
snapshots, not independently generated evidence. Original input artifacts
are unchanged. No mathematical case was dropped.

The step590 calculation required a separate conceptual audit of its new
rectangular ledger, all-index tail specialization, exact-trial applicability
and certificate action. Section6 completes that audit. No new general
theorem is reproved, no all-endpoint sign is inferred, and no RH resolution
is proposed.

### 6. Separate conceptual audit — step592, 12 November2026

Invocation-start SPECIALIZE assessment590, approved separately591, covers
exactly this audit. The endpoints, middle free dyadics, neutral completion,
reference R, head, support and output split are unchanged. The primary
theorem coverage recorded588/589 is reused; no new theorem hypothesis or
source discovery is needed. This is REPRODUCTION under all qualifications
in the Hypotheses, not progress beyond the inspected sources on RH.

**Form and variational direction.** Each parity ratio in Section1 is
the same for both exponential moments, so the exact low coefficients
annihilate C for all three profiles. The saved floating lows are centers
only. Finite raw support puts g in Dom(D). Bounded S and the closed-form
pairing against every v in V0 give g in Dom(A0) with A0g=P0(D+S)g.
This remains valid for complex v. The closed restriction is represented
on H0 under the inherited core qualification, using the cited Teschl
theorems; no invariance of H0 under D is needed.

The exact reduction from the trial energy is
<A0^-1 P0rho,P0rho>. C999k's unchanged form R has domain V containing
V0 and satisfies R<=a0 there. The selfadjoint relation with operator
part A0 and multivalued part H0-perp has inverse A0^-1 P0 on the full
space. Proposition2.1 and Corollary3.5 of the cited Behrndt et al. version
therefore imply the correct inverse upper comparison (3). No compressed
unrestricted inverse identity, exact Galerkin equation or real-only
minimization is assumed. The upper comparison holds for this arbitrary
specified strong trial and the infimum over the entire complex V0.

**Every scalar-entry case.** For n>=1024, m<=1023, the denominator
ratio is maximized at(1024,1023), where it is
1023.5002442598926 or less. For unequal indices in the saved square
the maximum is smaller. The frequency gap, normalization and maximum
shift argument thus retain C744w Section4's scalar arithmetic caps.
This verifies the new rectangle directly, without transferring a
512-column operator error. At m=0 the non-exponential b(0) is exactly
zero. The same-parity response formula and the exact zero for opposite
parities are applied before matvec accumulation. Equal indices, including
n=m=0, occur only in C999o's audited square and use their direct sums.
Both positive and negative shift formulas are used separately.

The uniform analytic remainder rmax and the normalized unequal-index
bound2rmax/pi give (4); the equal-index remainder and D contribution
are included in the local cap. Independent integer intervals give
local_derived<.000093587986356<.0001. The seven continuous terms and
their complete suffix,64 response terms and suffix, and all sixteen
nearest prime powers remain. The square's full T,T*,U and D+S were
audited in C999o Section6. In particular its M includes the actual D
on512:1023; no lower comparison diagonal is used in the new residual.
Symmetrization preserves the entry allowance.

For all1024 inputs the absolute product sum is <2400 per row and
gamma_2048<2.3e-13. The final three-term addition, coordinate error and
extra1e-11 per row fit the full1e-6 norm allowance. The same bound is
valid for either disjoint subset in (5). Thus no residual cross term
is lost by combining the three actual summands before squaring.

**Independent complete arithmetic.** Reproduce from the notebook with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/frozen-full-residual-audit-592.py

The full certificate is `scripts/separation-seven/frozen-full-residual-audit-592.json`.
A separate90-digit replay, basename `frozen-full-residual-replay-592`,
saves its py/json/npz/log in the same directory. It regenerates ALL
65536 residual rows and all65188 original checks. Every saved array
agrees bit for bit, including the reference, factor, solution, middle
dyadics and complete combined residual. This is preservation evidence;
the preceding analytic case analysis, not array agreement, links the
centers to the exact operators.

The audit independently uses the read110-place integer outward-interval
implementation from audit552. It encloses ell by the positive
atanh(1/2) series with geometric remainder, pi by Machin's alternating
series, and square roots by integer isqrt. Logarithms retain the stated
Decimal correct-rounding contract:130-digit endpoint values are widened
before conversion to the integer grid. All3072 exact profile coefficient
intervals nest in the original enclosures, and all conversion allowances
are checked. Every local center residual coordinate is also accumulated
as an exact dyadic/rational product using the full M,T,T* matrices;
its total arithmetic discrepancy is <7.020e-16, below the paid allowance.

The exact rational head is reconstructed as

    H=m0-(100/307)cov00-[6671/(307*12500)]I.

All512 coordinates of Hy and all512-square entries of FF* are computed
by integer dot products over common rational denominators. Every Hy
enclosure is contained in the original saved enclosure. The complete
exact reconstruction satisfies

    ||H-.24I-FF*||_F <4.491e-14<1e-6,
    ||rhohat_P-Hy||_2 <7.046e-20.

Hence the retained H>=.239999I floor is independently verified without
an accuracy assumption on Cholesky or solve. The exact squared-norm
numerator, denominators and complete H-action numerator vector are saved.
For b=P rho, the identity
<H^-1b,b>=2Re<y,b>-<Hy,y>+<H^-1(b-Hy),b-Hy>, together with
||b-rhohat_P||<=delta_P, gives exactly (6). The residual and linear
error terms are both paid; using only the tiny proposed-solve residual
would not give (6).

Every65024 complementary d_n is independently enclosed, checked against
its saved lower endpoint and6.14, and used in the complete weighted sum.
The weighted triangle inequality gives (7); d_n's positive derivative
justifies the tail weight d_K. Only the head, finite complement and
infinite complement are orthogonal for the block-diagonal R inverse.

**Entire infinite output and final margin.** The S bound holds for
every m<=1023 because c_j^2/(c_j^2+k_m^2)<=1 removes all m dependence
before summing. The shift antiderivative applies to both signs and gives
2/[pi(n-m)]<=2/[pi(n-1023)]. Integral comparison gives denominators
K-1024 and K-1 exactly as in (8). An independent integer enumeration
recovers all16 nearest prime powers. Both complete continuous norms,
not just their truncated remainders, are charged through ||f||+||h||.
Dg has no output past1023 and Cg=0 algebraically. The three tail
contributions are added before squaring, paying their entire covariance.

The independent outward upper bounds are

    head < .00000623343727734396162574265,
    finite complement < .000156200152309373966632536,
    infinite tail < .000598478405315946276083539,
    total < .000760911994902664204341818 < .000760912.

Full endpoints, not these shortened displays, are used in the addition.
The total is no larger than the original full upper endpoint. All68710
audit checks pass with no failures; all original input hashes are
preserved. The load-bearing total, tail, original energy and failure
values were inspected in full, and the checker evaluates every saved
coefficient, H-action coordinate and denominator rather than samples.

C999o Section6's independently audited original energy is
>.4232843888564016>.42328427. Its full signed U, all334 remote prime
powers, exact zero delay2187 and continuous suffixes remain in that
energy. U has no middle variable, which explains its absence from rho.
Thus (3) gives Q_min>.422523358005097335795658>.42252335.
This upholds (1)-(2) under the inherited contracts. C999n's zero-tail-
predictor quarter obstruction remains valid; one positive endpoint pair
does not supply any uniform endpoint-complement comparison. Whole-core,
unreplayed c_*, analytic/IEEE754/Decimal, C744q, H2 and global actual-Xi
qualifications remain exactly as stated.

## Mathlib

Full matching coverage for this fixed complete residual certificate,
the restricted relation-order specialization and its entry/tail bounds
has not been checked. The standard analytic inputs and their exact
citations are stated above. Unknown Mathlib coverage is not absence.
