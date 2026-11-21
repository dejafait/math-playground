# Corollary 233c: the complete actual associated kernel is not a positive Gaussian scale mixture

## Hypotheses

Let K be exactly L019's actual theta kernel on [0,infinity), and put
k(u)=K(|u|). Use the complete integral of L233,

\[
A(t)=\int_{\mathbb R}s^2k(s+t)k(s-t)\,ds.
\]

The A here is the associated kernel, not the auxiliary function called
A in L019. A positive Gaussian scale mixture means a positive Borel
probability measure nu on [0,infinity), with every scale finite and
with atoms allowed, satisfying

\[
\frac{A(t)}{A(0)}=\int_{[0,\infty)}e^{-a t^2}\,d\nu(a)
\quad\hbox{for every real }t.                       \tag{1}
\]

## Conclusion

The normalization is legitimate: 0<A(0)<infinity. There exist
epsilon>0, C>0 and R>=0 such that

\[
0<A(t)\le 128C\exp\bigl(-(|t|/2)^{2+\epsilon}\bigr)
\quad (|t|\ge 2R).                                \tag{2}
\]

No measure nu as in (1) exists. This excludes only this sufficient
representation class. It establishes neither a negative Fourier value
nor failure of positive definiteness on the real line. L233's actual
first Laguerre sign, higher/mixed signs, and RH remain unresolved.

## Proof

**Finite positive normalization.** L019 gives k>0 and continuity, with
k(u)<=C_0 exp(9|u|/2-pi exp(2|u|)) for a finite C_0. In particular,
k(u)<=C_1 exp(-|u|) for some finite C_1. Hence

\[
A(0)=\int_{\mathbb R}s^2k(s)^2\,ds
\le C_1^2\int_{\mathbb R}s^2e^{-2|s|}\,ds<\infty.
\]

Its integral on [1,2] is strictly positive: the continuous positive
function k has a positive minimum there. Thus A(0)>0. For each fixed
t, the inequality |s+t|+|s-t|>=2|s| bounds the defining integrand by
C_1^2 s^2 exp(-2|s|), proving finiteness. That integrand is strictly
positive when s is nonzero, so A(t)>0 as well.

