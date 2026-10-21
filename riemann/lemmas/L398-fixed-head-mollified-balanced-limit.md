# Lemma 398: the fixed-head mollified balanced limit is negative

## Hypotheses

Use the actual functions and ordinary jets of L390 and the exact mollifier
of L395. Thus, for real H tending to infinity, set

    ell=log H, vartheta=1/100, Y=H^vartheta,
    P_H(t)=sum_(a<=Y) mu(a)a^(-1/2-it)(log(Y/a)/log Y)^2,
    L(t)=log(2+t), x=f, y=f'/L, z=f''/L^2,
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    Z_N(t)=sum_(r<=N) r^(-5/2-it).

Fix the positive integer N independently of H. No derivative is applied
to the mollifier or to its cutoff. No RH, sign, phase independence,
zero simplicity, common-zero bound or growing-N hypothesis is assumed.

## Conclusion

With both functional-equation diagonals and every ordered response pair
retained, the sharp mean satisfies

    B_N(H)=H^(-1) integral_[H,2H] M |Z_N|^2 |P_H|^2
          = -(10282/1125) sum_(r<=N) r^(-5) + O_N(1/log H).

In particular its fixed-N limit is strictly negative. This evaluates only
the balanced term. It does not assemble the complete signed physical
mean, pass N to infinity, prove an eventual discriminant sign, bound
common zeros, extend actual-theta positivity or resolve RH. The separate
step 74 audit below validates this fixed-N specialization and makes its
compact-height and endpoint justifications explicit. No originality
claim is made.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-mollified-balanced-fixed-head-limit.md`.
The analytic moment input is M. P. Young, *A short proof of Levinson's
theorem*, Arch. Math. 95 (2010), 539–548, DOI
10.1007/s00013-010-0199-9,
[Lemmas 3–7, (6.1)–(6.4), and Section 7](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Import Lemma 5's two-diagonal twisted approximation and Section 6's
approximate-functional-equation contour estimate. The scalar evaluation
is not substituted for a response twist. We prove the finite arithmetic
modification below, because the source's normalization A(0)=1 does not
hold for every response ratio. This is the necessary specialization,
rather than a reproof of the source's moment theorem.

The ordinary-jet conversion and weighted bounds are the audited L395,
importing H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, arXiv:2304.05178v1, 11 April 2023,
[Proposition 1 and (6)–(8)](https://arxiv.org/html/2304.05178v1#S3).
All error estimates below are absolute estimates; M is not assumed
nonnegative.

### Both balanced diagonals, at the actual mollifier length

Let w be any smooth weight satisfying Young (2.1)–(2.3), with scale
T=2H, and put alpha=a/ell, beta=b/ell. The actual length remains
Y=H^vartheta, not (2H)^vartheta. For fixed r,s define

    I_(r,s)(alpha,beta;w)=integral w(t)(r/s)^(-it)
        zeta(1/2+alpha+it)zeta(1/2+beta-it)|P_H(t)|^2 dt.

After opening the two mollifiers, Young Lemma 5 applies with h=ra,
k=sb (here its a,b are integer mollifier indices). For all sufficiently
large H, hk<=N^2 H^(1/50)<=T^(1/25), so the source's fixed twist exponent
1/50<1/2 works. No coprimality is required. The sum of the absolute
mollifier coefficients is O(sqrt(Y)), and their double mass is O(Y).
Thus summing the arbitrary-power source error still gives an arbitrary
negative power of H. Each diagonal has the complete constraint

    r a m=s b n,

with the squarefree a,b weights and both degree-two cutoffs. The second
diagonal replaces (alpha,beta) by (-beta,-alpha) and retains
X_(alpha,beta,t). Initially take small-shift annuli with
|alpha+beta|>=c/ell; holomorphy is addressed before differentiation.

Write u,v for the two mollifier Mellin variables and w_0 for the
approximate-functional-equation Mellin variable. The collision series is

    F_(r,s)=sum_(ra m=sb n) mu(a)mu(b)
         /[a^(1/2+v)b^(1/2+u)m^(1/2+alpha+w_0)
                                     n^(1/2+beta+w_0)].

To compute its local factors, put d=v_p(s)-v_p(r),

    a_p=p^(-1/2-v), b_p=p^(-1/2-u),
    C_p=p^(-1-alpha-beta-2w_0), X_p=p^(-1-u-v),
    U_p=p^(-1-alpha-u-w_0), V_p=p^(-1-beta-v-w_0),
    E_j=p^(-(1/2+alpha+w_0)j)             (j>=0),
    E_j=p^(-(1/2+beta+w_0)(-j))          (j<0).

The four squarefree (a,b) exponent pairs (0,0),(1,0),(0,1),(1,1)
give, respectively, E_d,-a_p E_(d-1),-b_p E_(d+1),X_p E_d,
all divided by 1-C_p. Indeed the remaining m,n exponents satisfy
v_p(m)-v_p(n)=d+v_p(b)-v_p(a); their common increment sums the
geometric series with ratio C_p. Consequently the exact factorization is

    F_(r,s)=zeta(1+u+v)zeta(1+alpha+beta+2w_0)
            A_(r,s)(u,v,w_0;alpha,beta)
             /[zeta(1+alpha+u+w_0)zeta(1+beta+v+w_0)],

where the local factor of A_(r,s) is

    [(1+X_p)E_d-a_p E_(d-1)-b_p E_(d+1)]
                         (1-X_p)/[(1-U_p)(1-V_p)].       (1)

This includes nonsquarefree response indices and their common factors.
For d=0, (1) is exactly the source's unmodified factor, equivalently

    1-(X_p-U_p)(X_p-V_p)/[(1-U_p)(1-V_p)].

For primes outside rs this differs from one by O(p^(-2+epsilon))
uniformly in a sufficiently small fixed product of real-part strips.
The finitely many modified factors are rational functions with
|U_p|,|V_p|<1 there. Hence the Euler product is holomorphic, absolutely
convergent and uniformly bounded on those strips, including all imaginary
parts. No division by an unmodified local numerator is used.

At u=v=w_0=alpha=beta=0, E_j=p^(-|j|/2). If d>=1,
E_d=a_p E_(d-1) and X_p E_d=b_p E_(d+1); if d<=-1 the two
analogous cancellations have a_p,b_p interchanged. Thus its numerator
is zero for d!=0. For d=0 it is 1-1/p, and (1) equals one. It follows
that

    A_(r,s)(0,0,0;0,0)=1_(r=s).                        (2)

### The modified Mellin error, not just its formal value at the origin

Young's Section 6 contour shift in w_0 applies to this product. Move
Re u=Re v=delta, then Re w_0=-delta+epsilon, with fixed sufficiently
small delta and 0<epsilon<delta(1-2vartheta). The only retained
residue is w_0=0: Young's G cancels the pole at
2w_0=-alpha-beta. The finite changes in (1) are bounded on the contour
and introduce no poles. The size Y^(2delta) H^(-delta+epsilon) is
H^(-delta(1-2vartheta)+epsilon), a negative power. The source's gamma,
Gaussian-Mellin and zeta estimates therefore leave a power saving,
even with the annular G normalization's fixed powers of ell. This
justifies the same Section 6 residue reduction at the exact length Y.

Put lambda=log Y. For the sole polynomial u^2 the first diagonal equals

    what(0) zeta(1+alpha+beta) (4/lambda^4) J_(r,s)
                                          + O_N(H^(1-kappa)),
    J_(r,s)=(1/(2pi i)^2) integral integral
       Y^(u+v) zeta(1+u+v) A_(r,s)(u,v,0;alpha,beta)
       /[zeta(1+alpha+u)zeta(1+beta+v)u^3 v^3] du dv,    (3)

for some kappa>0, possibly decreased to absorb logarithms. Here
what(0)=integral w. Contours on small positive lines are legitimate
by absolute convergence before the residue estimates.

We give the extra arithmetic error argument in (3). At w_0=0 expand
the denominator factors in (1) geometrically. For a sufficiently small
fixed delta_1>0 this gives a double Dirichlet series

    A_(r,s)(u,v,0;alpha,beta)=sum_(D,E>=1) a_(D,E)D^(-u)E^(-v),
    sum |a_(D,E)|(DE)^delta_1 <= C_(r,s),                (4)

uniformly for |alpha|,|beta|<=C/ell. For unmodified primes the
weighted absolute mass beyond the constant term is O(p^(-2+4delta_1))
(enlarging this exponent slightly for the shifts), hence summable.
At each of the finitely many modified primes the numerator has finitely
many nonnegative powers of p^(-u),p^(-v), and the two denominators have
ratios of modulus at most p^(-1+delta_1+O(1/ell))<1.
This proves (4) and all its logarithmic coefficient-moment bounds.
It also gives

    sum a_(D,E)=A_(r,s)(0,0,0;alpha,beta)
               =1_(r=s)+O_(r,s)(1/ell).                (5)

The Taylor estimate in (5) follows from holomorphy on a fixed disk and
(2), not from an assumed cancellation of errors.

Here is the one-variable estimate needed to apply (4). For X=e^q>=1,
0<=q<=lambda, set

    V_alpha(X)=(1/(2pi i)) integral X^u
                            /[u^3 zeta(1+alpha+u)] du.

Then uniformly on the shift disks,

    V_alpha(e^q)=q+alpha q^2/2+O_C(1),                 (6)
    V_alpha(X)=0                                      (0<X<1).

For completeness, (6) uses exactly the classical zero-free-region and
reciprocal-zeta input in Young's proof of Lemma 7, p. 546, citing
Titchmarsh, second edition, Theorem 3.8 and (3.11.8). The quantitative
form is nonvanishing and |1/zeta(sigma+it)|=O(log(2+|t|)) in a sufficiently
small region sigma>=1-c_0/log(2+|t|), for large |t|; compact parts near
1 use the analytic reciprocal at its pole. No RH zero-free region is
used. On an initial line Re u=K/(1+q), choose fixed K>C vartheta+2,
so the reciprocal's absolutely convergent Dirichlet series applies.
For large q truncate at height exp(c_1 sqrt(q)) and shift to
Re u=-c_2/sqrt(q), with fixed c_1,c_2 sufficiently small. Since
q<=vartheta ell and |alpha|<=C/ell, the shifted argument remains inside
the quoted zero-free region for all large q. The reciprocal is
O(1+sqrt(q)) on the truncated rectangle. The new vertical integral is
bounded by a fixed polynomial in q times exp(-c_2 sqrt(q)); the
horizontal integrals and original tails have the same type of bound,
using u^(-3) and the absolute reciprocal series on the initial line.
Only the pole u=0 is crossed. For bounded q both the original integral
and the residue are uniformly bounded on a fixed positive line.

Writing Z(alpha)=1/zeta(1+alpha), the residue is exactly
Z(alpha)q^2/2+Z'(alpha)q+Z''(alpha)/2.
The local Laurent expansion gives Z(alpha)=alpha+O(alpha^2),
Z'(alpha)=1+O(alpha), Z''(alpha)=O(1). Its difference from the
right side of (6) is O(1), because |alpha|q is bounded. For X<1 the
absolutely convergent reciprocal series and the degree-two Perron
integral give zero (and also zero at X=1). This proves (6) with the
required uniformity.

Opening zeta(1+u+v) and using (4) now expresses (3) exactly as

    J_(r,s)=sum_(n<=Y) n^(-1) sum_(D,E) a_(D,E)
                      V_alpha(Y/(nD)) V_beta(Y/(nE)).

The interchanges first hold on positive absolute-convergence lines;
(4), (6) and the cutoffs then justify this bounded expression. Put
q=log(Y/n), W_alpha(q)=q+alpha q^2/2. For every D>=1, including
D>Y/n where the left side is zero, (6) gives

    |V_alpha(e^q/D)-W_alpha(q)|<=C(1+log D)^2,
    |V_alpha(e^q/D)|+|W_alpha(q)|<=C(1+q).

For D<=e^q this is the polynomial difference with q-log D; for
D>e^q use q<log D and |alpha|q=O(1). Applying these estimates to
the product and summing the logarithmic moments in (4) produces error
O_(r,s)(ell^2), since sum_(n<=Y)(1+log(Y/n))/n=O(ell^2).
Equation (5) changes the resulting product sum by another O(ell^2).
Finally elementary sum–integral comparison for the degree-four
polynomial (with |alpha|ell,|beta|ell bounded) gives

    J_(r,s)=1_(r=s) [lambda^3/3+(alpha+beta)lambda^4/8
                                      +alpha beta lambda^5/20]
                  + O_(r,s)(ell^2).                   (7)

For this last comparison, the error of sum n^(-1)h(log(Y/n)) against
its integral is O(ell^2): h and its logarithmic derivative are
O(ell^2) on [0,lambda], and integrating the derivative with n^(-2)
gives that bound. Thus (7) includes the complete arithmetic remainder.
Multiplying its error by 4/lambda^4 and by
zeta(1+alpha+beta)=1/(alpha+beta)+O(1) yields O_N(1/ell)
on the initial annuli. The first diagonal coefficient is consequently

    1_(r=s) c_1(a,b)+O_N(1/ell),
    c_1(a,b)=[4/(3vartheta)+(a+b)/2+vartheta ab/5]/(a+b).

The reflected diagonal has c_1(-b,-a) and retains X. Uniform Stirling
on the supported heights gives X=exp(-(a+b))+O_C(1/ell).
Both the exact residue reduction and its power-saving error are uniform
in t there, so integrating the X replacement costs O_N(H/ell).
This does not substitute a scalar mean for an absolute bound on a
signed diagonal. Combining the two terms gives

    I_(r,s)(a/ell,b/ell;w)
       =1_(r=s) what(0) c(a,b)+O_N(H/ell),              (8)
    c(a,b)=1+[4/(3vartheta)-(a+b)/2+vartheta ab/5]
                                      integral_0^1 exp(-v(a+b)) dv.

In particular the apparent a+b pole is removable. The exact I is
holomorphic on every fixed sufficiently large scaled shift bidisk:
its height support is bounded and stays away from zeta's pole.
To extend the error in (8) choose boundary circles |a|=R_1, |b|=R_2
with fixed R_1>R_2 and R_1-R_2>0; they enclose the desired disk and
are in the annular regime above. The two-variable maximum modulus
principle extends the uniform error bound to the interior. Cauchy's
formula then preserves O_N(H/ell) after any fixed scaled derivative,
including order two in each variable. Thus no differentiation is
performed on a singular separate-diagonal formula.

### Ordinary jets and their exact scalar coefficient

L395 identifies f with one constant sign times the real Hardy function.
Use its exact ordinary derivative formulas on each of the conjugate
representations. Freezing theta'/ell at 1/2, and L/ell at one, has
weighted integral error O(1/ell), by the scalar weighted jet bounds and
Schwarz; the theta'' term is retained in that error. The bounded fixed
response head causes no loss. For a product of jet orders j,k the leading
operator on (8) is

    i^j (-i)^k (1/2+partial_a)^j(1/2+partial_b)^k c(a,b)
       =i^j (-i)^k partial_a^j partial_b^k C(a,b) at a=b=0,
    C(a,b)=exp((a+b)/2)c(a,b).

This is a conjugate representation of the same real ordinary derivative;
there is no derivative of P_H. Let s_0=a+b and

    J(s_0)=integral_0^1 exp((1/2-v)s_0) dv
          =1+s_0^2/24+s_0^4/1920+O(s_0^6).

The complete generating function is

    C(a,b)=exp(s_0/2)
             +[4/(3vartheta)-s_0/2+vartheta ab/5]J(s_0).

Consequently the four scalar ordinary-jet coefficients used by M are

    m_00=1+4/(3vartheta),
    m_11=1/4+1/(9vartheta)+vartheta/5,
    m_02=-(1/4+1/(9vartheta)),
    m_22=1/16+1/(60vartheta)+vartheta/15.                (9)

For example the minus sign in m_02 is (-i)^2, whereas the m_22
factor i^2(-i)^2 is positive. The ab term contributes vartheta/5
to m_11 and vartheta/15 to m_22. This keeps both diagonals and all
ordinary carrier derivatives at the constant scale. Taking the actual
signed combination gives

    (m_22+3m_02/2+m_00/16-m_11)/2
        =-1/4-4/(45vartheta)-vartheta/15
        =-10282/1125                                  (vartheta=1/100).

Equations (8)–(9) therefore evaluate the smooth M mean with twist r/s
as this coefficient times 1_(r=s) what(0)/H, up to O_N(1/ell).
The off-diagonal response pairs have not been dropped: their complete
combined holomorphic coefficient has been shown to be O_N(1/ell).

### Absolute removal of both sharp endpoints

Choose a smooth w equal to one on [H+Delta,2H-Delta], zero outside
[H,2H], with Delta comparable to H/ell and 0<=w<=1. Then
what(0)=H+O(H/ell) and its derivatives satisfy the source hypotheses
at scale T=2H. Majorize |1_[H,2H]-w| by two nonnegative smooth
boundary bumps, each with support length O(H/ell), bounded height
and the same derivative scale. They fit [T/4,2T].

The scalar case r=s of (8), its uniformly holomorphic derivatives,
and the ordinary-jet conversion show for each such bump b_0 that

    integral b_0(t) (x^2+y^2+z^2)|P_H(t)|^2 dt
          <= C [integral b_0 + H/ell]=O(H/ell).

Each jet square is nonnegative; its source error is O(H/ell), even
though the bump mass is small. The exact length is still Y; the
preceding Section 6 power estimate and lambda=vartheta ell apply
unchanged. Since |M|<=C(x^2+y^2+z^2) and |Z_N|<=zeta(5/2),
the absolute difference of the sharp and smooth B_N means is
O(1/ell), with both endpoints included. No signed bracketing is used.

Finally expand |Z_N|^2 into every ordered r,s pair with weight
(rs)^(-5/2). There are finitely many pairs, (8) supplies their
uniform fixed-N errors, and only r=s survives at constant scale by
(2) and (7). Its weight is r^(-5), proving the asserted sharp limit.

The exact rational check is reproduced by
`python3 scripts/discriminant/mollified_balanced_coeff.py`; it saves the
complete degree-four generating polynomial and jet coefficients to
`scripts/discriminant/mollified_balanced_coeff_certificate.json`.
That certificate checks (9) and the signed arithmetic combination only;
the analytic errors and limit are justified above, not by a finite preview
or numerical experiment. No comparison with the carrier or infinite
response is part of this result.

### Separate critical audit — 2026-10-11, step 74

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-mollified-balanced-limit-audit.md`
authorizes this REPRODUCTION audit. The claimed sharp limit and its
O_N(1/ell) error pass. The following details close the abbreviated
compact-height and boundary arguments; no complete physical mean or
N-limit is assembled here. Direct local inputs remain L390 and L395.

