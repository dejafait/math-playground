# Lemma 351: a local dilation average for the endpoint weighted Gram matrix

**Hypotheses.** Use L349's real coefficients b_r^w and L350's
nonconstant reduced-pair set F, maximum weights, and samples:

F={(p,q): gcd(p,q)=1, p≠q},  ω_(p,q)=log(q/p),
I_N={N,…,2N−1},  a_n=sqrt(4π²exp(8n)−25),
w_N(ν)=max_(n∈I_N)|b_(2n)^w(ν)|,  W_N=Σ_(ν∈F)w_N(ν).

Omit zero weights. N is an integer tending to infinity. Define

K_N(t)=Σ_(ν∈F)w_N(ν)exp(itω_ν),
G_N^θ(n,m)=K_N(θ(a_n−a_m)),
H_N(θ)=Σ_(n,m∈I_N)|G_N^θ(n,m)|²/(N W_N)²,
ρ_N(θ)=||G_N^θ||op/(N W_N),
B_N=Σ_(ν∈F)w_N(ν)².

Thus H_N(1) and ρ_N(1) are exactly L350's diagnostics; θ is
an auxiliary common dilation, and the weights do not depend on θ.
Retain L349's nonnegative sequence γ, given by
γ(1,m)=γ(m,1)=Λ(m)/m for m≥2 and zero otherwise, and
C_w=||γ||_2²=2Σ_(m≥2)Λ(m)²/m²>0.

**Conclusion.** The maximum weights satisfy

||w_N−γ/sqrt(2N)||_2=O(1/N),
B_N=C_w/(2N)+O(N^(-3/2)),
3≤liminf_(N→∞)W_N≤limsup_(N→∞)W_N<∞.                 (1)

Uniformly for A∈ℝ and T>0,

(1/T)∫_A^(A+T)H_N(θ)dθ
 =1/N+(1−1/N)B_N/W_N²
             +O(N^(13/2)exp(−4N)/T).                 (2)

In particular, for T≥N^8 exp(−4N),

(1/T)∫_A^(A+T)H_N(θ)dθ
 =1/N+(1−1/N)C_w/(2N W_N²)+O(N^(-3/2))
 =O(1/N).                                             (3)

All constants are independent of A and T. At every dilation,

ρ_N(θ)²≤H_N(θ)≤ρ_N(θ),
H_N(θ)≥max(1/N,B_N/W_N²).                             (4)

For the intervals in (3) and any η>0, Lebesgue measure satisfies

|{θ∈[A,A+T]: ρ_N(θ)>η}|/T≤C/(Nη²).                  (5)

Thus the collision diagonal has the required vanishing size, and
most dilations in every such interval have a small sampling norm.
Neither (2) nor (5) proves H_N(1)=o(1). The auxiliary samples
θa_n with θ≠1 do not satisfy the prescribed endpoint height-index
relation. No pointwise endpoint margin, Laguerre sign, additional
zero-exclusion range, or RH candidate follows.

**Proof.** We first control the maximum over n without summing N
separate square norms. L349 gives, for every reduced pair,

|b_r^w(p,q)−r^(-1/2)γ_(1+r^(-1/2))(p,q)|
 ≤(C/r)D_2(p,q),
D_2(p,q)=τ(p)τ(q)(1+log(pq))²/(pq),                   (6)

where D_2 is square summable on the reduced pairs. The sequence
γ_σ has the same axial support as γ and values Λ(m)/m^σ.
Define E=D_2+γ log(pq), with multiplication coordinatewise.
This is square summable: on each axis the extra squared sum is
Σ_(m≥2)Λ(m)²(log m)²/m²<∞, since Λ(m)≤log m.
The elementary inequality 1−exp(−x)≤x for x≥0 gives

|b_r^w(ν)−r^(-1/2)γ(ν)|≤(C/r)E(ν).                 (7)

For 2N≤r≤4N, the right side is at most C E(ν)/N and
r^(-1/2)≤(2N)^(-1/2). Since γ≥0, (7) implies

|b_r^w(ν)|≤γ(ν)/sqrt(2N)+C E(ν)/N.

Conversely, the sample r=2N is present in the maximum, so

w_N(ν)≥|b_(2N)^w(ν)|≥γ(ν)/sqrt(2N)−C E(ν)/N.

