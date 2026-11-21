# C467a — Actual-h tested time-zero trace and finite-time balance

## Hypotheses

Use exactly the actual chart of C466z: h(w)=xi(1/2+sqrt(w))/xi(1/2),
its normalized logarithm B on |w-1|<1/4, x=B'(1) real, and
\[
 H(z)=H_x(z)=\sum_{j=1}^3\{B(1+z_j)-x(1+z_j)\},\qquad
 H_0=3(B(1)-x)\in\mathbb R,
\]
\[
 \mathcal B=\{z\in\mathbb C^3:|z_j|<R\},\quad
 R=\tfrac14,\quad a=\tfrac1{16},\quad T_0=\tfrac1{1920},
 \quad M_1=120,\quad M_2=1000.
\]
Retain C466z's external density qualifications when interpreting this
chart as part of that imported density. No RH assumption is made.
Put I=(-a,a)^3, Q=(0,T_0) times I,
Delta(z)=product_(i<j)(z_j-z_i), F=Delta^2 exp(-H), and
Omega=F dz1 wedge dz2 wedge dz3. For distinct real u, use C466y's
unit-flat raw flow
\[
 \dot X=\overline{\nabla(-2\log\Delta+H)(X)},\qquad X(0,u)=iu
\]
on its first maximal lifetime [0,tau(u)) in
U=mathcal B minus {Delta=0}, without restart. Only logarithmic
derivatives are used. Let D={(t,u) in Q: Delta(u)!=0, t<tau(u)}.
The strict buffer is r_*=(sqrt3+1)/16<R, as proved in C466z.

Fix eta in C_c^infinity(I;C) and chi in C_c^infinity(mathcal B;C).
Real tests are included. On D put J_j=partial_(u_j)X and V=dot X.
The determinant below is the complex determinant of its three columns.
Define the complete coefficients
\[
 \begin{split}
 A&=\chi(X)F(X)\det[J_1,J_2,J_3],\\
 B_{12}&=\chi(X)F(X)\det[V,J_1,J_2],\\
 B_{13}&=\chi(X)F(X)\det[V,J_1,J_3],\\
 B_{23}&=\chi(X)F(X)\det[V,J_2,J_3],\\
 G&=F(X)\bigl\{d\chi_X(V)\det[J_1,J_2,J_3]
       -d\chi_X(J_1)\det[V,J_2,J_3]\\
  &\hspace{34mm}+d\chi_X(J_2)\det[V,J_1,J_3]
       -d\chi_X(J_3)\det[V,J_1,J_2]\bigr\}.
 \end{split}                                                     \tag{1}
\]
Here dchi is the real differential, including both complex-coordinate
parts when chi is not holomorphic. Extend each coefficient by zero
on Q minus D, including all stopped parameters and initial diagonals.
The symbols in (1) henceforth denote those Borel zero extensions;
no derivative of a stopped map is defined. Thus C466y's full forms are
\[
 \bar\beta=A\,du_1\wedge du_2\wedge du_3
   +B_{12}\,dt\wedge du_1\wedge du_2
   +B_{13}\,dt\wedge du_1\wedge du_3
   +B_{23}\,dt\wedge du_2\wedge du_3,
 \qquad
 \bar\gamma=G\,dt\wedge du_1\wedge du_2\wedge du_3.       \tag{2}
\]
All orientations below are relative to dt wedge du1 wedge du2 wedge du3.

## Conclusion

