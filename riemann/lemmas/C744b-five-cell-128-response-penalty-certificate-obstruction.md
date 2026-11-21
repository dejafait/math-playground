# C744b: The fixed five-cell 128-response penalty certificate has a negative retained direction

## Hypotheses

Put ell=log(3)/2, L=5ell and a=L/2. Use L744 (6)'s complete smooth
energy E_L on the original complex space L2(0,L), L743's full arithmetic
operator and neutral class U_5, and only C744a (4)'s supported arithmetic
bound. No fixed H2 cap or conditional assertion of L742 is used.

The physical moment map has exactly the normalization

\[
 (Cu)_{j,\sigma}=\int_0^\ell e^{\sigma(s-\ell/2)/2}
                 u(s+j\ell)\,ds,
 \qquad 0\le j<5,\quad \sigma\in\{1,-1\}.
 \tag{1}
\]

Translate to (-a,a), and identify parity epsilon with L2(0,a) by
f(x)=v(x)/sqrt(2), f(-x)=epsilon v(x)/sqrt(2), x>0. Denote the induced
moment map by C_epsilon. Use the source's orthonormal bases

\[
 e_0^+=a^{-1/2},\quad e_q^+=(2/a)^{1/2}\cos(q\pi x/a)\ (q\ge1),
 \qquad e_q^-=(2/a)^{1/2}\sin((q+1/2)\pi x/a).
 \tag{2}
\]

Let k_q^+=q*pi/a, k_q^-=(q+1/2)*pi/a and
D_epsilon e_q^epsilon=h(k_q^epsilon)e_q^epsilon, where
h(t)=Re psi(1/4+it/2)-log(pi). Let B_p^epsilon be the parity restriction
of **minus** L743's arithmetic operator. Thus its quadratic form is
-2 sum Lambda(n)/sqrt(n) Re integral f(x+log(n)) conjugate(f(x)) dx.
Every active prime power is retained. Define

\[
 c_j=2j+\tfrac12,\quad
 r_j^\epsilon(x)=
 \frac{e^{-c_ja}(e^{c_jx}+\epsilon e^{-c_jx})}
      {\sqrt{1-\epsilon e^{-2c_ja}}},\qquad
 p_\epsilon(x)=e^{x/2}+\epsilon e^{-x/2}.
 \tag{3}
\]

The fixed lower comparison under test is the closed semibounded form

\[
 H_\epsilon=D_\epsilon+B_{\rm p}^\epsilon
   +\epsilon p_\epsilon\otimes p_\epsilon
   +\sum_{j=0}^{127}r_j^\epsilon\otimes r_j^\epsilon
   +256C_\epsilon^*C_\epsilon.
 \tag{4}
\]

P_epsilon retains q=0,...,4095 and Q_epsilon=I-P_epsilon. The proposed
covariance prefix ends at q=16384. Write M_epsilon=P_epsilon H_epsilon
P_epsilon. No alternate response count, penalty, basis or moment
normalization is included in this assertion.

Primary analytic imports, with their exact scope:

