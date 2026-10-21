# Fixed minus-three fiber genus: bounded attempt

Gate: reuse `drafts/literature/2026-10-20-global-rational-quadratic-fiber-genus.md`
(SPECIALIZE, saved before this invocation). The exact approved target is
normalization genera of the fixed-field marked locus, not rational points.

Main gap: both L095 integer systems and global factor compatibility remain
unresolved. Target: verify the marked model over Q, its geometric components
and normalization genera. Downstream use: select a rational-point method.
Continue only with full model comparison and exact ramification counts on
at most 1000 labels; otherwise preserve the precise obstruction.

Existing stops: ATTEMPTS/045 is a class-backend park; ATTEMPTS/046-minus-three-
joint-factor-at-seven.md and audited L105 stop local exclusion at seven.
Neither computes global geometry. The ready assessment records the source
comparison and no matching classification; no new literature search is needed.

Working calculation (unverified until the canonical proof and certificate):
use a=w*u? No: set a=u+w*v, b=u-w*v with w^2=-3.
Over Q(w), the coefficient equations become phi(a)=phi(b)=phi(r).
On the distinct-root open this is the ordered triple cover of degree 990.
The derivative suggests passports (5,5,1), (3,1^8), (11).
Check the group and all induced cycles before claiming a genus.

## Completed outcome

The working calculation is superseded by canonical L106, including full
model equivalence, geometric group A_11 and genus 75. The exact certificate
in scripts/global-fiber-genus/certificate.json covers all 990 labels and
passes 857 checks. No unfinished derivation remains in this draft. The
initial scratch notation was corrected before the proof: throughout,
a=u+wv and b=u−wv. The next action is the separate critical audit recorded
in PROGRESS.md. No rational-point or integer exclusion is claimed.
