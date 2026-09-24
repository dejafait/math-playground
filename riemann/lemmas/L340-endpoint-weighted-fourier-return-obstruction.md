# Lemma 340: the weighted Fourier return certificate still loses the height scale

**Hypotheses.** Let y≥3, let p_1,…,p_d be all primes at most y,
and let m≥1 be an integer. Thus d≥2. For 0<ε<π put

g_m(θ)=∏_(j=1)^d [(1−cos θ_j)/2]^m,
q=cos²(ε/2),
c_m=binom(2m,m)/4^m,  b_m=c_m^d,
V_y=Σ_(j=1)^d (log p_j)².

The target is the open ε-box about (π,…,π) on the phase torus.
For k∈{−m,…,m}^d write

C_m(k)=∏_(j=1)^d binom(2m,m+k_j)/4^m,
ω_k=Σ_(j=1)^d k_j log p_j,
Λ_m=Σ_(k≠0) C_m(k)/|ω_k|.                           (1)

All sums in this lemma are finite. Unique prime factorization gives
ω_k≠0 when k≠0. If b_m>q^m define the length threshold for the
coefficient-weighted absolute Fourier certificate by

H_m^abs=2Λ_m/(b_m−q^m).                             (2)

For the endpoint application use y=exp(6sqrt(r)) and ε=1/10 as in
L339, with r tending to infinity through positive real values.

**Conclusion.** The exact coefficient weights satisfy

Λ_m≥(1−b_m)^(3/2)/sqrt(mV_y/2).                     (3)

For every degree with b_m>q^m, uniformly in m,

H_m^abs≥(3m+1)^(d/2)/(sqrt(md)log y)
                         ≥2^d/(sqrt(d)log y).        (4)

Consequently, at L339's cutoff there is an absolute c>0 such that

log H_m^abs≥c exp(6sqrt(r))/sqrt(r)                   (5)

for all sufficiently large r, uniformly over all such degrees.
In particular H_m^abs/exp(2r)→∞ uniformly. If b_m≤q^m, this
constant-term comparison supplies no return certificate at any length.

Thus retaining every Fourier coefficient weight, and even evaluating
every reciprocal frequency exactly, cannot make this particular
absolute-error certificate prove a phase-box visit on length exp(2r).
The same holds on any length with logarithm 2r+O(1), including the
endpoint scale a_n=sqrt(4π²exp(4r)−25), r=2n.

This is a lower bound on a sufficient-length certificate, not a lower
bound on actual first-return times or on the actual Fourier discrepancy.
Cancellation between integrated Fourier modes is not estimated. No
claim is made that a particular interval lacks a visit. L339's negative
arithmetic consequence of a visit remains valid, but no visit is placed
at or near a_n and no Laguerre sign or zero-exclusion range changes.

**Proof.** L336's finite Fourier coefficient identity gives

ĝ_m(k)=(−1)^(Σ_j k_j)C_m(k),
Σ_k C_m(k)=1,  C_m(0)=b_m.                           (6)

The frequency map is injective: if ω_k=ω_l, exponentiating and
separating positive and negative prime exponents gives two equal
positive integers; unique prime factorization yields k=l. In
particular the only zero frequency in (6) is the zero vector, so
no coincident frequencies have been discarded before taking moduli.

For a single coordinate, the probabilities
binom(2m,m+k)/4^m are those of K=B−m, where B is the sum of
2m independent variables taking 0 and 1 with equal probability.
Each summand has mean 1/2 and variance 1/4. Independence therefore
gives E K=0 and E K²=m/2. The product in (6) makes the coordinates
independent. Expanding the square, with every cross term zero, gives
the exact frequency moment

Σ_k C_m(k)ω_k²=(m/2)V_y.                            (7)

These assertions can equivalently be obtained by twice differentiating
the finite Laurent polynomial ((2+z+z^(−1))/4)^m at z=1.
No distributional assumption on the actual prime-phase orbit is used.

Put P=1−b_m and J=Σ_(k≠0)C_m(k)|ω_k|. Both numbers are positive.
Two finite Cauchy–Schwarz inequalities give

P²≤Λ_m J,
J²≤P Σ_(k≠0)C_m(k)ω_k²=P mV_y/2.

Eliminating J proves (3). This estimate needs neither a small
frequency nor a worst-frequency Diophantine bound.

For a translated interval [t_0,t_0+H], direct integration gives

|(1/H)∫_(t_0)^(t_0+H)exp(−itω_k)dt|
                                      ≤2/(H|ω_k|).

Applying this to the exact finite Fourier expansion proves

