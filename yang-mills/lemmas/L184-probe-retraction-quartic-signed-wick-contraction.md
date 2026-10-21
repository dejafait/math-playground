# L184 — Complete signed Wick contraction of the probe-retraction quartic

## Hypotheses

Use precisely L182–L183's fixed-mesh SU(2) hypotheses: relative box
(-4,4)^4, admitted even N, a=8/N, straight direction-1 lower-rooted
forest, complete displacement, both actual L010 probes i=3,6 at
tau=1/16, and bare expansion before refinement. All matrices use
ordinary full variable-link coordinates, including forest rows and
normal end edges. Fixed boundary links are omitted and vertex
potentials vanish on every physical face. There is no periodic or
bulk replacement. All link sums below are unrestricted finite sums.

In L183's notation S is the one-color co-closed Gaussian covariance,
P is the co-closed projection, A=PAP is the full symmetric residual
including both insertion subtractions, B=B_i=PBP is the complete
final-time quadratic probe, and

\[
 T=2SA,\qquad M=TS=2SAS,\qquad
 V=q\Phi,\qquad F=D\Phi,\qquad H=1-F/2.                 \tag{1}
\]

Here q adds the two endpoint values. In particular V is an endpoint
map composed with the actual pinned prefix; it is not the generator
or a flowed matrix. M is symmetric but need not be positive. Neither
T nor M is commuted with B or a prefix. For three independent color
copies z with covariance S, retain

\[
 b=\tfrac12[z,Vz]-\tfrac14[Fz,Vz],\qquad
 J=2\langle Bz,b\rangle,\qquad W=P\,\mathrm db(z)[Tz].   \tag{2}
\]

The bracket is minus the color cross product. These are exactly L183's
polynomials, with the moving prefix Phi(Tz) and composed prefix Phi W
retained. The letter e used as a link index below is distinct from a
color index.

## Conclusion

Define skew link matrices Gamma_e and an alternating scalar tensor h by

\[
 \begin{split}
 (\Gamma_e)_{rs}
 &=-\tfrac12(\delta_{er}V_{es}-\delta_{es}V_{er})
       +\tfrac14(F_{er}V_{es}-F_{es}V_{er})\\
 &=-\tfrac12(H_{er}V_{es}-H_{es}V_{er}),\\
 h_{abc}&=2\sum_e\{B_{ea}(\Gamma_e)_{bc}
                 +B_{eb}(\Gamma_e)_{ca}
                 +B_{ec}(\Gamma_e)_{ab}\}.
 \end{split}                                                \tag{3}
\]

Then the entire quartic correction Q_(i,N)=E_S[dJ(z)[W(z)]] has the
exact signed contraction

\[
 \boxed{Q_{i,N}=6\sum_{a,b,c,g,u,v}
 h_{abc}P_{ag}(\Gamma_g)_{uv}M_{ub}S_{vc}.}                 \tag{4}
\]

There is no omitted internal pairing, extra color factor, covariance
replacement, or separate differentiation of W. In particular (4)
includes the Phi W term in L183(15). Expanding only h splits (4) into
three ordered probe-leg placements Q_1+Q_2+Q_3:

\[
 \begin{split}
 Q_1&=12\sum_{e,g,b,c,u,v}B_{eg}(\Gamma_e)_{bc}
                  (\Gamma_g)_{uv}M_{ub}S_{vc},\\
 Q_2&=12\sum_{e,g,a,c,u,v}(MB)_{ue}(\Gamma_e)_{ca}
                  P_{ag}(\Gamma_g)_{uv}S_{vc},\\
 Q_3&=12\sum_{e,g,a,b,u,v}(SB)_{ve}(\Gamma_e)_{ab}
                  P_{ag}(\Gamma_g)_{uv}M_{ub}.
 \end{split}                                                \tag{5}
\]

Only Q_2 has the tilted covariance M directly adjacent to B in this
representation. Q_1 and Q_3 retain M on rough slots. This observation
is about the displayed exact orders, not a proof that these placements
are nonzero for either actual probe or that later joint cancellations
are impossible. No smooth-input bound for their rough columns is
imported.

