# Lemma 876: the fixed primitive-theta Hankel square misses the second coefficient

## Hypotheses

Use exactly the positive kernel K of L019, without a change of variable,
measure, weight, shift, rank correction or exponential prefactor:

\[
K(u)=\sum_{n\ge1}(8\pi^2n^4e^{9u/2}-12\pi n^2e^{5u/2})
                    e^{-\pi n^2e^{2u}},\qquad u\ge0.
\]

On the complex Hilbert space \(\mathcal H=L^2((0,\infty),dx)\), let
\(Hf(x)=\int_0^\infty K(x+y)f(y)\,dy\). Let \(A=H^*H\),
\(T=\operatorname{Tr}A\), \(T_2=\operatorname{Tr}(A^2)\), and use
L021/L025's actual-Xi moments and coefficients

\[
M_j=\int_0^\infty u^jK(u)\,du\quad(j=0,2,4),\qquad
S_1=\frac{M_2}{2M_0},\quad S_2=\frac{3M_2^2-M_0M_4}{12M_0^2}.
\]

Define \(c=S_1/T\) after establishing \(T>0\) below.

## Conclusion

H is a bounded selfadjoint Hilbert-Schmidt operator; A is positive
trace class, and \(T,c>0\). For this fixed operator and normalization,

\[
 \boxed{\quad 0.00021317<c^2T_2-S_2<0.00050451.\quad}                 \tag{1}
\]

The bounds are rational decimal bounds, not floating-point estimates.
Consequently \(\det(I-cz^2A)\ne\Xi(z)/M_0\): the \(z^2\)
coefficients agree and the \(z^4\) coefficients disagree. This rejects
only this ansatz. It supplies no disproof of RH, no sign for arbitrary
mixed forms, and no obstruction to other independently specified operators.

## Proof

### Imported operator and determinant facts

