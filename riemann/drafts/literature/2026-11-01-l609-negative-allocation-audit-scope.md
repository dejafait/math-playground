# Coverage needed for an independent audit of the exact-theta witness

TARGET: Assess coverage for an independent audit of L609's negative exact-theta allocation witness, including the interval engine, all tails, quadrature and normalization.
CHECKED: 2026-11-01
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the unchanged exact-allocation and numerical-method comparisons; searched official Python Decimal exp/copy_negate/next_minus/next_plus specifications and inspected version-tagged CPython documentation. Scoped witness, correction history and allocation-stop reads identified the audit obligations; no renewed sign search.
SOURCE_EVIDENCE: CPython v3.15.0 Doc/library/decimal.rst, Decimal constructor, copy_abs/copy_negate/exp/next_minus/next_plus, Context correspondence and Rounding modes; https://docs.python.org/3.15/library/decimal.html corresponding named entries. Reuse Johansson arXiv:1802.07942v1 Sections 2–2.1 pp.2–3 and arXiv:1806.06725v1 Sections 1.2 and 1.4.2 pp.4,12–13 as assessed previously.
COMPARISON: Official arithmetic guarantees fill the missing implementation-semantics source coverage; existing numerical references cover inclusion and tail methods. None certifies this custom program or states G's sign. L609's negative witness remains unaudited and does not sign the full determinant.
GAP: Source coverage for preparing the bounded audit is complete; independent checking of every local algebraic/error specialization, full code and complete certificate remains pending. No replay or mathematical validation was performed here.
REASON: Import documented arithmetic guarantees rather than reprove a numerical library; test the custom specialization independently in the next mathematical step, retaining the original qualifications and corrections.
LITERATURE_REASON: Changed target from the approved witness calculation to independent implementation/proof audit; reuse adequate method coverage rather than repeat the exact-sign search or browse without a specific missing premise.

## Original proposed scope (retained; coverage completed below)

Read only L609 and its exact direct inputs as needed: L016, L019,
L564's complete-kernel envelope, L604, C604a and C604b. The executable
is `scripts/theta-allocation/certify.py`; complete enclosures are in
`scripts/theta-allocation/certificate.json`. The preview is selection
only, not evidence. Recheck k=2 Phi_R and k=4 Phi(u/2), the exact
Z^2G algebra, all denominator separation, and the retained floor in
D=ell F^2+integral G. No cross-notebook inputs are required.

Verify the precise interval arithmetic semantics and every actual
bound, not requested tolerances. Recompute the exact polynomial
recurrence independently, including P1's 60 and P2's -224; previous
transcription errors and the Decimal unary-negation correction remain
recorded in the working note and canonical lemma. Confirm that the
final run, not a superseded output, supports the stored endpoints.
Check geometric tails n>=6, real second derivatives on all [a,8]
cells, all [0,a] boxes, angle recurrence/Lipschitz bounds and H(b)'s
descending enclosure. A reproducible program is not a formal proof
assistant certificate; do not conflate its label with independent
correctness verification.

The later audit's bounded test is whether the complete evidence still
gives a strict negative upper bound for the single point (11,7/16).
Do not expand the grid, certify other candidates, or infer a sign for
the a integral or D. Preserve and repair any error before accepting
the witness; an invalid sign enclosure must reopen this allocation
question, not be hidden by a preview. Imported source proofs and all
higher signs remain independently unresolved. Mathlib coverage is
unchecked. This proposal did not approve or perform that audit; the
completed source decision below supersedes its coverage status only.

After source coverage is approved, the proposed audit is an ordinary
proof_audit/routine_audit, standard/high: finite arithmetic, hypotheses
and replay, with no creative mechanism or complete-solution claim.
No independently controlled signed theta estimate currently justifies
preempting this essential certificate check with a creative sign proof.

## Completed source comparison, 1 November 2026

The main gap is actual-Xi all-degree signs at unbounded heights. The
intermediate target is the independent audit of this single allocation
witness. Its downstream use is to decide whether the fixed-a sufficient
condition is actually excluded; neither outcome settles integrated
compensation, its floor, or independent higher signs.

Reused `2026-11-01-theta-integrated-layer-compensation-scope.md` and
`2026-11-01-theta-integrated-layer-negative-witness-test.md`: the object,
density and known-result comparison are unchanged. Read L609, the
calculation working note, witness history and allocation ATTEMPTS record.
They preserve P1/P2 transcription and negation corrections; the audit
must check final artifacts rather than obsolete outputs. Earlier
pointwise, generic-Stein and total-cancellation stops are contrasts,
not substitutes for evaluating this exact G. No duplicate audit was
found in these scoped records. No novelty claim is made.

The fresh official reference is the Python Software Foundation,
*Python Library Reference*, `decimal`, named API entries, with the
[CPython v3.15.0 source documentation](https://raw.githubusercontent.com/python/cpython/v3.15.0/Doc/library/decimal.rst)
as a versioned reference. Inspected constructor semantics; `copy_abs`,
`copy_negate`, `exp`, `next_minus`, `next_plus`; `Context` method
correspondence; and rounding definitions. The tagged text specifies
nearest-even correct rounding for exp, exact context-free sign copying,
adjacent representable values in the selected context, and equivalence
of `C.exp(x)` with `x.exp(context=C)`. The
[rendered 3.15 documentation](https://docs.python.org/3.15/library/decimal.html)
also describes exact string/integer construction, directed rounding,
exponent limits and signals. Its served page identifies itself as 3.15.2;
`python3 --version` here reports 3.15.0. The tagged reference resolves
the specification version; it does not identify the historical run's
backend or independently verify an implementation.

Read `certify.py` only through the initial sincos routine to identify
the actual APIs and source needs. Matching code to these specifications,
checking remaining operations and identifying the replay environment
are audit work. Documented exp accuracy alone does not certify the
program's endpoint widening, exponent handling or error propagation.
No executable arithmetic test or certificate replay was run.

Reuse Johansson's previously inspected real-box inclusion and explicit
series-tail coverage by the precise citations above. The integration
paper was also reopened at Section 2.1; no analytic-quadrature branch
is proposed. The standard named real Taylor remainder theorem is already
the midpoint-error input in L609. Its local derivative bounds and all
constants require audit, not another quadrature theorem or reproof of
the library. The second Johansson paper supplies a geometric-majorant
method, not u derivatives of this theta density. No inaccessible
library manual is essential and no source blocker remains.

Queries issued: `site.docs.python.org 3 decimal exp correctly rounded
ROUND_HALF_EVEN copy_negate next_minus next_plus` and the paired Johansson
identifiers `1802.07942` / `1806.06725`. Nonprimary search hits are not
inputs. Direct official API and tagged-source reads, with the adequate
reused assessments, are the evidence. Mathlib coverage remains unchecked;
no formal certificate claim is made.

IMPORT applies to this completed source-coverage task only. The actual
audit remains the separately prepared EXPLORE scope in
`2026-11-01-l609-independent-certificate-audit.md`; its readiness receives
the supervisor's separate next-turn approval. Continue only on complete
independent evidence retaining a strict negative upper endpoint; retain
and repair any defect before accepting the witness. No new lemma,
mathematical script, certificate, DAG edge or argument was written.
