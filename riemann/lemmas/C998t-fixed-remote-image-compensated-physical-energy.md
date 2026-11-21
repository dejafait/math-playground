# C998t: Compensated physical energy of the fixed remote image

## Hypotheses

Use C998s's unchanged real h=P0Uf, ell=log(3)/2, exact C999l
completion of the frozen C998r witness, and the complete U of C744z(1).
The witness is `scripts/separation-seven/defect-window-fixed-pair-707-witness.json`,
SHA256 `99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a`.
No coefficients, shift, endpoint or tolerance are varied. Use C744v's
full form a=D+S on V and C744z's restriction a0 to V0. In particular
both response parities and j=0 belong to S. C998s/audit714 gives h in V0
and its complete interval BV, supremum and norm bounds.

Retain the analytic-response, neutral-core, IEEE754/Decimal and unreplayed
c_* qualifications of those inputs. This argument uses no coercivity or
inverse estimate, no RH assumption and no approximation to neutrality.
It does not replay the inherited source certificates. Its real-profile
argument does not assert a new complex BV theorem.

The invocation-start SPECIALIZE assessment714/comparison715 covers this
one physical scalar attempt. Standard inputs imported, not reproved, are:

- [NIST DLMF5.9.16](https://dlmf.nist.gov/5.9.E16), accessed13November2026:
  psi(z)+gamma_E=integral_0^infinity (exp(-t)-exp(-zt))/(1-exp(-t))dt
  for Re(z)>0. We use z=1/4+i xi/2 and z=1/4.
- Hashash--Poliakovsky, *BMO-Interpolations and Jump Detection for
  Functions in BV intersect BMO*, [arXiv:2509.04176v1](https://arxiv.org/pdf/2509.04176v1),
  Definition9.3/Proposition9.4(1), printed pp45-46, including the forward
  proof(9.29)-(9.31) and smooth input(9.6) p42: for real u in BV(R),
  ||u(.+v)-u||_1<=|v| TV_R(u). There is no BMO assumption in this input.
- Aistleitner--Dick, *Functions of bounded variation, signed measures,
  and a general Koksma--Hlawka inequality*,
  [arXiv:1406.0230v2](https://arxiv.org/pdf/1406.0230v2),8October2014,
  Theorem1/(6) p3, general measurable proof in Section4 pp18-20.
  Only d=1 and Lebesgue measure are used; rescaling an interval of
  length L and taking K midpoints gives error<=L Var(f)/(2K).
- Nair, *Topics in Fourier Analysis*, July-November2018,
  Theorem2.5.15/full proof p43/PDF49,
  [primary PDF](https://home.iitm.ac.in/mtnair/FS-2018.pdf), as assessed711
  and specialized in C998s: the reflected BV cosine coefficients are
  bounded by four times interval variation divided by their index.
  Plancherel, Tonelli and dominated convergence have their usual
  Lebesgue-space meanings; their integrability hypotheses are checked below.

The smooth archimedean identity is C744v(4), with its named Li paper45
Lemma3.1 source and qualifications. L742(9)-(12) and its scalar audit
fix the full geometric-form normalization. No general response identity
or smooth Weil formula is being reproved.

## Conclusion

Choose a right-continuous BV representative of the zero extension of h,
with value0 at ell and outside [0,ell]. Put

    C(v)=integral_R h(x+v)h(x)dx,     Delta(v)=C(0)-C(v),
    k(v)=2 exp(-v/2)/(1-exp(-2v)), v>0,
    d0=psi(1/4)-log(pi).

Then the COMPLETE restricted form has the absolutely convergent identity

    a0(h,h)=d0 C(0)+integral_0^infinity k(v)Delta(v)dv.       (1)

Equivalently it equals

    -(log(4pi)+gamma_E) C(0)
      -integral_0^infinity k(v)[C(v)-exp(-v/2)C(0)]dv.       (2)

This is an equality with the full D+S closure, not just a new definition
of an integral or a generator-domain assertion. It includes the exact
334 shifts, identity shift2187, entire K14 and both exact P0 moments
through h. There is no discarded single-cell response. The separate
pole and prime terms vanish for the exact reasons in Section3.

Section4 fixes one nested midpoint prescription with delta=2^-70,
N=2^76 outer nodes and K=2^83 inner nodes. In an ideal exact-value model
its total omission/discretization error is strictly below

    133/2^32 < 2^-24 < 1e-6.                              (3)

However its specified streaming loop requests exactly

    K(2N+1)=2^160+2^83

values of h, even before paying for one such value. This parks that
prescription. A complete executable scalar certificate, precision and
finite arithmetic ledger have NOT been obtained; no energy or Gram was
evaluated. The count is sufficient work for this fixed loop, not a
necessary complexity lower bound. The bridge(1)-(2) is a local
standard-method REPRODUCTION. Separate conceptual audit718 in Section6
upholds the bridge and the expressly limited ideal ledger under the
retained contracts; it supplies no finite-arithmetic scalar certificate.
Signed S3, other entries, H2 and actual-Xi/global assembly remain open.

Section7's separate breakpoint-method preflight720 parks ONE direct
shift-pair/mode-pair primitive implementation: its C(0) preparation
alone requests at least11,076,833,565 scalar accumulations, exceeding
the10^8 total-operation cap. No analytic Gauss panels or scalar batch
were executed. This does not exclude compressed representations or
other implementations of breakpoint integration. Total error,
sufficient precision and byte storage remain unpaid for that method.

Section8's common-frequency preflight722 parks a different implementation:
reuse endpoint Toeplitz transforms, but separately assemble each piece-pair
correlation, including its affine resonances. Just the prescribed positive-
frequency resonant products require170,169,660 real operations>10^8.
This is not a lower bound for reassociated or non-pairwise algorithms.
No FFT, quadrature or scalar batch was executed; the full error,
precision and storage ledger remains unpaid.

## Proof

### 1. Zero-extension variation and compensated correlation

C998s gives interval variation<2^22, supremum<2^20 and L2 norm<2^10.
Zero extension adds the two endpoint traces, each of modulus<2^20.
Thus the following safe bounds apply to the full-line representative:

    M=2^20, B=2^23, A=MB=2^43,
    ||h||_infinity<M, TV_R(h)<B, ||h||_2<2^10.             (4)

They include all interior shifts and both endpoint jumps. The chosen
right-continuous values realize the BV variation without inserting
isolated spikes. Changing these values does not change any form or
Lebesgue integral. The real frozen coefficients, real U and real
two-moment Gram inverse make this particular h real.

The imported translation theorem now has its full-line hypothesis.
For all v,w, boundedness of h gives

    |C(v)-C(w)|
      <=M ||h(.+v)-h(.+w)||_1 <=A|v-w|.                  (5)

Translation invariance of the full-line L2 norm also gives

    Delta(v)=||h(.+v)-h||_2^2/2 >=0,
    Delta(v)<=A|v|,    Delta(v)<=2||h||_2^2<2^21.         (6)

For v>=ell the overlap has measure zero, so C(v)=0 exactly.
The inequality exp(2v)>=1+2v implies

    k(v)<=1/v+2 (v>0),
    k(v)<4 exp(-v/2) (v>=1).                            (7)

The second bound uses exp(2)>2. Equations(6)-(7) prove absolute
integrability of k Delta at zero and infinity. They also pay the
diagonal cancellation at jumps; h is not assumed H1.

### 2. Identification with the complete closed form

Subtract the two DLMF integrals in the hypotheses, take real parts
and set t=2v. For real xi this gives the nonnegative identity

    Re psi(1/4+i xi/2)-psi(1/4)
      =integral_0^infinity k(v)(1-cos(xi v))dv.           (8)

Each original DLMF integral is convergent at both ends; the subtraction
and change of variable are valid. If u is a compact smooth real profile
in (0,ell), Tonelli applied to the nonnegative integrand in(8) and
Plancherel with measure dxi/(2pi) give

    integral_R [Re psi(1/4+i xi/2)-log(pi)] |F_u(xi)|^2 dxi/(2pi)
      =d0||u||_2^2+integral_0^infinity k(v)Delta_u(v)dv.  (9)

Indeed Plancherel identifies the inner (1-cos) integral with
||u(.+v)-u||_2^2/2. C744v(4) identifies the left side with the full
a(u,u), including both response parities and j=0. Neutrality is not
needed here: (9) is the archimedean form, without pole or prime terms.

We justify passage to this BV h in BOTH expressions. For integers j
large enough, choose smooth cutoffs chi_j in [0,1], supported in
[1/j,ell-1/j], equal to1 on [2/j,ell-2/j], with total variation2.
Put b_j=chi_j h. The product variation inequality gives

    ||b_j||_infinity<=M,     TV_R(b_j)<=B+2M<2^24=:B'.

Let rho be a nonnegative smooth unit-integral mollifier supported in
[-1,1], and u_j=rho_(1/(4j))*b_j. These are real compact smooth
profiles in (0,ell). Averaging preserves the supremum bound; applying
the variation definition to each finite partition and integrating
preserves TV_R(u_j)<=B'. The cutoff errors tend to0 in L1 by their
shrinking support. Moreover the translation inequality gives

    ||u_j-b_j||_1 <= B'/(4j).

Thus u_j->h in L1 and in L2, since |u_j-h|<=2M implies
||u_j-h||_2^2<=2M||u_j-h||_1. This construction handles endpoints
and interior jumps simultaneously; no H1 convergence is claimed.

Reflecting each u_j onto the cosine circle, as in C998s Section2,
creates no seam jump. The imported BV coefficient bound yields
|<u_j,e_n>|<=4B'/n=2^26/n for n>=1, uniformly in j. C998s gives
|<h,e_n>|<=2^24/n. Every coefficient converges by L2 convergence;
the squared differences times 1+log(n+2) are dominated by
2^54(1+log(n+2))/n^2, a summable sequence. The index0 term converges
separately. Hence u_j->h in the defining V norm. C744v's bounded S
and logarithmic diagonal imply a(u_j,u_j)->a(h,h).

On the physical side, C_(u_j)(v)->C(v) uniformly in v by Cauchy--Schwarz
and L2 convergence. Uniformly in j, the bounds corresponding to(6) are
Delta_(u_j)(v)<=MB'v near0 and Delta_(u_j)(v)<=2M^2 ell everywhere.
Together with(7) they give an integrable majorant, independent of j.
Dominated convergence passes the entire integral in(9) to h. Thus
(1) equals a(h,h), and h in V0 makes this a0(h,h). We used an explicit
common approximating sequence, not L2 convergence alone or an assumed
continuity of the proposed physical integral in the form norm.

### 3. Normalization, support and exact neutrality

For completeness the constant in(2) can be checked without evaluating
psi(1/4). DLMF at1/4 gives

    psi(1/4)+gamma_E
      =integral_0^infinity 2[exp(-2v)-exp(-v/2)]/(1-exp(-2v))dv.

Subtract the convergent integral integral k(v)[exp(-v/2)-1]dv.
The resulting integrand is -2 exp(-v)/(1+exp(-v)), whose integral
is -2log2. Therefore

    d0=-(log(4pi)+gamma_E)
           +integral_0^infinity k(v)[exp(-v/2)-1]dv.

Substitution into(1) proves(2) with L742(10)'s exact scalar and
compensation. Both rewritten integrals converge separately at zero
and infinity by(6)-(7). This checks the normalization, not a new
smooth Weil theorem.

The single-cell prime sum in L742 vanishes because exp(ell)=sqrt3<2.
The pole term factors through the two exact exp(+/-x/2) moments.
They vanish by C998s's exact P0, not by small numerical residuals.
All334 prime shifts and full K14 remain in the input h; the empty
single-cell prime sum does not remove them from its quadratic energy.
The argument does not remove either response parity or the j=0
single-cell response, and does not assert membership in the original
causal generator domain. The equality is with its specified form
extension a0.

### 4. One fixed ideal scalar prescription and its cost stop

Define the exact scalar J=integral_ell^infinity k(v)dv. Since ell>1/2,
1-exp(-2ell)>1-exp(-1)>1/2, so

    0<J<8.

C998s Section4's already proved bound |d_n|<log(n+2)+512 gives
|d0|<513. In particular |d0+J|<521<2^10. No value of either scalar
is numerically evaluated here.

Fix, once, delta=2^-70, N=2^76 and K=2^83. Let L=ell-delta and

    v_i=delta+L(i-1/2)/N, i=1,...,N,
    x_j=ell(j-1/2)/K, j=1,...,K,
    Chat(v)=(ell/K)sum_(j=1)^K h(x_j+v)h(x_j).

Every h value here means the complete exact function with its chosen
BV representative, not a truncated kernel or rounded projection.
Our ideal scalar is

    Q=(d0+J)Chat(0)+(L/N)sum_(i=1)^N k(v_i)[Chat(0)-Chat(v_i)]. (10)

This treats the whole v>=ell tail by J C(0), exactly. There is no
far-tail omission. The following bounds account for the remaining
ideal errors.

First the omitted diagonal costs

    integral_0^delta k(v)Delta(v)dv
      <=A(delta+delta^2)<2A delta=2^-26.                 (11)

For outer quadrature F(v)=k(v)Delta(v) on [delta,ell], (5) makes
Delta Lipschitz, hence absolutely continuous with |Delta'|<=A
almost everywhere. The positive smooth kernel k is decreasing.
Using Delta(v)<=Av, the product rule and integration by parts give

    Var(F)<=A integral_delta^ell [k(v)-v k'(v)]dv
      =A[2 integral_delta^ell k(v)dv+delta k(delta)-ell k(ell)].

Here integral_delta^ell k(v)dv<=log(1/delta)+2<72 and
delta k(delta)<=1+2delta<2. Thus Var(F)<146 A<2^51.
The rescaled Koksma--Hlawka theorem at the N midpoints, whose star
discrepancy is1/(2N), bounds the exact-correlation outer error by

    L Var(F)/(2N)<2^50/N=2^-26.                         (12)

For each fixed v in [0,ell], the product h(x+v)h(x) has variation
on [0,ell] at most2MB=2^44. This follows directly by bounding each
factor in the product variation inequality; all its shifted jumps
and endpoint values are included in B. It is a real Borel BV
function, so the cited theorem's general measurable case applies.
The same midpoint rule gives, uniformly including v=0,

    |Chat(v)-C(v)|<=ell(2MB)/(2K)<A/K=2^-40=:epsilon.    (13)

The sampled kernel mass W=(L/N)sum_i k(v_i) is bounded using the
same theorem on the decreasing smooth k. Since k(delta)<2/delta,

    W<=integral_delta^ell k(v)dv+L k(delta)/(2N)
       <72+2^-6<128.                                  (14)

Consequently the Chat(0) error outside the outer sum is<2^10 epsilon
=2^-30; the errors of BOTH correlations inside it cost<256 epsilon
=2^-32. Combining(11)-(14) gives exactly the upper budget
2^-26+2^-26+2^-30+2^-32=133/2^32 in(3).

This is a complete ideal discretization bound, NOT a finite-arithmetic
certificate. Freeze the following streaming implementation: compute
Chat(0) with K calls to h; for each of the N outer nodes, compute
Chat(v_i) with K products, calling h twice per product, recomputing
h(x_j) rather than storing K values. Even counting zero-return calls,
this loop requests exactly K(2N+1)=2^160+2^83 h values and N kernel
values. The bound counts the specified loop; skipping, reusing or
analytically integrating values would be a different prescription.
It uses a constant number of exact scalar accumulators and current
nodes in addition to the fixed profile description. That is only an
exact-real storage count, not a justified number of bits or bytes.

More than2^160 requests is already unaffordable even if an h oracle
were free apart from one operation per call. Stop this prescribed
loop before developing or running its full finite-arithmetic service.
In particular numerical node locations at jump boundaries, every
shift weight and completed cosine coefficient, the entire K14 suffix,
both P0 moments and its inverse Gram matrix, d0, J, k, all h-value
errors and accumulated rounding remain unpaid. No inherited used-
rectangle allowance covers those obligations automatically. No
sufficient precision, actual byte count or total elementary-operation
bound is claimed. No all-entry or scalar batch was run.

This is not a lower bound on the complexity of computing a0(h,h),
not a lower bound on actual quadrature error and not evidence about
the sign of a Gram or S3. The new input retained for later use is the
full-form identity; one complete executable1e-6 scalar prescription
remains an unresolved part of the approved attempt.

### 5. Small exact check and remaining scope

Run `python3 scripts/separation-seven/remote-image-physical-energy-716.py`.
The full certificate is `scripts/separation-seven/remote-image-physical-energy-716.json`.
It checks the witness pin, every rational exponent/budget comparison
used in Section4, and the exact work count; it records all unpaid
arithmetic obligations. It neither evaluates h nor verifies the
analytic proof by software. No old certificate is overwritten.

The617/603/635/640/652/705/712 stops and unfinished work are preserved.
This scalar identity does not supply a way to control the signed
remote-plus-induced coupling in C744z(4). No complete-solution
candidate is claimed. The smooth-source imports and all retained
analytic/core/arithmetic qualifications still apply.

### 6. Separate conceptual audit — 13 November2026, step718

Invocation-start assessment716/comparison717 is SPECIALIZE for this
exact audit. The BV, Fourier, digamma and measurable-quadrature sources
listed in the hypotheses are reused. The audit upholds (1)-(3) and the
fixed-loop stop, without changing the witness, prescription or stated
scope. No mathematical error requiring repair was found. This establishes
the reviewed local input, not mathematics beyond the checked methods.

**One representative and one common sequence.** C998s Section1/audit714
gives real h and its interval BV bounds, including the complete U and
exact P0. The full-line right-continuous representative takes the right
trace at0 and value0 atell. Its distributional variation equals its
pointwise variation: the two added jumps have the endpoint trace
magnitudes, each at most M. Thus 2^22+2M<B pays both endpoints, with
no arbitrary isolated values at sampled nodes. An endpoint convention
used to reflect h for Fourier coefficients can differ on finitely many
points without changing those coefficients.

For j>4/ell the cutoff exists with the claimed plateau, support and
variation2. Its product with h has variation at most B+2M<B'. The
mollified support lies in [3/(4j),ell-3/(4j)], strictly inside the cell.
Nonnegative convolution preserves the bound M and bounds each finite
partition variation by B'; taking the supremum yields TV<=B'. The
imported full-line translation estimate applies to b_j, so averaging
over shifts of magnitude at most1/(4j) gives the displayed L1 error.
The cutoff error is supported in endpoint strips of total length4/j
and is bounded by M there. Consequently L1 convergence and the common
2M difference bound give L2 convergence, including interior jumps.

Reflection/scaling is exactly C998s Section2: the circle variation
is at most twice interval variation and the normalized cosine
coefficient is sqrt(2ell) times the Fourier coefficient, with
sqrt(2ell)<2. For n>=1 the difference coefficients are therefore
bounded by (2^26+2^24)/n<2^27/n. The dominating weighted square
2^54(1+log(n+2))/n^2 is summable. Pointwise coefficient convergence
and counting-measure dominated convergence prove convergence in V;
the constant coefficient is handled separately by L2 convergence.
C998s Section4 bounds the absolute diagonal by log(n+2)+512,
and C744v bounds S on L2. Weighted Cauchy--Schwarz for D and ordinary
Cauchy--Schwarz for S now give a(u_j,u_j)->a(h,h).

**Full physical limit and normalization.** The DLMF integrals use
arguments with real part1/4. Their real-part difference is nonnegative
and has exactly the factor2 from t=2v. Plancherel's dxi/(2pi)
normalization makes the (1-cos(xi v)) integral half the translation
square, not the full square. Thus nonnegative Tonelli gives (9).
C744v Section3/(4) applies to every compact smooth approximant,
before imposing neutrality; it retains both response parities and
j=0. No hidden neutral-core approximation is needed for this step.

For every v the correlation difference tends uniformly to zero, since
its absolute value is at most
(||u_j||_2+||h||_2)||u_j-h||_2. On 0<v<=1 an integrable uniform
majorant for k(v)Delta_(u_j)(v) is MB'(1+2v). On v>=1 one is
8M^2 ell exp(-v/2). These follow respectively from the translation
bound and Delta_(u_j)<=2||u_j||_2^2<=2M^2 ell. They justify
dominated convergence of the entire physical integral, in parallel
with the V convergence above. This proves equality to the original
D+S closure, not just existence of a separate quadratic functional.

The scalar subtraction in Section3 leaves
-2exp(-v)/(1+exp(-v)), whose integral is -2log2. This checks the
sign and log(4pi)+gamma_E constant against the unconditional portion
of L742(9)-(12)/its scalar audit. The bracket in (2) equals
-Delta(v)+(1-exp(-v/2))C(0), hence is O(v) at zero; its tail is
exponentially integrable. For v>=ell the overlap is empty almost
everywhere, so the support tail is exactly J C(0), including v=ell.
The empty single-cell prime sum uses sqrt3<2, whereas the pole
vanishes by both exact moments of P0. Neither fact deletes any of
the334 shifts, the2187 identity term, the full K14 or either projection
coefficient inside h. The final restriction uses h in V0, not a
generator-domain assertion. No conditional-on-RH statement is used.

**Ideal quadrature and its limits.** k is positive and decreasing,
as is seen directly from its decreasing positive numerator and increasing
denominator. On [delta,ell], Delta is absolutely continuous with
|Delta'|<=A. Thus the product rule bounds its weighted variation by
A integral(k-vk'); integration by parts gives exactly the boundary
signs in Section4. Dropping -ell k(ell) only increases the bound.
The inequality k<=1/v+2 gives integral_delta^ell k<72 and
delta k(delta)<2. The interval has length<1, and the rescaled
midpoint discrepancy is1/(2N), so (12) follows.

Each pointwise product x->h(x+v)h(x) has variation at most2MB on
the closed interval, including its right-continuous endpoint values.
This is within the cited theorem's general Borel BV case, even if a
node coincides with a jump. Therefore (13) is uniform, including v=0.
Applying the same theorem to k gives W<72+1/64<128. The external
norm error and both inner correlation errors are separately paid:
|d0+J|epsilon<2^10 epsilon and 2W epsilon<256 epsilon. Also
J<8 follows from 1-exp(-2ell)>1/2, and |d0|<513 is C998s's
uniform diagonal bound at n=0. All four budgets in (3) are present.

The exact streaming count uses one h call per squared value for
Chat(0), and two per product for each Chat(v_i). It includes calls
returning zero and the deliberately recomputed base value. Its
K(2N+1) count is correct for this loop. No call simplification,
inexact node/value allowance or storage in actual bits is implied.

Run `python3 scripts/separation-seven/remote-image-physical-energy-audit-718.py`.
The complete audit certificate is
`scripts/separation-seven/remote-image-physical-energy-audit-718.json`;
the output-redirected original replay is
`scripts/separation-seven/remote-image-physical-energy-replay-718.json`.
All21 original predicates were independently reconstructed; all30
audit checks pass, with no failures. The entire replay equals the
original certificate, including every bound, work field and unpaid
obligation. The original716 script/certificate and actual witness
hashes are unchanged. The full selected evidence was inspected;
software does not verify the analytic limit arguments above.

The audited bound remains 133/2^32<2^-24<1e-6 in the ideal model,
with exactly2^160+2^83 h requests. Finite arithmetic, node errors at
jumps, full h evaluation, precision and byte storage remain unpaid.
No scalar, Gram or large grid was evaluated. Stop716 and the other
recorded stops remain in force for their individual prescriptions.
No full signed S3, H2 or Xi implication is established. The inherited
analytic-response, neutral-core, IEEE754/Decimal and unreplayed c_*
qualifications remain; this proof does not use the c_* floor or any
inverse estimate. There is no new direct mathematical input or DAG edge.

### 7. Direct overlap-primitive preparation: cost stop720

The invocation-start SPECIALIZE assessment718/comparison719 covers
one breakpoint-resolved analytic Gauss prescription for the unchanged
full scalar, tested against absolute total error<=1e-6 and at most10^8
arithmetic/elementary-function operations, including preparation.
This subsection gives a negative preflight for one concrete direct
implementation of its cellwise primitives. It does not claim to test
every implementation licensed by the general quadrature sources.
Those sources do not imply a finite-work advantage. No new general
quadrature theorem or elementary integration rule is being reproved.

**Selected preparation.** Write h=p+s, where, using C744z(1),

    p(x)=sum_(n in P14) q_n 1_(I_n)(x) f(x+d_n),
    q_n=Lambda(n)/sqrt(n), d_n=log(2187/n),
    I_n=(max(0,-d_n), min(ell,ell-d_n)),
    s=K14 f-t_+exp(x/2)-t_-exp(-x/2).

All terms are zero-extended outside the cell. The t coefficients
are the exact C998s(7) projection, not rounded moment residuals.
Thus the complete correlation is C_pp+C_ps+C_sp+C_ss; at zero
C_ps(0)=C_sp(0) because the profiles are real. Full K14 and both
projection moments remain required. This splitting is just finite
bilinearity of the actual integral; it does not discard a small term.

Use Section4's exact scalar assembly with a separately computed C(0)
and the exact support tail J. The selected implementation starts by
computing the prime-prime contribution C_pp(0) with direct cellwise
cosine-product primitives. Write f=sum_(m=0)^511 F_m e_m with the
exact C999l completion used in C998s. For each pair of shifts a,b and
mode indices m,r, its primitive is

    integral_(I_a intersect I_b) e_m(x+d_a)e_r(x+d_b) dx.

It is multiplied by q_a q_b F_m F_r. At C(0) use exchange symmetry:
for a<b retain all ordered mode pairs (m,r), with the factor2 for
exchanging the two shifts; for a=b retain m<=r with the usual
off-diagonal factor2. A single shift n=2187 is the exact identity,
so its self term is computed by cosine orthonormality instead of a
dense mode square. Skip empty support intersections. Every remaining
primitive term is evaluated and separately added to a real scalar
accumulator. There is no grouping by common output frequency,
FFT, symbolic zero pruning or reuse of a precomputed whole norm in
this specified implementation. These choices define the count; they
are not asserted to be optimal. In particular some exact integrals
may vanish without changing this loop's prescribed operations.

Only after this preparation would the prescription construct the
remaining correlation panels and analytic Gauss rules, enclosing all
mixed terms, breakpoints, inner errors, moments and rounding. The
preflight stops before those steps. A complete sufficient precision,
node count or byte-storage specification is not obtained.

**Exact support test.** If a<b then d_a>d_b. Consequently

    max(left ends)=max(0,-d_b),
    min(right ends)=min(ell,ell-d_a).

Every active shift separately has |d_n|<ell. If both delays have
the same sign, their intervals overlap and d_a-d_b<ell. If they
have opposite signs, positive overlap is exactly
-d_b<ell-d_a, again d_a-d_b<ell. Thus in all cases

    |I_a intersect I_b|>0 iff log(b/a)<ell iff b^2<3a^2.

The equality b^2=3a^2 is impossible for positive integers: its two
sides have respectively even and odd3-adic valuation. Hence no
rounded logarithm, uncertain sort or boundary coincidence enters
this finite count. The exact same-sign observations also follow
from 2187/sqrt3<n<2187sqrt3 for each active n. The identity shift
overlaps every active interval.

**Operation failure.** C998s's frozen witness has510 nonzero free
coefficients at m=2,...,511. Omitting the two completed head modes
from the count is favorable to the prescription and does not omit
them from the mathematical target. Exact enumeration of all334
active shifts gives42,420 unordered distinct positive-overlap pairs
and13,191 disjoint pairs, totaling334*333/2=55,611. The selected
loop therefore contains at least

    42,420*510^2 + 333*510*511/2
      =11,033,442,000+43,391,565
      =11,076,833,565

separate accumulations. Each is an arithmetic operation in the
stated work model. This already exceeds10^8 by a factor greater
than110, even assigning ZERO cost to primitive evaluation, head
terms, weights, full K14, exact projection, all other preparation,
quadrature and rounding. Precomputing coefficient products alone
does not remove the separate primitive accumulations in this loop.

The stop does not depend on trusting a large overlap count: the
333 pairs involving the identity and the333 nonidentity self terms
already prescribe

    333*(510^2+510*511/2)=130,004,865>10^8

accumulations. This is still a count for this direct loop, not a
lower bound on evaluating C_pp(0) by another representation. No
actual-error lower bound, scalar value, signed S3 statement or
universal impossibility conclusion follows. The test parks this
implementation before choosing degrees/precision or running a batch;
it does not pay its outstanding total-error or storage obligations.

**Complete finite evidence.** Run

    python3 scripts/separation-seven/remote-image-breakpoint-preflight-720.py

The full certificate is
`scripts/separation-seven/remote-image-breakpoint-preflight-720.json`.
Trial factoring every candidate in the exact squared interval is
checked against independent sieve/power enumeration. Every unordered
shift pair is partitioned using the integer support test; an independent
monotone-window count agrees. All510 exact free coordinates are checked
nonzero, and the actual frozen witness hash matches the stated pin.
All12 checks pass. The complete selected work/check/failure fields
were inspected, not inferred from a truncated preview. The certificate
records the entire finite pair partition and all unpaid obligations;
software does not verify the analytic prose or execute any scalar,
Gram or quadrature batch.

This is a local REPRODUCTION negative result about direct preparation,
distinct from712's infinite-output truncation and716's midpoint grid.
It supplies no result beyond the checked general sources on analytic
quadrature. Preserve617/603/635/640/652/705/712/716 and the audited
bridge. All inherited contracts and signed/global gaps remain.
The existing direct mathematical inputs of C998t are unchanged.

### 8. Common-frequency piece-pair assembly: cost stop722

**Scope and imported tools.** Invocation-start assessment720/comparison721
is SPECIALIZE for this unchanged full-scalar preflight, with total absolute
error<=1e-6 and at most10^8 scalar arithmetic/elementary-function operations,
including preparation. This is one REPRODUCTION calculation. The imported
finite-polynomial Toeplitz algebra is Xu--Austin--Wei, *A Fast Algorithm for
the Convolution of Functions with Compact Support Using Fourier Extensions*,
SIAM J.Sci.Comput.39(2017),A3089-A3106, DOI10.1137/17M1114764,
Sections3.1-3.4/3.6,(3.7)-(3.10),(3.13)-(3.21), particularly the common-
frequency resonances, [published author PDF](https://faculty.nps.edu/aaustin/pubs/XAW2017.pdf).
Lessard, *Computing discrete convolutions with verified accuracy via Banach
algebras and the FFT*, Applications of Mathematics63(2018),219-235,
DOI10.21136/AM.2018.0082-18, author-manuscript Lemma1.2 and Section2
(8)-(12)/Remark2.3, [author PDF](https://www.math.mcgill.ca/jplessard/Publications_files/rig_FFT.pdf),
supplies the padding/interval-DFT tool, with comparison721's printed-index
qualification. No fitted Fourier extension, empirical truncation degree,
floating FFT accuracy or asymptotic work theorem is used. The general
algorithms are not reproved. The following local finite expansion checks
our support, correlation reflection, physical frequency and resonant term.
The cost stop occurs before using any numerical convolution or quadrature.

**One selected implementation.** Retain h=p+s exactly as in Section7,
including full K14 and the exact two-moment projection in s. Partition
(0,ell) at ALL interior endpoints of the shifted summands of p. Write
the consecutive open pieces as J_i=(a_i,b_i), i=0,...,N-1, in spatial
order. Let omega=pi/ell. On each piece the exact finite expression is

    p_i(x)=sum_(m=-511)^511 A_(i,m) exp(i m omega x),
    A_(i,-m)=conjugate(A_(i,m)).                         (14)

Here the first i in exp denotes the imaginary unit. More explicitly,
if F_m are the real completed cosine coefficients of f from C998s,
then for m>0

    A_(i,m)=(nu_m F_m/2)
             sum_(n active on J_i) q_n exp(i m omega d_n),
    A_(i,0)=nu_0 F_0 sum_(n active on J_i) q_n.

The same omega works on every piece: translations change phases, not
frequencies. All512 modes are retained. Identity2187 is active throughout
the cell. No finite Fourier representation of the zero extension on the
whole line is asserted. No approximate neutrality is substituted for P0.

Use shared endpoint Toeplitz transforms to prepare the nonresonant sums;
do not recompute an FFT for each piece pair. Store positive-frequency
complex coefficients and exploit conjugate symmetry. The selected
implementation then constructs the correlation of EACH distinct piece
pair separately, retaining its resonant affine coefficients explicitly.
For every pair and positive frequency it computes
A_(i,m) conjugate(A_(j,m)) by the classical complex product: four real
multiplications and two real additions/subtractions. It does not prune
exact zero coefficients or reassociate products across pairs. These are
implementation choices, not claims of optimality. Interval products would
cost at least these ideal real operations; their extra endpoint work and
every certification overhead are favorable zero in the lower count.

The remaining prescription would assemble C_pp+C_ps+C_sp+C_ss and C(0),
use Section4's support-tail and compensated-diagonal treatment, and use
comparison719's validated analytic Gauss tools for ALL mixed terms.
It must eventually pay all errors and preparation, precision and bytes.
The preflight below stops before selecting those panels or executing
the proposed transforms. It is not a completed scalar prescription.

**Exact partition.** For n<2187 the translated support ends at
log(n)-13ell; for n>2187 it starts at log(n)-14ell. Every such endpoint
is strictly inside (0,ell) by 3^13<n^2<3^15. Identity2187 has no interior
endpoint. Two entrances or two exits are distinct by injectivity of log.
An entrance for n and an exit for r could coincide only if n^2=3r^2,
impossible by the parity of the3-adic valuation. Thus all333 nonidentity
shifts give distinct interior events, so N=334 and every piece has
positive length. The certificate sorts them exactly using exp(2x):
entrances have n^2/3^14 and exits n^2/3^13. Endpoints0,ell correspond
to1,3. This uses rational ordering, with no rounded-log assumption.

**A required resonant coefficient.** Fix i>j. The piece-pair term for
positive lag v is

    C_ij(v)=integral_(J_j intersect (J_i-v)) p_i(x+v)p_j(x) dx.

The half-open endpoint convention affects no integral. Because pieces
are spatially ordered, a_i>=b_j. On the nonempty first-overlap interval

    a_i-b_j < v < min(a_i-a_j,b_i-b_j),                  (15)

the lower endpoint is a_i-v and the upper is b_j. Its length is
b_j-a_i+v; the length of the interval(15) is
min(b_j-a_j,b_i-a_i)>0. Every one of the N(N-1)/2 distinct spatial pairs
therefore has positive-length overlap on some positive-lag interval
inside (0,ell); nonzero correlation is not asserted for every pair.
This count differs from Section7's shift intersections at v=0.

Insert the FINITE sums(14). A nonresonant m+r!=0 term has primitive

    A_(i,m) A_(j,r) exp(i m omega v)
       exp(i(m+r)omega x)/(i(m+r)omega).

Evaluation at b_j and a_i-v gives respectively a fixed-endpoint
frequency m and a moving-endpoint frequency -r. Their reciprocal-index
endpoint sums are the reusable Toeplitz operations above. No conjugation
of the analytic continuation or change of physical scale is hidden here.
For r=-m the integrand is constant in x, so the EXACT resonant part is

    (b_j-a_i+v) sum_(m=-511)^511
         A_(i,m) A_(j,-m) exp(i m omega v).              (16)

For m>0 its real paired contribution is

    2 Re[(b_j-a_i+v) A_(i,m) conjugate(A_(j,m))
                                               exp(i m omega v)].

Hence the prescribed separate affine-coefficient assembly includes the
complex product stated above. Nonresonant terms on this interval have
no affine v factor; neither endpoint Toeplitz reuse nor conjugate
symmetry removes this product in this selected loop. This is a finite
specialization of the cited resonant integration cases, not a new
convolution theorem. Cancellations, factorizations, evaluation without
coefficient assembly and other algorithms are expressly untested.

**Finite work failure.** Count only m=2,...,511, favorably omitting the
other two input modes, all self pairs, and all remaining overlap branches.
There are55,611 distinct spatial pairs, so the loop prescribes

    55,611*510=28,361,610 complex resonant products,
    4*28,361,610=113,446,440 real multiplications,
    2*28,361,610=56,723,220 real additions/subtractions,
    total >=170,169,660>10^8.                           (17)

Real multiplications alone exceed the ENTIRE operation cap. This count
is valid even if some piece coefficients vanish, since the specified
implementation performs all products; it does not assert their nonzero
values. No actual coefficient, scalar, Gram or FFT batch is computed.
Giving zero cost to endpoint transforms, their preparation, all other
coefficients, s and every mixed term only favors feasibility. Thus an
unpaid error bound cannot rescue this implementation under the stated
cap. Precision and byte storage remain unpaid, rather than asserted
unnecessary. The count is not an error lower bound, an intrinsic
complexity theorem or a stop for every common-frequency representation.

**Reproduction and qualifications.** Run

    python3 scripts/separation-seven/remote-image-frequency-preflight-722.py

Full finite evidence is
`scripts/separation-seven/remote-image-frequency-preflight-722.json`.
The two independent prime-power enumerations agree; all334 shifts,
333 distinct rationally ordered events,334 positive pieces and all
55,611 positive first-overlap branches are checked. The unchanged witness
hash is reverified and its510 exact free coordinates are nonzero. All13
checks pass. The complete work, check, invalid-pair and error fields
were inspected. These finite checks do not verify the analytic prose.

This is a negative local standard-method implementation result, with
no progress beyond the checked sources on general convolution theory.
Preserve the Section7 direct-loop stop and617/603/635/640/652/705/712/716.
All analytic-response, neutral-core, IEEE754/Decimal and unreplayed c_*
contracts remain. No inverse estimate, RH or cross-notebook input enters.
Independent signed S3, other entries/endpoints, C744q/H2 and Xi/global
assembly remain open. Direct mathematical inputs of C998t are unchanged.

## Mathlib

Full matching coverage for this fixed BV profile, its complete D+S
identification and quantitative nested prescription has not been
checked. The named BV, Fourier, digamma and quadrature theorems are
supporting inputs, not a formalized fixed-profile certificate. No
absence claim or new formal verification is made.
Full matching coverage for Section7's fixed implementation/count has
not been checked; the exact finite script is not a Mathlib proof.
Full matching coverage for Section8's piecewise representation and fixed
implementation/count is not checked. The cited finite convolution tools
are supporting results; no absence or formal-verification claim is made.
