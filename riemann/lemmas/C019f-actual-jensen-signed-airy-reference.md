# C019f — Normalized finite Jensen cubic: Airy limit and endpoint-sign obstruction

## Hypotheses

Use precisely C019c's fixed-field data for K=Q and C019e's finite cubic
integral I_3(d,x), with d tending to infinity through positive integers,
1<=x<=4, q=q_e(d)+x d^(-2/3), the source saddle radius r^2, and both
counterclockwise angular arcs. Keep
\[
 P_d=d!/d^d,\qquad
 M_d(x)=P_d|a_q(-2\alpha)|e^{dH_q}d^{-1/3}>0,
 \qquad \epsilon=(\log d)d^{-1/3}.
\]
All source estimates have the uniform hypotheses verified in C019c and
C019e. The additional source input is the uniform near-edge expansion
in Ono v1, Lemma7, equation (3.11), including its analytic implicit-function
proof. No local-integral lower bound, sign or infinite cubic completion
is assumed. Constants and degree onsets below are existential.

## Conclusion

Put
\[
 a=4^{1/3},\qquad \beta=\frac{16a}{\pi^2},\qquad
 \mathcal F(x)=a\operatorname{Ai}(-\beta x).
\]
Then
\[
 \sup_{1\leq x\leq4}
 \left|\frac{I_3(d,x)}{M_d(x)}-\mathcal F(x)\right|\longrightarrow0.
                                                               \tag{1}
\]
The reference is real and has at least one simple zero in each of (1,2)
and (2,4). Every reference zero is simple. Each nonempty closed subinterval
of [1,4] avoiding all reference zeros has a strictly positive minimum of
\(|\mathcal F|\).
The following exact rational enclosures hold:
\[
 -\frac{257}{1000}\leq\mathcal F(1)\leq-\frac{32}{125}<0,
 \quad
 0<\frac{451}{1000}\leq\mathcal F(2)\leq\frac{113}{250},
 \quad
 -\frac{181}{500}\leq\mathcal F(4)\leq-\frac{361}{1000}<0.       \tag{2}
\]
Thus the approved target's **opposite signs at x=1 and x=4 are false**.
The uniform limit and reference zeros survive this obstruction. No
uniqueness or simplicity of an actual polynomial zero follows here.
This is a local specialization/reproduction of the assessed tools,
retained after the critical audit1357 below; it is not an RH candidate.

## Proof

