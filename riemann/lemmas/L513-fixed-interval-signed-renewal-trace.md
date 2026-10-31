# L513 — Fixed-interval signed renewal trace, with the domain split retained

## Hypotheses

Fix ell>0, I=(0,ell), and the Fourier convention
hat f(xi)=integral_R f(x)exp(-i xi x) dx. Put

    Psi(xi)=(1/2)log(1+xi^2),     n(t)=exp(-|t|)/(2|t|), t!=0.

G_D denotes the nonnegative self-adjoint **part operator** on the open
set D of the regular symmetric Levy Dirichlet form

    Q(f,f)=(1/(2pi)) integral_R Psi(xi)|hat f(xi)|^2 dxi
          =(1/2) integral_R integral_R
                    |f(x)-f(y)|^2 n(x-y) dx dy.                 (1)

The part form uses zero extension and the closure of compactly supported
smooth tests in D in the Q+L2 norm. In particular, this is the killed
process realization, not the operator obtained by subordinating a
Dirichlet Brownian generator after killing. Write G_+=G_(0,infinity).

Let u in Dom(G_I) be complex-valued, with u,h=G_I u in L-infinity(I).
Retain the interval-to-half-line **operator-domain split** as a
hypothesis: the extension U=u on I, U=0 on (ell,infinity), belongs
to Dom(G_+), and G_+U is the function

    g(y)=h(y),                                      0<y<ell,
    g(y)=-integral_0^ell n(y-z)u(z) dz,              y>ell.      (2)

The same domain-split hypothesis is retained for u reflected about
ell/2 when asserting the right trace. This is an operator statement,
not just a formal pointwise kernel calculation; it excludes an
unaccounted interface distribution. Its proof is outside this lemma.

