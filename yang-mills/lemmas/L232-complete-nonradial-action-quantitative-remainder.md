# L232 — Complete nonradial-action quantitative remainder

## Hypotheses

Use L213(1)'s complete response

\[
 G_i^{\rm nr}(a)=-\kappa_0(f_{i,0},r_0,S_4-S_{4,\rm rad}),\qquad i=3,6.
\]

Keep the pinned relative SU(2) cube (-4,4)^4, straight lower-rooted
direction-1 forest, sufficiently large admitted even N, a=8/N, both
actual probes at tau=1/16, and the bare expansion at fixed mesh before
refinement. Use ordinary stored dimensionless coordinates. All colors,
plaquettes, traversal signs, normal end rows, allowed constant modes,
upper jumps, both residual subtractions and full heat sums are retained.

Import L213(3), L215(6),(15), L216(1)--(2),(9), L217(6),(14),
L230(1) and L231(1), with their stated analytic hypotheses. L230 proof
section 7 and L231 proof section 6 accept their component estimates
relative to their imported inputs. No recursive audit of those inputs
is asserted here. Let P_i and A_i^dm be exactly the coefficients of
L216(9) and L217(6), without evaluation or renormalization.

## Conclusion

There are finite constants C_i and N_0, independent of N, such that
for all admitted even N>=N_0 and both probes,

\[
 \left|a^3G_i^{\rm nr}(a)-(P_i+A_i^{\rm dm})\right|
       \le C_i N^{-1/2},                                      \tag{1}
\]

and consequently

\[
 \left|G_i^{\rm nr}(a)-a^{-3}(P_i+A_i^{\rm dm})\right|
       \le (C_i/512)N^{5/2}.                                 \tag{2}
\]

This is a quantitative rate for the complete nonradial quartic-action
group only. It neither estimates all of L011 nor uses L219's evaluation
or L220's cubic cancellation. Other component rates, the interacting
reflected-error bound <=c_box/2, continuum axioms and finite positive
physical mass remain unresolved. There is no construction candidate.
This is a finite reproduction/assembly of existing estimates, with no
claim of progress beyond the sources checked. The separate critical
audit in proof section 4 accepts this assembly relative to its stated
imported inputs.

## Proof

### 1. Exact finite partition and its error

Write T_i^(0) for L213(2)'s complete transverse no-internal-action-pair
class and tilde T_i^(0) for L215's partially replaced contraction.
For each local signed traversal pair, L215(15) expands the actual
lifted residual covariance into one direct/direct block, two negative
mixed blocks and one positive two-prefix block. The replacement
changes only the last block, from f_e^T A_11 f_f to g_e^T A_11 g_f.
For the common axial plaquette level j this last expression is exactly
L216(1)'s q_e^T G A_<j G q_f, including its traversal signs.
The other three terms are exactly L217(14)'s V_p^dm.

The contraction -24 sum_(p in P_T) K:U_(i,p):V_p is linear in V_p.
Its tensor, exterior matrix, color blocks and plaquette set are identical
in these definitions. Therefore, at every finite admitted mesh,

\[
 \widetilde T_i^{(0)}=T_i^{\rm pl}+T_i^{\rm dm}.               \tag{3}
\]

Both mixed orientations occur separately in T_i^dm, with their original
negative signs. The positive plateau occurs once. No Gaussian-tilt
factor 2, outside factor 3 or two-cubic-action term enters (3).
Fixed traversal rows remain zero and variable normal end rows remain
present, so (3) does not remove a boundary class.

Define E_i=G_i^nr-tilde T_i^(0). L215(6) directly supplies

\[
 |E_i|\le c_{i,0}a^{-5/2}.                                  \tag{4}
\]

This bound already combines L213(3)'s discarded classes with L215's
scalar-block replacement error. In particular it includes the axial
classes, upper three-edge signed sums and transverse internal-pair
class. We use (4) once and do not add L213's allowance again. All full
heat sums have already been bounded by that input. Equations (3)--(4)
are the complete finite-response partition needed here, rather than a
quantitative interpretation of L216's qualitative o(1) statement.

### 2. Combine the finite estimates in the original normalization

Take N_0 large enough for (4), L230(1) and L231(1) to hold, for both
probes. Those component bounds are

\[
 |a^3 T_i^{\rm dm}-A_i^{\rm dm}|
       \le c_{i,\rm dm}\log(eN)/N,\qquad
 |a^3 T_i^{\rm pl}-P_i|\le c_{i,\rm pl}N^{-1/2}.              \tag{5}
\]

The constants in (4)--(5) depend only on the fixed data, not on N.
Subtract the unchanged summed coefficient from a^3 times (3) plus E_i
and apply the triangle inequality. Since a=8/N, this gives

\[
 |a^3G_i^{\rm nr}-(P_i+A_i^{\rm dm})|
 \le \sqrt8\,c_{i,0}N^{-1/2}
       +c_{i,\rm dm}\log(eN)/N+c_{i,\rm pl}N^{-1/2}.         \tag{6}
\]

For real N>=1,
log N=integral_1^N t^(-1)dt <= integral_1^N t^(-1/2)dt
=2(sqrt N-1), so log(eN)<=2sqrt N. Thus (1) holds with
C_i=sqrt8 c_(i,0)+2c_(i,dm)+c_(i,pl).
Finally a^(-3)=N^3/512 gives (2). Taking the maximum of the two
constants also gives a single constant valid for i=3,6. No sign,
positivity, coefficient cancellation or interchange of limits was used.

