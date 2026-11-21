# Corollary 466n: certified density and an explicit opposed-slice pair

## Hypotheses

Retain C466a/C466k/C466l's actual function
\(h(z)=\xi(1/2+\sqrt z)/c_0\), \(c_0=\xi(1/2)>0\),
\(p=\theta_1\), \(B=\log h\), \(x=B'(1)\), \(S=3x\),
and opposed slice \(K\). In particular \(p\) is the smooth probability
density supported on \([0,\infty)\), positive on \((0,\infty)\),
with Laplace transform \(h^{-1}\) on the open right half-plane.
Retain the imported density construction, strip, symmetry, paired
product, zero-counting and verified-low-zero qualifications of C466a.
Those external inputs have not been independently replayed. No RH,
PF-infinity, additional verified zeros or independence after conditioning
is assumed. Use C466m's explicit full-function estimates and all-r rate.

The finite calculation below uses the elementary outward interval
operations of the installed SymPy 0.7.4.1 bundled mpmath 0.17 library,
at 40 decimal digits. Gamma, zeta, differentiation and quadrature are
implemented with the explicit remainder bounds below, rather than
delegated to that library's special-function or quadrature routines.
Correctness of its elementary interval implementation is part of the
computational trust base; neither this calculation nor its aggregate
replay is a formal verification of that implementation.

## Conclusion

Under these inputs, the explicit choices
\[
 m=\frac1{1000},\qquad R=\exp(\exp(256))                         \tag{1}
\]
satisfy
\[
 p(S)>m,\qquad R\ge\frac\pi{2S},\qquad
 \big|K(r)|h(1+ir)|^2-2\pi p(S)\big|\le\pi m\quad(|r|\ge R).
                                                                    \tag{2}
\]
The computed enclosure, rounded outwards here, is
\[
 0.00994617<p(S)<0.01016314.                                    \tag{3}
\]
Thus the effective-pair target is completed locally and passed the
step939 critical audit of C466m and this numerical proof, under the
inherited and computational qualifications. This is not a practical compact sign certificate:
the huge intervening interval, full two-frequency marginal, all orders
and all x, and density-to-Xi transfer remain unpaid. There is no RH
candidate or claim of originality beyond the bounded review935 search.

## Proof

### Exact inversion and a finite quadrature error

C466k(7), conjugate symmetry and absolute integrability give
\[
 p(S)=\frac{e^S}{\pi}\int_0^\infty f(t)\,dt,
 \qquad f(t)=\operatorname{Re}\frac{e^{iSt}}{h(1+it)}.          \tag{4}
\]
In all point evaluations, S and c0 are intervals enclosing their exact
values; they are not replaced by numerical midpoint parameters.

Put \(L(s)=1/h(s)=\int e^{-su}p(u)du\) for real \(s>0\),
and define the five-value difference
\[
 D=L(1/2)-4L(3/4)+6L(1)-4L(5/4)+L(3/2).
\]
Its exact integral is
\[
 D=\int_0^\infty e^{-u}\big(2\cosh(u/4)-2\big)^2p(u)du
       \ge\frac1{256}\int_0^\infty u^4e^{-u}p(u)du.          \tag{5}
\]
The inequality follows from \(2\cosh v-2\ge v^2\). Every integral
is finite, including the positive exponential in the difference,
because its net tilt is at least 1/2. Differentiating the transform
in (4) four times is justified by boundedness of \(u^j e^{-u}\),
\(0\le j\le4\), against the probability density. Hence
\[
 \sup_{t\in\mathbb R}|f^{(4)}(t)|
 \le\int e^{-u}|S-u|^4p(u)du
 \le 8\{S^4L(1)+256D\}=:Q_4.                                \tag{6}
\]
Here \((a+b)^4\le8(a^4+b^4)\) for nonnegative a,b pays the
absolute value; no cancellation or derivative sign is assumed.

Import the standard **composite Simpson error theorem**,
[NIST DLMF 3.5(ii), equations 3.5.6-3.5.8](https://dlmf.nist.gov/3.5#ii): for a real
\(C^4\) function on \([0,T]\), an even number n of equal subintervals
of width \(\delta=T/n\) has error at most
\(T\delta^4\sup|f^{(4)}|/180\). Its hypotheses are satisfied by (6).
This elementary finite quadrature choice avoids the need to establish
complex ellipses for a Petras integrator. The bound applies to the
exact function throughout each subinterval, not just to its samples.
Take
\[
 T=4096,\quad n=8192,\quad\delta=1/2,
 \quad A=\frac\delta3\left[f(0)+f(T)+
       4\sum_{j\text{ odd}}f(j\delta)+
       2\sum_{\substack{j\text{ even}\\0<j<n}}f(j\delta)\right].
                                                                    \tag{7}
\]
The enclosed values below give
\[
 Q_4<0.000182705<\frac{183}{10^6},\qquad
 E_{\rm quad}=\frac{T\delta^4Q_4}{180}<\frac{260}{10^6}.       \tag{8}
\]

### Explicit omitted tail on the original line

C466m(3),(6),(8) give, for \(t\ge16\),
\[
 d(t):=\log|h(1+it)|-\log h(1)
 \ge\kappa\sqrt t\log t+\lambda\sqrt t+\frac78\log t
                         -2-\frac{4\log t}{\sqrt t},
\]
where \(\kappa=1/(4\sqrt2)\) and
\(\lambda=-(\log(2\pi)+1+\pi/4)/(2\sqrt2)\), and \(h(1)\ge1\).
The two interval-checked scalar comparisons at T are
\[
 \kappa\log4096+\lambda>3/16,\qquad
                    4\log4096/64<1.                         \tag{9}
\]
The first left side increases with t; \(\log t/\sqrt t\)
decreases for \(t\ge4096>e^2\). Consequently
\[
 |h(1+it)|^{-1}\le e^3t^{-7/8}e^{-3\sqrt t/16}\quad(t\ge T).
\]
With \(a=3/16\), substitution \(y=\sqrt t\) therefore gives
\[
 \left|\int_T^\infty f(t)dt\right|
 \le 2e^3\int_{\sqrt T}^\infty y^{-3/4}e^{-ay}dy
 \le\frac{2e^3}{a}T^{-3/8}e^{-a\sqrt T}
 =:E_{\rm tail}<\frac{59}{10^6}.                            \tag{10}
\]
This is an absolute infinite-tail estimate, not an extrapolation from
evaluated frequencies. It uses the full completion estimate at every
t above T, rather than C466m's much later coarse growth threshold.

### Enclosures of the full completion, S and every node

Here are the explicit algorithms and imported remainder statements,
so that the numerical result can be reviewed without inferring an
error bound from a requested precision. In the completion formula
\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),          \tag{11}
\]
the arguments used are s=1/2 for c0 and
\(s=1/2+\sqrt z\) with \(z\) a positive real number or
\(z=1+it\), \(0\le t\le4096\). There is no singular individual
completion factor at these arguments. Principal square roots have
positive real part; log-Gamma is the analytic branch real on the
positive axis.

