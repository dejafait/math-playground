# L242 — Quantitative projection removal in the reverse crossed order

## Hypotheses

Use precisely L105--L107's co-closed-base reverse trace R_R: the
relative all-face SU(2) cube, straight lower-rooted direction-1 forest,
sufficiently large admitted even N, a=8/N, tau=1/16, stored coordinates,
bare-first coefficient and both actual probes i=3,6. There is no outside
factor 3. Retain every axial level, transverse end row, constant
component index and exterior heat label. This is not the gradient-base
trace G_R or a transpose of R_L.

On one complete transverse layer use L085's edge space E, plaquette
space F, incidence T, circulation D, Delta_0=T^T T,
Delta_T=TT^T+D^T D, G=Delta_0^-1, P=TGT^T and Q=I-P. In particular
DT=0, D^T D=Delta_T Q and Delta_T commutes with P,Q. Write n=N-1,
L_D for the pinned axial Dirichlet matrix and

    R_ts^epsilon=[(L_D tensor I+I tensor Delta_T+epsilon I)^-1]_ts,
    G_eta=(Delta_0+eta I)^-1,
    U_t^eta=T G_eta W_t^T,
    S_st=1_(t<s)+delta_st/2.                              (1)

W_t and c_(i;kl,a) are the actual filtered generator and heat
coefficients of L105, with displacement at t. Import L105(5) and set

    Z_k(s)=Zeta_k(s)/a,
    O_k(s)=Z_k(s)^T D-D^T Z_k(s)=Omega_k^0(s)/a.           (2)

All coefficients in Z_k remain at their original level s. For
0<delta<=1 put P_delta=T(Delta_0+delta I)^-1 T^T and Q_delta=I-P_delta;
only for notation set Q_0=Q. Neither positive-mass matrix is assumed
idempotent. Take 0<epsilon<=1 and 0<eta<=1. The projection estimate
below also permits eta=0, meaning the original G.

## Conclusion

Define the following reduced regularized trace, with traces on E:

    B_(i,N;epsilon,eta,delta)=a sum_(k,l)c_(i;kl,a) sum_(s,t) S_st {
      Tr[R_ts^epsilon D^T Z_k(s) U_t^eta Q_delta Z_l(t)^T D]
      -Tr[R_ts^epsilon D^T Z_k(s) U_t^eta D^T Z_l(t)] }.    (3)

This is a new approximant after exact circulation identities, not the
literal all-projection substitution in L107(4). In particular, at
delta=0 it equals exactly L106's circulation-only trace
R^0_(i,N;epsilon,eta). Uniformly in epsilon,eta,delta,N, whenever
N sqrt(delta)>=1,

    |R^0_(i,N;epsilon,eta)-B_(i,N;epsilon,eta,delta)|
       <=C_i N^3 delta^(3/4) log(e/epsilon).               (4)

The constant does not deteriorate as eta decreases to zero. The
load-bearing complete axial block estimate is

    sum_(s,t=1)^n ||D R_ts^epsilon D^T||_op
       <=C n log(e/epsilon).                              (5)

Combining (4) with L106, if also N sqrt(epsilon)>=1 and
N sqrt(eta)>=1, gives

    |R_R-B_(i,N;epsilon,eta,delta)|
      <=C_i {N^2+N^3[sqrt(epsilon)+eta^(3/4)/epsilon
                                  +delta^(3/4)log(e/epsilon)]}.     (6)

Thus the explicit finite-inequality choices

    epsilon=N^-1, eta=N^-2, delta=N^(-2/3)

give |R_R-B_(i,N;N^-1,N^-2,N^(-2/3))|
<=C_i N^(5/2)log(eN), within the registered component error budget.
This is a projection/inverse comparison only. A quantitative estimate
of B minus exactly a^-3 K_(i,R) of L107(2) is still missing: its joint
localization, relative-boundary and ordered coefficient comparisons
are unproved. In particular the small middle mass eta cannot receive
a fixed-mass localization theorem by substitution. The separate
2026-10-20 audit in proof section 5 accepts this partial estimate
relative to its stated imported inputs. Other component rates,
complete quantitative L011 assembly, interacting reflected error
<=c_box/2, continuum axioms, infrared control and finite positive mass
remain unresolved.

## Proof

### 1. Reduce the exact ordered product before changing a projection

