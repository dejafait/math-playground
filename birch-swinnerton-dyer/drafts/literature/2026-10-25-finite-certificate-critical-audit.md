# L119 finite-certificate critical audit — source scope approved

TARGET: Assess source coverage for a critical audit of L119's finite Selmer/height certificate, including the sharp Kummer threshold, height normalization, determinant error bound and k=0 case.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior finite-certificate assessment's discovery and duplicate searches; compared complete L119 with L001/L003, the relevant L118 statement/proof and its step-490 audit, foundations/03/04, L019 and ATTEMPTS/002/031. Reopened the two already identified primary height papers for the new interface's convention and precision scope; no novelty search was repeated.
SOURCE_EVIDENCE: Reused inspected Milne, Elliptic Curves (2021), IV (29) p.113/Theorem 3.1 p.114, and Ray Theorem 3.4 p.445 via foundations/04; reinspected Harvey arXiv:0708.3404v1 Theorems 1--3 p.2, Section 2.2 p.4 and Section 5 pp.11--12 through Proposition 9, and Stein--Wuthrich (2013) Sections 4/4.1 pp.1769--1771 and Theorem 6.1 p.1776.
COMPARISON: The arithmetic premises of the exact L119 audit fit these known results at good ordinary p>=5; its matrix-ball propagation, sharp-threshold composition, rational spanning and empty case are explicit local proof obligations, not additional arithmetic theorems requiring discovery. Approve their separate critical audit, without issuing its verdict.
GAP: L119's full correctness has not been independently audited; actual full Selmer and height certificates, uniform production and comparison with arbitrary complex analytic order remain absent. No source-scope blocker was identified for the bounded audit.
REASON: The source review now maps each part of the new composition to inspected arithmetic coverage or an elementary local proof obligation; the prior proof-attempt approval alone did not provide this separate audit scope.
SCOPE: Classical cyclotomic Selmer conventions; E/Q on a global minimal integral model; good ordinary p>=5; exact rational points and p-torsion dimension; certified full p-Selmer upper bound; absolute ordinary height balls; CM allowed only through the sufficient Ray implication; no assumed finite Sha, saturated point basis or full-height nondegeneracy.
LITERATURE_REASON: The startup assessment was REVIEW_REQUIRED for the newly composed L119 audit. The essential additional comparison is the exact normalization/absolute precision interface and which claims require local audit rather than another source theorem.
COVERED_TARGET: Critically audit L119's finite Selmer/height certificate using L001, L003 and audited L118, checking the sharp Kummer threshold, ordinary height normalization, absolute determinant error propagation, rational spanning and k=0 case.

## Gap, intermediate target and discriminating test

The main unresolved claim is rational rank equal to complex analytic order
for arbitrary E/Q, especially order at least two. The intermediate target
here is source-scope approval for a separate critical audit of L119.
If that audit passes, its conditional finite interface could remove the
p-primary Sha and augmentation defects for eligible inputs. It would not
supply the independent complex-order comparison or a uniform producer.

The coverage test is whether every arithmetic premise has a checked
source at the stated hypotheses, leaving only explicit local deductions
for the audit. This test passes at the level of source scope. A later
failed determinant argument or Kummer composition must be repaired or
narrowed in the audit; it is not pre-certified by this review. A newly
needed arithmetic theorem outside this scope requires REVIEW_REQUIRED.
No new lemma, mathematical script, calculation or audit verdict is made
in this literature step.

## Reused discovery, duplicate and failure evidence

[The finite-certificate comparison](2026-10-25-selmer-height-finite-certificate.md)
retains its actual searches, inspected passages and unread leads. Its
scope is unchanged: no p=3 extension, nontrivial finite p-primary Sha,
unsharp descent bound or proper height minor is newly admitted.
L001 already gives the torsion-corrected finite rank mechanism; L003
already gives the sufficient height/order criterion. L118's step-490
critical audit is retained, including its full compact Selmer convention.
No reproof of these known arithmetic inputs is warranted.

L019's statement and marked-space obstruction, ATTEMPTS/002's
characteristic-order obstruction and ATTEMPTS/031's ordinary-to-strict
localization gap remain contrasts. They do not prohibit independent
sharp full Selmer input, but they prohibit replacing it by the weaker
inferences they refute. No cross-notebook result is used. Existing
unfinished numerical work and its reporting failures are untouched.

