# Lemma 162: triple-product diagonal bound

**Hypotheses.** Use the finite Gaussian window I, amplitudes A_n(t),
and T≤t≤2T of L156, with fixed 0<a<b and sufficiently large T.
Let W be the ordered sextuple mass defined in L161. At each t set

S=Σ_(n∈I) A_n²,
D2=Σ_k(Σ_(u,v∈I,uv=k) A_u A_v)²,
D3=Σ_k(Σ_(u,v,w∈I,uvw=k) A_u A_v A_w)².

**Conclusion.** Pointwise throughout this interval,

W=D3−3 S D2+2 S³,                                      (1)
0≤W≤D3≤C_(a,b)(1+log T)^8.                             (2)

For the C² cutoff and expectation of L161 this implies

|E_T[χ''(Q/M)W]/(2M²)|
 ≤ C_(a,b)||χ''||∞ (1+log T)^8 P_T(M<Q<2M)/M².          (3)

Here P_T denotes normalized Lebesgue measure on [T,2T]. This is an
upper bound only; it supplies neither logarithmic growth from below
nor a bound uniform in T for fixed M.

**Proof.**

First allow arbitrary nonnegative amplitudes on any finite set of
positive integers. Expand D3 as the mass of all ordered sextuples
(a,b,r,s,m,n) with arm=bsn, with weight A_a A_b A_r A_s A_m A_n.
Let E1, E2, E3 be the subsets with a=b, r=s, m=n respectively.
The mass of E1 is S D2: cancel a=b in the product equality, leaving
rm=sn. The same reasoning applies to E2 and E3. In E1∩E2 the
remaining equality forces m=n, so this intersection has mass S³.
Every other double intersection and the triple intersection also have
mass S³. Weighted inclusion–exclusion thus gives (1), including all
ordered multiplicities, even when several of the six indices coincide.
Nonnegativity and restriction of the summation domain give 0≤W≤D3.

Put N=sqrt(T/(2π)). L156 gives A_n≤C_(a,b)N^(−1/2).
For an integer j≥1 let d_j(k) count ordered j-tuples of positive
integers with product k. Since all indices are at most bN, with
X=(bN)³≥1 we have

D3≤C_(a,b)N^(−3) Σ_(k≤X)d_3(k)².                       (4)

We prove d_3(k)²≤d_9(k) elementarily. At a prime power p^e,
d_3(p^e)=binom(e+2,2). A pair of triples of nonnegative integers,
each totaling e, can be realized as the row and column sums of a
3-by-3 nonnegative integer matrix: fill the first available row and
column by the minimum of their remaining margins, subtract it, and
continue. At least one remaining margin becomes zero at each positive
allocation, so this terminates with the requested margins. There are
binom(e+8,8) such matrices in total. The map taking margins is
surjective, proving binom(e+2,2)²≤binom(e+8,8).
Unique prime factorization makes d_j multiplicative (distribute each
prime exponent independently among the ordered factors), proving the
asserted inequality for every k, including k=1.

Finally, counting nine ordered factors and fixing the first eight,

Σ_(k≤X)d_9(k)
 =Σ_(u1⋯u8≤X) floor(X/(u1⋯u8))
 ≤X (Σ_(1≤u≤X)1/u)^8
 ≤X(1+log X)^8.                                        (5)

The enlargement in the middle inequality includes all eight-tuples
with each coordinate at most X; all summands are nonnegative. The last
inequality follows by integral comparison of the harmonic sum.
Combining (4) and (5), N^(−3)X=b³ and log X=O_(a,b)(1+log T)
prove (2), uniformly in t. No infinite sum interchange is required.

The cutoff is constant outside [1,2] and C², hence χ'' vanishes
outside (1,2), including its endpoints. Taking absolute values and
using (2) on this transition event proves (3). ∎

## Scope, verification

The divisor estimate deliberately drops the restrictions on individual
factors after (4); no sharp logarithmic exponent is claimed. The
cutoff correlation and the other terms of L161 remain uncontrolled.
This result does not prove the fixed-cutoff tail target or RH.

The exact integer regression `python3 scripts/heat/check_triple_diagonal.py`
checks (1) by independently enumerating resonant sextuples, including
empty and small sets, repeated indices, zero weights and nontrivial
multiplicative coincidences. It also checks the local binomial inequality
for a finite range; its proof for all exponents is the surjection above.
L156 supplies the Gaussian window bound; L161 supplies W and
the retained cutoff expression. No numerical asymptotic is used.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
