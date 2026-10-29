# Bounded enumeration reduction — working checkpoint

Approved target and scope: `drafts/literature/2026-10-24-labeled-count-enumeration-reduction.md`.
Inputs read: L020, C001a, foundations/02; the saved count source comparison
and ATTEMPTS/010. No cross-notebook input. Preserve prior unfinished work.

Candidate mechanism: the pair image is injective by its monic root
polynomial. On p=u*s+v, incidence means (a-u)(b-u)=u^2+v.
For v!=-u^2 this is a matching; for v=-u^2 every edge contains u,
so there are no disjoint triples. Vertical sum lines are matchings too.
Scale endpoints by h in H: (u,v) maps to (h*u,h^2*v). Nonzero
slopes have 64 H-cosets, each of size 1024, with trivial line stabilizer.
Handle slope zero and vertical lines directly, without orbit division.

Proposed exact formula: vertical falling-third sums + horizontal
falling-third sums + 1024 times the sum over 64 slope representatives
and all nonstar intercepts. Each histogram uses the 523776 unordered
pairs, suggesting fewer than 35 million pair-bin updates and modest
packed-array storage. Pending: complete multiplicity proof, explicit
antipodal cases, operation/storage accounting and exhaustive small-field
cross-checks. No full-H count or safety transfer claimed.

Completed in this step: all pending reduction obligations above are written
in canonical L122, with the four exhaustive small-field checks and resource
certificate in `scripts/finite-support/l122-enumeration-reduction-check.json`.
This working checkpoint is preserved as scratch history; L122 supersedes
its tentative assertions. The full-H count and safety transfer remain open.
