# C744p: Weighted coercivity for varying dyadic corrected carriers

## Hypotheses

Fix ell=log(3)/2, finite M>=1 and a real nonnegative
chi in C_c^infinity(0,ell), positive on a nonempty open interval.
For R>=e^3 put

    y=log R, K_R=floor(log log R/ell), L_R=K_R ell.

For any finite integer J>=1, put t_j=2^j R and y_j=log(t_j),
0<=j<J. Independently choose w_j in L744(1)'s F_(K_R,M):

    w_j(x)=sum_(k=0)^(K_R-1) w_(j,k)(x-k ell),
    w_(j,k) in C_c^infinity(0,ell;C),
    ||w_j||_2=1, ||w_j||_H2<=M,
    ||u||_H2^2=||u||_2^2+||u'||_2^2+||u''||_2^2.

All extensions are by zero and all norms are the original unweighted
ones. Use precisely C744n(1)'s complex-linear cellwise correction,
on this common window. Explicitly, for sigma,tau in {+1,-1}, let

    b_tau(s)=chi(s)exp(tau s/2),
    G_(sigma,tau)=integral_0^ell chi(s)exp((sigma+tau)s/2) ds,
    d_(j,k,sigma)=exp(it_j k ell)
                integral_0^ell exp(sigma s/2)w_(j,k)(s)exp(it_j s) ds,
    h_j(x)=sum_(k,tau) (G^-1 d_(j,k))_tau b_tau(x-k ell),
    f_j(x)=exp(it_j x)w_j(x), v_j=f_j-h_j.

The fixed matrix G is invertible as used in C744n. Let
g=sum_j c_j v_j for arbitrary complex coefficients c_j. The complete
energy E_L is L744's energy for the original generator A_L, with
first-slot-linear inner product. No RH assumption is made. Empty
profile families make no existence claim.