Consequently |w_N−γ/sqrt(2N)|≤C E/N coordinatewise.
Taking the square norm proves the first assertion of (1).
Expanding the squared norm and using Cauchy–Schwarz gives
B_N=C_w/(2N)+O(N^(-3/2)). L350 proves W_N=O(1),
and L349 gives W_N≥Σ_(ν∈F)|b_(2N)^w(ν)|≥3−o(1).
This proves the remaining assertions of (1). In particular W_N
is bounded below by a positive absolute constant for large N.

We next obtain an absolute inverse-frequency-gap budget. Put
σ_N=1+1/(2sqrt(N)). L349's divisor formula and
0≤f_r≤exp(2) give

|b_r^w(p,q)|
 ≤(exp(2)+1)Σ_(d≥1)τ(dp)τ(dq)/(d²pq)^(1+r^(-1/2)).

For positive integers d,p, one has τ(dp)≤τ(d)τ(p), by
checking each prime exponent. L349 establishes convergence of
Σ_d τ(d)²/d². Since 1+r^(-1/2)≥σ_N for 2N≤r<4N,
the same pointwise bound applies uniformly before taking the
maximum:

w_N(p,q)≤C τ(p)τ(q)/(pq)^σ_N.                        (8)

Extend w_N by zero to all positive integer pairs outside F.
In the absolutely convergent product |K_N(t)|² group the pairs
(p,q),(u,v) by k=qu, l=pv, and set

c_N(k,l)=Σ_(q|k,p|l)w_N(p,q)w_N(k/q,l/p).

These coefficients are nonnegative and retain every collision.
Since τ*τ=d_4, where d_j counts ordered j-factorizations, (8)
implies

|K_N(t)|²=Σ_(k,l≥1)c_N(k,l)exp(it log(k/l)),
c_N(k,l)≤C² d_4(k)d_4(l)/(kl)^σ_N.                   (9)

Absolute convergence follows either from W_N²<∞ or from the
right side, whose sum is C²ζ(σ_N)^8<∞. Moreover

Σ_(k≥1)c_N(k,k)=B_N.                                 (10)

Indeed k=l is equivalent to q/p=v/u. Both nonzero factors have
coprime coordinate pairs, so uniqueness of reduced fractions
forces (p,q)=(u,v). Conversely every such pair contributes once.
No unequal reduced frequencies remain in (10).

We claim that

Q_N:=Σ_(k≠l)c_N(k,l)/|log(k/l)|≤C N^(17/2).           (11)

Here is the specific use of L333's positive harmonic-sum estimate.
For σ>1, set x_k=d_4(k)k^(-σ). Split the ordered pairs into
max(k,l)≥2min(k,l) and their complement. On the first set the
denominator is at least log 2. On k<l<2k, use
log(l/k)≥(l−k)/(2k) and 2x_kx_l≤x_k²+x_l², and sum
the two harmonic sums with one index fixed. Including reversed
pairs gives

Σ_(k≠l)x_kx_l/|log(k/l)|
 ≤C[ζ(σ)^8+Σ_k d_4(k)² log(2k)/k^(2σ−1)].            (12)

L333 proves d_4(k)²≤d_16(k) by the surjection from nonnegative
4×4 integer matrices to their row and column totals, first at
prime powers and then by multiplicativity. For u>0, ordered
factor counting and the integral test give

ζ(1+u)≤1+1/u,
Σ_k d_16(k)log(2k)/k^(1+u)
 ≤(log 2)ζ(1+u)^16
   +16ζ(1+u)^15[u^(-2)+(log 2)/u].                   (13)

These are precisely the convergent positive sums used in L333;
they do not require the old normalization r^(-1). Substitute
σ=σ_N into (12), so u=2σ_N−2=N^(-1/2) in (13).
The first term of (12) is O(N^4), and (13) is O(N^(17/2)).
Equations (9) and (12) therefore prove (11). This bound handles
arbitrarily close nonzero log-rational frequencies; no positive
minimum spacing for their infinite set has been assumed.

For distinct sample indices n,m write Δ_nm=a_n−a_m. Direct
integration of each nonconstant exponential in (9), using
|exp(ix)−exp(iy)|≤2, now yields

|(1/T)∫_A^(A+T)|K_N(θΔ_nm)|²dθ−B_N|
 ≤2Q_N/(T|Δ_nm|).                                    (14)

The integrated series is justified by absolute convergence in
(9); the resulting sum of absolute integral bounds is finite
by (11). The bound is uniform in A and uses actual sample gaps.

Those gaps have a useful summable reciprocal. Write b_j=2πexp(4j)
and f(x)=sqrt(x²−25) for x>5. Then f'(x)>1, so for m>n≥N≥2,