For every fixed pair eta,chi, the raw tested slice
\[
 a_{\eta,\chi}(t)=\int_I\eta(u)A(t,u)\,du\quad(0<t<T_0)   \tag{3}
\]
is bounded and measurable. It has the actual right limit
\[
 \lim_{t\downarrow0}a_{\eta,\chi}(t)
   =a_0:=i\int_I\eta(u)\chi(iu)\Delta(u)^2e^{-H(iu)}\,du. \tag{4}
\]
It has a unique Lipschitz representative tilde(a) on [0,T_0],
equal to (3) for almost every time, and for every 0<=s<=t<=T_0,
\[
 \begin{split}
 \widetilde a(t)-\widetilde a(s)
 &=\int_s^t\int_I
 \{\eta G-(\partial_1\eta)B_{23}
          +(\partial_2\eta)B_{13}-(\partial_3\eta)B_{12}\}
                  \,du\,dr,\\
 \widetilde a(0)&=a_0. 
 \end{split}                                                     \tag{5}
\]
In particular (5) with s=0 is the finite-time balance from the
explicit initial pullback. All four terms in (1)'s G and all three
parameter-flux terms in (5) are retained.

For a quantitative bound put p(u)=|Delta(u)|^2 and, off the diagonals,
\[
 m(u)=p(u)\left(2\sqrt2\sum_{i<j}|u_i-u_j|^{-1}+120\right),
 \quad E=\exp(-H_0+15\sqrt3/2+115/12).
\]
Set m=0 on the diagonals, and let C_0=||chi||_infinity and
C_1=sup_mathcal B ||dchi|| in the real covector norm. Then
\[
 \begin{split}
 |\widetilde a(t)-\widetilde a(s)|&\le L_{\eta,\chi}|t-s|,\\
 L_{\eta,\chi}&=E\int_I m(u)
 \left(4C_1|\eta(u)|+C_0\sum_{j=1}^3|\partial_j\eta(u)|\right)du
 <\infty. 
 \end{split}                                                     \tag{6}
\]

This is the local specialization of attempt995. Independent audit997
below validates its statement without changing hypotheses or constants.
Equality between tilde(a) and the raw stopped slice is asserted
only almost everywhere in positive time, for each fixed pair of tests;
no common exceptional set for all tests is asserted. At T_0 only the
representative is used. No positive-time pointwise slice continuity,
regularity of tau, cube-face trace, conservation, flux sign or flux
payment follows. Global assembly, all-degree positivity and Xi transfer
remain open. This is reproduction/specialization of the assessed
analysis, not a claim of progress beyond the checked sources or an RH
candidate.

## Proof

### Imported inputs and the specialization required

C466z/audit988 supplies this exact actual chart and verifies all
hypotheses of C466y/audit983. C466y(18),(26) supplies the Borel
coefficient bounds and the complete interior equation
\[
 |A|\le C_0Ep,\quad |B_{ij}|\le C_0Em,\quad |G|\le4C_1Em,
 \qquad -\int_Qd\phi\wedge\bar\beta=\int_Q\phi\bar\gamma
 \quad(\phi\in C_c^\infty(Q)).                            \tag{7}
\]
Its constants give the E above, because
sqrt3 a M_1=15sqrt3/2 and (4M_2+M_1^2)T_0=115/12.
Also p<=(2a)^6 and m<=6sqrt2(2a)^5+120(2a)^6, including the
diagonal extensions. Hence these are bounds on the entire finite box,
not only bounds on compact subsets separated from collisions.