|(1/H)∫_(t_0)^(t_0+H)g_m(−t log p_1,…,−t log p_d)dt−b_m|
                                      ≤2Λ_m/H.      (8)

Outside the target box at least one factor in g_m is at most q^m,
and all others are at most one. Its maximum there is exactly q^m,
attained by setting one coordinate on the boundary and the rest to π.
Thus (8) certifies a visit by the comparison

b_m−2Λ_m/H>q^m,                                    (9)

which requires b_m>q^m and H>H_m^abs. The statement that this
certificate fails means precisely that (9) fails. It does not replace
the actual average by the error bound in (8).

We next control the loss from b_m uniformly over the degree. The
central binomial recurrence is

c_0=1,  c_(m+1)/c_m=(2m+1)/(2m+2).

It implies c_m≤1/2 for m≥1, and also

c_m²≤1/(3m+1)  for every integer m≥0.               (10)

For (10), the assertion at zero is equality. The induction step is
the exact algebraic inequality

4(m+1)²(3m+1)−(2m+1)²(3m+4)=m≥0.

Consequently b_m≤(3m+1)^(−d/2) and P≥1/2. Using (3),
V_y≤d(log y)², and 0<b_m−q^m<b_m, we obtain

H_m^abs≥2Λ_m/b_m
 ≥2(1/2)^(3/2)/(b_m sqrt(mV_y/2))
 =1/(b_m sqrt(mV_y))
 ≥(3m+1)^(d/2)/(sqrt(md)log y).                     (11)

For real m≥1, the logarithmic derivative of
(3m+1)^(d/2)/sqrt(m) is

[3(d−1)m−1]/[2m(3m+1)]>0  when d≥2.

Its minimum on that range is its value 2^d at m=1. This proves
(4) simultaneously for every integer degree, even when the degree
varies arbitrarily with r. No optimization assumption about
the separating degree is needed.

For completeness, an elementary prime-count bound suffices to compare
(4) with the height scale. If N≥1 is an integer, the binomial theorem
and maximality of the central coefficient give

4^N/(2N+1)≤binom(2N,N).

For a prime p, the exponent of p in this integer is

Σ_(j≥1)[floor(2N/p^j)−2floor(N/p^j)].

Each summand is either zero or one and vanishes once p^j>2N.
Hence the total contribution p raised to this exponent is at most
2N. Unique factorization now bounds

binom(2N,N)≤(2N)^(π(2N)),
π(2N)≥[2N log 2−log(2N+1)]/log(2N).                (12)

For y≥16 take N=floor(y/2). Since y−2≤2N≤y, (12) implies

d=π(y)≥(log 2)y/(2log y).                          (13)

Indeed (y−2)log 2−log(y+1)≥y(log 2)/2 on y≥16:
the difference at 16 is log(64/17)>0, and its derivative is
(log 2)/2−1/(y+1)>0. Here log 2>1/2 follows by integrating
1/x on [1,2]. All denominators in this use of (12) are positive.

Taking logarithms in (4), using (13) and d≤y, gives

log H_m^abs
 ≥d log 2−(1/2)log d−log log y
 ≥(log 2)²y/(2log y)−(1/2)log y−log log y
 ≥(log 2)²y/(4log y)                                (14)

for sufficiently large y, independently of m. Substituting
log y=6sqrt(r) proves (5), for example with c=(log 2)²/24
and an unspecified sufficiently large starting r.
Since exp(6sqrt(r))/r^(3/2)→∞, this exceeds log(exp(2r))=2r
by a diverging factor. On r=2n, log a_n=2r+log(2π)+o(1), so
the same comparison applies to the coupled height scale.

L339 proves the negative margin for every assignment in the closed
box with this cutoff and tolerance; the open box considered here
is contained in it. Our failure to certify such a visit supplies no
new arithmetic sign. The obstruction is the small constant term
relative to a positive frequency moment, and remains after the old
shrinking-width and worst-frequency estimates are removed. ∎

**Mathlib.** Full statement: not checked. Coverage of the finite
Fourier moment, reciprocal-frequency lower bound, central binomial
prime count and degree-uniform certificate obstruction is not
checked. No full matching theorem or absence from checked sources
is claimed. L336 supplies the finite Fourier coefficient identity,
and L339 supplies the conditional arithmetic consequence of a visit;
neither is itself a match for this obstruction. No new library or
external analytic theorem is imported. The proof of (12)–(13) is
included rather than assuming a prime-number-theorem estimate.

The finite coefficient moments, binomial inequalities and prime
valuations can be checked with
`python3 scripts/laguerre/check_endpoint_weighted_return.py`.
Those exact checks supplement the proof; they do not compute the
large-dimensional Λ_m or certify any actual return time.
