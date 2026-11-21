# C467d — Actual-h chart-exhaustion mass deficit

## Hypotheses

Use precisely the actual chart and original first-lifetime current of
C467c, with C466's audited cone and C467b's audited tested balance:
\[
 h_\xi(w)=\xi(1/2+\sqrt w)/\xi(1/2),\quad e^{B(w)}=h_\xi(w),
 \quad B(1)=\log h_\xi(1)\in\mathbb R,\quad x=B'(1),
\]
\[
 g(z)=B'(1+z)-x,\quad
 H(z)=\sum_{j=1}^3[B(1+z_j)-x(1+z_j)],\quad H_0=3[B(1)-x].
\]
The normalized branch is on \(|w-1|<1/4\). Put
\[
 R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad I=(-a,a)^3,
 \quad \Delta(z)=\prod_{i<j}(z_j-z_i),\quad F=\Delta^2e^{-H}.
\]
For distinct real parameters use the raw solution
\[
 \dot X_j=-2\sum_{\ell\ne j}\frac{X_j-X_\ell}{|X_j-X_\ell|^2}
                  +\overline{g(X_j)},\qquad X(0,u)=iu
                                                        \tag{1}
\]
only before its first maximal lifetime \(\tau(u)\) in
\(\{|z_j|<R\}\setminus\{\Delta=0\}\). There is no restart.
Retain C467c's external density qualifications: the analytic assertion
does not prove the imported density realization or assume RH.

Fix the same ambient smooth compact cutoff \(\chi\), equal to one near
the closed Euclidean ball of radius \((\sqrt3+1)/16\). On survivors set
\[
 J_j=\partial_{u_j}X,\quad V=\dot X,\quad J=[J_1,J_2,J_3],
 \quad A=\chi F\det_{\mathbb C}J,\quad
 B_{ij}=\chi F\det_{\mathbb C}[V,J_i,J_j],
\]
\[
 G=F\{d\chi(V)\det[J_1,J_2,J_3]
       -d\chi(J_1)\det[V,J_2,J_3]
       +d\chi(J_2)\det[V,J_1,J_3]
       -d\chi(J_3)\det[V,J_1,J_2]\}.                   \tag{2}
\]
All cutoff factors are evaluated at \(X\), and \(d\chi\) is real.
Extend every coefficient by zero off the original survivor domain,
including initial diagonals. No derivative of a stopped map is used.

For each integer \(k\ge2\), prescribe nomination1006's datum
\[
 a_k=a(1-1/k),\qquad
 \eta_{0,k}(u)=\prod_{j=1}^3 b_k(u_j/a_k),\qquad
 b_k(s)=\begin{cases}
 \exp[-1/(k(1-s^2))],&|s|<1,\\
 0,&|s|\ge1.
 \end{cases}                                           \tag{3}
\]
An admissible \(\eta_k\) is real, smooth in space and \(C^1\) in time
on \([0,T_0]\times I\), with continuous bounded first derivatives,
\(0\le\eta_k\le1\), \(\eta_k(0,\cdot)=\eta_{0,k}\), and a single
compact spatial support \(K_k\Subset I\) for all times. Support and
derivative bounds may depend on \(k\).

## Conclusion

For every integer \(k\ge10^6\), no such test can satisfy
\[
 \operatorname{Re}\left[-i\int_I
 \{(\eta_k)_t A+\eta_k G-(\eta_k)_1B_{23}
                    +(\eta_k)_2B_{13}-(\eta_k)_3B_{12}\}\,du\right]
 \ge0\quad\text{for almost every }t\in(0,T_0).          \tag{4}
\]
In particular no unbounded set of the prescribed integer indices has
these capped integrated payments.

More precisely, define the positive finite reference mass and actual
raw survivor capacity by
\[
 W=\int_I|F(iu)|\,du,\qquad
 C(t)=\int_I\rho(t,u)\,du,\qquad \rho=\operatorname{Re}(-iA).
\]
Then \(\rho\ge0\) everywhere after zero extension, and
\[
 C(t)\le e^{-335t}W,\qquad
 C(t)\le\frac{768}{835}W<\frac{23}{25}W
       \quad(T_0/2\le t<T_0).                          \tag{5}
\]
For every \(k\ge10^6\), the initial real signed mass obeys
\[
 M_k:=\int_I\eta_{0,k}(u)\Delta(u)^2
                    \operatorname{Re}(e^{-H(iu)})\,du
       >\frac{47}{50}W.                               \tag{6}
\]
The required necessity \(M_k\le C(t)\) at almost every positive time
therefore fails on a positive-measure time interval. The separation
between the displayed lower and upper thresholds is \(W/50>0\).

