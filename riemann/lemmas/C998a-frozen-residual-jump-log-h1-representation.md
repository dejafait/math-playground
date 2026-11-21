# C998a: Exact jump/log subtraction for the three frozen residuals

## Hypotheses

Use C744v's full complex operators T,T* on L2(0,ell), ell=log(3)/2,
a=ell/2, and its normalized cosine basis e_n=nu_n cos(k_n x),
k_n=n*pi/ell, nu_0=ell^(-1/2), nu_n=sqrt(2/ell) for n>0.
Inner products are linear in the first slot. Use C999's unchanged
delta=1/100, m=286, J=14, B_trial=D+S_app-delta I and
B0q=P0 B_trial q on Dom(D) intersect H0. Here P0 projects onto the
kernel of the two moments against w_+(x)=exp(x/2), w_-(x)=exp(-x/2).
Use C999z's exact half-interval Carleman operator, h_m and all four
products in each E_epsilon,j. No singular response is truncated.

For columns j=0,1,2, define f_j,h_j by applying C999q's EXACT neutral
completion Z to the two endpoint components of C999y's frozen X.
The free coordinates occupy n=2,...,17; all other free coordinates
are zero. The entire96-integer witness, denominator2^24 and its
support in C^2044 are the witness640 upheld by audit642. Define q_j
by applying the SAME exact completion to the254 free coefficients
n=2,...,255 in `free_middle_dyadics`, read as exact binary rationals
from `scripts/separation-seven/frozen-reference-proposal-652.npz`,
SHA256 `2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
Neither saved rounded raw vectors nor saved sampled jumps define these
functions. Put

    g_j=Tf_j+T*h_j-B_trial q_j,   r_j=P0g_j.                 (1)

Thus r_j is the FULL residual P0(Tf_j+T*h_j)-B0q_j. U, the remote
operator, is absent from (1) because it has no middle variable; its
eventual signed pairing is not paid here. The reference inverse floor,
analytic-response, arithmetic, source-to-Xi, whole-core and unreplayed
c_* qualifications of the cited inputs are retained. The assertions
below concern these explicit operator formulas and do not validate
those original contracts.

Source coverage is the invocation-start SPECIALIZE assessment652,
completed comparison653. Tica--Galapon, *Finite-Part Integration of the
Generalized Stieltjes Transform and its dominant asymptotic behavior
for small values of the parameter*, [arXiv:1703.07979v1](https://arxiv.org/pdf/1703.07979v1),
Theorem4.1/(64)-(65), pp13-15 including (54)-(63), identifies the exact
n=1 correction -v(-t)log(t) for entire v and 0<t<a. The finite cosine
inputs meet that hypothesis. The effective calculation below uses a
constant leading coefficient instead, paying the whole difference
directly on 0<t<=a; it does not infer a derivative bound from an
asymptotic expansion or convergence at its radius. The general
Stieltjes theorem is not reproved.

For gluing import Guermond, *Part III, Chapter14: Traces and interface
jumps of finite elements*, [2016 author-hosted notes](https://people.tamu.edu/~guermond/M610_SPRING_2016/chap14.pdf),
Theorem14.6 and full proof, printed p177/PDFp3. For a finite mesh,
broken W^(1,p) has an Lp distributional gradient exactly when every
interior trace jump is zero. Apply dimension1,p=2 and real/imaginary
parts separately. No periodic endpoint condition is present. This
standard theorem is imported, not reproved. C999(19)'s already
sourced digamma recurrence/sector remainder is used only to bound the
finite diagonal; it retains its DLMF5.11.2/5.11(ii) qualifications.

## Conclusion

There are explicit exact computable functions sigma_j and step functions
J_j, specified below, such that

    r_j=sigma_j+J_j+R_j,       R_j in H1(0,ell),
    ||R_0||_H1<=253066,  ||R_1||_H1<=184234,
    ||R_2||_H1<=324793.                                    (2)

The H1 norm is sqrt(||R||_2^2+||R'||_2^2); in particular324793 is a
single bound for the three fixed columns. The two endpoint terms are

    sigma_j(x)=-(q_j(0)/2)log(a/x),             0<x<a,
    sigma_j(x)=-(q_j(ell)/2)log(a/(ell-x)),     a<x<ell.     (3)

Both one-sided values at a are zero. J_j is the sum of exact jump
coefficients times 1_(xi,ell), over603 distinct candidate interior
interfaces:32 translation events,570 h_m grid events and the midpoint.
A zero coefficient need not be an actual jump. The midpoint coefficient
includes the ENTIRE odd block of S_app, not just h_m. All scalar
coefficients are defined exactly and bounded; no numerical center is
identified with an exact coefficient or a projection moment.

This is a completed local REPRODUCTION under the source gate, initially
written654 and upheld by separate conceptual audit655 below. It gives a finite regularity
bound, not an accurate residual norm, implemented scalar/jump enclosure,
quadrature schedule, tractability guarantee, inverse-pairing certificate,
matrix sign or new general theorem beyond the sources checked. In
particular it proves neither the .000999 X*X comparison nor S3 or RH.
All independent higher/mixed-endpoint, C744q/H2, non-neutral and global
assembly gaps remain. The652 uniform-prescription stop is preserved.

## Proof

### 1. Exact parity map, neutral coefficients and scalar envelopes

Suppress the column subscript until Section6. In the reflected coordinate
t of C999z the unitary and its inverse are

    v_+(t)=[q(ell-t)+q(t)]/sqrt(2),
    v_-(t)=[q(ell-t)-q(t)]/sqrt(2),             0<t<a,
    q(x)=[v_+(x)-v_-(x)]/sqrt(2),             0<x<a,
    q(x)=[v_+(ell-x)+v_-(ell-x)]/sqrt(2),      a<x<ell.   (4)

This follows by centering at a, splitting into even/odd parts with the
sqrt(2) half-interval normalization, then reflecting y to a-t.
On e_n it is sqrt(2)(-1)^n e_n(t) in its parity and zero in the other.
Thus it agrees with C744v/C999z, including the odd sign. Write

    F_epsilon(t)=(1/2)C_end v_epsilon(t)
                   +(h_m v_epsilon)(t)
                   +sum_(l=0)^13 E_epsilon,l v_epsilon(t).  (5)

Then S_app q is the inverse reconstruction of F_+,F_- in (4).
The exact neutral completion of any of the free arrays u_n is

    u_p=-sum_(n>=2,n mod2=p) r_n u_n,
    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2), p=0,1.       (6)

C999q proves the two moment identities. Here 0<r_n<1: for odd n>=3
this is strict increase of k_n; for even n>=2 the numerator is
sqrt(2)/4 and k_n>10, using pi>3 and ell<.6. In particular
|u_0|+|u_1|<=sum_(n>=2)|u_n|, with no approximate neutrality test.

For any such finite free array define the rational envelopes

    M(u)=6 sum_(n>=2)|u_n|,
    L(u)=24 sum_(n>=2)(n+1)|u_n|.                       (7)

The actual arrays here are real dyadics, so these are rational. Since
.5<ell<.6, nu_n<2, sqrt(2)nu_n<3 and k_n<8n, (6) shows that M,L
bound the absolute function and first derivative on the full cell AND
each parity interval. For the derivative use
sum_n n|u_n|<=sum_(n>=2)(n+1)|u_n|; the constant coefficient has
zero derivative. These estimates also apply to complex coefficients
with their absolute values, even though only real arrays occur here.
Write F,L_f for (7) of f, H,L_h for h, and V,L_q for q. Each full-cell
L2 norm is at most its amplitude envelope because ell<1.

### 2. Complete jumps, their exact coefficients and coincidences

For d in (-ell,ell)\{0}, the zero-extended function u(x+d) has exactly
one possible interior jump:

    xi(d)=ell-d,  jump=-u(ell),   d>0;
    xi(d)=-d,     jump=+u(0),     d<0.                  (8)

Use right trace minus left trace. C744v's exact translation part of T
has all sixteen n in

    P7={29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79},
    d_n=7ell-log(n),       a_n=Lambda(n)/sqrt(n).

For each n, include a_n times (8) for (u,d)=(f,d_n) and (h,-d_n).
The adjoint has the reversed delay and the same real weight; its
continuous kernel is the transpose of K. The positive d_n correspond
exactly to29,31,32,37,41,43, as follows from n^2<3^7; no d_n is zero.
These formulas specify all32 translation coefficients exactly.

For i=1,...,m and epsilon=+,- put

    I_i=((i-1)a/m,ia/m),  z_i=(i-1/2)a/m,
    H_epsilon,i=sum_(k=1)^m h(z_i+z_k) integral_Ik v_epsilon(s)ds,
    Delta_epsilon,i=H_epsilon,i+1-H_epsilon,i, i<m.      (9)

Here h is C999z's scalar smooth correction, NOT the endpoint function h.
All arguments z_i+z_k are positive. From (4), the jumps of g due to
the grid, including the minus sign in -S_app q, are

    xi=ia/m:      eta=-(Delta_+,i-Delta_-,i)/sqrt(2),
    xi=ell-ia/m:  eta=+(Delta_+,i+Delta_-,i)/sqrt(2), i=1,...,285. (10)

At the midpoint the complete additional jump is

    eta_a=-sqrt(2) F_-(a),
    F_-(a)=(1/2)integral_0^a v_-(s)/(a+s)ds
              +H_-,m+sum_(l=0)^13(E_-,l v_-)(a).       (11)

All traces in (11) exist. Although v_-(a)=0, the finite approximation
F_- need not vanish there. Using only the h_m contribution in (11)
would therefore be unjustified. The other terms Dq,delta q and the
continuous forcing are smooth at a. There is no translation event at a.

To verify coincidences without samples, the T locations have the form
log(n)-b_n ell, with b_n=6 for d_n>0 and b_n=7 for d_n<0; the T*
locations are their reflections about a. Same-orientation equality
within one group forces the same n. Between groups it would require
a ratio of integers to equal sqrt(3), which is impossible. A reflected
coincidence requires n n'=3^((b_n+b_n'+1)/2). For equal groups this
is irrational; for unequal groups it is3^7, impossible since no
member of P7 is divisible by3. Finally a shift location equalling
any grid point (including a) would imply log(n)/log(3) rational.
If that ratio is p/q in lowest terms, n^q=3^p, contradicting the
prime factorization of n. Thus all32 locations are distinct and avoid
the571 full-cell grid/midpoint locations. The two grids in (10) lie
strictly in opposite half-intervals, so themselves have570 distinct
points. There are exactly603 candidate interior interfaces.

The K,K* parts have no jumps by Section4's uniformly convergent
derivative series. The finite E terms and Carleman terms are smooth
for t>0, including t=a; reconstruction introduces only (11). Projection
subtracts a smooth pair of exponentials and changes none of the jumps.
Consequently (8)-(11) are a complete inventory for r. Define

    J(x)=sum_(all603 events xi) eta_x 1_(xi,ell)(x).      (12)

Every coefficient uses exact q,f,h, not saved floating-point traces.

### 3. Endpoint subtraction on the whole half-interval

For any one of the finite cosine inputs v in (4), with |v|<=V and
|v'|<=L_q, direct addition and subtraction of v(0) in the integral gives

    C_end v(t)=v(0)log(a/t)+A_v(t),
    A_v(t)=v(0)log(1+t/a)
                  +integral_0^a [v(s)-v(0)]/(t+s)ds.    (13)

This is an exact identity for every t>0. It integrates the constant
input explicitly and retains the entire other density. It is the local
specialization needed for quantitative estimates, not a reproof of the
general Stieltjes expansion. In particular no replacement of the exact
analytic multiplier v(-t) by v(0) is made without paying its difference.

The integral in (13) is bounded by a L_q, since |v(s)-v(0)|<=L_q s.
Dominated convergence shows continuity at t=0 and at a. For t>0,
differentiation under the finite integral is valid locally uniformly,
and

    |A_v'(t)|<=V/(a+t)+L_q integral_0^a s/(t+s)^2 ds
              <=V/(a+t)+L_q log(1+a/t).               (14)

The first integral's exact value is log(1+a/t)+t/(a+t)-1.
The square of the second majorant is integrable, because

    integral_0^a log(2a/t)^2 dt
       =a[(log2)^2+2log2+2]<5a.

This follows by t=au and the integrals1,1,2 of1,-log u,(log u)^2;
these are also the endpoint integral used in C999(14). Moreover
||1/(a+t)||_2<=1/sqrt(a), so

    ||A_v'||_2<=V/sqrt(a)+sqrt(5a)L_q.                (15)

The continuous endpoint extension and this L1/L2 derivative majorant
give the weak derivative in (14): apply the fundamental theorem on
[tau,a] and let tau decrease to zero using the integrable derivative.
Thus A_v belongs to H1(0,a), not just H1 on compact interior panels.

After multiplying by1/2 and reconstructing (4), the singular term of
-S_app q is exactly (3): v_+(0)-v_-(0)=sqrt(2)q(0) and
v_+(0)+v_-(0)=sqrt(2)q(ell). The subtraction has zero midpoint traces.
Unitarity, including the sign on derivatives under reflection, and
.25<a<.3 imply that the two regular Carleman parts together have
broken derivative norm at most

    (sqrt(2)/2)[V/sqrt(a)+sqrt(5a)L_q]<2V+2L_q.        (16)

Their midpoint jump is still part of (11), and will be removed by J.
Also the exact integral of the two logarithms gives

    ||sigma||_2^2=(a/2)(|q(0)|^2+|q(ell)|^2)<=aV^2,
    ||sigma||_2<=V.                                   (17)

### 4. Every other term and the full infinite forcing

For K(x,y)=sum_(l>=1)exp[-c_l(7ell+x-y)], c_l=2l+1/2,
one has7ell+x-y>=6ell>3. On the CLOSED square,

    sum_(l>=1)c_l exp(-6ell c_l)
       <3 sum_(l>=1) l/64^l=192/3969<1.              (18)

Here c_l<3l and e>2; the series without c_l is bounded similarly.
The Weierstrass bounds justify differentiation in x and integration
against f or h; their L1 norms are finite. The transpose has the same
bound and opposite derivative sign. Thus the complete Kf+K*h has
derivative norm at most F+H, with no finite-prefix approximation.
For a tail starting at N>=1, the corresponding bound is explicitly
3 r^N[N/(1-r)+r/(1-r)^2], r=1/64; it tends effectively to zero.
This also supplies effective evaluation of all continuous forcing data.

Every a_n<1: log(p)<=log79<5<sqrt29<=sqrt(n), with e^5>79.
On each panel the derivative of the finite translations is therefore
bounded by16(L_f+L_h). Combining with (18), the full forcing has
broken derivative norm at most16(L_f+L_h)+F+H.

For n<=255, C999(19) with K=1 shows |h(k_n)|<20. Explicitly set
z=1/4+ik_n/2. Then1<|z+1|<1021, log|z+1|<8,
1/(2|z+1|)<=.4, 1/|z|<=4 and the sector remainder is less than.16;
also0<log(pi)<2. The strict bound20 follows by the triangle inequality.
The range k_n<2040 follows from Section1. The elementary bound
e>5/2 gives e^8>1021 and e^5>79 as used here. Thus the derivative
norm of (D-delta)q is at most21L_q, and its L2 norm at most21V.

For the finite E sum, use C999z(5) with
phi_l(t)=exp(-c_l t), psi_l(t)=exp[-c_l(2a-t)], b_l=exp(-2ac_l).
Both denominators1-epsilon b_l are at least d=1-exp(-a)>1/5.
Differentiating the OUTPUT variable in each of the four products
gives

    |partial_t E_epsilon,l(t,s)|<=4 c_l exp(-a c_l)/d. (19)

The same bound without c_l controls the kernel itself. Since
r=exp(-2a)<2/3,

    sum_(l>=0)c_l exp(-a c_l)
       <=2r/(1-r)^2+1/[2(1-r)]<27/2.

Multiplying (19) by aV bounds each parity output derivative by81V.
Only l=0,...,13 belong to B_trial, so the infinite geometric expression
is an upper bound, not an omitted action term. Reconstruction gives
full broken derivative norm at most81V since sqrt(2a)<1.

C999z bounds |h'|<=303/16<19 and |h|<=1/4+2a(303/16).
Hence the h_m operator has norm less than3.5, and each output value
has absolute value at most3.5V. The E sum has kernel supremum at most
4/[d(1-exp(-2a))], hence operator norm less than18 and output magnitude
less than18V. The Carleman contribution has norm at most pi/2<2.
It follows that ||S_app||<24. On our finite q, |h(k_n)-delta|<21;
therefore ||B_trial q||_2<=45V. C744v's full bound ||T||<4.71<5 gives

    ||g||_2<=G:=5(F+H)+45V.                            (20)

This uses full operators, not finite square centers. On open panels,
h_m and the subtracted J have zero derivative. Combining all other
terms, the broken derivative norm of g-sigma-J is at most

    16(L_f+L_h)+F+H+23L_q+83V.                        (21)

For later L2 control of J, the translation jump absolute sum is at most
16(F+H). From (9) and the Lipschitz bound on h,

    |Delta_epsilon,i|<=19 a^2 V/m.

Adding both orientations in (10), then both parities, gives total grid
jump sum at most4*19*a^2 V<7V. At t=a the Carleman output has
absolute value at most V log2<V. Together with the value bounds above,
|F_-(a)|<(.5+3.5+18)V=22V. Since sqrt(2)<1.5, (11) has magnitude
less than33V. Thus

    sum_xi |eta_xi|<=16(F+H)+40V,
    ||J||_2<=16(F+H)+40V.                              (22)

### 5. Projection cost, gluing and the H1 ledger

Let W alpha=alpha_+ w_+ + alpha_- w_- and Cg=(<g,w_+>,<g,w_->).
C999 gives P0g=g-WG_w^(-1)Cg, with

    G_w=[[exp(ell)-1,ell],[ell,1-exp(-ell)]].            (23)

No computed moment is assumed exact. The following uniform estimate
pays even the complete unknown moment vector. One has

    tr(G_w)=2sinh(ell)<2,
    det(G_w)=2cosh(ell)-2-ell^2>=ell^4/12>1/192.

The determinant bound follows from the positive cosh series. For the
trace, ell<.6 and exp(.6)<2; the latter follows from its power series,
bounding the tail after the linear term by .6^2/[2(1-.6/3)]<.225.
Thus ||G_w^(-1)||<384 and ||W||=||C||<sqrt(2).
Since W'=W diag(1/2,-1/2),

    ||(WG_w^(-1)Cg)'||_2<=384||g||_2<=384G.            (24)

The projection is smooth; its function norm need not be added separately
because ||P0g||_2<=||g||_2. Using (17), (20), (22),

    ||r-sigma-J||_2<=G+16(F+H)+41V.                    (25)

Equations (13)-(21) prove H1 on every closed panel, including the two
outer panels. All jumps of r are precisely (8)-(11). The subtraction
sigma has no interior jump, including at a, and (12) cancels each
jump exactly. Thus r-sigma-J has matching traces at every interface.
The cited Guermond theorem now gives ordinary H1(0,ell). It would
not follow merely from piecewise regularity, and no periodic seam is
imposed. Its weak derivative is the panelwise derivative. By (21),(24),

    ||R'||_2<=16(L_f+L_h)+F+H+23L_q+83V+384G.          (26)

Adding (25) and (26), which bounds the square-root H1 norm, yields

    ||R||_H1<=1942(F+H)+17449V+16(L_f+L_h)+23L_q.      (27)

This is uniform for any of the three fixed columns once their exact
coefficient envelopes are substituted. The constants deliberately
overestimate the complete moment and jump contributions; none are
fitted to sampled residuals.

The coefficients in (3),(8)-(12),(23) are exact computable numbers.
For (9) use finite sine antiderivatives of the finite cosine inputs;
the E terms use finite exponential/trigonometric integrals with
denominators bounded away from zero. The integral in (11) has a smooth
integrand on [0,a] since its denominator is at least a. For Cg, the
uniform series bound (18) pays the forcing suffix, while C999's full
Carleman action certificate and the logarithmic endpoint estimate pay
the action moments at arbitrary precision by Cauchy--Schwarz.
The positive determinant in (23) pays the two-by-two solve. Exact
locations are the displayed logarithms and rational multiples of ell;
their proved separation permits eventual interval ordering. Thus no
uncertain scalar or location is silently substituted in the identity.
This does NOT assert that their numerical evaluations or subsequent
singular-piece pairings have actually been carried out in this step.

### 6. Exact finite data check and qualifications

Reproduce the finite rational substitution into (27) with

    python3 scripts/separation-seven/jump-log-h1-bounds-654.py

The full certificate is
`scripts/separation-seven/jump-log-h1-bounds-654.json`. It checks the
entire pinned652 NPZ, equality of all96 witness integers with640 and
audit642, the exact supports/denominator, and all762 finite binary64
free trial coefficients. Their exact dyadic values, all envelopes,
every rational ledger entry and input/script hashes are saved. Twelve
checks pass, with no failures. No matrix or operator-center array is
used. Rounding UP the final rational bounds gives, respectively,
253066,184234,324793, proving (2). The full rational value for the last
column is

    6282395223318363954214193951853 / 19342813113834066795298816.

The script verifies coefficient arithmetic and preservation, not the
analytic proof. In particular the integer ceilings are upper bounds
on a regular remainder, not on ||r_j||, and are not smallness claims.
No complete residual or signed Hermitian enclosure was calculated.
Separate conceptual audit655 below checks the signs and normalization,
the full midpoint trace, the projection cost and the retained source
qualifications. Numerical residual certification remains separate.
It changes no earlier negative or inconclusive
route result, and is no possible complete solution of RH.

### 7. Separate conceptual audit — 12 November 2026, step655

The invocation-start SPECIALIZE assessment652/comparison653 covers this
same assertion, with its frozen X, exact Z, B0 and trial coefficients.
The primary Stieltjes and trace-gluing results cited in the hypotheses
are reused within their recorded scope. The audit checks the local
effective specialization rather than reproving either general theorem.
Equations (2)-(27) survive unchanged. No mathematical correction,
new bound, sign result or additional mathematical input is claimed.

**Domains, parity and normalization.** Exact neutral completion (6)
is the ratio of the two C999q moment formulas, for each parity and
both moment signs separately. The frozen trials are finite cosine
sums, hence in Dom(D) intersect H0; C999(3) therefore gives exactly
r=P0(Tf+T*h)-B0q. No unrestricted-inverse compression is used.
The source reference floor and the other imported contracts are not
replayed by this audit. They remain necessary for later inverse use.

Centering the full cell and applying C744v's sqrt(2) parity map,
followed by C999z's reflection, gives (4). Direct substitution on a
single cosine gives sqrt(2)(-1)^n e_n(t) in its parity. In particular
the left reconstruction subtracts the odd component, and the right
reconstruction adds it. Reflection reverses the derivative sign but
does not change its L2 norm. Since r_n<1 for every free index, the
sum of the absolute completion coefficients is at most the free
coefficient mass. Also the completed frequency-weighted sum is at
most sum_(n>=2)(n+1)|u_n|. The bounds sqrt(2)nu_n<3 and k_n<8n
then prove both envelopes (7), including the full-cell versions.

**Complete jump inventory.** Zero extension of u(x+d) removes the
right-end value when d>0 and introduces the left-end value when d<0.
This gives (8), and the adjoint reverses d without conjugating its
real weight. The prime powers in 27<n<81 are exactly the displayed
sixteen; the independent enumeration in the finite audit confirms
the list and both delay-sign groups. At a left grid interface, the
inverse parity combination has jump (Delta_+-Delta_-)/sqrt(2),
so the minus S_app sign gives the first formula (10). At a right
grid interface, increasing x decreases t: the parity-grid jump is
reversed before applying minus S_app, giving the second formula.
At a the reconstruction changes from (F_+-F_-)/sqrt(2) to
(F_++F_-)/sqrt(2). Thus (11) must include the full F_- trace.
The fact v_-(a)=0 gives no cancellation of this finite approximation.

For different shift groups, coincidence in one orientation would
require an integer ratio equal to sqrt(3). Reflected coincidences
would require either an irrational half-integral power of3 or the
integer product3^7, impossible since none of the powers is divisible
by3. A grid coincidence would make log(n)/log(3) rational and hence
force n to be a power of3. This proves distinctness without a
floating-point ordering test, including exclusion of the midpoint.
All remaining action terms are continuous on each open half and
at the noncentral interfaces; the projection is smooth. The603
candidate events are therefore complete, even when some coefficients
vanish. The bound for the paired grid jumps uses
(|Delta_+-Delta_-|+|Delta_++Delta_-|)/sqrt(2)
<=sqrt(2)(|Delta_+|+|Delta_-|); it is below7V after summation.
The complete midpoint trace is below33V, so (22) pays every jump.

**Endpoint weak derivatives and gluing.** Formula (13) integrates
the constant density exactly. It is not an asymptotic replacement
of v(-t) by v(0). The rest has a continuous endpoint value because
|v(s)-v(0)|/(s+t)<=L_q, and its derivative is locally obtained by
dominated differentiation for t>0. The majorant in (14) has finite
L2 norm on the WHOLE interval, as shown by the exact log-squared
integral. It also has finite L1 norm. Passing to t=0 in the
fundamental theorem on [tau,a] therefore proves absolute continuity
and the asserted weak derivative, not just interior smoothness.

Multiplication by1/2 and the inverse parity map produce exactly the
two coefficients -q(0)/2 and -q(ell)/2 in (3). Each logarithm tends
to zero at a. Their combined L2 norm squared is precisely
a(|q(0)|^2+|q(ell)|^2)/2. The regular Carleman derivative is bounded
by (16), with the two parity norms combined in quadrature and the
reflection signs retained. After subtracting J all interior traces
match, including a. Guermond Theorem14.6 applies in dimension1,p=2
to this finite mesh, separately to real and imaginary parts. It
requires no periodic seam or prescribed trace at0 or ell. Thus
the conclusion is ordinary H1(0,ell), with no remaining Dirac mass.

**Complete forcing and quantitative costs.** For l>=1, c_l<3l and
6ell>3 give c_l exp(-6ell c_l)<3l/64^l. The summed bound192/3969
controls both the kernel derivative and the transpose derivative on
the closed square. Uniform convergence justifies the full forcing
derivative and integration; no finite prefix stands in for that sum.
Each translation has its entire smooth derivative on its active
panel, with weight below1. These observations give16(L_f+L_h)+F+H.

For each of C999z(5)'s four E products, output differentiation has
absolute factor c_l. Its denominator is at least d>1/5; summing
with exp(-2a)<2/3 and a<.3 gives the derivative bound81V. The
undifferentiated operator bound is below18. The h_m bound is
.3[1/4+.6(303/16)]=3.48375<3.5; its panelwise derivative is zero.
The Carleman operator contributes below2 to the operator norm,
so ||S_app||<24 is valid. For n<=255 the K=1 digamma estimate
uses ONLY the real part log|z+1|, not a bound on the complex
logarithm by that real quantity. Its terms are bounded by
8+.4+4+.16+2<20, with |z+1|<1021 and Re(z+1)=5/4.
The recurrence/sector remainder is reused exactly as in C999(19).
Consequently the derivative and L2 bounds21L_q and21V for
(D-delta)q, and the full action bound G, are justified.

**Projection and full ledger.** The real symmetric Gram matrix in
(23) is the correct moment matrix under the first-slot-linear
convention. Its determinant exceeds1/192 and its trace is below2.
For its positive eigenvalues, lambda_min=det/lambda_max>1/384.
Hence ||G_w^-1||<384, ||W||=||C||<sqrt(2), and
||W'||<=||W||/2. Their product gives (24). This pays the derivative
of the actual unknown projection coefficients; they are not set
to zero by numerical neutrality. For the function norm use the
orthogonal contraction ||P0g||<=||g||, as in (25).

Adding the function and derivative estimates gives
385G+17(F+H)+124V+16(L_f+L_h)+23L_q, exactly (27).
All coefficient and location formulas are computable as explained
in Section5: finite sine/exponential integrals, a nonsingular
midpoint Carleman trace, a summably bounded forcing suffix and
the complete C999 action certificate suffice. Distinct computable
locations can eventually be separated by intervals. This verifies
computability, not completed numerical coefficient enclosures.

**Independent finite replay.** Reproduce with

    python3 scripts/separation-seven/jump-log-h1-audit-655.py

The full certificate is
`scripts/separation-seven/jump-log-h1-audit-655.json`. No earlier
calculation module is imported and no previous report is overwritten.
The audit checks the pinned NPZ, all96 witness integers against640,
642 and654, every one of the762 exact trial dyadics, all33 rational
ledger entries, the ledger expansion, every final ceiling, all source
pins and the654 generator hash. It also independently enumerates
the prime powers and checks the elementary rational majorants.
All41 checks pass, with an empty failure list and all inputs preserved.
The three upper bounds remain253066,184234,324793. This arithmetic
replay does not replace the analytic checks above.

The new evidence is independent verification of the existing local
regularity result. No progress beyond the inspected source methods
or toward a signed matrix inequality is asserted. Full scalar
enclosures, actual residual norms, inverse pairings, signed U and
the .000999 comparison remain unpaid. The652 uniform-prescription
stop and all inherited analytic/arithmetic/source-to-Xi/whole-core/
c_* qualifications remain intact. Mathlib matching coverage is
unchanged and unchecked; this is not a complete RH candidate.

## Mathlib

Full matching coverage of this fixed three-column residual representation
and its explicit constants was not checked. The source assessment likewise
left it unchecked; this is not evidence of absence. No Mathlib theorem
is used as a matching theorem. Finite interval integration, logarithmic
integrability and Sobolev trace gluing are supporting mathematics, with
the exact imported analytic source and specialization stated above.
