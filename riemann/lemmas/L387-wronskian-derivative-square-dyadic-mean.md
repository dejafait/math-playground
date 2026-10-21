# Lemma 387: logarithmic dyadic mean of the Wronskian derivative square

## Hypotheses

Use the fixed actual functions F_0,G,A of L366, with the carrier of
L368 and L380. For t>0 set T=1+t, L=log(2+t), f=F_0/A,
g=G/A and w=fg'−f'g, as in L370. All primes are ordinary real
derivatives. There is no positive regulator, RH, simplicity,
noncoincidence, phase independence, physical discriminant sign or
common-zero count assumption. Constants are uniform as H tends to
infinity for this fixed pair; the onset is not evaluated.

## Conclusion

Put S=ζ(5)ζ(3)²/ζ(6)>0. Then

\[
 \frac1H\int_H^{2H}\frac{w'(t)^2}{T^4L^4}\,dt
       =\frac{S}{960\pi^2}\log H+o(\log H).             \tag{1}
\]

This evaluates only the square term of L370. No mean or pointwise
sign of its total discriminant, total L367 margin, common-zero bound,
actual-theta positivity or zero-exclusion range follows here. The
separate critical audit below validates this specialization without
changing its coefficient or hypotheses.

## Proof

This is a **REPRODUCTION** under the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-10-wronskian-derivative-square-mean.md`.
The moment theorem is imported, not reproved: M. P. Young, *A short
proof of Levinson's theorem*, Arch. Math. **95** (2010), 539–548,
DOI 10.1007/s00013-010-0199-9, Lemmas 4–5, (4.1)–(4.5), printed
pp. 542–543, and the Cauchy paragraph after (3.4), p. 541, in the
[published PDF](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
We use its audited order-two application in L386, not a new shifted
moment theorem. The family-specific work is the exact derivative and
real projection, its normalization and coefficient. No originality
beyond the sources checked is claimed.

### 1. Imported moment with its precise scope

Let ℓ=log H, U=ζ(1/2+it), Z=ζ(5/2+it), and
\(\|a\|_H^2=H^{-1}\int_H^{2H}|a|^2dt\). L386 (4), (7), (8) give

\[
 \|U^{(j)}\|_H=O(\ell^{j+1/2}),\qquad 0\le j\le2,     \tag{2}
\]
\[
 \frac1H\int_H^{2H}U^{(j)}\overline{U^{(k)}}|Z|^2dt
  =S\frac{(-i)^j i^k}{j+k+1}\ell^{j+k+1}
         +o(\ell^{j+k+1}),\qquad 0\le j,k\le2.         \tag{3}
\]

These are sharp-interval moments of ordinary derivatives. To specify
the imported hypotheses: Young's scale is 2H, shifts are complex of
size O(1/ℓ), and each fixed rational twist h/k eventually satisfies
hk≤(2H)^(2θ) for any fixed 0<θ<1/2. The smooth weights have fixed
rescaled shape, support inside [H/2,3H] and derivatives O_a(H^(−a)),
so satisfy Young's support and derivative-scale requirements. No fast
gamma phase enters a weight. L386 (2) combines both functional-equation
diagonals into the holomorphic comparison
\(\gcd(h,k)/\sqrt{hk}\int\eta(t)\int_0^{\log(t/(2\pi))}
e^{-(\alpha+\beta)v}dv\,dt\) with error O(H). Its removable
shift-sum singularity is removed before product Cauchy differentiation.
This yields (3)'s derivative phases and order j+k error O(Hℓ^(j+k))
at each fixed head and smooth weight.

For clarity, the sharp and infinite-series qualifications of this
input are essential here. At fixed head Z_N=Σ_(n≤N)n^(−5/2−it),
all twists give
\(S_N=\sum_{m,n\le N}\gcd(m,n)/(m^3n^3)\), including unequal
pairs. Nonnegative smooth majorants of the endpoint intervals give
\(\limsup H^{-1}\ell^{-(2j+1)}\int q_\varepsilon
|U^{(j)}|^2\le C_j\varepsilon\). Schwarz therefore bounds every
complex mixed endpoint contribution by O(ε) after its appropriate
normalization; a complex integrand is never ordered. Height grows
first at fixed N,ε, then ε tends to zero, then N tends to infinity.
The tails

\[
 M_j=\sum_{n\ge1}(\log n)^j n^{-5/2}<\infty,\quad
 \rho_j(N)=\sum_{n>N}(\log n)^j n^{-5/2}\to0,\quad
 |Z^{(j)}-Z_N^{(j)}|\le\rho_j(N),\qquad j\le2,        \tag{4}
\]

use 1 at n=1 for j=0 and 0 otherwise. They follow from the locally
uniform absolute Dirichlet series, [DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1)
on Re s>1, as proved in L368. The bound
\(\big||Z|^2-|Z_N|^2\big|\le2M_0\rho_0(N)\), (2) and Schwarz
justify the last limit. Absolute grouping m=da,n=db, (a,b)=1 gives
\(S=\zeta(5)\sum_{(a,b)=1}a^{-3}b^{-3}
=\zeta(5)\zeta(3)^2/\zeta(6)\). These are the audited L386
qualifications of (3); no growing-head or shrinking-smoothing theorem
is assumed.

### 2. Exact ordinary derivative and norm errors

Use L380's exact notation

\[
 Q=Ae^{i\phi},\quad\omega=\phi',\quad
 b=(t^2/4-3/16-it/2)/\pi,\quad V=bZ,\quad
 r=e^{i\phi}U\in\mathbb R,\quad h=e^{i\phi}V.
\]

L366 and L368 give exactly f=−r, g=Re h. Since r and its
derivatives are real, define X=rh'−r'h; then w=−Re X. Product
differentiation cancels the first-jet carrier terms and yields

\[
 X=e^{2i\phi}(UV'-U'V),\qquad
 D:=X'=e^{2i\phi}\{UV''-U''V+2i\omega(UV'-U'V)\}.    \tag{5}
\]

Thus w'=−Re D. This is a derivative of the exact pointwise identity,
not of an averaged asymptotic. It retains g=G/A and all derivatives
of b; no function value is divided out, so zeros cause no exception.
Put

\[
 D_0=-be^{2i\phi}Z(U''+2i\omega U'),\qquad
 R=D-D_0=e^{2i\phi}(UV''+2i\omega UV').              \tag{6}
\]

Uniformly on [H,2H], b=O(H²), b'=O(H), b''=1/(2π), and (4)
gives V,V',V''=O(H²). The separately controlled carrier formulas of
L380 and L386 give ω=½log(t/(2π))+O(H^(−2)), ω'=O(H^(−1));
no asymptotic error is differentiated. The exact divisor T²L² is
comparable to H²ℓ². Applying (2) term by term gives

\[
 \|D_0/(T^2L^2)\|_H=O(\sqrt\ell),\qquad
 \|R/(T^2L^2)\|_H=O(\ell^{-1/2}).                    \tag{7}
\]

Indeed the two leading norms before division are O(H²ℓ^(5/2));
the two remainder norms are O(H²ℓ^(1/2)) and O(H²ℓ^(3/2)).
Consequently Schwarz and |Re a|≤|a| bound the averaged change of
either |D|²/(T⁴L⁴) or (Re D)²/(T⁴L⁴), on replacing D by D_0,
by O(1)+O(ℓ^(−1))=O(1).

The full derivative tails also have a uniform norm transfer. Set
ρ=ρ_0+ρ_1+ρ_2 and replace Z by Z_N in the complete (5), with
V_N=bZ_N. The product rules V'=b'Z+bZ' and
V''=b''Z+2b'Z'+bZ'' and (4) show

\[
 \|(D-D_N)/(T^2L^2)\|_H\le C\rho(N)\sqrt\ell.        \tag{8}
\]

All full and truncated normalized D norms are at most C√ℓ, uniformly
in N; the same holds for D_0. Thus the sharp mean of either square,
including a real square or a complex same-height square, changes by
at most Cρ(N)ℓ, using |a²−c²|≤|a−c|(|a|+|c|) and Schwarz.
No order-two right-line tail is discarded. The main calculation
below uses full functions; (8) supplies the complete-head limit if
one realizes it through finite heads.

### 3. Complete same-height projection and sharp endpoints

The exact real-square identity is

\[
 (\operatorname{Re}D)^2=\tfrac12|D|^2
                            +\tfrac12\operatorname{Re}(D^2).     \tag{9}
\]

To control the second term use the audited order-two height-rectangle
tools in L386 (15)–(18). On H≤Re τ≤2H, 0≤Im τ≤1 set

\[
 B(\tau)=\zeta(1/2-i\tau),\quad Z(\tau)=\zeta(5/2+i\tau),
 \quad\Omega(\tau)=\tfrac14[\Psi(1/4+i\tau/2)
                +\Psi(1/4-i\tau/2)-2\log\pi],
\]
\[
 J_0=B,\quad J_1=B'-2i\Omega B,\quad
 J_2=B''-4i\Omega B'-(4\Omega^2+2i\Omega')B,
 \qquad V=bZ.
\]

Here primes mean holomorphic τ derivatives and Ψ=Γ'/Γ. On the
bottom edge reflection gives J_j=e^(2iφ)U^(j) for j≤2 and
Ω=ω. Hence the holomorphic expression

\[
 D_*=J_0V''-J_2V+2i\Omega(J_0V'-J_1V)              \tag{10}
\]

equals the complete D there. As a check, substitution also gives
\(D_*=BV''-B''V+2i\Omega(B'V+BV')+2i\Omega'BV\),
the derivative of \(BV'-B'V+2i\Omega BV\). This retains the
Ω' term introduced by reflection and the complete b derivatives.

The quotient
\(P(\tau)=D_*(\tau)^2/[(1+\tau)^4\log^4(2+\tau)]\)
is holomorphic near the entire rectangle. Use the logarithm branch in
Re(2+τ)>0; both divisors are nonzero. Zeta and polygamma poles
would require Re τ=0, outside it. There are no crossed residues.
L386 (16) and its audit give, for y∈[0,1] and j≤2,

\[
 |B^{(j)}(x+iy)|\le C_j\ell^j H^{1/2-y/2},\quad
 |V^{(j)}|\le CH^2,\quad
 |\Omega|\le C\ell,\quad |\Omega'|\le C/H.          \tag{11}
\]

The B bounds use logarithmic-radius Cauchy disks on the imported
completion strip bound, including disks crossing Re s=3/2 where
absolute convergence applies. The Z disks stay in Re s>1. The paired
gamma arguments have imaginary magnitude comparable to H and remain
in admissible sectors even where their real parts are negative.
Thus the separately bounded polygamma derivative, not differentiation
of a digamma remainder, justifies Ω'. These are the qualifications
of L386's audited DLMF 5.15.1 and 5.15.8–9 inputs.

Equations (10)–(11) imply on both full vertical edges
\(|D_*|\le CH^2\ell^2 H^{1/2-y/2}\), so |P|≤CH^(1−y).
On the entire top edge B,Z and their first two derivatives are
absolutely bounded on Re s=3/2. Therefore |D_*|≤CH²ℓ² and
|P|≤C there. Cauchy's theorem, with both vertical edges retained,
now gives

\[
 \left|\frac1H\int_H^{2H}\frac{D^2}{T^4L^4}dt\right|
 \le C+\frac C H\int_0^1 H^{1-y}dy
 =O(1)+O(1/\ell)=O(1).                              \tag{12}
\]

This controls the full same-height projection on the sharp interval,
with full right-line series. It uses no phase heuristic, smoothing or
fast-phase Young weight. In particular no unestimated endpoint remains.

### 4. Moving coefficients and leading coefficient

From (6) an exact expansion on the real interval is

\[
 |D_0|^2=|b|^2|Z|^2\{ |U''|^2+4\omega^2|U'|^2
                  +4\omega\operatorname{Re}(iU'\overline{U''})\}.
                                                               \tag{13}
\]

For the cross sign, expanding (U''+2iωU') times its conjugate gives
\(2\operatorname{Re}(-2i\omega U''\overline{U'})
=4\omega\operatorname{Re}(iU'\overline{U''})\).
Uniformly on [H,2H],

\[
 \frac{|b|^2}{T^4}=\frac1{16\pi^2}+O(H^{-1}),\quad
 L=\ell+O(1),\quad\omega=\ell/2+O(1),
\]
\[
 L^{-4}=\ell^{-4}+O(\ell^{-5}),\quad
 4\omega^2/L^4=\ell^{-2}+O(\ell^{-3}),\quad
 4\omega/L^4=2\ell^{-3}+O(\ell^{-4}).                \tag{14}
\]

By (2), |Z|≤M_0 and Schwarz, the sharp absolute means of the three
jet quantities in (13) are O(ℓ⁵), O(ℓ³), O(ℓ⁴), respectively.
Consequently every replacement in (14), including the moving T and
complex polynomial b, costs O(1)+O(ℓ/H)=O(1) in the normalized
mean. No slowly varying factor is treated as exactly constant.
The three instances of (3) are

\[
 \langle |U''|^2|Z|^2\rangle_H=S\ell^5/5+o(\ell^5),\quad
 \langle |U'|^2|Z|^2\rangle_H=S\ell^3/3+o(\ell^3),
\]
\[
 \langle U'\overline{U''}|Z|^2\rangle_H
                          =iS\ell^4/4+o(\ell^4).    \tag{15}
\]

Their mixed term has real i-multiple −Sℓ⁴/4+o(ℓ⁴).
Equations (13)–(15) therefore give

\[
 \left\langle\frac{|D_0|^2}{T^4L^4}\right\rangle_H
 =\frac S{16\pi^2}(1/5+1/3-1/2)\ell+o(\ell)
 =\frac S{480\pi^2}\ell+o(\ell).                   \tag{16}
\]

The rational coefficient check is also
\(\int_0^1 x^2(1-x)^2dx=1/5+1/3-1/2=1/30\);
this is a check on the ordinary-jet phases, not an additional moment
assumption. By (7), replacing D_0 by D costs O(1). By (9), (12)
and w'=−Re D, the real-square factor is exactly one half, proving (1).

The complete error ledger is: lower jets O(1), moving coefficients
O(1)+O(ℓ/H), same-height projection O(1), and opposite-height moments
o(ℓ) with the sequential sharp/head limits in section 1. Full derivative
head transfer costs at most Cρ(N)ℓ with ρ(N)→0, section 2. Thus all
errors vanish after division by log H. Constants and the moment rate
may depend on a fixed head or smoothing shape before their limits;
no uniform effective onset is asserted.

This is local progress evaluating one missing term, using known-source
tools. L386's signed residual is a prospective comparison input, not
part of this conclusion. No total or lower-order discriminant expansion
has been derived. Global mixed positivity, physical D≤0, actual
common-zero upper counts, low indices, heights above forty and the
endpoint arithmetic margin remain unresolved. ∎

### Separate critical audit — 2026-10-10

This is the exact audit approved by the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-10-derivative-square-mean-audit.md`.
Conclusion (1) passes with its original coefficient and o(log H)
remainder. No mathematical repair, new moment theorem or additional
zero/phase hypothesis is required. The precise Young citation above and
the audited L386 application are reused, rather than reproved.

**Normalization and the complete derivative.** L366's F_0=-Re(QU),
L368's G=Re(QbZ), and L380's real r=e^{i phi}U give f=-r and
g=Re h exactly. The phase here is that of Q, not Qb. Thus
w=-Re(rh'-r'h), and differentiating this identity gives
w'=-Re(rh''-r''h). If q=i omega, the expansions

\[
 r''=e^{i\phi}(U''+2qU'+(q'+q^2)U),\qquad
 h''=e^{i\phi}(V''+2qV'+(q'+q^2)V)
