# Lemma 927: vanishing bump projection at arithmetic length T^(1/5)

## Hypotheses

Use exactly L637's actual real Hardy function Z and fixed data:
w>=0 in C_c^infinity((0,1)), integral w=1, u0 in (0,1) with
w(u0)>0, and psi(x)=exp(-1/(1-4x^2)) for |x|<1/2 and zero
otherwise. For T tending to infinity put

    L=log T, T<=X<=2T, a=X+u0*T,
    w_XT(t)=w((t-X)/T),
    <f,h>_T=integral w_XT(t) f(t) conjugate(h(t)) dt,
    g(t)=psi(L(t-a))/||psi(L(.-a))||_T,
    N=floor(T^(1/5)),
    U_c(t)=Z(t) sum_(n<=N) c_n n^(-it),
    V=span_C{Z(t)n^(-it):1<=n<=N}.

Pi is orthogonal projection onto this finite-dimensional subspace of
L2(w_XT dt). Coefficients c are arbitrary complex vectors, including
vectors depending on T,X. Every onset and constant below is uniform
in X and c; onsets are existential. No RH, simplicity, nonvanishing
at a, Gram invertibility or diagonal dominance is assumed.

Use L737's exact finite logarithmic form (5), its finite relative
bound (10), the local numerator (14), and the uniform window and
coefficient specialization justified in its step261 audit. Its
short-length analytic conclusion is not assumed at the new length.
Use audited L926 at the single fixed exponent epsilon=1/4:

    Q(c)=sum_(d<=N) phi(d)|sum_(k<=N/d)c_(dk)/sqrt(dk)|^2
         >=q0 N^(-1/4)||c||_2^2,                         (1)

where q0=a_(1/4)>0 is independent of N,c. L925 is not an input.

