# Heat deformation checkpoint — 2026-09-10

Draft reasoning, not a proved DAG input. Starting tree was clean.

Use Lemmas 19 and 20 only. Bound K by C exp(9u/2-π exp(2u)), with C=8π²(1+11q+11q²+q³)/(1-q)^5 and q=exp(-π), by n²-1≥n-1. For mixed derivative orders a,b and |λ|≤L, |z|≤R the majorant is C u^(2a+b) exp(Lu²+(R+9/2)u-π exp(2u)). Absorb the polynomial using u^p≤p!exp(u), then dominate the quadratic using half of π exp(2u). This proves joint entire dependence and the backward heat equation.

Resume by writing the full domination and analytic implicit-function proof: x'=Fzz/Fz at a simple real zero. Reality follows from conjugation and local uniqueness. The quotient has no sign from K positivity. A polynomial solution F=z²+2(c-λ) exhibits a double collision at λ=c and nonreal roots below c; it is only a counterexample to inference from the PDE alone, not a theta-kernel counterexample. No global zero theorem has been proved or assumed.

Completed in Lemma 58 on 2026-09-10. This draft is retained only as an interrupted-work checkpoint record; the canonical proof is in lemmas/L058-heat-deformation-and-local-zero-motion.md. No unfinished claim from this draft was promoted without proof.
