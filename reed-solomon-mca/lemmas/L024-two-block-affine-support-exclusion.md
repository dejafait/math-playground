# L024 — L023's two-block family has no affine-moment realization

## Hypotheses

Let F be a finite field containing a multiplicative subgroup H of order
sixteen, and let C be the degree-less-than-eight evaluation code on H.
Use the moments and affine pencil of L010:
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^j,\qquad
 s(T)=\sigma(a)+T\sigma(b)\in F[T]^8,
 \quad 1\le j\le8,
\]
where a,b are arbitrary words in F^H. Assume L010's nonzero-polynomial
hypotheses for D and every coordinate locator.

Let V={0,1}×(Z/8Z), A={0,1,2,4}, and
E_(i,t)={i}×(A+t), as in L023. Suppose there is a bijection
lambda:V -> H and sixteen pairwise distinct finite parameters
gamma_(i,t) in F. At each parameter suppose there is a word e_(i,t)
such that
\[
 \operatorname{supp}(e_{i,t})=\lambda(E_{i,t}),\qquad
 \sigma(e_{i,t})=s(\gamma_{i,t}).                         \tag{1}
\]
The support equality requires all four indicated weights to be nonzero.
In particular, (1) holds if these are the error representatives of the
sixteen bad parameters in an equality pencil of L010.

## Conclusion

These hypothetical realization data cannot exist, for any bijection
lambda and any allowed field F. Consequently L023's precise family
cannot be the sixteen full-weight error supports in L010's equality case.

This excludes one abstract support family, not all balanced support
families of matching number two. It gives no global fifteen-count bound,
no reduction to L022's fixed triple, and no challenge-level resolution.

## Proof

For i in {0,1}, put B_i=lambda({i}×(Z/8Z)). These are disjoint
eight-coordinate blocks. Fix any ordering of B_i and let
\[
 M_i=(x^j)_{1\le j\le8,\ x\in B_i}.
\]
L010 proves that any eight columns of this moment matrix are invertible,
using distinct nonzero coordinate labels. Apply that established fact to
B_i; it applies to every bijection under consideration. Define
\[
 u_i(T)=M_i^{-1}s(T)\in F[T]^{B_i}.                      \tag{2}
\]
Every coordinate of u_i is a polynomial of degree at most one, because
M_i^{-1} is constant and s is affine. Equation (2) is defined for all T,
without requiring a sparse representative at every parameter.

At gamma_(i,t), the word e_(i,t) vanishes outside B_i. Therefore (1)
gives M_i(e_(i,t)|_(B_i))=s(gamma_(i,t)). Invertibility implies
\[
 u_i(\gamma_{i,t})=e_{i,t}|_{B_i}.                      \tag{3}
\]
This uses only parameters assigned to block i. No identification with
the actual error at a parameter assigned to the other block is made.

Fix x=lambda(i,v) in B_i. L023 establishes that v belongs to exactly
four of the eight sets A+t. Thus there are four distinct parameters
gamma_(i,t) at which x is absent from the support in (1). By (3), the
affine polynomial u_(i,x)(T) vanishes at all four. In particular, if it
is written alpha+beta*T, vanishing at two distinct parameters yields
beta=0 by subtraction and then alpha=0. Hence u_(i,x) is identically
zero, including the case where it was zero from the outset.

But x belongs to four other prescribed supports. Choose any such t.
The full-weight requirement and (3) give
u_(i,x)(gamma_(i,t))=e_(i,t)(x) != 0, a contradiction. This already
occurs in either block. All sixteen parameters being distinct ensures
the distinctness needed inside each block.

The proof is an affine-support specialization of L010's established
moment invertibility and L023's incidence, not a reproof of RS distance.
For the underlying standard distance input, the inspected primary
reference is J. I. Hall, *Notes on Coding Theory*, GRS chapter,
Theorem 5.1.1, printed pp. 63–64, undated author-hosted copy retrieved
2026-10-05 ([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)).
Its distinct evaluation points, nonzero multipliers, and 0<k<=n
hypotheses specialize here to H, multipliers one, and k=8,n=16,
giving distance nine over every allowed F. No stronger conclusion
about support patterns is imported from that theorem. The additional
affine lift and zero-pattern passage is supplied in (2)–(3) above.

The contradiction does not use locator nonvanishing or D values beyond
the stated equality setting. It therefore has no singular-parameter
exception under the hypotheses. No affine lift of codewords is assumed:
(2) is a linear inverse for error coordinates on a fixed block. No
numerical test, coordinate normalization, or prime-field restriction is
used. The kernel/error correspondence needed to apply this obstruction
to an actual pencil is precisely the one already proved in L010.

## Mathlib

Coverage of this exact two-block exclusion and its supporting affine
linear algebra in Mathlib is **not checked**. No matching theorem name,
absence claim, or Lean verification is asserted. The local result is
the displayed specialization; the source assessment did not establish
coverage of the full obstruction and does not certify originality.
