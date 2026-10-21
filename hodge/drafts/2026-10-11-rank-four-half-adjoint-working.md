# Rank-four half-adjoint attempt — unfinished checkpoint

2026-10-11. Approved target: test L079's conditional stable symmetric
K_4, integral c_1=0,c_2=8, at L052's exact h. Assessment:
drafts/literature/2026-10-11-rank-four-orthogonal-spin-factor-constraints.md.
Inputs read: L079 actual parallel form and real reduction, L052 exact
metric/lattice and determinant-zero stable bound, L061 lifting and
simple twisted-index conventions. Preserve all other image branches.

Working calculation (not yet a canonical verified result): write the
real rank-four Euler class e=t eta and p_1=-8 eta. Associated
half-adjoints A_+,A_- have charges d_+=8-2t,d_-=8+2t. Local Spin(4)
lifts have common central triple cocycle; their rank-two End bundles
are O+A_± and inject into End(K_4). Thus simplicity of K_4 should
imply simplicity of each local/twisted factor. RR then gives individual
self-Ext dimensions (1,2-2t,1),(1,2+2t,1), hence t in {-1,0,1}.
Spin lifts must inherit actual zero-Einstein factor connections and
strict stability; their charges sum to four, contradicting L052's
minimum four on each. Nonspin determinant and twisted alternatives
must be retained and tested separately before claiming any exclusion.

Remaining applicability check: construct global holomorphic parallel
Hodge-star summands and actual local factor connections; show ordinary
lifts are stable with arbitrary determinant; verify cocycle cancellation,
Pontryagin-square signs and compatible examples for each Euler value.
No holomorphic K_4 or common F existence claim is intended.

Completed attempt: the full conditional proof and precise surviving
cases are now canonical in lemmas/L087-rank-four-half-adjoint-lifting-constraints.md.
All applicability obligations above were addressed in that attempt;
independent critical audit is still pending. The numerical witnesses
remain formal. PROGRESS.md records the sole continuation, a separate
source approval for the concrete critical audit, and ATTEMPTS/056
records why this bounded filter does not exclude the branch.
