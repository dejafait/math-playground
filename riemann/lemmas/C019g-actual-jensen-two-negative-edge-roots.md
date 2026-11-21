# C019g — Actual unshifted Jensen polynomial: two negative edge roots

## Hypotheses

Use C019c-C019f's exact fixed-field data for K=Q, their imported source
estimates and their established uniform conclusions. The completed xi
is L018's xi. Define the real entire function and unshifted polynomial by
\[
 F(z)=\xi(1/2+\sqrt z)=\sum_{j\geq0}\frac{\gamma(j)}{j!}z^j,
 \qquad
 J_d(X)=\sum_{j=0}^d\binom dj\gamma(j)X^j,
 \qquad d\in\mathbb Z_{\geq1}.
\]
The square-root expression denotes the single-valued entire function
given by the even Taylor expansion, not a chosen cut across the circle.
Retain the degree-dependent quantities
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad
 T>2\pi e,\quad \Lambda=2\left(\log\frac{T}{2\pi}-1\right),
 \quad B=T^2,\quad \kappa=\pi/2,
\]
\[
 \kappa r_e\left(1+\frac{2\log r_e}{\Lambda}\right)=2,
 \quad q_e=r_e^{-2}+\frac{2\kappa}{\Lambda r_e},\quad
 q_d(x)=q_e(d)+xd^{-2/3},\qquad 1\leq x\leq4.
\]
Here r_e is the positive source edge radius. Use C019c's actual saddle
radius r(d,x)^2, phase h_q, amplitude a_q and saddle angle alpha, with
\[
 H_q=\Re h_q(r^2e^{-2i\alpha}),\quad P_d=d!/d^d,\quad
 M_d(x)=P_d|a_q(-2\alpha)|e^{dH_q}d^{-1/3}>0
\]
at their common eventual onset. All arcs have their original
counterclockwise orientation. No effective degree threshold is assumed.

## Conclusion

With
\[
 R_d(y)=y^dJ_d(1/y),\qquad A_d(y)=(B/d)^dR_d(dy/B),\qquad
 \mathcal F(x)=4^{1/3}\operatorname{Ai}(-16\,4^{1/3}x/\pi^2),
\]
where R_d is understood as its polynomial extension at zero, one has
\[
 \sup_{1\leq x\leq4}
 \left|\frac{A_d(-q_d(x))}{M_d(x)}-\mathcal F(x)\right|
 \longrightarrow0.                                             \tag{1}
\]
There is a single integer D such that every integer d>=D satisfies
\[
 \frac{A_d(-q_d(1))}{M_d(1)}<-\frac{16}{125},\qquad
 \frac{A_d(-q_d(2))}{M_d(2)}>\frac{323}{1000},\qquad
 \frac{A_d(-q_d(4))}{M_d(4)}<-\frac{233}{1000}.                  \tag{2}
\]
In particular, put
\[
 X_d(x)=-\frac{B}{d(q_e(d)+xd^{-2/3})}.
\]
For every d>=D, the actual unshifted J_d has at least one zero in each
of the disjoint negative intervals
\[
 (X_d(1),X_d(2)),\qquad (X_d(2),X_d(4)).                       \tag{3}
\]
These give at least two distinct negative zeros. No uniqueness,
simplicity, effective D, improvement of a bulk exceptional-root bound,
or every-degree hyperbolicity is asserted. This is a local specialization
of the assessed inputs, retained after the critical application audit1361
below.

## Proof

**Exact polynomial and coefficient conventions.** The imported primary
identities are Ken Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, (1.1)-(1.4), (1.8), and (2.8)-(2.10). In particular,
for the entire F above, d>=1, B>0, q>0 and any counterclockwise circle
about zero, (2.9) states exactly
\[
 A_d(-q)=\frac{d!}{2\pi i d^d}
           \oint F(Bu)e^{-dqu}\frac{du}{u^{d+1}}.             \tag{4}
\]
Import this identity; no new Cauchy coefficient-extraction theorem is
being proved. Its arbitrary-circle provision permits the positive
radius r(d,x)^2 separately for every d,x. The phase factorization and
angular measure are precisely those already checked in C019c-C019e
against the source's (4.4)-(4.5) and Proposition15.

For the local coefficient check, L018 gives
Xi(z)=xi(1/2+iz). L021's entire Taylor series therefore gives
\[
 F(z)=\sum_{j\geq0}\frac{M_{2j}}{(2j)!}z^j,
 \qquad \gamma(j)=\frac{j!}{(2j)!}M_{2j}.                    \tag{5}
\]
Indeed Xi(-i sqrt(z)) has the displayed series because its two factors
(-1)^j cancel; evenness makes the identity single-valued and entire.
This uses L021's already justified locally uniform expansion. Thus (5)
agrees with the factorial convention of the cited source, and all
coefficients of J_d are real. Neither the raw moments nor a differently
normalized alternating polynomial replaces gamma(j). Also P_d=d!/d^d
is a scalar here, not a polynomial. Kernel formulas need not be
reimported with a different factor of two.

