# Known result used to calibrate the gap

Checked on 2026-09-24: Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12, [Theorem 1.3 in arXiv:1909.03562v7](https://arxiv.org/html/1909.03562v7). The inspected revision is dated 2026-07-16. This is background for route selection, not an input to L001.

## Hypotheses

Let C be the Collatz map of foundations/01-target-and-scope.md, and let f be any real-valued function on positive integers with f(n) tending to positive infinity.

## Conclusion

The set of n for which min over k>=0 of C^k(n) is less than f(n) has logarithmic density 1. In particular, if E is its complement, then

\[
\lim_{X\to\infty}\frac{1}{\log X}\sum_{\substack{n\le X\\n\in E}}\frac1n=0.
\]

## Proof

Precise citation: Tao, Theorem 1.3 at the link above; logarithmic density is Definition 1.2 of the same paper. The cited theorem is not reproved here. The displayed formulation uses that the harmonic sum up to X is asymptotic to log X.

The theorem permits an exceptional set and requires f to diverge. Choosing f identically 2 to force the integer orbit minimum to equal 1 is outside its hypotheses and would still leave exceptional starts. This is the difference from the required bound and quantifier. No numerical verification record or exhaustive literature review is claimed.

## Mathlib

Full Theorem 1.3: **not checked**. No Mathlib theorem names or matching coverage are asserted. The cited paper is a mathematical source, not evidence of Mathlib coverage.
