# L120 — Full included-anchor reduction and inconclusive global comparison

## Hypotheses

Use exactly L021's canonical positive rational primal vector a_i and
L098,L112–L114's fixed data on V, the 68-subsets of a 1024-point set:

    N=floor(65537^28/2^128)+1, H=binomial(1024,68), rho=N/H,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i), 5<=i<=68.

In particular N>1, rho>0, a_i>0, sum a_i=U-1, and
sum_i g_i*c_i=N. Write d(B,C)=|B\C|. Use L112's original box:
if q_k and p_k are its saved `point[k]` and `scale_powers[k]`, k=i-5,

    l_i=10^p_k*(q_k-10^25)/10^70,
    u_i=10^p_k*(q_k+10^25)/10^70, 5<=i<=68.

All 64 pairs of endpoints are positive and unchanged. Define normalized
moments y on nonempty sets of at most three supports: y({B})=1,
y({B,C})=c_d(B,C), and for three distinct supports use zero if any
side is 1,...,4, and x_i*x_j*x_h otherwise. Repetitions are evaluated
as sets, so sides (0,b,b) give c_b, including the all-equal value 1.
The homogeneous moment is rho*y. There is no extra incidence zero.

The interval statements below hold for every x in this box. Statements
using exact cardinality are restricted to L112's enclosed root x, where
all L098 contractions sum_(Z in V)y({A,B,Z})=N*c_d(A,B) hold.
No full source PSD, measure, global root uniqueness or RS realization
is assumed.

## Conclusion

Fix A in V and let W={B in V:5<=d(A,B)<=68}. Divide the included-anchor
union matrix, indexed by {A} and all {A,B} for B!=A, by rho. All
rows with 1<=d(A,B)<=4 are zero. After their deletion it is

    M=[[1,b^T],[b,C]],   b_B=c_d(A,B).

Let K be the global matrix on V with diagonal zero and off-diagonal
coefficient zero at distances 1,...,4 and x_i at distances i>=5.
Put D_BB=x_d(A,B)>0 and Delta_BB=c_d(A,B)/x_d(A,B)^2. Then

    C=D*(K[W]+Delta)*D.                                  (1)

At the exact root, C*1=(N-1)b and sum_B b_B=N-1. Consequently
M>=0 if and only if C>=0, even if C is singular. The full matrix has
the null vector (-(N-1),1_W), extended by zeros on deleted rows.

The standard global spectral comparison gives the sufficient test

    L(x):=min_(0<=j<=68) lambda_j(K)
                         +min_(5<=i<=68)c_i/x_i^2 >=0.   (2)

Complete signed interval evaluation at the unchanged box is inconclusive:
the computed enclosure [L_-,L_+] satisfies L_-<0<L_+. It therefore
neither certifies (2) nor refutes it. With the positive rational
reference R=c_5/u_5^2, the exact outward grid endpoints are

    floor(10^6*L_-/R)=-11660741035356041112426863955343247787961878293817116679,
    ceil(10^6*L_+/R)=630870.

These are endpoints for the enclosure of the sufficient comparison,
not eigenvalue bounds proving a negative matrix direction. This is a
REPRODUCTION of known spectral, interval and singular-Schur methods.
The prescribed straddle stop applies: no refinement, retuning, midpoint
verdict or alternate root. Full included-anchor PSD, excluded-anchor PSD,
stronger distribution constraints and realization remain unresolved;
there is no improvement to the 955–957 bracket. The separate critical
review below retains this reduction and the inconclusive comparison.

A subsequent fixed residual-corrected centered-form test at the same
root is also inconclusive. With the unchanged reference R0=R above,
its enclosure for (lambda_1(K(x*))+R0)/R0 lies within

    [-8460928885,8462190625]/10^6.

The complete enclosure strictly straddles zero. This one estimate is
parked, without a root-functional sign or full PSD conclusion. Its
specialization and independent arithmetic evidence are below; the
earlier critical review does not certify this subsequent addition.

## Proof

