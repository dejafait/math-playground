# L612 independent finite-family audit — completed with correction

Approved scope: exact TARGET in
`drafts/literature/2026-11-01-l612-saturation-audit.md` (EXPLORE at invocation).
Main gap: actual-Xi all-degree signs at unbounded heights. This audit tests
only the two-count finite-family nonimplication, not Xi realization.

Found a load-bearing exact-formula error in L612: its displayed sum
`d+2d(n-1)+d+min(d,r)` equals `2nd+min(d,r)`, not
`(2n+1)d+min(d,r)`. The old expression overcounts by d for every T.
Retain the old calculation scratch/history as evidence; correct the
canonical statement and proof explicitly after checking the lower bound.

Repair verified: since T=4nd+r, the corrected measure differs from
T/2 by `min(d,r)-r/2`. For 0<=r<=d this is r/2 in [0,d/2];
for d<=r<4d it is d-r/2 in (-d,d/2]. Thus the claimed lower
bound T/2-d and hence T/3 survive, but not by the printed floor-only
argument. This covers r=0, r=d, and r approaching 4d. All count
quantifiers, coordinates and clipping statements were checked before
accepting; the full corrected proof is canonical in L612.

Continuation/abandonment test: retain the obstruction only if both
uniform count constraints and a fixed positive union ratio hold for
every stipulated T, with a correct exact formula. No numerical sampling
or new mathematical script is required for these universal identities.

## Audit result

Accepted the corrected finite-family nonimplication. The old exact
equality is rejected, not treated as harmless notation. The proof's
interior intervals really lie at least 4d from the slab ends; the first
and last clipping contributions are as printed. The two cases for r
recover both the original T/3 lower bound and the asymptotic ratio 1/2.

The density check retains every H whose half-open slab intersects the
model: nonemptiness gives T/2<=H<2T, including H=T/2 and excluding
H=2T. The proof's lattice count and logarithm comparisons are uniform
there. At delta=d the strict right-side count is zero. For delta<d,
the leading density term alone exceeds the lattice count by the stated
constant margin. No fixed-sigma limit was used. The local count counts
both positive-real-part z points and possible lattice points at both
closed endpoints; its bound is uniform in all v>=0. The coordinate
identification was checked against L018, and the restated strict charge
against C464c. Neither result is applied as an actual-Xi theorem to the
model; no direct mathematical DAG input is added.

No new source retrieval was necessary. The saved approval and its earlier
primary-source comparison cover exactly this elementary replay/repair.
Classification REPRODUCTION; outcome ADVANCE is a repair of a real
mathematical error, not an advance beyond known zeta bounds or an
independently new obstruction. Mathlib remains unchecked. PROOF's
existing T/3/model-only summary and the DAG remain mathematically correct
without edits. Historical derivations and unrelated unfinished work are
preserved.

The next proposal examines a materially additional two-point constraint
using the previously identified unconditional Montgomery source. This
audit supplies no compatibility calculation or source approval for it;
the new exact target is REVIEW_REQUIRED. The source's positive-statistic
and horizontal-displacement content must be assessed before any such
mechanism can be called creative or used for actual-Xi signs.
