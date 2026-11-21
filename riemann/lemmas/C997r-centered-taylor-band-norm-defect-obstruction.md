# Corollary 997r: centered Taylor band sums cannot pay both norm and defect

## Hypotheses

Use the COMPLETE C997c point kernel and C997q definitions, for integer
n>=2:

    I=[7/4,9/4], E=[15/8,17/8], z_star=1+i/8,
    g_n(t)=((L_(n+1)^(2)(t)-1)/(n+1))*exp(-t/2)*cosh(3t/8),
    r=(n+2)/n, a=7n/4, b=9n/4,
    h(t)=exp(i z_star t)-F(t), q(t)=g_n(t)h(t),
    D(x)=r q(rx)-q(x),
    Delta=integral_a^(ra) q(t)dt-integral_n^(n+2) q(t)dt,
    d=sup_(a<=x<=b) exp(-x/4)|D(x)|.

The approved grid consists of gamma_(j,n)=15/8+j/(4n), 0<=j<=n.
Within this grid test the following SPECIFIC centered Taylor construction,
allowing any integer truncation order 0<=m<=n:

    alpha_n=(7-i)n/2, eta_n=exp(-n/4-7in/4),
    w_n(t)=1-exp(i(t-2n)/(4n)),
    T_(n,m)(w)=sum_(k=0)^m (alpha_n)_k w^k/k!,
    F_(n,m)(t)=eta_n exp(15it/8) T_(n,m)(w_n(t)).            (1)

Here (alpha)_k=alpha(alpha+1)...(alpha+k-1), with (alpha)_0=1.
Let lambda_(n,m) be the complex atomic measure whose Fourier transform
is (1), and M_(n,m)=||lambda_(n,m)||_TV. All coefficients with j>m
are zero. There is no additional scalar renormalization: eta_n is fixed
by matching the target at t=2n. Arbitrary grid coefficients, other
centers and other approximation rules are outside this corollary.

Both beta contributions, K's subtraction and both windows remain in
the definitions. No division by g_n, zero simplicity, actual-zero
realization, selected-response identity or RH hypothesis is assumed.

## Conclusion

Put rho=(log(168)-5)/24>1/400. For every n>=2 and m>=n/24,

    M_(n,m) >= [7/(10 e n)] exp(rho*n).                    (2)

There are constants c>0 and n_0, independent of m, such that for
every n>=n_0 and 0<=m<n/24,

    d_(n,m) >= c n^(-3/2) exp(n/64).                       (3)

Thus NO sequence of the centered Taylor sums (1), with arbitrary
choices m=m_n in [0,n], has BOTH subexponential original variation
and d=O(exp(-n/64)). It cannot meet the proposed three simultaneous
requirements including exp(-a/4)|Delta|=O(exp(-n/64)), regardless
of its boundary values. Formula (3) is a lower bound for the COMPLETE
defect, not merely failure of an approximation upper envelope.

This stops only (1), not the full equispaced-band family. The two
weighted conditions are sufficient for C997q's point residual, not
necessary; even for (1) we infer no lower bound for that residual from
(3). Arbitrary grid coefficients and the general approximate point
bridge remain open. The onset in (3) is existential because the reused
bulk asymptotic has an existential onset. There is no RH candidate.

Step367, 11 November 2026: RESEARCH / POTENTIALLY_NEW, scoped NEGATIVE,
under the pre-invocation EXPLORE review365, separately approved in
step366. This is a local quantitative specialization of known tools;
the recorded search did not identify this exact statement and does
not certify originality. The independent conceptual audit in step369
below accepts (2)-(3) without changing their hypotheses or constants.

## Proof

### Reused inputs, scope and the complete residual check

Reuse audited C997c(1),(4)-(6), in particular the exact finite-measure
kernel and its real bound

    |g_n(t)|<=2(n+2) exp(3t/8), t>=0.                      (4)

