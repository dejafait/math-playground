# Lemma 336: an effective endpoint phase return bound and its scale loss

**Hypotheses.** Let r tend to infinity through real values. Use the
endpoint weights W_r, full sum S_r(a), interior sum T_r(a), and
Liouville function λ from L335, and put A=ζ(2)². Define

U=8 sqrt(r log r),  Y=exp(U),  ε=1/[64r(U+1)].

Let p_1,…,p_d be all primes at most Y and P=∏_(j=1)^d p_j. Put

X=64d ε^(−2),  M=ceil(X log X),
β=(2M+1)^(−d),  H_r=8P^M(2M+1)^d.                    (1)

These are finite explicit quantities. All assertions below concern
sufficiently large r; L335's eventual negative asymptotic is an input,
and no numerical starting r is asserted.

**Conclusion.** The product cutoff log(jk)≤U discards absolute mass
at most

B_r=2(1+U²+8r)exp(−U²/(8r))=O(r^(−7)log r)=o(1/r).    (2)

If every −a log p_j has circular distance less than ε from π, then

S_r(a)<−A/(16r),  T_r(a)<−A/(16r).                    (3)

Every translated interval [b,b+H_r], b≥0, contains a height satisfying
(3). However this explicit sufficient waiting length obeys

log H_r≥c r³(log r)²,
log log H_r≤16 sqrt(r log r)+O(log r)                  (4)

for an absolute c>0. In particular H_r/a_n→∞ on r=2n, where
a_n=sqrt(4π²exp(4r)−25). This return certificate does not even locate
a negative value in [a_n,2a_n], let alone at the prescribed a_n.

The same scale failure holds for the product bump below at any degree
that separates its outside-box bound from its constant term,
if its Fourier integration error is bounded using the same worst
frequency estimate P^(−M). This is a restriction of that certificate,
not a lower bound on the actual first return or a prohibition on better
arithmetic estimates. No Laguerre sign, zero-exclusion range, or RH
conclusion changes.

**Proof.** Write t=log(jk). L297's elementary logarithmic inequality
gives

0≤W_r(j,k)≤(jk)^(−1)exp(−t²/(8r)).                    (5)

For t≥0 the cumulative harmonic pair mass satisfies

F(t):=Σ_(log(jk)≤t)1/(jk)
 ≤[Σ_(j≤exp(t))1/j]²≤(1+t)².                         (6)

The last inequality is decreasing integral comparison. Stieltjes
integration by parts, with F(U) including any atom at U, yields

Σ_(log(jk)>U) (jk)^(−1)exp(−log²(jk)/(8r))
 =−F(U)exp(−U²/(8r))
   +∫_U^∞ F(t)[t/(4r)]exp(−t²/(8r))dt
 ≤2∫_U^∞(1+t²)[t/(4r)]exp(−t²/(8r))dt
 =2(1+U²+8r)exp(−U²/(8r)).                           (7)

The boundary term at infinity vanishes by (6). Equations (5)–(7)
prove (2), for arbitrary phases as well as the untwisted weights.
In particular B_r<1/(128r) for large r. Also U<3r/4 eventually, so
every retained pair lies in the interior set J_r² as well.

We make the phase neighborhood quantitative without a first-order
loss. Suppose each prime phase is π+η_j modulo 2π, |η_j|<ε.
For any retained integer m write

ω(m)=λ(m)exp(iE_m),  E_m=Σ_j v_(p_j)(m)η_j.

Since Ω(jk)≤log(jk)/log 2, one has
|E_j−E_k|≤εU/log 2. Pairing j,k with k,j makes the retained sums
real. Their difference from the Liouville value is consequently
bounded, using 1−cos x≤x²/2, by

(ε²U²/[2(log 2)²]) Σ_(log(jk)≤U) W_r(j,k).             (8)

L297's proof bounds the full mass by 4r+2sqrt(2πr)+1≤11r for r≥1.
Here π<4 suffices. Since log 2>1/2, (8) is less than

22r ε²U²<22/(4096r)<1/(128r).                         (9)

For either S_r or T_r, its own twisted tail and the Liouville tail
each cost at most B_r. Thus its difference from its Liouville value
is less than 3/(128r). L335 gives both Liouville values at most
−A/(8r) for large r. Since A>1 and 3/128<1/16, this proves (3).
This argument respects every multiplicative relation and retains all
equal-ratio collisions.

Next quantify the recurrence. On the d-dimensional phase torus put

g_M(θ)=∏_(j=1)^d [(1−cos θ_j)/2]^M,
q=cos²(ε/2).

Outside the open ε-box about (π,…,π), g_M≤q^M. Its constant Fourier
coefficient is

