# Lemma 664: an additional anchor survives two shifted unit grids

## Hypotheses

Use L649's conventions: x=-d=-5/4, R=11/8, U=121/64,
eta=1/100, t_j=j/n for every 0<=j<n, and

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a).

Let q>=1 be an integer, n=12q+3, h=27/(5n), and let
delta be any real number in [1/8,3/8], possibly depending on n.
Take unit original residues at x and at each of the points

    x +/- i*h*(l+delta), x +/- i*h*(l+1-delta), 0<=l<q.

Denote this set by Z. Put M=4q+1=n/3 and retain all its moments:

    c_k(u)=R^(-1) sum_(a in Z) W_a(u)*(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k,
    T_M(v)=sum_(0<=k<M)v^k,
    D=sum_(a in Z) mean_u |W_a(u)|^2/(U-|a|^2),
    H=max_u mean_zeta log|G(u,zeta)|.

Both means are normalized circle means. D is the original
D_single,n with its squared unit residues. The same poles are used
at every angular u; the denominator angle remains 1/u=conjugate(u).

## Conclusion

The family is admissible. For all n>=183 in this sequence, uniformly
in delta and |zeta|=1,

    |G(-1,zeta)-R^(-1) T_M(x*zeta/R)|
                                  <=1000*n*exp(-n/3000).       (1)

Consequently there is one absolute onset, independent of delta,
after which

    c_0(-1)>=1/(2R),       H>=-log(2R).                       (2)

There is a connected angular arc I of normalized length n^(-2)
whose complete paid expression satisfies, for an absolute C,

    log mu(I)+2 mean_(I x T) log|G|-log D+n/16
                          >=(261/10000)*n-3log n-C.           (3)

In particular this family satisfies the approved rate-1/16 criterion
after a uniform onset. The arc is obtained at a maximizer of the
full spatial logarithmic mean, not asserted to be centered at -1.
Equation (1) retains the whole spatial polynomial, not just c_0.

This is a family-specific local advance, not the arbitrary-support
criterion or an RH candidate. The anchor here is additional to both
shifted grids. A grid that itself contains the anchor has a different
sampling identity; (1) is not asserted for it. General support,
matching upper bounds, Xi realization and signs remain open. This
proof received the separate conceptual audit in section 7. It accepts
(1)--(3) with these qualifications; no novelty beyond the recorded
source comparison is certified.

## Proof

### 1. Source scope and the bounded test

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
It covers the exact paid-arc target, with all integer masses,
spatial roots and diagonal costs. The present subfamily is the
two-offset test specified at invocation. The single-lattice
full-circle and endpoint stops in L663/C663a, and the signed saddle
in C663b, were checked as comparisons. They are not premises of
the new contour estimate, and their conclusions are preserved.
The scoped duplicate search found no prior two-offset result.

Import the residue theorem, simple-pole rule, Cauchy integral theorem
and contour absolute-value bound from R. W. Howell and J. H. Mathews,
*Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html)
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
These are the already inspected contour imports recorded in L663
and its source comparison; no new source-manuscript audit is claimed.
The Cauchy integral theorem is also the zero-pole case of the residue
theorem used here. The spatial root formula is F. Brunault and
W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
including boundary roots. L658 supplies the verified logarithmic
integrability, nonzero slices and paid localization, and L661 supplies
its audited general diagonal envelope. No general theorem is reproved.
The shifted kernel and uniform error below are the family-specific
difference not supplied by those imports.

### 2. Admissibility and the exact finite contour

The two positive grids cannot meet: equality would make the integer
l-l' equal to 1-2delta in [1/4,3/4]. Their ordinates are positive,
and neither contains zero. Thus there are exactly 4q+1 distinct poles,
each of residue one, including x. All ordinates have modulus below
Y_n=q*h<Y=9/20, and

    d^2+Y^2=353/200 < (273/200)^2=(R-eta)^2.

This verifies all L649 and L658 hypotheses, without replacing the
original squared-residue census.

Set

    b=1/50, c=1/200, omega=2*pi/h=(10*pi/27)*n,
    Gamma_n=boundary([-Y_n,Y_n]+i[-b,c]),
    K_delta(y)=i*omega/(exp(i*omega*y-2*pi*i*delta)-1)
               +i*omega/(exp(i*omega*y+2*pi*i*delta)-1).

Orient Gamma_n positively, so its lower edge runs left to right.
Its kernel poles are y=h(m+delta) and y=h(m-delta), all simple
of residue one. In -q<y/h<q, the first has -q<=m<=q-1 and
the second -q+1<=m<=q. These are exactly the 4q nonanchor ordinates.
There is no boundary pole or pole at zero. Using Y rather than Y_n
would enclose additional poles for some offsets and is not legitimate.

