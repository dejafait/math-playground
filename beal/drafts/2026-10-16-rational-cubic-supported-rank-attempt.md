# Rational-cubic supported restriction calculation — completed

Approved target: determine the combined rational-dyadic and both
rational-eleven-adic restriction rank on the image in V_S of the full
rational-cubic norm-square supported-unit kernel. Coverage is the saved
SPECIALIZE assessment `drafts/literature/2026-10-16-rational-cubic-supported-pruning.md`.

Main gap: primitive integer emptiness. Intermediate test: combined rank
at least two continues this family as a second-direction source; complete
rank at most one parks it. Uncertified generators decide neither case.
Potential use: contribute to the five removed unit directions needed by
L076, without computing other directions or the localized class kernel.

The completed hand-certificate uses
f(t)=t^3-t^2+t+1, s=t+1, v=-1/t, a=f'(t)/s^2 and b=11/a^2.
The full proof, qualifications and citations are canonical in
[L077](../lemmas/L077-rational-cubic-supported-restriction-rank.md).
It certifies maximality, the complete basis, norm kernel, scalar
transport and combined rank two, meeting the second-direction test.
This is REPRODUCTION using known methods, without a full descent or
integer conclusion; separate critical review remains pending.

The existing ATTEMPTS/032 and ATTEMPTS/033 stop the unfiltered bound and
deleting eleven; this calculation does neither. Essential inputs are
L033, L041, L046, L069–L071, L073–L076. Unresolved obligations
at the start of this target were maximality, full supported generation,
norm kernel, scalar transport and combined rank; L077 supplies them.
Outside this target remain the other D-units, localized class kernel,
other completions and global
point/integer lifting. No cross-notebook input is used.

The first optional arithmetic-backend check found Python's sympy absent.
Small exact rational-polynomial arithmetic replaced that optional backend.
The first certificate also rejected the provisional expectation w in
H2 (20/22 checks); it is preserved as
`scripts/rational-cubic-supported/initial-rank-certificate.json`.
The corrected relation is vw in H2, with both v,w outside H2.
The final certificate has 23/23 checks passing. This changes the dyadic
row to (1,1); the independent eleven-adic row remains (0,1).
