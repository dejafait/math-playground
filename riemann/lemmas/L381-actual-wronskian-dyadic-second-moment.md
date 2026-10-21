# Lemma 381: the actual Wronskian dyadic second moment

## Hypotheses

Use the fixed actual pair F_0,G and positive envelope A of L366, with
ordinary real derivatives and no positive regulator. For t>0 set
T=1+t, L=log(2+t), and use L380's convention

\[
 \mathcal W(t)=\frac{F_0'(t)G(t)-F_0(t)G'(t)}{A(t)^2T^2L}.
\]

H tends to infinity. No RH, simplicity, independence, noncoincidence,
discriminant sign or common-zero count hypothesis is imposed. Constants
may depend on a fixed finite head or smoothing function where explicitly
indicated. No numerical onset is asserted.

## Conclusion

\[
 \frac1H\int_H^{2H}\mathcal W(t)^2\,dt
   =c\log H+o(\log H),\qquad
 c=\frac{\zeta(5)\zeta(3)^2}{96\pi^2\zeta(6)}>0.       \tag{1}
\]

In particular \(\mathcal W\) is not identically zero on any sufficiently
high dyadic interval. This is a second-moment nondegeneracy assertion,
not a sign-set estimate or a zero-location theorem. It gives no
Wronskian zero away from common F_0,G zeros and no count bound for those
common zeros. Global actual-theta positivity, the total L367 margin,
the low-index and endpoint gaps, and heights above forty remain unresolved.

This is a **REPRODUCTION** under the prior SPECIALIZE assessment
`drafts/literature/2026-10-08-wronskian-second-moment-calculation.md`.
Young's finite-twist moment is imported; its fixed-head specialization,
projection estimate and infinite-tail transfer are justified below.
No originality beyond the sources checked is claimed. The separate critical
audit below validates this specialization without changing its conclusion.

## Proof

### 1. Exact projection and reduction

Use L380 (3)–(5), with

\[
 U(t)=\zeta(1/2+it),\quad Z(t)=\zeta(5/2+it),\quad
 b(t)=\frac{t^2/4-3/16-it/2}{\pi},\quad d(t)=T^2L.
\]

Write Q=A exp(iφ), ω=φ'. Critical-line reflection gives, including at
zeros,

\[
 e^{2i\phi}U=\overline U,\qquad
 e^{2i\phi}U'=\overline U'-2i\omega\overline U.
\]

Consequently the exact complex expression whose real part is Wcal is

