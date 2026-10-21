# L098 — A signed limit for the H diagonal's axial generator

## Hypotheses

Use exactly L095's R_H,ax, covariance blocks, actual alternating maps
A_k=Pcal Omega_k Qcal, displacement filters U_s and real symmetric
coefficients c_(i;kl,a). Thus the group is SU(2), the probes are both
actual L010 probes i=3,6, the forest is straight and lower-rooted in
direction 1, the box is D=(-4,4)^4 with all-face relative pinned links,
N is admitted and even, a=8/N and tau=1/16. Take the bare small-coupling
coefficient at fixed mesh before refinement. Coordinates and traces
are ordinary dimensionless stored coordinates. Keep every interior
axial level, transverse end row, ordered plaquette pair including
coincidences, both generator orientations and every exterior heat mode.

Write n=N-1, P for the transverse gradient projection, Q=I-P,
Delta_T for the relative transverse edge Hodge Laplacian and
R=(L_D tensor I+I tensor Delta_T)^(-1). All transverse spaces at
different axial levels are identified using their identical relative
domains. Set W_k(s)=A_k(s)U_s and extend W_k by zero at levels 0,N.
Use L097's continuum v_k, coefficients c_(i;kl), torus symbols
d, eta, lambda, P(theta), C(theta) and z_(v_k). Put Q(theta)=I-P(theta).

## Conclusion

There is a finite real signed functional K_(i,ax) such that

    a^3 R_H,ax -> K_(i,ax).                           (1)

For x in D and theta in [-pi,pi]^3 define

    alpha_k(x,theta)=P(theta) z_(v_k)(x,theta)^* C(theta) Q(theta),
    U(x,theta)=u_1(x) diag_(nu=2,3,4)[eta_nu^2],
    omega_k=alpha_k U,   ell=x_1+4.

Here * is complex conjugate transpose; the actual real matrices give
these Fourier adjoints. At lambda=0 set the displayed integrand to zero.
Then an explicit absolutely convergent formula is

    K_(i,ax)=-sum_(k,l)c_(i;kl) integral_D
       integral_([-pi,pi]^3) Re Tr[
          (Q/lambda) alpha_l^*
              (omega_k/2+ell partial_1 omega_k)] dtheta/(2pi)^3 dx.  (2)

The derivative includes both the actual exterior coefficient and u_1.
The half-weight in (2) is the centered derivative of the prefix kink;
it is not an assumed local replacement of min(s,t). Values and signs
are unevaluated. This proves neither the transverse generator limit
nor the complete H diagonal or other/other limit. In particular it
does not prove the required joint remainder -4 gamma D_i before the
outside factor 3, or compensation of L084's mixed coefficient.
K_(i,Q) from L097 still enters R_H with a minus sign. Independent
response jets, N^2 remainders, slower powers/logarithm, interacting
matching and error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain unresolved.

## Proof

### 1. Exact trace order and coefficient differences

Import L095(9)--(12), including its proof that the two generator
orientations add equally after the symmetric exterior sum and consume
the insertion's factor 1/2 exactly once. In particular

    R_H,ax=a^-1 sum_(k,l)c_(i;kl,a) Tr(K_h B_kl T_1),
    (B_kl)_st=min(s,t) A_l(s)^T W_k(t),
    (B_kl T_1)_st=[(B_kl)_(s,t-1)-(B_kl)_(s,t+1)]/2.   (3)

No transverse factor is commuted in these identities. L095's bounds
give ||A_k(s)||<=Ca p(k), ||W_k(s)||<=Ca p(k),
||W_k(s+1)-W_k(s)||<=Ca^2 p(k), and
||(B_kl T_1)_st||<=Ca^2 p(k)p(l), including the endpoints.
Enlarge the fixed mode polynomial p below as necessary.

We also need the following second difference, only for W_k:

    ||W_k(s+1)-2W_k(s)+W_k(s-1)||<=Ca^3 p(k).         (4)

