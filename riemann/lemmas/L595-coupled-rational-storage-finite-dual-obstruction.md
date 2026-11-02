# Lemma 595: a finite dual excludes the stipulated coupled rational storage family

## Hypotheses

Use L594's exact coordinates and denominator

    v=(x,y,z,X,Y,Z), w=(x,y,X,Y), dot_w=(y,z,Y,Z),
    q(w)=x^2/2+6y^2+X^2/2+6Y^2,
    V(w)=P(w)/q(w) for w!=0, V(0)=0,

where P is any real homogeneous quartic, with no extra coefficient,
parity, positivity or support restriction. Let H be any real symmetric
six-by-six matrix satisfying both inequalities at every v in R^6:

    v^T H v-DV(v)>=0,
    v^T H v-DV(v)-(xz-y^2)>=0.                            (1)

Here DV=gradient V(w) dot dot_w, including the origin as in L594.
Use the exact full matrix, in the displayed coordinate order,

    K_((r,j),(s,k))=
      integral_(-1/2)^(1/2) Re((iu)^j(-iu)^k exp(i(r-s)u)) du,
    r,s in {0,1}, j,k in {0,1,2}.                         (2)

No positive-definiteness of H or its acceleration block is assumed.
No SOS constraint, fixed state cutoff, sampled spectral condition,
periodic-law realization, dual attainment or cone closure is assumed.

## Conclusion

The finite certificate specified and verified below gives

    trace(HK)>9/1000>1/288,
    9/1000-1/288=199/36000.                               (3)

Thus this entire P4/q family cannot meet the stipulated cost below
1/288, even before imposing the closed-I spectral-cone condition.
The bound covers polynomial nonnegativity itself, not just an SOS
subclass. It neither excludes other denominators or general coupled
storage nor constructs a periodic bulk or proves any actual-Xi sign.
This is a computer-assisted specialization of the assessed sufficient
method and finite weak duality. The independent conceptual and
exact-rational certificate audit in Section 6 passed on 31 October 2026.
The exact certificate and all numerical failure evidence are retained.
No RH resolution or certified originality is claimed.

## Proof

