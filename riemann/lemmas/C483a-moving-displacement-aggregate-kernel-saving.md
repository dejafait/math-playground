# Corollary 483a: aggregate saving at a moving displacement cutoff

## Hypotheses

Use the actual Xi, positive completion factor A, Hardy function Z,
pairs gamma_j +/- i d_j, full multiplicities m_j, one-copy quotients
F_j, finite P_T and clipped windows J_j(T) of L471. Thus
Xi=-AZ on the real axis, 0<d_j<1/2 and
F_j(z)=Xi(z)/((z-gamma_j)^2+d_j^2). All logarithms are natural.
For real T>e put

    L=log T, l=log L, delta=delta(T)=100 l/L,
    S_T={j in P_T: d_j>=delta}, M(T)=sum_(j in S_T) m_j,
    B_delta(T)=sum_(j in S_T) m_j d_j^3
        integral_(J_j(T)) (1-v^2)
          |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv,
    Q_4(T)=integral_T^(2T) |Z(t)|^4 dt.

The cutoff is evaluated at T, including when a cumulative zero count
is evaluated at 3T. No weights or pair multiplicities are changed.

Use the precise inputs recorded in L483, with their retained source
qualifications:

* Shashi Chourasiya and Aleksander Simonic, *An explicit form of
  Ingham's zero density estimate*, arXiv:2507.15184v1 (21 July 2025),
  [Corollary 1, (3), Table 1, printed p. 2; proof in Section 2.1,
  (10)--(11), and closing perturbation in Section 4](https://arxiv.org/html/2507.15184v1).
  Uniformly for 1/2<=sigma<=5/8 and U>=3*10^12,

      N(sigma,U)<=8.604 U^[3(1-sigma)/(2-sigma)] log^3 U
                     +9.461 log^2 U+167.8 log U.          (1)

  N counts beta+i gamma with beta>=sigma and 0<gamma<=U,
  with multiplicity. Use the corollary's inclusive, near-line-uniform
  statement, not Theorem 1 without its omitted-strip argument.
  The verified-height input, parameter computations and full manuscript
  are cited, not independently audited here.
* H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
  Z(t)*, arXiv:2304.05178v1 (11 April 2023),
  [Theorem 3 and Section 7](https://arxiv.org/html/2304.05178v1),
  at fixed ordinary derivative orders (0,0,0,0): there are absolute
  C_4>0 and T_4 such that Q_4(T)<=C_4 T(log T)^4 for all real
  T>=T_4. This is the continuous fourth moment already used in
  L471 and L483; no selected-zero moment or manuscript audit is asserted.
* L467's multiplicity-counted closed unit-shell bound
  #{rho: v<=Im(rho)<=v+1, Im(rho)>0}<=18 log(v+2), v>=0.
  Its input is Chiara Bellotti and Peng-Jie Wong,
  *Improved estimates for the argument and zero-counting function of
  the Riemann zeta-function*,
  [arXiv:2412.15470v2 (7 July 2025), Theorem 1.1, printed p. 1](https://arxiv.org/pdf/2412.15470v2).
  Retain L467's local-audit and source-computation qualifications.

No RH, simplicity, spacing, selected-amplitude or external fixed-half-plane
premise is assumed. Matching Mathlib coverage is unchecked.

## Conclusion

For every real T>=10^12 for which 0<delta(T)<=1/8, set

    a_T=3(1/2-delta)/(3/2-delta)=1-4delta/(3-2delta),
    H_delta(U)=8.604 U^a_T log^3 U+9.461 log^2 U+167.8 log U.

Then the complete bound, including both additive density remainders, is

    B_delta(T)^2 <= 18 delta^(-3) log(2T+2) H_delta(3T) Q_4(T). (2)

For every sufficiently large real T it follows that

    [B_delta(T)/(T L^3)]^2
       <= (36 C_4/(10^6 l^3))
           [206.496 L^(-385/3)+37.844 L^4/T+335.6 L^3/T]. (3)

In particular B_delta(T)=o(T(log T)^3). The conclusion concerns
only d_j>=100 log log T/log T. It gives no bound for the complementary
sector, full negative mass, individual-height signs or all-degree mixed
positivity. It is a local specialization of known density, moment and
kernel tools, not a new density/moment theorem or a claim of originality.
The bounded critical application audit below verifies this specialization;
the cited source manuscripts and computations remain imported inputs.

## Proof

### 1. Freeze the cutoff and retain the original finite kernels

Fix T in the domain of (2). All estimates in this section are at this
one T; delta is a positive number. L471 makes P_T, hence S_T, finite.
Use L483's exact nonnegative kernel

    k_d(u)=(d^2-u^2)/(u^2+d^2)^2 for |u|<=d,
    k_d(u)=0 for |u|>d,
    K_T(t)=sum_(j in S_T) m_j k_(d_j)(t-gamma_j).

The finite substitution in L483 Section 1 applies to any subset of
P_T: with t=gamma_j+d_j v, the numerator d_j^3(1-v^2) dv
becomes (d_j^2-(t-gamma_j)^2) dt. On the real axis,
F_j/A=-Z/((t-gamma_j)^2+d_j^2). Thus exactly

    B_delta(T)=integral_T^(2T) |Z(t)|^2 K_T(t) dt.         (4)

The clipping is [T,2T] intersect [gamma_j-d_j,gamma_j+d_j].
Singleton windows contribute zero and k_d is zero at both support
endpoints. All identities hold at real Xi zeros, since the positive
quadratic denominator never vanishes there. F_j removes only one copy;
the coefficient in K_T is therefore precisely m_j, even if m_j>1.
Pairs with coincident ordinates remain separate terms.

For completeness, the parameter-dependent bounds used before fixing
delta in L483 Sections 2--3 are checked explicitly. On its support,
0<=k_d<=d^(-2), and k_d is the derivative of u/(u^2+d^2).
Consequently integral_R k_d=1/d. Nonnegativity and clipping give

    integral_T^(2T) K_T(t) dt <= delta^(-1) M(T).         (5)

At t in [T,2T], every contributing pair has
|t-gamma_j|<=d_j<1/2. By L018, its lower Xi zero corresponds to
rho_j=1/2+d_j+i gamma_j, preserving m_j. Different pairs give
different rho_j because both gamma_j and d_j are recovered from rho_j.
Thus L467 at v=t-1/2>=0 counts all selected zeros, including equal
ordinates and endpoints. It gives

    K_T(t)<=18 delta^(-2) log(t+3/2)
           <=18 delta^(-2) log(2T+2).                   (6)

There is no extra factor two: only the right-side zeta zero per pair
is selected. Multiplying (5) by the supremum bound (6) proves

    integral_T^(2T) K_T(t)^2 dt
       <=18 delta^(-3) M(T) log(2T+2).                  (7)

Cauchy--Schwarz in (4) now bounds B_delta(T)^2 by Q_4(T) times
the left side of (7). No infinite interchange or spacing estimate occurs.

### 2. Uniform density at the frozen cutoff and padded height

Every pair in P_T satisfies T-d_j<=gamma_j<=2T+d_j, so
0<gamma_j<3T. For j in S_T the selected rho_j also has
Re(rho_j)>=1/2+delta. The same multiplicity-preserving injection yields

    M(T)<=N(1/2+delta,3T)<=H_delta(3T).                 (8)

Indeed 0<delta<=1/8 places sigma=1/2+delta in the closed source
interval, and 3T>=3*10^12. Equality d_j=delta is included by the
source's beta>=sigma convention. Padding covers windows clipped at
either end of [T,2T]; no dyadic density assertion is used. The
explicit constants in (1) are simultaneous for all these sigma, so
(8) introduces no unknown constant depending on moving delta.
Combining (7), (8) and Cauchy--Schwarz proves (2), retaining all three
terms of H_delta. Empty selected sets cause no exception.

### 3. Full actual-versus-required comparison

Since l/L is positive for T>e and tends to zero, one common T_0
can ensure T>=10^12, T>=T_4, L>=1 and 0<delta<=1/8 for every
real T>=T_0. This uses only a limit, not a numerical height claim.
The density constants and C_4 are independent of T and delta.

Exact subtraction gives

    1-a_T=4delta/(3-2delta)>=4delta/3.

As log(3T)>=L, the moving cutoff therefore implies

    (3T)^a_T=3T exp(-(1-a_T)log(3T))
       <=3T exp(-(4/3)delta L)=3T L^(-400/3).           (9)

Here delta is still delta(T), not delta(3T). For T>=3,
log(3T)<=2L and log(2T+2)<=2L. Apply these inequalities to
each term of H_delta separately:

    H_delta(3T)<=206.496 T L^(3-400/3)
                      +37.844 L^2+335.6 L.             (10)

The exact decimal coefficients are 8.604*3*8, 9.461*4 and
167.8*2. Also delta^(-3)=L^3/(10^6 l^3). Substituting (10)
and Q_4(T)<=C_4 T L^4 into (2) gives the complete squared bound

    B_delta(T)^2 <= (36 C_4/(10^6 l^3))
       [206.496 T^2 L^(-367/3)+37.844 T L^10+335.6 T L^9]. (11)

The first exponent is 3+1+4+3-400/3=-367/3; the others are
3+1+4+2=10 and 3+1+4+1=9. Division by T^2 L^6 gives (3).
Every term on its right tends to zero: l tends to infinity,
L^(-385/3) tends to zero, and L^4/T and L^3/T tend to zero
(write T=exp L). Since B_delta is nonnegative, (3) proves the
claimed little-o for all sufficiently large real T.

This checks the proposed coefficient 100 with a large margin; it
does not optimize that coefficient or assert another approved cutoff.
The remainders in (1) were kept through (11), rather than silently
absorbed into a height exponent with a cutoff-dependent constant.
No new proof of any imported density or moment theorem was needed;
the necessary specialization was the finite moving-subset calculation.

Finally, no estimate above controls d_j<delta(T). In particular the
one-sided bound N(T)<=2B(T) in L471 cannot be applied with B_delta
in place of its full B. Even a full integrated negative-mass saving
would not supply individual-height signs or higher mixed positivity.

### Critical application audit — 30 October 2026

The application passes the invocation-start SPECIALIZE audit. This is
verification of the existing known-tool specialization, with no stronger
estimate, source-proof verification or originality claim. The audit also
checks L483's shared kernel argument; it does not reprove the imported
density, shell or moment results.

First, finiteness is independent of density: each selected Xi pair has
its zeros in the compact rectangle with real part in
[T-1/2,2T+1/2] and imaginary part in [-1/2,1/2]. L018's nonzero
entire Xi has finitely many zeros there, with finite orders. For each
fixed real T the restriction S_T is therefore a finite set, even though
it need not vary continuously with T. No assertion of continuity of
that set, differentiation in T or infinite interchange is used.

Replaying the substitution in the original definition gives
d_j^3(1-v^2)dv=(d_j^2-u^2)dt, where u=t-gamma_j. Since
q_j(t)=u^2+d_j^2>0 and Xi=q_j F_j, the remaining square is
|Z(t)|^2/q_j(t)^2. This proves (4) on the exact clipped interval.
The positive quadratic also proves the identity at real Xi zeros.
Removing one copy, rather than m_j copies, leaves exactly the original
coefficient m_j. Singleton windows have zero measure and the kernel
is zero at both support endpoints. Thus multiplicities, real zeros
and clipping introduce no correction term.

For |u|<=d, the numerator is between zero and d^2 and the
denominator is at least d^4; this gives 0<=k_d<=d^(-2).
Differentiation of u/(u^2+d^2) gives exactly k_d in the support
interior. Evaluating at +/-d gives integral k_d=1/d. Finite summation
and clipping yield (5). For each t, the affine correspondence of L018
sends gamma_j-i d_j to 1/2+d_j+i gamma_j, with the same order.
Equality of the selected zeta zeros would force equality of both d_j
and gamma_j, hence of the indexed pair. The resulting injection is
valid also for coincident ordinates and m_j>1. Each selected zero
lies in the closed unit shell [t-1/2,t+1/2]. L467 therefore proves
(6) with its exact coefficient 18; selecting one side of each pair
requires no factor two. The pointwise inequality K_T^2<=(sup K_T)K_T
then proves (7). Cauchy--Schwarz uses precisely integral |Z|^4=Q_4,
not a selected-zero moment or an independence assumption.

The same injection gives (8): window intersection implies
T-d_j<=gamma_j<=2T+d_j, hence 0<gamma_j<3T in the stated domain.
The selected real part is at least 1/2+delta(T), including equality.
The density input is explicitly the inclusive Corollary 1, uniform
on 1/2<=sigma<=5/8, rather than the theorem with a near-line
exception. Its three simultaneous constants do not depend on delta.
Both density remainders survive (8). Evaluation at height 3T does
not change the frozen real-part cutoff. The shell bound and fixed
ordinary fourth moment likewise have no delta-dependent constant.
These facts justify the uniformity required in (2).

For the final comparison, direct subtraction in a_T gives
1-a_T=4delta/(3-2delta)>=4delta/3. Thus delta L=100 log L
gives exactly the saving L^(-400/3) in (9). For T>=3,
3T<=T^2 and 2T+2<=T^2, justifying both logarithm bounds.
Exact multiplication gives 8.604*24=206.496,
9.461*4=37.844 and 167.8*2=335.6. Before normalization the
three powers of L are respectively
3+1+4+3-400/3=-367/3, 3+1+4+2=10 and 3+1+4+1=9.
Division by T^2 L^6 gives exactly (3), including -385/3 and
both separate terms L^4/T and L^3/T. With T=exp L these latter
terms tend to zero, as does L^(-385/3); the common positive factor
1/(log L)^3 is bounded and tends to zero as well. Since
100 log L/L tends to zero, one common eventual domain supplies
delta<=1/8, the density height, the fourth-moment onset and L>=1
for every real T beyond it. There is no sequence-only inference or
claimed effective numerical onset.

Accordingly the audited conclusion is the stated restricted little-o
bound. The contribution d_j<delta(T) remains unestimated. L471's
N(T)<=2B(T) uses the full B(T), so replacing it by this restricted
sum would be invalid. Full negative-mass saving, individual signs and
all-degree positivity remain open. All source-audit qualifications
and the unchecked Mathlib status below remain in force.

## Mathlib

Full matching coverage for this moving-sector mass estimate is not
checked. Supporting formal coverage for the density corollary, closed
shells, fourth moment, finite kernel estimates and limiting comparison
is also unchecked. Unknown availability is not evidence of absence.
The named citations and local specializations are the mathematical
inputs; no formal verification or independent source audit is claimed.
