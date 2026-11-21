# Corollary 32c: joint polynomial and logarithmic-moment error tolerances

## Hypotheses

Retain all of C032b's hypotheses: a finite or countable conjugation-invariant
multiset of nonzero complex nodes beta_j, including multiplicity, with
sum_j |beta_j|<=A; the entire multiset lies in the prescribed disjoint
closed sets E_0,E_+,E_- contained in |z|<=B; and E_+ contains at least
one node. In particular A>0 and B>0. Use C032b's exact constructed real
polynomial q and its finite bounds

    deg(q)<=M,     ||q||_{coeff,1}<=C,     Q(q)<=-3/2,
    Q(p)=sum_j beta_j^2 p(beta_j)^2.

Thus M is a nonnegative integer and C is a finite positive real number.
All squares in Q are algebraic squares. For k>=2 define

    S_k=sum_j beta_j^k,       ell_k=-S_k/k.

These are generic node moments, not assumed to be actual-Xi data.
Define the following strictly positive finite constants:

    R=max{1,B},       H_*=AB R^(2M),       N=2M+2,
    tau_c=min{1, 1/[4H_*(2C+1)]},
    tau_ell=1/[4N(C+1)^2].                                  (1)

Supply a real polynomial q_tilde of degree at most M and finite real
numbers ell_tilde_k for EVERY integer 2<=k<=N. Pad the coefficients
c_m of q and c_tilde_m of q_tilde through m=M. Require certified bounds

    delta=sum_{m=0}^M |c_tilde_m-c_m|<=tau_c,
    |ell_tilde_k-ell_k|<=eta<=tau_ell  (2<=k<=N),            (2)

where eta>=0. Obtaining these certificates is an additional input;
the statement does not provide a numerical construction of them.

## Conclusion

Define, with exact finite real arithmetic,

    Q_tilde(q_tilde)=-sum_{m,n=0}^M (m+n+2)
                          c_tilde_m c_tilde_n ell_tilde_(m+n+2).

Then the complete node sum for the rounded polynomial and its
approximate-moment evaluation satisfy respectively

    Q(q_tilde)<=-5/4<0,       Q_tilde(q_tilde)<=-1<0.        (3)

More explicitly the two separate error bounds are

    |Q(q_tilde)-Q(q)|<=H_*(2C delta+delta^2)<=1/4,
    |Q_tilde(q_tilde)-Q(q_tilde)|
                           <=N eta(C+delta)^2<=1/4.        (4)

If finite numerical evaluation returns a real scalar v with a further
certified error |v-Q_tilde(q_tilde)|<=1/4, then v<=-3/4<0.
Exact rational evaluation, when both supplied coefficient and moment
data are rational, incurs zero such additional error. Neither negativity
of an uncertified floating-point value nor a finite head alone suffices.

This is a finite-error specialization of standard bilinear norm bounds,
dated 17 November2026, step1261. Independent audit1263 passed without
changing its hypotheses, constants or proof; the checks are below. It
does not supply actual-Xi support/mass data, a nonreal actual-Xi cluster,
all-degree positivity, feasible precision or an RH conclusion.

## Proof

### Standard tool and scope of the specialization

