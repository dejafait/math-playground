# Corollary 919o: a positive inverse kernel after two specified real-zero pairs

## Hypotheses

Use the actual entire Xi of L018, the theta kernel K of L019, and
L058's normalization Xi(z)=integral_0^infinity K(u)cos(zu)du. For the
quotient conclusion assume actual real roots x,y with

    14<x<29/2, 21<y<22, Xi(x)=Xi(y)=0.

They are distinct by these brackets. Multiplicities are unrestricted;
no first-zero, simplicity, census, or existence assertion for y is used.
Use the accepted analytic one-removal result C919m and the complete-tail
and arithmetic contracts of accepted C919f. C919n is context only.

The numerical compact sign below assumes correct CPython integer and
Fraction arithmetic and libmpdec directed basic operations, representable
neighbors and correctly rounded HALF_EVEN exp. Actual evaluator runtime:
CPython3.15.2/libmpdec4.0.1, precision80. These are explicit backend trust
assumptions, not independently verified backend theorems. Import the
Simpson, real Taylor, theta-shape and Fourier tools cited below.

## Conclusion

For u>=0 define

    G_a(u)=a integral_0^infinity K(u+t)sin(at)dt,
    H_xy(u)=y integral_0^infinity G_x(u+t)sin(yt)dt.           (1)

For all real parameters in the stronger closed box
x in[14,29/2], y in[21,22], without a root premise, the half-line
trial satisfies

    H_xy(u)>69/10^10   (0<=u<=1),
    H_xy(u)>0         (u>=1).                               (2)

For the actual roots in the hypotheses, H_xy extends evenly to a smooth
strictly positive function on R. Every derivative decays faster than
every fixed exponential, and for every integer m,p>=0 and real B>=0,

    integral_0^infinity (1+u)^p exp(Bu)|H_xy^(m)(u)|du<infinity.

Its cosine transform is entire and is exactly

    R_xy(z)=integral_0^infinity H_xy(u)cos(zu)du
           =Xi(z)/((1-z^2/x^2)(1-z^2/y^2)),                 (3)

with all four apparent poles removable, including at multiple roots.
On the real axis R_xy is integrable, and for every real u,

    H_xy(|u|)=(2/pi) integral_0^infinity R_xy(v)cos(vu)dv.     (4)

This is a finite, source-covered REPRODUCTION specialization. It is
not an all-order closure theorem or a claim of progress beyond the
literature assessed. The proof and certificate received the separate
qualified critical acceptance2238 below. No RH candidate is asserted;
y-existence, arbitrary further removals, uniformity in a growing number
of roots, and L030-L032/C032a's all-degree algebraic mixed signs remain
unproved here.

## Proof

### Imported inputs and their scope

C919m imports the classical theta-shape theorem: G. Csordas,
*Fourier transforms of positive definite kernels and the Riemann
xi-function*, arXiv:1309.0055v2 (21 February2014), Theorem4.1 and
(4.2), printed p10, https://arxiv.org/pdf/1309.0055v2 . With its
normalization K(u)=4 Phi(u/2), K is smooth and even, positive and
strictly decreasing on[0,infinity), and all derivatives decay faster
than every exponential. Original Wintner/Spira proofs are not claimed
newly read. C919m also supplies the exact entire one-root quotient Q_x,
its smooth even inverse G_x, all derivative tails, and G_x'(0)=0.

The only positivity tool used in the exterior is the integrable,
continuous, strictly positive, strictly decreasing amplitude sine
criterion in E.O. Tuck, *On positivity of Fourier transforms*,
Bull. Austral. Math. Soc.74 (2006),133-138, pp133-134,(1)-(4);
https://doi.org/10.1017/S0004972700047511 . Direct primary PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf .
The complete same half-period proof is Csordas Remark3.11, printed p9.
That theorem says integral_0^infinity f(t)sin(at)dt>0 for a>0 under
these amplitude hypotheses. Positivity alone would be insufficient.