Use the standard Hilbert-Schmidt kernel theorem and its half-line
Hankel specialization in Thomas Bothner, *A Riemann-Hilbert approach to
Fredholm determinants of Hankel composition operators: scalar-valued
kernels*, [arXiv:2205.15007v2](https://arxiv.org/pdf/2205.15007v2#page=5),
Section 2.1, (10)-(13), printed p5. The weighted condition is
\(\int_0^\infty u|K(u)|^2du<\infty\), not merely an unweighted
integrability condition. Import the Hilbert-Schmidt product/trace-class
facts and the spectral determinant/Plemelj formula from Folkmar
Bornemann, *On the numerical evaluation of Fredholm determinants*,
[arXiv:0804.2543v2](https://arxiv.org/pdf/0804.2543v2#page=7),
Section 2, printed pp6-8, and [Section 3](https://arxiv.org/pdf/0804.2543v2#page=10),
(3.1)-(3.3), printed p10. Only these general operator facts are imported;
no Riemann-Hilbert asymptotics, resolvent formula or numerical quadrature
error theorem is used. The calculations below are necessary because
these sources do not evaluate this actual-theta specialization.

L019 gives continuous real K, positive everywhere and rapidly decaying.
Tonelli and \(u=x+y\) give

\[
 \|H\|_{\mathrm{HS}}^2
 =\int_0^\infty\!\int_0^\infty K(x+y)^2\,dx\,dy
 =\int_0^\infty uK(u)^2du=T\in(0,\infty).                            \tag{2}
\]

Thus the kernel theorem applies. The real symmetric kernel identifies
the Hilbert adjoint with H itself: for f,g in \(\mathcal H\), absolute
integrability of \(K(x+y)f(y)\overline{g(x)}\) follows by
Cauchy-Schwarz in \(L^2(dx\,dy)\), since
\(\|f(y)g(x)\|_2=\|f\|_2\|g\|_2\). Fubini therefore proves the
adjoint identity for all f,g. Positivity and trace class of \(A=H^*H\)
follow from the imported product theorem, and (2) is its trace identity.
This does not use an unjustified diagonal formula on an unbounded domain.
Strict positivity in (2) and L021's \(M_2,M_0>0\) establish \(c>0\).

### A fixed trial-function bound for the full trace

Fix \(b=3/10\), \(f=b^{-1/2}\mathbf1_{[0,b]}\), so \(\|f\|_2=1\).
Set

\[
 J=\langle f,Hf\rangle
   =b^{-1}\int_0^{2b}w_b(u)K(u)du>0,\qquad
 w_b(u)=\begin{cases}u&0\le u\le b,\\2b-u&b\le u\le2b.\end{cases}    \tag{3}
\]

The equality follows by the length of a line section of \([0,b]^2\),
or positive Tonelli. This trial function bounds the prescribed operator;
it is not a weight inserted into H or A. For any positive trace-class A,
\(\langle f,Af\rangle\le\|A\|_{\mathrm{HS}}=\sqrt{T_2}\).
Also \(\langle f,Af\rangle=\|Hf\|^2\ge|\langle f,Hf\rangle|^2=J^2\).
If \(\lambda_j\ge0\) are A's eigenvalues, their summability gives
\(\sum\lambda_j^2\le(\sum\lambda_j)^2\). Hence

\[
                  J^4\le T_2\le T^2.                               \tag{4}
\]

No finite-rank replacement or equality with the trial bound is asserted.

### Certified whole-kernel integration

The complete certificate and its implementation are
`scripts/primitive-hankel/coefficient-test-24.json` and
`scripts/primitive-hankel/coefficient-test-24.py`. Reproduce from this
notebook with

```sh
python3 scripts/primitive-hankel/coefficient-test-24.py
```

Here are the analytic bounds underlying the algorithm; the certificate
is not justified by a `rigorous` flag or by a quadrature preview.
Put \(q(v)=(8v^2-12v)e^{-v}\). A kernel summand equals
\(e^{u/2}q(\pi n^2e^{2u})\), and

\[
q'(v)=-4(2v-1)(v-3)e^{-v}<0\quad(v\ge\pi>3).
\]

On a cell \([a,d]\), a rigorous lower bound for K is
\(e^{a/2}\sum_{n=1}^2q(\pi n^2e^{2d})\); an upper bound is
\(e^{d/2}\sum_{n=1}^2q(\pi n^2e^{2a})+\epsilon\), where

\[
\epsilon=\frac{8\pi^2\,81e^{-9\pi}}{1-16e^{-7\pi}}<10^{-8}.        \tag{5}
\]

To prove the uniform omitted-series bound (5), use
\(q(v)\le8v^2e^{-v}\). The function
\(e^{9u/2}e^{-\pi n^2e^{2u}}\) decreases on \(u\ge0\), since its
logarithmic derivative is \(9/2-2\pi n^2e^{2u}<0\).
For \(n=3+j\), \(n^4\le81\,16^j\),
\(n^2\ge9+7j\), and sum the resulting geometric series at \(u=0\).
Every omitted term is positive, so omitting them from the lower bound
is valid. No single-term model substitutes for K.

For the half-line beyond 2, the same inequalities with \(n=1+j\) yield

\[
K(u)\le\frac{8\pi^2e^{9u/2}e^{-\pi e^{2u}}}
                   {1-16e^{-3\pi}}
       \le16\pi^2e^{9u/2}e^{-\pi e^{2u}}.                          \tag{6}
\]

Here \(n^4\le16^j\), \(n^2\ge1+3j\), and
\(16e^{-3\pi}<1/2\). The elementary bounds
\(3<\pi<4\), \(e^4>54\), \(e^{13}>256\) are enclosed explicitly by
the script. For \(u=2+w\), \(w\ge0\),
\(e^{2u}=e^4e^{2w}\ge54(1+2w)\). Therefore (6) gives

\[
 K(2+w)\le256e^{-153}e^{-319.5w}
          <e^{-140}e^{-70w}=e^{-70u}.                              \tag{7}
\]

For integer \(j\ge0\) and rate r, the exact exponential envelope
integral, obtained by integration by parts, is

\[
\int_2^\infty u^je^{-ru}du
 =e^{-2r}\sum_{k=0}^j\frac{j!}{(j-k)!}\frac{2^{j-k}}{r^{k+1}}.      \tag{8}
\]

Use r=70 for the three moment tails and r=140,j=1 for (2).
Their upper bounds are respectively below
\(2.258\cdot10^{-63}\), \(9.161\cdot10^{-63}\),
\(3.718\cdot10^{-62}\), and \(3.581\cdot10^{-124}\).

On [0,2], use 4000 cells of exact width 1/2000. Multiply each positive
kernel cell enclosure by the exact cell integral of \(u^j\) for the
moments, or square that enclosure and multiply by the cell integral of
u for (2). For (3), multiply by the exact integral of the piecewise
linear \(w_b\) and divide by b; both corners b and 2b are mesh points.
Add the nonnegative tails (8) only to upper endpoints. This is an
interval bound on every cell, with no unbounded-domain or smoothness
assumption hidden in a sampling rule.

All arithmetic uses 50-significant-digit Decimal interval endpoints,
with ROUND_FLOOR and ROUND_CEILING at every elementary operation.
The implementation uses neither binary floating point nor Decimal.exp.
Pi is enclosed by Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) and exact rational alternating
series, with 55 and 18 terms respectively and the first omitted term
as the error bound. To enclose \(e^x\) for \(x\ge0\), reduce to
\(y=x/2^m\le1/8\), sum terms k=0,...,36 with directed rounding, and
bound the positive remaining tail by

\[
 \frac{y^{37}}{37!}\frac1{1-y/38}.
\]

Then square the resulting interval m times. For negative x use the
reciprocal of the positive exponential enclosure. For interval x use
monotonicity and its two endpoints. Thus rounding, pi uncertainty,
exponential-series error, omitted n, cell variation and integration
tails are all included. Exact rational series and the displayed
inequalities, rather than an imported numerical convergence claim,
justify these elementary evaluation steps.

### Residual and factorial check

Outward-rounded excerpts of the complete enclosures are:

| Quantity | Lower bound | Upper bound |
| --- | ---: | ---: |
| \(M_0\) | 0.4965499282 | 0.4976918892 |
| \(M_2\) | 0.0229231967 | 0.0230208067 |
| \(M_4\) | 0.0029544576 | 0.0029712878 |
| \(T\) | 0.0802855244 | 0.0806857625 |
| \(J\) | 0.2364616436 | 0.2371348528 |
| \(S_1\) | 0.02302950 | 0.02318076 |
| \(S_2\) | 0.0000328469 | 0.0000415166 |

The S rows use L025's exact rational expressions and the full-precision
moment intervals in the certificate, rather than the shortened moment
rows in this table. Those enclosures, with (4), give

\[
 \frac{T_2}{T^2}\ge\frac{J^4}{T^2}>0.480229.
\]

Consequently exact rational arithmetic already proves

\[
\begin{split}
c^2T_2-S_2
 &>(0.02302950)^2(0.480229)-0.0000415166\\
 &=\frac{852706518689149}{4000000000000000000}>0.00021317,\\
c^2T_2-S_2
 &<(0.02318076)^2-0.0000328469\\
 &=\frac{315312958861}{625000000000000}<0.00050451.
\end{split}                                                       \tag{9}
\]

The certificate also directly encloses the residual in
\([0.00021317713723842147890060417884109525923618063141887,
0.00050450059387843903635256483520718100212857894460642]\).
The inequalities in (9) use simpler rational endpoints and suffice
independently of the extra displayed digits.

Finally, the imported Plemelj series is valid near zero, for instance
when \(|cz^2|\|A\|<1\). Its normalized local logarithm is

\[
\log\det(I-cz^2A)=-cTz^2-\frac{c^2T_2}{2}z^4+O(z^6).
\]

By L025 the normalized local logarithm of \(\Xi(z)/M_0\) is
\(-S_1z^2-S_2z^4/2+O(z^6)\). In particular, L021's factorials are
\(2!=2\), \(4!=24\), and L025 gives
\(S_2=S_1^2-M_4/(12M_0)\), as used above.
The choice cT=S_1 matches the first term. Their z^4 logarithmic
coefficients differ by \(-(c^2T_2-S_2)/2\ne0\). Since their constant
and z^2 coefficients agree, their ordinary z^4 coefficients differ
by the same amount. No global logarithm, real-zero premise, equality
of unknown spectra or RH-equivalent positivity has been assumed.

A preliminary nonrigorous diagnostic is retained separately at
`scripts/primitive-hankel/diagnostic-24.json`. It is not evidence for
(1). The initially considered universal bound \(S_2/S_1^2\le2/3\)
was too coarse for this trial function; actual moment enclosures,
not that unused shortcut, establish the claimed separation.

### Independent conceptual and implementation audit — 6 November 2026, step26

The stated exclusion and both strict bounds in (1) pass this independent
audit. No mathematical correction or change of ansatz is required.
The existing Bothner/Bornemann source assessment is reused at precisely
the hypotheses stated above; no additional theorem is imported. L019,
L021 and L025 were read in full. Only their actual-kernel, moment and
local-logarithm conclusions are needed; the audit does not infer real
zeros from the paired product or use a global logarithm.

For (2), positivity and the explicit tail (7) give a finite, strictly
positive weighted integral. Cauchy–Schwarz on the product measure
justifies the adjoint calculation for every pair of L2 functions.
The trace identity is the Hilbert–Schmidt norm identity for H*H, not
a diagonal-kernel assertion for an unbounded domain. H need not be
positive as an operator. For (4), its positive-valued kernel supplies
\(J>0\), and Cauchy–Schwarz gives \(J^2\le\langle f,Af\rangle\).
A's positive trace-class spectrum gives
\(\langle f,Af\rangle\le\|A\|\le\sqrt{T_2}\) and \(T_2\le T^2\).
Thus the trial bound
concerns the full operator and does not truncate its spectrum.

The two geometric majorants are valid for every omitted index:
3+j<=3*2^j and 1+j<=2^j by induction, while
(3+j)^2-(9+7j)=(1+j)^2-(1+3j)=j(j-1)>=0 for integers j>=0.
The logarithmic derivative in the proof bounds each omitted summand
uniformly in u. For the half-line, 9/2-324=-319.5 and 9-162=-153
give exactly (7); 256<e^13 makes the final bound strict even at u=2.
The polynomial weights in all cells and the triangular trial weights
are nonnegative, and their integrals are exact Fractions. Consequently
the lower/upper cell substitutions preserve the inequalities.

Every numerical path in `coefficient-test-24.py` was inspected. Decimal
construction from integers/decimal strings is exact, Fraction conversion
rounds both endpoints outward, multiplication checks all four products,
and reciprocal reverses positive endpoints. `copy_negate` avoids ambient
precision rounding of signs. The exponential recursion uses a positive
Taylor sum and a geometric tail whose successive-term ratio is at most
y/38; the reduction loop enforces y<=1/8. Squaring positive intervals
and reciprocal for negative arguments preserve enclosure. Pi's two
alternating sums and Machin combination have the correct error signs.
All divisions in this execution have positive interval denominators.
There is no Decimal transcendental call or binary floating-point path.
Full inspected constants, moments, tails and final interval values are
in the original certificate, rather than inferred from its rigor flag.

The preserving replay and exact rational endpoint checks are implemented
in `scripts/primitive-hankel/audit-26.py`. Reproduce with

```sh
python3 scripts/primitive-hankel/audit-26.py
```

This executes the unchanged production source with a different output
pathname, producing `scripts/primitive-hankel/coefficient-replay-26.json`.
It agrees with the complete original JSON, whose bytes remain unchanged.
The separate `scripts/primitive-hankel/audit-26.json` records source and
original-certificate hashes and every check, with no failures. Using
Fraction arithmetic independently of the Decimal implementation, it
checks the S_1, S_2, c, T_2, purity and residual deductions from the stored
integrals, all displayed endpoint directions, pi's alternating bounds,
the exact addition of positive moment tails, and the rational equalities
in (9). In particular the two margins in (9) are exactly

\[
 \frac{26518689149}{4000000000000000000}>0,
 \qquad \frac{5791139}{625000000000000}>0.
\]

These are the distances of its simpler lower and upper rational bounds
from 0.00021317 and 0.00050451, respectively. The replay is not a second
integration algorithm; its role is reproducibility. The independent
analytic/code inspection and rational checks supply the audit beyond
replay. No diagnostic floating-point values are used.

Finally take a common sufficiently small disk on which
|cz^2| ||A||<1 and Xi(z)/M_0 is nonzero. The two logarithms normalized
at zero are legitimate there. Their common z^2 coefficient makes the
ordinary z^4 coefficient difference equal to the logarithmic difference
-(c^2 T_2-S_2)/2. This confirms both the sign and factor of two in the
exclusion. This audit validates a local specialization of known operator
theory; it establishes no new result beyond the checked coefficient
exclusion, no all-degree sign and no claim of originality.

### Repeated conceptual check — 6 November 2026, step31

The scheduled audit rediscovered the completed step26 audit. Independent
inspection of the proof, its L019/L021/L025 inputs, the L016/L020
convergence and normalization passages, and both programs found no defect.
The above proof and strict bounds require no correction. The preserving
launcher `python3 scripts/primitive-hankel/audit-31.py` reruns the existing
audit with only its output pathnames changed. Its full evidence is
`scripts/primitive-hankel/audit-31.json` and
`scripts/primitive-hankel/coefficient-replay-31.json`: all 32 existing
checks pass, the complete production certificate is reproduced, and hashes
record preservation of all five step24/26 source and evidence files.
This is repeated verification, not a second integration algorithm, a new
mathematical advance or a new informative obstruction. No hypothesis,
conclusion, mathematical input, ansatz or Mathlib claim changes.

## Mathlib

Full matching theorem and supporting operator/interval-arithmetic
coverage were not checked. Availability is unknown; no absence claim
is made. The mathematical operator inputs are precisely cited above;
the executable certificate is not a Lean formalization.
