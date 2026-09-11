# Gcd residue split checkpoint — 2026-09-14

Use L186. Write m=gt, u=gs, (t,s)=1 and r=g ell.
Then sv=gt²+ell, with exact bounds L_m/g≤ell≤U_m/g,
ell≠0, and ell≡−gt² (mod s). Necessarily
(ell,s)=(g,s). Preserve P(gs)Q(v)H_m(g ell).

Planned bound: for each fixed m and divisor g of m, there are
O(N^(3/2)/g) possible nonzero displacements (zero excluded),
and each m²+r has O_epsilon(N^epsilon) ordered quadruple
representations. Summing g≥G gives O_epsilon(h N^(3/2+epsilon)/G).
This only removes large gcds; it gives no saving for g=1.

Checkpoint: verify the nonzero-integer count without a +1 loss,
write the exact identity and sector bound, and test finite signed sums.
Claims above are draft until checked in the canonical lemma.

Completed: L187 proves the exact split and uniform large-gcd bound.
The exclusion of r=0 removes the additive counting loss. The whole-sum
bound remains unchanged; no small-gcd decay was proved. Finite verification
is in scripts/heat/check_gcd_residue_split.py. No unfinished claim from
this checkpoint is used as an input.
