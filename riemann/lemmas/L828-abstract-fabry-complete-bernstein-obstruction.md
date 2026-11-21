# L828 — Abstract Fabry obstruction to a complete Bernstein factor

## Hypotheses

Let \(p:\mathbb R\to[0,\infty)\) be an even probability density, real
analytic and strictly positive on a neighborhood of zero. Assume
\[
 \int_{\mathbb R}e^{A|x|}p(x)\,dx<\infty\qquad(A>0).
\]
Write \(p(x)=\sum_{n\ge0}c_nx^{2n}\) near zero and
\(g(y)=\sum_{n\ge0}c_ny^n\). Suppose its Taylor radius is
\(0<R<\infty\), and its sum has holomorphic continuation to a
neighborhood of the positive endpoint \(R\), agreeing with the sum
on the overlap with its disk.

Define
\[
 M(s)=\int_0^\infty x^{2s}p(x)\,dx\quad(\Re s>-1/2),\qquad M(0)=1/2,
 \quad q(s)=2(2s-1)\frac{M(s-1)}{M(s)}\quad(s>1/2).
\]
Assume \(q(as)/q(s)\to a\) for every fixed \(a>0\), \(q(s)\to\infty\),
and \(q(s)/s\to0\) as \(s\to\infty\).

A nonzero complete Bernstein function \(\phi\) is understood in the
standard sense, with killing and drift permitted. Its distinguished
Bernstein-gamma function has normalization
\(W_\phi(1)=1\), \(W_\phi(z+1)=\phi(z)W_\phi(z)\).
Set
\[
 J_{u\phi(u)}(t)=
 \sum_{n\ge0}\frac{(-1)^nt^{2n}}{n!W_\phi(n+1)}.
\]
The identically zero Bernstein function does not define this series
and is not an additional representation case.

## Conclusion

There is no such complete Bernstein function for which
\[
 \int_{\mathbb R}e^{itx}p(x)\,dx=J_{u\phi(u)}(t)
 \qquad(t\in\mathbb R).
\]

