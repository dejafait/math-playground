# Lemma 963: the single whole-edge derivative enclosure is unpaid

## Hypotheses

Use L962's exact finite definitions at x=X=6000000185827, but now
let t range over the closed interval I=[a,b]=[98/625,1/5]. In particular
the physical phase, amplitude and ell all vary with t. Use the principal
logarithm at the fixed s=(1+iX)/2 and its conjugate branch. No polydisc
stability, torus floor or assertion about H_t is assumed for this finite
calculation. L960 supplies the audited uniform M32 bound and the existing
conditional two-sided payment; its analytic/remainder/companion and real
gauge hypotheses remain assumptions for any transfer to H_t.

This statement concerns the particular interval algorithm below. It
asserts neither failure of actual positivity nor an impossibility for
other enclosure methods.

## Conclusion

The natural support is N=690988 throughout I. The complete-support
first-derivative computation produces an interval D containing F'(I),
with exact endpoints satisfying

    -145424 < D_lower < -145423,
     136035 < D_upper < 136036.

Its mean-value propagated enclosure uses L962's independently audited
corner F(a). The separate uniform norm enclosure has upper endpoint
less than 677/100, and the payment upper endpoint is less than
203/1000000. The resulting enclosure J for F(t)-E(t), t in I, satisfies

    -6133 < J_lower < -6132 < 0 < 6027 < J_upper < 6028.

Thus this one whole-edge pass does not certify a positive paid sign.
The required derivative lower threshold for this method lies strictly
between -3480 and -3479, whereas its actual lower endpoint is below
-145423. The enclosure containing zero does not imply that F-E takes
zero or a negative value. No negative-sign certificate, H_t exclusion
on the edge, actual-Xi sign or RH candidate follows.

## Proof

