# Lemma 379: exact response-grid Riemann–Siegel reduction and absolute-budget failure

## Hypotheses

Let F_0,G,A be the actual functions and envelope in L366. Retain
L368's exact carrier Qb and L372's actual Euler-log phase
eta(t)=Im mathscr L(5/2+it). Let t tend to positive infinity through
the simple zeros of G on L372's eventual ray. Put

\[
 m=\left\lfloor\sqrt{t/(2\pi)}\right\rfloor,\qquad
 b=\frac{t^2/4-3/16-it/2}{\pi},\qquad
 \beta=-\arctan\frac{8t}{4t^2-3}\quad(t\ge2).
\]

Thus beta is the exact argument of b on this ray, not a replacement
of the Euler phase by a constant. Choose the Hardy gamma phase
vartheta with Q=A exp(i vartheta). For each sampled t choose the integer
k such that vartheta(t)+beta(t)+eta(t)=pi/2+k pi. The equality can be
made on continuous branches; changes by 2pi do not change its parity.
There is no RH, critical-line simplicity, noncoincidence or D<=0
assumption. All finite sums retain the specified moving cutoff.

## Conclusion

Define the actual centered finite sum

\[
 S_m(t)=\sum_{n=2}^m (n^{-1/2}-n^{-5/2})
                  \sin(\eta(t)+t\log n).
\]

For all sampled t>=8pi, the full Riemann–Siegel finite sum P(t) obeys

\[
 \begin{aligned}
 P(t)&=2\sum_{n=1}^m n^{-1/2}
                 \cos(\vartheta(t)-t\log n)
       =2(-1)^kS_m(t)+e(t),\\
 |e(t)|&\le\left(\frac{12}{t}+\frac{18}{t^2}\right)\sqrt m
                  +\frac4{3m^{3/2}}=O(t^{-3/4}).       \tag{1}
 \end{aligned}
\]

For the real Hardy function H(t)=exp(i vartheta(t))zeta(1/2+it),
the unconditional scalar formula therefore gives

\[
 H(t)=2(-1)^kS_m(t)+e(t)+R_{\rm RS}(t),\qquad
 R_{\rm RS}(t)=O(t^{-1/4}),\qquad F_0(t)=-A(t)H(t).    \tag{2}
\]

The absolute triangle-budget certificate does **not** give a positive
lower margin: writing W_m=sum_(n=2)^m(n^(-1/2)-n^(-5/2)), its bound is
|S_m|<=W_m=2sqrt(m)+O(1), with the centered enclosure [-W_m,W_m].
The radius for 2S_m divided by t^(-1/4) is asymptotic to
4(2pi)^(-1/4)t^(1/2), whereas a nonvanishing certificate needs a
positive lower bound exceeding the remainder. This is a failure of
this specified absolute certificate, not a lower bound for an actual
error, a proof that all phase-sensitive estimates fail, or evidence
of an actual common zero. No sign, count bound or RH range is obtained.

## Proof

