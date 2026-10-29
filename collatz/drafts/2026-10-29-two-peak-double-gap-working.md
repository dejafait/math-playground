# Step546 — double-gap symbolic pass (2026-10-29)

The approved target and coverage are unchanged in
`literature/2026-10-29-two-peak-double-gap-symbolic-test.md` (EXPLORE).
Main gap: universal eventual descent. Intermediate target: the cap
T^j(n)<=n+1 for the exact assessed family. Downstream use: reduce its
non-descent cases to equality or unit growth. Finite-drop existence,
other shapes and elimination of equality are separate open obligations.

Test: one symbolic integer-junction pass, stopping on a cap proof, an
actual counterexample with increment at least 2, or an unresolved sign.
No census, enlarged family, new source search or closed-cycle input.
L002 and Rozier2019's assessed finite affine identity are inputs;
L110 is a method comparison only. The companion source assessment and
Attempt036 were checked; the failed sorting inequality is not reused.
Existing changes and unfinished work are preserved.

## Saved reasoning before canonical write-up

Write A=3^a, C=3^c, P=2^a, Q=2^c, D=2^d. Exact runs give positive
odd u,v with n=Pu-1 and x=T^(a+2)(n)=Qv-1=(Au-1)/4, hence
Au+3=4Qv. The finite affine theorem, applied only to the observed
second segment, gives y=(Cv-1)/D; y has no assumed parity.

The first middle-run minimum gives A/(4P)>=1, hence a>=4.
The last proper prefix and final drop give
2PQD<=AC<4PQD. All other proper prefixes increase along odd runs
or lie earlier in the corresponding decreasing even run. Put
Delta=4PQD-AC>0 and h=y-n in Z. Elimination gives
Delta*u+4QD*h=4QD+3C-4Q. Therefore
h=1+(3C-4Q-Delta*u)/(4QD)
<1+3C/(4QD)<1+3P/A<=43/27<2.
The sought threshold is h<2, so integrality gives h<=1.

This is an adaptation of L110's method, not an application of its b=1
conclusion. No divisibility exclusion, cycle theorem, family expansion
or claim of original mathematics is added. The pass stops at the cap.

## Completion

The full proof and source specialization are canonical in L111.
Outcome ADVANCE / REPRODUCTION records the local cap; independent
critical audit is pending. No unresolved sign remains in the cap
proof, but equality, other shapes and finite-drop existence remain
open. The new audit nomination is REVIEW_REQUIRED; this turn neither
approves nor executes it.
