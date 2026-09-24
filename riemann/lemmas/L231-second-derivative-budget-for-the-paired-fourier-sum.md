# Lemma 231: second-derivative budget for the paired Fourier sum

**Hypotheses.** Use L230's F_H and divisor cutoff D=N^(1/4), with
H=ceil(N^6), L228's wholly contained intervals and endpoints, and
L227's benchmark B_0. Put M=h/N, so M is comparable to sqrt(N).
For fixed a,c,d,e,k write t=k/e and

Q_(e,k)=sum_(b in D(a,c,d)) [exp(2 pi i t alpha(b))
                                  -exp(2 pi i t beta(b))].

**Conclusion.** Uniformly in these indices,

|Q_(e,k)| <= C min(1,t) min(M, M sqrt(t)+t^(-1/2)).       (1)

Summing (1) with the absolute Fourier and divisor coefficients gives

|F_H| <= C N²h (1+log D)(1+log H).                       (2)

In fact L230's uniform boundedness of S_H gives the stronger bound

|F_H| <= C N²h (1+log D).                                (3)

Neither bound implies F_H=o(B_0). This is an insufficiency of these
upper-bound calculations, not a lower bound for the actual sum or
an obstruction to cancellation across its indices.

**Proof.**

Let v=cd. Throughout the interval, a is comparable to N, v to N²,
and alpha,beta to N². Direct differentiation yields

alpha''(b)=-(av)^2/(4 alpha(b)^3),
beta''(b)=-[a(v+1)]^2/(4 beta(b)^3).

Thus the absolute second derivatives of t alpha and t beta lie
between fixed positive multiples of t, uniformly even at the largest
frequency. The interval has length O(M). The standard named van der
Corput second-derivative test, in the form recorded in
foundations/notation-and-inputs.md, bounds either exponential sum,
and each of its initial partial sums, by

C [M sqrt(t)+t^(-1/2)].                                 (4)

Empty and singleton partial sums satisfy this too: M>=1 eventually
and M sqrt(t)+t^(-1/2)>=2 sqrt(M). The trivial bound is O(M).
For t>=1 the triangle inequality proves (1) directly.

For 0<t<=1 keep the pair intact. Set ell=beta-alpha and
A(b)=1-exp(2 pi i t ell(b)). L228 gives 0<ell<3/4 and
ell'=O(1/N), hence

sup |A| <= C t, integral_D |A'| <= C t M/N <= C t.

Finite summation by parts applied to
Q_(e,k)=sum_b exp(2 pi i t alpha(b)) A(b)
therefore multiplies the uniform partial-sum estimate (4) by O(t).
The direct absolute bound for this weighted sum is O(tM).
This proves (1), including arbitrary real interval endpoints.
The phase difference itself is an amplitude; replacing Q by a sum
of exp(2 pi i t (beta-alpha)) would be an invalid identity.

We now sum explicitly. Since H>=D>=e, the low-frequency contribution
for each e satisfies

sum_(1<=k<=e) |Q_(e,k)|/k
 <= C sum_(k<=e) [M sqrt(k/e)+sqrt(e/k)]/e
 <= C(M+1) <= C M.                                     (5)

Here sum_(k<=e) sqrt(k)<=C e^(3/2) and
sum_(k<=e) k^(-1/2)<=C sqrt(e), by integral comparison.
For k>e the capped bound in (1) is O(M), giving

sum_(e<k<=H) |Q_(e,k)|/k <= C M log(H/e).                (6)

The Fourier coefficient in S_H has magnitude 1/(pi k), so (5)-(6)
apply to its imaginary part as well. There are O(N²) ordered c,d,
and O(N/e) admissible a divisible by e. Dropping the absolute values
of the Möbius coefficients and the weights w_a only enlarges the bound.
Consequently

|F_H| <= C N³ M sum_(e<=D) [1+log(H/e)]/e,

which proves (2) since N³M=N²h. Separately, |S_H|<=C from L230
bounds each paired sawtooth by a constant. Counting the O(M) integers
b and summing N/e over e<=D proves (3).

The failure is already visible in (1) at k=e=1: its right-hand
scale is M, the trivial interval scale. The pair amplitude is O(1)
there, not a power of N smaller. More generally k>=e makes the
capped second-derivative expression equal to M. Thus the procedure
has no uniform saving for this entire frequency range. With the
prescribed D,H, (2) is O(N²h (log N)²), and (3) is
O(N²h log N). Using the established lower bound for B_0 only gives
relative bounds O((log N)^3) and O((log N)^2), respectively.
The upper bound B_0=O(N²h) also confirms that neither displayed
majorant is itself o(B_0). This does not assert these majorants are
attained by F_H. Möbius signs and cancellation between triples or
frequencies have not been estimated by this procedure.

## Qualifications, verification

Only the bound and the failure of this method to reach the desired
scale are proved. L230's reduction remains valid; cancellation in
F_H, other progression estimates, the signed comparison and RH remain
unproved. No new assertion about the distribution of phases is used.

Verification is analytic: exact second derivatives, uniform curvature
comparisons, partial summation with the paired amplitude, both elementary
frequency sums, divisor multiplicities, and benchmark exponents.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
