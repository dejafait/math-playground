# C744f: Complete five-cell even64-to-distant Schur comparison

## Hypotheses

Fix ell=log(3)/2, a=5ell/2, the even half-interval space L2(0,a),
C744b(1)-(3)'s orthonormal cosine basis, its ten physical moments C_+,
all nine active prime powers and penalty256. Let D e_q=h(k_q)e_q,
k_q=q*pi/a, h(k)=Re psi(1/4+ik/2)-log(pi). Use the complete form

    H = D + B_p + p tensor p + R*R + 256 C_+* C_+,

where R contains every response r_j, j>=0, and the even pole has
positive sign. Its diagonal form domain is

    V_D = {v: sum_(q>=0)(1+log(2+q)) |v_q|^2 < infinity}.

Only membership of this domain in the zero-extension smooth form
closure, proved below, is needed. No generator-domain enlargement,
full domain equality, exact neutrality or RH is assumed.

Let P retain q=0,...,63 and Q retain q>=4096; the intervening modes
are excluded. M=PHP is C744e's accepted exact complete matrix. B is
its saved invertible finite-decimal lower triangular congruence,
treated as an exact rational matrix. C744e's accepted step466 audit gives

    ||B M B^T-I||_2 <= epsilon < 1.774e-14.

Use rho=C_nr(2a) from C744a(3)-(4), with its specialization and
arithmetic audited in C744b, and t_q=h(k_q)-rho for q>=4096.
C744b gives increasing t_q and t_4096>1.76988. Define complete columns
c_q=P H e_q (the off-diagonal bounded operator, equivalently the
polarized form), and

    R_cov = sum_(q>=4096) c_q c_q^* / t_q,   G=M-R_cov.

