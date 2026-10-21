# Five-charge slice working record

2026-10-05. Approved target: Test whether relative direct-image finite-rank identities exclude every L052 survivor with a=-9 and arbitrary integer b.
Prior coverage: drafts/literature/2026-10-05-five-charge-relative-direct-image-slice.md (SPECIALIZE).

Main gap: primitive rational Hodge algebraicity, with compatible global
product-bundle realization as this route's immediate unresolved input.
Target: the whole c_2=5 projected-fibre slice. An exclusion moves prospective
constructions to larger factor charges; compatibility only parks this test.
Continue only with all-fibre concentration, and retain every exceptional
coefficient instead of asserting existence. No other slice is tested.

Inputs read: L044's fixed invariant mixed tensor, L048's full variable
character, L052's coefficient-independent restriction and split lattice,
and L054's fixed-pair application. L053 factor existence is not a premise.
Scoped existing-change inspection found unfinished prior work, all preserved.

Calculation checkpoint: p=-5, t=b+4. L048 gives ch_4=(-5t+78)P/6.
Every projected fibre is stable with h^1=1 by L052, so base change gives
G=R^1 p_2*F of rank one. Relative GRR, with the alternating negative sign,
gives ch(G)=1-(7t+78)eta/6 and ch_1(G)=0. The line identity requires
t=-78/7, equivalently b=-106/7, which is not an integer. In the survivor
residue class b=-10-12j (j>=0), the second character is (14j-6)eta,
never zero. Full proof, source hypotheses and qualifications will be
recorded canonically in L055 before completing this step.

Completed: lemmas/L055-five-charge-relative-direct-image-slice-obstruction.md
now contains the full proof and precise imported theorem hypotheses.
The slice is excluded; no independent larger-charge calculation was made.