**Arithmetic and absolute coefficient moments.** Write A_p,B_p for the
squarefree exponents of the two mollifier indices. The valuation equation
is m_p-n_p=d+B_p-A_p. Its minimum nonnegative solution has weight
E_(d+B_p-A_p), and adding j to both exponents multiplies this by C_p^j.
Thus all four cases give the numerator in (1), for every integer d.
At zero shifts put t_p=p^(-1/2). For d>=1 the numerator is
(1+t_p^2)t_p^d-t_p t_p^(d-1)-t_p t_p^(d+1)=0;
for d<=-1 interchange the last two powers. At d=0 it is 1-t_p^2,
giving local A-factor one. This includes arbitrary response prime
powers and common factors: r=s is exactly the case d=0 at every prime.
No unmodified numerator has been inverted.

For d=0, expansion of the numerator gives exactly
1-(X_p-U_p)(X_p-V_p)/((1-U_p)(1-V_p)). In the coefficient norm
sum |a_(D,E)|(DE)^delta_1, each monomial X_p costs p^(-1+2delta_1),
and U_p,V_p cost at most p^(-1+delta_1+C/ell). Each denominator has
a uniformly convergent geometric series. The nonconstant local norm is
therefore O(p^(-2+4delta_1+2C/ell)), with exponent less than -1
for a fixed sufficiently small delta_1 and all large H. At a modified
prime E_d is independent of u,v and the numerator is a finite sum of
nonnegative u,v exponents; its geometric denominators have ratios
strictly less than one in this same norm. Multiplying these absolutely
summable local series proves (4), not merely Euler-product convergence.
It also bounds every fixed logarithmic coefficient moment, since
(1+log D+log E)^k <= C_(k,delta_1)(DE)^delta_1. Holomorphy on a
fixed small alpha,beta bidisk gives (5) uniformly on every prescribed
scaled disk. There are finitely many pairs for fixed N.

