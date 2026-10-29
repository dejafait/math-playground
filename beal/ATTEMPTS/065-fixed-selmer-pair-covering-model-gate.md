# Fixed Selmer pair: raw covering-model gate

2026-10-28. The exact approved target is the fixed-witness Cassels–Tate
test in `drafts/literature/2026-10-28-pair-cassels-tate-test.md`.
L147 supplies complete 3/5-adic images, the derived rank bound <=4
(pending separate critical audit), and one certified independent pair
with masks 165,132102. It does not supply a pairing value.

The raw-form construction and full bounded evidence are preserved in
`drafts/2026-10-28-cassels-tate-membership-attempt.md` and
`scripts/pair-genus-two/pair-cover-gate-certificate.json`; its independent
replay is `scripts/pair-genus-two/pair-cover-gate-verification.json`.

WHY IT FAILS: in the chosen product basis, all 7448 primitive projective
vectors of height at most two fail the isotropy test for each of the three
required raw forms. Thus no dimension-three rational isotropic plane or
determinant-compatible standard model was certified. This is a bounded
construction failure, not a rational nonexistence theorem; no assertion
of an obstruction to Fisher–Yan or to larger-coordinate solutions is
made. Candidate class transport remains separately unaudited. The Kummer
point and pairing evaluation gates were not reached. Do not renew this
same box or backend route without a materially different construction
and a discriminating test. The immediate independent task is critical
review of the completed local theorem, not another search expansion.