**Known imports and applicability.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-full-product-johnson-kernel-comparison.md`.
For the union matrix import Polak, *Semidefinite Programming Bounds for
Constant-Weight Codes*, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
§1.1 (1)–(3), Proposition 1.1 and its indicator proof, p.2. Use its
proved constant-weight conclusion, retaining the printed A(n,d)
qualification recorded in foundations/12. At order three a singleton
anchor allows exactly the two-element extensions used here. This is
necessity for code indicators, not sufficiency for a measure or an RS list.

Import the global Johnson relation eigenvalues and common decomposition
from Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), §§1.2,3,
pp.3,10, and Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
§11.2 pp.162–163. Here 1024>=2*68. For principal interlacing and
the additive least-eigenvalue inequality import the latter book's
§2.4, Theorem 2.5.1(i), Corollary 2.5.2 and Theorem 2.8.1(ii),
pp.33–36. All matrices are finite real symmetric; the diagonal
perturbation need not commute with the kernel.

Import the singular-Schur criterion from Boyd–Vandenberghe,
*Convex Optimization*, [author book](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
§§A.5.4–A.5.5, pp.648–651: [[C,b],[b^T,1]] is PSD precisely when
C>=0, b lies in range C, and 1-b^T*C^dagger*b>=0. Foundations/09
records the inspected singular and unbounded cases. No inverse or
positive definiteness of C is presumed. Import interval-expression
inclusion from Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica 19 (2010), 287–449,
DOI [10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
§5.5 (5.16)–(5.17), author p.28; foundations/14 records coverage.
These theorems are imported without reproof. The following entrywise,
cardinality and finite-coefficient checks are the needed specialization.

**Zero rows and entrywise congruence.** For B at forbidden distance from
A the anchor entry and diagonal are c_d(A,B)=0. If C is distinct from
A,B, the triple contains that forbidden side and is zero. If C=A or B,
the repeated moment is the same zero pair moment. Thus every such row
is zero before deletion; no division by a forbidden c_i is used.
The case B=A duplicates the singleton index {A} and is retained only
as the anchor, without introducing an x_0.

For B in W the Boolean diagonal is c_d(A,B). For different B,C in W,
their entry is zero at a forbidden B,C distance, and otherwise equals
x_d(A,B)*x_d(A,C)*x_d(B,C). The diagonal of K is zero. Multiplication
by D on both sides therefore gives every off-diagonal entry, and
D_BB^2*Delta_BB=c_d(A,B) gives the diagonal. This proves (1) for
all actual supports, including every possible t-s, without orbit
averaging or a cardinality hypothesis. Every i=5,...,68 occurs in W
with g_i>0, so the minimum diagonal correction is exactly the second
minimum in (2). Principal interlacing and the additive bound give

    lambda_min(K[W]+Delta)>=lambda_min(K)+lambda_min(Delta)=L(x).

Positive diagonal congruence gives C>=0 whenever (2) holds.

**Exact-root anchor range and scalar.** For fixed B in W, the exact
contraction includes Z=A with contribution b_B; all forbidden Z rows
are zero. The sum over Z in W is C*1, and it retains Z=B with its
Boolean contribution b_B. Therefore

    C*1=N*b-b=(N-1)*b.

The coincident contraction and the canonical pair sum give
sum_(B in W)b_B=sum_(i=5)^68 g_i*c_i=N-1. Hence
v=1_W/(N-1) satisfies Cv=b and b^T v=1. This proves the range
condition even before assuming PSD. If C>=0, C^dagger*b is another
solution; their difference is in ker C, which is orthogonal to range C
because C is symmetric. Consequently b^T*C^dagger*b=b^T*v=1.
The singular-Schur scalar is exactly zero. The cited criterion yields
M>=0; necessity follows by principal restriction. Also direct block
multiplication gives M*(-(N-1),1_W)=0. Restoring zero rows and the
positive scalar rho preserves PSD and this null vector. These identities
use the contractions at the root and are not asserted on the entire box.

**Every global mode and original endpoint.** With out-of-range binomials
zero, the imported Eberlein entries, multiplicities and spectrum are

    P_j(i)=sum_(h=0)^i (-1)^h binom(j,h)
                            binom(68-j,i-h)binom(956-j,i-h),
    m_j=binom(1024,j)-binom(1024,j-1)>0,
    lambda_j(K)=sum_(i=5)^68 P_j(i)*x_i, 0<=j<=68.

The multiplicities sum to H and P_0(i)=g_i; the constant mode is
included. For every integer coefficient use l_i in its lower signed
sum if P_j(i)>=0 and u_i otherwise; reverse these choices for its
upper sum. Denote the resulting endpoints by alpha_j,beta_j.
Monotonicity on positive x_i gives

    delta_i^-=c_i/u_i^2 <= c_i/x_i^2 <= c_i/l_i^2=delta_i^+.

Finite minima are enclosed by the minima of lower and upper endpoints:

    L_-=min_j alpha_j+min_i delta_i^-,
    L_+=min_j beta_j+min_i delta_i^+.

This enclosure remains valid with correlated coordinates; no independent
attainment of its separate minima is assumed. Its lower spectral
minimizer is j=1, its upper spectral minimizer is j=64, and both
correction minimizers are i=5. Exact rational comparisons give the strict
straddle and outward grid endpoints stated above. A negative lower
endpoint is not evidence of a negative eigenvalue or of failure of (2).
The positive upper endpoint likewise does not certify (2).

**Complete evidence and stopping decision.** Reproduce from this notebook:

    python3 scripts/finite-support/full_product_global_comparison.py
    python3 scripts/finite-support/verify_full_product_global_comparison.py

Full rational certificates are saved at
`scripts/finite-support/full-product-global-comparison.json` and
`scripts/finite-support/full-product-global-comparison-verification.json`.
The constructor performs 165 checks; the independent verifier performs
5206, with zero failures. The verifier imports no constructor routine.
It reconstructs all 4761 integer P_j(i) as coefficients of

    (1-z)^j * sum_(r=0)^(68-j) binom(68-j,r)binom(956-j,r) z^r

by repeated polynomial multiplication. It independently computes the
binomials using factorials, every multiplicity, all 69 coefficient traces
sum_j m_j P_j(i)=H*1_(i=0), all signed sums, all 64 corrections, both
minima and both comparison endpoints. It reconstructs every original
point, scale and endpoint and checks the retained root status, all 64
strict inclusion margins, canonical pairs and prior audit hash bindings.
This consumes the already audited root input rather than rerunning its
nonlinear solve. The complete entrywise proof above handles actual
supports; no finite representative preview is substituted for it.

The straddle ends this approved test without refinement. ATTEMPTS/098's
different shell test remains stopped. This arithmetic verification is
not a dedicated critical review of the new manuscript and criterion.

**Separate critical review (2026-10-24, step 455).** The unchanged
SPECIALIZE assessment is
`drafts/literature/2026-10-24-l120-global-reduction-critical-audit.md`.
The review retains the stated reduction and comparison, without a
mathematical repair, new PSD conclusion or claim beyond the assessed
sources. It supersedes historical pending-review wording for L120 in
the overview. All direct mathematical inputs are unchanged.

The source index condition at order three and singleton anchor A allows
exactly {A} and {A,B}, B!=A. Their unions have at most three supports.
Dividing by rho>0 therefore produces precisely the displayed M, including
its anchor value one. No empty index or duplicate {A,A} is added. The
entrywise proof covers every actual support: Boolean coincidence gives
c_i rather than x_i squared times x_0; a forbidden anchor pair makes
the entire row zero even at coincidence; a forbidden opposite pair
makes only that off-diagonal entry zero. Thus deleting zero rows and
using positive D is valid, without assuming PSD to deduce the zeros.
The algebra is for this prescribed product assignment and needs no
permutation averaging of labeled RS constraints.

The additional auditor constructs an explicit 1024-point representative
for every four-region occupancy from L112. With A={0,...,67} and
B={0,...,67-i} union {68,...,67+i}, a third support selects r,a,b,o
points from the common, A-only, B-only and outside regions, respectively,
where o=68-r-a-b. Empty intervals here denote empty sets. Its actual
bitsets give j=68-r-a and h=68-r-b. It evaluates the moment from the
set of distinct supports and compares it to the appropriate reduced
matrix entry, retaining all original t,s through their bijection
t=i-a, s=b. It checks all 1,500,625 cases: 129 singleton-anchor cases,
6,896 forbidden-anchor-row cases, 64 Boolean diagonals, 3,336 forbidden
opposite-pair cases and 1,490,200 product off-diagonals. The categories
are disjoint; repeated forbidden entries belong to the zero-row cases.
This finite reconstruction supports, rather than replaces, the universal
entrywise proof above.

For every fixed i the auditor reconstructs each positive integer D and
all third-support shell totals g_j. The 205 repetitions are retained:
69 at i=0 and exactly two with D=1 for every i>0. Aggregating the
permitted distinct entries reproduces all 81,355 coefficients of
L112's exact root equations. In the lower block C, Z=A is absent and
Z=B is present. Consequently its row sum at the root is
(N-2)c_i+c_i=(N-1)c_i, not Nc_i or (N-2)c_i. Canonical pair
normalization gives sum_B b_B=N-1. Neither equality is obtained by
evaluating at the saved numerical point or asserted throughout the box.

For singular C the proof supplies the explicit solution
v=1_W/(N-1) of Cv=b; N>1 licenses the division. Symmetry gives
ker(C) perpendicular to range(C), so b^T v=1 is the correct
generalized-Schur scalar calculation whenever C is PSD. Positive
diagonal entries are never used to infer invertibility. Multiplication
of both block rows verifies the displayed null vector, which is
nonzero even after restoring deleted rows. These observations verify
both directions of the PSD equivalence, including a singular lower
block, without claiming that C actually is PSD.

The auditor replays the complete independent comparison verifier to
`scripts/finite-support/l120-critical-reverification.json`. All 5,206
checks pass and every output field equals the original verification
certificate. This reconstructs every one of the 4,761 coefficients,
all 69 modes and positive multiplicities, all 64 original endpoints
and corrections, dimension and trace identities, and both complete
comparison fractions. The cited Johnson theorem applies because
1024>=2*68; no single-relation minimum replaces the weighted spectrum.
The principal restriction W is nonempty. The diagonal correction need
not commute with that restriction for the imported additive inequality.

As a separate check of the same signed interval sums, the auditor
expands each endpoint as the weighted sum of coordinate centers plus
or minus the sum of absolute coefficients times coordinate radii.
Every endpoint agrees exactly with the original expression. This is
an algebraic identity check, not a midpoint sign verdict, alternate
enclosure or refinement. All 64 original points, scales and box
endpoints are preserved. The full rational lower and upper comparison
endpoints from both certificates were inspected; their positive
denominators and strict signs agree. Exact integer cross-products
verify the stated floor and ceiling, including the negative lower
endpoint. The lower and upper minimizers differ, as recorded; no
simultaneous attainment is inferred. The result remains only an
enclosure of a sufficient lower comparison, not a matrix eigenvalue
or a negative direction.

Reproduce without any constructor or nonlinear solve:

    python3 scripts/finite-support/critical_audit_l120.py

The complete additional certificate is
`scripts/finite-support/l120-critical-audit.json`, with all reconstructed
contraction coefficients, repetition rows, signed endpoints, both full
comparison fractions, input/replay hashes and check counts. Its
3,001,736 additional checks pass with zero failures. The audited
L112/L113 root and L114 scalar result are reused with their unchanged
evidence; their nonlinear enclosure and scalar proofs are not claimed
newly established by hash checks. No complete candidate follows.
ATTEMPTS/098–099 remain stopped. Full included/excluded-anchor PSD,
stronger distributions, global uniqueness, measures, packing and RS
realization remain unresolved, as does arbitrary-center 67/68 safety.

**Residual-corrected mode-one test (2026-10-24, step 457).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-24-root-residual-mode-one-functional.md`, with
exactly this pre-existing COVERED_TARGET. Import Rump, the paper and
corrected author PDF cited above, Theorem 13.1, (13.1)–(13.4), author
pp.87–88, and §11.6 (11.10), p.84. Foundations/14 records the inspected
full row-wise proof and integral variant (13.6). This theorem encloses
f(v) by f(a)+J(v-a) when J contains all derivatives on the segment;
a scalar function is covered by adjoining zero output components.
It needs neither a common intermediate Jacobian point nor an exact
adjoint. Import it without reproof; no narrowness guarantee is imported.

