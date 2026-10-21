# L176 — Prefix covariance replacement and cubic-scale mass removal

## Hypotheses

Keep precisely L175's hypotheses and conventions: SU(2), relative box
(-4,4)^4, a=8/N through admitted even meshes, straight direction-1
lower-rooted forest, complete compact displacement, both actual L010
probes i=3,6 at tau=1/16, and bare expansion at fixed mesh before
refinement. All matrices use ordinary stored coordinates. In particular
F=Phi Sigma, K=Phi Sigma Phi^T, and A^gen is L175(1)'s full symmetric
generator form. Keep its compact support, both generator orientations,
the exact multipliers m_(j,l) from q_l=L h_l, and L175's signs for J_j
and endpoint sum S. The full action column, all normal end links and
all exterior heat modes are retained.

On axial interior vertices let M_st=min(s,t). On transverse interior
vertices let Delta_T be the unscaled scalar Dirichlet Laplacian and
G=Delta_T^(-1). Write

    Y=M tensor G,
    G_epsilon=(Delta_T+epsilon I)^(-1),
    Y_epsilon=M tensor G_epsilon,       0<epsilon<=1.       (1)

The mass epsilon is dimensionless. It is inserted only in the G factor
of the left covariance in the trace below. It does not change F,
Sigma, the action column, the physical heat weights or any field law.

## Conclusion

For a vertex matrix H define the linear signed trace functional

    T_i(H)=-6 sum_(k,l) c_(i;kl) sum_(j=2)^4
            Tr[H m_(j,l) J_j F A^gen M_(h_k) S].          (2)

Thus L175's W_i is T_i(K). Define W_i^0=T_i(Y) and
W_i^epsilon=T_i(Y_epsilon). Constants below depend on the actual probe
and displacement but not N or epsilon. Then

    |V_i-W_i^0| <= C_i N^(5/2) sqrt(log(eN)),
    |W_i^0-W_i^epsilon| <= C_i N^3 epsilon^(1/4).         (3)

In particular

    limsup_(N->infinity) |a^3(V_i-W_i^epsilon)|
                           <= C_i epsilon^(1/4).        (4)

This removes the resolvent correction in K at cubic scale and gives
a uniform mass-removal estimate for its remaining transverse inverse.
It does not establish a fixed-epsilon signed limit: F is still the
full lower prefix of the relative Hodge inverse, the axial M remains
long range, and variable multipliers keep their original order.
Neither convergence nor vanishing of the complete cubic residual/action
response follows. Its coefficient comparison, the other jets, finer
powers/logarithm and the interacting/continuum/infrared gaps remain open.
This is local standard-method REPRODUCTION, with no originality claim.

## Proof

### 1. A positive comparison in the unchanged trace order

For every positive vertex matrix 0<=H<=Y we first prove

    |T_i(H)| <= C_i N^(1/2) sqrt(Tr H).                   (5)

This is not a positivity assertion for T_i, A^gen or either probe.
Fix k,l,j and put O=m_(j,l)J_j. Choose L175's link cutoff chi equal
to one on the input support of A^gen. Set

    B=Sigma^(1/2) A^gen Sigma^(1/2),
    X_H=Sigma^(-1/2) chi M_(h_k) S H^(1/2),
    Z_H=H^(1/2) O Phi Sigma^(1/2).                        (6)

Since A^gen chi=A^gen, cyclicity of the finite trace gives exactly

    Tr(B X_H Z_H)=Tr[H O F A^gen M_(h_k) S].             (7)

No multiplier has been commuted. L175(7), the compact-interior bound
||chi h_k||_infinity<=C a p(k), bounded endpoint incidence and bounded
||Sigma^(-1/2)|| give

    ||B||<=C N,
    ||X_H||_HS<=C a p(k) sqrt(Tr H).                     (8)

The interior estimate is used only at the residual input. No smooth
extension of h_k across its upper pinned jump is required.

Using the true Gram identity Phi Sigma Phi^T=K,

    ||Z_H||_HS^2=Tr[H O K O^T]
                <=Tr[Y O Y O^T].                        (9)

Indeed replace H by Y against the positive O K O^T, then replace K
by Y against the positive O^T Y O. This only uses H<=Y and K<=Y;
H and O need not commute, and H need not be bounded by K.
L159(12),(15), specialized in L175(15), give

    ||Y^(1/2) m_(j,l) J_j Y^(1/2)||_HS
                                  <=C p(l) N^(1/2),     (10)

