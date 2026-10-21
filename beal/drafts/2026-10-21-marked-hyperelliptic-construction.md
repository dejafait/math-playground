# Marked hyperelliptic construction — working record

Approved target and prior SPECIALIZE coverage:
`literature/2026-10-21-marked-genus-three-hyperelliptic-model.md`.
Inputs are audited L109–L111. The main gap remains primitive integer
exclusion; this step supplies only a potential point-cover input.

Use slope t=h/(T−2) on h²=3(4−T²), giving
T=2(t²−3)/(t²+3), h=−12t/(t²+3). Substitute in R²=b(T)
and clear the fourth power of t²+3. Require a squarefree degree-eight
polynomial, inverse fields, original u,z,v,W,s and elliptic projection,
and every omitted rational fiber. Check t=0, infinity and t²+3=0;
also rational exceptions F,K,L,rho in the old formulas. No point
search, rank calculation or completeness claim is authorized.

Completed specialization: [L113](../lemmas/L113-marked-genus-three-hyperelliptic-model.md)
contains the full proof, original functions and exceptional charts.
`scripts/pair-genus-two/marked-hyperelliptic-certificate.json` records
31 passing exact checks, with degree/genus/lift thresholds 8/8, 3/3,
2/2 and no failures. The initial erroneous expected remainder check is
preserved separately and explained in L113. This is local reproduction
of assessed methods, not progress beyond the checked sources.

Unfinished L108 and ATTEMPTS/050–051 are preserved. Independent critical
audit, descent arithmetic, surviving-cover points, root recovery and both
integer systems remain unresolved. The sole current continuation is in
PROGRESS.md; this working record does not approve further mathematics.