Here is its applicability argument, rather than an inference from
L095's first-difference estimate. L028(9)--(11) expresses each stored
exterior link as a times the relative smooth mode minus its exact
lower prefix. Two axial differences of the direct smooth mode are
O(a^2 p(k)). Two axial differences of the prefix are a transverse
difference of the difference of two consecutive axial link samples,
also O(a^2 p(k)) before the outer factor a. Consequently b_k,q_k
have second axial differences O(a^3 p(k)). Transverse circulation
annihilates the prefix exactly, so f_k is the direct smooth curvature
sample: its first and second axial differences are respectively
O(a^3 p(k)), O(a^4 p(k)). These estimates use only existing levels
and the bounded multiplicity of the path/circulation selectors in
L088(3). The relative sine/cosine modes have C^r bounds polynomial
in their mode label for each fixed r; their physical spectral gap
controls the square-root inverse. Thus the complete Omega_k and
A_k have second axial differences O(a^3 p(k)). Fixed P,Q do not
depend on level. U_s has first and second differences O(a), O(a^2),
by the smooth displacement and its actual endpoint averages.
The discrete product identity proves (4). W_k is identically zero
in fixed physical collars of both axial ends; zero extension therefore
preserves (4), without extending an exterior prefix through the upper pin.

For each fixed k these same formulas give convergence, on the
displacement support, of the normalized exterior coefficients and
their first axial differences to their continuum values and derivatives.
To see the derivative assertion explicitly, the first difference of
the prefix is its one new summand, while the direct part is a smooth
mode difference. The normalized difference quotient converges to
the axial derivative of the prefix integral. L080(8)--(10) retains
the constant axial mode and gives the same conclusion for every fixed
positive axial frequency. Neither statement changes the upper pin.

### 2. Transverse mass regularization controls every low mode

For 0<epsilon<=1 set

    K_h,epsilon=(L_D+Delta_T+epsilon I)^-1 Qcal.

For scalar lambda>0 the entries of R_lambda=(L_D+lambda I)^-1
are nonnegative by L095's discrete minimum principle. The resolvent
identity gives entrywise nonnegativity of R_lambda-R_(lambda+epsilon).
Moreover

    sum_t (R_lambda-R_(lambda+epsilon))_st
                   <=epsilon/[lambda(lambda+epsilon)].              (5)

Indeed the resolvent difference is epsilon R_lambda R_(lambda+epsilon),
and each inverse has row sum at most its inverse mass, as in L095(13).
Each corresponding transverse block is positive semidefinite after
spectral decomposition on Q. Therefore (3)'s block bound and (5) give

    |a^3 [R_H,ax-R_H,ax,epsilon]|
      <=C_i a^4 n Tr_Q[epsilon/(Delta_T(Delta_T+epsilon))]
      <=C'_i sqrt(epsilon),                          (6)

where R_H,ax,epsilon denotes (3) with K_h,epsilon. For completeness,
L086/L095's three-dimensional spectrum has lambda>=4r^2/N^2 in
shell max_j m_j=r, with at most Cr^2 labels. Its positive trace is
bounded by

    C epsilon N^4 sum_(r=1)^(N-1) 1/(r^2+epsilon N^2)
                                                   <=C N^3 sqrt(epsilon).

The last inequality follows by comparison with the integral of
1/(t^2+epsilon N^2) on t>=0, since the summand is decreasing.
Multiplying by a^4 n proves (6). This includes all low transverse
and axial modes and does not commute coefficients with a cutoff.

### 3. The differentiated prefix and its half-weight

Fix epsilon>0. Write

    D_c W_k(t)=[W_k(t+1)-W_k(t-1)]/2,
    h_st=1 if t<s,  h_ss=1/2,  h_st=0 if t>s.

The centered difference of min(s,t), with the zero-extended W at
the endpoints, and the product identity in (3) give

    (B_kl T_1)_st
      =-A_l(s)^T [h_st W_k(s)+s D_c W_k(s)] + E_(kl;st),
    ||E_(kl;st)||<=C a^3 p(k)p(l)(1+|t-s|).           (7)

