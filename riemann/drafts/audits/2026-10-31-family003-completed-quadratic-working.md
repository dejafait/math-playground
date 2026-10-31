# Completed quadratic reduction — working audit

2026-10-31. Approved target: the conditional implication from the pinned
`eq:quadratic-large-sieve` to `eq:completed-quadratic-reduction`, under
fixed source S containing primes above 6. The saved assessment is
`drafts/literature/2026-10-31-family003-completed-quadratic-primitive-audit.md`.

Main gap: actual-Xi all-degree positivity. This audit could discharge
L542 Hypothesis 1 in the source setting, while independent base-sieve
specialization, the cubic primitive, reflection and global/sign closure
remain unresolved. L542 and L541 are downstream, never premises.

Inspected the primary TeX at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, lines 519–588 and
2480–2626, via the direct URL in the assessment. Reused the completed
Goldmakher–Louvel comparison. Relevant family003 notes/history and
failure searches disclose no completed matching primitive audit.

Partial reasoning, not yet a completed proof: first separate t by
Hilbert-space Cauchy, then expand the entire (k,c) mask over r|(k,c).
After k=rk' and c=rc', (k',r t)=1 is a fixed row restriction; there is
no remaining (k',c') condition. Separate only the squarefree S-parts of
m,h and group their good parts by j. Preserve c' and the reconstructed
original coefficient support. The remaining checks are coefficient
independence, multiplicity at most O_delta((KNB)^delta C/q_r), and
normalization of the two sieve lengths on nonempty ranges. In particular
positive subunit centers can contain units and cannot simply be deleted.

Continue only with the exact T and (K/q_r+NG/C^2)C/q_r weights, no
extra power and constants depending only on fixed datum/comparisons and
epsilon. Narrow or stop on an unsupported mask, row-dependent coefficient,
uncontrolled S dependence or failed nonempty-range comparison. No script
or numerical experiment is needed for these finite identities.

Completed: the full conditional proof is now canonical in
[L543](../../lemmas/L543-conditional-completed-quadratic-reduction-audit.md).
All three small losses are explicit; no additional power or support mask
is needed. The base family specialization remains outside this audit.
