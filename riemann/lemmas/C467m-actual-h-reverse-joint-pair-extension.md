# C467m — Integrable physical-time extension of the actual pair family

## Hypotheses

Use C467e/audit1017's regular coefficient flow, C467j/audit1029's
original pair form, C467k/audit1033's actual triple-edge maps and
C467l/audit1037's common actual pair domain. Retain their actual
analytic background and qualifications from C466z/audit988 and
C466/audit993. In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
H(z)=H_0+\sum_j\beta(z_j),\quad F(z)=\Delta(z)^2e^{-H(z)},
\quad\Delta(z)=\prod_{j<k}(z_k-z_j),\quad
\Omega=F(z)\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2) with the inherited
conjugation normalization, beta(0)=beta'(0)=0 and |beta''|<40 on
|z|<R. Keep C466a's external qualifications for any reciprocal-density
interpretation. No realization or RH premise is assumed.

Set X=1/256 and H_*=1/128. On

\[
|x|\le X,\quad 0<|h|\le H_*,\quad |s|\le1,\quad y=x+h,
\tag{2}
\]

let Y^+(t,x,y) be the actual delta>0 trace from initial data
(x-delta/2,x+delta/2,y) of the raw flow

\[
Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
             -\overline{g(Y_j)},\qquad Y(0,u)=iu.
\tag{3}
\]

Put m=(Y^+_1+Y^+_2)/2, d=(Y^+_2-Y^+_1)/2, w=Y^+_3, and use
exactly Z=(m-sd,m+sd,w). Derivatives with respect to x below hold
h fixed, so they are partial_x+partial_y in the older independent
(x,y) coordinates. Orient both components by dt wedge dx wedge ds
wedge dh. This is C467j's orientation under y=x+h. Other slot
placements carry both their target permutation and their induced
parameter orientation. Multiplication of all forms by the common
minus sign is allowed only together, as in C467j–l.

## Conclusion

For one existential common 0<tau<=T_0, the original pullback has

\[
\Psi=Z^*\Omega
 =A\,dx\wedge ds\wedge dh+B_c\,dt\wedge dx\wedge dh
   +U\,dt\wedge ds\wedge dh+V\,dt\wedge dx\wedge ds,
\tag{4}
\]
\[
|A|+|U|+|V|\le C s^2 t^{3/2},\qquad
|B_c|\le C|s|^3\sqrt t
\quad(0<t\le\tau),
\tag{5}
\]

with finite C uniform over all of (2), on both components. The fixed
actual background is included in C. Thus all original coefficients
are absolutely integrable at the joint corner, with no restriction on
|h|/sqrt(t). The entire lower-time trace tends to zero in L1(dx ds dh)
at rate O(t^(3/2)).

The entire h=+eta and h=-eta restricted three-forms converge in
L1(dt dx ds), down to t=0, to the two actual limiting segment forms.
Under C467k's six prescribed slot choices and s=1-2lambda these are
its oriented outer-edge traces, opposite to the triangle faces.
The complete tested Stokes identity (18) below passes to the joint
limit for arbitrary relative rates of the time and separation cutoffs.
It retains every upper-time, x-side, s-endpoint and outer-h term, and
has no extra term supported at t=h=0.

This local result of attempt1039 is validated by the independent
conceptual audit1041 below. It does not pay any lateral face, construct a global cycle,
settle density realization, other degrees or actual-Xi positivity.
It does not remove C467i's defect for the unaugmented current or the
prescribed-cap obstruction1009. This is not a complete RH candidate.

## Proof

