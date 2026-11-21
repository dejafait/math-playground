# Corollary C048d: the omitted horizontal Gaussian pair

## Hypotheses

Let p be complex, r=|p|, L=log r>=12 and Re p>=-r/(4L).
As in C048c, let w=W_0(2p/pi) be the principal Lambert branch and put

\[
 A_0=4p(1+w)/w^2,\qquad d=1/(3L),\qquad
 G_{\rm loc}=\int_{-d}^d e^{-A_0s^2}\,ds.
\]

The variable s is real. All square roots below are principal.
Use the audited curvature and normalization conclusions of C048c,
in particular its (9)-(10). The quantitative source claim is a
conclusion to verify, not an additional hypothesis.

## Conclusion

Both omitted tails converge absolutely, and

\[
 T_{\rm ext}(p):=
 \frac{\left|\int_{(-\infty,-d)\cup(d,\infty)}e^{-A_0s^2}\,ds\right|}
      {|\sqrt{\pi/A_0}|}
 =\frac{|\sqrt{\pi/A_0}-G_{\rm loc}|}{|\sqrt{\pi/A_0}|}
 \le A_g\frac{L^{9/2}}r,
 \tag{1}
\]

where

\[
 y_0=e^{12}/12^4,\qquad
 A_g=\frac{\sqrt{6/\pi}}{13/10}\sqrt{y_0}\,
               e^{-(13/30)y_0}<0.099276.
 \tag{2}
\]

