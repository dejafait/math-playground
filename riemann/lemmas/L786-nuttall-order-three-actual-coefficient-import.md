# Lemma 786: known strict order-three sign in the actual normalization

## Hypotheses

Use the actual theta kernel K of L019, the moments M_(2n) of L021,
and only the ordinary-coefficient definition from L776:

\[
 G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
 =\sum_{n\ge0}a_nw^n,\quad
 a_n=\frac{M_{2n}}{8\,4^n(2n)!},\quad
 M_{2n}=\int_0^\infty u^{2n}K(u)\,du.
\]

The square-root expression means its entire series. No radius, zero
count, root grouping, boundary nonvanishing or Fredholm hypothesis from
L776 is assumed. Set D_(3,2)=det[a_(2+j-i)]_(i,j=0)^2.

## Conclusion

For this actual G, D_(3,2)>0, by Nuttall's Theorem 2.3. This is a
known-result import, not a new sign theorem. It makes no assertion about
other indices, growing orders, root grouping, a Fredholm norm threshold
or RH.

## Proof

**Precise imported result.** John Nuttall, *Wronskians, Cumulants, and
the Riemann Hypothesis*, Constructive Approximation **38** (2013),
193–212, DOI [10.1007/s00365-013-9200-8](https://doi.org/10.1007/s00365-013-9200-8).
Numbering binds to the inspected 16-page
[author copy](https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf),
(1.2)–(1.3), p.1, and Theorem 2.3/(2.9), pp.5–6. For integer n>=2,
the theorem states

\[
 \det[\beta_{n+j-i}]_{i,j=0}^2>0,\qquad
 \beta_n=\frac1{(2n)!}\int_0^\infty\Phi(t)t^{2n}\,dt,
\]
\[
 \Phi(t)=\sum_{m\ge1}(2\pi^2m^4e^{9t}-3\pi m^2e^{5t})
 e^{-\pi m^2e^{4t}}.
\]

We import this coefficient theorem without reproving its reverse
regularity input or claiming an independent full Section 3 audit.
The prior ready assessment is
`drafts/literature/2026-11-05-nuttall-order-three-import.md`.

**Exact normalization.** Comparing Phi's series with L019 gives
K(u)=4 Phi(u/2): its coefficients become 8 pi^2 m^4 and -12 pi m^2,
and the exponential arguments become 9u/2, 5u/2 and -pi m^2 e^(2u).
The series converge for u>=0 by L019. Substitute u=2t to obtain

\[
 M_{2n}=\int_0^\infty (2t)^{2n}4\Phi(t)\,2\,dt
       =8\,4^n\int_0^\infty t^{2n}\Phi(t)\,dt.
\]

Hence a_n=beta_n exactly, including n=0. The kernel factor 4,
Jacobian 2, power 4^n and factorial (2n)! are retained. No constant
or geometric rescaling remains. These are ordinary coefficients,
not derivatives with omitted factorials. L019's superexponential decay
ensures absolute convergence of every integral used in the substitution.

**Index and orientation.** At n=2 the source matrix is exactly

\[
 \begin{pmatrix}
 \beta_2&\beta_3&\beta_4\\
 \beta_1&\beta_2&\beta_3\\
 \beta_0&\beta_1&\beta_2
 \end{pmatrix}=[a_{2+j-i}]_{i,j=0}^2.
\]

No reversal is needed in this identification. The source already
includes its reversal sign in (2.9). Its smallest Mellin parameter
n-3/2 is 1/2>0 at n=2, so this endpoint satisfies the stated hypotheses.
Remark 2.4's separate numerical discussion at n=1 is unused.
Theorem 2.3 gives the required strict inequality.

Only applicability is newly recorded here. The stopped pointwise
product and reciprocal-duality mechanisms are not sign premises;
their obstructions remain unaffected.

## Mathlib

Full matching coverage is not checked. No Mathlib theorem for this
specific theta coefficient determinant is asserted or used. Supporting
determinant and integration results do not supply its sign.
