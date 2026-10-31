# Common pole phase: bounded attempt in progress

The approved target and exact bump/prime sets are those in
`literature/2026-10-30-pole-compensated-sonin-increment-test.md`.
Main gap: all-degree positivity; downstream use would be a signed
collective comparison towards L522, not an automatic nullvector import.
Test: finite separate traces and Delta_p=o(p^(-1/2) log p), or a
decisive signed-scale/domain obstruction. No result is yet claimed.

Source passages rechecked: bramble_trace paper 2 v2, Section 1,
(5.2), (6.1)--(6.3), Theorem 6.5 and (6.20)--(6.26), Theorem 7.1
and (7.1)--(7.4). The prior assessment is reused; this is a research
attempt, not a new source-discovery step. Exact source URL:
https://rstation.ai/problems/riemann_hypothesis/papers/2 .
The relevant previous stop is
`../ATTEMPTS/2026-10-30-uncorrected-sonin-arithmetic-import-stop.md`.
No matching pole-projection lemma was found in the scoped local search.

## Partial reasoning; not a proved range identity

In the lower Fourier half-plane the prospective causal pole factor is

    d_M(z)=exp(2 integral_0^M cosh(v/2)(exp(-izv)-1)/v dv).

It is analytic, zero free and bounded by one there. On the real line,
d_M(-t)/d_M(t)=exp(i chi_M(t)). Its inverse is not bounded: the
near-zero part of the integral gives polynomial decay of order two.
Thus the bounded-inverse Euler argument cannot simply be cited for
d_M. A possible repair is to factor d_M by (1+it)^(-2) and check
the remaining factor and its inverse at fixed M. Any changed rational
background and trace finiteness still require proof.

For the proposed M=L+2, the formal leading real-line log weight of
D_<p d_M, with A=sqrt(p)/L, is

    4 A [Re(exp(itL)(e exp(2it)-1)/(1+2it))-e].

The envelope is largest at zero: its squared amplitude is
[(e-1)^2+4e sin(t)^2]/(1+4t^2), and e<(e-1)^2.
This suggests a changed weighted-localization argument, but the
formula has not yet been supplied with a uniform error or a correct
range model. In particular it proves no trace increment bound.

Centering the two packets changes their Fourier transform only by
a unit-modulus factor relative to h+V_Lh. For L>2 the autocorrelation
at L is ||h||_2^2=1 and at kL, k>=2, is zero, including the padded
support endpoints. The common pole term cancels in the difference.
These checks do not assert a full-Weil identity for either partial
prime set.

## Developed continuation, awaiting canonical write-up

The missing fixed background can be made explicit. Put
b(z)=(z+i)/(z-i), e_M(z)=(1+iz)^2 d_M(z), and
k_M(v)=cosh(v/2)1_(0,M)(v)-exp(-v). Frullani's identity gives
log e_M=2 integral_0^infinity k_M(v)(exp(-izv)-1)/v dv.
Here k_M/v is integrable, so e_M and its inverse are bounded
analytic multipliers in the lower half-plane, for each fixed M.
The fixed background is u_*=u_infinity b^(-2); the corrected
space is (D_P e_M) times its Toeplitz kernel. Its members become
entire after multiplication by (z-i)^2. Hardy evaluation and the
gamma ratio give order exp(C R log R) growth, plus polynomial
real-line evaluation bounds. These suffice for finite separate
smoothed traces, with constants allowed to depend on p.

For a weighted unit vector, ||f_0||_2<=exp(C A). On
J=[-L^(-2),L^(-2)], the weight is at least exp(-4A-O(A/L)).
Taylor approximation of (z-i)^2 f_0 on radius A/(log A)^3,
degree K A/log A with K fixed sufficiently large, followed by
Legendre interpolation from J, gives squared evaluation at most
exp(4A+O_b(A log L/L)) on |t|<=L^b. Combining with the weight
envelope gives diagonal density <=exp(-c A L^(-4/5)) on
L^(-2/5)<=|t|<=L. This is the prospective corrected counterpart
of source (6.20), not an invocation of its uncorrected version.

The common-M Euler range identity then gives
S_+=D_p S_- G^(-1) S_- D_p^*, with
G=(1+r)^2 I-r S_- B S_- and G>=(1-r)^2 I.
Source (6.21)--(6.26) apply to this Toeplitz kernel without a
background-dependent constant. The same three frequency regions
give covariance O_h(L^(9/10)), hence Delta_p=O_h(r L^(9/10)).
The arithmetic benchmark remains exactly -2rL for L>2.

Completed: full proof and qualifications are now canonical in
`../lemmas/L526-common-pole-phase-sonin-prime-increment.md`.
The auxiliary estimate is unaudited. This draft retains the earlier
unresolved stage; the completed outcome is an informative negative
for the prescribed local absorption test, with separate audit
coverage nominated in PROGRESS.md. No complete RH candidate exists.