**Imported tail and exact normalization.** Use George Csordas,
*Fourier transforms of positive definite kernels and the Riemann
xi-Function*, arXiv:1309.0055v2 (21 February 2014),
[primary text](https://arxiv.org/html/1309.0055v2),
Definition 1.2(v), Theorem 3.5, equation (4.2), and Theorem 4.5
(printed pp.2,6-7,9,11). Write its (4.2) kernel as Phi and its
(4.6) n=1 associated kernel as B_1, to avoid confusing it with local K:

\[
\begin{aligned}
\Phi(v)&=\sum_{n\ge1}\pi n^2(2\pi n^2e^{4v}-3)
                       e^{5v-\pi n^2e^{4v}},\\
B_1(w)&=\int_{\mathbb R}v^2\Phi(v+w)\Phi(v-w)\,dv.
\end{aligned}
\]

Theorem 4.5 asserts that Phi and every complete associated kernel
are admissible. Its proof uses Theorem 3.5 with the strictly
logarithmically concave Phi. Definition 1.2(v), at derivative order
zero, therefore supplies epsilon>0, C>0, R>=0 with
B_1(w)<=C exp(-|w|^(2+epsilon)) for |w|>=R. Evenness extends the
stated positive-axis bound to both tails. This is a cited theorem
application; the general admissibility and log-concavity results are
not reproved here. Neither theorem asserts a Fourier sign.

For u>=0, expansion of the displayed Phi series and L019 gives
K(u)=4Phi(u/2): the coefficients become 8pi^2 n^4 exp(9u/2) and
-12pi n^2 exp(5u/2), with the same exponential factor. Phi is even
by its cited admissibility, so k(u)=4Phi(u/2) for all real u.
Substitute s=2v into the complete integral, retaining both halves
of the real line. The two kernel factors contribute 16, s^2
contributes 4, and ds contributes 2, giving

\[
A(t)=128\int_{\mathbb R}v^2\Phi(v+t/2)\Phi(v-t/2)\,dv
    =128 B_1(t/2).                                  \tag{3}
\]

All these integrals converge absolutely; L019's bounds already
justify the substitution. Applying the imported bound in (3) proves
(2), with the stated constants and eventual range. No finite theta
truncation or estimate for a Fourier transform is being substituted.

**Positive bounded-scale mass contradicts (2).** Suppose (1) holds.
The sets [0,M], with integer M>=1, increase to [0,infinity).
Continuity from below and total mass one imply that for some finite
M>=1 the number m=nu([0,M]) is strictly positive. Positivity of nu
then gives, for every real t,

\[
\frac{A(t)}{A(0)}\ge \int_{[0,M]}e^{-a t^2}\,d\nu(a)
                         \ge m e^{-Mt^2}.           \tag{4}
\]

The endpoint 0 and all atoms in [0,M], including at M, are included.
No density, finite moment, lower support bound, or upper bound on
the whole support has been assumed. There is no scale at infinity
in the measure space; a measure supported entirely at 0 is also
covered by (4).

Set p=2+epsilon>2 and D=128C/(A(0)m)>0. Combining (2) and (4)
forces, for all |t|>=2R,

\[
1\le D\exp\bigl(Mt^2-2^{-p}|t|^p\bigr).            \tag{5}
\]

As |t| tends to infinity, |t|^(p-2) tends to infinity; eventually
2^(-p)|t|^(p-2)>=2M. The right side of (5) is then at most
D exp(-Mt^2), which tends to zero. For a sufficiently large real
t it is strictly less than one, a contradiction. This proves the
exclusion, including all measure endpoints.

The only additional argument beyond the imported tail theorem is
the local normalization and elementary bounded-mass comparison.
This is a specialization of known inputs, not a novelty claim or a
negative actual-Xi Fourier-sign certificate. In particular, the
Gaussian-mixture condition is stronger than real-line positive
definiteness; its failure cannot be substituted for failure of the
first Laguerre inequality.

**Independent audit756 (13 November 2026).** Replayed the complete
proof against L019/L233 and the versioned primary Csordas text above.
Definition 1.2(v) applies at derivative order zero; Theorem 4.5 and
(4.6) concern the full real-line integral, including n=1. Theorem 3.5
asserts tail inheritance as part of admissibility; its displayed proof
expands the two monotonicity cases, not the tail estimate. This proof
imports that theorem and does not claim an independent proof of its
general tail assertion. No RH or associated Fourier positivity is a
hypothesis of that import.

Expanding (4.2) gives exactly the two coefficients of L019 after
multiplication by 4 and substitution v=u/2. Evenness supplies the
negative axis. The factors in (3) are 16 times 4 times 2, with no
half-line factor. L019's bound makes k(u)exp(|u|) bounded on the
whole real line, justifying the single global C_1 used above. The
same C_1 proves convergence for every fixed t; the positive minimum
on [1,2] proves strict positivity without an endpoint assumption.
The eventual source bound has existential epsilon,C,R, and requires
neither an effective onset nor a uniform derivative-order constant.

Finally [0,M], M=1,2,..., exhausts precisely the stated measure space.
Its positive mass m is independent of t. The atom at zero, an atom
at M, and unbounded support are all retained. Dividing by A(0)m is
legitimate; p>2 and M>=1 force the right side of (5) to zero. All
inequalities have the needed direction. No error or unpaid local
hypothesis was found. This validates the existing sufficient-class
stop, without adding a new sign theorem or strengthening its conclusion.

## Mathlib

Full matching and supporting coverage have not been checked. No
absence or matching theorem is claimed. L019 supplies the local
theta bounds, and Csordas's cited theorem supplies admissibility;
neither is a claimed Mathlib formalization. Reference documentation:
https://leanprover-community.github.io/mathlib4_docs/
