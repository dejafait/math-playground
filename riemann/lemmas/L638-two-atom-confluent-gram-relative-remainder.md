# Lemma 638: two-atom confluent Gram-relative complete remainder

## Hypotheses

Use exactly w,T,X,L,Z,W,M of L637, including the complete six-term
expression (18)--(19), its exact analytic phase, and its curvature
convention. Thus w>=0 is fixed in C_c^infinity((0,1)), integral w=1,
L=log T, T<=X<=2T and w_XT(t)=w((t-X)/T). For real
0<|h|<=1/2 and arbitrary complex c0,c1 put

    mu=c0 delta_0+c1(delta_h-delta_0)/h,
    U(t)=c0 Z(t)+c1[Z(t+h/L)-Z(t)]/h,
    G(mu)=integral w_XT |U|^2,
    E(mu)=integral w_XT W |U|^2-M(mu),
    |c|^2=|c0|^2+|c1|^2.

The parameters h,c0,c1 may depend arbitrarily on T,X; no lower bound
on |h| is imposed. This is only a two-dimensional family, without an
amplifier. Import L637 (20)'s holomorphic fourth-moment remainder and
L622's analytic-phase and zero-safe curvature identities, using L465's
gamma estimates. Their underlying Hughes--Young theorem is a named
import, not a source proof audited here.