for j=2,3,4. The multiplier bound is in the lower-anchored, upper-free
axial mixed energy with complete transverse Dirichlet end edges. Its
smoothness hypothesis holds for q_l=L v_l, including the normal end
links; it does not apply a compact cutoff to that action column.
Equations (9)-(10) bound ||Z_H||_HS by C p(l) N^(1/2).

The finite trace inequality |Tr(B X Z)|<=||B|| ||X||_HS ||Z||_HS
therefore bounds (7) by
C p(k)p(l) N a N^(1/2) sqrt(Tr H). Since Na=8, summing j and the
full heat expansion proves (5). Here L156(8) gives
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i for every fixed polynomial p.
The -6 in (2) is retained once; no new color factor is added.

### 2. Trace of the exact resolvent correction

L156(6) gives the exact operator identity

    D_N:=Y-K
        =(L_D tensor I+I tensor Delta_T)^(-1)(I tensor G),
    0<=D_N<=Y,                                          (11)

where L_D is the axial scalar Dirichlet Laplacian on N-1 interior
vertices. D_N is not the signed remainder E of the forest covariance.
It is positive because the two factors in (11) are positive and
commute; D_N<=Y follows from K>=0. This identity already includes
the constant axial edge mode of the original Hodge covariance.

The eigenvalues of L_D are alpha_p=4 sin^2(pi p/(2N)), 1<=p<N.
Those of Delta_T are lambda_q=sum_(j=2)^4 alpha_(q_j),
q in {1,...,N-1}^3. The full relative sine/cosine spectrum is L026(6)-(7).
The elementary sine bound gives alpha_p>=4p^2/N^2 and
lambda_q>=4|q|^2/N^2. Consequently

    Tr D_N=sum_(p,q) 1/[lambda_q(alpha_p+lambda_q)]
       <=(N^4/16) sum_(p,q) 1/[|q|^2(p^2+|q|^2)].       (12)

There are m^3-(m-1)^3<=3m^2 transverse indices with max q_j=m.
Both denominator factors increase with |q|^2, so their full shell
contribution is at most 3/(p^2+m^2). For a decreasing positive function,
sum_(p=1)^infinity f(p)<=integral_0^infinity f(x) dx. Hence

    Tr D_N <=(3N^4/16) sum_(m=1)^(N-1)
                              integral_0^infinity dx/(x^2+m^2)
            =(3 pi/32) N^4 sum_(m=1)^(N-1) 1/m
            <=(3 pi/32) N^4 log(eN).                    (13)

No axial level or low transverse mode has been removed from the
identity; enlarging the positive sums only bounds it from above.
Apply (5) to D_N and use linearity of (2):

    |W_i^0-W_i|=|T_i(D_N)|
                          <=C_i N^(5/2) sqrt(log(eN)).  (14)

Combining with L175(3)'s smaller N^(5/2) log(eN)^(1/4) error gives
the first assertion of (3). The replacement is made only after this
ordered error estimate; Y is not asserted to equal the true covariance.

### 3. Uniform removal of a transverse mass

Let H_epsilon=Y-Y_epsilon=M tensor (G-G_epsilon). Since G_epsilon
is a function of Delta_T, 0<=H_epsilon<=Y, without commuting it past
any multiplier in (2). Exactly

    Tr H_epsilon=Tr M sum_q epsilon/[lambda_q(lambda_q+epsilon)],
    Tr M=N(N-1)/2<=N^2/2.                               (15)

On the shell max q_j=m, monotonicity in lambda and its lower bound
4m^2/N^2 give

    sum_q epsilon/[lambda_q(lambda_q+epsilon)]
       <=(3 epsilon N^4/4) sum_(m=1)^(N-1)
                                            1/(4m^2+epsilon N^2)
       <=(3 epsilon N^4/4) integral_0^infinity
                                            dx/(4x^2+epsilon N^2)
        =(3 pi/16) N^3 sqrt(epsilon).                   (16)

Thus

    Tr H_epsilon <=(3 pi/32) N^5 sqrt(epsilon).          (17)

This estimate holds for every epsilon>0 and admitted N; no condition
N sqrt(epsilon)>=1 is needed. Applying (5) to H_epsilon proves the
second assertion of (3). Multiplication by a^3=512/N^3 yields

    |a^3(V_i-W_i^epsilon)|
       <=C_i [N^(-1/2) sqrt(log(eN))+epsilon^(1/4)],     (18)

