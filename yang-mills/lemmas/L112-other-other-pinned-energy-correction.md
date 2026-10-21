# L112 — The retained pinned energy correction is subcubic

## Hypotheses

Use L111's exact R_pin, both actual L010 probes i=3,6, SU(2), the
straight lower-rooted direction-1 forest, all-face relative fixed-link
box (-4,4)^4, sufficiently fine admitted even N, a=8/N and tau=1/16.
Take the bare small-coupling coefficient at fixed mesh before refinement.
Coordinates, incidences and norms here are ordinary stored ones:
incidence entries are 0,+1,-1. Retain every interior axial level,
transverse end row, exterior heat mode and both generator orientations.
Import L111(1)--(4), including its actual staggered F coefficients,
middle finite gradient projection P and min(s,t). No multiplier is
commuted with P. The displacement support and its fixed stencil
enlargement lie a fixed physical distance from all four faces, by
L028 and L111. Constants may depend on that distance and the fixed
data, but not on N or the heat labels.

At each axial level D is the transverse relative circulation. On the
concatenated levels write Dcal=I tensor D. Let L_1 be the unprojected
dimensionless relative Hodge Laplacian on the three transverse link
components with axial vertex coordinates; equivalently
L_1=L_D tensor I+I tensor Delta_T. Let L_2 be its relative Laplacian
on the three transverse plaquette components, again with axial vertex
coordinates. Let J_1,J_2 extend these finite arrays by zero into their
infinite four-dimensional arrays, preserving lower-vertex indices and
component labels. The full-grid operators are D_inf and L_inf, with
L_inf the scalar nearest-neighbor Laplacian on each component.
J_2 is the levelwise version of L111's J. All real transposes on the
infinite grid below mean Hilbert-space adjoints.

## Conclusion

For any collection Omega_N of finite plaquette output rows with at
most C_0 N^4 rows and distance at least delta N from every face,
where delta>0 is fixed, the actual energy difference satisfies

    ||R_Omega Bcal||_HS <= C_delta log N,
    Bcal=[B_ts]_(t,s=1,...,N-1).                         (1)

Here B_ts is exactly L111(3), not a changed covariance. In particular,
for its retained generator-ordered trace,

    |R_pin| <= C_i N^(5/2) log N = o(N^3),
    lim_(N->infinity) a^3 R_pin = 0,   i=3,6.          (2)

The comparison retains all boundary input rows; only output rows are
localized, as forced by the actual compact generator. It requires
neither summability of a differentiated image series nor an absolute
first moment of either alternating factor. It gives no cubic bound
for L111's moved bulk trace. The cubic errors of L110 and L111 remain
retained and may contribute to the coefficient. No complete other/other
limit, value, joint compensation, finer-scale estimate or logarithmic
coefficient follows. Other response jets, matching, interacting error
<=c_box/2, continuum axioms, reflection positivity, infrared control
and finite positive mass remain unresolved.

## Proof

### 1. Identify the exact energy difference before comparing boundaries

L088/L099 give K_h=L_1^-1 Qcal. Since Dcal Qcal=Dcal,
Qcal commutes with L_1, and Qcal Dcal^T=Dcal^T, exactly

    [E^pin_ts]_(t,s)=Dcal L_1^-1 Dcal^T.               (3)

This removes a projection only inside its circulation sandwich. It
does not alter the P between the two actual F factors in R_pin.
The relative incidences obey Dcal=J_2^* D_inf J_1, including plaquettes
touching fixed links. Consequently (3) equals

    J_2^* D_inf (J_1 L_1^-1 J_1^*) D_inf^* J_2.

The infinite circulation-sandwiched Green operator is defined by its
bounded Fourier multiplier D_inf(theta)D_inf(theta)^*/lambda_4(theta),
with lambda_4=sum_(j=1)^4 4 sin^2(theta_j/2). Its value at the single
zero frequency is immaterial. Integrating the axial Fourier variable
gives exactly L110's r_lambda(t-s)D(theta_T)D(theta_T)^*, using the
inverse recurrence checked there. Thus its compressed blocks are
precisely J^*E_(t-s)J. Neither a mass nor a low-frequency cutoff is
introduced. Using the spectral heat integral for the finite inverse
and the Fourier heat integral for this infinite energy operator gives

    Bcal = integral_0^infinity J_2^* D_inf
       [J_1 exp(-v L_1) J_1^* - exp(-v L_inf)]
                                      D_inf^* J_2 dv.             (4)

The localized integral will be absolutely convergent in Hilbert--Schmidt
norm by the bounds below; this also justifies that representation on
the rows used in (1). The unsandwiched infinite inverse need not be a
bounded operator on l^2. Equation (4) uses only its sandwiched version.

