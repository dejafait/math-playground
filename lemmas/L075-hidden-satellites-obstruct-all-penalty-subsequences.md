# Lemma 75: hidden satellites obstruct all penalty subsequences

**Hypotheses and construction.** For n≥1 set

X_n=2^n, b_n=1−2^{-n}, d_n=16^{-n}, δ_n=d_n²,
c_n=b_n+δ_n, w_n=X_n+i b_n, v_n=X_n+d_n+i c_n.

Define

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²)
                 (1−z²/v_n²)(1−z²/conjugate(v_n)²).

For each zero u define its upward contribution by

E_f(u)=2Σ_{Im ρ>Im u}(Im ρ−Im u)/|ρ−u|².

**Conclusion.** This is a nonzero even real entire function with exactly the simple zeros ±w_n, ±conjugate(w_n), ±v_n, ±conjugate(v_n), and finite full-zero reciprocal-square sum. Its positive-coordinate, positive-height zeros have strictly increasing coordinates and heights tending respectively to infinity and H=1, so this product belongs to the monotone quartet class in Lemma 74.

For every ε>0 the maximum of Im ρ−ε(Re ρ)² exists. Every maximizer is a center w_n or its reflection −conjugate(w_n), and every maximizer u satisfies E_f(u)>1. Consequently there is no sequence of positive penalties tending to zero and corresponding maximizing zeros along which E_f tends to zero. Equivalently the lower limit of E_f along the indices that can occur as penalty maximizers is at least 1, not zero.

## Proof

First, 0<d_n≤1/16 and X_n+d_n<X_{n+1}. Also

0<δ_n=2^{-8n}<2^{-n-1}=b_{n+1}−b_n,

so 0<b_n<c_n<b_{n+1}<1. The right upper zeros therefore interleave as w_1,v_1,w_2,v_2,… with strictly increasing coordinates and heights. Each cluster has eight distinct zeros of modulus at least X_n. Hence its full-zero reciprocal-square sum is at most 8·4^{-n}, with total at most 8/3.

The compact logarithmic-tail product argument in Lemma 72 applies directly: on |z|≤R the sum of the moduli of the four factor arguments per cluster is at most 4R²Σ_n4^{-n}; eventually each argument has modulus at most 1/2, and the power-series logarithm obeys |log(1−u)|≤2|u|. The analytic logarithmic tails converge uniformly on each disk and exponentiate to nonvanishing tails. The finite factors supply precisely the listed simple roots, since all roots are distinct. The limit is entire, even and real, and f(0)=1. Its supremum height is 1 and is not attained. The interleaved positive coordinates also have reciprocal-square sum at most 2Σ_n4^{-n}, as required for the stated class.

Put A_n=X_n² and D_n=(X_n+d_n)²−X_n²=2X_nd_n+d_n². The slope of the chord joining consecutive centers in the squared-coordinate/height plane is

t_n=(b_{n+1}−b_n)/(A_{n+1}−A_n)=1/(6·8^n).

The satellite lies strictly between those coordinates, 0<D_n<A_{n+1}−A_n. Its slope from the left center satisfies

δ_n/D_n=d_n/(2X_n+d_n)<d_n/(2X_n)
=1/(2·32^n)<1/(6·8^n)=t_n,                 (1)

where the last strict inequality is exactly 3<4^n. Thus c_n<b_n+t_nD_n. With λ_n=D_n/(A_{n+1}−A_n)∈(0,1), for every ε>0 its score satisfies

c_n−ε(A_n+D_n)
< (1−λ_n)(b_n−εA_n)+λ_n(b_{n+1}−εA_{n+1})
≤ max{b_n−εA_n, b_{n+1}−εA_{n+1}}.          (2)

This excludes every satellite from the maximizing set, for every penalty, including penalties where center scores tie. Reflection across the imaginary axis preserves scores. Negative-height roots have smaller scores than their same-coordinate positive-height partners, so they too are excluded.

A maximum exists: fix the score q of w_1. Any root with score at least q has ε(Re ρ)²≤1−q, and also |Im ρ|<1. There are only finitely many listed roots in this bounded rectangle, and the eligible set contains w_1. Its maximum is the global maximum. By (2), every maximizer is a center or its reflection.

For completeness, E_f(u) converges at every fixed root u. For |ρ|>2|u| the distance is at least |ρ|/2, while every positive height difference is at most 2. The corresponding summand is at most 16|ρ|^{-2}. The rest comprises finitely many distinct roots, with nonzero denominators. Thus the reciprocal-square bound proves convergence, as in Lemma 72.

At w_n the satellite v_n alone contributes

2δ_n/(d_n²+δ_n²)=2/(1+d_n²)>1.               (3)

All other upward summands are nonnegative. Reflection across the imaginary axis bijects the zero set and preserves heights and distances, giving the same bound at −conjugate(w_n). This proves the uniform all-penalty obstruction.

There are maximizing indices tending to infinity as ε↓0: for any fixed N choose a center w_m with m>N. Since b_m>b_N, for sufficiently small ε its score exceeds b_N, whereas all centers with index at most N have score at most b_N. Satellite exclusion then forces every maximizer to have index greater than N. This confirms that the asserted obstruction applies at arbitrarily high indices and heights approaching 1. ∎

## Qualifications

The example resolves the full-upward-contribution question along penalty-maximizing indices in the restricted monotone class negatively. It does not contradict Lemma 74: that lemma takes a lower limit over all indices, including satellites, whereas the penalized selection here excludes all satellites. A single immediate successor already supplies the obstruction at every selected index. No uniform right-hand tail estimate could remove this positive local term.

This is a generic paired product, not an identified theta transform or heat slice. It does not refute RH or a favorable-selection assertion using additional theta-specific information. It also leaves open favorable sequences of zeros without the quadratic-maximizer requirement and any useful estimate for the full signed zero interaction.

## Verification and formalization obligations

The all-index proof is analytic. Supplementary exact rational checks are reproducible with `python3 scripts/heat/check_hidden_satellites.py`; finite tests do not certify the infinite assertion. Formalization would require compact logarithmic-tail convergence, exact simple-root identification, reciprocal-square summability, interleaving, the strict chord inequality and affine-score comparison, compact score maximization, reflection invariance, and passage from a single nonnegative summand to the convergent full sum.
