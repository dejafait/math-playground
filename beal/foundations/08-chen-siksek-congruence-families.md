# Chen–Siksek's infinite congruence families

Audited on 2026-09-26. Imin Chen and Samir Siksek, *Perfect powers expressible as sums of two cubes*, **Theorem 1**, *Journal of Algebra* **322** (2009), no. 3, pp. 638–656, DOI [10.1016/j.jalgebra.2009.03.010](https://doi.org/10.1016/j.jalgebra.2009.03.010).

## Exact input

Let n >= 3. If a positive divisor d of n meets at least one condition below, no signed integer triple (X,Y,Z) with XYZ nonzero and gcd(X,Y,Z)=1 satisfies X^3+Y^3=Z^n:

\[
\begin{array}{ll}
\mathrm{I}:&d\equiv2,3\pmod5,\\
\mathrm{II}:&d\equiv17,61\pmod{78},\\
\mathrm{III}:&d\equiv51,103,105\pmod{106},\\
\mathrm{IV}:&d\equiv b+108j\pmod{1296},\quad
b\in\{43,49,61,79,97\},\quad 0\le j\le11.
\end{array}
\]

Clause IV groups the sixty residues printed in the source; L011 verifies this grouping. The positive-divisor quantifier is retained, and coordinates of absolute value one are allowed.

## Source and computational qualifications

The [author manuscript dated 12 February 2009, p. 2](https://samirsiksek.github.io/siksek.github.io/papers/qr8.pdf#page=2) states the theorem; p. 1 defines primitivity and nontriviality. Sections 4 and 9 prove it using modular restrictions, reciprocity, and finite MAGMA calculations. No unproved conjecture is assumed. This imports the identified manuscript's theorem by citation; its proof computations and the publisher's final PDF were not independently checked here. The source-version provenance is also recorded in [the earlier foundation](07-chen-siksek-exponent-range.md).

The local [residue audit](../scripts/chen-siksek-congruences/check_residues.py) checks only the elementary arithmetic of this application. The source's density assertions in section 10 are not used as nonexistence premises.

## Mathlib

Coverage of the full signed theorem: **not checked**. Supporting congruence, coprimality, and Chinese remainder declarations: **not checked**. The numbered external theorem supplies the nonexistence input; no Mathlib match or absence claim is asserted.
