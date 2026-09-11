# Lemma 215: negligible positive mass in exterior endpoint caps

**Hypotheses.** Use the exact ordered weight W and ratio r of L213,
with all original integer factors in [N,2N], m in M_in, exact
lengths ell, and gcd(m,ab)=1. In particular h is comparable to
N^(3/2) and R=O(N^(3/2)). Let 0<=D<=N², for sufficiently
large real N. Constants below are independent of D.

**Conclusion.** Define the nonnegative endpoint-cap mass

E_cap^+(D)=Σ_(cd<=N²+D or cd>=4N²-D)
                 W(a,b,c,d,m) max(r(c/N)r(d/N),0).

Then

E_cap^+(D)<=C Rh(D+N)²/N⁴.                              (1)

For D_*=N^(7/4)/log N, this is o(Nh), with normalized bound
O((log N)^(-2)+N^(-3/2)). Both caps lie in
|cd-2N²|>B_*=N^(15/8)/log N eventually. Thus they remove
one precisely scoped part of the remaining far exterior.

**Proof.**

If c,d>=N and cd<=N²+D, then cN<=cd and dN<=cd,
so both factors lie in [N,N+D/N]. If c,d<=2N and
cd>=4N²-D, then 2Nc>=cd and 2Nd>=cd, so both factors
lie in [2N-D/(2N),2N]. These are valid for real N and D;
intersecting with the original integer support preserves them.
An interval of length t has at most t+1 integers. The number of
ordered pairs in the union of the caps is therefore at most

(D/N+1)²+(D/(2N)+1)²<=2(D/N+1)².                       (2)

No sign restriction or assertion about divisor distribution is needed
for this upper bound.

For each fixed ordered pair c,d on the full original support, L213's
proof establishes uniformly

Σ_(a,b,m) W(a,b,c,d,m)<=C Rh/N².                        (3)

In detail, a positive exact length forces u=ab into its interval
J_v, v=cd, of length O(h). The aggregate weighted a,b count there
is O(h+N)=O(h). For each u,v, the exact coprime sum of
alpha_m ell is O(R), and phi(u)/u²<=N^(-2). The remaining
p(c/N)p(d/N) is bounded. These facts hold up to both product
endpoints; J_v is only an enlargement for the majorant. Neither
the defined lengths nor the defined coprime sums are replaced.

Since |r|<=1, multiply (3) by (2) to obtain (1). Dividing by
Nh and using R=O(N^(3/2)) yields

E_cap^+(D)/(Nh)<=C (D+N)²/N^(7/2).

At D=D_*, the inequality (x+y)²<=2x²+2y² gives the stated
normalized bound, tending to zero. In the lower cap the distance
from 2N² is at least N²-D_*; in the upper cap it is at least
2N²-D_*. Since D_*/N² tends to zero and B_*/N² tends
to zero, both distances exceed B_* eventually.

## Qualifications, verification, and formalization

This is an upper bound on a subset of the requested far exterior.
Combining it with L214 leaves the explicit region

N²+D_*<cd<4N²-D_*,  |cd-2N²|>B_*                       (4)

uncontrolled on the Nh scale. L214 is used only to describe this
comparison; (1) uses L213 alone. L212's negative-strip lower bound
cannot yet be compared with the mass on (4). No signed-total or RH
conclusion follows, and no assertion of sharpness is made.

Verification is analytic: both endpoint inequalities, integer counts
for real intervals, the uniform full-support estimate (3), finite
nonnegative restrictions, exponent arithmetic, and eventual cap
inclusion. No numerical inference is required. Formalization would
require these finite inequalities and the elementary logarithmic
limits, with constants uniform in D.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