Thus the allowance holds on the full closed sector, including both
imaginary signs, positive real p, permitted negative real parts,
r=e^12 and unbounded L. This is REPRODUCTION of the isolated Gaussian
allowance in K. Kawano, *Logarithmic Inequalities of Arbitrary Order for
the Riemann Xi Coefficients*, Preprints.org202611.0383v1, posted
4November2026, DOI10.20944/preprints202611.0383.v1,
[Section5.2(28), AppendixB's B_g and AppendixC's A_g](https://www.preprints.org/manuscript/202611.0383/v1).
Assessment1629 and source-notes1630 identify that exact scope.
No assertion of new mathematics beyond the source claim is made.
The source uses no symbol T_ext; (1) makes its omitted-pair allocation
precise. AppendixB's different width is not used.

## Proof

### Convergence, completion and the two-tail majorant

C048c(9)-(10) gives, throughout the stated domain,

\[
 b:=\Re A_0>\frac{39r}{10L^2}>0,\qquad
 |A_0|<\frac{6r}{L}.                                  \tag{3}
\]

In particular A_0 is nonzero in the open right half-plane. The bound
|e^(-A_0s^2)|=e^(-bs^2) proves absolute convergence on the real line.
[NIST DLMF7.7.6](https://dlmf.nist.gov/7.7.E6), with its a=A_0,
b=c=x=0, gives the integral on [0,infinity) as
(1/2)sqrt(pi/A_0), since erfc(0)=1. Here the source's coefficient b
is zero; it is distinct from the real curvature b in (3).
The theorem's condition Re a>0 is (3), and its principal Gaussian
branch agrees with C048c. Evenness doubles that integral, and absolute
convergence permits splitting off [-d,d]. This proves the equality
in (1), retaining the complex phase. Endpoint choices do not change
any of these integrals.

The triangle inequality and evenness of the real majorant give

\[
 \left|\int_{|s|>d}e^{-A_0s^2}\,ds\right|
 \le2\int_d^\infty e^{-bs^2}\,ds
 \le\frac2d\int_d^\infty s e^{-bs^2}\,ds
 =\frac{e^{-bd^2}}{bd}.                               \tag{4}
\]

The second inequality uses s/d>=1 for s>=d, and the last integral
uses the antiderivative -e^(-bs^2)/(2b), whose infinite endpoint is
zero. Thus (4) already pays both tails. It does not replace the
complex integral by an equal positive integral. This elementary
Gaussian tail estimate suffices; no stronger Mills inequality or
large-argument approximation is needed.

The absolute normalization is exactly
|sqrt(pi/A_0)|=sqrt(pi/|A_0|), including nonreal A_0. For positive b,
e^(-bd^2) decreases and 1/b decreases as b increases. Substitution
of the lower b and upper |A_0| bounds in (3), into (4), therefore
has the upper-bound direction:

\[
 \begin{split}
 T_{\rm ext}
 &\le\sqrt{|A_0|/\pi}\frac{e^{-bd^2}}{bd}\\
 &\le\frac{10}{13}\sqrt{\frac6\pi}\,
       \frac{L^{5/2}}{\sqrt r}
       \exp\left(-\frac{13r}{30L^4}\right).
 \end{split}                                         \tag{5}
\]

Indeed (39r/(10L^2))d=13r/(10L^3) and
(39r/(10L^2))d^2=13r/(30L^4). No modulus of the complex curvature
is substituted for its real part in the exponent.

### Uniform radial comparison

Put y(L)=e^L/L^4=r/L^4 and c=13/30. Dividing the last side of (5)
by L^(9/2)/r gives exactly

\[
 \frac{10}{13}\sqrt{6/\pi}\,\sqrt{y(L)}e^{-cy(L)}.
                                                               \tag{6}
\]

For L>=12, y'(L)=y(L)(1-4/L)>0, so y(L)>=y_0.
The exact endpoint bounds below give y_0>15/13. Direct differentiation
shows

\[
 \frac{d}{dy}(\sqrt y e^{-cy})
 =\frac{e^{-cy}}{2\sqrt y}(1-2cy)<0
 \quad\hbox{for } y>15/13.                             \tag{7}
\]

Consequently (6) is at most its value at L=12, which is A_g in (2).
This proves the uniform comparison on the whole unbounded ray, rather
than on a finite grid. All sector dependence in this argument was paid
by the audited (3); no extra angular restriction or division by Im p
is used. In particular the real case and both angular boundaries remain
included.

### Exact endpoint certificate

The fixed scalar calculation is reproduced by
`python3 scripts/mellin-horizontal-local/extension_constants_1631.py`;
its complete rational evidence is
`scripts/mellin-horizontal-local/extension_constants_1631.json`.
It uses no floating point decisions. The following analytic series
bounds explain every enclosure, so the certificate is only finite
arithmetic supporting the uniform proof.

For x>0 and an integer N with x<N+2, let S_N=sum_(k=0)^N x^k/k!.
Positivity and the ratio of successive omitted terms give

\[
 S_N<e^x< S_N+
 \frac{x^{N+1}}{(N+1)!}\frac1{1-x/(N+2)}.              \tag{8}
\]

Indeed every ratio after the first omitted term is at most x/(N+2)<1;
the geometric bound is strict since later ratios are smaller.
Apply (8) at x=12,N=120. Exact rational comparison yields

\[
 162754.7914190039<e^{12}<162754.7914190040.             \tag{9}
\]

For pi the script uses the standard Machin identity
pi=16 arctan(1/5)-4 arctan(1/239). One elementary verification is
tan(2 arctan(1/5))=5/12 and tan(4 arctan(1/5))=120/119;
the subtraction formula then gives
tan(4 arctan(1/5)-arctan(1/239))=1. The angle is in (0,pi/2):
arctan x<x and arctan x>=x/(1+x^2) for x>0 give the lower
endpoint positive and the upper endpoint <4/5<pi/2. Hence the angle
is pi/4, proving the stated identity without a branch ambiguity.

The alternating arctangent series at 1/5 through k=23 and at 1/239
through k=7 gives lower bounds; adding the first omitted positive
term gives upper bounds. This series and remainder follow by integrating
the finite geometric expansion of 1/(1+t^2) from 0 to x<1.
Machin's identity therefore gives, by exact rational comparison,

\[
 3.141592653589793<\pi<3.141592653589794.               \tag{10}
\]

Let y_- and y_+ be the rational endpoints in (9) divided by 12^4,
and pi_-,pi_+ those in (10). The certificate checks y_->15/13,
as required in (7). It encloses sqrt(6y_-/pi_+) from below and
sqrt(6y_+/pi_-) from above between adjacent multiples of 10^-18,
checking the corresponding squared rational endpoints exactly.
Denote the resulting outer root bounds by R_- and R_+.
Apply (8) with N=80 at the two positive rational arguments cy_-
and cy_+. Let E_- be the lower bound at cy_- and E_+ the upper
bound at cy_+. Both arguments satisfy x<82. Positivity and monotonicity
of exp and sqrt now give

\[
 \frac{10R_-}{13E_+}<A_g<\frac{10R_+}{13E_-}.
                                                               \tag{11}
\]

No independence of the true y_0 in the numerator and denominator is
assumed: separate outward replacements suffice. Exact rational
evaluation of (11) gives the convenient outer enclosure

\[
 0.099275864521823<A_g<0.099275864521825<0.099276,
                                                               \tag{12}
\]

with certified slack greater than 10^-7 from the required rational
threshold 0.099276=24819/250000. All nine comparison checks pass.
The script stores the complete sums, tail-ratio bounds, root squares
and unrounded enclosure as well as the short enclosure (12).
Decimal printing is merely a display of these rational comparisons.

This proves (1)-(2), reproducing the source's Gaussian component.
It neither supplies the full theta-Mellin remainder nor pays other
theta modes, horizontal tails, zero counts, inversion, or a sufficient
all-degree actual-Xi sign implication. No RH candidate follows.
Independent audit1632 below validates this reproduction.

### Independent audit1632 (19 November2026)

The approved target is exactly (1), with the hypotheses above, and the
SPECIALIZE assessment1629 is unchanged. The audit found no mathematical
error or missing restriction in this isolated allowance. This is local
verification of source-claimed mathematics, not a new result beyond it.

Only the audited C048c curvature and principal normalization are used as
local inputs. Its (9)-(10) hold on both imaginary signs and the closed
sector boundaries; no bound involving division by Im p enters this proof.
In particular Re A_0>0 includes positive real p and the permitted
negative real parts. DLMF7.7.6 applies at a=A_0, b=c=x=0. Since
arg A_0 lies in (-pi/2,pi/2), sqrt(pi/A_0)=sqrt(pi)/sqrt(A_0)
on the principal branches. Its modulus is exactly sqrt(pi/|A_0|).
Absolute convergence allows the two half-line integrals to be joined
and [-d,d] to be subtracted. Thus the completion equality is valid
with complex phase, not only after a modulus comparison.

For the majorant, the factor 2 in (4) pays the pair of tails and
cancels the 1/2 in the antiderivative. Both exp(-bd^2) and 1/b
decrease in positive real b. Increasing |A_0| increases only the
normalizing factor sqrt(|A_0|/pi). Substituting (3) therefore gives
(5) in the upper-bound direction, with coefficient
(10/13)sqrt(6/pi), power L^(5/2)/sqrt(r), and exponent
-13r/(30L^4). Dividing by L^(9/2)/r leaves exactly
(10/13)sqrt(6/pi)sqrt(y)exp(-13y/30). The derivative of y(L)
is positive for L>=12; the derivative of this last scalar profile
is negative for y>15/13. The certified lower endpoint exceeds
15/13. This checks the entire unbounded radial range without a grid.

For (8), successive omitted-term ratios are bounded above by
x/(N+2)<1; all three positive Taylor series used by the certificate
meet that hypothesis (x=12,N=120, and the two endpoint arguments
x=(13/30)y_-,(13/30)y_+, N=80). The lower sums and upper geometric
remainders have the claimed strict directions. Both alternating
arctangent sums end in a negative term, so adding the next positive
term bounds each from above. The minus sign in Machin's formula
requires the upper arctangent bound for the lower pi bound, exactly
as implemented. Its tangent subtraction is exactly 1 and its angle
is positive. Its upper angle is <4/5<1<pi/2, using the elementary
bound pi>2 (also obtained from pi/4=int_0^1 dt/(1+t^2)>1/2).
There is no circular use of the tight pi enclosure to select the angle.

The independent replay uses direct powers/factorials for every Taylor
sum and paired positive-minus-negative terms for each arctangent sum,
instead of importing the production script. It reads every complete
mathematical field of certificate1631 and compares full rational
values, including series sums, omitted terms, ratios, intervals,
root squares, denominator bounds, unrounded A_g and all nine scalar
comparisons. Its separate root checks use the actual rational squares,
not saved Boolean assertions. Positivity of both exponential
denominators and outward replacements give (11), even though numerator
and denominator share y_0. The exact enclosure (12), the strict
threshold and slack>10^-7 all pass. No displayed decimal or bounded
JSON preview is used as verification.

Reproduce this audit with
`python3 scripts/mellin-horizontal-local/audit_extension_constants_1632.py`.
The complete audit evidence is
`scripts/mellin-horizontal-local/audit_extension_constants_1632.json`:
27 checks, zero failures. The original proof and certificate1631 are
preserved. No new local dependency or stronger conclusion is introduced;
the full-theta remainder and all sign-transfer obligations remain open.

## Mathlib

Full matching coverage of this effective moving-sector inequality has
not been checked; unknown is not evidence of absence. The named
standard input used here is DLMF7.7.6 with all hypotheses and branch
specialized above. The needed weaker real tail estimate, monotonicity,
and finite endpoint comparisons are proved explicitly. The only local
mathematical input is C048c's audited curvature and branch normalization;
no formal verification is claimed.