For y=s+i*v in the closed rectangle put a=x+i*y=-e+i*s,
where e=d+v. Then 123/100<=e<=251/200, and

    |a|^2 <= (251/200)^2+(9/20)^2=71101/40000<16/9.

Thus |a|<4/3<R and |Re a|>=123/100>t_j. The function W_a(-1)
is holomorphic throughout a neighborhood of the rectangle: its
possible variable denominator zeros a=-t_j lie outside it, and its
fixed anchor denominators are nonzero. Its factors U+t_j*a cannot
vanish either, since |a|<U and t_j<1. In particular every contour
shift below is inside a pole-free region of that integrand.

For |zeta|=1 the full geometric polynomial satisfies

    |T_M(a*zeta/R)|<=sum_(k>=0)(32/33)^k=33.             (4)

The residue theorem therefore gives the exact identity

    G(-1,zeta)=R^(-1)T_M(x*zeta/R)
       +(1/(2*pi*i*R)) integral_(Gamma_n)
            W_(x+i*y)(-1) K_delta(y) T_M((x+i*y)*zeta/R) dy. (5)

The separate first term is the actual unit anchor residue. Every
spatial moment 0<=k<M occurs in (5), and the finite sum may also be
extracted coefficient by coefficient. No infinite spatial truncation
or angular continuation is used.

### 3. Complete-product bounds on all four edges

Write W_e(s)=W_(-e+i*s)(-1). Direct division of every grid factor,
including j=0, gives

    W_e(0)=product_j [(d-t_j)/(e-t_j)]
                       *[(U-e*t_j)/(U-d*t_j)]>0,
    W_e(s)/W_e(0)=product_j (1+i*b_j*s)/(1-i*A_j*s),
    A_j=1/(e-t_j), b_j=t_j/(U-e*t_j).                    (6)

Define A_e(t), b_e(t) by the same expressions and
g(e)=integral_0^1 [A_e(t)+b_e(t)]dt. Denominators are strictly
positive on our compact ranges. For e<=R,

    b_e(t)/A_e(t)<=t/R<=8/11,
    partial_e(A_e+b_e)=-A_e^2+b_e^2<=0,
    partial_t(A_e+b_e)=A_e^2+U/(U-e*t)^2>0.             (7)

The first inequality follows on multiplying positive denominators
from e*(R+t)<=R*(R+t). For e<=d one has the sharper b_e<=A_e/2:
it is equivalent to 3*e*t-2*t^2<=U, whose unrestricted maximum
is 9*e^2/8<=225/128<121/64.

Exact monotone 256-cell sums, detailed in section 6, give

    g(123/100)<11/5,             g(R)>9/5.               (8)

Let g_n(e)=sum_j[A_e(t_j)+b_e(t_j)]. Monotonicity in t implies
g_n(e)<=n*g(e), so (7)--(8) give g_n(e)<11n/5 for
123/100<=e<=d. Since partial_e log W_e(0)=-g_n(e) and W_d(0)=1,

    W_e(0)<=exp((11/5)*b*n),            123/100<=e<=d.  (9)

For d<=e<=R, g_n(e)>=g_n(R). The monotone left-sum error is
at most A_R(1)+b_R(1)-A_R(0)-b_R(0)=128/33; hence
g_n(e)>=9n/5-128/33. Integration from d to d+c gives

    W_(d+c)(0)<=exp(16/825-9n/1000)
                                      <=exp(1-9n/1000). (10)

Every factor modulus in (6) decreases when |s| increases, because
0<=b_j<A_j. Thus (9) bounds the whole lower edge, and (10)
bounds the whole upper edge. Also W_e(0)<=1 for e>=d.

Here is a uniform side bound, including the moving endpoints. For
n>=27, Y_n=9/20-27/(20n)>=2/5. For v>=0,
log(1+v)>=v/(1+v), by integrating 1/(1+v). Consequently

    log|W_e(s)/W_e(0)|
       <=-(1/2)sum_j (A_j^2-b_j^2)*s^2/(1+A_j^2*s^2). (11)

If 123/100<=e<=d and |s|=Y_n, use b_j<=A_j/2. All j
have A_j>=4/5; the (n-1)/2 indices with t_j>=1/2 have
A_j>=4/3, since n is odd. Their respective attenuation bounds in
(11) are

    L0=24/689,             L1=24/289.

