# Sharp postspell final-halving criterion: pending assessment

TARGET: Derive a sharp affine criterion for original-root descent after an actual residue-20 prefix (OOEO)^J O^H E^a with J>=2, H>=3, a congruent to 2 modulo 18 and a<e(J,H), and test whether such guarded excursions exist, retaining every integer and parity guard.
CHECKED: 2026-10-04
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: No target-specific search or theorem-level comparison for the lowered final-halving threshold has been performed; the prior adequate assessment is reused for the imported sufficient threshold only.
SOURCE_EVIDENCE: The prior assessment read Sodelin, Postspell_Guarded_Root_Descent.md, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, sections 1–3, on 2026-10-04; its guarded margin assumes a>=J+H, and no matching sharp criterion below that hypothesis has been assessed.
COMPARISON: L019 imports the sufficient threshold e(J,H), the least integer >=J+H congruent to 2 modulo 18; the new action lowers that exponent, so target membership remains relevant but the existing margin theorem does not cover its changed size hypothesis.
GAP: Whether a sharp guarded criterion excludes additional least-root prefixes below the imported threshold is unscreened; universal prefix entry, the remaining failed guards and convergence are still missing.
REASON: An exponent congruent to 2 modulo 18 below e(J,H) is below J+H, changing an essential hypothesis of the cited theorem; compare exact affine-word descent results and the inspected source before a separate calculation turn.

This is a pending record created at the end of step 027, not a new
literature review or permission to calculate this target in that step.
The ready assessment
[for the imported sufficient guard](2026-10-04-residue47-bounded-ancestor-cover.md)
is preserved unchanged. No new mathematical statement about a lower
threshold is asserted.

The closest inspected input is Sodelin,
[*Guarded root descent after independently unbounded return spells and odd runs*, sections 1–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md#1-uniform-original-root-margin).
The earlier review explicitly described its threshold as sufficient,
not optimal. That qualification is a reason to compare a changed
hypothesis, not evidence that the sharpening is new or even useful.
The source's failed-guard discussion and the known actual affine-word
arithmetic also need comparison at the precise lowered threshold.

The possible downstream use is a stricter necessary final-valuation
bound for some least-root prefix parameters. A discriminating test
would be an actual guarded excursion with a<e ending below its own
root, together with an exact criterion retaining positive offsets and
all parities. If the cited sources already supply the criterion, import
it rather than reproduce it. If no actual improvement is possible,
stop this sharpening. Neither outcome would settle the unproved
entry and insufficient-halving cases or reopen a fixed-depth ancestor
cover. No mathematical or literature exploration counter is changed
by this pending record.

## Mathlib

Full sharp postspell criterion and supporting affine-word arithmetic:
**not checked**. No library absence, theorem match or novelty is
asserted.