a_m−a_n=f(b_m)−f(b_n)≥b_m−b_n
 ≥2π(1−exp(−4))exp(4m).

It follows that

Σ_(n,m∈I_N,n≠m)|Δ_nm|^(-1)
 ≤CΣ_(m=N+1)^(2N−1)(m−N)exp(−4m)
 ≤C exp(−4N).                                        (15)

The last constant is finite by the geometric-series identity
Σ_(j≥1)j exp(−4j)=exp(−4)/(1−exp(−4))².
No equidistribution conclusion is inferred from these gaps.

In the definition of H_N, the N terms n=m equal W_N²
exactly. Apply (14) to the remaining N(N−1) terms and then
use (11), (15), and the lower bound on W_N. Their normalized
total error is at most

2Q_N/(T N² W_N²)·Σ_(n≠m)|Δ_nm|^(-1)
 =O(N^(13/2)exp(−4N)/T).

This proves (2). Substitution of (1) proves (3), including the
displayed sufficient interval length; its exponent eight is not
claimed optimal.

For completeness, G_N^θ is positive semidefinite, since it is the
sum of the rank-one matrices w_N(ν)z_ν z_ν*, with
z_ν(n)=exp(iθa_nω_ν). The normalized eigenvalues are nonnegative
and sum to one. Their maximum is ρ_N(θ) and their sum of
squares is H_N(θ), proving the first inequalities in (4) and
H_N(θ)≥1/N. An exact frequency-side identity gives the other
lower bound and isolates the remaining deterministic question:

H_N(θ)=Σ_(ν,μ∈F) [w_N(ν)w_N(μ)/W_N²]
        ·|(1/N)Σ_(n∈I_N)exp(iθa_n(ω_ν−ω_μ))|².       (16)

Expand the squared modulus in the sample indices; exchanging
the finite sample sum with the absolutely convergent frequency
sum recovers the definition of H_N. Every term of (16) is
nonnegative, and ν=μ contributes B_N/W_N² exactly. This
proves (4). If ρ_N(θ)>η, then H_N(θ)>η², so integration
and (3) prove (5) by Markov's inequality.

To state precisely what (16) still leaves open, let

C_N(x)=(1/N)Σ_(n∈I_N)exp(ia_n x),
M_N(ε)=Σ_(ν≠μ, |C_N(ω_ν−ω_μ)|>ε)
                    w_N(ν)w_N(μ)/W_N².

Splitting this nonnegative sum at any 0<ε<1 gives

H_N(1)≤B_N/W_N²+ε²+M_N(ε),
ε²M_N(ε)≤H_N(1).                                    (17)

For example, M_N(N^(-1/8))=o(1) would suffice for the actual
sampling target. That bound is not proved here, nor is it asserted
necessary at this particular shrinking threshold. It requires
control of the weighted frequency pairs at θ=1, which is not
provided by a Lebesgue-measure estimate in θ.

Even taking [A,A+T]=[1,1+N^8 exp(−4N)] in (3) cannot
exclude its endpoint 1 from the exceptional set. The failure of
a general pointwise deduction is visible within this family:
H_N(0)=1 for every N, whereas (3) also holds uniformly on
intervals containing zero. Continuity does not supply a uniform
modulus on the shrinking interval scale. This observation is not
a counterexample at θ=1 and does not refute H_N(1)=o(1).

Finally L350's bounded vector budget makes ρ_N(1)=o(1)
sufficient for a vanishing discrete relative mean, but even that
would leave exceptional prescribed indices. The endpoint assembly
needs a positive S_(2n)(a_n) margin dominating
(1+2n)²exp(−2n/256). A pointwise relative error at most a
fixed η<1 would supply a polynomial margin by L349; no estimate
here gives that pointwise hypothesis. All the later gaps remain. ∎

Finite algebra verification: run
`python3 scripts/laguerre/check_endpoint_gram_collisions.py`.
It checks 24 exact collision, Gram/correlation and constant-term
identities with formal prime-log frequencies, including six
repeated-sample cases that check the number of sample-diagonal
terms. It does not evaluate a_n or certify the infinite estimates.

**Mathlib.** Full statement: not checked. Coverage of the
maximum-weight square-norm asymptotic, collision-complete local
Gram average, inverse-frequency-gap estimate, and exceptional-
dilation statement is not checked; their proofs are above.
L349–L350 retain as present the supporting results
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re),
and [`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These inherited links were not rechecked. They support the
reciprocal and Euler expansions underlying b_r^w, not the full
statement here. No full library match or absence from checked
sources is asserted.
