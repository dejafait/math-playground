# L263 — Complete coefficient-subtracted residual/action remainder

## Hypotheses

Keep the relative SU(2) cube (-4,4)^4, sufficiently fine admitted even
N, a=8/N, tau=1/16, straight lower-rooted direction-1 forest,
ordinary stored coordinates and bare-first expansion. Use both actual
probes i=3,6 and the complete compact displacement of L155. In particular

    H_i=-kappa_0(f_(i,0),r_1,S_3)

is precisely L155(1), not a selected plaquette class. Full tensors
precede forest restriction. Retain both residual insertion subtractions,
every action/source/end row, the upper pinned jump, allowed constant
modes and complete heat sums.

Import L159(3)'s finite partition with L157(6)'s combined error,
L161(3)'s six complete signed traces, and the complete bounds stated
in L161(4), L162(2), L164(1), L255(2), L259(5), L260(1), L261(1)
and L262(1). These imports retain all upstream analytic and pending-audit
qualifications. K_(i,T) is exactly L255's L173(8) coefficient;
K_(i,Vmix) is exactly L259's L179(7) coefficient; K_(i,R) has the
normalization used in L172. L179(8) fixes their complete combination.
No numerical coefficient/sign premise or L220 cancellation is assumed.

## Conclusion

For each actual probe there are constants C_i and N_0, independent of
N, such that every admitted N>=N_0 satisfies

    |H_i-a^(-3)[K_(i,T)+K_(i,Vmix)-6K_(i,R)]|
                       <= C_i N^(5/2)log(eN)
                       <= C_i N^(5/2)log(eN)^2.          (1)

Thus the approved complete residual/action remainder budget holds,
conditionally on the stated component inputs. Equivalently the error
after multiplication by a^3 is O_i(N^(-1/2)log(eN)). This is a finite
assembly, classified REPRODUCTION, without a claim of originality.
The separate critical audit below accepts this finite assembly relative
to its stated imports. It supplies one block, not a complete quantitative
L011 response bound or interacting estimate.
Continuum axioms, nonzero physical states and finite positive infrared
mass remain unresolved. STATUS remains IN_PROGRESS.

## Proof

Write ell=log(eN)>=1. Choose N_0 to be the maximum of the finitely
many component mesh thresholds, for both probes. The hypotheses of all
inputs agree on the box, forest, normalization, fixed flow time and
bare-first order, so their complete bounds hold simultaneously.

Let J_(i,j), j=1,...,6, denote, in order, the six already signed
complete heat/color sums on the right of L161(3). L159(3) gives the
exact finite decomposition with a bounded remainder e_i:

    H_i=T_i+V_i+sum_(j=1)^6 J_(i,j)+e_i,
    |e_i|<=C_i N.                                      (2)

By L157(6), e_i already includes L156's O(1) two-gradient sector.
It is not added separately. No intermediate estimate removed in a
complete component statement is added again.

L172 proof section 3 identifies the trace coefficients in this exact
order. The matching complete quantitative statements give

| j | Cubic coefficient c_j K_(i,R) | Absolute coefficient-subtracted error bound | Input |
| --- | --- | --- | --- |
| 1 | 0 | C_i N^2 ell | L164(1) |
| 2 | -3 K_(i,R) | C_i N^2 ell | L261(1) |
| 3 | -(9/2) K_(i,R) | C_i N^2 ell | L262(1) |
| 4 | (3/2) K_(i,R) | C_i N^2 | L260(1) |
| 5 | 0 | C_i N | L161(4) |
| 6 | 0 | C_i N^(5/2) | L162(2) |

Here the first four trace factors -36,-12,-6,-1 and the last two
factors -6,-3 are already included. The table does not multiply them
again. Since 0-3-9/2+3/2+0+0=-6, subtraction before the triangle
inequality gives

    |sum_j J_(i,j)+6a^(-3)K_(i,R)|
        <= C_i[N^2 ell+N^2+N+N^(5/2)].                 (3)

Use the two complete branch bounds, without their intermediate errors:

    |T_i-a^(-3)K_(i,T)|<=C_i N^(5/2)ell,               (4)
    |V_i-a^(-3)K_(i,Vmix)|<=C_i N^(5/2)sqrt(ell).      (5)

These are exactly L255(2) and L259(5). In particular Vmix is not
L120's different displacement-placement coefficient. Equations (2)--(5)
bound the left side of (1) by

    C_i[N^(5/2)ell+N^(5/2)sqrt(ell)
                          +N^2 ell+N^2+N+N^(5/2)].    (6)

For N>=1 and ell>=1 every summand is at most N^(5/2)ell.
Absorb the finite number of constants into C_i to obtain (1).
Multiplication by a^3=512/N^3 gives the normalized error stated above.
All sums used in the component inputs are already complete; no limit
exchange or additional heat truncation occurs in this finite assembly.

The coefficient is exactly L179(8)'s combination. There is no outside
factor 3, no readdition of L175--L258's removed branch terms, and no
readdition of L165--L167's errors already included in L260--L262.
The argument neither discards this generally nonzero cubic coefficient
nor invokes complete-response cancellation. It audits no upstream
kernel estimate and does not resolve the failures preserved in
ATTEMPTS/037--038 by assuming their obstructed shortcuts.

### Separate critical audit, 2026-10-23

