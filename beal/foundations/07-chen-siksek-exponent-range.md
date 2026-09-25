# Chen–Siksek's finite exponent range

Audited on 2026-09-25. Imin Chen and Samir Siksek, *Perfect powers expressible as sums of two cubes*, **Theorem 2**, *Journal of Algebra* **322** (2009), no. 3, pp. 638–656, DOI [10.1016/j.jalgebra.2009.03.010](https://doi.org/10.1016/j.jalgebra.2009.03.010). The publication details are corroborated by [Warwick's institutional record](https://wrap.warwick.ac.uk/id/eprint/27755/).

## Exact statement and source version

For every integer n with 3 <= n <= 10^9, there are no integers X,Y,Z satisfying

\[
X^3+Y^3=Z^n,\qquad XYZ\ne0,\qquad \gcd(X,Y,Z)=1.
\]

The [author-hosted manuscript, dated 12 February 2009](https://samirsiksek.github.io/siksek.github.io/papers/qr8.pdf#page=3), supplies Theorem 2 on manuscript p. 3. Its abbreviated wording is interpreted in the nontrivial primitive scope defined on p. 1 and explicitly used in its proof, section 12, p. 18. Coordinates are signed integers, and absolute value one is allowed. No unproved conjecture is an assumption of this statement.

The introduction attributes n=5,7,11,13 to Dahmen's thesis, section 3.3.2, and the initial range through 10^4 to earlier results. Section 12 certifies the remaining prime exponents through Proposition 11.1. This is a bounded exponent range with unrestricted bases.

These are manuscript page numbers; the [author's publication page](https://samirsiksek.github.io/siksek.github.io/index.html) warns that its files may differ from final versions. The publisher's final PDF was not retrieved. The cited input is the numbered theorem in this identified manuscript of the published paper.

## Computational qualifications

The theorem is imported by citation; neither its earlier small-exponent proofs nor its full computation was independently reproduced. The [author's repository](https://github.com/samirsiksek/n33) identifies `thm2.gp` as the program for Theorem 2. Its [source](https://raw.githubusercontent.com/samirsiksek/n33/main/thm2.gp) was inspected. It tests a sufficient modular criterion, not a search for integer solutions. Its comments use Proposition 4.1, an older numbering than Proposition 11.1 in the manuscript; that difference is retained here.

The code tests auxiliary primes ell=kn+1, the required size restriction, and trace inequalities. Its point-multiplication shortcut is exact: if an integer N fails to annihilate a point of a finite group, Lagrange's theorem implies that the group order is not N. An annihilated test point by itself proves no equality; the code then compares the exact Frobenius traces. Thus the choice of a test point affects speed, not the logical force of a successful check. This observation does not certify that the entire reported range was rerun here.

Theorem 1's infinite congruence families and density assertions are separate statements and are not imported by this foundation.

## Mathlib

Coverage of the full signed nonexistence theorem: **not checked**. Supporting gcd, power, and finite-group declarations were not checked. Chen–Siksek's Theorem 2 is the precise external input, not an asserted Mathlib declaration; the computation repository is supporting provenance.