This is an audit/reproduction of bramble_trace, *Boundary traces and
support variation for localized Weil operators*, paper 67, v1,
27 October 2026, [Section 3.3, (3.11)–(3.19)](https://rstation.ai/problems/riemann_hypothesis/papers/67).
The gate is the pre-existing SPECIALIZE assessment at
`drafts/literature/2026-10-30-weil-renewal-trace-input-coverage.md`.
The reproduction is needed to distinguish a signed trace limit from
the boundary upper estimate and from the nonnegative occupation theorem.
No novelty or independent reproof of the imported primary theorems
is claimed.

## Conclusion

With the normalized renewal function specified in (3) below,

    V(x) sqrt(log(1/x)) -> 1                    as x decreases to 0.

The zero extension of u has a continuous representative. For that
representative the left trace exists and is

    tau_L(u) := lim_(x->0+) sqrt(log(1/x)) u(x)
              = lim_(x->0+) u(x)/V(x)
              = integral_0^ell v(y)h(y) dy
                - integral_0^ell u(z)
                    integral_ell^infinity v(y)n(y-z) dy dz.    (T)

Both displayed integrals are absolutely convergent. Reflection gives

    tau_R(u) := lim_(x->0+) sqrt(log(1/x)) u(ell-x)
              = integral_0^ell v(y)h(ell-y) dy
                - integral_0^ell u(ell-z)
                    integral_ell^infinity v(y)n(y-z) dy dz.

Zero and complex traces are allowed. No sign of g, h, or u is assumed.
The claim concerns one fixed interval and the bounded data in the
hypotheses. It neither proves boundedness of all full Weil-operator
eigenfunctions nor audits the split, collars, support variation,
varying-operator uniformity, or arithmetic positivity. In particular
it does not by itself discharge L512's general analytic interface.

## Proof

### Imported renewal facts and normalization

Use Grzywny–Ryznar, *Potential theory of one-dimensional geometric
stable processes*, [arXiv:1107.0745v1](https://arxiv.org/html/1107.0745v1),
Sections 2–3 (Levy density (2.4) and local-time normalization),
Proposition 3.2, Proposition 3.5's occupation identity, Remark 3.6,
and Lemmas 4.1 and 4.3. Their exponent at parameter two is
Psi_GR(xi)=log(1+xi^2), and their ladder-local-time constant is one.
The process is symmetric and non-compound-Poisson; log(1+s) is a
complete Bernstein function, so Proposition 3.2 applies, including
parameter two. In this convention define

    kappa(s)=exp{(1/pi) integral_0^infinity
                         s log(Psi(t))/(s^2+t^2) dt},
    F(s)=1/kappa(s)=integral_[0,infinity) exp(-sy) dV(y), s>0,
    v(y)=V'(y).                                                (3)

The integral defining kappa is finite: at zero log(Psi(t)) has only
a logarithmic singularity, and at infinity it grows as log log t.
As integral_0^infinity s/(s^2+t^2) dt=pi/2, multiplying Psi_GR
by 1/2 divides kappa by sqrt(2). Uniqueness of Laplace transforms
then gives V=sqrt(2)V_GR and v=sqrt(2)v_GR. Equivalently the process
has been slowed by two; its killed occupation kernel is multiplied
by two. These checks agree.

The imported statements give V(0)=0, V(x)=integral_0^x v(s) ds,
with v positive, continuous and decreasing on (0,infinity), and

    K(x,y)=integral_0^min(x,y) v(x-z)v(y-z) dz,  x!=y,
    integral_0^R K(x,y) dy <= V(x)V(R),          0<x<=R/2.       (4)

Thus the coefficient in (4) remains one after rescaling. One can
also verify that bound directly by Tonelli: for x<R, integrating
the factorization in y gives
integral_0^x v(x-z)V(R-z) dz <= V(x)V(R).
The diagonal value K(x,x) can be infinite; no bounded-diagonal claim
is used. Proposition 3.2's constant term b in v is retained:
b_GR=1 and b=sqrt(2). We do not assume decay of v at infinity.
The book occupation identity behind GR is Bertoin, *Levy Processes*,
Chapter VI, Theorem 20, p. 176, as quoted there; the book proof is
not independently audited here.

### Exact leading constant

Concavity and monotonicity of q->(1/2)log(1+q), with value zero at
q=0, imply for all s,r>0

    min(1,r^2) <= Psi(sr)/Psi(s) <= max(1,r^2).

Consequently |log(Psi(sr)/Psi(s))|<=2|log r|. After t=sr in (3),

    log(kappa(s)/sqrt(Psi(s)))
       =(1/pi) integral_0^infinity
                   log(Psi(sr)/Psi(s))/(1+r^2) dr.

For every fixed r>0 the integrand's numerator tends to zero as
s increases to infinity. The displayed bound is integrable on
(0,infinity), so dominated convergence gives
kappa(s)~sqrt(Psi(s))~sqrt(log s), and F(s)~1/sqrt(log s).

For fixed epsilon,M>0 and x>0, the nonnegative measure dV gives

    V(x) <= exp(epsilon) F(epsilon/x),
    V(x) >= F(M/x)-exp(-M/2)F(M/(2x)).                          (5)

The first bound uses exp(-epsilon y/x)>=exp(-epsilon) for y<=x.
For the second, split F(M/x) at x; its lower piece is at most V(x),
and on y>x use exp(-My/x)<=exp(-M/2)exp(-My/(2x)).
Divide (5) by F(1/x), let x decrease to zero, and use
F(c/x)/F(1/x)->1 for each fixed c>0. This bounds the limsup by
exp(epsilon) and the liminf by 1-exp(-M/2). Let epsilon decrease
to zero and M increase to infinity. Hence V(x)~F(1/x), proving
the constant one claimed in the conclusion. Mere comparability
from GR Lemma 4.1 would not suffice for this normalization.

### Continuous representative and the weak-form comparison

We apply Hernandez-Santamaria–Lopez Rios–Saldana,
*Optimal boundary regularity and a Hopf-type lemma for Dirichlet
problems involving the logarithmic Laplacian*,
[arXiv:2401.18033v2, Theorem 1.1](https://arxiv.org/html/2401.18033v2).
That theorem concerns L_Delta with symbol 2 log|xi|, on a bounded
open set with the uniform exterior sphere condition, for a weak
solution in H(I) intersect L-infinity(R) and bounded forcing.
The interval has the geometric property. Here is the operator and
weak-solution check, including the singular low frequencies.

With T having symbol log|xi|, the difference G-T has multiplier

    m(xi)=(1/2)log(1+xi^(-2))
         =integral_0^1 b/(b^2+xi^2) db.

The inverse Fourier transform of b/(b^2+xi^2) is
exp(-b|t|)/2. Integrating in b gives

    q(t)=(1-exp(-|t|))/(2|t|), q(0)=1/2,     0<=q<=1/2.        (6)

These identities hold as tempered distributions (m is integrable
in frequency); they require no nonexistent global L1 norm for q.
In particular |q*u|<=ell||u||_infinity/2 on I. Also finite (1)
controls the short-range energy defining H(I), since
n(t)>=exp(-1)/(2|t|) for 0<|t|<=1. Thus the zero extension of u
belongs to H(I).

For every smooth compactly supported test phi in I, the operator
domain identity gives Q(u,phi)=<h,phi>. The multiplier identity (6)
gives the full logarithmic weak equation

    L_Delta u = 2h-2q*u                in I, with u=0 outside I. (7)

To justify the weak interpretation, use Chen–Weth,
*The Dirichlet Problem for the Logarithmic Laplacian*,
[arXiv:1710.03416v6, Theorem 1.1(ii) and Section 3, (3.9)–(3.11)](https://arxiv.org/html/1710.03416v6),
or HLS (1.15)–(1.19): the pairing is the full form, including the
long-range and constant terms. The Fourier identity first holds on
tests; it extends to u by part-form approximation. Its G pairing is
continuous in the form norm, and its q pairing is continuous in L2
on this fixed bounded support by (6). The short-range form and the
bounded remaining terms likewise pass to that limit. No pointwise
evaluation of a divergent singular integral on rough u is needed.

The right side of (7) is bounded. Applying HLS Theorem 1.1 to real
and imaginary parts gives a continuous zero extension and its
logarithmic boundary upper bound. We use its continuity below;
that upper bound alone is not a trace limit. No positive solution
or positive lowest eigenvalue of L_Delta is required.

### Absolute exterior forcing and absolute occupation

Put H=||h||_infinity and B=||u||_infinity. For r=y-ell>0, (2) gives

    |g(ell+r)| <= (B/2) integral_r^(r+ell) exp(-t)/t dt.         (8)

For 0<r<1 this is bounded by (B/2)(|log r|+C), with absolute C;
for r>=1 it is at most B exp(-r)/(2r). Together with |g|<=H on I,
these bounds prove g in L1(0,infinity) intersect L2(0,infinity).
Global boundedness of g is neither asserted nor used. Moreover,
Tonelli gives the explicit finite cross integral

    integral_0^ell integral_ell^infinity n(y-z) dy dz
       =integral_0^infinity min(t,ell) exp(-t)/(2t) dt <= 1/2.   (9)

In particular integral_ell^infinity v(y)|g(y)| dy
<=v(ell)B/2. The interior weighted integral is at most H V(ell).
This proves absolute convergence of integral_0^infinity v(y)g(y)dy
and, using |u| in (9), the double integral in (T).

For 0<x<ell/4, (4) bounds the potential of |g| on (0,ell/2)
by H V(x)V(ell/2). On y>=ell/2, write s=x-z in (4) to obtain

    K(x,y)/V(x) <= v(y-x) <= v(y/2) <= v(ell/4).               (10)

Thus P(x)=integral_0^infinity K(x,y)g(y)dy is absolutely defined
for each such x. This step precedes every signed use of occupation.

### Identifying the signed potential with U

The killed semigroup used in GR must be the semigroup of G_+.
The relevant standard theorem is the part-form/part-process
correspondence: Fukushima–Oshima–Takeda, *Dirichlet Forms and
Symmetric Markov Processes*, second revised and extended edition,
Section 4.4, Theorems 4.4.2–4.4.3, pp. 173–175
([primary book text inspected in a hosted scan](https://www.scribd.com/document/968246537/Masatoshi-Fukushima-Yoichi-Oshima-Masayoshi-Takeda-Dirichlet-Forms-and-Symmetric-Markov-Processes-2010)).
It identifies the part form of a regular symmetric Dirichlet form
on an open set with its associated Hunt process killed on exit.
Here Lebesgue measure is the reference measure, the symmetric Levy
process has exponent Psi, and its whole-line semigroup has multiplier
exp(-t Psi). Its form is exactly (1), by Plancherel and monotone
convergence of (1-exp(-t Psi))/t to Psi.

The Levy form is regular: mollification converges in its Fourier
form norm, and smooth spatial cutoffs converge in that norm using
integral_R min(1,t^2)n(t)dt<infinity. More explicitly, the cutoff
error's jump difference is a sum of a bounded cutoff times
f(x)-f(y) and f(y) times the cutoff difference. The first vanishes
by dominated convergence in (1); the second is dominated after
integration in x-y by a constant times
||f||_2^2 integral min(1,t^2)n(t)dt and tends to zero. This gives
the compactly supported smooth core. The same local smoothing of
compactly supported form functions gives the core for the open part.
Right continuity of paths starting in the open half-line prevents
instantaneous exit at time zero, so the irregularity condition of
Theorem 4.4.2 is satisfied. Thus the theorem applies to the part
operator as defined in the hypotheses. Its transition density is
the rescaled killed density p_t^+ of GR Section 2, with
K(x,y)=integral_0^infinity p_t^+(x,y)dt. This is killing of the
Levy process itself; no change of killing/subordination order occurs.

There is no zero eigenvector of G_+: if G_+f=0 then (1) forces
the L2 Fourier transform of its zero extension to vanish off {0},
and hence to vanish almost everywhere. Thus ker(G_+)={0}. By
the spectral theorem, exp(-T G_+)U tends to zero in L2 as T tends
to infinity. A spectral gap is not needed. Because U is in Dom(G_+)
and G_+U=g by the retained hypothesis, the Bochner integral satisfies

    integral_0^T exp(-tG_+)g dt = U-exp(-TG_+)U -> U in L2.     (11)

For completeness, (11) agrees almost everywhere near zero with
the kernel time integral even for the present unbounded signed g.
The L2 contraction gives finite-time Bochner integrability. Pairing
against compactly supported L2 tests and using the positive kernel
shows that this integral has the representative
integral_0^T integral_0^infinity p_t^+(x,y)g(y)dy dt. Positivity
gives the absolute pairing bound T||phi||_2||g||_2. This and the
absolute potential bound above justify Fubini there; they
also justify passage to T=infinity by dominated convergence. For
integer T these representatives converge to P(x) near zero. Select
an almost-everywhere-convergent subsequence of the L2 convergence
in (11), and discard the countable union of the exceptional sets
for those integer-time representatives. It follows that U(x)=P(x)
for almost every x in (0,ell/4). No inverse with a bounded L2
operator norm has been asserted.

### Endpoint limit and all-point representative

For fixed y>0 and sufficiently small x<y, the normalized kernel
is the average of v(y-x+s) against v(s)ds/V(x), 0<s<x. Since v
is decreasing and continuous at y,

    v(y) <= K(x,y)/V(x) <= v(y-x),
    K(x,y)/V(x) -> v(y).                                      (12)

Fix 0<epsilon<ell/2. For x<epsilon/2 the absolute contribution
of 0<y<epsilon to P(x)/V(x) is at most H V(epsilon), by (4).
The corresponding piece of integral v g has the same bound.
On y>=epsilon, the kernel quotient is bounded by
v(epsilon/2), independently of x<epsilon/2. This constant times
|g(y)| is integrable, so dominated convergence using (12) applies
on the complement. Therefore

    limsup_(x->0+) |P(x)/V(x)-integral_0^infinity v(y)g(y)dy|
         <= 2H V(epsilon).

Let epsilon decrease to zero. We obtain the limit for P at every
sufficiently small positive x, not just along a subsequence.
To transfer it to u, the function u(x)/V(x) is continuous on the
open interval and equals P(x)/V(x) almost everywhere near zero.
For any prescribed error, the just-proved limit puts the latter
in a fixed closed disk about the limit for every sufficiently
small x. A full-measure set is dense in that interval, so continuity
puts u(x)/V(x) in the same disk at every point there. This proves
the asserted all-point limit for the continuous representative.

Substitute (2) into integral v g; the absolute bounds (9) permit
the final interchange of y and z. This gives (T). The renewal
asymptotic converts u/V to the stated sqrt(log(1/x)) normalization.
Reflection commutes with the interval part operator, so the same
argument for u(ell-x) gives tau_R with h(ell-x), under the reflected
split hypothesis. The proof nowhere divides by a trace, assumes
real data, or assumes positivity of the bounded signed forcing.

### Audit disposition and remaining scope

Equations (3.11)–(3.19) pass this fixed-interval audit with the
stated domain split retained. The proof explicitly supplies the
weak-form specialization, absolute signed inversion and dense-set
passage that prevent the boundary upper estimate from being mistaken
for the conclusion. These are local reproduction checks of the
manuscript's assertion, not progress beyond the checked sources.
General half-line forcing without the bounded-near-zero and
integrable-tail conditions is outside the result. No assertion of
uniformity at a varying or vanishing full-operator ground eigenvalue,
and no RH positivity conclusion, follows.

## Mathlib

Full matching coverage of this signed renewal trace statement has
not been checked. The primary renewal and boundary theorems and the
part-process theorem are imported by the precise citations above;
their proofs are not formally verified here. Unknown Mathlib coverage
is not evidence that the result or its supporting theorems are absent.
