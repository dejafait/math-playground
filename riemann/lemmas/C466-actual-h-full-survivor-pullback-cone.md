# C466 — Actual-h full survivor pullback cone

## Hypotheses

Use exactly C466z's normalized logarithm B on |w-1|<1/4,
x=B'(1) real, H_0=3(B(1)-x) real, and

\[
 H(z)=\sum_{j=1}^3\{B(1+z_j)-x(1+z_j)\},\qquad
 F(z)=\Delta(z)^2e^{-H(z)},\qquad
 \Delta(z)=\prod_{i<j}(z_j-z_i).
\]

Here h(w)=xi(1/2+sqrt(w))/xi(1/2) is the actual completion and
exp B=h. Retain the external density qualifications of C466a when
using this as a chart for that density; the analytic sign proof below
does not use the density construction or assume RH.

Put R=1/4, a=1/16, T_0=1/1920 and
\(\mathcal B=\{z:|z_j|<R\}\). On precisely C466y's first lifetime,
with no restart, let

\[
 \dot X=\overline{\nabla S(X)},\qquad
 S=-2\log\Delta+H,\qquad X(0,u)=iu.
\]

Only derivatives of S are used. The domain is the entire
\[
 D=\{(t,u):0<t<T_0,\ u\in(-a,a)^3,\ \Delta(u)\ne0,
                  \ t<\tau(u)\},
\]
where tau is the first maximal lifetime in
\(\mathcal B\setminus\{\Delta=0\}\). All parameter derivatives below
are at fixed physical time. Define the full signed coefficient

\[
 K(t,u)=-\frac{e^{H_0}}{\Delta(u)^2}F(X(t,u))
       \det_{\mathbb C}\!\left[\frac1i\partial_{u_k}X_j(t,u)\right].
                                                        \tag{1}
\]

## Conclusion

At every point of D, K is nonzero and has a representative phase
theta satisfying

\[
 |\theta|<\frac{19}{64}<\frac\pi2,\qquad
 \operatorname{Re}K\ge\cos(19/64)|K|>0.                 \tag{2}
\]

The estimate is uniform over all relative spacings and all surviving
approaches to pair or triple collisions. It makes no positive uniform
lower bound on |K| near a stopped boundary. In particular, it does
not assert an endpoint derivative, time-zero trace, restart, global
contour identity, patch-interface or tail payment, all-degree sign,
or actual-Xi transfer to L030-L032/C032a.

This is the local mathematical result of attempt991 under the prior
EXPLORE assessment ready989/approval990. Independent conceptual
audit993 below validates the full statement without changing its
hypotheses or constants. The original local result goes beyond the
conclusions of the sources compared there; this audit reproduces its
verification and asserts neither certified originality nor an RH candidate.

## Proof

### Imported tools and the needed specialization

C466z, including its audit988, supplies the normalized actual B, its
completion formulas, the bounds on the square-root image and Gamma
terms used below, and the strict spatial buffer. C466y/audit983 gives
smoothness on the survivor domain and, on every compact surviving
interval, the full real-parameter variational equation and weight law

\[
 J'=\overline{(D^2S)J},\quad J(0)=iI,\qquad
 \frac{d}{dt}F(X)=-\|\nabla S(X)\|_2^2F(X).              \tag{3}
\]

