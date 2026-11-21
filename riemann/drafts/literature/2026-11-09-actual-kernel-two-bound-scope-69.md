# Actual-kernel upper bound for direct-density error propagation

TARGET: Establish 0<K(u)<=2 for all u>=0 for L019's actual kernel, to sharpen L944's fixed-degree direct-density error bounds.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact kernel-maximum/decrease searches and notebook-local duplicate checks located Csordas v2 Theorem4.1(v), the existing coordinate identity in L605, and L826(8) with its step636 independent endpoint audit; no novelty claim.
SOURCE_EVIDENCE: Csordas, arXiv:1309.0055v2 (21 February2014), equation(4.2) and full Theorem4.1(i)-(v), printed p10, directly read in the PDF; L826 proof of(6)-(8) and independent step636 arithmetic audit read for the existing K(0)<2 input.
COMPARISON: Known strict theta-kernel decrease covers the global shape premise in the exact L605 normalization; L826 already supplies the required endpoint enclosure. The remaining work is a short applicability assembly, not a new maximum theorem or fresh numerical calculation.
GAP: A later research step must explicitly assemble the exact coordinate scaling, positive-half-line decrease and zero-endpoint bound; no density-error propagation or crossing certificate is approved by this assessment.
REASON: Missing coverage is resolved by an inspected named theorem and a recorded audited local endpoint result; repeating either proof or its numerical calculation would duplicate existing work.

## Original nomination context (superseded coverage status)

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Proposed downstream use: reduce L944's product constants using the
same degree256 polynomial. A bound on K does not by itself supply
all required derivative signs or any RH conclusion. Essential inputs
are L019's exact normalization, L938's existing K<7 argument and
L944(1)-(3). No cross-notebook input is requested.

Continuation test: locate an applicable primary result, or approve
one bounded elementary proof test for the exact constant2. Abandon
this constant if a rigorous actual value exceeds2; leave dependent
crossing work parked if essential source coverage remains blocked.
This nomination does not approve or derive the bound. Full/supporting
Mathlib coverage is unchecked, not asserted absent.

## Completed source comparison, step70

LITERATURE_REASON: The nominated constant2 changes the previous direct-density scope; the essential global shape theorem and exact numerical normalization had not been compared for this target.
SCOPE: Only the saved TARGET, using L019, L605's coordinate identity, L826's r=0 endpoint evidence and Csordas Theorem4.1. No new derivative envelope or density certificate is covered.

### Primary input and applicability

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February2014, printed p10, equation(4.2), Theorem4.1:
part(i) asserts positivity for t>=0; part(ii) analyticity in
|Im z|<pi/8; part(iii) evenness; part(iv) derivative decay;
part(v) strict negativity of Phi'(t) for t>0. This is unconditional.
The PDF was essential: the HTML omitted the theorem's enumerated clauses.
The source credits part(v) to Wintner [58], with Spira [54] as another
reference. Those original proofs were not inspected; import the named
Csordas theorem as stated, without claiming an audit of Wintner's proof.

The exact source-to-local identification is already proved in L605:
K(u)=4 Phi(u/2), u>=0. The future assembly must retain both the positive
scalar4 and coordinate u/2, and handle u=0 by the source regularity.
No ordinary theta3 bound, transform value or differently normalized
kernel maximum can substitute for these hypotheses.

### Local endpoint overlap and arithmetic qualification

L826(6)-(8) already records 1<K(0)<2. Read the finite-sum and tail
proof, all arithmetic-contract paragraphs, and the independent step636
endpoint verification. It uses the n=1,...,8 sum with the full n>=9
tail; the r=0 case is the required endpoint input. The step636 audit
uses independent polynomial construction and monomial evaluation at
higher integer precision, with complete containment comparisons and
strict rational comparisons for(8). No preview or decimal value is
being treated as verification here. The original and independent
certificates are scripts/log-theta/endpoints_634.json and
scripts/log-theta/endpoints_audit_636.json. They were not replayed or
loaded in this literature step; this review relies on the canonical
proof and its recorded audit, with its stated integer-program trust.
A later application should cite that specific audited endpoint subclaim,
not assume all other conclusions of L826 or formal verification.

This is adequate SPECIALIZE coverage: import decrease, reuse the
endpoint result, and write only the necessary applicability argument.
Do not redo a global derivative-series proof or calculate a new maximum.
No matching full Mathlib theorem was checked; availability is unknown.

### Search and route decision

External queries: `Riemann kernel Phi strictly decreasing Csordas
Theorem 4.1 Phi 0`; `Riemann xi kernel maximum Phi(0) 0.446696`.
Primary evidence is the versioned Csordas PDF, not search snippets or
unrelated recent claims. Reused the October31 actual-theta Stein-premise
assessment for coordinate context, then retrieved the exact theorem.
Local searches checked actual K normalization/endpoint occurrences;
L605 and L826 are the relevant reuse, while L789's K is a different
saddle quantity and supplies no bound here. Read L938's coarse K<7
argument, L944's hypotheses/(1)-(3), and the saved coarse-endpoint stop.
That stop concerns the old allowance only and remains intact.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: the saved uniform constant2. Its plausible use is
reducing twelve-factor error allowances with unchanged degree256 data.
The bounded continuation test is exact source normalization plus the
already audited r=0 strict endpoint comparison. If either input does
not apply, stop this specialization and record the precise discrepancy;
do not increase numerical budgets. Density derivative propagation,
compact crossing coverage, other energies, contacts and independent
parameter endpoint signs remain unresolved. No crossing conclusion is
inferred from a kernel bound.

The next invocation separately approves this newly completed assessment;
subsequent mathematics can reuse it without further discovery browsing.
No lemma, mathematical script, DAG or PROOF assembly was changed.
