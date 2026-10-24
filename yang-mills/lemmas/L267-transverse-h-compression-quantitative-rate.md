# L267 — Quantitative transverse-H finite-compression comparison

## Hypotheses

Use exactly L116's R_prod, R_inf, e_j, q_j(N), eta_N and its fixed
support-clearance constant c>0. In particular use L110's unshifted
integer-index Fourier convention and plane order (23,24,34). Retain
both actual L010 probes i=3,6, the relative SU(2) cube (-4,4)^4,
sufficiently fine admitted even N, a=8/N, tau=1/16, the straight
lower-rooted direction-1 forest, ordinary stored coordinates and the
bare small-coupling coefficient taken first at each fixed mesh.

Import L116's exact identities and complete trace estimates, including
both omitted-output compression selectors, all finite path/component
filters, both original coefficient levels and generator orientations,
all source and normal/end rows, constant modes and full heat sums.
Their imported premises are not independently audited here. L118's
separate full-grid identity R_inf=0 is used only for the last conclusion.

## Conclusion

There is a universal C, independent of every heat label and axial
offset, such that for all j in Z and z in Z^3,

    ||e_j(z)||_F <= C (1+sqrt(j^2+|z|^2))^(-4).             (1)

For L116's exact weighted squared tails this gives

    q_j(N)^2 <= C_c (1+N+|j|)^(-3),
    eta_N=sum_(j in Z) q_j(N) <= C_c N^(-1/2).             (2)

Consequently, for both actual probes and all sufficiently fine admitted
meshes,

    |R_prod-R_inf| <= C_i N^(5/2),
    |R_prod| <= C_i N^(5/2).                              (3)

Thus this one complete compression error meets the proposed
N^(5/2)log(eN)^2 component budget. The four transverse-H coefficient
placement remainders, full quantitative L011 assembly, upstream audit
qualifications and interacting/continuum/infrared construction remain
independent gaps. The separate critical audit below accepts this
specialization relative to its imported premises; it is not a complete
transverse-H remainder or a Yang–Mills construction.

## Proof

### 1. Import the scalar theorem with its actual normalization

