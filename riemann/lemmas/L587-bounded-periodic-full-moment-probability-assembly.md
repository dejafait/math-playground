# Lemma 587: bounded periodic probability assembly of all paired moments

## Hypotheses

Use L473's coordinate order a=(r,j), r=0,1 and j=0,1,2, its
reference second and fourth moments S_ab(H), F_m(H), and precisely
its 147 tolerances (2), including the four tighter odd second bounds.
Put ell=log H. All derivatives are ordinary derivatives, with ell
fixed when defining the scaled height coordinates.

For a real smooth periodic path h of period P>0 write

    J_h(s)=(h(s),h'(s),h''(s),h(s+1),h'(s+1),h''(s+1)),
    C(h)=P^(-1) integral_0^P J_h(s)J_h(s)^T ds,
    T_m(h)=P^(-1) integral_0^P J_h(s)^m ds, |m|=4.

K and q_m are exactly L473 (6) and (9). Fix the finite collection
of unit-jet smooth paths h_i and nonnegative weights a_i supplied by
L585 (1), and set

    W_4=sum_i a_i<infinity,
    R=sum_i a_i C(h_i),
    sum_i a_i T_m(h_i)=q_m,
    sup_s |J_(h_i)(s)|<=1.                                  (1)

Use L586's finite-cone interiority and absorption conclusions for
this fixed R. In particular both K and K-R/L have finite periodic
representations for some fixed real L>=1. L586's separate critical
application audit is recorded in its Section 6; this assembly's audit
is in Section 5 below. The identification
with Hardy reference moments retains L473's imported arithmetic
qualifications, particularly Bui--Hall Proposition 3's unaudited proof.
No RH, simplicity, zero-free-region or clipped-mass premise is used.

## Conclusion

There is one H_0>1 such that for every real H>=H_0 a finite positive
mixture of smooth periodic occupation probability laws, allowing
different periods, gives a law nu_H on the six coordinates with

    E_(nu_H) VV^T=ell K,
    E_(nu_H) V^m=ell^4 q_m+O_m(ell^2), |m|=4,               (2)
    |J_g(s)|<=ell^2 at every phase of every selected path g.

The law satisfies all 147 tolerances in L473 (2), with constants
uniform on the same eventual ray. In particular all four tight odd
second entries are exactly zero. A fixed finite dictionary of base
paths suffices; only their whole-path amplitudes and mixture weights
vary with H. Total mixture mass is one and every weight is nonnegative.

The result is non-effective: no numerical dictionary, constants or
height onset are asserted. It establishes bounded periodic moment
feasibility, with no positive lower bound for the clipped statistic,
no realization of L473's particular probability law, and no transfer
to actual-Xi signs. It is the approved standard finite-mixture
specialization, not a claim of a new general moment theorem or RH.

## Proof

### 1. A fixed finite dictionary with uniformly bounded weight

By L586 choose a fixed L>=1 such that L K-R is in its finite
restricted-frequency cone. Dividing a finite representation by L
places D=K-R/L in the same cone. L586 also places K in that cone.
Use its exact single-frequency smooth periodic generators (constant
path at frequency zero), normalizing the whole paths as in its
hypotheses. This gives finite lists f_j^+, f_j^- and nonnegative
weights k_j,d_j with

    K=sum_j k_j C(f_j^+),   D=sum_j d_j C(f_j^-),
    sup_s |J_(f_j^+)(s)|<=1,
    sup_s |J_(f_j^-)(s)|<=1.                               (3)

These choices are made once, independently of ell. Normalization is
legitimate: replacing f by f/M, M=max(1,sup |J_f|), multiplies
its covariance by M^(-2), so multiplying its weight by M^2
preserves the represented matrix. Smoothness and periodicity are
unchanged and every M is finite. Zero-weight paths may be omitted.