The changed analytic application imports S. Bettin, V. Chandee and
M. Radziwill, *The mean square of the product of the Riemann
zeta-function with Dirichlet polynomials*, J. reine angew. Math.
729 (2017), 51-79, DOI
[10.1515/crelle-2014-0133](https://doi.org/10.1515/crelle-2014-0133),
[arXiv:1411.7764v1, Theorem 1, pp. 1-2](https://arxiv.org/pdf/1411.7764v1).
For a fixed smooth phi supported in [1,2], M=Y^theta,
theta<17/33, and A(s)=sum_(n<=M) a_n n^(-s) with
a_n <<_eta n^eta, that theorem gives

    integral |zeta(1/2+it)A(1/2+it)|^2 phi(t/Y) dt
      =sum_(m,n<=M) a_m conjugate(a_n)/lcm(m,n)
         *integral [log(t*gcd(m,n)^2/(2*pi*m*n))+2*gamma]
                       phi(t/Y) dt
       +O_(eta,phi)(Y^(3/20+eta) M^(33/20)+Y^(1/3+eta)). (2)

Integer sums mean the floor of the displayed cutoff. Uniformity for
the specific smooth window family below uses the inspected source
proof operations: Section 3.1 p.9, Section 3.2 Cases 1-3 pp.12-15,
and Section 3.3 pp.15-16 (integration by parts and Mellin separation
with bounded weight seminorms), as checked in L737's step261 audit
and the changed-length source comparison. The arithmetic theorem is
imported, not reproved. Coefficients will have the common bound 1.
The prior SPECIALIZE gate is
drafts/literature/2026-11-09-longer-arithmetic-dictionary-test.md;
its completed source comparison is
drafts/literature/2026-11-09-longer-arithmetic-dictionary-scope.md.

The numerator uses only the undifferentiated real-axis
Riemann-Siegel formula, Titchmarsh-Heath-Brown, *The Theory of the
Riemann Zeta-Function*, 2nd ed. (1986), Section 4.17, (4.17.4),
p.89; see [DLMF 25.10.1-3](https://dlmf.nist.gov/25.10#E3),
including its O(t^(-1/4)) remainder. The real-axis normalization
Z(t)^2=|zeta(1/2+it)|^2 is unchanged from L637 and L737.

## Conclusion

For all sufficiently large T, uniformly for T<=X<=2T,

    ||U_c||_T^2 >= (q0/20) T L N^(-1/4)||c||_2^2
                       for every complex c,              (3)
    ||Pi g||_T^2 <= C N^(5/4)/(sqrt(T)L^2)
                 <= C T^(-1/4)/(log T)^2 = o(1).          (4)

Consequently ||g-Pi g||_T^2=1-o(1), uniformly in X. At this length
the dictionary cannot approximate the specified unit bump with any
fixed error strictly below 1 for all large T. This extends L737's
local realization obstruction. It does not supply signed weighted
transfer, Xi signs, all-degree mixed positivity or an RH candidate.
Longer lengths and other dictionaries remain undecided.

This is a source-covered quantitative specialization, classified
REPRODUCTION, not a new arithmetic or moment theorem. The checked
sources did not give a direct fixed-Z projection theorem at this
length; that search is not a certification of originality. Related
growing-order concentration/projection results are recorded in the
source comparison and have different order and weight hypotheses.
Written 9 November 2026; the separate audit below validates this
specialization under its named imports, without changing its conclusion.

## Proof

### 1. Charged moment estimate with a fixed padded cutoff

Use precisely L737's three nonnegative smooth partition functions
rho_j, sum 1 near [1,3], supported compactly inside
(alpha_j,2alpha_j), with alpha_j=3/4,5/4,2. Write x=X/T and
Y_j=alpha_j*T. The exact weight decomposition is

    w_XT(t)=sum_j phi_(j,x)(t/Y_j),
    phi_(j,x)(v)=rho_j(alpha_j*v) w(alpha_j*v-x).

The supports are common compact subsets of (1,2), and every required
smooth seminorm is bounded uniformly for x in [1,2]. These are the
same weight functions and source proof operations as in the prior
audit; the changed dictionary length does not alter them.

Fix the source exponent theta=1/4 and the source error parameter
eta=1/80, independently of T. Eventually N<=Y_j^(1/4) for each j,
since T^(1/5)/Y_j^(1/4)=alpha_j^(-1/4)T^(-1/20)->0.
For c nonzero set B=max_(n<=N)sqrt(n)|c_n|>0 and apply (2) with

    a_n=sqrt(n)c_n/B for n<=N,
    a_n=0 for N<n<=Y_j^(1/4).

Thus |a_n|<=1 uniformly, regardless of the vector's phases or its
dependence on T,X. Restore B^2 in both the main term and remainder.
Use B^2<=N||c||_2^2 and sum the three windows. The remainder in
each window before restoring B^2 is bounded by C T^(23/40), since

    3/20+(1/4)(33/20)+1/80=23/40,
    1/3+1/80=83/240 <23/40.

This uses the padded source cutoff, not the smaller physical cutoff
in the source error. The main coefficient equals
sqrt(m*n)/lcm(m,n)=gcd(m,n)/sqrt(m*n). Therefore, exactly as in
L737(4)-(5), but with the new charged exponent,

    ||U_c||_T^2=integral w_XT(t) F_(A_t)(c) dt+E(c),
    |E(c)|<=C_w N T^(23/40)||c||_2^2,                      (5)
    A_t=log(t/(2*pi))+2*gamma,
    F_A(c)=sum_(m,n<=N) c_m conjugate(c_n) gcd(m,n)/sqrt(m*n)
                     *[A+2log gcd(m,n)-log m-log n].

The zero vector satisfies (5) separately. Uniformity in X,c follows
from the already checked uniform weight operations and the common
normalized coefficient bound, not an entrywise error estimate.

### 2. Full logarithmic margin and error absorption

L737's finite divisor factorization and relative Schur estimate are
valid for every finite N and every complex c, independently of its
short-length analytic conclusion. They give

    F_(A_t)(c)>=(A_t-4log N)Q(c).                         (6)

Both coefficient logarithms, the gcd logarithm and 2*gamma remain
in (5)-(6); no diagonal surrogate is used. On the weight support,
t lies in [T,3T], and hence A_t>=L-C0 for a fixed C0. Since
log N<=L/5, (6) gives

    F_(A_t)(c)>=(L/5-C0)Q(c)>=(L/10)Q(c)                 (7)

after a single onset. Apply (1), use w_XT>=0 and
integral w_XT=T. Equations (5)-(7) imply

    ||U_c||_T^2 >= [(q0/10)T L N^(-1/4)
                                -C_w N T^(23/40)]||c||_2^2.

The ratio of the second bracketed term to T L N^(-1/4) is at most

    C_w N^(5/4) T^(-17/40)/L
       <=C_w T^(-7/40)/L ->0.                            (8)

Choose an onset making this ratio at most q0/20. This gives (3),
simultaneously for all X and c. Only the fixed conditioning exponent
1/4 was used; there is no epsilon->0 assertion. In particular the
generators are independent eventually as a consequence of (3),
rather than as an assumption needed for a Gram inverse.

### 3. Local numerator and the entire projection supremum

L737(14) uses no length restriction in its proof and gives

    |<g,U_c>_T|^2<=C_w N T^(1/2)||c||_2^2/L.             (9)

To make that applicability explicit, the bump has support
I=[a-1/(2L),a+1/(2L)] inside [T,3T] eventually, and has positive
norm since w(u0)>0. Its unit norm and weighted Cauchy-Schwarz give
integral w_XT |g|<=sqrt(||w||_infinity/L). The undifferentiated
Riemann-Siegel formula, including cutoff crossings, gives
sup_[T,3T]|Z|<=C T^(1/4). The elementary bound
|sum_(n<=N)c_n n^(-it)|<=sqrt(N)||c||_2 then proves (9).
This uses neither a microscopic-window moment nor a lower bound on Z.

For a finite-dimensional subspace in this complex Hilbert space,

    ||Pi g||_T^2=sup_(0!=U in V)|<g,U>_T|^2/||U||_T^2.

If Pi g=0 both sides are zero; otherwise Cauchy-Schwarz gives the
upper bound and U=Pi g attains it. Each U has a coefficient vector,
and (3) ensures a nonzero vector has nonzero norm at our onset.
Dividing (9) by (3) gives C N^(5/4)/(sqrt(T)L^2), uniformly in
every such vector, including T,X-dependent ones. Since
N^(5/4)<=T^(1/4), this proves (4). Orthogonality gives the exact
squared distance 1-||Pi g||_T^2 and the stated approximation exclusion.
All coefficient sums are finite; no closure or infinite-vector limit
has been interchanged with the uniform estimates.

### Separate application audit — 9 November 2026

The invocation-start SPECIALIZE assessment was
drafts/literature/2026-11-09-longer-arithmetic-dictionary-audit.md,
approved in a separate preceding literature turn. This audit reuses
that primary-source assessment and L737's step261 weight/coefficient
audit. It does not independently reprove BCR's arithmetic estimates.
The scope is the stated fixed bump, N=floor(T^(1/5)), all X in
[T,2T] and all complex coefficient vectors, including moving ones.

**Padded theorem and charged remainder.** The partition intervals
(3/4,3/2), (5/4,5/2), (2,4) cover [1,3], and the actual weight
is supported there. The explicit functions phi_(j,x) have uniformly
bounded derivatives and Mellin decay by the reused step261 argument;
changing the padded exponent does not change these functions. For
theta=1/4<17/33 and eta=1/80>0, each source scale is comparable
to T and N/Y_j^(1/4)<=alpha_j^(-1/4)T^(-1/20). Thus the
fixed padded cutoff is admissible at one common onset. The two exact
raw exponents are

    3/20+33/80+1/80=46/80=23/40,
    1/3+1/80=83/240 <138/240=23/40.

For every nonzero c, B>0 and A(1/2+it)=B^(-1)sum c_n n^(-it),
with the source coefficient bound |a_n|<=1 for the entire padded
prefix. Both main term and remainder must therefore be multiplied
by B^2. Since B^2<=N||c||_2^2, the actual quadratic remainder is
at most C_w N T^(23/40)||c||_2^2; at N<=T^(1/5) its power
of T is at most 31/40, not the uncharged 23/40. The source bound
is uniform in this normalized coefficient class, so this calculation
does not first fix c and then take T to infinity. The zero vector
is handled directly. The main coefficient is exactly
sqrt(mn)/lcm(m,n)=gcd(m,n)/sqrt(mn). Together with Z^2=|zeta|^2,
this gives the full Hermitian form (5), with no lost conjugation.

**Finite margin and its scale.** L737(6)-(10) are finite identities
and norm estimates, independent of the old length T^(1/10). In
particular the logarithmic cross-term operator has weighted row bound
4log N and column bound log N. Its norm is at most 2log N;
the factor 2 in the Hermitian cross term costs 4log N in F_A.
The nonnegative kappa contribution can be dropped. This verifies
the use of F_A>=(A-4log N)Q, without assigning signs to complex
entries or discarding either coefficient logarithm.

For t on the weight support, A_t>=L-C0 and 4log N<=4L/5.
Hence A_t-4log N>=L/5-C0>=L/10 at one onset (take, for
example, L>=10|C0|). L926 supplies one q0=a_(1/4)>0 for
every N>=2 and every complex c. Neither its constant nor its exponent
varies with T,X,c. Integrating against w_XT>=0 with integral T
therefore gives main lower bound (q0/10)T L N^(-1/4)||c||_2^2.
The ratio of the absolute error to T L N^(-1/4)||c||_2^2 is

    C_w N^(5/4)T^(23/40-1)/L
      <=C_w T^(1/4-17/40)/L
       =C_w T^(-7/40)/L ->0.

Thus it is eventually at most q0/20, uniformly in the window and
vector, leaving exactly the coefficient norm lower bound (3).
Equivalently, the main scale is at least T^(19/20)L times its
fixed constant, whereas the error power is at most T^(31/40).
The positive gap is 19/20-31/40=7/40. Floors improve these
inequalities and N>=2 holds eventually. No epsilon=0 endpoint or
effective onset was invoked.

**Bump and supremum.** The center a=X+u0 T has distances at least
u0 T and (1-u0)T from the endpoints of [T,3T], respectively.
Continuity at w(u0)>0 makes the bump norm positive at a uniform
onset. Its support length is 1/L, so unit normalization gives
integral w_XT|g|<=sqrt(||w||_infinity/L). The real-axis
Riemann--Siegel sum has O(sqrt(T)) terms with sum of absolute
coefficients O(T^(1/4)); its remainder is O(T^(-1/4)). This
proves the required uniform |Z| bound even at cutoff crossings.
Together with |sum c_n n^(-it)|<=sqrt(N)||c||_2, it proves (9)
for every vector without using any short-length conclusion of L737.

The finite-dimensional subspace is closed in the weighted L2 space,
interpreted as equivalence classes if w vanishes. Orthogonality and
Cauchy--Schwarz give the stated variational identity; when Pi g is
nonzero equality is attained at U=Pi g. Bound (3) ensures that every
nonzero coefficient vector represents a nonzero equivalence class.
Thus dividing the uniform bounds really controls the entire supremum:

    (C_w N T^(1/2)/L)/[(q0/20)T L N^(-1/4)]
      <=C N^(5/4)T^(-1/2)L^(-2)
      <=C T^(-1/4)L^(-2).

There is no assumption that coefficients have a limit, and no exchange
of a nonuniform asymptotic with this supremum. Pythagoras gives squared
distance 1-||Pi g||_T^2. For each fixed tolerance 0<=r<1, that squared
distance eventually exceeds r^2 uniformly in X, exactly the stated
approximation exclusion, not an exclusion of all dictionaries.

Audit result: all five load-bearing checks pass without correction.
The direct mathematical inputs remain L637, L737 and L926; the DAG
row is unchanged. This first separate application audit validates the
existing source-covered reproduction, not a new moment theorem or a
stronger projection estimate. BCR and the scalar source theorems remain
named imports. Effective constants, mixed/shifted dictionaries, signed
weighted transfer, actual-Xi signs and all-degree mixed positivity
are unresolved. Matching Mathlib coverage remains unknown.

## Mathlib

Full matching Mathlib coverage for this fixed-Z projection theorem,
the BCR moment theorem and its uniform window application is not
checked and remains unknown. No absence claim or formal verification
is made. Supporting finite-form, conditioning and Hilbert projection
inputs are used in their explicitly cited local scopes; no new
Mathlib declaration has been checked in this specialization.
