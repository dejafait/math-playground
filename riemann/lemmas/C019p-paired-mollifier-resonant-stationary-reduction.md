# C019p — Paired mollifier: resonances, stationary terms and transfer gap

## Hypotheses

Use C019m's actual real normalized Jensen value P, with its positive
normalization, and exactly its scales
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,
\]
where d tends through positive integers and T>2*pi*e. Put
J=[X,sqrt(2)X], D=[X,sqrt(2)X-h]. Use C019l's elementary reference
\[
 \begin{split}
 t(Y)&=Y^2/(2d),&\ell(Y)&=\log(Y/(2\pi)),\\
 v_n(Y)&=\ell(Y)/2-\log n,& c_0&=\pi/8,\\
 a_n(Y)&=n^{-1/2}\exp\{t(Y)(v_n(Y)^2-\pi^2/16)/4\},\\
 \vartheta(Y)&=Y\ell(Y)/2-Y/2-\pi/8,\\
 f_n(Y)&=\vartheta(Y)-Y\log n+c_0t(Y)v_n(Y),\\
 V(Y)&=2\sum_{n\leq N_d(Y)}a_n(Y)\cos f_n(Y),\\
 N_d(Y)&=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor.
 \end{split}                                                    \tag{1}
\]
Each shifted value uses its own time and floor. The auxiliary a_n,
v_n,f_n are defined for every positive real argument, including before
an index enters V. Set N_*=N_d(sqrt(2)X).

Fix, without optimization,
\[
 L=\lfloor X^{1/1000}\rfloor,\quad K=L^2,\quad
 \omega_L(n)=\frac{\log(L/n)}{\log L}\quad(1\leq n\leq L),
\]
and take the real coefficients alpha(n) of the Euler-product branch
\[
 \zeta(s)^{-1/2}=\sum_{n\geq1}\alpha(n)n^{-s}
 \quad(\operatorname{Re}s>1),
\]
positive on real s>1. Eventually L>=2. Only these coefficients in
finite polynomials are used; no critical-line reciprocal is taken.
Define
\[
 \mathcal M(Y)=\sum_{n\leq L}\alpha(n)\omega_L(n)n^{-1/2-iY},
 \qquad W(Y)=|\mathcal M(Y)\mathcal M(Y+h)|^2,
\]
\[
 b_k=\sum_{\substack{uv=k\\u,v\leq L}}
    \alpha(u)\alpha(v)\omega_L(u)\omega_L(v)v^{-ih},\qquad
 w_{kl}=\frac{b_k\overline{b_l}}{\sqrt{kl}}.                    \tag{2}
\]
All assertions below are for one sufficiently large absolute integer
onset. No RH, simplicity, nonvanishing or probabilistic hypothesis is
made. This is the partial outcome of the prior EXPLORE assessment1394,
separately approved in1395. Independent conceptual audit1401 below
retains this reduction; its conclusions alone are not a completed sign
test. The later sign and transfer argument is in C019r.

## Conclusion

The finite weight satisfies
\[
 |b_k|\leq1,\qquad
 \int_D W(Y)\,dY
 =|D|\sum_{k\leq K}\frac{|b_k|^2}{k}+O(K\log K)=O(Xq).        \tag{3}
\]
Here and below implicit constants are absolute, with the exponent
1/1000 fixed as stated.

For 1<=m,n<=N_*, retain the actual domain
\[
 I_{mn}=\{Y\in D:m\leq N_d(Y),\ n\leq N_d(Y+h)\}.
                                                               \tag{4}
\]
Write U_d(Y)=Y/(2*pi)+Y^2/(32d), and let rho_j>0 solve
U_d(rho_j)=j^2. Then I_mn is
[max(X,rho_m,rho_n-h),sqrt(2)X-h], or empty. Empty and singleton
intervals contribute zero in every expression below.

