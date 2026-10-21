# L096 fixed critical audit — working record

Step 375, 2026-10-20. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-Q-relative-P-critical-audit.md`.
The main gap remains arbitrary-curve rank/order equality at analytic
order at least two. This one audit targets L096 on the unchanged curve,
P, Q, prime seven and depth one. Its downstream use is a checked local
relation for possible rational Kummer-kernel work.

The complete L096 proof, producer and verifier, L081 local proof and
L083 local proof/audit have been inspected, together with step 373 and
ATTEMPTS/045. The ready assessment supplies the known-result and
duplicate comparison. No changed source hypothesis calls for browsing.
The full-group argument uses L030/L033/L081 and only L083's local part;
it does not depend on the unreplayed global computations in L034/L082.

Planned finite test: replay all certificate fields and compare the entire
saved verification report with fresh output; independently reconstruct
each valuation from the primitive projective coordinates by integer
division, without using the saved parameter or valuation as an input.
Require all seven valuation results and unit residues to match, all
scalar labels and branch denominators to pass, and every original byte
to be preserved. Stop on any discrepancy without changing the instance.
The script and full exact evidence will be in
`scripts/Q-relative-seven-audit-375/`.

The symbolic audit checks both U/7U -> G/7G containments, [7]U=E_2,
P's exact quotient order, and cancellation of 13. Global nonzero-class
membership, an actual zero-log rational point, uniform production and
the general BSD gap remain unresolved. No order iteration is resumed.

Completed: fresh replay matches the entire original verification report;
23 rows (7 tangent, 14 chord, 2 identity), 91 sequential additions and
all seven candidates pass. Eight independent projective integer checks
give the required valuation vector (1,1,1,1,2,1,1); full divisions and
unit witnesses are saved in `scripts/Q-relative-seven-audit-375/audit.json`.
The complete winning parameter and projective division evidence were
inspected with selected --full JSON pointers. All five inventoried
original files are preserved, and no mathematical failure occurred.
Both directions of the full local quotient comparison and congruence
pass the symbolic audit. The canonical detailed proof is in L096.

This closes the fixed audit, not the global nonzero-class obligation.
The proposed bounded good-prime witness target has a separate
REVIEW_REQUIRED assessment; no computation or proof on that new target
was performed here. PROOF.md and DAG.md are unchanged because the
mathematical assembly and its inputs did not change; L096 and the
checkpoint carry the completed audit status.
