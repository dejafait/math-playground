# Exterior endpoint caps — 2026-09-14

Prior L214 is complete; no interrupted proof was found. Scoped task:
bound the exact positive mass near v=N² and v=4N², both of which
belong to the remaining far exterior eventually.

For v<=N²+D, c,d>=N force c,d<=N+D/N. For
v>=4N²-D, c,d<=2N force c,d>=2N-D/(2N). Hence the
union contains O((D/N+1)²) ordered pairs. L213's uniform
fixed-pair bound is O(Rh/N²); |r|<=1. Candidate bound:
O(Rh(D+N)²/N⁴). With D=N^(7/4)/log N this is o(Nh).

Checkpoint before final proof: check endpoint inequalities for real N,
uniform fixed-pair applicability on the full support, and that these
caps lie beyond B_*=N^(15/8)/log N. The rest of the far exterior
is unproved and no bound on its coprimality distribution is assumed.

Completed: L215 proves the cap bound and eventual inclusion in the far
exterior. The interior remainder specified there is still unproved.
