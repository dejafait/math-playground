# One-coordinate quotient geometry — 2026-09-25

Read the shared rules, local target and checkpoint, whole overview, DAG, and
relevant proofs before choosing this step. Inspected existing changes and
preserved them. The [official statement](https://proximityprize.org/) was
reread: it still gives the prescribed-error target and a preliminary statement.
The separately pinned affine-line event is the scope of this calculation;
the unread ABF26 correspondence is not assumed or repaired here.

Gap: L004's certificate budget need not be simultaneously realizable across
bad challenges. At support cutoff n-1 its small-field test found two bad
challenges although its upper bound permits three. The sharp error at fixed
field size is therefore still missing even on this first nontrivial cell.

Intermediate target: prove E_C(delta)=2/q whenever 1<=k<=n-3 and
1/n<=delta<2/n, uniformly over distinct RS evaluation points. Downstream use:
an exact safety condition q>=2/epsilon for this cell, and a first test of
whether quotient geometry can replace loose certificate counting. Wider
radius cells, the paper-to-model correspondence, and endpoint and field-size
qualifications remain unresolved.

Test and decision rule: use Q=F^I/C and the images of coordinate vectors.
Try to exclude three transverse intersections of an affine line with the
one-coordinate subspaces, then construct two intersections. Check the result
by direct punctured-code membership over small fields, including zero quotient
directions and lines through the origin. Continue this mechanism if both the
uniform upper bound and an attaining pair survive; abandon the proposed
two-challenge formula if three admissible challenges occur under its stated
hypotheses. Compare 2/q with the actual error budget 2^-128, not just L004.

Redundancy and previous failures: L001 concerns radius cells, L003 counts
small certificates, and L004 gives their multiplicity; none proves this exact
cell. The endpoint-transfer and single-field disproof failures are preserved
and are not reopened. This is a new geometric mechanism, with zero consecutive
exploration turns entering the step.

## Saved unfinished reasoning

The polynomial root bound makes every nonzero codeword have weight at least
n-k+1>=4. Consequently any three distinct coordinate images in Q are
linearly independent. Write A=[a], B=[b], and U_i=F[e_i]. A support omitting
i witnesses a bad challenge exactly when A+gamma*B belongs to U_i but B
does not; full support instead requires A+gamma*B=0 and B nonzero.

If B=0 there are no bad challenges. If the affine line passes through zero,
only its zero point can be bad: every other intersection with U_i has its
direction in U_i. Otherwise all intersections are nonzero, each U_i supplies
at most one, and three of them would put three independent coordinate images
in span(A,B), which has dimension two. Thus at most two challenges seem
possible. The pair a=e_i, b=e_j-e_i should attain gamma=0 and gamma=1,
using the supports omitting i and j respectively.

This reasoning still needs a full statement, qualification check, and direct
finite test. It is not a complete challenge candidate.

## Completed assessment

The geometric mechanism succeeds. The full argument and attaining pair are
in [L005](../lemmas/L005-one-coordinate-sharp-error.md). It proves the exact
error 2/q throughout 1/n<=delta<2/n when 1<=k<=n-3, hence safety at the
actual 2^-128 budget exactly when q>=2^129. At length 16 the four listed
dimensions previously allowed 3,4,6,8 challenges by L004; the exact number
on this cell is two in every case. This does not extend the earlier
length-256 sufficient interval delta<90/256 and does not settle a maximal
safe radius.

The direct polynomial-membership check passed 528,620 pair classes across
five parameter sets. Four satisfy the theorem, including F_4; the fifth,
F_5 with n=4 and k=2, lies outside the hypothesis and attains four challenges.
L005 includes the explicit boundary example with a direct algebraic check,
so this qualification does not rest on enumeration. Lines through zero,
zero quotient directions, both admissible support sizes, the same-support
failure condition, and the strict radius endpoint were reviewed in the proof.

Outcome: ADVANCE for a relevant sharp partial result; zero consecutive
exploration turns remain. The reason to continue the geometric mechanism is
that it removes proven slack in the certificate budget. Its natural next
test involves two-coordinate error subspaces, where the three-independent-
coordinate argument no longer suffices. The concrete action is recorded only
in PROGRESS.md. The ABF26, endpoint, and wider-radius gaps remain open, and
there is no complete challenge candidate.
