# Attempt 001 — Finite residue correction with bounded return time

Tested on 2026-09-24. The proposed sufficient certificate was V(n)=log(n)+h(n mod q), with fixed q,K,N, such that every n>N has an iterate within K shortcut steps with smaller V. Finite base verification and the finite sublevel sets of V would then force convergence. The scheme was ruled out by an exact construction, not by failure to find suitable coefficients.

## WHY IT FAILS

[L001](../lemmas/L001-finite-residue-bounded-window-obstruction.md) constructs infinitely many starts above every cutoff with positive potential change at every time in the proposed window: all the relevant residues coincide, so every possible h cancels. Larger fixed moduli, larger fixed windows, residue-dependent windows with a common finite bound, and finitely many extra exceptions leave the obstruction intact. A variable-length return time or a correction using additional size information lies outside the theorem, but still needs its own descent argument. This is an obstruction to the certificate, not a disproof of Collatz; the witness can change with the requested prefix length.
