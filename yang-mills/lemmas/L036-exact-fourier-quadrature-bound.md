# L036 — Uniform exact-rule Fourier quadrature bound

## Hypotheses

Use L008's exact real cutoff rho and L034's Fourier coefficients

\[
 F_h(n)=\int_{-3}^3 x^h\rho(x)e^{i\kappa_n x}\,dx,
 \quad \kappa_n=\pi n/8,\quad h\in\{0,1\},\quad |n|\le224.
\]

Let Q be the **exact** 144-point Gauss–Legendre rule separately on
[-3,-5/2], [-5/2,0], [0,5/2], [5/2,3], added together. Nodes and
weights are the exact real ones, and integrand evaluations and summation
are exact. Define F_h^Q(n)=Q(x^h rho(x) exp(i kappa_n x)).
This definition does not identify F_h^Q with the binary64 tables in
`scripts/combined-ward-response/check_continuum_pure_sectors.py`.

The finite exact dyadic coefficients defining the degree-200 polynomial

\[
 p(x)=\sum_{j=0}^{200} c_j T_j(4x-11),\qquad 5/2\le x\le3,
\]

are stored completely under `/rho_coefficients` in
`scripts/combined-ward-response/exact-fourier-quadrature-certificate.json`.
That array specifies an auxiliary polynomial, not an assumed approximation.
The proof below verifies its residual with outward integer arithmetic.

## Conclusion

Uniformly in the stated n,

\[
 |F_0^Q(n)-F_0(n)|<7\,10^{-14}<6\,10^{-12},\qquad
 |F_1^Q(n)-F_1(n)|<2.1\,10^{-13}<9\,10^{-12}.                 \tag{1}
\]

Thus the exact rule satisfies the quadrature part of L035's proposed
input budget eta=1e-12, H_0=6, H_1=9. It does **not** discharge that
lemma's hypothesis for the stored binary64 transforms: stored nodes,
weights, rho/phase evaluation and summation still need error enclosures.
No retained response sign, full Ward coefficient, logarithm, forest
compensation or interacting reflected-error bound follows.

## Proof

### 1. Exact quadrature and approximation principles

Use the standard Gauss–Legendre quadrature theorem: an m-point rule on
a real interval integrates polynomials through degree 2m-1 exactly,
has positive weights and integrates the constant one to the interval
length. These facts apply after affine scaling, and by linearity to
complex polynomials. Consequently, if a complex polynomial q of degree
at most 287 approximates f uniformly on a panel of length L with error
d, then

\[
 |\int f-Qf|\le |\int(f-q)|+|Q(f-q)|\le2Ld.                \tag{2}
\]

For clarity, the theorem here requires no numerical claim about roots:
divide a polynomial of degree <=287 by the degree-144 Legendre
polynomial. The quotient has degree <=143, so orthogonality removes
its integral, while the remainder is integrated by interpolation at
the 144 exact roots. Positivity follows by applying exactness to the
square of each degree-143 cardinal polynomial: its integral is the
corresponding weight and is strictly positive. This recalls the named
standard theorem only to check its hypotheses and polynomial degrees.

We also use the standard Cauchy coefficient estimate. If an analytic
function on [-1,1] is bounded by M on the Bernstein ellipse of
parameter R>1, truncating its Chebyshev series at degree d gives
uniform error <=2M R^(-d)/(R-1). Indeed, compose with
z=(w+w^(-1))/2; the positive Laurent coefficients are bounded by
M R^(-j), and the symmetry w -> w^(-1) makes the positive-degree
Chebyshev coefficients twice those coefficients. Summing their
geometric tail proves the stated estimate. We apply it only to the
entire phase, not to rho's nonanalytic endpoints.

### 2. Analytic disks for the transition interior

Fix c in (5/2,3), set d=min(c-5/2,3-c), r=d/16, and let
u=9-z^2, v=z^2-25/4. At c, u_0,v_0>0 and u_0+v_0=11/4.
For |z-c|<=r,

\[
 |u-u_0|,|v-v_0|\le D=6r+r^2\le\min(u_0,v_0)/8.            \tag{3}
\]

To check the last inequality, u_0>=(11/2)d and v_0>=5d,
whereas r<=1/64 gives D<7d/16<5d/8. The disks therefore avoid
u=0 and v=0. On them define the analytic continuation
rho(z)=exp(-1/u)/(exp(-1/u)+exp(-1/v)). We next check that its
denominator stays nonzero, with |rho(z)|<=2.

