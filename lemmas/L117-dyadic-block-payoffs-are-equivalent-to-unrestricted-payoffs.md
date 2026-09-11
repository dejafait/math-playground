# Lemma 117: dyadic block payoffs are equivalent to unrestricted payoffs

**Hypotheses and definitions.** For a sequence c of nonnegative finite
counts and a nondecreasing finite-valued function F on the positive
integers, write

Q_c F(k)=Σ_(l>k) c_l(F(l)−F(k))/(l−k)².

Let S=⋃_(j≥1) [2^j,2^(j+1)−2]∩ℕ. Consider two existence assertions:

- (D) For every sequence of nonnegative integers M supported on S with
  Σ_l M_l/l²<∞, the counts c_l=1+M_l admit a positive strictly increasing
  unbounded F with Σ_l c_l F(l)/l²<∞ and sup_k Q_c F(k)<∞.
- (U) For every sequence of positive integers m with Σ_l m_l/l²<∞,
  there is a positive strictly increasing unbounded F with
  Σ_l m_l F(l)/l²<∞ and sup_k Q_m F(k)<∞.

**Conclusion.** Assertions (D) and (U) are equivalent. This is a proved
reduction only: neither assertion is established here.

More precisely, given counts m in (U), one can construct masses N
supported on S with Σ_r N_r/r²≤Σ_l m_l/l². Any payoff H supplied by
(D) for 1+N gives a payoff F for m satisfying

sup_k Q_m F(k)≤4 sup_r Q_(1+N) H(r)+Σ_l m_l/l².

## Proof

The complement of S is {1}∪{2^j−1:j≥2}. Each missing integer is
followed by an integer of S. Define

T(k)=min{r∈S:r≥k}.

Then k≤T(k)≤k+1≤2k. The map T is nondecreasing, tends to infinity,
and each fiber has at most two elements. For each r∈S set
N_r=Σ_(k:T(k)=r) m_k, and set N_r=0 off S. These are finite
nonnegative integers. Grouping nonnegative sums gives

Σ_r N_r/r²=Σ_k m_k/T(k)²≤Σ_k m_k/k²=:A<∞.

Assume (D), and apply it to these masses. Let H be its payoff and
C=sup_r Q_(1+N) H(r)<∞. Put P(k)=H(T(k)). This is positive,
nondecreasing and unbounded, but collisions of T can prevent strict
increase. Its weighted sum is finite, because T(k)≤2k implies

Σ_k m_k P(k)/k²
 ≤4Σ_k m_k H(T(k))/T(k)²
 =4Σ_r N_r H(r)/r²<∞.

Fix k, and write s=T(k). If l>k and T(l)=s, the increment
P(l)−P(k) vanishes. Otherwise r=T(l)>s and

r−s≤l+1−k≤2(l−k).

Consequently, using nonnegative series and grouping by r,

Q_m P(k)
 ≤4Σ_(r>s) [H(r)−H(s)]/(r−s)²
                ·Σ_(l>k:T(l)=r) m_l
 ≤4Σ_(r>s) N_r[H(r)−H(s)]/(r−s)²
 ≤4Q_(1+N) H(s)≤4C.

No mass at an equal image is divided by a zero distance; those terms
were removed before grouping. The estimate proves convergence of the
full series as well as its uniform bound.

For strict increase set B(k)=1−1/(k+1) and F=P+B. For integers
l>k≥1, put d=l−k≥1. The identity

(k+1)d−l=k(d−1)≥0

implies (k+1)(l+1)(l−k)≥l(l+1)≥l². Hence

(B(l)−B(k))/(l−k)²
 =1/[(k+1)(l+1)(l−k)]≤1/l².

It follows that Q_m B(k)≤A for every k. Since 0<B(k)<1,
Σ_k m_k B(k)/k²≤A. Therefore F has the stated generator bound,
finite weighted sum, positivity, strict increase and unboundedness.
This proves (D) implies (U).

Conversely, counts 1+M in (D) are positive integers with summable
reciprocal-square weights, because Σ_l 1/l²<∞. Applying (U) directly
proves (D). ∎

## Qualifications

The tested dyadic blocks thus impose no simplification of the universal
payoff-existence question, despite the mandatory gaps. The reduction
allows increase within blocks and does not use any block-constant
ansatz. It is not a counterexample to either assertion and does not
prove nonexplosion, a new upward-selection theorem, or RH. The earlier
endpoint obstruction is motivation only, not a mathematical input.

## Verification and formalization obligations

This elementary analytic proof requires no numerical certificate.
Audit the singleton first block, missing sites 1 and 3, fibers of size
two, equal-image cancellation, the factor-two distance inequality,
nonnegative grouping, weighted factor four, and the correction bound
including l=k+1 and k=1. Formalization would require the explicit map
T, these integer inequalities, nonnegative-series grouping, and the two
quantified implications. Neither (D) nor (U) may be used as an
unconditional proved existence input.
