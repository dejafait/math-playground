# Corollary C048k: actual Mellin interpolation fails the absolute vertical Rice gate

## Hypotheses

Use precisely the unconditional actual density and interpolation in
L829, and the unconditional entire-continuation construction of
L828 Section2. Write the density as rho to avoid confusing it with
the shifted Mellin parameter:

\[
 P(u)=\Phi(u)=K(u)/2,\quad
 Z=\int_{\mathbb R}P(u)\,du>0,\quad \rho(u)=P(u)/Z,
\]
\[
 M(s)=\int_0^\infty u^{2s}\rho(u)\,du\quad(\Re s>-1/2),\qquad
 E(s)=\frac{\sqrt\pi\,4^{-s}M(s)}{M(0)\Gamma(s+1/2)},\quad M(0)=1/2.
\]

Here P is the even real kernel of those results; its series on u>=0
is the one in C048a. Use C048a's principal Lambert branch and
C048j's audited relative estimate for

\[
 I(p)=2\int_0^\infty u^{2p-1}\Phi(u)\,du\quad(\Re p>0).
\]

Use C028b's actual unshifted coefficients and Jensen polynomial:
\(\gamma_k=k!M_{2k}/(2k)!\),
\(M_{2k}=\int_0^\infty u^{2k}K(u)\,du\), and
\(J_d(x)=\sum_{k=0}^d\binom dk\gamma_kx^k\).
Fix an integer d>=3, put c=-1/4, and define

\[
 B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)}.
\]

No conditional Bernstein representation, Laguerre--Polya membership,
software enclosure from L829's derivative diagnostic, Xi sign, or RH
is assumed. In particular d is fixed during every limit below.

## Conclusion

For every T>0, let R_T be the positively oriented rectangle with
vertical edges Re(s)=c and Re(s)=d+1/2 and horizontal edges Im(s)=+-T.
Then the finite identity is

\[
 \frac{J_d(-1)}{\gamma_0}
   =\frac{(-1)^d}{2\pi i}\int_{\partial R_T}E(s)B_d(s)\,ds.       \tag{1}
\]

The actual weighted interpolation has the strictly positive rate

\[
 \lim_{|t|\to\infty}\frac{\log|E(c+it)B_d(c+it)|}{|t|}
       =\frac\pi2.                                             \tag{2}
\]

The logarithm is defined on both sufficiently distant tails. In
particular, for some T_d and every |t|>=T_d,

\[
 |E(c+it)B_d(c+it)|\ge \exp(\pi|t|/4),\qquad
 \int_{\mathbb R}|E(c+it)B_d(c+it)|\,dt=+\infty.                 \tag{3}
\]

Thus this E on this line fails the absolute vertical Rice opening.
Equation (1) retains all four edges. This result does not establish
failure of a conditionally interpreted integral, all contour methods,
another sample interpolation, or any regularization. It supplies no
sign or height estimate and no resolution of RH. It is a REPRODUCTION
specialization of known Rice and gamma inputs using existing local
Mellin estimates, not a claimed discovery beyond the sources checked.

## Proof

### 1. Imported inputs and exact normalization

Import the finite analytic-contour template from P. Flajolet and
R. Sedgewick, *Mellin transforms and asymptotics: Finite differences
and Rice's integrals*, Theoret. Comput. Sci. **144** (1995),101--124,
[Section2 Lemma1/(6), pp104--105](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf).
It applies to a holomorphic coefficient interpolation on a neighborhood
of the contour and its interior enclosing the selected integers.
The separate unbounded-contour statement Section2/(7), and Section4
Theorem2/proof pp110--111, require growth and closing estimates;
neither is invoked to discard an edge here. Assessment1656 and its
source notes record these distinct hypotheses and inspected proof cases.

