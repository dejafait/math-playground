# Fixed L088 witness as a full included-anchor completion

Step 322, 2026-10-18: [L089](../lemmas/L089-fixed-new-only-witness-fails-mixed-modes.md)
rejects exactly the complete unchanged L088 assignment. Of its 36 omitted
mixed rows, 16 have strictly negative original/raw remainders and 20 have
strictly positive remainders. The retained subsystem and all reconstruction
controls pass. Full fractions and verification are canonical in L089.

WHY IT FAILS: the necessary equality/new-only/sign subsystem did not impose
the mixed rows. Its feasible witness has a negative new diagonal in mode
(7,3), whose old block and cross vector are zero. Hence this entire fixed
assignment is not PSD even though it satisfies L088's necessary subsystem.
This stops that assignment only; it does not exclude another completion
at the same columns or another zero-plane point. No solve, scan, retuning
or revival of the full-row/conic attempts occurs. The separate step-324 critical
review retains this fixed rejection; full evidence is canonical in L089.
The 955–957 RS bracket is unchanged.
