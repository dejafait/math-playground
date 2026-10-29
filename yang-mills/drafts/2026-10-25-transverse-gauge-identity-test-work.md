# Direct finite-domain gauge-identity test — work checkpoint

STEP_ID: YM-20261025-491-transverse-gauge-identity-test

The unchanged, previously saved EXPLORE assessment is
`literature/2026-10-25-transverse-complete-coefficient-log-growth.md`.
The supplied overview/DAG and assessment were used without rereading.
Inspected L280's chart, orbit derivative, full density and complete
signed coefficient; L279's exact jets and Gaussian source formula;
L003's relative domains, modes and positive Gaussian limit; and
ATTEMPTS/047–048. Existing unfinished changes are preserved.

Main gap: interacting continuum construction and finite positive mass.
The approved intermediate target is the complete logarithmic bound,
which could control the first correction to L003's positive coefficient.
Continue only if direct finite-domain identities control a complete
signed transverse family; longitudinal constraints alone fail the test.

Work in progress: apply the exact orbit derivative to the source-weighted
phase through fourth degree, with all normal-edge rows. Test whether
these identities constrain the transverse quartic contribution after
both source derivatives and the full density are kept. A gauge-invariant
comparison phase `Phi_{s,t}+lambda S^2`, lambda>=0, is a diagnostic
of what gauge identities alone imply, not a replacement target action.
It has the same Hessian, cubic jets, insertion jets and density, but
adds lambda S_2^2 to the quartic term. Check its complete mixed response
before deciding whether this produces a rigorous limitation of the
proposed identity mechanism. The comparison is nonlocal, so it cannot
refute a Wilson-specific locality estimate.

No new external theorem, script, source assessment, lemma ID or DAG
input is invoked. Full checked reasoning will be saved in L280 if the
diagnostic is completed; the logarithmic bound remains unresolved.

Completion: [L280 section 8](../lemmas/L280-local-relative-coulomb-source-coefficient.md)
contains the full orbit hierarchy, measure identity and diagnostic.
The comparison changes the complete mixed coefficient by
`-lambda [Tr(P_-)Tr(P_+)/2+(dim H+3)Tr(P_-P_+)]`, with a lower
bound of order N^4 on its magnitude, while all gauge identities and
the entire density persist. The nonlocal comparison disproves only
the inference from gauge identities alone. It does not test a replacement
action as a Yang–Mills construction or refute the actual Wilson bound.
Outcome NEGATIVE; classify the completed work as REPRODUCTION of the
finite Ward/Wick methods, without a claim of mathematical novelty.
Stop this mechanism after its second attempt. The new kernel-asymptotic
target is registered separately as REVIEW_REQUIRED; no work on its
mathematics has been undertaken. No exploration budget reset is claimed.

Validation: the scoped documentation checker passed with 291 nodes,
1732 unique edges and an acyclic, complete graph. Scoped diff whitespace
checks passed. The new diagnostic uses only the existing L003/L279
inputs of L280; no DAG edge or main-argument edit is required.
