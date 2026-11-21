# C753a: A fixed-test positive-time Gaussian anchor

## Hypotheses

Let f be in C_c^infinity(R;C), with the two exact neutral moments

\[
 \int_{\mathbb R}e^{x/2}f(x)\,dx
 =\int_{\mathbb R}e^{-x/2}f(x)\,dx=0.
\]

Set F(z)=integral f(x)exp(-izx)dx and
F^#(z)=overline(F(bar z)). Let Z be the complete zero multiset of Xi,
with every multiplicity retained. In L018's coordinates these are
z_rho=(rho-1/2)/i and satisfy |Im z_rho|<1/2. L024 supplies
0 not in Z and sum_(z in Z)|z|^(-2)<infinity.

For tau>0 let f_tau=G_tau*f, where
G_tau(x)=(4 pi tau)^(-1/2)exp(-x^2/(4tau)), and let f_0=f.
Write c_tau=f_tau*tilde(f_tau), with tilde(g)(x)=overline(g(-x)).
Use L753's full neutral Weil pairing, with no arithmetic cutoff:

\[
 \begin{split}
 \mathcal E_f(\tau)
 &=\int_{\mathbb R}
   [\Re\psi(1/4+iu/2)-\log\pi]
        |F_{f_\tau}(u)|^2\frac{du}{2\pi}\\
 &\quad-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       [c_\tau(\log n)+c_\tau(-\log n)].
 \end{split}                                                    \tag{1}
\]

Here psi is the digamma function and Lambda is the von Mangoldt function.
Assume a finite real H>1/2 such that **every** Xi zero with
|Re z|<=H is real. Assume there is a real Xi zero gamma_* satisfying

\[
 \gamma_*^2<H^2-\tfrac14,
 \qquad F(\gamma_*)\ne0.                                      \tag{2}
\]

These are hypotheses about a complete window and the particular test,
not about a finite list of sampled zeros. Simplicity is not assumed.