L105(3), with its two Omega occurrences replaced by a O, gives

    R^0_(i,N;epsilon,eta)=a sum_(k,l)c_(i;kl,a) sum_(s,t) S_st
      Tr[R_ts^epsilon Q (P O_k(s) Q)^T U_t^eta
                                             (Q O_l(t) Q)].       (7)

The coefficient a follows from the original a^-1 and the two factors
a; equivalently a^3 times (7) has exactly L107(4)'s a^4 coefficient.
All finite spaces and levels in this identity are unchanged.

Since DP=0, QD^T=D^T and PT=T, exact multiplication gives

    (P O_k Q)^T=D^T Z_k P,
    Q O_l Q=Q Z_l^T D-D^T Z_l Q,
    Q (P O_k Q)^T U_t^eta=D^T Z_k U_t^eta.               (8)

The last equality uses P T=T next to the explicit T in U_t^eta;
it moves no multiplier through G_eta. Expanding the last factor in
(7) now gives (3) at delta=0, except for a final Q in the second
trace. Cyclicity and Q R_ts^epsilon D^T=R_ts^epsilon D^T remove that
final Q exactly. The latter identity uses commutation of Q with the
covariance and QD^T=D^T, not commutation with Z or W.

This accounts for every projection displayed in (7). The one Q left
between W_t^T and Z_l(t)^T in the first trace is retained. Replacing
only it by Q_delta defines (3); there are no adjacent Q_delta factors
or hidden uses of Q_delta^2=Q_delta. The second trace is unchanged.

### 2. Sum the complete covariance with both circulations attached

Let H(r)=exp(-r L_D). On the full pinned interval L_D=2I-J, where
J has nonnegative nearest-neighbor entries and row sums at most 2.
The exponential series shows H_ts(r)>=0 and

    H(r)1=e^(-2r) sum_(j>=0) r^j J^j 1/j! <=1,
    sum_(s,t) H_ts(r)<=n.                               (9)

This includes both end rows: their missing outward neighbors reduce
the row sums. Finite spectral calculus gives the exact norm-convergent
Laplace representation

    R_ts^epsilon=integral_0^infinity
                    H_ts(r) e^(-epsilon r) exp(-r Delta_T) dr.     (10)

All spectra are finite and epsilon>0, so this representation and its
entrywise axial sum require no limit interchange with the mesh.
By L085's D^T D=Delta_T Q, the squared singular values of D on a
co-closed Delta_T mode are lambda. Consequently

    ||D exp(-r Delta_T) D^T||_op
      <=m(r):=sup_(0<=lambda<=12) lambda exp(-r lambda)
      <=min(12,1/(e r)), r>0.                           (11)

The bound at r=0 is 12; zero curvature-complement eigenvalues cause
no difficulty. The upper spectral bound 12 is the same relative
transverse bound used in L107. It does not impose scalar Dirichlet
conditions on normal link components.

Apply (9)--(11) before taking any product norm in the trace. Positivity
of H_ts(r) yields

    sum_(s,t)||D R_ts^epsilon D^T||_op
       <=n integral_0^infinity e^(-epsilon r) m(r) dr
       <=C n log(e/epsilon).                            (12)

For completeness, the integral from 0 to 1 is at most 12. On
[1,epsilon^-1] it is at most log(epsilon^-1)/e; on the remaining
interval the substitution v=epsilon r bounds it by
(1/e) integral_1^infinity e^(-v)/v dv<=e^-2. When epsilon=1 the
middle interval is empty. This proves (5) uniformly down to any
positive epsilon, with every source and end row retained. It is an
operator-norm sum of the joint two-circulation block; neither an
entrywise covariance estimate nor a first absolute moment of an
individual alternating kernel is being asserted.

### 3. Estimate the sole remaining projection difference

Put E_delta=P-P_delta=Q_delta-Q. L103(16), or equivalently
L107(6), gives on the full pinned transverse vertex spectrum

    ||E_delta||_HS<=C N^(3/2)delta^(3/4),
                                          N sqrt(delta)>=1.       (13)

Indeed its nonzero singular values are delta/(lambda_v+delta).
The pinned vertex modes have lambda_v>=c|m|^2/N^2,
m in {1,...,N-1}^3. With M=N sqrt(delta)>=1 the shells r<=M
contribute at most C M^3 to the squared norm, and those r>M at
most C delta^2 N^4 sum_(r>M)r^-2<=C N^3 delta^(3/2).
An empty high range contributes zero. Thus no low vertex mode is
dropped and no small projection operator norm is assumed.