\[
 C(t)=\frac{b(\overline U Z'-\overline U'Z+2i\omega\overline UZ)
                    +b'\overline UZ}{d}
     =\frac{e^{2i\phi}}d\{bUZ'-bU'Z+b'UZ\}.           \tag{2}
\]

All primes here are real t derivatives. Both terms in

\[
 \mathcal W^2=\tfrac12|C|^2+\tfrac12\operatorname{Re}C^2             \tag{3}
\]

will be estimated; the second is not discarded by a phase heuristic.
Since |exp(2iφ)|=1,

\[
 |C|^2=\frac{|b|^2}{T^4L^2}
       |U'Z-UZ'-(b'/b)UZ|^2.                         \tag{4}
\]

The polynomial b has no real zero by L368 (3)–(4); only its division on
the real interval in (4) is used. Uniformly there,

\[
 \frac{|b|^2}{T^4}=\frac1{16\pi^2}+O(H^{-1}),\qquad
 |b'/b|=O(H^{-1}).                                  \tag{5}
\]

The factors T and L are their exact moving values, not frozen in (2).

### 2. Fixed rational-twist jet moment

We first prove the precise specialization of the imported moment that
is needed. Fix positive integers h,k and a fixed smooth real weight w
with 0≤w≤1, supported in [H/2,3H], with
\(w^{(j)}=O_j(H^{-j})\). Constants can depend on this weight's fixed
rescaled shape. Put g=gcd(h,k), h_0=h/g, k_0=k/g and ℓ=log H.
The specialization is

\[
 \int w(t)(h/k)^{-it}|U'(t)|^2dt
 =\frac g{3\sqrt{hk}}\int w(t)\log^3(t/(2\pi))dt
                      +O_{h,k,w}(H\ell^2).         \tag{6}
\]

Its order-zero counterpart is

\[
 \int w(t)(h/k)^{-it}|U(t)|^2dt
 =\frac g{\sqrt{hk}}\int w(t)\log(t/(2\pi))dt
                      +O_{h,k,w}(H).               \tag{7}
\]

Import M. P. Young, *A short proof of Levinson's theorem*,
Arch. Math. **95** (2010), 539–548, DOI 10.1007/s00013-010-0199-9,
[Lemmas 4–5, (4.1)–(4.5), pp. 542–543, and the Cauchy argument
following (3.4), p. 541](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Here its scale parameter is 2H, so the support lies in its permitted
[H/2,4H]. Its derivative scale is 2H/log(2H); our fixed-shape weights
satisfy that weaker derivative requirement for all sufficiently large H.
Fix any 0<θ<1/2; fixed hk satisfies hk≤(2H)^(2θ) eventually. The
shifts below are complex and of size O(1/ℓ), as required. No response
carrier is inserted in w.

For clarity we evaluate the two retained diagonals rather than treating
an individual singular diagonal as holomorphic. Define

\[
 I_{h,k}(\alpha,\beta)=\int w(t)(h/k)^{-it}
 \zeta(1/2+\alpha+it)\zeta(1/2+\beta-it)dt,
 \quad u=\alpha+\beta,
 \quad x=t/(2\pi).
\]

Use the product Cauchy contours |α|=1/ℓ, |β|=2/ℓ. There
1/ℓ≤|u|≤3/ℓ. Young's auxiliary function is
\(G_u(z)=e^{z^2}(1-4z^2/u^2)\). Parametrize hm=kn by
m=k_0 a,n=h_0 a. The first diagonal at a fixed t is therefore

\[
 k_0^{-1/2-\alpha}h_0^{-1/2-\beta}
 \frac1{2\pi i}\int_{(1)}\frac{G_u(z)}z
 g_{\alpha,\beta}(z,t)(h_0k_0)^{-z}
                  \zeta(1+u+2z)\,dz.               \tag{8}
\]

Here g_{α,β} is exactly Young (4.2)'s product of gamma ratios. The
exchange of sum and integral on Re z=1 is absolute: the a sum has
real exponent near three, the gamma ratios grow at most polynomially
there after multiplication by the Gaussian vertical decay, and the
fixed h_0,k_0 contribute only a bounded factor.

Move this line to Re z=−δ with δ=1/8, for sufficiently large H. The
pole at z=−u/2 is canceled by G_u; the pole at z=0 has residue
ζ(1+u). All gamma numerator real parts remain positive during this
move near bounded imaginary z; their gamma poles have real part less
than −1/2+O(1/ℓ), hence are left of the new line even at imaginary
heights near ±t. There is no pole crossing from those factors. Gaussian
decay makes the horizontal connecting integrals vanish.

On the new line the integral is
\(O_{h,k}(H^{-\delta}\ell^2)\), uniformly on the stated shift contours
and t in the support. Here are the needed bounds for that claim.
The zeta argument has real part 1−2δ+O(1/ℓ), bounded away from its
pole; Euler summation in L320 (5) bounds it by a fixed polynomial in
1+|Im z|. On |Im z|≤H^(1/8), the sector-qualified Stirling gamma-ratio
estimate in Young (4.3) gives
\(|g_{\alpha,\beta}(z,t)|≤C H^{-δ}\) times a fixed polynomial in
1+|z|; its relative error is bounded since |z|²/H tends to zero.
On the complementary part, the uniform vertical-strip Stirling bounds
bound the ratios by a fixed polynomial in H+|Im z| and H, times
exp(O(|Im z|)); the factor exp(−(Im z)²) dominates this and makes that
part smaller than every power of H. The same bounds apply to the
horizontal connectors. Finally
\(|1-4z^2/u^2|≤C\ell^2(1+|z|^2)\).
These estimates prove the claimed error without differentiating it.
They use complex gamma arguments away from the negative real axis
when their modulus is large; bounded arguments have positive real part
and are controlled on compact sets. These are the gamma qualifications
of the imported formulas, not an assumption on zeta zeros.

The second diagonal is (8) with (α,β) replaced by (−β,−α), multiplied
by Young's X_{α,β,t}. Its residue is
\(k_0^{-1/2+\beta}h_0^{-1/2+\alpha}\zeta(1-u)X_{\alpha,\beta,t}\).
Young (4.3) gives X=x^(−u)(1+O(H^(−1))) uniformly on these small
complex contours. Thus Lemma 5, including its off-diagonal error,
yields the sum of these two residues integrated against w, with error
\(O_{h,k,w}(H^{1-\delta}\ell^2)\). No off-diagonal ordering or second
functional-equation diagonal is omitted.

Since fixed-base exponentials differ from one by O_{h,k}(1/ℓ), and
\(\zeta(1+u)=1/u+O(1)\), \(\zeta(1-u)=-1/u+O(1)\), the residue sum is

\[
 \frac g{\sqrt{hk}}\frac{1-x^{-u}}u+O_{h,k}(1).
\]

Both the actual I_{h,k} and

\[
 J_{h,k}(\alpha,\beta)=\frac g{\sqrt{hk}}\int w(t)
                  \int_0^{\log x}e^{-uv}\,dv\,dt
\]

are holomorphic throughout the small product disks. The latter also
defines its value at u=0, so the singularity has been removed before
differentiation. On the product contours, I−J=O_{h,k,w}(H): the
H^(1−δ)ℓ² error is o(H). Apply the two-variable Cauchy integral formula
to this holomorphic difference using precisely these unequal radii.
Its mixed derivative at zero is O_{h,k,w}(Hℓ²), and
\(\partial_\alpha\partial_\beta\int_0^{\log x}e^{-uv}dv
=(\log x)^3/3\) at zero. This proves (6), since
\(|U'|^2=\zeta_s'(1/2+it)\zeta_s'(1/2-it)\).
The order-zero statement at zero follows from the same Cauchy formula
without derivatives, proving (7). This procedure never differentiates
separate expressions singular at α+β=0 or a merely real-shift error.

Take h=k=1 and choose a fixed-shape majorant equal to one on [H,2H].
Equations (6)–(7) and nonnegativity give

\[
 \int_H^{2H}|U'|^2dt=O(H\ell^3),\qquad
 \int_H^{2H}|U|^2dt=O(H\ell).                        \tag{9}
\]

### 3. All collisions, sharp endpoints and infinite head removal

For a fixed positive integer N put

\[
 Z_N(t)=\sum_{n\le N}n^{-5/2-it},\qquad
 S_N=\sum_{m,n\le N}\frac{\gcd(m,n)}{m^3n^3}.
\]

Expanding |Z_N|², (6) applied to each rational twist gives

\[
 \int w(t)|U'Z_N|^2dt
       =\frac{S_N}3\int w(t)\log^3(t/(2\pi))dt
                    +O_{N,w}(H\ell^2).             \tag{10}
\]

In particular every gcd collision, including unequal m,n and m=n=1,
is retained. This is not an assumption of independent phases.

To pass to the sharp interval, fix 0<ε<1/4. Choose smooth weights
w_-≤1_[H,2H]≤w_+, valued in [0,1], with w_-=1 on
[H+εH,2H−εH] and w_+=0 outside [H−εH,2H+εH].
They have derivative bounds O_{j,ε}(H^(−j)) and integrals H+O(εH).
Their supports fit section 2. The integrand |U'Z_N|² is nonnegative,
so (10) brackets its sharp integral. First H tends to infinity at fixed
N,ε. Then ε decreases to zero. On either support log(t/(2π))=ℓ+O(1).
This proves

\[
 \frac1{H\ell^3}\int_H^{2H}|U'Z_N|^2dt\longrightarrow\frac{S_N}3.
                                                               \tag{11}
\]

There is no claim that constants in (10) are uniform as ε or N varies.
Since L=ℓ+O(1) uniformly on [H,2H], (11) equivalently gives the same
limit for \((H\ell)^{-1}\int |U'Z_N|^2/L^2\). Equation (9) bounds the
error from replacing L^(-2) by ℓ^(-2) by O(1) after averaging, for fixed
N and also for full Z because |Z| is uniformly bounded.

Retain the complete absolute tails from L368 (5):

\[
 \rho_j(N)=\sum_{n>N}(\log n)^j n^{-5/2}\to0\quad(j=0,1),
 \quad \sup_t|Z-Z_N|≤\rho_0(N),
 \quad \sup_t|Z'-Z_N'|≤\rho_1(N).                    \tag{12}
\]

With \(\|f\|_H^2=H^{-1}\int_H^{2H}|f|^2dt\), (9) yields

\[
 \left\|\frac{U'(Z-Z_N)}L\right\|_H
        ≤C\rho_0(N)\sqrt\ell.                      \tag{13}
\]

The reverse triangle inequality, divided by sqrt(ℓ), therefore bounds
the difference between the square roots of the two normalized moments
by Cρ_0(N), uniformly for large H. Let H tend to infinity at each fixed
N and then N tend to infinity. Positivity and absolute convergence give

\[
 \frac1{H\ell}\int_H^{2H}\frac{|U'Z|^2}{L^2}dt
       \longrightarrow\frac S3,
 \qquad S=\sum_{m,n\ge1}\frac{\gcd(m,n)}{m^3n^3}.     \tag{14}
\]

Convergence, for example, follows from gcd(m,n)≤sqrt(mn). To evaluate
S, group m=da,n=db with gcd(a,b)=1, obtaining
\(S=\zeta(5)\sum_{(a,b)=1}a^{-3}b^{-3}\).
The same absolute grouping without the gcd weight gives
\(\zeta(3)^2=\zeta(6)\sum_{(a,b)=1}a^{-3}b^{-3}\). Thus

\[
 S=\frac{\zeta(5)\zeta(3)^2}{\zeta(6)}>0.            \tag{15}
\]

All equal reduced ratios have already entered (10); this evaluation is
not diagonal-only summation.

For completeness the smaller real-projection terms in (4) retain the
full derivative tails too. Absolute right-line bounds give |Z|≤M_0,
|Z'|≤M_1, where M_j are the convergent sums in L368 (5). Equations
(5),(9) imply

\[
 \left\|\frac{UZ'+(b'/b)UZ}L\right\|_H=O(\ell^{-1/2}),\qquad
 \left\|\frac{U'Z}L\right\|_H=O(\sqrt\ell).
\]

Their cross term is O(1) in averaged square, and their own square is
O(1/ℓ). Removing a finite head from these smaller terms costs at most
\(C(\rho_1(N)+H^{-1}\rho_0(N))/\sqrt\ell\), by (12),(9).
Consequently (4),(5),(14) give

\[
 \frac1H\int_H^{2H}|C|^2dt
         =\frac S{48\pi^2}\ell+o(\ell).             \tag{16}
\]

The O(H^(-1)) coefficient variation in (5) costs O(ℓ/H), below this
scale. Infinite tails were controlled in norm before their removal;
pointwise series convergence was not used as a moment theorem.

### 4. Complete same-height projection term

No Fourier carrier will be treated as a permitted Young weight. Instead
extend (2)'s first expression holomorphically in a height variable τ:

\[
 B(\tau)=\zeta(1/2-i\tau),\quad Z(\tau)=\zeta(5/2+i\tau),
 \quad \Omega(\tau)=\tfrac14\{
 \Psi(1/4+i\tau/2)+\Psi(1/4-i\tau/2)-2\log\pi\},
\]
\[
 C_*(\tau)=\frac{
 b(\tau)[B Z'-B' Z+2i\Omega BZ]+b'(\tau)BZ}
                   {(1+\tau)^2\log(2+\tau)}.        \tag{17}
\]

Primes now mean holomorphic τ derivatives. On the real line B=bar U,
B'=bar U', Ω=ω by L380's exact digamma formula, hence C_*=C.
The logarithm uses its branch on Re(2+τ)>0. For sufficiently large H,
every factor is holomorphic on a neighborhood of the closed rectangle
H≤Re τ≤2H, 0≤Im τ≤1: the zeta pole would require Re τ=0, the
polygamma poles also have Re τ=0, and the denominator is nonzero here.
No conjugated function is silently called holomorphic.

We record the complete edge bounds. In the fixed real strip
1/2−r≤σ≤3/2, with r=1/ℓ and |v| comparable to H, L320 (4) at R=1,
divided by the completed polynomial and the sector-qualified gamma
modulus, gives

\[
 |\zeta(\sigma+iv)|≤C H^{3/4-\sigma/2}.             \tag{18}
\]

Indeed the completion bound has polynomial exponent 9/4; the divided
factors have exponent 2+(σ/2−1/2)=3/2+σ/2, and their exponential
moduli cancel. The constants are uniform for these σ in a fixed compact
positive strip. Above σ=3/2 the absolute Dirichlet bound applies instead.
For τ=x+iy on either vertical edge, the B argument has σ=1/2+y.
On its complex derivative circle of radius r, (18), with the absolute
bound if σ>3/2, implies |B|≤C H^(1/2−y/2), and Cauchy's estimate gives

\[
 |B'(\tau)|/\ell≤C H^{1/2-y/2}\quad(0≤y≤1).         \tag{19}
\]

The factor H^(r/2) from those disks is bounded; no fixed-width disk
loses a power of H. The corresponding Z arguments and their derivative
disks have real part at least 3/2−r>1, so |Z|+|Z'|≤C by the complete
absolute series. The exact paired digamma representation and its
sector-qualified expansion from L380 give |Ω|≤Cℓ on the rectangle.
Both digamma arguments have large imaginary part in a fixed sector
away from the negative real axis, even when one real part is negative.
Finally |b|=O(H²), |b'|=O(H), and
\(|(1+\tau)^2\log(2+\tau)|\asymp H^2\ell\).
Thus

\[
 |C_*(x+iy)|≤C H^{1/2-y/2}
\]

on both vertical edges. On the top edge y=1 both B and Z are on
Re s=3/2, and their first jets are absolutely bounded there;
(17) gives |C_*|≤C on that entire edge. These statements retain the
full right-line functions, not truncated Euler heads.

Cauchy's integral theorem for C_*² moves the bottom edge to the top.
The top integral is O(H); the two vertical integrals each have absolute
bound \(C\int_0^1 H^{1-y}dy=O(H)\) (in fact O(H/ℓ)). Therefore

\[
 \left|\frac1H\int_H^{2H}C(t)^2dt\right|=O(1)=o(\ell).             \tag{20}
\]

There are no omitted residues or unestimated contour endpoints.
The shift moves the critical negative-height line rightward and the
positive-height line leftward by exactly one, leaving both absolutely
convergent; it is not a shift of size two in Young's moment theorem.

Combining (3),(16),(20) proves (1) with (15). Continuity and c>0 imply
that Wcal is nonzero somewhere on each sufficiently high dyadic
interval. This does not imply a zero or a sign change there, nor rule
out common-zero resets. No first-Laguerre or RH-equivalent positivity
was assumed or obtained. ∎

### Separate critical audit, 2026-10-08

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-08-wronskian-second-moment-audit.md`.
The conclusion (1) survives. No extra zero hypothesis or mathematical
repair is required. The following checks concern the family-specific
application of Young's cited result, not a reproof of that theorem.

**Normalization and projection.** L366 (1) gives F_0=−Re(QU), and
critical-line reflection makes QU real. L368 (3) gives G=Re(QbZ),
with |Q|=A and exactly the b in (2). Hence F_0=−Ar and G=A Re h,
where r=e^{iφ}U is real and h=e^{iφ}bZ. The Wronskian divided by A²
is Re(rh'−r'h); all A' and common iφ' terms cancel. Differentiating
e^{2iφ}U=bar U gives the plus 2iω term when solving for e^{2iφ}U'.
These operations hold at U=0 and at common zeros. Factoring the second
expression in (2) verifies the minus b'/b term in (4), and squaring a
real part gives exactly (3), with its factor 1/2 on both summands.
The phase in Ω is that of Q, not Qb: the latter's b'/b correction is
already explicit. The positive real polynomial p in Q contributes no
phase derivative, so the paired digamma expression (17) is exact.

**Imported moment and uniformity.** Young's (2.1)–(2.3), (3.4),
Lemmas 4–5 and full Lemma 5 proof, printed pp. 540–543, were checked
directly in the cited primary PDF. Scale 2H accommodates every weight
used here. The derivative constants may depend on the fixed smoothing
shape, and fixed twists satisfy the length restriction eventually.
The two diagonals in (4.5) have respectively exponents
(m,n)=(−1/2−α,−1/2−β) and (−1/2+β,−1/2+α);
thus their parametrization and prefactors in section 2 are correct.

On the unequal-radius product contours, |u|≥1/ell. The auxiliary
polynomial and all its fixed-order derivatives cost at most a power
of ell. Such losses are harmless in the arbitrarily decaying
integration-by-parts remainder of Lemma 5. For precision, the
integration bound includes the interval length O(H); retaining that
factor and these logarithmic losses still gives arbitrary power
saving by increasing the number of integrations. Both orderings of
hm and kn have the same separation bound. The off-diagonal proof
uses decay in mn/T for large mn, the direction supplied by (4.1).
No small-mn decay or bound without the integration-length factor
is needed here.

There are also no hidden gamma singularities in the diagonal move.
For −1/8≤Re z≤1 the real parts of the numerator gamma arguments
are at least 3/16−O(1/ell)>0; their poles in z have real part
−1/2−Re α−2j or −1/2−Re β−2j. On Re z=−1/8, Euler summation
bounds ζ(1+u+2z) by C(1+|Im z|), since its real part stays in a
compact subset of (0,1) separated from 1. For |Im z|≤H^{1/8},
the ratio expansion has relative error O((1+|z|²)/H)=o(1).
Its main modulus is O(H^{-1/8}).

For the remaining Mellin heights v=Im z, vertical-strip Stirling,
with compact bounds when either numerator height is small, gives
an upper bound H^K(1+|v|)^K exp(C|v|) for some fixed K,C.
One can see why no uncontrolled exp(cH) remains: up to the small
shift imaginary parts, the gamma exponential quotient is
exp{πt/2−π(|t+v|+|v−t|)/4}≤1. The small shifts change this
by a bounded factor, by the triangle inequality. The polynomial
bound remains valid also near v=±t. Multiplication by e^{-v²}
makes the integral over |v|>H^{1/8} smaller than every power of H,
uniformly on the shift contours. Thus the integrated Mellin remainder
is indeed O(H^{7/8}ell²). Replacing X by x^{-u} costs only O(ell)
after integration, since |ζ(1−u)|=O(ell). Both are o(H).

The sum of residues differs from
(g/sqrt(hk))(1−x^{-u})/u by O_{h,k}(1), uniformly there:
each fixed-base factor is 1+O_{h,k}(1/ell), |x^{-u}|=O(1),
and both pole terms have modulus O(ell). The exact I and the
integral expression J are holomorphic on the full product disks,
even where u=0. Double Cauchy applied to I−J bounds its mixed
derivative by O(H ell²); no derivative of a nonholomorphic error
is invoked. The leading mixed derivative of J is (log x)^3/3.
Since U'=iζ_s' and bar U'=−i conjugate(ζ_s'), the mixed shift
derivative is precisely |U'|², with no minus sign. This verifies
(6) and (7), including the second functional-equation contribution.

**Sharp endpoints and full tails.** The bracketing is applied to
|U'Z_N|²≥0 after all fixed-head twists have been summed. It is not
applied to a complex twist individually. At fixed N and smoothing
width epsilon the normalized main term is S_N/3 times the rescaled
weight integral; the error is O_{N,epsilon}(1/ell). First H tends
to infinity, then epsilon tends to zero. Only after this does N grow.
For the final passage, put a_H=||U'Z/L||_H/sqrt(ell) and define
a_{H,N} with Z_N. Equation (9) gives
|a_H−a_{H,N}|≤C rho_0(N), with C independent of N,H. Together
with a_{H,N}→sqrt(S_N/3) and S_N→S, this squeezes both liminf
and limsup of a_H to sqrt(S/3). It proves (14), not merely a
subsequence limit. The derivative tail rho_1 handles the smaller
UZ' term. Its cross term costs O(1), its square O(1/ell), and
coefficient variation costs O(ell/H). All are o(ell).
The gcd grouping is absolute and gives exactly (15); discarding
unequal m,n would give the wrong constant.

**Height rectangle and endpoint jets.** L320's complete proof of
(4) was checked with R=1. It gives exponent 9/4 for the completion
on −1/2≤σ≤3/2, with the gamma exponential retained. Dividing
by the completion factors yields (18) on the positive substrip in
use. On the radius 1/ell disk centered at x+iy, B's real part in
its zeta argument is at least 1/2+y−1/ell. The resulting bound
is C H^{1/2−y/2} H^{1/(2ell)}; the last factor is bounded.
Cauchy therefore supplies (19). Portions of a disk above σ=3/2
use the absolute series; because 0≤y≤1, the desired exponent
is nonnegative and also bounds those portions. All Z disks stay
strictly to the right of 1. No derivative circle crosses a zeta pole.

Both digamma arguments on the rectangle have imaginary part of
magnitude at least H/2, and stay in a fixed sector away from the
negative real axis, including where their real part is negative.
Consequently Ω=O(ell). Poles of these factors or either zeta
factor would require Re τ=0, outside the rectangle. The chosen
logarithm is holomorphic and nonzero there. Thus C_* is a genuine
holomorphic extension of the complete C. The two vertical squared
integrals are bounded by C(H−1)/log H; the top integral is O(H).
After division by H the projection bound is O(1), as asserted,
with no unestimated endpoints or residues.

Finally the modulus coefficient is S/(48π²), and the real-part
square identity halves it to S/(96π²). This validates the positive
coefficient and every required o(log H) obligation. The result is
quantitative nondegeneracy only; it does not establish either sign,
a sign change, a noncommon Wronskian zero, or control of common-zero
resets. No RH criterion, actual-theta sign range or exclusion height
is advanced by this audit. Matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this actual-pair shifted-jet moment,
projection-contour estimate and infinite-tail specialization is **not
checked**. Young's analytic moment is an external named input, not a
Mathlib theorem claim. Supporting gamma, Dirichlet and completion
coverage is inherited through the cited local inputs; formal product
identities alone would not supply (6), (14) or (20). Unknown coverage
is not evidence of absence.
