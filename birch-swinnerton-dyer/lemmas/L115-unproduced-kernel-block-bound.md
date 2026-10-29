# L115 — Uniform absolute bound for the unproduced kernel block

## Hypotheses

Use the fixed normalized elliptic newform of conductor 389 in L101,
with its real Fourier coefficients a_n and its coefficient majorant
|a_n|<=n. Let t be any real number in [3/10,1/2], and use exactly
L101's kernel

\[
J_n(t)=\int_1^{128}e^{-tny}\frac{\log y}{y}\,dy.
\]

No computed kernel endpoint, derivative approximation, published
analytic order or additional coefficient computation is an input.

## Conclusion

Uniformly for every such t,

\[
0\le 4\sum_{n=43}^{128}\frac{|a_n|}{n}J_n(t)
 <\frac{520}{387}\,2^{-16}
 =\frac{130}{387}\,2^{-14}<2^{-14}.
\]

In particular the absolute value of the corresponding signed block
is strictly less than 2^-14, by the triangle inequality. This is a
known-method REPRODUCTION of a cutoff-specific estimate. It is not
a derivative enclosure, a nonvanishing assertion or a new BSD case.
The original 128-output finite-arithmetic contract of L101 is unchanged.
The separate critical audit of 2026-10-25, step 478, passes as recorded
below. This is informal verification, not a formal or numerical certificate.

## Proof

