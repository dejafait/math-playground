# C467c — Actual-h capped integrated adjoint payment

## Hypotheses

Use precisely C467b's actual logarithm and first-lifetime current:
\[
 h(w)=\xi(1/2+\sqrt w)/\xi(1/2),\quad e^{B(w)}=h(w),
 \quad B(1)=\log h(1)\in\mathbb R,\quad x=B'(1),
\]
\[
 g(z)=B'(1+z)-x,\quad
 H(z)=\sum_{j=1}^3\{B(1+z_j)-x(1+z_j)\},\quad
 H_0=3(B(1)-x),
\]
on \(|w-1|<1/4\). Set
\[
 R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad I=(-a,a)^3,
 \quad \Delta(z)=\prod_{i<j}(z_j-z_i),\quad F=\Delta^2e^{-H}.
\]
For distinct real parameters let
\[
 \dot X_j=-2\sum_{k\ne j}\frac{X_j-X_k}{|X_j-X_k|^2}
                     +\overline{g(X_j)},\qquad X(0,u)=iu
                                                        \tag{1}
\]
on its original first maximal lifetime in
\(\{|z_j|<R\}\setminus\{\Delta=0\}\), without restart.
Retain all external density qualifications in C466z; no density
realization or RH assumption is used here.

The ambient smooth compact cutoff \(\chi\) equals one near the closed
ball of radius \((\sqrt3+1)/16\). On survivors let
\[
 J_j=\partial_{u_j}X,\quad V=\dot X,\quad
 A=\chi F\det[J_1,J_2,J_3],\qquad
 B_{ij}=\chi F\det[V,J_i,J_j],
\]
\[
 G=F\{d\chi(V)\det[J_1,J_2,J_3]
       -d\chi(J_1)\det[V,J_2,J_3]
       +d\chi(J_2)\det[V,J_1,J_3]
       -d\chi(J_3)\det[V,J_1,J_2]\}.                  \tag{2}
\]
Here the functions and the real differential \(d\chi\) are evaluated
at \(X(t,u)\). All these coefficients are extended by zero off the original survivor
domain, as in C466y and C467b. No derivative of a stopped map is used.
The prescribed datum is exactly
\[
 \eta_0(u)=\prod_{j=1}^3 b(32u_j),\qquad
 b(s)=\begin{cases}e^{-1/(1-s^2)},&|s|<1,\\0,&|s|\ge1.\end{cases}
                                                        \tag{3}
\]

## Conclusion

There exists a real test \(\eta\), smooth in space and \(C^1\) in time
on \([0,T_0]\times I\), with continuous bounded first derivatives,
one compact spatial support strictly inside \(I\), and
\[
 0\le\eta\le1,\qquad \eta(0,u)=\eta_0(u),
\]
such that, for almost every \(t\in(0,T_0)\),
\[
 \operatorname{Re}\left[-i\int_I
 \{\eta_tA+\eta G-\eta_1B_{23}+\eta_2B_{13}-\eta_3B_{12}\}\,du
                    \right]\ge0.                       \tag{4}
\]
The Lipschitz tested representative therefore stays at least its
strictly positive initial value. In fact it becomes the constant
\(2\cdot10^{-16}e^{-H_0}\) after a sufficiently short positive time.
This statement concerns the representative at \(T_0\); it makes no
general identification of a raw stopped slice there.

The construction uses a compact reserve whose tested real mass is
\(>4\cdot10^{-16}e^{-H_0}\) throughout the interval, whereas the
initial mass is \(<8\cdot10^{-17}e^{-H_0}\). Its rational certificate
checks 25,600 time tubes in 100 initial boxes. Another 164 boxes are
uncertified and contribute nothing. Independent conceptual audit1006 below
validates the argument and replays the saved certificate without changing
the hypotheses or constants. This is the local result of the
ready1003-approved attempt1004, not a claim of certified originality,
global signed assembly, all-degree positivity, Xi transfer or an RH
candidate. C467b's pointwise obstruction remains valid.

## Proof

### Established tools and what must still be proved