\]

cancel the q'+q^2 terms in rh''-r''h. The result is precisely
D in (5), including 2i omega(UV'-U'V). This verifies why no
omega' belongs in (5), even though one appears after reflection.
The surviving highest critical-line jets are
-b e^{2i phi} Z(U''+2i omega U'), with exactly the minus sign
in (6). All polynomial derivatives remain in V',V''. No A, T or
b derivative is lost through a change of the normalized function g,
and no identity divides by a zero of either actual function.

**Imported moments and ordinary phases.** The input in L386 (2)
is an O(H) holomorphic difference on the unequal product contours
|alpha|=1/ell, |beta|=2/ell, after both functional-equation diagonals
have been combined. Its underlying L381 application retains both
off-diagonal orderings, far Mellin heights and gamma-pole exclusions.
Fixed h,k and fixed rescaled smooth weights meet Young's hypotheses
with scale 2H; no growing head or gamma-phase weight is needed here.
The shift-sum pole has already been removed. Product Cauchy through
orders j,k<=2 therefore costs only the fixed factor j!k! ell^{j+k},
yielding O(H ell^{j+k}) derivative error. The shift derivative of
the comparison integral contributes (-1)^{j+k}/(j+k+1), whereas
ordinary height derivatives contribute i^j(-i)^k. Their product is
(-i)^j i^k/(j+k+1). In particular the three required entries are
1/5, 1/3, i/4 for (2,2), (1,1), (1,2). A complex mixed moment
is retained; replacing it by a real or modulus moment would change
the coefficient.

At a fixed right-line head, each pair m,n contributes its twist
coefficient gcd(m,n)/sqrt(mn), multiplied by (mn)^(-5/2).
The complete double sum is therefore gcd(m,n)/(m^3 n^3), not
just its diagonal. Setting m=da,n=db with (a,b)=1 gives d^{-5}
a^{-3}b^{-3}. Absolute convergence and the Euler product yield
S=zeta(5)zeta(3)^2/zeta(6), as stated.

**Sharp endpoints and full derivative tails.** For a nonnegative
smooth endpoint majorant q_epsilon, the diagonal j=j moment is at
most C epsilon H ell^{2j+1}+O_epsilon(H ell^{2j}). Schwarz and
|Z_N|<=M_0 bound a mixed endpoint integral by
C epsilon H ell^{j+k+1} in normalized limsup. This estimates its
absolute value, without ordering a complex integrand. First H tends
to infinity at fixed epsilon,N, then epsilon tends to zero. The
uniform estimate abs(|Z|^2-|Z_N|^2)<=2M_0 rho_0(N), with the
positive jet norm bounds, permits N to tend to infinity last. Thus
(3) is a sharp full limit, not a subsequence or a uniform statement
for growing heads or shrinking endpoint widths.

For the complete D, write delta V=b(Z-Z_N). Its first two
derivatives are b'(Z-Z_N)+b(Z'-Z_N') and
b''(Z-Z_N)+2b'(Z'-Z_N')+b(Z''-Z_N''). Each has modulus at
most C H^2 rho, rho=rho_0+rho_1+rho_2, uniformly in N.
Inserting these into (5), the largest normalized norm contributions
are rho ell^{5/2}/ell^2 and rho ell ell^{3/2}/ell^2.
Both are O(rho sqrt(ell)); the other terms are smaller. Full and
truncated normalized D have norm O(sqrt(ell)), uniformly in N.
Schwarz consequently bounds changes of modulus, real and complex
squares by C rho ell. After division by ell this tends to zero
with N. This checks every V',V'' tail, not only the leading Z factor.

**Lower jets and moving coefficients.** The leading terms in D_0
have norms O(H^2 ell^{5/2}). The two remainder terms UV'' and
2i omega UV' have norms O(H^2 ell^{1/2}) and
O(H^2 ell^{3/2}), respectively. Dividing by the exact T^2 L^2
gives O(sqrt(ell)) and O(ell^{-1/2}) for leading and remainder
norms. Each leading/remainder square cross term has mean O(1),
and the remainder square has mean O(ell^{-1}). These bounds use
the finite M_1,M_2 and separately controlled carrier derivatives;
there is no critical-line pointwise smallness assumption.

In (13), the absolute means of the three jet terms are bounded by
C ell^5, C ell^3, C ell^4 using (2), |Z|<=M_0 and Schwarz.
Uniformly, |b|^2/T^4=1/(16 pi^2)+O(H^{-1}) and omega=ell/2+O(1).
The three coefficient errors in (14) are O(ell^{-5}),
O(ell^{-3}), O(ell^{-4}), respectively. Hence these errors cost
O(1), and the polynomial/envelope replacement costs O(ell/H).
This checks the moving normalization even for the signed cross term.

**Both real-square projections and the full rectangle.** Equation
(9) follows by expanding (D+conjugate(D))^2/4. Its same-height
term cannot be dropped by phase independence. Differentiating
e^{2i phi}U=B twice gives exactly the J_1,J_2 in section 3.
Substitution into (10) cancels the omega-square terms and gives

\[
 D_*=BV''-B''V+2i\Omega(B'V+BV')+2i\Omega'BV
     =(BV'-B'V+2i\Omega BV)' .
\]

Thus the full reflected derivative, including Omega' and all b
derivatives, agrees with D on the bottom edge. It is holomorphic
on a neighborhood of the rectangle: the possible zeta/gamma poles
require Re tau=0, and the chosen log and 1+tau divisors have no
zero there. This is an extension of an actual holomorphic formula,
not of a complex conjugate away from the real axis.

The inherited L386 strip estimate was checked at its L381/L320
source: completion exponent 9/4 minus the gamma/polynomial exponent
3/2+sigma/2 gives 3/4-sigma/2. On a radius 1/ell disk, the change
in its H power is bounded; Cauchy gives the ell^j factors through
j=2. Portions above sigma=3/2 use absolute convergence. This proves
the B-jet bounds (11), including both ends of each vertical edge.
The Z disks remain in Re s>1, so their two jets are bounded.
The paired gamma arguments remain at large imaginary height in fixed
sectors away from the negative real axis, even where a real part is
negative. Separate polygamma estimates give Omega'=O(H^{-1});
no digamma remainder is differentiated.

Consequently |D_*|<=C H^2 ell^2 H^{(1-y)/2} on each vertical
edge, and |P|<=C H^{1-y}. On the entire top, both zeta arguments
have real part 3/2, so their jets are absolutely bounded and
|P|<=C. The top integral divided by H is O(1); the sum of the
two vertical integrals divided by H is at most
C(1-H^{-1})/log H. Cauchy's theorem therefore gives (12) for
the full sharp integral. There is no residue, omitted endpoint or
uncontrolled same-height projection.

**Coefficient and verdict.** The cross term in the modulus square
is +4 omega Re(iU' conjugate(U'')); the i/4 moment makes its
contribution negative. The three leading normalized coefficients
are S/(16 pi^2) times 1/5, 1/3, -1/2. Their sum is S/(480 pi^2),
since 1/5+1/3-1/2=1/30. The exact real-square factor in (9) is
one half, giving S/(960 pi^2), unchanged.

All lower-jet, moving-coefficient and full projection errors are
O(1)+O(ell/H)=o(ell); the opposite-height remainder is o(ell)
under the justified sequential limits, and the complete head error
is at most C rho(N) ell with rho(N) tending to zero. This is the
entire logarithmic error ledger. Constants and the onset remain
unevaluated. The direct mathematical inputs are unchanged. This audit
validates an existing local reproduction, without a new theorem beyond
the sources checked, a total discriminant calculation, a pointwise
sign or any RH conclusion. Full matching Mathlib coverage is unchecked.

## Mathlib

Full matching coverage of this actual-pair derivative-square asymptotic,
its order-two shifted moments and complete projection/endpoint
application is **not checked**. Young is an external cited input;
formal product algebra alone would not supply the analytic theorem.
Unknown availability is not evidence of absence.