### 1. Known method and exact acceleration reduction

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-31-coupled-rational-global-certificate-scope.md`.
Reuse the sufficient rational pointwise-dual method in
A. Chernyavsky, J. J. Bramburger, G. Fantuzzi and D. Goluskin,
*Convex relaxations of integral variational problems: pointwise dual
relaxation and sum-of-squares optimization*,
[arXiv:2110.03079v1, Lemma 2.1, (2.4)--(2.11), and Remark 3.1,
printed pp.8--10 and 14--16](https://arxiv.org/pdf/2110.03079v1).
The C1 zero-flux formulation is G. Fantuzzi,
*Verification of some functional inequalities via polynomial
optimization*, [arXiv:2201.00362v1, Lemma 5, (7)--(10), PDF p.3](https://arxiv.org/pdf/2201.00362v1).
L594 checks the exact denominator's zero extension and growth. These
imports motivate the certificate class; no converse, strong duality,
fixed-degree completeness or source manuscript audit is imported.
The new work is the finite certificate for these exact data and cost.

For completeness the acceleration reduction used to find it retains
all singular cases. Reorder v as (w,a), where a=(z,Z), and write

    v^T H v=w^T E w+2a^T B w+a^T C a,
    g=(V_y,V_Y), d=V_x*y+V_X*Y,
    l_b=Bw-g/2-b*(x,0)/2, r_b=w^T E w-d+b*y^2.

The b-th branch, b=0,1, is a^T C a+2a^T l_b+r_b. It is
nonnegative for all a exactly when

    C>=0, l_b in range(C), r_b>=l_b^T C^+ l_b,           (4)

or equivalently [[r_b,l_b^T],[l_b,C]]>=0. To check (4),
diagonalize the real symmetric C. A negative eigenvalue gives a
negative quadratic along its eigenvector for large |a|. A nonzero
linear coefficient in a null direction is unbounded below in one
sign. On every positive eigenspace complete the square; the minimum
is r_b-l_b^T C^+l_b. Conversely these same squares are nonnegative
under (4). This includes C=0 and rank-one C. At w=0, L594 gives
g=d=0, so the condition reduces precisely to C>=0. Finite sampling
of w alone is not sufficient for a primal global certificate.

### 2. Finite positive matrix tests give a global lower bound

Fix any nonzero real state w_i=(x_i,y_i,X_i,Y_i), a real two-by-four
matrix R and a real two-by-two matrix A. These may be chosen freely;
they are not assumed to equal the conditional moments of any law.
Write (d_0,d_1)=R w_i for this fixed i and define the six-by-three matrix

    T_i=[[x_i,    0,    0],
         [y_i,    0,    0],
         [d_0,  A_00, A_01],
         [X_i,    0,    0],
         [Y_i,    0,    0],
         [d_1,  A_10, A_11]].                            (5)

Write B_i for the symmetric three-by-three matrix satisfying

    xi^T B_i xi = xz-y^2 at v=T_i xi.

Its 00 entry is x_i d_0-y_i^2, its first off-diagonal row is
x_i A_0*/2, and its lower two-by-two block is zero.

For a fixed P let g_i=gradient(P/q)(w_i). The quotient is even and
homogeneous of degree two, so gradient V(t w_i)=t g_i for every real
t, including t=0 by L594. Hence DV(T_i xi) is a quadratic form
xi^T F_i(P) xi, where

    F_i(P)_00=g_i dot (y_i,d_0,Y_i,d_1),
    F_i(P)_0a=(g_i,y A_0a+g_i,Y A_1a)/2,
    F_i(P)_ab=0 for a,b in {1,2}.                         (6)

Here A_0a and A_1a refer to columns a-1 of A, and g_i,y and g_i,Y
are the components differentiating in y and Y. Formula (6) is also
valid when the first coordinate of xi is negative or zero. Thus (1)
implies, for b=0,1,

    T_i^T H T_i-F_i(P)-b B_i>=0.                         (7)

Choose symmetric PSD matrices Y_i,b and nonnegative weights lambda_i,b.
For any PSD M, trace(Y_i,b M)>=0: write Y_i,b=L L^T and sum the
quadratic forms of M on the columns of L. Applying this to (7) and
summing gives

    trace(H sum_i,b lambda_i,b T_i Y_i,b T_i^T)
      >=sum_i,b lambda_i,b trace(Y_i,b F_i(P))
          +sum_i lambda_i,1 trace(Y_i,1 B_i).              (8)

Consequently exact covariance K and cancellation of every quartic's
flux on the right give a lower bound for every H,P in (1). The
matrices are merely finitely many tests of a global inequality; they
need not be a probability law, occupation law, or stationary process.

### 3. Exactly 46 equations suffice for all quartics

Divide P, as a polynomial in x, by q, whose leading x coefficient is
1/2. Homogeneity preserves degrees, giving uniquely

    P=q W+S,

where W is a homogeneous quadratic and S is a homogeneous quartic
with x-degree at most one. There are 25 monomials for S: 15 with
x-degree zero and 10 with x-degree one. No restriction on P results
from this division.

Under exact covariance (2), every quadratic W has zero derivative
expectation. Indeed, for state derivative orders j,k in {0,1},

    K_((r,j+1),(s,k))+K_((r,j),(s,k+1))=0,               (9)

because the two integrands in (2) have the common factor multiplied
by iu+(-iu)=0. For W=w^T S_0 w, its derivative is
dot_w^T S_0 w+w^T S_0 dot_w. Its expected value is zero by (9),
including both copies of every off-diagonal term. This uses only the
raw second matrix, with no centering or independence premise.

It therefore suffices to enforce the 21 upper-triangular covariance
entries and 25 flux equations for the remainder monomials. For each
pair (i,b), let a_i,b be the column of these 46 quantities:

    ((T_i Y_i,b T_i^T)_jk for 0<=j<=k<6;
     trace(Y_i,b F_i(w^e)) for |e|=4, e_x<=1).            (10)

Order the pairs (j,k) increasingly in lexicographic order, and the
four-tuples e in increasing lexicographic order. The target vector is
t(K)=(the corresponding 21 entries of K;25 zeros). Equations

    sum_i,b lambda_i,b a_i,b=t(K)                       (11)

imply the required full covariance and flux cancellation for every
real quartic, by division and (9). All 36 covariance entries are then
fixed; using 21 equations does not halve any off-diagonal trace term.

### 4. Exact rational data and a correction to the exact K

The complete finite data are in
`scripts/coupled-flux/rational_schur_dual_inputs.json`, SHA-256

    0178c10b3da0315bf2c67b0715e2f6c41b5a84c8714f516541c3b8d28b41647b.

There are N=1536 states. The `state_integers` are divided by the exact
integer `state_integer_denominator`=10^12. `mean` and
`acceleration_transform` specify R and A in (5). Every string in
these two arrays and in `dual_cholesky` denotes its exact finite
decimal rational, not an uncertainty interval or a binary float.
The latter array specifies 3072 real matrices L_j and Y_j=L_j L_j^T.
Indices 0,...,N-1 use b=0 and N,...,2N-1 use b=1, with state i
given by the index modulo N. Thus PSD of all Y_j is exact by their
definition, without an eigenvalue test. The 46 distinct indices in
`selected_matrix_indices` specify the only weights to be corrected.
All remaining weights stay one.

Let M be the 46-by-46 matrix with columns a_j at these selected
indices, in their saved order. Put

    r=t(K)-sum_j a_j, beta_j=trace(Y_j B_i) if b=1,
    beta_j=0 if b=0, beta=sum_j beta_j.

The selected weights are 1+delta_j, where delta solves M delta=r.
Thus an invertible M and a bound ||delta||_infinity<1 prove existence
of positive weights satisfying (11) with the exact K, not a Taylor
approximation to K.

The verifier constructs a finite-decimal approximate inverse B of M.
The entries of B are treated as exact real numbers for the subsequent
residual calculation. The elementary Neumann-series criterion gives

    eta=||I-BM||_infinity<1
      => M invertible,
    ||delta||_infinity
      <=||Br||_infinity/(1-eta).                          (12)

Indeed BM=I-(I-BM) is invertible by the absolutely convergent matrix
geometric series, so the square matrix M is invertible, and
delta=(BM)^(-1)Br. This is only a finite-dimensional inverse residual
bound, not an attainment or numerical-convergence assertion.

All entries of M are rational. The only nonrational data in r are
the entries of the exact K. To enclose them, use the order-24 integral
Taylor polynomial and the order-25 remainder in L594 Section 4.
In original coordinates the off-lag entry error is at most

    2/[25! 2^(j+k+25)(j+k+26)],                           (13)

and same-lag entries are exact. The bound follows by the exponential
Taylor remainder for |u|<=1/2 and exp(1/2)<2. Each enclosure contains
the corresponding integral (2). The identity (9) is an identity for
the exact integral and is not inferred from truncation or rounding.

### 5. Complete interval verification and quantitative separation

Reproduce the finite verification, from the active notebook, by

    OPENBLAS_NUM_THREADS=1 python3 scripts/coupled-flux/certify_rational_schur_dual.py

It reads the fixed rational input file. It does not rerun the floating
optimizer unless `--regenerate-inputs` is explicitly requested; that
option is not part of reproducing this fixed certificate. Full
enclosures, the approximate inverse, every inverse-residual entry,
all 46 moment residuals and preconditioned residuals, selected
objective terms and input/verifier hashes are written to
`scripts/coupled-flux/rational_schur_dual_certificate.json`.
Replaying the same exact data with `--precision 120` passes the same
five named rational bounds; the full independent-precision output is
`scripts/coupled-flux/rational_schur_dual_certificate_precision_120.json`.
This precision replay is not a separate conceptual audit.

The verifier evaluates all 3072 columns, all 25 remainder gradients
at every state, and all entries needed for (10)--(13). Its interval
arithmetic uses 90-digit Decimal contexts with ROUND_FLOOR for lower
endpoints and ROUND_CEILING for upper endpoints. Addition uses the
corresponding endpoints; multiplication bounds all four endpoint
products; division uses the reversed reciprocal endpoints and rejects
denominators containing zero. Integer powers use interval products.
Every state's q has a strictly positive lower bound. Infinity norms
use an upward-rounded sum of interval absolute upper bounds. The
approximate inverse need not be accurate by construction: all 46^2
entries of I-BM are independently enclosed by these interval operations.
Finite decimals in that inverse are exact inputs to this last check.
Floating arithmetic chooses the rational data and correction columns;
none is used by the interval verification or its acceptance tests.

The full certificate verifies these strict rational bounds:

    eta<10^(-70),
    ||Br||_infinity/(1-eta)<3/250,
    beta>459/50000,
    sum_selected |beta_j|<1/100.                         (14)

For reference the 90-digit enclosures give eta<=7.801*10^(-74),
the correction bound <0.011204, beta>0.009180283329,
and the selected absolute objective sum <0.009270065. These short
decimal inequalities are deliberately weaker than the stored bounds;
the program tests (14) directly against rational enclosures. No
displayed rounded preview is used in the proof.

By (12)--(14) the selected weights are between 247/250 and 253/250;
all other weights are one. Thus they are strictly positive. The
resulting corrected objective satisfies

    sum_j lambda_j beta_j
      >=beta-||delta||_infinity sum_selected |beta_j|
      >459/50000-(3/250)(1/100)
      =453/50000>9/1000.                                (15)

The unrounded enclosure supplies the stronger lower value
0.00907642344528..., but (15) is the stated certificate bound.
The exact solution delta may depend on the transcendental entries of
K; (12) establishes its existence and (14) controls it for those exact
entries. No claim that delta itself is a rounded rational solution is
made. Combining (8), (11), the all-quartic cancellation in Section 3
and (15) proves (3).

### 6. Independent conceptual and exact-rational audit

The separate audit used
`drafts/literature/2026-10-31-l595-finite-dual-audit-scope.md`, which
was ready before invocation. It confirmed the necessity argument,
including negative radial scales, zero first coordinate in (5), and
singular acceleration blocks. L594's bounds
|V(w)|<=2 M_0 |w|^2 and |gradient V(w)|<=(2 M_1+48 M_0)|w|
give the required C1 extension for each fixed P; in particular no
acceleration direction is removed at w=0. No uniform bound over P is
needed. Division in the polynomial ring R[y,X,Y][x] is valid because
q has invertible leading coefficient 1/2. It leaves 25 quartic
remainders and a quadratic quotient, with no parity restriction beyond
homogeneous degree four. The exact integral in (2) is symmetric, and
(9) cancels the derivative of every quadratic quotient. This
cancellation is an analytic identity, not a rounded zero in a file.

The Taylor sign and scale check was made directly in physical
coordinates. The coefficient of u^(j+k+n) is
Re(i^(j+3k+n))(r-s)^n/n!. An even power has integral
1/[2^(j+k+n)(j+k+n+1)]; odd powers integrate to zero. Since
j+3k+n and j-k+n differ by 4k, this agrees with L594's formula.
The absolute exponential remainder is bounded by
exp(1/2)|u|^25/25!, and exp(1/2)<2 follows by comparison of its
power series with sum_(n>=0) 2^(-n)=2. Integrating after multiplying
by |u|^(j+k) gives exactly (13). Same-lag entries require no
remainder. The verifier's scaling by (1,4,8,1,4,8) and subsequent
division cancel entry by entry, including both signs of the lag.

The original interval operations were checked individually: constructors
receive exact integers, decimal strings or Decimal values, not floats;
negation and absolute value use exact copy operations; addition and
all four multiplication endpoint products use directed contexts.
Reciprocal reverses endpoints for either sign of a zero-free interval;
all powers used are nonnegative integers. Only the approximate inverse
construction uses nondirected rounding; its finite output is then
treated as exact input to the residual test. Norm sums are rounded
upward. No numerical inverse accuracy or optimizer status is assumed.

Independently reproduce the audit with

    python3 scripts/coupled-flux/audit_rational_schur_dual.py

This script imports neither the original verifier nor NumPy, Decimal,
or the spectral-matrix helper. It reads all exact manifest entries as
Fractions. For each of the 3072 factors L it constructs the three
six-vectors v_l=T_i L[:,l]. Covariance is computed as
sum_l v_l v_l^T, the quartic flux as
sum_l L_0l gradient(P/q)(w_i) dot (v_l,1,v_l,2,v_l,4,v_l,5),
and branch-one objective as sum_l(v_l,0 v_l,2-v_l,1^2).
This gives a separate algebraic implementation of (10). It checks
all 35 formal polynomial divisions, and the corresponding exact flux
identity for every monomial at every matrix: 107520 identities.
Every individual contribution is computed exactly before summation.
For bounded-size rational accumulators an exact number a/b, b>0, is
enclosed by floor(10^160 a/b)/10^160 and ceil(10^160 a/b)/10^160;
integer addition then encloses the complete sum without floating
arithmetic or a cancellation-dependent error estimate.

The full audit certificate is
`scripts/coupled-flux/rational_schur_dual_independent_audit.json`.
For each of the saved 90- and 120-digit certificates the audit checks
the complete manifest hash and dimensions, all 46 baseline, target
and residual enclosures, every entry of the 46-by-46 correction matrix,
and all 46 preconditioned residuals. Each correction-matrix entry and
each of the 2116 entries of I-BM is reconstructed as an exact Fraction;
the saved enclosures contain these values. It also checks every
selected objective, the full objective sum, all norm directions,
the correction division, objective-loss multiplication and final
downward subtraction. The full reconstructed evidence and both
certificates' exact inverse residuals are saved, not just a preview.
All checks passed with an empty failure list; both saved certificates
satisfy all five bounds in (14)--(15). Their saved verifier hashes
match the inspected verifier. The original certificates and manifest
were not regenerated or overwritten.

Thus the independently verified strict bound is already
trace(HK)>453/50000, which implies the stated (3). The exact-K
correction exists by (12), even though its weights need not be
rational, and every weight remains positive. This confirms the
whole-family stop; it is neither a new mathematical discovery nor a
claim that the general storage method or an Xi transfer is complete.

### 7. Scope of the experiment and remaining qualifications

The floating search is `scripts/coupled-flux/rational_schur_probe.py`.
It uses covariance-scaled variables and finite-state Schur LMIs,
including both acceleration directions without sampling them. The
192-state relaxation was inconclusive. In the 1536-state run,
low-barrier iterations became numerically unreliable; their full
diagnostics remain in `rational_schur_probe_1536.json`. The separate
`rational_schur_probe_stable.json` retains the earlier numerically
stationary dual used only to generate the rational input file.
All associated maps and iterates are retained. Neither numerical
stationarity nor finite-state primal feasibility is used in (3).

L594's rejected cheap candidate and the L590/L592/L593 stops remain
unchanged. This proof differs from an SOS-only infeasibility claim:
(7) is necessary for every global certificate in the entire stipulated
family, and its finite PSD tests yield an exact lower bound. It does
not assert feasibility at that bound, sharpness, periodic realization,
fourth/probability assembly, or controlled nonlinear transfer to Xi.
Section 6 audits this finite certificate and its whole-family
interpretation. The source manuscripts retain their previous
qualifications; no broader method or actual-Xi conclusion is audited.

## Mathlib

Full matching Mathlib coverage for this fixed coupled rational family
and finite certificate has not been checked. Polynomial division,
PSD congruence and trace, finite matrix inversion, geometric series
and interval arithmetic are supporting mathematics, not a claimed
formal verification of this result. The stored certificate is checked
by the stated Python verifier and the independent exact-rational
auditor; neither is a Lean proof. Unknown
coverage is not evidence of absence.
