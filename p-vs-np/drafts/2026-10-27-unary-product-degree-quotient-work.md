# Step 528 — direct right-closed degree quotient

Pre-work checkpoint, 2026-10-27. RESEARCH under the unchanged prior
EXPLORE assessment `drafts/literature/2026-10-26-unary-product-sparse-quotient.md`.
The main gap remains uniform P versus NP; this tests only the unary sector
of the fourth comparison. The intermediate target is the exact checkpoint
target: a scalar FG/GF chain with universal linear support and intermediate
graph size, or a concrete obstruction to its proposed quotient.

Test the direct common remaining-degree chain, without a cut/path table:
states q_0,...,q_n with x edges q_j -> q_(j-1), plus a fresh source with
constant edges encoding the product coefficients. The maps should encode
the right-closed state residuals, with a separate source coordinate.
Check all three oriented equations, not raw constant intertwining. No
dense closure or coefficient-map construction is charged as free.

Discriminating family: F has n consecutive layers, with separate singleton
1 and x edges between each adjacent pair; G is the allowed one-vertex
empty-path graph. Set n=2^k. Independent wrapped products have fixed
denominator S=10n+20. Candidate obstruction: residuals at F vertices are
x(1+x)^r for 0<=r<n; their total coefficient support is 3^k. The graph
quotient may stay linear while the necessary explicit scalar maps do not.
These are work-in-progress formulas, pending the full proof and checks.

Continue this proposal only if both graph and support ledgers have a
universal C; reject this specific degree-coordinate quotient on a proved
unbounded support/S ratio. This would not exclude other scalar bases,
reverse arrows or longer zigzags. L110 fixes recipes and closure; L113
fixes the distinction from raw equations. L112/Attempts 047–048 retain
their narrower obstructions. No actual fixed-job reception is attempted.
Mixed-letter Dcomm, full costs, availability and unrestricted complexity
claims remain independent gaps. No new source review or approval occurs.

Completed: the candidate formulas and every oriented equation are proved
in `lemmas/L114-unary-product-degree-quotient-support-obstruction.md`.
The minimum support, not only one chosen map's support, is 3^k+2 per
arrow. Both maps exist; the intermediate graph stays linear, but total
support/S is unbounded. This is a NEGATIVE for the monomial-degree basis,
not for all closed-only chains. No mathematical script was run. Scoped
search of L110–L113, the unary source-review/raw-obstruction notes and
Attempts 047–048 found no previously recorded version of this particular
support test; no global duplicate or novelty claim follows. The completed
proof imports the prior simulation convention and L110's closure/recipe,
and derives only the assessed proposal's explicit maps and support count.