### 2. Bound the short-time heat difference on interior output rows

L003's tensor complex, also used in L024's heat expansion (6), fixes
the component generators exactly. A transverse link component has a
Neumann interval generator in its own edge coordinate (endpoint
diagonal 1), and Dirichlet interval generators in its three vertex
coordinates (diagonal 2). Off-diagonal neighbors have entry -1.
Thus exp(-v L_1) is the subprobability transition matrix of the
continuous-time nearest-neighbor walk with independent rate-one
proposals in each positive and negative coordinate direction: reject
an outward edge-coordinate proposal at an endpoint, and kill a walk
on leaving an interior vertex coordinate. This description verifies
the generator at endpoints, as well as the interior generator. Its
zero extension and the full-grid heat matrix have nonnegative entries
and row and column sums at most one; column bounds follow also from
symmetry. This retains the different component boundary conditions.

Couple the finite and infinite walks by those same proposals until
the first visit to a boundary collar. From a link output row at
distance >=delta' N, failure of this agreement by time v requires
some coordinate displacement to reach c_delta N. The l^1 distance
between their terminal subprobability rows, with the killed mass
represented by a cemetery state and then omitted, is at most twice
that failure probability. Every input row, including outside the
finite link array, is included in this comparison.

For completeness, for one coordinate of the infinite walk X(w),
starting at zero, its independent positive and negative Poisson
clocks imply that

    exp(eta X(w)-2w(cosh eta-1))

is a nonnegative martingale of initial expectation one. Doob's
nonnegative-submartingale maximal inequality therefore gives

    Pr{sup_(0<=w<=v) X(w)>=R}
                       <=exp[-eta R+2v(cosh eta-1)].               (5)

Indeed at a hitting time the displayed martingale is at least
exp(eta R-2v(cosh eta-1)). The same bound holds for -X. For
0<=eta<=1, cosh eta-1<=eta^2. Choose eta=min(1,R/(4v)); when
R/(4v)>=1 the exponent is <=-R/2, and otherwise it is
<=-R^2/(8v). Union over both signs in four coordinates proves

    Pr{a boundary collar is reached by time v}
               <= C exp[-c_delta min(N,N^2/v)].                    (6)

This is an extension of L024's short-time path comparison to times
of order N^2/log N; its earlier Poisson step-count estimate alone
does not give that extension. The martingale calculation provides
the missing diffusive maximal-displacement bound explicitly.

Put T_v=J_1 exp(-v L_1)J_1^*-exp(-v L_inf), and let R_Omega'
restrict to any fixed-stencil enlargement of the interior link rows.
The preceding row comparison gives an l^1 row bound
C exp[-c_delta min(N,N^2/v)] for R_Omega' T_v. The sum of absolute
values in any column is <=2, without an interior-input assumption.
The Schur test, equivalently Cauchy--Schwarz applied to the weighted
row and column sums, therefore gives

    ||R_Omega' T_v|| <= C exp[-c'_delta min(N,N^2/v)].               (7)

