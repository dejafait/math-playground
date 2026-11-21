# Degree12 time-edge model — failed auxiliary cap, step154

The approved single pass stopped after 22528 of 690988 terms. The saved
[working record](../drafts/2026-11-10-physical-time-edge-taylor-working-154.md)
identifies the implementation, exact partial evidence and diagnostic.
There is no completed mathematical lemma or positivity certificate.

## WHY IT FAILS

The implementation chose the unproved uniform majorant cap
v=h*(|Re beta_n|+|Im beta_n|)<=2 to use exp(v)<8 in the real-coordinate
tail. A bounded direct-log diagnostic in the unfinished block gives
v>2 at n=23545 (approximately2.00000091765). The assertion correctly
aborted an invalid cap. No complete-support model, final remainder or
Bernstein sign exists. This is a failure of the chosen cap, not an
obstruction to degree12 approximation or evidence of a negative physical
form. Preserve the failed pass: failed gates stop this test. No cap
increase, subdivision, sweep or degree retry was performed. Any future
different target needs its own scope; this pass is not completed evidence.
