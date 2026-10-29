# Full-H implementation checkpoint

Approved target: implement and certify the full-H ordered disjoint-pair
collinearity count using L122, with all star, vertical and antipodal cases
and both unexcluded incidence moments. Prior SPECIALIZE assessment:
`drafts/literature/2026-10-25-l122-full-count-implementation.md`.

Main gap remains arbitrary-center 67/68 safety. The intermediate count is
a whole-domain density diagnostic for L020, not a uniform core/link bound
or a threshold-saving transfer. Inputs read: L122 in full, L020's predicate
and examples, C001a, foundations/02, ATTEMPTS/010; targeted prior count and
failure coverage reused. No cross-notebook input or L121 work is used.

Implementation plan: packed uint32 pair coordinates and one histogram;
save every full histogram to a little-endian uint32 artifact with offsets,
digests and exact line-class subtotals in JSON. Independently regenerate H
as all roots of X^1024=1, recover cosets by power signatures, and histogram
all ordered endpoint products (a-u)(b-u), removing equal endpoints and
halving, then translate intercepts. Compare every saved bin, not a sample.

Continue only with complete equality, exceptional occupancies, matching
bounds, explicit L122 contributions and both moment identities passing.
Preserve and repair failures or stop. Mathematical classification is
REPRODUCTION. Actual count and replay are pending; no number is assumed.

Completed: canonical C122a records T=2298250371072. Production and independent
replay matched every one of 4325442 bins and both unexcluded moments, with
no failures. Complete arrays and subtotals are saved in the named l122-full-
count artifacts. This scratch plan is superseded by the canonical result;
its proposed critical audit still needs separate scope approval.
