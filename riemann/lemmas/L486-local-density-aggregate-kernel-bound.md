# Lemma 486: a count-only local-density bound for the aggregate kernel

## Hypotheses

Use the actual Xi, positive completion factor A, Hardy function Z,
conjugate pairs gamma_j +/- i d_j, full multiplicities m_j, one-copy
quotients F_j, finite P_T and clipped windows J_j(T) of L471. In
particular 0<d_j<1/2, Xi=-AZ on the real axis, and
F_j(z)=Xi(z)/((z-gamma_j)^2+d_j^2). For real T>1 and a frozen
cutoff delta define

    L=log T, U=3T, ell=log U,
    S_delta(T)={j in P_T: d_j>=delta},
    B_delta(T)=sum_(j in S_delta(T)) m_j d_j^3
        integral_(J_j(T)) (1-v^2)
          |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv,
    Q_4(T)=integral_T^(2T) |Z(t)|^4 dt.

All logarithms are natural. Use L483's exact finite nonnegative
kernel identity for this restricted sum, and L018's affine zero
correspondence, preserving multiplicities.

Let C_485 be an absolute constant in L485: if V>=2,
1<=H<=V^(1/4), 1/2<=sigma<=1, and N(sigma,y) counts zeta
zeros beta+i gamma with beta>sigma and 0<gamma<y, then

    integral_0^V [N(sigma,s+H/log V)-N(sigma,s)]^2 ds
        <= C_485 V H^2 exp(-(sigma-1/2)log V/4).       (1)