Write C for L112's saved rational preconditioner and R0=c_5/u_5^2>0
for the scalar reference. Put v_i=x_i/s_i using L112's unchanged scales,
point a and normalized box B=a+E, with every E_i=[-r,r], r=10^-45.
The system remains precisely L112's 64 equations

    F_i(v)=-1+sum_(j<=h) b_(i,j,h)*v_i*v_j*v_h,
    b_(i,j,h)=A_(i,j,h)*s_i*s_j*s_h/((N-2)*c_i).

All 81,355 entries are retained. Set exactly

    w_i=P_1(i)*s_i/R0, z=C^T*w,
    G(v)=1+w^T*v,     h(v)=G(v)-z^T*F(v).

The applicable Johnson formula gives
G(v*)=(lambda_1(K(x*))+R0)/R0 at the retained root. Since F(v*)=0,
h(v*)=G(v*). Neither F(a)=0 nor J_F(a)^T*z=w is presumed; their
entire residual and derivative defects must remain in the enclosure.
For every nondecreasing coordinate triple tau collect exactly

    q_tau=-sum_(i,j,h:sort(i,j,h)=tau) z_i*b_(i,j,h).

There are 28,215 such triples. With m_k(tau) the number of occurrences
of k, polynomial expansion and differentiation give the identities

    h(v)=1+sum_i z_i+sum_i w_i*v_i
                         +sum_tau q_tau*prod_(t in tau) v_t,
    partial_k h(v)=w_k+sum_(tau:k in tau) m_k(tau)*q_tau
                            *prod_(t in tau with one k removed) v_t.

