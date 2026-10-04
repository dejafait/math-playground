# L016 — Mixed seventh-power q=29 finite certificate

## Hypotheses

Set q=29. For t in {14,10,25,15}, let C_t be the smooth projective model of

\[
y^2=f_t(x)=5x^6-12x^5+10t x^3+t^2
\]

over F_29. Use the order t=14,10,25,15 throughout. The source's corresponding eta labels are 10,14,24,28; these are labels only here, with no asserted descent or parameter-reduction applicability.

The six comparison polynomials, in order, are

\[
H=(T,\ T^2,\ T^2+5T+2,\ T^2+3T+4,\ T-2,\ T-5).
\]

These data and the expected reductions are from Chocian, *The Primitive Generalized Fermat Equation x^3+y^5=z^7: A computer-assisted proof*, **arXiv:2609.26996v1, Section 6.2, equations (38)–(40)**, [versioned source](https://arxiv.org/html/2609.26996v1). This lemma independently reproduces the finite arithmetic; it does not assume the source's modular-packet exhaustion or its main theorem.

## Conclusion

Each C_t is a genus-two curve with two F_29-rational points at infinity. Its complete projective counts N1=#C_t(F_29), N2=#C_t(F_(29^2)), and trace coefficients A=30-N1, B=(A^2-842+N2)/2 are:

| t | N1 | N2 | A | B | P_t(T)=T^2-A T+B-58 | P_t modulo 7 |
| --- | --- | --- | --- | --- | --- | --- |
| 14 | 29 | 955 | 1 | 57 | T^2-T-1 | T^2+6T+6 |
| 10 | 22 | 916 | 8 | 69 | T^2-8T+11 | T^2+6T+4 |
| 25 | 37 | 931 | -7 | 69 | T^2+7T+11 | T^2+4 |
| 15 | 25 | 883 | 5 | 33 | T^2-5T-25 | T^2+2T+3 |

The four Frobenius characteristic polynomials, in the point-count convention, are respectively

\[
\begin{aligned}
&X^4-X^3+57X^2-29X+841,\\
&X^4-8X^3+69X^2-232X+841,\\
&X^4+7X^3+69X^2+203X+841,\\
&X^4-5X^3+33X^2-145X+841.
\end{aligned}
\]

In the indicated row and column orders, the resultants Res(P_t,H_j) modulo 7 are

\[
\begin{pmatrix}
6&1&5&1&1&5\\
4&2&3&1&6&3\\
4&2&6&1&1&1\\
3&2&6&2&4&3
\end{pmatrix}.
\]

All 24 entries are nonzero. Therefore no P_t has a root in common with any displayed H_j over the algebraic closure of F_7. This is a separation result relative to these six polynomials, not an assertion that they contain every possible trace required by the fixed-signature argument. No Beal signature is excluded by this lemma alone.

## Proof

**Smoothness and points at infinity.** In characteristic 29,

\[
f_t'(x)=30x^2(x^3-2x^2+t).
\]

If r were a common root of f_t and its derivative, r would be nonzero since f_t(0)=t^2 and all four t are nonzero. Thus t=-r^3+2r^2. Substitution gives f_t(r)=-4r^4(r^2-r-1), so r^2=r+1. Then r^3=2r+1 and t=1, contrary to every listed parameter. Hence f_t is squarefree. The double cover of the x-line has six simple geometric branch points, so the Riemann–Hurwitz formula gives genus two.

The infinity chart u=1/x, v=y/x^3 has equation

\[
v^2=5-12u+10t u^3+t^2u^6.
\]

At u=0, v=11 or 18 in F_29. Both roots are simple since 2v is nonzero. These are all the points at infinity, already rational over F_29, and each count over either field must include both.

**Exact field enumeration.** Since 29 is 5 modulo 8, the supplementary law for the Legendre symbol gives (2/29)=-1. Consequently F_(29^2)=F_29[w]/(w^2-2) is a field, with multiplication

\[
(a+bw)(c+dw)=(ac+2bd)+(ad+bc)w.
\]

For a field of odd order, the number of y with y^2=z is 1+chi(z), taking chi(0)=0. In the extension, chi(a+bw)=chi_29(a^2-2b^2): the norm is z^(29+1), and its base-field quadratic character is z^((29^2-1)/2).

The following table records the numbers of x with chi(f_t(x))=-1,0,+1 in each field. It is an exhaustive finite calculation, using all 29 base elements and all 841 distinct pairs (a,b) in the extension, with the multiplication above and Horner polynomial evaluation.

| t | F_29: -1,0,+1 | F_841: -1,0,+1 |
| --- | --- | --- |
| 14 | 15,1,13 | 364,1,476 |
| 10 | 19,0,10 | 384,0,457 |
| 25 | 11,1,17 | 376,1,464 |
| 15 | 17,1,11 | 400,1,440 |

Thus N1=31+n_+-n_- and N2=843+n_+-n_-, with the counts in their respective columns. These give exactly the displayed N1,N2. The complete reproducer is [check_q29.py](../scripts/mixed-seventh-certificate/check_q29.py), run from the notebook by `python3 scripts/mixed-seventh-certificate/check_q29.py`; its exact output is saved in [results.json](../scripts/mixed-seventh-certificate/results.json). Independently of character evaluation, it forms the full square multiplicity table from all y in each field, checks that table against the character on every field element, and counts affine points by summing multiplicities at f_t(x). It also checks polynomial gcds and adds the two infinity points. These are exact integer/finite-field calculations without a height cutoff or floating-point approximation.

**Frobenius coefficients.** Weil's zeta-function theorem for smooth projective curves gives the genus-two characteristic polynomial X^4-A X^3+B X^2-qA X+q^2, with A=q+1-N1. The sum of the squared Frobenius roots is q^2+1-N2, so Newton's identity gives 2B=A^2-(q^2+1-N2). Substituting the exact counts yields the four stated polynomials. The identity

\[
X^2 P_t(X+q/X)=X^4-A X^3+B X^2-qA X+q^2
\]

gives the two-trace polynomial in the source's convention. The reductions modulo 7 agree with equation (38).

**All resultants.** For P=T^2+aT+b, the resultants with T and T^2 are b and b^2. With T-k the resultant is P(k). For H=T^2+cT+d, put u=c-a and v=d-b. Since H-P=uT+v, the root-product formula gives

\[
\operatorname{Res}(P,H)=v^2-a u v+b u^2.
\]

Applying these formulas to the four integral P_t gives the following integral matrix before reduction:

\[
\begin{pmatrix}
-1&1&-9&29&1&19\\
11&121&1004&764&-1&-4\\
11&121&-1&29&29&71\\
-25&625&-421&401&-31&-25
\end{pmatrix}.
\]

Its reduction is the claimed matrix. The reproducer checks the same entries by Sylvester determinants over F_7 and by exact rational Gaussian elimination over Q. Multiplicities are preserved, including H_2=T^2; no squarefree or irreducibility premise about the comparison polynomials is used. For polynomials with nonzero leading coefficients over a field, a nonzero resultant is equivalent to no common root over its algebraic closure. This proves the finite separation and matches equations (39)–(40).

**Threshold and remaining gap.** The prior SPECIALIZE assessment authorizes this computation as reproduction of a load-bearing claim in an unverified source argument. Every displayed arithmetic check passes. Completeness of the six-factor comparison family, applicability of the four-parameter reduction, the pure-field exclusions, and the original signed descent remain unproved in the notebook. A nonzero finite resultant becomes a global contradiction only after the appropriate common-root relation and exhaustion are justified. This computation supplies neither, and cannot establish the required zero-solution threshold for (3,5,7) or for Beal.

## Mathlib

Coverage of the full finite certificate: **not checked**. Supporting finite-field, hyperelliptic, Frobenius and resultant declarations: **not checked**. The named zeta-function theorem supports the point-count-to-Frobenius passage; [Chocian, arXiv:2609.26996v1, Section 6.2](https://arxiv.org/html/2609.26996v1) matches the four reductions and 24 entries, not the independently unresolved exhaustion claim. No matching Mathlib theorem or formal verification is claimed.
