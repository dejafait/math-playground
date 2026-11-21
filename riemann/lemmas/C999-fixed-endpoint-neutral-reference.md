# C999: A fixed endpoint-preserving neutral lower reference and complete inverse-action procedure

## Hypotheses

Use C744v Section3's complex L2(0,ell), ell=log(3)/2, normalized
cosine basis e_n, diagonal D e_n=h(k_n)e_n, k_n=n*pi/ell, and full
positive response S. Its closed form domain is V; h(k_n)=O(log(2+n)).
Use C744z Section1's two-moment map C, H0=ker(C), V0=V intersect H0,
and actual restricted operator A0 represented by D+S. Inner products
are linear in the first slot. The moment representers are
w_c(x)=exp(cx), c=+/-1/2. Their real span is complexified when used
as H0-perp. Use the exact parity/reflection unitary U_par of C744v
and C999z, from the full cell to two copies of L2(0,a), a=ell/2.
Write C_end for the Carleman operator in C999z, to distinguish it
from the moment map C.

Import C999z's exact split and finite-rank kernels, including its
audit646. Fix delta=1/100, and the SMALLEST integers in its Section4
tolerance rules. They are m=286, J=14 as verified below. Set

    S_app=U_par^-1 diag(C_end/2+R_+;286,14,
                       C_end/2+R_-;286,14) U_par,
    B_trial=D+S_app-delta I                              (1)

on the full-cell form domain V. Its restriction to V0 on H0 is b0.
The symbol B0 below denotes the operator represented by this restriction,
not the compression of an unrestricted inverse.

Use C999k Section2 and audit6's complete qualified reference R:
R<=D+S+256C*C on V, R>=.239999 I. Its head floor and complete
complement, covariance, and IEEE754/Decimal/analytic contracts are
retained exactly. The fixed546 vector and .023083550 inverse-correction
bound are NOT used. No head factor or original source computation is
replayed here. C744z's original source-to-Xi, whole-core and unreplayed
c_* qualifications remain recorded; this proof does not validate them.
The new floor below uses R, not the numerical value of c_*.

Import the already assessed theorems from Gerald Teschl,
*Mathematical Methods in Quantum Mechanics*, GSM99, author version
12February2009: Theorem2.13 pp71-72 (closed-form representation),
Theorem2.18 p77 (lower spectral and resolvent bounds), Theorem6.4
p135 and Theorem6.24 p150 (bounded operator/form perturbations),
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
For inverse order use Behrndt--Hassi--de Snoo--Wietsma,
*Antitonicity of the inverse for selfadjoint matrices, operators, and
relations*, arXiv:1403.5704v1, Proposition2.1 p4, Corollary3.5 p12,
and the nonnegative proof case p11,
[pinned PDF](https://arxiv.org/pdf/1403.5704v1).
Their applicability and exact local specialization, rather than reproofs
of the general theorems, are the purpose of this result. Source coverage
is completed647 of review646 and construction assessment647.

For the computational diagonal use C744w Section3's exact digamma
recurrence and sector remainder, with its cited
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii). Elementary real constants
and functions below have certified rational enclosures converging to
their values, using their elementary power series and range reduction.
This is an exact-arithmetic algorithmic assertion, not reliance on an
unqualified library special function.

## Conclusion

The form b0 is densely defined, closed and represented by a unique
selfadjoint B0 on H0, with

    A0-2delta I <= B0 <= A0       (form order on V0),
    B0 >= beta I,   beta=.219999>0,
    0<=A0^-1<=B0^-1,  ||B0^-1||<=1/beta<4.546.          (2)

Its strong operator domain and action are

    Dom(B0)=Dom(D) intersect H0,
    B0 q=P0(Dq+S_app q-delta q),                         (3)

where P0 is the orthogonal projection onto H0. Exact-neutral finite
cosine sums form a strong operator core, not merely a form core.

For every complex f in H0 and q in Dom(B0),

    ||B0^-1 f-q|| <= ||f-B0 q||/beta.                   (4)