Use Lawler–Limic, *Random Walk: A Modern Introduction* (Cambridge,
2010), section 1.1, printed pp. 9–11, and Theorem 4.3.1, printed
pp. 81–83, in the
[author-hosted 289-page text](https://www.math.uchicago.edu/~lawler/srwbook.pdf#page=81).
The theorem concerns symmetric finite-range irreducible walks in
dimension at least three; its proof explicitly includes the bipartite
case. Four-dimensional nearest-neighbor simple random walk, with
probability 1/8 for each signed coordinate step, satisfies these
hypotheses. Its covariance matrix is I/4. The theorem's stated
simple-walk specialization gives

    G_walk(X) = (2/pi^2)|X|^(-2) + O(|X|^(-4))
                                              as |X| -> infinity. (4)

This asymptotic, including its uniform remainder over lattice points,
is imported, not reproved. No mixed-difference assertion is attributed
to the source's repeated-coordinate Corollary 4.3.3.

Let L_4 be the positive, unnormalized lattice Laplacian on Z^4,
with symbol

    ell(omega,theta)=2-2 cos(omega)+lambda(theta),
    lambda(theta)=sum_(mu=2)^4 |exp(i theta_mu)-1|^2.

If P_rw is the simple-walk transition operator, L_4=8(I-P_rw).
Its Green kernel is therefore H(X)=G_walk(X)/8, so (4) gives

    H(X)=(1/(4 pi^2))|X|^(-2)+O(|X|^(-4)).               (5)

For completeness this identification uses the Green kernel, not a
bounded inverse of the massless Laplacian on all of l2. Its Fourier
formula is

    H(j,z)=integral exp(i[j omega+z dot theta])
                     /ell(omega,theta) d omega dtheta/(2pi)^4.
                                                               (6)

Indeed ell^(-1) is integrable on the four-torus: its only singularity
is O(|(omega,theta)|^(-2)) at zero. For 0<=b<1, the Fourier multiplier
(1-b p_hat)^(-1) has the absolutely convergent geometric expansion
sum_n b^n p_hat^n, whose coefficient is sum_n b^n P_rw^n(0,X).
For b>=1/2, if p_hat>=0 then 1-b p_hat>=1-p_hat; if p_hat<0
then 1-b p_hat>=1>=(1-p_hat)/2. Thus the integrands are dominated
by 2/(1-p_hat), which is integrable. Dominated convergence on the
Fourier side and monotone convergence of the nonnegative transition
probabilities give the Fourier formula for G_walk. Division by eight
gives (6). In particular |H(X)|<=H(0)<infinity, including X=0.

For lambda>0, the axial Fourier coefficient of
(lambda+2-2 cos(omega))^(-1) is exactly L110's

    r_lambda(j)=exp(-kappa |j|)/(2 sinh kappa),
    kappa=2 asinh(sqrt(lambda)/2).

L110 proves its inverse recurrence, its unit source at j=0 and its
decay. Equivalently Fourier transformation of that recurrence gives
the displayed multiplier. Fubini in (6) is justified by ell^(-1)
integrability and hence gives, for every integer j,z,

    H(j,z)=integral exp(i z dot theta) r_lambda(j)
                                               dtheta/(2pi)^3. (7)

The transverse point lambda=0 has measure zero. The partial kernel
r_lambda(j)=O(lambda^(-1/2)) is integrable in three dimensions,
also for j=0. No constant mode is deleted from a finite relative
covariance; (6)–(7) concern only the separately defined full grid.

### 2. Identify every matrix entry, including the mixed differences

For mu,nu in {2,3,4} define on Z^4, with e_mu the coordinate vector,

    F_(mu nu)(X)=H(X+e_mu-e_nu)-H(X+e_mu)
                              -H(X-e_nu)+H(X).            (8)

By (7), its transverse multiplier at axial offset j is
r_lambda(j) t_mu conjugate(t_nu), where t_mu=exp(i theta_mu)-1.
This follows by multiplying the Fourier integrand by
(exp(i theta_mu)-1)(exp(-i theta_nu)-1); every shift in (8)
therefore has the stated sign in L110's inverse convention.

In plane order (23,24,34), the complete incidence matrix is

    D = [ -t_3   t_2    0  ]
        [ -t_4    0    t_2 ]
        [   0   -t_4   t_3 ].

Multiplying D by D* and using (8) yields the full real-space matrix
at X=(j,z):

    e_j(z) = [ F_22+F_33     F_34          -F_24     ]
             [ F_43          F_22+F_44     F_23     ]
             [ -F_42         F_32          F_33+F_44].       (9)

All entries on the right are evaluated at this same X. Reverse
off-diagonal entries retain their reversed shifts; no pointwise
symmetry F_mu,nu(X)=F_nu,mu(X) is assumed. For diagonal entries,
F_mu,mu=2H(X)-H(X+e_mu)-H(X-e_mu). Thus every entry, including
all six off-diagonal ones, is a sum of the genuine second differences
(8), without replacing a mixed difference by a repeated one.

To bound (8), write h(x)=(4 pi^2)^(-1)|x|^(-2) for nonzero real
x in R^4. Direct differentiation gives

    partial_mu partial_nu h(x)
      =(4 pi^2)^(-1)[-2 delta_mu,nu |x|^(-4)
                                      +8 x_mu x_nu |x|^(-6)].

Its Hessian norm is at most C|x|^(-4). For |X| sufficiently large,
the rectangle X+v e_mu-w e_nu, 0<=v,w<=1, has norm at least
|X|-2>=|X|/2. Twice applying the fundamental theorem of calculus
to h bounds its four-point difference in (8) by C|X|^(-4).

The remainder in (5) is bounded individually at all four shifted
lattice arguments by C|X|^(-4). Its four-point difference therefore
has this same bound by the triangle inequality. No derivative,
improved remainder, or smooth interpolation of that remainder is
needed. This is why the theorem's O(|X|^(-4)) error suffices even
for mixed directions. Combining the two parts gives
|F_mu,nu(X)|<=C|X|^(-4) for all large X, uniformly over the fixed
direction list. For the finitely many remaining X, boundedness of
H in (6) enlarges the same constant to give

    |F_mu,nu(X)|<=C(1+|X|)^(-4) for every X in Z^4.       (10)

Equation (9) and the fixed matrix dimension prove (1). This includes
j=0, arbitrary signs of j, all small spatial distances and shifted
arguments equal to zero.

### 3. Sum the complete spatial tail and then every axial offset

Fix a real L>=1 and write m=|j|. There are at most C(n+1)^2
points z in the three-dimensional shell n<=|z|<n+1. This follows,
for example, by enclosing their disjoint unit cubes in the annulus
with radii max(0,n-sqrt(3)) and n+1+sqrt(3), whose volume is
O((n+1)^2). On this shell |z|^2<=(n+1)^2 and

    1+sqrt(j^2+|z|^2) >= C^(-1)(1+m+n).

Using (1), and harmlessly including extra points in the first shell,

    sum_(|z|>=L) |z|^2 ||e_j(z)||_F^2
       <= C sum_(n>=floor L) (n+1)^4/(1+m+n)^8
       <= C sum_(n>=floor L) (1+m+n)^(-4)
       <= C (1+m+L)^(-3).                              (11)

For the final inequality, the decreasing series is bounded by its
first term plus the integral of (1+m+x)^(-4) from floor L to
infinity; floor L and L are comparable for L>=1. All constants are
independent of j and L. The estimate sums the complete Frobenius
matrix norm over all omitted spatial outputs; it is not a fixed-j
asymptotic or a finite offset preview.

Take L=cN in (11), for sufficiently large N that cN>=1. This gives
the first inequality in (2). Taking square roots and summing over
all positive and negative j gives

    eta_N <= C_c [(1+N)^(-3/2)
                    +2 sum_(m>=1) (1+N+m)^(-3/2)]
          <= C_c [(1+N)^(-3/2)+4(1+N)^(-1/2)]
          <= C_c' N^(-1/2).                            (12)

This supplies an explicit uniform tail modulus where L116 used
dominated convergence. It uses no first absolute kernel moment,
mass schedule, rough coefficient regularity or finite covariance
replacement.

### 4. Restore L116's exact compression and complete trace count

Retain L116(9)'s two terms in its exact B, with both coordinate
selectors Q_1 and Q_2 in place. Its compact input K_N has O(N^3)
rows, and each omitted output in either term is separated from
K_N by cN after the fixed stencil range has been allowed for.
L116(11)–(14) therefore give, with all their original filters,

    ||B E_j M_f||_HS <= C p(k)p(l) N^(1/2) q_j(N),
    |T_fin-T_inf| <= C p(k)p(l) N^2 q_(t-s)(N).          (13)

The second Hilbert–Schmidt factor has norm O(N^(3/2)), as proved
there; no output of E_j M_f has been made compact. Only the input
support is compact. Every infinite omitted-output row remains in
the norm and hence in (11).

For each original t there are at most N possible s, but the sum
over s of q_(t-s)(N) is bounded by the complete eta_N. Thus

    sum_(s,t=1)^(N-1) min(s,t) q_(t-s)(N)
                                               <= N^2 eta_N. (14)

Multiplying (13) by the original a min(s,t), summing all finite
stencil lists, and using the unchanged complete heat envelope
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i, yields

    |R_prod-R_inf| <= C_i a N^4 eta_N
                    <= 8 C_i N^3 C_c N^(-1/2).

Absorb the fixed clearance and numerical constants into C_i. This
proves the first inequality in (3), with a common sufficiently fine
mesh threshold for the two probes. L118's exact R_inf=0 then gives
the second. No outside factor 3 from L124 is applied here.

Only Delta_C has been quantified. Earlier exterior-circulation and
generator/scalar/energy placement errors retain their distinct signed
cubic coefficients, and no estimate for their remainders follows.
The proof imports the scalar asymptotic and L116's finite identities;
the necessary additional work is their explicit mixed-entry and
all-offset specialization. This is RESEARCH / REPRODUCTION under
the unchanged ready EXPLORE assessment
`drafts/literature/2026-10-23-transverse-h-compression-quantitative-rate.md`.
It is local standard-method progress, without a claim of originality
beyond the checked sources. No mathematical script or numerical
diagnostic supplies any part of this bound.

### 5. Separate critical audit — 2026-10-23

**Verdict: accepted relative to the stated imported premises.** This
RESEARCH / REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-compression-rate-critical-audit.md`.
It validates (1)–(3); no changed estimate, additional mathematical input
or repair of the argument is required. The following reconstruction
checks the specialization rather than recursively auditing L111,
L113–L115 or L118. Their existing qualifications remain.

**Scalar source and Fourier normalization.** The walk has eight
neighbors, transition probability 1/8, covariance I/4, and
8(1-p_hat)=sum_(mu=1)^4(2-2cos theta_mu). Thus division by eight
in (5) is necessary and correct. The cited Theorem 4.3.1 applies to
this symmetric, finite-range, irreducible bipartite walk. Its coefficient
2/pi^2 gives exactly 1/(4pi^2) for H. In addition,
Lawler–Limic, *Random Walk: A Modern Introduction* (2010),
Proposition 4.2.3, printed p. 79 in the
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf#page=79),
states the Fourier Green representation for d>=3, including the
bipartite case treated through (4.3) and (4.5). The positive exponent
here agrees by symmetry of the walk. The Abel argument above checks
that convention and the normalization; it is not a reproof of the
source asymptotic. Its domination also covers the negative part of
p_hat, in particular p_hat=-1. The only inverse singularity is at
p_hat=1, where the four-dimensional integral is finite.

For lambda>0, direct substitution gives
(2+lambda)r(j)-r(j-1)-r(j+1)=0 off zero and
(2 cosh kappa-2e^(-kappa))/(2 sinh kappa)=1 at zero.
The summable axial sequence therefore has Fourier transform
1/(lambda+2-2cos omega). Absolute integrability of ell^(-1)
justifies the partial integral (7). Its transverse singularity
lambda^(-1/2) is integrable, also at j=0. No finite relative mode is
removed and no bounded massless inverse on all of l2 is assumed.

**Nine signed entries and pointwise decay.** Independently taking the
inner products of incidence rows (-t_3,t_2,0), (-t_4,0,t_2),
(0,-t_4,t_3) gives the following complete table. Column headings
and row labels are plaquette planes, and each entry multiplies r_lambda(j).

| Row / column | 23 | 24 | 34 |
| --- | --- | --- | --- |
| 23 | abs(t_2)^2+abs(t_3)^2 | t_3 conjugate(t_4) | -t_2 conjugate(t_4) |
| 24 | t_4 conjugate(t_3) | abs(t_2)^2+abs(t_4)^2 | t_2 conjugate(t_3) |
| 34 | -t_4 conjugate(t_2) | t_3 conjugate(t_2) | abs(t_3)^2+abs(t_4)^2 |

Multiplication of exp(i X dot theta) by
(exp(i theta_mu)-1)(exp(-i theta_nu)-1) gives exactly the
four arguments and signs in (8). Thus (9), including every reverse
mixed entry, follows without equating F_mu,nu(X) and F_nu,mu(X).
The diagonal specialization is 2H(X)-H(X+e_mu)-H(X-e_mu).
The Hessian estimate applies only to the smooth leading function:
its four-point difference is a signed integral of a mixed Hessian
over a unit rectangle, which stays outside radius |X|/2 for |X|>=4.
Each of the four scalar remainder values separately is O(|X|^(-4)).
The remaining bounded set of lattice arguments is covered by H(0).
These checks give (1) for the full Frobenius norm, uniformly in signed
j and all spatial points, without differentiating a scalar remainder.

**All spatial and axial tails.** In dimension three the shell count
is O((n+1)^2); the extra squared spatial weight gives a numerator
(n+1)^4, whereas squaring (1) gives eight denominator powers.
The inequality (n+1)^4<=(1+|j|+n)^4 proves the summable majorant
in (11). Taking the complete tail and then its square root gives
q_j(N)<=C_c(1+N+|j|)^(-3/2). Its zero-offset term is finite and
the two signed nonzero tails sum to O(N^(-1/2)) by integration.
Constants are uniform in j before this sum; no fixed-offset limit
or finite preview is used. This proves exactly the eta_N in L116(10),
not the different first absolute moment excluded by L109.

**Both compression defects and the full trace.** Algebraically,
Q_1 S_beta Q_2 A_r-S_beta A_r equals the two terms of L116(9).
Each missing edge or plaquette row samples, through fixed-range
stencils, only energy-kernel outputs at distance at least cN from
the compact input. Both defects therefore retain all their infinite
output rows in the following estimate:

    ||R_Lambda E_j M_f||_HS^2
       <= C p(k)^2 p(l)^2 N^3 (cN)^(-2) q_j(N)^2.

This is the N^(1/2) factor after taking a square root. It restricts
neither covariance sources nor the nonlocal energy output. The
closing factor R_K S_alpha^* P_inf has at most O(N^3) selected
rows, bounded stencil row norms and ||P_inf||<=1, hence
Hilbert–Schmidt norm O(N^(3/2)). Finite rank of M_f justifies the
rectangular trace cyclicity before these two norms are paired.
Their product is N^2 q_(t-s), as in (13).

For a fixed t, min(s,t)<=N and the sum over the original s is
bounded by eta_N. There are fewer than N values of t. Thus the
weighted level count is N^2 eta_N, not a second unrestricted
pair count after eta_N has already summed the offset. The response
is bounded by a N^2 N^2 eta_N=8N^3 eta_N=O(N^(5/2)).
L115(2) confirms the outside factor a and the same scalar product
f in L116(1); L111(13) supplies the unchanged absolute heat envelope
for each of i=3,6. No additional mode degree was introduced, so the
original complete heat sums suffice. Fixed stencil ranges and common
compact support permit one sufficiently fine threshold for both probes.
All colors, generator orientations and both residual forms remain
within the imported exact response; no new factor 3 is inserted.

Finally L118's imported exact R_inf=0 concerns precisely this
comparison, giving the second bound in (3). It does not cancel any
of the earlier variable-coefficient placement errors. The audit
validates a local standard-method input, with no claim of progress
beyond the checked scalar source methods or of a full-response rate.
No numerical experiment or mathematical script is needed for this
analytic audit. The four coefficient remainders and all construction
gaps stated above remain unresolved.

## Mathlib

Full matching matrix-kernel/compression-rate theorem: **not checked**.
Supporting lattice Green asymptotics, Fourier coefficients, finite-rank
and Hilbert–Schmidt trace estimates, finite-difference calculus and
series-tail estimates: **not checked**. Unknown coverage is not absence.
The precise external input is Lawler–Limic Theorem 4.3.1 above, rather
than an assumed general mixed Green-difference theorem.
