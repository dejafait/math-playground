# Lemma 725: the unchanged constant spatial coefficient retains the bump edge

## Hypotheses

Fix the original actual L703/L708 profile before n varies. Retain the
full L666 family, all unit masses, the anchor, inverse denominator
angle, j=0 factor, original endpoints and all M spatial moments. Use
the audited L714 inverse identities, L719 phase, L720 factorial symbol,
L721 support construction and L723 uniform product/density bounds.
Explicitly, put

    n=12q+3, q>=1, M=n/3, h=A/n,
    d=5/4, R=11/8, U=121/64, A=27/10, c_0=1/8,
    alpha=d+c_0=11/8, u=u_*=(3+4i)/10, Y=9/20,
    s_m=m+1/2, y_m=h*(s_m+e_m), |e_m|<=1/8,
    E=sum_(m in Z)|e_m|<infinity,
    Z_n={-d} union {-d+i*y_m: -2q<=m<2q},
    Q_t(y)=(d+t*u)*(U*u+(d-i*y)*t)
                      /[(U*u+d*t)*(d+t*u-i*y)],
    W_n(y)=product_(j=0)^(n-1) Q_(j/n)(y),
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)
                                  *sum_(k=0)^(M-1)(a*z/R)^k.

Thus W_(-d)=1 and W_(-d+i*y)(u)=W_n(y), including
Q_0(y)=d/(d-i*y). The quantity tested here is the existing coefficient

    G_n(u_*,0)=R^(-1)*(1+sum_(m=-2q)^(2q-1) W_n(y_m)).

Let chi be the same fixed nonnegative smooth positive-frequency bump
supported in I=[omega-delta,omega+delta], equal to one on its middle
half, with 0<delta<1/3000, and b=sup supp chi. L708 supplies

    S_e(v)=sum_m [exp(i*v*(s_m+e_m))-exp(i*v*s_m)],
    |S_e(v)|<=E*|v|, S_e(v)=-chi(v) for 0<v<9/4.

The support lies in (0,9/4). No endpoint law, complex extension of chi,
new choice of profile or n-dependent shift is assumed. L714 gives

    W_n(y)=integral_0^infinity exp(i*y*v/h)*g_n(v)dv,
    g_n(v)=(D_n/h)*exp(-d*v/h)*H_n(exp(-u*v/A)), v>=0,
    g_n(v)=0, v<0,
    g_n(v)=c_0*p_n(v)-h*p_n'(v), v>0.

Here D_n and H_n are exactly L714's finite product and polynomial;
the value at zero in the displayed formula is the right limit, not
the midpoint. For each n this density is integrable, has a finite
first absolute moment, is smooth on each open half-line, and decays
exponentially at positive infinity. Let S(v) and s_v be L719's
holomorphic phase and saddle. L721 gives

    S'(v)=(u*s_v-d)/A,
    1/270<Re S'(v)<1/60, |S'(v)|<1/10, v in I.

Write r(v)=Re S(v). L723, using the audited L722 rate comparison,
supplies r(b)>1/200. All limits below use only n=12q+3 and
log(0)=-infinity.

## Conclusion

Define the signed, unweighted bump integral

    J_n=integral_I chi(v)*g_n(v)dv.

For this unchanged family, with a constant depending on the fixed
profile and a common existential onset,

    R*G_n(u_*,0)=1-J_n+epsilon_n,
    |epsilon_n|<=C*exp(-n/1000),                         (1)
    limsup log|J_n|/n=limsup log|G_n(u_*,0)|/n
                    =r(b)>1/200.                       (2)

In particular (2) exceeds the approved threshold r(b)/2. It supplies
an unbounded subsequence of nonzero constant coefficients. At those
same n, the unchanged full spatial polynomial satisfies

    mean_(|z|=1) log|G_n(u_*,z)|>=log|G_n(u_*,0)|.        (3)