To verify the error explicitly, first freeze only min(s,t) in the
product identity at t. Its centered derivative is h_st exactly.
The two cross products of a first difference of min and W contribute
at most Ca^3 p(k)p(l). Replace W(t) by W(s), at cost
Ca^3 p(k)p(l)|t-s|. Replace D_c W(t) by D_c W(s), using (4),
at cost Ca p(l) N a^3 p(k)|t-s|<=Ca^3 p(k)p(l)|t-s|.
Finally replace min(s,t) by s in its coefficient of D_c W(s);
its error is at most Ca^3 p(k)p(l)|t-s|. This proves (7) at
all levels; only W, not A_l, was extended beyond its natural levels.

The needed scalar axial kernel estimates can be checked directly.
For mass m=lambda+epsilon in [epsilon,13], define kappa>0 by
2cosh(kappa)-2=m. On the infinite axial lattice

    r_m(j)=exp(-kappa |j|)/(2sinh kappa),
    sum_j r_m(j)=1/m,
    sum_j (1+|j|)r_m(j)<=C_epsilon.                   (8)

The recurrence verifies the inverse at j=0 and elsewhere; the
geometric series proves both sums. The finite Dirichlet inverse
is bounded entrywise by this kernel, by the minimum principle.
Thus its transverse blocks, including Q, satisfy

    sum_(s,t)(1+|t-s|)||(K_h,epsilon)_ts||_1
                                                   <=C_epsilon N^4. 

Using (7) in the exact trace therefore costs at most
C_(i,epsilon) a^2 N^4=O_(i,epsilon)(N^2) before scaling.
This is o(N^3) for each fixed epsilon.

One must still evaluate the kink weight rather than incorrectly
replace the derivative by its diagonal value. On the infinite line,
symmetry and h_ss=1/2 imply

    sum_t r_m(t-s) h_st=1/(2m).                      (9)

For s a fixed physical distance from both ends, the corresponding
finite sum differs by at most C_epsilon exp(-c_epsilon N), uniformly
in lambda. Indeed the deficit of its full row sum from 1/m solves
the homogeneous recurrence with endpoint values 1/m and is bounded
by (exp(-kappa s)+exp(-kappa(N-s)))/m. The omitted infinite tails
have the same exponential bound, by (8). Since 0<=h<=1, this also
bounds the difference of the weighted sums in (9).
Only W_k(s) and D_c W_k(s) occur in (7)'s main term. They vanish
in fixed physical endpoint collars. Hence the possibly nonsymmetric
finite kernel near an endpoint cannot produce a leading term there.
The same row-sum estimate applies to the coefficient of s D_c W.
Spectral decomposition proves these replacements in transverse
operator norm before multiplication by A_l(s)^T; no variable
multiplier is moved across an inverse. Summing their exponentially
small errors over all rows and heat modes is negligible. We obtain

    R_H,ax,epsilon
       =-a^-1 sum_(k,l)c_(i;kl,a) sum_s Tr_T[
          (Delta_T+epsilon)^-1 Q A_l(s)^T
                        (W_k(s)/2+s D_c W_k(s))]
          +O_(i,epsilon)(N^2).                      (10)

This is a regularized finite-trace reduction with the exact prefix
and both orientations retained through (3), not a generator version
of L097's curvature-row energy estimate.

### 4. The regularized transverse trace limit

Put alpha_(k,a)=A_k/a, omega_(k,a)=W_k/a and
dot omega_(k,a)=D_c W_k/a^2. Multiplying (10) by a^3 leaves
the normalized trace

    -a^4 sum_(k,l)c_(i;kl,a) sum_s Tr_T[
       (Delta_T+epsilon)^-1 Q alpha_(l,a)(s)^T
                    (omega_(k,a)(s)/2+a s dot omega_(k,a)(s))].     (11)

All normalized coefficient factors have bounds polynomial in k,l.
For fixed epsilon the inverse has norm <=1/epsilon. The transverse
projection occurrences are treated as in L097's finite-range proof,
with an independent parameter delta>0:

    P_delta=T(Delta_0+delta I)^-1 T^T, Q_delta=I-P_delta,
    ||P-P_delta||_HS<=C N^(3/2) sqrt(delta).