For numerical errors import composite Simpson's theorem for C4 real
functions on[a,b] with positive even panel count M:
error <=(b-a)^5 sup|f''''|/(180 M^4). Source: NIST DLMF3.5(ii),
(3.5.6)-(3.5.8), citing Davis--Rabinowitz(1984),pp57-58,
https://dlmf.nist.gov/3.5.ii . Import smooth real Taylor's theorem
with its Lagrange remainder from Strang--Herman, *Calculus Volume2*,
Section6.3,Theorem6.7,
https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series .
All finite integrands below are smooth. No complex Taylor remainder
or sampled derivative estimate is substituted for these hypotheses.

For the final transform/inversion use the same input as C919m:
T. Tao, *245C, Notes2: The Fourier transform* (6 April2009), Section3,
Exercise30, Remark31, inversion(11) and its proof,
https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ .
The required derivative integrability and absolute continuity are
verified below. ODE uniqueness uses the elementary homogeneous equation,
consistent with DLMF1.13(iii),(1.13.8)-(1.13.10),
https://dlmf.nist.gov/1.13.iii . These general tools are reused from
assessment2234/approval2235, not reproved or newly discovered.

### Exact half-line construction and all tails

For any fixed positive a, the arguments for the half-line sine integral
in C919m give, without needing a root,

    G_a'(u)=-a^2 integral_0^infinity K(u+t)cos(at)dt,
    G_a''(u)=a^2(K(u)-G_a(u)).                              (5)

Every derivative has an exponential bound of any prescribed rate:
start with |G_a|<=a T and |G_a'|<=a^2 T, where
T(u)=integral_u^infinity K(t)dt, then use (5) recursively and
C919m's bounds on K^(m). The defining integrals and each initial
Leibniz differentiation are dominated by fixed multiples of K on
compact u sets. These facts apply also to the nonroot numerical box.

The double integral defining H is absolutely convergent because

    xy integral_0^infinity integral_0^infinity K(u+r+s)dr ds
      =xy integral_0^infinity t K(u+t)dt<infinity.

Fubini is thus valid before any sign cancellation. Direct finite
trigonometric integration, or differentiation of both sides with the
same zero initial data, gives for x!=y

    integral_0^t sin(xr)sin(y(t-r))dr
       =(y sin(xt)-x sin(yt))/(y^2-x^2).

Consequently, putting d=y^2-x^2>0,

    H(u)=integral_0^infinity K(u+t)W_xy(t)dt,
    W_xy(t)=xy*(y sin(xt)-x sin(yt))/d,
    H(u)=(y^2 G_x(u)-x^2 G_y(u))/d.                         (6)

This is the full signed integral, not an absolute-value surrogate.
One-factor positivity alone does not sign the difference in (6).

Differentiating the iterated definition, using the complete tails for
G_x exactly as for (5), gives

    H'(u)=-y^2 integral_0^infinity G_x(u+t)cos(yt)dt,
    H''(u)+y^2 H(u)=y^2 G_x(u).                             (7)

For every B>0, integral_u^infinity |G_x(t)|dt<=C_B exp(-Bu).
Thus H and H' have such bounds. Recursion
H^(m+2)=y^2(G_x^(m)-H^(m)) supplies them for all m. Taking a rate
B+1 and integrating (1+u)^p exp(-u) proves the claimed weighted
integrability and every infinity endpoint limit. These are complete
infinite tails, uniform on compact complex-frequency sets; constants
may depend on x,y,m,p,B. No growing-index uniformity is asserted.
Any two decaying C2 solutions of (7) for this fixed G_x differ by
A cos(yu)+B sin(yu); evaluating along full and quarter periods forces
A=B=0. Hence no decaying homogeneous ambiguity has been retained.

### Both root conditions, smooth even extension, and the exact inverse

Now impose the actual roots. C919m gives the entire transform
Q_x(z)=Xi(z)/(1-z^2/x^2), with smooth even G_x and all odd origin
jets zero. Since y!=x and y>0, the second root implies Q_x(y)=0.
Equation(7) at the origin therefore yields

    H'(0)=-y^2 Q_x(y)=0.                                    (8)

This is derived from the actual second root; no numerical approximation
to a root or unproved origin boundary condition is used. The recursion
following(7), with odd m, and the zero odd jets of G_x show inductively
that every odd derivative of H at zero vanishes. Its even extension
is consequently smooth; H'' has no point mass at zero.

Let R(z)=integral_0^infinity H(u)cos(zu)du. Its derivatives on |z|<=A
are dominated by u^j exp(Au)|H(u)|. The complete tails prove local
uniform convergence and entire dependence. Twice integrating (7)
against cos(zu) gives

    integral_0^infinity H''(u)cos(zu)du=-z^2 R(z),
    (y^2-z^2)R(z)=y^2 Q_x(z).                              (9)

Indeed the first boundary term is -H'(0)=0 by(8), the second origin
term contains sin(0), and both infinity terms vanish at a rate
B>|Im z|. This pays the endpoints for every complex z, not just real z.
Substituting Q_x proves(3) away from the four roots; the entire integral
provides their removable extension. More explicitly the extension
values at +/-x equal

    -x Xi'(x)/(2*(1-x^2/y^2)),

and at +/-y equal

    -y Xi'(y)/(2*(1-y^2/x^2)).

Evenness makes the paired values equal. Each denominator zero is
simple and the brackets are disjoint. Thus a root of multiplicity m
is reduced exactly to m-1 at each of its two signs; if m>1 the displayed
value is zero. No simplicity, unknown product sign, or branch is used.

For real v, |R(v)|<=||H||_1 and, for v!=0, (9)'s integration by parts
gives |R(v)|<=||H''||_1/v^2. Hence R is integrable on R. The smooth
even extension f(u)=H(|u|) is continuous with f,f',f'' in L1 and
locally absolutely continuous derivatives. In Tao's Fourier convention,
hat f(eta)=2 R(2*pi*eta). The quoted inversion theorem applies to f
and its integrable transform. Substitution v=2*pi*eta and evenness
give(4) at every u. It also proves uniqueness in the continuous L1
inverse class. This establishes the quotient interpretation separately
from the sign certificate that follows.

### Analytic exterior on the prescribed ray

For each original theta summand write v=pi*n^2 exp(2u). Then

    K_n(u)=(8v^2-12v)exp(u/2-v),
    K_n''(u)=exp(u/2-v)*(32v^4-224v^3+330v^2-75v).           (10)

For u>=1, pi>3 and exp(2)>7 imply v>21. The latter inequality
follows from the positive exponential series through degree4, whose
sum at2 is7, followed by its strictly positive remaining terms. The
polynomial in(10) is

    v^3*(32v-224)+v*(330v-75)>0.

The two differentiations may be taken termwise on every compact
subinterval of[1,infinity): the differentiated summands are bounded
by a fixed polynomial in n times exp(-c n^2) there, with c>0, giving
uniform summability. The same applies through order2, so the sum's
second derivative is the displayed sum. Every summand is strictly
positive. Thus K''(u)>0 on the full ray u>=1. This is additive-coordinate
convexity, not an appeal to a square-coordinate theta shape theorem.

Fix u>=1. The amplitude f(t)=-K'(u+t) is continuous, positive,
strictly decreasing, and integrable, by K'<0, the just-proved K''>0,
and the complete derivative decay. Integration by parts with vanishing
sine endpoints gives

    integral_0^infinity K(u+t)cos(xt)dt
       =(1/x) integral_0^infinity [-K'(u+t)]sin(xt)dt>0

by Tuck's sine criterion. Equation(5) now proves G_x'(u)<0 throughout
this exterior. C919m's same sine criterion gives G_x(u)>0 even without
a root premise: the amplitude K(u+t) is positive strictly decreasing
and integrable. For this fixed u>=1, G_x(u+t) is therefore continuous,
positive, strictly decreasing in t, and integrable. Tuck at frequency
y>0 applied to(1) proves H_xy(u)>0. This pays the fixed exterior,
including u=1. It does not assume or assert G_x'<0 on the full half-line.

### Compact signed certificate and complete omitted regions

The fixed settings and unfinished reasoning were saved before the
numerical run in
`drafts/calculations/2026-11-21-direct-two-real-zero-work-2236.md`.
No setting was refined after observing values. Reproduction commands:

    python3 scripts/real-zero-origin/joint_kernel_2236.py
    python3 scripts/real-zero-origin/inspect_joint_kernel_2236.py

The evaluator uses U=4, theta indices1..4,65536 Simpson panels,
1024 closed derivative cells of width1/256 on[0,4], frequency Taylor
degree8 at c_x=57/4,c_y=43/2 with radii1/4,1/2,16 closed x cells,
32 closed y cells, and256 closed u cells of width1/256 on[0,1].
All endpoints are exact dyadic rationals, including shared boundaries.
The target fixed before the run was a uniform lower margin>10^(-10).

C919f equations(1),(2), at lambda=0 and0<=j<=9, give the complete
absolute bounds

    B_I(j)=15000000 exp(-75) j!/145^(j+1),
    B_T=(200/768)exp(-384)                                  (11)

for omitted indices n>=5 on[0,4] and all indices on t>=4,
respectively, with weight t^j. These are disjoint omitted regions;
together they cover every omitted part. The index proof's pointwise
majorant also gives sum_(n>=5)K_n(u)<=15000000 exp(-75) for0<=u<=4.
It follows from its stronger exp(-145u) factor, which may be discarded.
A pointwise tail, rather than an integrated one, is used for K(u).

For finite derivative bounds on a cell[l,r], write each summand as
the difference of
8 alpha_n^2 exp((9/2)t-alpha_n exp(2t)) and
12 alpha_n exp((5/2)t-alpha_n exp(2t)), alpha_n=pi*n^2.
Enclose v_n(t) in[v_lo,v_hi]. For either exponent coefficient b,
let E0=|prefactor|exp(b*r-v_lo) and
A1=b+2v_hi,A2=4v_hi,A3=8v_hi,A4=16v_hi. Its derivatives through4
are bounded in absolute value by E0 times

    1; A1; A1^2+A2; A1^3+3A1*A2+A3;
    A1^4+6A1^2*A2+3A2^2+4A1*A3+A4.

This is the finite differentiation formula for an exponential,
with absolute values applied to every derivative of its exponent.
Sum the bounds over both exponential terms and n=1,...,4 to get
E_0,...,E_4 on the whole closed cell. For t^j/j!, its s-th derivative
has magnitude <=r^(j-s)/(j-s)! for s<=j, and zero otherwise.
Two Leibniz rules therefore give, for either sine or cosine phase
at center c, the full fourth-derivative bound

    B_j,c=sum_(a=0)^4 binom(4,a)c^(4-a)
               *sum_(s=0)^a binom(a,s) P_js E_(a-s),        (12)
    P_js=r^(j-s)/(j-s)! if s<=j, otherwise0.

Every finite integrand is C4. At a=u_k=k/256, the Simpson suffix
[a,4] has an even number65536-64k of panels of fixed width h=1/16384.
Let M_j,c(a) be the maximum of(12) over all closed cells in[a,4].
The error for its full, signed, unshifted moment integral is at most

    (4-a)*h^4*M_j,c(a)/180 + (B_I(j)+B_T)/j!.              (13)

Both errors are added on both sides of each quadrature. All maxima
are complete cell bounds, never sampled derivative maxima.
For the frequency Taylor remainder, bound the complete moment
integral_a^infinity t^9 K(t)dt by

    M9(a)=sum_(cells [l,r] in[a,4]) (r-l)*r^9*E_0
                  +B_I(9)+B_T.                            (14)

The identical sum without r^9 gives a complete mass upper bound M0(a).
Both moment bounds retain all tails, including when a>0.

### Frequency and spatial interpolation of the signed integral

The quadrature computes both phase families

    I_j^s(c,a)=(1/j!) integral_a^infinity t^j K(t)
                            sin(ct+j*pi/2)dt,
    I_j^c(c,a)=(1/j!) integral_a^infinity t^j K(t)
                            cos(ct+j*pi/2)dt, 0<=j<=8,

with the errors(13). The suffix quadrature is obtained as total
Simpson minus its prefix; the saved intervals retain rounding widths.
At an interior even-index endpoint the global weight2 is reduced to1
for the prefix, so subtraction leaves exactly the correct suffix
weights1,4,2,...,4,1. At a=0 the prefix is exactly zero. This is an
algebraic decomposition of the same quadrature, not a subtraction of
unpaid approximate integrals.

For S_a(b)=integral_a^infinity K(t)sin(b(t-a))dt and its cosine
counterpart C_a(b), the j-th Taylor coefficient at b=c is

    (1/j!) integral_a^infinity (t-a)^j K(t)
                   sin(c(t-a)+j*pi/2)dt                    (15)

or its cosine phase. Expand (t-a)^j/j! as
sum_(ell=0)^j (t^ell/ell!)*(-a)^(j-ell)/(j-ell)!.
Rotate the stored ell-th phases by(j-ell)*pi/2 and then by-ca.
This exactly produces(15), with ordinary signed interval arithmetic
on every term. Finite binomial weights multiply both quadrature and
tail errors; no old unshifted error is reused without those factors.

For real b in either full frequency bracket, Taylor's theorem and
0<=t-a<=t give the common error

    |remainder|<=radius^9*M9(a)/9!.                         (16)

Differentiating under the integral is justified by L058's weighted
integrability (or C919m's stronger tail bounds). On every closed
frequency cell, interval Horner evaluates the entire degree8
polynomial and adds(16) on both sides. Multiplication by b gives
an interval for G_b(a)=b S_a(b); multiplication by -b^2 gives one
for G_b'(a)=-b^2 C_a(b). Both are signed enclosures throughout each
cell, not endpoint samples.

From(5),(6), the four spatial Taylor coefficients of H at a are

    H(a)  =(y^2 G_x(a)-x^2 G_y(a))/d,
    H'(a) =(y^2 G_x'(a)-x^2 G_y'(a))/d,
    H''(a)/2 =x^2*y^2*(G_y(a)-G_x(a))/(2d),
    H'''(a)/6=x^2*y^2*(G_y'(a)-G_x'(a))/(6d).               (17)