**One circle and one positive normalization.** Fix theta_0=1/10 once
and let epsilon=(log d)d^(-1/3). Take d beyond the finite maximum of
the uniform onsets in C019c-C019f, so epsilon<theta_0 and M_d(x)>0
for every x in [1,4]. The source parameter conditions also hold at this
onset. In particular q_e>0 since r_e, Lambda and kappa are positive,
and q_d(x)>0 throughout the window, as required in (4).

Parameterize the same circle in (4) by u=r^2 exp(i theta), with theta
in [-pi,pi] increasing. The three angular sets
\[
 \{|\theta|\geq\theta_0\},\qquad
 \{\epsilon\leq|\theta|\leq\theta_0\},\qquad
 \{|\theta|\leq\epsilon\}
\]
partition it up to endpoints of zero integration measure. The actual
integrand F(Bu)exp(-dqu)u^(-d) is single-valued on this circle, including
the coincident negative-axis endpoints: d is an integer. The angular
measure is du/u=i dtheta. Consequently, with exactly the integrals
defined in C019c, C019d and C019e,
\[
 A_d(-q_d(x))=I_{\rm out}+I_{\rm ann}+I_{\rm loc}.            \tag{6}
\]
There is no reversed arc, additional radius factor, connector, contour
deformation or missing arc. The local branches used in the estimates
represent these same actual integrals.

Write \(\eta_d=\sup_{x\in[1,4]}|I_3(d,x)/M_d(x)-\mathcal F(x)|\),
so eta_d tends to zero by C019f. With the same finite constants B_0,B_1
as C019d/C019e, and the fixed-cutoff constants C_out,gamma_out>0 from
C019c, define
\[
 \begin{split}
 E_d={}&C_{\rm out}\frac{d^{4/3}}{\log d}e^{-\gamma_{\rm out}d}
       +\frac{1216B_0}{9\pi(\log d)^2}
       +\frac{32B_1}{3\pi d^{1/3}\log d}\\
 &+d^{-1/3}\left[
       \frac{B_1}{2\pi}(\log d)^2+
       \frac{B_0}{24\pi}e^{\delta_d}(\log d)^5\right]+\eta_d,
 \qquad \delta_d=\frac5{24}d^{-1/3}(\log d)^4.
 \end{split}                                                \tag{7}
\]
All quantities in (7) are independent of x. Their bounds apply
simultaneously after enlarging the same onset. Equation (6), the
triangle inequality, and the three cited error estimates give
\[
 \sup_{[1,4]}
 \left|\frac{A_d(-q_d(x))}{M_d(x)}-\mathcal F(x)\right|
 \leq E_d\longrightarrow0.                                  \tag{8}
\]
For the limit, the exponential dominates its polynomial factor, the
annular terms vanish, delta_d tends to zero, the local powers of log d
are dominated by d^(1/3), and eta_d tends to zero. All four contributions
use the identical M_d(x), not merely asymptotically proportional scales.
This proves (1). No division by I_3 or the possibly vanishing reference
is used, and no new infinite-integral limit is interchanged.

**A common strict sign margin.** C019f's audited rational enclosures
give \(\mathcal F(1)\leq-32/125\), \(\mathcal F(2)\geq451/1000\) and
\(\mathcal F(4)\leq-361/1000\). The least of their guaranteed absolute margins
is 32/125. Choose one integer D above the preceding onsets such that
E_d<16/125 for every d>=D; (7)-(8) give its existence. Subtracting or
adding this error gives respectively
\[
 -32/125+16/125=-16/125,\quad
 451/1000-16/125=323/1000,\quad
 -361/1000+16/125=-233/1000,
\]
with strict inequalities because E_d is strictly smaller than 16/125.
These prove (2). Multiplication by the positive M_d preserves the
negative/positive/negative signs of A_d itself. This is an existential
all-d>=D assertion; the unevaluated constants and eta_d supply no
numerical degree threshold.

**Real roots and the exact reciprocal map.** For each fixed d>=D,
the function x -> A_d(-q_e-xd^(-2/3)) is a real polynomial in x, hence
continuous on both [1,2] and [2,4]. Apply the standard intermediate
value theorem to (2). It gives x_1 in (1,2) and x_2 in (2,4) at which
A_d(-q_d(x_j))=0. Continuity of a contour, saddle choice or normalized
quotient is not needed: continuity is that of the exact polynomial.

Specializing the imported definitions (1.8),(2.8) at y=-q gives
\[
 A_d(-q)=(B/d)^d(-dq/B)^d J_d(-B/(dq))
        =(-q)^dJ_d(-B/(dq)).                                \tag{9}
\]
For q>0 the factor is nonzero and has sign (-1)^d. Thus zeros transfer
in both directions, as in source (2.10); signs of J_d, when needed,
are (-1)^d times the corresponding signs of A_d. A positive M_d does
not remove this parity factor.

