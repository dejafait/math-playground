# Fixed-span 11-adic attempt — working record

Started 2026-10-26 under the prior SPECIALIZE assessment
`drafts/literature/2026-10-26-pair-eleven-adic-filter.md`.
The approved target is one extra local codimension on L140's real-compatible
span of exactly 39 witnesses, with no enlarged search.

Main gap: residual primitive Beal signatures. Intermediate target: a
positive quotient rank after the complete 11-adic Jacobian image is
certified. Downstream use: a smaller genus-two rank upper bound for possible
point control, leaving every lifting and other-signature gap unresolved.

Inputs to bind: L135's g and basis, L136 accepted ideal records, L137's
prime (11,alpha+5) and support, L138's actual G,H,eta, L139's norm kernel,
and audited L140's 39 witness records and W. No cross-notebook inputs.

First gate: certify g(U-5) Eisenstein at 11, the specified uniformizer,
full local factorization and the single rational branch-divisor image.
Require that image to span dimension m-1 from Stoll Lemma 4.4. Stop if
this gate fails. Otherwise use exact valuation and normalized-unit residue
bits in both product coordinates and coefficient-space elimination subject
to all assessment caps. Zero quotient rank stops only this fixed-span test.
No exclusion or rank improvement was asserted at that unfinished checkpoint.

## Completed result

The fixed field and branch gates succeed. Complete proof and qualifications
are canonical in L141. The complete local image has dimension one;
the 39-column real coefficient map has rank two and kernel dimension 37;
all 37 basis products were reconstructed and their local quotient has
rank one. The decisive product is the saved rational-2 column alone,
([1/16],[2]), with real mask zero and local mask eight, outside local
image masks {0,5}. The combined rank upper bound is 7+c<=9, eight above
the sufficient bound one. This is a specialization of known theory.

Producer and independent replay certificates are
`scripts/pair-genus-two/eleven-adic-filter-certificate.json` and
`scripts/pair-genus-two/eleven-adic-filter-verification.json`.
Replay passes 12335 checks after adding explicit source-coordinate bit
checks (the initial replay passed 12079). No mathematical failure or
assessment cap occurred.
The exact real and 11-adic norm quotients are fully detected, so stop
adding witnesses for these same restrictions. Proceed to separate critical
audit only after its new scope receives the required literature approval.
No Beal candidate is asserted; all other gaps remain.
