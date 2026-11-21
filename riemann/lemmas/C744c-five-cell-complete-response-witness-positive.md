# C744c: The unchanged five-cell witness has positive complete penalized form value

## Hypotheses

Use exactly C744b's even vector v, with its 64 integer coefficients and
denominator 2^44, and the same ell=log(3)/2, L=5ell, a=L/2,
penalty 256, ten physical moments C and nine active prime powers.
Let f(x)=v(|x|)/sqrt(2) on (-a,a), extended by zero, and
u(y)=f(y-a) on (0,L). Neither vector nor any parameter is adjusted.
Use C744b (2)-(3)'s cosine basis, diagonal D_+, responses r_j^+,
pole p_+, arithmetic operator B_p^+, and (8)'s response projections.

Write bar E_L for the semibounded **form closure** of the smooth
energy L744 (6), not a value asserted on the domain of its generator.
The proof below establishes that u belongs to this closure domain.
No membership in that generator domain or zero-extension H1 space
is assumed. No exact neutrality of u, all-test sign, or RH is assumed.

The imported smooth identity is Hongmin Li, *Cutoff-free positivity
of localized Weil forms through the (log 11)/2 threshold*,
[paper45 displayed v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma 3.1, (2.1)-(2.5), with arbitrary a>0, as normalized in C744b (7).
The source's endpoint positivity and numerical supplement are not inputs.
[Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3#S3),
Theorem 1.1, Lemma 3.1 and Section 3.2, (3.2)-(3.4), provide the
finite-trigonometric-test smooth-core method. The bounded-response
kernel argument is the method of bramble_trace,
[paper60 displayed v1, 26 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/60),
Section 2, (2.1)-(2.7) and its following core paragraph. That source
uses a=2; its constants, prime list and positivity are not imported.
Below we verify the present boundary factors and cutoff convergence,
as necessary to specialize these known methods at our a. This is
REPRODUCTION under the ready SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-all-response-witness-457.md`.
Numerical operation contracts and all unchanged scalar contributions
are the already audited inputs in C744b, not new source discoveries.

## Conclusion

The unchanged vector is in the zero-extension smooth form closure and

\[
 2.0418\,10^{-7}
 <\overline E_L(u)+256\|Cu\|^2
 <2.1169\,10^{-7}.                                      \tag{1}
\]

In particular this direction is positive after every omitted response
is restored. The recovered mass satisfies

\[
 2.2785\,10^{-7}
 <\sum_{j\ge128}|\langle v,r_j^+\rangle|^2
 <2.3458\,10^{-7}.                                      \tag{2}
\]

This diagnoses loss from the fixed 128-response truncation for this
one direction. It does not repair that lower operator's negative
compression or prove a positive full operator, a neutral-subspace
sign, complement signs, all-window propagation or actual-Xi positivity.
The vector has the same nonzero moments established in C744b's audit.
The separate conceptual audit below (11 November 2026, step461)
accepts this result and its form-domain specialization. The old audited
truncated stop remains valid.

## Proof

### 1. The response form is bounded for this half-width

Put d=1-exp(-a)>0. In the coordinate t=a-x, 0<t<a, formula C744b (3)
for the even response becomes

\[
 r_j^+(a-t)=
 \frac{e^{-c_jt}+e^{-c_j(2a-t)}}{\sqrt{1-e^{-2c_ja}}},
 \qquad c_j=2j+\tfrac12.
\]

Since 2a-t>=t and 2c_j>=1, each numerator is at most 2exp(-c_jt)
and its squared denominator is at least d. For t,s>0 the nonnegative
kernel of any finite response prefix is therefore bounded by

\[
 \begin{split}
 \sum_j r_j^+(a-t)r_j^+(a-s)
 &\le\frac4d\sum_{j\ge0}e^{-c_j(t+s)}\\
 &=\frac4d\frac{e^{-(t+s)/2}}{1-e^{-2(t+s)}}
 \le\frac4d+\frac2{d(t+s)}.                         \tag{3}
 \end{split}
\]

The last inequality uses 1/(1-e^{-2z})=1+1/(e^{2z}-1)<=1+1/(2z)
and exp(-z/2)<=1. The constant kernel on (0,a) has operator norm a.
The Carleman kernel 1/(t+s) has norm at most pi on this interval:
Schur's test with weight t^(-1/2) applies because

\[
 \int_0^a\frac{s^{-1/2}}{t+s}\,ds
 =t^{-1/2}\int_0^{a/t}\frac{z^{-1/2}}{1+z}\,dz
 \le\pi t^{-1/2}.
\]

Here the integral to infinity is pi by z=w^2 and integration of
2/(1+w^2). Applying (3) to |v| bounds every finite-prefix quadratic
form, even for complex v. Monotone convergence of the nonnegative
squared projections gives the bounded linear response map

\[
 R:L^2(0,a)\longrightarrow\ell^2(\mathbb N_0),\quad
 (Rv)_j=\langle v,r_j^+\rangle,
 \qquad \|R\|^2\le(4a+2\pi)/d<\infty.                \tag{4}
\]

This is the source's constant-plus-reflected-Carleman argument with
our actual a and boundary denominator; no a=2 numerical bound is used.
In particular the full response sum is continuous in the L2 norm.

### 2. Form-domain applicability and equality on the finite vector

L744 (8), together with the convergent digamma difference C744b (11),
shows that m(xi)=Re psi(1/4+i xi/2)-log(pi) is bounded below and,
after a sufficiently large constant shift, comparable above and below
to 1+log(2+|xi|). Thus its full-line Fourier form is closed in its
weighted Fourier norm. Restricting to functions supported in [-a,a]
keeps this form closed: convergence in the form norm implies L2
convergence, and this support subspace is L2-closed. The prime, pole
and moment forms are bounded L2 perturbations. Hence the restriction
to smooth compactly supported tests is closable, and form convergence
can be checked with the logarithmic Fourier norm. We need only show
that this particular finite vector is in its smooth closure.

Choose real even smooth interior cutoffs chi_e, for 0<e<min(a/4,1/2),
that equal 1 for |x|<=a-2e and vanish for |x|>=a-e, with
|chi_e'|<=C/e for a fixed C. Then f_e=chi_e f is even and belongs to
C_c^infinity(-a,a). Write g_e=f-f_e on that interval and extend by
zero. The finite trigonometric function f and its derivative are
bounded. Therefore g_e is supported in two strips of total length
4e, its L1 norm is O(e), and its total variation after zero extension
is O(1). The latter includes both endpoint jumps; its interior
variation is bounded by the integrals of |f'|(1-chi_e) and |f chi_e'|.
Integration by parts, with those endpoint terms retained, gives

\[
 |F_{g_e}(\xi)|\le C_f\min(e,|\xi|^{-1})\quad(\xi\ne0),
 \qquad |F_{g_e}(0)|\le C_f e.
\]

Splitting the positive-frequency integral at 1/e gives

\[
 \int_{\mathbb R}(1+\log(2+|\xi|))
       |F_{g_e}(\xi)|^2\,\frac{d\xi}{2\pi}
 =O_f(e\log(1/e))\longrightarrow0.                    \tag{5}
\]

Indeed the portion up to 1/e is bounded by a constant times
e^2 integral_0^(1/e)(1+log(2+xi)) dxi, and the remainder by the
integral of (1+log(2+xi))/xi^2. Both are O(e log(1/e)).
This verifies the Suzuki cutoff mechanism in our Fourier convention;
merely assigning zero endpoint values would not suffice.

We also need convergence in the periodic diagonal form to pass the
other side of Li's identity. Put v_e=sqrt(2) f_e on (0,a).
For q>=1 the cosine coefficient of v-v_e is O(min(e,1/q)):
the L1 estimate gives O(e), and integration by parts against
cos(q*pi*x/a) gives O(1/q) from its uniformly bounded derivative
integral. The boundary sine terms vanish at both 0 and a. The
constant coefficient is O(e). Since |h(k_q)|<=C_a(1+log(2+q)),
the same split, now in a series at q=floor(1/e), yields

\[
 \sum_{q\ge0}(1+\log(2+q))
  |\langle v-v_e,e_q^+\rangle|^2
 =O_f(e\log(1/e))\longrightarrow0.                    \tag{6}
\]

L2 convergence also follows. Formula (4) pays the entire response
form under this limit. Arithmetic is a finite sum of bounded delays;
the pole and all ten moments are bounded representer forms. They
therefore converge, with the same centering and parity factors
already established in C744b. Equations (5)-(6) justify the limit
of Li's smooth compact identity on both sides. Consequently

\[
 \overline E_L(u)+256\|Cu\|^2
 =\langle D_+v,v\rangle+\langle B_p^+v,v\rangle
    +|\langle v,p_+\rangle|^2+256\|C_+v\|^2
    +\sum_{j\ge0}|\langle v,r_j^+\rangle|^2.           \tag{7}
\]

No equality of whole periodic and zero-extension domains, or claim
about the generator domain, was needed. This is a value of the
smooth form closure. In particular we may now add the missing responses
to C744b's certified scalar without reversing its lower inequality.

### 3. All-index scalar remainder with cancellation retained

Let z_q=b_q/2^44 be C744b's unchanged coefficients, n_0=a^(-1/2),
n_q=(2/a)^(1/2) for q>=1, k_q=q*pi/a, and d_q=z_q n_q(-1)^q.
C744b (8) gives exactly

\[
 R_j=\sqrt{1-e^{-2ac_j}}\,S(c_j),\qquad
 S(c)=\sum_{q=0}^{63}\frac{d_qc}{c^2+k_q^2}.
\]

The finite prefix is evaluated with its signed cancellations inside
S before squaring. To pay every j>=N, define S0=sum d_q,
A0>=|S0| and B1>=sum |d_q| k_q^2. For every c>0 the exact identity

\[
 S(c)=\frac{S0}{c}
       -\frac1c\sum_q\frac{d_qk_q^2}{c^2+k_q^2}
\]

implies |S(c)|<=A0/c+B1/c^3. This bound needs no c>max k_q
hypothesis and retains the endpoint cancellation in S0. Since
0<1-exp(-2ac_j)<1, for p>1 the decreasing-function comparison gives

\[
 \begin{split}
 T_p(N):=\sum_{j\ge N}c_j^{-p}
 &\le c_N^{-p}+\int_N^\infty(2x+1/2)^{-p}\,dx\\
 &=c_N^{-p}+\frac{c_N^{1-p}}{2(p-1)}=:U_p(N),\\
 0\le\sum_{j\ge N}R_j^2
 &\le A0^2U_2(N)+2A0B1U_4(N)+B1^2U_6(N).              \tag{8}
 \end{split}
\]

This scalar elementary remainder implements the approved finite-prefix
option; paper60's Fourier covariance-tail index is not substituted for
the physical response index j.

### 4. Certificate, numerical conclusion and limits

The program `scripts/five-cell-penalty/complete-response-459.py` imports
only the audited interval implementation in `certify-455.py` and the
complete saved input `certificate-455.json` from that same directory.
It checks the exact witness, half-width, 64 diagonal indices, all ten
moment indices, all nine prime powers and old response prefix. It
preserves and hashes both old files; neither is overwritten. The old
five scalar contributions and their uncertainties are retained exactly.
Their full proofs and numerical contracts remain canonical in C744b.
For B1 the program sums upper magnitudes of d_q times the enclosed
k_q^2, and uses the resulting upper endpoint in (8). The new program
uses only directed basic interval arithmetic, exp and sqrt from that
implementation; no float special function is evaluated.

Reproduction command:

```sh
python3 scripts/five-cell-penalty/complete-response-459.py
```

Full output is `scripts/five-cell-penalty/complete-response-459.json`.
It records every response projection and square for 128<=j<2048,
the original terms, exact witness, all remainder inputs, hashes,
checks and final interval. For N=2048, c_N=4096.5, the outward
coarsenings are

| Quantity | Enclosure or upper bound |
| --- | --- |
| S0 | [0.00720056657530500226, 0.00720056657530500228] |
| B1 majorant | <10692.84153364051534 |
| Additional prefix sum, 128<=j<2048 | [2.2785777575234464e-7, 2.2785777575234465e-7] |
| Entire remaining sum j>=2048 | [0, 6.715256029384072e-9] |
| Complete restored mass j>=128 | [2.2785777575234464e-7, 2.3457303178172872e-7] |
| Complete penalized form (7) | [2.0418078465924468e-7, 2.1168960422787452e-7] |

All bounds are strictly on the positive side needed for (1)-(2).
The old diagonal uncertainty, approximately 7.94e-10, is included,
as is the entire upper remainder in (8), approximately 6.72e-9.
Even the lower bound from the paid finite added prefix exceeds the
magnitude of the old negative scalar. The upper remainder is required
to enclose the complete value, not to claim an uncomputed sum is zero.

The exact-rational consistency program
`scripts/five-cell-penalty/check-complete-response-459.py` checks every
saved additional square, the prefix sum, the rational expression (8),
aggregation and the strict displayed thresholds. Its complete report is
`scripts/five-cell-penalty/complete-response-checks-459.json`.
These are same-step consistency checks. The separate conceptual and
certificate audit is recorded below; consistency alone does not establish
the response projections or the form-domain identity.

Thus the missing positive responses more than repay this vector's
negative truncated value. There is no all-test inference: positivity
on one non-neutral finite vector cannot establish positivity on U_5
or on its moment complement. No boundedness, coverage or propagation
condition closing L030-L032/C032a follows from this scalar computation.

### Separate conceptual audit — 11 November 2026, step461

**Verdict and source scope.** Equations (1)-(2), the smooth-closure
membership and equality (7) pass this audit. The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-11-11-five-cell-complete-response-audit-459.md`.
This is REPRODUCTION: local validation of a known-method specialization,
not a result beyond the inspected sources. Li's arbitrary-a smooth
identity, Suzuki's cutoff method and paper60's kernel method are the
precisely cited inputs in the Hypotheses. Their numerical positivity
claims and inaccessible supplements are not used. C744b's accepted
step457 audit is reused only for the unchanged contributions.

**Closed form and the two limiting norms.** L744 (8) gives
m(xi)=log(|xi|/(2pi))+O(|xi|^(-2)) for |xi|>=1 and a bounded symbol
on the remaining compact interval. C744b (11) also gives m(xi)>=m(0).
Consequently some fixed shift M makes m+M positive and comparable,
above and below, to 1+log(2+|xi|). This proves semiboundedness and the
claimed equivalence of form norms without any positivity hypothesis
on the unshifted energy. The full-line weighted Fourier form is
closed by the weighted L2 completeness and Plancherel theorem.
Its supported subspace is closed in that norm because norm convergence
implies L2 convergence. The finite arithmetic delays, pole and physical
moment forms are bounded on that supported L2 space. Adding them and
a sufficiently large scalar shift preserves closedness and equivalence
of the form norm. Restriction to the smooth core is therefore closable;
its closure is its closure inside this supported form domain. No
assertion of equality of the two entire domains is needed.

The cutoffs in Section 2 can be chosen with 0<=chi_e<=1, a genuine
interior collar where they vanish, and derivative bounded by C/e.
The centered finite cosine sum is smooth and even, including at zero.
Thus f_e is actually in C_c^infinity(-a,a), rather than merely assigned
zero endpoint values. The two error strips have total length at most
4e. The interior variation of g_e is uniformly bounded: the derivative
of f contributes O(e), and the cutoff derivative contributes O(1).
The jumps of the zero extension at -a and a add only a fixed bound.
The BV integration-by-parts estimate therefore yields
|F_(g_e)(xi)|<=C min(e,1/|xi|), with the L1 bound at zero. Both sides
of the frequency split at 1/e in (5) are O(e log(1/e)); the negative
frequencies are covered by the same estimate. This proves convergence
in the full-line form norm and membership of this particular f in the
smooth closure.

The other limiting norm must be checked separately. For q>=1,
integration by parts of the half-interval cosine coefficient has zero
sine boundary terms at both 0 and a, even though v-v_e need not vanish
at a. Its derivative has uniformly bounded L1 norm. Combining this
O(1/q) bound with the O(e) coefficient bound gives (6); q=0 is O(e).
Indeed e^2 sum_(q<=1/e)(1+log(2+q)) and
sum_(q>1/e)(1+log(2+q))/q^2 are both O(e log(1/e)). The diagonal
weights h(k_q) grow at most logarithmically and are bounded below.
This proves convergence in a shifted diagonal form norm, hence
convergence of its quadratic values by Cauchy-Schwarz in that norm.
The same reasoning applies to the full-line quadratic values.
Neither estimate uses zero-extension H1 membership or a generator
domain assertion; those stronger properties are unnecessary here.

**Full complex response map and equality.** In (3), 2a-t>=t,
c_j>=1/2 and 1-exp(-2c_j a)>=1-exp(-a)=d>0. These give the indicated
pointwise kernel domination for every finite response prefix. For a
complex vector its finite-prefix quadratic form is bounded above by
the double integral of this kernel against |v(t)||v(s)|. The constant
kernel has norm a, and the displayed Schur-weight integral proves
the Carleman bound pi on (0,a). Hence the same bound (4) holds for
every prefix on the original complex L2 space. Increasing the prefix
gives an ell2-valued linear map R with that bound, since the squared
projection sums are nonnegative. In particular
||R(v_e-v)||_ell2 <= sqrt((4a+2pi)/d)||v_e-v||_2 -> 0;
this is convergence of the whole response family, not just each fixed
coordinate. Its squared norm therefore converges too.

Apply the imported smooth identity to every f_e. The two separately
verified form limits, the bounded response map and the bounded prime,
pole and ten moment maps pass every term to the limit. Centering is
unitary; in the even parity map F_f(+-i/2)=<v,p_+>/sqrt(2), so the
full pole product is exactly |<v,p_+>|^2. The unchanged full-interval
coefficients z_q n_q/sqrt(2) still enter the physical moments and
arithmetic correlations, while z_q n_q enters the half-interval
responses. C744b's accepted normalization thus gives exactly (7).
This equality is established by limits on both sides, not by reversing
C744b's lower inequality.

**Entire scalar chain.** The response integral in C744b (8) has the
same c_j, frequency and square-root factors as Section 3. Its signed
sum is formed before squaring. The exact identity preceding (8) is
valid for all positive c, including the q=0 term; no large-frequency
expansion or unproved condition c>k_q is used. The triangle inequality
then gives |S(c)|<=A0/c+B1/c^3. Squaring this nonnegative bound gives
the three terms with coefficient 2 in the middle. Multiplication by
1-exp(-2ac)<1 can only decrease the true response square. The
decreasing-series integral bound at c_N=4096.5 covers every omitted
j>=2048, including its first term. It neither discards a physical
response nor substitutes a Fourier-index covariance tail.

All 108 lines of the new evaluation program and all 78 lines of its
consistency checker were inspected, together with the reused interval
operations and initialization. Positive denominator intervals avoid
zero. The exact dyadic coefficients, 64 frequencies, normalizations,
exp arguments and square-root arguments implement the displayed
projection formula. Directed basic operations, exact copy_abs and
copy_negate, and adjacent-number widening for exp/sqrt use the
previously assessed Decimal contracts. The B1 interval need not
enclose the exact sum of |d_q|k_q^2 from below: its upper endpoint
is a majorant because each |d_q| is replaced by the upper magnitude
of its interval and k_q^2 is nonnegative. The tail polynomial is
increasing in these nonnegative majorants, which justifies its use.
The old five scalar uncertainties are retained when adding the new
prefix and the interval [0,tail_upper].

Reproduction command for this separate audit:

```sh
python3 scripts/five-cell-penalty/audit-complete-response-461.py
```

The complete report is `scripts/five-cell-penalty/replay-461/audit.json`.
The old source and input hashes agree exactly with the accepted
step457 audit, so all 64 old diagonal enclosures, nine prime-power
terms, 128 old response projections and ten physical moments remain
the audited inputs. The new source replays with only its output path
changed: all 17 top-level certificate fields reproduce byte for byte.
The original consistency report also reproduces byte for byte. All
seven pre-existing source/certificate/audit artifacts read by this
audit are preserved.

In addition, all 1920 new projections were enclosed at 110-digit
precision using the algebraically regrouped expression

\[
 a^{-1/2}\sqrt{1-e^{-2ac_j}}
 \left[\frac{z_0}{c_j}+\sqrt2\,c_j
       \sum_{q=1}^{63}\frac{(-1)^qz_q}{c_j^2+k_q^2}\right].
\]

The positive and negative summands are accumulated separately.
The constants pi and a are recomputed with the same proved Machin
remainder and contracted logarithm, and lie within the accepted old
enclosures. Every refined projection interval is contained in its
saved 70-digit interval; none is checked only by a preview. This is
a different grouping and precision, not an independent implementation
of exp/sqrt. The full refined evidence is
`scripts/five-cell-penalty/replay-461/refined-projections-110.json`.

Exact Fraction arithmetic checks the ordering of all saved intervals,
each saved square against its entire projection interval, all 1920
prefix terms, S0/A0, the B1 majorant, the three rational series
expressions, the full tail polynomial, both aggregations and every
displayed outward coarsening. All 9655 checks pass without failures.
In particular the full tail upper endpoint is
6.715256029384071622963753554542085462895585722401763404087183930247929e-9.
The complete scalar lower endpoint is
2.041807846592446887123238795645399683688680931171271609176280631771240e-7,
and its upper endpoint is
2.116896042278745163647012095801456334419837024266806801700172105642099e-7.
These lie strictly within (1); the restored-mass endpoints also lie
strictly within (2). No further refinement is needed for this test.

**Scope of the accepted result.** The witness's first physical moment
still has an interval strictly below zero, so the witness is not
neutral. The result concerns its complete penalized form value only.
It supplies no lower eigenvalue for a finite compression or the whole
operator, no paid moment complement and no all-window propagation.
C744b's negative truncated comparison is still valid; this result
identifies a positive omitted contribution large enough to repair
that single direction. Actual-Xi positivity remains unresolved.

## Mathlib

Full matching Mathlib coverage of this fixed complete-response scalar,
its domain specialization or its interval certificate has not been
checked; no absence claim or formal verification is made. The source
response identity and smooth-core/Carleman methods are known inputs.
The present normalization, finite bounds and enclosure are local
specializations accepted by the separate audit above; they have not
been formally verified in Mathlib.