This is the negative outcome of the ready1007-approved bounded
attempt1009. Independent conceptual audit1011 below validates the full
analytic proof with unchanged hypotheses and constants; the rational
certificate checks arithmetic, not that analytic proof. It obstructs this exact local initial-data
exhaustion, preserves C467c's attenuated fixed-bump payment, and proves
neither global assembly, all-degree positivity, Xi transfer nor an RH
candidate. Smaller k and changed caps, interface data or currents are
not decided. No originality claim is made beyond the comparisons in
ready1007 and nomination1006.

## Proof

### Imported inputs and scope of the specialization

C466/audit993 supplies \(g(0)=0\), \(|g'|<40\),
\(|H(iu)-H_0|\le15/64\), the full survivor sign
\(\rho>0\), and the full fixed-time Jacobian framework.
C467c's radial estimate (22) and its preceding proof give
\(\|X(t,u)\|\le\|u\|\) on every original survivor. These estimates
have constants independent of the pair gaps. C466y/audit983 supplies
the real variational equation, the weighted exterior-volume estimate,
bounded Borel zero extensions and the complete weak-current identity.
C467b/audit1002 supplies the full time-dependent representative balance.
Its proof applies to any datum satisfying the stated test regularity;
its separate pointwise obstruction is not used here.

The real exterior-growth input underlying C466y is Wu, Kanevskiy and
Margaliot, *k-Contraction: Theory and Applications*,
[arXiv:2008.10321v2, 27 September 2021, Section 3.1 (29),
Theorem 4/Proposition 5 and proofs, printed pp.8–9](https://arxiv.org/pdf/2008.10321v2).
Only its bound by the integrated matrix measure is used, for continuous
real coefficient matrices on compact intervals before \(\tau(u)\).
No global contraction theorem or stopped extension is imported. C466y
already proves the special pair-spectrum and determinant comparisons
needed here. We use those inputs rather than reprove the source theorem.

For integration, reuse J. K. Hunter, *Measure Theory*,
[Theorem 4.24, printed p.49](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11)
(dominated convergence) and
[Theorem 5.18, printed p.61](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf#page=8)
(Fubini), already assessed with these inputs. Representative endpoints
are provided by C467b using T. Muthukumar, *Sobolev Spaces and
Applications*, 17 December 2023,
[Theorem 2.8.2 and proof, printed p.109](https://home.iitk.ac.in/~tmk/courses/mth656/main.pdf#page=117),
and the bounded-derivative fundamental theorem recorded there. We do
not upgrade per-test almost-everywhere raw identification to arbitrary
terminal slices.

The necessary difference from the ready literature is quantitative:
retain the negative singular term in C466y's weighted three-volume
estimate, bound it over every actual survivor, and compare with this
prescribed near-unit initial family. No static-cap optimization theorem,
global real transport velocity or lifetime regularity is used.

### Uniform decay of the full weighted spatial Jacobian

Fix distinct \(u\in I\) and \(0<T<\min\{T_0,\tau(u)\}\). All ODE
operations in this paragraph take place on the compact surviving
interval \([0,T]\). Write
\[
 f_0=-2\nabla\log\Delta,\quad h=\nabla H=(g(X_j))_{j=1}^3,
 \quad f=f_0+h,\quad P=\sum_{i<j}|X_i-X_j|^{-2}.
\]
The letter \(h\) here denotes the background gradient, not \(h_\xi\).
Because each segment from zero to \(X_j\) lies in the original disk,
\(|g(X_j)|\le40|X_j|\), and the diagonal background Hessian has
operator norm at most 40. C467c's radial contraction therefore yields
\[
 \|X\|^2\le3a^2=3/256,\qquad \|h\|^2\le1600(3/256)=75/4.
                                                               \tag{7}
\]
For completeness, the input contraction follows from its exact identity
\((\|X\|^2)'=-12+2\operatorname{Re}\sum\overline X_j\overline{g(X_j)}
\le-12+80\|X\|^2\): at any attempted upward crossing of the initial
level \(\|u\|^2\le3/256\), the derivative is strictly negative.
This uses original survivors only and supplies no endpoint continuation.

The pair-distance identity and Cauchy–Schwarz give
\[
 \sum_{i<j}|X_i-X_j|^2
   =3\|X\|^2-|X_1+X_2+X_3|^2\le9/256,
 \qquad P\ge\frac9{\sum_{i<j}|X_i-X_j|^2}\ge256.       \tag{8}
\]
All pair distances here are nonzero. C466y's (7),(12) give
\[
 \|f_0\|^2\ge8P,\qquad
 \mu_3(Dv)\le4P+3\cdot40=4P+120,                     \tag{9}
\]
where \(\mu_3\) is the sum of the three largest eigenvalues of the
real symmetric variational matrix. The 40 in (9) is justified along
the entire interval by the actual Hessian bound; the original global
constant 1000 need not be retained in this pointwise estimate.

Young's inequality, explicitly
\(2\operatorname{Re}\langle f_0,h\rangle
\ge-\|f_0\|^2/4-4\|h\|^2\), gives
\[
 \|f_0+h\|^2\ge\tfrac34\|f_0\|^2-3\|h\|^2.
\]
Consequently (7)–(9) imply the uniform differential exponent bound
\[
 \mu_3(Dv)-\|f\|^2
 \le4P+120-6P+225/4
 \le-512+120+225/4=-1343/4<-335.                       \tag{10}
\]
This estimates the complete coupled real variational matrix; there is
no factorization into independent pair Jacobians.

Let \(\mathcal V_3(t)=\|J_1\wedge J_2\wedge J_3\|_{\mathbb R^6}\).
It starts at one. The exterior-growth input and exact weight law
\((|F(X)|)'=-\|f\|^2|F(X)|\), applied on this same compact interval,
give
\[
 |F(X(t,u))|\mathcal V_3(t)
 \le |F(iu)|\exp\int_0^t(\mu_3(Dv)-\|f\|^2)\,dr
 \le |F(iu)|e^{-335t}.                                \tag{11}
\]
C466y's complex-determinant/real-volume comparison gives
\(|\det_{\mathbb C}J|\le\mathcal V_3\). C467b's strict-buffer
argument makes \(\chi(X)=1\) and every term of (2)'s \(G\) zero.
Thus the full actual spatial coefficient satisfies
\[
 0<\rho(t,u)\le|A(t,u)|\le|F(iu)|e^{-335t}             \tag{12}
\]
on survivors. Since \(T\) was arbitrary, this holds at every survivor
point before \(T_0\), with constants independent of proximity to a
collision. After zero extension it holds with \(0\le\rho\) everywhere
on \((0,T_0)\times I\). No limiting collision value is assumed.

### Domination and the prescribed initial masses

Put \(c=15/64\) and \(D_0=\int_I\Delta(u)^2\,du\). This integral is
finite and positive: its integrand is a continuous polynomial on the
closed bounded cube and strictly positive on an open distinct-coordinate
subcube. The initial phase and modulus estimates imply
\[
 e^{-H_0-c}\Delta(u)^2\le|F(iu)|\le e^{-H_0+c}\Delta(u)^2,
 \quad
 \Delta(u)^2\operatorname{Re}(e^{-H(iu)})
             \ge\cos(c)|F(iu)|.                       \tag{13}
\]
Here \(\Delta(iu)^2=-\Delta(u)^2\), while the real mass uses the
\(-i\) normalization of the full initial pullback. Formula (13) gives
\(0<W<\infty\). It dominates (12), so integration over all parameters
proves the first inequality in (5), including every survivor and with
zero contribution from every stopped parameter. Borel measurability is
the already established first-lifetime extension, not an assumption on
the regularity of \(\tau\).

For each fixed \(u\in I\), \(a_k\to a\), and eventually
\(|u_j|<a_k\); the exponent in each factor of (3) tends to zero.
Thus \(\eta_{0,k}\to1\) pointwise in \(I\). Also
\(0\le\eta_{0,k}\le1\), so (13) and the cited dominated-convergence
theorem prove
\[
 M_k\longrightarrow M_\infty
   :=\int_I\Delta(u)^2\operatorname{Re}(e^{-H(iu)})\,du.
                                                               \tag{14}
\]
This limit is not used to hide a non-effective threshold: the following
explicit estimate proves (6).

Let \(k\ge k_0:=10^6\), \(\lambda=999/1000\), and
\(I_\lambda=(-\lambda a,\lambda a)^3\). On this inner cube,
\[
 |u_j/a_k|\le\frac\lambda{1-1/k_0}
             =\frac{999000}{999999},\qquad
 1-\left(\frac{999000}{999999}\right)^2>\frac1{1000}.
                                                               \tag{15}
\]
Therefore the sum of the three positive exponents in (3) is at most
\(3000/k\le3/1000\), and
\[
 \eta_{0,k}\ge e^{-3/1000}\ge997/1000\quad\hbox{on }I_\lambda.
                                                               \tag{16}
\]
Homogeneity of the degree-six polynomial \(\Delta^2\) and the
three-dimensional substitution \(u=\lambda v\) give
\(\int_{I_\lambda}\Delta^2=\lambda^9D_0\). By (13),
\[
 \int_{I\setminus I_\lambda}|F(iu)|\,du
 \le e^{-H_0+c}(1-\lambda^9)D_0
 \le e^{2c}(1-\lambda^9)W
 <2\cdot\frac9{1000}W.                               \tag{17}
\]
Here \(e^{2c}=e^{15/32}\le(1-15/32)^{-1}=32/17<2\), by comparing
the positive exponential series with the geometric series. Also
\((1-1/1000)^9\ge1-9/1000\), by the elementary Bernoulli inequality
(or its nine-step induction). Finally
\(\cos c\ge1-c^2/2>97/100\). Equations (13),(16),(17) prove
\[
 M_k>\frac{97}{100}\frac{997}{1000}\frac{982}{1000}W
     =\frac{47484119}{50000000}W>\frac{47}{50}W.        \tag{18}
\]
The proof bounds all excluded boundary mass, including arbitrary
relative spacings; it is independent of the certified reserve boxes.

For \(t\in[T_0/2,T_0)\), \(e^x\ge1+x\) and (12) yield
\[
 C(t)\le\frac{1}{1+335/3840}W
       =\frac{768}{835}W<\frac{23}{25}W,               \tag{19}
\]
as required. None of (15)–(19) uses floating-point values of \(B\),
\(H_0\), a trajectory or a stopped slice.

### Necessity from the complete signed tested balance

Suppose an admissible test for one \(k\ge k_0\) satisfies (4).
C467b's balance, with all terms retained, gives its Lipschitz
representative \(\widetilde a_k\), the exact initial value
\[
 \widetilde a_k(0)=i\int_I\eta_{0,k}(u)\Delta(u)^2e^{-H(iu)}\,du,
\]
and for \(0\le s\le t\le T_0\),
\[
 \operatorname{Re}[-i\widetilde a_k(t)]
 -\operatorname{Re}[-i\widetilde a_k(s)]
 =\int_s^t\operatorname{Re}\left[-i\int_I
  \{(\eta_k)_rA+\eta_k G-(\eta_k)_1B_{23}
                    +(\eta_k)_2B_{13}-(\eta_k)_3B_{12}\}\,du\right]dr.
                                                               \tag{20}
\]
The tested coefficient bounds, finite cube and bounded derivatives
justify these integrals. The ambient term is zero by the actual-image
argument above; the three signed mixed terms are retained in (20)
and in hypothesis (4), not discarded or bounded by an unsigned identity.
Equation (4) makes the real representative nondecreasing, hence at
least \(M_k\) at every time.

For this test there is a null set \(N_k\subset(0,T_0)\) outside which
the representative agrees with its raw tested integral. For every such
time, real \(0\le\eta_k\le1\) and (12) give
\[
 M_k\le\operatorname{Re}[-i\widetilde a_k(t)]
       =\int_I\eta_k(t,u)\rho(t,u)\,du\le C(t).        \tag{21}
\]
The interval \((T_0/2,T_0)\) has positive measure, so it contains a
time outside \(N_k\). At that time, (18),(19),(21) contradict
\(47/50>23/25\). Thus no test exists for this k. The proof is
individual for every k and needs no simultaneous choice of tests.
If a countable family is postulated, a common full-measure set is
legitimate only after replacing the individual exceptional sets by
their countable union. No claim is made for an uncountable test class.
No raw identification at \(T_0\) or restart at a collision occurs.

### Exact arithmetic evidence and limitations

Reproduce the finite rational checks with
```
python3 scripts/adjoint-flux/chart-exhaustion-deficit-1009.py
```
The full certificate is
`scripts/adjoint-flux/chart-exhaustion-deficit-1009.json`.
It checks (7)–(10), the exact integer comparison in (15), the bump,
phase and boundary factors, the initial threshold and the capacity
threshold. It contains no sampled trajectory and cannot verify the
analytic exterior-volume theorem or the representative argument.

This obstruction uses a full-mass upper bound, not the failure of an
ansatz or rejection of a reserve box. It does not turn an unsigned
current into positivity: the needed sign is exactly C466's audited
full coefficient. The cap is essential in (21), and the prescribed
initial family is essential in (18). Changed caps, time horizons or
interface currents require their own analysis. Stops961/968/979/1000
remain intact within their original scopes. The global signed
assembly and actual-Xi all-degree gaps remain unresolved.

### Independent conceptual audit — 15 November 2026, step1011

The invocation-start EXPLORE assessment nomination1009, separately
approved1010, covers this exact audit. Reuse the primary versions,
theorem statements and essential proof cases recorded there and cited
above. C466/audit993, C466y/audit983, C467b/audit1002 and
C467c/audit1006 are used within their stated scopes; C466z/audit988
and C467a/audit997 supply their inherited branch, buffer and initial
trace. No new source theorem, density realization or RH premise is
introduced. This audit reproduces the written local obstruction; it
does not assert a discovery beyond the assessed sources.

**Actual background and confinement.** The normalized actual branch
has real H_0 and g(0)=0. C466(7) bounds the holomorphic derivative on
the entire convex disk by 198/5<40. Integrating along radial segments
therefore bounds |g(z)| by 40|z|, and separability makes the complex
Hessian diagonal with operator norm at most 40. Conjugation preserves
this norm on the real six-dimensional space: no factor two or three
belongs in that operator bound. The three appears only in its trace
on a real three-frame. Every pair contributes -4 to the derivative
of the full squared norm, giving -12 in (7)'s preceding identity.
At the largest initial squared norm, the upper derivative is
-12+80(3/256)=-177/16<0. The scalar differential inequality, or its
first-crossing comparison at the initial value, proves the claimed
nonincrease throughout every surviving interval. It neither extends
a trajectory at its first lifetime nor drops a singular force.

The exact pair-distance sum is 3||X||^2-|sum X_j|^2. Its upper bound
9/256 and Cauchy–Schwarz for the three positive squared distances
give P>=256, including all spacing ratios. Thus ||h||^2<=75/4.
All these estimates hold on each compact interval before the original
lifetime, with constants independent of its minimum pair distance.

**Complete weighted volume.** In C466y's real variational equation,
both factors in the complex product are conjugated. The resulting
real matrix is symmetric. Each pair has one positive eigenvalue
4/|X_i-X_j|^2, its negative, and four zeros; its trace on any fixed
orthonormal real three-frame is at most that positive eigenvalue.
Adding on the same frame before maximizing gives 4P+120 without
commuting pair matrices. The collective complex-triangle inequality
supplied by C466y is ||f_0||^2>=8P; its area remainder is nonnegative
also at collinear triples. Young's inequality with epsilon=1/4 gives
||f_0+h||^2>=(3/4)||f_0||^2-3||h||^2. Subtraction therefore leaves
-2P+120+225/4<=-1343/4<-335. The negative singular term has not
been removed in passing to a global constant.

WKM Proposition5 applies to the continuous real matrix on each such
compact interval, in exterior degree three and dimension six. It
requires neither endpoint boundedness nor a negative measure for its
general growth inequality. Its fundamental matrix transports all
three full parameter columns, initially ie_j with real volume one.
Multiplication by the exact scalar weight law proves (11). For
clarity, the inherited determinant comparison needs no Lagrangian
assumption: real Gram–Schmidt writes the columns as E Q with real
orthonormal columns E and real triangular Q; complex Hadamard bounds
|det E| by one, and the real volume is |det Q|. The dependent case
has both sides zero. Thus no complex-to-real norm constant is missing.

The buffer places every image where chi=1 and its real differential
is zero. Consequently all four terms of G vanish individually. The
actual cone applies to precisely F det J: since det(J/i)=i det J,
C466's definition gives -iA=e^{-H_0}Delta(u)^2 K on survivors.
It supplies the positive sign needed in (12), not just an unsigned
norm estimate. Zero extension then preserves 0<=rho<=e^{-335t}|F(iu)|
pointwise on the full parameter cube. Borel measurability follows
from the open survivor domain and its smooth coefficients. No
regularity of the lifetime is needed for integration at a fixed time.

**Initial mass, all parameters and the effective index.** The
initial phase bound uses real H_0 and |H(iu)-H_0|<=15/64. The two
initial orientation factors are det(iI)=-i and Delta(iu)^2=-Delta(u)^2,
so the signed initial density is exactly the positive expression in
(13). Its modulus bounds show 0<W<infinity: Delta^2 is integrable
and positive on an open set. They dominate both all surviving mass
and the bounded initial bumps, including their diagonal extensions.
DCT in (14) is legitimate but is not the source of the effective k.

For every k>=10^6, the inner-cube coordinate ratio is at most
999000/999999=1000/1001, strictly below one. Its denominator margin
is 2001/1002001>1/1000. Summing the three bump exponents thus gives
at most 3/1000, and e^{-x}>=1-x gives the floor 997/1000. The
Vandermonde square has degree six and the volume element degree
three, so the inner-cube mass scales by lambda^9. This accounts for
the entire excluded boundary region, with no spacing restriction.
The ratio of its upper modulus bound to W's lower modulus bound is
at most e^{2c}(1-lambda^9), strictly below 18/1000. The exponential
series comparison is valid because 2c=15/32<1; the cosine bound
uses 1-c^2/2=7967/8192>97/100. Outside the inner cube the initial
signed integrand remains nonnegative. Combining these facts proves
(18), not merely its limiting version. For the later interval,
e^x>=1+x gives precisely 768/835<23/25 in (19).

**Complete balance and the contradiction.** C467b's balance is
proved for every test with the stated regularity and common compact
support; its proof does not depend on the particular smaller bump
used in its separate pointwise obstruction. The new eta_{0,k} is
smooth across its support boundary and compactly supported in I
for each finite k. Constants may depend on k. The bounded Borel
coefficient majorants and bounded test derivatives ensure absolute
integrability of every term in (20). The weak identity has exactly
the mixed signs minus, plus, minus and the plus eta G term displayed
there. Thus the scalar representative has the asserted bounded weak
derivative. Its initial value follows from C467a's fixed-test DCT
limit and the O(t)||eta_t||_infinity bound for changing the test.
It is not inferred by assigning a flow on an initial diagonal.

Assumption (4) makes the real Lipschitz representative nondecreasing
by the fundamental theorem for absolutely continuous functions.
For this individual test its raw integral agrees almost everywhere;
the real cap and the nonnegative actual rho give (21) on that set.
The interval (T_0/2,T_0) has length 1/3840, so removing a null set
cannot remove every comparison time. At any remaining time (18)
and (19) contradict (21), with the stated threshold gap W/50>0.
No raw slice at T_0, uniform exceptional set for an uncountable test
class, boundary trace or stopped-map derivative enters this argument.

**Arithmetic and verdict.** Read the entire rational-check program,
inspected all 23 saved actual/relation/required entries, matched them
to (7)–(10) and (15)–(19), and reran the reproduction command above.
All 23 pass, with no failures. The computed initial floor is
47484119/50000000>47/50; the capacity ceiling is 768/835<23/25.
Their exact difference is 249847873/8350000000>0. These checks
verify arithmetic only; the analytic justification is the audit above.
The written exclusion passes without a mathematical correction or
additional direct input. Its DAG row remains unchanged. C467c's
attenuated fixed-bump payment and stops961/968/979/1000 remain valid
in their own scopes. Neither other currents or caps nor global
assembly, all-degree signs or actual-Xi transfer have been settled.

## Mathlib

Full matching coverage for this actual stopped-flow mass obstruction
has not been checked; no absence claim is made. C466y and C467b retain
their qualifications for the supporting exterior-power, ODE,
integration and Sobolev-representative inputs. The rational certificate
is not a Lean proof or a formal verification of those inputs.