Write s=min(u_0,v_0), l=max(u_0,v_0). If s<=1/2, the exponential
with small real denominator is dominated by the other. The elementary
reciprocal-disk bounds Re(1/t)>=1/(t_0+D) and
Re(1/t)<=1/(t_0-D), for |t-t_0|<=D<t_0, give

\[
 \operatorname{Re}(1/t_s)-\operatorname{Re}(1/t_l)
 \ge\frac1{s+D}-\frac1{l-D}
 \ge\frac{16}{9}-\frac{16}{35}>1.
\]

The modulus ratio of these exponentials is consequently <e^(-1)<1/2.
If the numerator is the smaller, |rho|<1; if it is the larger,
|rho|<2. Neither case permits a denominator zero.
If s>1/2, instead

\[
 |\operatorname{Im}(1/u)|\le\frac{D}{(u_0-D)^2}
 \le\frac8{49u_0}<\frac{16}{49},
\]

and the same bound holds for v. Both exponentials therefore have
real part greater than half their modulus, since 16/49<pi/3.
Their sum has modulus greater than half the sum of their moduli;
again |rho|<=2 and the denominator is nonzero. The reciprocal-disk
bounds used above also follow directly from the image circle under
t -> 1/t, so they hold for complex perturbations, not only real ones.

By Cauchy's estimate, the Taylor coefficients about c have absolute
value <=2/r^j. On a real cell [c-lambda,c+lambda] with lambda<r,
the remainder after degree 24 is bounded by

\[
 R_c=\frac{2(\lambda/r)^{25}}{1-\lambda/r}.                  \tag{4}
\]

### 3. Endpoint collars and complete polynomial residual certificate

Put delta=1/256. On the lower collar [5/2,5/2+delta],
0<=v<=6delta and u>=11/4-6delta. Hence
exp(-1/v)/exp(-1/u)<=exp(-41), by continuity also at v=0.
The analogous estimate, exchanging u and v, holds on [3-delta,3].
Thus, with b=exp(-41)/(1-exp(-41)),

\[
 |rho-1|<=b\quad\hbox{on the lower collar},\qquad
 |rho|<=b\quad\hbox{on the upper collar}.                    \tag{5}
\]

The conservative denominator 1-exp(-41) is valid; on the real
axis one could use the sharper 1+exp(-41). No complex endpoint
continuation is assumed. Each collar is covered by 16 equal cells.
The remaining interval is covered by 533 rational cells: beginning
at L=5/2+delta, use width min(min(L-5/2,3-L)/64,3-delta-L),
then advance L by that width. Every cell has center c, halfwidth
lambda and r as in section 2; its lambda/r<=1/4 is verified exactly.
The saved audit checks every adjacency and both endpoints, so this
is full coverage rather than sampling.

Here is the integer certificate's arithmetic and error logic. Set
S=10^80. An interval [a/S,b/S] uses integers a,b, with every
addition exact and every multiplication/division rounded outward
by integer floor/ceiling of all endpoint products/quotients.
Division is performed only when its denominator interval avoids zero.
Each exact dyadic c_j is enclosed this way. Full Taylor coefficients
of p(c+lambda t) are then enclosed using
T_0=1, T_1=4c-11+4lambda t, T_(j+1)=2T_1 T_j-T_(j-1).
No polynomial tail is dropped.

For rho, square c+lambda t and form u,v. Reciprocals use
q_0=1/a_0 and q_n=-(sum_(k=1)^n a_k q_(n-k))/a_0.
For an exponential e^q, its coefficients obey
e_n=(sum_(k=1)^n k q_k e_(n-k))/n. Quotients use the analogous
coefficient identity obtained by multiplying by the denominator.
These exact algebraic recurrences enclose the first 25 scaled rho
coefficients. Its constant exponentials are enclosed by reducing a
nonnegative x to x/2^k<=1/8, enclosing exp(-x/2^k) between the
alternating Taylor partial sums of orders 61 and 60, and squaring
k times. Those terms decrease in magnitude, so the alternating
remainder bounds apply. Interval operations propagate all rounding.

On each interior cell, if a_j,p_j enclose those rho and polynomial
coefficients, the error bound is

