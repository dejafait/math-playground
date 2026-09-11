# Two-factor short sums checkpoint

Date: 2026-09-14. Draft; no new proved graph input.

Use pair weights P(u)=sum_{ab=u} p(a/N)p(b/N), Q(v) similarly
for q, with a,b in the original integer interval. Then W(k)=sum_{uv=k}
P(u)Q(v). For each m retain L185's exact lower and upper displacement
bounds L_m=max(a−²−m²,−2m rho+rho²),
U_m=min(a+²−m²,2m rho+rho²). Integer v must lie between
ceil((m²+L_m)/u) and floor((m²+U_m)/u), excluding uv=m².
Since u≥N² and U_m−L_m≤4m rho=O(N^(3/2)), there is at most
one such v for large N. This is a residue filter, not cancellation.

Resume: state the exact finite identities, formulate the normalized
weighted cancellation criterion, and verify integer endpoints and excluded
squares using exact rational toy inputs before promoting the reduction.

Completed: L186 proves the finite identities, unique-candidate residue
filter, and equivalence with B_N=o(Nh). Exact rational regression checks
passed. The cancellation estimate itself remains unproved; this checkpoint
is closed.
