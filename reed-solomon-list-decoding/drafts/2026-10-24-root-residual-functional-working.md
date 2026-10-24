# Fixed residual-functional test — working record

2026-10-24, step 457. RESEARCH / REPRODUCTION / calculation under the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-24-root-residual-mode-one-functional.md`.
Exact approved target: Test one residual-corrected centered-form enclosure of lambda_1(K(x*))+R using L112's original box and saved preconditioner, with all data unchanged.

Main gap: arbitrary-center 67/68 safety, with bracket 955–957.
Intermediate target: enclose the normalized mode-one functional at L112's
same root using the exact contractions and one fixed residual correction.
A nonnegative lower endpoint could settle this one sufficient spectral
comparison toward an eventual all-mode bound. An upper endpoint below
zero rejects that comparison only; a strict straddle parks this estimate.
No change to the point, scales, equations, endpoints, preconditioner or
root is authorized. No second weights, solve, scan or refinement.

Inputs: L021,L098,L112,L113,L114,L120 and foundations/09,12,13,14,
the original root/global-comparison certificates and their audits.
Read the relevant full L112/L120 proofs, primary mean-value import and
ATTEMPTS/098–099; no duplicate functional computation was found in the
saved assessment or these records. Existing notebook changes are preserved.

Plan: use v_i=x_i/s_i, a and B from L112, positive R0=c5/u5^2,
w_i=P1(i)*s_i/R0, z=C^T w with the saved rational C. Collect exactly
the cubic coefficients of h(v)=1+w^T v-z^T F(v), including repeated
factors. Enclose its complete gradient on B and apply the imported
scalar mean-value theorem with B-a unchanged. Independent reconstruction
must verify coefficients, constants, weights, derivative occurrences,
all arithmetic and the final zero comparison before any verdict.
This record is saved before computation. No sign has been established.

Even success leaves modes other than one, full included/excluded PSD,
stronger distributions, global uniqueness, measures, packing, RS realization
and the finite boundary unresolved.

Completed: the fixed 10^120 arithmetic grid yields a strict straddle,
with outward normalized bounds [-8460928885,8462190625]/10^6. All
56,821 independent checks pass, including exact source-row residuals,
all 28,215 collected cubics and complete derivative bounds. The full
proof and precise import are canonical in L120's added residual-test
section; certificates are `scripts/finite-support/root-residual-functional.json.gz`
and `scripts/finite-support/root-residual-functional-verification.json`.
Both result and error fractions were inspected completely. The initial
JSON-inspector pointer '/' was rejected; omitting the pointer supplied
the intended root preview, which was not used as mathematical evidence.
One documentation patch failed its final context match and applied no
changes; the corrected patch preserved all earlier text.

Outcome: inconclusive mathematical EXPLORATION, no functional sign,
full PSD or main-boundary improvement. Park the estimate under
ATTEMPTS/100. The next actual-principal Rayleigh target is explicitly
REVIEW_REQUIRED, without a new derivation or approval. After the canonical
L120 addition, the constructor and verifier were rerun to bind the final
documentation inputs. The complete bounds and 56,821-check result agree.
Scoped structural validation passes: 126 nodes, 477 edges, acyclic and
complete local coverage. No DAG or PROOF assembly change was needed;
the new subsection adds an inconclusive estimate to the existing L120
argument without changing its conclusions or direct mathematical inputs.
