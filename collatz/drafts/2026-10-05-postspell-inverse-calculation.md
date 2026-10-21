# Guarded postspell inverse attempt — completed

The unchanged EXPLORE assessment is
`drafts/literature/2026-10-05-postspell-extendible-inverse-rigidity.md`.
The gap is universal eventual descent. The approved intermediate test is
uniqueness of positive extendible postspell predecessors at odd
residue-20 endpoints. Rigidity might constrain growing survivors but
would leave fixed-start escape, entry and compensation unresolved.

Use L020/L021's positive offsets and imported finite coding; preserve
all unfinished work. For each two-word label in the approved 25-by-25
alphabet, code the concatenation with one extra O guard at its endpoint.
If D is the concatenation length, A its multiplier, and p0 its least
positive CRT root, all roots are p0+27*2^(D+1)*k for k>=0.
Their endpoints are m0+54*A*k. Thus compare the exact endpoint classes,
retaining the lower bound m>=m0, rather than scan bounded integers.

Compare distinct final predecessors, not labels. One common endpoint
with two distinct positive intermediates and complete actual replays
stops uniqueness. If no collision occurs, the finite screen alone is
EXPLORATION; do not enlarge the rectangle without a new mechanism.
No least-root filters are part of this target. Any negative result here
refutes this decoder, not the Collatz conjecture.

The complete screen in `scripts/postspell-inverse/result.json` finds
1,250 compatible unordered pairs among 195,000 comparisons; none has
different final words. All 1,250 class replays pass. This finite result
alone would be EXPLORATION.

The screen suggested an exact obstruction, proved in
[L023](../lemmas/L023-postspell-extendible-inverse-rigidity.md): a
residue-20 endpoint of an actual OOEO block cannot also be the endpoint
of an allowed preceding postspell word. The final endpoint's valuation
fixes H, and injectivity then reduces unequal J values to that
obstruction. Thus uniqueness holds for the full unbounded alphabet.
This is a local ADVANCE classified POTENTIALLY_NEW relative to the
bounded source comparison, not a certified novelty claim.

No collision certificate is present because no collision was found.
The canonical all-parameter proof, rather than this preview or a finite
screen, establishes the theorem. No fixed-start escape estimate has
been derived. Any use of the new decoder to replace the stopped
repeated-minimum transfer needs a separately assessed target.
