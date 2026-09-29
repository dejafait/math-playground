# Attempt 017 — Terminal stable resolution with one polarization

Date: 2026-09-27. Outcome: stopped at the common-metric Chern test.

The tested recipe is Mistretta's terminal stable resolution of I_C
using powers of one ample product polarization, allowing any final
line-bundle twist. Its ch_2 action is U. The full proof is
[L026](../lemmas/L026-stable-resolutions-fail-common-metric-chern-test.md).

**WHY IT FAILS.** The normalized second Chern character is invariant
under line-bundle twists. Its mixed operator on divisor classes is
2 id plus a rational rank-one correction, so all its eigenvalues are
rational. Diagonal SU(2) invariance would force U's irrational cubic
eigenvalue on the metric's Kahler class. Thus the first two Chern
classes cannot both be invariant, for any allowed construction
choices. This rejects the recipe before testing stability at the
required metric; it does not reject arbitrary compatible bundles
or presentations with other divisor-tensor corrections.