The saved SPECIALIZE assessment is
`drafts/literature/2026-11-04-neutral-gaussian-anchor-specialization.md`.
The analytic identity is imported from audited L753, which specializes
E. Carneiro and M. B. Milinovich, *On Littlewood's estimate for the modulus
of the zeta function on the critical line*,
[arXiv:2403.17803v1, Section 2.2, Lemma 4, printed p.5](https://arxiv.org/pdf/2403.17803v1).
That unconditional Guinand-Weil formula is not reproved here. Its
analytic-strip hypotheses and both neutral pole cancellations are paid
in L753. The additional work below is an elementary exponential
comparison, classified REPRODUCTION, with no originality claim.

## Conclusion

Put a=H^2-1/4, b=gamma_*^2, and delta=a-b>0. Let m_* be the
multiplicity of gamma_* and define

\[
 c_*=m_*|F(\gamma_*)|^2>0,\qquad
 B_H=\sum_{\substack{z\in Z\\|\Re z|>H}}
                |F(z)F^\#(z)|<\infty.                         \tag{3}
\]

For every tau>=0,

\[
 \mathcal E_f(\tau)
 \ge e^{-2b\tau}\left(c_*-B_H e^{-2\delta\tau}\right).         \tag{4}
\]

In particular define

\[
 \tau_0=
 \begin{cases}
  0,&B_H=0,\\
  \max\{0,\log(2B_H/c_*)/(2\delta)\},&B_H>0.
 \end{cases}                                                  \tag{5}
\]

Then, for every tau>=tau_0,

\[
 \mathcal E_f(\tau)\ge\tfrac12 c_* e^{-2b\tau}>0.              \tag{6}
\]

This is a fixed-test eventual sign. Formula (5) is not a certified
numerical onset: B_H includes the entire unverified zero multiset and
has not been evaluated. No onset uniform over f, no visibility for all
neutral tests, no sign at tau=0 in general, and no backward propagation
or RH conclusion follows. The separate bounded audit of 4 November 2026
(step 333) accepts this conditional conclusion; its checks are in
Section 4 below. No hypothesis, constant or mathematical input changed.

## Proof

### 1. A time-independent, complete coefficient majorant

Choose R>=1 with supp(f) contained in [-R,R]. L753(10), with
N=2 and strip width 1/2, gives a finite constant

\[
 A=4e^{R/2}(\|f\|_1+\|f''\|_1)
\]

such that both |F(x+iy)| and |F^#(x+iy)| are at most
A(1+|x|)^(-2) when |y|<=1/2. The reflected transform has the same
bound on this symmetric strip; no reality assumption on f is used.
For a zero z=x+iy, L018 and L024 give z!=0 and

\[
 |z|^2=x^2+y^2\le x^2+\tfrac14
       \le(1+|x|)^2\le(1+|x|)^4.
\]

Consequently

\[
 \sum_{z\in Z}|F(z)F^\#(z)|
 \le A^2\sum_{z\in Z}(1+|\Re z|)^{-4}
 \le A^2\sum_{z\in Z}|z|^{-2}<\infty.                         \tag{7}
\]

L024's representative-pair sum is doubled when all zeros are included;
it remains finite and retains every multiplicity. In particular B_H
is finite. Bound (7) is independent of tau and covers every tail term.
It is not a finite-zero preview or an assumption of real tail zeros.

### 2. Separate the certified window from its entire complement

For each individual tau>=0 choose any finite T>tau. L753(3) on
[0,T] identifies the real quantity (1) with the absolutely convergent
series

\[
 \mathcal E_f(\tau)=
      \sum_{z\in Z} e^{-2\tau z^2}F(z)F^\#(z).                \tag{8}
\]

This use for arbitrary finite tau is legitimate because L753 holds for
every finite T. No derivative, limit as T tends to infinity, or bound
uniform in T is imported. The new large-time bound is supplied below.

The zeros with |Re z|<=H lie in a compact rectangle by the strip
bound. Xi is a nonzero entire function, so there are finitely many,
including multiplicities. They are real by hypothesis. Their sum is

\[
 P_H(\tau)=\sum_{\substack{z\in Z\\|\Re z|\le H}}
                  e^{-2\tau z^2}|F(z)|^2
       \ge c_*e^{-2b\tau}.                                  \tag{9}
\]

The inequality retains all m_* occurrences of gamma_*; (2) puts this
zero strictly inside the window. Every other term in this finite sum
is nonnegative. This step uses no equality between F(gamma_*) and
F(-gamma_*), which need not hold for a complex test.

On the complementary multiset, z=x+iy has |x|>H and |y|<1/2.
Hence Re(z^2)=x^2-y^2>a, and for all tau>=0

\[
 \left|e^{-2\tau z^2}F(z)F^\#(z)\right|
 \le e^{-2a\tau}|F(z)F^\#(z)|.
\]

The triangle inequality for the complete absolutely convergent series
and (7) prove

\[
 \left|R_H(\tau)\right|
 :=\left|\sum_{\substack{z\in Z\\|\Re z|>H}}
           e^{-2\tau z^2}F(z)F^\#(z)\right|
 \le B_H e^{-2a\tau}.                                      \tag{10}
\]

The coefficient majorant in (7) dominates even the absolute sum after
multiplication by e^(2a tau). Thus (10) controls all unbounded times
directly, without using L753's bounded-interval exponential constant.
At a complex zero the holomorphic coefficient remains F(z)F^#(z),
not |F(z)|^2. No individual tail sign is asserted.

Equation (8) is real by L753. Also P_H is real, so R_H is real;
alternatively conjugation symmetry of the complementary zero multiset
and absolute convergence prove this. It follows from (9)-(10) that

\[
 \mathcal E_f(\tau)=P_H(\tau)+R_H(\tau)
 \ge c_*e^{-2b\tau}-B_He^{-2a\tau},
\]

which is (4). This argument neither rearranges a conditionally
convergent sum nor discards any zeros.

### 3. Strict eventual domination and the source scope

By (2), delta>0 and c_*>0. Therefore the ratio of the bound (10)
to the retained positive contribution in (9) is at most

\[
 (B_H/c_*)e^{-2\delta\tau}\longrightarrow0.
\]

If B_H=0, (4) already exceeds the bound in (6). If B_H>0 and
2B_H<=c_*, that bound holds from tau=0. Otherwise the second line of
(5) gives B_H exp(-2delta tau)<=c_*/2 for all tau>=tau_0.
These cases prove (6), including equality at the threshold.
No time derivative or backward heat operator is used.

For source context, certified real-zero windows and interior real
zeros can be supplied by the primary results already inspected in
`drafts/literature/2026-11-04-neutral-gaussian-positive-time-anchor.md`:
D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, Bull. London Math. Soc. 53 (2021), 792-797,
[arXiv:2004.09765v1, Theorem 1 and Section 2, printed p.2](https://arxiv.org/pdf/2004.09765v1),
and D. J. Platt, *Isolating some non-trivial zeros of zeta*, Math.
Comp. 86 (2017), 2449-2467,
[accepted manuscript, Theorem 5.1 and preceding isolation/count report,
printed p.8, with Sections 4.1-4.2](https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf).
The latter theorem is symmetric in the zeta height; L018 translates
height to Re z and critical-line location to real z. These computational
theorems are cited, not replayed. No particular numerical H or gamma_*
is instantiated in this conditional corollary, and no computation is
needed for (7)-(10). Neither certificate supplies F(gamma_*)!=0 for an
arbitrary chosen f. Strict separation and this visibility assumption
remain explicit. The L751/L752 absorption stop is neither used nor
reopened; it supplies no propagation from (6) to zero time.

### 4. Bounded independent audit of the comparison

The previously saved SPECIALIZE scope is
`drafts/literature/2026-11-04-neutral-gaussian-anchor-audit.md`.
This audit verifies the written specialization, not the external
computational certificates or the proof of the Guinand-Weil theorem.
It establishes no result beyond the checked source mathematics.

**Complete coefficient sum.** For complex f, reflected conjugation
replaces y by -y in the strip bound and preserves its constant; hence
the same A bounds both factors. Since every zero satisfies
0<|z|^2<=(1+|Re z|)^4, taking reciprocals gives the inequality in
(7) in the required direction, even for zeros with |z|<1. L024's
full sum is twice its representative sum, with each multiplicity
retained. Thus (7) is a bound for the entire coefficient series,
not just a finite truncation. Its constant is independent of time.

**Window and tail.** The strip and |Re z|<=H put the window in a
compact rectangle. Xi(0)>0, supplied by L024, makes Xi nonzero as
an entire function, so its zeros there are finite in number with
finite multiplicities. The inequality b<H^2-1/4<H^2 places the
stipulated real gamma_* inside this window, and m_*>=1. Each window
coefficient is a modulus square only because its argument is real.
No equality of the coefficients at gamma_* and -gamma_* is needed.
On the complement, x^2>H^2 and y^2<1/4 imply Re(z^2)>a>0.
For tau=0 the exponential bound is equality; for tau>0 it still
has the asserted weak direction. Summing its absolute bound gives
(10) at every time. In particular
sup_(tau>=0) e^(2a tau) sum_complement |H_tau(z)|<=B_H.
Here H_tau(z)=exp(-2tau z^2)F(z)F^#(z), as in L753.
This proves the required unbounded-time bound directly.

**Identity and reality.** At any chosen tau>=0, L753 may be applied
with T=tau+1. Its zero-side equality includes all multiplicities,
and requires neither a limit as T grows nor uniform differentiated
estimates on an unbounded interval. For the holomorphic coefficient
K(z)=F(z)F^#(z), K(bar z)=overline(K(z)); the Gaussian factor has
the same conjugation property. L018 gives conjugate zeros with
equal multiplicity, and (7),(10) pay absolute convergence. Thus
conjugate pairing, as well as L753's real arithmetic expression,
proves realness. The complementary remainder may have either sign;
its lower bound is -|R_H|, never an asserted modulus square.

**All threshold cases.** The actual required dominance ratio is
at most (B_H/c_*)exp(-2delta tau), which tends to zero because
delta>0 and c_*>0. If B_H=0, (4) gives c_*exp(-2b tau) for all
tau>=0. If 0<2B_H<=c_*, then tau_0=0 and the subtracted term in
the parentheses of (4) is at most c_*/2 already at zero. Equality
2B_H=c_* is included. If 2B_H>c_*, then tau_0>0 and
B_H exp(-2delta tau_0)=c_*/2 exactly; its monotonic decrease gives
(6) including tau=tau_0. For every finite tau the exponential is
strictly positive, although it can tend to zero as tau grows.

The audit therefore accepts (3)-(6) under exactly the stated
hypotheses. No mathematical correction or new direct input is needed.
The window, strict separation and nonvanishing remain assumptions;
B_H has no certified numerical value. The result is a restricted
fixed-test starting sign, with no uniform onset, backward comparison,
sign for arbitrary neutral tests or RH consequence. L751/L752's
absorption stop is unchanged. Mathlib coverage below remains unchecked.

## Mathlib

Full matching coverage of this fixed-test Gaussian anchor is not
checked. Absolute convergence, Fourier strip bounds and exponential
comparison are used as proved above or imported from L753/L024; no
matching Mathlib theorem or absence claim is asserted.
