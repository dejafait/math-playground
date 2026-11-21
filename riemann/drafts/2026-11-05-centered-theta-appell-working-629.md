# Step629 — approved centered-factor compatibility attempt

Target and gate: reuse SPECIALIZE in
`drafts/literature/2026-11-05-centered-theta-factor-appell-test.md`.
Main gap: actual-Xi all-degree mixed positivity. Test only the necessary
degree2/3 common-symbol lowering relation; no factor-sign test or sweep.
Nonzero certified defect stops this bridge; equality only passes the prefix.

Inspected L019/L021/L795 definitions, L791 coefficient proof and step478
audit, L778 evaluator/step433 contracts, and the recorded common-Favard,
inverse and automatic-Gram stops. Complete gamma endpoints and step478
checks/failures/inherited error were read; coefficient evidence is being
checked before arithmetic. No use of L823 or L824's mathematical result.

Working algebra, not yet a verified result: put h2=R1/R2, h3=R2/R3.
Center P2/R2 and P3/(-R3) by x=y+h_d. The depressed coefficients should be
u2=1/R2-h2^2, u3=3R1/R3-3h3^2,
v3=-1/R3+3R1*h3/R3-2h3^3. The MSS fixed-degree equations imply the
centered self-convolution factors have nonleading coefficients halved.
Verify every coefficient equation and uniqueness before claiming this.
The proposed derivative defect is the constant (u3-3u2)/2; its interval
has not yet been computed. Preserve original certificates and all work.

Completed: L825 now contains the full specialization and restricted stop;
`scripts/central-jacobi/centered-appell-629.json` certifies the strictly
positive constant defect in (9.582501,9.582502), required zero. All 27
finite checks pass. The algebra and current arithmetic await a separate
audit; inherited contracts remain premises. This note preserves the
pre-calculation checkpoint, not an additional current-status record.
