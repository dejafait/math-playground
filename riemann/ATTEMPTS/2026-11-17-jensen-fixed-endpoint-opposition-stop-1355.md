# Finite Jensen reference: fixed endpoint opposition fails1355

The canonical [C019f proof](../lemmas/C019f-actual-jensen-signed-airy-reference.md)
establishes a uniform normalized Airy limit and rigorously encloses its
values at x=1,2,4. The original opposite-endpoint target is false: both
fixed endpoints are negative. This is a local sign obstruction, not an
RH counterexample. The new canonical result still needs a separate audit.

WHY IT FAILS: the exact normalization selects
4^(1/3) Ai(-16*4^(1/3)*x/pi^2); its signs are negative, positive, negative
at 1,2,4 respectively. Thus one cannot force a sign crossing by comparing
only the ends of this entire window. There are nevertheless simple reference
zeros inside the window, and the uniform limit remains useful. Preserve
both endpoints and this stop evidence. Changed windows or actual-polynomial
root-transfer claims require their own assessed target. Stop1345's
automatic-import obstruction remains a separate historical failure.