which proves (4). It permits taking the mesh limit first and then
removing epsilon once the required fixed-mass limit is established.
It does not provide that limit, or justify a mesh-dependent choice
inside a future fixed-mass convergence theorem.

### 4. Scope of verification and continuation

The proof checks the full matrix order through (7), the two positive
comparisons through (9), and both complete spectral traces through
(12)-(17). These are analytic bounds; no numerical certificate, mesh
extrapolation or imported IEEE heat interval is used. All exterior
heat modes are summed using L156(8), independently of the internal
mass. Neither Q form is removed anew: L175 already justifies their
subcubic contribution in this branch alone. Upper action contributions
are retained through its exact globally co-closed column.

For the remaining signed limit, (4) supplies one covariance
regularization with an explicit vanishing error. The other long axial
factor F, variable coefficients, finite boundaries and the original
trace sign must still be controlled. A fixed-mass frozen calculation
without that control would not answer the approved target.

### 5. Separate critical audit of the uniform comparison

Audit date: 2026-10-21. STEP_ID:
YM-20261021-394-static-upstream-mass-critical-audit.
The verdict is acceptance of (3)--(4), relative to the stated imports;
no correction is needed. This validates the comparison used in L179(7)
and the coefficient identification for the ordered static rate. It is
not a new bound or an audit of L175's preceding reduction.

The finite factorization (7) passes directly: multiplying B X_H Z_H
and cycling leaves A^gen chi M_(h_k) S H O Phi Sigma. The identity
A^gen chi=A^gen restores exactly (2). The cutoff is adjacent to the
residual input; it neither cuts off m nor restricts any covariance
source. The compact O(a) estimate on h_k is therefore sufficient even
with its upper forest jump retained. Both orientations of A^gen remain
inside B, and the sole -6 is still outside this same trace.

The two positive replacements in (9) are legitimate for arbitrary
0<=H<=Y, not just H<=K. First Tr[(Y-H) O K O^T]>=0; then
Tr[(Y-K) O^T Y O]>=0 after cyclicity. Thus there is no multiplier
commutation or positivity assumption on the signed response. L159's
mixed-energy product proof applies to the actual smooth action
multiplier with physical C^2 bound C a^3 p(l); its lower-anchored,
upper-free axial domain and all transverse Dirichlet end edges agree
with Y. The complete transverse skew-difference energy estimate gives
the N^(7/2) unmultiplied sandwich, hence (10)'s N^(1/2) after a^3.
With ||B||=O(N) and ||X_H||_HS=O(a sqrt(Tr H)), this reproduces
(5) with a constant independent of H, mesh and any later mass.

L156(6) and L026's componentwise sine/cosine spectrum give exactly
(11), including the constant axial edge mode. Diagonalizing the
positive correction uses axial vertex labels p>=1 only because its
constant edge contribution cancels in Y-K; it is not removed from K.
The full transverse shell has at most 3m^2 labels and |q|>=m.
Consequently its contribution to (12) is bounded by
3/(p^2+m^2), giving precisely the harmonic sum in (13). The estimate
is O(N^4 log(eN)), and (5) therefore gives
O(N^(5/2)sqrt(log(eN))) before importing L175(3).

For the mass difference, functional calculus gives
0<=H_epsilon=M tensor (G-G_epsilon)<=Y. The same full shell bound
reduces its transverse trace to
(3 epsilon N^4/4) sum_m (4m^2+epsilon N^2)^(-1).
The decreasing-function integral is pi/(4 N sqrt(epsilon)); with
Tr M<=N^2/2 this proves (17), uniformly also when epsilon<N^(-2).
Applying (5) gives exactly O(N^3 epsilon^(1/4)). All source/end rows
and the constant mode are already present in these tensor traces.

Finally the complete heat sum in L156(8) absorbs the fixed polynomial
p(k)p(l) in each bound for both probes. Multiplication by a^3 then
gives (18) with no numerical heat-value premise. This is a uniform
finite comparison before the mesh limsup, not a fixed-mass convergence
claim at a varying mass. The qualified import of L175, the original
mode estimates and the independent interacting/construction gaps remain.

## Mathlib

Full matching theorem: **not checked**. Supporting finite trace/Schatten
inequalities, tensor-product spectral sums and resolvent functional
calculus: **not checked**. Unknown coverage is not absence. Reuse the
unchanged [assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. The specialization is
needed to distinguish a true cubic-scale covariance comparison from
the earlier positive domination bound, with the actual matrix order
and pinned domains unchanged.
