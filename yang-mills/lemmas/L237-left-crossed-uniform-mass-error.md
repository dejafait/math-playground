# L237 — Uniform mass error in the complete left crossed trace

## Hypotheses

Use exactly L100(1), with the relative all-face pinned SU(2) cube,
straight lower-rooted direction-1 forest, sufficiently large admitted
even N, a=8/N, tau=1/16, ordinary stored coordinates and actual probes
i=3,6. Take the bare small-coupling coefficient at fixed mesh before
refinement. All relative source/end rows, interior axial levels,
allowed constant component indices and exterior heat labels remain.

Write L100's operators as

    K=Delta_E^(-1)Q,  Omega_(gh,k)=P Omega_k Q,
    Omega_(hh,k)=Q Omega_k Q,  A=H_g K_a I_T,
    R_L=sum_(k,l)c_(i;kl,a)
              Tr(K Omega_(gh,k)^T A K Omega_(hh,l)).       (1)

P,Q are the fixed transverse gradient/co-closed selectors. They
commute with Delta_E; no commutation with Omega_k or A is assumed.
K_a and A retain their complete endpoint/clover filters and displacement.
Import L088(3)--(5)'s actual skew Omega_k and full heat expansion,
L089(1)'s split Omega_k=F_k+H_k, L090(7)--(9)'s derivative/collar
estimates, L093(1)'s ||A||<=C/a, and L100(7)--(8)'s exact prefix split.
Use L225(1) only as the scalar resolvent-difference energy estimate;
its differently ordered co-closed trace conclusion is not assumed here.

For 0<epsilon<=1 define

    K_epsilon=(Delta_E+epsilon I)^(-1)Q,
    J_epsilon=K-K_epsilon,  L_N=log(eN),
    R_(L,epsilon)=sum_(k,l)c_(i;kl,a)
          Tr(K_epsilon Omega_(gh,k)^T A
                             K_epsilon Omega_(hh,l)).    (2)

Only the two K positions are changed in (2).

## Conclusion

Uniformly in N and epsilon, for both actual probes,

    |R_L-R_(L,epsilon)|
       <=C_i[N^3 sqrt(epsilon)+N^(5/2)sqrt(L_N)].         (3)

In particular,

    |R_L-R_(L,N^-1)|<=C_i N^(5/2)sqrt(L_N).              (4)

Consequently the approved O(N^(5/2)L_N^2) bound for R_L is equivalent
to the same bound for precisely R_(L,N^-1). This is only a partial
reduction: neither bound is established here.

The complete prefix contribution in this massive trace is explicitly
retained below. The elementary bounds proved here give only

    |R_(pref,epsilon)|
       <=C_i min{N^3, N^(5/2)/epsilon}.                  (5)

At epsilon=N^-1, (5) is O(N^3), above the required threshold.
This is a limitation of these upper bounds, not a lower bound, signed
growth, noncancellation claim or disproof of the requested rate.
Ordered prefix, projection, localization, coefficient-freezing and
relative-boundary estimates remain unresolved. No full L011 rate,
interacting reflected estimate or continuum/mass-gap result follows.

## Proof

### 1. Apply the scalar input before either alternating projection

The spectral objects in L225(1) are exactly the present Delta_E,Q,K
and J_epsilon, on the same relative transverse-link space with axial
Dirichlet labels. Thus its established inequality applies without a
change of normalization:

    Tr(Delta_E J_epsilon^2)<=C N^4 epsilon.               (6)

This includes epsilon<N^-2 and all allowed zero own-direction labels;
there is no full zero eigenvalue on E. We import this scalar inequality
and do not reprove its shell sum or transfer L225's final trace bound.

J_epsilon=K F_epsilon(Delta_E), with
F_epsilon(rho)=epsilon/(rho+epsilon) in [0,1]. It therefore meets
L090(7)'s hypotheses. That estimate is for unprojected H_k J,
which is essential here since the left selector will be P, not Q.
Its natural-difference energy is (6). L090(8)--(9) also give

    ||J_epsilon||_HS<=C N^2 sqrt(L_N),
    ||E_partial J_epsilon||_HS<=C N^(3/2)sqrt(L_N),