Use the mixed subordinate norm and its bilinear characterization in
N. J. Higham, [What Is a Matrix Norm?](https://nhigham.com/2021/10/12/what-is-a-matrix-norm/),
12 October2021, section Mixed Subordinate Matrix Norms, Theorems1 and3.
For a finite real matrix T, the norm from l1 to l-infinity is its largest
absolute entry, and duality gives

    |u^t T v|<= (max_{m,n}|T_mn|) ||u||_1 ||v||_1.          (5)

These statements require neither positivity nor invertibility of T.
Zero vectors give zero directly; the nonzero-vector norm quotients in
the cited characterization apply to all other cases. Here the matrices
are finite and real symmetric but can be indefinite. We import this
standard bound; we do not reprove a general perturbation theorem or
use its unrelated positive-semidefinite special case. The required
specialization tracks the moving coefficient vector, the node-mass
entry bound, the power shift by two and the conversion ell_k=-S_k/k.
L895's exact-vector error bound alone would not pay coefficient rounding.

### Generic moments and the complete finite form

Only the generic convergence/finite-expansion argument in L895's proof
is used, not its exact-head interpolation hypotheses or constants.
For clarity, the sharper bounds needed for the supplied B are as follows.
Since |beta_j|<=B and sum_j |beta_j|<=A, for every k>=2,

    sum_j |beta_j|^k<=A B^(k-1).                            (6)

For any fixed polynomial p of degree at most M, it follows that
|p(beta_j)|<=||p||_{coeff,1}R^M and
sum_j |beta_j|^2 |p(beta_j)|^2
<=AB ||p||_{coeff,1}^2 R^(2M)<infinity.
Thus both Q(q) and Q(q_tilde) converge absolutely. Conjugation with
multiplicity and real coefficients makes these sums real, and also
makes each absolutely convergent S_k real. Finite expansion therefore
gives the generic L030-normalized identity

    H_mn=S_(m+n+2)  (0<=m,n<=M),
    Q(p)=p_vec^t H p_vec,                                  (7)

where p_vec is padded through M. This interchanges only a finite
polynomial expansion with absolutely convergent node sums; it drops
no tail or multiplicity. L030's actual-Xi interpretation is not needed.

For 0<=m,n<=M, (6) yields

    |H_mn|<=AB B^(m+n)<=AB R^(2M)=H_*.                      (8)

If 0<B<1, then B^(m+n)<=1=R^(2M). If B>=1, then
B^(m+n)<=B^(2M)=R^(2M). This proves (8) in both cases and at B=1;
replacing its right side by AB^(2M+1) when B<1 would be unjustified.
No internal node separation, node coordinates or cluster count is used.

### Moving polynomial: both cross terms and the error square

Set e=c_tilde-c. Then ||e||_1=delta, ||c||_1<=C, and
||c_tilde||_1<=C+delta. From (7),

    Q(q_tilde)-Q(q)=e^t H c+c^t H e+e^t H e.

Apply (5) to all three terms using (8). This proves the first bound
in (4), including its delta^2 term. Since delta<=tau_c<=1,

    H_*(2C delta+delta^2)
       <=H_*(2C+1)delta<=1/4.                              (9)

Indeed tau_c<=1/[4H_*(2C+1)] regardless of which branch of the
minimum in (1) is active. Applying (9) to C032b's Q(q)<=-3/2 gives
Q(q_tilde)<=-5/4. This controls the exact form of the rounded
polynomial before any moment approximation is used.

### Moving moments and total budget

Put S_tilde_k=-k ell_tilde_k and
H_tilde_mn=S_tilde_(m+n+2). By (2), for every 0<=m,n<=M,

    |H_tilde_mn-H_mn|
       =(m+n+2)|ell_tilde_(m+n+2)-ell_(m+n+2)|<=N eta.     (10)

The smallest index used is 2 and the largest is 2M+2=N. Both endpoints
and every intervening integer in (2) are therefore covered. The given
real data ensure H_tilde is real symmetric. Applying (5) to the SAME
rounded vector on both sides of H_tilde-H gives

    |Q_tilde(q_tilde)-Q(q_tilde)|
       <=N eta ||c_tilde||_1^2
       <=N eta(C+delta)^2
       <=N tau_ell(C+1)^2=1/4.                             (11)

Using C+delta rather than C pays the interaction between polynomial
and moment errors. Equations (9) and (11) telescope through the exact
Q(q_tilde), so the full error relative to Q(q) is at most 1/2; no
additional cross term remains. Consequently

    Q_tilde(q_tilde)<=Q(q_tilde)+1/4<=-1,

proving (3). A further scalar evaluation error at most 1/4 gives
v<=-1+1/4=-3/4, as stated.

All constants in (1) are positive since A,B,C are finite and positive,
M>=0 and R>=1. They are mathematically specified tolerances, not a
precision or complexity guarantee for computing q. The argument allows
zero coefficient error and zero moment error. It also covers M=0
algebraically: (7) is a 1-by-1 form, N=2, and only ell_2 is used.
Leading zero coefficients cause no change. The proof uses the full
closed support and the entire node sum, so boundary nodes, repeated
nodes and an infinite near-zero remainder require no extra estimates.

For actual Xi one would separately need the summability and logarithmic
interpretation from L024/L025 with L018/L026, and independently certified
support, mass and nonreal-cluster data. Those interpretation statements
are not inputs to this generic corollary. A conditional negative
direction does not establish that such data occur for Xi or settle
actual-Xi all-degree signs. QED.

### Independent audit, 17 November2026, step1263

Scope1261 had separate source approval1262 before this audit. The
verification uses its inspected Higham mixed-norm statements, C032b's
audited exact q and finite M,C, and only L895's generic convergence and
fixed-vector moment comparison. No exact-head interpolation, eigenvalue
theorem, node separation or actual-Xi hypothesis is imported. The
specialization and its two budgets pass without a mathematical repair.

**Full sum and entry bound.** Every node copy satisfies
|beta_j|^k<=|beta_j| B^(k-1) for k>=2. Summing gives (6), including
boundary nodes and all multiplicities. On |z|<=B, each monomial z^m
with 0<=m<=M has modulus at most R^M, so the absolute Q-sum is bounded
by AB R^(2M)||p||_{coeff,1}^2. Thus expanding the finite polynomial
inside the sum is justified, and absolute convergence permits conjugate
pairing even for a countable multiset. Fixed real nodes give real terms
individually. Therefore H and Q(p) are real, and (7) includes the full
multiset. For every matrix entry, the actual bound is
AB B^(m+n). If B<1 this is at most AB; if B>=1 it is at most
AB B^(2M). Hence H_* is a valid common bound in every stated case,
including B=1 and M=0. There is no finite-head substitution.

**Coefficient budget.** Higham's l1-to-l-infinity specialization
applies to this finite real H, independently of its signature. The
identity with e=c_tilde-c contains both e^t H c and c^t H e as well
as e^t H e. Their absolute bounds are H_* C delta, H_* C delta and
H_* delta^2, respectively. Since delta<=1, their sum is at most
H_*(2C+1)delta. Write D=4H_*(2C+1)>0. If D>=1, tau_c=1/D pays
at most 1/4; if D<=1, tau_c=1 pays at most D/4<=1/4. Equality of
the branches is harmless. Subtracting this allowance from the exact
negative margin in C032b gives the verified bound Q(q_tilde)<=-5/4.

**Moment and evaluation budgets.** As m,n vary from 0 to M, m+n+2
ranges over every integer from 2 through N, not just the endpoints.
The sign S_k=-k ell_k agrees with the displayed definition of Q_tilde;
the error magnitudes are k times the ell-errors and hence at most
N eta. The rounded vector has norm at most C+delta<=C+1. The same
bilinear bound at that vector gives at most
N eta(C+delta)^2<=N tau_ell(C+1)^2=1/4. This uses the rounded
vector twice and thereby includes the interaction of the two data
errors. Telescoping through Q(q_tilde) yields Q_tilde(q_tilde)<=-1;
the additional scalar allowance yields v<=-3/4. These weak upper
bounds are all strictly negative. No unaccounted cross term remains.

All denominators are positive and finite by the retained hypotheses.
If either error is zero its corresponding allowance vanishes. Padding
leading zero coefficients changes neither norm nor form. For M=0 the
same computation is a scalar form with only ell_2; it does not assert
that C032b must produce degree zero for any given enclosure. These
checks certify conditional sufficient accuracy, not a method of obtaining
the supplied coefficient-distance or moment certificates. Exact rational
finite evaluation has no rounding error only when the supplied data are
rational and arithmetic is exact. A floating-point sign by itself is
insufficient. Full Mathlib coverage remains unchecked.

This is verification of a known-tool specialization,
not a new norm theorem, improved bound or advance beyond the inspected
sources. Actual-Xi data and all-degree signing remain independent gaps.

## Mathlib

Full coverage of this quantitative joint-error corollary has not been
checked; availability is unknown, not asserted absent. No Mathlib
theorem is imported. General finite matrix-norm or polynomial support
would not alone certify C032b's data or the tolerances (1).