**Verdict: accepted relative to the stated component premises.** The
unchanged assessment
`drafts/literature/2026-10-23-residual-action-assembly-critical-audit.md`
authorizes this finite audit. It does not authorize a recursive audit
or repair of the imported kernel estimates. No correction to (1)--(6)
or change to the mathematical inputs was needed.

**Original response and partition.** L155(1) defines H with the
single-action minus sign. L155(5)'s +3 already contains that sign and
its color/action normalizations; L156 proof section 1 explicitly
identifies the same contraction as -36 in the combined-color Taylor
tensor convention. Thus these are two conventions for the same
response, not two outside factors to multiply. L157(3)--(5) splits
the mixed sector by expanding Q_A=A B_h-B_(A h). Its retained term
is negative and retains Q_L=L B_ell-B_(L ell). Expanding this Q_L
therefore gives the negative action-Hessian branch and positive
smooth-action branch in L158(1). Its exact ordered collapse gives
L159(1)'s V, without replacing E by a positive covariance. L157(6)
then includes the two-gradient O(1) term in its O(N) remainder.
Consequently L159(3) is exactly (2), with no additional sector.
These normalization checks concern the premises already imported
through L157/L159, not newly assumed analytic identities.

**Six signed words.** The original L161(3) contains, in order,
Tr(M Sigma N Sigma), Tr(Q_A F N Sigma), Tr(Q_L F M Sigma),
Tr(Q_A F Q_L F), Tr(D^T B_(A h) F N F^T), and
Tr(D^T B_(L ell) F M F^T), with their hats and full heat/color sums.
Their factors are respectively -36,-12,-6,-1,-6,-3. L161's proof
section 1 obtains these from the nine terms of E=Sigma-D F-F^T D^T:
the two distinct single-gradient placements have multiplicity two,
the crossed double-gradient word has multiplicity two, and the two
same-vertex words occur once. Its identities M D=-Q_A/6 and
N D=-Q_L/12 give the displayed factors after multiplication by -36.
This verifies the trace correspondence without transposing away a
placement or treating F as a positive prefix covariance.

The first complete word is L164's W. The second, third and fourth
are exactly L166(1)'s Y, L165(1)'s Z and L167(1)'s X, the original
objects explicitly specified in L261, L262 and L260. The fifth is
L161's J_R2 and the sixth is L162(1)'s J_S2. Their complete bounds
are precisely the six rows of the table above. In particular the
sixth uses L162's improved N^(5/2), not L161's earlier N^3 bound.
L172 proof section 3 matches their coefficients in this same order;
L260--L262 subtract those coefficients from the complete original
words. The rational sum is -3-9/2+3/2=-6. L172's numerical intervals
are unnecessary and have not been used.

**Complete branch and error coverage.** L255(1)--(2) uses the
one-color -6 branch of L173(1), which identifies itself with L158's
T, and subtracts exactly L173(8)'s K_T. Its -6 already includes the
color contraction. L259(5) is the complete V remainder against
exactly L179(7)'s K_Vmix. L259 proof section 5 explicitly obtains
it by adding the already combined V comparison once; its Q forms
are already included through the earlier complete branch comparison.
It is not merely the first, static N^2 statement in L259(4).
Similarly L260--L262 explicitly include their removed upper-exterior
and smooth-column contributions. None is an extra summand in (6).
The two N-sized errors, e_i and the fifth E,E trace, are distinct
partition terms and both are retained; their constants can be added.

Every quoted conclusion has mesh-independent constants for the same
sufficiently fine admitted even N, a=8/N, tau=1/16, relative box,
lower-rooted forest and actual probes. Stored coordinates and the
bare-first order agree. All full tensors, both subtractions, source
and end rows, upper jump, constant modes and complete heat sums stay
in those imported conclusions. A maximum over their finitely many
mesh thresholds and the two probes therefore gives a common N_0.

**Subtraction and threshold.** Define the eight centered errors by
subtracting a^(-3)K_T, a^(-3)K_Vmix and the six table coefficients
from their respective finite terms. Their exact sum plus e_i is
H_i-a^(-3)(K_T+K_Vmix-6K_R). Only after this identity is the triangle
inequality applied. For N>=1, ell=log(eN)>=1 gives sqrt(ell)<=ell
and N^2,N<=N^(5/2). Each error is consequently bounded by its own
constant times N^(5/2)ell. Adding those constants proves (1), and
ell<=ell^2 proves the requested budget. Multiplication by 512/N^3
gives the stated N^(-1/2)ell normalized error. This is a uniform
finite inequality; it uses no mesh-dependent parameter in a qualitative
limit and no extra factor 3. L179(8) independently fixes the same
coefficient name and normalization.

This audit validates one existing local assembly, not a new rate or
progress beyond the checked sources. All upstream analytic and
pending-audit premises remain imports. It proves neither the complete
L011 remainder nor L220's cancellation, coefficient signs, interacting
reflection control, continuum axioms or a finite positive mass.
No mathematical script is needed for these finite identities and
inequalities. The DAG's direct assembly inputs are unchanged.

## Mathlib

Full matching coverage for this forest/probe assembly is not checked.
Only finite-sum triangle inequalities and elementary positive-power
comparisons are newly used here; no theorem-name or absence claim is
made for Mathlib. The mathematical component results are imported by
their precise canonical statements above, not reproved.