Set W_+=sum_j k_j, W_-=sum_j d_j and W_2=max(W_+,W_-).
All are finite; K is nonzero, so W_2>0. For every real ell>=L,
put t=L/ell in [0,1]. Combine the two fixed lists, giving f_j^+
weight (1-t)k_j and f_j^- weight t d_j. Call the combined list
f_j with weights b_j(ell). Then

    b_j(ell)>=0,
    sum_j b_j(ell) C(f_j)
      =(1-t)K+t(K-R/L)=K-R/ell,
    sum_j b_j(ell)=(1-t)W_++t W_-<=W_2.                    (4)

This is finite convex interpolation, not an inference of a uniform
mass bound from pointwise cone membership. It supplies the required
common dictionary and fourth-cost bound: for every |m|=4,

    |T_m(f_j)|<=average |J_(f_j)|^4<=1,
    |sum_j b_j(ell) T_m(f_j)|<=W_2.                        (5)

The general finite-representation and interior theorems are imported
in L586: Bayer--Teichmann, *The proof of Tchakaloff's theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
([v2, Corollary 2 and pushforward proof, pp.3--4](https://arxiv.org/pdf/math/0502473v2#page=3));
Blekherman--Fialkow, *The core variety and representing measures in
the truncated moment problem*, [v1, Proposition 2.1 and Corollary 2.2,
pp.5--6](https://arxiv.org/pdf/1804.04276v1#page=6).
Their specializations and hypotheses are proved in L586; no new
general representation theorem is needed or reproved here.

### 2. Probability weights, whole-path amplitudes and support

Set the fixed constant B=max(1,4W_2). For each ell>=L include
the following occupation components. An occupation law means that
the phase is uniform on one full period of the indicated path.

* Rare component i: path ell^2 h_i, with mass a_i ell^(-4).
* Second component j: path sqrt(B ell) f_j, with mass b_j(ell)/B.

Their total masses p_4,p_2 satisfy

    p_4=W_4 ell^(-4),
    0<=p_2=B^(-1)sum_j b_j(ell)<=W_2/B<=1/4.               (6)

Require ell^4>=4W_4, so p_4<=1/4. Add the zero path, of any
positive period, with mass 1-p_4-p_2>=1/2. All component masses
are nonnegative and their sum is exactly one. The phases can be
chosen conditionally after the finite component choice, even when
the periods differ. The resulting process is stationary in the
scaled variable, since translation preserves each uniform phase law.
No common period or time dilation has been used.

The rare paths satisfy sup |J_(ell^2 h_i)|<=ell^2. The second
paths satisfy sup |J_(sqrt(B ell) f_j)|<=sqrt(B ell), which is
at most ell^2 when ell^3>=B. The zero path satisfies the same bound.
These inequalities hold at every phase, including phases of measure
zero. They imply compact support and all required integrability.

Scaling whole paths preserves all ordinary derivative and fixed-lag
identities, since J_(a h)=a J_h for a constant amplitude a. More
explicitly, a path g(s) yields a height path F(t)=g(ell t), and

    F^(j)(t+r/ell)/ell^j=g^(j)(ell t+r).

Thus these six-coordinate occupation laws have exactly the prescribed
scaled ordinary-jet interpretation. The period of F changes with
ell, which is allowed; the lag in g remains exactly one.

### 3. All second and fourth entries

Mass times the squared rare amplitude is a_i, so its full second
matrix is R by (1). For the second components, mass times squared
amplitude is ell b_j(ell), giving by (4)

    E_(nu_H) VV^T
      =R+ell sum_j b_j(ell)C(f_j)=ell K.                   (7)

This is equality of matrices, hence includes all 21 unordered entries.
For the four same-height odd pairs, K_ab=0 by L473 (7); thus the
law's moments vanish exactly. Their absolute values satisfy both
specified H^(-2/3) bounds with zero constant. Their difference from
the corresponding reference second moments also has the stated tight
bound, by L473's direct odd estimates. The other 17 reference entries
satisfy S_ab(H)=ell K_ab+O(1) by L473 (6). No generic O(1) error
has been substituted for any of the four tight requirements.

For any of the 126 monomials |m|=4, mass times the fourth rare
amplitude is a_i ell^4. Its full contribution is exactly ell^4 q_m.
The second components contribute

    E_(nu_H) V^m-ell^4 q_m
      =B ell^2 sum_j b_j(ell) T_m(f_j),
    |E_(nu_H) V^m-ell^4 q_m|<=B W_2 ell^2,                 (8)

by (5). This absolute estimate covers signed mixed monomials and
vanishing q_m, without assuming odd cross entries vanish. L473 (9)
gives F_m(H)=ell^4 q_m+O_m(ell^3), so for ell>=1 equation (8)
proves E V^m=F_m(H)+O_m(ell^3) for every m. It does not claim
O(ell^2) error relative to F_m(H), whose lower coefficients have
not been supplied. The zero component changes none of these moments.

### 4. One eventual real-height ray and scope

Let H_src>1 be one eventual onset for L473's finite collection of
reference estimates. Such a common onset exists by maximizing the
finitely many source constants/onsets. Define

    ell_* = max(1,L,(4W_4)^(1/4),B^(1/3)),
    H_0=max(H_src,exp(ell_*)).

All constants, base paths and choices in (1)--(5) are fixed before
H varies. For every real H>=H_0, ell=log H satisfies every mass,
support and error requirement above. There is no subsequence or
height-by-height onset, and no compactness limit or infinite mixture.

This closes the approved moment-feasibility interface using only the
stated local inputs. The packet-dictionary stops and exact corrected-law
stationarity obstruction retain their original scopes: this law uses
different paths and only the permitted fourth tolerances. No sign of
E(x_0 z_0-y_0^2)_+ beyond nonnegativity has been computed; an order-ell
lower bound is a separate question. Nothing here identifies this law
with actual Hardy trajectories or controls actual-Xi all-degree signs.
The separate critical audits in L586 Section 6 and Section 5 below
pass; the arithmetic source proofs remain imported, as stated above.

### 5. Separate critical application audit, 31 October 2026

The invocation-start SPECIALIZE coverage is
`drafts/literature/2026-10-31-l586-l587-critical-application-audit.md`.
This joint audit checks the complete assembly from L473 (1)--(2),
(6)--(9), audited L585 (1), and L586, whose application was checked
in the same step. It passes without changing the mathematical
statement or construction. The arithmetic-source proofs remain
imported; no general representation theorem is reproved here.

**Fixed choices before varying height.** L586 supplies an L>=1
with LK-R in C_I and separately K in C_I. Scaling the former
finite representation by 1/L gives D=K-R/L, so both endpoint
representations in (3) are genuine finite representations. Each
whole-path normalization uses a finite constant M, changes C by
M^(-2), and changes its nonnegative coefficient by M^2. These
constants depend only on the chosen paths. Zero weights or an empty
D representation cause no problem. K's value variance is 1, so
its representation cannot be empty and W_2>0. All choices and
W_2 are fixed independently of ell.

For ell>=L the coefficients 1-L/ell and L/ell are nonnegative
and sum to one. The identity (4) is exact, including ell=L, and
the sum of coefficients is bounded by the fixed W_2. This step
is why the proof needs only two dictionaries: pointwise finite
representations alone would not supply the required uniform bound.
Every fourth monomial satisfies |J^m|<=|J|^4<=1 on these base
paths, regardless of the sign of that monomial. Thus the absolute
fourth bound (5) holds for all 126 indices with the same constant.

**Mass, support, and path consistency.** B=max(1,4W_2) is a
positive fixed number. The second-component mass is at most 1/4,
and ell^4>=4W_4 makes the rare mass at most 1/4. The remaining
mass of at least 1/2 is assigned to a genuine zero path. Each
component is a probability law after its own normalized period
average, so these masses sum to exactly one even with different
periods. A finite mixture of their uniform phase laws is stationary
under every scaled translation: conditional translation preserves
each component's normalized Haar measure. No assertion of a common
period, ergodicity or realization by actual Hardy paths follows.

The rare amplitude ell^2 and the second amplitude sqrt(B ell)
are constants along an entire selected path. Consequently the six
coordinates remain ordinary derivatives at lag one. Their norms
are respectively at most ell^2 and sqrt(B ell) at every phase,
and the latter is at most ell^2 for ell^3>=B. For F(t)=g(ell t),
the chain rule gives F^(j)(t+r/ell)/ell^j=g^(j)(ell t+r)
with ell held fixed. The support bound therefore concerns the
prescribed scaled ordinary jets, not a separately scaled or patched
collection of six coordinates. All moment integrations are finite.

**Every second entry, including the four tight requirements.**
For each rare component mass times amplitude squared is a_i,
whereas for each second component it is ell b_j(ell). These
identities give R+ell(K-R/ell)=ell K entry by entry. There are
6*7/2=21 unordered entries. At each of r=0,1, L473 (7) has
K_((r,0),(r,1))=K_((r,1),(r,2))=0, so the four exceptional
law moments are identically zero. Their bounds are respectively
O(H^(-2/3)ell^(-1)) and O(H^(-2/3)ell^(-3)), not O(1).
If compared to S_ab rather than zero, L473's direct odd estimates
give these same tight error scales. Each of the other 17 entries
differs from S_ab by O(1) using L473 (6). This exhausts the
second constraints without assuming independence between the lags.

**Every fourth entry and the correct error scale.** There are
binomial(9,4)=126 degree-four monomials in six coordinates. For
each of them mass times fourth amplitude is a_i ell^4 in the
rare component and B ell^2 b_j(ell) in the second component.
Consequently (1) reproduces every leading coefficient q_m exactly,
and (5) bounds the remaining contribution by B W_2 ell^2.
Signed monomials, zero leading coefficients and all distributions
of the four factors between the two lags are included. With
|F_m(H)-ell^4 q_m|<=C_m ell^3 from L473 (9), the actual
reference error is bounded for ell>=1 by

    |E V^m-F_m(H)| <= (B W_2+C_m) ell^3.

This is O_m(ell^3) relative to F_m, whereas the O_m(ell^2)
claim is relative only to ell^4 q_m. No lower reference coefficient
is identified or absorbed into the tighter claim. The zero path
contributes zero to all these positive-degree moments.

**One common real-H onset and verdict.** The estimates imported
from L473 are finitely many eventual estimates, so taking the
maximum of their onsets is legitimate. Every additional inequality
is satisfied by ell>=max(1,L,(4W_4)^(1/4),B^(1/3)). The fixed
H_0 in Section 4 therefore works simultaneously for all 147
constraints and every-phase support for every real H>=H_0.
All dictionaries, masses' fixed constants and error constants were
chosen before this universal quantifier. No asymptotic subsequence,
uniformity across varying dictionaries or exchange of infinite
mixtures is assumed.

The audit validates a bounded derivative-consistent probability law
for the stated tolerance problem, a reproduction/specialization of
the imported tools using the local carrier. It does not compute a
positive clipped lower bound or identify the law with L473's exact
corrected law. L578/L579's packet-family stops, L581's exact-law
stationarity obstruction and L584's exceptional-budget obstruction
therefore retain their scopes. L473's arithmetic qualifications,
non-effective constants and actual-Xi transfer remain unchanged.
No new direct mathematical input or DAG edge is required.

## Mathlib

Coverage of this full bounded periodic 147-moment probability assembly
has not been checked. Relevant finite-mixture integration, homogeneity,
finite convex combinations and ordinary derivative rules are standard
supporting facts; no full matching Mathlib theorem is claimed. The
moment-cone and Fourier inputs remain as documented in L586. Unknown
coverage is not evidence of absence. No numerical script or Lean
certificate is used to establish (1)--(8).
