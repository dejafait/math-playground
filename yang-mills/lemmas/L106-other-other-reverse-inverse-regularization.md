# L106 — Uniform cubic-scale inverse regularization of the reverse trace

## Hypotheses

Keep L105's actual co-closed-base reverse trace R_R, for both L010
probes i=3,6, SU(2), the straight lower-rooted direction-1 forest,
relative all-face fixed-link box (-4,4)^4, admitted even N, a=8/N and
tau=1/16. The bare small-coupling coefficient is taken at fixed mesh
before refinement. Coordinates and norms are ordinary stored ones.
Every interior axial level, pinned transverse end row and exterior
heat mode is retained. This is not the gradient-base reverse trace G_R.

Import L105(1)--(3), writing n=N-1 and

    Delta_0=T^T T, G=Delta_0^-1, P=T G T^T, Q=I-P,
    A_k(s)=P Omega_k(s) Q, H_l(t)=Q Omega_l(t) Q,
    K_ts=R_ts(Delta_T)Q,
    R_ts(lambda)=[(L_D+lambda I)^-1]_ts,
    S_st=1_(t<s)+delta_st/2.

The matrices W_t, Omega_k and real coefficients c_(i;kl,a) are exactly
those of L105. In particular W_t retains both transverse generator
filters and its actual level-t displacement. For 0<epsilon,eta<=1 set

    K_ts^epsilon=R_ts(Delta_T+epsilon I)Q,
    G_eta=(Delta_0+eta I)^-1,
    R_(i,N;epsilon,eta)=a^-1 sum_(k,l)c_(i;kl,a) sum_(s,t) S_st
      Tr[K_ts^epsilon A_k(s)^T T G_eta W_t^T H_l(t)].       (1)

Only these two displayed inverses change. In particular P and Q in
A,H,K^epsilon stay exact, although P itself contains G. No projection
regularization, coefficient freezing or axial replacement is included.
Use eta=0 in this notation to mean the original middle G.

## Conclusion

There is a mesh- and parameter-independent C_i such that, whenever
N sqrt(epsilon)>=1 and N sqrt(eta)>=1,

    |R_R-R_(i,N;epsilon,eta)|
      <= C_i N^3 [sqrt(epsilon)+eta^(3/4)/epsilon].        (2)

Consequently the explicit choice eta=epsilon^2 satisfies, for
0<epsilon<=1 and N epsilon>=1,

    |R_R-R_(i,N;epsilon,epsilon^2)|
      <= C_i N^3 sqrt(epsilon),
    limsup_(N->infinity) a^3
      |R_R-R_(i,N;epsilon,epsilon^2)|<=C'_i sqrt(epsilon). (3)

The same estimates hold with both Omega factors replaced by L105's
Omega^0, keeping all other factors fixed. Moreover the difference
between the full and Omega^0 versions of (1) is O_i(N^2), uniformly
in both parameters. Thus exterior circulation may still be removed
at cubic scale after this regularization.

This is a uniform approximation, not a scaled-limit theorem.
It clears an inverse-removal obligation for a later fixed-parameter
trace limit. Exact projections, axial localization, coefficient and
boundary control and that fixed-parameter limit remain to be handled.
The transverse H generator still lacks cubic control; the other
functionals remain unevaluated and joint compensation with
-4 gamma D_i before the outside factor 3 is unproved. There is no
interacting continuum or mass-gap conclusion.

## Proof

### 1. Inputs and the order of approximation

Import the exact layer formula L105(3) and its estimates (10)--(12):

    ||T G^(1/2)||=1, ||W_t G^(1/2)||<=C,
    ||A_k(s)||+||H_k(s)||<=C a p(k),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                   (4)

One fixed mode polynomial p suffices uniformly in the axial levels.
In particular ||T G W_t^T||<=C. The same bounds hold with Omega^0.
These imported bounds retain all cross-component filters and heat
modes; they require no scalar polarization or norm gain for the full
reverse prefix. We first change K while keeping G exact. Only after
this step do we use the massive K to estimate the change in G.

### 2. Positive differences of the axial covariance blocks

For a scalar lambda>0 let R_lambda=(L_D+lambda I)^-1. L095(13)
proves entrywise nonnegativity and R_lambda 1<=lambda^-1 1 on
the full finite Dirichlet interval, including both pinned ends.
The finite resolvent identity gives

    R_lambda-R_(lambda+epsilon)
      =epsilon R_lambda R_(lambda+epsilon).             (5)

The right side is entrywise nonnegative. Applying it to 1 and using
the two row-sum bounds proves

    sum_(s,t)[R_lambda-R_(lambda+epsilon)]_ts
      <=n epsilon/[lambda(lambda+epsilon)].             (6)

Since Delta_T commutes with Q, the transverse operator
K_ts-K_ts^epsilon has precisely these nonnegative scalar eigenvalues
on ker P, and is zero on gradients. Each such block is positive
semidefinite. Hence its trace norm equals its trace, giving

    sum_(s,t)||K_ts-K_ts^epsilon||_1
      <=n Tr_(ker P)[epsilon Delta_T^-1
                                  (Delta_T+epsilon)^-1]
      <= C N^4 sqrt(epsilon).                           (7)

