# L256 — Massless second-prefix comparison in the smooth-action trace

## Hypotheses

Keep L175--L177's relative SU(2) box (-4,4)^4, admitted even N,
a=8/N, straight direction-1 lower-rooted forest, stored coordinates,
bare-first expansion, complete compact displacement and actual probes
i=3,6 at tau=1/16. All action faces, covariance sources, normal end
links, constant component modes and exterior heat labels remain.

Use exactly their endpoint sum S, symmetric generator A^gen, signed
transverse differences J_j, exterior columns h_k, action multipliers
m_(j,l) and coefficients c_(i;kl). On transverse interior vertices let
G=Delta_T^(-1). Let P_(s,r)=1 for 0<=r<s, 1<=s<N, 0<=r<N,
and zero otherwise, and M=P P^T. The component-1 extractor E_1 includes
both axial end edges. Set

    Y=M tensor G,       F=Phi Sigma,       Phi=(P tensor I)E_1,
    F^0=(P tensor G)E_1,                 Delta=Sigma^(-1).

Define the finite linear functional at zero left mass by

    U_i^0(T)=-6 sum_(k,l) c_(i;kl) sum_(j=2)^4
                 Tr[Y m_(j,l) J_j T A^gen M_(h_k) S].       (1)

Thus W_i^0=U_i^0(F) is exactly L176's massless-left comparison;
(1) is L177(2) with H=Y, not an infinite-volume inverse or mass limit.
The axial M and P profiles are not shortened, and the action and
generator/probe coefficient levels are not identified.

## Conclusion

For both actual probes and sufficiently large admitted N,

    |W_i^0-U_i^0(F^0)| <= C_i N^(5/2),                     (2)

with C_i independent of N. Each individual j,k,l summand has a bound
C p(k)p(l)N^(5/2) for a fixed polynomial p, permitting the complete
heat sum. Consequently, together with L176(3),

    |V_i-U_i^0(F^0)| <= C_i N^(5/2)sqrt(log(eN)).            (3)

This is a local quantitative specialization of the existing prefix
energy and finite weighted Hilbert--Schmidt inequalities, classified
REPRODUCTION without an originality claim. The separate critical audit
in proof section 4 accepts (2)--(3) relative to the named imported
premises. The ordered static trace in (3) has not been compared
quantitatively with exactly L179's coefficient. No complete branch or
L011 remainder, interacting reflected bound, continuum theory or finite
positive infrared mass follows.

## Proof

### 1. Retain the exact pinned cross-matrix energy

Write D for the full axial gradient from interior vertex values with
both endpoint values zero to all N axial edges. L177(6)--(8), on these
same spaces, give

    Z:=F^0-F=R_D(D^T tensor G)E_1,
    R_D=(D^T D tensor I+I tensor Delta_T)^(-1),
    Z Delta Z^T=R_D(D^T D tensor G^2)<=I tensor G^2.        (4)

These are exact finite identities before any inequality or limit.
The last upper edge is retained in D and Delta. The constant axial
edge mode contributes zero to Z by (4), rather than being removed from
the covariance. The right side bounds a genuine energy square, not a
signed response or forest-remainder covariance.

### 2. A full-spectrum transverse estimate without an inverse supremum

For any positive finite matrix G and any square matrix C on its space,

    ||G^(1/2) C G^(1/2)||_HS^2 <= ||C||^2 Tr G^2.          (5)

This is the elementary weighted HS estimate used after L159(16).
For completeness, diagonalize G with eigenvalues g_r>0. Its left
side is sum_(r,s) g_r g_s |C_rs|^2. Apply
2g_r g_s<=g_r^2+g_s^2. Both sum_s |C_rs|^2 and
sum_r |C_rs|^2 are <=||C||^2, as the diagonal entries of
C C^* and C^* C respectively. The resulting two half-sums give (5).
This argument needs no commutation, symmetry or positivity of C.

L159's complete transverse end-edge energy bound gives

    J_j^T J_j<=4 Delta_T,        ||J_j G^(1/2)||<=2.

Indeed (J_j x)_v=x_(v+e_j)-x_(v-e_j) is the sum of its two adjacent
forward differences, with pinned vertex values zero. Each directional
edge difference occurs at most twice in the squared vertex sum, giving
the factor four, including both end edges. Put C=J_j G^(1/2) in (5).
It follows that

    Tr[G J_j G^2 J_j^T]
      =||G^(1/2) J_j G||_HS^2 <=4 Tr G^2 <= C N^4.         (6)