For fixed d and 1<=x<y<=4, the denominators are positive and
\[
 X_d(y)-X_d(x)
   =\frac{B\,d^{-5/3}(y-x)}{q_d(x)q_d(y)}>0.                \tag{10}
\]
The same nonzero denominators make X_d continuous. It is therefore
strictly increasing, with X_d(1)<X_d(2)<X_d(4)<0, and maps the two
open x-intervals onto the two disjoint open intervals in (3).
Equations (9)-(10) transfer x_1,x_2 to distinct negative roots of J_d.
This proves exactly the claimed existence and locations.

**Qualifications and relevance.** A C0 comparison and sign changes
prove neither uniqueness nor simplicity of these actual roots; the
simple zeros of the Airy reference do not change that limitation.
The same-sign endpoint obstruction in C019f remains true, and this
proof uses the certified interior point x=2. It does not automatically
import a generic Airy asymptotic or discard the contour-payment work.
Ono v1 Theorem1 already supplies a much larger bulk count,
at least d-C sqrt(d log d) distinct negative roots. The present result
locates two roots in the specified edge intervals; without a separate
disjointness proof they cannot be added to that count. No decrease of
the unbounded exceptional-root deficit, other-edge result, all-degree
positivity or RH conclusion follows. No novelty beyond the assessed
sources is claimed. Source-wide validity and asserted formal artifacts
have not been independently audited by this specialization.

**Critical application audit, 17 November 2026 (1361).** Under the
unchanged SPECIALIZE coverage1359, this replay retains (1)-(3). It audits
the finite application of L018/L021 and C019c-C019f, not the underlying
source manuscript or its asserted formal artifacts. The primary
identities (1.1)-(1.4), (1.8), (2.8)-(2.10), the factorization
(4.4)-(4.5), and Proposition15's angular substitution are reused as
inspected in review1358; no additional source theorem is imported.

First, L021's coefficient of z^(2j) in Xi is
(-1)^j M_(2j)/(2j)!. Substitution of -i sqrt(z) multiplies this by
another (-1)^j. Comparing the resulting coefficient with gamma(j)/j!
gives exactly (5), with no remaining alternating sign or omitted
factorial. This is the F in the cited full-circle identity (4).
The scalar P_d remains d!/d^d throughout.

Second, fix theta_0=1/10 in C019c and C019d, and use C019e's same
epsilon and radius. All three actual contributions include
F(T^2u)exp(-dqu)du/u^(d+1), with the same prefactor P_d/(2 pi i).
Their angular domains cover [-pi,pi], with overlap only at finitely
many endpoints. Integer d and the entire F make the actual integrand
single-valued; local logarithm branches do not change the integral.
Thus (6) is an equality of the actual integrals. Each input divides
by exactly P_d|a_q(-2alpha)|exp(dH_q)d^(-1/3), positive at one uniform
onset. In particular no comparison of different normalizations is
needed.

For an explicit quantifier check, group (7) into exterior, annular,
local-replacement and reference errors. Each is nonnegative,
independent of x, and tends to zero by the recorded uniform input
conclusions. Delta_d tends to zero, so the exponential in the local
bound stays bounded. Choose an integer onset for each grouped error
to be strictly below 4/125 for every later degree. The maximum of
these four onsets and the finitely many input onsets gives a single D
with E_d<16/125 for all d>=D and all x in [1,4]. This is a uniform
tail assertion, not a sequence of point-dependent choices. The three
resulting strict margins are exactly -128/1000, 323/1000 and
-233/1000. Positivity of M_d preserves them as signs of A_d.

Finally, for fixed d the polynomial A_d(-q_e-xd^(-2/3)) is continuous,
and its value at x=2 is strictly positive. The two IVT roots lie in
the open intervals (1,2) and (2,4). In (9) the multiplier is
(-q)^d, nonzero with parity (-1)^d since q_e>0 and x>0. Formula (10)
has the factor B*d^(-5/3), is strictly positive for y>x, and has no
vanishing denominator. Hence the two images are precisely the
disjoint negative open intervals (3). This verifies distinctness,
without any derivative or multiplicity claim. No mismatch or proof
repair was needed. The dependency row remains unchanged. The
existential onset, other edges, overlap with the source's bulk count,
unbounded exceptional-root deficit and all-degree hyperbolicity remain
unresolved; the audit establishes no stronger conclusion than C019g.

## Mathlib

The full matching theorem and supporting formal coverage were not
checked. The named intermediate value theorem is used only for a real
polynomial on a closed bounded real interval with strictly opposite
endpoint signs. The proof is informal and imports precisely the cited
Cauchy identity and the recorded analytic estimates; no verified Lean
artifact is asserted.
