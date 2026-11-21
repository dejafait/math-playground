# Lemma 870: a full zero-fiber closure lift still permits a negative Green form

## Hypotheses

Let ell be real and H>0. Set phi=pi modulo 2pi. This is exactly
the phase of C868b's chosen actual zero a=-4 gamma^2; its ell is
therefore included. Write X=x1-ell, Y=x2-ell, and
T2=(R/(2pi Z))^2. Normalize angular Fourier coefficients by

\[
 \widehat h_n(x)=(2\pi)^{-2}\int_{[0,2\pi]^2}
                   h(x,y)e^{-i n\cdot y}\,dy.
 \tag{1}
\]

The class under test is exactly L869(1)-(3)'s package, with
nonzero forcing frequencies restricted to

\[
 \pm(1,0),\quad\pm(0,1),\quad\pm(1,1),\quad\pm(1,-1).
 \tag{2}
\]

Thus h must be real, globally C1, periodic and nonnegative, with
mean m satisfying m(s,s)=m(ell,s)=H. Each nonzero coefficient
must be U_n(n dot x), for a compactly supported C1 profile with
|U_n|<=H, U_(-n)(t)=overline(U_n(-t)), and U_n=B_n-B_n'' for
some C3 profile B_n. All the opposite-index tests in L869(3)
are retained, with their zero coefficient H.

In addition there must be real global C1 periodic q,r satisfying

\[
 r_{x_j}=q_{y_j},\qquad(q+h)_{x_j}=-r_{y_j}\quad(j=1,2),
 \qquad
 q((\ell,s),(\pi,v))=r((\ell,s),(\pi,v))=0
 \quad(s,v\in\mathbb R).
 \tag{3}
\]

The allowed class imposes no growth or bandwidth restriction on
q,r, no restriction on homogeneous lift modes, and no actual-F
domination or other zero/diagonal trace. The Green data under
test, independently of the lift's zero mode, are exactly

\[
 b_0=H,\qquad
 b_n(x)=\frac12\int_{\mathbb R}e^{-|n\cdot x-u|}U_n(u)\,du
          \quad(n\ne0).
 \tag{4}
\]

## Conclusion

For every ell and H>0 there are explicit h,q,r satisfying all
these conditions. At x*=(ell+12,ell+50), with the fixed order
E=(0,(1,0),(0,1),(1,1)) and c=(1,-1,-1,1), they satisfy

\[
 \sum_{j,l\in E}c_j\overline{c_l}\,b_{j-l}(x^*)<-H/6<0.
 \tag{5}
\]

Consequently the bounded-profile package together with both
closure equations and this entire actual-zero fiber does not
imply the specified joint Green positivity at mass H. This is
an explicit witness in the allowed unrestricted lift class;
constructing a finite-mode member does not restrict that class.

The separate conceptual audit of 6 November 2026 below accepts
the stated construction and strict bound. It is not a
counterexample to actual-F admissibility, the period bound
K>=-|M|, graph realization, actual-Xi signs or RH. The chosen
phase pi suffices for the gate-approved C868b test; no assertion
for other phases is needed or made here.

## Proof