Define the real resonant expression
\[
 \mathcal R_d=2\operatorname{Re}
 \sum_{\substack{m,n\leq N_*;\ k,l\leq K\\nl=mk}}
 w_{kl}\int_{I_{mn}}a_m(Y)a_n(Y)
   e^{i\{c_0t(Y)\log(n/m)-hv_n(Y)\}}\,dY.                    \tag{5}
\]
For the other channel put
\[
 H=X^{3/5},\quad x=x_{mnkl}=2\pi mnk/l,\quad
 \psi_{mn}(Y)=c_0t(Y)(v_m(Y)+v_n(Y))+hv_n(Y).
\]
If I_mn=[a,b], let
\[
 \mathcal F_{mn}(x)=
 \int_{\max(a-x,-H)}^{\min(b-x,H)}e^{iz^2/(2x)}\,dz,           \tag{6}
\]
interpreted as zero when the upper endpoint is no larger than the
lower endpoint or I_mn is empty. Define
\[
 \mathcal S_d=2\operatorname{Re}
 \sum_{m,n\leq N_*;\ k,l\leq K}
 w_{kl}\,a_m(x)a_n(x)
 e^{i\{\psi_{mn}(x)-x-\pi/4\}}\mathcal F_{mn}(x).             \tag{7}
\]
A term with an empty intersection in (6) is defined to be zero
without evaluating its amplitude at x. All nonempty terms have
x in [X-H,sqrt(2)X-h+H], hence in [X/2,2X] eventually.
This is a truncated Fresnel integral, not its full-line replacement.

Both channels together satisfy the absolute-error formula
\[
 \int_D V(Y)V(Y+h)W(Y)\,dY
    =\mathcal R_d+\mathcal S_d+O(X^{451/500}),\qquad
 X^{451/500}=o(B).                                           \tag{8}
\]
In particular all nonresonant difference terms and all omitted
nonstationary/Taylor errors have been paid below scale B. No sign of
R_d+S_d is claimed, and neither main expression has been discarded.

Set
\[
 Q_j=\int_D V(Y+j)^2W(Y)\,dY\quad(j=0,h).
\]
The actual-Jensen comparison gives only the following payment here:
\[
 \left|\int_D\{P(Y)P(Y+h)-V(Y)V(Y+h)\}W(Y)\,dY\right|
 \leq C\sqrt{X/q}(\sqrt{Q_0}+\sqrt{Q_h})+CX/q.                \tag{9}
\]
Thus Q_0+Q_h=o(Xq) would suffice for an o(B) transfer. This bound
on Q is unproved. Likewise a fixed negative B-scale upper bound for
(5)+(7) is unproved. The first (M2) inequality, squared-mass bound,
quantitative root selection, every-degree positivity and RH remain open.

## Proof

### Standard inputs and why a specialization is necessary