**Imported inputs and the reason for this specialization.** L101's
audited positive full-kernel majorant and exponential/geometric-tail
method are the mathematical inputs. Its coefficient bound is imported
there from Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2, Lemma 4 and its proof, printed pp.6–7
([primary version](https://arxiv.org/pdf/1608.06423v2#page=7)).
This applies to the specified normalized elliptic newform; no bound
for arbitrary unnormalized cusp forms is asserted. The elementary
inequality log(y)<=y-1 for y>0 is NIST DLMF 4.5.4
([equation](https://dlmf.nist.gov/4.5.E4)), as already used in L101.
The ready source assessment is
`drafts/literature/2026-10-25-unproduced-kernel-block-bound.md`.
L101's proved Fourier remainder begins at n=129, so a citation to
that numerical bound does not establish the present n=43 cutoff.
Only this explicit cutoff comparison is supplied below; no Mellin
identity or general truncation theorem is reproved or needed here.

Put c_0=3/10 and q=exp(-c_0). On y>=1 we have
0<=log(y)/y<=1. Since t>=c_0>0 and n>=43,

\[
\begin{aligned}
0\le J_n(t)
&\le\int_1^\infty e^{-c_0ny}\,dy\\
&=\frac{e^{-c_0n}}{c_0n}
\le\frac{q^n}{43c_0}.
\end{aligned}
\]

The improper integral converges because c_0*n>0; its displayed
value follows by evaluating -exp(-c_0*n*y)/(c_0*n) at the endpoints.
All enlargements concern nonnegative functions. Applying |a_n|/n<=1
only to the actual finite block, and then enlarging a purely geometric
sum, gives

\[
\begin{aligned}
4\sum_{n=43}^{128}\frac{|a_n|}{n}J_n(t)
&\le\frac4{43c_0}\sum_{n=43}^{128}q^n\\
&\le\frac4{43c_0}\sum_{n=43}^{\infty}q^n
 =\frac4{43c_0}\frac{e^{-43c_0}}{1-q}.
\end{aligned}
\]

Here 0<q<1, so the infinite geometric sum converges. In particular
no unknown coefficients beyond n=128 or interchange with a signed
Fourier series enter this step.

For completeness, the exact elementary comparisons already used in
L101 are enough at this cutoff. The positive exponential series gives
exp(c_0)>1+c_0=13/10, hence q<10/13 and
1/(1-q)<13/3. The same series at 3 gives

\[
e^3>1+3+\frac92+\frac{27}{6}+\frac{81}{24}
 =\frac{131}{8}>16.
\]

The strict first inequality holds because every omitted term is
positive. Raising to the fourth power gives e^12>16^4=2^16.
Since 43*c_0=129/10>12, strict monotonicity of the real exponential
then gives e^(-43*c_0)<e^-12<2^-16. Consequently the previous bound
is strictly less than

\[
\frac4{43(3/10)}\frac{13}{3}\,2^{-16}
 =\frac{520}{387}\,2^{-16}
 =\frac{130}{387}\,2^{-14}<2^{-14},
\]

where the final comparison is exactly the integer inequality 130<387.
The factor four and every absolute coefficient weight have been
retained. The entire proof uses the lower endpoint c_0, so the strict
bound holds also at t=3/10 and throughout the stated closed interval.
Finally, the triangle inequality for the finite signed block gives
|4*sum_(n=43)^128 (a_n/n)J_n(t)| bounded by the nonnegative sum
just estimated; positivity never changes signs in a retained sum.

**Scope and remaining obligations.** This estimates only the finite
block n=43,...,128 with y in [1,128]. L101's n>128 full-kernel and
y>128 retained-kernel remainders are separate. A future 42-kernel
assembly must explicitly account for this block, those remainders,
actual-parameter propagation, retained signed coefficients, kernel
errors and arithmetic errors. Neither that new contract nor any
assembled value or zero exclusion is established here. All original
missing certificates and their provenance obligations remain missing
under L101's existing contract.

### Separate critical audit — 2026-10-25, step 478

**Verdict and input scope.** PASS for precisely the displayed finite-block
bound. This audit reread the complete producing proof and L101's kernel,
coefficient majorant, analytic remainders and finite-arithmetic contract,
reusing the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-unproduced-block-bound-audit.md`.
No correction to the producing inequality was necessary. The imported
coefficient bound concerns the same normalized elliptic newform; the
Wuthrich and DLMF citations above provide supporting inputs, not this
cutoff's numerical conclusion. The proof does not invoke the derivative
identity, lower-order vanishing, a computed coefficient list or L103.

**Domains and positivity.** For y>=1, log(y)>=0 and DLMF's inequality
gives log(y)/y<=(y-1)/y<=1, including the value zero at y=1.
For every allowed t, n>=43 and y>=1, t*n*y>=c_0*n*y>0;
therefore exp(-t*n*y)<=exp(-c_0*n*y). Enlarging [1,128] to
[1,infinity) is valid for the nonnegative majorant. Its integral is
exp(-c_0*n)/(c_0*n): the exponential tends to zero at infinity,
and c_0*n is strictly positive. Replacing n by 43 only in the
denominator enlarges the bound. These facts also hold at t=3/10;
the upper endpoint t=1/2 requires no separate approximation.

**Finite weights and convergence.** Each of the 86 terms has
0<=|a_n|/n<=1. Applying this inequality and retaining the factor four
gives exactly 4/(43*c_0) times the finite sum of q^n. Since
0<q=exp(-c_0)<1, its nonnegative extension sums to q^43/(1-q).
This is a geometric majorant, not an extension of the signed coefficient
sum. Thus no coefficients beyond 128 and no interchange of a signed
series and an integral are assumed.

**Strict arithmetic checks.** Positive omitted exponential terms give
exp(3/10)>13/10 and hence 1/(1-q)<13/3. The degree-four partial
sum at 3 is (8+24+36+36+27)/8=131/8>128/8=16.
Thus exp(12)>16^4=2^16. Since 43*c_0=129/10>120/10=12,
exp(-43*c_0)<2^-16. All multiplied bounds are positive, so the
resulting strict upper bound is
4*(10/129)*(13/3)*2^-16=(520/387)*2^-16
=(130/387)*2^-14. Its ratio to the required threshold 2^-14 is
130/387<1, with exact rational margin 257/387. The finite triangle
inequality gives the same strict upper bound for the absolute signed
block, including when coefficients are negative or zero.

**Contract and dependency check.** L101 defines exactly the same J_n
and weight 4*a_n/n. Its omitted regions are n>128 with full kernels
and y>128 for n<=128; neither is included in this finite-block estimate.
Its conditional formula still requires all 128 coefficient and kernel
certificates, parameter control and arithmetic control; a nonvanishing
claim additionally requires subsequent zero exclusion.
The present bound does not prove its sufficient radius
B<2^-40: the displayed block allowance itself exceeds 2^-40.
It gives no lower bound on the true block error and proves no impossibility
of a more accurate estimate. It also supplies no signed center against
which even a larger radius could be tested. No revised 42-kernel contract
is selected or proved here. L101 remains the sole direct mathematical
input in the unchanged DAG row. Historical production failures and the
86 missing outputs under the original contract remain unresolved.
No general rank comparison, Sha assertion or refined BSD claim follows.

## Mathlib

Full matching Mathlib coverage was not checked. No absence claim is
made. The proof uses only the imported coefficient bound, elementary
real integration, exponential comparisons and a convergent geometric
sum; no formal verification of this specialization is claimed.