### Sources, scope and the trace-driven choice

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-lift-first-variable-forcing-green-test.md`.
It covers this simultaneous forcing/lift test and the exact
negative-form threshold. The checked sources did not settle it;
that bounded comparison does not establish originality.

Reuse L869's elementary cutoff and scalar Green regularity.
The underlying resolvent input is Klaus-Jochen Engel and Rainer
Nagel, *One-Parameter Semigroups for Linear Evolution Equations*,
GTM194, Springer (2000),
[VI.4.1, proof (4.2)-(4.3), pp384-386](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf#page=400).
Here every profile is continuous and compactly supported, hence
has the finite endpoint limits required there. L869(13)'s
split-integral calculation gives C3 regularity for C1 profiles.
This is reuse of the known scalar kernel, not a new resolvent
or existence theorem for the coupled system.

For the finite matrix criterion reuse Rajendra Bhatia,
*Positive Definite Matrices*, Princeton (2007),
[Section1.1, pp1-2](https://assets.press.princeton.edu/chapters/s8445.pdf).
The full real symmetric matrix and its quadratic form will be
computed below. No positivity inference comes from that citation.

C868b's proof (7) chooses a=-4 gamma^2<0 using the named Hardy
input, so phi=pi without an RH or simplicity assumption. That
phase selection is the only actual-zero fact used here. The
closure/profile interface of C868a and the tangential trace
obstruction of C869a motivate the construction; their stronger
actual-F hypotheses and the stopped fixed forcing are not assumed.
In particular, the paired profiles below impose cancellation on
the fiber before the forcing is chosen. The direct finite formulas
verify all of (3), rather than claiming sufficiency from just
h_x2=0 on the fiber. No general PDE extension or infinite Fourier
reconstruction is used.

### Cutoffs, profiles and the forcing

Use L869's even cutoff

\[
 p(t)=\begin{cases}
 1,&|t|\leq2,\\
 1-3v^2+2v^3,\quad v=|t|-2,&2<|t|<3,\\
 0,&|t|\geq3.
 \end{cases}
 \tag{6}
\]

It is C1, 0<=p<=1, supported on [-3,3], with |p'|<=3/2.
Its derivative is globally Lipschitz with constant 6: on each
open polynomial piece |p''|<=6, and p' agrees continuously at
all junctions. Partitioning a finite interval at those junctions
and adding the piecewise derivative bounds proves this global
claim, including intervals crossing a junction. No C2 regularity
at the junctions is asserted.

Set beta=6/25 and define

\[
 \alpha(t)=\tfrac12\{p(t)+p(t-12)\},\qquad
 f(t)=\beta\{p(t-50)-p(t-38)-p(t-62)\}.
 \tag{7}
\]

The two supports in alpha and the three supports in f are
pairwise disjoint within each respective sum. Thus

\[
 0\leq\alpha\leq\tfrac12,\qquad
 |f|\leq\tfrac6{25},\qquad |f'|\leq\tfrac9{25},\qquad
 \operatorname{Lip}(f')\leq\tfrac{36}{25}.
 \tag{8}
\]

For the last bound, partition at all translated cutoff junctions.
At each point in an open piece at most one translated p contributes;
its second derivative has magnitude at most 6 beta. The derivatives
are continuous across the finitely many junctions. Adding the
piecewise bounds gives (8), not three times that constant.

Define the radial mean and forcing by

\[
 \begin{split}
 m(x)&=H\{1+30X^2(X-Y)^2\},\\
 h(x,y)&=m(x)+H\{2\alpha(X)\cos y_1+4f(Y)\cos y_2\\
 &\hspace{35mm}+2f(X+Y)\cos(y_1+y_2)
                   +2f(Y-X)\cos(y_1-y_2)\}.
 \end{split}
 \tag{9}
\]

These functions are real C1, and h is angularly periodic. Its
angular mean is exactly m. The formula gives m(s,s)=H and
m(ell,s)=H for every finite real s. Its radial growth is allowed
by the hypotheses; no bounded zero mode is being imposed.

The positive-index profiles are

\[
 \begin{split}
 U_{(1,0)}(t)&=H\alpha(t-\ell),&
 U_{(0,1)}(t)&=2Hf(t-\ell),\\
 U_{(1,1)}(t)&=Hf(t-2\ell),&
 U_{(1,-1)}(t)&=Hf(-t).
 \end{split}
 \tag{10}
\]

Define U_(-n)(t)=U_n(-t) for these four indices, and U_n=0
for all other nonzero n. All are real C1 compactly supported
profiles; (9) gives precisely hhat_n(x)=U_n(n dot x).
Their magnitude bounds are respectively H/2, 12H/25, 6H/25
and 6H/25, each <=H. This also verifies the required reality
relation for every n and every t.

### Global nonnegativity, including the two mean lines

Let g(x,y) denote the expression h/H with the mean m/H
replaced by 1. From (8), everywhere

\[
 g\geq1-1-4\beta-2\beta-2\beta=-48/25.
 \tag{11}
\]

First suppose |X-Y|<=1. The term f(Y-X) vanishes because
f is supported in [35,41] union [47,53] union [59,65].
At most one of alpha(X), f(Y), f(X+Y) is nonzero:

- If alpha(X) is nonzero, X is in [-3,3] union [9,15].
  Then Y is in [-4,16] and X+Y is in [-7,31], outside
  f's support.
- If f(Y) is nonzero, Y>=35 and X>=34. Hence alpha(X)=0
  and X+Y>=69, so f(X+Y)=0.
- If f(X+Y) is nonzero, 35<=X+Y<=65 and |X-Y|<=1 give
  17<=X,Y<=33. Hence alpha(X)=f(Y)=0.

The absolute amplitudes of the single possible cosine are at most
1, 24/25 and 12/25 respectively. Thus g>=0 on this entire strip.
All endpoint cases are included, with the cutoffs zero at their
outer endpoints. Since m/H>=1, h>=0 there.

Next suppose |X|<=1, without restricting Y. Then alpha(X)=1/2.
The fundamental theorem of calculus and (8) give

\[
 f(Y\pm X)=f(Y)\pm X f'(Y)+E_\pm,
 \qquad |E_\pm|\leq\frac{18}{25}X^2.
 \tag{12}
\]

Indeed, integrate f'(Y+t)-f'(Y) over the interval from 0 to
plus or minus X and use its Lipschitz bound. This argument uses
only C1 regularity and that bound. Substitution into g yields

\[
 \begin{split}
 g={}&(1+\cos y_1)(1+4f(Y)\cos y_2)
        -4Xf'(Y)\sin y_1\sin y_2+R,\\
 |R|&\leq72X^2/25.
 \end{split}
 \tag{13}
\]

The first factorization uses the sum and difference formulas for
cosines; R consists of exactly the two error terms 2E_+ and
2E_- times their cosines. Since 1+4f(Y)cos(y2)>=1/25 and
sin^2(y1)<=2(1+cos(y1)), put sigma=|sin(y1)| to obtain

\[
 \begin{split}
 g&\geq \frac{\sigma^2}{50}
        -\frac{36}{25}|X|\sigma-\frac{72}{25}X^2\\
  &=\frac{(\sigma-36|X|)^2}{50}-\frac{144}{5}X^2
   \geq-\frac{144}{5}X^2.
 \end{split}
 \tag{14}
\]

If now |X-Y|>1, the mean correction in (9) is at least
30 X^2, which dominates (144/5)X^2. Therefore h>=0 in
this second region also. In the only remaining region,
|X|>1 and |X-Y|>1, the correction is >30 and (11) applies,
so h/H>30-48/25>0. These three regions cover all radial points
and every angle. Thus (9) is one globally nonnegative forcing,
not merely separate admissible coefficient choices.

### All opposite-index tests and the C3 profile relation

At a fixed x the subgroup coefficients are a_0=H,
a_1=a_(-1)=H f(Y-X), and a_k=0 for |k|>=2. They are the
circle Fourier coefficients of

\[
 \rho_x(\theta)=H\{1+2f(Y-X)\cos\theta\}\geq13H/25>0.
 \tag{15}
\]

Consequently for every N>=0 and every c_0,...,c_N in C,

\[
 \sum_{j,l=0}^N c_j\overline{c_l}a_{j-l}
 =\frac1{2\pi}\int_0^{2\pi}\rho_x(\theta)
       \left|\sum_{j=0}^N c_j e^{-ij\theta}\right|^2d\theta\geq0.
 \tag{16}
\]

This finite-sum identity verifies the entire required family.

Let G(t)=exp(-|t|)/2, A=G*alpha and V=G*f. For every n!=0
take B_n=G*U_n. L869(13), applied to the compact C1 profiles
(10), gives B_n in C3 and B_n''=B_n-U_n. In particular,

\[
 A''=A-\alpha,\qquad V''=V-f.
 \tag{17}
\]

The even real kernel preserves the stated reality relation.
These bounded particular solutions will construct one lift; no
claim is made that arbitrary lifts lack homogeneous terms.

### A complete global lift and its entire zero-fiber trace

Set K=H(1+2A''(0)) and define the finite expressions

\[
 \begin{split}
 q={}&K-m+2HA''(X)\cos y_1+4HV''(Y)\cos y_2\\
    &+2HV''(X+Y)\cos(y_1+y_2)
                       +2HV''(Y-X)\cos(y_1-y_2),\\
 r={}&-2HA'(X)\sin y_1-4HV'(Y)\sin y_2\\
    &-2HV'(X+Y)\sin(y_1+y_2)
                       +2HV'(Y-X)\sin(y_1-y_2).
 \end{split}
 \tag{18}
\]

They are real global C1 periodic functions by (17); in particular
the first derivatives of q use at most the continuous third
derivatives of A,V. The zero mode K-m is permitted to grow.
Equation (17) makes S=q+h equal to the corresponding finite sum
with A,V in place of A'',V'', and zero mode K.

For a nonzero index n, a real C3 profile B(t), t=n dot x,
and theta=n dot y, the three terms

\[
 S_n^{\rm pair}=2B(t)\cos\theta,\quad
 q_n^{\rm pair}=2B''(t)\cos\theta,\quad
 r_n^{\rm pair}=-2B'(t)\sin\theta
 \tag{19}
\]

satisfy, for each j,
r_xj=-2 n_j B'' sin(theta)=q_yj and
S_xj=2 n_j B' cos(theta)=-r_yj. Each pair in (18) has this
form, including n=(1,-1) with B(t)=H V(-t); the latter
reflection accounts for the plus sign of its sine term in r.
The constant zero modes of S and r and the angularly constant
zero mode of q also satisfy both equations. Adding these finite
identities proves every closure equation in (3) on the full domain.

On the prescribed fiber, X=0, Y=s-ell, y1=pi, y2=v,
the second-frequency terms of q in (18) have coefficients
4-2-2=0 times H V''(Y)cos(v). Hence

\[
 q((\ell,s),(\pi,v))=K-H-2HA''(0)=0.
 \tag{20}
\]

The first sine term of r vanishes. The other sine terms have
coefficients -4+2+2=0 times H V'(Y)sin(v), because
sin(pi+v)=-sin(v) and sin(pi-v)=sin(v). Thus r=0 on
the same entire fiber. Both identities hold for every finite
real s and every v, not just for an angular mean or one radial
point. Formula (9) also gives h=0 there, consistently with
nonnegativity and C869a's necessary tangential identity.

No other modes are needed for this witness. The proof does not
exclude them from the admissible class and does not use uniqueness
of the lift. It verifies an explicit member of the full class.

### The exact prescribed-mass Green form

Write kappa_d=(G*p)(d). Evenness gives kappa_(-d)=kappa_d,
and 0<=kappa_d<=1 since 0<=p<=1 and the kernel has integral 1.
The plateau in (6), as in L869(15), gives

\[
 \kappa_0\geq1-e^{-2}>6/7.
 \tag{21}
\]

For the one required tail, support in [-3,3] gives

\[
 \kappa_{12}\leq\tfrac12\int_{-3}^{3}e^{-(12-u)}\,du
   =\tfrac12(e^{-9}-e^{-15})<\tfrac12e^{-9}<1/1024.
 \tag{22}
\]

The last inequality follows from e>2 and hence e^9>2^9.
These are exact inequalities, not rounded numerical values.

At X=12,Y=50 the four positive-frequency Green entries, divided
by H, are

\[
 \begin{split}
 \eta_1&=\tfrac12(\kappa_0+\kappa_{12}),\\
 \eta_2&=\tfrac{12}{25}(\kappa_0-2\kappa_{12}),\\
 \eta_3&=\eta_4=\tfrac6{25}
               (\kappa_{12}-\kappa_0-\kappa_{24}).
 \end{split}
 \tag{23}
\]

Here the fourth entry is V(Y-X)=V(38), while the third is
V(X+Y)=V(62); their equality uses the two equally weighted
negative bumps at 38 and 62. Translation and reflection in
(10) commute with convolution by the even kernel, justifying
these evaluations. All entries are real, including the negative
indices. In the stated order E, the full matrix is

\[
 [b_{j-l}(x^*)]_{j,l\in E}
 =H\begin{pmatrix}
 1&\eta_1&\eta_2&\eta_3\\
 \eta_1&1&\eta_4&\eta_2\\
 \eta_2&\eta_4&1&\eta_1\\
 \eta_3&\eta_2&\eta_1&1
 \end{pmatrix}.
 \tag{24}
\]

For c=(1,-1,-1,1), its quadratic form is exactly

\[
 \begin{split}
 c^*Bc/H
 &=4-4\eta_1-4\eta_2+2\eta_3+2\eta_4\\
 &=4-\tfrac{122}{25}\kappa_0
       +\tfrac{14}{5}\kappa_{12}-\tfrac{24}{25}\kappa_{24}\\
 &<-\tfrac{32}{175}+\tfrac7{2560}<-\tfrac16.
 \end{split}
 \tag{25}
\]

The first equality counts each unordered off-diagonal pair twice.
The last line uses (21)-(22) and kappa_24>=0; its final comparison
is equivalent to 17/1050>7/2560. Thus (5) follows with its
prescribed zero coefficient H. The constant K in the closure
lift is not substituted for that coefficient.

All required conditions now hold for the same h,q,r and profiles.
The provisional amplitude 1/8 in the working record was discarded
after an off-diagonal factor-of-two error was found; the corrected
amplitude 6/25, global bounds and matrix above are the claimed
result. The preserved working record is
`drafts/2026-11-06-lift-first-variable-forcing-working.md`.
No script, sampled eigenvalue, unstated series differentiation or
limit interchange supplies any part of the strict inequality.

This countermodel stops the implication from the stated stronger
package to (4)'s joint positivity. It leaves actual-F domination,
all other zeros and the actual diagonal pointwise trace unresolved;
the two mean lines do not replace them. It establishes neither
sign of a period advantage nor a statement about actual-Xi zeros.

### Independent conceptual audit, 6 November 2026

The prior EXPLORE assessment
`drafts/literature/2026-11-06-lift-first-green-countermodel-audit.md`
approved exactly this audit. The result passes for every real ell
and H>0 with phase pi. This verifies the submitted countermodel;
it is not an additional counterexample or a claim of originality.
The preliminary doubled pair count is not used. The complete
check follows, including the global rather than sampled inequalities.

**Regularity and the calculus inputs.** On the transition interval,
p has derivative 6v(v-1), with magnitude at most 3/2, and second
derivative -6+12v, with magnitude at most 6. Reflection changes
the first derivative's sign without increasing either bound.
The values and first derivatives agree with the constant pieces
at +/-2 and +/-3; p is constant near 0. Thus p is C1, not
asserted C2. The two alpha supports are [-3,3] and [9,15]; the
three f supports are [35,41], [47,53], [59,65]. Each family is
disjoint, so no overlapping derivatives increase the bounds in (8).
Partitioning any finite interval at every translated junction and
adding its piecewise Lipschitz estimates gives Lip(f')<=36/25.

This uses the inspected standard inputs in Jiří Lebl, *Basic
Analysis I*, author HTML accessed 2026-11-06:
[Theorem4.2.4](https://www.jirka.org/ra/html/sec_mvt.html) (mean
value theorem for a continuous function on a closed interval,
differentiable in its interior), and
[Theorems5.3.1,5.3.3](https://www.jirka.org/ra/html/sec_ftc.html)
(fundamental calculus, with integrable derivative and continuity
at the point of differentiation, respectively). On each closed
polynomial piece f' is continuous and differentiable in the
interior, so the mean value theorem applies there. The finitely
many matching junction values allow the estimates to be added.
Since f is C1, integrate f'(Y+t)-f'(Y) along either orientation
to obtain (12), with remainder <=(36/25)|X|^2/2. These are
applications of the imported theorems; no C2 junction, infinite
differentiation or new Taylor theorem is being assumed.

**All radial regions.** In |X-Y|<=1, f(Y-X)=0. If alpha(X)
is nonzero, Y lies in [-4,16] and X+Y in [-7,31], outside
the f supports. If f(Y) is nonzero, X>=34 and X+Y>=69;
if f(X+Y) is nonzero, both X,Y lie in [17,33]. These checks
leave at most one nonzero term, with amplitude <=1, 24/25 or
12/25. Hence g>=0 on the closed strip. In |X|<=1, alpha=1/2,
and the two remainders in (12) contribute at most 72X^2/25
to (13). The coefficient 1+4f(Y)cos(y2) is at least 1/25.
Consequently the completed square in (14) is exact: its X^2
cost is 1296/50+72/25=144/5. Outside the diagonal strip,
30X^2(X-Y)^2 is at least 30X^2, exceeding this cost whenever
X!=0; when X=0 both costs vanish. In the remaining open region
|X|>1, |X-Y|>1, the correction is >30 while g>=-48/25.
This covers every boundary and every angle. The mean identities
hold because X=Y on (s,s) and X=0 on (ell,s). Thus the same
global C1 function is nonnegative and has both required means.

**Every coefficient and the entire subgroup family.** Expansion
of each cosine gives exactly (10), with absolute bounds
H/2, 12H/25, 6H/25, 6H/25. In the last profile,
t=x1-x2=X-Y, so f(-t)=f(Y-X). Reflection supplies all four
negative indices with the required conjugacy; every remaining
nonzero index has the zero compact C1 profile. For (k,-k),
only k=+/-1 can contribute. Thus (15) has exactly these
coefficients with zero coefficient H and is >=13H/25.
Expanding the finite squared modulus in (16) verifies every
N and every complex vector, with the stated Fourier convention.
This does not replace H by the generally larger actual mean m.

For each of these profiles the absolutely convergent split
integrals in L869(13) have derivatives U-A and D-U. Their sum
gives B''=B-U and B'''=B'-U'. All are continuous, including
at the cutoff junctions. Hence B is C3 and (17) applies globally.
The compact C1 data meet the cited scalar resolvent hypotheses;
neither its uniqueness nor a coupled PDE existence theorem is
used. Translation and reflection commute with convolution by
the even real kernel, by changing its integration variable.

**Both closure equations and the complete trace.** For j=1,2,
differentiating (19) gives respectively
r_xj=-2n_j B'' sin(theta)=q_yj and
-r_yj=2n_j B' cos(theta)=S_xj. This also holds when n_j=0.
For n=(1,-1), B(t)=H V(-t) has derivative -H V'(-t),
which produces the plus sign in (18)'s last sine term.
The zero mode of S is K, so its radial derivatives vanish;
the angular derivatives of K-m vanish. Thus no unaccounted
derivative of m enters closure. All first derivatives of q,r
are continuous since B is C3 and m is a polynomial.

On X=0,y1=pi, the three q terms involving V''(Y)cos(v)
have weights 4,-2,-2. Their sum is zero for every Y,v, while
K-H-2HA''(0)=0. The first sine term vanishes, and the other
r terms have weights -4,2,2, using both sin(pi+v)=-sin(v)
and sin(pi-v)=sin(v). Thus both functions vanish on the
entire fiber. Direct substitution in h also gives zero there.
C868b(7)'s already audited Hardy specialization supplies the
actual negative zero and phase pi without any RH or simplicity
assumption. Ell enters only by translation. No restriction of
the allowed homogeneous modes, or uniqueness of this lift, is
needed for an existence witness.

**Actual matrix and strict margin.** At (X,Y)=(12,50), the
four entries are A(12), 2V(50), V(62), V(38), all multiplied
by H. Substitution into the three shifted bumps gives (23):
V(62)=V(38)=6(kappa12-kappa0-kappa24)/25. The six unordered
pairs in E have values eta1,eta2,eta3,eta4,eta2,eta1 and
products of vector components -1,-1,+1,+1,-1,-1. Counting
each pair twice gives precisely -4,-4,+2,+2 for the four
distinct entries and diagonal contribution 4. The resulting
coefficients of kappa0,kappa12,kappa24 are -122/25,14/5,-24/25.
These checks establish the entire matrix (24), not a selected
minor or a numerically sampled eigenvalue.

The plateau gives kappa0>=1-e^(-2)>6/7, since the first five
terms of the exponential series sum to 7 and the remaining
terms are positive. The support bound gives
0<=kappa12<e^(-9)/2<1/1024, since e>2, and kappa24>=0.
Hence the audited bound is

\[
 \frac{c^*Bc}{H}
 <-\frac{32}{175}+\frac7{2560}
 =-\frac16-\frac{3617}{268800}<-\frac16.
\]

The diagonal is H throughout this computation, independently
of K. All inequalities are exact and uniform in ell and H>0.
No numerical certificate is required.

**Decision and scope.** Accept (5) and the route stop for the
stated relaxed package. The DAG inputs remain C868b for the
actual phase and L869 for the cutoff/Green facts; C868a and
C869a are motivation and contrasts, not additional premises.
The fixed-forcing obstruction in C869a is unaffected because
this is a different forcing. Actual-F domination, other zeros,
the actual diagonal pointwise trace, the period inequality,
graph realization and actual-Xi positivity remain unresolved.
The main RH gap is unchanged; only this local implication has
now been critically verified.

## Mathlib

Full matching coverage is unchecked; no absence claim is made.
The reused sources supply the scalar Green kernel, elementary
calculus and finite Hermitian criterion. The finite cutoff, global bounds, explicit
closure identities and exact form are proved above. No Mathlib
theorem or numerical certificate is being asserted as verification
of this simultaneous construction.