**Precise imported tools and the needed specialization.** The saddle
expansion is Ken Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, Lemma7/(3.11) and the uniform analytic proof immediately
preceding it. The amplitude uses Lemma12/(4.2)–(4.3), its exact gamma
remainder, and the absolutely convergent half-plane estimates in Lemma13's
proof. C019c/C019e already verify their applicability on these angles.
We use the real improper Airy integral
[DLMF9.5.1](https://dlmf.nist.gov/9.5.E1), the Airy equation and initial
values [9.2.1](https://dlmf.nist.gov/9.2.E1),
[9.2.3](https://dlmf.nist.gov/9.2.E3),
[9.2.4](https://dlmf.nist.gov/9.2.E4), and entire series
[9.4.1](https://dlmf.nist.gov/9.4.E1). DLMF attributes these to Olver,
*Asymptotics and Special Functions*, A.K.Peters, 1997 corrected reprint
of 1974, pp.53, 392 and 54, respectively. Initial-value enclosures use
Euler's integral [DLMF5.2.1](https://dlmf.nist.gov/5.2.E1), for Re(z)>0.
These precise identities are imported, not reproved. Their finite,
degree-dependent specialization, signed prefactor, tail bounds and exact
endpoint evaluation are the work below. No general Gaussian or CFU
conclusion is used as an automatic Airy import.

**Uniform coefficient limits, with the edge retained exactly.** Write
\(\delta=1/\Lambda\), and retain C019e's notation
\[
 A=qr^2,\quad C=2\kappa r/\Lambda,\quad
 R=\alpha/\sin\alpha,\quad
 E=2(A+1)\cos\alpha-2C,\qquad \kappa=\pi/2.
\]
C019c gives uniformly \(\alpha=O(d^{-1/3})\), bounded positive r,
\(\delta\to0\), and \(Tr\to\infty\). The exact identity
\(A-1=CR\) implies \(C=O(\delta)\) and \(A=1+O(\delta)\).
The uniform source expansion says
\[
 x d^{-2/3}=q-q_e
   =\bigl(\kappa^2/4+O(\delta)\bigr)\alpha^2+O(\alpha^4).
\]
The coefficient is bounded away from zero; using the already known
uniform bound for alpha in this identity gives
\[
 d^{2/3}\alpha^2=\frac{4x}{\kappa^2}
                         +O(\delta+d^{-2/3}).                 \tag{3}
\]
In particular q_e was never replaced by its limit inside q-q_e.

For C019e's angular phase let \(\Psi_0=\Psi(0)=-A+E-2\log r\).
Set
\[
 \ell_d=d^{2/3}(-A+C+E/2-1),\quad
 b_d=\frac{d^{1/3}}2(A-C-E/4),\quad
 c_d=\frac16(A-3C/4-E/8).
\]
The exact identities, before any limiting step, are
\[
 \ell_d=d^{2/3}(A+1)(\cos\alpha-1),\qquad
 b_d=\frac{d^{1/3}}4
       \{C(R-1)+(A+1)(1-\cos\alpha)\}.                       \tag{4}
\]
Consequently, uniformly on [1,4],
\[
 \ell_d=-\frac{16x}{\pi^2}+O(\delta+d^{-2/3}),\qquad
 0\leq b_d=O(d^{-1/3}),\qquad
 c_d=\frac1{12}+O(\delta+d^{-2/3}).                           \tag{5}
\]
For (4)–(5) use \(R-1=O(\alpha^2)\),
\(1-\cos\alpha=\alpha^2/2+O(\alpha^4)\), and (3).
All remainders are on a fixed small angular neighborhood. In particular,
no small-o coefficient is multiplied by an uncontrolled power of log d
to compare phases on the entire expanding interval.

**Constant exponent and signed amplitude.** Let
\(D_d=d(\Psi_0-H_q)\). The real quadratic derivative
\(D_2=A-C-E/4\) is O(alpha^2), by (4). C019e's fourth-derivative
bound and its real/imaginary coefficient parity, evaluated at -2alpha,
give
\[
 H_q=\Psi_0+2D_2\alpha^2+O(\alpha^4),\qquad
 |D_d|=O(d\alpha^4)=O(d^{-1/3}).                             \tag{6}
\]
The actual-phase envelope also gives \(D_d\leq0\). For sufficiently
large d, -2alpha lies in the common fixed neighborhood on which that
Taylor bound holds.

Put W=Tr. The exact amplitude of C019c at zero is
\[
 a_q(0)=2^{-1/4}\pi^{1/4}W^{7/4}
                \zeta(1/2+W)g_{\mathbb Q}(W)>0.              \tag{7}
\]
Indeed \(1/2+W>1\), and the source's exact gamma remainder on positive
W is \((1-1/(4W^2))\) times a quotient of positive gamma and elementary
factors. Thus it is positive when W>1/2, rather than merely nonzero.
On both zero and saddle arguments, \(g=1+O(W^{-1})\). At the saddle
\(w=We^{-i\alpha}\), \(\Re(1/2+w)\geq1/2+W/2\) eventually.
For any \(\sigma>1\), absolute convergence gives
\[
 |\zeta(\sigma+it)-1|
 \leq\sum_{n\geq2}n^{-\sigma}
 \leq2^{-\sigma}+\frac{2^{1-\sigma}}{\sigma-1}.
\]
Hence both zeta factors tend to 1 uniformly. The moduli of the two
principal powers \(w^{7/4}\) are the same \(W^{7/4}\). It follows that
\[
 p_d(x):=\frac{a_q(0)}{|a_q(-2\alpha)|}e^{D_d}>0,
 \qquad \sup_{[1,4]}|p_d-1|\longrightarrow0.                 \tag{8}
\]
This identifies the sign of the normalization, not just its modulus.

**The finite oscillatory tails.** C019e's exact orientation formula and
the real substitution \(t=d^{1/3}\theta\) give, with L=log d,
\[
 \frac{I_3}{M_d}
 =\frac{p_d}{2\pi}\int_{-L}^{L}
             e^{b_dt^2}e^{i(\ell_dt+c_dt^3)}\,dt.            \tag{9}
\]
There is no extra radius, phase or orientation factor. The two halves
are conjugate, so (9) is real. Notice that b_d is nonnegative: directly
extending the finite integrand to infinity would not be justified.

For a common sufficiently large degree, (5) ensures
\[
 |\ell_d|\leq8,\quad 1/24\leq c_d\leq1/8,\quad
 e^{b_dL^2}\leq2.
\]
Fix any R>=16 and take L>=R. For \(R\leq t\leq L\), write
\(h=e^{b_dt^2}\), \(\phi=\ell_dt+c_dt^3\). Then
\[
 \phi'\geq t^2/16,\quad |\phi''|\leq3t/4,
 \quad |h|\leq2,\quad |h'|\leq4b_dt.
\]
Finite-interval integration by parts, including both endpoints, gives
\[
 \int_R^L h e^{i\phi}dt
 =\left[\frac{he^{i\phi}}{i\phi'}\right]_R^L
 -\int_R^L\left(\frac{h'}{i\phi'}
                 -\frac{h\phi''}{i(\phi')^2}\right)e^{i\phi}dt.
\]
The two endpoint moduli total at most 64/R^2. The h' term is at most
\(64b_d\log(L/R)\); the other remainder is at most
\(384\int_R^L t^{-3}dt\leq192/R^2\). Therefore
\[
 \left|\int_R^L h e^{i\phi}dt\right|
 \leq\frac{256}{R^2}+64b_d\log(L/R).                        \tag{10}
\]
The negative tail is its conjugate, so its identical bound must also be
included. For fixed R the last term tends to zero uniformly in x,
since \(b_d=O(d^{-1/3})\) and \(L=\log d\).

For the limiting phase \(\phi_0=t^3/12-16xt/\pi^2\), the same
bounds hold with h=1 and b=0, for all t>=R. Its integration-by-parts
boundary at infinity vanishes and the remainder is absolutely bounded
by a constant times \(\int_R^\infty t^{-3}dt\). Thus each improper
tail exists and has modulus at most 256/R^2, uniformly in x.
On every fixed [-R,R], (5) gives uniform convergence of integrands,
so integration over that finite interval is legitimate. Adding the two
finite tails and two limiting tails yields
\[
 \limsup_{d\to\infty}\sup_{[1,4]}
 \left|\int_{-L}^L e^{b_dt^2+i(\ell_dt+c_dt^3)}dt
      -\int_{-\infty}^{\infty}e^{i\phi_0(t)}dt\right|
 \leq\frac{1024}{R^2}.
\]
Now let R tend to infinity. This proves uniform convergence, as well as
uniform boundedness of the finite integrals needed when multiplying by
p_d in (9). No dominated convergence on the entire real axis is invoked.

**Identification of the known Airy integral.** Set t=a s, a=4^(1/3).
Then \(t^3/12=s^3/3\) and \(-16xt/\pi^2=-\beta xs\).
Both one-sided improper tails have just been justified, so conjugation
and the real DLMF9.5.1 formula give
\[
 \frac1{2\pi}\int_{-\infty}^{\infty}e^{i\phi_0(t)}dt
 =\frac a\pi\int_0^\infty\cos(s^3/3-\beta xs)ds
 =a\operatorname{Ai}(-\beta x).
\]
Together with (8)–(10), this proves (1).

**Exact sign certificate, including all numerical errors.** Reproduce with
`python3 scripts/jensen-edge/signed_reference_1355.py`.
The full certificate is `scripts/jensen-edge/signed-reference-1355.json`.
Every comparison uses Python integers and Fraction; floating-point
approximations and published decimal zero tables are not inputs.

Here is the mathematical justification of every approximation in that
script. The pi enclosure uses Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\). To check the branch, if
v=arctan(1/5), then tan(4v)=120/119 and
tan(4v-arctan(1/239))=1; this angle lies in (0,pi/2), so equals pi/4.
Each arctangent is summed through index 100, with absolute error at most
\(1/((203)q^{203})\) by the alternating-series bound. The positive cube
roots of 3 and 4 are enclosed by integer bisection, with both cubed
endpoint inequalities checked exactly.

For m=0,1, Euler's integral with t=u^3 gives
\(\Gamma((m+1)/3)=3\int_0^\infty u^m e^{-u^3}du\).
Taylor's theorem for e^(-v), 0<=v<=64, yields, with N=320,
\[
 S_m=3\sum_{k=0}^{N}
       \frac{(-1)^k4^{3k+m+1}}{k!(3k+m+1)},\qquad
 E_m=\frac{3\,4^{3(N+1)+m+1}}{(N+1)!(3(N+1)+m+1)}.
\]
The integral up to u=4 lies in [S_m-E_m,S_m+E_m]. In the original
t variable, the positive remaining tail is at most
\(\int_{64}^\infty e^{-t}dt=e^{-64}<2^{-64}\), because
t^((m+1)/3-1)<=1 there. Thus the exact gamma enclosure is
\([S_m-E_m,S_m+E_m+2^{-64}]\). Both E_m<10^(-60) are checked.
These positive intervals and the cited initial values give enclosures for
Ai(0) and Ai'(0), with no assumed decimal constants.

For each z=-beta x, x=1,2,4, the argument enclosure lies strictly in
(-11,0). In the two series of DLMF9.4.1 let the initial terms be
\(T_{0,0}=1\), \(T_{1,0}=z\), and use the exact recurrence
\[
 T_{j,k+1}=\frac{z^3 T_{j,k}}{(3k+j+3)(3k+j+2)},\qquad j=0,1.
\]
Sum through k=100, including both endpoints of each interval operation.
Let B_(j,100) be the positive bound obtained by starting at 11^j and
replacing every |z|^3 by 11^3 in this recurrence. Put
\(\rho_j=11^3/((303+j)(302+j))<1\). The entire remaining series
is bounded in absolute value by
\(B_{j,100}\rho_j/(1-\rho_j)\), since all later term ratios are
smaller. Both bounds are checked below 10^(-60). Multiplication by
the two initial-value intervals, summation, and multiplication by a
enclose the reference value. Every intermediate interval is rounded
outward to the rational grid 10^(-60); this only enlarges it. The
certificate retains constants, sums, term intervals and remainder bounds.

The resulting exact intervals have widths less than 10^(-12) for each
of the three values (the required check was 10^(-6)). Rounding these
intervals further outward to denominator 1000 gives exactly (2).
The complete selected initial-value, beta and reference intervals and
the complete certificate summary were inspected with
`python3 ../scripts/loop/inspect_json.py` using their exact pointers and
`--full`. The canonical proof uses their exact rational signs, not a
bounded preview. The script reports the failed opposite-endpoint
condition explicitly; it is not treated as a failed enclosure check.

**Zeros, margins and limits of transfer.** By (2), the intermediate value
theorem gives a reference zero in each of (1,2) and (2,4). Any multiple
real zero of Ai would give both Ai and Ai' zero there. Uniqueness for
the linear ODE y''=z y (DLMF9.2.1) would then force the identically zero
solution, contradicting the positive exact Ai(0). Scaling by the nonzero
constants a and -beta preserves simplicity. On each closed zero-free
subinterval, continuity and the extreme-value theorem give
\(\min|\mathcal F|>0\); the constant depends on the chosen subinterval.
There is no positive absolute margin across a reference zero, and no
claim that the window contains only one or only two zeros.

Equation (1) permits eventual sign transfer wherever that reference
margin is positive. Combining with C019c/C019d/C019e is a plausible
later actual-integral application, not a new global root theorem here.
Uniform value convergence alone does not prove uniqueness or simplicity
of polynomial zeros. The fixed endpoint opposition is disproved by
(2); moving endpoints to rescue it would change the target. Other edge
windows, the exceptional-root deficit, all-degree hyperbolicity and
L030–L032/C032a positivity remain unresolved. No effective degree onset,
full source-manuscript audit or source formal-artifact validation is supplied.

**Critical audit, 17 November 2026 (1357).** This independent replay
retains (1)–(2) with exactly the same hypotheses, scale, radius, window
and arc orientations. It uses C019c/C019e directly, with C019d upstream;
no additional mathematical input or DAG edge is needed. Coverage1355 is
reused under SPECIALIZE/REPRODUCTION. Stops1345 and1355 remain in force
for their stated automatic-import and endpoint-opposition claims.

The primary v1 Lemma7 statement, (3.8)–(3.11) and uniform implicit-function
proof, Lemma12's exact gamma remainder, and Lemma13's half-plane proof
were compared with the actual uses. The DLMF identities cited above were
checked in their real-integral, entire-series and positive-Gamma-argument
ranges. This is an audit of these applications, not of the full manuscript
or its formal artifacts. In particular no rescaled local C1 conclusion
from Lemma13 is extended to a larger arc. C019d's fixed-angle half-plane
check supplies the requisite amplitude control there.

For the coefficient replay, substituting E into the linear coefficient
cancels C exactly, giving (A+1)(cos(alpha)-1). For the quadratic
coefficient, the exact identity is
\[
 D_2=A-C-E/4
 =\tfrac12\{C(R-1)+(A+1)(1-\cos\alpha)\}\geq0.
\]
Thus D_2=O(alpha^2), uniformly. The source expansion, with its positive
quadratic coefficient bounded away from zero, gives (3); its O(alpha^4)
error becomes O(d^(-2/3)) after multiplying by d^(2/3). This reproduces
ell_d, b_d and c_d in (5), including c_d -> 1/12 and the sign of b_d.
No factor (log d)^3 is applied to the slowly vanishing O(1/Lambda) error.
Evaluating the fourth-order remainder at -2alpha gives explicitly
\[
 |H_q-\Psi_0-2D_2\alpha^2|\leq(10/3)\alpha^4.
\]
Consequently (6) has the claimed uniform order, and the actual envelope
gives its stated nonpositive sign. The exact positive-real gamma quotient
and positive zeta series at W>1/2 establish a_q(0)>0. Uniform convergence
of both zeta and gamma factors to 1 at zero and the saddle then proves
p_d -> 1 with its positive sign. The angular Jacobian is d^(-1/3),
canceling the same factor in M_d; conjugation pairs the two increasing,
counterclockwise angular intervals with a plus sign.

The tail constants also survive independent calculation. For t>=R>=16,
\(3c_dt^2+\ell_d\geq t^2/8-8\geq t^2/16\).
The two endpoint bounds are 32/R^2+32/L^2, at most 64/R^2.
The differentiated-amplitude term is 64 b_d log(L/R), and the other
remainder is at most 384 integral_R^L t^(-3) dt <=192/R^2.
For fixed R, b_d log(L/R) ->0 uniformly; L>=R eventually.
The limiting tails obey the same bounds with b=0. Accordingly all four
tails total at most 1024/R^2 in the limsup. Taking d to infinity first,
then R to infinity, proves the claimed uniform limit and boundedness
needed for multiplying by p_d. This argument never forms an infinite
integral with b_d>0 and never uses global dominated convergence.

The original exact certificate replay is byte-identical and preserved at
`scripts/jensen-edge/replay-1357/signed-reference-1355.json`. Its SHA256 is
`a44707eebebd2194531f68993719e76a728cc09a4e0bbc8da5b2f84a44dc2c86`.
An independent checker is reproducible with
`python3 scripts/jensen-edge/audit_signed_reference_1357.py`; full evidence
is `scripts/jensen-edge/signed-reference-audit-1357.json`.
It imports no functions from the original script. In particular every one
of the 606 retained Airy terms is checked using the closed-form coefficient
\[
 T_{j,k}(z)=\frac{\prod_{h=0}^{k-1}(3h+j+1)}{(3k+j)!}\,z^{3k+j},
 \qquad j=0,1,\quad 0\leq k\leq100.
\]
Cancellation of successive numerator and factorial factors gives exactly
the recurrence already proved above. Real endpoint powers enclose each
term on the negative argument interval. Their independently rounded sums
are contained in the saved sums. The first omitted bound is computed
directly from the same formula at k=101 and |z|=11; the decreasing-ratio
geometric bound is checked in full. The checker also verifies both entire
Gamma sums, their integrated Taylor errors and positive tails, cube-root
endpoint inequalities, Machin bounds, initial values, beta, all final
interval inclusions, widths and signs. The analytic Taylor remainder uses
|exp(-v)|<=1 on v>=0; the Gamma tail uses e>2 and t^(z-1)<=1 for t>=64,
z=1/3,2/3. Thus the numerical bounds cover all truncation and rounding
errors, rather than merely repeating decimal values.

All 1304 checker assertions pass. The three exact saved widths are
strictly below 10^(-12), against the required 10^(-6); each Gamma Taylor
error and each Airy series tail is below 10^(-60). The positive Gamma-tail
bound remains 2^(-64), not 10^(-60). Complete selected rational reference
intervals, widths and the summary were inspected using the JSON inspector
with `--full`; all retained terms were traversed by the independent checker.
There is no enclosure failure. The opposite-endpoint condition still fails,
since both endpoint upper bounds are strictly negative. IVT and uniqueness
for the Airy ODE justify the stated reference zeros and their simplicity;
neither asserts an exact zero count in [1,4]. Compact zero-free margins
remain dependent on the compact set. Actual-polynomial identification,
root transfer, uniqueness/simplicity, effective onset and global closure
are not established by this audit. No stronger theorem or novelty beyond
the assessed sources is claimed.

## Mathlib

Full matching theorem and supporting formal theorem coverage were not
checked. The exact rational script is an informal computational certificate,
not a Lean proof. DLMF supplies the known analytic identities; the
degree-dependent uniform limit and the particular strict sign bounds are
justified above. No originality beyond the checked literature is claimed.
