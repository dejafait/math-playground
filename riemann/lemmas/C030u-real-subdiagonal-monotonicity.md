# Corollary C030u: monotonicity of the fixed-real-rate subdiagonal

## Hypotheses

Let m>=1, n>=max(4,2m), and 2<=d<=floor(n/2) be integers. Fix
positive real a_1,...,a_m,r and use C030r's real-reference rate list

    (q_1,...,q_n)=(a_1,a_1,...,a_m,a_m,r,...,r).

All rates remain fixed as the evaluation variable t>0 varies. Repeated
rates, n=2m (no r entries), and arbitrary real-rate contrasts are included.
Let f be the convolution of q_j*exp(-q_j*t)*1_(t>0), and put

    D_k(t)=(-1)^(k*(k-1)/2)*det[f^(u+v)(t)]_(0<=u,v<k),
    D_0=1,
    beta_i(t)=sqrt(D_(i+1)(t)*D_(i-1)(t))/D_i(t).

Use C030r at zero phases: every D_k, 0<=k<=n, is positive for every
t>0. Thus the square root is the positive real one. The beta_i here
is exactly beta_(i,0) of the approved comparison target.

## Conclusion

For every required rank 1<=i<d, beta_i is nonincreasing on (0,infinity).
Consequently, for every x>0,

    beta_(i,0)(t)>=beta_(i,0)(x)>0,       0<t<=x.             (1)

In particular the approved half-value comparison holds on [3*x/4,x].
This supplies C030t's additional premise (H) with c=1, hence also with
c=1/2. C030t's separate reduction and phase conclusion are now verified
in its audit1238; this corollary supplies (H), not that integration proof.

This is the local proof from research attempt1234 under the unchanged
EXPLORE assessment1232/review1233. Independent conceptual audit1236,
under assessment1234/review1235, passes the full stated comparison;
its checks are recorded below. POTENTIALLY_NEW for the original attempt
records only that the assessed bounded source
comparison did not supply the claim; it is not an originality finding.
No finite evolution bound, actual-Xi supply, signing, graph realization,
all-degree positivity or RH candidate is asserted.

## Proof

### Imported determinant interface and necessary specialization