Status: derived in step 208; accepted by the separate step-210
conceptual audit in Section 6 below.
This is a local extension of the existing exact-kernel/support
mechanism within the prior EXPLORE scope, not certified originality.
Only limsup rates are claimed: no full limit, eventual nonvanishing,
effective onset or positivity. The point u_* is inside the angular
disk. No angular-circle transfer, full angular or spatial/global
charge, H/support, Xi realization or actual-Xi mixed signs are proved.
This is not an RH candidate.

## Proof

### 1. Source scope and the changed exact analytic symbol

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-complete-response-zero-moment-edge.md`
and its exact COVERED_TARGET. The prior origin-normalization stop
concerns angular u=0; the highest-moment stop concerns a different
coefficient and profile test. Neither supplies a premise here. L723's
absolute one-sided physical tails are not reused for W_n.

The analytic-symbol and support tools are the already assessed inputs
in L719--L721. In particular import Cauchy's derivative formula,
[NIST DLMF 1.9(iii), (1.9.30)--(1.9.31)](https://dlmf.nist.gov/1.9.iii),
the holomorphic inverse and residue theorems,
[DLMF 1.10(iv),(vii)](https://dlmf.nist.gov/1.10), and the compact
complex Fubini theorem, Terence Tao, *An Introduction to Measure Theory*,
AMS GSM 126 (2011), December 2012 author text, Theorem 1.7.21 and
Corollary 1.7.23, pp.204--206, as precisely cited and checked in L721.
L720 already imports Hitrik--Sjostrand, *Two Minicourses on Analytic
Microlocal Analysis*, [arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1),
Section 2.2 and Theorem 2.3.1, with the complete exact-contour error.
No general stationary-phase or Fourier theorem is reproved. The work
below verifies the changed amplitude and the previously unpaid finite
coefficient correction; citation of the old p_n result alone would not
establish either.

Put P_n(v)=n^(-1/2)*exp(-n*S(v))*p_n(v), using the holomorphic
positive-half-line expression. L720 gives, on a fixed complex
neighborhood of I,

    |a_k|<=C^(k+1)*k!,
    |P_n-sum_(k<m) a_k*n^(-k)|<=C^(m+1)*m!*n^(-m),     (4)

uniformly for 1<=m<=epsilon*n, with a_0 bounded away from zero.
The finite-exponential identity in L714 extends holomorphically to
this neighborhood. Hence the exact changed symbol is

    Q_n(v):=n^(-1/2)*exp(-n*S(v))*g_n(v)
       =m(v)*P_n(v)-(A/n)*P_n'(v),
    m(v)=c_0-A*S'(v)=alpha-u*s_v.                       (5)

Choose a smaller fixed tube with positive distance rho from the
boundary of a tube where (4) holds. Cauchy's formula bounds each
derivative remainder by rho^(-1) times its bound in (4). Set

    a_tilde_0=m*a_0,
    a_tilde_k=m*a_k-A*a'_(k-1), k>=1.                  (6)

These are holomorphic, independent of n, and satisfy factorial
bounds on the smaller tube. For m>=2, substituting the m-term
expansion of P_n and the (m-1)-term expansion of P_n' into (5)
leaves exactly m(v) times the remainder of order m minus A/n
times the derivative remainder of order m-1. Thus, after increasing
a constant C_1, uniformly through the same epsilon*n,

    |a_tilde_k|<=C_1^(k+1)*k!,
    |Q_n-sum_(k<m) a_tilde_k*n^(-k)|
                         <=C_1^(m+1)*m!*n^(-m).        (7)

At m=1, (4) bounds P_n uniformly on the larger tube; Cauchy bounds
P_n' uniformly on the smaller one, giving (7) directly. This treats
the full exact remainder, not the derivative of a pointwise estimate.

L719 gives s_v=x-i*y with 9/5<x,y<37/20 on I. Consequently

    Re m(v)=11/8-(3*x/10+2*y/5)>11/8-259/200=2/25.

After another fixed shrinking, Re m>1/25 and a_tilde_0 is bounded
away from zero. Equivalently L720's explicit leading term gives

    a_tilde_0=s_v*exp(c_0(s_v))/(A*sqrt(2*pi)*sqrt(H(v))),

where c_0(s) is L719's logarithmic endpoint correction and
H(v)=s_v^2*Phi_ss(s_v;v), Re H>1/3. This c_0(s) is distinct from
the fixed scalar c_0=1/8. Every displayed factor is nonzero.

### 2. Support-edge transfer for the changed symbol

We specialize the complete L721 construction, recording the changed
coefficients and the exact-error test. The phase and its injective
sampled arc are unchanged. Define the normally convergent germ

    B(v,t)=sum_(k>=1) a_tilde_k(v)*t^(k-1)/(k-1)!.

By (7) it is jointly holomorphic for |t| sufficiently small on a
common v tube. On a smaller closed t disk, Cauchy gives
|partial_t^j B|<=C_B^(j+1)*j!. Choose ell>0 fixed so that
a=b-2ell, v0=b-ell lie in I and every path

    t=S(v)-S(w), w from v down to a, v0<=v<=b,

lies in that disk. The phase bounds give
Re t>=(v-w)/270, |dt|<=|dw|/10 and Re T_v>=ell/270,
where T_v=S(v)-S(a). Put

    A_n(v)=a_tilde_0(v)+integral_0^T_v exp(-n*t)*B(v,t)dt.

Integrating by parts m-1 times gives the coefficients in (7), an
endpoint term

    -exp(-n*T_v)*sum_(j=0)^(m-2) partial_t^j B(v,T_v)/n^(j+1),

and a remainder n^(-(m-1))*integral_0^T_v
exp(-n*t)*partial_t^(m-1)B(v,t)dt. For m=1 use the original
integral with the endpoint sum empty. Since
integral_path |exp(-n*t)| |dt|<=27/n, the last remainder is at
most 27*C_B^m*(m-1)!/n^m. For C_B*m/n<=1/2 the endpoint sum
is at most (2*C_B/n)*exp(-n*ell/270). Comparing with (7) and
choosing m=floor(eta*n) for fixed sufficiently small eta>0 proves

    sup_[v0,b]|Q_n-A_n|<=C_2*exp(-c*n), c>0.            (8)

Indeed, the two factorial remainders are bounded by
D^(m+1)*m!/n^m<=D*(D*m/n)^m, with D*eta<=1/4. All constants
and paths are fixed before n. The full exact symbol in (7), including
the differentiated complementary-contour error, is used in (8).

Change variables back to w and apply compact Fubini to obtain the
fixed density

    f(w)=a_tilde_0(w)*chi(w)
          +S'(w)*integral_w^b chi(v)*B(v,S(v)-S(w))dv,
                                                   v0<=w<=b.

The substitution dt=-S'(w)dw gives the plus sign. The part a<=w<=v0
and the original part v<=v0 have bound C*exp(n*r(v0)). The latter
uses (7) at m=1. Equation (8) bounds the remaining error. Thus

    n^(-1/2)*J_n=integral_(v0)^b f(v)*exp(n*S(v))dv+E_n,
    |E_n|<=C*exp(n*(r(b)-gamma)), gamma>0.              (9)

For example take gamma=min(c,r(b)-r(v0))/2. Every compact Fubini
integrand is bounded on a finite triangle, so it is absolutely
integrable even though complex-valued.

The actual f has right support edge b. If f vanished on a terminal
interval, division by the elliptic a_tilde_0 would give
|chi(w)|<=C_3*integral_w^b |chi(v)|dv there. On a shorter terminal
interval of length e with C_3*e<1, taking the supremum forces chi=0,
contradicting b=sup supp chi. This does not assume a sign for f.

For completeness the sampled-germ test is as follows. Put
Z(v)=exp(-12*S(v)). Its modulus is strictly decreasing on I,
and Z'(b)!=0. For the fixed-density moments at n=12q+3, q>=0,
the geometric series converges normally on |z|<R_*=exp(-12*r(b)),
giving exactly

    M(z)=integral_(v0)^b H_1(v)/(Z(v)-z)dv,
    H_1(v)=f(v)*exp(3*S(v))*Z(v).                       (10)

It is holomorphic off Gamma=Z([v0,b]). Suppose its germ from zero
extended to a disk of radius greater than R_*. The inverse theorem,
strict modulus monotonicity and compact separation of the remote arc
give a neighborhood U=Z({|w-b|<r0}) in that disk meeting Gamma
exactly in Z((b-r0,b]). U minus Gamma is connected. It meets
|z|<R_* because real w>b sufficiently close to b has Re S(w)>r(b).
The identity theorem identifies the extension with (10) on both
sides of this slit.

For each 0<rho<r0 integrate around the positive image under Z of
|w-b|=rho. Its unique transverse crossing with Gamma is at
Z(b-rho). Near the crossing the denominator is a nonzero complex
multiple of (v-(b-rho))+i*rho*(theta-pi), up to a quadratic error.
Its reciprocal is locally integrable in the two real variables;
bounded numerators and compact separation elsewhere give absolute
Fubini. The residue theorem therefore yields

    0=-2*pi*i*integral_(b-rho)^b H_1(v)dv.

This holds for every sufficiently small rho, so continuity and
differentiation force H_1, hence f, to vanish on a terminal interval.
This contradicts its support edge. Thus (10)'s radius is exactly
R_*. The error series from (9) is holomorphic on the strictly larger
disk |z|<exp(-12*(r(b)-gamma)); finite omitted q change only a
polynomial. If limsup log|J_n|/n<r(b), both normalized J_n and
E_n would have a rate r1<r(b) and their difference would extend (10)
to a larger disk, a contradiction. Conversely (7) at m=1 gives
|J_n|<=C*sqrt(n)*||chi||_1*exp(n*r(b)). This proves

    limsup log|J_n|/n=r(b).                            (11)

This argument proves neither a full limit nor eventual nonvanishing.

### 3. The origin coefficient and paired physical tails

From the audited L723 (8) and the bound for g_n before its (10),
for all sufficiently large permitted n,

    |W_n(y)|<=C*exp(-n/500)/|y|, |y|>=2/5,
    |g_n(v)|<=(d/h)*(3/2)^n*exp(-n*v/5)
              <=C*n*exp(41*n/100-n*v/5), v>=0.         (12)

The latter includes the right limit at zero; it is only an upper
bound. Define the exact high-frequency coefficient

    beta_n=d*product_(j=1)^(n-1) r_(j/n),
    r_t=t*(d+t*u)/(U*u+d*t).

Directly in the rational product, (-i*y)*W_n(y)->beta_n as
y->+infinity. L714's finite partial fractions show
h*g_n(0+)=D_n*sum_j b_(n,j)=beta_n. Taking the same limit in
(12) proves

    |beta_n|<=C*exp(-n/500),
    |g_n(0+)|<=C*n*exp(-n/500).                        (13)

This pays the origin term without assuming continuity through zero.

For t_k=k/n, k>=1, write A_k=d+U*u/t_k and B_j=d+u*j/n.
The exact product is

    W_n(y)=beta_n/(-i*y)*E_n^phys(y),
    E_n^phys(y)=product_(k=1)^(n-1)(1+A_k/(-i*y))
                    /product_(j=0)^(n-1)(1+B_j/(-i*y)).

Here |A_k|<=2n and |B_j|<2 for n>=15; their summed moduli are
at most 4n^2. For real |y|>=L_n:=16n^2, every normalized parameter
has modulus <=1/2. The convergent local logarithms and
|Log(1+z)|<=2|z| give

    |log E_n^phys(y)|<=8n^2/|y|<=1/2,
    |E_n^phys(y)-1|<=16n^2/|y|.

The same beta_n occurs at both signs. Its leading 1/y term is odd,
so the pair, with no modulus taken before addition, satisfies

    |W_n(y)+W_n(-y)|<=32*|beta_n|*n^2/y^2, y>=L_n.    (14)

For Y<=y<L_n, (12) instead bounds that pair by
2C*exp(-n/500)/y. At the unshifted lattice y=h*(k+1/2), k>=2q,
the first point is exactly Y. Integral comparison yields

    sum_(Y<=h*(k+1/2)<L_n) 1/[h*(k+1/2)]
                                     <=C*n*log(n+2),
    sum_(h*(k+1/2)>=L_n) 1/[h*(k+1/2)]^2<=C/(h*L_n).

The endpoint summands are absorbed into C: h<=A/15 and L_n>=16*15^2.
Consequently the unshifted paired tail has absolutely convergent
pairs and total modulus at most C*n*log(n+2)*exp(-n/500).
No separate one-sided series is assigned a value.

To keep both actual displaced endpoints, for real y differentiate
the nonzero product. Each logarithmic derivative has bound

    |Q_t'(y)/Q_t(y)|
       <=t/(U*Re u+d*t)+1/(d+t*Re u)<=2/d.

This also covers t=0. Hence |W_n'|<=(2n/d)|W_n| on the real
line. Each tail displacement segment has |y|>=Y-h/8>2/5 for
n>=15. Equations (12) and h*n=A give

    |W_n(h*(s_m+e_m))-W_n(h*s_m)|
                               <=C*|e_m|*exp(-n/500).

Summing by E<infinity pays every shift in both tails. Define their
joint sum with the original pairing by

    T_n=sum_(k=2q)^infinity [W_n(y_k)+W_n(y_(-k-1))].

It is a convergent series of pairs, and

    |T_n|<=C*(n*log(n+2)+E)*exp(-n/500).               (15)

The original finite interval is exactly the omitted pairs
0<=k<2q. The possibly unequal e_k and e_(-k-1) are retained.

### 4. Midpoint comb, remote frequencies and the exact finite identity

Import the same primary Schwartz Poisson theorem used in L723:
S. D. Miller, *Some notes on distributions*, 15 January 2006,
[Theorem 4.1 and Section 6, pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf).
The zero-moment assessment reuses this coverage and separately checks
the BV/midpoint issue. Here Gaussian regularization verifies the
conditional specialization directly. Its midpoint agrees with
[DLMF 1.14(i), (1.14.3)](https://dlmf.nist.gov/1.14.E3),
whose L1/local-BV hypotheses hold by the finite exponential formula.
No zero-frequency term or independent one-sided limit is discarded.

For fixed n and epsilon>0 apply Poisson to
F_epsilon(s)=W_n(h*s)*exp(-epsilon*s^2). This is Schwartz since
the rational function has no real poles. With
G_epsilon(v)=(4*pi*epsilon)^(-1/2)*exp(-v^2/(4*epsilon)),
absolute Fubini using ||g_n||_1*sqrt(pi/epsilon)<infinity gives

    hat F_epsilon(l)=2*pi*(g_n*G_epsilon)(2*pi*l),
    sum_m W_n(h*s_m)*exp(-epsilon*s_m^2)
        =2*pi*sum_(l in Z)(-1)^l*(g_n*G_epsilon)(2*pi*l). (16)

On the physical side, pair m=k with m=-k-1. The Gaussian weights
are equal within each pair. Equation (14) makes their unregularized
sum absolutely convergent in pairs for each fixed n; dominated
convergence therefore gives the symmetric half-integer sum B_n.

For fixed n, L714's finite formula gives
|g_n(v)|<=C_n*exp(-a_n*|v|), with g_n=0 on v<0 and a_n>0.
For 0<epsilon<=1 this implies

    |(g_n*G_epsilon)(w)|
                     <=2*C_n*exp(a_n^2)*exp(-a_n*|w|).

Indeed use |v|>=|w|-|w-v| and the Gaussian exponential moment.
The bound is summable at w=2*pi*l. At nonzero samples the convolution
tends to g_n(w). At zero, symmetry of G_epsilon, g_n=0 on the
negative half-line and its finite right limit give g_n(0+)/2;
rescaling v=sqrt(epsilon)*t and dominated convergence verifies this
value. Thus (16) yields exactly

    B_n=pi*g_n(0+)+2*pi*sum_(l>=1)(-1)^l*g_n(2*pi*l).  (17)

Negative aliases vanish. Equations (12)--(13) and pi>3 bound this by

    |B_n|<=C*n*exp(-n/500)+C*n*exp(-79*n/100).          (18)

The geometric alias denominator 1-exp(-2*pi*n/5) is bounded below
for n>=15. This passes to the limit for each n before using uniform
asymptotic estimates; no n-uniform regularization limit is assumed.

The shifted-minus-unshifted series is absolutely convergent, because
L714's finite first absolute moment gives

    sum_m integral_0^infinity
       |exp(i*v*(s_m+e_m))-exp(i*v*s_m)|*|g_n(v)|dv
                        <=E*integral_0^infinity v*|g_n(v)|dv<infinity.

Consequently the full shifted paired sum equals
B_n+integral_0^infinity S_e(v)*g_n(v)dv. Its low-frequency part
is exactly -J_n. The remaining part V_n is over v>=9/4, so (12)
gives

    |V_n|<=C*E*n*exp(41*n/100)
                         *integral_(9/4)^infinity v*exp(-n*v/5)dv
             <=C*E*exp(-n/25).                        (19)

There is no negative-frequency contribution because g_n vanishes
there. Removing the single paired tail (15) and adding the unchanged
anchor now gives the exact finite identity

    R*G_n(u_*,0)=1-J_n+B_n+V_n-T_n.                    (20)

The retained indices are precisely -2q<=m<2q, with no endpoint
averaging. Combining (15),(18),(19) gives an error
O(n*log(n+2)*exp(-n/500)); absorbing its polynomial/logarithmic
factor yields (1). Constants may depend on E and the fixed profile.
This proves the full correction estimate before any sampled series
in n is considered.

### 5. Same-subsequence conclusion and the Jensen qualification

Equation (11) and r(b)>0 imply that for every 0<eta<r(b) there
are arbitrarily large permitted n with
|J_n|>=exp((r(b)-eta)*n). On that same subsequence, (1) gives
|R*G_n(u_*,0)|>=|J_n|/2 eventually. The upper bound follows
from (1) and the upper bound for J_n used in (11). Taking eta down
to zero proves (2). Thus the entire correction, including its origin
term and both tails, cannot cancel the bump on the selected subsequence.
Some other coefficients may be zero; no claim excludes that case.

For (3) import F. Brunault and W. Zudilin, *Many Variations of Mahler
Measures*, ISBN 9781108794459, Propositions 1.4--1.5, pp.6--7,
[publisher excerpt](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
as already source-assessed for L666's Jensen interface. At u_* all
original rational denominators are nonzero, as is also clear from
the positive real parts in Q_t on real y. At each n in the indicated
subsequence the polynomial has nonzero constant coefficient. In its
actual degree factorization P(z)=c*product_j(z-alpha_j), its circle
logarithmic mean is log|c|+sum_j log max(1,|alpha_j|), at least
log|P(0)|. Boundary roots and multiplicities are allowed; a constant
polynomial gives equality. This verifies the specialization with
all original moments and any actual degree drop. It is a statement
at angular u_*, not at a point on the angular unit circle.

### 6. Independent conceptual audit, step 210

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-complete-zero-moment-audit.md` covers
exactly this audit. The checks below accept (1)--(3) with their original
hypotheses, common existential onset and limsup qualification. They
introduce no stronger rate or new general theorem. The previously
accepted L714/L719/L720/L721/L723 inputs are used in their stated
scopes; their earlier audits and certificates are not replaced by a
numerical preview. The input list in the canonical DAG is unchanged.

