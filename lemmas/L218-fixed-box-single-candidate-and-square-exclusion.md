# Lemma 218: fixed-box single candidate and square exclusion

**Hypotheses.** Use the exact weights, scales and normalized A_cd of
L217, the cell endpoints of L191, and the positive coefficient alpha_m
of L194. Restrict the ordered integers c,d to [8N/5,17N/10]; a,b
remain in [N,2N]. The actual profile p is continuous and strictly
positive on [1,2], hence has fixed positive upper and lower bounds.
All statements are for sufficiently large real N. Put u=ab, v=cd and

k=ceil(sqrt(uv-R)).

If k belongs to M_in and gcd(k,u)=1, evaluate the exact endpoints
b_0,t_0 from L191 at m=k and set e=max(t_0-b_0,0)/R.
Otherwise set e=0. In particular e is a normalized length, not an
integer count and not a coprimality density. Define the finite sum

Q_N=sum_(a,b,c,d in the indicated boxes) [phi(u)/u] e.

**Conclusion.** At most one integer m can have a nonempty cell for
each quadruple; it must be k. Thus the exact mass uses only this
candidate. Every quadruple with abcd a perfect square contributes
zero, including before any stationary endpoint restriction.
Moreover, with fixed positive comparison constants,

sum_(c,d in the fixed box) A_cd f_cd comparable to Q_N/h.       (1)

Consequently the requested O(N^(3/2)) bound on this box is equivalent
to Q_N=O(N³); the corresponding little-o statements are also equivalent.
The available elementary estimate is only Q_N=O(N^(7/2)).
The stronger counting estimate is **unproved**.

**Proof.**

A nonempty exact cell implies, by L191,

uv-R <= m² <= u(v+1)+R-1.                                  (2)

All m are positive. The length of the possible real m interval is

(u+2R-1)/(sqrt(u(v+1)+R-1)+sqrt(uv-R)).                     (3)

Uniformly on the box, uv is bounded below by (64/25)N⁴,
R=O(N^(3/2)), and u<=4N². The expression in (3) is at most

(1/2)sqrt(u/v)(1+O(N^(-5/2)))+O(N^(-1/2))
 <= 5/8+O(N^(-1/2)) <1.

Here sqrt(u/v)<=sqrt(4/(64/25))=5/4. Thus any integer in
this closed interval must be its first possible integer k. There
may be no integer, and the original outer constraints can still
exclude k. Evaluating the exact cell at k and keeping those constraints
therefore gives precisely the original length sum, with no averaging.

If uv=j² is a perfect square, j>=8N²/5 and eventually R<2j-1.
It follows that j-1<sqrt(j²-R)<j, so k=j. Any prime dividing
u>1 divides j²=uv and therefore j. Thus gcd(j,u)>1 and the
quadruple has zero coprime weight. This argument does not use a
putative frequency distribution of squares or nonsquares.

For an admissible candidate with e>0, insert ell=Re into L195's
weight and L217's definition. Exactly,

sum_(box) A_cd f_cd
 = (1/h) sum_(quadruples with admissible k)
       B(a,b,c,d,k) [phi(u)/u] e,                          (4)

where

B=(N²/u) p(a/N)p(b/N)p(c/N)p(d/N) alpha_k f_cd.

The factor N²/u lies in [1/4,1]. By L194 alpha_k is bounded
above and below by fixed positive constants on M_in. The same is
true for the p factors by the stated compact positivity. L217 proves
f_cd>=r0²>0 on this fixed box, while f_cd<=1. Hence B has
uniform positive upper and lower bounds, proving (1). Candidates
with e=0 contribute nothing and require no value of alpha outside
M_in. Since h is comparable to N^(3/2), the equivalences follow.

For completeness, e<=2 and phi(u)/u<=1. If e>0, (2) and
k in [a−,a+] imply u in L213's interval J_v of length O(h).
The ordered pair bound proved there gives O(h) possibilities for
a,b for each fixed c,d, and there are O(N²) choices of c,d.
Thus Q_N=O(hN²)=O(N^(7/2)). Passing to the required O(N³)
would save a factor N^(1/2) in this length- and totient-weighted
coprime population. Square-product exclusion alone supplies no such
saving; no estimate for the remaining population is asserted.

## Qualifications, verification

This is a scoped reduction of the fixed-box question, not a proof or
refutation of its proposed bound. The candidate uses sqrt(uv-R),
not sqrt(uv): near the lower edge those ceilings can differ. Both
the exact displacement length and gcd(k,u)=1 remain in Q_N; the
totient weight has not been replaced by a constant. In particular
square-product mass from a sector without this gcd restriction cannot
be imported as a lower bound here. The signed total and RH remain open.

Analytic verification consists of the uniform interval-width estimate,
the prime-divisor exclusion, the exact normalization (4), and the
aggregate support count. `python3 scripts/heat/check_fixed_box_candidate.py`
checks the unique-candidate and square-exclusion assertions and compares
the exact length sum against a direct integer-m enumeration on finite
samples with rational endpoints. These tests are not asymptotic evidence.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