\[
 \sum_{j=0}^{24}\sup|a_j-p_j|
 +\sum_{j=25}^{200}\sup|p_j|+R_c.                            \tag{6}
\]

The R_c saved in the certificate is rounded upward to scale S.
On each collar cell, replace the rho Taylor sum by its baseline
0 or 1 and add b from (5), enclosing the complete polynomial
coefficient sum in the same way. The exp(-41) bound defining b
is itself computed with the just-described outward exponential rule.

Reproduce the complete finite check with

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_exact_fourier_quadrature.py
python3 scripts/combined-ward-response/audit_exact_fourier_quadrature.py
```

The first command stores all 201 exact coefficients and all 565 cell
bounds in `scripts/combined-ward-response/exact-fourier-quadrature-certificate.json`.
The second checks every saved cell, its disk condition (3), remainder,
complete coverage, degrees and the final rational bounds, and stores
`scripts/combined-ward-response/exact-fourier-quadrature-audit.json`.
It does not independently recompute the Taylor jets. The mathematical
justification for those jets is the outward arithmetic and recurrences
above, implemented in the first script; this is an informal exact
arithmetic verification, not a formal proof assistant certificate.

There are no failed cells. The maximum bound is below the rational
number 3.48e-14 (its outward display is 3.4708284560e-14). Therefore

\[
 \epsilon:=\sup_{[5/2,3]}|rho-p|<3.48\,10^{-14}.             \tag{7}
\]

NumPy only proposes the exact dyadic coefficients. Neither its
coefficient computation nor refinement agreement is a premise of (7):
an inaccurate proposal would fail (6). Bounds are regenerated and
checked from the specific saved polynomial.

### 4. Phase approximation and panel assembly

For |n|<=224, |kappa_n|<=28pi<88. A panel's affine coordinate has
halfwidth d. On the Bernstein ellipse of parameter 4 the phase is
bounded by exp(|kappa_n|d(4-1/4)/2). On a transition panel d=1/4;
on a core panel d=5/4. Using e<3 gives valid respective majorants
3^42 and 3^207. The elementary inequalities pi<22/7 and e<3 are
used only outward. Section 1 therefore supplies phase polynomials
of degrees 86 and 286 with uniform errors

\[
 delta_t=\frac{2\,3^{42}}{3\,4^{86}},\qquad
 delta_c=\frac{2\,3^{207}}{3\,4^{286}}.                       \tag{8}
\]

On the positive transition panel use x^h p(x) times its degree-86
phase polynomial. Its degree is <=200+86+h<=287, and its uniform
error is <=3^h[epsilon+(1+epsilon)delta_t]. On the negative
transition panel use p(-x), since rho is even; the same estimate
and degree apply. On the core rho=1, and x^h times the degree-286
phase polynomial has degree <=287 and error <=(5/2)^h delta_c.

The two transition panels have total length 1 and the two core
panels total length 5. Equation (2) consequently yields

\[
 |F_0-F_0^Q|<=2\epsilon+2(1+\epsilon)delta_t+10delta_c,
\]
\[
 |F_1-F_1^Q|<=6\epsilon+6(1+\epsilon)delta_t+25delta_c.        \tag{9}
\]

The certificate evaluates these using the exact maximum from section
3, with outward displays 6.9416569119e-14 and 2.08249707357e-13.
The all-cell rational audit verifies they are strictly below 7e-14
and 2.1e-13, respectively. This proves (1), simultaneously for both
signs of n and for n=0. It does not transfer an exact-rule estimate
to stored floating-point data without the additional error comparison.

The general flow/matching inputs remain imported with the precise
primary citations and qualifications in
`drafts/literature/2026-09-26-current-target.md`. They do not certify
this numerical rule. This elementary specialized quadrature verification
is needed for the actual cutoff rho and chosen rule; it is a reproduction
of standard approximation and interval arithmetic methods, with no
claim of progress beyond the literature checked for those methods.

## Mathlib

Full matching coverage for this cutoff and certified quadrature bound:
not checked. Supporting Gauss–Legendre exactness/positivity, Cauchy
estimates, Chebyshev series, Taylor recurrences and interval arithmetic:
not checked. No matching theorem name or direct Mathlib link is asserted.
The Python certificate is not a Mathlib formalization; unknown coverage
does not imply absence.
