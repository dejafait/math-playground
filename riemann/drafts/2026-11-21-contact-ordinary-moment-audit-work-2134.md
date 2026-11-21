# C874c independent audit work, step2134

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-21-contact-ordinary-moment-audit-2132.md`.
Exactly its two S_1=16, degree-seven ordinary witnesses are audited.
Inputs: C874c,C874b,L058,L874. Main gap: L030-L032/C032a.
The original program, full certificate cases/failures, canonical proof,
and prior source coverage have been read; no existing work is discarded.

Plan: independently extract the degree-seven exponential by finite
partitions (without importing the original code), recover its logarithm
by the finite log series, compute all sixteen integer determinants by
fraction-free Bareiss elimination, compare every saved coefficient,
moment, matrix entry and minor, and check the printed canonical tables.
Replay the original program and retain byte-equality evidence. A clean
result validates only the finite restriction stop; any discrepancy
requires retained evidence and a localized correction. Recheck the
nonsingular Curto-Fialkow Thm5.1 hypotheses and square-root pushforward/
cosine logarithm interpretation. Neither m_8/S_8=2, actual theta,
parameter tilts, contact existence nor global closure is covered.

Status: completed. All sixteen minors are strictly positive; every
coefficient, moment, matrix entry and canonical table matches. The
original replay is byte-identical. Primary theorem applicability and
the finite logarithmic germ pass. No discrepancy was found. Complete
reasoning is canonical in C874c; full independent arithmetic is in
`scripts/heat/contact-ordinary-moment-audit-2134.json`. This parks only
the degree-seven exclusion and leaves prescribed S_8 unresolved.