Cancellation of the two K terms in the last two identities is exact
before interval evaluation. Each denominator interval is positive:
throughout the full box d>=21^2-(29/2)^2=923/4. A further derivative
gives the exact identity

    H''''(s)=x^2*y^2*(K(s)+(x^2 G_x(s)-y^2 G_y(s))/d).

For s in[a,a+1/256], decrease of K, the bound
|G_b(s)|<=b integral_s^infinity K(t)dt, and (14)'s mass version give

    |H''''(s)|<=M4(a)
      :=(29/2)^2*22^2*
        (K_upper(a)+((29/2)^3+22^3)/(923/4)*M0(a)).          (18)

K_upper(a) uses the finite node value plus the pointwise index tail.
Thus the spatial Taylor remainder is bounded by
M4(a)/(24*256^4), uniformly over the complete parameter cell.
Interval Horner on v in[0,1/256] with(17), followed by this symmetric
remainder, encloses H_xy(a+v) on the whole closed three-dimensional
cell. This includes u=0, u=1, and all faces shared by adjacent cells.
No root condition is used in this stronger compact computation.

### Arithmetic implementation and complete evidence

The interval operations, Machin pi enclosure, exponential enclosure,
Bell bounds and small-angle trigonometric recurrence are copied from
the reviewed C919f/C919n evaluator lineage. Its only changed small-step
restriction was preregistered: degree31 sine/cosine Taylor with error
h_angle^32/32! is allowed for0<h_angle<0.002 rather than0.001.
Both fixed center steps satisfy this; the same Taylor theorem proves
the bound on the larger small interval. There is no built-in sine or
cosine evaluation. The interval angle-addition recurrence, from(1,0),
encloses every node phase by induction, retaining accumulated widths.

