# Proposed separate critical audit of the actual Wronskian second moment

TARGET: Critically audit L381's dyadic Wronskian second moment, checking the shifted-jet specialization, same-height contour, infinite tails and sharp endpoints.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed primary comparison and its exact-statement/stronger-result search; checked L381 in full, the prior calculation assessment, its history, and the stopped first-mean certificate for duplicates and scope. No changed mathematical hypothesis requires a broad search.
SOURCE_EVIDENCE: https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf (Young, Arch. Math. 95 (2010), 539–548, DOI 10.1007/s00013-010-0199-9), (2.1)–(2.3), (3.4), Lemmas 4–5 and complete Lemma 5 proof pp. 540–543; local L320 full strip proof (4)–(5), L380 exact carrier/reflection (3)–(5), and L368 right-line jets (3)–(5).
COMPARISON: The inspected moment input covers fixed rational twists and small complex shifts; it does not state L381's full projected statistic. The canonical result's diagonal evaluation, holomorphic projection contour, endpoint jets, and sequential infinite-tail/unsmoothing limits are the specific difference to audit, not a known full matching theorem.
GAP: Essential source coverage is ready; independent verification of L381's coefficient and all o(log H) obligations remains pending. This approval authorizes the audit, not the asymptotic or its correctness.
REASON: The newly proposed audit now has separately reviewed coverage; import the known moment by citation and independently check only its applicability and the family-specific remainder arguments.
LITERATURE_REASON: Separate approval is required for the newly written audit continuation; reuse ready sources while checking the essential qualifications of the unequal-shift and contour implementations.
SCOPE: L381 with the fixed actual F_0,G,A,Wcal, positive real heights, ordinary derivatives and H tending to infinity; no RH, simplicity, noncoincidence, discriminant or common-zero hypothesis.

Essential input IDs: L381, L380, L368, L366, L320. Reuse
`drafts/literature/2026-10-08-wronskian-second-moment-calculation.md`
and the complete primary comparison in
`drafts/literature/2026-10-08-wronskian-second-moment.md`.

A bounded independent audit should check Young's weight/shift/twist hypotheses,
both hm=kn diagonals, the uniform Mellin-line remainder on the unequal-radius
shift contours, removal of alpha+beta degeneracy before Cauchy differentiation,
the full gcd coefficient, the nonnegative smooth bracketing, and the sequential
head/tail limits. Check the explicit holomorphic replacements for conjugation
and omega in the same-height component, absence of rectangle poles, the
logarithmic-radius endpoint jet bounds from L320 at R=1, and the O(1)
projection average. Do not accept merely a positive modulus diagonal.

Continue by validating or repairing the precise coefficient and every o(log H)
obligation. If an essential estimate fails, retain the completed work, record the
failed claim and narrow the conclusion honestly. A validated second moment still
leaves common-zero resets, common-free localization, global actual-theta positivity,
total L367 margin, low indices, heights above forty and endpoint margin unresolved.
Full matching Mathlib coverage is not checked. This is now a ready assessment
for the exact audit target; the mathematical critical audit is not completed.

## Separate source-coverage review, 2026-10-08

The direct primary PDF was accessible. Read the weight requirements,
Cauchy-differentiation paragraph, both functional-equation terms, gamma-ratio
remark, and the complete off-diagonal proof. Young permits complex shifts
of size O(1/log T), positive integer twists with hk≤T^(2θ), θ<1/2,
and smooth weights in [T/4,2T] with derivatives bounded at scale T/log T.
The Cauchy argument requires holomorphic errors uniform on the contours.
Lemma 4's auxiliary factor is singular when the shift sum vanishes;
the two-diagonal combination must be handled before differentiation.
Lemma 5 treats both off-diagonal orderings by symmetry and integration
by parts. These inspected cases are the necessary source qualifications,
not an endorsement of L381's Mellin remainder.

The prior comparison already screened Bui–Hall, Bettin–Chandee–Radziwiłł
and Pliego; their mismatched hypotheses and unread leads stay as recorded.
No full matching theorem or novelty inference is added. The stopped L380
first-mean signing mechanism is a contrast, not a duplicate of this audit.

L381 was read in full to locate the source/application boundary. Its
sections 2–4 claim all remaining estimates explicitly, so the next audit
has concrete independently checkable obligations rather than an essential
unread-source blocker. Reading those claims is not verification. In
particular, check the gamma-ratio uniformity outside bounded Mellin height
against the actual Gaussian factor; the logarithmic-radius derivative
disks against the full L320 strip; the exact Ω formula against L380/L369;
and both orders of limiting operations against the norms actually proved.
L366 (1) must also be checked for the actual-pair normalization in that
audit. Ordinary Cauchy integral/derivative theorems and holomorphic-series
differentiation are standard named inputs, not new lemmas to reprove.

Continue only if the full coefficient and every required error survive
independent checking, or a precise repair is possible within the same
covered statistic. An uncontrolled contribution at order log H requires
retaining the failed claim and narrowing the conclusion. Neither source
access nor a positive modulus diagonal certifies the total real square.
This completed step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION;
the next mathematical audit is intended as REPRODUCTION. No new result,
lemma edit, mathematical script or argument change is made here.