There is a terminating complete-residual procedure to achieve any
prescribed positive rational tolerance in (4), provided f is given
by certified L2 step approximations with errors tending effectively
to zero. Concretely the supplied steps have Gaussian rational values,
rational endpoints in x/ell, and certified error bounds refinable to
every requested positive accuracy. It covers arbitrary such complex
L2 data, with no smoothness, parity or finite-family restriction.
It includes the entire singular
output, forcing error, all finite-rank/diagonal actions and the neutral
projection. An unspecified abstract L2 element is not computational
input; no universal cutoff, complexity bound or implemented inverse
solver is claimed. An analytic estimate (4) holds even without an
effective representation of f.

This is a standard-method REPRODUCTION under the retained contracts,
not a new general inverse theorem or progress beyond the sources
checked. The construction and algorithmic proof were written648;
separate conceptual audit650 below upholds them under the retained
contracts. They prove no superiority to R,
uniform signed remote-plus-induced comparison, S3 positivity, C744q/H2
margin, non-neutral coverage, higher-endpoint bound, or RH. No possible
complete RH solution is asserted.

## Proof

### 1. Fixed integer rules and form order

Put H=303/16 and C_a as in C999z Section4. The smallest integers are
m=ceil(2H a^2/delta)=286 and
J=ceil(log(2C_a/delta)/(2a))=14. The max-with-1 and max-with-0
clauses do not change these values. In particular J is equivalently
the smallest nonnegative integer with C_a exp(-2aJ)<=delta/2.

The exact-rational certificate
`scripts/separation-seven/endpoint-reference-648.json` verifies these
claims using the full positive atanh(1/2) series tail for log(3) and
integer-power enclosures for 3^(1/8). It proves

    285 < 2H a^2/delta < 286,
    C_a exp(-26a) > .005,
    C_a exp(-28a) < .005,
    eta=H a^2/286+C_a exp(-28a)
        < .009308749378074894 < .01.                   (5)

These are complete scalar intervals, not floating-point diagnostics;
the inherited .239999 floor is identified as an assumed qualified
input in the certificate. Reproduce with

    python3 scripts/separation-seven/endpoint-reference-648.py

All six checks pass. No inverse or new reference matrix is sampled.

C999z bounds the error in EACH selfadjoint parity block by eta<=delta.
The norm of their direct sum is their maximum, and U_par is unitary.
Hence ||S_app-S||<=delta on full complex L2. The Hermitian error has
form values between -delta||v||^2 and +delta||v||^2. Subtracting
delta I in (1) therefore gives, on V and then V0,

    D+S-2delta I <= B_trial <= D+S.                    (6)

On V0, Cq=0, so C999k's full reference comparison gives

    b0(q,q) >= <Rq,q>-2delta||q||^2
              >=(.239999-.02)||q||^2=beta||q||^2.     (7)

For a general form-domain q, <Rq,q> denotes its reference form value;
no strong membership in Dom(R) is required. The certificate also
pays the slightly stronger floor .239999-delta-eta>.220690250621925106,
but (7)'s simpler beta suffices. This does not claim R<=B_trial.

The bounded selfadjoint S_app-delta I preserves D's closed semibounded
form on V and its full strong domain Dom(D), by the cited perturbation
theorems. V0 is closed in its shifted form norm since C is L2-bounded;
the bounded perturbation leaves that norm equivalent to V's original
weighted norm. C744z Section1 establishes that V0 is dense in H0.
Alternatively the neutral cosine density in Section2 below proves
this without any use of the value of c_*. Apply representation on H0,
not on the full space with a non-dense domain. It gives B0>=beta I.
The same lower bound for D+S follows from R on V0; the corresponding
operator is the already defined A0 by uniqueness. Equal form domains
V0 and (6) give the first order in (2). Inverse antitonicity for these
strictly positive selfadjoint operators gives A0^-1<=B0^-1. Teschl's
resolvent bound supplies ||B0^-1||<=1/beta; beta*(4.546)>1 proves
the displayed decimal bound. No projected unrestricted inverse is used.

