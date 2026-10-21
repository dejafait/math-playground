# Cyclic 0135 quotient attempt

Approved input: `drafts/literature/2026-10-06-cyclic-0135-full-rank.md`
(EXPLORE saved before invocation). Main gap: sixteen-support equality,
with the count interval still eleven through sixteen. Target: rank 28
of the full alternating matrix for every H-labeling of J_t={t,t+1,t+3,t+5}.
The downstream use is an independent family obstruction; other support
families and dependent-direction/application checks remain separate.

Decision test: complete the uniform quotient certificate, retain a rigorous
residual constraint, or stop the criterion on a certified deficient labeling.
No genericity or labeling sample is a substitute for uniformity. The local
duplicate/failure check used L010, L026, L027, L028 and ATTEMPTS/019;
the old containment failure remains preserved.

Checkpoint before canonical write-up: in the basis b_0,...,b_7, the first
three blocks leave pairs 02,12,13,15,17,23,25,34,36,45,56. Block 3,
J_3={3,4,6,8}, uses quotient basis q_0,q_1,q_2,q_5. Its only nontrivial
extra coefficient is the q_0 coefficient of q_7, forced nonzero by
eight-column independence. The restricted map has rank five, leaving
13,23,34,36,45,56. Subsequent kernels are 34,45,56; then 45,56;
then 56; then zero at block 7. No exceptional division is proposed.
The completed proof and all quotient independence checks are now canonical
in [L029](../lemmas/L029-cyclic-0135-eight-block-rank.md). This saved
checkpoint preserves the attempt's initial reasoning; it is not an
additional proof. The result is a local rank advance, with separate
critical audit and equality-pencil application still pending.