The imported L103(13)--(14) and L105--L106 energy factorization give

    ||Z_k(s)||<=C p(k),
    ||U_t^eta||=||(T G^(1/2))[Delta_0/(Delta_0+eta)]
                                      (W_t G^(1/2))^T||<=C,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                  (14)

At eta=0 the middle spectral contraction is the identity. In
particular (14) retains W_t's variable displacement and both actual
generator filters in their original order. Both E and F have
dimension at most C N^3, so also ||Z_l(t)^T||_HS<=C N^(3/2)p(l).

Subtract (3) at delta and at zero. The second traces cancel. Only
in this difference cyclically join the two D factors in the first
trace, using the exact rectangular trace identity:

    Tr_E[R_ts^epsilon D^T Z_k U_t^eta E_delta Z_l^T D]
      =Tr_F[(D R_ts^epsilon D^T) Z_k U_t^eta E_delta Z_l^T].        (15)

For B_ts=D R_ts^epsilon D^T, Hilbert--Schmidt duality and
submultiplicativity, in precisely the order (15), give

    |Tr_F[B_ts Z_k U_t^eta E_delta Z_l^T]|
      <=||B_ts||_op ||Z_k||_op ||U_t^eta||_op
                                     ||E_delta||_HS ||Z_l^T||_HS
      <=C N^3 delta^(3/4)p(k)p(l)||B_ts||_op.             (16)

No coefficient or projection has crossed another factor in this
inequality. Using 0<=S_st<=1, (5), (14), and the original a in (3),
the complete signed response difference is bounded by

    C_i a N^3 delta^(3/4) n log(e/epsilon)
       <=C'_i N^3 delta^(3/4)log(e/epsilon),              (17)

because an<=8. This proves (4). The summable heat majorant in (14)
applies before any parameter choices, for both actual probes.

### 4. Combine only uniform finite errors

L106(2) changes the original covariance first and the explicit middle
inverse second with error C_i N^3[sqrt(epsilon)+eta^(3/4)/epsilon]
under its two stated spectral conditions. Its section 4 gives the
full-to-circulation-only error C_i N^2 uniformly in both masses.
Combine those imported inequalities with (4) to obtain (6).

At the displayed schedule the three spectral conditions read
sqrt(N)>=1, 1>=1 and N^(2/3)>=1. The two inverse terms each become
N^(5/2); the projection term is N^(5/2)log(eN). Hence all comparison
errors meet the stated bound. This invokes no fixed-mass trace limit
at varying parameters. The remaining trace B still contains both
original axial levels, S_st, the entire middle inverse and covariance,
Q_delta, every coefficient/filter and the complete heat series.

The subtraction required for the complete target is exactly L107(2).
Nothing here bounds B-a^-3 K_(i,R) at the desired rate, evaluates a
coefficient or supplies a complete L011 estimate. The argument is
local progress by established finite spectral and trace-ideal methods,
classified REPRODUCTION under the unchanged reverse-remainder EXPLORE
assessment. L105--L107 are imported rather than reproved, and no
claim of progress beyond the checked source methods is made.

### 5. Separate critical audit, 2026-10-20

