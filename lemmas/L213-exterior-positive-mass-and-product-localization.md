# Lemma 213: exterior positive mass and product localization

**Hypotheses.** Use L195's ordered weight W, ratio r, exact lengths
from L191, and interior integer set M_in. All sums retain gcd(m,ab)=1.
The fixed scales satisfy h comparable to N^(3/2), R=O(N^(3/2)),
a± comparable to N², and a+−a−=h/(2π). Fix K>0 and put L=N^(3/2).
Statements hold for sufficiently large real N. Constants may depend
on K, the fixed profiles, and scale constants, but not on B below.

**Conclusion.** Define the ordered exterior positive mass

E_out^+=Σ_(|cd−2N²|>KL) W(a,b,c,d,m)
                           max(r(c/N)r(d/N),0).

Then max(Y_out,0)<=E_out^+=O(Rh)=O(N³). More precisely, for
KL<=B<=N², its part E_out^+(B) with |cd−2N²|<=B satisfies

E_out^+(B)<=C R h B²(B+N)/N⁶.                            (1)

Consequently, uniformly for L<=B<=N² with B>=KL,

E_out^+(B)=O(B³/N³),
E_out^+(B)/(Nh)=O(B³/N^(11/2)).                          (2)

In particular B=N^(7/4) yields E_out^+(B)=o(Nh). More generally
this holds whenever B=o(N^(11/6)) within the stated range.
These are upper bounds, not sharpness claims. They do not decide
whether the full exterior can cancel L212's negative-strip mass.

**Proof.**

Write u=ab, v=cd, and P_p(u)=Σ_(ab=u) p(a/N)p(b/N), with
all original ordered factor restrictions. This is nonnegative and
bounded-profile weighted. L197 proves, uniformly for fixed u,v,

Σ_(m∈M_in, gcd(m,u)=1) alpha_m ell(u,v,m)<=C R.           (3)

In particular it keeps all exact cell lengths and restrictions.
Its proof uses only the O(1) possible m in a nonempty cell, so (3)
applies on the full product support, not only the central strip.

If ell>0, a nonempty exact integer cell has
uv−R<=m²<=u(v+1)+R−1. Since a−<=m<=a+, it follows that

u∈J_v=[(a−²−R)/(v+1),(a+²+R)/v].                       (4)

This is only an enlargement used for an upper bound. Its length is

|J_v|=(a+²−a−²)/v+a−²/[v(v+1)]
                         +R(1/v+1/(v+1))=O(h),         (5)

uniformly for v∈[N²,4N²]. Here a+²−a−²=O(hN²), the
second term is O(1), and the last is O(R/N²). The aggregate
ordered-pair interval bound proved in L197 gives

Σ_(u∈J_v) P_p(u)<=C(|J_v|+N)<=C h.                     (6)

For any real product interval J of length D, summing first in u,m,
using phi(u)/u²<=N^(−2) and then (3)–(6), gives the nonnegative
weight estimate

Σ_(cd∈J) W <= C R h N^(−2) Σ_(v∈J)P_p(v)
            <= C R h (D+N)/N².                         (7)

All finite sums on the left still have their original cutoffs and
coprimality. Only the majorant on the right enlarges their support.
Taking J=[N²,4N²] and using |r|<=1 proves E_out^+<=C Rh.
Termwise positive-part domination proves max(Y_out,0)<=E_out^+.

For |v−2N²|<=B<=N² put x=c/N, y=d/N. The quantity
A=(3/2)log(xy/2) in L195 satisfies |A|<=C B/N², by the
mean value theorem on xy/2∈[1/2,3/2]. Its other coordinate D
has cosh D>=1. Therefore L195's exact identity implies

max(r(x)r(y),0)<= (cosh A−1)/2 <= C B²/N⁴.              (8)

For the first inequality, when the numerator cosh A−cosh D
is positive it is at most cosh A−1 and its denominator is at
least 2; otherwise the positive part vanishes. The second follows
from Taylor's theorem on the fixed compact range of A.
Apply (7) to [2N²−B,2N²+B] and multiply by (8).
Removing the inner strip only decreases this nonnegative sum.
This proves (1). For B>=L, B+N<=2B eventually, Rh=O(N³),
and Nh is comparable to N^(5/2), proving (2) and its consequences.

## Qualifications, verification

E_out^+ takes positive parts before collecting ordered factors; it
need not equal max(Y_out,0). For example (2) with B=N^(7/4)
is O(N^(9/4)), whereas the full bound O(N³) exceeds Nh by a
factor N^(1/2). Thus this estimate localizes any possible positive
mass of size Nh to |cd−2N²|>N^(7/4); it does not prove such
mass exists there or determine its signed balance. L212 is used
only for this comparison and not to prove the bound.

The cutoff is never replaced by an average length or extended in
the defined masses. Verification is analytic: the nonempty-cell
inequality, exact rational identity (5), uniform aggregate pair
counts, nonnegative finite majorants, hyperbolic positive-part bound,
and scale exponents. No computational or distribution hypothesis is
used. RH is unresolved.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
