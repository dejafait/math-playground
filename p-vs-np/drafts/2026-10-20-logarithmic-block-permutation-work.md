# Step 357 — logarithmic block permutation proof work

Authorized target: the unchanged TARGET in
`drafts/literature/2026-10-19-logarithmic-block-permutation-witness.md`,
saved EXPLORE before this invocation. This is RESEARCH / proof_attempt /
POTENTIALLY_NEW, with no originality certification. The supplied overview,
DAG and assessment have been read; relevant canonical components are
L026, L035, L071 (post-compilation only), L087 and audited L091.
Attempts 018/030 are preserved. No new external source is needed.

The main gap is unrestricted SAT decision/separation. The intermediate
target may extend the restricted W₂ supplier to a growing number of
order discontinuities. Arbitrary-order W₂, ER-data availability and SAT
transfer remain independent gaps. Continue only with both original-fg
formal identities and a uniform original-M full-bit/time/path bound;
an M^{Theta(b)} estimate or a factor-order failure stops this mechanism.

## Interruption checkpoint, before the all-size argument

Proposed test: enumerate all internal block-boundary states of each
original diagram, at most 3^{b-1} choices per diagram. For each pair of
choices the original term is a product of 2b x-only block factors.
Stable sorting by D's block order should use at most (2b choose 2)
adjacent exchanges. Each exchange is corrected additively by L035,
with independently copied current x-only surrounding factors; do not
pass a prior witness to L035. Then replace each neighboring same-block
factor pair by its synchronous P using L026/L071, again additively.
The proposed residual is a sum of ordered products P_1...P_b; prove its
ordered-multilinear membership and Boolean agreement with original fg
before using injectivity. Count every context copy, local block,
dictionary and construction operation. No conclusion or bound is yet
asserted in this interruption checkpoint. Full proof will be canonical.

## Completed proof attempt

The full all-size argument and hypotheses are now canonical in L092.
It uses all cut-state tuples, stable additive original-only exchanges
and additive synchronous block corrections; a single ordered residual
is zero by the existing injectivity input. The proved informal ledger
is K 9^b(M+b+2)^12≤K'(M+2)^16 bits, O((M+2)^48) bit time and
pre-substitution path degree ≤2q+1. No script or implementation is
claimed. This meets the approved discriminating threshold and is an
ADVANCE locally, without certified originality. A separate audit is
proposed with REVIEW_REQUIRED coverage; no audit verdict is asserted.
