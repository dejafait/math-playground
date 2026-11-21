# Lemma 813: known order-five nonnegativity in the actual normalization

## Hypotheses

Use the actual Riemann completion xi and Xi from L018 and the globally
convergent moment expansion of L021, with K as defined in L019. Use only
the ordinary-coefficient and minor conventions of L776:

\[
 G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
     =\sum_{n\ge0}a_nw^n,\qquad
 a_n=\frac{M_{2n}}{8\,4^n(2n)!},\qquad
 D_{(5,4)}=\det[a_{4+j-i}]_{i,j=0}^4.
\]

The square-root expression denotes its entire series, independent of
the square-root choice by xi's reflection symmetry. No radius, zero
count, Fredholm norm, simplicity, RH or coefficient-minor sign is assumed.

## Conclusion

For this actual G, D_(5,4)>=0. This is an application of a known
finite-order coefficient theorem, not a new sign theorem. Strict
positivity, a quantitative margin, all-degree mixed positivity and RH
are not established here.

## Proof

**Precise imported result and qualification.** Olga M. Katkova,
*Multiple positivity and the Riemann zeta-function*, Comput. Methods
Funct. Theory **7** (2007), 13–31,
DOI [10.1007/BF03321628](https://doi.org/10.1007/BF03321628).
Numbering and inspected evidence here bind to
[arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
(2)–(6), pp.2–3, Definition 2/(8), p.4, and Theorem B and
Theorem 1 with its complete short proof, pp.5–6. The journal text and
the separately located author revision are not presumed inspected.

The source uses exactly the completion of L018 and defines ordinary
coefficients b_n by

\[
 \xi_1(z)=\xi(1/2+\sqrt z)=\sum_{n\ge0}b_nz^n.
\]

Its PF_m convention is nonnegativity of every minor of order at most m
of the upper Toeplitz matrix T(b)_(p,q)=b_(q-p), p,q>=0, with b_h=0
for h<0. In particular PF_m does not assert strict positivity.

We import only the order-five consequence of Theorem 1. The statement
prints PF44, but its proof prints a zero-free sector |arg z|<43*pi/44,
while Theorem B's sufficient sector for PF_m is |arg z|<m*pi/(m+1).
Thus we do not use the printed maximal-order PF44 inference. For m=5,
5*pi/6<43*pi/44, so the required sector is strictly contained in the
sector actually supplied by that proof. The same proof's positive
constant, genus-zero product and compact polynomial limit give its
order-five consequence without using the mismatched endpoint. These
are cited source inputs; no new zero-free sector, product theorem or
maximal-order correction is asserted. In taking the real polynomial
truncations in this cited argument one may group conjugate zero pairs;
this preserves their stated sector and compact product limit. Thus
the lower-order application does not require a nonreal polynomial
version of Theorem B. The imported conclusion needed below is b in PF5.

**Entire-function and coefficient normalization.** L018 gives
Xi(z)=xi(1/2+iz). Substitute z=-i*sqrt(w)/2 into L021's entire series.
For each integer n>=0, the two factors (-1)^n multiply to +1, giving

\[
 G(w)=\frac18\sum_{n\ge0}\frac{M_{2n}}{(2n)!}
                         \left(\frac w4\right)^n
     =\frac18\xi_1(w/4).
\]

All series converge on every bounded w-disk by L021's global absolute
convergence. Equivalently the even power series of xi at 1/2 gives
b_n=M_(2n)/(2n)! and therefore

\[
 a_n=\frac{b_n}{8\,4^n}\quad(n\ge0).
\]

Both b_n and a_n are ordinary Taylor coefficients, not derivatives or
exponential generating coefficients. In particular no factorial is
removed in the use of PF5.

**Increasing indices and positive scaling.** Select rows p=0,1,2,3,4
and columns q=4,5,6,7,8 of T(b), in those increasing orders. The
resulting matrix B has entries B_(i,j)=b_(4+j-i), 0<=i,j<=4. Its
smallest coefficient index is 0 and its largest is 8. Hence PF5 gives
det B>=0, with no row or column reversal and no determinant sign.

Let U=diag(4^0,4^1,4^2,4^3,4^4) and let
A=[a_(4+j-i)]_(i,j=0)^4. Entrywise the preceding coefficient identity is

\[
 A=8^{-1}4^{-4}UBU^{-1}.
\]

Taking determinants retains all constant and geometric factors:

\[
 D_{(5,4)}=\det A
 =8^{-5}4^{-20}\det B\ge0.
\]

Indeed the powers 4^(sum i) and 4^(-sum j) cancel since both sums
are 0+1+2+3+4=10; the remaining factor is strictly positive.
This completes the applicability argument.

The generic negative minor in L772, the strict order-three input in
L786, and the Jensen/preserver obstructions in L792/C792a/b are
comparisons only, not mathematical premises. This result excludes a
negative-minor search for this actual cell. It does not supply signed
compensation, a strict margin, a degree-uniform bridge or the missing
initial, edge and shifted/mixed regimes. No numerical determinant
calculation or mathematical script is used.

## Mathlib

Full matching coverage is not checked. No claim of presence or absence
of a Mathlib theorem for Katkova's finite-order coefficient result or
this actual minor is made. The informal input is the precisely cited
primary result, with the conservative order and normalization above.
