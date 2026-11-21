# Terminal-shear finite audit continuation1588

TARGET: Audit C028i's terminal-shear multiplication, trace-norm factor, unrestricted substitution and equality cases, and verify that its c*d floor stops only the specified majorant family.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1587 and source-notes1587's bounded exact-shear comparison, plus assessments1523/1524 and audit1527; no changed family or new external theorem is proposed. Current calculation1588 searched the specific C028 proofs and companion histories/assessments for duplicates and retained prior stops.
SOURCE_EVIDENCE: Schmeisser2002 Section3 Lemma1 pp211-212 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; Higham2021 determinant identity(*) https://nhigham.com/2021/03/23/what-is-a-companion-matrix/ ; Watrous2018 Section1.1(1.175),(1.179)-(1.181) pp32-34 https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf . Exact hypotheses/read cases remain those recorded in source-notes1587 and approval1524; no fresh source retrieval is claimed.
COMPARISON: These standard inputs cover every square matrix after an invertible shear and compatible rectangular compression, without normality or simple roots. C028h already optimizes the unsheared block. C028i's new local specialization claims a reduction to that optimum; the proposed audit verifies its algebra rather than reproving imported matrix results.
GAP: C028i has a written finite proof but no separate independent replay of its support/order, skew factor, parameter substitution, all-d floor or strict nonzero-shear equality exclusion. Actual H_d=o(d) and S_F=0 remain independent unpaid gaps.
REASON: A finite ordinary audit can confirm or repair the newly established method-specific stop before changing mechanisms. This newly written continuation requires separate next-turn approval; it was not invoked in calculation1588.
SCOPE: Only C028i's actual centered A_d, d>=3, S=I+t E_(d,d-1), real unbounded degree-dependent t and arbitrary positive diagonal D in the fixed order D S A_d S^(-1) D^(-1); trace norm of the last-three Hermitian compression. No extra coordinates, shear, RH, root simplicity, diagonalizability or conditioning bound.

## Audit inputs and bounded test

Read C028i in full and the relevant C028h block/optimization/audit ranges.
The sole local direct mathematical input claimed for C028i is C028h;
C028a/d's coefficient facts enter through that established result.
C028b supplies the downstream multiplicity-counted height criterion,
not the matrix estimate. Standard sources above are imported at their
recorded hypotheses; no additional theorem discovery is needed for
this unchanged finite scope. Full matching Mathlib coverage is unknown.

Replay S^-1=I-tT using T^2=0; verify the full-size compression commutes
with the terminal-supported shear despite exterior companion entries.
Check left row and right column operations, then positive diagonal
ratios. Expand the three-by-three skew determinant with 1/(2i).
Check cancellation in the first two squares, the equality x^2=b/y,
k=sqrt(1+t^2*y^2)>=1, r=y/k>0, and the unrestricted comparison to
C028h's f_d(r). Confirm its same c and onset, attainment at t=0,
and strict exclusion of nonzero t, including d=3. A hand replay is
sufficient; do not perform a parameter sweep or infer an upper bound
from the compression.

Continue by accepting the stop only if every displayed identity and
inequality survives these checks. Otherwise correct the precise error
and state whether the uniform floor remains proved. No independent
actual-height or RH conclusion is authorized. Recommended routing:
proof_audit/routine_audit, standard/high; classification REPRODUCTION.
An independent o(d) full-cost mechanism is still missing, so no
justified creative upper-payment target has yet been nominated.

## Separate source approval1589 (2026-11-18)

LITERATURE_REASON: The supervisor requires separate approval of the newly
written assessment1588 before the saved C028i audit; essential source
coverage is reused rather than refreshed for scheduling.

Approved unchanged as SPECIALIZE for precisely TARGET and SCOPE above.
Read source-notes1587 in full, assessment1587, the primary-statement and
URL-recovery sections of source-notes1523, and histories1524/1527.
These retain inspected source versions, exact theorem locations, direct
URLs and read limits. No new external retrieval or broader theorem
comparison is claimed. Schmeisser's arbitrary-square-matrix statement,
Higham's companion convention and Watrous's compatible rectangular
ideal inequality cover the proposed audit's imported inputs. The
unread Gohberg--Krein book proof is not essential because Schmeisser's
stated matrix lemma itself is imported. No need to reproduce it.

Checked C028i's hypotheses/conclusion and imported-input section against
this coverage, without replaying its multiplication or optimization.
Its full finite calculation and equality claims remain unaudited.
The recorded C028h audit1527 and retained ATTEMPTS1588 distinguish the
old diagonal stop from the new single-shear stop; neither is an actual
height lower bound. Prior duplicate searches in source-notes1587 cover
this unchanged family; no novelty follows from their negative search.
No new coefficient identity, sign assumption, norm conversion or
asymptotic interchange is needed for the finite audit. Mathlib matching
coverage remains unknown, as already qualified in the canonical result.

Outcome STALLED: this separate gate review confirms existing coverage;
it establishes no new mathematical evidence and no expanded source
scope. Next turn should perform exactly the bounded hand audit above,
using C028i in full and C028h's relevant proof/audit ranges. Keep
C028a/d coefficient facts at their established hypotheses and C028b
only as downstream context. Accept the stop only if all displayed
identities, unrestricted comparisons and equality cases pass; otherwise
repair the precise error and reconsider whether the floor survives.
No full-cost upper estimate or independently supported signed compact-mass
mechanism is ready. That remains the blocker to an honest creative
central-gap nomination; this essential audit is not relabeled creative.
