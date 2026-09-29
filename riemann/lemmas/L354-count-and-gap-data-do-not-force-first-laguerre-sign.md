# Lemma 354: the counting law and small real gaps do not force the first Laguerre sign

**Hypotheses.** For a real entire function F put
D_1(F;x)=F'(x)^2−F(x)F''(x). Count zeros with multiplicity by

\[
 N_F(T)=\#\{\rho:F(\rho)=0,\ 0<\operatorname{Re}\rho\le T\}.
\]

The count here concerns positive real part, not positive imaginary
part or modulus. Define the increasing counting main term

\[
 M(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi},
 \qquad t\ge 2\pi e.
\]

**Conclusion.** There is a real even canonical product F of order
exactly one, with F(0)=1, such that

\[
 N_F(T)=M(T)+O(1).
\]

All its zeros are simple. Except for exactly one quartet
±(A±ib), with A>40 and 0<b<1/4, they are real and have absolute
value greater than 4. Its consecutive positive real zeros t_n obey

\[
 t_{n+1}-t_n\le \frac{2\pi}{\log(t_n/(2\pi))}
             =O(1/\log t_n).
\]

Nevertheless F(A)≠0 and

\[
 \frac{D_1(F;A)}{F(A)^2}<-31.
\]

Thus even the O(1) counting remainder, stronger than the requested
O(log T), and these eventual real-gap bounds do not imply the first
Laguerre inequality. This is a counterexample to that implication,
not to RH. A positive Fourier kernel, theta transformation, Euler
product, or all of zeta's finer zero statistics is not asserted.