This is a **REPRODUCTION**: import the scalar Riemann–Siegel formula
by [NIST DLMF 25.10.1–3](https://dlmf.nist.gov/25.10#E3), version 1.2.8,
15 September 2026, inspected with its complete O(t^(-1/4)) remainder
on 2026-10-08. Its source is E. C. Titchmarsh, *The Theory of the
Riemann Zeta-function*, second edition, revised by D. R. Heath-Brown
(1986), section 4.17, (4.17.2)/(4.17.4), p. 89. The formula applies
unconditionally at every sufficiently large positive real t with the
exact m above, including cutoff transitions. It needs no assumption
that t is a zeta zero. The displayed higher remainder correction
DLMF 25.10.4 is unused. We do not reprove the scalar theorem. The
specialization below is necessary because the actual sampling phase
includes both b and the Euler logarithm; no imported theorem supplies
the desired lower margin there. Ready coverage is the unchanged
`drafts/literature/2026-10-08-response-grid-remainder-margin.md`.

**Phase and normalization.** DLMF 25.10.2 defines vartheta as the
gamma argument of Gamma(1/4+it/2), minus (t/2)log pi. Since the
remaining factor p=t^2+1/4 of Q is positive, this is exactly Q's
argument. Any principal versus continuous gamma-argument choice
differs pointwise by 2pi integers. Its exponential and the finite
cosine sum are unchanged. On t>=2 the real part of b is positive,
its imaginary part negative, and their ratio gives exactly beta.
L372's continuous carrier phase equals vartheta+beta modulo 2pi.
Its G-zero equation therefore gives the stated integer k with the
same parity, without changing any sampled height. Consequently

\[
 \cos(\vartheta-t\log n)
   =(-1)^k\sin(\eta+\beta+t\log n).                  \tag{3}
\]

DLMF 25.10.1 makes H real. L366 (1), with
Lambda(1/2+it)=Gamma(1/4+it/2)pi^(-1/4-it/2)zeta(1/2+it),
then gives F_0=-p Re Lambda=-A H. Here A>0. This checks the
minus sign and proves that nonvanishing of H would be nonvanishing
of F_0 at the same response zero.

**Exact right-line cancellation.** L368 (5), at j=0, is the absolutely
convergent Dirichlet series at Re v=5/2; its scalar source is
[DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1). L372 (4) fixes eta as
the imaginary part of a logarithm whose exponential is that actual
zeta value. Hence

\[
 e^{-i\eta(t)}\zeta(5/2+it)=|\zeta(5/2+it)|>0.
\]

Taking imaginary parts of its absolutely convergent series gives

\[
 \sum_{n\ge1}n^{-5/2}\sin(\eta+t\log n)=0.           \tag{4}
\]

This identity holds at every real t, not just a sample, and does not
continue the Euler or Dirichlet series into the critical strip.
Let

\[
 V_m=\sum_{n>m}n^{-5/2}\sin(\eta+t\log n),\qquad
 C_m=\sum_{n=1}^m n^{-1/2}\cos(\eta+t\log n).
\]

Equation (4) implies exactly
sum_(n=1)^m n^(-1/2)sin(eta+t log n)=S_m-V_m, since the n=1
coefficient in the difference of weights is zero. Thus (3) yields

\[
 P(t)=2(-1)^k\{\cos\beta\,(S_m-V_m)+\sin\beta\,C_m\}. \tag{5}
\]

No finite term has been dropped, and the only infinite tail is V_m,
which remains absolutely convergent. This uses the exact right-line
identity rather than unrelated prime-phase choices.

**Complete error bound.** For t>=2,
|beta|<=8t/(4t^2-3)<=3/t. Hence
|sin beta|<=3/t and |1-cos beta|<=9/(2t^2). Integral comparison gives

\[
 |V_m|\le\frac{2}{3}m^{-3/2},\qquad
 |C_m|\le\sum_{n=1}^m n^{-1/2}\le2\sqrt m,
 \qquad |S_m|\le W_m\le2\sqrt m.
\]

Subtracting 2(-1)^kS_m from (5), bounding its three remaining terms,
gives precisely (1). If x=sqrt(t/(2pi))>=2, then x/2<=m<=x.
In particular sqrt(m)/t<= (2pi)^(-1/4)t^(-3/4),
m^(-3/2)<=2^(3/2)(2pi)^(3/4)t^(-3/4), and the extra
sqrt(m)/t^2 term is O(t^(-7/4)). These are uniform bounds through
all cutoff transitions. Importing P+R_RS=H proves (2).

**What the tested certificate supplies.** Every difference weight in
S_m is positive. Integral bounds give
sum_(n=1)^m n^(-1/2)=2sqrt(m)+O(1); absolute convergence bounds
sum_(n=1)^m n^(-5/2) uniformly. Therefore W_m=2sqrt(m)+O(1).
Since m/sqrt(t/(2pi)) tends to one, the stated radius ratio follows.
The bound obtained by replacing each sine with [-1,1] is centered
at zero and provides no lower bound for |S_m|. This observation
does not assert that zero is attained by the actual correlated phases.

Even before using (4), first-term domination by these same absolute
bounds cannot work: the n=1 term of P has modulus at most 2, while
the tail budget 2 sum_(n=2)^m n^(-1/2) tends to infinity. The
reverse-triangle sufficient surplus is thus negative eventually,
even at the largest possible first-term modulus. Eliminating that
term in (5) improves the algebraic description and leaves the
correction o(t^(-1/4)); it still supplies no lower margin for S_m.
A uniform |S_m|/t^(-1/4) tending to infinity would suffice despite
the unspecified R_RS constant, but is not proved here. The approved
test therefore stops at an uncontrolled actual signed finite sum.
Eventual noncoincidence, the quantitative common-zero bound, actual
D<=0 and the total L367 margin remain unresolved. ∎

## Mathlib

Full matching coverage for this exact actual-response-grid reduction,
the scalar Riemann–Siegel theorem, and supporting gamma-phase results
has not been checked. Unknown coverage is not absence. The source
formula and applicable hypotheses are the precise references above;
no formalization or progress beyond the inspected scalar sources is
claimed. The new local specialization awaits separate critical review.
