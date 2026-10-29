# L135 conceptual audit — completed, 2026-10-27

Exact approved target: Critically audit L135's span-two evaluation-line bridge, including the exceptional-root split, both collision arguments and all 21 projection-subgroup witnesses, without assuming a group-labeled classification.

Coverage: `drafts/literature/2026-10-27-l135-critical-audit-coverage.md`
was EXPLORE before invocation. This is a mathematical audit, not another
literature review. The main gap is arbitrary-center 67/68 safety; accepting
this intermediate bridge could support a later span-two classification.
The acceptance test is every permitted case and all 21 finite identities;
a failed case blocks classification use. Span three, retention, threshold
1532496, compatible laws and global RS transfer remain independent.

Read the complete canonical L135 proof and generator, L030's actual-label
construction, the approved assessment and the previous bridge comparison,
ATTEMPTS/109 and history/527. The exact table and the two failed arbitrary
omission probes have been read in full. No cross-notebook input or new
source theorem is needed. Existing changes and all stopped routes remain.

Initial conceptual checks (subsequently accepted): affine span is two since the original
coefficient image includes zero and spans V. A zero evaluation makes
V the entire two-dimensional space of quadratics divisible by X-x_0;
the remaining normals are [1:x]. In the other case each normal occurs
at most twice by the nonzero quadratic s h_1-r h_2. Both projection
formulas have the stated sign. Same-direction invariance uses a nonzero
translation in the prime field. Cross-direction invariance uses the
ratios kappa_r/kappa_r0 and retains the origin separately. For Q off the
two lines, at most one of its seven marked intersections is the origin;
six marks and two possible polynomial values force three distinct actual
evaluation labels. Coordinate translation preserves the affine span
although the reference polynomial changes. Repeated messages are allowed.

The initial checkpoint left arithmetic and final acceptance pending.
They are now complete; no classification or new lemma was attempted.

Implementation failure retained: the first independent-check run raised
`ValueError: malformed node ... Name(id='a', ctx=Load())` because its table
parser also selected the symbolic `(a,b)` header. It produced no
certificate and established nothing. The parser was restricted to rows
starting with a numeric pair before rerunning; no mathematical data or
threshold was changed.

## Decision and evidence

Accept L135 without changing its hypotheses or conclusion. The complete
proof and detailed logical audit are canonical in
`lemmas/L135-span-two-evaluation-line-separation.md`, including affine
origin invariance, both projection signs, all exceptional normals, and
distinct evaluation labels in the six-mark pigeonhole step. The L030
construction is the only local theorem input; its probability law and
the other contextual lemmas are unused. The existing DAG needs no change.

`scripts/finite-support/critical_audit_l135.py` independently verifies
all 21 printed witness rows using exhaustive quotient solving and a
discrete-log/gcd subgroup construction. It compares every field of all
126 saved cases, all size-table entries, witness records and summaries.
The complete audit certificate is
`scripts/finite-support/l135-critical-audit.json`; `/required_checks`
and `/failed_probe_checks` were inspected in full. Required subgroup
minimum 68 and orbit maximum two meet the respective bounds >=68 and
<=2. The two stronger omission failures have sizes 34 and 17 and four
and eight orbits; their complete sets match and remain preserved.

Outcome: ADVANCE through independent verification of this local input,
classification REPRODUCTION. There is no new theorem or asserted
progress beyond the checked sources. The bridge is available for a
subsequent source-gated cyclic-cubic comparison. Span-two collapse,
span three, deletion robustness, threshold 1532496, compatible laws and
RS transfer remain unresolved; the 955–957 bracket is unchanged.
