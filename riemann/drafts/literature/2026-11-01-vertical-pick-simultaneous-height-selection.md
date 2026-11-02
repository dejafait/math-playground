# Vertical Pick simultaneous height selection — completed source comparison

TARGET: Test whether L641's count margin and L643's annulus mean permit simultaneous heights X in [T,2T] with dim U_X>=cN and |tau_X|=o(ell_X dim U_X), using L642's complete uniform tail and some fixed c>0.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four saved assessments named below and searched the exact constrained-trace/model-space and local-zero/height-selection terminology; no matching simultaneous actual-Xi theorem was identified. Newly read MIT 6.436J Fall 2018 Lecture 17 p.1 Markov statement/indicator proof and Lototsky's author-hosted RKHS note p.1 theorem/proof, basis formula and projection corollaries. Queries, scope and unread leads are recorded below; no exhaustive search or novelty claim.
SOURCE_EVIDENCE: New: MIT Lecture 17 Section 1 p.1 https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/f44fa78f05ac31a4ba2bd82f599dcf60_MIT6_436JF18_lec17.pdf ; Lototsky, Reproducing Kernel Hilbert Space, p.1 theorem/proof and (1.2)/Corollaries (3)--(4) https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/RepKernHilbSp.pdf . Reused inspected inputs: Bellotti--Wong 2412.15470v2 Thm 1.1 https://arxiv.org/pdf/2412.15470v2 ; Suzuki 2206.03682v4 Section 2.2/(2.6) https://arxiv.org/pdf/2206.03682v4 ; Penrose 1955 Thm 1 pp.406--407/lemma p.408 https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5F4516D6B9989BB6563A4B267CC7D615/S0305004100030401a.pdf/div-class-title-a-generalized-inverse-for-matrices-div.pdf ; Baluyot 2017 Thm 1.2.1 p.16 https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320 . Exact reusable proof coverage is detailed below.
COMPARISON: Markov's inequality and finite orthogonal-projection/Cauchy--Schwarz tools cover the remaining kinds of operation; the saved assessments cover the count, model-space, zero-expansion and density inputs without changed hypotheses. None of these sources states the exact combined conclusion. L641 (11)--(12), L642 (1)--(5) and audited L643 provide locally stated quantitative premises for a joint application, whose relevant proofs still need verification before use. No nested-grid spectral theorem or signed sampling theorem is required by the proposed comparison.
GAP: Prove a positive-measure count-admissible set from L641's average and strict dimension margin, intersect it with a small fixed-E_N annulus-majorant set, justify domination for U_X inside E_N, and retain L642's complete uniform tail and ell_X normalization. Check the relevant L641 proof and the full L642 proof before importing those local conclusions. This review proves none of the combined inequalities or height selections.
REASON: The changed joint scope has now received a separate source comparison. No essential source remains inaccessible; one bounded application of inspected standard tools is ready. SPECIALIZE authorizes only the identified finite/measure specialization with written hypotheses and applicability checks, not a reproof of density/count source theorems, approval of the unaudited local arguments, or a claim beyond known sources.
SCOPE: Exact N=floor(log T), fixed E_N and F_N/W_T of L643, U_X inside E_N with every local actual-Xi value constraint, and the entire mixed tau_X of L642; check L018/L467 conventions and relevant L641/L642 proofs, then test the exact TARGET. Standard Markov, finite spectral/rank/projection and Cauchy--Schwarz arguments are covered. No changed pole array, derivative constraints, RH, simplicity, spacing, positive paired measure or eigenvalue sign is assumed.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changed fixed-space averaging into simultaneous count/trace selection; this completes that missing scope comparison while reusing ready source coverage. Further unchanged-target browsing is unnecessary.

## Completed comparison — 1 November 2026

This is a LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step, actual task
literature_comparison. It makes the unchanged target ready for a research
attempt; it establishes no new lemma, quantitative bound or mathematical
obstruction. No lemmas or mathematical scripts were edited. The prior
nomination is preserved below as historical text, not a current gate.

### Newly inspected standard tools

MIT, *6.436J/15.085J Fundamentals of Probability*, Fall 2018,
[Lecture 17](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/f44fa78f05ac31a4ba2bd82f599dcf60_MIT6_436JF18_lec17.pdf),
Section 1, printed p.1, states Markov's inequality for a nonnegative
random variable: P(Y>=a)<=E(Y)/a, with positive a and finite mean for
the useful finite bound. Read the complete indicator-function proof.
It applies to atomic as well as continuous laws; no density or
independence hypothesis occurs. The intended specialization is the
probability space [T,2T] with normalized Lebesgue measure. Measurability,
nonnegativity and integrability of the actual count and majorant, and
the quantitative intersection of their level sets, must be justified
in the research turn. Markov alone does not supply an Xi theorem.