For row maps X,Y chosen from H,V put C_XY=XSY^T and K_XY=XMY^T.
The first placement has the smaller signed covariance-minor formula

\[
 \boxed{Q_1=3\sum_{e,g}B_{eg}\bigl\{
 (K_{HH})_{eg}(C_{VV})_{eg}
 -(K_{HV})_{eg}(C_{VH})_{eg}
 -(K_{VH})_{eg}(C_{HV})_{eg}
 +(K_{VV})_{eg}(C_{HH})_{eg}\bigr\}.}                      \tag{6}
\]

This is a local exact contraction input for the approved joint-group
scale question, obtained by specializing Isserlis' theorem to its
actual tensors. It supplies no O(N^3) bound, finite a^3-scaled limit,
actual-probe value, vanishing or progress beyond the checked source
methods. Its signs must remain before estimates. L183's sextic partner
and the co-closed zero-time flow contribution remain independent gaps,
as do f_(i,2),r_0 compensation, finer scales, finite matching,
reflected error <=c_box/2, continuum axioms and infrared finite mass.

## Proof

### 1. The actual prefix tensor and all three differentiated probe slots

With epsilon_123=1 and the minus-cross-product convention, expand
(2) edge by edge and antisymmetrize its two input link indices. This
is exactly

\[
 b_e^k=\tfrac12\sum_{r,s,d,f}(\Gamma_e)_{rs}
                        \epsilon_{kdf}z_r^d z_s^f.        \tag{7}
\]

For example the first bracket in b has unsymmetrized coefficient
-\delta_er V_es/2; its skew difference is the first term of Gamma.
The second bracket has coefficient F_er V_es/4 and gives the second
term. The factor 1/2 in (7) compensates the two skew indices.
Substituting (7) into J=2<Bz,b> and collecting the three cyclic link
placements gives

\[
 J=\tfrac16\sum_{a,b,c,k,d,f}
                       h_{abc}\epsilon_{kdf}z_a^k z_b^d z_c^f.
                                                               \tag{8}
\]

Indeed each of the three cyclic terms in h contributes the same
scalar after cyclically relabeling link and color indices. The 2/6
factor times those three terms is one, which is the coefficient
obtained directly from 2<Bz,b>. Skewness of Gamma also makes h fully
alternating. Thus (8) is the complete cubic, rather than a chosen
representative on the co-closed space.

Differentiating (7) in direction Tz differentiates both of its input
slots. Write W_a^k=(1/2)sum_(r,s,d,f)w_(a;rs)epsilon_kdf z_r^d z_s^f.
Then

\[
 w_{a;rs}=\sum_{g,u}P_{ag}\{
                (\Gamma_g)_{us}T_{ur}
                  +(\Gamma_g)_{ru}T_{us}\}.              \tag{9}
\]

The second term of (9) is indispensable. V and F both contain Phi;
(9) therefore retains their variations, including V(Tz)=q Phi(Tz).
In (8), differentiating each of the three slots instead gives

\[
 {\partial J\over\partial z_a^k}
     =\tfrac12\sum_{b,c,d,f}h_{abc}\epsilon_{kdf}z_b^d z_c^f.
                                                               \tag{10}
\]

This is a full-space polynomial derivative. Since W lies in im P,
its contraction with W agrees with differentiation on that subspace.
In particular the last two placements in (10) differentiate b within
J, so they include Phi W without needing to expand it separately.

### 2. All quartic Wick pairings and their exact factors

Apply Isserlis' theorem (the Gaussian fourth-moment formula) to the
product of (9) and (10). It is valid also for positive semidefinite S:
write z=S^(1/2)xi with standard independent Gaussian xi and substitute
into the usual finite-dimensional formula. Color covariance is
E[z_r^d z_s^f]=delta_df S_rs.

