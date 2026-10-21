# Lemma 430: a fixed-prime signed cubic separates the unchanged Poisson counterlaw

## Hypotheses

Use the actual ordinary critical jets, complete response, physical
Delta and Bcal, and leading polynomials d and B0 of L406--L409.
In particular c=1/(4pi), ell=log H, L=log(2+t),
Z=zeta(5/2+it), R=exp(i phi), E=R^2 and

    (x,y,z)=(f,f'/L,f''/L^2), b0jet=z-x/4,
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    Kjet=(b0jet-iy)^2/2,
    d=c^2[M|Z|^2+Re(Kjet E Z^2)],
    B0=-c[b0jet Re(RZ)+y Im(RZ)].

For the comparison use precisely the complete L429 law nu_(H,t),
with its sufficiently slowly growing Poisson cutoff and uniform
height marginal dt/H. Its exact forms are B(X;t)=b(t)^T X and
D(X;t)=X^T J(t)X. Retain L421's unchanged high and intermediate
kernels and L429's entire translated six-state bulk, including its
mean, full matrix correction and normalizing mass. No actual
conditional distribution, consistency across H, growing prime,
effective cutoff rate, clipping or RH hypothesis is imposed.

H tends to infinity through all sufficiently large real values.
Every response head N used in the proof is fixed before H grows.

## Conclusion

For a positive rational r let num(r) be its numerator in lowest terms,
and define A_u=u^(-2) sum_(a=1)^u gcd(a,u). Put

    kappa=17c^3/20160,
    u_+=num(2mn/k), u_-=num(mn/(2k)),
    gamma_2=(kappa/2) sum_(m,n,k>=1) (mn)^(-2) k^(-3)
                              [sqrt(2) A_(u_+)+A_(u_-)/sqrt(2)]. (1)

This series converges absolutely, and

    (5sqrt(2)/8)kappa <= gamma_2
                  <= (3/(2sqrt(2)))kappa zeta(2)^2 zeta(3).       (2)

Writing E_H for H^(-1) integral_[H,2H], the complete sharp means are

    E_H[Delta Bcal cos(t log 2)]=gamma_2 ell^2+o(ell^2),          (3)
    E_nu[DB cos(t log 2)]=O(ell)+O(ell^2/H)=o(ell^2).            (4)

Thus this unchanged law cannot also match the actual cosine-weighted
cubic with error o(ell^2). It remains valid on its original selected
list. This is a local REPRODUCTION specialization of already assessed
known tools; no originality beyond the sources checked is claimed.
The separate step-216 critical audit below validates (1)--(4).
It supplies no actual clipping,
critical-function or cross-H realization, capped nondegeneracy,
L413 regulator margin, mixed positivity or RH consequence.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-prime-twisted-cubic-coefficient-test.md`.
The completed step-213 discovery and narrow duplicate/failure check
are reused. The target, fixed weight and full law are unchanged.
L427's fixed-mixture stop and L428's uniform-bound stop are contrasts,
not premises for this coefficient comparison. C426c is unused.

### Exact characters and fixed-head coefficient

L407's exact ordinary-jet identity is

    d_N B0_N=c^3 Re{E P1(Djet) conjugate(Z_N)^2 Z_N
                                      +P0(Djet) conjugate(Z_N)^3}.

Here P1=M_D J_plus+J_plus^2 J_minus/4 and P0=J_plus^3/4,
with the exact Djet, J_plus, J_minus and M_D defined in L407.
Expand P_e=sum_nu w_(e,nu) F_nu(s), s=1/2+it, where
F_nu is the product of three ordinary zeta derivatives of orders
0, 1 or 2. Write dnu=nu1+2nu2<=6. The exact weights include all
Omega' terms and obey on the entire height rectangle of L407

    |w|<=C ell^(-dnu), |w'|<=C ell^(-dnu)/H.                    (5)

Since cosine is real, Re(V)cos(t log 2) equals
Re(V exp(it log 2)+V exp(-it log 2))/2. For a response tuple
(m,n,k) put alpha=(mnk)^(-5/2). The single-carrier rational twists
are therefore r=2mn/k and mn/(2k), each with prefactor alpha/2;
the zero-carrier twists are r=2mnk and mnk/2. This is an exact
algebraic multiplication, rather than slowly varying weight transfer.

For fixed positive rational r=u/v in lowest terms and each nu,
L408's arbitrary-rational pole calculation and sharp transfer give

    S_(r,nu,w_(1,nu))
      =H ell^2 sqrt(r) A_u a_nu m_nu+o_(r,nu)(H ell^2),        (6)
    m_nu=(-1)^dnu product_(i=1)^3 p_i!/(dnu+2)!,

where p lists the derivative orders and a_nu is the leading
coefficient of P1 in the formal normalized variables. For clarity,
the source and applicability of this reusable formula are as follows.
Fazzari, *A Voronoi summation formula for the shifted triple divisor
function*, [arXiv:2306.15553v1, (3.5)](https://arxiv.org/html/2306.15553v1#S3),
supplies the finite three-progression identity. Its additive numerator
is -v and modulus u, with (u,v)=1. All classes 1,...,u, including
nonunits and the zero class, remain. The residue-one Hurwitz pole
in [DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i) makes the highest
combined pole coefficient A_u (-1)^dnu product p_i!: summing the
third class gives u exactly when u divides the product of the first
two, leaving u^(-2) sum gcd(a,u)=A_u. Thus it depends on u, not v.
The continuation and polynomial growth needed for the smooth Mellin
step follow from [DLMF 25.11.5](https://dlmf.nist.gov/25.11.E5),
Apostol (1976), (25), p. 269, with positive progression parameter,
Re s>0 and s!=1. L408's proof uses derivative disks in that domain,
then an unsigned d_3 boundary majorant before removing fixed smooth
endpoint bands. It applies to every fixed r here; no sharp indicator
is inserted into Fazzari's Schwartz-weight theorem.

The exact leading weights and their O(ell^(-dnu-1)) errors are
unchanged: the added character is already inside r, not inside w.
L408's complete polynomial and signed polar sum are

    P1 -> X^2 Z/4-X Y^2-X Y Z-X Z^2/2
                              -2Y^3-4Y^2 Z-3Y Z^2-3Z^3/4,
    sum_nu a_nu m_nu=17/20160.                                 (7)

All zero leading monomials retain their lower-order weight errors.
The sharp coefficient convention is H<2pi j/r<=2H. Its full
absolute boundary estimate includes both integer endpoints. The
weight replacement costs O_(r,nu)(H ell); the sharp residue error
is o_(r,nu)(H ell^2). These are exactly the bounds in L408 (8)--(12).

L407's rational support encoding and both sharp connectors apply to
each changed fixed r, with error O_N(H^(71/120)). Its zero-carrier
rule retains j=r if r is an integer and no resonance otherwise;
each such fixed-r contribution is O_(r,nu)(H). Consequently summing
(6)--(7) over the finite head gives

    E_H[d_N B0_N cos(t log 2)]=gamma_(2,N) ell^2+o_N(ell^2),     (8)

where gamma_(2,N) is (1) restricted to m,n,k<=N. Both real
characters and every critical monomial are included. The final real
projection preserves their real leading coefficients.

### Complete single-carrier tails and both sharp endpoints

An integrated signed-tail estimate cannot simply be multiplied by
cosine. Instead specialize L409's frequency-level bounds to each
r=a0 mn/k with a0 in {2,1/2}. On tau=t-iq, 0<=q<=delta=11/20,
the twist has modulus r^q<=1+r^delta. The complete response series
converge normally on a neighborhood of this rectangle: their
exponents allow -3/2<q<3/2. Multiplication by either fixed character
preserves holomorphy and local normal convergence. The separately
controlled L407 connector estimates are

    C(1+r^delta)H^(71/120) for the single carrier,
    C(1+r^delta)H^(1/2) for zero carrier.                       (9)

These sum absolutely against alpha for all four response patterns.
The inherited subconvex/Cauchy input is Bourgain, *Decoupling,
exponential sums and the Riemann zeta function*, JAMS 30 (2017),
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
with the fixed-strip specialization already justified in L407/L409.
No connector bound depending arbitrarily on r is summed.

For completeness the uniform kernel used in L409 is Milinovich--Ng,
*Lower bounds for moments of zeta'(rho)*, author-hosted 19-page
manuscript, [Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9).
For x>0 and fixed 0<kappa0<=a<=2 it bounds the primitive
of chi(1-s)x^(-s), divided by 2pi i, on [a+i,a+iV] by

    1_(x<=V/(2pi)) exp(-2pi i x)
      +O(x^(-a)[V^(a-1/2)
                    +V^(a+1/2)/(|V-2pi x|+sqrt(V))]).          (10)

The constant is independent of x and V. Its stationary, endpoint
and exterior cases are sourced to Gonek, *Mean values of the Riemann
zeta-function and its derivatives*, Invent. Math. 75 (1984),
[Section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
The prior assessment inspected these cases; no new stationary-phase
theorem is reproved. Take a=21/20, x=j/r>0 and use the exact complete
chi kernel. L409 sums (10) against the absolutely convergent
right-line coefficients C_nu(j), then subtracts the primitives at
H and V. Its proof holds for every positive real r, so also for
both fixed scalings here. After integration by parts against the
exact w, the weighted error is at most

    C[H^(11/20)r^(11/20)
       +H^(1/100)r^(-49/100)(1+log_+r)^dnu
       +H^(51/100)ell r^(51/100)(1+log_+r)^dnu].               (11)

Both endpoint errors and the full variation bound (5) are included.
In particular the nearest saddle term in (10) covers exact endpoint
resonance. No error asymptotic is differentiated. For a0=2 or 1/2,

    alpha r^q=a0^q m^(-5/2+q)n^(-5/2+q)k^(-5/2-q).

All q in (11) lie strictly between -3/2 and 3/2, so these sums
converge, including their fixed logarithmic powers. Moreover
1+log_+(a0 mn/k)<=C(1+log_+(mn/k)). Thus summing (11) gives
O(H^(11/20)+H^(1/100)+H^(51/100)ell)=o(H ell^2), uniformly
for every subset of response tuples.

The same source proof bounds the absolute arithmetic main sum by

    |S_(r,nu,w)|<=C H sqrt(r)ell^2(1+log_+r)^(dnu+2).          (12)

Indeed sum_(j<=Y)d_3(j)<=Y(1+log Y)^2; if Y=rH/pi<1 the
sum is empty. For both scalings a common summable majorant is

    B(m,n,k)=(mn)^(-2)k^(-3)(1+log_+(mn/k))^8.                 (13)

Its logarithm is at most 1+log m+log n. Hence its tail epsilon_N
over max(m,n,k)>N tends to zero. This checks the changed characters
at the frequency level before any head limit.

### Denominator-two zero carrier

For r=2mnk or mnk/2, r is on the half-integer grid r>=1/2.
The first twist always has an integer resonance j=r. The second
has that resonance exactly when mnk is even; otherwise it has none.
At an integer resonance the right-line contribution is exactly

    r^(-1/2) C_nu(r) integral_[H,2H] w_(0,nu)(t-i delta)dt.     (14)

L409's bound |C_nu(j)|<=C j^(1/100)log(2j)^dnu and (5) bound
this by C H r^(-49/100)log(2+r)^dnu. Its sum against alpha is
O(H), for either fixed scaling of mnk. This includes j=r=1 and
all undifferentiated coefficients.

For nonresonant j, the unweighted oscillatory primitive is at most

    2r^(11/20) sum_(j!=r) |C_nu(j)|j^(-21/20)/|log(r/j)|.      (15)

Outside r/2<j<2r the denominator is at least log 2, and the
absolutely convergent coefficient sum gives C r^(11/20).
Inside, |log(r/j)|>=|j-r|/(2r). Nonzero distances on this grid
are at least 1/2, and each successive distance interval of length
1 contains at most two integers j. Their inverse-distance sum is
at most C log(2+r). Using j comparable to r and the same coefficient
bound, the interior of (15) is therefore at most

    C r^(51/100)log(2+r)^(dnu+1).

For r=1/2 the interior is empty, and the exterior bound still applies.
These estimates also cover integer r after its single resonance is
removed. Partial summation using (5) multiplies this uniform primitive
bound by at most C ell^(-dnu)<=C, retaining both endpoints. Finally
alpha r^q=a0^q(mnk)^(-5/2+q) for a0=2 or 1/2. The exponents
q=11/20 and 51/100 are below 3/2, so (15) sums to O(1).
Thus the whole zero carrier costs O(H), plus its already summable
connectors. No denominator-two near resonance is left uncontrolled.

### Sequential full-response limit and positivity

Equations (9)--(15) justify absolute summation of the shifted
identities at each H, including every cube complement. In normalized
form they give

    limsup_(H->infinity)
      |E_H[(d B0-d_N B0_N)cos(t log 2)]|/ell^2<=C epsilon_N.   (16)

Here the O(H) zero-carrier term divided by H ell^2 vanishes, as do
all connector and kernel errors. The constant is independent of N.
This is a new application of the frequency bounds, not multiplication
of L409's previously integrated signed error by a bounded function.

Since 0<A_u<=1, (1) is absolutely convergent and gamma_(2,N)
tends to gamma_2. Given a tolerance, choose N first to control
C epsilon_N+|gamma_2-gamma_(2,N)|, and only then take H large
in (8). This proves (3) with d B0 in place of Delta Bcal, for all
real H. L406's absolute physical replacement error O(ell^(5/4))
remains valid after multiplication by bounded cosine, and proves (3)
with the exact physical quantities, full derivatives and curvature.

For the lower bound retain only (m,n,k)=(1,1,1): u_+=2,
u_-=1, A_2=3/4 and A_1=1, so its contribution is

    (kappa/2)[3sqrt(2)/4+1/sqrt(2)]=(5sqrt(2)/8)kappa.

All other terms are positive. Bounding every A_u by one and summing
(mn)^(-2)k^(-3) proves the upper bound (2). In particular the actual
coefficient is rigorously separated from zero without numerical
truncation or a cancellation-sensitive decimal calculation.

### Complete unchanged-law coefficient

Use E_H throughout for the height integral. L421 (4) gives for the
unchanged high component

    E_H[p |D(Y;t)B(Y;t)|]=O(ell).

Thus its cosine-weighted contribution is O(ell). L421 (5) calibrates
the unchanged intermediate component at every height, with the exact
physical forms, by

    k(t)D(Z_mid;t)B(Z_mid;t)=beta_* ell^2.

Consequently its complete weighted integral is beta_* ell^2 times
E_H cos(t log 2), whose absolute value is at most 2/(H log 2).
No averaging of the response-dependent intermediate direction is
needed; its conditional cubic has already been calibrated exactly.

For the bulk retain all of L429's definitions, with K its fixed
positive raw-second matrix and W_H=E_H w:

    d_H=(-b0-J_R)/W_H, m=d_H b/|b|^2,
    A_H=-(Q+E_H[wmm^T])/W_H,
    Sigma=ell g_H K+A_H, g_H=P_(j(H))/N_H,
    N_H=E_H[wP_(j(H))], E_H(wg_H)=1.

These are the full mean and symmetric matrix; neither odd entry is
dropped. L429 proves uniformly bounded J,b,m, W_H>=1/4 and
||A_H||=O(sqrt(ell)). The translated six-state conditional law mu
is centrally symmetric about m, with centered covariance Sigma.
Expanding the exact cubic and cancelling odd centered terms gives

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                       +(m^T Jm)(b^T m).       (17)

All three terms are retained, including the mean-square term.
Bounded J,b,m imply |E_mu DB|<=C(||Sigma||+1). Since g_H is
positive, its exact normalization gives

    E_H[w||Sigma||]
        <=ell||K|| E_H(wg_H)+W_H||A_H||=O(ell).

It follows that E_H[w |E_mu DB|]=O(ell), for the same entire
real-H family and every allowed cutoff j(H) from L429. Multiplying
this conditional expectation by cosine costs at most that bound.
We do not assert E_mu |DB|=O(ell); that different absolute cubic
is unnecessary. No supremum bound on the growing Poisson product
or rate for its cutoff is used.

Adding the three law components proves (4). Combining (3)--(4)
makes their difference divided by ell^2 tend to gamma_2>0;
eventually it is at least (5sqrt(2)/16)kappa. This is the required
coefficient separation with the total remainder o(ell^2).

The downstream implication is restricted: adding this correlation
rejects this unchanged complete law. Redesigning its intermediate
calibration is outside this result. It does not reject L429 on the
selected list it was proved to match, and gives no information about
actual clipped signs, capped nondegeneracy or the quantitative
regulator margin. No RH candidate is obtained.

### Separate critical audit — 2026-10-18, step 216

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-prime-twisted-cubic-separation-audit.md`.
The inspected source coverage and the separate L406--L409/L429 audits
are reused. The following checks concern precisely the changed fixed
characters and the unchanged complete law, not a new moment theorem.

**Characters, poles and normalization.** For a complex V and real t,
Re(V)cos(t log 2)=Re(V 2^(it)+V 2^(-it))/2. In L407's exact
identity, conjugate(Z)^2 Z has phase (mn/k)^(it) and conjugate(Z)^3
has phase (mnk)^(it). Thus both lists of r in the proof are exact,
with a factor 1/2 for each. On the shifted contour the characters
continue as 2^(+/-i tau); they belong to r^(s-1/2), not to a
weight satisfying (5). No derivative of the added oscillation has
been discarded. The exact ordinary-jet coefficients remain unchanged.

For r=u/v reduced, the gamma saddle phase is exp(-2pi i vj/u).
In L408's finite progression identity the leading three pole residues
carry u^(-3). Summing the third class gives u when u divides ab
and zero otherwise. Since v is a unit modulo u, the coefficient is
u^(-2) sum_a gcd(a,u), independently of v. This verifies the
numerator convention for both 2mn/k and mn/(2k), with all nonunit
and zero classes included. L408's smooth-first transfer uses an
unsigned boundary majorant and therefore applies to either complex
phase, including integer endpoints, for each fixed r before H grows.

Substituting D0=X, D1=i(Y+X/2), D2=-Z-Y-X/4 gives
J_plus=-X-2Y-Z, J_minus=-Z and the eight monomials in (7).
Their factorial-rule contributions, put over denominator 20160, are

    420, -840, 336, -56, 336, -224, 48, -3,

whose sum is 17. This checks the complete signed sum without a
numerical approximation or new script. The two zero leading weights
still have L408's O(ell^(-dnu-1)) error. Multiplying the saddle
factor 2pi r^(-1/2) by rH/(2pi), then by alpha/2, gives
H (mn)^(-2)k^(-3)sqrt(a0)/2 for a0=2 or 1/2. There is no
additional real-part factor: all leading residues and weights are
real. This verifies exactly gamma_(2,N), not only its sign.

**Complete tails and both sharp endpoints.** L409's kernel statement
is uniform for every x>0; x=j/r remains positive for either scaling.
Its proof retains the two nearest lattice points to each endpoint,
including a saddle at that endpoint. The spacing is 2pi/r, and the
summed denominator bound is C(H^(-1/2)+r log(2+H)). Subtracting
the H and V primitives gives H<2pi j/r<=V. Partial summation costs
|w(2H-i delta)|+integral |w'|, so (11) includes both endpoints
and all exact analytic-weight variation. No fixed-r error constant
or differentiated asymptotic is summed over the response.

For the powers q=11/20,-49/100,51/100 in (11), the exponents
-5/2+q on m,n and -5/2-q on k are strictly below -1. The fixed
scaling a0 changes only constants, and its positive logarithm costs
at most C(1+log m+log n). The full sum and every cube complement
therefore obey the same o(H ell^2) kernel error. The connector
factor 1+r^(11/20) is summable for each of the four patterns;
normal convergence holds on a neighborhood of the whole contour.
The inherited powers 71/120 and 1/2 are strictly below one.
Finally the absolute arithmetic main terms have the summable
(mn)^(-2)k^(-3)(1+log_+(mn/k))^8 majorant. This is the bound
needed for (16), rather than a bound for the absolute real-line cubic.

**Half-integer zero carrier.** On the right line its frequency is
log(r/j). For r=2mnk the integer resonance is always present;
for r=mnk/2 it is present exactly for even mnk. At j=r the
amplitude is r^(21/20-1/2)r^(-21/20)=r^(-1/2), confirming (14).
The resonance sum costs O(H) because its coefficient after alpha
is O((mnk)^(-5/2-49/100)log(2+mnk)^dnu). The case j=r=1
retains the undifferentiated coefficient; positive derivatives there
vanish, not diverge.

For every other j in (r/2,2r), the logarithmic denominator is at
least |j-r|/(2r). Integer j and half-integer r have nonzero spacing
at least 1/2, giving inverse-distance sum O(log(2+r)). The resulting
power is 11/20+(1/100-21/20)+1=51/100. Outside that band the
denominator is at least log 2. At r=1/2 the band is empty; its
j=1 boundary is in this exterior case. Both resulting powers are
less than 3/2, so summing against alpha gives the claimed O(1)
nonresonant primitive, including weight variation and both endpoints.

The summed errors divided by H ell^2 vanish independently of N,
and the main-term tail tends to zero as N grows. Thus one may choose
N first and H second. The positive coefficient series converges by
A_u<=1; its (1,1,1) term is exactly (5sqrt(2)/8)kappa. L406's
absolute physical error costs O(ell^(5/4)) after bounded cosine
multiplication. This proves the stated complete coefficient and lower
bound for all sufficiently large real H, without a growing-head rate.

**Every component of the unchanged law.** L421's high-state orientation
and cubic bound give E_H[p|DB|]=O(ell). Its intermediate component
has k DB=beta_* ell^2 pointwise, so multiplication by cosine gives
exactly beta_* ell^2[sin(2H log 2)-sin(H log 2)]/(H log 2).
These statements include the zero conventions and both high branches.

For the bulk set X=m+xi. Central symmetry kills the terms linear
and cubic in xi; E xi xi^T=Sigma leaves exactly (17). This
expansion uses the full m and Sigma, including every entry of A_H.
The independently audited bounds |m|+|b|+||J||<=C,
||A_H||=O(sqrt(ell)) and the exact identity E_H(wg_H)=1 give

    E_H[w |E_mu DB|]
       <=C[ell||K||+W_H||A_H||+W_H]=O(ell).

Here 1/4<=W_H<=1 and g_H is positive. This bound is on the
absolute conditional expectation, which is sufficient for the
height-measurable cosine; it does not assert the larger absolute
third moment has this size. The original N_H and all-real-height
cutoff are unchanged. No effective cutoff rate, new phase law or
actual conditional distribution is assumed.

Consequently the complete difference divided by ell^2 tends to
gamma_2>0, and the eventual lower bound stated after (17) follows.
No defect or missing direct mathematical input was found. The
argument and DAG inputs are unchanged. This independent audit validates
the local specialization, not mathematics beyond the cited sources.
Only adding this observable to this unchanged law is excluded; law
redesign, actual clipping, capped nondegeneracy, cross-H realization,
the full-error regulator margin and global mixed positivity remain open.

## Mathlib

Full matching coverage of this sharp rationally twisted cubic and
complete-law comparison has not been checked. The analytic source
inputs are precisely cited above and their previously audited local
specializations are reused. The changed fixed characters, half-integer
zero-carrier estimate, sequential passage and complete-law calculation
are justified here. Unknown Mathlib coverage is not evidence of absence.
No numerical or symbolic script is needed for this specialization;
the finite polynomial sum (7) is the audited exact L408 identity.
