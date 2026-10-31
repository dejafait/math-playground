# L527 — Common-pole generic prime increment

## Hypotheses

Use exactly L526's normalized real even bump h, Fourier convention
`H(t)=integral h(x)exp(-itx)dx`, measure `dm=dt/(2pi)`, primes p,
`L=log p`, `r=p^(-1/2)`, common `M=L+2`, actual sets P_-/P_+,
two-packet test `f_p(x)=h(x+L/2)+h(x-L/2)` and corrected symbols
u_-/u_+. In particular, the pole phase is identical on the two sides.
Write Pi for the physical positive-half-line projection and J_-/J_+
for the corresponding involutions. Their Fourier representations are
`g(t) -> u_+/-(-t)g(-t)`. Let S_-/S_+ be L526's Sonin projections.

The standard inputs are imported in these precise scopes:

* P. R. Halmos, *Two subspaces*, Trans. AMS 144 (1969), 381--389,
  [p.381 and Theorem 2, pp.384--385](https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf):
  split the four range/kernel intersections before using the generic
  two-projection block. No generic-position hypothesis on the whole
  space is made.
* bramble_trace, *Sharp Schatten asymptotics and Sonin trace
  localization for semilocal Fourier cutoffs*,
  [paper 2 v2, 16 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/2):
  Lemma 4.1 and (4.2)--(4.4) give localized Hardy trace finiteness;
  (5.2)--(5.4) give the phase derivative, its second-derivative bound
  and its compact-uniform PNT asymptotic; (7.1),(7.3) specify the pole
  phase. Only these stated inputs are used, not a moving-test version
  of a fixed-test trace asymptotic. These source proofs remain
  independently unaudited.
