# Lemma 150: dyadic fourth moment with divisor loss

**Hypotheses.** Let S(t) be as in L149, and let T tend to infinity. Constants below are absolute; measure means Lebesgue measure.

**Conclusion.**

∫_T^(2T)|S(t)|⁴dt = O(T^(−2)log(2T)⁴).                    (1)

There are constants a,c>0 such that, for all sufficiently large T,

meas{t∈[T,2T]: |S(t)|≥a T^(−3/4)} ≥ c T/log(2T)⁴.         (2)

This does not establish a positive proportion, an eventual pointwise lower bound, or nonvanishing.

**Proof.**

Use L149's exact unit-phase removal, weights b_n(t), and envelope

b_n(t)≤B_n=C N^(−2)f(n/N),  N=sqrt(T/(2π)),
f(x)=min(x²,x^(−4)),  M=N².

The constant C is uniform for t∈[T,2T]. We can assume M≥2. The square of the phase-removed series has coefficients

a_k(t)=Σ_{mn=k}b_m(t)b_n(t)

and frequencies log k, with the fixed extra phase exp(−iπ log k/2). Because f(x)f(y)≤f(xy),

a_k(t)≤A_k:=C²N^(−4)d(k)f(k/M),                           (3)

where d(k) is the number of positive divisors. The inequality for f follows by taking logarithms: min(2u,−4u)+min(2v,−4v)≤min(2(u+v),−4(u+v)). Absolute uniform convergence of the original series on this interval, bounded by c₀Σn^(−2), justifies multiplication and termwise integration of its fourth power.

### Elementary divisor estimates

Let d_4(k) count ordered factorizations into four positive integers. Prime factorization gives d(k)²≤d_4(k), because for every integer e≥0,

(e+1)²≤(e+1)(e+2)(e+3)/6.

Indeed the difference after division by e+1 is e(e−1)/6≥0. Also, for X≥1,

Σ_{k≤X}d_4(k)≤X(Σ_{n≤X}1/n)³≤X(1+log X)³.               (4)

To see the first inequality, sum floor(X/(abc)) over abc≤X and then enlarge the three reciprocal sums independently.

Equations (4) and dyadic decomposition imply

Σ_k d(k)² f(k/M)² = O(M log(2M)³),                        (5)
Σ_k k d(k)² f(k/M)² log(2k) = O(M² log(2M)⁴).             (6)

Here are explicit tail controls. For k≤M, use f≤1, k≤M and log(2k)≤log(2M) in (4). On 2^j M<k≤2^(j+1)M, j≥0, f(k/M)²≤2^(−8j). The bounds in (4) then give summands bounded by a constant times M 2^(−7j)(log(2M)+j+1)³ for (5), and M²2^(−6j)(log(2M)+j+1)⁴ for (6). Both series converge with the stated orders. Thus all weighted sums used below include the infinite tails.

### Fourth-moment expansion

The diagonal k=l is at most

T Σ_k A_k² = O(T N^(−8)M log(2M)³)
 = O(T^(−2)log(2T)³).                                   (7)

For k≠l expand a_k(t)a_l(t) into individual products of four b weights. Each such product has logarithm equal to a constant minus a sum of four squares (log n−log N_t)². It is unimodal as a function of log N_t, and hence as a function of t. Its total variation is at most twice its supremum. Integration by parts, including both endpoints, bounds its oscillatory integral by four times its envelope product divided by |log(k/l)|. Summing the finitely many factorizations at fixed k,l gives

|∫_T^(2T)a_k(t)a_l(t)exp(it log(k/l))dt|
 ≤4 A_k A_l/|log(k/l)|.                                  (8)

This argument does not assume that a_k a_l is unimodal.

For l≥2k the denominator is at least log 2. The two-factor version of (4) gives Σ_{k≤X}d(k)≤X(1+log X). Applying this bound below M, and on successive dyadic intervals above M with f(k/M)≤2^(−4j), gives

Σ_k A_k=O(N^(−4)M log(2M))=O(N^(−2)log(2M)).

Consequently the far pairs contribute O(N^(−4)log(2M)²).

For k<l<2k, log(l/k)≥(l−k)/(2k). Applying 2 A_k A_l≤A_k²+A_l², their contribution is at most a constant times

Σ_{k<l<2k} k(A_k²+A_l²)/(l−k)
 ≤ C' Σ_k k A_k² log(2k).                                (9)

For the A_k² term, sum 1/(l−k) up to k. For the A_l² term fix l, note l/2<k<l and k≤l, and sum 1/(l−k) up to l. These are finite harmonic sums. By (6), (9) is O(N^(−8)M²log(2M)⁴)=O(T^(−2)log(2T)⁴). The reverse ordered pairs obey the same bounds. These estimates also prove absolute summability in (8), so the integrated expansion and bounds are legitimate. Together with (7) they prove (1).

### Measure consequence

Let K>0 be the constant in L149. For sufficiently large T its second moment is at least (K/2)T^(−1/2). Choose a²=K/4 and let E be the set in (2). On its complement, the integral of |S|² is at most a²T^(−1/2). Hence

(K/4)T^(−1/2)≤∫_E|S|²≤meas(E)^(1/2)(∫_T^(2T)|S|⁴)^(1/2).

Squaring and using (1) proves (2). ∎

## Scope, verification

The logarithmic loss prevents this argument from giving a fixed positive fraction of the interval. It does not prove that such a fraction is impossible: both the fourth-moment bound and the measure deduction may be nonsharp. No lower bound valid at every point follows from either moment.

Verification is analytic: the product envelope inequality, prime-power divisor inequality, summatory factorization bounds, convergent dyadic tails, variation of each individual product, harmonic sums with both indices fixed in turn, and Cauchy–Schwarz establish every estimate. No numerical evidence is required. The only previously proved mathematical input is L149, including its representation, envelope, and second moment.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