Combining with (9) yields

    log|W_e(s)| <= -n*[(L0+L1)/2-11/250]+(L1-L0)/2
                                      <=1-n/100,       (12)

because the bracket is 743669/49780250>1/100 and the final
constant is 4800/199121<1. If d<=e<=d+c, use W_e(0)<=1,
A_j>=8/11 and b_j/A_j<=8/11. Each summand attenuation in (11)
is at least

    (1/2)*(57/121)*(256/3025)/(1+256/3025)
                                    =7296/397001>1/100.

This proves (12) on both complete vertical sides. These are
finite-product bounds, with the parity and Riemann-sum errors paid;
no saddle asymptotic or unbounded-domain contour is needed.

### 4. Separate and shift the first frequency; keep every other one

For n>=183, both omega*c and omega*b exceed one. Using
3<pi<22/7 and 2<exp(1)<3, the kernel on the upper edge is bounded
by 4*omega. On a side omega*Re y=+/-2*pi*q. For r>0 and
phi=2*pi*delta in [pi/4,3*pi/4],

    |r*exp(+/-i*phi)-1|^2=(r-cos phi)^2+sin^2 phi>=1/2.

Thus |K_delta|<=2*sqrt(2)*omega<3*omega on both sides, uniformly
in delta and the side height. The combined upper and side lengths
are at most 2Y+2(b+c)=19/20<1. Equations (4), (10), (12),
omega<(6/5)n and 1/(2*pi*R)<1 therefore bound their entire
contribution to (5) by

    (2376/5)*n*exp(-n/3000).                            (13)

For example the rate on the upper edge is 9/1000 and that on
the sides is 1/100, both exceeding 1/3000; the constant uses
4*(6/5)*33*3=2376/5. All orientations are retained in (5) before
this absolute bound is taken.

On the lower edge the exact, uniformly absolutely convergent expansion is

    K_delta(y)=2*i*omega*sum_(m>=1)
                          cos(2*pi*m*delta)*exp(-i*m*omega*y). (14)

It follows by expanding each denominator in inverse powers of its
exponential, whose modulus is exp(omega*b)>2. The total remainder
after m=1 has modulus at most
4*omega*exp(-2*omega*b), regardless of delta. With (4) and (9),
its entire integral contribution is at most

    (792/5)*n*exp(-n/3000),                             (15)

since the lower-edge length is below one and its decay rate is

    (2*omega/n-11/5)*b > (20/9-11/5)/50
                                            =1/2250>1/3000.

The first frequency cannot be bounded on that lower edge by the
same argument. Instead the function

    F_zeta(y)=W_(x+i*y)(-1) T_M((x+i*y)*zeta/R)
                                                  *exp(-i*omega*y)

is holomorphic on our rectangle. Cauchy's theorem moves its lower
left-to-right integral to the upper left-to-right integral, plus
the two vertical joining integrals with their corresponding signs.
There are no kernel denominators in F_zeta and no poles to cross.
On the upper edge |exp(-i*omega*y)|=exp(omega*c); on the sides
it is at most that same quantity. Thus its upper-edge decay rate
is at least

    (9/5-220/189)/200=601/189000>1/3000,

and its side rate is at least

    1/100-(220/189)/200=79/18900>1/3000.

The total length is below one and |T_M|<=33, so the shifted integral
has modulus at most 99*exp(-n/3000). Its coefficient in (5) is
2*i*omega*cos(2*pi*delta)/(2*pi*i*R). Using |cos|<=1 bounds
the whole first-frequency contribution by

    (1188/5)*n*exp(-n/3000).                            (16)

This estimate neither assumes a positive first frequency nor divides
by its cosine; it remains uniform when that frequency vanishes or
delta varies with n. Equations (13), (15), (16) exhaust (5).
Their constants sum to 4356/5<1000, proving (1). In particular
no higher-frequency or endpoint term is left uncharged.

### 5. Full spatial roots and the exact diagonal comparison

The same finite identity and bounds apply to each coefficient of
the full T_M; alternatively, the constant coefficient of a polynomial
is its normalized circle average. Applying this to (1) gives

    |c_0(-1)-1/R|<=1000*n*exp(-n/3000).

Conjugate pole pairs and real product coefficients at u=-1 make c_0(-1)
real. The error tends to zero with one bound independent of delta,
so the first assertion (2) follows after one absolute onset.

For a nonzero polynomial P with nonzero constant coefficient, the
cited root identity gives mean log|P|>=log|P(0)|: in its full
factorization each max(1,|alpha|) is at least |alpha|. Leading
factors, every root, boundary roots and degree drops are retained.
Apply this to G(-1,.) to obtain the second assertion (2).
No logarithmic error estimate near zeros is inferred from (1).

