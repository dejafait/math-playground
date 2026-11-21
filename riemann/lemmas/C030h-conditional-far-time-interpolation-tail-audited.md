# Corollary C030h: conditional far-time interpolation-tail audit

## Hypotheses

Let \(N\ge1\) be an integer and let \(\tau>0\). A spectrum is a
multiset of occurrences \((\gamma,a)\), where \(\gamma>0\) and
\(a\in\mathbb C\). All counts and sums below count occurrences,
including multiplicity. Conjugation
\((\gamma,a)\mapsto(\gamma,\overline a)\) preserves this multiset.
Assume, for every occurrence,

\[
 \operatorname{Re}a\ge\gamma^2-\tfrac14,\qquad
 |a|\le\gamma^2+\tfrac14.
\]

Let \(T\ge\max(1000,150N)\), and assume that \(a\) is positive real
for every occurrence with \(\gamma\le T\). Assume the exact bound

\[
 N_*(r):=\#\{(\gamma,a):\gamma\le r\}\le r^2
 \quad\text{for every real }r\ge T.
\]

There are \(N\) selected occurrences with distinct positive real
exponents \(a_j\), labeled so that

\[
 10000<a_j\le D_N:=22500N^2,\qquad
 |a_j-a_l|\ge10000|j-l|\quad(j\ne l).
\]

Retain all the following threshold assumptions:

\[
 \tau T^2\ge4N,\qquad
 \Delta:=T^2-D_N-\tfrac14>0,\qquad
 \rho_N(T,\tau)<1,
\]

where

\[
 S_N=\sum_{j=1}^N\frac1{((j-1)!(N-j)!)^2}
     =\frac{\binom{2N-2}{N-1}}{((N-1)!)^2},\qquad
 \rho_N(T,u)=\frac4{10000}
       \left(\frac3{10000}\right)^{2N-2}
       S_N T^{4N}e^{-\Delta u}.
\]

No relation \(a=\gamma^2\) is required outside these hypotheses.
In particular, this is a conditional general-spectrum statement,
not a certification that the actual zeta spectrum satisfies the
node or count assumptions at any given cutoff.

## Conclusion

For every \(\epsilon\in\{0,1\}\), \(t\ge\tau\), and nonzero
\(P\in\mathbb R[X]\) of degree less than \(N\), put

\[
 L_\epsilon(P,t)=
 \sum_{j=1}^N a_j^\epsilon e^{-a_jt}P(a_j)^2.
\]

Then \(L_\epsilon(P,t)>0\), all spectral sums in this conclusion
converge absolutely, and

\[
 \frac{\displaystyle\sum_{\gamma>T}
       |a^\epsilon e^{-at}P(a)^2|}{L_\epsilon(P,t)}
 \le B_\epsilon(t):=
 2^{\epsilon+1}10000^{-\epsilon}
 \left(\frac3{10000}\right)^{2N-2}
 S_N T^{4N-2+2\epsilon}e^{-\Delta t}
 \le \rho_N(T,\tau)<1.                                      \tag{1}
\]

The full form is real and satisfies

\[
 \sum_{(\gamma,a)}a^\epsilon e^{-at}P(a)^2
 \ge (1-\rho_N(T,\tau))L_\epsilon(P,t)>0.                    \tag{2}
\]

Consequently both real symmetric matrices

\[
 \left[\sum_{(\gamma,a)}
        a^{r+s+\epsilon}e^{-at}\right]_{0\le r,s<N}
\]

are positive definite. For \(P=0\) the form is zero. The squares
in the full form are algebraic squares; absolute values in (1)
only estimate the tail.

## Proof

### Source and reason for replay