The imported smooth identity is Hongmin Li, *Cutoff-free positivity of
localized Weil forms through the (log 11)/2 threshold*,
[paper45 displayed v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma3.1 and (2.1)-(2.5); its form comparison and weighted covariance
method are (4.6)-(5.5). The complete-response/divided-difference,
zero-mode, combined-source and separated-tail methods are
[bramble_trace, paper60 displayed v1, 26 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/60),
Sections2-3, (6.2)-(6.8), (7.1)-(7.7). No numerical source sign,
radius2 constant or inaccessible supplement is imported. C744c's
accepted bounded complex response map and C744e's smooth-cutoff and
finite arithmetic contracts apply at this a. L744(8)'s audited
digamma remainder is used for tail weights, not replaced by an
unenclosed special-function call. These are known inputs; the fixed
certificate is REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-distant-covariance-test-467.md`,
separately approved at step468.

## Conclusion

The complete covariance obeys

\[
 \operatorname{tr}(B R_{\rm cov}B^T)
 =\sum_{q\ge4096}\frac{\|Bc_q\|^2}{t_q}
 <0.289114<1-\epsilon.                                      \tag{1}
\]

In particular G is positive definite; more conservatively
BGB^T>0.709 I. The complete penalized form is strictly positive
on every nonzero vector of V_D in P L2 plus Q L2. This pays one
infinite block interaction, not the omitted modes64-4095, the odd
sector, exact-neutral full-space positivity, all windows or actual-Xi
positivity. RH remains unresolved.

The separate conceptual audit below (11 November2026, step471)
accepts this certificate and the stated two-block form-domain claim.
It is local progress within the inspected methods and makes no claim
of progress beyond the source claims.

## Proof

### Block domain, complete responses and the original distant floor

C744c proves R bounded from complex L2(0,a) to ell2. The finite
prime-delay sum, pole and physical moment forms are bounded on L2
as well. Thus H is a closed semibounded form on V_D. For any finite
cosine sum, the smooth interior cutoff argument in C744c/C744e
applies with constants depending on that finite sum: the collar
error has Fourier and cosine coefficients bounded by
C min(delta,1/|frequency|), with constant coefficient O(delta).
Both shifted logarithmic form errors tend to zero as
O(delta log(1/delta)). All bounded terms, including the whole
response map, converge in L2. The imported smooth identity therefore
identifies H with the zero-extension smooth form closure on every
finite cosine sum. This argument uses no bound uniform in its degree.

For a general vector in V_D, its finite cosine partial sums are
Cauchy in a sufficiently shifted H form norm, because H-D is bounded.
On their differences that norm is exactly the shifted smooth-closure
norm just identified. Closedness of the latter, together with L2
convergence, gives membership and equality for the limiting vector.
This proves the needed inclusion, without asserting its converse.

On Q, C744a's arithmetic bound gives B_p>=-rho I. The complete even
pole, response and penalty forms are nonnegative. Hence QHQ>=T,
where T is the positive diagonal form with entries t_q. In particular
the original rho remains valid for the complete form. Since H-D is
bounded, the cross operator C=P(H-D)Q is bounded. Its rows are ell2,
so the covariance converges, since t_q>=t_4096>0. The estimates below
give its explicit quantitative bound.

### Complete combined columns, including zero mode and moments

Put n_0=a^(-1/2), n_s=(2/a)^(1/2) for s>0, u_s=k_s^2,
c_j=2j+1/2 and alpha_n=log(p)/sqrt(n) for each active n=p^m.
Define the convergent sums

\[
 T(u)=\sum_{j\ge0}\frac{u}{c_j^2+u},\quad
 T_e(u)=\sum_{j\ge0}\frac{e^{-2ac_j}u}{c_j^2+u},\quad
 W(u)=T(u)-T_e(u),\qquad
 Z_s=W(u_s)+\sum_n\alpha_n k_s\sin(k_s\log n).          \tag{2}
\]

T(0)=T_e(0)=0. For q>=4096, write k=k_q, v=k^2 and define
Z(v) by the same expression with k in place of k_s. For these
disjoint labels the prime-plus-response cross entry is exactly

\[
 n_s n_q(-1)^{s+q}\frac{Z(v)-Z_s}{v-u_s}.              \tag{3}
\]

For the response part this follows term by term from

\[
 \frac{v/(c^2+v)-u/(c^2+u)}{v-u}
       =\frac{c^2}{(c^2+u)(c^2+v)}.
\]

The sums are absolutely convergent, so subtraction and summation
are justified. For a prime delay d, C744e(2)'s two sine-integral
terms have frequencies k-k_s,k+k_s. Since their half-overlap is
a-d/2, their sines are (-1)^(q+s+1) times the corresponding
sines at (k+-k_s)d/2. Product-to-sum gives the bracket

    (-1)^(q+s+1) [k sin(kd)-k_s sin(k_s d)]/(v-u_s).

Multiplication by -alpha_n n_s n_q gives precisely the prime
part of (3). This also checks s=0: its prime entry is
alpha_n n_0 n_q(-1)^q sin(kd)/k. No repeated-label denominator
or zero-frequency limit is used here.

Write w_is=B_is n_s(-1)^s. Define

\[
 A_i(v)=\sum_{s<64}\frac{w_{is}}{v-u_s},\qquad
 D_i(v)=\sum_{s<64}\frac{w_{is}Z_s}{v-u_s}.             \tag{4}
\]

The B transform of (3) is n_q(-1)^q[Z(v)A_i(v)-D_i(v)].
All prime and response contributions are combined before estimates.

Let b_i=(Bp)_i for C744e's physical pole row p, and put
P_i=b_i exp(a/2)(1-exp(-a))/2. Its cross contribution is exactly
n_q(-1)^q P_i/(v+1/4). For each moment row m_(j,sigma), put
b_(i,j,sigma)=(Bm_(j,sigma))_i, beta=sigma/2,
l_j=2j-5, r_j=2j-3 and e_-=exp(-sigma ell/4), e_+=exp(sigma ell/4).
For each residue r modulo10 define the vectors

\[
 U_{r,i}=256\sum_{j,\sigma}b_{i,j,\sigma}
       [e_+\sin(rr_j\pi/5)-e_-\sin(rl_j\pi/5)],\qquad
 V_{r,i}=256\sum_{j,\sigma}\beta b_{i,j,\sigma}
       [e_+\cos(rr_j\pi/5)-e_-\cos(rl_j\pi/5)].         \tag{5}
\]

The arguments use the residue times the cell edge integer. Exact
periodicity makes these formulas valid for every integer q with
r=q mod10. C744b's physical 1/sqrt(2) normalization gives the full
transformed column

\[
 y_i(q):=(Bc_q)_i
 =n_q(-1)^q\left[Z(v)A_i(v)-D_i(v)+\frac{P_i}{v+1/4}\right]
   +\frac{n_q}{\sqrt2}\frac{kU_{r,i}+V_{r,i}}{v+1/4}.   \tag{6}
\]

Every term in (6) is included before squaring its sum. Thus response,
prime, pole and moment mixed terms are retained. This specialization
is necessary because the source's displayed source family omits
the added ten physical penalty sources.

### Directed finite prefix and its complete-response enclosure

The core T(u_s) uses the accepted C744e inverse-power sums
S_p=sum_(j>=512)c_j^(-p), first512 direct summands and32 terms:

    T(u)=sum_(j<512)u/(c_j^2+u)
          +sum_(m=0)^31 (-1)^m u^(m+1) S_(2m+2) + error,
    |error| <= u (u/c_512^2)^32 S_2.

The finite geometric identity, with denominator 1+u/c_j^2>=1,
proves the remainder including u=0. T_e is evaluated through j=63;
every j>=64 is bounded by exp(-2ac_64)/(1-exp(-4a)). This is the
sum of the geometric exponential majorant; u/(c_j^2+u)<=1.

For the distant T(k^2), f(x)=k^2/((2x+1/2)^2+k^2) decreases, so

\[
 I(k)\le T(k^2)\le I(k)+\frac{k^2}{k^2+1/4},\qquad
 I(k)=\frac{k}{2}\left[\frac\pi2-\arctan\frac1{2k}\right]. \tag{7}
\]

Here integral_0^infinity f=I(k), and the decreasing sum/integral
comparison includes the first term. The alternating arctan polynomial
through x^9 has error at most x^11/11. T_e uses j<16 and the entire
remaining exponential majorant exp(-2ac_16)/(1-exp(-4a)). Thus (7)
is an enclosure of all responses, though deliberately coarse.

For stable evaluation of (4) put U=u_63, K=16 and

    a_im=sum_s w_is (u_s/U)^m,
    d_im=sum_s w_is Z_s (u_s/U)^m,  0<=m<K.

Then A_i(v) and D_i(v) are respectively 1/v times their polynomials
in U/v, with errors bounded by

    W_i (U/v)^K/(v-U),    W'_i (U/v)^K/(v-U),
    W_i=sum_s |w_is|,     W'_i=sum_s |w_is Z_s|.          (8)

This is the finite geometric identity with v>U. In the finite prefix
one may use the values at q=4096 as uniform error majorants because
both factors decrease with v. Signed coefficients are summed before
taking the tail magnitudes. This controls the otherwise severe B
cancellation; no floating inverse or discarded small term is used.

For every 4096<=q<16384, the program encloses (6) and uses

    t_q >= log(q/(2a))-2/k_q^2-rho =: lower_t_q >0,      (9)

from L744(8), since k_q>=1. The log remainder bound applies at all
these positive frequencies. Division by the lower bound explicitly
pays the loss from replacing the true weights; no sampled weight
is silently substituted. Nine prime phases use directed sine/cosine,
with interval rotation and a fresh evaluation at each32 labels.
Each interval rotation encloses the exact addition formulas; no
assumption of independent or equidistributed phases is made.

The saved outward finite trace upper bound is

    sum_(4096<=q<16384) ||y(q)||^2/lower_t_q
       <= 0.07809639639998459846727514764730614687634680120901821640701204843710669.

All 12,288 columns, all 64 components, scalar enclosures and weights
are saved, not just an eigenvalue preview.

### Entire q>=16384 remainder

Set E=16384, k_E=E*pi/a, v_E=k_E^2 and R_E=U/v_E<1.
For every v>=v_E, define nonnegative component majorants

    e_i=sum_(m=1)^15 |a_im| R_E^m + W_i R_E^16/(1-R_E),
    d_i=sum_(m=0)^15 |d_im| R_E^m + W'_i R_E^16/(1-R_E).

They imply |v A_i(v)-a_i0|<=e_i and |v D_i(v)|<=d_i,
by (8). Write a0=(a_i0), e=(e_i), d=(d_i), and
N=norm_2((|a_i0|+e_i)_i). Every norm below is upper bounded by
directed sums of squared component magnitudes and sqrt.

Let alpha=sum_n alpha_n, Cmax=pi/4+alpha and
E0=exp(-a)/(1-exp(-4a)). Formula(7), atan x<=x and T_e<=E0 give

    Z(v)=k[pi/4+sum_n alpha_n sin(k log n)]+delta(k),
    |delta(k)|<=1+E0.                                  (10)

This holds for all k>=k_E, not only saved labels. In particular the
prime phases are bounded in absolute value by1 in the entire tail.
Combine the fixed leading response and moment vectors before taking
their norm. For each residue r define

\[
 A_r=n_q\left(\|(-1)^r(\pi/4)a0+U_r/\sqrt2\|_2
                     +\alpha\|a0\|_2+Cmax\|e\|_2\right),\qquad
 B_r=n_q\left((1+E0)N+\|d\|_2+\|P\|_2
              +[\|V_r\|_2+\|U_r\|_2/(4k_E)]/\sqrt2\right). \tag{11}
\]

The triangle inequality in (6) now proves

    ||y(q)||_2 <= A_r/k_q + B_r/k_q^2, q>=E, r=q mod10. (12)

Indeed the A(v) leading term times k gives a0/k; its error
contributes Cmax||e||/k. The delta term costs (1+E0)N/k^2.
D and the pole cost ||d||/k^2 and ||P||/k^2. Finally
k/(k^2+1/4)-1/k=-1/[4k(k^2+1/4)], whose magnitude is at most
1/(4k_E k^2); the V_r denominator is at most1/k^2.
These prove each term of (11), including the denominator correction.

The directed maxima over all ten residues are

    A_* <236.996,   B_* <147380,
    lower_t_E >3.15619206678320118.

The true t_q is increasing; (9) at E is a valid positive lower
bound for every tail weight. For p=2,3,4, decreasing sum/integral
comparison gives

    sum_(q>=E) q^(-p) <= E^(-p)+E^(1-p)/(p-1)=S_p^E.

With a_*=A_* a/pi, b_*=B_*(a/pi)^2, (12) yields the full bound

\[
 \sum_{q\ge E}\frac{\|y(q)\|^2}{t_q}
 \le\frac{a_*^2S_2^E+2a_*b_*S_3^E+b_*^2S_4^E}
             {\mathrm{lower\_t}_E}
 \le0.2110174102899625595866476973955331988084504659373426208110505541110446.
                                                               \tag{13}
\]

The first omitted index E is included. No asymptotic onset or
uncontrolled response/frequency exchange is needed in (12)-(13).

### Certificate, strict sign and limits

Commands, relative to the notebook:

```sh
python3 scripts/five-cell-penalty/distant-469.py
python3 scripts/five-cell-penalty/distant-trace-469.py
python3 scripts/five-cell-penalty/check-distant-469.py
```

The first program saves `distant-469.json`. Its complete direct
q=4096 column gives ||Bc_4096||^2 in
[0.0001162032964452587120657946408101873,
 0.0001162032964452587120657946408101878]. Its proposed rational
negative-direction test instead has positive comparison value near
2.55908e-39 and is inconclusive about G. This diagnostic is preserved;
it is not a negative result or the full sign proof. The final proof
uses only its core T values and checks all transformed q=4096
intervals against that direct calculation.

`distant-trace-469.json` saves every combined coefficient, prefix
column and entire-tail bound. The two upper bounds above sum outward to

    0.2891138066899471580539228450428393456847972671463608372180626025481513,

strictly below 1-epsilon, whose accepted lower bound is

    0.9999999999999822640999755138953936410962266284328034154949509298021911.

All operations use C744b's audited70-digit directed interval library
and explicit elementary remainders. The congruence B is unchanged.
The integer checker replays every transformed column using 110-digit
fixed-scale integer interval operations, all squared norms, all
weighted contributions, prefix aggregation, tail scalar expression
and the strict threshold. All 823,342 checks pass with no failures.
Its saved report is
`scripts/five-cell-penalty/distant-checks-469.json`. It also checks
the core hash against the accepted step466 audit and preservation
of all inputs. These are same-step arithmetic checks; they do not
replace conceptual review of (2)-(13) or independently implement
transcendental functions.

For positive semidefinite finite-dimensional B R_cov B^T, its
operator norm is at most its trace, by the spectral theorem. Monotone
partial covariance sums and (1) justify the trace identity and limit.
C744e's residual bound therefore gives BGB^T>0.709 I and G>0.
This is a complete-covariance bound, not a failed-Cholesky inference.

For x in P and y in Q in the form domain, apply the QHQ>=T bound
and weighted Cauchy-Schwarz, or square completion, to obtain

    H[x+y] >= x*Gx + ||T^(1/2)y + T^(-1/2)C*x||^2.

T^(-1/2)C*x is defined since T>=t_4096 I>0. The identity follows
first for finite sequences and then in the form norm; equivalently
T^(-1)C*x lies in the T form domain since C*x is ell2. If x!=0 the
first term is strictly positive; if x=0 and y!=0 the second is.
The previously proved smooth-closure inclusion identifies this with
the complete physical penalized form on the specified two-block space.

No Fourier projection is asserted to preserve Cu=0. No sign is
claimed after restoring the missing middle modes, their cross terms,
the odd pole or other windows. Those are independent unresolved gaps.

### Separate conceptual audit — 11 November 2026, step471

This REPRODUCTION audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-distant-schur-audit-469.md`,
separately approved at step470. It accepts (1) and the precise
two-block positivity conclusion. No mathematical error requiring a
changed constant was found. The analytic imports and arithmetic
contracts in the Hypotheses remain inputs; neither source numerical
signs nor inaccessible supplements are inputs.

**Closed form and inclusion.** L744(8) and bounded low-frequency
digamma values make a sufficiently shifted D norm equivalent to the
V_D norm. C744c's accepted complex response bound makes the WHOLE
R*R bounded on L2. The other perturbations are bounded self-adjoint
forms, so H is closed and semibounded. Choose one sufficiently large
shift for H and the physical smooth-form closure; this assumes no
positivity of either unshifted form. C744c/C744e's cutoff proof applies
to every finite cosine sum, separately to its real and imaginary parts.
Its zero-extension BV estimate includes the endpoint jumps; its
cosine integration by parts has zero sine boundary terms. Both squared
logarithmic errors are O(delta log(1/delta)), with constant coefficient
O(delta). All bounded terms, including the whole R map, converge in
L2. Hence every finite sum belongs to the physical closure and has
exactly H's value. This also applies to differences of finite sums.

For v in V_D, its finite partial sums are Cauchy in the shifted H
norm, hence in the SAME physical norm on those differences. Closedness
and L2 convergence identify the physical limit with v. This proves
the needed inclusion and equality without a degree-uniform cutoff
estimate, converse domain theorem or generator-domain claim. C744a's
supported prime bound, as accepted in C744b step457, restricts to Q;
the even pole, response and penalty terms are nonnegative. Thus QHQ>=T.
The digamma difference has increasing nonnegative summands
2k^2/[c_j(c_j^2+k^2)], so the accepted t_4096 floor applies throughout
Q. T has the same logarithmic form weights. Since H-D is bounded,
C=P(H-D)Q is bounded and C*x is in ell2. The positive lower bound
on T justifies covariance convergence and T^(-1/2)C*x.

**Complete columns.** Each T(u) is absolutely convergent, bounded
termwise by u/c_j^2, so the response divided difference can be summed
including u=0. For the prime term put A=(k-k_s)d/2 and B=(k+k_s)d/2.
The sine bracket is
(-1)^(q+s+1)[sin(A)cos(B)/(k-k_s)+sin(B)cos(A)/(k+k_s)].
Its numerator over v-u_s is k sin(kd)-k_s sin(k_s d).
Multiplication by -alpha_n n_s n_q gives (3), including its sign.
At s=0 the entry is alpha_n n_0 n_q(-1)^q sin(kd)/k, with
n_0=a^(-1/2); no denominator vanishes for the separated labels.
All nine base-prime logarithms are retained.

Integrating 2cosh(x/2) against n_q cos(k_q x) gives
n_q(-1)^q exp(a/2)(1-exp(-a))/[2(v+1/4)], verifying P.
C744b(10)'s physical antiderivative gives n_q/sqrt(2) times
[k sine difference + beta cosine difference]/(v+1/4), with endpoint
factors exp(+-sigma ell/4). The six endpoints have angles
q*edge*pi/5, for edge=-5,-3,-1,1,3,5. These have period10 in q,
including parity. Thus (5)-(6) retain the exact physical normalization.
Every response/prime/pole/moment term is combined before squaring;
the real symmetric entries also define the complex Hermitian form.

**Scalar enclosures and prefix.** The first 64 core T values are the
only load-bearing output of `distant-469.json`. Each is recomputed
from the accepted step466 inverse-power sums at 512 using the finite
geometric identity and its positive-denominator remainder. Every
field of all 64 records reproduces exactly, including u=0, direct 512
sums, ratios and errors. The diagnostic's new inverse powers at 65536
and proposed negative direction are not needed for (1), and are not
rerun or promoted by this audit.

For fixed k>0 the summand in (7) decreases on [0,infinity); integration
gives its displayed I(k), proving both endpoints with the first term
included. The arctan argument lies in (0,1) throughout the prefix,
so its alternating polynomial and x^11/11 error are valid. Both
exponential majorants include every omitted index. In (8), the last
geometric term is (u_s/v)^16/(v-u_s); summing absolute coefficients
and using u_s<=U<v proves the error. Both factors decrease with v,
justifying the uniform 4096 bound. Signed B sums are retained in the
polynomial coefficients. The replay recalculates all those scalars,
combined coefficients, ten residue vectors and all 12,288 columns.

Prime phases are recomputed every 32 labels; each intervening interval
rotation contains the exact addition formulas. Every trigonometric
guard succeeds, with no statistical phase assumption. L744(8) gives
(9) since log(k_q/(2pi))=log(q/(2a)), with the correct lower sign
on 2/k_q^2. Every prefix lower weight is positive and each division
uses that lower endpoint. Directed arithmetic, widened correctly
rounded exp/ln/sqrt and accepted Taylor errors justify these scalar
enclosures; the integer checker alone would not establish them.

**Entire remainder.** Equation(7) and atan(x)<=x imply
-1/4<=T(k^2)-pi*k/4<=1. Since 0<=T_e<=E0, (10)'s conservative
absolute error 1+E0 holds for every k>=k_E. The e_i,d_i majorants use
U/v_E<1 and the full geometric remainder, not sampled frequencies.
The leading moment vector combines with (-1)^r(pi/4)a0 before its
norm is taken. The remaining prime leading term costs alpha||a0||
and the A-column error costs Cmax||e||. The delta, D and pole terms
give exactly the k^(-2) bounds in (11). Replacing the sine moment
denominator costs ||U_r||/[4sqrt(2)k_E k^2], and its cosine term costs
||V_r||/[sqrt(2)k^2]. This accounts for the potentially missed
k^(-3) term without discarding it. All norms use directed sums of
squared component magnitudes and square roots.

The full replay verifies A_*=236.995419164945545...<236.996,
B_*=147379.714881727733...<147380 and
lower_t_E>3.15619206678320118; their FULL stored values enter (13).
Monotonicity and positivity of the original t_q justify that tail
denominator. For p=2,3,4, E^(-p)+integral_E^infinity x^(-p)dx
includes q=E and every later integer. Squaring (12) retains its cross
term 2a_*b_* and proves precisely (13), with no asymptotic onset,
unpaid response tail or unverified frequency exchange.

**Complete evidence and implication.** Reproduction command:

```sh
python3 scripts/five-cell-penalty/audit-distant-471.py
```

All 141 audit checks and all 823,342 fixed-scale integer checks pass
with no failures. The complete 182,820,629-byte trace certificate and
full integer report reproduce byte for byte. All 12 old artifacts
are preserved. Full evidence is in
`scripts/five-cell-penalty/replay-471/audit.json`, `core-T.json`,
`distant-trace-469.json` and `distant-checks-469.json` in that directory.
This is complete replay and formula verification under the accepted
arithmetic contracts, not an independent transcendental implementation.

Exact finite-decimal comparisons give total trace
0.2891138066899471580539228450428393456847972671463608372180626025481513
<0.289114<1-epsilon, with the latter lower bound recorded above.
The report also checks 1-epsilon-total>0.709 by exact rational
arithmetic. Monotone positive covariance sums, the finite-dimensional
norm<=trace bound and C744e's accepted residual give BGB^T>0.709 I;
B is invertible by that accepted certificate. Moreover T^(-1)C*x
belongs to T's form domain because T has a positive lower bound and
C*x is in ell2. Square completion is therefore legitimate on the
entire claimed form domain. If x!=0 its G term is positive; if x=0
and y!=0 its T term is positive. No uniform full-space or neutral sign
has been inferred.

The truncated 128 stop, coarse-box obstruction, inaccessible source
artifacts and inconclusive first-column diagnostic remain unchanged.
This audit resolves only the conceptual-review qualification of this
fixed two-block result. Middle 64-4095, odd sector, exact-neutral
full-space transfer and all-window positivity remain open.

## Mathlib

Full matching Mathlib coverage of this physical complete-response
Schur specialization and interval certificate is unchecked. No
formal verification or absence claim is made. Smooth-core, divided-
difference, covariance, geometric-series and finite congruence methods
are imported known mathematics with the necessary local normalization
and quantitative certificate above. The local sign and domain inclusion
pass the separate conceptual audit above; no formalization is claimed.
