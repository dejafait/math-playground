# Corollary 947b: the fixed negative-tail uniform allowance exceeds the margin

## Hypotheses

Use L938's exact continuous signed density v: all34 rows, twelve
labelled factors, factorials and retained M_0^12 normalization. Let
p and epsilon be its unchanged degree256 kernel polynomial and full
uniform error on[0,8], using257 nodes, theta cutoff8, precision200
and rational coefficient grid10^-120. Let v_p be the corresponding
polynomial-kernel density on that compact interval. Retain L938's
directed Decimal/exponential/pi and exact-integer execution contracts;
the libraries and inherited theta-node producer are not independently
verified here. No RH, density sign, effective eventual-sign onset,
primitive crossing bound or determinant positivity is assumed.

Fix the tilt1/10, split8 and threshold from L947,

    m = 8.935649629627030*10^-35,
    B_4 = integral_4^infinity exp(E/10)max(-v(E),0)dE.

Test precisely the additive full-uniform-error certificate of
assessment85: combine the signed polynomial on[4,8], pay the full
kernel-replacement allowance there, and pay a separate nonnegative
negative-row tail bound beyond8. No refinement is included.

## Conclusion

Define the prescribed positive allowance

    W = 293/540,
    Z = W/(2^36*17!),
    A_K = exp(4/5)*12 epsilon 8^11*pi^6*Z*(8^18-4^18)/18.

Under the retained contracts,

    3.265161739633638*10^-32 <= A_K <= 3.265161739633639*10^-32,
    365.4084341901312 <= A_K/m <= 365.4084341901313.

Thus this fixed additive certificate cannot give B_4<m, even if its
other two nonnegative allowances were zero. This is an informative
certificate limitation, not a lower bound for B_4 or for the actual
kernel-replacement error. B_4<m itself, signs beyond8, global primitive
variation and all-degree mixed positivity remain undetermined.
This specializes known product/beta/exponential estimates; it is not
a new general theorem beyond the sources assessed.

## Proof

### Applicability on the entire compact shell

L938(9),(15),(16) apply for every0<=E<=8, since each simplex energy
Et_i is in[0,8]. They give the absolute pointwise estimate

    |v(E)-v_p(E)| <= 12 epsilon 8^11*pi^6*Z*E^17.             (1)

Here the triangle inequality is applied only to the error. To verify
the constant, each row's positive simplex integral is
product Gamma(k_i+1/2)/Gamma(18). Its twelve beta parameters are
k_i+1/2>0, including k_i=0. Cancelling the original factorials by
Gamma(k+1/2)=sqrt(pi)(2k)!/(4^k k!) gives

    pi^6/(2^36*17!)*|c_alpha|/product_k(k!)^alpha_k.

Every row has twelve factors and sum k_i=12; there is no permutation
factor. Summing all34 absolute row weights gives W. This uses precisely
the positive beta and gamma identities cited and specialized in L938,
[DLMF5.12.1](https://dlmf.nist.gov/5.12#E1) and
[DLMF5.5.1/5](https://dlmf.nist.gov/5.5#E5).
The singular individual factors cause no omitted boundary term:
their beta weights are integrable, and v,v_p are continuous densities.

For real a,b, max(-a,0)<=max(-b,0)+|a-b|. Apply this with
a=v(E), b=v_p(E), multiply by the positive exponential and integrate.
Since exp(E/10)<=exp(4/5) on[4,8], (1) proves

    integral_4^8 exp(E/10)max(-v(E),0)dE
       <= integral_4^8 exp(E/10)max(-v_p(E),0)dE + A_K.       (2)

The integral of E^17 is (8^18-4^18)/18; equivalently the
normalization after integration is W/(2^36*18!). This distinction
between17! and18! is checked independently in the certificate.
L938(2) ensures finiteness of B_4 and of every positive row tail.
The polynomial in (2) is used only on[4,8], never at infinity.

Any upper bound for the first term on the right of (2) is
nonnegative. So is the separately paid tail bound beyond8.
The prescribed sum of these two bounds and A_K is at least A_K.
Consequently A_K>m prevents this particular sum from certifying
B_4<m. An oversized upper allowance does not force any corresponding
lower bound for the actual error or for B_4.

### Exact evaluation and retained qualifications

Reproduce with

    python3 scripts/heat/l938-negative-tail-allowance-87.py

The full certificate is
`scripts/heat/l938-negative-tail-allowance-87.json`.
The script reads every257 coefficient interval and chosen rational
coefficient, reconstructs each radius eta_l and the full exact value

    epsilon=8*10^9*(2/3)^256+sum_l eta_l,

and checks equality with the saved error. Its outward scale is
[6.663887684939326,6.663887684939327]*10^-36. All34 canonical rows
and their exact beta weights are checked, giving exactly

    Z=293/13199033127778602178314240000.

It reads all5101 step50 audit flags and checks the selected inherited
kernel-certificate hash. Those flags and a hash do not independently
verify the analytic kernel enclosure, theta-node computation or
integer implementation. No convolution polynomial or endpoint
producer is required or rerun for this allowance test.

For the exponential use its positive power series
[DLMF4.2.19](https://dlmf.nist.gov/4.2#E19), already covered by the
approved comparison. Put x=4/5 and

    s=sum_(j=0)^32 x^j/j!,
    r=(x^33/33!)/(1-x/34).

The omitted positive terms have successive ratios at most x/34<1,
so s<=exp(4/5)<=s+r. This is an exact rational enclosure; no new
transcendental-library evaluation is used. The inherited positive pi
interval is independently checked against the full128-term alternating
Machin sums and their next-term bounds, as in L037/L938's pi convention.

Let pi_-,pi_+ be these positive enclosing endpoints. The exact rational
lower and upper evaluations are

    A_- = s*12 epsilon 8^11*pi_-^6*Z*(8^18-4^18)/18,
    A_+ = (s+r)*12 epsilon 8^11*pi_+^6*Z*(8^18-4^18)/18.

Every factor is nonnegative, so A_-<=A_K<=A_+. The script checks
the independent18!-normalization form, m<A_-, and the exact ratios
A_-/m,A_+/m. The complete relevant lower rational and complete
summary were inspected, not accepted from a truncated preview.
Directed16-digit displays are themselves compared with the exact
rationals. All5682 recorded checks pass, with no failures. Their
inheritance and library qualifications remain in force.

The ratio is strictly above365, whereas the complete certificate
would need a ratio strictly below1. The stipulated stopping test
therefore fires. No Bernstein polynomial or Chernoff tail computation
is performed and no budget is changed. A future attempt needs a
materially different cancellation/error input and separate source
coverage; this result does not bar other bounds for B_4.

## Mathlib

Full or supporting Mathlib coverage of this exact density/allowance
certificate is not checked; unknown availability is not evidence of
absence. The mathematical inputs are the cited standard beta/gamma
identities and exponential series, with L938's qualified approximation
and L947's endpoint threshold.
