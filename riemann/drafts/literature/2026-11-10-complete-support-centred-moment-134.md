# Complete-support centred moment — essential evidence review completed

TARGET: Review the essential source and executable coverage for an independent audit of Planat–Raymond v1 Theorem 3.3's bound M32<81/4 on its full closed parameter rectangle and all 151 index leaves.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step135 searched the exact checker filename and arXiv identifier/centred-moment terminology, followed the primary arXiv ancillary README to the fixed author release, and inspected the full pinned checker plus official python-flint 0.9.0 comparison/serialization documentation; scoped local searches found the pending premise, not a prior completed replay.
SOURCE_EVIDENCE: Planat–Raymond arXiv:2611.06245v1, 4 November2026, Section3.8.1 Theorem3.3 complete proof and Section3.9; complete core/analytic/check_centred_moment_01568.py at commit18dbc01ea36bf9a24d8f79822b5ce06b545e4ace; ancillary README, SOURCE_INPUT_HASHES, TESTED_ENVIRONMENT and PROOF_INPUT_BINDINGS; fixed release and CORE_INPUT_HASHES inspected. Exact locators and qualifications below.
COMPARISON: The theorem is exactly L960's moment premise and the executable supplies every stated finite proof case. No stronger result is sought. An independent reconstruction/audit is justified by the unrefereed proof-bearing computation; readable code and author receipts do not certify its execution or the analytic reduction.
GAP: Independently check the cited reduction, exact leaf coverage and every directed inequality, then certify the strict 81/4 bound; source availability is resolved, but no local replay, byte-hash verification or theorem verification occurred in this literature turn.
REASON: This essential executable was unread at startup. The source review now permits preparing a bounded reproduction, while complete stable models, other analytic estimates and global transfer remain separate.
SCOPE: Completed source comparison only; no new mathematical result, lemma or mathematical script. The separately nominated audit requires next-turn approval of its exact target.

## Proposed later audit, preserved from step134

The intended mathematical test is the source's complete-support bound

    M32(t,x)=sum_(n<=floor(sqrt(x/(4pi)+t/16)))
        exp(t log(n)^2/4-(1/2+t c_pol(x))log n) |log(n/32)| <81/4,
    c_pol(x)=log(sqrt(1+x^2)/(4pi))/4-1/(2(1+x^2)),
    98/625<=t<=1/5,
    6000000185827<=x<=120000000000000.

The source divides its covering index range from C=690988 to
H_g=3100000 into 151 consecutive closed intervals, uses the lower
spatial wall for the coefficient comparison, evaluates a 128-term
prefix and an integral through each leaf's upper index, and states
914 directed Arb gates. These remain source claims awaiting independent
execution and mathematical audit, not newly verified inputs. Preserve the n=32 zero factor,
the exact natural-index right-wall convention, and all terms through
the actual natural support. An envelope may extend beyond that support
only when its comparison is paid.

The primary source version and named script have now been located and
their entire load-bearing cases inspected; the comparison is below.
A positive printed receipt is not a proof.
Continue only with a precisely reproducible audit contract; if a source
block persists, park this premise and select independent work under
the shared recovery rule. No repeated admission or potential-cusp
audit is requested.

L960 is the consuming conditional result. L019/L058 fix its notebook
normalization; L059/L060/L617 explain collision relevance, not the
moment estimate. The real-jet remainder and phase/support bounds,
complete-polynomial stability/modulus, initialization, seams, infinite
exterior, zero time and L030–L032/C032a signs stay unresolved. No
cross-notebook input. Full Mathlib coverage remains unknown.

## Step135 primary executable and provenance