The underlying Laguerre input is
[NIST DLMF 18.14.8](https://dlmf.nist.gov/18.14.E8); C997c includes
the original subtraction. Its finite-complex-measure Fubini contract
is specified in its step322 audit: Axler, *Measure, Integration & Real
Analysis*, author version 12 June 2026, 9.10 and 9.41(b), and Tao,
[*245A, Notes 6*, Theorem 43](https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/).

Check C997q(1)-(2) directly, rather than assuming its entire unaudited
argument. Finite variation on compact frequency and time intervals
permits Fubini in BOTH windows. If J(x)=integral_x^(rx) q(t)dt and
B=integral_n^(n+2) q(t)dt, the complete point residual is

    R(x/n)=-2 exp(-x/4)[J(x)-B].

The fundamental theorem of calculus gives J'(x)=D(x), hence

    R(x/n)=-2 exp(-x/4)[Delta+integral_a^x D(u)du],
    ||R||_(C(I))<=2 exp(-a/4)|Delta|+8d.                  (5)

Indeed exp(-x/4) integral_a^x exp(u/4)du<=4, including endpoints.
This verifies exactly the sufficient implication used to motivate the
target, not the rest of C997q. No reverse differentiation estimate is
asserted. To refute the simultaneous conditions it is enough to prove
(2)-(3); no boundary term is discarded or claimed to cancel a defect.

The sole additional kernel input is the uniform REAL bulk formula
already established in C997e(4) and checked in its step329 audit:
for c in J=[15/8,17/8],

    L_(n+1)^(2)(cn)/(n+1)
      =n^(-3/2) exp(cn/2)
         [A(c) cos(n phi(c)+psi(c))+O(1/n)],
    A(c)=sqrt(2/pi)c^(-5/4)(4-c)^(-1/4)>0,
    theta(c)=arccos(1-c/2),
    phi(c)=theta(c)+sqrt(c(4-c))/2,
    psi(c)=5theta(c)/2-5pi/4,
    phi'(c)=(1/2)sqrt((4-c)/c), theta'(c)=1/sqrt(c(4-c)).  (6)

The O(1/n) is UNIFORM on this fixed closed J. C997e imports
M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal polynomials
and applications in random matrix theory*,
[math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
Theorem 2.4(b)/(2.13), Remarks 2.3/2.5, Proposition 3.31,
Theorem 3.32 and Proposition 5.1/(5.5)-(5.6), printed pp5-7,32-34,39.
The specialization is the SAME Q(x)=x, alpha=2>-1, N=n+1 and
normalization p_N=(-1)^N L_N^(2)/sqrt((N+1)(N+2)); its source norm
is [DLMF Table 18.3.1](https://dlmf.nist.gov/18.3#T1).
Reviews291/325 and the C997e audit already assessed these contracts.
Here only u=0 and real c in that same J are used. There is no new
complex domain, saddle, varying curvature, or Gaussian-packet input.

The general inputs are imported, not reproved. The coefficient and
phase argument below is needed because known finite-sum approximation
or minimum-energy formulas do not supply this original-TV/complete-D
dichotomy. In particular a worst-direction energy upper bound is not
used as a lower bound. C997g's complete jet conditions concern slope
densities, not the atomic band measures (1); the recorded packet and
exact-chain stops are comparisons, not additional premises.

### Exact original coefficients and the high-order cost

Near t=2n, the local logarithm of 1-w_n(t) is i(t-2n)/(4n).
Therefore

    exp(i z_star t)/exp(15it/8)
            =eta_n (1-w_n(t))^(-alpha_n).

The standard generalized binomial theorem
([DLMF 4.6.7](https://dlmf.nist.gov/4.6.E7), |w|<1) identifies (1)
as its Taylor truncation. It matches the first m derivatives in the
local coordinate w. No moving-window convergence is imported from
the fixed-compact superoscillation theorem in review364.

For any alpha with alpha+j!=0, finite expansion gives

    sum_(k=0)^m (alpha)_k(1-z)^k/k!
       =sum_(j=0)^m (-1)^j (alpha)_(m+1)
                            z^j/[(alpha+j)j!(m-j)!].      (7)

For completeness, the z^j coefficient on the left is
(-1)^j(alpha)_j/j! times sum_(l=0)^(m-j)(alpha+j)_l/l!.
Induction on M gives sum_(l=0)^M(beta)_l/l!=(beta+1)_M/M!;
substitution proves (7). Our alpha_n+j has positive real part, so
there is no division by zero. Substituting z=exp(-i/2)exp(it/(4n))
gives the original grid coefficients

    A_(j,n,m)=eta_n (-1)^j exp(-ij/2)(alpha_n)_(m+1)
                             /[(alpha_n+j)j!(m-j)!], j<=m.

Distinct real frequencies imply that the variation is exactly

    M_(n,m)=exp(-n/4)|(alpha_n)_(m+1)|
                 *sum_(j=0)^m 1/[|alpha_n+j|j!(m-j)!].     (8)

Since |alpha_n+k|>=7n/2 and |alpha_n+j|<5n for 0<=j<=m<=n,

    M_(n,m)>=(7/10)exp(-n/4)(7n)^m/m!.                    (9)

For m>=1, monotonicity of log gives
log(m!)<=integral_1^m log t dt+log m, so
m!<=e m(m/e)^m. Write s=m/n. The exponent in (9) is at least
n[-1/4+s(log(7/s)+1)], apart from the factor 7/(10 e m).
The bracket is increasing for 0<s<=1, since its derivative is
log(7/s)>0. At s=1/24 it is rho. Also m<=n, proving (2).

An elementary positive margin avoids relying on decimal logarithms.
The exponential series gives e<11/4 and exp(3/50)<50/47; moreover
(11/4)^5(50/47)<168. Thus log168>5+3/50 and rho>1/400.
These facts concern the ACTUAL coefficient variation (8), not a
triangle-inequality upper estimate for it.

### Low orders: the two endpoint values cannot be collinear

Now take 0<=m<n/24 and put

    J_n=[17/8-16/n,17/8], x=cn, y=c(n+2), c in J_n.

For all sufficiently large n, J_n is a subset of J and
c>=53/25. For t=x,y, set vartheta_t=(t-2n)/(4n). It is positive,
less than pi, and

    |w_n(t)|=2sin(vartheta_t/2)>=31/1000.                 (10)

For an explicit sufficient onset for these elementary statements take
n>=32768: vartheta_x>=1/32-1/8192, vartheta_y>=vartheta_x,
and vartheta_y<1/16. The bound sin v>=v-v^3/6 proves (10).

Write U_k(t)=(alpha_n)_k w_n(t)^k/k!. For 1<=k<=m,

    |U_(k-1)(t)/U_k(t)|
       =k/(|alpha_n+k-1||w_n(t)|)<=250/651.

Consequently, with V_t=T_(n,m)(w_n(t))/U_m(t),

    |V_t-1|<=sum_(l>=1)(250/651)^l=250/401,
    |V_t|>=151/401, |arg V_t|<7/10.                      (11)

The argument is the branch about 1; the disk does not contain zero.
Indeed sin(7/10)>=3857/6000>250/401, and the maximum angle subtended
by a disk of radius R<1 about 1 is arcsin R. The m=0 case has
U_0=V_t=1 and satisfies all the same bounds. The ratio estimate also
shows |U_m(t)|>=1, so

    |F_(n,m)(t)|>=(151/401)exp(-n/4), t=x,y.              (12)

For 0<vartheta<pi,
w=2sin(vartheta/2)exp(i(vartheta/2-pi/2)). The phases of eta_n
and (alpha_n)_m cancel in the ratio F(y)/F(x). A representative of
its phase is therefore

    (15/8)(y-x)+m(vartheta_y-vartheta_x)/2
                       +arg V_y-arg V_x
       =(15/4+m/(4n))c+arg V_y-arg V_x.                  (13)

The first term lies between 79/10 and 8: use c>=53/25,
c<=17/8 and m/n<1/24; the upper bound is 6137/768<8.
By (11), the full phase in (13) lies in [13/2,47/5].
Using 157/50<pi<22/7, this interval lies strictly between 2pi
and 3pi, at distance at least 1/50 from either endpoint. Hence

    |sin(arg(F(y)/F(x)))|>=1/100.                        (14)

For the last bound use sin v>=v-v^3/6 at v=1/50 and symmetry
and monotonicity of sine on [0,pi]. No argument winding or asymptotic
phase derivative of the Taylor sum has been assumed.

### A real bulk peak and the complete defect lower bound

Both g_n(x) and g_n(y) are REAL. Define the approximant-only defect

    D_F(x)=r g_n(y)F_(n,m)(y)-g_n(x)F_(n,m)(x).

Project this vector perpendicular to F_(n,m)(y), which is nonzero
by (12). The first term has zero projection. Equations (12),(14) give

    |D_F(x)|>=(1/100)|g_n(x)F_(n,m)(x)|
             >=[151/40100]exp(-n/4)|g_n(x)|, c in J_n.    (15)

This works even if g_n(x) or g_n(y) vanishes. No inverse kernel or
assumption about its zeros is involved.

To find one useful x, use (6). On J, phi'(c)>2/5 and theta'(c)>0.
The phase n phi(c)+psi(c) therefore increases by more than
32/5>2pi across J_n. There is c_n in J_n at which this phase is
an integer multiple of 2pi. Let A_min=min_J A(c)>0. The UNIFORM
O(1/n) in (6), the retained -1, and cosh(3x/8)>=exp(3x/8)/2
give, for all sufficiently large n and x_n=c_n n,

    |g_n(x_n)|>=(A_min/8)n^(-3/2)exp(3x_n/8).             (16)

Explicitly the bracket before cosh is
n^(-3/2)[A(c_n)+O(1/n)]-exp(-x_n/2)/(n+1);
its error and subtracted term are each eventually smaller than
A_min n^(-3/2)/4. Both beta terms are still in the cosh. We need
no derivative estimate on the O term and no subsequence hypothesis.

Combining (15),(16), and c_n>=17/8-16/n, gives a fixed C_1>0 with

    exp(-x_n/4)|D_F(x_n)|
                  >=C_1 n^(-3/2)exp(n/64).              (17)

For example C_1=151 A_min/(320800 exp(2)) works. The exponent
comes from (c_n/8-1/4)n>=n/64-2.

The target-only defect D_star(x)=r g_n(y)exp(i z_star y)
-g_n(x)exp(i z_star x) satisfies, by the COMPLETE bound (4),

    exp(-x/4)|D_star(x)|
       <=2(n+2)[1+r exp((y-x)/4)]
       <=2(n+2)[1+2 exp(9/8)], c in J_n.                 (18)

Here |exp(i z_star t)|=exp(-t/8), y-x=2c, r<=2 and c<=9/4.
Finally D=D_star-D_F EXACTLY, so (17)-(18) prove (3), after
increasing the fixed onset and taking c=C_1/2. This is uniform in
every low order m; a positive exponential dominates the polynomial
bound in (18).

If m_n>=n/24 occurs infinitely often, (2) contradicts the
subexponential norm condition by taking epsilon=rho/2. Otherwise
m_n<n/24 eventually and (3) contradicts the requested weighted
defect decay. This proves the claimed dichotomy. The boundary
Delta is retained but cannot repair either failing necessary component
of the simultaneous criterion. No conclusion about arbitrary grid
measures, selected transfer or the original residual is drawn.

### Verification and limitations

The scalar margins are checked by
`python3 scripts/adaptive-slope/centered-taylor-band-checks-367.py`.
The certificate is
`scripts/adaptive-slope/centered-taylor-band-checks-367.json`.
All 21 checks pass; the complete /checks object was inspected with
`python3 ../scripts/loop/inspect_json.py scripts/adaptive-slope/centered-taylor-band-checks-367.json --pointer /checks --full`.
They support the displayed arithmetic; the coefficient identity is
proved algebraically in (7), not tested by this script. The checks
do not replace the uniform bulk input or the written all-n argument.
The whole-family optimization problem is still open, as are C997a(8),
selected/both-sign transfer, assay/reconstruction, complements and
regulators, L993, L984(H) and actual-Xi positivity.

### Independent conceptual audit — step369, 11 November 2026

RESEARCH / REPRODUCTION under the unchanged, separately source-approved
SPECIALIZE assessment
`drafts/literature/2026-11-11-centered-taylor-band-audit-review-367.md`.
The audit accepts the scoped dichotomy for every sufficiently large
integer n, uniformly over ALL integer 0<=m<=n. This establishes a
checked local input, not a new result beyond the sources compared, an
all-grid obstruction, or progress on actual-Xi positivity itself.
No claimed bound required repair. The following checks concern the
load-bearing argument, rather than only its scalar certificate.

**Complete kernel and imported bulk contract.** Finite variation and
compact time/frequency rectangles justify the interchange in each of
the TWO windows of C997c(1). Thus q uses the same F in both windows,
J'(x)=r q(rx)-q(x), and (5) follows with the retained constant Delta.
The integral of exp(u/4) gives exactly the factor 8 in that inequality.
Only C997q(1)-(2) are independently checked here; no audit of its other
conclusions is claimed. The real bound (4) retains K's -1 and both
terms in cosh, as required by the audited C997c contract.

For (6), set u=0 in C997e(4). Its two leading amplitudes are
(A(c)/2)exp(+/- i psi(c)); their sum after multiplication by
exp(+/- in phi(c)) is A(c)cos(n phi(c)+psi(c)). On real J both
exponentials have modulus one, so the two uniform O(1/n) amplitude
errors remain a uniform O(1/n) additive error in the bracket.
The C997e step329 conversion uses N=n+1, alpha=2 and Q(x)=x,
with the normalization and source references displayed above (6).
Thus there is no missing factor of n, 2, or (-1)^N. This reuses that
audited primary-source specialization; it does not reprove Vanlessen
or require a new source domain. The moving J_n stays INSIDE the same
fixed J, including its right endpoint. No error differentiation or
complex-contour estimate is needed for the peak argument.

**Original variation and the high-order branch.** Expanding (1-w)^k
before collecting equal frequencies yields (7). The finite-sum
identity used there follows from
(beta+1)_M/M!-(beta+1)_(M-1)/(M-1)!=(beta)_M/M!,
with initial value one. All alpha_n+j have positive real part.
The phase exp(-ij/2) has modulus one and the frequencies are distinct;
therefore (8) is the exact atomic TV, including all cancellations in
the polynomial expansion. In particular it is not an upper bound
obtained before collecting coefficients.

For 0<=j<=m<=n,
|alpha_n+j|<=sqrt((9n/2)^2+(n/2)^2)<5n, whereas every numerator
factor has modulus at least 7n/2. The remaining sum is
sum_j 1/[j!(m-j)!]=2^m/m!, giving (9). When m>=n/24 and n>=2,
integrality guarantees m>=1. The integral estimate for log(m!)
and the increasing function -1/4+s(log(7/s)+1), 0<s<=1,
then give (2) for all such indices, without an asymptotic Stirling
error. For the strict rho margin, the exponential-series tail gives
e<=5/2+2/9<11/4, and exp(3/50)<1/(1-3/50)=50/47.
The rational comparison in the certificate proves rho>1/400.

**Uniform low-order phase separation.** For n>=32768 and c in J_n,
the bounds in (10) apply simultaneously at x=cn and y=c(n+2).
The ratio of successive terms backwards is at most 250/651<1;
iterating it bounds the sum of every earlier term by the same
geometric tail, independently of m. Hence V_x and V_y lie in
the disk centered at 1 of radius 250/401, with modulus at least
151/401 and principal arguments of magnitude less than 7/10.
The m=0 case has V=1 and is included. Also each forward term
has modulus at least its predecessor, so |U_m|>=|U_0|=1.

The exact argument of w is vartheta/2-pi/2 in the stated interval.
Consequently the common eta_n and (alpha_n)_m cancel in F(y)/F(x),
and its phase modulo 2pi has the representative (13). Its carrier
part lies between 79/10 and 8, while the two principal V arguments
change it by less than 7/5. The resulting interval [13/2,47/5]
lies in [2pi+1/50,3pi-1/50], using 157/50<pi<22/7.
Thus |sin phase|>=sin(1/50)>1/100. This is a finite phase argument;
it assumes neither smooth phase tracking nor a zero-free Laguerre
interval. With e_y=F(y)/|F(y)|, taking the imaginary part after
multiplication by conjugate(e_y) annihilates r g_n(y)F(y), since
g_n(y) is real. The other term has magnitude
|g_n(x)F(x)|*|sin phase|. This proves (15), also at any zero of
either real kernel value, without dividing by g_n.

**Peak, complete subtraction and sequence quantifiers.** On J,
(phi')^2>=(15/68)>(2/5)^2 and psi'=(5/2)theta'>0.
The phase therefore increases by more than 32/5>2pi across the
length-16/n interval J_n. The intermediate value theorem gives
a point c_n where the cosine is exactly 1 for EVERY sufficiently
large n, not merely a subsequence. Its choice does not depend on m.
Uniformity in (6) bounds the bracket error by A_min/4 eventually.
Since x_n>=53n/25, exp(-x_n/2)/(n+1) is also at most
A_min*n^(-3/2)/4 eventually. The positive main bracket, followed
by cosh(3x_n/8)>=exp(3x_n/8)/2, implies (16), even with its
conservative constant A_min/8. Every onset here is independent of m.

The projection lower bound is at least
C_1*n^(-3/2)*exp(n/64), with the displayed positive C_1, because
x_n/8-n/4>=n/64-2. For the target term, exp(-t/8) times (4)
gives exactly (18), uniformly at both endpoints. Choose one further
fixed onset so that

    C_1*n^(-3/2)*exp(n/64)
            >=4(n+2)[1+2exp(9/8)].

This is possible since its exponential growth dominates the polynomial.
Then |D_star-D_F|>=|D_F|-|D_star| proves (3) with c=C_1/2.
The target was subtracted BEFORE concluding a lower bound for D.

If high orders occur infinitely often, their TV lower bound divided
by exp((rho/2)n) tends to infinity on that subsequence. This contradicts
even the epsilon=rho/2 instance of the all-epsilon subexponential
requirement. Otherwise the low-order defect lower bound eventually
holds at every index and its ratio to exp(-n/64) tends to infinity.
These cases exhaust arbitrary mixed sequences m_n. Delta remains
unestimated and cannot repair failure of this simultaneous sufficient
criterion; no converse to (5) is asserted.

Replayed the unchanged exact-arithmetic script and inspected the
COMPLETE `/checks` object of its disk certificate: 21/21 comparisons
passed, with no failures. The certificate supplies scalar margins only;
the algebra, uniform source specialization, phase projection, peak and
complete subtraction above supply the proof audit. The onset remains
existential. DAG inputs remain C997c, C997e and C997q, with the latter
used only for the directly checked definitions and (1)-(2). Other
packet stops are comparisons, not mathematical premises. General band
duals, original residual bounds and the independent transfer/positivity
gaps remain open. No new lemma or mathematical script was created.

## Mathlib

Full matching coverage is unchecked and unknown. No formal theorem
identifier has been verified for this grid-coefficient, phase-separation
and Laguerre-bulk combination. The named binomial and bulk sources
above are mathematical inputs, not claims of Mathlib coverage.