### 2. Strong domain and an exact-neutral graph core

For c=+/-1/2, the exact C999k Section1 moment formula is

    <e_n,w_c>=nu_n c[(-1)^n exp(c ell)-1]/(1/4+k_n^2),
    nu_0=ell^(-1/2),   nu_n=sqrt(2/ell) for n>0.        (8)

It is O(n^-2) as n tends to infinity. Since |h(k_n)|=O(log(2+n)),
sum |h(k_n)|^2|<e_n,w_c>|^2 converges. Thus each w_c belongs to
Dom(D). They are linearly independent, and their Gram matrix is

    G=[[exp(ell)-1, ell],[ell, 1-exp(-ell)]].           (9)

It is strictly positive: equality in Cauchy--Schwarz would make the
two distinct exponentials proportional almost everywhere, which they
are not. Consequently the L2 projection onto their span maps L2
boundedly into Dom(D) with its graph norm. In particular P0 preserves
Dom(D) and V. Every v in V decomposes as v0+w, v0 in V0 and w in
W=span{w_+,w_-} subset Dom(D).

Write K_b=S_app-delta I, a bounded selfadjoint operator. If
q in Dom(D) intersect H0, then for v in V0,
b0(q,v)=<Dq+K_b q,v>=<P0(Dq+K_b q),v>. Representation proves
membership in Dom(B0) and the action in (3).

Conversely let q in Dom(B0), so q in V0 and some u in H0 represents
b0(q,v0) for all v0 in V0. In the decomposition above,

    b_full(q,v)=<u,v0>+b_full(q,w),
    b_full(q,w)=<q,(D+K_b)w>.

The last equality is valid for q in V and w in Dom(D), by the
diagonal form identity and boundedness of K_b. On the finite-dimensional
W it is a bounded functional in ||w||_2. The projection defining the
decomposition is L2-bounded, so the displayed functional on all V is
bounded in ||v||_2. The full-space representation theorem therefore
places q in Dom(D+K_b)=Dom(D). This proves (3), including its converse;
the argument does not infer a strong core from a form core.

For density let P_N truncate cosine modes0,...,N. For any
q in Dom(D) intersect H0, P_N q converges to q in the D graph norm.
Let M be the two by two moment matrix with columns C e_0, C e_1.
It is invertible. Indeed in (8) the ratio of its plus and minus
entries is +exp(ell/2) for n even and -exp(ell/2) for n odd; all
four entries at n=0,1 are nonzero. Define

    q_N=P_N q-(e_0,e_1)M^-1 C(P_N q).                 (10)

Then Cq_N=0 exactly. The correction tends to zero in the D graph
norm since C(P_N q) tends to Cq=0 and e_0,e_1 are fixed in Dom(D).
By (3) and boundedness of K_b and P0, q_N converges in the B0 graph
norm. The same argument applied to q in H0, using only L2 convergence,
proves L2 density of V0 claimed above.

For an EFFECTIVE countable trial family take finitely many free
coefficients q_n in Q+iQ, n>=2, and set, for p=0,1,

    q_p=-sum_(n>=2, n mod2=p) r_n q_n,
    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2).            (11)

Equation (8) proves exact neutrality for both moments separately.
All coefficients are computable exact real/complex numbers; neutral
membership is an algebraic identity, never a rounded residual test.
Rational approximation of the free coefficients in each finite space
and (10) prove graph density of this countable family. Finite sums
of computable trigonometric functions in (11) are Lipschitz on the
closed full cell and on both reflected parity intervals.

### 3. A complete effective singular-action certificate

Here v is one smooth parity input from a trial in (11). For any step
p=sum b_i 1_[alpha_i,beta_i] on a partition of [0,a], all b_i complex,
the FULL Carleman action is, for t>0,

    (C_end p)(t)=sum_i b_i log((t+beta_i)/(t+alpha_i)). (12)

