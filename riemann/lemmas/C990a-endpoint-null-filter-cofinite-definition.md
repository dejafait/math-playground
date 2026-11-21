# Corollary 990a: eventual definition of the fixed endpoint-null filter

## Hypotheses

For integer n>=2 use exactly L990's real polynomials and oriented rows:

    K_m(u)=[L_(m-1)^(2)(u)-1]/(m-1),
    a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)),
    b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)),
    d_n=a_n cross b_n,  D={n>=2:d_n!=0}.

Use the standard Laguerre normalization, with p_n(u)=L_n^(2)(u).
There is no assumption of RH, actual off-line zeros, effective onset,
uniform conditioning of the normalized cross product, or an expansion
of individual Laguerre zeros. The uniform bulk result imported below
is used only with fixed alpha=2 and a positive compact scaled interval.

## Conclusion

There is n_0 such that d_n!=0 for every integer n>=n_0. Thus D is
cofinite and L990's prescribed c_n=d_n/||d_n||_1 and F_n are eventually
defined on all integers. Together with L990's signed subsequence and
upper bound, its fixed synthetic quartet diagnostic has

    limsup_(n->infinity) log(1+max(Z_n,0))/n = 1/2,

where omitting the finitely many undefined indices has no effect.

The load-bearing endpoint formula is additive, including at zeros.
Put N=4n+6, t_(r,n)=rn/N, and

    b(t)=[sqrt(t-t^2)+arcsin(sqrt(t))]/2,
    D_0(t)=4*t^(5/4)*(1-t)^(1/4),
    M_(r,n)=exp(rn/2)*sqrt(2/(pi*N))/D_0(t_(r,n)),
    kappa_1=sqrt(3)/2+pi/3, kappa_2=1+pi/2,
    theta_(1,n)=n*kappa_1-3*pi/4+13*sqrt(3)/(108*n),
    theta_(2,n)=n*kappa_2-pi/2-13/(24*n).

There are constants C_*, n_* independent of n and r in {1,2} such that

    |p_n(rn)/M_(r,n)-cos(theta_(r,n))| <= C_*/n^2       (1)

for every n>=n_*. A finite expression for C_* in terms of the imported
uniform remainder constants and compact maxima is supplied below;
no numerical constant or effective onset is claimed.

Step263, 10 November2026: REPRODUCTION under review262, a local
specialization of published asymptotics and L990's finite reduction.
Step265 critically audited the cofinite-definition proof and (1)
under separately approved review263, including the needed parts of
L990's row bounds and exact reduction. Those claims pass the audit.
The displayed signed limsup inherits L990's signed-response argument,
separately audited in step267; it was not audited in step265.
This settles a synthetic definition obligation, not actual B_n,
L984(H), the two complements, other-zero control, arithmetic transfer
or RH. No original discovery beyond the sources checked is claimed.

## Proof

### The precise bulk import

