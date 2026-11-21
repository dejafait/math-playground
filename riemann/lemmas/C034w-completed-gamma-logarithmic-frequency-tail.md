# C034w: completed gamma vector has a logarithmic-frequency tail bound

## Hypotheses

Use C034r's actual full theta kernel \(\Phi\), Fourier transform
\(\widehat f(u)=\int_{\mathbb R}f(y)e^{-iuy}dy\), weighted space
\(E=L^2(\mathbb R,e^{-y/2}dy)\), unitary map \(Jf=e^{-y/4}f\),
translations \(T_rf(y)=f(y+r)\), and projections
\(\widehat{J\Pi_Hf}=1_{[-H,H]}\widehat{Jf}\).
Fix precisely its input
\[
 g(y)=e^{-1/(1-y^2)}1_{|y|<1},\qquad h=-g''+g/4,
 \qquad Q=\log2.
\]
For real \(X\ge2\), use the entire finite source
\[
 U_Xh=\sum_{X/2<n\le X}\mu(n)\log(X/n)n^{-1/2}
             T_{\log(n/X)}C_\Phi h.
\]
Use C034v's definitions of \(G_{1,X,M},B_{1,X,M}\) and
\(C_{1,X,M}=G_{1,X,M}-B_{1,X,M}\), including every divisor column
and the complete boundary vector. Set \(T=\lceil X^3\rceil\) and
let \(M_*=M_*(X,T)\) be exactly C034v(3)'s least minimizing integer
cap in \([T,2T)\), chosen jointly for the two centered discrepancies.
In particular C034v(4)'s uniform operator estimate applies. There is
no selected zero, RH assumption or arithmetic sign assumption.

## Conclusion

There exist constants \(K_h<\infty\) and \(X_1\ge2\), independent
of the real variable \(X\), such that for every \(X\ge X_1\),
\[
 \big\|(I-\Pi_{4\log X})C_{1,X,M_*(X,\lceil X^3\rceil)}h\big\|_E^2
 \le K_hX^{-1}.                                                   \tag{1}
\]
The onset is existential. This is localization of the fixed completed
vector, not an upper bound on its energy inside the band. It supplies
neither subpower full energy, a cumulative-energy upper, nor the
actual-Xi all-degree algebraic mixed signs.

## Proof

### 1. Imported analytic inputs and their exact specialization

The prior SPECIALIZE assessment2096, separately approved in recovery2097,
covers this target. We reuse its source and duplicate comparison.
The result is a local reproduction/specialization of standard decay
inputs and the already audited completion estimate, with no claim of
original arithmetic cancellation. The proof below is necessary because
neither source states this projected finite-cap estimate.

