# C744n: Growing-window half-log bound for corrected neutral modulations

## Hypotheses

Fix ell=log(3)/2, a finite M>=1, and a real nonnegative
chi in C_c^infinity(0,ell), positive on a nonempty open interval.
For T=|t|>1 put

\[
 K(t)=\left\lfloor\frac{\log\log T}{\ell}\right\rfloor,
 \qquad L(t)=K(t)\ell.
\]

When K(t)>=2, use precisely L744(1)'s family F_(K(t),M):
w=sum_(j=0)^(K(t)-1) w_j(x-j ell), with complex
w_j in C_c^infinity(0,ell), ||w||_2=1 and
||w||_(H2(R))<=M. Extensions are by zero and
||w||_(H2)^2=||w||_2^2+||w'||_2^2+||w''||_2^2.
Use L744(3)'s unchanged complex-linear correction:

\[
 \begin{split}
 b_\tau(s)&=\chi(s)e^{\tau s/2},\quad
 G_{\sigma\tau}=\int_0^\ell\chi(s)e^{(\sigma+\tau)s/2}\,ds,\\
 d_{j,\sigma}&=e^{itj\ell}\int_0^\ell e^{\sigma s/2}w_j(s)e^{its}\,ds,\\
 h_{t,w}(x)&=\sum_{j,\tau}(G^{-1}d_j)_\tau b_\tau(x-j\ell),
 \qquad v_{t,w}=e^{itx}w-h_{t,w},\quad \sigma,\tau\in\{+1,-1\}.
 \end{split}                                                     \tag{1}
\]

L743(9) establishes invertibility of this fixed G. The complete
energy is E_L(f)=-Re<A_L f,f> for L740's generator, in the
original unweighted L2 space, with first-slot-linear inner product.
No RH assumption or finite positivity computation is used.

