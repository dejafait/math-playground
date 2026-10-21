# Lemma 386: negative logarithmic dyadic mean of the signed residual

## Hypotheses

Use the actual F_0,G,A of L366, the carrier of L368 and L380, and
L370's ordinary derivatives. For t>0 put T=1+t, L=log(2+t),
f=F_0/A, g=G/A, w=fg'−f'g and k=f'g''−f''g'. All functions are
fixed as H tends to infinity. No RH, simplicity, noncoincidence,
physical discriminant sign or common-zero count bound is assumed.

## Conclusion

With S=ζ(5)ζ(3)²/ζ(6)>0,

\[
 \frac1H\int_H^{2H}\frac{-4w(t)k(t)}{T^4L^4}\,dt
   =-\frac{S}{192\pi^2}\log H+o(\log H).                 \tag{1}
\]

In particular this residual is negative somewhere in every sufficiently
high dyadic interval. Constants and the onset are not numerically
evaluated. This is one term of L370, not the mean of its full
discriminant: the separate w'-square term can contribute at this scale.
No pointwise discriminant sign, total L367 margin, actual-theta
positivity, common-zero bound or RH consequence follows.

This is a **REPRODUCTION** under the previously saved SPECIALIZE
assessment `drafts/literature/2026-10-10-signed-residual-mean-calculation.md`.
It is a local specialization of known moment tools, with no originality
beyond the checked sources claimed. The separate critical audit below
validates the stated asymptotic without a mathematical repair.

## Proof

### 1. Imported holomorphic moment and its order-two application