This follows by integration of 1/(t+s) on each input interval. There
is no integral or operator interchange. Coefficients can be dyadic
approximations to v at interval midpoints. If v has a certified
Lipschitz bound L and the input mesh is at most d_in, and midpoint
value errors are at most e_in, then

    ||v-p||_2 <= sqrt(a)(L d_in/2+e_in).               (13)

C999z's weighted Schur bound gives
||C_end(v-p)||_2<=pi||v-p||_2. It applies to the actual singular
operator, not to a Hilbert--Schmidt surrogate.

Put M_p=max_i |b_i|, or any certified upper bound for it. Positivity
of 1/(t+s), used only to bound absolute values, gives

    |C_end p(t)|<=M_p log((t+a)/t).

For 0<tau<=a and 0<t<tau, this is at most M_p log(2a/t).
The exact integrable majorant is

    ||1_(0,tau) C_end p||_2^2
       <=M_p^2 tau[L_tau^2+2L_tau+2],
    L_tau=log(2a/tau).                                (14)

To verify the endpoint term, substitute t=tau u and integrate
(L_tau-log u)^2 on (0,1); the three integrals are 1,1,2 for
1,-log u,(-log u)^2, respectively. Equivalently use the elementary
antiderivative and t(log t)^2 tending to zero at zero. Thus no
unpaid interval or infinite output remains. At tau=a*2^-s the bound
is M_p^2 a*2^-s[((s+1)log2)^2+2(s+1)log2+2], tending effectively
to zero for fixed p.

On [tau,a] differentiate the finite integral (12):

    |(C_end p)'(t)|
       <=M_p integral_0^a (t+s)^(-2) ds<=M_p/tau.      (15)

Approximate (12) by midpoint steps on this OUTPUT interval with mesh
at most d_out and scalar value errors at most e_out. Set the output
approximation to zero on (0,tau). Combining (13)--(15), its entire
L2 error relative to C_end v is at most

    pi sqrt(a)(L d_in/2+e_in)
    +M_p sqrt(tau[L_tau^2+2L_tau+2])
    +sqrt(a)(M_p d_out/(2tau)+e_out).                 (16)

The last term may use sqrt(a-tau); sqrt(a) is a safe upper bound.
First choose p to pay the first term, then tau to pay the second,
then the output mesh and scalar precision to pay the third. This
sequential order matters: no bound uniform in the changing M_p is
assumed. Every prescribed positive action tolerance is reached by
these explicit choices. For p=0 all terms can be set to zero directly.
The coefficient1/2 in (1) is retained. For the two blocks with action
errors E_+,E_- the full-cell singular-action error is at most
sqrt(E_+^2+E_-^2)/2, by unitarity. This includes complex inputs.

### 4. Every other action and the projected residual norm

There are finitely many other terms, but their ENTIRE output is needed.
For the fixed remainder, C999z(12) gives exactly

    (h_m v)(t)=sum_i 1_Ii(t) sum_k h(xi_i+xi_k) integral_Ik v(s)ds,

and for epsilon in {+1,-1}, each j=0,...,13 contributes

    E_epsilon,j v=
      [epsilon b_j phi_j <v,phi_j>+psi_j <v,psi_j>
       +epsilon phi_j <v,psi_j>+epsilon psi_j <v,phi_j>]
       /(1-epsilon b_j).                              (17)

All functions phi_j,psi_j are the real exponentials of C999z
Section1; (17) uses the first-slot-linear convention. Both cross
products and j=0 are included. The denominators are at least
d=1-exp(-a)>0; h evaluations have arguments at least a/m>0.
Thus every coefficient in this FINITE formula has arbitrarily tight
certified elementary enclosures. Integrals of the finite trigonometric
v against indicators or exponentials can either be integrated directly
or bounded by midpoint integration: for a Lipschitz function F on
an interval of length l, the integral error is at most l Lip(F)d_mesh/2,
plus the length times scalar value error. For a complex F, apply the
same absolute-value bound; explicit derivative sums supply Lip(F).
Output exponentials have bounded derivatives on [0,a] and hence
converging step approximations with the bound used in (13).