- Hongmin Li, *Cutoff-free positivity of localized Weil forms through
  the (log 11)/2 threshold*, [paper45 displayed v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
  (2.1)–(2.5), **Lemma 3.1**, and (4.6)–(5.5). Lemma 3.1 gives the
  arbitrary-a response identity on smooth compact parity tests. Its
  Green identity and convergence argument are imported, not reproved.
  Sections 4–5 supply the comparison, complete covariance and Schur
  method; their numerical constants and endpoint certificate are not
  imported. Our window exceeds that paper's certified endpoint.
- [NIST DLMF 5.4.14](https://dlmf.nist.gov/5.4.E14) and
  [5.4.19](https://dlmf.nist.gov/5.4.E19), for integer and rational
  digamma values. The latter at p=1,q=4 gives
  psi(1/4)=-gamma-pi/2-3log(2).
- [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) and
  [5.11(ii)](https://dlmf.nist.gov/5.11#ii), already used in L744:
  for real N>0, |psi(N)-log(N)+1/(2N)|<=1/(12N^2).
- The [Python Decimal arithmetic contract](https://docs.python.org/3/library/decimal.html),
  in particular directed basic arithmetic, correctly rounded exp/ln/sqrt
  and next_minus/next_plus. The certificate below uses no noninteger
  Decimal power function and no floating special-function evaluation.

These supporting formulas implement the unchanged preapproved test.
They do not import paper45/paper60's inaccessible numerical artifacts.

## Conclusion

There is an explicit real even vector v in span(e_0^+,...,e_63^+) with

\[
 1<\|v\|^2<1.000000000000004,\qquad
 -2.368\,10^{-8}<\langle H_+v,v\rangle<-2.288\,10^{-8}<0.
 \tag{5}
\]

Thus M_+ is not positive definite. In particular no positive Schur
lower matrix G<=M_+-C_cross T^(-1) C_cross^* can exist for this fixed
comparison with T>0. The entire-complement diagonal floors supplied
by C744a are, nevertheless, strictly positive:

\[
 t_{4096}^+>1.76988,\qquad t_{4096}^->0.82159.
 \tag{6}
\]

This is an informative failure of the specified lower certificate,
not a failed pivot or merely a nonpositive scalar lower bound.
It establishes no negative value of the actual complete penalized
energy, no negative U_5 test and no result against RH. The separate
conceptual audit below (11 November 2026, step457) accepts this local
certificate within that scope. The fixed quantitative
obstruction is POTENTIALLY_NEW only relative to the prior inspected
search; the response and Schur methods are known.

## Proof

### 1. Centering, constraints, parity and the lower form

Set f(x)=u(x+a). Its Fourier transform is exp(iaz) times that of u.
For real z this preserves the Fourier modulus; at z=+i/2 and -i/2
the factors are reciprocal positive reals, so L744's pole product is
unchanged. Correlations and the L2 norm are translation invariant.
Thus the centered complete form has exactly Li (2.1)'s normalization.

The five cell centers are t_j=(j-2)ell, and (1) becomes
integral over (t_j-ell/2,t_j+ell/2) of exp(sigma(x-t_j)/2)f(x) dx.
Each moment is L2-bounded: its representer has squared norm
2sinh(ell/2). The ten representers are linearly independent, since
they have disjoint cell interiors and the two exponentials in each
cell are independent. Hence C has rank ten and C*C is bounded positive.
The equations Cu=0 agree with L743's moments, multiplied by the
nonzero factors exp(-sigma ell/4); in particular C vanishes on U_5.
We do not assert that a Fourier projection preserves those equations.

Under reflection f(x)->f(-x), moment (j,sigma) becomes (4-j,-sigma).
This is a unitary permutation of the ten outputs. Hence C*C commutes
with reflection, and its complex quadratic form splits into the two
parities without mixed terms. The original form has the same symmetry.
In each half-interval identification its pole is
epsilon |<v,p_epsilon>|^2. The odd pole is negative and is retained.

Li's arbitrary-a identity gives, on the smooth compact parity core,

\[
 E_L(u)+256\|Cu\|^2
 =\langle H_\epsilon v,v\rangle
    +\sum_{j\ge128}|\langle v,r_j^\epsilon\rangle|^2
 \ge\langle H_\epsilon v,v\rangle.
 \tag{7}
\]

All terms added to D in (4) are bounded self-adjoint operators:
there are finitely many supported delays and L2 representers. Thus
H is a closed semibounded form on the diagonal form domain. If using
the source's full form closure, its smooth-core comparison extends
exactly by Li (4.7)–(4.8): adding a bounded moment form preserves the
core, and a target-form Cauchy sequence is also Cauchy in the shifted
lower-form norm. No identity between a periodic Fourier domain and
the full zero-extension domain is asserted. For the obstruction
itself, the finite vector v is already in D(D), so even this extension
is unnecessary. A sign of a lower comparison does not reverse (7).

### 2. Exact witness and finite evaluation formulas

Write v=sum_(q=0)^63 z_q e_q^+, where z_q=b_q/2^44 and the ordered
integer coefficients are

```text
-17872052310, 75171134711, -779589332438, -216395112806,
1634677879771, -6240440545252, 474513380674, -7380987806467,
3534606652904, 1338289351872, 3902925481134, -926004774320,
214768754178, 4164416820465, -3416436601858, 1764560752362,
-3411484835569, 3896170618038, -345752118841, -171631769846,
-5392559402793, 72903323675, -397128640889, 489314766534,
-4285719135317, 2941429585406, -392370117284, 4645783360655,
5413934929566, -1629821844814, 1846643922840, -1934920464165,
2242788956108, 217698906301, 350470509376, -559968073737,
-293513938222, 23737686482, -80058863291, -61913706192,
-126262699439, 34393856121, 7303521917, 19035179137,
-16558277082, 10031954378, -1625473696, -3641436496,
-8229363291, -516079533, 165516102, -1348394095,
464019678, 320825487, 244238387, -1712625828,
674947070, -380212024, 703366489, -337751377,
1022435225, -654771221, 718104974, -848402577
```

Its exact squared norm is
309485009821346058612548645/309485009821345068724781056.
It is a proposal obtained by floating linear algebra, then fixed
exactly; the certificate does not read the floating screen.

For the following formulas let k_q=q*pi/a, n_0=a^(-1/2),
n_q=(2/a)^(1/2) for q>=1 and w_q=z_q n_q/sqrt(2). The centered
even full-interval function is f(x)=sum w_q cos(k_q x).

The diagonal contribution is sum z_q^2 h(k_q). Direct elementary
integration of (3), using sin(k_q a)=0 and cos(k_q a)=(-1)^q, gives

\[
 R_j:=\langle v,r_j^+\rangle
 =\sqrt{1-e^{-2ac_j}}
   \sum_{q=0}^{63}\frac{z_q n_q c_j(-1)^q}{c_j^2+k_q^2},
 \qquad
 \langle v,p_+\rangle=e^{a/2}\sqrt{1-e^{-a}}R_0.
 \tag{8}
\]

Only the first 128 squared R_j are added in (4). This specialization
evaluates the prescribed response family; it does not reprove the
Green identity. All of their projections are saved in the certificate.

Since e^L=9sqrt(3) lies strictly between 15 and 16, the active powers
are exactly 2,3,4,5,7,8,9,11,13, with base primes 2,3,2,5,7,2,3,11,13.
For a delay d=log(n), put b=a-d/2 and define
S_d(t)=sin(tb)/t for t!=0, S_d(0)=b. Product-to-sum followed by
integration about the midpoint -d/2 gives the correlation exactly:

\[
 C_f(d)=\sum_{r,s=0}^{63}w_rw_s\left[
 S_d(k_r-k_s)\cos((k_r+k_s)d/2)
 +S_d(k_r+k_s)\cos((k_r-k_s)d/2)\right].
 \tag{9}
\]

The arithmetic contribution is -2 sum Lambda(n) C_f(log n)/sqrt(n).
No prime power or reflected contribution is lost by this full-interval
evaluation. The symmetric matrix permits summing r<=s with factor two
off the diagonal. For r=s=0, (9) gives the interval-overlap length 2b,
which also checks its normalization.

For a cell center t_j and beta=sigma/2, each moment is obtained from

\[
 \int e^{\beta(x-t_j)}\cos(k_qx)\,dx
 =\frac{e^{\beta(x-t_j)}
             (\beta\cos(k_qx)+k_q\sin(k_qx))}{\beta^2+k_q^2}.
 \tag{10}
\]

Evaluate at x=t_j+-ell/2 and sum with coefficients w_q, then add
256 times the ten squared real moments. Formula (10) includes the
constant mode. The vector need not have exactly zero moments.

### 3. Rigorous scalar enclosures

The self-contained program is
`scripts/five-cell-penalty/certify-455.py`; its full output is
`scripts/five-cell-penalty/certificate-455.json`. Reproduction command:

```sh
python3 scripts/five-cell-penalty/certify-455.py
```

Its arithmetic precision is 70 decimal digits. Each basic interval
operation rounds its endpoints outwards. Monotone exp, ln and sqrt
are evaluated at the endpoints and widened by one adjacent representable
number under the cited correctly rounded contract. Products check all
endpoint pairs; squares include zero when the interval crosses zero.
All rational input coefficients are exact. Thus cancellation in the
small final value is included, rather than estimated from float digits.

For pi the program uses Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), with 100 alternating-series terms
per arctangent and remainder at most 1/(201 n^201). This identity
also follows by the tangent addition formula with the angle in (0,pi/2).
For sin/cos, subtract an integer multiple of the enclosed 2pi, verify
the reduced argument has modulus <4, and evaluate their polynomials
through degree 99 (the degree-99 cosine coefficient is zero). Taylor's
theorem bounds each remainder by 4^100/100!, which is added outwards.
The reduction integer is only a choice; the interval subtraction
encloses the corresponding exact reduced argument.

Euler's constant is enclosed using H_N-log N-1/(2N) with a symmetric
error 1/(12N^2), N=100000. The cited integer digamma value and real
remainder give this directly. Together with the cited rational value
it encloses h(0)=-gamma-pi/2-3log(2)-log(pi).

For the remaining diagonal values use Li (3.3), rewritten exactly as

\[
 h(k)-h(0)=\sum_{j\ge0}
      \frac{2k^2}{c_j(c_j^2+k^2)}.
 \tag{11}
\]

The summand, viewed as a function of real j>=0, is nonnegative and
decreasing: its numerator is constant and all positive denominator
factors increase. For N=8192 and c_N=2N+1/2, the entire omitted sum
is between

\[
 I_N(k)=\tfrac12\log(1+k^2/c_N^2)
 \quad\hbox{and}\quad
 I_N(k)+\frac{2k^2}{c_N(c_N^2+k^2)}.
 \tag{12}
\]

Indeed the first expression is its integral from N to infinity, and
the decreasing-function rectangle bounds put the sum between that
integral and that integral plus the first term. The k=0 case is zero.
Every finite summand, both tail endpoints and all weighted sums are
evaluated by the same outward arithmetic. This pays the whole digamma
tail; a special-function approximation from the float screen is unused.

The completed run encloses the scalar contributions as follows; these
displayed endpoints are outward coarsenings of the full certificate:

| Contribution | Enclosure |
| --- | --- |
| Diagonal | [1.56387725364006860, 1.56387725443363215] |
| All arithmetic delays | [-1.575649563114654958, -1.575649563114654957] |
| Responses j=0,...,127 | [0.0117722857975950052, 0.0117722857975950053] |
| Positive even pole | [8.8089e-19, 8.8090e-19] |
| All ten penalty terms | [2.5464e-16, 2.5465e-16] |
| Total, from full-precision endpoints | [-2.367700e-8, -2.288342e-8] |

The upper endpoint is strictly below -2e-8. The norm enclosure and
the exact fraction above give (5). This is an upper enclosure of an
actual value of the specified lower operator, not a negative lower
estimate for an unknown value. The certificate preserves every moment,
prime-power term, retained response and diagonal enclosure, as well as
the exact witness and all numerical truncation specifications.

### 4. Entire complement and the Schur obstruction

C744a's norm bound restricts unitarily to both parity spaces. Thus
take rho_+=C_nr(L) and rho_-=C_nr(L)+2(sinh(a)-a). The latter pays
the full negative odd pole; all retained responses and the penalty
are positive. Consequently the Q diagonal lower model is
t_q^epsilon=h(k_q^epsilon)-rho_epsilon. Equation (11) makes h(k)
increasing for k>=0, so t_q is increasing throughout the complement.

The program verifies the nilpotency indices q_n as 4 for n=2, 3 for
n=3, and 2 for the other seven powers, by strict interval comparisons
with L/log(n). It evaluates C_nr using these indices and the same
trigonometric enclosures. Using (11)–(12) also at k_4096^epsilon gives

\[
 t_{4096}^+\in[1.76988266347021,1.76991274823679],\qquad
 t_{4096}^-\in[0.82159196826206,0.82162205856331].
 \tag{13}
\]

Thus T>0 on the entire complement in both parities. The 64-mode vector
belongs to the fixed 4096-mode P_+ space and has negative M_+ value.
For every positive T, C_cross T^(-1) C_cross^* is positive semidefinite;
subtracting it cannot increase that value. The finite-prefix/remaining-
covariance payment in Li (5.4)–(5.5) only lowers it further. Hence the
required G>0 is impossible for (4), regardless of how accurately the
4096<=q<16384 prefix and q>=16384 tail are computed. This settles the
fixed test before matrix/covariance assembly, without dropping any
cross term from a claimed positive certificate.

The unpaid physical term relative to the actual form is precisely the
nonnegative response sum j>=128 in (7). No bound making that sum
negligible has been proved. The witness is a finite cosine vector,
not a compactly supported neutral smooth test; its recorded moments
are small but nonzero. Do not use (5) to infer a sign of E_L or of
E_L+256||C||^2. A future different certificate needs an independently
covered improvement that recovers the lost positive response energy
or another signed mechanism; repeating the same fixed test cannot help.

### Separate conceptual audit — 11 November 2026, step457

**Verdict.** Equations (5), (6) and the fixed lower-form/Schur obstruction
pass this audit. The prior SPECIALIZE assessment is
`drafts/literature/2026-11-11-five-cell-penalty-obstruction-audit-455.md`.
This verifies the existing certificate by REPRODUCTION; it supplies
neither a new quantitative theorem nor a complete-energy sign. The
previous witness, numerical source and certificate are preserved.

**Analytic input and domain.** The displayed paper45 v2, dated
9 November 2026, was checked at (2.1)-(2.5), Lemma 3.1 and its two
Green-kernel cases, and (4.6)-(5.5). Its arbitrary-a response identity
is the input to (7); no endpoint or numerical supplement is used.
L744 (6) has the same Fourier measure, digamma scalar, pole product
and arithmetic coefficient. For the translation f(x)=u(x+a),
F_f(z)=exp(iaz)F_u(z); the two factors at z=+-i/2 cancel in the pole
product even for complex u. Correlations and norm are unchanged.
Under the unitary parity map, F_f(i/2)=<v,p_epsilon>/sqrt(2) and
F_f(-i/2)=epsilon<v,p_epsilon>/sqrt(2), so the pole is exactly
epsilon|<v,p_epsilon>|^2, with no missing factor two.

The moment representers have squared norm 2sinh(ell/2). Reflection
permutes their ten outputs by (j,sigma)->(4-j,-sigma), proving the
parity split for the penalty on the original complex space. The
cell-centered weights differ from L743's defining local moments by
exp(-sigma ell/4), a nonzero factor. Thus U_5 lies in ker C; neither
projection nor approximate moment cancellation proves neutrality.

For this finite response family, every perturbation of D in (4) is
bounded and self-adjoint. The diagonal form is closed and bounded
below by the imported h formula. This proves the stated closed lower
form. On smooth compact parity tests the response identity gives (7).
The extension argument requires only the source's target-form closure:
after a common sufficiently large shift, lower-form norm is bounded
by target-form norm on the core, so a target-form Cauchy sequence
converges in the closed lower-form domain and preserves the inequality.
Adding the bounded moment form does not change that core argument.
Most importantly, the negative witness is a finite diagonal-basis
vector and hence belongs to D(D), independently of this extension.
No assertion about its membership in the zero-extension target-form
domain is needed or made in this audit.

**Witness and normalization of each summand.** All 64 integers were
compared between the canonical list, the source program and the saved
certificate. Exact rational arithmetic gives the displayed norm
fraction, strictly between the bounds in (5). The full-interval even
function has coefficients w_q=z_q n_q/sqrt(2); this factor is present
in both the arithmetic and physical-moment evaluations, whereas
responses and D are evaluated in the half-interval orthonormal basis.

For a response of parameter c, the integral of cos(k_q x) against
e^(cx)+e^(-cx) on (0,a) is
c(-1)^q(e^(ca)-e^(-ca))/(c^2+k_q^2). Multiplication by the response
normalization gives (8), including q=0. At c=1/2 its relation to
p_+ gives the pole factor in (8), which the program squares once.
For a prime delay d, substitution x=y-d/2 leaves -b<y<b. Integrating
the product-to-sum expression yields (9); S_d and cosine are even in
their frequency arguments, so the implemented |r-s| and symmetric
r<=s summation have the stated factor two. The constant-mode entry
is 2b. The derivative of (10)'s right-hand side is its integrand.
The six cell edges are x=edge*ell/2 with edge=-5,-3,-1,1,3,5;
k_q x=q*edge*pi/5 and the two exponential endpoint factors are
exp(+-sigma ell/4). These agree with every moment code path.

Since 15<exp(L)=9sqrt(3)<16, exactly the nine listed prime powers
occur. Their coefficients use log of the base prime, not log(n) for
a higher power. Both signs of the correlations are retained: the
n=8 and n=13 contributions, in particular, are positive, not discarded.
All ten stored moments were read; the (0,+1) interval lies strictly
below zero. This is evidence of non-neutrality, not merely a failure
to certify zero. The tiny penalty is still included in the total.

**Enclosure code audit.** All 268 source lines were inspected. Decimal
construction from integers or decimal strings is exact. Addition,
multiplication and reciprocal use the lower and upper directed
contexts; multiplication examines all four endpoint products and
the reciprocal rejects intervals containing zero. Negation uses
copy_negate, avoiding ambient-context rounding. Squaring uses lower
endpoint zero exactly when the interval contains zero. For monotone
exp, ln and sqrt, correctly rounded endpoint evaluations widened by
one adjacent representable number enclose the exact endpoint values.
The operation contracts are the Python Decimal and General Decimal
Arithmetic v1.70 references in the approved assessment. There is no
fractional-power call or floating special function in this chain.

Machin's formula uses 100 terms for each positive reciprocal tangent
argument, with first-omitted-term errors. Its branch is the angle in
(0,pi/2). The chosen reduction integer in sincos need not be certified
as nearest: subtracting that integer times the enclosed 2pi contains
an exact period-equivalent argument. The guard ensures modulus below
4. The iterates produce the sine polynomial through degree 99 and
the cosine polynomial through degree 98, also its degree-99 Taylor
polynomial. In both cases Taylor's degree-99 remainder is bounded
by 4^100/100!, and is added outward. The guard's use of ambient-rounded
Decimal abs does not permit false acceptance at modulus >=4:
round-to-nearest is monotone and fixes the exactly representable 4.
No enclosure endpoint is calculated by that ambient operation.

For Euler's constant, psi(N)=H_N-1/N-gamma together with the imported
real DLMF remainder gives exactly the center
H_N-log N-1/(2N), with symmetric radius 1/(12N^2). Thus the H_N index
and sign of the half term in gamma_interval are correct. Formula (11)
is the source's digamma difference, not an asymptotic approximation.
Writing c=2j+1/2, its integral from j=N to infinity is
(1/2)log(1+k^2/c_N^2); its nonnegative decreasing summand gives both
bounds in (12). The program adds this entire tail at N=8192 for each
of the 64 witness modes and both complement endpoints. Interval
evaluation retains uncertainty in k, pi, a and h(0) throughout.
Only the diagonal/digamma uncertainty is appreciable at the displayed
energy scale; cancellation is evaluated with full interval endpoints.

**Full replay and certificate integrity.** Reproduction command:

```sh
python3 scripts/five-cell-penalty/audit-457.py
```

The replay executes the unchanged enclosure source, changing only the
output destination. It writes the complete replay certificate and log
to `scripts/five-cell-penalty/replay-457/`; the original output is not
overwritten. All 18 top-level fields, including every one of the
64 diagonal enclosures, nine prime terms, 128 response projections,
ten moments and both complement records, reproduced byte for byte.
`scripts/five-cell-penalty/replay-457/audit.json` records source/output
hashes, runtime version, every check, full sign endpoints and failures.
Its 607 checks passed with no failures. This is a replay of the audited
algorithm, not a second implementation of its special functions.

Independent Fraction arithmetic checks the coefficient transcription,
exact norm, interval ordering, indices, every saved response square,
each penalty square, all contribution sums, complement subtractions
and the final strict bounds. In particular the complete upper endpoint
is -2.288342755385419656665469092612353040744713280306766521682565772764537e-8,
strictly below the -2e-8 acceptance threshold. The lower endpoint is
strictly above -2.368e-8. Reading status labels or previewed JSON was
not used to establish these inequalities.

**Whole complement and direction of implication.** For each delay,
the replay verifies (q_n-1)log(n)<L<q_n log(n), with indices 4,3,2
as stated. C744a (4) therefore supplies the same C_nr bound on the
original space and its two parity restrictions. Its imported
Haagerup-de la Harpe inequality applies to these norm-one nilpotent
delays without a dimension or neutral-subspace hypothesis. The odd
pole is paid in full by ||p_-||^2=2(sinh(a)-a). All retained response
and penalty forms are positive, so they may be discarded for the Q
floor. Each summand of (11) is increasing with k>=0. The positive
q=4096 floors therefore bound every remaining mode in the respective
parity, not just a finite sample. They give T>=tau I with tau>0, so
T^(-1) is bounded and positive.

For the exact witness x=v in P_+, <M_+x,x><0. Thus
< (M_+-C_cross T^(-1)C_cross^*)x,x>
=<M_+x,x>-||T^(-1/2)C_cross^*x||^2<0.
Any paid lower matrix G below this Schur complement has the same
negative-direction obstruction. A more accurate covariance evaluation
cannot change this ordering. The conclusion is failure of the fixed
lower comparison, irrespective of a covariance prefix computation.
The positive omitted responses j>=128, complete target-form
admissibility of this finite vector, exact-neutral signs and all-window
propagation remain unresolved. No inequality in (7) is reversed.

## Mathlib

Full matching Mathlib coverage of this fixed response-penalty obstruction
and its numerical certificate has not been checked. No absence claim or
formal verification is made. The named source identities are imported;
the moment/parity specialization, scalar evaluation and fixed-test
obstruction above are local and pass the separate audit recorded above
in the Proof section. The audit is REPRODUCTION, not a new sign theorem.
