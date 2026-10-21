# Attempt 022 — Nineteen-word fixed 48/25 comparison

The approved target retained L041's nineteen-dependent seed, own-index
bounds, shifted endpoints and length conversion, and L044/L046's
existing numerical transfer coefficient 48/25. No stronger input was tested.

## WHY IT FAILS

[L047](../lemmas/L047-nineteen-word-fixed-transfer-obstruction.md)
assembles the nineteen-word necessary length inequality and gives an
exact scalar obstruction at N=370000000: its right side exceeds
392550000. This length is above even (8/5) times the published primitive
odd-count threshold. The inequality still gives a conditional ceiling
N<10^9, but cannot contradict the whole admissible length ray. Stop
this fixed comparison. The scalar length assigns no heights, parameters,
primitive counts, parities or closure, and establishes no actual
feasibility or cycle. A separately covered changed bound or additional
retained information is required for any renewed exclusion attempt.
Attempt 021's factor-2 stop and L045's weaker witness remain valid.
