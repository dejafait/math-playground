# Step583 unfinished exact aggregate repair

Approved target: Certify the stored census579 pi interval by exact rational Machin partial sums and alternating remainders, without rerunning the census, and determine whether this bypasses the failed power-inclusion premise.

Prior SPECIALIZE coverage: `literature/2026-11-05-polya-census-exact-machin-repair.md`.
Read L815's full current proof and step581 qualification, census579 source,
audit581 source, saved pi/checks/hash fields and the recorded power failure.
No census execution. Existing unfinished changes are preserved.

Pending calculation: for q=5,239 set S_q=sum(k=0..119)
(-1)^k/((2k+1)q^(2k+1)), r_q=1/(241q^241). Use A=16S_5-4S_239,
E=16r_5+4r_239 and compare [A-E,A+E] exactly with saved decimal strings.
All arithmetic is integer/Fraction, including finite decimal conversion.
Check original source and certificate hashes against audit581; reconstruct
the historical L815 by removing its marked audit annotation as step581 did.
Save complete rational certificate and comparisons. No generic power repair.

Main gap remains actual-Xi mixed positivity. Success repairs only pi input;
full tails, trig, normalization, grid, whole cells and thirteen exclusions
remain unaudited; [6.5,40], unbounded x, signs and multiple/common zeros open.
On noncontainment retain unsupported status: a conservative enclosure
failure is not a counterexample to the saved pi interval.

Completed: both exact containment inequalities pass. Canonical proof and
qualifications are in L815's step583 annotation; full certificate and code
are `../scripts/polya-census/exact-machin-583.json` and `.py`. The error
radius is <=3*10^-170; endpoint margins are >=1010*10^-50 and919*10^-50.
No downstream exclusion was audited. Reuse the unchanged prior independent
audit assessment for the next mathematical step; no new assessment needed.
