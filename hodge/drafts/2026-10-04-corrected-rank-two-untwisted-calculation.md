# 2026-10-04 — Corrected rank-two untwisted arithmetic

The turn-start SPECIALIZE
[assessment](literature/2026-10-04-corrected-point-rank-two-integrality.md)
covers this unchanged target. No new literature work was needed.
The gap is an actual compatible representative reaching the fourth
NS-fixed RM direction. The intermediate test asks whether L047's
integer corrections can even satisfy rank-two truncation and the
untwisted HRR integer threshold before construction or transport.
An empty arithmetic region would stop these rank-two data; a nonempty
region warrants the already covered product-line index test.

The fixed V' and unchanged-data exclusions do not evaluate this
changed second character. Reused L045's full mixed square 156 and
K3-product Todd class, and imported the assessed rank and character
formulas. For p=4+a,t=4+b, truncation forces ch_3=0 and
ch_4=(pt+78)P/6. Untwisted HRR is integral exactly when 6 divides pt.
The full informal argument is in
[L048](../lemmas/L048-corrected-rank-two-untwisted-euler-region.md).

The surviving region a+b<=-13, 6|(a+4)(b+4) is nonempty:
(-13,0) gives chi=5. The smallest symmetric Bogomolov correction
(-7,-7) fails with chi=21/2; symmetric survivors have a=b congruent
to 2 modulo 6, beginning at (-10,-10), where chi=3.
This is a REPRODUCTION and local numerical ADVANCE. It supplies no
integral K-class, bundle, stable representative or transverse motion.
The known span 21 and three attained directions against four required
are unchanged. Prior stops and unfinished branches are preserved.

Verification command:
`python3 scripts/cubic-kahler/check_corrected_rank_two_untwisted.py`.
The exact script checks the sparse-polynomial identity, all 36 residue
pairs modulo 6 (15 survive), and the three examples. The universal
condition follows from the polynomial congruence, not finite sampling
of the infinite Bogomolov region. The script passed, retaining the
mixed contributions 36+120, verifying the polynomial congruence and
all stated examples. The shared documentation checker
`python3 ../scripts/docs/check_structure.py --problem hodge` passed
with 49 nodes and 108 unique edges. Checkpoint fields are unique;
the next action exactly matches the prior COVERED_TARGET. These
checks verify arithmetic and structure, not existence or transport.