For the second moment import Sandro Bettin, *The second moment of the
Riemann zeta function with unbounded shifts*, Int. J. Number Theory 6
(2010), 1933--1944, [arXiv:1111.0925v1, Theorem 1, p. 2, with the
small-shift proof cases pp. 9--10](https://arxiv.org/pdf/1111.0925v1#page=2),
DOI 10.1142/S1793042110003861. Its primitive for fixed complex a,b,
c=a-b, is the integral of

    zeta(1+c)+zeta(1-c) chi(1/2+a+it)chi(1/2-b-it),

with error O((sqrt(Y)+sqrt(|Im a|)+sqrt(|Im b|))log^2 Y),
under Re a,Re b=O(1/log Y); at c=0 use the limit of the full bracket.
Only |a|,|b|<=C/log T and Y comparable to T are used. This is the
same import and Hardy conversion as L473 Section 1; the changed smooth
window and coalescing observer require the specialization below.

The divided-difference identity used below is the first-order case of
Hartmann--Lesch, *Divided differences and multivariate holomorphic
calculus*, [DOI 10.4171/DM/1060, Appendix A.2, (A.5)--(A.8),
pp. 20--21](https://ems.press/content/serial-article-files/52597).
Only a segment contained in an open holomorphy domain is needed. Its
first-order formula is displayed to fix normalization, not reprove a
general calculus. Source coverage for this exact test was approved in
drafts/literature/2026-11-01-hardy-two-atom-confluent-error-test.md.

## Conclusion

There are C_w and an existential onset, independent of h,c,T,X, such
that

    G(mu)>= (T L/32)|c|^2,                                  (1)
    |E(mu)|<=C_w |c|^2 [T^(19/25)L^2+T^(-1)L^4].            (2)

Consequently, with a possibly enlarged constant,

    |E(mu)|<=eta(T) L^5 G(mu),
    eta(T)=C_w[T^(-6/25)L^(-4)+T^(-2)L^(-2)] ->0.           (3)

The complete M is unchanged. This is a fixed-dimensional specialization
of imported moment estimates, not a new arithmetic moment theorem or
an RH solution. It removes inverse separation losses for this family;
no uniformity in derivative order or atom count follows. Realization,
signed approximation and a useful main-term margin remain open. The
separate conceptual application audit below passed on 1 November 2026,
under the named imports, without changing a hypothesis or bound.

## Proof

### 1. Smooth-window analytic second moment

For independent complex r,s in a fixed bounded neighborhood, set

    B(r,s)=integral w_XT(t) Z(t+r/L)Z(t+s/L) dt,
    a=ir/L, b=is/L, c=a-b=i(r-s)/L,
    g(t)=exp(i[theta(t+r/L)-theta(t+s/L)]).

The exact functional-equation conversion in L473 gives the product
as g times the zeta product in Bettin, and the chi product as g^(-2).
The phase bounds from L622 imply |g|=O(1), g'=O(1/(TL)) on [T,3T],
uniformly on these complex sets. The physical a,b and L are fixed at
every primitive endpoint Y, with log Y=L+O(1). Subtract Bettin's
primitive at T; its residual R(Y) on [T,3T] is uniformly
O(sqrt(T)L^2). Partial integration with p(t)=w_XT(t)g(t) gives

    integral_X^(X+T) p(t) dR(t)=-integral_X^(X+T) p'(t)R(t) dt.

The boundary terms vanish since w has compact support in (0,1).
Also integral |p'|=O(1), by the w'/T term and the displayed g' bound.
Thus the residual is O(sqrt(T)L^2). This does not differentiate a
pointwise error, and is uniform in X.

Write lambda_t=log(t/(2pi)). L637's phase/gamma scope gives
theta'(t)=lambda_t/2+O(1/T), theta''(t+z/L)=O(1/T) on fixed complex
shift sets. Integrating along the segment from t+s/L to t+r/L yields

    g(t)=exp(c lambda_t/2)+c O(1/T),

uniformly; the error is holomorphic and divisible by c, since it
vanishes on r=s. In particular its quotient is bounded through
coincidence. Write zeta(1+c)=1/c+j(c), where j is bounded holomorphic
near zero. The combined weighted main bracket is

    g zeta(1+c)+g^(-1)zeta(1-c)
      =(g-g^(-1))/c+g j(c)+g^(-1)j(-c)
      =2 sinh(c lambda_t/2)/c+O(1).

No separate singular pole is bounded at c=0. Replacing lambda_t by L
costs O(1): its derivative in lambda is cosh(c lambda/2)=O(1), and
lambda_t-L=O(1). Therefore, with

    k(d)=integral_(-1/2)^(1/2) exp(i d u) du,

the main bracket is L k(r-s)+O(1). Since integral w_XT=T,

    B(r,s)=T L k(r-s)+R2(r,s),    sup |R2|<=C_w T.         (4)

Here sqrt(T)L^2=O(T). Both B and the right main term are holomorphic
in r,s on a neighborhood of, for example, |r|,|s|<=1. For B this
follows from compact t support, local holomorphy of Z, and compact
integrand bounds. The error bound in (4) holds on a larger fixed
neighborhood as needed; its Cauchy derivatives of each fixed order
are also O(T) on smaller polydiscs.

### 2. Uniform actual complex Gram coercivity

For any holomorphic f of one observer variable write

    D_h f=[f(h)-f(0)]/h=integral_0^1 f'(tau h) d tau,
    Lambda_c f=c0 f(0)+c1 D_h f.

Both observer variables have independent copies of this operator;
use conjugate coefficients in the second variable. The nodes and
segments lie in [-1/2,1/2]. Cauchy on radius-1/4 circles about those
segments bounds each of R2, D_h^(r)R2, D_h^(s)R2,
D_h^(r)D_h^(s)R2 by C_w T, uniformly as h tends to zero. Applying
the operators to (4) thus gives

    G(mu)=T L B_h(c)+O_w(T |c|^2),
    B_h(c)=integral_(-1/2)^(1/2)
                   |c0+c1(exp(i h u)-1)/h|^2 du.          (5)

The conjugate orientation follows from k(r-s), and (5) includes
arbitrary complex cross terms, not just real coefficients.

For real x, |exp(ix)-1-ix|<=x^2/2, by the integral Taylor remainder.
Consequently the L2(du) distance between (exp(i h u)-1)/h and i u is
at most

    |h|/(2 sqrt(80))<=1/(4 sqrt(80))<1/32.

The functions 1 and i u are orthogonal in the complex Hilbert space,
with squared norms 1 and 1/12. The triangle inequality now yields

    sqrt(B_h(c))
      >=sqrt(|c0|^2+|c1|^2/12)-|c1|/32
      >=(1/sqrt(12)-1/32)|c|
      >(2/7-1/32)|c|>|c|/4.

This also holds in the confluent limit, though no value h=0 was
assumed. Equation (5) gives (1) beyond one uniform onset.

### 3. Complete fourth-moment remainder before curvature

Denote L637 (20)'s holomorphic error by R4(b), to distinguish it
from E(mu):

    F(b)=integral w_XT product_(j=1)^4 Z(t+bj/L) dt
        =T L^4 H(b)+R4(b),
    sup_(|bj|<=2)|R4(b)|<=C_w T^(19/25).

H is exactly L637 (19); retain all six terms and the exact phase.
Let Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2.
Apply Q at b1=b2=0, then Lambda_c in b3 and Lambda_conjugate(c)
in b4. For a,b in {0,1}, Cauchy on radius-one circles in the first
two variables and radius-1/2 circles centered on the two real
observer segments gives

    |partial_3^a partial_4^b Q R4(0,0,x,y)|
       <=3*2^(a+b) C_w T^(19/25),  |x|,|y|<=1/2.

All circles lie inside the given polydisc. The factor 3 includes
the two 2! derivatives with their halves. Integrating the first
derivatives along the two segments, before taking absolute values,
therefore bounds the contracted error by

    3 C_w T^(19/25)(|c0|+2|c1|)^2
       <=15 C_w T^(19/25)|c|^2.                           (6)

Differentiating the compact integral is legitimate by holomorphy.
The exact identity is

    L^2 Re[Lambda_c^(3) Lambda_conjugate(c)^(4) Q F]_(b1=b2=0)
       =integral w_XT (Z'^2-ZZ'') |U|^2.

Contracting T L^4 H gives precisely M(mu), since Lambda represents
the original two atomic coefficients even when those are large.
Thus (6) contributes at most C_w |c|^2 T^(19/25)L^2, without a
TV factor or inverse power of h.

### 4. Complex shifted fourth moments and full curvature

We need an absolute L4 bound also on complex circles; the real-node
TV curvature bound alone would be insufficient. First show

    sup_(|bj|<=1)|H(b)|<=C_w.                             (7)

On the product circles |bj|=rho_j with
(rho_1,rho_2,rho_3,rho_4)=(1,5/4,3/2,7/4), every pair of distinct
bj has distance at least 1/4. In each of L637 (18)'s six R terms,
the four polar arguments are 1 plus signed i(bj-bk)/L, with j!=k.
Thus each zeta factor is O(L) there by its Laurent expansion; the
reciprocal zeta denominator has argument 2+O(1/L) and is bounded.
The exponential swaps and Phi are O(1), uniformly for t in [T,3T].
It follows that the full S is O(L^4) on these product circles, and
its defining integral makes H=O(1). The complete sum H is holomorphic
on the polydisc by the imported holomorphy theorem. Iterated maximum
modulus on these four discs proves (7) on |bj|<=1. No bound on
separate pole terms at interior collisions has been used.

It follows from (7) and the R4 estimate that |F(b)|<=C_w T L^4
there. The analytic Hardy function is real on the real interval;
Schwarz reflection on its symmetric neighborhood gives
Z(t+conjugate(z)/L)=conjugate(Z(t+z/L)). Inserting
b=(z,conjugate(z),z,conjugate(z)) therefore proves

    integral w_XT |Z(t+z/L)|^4 dt<=C_w T L^4, |z|<=1.    (8)

For real |x|<=1/2, Cauchy's integral formula on the scaled-variable
circle |z-x|=1/4, followed by Minkowski in L4(w_XT dt), gives

    ||Z'(t+x/L)/L||_4<=4 sup_(|z-x|=1/4)||Z(t+z/L)||_4
                      <=C_w (T L^4)^(1/4).

The integral segment formula for the difference observer then yields

    ||[Z(t+h/L)-Z(t)]/h||_4<=C_w(T L^4)^(1/4),
    ||U||_4<=C_w |c| (T L^4)^(1/4).                       (9)

All integrations are over compact parameter sets with bounded
integrands for each T, so the Cauchy and Minkowski interchanges are
valid. Constants in (8)--(9) are uniform in h,X.

Finally L622's zero-safe identity and L465's gamma bound give

    W=Z'^2-ZZ''-(log A)''Z^2,    |(log A)''|<=C T^(-2).

Weighted Holder, (8) at z=0 and (9), bound the entire curvature
contribution by

    C T^(-2) ||Z||_4^2 ||U||_4^2
       <=C_w |c|^2 T^(-1)L^4.                            (10)

Together (6) and (10) prove (2), with the actual W and exact M.
Dividing by L^5 times (1) gives (3). If c=0 all quantities vanish;
otherwise (1) justifies the division. There is no assumption on
zeros, simplicity, spacing or initial signs anywhere in this proof.

### 5. Separate conceptual application audit — 1 November 2026

The audit reused the unchanged approved assessment, read Sections 1--4
in full and checked the used passages of L637, L622, L465 and L473.
The Bettin and Hughes--Young theorems and complete-sum holomorphy remain
named imports. This verifies this local specialization, not those
manuscripts, a new arithmetic theorem, or any larger observer family.

**Second moment, endpoints and the removable pole.** Keep
a=ir/L and b=is/L fixed while the primitive endpoint Y varies over
[T,3T]; log Y=L+O(1) preserves Bettin's small-real-part hypotheses
uniformly. If R(Y) is the primitive error after subtraction at T,
then sup |R(Y)|<=C sqrt(T)L^2. With p=w_XT g, the support of w
makes both endpoint values of p zero, and

    integral |p'| dt
      <= ||w'||_1 sup |g|+T ||w||_1 sup |g'|=O_w(1).

Integration by parts therefore uses only the primitive bound, never
a differentiated asymptotic error. All t in the support lie in [T,3T]
for every allowed X. The exact Hardy conversion fixes the sign of g
and of the difference r-s.

On a larger fixed complex shift set the segment formula gives

    i[theta(t+r/L)-theta(t+s/L)]
      =c [lambda_t/2+e_t(r,s)],  |e_t(r,s)|<=C/T,

where e_t is holomorphic through r=s. Hence
g-exp(c lambda_t/2)=c O(1/T), with a uniformly bounded holomorphic
quotient, and the same assertion holds for g^(-1) with the opposite
exponent. Combining the two Laurent poles before taking a bound
leaves 2 sinh(c lambda_t/2)/c+O(1), also at c=0. Replacing lambda_t
by L costs O(1). The integrated O(T) error and primitive
O(sqrt(T)L^2) error are both O(T) at a uniform large-T onset.
Their sum R2 is holomorphic as the difference in (4). Cauchy therefore
controls its mixed derivatives on fixed smaller polydiscs; it does not
differentiate the source's big-O notation.

**Actual complex Gram and simultaneous coalescence.** For real h,
positive or negative, D_h f=integral_0^1 f'(tau h) d tau.
Apply it separately in r and s. Every pair of radius-1/4 Cauchy
circles about the segments stays in |r|,|s|<=3/4, where the preceding
uniform bounds apply. The two slot operations commute and their
mixed residual is O_w(T). Contracting all four entries costs at most
C_w T(|c0|+|c1|)^2<=2 C_w T|c|^2, independent of h.

The identity k(r-s)=integral exp(iru)exp(-isu)du shows that the
second slot carries conjugate coefficients and the conjugate Fourier
factor. Thus (5) is the actual |U|^2 Gram form even for complex c;
no real-coefficient reduction is made. Since integral u^4 du=1/80,
the Fourier-vector perturbation norm is at most
|h|/(2 sqrt(80))<=1/(4 sqrt(80))<1/32. The orthogonal reference
pair 1,iu has minimum squared norm 1/12. Moreover

    1/sqrt(12)>2/7,  2/7-1/32=57/224>1/4.

Consequently B_h(c)>=|c|^2/16. Writing the residual bound as
C_2 T|c|^2, the single threshold L>=32 C_2 proves (1). Neither the
onset nor its constant depends on how h or c varies with T or X.

**Fourth-moment extraction and all six pole configurations.** L637's
audit supplies holomorphy on |bj|<3 and a uniform source bound on
closed smaller polydiscs. In particular all the circles used in
Section 3 lie inside this domain. The three terms of Q have Cauchy
costs 1,2!/2,2!/2, totaling 3. An observer derivative costs 2 on
its radius-1/2 circle. Therefore the four entries after the two
segment integrations have bounds 3,6,6,12 times C_w T^(19/25).
Their contraction is bounded by
3 C_w T^(19/25)(|c0|+2|c1|)^2<=15 C_w T^(19/25)|c|^2.
This applies both divided differences before absolute values and
never incurs |h|^(-1) or |h|^(-2).

Direct differentiation of the compact Hardy product gives
L^2 QF=integral w_XT (Z'^2-ZZ'') Z_3 Z_4. The observer contraction
is exactly |U|^2. The same linear contraction of H is precisely
the atomic M of L637 (19); taking real parts is done after extraction.
No symmetry or positivity of an individual source term is presumed.

For the maximum-modulus argument in Section 4, the four polar offsets
of each successive R term in L637 (18), after removing the common
factor i/L, are as follows:

    first:  b1-b3, b1-b4, b2-b3, b2-b4
    second: b3-b1, b3-b2, b4-b1, b4-b2
    third:  b3-b1, b3-b4, b2-b1, b2-b4
    fourth: b4-b3, b4-b1, b2-b3, b2-b1
    fifth:  b1-b2, b1-b4, b3-b2, b3-b4
    sixth:  b1-b3, b1-b2, b4-b3, b4-b2.

All involve distinct indices. On the chosen product circles the
reverse triangle inequality bounds every difference below by 1/4;
the Laurent estimate for each polar factor is therefore O(L).
Each denominator is 2+O(1/L), where reciprocal zeta is uniformly
bounded, and every swap exponential and exact phase is O(1).
This bounds H on the product boundary of the polydisc with those
four radii. Iterated maximum modulus is applied to the holomorphic
complete H, not to its meromorphic summands, and proves (7) on
|bj|<=1, including all collisions.

**Absolute L4 and curvature, including zeros.** The analytic gauge
is nonzero on a symmetric neighborhood of [T,3T] and Z is real
on its real interval. Schwarz reflection there gives the conjugate
identity used in (8). The tuple (z,conjugate(z),z,conjugate(z))
lies in the closed unit polydisc and its Hardy product is |Z|^4;
combining (7) and the R4 bound yields (8) uniformly. Cauchy's
integral formula for f_t(z)=Z(t+z/L) on |z-x|=1/4 has L4 norm
cost 4. Minkowski is valid for the finite positive measure w_XT dt
and the compact circles; all integrands are bounded on these compact
sets for each T. A second Minkowski application on the real segment
proves (9), including negative h and arbitrary complex c.

Differentiating Xi=-AZ directly gives
W=Z'^2-ZZ''-(log A)''Z^2 with no division by Z. L465's paired
gamma cancellation, including the polynomial prefactor, supplies
the O(T^(-2)) bound on the whole support. Holder thus costs
T^(-2)(T L^4)^(1/2)|c|^2(T L^4)^(1/2), proving (10).
No zero simplicity or nonvanishing hypothesis has entered.

Finally L^5 G>=T L^6 |c|^2/32, so the two error ratios are exactly
O_w(T^(-6/25)L^(-4)) and O_w(T^(-2)L^(-2)). They tend to zero
uniformly. The zero vector is handled separately without division.
All stated constants and powers survive the audit. Higher derivative
orders, growing atom counts, realization and signed main-term margins
remain unproved by this result; no claim about them follows from the
uniformity in the single separation h.

## Mathlib

Matching coverage has not been checked. The arithmetic shifted-moment
theorems and full-sum holomorphy are the precise named imports above
and in L637/L622; no formalization is claimed. Cauchy estimates,
maximum modulus, Schwarz reflection, Minkowski, Holder and elementary
Hilbert-space inequalities are standard supporting results; their
normalizations and applications needed here are explicit in the proof.