The primary [arXiv record](https://arxiv.org/abs/2611.06245v1) links
the checker and its [reproducibility README](https://arxiv.org/src/2611.06245v1/anc/README_REPRODUCIBILITY.txt).
That README identifies the [fixed author release](https://github.com/Dale-Dug/planat-raymond-collision-exclusion-0156821/releases/tag/certificates-0156821-v1),
commit `18dbc01ea36bf9a24d8f79822b5ce06b545e4ace`.
The complete release ZIP is `Planat_0156821_Reproducibility_20261104.zip`,
advertised SHA-256 `08bf5123ac79a438b626275eb8174df6d8cdfd069e7c7a0a70c1c4807b1ebde7`.
The needed small [checker at that commit](https://raw.githubusercontent.com/Dale-Dug/planat-raymond-collision-exclusion-0156821/18dbc01ea36bf9a24d8f79822b5ce06b545e4ace/core/analytic/check_centred_moment_01568.py)
was read completely, including imports, arguments, every loop/gate and receipt output.
The [GitHub code view](https://github.com/Dale-Dug/planat-raymond-collision-exclusion-0156821/blob/18dbc01ea36bf9a24d8f79822b5ce06b545e4ace/core/analytic/check_centred_moment_01568.py)
also exposes it. The pinned repository path begins `core/analytic/`, not `source/analytic/`.

Both the [arXiv hash inventory](https://arxiv.org/src/2611.06245v1/anc/SOURCE_INPUT_HASHES.json)
and [pinned core inventory](https://raw.githubusercontent.com/Dale-Dug/planat-raymond-collision-exclusion-0156821/18dbc01ea36bf9a24d8f79822b5ce06b545e4ace/CORE_INPUT_HASHES.json)
declare checker SHA-256 `c6470667cbf92f7fcd219ff413fc2874dbab3c1f606f645cc4abfad89c50a818`.
These are inspected declarations, not locally verified hashes. The arXiv
Python attachment was rejected by the browser's content-type handling;
shell curl failed DNS. The pinned raw GitHub text succeeded, so this is
not a persistent essential-source block. No executable was run or saved.

The [tested environment](https://arxiv.org/src/2611.06245v1/anc/TESTED_ENVIRONMENT.json)
states CPython3.12.14, python-flint0.9.0 and FLINT3.6.0. Its NumPy pin
qualification concerns the larger release; this checker imports no NumPy,
source arrays, local modules or old receipts. The full 100MB archive and
unrelated Gram/separator programs were not needed or read for this target.

## Complete source-to-code comparison; execution still unpaid

The following maps inspected code to the cases in
[Theorem3.3's proof](https://arxiv.org/html/2611.06245v1#S3.SS8.SSS1).
It records coverage, not a fresh proof of those reductions.

| Required case | Inspected implementation |
| --- | --- |
| Exact domain and natural-index walls | Integer X,W,H,C; Arb rational a=98/625,T=1/5; both global wall gates. |
| Closed integer cover | `ends` recurrence uses integer `101*n//100`, capped at H; adjacent endpoint pairs; start/end/increasing gates; endpoints and leaf count saved. |
| First and later left walls | X for L=C; otherwise 4*pi*(L²-T/16); per-leaf `xleft>=X`. |
| Coefficient comparison | Exact displayed c_pol formula; sigma=1/2+a*c_pol(xleft); per-leaf log(U)<4*c_pol(xleft). |
| Whole decreasing tail | g(log128)<0 and g(logU)<0 gates for the source's convex quadratic; no sampled derivative test. |
| Prefix, including n=1 and n=32 | All n=1,...,128; distance uses log(32/n) below32 and log(n/32) otherwise; at32 the argument is exactly1. |
| Exact integral | B=sigma-1; erfi endpoint difference gives I; J=2/a*(E(logU)-E(log128)+B*I); tail=J-log32*I. |
| Strict bound and proof data | I>0,tail>0 and head+tail<81/4 on every leaf; individual enclosures and named gates written. |

The proof also supplies the analytic cases not encoded as scalar gates:
c_pol increases; the heat exponent is nonpositive throughout each support;
the convex quadratic's endpoint signs control its entire interval; and
the decreasing-tail sum is bounded by the integral through U. These
arguments, the antiderivative identity, all closed walls, and the allowed
extension from N to U must be audited before importing the conclusion.
No cancellation of signed summands or support truncation is being licensed.

Official [python-flint0.9.0 general concepts](https://python-flint.readthedocs.io/en/stable/general.html#inexact-numbers-and-numerical-evaluation)
specify rigorous ball arithmetic and certain-truth comparisons; unresolved
comparisons return False. The [arb reference](https://python-flint.readthedocs.io/en/stable/arb.html)
documents erfi, logarithm, exponential, square root and parseable ball
serialization, warning that decimal round trips may enlarge balls.
The code uses Arb throughout the evaluated formulas and rejects precision
below192; `gate` raises on failure. A replay must retain radii and exact
rational thresholds, and record its actual arithmetic-library versions.

The printed `maximum_leaf_upper` chooses a serialized leaf ball by midpoint;
it is not itself a certified maximum of the upper endpoints. This is an
output-scope caveat, not an established defect in the per-leaf strict gates.
The independent audit should compute a genuine maximum upper endpoint and
check all individual gates. It should explicitly check the claimed151 leaves
and914 named gates rather than accepting the printout or count alone.
The paper's approximate20.21385859525945 is author-reported, unreplayed here.

## Decision and bounded continuation

Essential source coverage is now adequate for a separate REPRODUCTION audit,
not a novel lemma. The exact next target and replay contract are saved in
`drafts/literature/2026-11-10-centred-moment-independent-audit-135.md`.
Continue only with complete directed evidence for every case; fail/narrow
the audit on a bad reduction, missing closed leaf or unresolved/failed gate.
Do not expand to the release's global Newman claim. If local access to the
original bytes fails, an explicitly labelled independent implementation of
the inspected formulas is permissible; never claim an unverified hash or
byte-identical replay. Library implementation correctness remains trusted,
and reuse of Arb is not an independent interval-arithmetic foundation.