Sergey Lototsky, [*Reproducing Kernel Hilbert Space (RKHS)*](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/RepKernHilbSp.pdf),
undated two-page author-hosted note, p.1, gives the bounded-evaluation
characterization and its Riesz/Cauchy--Schwarz proof, orthonormal-basis
formula (1.2), and subspace/projection Corollaries (3)--(4). Read these
passages. Use only finite-dimensional closed subspaces with their
inherited Hilbert norm. The unqualified wording about a linear subspace
is not imported for an incomplete subspace. The note's extracted
norm-squared line is garbled and is not an imported identity. The
basis formula and ordinary orthogonal projection give standard tools;
they do not bound the actual mixed exterior trace. The specialization
from E_N to its zero-dependent U_X, including both complex evaluations,
remains to be written and checked. No infinite-dimensional subspace
extension or uniform condition-number bound is needed or asserted.

### Reused primary coverage and exact local scope

The following completed assessments, including their inspected proof
cases and source qualifications, are adequate without reopening their
unchanged manuscripts:

- [Zero count and concentration](2026-11-01-vertical-pick-zero-count-concentration.md):
  Bellotti--Wong v2 Theorem 1.1 p.1 and final height cases in Sections
  3/5, all positive ordinates with multiplicities; Suzuki v4 Section
  2.2, printed p.7, (2.6) and full compensated-expansion proof; the
  finite rational kernels and norm conventions in Baranov--Zarouf v1
  Section 1.1 and Baranov et al. v2 Section 3.1. The source count is
  a cumulative statement, not a same-height selection theorem.
- [Constrained full exterior trace](2026-11-01-vertical-pick-constrained-exterior-trace.md):
  Penrose Theorem 1 and full existence/uniqueness proof pp.406--407,
  including singular cases, and lemma/proof p.408. This allows dependent
  evaluation rows. Boundary Clark/Toeplitz representations and the
  nested-sequence Szego theorem do not supply our mixed trace.
- [Weighted-annulus density comparison](2026-11-01-vertical-pick-density-weighted-annulus.md):
  Baluyot's unconditional Theorem 1.2.1 p.16, uniform sigma>=1/2 for
  fixed theta<4/7, and the inspected near-line cases in Sections 3.2
  and 3.6. Its multiplicities, single logarithm, strict threshold and
  existential onset are unchanged. No general weighted version of
  Maples--Rodgers (19) is imported.
- [Completed L643 audit coverage](2026-11-01-l643-weighted-annulus-audit.md):
  the exact fixed-space majorant and its already audited application
  are retained. Its source arithmetic proofs are imported, not audited
  manuscripts. The joint target adds no density hypothesis.

Local comparison read L018, L467's count statement/application, L641's
definitions, zero-pair/kernel and concentration/count proof through
(13), L642 in full, and L643's hypotheses/conclusion. L643's detailed
weighted proof need not be re-audited for a changed selection scope.
L641 (11) is the recorded dimension estimate with leading coefficient
q_0=(arctan(1/3)+pi/4)/pi; (12) records the height-averaged local count,
and its proof compares that mean with N/pi+O(1). Its strict margin
q_0>1/pi is already proved there. The source review does not infer or
compute a measure proportion from these statements. The relevant
L641 application, including its endpoint/constant claims, remains a
proof obligation before use; its countervector construction is outside
the proposed application.

L642 (1)--(2) records the projection in E_N and the entire mixed trace,
with repeated values and rank deficiency retained. Its proof of (3)--(4)
claims a tail constant independent of X and the constraint matrix;
(5) splits the annulus from the full distant tail. A fixed-N convergence
statement would not replace this uniform claim. The entire L642 proof
remains to be checked before that claim is used. L643 supplies the
audited fixed-E_N mean O(N^(159/80)), not a selected-height trace.
These observations identify existing premises and the difference to
derive; they do not verify the combined application in this turn.

### Duplicate/failure check, bounded test and downstream use

Scoped searches of the vertical-Pick assessments and L641--L643 found
no already written simultaneous-height proof. The two preserved stops
are the [boundary-paired transfer countermodel](../../ATTEMPTS/2026-11-01-vertical-pick-boundary-paired-transfer-stop.md)
and the [deterministic annulus envelope failure](../../ATTEMPTS/2026-11-01-vertical-pick-constrained-trace-annulus-inconclusive.md).
Their conclusions are unchanged. The first uses a permitted test pair,
not asserted Xi zeros, and countervectors not known to lie in U_X.
The second fails to upper-bound the annulus at the required scale;
it is not a trace lower bound. The new retained input is L643's actual
zero-density mean, rather than another deterministic boundary-transfer
claim. Prior arithmetic and budget stops remain in force for their
specific mechanisms. No exploration counter is reset by this review.