To propagate errors in each coefficient times output function use

    ||c u-c_hat u_hat||_2
       <=|c-c_hat| ||u||_2+|c_hat| ||u-u_hat||_2.       (18)

Finite triangle summation pays every term of (17) and h_m, with any
desired total error allocation. There is no omitted response tail
in the ACTION of B_trial: B_trial uses exactly the finite remainder
and the full C_end. C999z's eta is used for order in Section1, not
silently subtracted a second time from this action.

Dq is a finite cosine sum. For any positive integer K and real k,
C744w's recurrence/remainder argument at z=1/4+ik/2 gives

    psi(z)=log(z+K)-1/[2(z+K)]-sum_(j=0)^(K-1)1/(z+j)+E,
    |E|<=sqrt(2)/[6((K+1/4)^2+k^2/4)].                (19)

This is its cited sector estimate with64 replaced by K; Re(z+K)>0
and |arg(z+K)|<pi/2 check all the same hypotheses. Only the real
part is needed, with Re log(z+K)=log|z+K|. Its error tends to zero
as K grows, including k=0. Reciprocals have nonzero denominators;
logs and real parts are elementary. Hence each of the finitely many
h(k_n) and each coefficient of Dq has a certified approximation at
arbitrary precision. A finite trigonometric derivative bound then
produces full-output step approximations to Dq. The term delta q is
handled the same way. The fixed finite value of the largest frequency
may enlarge the needed work but causes no convergence obstruction.

Combine these approximations, (16), and the exact unitary inverse
parity/reflection map. They give full-cell steps z_l and certified
E_l tending effectively to zero such that

    ||B_trial q-z_l||_2<=E_l.                         (20)

The meshes can be refined together: the unitary uses only reflections,
translations, signs and the fixed sqrt(2), so maps the step outputs
to full-cell steps with certified scalar errors. An enclosure of an
exact scalar step value can always be replaced by a dyadic value,
charging sqrt(length) times its error in (20).

For completeness the projection has an explicit full-norm certificate.
For any full-cell step u, its two moments d=Cu are finite sums using

    integral_alpha^beta exp(cx)dx
       =[exp(c beta)-exp(c alpha)]/c.

With G from (9),

    ||P0 u||_2^2=||u||_2^2-d^*G^-1 d.                (21)

This is the orthogonal-projection identity, obtained by solving its
two by two Gram system. G is real symmetric positive definite, so
there is no conjugation ambiguity for complex u. All step lengths,
coefficients, moments and G entries are computable with arbitrarily
tight intervals; det(G)>0 can be certified by refinement since it
is strictly positive. Intersect a squared-norm enclosure with [0,infinity)
and take its nonnegative square root. Even when the true norm is zero,
the resulting upper bounds tend to zero. Exact positivity of a tiny
computed difference is never assumed.

Let f_l be supplied step data with ||f-f_l||_2<=e_l, e_l tending
effectively to zero. Refine f_l and z_l to a common step partition.
Using (3), f=P0f, ||P0||=1 and (20) yields

    ||f-B0 q||_2
       <=||P0(f_l-z_l)||_2+e_l+E_l.                  (22)

Equation (21), with its scalar error paid, gives arbitrarily tight
upper bounds for the first term. The three allowances in (22) cover
the entire residual. In particular B_trial q need not itself be
neutral; using an unprojected residual would generally not give a
converging solve. Formula (21) computes a projection of the ACTION,
not a projected unrestricted inverse.

### 5. Error estimate and effective termination

Let q*=B0^-1 f. For any strong-domain q,

    q*-q=B0^-1(f-B0 q).

The lower spectral bound gives (4). Thus an upper bound rho from
(22) certifies error <=rho/beta, including every full-output error.
For a prescribed positive rational epsilon, accept only when a rational
upper enclosure for rho is strictly below beta*epsilon.