Every row of R_Omega J_2^* D_inf samples only the corresponding
interior link enlargement, with bounded dimensionless stencil norm.
D_inf^*J_2 has bounded norm as well. The number of output rows is
O(N^4). The rank bound ||X||_HS<=sqrt(rank X)||X|| now gives, for
the localized integrand I_v in (4),

    ||R_Omega I_v||_HS
                 <= C N^2 exp[-c'_delta min(N,N^2/v)].             (8)

The infinite input space in (7) causes no rank problem: (8) has
finitely many output rows, and the subsequent input restriction only
decreases its Hilbert--Schmidt norm. No boundary input is dropped.

### 3. Bound the long-time circulation heat tails by the full spectrum

The transverse relative complex gives

    Dcal L_1=L_2 Dcal,
    0<=Dcal Dcal^T<=L_2,
    [Dcal Dcal^T,L_2]=0.

These follow directly by tensoring the three-dimensional cochain
identities with the axial interval; L_2 includes the positive axial
Dirichlet Laplacian in addition to the transverse Laplacian. Hence

    ||Dcal exp(-v L_1)Dcal^T||_HS^2
                           <= Tr[L_2^2 exp(-2v L_2)].             (9)

L003's dimensionless sine/cosine spectrum gives for a transverse
plaquette two edge-cosine coordinates and two vertex-sine coordinates,
one of the latter axial. There is no zero eigenvalue. With
r=max_j m_j>=1, its eigenvalue satisfies
4r^2/N^2<=lambda_m<=4pi^2 r^2/N^2, and shell multiplicity is <=Cr^3,
including all three components and the permitted zero edge indices.
Thus, for v>=1,

    Tr[L_2^2 exp(-2v L_2)]
          <= C N^-4 sum_(r>=1) r^7 exp(-c v r^2/N^2)
          <= C N^4 v^-4.                              (10)

The last series bound is <=C x^-4 for x=v/N^2>0. For x<=1 it
follows by grouping r in dyadic shells and comparing the resulting
Gaussian integral; for x>=1, extract exp(-cx/2), bound the remaining
series by sum r^7 exp(-c r^2/2), and use exp(-cx/2)<=C x^-4.
Thus (10) covers long times beyond N^2 as well as all low physical
modes. Output restriction and zero extension do not enlarge (9).

For the infinite term, Fourier Plancherel gives the squared l^2 norm
of any component row of D_inf exp(-v L_inf)D_inf^* at most

    C integral_([-pi,pi]^4)
          lambda_4(theta)^2 exp(-2v lambda_4(theta)) dtheta
                                                      <= C v^-4,           (11)

since c|theta|^2<=lambda_4<=|theta|^2 and the four-dimensional
radial majorant is C integral_0^infinity r^7 exp(-cv r^2)dr.
The transverse circulation symbol obeys ||D_inf D_inf^*||_F
<=C lambda_4, which justifies the first inequality with both
circulations retained. Summing (11) over at most C_0 N^4 output
rows and then restricting inputs gives

    ||R_Omega I_v||_HS <= C N^2 v^-2,  v>=1.          (12)

Here (12) uses the triangle inequality between the finite and infinite
terms, (9)--(11), rather than any unproved image-kernel cancellation.

### 4. Integrate with a fixed logarithmic cutoff

Choose a fixed A sufficiently large that c'_delta A>=6, and take
T=N^2/(A log N). For sufficiently large N, T>=1 and
min(N,N^2/v)>=A log N throughout 0<v<=T. Equation (8) gives

    integral_0^T ||R_Omega I_v||_HS dv
                          <= C N^2 T N^-6 <= C.

Equation (12) gives

    integral_T^infinity ||R_Omega I_v||_HS dv
                               <= C N^2/T <= C A log N.

Minkowski's integral inequality proves (1), and the absolute
Hilbert--Schmidt convergence justifies (4) on these output rows.
This cutoff is an explicit bound on one heat integral, not a
mesh-dependent substitution into a fixed-mass localization theorem.

### 5. Use the actual generator and both axial indices in the trace

The finite operator D H_t of L111 is block diagonal in axial levels,
has uniformly bounded norm, and has nonzero input columns only in
a fixed-stencil enlargement of the displacement support. This
enlargement supplies a collection Omega_N satisfying (1). Therefore,
with X_ts=D H_t B_ts exactly as in L111(4),

    (sum_(s,t) ||X_ts||_HS^2)^(1/2) <= C log N.        (13)

This is the Hilbert--Schmidt norm of the concatenated block matrix
after left multiplication by the bounded block-diagonal D H. The
restriction in (1) is on covariance output rows before that
multiplication, so variable generator coefficients are retained.
L111(13), with the exact middle orthogonal P, gives

    ||Z_(kl;st)||_HS <= C a^2 p(k)p(l) N^(3/2),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l) <= C_i.              (14)

Since there are fewer than N^2 pairs (s,t) and min(s,t)<=N,
Cauchy--Schwarz over both indices implies

    sum_(s,t) min(s,t)||X_ts||_HS
       <= (sum_(s,t) min(s,t)^2)^(1/2)
                          (sum_(s,t)||X_ts||_HS^2)^(1/2)
       <= C N^2 log N.                                (15)

The trace inequality, (14)--(15), and the outside a^-1 of L111(4)
give

    |R_pin| <= C_i a N^(7/2) log N
             =8 C_i N^(5/2) log N.

This is o(N^3), proving (2). All exterior heat labels are summed by
(14); no finite exterior truncation or upper-face source estimate is
used. L111's normalization already retains both generator orientations;
the complete other/other group's outside factor 3 has not been applied
here. The zero scaled value remains zero after that fixed factor.

This is local standard-method progress, classified REPRODUCTION under
the unchanged EXPLORE assessment, without a novelty claim beyond the
checked sources. The finite contraction and relative spectrum are
imported. The specialization is necessary because L024's short-time
entry estimate and L111's infinite-grid moment did not control this
unregularized full-level boundary correction in its actual trace order.
No value or numerical sign of either probe is used.

## Mathlib

Full matching localized pinned-energy comparison and retained trace
estimate: **not checked**. Supporting Doob maximal inequality,
Poisson exponential martingales, Schur test, Fourier Plancherel,
relative cochain identities, Hilbert--Schmidt and integral inequalities:
**not checked**. Unknown availability is not absence. The standard
named inequalities are used in their stated forms; no flow/Ward
finiteness theorem or Yang--Mills construction theorem is imported.