**Differentiation and ellipticity.** L714's finite exponential formula
gives g_n=c_0*p_n-h*p_n' on the positive half-line, and both sides have
holomorphic continuations to the same tube about I. Differentiating
p_n=sqrt(n)*exp(n*S)*P_n therefore gives (5) exactly, with
m=c_0-A*S'=alpha-u*s_v. For nested tubes separated by rho>0,
Cauchy's formula applies to the holomorphic remainder itself. For
m>=2 the derivative remainder of order m-1, multiplied by A/n, is
bounded by A*rho^(-1)*C^m*(m-1)!*n^(-m), while the undifferentiated
remainder has order C^(m+1)*m!*n^(-m). Their sum gives (7) after
enlarging one constant. At order one, boundedness of P_n on the
larger tube gives bounded P_n' on the smaller tube. Thus no derivative
of a merely real or pointwise error is taken. The strict inequalities
x,y<37/20 imply Re(u*s_v)<259/200 and Re m>2/25. Continuity on
compact smaller tubes supplies the claimed nonvanishing amplitude;
the scalar c_0=1/8 is not the logarithmic correction c_0(s).

**Complete symbol and sampled support.** From the factorial coefficient
bound the terms defining B are bounded by C_1^(k+1)*k*|t|^(k-1).
This gives a common positive convergence radius and the stated Cauchy
derivative bounds. Along the actual finite paths, Re t>=(v-w)/270
and |dt|<=|dw|/10 give the bound 27/n. In the endpoint sum successive
majorants have ratio at most C_B*m/n<=1/2. For m=floor(eta*n),
eta small enough for both factorial estimates and m>=eta*n/2,
the remaining bound is D*(1/4)^m plus the exponentially small endpoint
term. This verifies (8) for the full normalized g_n, including the
differentiated complementary-contour error already inside (7).