Here is a terminating algorithm rather than an assumed convergence
of an uncontrolled finite inverse. Enumerate the trial family (11)
by increasing finite support, rational numerator/denominator heights
and real/imaginary parts. At stage s process the first s trials,
and for each compute (22)'s upper bound with forcing, action and
scalar norm errors each below2^-s. Require the input representation
to return a step approximation at a requested L2 accuracy; a sequence
with certified errors effectively tending to zero is equivalent by
searching those error bounds. Each stage is finite. The construction
in Sections3--4 and the input contract make every requested refinement
terminate. Test the strict acceptance condition after each certificate.

By Section2 graph density, there exists a trial q_i with
||f-B0 q_i||_2<beta*epsilon/2: approximate q* in the B0 graph norm.
This is an existence fact used to prove termination, not a presumed
computable convergence rate for q*. For that fixed i, (20)--(22) and
the norm enclosures converge to its actual residual norm. For all
sufficiently large stages s>=i their upper bound is below
beta*epsilon, so the algorithm stops and returns a certified trial.
There is no need to know i or that stage in advance. The algorithm
may be very slow; it is an explicit terminating search with complete
computable certificates, not merely qualitative existence of an inverse.
It neither assumes computability of an unspecified f nor asserts a
uniform finite cutoff independent of supplied data.

All steps retain both parity endpoint operators and the fixed286/14
remainders. No actual signed remote operator was approximated or
tested in this construction. The fixed32,598 rank-two and600/603/635
stops remain intact. A later comparison must still pay both induced
coupling terms and the original remote term together; (2)--(4) alone
give none of their signs.

### 6. Separate conceptual audit — 12 November 2026, step650

**Scope and result.** Reuse the unchanged SPECIALIZE assessment648,
separately approved649, and the inspected primary cases in completed647
of review646. All of (1)--(22) survive; no mathematical correction or
parameter change is required. This is REPRODUCTION: a verified local
application of the cited representation, bounded-perturbation, inverse-
order and resolvent results. No general theorem is reproved, and no new
source coverage or originality is claimed. The floor supplied by C999k
and the original analytic/arithmetic/source-to-Xi/whole-core/c_* contracts
are retained, not independently replayed by this audit. In particular
the new proof of the neutral cosine strong core does not validate the
original smooth-source identification with Xi.

**Complete scalar replay and form order.** The original exact-rational
generator was read in full. The independent audit reads every complete
rational interval of `scripts/separation-seven/endpoint-reference-648.json`,
checks each enclosure and every displayed decimal outwardly, and uses
a separate120-term positive-series enclosure for log(3). For n terms,
the sum is sum_(j<n)1/[(2j+1)2^(2j)] and its entire positive tail is
at most4/[3(2n+1)2^(2n)]; division by4 encloses a. The stored eighth-
root endpoints are verified by exact eighth powers. For r>1, the
positive denominator r(1-r^-2)(1-r^-4) increases, giving the two
endpoints used for C_a. Integer powers, positive quotients and sums
then verify all the remaining stored intervals without rounding.

Reproduce with

    python3 scripts/separation-seven/endpoint-reference-audit-650.py

Full evidence: `scripts/separation-seven/endpoint-reference-audit-650.json`.
All33 checks pass with no failures. The original648 certificate, SHA256
`77ff397acbfaf8d540005c69fd14b0248d461424d5a271ee8f9ae1917d80ceb2`,
is preserved. The actual bounds are

    285.707449317353390 < m_rule < 285.707449317353391,
    tail_J13 > .00747183145260114838 > .005,
    tail_J14 < .00431386390049878553 < .005,
    eta < .00930874937807489374 < .01,
    .239999-delta-eta > .220690250621925106 > .219999.

Since exp(-2a)<1, the failed J=13 and passed J=14 certify minimality
among all nonnegative integers; the m interval similarly certifies286.
The exact check beta*4.546>1 pays the inverse norm bound. The replay
certifies scalar specialization only, not a new factorization of R.