Reuse C466/audit993's actual \(|g'|<40\), \(g(0)=0\), pair-secant
cone, and full matrix factorization
\[
 J=(Z+iI_3)Q,\quad Z=Z^T\in M_3(\mathbb R),\quad
 \|Z\|\le\tan(40t)<1/47,\quad \det Q>0.                \tag{5}
\]
Every actual pair has the same bound on its real-to-imaginary slope.
The full coefficient has phase
\[
 \operatorname{Re}(-iA)\ge\cos(19/64)|A|>0
                                                        \tag{6}
\]
on survivors. C466z/audit988 gives the strict buffer. C466y/audit983
supplies smoothness on the survivor domain and bounded complete
coefficient extensions. C467a/audit997 and C467b/audit1002 supply,
respectively, the fixed-test Lipschitz representative and the complete
time-dependent tested balance, including the actual initial limit.
These inputs do not themselves provide a reserve mass bound or (4).

For smooth dependence and compact continuation use the already assessed
G. Teschl, *Ordinary Differential Equations and Dynamical Systems*,
April 2012 author preliminary version,
[Lemma 2.14/Corollary 2.15, pp.52–53, and Theorem 6.1 with proof, pp.189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
Only compact subsets separated from the original divisor are used.
No new transport, optimization, boundary-trace or lifetime theorem is
imported. Review1003 found that static capped optimization and
density-constrained transport do not give this fixed-current smooth
test. The needed differences are the following actual-flow reserve
estimate and the smooth transfer. Neither is claimed as a reproof of
those comparison theorems.

### Quantitative survival on finite parameter boxes

Label one chamber by \(u_1<u_2<u_3\). Write \(X_j=p_j+iq_j\) and
\[
 r=(q_3-q_1)/2,\quad v=(q_3-2q_2+q_1)/2,\quad
 q_2-q_1=r-v,\quad q_3-q_2=r+v,\quad R_q=r^2.
\]
The ordering persists on survivors by (5), so \(r>|v|\). Put
\(h=1/2209\). For every pair, the singular imaginary velocity has
factor
\[
 \lambda_{ij}=\frac{(q_j-q_i)^2}{|X_j-X_i|^2}
                 \in[1/(1+h),1].                      \tag{7}
\]
For the background imaginary force \(f_j=-\operatorname{Im}g(X_j)\),
the convex disk, \(|g'|<40\), and the secant cone imply
\[
 |f_j-f_i|\le40\sqrt{1+h}|q_j-q_i|<41|q_j-q_i|.        \tag{8}
\]
This retains the actual background, including its real-coordinate
dependence; it does not replace it by a scalar linear force.

Subtracting the three equations (1) gives the singular terms
\[
 r'_{\rm sing}=-\frac{\lambda_{12}}{r-v}
               -\frac{\lambda_{23}}{r+v}
               -\frac{\lambda_{13}}r,
\qquad
 v'_{\rm sing}=3\left(\frac{\lambda_{12}}{r-v}
                         -\frac{\lambda_{23}}{r+v}\right).
\]
The background contributions have moduli at most \(41r\) in each
equation. Consequently, before the first lifetime,
\[
 R_q'\ge-\frac{4R_q}{R_q-v^2}-2-82R_q,\qquad
 R_q'\le-\frac6{1+h}+82R_q,                            \tag{9}
\]
\[
 D^+|v|\le\frac{6(|v|+h\sqrt{R_q})}{R_q-v^2}
                               +41\sqrt{R_q}.          \tag{10}
\]
For (10), separate \(\lambda_{ij}=1+(\lambda_{ij}-1)\): the main
term is \(6v/(R_q-v^2)\), and the two errors sum to at most
\(6hr/(R_q-v^2)\). The upper right derivative covers \(v=0\).
Because \(6/(1+h)-82a^2>567/100\), first crossing at \(R_q=a^2\)
and (9) show
\[
 R_q(t)\le r(0)^2-(567/100)t.                           \tag{11}
\]

Here is the full meaning of the rational certificate's tubes. Initial
coordinates are
\[
 u=(m-r_0+v_0/3,\ m-2v_0/3,\ m+r_0+v_0/3),            \tag{12}
\]
whose real Jacobian has absolute determinant 2. The grid consists of
\[
 r_0\in[r_-,r_+]=[(580+2i)/10000,(582+2i)/10000],\quad 0\le i<22,
\]
\[
 |v_0|\in[v_-,v_+]=[j/10000,(j+1)/10000],\quad 0\le j<12,
\quad |m|\le m_*:=a-r_+-v_+/3-10^{-6}.                 \tag{13}
\]
Use both signs of \(v_0\) and all six coordinate permutations.
The script retains only certified boxes with \(m_*>0\). The grid
interiors are disjoint; overlaps on their boundaries have measure zero.
Every closed box lies strictly in \(I\), and its initial gaps are
positive. Its total volume, with signs and permutations, is
\[
                       48m_*(r_+-r_-)(v_+-v_-).         \tag{14}
\]

Divide time into 256 intervals of length \(d=T_0/256\). At a left
endpoint suppose \(R_q\ge L\), \(|v|\le W\). Set
\(H_j=r_+^2-(567/100)jd\), an upper bound throughout that interval.
Each accepted row supplies rational \(\ell<L\), \(w>W\), with
\(\ell>w^2\). Let \(s_+\) be a rational upper bound for
\(\sqrt{H_j}\), and \(s_-\) a rational lower bound for \(\sqrt\ell\).
Define
\[
 D=4\ell/(\ell-w^2)+2+82H_j,\qquad
 E=6(w+hs_+)/(\ell-w^2)+41s_+,
\]
\[
 P_*=2/(s_--w)^2+1/(4\ell).                            \tag{15}
\]
The saved row is accepted only when
\[
 Dd<L-\ell,\quad Ed<w-W,\quad s_->w,
\]
\[
 \ell\le L_{\rm next}\le L-Dd,\qquad
 W+Ed\le W_{\rm next}\le w.                            \tag{16}
\]
While \(R_q\ge\ell\), \(|v|\le w\), equations (9)–(11) bound
\(-R_q'\) by \(D\) and \(D^+|v|\) by \(E\). For example,
\(R_q/(R_q-v^2)\le\ell/(\ell-w^2)\), and the remaining \(82R_q\)
term is bounded by \(82H_j\). Strict inequalities (16) exclude a
first exit from the tube. Integration then gives its endpoint bounds.
Initialization uses \(L\le r_-^2\) and \(W\ge v_+\). This proves
the entire finite induction, rather than merely sampling times.

Every accepted tube has a positive imaginary gap. Its finitely many
lower bounds and C466z's strict buffer place the whole raw trajectory
in a compact nonsingular set through \(T_0\). A putative earlier first
lifetime would contradict the cited compact-continuation theorem.
The same theorem extends each such trajectory slightly past \(T_0\).
Smooth dependence and a finite cover of the closed parameter boxes
give an open neighborhood of their union on which all these original
raw solutions survive through \(T_0\). No regularity of the function
\(\tau(u)\), stopped-set inverse or collision extension is required.

### The full Jacobian retains enough mass

Write \(D^2S=\mathcal A+i\mathcal C\), as in C466, and
\(P_q=\sum_{i<j}(q_j-q_i)^{-2}\). Its actual factorization gives
\((\log\det Q)'=\operatorname{tr}(-\mathcal A-\mathcal C Z)\).
For a gap \(s+i\) times its imaginary length \(d_{ij}>0\), the
pair Hessian has coefficients
\[
 c_{ij}=\frac{2(1-s^2)}{d_{ij}^2(1+s^2)^2},\qquad
 d^{\rm Hess}_{ij}=\frac{-4s}{d_{ij}^2(1+s^2)^2}
\]
against \(-\mathcal A\) and \(\mathcal C\), respectively. For
\(E_{ij}=(e_i-e_j)(e_i-e_j)^T\), one has
\(\operatorname{tr}E_{ij}=2\) and
\(|\operatorname{tr}(E_{ij}Z)|\le2/47\). Each pair therefore contributes
at least
\[
 \frac{4(1-3h)}{d_{ij}^2(1+h)^2}
                         \ge\frac{4(1-5h)}{d_{ij}^2}.   \tag{17}
\]
The last inequality follows on multiplying by \((1+h)^2\); the
difference is \(9h^2+5h^3\). The background trace costs at most
\(120(1+1/47)\). Thus
\[
 (\log\det Q)'\ge4(1-5h)P_q-120(1+1/47).              \tag{18}
\]

Let \(\Delta_q=\prod_{i<j}(q_j-q_i)>0\) and
\(l_j=\sum_{k\ne j}(q_j-q_k)^{-1}\). Direct expansion gives
\(\sum l_j^2=2P_q\): the three cross products sum to zero after
multiplication by the three distinct pair gaps. The singular imaginary
velocity is \(-2l+e\), where
\[
 \|e\|_2\le2\sqrt2h\sum_{i<j}|q_j-q_i|^{-1}
                         \le2\sqrt6h\sqrt{P_q}.
\]
Hence its contribution to \((\log\Delta_q)'=\sum l_jq_j'\) differs
from \(-4P_q\) by at most \(4\sqrt3hP_q<7hP_q\). By (8) the
background contribution is a sum of three divided differences, each
of modulus at most 41. Combining with (18), and using
\(120(48/47)+123<246\), proves
\[
       (\log(\det Q\,\Delta_q))'\ge-27hP_q-246.         \tag{19}
\]
This calculation retains the full matrix \(Z\); it is not a product
of independent pair Jacobians or a modulus substitution for (4).

The tube (15) bounds \(P_q\le P_*\). Starting with \(\Lambda_0=0\),
the certificate also checks
\[
 \Lambda_{j+1}\ge\Lambda_j+(27hP_*+246)d.               \tag{20}
\]
Since \(Q(0)=I\), integration of (19) gives, uniformly throughout
an accepted box and \(0\le t\le T_0\),
\[
 \det Q(t)\ge\frac{\Delta(u)}{\Delta_q(t)}e^{-\Lambda_{256}}.
                                                        \tag{21}
\]
The ordered \(\Delta(u)\) here is positive. The estimate extends to
the endpoints by smoothness on this strictly surviving neighborhood.

Grouping the singular forces in (1) gives
\[
 (\|X\|^2)'=-12+2\operatorname{Re}\sum_j\overline{X_j}\,
                                      \overline{g(X_j)}
             \le-12+80\|X\|^2.
\]
Since initially \(\|u\|^2<3a^2\) and \(80\cdot3a^2<12\), a first
crossing proves \(\|X\|\le\|u\|\). Taylor's formula along the radial
segments in the original convex disk, using \(g(0)=0\), gives
\[
 |H(X)-H_0|\le20\|X\|^2\le15/64.                      \tag{22}
\]
Further, \(|\Delta(X)|\ge\Delta_q\), and (5) implies
\(|\det J|=\det Q\prod_{j=1}^3\sqrt{1+\lambda_j(Z)^2}\ge\det Q\).
Together (6), (21) and (22) give the lower bound for the *actual*
real density \(\rho=\operatorname{Re}(-iA)\):
\[
 \rho(t,u)\ge e^{-H_0}\cos(19/64)e^{-15/64-\Lambda_{256}}
                                  \Delta(u)\Delta_q(t). \tag{23}
\]
The final recorded \(L_*,W_*\) are respectively no larger and no
smaller than the bounds at any earlier time. Thus
\[
 \Delta(u)\ge2r_-(r_-^2-v_+^2),\qquad
 \Delta_q(t)\ge2\sqrt{L_*}(L_*-W_*^2).                 \tag{24}
\]
All estimates are unchanged by simultaneous coordinate permutations.

### Exact evidence and the initial mass

The complete certificate and its generator/verifier are
`scripts/adjoint-flux/integrated-reserve-certificate-1004.json` and
`scripts/adjoint-flux/integrated-reserve-certificate-1004.py`.
Reproduce with
```
python3 scripts/adjoint-flux/integrated-reserve-certificate-1004.py
```
All tube endpoints are rounded outward on the rational grid \(2^{-64}\).
Square-root bounds use integer square roots and are checked by the
integer-square construction. Each saved tube is replayed using exact
`Fraction` arithmetic for (15), (16), (20), its positive gap, and its
endpoint density. The replay also checks disjointness of the original
grid interiors and the volume factors. It uses
\[
 \cos(19/64)\ge1-(19/64)^2/2,\qquad
 e^{-z}\ge\sum_{k=0}^{9}(-z)^k/k!\quad(z\ge0),          \tag{25}
\]
the latter by the positive order-ten Taylor remainder. A box whose
polynomial lower factor is nonpositive is not accepted. Density lower
bounds are rounded down to multiples of \(10^{-40}\).

Summing (23)–(25) times (14) over the 100 accepted boxes yields
\[
 \int_C\rho(t,u)\,du\ge e^{-H_0}\mathcal R,
 \quad
 \mathcal R=\frac{12701285019439211927675528954987981661}
 {31250000000000000000000000000000000000000000000000000}
                  >4\cdot10^{-16},                    \tag{26}
\]
where \(C\) is their union including signs and permutations. All 25,600
accepted time tubes pass the exact replay. The 164 rejected boxes and
their failure locations remain in the certificate, with zero contribution.
A preceding floating diagnostic is retained separately as
`scripts/adjoint-flux/integrated-reserve-diagnostic-1004.py/.json`;
none of its approximations is a premise of (26).

For the prescribed initial mass, \(|H(iu)-H_0|\le15/256\) on the
support of (3). On \([0,1]\), the even bump \(b\) decreases. On
\([j/64,(j+1)/64]\) define the step envelope \(w\) to have height
\[
 w_j=10^{-12}\left\lceil
 \frac{10^{12}}{\sum_{k=0}^{24} x_j^k/k!}\right\rceil,
 \qquad x_j=\frac1{1-(j/64)^2}.                         \tag{27}
\]
The positive exponential series proves \(w_j\ge b(j/64)\), hence
\(w\ge b\) pointwise apart from irrelevant interval-end conventions.
Extend \(w\) evenly and let \(\mu_k=\int_{-1}^1s^kw(s)\,ds\).
Expanding the squared three-variable Vandermonde and integrating its
monomials gives exactly
\[
 \int_{[-1,1]^3}\Delta(s)^2\prod_jw(s_j)\,ds
                         =6(\mu_0\mu_2\mu_4-\mu_2^3).  \tag{28}
\]
For example, this is six times the determinant of the matrix with
rows \((\mu_0,0,\mu_2),(0,\mu_2,0),(\mu_2,0,\mu_4)\);
it follows directly from the two finite determinant expansions, with
no limit interchange. The exact step integrals are in the certificate.
Using \(e^{15/256}\le256/241\), nonnegativity of \(\Delta^2\), and
the change of scale \(u=(a/2)s\), one obtains
\[
 0<M_0\le e^{-H_0}\mathcal U,
\quad
 \mathcal U=\frac{256}{241}(a/2)^9
                    6(\mu_0\mu_2\mu_4-\mu_2^3)
                       <8\cdot10^{-17}.                \tag{29}
\]
Strict positivity is C467b(6). Exact replay regenerates all 64 upper
heights using positive rational sums and all three rational moments;
it verifies both strict comparisons (26), (29). The full selected
certificate summary gives \(\mathcal R\approx4.06441120622\cdot10^{-16}\),
\(\mathcal U\approx7.72298554433\cdot10^{-17}\), with
\(\mathcal R/\mathcal U>5.2627\). These decimals only display the exact
comparisons; they are not the evidence for them.

### Smooth capped transfer and the complete signed inequality

The finite compact union \(C\) lies in an open relatively compact
parameter neighborhood whose original raw trajectories all survive
through \(T_0\), as proved above. Choose a smooth \(\psi\), with
\(0\le\psi\le1\), equal to one near \(C\) and compactly supported
in that neighborhood. One explicit construction uses finitely many
smaller balls covering \(C\), smooth cutoffs \(\psi_j\) equal to one
on them and supported in larger balls in the neighborhood, and
\(\psi=1-\prod_j(1-\psi_j)\). The usual cutoffs are obtained from
\(e^{-1/s}\) for \(s>0\), extended by zero, so no nonsmooth optimizer
or new selection theorem is required.

The actual function
\[
                   G_\psi(t)=\int_I\psi(u)\rho(t,u)\,du
\]
is smooth on an interval containing \([0,T_0]\): the integrand and
all needed derivatives are smooth on this compact surviving support.
The nonnegative density (6), (26), and endpoint continuity imply
\[
                    G_\psi(t)>4\cdot10^{-16}e^{-H_0}.   \tag{30}
\]
This special surviving-support statement does not assert continuity
of arbitrary zero-extended raw slices. Its fixed-test representative
agrees with this smooth integral, because they agree almost everywhere
and both are continuous.

Set
\[
 c=2\cdot10^{-16}e^{-H_0},\quad
 U=8\cdot10^{-17}e^{-H_0},\quad \delta=c-U>0,
 \qquad \Phi(t,u)=c\psi(u)/G_\psi(t).                  \tag{31}
\]
Then \(0\le\Phi<1/2\), it has common compact support, and its
tested mass is identically \(c\). Let \(f(t)\) be the real Lipschitz
representative for the fixed test \(\eta_0\) from C467a, so
\(f(0)=M_0<U\). Choose any finite Lipschitz bound \(L\ge1\) for it
(C467a(6) supplies one), and put
\[
 \varepsilon=\min\{T_0/2,\delta/(2L)\}>0,\qquad
 \theta(t)=\begin{cases}
 1-\exp[-t/(\varepsilon-t)],&0\le t<\varepsilon,\\
 1,&\varepsilon\le t\le T_0.
 \end{cases}                                           \tag{32}
\]
The function \(1-\theta\) and all its derivatives tend to zero at
\(\varepsilon\), so \(\theta\) is smooth on the closed time interval
in the one-sided endpoint sense. It is increasing, \(\theta(0)=0\),
and
\[
 \theta'(t)=\frac{\varepsilon}{(\varepsilon-t)^2}(1-\theta(t))
                    \ge\frac{1-\theta(t)}\varepsilon
                       \quad(0\le t<\varepsilon).      \tag{33}
\]
Define the required test by
\[
                  \eta(t,u)=(1-\theta(t))\eta_0(u)
                                      +\theta(t)\Phi(t,u). \tag{34}
\]
This is a convex combination of functions in \([0,1]\), with exactly
the initial datum (3). Its support is contained in the fixed compact
union of the two supports, strictly inside \(I\). Smoothness of
\(\Phi\), positivity (30), and (32) give the asserted joint regularity
and bounded first derivatives. No time derivative of \(f\) enters
the test itself.

By the complete C467b(5) balance, the real tested representative for
(34) is
\[
                        m_\eta(t)=(1-\theta(t))f(t)+\theta(t)c. \tag{35}
\]
Indeed this equality first holds for raw slices almost everywhere
for this test and the fixed test \(\eta_0\); uniqueness and continuity
of their representatives extend it to both endpoints. Only finitely
many tests are involved, so no common exceptional set for all tests
is being assumed. On \([0,\varepsilon]\),
\[
 f(t)\le M_0+L\varepsilon<U+\delta/2=c-\delta/2.
\]
For almost every \(t<\varepsilon\), (33) therefore gives
\[
 m_\eta'(t)=(1-\theta)f'+\theta'(c-f)
       \ge(1-\theta)\{-L+\delta/(2\varepsilon)\}\ge0.  \tag{36}
\]
After \(\varepsilon\), the representative equals \(c\).

Finally C467b's buffer argument makes \(\chi(X)=1\) and
\(d\chi_X=0\) on every survivor. Each of the four terms in the full
\(G\) of (2) vanishes, as does its zero extension. Apply C467b(5)
to (34), retaining its \(\eta_t A\), \(\eta G\), and all three mixed
flux terms with their stated signs. Its derivative is exactly the
left side of (4). Equation (36) proves (4), including the full signed
flux, without any pointwise payment assertion or absolute-value
replacement. The cap is paid by the strict reserve comparison, not
by unrestricted amplification.

The argument is local to this one chart and this fixed three-particle
time interval. It supplies neither signs or payment on other charts
nor their global assembly or the actual-Xi all-degree conclusion.

### Independent conceptual audit — 15 November 2026, step1006

This audit uses the unchanged invocation-start EXPLORE assessment
nomination1004/completed review1005. Reuse the inspected source coverage
in reviews1001/1003/1005, including the precise Teschl cases cited above,
and the audited input qualifications in C466, C466y, C466z, C467a and
C467b. The audit is reproduction of this written construction, not a
new theorem, a new literature discovery or certified originality.
Stops961/968/979/1000 retain their recorded scopes. In particular the
integrated inequality does not assert the pointwise condition of C467b.

**Signs and all-time gap barriers.** In an ordered chamber the singular
imaginary velocities are
\[
 2\left(\frac{\lambda_{12}}{r-v}+\frac{\lambda_{13}}{2r}\right),
 \quad 2\left(-\frac{\lambda_{12}}{r-v}
                    +\frac{\lambda_{23}}{r+v}\right),
 \quad-2\left(\frac{\lambda_{23}}{r+v}
                    +\frac{\lambda_{13}}{2r}\right).
\]
Their half-difference and half-second-difference give exactly the two
equations preceding (9). The background errors are bounded by
\(41r\): for the second difference use the sum of the two adjacent
absolute differences divided by two. The secant bound used here is
uniform: \(\tan(1/48)\le(1/48)/(1-1/(2\cdot48^2))<1/47\).
The sine upper and cosine lower Taylor bounds justify this inequality
without a floating trigonometric estimate.

For (9)'s upper bound use
\(4R_q/(R_q-v^2)+2\ge6\); the lower bound uses
\(\lambda_{ij}\le1\). At \(R_q=a^2\) the upper derivative is
strictly negative, so no first upward crossing occurs. The stated
\(567/100\) inequality then gives (11) throughout every survivor
interval. For (10), the adjacent reciprocal errors have sum bounded
by \(6hr/(R_q-v^2)\), while the main term is
\(6v/(R_q-v^2)\). The upper Dini derivative of \(|v|\) also covers
its zeros.

On a tube, \(R/(R-v^2)\) decreases with \(R\) and increases with
\(|v|\), so its maximum is at \((\ell,w)\). The other factors in
(15) have the claimed directions, with \(R_q\le H_j\). At a first
lower-radius or upper-shape contact, integration of the respective
differential inequality contradicts the strict margin in (16).
Continuity and the upper-Dini comparison justify the same argument
when \(v\) changes sign. Induction therefore covers each entire time
interval, not just its endpoints. The accepted endpoint radius bounds
decrease and shape bounds increase, which justifies (24) at every
earlier time as well.

The replay finds a common adjacent-imaginary-gap lower bound over
every accepted tube of
\[
 d_* = \frac{84594088907682161}{18446744073709551616}>0.
\]
Every earlier raw trajectory from the closed accepted boxes thus lies
in the closed set \(\|z\|\le r_*<R\),
\(|z_i-z_j|\ge d_*\). This is a compact subset of the original open
nonsingular domain. If a first lifetime were at or before \(T_0\),
the tube bounds up to that lifetime and this compact set would satisfy
Teschl's compact-continuation hypotheses and contradict maximality.
Consequently each trajectory exists beyond \(T_0\); no continuation
across a divisor has been used. Smooth dependence on the open flow
domain and compactness of the initial boxes give a common open
surviving parameter neighborhood. Shrink it within \(I\), away from
initial diagonals, before choosing the reserve support. Compactness
also gives a common small time extension for any compact subset of
that neighborhood. This checks the continuation required for the
smooth integral, without assuming regularity of \(\tau\).

**Full matrix mass and volume.** The actual factorization is
\(J=(Z+iI)Q\), with \(Q'=(-\mathcal A-\mathcal C Z)Q\).
For a pair, the contribution to its logarithmic determinant is
\(2c_{ij}-d^{\rm Hess}_{ij}\operatorname{tr}(E_{ij}Z)\), hence at
least \(4(1-3h)/(d_{ij}^2(1+h)^2)\). This keeps the potentially
adverse full-matrix term. The background estimate follows from its
three diagonal entries and \(|Z_{jj}|\le1/47\). Thus (17)–(18)
have the correct signs and constants.

Writing the adjacent positive gaps as \(b_1,b_2\), the cross terms
in \(\sum l_j^2\) cancel because
\(1/[b_1(b_1+b_2)]-1/(b_1b_2)+1/[b_2(b_1+b_2)]=0\).
This proves \(\|l\|^2=2P_q\). The error vector estimate gives
\(|l\cdot e|\le4\sqrt3hP_q<7hP_q\); the three background divided
differences contribute at worst \(-123\). Together with (18) this
gives \(-27hP_q-246\), exactly the loss in (19)–(20). The bound
on \(P_q\) uses both adjacent gaps \(\ge\sqrt\ell-w\) and the
outer gap \(2r\ge2\sqrt\ell\). Since \(Q(0)=I\), integration
starts with \(\Delta(u)\), as required by (21).

The squared-norm derivative groups each unordered pair to \(-4\),
giving \(-12\) for three pairs. The background bound follows from
\(|g(z)|\le40|z|\). First crossing at the initial squared norm
proves the norm contraction in (22). Radial Taylor integration then
bounds each background remainder by \(20|X_j|^2\). There is no
unstated scalar-force substitution. The inequalities
\(|\Delta(X)|\ge\Delta_q\), \(|\det J|\ge\det Q\), and the
audited phase cone now give (23) for the actual real density.

The real determinant of (12), in variables \((m,r_0,v_0)\), is
2. Its center interval has length \(2m_*\), there are two signs of
\(v_0\), and six ordered chambers; the total factor is therefore
48. Distinct grid interiors do not overlap; chamber and sign
intersections are measure-zero boundaries. Under simultaneous
permutation of initial and final coordinates, \(J\) is conjugated
by a permutation matrix and \(F\) is unchanged. Thus the density
has the same sign and bound in all six chambers. No orientation
factor is missing from the positive Lebesgue-volume calculation.

**Complete finite replay and initial comparison.** Read and execute
the existing verifier on the saved certificate; do not regenerate it:
```
python3 scripts/adjoint-flux/integrated-reserve-audit-1006.py
```
The full audit artifact is
`scripts/adjoint-flux/integrated-reserve-audit-1006.json`. It records
input hashes, the exact replay summary and audit checks, with no
verification failures. All 25,600 accepted rows are checked, along
with all 64 bump-envelope heights and all three exact moments. The
wrapper also checks every recorded constant, the precise 264-box
grid and center margin, square-root enclosures by rational squares,
strict tube-exit margins and monotone endpoint bounds. The original
certificate remains byte-for-byte unchanged. The 164 omitted boxes
comprise 150 uncertified positive-gap tubes and 14 nonpositive center
intervals; none contributes mass. Their rejection is not evidence
of actual collision.

The odd degree-nine Taylor polynomial is a lower bound for
\(e^{-z}\), since its order-ten remainder is positive for \(z\ge0\).
Its positivity on each accepted box and the cosine lower bound
justify the saved rounded density. Replay reproduces exactly the
rational \(\mathcal R\) in (26), not merely its decimal preview.
At time zero, \(-iA(0,u)=\Delta(u)^2e^{-H(iu)}\). On the initial
bump support, \(20\sum u_j^2\le15/256\). The positive partial
exponential sums in (27) give an upper envelope for the bump, and
the finite double determinant expansion gives (28) with its factor
six. Multiplying a nonnegative squared Vandermonde by the three
pointwise envelope bounds is legitimate. The scale contributes
\((a/2)^{6+3}\), and \(e^{15/256}\le(1-15/256)^{-1}\).
Consequently the regenerated \(\mathcal U\) is an actual upper
bound for \(M_0e^{H_0}\). The exact comparisons are
\[
 \mathcal R>4\cdot10^{-16}>2\cdot10^{-16}
       >8\cdot10^{-17}>\mathcal U>0.
\]
The displayed ratio \(>5.2627\) is descriptive; the rational
comparisons, not floating output, pay the cap.

**Smooth transfer and the full signed balance.** Choose the reserve
cutoff in a relatively compact subneighborhood with closure inside
the surviving neighborhood just established. It is one on \(C\)
and between zero and one elsewhere. The actual density is
nonnegative on the whole support. Hence contributions outside \(C\)
cannot reduce (26). Smooth dependence on a common extended compact
time interval bounds all needed derivatives of the integrand, so
differentiation under the integral makes \(G_\psi\) smooth, with
the strict lower bound (30) including both endpoints. There is no
claim about arbitrary stopped raw slices.

The fixed-test mass \(f\) is Lipschitz by C467a, with
\(|f'|\le L\) almost everywhere and \(f(0)=M_0<U\). The test
itself uses only smooth \(G_\psi\), fixed bumps and \(\theta\),
never a derivative of \(f\). The strict reserve gives
\(0\le\Phi<1/2\); (34) is therefore capped by one and has exactly
the initial datum, with common compact spatial support. Flatness
at \(\varepsilon\) proves the required joint regularity and
bounded first derivatives despite possibly very small
\(\varepsilon>0\). Equations (32)–(33) imply
\(c-f\ge\delta/2\) before \(\varepsilon\), so the almost-everywhere
derivative in (36) is nonnegative. After that time the mass is
exactly \(c\).

For (35), first use raw-slice linearity at times outside the union
of the exceptional null sets for the fixed and constructed tests.
Only finitely many tests occur. Both sides are continuous
representatives, so equality extends to the closed interval. The
imported C467b balance applies because the constructed test has
bounded first derivatives and one compact support. Its three mixed
signs remain \(-,+,-\), and all four terms of \(G\) vanish from
\(d\chi_X=0\) on the buffered image before zero extension.
Taking \(\operatorname{Re}(-i\,\cdot)\) identifies its weak
derivative with (4). This proves the claimed complete integrated
inequality and representative endpoints without a pointwise
inequality, a global real transport velocity or a terminal raw-slice
assumption.

No load-bearing error was found. Retain C467c with unchanged
hypotheses, constants and direct mathematical inputs. This validates
one local initial-cycle payment; global interfaces, other charts,
all-degree signs, external density realization and actual-Xi
transfer remain unresolved. It is not an RH candidate.

## Mathlib

Full matching coverage for this actual-current reserve and capped
integrated test has not been checked. C466, C467a and C467b record
supporting finite-dimensional and scalar-analysis coverage with their
qualifications. The rational Python certificate is not a Lean proof;
it verifies the finite arithmetic conditions. Audit1006 independently
checks the differential inequalities, continuation and representative
argument informally; it does not constitute a Lean formalization.
