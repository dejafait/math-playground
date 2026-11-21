# C468f — A matched curved lower connector on the chamber graph

## Hypotheses

Retain C467e/audit1017's actual coefficient flow, C467l/audit1037's
ordered-root limits, C467p(6)–(14)/audit1049's lower imaginary
interpolation and C467z(6)–(10)/audit1083's regular physical graph.
In particular, keep

\[
n=3,\quad R=1/4,\quad a_0=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
H(z)=H_0+\sum_{j=1}^3\beta(z_j),\quad
F(z)=\Delta(z)^2e^{-H(z)},\quad
\Delta(z)=\prod_{j<k}(z_k-z_j),\quad
\Omega=F(z)\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm with
exp B(w)=xi(1/2+sqrt(w))/xi(1/2) on |w-1|<R. Its inherited
qualifications, beta(0)=beta'(0)=0 and |beta''|<40 are unchanged.
The finite-zero/product inputs through L018/L021/L024/C466a and
the actual-background records remain qualified; in particular, this
step does not replay the external low-zero verification. It does not
need C467u's stronger derivative signs. No all-degree positivity,
density realization or RH premise is assumed.

For distinct initial u in (-a_0,a_0)^3 use the original raw flow

\[
Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                         -\overline{g(Y_j)},\qquad Y(0,u)=iu.
\tag{2}
\]

Use the closed ordered collar

\[
\mathcal U=\{(x-d,x+d,x+h): |x|\le X,\ 0\le h\le H_*,\
                                      0\le d\le h/4\}.
\tag{3}
\]

On its collision faces Y denotes the ordered limit, not a solution
of (2) started on the divisor. The existence and continuity needed
below follow from the cited coefficient/root inputs. At fixed outer
faces neighborhood extensions are allowed; no extra lateral value
is prescribed beyond continuity and the initial product.

Let f be any fixed real smooth function with 0<=f<=1, equal to one
on [-b_*,b_*], with support in (-2b_*,2b_*). Set G(q)=product f(q_j).
Neither f nor beta is assumed even. Write p_c(t,q) for C467z's
physical momentum graph, and W(t,q)=p_c(t,q)+iq. Let
q_1<q_2<q_3 be the actual imaginary roots on the lower face
Y^+(t,x,x+h). Define, without changing the original imaginary map,

\[
I=q_1+q_2+q_3,\quad q=q_3,\quad
\alpha=q_2-q_1,\quad \beta_g=q_3-q_2,\quad
m=(I-q)/2,\quad v=s\alpha/2,
\]
\[
Q_p(t,x,s,h)=(m-v,m+v,q),\qquad
Z_{\rm new}(t,x,s,h)=W(t,Q_p(t,x,s,h)).
\tag{4}
\]

The pair box is K=[0,tau] times [-X,X] times [-1,1] times [0,H_*],
with orientation dt wedge dx wedge ds wedge dh. The common minus
sign multiplies the entire chamber and pair forms. Time, divisor,
actual background and initial products remain unchanged. Only the
connector's real interpolation is replaced. The old affine scalar,
velocity, time-minor estimates and triangle match are not hypotheses.

## Conclusion

For one existential 0<tau<=T_0 there are real [0,1]-valued scalars
Theta on [0,tau] times the collar and phi on K, continuous on these
closed domains and smooth on their regular positive-time interiors,
such that

\[
\Theta(0,u)=G(u),\qquad \phi(0,x,s,h)=f(x)^2f(x+h),
\]
\[
d\Theta\wedge\operatorname{Re}(-Y^*\Omega)=0,\qquad
d\phi\wedge\operatorname{Re}(-Z_{\rm new}^*\Omega)=0,
\]
\[
Z_{\rm new}(t,x,1,h)=Y^+(t,x,x+h),\qquad
Z_{\rm new}(t,x,-1,h)=P_{12}Y^+(t,x,x+h),
\]
\[
\phi(t,x,1,h)=\phi(t,x,-1,h)=\Theta(t,x,x,x+h).
\tag{5}
\]

Here P_12 exchanges the lower two slots. The map stays in |z_j|<R
on the full box. Write its original, unnormalized complex pullback as

\[
\Psi=Z_{\rm new}^*\Omega
 =A\,dx\wedge ds\wedge dh+B_c\,dt\wedge dx\wedge dh
       +U\,dt\wedge ds\wedge dh+V\,dt\wedge dx\wedge ds.
\tag{6}
\]

The spatial density has the correct chamber-induced sign:

\[
\operatorname{Re}(-A)\ge\tfrac12|A|.
\tag{7}
\]

For t,h>0 it is nonzero precisely when s!=0. At h=0 and t>0
the spatial coefficient is zero. Its lower-time trace tends to zero.

Put lambda=h+sqrt(t). Constants below are uniform in K for t>0;
they can depend on the fixed analytic background and, for C_f, on f.
All four complex coefficients satisfy

\[
|A|\le C s^2\alpha\lambda^2,\qquad
|B_c|\le C s^2\lambda^2/\alpha,\qquad
|U|+|V|\le C s^2\alpha\lambda^3,
\tag{8}
\]
\[
|A\phi_t|+|B_c\phi_s|+|U\phi_x|+|V\phi_h|
                         \le C_f s^2\lambda^2.
\tag{9}
\]

In particular, these eight absolute terms have joint L1 majorants
through t=h=0. The four terms in (9) are bounded separately, before
any real adjoint cancellation. Positive-time face traces are the
actual restrictions of the new map and scalar, and their integrals
have dominated limits down to t=0 and h=0. No independent corner
term is needed for this local cutoff passage.

This local construction was obtained in attempt1096 under
nomination1094/review1095 and is **validated under its stated qualifications
by independent conceptual audit1098 below**. It meets that lower-connector test;
it does not establish an old-triangle match, a relative deformation,
an integrable chamber assembly identity, outer-face payment, a global
cycle, density realization, other degrees or actual-Xi positivity.
C468e/audit1094 stops a different, affine connector class and remains
intact. No complete RH candidate or certified originality is claimed.

## Proof

### Source scope and one regular physical transport

The unchanged invocation-start assessment is
`drafts/literature/2026-11-16-common-graph-curved-connector-nomination-1094.md`,
approved as EXPLORE by the separate review1095. The following is the
covered changed-geometry test. Its new work is the construction and
its signed and weighted parameter estimates, not general ODE or
pullback theory.

Import Gerald Teschl, *Ordinary Differential Equations and Dynamical
Systems*, April2012 author preliminary version,
[Theorems2.5/2.10–2.11, pp40–48; Lemma2.14/Corollary2.15, pp52–53;
Theorems3.9/3.12, pp81–84; Theorem6.1, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
We use smooth existence, uniqueness, dependence and continuation
only for the smooth time-dependent field on the open boxes below.
No singular-root transport theorem is imported.

C467z(6)–(10) supplies a smooth real graph p=p_c on an open box
containing [-a_0/2,a_0/2]^3. All its fixed-order derivatives are
bounded on smaller compact boxes; p and its spatial derivatives are
O(t). Put

\[
M=\mathrm{Id}-iD_qp,\qquad
\sigma_l=-\widehat\Pi_{t,2}(e(q))-q_l\widehat\Pi_{t,3}(e(q)),
\]
\[
\widehat a=e^{-H(W(t,q))}\prod_{l=1}^3(i+\sigma_l)^2\det M,
\quad \upsilon=-iM^{-1}p_t,\quad
b_c=-\frac{\operatorname{Re}(\widehat a\upsilon)}
                 {\operatorname{Re}\widehat a}.
\tag{10}
\]

After one common time reduction M is invertible and
Re(-widehat a)>=|widehat a|/2>0 throughout that compact box.
These are exactly C467z's quantities. Their smoothness, bounded
derivatives and permutation equivariance extend across q diagonals.
The division in (10) is by the nonzero regular graph factor, not
by Delta(q)^2 or a vanishing parameter coefficient.

The actual ordered chamber images for u in the compact collar, and
all Q_p images, lie in [-a_0/3,a_0/3]^3 on one smaller time interval.
Here is why the repeated-root cases cause no loss of uniformity.
For distinct collar data C467l(11)'s actual-flow argument bounds
the minimum imaginary gap from below by sqrt(t). The smooth
coefficient solution therefore has, at every t>0, three simple real
roots even at limits of ordered initial data. The limiting roots
are uniquely specified by their order, as in C467l(12). They depend
smoothly on positive-time coefficient charts, including the lower
and triple collision limits. At t=0, convergence of the coefficients
to e(u), compactness of the roots and uniqueness of the ordered
root list imply q(t,u)->u uniformly on the compact collar: otherwise
a convergent subsequence of the initial data and roots would give
a different ordered root list for the same limiting polynomial.
Every initial coordinate has modulus at most 3/256<a_0/3. The map
Q_p takes convex combinations of its first two roots and keeps its
third, so it lies in the same box. C467e's graph identification
and continuity give Y=W(t,Im Y) also on these ordered faces.

Bound b_c on a neighborhood of [-a_0/2,a_0/2]^3. Reduce time so
that its maximum displacement on [0,tau] is less than the positive
margin from [-a_0/3,a_0/3]^3 to that larger box. The cited ODE
continuation theorem then gives a single smooth backward endpoint
map R_c(t,q) for every q in a neighborhood of the smaller box,
with all first derivatives bounded and |R_c(t,q)-q|<=Ct. The
entire backward path lies in the larger physical box. Define

\[
\chi(t,q)=G(R_c(t,q)).
\tag{11}
\]

The chain rule along characteristics, uniqueness and smooth
dependence give

\[
\chi_t+b_c\cdot D_q\chi=0,\quad \chi(0,q)=G(q),\quad
0\le\chi\le1,\quad |\chi_t|+|D_q\chi|\le C_f.
\tag{12}
\]

The initial product is defined on the whole physical box. It is
invariant under slot permutations, even for asymmetric f. Uniqueness
and equivariance of b_c make R_c equivariant and chi invariant.

This is a particular smooth auxiliary selection. A path in this box
need not stay in the evolving image of the original chamber, as
C467 shows. No such assertion is used: the equation will be checked
pointwise after pullback. All values on the collar's outer faces
are determined by (11), with neighborhood extensions; none is an
independently adjustable inflow value. This respects the permitted
outer-face conditions and does not assert uniqueness in the original
chamber domain or a necessary trace for every possible scalar.

### Exact pullback, undivided equations and matched endpoints

For smooth maps use pullback composition, preservation of wedges
and commutation with exterior derivative, as stated and proved in
Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*,
author version 13January2010,
[sections13.5–13.6, pp441–442](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).
No immersion is required. We apply these identities on positive-time
smooth parameter charts; boundary continuity and mass estimates
are proved separately below.

Write a(t,q)=Delta(q)^2 widehat a(t,q). Since W_q/i=M and
W_t/i=-ip_t=M upsilon, direct expansion gives

\[
\Gamma:=W^*\Omega
 =a\{dq_1\wedge dq_2\wedge dq_3
   +\upsilon_1dt\wedge dq_2\wedge dq_3
   -\upsilon_2dt\wedge dq_1\wedge dq_3
   +\upsilon_3dt\wedge dq_1\wedge dq_2\}.
\tag{13}
\]

In particular,

\[
d\chi\wedge\operatorname{Re}(-\Gamma)
 =\Delta(q)^2\operatorname{Re}(-\widehat a)
       (\chi_t+b_c\cdot D_q\chi)\,
                    dt\wedge dq_1\wedge dq_2\wedge dq_3=0.
\tag{14}
\]

This is an undivided identity, valid on the diagonals too: there
the full form vanishes. Define

\[
\Theta(t,u)=\chi(t,\operatorname{Im}Y(t,u)),\qquad
\phi(t,x,s,h)=\chi(t,Q_p(t,x,s,h)).
\tag{15}
\]

The root continuity already proved and smoothness of chi make both
scalars continuous on their closed domains, including t=h=0.
They are smooth in their regular positive-time interiors. At t=0,
Im Y=u and Q_p=(x,x,x+h), proving the initial values in (5).
Pulling back (14) proves both equations in (5), without dividing
by any spatial coefficient. In the pair orientation, the exact
coordinate equation is

\[
\operatorname{Re}(A)\phi_t-\operatorname{Re}(U)\phi_x
       +\operatorname{Re}(B_c)\phi_s
       -\operatorname{Re}(V)\phi_h=0.
\tag{16}
\]

The common minus sign multiplies this entire equation by -1.
In particular (16) does not reuse the affine-pair velocity or equation.

For completeness all four new coefficients can be computed without
inverting the singular parameter Jacobian. With Q=Q_p and every
graph quantity evaluated at (t,Q), they are

\[
A=a\det(Q_x,Q_s,Q_h),\quad
B_c=a\det(Q_t+\upsilon,Q_x,Q_h),
\]
\[
U=a\det(Q_t+\upsilon,Q_s,Q_h),\quad
V=a\det(Q_t+\upsilon,Q_x,Q_s).
\tag{17}
\]

These identities follow by factoring M out of the three columns;
they are valid at s=0 and h=0 as well as the regular interior.

At s=1, Q_p is the original ordered imaginary face. C467e's graph
reconstruction makes W(t,Q_p)=Y^+. At s=-1 the imaginary entries
are exchanged, and equivariance of W gives P_12 Y^+. Equivariance
also gives Z_new(t,x,-s,h)=P_12 Z_new(t,x,s,h). Invariance of chi
then proves all scalar matching in (5) for the whole common horizon,
including h=0. No reflection symmetry of f was used.

The parameter orientations have not changed. At s=1 the pair face
has orientation dt wedge dx wedge dh. The map
u=(x-d,x+d,x+h) has spatial determinant 2, so the lower d=0 face
of the ordered chamber has orientation -dt wedge dx wedge dh.
Thus the matching values and maps have the original opposite face
signs. At s=-1 the endpoint and its parameter face orientation
are exactly the original permuted ones; P_12^*Omega=-Omega since
F is symmetric. This preserves the stated lower-slot permutation
convention. It asserts no matching to any upper or triangle face.

Finally, all Q_p are in the smaller physical box and p=O(t)
uniformly there. Reducing time to have |p_j|<=a_0/2 gives
|W_j|<=sqrt((a_0/2)^2+(a_0/3)^2)<R. The original analytic weight
is therefore defined throughout the new map, including its divisor.

### The signed spatial Jacobian

Set c=x+h/3 and lambda=h+sqrt(t). C467p(8)–(9) gives, uniformly,

\[
\sqrt t\le\alpha\le5\sqrt t,\qquad
c_0\lambda\le\beta_g\le C\lambda,\qquad
c_0\lambda\le\alpha+\beta_g\le C\lambda,
\tag{18}
\]

where c_0>0 is a constant, not a new time parameter. Define the
coefficient polynomial
mathcal Q_t(z)=z^3-E_1 z^2+E_2 z-E_3 on the actual lower face.
C467p(12)–(14), with derivatives here at fixed c or fixed h, gives

\[
I_c=a_1,\quad I_h=h b_1,\quad
q_c=a_2/\mathcal Q_t'(q),\quad
q_h=h b_2/\mathcal Q_t'(q),
\]
\[
N=a_1b_2-b_1a_2>0,\quad c_1\lambda\le N\le C\lambda,
\quad \mathcal Q_t'(q)=\beta_g(\alpha+\beta_g)>0.
\tag{19}
\]

These are estimates for the unchanged imaginary map, not assertions
about its old real interpolation. The linear map (I,v,q)->Q in
(4) has determinant 1. Only v depends on s, with v_s=alpha/2.
Also (x,s,h)->(c,s,h) has determinant 1. Consequently

\[
J_Q:=\det D_{(x,s,h)}Q_p
 =\frac\alpha2(I_cq_h-I_hq_c)
 =\frac{\alpha hN}{2\mathcal Q_t'(q)}>0\quad(t,h>0).
\tag{20}
\]

At every t>0 the simple roots and their initial-data derivatives
are smooth through h=0. The exact h factor in (20) therefore
also shows J_Q=0 there. No O(t)/h sign comparison is used.

Write ell=q-m=(alpha+2 beta_g)/2. Since |v|<=alpha/2,
ell-|v|>=beta_g>0. Thus

\[
\Delta(Q_p)^2=s^2\alpha^2(\ell^2-v^2)^2.
\tag{21}
\]

By (17), A=Delta(Q_p)^2 widehat a J_Q. Both real factors are
nonnegative, and strictly positive when t,h>0 and s!=0.
The graph sector in (10) proves (7), including all stated zeros.
This calculation retains the algebraic square and full complex
determinant; it does not substitute a modulus-square current.

### All complex masses and their scalar derivatives

Here and below x derivatives hold h fixed, as required in (6).
The coefficient functions E(t,e(x,x,x+h)) and their first t,x,h
derivatives are bounded on a common compact neighborhood by C467e.
For each actual simple root q_j and r=x,h, implicit differentiation
gives

\[
(q_j)_r=
\frac{(q_j^2,-q_j,1)E_r}{\mathcal Q_t'(q_j)}.
\tag{22}
\]

The absolute denominators are respectively alpha(alpha+beta_g),
alpha beta_g and beta_g(alpha+beta_g). Each is at least c alpha
lambda by (18), since alpha<=C lambda. The roots and numerators
are bounded. Therefore

\[
|(q_j)_x|+|(q_j)_h|\le C/(\alpha\lambda).
\tag{23}
\]

For time use the actual equation, not the weaker coefficient
derivative bound. C467l(9), passed to the positive-time simple-root
limit, says

\[
(q_j)_t=2\sum_{k\ne j}\frac{c_{jk}}{q_j-q_k}
                +\operatorname{Im}g(Y_j^+),\qquad
0<c_{jk}\le1.
\tag{24}
\]

All gaps are at least sqrt(t), and the actual background is bounded
on the compact analytic domain. Since alpha<=5sqrt(t), (24) yields
|(q_j)_t|<=C/alpha. Passing (24) to the repeated-initial-data limit
is legitimate on every compact positive-time interval: the limiting
roots remain simple, so coefficient/root derivatives converge there.
No equation is evaluated at a time-zero collision.

The interpolation (4) now gives

\[
|Q_x|+|Q_h|\le C/(\alpha\lambda),\qquad
|Q_s|\le C\alpha,\qquad |Q_t|\le C/\alpha.
\tag{25}
\]

The graph quantities widehat a and upsilon are uniformly bounded.
Alternatively, the exact factorization
p_k-p_j=(q_k-q_j)sigma_l shows directly that the original complex
weight is bounded by C Delta(Q_p)^2 on this box. In either form,
(18),(21) give

\[
|a(t,Q_p)|\le C s^2\alpha^2\lambda^4.
\tag{26}
\]

Use the determinant bound by the product of column norms in (17).
Since alpha is bounded above, |Q_t+upsilon|<=C/alpha. The three
column products for A, B_c and either of U,V, respectively, are
bounded by

\[
\frac1{\alpha\lambda}\,\alpha\,
       \frac1{\alpha\lambda},\qquad
\frac1\alpha\,\frac1{\alpha\lambda}\,
       \frac1{\alpha\lambda},\qquad
\frac1\alpha\,\alpha\,\frac1{\alpha\lambda}.
\tag{27}
\]

Multiplication by (26) proves precisely (8). In particular, this
bound has recomputed the coefficient without ds; no affine-minor
cancellation or old pair estimate has been transferred.

The chain rule in (15) and the uniform physical derivatives in
(12) also give

\[
|\phi_t|\le C_f/\alpha,\quad
|\phi_s|\le C_f\alpha,\quad
|\phi_x|+|\phi_h|\le C_f/(\alpha\lambda).
\tag{28}
\]

Multiplying (28) by the corresponding coefficient bounds in (8)
gives (9) term by term. For example |B_c phi_s|<=C_f s^2 lambda^2,
and |U phi_x|<=C_f s^2 alpha lambda^3/(alpha lambda).
Thus the absolute products are controlled before (16) is used.

For explicit joint integrability, let Lambda=H_*+sqrt(tau). From
(18), lambda<=Lambda and alpha>=sqrt(t), so the sum of the four
coefficient moduli is bounded by C(1+t^(-1/2)) on K, and the sum
in (9) by C_f Lambda^2. These are integrable in all four parameter
variables. For example the integral of the first majorant is at
most C(2X)(2)H_*[tau+2sqrt(tau)]. Values on t=0 may be defined
arbitrarily for this Lebesgue estimate. Removing either t<epsilon
or h<eta gives tails tending to zero uniformly in the other cutoff.
This is a joint majorant, not merely an iterated pointwise limit.

### Actual face limits and limitations

At every positive time the ordered roots, W and chi are smooth in
the parameters through h=0 and at the fixed x,s faces. Their
restricted forms therefore converge to their actual restrictions
on compact positive-time slabs. The following bounds pay the
remaining time interval as well. The h-face coefficient is V, with
|V|<=C sqrt(t)(H_*+sqrt(t))^3 uniformly in h. The x-face coefficient
is U with the same bound. The s-face coefficient B_c has the
integrable majorant C(H_*+sqrt(t))^2/sqrt(t), uniformly in s,h.
Multiplication by the continuous scalar, bounded by one, preserves
these bounds. The lower-time coefficient satisfies
|A|<=C sqrt(t)(H_*+sqrt(t))^2 uniformly on the spatial box, and
therefore tends to zero in L1(dx ds dh).

Dominated convergence applies componentwise, using John K. Hunter,
*Measure Theory*,
[Chapter4, Theorem4.24 and section4.6, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf).
The convergent face integrands are measurable, and the displayed
majorants are independent of the cutoffs. If one writes the tested
Stokes identity on a positive-cutoff box, Brian Conrad,
[*Stokes' theorem with corners*, Theorem1.1 and coordinate proof,
pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf),
applies to its smooth forms with their induced orientations, after
a smooth compact cutoff on a neighborhood of that compact box.
The bulk terms involving a smooth test derivative are bounded by
(8), and those involving dphi by (9). The form Omega is closed
on its analytic domain, so pullback gives dPsi=0 in the smooth
region; no extra derivative term is missing. Hence every term has
the described limit for arbitrary relative cutoff rates. This is
a local cutoff statement retaining all boundary terms, not their
payment or cancellation in a global construction.

In particular the h=0 trace is the restriction of the new curved
graph (4). It has not been identified with the old affine triangle
edge. No common value along that edge, new time-zero scalar
derivative, or confinement in the evolving chamber image was
assumed. The original matched endpoints, one horizon, signed
spatial density and full complex mass requirements are met by
this construction; independent audit1098 below checks these local claims.

### Independent conceptual audit — 16 November 2026, step1098

This is RESEARCH / REPRODUCTION under the invocation-start SPECIALIZE
assessment
`drafts/literature/2026-11-16-common-graph-curved-connector-audit-nomination-1096.md`,
separately approved by review1097. Reuse its primary theorem and proof-case
coverage, with the precise ODE, pullback, Stokes and dominated-convergence
citations above. This audit checks their application to (4), rather than
reproving those theorems or constructing another connector. C467e/audit1017,
C467l/audit1037, C467p/audit1049 and C467z/audit1083 retain their original
qualifications. The external low-zero evidence is not replayed, and no
all-degree sign or Xi realization is a premise.

**Common domain and ordered limits.** C467e's convex coefficient
neighborhood contains the coefficient image of [-a_0,a_0]^3 strictly
inside its regular ODE domain. E_t is uniformly C1-close to the identity;
its inverse is defined on a neighborhood of the smaller compact
coefficient image used by C467z. Thus C467z(6) gives one smooth graph on
(-3a_0/4,3a_0/4)^3, not inverses only on separate simple-root charts.
The closed box [-a_0/2,a_0/2]^3 has positive distance from that boundary.
On it p and its fixed-order spatial derivatives are O(t), and p_t and
the needed mixed derivatives are bounded. C467z(7) gives the exact three
pair-difference factors. At t=0 the product of the three squared i
factors is -1. C467z(9)'s phase estimate and compact continuity give
the nonzero regular factor and sector in (10) on one horizon. Hence
division in (10) is legitimate on the whole physical box.

For ordered distinct initial collar data, C467e identifies the
coefficient solution with the actual raw flow. C467l(9)–(11)'s
minimum-gap estimate uses only that initial domain, the secant bound
and |g'|<40, so it applies to these data too. On taking ordered limits
at either collision face, the positive-time gaps remain at least
sqrt(t). The limiting polynomial has three simple real roots uniquely
identified by their order, and the simple-root implicit function theorem
gives its smooth positive-time charts. To check uniform convergence at
time zero, suppose it fails and choose t_n tending to zero, initial
data u_n tending to u_* and a convergent subsequence of the bounded
ordered roots witnessing failure. Coefficient convergence makes that
limit the ordered root list of the polynomial with roots u_*, including
repetitions. That list is uniquely u_*, a contradiction. Reconstruction
gives the continuous complex trace and its graph identification. This
proves joint continuity, not merely convergence at each fixed h.

Every initial collar coordinate has modulus at most 3/256<1/48=a_0/3.
Uniform convergence therefore places all collar roots in
[-a_0/3,a_0/3]^3 on one horizon. Q_1 and Q_2 are convex combinations
of its first two roots, and Q_3 is unchanged, so the same box contains
all interpolated images. Its margin inside the larger box is a_0/6.
Bound b_c and its derivatives on a slightly larger compact neighborhood
and choose tau with displacement smaller than that margin. The cited
regular-flow continuation and smooth-dependence theorems give R_c and
bounded first derivatives on a neighborhood of every image. This is a
regular physical ODE, not an ODE started on the root divisor. Finitely
many subsequent time reductions preserve this single horizon.

The collar allows neighborhood extensions at outer faces and prescribes
no independent lateral value. G is smooth on the entire physical box.
Thus chi=G composed with R_c is an admissible auxiliary choice even
when a backward path leaves the evolving chamber image. The exact
pullback identity below checks its restriction's original equation.
This does not claim original-domain confinement or a necessary trace
for all possible scalars. Every outer value is determined by the same
chi; no free inflow is being asserted after restriction.

**Undivided equations, initial data and endpoints.** W_q/i=M and
W_t/i=-ip_t=M upsilon. Factoring M gives (13). With dt first,
wedging dchi into its three time terms gives
-sum_j Re(a upsilon_j) chi_(q_j), while its spatial term gives
Re(a) chi_t. Since a=Delta(q)^2 widehat a with Delta(q)^2 real,
the common minus sign gives precisely (14), with b_c as in (10).
On a diagonal the full form is zero: no divided equation is used
there. Smooth pullback on positive-time charts gives both equations
in (5), including points where the spatial Jacobian vanishes. In
dt,dx,ds,dh order the signs in (16) are +,-,+,-. Factoring M after
composition gives all four column orders in (17), in particular
B_c=a det(Q_t+upsilon,Q_x,Q_h).

Ordered continuity and chi(0,q)=G(q) give both original initial
products. G is invariant under slot permutations even for asymmetric
f. Equivariance of b_c, uniqueness of its flow and equivariance of W
prove the permuted s=-1 endpoint and equal scalar values from s=1.
These identities extend to h=0 by the proved continuity. No time-zero
scalar derivative is used. The pair's s=1 face has orientation
dt wedge dx wedge dh. The chamber map u=(x-d,x+d,x+h) has determinant
2, and its lower d=0 face has the negative orientation. At s=-1
the parameter orientation reverses and P_12^*Omega=-Omega, retaining
the original permutation convention. Finally |p_j|<=a_0/2 and
|Q_j|<=a_0/3 give |W_j|<=a_0 sqrt(13)/6<R, so the original analytic
weight is defined everywhere on the map, including its divisor.

**Exact spatial Jacobian.** The pair parameters satisfy
|c|<=5/768<1/64 and h<=1/128<1/64, strictly inside C467p(6)'s
enlarged domain. Its audited (8)–(14) apply to this unchanged imaginary
map and give (18)–(19): N is positive and comparable to lambda,
and mathcal Q_t'(q)=beta_g(alpha+beta_g) is comparable to lambda^2.
The linear map (I,v,q) to Q has matrix

    ( 1/2  -1  -1/2 )
    ( 1/2   1  -1/2 )
    (  0    0    1  ),

whose determinant is one. The map (x,s,h) to (c,s,h) also has
determinant one. Expand the remaining determinant along its s column,
whose only nonzero entry is v_s=alpha/2: this gives exactly (20).
Its h factor is exact, and the roots and parameter derivatives are
smooth through h=0 at each positive time. Thus J_Q>0 for t,h>0 and
J_Q=0 for h=0, without an O(t)/h comparison.

The Q differences are s alpha, ell+v and ell-v. The last two are
positive and at least beta_g; their algebraic square gives (21).
Therefore A=Delta(Q)^2 widehat a J_Q satisfies (7) and is nonzero
exactly when s!=0 for t,h>0. At h=0 it vanishes. This verifies the
full complex determinant with the common minus sign, not a replacement
by a modulus-square current.

**Each complex coefficient and derivative product.** The derivatives
E_x,E_h in (22) are uniformly bounded at fixed initial x,h on the
compact coefficient neighborhood. The absolute root denominators are
alpha(alpha+beta_g), alpha beta_g and beta_g(alpha+beta_g). The first
two are at least c alpha lambda. The third is at least c lambda^2,
hence at least c' alpha lambda because alpha<=5lambda. This proves
(23) separately for every root. For time, the actual equation (24)
passes through the positive-time simple-root charts. Its repulsive
terms are at most C/sqrt(t), and its background is bounded. Since
alpha<=5sqrt(t), this gives C/alpha. The weaker coefficient-derivative
bound is not substituted for this necessary time estimate.

Interpolation gives (25), and widehat a and upsilon are uniformly
bounded. The two singleton gaps in (21) are at most C lambda, giving
(26), including s=0. The determinant column products in (17) are
bounded respectively by

    A:   C/(alpha lambda^2),
    B_c: C/(alpha^3 lambda^2),
    U,V: C/(alpha lambda).

Multiplication by C s^2 alpha^2 lambda^4 proves exactly (8).
The chain rule for the single smooth chi gives (28), including the
explicit chi_t term in phi_t. Multiplying term by term bounds each
of |A phi_t|, |B_c phi_s|, |U phi_x| and |V phi_h| by
C_f s^2 lambda^2. Thus all eight absolute quantities pass independently
of real cancellation, normalized coefficients or old affine time-minor
estimates. On the full box their sums are bounded respectively by
C(1+t^(-1/2)) and C_f Lambda^2, the joint integrable majorants
stated after (28).

**Faces and joint cutoffs.** The simple-root charts extend smoothly
through h=0 at every positive time. The V integrand on h=eta therefore
converges to its actual restriction there. Its majorant
C sqrt(t)(H_*+sqrt(t))^3 is independent of eta and integrable. The
same majorant bounds U on x faces. On s faces the majorant for B_c
is C(H_*+sqrt(t))^2/sqrt(t), integrable and independent of h,s.
Multiplying by phi or a fixed smooth test preserves these bounds.
On t=epsilon, A is uniformly bounded by
C sqrt(epsilon)(H_*+sqrt(epsilon))^2. Its whole spatial face integral
tends to zero uniformly in a simultaneous lower h cutoff. The
upper-time face is smooth through h=0 and its omitted strip has
vanishing integral.

For arbitrary relative cutoff rates, first fix delta>0 in time.
On [delta,tau] smoothness gives convergence of the h-face integrands.
The omitted [0,delta] tails of V and U are uniformly small by their
displayed majorant; the B_c tail is uniformly small by its integrable
t^(-1/2) bound. Removing an h strip on a fixed x or s face costs at
most its width times the integral of the corresponding dominator.
The lower-time face is already uniformly small. These facts give the
same limit along every (epsilon,eta) tending to (0,0), without a
relation between the cutoffs. Bulk terms involving smooth test
derivatives use (8), and those involving scalar derivatives use (9);
absolute continuity of their integrals gives the joint bulk limit.
No face convergence is inferred merely from bulk L1.

Omega is a closed holomorphic three-form on the verified polydisc,
with zeros rather than poles on the divisor. Its smooth pullback on
every positive-cutoff box satisfies dPsi=0. The cited Stokes theorem
applies after a compact cutoff equal to one near that box. The bounds
above justify every limiting term componentwise by dominated
convergence. There is no omitted independent corner term. The h=0
face remains as its actual new restriction, not a vanished face or an
identified old triangle edge.

All local claims (5)–(9) and their stated cutoff interpretation pass
without changing the construction or adding an assumption. This
validates an existing local input, not a discovery beyond the assessed
sources or a complete RH argument. The horizon remains existential.
Other interfaces, a replacement for the old triangle, chamber/global
assembly, outer-face payment and Xi transfer remain independent gaps.
C468e/audit1094 and earlier affine-class stops are unchanged. No
numerical certificate or mathematical script is needed for these checks.

## Mathlib

Full matching Mathlib coverage for this actual curved-connector
construction is unchecked. The regular ODE, smooth pullback,
Stokes and dominated-convergence inputs are imported with their
precise citations above; their supporting formalizations would not
by themselves verify the actual-root specialization or these bounds.
Audit1098 is an informal mathematical check, not a Lean verification
or a claim of absence from Mathlib.