Import A. Gil, J. Segura and N. M. Temme, *Asymptotic approximations
to the nodes and weights of Gauss–Hermite and Gauss–Laguerre
quadratures*, [arXiv1709.09656v1, 27September2017, section3.3,
equations81–87 and section3.3.1](https://arxiv.org/html/1709.09656v1#S3.SS3).
Its fixed-alpha uniform expansions apply for rho<=1-delta,
delta in (0,1) fixed. Restrict to J=[1/9,1/2] and alpha=2;
both t_(r,n) belong to J for n>=2. With v=2n+3=N/2,
zeta=b(t)^2, the representation and its asymptotic contract become

    p_n(Nt)=exp(Nt/2)*sqrt(b(t))/D_0(t)
                  *[J_2(Nb(t))*A - J_3(Nb(t))*B/b(t)],
    A=1+O(v^-2), B=C(t)/v+O(v^-3),                    (2)

uniformly on J. All O bounds here and below are absolute bounds.
We use the uniform Poincare expansion, not that paper's subsequent
assumed expansions of individual zeros or its numerical accuracy tests.
For clarity, at alpha=2 its prefactor satisfies
chi(zeta)/(4*zeta)=sqrt(b(t))/D_0(t): here
chi=(1-t)^(-1/4)*(zeta/t)^(5/4) and zeta=b(t)^2.
Thus both the prefactor and Bessel argument use the same N=2v.
The positive compact J lies within the source domain with delta=1/2;
the uniform series and its smooth coefficients give finite remainder
constants on J, without differentiating any remainder.

For the first coefficient use the authors' *Efficient computation of
Laguerre polynomials*, Computer Physics Communications210 (2017),
124–131, DOI[10.1016/j.cpc.2016.09.002](https://doi.org/10.1016/j.cpc.2016.09.002),
[arXiv1609.00829v1, section2.1.3, equations20–25](https://arxiv.org/html/1609.00829v1#S2.SS1.SSS3).
At alpha=2 its coefficient25 reads, with q=t/(1-t),

    C(t)=-15/16+b(t)/(8*sqrt(q))*(15/2+q+5*q^2/6).    (3)

The 2016 B-series starts at C, with an external 1/v; the 2017
B-series starts at C/v. Thus (2) retains exactly the same correction.
The 2016 alpha convention resolves the undefined a in the 2017
display86. We do not replace a coefficient inside DLMF18.15.19's
different printed formula or borrow its remainder. The discrepancy
and original Frenzen–Wong access limitation remain recorded in
`drafts/literature/2026-11-10-laguerre-normalization-source-notes-262.md`.
No higher explicit GST coefficient or recursive display is needed.

### An additive normalized remainder

Let z=Nb(t), Phi=z-5*pi/4, and S_j(z)=sqrt(pi*z/2)*J_j(z).
Import [DLMF10.17.1–3 and10.17(iii)](https://dlmf.nist.gov/10.17#iii),
fixed orders2 and3 and z>0. Order2 permits ell=1 in both real
remainder bounds. For order3 take ell=2 in the cosine sum and ell=1
in the sine sum before absorbing higher terms. Consequently for z>=1,

    S_2(z)=cos(Phi)-15*sin(Phi)/(8*z)+R_2,
    |R_2|<=c_2/z^2,
    S_3(z)=sin(Phi)+R_3, |R_3|<=c_3/z,                (4)

where one admissible choice, using DLMF's coefficients a_k(j), is

    c_2=|a_2(2)|+|a_3(2)|,
    c_3=|a_1(3)|+|a_2(3)|+|a_3(3)|+|a_4(3)|.

These inequalities follow from the separate sine and cosine bounds;
they are not relative errors at an oscillatory zero. The order3 phase
is Phi-pi/2, so its leading cosine is +sin(Phi).
Specifically the cosine restriction is ell>=max(j/2-1/4,1)
and the sine restriction is ell>=max(j/2-3/4,1). For j=2
both thresholds are1; for j=3 they are5/4 and1. Thus the
respective choices (1,1) and (2,1) meet both restrictions.
Before absorbing powers for z>=1, the order2 error is bounded by
|a_2(2)|/z^2+|a_3(2)|/z^3; the order3 error from its leading
term is bounded by the sum of |a_k(3)|/z^k for k=1,2,3,4.

Choose finite constants c_A,c_B and a source onset for which
|A-1|<=c_A/v^2 and |B-C/v|<=c_B/v^3 throughout J. Write
a=4*c_A, e=8*c_B, b_*=min_J b>0 and C_0=max_J |C|.
For sufficiently large n, z>=1. Dividing (2) by the positive
amplitude exp(Nt/2)*sqrt(2/(pi*N))/D_0(t) gives exactly
S_2 A-S_3 B/b. Equations (3)–(4) therefore imply

    p_n(Nt)/[exp(Nt/2)*sqrt(2/(pi*N))/D_0(t)]
       =cos(Phi)-H(t)*sin(Phi)/N+R,
    |R|<=K_0/N^2,                                    (5)
    H(t)=[15/8+q/4+5*q^2/24]/sqrt(q),
    K_0=c_2/b_*^2+a*(1+15/8+c_2)
                       +2*C_0*c_3/b_*^2+e*(1+c_3)/b_*.

Indeed the coefficient of -sin(Phi)/N before simplification is
(15/8+2*C(t))/b(t). The constant -15/8 from 2*C cancels the
Bessel term15/8, leaving exactly H(t). The four terms in K_0
bound respectively R_2, (A-1)S_2, (2C/Nb)R_3, and
(B-2C/N)S_3/b. In the last term we used N>=1 to replace N^-3
by N^-2. Thus every retained or discarded source term is accounted for.

Set H_0=max_J |H| and H_1=max_J |H'|, both finite. Taylor's theorem
for cosine, uniformly in Phi, changes (5) into

    |p_n(Nt)/[exp(Nt/2)*sqrt(2/(pi*N))/D_0(t)]
                         -cos(Phi+H(t)/N)|<=K/N^2,
    K=K_0+H_0^2/2.                                   (6)

Neither a cosine nor a cross product has been divided out, and no
asymptotic remainder has been differentiated.

### Endpoint phases and their complete error bound

Fix r in {1,2} and let g(s)=s*b(rn/s), 4n<=s<=4n+6.
With t=rn/s and q=t/(1-t), direct differentiation of b gives

    b'(t)=1/(2*sqrt(q)),
    g'(s)=arcsin(sqrt(t))/2,
    g''(s)=-sqrt(q)/(4*s),
    g'''(s)=sqrt(q)*(3-2*t)/[8*(1-t)*s^2].             (7)

Here 0<t<=1/2, so sqrt(q)<=1 and (3-2t)/(1-t)<=4.
Hence |g'''(s)|<=1/(32*n^2). Taylor expansion through degree2
over the increment6 has remainder at most9/(8*n^2). With
t_0=r/4 and q_0=t_0/(1-t_0), it follows that

    (4n+6)*b(rn/(4n+6))
       =4n*b(t_0)+3*arcsin(sqrt(t_0))
                         -9*sqrt(q_0)/(8*n)+E,
    |E|<=9/(8*n^2).                                  (8)

Also |t_(r,n)-t_0|<=3/(4*n) and
|1/(4n+6)-1/(4n)|<=3/(8*n^2). By the mean value theorem,

    |H(t_(r,n))/(4n+6)-H(t_0)/(4n)|
                     <=[3*H_1/16+3*H_0/8]/n^2.      (9)

At the two endpoints the finite values are

    4*b(1/4)=sqrt(3)/2+pi/3,
    4*b(1/2)=1+pi/2,
    H(1/4)=107*sqrt(3)/54, H(1/2)=7/3.

Subtracting5*pi/4 from (8) gives constants -3*pi/4 and
-pi/2. Adding (9) gives the respective 1/n coefficients

    gamma_1=-9/(8*sqrt(3))+107*sqrt(3)/216
                                             =13*sqrt(3)/108,
    gamma_2=-9/8+7/12=-13/24.                         (10)

The Lipschitz bound for cosine and (6)–(9) prove (1), with

    C_*=K/16+9/8+3*H_1/16+3*H_0/8.                  (11)

This is an additive normalized O(n^-2) bound with a constant
independent of the phases. Its source onset is existential.

### Exact degeneracy would give an impossible integer limit

Use L990's exact degeneracy reduction and its uniform endpoint-row
bounds. The latter are legitimate at every sufficiently large n:
its leading first row has squared Euclidean norm3/2, and its
leading second row has squared norm1+cos(psi_n)^2 in [1,2].
Their additive O(1/n) row errors thus leave uniform positive lower
bounds. To check this input independently of L990's signed work,
use its displayed row scales A_n^*,B_n^* and formula(5).
The same GST import above, with degree n+j-1 and N_j=4n+4j+2,
gives the first-order additive cosine bound uniformly for j=0,1,2
and t=rn/N_j in J. A bounded Taylor shift 4j+2 from4n gives
phase increments (4j+2)*pi/12 at r=1 and (4j+2)*pi/8 at r=2,
with O(1/n) error; the amplitude has relative error O(1/n).
The retained -1/(n+j-1), after row scaling, contributes
O(sqrt(n)*exp(-rn/2))=O(1/n). This verifies exactly L990's
two first-order row formulas, without using its transform or orbit
argument. The first norm identity follows from summing
cos(2*phi+2*j*pi/3) over j=0,1,2; the second is immediate.
The l2 norm of each error is at most its l1 norm. Consequently the
positive lower bounds hold for every large n, including collisions
of the two row directions; no cross-product lower bound is used.

If d_n=0, then b_n=lambda_n*a_n, where

    c*exp(n/2)<=|lambda_n|<=C*exp(n/2),
    p_n(n)=2-2/lambda_n, p_n(2n)=lambda_n-1.           (12)

These are exact consequences of the shifted three-term recurrence,
including both -1 corrections, not just leading phase conditions.
Explicitly L990(13) reads R(u) dot K(u)=-u, with
R(u)=((n-1)*(n+2),-n*(2n+3-u),(n+1)^2).
Substituting p_(n+j-1)=(n+j-1)*K_(n+j)+1 in the standard
three-term recurrence leaves the constant u on its left side,
which verifies the sign -u. Since R(2n)-R(n)=(0,n^2,0),
collinearity gives lambda_n*(-n+n^2*K_(n+1)(n))=-2n.
This is lambda_n*(p_n(n)-2)=-2, and its middle component
then gives p_n(2n)-1=lambda_n*(p_n(n)-1)=lambda_n-2.
The norm ratio B_n^*/A_n^* times bounded nonzero row norms
proves both sides of the stated bound on |lambda_n|.
Since M_(r,n) is comparable to exp(rn/2)*n^-1/2 on J, (12) gives

    |p_n(rn)/M_(r,n)|<=C'*sqrt(n)*exp(-n/2), r=1,2.   (13)

Suppose there are arbitrarily large degenerate indices. On these
indices (1) and (13) imply |cos(theta_(r,n))|=O(n^-2), with one
constant. For any real x, its distance d to pi/2+pi*Z is at most
pi/2, and |cos(x)|=sin(d)>=2*d/pi. Thus there exist integers k_n,l_n
such that, along the degenerate indices,

    n*kappa_1-3*pi/4+gamma_1/n=pi/2+pi*k_n+O(n^-2),
    n*kappa_2-pi/2+gamma_2/n=pi/2+pi*l_n+O(n^-2).     (14)

No inverse-function estimate at a small cosine or assumed zero
expansion is used. Retain the rational offsets by defining integers

    A_n=12*k_n+15-4*n,
    B_n=2*l_n+2-n.

Rearranging (14) gives

    A_n=6*sqrt(3)*n/pi+12*gamma_1/(pi*n)+O(n^-2),
    B_n=2*n/pi+2*gamma_2/(pi*n)+O(n^-2).              (15)

Squaring is safe here: the leading terms are O(n), so each product
with its O(n^-2) error is O(n^-1). The n^2 terms cancel, leaving

    A_n^2-27*B_n^2
       =(144*sqrt(3)*gamma_1-216*gamma_2)/pi^2+O(n^-1)
       =(52+117)/pi^2+O(n^-1)=169/pi^2+O(n^-1).       (16)

The left side is an integer. The right side tends to a noninteger:
pi is transcendental by the Lindemann–Weierstrass theorem (the precise
input already used in L990 is L. Fukshansky, *Geometric Number Theory*,
[Theorem6.2.1, printed p138](https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=142)).
Indeed if pi were algebraic, the distinct algebraic exponents0
and i*pi, with coefficients1 and1, would contradict that theorem
via Euler's identity exp(0)+exp(i*pi)=0.
If 169/pi^2 were an integer m, then m!=0 and m*pi^2-169=0
would make pi algebraic. Equivalently its distance delta>0 from Z
is positive; (16) has error smaller than delta/2 at all sufficiently
large degenerate indices, which is impossible. Hence the degenerate
indices are bounded, proving cofinite definition.

The audit's decisive error threshold is an additive o(1/n) phase
error: squaring the O(n) integer expressions must leave o(1).
The proved O(n^-2) bound supplies the stronger O(n^-1) final error
in(16). All constants are uniform along any putative unbounded
degenerate subsequence. For its finite error constant C, taking
n>2C/delta beyond the source onsets contradicts integrality.
This quantifier check proves an existential n_0, not a computed one.

The signed limsup statement now follows directly from L990 on D,
which contains every sufficiently large integer. This last use does
not independently audit L990's finite transform or signed subsequence.
There is no uniform lower bound here for ||d_n|| after bulk scaling,
no effective value of n_0, and no assertion that all n>=2 are defined.
The synthetic quartet has not been realized by zeta zeros. No passage
to an infinite zero sum, prime estimate, positivity criterion or RH
is licensed by this finite-family nonvanishing result.

## Mathlib

Full matching Mathlib coverage of this moving normalized filter and
its cofinite definition has not been checked. The uniform GST
expansion, Bessel error bounds and transcendence input are imported
by precise citations; the displayed algebra and calculus justify
their specialization. No formalization or absence claim is made.