Both factors in the variational product are conjugated. Its primary
source is Tanizaki, Nishimura and Verbaarschot,
*Gradient flows without blow-up for Lefschetz thimbles*,
JHEP10(2017)100,
[arXiv:1706.03822v2, Appendix B (B.1)-(B.5), p.22](https://arxiv.org/pdf/1706.03822v2).
The local existence, uniqueness, smooth-dependence and compact
continuation tools are the smooth ODE theorems used in C466y:
Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems*,
author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, p.52, and Theorem6.1 with proof, pp.189-190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
They will be applied only on compact intervals strictly before tau.

The source assessment ready989 compared the exact full-coefficient
target and the recorded stops. It imports no pointwise phase cone.
The additions needed here are a sharper background constant, coupled
secant barriers and a matrix barrier for the full spatial derivative.
We derive the particular finite-dimensional identities and first-contact
arguments explicitly. No general Lagrangian-graph, invariant-cone or
collision-extension theorem is assumed or unnecessarily reproved.

### A background bound that pays the phase budget

Set q=sqrt(w), s=1/2+q and v=s/2. C466z proves, on the whole disk,

\[
 \Re s>4/3,\quad |q|>5/6,\quad |1/s|<3/4,\quad
 |1/(s-1)|<3,\quad |\psi(v)|<5,\quad |\psi'(v)|<5.       \tag{4}
\]

Its complete series majorants give
\[
 \sum_{n\ge2}(\log n)n^{-4/3}<12,\qquad
 \sum_{n\ge2}(\log n)^2n^{-4/3}<75.                     \tag{5}
\]
These were proved by integration on each [n-1,n], not by assuming
that the summands decrease there. For the sharper bound use the same
assessed Euler product,
[DLMF25.2.11](https://dlmf.nist.gov/25.2#E11), rather than separately
majorizing zeta and its reciprocal. Expanding each logarithmic factor
and differentiating gives

\[
 \frac{\zeta'}{\zeta}(s)=-\sum_{n\ge2}\Lambda(n)n^{-s},
 \qquad
 \left(\frac{\zeta'}{\zeta}\right)'(s)
       =\sum_{n\ge2}\Lambda(n)\log n\,n^{-s}.            \tag{6}
\]

Here Lambda(p^k)=log p and Lambda(n)=0 otherwise, so
0<=Lambda(n)<=log n. The prime-power expansions and both derivative
series are absolutely, locally uniformly convergent for Re s>1;
on the image in (4) the derivative series have the uniform summable
majorants (5). One can first differentiate finite prime products,
then use these locally uniform limits and the nonvanishing zeta
already proved in C466z. Thus (6) has no unproved interchange or
choice of a global logarithm. In particular its two moduli are <12
and <75. This elementary specialization of the already imported
Euler product is necessary to improve C466z's coarse constant 1000;
it is not claimed as a new number-theoretic estimate.

For L(s)=xi'(s)/xi(s), C466z's completion identities and (4)-(6)
give, using log pi<2,

\[
 |L(s)|<3/4+3+1+5/2+12=77/4<20,
\]
\[
 |L'(s)|<9/16+9+5/4+75=1373/16<86.
\]

The same exact chain rule as there yields
\[
 B''(w)=\frac{L'(s)}{4q^2}-\frac{L(s)}{4q^3},\qquad
 |B''(w)|<\frac9{25}\,86+\frac{54}{125}\,20
          =\frac{198}{5}<M:=40.                         \tag{7}
\]
All estimates hold throughout the original disk, including every
complex line segment used below.

Writing b(z)=B'(1+z)-x, we have b(0)=0 and b'(z)=B''(1+z).
Taylor's formula along each segment from 0 to iu_j gives

\[
 H(iu)-H_0=\sum_j(iu_j)^2
        \int_0^1(1-r)B''(1+riu_j)\,dr,
\]
\[
 |H(iu)-H_0|\le\frac M2\sum_j u_j^2
                 <\frac{3Ma^2}{2}=\frac{15}{64}.       \tag{8}
\]

### Coupled secants stay in a vertical cone

Fix an arbitrary u with distinct coordinates and an arbitrary
T<min(T_0,tau(u)). The trajectory on [0,T] is compact in the
nonsingular domain. Its actual pair distances therefore have a
positive minimum on this particular interval; that minimum will
be used only for continuation, never in a uniform estimate.

Permutation equivariance permits labelling u_1<u_2<u_3. Simultaneous
relabeling of initial and final coordinates conjugates J by a real
permutation matrix, so (1) is unchanged. Write X_j=p_j+iq_j.
Until a first failure of q_1<q_2<q_3, put

\[
 d_1=X_2-X_1=g_1(s_1+i),\quad
 d_2=X_3-X_2=g_2(s_2+i),\qquad
 g_1=q_2-q_1>0,\quad g_2=q_3-q_2>0.                    \tag{9}
\]

The singular velocity is exactly
\(-2\sum_{k\ne j}(X_j-X_k)/|X_j-X_k|^2\). Hence its two
gap velocities are

\[
 (d_1')_{\rm sing}=-4\frac{d_1}{|d_1|^2}
       +2\frac{d_2}{|d_2|^2}-2\frac{d_1+d_2}{|d_1+d_2|^2},
\]
\[
 (d_2')_{\rm sing}=-4\frac{d_2}{|d_2|^2}
       +2\frac{d_1}{|d_1|^2}-2\frac{d_1+d_2}{|d_1+d_2|^2}.
\]

Taking (Re d_l'-s_l Im d_l')/g_l gives

\[
 (s_1')_{\rm sing}=\frac{2g_2}{g_1}
       \left(\frac1{|d_2|^2}-\frac1{|d_1+d_2|^2}\right)(s_2-s_1),
                                                               \tag{10}
\]
and the expression with 1 and 2 exchanged for s_2. If
|s_1|,|s_2|<1, then
\(\Re(d_1\overline{d_2})=g_1g_2(1+s_1s_2)>0\).
Consequently |d_1+d_2| exceeds each individual |d_l|, and both
multipliers in (10) are positive. The singular terms point inward
at the maximum and minimum of the two slopes, regardless of the
relative sizes of g_1 and g_2.

For a gap from z_i to z_j, set
\[
 m_{ij}=\int_0^1 B''(1+z_i+r(z_j-z_i))\,dr,
 \qquad |m_{ij}|\le M.
\]
Convexity of the disk justifies the use of (7) along this segment.
The background gap velocity is conjugate(m_ij d). If m_ij=A+iC
and d=g(s+i), its slope contribution is

\[
 (s')_{\rm bg}=2As+C(s^2-1),\qquad
 |(s')_{\rm bg}|\le M\sqrt{4s^2+(s^2-1)^2}=M(1+s^2).
                                                               \tag{11}
\]

Here and below k(t)=tan(Mt); M T_0=1/48<pi/4. To make the
comparison strict, choose epsilon>0 sufficiently small that
k_epsilon(t)=tan((M+epsilon)t+epsilon)<1 on [0,T_0]. Initially
s_1=s_2=0 lie strictly between +/-k_epsilon(0). At a first upper
contact s_l=k_epsilon, (10)-(11) give
s_l'<=M(1+k_epsilon^2)<k_epsilon'; at a first lower contact they
give s_l'>=-M(1+k_epsilon^2)>-k_epsilon'. Both contradict a first
crossing from the interior. This proves the strict barrier on the
ordered interval; letting epsilon decrease to zero gives

\[
 |s_1(t)|,|s_2(t)|\le k(t).                              \tag{12}
\]

Ordering cannot fail before T: if a first adjacent imaginary gap
tended to zero, (9),(12) would force the corresponding actual
complex gap to zero, contrary to compact survival on [0,T]. Thus
(12) holds throughout this interval. The remaining pair slope is
\((g_1s_1+g_2s_2)/(g_1+g_2)\), which obeys the same bound. This
argument does not require separated subboxes or comparable gaps.

### The full matrix barrier and invertibility

Along the trajectory write D^2S=A+iC, with A,C real symmetric.
Let E_ij=(e_i-e_j)(e_i-e_j)^T. The singular Hessian is
\(2\sum_{i<j}(X_j-X_i)^{-2}E_{ij}\). For a pair gap g(s+i),
(12) gives its contributions as

\[
 A_{ij}=-c_{ij}E_{ij},\quad C_{ij}=d_{ij}E_{ij},\qquad
 c_{ij}=\frac{2(1-s^2)}{g^2(1+s^2)^2}>0,
\]
\[
 d_{ij}=\frac{-4s}{g^2(1+s^2)^2},\qquad
 |d_{ij}|\le\frac{2k(t)}{1-k(t)^2}\,c_{ij}.             \tag{13}
\]

The background Hessian is diag(B''(1+X_j)). For any real unit
vector w, its quadratic form is a complex number of modulus <=M,
by (7) and sum w_j^2=1.

Do not assume that the complex determinant, or any real projection
of J, is invertible. Instead solve the independent real matrix ODE

\[
 Z'=AZ+ZA+ZCZ-C,\qquad Z(0)=0.                          \tag{14}
\]

The coefficients are bounded and continuous on [0,T]. Local
existence and uniqueness apply; transposition of (14) shows that
Z remains symmetric. We prove -k(t)I<=Z(t)<=k(t)I in the order
on real symmetric matrices.

Use the same strict k_epsilon as above. At a first contact with the
upper barrier choose a real unit vector w with Zw=ell w,
ell=k_epsilon(t). Then

\[
 w^TZ'w=2ell\,w^TAw+(ell^2-1)w^TCw.                    \tag{15}
\]

The contribution of any pair in (13) is at most

\[
 \{-2ell\,c_{ij}+(1-ell^2)|d_{ij}|\}\,w^TE_{ij}w\le0.
                                                               \tag{16}
\]
Indeed ell>=k(t), ell<1, and 2r/(1-r^2) increases on [0,1),
so (13) makes the braces nonpositive. The background contribution
in (15) is at most
\(M\sqrt{4ell^2+(ell^2-1)^2}=M(1+ell^2)<k_epsilon'\).
For complete first-contact justification, keep this w fixed and
consider w^T(k_epsilon I-Z)w at nearby earlier times. It is
nonnegative and reaches zero at contact, so its left derivative
is <=0. The computed derivative is strictly positive, a contradiction.

At a first lower contact ell=-k_epsilon, each pair contributes at
least \(\{2k_epsilon c_{ij}-(1-k_epsilon^2)|d_{ij}| \}w^TE_{ij}w\ge0\).
The background contributes at least -M(1+k_epsilon^2).
Applying the same fixed-vector argument to Z+k_epsilon I again
contradicts contact. Hence Z stays bounded by k_epsilon on its
interval of existence. The smooth matrix ODE has no finite maximal
endpoint <=T with bounded Z and bounded coefficients; compact
continuation extends it to T. Letting epsilon decrease to zero gives

\[
                         \|Z(t)\|_{\rm op}\le k(t).      \tag{17}
\]

Now solve the real linear equation
\[
 Q'=(-A-CZ)Q,\qquad Q(0)=I,
\]
and put P=ZQ. Substitution of (14) gives
\[
 P'=AP-CQ,\qquad Q'=-AQ-CP,
 \qquad P(0)=0,\quad Q(0)=I.                            \tag{18}
\]
These are exactly the real and imaginary parts of (3). Uniqueness
therefore proves that the actual full fixed-time derivative is
J=P+iQ. The real linear determinant identity gives

\[
 \det Q(t)=\exp\!\int_0^t\operatorname{tr}(-A-CZ)\,ds>0. \tag{19}
\]
This identity follows by differentiating the determinant with its
adjugate, which gives (det Q)'=tr(-A-CZ) det Q even without
assuming invertibility. Thus (19) proves that Q is invertible,
and only now can Z be identified as P Q^{-1}. No inference from
real immersion to complex determinant invertibility has been made.

Let lambda_1,lambda_2,lambda_3 be the real eigenvalues of symmetric
Z. The real symmetric spectral theorem and (17)-(19) give

\[
 \det(J/i)=\det(Q-iP)=\det Q\prod_{j=1}^3(1-i\lambda_j)\ne0.
\]
Each factor has phase -arctan(lambda_j) in (-pi/2,pi/2).
Their sum is a representative phase theta_J with

\[
 |\theta_J|\le3\arctan k(t)=3Mt<3MT_0=\frac1{16}.         \tag{20}
\]
The factor det Q is positive, so it contributes no hidden sign.

### Reassembly of the actual weight and full Jacobian

The exact weight law (3), on this same compact surviving interval,
integrates to
\[
 F(X(t,u))=F(iu)\exp\!\left(-\int_0^t\|\nabla S(X(r,u))\|_2^2\,dr\right).
\]
The integral is finite for each such point. Moreover
\(\Delta(iu)^2=i^6\Delta(u)^2=-\Delta(u)^2\). Consequently
(1) is precisely

\[
 K(t,u)=e^{H_0-H(iu)}
    \exp\!\left(-\int_0^t\|\nabla S(X(r,u))\|_2^2\,dr\right)
    \det(J/i).                                         \tag{21}
\]

The middle factor is positive. Equations (8),(20), and the reality
of H_0 give a representative phase
theta=-Im(H(iu)-H_0)+theta_J with
\[
 |\theta|<15/64+1/16=19/64<\pi/2.
\]
Every factor in (21) is nonzero, so (2) follows. The arbitrary
compact surviving interval was used only to justify ODE operations;
the constants (7),(12),(17),(20) are independent of its minimum
pair distance. Taking any t<min(T_0,tau(u)) proves the statement
on the entire D, including arbitrarily unequal initial spacings
and approaches to coupled collisions within the first lifetime.

C466y's complete beta/gamma current identity remains in force through
C466z. This proof signs only its spatial coefficient with the
normalization (1); it neither discards the time coefficients nor
asserts a signed global assembly from them. Stops927/932/941/947/948
and C466j/t concern the different scopes recorded in review989 and
are not contradicted. All independent global/all-degree/Xi gaps remain.

### Independent conceptual audit — 14 November 2026, step993

This audit uses the unchanged invocation-start EXPLORE assessment
ready992, admitted for mathematics by the supervisor. C466y/audit983
and C466z/audit988 are established inputs, including their first-lifetime,
full-variation and external-density qualifications. The comparison of
stops927/932/941/947/948 and C466j/t in review989 remains applicable:
none settles this prescribed coupled flow's complete spatial coefficient.

**Analytic domain and constants.** All square roots, completion factors
and logarithmic derivatives are evaluated on C466z's original disk,
where Re(s)>4/3 and exp B is nonzero. The logarithmic prime-product
series and its first two derivatives converge absolutely and locally
uniformly on Re(s)>1. Indeed their derivative prime-power coefficients
are Lambda(n) and Lambda(n)log n, dominated by log n and (log n)^2;
the undifferentiated logarithmic terms p^(-ks)/k are also absolutely
summable there. Thus finite prime products yield
(6) after locally uniform passage to the limit, with no assertion
about zeta on the critical strip. C466z's [n-1,n] integral majorants
apply without monotonicity of the logarithm-weighted summands.

The completion-derivative majorants are 77/4<20 and 1373/16<86;
the q-chain-rule coefficients are 9/25 and 54/125. Consequently
the bound is 198/5<40, on every segment in the disk. The linear
term cancels because x=B'(1), and the integral Taylor remainder
has factor 1/2. Hence (8) is strictly below 3Ma^2/2=15/64.
No background estimate depends on pair spacing or a real-only bound.

**Both secant contacts and ordering.** Subtracting the two singular
particle velocities gives the displayed gap equations: the self-gap
term is -4d_l/|d_l|^2. It drops out of
Re(d_l')-s_l Im(d_l'). The other adjacent gap and the total gap
give precisely (10), with a positive multiplier whenever both slopes
have modulus below one. For the background, conjugating m g(s+i)
gives real part g(As-C) and imaginary part -g(A+Cs), so (11)
has the stated sign, including its C(s^2-1) term.

At an upper contact with k_epsilon the other slope is no greater,
so the singular contribution is nonpositive; at a lower contact it
is nonnegative. The strict derivative differences are respectively
at least epsilon(1+k_epsilon^2) for k_epsilon-s_l and
s_l+k_epsilon. A first contact from positive values would have
nonpositive left derivative, a contradiction. This also handles
simultaneous contacts of the two slopes. Letting epsilon tend to zero
gives (12) on the ordered interval. At a putative first loss of
ordering, some adjacent g_l tends to zero, and the bound
|d_l|<=g_l sqrt(1+k^2) forces an actual collision. Continuity on the
fixed compact surviving interval excludes that event, even if both
adjacent imaginary gaps vanish together. The total-gap slope is a
positive weighted mean. Thus all three pair estimates in (13) apply.

**Both matrix contacts and compact continuation.** Direct expansion
of 2/[g(s+i)]^2 gives the negative real coefficient -c and imaginary
coefficient d in (13). In particular c>0 and
|d|/c=2|s|/(1-s^2)<=2k/(1-k^2). The independent Riccati ODE is
locally Lipschitz in the entries of Z, and transposition preserves it,
so its initially symmetric solution stays symmetric. On a unit contact
vector with Zw=ell w, its derivative is exactly (15).

For an upper contact ell=k_epsilon, each pair contributes at most
[-2ell+(1-ell^2)2k/(1-k^2)]c(w_i-w_j)^2<=0. For a lower contact
ell=-k_epsilon, the lower bound is the negative of that upper bound
evaluated at ell=k_epsilon, hence nonnegative. The background quadratic form is
sum_j w_j^2 B''(1+X_j), of modulus at most M; combining its real
and imaginary parts bounds its contribution in absolute value by
M(1+ell^2). Thus both strict barrier derivatives have the same
positive margin epsilon(1+k_epsilon^2) as above. At contact the
chosen vector is held fixed at earlier times. The relevant quadratic
form of k_epsilon I-Z or Z+k_epsilon I was positive there and is
zero at contact, so its left derivative cannot be positive. This
argument requires neither a differentiable eigenvector nor a simple
eigenvalue, and covers simultaneous upper/lower or repeated contacts.

For any fixed T<min(T_0,tau(u)), A,C are bounded on [0,T] and
extend a little farther since T<tau(u). The barrier bounds all entries
of Z. Its graph therefore stays in a compact subset of the
time/matrix domain of the Riccati field up to any proposed endpoint
at or before T. The cited compact-continuation theorem applies.
The compact set may depend on u,T; the bound (17) does not depend
on its minimum pair distance. No endpoint at tau(u) is included.

**Reconstruction before inversion.** The factor order is essential.
With Q'=(-A-CZ)Q and P=ZQ, direct multiplication gives
P'=(AZ+ZA+ZCZ-C)Q+Z(-A-CZ)Q=(AZ-C)Q.
Thus (18), including both conjugations in (3) and J(0)=iI, holds.
Uniqueness of this real linear system identifies P+iQ with the
actual fixed-time derivative before any inverse is used.

For (19) import Abel-Liouville's determinant formula: Teschl,
the April2012 preliminary version cited above, Lemma3.11, equation
(3.91) and proof, p83; continuous-coefficient existence is Theorem3.9,
p81. The coefficient -A-CZ is a continuous real matrix on [0,T]
and Q(0)=I. These are precisely the needed hypotheses; the formula
does not require invertibility as a premise. The short adjugate check
above records this noncircular application, rather than adding a new
determinant theorem. It follows that det Q>0 and only then that
Z=P Q^(-1). Consequently Q-iP=(I-iZ)Q, in this order, proves the
full complex determinant factorization in (20).

**Signed reassembly.** Simultaneous permutation of initial and final
coordinates conjugates J by the same permutation matrix; the two
permutation determinants cancel. Both Vandermonde squares are invariant.
For real distinct u, Delta(iu)^2=-Delta(u)^2, and det(J/i) initially
equals one. Hence the minus sign in (1) cancels exactly, as in (21),
without replacing a complex determinant by its modulus. The integrated
weight law has a finite real exponent on each compact survivor and
therefore preserves the initial weight phase. The positive det Q
contributes no phase; the symmetric eigenvalues of Z contribute a
total of at most 3 arctan(tan(Mt))=3Mt<1/16. The initial weight
contributes less than 15/64. Their sum is strictly below 19/64,
and all factors are nonzero. This proves exactly (2) for every point
of D, not a positive uniform modulus floor at its boundary.

**Verdict and limits.** The full statement passes with no mathematical
correction or additional lemma input. C466y and C466z remain its direct
inputs; C466k supplies only an orientation comparison, not a premise.
The audit validates a previously unverified local input by reproduction;
it adds no new theorem or novelty claim. The complete beta/gamma forms
remain as in C466y/z: an arbitrary complex ambient cutoff is not signed
by (2), and the mixed time/parameter coefficients have not been discarded.
There is still no time-zero trace, global transport or contour identity,
patch/tail payment, all-degree positivity or actual-Xi transfer. No
numerical certificate, mathematical script, formal verification or RH
candidate is claimed.

## Mathlib

Full matching coverage has not been checked; this is not evidence
of absence. Supporting inputs are ordinary smooth ODE existence,
uniqueness and continuation, the real symmetric spectral theorem,
the determinant identity for a linear matrix ODE, and the assessed
analytic formulas in C466z. No exact Mathlib theorem names for this
coupled singular-flow cone or its complete specialization have been
checked. No numerical certificate or formal verification is claimed.
