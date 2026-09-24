# Bounded-domain height checkpoint — 2026-09-11

Proposed statement, not yet promoted: for a bounded open set Ω with f nonzero on its boundary and positive maximum zero height B inside, the forward maximum height has right derivative max over the finitely many initial top zeros of 2 Im(h'/h). For simple zeros this is Im(f''/f'); for multiple zeros use L127. If B is also the global upper zero height, L066 and L127 bound each rate by −m/B−mB/(a²+B²).

Proof audit to finish: choose disjoint closed isolating discs inside Ω around every initial zero, not only the top zeros. The compact remainder of closure Ω is zero-free, so compact parameter continuity rules out incoming/new zeros there. Rouché preserves each disc count. Lower discs can be chosen below B minus a fixed positive gap; at least one top cluster remains near B. On top clusters use the finite uniform O(t^(3/2)) expansions (simple branches have O(t²)). The maximum of finitely many expansions yields the claimed derivative. No global exhaustion or uniform-in-radius time interval follows.

Resume here: verify boundary isolation and lower-cluster exclusion, then store the final lemma and its graph edges. No failed approach is asserted.

Completed audit: all initial zeros are finite in closure Ω; after selecting every isolating disc the compact complement has a positive minimum modulus. This excludes incoming zeros and lower clusters. The finite maximum estimate and conditional multiplicity sign are now proved in L128. This draft is retained as a checkpoint record, not an additional current next-action record.
