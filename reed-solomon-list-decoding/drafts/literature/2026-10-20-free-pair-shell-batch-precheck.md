# Free-pair coupled shell batch — proposed first calculation

TARGET: Construct the specified free-pair two-family shells-5–8 SDP batch and test L022/L023's unchanged extension as an exact above-threshold feasibility witness.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed changed-scope comparison and queries are recorded in 2026-10-19-free-pair-coupled-dual-discovery.md; no new mathematical calculation or additional external search is claimed here.
SOURCE_EVIDENCE: Schrijver (2005) III.A (53)–(58), III.B (60)–(67); Kim–Toan arXiv:1212.3467v1 (31)–(35),(40); Boyd–Vandenberghe §5.9.1 and Example 5.11, pp. 264–266; canonical formulas and qualifications in foundations/04, with detailed inspection record in the companion assessment. Direct primary URLs: https://homepages.cwi.nl/~lex/files/codes.pdf ; https://arxiv.org/pdf/1212.3467v1 ; https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf .
COMPARISON: The old common extension is certified for L022/L023/L024's specified constraints, not for all the added shell modes/cross entries. A simultaneous exact pass stops this selected support; failure rejects only that extension and leaves its free-pair optimum unknown.
GAP: Exact source-coefficient construction, shared-orbit closure, resource counts and complete rational feasibility test for this new finite batch; no mathematical witness evaluation has yet occurred.
REASON: One bounded precheck can rule out a global dual support before optimization; all pairs are free in the modeled relaxation and the old extension is only a test point.
SCOPE: The finite support, rows, normalizations and caps in the companion assessment; model construction and one unchanged-witness test only, with no optimization, retuning, block enlargement or stopped solve restart.

The full prescription and known-result comparison are in
[the completed review](2026-10-19-free-pair-coupled-dual-discovery.md),
sections “One finite block and row support” and “Exact certificate and
first discriminating test”. This newly saved ready continuation receives
the supervisor's separate approval handling before a research invocation.

Essential inputs: L001,C001a,C012a,L019,L021,L022,L023; L024 is comparison
evidence, not an additional constraint. Use foundations/04 directly for
both original affine families; L053–L096 fixed-pair/base/column contracts
and Schur inverses are not inputs. Preserve ATTEMPTS/012–018,067,068,071,079.

Main gap: 68-agreement arbitrary-center safety. Intermediate target: the
exact global relaxation model and one whole-support feasibility verdict.
Downstream use, if a later sufficient dual is found: L001/L021's existing
uniform-in-m support transfer. Independent gaps: 67 agreements, global
triple completion, labeled restrictions, RS realization and qualified
ABF/ArkLib comparison. No boundary improvement is assumed.

Save full coefficients, original orbit maps, all retained scalar slacks,
both matrix families and complete rational PSD factors under
scripts/finite-support/ in the future research turn. Report actual and
required objectives, counts, failures and certificate paths. Independently
reconstruct all load-bearing coefficients/signs; previews are insufficient.
Use the shared bounded JSON inspector for selected evidence.

Continue/stop test: an exact common feasible point with floor(M)>K,
K=floor(65537^28/2^128), stops this entire finite support as a sufficient
certificate. Otherwise give a complete violated scalar row or a full
matrix/rational negative vector for this unchanged point. Failure leaves
the free-pair bound open; it permits no automatic solve or new support.
Exceeding 20000 variables or 200000 scalar/pair rows is a resource stop,
and unverified signs are inconclusive. Future classification REPRODUCTION;
full matching Mathlib coverage remains not checked.

## Citation-field recovery — 2026-10-20

Added the direct primary URLs to SOURCE_EVIDENCE here and in the companion
assessment. The target, SPECIALIZE decision, hypotheses, finite support,
resource caps and continuation test are unchanged. This is metadata recovery,
not an additional theorem comparison or mathematical advance.

Access check: the Schrijver author manuscript and Kim–Toan v1 PDF loaded
through the browser today. The Boyd–Vandenberghe PDF returned an internal
browser error; the official book page at
https://web.stanford.edu/~boyd/cvxbook/ loaded and lists the book download.
The existing detailed §5.9.1 inspection recorded in the companion assessment
is reused, not claimed as a fresh PDF reading. This transient retrieval error
does not invalidate that saved coverage. No source hypothesis has changed.

Mathlib: full matching coverage remains not checked. The next task is the
same bounded model construction and unchanged-witness precheck, using the
essential input IDs and unresolved assumptions already specified above.
