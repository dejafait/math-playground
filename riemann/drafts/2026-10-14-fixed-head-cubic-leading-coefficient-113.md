# Fixed-head cubic leading coefficient — step 113 completion record

Prior ready assessment: `literature/2026-10-14-fixed-head-cubic-leading-coefficient.md`.
The approved target is the fixed-N coefficient of audited L407 (9) at
H(log H)^2, including every rational twist and analytic weight.

Main gap: global actual-theta mixed positivity. Downstream use: settle
whether this cubic scale can support a later signed statistic; full tails,
clipping, total pencil margin and common-zero counts remain independent.
Continue only with complete o(H(log H)^2) errors; otherwise preserve the
precise failed obligation without claiming an asymptotic. Zero is allowed.

Input/duplicate check: L407 (3)–(9) and its step-111 audit; L391's
ordinary jets/polygamma bounds; the saved step-112 primary comparison.
L394/L399/L400 are different-weight stops, not inputs or a ban. Existing
unfinished notebook files remain intact. No unproved Bui theorem is used.

Initial saved plan (before the calculation): use the finite Hurwitz identity to
extract the highest Laurent coefficient after the three ordinary
derivatives, replace each exact weight by its uniform leading coefficient,
apply smooth Mellin inversion then absolute unsigned boundary control,
and assemble the complete cubic polynomial. The zero-carrier resonances
are retained and estimated at their own scale. Any auxiliary certificate
checks finite algebra only; analytic assertions require written proofs.

Completed RESEARCH / REPRODUCTION / calculation; ADVANCE records the
local fixed-N specialization in
[L408](../lemmas/L408-fixed-head-cubic-positive-leading-coefficient.md).
The full pole/weight/sharp-boundary proof and qualifications are canonical
there. The coefficient is positive with signed jet factor 17/20160 and
positive complete residue-class factors A_u; all zero-carrier resonances
are O_N(H). The achieved error is o_N(H(log H)^2), with N fixed.

The exact verifier passed seven checks. Its complete signed terms,
polynomial, empty residual and tests were inspected in
`scripts/discriminant/cubic-leading-coefficient-certificate.json`.
These verify finite algebra only. No new mathematical input beyond the
inspected source tools is asserted; the local assembly has not yet had
its separate critical audit. The proposed audit coverage is recorded
as REVIEW_REQUIRED for a separate turn. Full tails and clipping remain
outside this completed target; no RH candidate is obtained.