The arithmetic import is Rosser and Schoenfeld, *Approximate formulas
for some functions of prime numbers*, Illinois J. Math. 6(1) (1962),
64-94, [Theorem 12, (3.35), printed p.71](https://doi.org/10.1215/ijm/1255631807):
psi(x)=sum_(n<=x) Lambda(n)<1.03883x for every real x>0.
This includes all prime powers. The primary theorem and proof routing
were inspected in the prior assessment
`drafts/literature/2026-11-11-growing-window-modulation-494.md`;
its numerical tables are imported as part of that theorem, not replayed.
The other named imports, already specialized in L744, are Plancherel
and Fourier differentiation, and [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2)
with its [complex remainder, 5.11(ii)](https://dlmf.nist.gov/5.11#ii).

## Conclusion

There exists T_*(M,chi)<infinity such that for every real t with
T=|t|>=T_*, K(t)>=2 and every w in F_(K(t),M),
v_(t,w) belongs to D(A_(L(t))), has exactly zero cellwise and global
exponential moments of both signs, and satisfies

\[
 \|v_{t,w}\|_2^2\ge\frac14,\qquad
 \boxed{\ E_{L(t)}(v_{t,w})\ge
                    \frac{\log|t|}{2}\|v_{t,w}\|_2^2\ }.          \tag{2}
\]

The single onset is independent of w and the resulting K(t), and
works for both signs of t. An empty family makes no existence claim.
This is a REPRODUCTION using the assessed standard high-frequency
mechanism. It is a local quantifier extension of L744, not a claim
of novelty beyond the literature checked. The separate conceptual audit
below (11 November 2026, step498) accepts (2) with these exact hypotheses;
it makes no assertion for unrestricted mixtures or bounded carriers.

## Proof

### Uniformity of the explicit fixed-window estimates

We use L744's displayed estimates, rather than substituting K(t)
into its fixed-K asymptotic conclusion. First let K>=2 be any finite
integer, set L=K ell, and keep M,chi fixed as above.
For each such K, both f=e^(itx)w and h in (1) are smooth and compactly
supported in (0,L). L744's smooth-domain argument, using L740(3),
therefore puts v=f-h in D(A_L). This membership requires no uniform
bound on the domain norm as L grows.

Write F_g(xi)=integral g(x)e^(-i xi x)dx and
m(xi)=Re psi(1/4+i xi/2)-log pi. L744(5)-(7), using L741's
full-line scalar/kernel identities restricted to this finite interval,
give

\[
 E_L(v)=Q_m(v)-\langle B_Lv,v\rangle,\qquad
 Q_m(g)=\int_{\mathbb R}m(\xi)|F_g(\xi)|^2\frac{d\xi}{2\pi},
 \quad B_L=\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}
                         (T_{\log n}+T_{\log n}^*).             \tag{3}
\]

Indeed G(G^-1 d_j)=d_j kills each local moment
integral_0^ell e^(sigma s/2)v(s+j ell)ds exactly. Thus
F_v(sigma i/2) is a finite sum of zeros multiplied by
e^(sigma j ell/2), and is zero for each sigma. The full complex pole
product in L744(6) vanishes exactly, regardless of the size of these
weights. All kernel pairings take place on a finite square for each
K; there is no infinite-window limit or discarded pole term in (3).

For completeness specify the constants in the uniform error. Put

\[
 \begin{split}
 A&=2+8\sqrt2/3+\log(4\pi),\qquad c_T=\log(T/(2\pi)),\\
 R_\chi&=\|G^{-1}\|
       (\|b_+\|_{H^2}^2+\|b_-\|_{H^2}^2)^{1/2},\\
 H&=R_\chi\sqrt{33\ell e^\ell/8}\,M,\qquad
 \delta(T)=H/T^2,\qquad U(T)=A+\log(2+T)+3+M^2,\\
 a(T)&=\frac{2M}{T}+\frac{8+4M^2}{T^2}
 +\frac{16M^2}{T^4}[A+\log3+3+\log(2\pi)+\log T],\\
 b(T)&=2\sqrt{U(T)(A+3)}\,\delta(T)+(A+3)\delta(T)^2,\\
 \varepsilon(T)&=
 \frac{a(T)+b(T)+|c_T|(2\delta(T)+\delta(T)^2)}
 {(1-\delta(T))^2}
 \quad\left(T\ge T_0:=\max\{2,\sqrt{2H}\}\right).
 \end{split}                                                     \tag{4}
\]

None of these constants or functions contains K. Their estimates
are valid simultaneously for all finite K, for the following reasons.

The zero-extended w has unit L2 norm, and Plancherel gives
integral(1+eta^2+eta^4)|F_w(eta)|^2 deta/(2pi)<=M^2.
L744(8)'s scalar bounds hold on the full real line, independent of
support. Its split at |eta|=T/2 and fourth-moment tail estimates
therefore give |Q_m(f)-c_T|<=a(T) for every such K. In particular
the possibly low frequency t+eta near zero is included, not removed.
The same moment bound gives ||f||_W^2<=U(T), where
W(xi)=A+log(2+|xi|). Both assertions apply for positive and negative t.

For the correction, two integrations by parts have no endpoint
terms in any cell, since each w_j is compactly supported there.
Exactly as in L744(12),

\[
 \sum_j|d_j|^2\le\frac{33\ell e^\ell}{8T^4}
                       \sum_j\|w_j\|_{H^2}^2
 \le\frac{33\ell e^\ell M^2}{8T^4}.                            \tag{5}
\]

The equality ||w||_(H2)^2=sum_j||w_j||_(H2)^2 follows from disjoint
supports of the zero-extended derivatives through order two. Applying
the fixed two-dimensional inverse G^-1 on each cell and summing the
squared H2 norms of the corrections proves ||h||_(H2)<=delta(T).
There is no factor K, even when the number of cells grows.
Since W<=(A+3)(1+xi^2), also
||h||_W<=sqrt(A+3)delta(T). Weighted Cauchy--Schwarz with |m|<=W
then gives |Q_m(v)-Q_m(f)|<=b(T), as in L744(13)-(14).
Translations of the cells do not affect these derivative norms or
the modulus of their phase factors e^(itj ell).

Writing N=||v||_2^2, the triangle inequality now gives, for T>=T_0,

\[
 N\ge(1-\delta(T))^2\ge\frac14,\qquad
 |N-1|\le2\delta(T)+\delta(T)^2,\qquad
 \left|\frac{Q_m(v)}{N}-c_T\right|\le\varepsilon(T).              \tag{6}
\]

For the last inequality expand Q_m(v)/N-c_T as
[Q_m(v)-c_T+c_T(1-N)]/N. This retains the norm-defect term
|c_T|(2delta+delta^2) in (4). All preceding estimates concern a finite
smooth function for each K; neither a compactness argument over
supports nor a limit of operators was used.

Directly from (4), a(T)=O_M(T^-1), b(T)=O_(M,chi)(T^-2 sqrt(log T)),
and |c_T|(2delta+delta^2)=O_(M,chi)(T^-2 log T).
The denominator is at least 1/4. Hence epsilon(T)=O_(M,chi)(T^-1)
and tends to zero. Here ell is fixed throughout. This proves the
uniform decay from its explicit expression, rather than reusing
L744's K-dependent big-O label.

### Full prime payment and one eventual onset

Let C=1.03883 and X=e^L>1. Every delay and its adjoint in (3) is a
contraction, so

\[
 \langle B_Lv,v\rangle\le
 C_{\rm prime}(L)N,\qquad
 C_{\rm prime}(L)=2\sum_{2\le n<X}\frac{\Lambda(n)}{\sqrt n}.
                                                                    \tag{7}
\]

We bound the strict cutoff by the inclusive sum; its terms are
nonnegative. Abel summation, including the possible atom at X, gives

\[
 \sum_{2\le n\le X}\frac{\Lambda(n)}{\sqrt n}
 =\frac{\psi(X)}{\sqrt X}
   +\frac12\int_1^X\frac{\psi(u)}{u^{3/2}}\,du
 \le C\sqrt X+\frac C2\int_1^X u^{-1/2}du
 =2C\sqrt X-C.
                                                                    \tag{8}
\]

There is no n=1 contribution since Lambda(1)=0. The imported psi
bound applies for every u in this integral and does not discard
prime powers. Thus C_prime(L)<=4C sqrt(X)-2C<=4C e^(L/2),
retaining the full factor two in (7).

Now choose K=K(t). Its floor relation yields L<=log log T, hence
X<=log T and C_prime(L)<=4C sqrt(log T). Equations (3), (6), (7)
therefore prove, simultaneously for every admitted w and both signs,

\[
 \frac{E_{L(t)}(v_{t,w})}{\|v_{t,w}\|_2^2}
 \ge \log T-\log(2\pi)-4C\sqrt{\log T}-\varepsilon(T).
                                                                    \tag{9}
\]

By the proved uniform decay, choose T_epsilon>=T_0, depending only
on M,chi, such that epsilon(T)<=1 for all T>=T_epsilon. One
sufficient single onset is

\[
 T_* =\max\left\{T_\varepsilon,
  \exp\!\left(\max\{3,(16C)^2,4(\log(2\pi)+1)\}\right)\right\}.
                                                                    \tag{10}
\]

For y=log T and T>=T_*, y>=3 gives log log T>=log3=2ell, so K(t)>=2.
Also 4C sqrt(y)<=y/4 and log(2pi)+epsilon(T)<=y/4.
The right side of (9) is consequently at least y/2, proving (2).
No numerical value or sharpness of T_epsilon is claimed.

### Qualifications and downstream use

The achieved threshold is the stated half-log Rayleigh lower bound,
with a uniform nonzero denominator and one M,chi-dependent onset.
It pays only these corrected modulations with a fixed global H2
bound and the specified support rate. It does not sign arbitrary
supported profiles, bounded-carrier tests, their moment complements,
or their signed cross terms. No simultaneous-return condition is
needed, and no prime-only Rayleigh equality is used.

In particular this does not reopen L742's conditional summability
obstruction or L750's failed corrected-localization inequality.
Those assembly mechanisms are independent of the present estimate.
The actual-Xi positivity gap L030-L032/C032a remains unresolved.

### Separate conceptual audit (11 November 2026, step498)

**Verdict.** The unchanged assertion (2) passes. This is a REPRODUCTION
audit under the prior SPECIALIZE assessment
`drafts/literature/2026-11-11-growing-window-modulation-audit-496.md`.
It verifies the simultaneous quantifiers, rather than substituting a
varying K into L744's fixed-K asymptotic. No repair, new theorem beyond
the sources checked, numerical positivity computation, or RH premise
is required. The following checks concern all finite K before the
prescribed K(t) is chosen.

**Finite-window domain and complete scalar.** For any fixed finite K,
the finite sums f,h,v have smooth compact support in (0,L). For such
a function g, absolute Fubini writes L740's Phi_g as
integral_0^x [(x-z)log(x-z)-(x-z)]g'(z)dz. Differentiating this
absolutely continuous integral gives
Phi_g'(x)=integral_0^x log(x-z)g'(z)dz, bounded by
||g'||_infinity integral_0^L |log u|du. Hence g belongs to L740(3)'s
actual domain. This bound may depend on g,L; uniformity of that domain
norm is neither needed nor claimed.

L741(9) is a full-line distribution identity, and its (13)-(16) use
an L1 kernel r with
r-hat(i xi)=log(1+i xi)-psi(1/4+i xi/2)-log2.
Substitution in L740(5), with q-d_0=r-4cosh, gives L744(5) for this
finite L, with the complete P_L. The negative real part of
-log(1+i xi)+log(2pi)+r-hat(i xi) is exactly
Re psi(1/4+i xi/2)-log pi=m(xi). The gamma has already entered
L741(9); no extra scalar is missing. Smooth Fourier transforms are
Schwartz, so the multiplier pairing is finite. The remaining causal
cosh pairing is on a finite square, not on the full line.

**Complex poles and arithmetic normalization.** With the first-slot-
linear convention, put
I=Re(F_g(i/2) overline(F_g(-i/2))). On the finite square, symmetrizing
e^((x-y)/2) against Re(g(x)overline(g(y))) replaces it by
cosh((x-y)/2). Symmetry then gives I=2 Re<V_L g,g>. Thus the energy
contains +2I, exactly as in L744(6); it is not a modulus square.
The matrix G is the fixed positive definite Gram matrix established
in L743(9). Its complex-linear inverse satisfies GG^-1 d_j=d_j,
without conjugating d_j, and kills both local moments exactly.
Consequently each global moment is a finite sum of exact zeros times
e^(sigma j ell/2). Increasing these weights creates no residual.
Both poles in the complex product vanish, proving their omission in
(3) is exact. Also
Re<P_L v,v>=2 sum_n Lambda(n)/sqrt(n) Re<T_(log n)v,v>
=<B_L v,v>. This verifies the sign and factor in (3). The delay at
log n=L acts as zero almost everywhere; every smaller prime-power
delay is included. No small-window sign conclusion of L741 is used.

**Global scalar and shifted Fourier error.** Reuse the cited DLMF
remainder, not a new asymptotic theorem. On z=1/4+i xi/2 its secant
factor is at most 2sqrt2. For |xi|>=1 the errors between
Re psi(z) and log(|xi|/2) are bounded respectively by
1/(8xi^2), 1/(2xi^2), and 2sqrt2/(3xi^2); their constants sum to
less than 2. For |xi|<=1, 1/4<=|z|<1 gives |m(xi)|<=A.
For |xi|>=1, A>=2+log(2pi) extends this to the global bound
|m(xi)|<=A+log(2+|xi|)=W(xi). Thus there is no use of log|xi|
at zero.

The probability measure dmu=|F_w(eta)|^2 deta/(2pi) has
integral(1+eta^2+eta^4)dmu<=M^2 and integral|eta|dmu<=M,
independently of K. For either sign of t, |eta|<=T/2 implies
|t+eta|>=T/2>=1 and
|m(t+eta)-c_T|<=2|eta|/T+8/T^2. On the complement,
|t+eta|<3|eta| gives the bound
A+log3+3+log(2pi)+log T+eta^2. The complement has mass at most
16M^2/T^4 and second moment at most 4M^2/T^2, by its fourth
moment. Integrating gives every term of a(T) in (4), including
frequencies near t+eta=0. Finally
2+|t+eta|<=(2+T)(2+|eta|) and log(2+r)<=3+r^2 give
||f||_W^2<=A+log(2+T)+3+M^2=U(T). None of these facts uses support
size or a profile-dependent convergence rate.

**Correction and denominator uniformity.** In each cell, w_j and
its first derivative vanish near both endpoints. Two integrations
by parts therefore give
|d_(j,sigma)|<=T^-2 sqrt(ell)e^(ell/2)(sqrt(33)/4)||w_j||_(H2):
the derivative combination is w_j''+sigma w_j'+w_j/4, whose
coefficient squared norm is 33/16. Summing the two signs produces
33ell e^ell/8. For derivatives of order 0,1,2, different translated
cells have disjoint supports. Their squared norms add exactly; there
are no distributional boundary jumps for these smooth zero extensions.
Thus the sum over cells is ||w||_(H2)^2<=M^2, proving (5) without
a factor K. Applying the same Hilbert-space two-term bound to
sum_tau (G^-1 d_j)_tau b_tau and again summing squares gives
||h||_(H2)<=H/T^2=delta(T). Translation and the phase e^(itj ell)
do not enlarge these bounds; ell,chi,G are fixed.

Since W<=(A+3)(1+xi^2), ||h||_W<=sqrt(A+3)delta. The bound
|m|<=W gives weighted Cauchy--Schwarz even where m is negative.
Expansion of Q_m(f-h) consequently gives precisely b(T), including
its factor two on the mixed term. At T>=T_0, delta<=1/2, so
||f-h||_2>=1-delta may legitimately be squared to give N>=1/4.
The inequality |N-1|<=2delta+delta^2 and the identity
Q_m(v)/N-c_T=[Q_m(v)-c_T+c_T(1-N)]/N give (6), with the necessary
norm-defect term multiplied by |c_T|. This avoids the all-T squaring
defect repaired in L744's earlier audit. All parameters in (4) depend
only on M,chi and the fixed ell. In particular epsilon(T)=O(T^-1)
with those dependencies: its additional terms are
O(T^-2 sqrt(log T)) and O(T^-2 log T), and its denominator is at
least 1/4. This is a uniform bound on an explicit function, not an
interchange of quantifiers in fixed-K big-O notation.

**Full arithmetic payment and simultaneous onset.** Every T_a and
its adjoint has norm at most one, so the absolute value of
<B_L v,v> is at most the entire coefficient mass in (7) times N.
The Rosser--Schoenfeld theorem cited above applies to all real u>0
and includes prime powers. Finite Abel summation with the inclusive
psi gives (8), even when X is itself a prime power: its endpoint
atom is present in psi(X)/sqrt(X). The lower endpoint contributes
nothing since psi(1)=0. Replacing the strict sum by the inclusive
one is an upper bound because Lambda(n)>=0. Integration therefore
gives 2C sqrt(X)-C, and the operator's factor two gives
C_prime(L)<=4C sqrt(X)-2C<=4C e^(L/2). No arithmetic cancellation
or zero-free estimate is assumed.

For the stipulated floor, L<=log log T, so e^L<=log T and (9)
follows for both signs of t and every admitted w. Uniform decay of
the explicit epsilon supplies a single T_epsilon(M,chi), with
epsilon(T)<=1 for every T>=T_epsilon. For y=log T above (10)'s
threshold, y>=3 implies log y>=log3=2ell and hence K(t)>=2.
The inequality y>=(16C)^2 implies 4C sqrt(y)<=y/4; independently,
y>=4(log(2pi)+1) implies log(2pi)+epsilon(T)<=y/4.
Subtracting both payments from y leaves y/2. Together with N>=1/4
this proves exactly (2), with one onset independent of w,K(t).
No monotonicity of epsilon, effective numerical onset, existence of
an admitted profile for every M, or limit of operators is needed.

**Use and limitations.** This audit makes C744n available only as
the stated growing-window high-carrier estimate. The direct local
input uses remain L740, L741, L743 and L744; no DAG change is needed.
The L742 summability and L750 corrected-IMS stops are contrasts,
not premises and not repaired by (2). The sign of bounded carriers,
the mixed Hermitian pairing with them, moment complements, arbitrary
profiles and support-uniform assembly remain unresolved. Successful
verification of this specialization supplies no additional RH sign.

## Mathlib

Full matching Mathlib coverage of (2), including this complete energy,
varying support and exact correction, has not been checked. No claim
of absence or formal verification is made. Supporting named inputs
are the Fourier identities, DLMF's scalar remainder, Abel summation
and the precisely cited Rosser--Schoenfeld theorem. This proof supplies
the specialization and its uniformity qualifications; it does not
reprove those imported results.