The inequality follows from the shell trace bound Tr Delta_0^-1<=CN^3
and [delta/(lambda+delta)]^2<=delta/lambda. Telescope every P,Q
occurrence in (11), including those in the derivative of W. They
are fixed level-independent factors. Trace Cauchy--Schwarz bounds
the normalized error by C_(i,epsilon) sqrt(delta), uniformly in N;
one factor has Hilbert--Schmidt norm O(N^(3/2) sqrt(delta)), the
remaining bounded product has Hilbert--Schmidt norm O_(epsilon)(N^(3/2)),
and a^4 times the number of levels times N^3 is bounded.

For fixed epsilon,delta approximate each inverse on its finite
spectral interval by L097's explicit uniformly convergent geometric
polynomials. The telescoped normalized trace errors tend uniformly
to zero with the polynomial approximation errors. The resulting
traces contain only fixed-range closed walks. Their transverse
boundary collar has O(N^2) rows per level and bounded normalized
entries, so its total contribution is O_(epsilon,delta)(1/N).
All axial coefficients W and their differences have compact support.
In the remaining rows coefficients can be frozen over a fixed walk
with an error tending to zero. The axial derivative coefficients
converge by section 1; for each fixed mode pair all relevant spatial
coefficients and first axial derivatives are uniformly continuous
on the displacement support. Staggered offsets tend to zero as well.
The Riemann-sum theorem therefore identifies the trace limit with
the integral of its frozen transverse Fourier trace.

Send polynomial degrees to infinity, then delta to zero. The uniform
errors just established justify the order. At fixed epsilon the torus
integrands are bounded by C_(epsilon)p(k)p(l), so dominated convergence
removes projection regularization. In the leading alternating block,
L088's exterior-circulation terms divided by a tend to zero, including
their normalized axial differences, by section 1. The other terms
give P z_(v_k)^* C Q, exactly as in L097's symbols; the C^* term
on the left vanishes since P C^*=0. No variable-coefficient identity
of that kind was assumed before the finite-trace approximation.
L095's actual C_nu^T M_(u_1) C_nu has frozen symbol
u_1 eta_nu^2. The derivative keeps both factors alpha_k and U.
Thus (11) tends, for fixed epsilon, to formula (2) with
Q/lambda replaced by Q/(lambda+epsilon).

### 5. Remove the transverse mass and retain the full heat sum

On the torus ||C||<=C sqrt(lambda), ||z_(v_k)||<=Cp(k),
and the same bound holds for its first axial derivative with enlarged p.
Hence ||alpha_k||+||partial_1 alpha_k||<=Cp(k)sqrt(lambda).
U and partial_1 U are bounded. The integrand with inverse
lambda+epsilon is consequently bounded by Cp(k)p(l), independently
of epsilon; it converges almost everywhere to (2). Dominated convergence
gives its limit as epsilon decreases to zero. Alternatively the
three-dimensional integrability of 1/lambda suffices here.
Combining that limit with the uniform finite-trace error (6) proves (1).
The original unregularized trace is never replaced in operator norm
at its singular low modes.

L088/L097's actual coefficients have a uniform summable heat majorant

    |c_(i;kl,a)|p(k)p(l)
       <=C p(k)p(l) exp[-(tau/16)(|k|^2+|l|^2)].

The original scaled trace is bounded modewise by Cp(k)p(l), by L095;
so are (6) and the torus limit. Fixed-epsilon estimates may have
epsilon-dependent constants, but the same majorant sums them at
each fixed epsilon. Modes absent at a mesh are extended by zero,
and fixed-pair coefficients converge as in L097. Finite-pair limits
followed by these full heat-tail bounds justify every exterior sum
and the absolute convergence in (2). The real original traces give
the real part displayed there; no sign is inferred.

This is one RESEARCH / REPRODUCTION specialization under unchanged
EXPLORE coverage in
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
It imports the finite contraction and specializes the existing pinned
spectral and finite-range methods to the actual differentiated prefix.
It claims local progress, without certified originality or a result
beyond the checked source methods. No numerical script, sign certificate
or new continuum Ward/flow theorem is used.

## Mathlib

Full matching signed-limit theorem: **not checked**. Supporting finite
spectral decomposition, discrete minimum principles, trace ideals,
geometric kernel sums, Riemann sums and dominated convergence: **not
checked**. Unknown availability is not absence. No standard flow result
assigns this isolated group's coefficient here.