The constant includes all residual -1 terms. Every factor occurrence
is differentiated, including squares and cubes; exactly two factors
remain after removing one occurrence. Signed coefficients are collected
before interval evaluation. These are finite polynomial identities,
without an inferred exact-adjoint cancellation.

Let H_a enclose h(a) and D_k enclose partial_k h throughout the full
original B. The polynomial is continuously differentiable on R^64,
B is convex, and a,v* belong to B. The imported mean-value theorem gives

    (lambda_1(K(x*))+R0)/R0 in H_a+sum_k D_k*[-r,r].       (3)

This uses the original error box; no Krawczyk-image iteration, smaller
coordinate enclosure, updated point, weight change or new root is used.

Every q_tau,w_i,z_i and the constant are formed as exact rational numbers.
For arithmetic only, fix T=10^120 and enclose q by
[floor(T*q),ceil(T*q)]/T. Both original point and box already lie
exactly on this grid. Addition sums endpoints. Multiplication takes
all four integer endpoint products and divides their minimum downward
and maximum upward by T, also at negative endpoints. Evaluate the full
collected cubic at a and each full quadratic derivative on B with these
outward operations. All 64 products D_k*[-r,r] are retained in (3).
Changing the arithmetic grid does not change any mathematical input.

The constructor saves the complete w,z, constant, exact cubic
coefficients and their outward bounds, all derivative occurrences,
all 64 D_k, H_a, the error sum and the full final rational interval.
Its complete lower endpoint is negative and upper endpoint positive.
Exact comparisons give floor(10^6*lower)=-8460928885 and
ceil(10^6*upper)=8462190625. Thus (3) supplies no sign certificate.
This does not prove that the actual functional has either sign.