This is an independently checked reproduction of bramble_trace,
*A Fabry obstruction to complete Bernstein constructions of the Riemann
xi function*, [paper20 v2, 18 October 2026, Theorem2,
Section2, (3)–(16)](https://rstation.ai/problems/riemann_hypothesis/papers/20),
not a new theorem claim. The audit below supplies the root-zero product
calculation needed because of the recorded KPS parameter-range
inconsistency, and makes the domain and counting cases explicit.
It does not verify paper20 Theorem1's theta specialization, exclude
ordinary Bernstein factors, or establish any Xi zero or mixed sign.

## Proof

Suppose the representation exists.

### 1. Root-zero probability law and the Mellin domain

For a nonzero Bernstein function, use the exponential functional
\(I_\phi=\int_0^\zeta e^{-\xi_t}\,dt\) of the possibly killed
subordinator with Laplace exponent \(\phi\).
Patie–Savov, *Bernstein-gamma functions and exponential functionals of
Lévy processes*, EJP23 (2018), [arXiv:1604.05960v4,
Theorem4.1(1), p22, and Section7.1, pp63–64](https://arxiv.org/pdf/1604.05960v4),
give the distinguished \(W_\phi\), holomorphic and zero-free on
\(\Re z>0\), and
\[
 \mathbb E I_\phi^{z-1}=\frac{\Gamma(z)}{W_\phi(z)}
 \qquad(\Re z>0).
 \tag{1}
\]
The latter identity is displayed in Section7.1 immediately before (7.2),
there attributed to [61, Proposition6.8]. These facts are imported;
uniqueness from integer recurrence data is not asserted.

Take \(A\), independently of \(I_\phi\), with density
\((\pi\sqrt{4-x^2})^{-1}\) on \((-2,2)\), and set
\(Y=\sqrt{I_\phi}A\). Euler's beta integral gives
\[
 \mathbb E|A|^{2s}
 =\frac{4^s\Gamma(s+1/2)}{\sqrt\pi\,\Gamma(s+1)}
 \quad(\Re s>-1/2),\qquad
 \mathbb E A^{2n}=\frac{(2n)!}{(n!)^2}.
 \tag{2}
\]
For example, substitute \(x=2\sqrt v\) in the integral over \(0<x<2\);
the result is \(4^s B(s+1/2,1/2)/\pi\), with absolute convergence
precisely on the stated half-plane.
Independence and (1) at integers yield
\[
 \mathbb E Y^{2n}=\frac{(2n)!}{n!W_\phi(n+1)}.
\]
For every real \(t\), monotone convergence for the nonnegative cosh
series gives
\[
 \mathbb E\cosh(tY)=
 \sum_{n\ge0}\frac{t^{2n}}{n!W_\phi(n+1)}<\infty.
\]
Indeed the ratio of consecutive terms is
\(t^2/((n+1)\phi(n+1))\), bounded by
\(t^2/((n+1)\phi(1))\to0\); a nonzero Bernstein function has
\(\phi(1)>0\) and is nondecreasing. Since
\(e^{|tY|}\le2\cosh(tY)\), the characteristic series is absolutely
integrable. Symmetry now gives
\(\mathbb E e^{itY}=J_{u\phi(u)}(t)\).
Uniqueness of characteristic functions identifies the law with \(p\).

This directly checks the needed root-zero case of Konstantopoulos,
Patie–Sarkar, *A new class of solutions to the van Dantzig problem,
the Lee–Yang property, and the Riemann hypothesis*, AIF74 (2024),
377–421, [Lemma5.8, (5.24)–(5.29), pp412–414](https://www.numdam.org/item/10.5802/aif.3600.pdf).
The extracted lemma says \(\nu\le-1/2\), while the construction's
introductory range and displayed density point to a different endpoint.
No correction of that source text is assumed. The calculation above
establishes the case used here without citing an out-of-range
specialization, and does not import its density-smoothness assertions.

For \(\Re s>0\), equality of laws, (1), (2), and independence give
\[
 \frac{M(s)}{M(0)}
 =\frac{4^s\Gamma(s+1/2)}{\sqrt\pi\,W_\phi(s+1)}.
 \tag{3}
\]
All product integrals are absolutely convergent: use (1) and (2) at
\(\Re s\) to bound their absolute values. Both sides of (3) are
holomorphic on \(\Re s>-1/2\). For \(M\), local boundedness of \(p\)
at zero and the exponential moments supply domination on compact
subsets, including logarithmic factors for derivatives. For the right
side, \(s+1\) has real part greater than \(1/2\), and the gamma factor
has no pole on this domain. The identity theorem therefore extends
(3) to this full half-plane.

For real \(s>1/2\), both \(s\) and \(s-1\) lie in that domain.
The gamma and \(W_\phi\) recurrences in (3) give
\[
 \frac{M(s)}{M(s-1)}
 =\frac{4(s-1/2)}{\phi(s)},\qquad \phi(s)=q(s).
 \tag{4}
\]
This verifies the range needed in the hypotheses, rather than taking
a ratio beyond the initially displayed Mellin identity.
In particular, \(\phi\) is nonconstant, unbounded, sublinear, and
regularly varying with index one.

### 2. Entire continuation and normalization at canceled poles

Fix \(h>0\) within the analytic radius of \(p\). For every integer
\(N\ge0\), Taylor subtraction gives
\[
 \begin{split}
 M(s)={}&\int_h^\infty x^{2s}p(x)\,dx
 +\int_0^h x^{2s}
       \left(p(x)-\sum_{j=0}^N c_jx^{2j}\right)\,dx\\
 &+\sum_{j=0}^N\frac{c_jh^{2s+2j+1}}{2s+2j+1}.
 \end{split}
 \tag{5}
\]
The first integral is entire: on each compact \(s\)-set, its absolute
value and all needed logarithmic factors are dominated by an integrable
exponential weight times \(p\). The second integral is holomorphic for
\(\Re s>-N-3/2\), since its parenthesis is \(O(x^{2N+2})\).
These continuations agree on overlaps. Thus \(M\) is meromorphic on
\(\mathbb C\), with only possible simple poles
\(s_n=-n-1/2\) and residues \(c_n/2\).

Define
\[
 E(s)=\frac{\sqrt\pi\,4^{-s}M(s)}
              {M(0)\Gamma(s+1/2)},\qquad F(z)=E(z-1).
 \tag{6}
\]
The simple zeros of \(1/\Gamma(s+1/2)\) cancel all the possible poles,
so \(E\) and \(F\) are real entire. Equation (3) first identifies
\(F=1/W_\phi\) on \(\Re z>1/2\); the identity theorem extends this
equality to \(\Re z>0\). In particular \(F\) is zero-free there and
\(F(1)=E(0)=1\).
At \(s_n\),
\(1/\Gamma(s+1/2)=(-1)^n n!(s-s_n)+O((s-s_n)^2)\).
Consequently
\[
 c_n=\frac{M(0)(-1)^n}{\sqrt\pi\,4^n n!}E(-n-1/2).
 \tag{7}
\]
This remains valid when \(c_n=0\): then \(M\) has no pole at \(s_n\),
and the reciprocal gamma factor makes \(E(s_n)=0\).

### 3. Meromorphic factor, interlacing, and all integer strings

On \(\Re z>0\) the recurrence gives
\[
 F(z)=\phi(z)F(z+1),\qquad \phi(z)=\frac{F(z)}{F(z+1)}.
 \tag{8}
\]
The quotient of two entire functions, with denominator not identically
zero, continues \(\phi\) meromorphically to the plane. It agrees with
the original function on the slit plane by the identity theorem.
It is real on every real pole-free interval. At zero the denominator
is \(F(1)=1\), so there is no pole.

We may now apply Chorbadzhiyska–Minchev–Savov,
*Asymptotics for Beta-Splitting Trees via Homogeneous Fragmentations
and Meromorphic Potential Theory*, [arXiv:2608.18320,
AppendixA, LemmaA.1 and proof, pp30–31](https://arxiv.org/pdf/2608.18320).
Its hypotheses are a nonconstant complete Bernstein function with
meromorphic continuation to the plane, both now verified.
It gives a locally uniform atomic representation
\[
 \phi(z)=\gamma+\beta z+
 \sum_j B_j\left(\frac1{b_j}-\frac1{z+b_j}\right),
 \quad \gamma,\beta\ge0,\quad B_j>0,\quad
 \sum_j B_j/b_j^2<\infty,
 \tag{9}
\]
where \(0<b_1<b_2<\cdots\), and an infinite pole sequence tends to
infinity. It also gives simple real poles, simple real interlacing
zeros, positive derivative on the real pole-free intervals, and no
nonreal zeros. These are standard meromorphic complete Bernstein
facts; they supply no integer-length assertion.

With finitely many poles, (9) is bounded at positive infinity if
\(\beta=0\), whereas \(\phi(s)/s\to\beta>0\) if \(\beta>0\).
Both contradict (4) and the hypotheses. Thus there are infinitely
many poles. The derivative and one-sided pole limits in LemmaA.1,
together with \(\phi(0)\ge0\), locate the first zero between
\(-b_1\) and zero, permitting the endpoint zero at zero.
Thereafter there is one zero between consecutive poles. Write the
entire ordering as
\[
 0\le a_1<b_1<a_2<b_2<\cdots,\qquad
 \phi(-a_j)=0,\quad -b_j\text{ a pole}.
 \tag{10}
\]
There is no omitted positive zero, since \(\phi(s)>0\) for \(s>0\).

For real \(t\ge0\), let \(m(t)\) be the zero multiplicity of \(F\)
at \(-t\), and put \(m(t)=0\) for \(t<0\). Taking orders in the
meromorphic identity (8) gives
\[
 m(t)-m(t-1)=\nu(t),\qquad
 \nu(t)=\sum_j\left({\bf1}_{t=a_j}-{\bf1}_{t=b_j}\right).
 \tag{11}
\]
For each \(t\ge0\), this has the exact finite solution
\(m(t)=\sum_{k=0}^{\lfloor t\rfloor}\nu(t-k)\).
Before \(b_1\), the only possible source in this sum is \(a_1\).
At \(t=b_1\), the negative unit from \(b_1\) must be canceled,
since \(m(b_1)\ge0\). Hence \(b_1-a_1\) is an integer; it is
positive by (10). If \(L_1=b_1-a_1\), the two sources' combined
contribution is exactly one on
\(\{a_1,a_1+1,\ldots,a_1+L_1-1\}\) and zero elsewhere.
This also covers \(a_1=0\).

Inductively suppose all preceding pairs have this form. Their entire
contributions end before \(b_{j-1}<a_j\), so at \(t=b_j\) only
the current pair can cancel the negative unit. It follows again
that \(L_j=b_j-a_j\) is a positive integer and its contribution
is the finite string
\[
 T_j=\{a_j,a_j+1,\ldots,a_j+L_j-1\}.
 \tag{12}
\]
This proves the claim for each pair without assuming a uniform bound
on \(L_j\). The finite-sum formula determines every real zero, and
the strings have disjoint supports. Each zero is simple.
A nonreal zero of \(F\) would propagate by (8) through positive
integer shifts, since \(\phi\) has no nonreal zeros or poles.
Eventually it would reach \(\Re z>0\), a contradiction.
Thus (12) accounts for all zeros of \(F\), with negatives as their
locations. The gaps in their nonnegative parameters are one within
a string and \(a_{j+1}-(b_j-1)>1\) between strings.

### 4. Density from the logarithmic representation

Let \(U=\bigcup_j(a_j,b_j)\). By (10) and the pole limits,
\(\phi(-t)<0\) precisely for \(t\in U\), away from endpoints.
Use Schilling–Song–Vondraček, *Bernstein Functions: Theory and
Applications*, **first edition (2010)**, Theorem6.2 and Corollary6.3,
pp50–55, and Theorem6.10 and its proof, pp58–59
([book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MC/MCat/Schilling%20R.L.%2C%20Song%20R.%2C%20Vondracek%20Z.%20Bernstein%20functions..%20theory%20and%20applications%20%28De%20Gruyter%2C%202010%29%28ISBN%209783110215304%29%28O%29%28328s%29_MCat_.pdf)).
The primary statement was inspected in the saved step642 assessment;
that unchanged coverage is reused. The optional mirror retrieval
in this audit timed out. No 2012 theorem numbering is substituted.

The logarithmic representation for a nonzero complete Bernstein
function is
\[
 \log\phi(s)=\kappa+
 \int_0^\infty
 \left(\frac{t}{1+t^2}-\frac1{s+t}\right)\eta(t)\,dt,
 \quad s>0,\quad 0\le\eta\le1\ \text{a.e.},
 \tag{13}
\]
with real \(\kappa\), and no extra singular measure or linear term.
To identify its density here, the principal \(\log\phi\) has
imaginary part in \((0,\pi)\) in the upper half-plane.
At a negative real point not a zero or pole, its upper boundary
value has imaginary part \(0\) or \(\pi\), according to the sign
of \(\phi\). The imaginary part of the integral representation is
the Poisson integral of \(\eta\); its boundary value is \(\pi\eta(t)\)
at almost every Lebesgue point. Hence
\(\eta(t)={\bf1}_U(t)\) almost everywhere. The countable zero and
pole endpoints do not change this assertion.

Differentiate (13) at \(s>0\). On a neighborhood of a fixed
\(s_0>0\), the derivative integrand is bounded by
\((s_0/2+t)^{-2}\), an integrable majorant. It follows that
\[
 \frac{\phi'(s)}{\phi(s)}
 =\int_0^\infty\frac{{\bf1}_U(t)}{(s+t)^2}\,dt.
 \tag{14}
\]
Concavity of a Bernstein function gives
\[
 \frac{\phi(2s)-\phi(s)}{\phi(s)}
 \le\frac{s\phi'(s)}{\phi(s)}
 \le\frac{2(\phi(s)-\phi(s/2))}{\phi(s)}.
 \tag{15}
\]
By index-one regular variation the two outer quantities tend to one.
Combining this with (14) and
\(\int_0^\infty s(s+t)^{-2}\,dt=1\) gives
\[
 \delta(s):=\int_0^\infty
        \frac{s{\bf1}_{U^c}(t)}{(s+t)^2}\,dt\longrightarrow0.
 \quad
 |[0,s]\setminus U|\le4s\delta(s)=o(s).
 \tag{16}
\]
Here \(U^c\) is the complement in \([0,\infty)\).

Let \(N_F(s)=\#\{t\in[0,s]:F(-t)=0\}\). A completed interval
\((a_j,b_j)\) contributes length \(L_j\) and exactly \(L_j\)
string points. At most one interval is partially cut by \(s\).
If \(a_j\le s<b_j\), its point count is
\(\lfloor s-a_j\rfloor+1\), while its included length is \(s-a_j\);
their difference is in \((0,1]\).
The same bound includes \(s=a_j\); at \(s=b_j\) the difference
is zero. Thus
\[
 N_F(s)=|U\cap[0,s]|+\epsilon(s),\quad
 0\le\epsilon(s)\le1,\qquad N_F(s)=s+o(s).
 \tag{17}
\]
This treats a long terminal string without summing a rounding error
over all strings.

### 5. Sign changes, zero coefficients, and Fabry

Put \(f(x)=E(-x-1/2)=F(1/2-x)\). Its zeros have locations
\(t+1/2\), \(t\in\bigcup_jT_j\), all positive and simple,
with gaps at least one. Its positive zero count satisfies
\[
 N_f(x)=x+o(x).
 \tag{18}
\]
Equation (7) implies
\(\operatorname{sgn}c_n=(-1)^n\operatorname{sgn}f(n)\);
it also gives \(c_n=0\) if and only if \(f(n)=0\).
In particular \(c_0=p(0)>0\), and \(f(0)>0\).

Let \(m<n\) be successive indices with nonzero coefficients, set
\(d=n-m\), and let \(r\) count all zeros of \(f\) in \((m,n)\).
Neither endpoint is a zero. Because all real zeros are simple,
\[
 \operatorname{sgn}(c_nc_m)=(-1)^{d+r}.
 \tag{19}
\]
Spacing at least one gives \(r\le d\): if \(r\ge d+1\), the
distance between the first and last zero would be at least \(d\),
impossible in that open interval. If the coefficients change sign,
\(d+r\), equivalently \(d-r\), is odd, so \(d-r\ge1\).
Thus each sign change is bounded by the nonnegative integer deficit
\(d-r\). Zeros at skipped integer indices belong to \(r\); discarding
them would invalidate the argument.

For a nonzero \(c_n\), sum these inequalities over consecutive
nonzero indices from \(0\) to \(n\). The interval lengths sum to
\(n\); their zero counts sum exactly to \(N_f(n)\). If \(S(n)\)
counts changes between consecutive nonzero coefficients through
index \(n\), this proves
\[
 0\le S(n)\le n-N_f(n)=o(n).
 \tag{20}
\]
Finite radius implies infinitely many nonzero coefficients. At any
integer \(N\), take the last nonzero index \(k\le N\). Then
\(k\to\infty\) as \(N\to\infty\), \(S(N)=S(k)\), and
\(S(N)/N\le S(k)/k\to0\). Thus the sign-change set
\(S\subset\mathbb N\), with the later nonzero index marking each
change, has counting function \(n_S(x)=o(x)\).

Its maximum density, in the convention used by Eremenko, is zero:
for every fixed \(r>0\),
\[
 0\le\limsup_{x\to\infty}
 \frac{n_S((1+r)x)-n_S(x)}{rx}
 \le\limsup_{x\to\infty}\frac{o((1+r)x)}{rx}=0.
 \tag{21}
\]
Taking \(r\downarrow0\) after this limit gives \(D_2(S)=0\).
This is the required density, not an unproved identification of
different density notions.

Apply the zero-maximum-density consequence of A. Eremenko,
*A version of Fabry's theorem for power series with regularly varying
coefficients*, Proc. AMS136 (2008),4389–4394,
[arXiv:0710.5894v2, TheoremA and the sign-change definition,
pp1–2; maximum-density characterization, p3](https://arxiv.org/pdf/0710.5894v2).
It says that a real power series of radius one whose changes
between consecutive nonzero coefficients have maximum density zero
is singular at \(+1\). The measurable-superset characterization
on p3 supplies precisely the density form of TheoremA.
No magnitude-regularity condition from that paper's Theorem1 is used.

The series \(g(Rz)=\sum_n(c_nR^n)z^n\) has real coefficients,
radius exactly one, and exactly the same zero coefficients and
sign-change indices because \(R>0\). Therefore it is singular
at \(+1\). But the assumed continuation of \(g\) near \(R\)
continues \(g(Rz)\) near \(1\). This contradiction proves the claim.

All auxiliary conclusions above were derived under the contradictory
complete-Bernstein representation. In particular, no zero-density
statement for the actual Xi Taylor coefficients has been assumed.
The proof needs no numerical certificate, no integer-moment
interpolation uniqueness, and no assertion that ordinary Bernstein
functions have the Pick representation (13).

## Mathlib

Full matching coverage is **not checked**. No Mathlib theorem is claimed
to implement the abstract obstruction, Bernstein-gamma product law,
meromorphic string argument, or Fabry specialization. The named analytic
and probability results are imported by the precise citations above;
their formal availability is not inferred from this informal audit.