### 3. Coverage and checks

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-nonradial-action-rate-assembly.md`.
Its exact target and hypotheses are unchanged. The proof specializes
only the cited canonical finite identities and bounds; it requires no
new external theorem or reproof of a source estimate. That assessment
records the primary Green/Taylor sources supporting the component
work, and the duplicate and failure checks in ATTEMPTS/011--013.
No raw-loop bound or smooth upper-pin extension is introduced here.

The meaningful checks are the exact four-block partition (3), the
single use of (4), equality of the two subtracted coefficients in (5),
the a^3/a^(-3) factors in (6) and (2), and the elementary uniform
logarithmic comparison. These are analytic finite equalities and
inequalities; a numerical mesh test would not verify their hypotheses.
The achieved threshold is O(N^(5/2)), without the formerly allowed
logarithmic loss. No stronger remainder for this group is asserted.

### 4. Separate critical audit, 2026-10-18

**Verdict: accepted relative to L213, L215, L216, L217, L230 and
L231, with their upstream analytic hypotheses imported.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-complete-nonradial-rate-assembly-audit.md`.
This audit checks (3)--(6) and their implication (1)--(2), not the
upstream kernel or spectral arguments. No missing class, sign error,
changed coefficient or nonuniform assembly constant was found.

**Exhaustion before replacement.** L213(1) is the same complete
negative cumulant as the present G_i^nr. Its (2) keeps precisely the
transverse no-internal-action-pair class, with coefficient -24 and
signed color/traversal indices. L213(3) and proof section 4 account
for the non-upper axial classes, both upper three-edge classes, the
transverse internal-pair class and the identically zero fixed/lower
classes. The upper bounds are for complete signed sums; this audit
does not replace them by an absolute plaquette estimate. Their use
therefore loses no orientation, pairing class or boundary layer.

**Exact four-block identity.** In L215(15) the two forest row minus
signs produce a positive two-prefix term, while the two mixed terms
are individually negative. All four transverse plaquette rows share
the same axial cut j. With B_j=b_j^T tensor I as in L216, the signed
version of L215(3) gives g_l=B_j^T G q_(p,l). Since G is symmetric,

    g_l^T A_11 g_m
      =q_(p,l)^T G (B_j A_11 B_j^T) G q_(p,m)
      =q_(p,l)^T G A_<j G q_(p,m).

A pinned endpoint is omitted in each dipole on both sides; for a
fixed link its selector and dipole vanish. Thus this identity includes
variable normal end rows. Negative traversals change both the direct
selector and its dipole, without a second sign outside the tensor.
The displayed expression is L216(1) exactly. L217(14) is precisely
the other three terms of L215(15), with I_1 absorbed into its axial
selectors. Both mixed fibers end at j-1, or -1 after translation;
no endpoint shifts between the definitions.

L215 keeps K and U_i unchanged. Extending these scalar blocks by the
same three diagonal color blocks and applying the linear contraction
-24 sum K:U_i:(.) proves (3) at finite mesh. There is no additional
tilt factor 2 or factor 3 from the two-cubic-action group. These are
disjoint blocks of one contraction, not overlapping complete cumulants.

**Single complete-response allowance.** L215(6) bounds a sum of two
nonnegative absolute errors. Its second summand is exactly
|G_i^nr-tilde T_i^(0)| and implies (4). L213 justifies that imported
complete allowance; it is not added to (4). The two errors in (5)
compare the blocks of (3) with their own coefficients and duplicate
neither allowance. No rate is assigned to L216(16)'s qualitative o(1).

**Applicability and constants.** L230(1) subtracts exactly L217(6)'s
A_i^dm and excludes the plateau. L231(1) subtracts exactly L216(9)'s
P_i and includes only that plateau. Their canonical audits, sections
7 and 6 respectively, accept those finite estimates relative to their
inputs. Their cube, forest, stored coordinates, probes, tau, admitted
meshes and bare-first ordering agree with the present ones. Constants
already include the full heat sums and may depend on the fixed data,
but not on N. The maximum of the finitely many starting mesh thresholds
is legitimate; no qualitative limit is used to choose it.

Multiplying (4) by a^3 gives c_(i,0)sqrt(a), exactly
sqrt(8)c_(i,0)N^(-1/2). Subtracting P_i+A_i^dm before estimating gives
(6) without a sign assumption. For N>=1,
1+log N<=2sqrt(N)-1<=2sqrt(N), so

    C_i=sqrt(8)c_(i,0)+2c_(i,dm)+c_(i,pl)

is independent of N and proves (1). Multiplication by N^3/512 proves
(2) with exactly C_i/512. Taking the maximum over i=3,6 is permitted.
The achieved unscaled threshold is O(N^(5/2)); no evaluation or
cancellation from L219 or L220 is needed.

These checks establish a reviewed local input, with no stronger rate
or new discovery beyond the sources checked. They neither reprove an
external theorem nor recursively certify the analytic imports.
ATTEMPTS/011--013's raw-loop and upper-pin obstructions are preserved.
Numerical tests are not needed for these finite identities and bounds.
Other L011 rates, interacting reflected error <=c_box/2, continuum
axioms and finite positive mass remain open. The argument and direct
inputs are unchanged, so the existing DAG row remains sufficient.
Mathlib qualifications below are unchanged.

## Mathlib

Full matching coverage of this forest-action assembly: **not checked**.
Supporting finite linearity, triangle inequalities and elementary
logarithmic bounds: **not checked**. Unknown coverage is not absence.
No matching Mathlib declaration or certified originality is claimed.
