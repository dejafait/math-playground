# Equality relative Ext and reflexive extension — source comparison

TARGET: Assess whether the relative trace-free Ext complex of the (14,21) equality family yields a global Chern-class obstruction after extending the stable tangent summand reflexively across Z.
CHECKED: 2026-10-15
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted relative-Ext/reflexive-extension, Bando--Siu admissibility and weak-hyperholomorphic stability searches; read L068, L100 including its canonical separate audit, L071/L097 hypotheses and scoped L066 jump passages; compare ATTEMPTS/063/065 and the existing tangent assessment.
SOURCE_EVIDENCE: Stacks 0EBJ and 0B3N give algebraic reflexive extension and surface local freeness; 0B91 and 0BDH distinguish perfect base change from ordinary concentration. Verbitsky math/0107182v9 Definition 4.14/Theorem 4.15 require codimension at least three; Proposition 5.3's complete proof uses Lemma 5.4 with complex dimension greater than two.
COMPARISON: Algebraic reflexive extension is a covered tool, but it does not extend the given metric or identify the reflexive hull's second Chern class with the virtual index. The inspected no-L2 shortcut has a codimension mismatch on this K3 base; the isolated-point proof does not supply its missing dimension-two case. L068's everywhere-stable concentration is unavailable at split fibres.
GAP: No applicable theorem inspected makes the punctured normal connection admissible or its algebraic extension semistable at h; point-supported higher-image, torsion and reflexive-hull corrections also remain uncomputed. No global Chern contradiction follows from this review.
REASON: Park the automatic metric-extension/Chern-inequality mechanism, with a specific source-hypothesis obstruction rather than another search for the same bridge. Isolate an independently testable algebraic extension-and-defect budget, requiring no metric extension, in a separate proposed continuation.
LITERATURE_REASON: The gate required review of this changed extension target; prior determinant and stable-open geodesy coverage did not address its essential codimension-two admissibility or Ext-defect hypotheses.

## Completed comparison

Completed LITERATURE / NEGATIVE / NOVELTY_UNCHECKED: the negative evidence
changes the route, not the existence verdict for F. No lemma, numerical
calculation or mathematical script was made. The main gap remains universal
primitive rational Hodge realization. A global constraint on this particular
equality kernel could help restrict one candidate supply; it would not
construct cycles or settle the independent transport problem.