The change dt=-S'(w)dw produces the positive triangular term in f.
Its integration domain is compact, so complex Fubini is absolute.
The discarded w<=v0 and v<=v0 pieces are O(exp(n*r(v0))); the
symbol error is O(exp(n*(r(b)-c))). Since r'>1/270, their gap is
strictly positive. If f vanished on a terminal interval, ellipticity
and the bounded triangular kernel would give sup|chi|<=C_3*e*sup|chi|
on a shorter interval with C_3*e<1, contradicting b=sup supp chi.
This verifies the support of the actual changed density, without a
sign assumption on f or an analytic continuation of chi.

For the samples n=12q+3, summing the geometric series gives exactly
(10), including its exp(3*S)*Z numerator. Strictly decreasing |Z|
gives global injectivity on the real interval and separates the remote
arc from Z(b); Z'=-12*S'*Z is nonzero. In the inverse coordinate,
U minus the terminal slit is connected and meets the original disk
|z|<R_*. Therefore a hypothetical extension to a larger disk agrees
with the integral on both sides of that slit. At its contour crossing
the two real derivative directions are independent: multiplication by
Z'(b-rho)!=0 preserves the independence of 1 and i*rho. The reciprocal
denominator is bounded locally by a constant times 1/sqrt(x^2+y^2),
which is integrable over a two-dimensional neighborhood. This supplies
the absolute Fubini needed for the residue computation. Its sign is
negative because the kernel is 1/(Z(v)-z). Varying rho forces H_1=0
on a terminal interval if the extension exists, a contradiction.
The error series in (9) has a strictly larger radius, and the factor
sqrt(n) has zero exponential rate. These facts verify (11) for the
same allowed samples, rather than for an interpolating sequence.

