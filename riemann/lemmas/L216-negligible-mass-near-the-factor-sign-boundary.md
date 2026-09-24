# Lemma 216: negligible mass near the factor sign boundary

**Hypotheses.** Use the exact nonnegative ordered weight W and ratio r
of L213, with all original factors in [N,2N], m in M_in, integer
displacement lengths and gcd(m,ab)=1. In particular h is comparable
to N^(3/2), R=O(N^(3/2)), and N is sufficiently large and real.
Let 0<=H<=N and s=sqrt(2)N. Constants are independent of H.

**Conclusion.** Define the absolute ordered mass in the factor tubes by

T(H)=Σ_(min(|c-s|,|d-s|)<=H) W(a,b,c,d,m)|r(c/N)r(d/N)|.

Then

T(H)<=C Rh H(H+1)/N².                                   (1)

Consequently H_*=N^(3/4)/log N gives T(H_*)=o(Nh), with
normalized bound O((log N)^(-2)+N^(-3/4)/log N). The same
bound holds for the ordered positive mass in any further restriction
of these tubes, including the interior far exterior remaining in L215.

**Proof.**

L195 gives r(x)=-tanh((3/2)log(x/sqrt(2))) on [1,2]. Thus
r(sqrt(2))=0 and

|r'(x)|=(3/(2x)) sech²((3/2)log(x/sqrt(2)))<=3/2.

The mean value theorem, applied within [1,2], implies

|r(c/N)|<=3|c-s|/(2N).

Also |r(x)|<=1. If either factor is within H of s, it follows that

|r(c/N)r(d/N)|<=3H/(2N).                                (2)

This bound includes H=0, when every selected term vanishes.

The interval [s-H,s+H] contains at most 2H+1 integers, and
[N,2N] contains at most N+1 integers. Counting each choice of the
restricted coordinate, with possible overlap, gives at most

2(2H+1)(N+1)<=C N(H+1)                                 (3)

ordered pairs for N>=1. Intersections with the actual factor support
only decrease this count. No factor-product distribution is assumed.

For every fixed c,d on that support, the proof of L213 gives

Σ_(a,b,m) W(a,b,c,d,m)<=C Rh/N².                        (4)

Its constant is uniform in c,d: exact nonempty cells restrict ab to
an interval of length O(h), whose weighted ordered-pair population
is O(h); the exact coprime m sum of alpha_m ell is O(R), and
phi(ab)/(ab)²<=N^(-2). The remaining profiles are bounded.
The left side of (4) retains every original restriction. In particular,
no replacement of cell lengths or coprimality by density occurs.

Multiplying (2), (3), and (4), using nonnegativity, proves (1).
Dividing by Nh and using the scale for R gives

T(H)/(Nh)<=C H(H+1)/N^(3/2).

Substituting H_* yields exactly the two vanishing terms asserted.
For any subset of the tubes, its positive mass is bounded termwise
by T(H); this proves the restricted assertion.

## Qualifications, verification

Combining this with the earlier localizations leaves positive mass on

N²+D_*<cd<4N²-D_*, |cd-2N²|>B_*,
|c-s|>H_*, |d-s|>H_*,

where D_*=N^(7/4)/log N and B_*=N^(15/8)/log N.
There is no estimate on that complement at the Nh scale in this
lemma. L214 and L215 are comparisons, not inputs to (1). L212's
negative-strip bound still cannot be used to decide the signed total.
Neither a signed-total assertion nor an RH assertion follows.

Verification is analytic: differentiation on the compact factor interval,
the mean value theorem, integer interval counts including H=0,
the uniform fixed-pair estimate, nonnegative restriction, and scale
normalization. No numerical or distribution claim is used.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
