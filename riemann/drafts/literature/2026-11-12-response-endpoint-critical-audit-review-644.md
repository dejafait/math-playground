# Nomination644: critical audit of the response endpoint decomposition

TARGET: Critically audit C999z's exact two-parity Carleman split and effective raw-L2 finite-rank remainder bound, including the singular corner, j=0 and bounded-operator passage.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate literature-only645 reused review642/comparison643's recorded exact-response/Carleman/Hankel and effective-kernel searches and532/541 comparison; inspected C999z for scope, C744v Section3/audit534, C999k Sections1-2, C744z Section8 stop, C999y audit642 conclusion and600/603/635/640 failure records. No fresh external search, originality claim or mathematical audit was performed645.
SOURCE_EVIDENCE: Reused assessment642/comparison643's inspected Li paper45 displayed v2 (9November2026),Section2/(2.4)-(2.5),Lemma3.1/full proof/(3.1)-(3.4); paper60 displayed v1 (26October2026),Section2/(2.4)-(2.7),Section3/(3.1)-(3.7); Teschl GSM99 (2009),Section6.3 pp139-141/(6.8)-(6.18),Lemma6.9/proof andCorollary6.11/proof. URLs and applicability below and in642; no new primary retrieval is claimed.
COMPARISON: Ready sources cover arbitrary-a parity vectors, the smooth-core identity, Carleman boundedness and square-integrable-kernel operator control. They suffice for a separate audit of this fixed-a specialization; they do not verify C999z's coefficient, corner regularization, local estimates, finite-rank construction or all-L2 identity. Those remain later audit obligations.
GAP: Essential coverage is ready for this audit only. C999z's derivation remains unaudited; verify every normalization, boundary case, complete error allowance and operator-extension hypothesis before downstream use. No sign, reference-order/coercivity, energy-normalized estimate or RH consequence is covered.
REASON: Separate comparison645 approves the unchanged saved audit target using ready coverage; mathematics644 is retained without being accepted as audited. No additional essential theorem or changed source hypothesis was identified. Next perform the conceptual audit, not another source approval.
LITERATURE_REASON: The target changed from constructing the endpoint split to auditing new C999z. This separate scope approval uses ready642/643 coverage and resolves the pending gate without fresh browsing or deriving mathematics.

## Historical nomination644 (approval was pending)

Main gap: L030-L032/C032a actual-Xi positivity. This audit could make the
endpoint decomposition a trustworthy input to a later middle-form
reference. It establishes no reference coercivity, induced-coupling sign,
S3 inequality, higher-endpoint coverage or global RH assembly.

The exact new local claim is in
[C999z](../../lemmas/C999z-response-endpoint-carleman-remainder.md).
Do not treat this nomination as its verification. Its source gate was
review642/comparison643 for the completed calculation; that prior approval
is not retroactively changed by this new REVIEW_REQUIRED nomination.

Bounded audit test after approval: check the unitary reflection and both
parity denominators, all four product contributions and j=0, the exact
1/2 pole coefficient, the quotient-derivative bound303/4, both closed-square
boundary cases, the compact-test density argument on complex L2, and the
rank and full error formula in (4)/(12). Confirm that raw-L2 control is
not claimed as an energy-normalized comparison. Retain a precise error if
one is found; continue only with the corrected complete statement. Failure
of the full split or a nonvanishing error bound stops this construction,
without converting any stopped sufficient comparison into an actual-form
counterexample.

Essential inputs are C744v Section3/audit534, C999z (new and unaudited),
and assessment642/comparison643's precise source cases. C744z Section8,
C999k Sections1-2 and C999y Section4 are scope contrasts and later-use
warnings, not mathematical premises of C999z. No cross-notebook input.
The original source-to-Xi/core/c_* and computational contracts remain
unresolved; the elementary kernel calculation itself uses no floating-point
certificate. Full matching Mathlib coverage remains unchecked.

After a source-scope approval, route the actual critical audit as
proof_audit/conceptual_audit, deep_research/xhigh: the relevant issue is
the normalization and limiting operator identity at a non-square-integrable
singular kernel, not a routine numerical replay. No protected creative
sign mechanism is nominated yet: coercivity and signed-coupling evidence
are missing, and an audit must precede treating the new split as a reliable
input. Do not reopen the unchanged598 rank-two or32-prefix comparisons.

## Separate source-scope approval645 — 12 November 2026