**High-frequency coefficient and actual paired tails.** In the rational
product, the numerator degrees are n-1 and the denominator degree is n.
Their leading coefficient is exactly beta_n, with the same value at
both real infinities. L714's partial fractions give
beta_n=D_n*sum_j b_(n,j)=h*g_n(0+), so the uniform real bound (12)
supplies (13). Factoring out that leading coefficient gives precisely
E_n^phys. For n>=15, |A_k|<=d+U*n/2<=2n and |B_j|<2, hence the
sum of their moduli is at most 4n^2. At |y|>=16n^2 every logarithm
is on its convergent local branch. The bounds in (14) then follow
from |exp(z)-1|<=2|z| for |z|<=1/2 and cancellation of 1/(-i*y)
with 1/(i*y). Pairing precedes taking the modulus.

The first omitted unshifted point is exactly h*(2q+1/2)=9/20.
Integral comparison on a lattice of spacing h gives the near-tail
O(n*log(n+2)) and far-tail O(1/(h*16n^2)) sums used in (15).
For the displaced tails, the real parts of the numerator and denominator
of Q_t give the stated logarithmic derivative bound 2/d, including
t=0. Every displacement segment has |y|>=9/20-A/(8n)>=171/400>2/5.
The derivative estimate, h*n=A and sum|e_m|=E thus give an absolutely
summable displacement error O(E*exp(-n/500)). No symmetry of e is
needed. The retained pairs k=0,...,2q-1 are exactly -2q<=m<2q.
This verifies both finite endpoints and avoids assigning values to
the separate divergent half-sums.

