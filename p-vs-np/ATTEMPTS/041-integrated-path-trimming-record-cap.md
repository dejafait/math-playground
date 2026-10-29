# Attempt 041 — whole-operand trimming before all L035 calls

The step-476 SPECIALIZE target was attempted on exactly the retained
step-470 proof/request and step-461 occurrence data, using the scalar-aware
translator and unchanged constructors, receivers and caps. Canonical evidence
and qualifications are in [L097 §14](../lemmas/L097-source-resolution-occurrence-product-affine-abp-witness.md).

**WHY IT FAILS.** Source-to-sink trimming completes the old isolated pair,
but a later nonzero sum-commutator at source record 22, Boolean parent 196,
event 219 still requires 3,586,238 records against 2,000,000. Its actual
restricted operands have 45/57 and 83/107 vertices/edges. All 220 saved trace
events and both complete operand polynomials pass independent prefix reception;
full structural checks bind the retained 45 blocks and verify the rejected
ledger. Complete evidence is in scripts/four-rule-extraction/output-477/.
No K/H exists and the occurrence direct wrapper is not reached. Stop this
exact whole-operand-trimming/input/unchanged-constructor combination without
raising caps. This is a bounded representation failure, not an algebraic
counterexample, a proof lower bound or a SAT result. A changed internal branch
inventory needs separate source approval and an independently testable target;
no such change or passing bound is established by this attempt.