The additional matrix import is H. L. Montgomery and R. C. Vaughan,
*Multiplicative Number Theory II: Primes and Sieves*,
[author-hosted draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
undated version retrieved 11 November 2026, Theorem G.3 and proof,
printed pp.399-400 (PDF pp.411-412). For every finite complex matrix A,

    ||A||_(2->2) <= sqrt((max_i sum_j |a_ij|)(max_j sum_i |a_ij|)).

This finite Schur theorem is imported, not reproved. The quantitative
Gram estimates below are the required specialization. The ready
source comparison is
`drafts/literature/2026-11-11-dyadic-varying-carrier-coercivity-502.md`.

## Conclusion

There is one R_*(M,chi)<infinity such that for every R>=R_*, every
finite J, every admitted family and every complex coefficient vector,

    E_(L_R)(g) >= (1/8) sum_(j=0)^(J-1) log(t_j)|c_j|^2.       (1)

The explicit error bound (16) below is uniform in all these choices.
In particular g is nonzero for nonzero c at that onset. This is a
standard-mechanism REPRODUCTION, written 11 November 2026, step504;
the separate conceptual audit below (step506) accepts (1)-(16)
without a mathematical repair. It is local
progress on a finite trial block, not a claim of originality beyond
the sources checked, an all-test positivity theorem, or an RH candidate.
Independent low-block signs, non-neutral coverage and general assembly
remain open. No infinite synthesis or density conclusion is asserted.

## Proof

### 1. Complete form and estimates before selecting the window

Use F_u(xi)=integral_R u(x)exp(-i xi x)dx and dmu=dxi/(2pi).
For any finite K>=2 all the functions in question and their finite
linear combinations are smooth and compactly supported in (0,K ell).
L744's smooth-domain argument puts them in the actual generator
domain; it requires no domain-norm bound uniform in K or J.
C744o(4)'s complete polarization reads

    mathcal E_L(a,b)=Q_m(a,b)
       +F_a(i/2)conj(F_b(-i/2))+F_a(-i/2)conj(F_b(i/2))
       -<B_L a,b>,
    Q_m(a,b)=integral m(xi)F_a(xi)conj(F_b(xi)) dmu,
    m(xi)=Re psi(1/4+i xi/2)-log pi,
    B_L=sum_(2<=n<exp L) Lambda(n)/sqrt(n)
                            (T_(log n)+T_(log n)^*).           (2)

This retains all prime powers and the original factor two; a delay
at L is zero. Matrix inversion in each cell gives both local moments
of v_j exactly zero. Finite linearity gives the same for g, and hence
F_g(i/2)=F_g(-i/2)=0. Therefore

    E_L(g)=Q_m(g,g)-<B_L g,g>.                                 (3)

The poles cancel for the actual corrected sum before any estimates.
We do not discard poles of the uncorrected summands separately.

Here are the quantitative inputs, valid for every finite K before
choosing K_R. Set

    A=2+8sqrt(2)/3+log(4pi), W(xi)=A+log(2+|xi|),
    p(s)=1+s^2+s^4, D0=A+log3+3+log(2pi),
    a(t)=2M/t+(8+4M^2)/t^2+16M^2(D0+log t)/t^4,
    U(t)=A+log(2+t)+3+M^2,
    H=||G^-1|| (||b_+||_H2^2+||b_-||_H2^2)^(1/2)
                         sqrt(33 ell exp(ell)/8) M.

L744(8)-(13), with the K-independence justified in C744n(4)-(5), give

    |m|<=W, W(xi)<=(A+3)(1+xi^2),
    integral p(eta)|F_(w_j)(eta)|^2 dmu(eta)<=M^2,
    |Q_m(f_j,f_j)-(y_j-log(2pi))|<=a(t_j),
    ||f_j||_W^2:=integral W|F_(f_j)|^2 dmu<=U(t_j),
    ||h_j||_H2<=H/t_j^2.                                     (4)

The source scalar input already specialized there is
[NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2), with the complex
remainder in [5.11(ii)](https://dlmf.nist.gov/5.11#ii), applied on
z=1/4+i xi/2. Its bound includes bounded xi. The Fourier inputs are
Plancherel and Fourier differentiation: Andras Vasy, *Math 172: The
Fourier Transform — Basic Properties and the Inversion Formula*,
[author-hosted notes](https://math.stanford.edu/~andras/172-4.pdf),
undated version inspected 11 November 2026, pp.1-2 and Lemma 0.4/proof,
p.13. Smooth compactly supported zero extensions meet their decay
and differentiability hypotheses. We reuse these identities and the
already proved scalar and correction estimates, not new versions of
the underlying theorems. In particular, (4) does not use C744n's final
conclusion with its carrier-dependent K(t_j) on a different window.

### 2. Uniform off-diagonal Fourier estimates

For i<j write d=t_j-t_i. Dyadic separation gives d>=t_j/2.
At each real xi put r=max(|xi-t_i|,|xi-t_j|). Then
r>=d/2>=R/2>1, t_j<=2d<=4r and |xi|<=t_j+r<=5r.
Since sqrt(p(s))>=max(1,s^2),

    sqrt(p(xi-t_i)p(xi-t_j))>=r^2.

The function [A+log(2+5r)]/r^2 decreases on r>=1: its derivative
has numerator 5r/(2+5r)-2[A+log(2+5r)]<0. Consequently

    W(xi)/sqrt(p(xi-t_i)p(xi-t_j))
       <=4[A+log(2+5d/2)]/d^2
       <=4[A+log3+y_j]/d^2.                                  (5)

The last step uses d<=t_j and t_j>=4, so 2+5d/2<=3t_j.
Multiply (5) by sqrt(p(xi-t_i))|F_(w_i)(xi-t_i)| times the
analogous j factor and apply integral Cauchy--Schwarz and (4).
For either s=m or s=W this proves

    |Q_s(f_i,f_j)|<=4M^2(A+log3+y_j)/d^2
                  <=16M^2(A+log3+y_j)/t_j^2.                  (6)

For m, use |m|<=W; for W the form Q_W is the positive weighted
inner product. The same reasoning without W gives

    |<f_i,f_j>|<=4M^2/d^2<=16M^2/t_j^2.                       (7)

There is no disjoint-Fourier-support assumption and no higher uniform
derivative or support-dependent L1 bound in these estimates. All
Fourier integrals are absolutely convergent for each finite family.

### 3. Finite Schur payment independent of J

Define constants and nonnegative error functions

    B=A+log3, D=16M^2(1+B/3),
    eta(R)=2D/R^2, rho(R)=16M^2/R^2,
    D1=A+log2+3+M^2, V(R)=1+D1/y+eta(R),
    S=sum_j y_j|c_j|^2.                                     (8)

For each of the m and W Gram matrices remove the diagonal and divide
entry (i,j) by sqrt(y_i y_j). For i<j, (6) and y_j>=y>=3 give the
entry bound

    D R^-2 4^-j sqrt(y_j/y_i)
       <=D R^-2 4^-j (1+j-i).                               (9)

Indeed y_j/y_i=1+(j-i)log2/y_i<=1+(j-i), whose square root is at
most 1+(j-i). The absolute entries are symmetric, since both forms
are Hermitian. For row i the indices j>i contribute at most

    (D/R^2)4^-i sum_(n>=1)(1+n)4^-n
       =(D/R^2)4^-i (7/9).

The indices j<i contribute at most

    (D/R^2)4^-i sum_(n=1)^i(1+n)
       =(D/R^2)4^-i i(i+3)/2 <=D/(2R^2).

For the latter inequality i(i+3)<=4^i for i>=1: it holds at i=1,
and (i+1)(i+4)<=4i(i+3) for i>=1 proves induction. At i=0 the
sum is empty. Every row, and thus every column, is bounded by
(23/18)D/R^2<eta(R). Apply the imported finite Schur theorem to
each normalized off-diagonal matrix. Its quadratic-form contribution
has absolute value at most eta(R)S, for arbitrary complex c. The
first-slot-linear convention uses sum c_i conj(c_j) times the Gram
entries; applying the matrix norm inequality to the conjugate
coefficient vector gives precisely the same bound.

For the unweighted L2 Gram remainder, (7) bounds row i by

    (16M^2/R^2)4^-i (i+1/3) <=rho(R).

Here i4^-i<=1/4 for i>=1, the i=0 term is zero, and 4^-i/3<=1/3.
Symmetry again gives the column bound. Its diagonal is exactly one,
so Schur gives ||sum c_j f_j||_2^2<=(1+rho)sum|c_j|^2.
These geometric majorants bound finite row sums only; they assert
no convergence or synthesis statement for an infinite family.

Put f=sum c_j f_j. Since a(t) decreases for t>=e^3, a(t_j)<=a(R).
For its last term this follows by differentiating
(D0+log t)/t^4, whose derivative has sign 1-4(D0+log t)<0;
the other terms plainly decrease. From the m diagonals in (4) and
the normalized remainder bound,

    Q_m(f,f)>=[1-(log(2pi)+a(R))/y-eta(R)]S.

Also log(2+t_j)<=log t_j+log2 implies U(t_j)<=y_j+D1.
The W and L2 Gram bounds therefore give, together,

    ||f||_W^2<=V(R)S,
    ||f||_2^2<=(1+rho(R))S/y.                               (10)

Thus the unbounded logarithmic multiplier has been paid before
estimating the correction, uniformly even in the largest carrier.

### 4. The whole correction and all its pairings

Put h=sum c_j h_j and

    delta(R)=4H/(sqrt(15) R^2 sqrt(y)).

The triangle inequality, (4), and coefficient Cauchy--Schwarz give

    ||h||_H2 <= H sum |c_j|/t_j^2
       <= H sqrt(S) (sum 1/(y_j t_j^4))^(1/2)
       <= H sqrt(S)/(R^2 sqrt(y)) (sum_(j>=0)16^-j)^(1/2)
       =delta(R)sqrt(S).                                    (11)

This is a bound on the entire correction synthesis, not a sum of
individual energy lower bounds. In particular
||h||_W<=sqrt(A+3)delta sqrt(S) and ||h||_2<=delta sqrt(S).
Using |m|<=W, weighted Cauchy--Schwarz and (10)-(11) gives

    |Q_m(f-h,f-h)-Q_m(f,f)|
       <=[2sqrt((A+3)V(R))delta(R)+(A+3)delta(R)^2]S,
    ||g||_2^2<=q(R)S,
    q(R)=[sqrt((1+rho(R))/y)+delta(R)]^2.                     (12)

Both carrier/correction terms and the correction/correction term
are included. No factor J is introduced by summing the weighted
norms of individual carriers. No positivity of Q_m is assumed.

### 5. Full arithmetic payment and the required threshold

Import C744n(7)-(8)'s bound, for every finite L,

    ||B_L||<=C_prime(L)
       =2 sum_(2<=n<exp L) Lambda(n)/sqrt(n)
       <=4c exp(L/2), c=1.03883.                             (13)

Its arithmetic source is Rosser and Schoenfeld, *Approximate formulas
for some functions of prime numbers*, Illinois J. Math. 6(1) (1962),
64-94, [Theorem 12, (3.35), printed p.71](https://doi.org/10.1215/ijm/1255631807),
psi(x)<1.03883x for every x>0, with all prime powers included.
The original article is also available in the
[primary scan](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf)
verified in the prior audit assessment; its p.64 definition uses
inclusive prime-power endpoints.
C744n's Abel-summation specialization bounds the strict cutoff by
the inclusive sum; no new prime estimate or finite table replay is
needed here. For our common window L_R<=log log R, (13) becomes

    ||B_(L_R)||<=4c sqrt(y),
    |<B_(L_R)g,g>|<=4c sqrt(y)q(R)S.                         (14)

This contraction-operator bound includes every arithmetic pairing
of the mixture, including its corrections. It requires no high/high
delay estimate beyond the already paid collective L2 norm (12).

Combine (3), (10), (12), and (14). Define the explicit nonnegative
loss, depending only on R,M,chi,

    Delta(R)=(log(2pi)+a(R))/y+eta(R)
       +2sqrt((A+3)V(R))delta(R)+(A+3)delta(R)^2
       +4c sqrt(y)[sqrt((1+rho(R))/y)+delta(R)]^2.             (15)

For every R>=e^3 and every finite admitted family we have proved

    E_(L_R)(g)>=[1-Delta(R)]S.                               (16)

In detail, a(R)=O_M(R^-1), eta,rho=O_M(R^-2), V(R)->1, and
delta(R)=O_(M,chi)(R^-2 y^-1/2). The last term of (15) equals

    4c[(1+rho(R))/sqrt(y)
           +2sqrt(1+rho(R))delta(R)+sqrt(y)delta(R)^2],

which tends to zero. Thus Delta(R)->0 with no dependence on J,K_R
or the profiles. By the definition of this scalar limit, one finite
R_*(M,chi)>=e^3 makes Delta(R)<=7/8 for every R>=R_*; equivalently,
(15) is an explicit sufficient scalar threshold to check. This
proves exactly (1). No numerical value or sharpness of the onset is
claimed. K_R>=2 follows from R>=e^3 and log3=2ell. If c is nonzero
then S>0, so (1) implies g is nonzero. For c=0 the inequality is an
equality, without any division by S.

### Qualifications and main-gap use

The common-window diagonal is obtained from pre-window estimates,
not by identifying K_R with K(t_j). The varying-profile Gram costs
use only their global H2 bounds. Every sum defining g is finite;
summable scalar majorants do not authorize a limit of forms as J
or L grows. Both exact complex poles vanish by the given correction,
and the whole arithmetic operator is paid in its original norm.

This pays the nominated weighted finite high block. C744o may help
with future couplings to a separately paid low block, but no such
block margin or many-block assembly is concluded here. The L745
carrier-span scope stop, L742 spatial-summability obstruction and
L750 corrected-IMS defect remain intact. In particular no neutral
space density, non-neutral sign, or actual-Xi positivity is inferred.

### Separate conceptual audit (11 November 2026, step506)

**Verdict and imported scope.** Equations (1)-(16) pass under their
stated hypotheses, with no mathematical repair. This REPRODUCTION
audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-11-dyadic-varying-carrier-audit-504.md`.
It reuses the inspected source statements and their local scalar,
Fourier and arithmetic specializations. In particular the finite
Schur theorem supplies only an upper matrix norm bound; the lower
energy estimate still requires all the checks below. This is
verification of a local input, not a new source theorem or an RH sign.

**Common window, domain and exact poles.** Since R>=e^3 and
2ell=log3, K_R>=2. For every finite J and K_R, all the cell sums
and their finite linear combinations are smooth and compactly
supported in (0,L_R). L744's domain calculation therefore applies
without a uniform domain norm or an infinite-window limit. The
Hermitian identity C744o(4) applies on this entire smooth space;
it is not restricted to unit or neutral inputs. Its two pole products
are conjugate on the diagonal and give the full factor two in (2).

For each j,k, multiplying the correction coefficient by G recovers
d_(j,k), with no complex conjugation. Thus each of the two local
moments of v_j vanishes exactly. Each global moment is a finite
sum of these zeros times exp(sigma k ell/2). The same holds for
g by finite complex linearity. Equation (3) consequently removes
both poles of the actual corrected sum, before separating f and h.
No large exponential weight multiplies an approximate cancellation.

L744(8)-(13) and C744n(4)-(5) are estimates for every finite K before
any window prescription. Their Fourier measure has mass one and
p-moment at most M^2. Their two integrations by parts in each cell
have no endpoint terms; squared derivative norms add across disjoint
cells. The correction constant is therefore exactly the H in (4),
independent of K. These facts verify the use of (4) at each t_j on
K_R even when K(t_j) differs from K_R. The final half-log conclusion
of C744n is not used as a common-window diagonal assertion.

**Pointwise comparison on the whole frequency line.** For i<j,
t_i<=t_j/2 gives t_j/2<=d<=t_j. The triangle inequality gives
2r>=d, while |xi|<=t_j+|xi-t_j|<=t_j+r<=5r. One p factor has
square root at least r^2 and the other has square root at least one.
Hence the quotient in (5) is bounded by
[A+log(2+5r)]/r^2 for every real xi. Its derivative is

    [5r/(2+5r)-2A-2log(2+5r)]/r^3 < 0  (r>=1).

Here r>=d/2>=R/2>1. Evaluation at d/2 gives the first bound
in (5); 2+5d/2<=3t_j follows from d<=t_j and t_j>=4.
This verifies the second bound including near xi=0, either carrier,
and arbitrarily far tails. Multiplication by the two p-weighted
Fourier absolute values followed by integral Cauchy--Schwarz yields
4M^2(A+log3+y_j)/d^2. Replacing d by t_j/2 proves (6).
The same argument with weight one proves (7). Neither estimate
uses pointwise decay constants of the profiles, disjoint Fourier
supports, a support-dependent L1 norm or higher derivative bounds.

**Both Schur maxima and the coefficient normalization.** Since
y_j>=3, (A+log3+y_j)<=[1+(A+log3)/3]y_j. After division by
sqrt(y_i y_j), this gives exactly the first expression in (9).
Also y_j/y_i=1+(j-i)log2/y_i<=1+(j-i), so its square root
is at most 1+(j-i). The larger-index part of row i is bounded
using sum_(n>=1)4^-n=1/3 and sum_(n>=1)n4^-n=4/9.
The smaller-index part is 4^-i i(i+3)/2 times D/R^2. At i=1,
i(i+3)=4^i; and 4i(i+3)-(i+1)(i+4)=3i^2+7i-4>0 for i>=1,
proving the induction used in the proof. The i=0 part is empty.
Thus the row bound is at most (7/9+1/2)D/R^2=23D/(18R^2),
strictly below eta(R). Hermitian symmetry makes each absolute
column sum a corresponding absolute row sum. Both maxima in the
imported finite Schur theorem are therefore paid independently of J.

With z_i=sqrt(y_i)c_i, the off-diagonal form is
sum z_i conj(z_j)G_ij=conj(z)^*G conj(z), where G is the
normalized remainder matrix. The operator norm bound gives absolute
value at most eta||z||_2^2=eta S, with the stated first-slot-linear
convention. No additional factor two is needed: both matrix triangles
are already included. This check applies separately to m and W.

For the unweighted L2 matrix, row i has at most i smaller indices,
each bounded by 16M^2 R^-2 4^-i; its larger-index sum is at most
(16M^2/R^2)4^-i/3. The inequality
4^-i(i+1/3)<=1 follows from i4^-i<=1/4 for i>=1 and
4^-i/3<=1/3, and is immediate at i=0. Column control again
follows from Hermitian symmetry. The diagonal equals one, so this
different matrix gives the unweighted synthesis bound in (10).

Every term of a(t) decreases for t>=e^3, including the last one
because 1-4(D0+log t)<0. The diagonal deficit is consequently at
most (log(2pi)+a(R))sum|c_j|^2<=(log(2pi)+a(R))S/y.
For W, U(t_j)<=y_j+D1; its diagonal contribution is at most
(1+D1/y)S. Combining these bounds with the respective Schur
estimates proves both lines of (10) and its preceding m lower bound.
There is no factor depending on the maximum y_j.

**Whole correction and logarithmic form cost.** Apply coefficient
Cauchy--Schwarz to the finite sum with factors sqrt(y_j)|c_j|
and 1/(sqrt(y_j)t_j^2). Since y_j>=y and t_j^4=16^j R^4,
the latter squared sum is at most 16/(15yR^4). This proves (11)
with delta=4H/(sqrt(15)R^2 sqrt(y)). It bounds h as a whole,
including arbitrary phases of its coefficients. Plancherel and
W<=(A+3)(1+xi^2) then give the stated W norm of h.

Expansion of Q_m(f-h,f-h)-Q_m(f,f) consists of two mixed terms
and the h diagonal. The majorant |m|<=W and weighted
Cauchy--Schwarz bound them by
2sqrt(VS)sqrt(A+3)delta sqrt(S)+(A+3)delta^2 S.
This is exactly (12); it does not require Q_m to be positive.
The ordinary norm triangle inequality with (10) and (11) gives
||f-h||_2<=sqrt(S)[sqrt((1+rho)/y)+delta], proving q(R)
without division by S or a potentially negative norm lower bound.

**Full arithmetic term and the uniform onset.** C744n(7)-(8)
applies for every finite L. The inclusive Rosser--Schoenfeld bound,
with its possible endpoint atom, bounds the strict prime-power sum
by 2c exp(L/2)-c. Each delay and adjoint is a contraction; the
factor two yields ||B_L||<=4c exp(L/2). A delay at L vanishes
almost everywhere. There is no restriction to primes or removal of
correction pairings. On L_R<=log y this is 4c sqrt(y); applying
it to g itself and its norm bound qS pays every arithmetic term.

Combining the m lower bound with exactly these two losses gives
the full Delta in (15), and hence (16), even if its right side is
negative at some finite R. For fixed M,chi, a(R)=O(R^-1),
eta,rho=O(R^-2), V->1 and delta=O(R^-2 y^-1/2). The first
four terms of Delta tend to zero. Its last term expands to

    4c[(1+rho)/sqrt(y)+2sqrt(1+rho)delta+sqrt(y)delta^2],

so it also tends to zero. All these functions depend only on R,M,chi
and the fixed ell. The definition of their scalar limit supplies
one R_* making Delta<=7/8 for every R>=R_*, without assuming
monotonicity of Delta or exchanging quantifiers over families.
Thus (1) holds for every finite J and all admitted profile choices.
For c=0 all forms vanish. For c!=0, S>0, so the floor implies
g!=0. An empty profile class asserts no existence, and no infinite
synthesis or form limit has been used.

**Use and limits.** The only direct local inputs remain L744,
C744n and C744o. The audited floor can pay this finite high block;
it supplies neither its coupling to a whole low block nor the
independent sign of that block. Non-neutral directions, general
test coverage and actual-Xi positivity remain unresolved. The
L742, L745 and L750 stops remain scope comparisons, not premises
or refuted claims. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of (1), the complete generator identity and
the quantitative varying-profile specialization is not checked.
The supporting Fourier and finite-matrix results are imported from
the precise mathematical sources above. No Lean theorem name or
formal certificate for this result is asserted; unknown coverage is
not evidence of absence.