Pi uses exact alternating Machin fractions (80 terms at1/5,25 at1/239)
with the next terms as errors and the branch justified in C919f.
For exp([A,B]), take the lower representable neighbor of HALF_EVEN
exp(A) and upper neighbor of exp(B); monotonicity transports these
to the full interval. The exp contract is the one retained in C919f,
https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp .
Exp is not presumed to obey FLOOR/CEILING rounding. All basic bounds
use directed contexts; signed products retain all needed sign cases.
Dyadic nodes are checked against exact Fractions. No binary floating
point enters any mathematical bound. Contexts trap every exceptional
signal except Inexact and Rounded, the only flags set in the run.

Full evidence is saved at

    scripts/real-zero-origin/joint_kernel_preflight_2236.json
    scripts/real-zero-origin/joint_kernel_nodes_2236.json
    scripts/real-zero-origin/joint_kernel_2236.json
    scripts/real-zero-origin/joint_kernel_inspection_2236.json

The preflight, written before the node pass, contains all1024 spatial
bound records and256 suffix records. The node record preserves both
phase families' total sums, all256 suffix-origin snapshots and step
phases. The main certificate retains every enlarged coefficient,
frequency family, spatial remainder and all131072 joint enclosures.
The minimum lower endpoint is

    6.9115465875563516828632159916106789917904756166197961389393561124197486783524908e-9,

