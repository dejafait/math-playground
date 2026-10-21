# 2026-10-11 — Prescribed local torsion with global mod-7 image

Approved target: establish whether L044's integer cubic approximation
can be chosen with global mod-7 image GL_2(F_7) while preserving its
full local 210-torsion module. Reuse the startup SPECIALIZE assessment
`drafts/literature/2026-10-11-mod7-surjective-local-approximation.md`.
The complete L044/L042 proofs and relevant audit/stop records were read.
There is no earlier global-image result in the targeted local search.
Existing changes and unfinished work are retained.

Saved working checkpoint before completing the proof: fix sufficient M and
the integer quadratic coefficient c of L044's monic cubic; put h=3^M.
For d=d_0+h s and e=e_0+h t, the pointed Q-change
X=9x+3c, Y=27y gives A=81d-27c^2 and
B=729e-243cd+54c^3. The parameter matrix has determinant
3^10 h^2, so this is a full-rank affine lattice, not a thin family.
The intended comparison is a positive multiple of X_bound^2 versus
Zywina's O(X_bound^(3/2) log X_bound) exceptional count at fixed M.
Still to write completely: projective inverse, count including
singular models, cited global-image implication and full local-module
transport. No image preservation after restriction to F is assumed.

The main gap remains original finite B>=A. Passing supplies only
a global-image prerequisite; full initial data, geometric parameter,
native/input/action, pilot transport and essentiality remain open.
The continuation/abandonment test is the full-rank count and retention
of the original congruences and Q-defined pointed isomorphism.

Completed outcome: the test passes. The full proof and qualifications
are canonical in
`lemmas/L046-surjective-mod7-approximation-preserves-local-torsion.md`.
The candidate count has positive leading term 4R^2/3^(2M+10),
dominating the imported O(R^(3/2) log R) exceptional count. No
mathematical script was needed. The direct mathematical input is
L044; its L042 packet is retained, while L045 is downstream. This is
REPRODUCTION of known methods, not progress beyond the sources checked.
The next direction is a separate critical-audit coverage review;
no new target is approved or researched in this step.
