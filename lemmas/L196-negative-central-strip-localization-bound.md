# Lemma 196: negative central-strip localization bound

**Hypotheses.** Use the exact ordered weights, intervals, interior m set,
and central strip of L195, with fixed K>0. Thus h is comparable to
N^(3/2), R=O(N^(3/2)), m is comparable to N², and all four ordered
factors lie in [N,2N] intersected with the integers. Take N sufficiently
large in terms of the fixed scale constants and K.

**Conclusion.** Set V=2N² and T=K N^(3/2). Every contributing product
u=ab in the central strip belongs to the real interval

I_m=[(m²-R)/(V+T+1), (m²+R)/(V-T)].                       (1)

Uniformly in m, this interval has length O_K(N^(3/2)). For every
epsilon>0 the negative ordered-pair mass satisfies

0 <= Y_mid^- <= O_(K,epsilon)(h N^(1+epsilon)).            (2)

The same upper bound holds for the sum of all nonnegative weights W
in this strip. This improves the unrestricted absolute bound by a
factor N^(1/2), but does **not** establish Y_mid^-=o(Nh).

**Proof.**

For any nonempty exact integer interval [b,t] choose an integer r
in it. The endpoints in L191 imply |r|<=R and

uv<=m²+r<=u(v+1)-1.

Consequently uv<=m²+R and u(v+1)>=m²-R+1. In the central
strip V-T<=v<=V+T. All quantities being divided by are positive
for sufficiently large N, as is m²-R. Weakening the last inequality
by 1 gives (1). This implication also holds for singleton intervals;
their weight ell=t-b is zero, so they cause no exception.

Writing A=m², the length in (1) equals

[A(2T+1)+R(2V+1)]/[(V-T)(V+T+1)].                        (3)

Here A=O(N⁴), V is comparable to N², T=K N^(3/2), and
R=O(N^(3/2)). The denominator is comparable to N⁴, while the
numerator is O_K(N^(11/2)). Thus the length is O_K(N^(3/2)),
and I_m contains O_K(N^(3/2)) integers. Intersecting with the
original product support only reduces this count.

Define P_p(u) as the sum of p(a/N)p(b/N) over the original ordered
factor pairs ab=u. The bounded positive profile and the elementary
divisor estimate used in L193 give, for every eta>0,
P_p(u)=O_eta(N^eta) uniformly for N²<=u<=4N². This bound holds
for both products u and v. For fixed u,m at most two cells v have
nonempty exact intervals: the integers m²+r range over an interval
of diameter at most 2R<u, and floor division by u can therefore
produce at most two adjacent values. Additional cutoffs only remove
values. This also proves the count directly at strict floor endpoints.

Group the nonnegative ordered weights W by u,v. Retaining all original
restrictions, their strip sum for fixed m is

alpha_m Σ_(u,v: |v-V|<=T, gcd(m,u)=1)
             P_p(u)P_p(v) phi(u)/u² ell(u,v,m).           (4)

The coefficient alpha_m is bounded and nonnegative by L194. Also
ell<=2R and phi(u)/u²<=1/u<=N^-2. In an upper bound for (4)
we may drop gcd(m,u)=1, without asserting anything about its density.
Using (1), the integer count following (3), at most two v per u,
and the two multiplicity bounds with eta=epsilon/2, gives

(4) <= C_(K,epsilon) N^(3/2) N^epsilon R N^-2
     = O_(K,epsilon)(N^(1+epsilon)).

There are O(h) values of m. Finally |r(x)|<=1 for the ratio
r=q/p in L195, since p=(b+d)/2 with b,d positive. Therefore
max(-r(c/N)r(d/N),0)<=1, so Y_mid^- is at most the full
nonnegative strip weight. Summing (4) proves (2). ∎

## Qualifications and verification

Coprimality and floor lengths remain exact in the definition of the
mass. Their removal or enlargement occurs only in its positive upper
bound. After division by Nh the bound is O_epsilon(N^epsilon),
which does not tend to zero; no lower bound or failure of decay is
proved either. In particular this result does not justify replacing
the coprimality condition by an average density, and it says nothing
new about the exterior signed mass or RH.

Verification is analytic: the strict integer-cell inequalities, the
exact rational difference (3), uniform divisor bounds with separately
chosen exponents, and finite nonnegative summation. Formalization
requires these inequalities, the interval integer count, the two-cell
count, and the grouped ordered-weight identity (4).

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