at cell(u,x,y) indices(255,0,0), strictly above69/10^10 and the
preregistered required10^(-10). Thus(2)'s rational compact bound
follows from the full enclosure construction and internal reconstruction
reported below; no incomplete cell coverage or numerical samples are
used as sign evidence.

The separate internal inspector reads every relevant record and
reconstructs with exact Fraction arithmetic all fourth-derivative
bounds from E_j, suffix maxima and moment sums, Simpson errors and
both tails, coefficient enlargements, binomial/phase transformations,
frequency Taylor remainders and every parameter-family enclosure.
It then reconstructs the spatial remainder and all131072 final
interval enclosures, their complete cell coverage and minimum. It
checks source/artifact hashes, node/rotation counts and all runtime
flags. It does not independently recompute the exponential values,
replay the node pass, verify the backend or replace the later critical
mathematical audit. The evaluator's mathematical bounds and the stated
arithmetic contracts remain essential. The complete run passes464918
exact-rational checks with zero failures, consuming all1024 spatial
records,256 suffix records,256 node snapshots,256 u records and131072
joint enclosures. Its final minimum agrees exactly with the saved
80-digit value above and exceeds the claimed rational69/10^10.

### Scope and known traps

The analytic construction uses both actual roots exactly for even
origin compatibility, and the nonroot parameter-box sign is a stronger
half-line calculation. No claim that every nonroot extension is smooth
is made. Compact positivity and the analytic ray meet at the fixed
split1. All infinite tails and signed integrands are retained.
Neither root was identified numerically; simplicity and exact census
are unnecessary. Existence of y in the stated bracket remains outside
this result. There is no assertion of arbitrary iteration, global
residual monotonicity, or mixed algebraic positivity. The original K
was already positive; another positive inverse alone does not establish
RH. Recorded stops concerning other deflations or finite-to-infinite
closure are preserved and not treated as global bans. QED, subject
to the stated arithmetic contract; separate audit2238 is below.