The independent checker imports no constructor routines. It checks all
input/audit bindings, reconstructs canonical c_i,N,H,rho, every original
endpoint and every saved-preconditioner weight. Independently,

    P_1(i)=binom(67,i)*binom(955,i)
                          -binom(67,i-1)*binom(955,i-1).

It reconstructs all 81,355 exact b coefficients from the unchanged
integer A array, consuming its full actual-union reconstruction from
the retained L120 audit. It sums all 64 source-row residuals exactly
and compares each to the L112/L113 audit. It independently collects
every cubic from source-row contributions and differentiates the three
source factors separately before collection. This checks all 28,215
q_tau and every repeated-factor derivative occurrence. Each coefficient
bound is verified directly, with each endpoint error less than 1/T.

Independently of the constructor's rounded operation order, the checker
computes h(a)=1+w^T*a-z^T*F(a) as an exact rational. It computes full
signed quadratic derivative endpoint sums as exact rationals: B is
positive, so each remaining two-factor product is bounded by its
lower/lower and upper/upper products, also when the factors coincide.
Each exact natural derivative interval lies in the saved D_k. It checks
the exact error r*sum_k max(abs(D_k.lower),abs(D_k.upper)) against the
saved error sum, then the full (3), both strict signs and both grid
comparisons. No point-value sign, sampling or preview gives the verdict.

Reproduce without solving or changing any input:

    python3 scripts/finite-support/root_residual_functional.py
    python3 scripts/finite-support/verify_root_residual_functional.py

