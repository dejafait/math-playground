# L239 — Ordered projection error for the local left crossed trace

## Hypotheses

Use L100(1),(7),(10)--(11), L237 and L238 on the relative all-face
pinned SU(2) cube, straight lower-rooted direction-1 forest, sufficiently
large admitted even N, a=8/N, tau=1/16, ordinary stored coordinates,
bare-first coefficient and both actual probes i=3,6. Retain every
relative source/end row, axial level, allowed constant component index,
actual endpoint/clover filter and exterior heat label. The imports
L237 and L238 still await separate critical audit.

Write P,Q=I-P,T,Delta_E,Delta_0 as in L100, and for
0<epsilon,delta<=1 put

    R=(Delta_E+epsilon I)^(-1),
    P_delta=T(I_ax tensor (Delta_0+delta I)^(-1))T^T,
    Q_delta=I-P_delta, D=Q_delta-Q=P-P_delta,
    G=aG0, V=sum_(mu=2)^4 H_av U_mu C_mu,
    A_0=P G-T V, A_delta=P_delta G-T V.                 (1)

The axial tensor identity in P_delta is understood as in L100(11).
Use the complete unnormalized skew Omega_k=F_k+H_k of L088(3)
and L089(1), and the full actual coefficients c_(i;kl,a).
Define grouped factors, separately for each heat label,

    X_(0,k)=R Q Omega_k^T P,
    Y_(0,l)=R Q Omega_l Q,
    X_(delta,k)=R Q_delta^2 Omega_k^T P_delta,
    Y_(delta,l)=R Q_delta^2 Omega_l Q_delta.             (2)

Thus the exact local massive trace in L238 is

    R_(loc,epsilon)=a^-1 sum_(k,l)c_(i;kl,a)
                                      Tr(X_(0,k) A_0 Y_(0,l)).

Let its literal projection-regularized companion be

    R_(loc,epsilon,delta)=a^-1 sum_(k,l)c_(i;kl,a)
                         Tr(X_(delta,k) A_delta Y_(delta,l)). (3)

This is precisely L100(10)--(11)'s substitution, in unnormalized
Omega coordinates. The squares Q_delta^2 retain the two adjacent
occurrences from K_(epsilon,delta) and the projected alternating
factor; Q_delta is not treated as idempotent. The P inside A_0
is replaced as well. T,V,G and all their original orders remain.

Import L226(4)--(8),(10)--(11) only as finite spectral and
unprojected composite inequalities on the identical relative spaces.
Its co-closed trace conclusion is not imported for (3).

## Conclusion

Uniformly in these masses and meshes,

    |R_(loc,epsilon)-R_(loc,epsilon,delta)|
       <=C_i[N^3 delta^(3/4)epsilon^(-1/2)
                           +N^(5/2)sqrt(log(eN))].       (4)

Consequently L238(4), with its imported L237 mass error, gives

    |R_L-R_(loc,N^-1,N^(-4/3))|
                         <=C_i N^(5/2)sqrt(log(eN)).    (5)

This controls all projection replacements in the local crossed
product, including P inside A_loc. It does not bound the remaining
regularized trace in (5). Its quantitative localization,
coefficient-freezing and relative-boundary comparison remain open;
no O(N^(5/2)log(eN)^2) bound for complete R_L is established here.
Other L011 rates and full assembly, interacting reflected error
<=c_box/2, continuum axioms, infrared control and finite positive mass
remain independent gaps. This partial specialization requires separate
critical audit; there is no complete-solution candidate.

## Proof

### 1. Two distinct alternating/resolvent placements

Put L_N=log(eN) and

    E_N=N delta^(3/4)epsilon^(-1/2)+sqrt(N L_N).

L226(4)--(5) gives, on the present full finite spaces,

    Cc D=0, QD=DQ=0,
    ||D||_HS<=C N^2 delta^(3/4).                        (6)

D,P_delta,Q_delta commute with R and with one another; all are
symmetric contractions. These are spectral relations, not
commutation statements about Omega or G. In particular

    Q_delta^2=Q+D^2.                                   (7)

L226(6)--(8) applies before any gh/hh selectors, including to R
rather than RQ. Its row-product proof explicitly retains all
staggered boundary exceptions in the fixed-width physical collar.
On these same spaces its conclusions are

    ||H_k R||_HS<=C p(k)N,
    ||H_k R D||_HS<=C p(k)E_N.                         (8)