### Separate conceptual audit2238 — 21 November 2026

This audit accepts conclusions(2)-(4), including all smoothness and
tail qualifications, under exactly the stated hypotheses and backend
contracts. It is REPRODUCTION: critical acceptance of a finite local
specialization, not a claim beyond the sources assessed. The prior
SPECIALIZE assessment2236, separately approved2237, covers this audit.
All of this proof, both2236 Python sources, and every essential record
of their four JSON artifacts were checked as described below. Source
coverage2225/2230/2234/2235 is reused without new discovery browsing.
No root bracket, split, numerical setting or mathematical premise changed.

**Signed construction and complete analytic tails.** L019's summand
is exactly4v(2v-3)exp(u/2-v), matching the numerical integrand. L058
identifies its cosine transform with L018's actual Xi. C919m imports
all derivative decay, which is stronger than L019's initial-order
statement. This distinction is necessary for the all-derivative claim.
The absolute double integral in(6) has t K(u+t) as its integrand
after integrating along r+s=t, so Fubini is paid before cancellation.
The signed sine convolution has denominator y^2-x^2 and numerator
y sin(xt)-x sin(yt); multiplying by xy gives exactly the two
coefficients y^2 and -x^2 of G_x and G_y. No modulus-square sign
is substituted. Equations(5),(7) follow by differentiating the
equivalent integrals with lower endpoint u; the sine endpoint is
zero and differentiating the cosine integral contributes G_x(u).
Initial domination and the recurrences then justify smoothness and
every higher derivative without iterating an unpaid differentiation.
Rate B+1 makes each polynomially weighted integral and infinity
endpoint finite. Constants depend on the fixed roots and orders;
these estimates are not uniform in a growing removal count.

