# Fixed lower Chern data cannot supply a compatible polystable bundle

Date: 2026-10-04. Classification: REPRODUCTION. Outcome: NEGATIVE.

Tested arbitrary positive rank and unrestricted higher characters,
with c_1=0, ch_2=2[C]+B_c and the exact real product polarization
in L044's final ample chamber. This is broader than the fixed
rank-two K-class stopped in the preceding attempt.

WHY IT FAILS: [L046](../lemmas/L046-fixed-lower-chern-bogomolov-exclusion.md)
computes a strictly positive second-character intersection, whereas
the cited Bogomolov inequality requires it to be nonpositive when
c_1=0. The contradiction holds at every positive rank and uses no
higher Chern class. This closes the unchanged lower data, not
other representatives of the cubic action or the rational Hodge
conjecture. Pure point corrections are a separate numerical test
already covered by the saved assessment; satisfying a necessary
inequality would still supply no bundle or transverse transport.