For the scalar representative import T. Muthukumar, *Sobolev Spaces
and Applications*, 17 December 2023,
[Theorem 2.8.2 and proof, printed p.109](https://home.iitk.ac.in/~tmk/courses/mth656/main.pdf#page=117):
on an open interval a W^(1,p) function, 1<=p<=infinity, has an
absolutely continuous representative. Use this for the real and
imaginary components. The fundamental theorem and the bounded-weak-
derivative Lipschitz conclusion, with endpoint extension, are also
recorded in J. K. Hunter, *PDE notes*, 2009,
[Appendix, Theorems 3.50, 3.57, 3.59, 3.60, pp.75–77](https://www.math.ucdavis.edu/~hunter/m218a_09/ch3A.pdf).

Import complex-valued dominated convergence from Hunter,
*Measure Theory*, author-hosted chapter version inspected in review994,
[Theorem 4.24, proof and Section 4.6, pp.49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11),
and complex Fubini on sigma-finite measure spaces from
[Theorem 5.18, p.61](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf#page=8).
For smooth local flow at an interior distinct initial point, reuse
G. Teschl, *Ordinary Differential Equations and Dynamical Systems*,
author-hosted April 2012 preliminary version,
[Lemma 2.14/Corollary 2.15, pp.52–53, and Theorem 6.1 with proof, pp.189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
as assessed in ready992 and used in C466y.

These are precisely the tools covered by nomination993/completion994
before this attempt. They are imported, not reproved. What remains
to check is the oriented coefficient identity, its tested integrability,
the actual initial pullback and domination, and the representative's
identification with that limit. No smooth moving-domain transport
theorem or regular lifetime is used. The outer-grazing and sign-inference
stops961/968 are preserved; neither is a premise of this proof.

### Every term of the scalar weak derivative

Write eta_j=partial_j eta. For phi(t,u)=theta(t)eta(u), where
theta in C_c^infinity(0,T_0), expansion of dphi wedge bar(beta)
in the orientation of (2) gives the coefficient
\[
 \theta'\eta A+\theta(-\eta_1 B_{23}+\eta_2 B_{13}-\eta_3 B_{12}).
                                                               \tag{8}
\]
Indeed du1 wedge dt wedge du2 wedge du3 has sign minus;
du2 wedge dt wedge du1 wedge du3 has sign plus; and
du3 wedge dt wedge du1 wedge du2 has sign minus. Terms with a
repeated differential vanish. This checks all three mixed signs.
The formula for G in (1) is independently the alternating expansion
of (dchi wedge Omega)(V,J1,J2,J3), so it omits no cutoff derivative.

All coefficients are Borel by (7), each spatial slice is absolutely
integrable, and the corresponding space-time products are absolutely
integrable: I and the time interval are bounded, the coefficients
satisfy (7), and the fixed tests and their derivatives are bounded.
Thus complex Fubini applies. Substituting (8) into (7) and moving
the mixed terms to the right yields
\[
 -\int_0^{T_0}\theta'(t)a_{\eta,\chi}(t)\,dt
   =\int_0^{T_0}\theta(t)g_{\eta,\chi}(t)\,dt,\qquad
 g_{\eta,\chi}(t)=\int_I
   (\eta G-\eta_1B_{23}+\eta_2B_{13}-\eta_3B_{12})\,du.    \tag{9}
\]
Complex tests follow by linearity if (7) is first taken for real
tests. Bounds (7) give
\[
 |a_{\eta,\chi}(t)|\le C_0E\int_I|\eta|p\,du<\infty,
 \qquad |g_{\eta,\chi}(t)|\le L_{\eta,\chi}<\infty.       \tag{10}
\]
The bounds are uniform in 0<t<T_0. Compact parameter support makes
phi a legitimate test in Q even if its support meets initial diagonals.
There is no integration over the faces of I and no discarded derivative
of eta. Equation (9) identifies the full scalar weak derivative.

Consequently a belongs to W^(1,infinity)(0,T_0), with weak derivative
g. The cited one-dimensional representative theorem and fundamental
theorem, applied componentwise, give an absolutely continuous
representative with
tilde(a)(t)-tilde(a)(s)=integral_s^t g(r)dr on the open interval.
The complex triangle inequality and (10) give Lipschitz constant L,
without an extra componentwise factor. This implies unique continuous
extension to both finite endpoints. The integral formula extends there
as well, since g is integrable. Two such continuous representatives
agree everywhere if they agree almost everywhere, proving uniqueness.
This proves the balance part of (5) and (6) before identifying a_0.

### The actual initial limit and its representative

Fix distinct u in I. Then iu lies strictly inside U. The smooth real
local-flow theorem applies in a neighborhood of that point and its
initial parameters, for some positive time depending on u. On that
time interval the raw solution is the first-lifetime solution by
uniqueness. In particular
\[
 X(t,u)\longrightarrow iu,\qquad
 J_j(t,u)\longrightarrow ie_j\quad(t\downarrow0).         \tag{11}
\]
No lower bound on this time uniform in u is asserted. The determinant
limit is det(iI)=i^3=-i, and, because Delta has three factors,
Delta(iu)=i^3 Delta(u), hence Delta(iu)^2=-Delta(u)^2.
Continuity of chi, F and the determinant in (1) therefore gives
\[
 A(t,u)\longrightarrow(-i)\chi(iu)F(iu)
       =i\chi(iu)\Delta(u)^2e^{-H(iu)}.                 \tag{12}
\]
On an initial diagonal the extended A is zero for every positive
time, and the right side of (12) is also zero; no flow is assigned
there. Thus the claimed convergence holds with the specified
extension (in particular almost everywhere). The union of those
three hyperplanes is Lebesgue null.

For any sequence of positive times tending to zero, (7) supplies the
single integrable majorant C_0 E |eta(u)|p(u) for eta(u)A(t,u).
The limit in (12) is measurable, indeed continuous in u after its
diagonal value is included. All hypotheses of complex dominated
convergence hold. It gives (4) along every such sequence, and hence
the actual right limit in (4). This does not exchange any derivative
with a stopped endpoint or require a common survival time.

Finally choose times t_k decreasing to zero in the full-measure set
where the representative equals the raw tested slice. Such a sequence
exists because every initial time interval has positive measure.
Continuity of the representative at zero, equality at those t_k and
(4) yield tilde(a)(0)=a_0. Together with (9) this proves all of (5).
The same argument gives no identification of an arbitrary exceptional
positive-time raw slice or a literal raw slice at T_0, and none is used.

This connects the tested local current to its initial cycle with every
flux and cutoff source visible. Its use in a signed deformation would
still require paying those terms; the spatial cone in C466 is context,
not a mathematical input to this balance. No conservation or positive
flux is inferred from boundedness or the weak equation.

### Independent audit — 14 November 2026, step997

The invocation-start SPECIALIZE assessment995, separately approved996,
covers exactly this audit. Reuse completion994's inspected Muthukumar
Theorem2.8.2/proof, Hunter's representative/fundamental-theorem and
complex DCT/Fubini statements, and ready992's Teschl local-flow coverage.
No fresh source retrieval, general transport theorem or stronger trace
result is invoked. C466y/audit983 and C466z/audit988 are the established
mathematical inputs; the cone C466 is not used in this proof.

**Forms and orientation.** Evaluating a three-form on the ordered
coordinate vectors gives exactly the four coefficients in (2): for
example the dt du1 du3 coefficient evaluates on (V,J1,J3), with no
permutation of its columns. The alternating evaluation of dchi wedge
Omega on (V,J1,J2,J3) is

dchi(V) Omega(J1,J2,J3) - dchi(J1) Omega(V,J2,J3)
+ dchi(J2) Omega(V,J1,J3) - dchi(J3) Omega(V,J1,J2).

Since Omega=F omega, this is precisely (1)'s G, including all four
terms and the real differential of a possibly nonholomorphic chi.
For dphi wedge beta, the ordered lists (u1,t,u2,u3),
(u2,t,u1,u3), (u3,t,u1,u2) have respectively one, two and three
inversions relative to (t,u1,u2,u3). This proves the signs -, +, -
in (8). Substitution in the imported identity gives
\[
 -\int_0^{T_0}\theta'a\,dt-\int_0^{T_0}\theta C\,dt
   =\int_0^{T_0}\theta(t)\int_I\eta G\,du\,dt,
 \qquad C(t)=\int_I(-\eta_1B_{23}+\eta_2B_{13}-\eta_3B_{12})\,du.
\]
Moving C to the right gives exactly (9), not its sign reversal.

**Bounds, measurability and weak derivative.** C466z has the same
actual H, domain, first lifetime and strict buffer required by C466y.
Thus its Borel zero extensions are precisely those in (1), including
stopped parameters and initial diagonals. The constants are
sqrt3*(1/16)*120=15sqrt3/2 and
(4*1000+120^2)/1920=18400/1920=115/12, proving the stated E.
For distinct u each term p/|u_i-u_j| is one absolute difference to
power one times the other two to power two. Hence it is bounded by
(2a)^5; there are three such terms with coefficient 2sqrt2.
The remaining term is at most 120(2a)^6. The diagonal zero convention
obeys the same bounds. They are valid on all I, including triple
coincidences, not just compact sets away from them.

With fixed smooth compact eta,chi their norms and derivatives are
finite, and Q has finite measure. Every product used in (8)-(10) is
absolutely integrable in space and space-time. Borel measurability
and complex Fubini give measurable a and g; (10) holds at every raw
time in (0,T_0), while the weak derivative is an equivalence-class
statement. The bound for g is exactly (6), including 4C1 from the
complete gamma bound and all three first derivatives of eta. Thus
both components of a are in W^(1,infinity) on the finite interval.
The imported representative theorem and fundamental theorem apply;
the complex integral triangle inequality gives L, with no extra
factor from treating two components. Bounded derivative makes the
representative Lipschitz and gives its unique extension to both
endpoints. The integral formula persists there because g is in L1.
These facts identify no arbitrary exceptional raw positive-time slice.

**Initial pullback and endpoint identification.** Every distinct iu
is strictly interior to the punctured ODE domain: |u_j|<a<R and
Delta(iu) is nonzero. Smooth local dependence applies in a neighborhood
of that individual initial point. Uniqueness identifies this local
flow and its parameter derivative with the prescribed raw solution
for sufficiently small positive times depending on u. Its initial
Jacobian is iI. There are exactly three Vandermonde factors, so
Delta(iu)^2=i^6 Delta(u)^2=-Delta(u)^2 and det(iI)=i^3=-i.
Their product is +i, proving (12) with its full H(iu) phase.

On initial diagonals both sides of (12) vanish by definition, with
no assigned singular flow. For any sequence t_k tending to zero,
the function C0 E |eta|p is a single measurable integrable majorant
of every eta A(t_k,.) by (7). The pointwise limit is measurable and
continuous after its zero diagonal values are included. The assessed
complex DCT therefore gives the asserted actual right limit along
every sequence. No uniform positive lifetime or exchange with a
stopped-map derivative enters. Finally, the full-measure time set
where the representative equals a meets every interval (0,epsilon).
Choose a decreasing sequence there tending to zero. The raw right
limit and continuity of the representative identify its initial value
as (4). The endpoint at T_0 is only the representative's extension.

**Verdict.** No mathematical correction is required: (1)-(12), the
explicit Lipschitz constant, uniqueness and all endpoint qualifications
pass this bounded audit for every fixed admissible pair eta,chi.
The direct mathematical inputs remain C466y and C466z. This validates
a local analytic specialization; it is not a new result beyond the
sources compared or a proof of conservation. All beta/gamma terms
remain in (5). The strict buffer is retained, so stop961's earlier
outer-grazing example is outside these hypotheses. Stop968 still
forbids inferring signed global positivity from the current equation;
stop979's completed volume audit is not reopened. Cube interfaces,
flux payment, global tails, all degrees and actual-Xi transfer remain
independent gaps. No script, numerical experiment, Lean verification
or RH candidate is claimed.

## Mathlib

Full matching coverage for this current trace/balance has not been
checked; unknown availability is not absence. The previously inspected
[DominatedConvergence documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html)
contains supporting results
`MeasureTheory.tendsto_integral_of_dominated_convergence` and
`MeasureTheory.tendsto_integral_filter_of_dominated_convergence`.
Their measurability, integrable-majorant and a.e.-convergence hypotheses
are supported here by (7),(12); the filter variant has its additional
countably-generated-filter condition. No full matching Sobolev trace
or stopped-flow theorem was checked, and no Lean verification or
numerical certificate is claimed.