Import NIST DLMF [5.11.9](https://dlmf.nist.gov/5.11.E9):
\[
 |\Gamma(x+iy)|\sim\sqrt{2\pi}|y|^{x-1/2}e^{-\pi|y|/2}
 \quad(y\to\pm\infty),
\]
uniformly for \(x\) in bounded real intervals. Also import NIST DLMF
[25.2.8](https://dlmf.nist.gov/25.2.E8), for \(\Re s>0\), integral
\(N\ge1\), and \(s\ne1\):
\[
 \zeta(s)=\sum_{k=1}^Nk^{-s}+\frac{N^{1-s}}{s-1}
             -s\int_N^\infty\{x\}x^{-s-1}dx.                     \tag{2}
\]
Its recorded source is Apostol, *Introduction to Analytic Number
Theory* (1976), equation (25), p.269; the DLMF proof note cites
Theorem12.21 with \(a=1\) and \(N\) replaced by \(N-1\).
These formulas and their domains were read in assessment2096/recovery2097;
no fresh literature claim or reproof of either formula is made.

C034r section2 gives the exact multiplier
\(\widehat{e^{-y/4}\Phi(y)}(u)=\Xi(u-i/4)\). With its conventions,
\[
 \Xi(u-i/4)=\xi(3/4+iu),\qquad
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).             \tag{3}
\]
Thus (2) applies at \(s=3/4+iu\), never at the pole. Taking \(N=1\)
and bounding the absolutely convergent remainder gives, for real \(u\),
\[
 |\zeta(3/4+iu)|
 \le1+4+|3/4+iu|\int_1^\infty x^{-7/4}dx
 =5+\tfrac43|3/4+iu|\le C(1+|u|).                               \tag{4}
\]
The gamma argument is \(3/8+iu/2\). At both imaginary ends, the
imported asymptotic gives
\[
 |\Gamma(3/8+iu/2)|
 \le C|u|^{-1/8}e^{-\pi|u|/4}\quad(|u|\ge1).                   \tag{5}
\]
To include a bounded portion of \(|u|\ge1\), enlarge the constant
using continuity and absence of gamma poles on this fixed line.
The other factors in (3) satisfy
\(|\pi^{-s/2}|=\pi^{-3/8}\) and
\(|s(s-1)|\le C|u|^2\) for \(|u|\ge1\). Consequently
\[
 |\Xi(u-i/4)|\le C|u|^{23/8}e^{-\pi|u|/4}
                    \quad(|u|\ge1).                            \tag{6}
\]
This uses only the polynomial zeta bound (4), with no zero-free region
or reciprocal-zeta estimate.

### 2. The entire source tail

Since \(Jh\) is compact smooth, \(b_h=\|Jh\|_{L^1}<\infty\) and
\(|\widehat{Jh}(u)|\le b_h\). C034r's weighted translation identity
\(JT_r=e^{r/4}T_rJ\), its convolution multiplier, and the finite
source sum give
\[
 \widehat{JU_Xh}(u)=\Xi(u-i/4)\widehat{Jh}(u)P_X(u),
\]
\[
 P_X(u)=\sum_{X/2<n\le X}\mu(n)\log(X/n)n^{-1/2}
                (n/X)^{1/4}e^{iu\log(n/X)}.                      \tag{7}
\]
The phase has the positive sign because
\(\widehat{T_rf}(u)=e^{iur}\widehat f(u)\).
For every real \(u\) and \(X\ge2\), all present shifts satisfy
\(0<n/X\le1\) and \(0\le\log(X/n)\le Q\). Hence
\[
 |P_X(u)|\le Q\sum_{n\le X}n^{-1/2}\le2Q\sqrt X.                \tag{8}
\]
For the last bound, if \(N=\lfloor X\rfloor\ge1\), monotonicity
gives \(\sum_{n=1}^Nn^{-1/2}\le1+\int_1^Nt^{-1/2}dt
=2\sqrt N-1\le2\sqrt X\). No cancellation is asserted in (8).

Plancherel, (6)-(8), and both frequency ends yield, for every \(H\ge1\),
\[
 \begin{split}
 \|(I-\Pi_H)U_Xh\|_E^2
 &=\frac1{2\pi}\int_{|u|>H}
       |\Xi(u-i/4)\widehat{Jh}(u)P_X(u)|^2du\\
 &\le C_hX\int_H^\infty t^{23/4}e^{-\pi t/2}dt\\
 &\le C_hX(1+H)^{23/4}e^{-\pi H/2}.                            \tag{9}
 \end{split}
\]
For completeness, put \(a=\pi/2\), \(p=23/4\), and \(t=H+v\).
The last integral is at most
\[
 e^{-aH}(1+H)^p\int_0^\infty(1+v)^pe^{-av}dv,
\]
using \(H+v\le(1+H)(1+v)\). The remaining integral is finite and
independent of \(H,X\). All integrations are nonnegative majorants
or Plancherel integrals; there is no infinite arithmetic interchange.

Set \(H=4\log X\ge1\). The right side of (9) becomes
\[
 C_h(1+4\log X)^{23/4}X^{1-2\pi}=O_h(X^{-1}),                  \tag{10}
\]
because \((1+4\log X)^{23/4}X^{2-2\pi}\) is bounded for \(X\ge2\)
and tends to zero. Indeed on setting \(v=\log X\), the logarithm
of this factor is \((23/4)\log(1+4v)-(2\pi-2)v\to-\infty\).
This is uniform for all sufficiently large real \(X\), including
arithmetic endpoints.

### 3. Projection of the whole completion error

The choice \(T=\lceil X^3\rceil\) satisfies
\(T\ge\lceil X\rceil\). C034v(4), for the unchanged joint cap, gives
\[
 \|C_{1,X,M_*}-U_X\|_{E\to E}
 \le C(X^{1/4}T^{-1/4}+X^{5/4}T^{-3/4})
 \le C(X^{-1/2}+X^{-1})\le2CX^{-1/2}.                           \tag{11}
\]
Take \(X\) above any onset required by that cited estimate.
For each such \(X\), \(I-\Pi_{4\log X}\) is an orthogonal
projection of norm at most one, even though its cutoff varies with
\(X\). Apply it to the equality
\(C_{1,X,M_*}h=U_Xh+(C_{1,X,M_*}-U_X)h\).
The Hilbert-space inequality \(\|a+b\|^2\le2\|a\|^2+2\|b\|^2\),
(10), and (11) prove
\[
 \|(I-\Pi_{4\log X})C_{1,X,M_*}h\|_E^2
 \le2\|(I-\Pi_{4\log X})U_Xh\|_E^2
       +8C^2X^{-1}\|h\|_E^2=O_h(X^{-1}),
\]
which is (1).

Here \(C\) is always the whole \(G-B\) vector. In particular its
projected norm contains
\(\|(I-\Pi_H)G\|^2-2\Re\langle(I-\Pi_H)G,(I-\Pi_H)B\rangle
+\|(I-\Pi_H)B\|^2\). No separate bound on either term was used;
the cross term and every divisor column are retained. C034v(5)'s
signed difference of total energies is not used as a tail bound.
Nothing in this proof estimates the signed source sum within the
band, so the main mixed-positivity gap remains open.

### 4. Independent mathematical audit2100

The unchanged statement (1) passes the approved audit. This is a
verification of a standard-input specialization, not a new arithmetic
estimate. The complete proof above, C034r's theta normalization and
section2, and C034v's hypotheses, joint-cap construction and complete
section4 operator-error argument were inspected. The source coverage
of the two DLMF formulas is reused from the approved assessment2098;
neither their general proofs nor C034v's independent arithmetic inputs
are newly certified by this audit.

**Shift and analytic lines.** Directly,
\(e^{-y/4}f(y+r)=e^{r/4}(Jf)(y+r)\). Conjugating convolution
gives the kernel \(e^{-y/4}\Phi(y)\), whose transform evaluates
\(\widehat\Phi\) at \(u-i/4\). Therefore its xi argument is
\(1/2+i(u-i/4)=3/4+iu\); no sign reversal or critical-line
estimate is being used. Translation with the stated Fourier phase
gives \(e^{iur}\), so both the phase and the factor \((n/X)^{1/4}\)
in (7) are necessary. Weighted Young's inequality in C034r makes
these Fourier identities valid in \(L^2\); here \(Jh\in L^1\)
also supplies the pointwise bounded transform used in the majorant.

**Both gamma ends and exponents.** At \(s=3/4+iu\),
\(|s-1|\ge1/4\), and the remainder in (2) with \(N=1\) has
absolute integral at most \(\int_1^\infty x^{-7/4}dx=4/3\).
Thus (4) holds for every real \(u\). The gamma real part is the
fixed positive number \(3/8\), so there are no poles and the
vertical asymptotic applies as \(u\to+\infty\) and
\(u\to-\infty\). Its polynomial exponent is \(-1/8\), and
the exponential is \(e^{-\pi|u|/4}\). Combining the two polynomial
factors from \(s(s-1)\), one from (4), and \(-1/8\) from gamma
gives \(2+1-1/8=23/8\). Squaring therefore gives exactly
\(23/4\) and \(e^{-\pi|u|/2}\) in (9). Enlarging a constant
on a compact portion of the fixed gamma line is legitimate.

**Real-X uniformity and the achieved threshold.** Every summand
in (7), including at arithmetic endpoints, satisfies the unsigned
bound in (8); the floor comparison proves its constant independent
of real \(X\). Both ends of the Plancherel integral are bounded
by the same nonnegative majorant. The ratio of the resulting bound
at \(H=4\log X\) to the required \(X^{-1}\) is at most a constant
times
\[
 (1+4\log X)^{23/4}X^{2-2\pi}.
\]
It tends to zero since \(2\pi-2>0\), and is continuous and bounded
on \([2,\infty)\). Thus no subsequence of integer \(X\), omitted
frequency end, or unproved uniform decay of the bump transform is
needed.

**Cap and projected error.** The integer \(T=\lceil X^3\rceil\)
satisfies C034v's \(T\ge\lceil X\rceil\) condition. Its least
minimizer in \([T,2T)\) is selected jointly for \(j=0,1\), without
reference to \(h\) or the moving projection. C034v(4)'s constants
are uniform in those variables. Substitution gives exponents
\(1/4-3/4=-1/2\) and \(5/4-9/4=-1\) in (11); replacing
\(T\) by its lower bound is valid because both powers of \(T\)
are negative. The error is an operator norm for the entire
\(C=G-B\). For each real \(X\), orthogonal projection is a
contraction, and the squared triangle bound yields
\[
 2\|(I-\Pi_{4\log X})U_Xh\|_E^2
 +2C^2(X^{-1/2}+X^{-1})^2\|h\|_E^2=O_h(X^{-1}).
\]
This verifies (1) without substituting a difference of total energies
for an operator estimate. The existential onset includes C034v's
onset; it is not an effective cutoff. The only direct local
mathematical inputs remain C034r and C034v. Full energy inside the
band, signed primitive-sector uppers, cumulative-energy control and
the actual-Xi mixed signs remain unresolved.

## Mathlib

A full matching theorem for this fixed completed vector and moving
projection has not been checked; availability is unknown. Supporting
Fourier/Plancherel, weighted translations, gamma asymptotics and the
Euler-Maclaurin zeta identity have not been matched to exact Mathlib
theorem names. The two DLMF formulas are cited mathematical inputs,
not claimed formalized here. No machine verification is asserted.
