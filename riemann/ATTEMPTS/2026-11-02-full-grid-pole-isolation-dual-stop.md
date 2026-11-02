# Full-grid polewise polynomial dual — separation-cost stop

The completed proof and exact qualifications are canonical in
[L650](../lemmas/L650-full-grid-pole-isolation-dual-cost.md).
It tests C645y's complete identity with the actual multiplicity
polynomial and identifies its retained component with L649's kappa.
The certificate chooses and scalar-normalizes one pole-isolating dual
at each angle; no initial grid prefix or fractional residue is used.

WHY IT FAILS: On the admissible pair x and x+i*2^(-n), separate
dual norms grow like the reciprocal separation. Their exact normalized
responses are at most (217/55)R^(-n), missing the required squared rate
1/16 even relative to the anchor diagonal. Their sum cancels the large
terms and has norm one, giving a positive full retained-energy bound
on the same pair. Thus this is a stop for separate pole isolation only;
it is not a counterexample to joint duals, the full angular target or RH.

The exact finite normalization evidence is
`scripts/one-sided-hankel/full-grid-pole-dual-check.json`: 126 checks
passed at six rational cases. Uniform claims come from L650's proof,
which remains separately unaudited. The proposed joint-space comparison
has a REVIEW_REQUIRED assessment; no approval is inferred from this stop.