**Approximate-functional-equation contour and the height range.** Young,
published version, Lemma 5, pp. 543–544, has both orderings of h,k and
both diagonals. The values h=ra,k=sb fit its fixed exponent 1/50
eventually, and the O(Y) absolute mollifier mass can be absorbed in its
arbitrary-power error. In the Section 6 contour, choose for example
delta=1/100 and epsilon=delta/4, decreasing delta if needed for an
arithmetic convergence strip. On Re u=Re v=delta,
Re w_0=-delta+epsilon, both reciprocal arguments have real part
1+epsilon+O(1/ell)>1. The factor zeta(1+u+v) is also in its
absolute convergence half-plane. A_(r,s) is bounded there uniformly
in all imaginary variables, and (1) has no finite-prime poles.
The pole of zeta(1+alpha+beta+2w_0) is canceled by G; the sole
remaining crossed pole is w_0=0. Gamma poles have real w_0 near
-1/2-2j and are outside this narrow shift.

The source's Section 6, p. 545, writes t>=T/2. The weights used here
at T=2H actually have support inside [T/4,2T]=[H/2,4H], including
the bumps extending slightly below H. The needed power estimate still
follows directly from its gamma formula (4.2) and Stirling (4.3): for
|Im w_0|<=t/2, the gamma quotient on this fixed strip is bounded by
C t^(Re w_0) times a fixed polynomial in 1+|Im w_0|. For the remaining
imaginary tail, the Gaussian in G absorbs the gamma growth. Indeed
the exact gamma quotient has at most exponential growth in t+|Im w_0|
times polynomial factors, while |Im w_0|>t/2 and t>=H/2 make the
Gaussian tail exponentially small in H^2. Since t is between H/2
and 4H, the non-tail integral costs

    C_N ell^K H Y^(2delta) H^(-delta+epsilon)
      = C_N ell^K H^(1-delta(1-2vartheta)+epsilon).

