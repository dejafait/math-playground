# Lemma 500: weighted two-branch reduction and the unclosed correlations

## Hypotheses

Use the actual Riemann zeta function. Let T be sufficiently large and real,
and set

    L=log T, delta=log L/L, a=delta/2,
    U=N=3T, ell=log(3T), R=ell^2,
    X=T^(1/8), Y=T^(1/4), K=Y R.

All logarithms are natural. Index distinct nontrivial zeros by
rho=beta+i gamma with their full orders m_rho. Let

    S={rho: beta>1/2+a, T-2delta<=gamma<=2T+2delta},
    I_rho=[T,2T] intersect [gamma-2delta,gamma+2delta],
    E_rho=integral_(I_rho) |zeta(1/2+it)|^2 dt,
    n_delta(t)=sum_(rho in S) m_rho 1_{|gamma-t|<=2delta},
    W_delta=integral_T^(2T) |zeta(1/2+it)|^2 n_delta(t) dt.

No simplicity, ordinate separation, RH, external half-plane premise,
independence or zero-conditioned amplitude estimate is assumed.

The detector input is S. Baier, *On the p^lambda problem*, Acta Arith.
113 (2004), 77--101, Proposition 4, printed pp. 83--84,
[journal PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83115),
[arXiv:math/0512445v1, (16), (17), (22)](https://arxiv.org/html/math/0512445v1).
With M_X(s)=sum_(n<=X) mu(n)n^(-s) and
b_X(k)=sum_(d|k,d<=X) mu(d), put

    U_Gamma(rho)=|integral_(-R)^R zeta(1/2+i(gamma+v))
                   M_X(1/2+i(gamma+v))
                   Y^(1/2-beta+iv) Gamma(1/2-beta+iv) dv|,
    P_d(s)=sum_(X<k<=K) b_X(k) exp(-k/Y) k^(-d) k^(-s),
    U_P(rho)=|P_(beta-1/2)(1/2+i gamma)|.

The cited proposition gives max(U_Gamma,U_P)>1/2 at zeros with
beta>=1/2 and (log N)^2<gamma<=U, provided X,Y>=1,
log N, log U, log Y are comparable, and log X=O(log N).
We apply it only at beta>1/2+a, where its Gamma integral is regular.
Its proof is imported, not reproved or independently audited.

For the fallback only, use the restricted count theorem of L485 and
the continuous fourth moment Q_4(T)<=C_4 T L^4 from L471. L485
imports Maples--Rodgers, arXiv:1404.3080v2, Proposition 2.5 at
k=2,c=1/4 with its recorded restricted proof repairs. L471 imports
Bui--Hall, arXiv:2304.05178v1, Theorem 3 and Section 7 at derivative
orders (0,0,0,0). Their manuscript/arithmetic audit qualifications remain.
Neither is a weighted sampling theorem.

## Conclusion

The finite positive reduction is

    W_delta=sum_(rho in S) m_rho E_rho
      <=4 sum_(rho in S) m_rho E_rho
                                (U_Gamma(rho)^2+U_P(rho)^2).       (1)

Define the integrable positive envelope

    g_a(v)=(a^2+v^2)^(-1/2),                 |v|<=1,
    g_a(v)=exp(-pi|v|/2)|v|^(-1/2),          |v|>1,
    G_a=integral_R g_a(v) dv,
    R_Gamma=sum_(rho in S) m_rho E_rho
          integral_(-R)^R g_a(v)
                    |zeta M_X(1/2+i(gamma+v))|^2 dv,
    R_P=sum_(rho in S) m_rho E_rho
                         |P_(beta-1/2)(1/2+i gamma)|^2.

Here integral_R means integration over the whole real line; R as an
endpoint in (-R,R) is the positive number ell^2 defined above. There
is an absolute constant C such that

    W_delta <= C Y^(-delta) G_a R_Gamma + 4 R_P,                  (2)
    G_a=2 asinh(1/a)+2 integral_1^infinity exp(-pi v/2)v^(-1/2)dv
       =2 log L-2 log log L+O(1).                              (3)

Both R_Gamma and R_P are retained unknown correlations. In particular,
the desired estimate for some fixed c>0 would follow from the pair of
sufficient estimates

    R_Gamma <= C' T delta L^2 L^(1/4-c)/G_a,
    R_P     <= C' T delta L^2 L^(-c),                          (4)

with constants independent of T. Neither estimate in (4) is proved.
These are not necessary conditions on W_delta; a loose majorant can
fail even when the desired bound holds.

The unconditional count/moment fallback gives only

    W_delta <= C'' T delta L^3 exp(-delta L/16),
    W_delta/(T delta L^2) <= C'' L^(15/16).                     (5)

Its upper-bound certificate does not establish the required O(L^(-c)).
This is a known-tool specialization and a diagnosis of this detector
implementation, not a new density estimate, a lower bound on W_delta,
an impossibility theorem, an RH criterion or a solution. The local
derivation has not received a separate critical audit. The application
of Fazzari's polynomial tool fails to close (4) for the reasons below;
no new weighted theorem is silently inserted.

## Proof

### 1. Parameter and finite-window checks

For a common sufficiently large onset, 1/L<=delta<=1/8 and
T-2delta>ell^2, while 2T+2delta<3T. Thus every selected zero is in
the detector's height range. The logarithms of N,U,Y have fixed
positive comparability constants, and log X=(1/8)L=O(ell).
These constants do not vary with a or the particular zero. Also
0<beta-1/2<1/2 for the selected nontrivial zeros. The upper bound
1/2 here is strict, from the unconditional zero strip.

S is finite by isolatedness of zeta zeros in a compact neighborhood
of 0<=Re(s)<=1 and T-2delta<=Im(s)<=2T+2delta; the pole at s=1 is
outside that neighborhood. The critical-line integrands are continuous
on compact intervals. All sums in (1)--(2) are finite and all displayed
integrals are finite. An empty S or a singleton I_rho has zero weight.
Coincident ordinates do not identify distinct zeros.

Finite interchange proves W_delta=sum m_rho E_rho. Since one of the
two detector magnitudes exceeds 1/2 at every zero, one has
1<=4(U_Gamma^2+U_P^2). Multiply by m_rho E_rho>=0 and sum to obtain
(1). The detector need only hold once at the zero location; the same
inequality is valid for each of its m_rho copies. There is no thinning
or loss of multiplicity. A zero satisfying both alternatives causes no
problem in this positive majorant.

### 2. Gamma cost and the surviving two-height statistic

Write d=beta-1/2, so a<d<1/2. The classical Gamma recurrence gives

    Gamma(-d+iv)=Gamma(1-d+iv)/(-d+iv).

For |v|<=1 the numerator is uniformly bounded on the compact strip
1/2<=Re(z)<=1, |Im(z)|<=1. Hence
|Gamma(-d+iv)|<=C(a^2+v^2)^(-1/2). For |v|>1, the classical
Stirling estimate in a fixed vertical strip, with its remaining compact
part included in the constant, gives

    |Gamma(-d+iv)|<=C |v|^(-d-1/2) exp(-pi|v|/2)
                  <=C |v|^(-1/2) exp(-pi|v|/2).

Thus |Gamma(-d+iv)|<=C g_a(v), uniformly for the entire selected
range. This is the standard Gamma estimate used in the detector
method, with its near-line dependence made explicit, not a reproof of
Baier's detector. Integrating the first piece exactly gives (3); the
second piece has a finite constant integral. Substituting
a=log L/(2L) gives the last equality in (3).

Cauchy--Schwarz in the positive measure |Gamma(-d+iv)|dv yields

    U_Gamma(rho)^2
      <=Y^(-2d) (integral_(-R)^R |Gamma(-d+iv)|dv)
             * integral_(-R)^R |Gamma(-d+iv)|
                             |zeta M_X(1/2+i(gamma+v))|^2 dv
      <=C Y^(-delta) G_a
             integral_(-R)^R g_a(v)
                             |zeta M_X(1/2+i(gamma+v))|^2 dv.

We used 2d>delta and Y>=1, not a uniform O(1) Gamma mass. Summing
and using (1) proves (2). Since Y^(-delta)=L^(-1/4), (4) implies
the desired bound by substitution. This implication supplies no bound
for either premise in (4).

To exhibit the remaining correlation without suppressing the weight,
finite interchange writes R_Gamma exactly as

    integral_T^(2T) |zeta(1/2+it)|^2
      sum_(rho in S, |gamma-t|<=2delta) m_rho
        integral_(-R)^R g_a(v)
                     |zeta M_X(1/2+i(gamma+v))|^2 dv dt.          (6)

Its two zeta amplitudes occur at t and gamma+v, while the sampling
measure is chosen by the off-line zeros. Even a proposed replacement
by an unselected, fixed-offset integral would leave
|zeta(1/2+it)|^2 |zeta(1/2+i(t+h))M_X(1/2+i(t+h))|^2.
That has a second zeta-squared factor. No such replacement or mixed
moment bound is proved here. Linearizing the detector's absolute value
instead would introduce phases selected by the zeros; those phases
are not deterministic Dirichlet-polynomial coefficients either.

### 3. The tail has a length margin but still a selected measure

The other surviving term has the exact representation

    R_P=integral_T^(2T) |zeta(1/2+it)|^2
      sum_(rho in S, |gamma-t|<=2delta) m_rho
        |P_(beta-1/2)(1/2+i(t+(gamma-t)))|^2 dt.                 (7)

Since |b_X(k)|<=tau(k), the coefficients of P_d(s+ih) are bounded
by tau(k), uniformly in d>=0 and deterministic real h. The standard
divisor bound tau(k)=O_epsilon(k^epsilon) gives the displayed
coefficient condition of A. Fazzari, *A weighted central limit theorem
for log|zeta(1/2+it)|*,
[arXiv:1912.08127v2, Lemma 2.1, printed p. 3](https://arxiv.org/html/1912.08127v2).
Also K=T^(1/4)(log(3T))^2<=T^(3/8) eventually. For A=1 and
B=P_d(s+ih), that lemma's length restriction theta+2sigma<1
has the fixed margin 1-2(3/8)=1/4.

These checks address size and length only. The source evaluates a
continuous deterministic-polynomial moment against |zeta|^2. It does
not identify (7) with that moment: d and h=gamma-t are selected by
the zeros, and the multiplicity-counted measure in (7) remains.
Even granting uniform source errors for deterministic d,h would not
remove this measure. Bounding by a supremum merely leaves
n_delta(t) times a polynomial supremum inside the weighted integral;
replacing n_delta by its mean is an additional unproved assertion.
No uniformity for a selected or truncated family is assumed.

In Baier Section 6, (79)--(84), the retained weight is its specified
finite polynomial; the subsequent use of separated subsets is a
further step. The weight E_rho in (6)--(7) is not that polynomial.
Substituting it in the final weighted-density conclusion would assume
the missing extension. Thus the present positive reduction closes
neither detector branch with the approved moment tool. This is the
concrete stopping point, not an assertion that every use of the
detector, Gamma cancellation or weighted zero information must fail.

### 4. Check what the available count-only fallback actually proves

Let N_>(sigma,v) use the strict beta and strict upper-height convention
of L485. Take sigma=1/2+delta/2 and H=5delta ell. For
s=t-(5/2)delta, the closed target interval
[t-2delta,t+2delta] lies strictly inside [s,s+5delta). Consequently

    n_delta(t)<=N_>(sigma,s+H/log U)-N_>(sigma,s).

This includes all closed window endpoints and all multiplicities;
the horizontal threshold already agrees exactly with the source.
For a common large onset, 1<=H<=U^(1/4) and the translated
t interval is contained in [0,U]. L485 therefore gives

    integral_T^(2T) n_delta(t)^2 dt
       <=25 C_485 U delta^2 ell^2 exp(-delta ell/8).

Cauchy--Schwarz with Q_4(T)<=C_4 T L^4 now gives

    W_delta<=5 sqrt(3 C_485 C_4) T delta ell L^2
                                         exp(-delta ell/16)
            <=10 sqrt(3 C_485 C_4) T delta L^3
                                         exp(-delta L/16),

using L<=ell<=2L. Since delta L=log L, this is (5). Compared with
the proposed O(T delta L^2 L^(-c)), this available certificate has
the divergent ratio L^(15/16+c) for every fixed c>0. It repeats the
known separation loss in L486 at this target's halved horizontal
cutoff. It cannot establish that the actual W_delta is large.

The new diagnostic information is (6)--(7), with the exact Gamma
cost and a verified polynomial length margin, not an improvement
over (5). Stop this implementation until a materially new mixed
weighted input or a different cancellation mechanism is justified.
The original mass kernel, other scales, complementary mass and
individual-height positivity remain outside the proved reduction.

## Mathlib

Full matching coverage is not checked. No Mathlib theorem is claimed
to prove the detector, the selected mixed moments or the desired
weighted bound. The Gamma recurrence, finite interchange and
Cauchy--Schwarz are standard supporting mathematics; library support
for them alone would not certify the number-theoretic inputs.