* Jordan Bell, *Trace class operators and Hilbert--Schmidt operators*,
  [18 April 2016, Theorems 15, 18, 23 and 25](https://jordanbell.info/LaTeX/mathematics/traceclass/):
  Hilbert--Schmidt products, ideal bounds and trace cyclicity, including
  the two-Hilbert--Schmidt-factor identity in Theorem 23's proof.
* Gerald Teschl, *Mathematical Methods in Quantum Mechanics*,
  [author's posted GSM 99 edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
  Theorems 3.1/3.7, (3.52), printed pp.90--91,96--97, and Theorem
  5.1, pp.123--124: bounded Borel spectral calculus, self-adjoint
  spectral measures, unitary transport including domains, and the
  generated unitary group. No convergence of moving projections is
  imported. Plancherel and Riemann--Lebesgue are used in their
  standard forms.

L526 supplies its separately finite Sonin traces and
`Delta_p=O_h(r L^(9/10))`. Its upstream-source qualification remains.
No RH, nullvector, full-Weil identification for these partial prime
sets, simplicity, or trace-vanishing hypothesis is assumed.
The local argument and complete coefficient certificate passed a
separate conceptual audit on 30 October 2026. This is reproduction
and validation of this existing claim, not an audit of its upstream
source manuscripts or a new increment mechanism.

## Conclusion

For each p, the operators and smoothed traces

    C_+/- = Pi J_+/- Pi J_+/- Pi - S_+/-,
    Q_+/-(f_p) = Tr(T_(f_p) C_+/- T_(f_p)^*),
    Gamma_p = Q_+(f_p)-Q_-(f_p)

are well defined, with C_+/- positive and Q_+/- finite. Put

    K(t)=(e exp(2it)-1)/(1+2it),
    c_h=integral |H(t)|^2 Re(K(t)/|K(t)|) dm(t).

Then, as p tends through primes,

    Gamma_p/(rL) -> -1-(4/pi)c_h.                       (1)

The exact interval certificate below proves the conservative bounds

    0.1511 < c_h < 0.2343 < pi/4,
    -1.299 < -1-(4/pi)c_h < -1.192.                     (2)

Thus this generic contribution is negative to leading order, but its
magnitude is strictly smaller than the required 2rL. Its addition to
L526's subleading Sonin increment still does not absorb that decrement.
This stops only the prescribed local generic-plus-Sonin mechanism.
The negative overlap/remainder and a collective signed comparison
have not been estimated. This is neither Weil positivity nor RH.

## Proof

### 1. Projection identification and both finite traces

Work in L^2(dm). Let E and P=I-E be the lower- and upper-half-plane
Hardy projections, respectively. Equivalently they are the negative
and positive spectral projections of D=-i d/dt. The Fourier transform
of the physical positive-half-line space is ran(E). Let R_0 denote
reflection in t in this paragraph only. Since u(-t)=bar u(t),

    J=M_(bar u) R_0,
    J E J=M_(bar u) P M_u,
    A=E J E J E=E M_(bar u) P M_u E.                    (3)

The intersection ran(E) intersect ran(J E J) consists precisely of
`g in H_-` with `u g in H_+`, so its projection is L526's S.
Halmos's decomposition makes A-S zero on the four intersection
summands and the positive squared-cosine block on the E part of
the generic summand. In particular, `0<=A-S<=A`. One can also
check positivity directly: A is positive, AS=SA=S, and its
restriction to the orthogonal complement of ran(S) is positive.

Write v=bar u. The smoothed full trace is

    N(u)=Tr(M_F A M_F^*)=||M_F E M_v P||_HS^2,           (4)
    F=2H cos(Lt/2),  W=|F|^2=|H|^2(2+2cos(Lt)).

Here the symbol in source Lemma 4.1 is v, not u: its Q is E
and its Pi is P. The change from dt to dm is a constant unitary
renormalization of L^2; the density integral is written using dm.
There is no additional reflection in (4); F is even in any case.

For each finite p the symbol is smooth and unimodular. The gamma
phase derivative grows logarithmically, its next derivative is
bounded, and higher symbol derivatives grow at most polynomially.
Each finite Euler factor has a nonvanishing denominator on the real
axis and bounded derivatives of every order. The pole phase has
bounded derivatives of positive order, since its v-integrals are
over [0,M]; at zero the sine quotient has its smooth extension.
Thus v satisfies all the hypotheses of source Lemma 4.1. Its phase
derivative has polynomial growth, so its positive/negative parts
are integrable against the Schwartz weight W. The lemma proves
(4) finite separately for P_- and P_+. Constants at this stage
may depend on p. No uniform error from that lemma is subtracted.

L526 proves `||M_F S||_HS^2` finite on each side. Therefore the
positive sandwiched operator for A-S is trace class and

    Gamma_p=N(u_+)-N(u_-)-Delta_p.                       (5)

Only these finite traces are used below.

### 2. A correlated first-order band trace

In this section set `v=bar u_-`, `V=M_v P M_v^*`,
`R=M_v^* E M_v`, and `Z=M_(exp(itL))`. Let B be the spectral
projection of D onto (0,L). Endpoints have Lebesgue measure zero.
The added conjugate Euler factor is the unitary multiplier

    a=(1-rZ^*)/(1-rZ),
    a=(1-r^2) sum_(n>=0) r^n Z^n-rZ^*.                 (6)

The series is absolutely convergent in operator norm. Directly in
the D spectral variable,

    [Z,P]=-BZ,  [Z^*,P]=Z^*B,
    [Z-Z^*,P]=-(BZ+Z^*B).                              (7)

We first give uniform localized trace-ideal bounds to justify using
(6). For an interval projection B_I of length |I| and any bounded
multiplier m, commuting M_F past E gives

    ||M_F E M_v M_m B_I||_HS
       <=||m||_infinity
          [(|I| integral |F|^2 dm)^(1/2)
            +||[M_F,E]||_HS].                          (8)

Indeed the term with E moved to the left is bounded by the
Hilbert--Schmidt norm of M_(Fvm) B_I; its squared norm is
`|I| integral |Fm|^2 dm`. The commutator term is bounded by
the ideal property. In the D spectral representation, integration
of the off-diagonal convolution kernel gives exactly

    ||[M_F,E]||_HS^2=integral |x| |f_p(x)|^2 dx<=L+2

for L>2; also `integral |F|^2 dm=2`. To see the identity, for a
fixed difference x the set of spectral pairs on opposite sides of
zero has length |x|. Plancherel then gives the displayed integral.
For F replaced by H this norm is at most one.

For n>=1, `[Z^n,P]` is minus a band of length nL followed by Z^n.
Sandwiching such a term times a bounded multiplier m between
`M_F E M_v` and its adjoint yields a trace-class operator of norm
at most `C_h(n+1)L ||m||_infinity`. Factor at the band and apply
(8) to both factors; the adjoint of the second factor has multiplier
`bar m Z^(-n)`, so the same estimate applies. The negative first
shift has the same bound.

Now `aPa^*-P=[a,P]a^*`. In (6) the commutator terms beyond
`r[Z-Z^*,P]` have coefficients whose (n+1)-weighted absolute sum
is O(r^2), uniformly for r<=1/2. Explicitly their coefficients are
`-r^3` at n=1 and `(1-r^2)r^n` for n>=2. The remaining multiplier
`a^*-I` has norm at most `2r/(1-r)`. Consequently the localized
series converges in trace norm, and

    N(u_+)-N(u_-)
       =-2r Re Tr(B Z R W R B)+O_h(r^2 L).              (9)

For clarity, the first linear term before cycling is
`Tr(M_F E M_v B Z M_v^* E M_F^*)`. Both factors split at B
are Hilbert--Schmidt by (8). Their trace-product identity puts
this equal to `Tr(B Z M_v^* E W E M_v B)=Tr(B Z R W R B)`.
The other term is its complex conjugate. The trace-norm convergent
remainder agrees with the bounded-operator expansion, so (9) does
not depend on interchanging unlocalized traces. All prime powers
in the added factor are included in (6) and its O(r^2 L) remainder.

### 3. Uniform Hardy selection on the moving band

Write `u_-(t)=exp(i phi_p(t))`, choosing a smooth real phase.
In this section put `R_p=sqrt(p)` and `a_p=phi_p'/R_p`.
The imported phase estimates and the explicit common pole give

    ||phi_p''||_infinity=O(R_p L),
    a_p(t)=4 Re(exp(itL)K(t))+o(1)                      (10)

uniformly on each fixed compact t interval. Indeed the finite-prime
part has leading term `-2R_p Re(exp(itL)/(1/2+it))`; omission of
the endpoint prime changes the derivative by O(rL). The pole
derivative has leading term `2e R_p Re(exp(it(L+2))/(1/2+it))`.
Its remaining terms and the gamma derivative are bounded on a
fixed compact interval after division by R_p. The second derivative
of the pole is bounded by `4 integral_0^(L+2) v cosh(v/2)dv`,
which has the stated order. This verifies both parts of (10)
without differentiating a PNT error.

Set `b_p(t)=1_(a_p(t)>0)`. We claim that

    sup_(|xi|<=2L)
    ||R(H exp(i xi t))-b_p H exp(i xi t)||_(L^2(dm))
        ->0.                                          (11)

Here is a direct proof, included because fixed-test asymptotics do
not justify this moving-family assertion. The self-adjoint operator

    A_p=M_(u_-) (D/R_p) M_(bar u_-)

is defined by unitary conjugation, and R is its negative spectral
projection. On the Schwartz test vectors used here it acts as
`D/R_p-a_p`. More precisely its domain is `M_(u_-) H^1(R)`.
For each p, phi_p' has polynomial growth and H is Schwartz, so
`bar u_- psi_xi` belongs to H^1, including every |xi|<=2L.
For `psi_xi=H exp(i xi t)`, its exact unitary group
and the fundamental theorem of calculus imply, for real s,

    ||exp(is A_p)psi_xi-exp(-is a_p)psi_xi||_2
       <= |s| ||psi_xi'||_2/R_p
            +s^2 ||phi_p''||_infinity ||psi_xi||_2/(2R_p^2)
       <= C_h (L/R_p)(|s|+s^2).                        (12)

In fact the group is `u_-(t)bar u_-(t+s/R_p)psi_xi(t+s/R_p)`.
The translation estimate accounts for the amplitude, while Taylor's
remainder accounts for the phase. The estimate is uniform in
`|xi|<=2L`, since `||psi_xi'||_2<=||H'||_2+2L||H||_2`.

For epsilon>0 define

    g_epsilon(x)=1/2-arctan(x/epsilon)/pi,
    m_epsilon(x)=epsilon^2/(epsilon^2+x^2).

The elementary identities

    arctan(x/epsilon)
        =integral_0^infinity exp(-epsilon s)sin(sx) ds/s,
    m_epsilon(x)
        =epsilon integral_0^infinity exp(-epsilon s)cos(sx) ds

follow by integrating the exponential integral (differentiate the
first identity in x and use its value at zero). Spectral calculus
and (12) therefore give, for fixed epsilon, uniformly in xi,

    ||[g_epsilon(A_p)-g_epsilon(-a_p)]psi_xi||_2=o(1),
    ||[m_epsilon(A_p)-m_epsilon(-a_p)]psi_xi||_2=o(1).   (13)

Their errors are bounded by a constant times
`(L/R_p)(epsilon^(-1)+epsilon^(-2))`. The first integral is
well defined on these domain vectors at zero; its difference is
absolutely dominated by (12). The exponential controls infinity.
Thus no operator-norm assertion about discontinuous spectral
projections is being assumed.

Pointwise on the real line, including zero,

    |1_(x<0)-g_epsilon(x)|^2<=m_epsilon(x).

The spectral theorem and (13) consequently bound the limsup of
the error in (11) by a constant times the square root of

    limsup_p integral |H(t)|^2 m_epsilon(a_p(t)) dm(t). (14)

Explicitly, the squared norm of `(R-g_epsilon(A_p))psi_xi`
is at most `<psi_xi,m_epsilon(A_p)psi_xi>`. By (13) this is
the displayed integral plus o(1), uniformly in xi. The multiplier
error `(g_epsilon(-a_p)-b_p)psi_xi` has the same integral bound.
The triangle inequality and (13) give the asserted limsup bound.
This also covers spectral zero; no spectral gap is assumed.

This expression tends to zero as epsilon decreases to zero.
To check the discontinuity explicitly, write `K=|K|exp(i alpha)`
with a smooth real alpha. K never vanishes because e>1, and
`|alpha'|<=26/5`. On a fixed compact interval |K| has a positive
minimum. By (10), the set `|a_p|<=eta` is, eventually, contained
in `|cos(Lt+alpha(t))|<=C eta`. The map `t -> Lt+alpha(t)`
has derivative between `L-26/5` and `L+26/5`. On that interval
the measure of this set is O(eta)+O(1/L). Thus its |H|^2 mass
has the same bound. Outside it `m_epsilon(a_p)<=epsilon^2/eta^2`.
First take p to infinity, then epsilon to zero with eta=sqrt(epsilon).
Finally remove the compact interval using the integrability of
|H|^2 and `0<=m_epsilon<=1`. This proves (14) tends to zero,
and hence proves (11), uniformly over the required moving band.

### 4. Evaluating the signed band trace

Put `D_L=2+Z+Z^*`, so W=M_(bar H) D_L M_H and ||D_L||<=4.
Multiplication by H commutes with the phase u_-, whence

    ||[R,M_H]||_HS=||[E,M_H]||_HS<=1.                 (15)

Only H is commuted at this fixed cost, not the whole moving F.
Writing the trace in (9) as a Hilbert--Schmidt inner product gives

    Tr(B Z R W R B)
       =<M_H R Z^*B, D_L M_H R B>_HS
       =<R M_H Z^*B, D_L R M_H B>_HS+O_h(sqrt(L)).    (16)

Indeed each commutator error has Hilbert--Schmidt norm at most
one, and each other factor has norm at most sqrt(L)+1, by (15)
and `||M_H B||_HS=sqrt(L)||H||_2=sqrt(L)`.

The unitary D spectral transform uses measure dxi and inverse
kernel exp(i xi t). Since M_H B is Hilbert--Schmidt, its columns
are `H exp(i xi t)`, 0<xi<L. Thus the last inner product in (16)
equals the absolutely convergent integral

    integral_0^L
      <R(H exp(i(xi-L)t)), D_L R(H exp(i xi t))>_2 dxi.

Use (11) on both vectors. Their norms are at most one and D_L
has norm at most four, so the total error is o(L), uniformly.
It follows that

    L^(-1) Tr(B Z R W R B)
       =integral |H(t)|^2 b_p(t)
                     [1+2exp(itL)+exp(2itL)] dm(t)+o(1). (17)

The turning-set estimate used for (14) permits replacement of b_p
by `1_(cos(Lt+alpha(t))>0)` in (17), with error o(1). The factors
in square brackets are uniformly bounded, and |H|^2 controls tails.
Periodic averaging, or trigonometric approximation followed by
Riemann--Lebesgue, now applies. At its jump points the same
turning-set bound justifies the approximation. The real one-period
average, for fixed alpha, is exactly

    mean_theta 1_(cos(theta+alpha)>0)
                    [1+2cos(theta)+cos(2theta)]
       =1/2+(2/pi)cos(alpha).                          (18)

The second harmonic integrates to zero over the half-period, and
the first harmonic integrates to cos(alpha)/pi. Therefore the
real part of (17) tends to `1/2+(2/pi)c_h`. Equations (9) and
(5), together with `r->0` and L526's `Delta_p=o(rL)`, prove (1).

For the averaging step, smooth the periodic half-circle indicator
only where |cos(theta)|<=eta and keep it between zero and one.
The turning-set estimate bounds the error on each compact interval
by O(eta)+O(1/L). Uniform trigonometric approximation of the smoothed
function then reduces the integral to terms with phase (k+j)Lt,
j=0,1,2, and integrable amplitude |H|^2 exp(ik alpha(t)).
Riemann--Lebesgue removes exactly the terms k+j!=0; the others
give the corresponding one-period mean. Take p to infinity before
removing the approximation and eta, and then remove the compact
interval using the |H|^2 tail. This checks the moving phase and
discontinuity without a uniform pointwise Fourier-series assertion.

### 5. Exact enclosure of the fixed coefficient

This is a rigorous bounded integral computation, not a numerical
assumption about primes or zeros. The complete reproducible artifacts
are `scripts/common-pole-generic/coefficient_certificate.py` and
`scripts/common-pole-generic/coefficient-certificate.json`. Run

    python3 scripts/common-pole-generic/coefficient_certificate.py

The JSON retains every quadrature-node enclosure, the elementary
enclosures, all discretization/tail bounds and the strict comparison.
Its calculation and decisions use only exact integer arithmetic.
All interval endpoints are integers divided by 10^40; products and
quotients round outward by integer floor/ceiling, and square roots
use integer square root with an outward upper endpoint. Exponentials,
sines, cosines and arctangents use alternating Taylor remainders.
For exp(-y) reduce to 0<=y<=1/8 and square back; for sine/cosine
reduce to [0,1/8] and use double-angle identities. Machin's identity
`pi=16 arctan(1/5)-4 arctan(1/239)` supplies the pi enclosure.
The series degrees and the following global error bounds are
explicit in the script; it uses no floating-point library estimates.

Here are the error bounds, so the certificate is mathematically
interpretable. Write

    b(x)=exp(-1/(1-x^2))  (|x|<1), zero otherwise,
    I=integral b(x)^2 dx,
    B(t)=integral b(x)cos(tx)dx, H=B/sqrt(I),
    c(t)=Re(K(t)/|K(t)|).

These are even functions where applicable, and
`c_h=(pi I)^(-1) integral_0^infinity B(t)^2 c(t)dt`.
With y=1/(1-x^2), differentiating b and using e>8/3 gives

    |b|<=3/8, |b'|<=9/8, |b''|<=33,
    |(b^2)''|<=873/32, ||b'||_2^2<=81/32.             (19)

For example `|b''|<=(4y^4+8y^3+2y^2)exp(-y)`. Each
`y^j exp(-y)` is at most `j^j exp(-j)` for y>=1; substitution
of e>8/3 bounds the sum by 32.765625<33. The bounds extend
through +/-1 by smoothness and vanishing of all bump derivatives.

For 0<=t<=T=32, the second x derivative of b(x)cos(tx) is
bounded by `33+(9/4)T+(3/8)T^2=489`. Composite midpoint
quadrature on [-1,1] with n_x=512 therefore has errors at most

    E_B=489/(3 n_x^2),  E_I=873/(96 n_x^2).            (20)

The rule's error bound is `length^3 sup|second derivative|/(24 n^2)`;
it follows by integrating the second-order Taylor remainder on each
cell. Symmetry reduces storage to its positive-half nodes.

For the outer quadrature, the smooth argument alpha of K satisfies

    |alpha'|<=26/5, |alpha''|<=171/25,
    |c'|<=26/5, |c''|<=847/25.                        (21)

Indeed the numerator contributes at most `2e/(e-1)<=16/5`
to |alpha'|, and the denominator contributes at most 2. For the
second derivative their bounds are `4e/(e-1)^2<=96/25` and
`sup 16|t|/(1+4t^2)^2<3`. This proves (21). Also
`|B|<=3/4`, `|B'|<=3/8`, `|B''|<=1/4`. Consequently

    |(B^2 c)''|
      <=2[(3/8)^2+(3/4)(1/4)]
          +4(3/4)(3/8)(26/5)+(3/4)^2(847/25)<26.

With n_t=2048 on [0,32], the outer midpoint error is at most
`26 T^3/(24 n_t^2)`. Each B value is enclosed with (20) before
squaring; no point evaluation is treated as exact. Finally,
Plancherel and (19) bound the normalized omitted tail by

    (pi I)^(-1) integral_T^infinity B(t)^2 dt
       <= ||b'||_2^2/(T^2 I)<=81/(32 T^2 I).           (22)

Both signs of that tail are included since |c(t)|<=1. The
normalization I has its own strictly positive interval enclosure.
Using

    c(t)=[e cos(2t)-1+2t e sin(2t)]
          /sqrt((1+4t^2)(e^2+1-2e cos(2t)))

the certificate encloses c_h between
`0.1511396475182945214093713962228826098284` and
`0.2342725848138675893829464080374919436350`.
The lower enclosure of pi/4 is
`0.7853981633974483096156608458198757210391`.
The coefficient in (1) is enclosed between
`-1.2982851192323385571256392174555451583114` and
`-1.1924369759976262773504415910713899679588`.
These outward bounds imply (2) with ample strict margin.
They decide only this auxiliary coefficient; the analytic limit
was proved in Sections 2--4, not inferred from the computation.

The separate audit replayed the generator and checked its complete
integer-interval implementation. At each outer node the angle seed
is t/n_x; the recurrence with step 2t/n_x encloses cos(t x_i) for
every positive midpoint x_i=(2i+1)/n_x. All these nodes, the factor
2 for reflection, and the width 2/n_x enter both inner sums.
The reduced Taylor series have decreasing alternating terms;
their first omitted terms bound the remainders. Range reduction,
double-angle steps and outward squaring preserve enclosure even
when interval endpoints are dependent. Clipping uses only the
known ranges of exp(-y), sine, cosine and c. The square-root and
positive-denominator checks use exact integers, including when
the Fourier interval crosses zero. No endpoint display is used
as a substitute for its rational value.

Run the complementary full-data audit with

    python3 scripts/common-pole-generic/coefficient_audit.py

Its `scripts/common-pole-generic/coefficient-audit.json` records
the generator/certificate hashes and checks all 8,459 interval
records, all 256 bump nodes and all 2,048 outer nodes. Using exact
Fraction arithmetic independent of the generator's interval class,
it checks every saved signed product, the normalization and full sum,
the rational quadrature/tail assembly and final strict comparison:
33,846 checks, no failures. This verifies the stored arithmetic
assembly after full replay; elementary-function validity and the
operator limit rest on the mathematical arguments above, not the
audit program's passed flag.

L526's added arithmetic term is exactly -2rL for L>2: its
autocorrelation is one at L, zero at every kL for k>=2, and zero
at the padded endpoints +/-M. The same M is used here, so no
pole increment is present. Thus (1)--(2) are a contrary asymptotic
for the specified test. Other cells/tests, full-Weil identification,
negative overlap and off-diagonal remainder, missing visible primes,
L522's nullvector/trace/nonresonance premises, family bounds and Xi
transfer remain unresolved. No effective onset is provided.

## Mathlib

Full matching coverage is not checked. No Mathlib theorem is claimed
for the moving Hardy selector, the correlated generic increment or
the certificate. The cited projection and trace-ideal theorems are
standard imported inputs; the changed-family argument is the local
extension developed here under the pre-existing EXPLORE assessment.
The scoped search did not establish a matching result, but does not
certify originality. The separate conceptual audit validated the
local proof and certificate, including its moving-family limits;
the upstream source-proof qualifications remain unchanged. Neither
this audit nor its rational-arithmetic checks provide a formalization.