**Gaussian comb and origin midpoint.** For each fixed n, the rational
function has no real poles and Gaussian multiplication makes all
derivatives rapidly decreasing. Miller's Schwartz theorem therefore
applies before either regulator limit. With his convention
hat F(l)=integral F(s)*exp(-2*pi*i*l*s)ds, absolute Fubini reduces
the inner integral to

    integral_R exp(-epsilon*s^2+i*s*(v-2*pi*l))ds
      =sqrt(pi/epsilon)*exp(-(v-2*pi*l)^2/(4*epsilon)).

This is the standard Gaussian transform, covered by
[NIST DLMF (7.7.3)](https://dlmf.nist.gov/7.7.E3) at positive real
Gaussian width (combine the two half-line formulas). It equals
2*pi*G_epsilon(v-2*pi*l); no h remains because W_n(h*s) uses
exp(i*s*v). Translating by 1/2 gives (-1)^l. Thus every factor and
sign in (16) agrees with the cited convention.

For the physical limit the two Gaussian weights within each pair
are equal, and (14) dominates their sum for fixed n. For the dual
limit, |g_n(v)|<=C_n*exp(-a_n*|v|) and the Gaussian exponential
moment give the summable majorant
2*C_n*exp(a_n^2)*exp(-2*pi*a_n*|l|), uniformly for 0<epsilon<=1.
At l=0, put v=sqrt(epsilon)*t in the half-line convolution. The
integrand is dominated by C_n*exp(-t^2/4)/sqrt(4*pi), and its limit
integrates to g_n(0+)/2. At positive samples continuity gives g_n,
and at negative samples it gives zero. This proves (17), including
pi*g_n(0+), without using the BV Poisson theorem at its excluded
zero modulation or replacing Gaussian convergence by PV inversion.
Both limits are for fixed n; uniform estimates enter only afterward.

**Complete correction, rate and Jensen.** Absolute Fubini for the
shifted-minus-unshifted sum follows from E*integral v*|g_n(v)|dv<infinity.
Its low-frequency part is -J_n, not +J_n. The alias exponent obeys
41/100-2*pi/5<-79/100, and the remote cutoff gives
41/100-(9/4)/5=-1/25. Thus (18)--(19), together with (15), yield
exactly (20) and O((n*log(n+2)+1+E)*exp(-n/500)); the fixed profile
allows absorption into C*exp(-n/1000) beyond one common onset.
For any 0<eta<r(b), the subsequence |J_n|>=exp(n*(r(b)-eta))
dominates the anchor 1 and this entire error, giving
|R*G_n(u_*,0)|>=|J_n|/2 eventually on that subsequence. The matching
upper rate follows from (7) at order one, so (2) is accepted.

At this angular point, Re(U*u+d*t)>0 and Re(d+t*u-i*y)>0 for
real y and 0<=t<=1; all evaluated rational weights are defined.
The original spatial polynomial has nonzero constant coefficient on
the selected subsequence. The cited Brunault--Zudilin root formula
therefore gives (3), including boundary roots, multiplicities and
degree drops. No statement at an angular boundary or about another
subsequence is inferred. Angular/global charge, H/support, realization
and actual-Xi signs remain independent unresolved obligations.

## Mathlib

Full matching coverage for this exact changed-kernel, midpoint-comb
and paired-tail result has not been checked. Cauchy estimates,
holomorphic inverse/residue theorems, compact Fubini, Gaussian Poisson
summation and polynomial Jensen are supporting ingredients; no exact
Mathlib declarations for the complete result have been verified.
Unknown availability is not evidence of absence.