L658 applies to this admissible family and provides a connected arc
of measure n^(-2) with

    log mu(I)+2 mean_(I x T)log|G|
                               >=2H-2log n-32*pi^2/9.

Its inherited nonzero-slice and absolute logarithmic-integrability
proofs justify this even if other spatial slices have boundary roots.
L661's general envelope, with kappa=91/5000 and sigma^2=137/5000,
uses the exact sum of original squared residues, here M=n/3, and gives

    D<=n*exp(2*kappa*n+6)/(3*sigma^2).

Combining these two inputs with (2) proves (3), since
1/16-2*kappa=261/10000. For example one may take
C=2log(2R)+32*pi^2/9+6-log(3*sigma^2). Every bound and onset
used is independent of delta. The positive linear excess eventually
exceeds 3log n+C, proving the stated paid-arc criterion for this
subfamily. No effective final onset or general-support inference
is required or claimed.

### 6. Verification and limitations

Run `python3 scripts/one-sided-hankel/two-offset-anchor.py`.
The complete exact certificate is
`scripts/one-sided-hankel/two-offset-anchor.json`. For each of
e=123/100 and e=R it stores all 257 rational values of A_e+b_e,
their exact left/right sums, and outward rounding to denominator 10^12.
The increasing-in-t property in (7) justifies the quadrature bounds.
The selected outward bounds are

    g(123/100)<=109378422017/50000000000<11/5,
    g(R)>=93186711129/50000000000>9/5.

The certificate checks the domain clearances, both side attenuations,
all five relevant decay rates, parity and Riemann charges, and the
positive paid rate. All checks pass, with no failures; the complete
check map, summary and empty failure list were inspected. The program
evaluates every rational row; it does not use a sampled supremum or
floating-point claim. It does not independently verify the contour
identity, analytic estimates, source manuscripts or inherited L658/L661
proofs. The separate conceptual audit in section 7 checks the analytic
argument and the applicability of the inherited inputs.

The working proposal's rate 1/1000 was weakened to 1/3000 to use only
the elementary inherited bound pi>3. The actual lower bound used for
the tail rate is 1/2250; no stronger unchecked rate is a premise.
This does not change the positive paid exponent, since the polynomial
converges to an anchor contribution of fixed size.