For Gamma, put \(w=s/2\), \(v=w+32\), and use
\[
 \log\Gamma(w)=(v-\tfrac12)\log v-v+\tfrac12\log(2\pi)
 +\sum_{k=1}^{11}\frac{B_{2k}}{2k(2k-1)v^{2k-1}}
 -\sum_{j=0}^{31}\log(w+j)+R_{12}(v),
\]
\[
 |R_{12}(v)|\le\frac{|B_{24}|\,2^{12}}{24\cdot23\,|v|^{23}}.
                                                                    \tag{12}
\]
This imports [DLMF 5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11),
the log-Gamma remainder already inspected in review935. Since
\(\operatorname{Re}v>0\), its secant factor is at most \(2^{12}\).
The shift identity uses logarithms in the right half-plane and the
positive-real normalization, so branch increments are not lost.
The modulus error is added to both rectangular components before
exponentiating; this deliberately overencloses a disk error.

For zeta use endpoint W=64 and M=16:
\[
 \zeta(s)=\sum_{j=1}^{63}j^{-s}+\frac{64^{1-s}}{s-1}
 +\frac12 64^{-s}
 +\sum_{k=1}^{16}\frac{B_{2k}}{(2k)!}(s)_{2k-1}64^{1-s-2k}
 +R(s),
\]
\[
 |R(s)|\le\frac{4|(s)_{32}|}{(2\pi)^{32}}
              \frac{64^{1-\sigma-32}}{\sigma+31},
 \qquad \sigma=\operatorname{Re}s,\quad\sigma+31>0.          \tag{13}
\]
Import Fredrik Johansson, *Rigorous high-precision computation of the
Hurwitz zeta function and its derivatives*,
[arXiv:1309.2877v1, Section 2, Theorem 1, (5)–(14), pp.2–4](https://arxiv.org/pdf/1309.2877v1),
as inspected in review935. In the Hurwitz convention a=1, the summation
parameter is N=63, so a+N=64>1; M=16 and \(\operatorname{Re}s+32>1\)
hold in all evaluations and in the derivative disk below. Formula (13)
is its constant-term remainder case: the periodic Bernoulli integral
has modulus at most \(2(32)!\zeta(32)/(2\pi)^{32}\), and
\(\zeta(32)<2\) gives the stated factor 4. This is an applicability
and constant specialization, not a reproof of Euler–Maclaurin.

The exact derivative needed for S is
\[
 x=\frac43-\frac{\log\pi}{4}+\frac{\psi(3/4)}4
                                  +\frac{\zeta'(3/2)}{2\zeta(3/2)}.
                                                                    \tag{14}
\]
It follows by logarithmically differentiating (11) at z=1.
For \(\zeta'(3/2)\), differentiate the finite expression in (13).
Its remainder derivative is enclosed by Cauchy's estimate on
\(|s-3/2|\le1/4\). There \(\sigma\ge5/4\) and
\(|(s)_{32}|\le\prod_{j=0}^{31}(j+7/4)\), so four times
the right side of (13) with those replacements bounds \(|R'(3/2)|\).
For \(\psi(3/4)\), differentiate the finite expression in (12)
and use a radius-1/4 Cauchy disk about \(v=131/4\). Its minimum
modulus is 65/2, its real part stays positive, and four times (12)'s
remainder bound with that minimum modulus bounds the derivative error.
No value-only asymptotic remainder is differentiated without this step.

The script evaluates elementary exp/log/sqrt/sin/cos/atan2 and arithmetic
with outward intervals. Complex logarithms and exponentials are built
from those real operations. Bernoulli numbers are generated as exact
rational numbers. Every completion denominator is enclosed away from
zero before division. S and c0 propagate through all 8,193 integrand
values. Smoothness between nodes follows analytically from (4)–(6),
so the proof requires no untested complex-neighborhood assertion for
the numerical intervals. The resulting enclosures include
\[
\begin{split}
 0.49712077818831&<c_0<0.49712077818832,\\
 0.06920389209069&<S<0.06920389209070,\\
 0.02947556997059&<A<0.02947556997060,\\
 E_{\rm quad}+E_{\rm tail}&<0.000319.
\end{split}                                                     \tag{15}
\]
Combining the exact stored endpoints in (4),(7)–(10) gives (3).
For the weaker required bound, one does not even need the numerical
prefactor: S>0 and \(\pi<4\) give \(e^S/\pi>1/4\), while
the certified \(A-319/10^6>1/250>0\) gives \(p(S)>1/1000\).

### The all-r conclusion and evidence limits

C466m(1) gives the normalized error at most \(e^S|r|^{-1/16}\)
for \(|r|\ge R\). The application check in this attempt followed
its full completion remainder, compact characteristic-function bound,
small/comparable/far frequency ranges including t=±r, and integrated
complex-ratio error. No unproved differentiated remainder, phase
replacement or sampled-r inference was introduced. This check is not
the separately scheduled independent audit of C466m.

From (15), \(1/100<S<1\). Thus \(\pi/(2S)<200\), and, using
\(e<3<\pi\),
\[
 \left(\frac{e^S}{\pi m}\right)^{16}<1000^{16}<R.
\]
Indeed \(16\log1000<160<e^{256}=\log R\); also R>200.
Therefore C466m's error is at most \(\pi m\) for every \(|r|\ge R\),
proving (1)–(2). Evenness covers negative r. This signs only the
eventual opposed slice; it does not sign the intervening frequencies
or any complete determinant.

Reproduce the interval calculation with
`/Users/vermeer/Applications/anaconda/bin/python scripts/reciprocal-tail/density_937.py`
(Python 2.7.6, bundled mpmath 0.17). The full certificate is
`scripts/reciprocal-tail/density-937.json`: exact dyadic endpoints
for all 8,193 nodes, constants, actual/required inequalities, script
hash, and empty failure lists. The computation completed in attempt937;
a failed optional FLINT installation supplied no mathematical evidence.
There is no dependency on FLINT or network access in the successful run.

Run `python3 scripts/reciprocal-tail/check_density_937.py` for the exact
rational aggregate replay. It processes every saved node, confirms
containment of the full weighted sum, checks the explicit error budgets
and the positive density margin, and saves
`scripts/reciprocal-tail/density-937-check.json`. All 14 checks passed.
This replay does not independently recompute the special functions,
certify the elementary library or audit the all-r proof. The numerical
enclosure and analytic argument were the subjects of the separate
step939 critical review below; (2) remains a qualified partial result.

### Critical audit, 14 November 2026, step939

The pair (1)-(2) passes under the stated imported and computational
inputs. The mathematical argument, actual special-function code,
every node, and the complete error propagation were reviewed. This
is validation of the existing local partial result, not a stronger
sign theorem, independent proof of the external inputs, or claim of
discovery beyond the checked sources. Reuse nomination937/approval938
and review935; no source version or density hypothesis was changed.

First, (4) has the correct normalization e^S/pi: conjugate symmetry
turns C466k's full-line integral into twice its real half-line integral.
For (5), expanding
\((e^{u/4}+e^{-u/4}-2)^2\) gives the five coefficients
\(1,-4,6,-4,1\) at the stated tilts. Its lower bound is
\(u^4/256\). The probability-law domination makes f a real C4
function on the whole line; it also justifies differentiating under
the integral four times. Thus the cited Simpson theorem applies
with even n=8192, step=1/2, and error coefficient
\(4096(1/2)^4/180=64/45\). These are interval error bounds
between nodes, not numerical derivative samples.

For (9)-(10), the coefficient \(\kappa\log t+\lambda\)
increases and \(4\log t/\sqrt t\) decreases for t>=4096.
C466m's constant lower bound C>-2 and its value remainder therefore
give the factor e^3. Substitution y=sqrt(t) changes t^(-7/8)dt
to 2y^(-3/4)dy; bounding the power by its value at 64 gives exactly
the recorded absolute omitted tail. This holds for all t>=4096.

The completion code was checked term by term. At every node the
principal root lies in the right half-plane, and all w+j used for
Gamma logarithms have positive real part. The 32 shifts and eleven
Bernoulli terms match (12); for n=12, sec^(24)(arg(v)/2)<=2^12.
Adding the disk-error radius to both rectangular components before
the complex exponential is an overenclosure. For zeta, summation
over 1 through 63 and endpoint 64 is precisely a=1,N=63,M=16.
Its value remainder uses the full product of 32 rising factors and
the lower real part in the decreasing integral bound. These checks
also cover s=1/2 for c0, where the absolutely convergent Dirichlet
series itself would not suffice. Taking the real component for c0
is legitimate because the exact completed value is real.

The derivative recurrence differentiates each rising factor once;
the finite endpoint and power derivatives have the signs in (14).
For the zeta remainder disk, the lower real part is 5/4, the upper
factor is j+7/4, the exponent at 64 is -129/4 and the denominator
is 129/4. Multiplication by four is Cauchy's radius-1/4 estimate.
For the log-Gamma derivative disk, center 131/4 and minimum modulus
65/2 give the other stated derivative bound. There is no unpaid
differentiation of an asymptotic error. At s=3/2 the zeta denominator
is nonzero (indeed zeta(3/2)>1); the interval division stays finite.
The code checks nonzero completion denominators for all five Laplace
values and all 8193 nodes. S and c0 are enclosing intervals throughout.

Run
`/Users/vermeer/Applications/anaconda/bin/python scripts/reciprocal-tail/audit_pair_939.py`.
The audit reran the entire inspected generator, changing only its output
filename and preserving its original source hash. The regenerated full
certificate is `scripts/reciprocal-tail/density-939-recomputed.json`;
the original `density-937.json` was not overwritten. All 8193 nodes
were recomputed, and all 8229 endpoint-bearing records in the entire
certificate matched exactly. Thus this check includes special-function
evaluations at every node, as implemented with the explicit remainder
bounds, rather than only summing old node intervals. It still uses the
same trusted elementary interval library, not an independent library
or formal verification of its operations.

`scripts/reciprocal-tail/pair-audit-939.json` records 66 passing exact
checks, all actual/required bounds, full provenance, and no failures.
These include an independent rational Bernoulli recurrence through
B32; every stored prerequisite inequality; the complete positively
weighted node sum; S=3x; the five-Laplace difference, mu4 and Q4;
the Simpson coefficient; coverage of both error budgets; and every
rounded numerical assertion in (3),(8),(15). In particular the exact
sum interval lies within (0.02947556997059,0.02947556997060), while
the total integral error is below 0.000319. Its positive lower endpoint
and e^S/pi>1/4 prove p(S)>1/1000 without relying on an approximate
transcendental prefactor. The narrower displayed density enclosure also
reproduces with the full interval prefactor and outward rounding.

Finally, C466m's step939 audit supplies the uniform all-r error bound.
The certified 1/100<S<1, e<3<pi and m=1/1000 imply
pi/(2S)<200 and (e^S/(pi*m))^16<1000^16<R. Hence the stated R
meets every obligation in (2). No numerical representation of the
double exponential, sampled-r test, or strengthened density theorem
is used. The false audit flag in the original historical certificate
records its status in step937; the later audit is this section and
the separate 939 certificate, with the original evidence preserved.

The direct mathematical inputs in the existing DAG row are unchanged.
The compact middle, full marginal, all orders/all x and Xi transfer
remain open; the external density/counting/low-zero imports and the
elementary interval trust base remain explicit qualifications.

## Mathlib

Full matching coverage is unchecked. Standard Fourier inversion,
Laplace differentiation, Cauchy estimates, Gamma/zeta identities and
quadrature results are supporting inputs, not a formalization of this
interval calculation or the all-r bound. No declaration-name or absence
claim is made; unknown availability is not evidence of absence.