## Source-to-obligation comparison

**Full Selmer threshold.** Reuse Milne, *Elliptic Curves*, second edition
(2021), IV equation (29), printed p.113 and Theorem 3.1, p.114
[primary text](https://www.jmilne.org/math/Books/EC2.pdf#page=118),
as inspected in the preceding assessment. That exact sequence does not
assume finite Sha. Its local application is L001. The critical audit must
check L119's use at n=1, the rational p-torsion correction, that b bounds
the full Selmer group, and the argument from Sha[p]=0 to vanishing of
p-primary Sha. A subgroup or isogeny-Selmer bound is not covered without
an independent comparison. No descent implementation is certified here.

**Height precision.** Reinspected Harvey,
[*Efficient computation of p-adic heights*, arXiv:0708.3404v1](https://arxiv.org/pdf/0708.3404v1),
24 August 2007: the integral-model/ordinary p>=5 hypotheses and complete
Theorems 1--3 on printed pp.1--2, Section 2.2 p.4, and Section 5
pp.11--12 through Lemma 8 and Proposition 9's statement. Theorem 3
provides absolute point-height precision with the increased sigma
precision specified there. Section 5 handles bad-prime admissibility by
multiplication and accounts for division and logarithms. These are point
computations, not a certified determinant algorithm. The audit must
retain exact zero/torsion handling and not evaluate a sigma formula at
the identity. Proposition 9 has its own admissibility and multiplier
conditions; no implementation or unexamined case is validated here.

**Normalization.** Reinspected Stein--Wuthrich,
[*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf),
Sections 4/4.1, pp.1769--1771: quadraticity, polarization, torsion and the
canonical ordinary sigma formula, and Theorem 6.1 p.1776. Its denominator
convention is opposite to Harvey Section 2.2 equation (3), as already
recorded in the preceding assessment and L119. The audit must verify the
same model, invariant differential and canonical sigma before accepting
the stated scalar conversion; matching two uses of the word height is
insufficient. Generator normalization is covered by foundations/04.
The audit must distinguish exact scalar nonvanishing from finite scalar
conversion, including any loss of absolute precision. The paper's
standing non-CM restriction remains when invoking its order theorem.

**Characteristic order and filtration.** Reuse foundations/03's named
control/cotorsion inputs and foundations/04's inspected Ray,
*Remarks on Hilbert's tenth problem and the Iwasawa theory of elliptic
curves*, Theorem 3.4, *Bull. Aust. Math. Soc.* 107 (2023), 440--450,
[printed p.445](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/32000D6BB2B3EC97CAD0B6F932B84935/S000497272200082Xa.pdf/remarks-on-hilberts-tenth-problem-and-the-iwasawa-theory-of-elliptic-curves.pdf#page=6).
This sufficient implication, specialized to Q, covers CM without using
the non-CM converse or an Iwasawa main conjecture. Schneider's original
proof remains unread as explicitly recorded in foundations/04; this is
not a new source-access claim. The audit must establish all premises
before invoking L003(2), then use audited L118's full-space accounting.
Vanishing higher layers must not be presented as a complex-order theorem.

**Elementary interface, not a missing arithmetic source.** L119 itself
contains the proofs to be audited for polarization of absolute balls,
integral scaling of true and approximate entries, column telescoping,
scaling back, strict zero exclusion and optional scalar-ball conversion.
Those finite matrix and valuation arguments require no new arithmetic
input. The audit must inspect the complete proofs and the stated
nonintegral boundary example, not merely their summaries. It must also
check independence before the rank bound, rational spanning before the
full regulator criterion, lack of any integral saturation requirement,
and the empty determinant with no height computation. Approving these
proof obligations is not proving or critically verifying them this turn.

## Decision and limitations

SPECIALIZE approves exactly the COVERED_TARGET above for a separate
research turn classified REPRODUCTION. No further literature turn is
needed unless the hypotheses or essential source needs change. The
completed review is source coverage, not a critical PASS for L119 and
not progress beyond the inspected arithmetic results. No actual E,p,
points, descent or height certificate is supplied.

Mathlib full matching certificate, arithmetic inputs and exact supporting
matrix/valuation theorem names remain not checked. This is not an
absence claim. No additional library search is needed to scope the
informal proof audit; precise canonical citations and local proof
obligations already suffice.