Continue only if the next attempt verifies its local inputs and proves
the stated simultaneous dimension and normalized full-trace conclusions,
or identifies a precise failing quantitative premise. It must establish
a fixed positive-measure count-admissible set and an intersecting
small-majorant set, with all boundary occurrences, zero orders and both
displacement signs. State any chosen count threshold, measure fraction
and vanishing trace threshold explicitly in that later proof. Include
the full distant tail, the projection inside E_N and uniform ell_X
normalization. No continuity of the changing rank or spectral gap in
the evaluation matrix may be silently assumed. This review chooses no
new parameter value and proves no selection inequality.

The plausible downstream use is the normalized Rayleigh diagnostic
already described conditionally in L642's last proof paragraph.
Small signed trace alone does not place an eigenvalue near zero in
absolute value. Spectral signs, realization and global initial signs
remain independent gaps. The exact main RH gap is unchanged. If a
load-bearing premise fails, retain that evidence and reassess this
application; success of its mean prerequisite does not guarantee it.

### Search record, leads and routing

New queries included `"Markov inequality" nonnegative random variable
proof site:ocw.mit.edu`, `"zeta" "model space" "trace" "zeros"
interpolation`, `"Riemann" "simultaneous" "height" "trace" zeros`,
`"zeta" "constrained trace" "model space"`, `"Riemann" "local zeros"
"Markov" "trace"`, and `"reproducing kernel" "subspace" "orthogonal
projection" "Cauchy"`. Exact joint searches identified no matching
primary theorem; broad results were largely irrelevant. This is a
bounded comparison, not evidence of originality. Only the two named
primary teaching sources were newly inspected for operative tools.
Other RKHS/interpolation theses and effective-interpolation search hits
remain unread leads and are not mathematical inputs. A 2025 journal
Szego hit is not imported; the previously inspected version's scope
comparison suffices. No source-access blocker or cross-notebook input.
Full matching Mathlib coverage is unchecked, not asserted absent.

Ready continuation: the exact TARGET above, as established-route
proof development (REPRODUCTION if undertaken under SPECIALIZE).
Its difficulty is checking the mixed trace, uniform complete tail and
zero-dependent constraints together with the measure argument. No new
signed-cancellation idea has been identified that warrants creative
routing; manufacturing one would bypass the concrete pending use of
the retained mean. No additional literature turn is mathematically
needed if this unchanged coverage is accepted.

## Original nomination (preserved; completed comparison above controls)

The next invocation is literature-only because DECISION is
REVIEW_REQUIRED. Begin with the existing assessments, not a repeat
search for unchanged density or rational-kernel theorems:

- [Zero count and concentration](2026-11-01-vertical-pick-zero-count-concentration.md).
- [Constrained full exterior trace](2026-11-01-vertical-pick-constrained-exterior-trace.md).
- [Weighted-annulus density comparison](2026-11-01-vertical-pick-density-weighted-annulus.md).
- [Completed L643 audit coverage](2026-11-01-l643-weighted-annulus-audit.md).

The exact proposed objects remain those of L641--L643: N=floor(log T),
the fixed E_N, U_X obtained by all local actual-Xi value constraints,
and tau_X the full exterior mixed trace. Essential local inputs are
L018, L467, L641, L642 and L643. Count zero orders, both horizontal
displacements and local boundary occurrences; repeated values are not
derivative constraints. No simplicity, RH, favorable spacing, positive
paired measure or spectral sign is to be assumed.

The bounded test is whether the count argument supplies a set of
heights of measure at least a fixed positive fraction of T, on which
dim U_X is at least a fixed positive fraction of N, and whether that
set can meet the small-majorant set with the complete tail retained.
Existence of one favorable height alone is insufficient. Do not replace
the zero-dependent projection by an unconstrained boundary projection,
or use a small signed trace to assert a small eigenvalue in absolute
value without a separate spectral argument. The target is only the
stated dimension and normalized trace conclusion.

Continue only with a proof of those simultaneous conclusions or a
specific failing quantitative premise. Preserve the boundary-transfer
countermodel and deterministic-annulus failed upper-bound certificate;
the new input relative to those attempts is L643's retained density
mean, not a renaming of their mechanisms. No such selection proof is
written in this nomination. Mathlib coverage of the combined target
is unchecked.

This is established-route development after coverage, not a creative
signed-cancellation mechanism. No concrete new sign mechanism is
justified by the audit, so creative routing is not manufactured to fill
a scheduling target. A separate review may approve reuse of the saved
primary coverage without reopening unchanged source manuscripts.