**Algebraic versus metric extension.** Read the statements and full short
proofs of [Stacks Lemma 31.13.12, 0EBJ](https://stacks.math.columbia.edu/tag/0EBJ)
and [Lemma 31.13.15, 0B3N](https://stacks.math.columbia.edu/tag/0B3N).
The first is an equivalence for coherent reflexive modules under restriction
and pushforward across an open complement where the ambient local rings
have depth at least two; the second identifies reflexive and finite locally
free modules on a regular scheme of dimension at most two. The smooth
algebraic K3 base and its finite complement fit those ambient hypotheses.
An actual *algebraic* splitting on U would therefore have a covered extension
tool. One must first construct that splitting algebraically; analytically
holomorphic data on nonproper U do not acquire algebraicity by GAGA alone.
Neither cited theorem asserts extension of a chosen Hermitian metric,
semistability, or a Chern number computed from a derived index. These
standard results should be imported, not reproved.

Read [Stacks Lemma 36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91)
and [Lemma 36.31.3, section 0BDH](https://stacks.math.columbia.edu/tag/0BDH).
Proper flat finite-presentation pushforward of a perfect complex is perfect
with arbitrary derived base change. The second result gives the open locus
of single-degree locally free concentration by a derived-fibre criterion.
It does not turn jumps of derived-fibre Ext into constant-rank ordinary
direct images. L066 already records this trap, for a different two-parameter
Hom complex; it does not calculate this equality-family self-Ext object.

**The proposed no-energy shortcut fails its scope test.** M. Verbitsky,
*Hyperholomorphic connections on coherent sheaves and stability*,
[math/0107182v9, 24 January 2008](https://arxiv.org/html/math/0107182v9#S4.SS3),
Definition 4.14/Theorem 4.15, PDF p. 17, require the connection off an
analytic set of complex codimension at least three. A nonempty finite Z
in B has codimension two. Definitions 4.6--4.7/Theorem 4.8 require L2
curvature and bounded contraction for admissible HE correspondence.
Proposition 5.3, PDF pp. 18--21, appears broader; its entire proof invokes
Lemma 5.4, n>2, and the form r_2 omega^(n-3), then Sibony integrability.
That proof supplies no surface case. Do not import its printed statement
unqualified here. This is a source-scope caution, not a counterexample to
the proposition. HTML confirms the codimension inequality, avoiding PDF
text extraction's ambiguous greater-than glyph. No admissibility conclusion
is drawn. If Z is empty the puncture issue disappears; the changed actual
character and ordinary-bundle constraints would still need evaluation.

The author-hosted Bando--Siu paper index (1994, pp. 39--50) was located,
but its image-only pages were not inspectable through this interface;
no original theorem/proof from those images is claimed read. Verbitsky's
precise admissibility statement was inspected as above. This is not an
essential blocker for the algebraic continuation, which uses no analytic
removable-singularity theorem. No exhaustive absence or novelty is claimed.

**Local scope and stopping evidence.** L100's canonical separate audit
(2026-10-14, step 264) is present and preserves geodesy on U, including
Z empty, with no assertion at Z. L068's audited relative-Ext splitting
and compatible index concern an everywhere-stable charge-seven family,
not this family. Reuse its primary tangent/KS and GRR coverage in
[the existing assessment](2026-10-07-charge-seven-parallel-tangent-index.md);
do not import its characters or a global equality-family HE connection.
[ATTEMPTS/063](../../ATTEMPTS/063-singular-metric-local-degree-feasibility.md)
already parks a different singular-metric degree argument.
[ATTEMPTS/065](../../ATTEMPTS/065-equality-determinant-ample-cone-filter.md)
remains the compatible determinant stop. The new comparison identifies a
different precise codimension/dimension mismatch and does not reopen either.

Queries included: “Bando Siu stable sheaves Einstein Hermitian metrics
admissible reflexive extension theorem L2 curvature”; “relative Ext
jumping ranks polystable K3 family tangent sheaf reflexive extension
Bogomolov inequality”; “reflexive sheaves smooth surface restriction
codimension two”; and the exact Verbitsky title. Search snippets were
discovery only. No cross-notebook input was used. Full matching Mathlib
coverage is not checked.

The continuation threshold for an automatic global Chern inequality was
not met. Preserve this stop in ATTEMPTS/066. A different algebraic target
is proposed in
[the extension-and-defect assessment](2026-10-15-equality-relative-ext-algebraic-defect-budget.md).
Its readiness is newly recorded and requires separate approval next turn;
no mathematical specialization has been performed here.

## Original uncovered proposal retained

This is a proposed source question, not an approved mathematical
continuation or an assessment of novelty. No new lemma or Chern
calculation has been carried out for it.

Essential proposed inputs: L071's full negative integral tensor and
actual rank-two character; L097's actual flat family with stable open
B minus Z and possible split fibres L plus L^{-1}; L100's conditional
parallel tangent statement on that stable open. Verify L100's exact
canonical audit scope before using it. L068 is the local methodological
comparison for an everywhere-stable family, not an imported equality
family result. The source review must inspect its limitations and the
recorded equality singular-metric stop ATTEMPTS/063; ATTEMPTS/065
remains the completed determinant stop. No cross-notebook input.

The main gap remains primitive rational Hodge realization. A justified
global deformation-sheaf inequality could constrain existence of this
particular equality kernel independently of compatible determinant
classes. F existence, any extension theorem, stability of an extended
object, control of point-supported corrections, and transverse transport
are unresolved. Z is finite and may be empty; treat both cases without
assuming constant relative Ext ranks, a universal sheaf, image normality,
a smooth split quotient or extension of the L2 metric.

Continuation threshold: inspected primary statements must provide an
actual extension and a testable Chern constraint with the retained
hypotheses, or isolate a narrower independently testable subtarget.
Abandon this proposed mechanism if it merely restates a virtual GRR
identity, needs an unprovided metric-extension theorem, or repeats an
already compatible index. Do not compute a new equality-family lemma
in the approval turn. Full matching Mathlib coverage is not checked.