For the final bound, the exact transverse eigenvalues are
lambda_q=sum_(r=2)^4 4 sin^2(pi q_r/(2N)), 1<=q_r<N.
They obey lambda_q>=4|q|^2/N^2. Shells max q_r=m have at most
3m^2 entries, so the entire spectrum satisfies

    Tr G^2<= (3N^4/16) sum_(m=1)^(N-1) m^(-2)<=C N^4,
    Tr G<= (3N^2/4) sum_(m=1)^(N-1)1<=C N^3.             (7)

These are L156's full transverse shell estimates. No internal cutoff,
bulk replacement or J_j/G commutation is used. In particular (6)
retains both Green weights rather than replacing the left one by
its operator supremum, the source of L177's left-mass loss.

### 3. Apply the bound in the original ordered trace

Fix k,l,j, put h=h_k and m=m_(j,l), and let chi be L175's link
cutoff equal to one on the input support of A^gen. Define

    B_gen=Sigma^(1/2) A^gen Sigma^(1/2),
    X=Sigma^(-1/2) chi M_h S Y^(1/2),
    T_Z=Y^(1/2) m J_j Z Sigma^(-1/2).

Using A^gen chi=A^gen and finite rectangular trace cyclicity gives

    Tr(B_gen X T_Z)=Tr[Y m J_j Z A^gen M_h S].             (8)

This is the same factorization as L177(11); only H has been set to
Y. No factor has crossed a multiplier or covariance. L175(7) gives
||B_gen||<=C N. Its compact-input bound
||chi h_k||_infinity<=C a p(k), bounded endpoint incidence and
||Sigma^(-1/2)||<=C give

    ||X||_HS<=C a p(k) sqrt(Tr Y)<=C p(k)N^(3/2),         (9)

since Tr M=N(N-1)/2<=N^2/2 and (7) gives Tr Y<=C N^5.
This uses small exterior values only on the compact residual input;
there is no extension of h_k across its upper pinned jump.

The smooth action multiplier has physical C^2 norm <=C a^3 p(l).
L159(12)--(13), on the lower-anchored, upper-free axial mixed energy
and full transverse Dirichlet domain, therefore gives

    ||Y^(1/2) m Y^(-1/2)||<=C a^3 p(l).

Its hypothesis concerns the smooth mode extension of Lh_l, including
normal end links; it does not concern a rough prefix. Factor this
bounded multiplier on the left of T_Z. By (4) and positivity of the
energy square,

    ||T_Z||_HS^2
      <=C a^6 p(l)^2 Tr[Y J_j (Z Delta Z^T) J_j^T]
      <=C a^6 p(l)^2 Tr M Tr[G J_j G^2 J_j^T]
      <=C a^6 p(l)^2 N^6<=C p(l)^2.                     (10)

Only the positive energy factors receive the operator comparison;
the signed trace is not positive. Tensor separation occurs after
the multiplier has been bounded in mixed energy, so no variable
coefficient is treated as a tensor factor.

Finally the finite trace inequality, (8)--(10), yields

    |Tr[Y m J_j Z A^gen M_h S]|
      <=||B_gen|| ||X||_HS ||T_Z||_HS
      <=C p(k)p(l)N^(5/2).                              (11)

L156(8) bounds sum_(k,l)|c_(i;kl)|p(k)p(l) uniformly for both actual
probes. Sum (11) over all these labels and j=2,3,4, retaining the
single -6 in (1). Since W_i^0-U_i^0(F^0)=-U_i^0(Z), this proves
(2). L176(3)'s complete comparison with V_i then gives (3). The two
Q subtractions and axial/midpoint errors were accounted for in L175
and enter that imported comparison once; none is silently removed here.

All estimates hold at finite N without a transverse mass, varying
parameters, spatial localization of a covariance source, or a signed
cancellation assumption. No numerical script or heat-value enclosure
is needed. The independently unresolved static-to-continuum comparison
must retain M,P, both coefficient levels, the full heat series and
exactly L179's coefficient; (3) alone supplies none of that comparison.

### 4. Separate critical audit, 2026-10-20

The audit accepts (2) and its conditional assembly (3), with no change
to the bound or proof mechanism. Its scope is the application of L156,
L159, L175, L176 and L177 in (4)--(11), not a recursive verification
of their upstream inputs. The source coverage is the saved
[audit assessment](../drafts/literature/2026-10-20-massless-second-prefix-critical-audit.md).
The following checks establish the relative-premise verdict; no finite
mesh experiment or numerical heat enclosure is used.

