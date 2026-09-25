# Attempt 004 — A correction depending only on v_2(n+5)

Tested on 2026-09-25. The proposed potential was
V_c(n)=log(n+5)+c v_2(n+5), with c>0 chosen to make every complete block
outside a finite exception set decrease. Its finite sublevel sets would
force entry into that set, whose convergence would still require proof.
L003 motivates the correction: c>log(9/8)/3 compensates for every growing
(2,1) block. This unbounded valuation lies outside the finite-residue
obstructions, so a separate test was needed.

## WHY IT FAILS

[L004](../lemmas/L004-shifted-valuation-potential-obstruction.md) constructs
arbitrarily large starts 128s+103 with complete (3,1) block endpoint
216s+175, both having v_2(n+5)=2. Every real-valued correction F of this
valuation therefore cancels exactly, while logarithmic growth gives an
increment at least log(5/3)>0. This refutes all constants c, all such
functions F, and every finite exception cutoff. A second growing family
has unbounded positive valuation gains, which further obstruct positive
c. The failure is decrease at every block for this particular information;
eventual decrease over an unbounded number of blocks and corrections using
other arithmetic information remain untested. This is not a disproof of
Collatz.