SPECIALIZE now covers the exact TARGET above for a later independent
conceptual audit. This is a source comparison, not verification of C999z.
The full new proof was read to identify its inputs and obligations only;
no estimate was rederived or accepted and no lemma or script was changed.
The original nomination and completed calculation644 remain preserved.

The ready [assessment642/comparison643](2026-11-12-response-endpoint-carleman-review-642.md)
contains the actual searches, primary passages read, versions and access
limits. Reuse is adequate because this audit changes neither the fixed
value a=log(3)/4 nor the response vectors, measure, parity spaces or
square-integrable-remainder hypothesis. No new source discovery or
fresh primary extraction is claimed here. The relevant primary inputs are:

- Hongmin Li, *Cutoff-free positivity of localized Weil forms through the
  (log 11)/2 threshold*, [paper45 displayed v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
  Section2/(2.4)-(2.5), Lemma3.1 and complete proof/(3.1)-(3.4).
  This supplies arbitrary-a response vectors and the smooth-core identity
  under the unitary half-interval convention, including both boundary
  conditions. It does not alone supply the all-L2 operator identity.
- bramble_trace, [paper60 displayed v1, 26 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/60),
  Section2/(2.4)-(2.7), Section3/(3.1)-(3.7). Its boundedness/core cases
  cover the Carleman-majorant method; its full Fourier formulas are a
  comparison, not a physical-kernel compact split. Radius2 constants and
  numerical positivity are not imported at the present a. The audit may
  use C744v Section3/audit534's specialized bounded extension, while
  checking C999z's applicability rather than reproving the Green identity.
- Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99
  (AMS, 2009), [author-hosted edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
  Section6.3 printed pp139-141, (6.8)-(6.18), Lemma6.9/proof and
  Corollary6.11/proof. A square-integrable kernel on the product measure
  space gives the stated operator-norm control and Hilbert-Schmidt
  compactness. Apply this only to the remainder/error after its kernel
  hypotheses are verified; the singular Carleman kernel is not covered
  by that square-integrability assertion. No general theory needs reproof.

The precise difference requiring local audit is C999z's own algebra and
bounds, not an absent source theorem. Check reflection/unitarity and both
parity denominators; all four products and j=0; the claimed singular
coefficient; the closed-square quotient estimates and both boundary
conditions; integration on compact test supports followed by the bounded
sesquilinear extension on complex L2; and the rank, full error formula
and tolerance rule. These are audit questions, not conclusions645.
Confirm that neither positivity of the remainder nor energy-normalized
control is inferred from a raw-L2 error. Correct and retain any precise
failure. Continue downstream only if the complete corrected identity and
vanishing error survive; an unisolated singular contribution or a
nonvanishing complete allowance stops this construction.

Duplicate/failure comparison: C744v already supplies the response identity
and boundedness; C999z is the single canonical new split, so the audit
must not create a duplicate lemma. C744z Section8/9 stops its fixed32
sufficient comparison. C999y Section4 stops a rank-two addition to the
unchanged598 matrix. The600/603/635 records concern failed sufficient
allowances or incomplete computation, not actual negative forms. None
answers this audit, supplies a sign for the compact remainder, or licenses
restarting the parked prescriptions. Broader Carleman/Hankel leads left
unread in643 remain unused and nonessential. No novelty inference follows
from the recorded searches. Full matching Mathlib coverage is unchecked;
its absence is not asserted and is not an audit-completion gate.

The main gap remains L030-L032/C032a actual-Xi positivity. A successfully
audited full endpoint split could support a later middle-form reference;
its form order/coercivity, energy comparison, actual remote and induced
couplings, C744q, H2, higher endpoints and global assembly remain separate.
Essential audit inputs are C744v Section3/audit534, C999z and the precise
sources above via642/643. C744z, C999k and C999y are scope warnings, not
new mathematical premises. Original source-to-Xi/core/c_* and numerical
contracts remain unresolved. There is no cross-notebook input.

Source coverage is sufficient and no persistent essential access blocker
remains. Route the next turn to proof_audit/conceptual_audit,
deep_research/xhigh: singular-corner cancellation and extension of a
non-square-integrable kernel identity are delicate analytic obligations.
This preparatory audit is not creative mathematics. A justified new
central sign mechanism remains unavailable until the split is reliable
and a concrete coercivity/coupling test has its own source coverage.
Outcome645 is EXPLORATION in source-scope comparison, not mathematical
ADVANCE or verification. No mathematical exploration attempt is spent.
