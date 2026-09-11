# Lemma 168: blockwise cutoff covariance and the local moment gap

**Hypotheses.** Use W and Q from L166 for the window [N,2N],
N=sqrt(T/(2π)), and put L=log T. Fix M>0 and a C³ real cutoff χ,
zero on (−∞,1] and one on [2,∞). Set f(t)=χ''(Q(t)/M).
For 1≤H≤T let J=ceil(T/H), h=T/J, and partition [T,2T] into
J equal intervals B_j. Write E_j for normalized integration on B_j,
f_j=E_j f, W_j=E_j W, and bar W=E_T W. Constants may depend
on χ and the fixed window, but not on T,H,M unless indicated.

**Conclusion.** There is an exact decomposition

E_T[f(W−bar W)]
 = (1/J)Σ_j (W_j−bar W)f_j + R,
R=(1/J)Σ_j E_j[(W−W_j)(f−f_j)],                         (1)

with |R|≤C_χ H L⁴/T. In particular, if H L⁴/T→0, the actual
covariance is o(1) if and only if the block sum in (1) is o(1).

For D(t)=Σ_(N≤n≤2N) A_n(t)² with A_n as in L156, uniformly in j,

E_j Q = E_j D + O(sqrt(T)log T/h),   0≤D(t)≤C.           (2)

Consequently

|f_j|≤C_χ min(1, (1+sqrt(T)log T/h)/M).                 (3)

There is a nonempty range sqrt(T)log T≪H≪T/L⁴ where (2) has
vanishing error and R=o(1). Nevertheless (3) gives only
O_χ(L⁴ min(1,1/M)) for the block sum in that range. First-moment
information alone does not determine a signed cutoff average: for
every m>0 there are two nonnegative random variables of mean m with
different expectations of χ''(X/M). This is an information obstruction,
not a claim that the actual Q realizes either law.

**Proof.**

The identities E_j(W−W_j)=E_j(f−f_j)=0 give (1) by expanding
each block integral. L166 supplies W≤CL⁴ and |W'|≤CL⁴/T.
Thus sup_(B_j)|W−W_j|≤ChL⁴/T. Since |f−f_j|≤2||χ''||∞,
averaging proves the claimed remainder bound. The equivalence follows
by subtracting this o(1) remainder. Also H/2≤h≤H.

For (2), use the carrier-removed finite sum in L156,
Q=|Σ A_n(t)exp(i(t−π/2)log(n/N))|². Its coefficient bounds give
sup|A_m A_n|≤CT^(−1/2) and
∫_(B_j)|(A_m A_n)'|≤ChT^(−3/2)≤CT^(−1/2).
Integration by parts at both block endpoints bounds each off-diagonal
integral by CT^(−1/2)/|log(m/n)|. L156's elementary difference sum
is O(N²log(2N)). Dividing by h therefore yields
O(sqrt(T)log T/h). The diagonal is E_j D, and the pointwise bound
D≤C follows from O(N) terms of size O(T^(−1/2)). All sums are
finite, so no interchange or uniform infinite tail is involved.

Since χ'' vanishes outside (1,2),
|f_j|≤||χ''||∞ P_j(M<Q<2M)≤||χ''||∞ min(1,E_j Q/M).
This proves (3). For example H=T^(3/4) satisfies both scale conditions.
The bound |W_j−bar W|≤CL⁴ then proves the stated available bound
for the block sum; it is not a lower bound for that sum.

To verify the limitation of first-moment information, χ'' cannot vanish
identically on (1,2): otherwise χ would be affine there, and the zero
endpoint derivatives would force it to be constant, contradicting its
endpoint values. Choose x∈(M,2M) with k=χ''(x/M)≠0. For any m>0
choose R>max(2M,m,x). A law supported on {0,R} with probability m/R
at R has mean m and zero χ'' expectation. Choose

0<ε<min(m/x, (1−m/R)/(1−x/R)).

A second law assigns masses ε at x, (m−εx)/R at R, and
1−ε−(m−εx)/R at 0. The displayed inequalities ensure all masses
are nonnegative, with total one and mean m. Its χ'' expectation is
εk≠0. These laws even have finite support. Thus knowing the first
moment exactly, not just to the error in (2), does not specify the
nonlinear cutoff mean. No incompatibility with possible additional
arithmetic information about the actual Q is asserted. ∎

## Scope, verification, and formalization obligations

An adequate additional estimate would be, for some scalar c_T,
J^(−1)Σ_j |f_j−c_T|=o(L^(−4)); centering Σ(W_j−bar W)=0 would
then make (1) o(1). This is a sufficient condition only, and is unproved.
Weighted signed cancellation could suffice without this condition.
Neither local mean squares nor the two artificial laws settle the
actual block correlation, a tail theorem, or RH.

Verification is analytic: block endpoint normalization, centered-product
expansion, Gaussian derivative bound, both integration-by-parts boundary
terms, harmonic difference sum, Markov support restriction, and the
probability masses and expectations above. No numerical certificate is
needed. Formalization would require these finite-sum estimates and the
explicit two-law construction; it would leave the signed estimate open.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