**Proof.** We specialize standard product and first-sign theorems;
their general proofs are not repeated. The prescribed-zero product
theorems are Laine, Nevanlinna Theory and Complex Differential
Equations (1993), §1.2, Theorems 1.2.3–1.2.4, pp. 7–8, with the
order remark and equations (1.2.6)–(1.2.7) immediately following
([publisher preview](https://api.pageplace.de/preview/DT0400.9783110863147_A19976604/preview-9783110863147_A19976604.pdf)).
The canonical-product order statement is also the named Borel
order theorem, Theorem 4.7.14, p. 174, in
[HKUST MATH5030 Chapter 4](https://www.math.hkust.edu.hk/~machiang/5030/notes/Chap4.pdf).
The local sign identity is Csordás, Fourier transforms of positive
definite kernels and the Riemann ξ-Function,
[arXiv:1309.0055v2, Proposition 2.2, equation (2.3), and Proposition 2.3, pp. 3–4](https://arxiv.org/pdf/1309.0055v2).
The following checks supply the joint hypotheses left open by the
saved literature assessment.

Since M(2πe)=0, M tends to infinity, and

\[
 M'(t)=\frac{1}{2\pi}\log\frac{t}{2\pi}>0,
 \qquad M''(t)=\frac{1}{2\pi t}>0,
\]

there is a unique t_n>2πe with M(t_n)=n for every integer n≥1.
They are strictly increasing and tend to infinity. Their positive
count is exactly floor(M(T)) for T≥2πe. Also

\[
 1=\int_{t_n}^{t_{n+1}}M'(t)\,dt
   \ge M'(t_n)(t_{n+1}-t_n),
\]

which proves the displayed gap bound. Eventually
log(t_n/(2π))≥(1/2)log t_n, so its implied constant may be taken
as 4π.

The count floor(M(T)) is O(T log T). Splitting into dyadic intervals
therefore proves sum_n t_n^(-q)<∞ for every q>1: the tail is
bounded by a constant times sum_k (k+1)2^((1−q)k).
On the other hand,

\[
 \sum_{t_n\le T}\frac1{t_n}
 \ge \frac{\lfloor M(T)\rfloor}{T}\longrightarrow\infty.
\]

Thus the zero convergence exponent is exactly one, and the least
canonical genus is one. With E_1(w)=(1−w)e^w, the standard product
theorem applies to the sequence ±t_n. Pairing is legitimate because
the genus-one factors converge absolutely and locally uniformly in
the tail. It gives

\[
 H(z)=\prod_{n\ge1}E_1(z/t_n)E_1(-z/t_n)
     =\prod_{n\ge1}(1-z^2/t_n^2).
\]

The product is even, real entire, nonzero at zero, and has exactly
the simple zeros ±t_n. Borel's order theorem gives order exactly
one; finite exponential type is neither assumed nor needed.

Choose an integer m≥1 with m>M(40), and put
A=(t_m+t_{m+1})/2. Then A>40 and H(A)≠0. Define, before choosing b,

\[
 S_A=\sum_{n\ge1}
       \left(\frac1{(A-t_n)^2}+\frac1{(A+t_n)^2}\right).
\]

This is positive and finite. None of its denominators is zero;
for t_n>2A each summand is at most 5/t_n², and the remaining
head is finite. In particular S_A is independent of b. Set

\[
 b=(S_A+16)^{-1/2},\qquad
 P_b(z)=\frac{((z-A)^2+b^2)((z+A)^2+b^2)}{(A^2+b^2)^2},
 \qquad F(z)=P_b(z)H(z).
\]

Then 0<b<1/4. The four distinct zeros of P_b are ±(A±ib), so
they do not coincide with any real zero. For α=A+ib the identity

\[
 P_b(z)=(1-z^2/\alpha^2)(1-z^2/\overline{\alpha}^{\,2})
\]

exhibits P_b as the paired genus-one factors for this quartet.
Consequently F itself is the canonical genus-one product for the
enlarged sequence, with F(0)=1. Its convergence exponent, and hence
order by the cited theorem, remains one. Its real zero sequence and
its gaps are unchanged. Exactly two inserted zeros have positive
real part, both equal to A. Hence, for every T≥2πe,

\[
 N_F(T)=\lfloor M(T)\rfloor+2\,\mathbf1_{\{T\ge A\}},
\]

which proves the claimed stronger counting remainder. All real
zeros have modulus greater than 2πe>4. Finally
P_b(A)=b²(4A²+b²)/(A²+b²)²>0, so F(A)≠0.

Apply the cited reciprocal-square identity to this canonical
product, with no quadratic exponential factor. Its real-zero sum
converges as checked above. On a sufficiently small complex
neighborhood of A avoiding the zeros, its tail also has a uniform
constant multiple of sum_n t_n^(-2) as majorant, so this use
introduces no unlicensed differentiation of an infinite sum.
The identity gives exactly

\[
 \frac{D_1(F;A)}{F(A)^2}
 = S_A-\frac{2}{b^2}
       +\frac{2(4A^2-b^2)}{(4A^2+b^2)^2}.
\]

The last term R_b is the reflected pair's contribution. It has
not been held fixed while b varies. Uniformly for 0<b<1/4 and
A>40,

\[
 0<R_b<\frac{1}{2A^2}<1.
\]

Indeed 4A²>b², its numerator is less than 8A², and its denominator
is greater than 16A⁴. Our choice of b therefore gives

\[
 S_A-\frac{2}{b^2}+R_b
 =-S_A-32+R_b<-31,
\]

as required. This verifies the symmetric specialization directly;
it does not misapply Proposition 2.3's fixed-background conclusion
to the b-dependent reflected factor. ∎

The achieved sign is strictly below zero, whereas a compensation
certificate would require nonnegativity at every exterior center.
The selected count and gap inputs therefore cannot supply even
that first sign in this function class. Actual-theta first positivity,
the remaining low-index signs in L320, and the endpoint arithmetic
margin are still unresolved. L251 and L264 provide different
countermodels; neither is a mathematical input to this construction.

This is a reproduction/specialization of the cited classical
mechanism with simultaneous count, gap and symmetry checks. The
prior search did not locate the full statement, but no mathematical
novelty beyond the checked literature is claimed. The argument is
analytic; no numerical zero finding or computational certificate
is used.

**Mathlib.** Full statement: **not checked**. Supporting
canonical-product existence, Borel order and first Laguerre identity
coverage: **not checked**. The precise named sources and direct links
above are mathematical references, not asserted Mathlib matches.
