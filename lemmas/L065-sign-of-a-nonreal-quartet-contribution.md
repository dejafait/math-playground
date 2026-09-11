# Lemma 65: sign of a nonreal quartet contribution

**Hypotheses.** Fix a real parameter λ₀ in the theta heat deformation, and let x be a simple real zero of that slice, as in Lemma 64. Suppose the slice also has a quartet of distinct zeros

Q={a+ib,a-ib,-a+ib,-a-ib}, with a>0, b>0,

of common multiplicity m≥1. The common multiplicity follows from evenness and conjugation of the real slice. No existence of such a quartet for any particular slice is asserted.

**Conclusion.** Its additive contribution V_Q(x) to the forward-parameter velocity x'(λ₀) is

V_Q(x)=8mx(x²-a²+b²)/[(x²-a²+b²)²+4a²b²].                 (1)

In particular sign(V_Q(x))=sign(x) sign(x²-a²+b²). Equivalently:

| Condition | x>0 | x<0 |
| --- | --- | --- |
| x²>a²-b² | positive | negative |
| x²=a²-b² | zero | zero |
| x²<a²-b² | negative | positive |

Since x≠0, equality or the last row can occur only if a>b. If a≤b, the contribution always points away from the origin. If a>b, it points toward the origin for 0<|x|<sqrt(a²-b²), vanishes at |x|=sqrt(a²-b²), and points away for larger |x|. These are signs of this contribution, not of the full velocity.

## Proof

Lemma 64 supplies x≠0 and an absolutely convergent sum over the other opposite-zero pairs. The two representatives a+ib and a-ib account for the whole quartet, each repeated m times. Thus its contribution is precisely

4mx[1/(x²-(a+ib)²)+1/(x²-(a-ib)²)].

Put d=x²-a²+b² and e=2ab. The two denominators are d-ie and d+ie. Their reciprocal sum is 2d/(d²+e²), proving (1). The denominator is strictly positive because a,b>0. The sign classification follows because 8m>0 and x≠0. When a≤b, d=x²+(b²-a²)>0. When a>b, comparing |x| with sqrt(a²-b²) gives all remaining cases. Absolute convergence from Lemma 64 justifies extracting this finite contribution even when there are infinitely many other pairs. No limit or parameter derivative of the zero sum is involved. ∎

## Qualifications and algebraic checks

For a=5, b=3, m=1, the values at x=3,4,5 are respectively -168/949, 0, and 40/109. Changing x to -x reverses each sign. These are exact algebraic configurations, not asserted theta zero locations. They show why the quartet expression alone has no universal positive sign at a positive real zero. No failed theta theorem or counterexample to RH is claimed.

The threshold sqrt(a²-b²) is strictly smaller than a. Thus for a>b the quartet can contribute positively even when 0<x<a; a rule based only on whether x lies to the left or right of a is incorrect. Purely imaginary zeros would form an opposite pair, not a distinct quartet, and are outside the stated hypotheses.

One can independently check the normalization with the real polynomial

P(z)=(z²-x²)[z⁴-2(a²-b²)z²+(a²+b²)²]^m.

Its zero at x is simple, and direct differentiation gives P''(x)/P'(x)-1/x=V_Q(x). This polynomial is only an algebraic check of the isolated contribution. It is not claimed to be a theta heat slice.

## Verification and formalization obligations

The proof consists of exact conjugate-denominator algebra and a positive-denominator sign analysis. Run `python3 scripts/heat/check_quartet_contribution.py` for exact rational checks of the polynomial identity, both signs of x, multiple multiplicities, and the equality case. These finite checks supplement the proof and are not numerical evidence about zeta zeros. Formalization would require extraction of the finite sub-sum in Lemma 64, the conjugate reciprocal identity, strict denominator positivity, and the displayed real inequalities.