For the operator order, both parity errors are selfadjoint. A direct
sum has the maximum of their norms, not their sum, and the imported
unitary includes its sqrt(2) normalization. Thus subtracting delta
gives precisely the interval [-2delta,0] relative to D+S on V.
C999k's R<=D+S+256C*C holds on the whole form domain; restricting
to V0 removes the penalty and loses at most2delta. Its head floor
.239999 and complementary floor greater than3.07 give (7), with no
finite-head substitution for the full form. Bounded perturbation
preserves closedness on V; continuity of C makes V0 closed in the
equivalent shifted form norm. The density argument below is on H0.
Representation therefore applies there. Both A0 and B0 are strictly
positive with the same form domain V0, so the cited antitonicity theorem
has the required domain and positivity hypotheses. This proves the
stated inverse direction; it does not prove R<=B_trial or identify
any restricted inverse with P0 times an unrestricted inverse times P0.

**Both strong-domain inclusions and graph density.** Direct integration
in (8), including n=0, has denominator c^2+k_n^2=1/4+k_n^2. Its
O(n^-2) decay makes sum_n |h(k_n)|^2|<e_n,w_c>|^2 finite since h
grows at most logarithmically. The Gram entries (9) are the exact
integrals of exp(x),1,exp(-x). The two representers are independent,
so G is strictly positive. Consequently projection onto their span
W is L2-bounded into Dom(D) with its graph norm, and P0 preserves
both Dom(D) and V. This checks the decomposition for EVERY v in V.

The forward domain inclusion follows by testing Dq+K_b q against
all V0. For the reverse inclusion, if u represents b0(q,.) on V0,
write v=P0v+P_Wv. Then the full form is

    <u,P0v>+<q,(D+K_b)P_Wv>.

The map (D+K_b)P_W is bounded on L2 because W is finite dimensional
inside Dom(D). Hence this is a bounded conjugate-linear functional
of v in its L2 norm. Full-space form representation gives
q in Dom(D+K_b)=Dom(D). No merely form-norm estimate is substituted
for that L2 boundedness. The representing vector on H0 is exactly
P0(D+K_b)q, proving both parts of (3).

For n even, the ratio C_+(e_n)/C_-(e_n) is +exp(ell/2);
for n odd it is -exp(ell/2). All n=0,1 moments are nonzero, so
the two columns used in M are independent. Diagonal truncation
converges in the D graph norm. The correction in (10) has fixed
finite support and coefficients tending to zero, so it also tends
to zero in that norm. Formula (3) transfers this convergence to
the B0 graph norm. Applying the same correction to ordinary L2
truncations proves density in H0, without appealing to c_*.
Within each parity, the ratio in (11) is independent of c; thus
both moments vanish exactly even for complex free coefficients.
In any fixed finite space the completion map is continuous in the
D graph norm. Gaussian-rational approximation of its free coordinates
and the preceding truncations therefore make the enumerable trial
family a strong core. This is sufficient for approximating B0^-1 f;
no equality of the two graph norms needs to be assumed.

**Complete singular action.** Formula (12) integrates each input step
exactly for t>0, even for the interval starting at zero. Its logarithmic
divergence there is not omitted from the L2 output. The input error
is a uniform midpoint error times sqrt(a), followed by the actual
Carleman norm bound pi. On (0,tau), the absolute value of the complex
step action is bounded by M_p log(2a/t). The integral of its square is
exactly the right side of (14), by the stated integrals1,1,2. For
tau=a*2^-s its polynomial-in-s factor times2^-s tends effectively
to zero. The input step p is fixed BEFORE this search, so M_p does
not vary while shrinking tau.