### 7. Independent conceptual audit — 2 November 2026

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-02-two-offset-anchor-audit.md` covers this
exact audit. The audit accepts (1)--(3), without changing their
constants, quantifiers or onset qualifications. This validates the
existing family-specific argument; it establishes no stronger theorem
or progress beyond the sources checked. In particular n>=183 is the
onset of (1), not a claimed onset of (2) or (3).

**Census, orientation and holomorphy.** For the first shifted grid,
the integers -q<=m<=q-1 give the positive ordinates h(l+delta)
and negative ordinates -h(l+1-delta). The second grid supplies the
other two signed lists. Since 2delta is in [1/4,3/4], no grids
coincide, and neither hits zero or the sides +/-qh. Differentiating
the exponential denominator gives residue one at every kernel pole.
The lower edge of the positively oriented rectangle runs left to
right, so the signs in (5) give the sum of the 4q grid residues;
the additional anchor is the separate first term. Its inclusion in
M=4q+1 is essential.

For the whole rectangle, |Re a|>=123/100>t_j and |a|<4/3.
Thus the factors a+t_j in the variable denominator of W_a(-1)
are nonzero. The fixed denominators U-d*t_j are positive. These
facts hold on a neighborhood of the closed rectangle, so the finite
residue theorem and the later holomorphic deformation apply. The
bound |a/R|<32/33 controls the complete T_M by 33, uniformly in its
degree and every spatial angle. No limit in M is taken in (5).

**Products, finite-grid errors and moving sides.** In (6), the
j=0 ratio is d/e times 1/(1-i*s/e); it has not been omitted.
Differentiation gives exactly (7) and partial_e log W_e(0)=-g_n(e).
The increasing-in-t integrand has the left-sum error
0<=n*g(R)-g_n(R)<=128/33. Hence the upper-edge charge is
16/825, not an unbounded error times n. The upper bound at e=d-b
likewise gives the lower-edge growth 11n/250.

The factorwise inequality (11) follows by writing its negative log
ratio as one half of
log(1+(A_j^2-b_j^2)*s^2/(1+b_j^2*s^2)) and applying
log(1+v)>=v/(1+v). At |s|=Y_n>=2/5, the (n-1)/2 indices
with t_j>=1/2 have attenuation at least L1; the other (n+1)/2
have at least L0. This gives exactly the parity charge (L1-L0)/2
in (12). For e>=d the alternate per-factor bound 7296/397001
applies, with W_e(0)<=1. Thus both complete moving sides obey
exp(1-n/100); no fixed-endpoint approximation is involved.

**First frequency, joining sides and full tail.** On the upper edge
omega*c>1 makes each kernel denominator have modulus >1/2.
On either vertical side the fractional phase is +/-2*pi*delta,
so its sine squared is at least 1/2 for every side height. This
charges the entire upper and side contribution in (13), uniformly
even for n-dependent offsets.

On the lower edge, |exp(-i*omega*y)|=exp(-omega*b)<1/2.
Summing the absolute geometric series starting at m=2 yields
4*omega*exp(-2*omega*b), including every remaining frequency.
After the product growth, its rate is greater than 1/2250.
The m=1 integrand has no kernel denominator. Cauchy's theorem moves
it to the upper edge and both joining sides. Their combined length
is at most 19/20, and their respective rates after the exponential
multiplier are at least 601/189000 and 79/18900. Both exceed
1/3000. The orientations do not remove a side; the proof bounds
all three resulting integrals. Its factor cos(2*pi*delta) is only
bounded in absolute value, so delta=1/4 and sign changes are included.
The three error constants add to 4356/5<1000. These contributions
exhaust (5) and prove the stated full-polynomial error.

**Logarithms, inherited hypotheses and the exact diagonal.** The
constant coefficient of the polynomial difference in (1) is its
circle average, so |c_0(-1)-1/R| is bounded by the uniform spatial
error. Conjugate original poles make c_0(-1) real;
1000n*exp(-n/3000)->0 independently of delta. This proves eventual
positivity with a single uniform onset. The cited complete polynomial
root formula then gives mean log|G(-1,.)|>=log|c_0(-1)|, including
boundary roots and degree drops. There is no division by a small
polynomial value and no perturbation estimate for its logarithm.

L658 applies because the original poles remain on Re(a)=x,
|a|<R-eta, with N=M=n/3 and positive integer residues. Its inherited
L657 clearing and nonzero-slice proof were checked: the N distinct
spatial nodes give a nonsingular Lagrange system since N<=M; each
nonanchor angular term has its own uncancelled exterior pole, with
nonzero spatial multiplier T_M(a*zeta/R). The full numerator is
nonzero, so the cited polynomial logarithmic-integrability theorem
applies. The denominator has no angular boundary zero. These facts
justify the product integrals and Fubini even at torus zeros.

In L658's localization, each numerator root loses at most -(log s)/2 under
Poisson averaging and every reflected denominator root has modulus
<4/5. L658 (9), with d_ang=N(n-1)<=n^2/3,
s=1-pi/n^2, and global H-m>=0, gives the stated 16*pi^2/9 arc
loss. Thus its maximizer and normalized arc apply to this full
polynomial, with no assumption about the diagonal-maximizing angle.
This checks the inherited applicability, not unrelated claims of L657.

For D, reuse only L661's already-audited general envelope (3), whose
scope and exact replay are recorded in L662 section 7. The special
phase census of those lemmas is not an assumption here. All 4q+1
original residues are one, hence sum r_a^2=n/3. Subtracting its
logarithmic upper bound from L658's arc lower bound and (2) gives
exactly 261n/10000-3log n-C, with the C written in section 5.
The positive linear term dominates the logarithmic loss after one
absolute onset. No effective final onset is asserted.

**Replay and limits.** Read and reran the exact scalar program in
section 6. It evaluates all 514 rational quadrature values and both
pairs of exact sums. Its complete 22 actual/required comparisons and
empty failure list were inspected; every comparison passes. The two
quadrature bounds are the outward rational bounds recorded above.
The replay checks arithmetic; the finite contour, frequency shift,
uniformity and inherited hypotheses are justified by this audit.
No independent arithmetic backend, source-manuscript audit, general
irregular-support bound, Xi realization or sign conclusion is supplied.
The source citations and Mathlib qualifications below remain in force.

## Mathlib

The reused assessment inspected
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Supporting results include
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. The ordinary analytic nonzero
hypotheses are retained; Lean's totalized logarithm is not a reason
to discard them. Full matching coverage for this two-offset contour,
its uniform error and the paid-arc specialization has not been checked.
Unknown broader coverage is not evidence of absence.

