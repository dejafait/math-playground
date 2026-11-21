# C744l: Three-piece power-log reduction for the neutral Schur matrices

## Hypotheses

Use C744j's exact complex neutral graph and C744k's N=256 action,
degree96 regular-kernel approximants and finite matrices. Work in the
unitary coordinate v=x/ell on (0,1), with ell=log(3)/2,
d=log(2), a=d/sqrt(2), b=d/ell-1, and

    Zc=g(v)=sum_(n=2)^256 c_n sqrt(2n+1)
                  [P_n(2v-1)-r_n sqrt((2e+1)/(2n+1))P_e(2v-1)],
    e=n mod2, r_n as in C744j(5)-(6).

Thus ||Z||<51/50. Let P_N be orthogonal projection onto degrees<=256
and Q_N=I-P_N. Inner products are linear in their first argument;
all displayed matrices use the corresponding Hermitian quadratic-form
convention. No RH, support collar, energy shift or H2 cap is assumed.

The general spectral and Schur tools are the same known inputs as
in C744j: Gerontogiannis--Mesland, arXiv:2309.16636v2,
[Proposition5.8 and Section2](https://arxiv.org/pdf/2309.16636v2),
and the complete-covariance square completion compared with Li,
[paper45 displayed v2, Sections4-5, (4.1)-(5.5)](https://rstation.ai/problems/riemann_hypothesis/papers/45).
They are not reproved or used to assert any finite matrix sign.
The additional computations below are elementary Taylor and power-log
integration formulas needed to evaluate this specific application;
the unchanged step483 EXPLORE assessment covers that application.

## Conclusion

There is an explicitly defined real piecewise polynomial-log map T_s,
for each s=-1,+1, on the three intervals (0,b),(b,1/2),(1/2,1).
On each interval, after an affine change to 0<t<1, each column is

    P_(s,j,i)(t)+Q_(s,j,i)(t)log(t),
    deg P_(s,j,i)<=1024, deg Q_(s,j,i)<=256, Q_(s,1,i)=0.  (1)

Here j=0,1,2 labels intervals and i=2,...,256 labels columns. Define
the exactly Hermitian matrices

    M_T,s=(Z^*T_s+T_s^*Z)/2,
    R_T,s=T_s^*T_s-(P_N T_s)^*(P_N T_s),
    S_T,s=M_T,s-(250/171)R_T,s.                          (2)

Every entry of (2) is a finite sum of polynomial coefficients times
the exact moments

    int_0^1 t^k (log t)^r dt=(-1)^r r!/(k+1)^(r+1),
    r=0,1,2, 0<=k<=2048.                               (3)

No numerical quadrature, mixed-log special function or numerical
Carleman recurrence is needed to evaluate this representation.
Coefficient arithmetic and cancellation are still essential.

For C744j's exact M_s,R_s, both signs satisfy

    M_s-(250/171)R_s >= S_T,s-2*10^(-19) I.              (4)

Consequently S_T,s>=I/25 for both signs suffices, under the retained
analytic reductions, for the original full neutral forms to have a common
margin mu>1/30. Section8 records both full255-dimensional matrix
inequalities. Section9's separate conceptual audit accepts the analytic
implication, with margin mu>9/260, conditional on those finite inequalities
for the exact maps defined here. Section10 audits the action source and
freshly reproduces all coefficient and projection operands. Section11
checks all native inputs and freshly reproduces every midpoint Gram
product, then certifies both complete finite signs with a separate LDL
implementation. Together these audits establish (13), hence beta_1<1/2
on the stated exact neutral class. GMP and the reviewed high-level scalar/
action formulas remain shared implementation inputs. No global positivity
or RH conclusion is asserted.

The Section5 integer-arithmetic certificate encloses the scalar inputs
and all255 exact r_n in intervals of width<10^(-600). Sections6-7 record
the earlier3- and17-column principal enclosures. Section8 propagates
all scalar and coefficient uncertainties through all255 action columns,
all257 projection rows and every finite coupling. Section9 specifies the
precise analytic portions of C744i/j/k accepted in its audit; it does not
audit C744i's separate sharp-tail theorem. Remote, non-neutral, odd and
all-window signs remain open.

## Proof

### 1. One-sided rational replacement of the scalar

C744k's exact potential in this coordinate is

    c_0-(1/2)log(v(1-v)), c_0=-gamma-log(2pi ell).

Set c_*=-183/100. We have c_0>c_*: C744j's elementary bounds give
gamma<293/500, pi<22/7 and ell<11/20. Hence 2pi ell<121/35.
The positive degree20 Taylor prefix for exp(311/250) is larger
than 121/35, as checked exactly in the certificate. Therefore
gamma+log(2pi ell)<293/500+311/250=183/100.

Let A_tilde_s=A_hat_s-(c_0-c_*)Z, using C744k's A_hat_s.
Since Q_N Z=0, its uncorrected covariance equals that of A_hat_s:

    A_tilde_s^*Q_N A_tilde_s=A_hat_s^*Q_N A_hat_s.

Its finite quadratic form is smaller by (c_0-c_*)Z^*Z>=0.
Thus the associated Schur matrix S_tilde_s is <=S_hat_s in
Hermitian order. This replacement is a lower comparison for the
original unshifted energy; the target form has not been redefined.
C744k(3) still pays the actual moment-graph coupling correction.

C744k gives ||A_hat_s||<501 and |c_0|<3. Since |c_*|<2,

    ||A_tilde_s||<501+5(51/50)<510.                      (5)

The large bound is used only to pay approximation error; it is not
a lower bound or spectral estimate.

### 2. Three affine pieces and uniform logarithm approximants

The strict inequalities 256>243 and 8<9 imply

    1/4 < b=2log2/log3-1 < 1/3.

Indeed the lower inequality is 8log2>5log3; the upper is
3log2<2log3. Define

    L_-(u)=-sum_(k=1)^768 u^k/k,
    L_+(u)= sum_(k=1)^768 (-1)^(k+1)u^k/k.

For 0<=u<=1/2, each differs from log(1-u) or log(1+u), respectively,
by at most

    delta=2^(-768)/769.                                (6)

This follows by integrating the geometric series, or by bounding
its absolute tail sum by u^769/[769(1-u)]. The same bound is valid
at u=1/2. Apply the following substitutions to the three logarithms
in C744k(10), while keeping all its polynomial and reflection terms:

    j=0: v=bt, length b:
      log v       = log b + log t                       (exact),
      log(1-v)   -> L_-(bt),
      log(1+v)   -> L_+(bt).

    j=1: v=1/2-(1/2-b)t, length 1/2-b, w=(1-2b)t:
      log v      -> -log2+L_-(w),
      log(1-v)   -> -log2+L_+(w),
      log(1+v)   -> log(3/2)+L_-(w/3).

    j=2: v=1-t/2, length 1/2:
      log v      -> L_-(t/2),
      log(1-v)    = -log2+log t                         (exact),
      log(1+v)   -> log2+L_-(t/4).

Every series argument lies in [0,1/2], using 1/4<b<1/3.
The negative affine orientations in pieces1 and2 are absorbed by
the positive interval lengths in integration. The full partial
reflection is zero on piece0 and is g(d/ell-v) on pieces1 and2.
Values at the finitely many endpoints do not affect any L2 integral.

Apply these replacements to A_tilde_s to define T_s. C744k(10)'s
polynomial portion has degree<=353 and each log coefficient has
degree<=256, so the new polynomial degree is <=256+768=1024.
The only retained log coefficients are

    Q_(s,0)(t)=-g(bt)/2-s g(-bt),
    Q_(s,2)(t)=-g(1-t/2)/2,

and Q_(s,1)=0. This proves the representation (1), with the full
reflection jump retained. The construction uses exact finite formulas;
it does not assert that their coefficients have been numerically enclosed.

### 3. Paying cancellation in the log replacement

The individual log coefficients are -g(v)/2-sg(-v), -g(v)/2
and sg(-v). It would be invalid to omit the off-interval growth
of g(-v) when charging their log approximation. Here is an explicit
whole-map bound that includes it.

For 1<=x<=3, Laplace's polynomial representation gives

    |P_n(x)| <= (x+sqrt(x^2-1))^n < 6^n.

At n=0 use <=1. This is the same generating-function representation
used in C744k Section2; for x>=1 the integral is
pi^(-1)int_0^pi (x+sqrt(x^2-1)cos(theta))^n dtheta.
Its generating series is (1-2xz+z^2)^(-1/2) near z=0,
so equality of coefficients justifies the representation without
assuming an asymptotic formula. Parity covers -3<=x<=-1.
Consequently, by Cauchy--Schwarz in the orthonormal shifted basis,

    sup_(0<=v<=1)|g(-v)|
      <= [sum_(n=0)^256 (2n+1)6^(2n)]^(1/2)||g||_2
      <=257*6^256 ||g||_2
      <(51/50)257*6^256 |c|.

Using (6), the pointwise error is at most
delta(|g(v)|+2|g(-v)|). Taking L2 norms over the entire unit interval
therefore gives the joint 255-column map bound

    ||T_s-A_tilde_s|| <= epsilon_L,
    epsilon_L=delta(51/50)(1+514*6^256)
              <7.069*10^(-33)<10^(-30).                 (7)

This is not a per-column estimate, a sampled residual or a floating
point evaluation bound. It explicitly pays the large cancelling
off-interval polynomial values. The singular log t terms are exact.

Since ||T_s||<511 by (5)-(7), the elementary Gram perturbation
identity, also used in C744k(11), gives

    ||T_s^*Q_N T_s-A_tilde_s^*Q_N A_tilde_s||
         <=(2*511+1)epsilon_L=1023epsilon_L.

The symmetrized finite head error is at most ||Z||epsilon_L<2epsilon_L.
Symmetrization is required: the separate log replacements need not
define a self-adjoint operator, even though A_tilde_s does. Hence

    S_tilde_s >= S_T,s-epsilon_SL I,
    epsilon_SL=[2+(250/171)1023]epsilon_L
                <1.059*10^(-29)<10^(-19).               (8)

Combining S_hat_s>=S_tilde_s, (8) and C744k(3) proves (4).
If both finite matrices were >=I/25, their original Schur margins
would exceed 1/25-2*10^(-19)>9/250. The complementary reserve from
rho=19/20 and floor18/25 is 9/250. C744j(4) and eta^2<1/25 then
give mu>(9/250)/(26/25)=9/260>1/30. No matrix sign is assumed as
an established result in this conditional implication.

### 4. Exact integration functional

For k>=0, substitute t=exp(-u) to obtain
int_0^1 t^k (log t)^r dt=(-1)^r int_0^infinity u^r exp(-(k+1)u)du.
For r=0,1,2, integration by parts evaluates this as (3); all boundary
terms vanish and the integrals converge absolutely. Thus for real
column coefficients P_i(t)=sum p_(i,m)t^m and Q_i(t)=sum q_(i,m)t^m,
the Gram entry on one piece of length L is exactly

    L sum_(m,n) [p_(i,m)p_(j,n)/(m+n+1)
       -(p_(i,m)q_(j,n)+q_(i,m)p_(j,n))/(m+n+1)^2
       +2q_(i,m)q_(j,n)/(m+n+1)^3].                     (9)

Use conjugates on the first coefficient for complex column
representations; the actual basis and action columns here are real.
Head entries and all projected moments are the same formula with
one Q polynomial zero and P the appropriately composed Z column
or normalized Legendre polynomial. Sum (9) with lengths b,1/2-b,1/2.
The complete covariance then uses all 257 projection rows, exactly
as in (2). Nothing is inferred from a truncated positive covariance
or from discarding a negative floating point eigenvalue.

Degrees in (1) show that k<=2048 suffices for every product. Equation
(9) is a finite evaluation scheme, not a lower spectral bound. It
does not protect an implementation using insufficient precision:
the power-basis coefficients and subtraction of the projection can
cancel strongly. Their interval errors must still be propagated.

### 5. Certified scalar inputs and certificate scope

Run `python3 scripts/adjacent-neutral/power-log-enclosure-486.py`.
It writes `scripts/adjacent-neutral/power-log-enclosure-486.json`.
All intervals have exact integer endpoints divided by 2^2048.
Addition/subtraction use exact endpoint arithmetic; multiplication
and positive-denominator division take all four corners and round
outward with integer floor/ceiling. Square roots use integer square
root and the next integer unless the upper radicand is a square.
These operations enclose their exact real arguments by monotonicity
or the elementary rectangle extrema; no hardware rounding assumption
or external numerical library is involved.

For x in [1,2], set z=(x-1)/(x+1) in [0,1/3]. The first700 terms
of 2sum z^(2k+1)/(2k+1) enclose log x after adding the positive
remainder interval with upper endpoint

    2/[1401*3^1401*(1-1/9)].

The identity follows by integrating the uniformly convergent geometric
series on each compact subinterval of (-1,1); the displayed geometric
tail bound holds at z=1/3 as well. First compute log2 and log(3/2),
then log3, ell, b, log b=log(4b)-2log2, sqrt2, a and t=ell/4.
The already proved 1/4<b<1/3 ensures that 4b is in [1,2]. Runtime
endpoint assertions also verify the interval arguments of this formula.

For all n=0,...,256, enclose C744j's i_n(t) positive series through
k=256. Its successive series factors are
t^2/[2(k+1)(2n+2k+3)]<1/294, since t<1/7. Thus the remainder
before multiplying by t^n/(2n+1)!! is at most
(1/294)^257/(1-1/294). The leading factor is obtained by its positive
recurrence. Division by the enclosed, strictly positive i_0 or i_1
then gives every r_n, n=2,...,256, using C744j's exact formula.
Clamping a lower interval endpoint to zero is used only for these
mathematically nonnegative series quantities. No small moment is
silently rounded to an exact zero; an enclosure containing zero is
retained as an interval.

All17 exact/dyadic checks pass. The upward-rounded display bounds are:

    joint action error <=7.068387972715e-33, required<1e-30;
    extra Schur error <=1.058571703339e-29, required<1e-19;
    maximum scalar interval width <=8.467677958663e-613;
    maximum of 255 moment-ratio widths <=1.822569821909e-614,
        both width requirements <1e-600.

The exact rational comparisons decide the checks, not the decimal
displays. The certificate saves all intervals, all2049 triples of
exact rational moments, every bound operand and every failure field.
Positivity of the individual two-by-two power-log moment blocks is
only a consistency check, not positivity of either Schur matrix.

At step486, unfinished work was the full finite calculation: construct all
piecewise action coefficients with certified arithmetic, evaluate
(9) and every projected moment, form the complete covariance and
certify both inequalities S_T,s>=I/25 (or obtain another strictly
positive common margin after all payments). Scalar widths alone are
not entrywise matrix error bars. No matrices are constructed by this
script. No fixed-target counterexample has been certified either.

### 6. Implementation of enclosed finite products (step487)

The bounded implementation in
`scripts/adjacent-neutral/matrix-enclosure-487.py` evaluates (1)-(3)
on the selected columns n=2,3,256. It retains all257 projection rows;
it does not replace Q_N by a smaller projection. This is a principal
block calculation, not a lower bound for the complete finite matrix.
The following explains its arithmetic independently of numerical displays.

It uses the exact integer coefficients
P_n(2v-1)=sum_k (-1)^(n+k) binom(n,k)binom(n+k,k)v^k.
The saved checks verify every coefficient of the Legendre three-term
recurrence through degree256, with initial polynomials1 and2v-1;
uniqueness of that recurrence identifies all these polynomials.
All three-piece projection polynomials are generated together by
the same recurrence after affine substitution, then multiplied by
the enclosed positive sqrt(2n+1). Moment ratios and scalar intervals
are regenerated by Section5's exact interval procedure. The neutral
columns and harmonic diagonal are precisely C744j/k's, including the
low parity correction; these checks do not assume numerical neutrality.

All coefficient intervals use the dyadic denominator S=2^2048 from
Section5. For an interval coefficient choose integer midpoint m and
integer radius r so that the coefficient lies in (m+[-r,r])/S.
For polynomial coefficient vectors m,u with radii r,v, exact integer
convolution gives the product midpoint m*u, and an enclosing radius

    |m|*v+r*|u|+r*v.

Here absolute values and inequalities are coefficientwise. Divide
by S^2 and round outward back to the denominator S. This follows
by expanding (m+delta)(u+epsilon), with |delta|<=r, |epsilon|<=v;
every product coefficient has precisely the displayed absolute bound.
No cancellation is discarded from the midpoint convolution.

The implementation accelerates signed integer convolution by packing
coefficients into nonnegative integer slots. For integer arrays a,b,
put A=max|a_i|, B=max|b_i| and encode a_i+A and b_i+B in a power-of-two
base strictly larger than 4 min(length(a),length(b))AB. Every product
slot is smaller than this base, so integer multiplication has no
inter-slot carries. From slot k subtract

    B sum_(i+j=k) a_i + A sum_(i+j=k) b_j
                         + AB #{(i,j):i+j=k}.

The result is exactly sum_(i+j=k) a_i b_j, including negative values.
A zero array is handled separately. GMP integer multiplication is an
accelerator for this exact operation, not interval floating-point
arithmetic. Saved comparison checks use direct Python integer products.

Formula (9) is applied to the midpoint integer polynomials with exact
common rational denominators. For maximum product index K, take
L=lcm(1,...,K+1)^3. Then all weights L/(k+1)^r, r=1,2,3, are integers.
Sum the signed integer products against these weights before any
rounding; division by LS^2 produces the exact midpoint integral.
The corresponding power moments for projection rows use the square
of the appropriate lcm and denominator S. Thus small interval widths
are not obtained by treating large intermediate sums as small.

For an action column P+Q log t let

    B_col=(sum|mid(P)_i|+2 sum|mid(Q)_i|)/S,
    e_col=(sum rad(P)_i+2 sum rad(Q)_i)/S.

Since ||t^k||_2<=1 and ||log t||_2=sqrt2<2 on (0,1), these bound
the midpoint L2 norm and its L2 error, respectively. Cauchy--Schwarz
therefore bounds the error in a product integral of two columns by
B_1 e_2+B_2 e_1+e_1 e_2. The same argument with t^k gives error at
most e_col for each projection power moment. Uncertain piece lengths,
affine transformations and normalized Legendre coefficients retain
their full interval bounds. Combining projection moments, forming
their products and subtracting them from the complete Gram uses
outward dyadic interval operations. Both signs and every cross term
in the selected block are retained.

The polynomial-kernel implementation uses an algebraically shorter
form of C744k(10). With mu_m=int_0^1 w^m g(w)dw, it uses

    Psi_j(v)=sum_(l=0)^j binom(j,l)v^l mu_(j-l),
    Phi_j(v)=sum_(l=0)^j (-1)^l binom(j,l)v^l mu_(j-l)
       +(1-(-1)^j)sum_k g_k [j!k!/(j+k+1)!]v^(j+k+1).

The first identity is the binomial theorem. For the second, on w>=v
expand (w-v)^j and integrate w^(j-l)g(w) from v to1. Its upper limits
give the displayed first sum. Its lower limits for the monomial w^k
are -(-1)^j int_0^v (v-w)^j w^k dw. The integral from w<=v adds one
copy of this integral; substitution w=vu evaluates it as
v^(j+k+1)j!k!/(j+k+1)! by j integrations by parts. This proves the
formula for all nonnegative j,k, including j=0 and k=0. The code
generates the beta factors by their positive k recurrence. No kernel
term or degree is omitted by this optimization. The rational identity
checks compare endpoints and an interior point, both kernel parities,
and the maximal monomial degree against C744k's unsimplified formula.

Finite head entries are symmetrized as in (2). The code's dyadic
Gershgorin lower bound, when positive, applies only to the selected
principal block: diagonal lower endpoint minus the sum of maximum
absolute off-diagonal endpoints in its row. The elementary proof is
2|c_i c_j|<=|c_i|^2+|c_j|^2 in the Hermitian quadratic form. It gives
no lower bound for the omitted rows or their interactions. Selected
polynomial columns need not be compactly supported; they are the
admissible finite form-domain columns already used in C744j/k.

Run `python3 scripts/adjacent-neutral/matrix-enclosure-487.py`, then
`python3 scripts/adjacent-neutral/matrix-replay-487.py`. The first
requires the already installed GMP library at
`/opt/homebrew/lib/libgmp.dylib`; no package or environment was modified.
It saves all selected coefficient endpoints in
`scripts/adjacent-neutral/matrix-coefficients-487.json.gz`, and all
projected moments, head/Gram/covariance/Schur intervals, exact lower
endpoints, widths and failures in
`scripts/adjacent-neutral/matrix-enclosure-487.json`. No coefficient
array or projection row used in the calculation is replaced by a
sampled action or a floating-point moment projection.

All7 computation checks pass. For the principal submatrices of S_T,s
with coordinate indices2,3,256, the exact dyadic Gershgorin endpoints
give the conservative bounds

    S_T,-1|_(2,3,256) > (5879/10000) I,
    S_T,+1|_(2,3,256) > (2331/2000) I.

Every saved head/Gram/covariance/Schur entry has interval width
<1.046*10^(-236), compared with the requested arithmetic budget
10^(-30). The rational comparisons, not the decimal displays, decide
these statements. The second command replays all matrix entries from
the saved head, complete Gram and all257 projection rows, verifies
every covariance/Schur endpoint, the Gershgorin bounds, conservative
reported thresholds and coefficient-artifact hash. All13 checks pass;
its full exact evidence is `scripts/adjacent-neutral/matrix-replay-487.json`.
This replay does not independently audit the analytic input lemmas
or reconstruct the coefficient arrays from scratch.

The new result is a finite arithmetic specialization of the existing
scheme, not a source-independent general theorem. No full finite
spectral bound follows from positive principal submatrices. At step487,
columns4,...,255 and their entire mutual and selected-column interactions
remained unenclosed; Section7 records the subsequent expanded section.
At step487 both full inequalities (2)>=I/25, hence the full
mu>1/30 and beta_1<1/2 conclusions, remained unproved. The degree128
failure, unaudited analytic inputs and independent global gaps are
unchanged. This calculation pays a concrete implementation test at
the maximal degree, rather than replacing the target by a finite one.

### 7. Expanded principal section and shifted interval LDL (step488)

Let I={2,...,17,256}, in this order. The same exact finite matrices
in (2), restricted to these17 coordinate indices, satisfy

    S_T,-1|_I >= (1/25)I_17,  S_T,+1|_I >= (1/25)I_17.   (10)

These are principal-matrix inequalities only. In particular (10)
does not supply the full-matrix lower bounds required after (4).
Every coupling within I is retained, together with all257 projection
rows in the covariance. This finite result uses the previously assessed
arithmetic and square-completion tools, not a new general theorem.

The implementation is `scripts/adjacent-neutral/matrix-enclosure-488.py`.
It imports Section6's unchanged coefficient and integration procedures,
reuses the saved enclosed columns2,3,256, and generates columns4,...,17.
It saves every three-piece P/Q coefficient endpoint in
`scripts/adjacent-neutral/matrix-coefficients-488.json.gz`. Projection
moments for each column retain rows0,...,256. If t_(s,j) is the j-th
action column and U_(k,j)=<p_k,t_(s,j)> in the real unitary-coordinate
basis, the unsymmetrized head entries are

    <z_i,t_(s,j)>=U_(i,j)-r_i U_(i mod2,j).

This is exactly C744j's definition of z_i and is used in place of a
second evaluation of the head integral. Complete Gram products use
(9), with outward coefficient-error payments as in Section6. Their
upper triangle is reflected by exact real symmetry. The code subtracts
the complete257-row projection Gram, symmetrizes the head as in (2),
and forms both Schur matrices with the exact multiplier250/171.

For completeness the finite sign algorithm is justified here because
it replaces diagonal dominance in Section6. Put A=S_T,s|_I-(1/25)I_17.
The ordinary LDL recurrences, with L unit lower triangular, are

    D_j=A_jj-sum_(k<j)L_jk^2 D_k,
    L_ij=[A_ij-sum_(k<j)L_ik L_jk D_k]/D_j, i>j.

Whenever earlier pivots are positive, elimination of their rank-one
terms gives these identities and, by induction, A=L diag(D_j)L^T.
Every recurrence is evaluated in outward dyadic intervals. Division
is performed only when the entire pivot interval is strictly positive.
Inductively the intervals enclose the exact factors of this exact
symmetric A, despite dependencies between their operands. All17
positive pivot intervals therefore imply, for every nonzero complex c,
c^*Ac=sum_j D_j |(L^T c)_j|^2>0, since L is invertible. This proves
(10). A pivot is not itself an eigenvalue lower bound. The elementary
elimination proof explains the assessed finite square-completion
implementation; no additional spectral theorem is asserted or imported.

All10 computation checks pass. Both shifted factorizations have all17
strictly positive pivots. The exact smallest pivot lower endpoints
are >2947/10000 and >6492/10000, respectively; these numbers describe
the factorization, while the certified matrix lower bound is1/25.
All head/Gram/covariance/Schur interval widths are <1.046*10^(-236),
compared with the required arithmetic budget10^(-30). Full interval
operands, factors, exact bounds, artifact hashes and failure fields are
in `scripts/adjacent-neutral/matrix-enclosure-488.json`.

Run `python3 scripts/adjacent-neutral/matrix-enclosure-488.py`, then run
`python3 scripts/adjacent-neutral/matrix-replay-488.py`. The latter
checks every saved head/covariance/Schur endpoint, every LDL operand,
positive pivot, exact width, all257 projection rows, all matrix
dimensions and coefficient-artifact hashes. It also checks exact
agreement of the old projection endpoints and overlap of every old
selected matrix entry, including the independently integrated old
head. All35 replay checks pass; complete evidence is saved in
`scripts/adjacent-neutral/matrix-replay-488.json`. The replay uses the
same interval algorithms; it is not an independent analytic audit or
a reconstruction of every coefficient from its defining formula.

At step488 columns18,...,255 and all interactions involving them remained
unenclosed. Neither a bound for either full255-dimensional matrix,
a full common neutral margin, beta_1<1/2, nor RH follows. C744i/j/k/l
remain independently unaudited. No smooth counterexample or global
sign claim is made. The prior degree128 and fixed-response stops keep
their original scopes; this computation does not reopen those routes.

### 8. Complete finite evaluation by batched exact moments (step489)

The implementation `scripts/adjacent-neutral/full-matrix-enclosure-489.py`
constructs columns2,...,256. It reuses the17 enclosed coefficient columns
from Section7 and constructs every other column by the unchanged Section6
procedure. Every projection retains degrees0,...,256. The exact input
form, neutral graph, polynomial degrees, three intervals and both signs
are unchanged. This is the quantitative implementation of the already
assessed finite-integration and square-completion tools; no source theorem
provides these particular matrices and no new general theorem is claimed.

Here is the batched integration identity. Put S=2^2048 and
D=lcm(1,...,2049)^3. On one piece let p_(j,l),q_(j,l) be the integer
midpoints of column j's coefficient intervals, so its midpoint function
is S^(-1)sum_l[p_(j,l)+q_(j,l)log t]t^l. Define the integers

    U_(j,k)=sum_l [p_(j,l)D/(k+l+1)-q_(j,l)D/(k+l+1)^2],
                         0<=k<=1024,
    V_(j,k)=sum_l [-p_(j,l)D/(k+l+1)^2
                              +2q_(j,l)D/(k+l+1)^3],
                         0<=k<=256.                    (11)

All displayed quotients are integers: k+l<=2048 and every denominator
divides D. Formula(3), applied to the finite sums, identifies U_(j,k)/(DS)
as the integral of t^k times the midpoint function, and V_(j,k)/(DS)
as the integral with the additional factor log t. Thus the midpoint
product integral is exactly

    sum_k [p_(i,k)U_(j,k)+q_(i,k)V_(j,k)]/(D S^2).

This is (9), including both mixed-log products and the log-squared
product. Arrays are padded only by exact zero coefficients. The
unweighted product is symmetric by this integral identity; only its
upper triangle needs evaluation. No interval or sign is inferred from
symmetry of a sampled approximation.

For an integer coefficient array a of length L and weights w_r=D/(r+1)^j,
coefficient L-1+k of reversed(a)*w is sum_l a_l D/(k+l+1)^j.
This follows directly from the finite convolution indices. Section6's
exact signed integer convolution therefore evaluates all moments in(11)
at once, without rounding these midpoint sums. The small native program
`scripts/adjacent-neutral/exact-gram-489.c` stores the resulting integers
and evaluates the displayed dot products by GMP integer multiplication
and addition. Its loop computes each summand once for each selected
pair. It uses no floating arithmetic. Signed tests, including integers
longer than a machine word, compare its outputs with direct Python
integer dot products; the moment tests compare every tested sequence
coefficient with the defining rational-weight sums.

The native midpoint products are not themselves enclosures for the
actual action. Each piece retains the entire coefficient-error payment
B_i e_j+B_j e_i+e_i e_j from Section6. Multiply each resulting interval
by its enclosed positive piece length, and sum all three pieces.
Projection power moments use U_(j,k)/(DS), k<=256, with their full L2
coefficient-error payment before multiplication by the enclosed affine
Legendre coefficients. These are the same257 projection rows as in
Sections6-7; there is no covariance truncation or negative-eigenvalue
repair. The head uses the same exact neutral-row identity as Section7.

The cancellation-sensitive coefficients and power-moment integration
retain2048-bit dyadic intervals. Only after these operations are complete
are finite projection/matrix intervals rounded outward to a512-bit
dyadic grid, by floor of the lower endpoint and ceiling of the upper
endpoint. This deliberate coarsening preserves containment. Every head,
Gram, complete covariance and Schur entry retains its entire resulting
error interval. The shifted LDL recurrence from Section7 is evaluated
with outward intervals, including outward rounding of each pivot and
lower-triangular factor to the512-bit grid. The same induction encloses
the exact point factors; divisions require strictly positive lower
pivot endpoints. Positivity of all255 pivots for a sign would therefore
certify its entire matrix above I/25. A pivot value is not an eigenvalue
bound, and a failed sufficient shifted test alone would not refute the
original neutral target.

Per-column coefficient intervals, exact midpoint operands, all native
inputs and product outputs, coefficient-error operands and completed
matrix/factorization intervals are saved under
`scripts/adjacent-neutral/full-matrix-489/`. Native inputs are retained
in gzip files for the midpoint-Gram calculation, with hashes of their
complete uncompressed contents; the projection replay also retains its inputs.
No selected coefficient or mixed term is replaced by a floating value.
The replay program `scripts/adjacent-neutral/full-matrix-replay-489.py`
reconstructs every saved Gram, head, complete covariance, Schur and LDL
interval from these saved operands. Its complete projection Gram uses
the separate `scripts/adjacent-neutral/interval-projection-489.c`:
input endpoints have denominator2^512, so each endpoint product has
denominator2^1024 and is exactly representable on the2048-bit grid.
Taking the minimum and maximum of all four integer corner products,
then adding them, is therefore exactly the Python interval dot product,
with no extra approximation. The replay checks every resulting
covariance endpoint; its signed tests include intervals crossing zero
and products longer than a machine word. The LDL replay still uses
the same interval routine. This is a complete saved-operation replay,
not an independent reconstruction of all action coefficients or the
midpoint Gram kernel, and not an independent analytic audit.

The completed calculation gives the entire finite inequalities

    S_T,-1 >= (1/25)I_255,   S_T,+1 >= (1/25)I_255.      (12)

For each sign all255 shifted interval LDL pivots have strictly positive
lower endpoints. The induction in Section7, applied to all255 rows,
therefore proves(12), for every complex coordinate vector. There are
no omitted finite columns or unpaid mutual finite interactions in(12).
The exact dyadic signs decide this conclusion; no numerical eigenvalue
or positive principal submatrix is substituted for the full test.

All12 computation checks pass, including overlap of every Section7
projection interval and every old head/Gram/covariance/Schur entry.
The upward-rounded maximum matrix-width displays are
4.325837624097e-153 and4.400421031409e-153 for s=-1,+1 respectively;
the exact comparisons to the required10^(-30) decide the width checks.
The complete summary, exact rational bounds and failure fields are in
`scripts/adjacent-neutral/full-matrix-enclosure-489.json`. All complete
matrix and factorization operands, including every positive pivot,
are in the two `full-sign-*.json.gz` files in the saved-data directory.

Run `python3 scripts/adjacent-neutral/full-matrix-enclosure-489.py`,
then `python3 scripts/adjacent-neutral/full-matrix-replay-489.py`.
All54 complete saved-operation replay checks pass, including every
Gram/head/covariance/Schur endpoint, all257 projection rows for all255
columns, all native-input and coefficient hashes, every shifted LDL
operand, all255 positive pivots per sign, dimensions and exact reported
bounds. The complete evidence and failure fields are in
`scripts/adjacent-neutral/full-matrix-replay-489.json`. This completes
the finite arithmetic ledger; it does not supply the independent
coefficient/kernel reconstruction or analytic audit excluded above.

Conditional on the analytic reductions in C744j/k and Sections1-4,
(4) and(12) give the common original-form margin mu>9/260>1/30
by the calculation following(8). That implication, including the
identification of the original energy, the exact neutral form domain,
the whole-complement payment and the whole-map error estimates,
was still unaudited at step489. Section9 now audits that analytic
implication; the independent finite reconstruction described above
remains open. No smooth counterexample, remote interaction bound,
non-neutral or odd sign, all-window propagation, or RH conclusion is
claimed. The older degree128 and pure-L2 response-tail stops retain
their original scopes.

### 9. Separate conceptual audit of the analytic implication (step490)

This audit uses exactly the complex smooth class N_neut, ell=log(3)/2,
the original unshifted E and X=K_1+aJ_d. It accepts C744i(4), (6),
(11), the analytic statements of C744j Sections1-3 and C744k Sections1-4,
and Sections1-5 above. It does not audit the separate sharp response-tail
claim in C744i(5), the floating-point locators, or independently reconstruct
the Section8 finite certificate. In particular the following is the
audited conditional statement, not a replacement for that reconstruction:

    If the exact S_T,-1 and S_T,+1 in (2) both satisfy S_T,s>=I/25,
    then there exists one mu>9/260 such that
    E(h)+s 2<Xh,h> >= mu||h||_2^2
    for every h in N_neut and s=-1,+1.                    (13)

The common mu is independent of h. This is a verification of the existing
quantitative specialization, not a new general spectral theorem. The
regional spectral import remains Gerontogiannis--Mesland v2, Proposition5.8,
printed p19 and Section2; its affine interval change multiplies both the
L2 norm and regional double integral by the same length factor. Its
operator eigenvalues 2H_n therefore give the form entries H_n used here.
The Carleman upper bound remains Perfekt--Pushnitski, Lemma2.1, p166,
with domination constant1/2 for K_1. The standard form square completion
compared with Li paper45 v2 (4.1)-(5.5) is justified explicitly below;
no positivity or coefficient certificate from that paper is imported.
The saved step483 assessment supplies the reused primary-source coverage.

**Original energy and regional normalization.** L741(9), (14)-(18),
or equivalently L744(5)-(6) on smooth tests, give the causal distribution
gamma delta_0+(1_(u>0)log u)' together with log(2pi)I and the bounded
regular kernel q_0-4cosh(u/2). Its negative Hermitian part supplies
-gamma-log(2pi); no second gamma is added. To check the endpoint term
without assuming a generator trace, put

    I_epsilon(x)=int_(0<y<ell, |x-y|>epsilon) dy/|x-y|
       =log(x/epsilon)_+ + log((ell-x)/epsilon)_+.

Symmetrizing the truncated causal integral gives its negative real part
as one quarter of the truncated double-difference integral minus
(1/2)int I_epsilon(x)|h(x)|^2dx. The distributional compensation adds
-log(epsilon)||h||^2. Thus the limiting multiplier is
-1/2 log(x(ell-x)). For a smooth interior h, its difference is Lipschitz,
so the double-difference integrand is bounded by a constant times |x-y|;
dominated convergence applies. The cutoff compensation using h(x-epsilon)
instead of h(x) differs by O(epsilon|log epsilon|). For a polynomial on
the closed interval, the same difference estimate holds inside, while
the endpoint layers contribute O(epsilon(1+|log epsilon|)); log and
log-squared are integrable. These facts also justify the polynomial
form evaluations and their L2 action columns.

The bounded cosh term factors into the two exponential moments, hence
vanishes on the exact neutral class. The delay d=log2 exceeds ell,
so there is no single-cell arithmetic term. This proves that D+V-Q/2
in C744j is the original E on that class, with V exactly as stated.
The regional form is one quarter of the double integral, hence one half
of the regional operator quadratic value: its entries are H_n, not2H_n.
In the adjacent cross term L741(21)-(24) gives -1/2 of the continuous
kernel and -a of the delay. After reflection, the cosh moments and the
rate1/2 response vanish; the remaining kernel is exactly K_1 and the
delay is exactly J_d. Compact interior supports justify the geometric
series integration absolutely. Reflection interchanges the two moment
conditions and preserves E because its Fourier symbol is even. This
checks C744i(4), including its factors and the complete n=2 contribution.

**Neutral graph and form domain.** The two moment rows of p_n are exactly
C744j(5): after removing e^(sigma ell/4) their even rows agree and their
odd rows differ in sign. The positive i_0,i_1 permit solving for p_0,p_1.
The resulting r_n are real, and their square summability makes both
correction functionals continuous on L2. Thus C744j(6) is an equality
for every neutral L2 function, including complex ones. Orthogonality
gives the norm bounds using eta and epsilon_N without identifying a
neutral compression with a raw Legendre truncation.

The form domain is the intersection of the domains of the nonnegative
closed forms D and V-v_min. With the sum of their form norms this
intersection is complete; B_s and v_min are bounded form perturbations.
The cited regional spectral theorem puts smooth interior functions in
the D-form domain. Every polynomial belongs to the intersection, and its
product with V is in L2. For neutral h in this domain, q=Q_N h differs
from h by a polynomial, and T_N q differs from q by two polynomials.
Both remain in the form domain. The head p=h-T_N q is exactly the
finite sum of z_2,...,z_N. No density claim about raw neutral truncations,
new boundary trace, or unproved equality of operator domains is needed.

**Complete complement and mixed terms.** C744j's power-series comparison
gives 0<=q_0(u)<=1/2 for 0<u<=ell<1, so ||Q||<=ell/2. Carleman
domination gives ||K_1||<=pi/2 and reflection gives ||J_d||=1. Together
with V>=-gamma-log(pi ell), these imply the entire-complement floor
H_(N+1)-c(1+epsilon_N^2). The c used here is positive. The nonnegative
p_1 regional contribution can be omitted in this lower bound.
The potential is replaced by its minimum only on the complement;
its mixed terms have not been removed.

In fact b_i=(D+V+B_s)z_i belongs to L2. With the inner product linear
in its first argument, direct expansion yields

    F_s(z_i,T_N q)
      =<Q_N b_i-sum_e <b_i,p_e>v_(e,N),q>.

This verifies the conjugations and the exact low-moment correction in
C744j(8). The Gram of these complete vectors is R_s. All endpoint-log,
Hankel, reflection and covariance cross terms are included. For p=Zt,
Young's inequality with gamma_0=18/25 and rho=19/20 gives

    F_s(p+T_N q)
      >= t^*[M_s-(250/171)R_s]t + (9/250)||q||^2,

because the actual complementary floor is strictly larger than gamma_0.
This is a form argument on the stated domain, not an assertion that an
unbounded operator has a bounded inverse.

**Whole-map approximations and scalar comparison.** In C744k the disk
bound |sinh(z)/z-1|<5/6 on |z|<=2 makes the two removable regular
kernels analytic there. The stated Cauchy bounds and geometric tails
therefore control the kernels uniformly on their respective full real
intervals. A uniform kernel error delta on (0,ell)^2 has L2 operator
norm at most ell delta. Multiplication by ||Z||<51/50 gives the joint
255-column error epsilon, with no missing dimension factor.
The endpoint potential is never approximated at this stage. Its
finite-head bound follows from ||g||_infinity<=257||g||_2 and the
L2 norms sqrt2 of both endpoint logarithms. This yields ||A_s||<500.

The exact coupling is Q_N A_s-WP_(0,1)A_s with ||W||<10^(-100).
Thus its distance from Q_N A_hat_s is at most epsilon+500*10^(-100).
The Gram perturbation estimate uses the full operator norm, giving
C744k(11)-(12). It pays the moment correction even when small high
moments cannot be represented as positive floating-point numbers.

Next c_0>c_*=-183/100 is a one-sided lower comparison. Although it
changes the head by -(c_0-c_*)Z^*Z, it leaves Q_N A_hat_s unchanged
because Q_N Z=0. The actual graph-corrected coupling was already paid
before this comparison. Therefore S_hat_s>=S_tilde_s is valid; this
does not shift the target energy. Each logarithm substitution in
Section2 has argument in [0,1/2]. The singular log t factors remain
exact, the reflection jump is exactly at b, and negative orientations
are absorbed by positive piece lengths. The coefficient g(-v) is
bounded on the entire interval using 257*6^256||g||_2. Consequently
Section3's error is a whole-map L2 error, not a sampled or per-column
error. Symmetrizing the approximated head and applying the full Gram
perturbation proves (4) for both signs.

**Constants, scope and conditional assembly.** The three small existing
certificates were inspected and rerun in this audit:

- `python3 scripts/adjacent-neutral/complement-rational-check-484.py`:
  all11 exact comparisons pass; floor>36223/50000=0.72446>0.72.
- `python3 scripts/adjacent-neutral/action-enclosure-485.py`: all19
  comparisons pass; joint kernel-action error<=5.21328181664e-24
  and Schur error<=7.65504887662e-21<1e-19.
- `python3 scripts/adjacent-neutral/power-log-enclosure-486.py`: all17
  comparisons pass; joint log-action error<=7.068387972715e-33 and
  additional Schur error<=1.058571703339e-29<1e-19.

Their exact rational/dyadic operands and empty failure fields remain
in the same-named JSON files. Their old printed finite-sign limitations
describe those scripts' scopes; none evaluates the full matrices.
The scalar interval rules, positive-series remainders, and finite
power-log moment functional were also checked against Sections4-5.
This audit did not rerun or independently reconstruct Section8's large
coefficient and native Gram calculations. Reading a summary or a check
flag is not independent verification of those operands.

Under the explicit finite hypothesis of (13), (4) gives head margin
delta=1/25-2*10^(-19)>9/250. The preceding square completion therefore
gives F_s(h)>=(9/250)(|t|^2+||q||^2). Since
||h||^2<=(1+eta^2)(|t|^2+||q||^2) and eta^2<1/25, one can take
mu=(9/250)/(1+eta^2)>9/260, uniformly in h and s. This proves (13).
No limit from a positive finite section to an unpaid infinite space
has been used.

Finally (13) implies E(h)>=mu||h||^2 by averaging its two signs, so
the positive energy needed in C744i(6)'s polarization follows from
this certificate itself. Its implication beta_1<=C/(2C+mu)<1/2,
C=pi/2+a, therefore needs no additional use of Zhu's unreplayed sign
computation. Boundedness of X and Hermitian polarization apply on the
complex linear neutral class; balancing the two positive energies
gives the cross bound. At step490 this remained conditional on the exact
finite matrix inequalities. Sections10-11 subsequently audit their
coefficient/moment construction, native midpoint products and complete
finite signs. Remote, non-neutral, odd and all-window signs remain gaps.

### 10. Source and coefficient/moment reconstruction audit (step491)

This audit uses the same hypotheses and exact maps as Sections1-9.
It checks the finite action construction against C744k(10), and freshly
reconstructs its saved coefficient and projection operands. It does not
yet check the native midpoint Gram outputs. The proposed implication
to a uniform neutral margin therefore retains that explicit premise.
These are arithmetic/provenance checks of the existing specialization,
not new mathematics beyond the sources assessed in step483.

The high-level interval evaluator in `matrix-enclosure-487.py` is
reused after the following source audit; this is not a wholly separate
implementation of the action formulas. Every coefficient of the
unnormalized shifted Legendre polynomials is identified by the verified
three-term recurrence through degree256. Their positive normalizations
and all exact moment ratios use Section5's enclosing scalar arithmetic.
For the parity correction e=0,1, H_e=e. Thus `dg` in `build_column`
is exactly the enclosed harmonic diagonal applied to z_n, including
the low-degree correction, rather than H_n times the whole z_n.

The regular-kernel sums start their power at ell and multiply it by
ell at each j. Consequently their powers are ell^(j+1), including
the coordinate Jacobian. The source's `qa` and `ha` use respectively
Phi_j and Psi_j of Section6, with every j=0,...,96 retained. The
coefficient of v^r in the Carleman quotient polynomial is precisely
(-1)^r sum_(k>r)g_k/(k-r), including empty sums. Its remaining term
is g(-v)[log(1+v)-log v], giving the three log coefficients stated
in C744k(10). The scalar part is c_*=-183/100. Before multiplication
by the sign, the regular Hankel action has coefficient2 and the
reflection has coefficient2a. The reflection is omitted only on
piece0, and on both other pieces is g(1+b-v), since 1+b=d/ell.
Thus every term and sign agrees with the retained formula.

For v=u+wt the evaluator's Horner recurrence is affine substitution
in a finite polynomial. The three u,w pairs and their logarithm
constant/series/log(t) parts coincide with Section2. Negative affine
orientation is accounted for by the positive length, not a signed
integral. Interval addition, multiplication, division by positive
integers and positive square roots enclose their exact operations by
integer floor and ceiling. All divisors in the scalar ratios have
strictly positive lower endpoints. `trim` removes only coefficients
whose two endpoints are both zero. The polynomial product's midpoint
and radius are the enclosing convolution expression in Section6.
Induction over these finite operations therefore proves containment
of every coefficient in the original exact T_s; dependency between
interval inputs only widens this enclosure. Matching two interval
computations alone would not prove containment.

The independent arithmetic component in
`scripts/adjacent-neutral/finite-reconstruction-491.py` replaces signed
convolution's offset encoding. For nonzero integer arrays a,b, let

    C=min(length(a),length(b)) max|a_i| max|b_i|.

Every true convolution coefficient has absolute value<=C. Choose a
byte-power base B>2C. Encode each polynomial as the difference of
the encodings of its positive and negative coefficient parts, then
multiply the resulting signed integers. The same installed GMP is
used solely for exact nonnegative integer multiplication; it is not
an independent multiplication library. Decode the product using
centered digits: a raw base-B digit plus its incoming carry is left
unchanged if <=B/2, and otherwise B is subtracted with carry1 to
the next digit. Treat the overall product sign separately. Since
each true coefficient is strictly between -B/2 and B/2, congruence
modulo B uniquely determines it; induction after division by B
recovers every coefficient. The final carry must vanish and is
checked. Zero arrays are handled directly. All original coefficients
fit in one input digit, since C dominates their maximum absolute
values. The product magnitude is <B^(length(a)+length(b)-1), so its
fixed-length byte representation cannot truncate it. This proves
the new convolution is exact without using the old offset formula.

The additional full-degree check evaluates, for all24929 pairs
0<=j<=96 and0<=k<=256,

    sum_(r=0)^j (-1)^r binom(j,r)/(k+r+1)
                = j! k!/(j+k+1)!.

This is the beta integral already used in Section6, obtained by
expanding (1-t)^j in integral_0^1 t^k(1-t)^j dt. Its right side
follows by j integrations by parts, with the j=0 case1/(k+1).
It checks every kernel degree and monomial in the action, rather
than only selected point evaluations; no new kernel theorem is claimed.

The fresh reconstruction never loads saved action coefficients as
construction inputs. It starts from the scalars, ratios and rational
Taylor coefficients, invokes the reviewed source evaluator with the
new convolution, and compares every regenerated coefficient endpoint
to the saved three-piece g,P,Q arrays. It then rebuilds both full
1282-integer midpoint/moment arrays per sign and piece using(11),
checks the complete saved size/error operands, and reconstructs all257
projection rows using the normalized affine Legendre recurrence.
The moment-error payment and positive piece lengths are those already
proved in Sections6 and8. Exact endpoint equality ties the reviewed
construction to the saved data; it is not an interval-overlap argument.

The two-column pilot, n=2,256, passed37/37 checks per column and
matched all12600 compared coefficient intervals. Its log is
`scripts/adjacent-neutral/finite-reconstruction-491-pilot.log`.
The completed full run, with no saved coefficient cache used as a
construction input, passes all9435 column checks (37 per column) and
all three grouped primitive checks. It compares all1606500 coefficient
intervals, all3922920 integers in the1530 left/right dot-array pairs,
all3060 size/error integers and all131070 projected-moment intervals.
Every regenerated endpoint and integer agrees exactly; the complete
failure list is empty. All255 columns2,...,256, both signs, three
pieces and257 projection rows per sign/column are retained.

Run `python3 scripts/adjacent-neutral/finite-reconstruction-491.py`.
The complete summary is
`scripts/adjacent-neutral/finite-reconstruction-491.json`; full
per-column comparisons and source-data hashes are under
`scripts/adjacent-neutral/finite-reconstruction-491/`, with the complete
execution log at `scripts/adjacent-neutral/finite-reconstruction-491.log`.
The source review and fresh exact reproduction accept the stated
coefficient/moment construction and its provenance. The high-level
evaluator and scalar arithmetic are reused as explicitly disclosed;
only signed convolution encoding has a separate implementation, and
GMP remains the shared exact multiplication primitive.

Step491 did not recompute any native midpoint Gram output, full
Schur entry or shifted LDL factorization. The unchanged sufficient
finite threshold is I/25; at step491 Section9's mu>9/260 remained conditional
on the full finite inequalities. A fresh audit had to tie all six archived
native inputs to the now-reconstructed dot arrays and check all195840
upper-triangular Gram outputs, then the resulting full finite signs.
Any discrepancy would block acceptance until resolved. Section11 supplies
this remaining audit. A failed sufficient finite budget alone does not
refute the original target; a certified
exactly neutral smooth ratio>=1/2 would stop that target. No independent
end-to-end all-space certificate or RH conclusion was asserted at step491.

### 11. Exhaustive native products and separate finite-sign audit (step492)

The target, exact maps, degrees, neutral constraints and hypotheses are
unchanged. This completes the outstanding arithmetic/provenance audit;
it does not propose a new spectral theorem or a new source-covered target.
Run `python3 scripts/adjacent-neutral/native-audit-492.py`. Original
step489 and step491 artifacts are read-only; fresh full products, matrix
intervals, factors, provenance and hashes are retained under
`scripts/adjacent-neutral/native-audit-492/`. The complete summary is
`scripts/adjacent-neutral/native-audit-492.json`, and the execution log is
`scripts/adjacent-neutral/native-audit-492.log`.

**Input binding and exact products.** All255 coefficient and column
artifact hashes equal the corresponding complete step491 reports, whose
37 checks per column have no failures. Each of the six decompressed
native inputs has header255 by1282 and exactly the255 left/right operand
rows in the audited dot artifacts. Every integer is compared, in order,
including all zero padding; no extra input is permitted. The complete
uncompressed hashes match those attached to the archived product tables.
The audit compares all3922920 input integers and records each current
dot-artifact hash. The prior reviewed coefficient/moment reconstruction
is reused, not invoked again or replaced by a preview of its summary.

`scripts/adjacent-neutral/reverse-gram-492.c` uses separate GMP integer
multiplication and addition and sums coordinates in descending order,
where the original kernel used ascending add-multiply. For each i<=j
it computes exactly sum_(r=0)^1281 left_(i,r) right_(j,r). This follows
by induction on its descending coordinate loop: the accumulator is
the sum of the already visited products, with initial value zero.
There is no rounding, modular reduction or fixed integer word bound.
The header, end-of-input, output dimensions and zero process exit are
checked. Its full195840 outputs agree exactly with the archived six
upper triangles. The fresh products are saved in six gzip files, not
sampled, and the signed long-integer regression agrees with direct
Python products. This changes summation and accumulation code, but
retains GMP as the shared multiplication library.

The denominator is exactly D S^2 from(11) for all six tables. Its
symmetry is justified by the full power-log product integral in Section8,
not by matching sampled data. The existing coefficient-error payment,
positive interval lengths and all three pieces are retained when the
freshly checked products are used to reconstruct the complete Gram.

**Complete matrix reconstruction.** The audit reconstructs all257
projection rows for every one of the255 columns from their step491-bound
column operands. It freshly evaluates their complete interval projection
Gram with the source-reviewed `interval-projection-489.c`, compiled into
the new audit directory. As in Section8, all four integer endpoint
products are evaluated before their minimum and maximum are added;
denominator2^1024 is exactly representable on the2048-bit grid. The
whole Gram, unsymmetrized head, covariance and Schur intervals match
every archived endpoint for both signs. All matrix dimensions and
exact symmetric entries are retained. No off-diagonal term or column
is omitted. The maximum widths remain below4.325837624097e-153 and
4.400421031409e-153, respectively, versus10^(-30) required. Exact
rational widths, rather than these decimal displays, decide the checks.

**Separate row-wise interval elimination.** A new implementation uses
integer endpoint pairs on the512-bit grid, rather than the reused Ball
class or its LDL routine. Addition and subtraction use the endpoint
identities. For multiplication take the minimum and maximum of all
four integer products, then divide by2^512 with outward floor/ceiling.
For division, require a strictly positive denominator interval and
take floor/ceiling of all four endpoint quotients, with numerator
multiplied by2^512. Each operation therefore encloses its exact real
operation. The shift1/25 is likewise enclosed by floor/ceiling, so it
need not be a dyadic. Every primitive, not merely each finished factor,
is rounded outward on this coarser grid.

The new routine computes lower-triangular rows in order. In row i it
first computes L_ij for all j<i using the already positive D_j, then
computes D_i from that row. These are precisely the finite LDL identities
in Section7 for S_T,s-(1/25)I. Their induction encloses the exact factors
of every symmetric matrix inside the entry intervals; repeated operands
may widen intervals without invalidating containment. All255 pivot
lower endpoints are strictly positive for each sign. Consequently,
for every nonzero complex c,

    c^*[S_T,s-(1/25)I]c=sum_i D_i |(L^T c)_i|^2>0,

since L is invertible. This certifies(12); the pivot values themselves
are not eigenvalue bounds. The new smallest pivot lower endpoints are
>2947/10000 and >6492/10000, respectively; exact endpoints and every
factor are saved in the two `finite-sign-*.json.gz` certificates. The
new endpoint factors need not equal the old ones, since the new routine
rounds every intermediate operation to512 bits. Signed interval-product,
positive-matrix and indefinite-matrix rejection regressions also pass.
All six native-piece checks and both complete finite-sign check sets
have empty failure lists.
The exact two rational pivot comparisons and all complete native/sign
check sets also pass the10 comparisons saved in
`scripts/adjacent-neutral/native-audit-492/completion-checks.json`.

**Assembly and limits.** Section10's audited action/moment construction,
the complete native input/product checks above and the independent finite
elimination establish the exact finite hypotheses of Section9. That
already audited argument now gives(13) with a single mu>9/260 on the
entire stated complex neutral class. Its polarization argument then gives
beta_1<=C/(2C+mu)<1/2, C=pi/2+a. This is local verification of the
quantitative specialization, not a claim of novelty beyond the assessed
sources. The scalar/high-level action formulas, GMP and ordinary compiler/
runtime correctness remain explicit trusted implementation inputs; a
fully separate action evaluator or integer library was not built.
C744i's separate sharp-response-tail theorem is outside these audits.
The older fixed five-cell and pure-L2-tail stops retain their scopes.
Remote, non-neutral, odd and all-window signs remain unresolved, and
no proof of RH follows.

## Mathlib

Full matching coverage of this particular exact-neutral matrix
reduction has not been checked; availability is unknown. Taylor
series, integer interval arithmetic, power-log integrals and Gram
perturbations are supporting standard mathematics. Neither these
tools nor the scalar certificate alone formally proves the complete
finite Schur signs. Section8 supplies an informal exact-arithmetic
certificate, not a Mathlib formalization. No novelty or absence claim is made.
Full matching coverage of the expanded exact-neutral principal section
and this particular interval LDL certificate has not been checked.
Full matching coverage of the batched exact-moment implementation has
not been checked; availability remains unknown.
Section9 is an informal conceptual audit of the stated conditional
analytic implication. Full matching Mathlib coverage remains unchecked.
Section10's source/provenance audit and centered-digit implementation
are informal exact-arithmetic checks; full matching Mathlib coverage
has not been checked.
Section11's native-input/product audit and separate row-wise interval
elimination are also informal certificates; full matching Mathlib coverage
is unchecked. No availability or absence claim is inferred.