Import Legendre duplication from
[DLMF5.5.5](https://dlmf.nist.gov/5.5.E5), at positive half-integers,
and the vertical asymptotic from
[DLMF5.11.9 and its uniformity sentence](https://dlmf.nist.gov/5.11.E9):
for bounded real a, as |t| tends to infinity,

\[
 |\Gamma(a+it)|\sim\sqrt{2\pi}|t|^{a-1/2}e^{-\pi|t|/2}.        \tag{4}
\]

Only the single a=1/4 is needed in (4). These are imported standard
results, not reproved. The finite residue calculation below checks
the actual specialization, normalization and orientation; the Lambert
calculation is needed because none of these citations determines
the growth of this E.

Evenness gives Z=2 integral_0^infinity P(u)du=I(1/2). From the exact
definitions on Re(s)>-1/2,

\[
 M(s)=\frac{I(s+1/2)}{2Z},\qquad
 E(s)=\frac{\sqrt\pi\,4^{-s}I(s+1/2)}{Z\Gamma(s+1/2)}.         \tag{5}
\]

These integrals converge there by boundedness at zero and the
superexponential tail. L828 Section2's Taylor subtraction and
reciprocal-gamma pole cancellation make E entire. This construction
uses only the local analyticity and decay of the actual density;
L828's representation-conditioned identities and zero assertions are
not used. At nonnegative integers, L019/L021 identify
I(k+1/2)=M_{2k}, with Z=M_0=gamma_0. Duplication gives

\[
 (2k)!=4^k k!\Gamma(k+1/2)/\sqrt\pi,\qquad
 E(k)=\frac{k!M_{2k}}{(2k)!\gamma_0}
     =\frac{\gamma_k}{\gamma_0}.                              \tag{6}
\]

Thus neither a missing factor two nor a second factorial occurs.

### 2. Finite rectangle and orientation

E is holomorphic on a neighborhood of the entire closed rectangle,
and B_d has precisely the simple poles 0,...,d inside it. No pole
lies on its boundary for T>0. At k,

\[
 \mathop{\rm Res}_{s=k} E(s)B_d(s)
 =\frac{d!E(k)}{k!(-1)^{d-k}(d-k)!}
 =(-1)^{d-k}\binom dk E(k).
\]

Summing these residues in the positive finite Rice template and
multiplying by (-1)^d gives (1), since (-1)^(2d-k)=(-1)^k and (6)
identifies the finite sum. Positive orientation means the left edge
is traversed downwards: explicitly the contour runs from c-iT to
d+1/2-iT, then upwards, then leftwards, then downwards. If all other
edges could be discarded, the upward left-line prefactor would be
(-1)^(d+1)/(2pi i). No such limiting step is made here.

### 3. Shifted-line applicability and both-sided Mellin control

Take t>0 and p=1/4+it. Then r=|p| tends to infinity and Re(p)>0,
so p lies in C048j's sector for every r>=exp(12). Set L=log r and
w=W_0(2p/pi)=U+iV. C048a gives U>0 and 0<V<pi/2. C048j gives

\[
 I(p)=S(p)(1+\eta(p)),\quad
 |\eta(p)|<\frac{17}{10}\frac{L^{9/2}}r\longrightarrow0,
\]
\[
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\}\ne0.             \tag{7}
\]

Choose a sufficiently large fixed onset at which |eta|<1/2. Then
1-|eta|<=|I/S|<=1+|eta|, so I is nonzero on this tail and
log|I|-log|S|=log|1+eta| tends to zero. This is a lower as well as
an upper comparison. A one-sided upper estimate would not suffice
to establish (3).

### 4. Lambert factor from its exact defining equation

No growing-shift W expansion is assumed. Put theta=arg p. Taking
moduli and arguments in w exp(w)=2p/pi gives

\[
 U+\log|w|=b:=\log(2r/\pi),\qquad
 V+\arg w=\theta.                                            \tag{8}
\]

There is no argument wrapping: U>0 and 0<V<pi/2 imply
0<arg w<pi/2, hence their sum lies in (0,pi), as does theta.
First U tends to infinity. Otherwise a sequence with bounded U,
and bounded V, would make |w|exp(U)=2r/pi bounded, a contradiction.
Once U>=1, (8) implies U<=b and

\[
 |w|\le U+V\le b+\pi/2,\qquad
 b-\log(b+\pi/2)\le U\le b.
\]

Since r/t tends to one, these bounds give U/log t ->1.
Next arg w=arctan(V/U) tends to zero and theta tends to pi/2;
the second identity in (8) therefore gives V->pi/2. Using
arctan x /x ->1 as x->0 now yields

\[
 (\log t)\arg w\longrightarrow\pi/2.                         \tag{9}
\]

All logarithms in (7)--(9) have the principal branch prescribed in
C048a. Taking the real part of the exponent in (7), with a=1/4,
gives the exact real identity

\[
\begin{split}
 \log|S(p)|={}&\log(8\pi^{5/2})+\frac94 U
       -\frac12\log r-\frac12\log|1+w|\\
 &+2a\log(|w|/2)-2t\arg w
       -2\frac{aU+tV}{U^2+V^2}.                              \tag{10}
\end{split}
\]

Indeed Log(w/2)=log(|w|/2)+i arg w and
Re(p/w)=(aU+tV)/(U^2+V^2). The square root in S contributes
one half of log|p(1+w)|, independently of its phase.
The terms in (10) other than -2t arg w are
O(log t)+O(t/(log t)^2): U~log t, V is bounded, and
log|w| and log|1+w| are O(log log t). Consequently (9) and
the both-sided comparison following (7) prove

\[
 \lim_{t\to\infty}\frac{\log t}{t}\log|I(1/4+it)|=-\pi.
                                                                  \tag{11}
\]

In particular log|I(1/4+it)|/t ->0. Formula (11) quantifies
subexponential decay; it does not offset an exponential reciprocal
gamma factor.

### 5. Weighted growth, compact part and divergence

On s=c+it, (5) involves precisely Gamma(1/4+it). Its other scalar
prefactor has the fixed positive modulus sqrt(pi)4^(1/4)/Z.
Equation (4) therefore gives

\[
 \log|E(c+it)|=\log|I(1/4+it)|
       +\frac\pi2t+\frac14\log t+O(1),\qquad t\to\infty.   \tag{12}
\]

For fixed d, each |c+it-k|/t tends to one. There are only d+1
factors, so

\[
 \log|B_d(c+it)|=\log(d!)-(d+1)\log t+o(1).                \tag{13}
\]

Combining (11)--(13), the logarithm of the weighted modulus is

\[
 \frac\pi2t-(\pi+o(1))\frac{t}{\log t}+O_d(\log t).
                                                                  \tag{14}
\]

This proves (2) for positive t. The real density, principal powers
on the positive integration ray, real gamma normalization and real
B_d coefficients give E(c-it)=conjugate(E(c+it)) and the analogous
identity for B_d. Thus the moduli agree on opposite tails, proving
the asserted |t| limit. The large-tail nonvanishing in (7), gamma
finiteness on Re(p)=1/4, and nonvanishing of B_d make all logarithms
used in that limit legitimate.

By (2), the logarithm divided by |t| is at least pi/4 for all
sufficiently large |t|, which proves the pointwise lower bound in
(3). Its integral on even one infinite tail diverges. On every
compact t interval E is continuous and B_d has no pole because
c is not an integer 0,...,d; the compact contribution is finite.
Thus no singular compact piece or deleted origin accounts for
the divergence, and none has been approximated by the large-p bound.

The conclusion holds for each d>=3 separately, without a uniform
T_d or any simultaneous degree/height limit. The polynomial
denominator cannot pay the rate pi/2 at any fixed such degree.
This settles only the approved absolute-convergence gate. It does
not license an unbounded Rice identity, disposal of the other finite
edges, an alternative interpolant, degree-uniform signed comparison,
C028b's H_d=o(d), or an actual-Xi positivity conclusion.

### Independent conceptual audit1659 — 19 November2026

Assessment1657, separately approved in step1658, covers exactly this
fixed-line, fixed-degree audit. The full proof above and C048j's
assembly/audit were read, together with C048a's normalization and
principal-branch proof, L019/L021, C028b's coefficient definitions,
L829's definitions and L828 Section2's unconditional construction.
Source-notes1656 supplies the inspected primary finite Rice and gamma
statements; no further source theorem or stronger source claim is used.
The audit accepts (1)--(3) without a mathematical correction, as a
checked reproduction/specialization, not a new result beyond those
sources. The following are the load-bearing verification checks.

**Density, analyticity and samples.** Since K=2P and P is even,
Z=2 integral_0^infinity P=M_0=gamma_0, while
I(s+1/2)=2 integral_0^infinity u^(2s)P(u)du. Thus M=I/(2Z),
and division by M(0)=1/2 gives precisely (5). L019 supplies the
positive integrable density and every exponential moment; C048a
supplies local even analyticity. These are all the hypotheses used
by L828's Taylor subtraction: its remainder is O(u^(2N+2)), its
continuation has only possible simple poles at -n-1/2, and the
reciprocal gamma cancels those poles. Neither the assumed Bernstein
representation in other parts of L828 nor L829's software diagnostic
is needed. In fact the finite rectangles and the entire vertical
line here already lie inside the original domain Re(s)>-1/2.
Duplication at k+1/2, k>=0, is within its domain and gives (6),
including k=0. The factorial and factor-two normalizations agree
with C028b; the interpolated values are gamma_k/gamma_0.

**Residues and retained edges.** The product of the d nonzero
factors at k is k!(-1)^(d-k)(d-k)!. Multiplying its reciprocal by
d! gives the residue (-1)^(d-k)binom(d,k)E(k). The positive
rectangle therefore gives (1) after multiplication by (-1)^d.
For every T>0, 0,...,d are strictly interior and no other poles
occur. The bottom runs right, the right edge up, the top left and
the left edge down. This checks both the finite identity and the
stated hypothetical upward-line sign. The polynomial-growth and
closing conditions of the unbounded Rice formula are never invoked
or inferred from the finite theorem. All four edges remain present.

**Sector, branch and lower bound.** For t>0, p=1/4+it has positive
real part and eventually |p|>=e^12, so C048j applies on the full
tail, with the same S and principal branches as C048a. Its bound
epsilon=(17/10)(log r)^(9/2)/r tends to zero; no less-than-one
claim at the endpoint r=e^12 is needed. Once epsilon<1/2,
1-epsilon<=|I/S|<=1+epsilon and
|log|I/S||<=2epsilon. This last logarithm is the real logarithm
of a positive modulus; it introduces no choice of a complex log
of I. In particular I cannot vanish there. S is nonzero because
p, w and 1+w are nonzero and its exponential factors never vanish.

Writing w=U+iV, C048a gives U>0 and 0<V<pi/2. Both V+arg(w)
and arg(p) lie in (0,pi), so their equality modulo 2pi from
w exp(w)=2p/pi is an equality without wrapping. The modulus identity
forces U to infinity: a bounded subsequence of U, together with the
bounded V, would bound |w|exp(U), contradicting r tending to infinity.
For U>=1 the two explicit bounds on U in Section4 follow from
1<=|w|<=U+V<=b+pi/2. Since b/log(t)->1, U/log(t)->1.
Then arg(w)=arctan(V/U)->0 and V=arg(p)-arg(w)->pi/2.
More explicitly,

    log(t)*arg(w) = (log(t)/U)*V*
                   (arctan(V/U)/(V/U)) -> pi/2.

This verifies the scale in (9), not just convergence of arg(w) to
zero. The exact real part Re(p/w)=(U/4+tV)/(U^2+V^2) is positive
and O(1/log(t)+t/(log(t))^2). The prefactor and real-log terms in
(10) are O(log(t)); after multiplication by log(t)/t all these
terms tend to zero. The term -2t arg(w) tends to -pi on that
scale, and the two-sided relative comparison changes the logarithm
by o(1). Thus (11) is valid as a limit for every sufficiently large
t, not merely on a sequence and not merely as an upper bound.

**Gamma, polynomial loss and both tails.** The shifted gamma
argument is 1/4+it. DLMF5.11.9 gives its modulus as
sqrt(2pi)t^(-1/4)exp(-pi t/2)(1+o(1)); taking the reciprocal
produces the positive exponential rate and +1/4 log(t) in (12).
The factor 4^(-s) has constant modulus 4^(1/4) on this line.
For each fixed d, the d+1 factors in B_d have modulus divided by
t tending to one, yielding exactly (13). Together with (11),
these verify (14) and its limiting rate pi/2. There is no uniform
estimate in a moving d hidden in this use of a finite product.

The original convergent Mellin integral with a real density gives
conjugation on this line; gamma and B_d have the same symmetry.
Hence the lower tail has the identical modulus and nonvanishing.
The positive limit yields the asserted exp(pi|t|/4) lower bound
on both sufficiently distant tails. On any compact t interval,
E is holomorphic and every factor c+it-k is nonzero, so the
integrand is bounded and its absolute integral finite. Divergence
comes from the infinite tails, not a compact singularity or a
deleted origin. This proves the absolute-opening obstruction.

No numerical evidence, new script or extension of the input audits
is required for these analytic junctions. The direct mathematical
inputs are unchanged. Conditional or regularized integrals, other
interpolants, a simultaneous degree/height limit, signed margins
and actual-Xi transfer remain outside the conclusion. In particular
the accepted stop is neither an off-line zero nor evidence for RH.

## Mathlib

Full matching coverage for this actual-E vertical divergence and
finite Rice specialization has not been checked; availability is
unknown. No absence or formal verification is claimed. The standard
inputs imported above are the precise finite Rice template, gamma
duplication and vertical gamma asymptotic. The actual normalization,
Lambert rate and lower-bound application are the specialization proved
here using C048a/C048j, not a claimed matching Mathlib theorem.
