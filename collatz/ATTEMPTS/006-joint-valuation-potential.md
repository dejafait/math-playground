# Attempt 006 — A correction using both shifted valuations

Tested on 2026-09-25. The proposed potential was
V(n)=log(n+5)+c v_2(n+5)+d v_2(11n+19), with c,d>=0 and strict
decrease on every (2,1) and (3,1) complete block outside a finite set.
The two shifts arise from the single-letter repetition identities in
L005. Such a potential would exclude infinite itineraries in this
restricted alphabet: its value is at least log(n+5), while both block
maps increase n by a factor greater than or equal to 9/8. Other block
types and universal eventual descent would still need separate control.

## WHY IT FAILS

[L006](../lemmas/L006-joint-valuation-potential-obstruction.md) gives
arbitrarily large legal two-block paths with valuation pairs
(5,2), (2,6), (5,2) and shifted size increasing by at least 93/49.
Every correction F of the pair cancels between the first and last
endpoints, even if F is nonlinear or nonseparable. At least one block
has potential increase at least (1/2)log(93/49), defeating every finite
exception set. This rules out all real coefficient choices and all
functions of these two valuations for decrease at every permitted block.
It does not rule out unbounded return times or other information. The
valuation return is not an integer cycle and cannot be extrapolated to
an infinite growing positive orbit.
