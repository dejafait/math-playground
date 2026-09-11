# Lemma 71: quadratically penalized height maxima

**Hypotheses.** Let f be a nonzero even real entire function whose zeros are simple, nonzero, and have full-zero reciprocal-square sum M=Σ_ρ |ρ|^{-2}<∞. Suppose H=sup_ρ Im ρ is finite and positive. These hypotheses apply in particular to simple-zero paired products with these properties. For ε>0 choose a zero w_ε=a_ε+i b_ε maximizing Im ρ−ε(Re ρ)². Define the upward contribution E_f as in Lemma 67.

**Conclusion.** Such a maximizer exists for every ε>0. Every choice of maximizers satisfies b_ε→H and εa_ε²→0 as ε↓0. For all sufficiently small ε, b_ε>0. For such ε write a=a_ε, b=b_ε and

R=2sqrt(a²+H²)+1,

A_ε=Σ_{ρ=u+iv: v>b, |u|≤R} |u+a|/|u−a|,

T(R)=Σ_{ρ: |Re ρ|>R}|ρ|^{-2}.

The sum A_ε is finite, all its denominators are nonzero, and

0≤E_f(w_ε)≤2ε A_ε+8(H−b)T(R).                 (1)

The second term tends to zero. Thus ε A_ε→0 would imply a favorable sequence (indeed the corresponding full limit) of upward contributions. No such estimate on A_ε is asserted from the hypotheses.

For each fixed 0<ε≤1/4, there are finite paired products with H≤1 for which a penalized maximizer has arbitrarily large E_f. This last assertion varies the product; it is not a counterexample to a limit for one fixed product as ε↓0.

## Proof

Evenness and the height supremum give |Im ρ|≤H. Fix any zero ρ_0=u_0+iv_0 and put q_0=v_0−εu_0². A zero with score at least q_0 must satisfy ε(Re ρ)²≤H−q_0. Such zeros lie in a compact rectangle. A nonzero entire function has finitely many zeros in that rectangle, and at least ρ_0 is eligible. Maximizing over this finite set also maximizes over all zeros.

Let m_ε=b_ε−εa_ε² be this maximum. For every η>0 there is a fixed zero u+iv with v>H−η. Therefore

H≥b_ε≥m_ε≥v−εu².

Taking a lower limit as ε↓0 and then letting η↓0 gives m_ε→H and b_ε→H. Moreover 0≤εa_ε²=b_ε−m_ε≤H−m_ε→0. These arguments do not require uniqueness or a continuous choice of maximizer.

For every higher zero ρ=u+iv, maximality implies

0<v−b≤ε(u²−a²).

In particular |u|>|a|, so u−a is nonzero and

2(v−b)/((u−a)²+(v−b)²)
≤2ε(u²−a²)/(u−a)²
=2ε |u+a|/|u−a|.                              (2)

The last equality uses u²−a²>0, which makes the ratio (u+a)/(u−a) positive. There are finitely many zeros in |u|≤R, |v|≤H, so summing (2) there gives the first term of (1).

For |u|>R, |ρ|≥|u|>2sqrt(a²+H²)≥2|w_ε|. Thus |ρ−w_ε|≥|ρ|/2, and the corresponding upward term is at most 8(H−b)|ρ|^{-2}. Summing gives the second term of (1). The definition and absolute convergence of E_f follow by the reciprocal-square tail argument of Lemma 67: at a fixed simple zero the remaining finite denominators are nonzero, and the tail has the same distance majorant. All terms are nonnegative, so the estimates pass to the infinite sum. Finally T(R)≤M and H−b→0, proving the asserted vanishing of the second term even without knowing that R tends to infinity.

To prove the finite-product assertion, fix 0<ε≤1/4 and 0<d≤1/2. Put

b=1/2,  δ=εd(2+d)/2,  c=b+δ,

f_{ε,d}(z)=Π_{α∈{1+ib,1−ib,1+d+ic,1+d−ic}}(1−z²/α²).

This polynomial is even and real. Its eight zeros are distinct and simple, nonzero, and have H=c≤1/2+5/32<1. Its reciprocal-square sum is finite (in fact at most 8). The scores of its positive-height zeros at real coordinates ±1 are b−ε. At ±(1+d) the scores are

c−ε(1+d)²=b−ε−δ<b−ε.

Negative-height zeros have smaller scores than their same-coordinate positive-height partners. Hence w=1+ib is a global penalized maximizer. The higher zero 1+d+ic alone yields

E_{f_{ε,d}}(w)≥2δ/(d²+δ²)
=ε(2+d)/[d(1+ε²(2+d)²/4)].                  (3)

For fixed ε this tends to infinity as d↓0. Thus neither maximality nor uniform bounds H≤1 and M≤8 control the local contribution uniformly over this class. Each individual polynomial has an attained highest zero, and for sufficiently small penalty its maximizers have that highest height and E_f=0; changing d or ε changes the example. ∎

## Qualifications and unresolved estimate

Penalization excludes a higher zero at the same absolute real coordinate, but imposes no positive lower bound on its horizontal distance. Formula (2) retains an inverse horizontal distance; (3) shows this is a real obstruction to a uniform local estimate, not just an artifact of the tail split. The finite examples do not decide whether every fixed infinite product admits a favorable sequence, nor whether all its penalized maximizers are favorable. No time-dependent supremum derivative, heat evolution, or conclusion about RH follows.

## Verification and formalization obligations

The proof uses elementary compactness of the zero set, inequalities, and summation of nonnegative terms. The exact arithmetic checks in `python3 scripts/heat/check_quadratic_penalty.py` verify the example's score ordering, bounds on H, and (3), plus the pointwise inequality (2). They are supplementary, not an infinite-product certificate. Formalization would require finite zeros in a compact rectangle, the supremum approximation and squeeze limits for arbitrary maximizer choices, splitting the upward sum, and the explicit polynomial's distinct roots and scores.
