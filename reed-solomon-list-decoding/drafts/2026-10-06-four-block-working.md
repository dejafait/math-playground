# Fixed four-block diagnostic — work in progress

Gate-approved target: test every actual ordered L022-extension orbit with
sum of independently complemented four-block weights at most 10, using
only the fixed Proposition 22/25 recursion. Prior assessment:
`drafts/literature/2026-10-06-four-block-small-residual-test.md` (SPECIALIZE).

Inputs: L022's unchanged pair values and assignment, L023's full scalar
supplement, and foundations/04's Theorem 12 normalization. L024 records
the independent mixed-block stop, not an input to the new coefficients.
The main gap is arbitrary-center safety at 68 agreements. A negative
exact slack excludes only this extension; a complete pass parks this
diagnostic without widening the cap. No full-SDP or list conclusion follows.

Before implementation, justify the cited appendix properties. Independent
block complementation is a Hamming isometry and zero-weight blocks are
fixed zero coordinates, so removal preserves every distance. For total
weight S<5, two words have distance at most 2S<10, so the maximum is 1
(a permitted word exists). At S=5, two distinct words must have disjoint
supports: distance is 10 minus twice their common-support size. Thus any
positive block (u,n) allows at most floor(n/u) words; simultaneously
choosing that many disjoint u-subsets in every block attains their minimum.
For S>5, sum the incidences of ones in any positive block over a code of
size M: there are M*u incidences over n positions. Words with a one at
one fixed position shorten injectively, with all pair distances unchanged,
to the child parameters (u-1,n-1). Therefore M*u<=n*T(child).
Induction and integrality give floor(n*R(child)/u); taking the minimum
over all positive blocks remains an upper bound. Normalization does not
increase total weight; here a normalized child actually loses exactly one
unit, so the selected recursion has at most five shortening levels.

The source omits appendix proofs; the preceding applicability argument
is required to certify the implementation, not claimed as a new bound.
Completed: canonical proof and qualifications are in L025. Generator and
independent audit retain every selected original row and all recursion
branches; all 12768 rows pass with minimum slack zero. The fixed diagnostic
is parked under ATTEMPTS/016. Full certificates are
`scripts/finite-support/four-block-results.json` and
`scripts/finite-support/four-block-audit-results.json`. No widening,
assignment tuning or full-SDP inference was performed.