Import H. Kösters, *On the Occurrence of the Sine Kernel in Connection
with the Shifted Moments of the Riemann zeta function*, 5 September2008,
[arXiv:0803.1141v2, Appendix A](https://arxiv.org/html/0803.1141v2#A):

- Lemma A.1, also Titchmarsh, *The Theory of the Riemann Zeta-function*,
  second edition, Lemma4.2: a real differentiable phase F with monotone
  F' and either F'>=epsilon>0 or F'<=-epsilon throughout an interval
  satisfies |integral exp(iF)|<=4/epsilon.
- Lemma A.3, also Titchmarsh Lemma7.2:
  sum_{1<=u<v<=R} 1/(sqrt(uv)log(v/u))=O(R log R).

Their exact statements and relevant proof cases were already inspected
in reviews1377/1395. They are imported, not reproved. In particular
A.3 is used only after reindexing to ordinary positive integers; it is
not asserted for arbitrary unseparated rational frequencies.

C019l supplies N_*=O(sqrt X), d comparable to X^2q^2,
t=O(q^(-2)), its phase derivatives, amplitude variation, and shift
estimates. C019m supplies the actual-P uniform comparison and the
full-band square estimate. Neither supplies this weighted theorem.
The explicit finite coefficient bookkeeping, changed resonance
condition and stationary-entry geometry are the needed difference.
The elementary divisor estimate below is included only to justify
the chosen power-saving exponent after reindexing, not as a new
number-theoretic input. No unread Selberg paired formula is used.

### Finite coefficient bound and weight mass

For a prime p, write
(1-z)^(1/2)=1-sum_{r>=1}c_r z^r. The binomial expansion gives
c_1=1/2, c_2=1/8, and
c_{r+1}/c_r=(r-1/2)/(r+1) for r>=1. Thus c_r is positive
and decreasing. The Euler product gives multiplicative alpha, with
alpha(p^r)=-c_r for r>=1. The prime-power generating series for
the Dirichlet convolution |alpha|*|alpha| is
\[
 (2-\sqrt{1-z})^2=5-z-4\sqrt{1-z}.
\]
Its constant coefficient is1, its coefficient at z is1, and its
coefficient at z^r for r>=2 is4c_r<=1/2. Multiplicativity therefore
gives (|alpha|*|alpha|)(k)<=1 for every k. Since the taper lies in
[0,1] and |v^(-ih)|=1, (2) implies |b_k|<=1. This argument is
coefficient algebra inside the absolutely convergent Euler product
on Re(s)>1; it requires no continuation of a reciprocal.

Multiplying the two finite mollifiers gives exactly
\[
 \mathcal M(Y)\mathcal M(Y+h)
   =\sum_{k\leq K}b_k k^{-1/2-iY},\qquad
 W(Y)=\sum_{k,l\leq K}w_{kl}e^{iY\log(l/k)}.                 \tag{10}
\]
For k!=l the integral of the exponential over D is at most
2/|log(l/k)|. A.3 and |b_k|<=1 bound the sum of these terms by
O(K log K), while the equal-index terms give exactly (3)'s diagonal.
The harmonic sum is at most1+log K. Since K<=X^(1/500),
|D|=O(X) and log K=O(q), (3) follows. Nonnegativity of W is
preserved by its original definition, not inferred termwise.

For later absolute summations we also have
\[
 \sum_{m,n\leq N_*;\ k,l\leq K}
 \frac{|b_kb_l|}{\sqrt{mnkl}}
 \leq16N_*K=O(X^{251/500}).                                 \tag{11}
\]
This uses sum_{j<=A}j^(-1/2)<=2sqrt(A), twice for each pair.

### Exact entries and the shift replacement

The strict monotonicity U_d'(Y)=1/(2*pi)+Y/(16d)>0 proves (4),
including both actual entries and every floor equality. On J, all
auxiliary a_n with n<=N_* satisfy
\[
 |a_n|\leq C/\sqrt n,\quad |a_n'|\leq C/(X\sqrt n),\quad
 a_n(Y+h)=a_n(Y)(1+O(h/X)),
\]
\[
 f_n(Y+h)=f_n(Y)+hv_n(Y)+O(h/X)\quad(Y\in D).                \tag{12}
\]
These are C019l (12),(22); they do not require that n have entered
at Y. Thus the later n-entry at Y+h presents no exception.

Because W is real, the finite real-product identity is
\[
 \int_D VV_hW=2\operatorname{Re}
 \sum_{m,n,k,l} w_{kl}\int_{I_{mn}}a_m(Y)a_n(Y+h)
 \left[e^{i(f_m(Y)-f_n(Y+h)+Y\log(l/k))}
       +e^{i(f_m(Y)+f_n(Y+h)+Y\log(l/k))}\right]dY.           \tag{13}
\]
All four index ranges here and below are those in (11).
Replace only the shifted amplitude and phase by (12), keeping I_mn
unchanged. For each term, the pointwise error is at most
C*h/(X*sqrt(mn)), before multiplication by |w_kl|. Integrating
over length O(X) and using (11) pays total
\[
 O(hN_*K).                                                   \tag{14}
\]
There is no floor differentiation or replacement of a cutoff by a
real number. The two phases after this paid replacement are
\[
 F_-(Y)=Y\log(nl/(mk))+c_0t(Y)\log(n/m)-hv_n(Y),              \tag{15}
\]
\[
 F_+(Y)=Y\log(Y/x)-Y-\pi/4+\psi_{mn}(Y),
 \qquad x=2\pi mnk/l.                                      \tag{16}
\]
Both multiply the same smooth amplitude a_m(Y)a_n(Y).

### Difference-channel nonresonances

Put R=N_*K and eta=log(nl/(mk)). If nl!=mk, the two distinct
positive integers are at most R, so |eta|>=1/R. The slow part
g(Y)=c_0t(Y)log(n/m)-hv_n(Y) of (15) satisfies exactly
\[
 g'(Y)=c_0Y\log(n/m)/d-h/(2Y),\qquad
 g''(Y)=c_0\log(n/m)/d+h/(2Y^2).
\]
As |log(n/m)|<=Cq, these are O(1/(Xq)) and O(1/(X^2q)),
uniformly. Since R/(Xq) tends to zero, eventually
|F_-'|>=|eta|/2 on all of I_mn. For A=a_ma_n,
\[
 \sup_{I_{mn}}|A|+\int_{I_{mn}}|A'|\leq C/\sqrt{mn},\qquad
 \int_{I_{mn}}|F_-''|\leq C/(Xq).
\]
Integration by parts against 1/(iF_-') gives
\[
 \left|\int_{I_{mn}}Ae^{iF_-}\right|
 \leq\frac{C}{\sqrt{mn}}
       \left(\frac1{|\eta|}+\frac1{Xq|\eta|^2}\right)
 \leq\frac{C}{\sqrt{mn}|\eta|}.                             \tag{17}
\]
This includes both endpoint terms, the A' integral and the F_-''
integral. Monotonicity of F_-' is not assumed.

Reindex by u=mk,v=nl. For fixed u there are at most tau(u)
choices of (m,k), and similarly for v; |b_k|<=1. Hence the sum
of (17), multiplied by |w_kl|, is at most
\[
 C\sum_{\substack{u,v\leq R\\u\ne v}}
       \frac{\tau(u)\tau(v)}{\sqrt{uv}|\log(v/u)|}.
\]
For completeness, tau(u)<=C*u^(1/4): for every prime p>=16 and
integer a>=0, a+1<=2^a<=p^(a/4); for each of the finitely many
primes p<16, sup_{a>=0}(a+1)p^(-a/4) is finite. Multiplying
these inequalities over the prime factorization gives one absolute C.
Therefore tau(u)tau(v)<=C*R^(1/2). The cited A.3 now applies
to the integer pair u,v, giving total
\[
 O(R^{3/2}\log R)=O(X^{753/1000}q)=o(X).                     \tag{18}
\]
All remaining difference terms have nl=mk, and (15) gives precisely
(5). In particular m=n alone would be an incorrect resonance set.

### Sum-channel stationary and entry-boundary terms

Write phi_x(Y)=Y log(Y/x)-Y-pi/4 and
A_+(Y)=a_m(Y)a_n(Y)exp(i*psi_mn(Y)). On J,
\[
 \phi_x'(Y)=\log(Y/x),\quad \phi_x''(Y)=1/Y,\quad
 \sup|A_+|+\int_J|A_+'|\leq C/\sqrt{mn}.                    \tag{19}
\]
Indeed psi_mn'=O(1/(Xq)) follows by differentiating its displayed
definition, using t'=Y/d and v_n'=1/(2Y). The amplitude bounds
and their derivative bounds also hold on [X/2,2X], with different
absolute constants: the explicit (1) still has |v_n|<=Cq,
t=O(q^(-2)), and d comparable to X^2q^2 there. This extension
concerns smooth auxiliary functions only, not an extended formula
for V or P.

Outside [x-H,x+H], I_mn has at most two components. On each,
phi_x' is monotone, of one fixed sign, and has modulus at least
cH/X. This last estimate is uniform even if x is far from J:
for x in [X/2,2X] it follows by integrating 1/u between x and Y;
for x outside that range it follows from a positive constant
separation (with sqrt(2)X the upper end of J). Since H/X tends
to zero, the same lower bound applies in both cases.

The imported A.1 gives a bound C*X/H for the unweighted integral
on every subinterval of either component. If its primitive starting
at a component endpoint is G, integrating A_+ against G gives
the bound (C*X/H)(sup|A_+|+integral|A_+'|). Thus the whole
outside part costs at most
\[
 C X/(H\sqrt{mn}).                                         \tag{20}
\]
This explicitly pays variation of the complex amplitude. It does
not apply an unweighted theorem directly to that amplitude.

For the inside part, nonempty intersection implies
x in [X-H,sqrt(2)X-h+H] subset [X/2,2X]. Uniform Taylor
expansion about x, with phi_x'''(Y)=-1/Y^2, gives for |z|<=H
on the relevant interval
\[
 \phi_x(x+z)=-x-\pi/4+z^2/(2x)+O(|z|^3/X^2).
\]
The connecting segment between x and x+z lies in [X/2,2X]
at one common onset. Its amplitude change is bounded by
\[
 |A_+(x+z)-A_+(x)|\leq C|z|/(X\sqrt{mn}).
\]
Using |exp(iu)-exp(iv)|<=|u-v| for real u,v and integrating
these errors over the actual intersection gives
\[
 \int_{I_{mn}\cap[x-H,x+H]}A_+(Y)e^{i\phi_x(Y)}dY
 =a_m(x)a_n(x)e^{i\{\psi_{mn}(x)-x-\pi/4\}}
        \mathcal F_{mn}(x)
 +O\left(\frac1{\sqrt{mn}}
              \left(\frac{H^2}{X}+\frac{H^4}{X^2}\right)\right).
                                                               \tag{21}
\]
The limits in (6) are essential. A stationary center at an index
entry or a band endpoint yields only its corresponding incomplete
Fresnel integral. No full-line stationary-phase theorem or endpoint
discard is used.

With H=X^(3/5), the three costs X/H,H^2/X,H^4/X^2 are
X^(2/5),X^(1/5),X^(2/5). Multiply (20)--(21) by |w_kl|
and sum using (11). The total error is
\[
 O(N_*K X^{2/5})=O(X^{451/500}).                             \tag{22}
\]
The retained expression is exactly (7). Combining (14), (18)
and (22) proves (8): the smaller terms O(hN_*K) and
O(X^(753/1000)q) are absorbed at a common onset. Dividing its
error by B gives O(X^(-49/500)), which tends to zero.

### Actual-P transfer: paid quadratic error and unpaid mixed errors

C019m (19) gives P-S_d=O(1/q) uniformly on J, and C019l (9)
gives S_d+V=O(X^(-3/4)). Thus e(Y)=P(Y)+V(Y) satisfies
sup_J|e|<=C/q. For Y in D, both arguments are in J and
\[
 P(Y)P(Y+h)-V(Y)V(Y+h)
  =-e(Y)V(Y+h)-V(Y)e(Y+h)+e(Y)e(Y+h).                        \tag{23}
\]
The last term, integrated against W>=0, costs at most
(C/q^2)integral_D W=O(X/q), by (3). Apply integral
Cauchy--Schwarz against the measure W(Y)dY separately to each
of the first two terms. Their costs are at most
(C/q)sqrt(integral_D W)*sqrt(Q_h) and the analogous expression
with Q_0. This proves (9), including all three errors and both shifts.
Every function is square-integrable: all are continuous or finite
piecewise-smooth sums on compact intervals, with finitely many entries.

The available coarse estimate does not finish this payment. From (10),
W<=(sum_{k<=K}k^(-1/2))^2<=4K. C019m's square bound and
S_d+V=O(X^(-3/4)) give integral_J V^2=O(Xq). Hence only
Q_0+Q_h=O(KXq) follows by this route, leading in (9) to
O(X*sqrt(K))+O(X/q). That upper bound is insufficient for o(X);
it is not a lower bound or evidence that the actual transfer fails.
Likewise (8) does not give a sign merely because its error is small.

### Scope, remaining discriminator and verification status

All interchanges are finite. Both conjugated and unconjugated
product channels, every arithmetic twist, both true entry times and
stationary centers on boundaries remain explicit. The shift, heat
time, taper and length have not been changed. No gamma phase or
normalization is removed except through the cited local comparisons.

A concrete sufficient completion would establish
R_d+S_d<=-2cB for one absolute c>0 and Q_0+Q_h=o(Xq).
Then (8)--(9) would imply the required actual-P mean <=-cB
eventually. Both premises are unresolved, not imported lemmas or
conclusions of this calculation. A rigorous incompatible actual-P
asymptotic would stop the fixed test. Presently neither sign outcome
has been obtained, so the bounded attempt is inconclusive.

This is a partial local finite-sum reduction beyond the previously
recorded unweighted calculation. The checked sources supply its
classical estimates, not this exact moving-heat statement; no claim
of certified originality is made. The proof was initially checked while
being written; independent audit1401 below now retains it. No numerical
computation or mathematical script is used as evidence.

### Independent conceptual audit1401 — 17 November 2026

This checks the essential reduction under the prior EXPLORE audit
assessment1398, approved1399 and URL-repaired1400. Equations (3)--(9)
are retained without changing their hypotheses or error orders. The
statements that the sign and mixed transfer were unpaid describe this
reduction's original scope; their subsequent treatment is C019r.

**Coefficients, domains and product identity.** The local convolution
coefficients of (2-sqrt(1-z))^2 are 1,1,4c_2,4c_3,..., with
0<4c_r<=1/2 for r>=2. Multiplicativity and the taper in [0,1]
therefore prove |b_k|<=1 even with the complex shift. In (10), the
coefficient is b_k conjugate(b_l)/sqrt(kl) and the frequency is
log(l/k). Summing the logarithmic-integral bound at k!=l and the
harmonic diagonal proves (3). The absolute four-index sum (11) is
16N_*K, not a bound that presumes cancellation of the b coefficients.

The two actual index conditions are precisely rho_m<=Y and
rho_n-h<=Y. Thus each I_mn is one interval; the shift approximation
changes its smooth integrand only. From f_n'=v_n+O(1/(Xq)) and
f_n''=O(1/X), its phase error is
O(h/(Xq)+h^2/X)=O(h/X), uniformly even for an index not yet entered
at Y. The corresponding relative amplitude error is O(h/X).
Their integrated total is (14). The factor 2 Re in (13) follows
from 4 cos(u)cos(v)=2 Re(e^{i(u-v)}+e^{i(u+v)}) and the fact
that the full finite sum representing W is real. No termwise
reality of w_kl is assumed. Substitution then gives (15)--(16),
including -Y log(mn), the twist log(l/k), and the -pi/4 phase.

**Separated difference terms.** For unequal positive integers
u=mk,v=nl<=R=N_*K, |log(v/u)|>=1/R. The displayed derivatives
of the slow phase give |F_-'|>=|eta|/2 because R/(Xq)->0.
The endpoint and amplitude-variation terms in integration by parts
cost C/(sqrt(mn)|eta|); its second-derivative term divided by this
cost is O(1/(Xq|eta|))=o(1). This checks (17) without needing
monotonicity. Reindexing leaves exactly 1/sqrt(uv), and at most
tau(u)tau(v) representations. The elementary prime-power bound gives
tau(u)tau(v)<=C R^{1/2}. Kösters v2 A.3, cited above, applies to
these integer indices, so the total is
O(R^{3/2}log R)=O(X^{753/1000}q). The retained relation is nl=mk.

**Stationary window and all boundaries.** The slow phase is part of
the complex amplitude; x is the stationary center of phi_x only.
On [X/2,2X], both that amplitude's derivative and its total variation
have the bounds in (19). Outside |Y-x|<=H, phi_x' is monotone,
one-signed and separated by cH/X on each component. The cited A.1
applies on every subinterval, so partial integration pays the complex
amplitude variation as well. For x outside [X/2,2X] there is a fixed
positive separation instead, which is stronger.

Inside the window, the connecting segment stays in [X/2,2X]. The
phase remainder integrates to O(H^4/(X^2 sqrt(mn))); the amplitude
remainder integrates to O(H^2/(X sqrt(mn))). Both estimates apply
to the actual truncated interval, including a stationary center at
an entry or endpoint. No complete Fresnel integral is substituted
here. Multiplying by (11), X/H and H^4/X^2 each give
X^{1/2+1/500+2/5}=X^{451/500}; H^2/X gives a smaller power.
Together with (14),(18) this verifies (8) uniformly.

**Actual-P comparison contract.** C019m (19) and C019l (9), with
their recorded audits, give e=P+V=O(1/q) on the entire closed J.
C019j/k use the same strictly positive gamma normalization and own
heat time; their audited uniform errors are inherited, not new
claims of this audit. In (23) both mixed errors have their displayed
minus signs and the quadratic error has a plus sign. Applying
Cauchy--Schwarz to each against the nonnegative measure W dY,
using (3), proves (9). Thus no unweighted estimate has silently
been applied to a weighted error. This audit adds no bound on Q_j
beyond the statements of this lemma.

All thresholds above are uniform consequences of the exact scales
and the previously stated absolute input onsets. Their finite maximum
is an integer onset. This is verification of the existing local
reduction, not a new literature theorem or a stronger result.

## Mathlib

Full matching Mathlib coverage has not been checked. No absence claim
or formal verification is asserted. The cited classical derivative
and logarithmic-sum estimates, finite coefficient identities and
Cauchy--Schwarz are the mathematical inputs used here; possible
supporting formal lemmas have not been substituted for this proof.