**Both roots, origin compatibility and inverse normalization.** The
first actual root is used in C919m to make G_x smooth and even with
all odd origin jets zero. At the second root, y!=x and Q_x(y)=0,
so(8) supplies the new vanishing first odd jet. Recursion with
m=1,3,5,... kills every later odd jet of H. Thus even reflection
has matching one-sided derivatives of every order and no distributional
term. Without these roots the half-line sign remains valid but the
smooth even quotient identification is not claimed.

The weighted tail estimates dominate every complex-frequency
derivative locally. Integrating H'' twice gives -H'(0)-z^2 R(z),
with the sine origin term zero and both infinity terms vanishing
at any rate B>|Im z|. Hence(9), with its positive y^2 numerator,
is valid for every complex z. Each of the four denominator factors
has a simple zero; the disjoint brackets exclude collisions. Division
reduces each original multiplicity by precisely one. The derivative
of1-z^2/x^2 at x is -2/x, giving the stated removable value;
oddness of Xi' gives the same value at -x, and likewise for y.
This includes multiple zeros and does not assume simplicity.

For inversion, the L1 bounds on H and H'' give a bounded transform
near zero and an integrable v^(-2) bound away from zero. The smooth
even extension has the absolute continuity and L1 derivatives required
by the cited Fourier input. In the source convention its transform
is2R(2*pi*eta). Substitution in Fourier inversion gives
(1/pi)integral_R R(v)exp(iuv)dv, hence(4) by evenness. All changes
of variable are absolutely integrable; continuity gives pointwise
inversion even at zero. Decaying homogeneous uniqueness in(7) is
checked using full and quarter periods, with no assumed oscillatory
boundary cancellation.

**Strict exterior, including the join.** Twice applying
2v*d/dv+(1/2-2v) to8v^2-12v gives exactly the polynomial in(10).
For v>21 its two displayed summands are positive. Uniform domination
by a polynomial in n times exp(-c n^2) on every compact u interval
justifies both termwise differentiations. Thus K''>0 on[1,infinity).
The imported K'<0 and this convexity make -K'(u+t) positive,
strictly decreasing and integrable there. Integration by parts has
zero sine endpoints and the factor1/x with a positive sign.
Tuck therefore gives G_x'<0 on this entire ray. Its first sine
application to K also gives G_x>0; these are separate statements.
The second sine application now has all the required amplitude
hypotheses for G_x(u+t), and gives strict H>0 at every u>=1,
including1. No claim of global residual decrease is used.

**Complete errors and signed arithmetic.** C919f's index majorant
is pointwise15000000 exp(-75-145t) on[0,4]; its integrated j-th
moment and the separate all-index tail[4,infinity) give(11) for
all j<=9. These lie within C919f's0..18 and lambda=0 scope.
The pointwise version is correctly used for K_upper; an integral
tail could not replace it. All moment errors include1/j!, and
frequency Taylor includes the separate9! and radius^9. Both
Leibniz sums in(12) include every derivative distribution. The
E bounds use both exponentials' absolute values on whole closed
cells. Suffix maxima cover every derivative cell to4, and the
moment sums include both complete infinite tails.

At a=k/256 the node index is64k, so the suffix has65536-64k
panels, positive and even. Removing one interior-node contribution
from the accumulated global Simpson prefix changes its weight2 to1;
subtracting that prefix leaves the correct suffix endpoint weight1.
At zero the prefix is exactly zero. Directed subtraction retains
the dependency widening. The shift in(15) includes every signed
binomial weight and both phase rotations, and therefore propagates
every coefficient's original quadrature and tail error. The ordinary
real Taylor theorem applies because every ninth frequency derivative
is bounded by the full positive t^9 moment. Interval Horner is
applied over whole closed frequency cells, not at endpoints alone.