Here p is the fixed modal polynomial, enlarged when necessary.
For the other placement L226(10)--(11) proves

    H_k D=-Cc^T M_(b_k) Bq D+Cc^T M_(q_k) Bb D,
    ||R H_k D||_HS
                   <=C p(k)N delta^(3/4)epsilon^(-1/2). (9)

The applicability is exact: D has the finite transverse gradient
range, so the two right-circulation terms vanish by Cc D=0;
the other two terms keep their multipliers in place. The form
Cc^T Cc<=Delta_E gives ||R Cc^T||<=1/(2 sqrt(epsilon)).
With ||b_k||_infinity+||q_k||_infinity<=Ca p(k), bounded path
norms and (6), this gives (9). In particular (8) and (9) address
different products; neither uses a transpose to commute R through H.

Both exterior-circulation terms F_k are retained. L088(5), bounded
path multiplicity and the complete inverse-square bound L090(8)
give

    ||F_k||<=C a^2 p(k),
    ||R||_HS<=C N^2 sqrt(L_N),
    ||F_k R||_HS+||F_k R D||_HS+||R F_k D||_HS
                                      <=C p(k)sqrt(L_N). (10)

For each term use the operator ideal inequality, ||D||<=1 and
a^2 N^2=64; no derivative of f_k or projection commutation is needed.
Since sqrt(L_N)<=C N and sqrt(L_N)<=sqrt(N L_N), adding (8)--(10)
proves all three bounds

    ||Omega_k R||_HS<=C p(k)N,
    ||Omega_k R D||_HS<=C p(k)E_N,
    ||R Omega_k D||_HS<=C p(k)E_N.                     (11)

Skew-symmetry Omega_k^T=-Omega_k and symmetry of R,D also give
||R Omega_k||_HS<=C p(k)N and
||R D Omega_k^T||_HS=||Omega_k R D||_HS<=C p(k)E_N.
All covariance sources and normal end rows remain in these full
Hilbert--Schmidt norms. The collar term in (8) is retained in E_N,
not assigned any delta-dependent gain.

### 2. Count both occurrences of Q_delta and the gh projection

Contractions and commutation of R with Q_delta,P_delta, together
with (11), imply for s=0,delta

    ||X_(s,k)||_HS<=C p(k)N,
    ||Y_(s,l)||_HS<=C p(l)N.                           (12)

For example X_delta=Q_delta^2 R Omega_k^T P_delta;
all factors outside R Omega_k^T are contractions. The analogous
formula for Y_delta keeps Q_delta on its right.

By (7) and P_delta-P=-D, exact subtraction in (2) gives

    X_delta-X_0=R D^2 Omega_k^T P
                               -R Q_delta^2 Omega_k^T D,
    Y_delta-Y_0=R D^2 Omega_l Q
                               +R Q_delta^2 Omega_l D. (13)

There is no removal of a projection occurrence: (7) groups the two
adjacent Q_delta factors exactly, and each rightmost selector change
is the second term in its respective difference. For the first
terms, transpose R D^2 Omega^T or R D^2 Omega, use symmetry and
commute only D and R; the norm is bounded by
||Omega R D^2||_HS<=||Omega R D||_HS.
For the second terms move only Q_delta^2 past R, then use
||R Omega^T D||_HS or ||R Omega D||_HS. Thus (11) proves

    ||X_delta-X_0||_HS<=C p(k)E_N,
    ||Y_delta-Y_0||_HS<=C p(l)E_N.                     (14)

No coefficient, path or component filter has crossed a projection.

### 3. Retain the projection inside the local generator

L100(7) gives ||G||<=C and ||T V||<=C; the latter uses the
bounded displacement, endpoint averages, H_av and transverse
incidence. Hence

    ||A_0||+||A_delta||<=C,
    A_delta-A_0=-D G.                                 (15)

Estimating D G alone by its Hilbert--Schmidt norm is unnecessary.
In the actual changed trace it is preceded by X_delta. The commuting
spectral identity P_delta D=D P_delta yields exactly

    X_delta D=R Q_delta^2 Omega_k^T D P_delta.

