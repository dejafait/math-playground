# Lemma 204: positive proportion in quartic factor slices

**Hypotheses.** Use L202's box F_N and L203's actual integer slices,
with fixed t>0 satisfying L202's restrictions and real N tending to
infinity. For each allowed triple (a,c,d), retain exactly the b0, M,
x0 and polynomial P4 of L203. Put n=M+1 and I=[21/32,27/32].

**Conclusion.** Uniformly over every allowed triple, for sufficiently
large N depending on t,

#{0<=j<=M: frac(P4(j)) in I} >= (3/64)n.                 (1)

Consequently L203's aggregate interior count (2) with eta=1/32
is bounded below by (3/64)#F_N, and is therefore of order N³.
In particular L202's phase-selected population has order N³.
Its members have occupied full-core windows whenever W satisfies
L202's hypotheses. No coprimality or totient selection is asserted.

**Proof.**

All comparisons in this proof are uniform over the actual triples,
with constants allowed to depend on fixed t. L203 gives b0 comparable
to N, x0 comparable to N², and n comparable to sqrt(N). On the
whole real interval 0<=y<=M, differentiation of its polynomial gives

P4'''(y) = (3x0/(8b0³))(1-5y/(2b0)).                    (2)

Since M/b0=O_t(N^(-1/2)), for sufficiently large N the parenthesis
lies between 1/2 and 1. Thus there are constants c_t,C_t>0 with

c_t/N <= P4'''(y) <= C_t/N.                             (3)

For each fixed integer k!=0 apply the standard van der Corput
third-derivative test, in the form recorded in foundations, to
f(y)=k P4(y). This is a real smooth phase on the entire interval,
and its third derivative has magnitude between |k|c_t/N and
|k|C_t/N. The ratio of these bounds is fixed; there are n consecutive
integer arguments. With e(z)=exp(2πiz), the test yields

|Σ_(j=0)^M e(k P4(j))|
 <= C_t [n (|k|/N)^(1/6)+n^(1/2)(N/|k|)^(1/6)]
 = O_(t,k)(N^(5/12)).                                  (4)

Dividing by n shows that these normalized sums are
O_(t,k)(N^(-1/12)), uniformly over the triples. The N^(1/3)
first term is smaller than the displayed N^(5/12) bound. Only fixed
frequencies will be used, so no growing-frequency uniformity is assumed.

Here is an explicit continuous minorant that avoids any inference
about points near phase boundaries. Put r=3/32, q=3/4 and let

psi(z)=max(1-dist(z,q+Z)/r,0).

This is a continuous periodic triangle, supported modulo one on I,
with 0<=psi<=1_I (including the endpoints), and integral r over a
period. To compute its Fourier coefficients, convolve the periodic
indicator of [-r/2,r/2] with itself, divide by r, and translate by q.
Since r<1/2, this convolution is exactly psi. Integrating that indicator
against e(-kz) and using the finite convolution integral gives

psi_hat(0)=r,
psi_hat(k)=e(-kq) sin²(πkr)/(r π² k²),  k!=0.             (5)

In particular |psi_hat(k)|<=1/(r π² k²). Its Fourier series
converges absolutely and uniformly to psi: the coefficient bound gives
uniform convergence, and Fejér's theorem for continuous periodic
functions identifies the sum with psi. This standard named theorem
is recorded in foundations. Thus finite averaging and the series can
be interchanged without any distribution assumption.

For any integer H>=1, writing S_k for the sum in (4), we obtain

|n^(-1)Σ_(j=0)^M psi(P4(j))-r|
 <= Σ_(0<|k|<=H) |psi_hat(k)| |S_k|/n
    + 2/(r π² H).                                     (6)

Here the tail uses |S_k|<=n and Σ_(k>H) k^(-2)<=1/H.
First choose fixed H so the last term is less than r/4. Then (4)
lets us choose N large enough that the finite first sum is less
than r/4, simultaneously for every allowed triple. The average of
psi is therefore at least r/2=3/64. Its minorant property proves (1).
There is no exchange of a growing H with N, and the shift q and the
possibly large constant coefficient of P4 do not affect (4).

Every tuple has precisely one slice and one index j. Hence the sum
of n over triples equals #F_N exactly. Summing (1) and using L202's
order N³ box count proves the aggregate assertion; its upper bound
is simply #F_N. L203's interior-count inclusion puts these tuples
in L202's phase-selected population. L202 then supplies the occupied
full-core window and all safe-m restrictions for the indicated W.

## Qualifications and verification

This proves the geometric phase-selection target on the actual factor
box, rather than on an independent coefficient model. The unique window
integer is still m0=floor(sqrt(abcd))+1. Nothing here controls
its common divisors with ab or a positive lower threshold for phi(ab)/ab.
In particular the arithmetic counting criterion and RH remain unproved.
The overall argument in PROOF.md is unchanged.

Analytic verification checks the derivative identity, its positive lower
bound on the whole real slice, the two exponents in (4), the Fourier
normalization and tail, uniformity before summing slices, and L203's
interval inclusion. `python3 scripts/heat/check_factor_slice_phase.py`
rechecks the exact rational approximation inequalities used for that
inclusion. These finite checks do not substitute for the asymptotic
proof (2)-(6). Formalization would require the named derivative test,
periodic convolution and Fejér theorem, uniform finite-mode estimates,
and the unique indexing of integer tuples.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