On [tau,a], differentiating the finite logarithmic sum gives an
absolute derivative at most M_p integral_0^a(t+s)^(-2)ds<=M_p/tau,
including complex coefficients by the triangle inequality. The final
midpoint output error is therefore exactly bounded by the third term
of (16). The three errors can each receive any fixed positive fraction
of the desired tolerance, in their stated sequential order. For two
parities, the complete error after multiplying by1/2 and applying the
unitary is sqrt(E_+^2+E_-^2)/2. There is no uncomputed endpoint interval,
Hilbert-Schmidt assumption on C_end or missing normalization factor.

**Other actions, projection and arbitrary data.** Expanding the real
symmetric correction kernel from C999z gives all four terms of (17)
with the displayed signs in the first-slot-linear convention. The
denominators are at least1-exp(-a)>0 for BOTH parities and all j=0:13.
The midpoint kernel has only positive evaluation arguments. Thus all
coefficient integrals and full output functions are computable with
the derivative bounds and product error (18); finite summation pays
every term. The response approximation error eta is already paid in
the order comparison and is not a fixed residual error to be paid at
each solve. No omitted response tail belongs to B_trial's action.

For (19), each z+j has positive real part, while z+K has
|arg(z+K)|<pi/2. The retained DLMF sector factor is at most2sqrt(2);
the first omitted coefficient1/12 gives exactly sqrt(2)/(6|z+K|^2).
The exact recurrence has the minus sign shown. Letting integer K grow
gives arbitrary precision also at k=0. Only Re log(z+K)=log|z+K|
is used. A finite q needs finitely many such values and finite
trigonometric derivative bounds, so its entire D action is effective.

All meshes may be chosen with rational endpoints in t/a or x/ell.
Reflection/translation maps them to rational full-cell endpoints,
so common refinements require only rational comparisons, not deciding
equality of arbitrary computable reals. Scalar value approximations
and the fixed sqrt(2) are charged in (20). For a step u, writing its
moment vector d=Cu, the projection coefficients solve G alpha=d.
With G real symmetric, its W-projection squared norm is d*G^-1d for
complex d under the stated convention; subtraction gives (21).
Interval refinement eventually certifies det(G)>0. The resulting norm
enclosure converges even at zero after intersecting with [0,infinity)
and taking square roots. No cancellation sign is assumed numerically.

The supplied forcing contract gives arbitrarily accurate step data;
its exact membership in H0 is a mathematical hypothesis, not something
decided from approximate moments. For a fixed trial q let
r=f-B0q and r_l=P0(f_l-z_l). Then

    ||r_l-r||<=e_l+E_l.

If n_l is the computed norm upper bound with
0<=n_l-||r_l||<=s_l, the certified rho_l=n_l+e_l+E_l satisfies

    ||r||<=rho_l<=||r||+2(e_l+E_l)+s_l.

This explicitly checks convergence of the COMPLETE projected residual,
not only of a finite output or an unprojected action. At stage s the
three allowances below2^-s make the excess at most5*2^-s.
Strong-core density supplies a fixed trial with residual strictly below
beta*epsilon/2. After its enumeration index, a sufficiently large finite
stage has5*2^-s<beta*epsilon/2 and therefore passes strict acceptance.
Every stage has finitely many trials and each requested refinement
terminates. The spectral identity (4) then certifies the returned error.
This proves effective termination for the stipulated input representation,
without a computable convergence rate for an arbitrary unspecified f,
a universal cutoff, a complexity estimate or an implemented inverse solve.

The600/603/635/640 and fixed32 stops are preserved. This audit establishes
the usability of C999 as a qualified inverse input; it establishes no
signed remote-plus-induced comparison or progress beyond checked sources.

## Mathlib

A full matching theorem for this fixed two-parity reference, its neutral
strong core and the complete effective arbitrary-data inverse procedure
has not been checked in Mathlib. The precise named source theorems above
support the closed-form, bounded-perturbation and inverse-order steps;
finite-dimensional Gram projection, scalar integration and Hilbert-space
norm inequalities are supporting mathematics. This is not a formalization
or proof of absence from Mathlib. Separate audit650 upholds construction648
under its retained analytic and arithmetic qualifications; full matching
Mathlib coverage remains unchecked.
