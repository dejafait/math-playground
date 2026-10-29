# Pair-free capped cover — step 537 result

Outcome: **EXPLORATION**, not a uniform exclusion, a deficient twelve-family,
or a challenge candidate. The invocation-start assessment was
`drafts/literature/2026-10-28-pair-free-envelope-cover-review.md` (EXPLORE).
The pre-run cover justification and counter conventions are preserved in
`drafts/2026-10-28-pair-free-envelope-working.md`; that hashed input is unchanged.

## Actual attempt and exact evidence

The implementation reuses L169's audited ordered-history/envelope/dual
method with **no mandatory support**, starting at the empty history.
It uses all 756 original L109 blocks on
S=(1,8,12,18,22,27,33), J=(47,50,64,70,75,79,85,89,96), characteristic 97,
distinct two-plus-two supports, integer degree <=4 and pairwise intersections
<=1. No pair transport, new domination rule or coding converse was used.

| Quantity | Exact result |
|---|---:|
| Distinct generated deficient spans, including the empty root | 524 |
| Processed separate histories | 102667 |
| Branch nodes | 972 |
| Closed capacity nodes | 101695 |
| Largest bound on a closed node | 11 |
| Required complete-cover bound | 11 |
| Pending histories | 1665 |
| Producer whole-block tests | 498333 |
| Independent verifier whole-block tests | 501667 |
| Combined actual tests / cap | 1000000 / 1000000 |
| Span count / cap | 524 / 10000 |
| Exact twelve-support witness | None found |
| Verification failures | 0 |

The budget stop occurred during the extension scan for the pending history
(0,51,281), span 523; its tested prefix and untested suffix boundary remain
in the certificate. The frontier has 755 length-one, 559 length-two and
351 length-three histories. Thus 755 of 756 root children have not even
been entered. Closed descendants are not a uniform bound. All 1664
not-yet-evaluated child kernels remain explicit obligations; the remaining
frontier state retains its already generated kernel and partial scan.

Processed history lengths 0,1,2,3,4,5,6 have counts
1,1,1,63,14669,44969,42963 respectively. Distinct-span ranks
0,6,11,15,16,18,19,20 have counts 1,1,1,11,14,376,11,109.
These are reached states, not assumptions limiting deficient ranks.
All 180 evaluated zero-increment children remain genuine selected histories;
closure membership never made a support mandatory.

The complete producer certificate is
`scripts/pair-free-envelope/cover.json`; the independent full reconstruction
is `scripts/pair-free-envelope/verification.json`. The verifier imports no
pair-free producer code. It reuses the previously audited independent
polynomial/normalized-quotient construction and elimination from L169's
verifier, reconstructing all original blocks rather than trusting producer
blocks. It checks all 756 rank-six blocks, all 524 entire span kernels and
original nonzero rank minors, every stored extension-prefix entry, and
all 102667 evaluated child kernels. It checks every complete candidate
list, all 2329003 dual column inequalities, exact rational objectives,
integer degrees/linearity, every child obligation and the complete frontier.
The shared test count is independently reconstructed from those actual
operations and equals the reserved count exactly. No failed check or
untested suffix is hidden by a preview. Both paths use Python and exact
integer/residue arithmetic; no proof assistant verification is claimed.

The verifier's matrix products sum at most 21 products of residues at
most 96, bounded by 193536 before reduction; signed 64-bit products do
not overflow. Elimination and incidence/dual arithmetic use Python integers.
Ranks of specified original stacks persist over every extension of F_97
by minors. This does not confer rank, decomposability or coding meaning
on untested stacks. Full matching Mathlib coverage is not checked.

The one attempt was run with `make -C scripts/pair-free-envelope run`;
the completed independent check used
`make -C scripts/pair-free-envelope verify`. The recorded cap includes
that verification; another mathematical replay is not part of this step's
remaining budget. The saved scripts/certificates make the work reviewable.

## Decision and limits

The pair-free complete-cover threshold was **not reached**. The trial gives
checked partial search evidence and a measured implementation bottleneck,
not a new bound, discovery or informative counterexample. Classification
POTENTIALLY_NEW refers only to investigating an instance question not settled
by the checked sources; the generic cover and weak duality are known inputs.
L169 remains an audited fixed-numerical-pair result. C152a's unspecified
pair is not identified, and no challenge conclusion changes.

The existing rank-extrapolation, four-row survivor, equal-pair-rank and marked
extraction failures in ATTEMPTS/041,043,048,055 were inspected before running
and remain intact. This test did not assert any of those failed implications.
The bounded empty-root run is stopped at its cumulative cap, with no counter
restart proposed. A next-turn source comparison for residual-history
domination is a **new, unapproved target**: equal kernels alone do not permit
history merging, as the existing assessment and L169 already warn.
Its proposed purpose is to address the observed 102667-history/524-span
expansion; no valid domination criterion or efficiency improvement was derived.

Even a future uniform bound on this finite partition would still leave
arbitrary representation, decomposability/projection/weight/chart gates,
sixteen-event completion and identification with the exact grand challenge
unresolved. Any coding application retains L104/L086/L010 and all their
finite-field, t=0, nonzero-polynomial and event qualifications.