Differentiating the exact signed expression verifies all four
spatial coefficients in(17) and H'''' as stated. The denominators
are at least923/4. On each spatial cell, K(s)<=K(a) and
|G_b(s)|<=b integral_a^infinity K(t)dt prove(18), with the full
mass upper bound. The cubic remainder is divided by24 and multiplied
by(1/256)^4. The final symmetric error therefore covers every point
of each closed three-dimensional cell, including u=0 and u=1.

Reviewed all sign branches in the interval operations: multiplication
by a nonnegative interval chooses the larger factor for a negative
lower or positive upper endpoint, and the remaining case takes all
four products. Reciprocal denominators are strictly positive; negation
uses exact copy_negate. All upper-bound sums/products are nonnegative
and rounded upward. Exact dyadic endpoints and integer-times-mesh
products fit within80 digits and are checked against Fraction.
Binary floats occur only in runtime reporting, not mathematical bounds.
The exp enclosure uses neighbors of HALF_EVEN exp, not presumed
directed exp. Its validity remains the explicitly stated contract.
Both small-angle steps are positive and below0.002; the degree31
Taylor remainder is h_angle^32/32!, including cosine's zero degree31
coefficient. Rotation uses the old sine and cosine together and
retains every interval width. Induction from(1,0) covers all nodes.

**Independent base reconstruction and complete replay.** Run

    python3 scripts/real-zero-origin/audit_joint_kernel_2238.py

in a checkout without the generated audit2238-replay directory; the
wrapper refuses to overwrite existing replay sources. Its full audit
certificate is `scripts/real-zero-origin/joint_kernel_audit_2238.json`.
It independently reconstructs all5120 E bounds at110-digit precision,
using the Bell recurrence rather than the original closed polynomials.
Every new upper bound lies below its saved80-digit bound. It also
checks the exact Machin fractions and their outward conversion, both
complete tail constants, and both sine/cosine step polynomials with
exact rational remainders. All5136 base checks pass. Higher precision
shares libmpdec; it is not independent verification of that backend.

Byte-identical copies of both original2236 sources are executed in
`scripts/real-zero-origin/audit2238-replay/`. The changed __file__
directory selects new outputs; no source expression is modified.
Their hashes and this provenance are recorded in that directory's
`provenance.json`. The replay completes65537 nodes and131072
rotations. Every saved mathematical record, including total sums,
all256 prefix/phase/kernel snapshots, every preflight bound and every
joint-cell interval, equals the original exactly. Runtime records
also agree except elapsed seconds; the resulting run-specific
artifact digests are checked separately. Original evidence is preserved.

The reviewed exact-rational inspector then reconstructs all464918
checks from the replay evidence:1024 spatial records,256 suffixes,
256 node snapshots,256 u records and131072 joint enclosures. Every
check passes, with zero failures. Equality of all mathematical fields
connects this complete reconstruction to the original artifacts;
the original inspection's categories, counts, hashes, minimum and
failure list are also checked in full. A reported PASS or preview
was not substituted for consuming these records. Base exponential
reconstruction, source/node replay and rational propagation are distinct
parts of the audit; none is claimed to verify CPython/libmpdec itself.

The audit adds5224 checks with zero failures. The exact minimum is
the80-digit value already displayed above, at(255,0,0), strictly
greater than69/10^10, which itself exceeds the preregistered1/10^10.
Every closed cell is present. This and the strict analytic exterior
establish(2) under the contracts, rather than sampled positivity.

**Acceptance and remaining gap.** No mathematical repair was needed.
The direct mathematical inputs remain L018/L019/L058,C919m,C919f;
C919n remains context only. The actual-root hypotheses, all tails,
signed errors, multiplicities and backend qualifications are retained.
Existence of y, arbitrary iteration, growing-root uniformity and the
all-degree Xi bridge remain separate unresolved tasks. Finite positivity
does not prove RH; no candidate resolution is asserted. Historical
finite-block and nonreal-deflation stops keep their original scopes.

## Mathlib

Full matching coverage of this specific two-root quotient and certified
box sign is unchecked. No absence claim or full matching declaration
is asserted. Standard Fourier, ODE, dominated-integral or quadrature
support would not alone certify this specialization. Reference:
https://leanprover-community.github.io/mathlib4_docs/ .