The pairing internal to the two inputs of (10) sets its two colors
equal, so its alternating epsilon vanishes. The remaining two inputs
would pair internally in W as well. Thus the entire internal/internal
pairing is zero. The other two pairings run across the two quadratic
factors. For the first crossing the color sum is
sum_(k,d,f)epsilon_kdf^2=6. For the second it is -6, but swapping the
skew input indices r,s in w changes that minus back to a plus. Their
net contraction is therefore

\[
 Q_{i,N}=3\sum_{a,b,c,r,s}h_{abc}w_{a;rs}S_{br}S_{cs}.     \tag{11}
\]

The coefficient is (1/2)(1/2) times (6+6)=3. Substituting (9), its
two terms are equal after exchanging b,c and r,s and using the
skewness of h and Gamma. Finally sum_r T_ur S_br=(TS)_ub=M_ub,
using only the symmetry of S. This proves (4) with coefficient 6.
The symmetry M=2SAS follows from A=A^T; positivity of M is not used.

### 3. Preserve the three probe-leg orders and the covariance minors

Expand (3)'s three terms for h in (4). The first sums a using
sum_a B_ea P_ag=(BP)_eg=B_eg. The second sums b using
sum_b B_eb M_ub=(MB)_ue. The third sums c using
sum_c B_ec S_vc=(SB)_ve. These yield exactly (5). Only these displayed
index sums are performed; no multiplier or prefix is moved through
S, A or B.

For Q_1 insert the second formula for Gamma in (3). Its two factors
of -1/2 give +1/4. Expanding their two row wedges gives, respectively,
K_HH C_VV, -K_HV C_VH, -K_VH C_HV, +K_VV C_HH at indices e,g.
The coefficient 12/4=3 proves (6). Each entry uses the same original
S and M and the full pinned maps. This argument holds at all physical
end rows without an integration by parts or an extension of Phi
across a face.

These finite identities are sufficient to verify the signed contraction,
but do not estimate any of its unrestricted sums uniformly in N.
Final-time smoothing of B does not by itself justify assigning smooth
consistency to the M input in Q_1 or Q_3. Even bounds on the three
placements would leave a convergence proof and the other parts of the
joint response to establish. The earlier O(N^5) energy bound in L183
is neither replaced by a proved O(N^3) bound here nor used as a lower
bound.

### 4. Exact algebra check and its limited scope

Run, from the active notebook,

    python3 scripts/combined-ward-response/check_probe_quartic_wick.py

The full certificate is
`scripts/combined-ward-response/probe-quartic-wick-certificate.json`.
The script uses rational sparse polynomials, constructs b from both
its original two brackets and Gamma, differentiates J and W directly,
and applies all three Gaussian fourth-moment pairings. It separately
checks the cubic coefficients h, (4), all three placements (5), and
(6). A full-space example and a singular rank-three co-closed example
pass exactly; supported covariance positivity is certified by positive
rational LDL pivots. Their direct quartic values are -55728 and -9126,
matching the respective placement sums (34146,-8514,-81360) and
(-5712,-2532,-882). All selected check records were inspected in full.

These maps are synthetic and are not actual box or L010 probe data.
The check detects factor, order and sign mistakes in the algebra;
the general identities are proved in sections 1–3. Its nonzero values
are not evidence for an actual-probe sign, exponent or noncancellation.
The required actual-probe bound is O(N^3); no such bound or limit is
reported by this certificate.

## Mathlib

Full matching theorem for this actual probe contraction or its cutoff
limit: **not checked**. Supporting Gaussian, skew-tensor and relative
cochain coverage: **not checked**; unknown availability is not absence.
The standard input is Isserlis' theorem, specifically its three-pair
fourth-moment formula, with the singular covariance and color cases
justified above. L182–L183's exact probe and residual retractions are
reused. This specialization is needed to expose the actual two moving
prefixes and the three probe-leg placements; it does not reprove flow
renormalizability or infer a selected bare limit from a full-correlation
source. The unchanged approved assessment
[records the source comparison](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md).
