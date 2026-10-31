# Lemma 483: aggregate-kernel saving at fixed displacement

## Hypotheses

Use the actual Xi, A, Hardy function Z, conjugate pairs
gamma_j +/- i d_j, multiplicities m_j, one-copy quotients F_j,
P_T and clipped windows J_j(T) of L471. Thus Xi=-AZ on the real
axis, 0<d_j<1/2, F_j=Xi/q_j and q_j(z)=(z-gamma_j)^2+d_j^2.
For T>=2 set delta=1/16 and restrict the original sum without
changing its weights:

    S_T={j in P_T: d_j>=delta},  M(T)=sum_(j in S_T) m_j,
    B_delta(T)=sum_(j in S_T) m_j d_j^3
       integral_(J_j(T)) (1-v^2)
          |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv,
    Q_4(T)=integral_T^(2T) |Z(t)|^4 dt.

Import Shashi Chourasiya and Aleksander Simonic, *An explicit form
of Ingham's zero density estimate*, arXiv:2507.15184v1 (21 July 2025),
[Corollary 1, equation (3), Table 1, p. 2](https://arxiv.org/html/2507.15184v1).
Its N(sigma,U) counts beta+i gamma with beta>=sigma and
0<gamma<=U, with multiplicity. For 0.500<=sigma<=0.625 and
U>=3*10^12 it states

    N(sigma,U)<=8.604 U^[3(1-sigma)/(2-sigma)] log^3 U
                  +9.461 log^2 U+167.8 log U.

The cutoff inequalities are inclusive. Its verified-height input,
constants and manuscript proof remain cited, not independently
audited here. This is not the separate external half-plane premise.

Import H. M. Bui and R. R. Hall, *On the derivatives of Hardy's
function Z(t)*, arXiv:2304.05178v1 (11 April 2023),
[Theorem 3 and Section 7](https://arxiv.org/html/2304.05178v1), at
ordinary derivative orders (0,0,0,0): Q_4(T)=O(T(log T)^4), as
already applied in L471 Section 4. This is a continuous fourth
moment, with no selected-zero or short-window hypothesis. No shifted
moment proposition or new proof of this known moment is needed.

Use L467's multiplicity-counted closed-shell bound
#{rho: v<=Im(rho)<=v+1, Im(rho)>0}<=18 log(v+2), v>=0, for all
nontrivial zeros. Its Bellotti--Wong v2 Theorem 1.1 citation and
local specialization retain their qualifications. No RH, simplicity,
spacing, selected-amplitude bound or external fixed-half-plane
estimate is assumed. All logarithms are natural.

## Conclusion

Define H(U)=8.604 U^(21/23) log^3 U+9.461 log^2 U+167.8 log U.
For every real T>=10^12,

    B_delta(T)^2<=73728 log(2T+2) H(3T) Q_4(T).           (1)

Consequently, as real T tends to infinity,

    B_delta(T)=O(T^(22/23)(log T)^4)=o(T(log T)^3).        (2)

This controls only the original L471 summands with d_j>=1/16.
It supplies no complementary-sector estimate, full negative-mass
saving, individual-height sign or RH conclusion. It is a local
specialization of cited density and moment results, not a new density
or fourth-moment theorem. No matching theorem for the whole restricted
B sum was established by the recorded literature review; no originality
claim is made. Its shared kernel argument passes the bounded application
audit recorded below; no independent source-manuscript audit is claimed.

## Proof

### 1. Exact kernel and finite aggregation

For d>0 define k_d(u)=(d^2-u^2)/(u^2+d^2)^2 on |u|<=d,
and k_d(u)=0 otherwise. Put

    K_T(t)=sum_(j in S_T) m_j k_(d_j)(t-gamma_j).

The endpoint values of k_d are zero, so it is continuous and
nonnegative. L471 proves P_T finite without a density assumption.
In each original integral substitute t=gamma_j+d_j v. The factor
d_j^3(1-v^2) dv becomes (d_j^2-(t-gamma_j)^2) dt on exactly
I_j=[T,2T] intersect [gamma_j-d_j,gamma_j+d_j]. On the real axis
q_j(t)>0, and the entire identities give F_j/A=-Z/q_j. Therefore

    B_delta(T)=integral_T^(2T) |Z(t)|^2 K_T(t) dt.        (3)

This holds also at real Xi zeros. Only a finite sum was integrated.
A singleton clipped window has zero integral and its kernel vanishes
there. F_j removes one pair, not all m_j copies; hence the coefficient
m_j in (3) is precisely the original coefficient. Coincident ordinates
have not been merged.

### 2. Multiplicity-counted density input

The meeting-window condition gives T-d_j<=gamma_j<=2T+d_j.
Since T>=2 and d_j<1/2, this implies 0<gamma_j<3T. By L018,
the lower Xi zero gamma_j-i d_j corresponds to the zeta zero
rho_j=1/2+d_j+i gamma_j, of multiplicity m_j. Its real part is at
least 9/16. Distinct conjugate pairs give distinct rho_j, since equality
determines both gamma_j and d_j, even when only the ordinates coincide.
Thus the multiplicity-counted injection proves

    M(T)<=N(9/16,3T)<=H(3T), T>=10^12.                  (4)

Indeed 9/16 is inside the source range, 3T>=3*10^12, and
3(1-9/16)/(2-9/16)=21/23. Its inclusive cutoff covers d_j=1/16.
The cumulative padded count covers both clipped endpoint windows;
no dyadic density theorem or generic-height restriction is used.

### 3. Kernel mass and overlap

For d>=delta, 0<=k_d<=d^(-2)<=delta^(-2). Inside its support
k_d is the derivative of u/(u^2+d^2), so

    integral_R k_d(u) du=[u/(u^2+d^2)]_(-d)^d=1/d.

Clipping decreases this nonnegative integral. Consequently

    integral_T^(2T) K_T(t) dt<=delta^(-1) M(T).           (5)

At fixed t, every contributing pair has |t-gamma_j|<=d_j<1/2.
Its selected right-side zeta zero is in [t-1/2,t+1/2]. The same
injective selection as in (4), now followed by L467 at v=t-1/2>=0,
therefore gives

    K_T(t)<=18 delta^(-2) log(t+3/2)
           <=18 delta^(-2) log(2T+2), T<=t<=2T.          (6)

L467 counts both endpoints and all multiplicities. No factor of two
is required: one right-side zero of multiplicity m_j is selected per
pair, and the shell bound counts at least those zeros. There is no
simplicity or lower-spacing assumption.

Nonnegativity, (5) and (6) imply

    integral_T^(2T) K_T(t)^2 dt
       <=18 delta^(-3) M(T) log(2T+2)
        =73728 M(T) log(2T+2).                           (7)

Cauchy--Schwarz applied once to (3), after aggregation, gives
B_delta(T)^2<=Q_4(T) integral_T^(2T) K_T(t)^2 dt. Together with
(4) and (7), this proves (1). All sums and integrals are finite.
This calculation differs from L471's separate-pair substitution;
that recorded loss did not establish a failure of this aggregation.

### 4. Actual versus required scale

The explicit H(3T) is O(T^(21/23)(log T)^3). Padding by 3 changes
only the implied constant. Combining (1), log(2T+2)=O(log T) and
the cited fourth moment yields

    B_delta(T)^2=O(T^(44/23)(log T)^8),
    B_delta(T)=O(T^(22/23)(log T)^4).

Dividing by the required scale T(log T)^3 gives
O(T^(-1/23) log T), tending to zero: with x=log T this limit is
x exp(-x/23)->0. This proves (2) for all sufficiently large real T,
not just a height sequence. No effective numeric fourth-moment
constant or onset is asserted. Empty selected sets give zero throughout.

Nothing estimates d_j<1/16. Removing one nonnegative sector of a
sufficient majorant does not bound the full majorant or reverse
L471's one-sided inequality. Even a full integrated saving would
not establish all-height signs or all-degree mixed positivity.

### Shared kernel audit — 30 October 2026

The separate critical audit of C483a verifies Sections 1--3's shared
finite kernel argument under the saved moving-cutoff audit scope.
In particular, substitution in the original B sum produces k_d exactly;
one-copy F_j and full m_j are preserved. The kernel is nonnegative,
has supremum at most d^(-2) and full mass 1/d. The right-side zeta
zero selection is injective with orders, including coincident
ordinates. The closed shell therefore gives the displayed supremum
bound without an extra factor two, and multiplication by the L1 bound
gives the exact delta^(-3) loss. For delta=1/16 its coefficient is
18*16^3=73728. Cauchy--Schwarz requires only the cited continuous
fourth moment. Clipped and singleton windows, real zeros and empty
sets cause no exceptional terms. The full replay and its qualifications
are recorded in C483a's canonical audit, without creating a new lemma.

This is a check of the common local application, not an independent
audit of the density or moment manuscripts or their computations.
It adds no complementary-sector bound, full negative-mass saving or
positivity result. Mathlib matching remains unchecked.

## Mathlib

Full matching coverage for this restricted pair-mass result has not
been checked. Supporting coverage for the density theorem, explicit
closed shells, continuous fourth moment and their analytic applications
is also unchecked; unknown availability is not absence. The citations
and L018/L467/L471 are the inputs; the finite kernel and hypothesis
arguments above are the needed specialization.
