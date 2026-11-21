# L877 — The stated binomial-to-step coefficient norm diverges

## Hypotheses

Let N>=1 be an integer. For positive integers k define

    a_N(k)=sum_(n=k-1)^N 2^(-n-1) binom(n,k-1),  1<=k<=N,
    a_N(k)=0,                                      k>N,
    b_N(k)=1,                                     1<=k<=N,
    b_N(k)=0,                                      k>N.

Use the ordinary unweighted ell2 norm and set

    delta_N^2=sum_(k=1)^N (1-a_N(k))^2.

These are precisely the first N coordinates selected in the approved
audit of Y. Jerby, *On the approximation of the Hardy Z-function via
high-order sections*, [arXiv:2405.12557v2](https://arxiv.org/pdf/2405.12557v2),
25 March 2025, equations (13), (18), printed pp6–7. The cutoff is not
altered. No approximation theorem, zero claim or asserted coefficient
convergence from that source is a hypothesis.

## Conclusion

For every integer N>=1,

    sum_(k=1)^N a_N(k)=(N+1)/2-2^(-N-1),                         (1)

    delta_N >= ((N-1)/2+2^(-N-1))/sqrt(N).                       (2)

Consequently delta_N tends to infinity as N tends to infinity, and
liminf_(N->infinity) delta_N^2/N>=1/4. In particular the unweighted
convergence to zero asserted in that version's Corollary 2.2, equation
(19), fails for these exact coefficients. This remains a contradiction
along N=floor(t/2) as t tends to positive infinity.

This is an elementary source-consistency obstruction, not a result on
actual Xi signs, zeros of sections, or RH. It does not assert a sharp
asymptotic constant or exclude approximation through oscillatory
cancellation, another cutoff, or a different norm.

## Proof

Import the binomial zero convention and finite binomial theorem from
[NIST DLMF 26.3.2](https://dlmf.nist.gov/26.3.E2) and
[26.3.3](https://dlmf.nist.gov/26.3.E3), respectively. Their indices here
are nonnegative integers. The latter identity is used at the allowed
real value x=1, so sum_(j=0)^n binom(n,j)=2^n, including n=0.
No infinite generating function or limit interchange is needed.

Reordering the finite triangle, retaining the upper cutoff k=N, gives

    sum_(k=1)^N a_N(k)
      =sum_(n=0)^N 2^(-n-1)
           sum_(k=1)^min(N,n+1) binom(n,k-1).

For 0<=n<=N-1 the inner sum is 2^n. For n=N it is
sum_(j=0)^(N-1) binom(N,j)=2^N-1. Thus the first N rows each
contribute 1/2 and the last row contributes 1/2-2^(-N-1).
This proves (1), also at N=1.

Put d_k=1-a_N(k). Equation (1) implies

    sum_(k=1)^N d_k=(N-1)/2+2^(-N-1)>0.

Finite-dimensional Cauchy–Schwarz, applied to (d_1,...,d_N) and
(1,...,1), yields

    ((N-1)/2+2^(-N-1))^2 <= N sum_(k=1)^N d_k^2=N delta_N^2.

Taking nonnegative square roots proves (2); no sign assumption on
individual d_k is needed. For N>=2 its right side is at least sqrt(N)/4,
so delta_N tends to infinity. Dividing the squared bound by N gives

    delta_N^2/N >= ((N-1)/(2N)+2^(-N-1)/N)^2 -> 1/4.

Every sequence of positive real t tending to infinity has
floor(t/2) tending to infinity, proving the source-cutoff assertion.

**Endpoint qualification.** In the source's preceding triangular
formula (10), relabeling k+1 produces an additional coordinate N+1,
of size 2^(-N-1). That coordinate is absent from its displayed (12).
The argument above uses only the common first N coordinates, so it
does not silently repair that mismatch. If the extra coordinate is
retained and compared with the unchanged step vector b_N, its squared
contribution is 2^(-2N-2)>=0, leaving the obstruction intact.
Dropping an endpoint cannot explain the divergent common-coordinate
lower bound. The source's Corollary 2.2 states ell2, not a normalized
or amplitude-weighted variant; no such reinterpretation is used here.

**Verification and scope.** All sums in the proof are finite. The
primary coefficient, step and norm displays, and the entire finite
regrouping passage on printed pp6–7, were checked directly in the
versioned PDF text. The lower bound is analytic for every integer N,
not an extrapolation from a finite computation. No mathematical script
or numerical evidence is required. This reproduces elementary known
tools for the source-specific audit; it makes no originality claim.

## Mathlib

Full matching coverage and supporting theorem names were not checked.
No absence claim is made. The mathematical inputs are the cited finite
binomial identities and the standard finite-dimensional
Cauchy–Schwarz inequality; there is no local lemma input.
