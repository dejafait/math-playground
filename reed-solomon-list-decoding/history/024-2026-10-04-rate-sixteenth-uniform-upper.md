# 2026-10-04 — Rate-1/16 uniform two-coefficient upper application

Completed one mathematical attempt on the saved SPECIALIZE-ready target,
reusing its adequate source coverage without new literature work. The
gap was whether the rate-1/16 two-coefficient center family could supply
an unsafe witness at 66 agreements after its averaging lower certificate
missed the threshold. The continuation test was a uniform upper estimate
at most the actual ambient 65537^28/2^128.

[L014](../lemmas/L014-rate-sixteenth-uniform-two-moment-upper.md) imports
the inspected monomial character estimate and weighted sieve. Deleting
zero costs one character term; every cycle length is below characteristic,
so all nontrivial Fourier pairs retain the bound 514. The resulting
unordered error is at most (1-65537^-2)binomial(579,66). The entire
center-list correspondence from L013 transfers the bound to every m>=1
over the ambient extension, with no exponent m.

The uniform integer list upper bound is below 2^317, whereas the ambient
threshold exceeds 2^320. Its ratio to that threshold is between 0.11256
and 0.11257, by exact rational comparisons. Thus every assessed center
in this family is below threshold at A=66. This stops that witness family
but proves no worst-case code safety; t_star<=958 remains unchanged.
All earlier unsafe certificates and the averaging failure are preserved.
The full proof and
[exact certificate](../scripts/coefficient-fibers/uniform-upper-results.json)
replace neither the unknown largest fiber nor the maximum over centers
with empirical estimates. No 1024-point subset fiber was enumerated.

Outcome: ADVANCE, a relevant local uniform upper input; STEP_KIND: RESEARCH;
classification: REPRODUCTION. This applies known tools, with no claim of
progress beyond the checked literature. Exploration turns used remain
0/3. No complete candidate appeared; STATUS remains IN_PROGRESS. Arbitrary
centers, sharp boundaries, the general differential cover and the ABF26
comparison remain missing.

The next direction retains A=66 and changes the center degree to 67,
allowing a residual linear factor. This is a concrete intermediate family
toward the arbitrary-center gap, distinct from the excluded degree-66
maximal-root family. Its
[pending assessment](../drafts/literature/2026-10-04-degree-sixty-seven-linear-cofactor.md)
is REVIEW_REQUIRED because the changed partial-agreement constraints
are outside the prior scope. No mathematics or new source review on that
target was performed here. Parked source blockers remain parked.

Exact-arithmetic verification passed, including the integer bound and an
independent rational square-root estimate. On a small subgroup, an exact
group-algebra sieve agrees with direct distinct-tuple and subset counts
at every moment pair, checking cycle signs, multiplicities and A!.
The ID-only DAG adds only L014's genuine use of L013; the narrative
overview records the family bound and its remaining limitation.

The required command
`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with 16 nodes and 15 edges; `git diff --check -- .` passed.
Unique completed-step fields, the prior ready assessment, classification
and exact pending-target match passed. The checkpoint has 14 lines and
the overview 100. Structural checks do not validate the cited theorems
or mathematical correctness. Only active-notebook files were edited;
existing unfinished work and all parked failures were preserved.