Here is the complete spectral bound used in the last step. Import
L095's relative transverse edge spectrum: for component nu its own
index lies in 0,...,N-1 and its other two indices in 1,...,N-1,
lambda_m>=c |m|^2/N^2, and shells max_j m_j=r contain at most C r^2
labels, including all components. There is no zero mode. Restriction
to ker P only decreases the positive trace. Put M=N sqrt(epsilon)>=1.
For r<=M bound epsilon/[lambda(lambda+epsilon)] by 1/lambda;
the shell sum is at most C N^2 M. For r>M use epsilon/lambda^2;
the remaining sum is at most C epsilon N^4 sum_(r>M) r^-2
<=C epsilon N^4/M. Both are O(N^3 sqrt(epsilon)). If M exceeds
the final shell, the empty high range contributes zero and the same
low-range bound holds. Multiplication by n proves (7). Thus the
estimate includes the low physical modes and all relative end rows.

In L105's exact layer trace, the operator multiplying each covariance
block has norm at most C a^2 p(k)p(l), by (4). Since 0<=S_st<=1,
trace duality, (7), the a^-1 prefactor and the full heat sum give

    |R_R-R_(i,N;epsilon,0)|
      <=C_i a N^4 sqrt(epsilon)
      <=C'_i N^3 sqrt(epsilon).                         (8)

No sign of the response or of its exterior coefficients is used.
Positivity concerns only the scalar differences and their transverse
spectral blocks. All coefficients remain in their original order.

### 3. The massive covariance permits a different norm estimate

Entrywise resolvent monotonicity, proved by (5), also gives
0<=R_ts(lambda+epsilon)<=R_ts(epsilon) for every lambda>=0.
The transverse edge dimension is at most C N^3, and Q is an
orthogonal spectral projection. Therefore

    ||K_ts^epsilon||_HS<=C N^(3/2) R_ts(epsilon),
    sum_(s,t)||K_ts^epsilon||_HS
      <=C N^(3/2) n/epsilon<=C N^(5/2)/epsilon.           (9)

The row-sum estimate here is applied to the scalar finite axial
matrix L_D+epsilon I, so it requires neither axial translation
invariance nor an infinite-interval replacement. Its epsilon^-1
dependence is retained and is essential to the parameter choice.

On the transverse vertex space define
J_eta=eta(Delta_0+eta I)^-1. Exact spectral calculus gives

    T(G-G_eta)W_t^T
      =(T G^(1/2)) J_eta (W_t G^(1/2))^T.                (10)

Import L103(16)'s second spectral bound on this same pinned vertex
space: ||J_eta||_HS^2<=C N^3 eta^(3/2) when N sqrt(eta)>=1.
It is the shell estimate for sum_lambda eta^2/(lambda+eta)^2,
not an operator-norm-smallness assertion. Thus (4),(10) give

    ||T(G-G_eta)W_t^T||_HS<=C N^(3/2) eta^(3/4).         (11)

This factorization preserves the level-t multiplier in W_t and
does not commute it through any inverse or projection. In particular
the existing reverse-prefix operator obstruction is unaffected.

Use Hilbert--Schmidt trace duality for each (s,t), with A_k(s),H_l(t)
in operator norm, then sum (9). Equations (4),(11) yield

    |R_(i,N;epsilon,0)-R_(i,N;epsilon,eta)|
      <= C_i a^-1 a^2 N^(3/2) eta^(3/4)
                                      N^(5/2)/epsilon
      <= C'_i N^3 eta^(3/4)/epsilon.                    (12)

Every sum is finite before the uniform heat estimate; the absolute
mode majorant in (4) also justifies the stated full exterior sum.
Combining (8),(12) proves (2). Setting eta=epsilon^2 makes the
second error epsilon^(1/2). The condition N epsilon>=1 implies
both required spectral conditions, proving (3). The intended order
is fixed epsilon, mesh limit, then epsilon down to zero. No choice
of epsilon depending on N is inserted into an unproved localization
estimate, and using equal masses is not asserted to give a vanishing
error by (2).

### 4. Exterior circulation and the scope of the result

The preceding proof applies to Omega^0 with precisely the same
bounds. To check uniformity of its O(N^2) comparison with the full
regularized trace, observe that

    ||T G_eta W_t^T||
      =||(T G^(1/2))[Delta_0/(Delta_0+eta)]
                                  (W_t G^(1/2))^T||<=C.

Also K_ts^epsilon is positive semidefinite and its trace is at most
that of K_ts, by (5). Thus its summed trace norm is at most C N^4,
as in L105(14). L105(16) gives ||F_k||<=C a^2 p(k) and
||Omega_k^0||<=C a p(k). Expanding the two alternating factors,
each of the three difference terms has at least one F and costs
at most C a^3 p(k)p(l) in operator norm, including the unchanged
projections and regularized middle factor. The trace sum with its
a^-1 prefactor is at most C_i a^2 N^4=O_i(N^2), uniformly in
epsilon,eta. This proves the additional conclusion without deleting
any remaining path term or boundary row.

This is local progress by finite resolvent identities, trace-ideal
inequalities and the already established relative spectral bounds.
It does not rederive L048 or import finiteness of a complete Ward
response for an isolated group. L100's left orientation and L104's
gradient-base limit do not cover the present order. Their results
are method comparisons, not mathematical premises here. The ready
complete-group EXPLORE assessment is reused without a source refresh;
classification is REPRODUCTION, with no claim beyond sources checked.
No numerical script or arithmetic-model assumption is used. L082's
IEEE qualifications remain attached to eventual numerical comparisons
with D_i, which this result does not perform.

## Mathlib

Full matching two-stage reverse-trace approximation: **not checked**.
Supporting finite resolvent identity, positive matrix row-sum bounds,
spectral functional calculus and trace-ideal coverage: **not checked**.
Unknown availability is not evidence of absence. All inputs are the
specified local finite-matrix estimates; no external continuum or
Yang--Mills construction theorem is invoked.