**Verdict:** accept (3)--(6) relative to L085's relative Hodge
identities, L103's pinned shell and energy estimates, L105's actual
layer/exterior normalization and L106's inverse/exterior comparisons.
This audits the existing specialization; it does not independently
reprove those imports, strengthen the rate or certify downstream
localization. The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-20-reverse-crossed-projection-audit.md`.
No numerical or IEEE premise is used in this audit.

First fix the map domains. If V is the pinned transverse vertex
space, then T,W_t:V->E, D,Z_k:E->F, G_eta:V->V and U_t^eta:E->E.
All transposes use the stored inner products. Since
P D^T=0 and D Q=D, one has

    P O_k Q=P Z_k^T D,
    (P O_k Q)^T=D^T Z_k P.

Thus the sign in (8) is positive even though O_k is skew. The
preceding Q disappears next to D^T, and P U_t^eta=U_t^eta because
P T=T for every eta>=0. Expanding Q O_l Q gives exactly the first
word of (3) with Q and the negative second word with an additional
final Q. Cyclicity moves only that final Q to the start; commutation
of Q with R_ts^epsilon and Q D^T=D^T then remove it. This checks
both words without moving Z_k, Z_l or W_t through an inverse.
The prefactor is a^-1 a^2=a, and S_st is unchanged, including its
diagonal half. There is no outside factor 3. Delta=0 is solely
the exact identity case, not a use of the positive-delta shell bound.

For (5), the complete pinned interval has n rows, including 1 and n.
The nonnegative adjacency J has J1<=2 1, hence J^j1<=2^j1 by
induction. Its exponential proves (9) on those same rows.
The Laplace representation (10) is valid in finite dimension at
each positive epsilon. The nonzero singular values of
D exp(-r Delta_T/2) have squares lambda exp(-r lambda) on the
co-closed edge modes: D^T D=Delta_T Q and Q commutes with Delta_T.
This also accounts for the zero complement on F. The complete
relative transverse spectrum lies in [0,12]; normal-link constant
indices are retained, not assigned vertex Dirichlet conditions.
Therefore the triangle inequality under the Laplace integral gives

    sum_st ||D R_ts^epsilon D^T||
      <=integral_0^infinity e^(-epsilon r)
           min(12,1/(e r)) sum_st H_ts(r) dr.

For r=0 use the finite bound 12. The three intervals
[0,1], [1,epsilon^-1], [epsilon^-1,infinity) give respectively
12, log(1/epsilon)/e and at most e^-2. This proves the claimed
Cn log(e/epsilon) without omitting any s,t pair or using positivity
of individual entries of Q. In particular there is no extra n
from summing the second axial index.

For the projection step, V_0=T G^(1/2) is an isometry from V into
E. Consequently

    E_delta=V_0 [delta/(Delta_0+delta)] V_0^T.

Its nonzero singular values are exactly those in (13); no edge
zero-index multiplicity is mistakenly counted as a vertex zero
mode. L103(16)'s full pinned vertex shell bound applies for
N sqrt(delta)>=1 and gives the stated Hilbert--Schmidt exponent.
Meanwhile the exact factorization

    U_t^eta=V_0 [Delta_0/(Delta_0+eta)] (W_t G^(1/2))^T

places the spectral contraction between two bounded factors.
It is valid at eta=0 since Delta_0 is strictly positive on pinned
vertices. The coefficient in W_t stays on its original side; no
eta^-1 factor is introduced. L103(14) supplies the separate Z_k
bound and full polynomial heat envelope used in (14), rather than
inferring a bound on Z_k from a potentially canceling O_k.

Only the first word changes when Q is replaced. Rectangular
cyclicity transfers its trace from E to F exactly as in (15).
For A=B_ts Z_k U_t^eta, the inequality
|Tr_F(A E_delta Z_l^T)|<=||A E_delta||_HS ||Z_l^T||_HS
holds for these compatible maps, and
||A E_delta||_HS<=||B_ts||||Z_k||||U_t^eta||||E_delta||_HS.
Both layer dimensions are O(N^3), so the two Hilbert--Schmidt
costs multiply to N^3 delta^(3/4)p(l). Summing (5), the heat
majorant and 0<=S_st<=1 yields precisely
C_i a n N^3 delta^(3/4)log(e/epsilon); an<=8 gives (4).
This controls every heat label for each actual probe and is
uniform in eta, including zero. No projection idempotence,
coefficient commutator or free reverse-block norm gain is used.

Finally (6) uses L106(2) only at positive eta and epsilon under
both of its spectral conditions, then L106 section 4's uniform
O(N^2) full-to-circulation comparison, then (4). It does not
apply L106's combined positive-eta conclusion at eta=0.
At epsilon=N^-1, eta=N^-2, delta=N^(-2/3) the inverse errors are
both N^(5/2), and the projection error is
N^(5/2)log(eN); the spectral conditions are respectively
sqrt(N)>=1, 1>=1 and N^(2/3)>=1. These are substitutions in
uniform finite inequalities. L107(2) remains the required eventual
subtraction, and no fixed-mass limit is evaluated at varying mass.

No unsupported assertion was found within this audit scope.
The existing direct mathematical inputs are unchanged. The result
is local verification by standard finite spectral and trace-ideal
methods (REPRODUCTION), not progress beyond the sources checked.
It supplies no independent component rates, quantitative L011
assembly, interacting reflected-error estimate or construction.

## Mathlib

Full matching reduced reverse-trace projection estimate: **not
checked**. Supporting finite matrix exponential, spectral calculus,
rectangular trace cyclicity and Hilbert--Schmidt inequality coverage:
**not checked**. Unknown coverage is not evidence of absence. No
external continuum Ward/flow theorem or Yang--Mills construction result
is imported for this isolated bare forest trace.
