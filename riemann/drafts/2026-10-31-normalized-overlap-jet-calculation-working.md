# Approved normalized-overlap jet calculation

Gate: `literature/2026-10-31-normalized-overlap-fourth-jet-test.md`
(SPECIALIZE, unchanged at invocation). Inputs L019/L239 and L233.
Only the actual quotient's fourth zero jet is being evaluated.

Let b(t)=C_k(2t)=integral k(s+t)k(s-t) ds, and a(t)=A(t).
Writing k_j=k^(j)(s), the differentiated overlap factors at t=0 are
q_0=k_0^2, q_2=2k_0k_2-2k_1^2,
q_4=2k_0k_4-8k_1k_3+6k_2^2.
Then b_j=integral q_j, a_j=integral s^2 q_j, for j=0,2,4.
All are full-line integrals. The quotient rule gives
v_0=a_0/b_0, v_2=(a_2-v_0 b_2)/b_0,
v_4=(a_4-v_0 b_4-6v_2 b_2)/b_0.
The target is v_0 v_4-v_2^2, threshold zero.

A nonrigorous Simpson preview gives approximately 0.111569934.
This is NOT a certificate. Pending: complete directed interval integrals,
midpoint error bounds, all-mode tails, and the analytic applicability proof.
Planned certificate uses exact polynomial recurrence
P_0(v)=8v^2-12v,
P_(j+1)=(1/2-2v)P_j+2v P'_j,
so k_j(u)=e^(u/2) sum P_j(pi n^2 e^(2u))e^(-pi n^2 e^(2u)).
Preserve all prior unfinished work. No all-frequency conclusion follows.

## Completion of this attempt

The preview and pending notes above are preserved as a checkpoint, not
used as evidence. The completed proof is canonical in L602; the complete
certificate is `scripts/normalized-overlap/fourth-jet-certificate.json`.
The determinant is enclosed in [0.111440279693024071740668487883077875076364046,
0.111699725815406230855769734184448542065713220], strictly above zero.
All six complete integrals, seven derivative-tail and geometric-ratio
bounds, real-variable tails, polynomial coefficients and midpoint-error
fields were inspected. The exact tested scalar passes one necessary
condition. Neither positive definiteness nor a first/all-degree sign
is proved. A separate critical audit of L602 is the proposed continuation;
there is no reason to tighten the already decisive numerical enclosure.
