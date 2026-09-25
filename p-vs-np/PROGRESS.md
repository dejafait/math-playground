# Current checkpoint

STATUS: IN_PROGRESS
STEP_ID: 2026-09-25-10-tseitin-resolution-versus-decision
STEP_OUTCOME: NEGATIVE
STEP_EVIDENCE: lemmas/L010-tseitin-resolution-versus-decision.md constructs Tseitin CNFs requiring 2^(Omega(N/log N)) resolution lines while one total SAT decider solves every family member in polynomial time, refuting the proposed instancewise proof-size transfer.
Bottleneck: No unconditional NP language outside P or polynomial-time SAT algorithm is established. Resolution lower bounds do not constrain arbitrary decision computations on the same instances; no adequate simulation by a stronger proof system is established.
Route decision: Stop the direct resolution-length-to-decision-time inference. Investigate the missing simulation requirement for a stronger proof system; preserve earlier branches.
Exploration turns used: 0
Next action: Construct the proof system induced by a hypothetical polynomial-time SAT decider and test whether extended resolution can simulate it with polynomial overhead without assuming short proofs of the decider's correctness.
