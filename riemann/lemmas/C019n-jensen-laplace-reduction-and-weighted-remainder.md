# C019n — Bounded Jensen transfer, Laplace tails and the unpaid weighted remainder

## Hypotheses

Use C019m's actual real normalized Jensen value P(Y), with precisely
its positive normalization, and its reference S_d(Y). Thus d tends
to infinity through positive integers and
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad T>2\pi e,
 \quad X=\frac{T}{\sqrt{2d}},\quad q=\log X,
 \quad B=(\sqrt2-1)X,\quad h=\frac{3\pi}{q},
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad L_D=|D|=B-h.
\]
In particular
\[
 P(Y)=\frac{(-1)^d A_d(-T^2/Y^2)}{N_d^{\rm norm}(T^2/Y^2)}
\]
is exactly C019m (1), not a new rescaling. Use C019l's elementary
real sum, with its actual moving coefficients and floor:
\[
 t(Y)=\frac{Y^2}{2d},\quad \ell(Y)=\log(Y/(2\pi)),\quad
 v_n(Y)=\ell(Y)/2-\log n,
\]
\[
 a_n(Y)=n^{-1/2}\exp\{t(Y)(v_n(Y)^2-\pi^2/16)/4\},
\]
\[
 f_n(Y)=Y\ell(Y)/2-Y/2-\pi/8-Y\log n+\pi t(Y)v_n(Y)/8,
\]
\[
 N(Y)=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor,
 \qquad V(Y)=2\sum_{n\leq N(Y)}a_n(Y)\cos f_n(Y).
\]
Write V_+(Y)=V(Y+h) and E(Y)=V(Y)^2+V_+(Y)^2 on D. Every shifted
factor retains its own time and floor. All constants below are absolute
and the common onset is existential. No RH, nonvanishing, simplicity,
independence, Gaussian value law or effective onset is assumed.
The phase above was corrected in audit1389 to match C019l (8) and
C019m (7); the original omission and its effect are recorded below.

## Conclusion

Define
\[
 I_P=\int_D\frac{P(Y)P(Y+h)}{1+P(Y)^2+P(Y+h)^2}\,dY,
 \qquad F(u)=\int_D V(Y)V_+(Y)e^{-uE(Y)}\,dY\quad(u\geq0).
\]
Then the full Laplace reduction, including actual-Jensen transfer, is
\[
 I_P=\int_0^\infty e^{-u}F(u)\,du+O(B/q)
     =\int_{q^{-2}}^{2\log q}e^{-u}F(u)\,du+O(B/q).       \tag{1}
\]
The double integral is absolutely integrable. The transfer also holds
in absolute L1 over the entire parameter interval, as proved below.

There are absolute C_E,C_M>=1 such that
\[
 \int_D E\leq C_EBq,\qquad \sup_D E\leq C_M\sqrt X.       \tag{2}
\]
With kappa=1/(3*pi), a=kappa/(C_MC_E)>0, and u_0=a/sqrt(X),
\[
 F(u)\leq-\frac\kappa2Bq\quad(0\leq u\leq u_0),\qquad
 \left|\int_0^{u_0}e^{-u}F(u)\,du\right|
       \leq\frac{C_Ea}{2}\frac{Bq}{\sqrt X}=o(B).          \tag{3}
\]
Thus this certified negative parameter interval is insufficient for
the fixed length-B margin required by (N).

The exact equal-index difference contribution is
\[
 H(Y)=2\sum_{n\leq N(Y)}a_n(Y)a_n(Y+h)
                      \cos(f_n(Y)-f_n(Y+h)).
\]
At one common onset,
\[
 H(Y)\leq-\kappa q\quad(Y\in D),\qquad
 I_H:=\int_D\frac{H(Y)}{1+E(Y)}\,dY\leq-c_DB,\quad
 c_D=\frac{\kappa}{4(1+C_E)}>0.                            \tag{4}
\]
The remaining exact decomposition is
\[
 I_P=I_H+\mathcal R+O(B/q),\qquad
 \mathcal R=\int_D\frac{V(Y)V_+(Y)-H(Y)}{1+E(Y)}\,dY.     \tag{5}
\]
In particular an eventual upper bound \(\mathcal R\leq c_DB/2\) would imply
(N), with c=c_D/4 after enlarging the onset. That upper bound is NOT
proved here. The direct transplant of C019l's oscillatory bounds,
including the new weight's variation and jumps, gives no adequate
estimate for it. This is a partial reduction, not a proof or disproof
of (N), a sign-sample theorem, or an RH candidate. Audit1389 below retains
the present partial claims after correcting the phase definition; it
does not establish the sufficient remainder bound.