**Domains and (4).** The vertex space has (N-1) axial levels and
(N-1)^3 transverse sites. E_1 extracts N axial edges over each
transverse site; D includes both end edges, whereas P has zero last
column. All inverses in (4) exist at finite N: transverse Dirichlet
energy is strictly positive even on the constant axial edge mode.
On a transverse eigenvalue lambda, put R=(L_D+lambda)^(-1).
The exact intertwining D^T(L_E+lambda)=(L_D+lambda)D^T gives

    (R D^T/lambda)(L_E+lambda)(D R/lambda)
       =R L_D/lambda^2.

Its axial eigenvalue is alpha/[(alpha+lambda)lambda^2], between
zero and lambda^(-2). This verifies both the energy identity and
Loewner comparison in (4). D^T annihilates the constant edge vector;
that mode agrees in F and F^0, rather than being deleted from either.
The upper pin and its last gradient row remain in this computation.

**Weighted estimate (5)--(7).** The row and column square bounds used
in (5) hold for arbitrary C, including the nonsymmetric J_j G^(1/2).
The full end-edge energy inequality bounds this C by 2. Substituting
it gives exactly G^(1/2) J_j G inside the HS norm, and hence the
trace G J_j G^2 J_j^T after cyclicity. No J_j/G interchange occurs.
The sine lower bound applies to every q_j=1,...,N-1. Counting shells
by max q_j=m bounds the inverse-square sum by a convergent m^(-2)
series; counting the inverse sum gives N shells. Thus N^4 and N^3
in (7) include the lowest transverse modes and every boundary row.

**Order and (8)--(9).** B_gen is link-to-link, X is vertex-to-link,
and T_Z is link-to-vertex. Multiplying them in their displayed order
and cycling the finite link trace gives

    Tr(B_gen X T_Z)=Tr[A^gen chi M_h S Y m J_j Z].

Using A^gen chi=A^gen and cycling once more gives (8), with the
original action and exterior levels unchanged. L175(7) applies to
the generator alone, including both adjoint orientations. The bound
on chi h is applied before the endpoint map, exactly where the
generator's input support permits it. Tr M=N(N-1)/2 and Tr G=O(N^3)
then give a sqrt(Tr Y)=O(N^(3/2)); all nonlocal outputs of Y^(1/2)
remain in that trace. The cutoff does not restrict covariance sources.

**Multiplier and (10).** The actual m is the real diagonal sample of
Lh_l=Lv_l, with physical C^2 norm C a^3 p(l), by L159(6).
L159(12)--(13) use precisely Y here: M^(-1)=B^T B with a lower
anchor and free upper end, and full transverse Dirichlet differences.
Its product estimate preserves the pinned values of the argument,
and transposition gives the required orientation Y^(1/2)mY^(-1/2).
It needs no smooth extension of h_l or a rough prefix through the
upper pin. Factoring this multiplier leaves the positive energy trace
in (10). Congruence by J_j preserves (4)'s inequality; tracing against
positive Y preserves it again. Only then do the tensor factors split.
The complete count is a^6 times N^2 times N^4=O(1), with polynomial
p(l)^2. Positivity of the signed response is never invoked.

**Heat sum and assembly (11), (2)--(3).** The three norms contribute
N, p(k)N^(3/2), and p(l), respectively. The generator/cutoff bounds
have fixed constants, and physical derivatives of the action mode
only enlarge a fixed polynomial. L156(8)'s bounded heat matrix and
positive physical spectral gap therefore sum this entire envelope
for both probes uniformly in N; allowed constant component indices
are retained. The single -6 is already in U. Linearity gives the
sign W_i^0-U_i^0(F^0)=-U_i^0(Z). Finally L176(3) compares V_i with
this same W_i^0, already incorporating L175's direct term, both Q
subtractions and axial/midpoint errors. One triangle inequality gives
(3), without adding any of those terms again.

The claimed N^(5/2) threshold thus survives the audit. This verifies
a local specialization, not new mathematics beyond the inspected
sources or a complete smooth-action remainder. Static matching with
exactly L179's coefficient, other component rates, quantitative L011
assembly and the interacting/continuum/infrared requirements remain
unresolved. The failed varying-mass and rough-prefix smoothness
shortcuts recorded in ATTEMPTS/030 and ATTEMPTS/045 are not used;
the nonzero coefficient in ATTEMPTS/038 is not set to zero.

## Mathlib

Full matching theorem: **not checked**. Supporting weighted finite
trace inequalities, relative tensor spectra and rectangular resolvent
identities: **not checked**. Unknown availability is not absence.
Reuse the unchanged [source assessment](../drafts/literature/2026-10-20-smooth-action-branch-quantitative-remainder.md).
No new external theorem is imported or reproved. The specialization
is needed because L177's quantitative estimate uses a left mass,
whereas (2) retains the complete left transverse inverse at zero mass.