b_M=[binom(2M,M)/4^M]^d≥(2M+1)^(−d)=β.               (10)

Indeed each one-dimensional Fourier coefficient at k, |k|≤M, is
(−1)^k binom(2M,M+k)/4^M. Its coefficients' absolute sum is one,
as is that of their d-fold product. Formula (10) and the lower bound
follow from the binomial theorem and maximality of the central term.

For 0≤x<π/2, integrating tan x≥x gives log cos x≤−x²/2.
Therefore q^M≤exp(−Mε²/4). For the choice (1), X≥64,
M≥X log X and M≤2X log X. Also 5 log X≤X for X≥64, by
differentiation and the inequality at 64. Hence

log(2M+1)≤2 log X,
Mε²/4≥16d log X≥d log(2M+1)+log 4.

We have proved

q^M≤β/4.                                             (11)

For any nonzero integer vector k in this polynomial's Fourier
support, |k_j|≤M. Unique prime factorization gives

ω_k:=Σ_j k_j log p_j=log(u/v)≠0,
u=∏_(k_j>0)p_j^(k_j),  v=∏_(k_j<0)p_j^(−k_j).

Both positive integers are at most P^M. If u>v, integration of 1/x
on [v,u] gives log(u/v)≥(u−v)/u≥P^(−M); the other case is the
same after interchanging u,v. Thus

|ω_k|≥P^(−M).                                        (12)

For any real b and T>0, direct integration gives

|(1/T)∫_b^(b+T)exp(−iaω_k)da|≤2/(T|ω_k|).

The Fourier coefficient absolute sum is one. Summing this finite
identity and using (12) bounds the discrepancy of the average of
g_M(−a log p_1,…,−a log p_d) from b_M by 2P^M/T,
uniformly in b. At T=H_r this is β/4. Its average is therefore at
least 3β/4, whereas an orbit staying outside the box would have
average at most q^M≤β/4 by (11). A visit occurs in every such
interval, and (3) proves the asserted negative values. All averages
here are finite Fourier sums; no limiting equidistribution theorem
or uniform Diophantine hypothesis has been imported.

For the scale comparison, d≤Y and log P≤dU. Since
ε^(−2)=4096r²(U+1)², one has

log X≤U+O(log r),  X≤C exp(U)r²(U+1)²,
log(2M+1)≤2 log X.

It follows from (1) that

log H_r=log 8+M log P+d log(2M+1)
 ≤exp(2U+O(log r)).                                   (13)

This proves the upper assertion in (4). For the lower assertion,
d≥1 and P≥2 give

log H_r≥M log 2≥64ε^(−2)log(64ε^(−2))log 2
                 ≥c r³(log r)²,                      (14)

since U²=64r log r. By contrast log a_n=2r+log(2π)+o(1).
Thus the particular sufficient length H_r is asymptotically much
larger than a_n. Equation (14) bounds this certificate, not the
actual waiting time from below; the latter may be far shorter.

Finally this loss is not removed merely by optimizing M within the
same worst-frequency calculation. Write m for an arbitrary bump
degree and b_m for its constant term. The one-dimensional central
coefficient starts at 1/2 when m=1 and decreases: the ratio of
successive values is (2m+1)/(2m+2)<1. Thus b_m≤1/2 for d≥1.
Any separation q^m<b_m implies q^m<1/2, whence

m≥log 2/(−log q).

For 0<ε≤1, tan x≤2x on 0≤x≤1/2: indeed sin x≤x and
cos x≥1−x²/2≥7/8. Integrating gives
−log q=2∫_0^(ε/2)tan x dx≤ε²/2. Hence

m≥2(log 2)ε^(−2).                                    (15)

To obtain an average greater than q^m using the discrepancy bound
2P^m/T alone requires T>2P^m/(b_m−q^m)≥2P^m/b_m≥4·2^m.
Equations (15) and the definition of
ε force log T≥c ε^(−2)≥c r³log r, still exceeding 2r.
This last statement concerns that chosen upper-error calculation
and the specified phase box. Sharper weighted-frequency estimates,
a different sufficient neighborhood, or actual earlier returns are
not ruled out. None would itself supply the separately missing
transfer to the coupled theta coefficients. ∎

**Mathlib.** Full statement: not checked. Coverage of the harmonic
tail bound, quantitative phase neighborhood, finite Fourier return
estimate and certificate-scale comparison is not checked; all are
proved above. The Liouville asymptotic is supplied by L335. Its
supporting nonvanishing input was recorded as present in L001:
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
That source was not rechecked here, and its theorem is supporting
coverage for L335, not a match for this statement. No full match or
absence from checked sources is claimed.