This is Kenneth Maples and Brad Rodgers, *Bootstrapped zero density
estimates and a central limit theorem for the zeros of the zeta
function*, IJNT 11 (2015), 2087--2107,
[arXiv:1404.3080v2 (4 June 2016), Proposition 2.5, printed p. 5](https://arxiv.org/html/1404.3080v2),
at k=2,c=1/4, with the restricted normalization/tail repairs in
L485. Its arithmetic inputs, including Theorem 2.4 and Corollary
4.2, remain citations; neither a full manuscript audit nor the
general-weight assertion (19)/Lemma 4.3 is imported. Constants in
(1) are uniform in all displayed parameters.

Use also C_4,T_4 such that Q_4(T)<=C_4 T L^4 for every real
T>=T_4. This is the continuous fourth moment already imported in
L471/L483 from H. M. Bui and R. R. Hall, *On the derivatives of
Hardy's function Z(t)*,
[arXiv:2304.05178v1 (11 April 2023), Theorem 3 and Section 7](https://arxiv.org/html/2304.05178v1),
at ordinary derivative orders (0,0,0,0), retaining their source-audit
qualifications. It is not a zero-conditioned amplitude estimate.

No RH, simplicity, spacing, independence, selected-value moment,
closed-beta extension of (1), or external half-plane premise is used.

## Conclusion

There is a single absolute T_* such that for every real T>=T_*
and every real 1/log T<=delta<=1/8,

    B_delta(T)^2 <= 100 exp(1/4) C_485 U ell^2 delta^(-2)
                        exp(-delta ell/4) Q_4(T).       (2)

Consequently, uniformly over these moving cutoffs,

    B_delta(T)/(T L^3)
        <= C_* delta^(-1) exp(-delta L/8),              (3)
    C_*=20 exp(1/8) sqrt(3 C_485 C_4).

In particular delta=8 log log T/log T gives

    B_delta(T)/(T L^3) <= C_*/(8 log log T) -> 0.        (4)

This replaces the recorded sufficient coefficient 100 in C483a by
8 for this sector, using a different known-tool estimate. It does
not assert an optimal coefficient, or superiority to an optimized
application of C483a's density input. It is a routine specialization
of cited count/moment results, with no claim of a new density theorem
or verified originality beyond the sources checked.

The right side of (3) does not tend to zero for every admissible
delta with delta log T tending to infinity. For example, at
delta=log log T/log T its scale factor is
(log T)^(7/8)/log log T, which tends to infinity. Thus this
certificate does not establish the all-mesoscopic little-o target.
This is not a lower bound on B_delta, a counterexample to that
target, or an obstruction to every count-based method. Smaller
displacements, the full negative mass, all-height signs and
all-degree mixed positivity remain unresolved. The separate critical
application audit below verifies (2)--(4) without a repair; the cited
source arithmetic and manuscript proofs are not independently audited.

## Proof

### 1. Preserve the original finite kernel

For d>0 let

    k_d(u)=(d^2-u^2)/(u^2+d^2)^2, |u|<=d,
    k_d(u)=0, |u|>d,
    K_delta(t)=sum_(j in S_delta(T)) m_j k_(d_j)(t-gamma_j).

L483's substitution t=gamma_j+d_j v on the exact clipped windows
gives

    B_delta(T)=integral_T^(2T) |Z(t)|^2 K_delta(t) dt.   (5)

Indeed d_j^3(1-v^2)dv=(d_j^2-(t-gamma_j)^2)dt and
F_j/A=-Z/((t-gamma_j)^2+d_j^2) on the real axis. The quadratic
denominator is positive there, including at real Xi zeros. Removing
one pair copy leaves exactly the coefficient m_j. Singleton windows
have zero integral and k_d vanishes at both support endpoints.
L471's compact-rectangle finiteness makes every sum below finite;
no density estimate or infinite interchange establishes finiteness.

Choose T_* large enough that, for every T>=T_*,

    T>=max(3,T_4), L>=8, (5/2)log(3T)<=(3T)^(1/4).   (6)

Such a common onset exists because log x/x^(1/4) tends to zero.
It is independent of delta and of every band chosen below. No
effective numerical onset or source-moment constant is claimed.

### 2. Bands, strict horizontal cutoff and enlarged ordinate window

Freeze T and delta in the stated range. Let r_b=2^b delta,
b=0,...,J, where r_J<1/2<=2r_J. Partition S_delta(T) into

    S_b={j in P_T: r_b<=d_j<min(2r_b,1/2)},
    K_b(t)=sum_(j in S_b) m_j k_(d_j)(t-gamma_j).

These half-open bands include equality at each lower boundary;
equality at 2r_b goes into the next band, and d_j=1/2 is excluded
by the actual zero strip. They partition the original restricted
sum, so K_delta=sum_(b=0)^J K_b, without changing weights.
The last band may be truncated or empty.

Since 0<=k_d<=d^(-2), a nonzero contribution to K_b(t) is at
most r_b^(-2) times its multiplicity and has
|gamma_j-t|<=d_j<2r_b. Select, as in L483, the right-side zeta
zero rho_j=1/2+d_j+i gamma_j using the lower Xi zero and L018.
This is injective on the distinct indexed pairs, with order m_j:
rho_j determines both d_j and gamma_j. Equal ordinates and
repeated zeros therefore require no spacing or factor-two correction.

Put

    a_b=r_b-1/ell, sigma_b=1/2+a_b,
    H_b=5r_b ell, h_b=H_b/log U=5r_b,
    C_b(s)=N(sigma_b,s+h_b)-N(sigma_b,s).

Because r_b>=delta>=1/L and ell>L, one has
0<a_b<r_b<1/2, hence 1/2<sigma_b<1. Every selected zero in
the band satisfies beta=1/2+d_j>=1/2+r_b>sigma_b, including
equality d_j=r_b. The deliberate shift 1/ell below the band's
lower cutoff will cost exactly exp(1/8) after taking the L2 norm;
no inclusive-beta version of the source is assumed.

At t in [T,2T] set s=t-2r_b. Since r_b<1/2 and T>=3,
0<T-1<s<=2T<U. The selected positive ordinate satisfies

    s<gamma_j<t+2r_b<t+3r_b=s+h_b.

The source's strict cumulative height convention makes C_b(s)
the multiplicity-counted number in [s,s+h_b), restricted to
positive ordinates. The strict enlargement to width 5r_b includes
all relevant closed support endpoints; no almost-everywhere
endpoint extension is needed. Counts may include extra zeros,
which only enlarge the nonnegative majorant. Pointwise,

    0<=K_b(t)<=r_b^(-2) C_b(t-2r_b), T<=t<=2T.         (7)

The source parameters are admissible simultaneously for every band:

    H_b>=5ell/L>5>=1,
    H_b<(5/2)ell<=U^(1/4),
    [T-2r_b,2T-2r_b] is a subset of [0,U].

The fixed padding U=3T and the physical width h_b=5r_b both
remain in the estimate. We have not used translation invariance
of a moment theorem or a fixed-H-only limit.

### 3. Integrated count, finite L2 sum and fourth moment

Squaring (7), substituting s=t-2r_b, and enlarging the nonnegative
integral only to [0,U], permits (1) at this exact U,H_b,sigma_b:

    ||K_b||_(L2[T,2T])
       <=r_b^(-2) sqrt(C_485 U) H_b exp(-a_b ell/8)
       =5 exp(1/8) sqrt(C_485 U) ell r_b^(-1)
                                             exp(-r_b ell/8). (8)

There is no correlation assumption here: (8) bounds only the count
kernel. In particular the source exponent -(sigma_b-1/2)/4 in
the squared integral becomes -a_b ell/8 in its norm.

The finite L2 triangle inequality, followed by r_b=2^b delta,
gives, retaining the entire band sum before bounding it,

    ||K_delta||_2
       <=5 exp(1/8) sqrt(C_485 U) ell
                sum_(b=0)^J r_b^(-1) exp(-r_b ell/8)
       <=5 exp(1/8) sqrt(C_485 U) ell delta^(-1)
                exp(-delta ell/8) sum_(b=0)^J 2^(-b)
       <=10 exp(1/8) sqrt(C_485 U) ell delta^(-1)
                                             exp(-delta ell/8). (9)

Thus no factor J or sqrt(J) is hidden. The geometric bound is
uniform as delta moves, including when J changes. Empty bands,
coincident ordinates and multiplicities leave (7)--(9) unchanged.

Cauchy--Schwarz applied after aggregation in (5) gives
B_delta<=sqrt(Q_4(T))||K_delta||_2. Squaring (9) proves (2).
This uses the continuous fourth moment only, without inserting it
at a zero-selected height. With U=3T, ell<=2L for T>=3,
ell>=L and Q_4(T)<=C_4 T L^4, it follows that

    B_delta(T)
       <=10 exp(1/8) sqrt(3 C_485 C_4) T L^2 ell
                          delta^(-1) exp(-delta ell/8)
       <=C_* T L^3 delta^(-1) exp(-delta L/8).

This proves (3) with the displayed constant. Every height/cutoff
loss is explicit: padding by 3, width 5r_b, lowered strict cutoff
1/ell, kernel factor r_b^(-2), square-root source decay and
the finite geometric sum at most 2. No unit-shell supremum or
unrestricted weighted source formula has entered the proof.

### 4. Actual versus required scale and the certificate's limit

Write x=delta L. The dimensionless factor in (3) is exactly

    delta^(-1) exp(-delta L/8)=L exp(-x/8)/x.           (10)

For delta=8 log L/L the admissible interval holds eventually,
since 8 log L grows to infinity and (log L)/L tends to zero.
Then x=8 log L and (10)=1/(8 log L), proving (4) for every
sufficiently large real T, not just a height sequence. No optimization
of this sufficient coefficient is needed for the conclusion.

For the independent admissible test delta=log L/L, one instead
has x=log L tending to infinity but (10)=L^(7/8)/log L tending
to infinity. To check the latter limit, put y=log L; its logarithm
is 7y/8-log y, which tends to infinity. Consequently the proved
upper bound (3) does not certify little-o for every admissible
mesoscopic cutoff. This says nothing about the actual size of
B_delta at that test cutoff. In particular a divergent upper
bound cannot refute its possible little-o behavior.

This stops this count-only certificate at the stated universal
threshold; it does not rule out another use of counts, a sharper
weighted argument, or the actual mass claim. Formula (4) controls
only d_j>=8 log log T/log T. L471's negative-mass inequality
uses the full B(T); its replacement by B_delta would be invalid.
The complementary sector, a full integrated saving, individual
signs and higher mixed positivity remain separate gaps.

### 5. Separate critical application audit — 30 October 2026

The invocation-start SPECIALIZE scope is
`drafts/literature/2026-10-30-l486-critical-audit-coverage.md`.
This audit checks the complete application (2)--(10), using L018,
L471, L483 and L485. Their primary-source comparison is reused;
neither the arithmetic inputs to L485 nor Bui--Hall's fourth-moment
proof is independently audited. No stronger estimate is claimed.

First, the original pair integral gives (5) exactly: with
u=t-gamma_j=d_j v, d_j^3(1-v^2)dv=(d_j^2-u^2)dt, and
|F_j/A|^2=|Z|^2/(u^2+d_j^2)^2. The denominator is positive
on the real axis, so this remains true at real Xi zeros. F_j removes
one pair copy and the original m_j stays in front. P_T is finite by
L471's compact-rectangle argument, with no count theorem needed.
Clipping is precisely intersection with [T,2T]; singleton windows
and the endpoints u=+/-d_j contribute zero. Thus all kernels are
finite, nonnegative sums of continuous functions. On their supports,
k_d=d^(-2)(1-v^2)/(1+v^2)^2 lies between zero and d^(-2).

For every permitted delta, let J be the largest nonnegative integer
with 2^J delta<1/2. Such J exists since delta<=1/8, and is finite.
Then 1/2<=2r_J and the half-open bands cover every delta<=d<1/2
exactly once, including dyadic equalities. For a contributing pair,
L018 sends gamma_j-i d_j to 1/2+d_j+i gamma_j with the same
order m_j. Equality of two selected zeta zeros forces equality of
both gamma_j and d_j, so there is no multiplicity or factor-two
loss, even at coincident ordinates.

Since ell>L and r_b>=1/L, a_b=r_b-1/ell>0; also a_b<1/2.
Thus sigma_b is admissible in L485, and beta>=1/2+r_b>sigma_b
covers d_j=r_b under its strict convention. For t in [T,2T],
s=t-2r_b is in [T-2r_b,2T-2r_b] subset (0,U). A nonzero
kernel summand has |gamma_j-t|<=d_j<2r_b, hence
s<gamma_j<t+2r_b<t+3r_b=s+5r_b. In particular the ordinate
is positive and belongs to the source's [s,s+h_b) count. This
proves (7) pointwise without any endpoint exception.

All bands share the onset in (6): 5ell/L<=H_b<(5/2)ell,
where 5ell/L>5, and (5/2)ell<=U^(1/4) eventually for every
real T beyond a fixed threshold. The translated integration domain
is contained in [0,U]; nonnegativity allows its enlargement to that
interval. The physical width is exactly H_b/log U=5r_b. Thus
L485 is applied at the base U itself, with its uniform constant,
rather than at an unproved translate of a T-based moment theorem.

Taking the square root of (1) gives exp(-a_b ell/8). Multiplying
by r_b^(-2)H_b gives precisely
5ell r_b^(-1)exp(1/8)exp(-r_b ell/8), verifying (8).
Finite L2 triangle is valid regardless of band overlap. Since
r_b^(-1)=2^(-b)delta^(-1) and exp(-r_b ell/8) is at most
exp(-delta ell/8), its entire finite sum is bounded by the geometric
sum at most 2. There is no J-dependent loss. Squaring the resulting
coefficient 10 exp(1/8) gives 100 exp(1/4) in (2).
Cauchy--Schwarz uses the continuous Q_4 on exactly [T,2T]; it
never evaluates a moment at a selected zero or random window.

Substituting U=3T and Q_4<=C_4 T L^4 gives the coefficient
10 exp(1/8)sqrt(3 C_485 C_4) times T L^2 ell. Since T>=3
implies L<=ell<=2L, (3) has exactly the stated C_*, uniformly
in T,delta and b. The single onset combines (6) with the cited
fourth-moment onset; no parameter-dependent threshold is introduced.

Finally, putting x=delta L yields (10) exactly. At x=8 log L
the factor is 1/(8 log L), and the cutoff is admissible eventually
because 8 log L>=1 and 64 log L<=L eventually. At x=log L
it is L^(7/8)/log L, tending to infinity since
(7/8)log L-log log L tends to infinity. This second cutoff is
also eventually admissible and has x tending to infinity. Both
tests hold at all sufficiently large real heights. They verify the
sufficient coefficient 8 and the recorded limitation of this upper
bound, without lower-bounding the actual B_delta.

The audit therefore retains (2)--(4) unchanged. Empty bands and empty
selected sets satisfy all bounds; arbitrary multiplicities and clipped
endpoints have been included. The complementary displacements, full
B(T), full negative mass and all-height/all-degree signs remain open.
This is local verification of a known-tool specialization, not progress
beyond the checked source theorems or an independent manuscript audit.

## Mathlib

Full matching coverage for (2)--(4) is not checked. Supporting
coverage for the imported local count theorem, continuous fourth
moment, finite L2 triangle inequality and kernel estimates is also
unchecked. Unknown availability is not evidence of absence. The
precise citations and local specialization above supply the informal
inputs, without a formal-verification or source-manuscript-audit claim.