Thus the right-gradient placement in (11) gives

    ||X_delta D||_HS<=C p(k)E_N.                       (16)

This is the ordered applicability argument for the extra P inside
A_loc. It moves D through P_delta only, never through Omega_k,G,T
or a variable multiplier. It uses neither gradient annihilation by
G nor an assumed small projection commutator.

### 4. Telescope the original local trace before choosing masses

For each pair k,l the complete difference is exactly

    Tr(X_0 A_0 Y_0)-Tr(X_delta A_delta Y_delta)
      =Tr((X_0-X_delta) A_0 Y_0)
       +Tr(X_delta D G Y_0)
       +Tr(X_delta A_delta (Y_0-Y_delta)).              (17)

The middle sign follows from A_0-A_delta=D G. For the first and
third terms use |Tr(B C E)|<=||B||_HS ||C|| ||E||_HS
with (12),(14),(15). For the middle term group X_delta D and
use (12),(16),||G||<=C. Every term is therefore bounded by
C p(k)p(l)N E_N. Multiplication by the original a^-1 and summation
with L088's complete actual heat envelope

    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i

prove (4), since a^-1=N/8. This counts both exterior-circulation
terms, both covariance positions, the gh and hh selectors and the
P inside A_loc. The unaltered T V part is retained in both traces.
No external or internal mode cutoff is made.

Only now substitute epsilon=N^-1, delta=N^(-4/3).
Then delta^(3/4)epsilon^(-1/2)=N^(-1/2), so (4) is at most
C_i N^(5/2)sqrt(L_N). Combine with L238(4), including L237's
mass error, to obtain (5). This substitutes schedules into uniform
finite inequalities, not into a fixed-parameter limiting theorem.

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE
assessment for the complete quantitative R_L target. L226's spectral,
collar and gradient-range estimates are known local inputs; the
new applicability check is (13),(16),(17) for this different ordered
product. The finite spectral and Hilbert--Schmidt inequalities are
not new general theorems. No originality beyond the sources checked
is claimed, and no numerical certificate is used. Upstream results
and the remaining bulk/boundary rate are not audited or established
by this proof.

### 5. Separate critical audit of every projection placement

Audit dated 2026-10-19, STEP_ID YM-20261019-339-left-crossed-complete-rate-audit.
Accept (4)--(5) relative to the stated finite spectral and row estimates.
The new applicability checks below, and the separate audits of L237
and L238 in this step, supersede the pending-audit status above.

The imported L226 estimates (6)--(8) explicitly allow unprojected R:
their proof uses component differences and a physical collar, not
QJ=J. Its transverse shell count for D includes masses below N^-2.
For the other order, Cc D=0 leaves precisely the two terms in (9);
R Cc^T is bounded by the relative quadratic-form inequality, without
moving either path multiplier. The F_k terms in (10) use the full
four-dimensional inverse-square trace and remain in both orders.
Thus all three distinct norms in (11) have their asserted bounds.

Since QD=DQ=0, Q_delta^2=Q+D^2 is exact even though Q_delta is
not a projection. Subtracting the two words in (2) directly gives
(13). The first terms are controlled after transposition by
Omega R D^2; the second terms use R Omega D. These are different
placements, both covered by (11). The full X,Y factors remain O(p N).

The middle change is A_0-A_delta=D G. Its trace contribution in
(17) has a plus sign and contains X_delta D. Commuting only the
two spectral factors P_delta,D gives
X_delta D=Q_delta^2 R Omega_k^T D P_delta, so the same
right-gradient norm applies. No derivative gain for D G is assumed.
All three terms of (17) are therefore O(p(k)p(l)N E_N) before
a^-1. The complete heat sum yields N^2 E_N, equal to the bound
in (4). The schedule has delta^(3/4)epsilon^(-1/2)=N^-1/2,
and L238 supplies the other comparison in (5). No projector
occurrence, endpoint row or exterior-circulation term is dropped.

## Mathlib

Full matching ordered left-crossed projection estimate: **not checked**.
Supporting finite relative cochain, spectral calculus, Hilbert--Schmidt
ideal and trace inequalities: **not checked**. Unknown coverage is
not absence. No continuum flow-finiteness or Ward theorem supplies
the isolated trace rate.