The exponent saving is strictly positive. The fixed power ell^K includes
G's annular shift denominator; u^(-3)v^(-3) are integrable on the
fixed positive lines. This verifies the power saving on the whole
weight support rather than silently citing the narrower height range.
It keeps Y=H^vartheta and T=2H exactly. The reflected shifts satisfy
the identical estimates. At w_0=0 the gamma quotient is exactly one;
the reflected residue is the same t-independent J with shifts
(-beta,-alpha), multiplied by X_(alpha,beta,t).

**Reciprocal contour, including every compact shifted height.** The
quantitative reciprocal input used in (6) is the already assessed
statement of S. Baluyot and S. M. Gonek, *Explicit formulae and
discrepancy estimates for a-points of the Riemann zeta-function*,
Pacific J. Math. 303 (2019), 47–72, DOI 10.2140/pjm.2019.303.47,
[Section 2, p. 53, before (2-3)](https://msp.org/pjm/2019/303-1/pjm-v303-n1-p02-p.pdf#page=9),
citing Titchmarsh (3.11.8). It gives nonvanishing and reciprocal bound
C log |tau| for large positive tau in sigma>=1-A/log tau;
conjugation supplies negative tau. Young p. 546 uses this classical
input. Direct inspection of the original book pages is not asserted.
For the compact portion also use the classical Hadamard–de la Vallee
Poussin zero-free-line theorem: zeta(1+i tau) is nonzero for tau!=0.
After defining 1/zeta(1)=0, the Laurent expansion makes the reciprocal
holomorphic at tau=0. Compactness then gives a fixed-width open strip
around any bounded segment of Re s=1 with bounded holomorphic reciprocal.
This compact argument is essential; analyticity solely at s=1 would
not suffice for the intervening shifted heights.

Fix a scaled shift radius C. For large q<=lambda, |alpha|<=C/ell
implies |alpha|<=C vartheta/q. Put B=exp(c_1 sqrt(q)),
eta=c_2/sqrt(q), and a_0=K/(1+q), with K>C vartheta+2.
Choose c_1,c_2 positive with c_1 c_2<A/4. For sufficiently large q,
the rectangle -eta<=Re u<=a_0, |Im u|<=B, after translation by
1+alpha, lies in the large-height region just stated or in the compact
zero-free neighborhood. Its possible negative displacement from Re s=1
is at most c_2/sqrt(q)+C vartheta/q; its shifted height is at most
B+C vartheta/q. This proves containment uniformly for complex alpha,
including heights for which Im u+Im alpha=0. The reciprocal is
O(1+sqrt(q)) everywhere on the rectangle.

On the initial line its absolute reciprocal series is O(1+q), since
Re(alpha)+a_0>=c/(1+q). The two original tails are
O((1+q)B^(-2)), using exp(q a_0)<=exp K. The horizontal connectors
are O((1+sqrt(q))B^(-3)(a_0+eta)). The new vertical integral is
O((1+sqrt(q))eta^(-2)exp(-eta q)), by integrating |u|^(-3).
All are O(1) uniformly and decay for large q. Only u=0 is a pole;
u=-alpha is a zero of the reciprocal, not an additional residue.
For bounded q the integral on a fixed positive line and the residue
are uniformly bounded. The residue error is bounded by
C(|alpha|^2 q^2+|alpha|q+1)=O_C(1). This proves the entire uniform
statement (6). On an absolute convergence line the Perron expression is
(1/2) sum_(n<=X) mu(n)n^(-1-alpha) log^2(X/n), so it is zero
for X<1 and at X=1. No unproved boundary value is used.

**Two-variable remainder and combined shifts.** On fixed positive
u,v lines all opened Dirichlet series and integrals are absolutely
convergent. The preceding Perron formula therefore gives the exact
double-cutoff expression following (6). Both factors are O_C(1+q),
and replacing either by W_alpha(q) or W_beta(q) costs at most the
corresponding logarithmic coefficient moment times C(1+q), even if
D>exp q or E>exp q. Thus the entire replacement error is O_N(ell^2).
The change (5) costs O_N(ell^(-1) lambda^3)=O_N(ell^2).
For h(q)=W_alpha(q)W_beta(q), both h and h' are O_C(ell^2)
on [0,lambda]. The derivative of h(log(Y/x))/x is bounded in
integral by O_C(ell^2) against x^(-2), proving the stated sum–integral
error. Its integral is exactly the polynomial in (7).

On enclosing scaled circles |a|=R_1,|b|=R_2, R_1>R_2, the factor
|zeta(1+alpha+beta)| is O(ell), so the J error after normalization
is O_N(ell^(-1)). The residue itself is uniformly O_N(1).
Stirling gives X=exp(-(a+b))+O_C(ell^(-1)) throughout [H/2,4H].
Multiplication by this last error costs O_N(H/ell), using the bounded
t-independent residue; it does not require absolute domination of
an unsigned separate-diagonal series. The combined coefficient is
holomorphic at a+b=0. Successive one-variable maximum principles on
the enclosing bidisk and then Cauchy on interior circles preserve one
O_N(H/ell) error through scaled order two in each variable. This
does not differentiate G's singular separated representation.

**Ordinary jets and absolute endpoints.** L395's exact Hardy identity
and derivative formulas yield i^j(-i)^k on the two conjugate factors.
An independent simplification of the generator is

    C(a,b)=cosh((a+b)/2)
       +[4/(3vartheta)+vartheta ab/5]
                         integral_0^1 exp((1/2-v)(a+b)) dv.

Its odd total-degree coefficients vanish. The degree-two and degree-four
terms give exactly (9), including the negative m_02 and positive m_22.
The exact rational script was rerun with zero failures; its complete
degree-four polynomial and all four jet values were inspected. It
verifies the coefficient -10282/1125 against zero, not any analytic
estimate. No derivative of the mollifier or of its cutoff occurs.

To avoid extending L395's sharp interval bound to a different interval,
derive the bump bounds directly from the scalar r=s case of (8).
Before Hardy conversion, its scaled derivative of order (j,j) gives,
for every permitted nonnegative bump b_0 and j=0,1,2,

    integral b_0 |zeta^(j)(1/2+it)/ell^j|^2 |P_H|^2
                   <= C_j (integral b_0 + H/ell).

This follows by the uniform Cauchy bound on c and its error, with
positivity of the displayed integral. The exact Hardy conversion has
bounded coefficients on [H/2,4H], including theta''/ell^2 and ell/L.
The square-of-a-sum inequality gives the identical upper bound for
each actual jet square. On a smooth bulk weight these bounds and
Schwarz control the freezing error by O(H/ell); on a bump they give
O(H/ell) directly, without a freezing assumption.

Choose two fixed smooth profiles scaled by Delta=H/ell, each equal
to one on the corresponding length-Delta boundary piece, with supports
[H-Delta,H+2Delta] and [2H-2Delta,2H+Delta], respectively. They have
height at most one, mass O(Delta), source derivative bounds and support
in [H/2,4H] for large H. Together they majorize the absolute sharp
minus smooth cutoff, at both ends. The preceding bound, |M|<=C U
and |Z_N|<=zeta(5/2) prove absolute error O(H/ell). In particular,
neither L395's O(H) whole-interval envelope nor signed bracketing is
being substituted for the needed small-bump estimate.

Every retained response twist and both diagonals therefore meet the
required normalized O_N(1/log H) threshold. The proof is usable at
fixed N, with existential N-dependent constants and onset. It gives
no bound uniform in growing N, complete signed mean, eventual sign,
common-zero upper count, total L367 margin or RH consequence. The
L390 and L394 failures and repeated-carrier stop remain unaffected.

## Mathlib

Full matching coverage for the twisted mollified moment, its finite-prime
specialization and the ordinary-Hardy-jet limit is not checked. No Lean
verification or library absence is claimed. The complex-analytic and
arithmetic inputs are the precise primary references stated above.