### Source scope and standard imports

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-reverse-pair-joint-extension-nomination-1037.md`,
separately approved in review1038. Its inspected comparison found no
matching joint-extension theorem; that bounded search establishes no
originality. The additional target-specific work is the uniform gap
comparison and weighted mixed-minor cancellation below. The spatial
sector alone is not being used as a time-derivative bound.

For positive-cutoff boxes import Brian Conrad, *Math396. Stokes'
theorem with corners*, [Theorem1.1 and its coordinate proof, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf).
Each box is a compact oriented manifold with corners; the maps and
forms are smooth on its neighborhood. A smooth cutoff equal to one
on the box meets the compact-support convention. Apply the theorem
componentwise to the complex form. No immersion is required; the
smooth-map convention is also recorded in Guillemin–Sternberg,
*Semi-classical analysis*, 13January2010,
[section13.13, (13.7)–(13.8), pp449–452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).

For integrable limits import John K. Hunter, *Measure Theory*,
[Chapter4, Theorem4.24 and section4.6, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf).
Use its dominated-convergence theorem for real and imaginary parts
on the fixed finite parameter spaces, with majorants proved below.
No singular Stokes, automatic trace or removability theorem is used.

Smooth coefficient dependence is the already established C467e input,
using Gerald Teschl, *Ordinary Differential Equations and Dynamical
Systems*, April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81; Theorem6.1,
pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
C467l checks the common compact domain and the positive-time simple
root charts. We need only finitely many first coefficient derivatives
there. These cited general theorems are not reproved.

### A uniform upper bound for the split pair

First work on actual distinct-data trajectories approximating (2),
with 0<delta<2|h|. Their ordered imaginary coordinates r_1<r_2<r_3
obey C467l(9):

\[
r_j'=2\sum_{k\ne j}\frac{c_{jk}}{r_j-r_k}+b_j,
\quad 0<c_{jk}\le1,\quad |b_j-b_k|\le41|r_j-r_k|.
\tag{6}
\]

Here c_{jk}=(1+theta_{jk}^2)^(-1), with the actual secants
|theta_{jk}|<=kappa=5/1024. The background in b_j is the actual
Im g(Y_j); the bound follows from |g'|<40 and the secant estimate.
These bounds hold on one compact common coefficient-flow interval.

Write alpha_1=r_2-r_1 and alpha_2=r_3-r_2. Direct subtraction gives

\[
\alpha_1'=4c_{12}/\alpha_1-2c_{23}/\alpha_2
              +2c_{13}/(\alpha_1+\alpha_2)+b_2-b_1
\le6/\alpha_1+41\alpha_1.
\tag{7}
\]

The corresponding upper-gap equation is
alpha_2'=4c_{23}/alpha_2-2c_{12}/alpha_1
+2c_{13}/(alpha_1+alpha_2)+b_3-b_2, giving the same bound.
Thus (alpha_j^2)'<=12+82alpha_j^2. Integrating this inequality
before taking a collision limit gives

\[
\alpha_j(t)^2\le e^{82t}\alpha_j(0)^2
                       +\frac{12}{82}(e^{82t}-1).
\tag{8}
\]

For h>0 the initial split pair is the lower adjacent pair; for h<0
it is the upper adjacent pair. In each case its initial gap is delta.
C467l's ordered actual-trace limit permits delta to tend to zero in
(8). Write alpha for that pair's resulting gap and b for the other
adjacent gap. C467l(12) supplies the lower bounds for both. Since
e^(82T_0)<2, (8) gives

\[
\sqrt t\le\alpha<\sqrt{24t}<5\sqrt t,\quad b\ge\sqrt t,
\quad c:=\alpha+b\le6b.
\tag{9}
\]

The elementary bound e^(82T_0)<2 follows, for example, from
82T_0<1/2 and exp(z)<=1/(1-z) for 0<=z<1. All constants are
independent of x,h and the approximation. No field is evaluated on
an initial divisor. Decrease the common time to the minimum of the
positive times already supplied by C467e,k,l when necessary.

### Keep the full original weight before bounding the minors

Use the paired labels q_1<q_2 and singleton q_3 for Im Y^+; the
singleton is extreme, above for h>0 and below for h<0. In either
case |Delta(q)|=alpha b c and Q'(q_3)=bc>0. C467e's reconstruction
is

\[
Q(v)=v^3-E_1v^2+E_2v-E_3,\qquad
P(v)=\Pi_1+(E_1-v)\Pi_2+(v^2-E_1v+E_2)\Pi_3,
\quad Y_j^+=P(q_j)+iq_j.
\tag{10}
\]

Here e(q)=(q_1+q_2+q_3,q_1q_2+q_1q_3+q_2q_3,q_1q_2q_3).
The coefficients E,Pi are smooth functions of
(t,e^0), where e^0=e(x,x,x+h), on a compact neighborhood including
t=h=0. Their t,x,h derivatives and the corresponding coefficients
of P are uniformly bounded. Indeed |x+h|<=3/256<a, so the entire
initial set and a neighborhood of its distinct approximants lie
inside C467e's common regular coefficient domain. Also
|q_j|<=r_*:=sqrt(3/160), and all
real-to-imaginary secants have modulus at most kappa.

Consequently |d|<=sqrt(1+kappa^2)alpha/2. Each singleton-to-segment
gap is a convex combination of the two actual singleton gaps, hence
has modulus at most sqrt(1+kappa^2)c. Use the exact identity
Delta(Z)=2sd[w-(m-sd)][w-(m+sd)]. C467l's domain bound gives
|sum beta(Z_j)|<=3/8. With finite constants depending only on this
fixed compact setup,

\[
|F(Z)|\le C s^2\alpha^2c^4
        \le C s^2\alpha^2b^2c^2
        =C s^2|\Delta(q)|^2.
\tag{11}
\]

The second inequality uses c/b<=6 and absorbs its square in C.
This is a bound on the original F, valid also at s=0. Neither the
current nor any form is divided by its vanishing weight.

### The three coefficients containing ds

The symmetric sum is smooth even at the initial discriminant:

\[
S=\sum_jY_j^+=3\Pi_1+2E_1\Pi_2+E_2\Pi_3+iE_1,
\qquad m=(S-w)/2.
\tag{12}
\]

All S_r, r in {t,x,h}, are bounded. At the singleton root q=q_3,
implicit differentiation at positive time gives

\[
q_r=\frac{(q^2,-q,1)E_r}{bc},\qquad
w_r=P_r(q)+(P_v(q)+i)q_r.
\tag{13}
\]

Here P_r means differentiation of its coefficients with v held
fixed. Its value and every numerator are bounded. Since bc is
bounded above, |w_r|<=C/(bc). Thus for r,v in {t,x,h},

\[
J_{rv}:=m_rw_v-m_vw_r
       =\tfrac12(S_rw_v-S_vw_r),\qquad |J_{rv}|\le C/(bc).
\tag{14}
\]

The cancellation in (14) is essential: separately multiplying
two root-derivative bounds would not give this estimate.

C467j's exact form identity, now in (t,x,s,h), gives
A=2iF dJ_{xh}, U=2iF dJ_{th}, V=-2iF dJ_{tx}.
Indeed dz_1 wedge dz_2=2dm wedge(s dd+d ds), and division of
the three differentials by i contributes the factor i. Equations
(9),(11),(14) bound the sum of their moduli by
C s^2 alpha^3bc <= C s^2 t^(3/2), since b,c are bounded above.
This proves the first part of (5), including all zeros s=0.

### The coefficient without ds

It is necessary to retain the full three-column determinant here.
Put J_q=D_q e(q) and R_q=diag(P_v(q_j)+i). The real coefficients
of P give |(R_q)_(jj)|>=1, so R_q and its inverse are uniformly
bounded on the compact set. For r in {t,x,h}, let
a_r=(P_r(q_1),P_r(q_2),P_r(q_3))^T. Then

\[
J_q q_r=E_r,\qquad
Y_r^+=R_qJ_q^{-1}\big(E_r+J_qR_q^{-1}a_r\big).
\tag{15}
\]

The entries of each bracket are bounded: J_q is polynomial in the
bounded roots, while E_r and a_r have the coefficient bounds above.
Since det J_q=-Delta(q), taking the determinant of all three columns
in (15), before taking absolute values, yields

\[
\left|\det(Y_t^+,Y_x^+,Y_h^+)\right|\le C/|\Delta(q)|.
\tag{16}
\]

In particular three inverse root denominators have not been estimated
independently. At fixed s, Z=M_sY^+ where

\[
M_s=\begin{pmatrix}(1+s)/2&(1-s)/2&0\\
(1-s)/2&(1+s)/2&0\\0&0&1\end{pmatrix},\qquad\det M_s=s.
\]

Therefore B_c=iF s det(Y_t^+,Y_x^+,Y_h^+). Equations (11),(16)
give |B_c|<=C|s|^3|Delta(q)|=C|s|^3alpha bc
<=C|s|^3sqrt(t), completing (5). This also verifies the full
coordinate change: V uses x at fixed h, equivalently the older
C467j coefficient V minus its U. No time minor is replaced by the
spatial minor or evaluated with y incorrectly held fixed.

### Entire faces and their oriented triple-edge traces

All bounds (5) hold pointwise on every fixed x,s,h face of the
domain. Thus fixed x=+-X faces have integrable U bounds, fixed
s=+-1 faces have integrable B_c bounds, fixed h=+-H_* faces have
integrable V bounds, and t=T>0 faces have bounded A. These are
prescribed-face estimates, not conclusions drawn from a.e. Fubini
slices. On the full lower-time spatial face, (5) gives
integral |A(epsilon,x,s,h)| dx ds dh <=C'epsilon^(3/2),
uniformly when any central h interval is removed.

For fixed t>0, C467k's incident-limit charts and C467l's ordered
identification show smooth convergence as h tends to zero from
either side, with the tangential t,x,s derivatives. The two limiting
maps are

\[
Z_0^+(t,x,s)=
 ((v_1+v_2)/2-s(v_2-v_1)/2,
  (v_1+v_2)/2+s(v_2-v_1)/2,v_3),
\]
\[
Z_0^-(t,x,s)=
 ((v_2+v_3)/2-s(v_3-v_2)/2,
  (v_2+v_3)/2+s(v_3-v_2)/2,v_1),
\tag{17}
\]

where the v_k are C467k's actual triple roots in increasing imaginary
order. In particular V(t,x,s,+eta) and V(t,x,s,-eta) converge
pointwise for t>0 to the coefficients V_0^+,V_0^- of
(Z_0^+)^*Omega,(Z_0^-)^*Omega in dt dx ds.
The x derivative here is precisely the simultaneous motion of the
initial pair and singleton, as required by (17).

The common majorant C s^2t^(3/2) is integrable on
(0,T] x [-X,X] x [-1,1]. It also bounds the limiting coefficients.
Hunter's theorem applied to each difference proves convergence in
L1 on this entire fixed face, not only on positive-time compact
slabs. Its time tail, uniformly in eta and in the limiting face,
is at most C'epsilon^(5/2). Multiplication by a fixed smooth test
at h=+-eta preserves L1 convergence to its value at h=0, since the
test is uniformly bounded and uniformly continuous.

For completeness the six slot choices are exactly C467k's table:
for edges j=0,2,4 use h>0 and slot orders (1,2,3),(3,1,2),(2,3,1);
for j=1,3,5 use h<0 and (1,3,2),(2,1,3),(3,2,1). With s=1-2lambda
the corresponding maps (17) are exactly
(1-lambda)V_j+lambda V_(j+1). This is equality of full maps and
their t,x,lambda derivatives, hence of the full restricted forms.
Finite permutations preserve the bounds just proved.

If epsilon_sigma is the permutation sign, the pair orientation is
epsilon_sigma dt dx ds dh. At the inner h face its induced
orientation is +epsilon_sigma dt dx ds for h>0 and
-epsilon_sigma dt dx ds for h<0. The listed signs are respectively
+1 and -1, so all six become positive dt dx ds. The substitution
ds=-2 dlambda makes each negative dt dx dlambda, whereas the
triple triangle's r=1 face is positive dt dx dlambda. Thus their
oriented full forms cancel, including the factor 2, whenever their
test values agree. The target permutation acts on Omega as well;
neither it nor the induced parameter sign is suppressed. The common
minus normalization preserves these cancellations. No statement
about unmatched test values or payment of other faces is intended.

### Full tested identity and arbitrary relative cutoff rates

Fix 0<T<=tau and a smooth phi on a neighborhood of the closed full
parameter box [0,T] x [-X,X] x [-1,1] x [-H_*,H_*], with bounded
values and first derivatives. Put
I_eta=[-H_*,-eta] union [eta,H_*] and
Q_(epsilon,eta)=[epsilon,T] x [-X,X] x [-1,1] x I_eta,
with the positive orientation on each component. Bracketed integrals
below use the increasing coordinate measures on their displayed
intervals. Since Omega is a holomorphic top-degree form on the entire
analytic polydisc, dOmega=0 including its zeros. At every positive
cutoff smooth pullback and the cited Stokes theorem give exactly

\[
\begin{split}
&\int_{Q_{\epsilon,\eta}}
 (\phi_t A-\phi_x U+\phi_s B_c-\phi_h V)\,dt\,dx\,ds\,dh\\
={}&\int_{[-X,X]\times[-1,1]\times I_\eta}
       [\phi A]_{t=\epsilon}^{T}\,dx\,ds\,dh\\
&+\int_{[\epsilon,T]\times[-X,X]\times I_\eta}
       [\phi B_c]_{s=-1}^{1}\,dt\,dx\,dh\\
&-\int_{[\epsilon,T]\times[-1,1]\times I_\eta}
       [\phi U]_{x=-X}^{X}\,dt\,ds\,dh\\
&-\int_{[\epsilon,T]\times[-X,X]\times[-1,1]}
 \left([\phi V]_{h=-H_*}^{-\eta}
             +[\phi V]_{h=\eta}^{H_*}\right)\,dt\,dx\,ds.
\end{split}
\tag{18}
\]

The signs follow by contracting dt dx ds dh in the positive
t,x,s,h directions: respectively dx ds dh, -dt ds dh,
+dt dx dh, -dt dx ds. The interior phi_s term is retained.

Let epsilon,eta tend to zero along any joint sequence. The bulk
integrands are dominated by a fixed multiple of sqrt(t)+t^(3/2)
on the full finite box. Their indicators converge almost everywhere,
so dominated convergence works along every such sequence. The
lower-time integral has modulus at most C epsilon^(3/2), regardless
of eta, and tends to zero. The upper-time term converges by its
bounded fixed-T majorant as the omitted h interval shrinks.

The x-side and s-endpoint terms converge on their fixed full faces
using (5), with the two cutoff indicators; the outer-h terms converge
using their integrable time majorant. This justifies every retained
exceptional slice individually.

For an inner-h term, first compare its integral over [epsilon,T]
with the entire-face integral over [0,T]. The error is bounded by
C epsilon^(5/2), uniformly in eta. The latter entire-face integrals
converge in L1 as proved above. Thus this comparison, rather than
an iterated-limit assumption, proves that the inner contribution in
(18) tends to

\[
\int_{[0,T]\times[-X,X]\times[-1,1]}
 \phi(t,x,s,0)(V_0^+-V_0^-)\,dt\,dx\,ds.
\tag{19}
\]

Consequently (18) holds in the limit with all its other faces
retained, its lower-time term zero and (19) the prescribed inner
trace. There is no residual joint-corner term: every term of the
exact cutoff identity has its stated limit for arbitrary relative
cutoff rates. The same proof even allows distinct eta_+,eta_- and
different positive lower-time cutoffs on the two components. It uses
fixed tests, not derivatives of shrinking cutoff functions.

The face matches in (17)–(19) permit local pair/triple assembly when
the tests match. They supply no independent positivity or payment of
the lateral terms of (18). All unproved global obligations stated in
the conclusion remain separate.

### Independent conceptual audit — 16 November 2026, step1041

The invocation-start SPECIALIZE gate is
`drafts/literature/2026-11-16-reverse-pair-joint-extension-audit-nomination-1039.md`,
separately approved in review1040. This REPRODUCTION audit checks the
complete statement above using the already inspected standard imports.
It makes no originality claim and does not extend their scope. The
direct mathematical inputs remain C467e/audit1017, C467j/audit1029,
C467k/audit1033 and C467l/audit1037. Their inherited C467i/audit1025
and C466z/audit988,C466/audit993 qualifications are unchanged. The
analytic argument does not use C466a's externally imported density;
any such interpretation still carries its critical-strip, symmetry,
paired-product, counting and verified-low-zero qualifications.

**Common domain and the prelimit gap.** C467e(18)–(22) constructs
a smooth real coefficient field on an open neighborhood of the closed
initial coefficient box, including its discriminant. Since
|x+h|<=3/256<a and |x|<=1/256, the closed family e(x,x,x+h)
and sufficiently close distinct approximations lie strictly inside
that box. Smooth dependence on a slightly larger compact set bounds
all first t,x,h coefficient derivatives used here. The coefficients
of P are real and smooth there. This assertion concerns coefficient
variables, not smooth individual roots at t=0. C467l's separation
and ordered limiting argument identifies those roots and their
derivatives only at positive time, on both sides of h=0.

For distinct initial data with 0<delta<2|h|, the paired slots are
adjacent in imaginary order. Subtracting the actual imaginary
equations gives (7); the other adjacent gap has the same three
interaction terms with its indices exchanged. The negative term can
be discarded for this upper bound, and 2c_13/(alpha_1+alpha_2)
is at most 2/alpha_j. The background difference has upper bound
41alpha_j, so (alpha_j^2)'<=12+82alpha_j^2 follows for either gap.
Multiplying by exp(-82t) and integrating gives exactly (8).
This calculation is on the distinct-data flow, where the order is
preserved; no derivative on an initial collision is taken.

Now let delta tend to zero with x,h fixed. The initial paired gap
is delta whether h is positive or negative. C467l's coefficient and
ordered-root convergence passes (8) to that pair. Since
(exp(82t)-1)/82<=t exp(82t) and 82T_0=41/960<1/2,
alpha^2<=12t exp(82t)<24t. The already proved minimum-gap
bound is sqrt(t) for each adjacent gap. Hence alpha/b<5 and
c/b=1+alpha/b<6, proving precisely (9). Uniformity is inherited
before the limit, so no lower bound on |h|/sqrt(t) has entered.
The radial bound also gives b,c<=2r_* and bc<=3/40. Taking the
minimum of the finitely many compact-domain times gives one positive
tau; it remains existential and need not equal T_0.

**Original weight and both determinant cancellations.** The exact
secant bound gives |d|<=sqrt(1+kappa^2)alpha/2. Each of the two
singleton-to-segment vectors is a nonnegative convex combination
of actual singleton-to-pair vectors, including at s=+-1. Their
moduli are therefore at most sqrt(1+kappa^2)c for either h sign.
The original Vandermonde, without division by F, gives
|F(Z)|<=C s^2 alpha^2 c^4. The finite factor exp(-H_0) and the
bound |sum beta(Z_j)|<=3/8 are included in C. As c/b<6,
this proves (11) with a constant independent of h,t,s,x, also at
s=0. It is an absolute bound on an algebraic square, not a change
of the differential form to a modulus-square weight.

Summing P(q_j)+iq_j and using sum q_j^2=E_1^2-2E_2 verifies
(12), so S_r is bounded. For the singleton, which is extreme on
either side, Q'(q_3)=(q_3-q_1)(q_3-q_2)=bc>0. Differentiating
Q(q_3)=0 gives the positive numerator (q_3^2,-q_3,1)E_r in
(13). The coefficient derivative P_r and root derivative P_v q_r
are both present in w_r. The bounded upper value of bc absorbs
the bounded P_r term, proving |w_r|<=C/(bc). Substitution of
m=(S-w)/2 cancels w_r w_v exactly in J_rv. Thus (14) has one
inverse bc, not its square.

Expansion of dz_1 wedge dz_2=2dm wedge(s dd+d ds), followed by
i^(-3)=i, gives A=2iFdJ_xh, U=2iFdJ_th and V=-2iFdJ_tx.
All x derivatives in these formulas hold h fixed. The bounds are
therefore C s^2 alpha^3 bc<=C' s^2 t^(3/2), including their
values on s=0. In the old independent x,y coordinates, dy=dx+dh
turns U_old dt ds dy into U_old dt ds dh-U_old dt dx ds.
Consequently V_new=V_old-U_old, in agreement with J_tx computed
using partial_x+partial_y. This checks the coordinate change in the
time minor, not only in the spatial determinant.

For the remaining coefficient, R_q is diagonal with entries
P_v(q_j)+i, with P_v(q_j) real. Their moduli are at least one
and bounded above on the compact coefficient/root set. Thus R_q
and R_q^(-1) are uniformly bounded. The identities
q_r=J_q^(-1)E_r and Y_r=R_q q_r+a_r give (15) exactly.
The matrix J_q is polynomial in bounded roots and det J_q=-Delta(q).
Every entry in each bracket of (15) is bounded for r=t,x,h.
Factoring the same matrix R_q J_q^(-1) out of all three columns
therefore leaves precisely one inverse Delta in (16). This does
not assume bounded root derivatives or invertibility at t=0.
At fixed s, det M_s=s gives B_c=iFs det(Y_t,Y_x,Y_h);
(11),(16) imply |B_c|<=C|s|^3 alpha bc<=C'|s|^3 sqrt(t).
Thus both parts of (5) pass with the original complex form.

**All fixed faces and moving traces.** The estimates just checked
are pointwise on the full closed x,s parameter intervals and on
each closed nonzero-h component. A neighborhood is available at
their endpoints by the strict initial and analytic-domain margins.
At a positive time the roots are simple, so positive-cutoff maps
are smooth on a neighborhood of each box; extension a little past
s=+-1 preserves the analytic domain by its strict compact margin.
Thus Conrad's smooth Stokes hypotheses hold, including at s=0
where only the weight vanishes. No immersion assumption is needed.

The x faces use U, the s faces use B_c and the outer h faces
use V. Each has its own integrable bound from (5), valid at the
specified endpoint rather than only for almost every slice. The
upper t face uses bounded A at fixed T; the whole lower t face
has absolute integral at most C epsilon^(3/2), independently of
any removed central h interval.

For t>0, ordered simple-root charts and smooth coefficient dependence
identify the two h limits with exactly (17). Differentiation in x
at fixed h tends to the derivative along e(x,x,x); hence the entire
t,x,s maps and their tangential derivatives converge. This proves
pointwise convergence of V on each moving face, including fixed x
endpoints. Its uniform majorant C s^2 t^(3/2) and the same bound
for the limit give DCT for the absolute coefficient difference on
the full finite (t,x,s) face. For bounded smooth fixed tests the
change from phi(t,x,s,+-eta) to phi(t,x,s,0) tends uniformly to
zero; the other factor has a uniform L1 bound. The missing time
tail is bounded by a constant times integral_0^epsilon t^(3/2)dt,
namely O(epsilon^(5/2)), uniformly in eta and on the limit face.

**Six full oriented edges.** Reading slot orders as output orders,
the endpoint lists at s=1 and s=-1 are respectively

| j | side and output order | s=1 | s=-1 |
|---|---|---|---|
| 0 | h>0, (1,2,3) | (v1,v2,v3) | (v2,v1,v3) |
| 1 | h<0, (1,3,2) | (v2,v1,v3) | (v3,v1,v2) |
| 2 | h>0, (3,1,2) | (v3,v1,v2) | (v3,v2,v1) |
| 3 | h<0, (2,1,3) | (v3,v2,v1) | (v2,v3,v1) |
| 4 | h>0, (2,3,1) | (v2,v3,v1) | (v1,v3,v2) |
| 5 | h<0, (3,2,1) | (v1,v3,v2) | (v1,v2,v3) |

They are V_j,V_(j+1) in C467k's order, including the last join.
Since each map is affine in s, substitution s=1-2lambda gives
the whole segment, with equal t,x,lambda derivatives. Contraction
in the last coordinate of epsilon_sigma dt dx ds dh gives
+epsilon_sigma dt dx ds at the inner face of h>0 and
-epsilon_sigma dt dx ds at that of h<0. The listed lower-pair
permutations are even and the upper-pair permutations odd. Thus
all six inner orientations are positive in (t,x,s), becoming
negative in (t,x,lambda). The triangle r=1 orientation is positive
in (t,x,lambda). If V_sigma is the actual permuted pair coefficient,
the triangle edge coefficient is exactly -2 V_sigma(t,x,1-2lambda),
whereas integration on the positively oriented s face gives
+2 integral_0^1 V_sigma(t,x,1-2lambda)dlambda. This explicitly
checks cancellation of the full forms and the factor 2. The target
permutation is already included in V_sigma; no extra parity is
discarded or applied twice. Tests must match under the same map.
Multiplying every piece by the common minus sign preserves this.

**Tested limit and verdict.** Closedness of the holomorphic top
form gives dPsi=0 without excluding its divisor. Direct expansion
of dphi wedge Psi gives phi_t A-phi_x U+phi_s B_c-phi_h V;
contraction of the box orientation gives exactly the four boundary
lines of (18). In particular the inner contributions are
+phi V at h=eta and -phi V at h=-eta. DCT on the full bulk and
on each fixed lateral face applies to the two cutoff indicators,
with the integrable bounds already checked. The upper-time face
converges by its bounded majorant and the lower face tends to zero.
For either moving h face, comparison with its entire [0,T] integral
costs at most C epsilon^(5/2) independent of eta, and the entire
integral has its proved L1 limit. This yields (19) along every
joint sequence epsilon,eta tending to zero. The same separate
bounds allow independent cutoffs on the two components.

All local conclusions pass with unchanged hypotheses and constants.
Every term in the exact cutoff identity has been accounted for;
there is no unexplained joint-corner remainder for these fixed smooth
tests. This is validation of the existing local extension, not a new
theorem beyond the sources checked or a complete RH candidate.
No lateral payment, matched global construction, density realization,
all-degree sign or Xi transfer is supplied. The audited stops1009
and1023 keep their original scopes. No numerical experiment or
mathematical script is needed for this analytic audit.

## Mathlib

Full matching coverage for this actual weighted pair family, its
mixed minors and its oriented joint limit has not been checked; no
absence assertion or formal verification is made. The supporting
dominated-convergence locator reused in assessment1037/review1038 is
[`MeasureTheory.tendsto_integral_of_dominated_convergence`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
It does not supply the estimates (9),(11),(14),(16) or the face
identifications. The named standard analytic inputs and their precise
citations are given above.
Audit1041 is an informal conceptual verification of this written
argument, not a Lean proof or a new Mathlib coverage determination.