where E_partial is the entire fixed-width staggered face collar.
Substituting these three quantities into L090(7), in its original
order, gives

    ||H_k J_epsilon||_HS
       <=C a p(k)[N^2 sqrt(epsilon)
                    +a N^2 sqrt(L_N)+N^(3/2)sqrt(L_N)]
       <=C p(k)[N sqrt(epsilon)+sqrt(N L_N)].            (7)

L088(3),(5) and the bounded path multiplicities imply
||F_k||<=C a^2 p(k). Hence the exterior-circulation terms, still
present in both alternating factors, satisfy

    ||F_k J_epsilon||_HS
       <=C a^2 p(k)N^2 sqrt(L_N)<=C p(k)sqrt(L_N).

Combining this with (7) proves

    ||Omega_k J_epsilon||_HS
       <=C p(k)[N sqrt(epsilon)+sqrt(N L_N)].            (8)

Enlarge the fixed polynomial p as in L100(3). The complete actual
heat coefficients satisfy sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.
There is no internal or external mode truncation in (8).

### 2. Check both covariance positions in the crossed order

For Z=K, K_epsilon or J_epsilon, Z is symmetric and ZQ=QZ=Z.
Put X_k(Z)=Z Omega_(gh,k)^T and Y_l(Z)=Z Omega_(hh,l).
Their exact transposes are

    X_k(Z)^T=P Omega_k Z,
    Y_l(Z)^T=-Q Omega_l Z.                              (9)

Thus (8) bounds X_k(J_epsilon) and Y_l(J_epsilon), by left
contraction only. No P is moved through Omega_k; in particular
the gh factor is not replaced by an hh factor.

L100(4) gives ||Omega_k K||_HS<=C p(k)N. Since
K_epsilon=K Delta_E(Delta_E+epsilon I)^(-1), the last factor
is a spectral contraction on the right, so

    ||X_k(K)||_HS+||X_k(K_epsilon)||_HS<=C p(k)N,
    ||Y_l(K)||_HS+||Y_l(K_epsilon)||_HS<=C p(l)N.         (10)

For every pair k,l the exact difference of the traces (1),(2) is

    Tr(X_k(J_epsilon) A Y_l(K))
       +Tr(X_k(K_epsilon) A Y_l(J_epsilon)).             (11)

Use |Tr(X A Y)|<=||X||_HS ||A|| ||Y||_HS in each summand,
then (8)--(10) and ||A||<=C/a. The resulting pairwise bound is

    C p(k)p(l) a^-1 N
                       [N sqrt(epsilon)+sqrt(N L_N)].

The complete heat sum and a=8/N prove (3). Substitution epsilon=N^-1
is now into a uniform finite inequality, proving (4). Applying the
triangle inequality in both directions proves the stated equivalence
of the two target bounds, since sqrt(L_N)<=L_N^2. No fixed-mass
limit is evaluated at a varying parameter.

### 3. Expose the remaining full prefix trace and the failed norm count

Keep exactly L100(7)'s finite identity aA=A_loc+E_pref, where

    A_loc=P(aG0)-T sum_(mu=2)^4 H_av U_mu C_mu,
    E_pref=-T sum_(mu=2)^4 S[U_mu,T_1]C_mu,
    G0=I_T^T K_a I_T,  S=B C_1^T,
    (T_1 x)_j=(x_(j+1)-x_(j-1))/2,
    H_av=(2I+S_++S_-)/4,  U_mu=M_(u_(a,mu)).

All sums use the original pinned interval x_0=x_N=0; C_mu is
the original transverse endpoint average. L093(5)--(8) proves
this identity with its lower rank-one term removed only because
u_(a,mu)(1,y)=0. The full prefix tail and upper rows remain.
The split gives the exact retained contribution

    R_(pref,epsilon)=a^-1 sum_(k,l)c_(i;kl,a)
               Tr(X_k(K_epsilon) E_pref Y_l(K_epsilon))
      =-a^-1 sum_(k,l,mu)c_(i;kl,a)
        Tr(X_k(K_epsilon) T S[U_mu,T_1]C_mu
                                             Y_l(K_epsilon)). (12)