## Proof

### Reused sources and exact local bounds

The prior EXPLORE gate is
`drafts/literature/2026-11-17-jensen-laplace-damped-product-attempt-1386.md`.
Its inspected classical Laplace input is NIST DLMF,
[definition 1.14.17](https://dlmf.nist.gov/1.14.E17) and
[Table 1.14.4, first row](https://dlmf.nist.gov/1.14.T4): the transform
of 1 is 1/s for Re(s)>0. Here s=1+a^2+b^2 is strictly positive for
every real a,b. We import this identity; we do not infer a signed
correlation theorem from it. The named Fubini and Tonelli theorems
will only be applied after their integrability/nonnegativity conditions
are verified. Integral Cauchy--Schwarz is used with explicitly finite
square integrals.

C019m (19), its audited square (2), and C019l (9) give, uniformly on J,
\[
 \sup_J|P-S_d|=O(q^{-1}),\quad
 \sup_J|S_d+V|=O(X^{-3/4}),\quad
 \sup_J|V|=O(X^{1/4}),\quad \int_J S_d^2=O(Xq).             \tag{6}
\]
Consequently sup_J|P+V|=O(q^{-1}) and
\[
 \int_J V^2\leq2\int_J S_d^2+2|J|\sup_J|S_d+V|^2=O(Xq).
\]
Since D and D+h are both subsets of J and B is a fixed positive
multiple of X, change of variable in the shifted integral proves (2).
Increase C_E,C_M to at least 1. All functions are bounded, real and
piecewise smooth with finitely many jumps on these finite intervals.
The actual P is smooth; the reference sums need not be continuous.

### The nonlinear transfer and the full parameter integral

For real a,b put G(a,b)=ab/(1+a^2+b^2). Direct differentiation gives
\[
 |\partial_aG|=\frac{|b|\,|1-a^2+b^2|}{(1+a^2+b^2)^2}
 \leq\frac{|b|}{1+a^2+b^2}\leq\frac12,
\]
and the same bound with a,b swapped. The mean value theorem along
two coordinate segments therefore gives
\[
 |G(a,b)-G(c,e)|\leq\tfrac12(|a-c|+|b-e|).                 \tag{7}
\]
Using (6) and G(-a,-b)=G(a,b), integration over D pays the first
error in (1) by O(B/q), without dividing a mean by a varying weight.

For a stronger parameter-uniform statement set
g_u(a,b)=ab exp(-u(1+a^2+b^2)). For c_0=1+a^2+b^2,
\[
 \int_0^\infty |\partial_a g_u(a,b)|\,du
 \leq\frac{|b|}{c_0}+\frac{2a^2|b|}{c_0^2}\leq\frac32.   \tag{8}
\]
The integral of u exp(-c_0u) is c_0^(-2), by one integration by
parts; its boundary terms vanish because c_0>0. The b derivative
has the same bound. Integrate the derivatives along the same two
finite coordinate segments and apply Tonelli to their absolute values.
It follows that
\[
 \int_0^\infty|g_u(a,b)-g_u(c,e)|\,du
       \leq\tfrac32(|a-c|+|b-e|).
\]
Substituting the two actual P values and the two values -V,-V_+,
then integrating over D, proves an O(B/q) bound for the absolute
double integral of their difference. Thus the transfer holds on any
parameter subset, with a single error budget for the entire range.
No estimate at a fixed u is being integrated without uniform control.

For each Y the imported Laplace identity, with s=1+E(Y)>0, gives
\[
 \int_0^\infty |V V_+|e^{-u(1+E)}\,du
       =\frac{|V V_+|}{1+E}\leq\frac12.
\]
Tonelli on this nonnegative integrand bounds the double integral by
L_D/2. Fubini therefore applies to its signed version and proves
\[
 I_V:=\int_D G(V,V_+)\,dY=\int_0^\infty e^{-u}F(u)\,du.  \tag{9}
\]
There is no infinite arithmetic sum or unproved limiting interchange.

For delta,R>0, (2) and |V V_+|<=E/2 give the explicit tail budgets
\[
 \left|\int_0^\delta e^{-u}F(u)\,du\right|
      \leq\tfrac12 C_E\delta Bq,\qquad
 \left|\int_R^\infty e^{-u}F(u)\,du\right|
      \leq\tfrac12B e^{-R}.                               \tag{10}
\]
For the second bound integrate first at each Y, obtaining
|V V_+| exp(-R(1+E))/(1+E)<=exp(-R)/2. With delta=q^(-2)
and R=2 log q these costs are C_E B/(2q) and B/(2q^2).
Take q large enough that 0<delta<R. Equations (7)--(10) prove (1).

### The negative interval available from continuity at zero

C019l's full correlation and (6) give
\[
 F(0)=Bq\mathcal K+O(X\log q),\qquad
 \mathcal K\leq-2/(3\pi).
\]
The reference change costs O(sqrt(X)), as already paid in C019l (10).
Since X log q=o(Bq), choose one onset with F(0)<=-kappa Bq.
For u>=0, the elementary inequality 0<=1-exp(-uE)<=uE and (2)
then yield
\[
 |F(u)-F(0)|\leq u\int_D|V V_+|E
       \leq\tfrac12u C_MC_E\sqrt X\,Bq.                   \tag{11}
\]
At u<=a/sqrt(X) the last cost is at most kappa Bq/2, proving
the sign in (3). Also |F(u)|<=C_E Bq/2 for all u>=0. Integration
proves the magnitude bound in (3); more explicitly the signed integral
is at most -(kappa Bq/2)(1-exp(-u_0))<0 and at least
-(C_E Bq/2)u_0. Finally q/sqrt(X) tends to zero, so both bounds have
scale o(B). Indeed u_0<q^(-2) eventually. This negative interval is
entirely inside the already disposable small-parameter tail. It says
nothing about the sign on the remaining interval in (1).

### A genuinely negative diagonal after damping

It is necessary here to use the uniform pointwise estimates inside
C019l's proof, not only its integrated coefficient. C019l (22) and
the uniform sum-to-integral comparison preceding (24), at a fixed
Y=lambda X in D, give
\[
 H(Y)=2e^{-\pi^2t(Y)/32}\int_0^{\ell(Y)/2}
                e^{t(Y)v^2/2}\cos(hv)\,dv+O(1).           \tag{12}
\]
To track the scope: the per-term relative amplitude and phase errors
in (22) are O(h/X), whose harmonic sum costs O(hq/X); the Euler
comparison costs O(1); and the floor endpoint replacement costs
O(X^(-1/2)). These are pointwise uniform bounds, including actual
entry thresholds. No weighted off-diagonal estimate is used in (12).

In (12) set v=qz. C019l (25) and its exact scales imply, uniformly
for 1<=lambda<=sqrt(2),
\[
 H(Y)=2q\int_0^{1/2}e^{\pi^2\lambda^2z^2/8}\cos(3\pi z)\,dz
                         +O(\log q).                      \tag{13}
\]
The error follows from t q^2/2=pi^2 lambda^2/8+O(log q/q),
ell/(2q)=1/2+O(1/q), and exp(-pi^2t/32)=1+O(q^(-2)), on a
fixed compact exponential range. These are precisely the uniform
bounds established before the outer integration in C019l.

C019l (27)'s monotone-weight sign comparison applies separately for
each lambda: the cosine is nonnegative up to z=1/6 and nonpositive
thereafter up to 1/2, whereas its exponential weight is increasing.
The integral in (13) is consequently at most -1/(3*pi). Absorb the
uniform O(log q) error into q/(3*pi) to obtain H<=-kappa q.
Also |H|<=Cq, either directly from its harmonic sum or from (13).
This proves the first part of (4) with the actual two times and floors.

For the integrated bound use Cauchy--Schwarz on D with factors
(1+E)^(1/2) and (1+E)^(-1/2). Both have finite square integrals
by (2) and 1+E>=1. It gives
\[
 \int_D\frac1{1+E}\geq\frac{L_D^2}{L_D+\int_D E}.
\]
Once h<=B/2 and q>=1, this proves
\[
 I_H\leq-\frac{\kappa q L_D^2}{L_D+\int_D E}
 \leq-\frac{\kappa Bq}{4(1+C_Eq)}
 \leq-\frac{\kappa B}{4(1+C_E)}=-c_DB.                    \tag{14}
\]
The constant is positive and independent of d, though not effective.
Only the diagonal is bounded here. The elementary exact decomposition
\(I_V=I_H+\mathcal R\) and the paid transfer prove (5) and its stated
sufficient condition for (N).

### Attempt to pay the other channels, including every new jump

Let W_u(Y)=exp(-uE(Y)), and let M=N(sqrt(2)X)=O(sqrt(X)).
For an ordered pair m,n the exact entry interval remains
\[
 I_{mn}=[\max(X,r_m,r_n-h),\sqrt2X-h],\quad
 r_k/(2\pi)+r_k^2/(32d)=k^2,
\]
with empty intervals contributing zero. On that interval the amplitude
A_mn=a_m(Y)a_n(Y+h) is smooth, with sup|A_mn|+integral|A_mn'|
at most C/sqrt(mn), by C019l (14). However W_u can jump at EVERY
entry of either whole sum, not only at this pair's entry.

Between those finitely many entries, C019l (11)--(12) give
\[
 |V'(Y)|+|V_+'(Y)|\leq CqX^{1/4}.
\]
Indeed |f_n'|<=Cq and summing |a_n'|+|a_nf_n'| costs at most
Cq sum_{n<=M} n^(-1/2). At an entry of index k the corresponding
jump of V has modulus at most C/sqrt(k). Summing the jumps of both
factors costs O(X^(1/4)), even if two entries coincide. The gradient
of exp(-u(a^2+b^2)) has Euclidean norm at most sqrt(2u/e).
The mean value theorem on each smooth segment and across each jump
therefore proves the total-variation bound
\[
 \operatorname{TV}_D(W_u)
       \leq C\sqrt u\,(BqX^{1/4}+X^{1/4})
       \leq C\sqrt u\,BqX^{1/4}.                          \tag{15}
\]
For u=0 both sides are zero. No derivative of a floor or of an
asymptotic error has been taken.

For clarity the oscillatory source being reused is H. Koesters,
*On the Occurrence of the Sine Kernel in Connection with the Shifted
Moments of the Riemann zeta function*,
[arXiv:0803.1141v2, Appendix A, Lemmas A.2--A.3](https://arxiv.org/html/0803.1141v2#A),
5 September 2008. A.2 requires a real twice differentiable phase
whose second derivative has a fixed sign and magnitude at least
epsilon>0, and gives 8/sqrt(epsilon) on every subinterval. A.3 gives
sum_{m<n<=M} 1/(sqrt(mn) log(n/m))=O(M log M). These are the
Titchmarsh second-edition Lemmas 4.4 and 7.2. Their exact phase
hypotheses here were verified in C019l (16), (18)--(20): the sum
phase has second derivative >=1/(4X); for unequal indices the
difference phase has first derivative of modulus >=|log(n/m)|/2,
with the stated integrable second-derivative correction. No new
weighted source theorem is assumed.

Apply integration by parts separately between all jumps of W_u,
and retain the intervening boundary terms. Those terms are bounded
by the unweighted primitive bound times the jump sizes of A_mn W_u.
The resulting amplitude cost is at most
\[
 \frac C{\sqrt{mn}}\{1+\operatorname{TV}_D(W_u)\},
\]
since 0<=W_u<=1. Thus the sum-phase bound is multiplied by precisely
this variation factor. For unequal difference phases the direct
integration by parts with 1/(iF_-') used in C019l (20) has the same
additional jump/variation cost; its F_-'' term is still bounded by
the old estimate because W_u<=1. Summing both complete channels gives
\[
 \left|F(u)-\int_D H(Y)W_u(Y)\,dY\right|
 \leq C(X+\sqrt Xq)\{1+\operatorname{TV}_D(W_u)\}.          \tag{16}
\]
Equal indices of the sum phase are included; only the equal-index
difference phase was placed in H. This is a valid estimate, but too
weak. Integrating (16) with e^(-u), using (15) and
integral_0^infinity e^(-u) sqrt(u) du<=integral e^(-u)(1+u) du=2,
gives
\[
 |\mathcal R|\leq C X(1+BqX^{1/4})=O(X^{9/4}q).           \tag{17}
\]
All signed interchanges are legitimate: the absolute double integral
of exp(-u)|H|W_u over D times [0,infinity) is at most C Bq, and
the one for exp(-u)|V V_+|W_u is at most B/2 by (9).
In fact the elementary direct bound is better
than (17): \(|\mathcal R|\leq B/2+CBq=O(Bq)\). Neither bound is the
required signed upper bound c_D B/2, nor an o(B) absolute error.

Equations (15)--(17) show exactly what the unweighted-proof transplant
pays; a large upper bound is NOT a lower bound or a counterexample.
There may be signed cancellation not measured by total variation.
Together with (3), this stops closure by origin continuity and direct
absolute variation alone. It does not stop all Laplace methods, prove
(N) false, or assert that the actual remainder is large or positive.

All thresholds are finitely many absolute eventual conditions: the
input onsets; q sufficiently large; h<=B/2; q^2/sqrt(X) tending to
zero; the negative-correlation and pointwise-diagonal margins; and
the phase-separation conditions already uniform in C019l. Their maximum
is one integer onset independent of Y,u,m,n. No numerical experiment,
unproved distributional hypothesis or effective constant is used.

### Conceptual audit1389 — 17 November 2026

The prior SPECIALIZE assessment
`drafts/literature/2026-11-17-jensen-laplace-reduction-audit-1387.md`,
approved by review1388, covers this audit and correction. The verdict
retains (1)--(5) and the qualified bounds (15)--(17) with the corrected
phase in the Hypotheses. It is a reproduction and repair of this local
partial argument, not a new signed-remainder theorem or a claim of
progress beyond the cited sources. Full matching Mathlib coverage
remains unchecked. The inherited C019j/k inputs are used through the
audited C019l/m comparisons; they are not audited anew here.

**Essential phase correction.** The original displayed definition was
`f_n(Y)=Y*ell(Y)/2-Y/2-pi/8+pi*t(Y)*v_n(Y)/8`, omitting
`-Y*log(n)`. It was inconsistent with the asserted reuse of C019l (8)
and C019m (7). All three now use the latter definition. This is a
mathematical correction: for eta=log(n/m) the corrected same-point
derivative difference is (1+pi*Y/(8*d))*eta, whereas the misprinted
phase gives only pi*Y*eta/(8*d). Its second derivative is unchanged.
For example, with m=1,n=2 the misprinted shifted difference derivative
is O(X/d+h/X), uniformly tending to zero, so it cannot satisfy the
claimed lower bound log(2)/2. The proof's imported separation estimate
and comparison (6) therefore did not apply to the printed sum. No
claim here is made that (1)--(5) hold for that different sum; the
corrected claims concern exactly C019l/m's original V.

**Real domains and transferred bounds.** For Y in J, r=T^2/Y^2 lies
in [d,2d], and P has C019m (1)'s positive normalization. On D both Y
and Y+h belong to J. C019m (19) and C019l (9) therefore give
sup_J|P+V|=O(1/q), since X^(-3/4)=O(1/q). The square estimate
in (6) yields integral_J V^2=O(Xq), including the error square
O(X^(-1/2)). A change of variable on D+h proves integral_D E<=C_E Bq.
The two pointwise bounds give sup_D E<=C_M sqrt(X). These functions
are bounded and measurable; the finite sums are piecewise smooth,
while P is smooth because its normalization is positive. Constants
do not depend on Y or indices, and can be enlarged to be at least 1.

**Global nonlinear and parameter-L1 transfer.** In (7),
|1-a^2+b^2|<=1+a^2+b^2 and |b|/(1+a^2+b^2)<=1/2 for all real
a,b. In (8), the first term is at most 1/2 and the second at most 1,
because a^2/c_0<=1. Thus both coordinate derivatives have integrals
at most 3/2 globally. Tonelli on each finite coordinate segment
then gives the displayed L1 difference estimate, without requiring
a pointwise-in-u bound independent of the endpoints. The substitution
(a,b)=(P,P_+), (c,e)=(-V,-V_+) is legitimate, and simultaneous
sign reversal leaves both kernels unchanged. Integrating the uniform
O(1/q) error over D costs O(B/q) on the full parameter range.

For either pair of real values the absolute Laplace integral is
|ab|/(1+a^2+b^2)<=1/2. Tonelli bounds its full double integral by
L_D/2, and only then does Fubini identify the signed integral. This
checks actual P as well as V. The two tails in (10) cost respectively
C_E B/(2q) and B/(2q^2) at the stated cutoffs. No error depending
on u has been integrated with a missing uniform majorant.

**Origin interval and diagonal.** C019l (2)/(10) gives the stated
F(0) asymptotic, with error O(X log q)+O(sqrt(X))=o(Bq).
The inequality |V V_+|E<=E^2/2 and (2) give (11) for every u>=0.
At u_0=kappa/(C_M C_E sqrt(X)) this costs at most kappa Bq/2.
The absolute integral on [0,u_0] is at most C_E Bq*u_0/2=o(B),
and u_0<q^(-2) eventually. Its verified negative sign cannot pay a
fixed length-B margin on the complementary parameter interval.

For H, monotonicity of N leaves exactly n<=N(Y), including equality
at an entry. The amplitude and phase errors in C019l (22), summed
with sum 1/n=O(q), are pointwise O(hq/X). At each fixed Y the
derivative of x^(-1)g_Y(log x) is (g_Y'-g_Y)/x^2 and has absolute
integral at most C on [1,N(Y)]. The unit-interval comparison plus
the last endpoint gives the uniform O(1) error. The floor changes
log N(Y) from ell(Y)/2 by O(X^(-1/2)), at a bounded integrand.
These facts prove (12) pointwise, not just after integration in Y.

The exact identities in C019l (4)/(25) give (13), with a uniform
O(log q) error for 1<=lambda<=sqrt(2); the endpoint and outside
exponential errors are O(1) and O(1/q). On [0,1/6] replacing the
increasing exponential by its value at 1/6 increases the nonnegative
integrand. On [1/6,1/2] the same replacement increases the nonpositive
integrand. The resulting integral is at most -1/(3*pi). Absorbing
O(log q) into q/(3*pi) proves H<=-kappa q uniformly, including
all jumps. The harmonic sum also gives |H|<=Cq.

Both square integrals for Cauchy--Schwarz in (14) are finite. Its
lower bound for integral_D (1+E)^(-1) becomes an upper bound after
multiplication by -kappa q. Next L_D>=B/2 and
L_D+integral_D E<=B(1+C_E q); finally
q/(1+C_E q)>=1/(1+C_E) for q>=1. Every inequality in (14) has
the stated direction. The exact decomposition (5) follows from (9).
If its proposed remainder bound held, the uniform O(B/q) transfer
would be <=c_D B/4 at a later onset, yielding I_P<=-c_D B/4.
This conditional implication supplies no premise about the remainder.

**All jump terms and both oscillatory channels.** Partition D at the
union of every r_k and r_k-h in D, with k<=M, merging coincident
entries. On smooth pieces the corrected phase gives
|V'|+|V_+'|<=Cq X^(1/4). At an entry the relevant coordinate jump
is at most C/sqrt(k); their combined sum is O(X^(1/4)). For u>0,
the global gradient norm of exp(-u(a^2+b^2)) is bounded by
sqrt(2u/e); for u=0 it is zero. Applying this bound along smooth
pieces and the straight segment across every jump proves (15).
Coincident entries are bounded by the sum of their coordinate jumps.
Endpoint values have no effect on the integrals.

Here is an explicit check that partial integration introduces no
extra factor equal to the number of entries. On a nonempty pair
interval [a,b], let Psi(y)=integral_a^y exp(iF(r)) dr. Summing
ordinary integration by parts over its smooth pieces gives
\[
 \int_a^b A W_u e^{iF}
 =A(b-)W_u(b-)\Psi(b)
  -\sum_{\text{pieces}}\int \Psi(AW_u)'
  -\sum_{a<r<b}\Psi(r)\Delta(AW_u)(r).
\]
The initial endpoint is zero because Psi(a)=0; the internal boundary
terms are exactly the displayed jumps. Thus its absolute value is at
most sup|Psi|*(sup|AW_u|+TV(AW_u)), with
TV(AW_u)<=integral|A'|+sup|A|*TV_D(W_u).

For F(Y)=f_m(Y)+f_n(Y+h),
C019l (16) and the cited Koesters A.2 bound sup|Psi| by C sqrt(X)
on every pair interval, including stationary first derivatives and
equal indices. For F(Y)=f_m(Y)-f_n(Y+h), m!=n, apply ordinary
integration by parts with amplitude 1 using C019l (18)--(19).
On every subinterval its endpoint and derivative costs are bounded by
C times 1/|eta|, X/(d|eta|), and h/(X|eta|^2), respectively,
and the last two ratios are bounded by X/d and hM/X. Both signs of
eta are included, so sup|Psi|<=C/|eta|. Combining these bounds with
C019l (14) and the finite variation formula above gives
C sqrt(X)/sqrt(mn) or
C/(sqrt(mn)|eta|), each multiplied by 1+TV_D(W_u). Summing the
whole sum channel and both orders of the unequal difference channel
proves (16). Only the equal-index difference channel was removed.
Empty or singleton pair intervals have zero integral.

Finally sqrt(X)*q=O(X) and integral_0^infinity e^(-u)sqrt(u)du<=2
give (17). Fubini for the subtracted H term is justified by
integral_D |H|/(1+E)<=CBq; the product term already has absolute
double integral at most B/2. The better elementary O(Bq) bound is
also valid. Neither is a bound of the required sign and size on R,
and neither implies a lower bound or failure of (N).

**Common onset and verdict.** All d-dependent requirements are the
input onsets, q>=1, h<=B/2, the uniform phase conditions X/d and
hM/X small, the scale limits q^2/sqrt(X)->0 and log(q)/q->0,
the two negative margins, and the ordered tail cutoffs. Their finite
maximum is one integer onset. Bounds involving u hold for every
u>=0 before choosing it; there is no parameter-dependent onset.
The correction above resolves the sole defect found in this audit.
The partial reduction is retained; the origin/absolute-variation
closure remains stopped and the signed remainder remains unpaid.

### Qualifications and downstream use

This calculation removes the actual-Jensen transfer and parameter-tail
obligations and pays a fixed negative contribution from the exact
diagonal. The signed weighted remainder in (5) is still unresolved.
The new specialization was needed because an integrated unweighted
correlation cannot be multiplied by this endogenous damping factor.
The Laplace identity and classical oscillatory estimates are standard
imports, not discoveries; no claim of originality follows from the
prior bounded search. The separate conceptual audit1389 above retains
the corrected partial calculation; it proves no further sign estimate.

Even (N) would leave ordered disjoint sign samples, the exact reciprocal
root map, additional-root scale, separation from the existing bulk
roots, every-degree Jensen hyperbolicity and L030--L032/C032a positivity
unpaid. Stops1345/1355/559 and parked direct (A) keep their prior scopes.

## Mathlib

Full matching coverage is not checked. No identifier for a formalized
version of (1)--(5) or the weighted remainder estimate is asserted.
Elementary differentiation, finite sums, Fubini/Tonelli and integral
Cauchy--Schwarz would support parts only. The precisely cited standard
Laplace and oscillatory results and the audited local comparisons are
the inputs used here; this is an informal partial proof, not a Lean
verification or a result of numerical testing.
