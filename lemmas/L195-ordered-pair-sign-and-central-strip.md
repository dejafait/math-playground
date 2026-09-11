# Lemma 195: ordered-pair sign and central strip

**Hypotheses.** Use Y_N, M_in, alpha_m and the nonnegative integer
interval lengths ell(u,v,m) of L194, with the exact endpoints of L191.
Use the actual profiles p=(b+d)/2, q=(b-d)/2 of L179 and the ratio
d(x)/b(x)=x³/(2sqrt(2)) of L178. Fix K>0. All factor indices lie in
I=[N,2N] intersected with the integers. The inherited scales are
h comparable to N^(3/2), R=O(N^(3/2)).

**Conclusion.** Put r(x)=q(x)/p(x). For x,y in [1,2],

r(x)=-tanh((3/2)log(x/sqrt(2))),
r(x)r(y)=(cosh A-cosh D)/(cosh A+cosh D),                 (1)

where A=(3/2)log(xy/2), D=(3/2)log(x/y).
In particular the product is positive exactly when x,y are strictly
on the same side of sqrt(2), negative when they are on opposite sides,
and zero when either equals sqrt(2).

For ordered a,b,c,d in I define the nonnegative weight

W(a,b,c,d,m)=p(a/N)p(b/N)p(c/N)p(d/N)
             phi(ab)/(ab)² alpha_m ell(ab,cd,m).

Every sum below imposes m in M_in and gcd(m,ab)=1. Then exactly

Y_N=Σ W(a,b,c,d,m) r(c/N)r(d/N).                         (2)

Restrict to the central product strip |cd-2N²|<=K N^(3/2), and define
Y_mid^+=Σ W max(r(c/N)r(d/N),0) and
Y_mid^-=Σ W max(-r(c/N)r(d/N),0) there. For every epsilon>0,

0<=Y_mid^+ = O_(K,epsilon)(h N^(1/2+epsilon)) = o(Nh),    (3)

where the little-o uses epsilon<1/2. Thus, writing Y_out for the
exact signed sum outside this strip,

Y_N=Y_out-Y_mid^-+o(Nh).                                (4)

No decay or lower bound for Y_mid^- or Y_out is asserted.

**Proof.**

The profiles b,d are strictly positive and bounded on [1,2], by L178.
Consequently p is positive and bounded. Write z=(x/sqrt(2))³=d(x)/b(x).
Then r(x)=(1-z)/(1+z), which proves the first identity in (1).
For s=(3/2)log(x/sqrt(2)), t=(3/2)log(y/sqrt(2)), the elementary
identities 2sinh(s)sinh(t)=cosh(s+t)-cosh(s-t) and
2cosh(s)cosh(t)=cosh(s+t)+cosh(s-t) prove the second one.
The sign assertion also follows directly from the first formula.

Insert the two ordered-pair definitions of L186 into Y_N. Replace
q(c/N)q(d/N) by p(c/N)p(d/N)r(c/N)r(d/N). These are finite sums,
so rearrangement is exact and proves (2). The length, totient, and
coprimality factor are untouched. Positivity of alpha_m from L194
makes W nonnegative, including at stationary endpoints.

In the central strip, xy=cd/N² satisfies |xy-2|<=K N^(-1/2).
For all sufficiently large N, the mean value theorem for log gives
|A|<=C_K N^(-1/2). Since cosh D>=1 and the denominator in (1)
is at least 2,

max(r(x)r(y),0)<= (cosh A-1)/2 <= C_K N^(-1).             (5)

The last inequality follows from Taylor's theorem on a fixed compact
interval. It holds even when the product on the left is negative
before taking the positive part.

For completeness the full positive weight sum is bounded as follows.
Let P_p(u)=Σ_(ab=u) p(a/N)p(b/N), so Σ_u P_p(u)=O(N²).
Boundedness of p and the elementary divisor bound used in L193 give
P_p(v)=O_epsilon(N^epsilon). For each fixed u,m at most two cells v
have nonempty intervals, as in L193; each has ell<=2R and
phi(u)/u²<=1/u<=N^(-2). Also alpha_m=O(1) and #M_in=O(h).
Dropping coprimality only in this nonnegative upper bound yields

Σ W <= C_epsilon h R N^epsilon = O_epsilon(h N^(3/2+epsilon)).

Combine this with (5), retaining the exact restrictions in the defined
masses, to obtain (3). Dividing by Nh and choosing epsilon<1/2 proves
its little-o assertion. Partition (2) into the strip and its complement,
and into positive and negative parts inside the strip, to obtain (4).
This establishes the claimed reduction. ∎

## Qualifications and verification

The positive part is taken at the ordered-pair level, before collecting
Q(v); it is not the positive part of Q(v). At xy=2 formula (1) is
nonpositive and strictly negative unless x=y=sqrt(2). Thus signs of
individual q values do not automatically cancel on a product cell.
Equation (4) leaves the required signed arithmetic estimate unproved,
as well as the other frequency and gcd sectors and RH.

Verification is analytic: profile-ratio algebra, hyperbolic identities,
Taylor's bound, exact finite expansion, and the inherited two-cell
absolute estimate. Formalization requires these identities and bounds,
nonnegativity of W, finite positive-part decomposition, and the stated
normalization. No numerical evidence is used for an asymptotic claim.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