The real determinant formula is S. Sra, *On some positivity properties
of the Riemann Xi function*,
[author-v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.6/(C.10), pp23-25, including coalescing rates; the derivative
coefficient identity is in C.9/(C.22), pp27-28. The assessed accessible
version is also [arXiv2611.02944v1](https://arxiv.org/pdf/2611.02944v1).
C030r establishes the actual normalization, positivity, analyticity
and basis identification, including all determinant ranks up to n.
We use precisely its zero-phase specialization, not a positive-measure
interpretation of the signed derivative functional or the source's
additional moving-frame degree restriction.

For probability Haar measure on U(n), write

    Z_k(t)=integral exp(-t*tr(A*U*P_k*U^*)) dU,
    A=diag(q_1,...,q_n),     G_k(t)=-Z_k'(t)/Z_k(t),
    F_j=product_(h=0)^(j-1) h!,     R=product_j q_j.

Here P_k is any orthogonal projection of rank k; F_0=1. C030r gives

    D_k=R^k*(F_k*F_(n-k)/F_n)*t^(k*(n-k))*Z_k.           (2)

Every rank retains its own positive normalizer Z_k. In particular
D_n=R^n*exp(-t*sum_j q_j), and D_0=1. The fixed-rate functions D_k
are real analytic, strictly positive on (0,infinity).

The source's pointwise upper bound for beta_i is not sufficient to
compare two times. The argument below supplies that additional comparison
using the signed determinant evolution and its endpoints. The brief
determinant differentiation specifies the sign needed for this use;
it does not reprove the imported finite-convolution formula.

### Signed determinant evolution, with both boundary indices

For the proof introduce the same beta_i for every 1<=i<=n-1, even
though only i<d is required in the conclusion. This uses only the
already positive determinants in (2). Set beta_0=beta_n=0 as auxiliary
boundary values; no ratio involving D_(-1) or D_(n+1) is defined.

For tau_i=det[f^(p+q)]_(0<=p,q<i), the Desnanot--Jacobi identity gives

    tau_i*tau_i''-(tau_i')^2=tau_(i+1)*tau_(i-1),
                                      1<=i<=n-1.       (3)

To check the differentiation, differentiating by rows in tau_i leaves
only its last row: every earlier differentiated row duplicates its
successor. Thus tau_i' is the minor with last row index i replacing
i-1. Differentiating that minor by columns leaves only its last column,
so tau_i'' is the minor with both last indices i. In the size i+1
Hankel matrix these are exactly the four single-deletion minors in
Desnanot--Jacobi; the double-deletion minor is tau_(i-1). Symmetry
identifies the two cross minors with tau_i'. For i=1, (3) reads
f*f''-(f')^2=tau_2 with tau_0=1. Hence no boundary derivative or
infinite determinant is being used.

The neighboring signs satisfy
(-1)^((i+1)*i/2+(i-1)*(i-2)/2)=-1. Since D_i differs from tau_i
by its constant sign, (3) gives

    (log D_i)''=-D_(i+1)*D_(i-1)/D_i^2=-beta_i^2.       (4)

The same formula holds at i=0,n with the auxiliary beta values, because
D_0 is constant and log D_n is affine. Define

    v_i=(log beta_i)',                 1<=i<=n-1.

Taking two derivatives in
log beta_i=(log D_(i+1)+log D_(i-1))/2-log D_i yields

    v_i'=beta_i^2-(beta_(i-1)^2+beta_(i+1)^2)/2.

One more derivative, using (beta_j^2)'=2*beta_j^2*v_j, gives

    v_i''=2*beta_i^2*v_i
             -beta_(i-1)^2*v_(i-1)-beta_(i+1)^2*v_(i+1). (5)

At an endpoint the corresponding product is defined to be zero; one
may set v_0=v_n=0. There is no logarithm of a zero boundary beta.
All interior functions in (5) are real analytic on (0,infinity).

### The signs at zero and infinity

The adjacent powers of t in (2) have second difference -2, so

    v_i(t)=-1/t
       -(G_(i+1)(t)-2*G_i(t)+G_(i-1)(t))/2.             (6)

For fixed rates, the energy E_k(U)=tr(A*U*P_k*U^*) is a bounded real
function on U(n), and G_k is its expectation under the positive
weight exp(-t*E_k), with that rank's own normalization. Differentiation
under the integral is justified by bounded energy and compactness, as
in C030r. All G_k are bounded uniformly in t>0 for this one fixed
finite family. It follows from (6) that v_i=-1/t+O(1) as t decreases
to zero, simultaneously for the finitely many i. There is therefore
an epsilon>0, allowed to depend on the fixed family, such that

    v_i(t)<0 for every i and 0<t<=epsilon.              (7)

To obtain the other endpoint, order the rates
q_(1)<=...<=q_(n) and put e_k=sum_(j=1)^k q_(j), e_0=0.
For any rank-k projection Q its diagonal lies in [0,1]^n and sums
to k. The minimum of sum_j q_(j)*Q_jj is e_k. For 1<=k<n this follows
directly by subtracting e_k and using q_(j)<=q_(k) for j<=k and
q_(j)>=q_(k) for j>k: the resulting lower bound is
q_(k)*(sum_j Q_jj-k)=0. The diagonal projection onto the first k
coordinates attains it and belongs to the unitary orbit. The endpoints
k=0,n are constant. Sorting is harmless by unitary invariance.

Here is the exact concentration argument, including repeated rates.
For fixed k and delta>0, continuity supplies an open neighborhood of
a minimizer where E_k<e_k+delta/2. Its Haar probability p_delta is
strictly positive. A nonempty open set in a compact group has positive
Haar measure: otherwise its translates, a finite subcover of the group,
would give total measure zero. Thus

    Z_k(t)>=p_delta*exp(-t*(e_k+delta/2)).

The tilted probability of E_k>=e_k+delta is at most
p_delta^(-1)*exp(-t*delta/2). If M_k=max E_k-e_k, then

    0<=G_k(t)-e_k
       <=delta+M_k*p_delta^(-1)*exp(-t*delta/2).

First letting t tend to infinity and then delta decrease to zero gives
G_k(t)->e_k. The argument requires neither a unique minimizer nor a
positive spectral gap. Equation (6) therefore implies

    v_i(t)->-(q_(i+1)-q_(i))/2<=0.                    (8)

Repeated rates give limit zero. No convergence rate uniform in rates
is required: (7)-(8) will be applied separately to each fixed family.

### Convexity of the sum of positive parts

Set V(t)=sum_(i=1)^(n-1) max(v_i(t),0). We prove that V is convex.
On an interval with no zero of any v_i, let S={i:v_i>0}. It is fixed
there. For j=1,...,n-1 let N_S(j) be the number, at most two, of its
neighbors j-1,j+1 that belong to S and to {1,...,n-1}. Summing (5)
over i in S and collecting the coefficient of each beta_j^2*v_j gives

    V''=sum_(j in S) (2-N_S(j))*beta_j^2*v_j
           -sum_(j not in S) N_S(j)*beta_j^2*v_j >=0.   (9)

Every first-sum term is nonnegative since v_j>0 and N_S(j)<=2.
Every second-sum term is nonnegative since v_j<=0. Endpoint indices
have at most one neighbor and cause no omitted negative contribution.
This is a column-counting argument; it assumes no ordering or
concavity of the beta_j across ranks.

To include the crossing points rigorously, each v_i is real analytic
and is not identically zero by (7). On any compact interval inside
(0,infinity), it consequently has finitely many zeros. Between this
finite collection of zeros, (9) holds. At a zero of a C^1 function v,
the derivative of max(v,0) has a nonnegative jump: at a simple crossing
the jump is |v'|, while if v'=0 both one-sided derivatives are zero.
Thus the one-sided derivative of V can only jump upwards. On each
intervening interval it is nondecreasing by (9). This proves convexity
on every compact interval, hence on (0,infinity).

By (7), V(epsilon)=0. By (8) and the finite number of ranks,
V(T)->0 as T tends to infinity. For any fixed t>epsilon and T>t,
convexity gives

    0<=V(t)<=((T-t)/(T-epsilon))*V(epsilon)
                 +((t-epsilon)/(T-epsilon))*V(T).

The right side tends to zero. Hence V(t)=0 for t>epsilon, and (7)
already gives V=0 below epsilon. Thus v_i<=0 for every interior rank
and every t>0. Since beta_i>0 and beta_i'=beta_i*v_i, each required
beta_i is nonincreasing. This proves (1), including both endpoints
of [3*x/4,x].

### Scope and proof checks

The zero and infinity arguments are not estimates with hidden uniform
onsets: for each arbitrary admissible fixed rate list they force the
exact global sign v_i<=0. The resulting comparison constant 1 is the
same for every family and rank. The proof covers n=2m, all repeated
rates and either sign of every contrast. It uses no lower bound on
beta across families, no change of rates with t, no numerical sample,
and no positive-measure recurrence identification. Only the real orbital
weights used to evaluate G_k are positive. The actual derivative
functional retains its alternating signs, responsible for (4)-(5).

The rounded exploratory script real_scale_1234.py and its full output
under scripts/paired-subdiagonal/ are not proof inputs. The determinant
identity, exact finite evolution, concentration limit and convexity
argument above are the entire mathematical argument for this corollary.
Audit1236 checks these, especially the sign in (5), the collection of
neighbors in (9), and the zero-crossing argument, as recorded below.

### Independent conceptual audit1236

17 November 2026. Verdict: (1) passes under all stated hypotheses,
relative to C030r's established determinant interface. This is an
independent reconstruction of this local proof (REPRODUCTION), not
an independent audit of the cited source theorem or an originality
finding. No hypothesis, constant or mathematical dependency is changed.

First, setting every phase to zero in C030r makes its phase interval
all of (0,infinity). Its determinant statement covers ranks 0 through n,
even though the moving basis is needed only through dimension d.
Thus all auxiliary beta_i, 1<=i<n, are positive. The positive analytic
square root and logarithm are real analytic locally on that interval.
No polynomial of degree n or nonzero determinant of size n+1 is needed.
At rank n, (2) has factorial ratio 1 and t exponent 0, and P_n=I
gives D_n=R^n*exp(-t*sum q_j). At rank 0 it gives D_0=1.

For an independent check of (3), take the matrix with row and column
indices 0,...,i. Deleting row i and column i gives tau_i; deleting
row i-1 and column i-1 gives tau_i''. The two cross deletions give
tau_i', and deleting both final rows and columns gives tau_(i-1).
The identification of tau_i'' is valid because after differentiating
tau_i by rows, its columns still have consecutive derivative indices;
all but the last column derivative duplicate the following column.
Desnanot--Jacobi therefore gives exactly (3), including i=1 with the
empty determinant equal to 1. The sign exponent on its right side is
i*(i+1)/2+(i-1)*(i-2)/2=i*i-i+1, which is odd. Dividing by the
positive D_i^2 gives (4) with the minus sign.

Twice differentiating log beta_i gives

    v_i'=beta_i^2-(beta_(i-1)^2+beta_(i+1)^2)/2.

Differentiating again gives (5), since (beta_j^2)'=2*beta_j^2*v_j
at every interior rank. At each edge the missing term is the derivative
of the identically zero boundary square. Assigning v_0=v_n=0 is only
notation for this zero product, not a logarithmic derivative of zero.
This independently checks every coefficient and both end equations.

In (2), the exponent p_k=k*(n-k) has
p_(i+1)-2*p_i+p_(i-1)=-2. Every other non-orbital factor is constant
in t. Since Z_k'/Z_k=-G_k, this reproduces (6). For each fixed rate
list, all rank-k energies lie between k*min q_j and k*max q_j.
The resulting finite common bound for the G_k makes the -1/t term
dominate simultaneously for all n-1 ranks near zero, proving (7).
This requires no lower bound on a gap between rates.

At infinity, the diagonal-projection argument proves that e_k is an
attained minimum on the full orbit, including when the ordered rates
coincide. The open set used in the concentration proof has positive
Haar mass: its translates cover U(n), and compactness gives a finite
subcover, ruling out zero mass. Its lower bound for Z_k and the bound
on the complementary tilted mass give the displayed estimate for
G_k-e_k. Taking t to infinity before delta to zero is legitimate for
each fixed k and rate list. The constant-rank endpoints are exact.
Thus G_k tends to e_k and (6) gives (8), with value zero at every
repeated-rate gap. No isolated minimizer or uniform convergence rate
is assumed. Finiteness of the ranks gives V(T)->0.

For (9), each column j of (5) contributes

    [2*1_(j in S)-N_S(j)]*beta_j^2*v_j.

If j belongs to S the bracket is nonnegative; if not, it is
nonpositive and v_j<=0. This covers isolated positive indices,
consecutive blocks, the entire interior chain and its two ends.
It does not require diagonal dominance with unequal row weights.
Analyticity and (7) exclude an identically zero v_i, so the union of
their zeros on any compact subinterval is finite. At a crossing with
v_i'>0 the positive-part slope jumps from 0 to v_i'; with v_i'<0
it jumps from v_i' to 0. When v_i'=0 both slopes are zero, including
higher-order crossings and tangencies. Simultaneous crossings add
only nonnegative jumps. Combined with (9) between zeros, this proves
convexity on each compact subinterval and hence on (0,infinity).

Finally fix the common epsilon from (7) and any t>epsilon. The chord
inequality holds on [epsilon,T] for every T>t; V(epsilon)=0 and
V(T)->0 force V(t)=0. Together with (7), this gives v_i<=0 everywhere.
Since beta_i'=beta_i*v_i and beta_i>0, ordinary integration gives
(1) for every 0<t<=x. All endpoint arguments were performed within
one arbitrary fixed family; the resulting constant 1 is independent
of that family without exchanging a family limit with a time limit.
In particular n=2m, all contrasts and all multiplicities are retained.

C030t(H) is therefore supplied with c=1; C030t itself was not audited
in this step and its phase conclusion is not promoted. Its conditional
wording predates this result. C030q and C030t are not additional inputs
to the present proof. The parked joint route and the independent finite
evolution, actual-Xi, degree/time, complement, signing and realization
gaps are unaffected. The exploratory numerical file was not replayed:
no part of this verdict relies on its rounded values.

## Mathlib

Full matching coverage of this monotonicity statement and the cited
finite-convolution determinant identity is unchecked; no absence claim
is made. Supporting mathematics includes Desnanot--Jacobi, finite
analytic functions, compact-group Haar measure, elementary Laplace
concentration and convexity from a nondecreasing one-sided derivative.
Exact supporting Mathlib theorem names were not checked, and no formal
verification is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