Write ℓ=log H and U(t)=ζ(1/2+it). We import M. P. Young,
*A short proof of Levinson's theorem*, Arch. Math. **95** (2010),
539–548, DOI 10.1007/s00013-010-0199-9, Lemmas 4–5,
(4.1)–(4.5), pp. 542–543, and the Cauchy argument following
(3.4), p. 541, in the
[primary published PDF](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
We use the audited application in L381, section 2 and its critical
audit, rather than reprove Young's theorem or its off-diagonal estimates.

Specifically, fix positive integers h,k and a fixed smooth real weight
η, 0≤η≤1, supported in [H/2,3H], with η^(a)=O_a(H^(−a)).
Its rescaled shape is fixed before H grows. Young's parameter is 2H;
the support and derivative scale 2H/log(2H) conditions hold. For any
fixed 0<θ<1/2, hk≤(2H)^(2θ) eventually. All shifts below have
size O(1/ℓ). No gamma phase is inserted in this slow weight.

Let d=gcd(h,k), and let I(α,β) denote the integral of
η(t)(h/k)^(−it)ζ(1/2+α+it)ζ(1/2+β−it).
L381's audited two-diagonal calculation gives, on the product contours
|α|=1/ℓ, |β|=2/ℓ,

\[
 I(\alpha,\beta)-\frac d{\sqrt{hk}}\int\eta(t)
       \int_0^{\log(t/(2\pi))}e^{-(\alpha+\beta)v}\,dv\,dt
       =O_{h,k,\eta}(H).                              \tag{2}
\]

Both terms on the left extend holomorphically to the full product
disks. In particular the shift-sum singularity is removed before
differentiation. This imports both functional-equation diagonals,
the large-Mellin-height bounds and both off-diagonal orderings of L381;
it does not differentiate an error known only for real shifts.

For 0≤j,k_1≤2 apply product Cauchy to (2). The derivative error
is O(Hℓ^(j+k_1)). Ordinary real derivatives contribute i^j(−i)^k_1,
whereas derivatives of e^{−(α+β)v} contribute (−1)^(j+k_1).
Thus, with a=j+k_1 and c_{j,k_1}=(−i)^j i^k_1/(a+1),

\[
 \int\eta(t)(h/k)^{-it}U^{(j)}\overline{U^{(k_1)}}\,dt
 =\frac d{\sqrt{hk}}c_{j,k_1}
     \int\eta(t)\log^{a+1}(t/(2\pi))\,dt
       +O_{h,k,\eta}(H\ell^a).                        \tag{3}
\]

The conjugate in (3) is the conjugate of the ordinary real derivative.
In particular c_{1,1}=1/3, c_{1,2}=i/4, and c_{2,2}=1/5.
The last sign and the i in the mixed moment are essential here.
Taking h=k=1 and a fixed positive majorant equal to one on [H,2H]
gives, for j=0,1,2,

\[
 \|U^{(j)}\|_H=O(\ell^{j+1/2}),\qquad
 \|a\|_H^2=H^{-1}\int_H^{2H}|a(t)|^2dt.                \tag{4}
\]

### 2. Signed sharp endpoints and all right-line coefficients

Put Z=ζ(5/2+it), Z_N=Σ_{n≤N}n^(−5/2−it), and
S_N=Σ_{m,n≤N}gcd(m,n)/(m³n³). At fixed N, expanding |Z_N|²
in (3) retains every rational twist, including every unequal pair:

\[
 \int\eta U^{(j)}\overline{U^{(k_1)}}|Z_N|^2dt
 =S_Nc_{j,k_1}\int\eta\log^{a+1}(t/(2\pi))dt
       +O_{N,\eta}(H\ell^a).                         \tag{5}
\]

Here is the signed unsmoothing argument. Fix 0<ε<1/4 and take η
equal to one on [H+εH,2H−εH], zero outside [H,2H], and between
zero and one elsewhere. The difference from the sharp integral is
supported in two intervals of total length 2εH. Choose a nonnegative
smooth majorant q_ε for these intervals, supported in slightly larger
intervals inside [H/2,3H], bounded by one, with integral O(εH).
It has fixed rescaled shape at fixed ε. Formula (3) with h=k=1
and j=k_1 gives

\[
 \limsup_{H\to\infty}
 \frac{\int q_\varepsilon|U^{(j)}|^2dt}{H\ell^{2j+1}}
       \le C_j\varepsilon.                           \tag{6}
\]

The constants in the error of (3) can depend on ε; they vanish in
this limit at each fixed ε. The main-term constants C_j do not.
Since |Z_N|≤ζ(5/2), Schwarz and (6) bound the absolute endpoint
error in (5), divided by Hℓ^(a+1), by O(ε) in limsup.
This works for the complex mixed moment; no order or nonnegative
bracketing is applied to it. Let H grow at fixed N,ε, then ε decrease
to zero. The sharp normalized limit in (5) is S_Nc_{j,k_1}.

L368 (5), from the absolute Dirichlet series
[DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1) on Re s>1, gives

\[
 M_j=\sum_{n\ge1}(\log n)^j n^{-5/2}<\infty,\qquad
 \rho_j(N)=\sum_{n>N}(\log n)^j n^{-5/2}\to0,
 \quad |Z^{(j)}-Z_N^{(j)}|\le\rho_j(N),\quad j\le2.    \tag{7}
\]

The convention at n=1 is 1 for j=0 and 0 otherwise. Since
||Z|²−|Z_N|²|≤2M_0ρ_0(N), (4) and Schwarz show that replacing
|Z_N|² by |Z|² in the sharp normalized moment costs at most
Cρ_0(N), uniformly for large H. L381's absolutely convergent gcd
grouping gives S_N→S=ζ(5)ζ(3)²/ζ(6); no unequal-pair term is lost.
Taking N to infinity after the height and smoothing limits proves

\[
 \frac1H\int_H^{2H}U^{(j)}\overline{U^{(k_1)}}|Z|^2dt
      =S c_{j,k_1}\ell^{j+k_1+1}+o(\ell^{j+k_1+1}).    \tag{8}
\]

### 3. Complete ordinary-jet algebra and lower-order errors

Use L366, L368 and L380 to write

\[
 Q=Ae^{i\phi},\quad \omega=\phi',\quad
 b=(t^2/4-3/16-it/2)/\pi,\quad V=bZ,
 \quad r=e^{i\phi}U\in\mathbb R,\quad h=e^{i\phi}V.
\]

Exactly f=−r and g=Re h, so w=−Re X and k=−Re Y, where

\[
 X=rh'-r'h=e^{2i\phi}(UV'-U'V),                       \tag{9}
\]
\[
 \begin{split}
 Y=r'h''-r''h'=e^{2i\phi}\{&U'V''-U''V'
       +i\omega(UV''-U''V)\\
       &-(\omega^2+i\omega')(UV'-U'V)\}.             \tag{10}
 \end{split}
\]

For verification of (10), use
r'=e^{iφ}(U'+iωU),
r''=e^{iφ}(U''+2iωU'+(iω'−ω²)U), and the same formulas for h.
The U'V' and UV terms cancel. The remaining U'V coefficient is
ω²+iω', and the UV' coefficient is −ω²−iω', giving (10).
These identities divide by no function value and include all zeros.
They use g=G/A itself; derivatives of the polynomial b are retained.

Set

\[
 X_0=-be^{2i\phi}U'Z,\qquad
 Y_0=be^{2i\phi}Z(\omega^2U'-i\omega U'').           \tag{11}
\]

On [H,2H], |b|=O(H²), |b'|=O(H), b''=1/(2π).
Equations (7) give |V|+|V'|+|V''|=O(H²), with complete series.
The separately controlled carrier estimates in L368/L380 give
ω=½log(t/(2π))+O(H^(−2)) and ω'=O(H^(−1)).
Now X−X_0=e^{2iφ}UV'. The exact remainder of Y after (11) is

\[
 e^{2i\phi}\{U'V''-U''V'+i\omega UV''
       -(\omega^2+i\omega')UV'+i\omega'U'V\}.        \tag{12}
\]

Using (4) on every term proves

\[
 \|X_0/(T^2L)\|_H+\|Y_0/(T^2L^3)\|_H=O(\sqrt\ell),
 \quad
 \|(X-X_0)/(T^2L)\|_H+
 \|(Y-Y_0)/(T^2L^3)\|_H=O(\ell^{-1/2}).              \tag{13}
\]

For example the largest terms U''V' and ω²UV' in (12) each have
norm O(H²ℓ^(5/2)); the divisor is comparable to H²ℓ³.
The retained Y_0 terms have norm O(H²ℓ^(7/2)). All coefficients
are bounded uniformly on the interval, so these are estimates with
the exact moving T,L. Schwarz shows that replacing X,Y by X_0,Y_0
in the average of X conjugate(Y)/(T⁴L⁴) costs O(1).

The order-two tails have not been omitted: X,Y are linear in V,V',V''.
Replacing Z by Z_N in (9)–(10) gives, with ρ=ρ_0+ρ_1+ρ_2,
norm differences at most Cρ√ℓ for each normalized factor in (13).
The full and truncated normalized factors have norm at most C√ℓ,
uniformly in N. Thus either product, or the product of their real
parts, changes in sharp mean by at most Cρℓ. This supplies full
order-two tail transfer, independently of pointwise convergence.
For the leading opposite-height mean (8) only ρ_0 is needed; for
(12) the finite M_1,M_2 already give the stronger O(1) error.

### 4. Complete same-height projection on a height rectangle

The real-part identity, with no phase averaging assumption, is

\[
 \frac{-4wk}{T^4L^4}
   =-2\operatorname{Re}\frac{X\overline Y+XY}{T^4L^4}. \tag{14}
\]

We estimate XY for the complete expressions, not just (11).
Use L381's holomorphic height functions on
H≤Re τ≤2H, 0≤Im τ≤1:

\[
 B(\tau)=\zeta(1/2-i\tau),\quad Z(\tau)=\zeta(5/2+i\tau),
 \quad \Omega(\tau)=\tfrac14[
 \Psi(1/4+i\tau/2)+\Psi(1/4-i\tau/2)-2\log\pi].
\]

Here Ψ=Γ'/Γ. All derivatives now mean holomorphic τ derivatives.
Let V=bZ and put

\[
 J_0=B,\quad J_1=B'-2i\Omega B,\quad
 J_2=B''-4i\Omega B'-(4\Omega^2+2i\Omega')B,
\]
\[
 X_*=J_0V'-J_1V,
\]
\[
 Y_*=J_1V''-J_2V'+i\Omega(J_0V''-J_2V)
                    -(\Omega^2+i\Omega')(J_0V'-J_1V). \tag{15}
\]

On the bottom edge L380's reflection gives e^{2iφ}U=B;
differentiating once and twice gives e^{2iφ}U'=J_1 and
e^{2iφ}U''=J_2. Consequently X_*=X and Y_*=Y exactly there.
This accounts for all carrier terms, including Ω'.

Every function in
P(τ)=X_*(τ)Y_*(τ)/[(1+τ)^4 log^4(2+τ)] is holomorphic in a
neighborhood of the rectangle. Use the logarithm branch in Re(2+τ)>0.
Zeta and polygamma poles here would require Re τ=0, outside the
rectangle; the divisor has no zero there. There is no contour residue.

For completeness the order-two edge estimates are as follows. L320's
strip bound, divided by the completed gamma and polynomial factors,
is exactly L381 (18): |ζ(σ+iv)|≤C H^(3/4−σ/2) in the positive
strip needed here up to σ=3/2. On logarithmic-radius disks of radius
1/ℓ about x+iy, L381's argument gives

\[
 |B^{(j)}(x+iy)|\le C_j\ell^j H^{1/2-y/2},
          \quad j=0,1,2,\quad 0\le y\le1.             \tag{16}
\]

Indeed the disk changes the exponent by at most 1/(2ℓ), a bounded
factor, and Cauchy supplies j!ℓ^j. If a disk crosses σ=3/2,
absolute convergence on that portion gives the same bound, since
1/2−y/2≥0. All Z disks lie in Re s≥3/2−1/ℓ>1, so its first
two jets are uniformly bounded by absolute series there. Also
|V^(j)|≤CH² for j≤2 throughout the rectangle.

The paired digamma expansion gives Ω=O(ℓ); its separately bounded
polygamma derivative gives Ω'=O(H^(−1)). These are the
sector-qualified tools of L368 (7)–(8), extended to the bounded
height rectangle: both gamma arguments have imaginary magnitude
comparable to H and stay away from the negative real axis.
For example Ω'=i[Ψ'(1/4+iτ/2)−Ψ'(1/4−iτ/2)]/8 and each
Ψ' is O(H^(−1)). No asymptotic error is differentiated.
Thus |J_j|≤Cℓ^j H^(1/2−y/2), and (15) gives on both vertical edges

\[
 |X_*|\le CH^2\ell H^{1/2-y/2},\qquad
 |Y_*|\le CH^2\ell^3 H^{1/2-y/2},\qquad
 |P|\le C H^{1-y}.                                  \tag{17}
\]

On the top edge B and Z and their first two jets are absolutely
bounded on Re s=3/2. Formula (15), including all Ω powers, then
gives |P|≤C along the entire top edge. Cauchy's integral theorem
and the two full vertical edges therefore imply

\[
 \left|\frac1H\int_H^{2H}\frac{XY}{T^4L^4}\,dt\right|
 \le C+\frac C H\int_0^1 H^{1-y}dy=O(1).             \tag{18}
\]

This is a sharp-interval contour estimate with all endpoints retained.
It uses full right-line functions, has no smoothing limit, and inserts
no fast carrier into Young's weight.

### 5. Coefficient and error comparison

From (11),

\[
 \operatorname{Re}(X_0\overline{Y_0})
 =-|b|^2|Z|^2\{\omega^2|U'|^2
                         +\omega\operatorname{Re}(iU'\overline{U''})\}.
                                                               \tag{19}
\]

Uniformly on the sharp interval,
|b|²/T⁴=1/(16π²)+O(H^(−1)), L=ℓ+O(1), and ω=ℓ/2+O(1).
In particular ω²/L⁴=1/(4ℓ²)+O(ℓ^(−3)) and
ω/L⁴=1/(2ℓ³)+O(ℓ^(−4)). By (4), boundedness of Z and Schwarz,
the errors in freezing these coefficients in the sharp average of
(19)/(T⁴L⁴) are O(1)+O(ℓ/H)=O(1).
Equation (8) supplies the two required full-coefficient moments:

\[
 H^{-1}\int|U'Z|^2dt=\frac S3\ell^3+o(\ell^3),\qquad
 H^{-1}\int U'\overline{U''}|Z|^2dt=\frac{iS}4\ell^4+o(\ell^4).
\]

Consequently (13) and (19) give

\[
 \frac1H\operatorname{Re}\int_H^{2H}\frac{X\overline Y}{T^4L^4}dt
 =-\frac1{16\pi^2}\left(\frac S{12}-\frac S8\right)\ell
       +o(\ell)=\frac S{384\pi^2}\ell+o(\ell).        \tag{20}
\]

Combining (14), (18) and (20) proves (1). The sequential moment
limits were H→∞, then ε→0, then N→∞; the uniform norm tail
bounds justify their use for the full functions. Projection,
lower-order jets and moving-divisor errors are O(1)=o(log H).
The remaining error is the explicitly justified o(log H) from (8).
There is no quantitative rate or evaluated onset claim. Continuity
and the strictly negative mean give the stated negative occurrence.

The coefficient is minus one half of L381's Wronskian-square
coefficient, but that observation is only a normalization check.
It does not identify a w'-square mean or permit a sign inference for
their sum. The global mixed positivity, total margin, low indices,
exterior heights above forty, endpoint arithmetic margin and actual
common-zero upper bound all remain unresolved. ∎

### Separate critical audit — 2026-10-10

This audit uses the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-10-signed-residual-mean-audit.md`.
Conclusion (1) survives unchanged. The argument is a specialization of
Young's precisely cited moment and the already audited L381 application,
not a new moment theorem. No additional zero or phase assumption is used.

**Exact normalization and ordinary jets.** L366 (1) gives F_0=-Re(QU),
and L380 (3)–(4) makes r=e^{i phi}U real and F_0=-Ar. L368 (3)
gives G=A Re(e^{i phi}bZ) with the complete complex polynomial b.
Thus f=-r and g=Re h, whence w=-Re X and k=-Re Y, including at
zeros. In particular the sign convention differs from L380's Wcal,
but both minus signs cancel in wk. The phase is that of Q, not Qb;
the b derivatives belong in V',V''. No derivative of T^2 is suppressed
by redefining g.

To check (10) independently, write q=i omega. Expanding
(U'+qU)(V''+2qV'+(q'+q^2)V) minus
(U''+2qU'+(q'+q^2)U)(V'+qV) gives

\[
 U'V''-U''V'+q(UV''-U''V)+(q^2-q')(UV'-U'V).
\]

Here q^2-q'=-omega^2-i omega'. The UV and U'V' coefficients
cancel. This verifies every term in (10) and hence (11)–(12), with
no division by r, h, U or a real projection.

**Both moment diagonals and differentiation.** L381 section 2 and
its separate audit establish precisely (2), uniformly on the unequal
product contours, after combining both Young diagonals. Fixed twists
satisfy Young's hk restriction with scale 2H; every fixed-shape smooth
weight here satisfies the support and derivative hypotheses. The exact
I and comparison integral are holomorphic on the full product disks.
For derivative orders j,k_1 at most two, product Cauchy bounds the
derivative error by C j! k_1! H ell^{j+k_1}; the factorials are fixed
constants. The shift-sum singularity was already removed, so crossing
alpha+beta=0 inside those disks causes no problem. The leading shift
derivative is (-1)^{j+k_1} log^{j+k_1+1}(t/(2 pi))/(j+k_1+1).
Ordinary real derivatives multiply it by i^j(-i)^{k_1}. This gives
exactly c_{j,k_1}=(-i)^j i^{k_1}/(j+k_1+1), including
c_11=1/3, c_12=i/4 and c_22=1/5. No real-shift-only error is
differentiated. The inherited off-diagonal orderings, gamma poles and
far Mellin estimates are those explicitly validated in L381's audit;
raising the fixed Cauchy order does not alter their source hypotheses.

**Signed endpoints and full tails.** At fixed N, expansion of |Z_N|^2
multiplies each twist's gcd(m,n)/sqrt(mn) by (mn)^(-5/2), yielding
gcd(m,n)/(m^3 n^3). This includes every unequal pair. Absolute grouping
m=da,n=db gives S=zeta(5) zeta(3)^2/zeta(6), as in L381 (15).
For the endpoint majorant q_epsilon, the positive j=j moment has
main term at most C epsilon H ell^{2j+1} and error
O_epsilon(H ell^{2j}). Consequently Schwarz bounds the mixed
endpoint integral by C epsilon H ell^{j+k_1+1} in the normalized
limsup; |Z_N| is uniformly at most zeta(5/2). This proves signed
unsmoothing, not an invalid order comparison for a complex integrand.
Constants depending on epsilon disappear only after H grows at fixed
epsilon. The head is still fixed at that point.

Next, the uniform bound
abs(|Z|^2-|Z_N|^2) <= 2M_0 rho_0(N), together with (4), bounds the
normalized mixed-moment difference by C rho_0(N). The constant is
independent of H and N. Taking H first, epsilon second, and N last
therefore yields a full limit in (8), not a selected subsequence or
a growing-head assertion. For the original X,Y, linearity in V,V',V''
and the absolute series bounds (7) control every derivative tail.
After their respective T^2 L and T^2 L^3 divisions, norm differences
are at most C(rho_0+rho_1+rho_2)sqrt(ell); full norms are O(sqrt(ell)).
Schwarz bounds each product's averaged tail by C rho ell, also for
real parts. Thus no order-two tail or conditional interchange is hidden.

**Lower-order errors.** With the moving divisors retained, (4) gives
norms O(ell^{j+1/2}) for U^{(j)}, j<=2. The X remainder has norm
O(H^2 sqrt(ell)) before division. In (12) the largest Y remainder
norms are O(H^2 ell^{5/2}), from U''V' and omega^2 UV'. All other
terms are no larger, using omega'=O(H^(-1)). The X_0,Y_0 norms are
O(H^2 ell^{3/2}) and O(H^2 ell^{7/2}). This verifies (13) term by
term. After division, each cross product of a leading factor and a
remainder has averaged absolute value O(1); the two-remainder product
is O(ell^(-1)). The derivative bounds on b and the complete finite
M_1,M_2 are sufficient. No pointwise smallness of critical-line jets
or favorable correlation is presumed.

**Full projection and height rectangle.** Real-part multiplication
gives -4 Re X Re Y=-2 Re(X conjugate(Y)+XY); hence both terms of
(14) are indispensable. Differentiating e^{2i phi}U=B twice gives
J_1=B'-2i omega B and
J_2=B''-4i omega B'-(4omega^2+2i omega')B.
This checks the sign of the omega' term in (15). On the bottom edge
Omega equals omega, since the real polynomial in Q has no phase
derivative and the gamma arguments are conjugate. Its holomorphic
derivative therefore equals omega' there. Thus X_*,Y_* extend the
complete X,Y exactly, not only their leading jets.

For the rectangle 0<=Im tau<=1, L320 (4) with R=1 bounds the
completion by C H^{9/4} times its gamma exponential. Dividing by
the completion factors gives the zeta exponent 3/4-sigma/2. A disk
of radius 1/ell changes this power of H by a bounded factor, and
ordinary Cauchy gives (16) through order two. Portions with sigma>3/2
use absolute convergence; the desired power H^{(1-y)/2} is at least
one. The right-line disks remain in Re s>1. The paired gamma
arguments have imaginary magnitude comparable to H throughout, so
the cited sector-qualified digamma and polygamma bounds apply also
where their real parts are negative. In particular Omega=O(ell) and
Omega'=O(H^(-1)) follow from separate estimates, not differentiation
of an asymptotic error. There are no zeta or polygamma poles on this
rectangle, and the analytic logarithmic divisor has no zero there.

It follows that each vertical edge has |P|<=C H^{1-y}; its full
integral is at most C(H-1)/log H. On the entire top edge both zeta
factors and their two jets have absolutely convergent series at real
part 3/2, yielding |X_*|<=C H^2 ell and |Y_*|<=C H^2 ell^3.
The complete top integral is therefore O(H). Cauchy's theorem,
including both vertical edges and the entire top, proves (18):
the averaged same-height projection is O(1)+O(1/log H)=o(log H).
No fast carrier has entered Young's slow weight, and no residue or
endpoint is discarded.

**Coefficient and complete error ledger.** Conjugating Y_0 in (11)
gives precisely the plus i inside (19). Equation (8) then gives
Re(i U' conjugate(U'')) mean -S ell^4/4+o(ell^4), whereas the
|U'|^2 moment is S ell^3/3+o(ell^3). The exact normalization has
|b|^2/T^4=1/(16pi^2)+O(H^(-1)), omega^2/L^4=1/(4ell^2)+O(ell^(-3))
and omega/L^4=1/(2ell^3)+O(ell^(-4)), uniformly on the interval.
Schwarz bounds the absolute unweighted mixed moment by O(ell^4),
so coefficient variation costs O(1)+O(ell/H), even for the signed
mixed term. Hence the opposite-height contribution is
-S(1/12-1/8)ell/(16pi^2)=S ell/(384pi^2), up to o(ell).
The -2 in (14) supplies -S ell/(192pi^2).

All lower-order jets, coefficient freezing and the complete projection
cost O(1)+O(ell/H); the remaining error is the o(ell) furnished by
the justified moment limits. These are all o(log H). The integral is
therefore strictly negative for sufficiently large H, and continuity
gives a negative point on each such interval. This verifies the stated
existential conclusion, with no effective onset claim.

The direct mathematical inputs remain exactly those in the existing
DAG row. This audit adds no lemma, sharper estimate, positivity range
or total discriminant sign. In particular it neither computes the
independent w'-square mean nor licenses a pointwise inference from a
negative residual average. Full matching Mathlib coverage is unchecked.

## Mathlib

Full coverage of this actual-family residual asymptotic, its order-two
shifted-jet moments and signed endpoint/height-contour application is
**not checked**. Young is an external cited input. Existing local
gamma, Dirichlet and strip inputs supply analytic tools; support for
product algebra alone would not cover this theorem. Unknown Mathlib
availability is not evidence of absence.