The complementary contribution has A_loc/a in place of E_pref/a.
Neither part is deleted. Import L100's uniform ||E_pref||<=C and
||E_pref||_HS<=C N^(3/2), both proved with the full prefix present.
Using (10) on both sides of E_pref/a gives the first bound C_i N^3
in (5). Alternatively bounded path multiplicity and L088(5) give
||Omega_k||<=C a p(k), hence

    ||X_k(K_epsilon)||<=C a p(k)/epsilon.

The Schatten product inequality applied to (12), with E_pref in
Hilbert--Schmidt norm and Y_l controlled by (10), gives

    |R_(pref,epsilon)|
       <=C_i a^-1 (a/epsilon) N^(3/2)N
       =C_i N^(5/2)/epsilon.

This proves (5), improving the epsilon^-2 allowance from a fully
crude reading of L100(9), but not closing the prefix estimate.
For example epsilon=N^-1 gives only the cubic bound. Even treating
the displayed sufficient estimates as a parameter-selection scheme
does not close the target: keeping N^3 sqrt(epsilon) within
N^(5/2)L_N^2 asks for epsilon=O(N^-1 L_N^4), whereas keeping
N^(5/2)/epsilon within that budget asks for epsilon bounded below
by a constant times L_N^-2. Those sufficient ranges are disjoint
for large N. They are not necessary conditions on the actual traces.
A better ordered estimate in (12), or a joint estimate retaining its
local companion, is needed; optimizing these factor norms alone is
not such an estimate.

This is a RESEARCH / REPRODUCTION specialization under the unchanged
EXPLORE assessment for the complete quantitative R_L target. The
scalar theorem is imported from L225(1); the new applicability check
is (8)--(11) for the gh/hh product with its full A. The finite trace
inequalities are elementary supporting tools already used in L100.
No claim of originality beyond the checked sources is made. This
partial input requires a separate critical audit and does not audit
its upstream analytic premises. No numerical evidence is used.

### 4. Separate critical audit of the mass comparison

Audit dated 2026-10-19, STEP_ID YM-20261019-339-left-crossed-complete-rate-audit.
Accept (3)--(4) relative to the stated L088--L090, L093, L100 and
L225 scalar inputs. This is an applicability audit of this trace,
not an independent reconstruction of their finite Gaussian contraction.
The pending-audit language above records the original proof's status;
this section supplies its later review.

The scalar difference in (6) is on exactly the same transverse-link
space as L225(1). Its axial Dirichlet factor excludes a full zero
eigenvalue without excluding constant own-direction edge indices.
The shell comparison also covers epsilon below N^-2. L090(7) acts
on the unprojected H_k J_epsilon, so left multiplication by either
P or Q is legitimate. Its collar allowance is retained in (7), and
the complete F_k contributes O(p(k)sqrt(log(eN))) in addition.

Independently transposing the literal gh and hh factors gives (9),
with the minus sign only in the hh expression. The unchanged factors
in both terms of (11) have norm O(p N): K_epsilon is K followed
on the right by a spectral contraction. Thus the two errors, before
the heat sum, are at most

    C p(k)p(l) a^-1 N [N sqrt(epsilon)+sqrt(N log(eN))].

This is precisely (3) after a=8/N, not a fixed-mass asymptotic.
L088's polynomial heat envelope permits the same enlarged polynomial
in both placements. The prefix/local decomposition in section 3
matches L100(7) with its single outside a^-1. The bound (5) remains
only a failed sufficient factor count; no lower bound was inferred.
This audit does not convert that count into a prefix estimate; L238
contains the separate composite estimate needed for the assembly.

## Mathlib

Full matching crossed-trace estimate: **not checked**. Supporting
finite spectral calculus, Hilbert--Schmidt/Schatten inequalities and
relative incidence coverage: **not checked**. Unknown coverage is
not absence. No general continuum Ward or flow-finiteness theorem
is being used to supply a bound on this isolated forest trace.