The full certificate is `scripts/finite-support/root-residual-functional.json.gz`;
the independent evidence is
`scripts/finite-support/root-residual-functional-verification.json`.
All 56,821 independent checks pass, with zero failures. Both complete
result fractions and error fractions were inspected. The working record
is `drafts/2026-10-24-root-residual-functional-working.md`;
ATTEMPTS/100 records the stop. This is a reproduction of known
mean-value/interval methods and inconclusive exploration, without
progress beyond the assessed sources. A separate critical review of
this addition is not claimed. The strict straddle parks this estimate
without retuning, higher-order rescue, refinement or midpoint verdict.
ATTEMPTS/098–099 retain their earlier distinct failures. Other modes,
full included/excluded PSD, stronger distributions, global uniqueness,
measures, packing, RS realization and the 955–957 boundary remain open.

**Fixed actual-principal Rayleigh test (step 459).** This separate
addition consumes the audited entrywise reduction above; the previous
critical audit does not certify this new calculation. The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-24-actual-principal-fixed-rayleigh-test.md`.
Retain all hypotheses above and all original L112 data. On the actual
lower block C, fix A={0,...,67} and

    v_B=1_(0 in B)-1_(1 in B), B in W.

Import the finite real-symmetric Rayleigh criterion from
Brouwer–Haemers, *Spectra of Graphs*, the same
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
§2.4, printed p.33, including its orthonormal-eigenvector expansion:
a negative quadratic value for a nonzero vector implies a negative
eigenvalue. This covers singular matrices. No global eigenvector
claim or reproof is used. Import enclosing-expression arithmetic from
Rump, the citation above, §5.5 (5.16)–(5.17), author p.28. The
following count is the assignment-specific specialization not supplied
by either source.

Only supports containing exactly one of 0,1 have nonzero v_B. For
5<=i<=67 each marked sign class at d(A,B)=i has size

    n_i=binom(66,67-i)binom(956,i)>0.

At i=68 both sign classes are empty, since B avoids all of A.
The remaining supports in every layer have v_B=0 and contribute zero
to every quadratic summand. This accounts for full W, including its
boundary; it is not a deletion of nonzero vector coordinates. In
particular v is nonzero and ||v||^2=2*sum_(i=5)^67 n_i.

Fix a positive-sign B in layer i. Its four unmarked regions, in the
order (A intersect B) minus {0}, A minus (B union {1}), B minus A,
and outside A union B, have sizes 67-i,i-1,i,956-i. A positive-sign
C in layer j selects a,b,p,q points respectively, where
b=67-j-a and q=j-p. Its B-intersection has size 1+a+p and hence
h=d(B,C)=67-a-p. A negative-sign C has the identical unmarked choices
but no marked intersection with B, so its opposite distance is h+1.
Define, with zero out-of-range binomials and f_ij outside 0,...,68 zero,

    f_ij(h)=sum_(a,p:67-a-p=h)
       binom(67-i,a)binom(i-1,67-j-a)
       *binom(i,p)binom(956-i,j-p).

The precise nonzero summation ranges are
max(0,68-i-j)<=a<=min(67-i,67-j),
max(0,j-(956-i))<=p<=min(i,j).
They exhaust the choices bijectively. Thus sum_h f_ij(h)=n_j,
f_ij(0)=1_(i=j), and f_ij(68)=0. Simultaneously exchanging the two
marked points reverses both signs and preserves all distances and
matrix entries. Unmarked permutations within A and its complement
also preserve those entries, directly from the displayed definition
of C. These are ordinary support-counting symmetries, without any
RS-label averaging. The complete ordered signed coefficient is

    S_ijh=2*n_i*(f_ij(h)-f_ij(h-1)).

It counts both B signs and both C signs; no division by two or six
is appropriate. The h=0 entries are precisely coincidences, with
S_ij0=2*n_i*1_(i=j); their value is c_i, not a product. Entries with
1<=h<=4 are zero by the forbidden-pair rule. Therefore exactly

    Q(x):=v^T C v
       =D0+sum_(i,j=5)^67 sum_(h=5)^68 S_ijh*x_i*x_j*x_h,
    D0=2*sum_(i=5)^67 n_i*c_i>0.                         (4)

For every sorted cubic key t collect the integer
w_t=sum_(sort(i,j,h)=t) S_ijh before enclosing. Repeated indices
are retained. Let L_t be the product of the original lower endpoints
for t and U_t the product of the original upper endpoints. Positivity
of all endpoints gives the exact rational enclosure

    Q_-=D0+sum_(w_t>0) w_t*L_t+sum_(w_t<0) w_t*U_t,
    Q_+=D0+sum_(w_t>0) w_t*U_t+sum_(w_t<0) w_t*L_t.       (5)

No coordinate endpoint is changed and no preconditioner or root solve
is used. There are 28,151 nonzero collected cubics. Complete exact
evaluation gives Q_-<0<Q_+, with outward normalized grid endpoints

    floor(10^6*Q_-/D0)=-21799306934180908892628472930423400592200286549410520871,
    ceil(10^6*Q_+/D0)=21799306934180908892628472930427308209361609554273837832.

Consequently this enclosure neither supplies a negative direction nor
certifies this vector's quadratic value nonnegative. It is not an
eigenvalue enclosure or a PSD verdict. The straddle parks this vector
and estimate, with no refinement, second vector, D-inverse transform,
midpoint verdict or retuning.

**Complete independent reconstruction for (4)–(5).** The constructor
fixes B and uses the four binomials defining f. Independently, first
select the common unmarked anchor cell a, then B-only and C-only
cells. Their global multiplicity is

    binom(66,a)binom(66-a,67-i-a)binom(i-1,67-j-a).

Selecting the common outside cell p, then the outside B-only and
C-only cells, gives

    binom(956,p)binom(956-p,i-p)binom(956-i,j-p).

Their product times two counts the two equal-sign marked assignments
at h=67-a-p; the two opposite-sign assignments have the same count
at h+1. This independently reconstructs every unsigned and signed
count for all 3,969 ordered layer pairs and all 69 opposite distances.
Complete counts agree with the fixed-B formula, including coincidence,
zero signed totals, transposes and both boundary distances. A separate
direct enumeration of all ordered pairs among the 126 four-subsets
of a nine-set checks every i,j,h cell, including the zero vector
coordinates and both marked cases, against this global-cell formula.
This small check supplements, rather than replaces, the full exact
1024-point reconstruction.

The independent verifier reconstructs canonical c_i,N,H,rho from
L021, checks all 64 original endpoint pairs and strict root margins,
binds every retained audit input, and compares all 81,355 contraction
coefficients to the retained L120 audit. Hash binding of the root
certificate preserves its equations, point, scales, box and
preconditioner. Every collected coefficient and both complete rational
term endpoints in (5) are independently checked; positive and negative
partial sums are accumulated separately. Both full normalized result
fractions were inspected, not merely previews.

Reproduction commands (relative to this notebook):

    python3 scripts/finite-support/actual_principal_rayleigh.py
    python3 scripts/finite-support/verify_actual_principal_rayleigh.py

Full counts, coefficients and rational endpoints are in
`scripts/finite-support/actual-principal-rayleigh.json.gz`;
independent evidence is
`scripts/finite-support/actual-principal-rayleigh-verification.json`.
All 898,038 independent checks pass with zero failures. This is an
inconclusive reproduction of assessed finite-counting and Rayleigh
methods, without progress beyond the sources checked or a new lemma
claim. Separate critical proof review of this addition remains open.
Full/excluded PSD, stronger distributions, global uniqueness, measures,
packing, RS realization and the 955–957 boundary remain unresolved.

## Mathlib

Full matching specialization and global comparison: not checked.
Supporting Johnson spectral, interlacing, additive spectral and singular
Schur theorems: not checked. Unknown availability is not evidence of
absence. No formal verification or new theorem beyond the checked
source scope is claimed.

For the residual-functional addition, supporting
`Convex.norm_image_sub_le_of_norm_fderiv_le` and its primed variant are
recorded with direct links in foundations/14. Full matching coverage
for the interval-functional certificate is not checked. These supporting
declarations do not constitute a formal verification of (3).

Full matching Mathlib coverage for the marked-coordinate count and
fixed actual-principal Rayleigh specialization (4)–(5) was not checked.
Unknown availability is not evidence of absence; the independent
arithmetic checks are not Lean verification.