This is a reproduction of Nicholas G. Polson, *On Hilbert's 8th
Problem*, [arXiv:1708.02653v24, 11 September 2026,
Lemma 7.9 and equation (28), printed p21](https://arxiv.org/pdf/1708.02653v24#page=21).
The full lemma and proof were inspected in source coverage1194
and checked against the replay below in audit1195. The purpose is
to validate this conditional source input used within C030b's
imported finite-block theorem, especially its cutoff, weights and
parity constants. It is not a new positivity theorem beyond that
source.

Import the polynomial Lagrange interpolation identity at distinct
nodes from [NIST DLMF 3.3(i), equation (3.3.1)](https://dlmf.nist.gov/3.3#i),
specialized to \(N\) real nodes and degree at most \(N-1\).
Use weighted finite-dimensional Cauchy-Schwarz. For the scalar
integral below import [DLMF 8.2.2](https://dlmf.nist.gov/8.2.E2)
and the integer upper-incomplete-gamma identity
[DLMF 8.4.8](https://dlmf.nist.gov/8.4.E8), with the finite sum
defined in [DLMF 8.4.11](https://dlmf.nist.gov/8.4.E11).
Its arguments here are positive real and its index is a
nonnegative integer. The finite counting integration argument
is written explicitly because arbitrary real ordinates, strict
cutoffs and multiplicities must be checked; an integer-index
Abel formula does not by itself establish that step.

### Convergence and selected occurrences

For every fixed integer \(k\ge0\) and real \(t>0\),
\(\sum |a|^k e^{-t\operatorname{Re}a}<\infty\).
Indeed, \(N_*(T)\le T^2\) makes the low sum finite. Set
\(n_0=\lceil T\rceil\); the occurrences through \(n_0\) are
also finite. For integers \(n\ge n_0\), the contribution from
\(n<\gamma\le n+1\) is at most

\[
 (n+1)^2\big((n+1)^2+\tfrac14\big)^k
       e^{t/4-tn^2}.
\]

The series of these bounds converges: its polynomial prefactor
has bounded successive ratio for large \(n\), whereas the
successive exponential ratio is \(e^{-t(2n+1)}\to0\).
Every polynomial expression under consideration is a finite
linear combination of these absolutely summable moments.
This proves entrywise and quadratic-form absolute convergence
before any regrouping.

The selected occurrence of \(a_j\), with ordinate \(\gamma_j\),
satisfies \(\gamma_j^2\le a_j+1/4\le D_N+1/4<T^2\).
Thus all selected occurrences belong to the low part. One
occurrence is selected for each distinct \(a_j\); other copies
remain in the spectrum. Their weights
\(w_j=a_j^\epsilon e^{-a_jt}\) are positive. If
\(L_\epsilon(P,t)=0\), then \(P(a_j)=0\) for all \(j\).
A polynomial of degree less than \(N\) vanishing at these
\(N\) distinct nodes is zero, a contradiction. Hence division
by \(L_\epsilon(P,t)\) below is legitimate.

### Interpolation bound with both weights

Write

\[
 \ell_j(z)=\prod_{l\ne j}\frac{z-a_l}{a_j-a_l},
 \qquad P(z)=\sum_{j=1}^N P(a_j)\ell_j(z).
\]

Cauchy-Schwarz applied to
\(\sqrt{w_j}P(a_j)\) and \(\ell_j(z)/\sqrt{w_j}\) gives

\[
 |P(z)|^2\le L_\epsilon(P,t)
       \sum_{j=1}^N a_j^{-\epsilon}e^{a_jt}|\ell_j(z)|^2.
                                                               \tag{3}
\]

For an occurrence with \(\gamma>T\),

\[
 |a-a_l|\le |a|+a_l\le\gamma^2+\tfrac14+D_N<3\gamma^2.
\]

The separation hypothesis gives

\[
 \prod_{l\ne j}|a_j-a_l|
 \ge10000^{N-1}\prod_{l\ne j}|j-l|
 =10000^{N-1}(j-1)!(N-j)!.
\]

Therefore

\[
 |\ell_j(a)|\le
 \frac{(3\gamma^2/10000)^{N-1}}{(j-1)!(N-j)!}.
\]

Since \(a_j^{-\epsilon}\le10000^{-\epsilon}\) and
\(e^{a_jt}\le e^{D_Nt}\), (3) implies

\[
 \frac{|P(a)|^2}{L_\epsilon(P,t)}
 \le10000^{-\epsilon}e^{D_Nt}
       \left(\frac3{10000}\right)^{2N-2}
       S_N\gamma^{4N-4}.                                    \tag{4}
\]

For completeness, the stated closed form for \(S_N\) follows
by multiplying its sum by \(((N-1)!)^2\), obtaining
\(\sum_{k=0}^{N-1}\binom{N-1}{k}^2
 =\binom{2N-2}{N-1}\), the coefficient of \(x^{N-1}\)
in \((1+x)^{N-1}(1+x)^{N-1}\).

### Strict-tail counting estimate

Set \(m=2N-2+\epsilon\), so \(0\le m\le2N-1\), and
\(f(r)=r^{2m}e^{-tr^2}\). Since
\(tT^2\ge\tau T^2\ge4N>m\), \(f\) decreases on
\([T,\infty)\), and

\[
 0\le-f'(r)
 =2r^{2m-1}(tr^2-m)e^{-tr^2}
 \le2t r^{2m+1}e^{-tr^2}.                                  \tag{5}
\]

Define \(A(r)=N_*(r)-N_*(T)\) for \(r\ge T\). This counts
exactly \(T<\gamma\le r\), has \(A(T)=0\), and obeys
\(0\le A(r)\le r^2\). For every \(R>T\), finite summation of
\(f(\gamma)=f(R)+\int_\gamma^R(-f'(r))\,dr\) yields the exact
identity

\[
 \sum_{T<\gamma\le R}f(\gamma)
 =A(R)f(R)+\int_T^R A(r)(-f'(r))\,dr.                       \tag{6}
\]

The finite identity includes an occurrence at \(R\), whose
integral is zero, and counts repeated occurrences separately.
An occurrence at \(T\) is excluded from both sides.
The boundary term tends to zero since
\(0\le A(R)f(R)\le R^{2m+2}e^{-tR^2}\to0\).
The integrand is nonnegative. Taking the increasing limit in
the integral and the sum in (6), and then using (5), gives

\[
 \sum_{\gamma>T}\gamma^{2m}e^{-t\gamma^2}
 \le2t\int_T^\infty r^{2m+3}e^{-tr^2}\,dr.                 \tag{7}
\]

This proves the required counting step without assuming
integer ordinates, absence of a cutoff atom, or simplicity.

Put \(x=tT^2>0\). The substitution \(u=tr^2\) and the cited
integer gamma formula give

\[
 \begin{split}
 2t\int_T^\infty r^{2m+3}e^{-tr^2}\,dr
 &=t^{-(m+1)}\Gamma(m+2,x)\\
 &=e^{-x}\sum_{j=0}^{m+1}
       \frac{(m+1)!}{(m+1-j)!}
       T^{2(m+1-j)}t^{-j}.
 \end{split}                                               \tag{8}
\]

If \(b_j\) denotes the \(j\)-th summand without \(e^{-x}\),
then, for \(0\le j\le m\),

\[
 \frac{b_{j+1}}{b_j}=\frac{m+1-j}{tT^2}
 \le\frac{2N}{4N}=\tfrac12,\qquad b_0=T^{2m+2}.
\]

The finite geometric sum is at most \(2b_0\). Thus (7)-(8)
prove

\[
 \sum_{\gamma>T}\gamma^{2m}e^{-t\gamma^2}
 \le2T^{2m+2}e^{-tT^2}.                                   \tag{9}
\]

### Tail ratio, parity comparison and positivity

For \(\gamma>T\ge1000\), the strip bounds imply

\[
 |a|^\epsilon\le2^\epsilon\gamma^{2\epsilon},
 \qquad |e^{-at}|\le e^{t/4}e^{-t\gamma^2}.
\]

Also \(|P(a)^2|=|P(a)|^2\), an equality used only for the
absolute estimate. Multiplying (4) by these bounds and summing,
then applying (9) with \(m=2N-2+\epsilon\), proves
the first inequality of (1), because \(2m+2=4N-2+2\epsilon\).

All constants are positive, and

\[
 B_1(t)=\rho_N(T,t),\qquad
 \frac{B_0(t)}{B_1(t)}=\frac{5000}{T^2}\le\frac1{200}<1.
\]

Since \(\Delta>0\), \(\rho_N(T,t)\) decreases for \(t\ge\tau\).
This proves the rest of (1). When \(N=1\), the interpolation
product is empty, \(0!=1\), \(S_1=1\), and \(m=\epsilon\).
In particular \(m+1\le2\) and \(tT^2\ge4\), so the same
factorial and geometric estimates apply to both parities.
There is no separate unproved base case.

Absolute convergence and conjugation invariance imply that the
full form and its high part are real: the term for
\((\gamma,\overline a)\) is the conjugate of the term for
\((\gamma,a)\), because \(t\) and the coefficients of \(P\)
are real. Every low occurrence is positive real and
contributes \(a^\epsilon e^{-at}P(a)^2\ge0\).
After removing the selected occurrences, all remaining low
terms are still nonnegative, including multiplicity copies.
The real high part is at least minus its absolute sum.
Consequently the full form is at least
\(L_\epsilon(P,t)-B_\epsilon(t)L_\epsilon(P,t)\), which
proves (2).

Expanding the finite polynomial square and using absolute
convergence identifies the full form with the displayed
matrix quadratic form on the real coefficient vector.
Conjugation gives real entries, and the index \(r+s+\epsilon\)
gives symmetry. Every nonzero vector corresponds to a nonzero
polynomial of degree less than \(N\); (2) proves positive
definiteness.

### Scope of the passed audit

The conditional estimate (28), its two parity-specific bounds,
and its strict-positivity inference pass this replay for every
\(N\ge1\). No source inequality in this delimited proof failed.
This validates one source input locally; it adds no result
beyond the cited preprint. Lemma 7.8's actual-node existence,
the actual-zero count (13), Theorem 7.4's joining constants,
and the external finite line verification are separate inputs
not certified here. C030b's entire source proof is therefore
not declared independently checked. The missing all-degree
actual-Xi positivity, actual-theta signing and graph
realization remain unresolved.

## Mathlib

Full matching coverage for this conditional general-spectrum
statement is unchecked. The supporting
[Mathlib.NumberTheory.AbelSummation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/AbelSummation.html)
theorem sum_mul_eq_sub_sub_integral_mul concerns a natural-number
coefficient sequence under its differentiability and
integrability hypotheses. It is not a matching theorem for
arbitrary real ordinate locations in (6). The finite identity
and its limit have been proved above instead. Lagrange,
Cauchy-Schwarz and incomplete gamma are named informal inputs;
no formal verification or claim of Mathlib absence is made.