### Coverage and known inputs

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-11-10-physical-time-edge-paid-reserve-150.md`.
It covers exactly this complete finite, whole-edge derivative test,
with no subdivision or time sweep. This is reproduction/specialization
of known interval inclusion, not a new general positivity theorem.

Import Siegfried M. Rump, *Verification methods: rigorous results using
floating-point arithmetic*, Acta Numerica19(2010),287–449,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Sections11.1/11.6, (11.1)–(11.2)/(11.10), and Theorem13.1, p.380,
(13.1)–(13.4). For a real C1 function on a box, a Jacobian enclosure
over the full joining segment gives the mean-value inclusion. Here
the box is the real interval I and the output is the smooth real F.
This supplies inclusion only, not small width or positivity. The
finite elementary series, dyadic arithmetic, periodic reduction and
their precise citations are as in L962. No interval theorem is
reproved; the application and implementation correspondence are below.
The admission source's stationary nonvanishing claim is a different
observable and is not used as numerical evidence.

### Support, branches and finite differentiation

The exact outward endpoint gates in the certificate are

    X/(4pi)+a/16-690988^2 > 0,
    690989^2-X/(4pi)-b/16 > 0.

Both lower dyadic endpoints are strictly positive. The radicand is
increasing in t, so these establish the stated floor on the entire
closed interval, including its endpoints. No floor is differentiated.
The fixed s has positive real and imaginary parts, avoiding zero,
one and the principal-log cut; the conjugate branch is likewise valid.
Thus alpha(s), alpha'(s) are constants in t and all subsequent finite
exponentials are smooth real-coordinate functions on a neighbourhood
of I. No nonvanishing of A or any limiting interchange is used.

Write alpha=u+iv, k_n=log n, and

    z_n(t)=exp(-s*k_n+t*(k_n^2/4-alpha*k_n/2)),
    beta_n=k_n^2/4-alpha*k_n/2.

This is exactly a_n exp(-i tau k_n), with sigma=1/2+tu/2,
tau=X/2+tv/2. Differentiating this entire exponential in real t gives
z_n'=beta_n z_n, including amplitude and physical phase. After the
support gates all sums are finite, so

    A'=sum beta_n z_n,      L'=sum k_n beta_n z_n,
    ell=2Re(alpha)+t Re(alpha alpha'),
    ell'=Re(alpha alpha'),
    S=ell A-2L,            S'=ell' A+ell A'-2L',
    F'=Re(conj(A')S+conj(A)S').

The ell identity is L962's exact carrier formula, not an asymptotic.
The product rule applies in real coordinates to conjugation as well.
For n=1, k_1=0, z_1=1 and beta_1=0 exactly. That term is included.

### Included computation

Run from the notebook directory:

    python3 scripts/physical-corner/time_edge_152.py
    python3 scripts/physical-corner/inspect_time_edge_152.py

The evaluator imports the already justified Q=2^256 dyadic operations,
Machin pi, logarithm and square-root routines through L962's generator.
It uses the same eight-term inverse-argument atan, 40-term reduced
exponential and 48-term-per-function trigonometric polynomials, with
their full rigorous remainders. The code/helper/anchor hashes are saved.
Its only floating outputs are display approximations, never inputs.

It recomputes alpha and alpha' from the real formulas of L962 and
forms sigma,tau,ell on the whole t interval. The gates verify
ell-log N>13, 0<ell-2log32<25, and sigma-t log N/4>0 everywhere by
included interval endpoints. For k_n>0 the last inequality implies
k_n(t k_n/4-sigma)<0; the n=1 exponent is zero. The reused exponential
algorithm checks every nonpositive exponent enclosure, halves its
negative until the entire reduced interval is in [0,1/8], includes
the positive exponential remainder, squares and reciprocates only
after checking a positive lower endpoint. A physically wide input
remains wide; no arithmetic-width suppression is made.

A smallest-prime-factor sieve and increasing induction visit every
integer 1,...,N. At primes the phase is -tau log p, with the full time
interval retained. For an integer j chosen by midpoint arithmetic,
the entire reduced phase -tau log p-2j*pi must lie in (-4,4).
Every such per-prime gate passes. Periodicity holds for any integer j;
it does not require a unique nearest-integer branch. The L962 sine
and cosine polynomials and remainder bounds on this whole interval
therefore enclose the prime character. At composites, included complex
multiplication of the already computed proper-factor characters uses
the exact identity chi(pm)=chi(p)chi(m) at each common t. Independent
interval occurrences may overestimate but never exclude that common
value. Logarithms are treated by the corresponding exact additive
identity. All cached factors exist by increasing induction, as checked
by the same sieve/factor assertions as L962.

For each n, included complex multiplication forms beta_n z_n and
its k_n multiple, alongside z_n and k_n z_n. The exact all-sign
endpoint arithmetic sums each of A,L,A',L' in 338 consecutive blocks.
For real coordinates, Re(conj(c)d)=c_re d_re+c_im d_im, so the code's
dot products give precisely the displayed F' formula. This proves
inclusion in the recorded D; it does not assume statistical cancellation
or an independently constant character during differentiation.

### Mean-value propagation and payment

Let F0 be the interval for F(a) in L962's independent step150 replay,
read at its full exact dyadic endpoints and included exactly at 256 bits.
The completed replay is an established input, not repeated here.
The real C1 theorem cited above gives for all t in I

    F(t) in F0 + D*[0,b-a],       b-a=27/625.

The elapsed interval's upper endpoint is rounded outward, so the
implemented propagation still includes this range.

From the rectangle enclosure for A, put

    U2=max(|A_re_lower|,|A_re_upper|)^2
       +max(|A_im_lower|,|A_im_upper|)^2.

Then |A(t)|<=sqrt(U2). Included multiplication and the outward square
root bound U2 above. Using [0,sqrt(U2)_upper] encloses R everywhere,
even if A vanishes. In particular neither differentiating |A| nor
dividing by it is required. With the exact positive p,q in L962,

    E=p*(25R+81/2)+qR+pq

is enclosed directly; all cross terms, including pq, are retained.
The uniform M32 input and verified ell shift gates make this the same
conditional payment as in L960/L962. Actual remainder, companion and
real-gauge estimates are still hypotheses, not outputs of this test.
Subtracting the included payment from the propagated range gives J.

For a negative derivative lower endpoint and exact h=b-a, paying this
particular mean-value lower bound would require

    D_lower > (E_upper-F0_lower)/h.

The exact Fraction endpoint checker places this threshold in
(-3480,-3479) and the actual D_lower in (-145424,-145423).
Outward elapsed rounding only weakens the implemented lower bound.
This explains the width failure; it gives no lower bound on the true
variation or evidence for an actual negative point.

### Complete evidence and limitations

The full evaluator certificate is
`scripts/physical-corner/time-edge-152.json`. Its completed run took
104.9 seconds and visited all 690988 terms in 338 consecutive blocks.
Every support/domain/payment gate passed; the sole failure record is
`whole_edge_derivative_enclosure_does_not_pay_zero_threshold`.
Status is INCONCLUSIVE_WIDTH. No subdivision, precision retry,
installation, parameter sweep or incomplete-support inference occurred.

The separate checker imports no generating arithmetic. It reads every
block, verifies all adjacency/count/domain records, independently sieves
and counts primes, exactly adds every real/imaginary A,L,A',L' endpoint,
and checks equality with all saved totals. It verifies hashes and the
anchor conversion, recomputes S,S',F' and propagation inclusions with
Fraction endpoints, checks the norm upper bound by exact squaring,
and checks the full payment, final range and all stated rational
thresholds. Its 1056 checks pass with no failure; evidence is
`scripts/physical-corner/time-edge-inspection-152.json`. The selected
complete support-gate, derivative, propagated, norm, payment and paid
endpoints were also inspected. This is exhaustive endpoint/block
inspection plus the inclusion argument, not an independent replay of
every elementary function and not formal software verification.

The rounded display values are D approximately [-145423.84848,
136035.02653], propagated F approximately [-6132.00397,6027.01944],
R_upper approximately 6.76924, E_upper approximately 0.000202038,
and J approximately [-6132.00418,6027.01942]. Exact endpoints in the
certificate and the checked rational comparisons above carry the claim.
This stops only this rectangular whole-edge enclosure mechanism.
Uniform physical signs, spatial transfer, seams, initialization/recovery,
exterior/global continuation, zero time and Xi mixed positivity stay open.

### Independent uniform payment replay (step156)

The separately approved SPECIALIZE assessment is
`drafts/literature/2026-11-10-physical-time-edge-uniform-payment-audit-154.md`.
This audits only the uniform payment, not the unpaid derivative or a
physical sign. It is REPRODUCTION of the interval method and scalar
payment already stated above. The independently written step150
elementary implementation in L962 is reused as standalone code, with
time now an interval; no generating helper, numerical constant, anchor
or saved sum is imported. Reproduction commands are

    python3 scripts/physical-corner/uniform_payment_156.py
    python3 scripts/physical-corner/inspect_uniform_payment_156.py

**Preserved failed comparison.** The evaluator's final status is FAIL,
with the sole record `ArithmeticError: R_upper_lt677over100`. That
assertion was an extra comparison against the old norm enclosure, which
the assessment explicitly treats as a comparison, not a premise. It was
inserted too strongly as a required gate. No evaluator change, rerun,
parameter refinement, derivative pass or positivity test followed.
All terms, all 338 blocks and the final norm/payment endpoints had been
saved before this assertion. The independent enclosure's upper endpoint
lies between 677/100 and 679/100, so it does **not** independently
reproduce the old norm bound. This wider enclosure does not refute that
bound or conflict with the earlier enclosure. The exact endpoint audit
below verifies the approved payment threshold directly; it does not
report an all-gates PASS for the evaluator. Its first inspection also
reported the preserved driver/comparison failures; the corrected
inspection distinguishes these from the actual payment obligations.

**Inclusion proof and domains.** Use Q=2^224. The standalone `Box`
operations and finite elementary series are exactly those justified in
L962's independent step150 proof. Rational constants are enclosed by
integer floor/ceiling; signed multiplication takes all four endpoint
products; reciprocal reverses endpoints and excludes zero. Square roots
use integer square roots and a final exact upper-square comparison.
These are instances of Daumas–Lester–Munoz, *Verified Real Number
Calculations: A Library for Interval Arithmetic*,
[arXiv:0708.3721v1, Section III, Propositions9/10/12](https://arxiv.org/html/0708.3721),
not newly proved interval theorems. The cited propositions do not verify
the implementation. Here their specialization is justified operation by
operation by these exact endpoint formulas, including signed inputs.

Pi is independently enclosed as 4(atan(1/2)+atan(1/3)), using128 exact
rational alternating terms and the first omitted term. Tangent addition
and the range (0,pi/2) justify the identity. Four alternating terms for
atan(1/X) give arg(s)=pi/2-atan(1/X). Positive rational logarithms use
power-of-two scaling to m in [1,2) and64 terms of
log(m)=2 sum z^(2j+1)/(2j+1), z=(m-1)/(m+1); the tail is bounded by
2z^129/(129(1-z^2)), and log2 restores the scale. Monotonicity handles
positive interval inputs. These are the same specializations of
[DLMF4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.24.3–4](https://dlmf.nist.gov/4.24#i) as in L962. The whole interval
input to each division excludes zero; logarithm inputs are positive.

The carrier uses the independent real formulas in L962:

    u=log(1+X^2)/4-log(4pi)/2-1/(1+X^2),
    v=arg(s)/2-3X/(1+X^2),
    Re(alpha')=6(X^2-1)/(1+X^2)^2+1/(1+X^2),
    Im(alpha')=-4X/(1+X^2)^2-X/(1+X^2).

It forms sigma=1/2+tu/2, tau=X/2+tv/2 and
ell=2u+t Re(alpha alpha') on the entire closed I. Both support margins
above, ell-log N>13, 0<ell-2log32<25 and
sigma-t log N/4>0 have strictly positive lower margins. Principal and
conjugate logarithm branches remain as above at this fixed s. The
closed I and x=X lie within L960's audited moment rectangle, so its
uniform M32<20213859/1000000<81/4 applies to this same complete support.

A largest-prime-factor sieve supplies every log n by increasing
induction from prime logarithms: each composite's two proper factors
have already been evaluated. Every n>=2 then has its **own direct**
phase -tau log n evaluated, retaining the entire physical time interval.
Subtracting an integer multiple of 2pi is exact by periodicity; every
entire reduced interval is checked inside (-4,4). Division by16 puts
it inside (-1/4,1/4). Cosine through degree46 and sine through degree47
have absolute Taylor errors at most (1/4)^48/48! and (1/4)^49/49!,
respectively: use Taylor orders47 and48 with their vanishing last
coefficients. Four included angle doublings recover the full reduced
phase. These specialize [DLMF4.19.1–2](https://dlmf.nist.gov/4.19) and
[4.45.6–7](https://dlmf.nist.gov/4.45#i); endpoint evaluation alone is
never used as a trigonometric range bound.

Each entire exponent e_n=(log n)(t log n/4-sigma) is checked in [-32,0].
On e_n/256 in [-1/8,0], the degree28 exponential Taylor polynomial has
absolute error at most (1/8)^29/29!, since its29th derivative is <=1
on the joining segment to0. After including that error on both sides,
a positive lower endpoint is required before eight included squarings.
This uses [DLMF4.2.19](https://dlmf.nist.gov/4.2#iii) with Taylor's
remainder theorem, exactly as in L962. No pointwise truncation is used
for a varying exponent. The n=1 term is exactly1; all other690987
terms have positive amplitude enclosures and a direct physical phase.
For any one t in I, all its true factors lie in the respective boxes;
independent occurrences can widen but cannot exclude their common-t
values. Thus summing every signed component includes A(t) uniformly.

**Exact norm and payment.** If the complete A component intervals have
integer endpoints divided by Q, let m_re,m_im be the larger absolute
integer endpoints of each component. Then

    |A(t)|^2 <= (m_re^2+m_im^2)/Q^2.

Round this nonnegative upper bound upward to the Q grid and apply the
included square root to [0,upper]. The resulting R interval has no
positive lower bound premise and is valid even if A vanishes. Its upper
endpoint is exactly

    182989444449058291061325918635364687036467475711663021145191577696830 / 2^224,

strictly between677/100 and679/100. With the exact p,q defined above,
included arithmetic for p(25R+81/2)+qR+pq gives upper endpoint

    5460091081843496923583164750614151683952799218443197848611799210 / 2^224
      <203/1000000.

This is approximately0.00020252603424. In particular the approved
payment threshold is verified despite the extra norm-comparison stop.
The payment need not use the smaller old norm bound.

For the conditional interpretation, at each t retain the analytic,
remainder/companion and real-gauge hypotheses above. Write
a=A_true-A, b=B_true-S. L960's exact expansion gives |a|<p, |b|<q,
and its moment/shift argument gives |S|<25|A|+81/2. Expansion of all
four products therefore gives

    |Re(conj(A_true)B_true)-Re(conj(A)S)|
      <= |a||S|+|A||b|+|a||b|
      < p(25|A|+81/2)+q|A|+pq <203/1000000.

No stability or torus floor is needed for this error input. The inequality
does not establish the retained analytic bounds or any sign for F.

**Complete evidence.** The single86.88-second replay saved every one of
338 consecutive blocks through690988 in
`scripts/physical-corner/uniform-payment-156.json`. Every elementary
assertion and support/domain gate completed successfully; only the
extra norm comparison failed after the completed sum. No partial-support
value is used. The Fraction inspector imports no evaluator, verifies
all blocks and adjacency, independently counts primes, adds every
component endpoint exactly, checks every domain record and finite-error
constant, and checks the norm by exact squares, the exact p,q, and the
full payment including pq. It also compares all common carrier constants,
every A block and final bounds with step152 after the independent run;
all comparisons overlap and none is a premise. All3110 inspection checks
pass, including explicit preservation of the driver failure, in
`scripts/physical-corner/uniform-payment-inspection-156.json`, status
VERIFIED_PAYMENT_WITH_DRIVER_COMPARISON_STOP. Full final norm/payment,
gate and failure endpoints were inspected. This is an informal code and
proof audit, not formal software verification. The original stronger
norm claim retains its original proof; only its weaker sufficient payment
consequence is independently secured here. Spatial/global/zero-time
transfer and actual-Xi mixed positivity remain open.

## Mathlib

Full coverage for this exact finite parameter enclosure and its Python
certificate is unchecked. Supporting interval/elementary methods are
reused from the assessed sources; there is no Lean port or formal
verification claim. Unknown availability is not evidence of absence.
No cross-notebook input is used.
