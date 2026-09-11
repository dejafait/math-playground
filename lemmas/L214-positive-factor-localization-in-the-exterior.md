# Lemma 214: positive-factor localization in the exterior

**Hypotheses.** Use the exact ordered mass, fixed K>0, scales and
profiles of L213. Put L=N^(3/2). All defined sums retain the exact
integer displacement lengths, m in M_in and gcd(m,ab)=1.
Let KL<=B<=N², with constants independent of B and sufficiently
large real N.

**Conclusion.** The exterior positive mass with
KL<|cd-2N²|<=B obeys the improved estimate

E_out^+(B) <= C Rh B²(B+N)²/N⁸.                         (1)

For B>=L this is O(B⁴/N⁵). Consequently it is o(Nh) for any
B=o(N^(15/8)) in the stated range. In particular, with
B_*=N^(15/8)/log N, the portion of the previously remaining far
exterior N^(7/4)<|cd-2N²|<=B_* is o(Nh).
The portion |cd-2N²|>B_* remains uncontrolled on the Nh scale.

**Proof.**

Set s=sqrt(2)N. By L195, a strictly positive ratio product requires
both c,d>s or both c,d<s. If both exceed s and cd<=s²+B,
then cs<cd<=s²+B and ds<cd<=s²+B. Hence

s<c,d<s+B/s.

If both are below s and cd>=s²-B, then cs>cd>=s²-B and
ds>cd>=s²-B. Hence

s-B/s<c,d<s.

Factors equal to s give zero ratio product and can be omitted.
An interval of length B/s contains at most B/s+1 integers, so
there are at most 2(B/s+1)² positive ordered pairs in the band.
Intersecting with the original factor support only decreases this
count. This uses no assertion about the distribution of products.

For each fixed ordered pair c,d, put v=cd. The proof of L213,
before summing in c,d, gives the uniform bound

sum_(a,b,m) W(a,b,c,d,m) <= C Rh/N².                    (2)

Indeed its exact nonempty cells force u=ab into J_v of length O(h).
The sum of P_p(u) over that interval is O(h), the exact coprime
m sum of alpha_m ell is O(R), and phi(u)/u²<=N^(-2).
The remaining factor p(c/N)p(d/N) is uniformly bounded.
All terms are nonnegative; enlargements occur only in this upper
bound, not in the defined mass. Thus (2) is also valid for each
pair selected by its sign or product band.

L213's hyperbolic estimate, derived from L195, gives uniformly
for |cd-2N²|<=B<=N²

max(r(c/N)r(d/N),0)<=C B²/N⁴.                           (3)

Multiplying (2), (3), and the ordered-pair count proves (1).
Discarding |cd-2N²|<=KL only decreases the nonnegative sum.
For B>=L, B+N<=2B eventually and Rh=O(N³), proving
E_out^+(B)=O(B⁴/N⁵). Since Nh is comparable to N^(5/2),

E_out^+(B)/(Nh)=O(B⁴/N^(15/2)).                         (4)

The claimed little-o statement follows with uniform constants.
For B_*, (4) is O((log N)^(-4)), and B_*/N^(7/4)
=N^(1/8)/log N tends to infinity. Thus the specified far-exterior
annulus is eventually nonempty as a real band and is bounded by
E_out^+(B_*), proving its asserted negligibility.

## Qualifications, verification, and formalization

This is one scoped part of the far-exterior comparison. It does not
bound the full positive mass by o(Nh), prove actual cancellation,
or decide the signed total or RH. L212 is comparison only, not an
input. The gain over L213 comes from counting only same-side ordered
factor pairs before taking their weight, without replacing exact
cell lengths or coprimality by density.

Verification is analytic: both sign cases, integer interval counts,
the uniform fixed-pair estimate, nonnegative restriction, and exponent
arithmetic in (4). No numerical or distribution claim is required.
Formalization would require these finite inequalities, uniformity in
the moving band B, and the elementary logarithmic limit for B_*.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
