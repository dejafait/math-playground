# Joint energy finite-compression comparison

One bounded proof attempt under the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The main gap is interacting ultraviolet control. The intermediate test
is an O(N^3) comparison of L115(2) with its full-grid trace, retaining
both coefficient levels, every path filter and all exterior heat modes.
This could allow a later signed frozen-trace bound, not yet a limit.

Essential inputs: L110 L111 L113 L114 L115. L088 specifies the paths;
L099 supplies the separate frozen comparison, and L091 the assembly.
L111/L113/L114/L115 control different placements and do not remove these
remaining compressions. ATTEMPTS/028--032 stay in force for their specific
failed shortcuts. Ready coverage is reused; no new literature is needed.

Working identity: write Q_q=J_q J_q^*, use infinite path stencils
S_alpha^infty with S_alpha=J_1^* S_alpha^infty J_2, and put
f=b_(r,t) phi_(l,alpha,s) phi_(k,beta,t). Compact support gives
M_f Q_2 (S_alpha^infty)^* Q_1=M_f (S_alpha^infty)^* exactly.
After lifting the finite trace, only
Q_1 S_beta^infty Q_2 A_r E_j M_f
must be compared with S_beta^infty A_r E_j M_f. Its difference is
[(Q_1-I) S_beta^infty A_r+Q_1 S_beta^infty (Q_2-I) A_r] E_j M_f.
Each term samples E_j only at output rows separated by c N from
the input support. L110/L111 suggest HS error
C p(k)p(l) N^(1/2) (Q_j+W_j). Pair with the compact-column
(S_alpha^infty)^* P_inf factor of HS norm O(N^(3/2)); outside a
and weighted axial sum O(N^2) would then give O(N^3).

Continue if this exact trace identity, boundary tail estimate and full
level/heat sums hold. Stop if a finite end-edge path differs from the
claimed compression, compact input is transferred to nonlocal output,
or a filter must cross P_inf. No such property is assumed as proved here.
The frozen transfer and all cubic placement-error limits remain open;
no negligible cubic error, finite H limit or compensation is assumed.

Completed: L116 proves the comparison with the stronger error o(N^3).
The exact input-support identity removes the right compressions; the
left compression error samples only distant rows of the joint energy
kernel. Its full quadratic tails are summable over every axial offset
and vanish after that sum. L116 also records the exact remaining
full-grid diagonal, without asserting its signed cancellation. This
is RESEARCH / REPRODUCTION, local standard-method progress only.

Continuation within the unchanged approved complete-group target:
test whether L116(4)--(5)'s complete signed coefficient sum is O(N^3)
using L088/L099's frozen cancellation, with controlled comparison of
the actual path coefficients to their local constant-field values.
Retain both distinct levels, all filters, both orientations and every
heat mode. Essential inputs: L088 L099 L110 L111 L113 L114 L115 L116;
L091 supplies assembly. Continue only if the summed remainder is at
most cubic; stop if the cancellation requires equating the levels,
omitting path phases or moving a component filter through P_inf.
No cubic bound for R_inf, negligible earlier O(N^3) placement errors,
finite transverse H limit or evaluated compensation is assumed.
L097 L098 L100 L101 L104 L107 retain other limits, while L084 with
L079 L080 L082 fixes the reference and its numerical qualifications.
Other jets, finer powers/logarithm, matching, interacting error
<=c_box/2, continuum axioms, reflection positivity, infrared control
and finite positive mass remain open. Preserve ATTEMPTS/028--032.
