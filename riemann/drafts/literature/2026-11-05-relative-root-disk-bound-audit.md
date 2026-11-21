# Uniform relative root disks — approved critical-audit scope

TARGET: Audit L793's explicit epsilon(d,Q) and all-root proof against the inherited componentwise perturbation and Rouche source cases, including arbitrary root scales, varying leading coefficient and d=1.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step490/491's completed finite componentwise/pseudozero and disjoint-disk comparison in 2026-11-05-mesh-losing-root-disk-tolerance.md and 2026-11-05-mesh-losing-root-disk-specialization.md; step493 reopened both direct author PDFs and checked the unchanged theorem statements and conjugation case, without a new broad search.
SOURCE_EVIDENCE: Graillat--Langlois P32, 6 January 2004, https://perso.lip6.fr/Stef.Graillat/papers/P32.pdf , Theorem3/proof pp.6--7 and Corollary5 p.9 eq.(8); Alexanderian, 28 January 2022, https://aalexan3.math.ncsu.edu/articles/polyroots.pdf , Theorem2.2 pp.1--2 and Theorems3.2/3.5 proofs pp.3--5. The complete relevant cases were inspected in step490 and direct author URLs recovered in step491.
COMPARISON: L793 specializes the reviewed all-coefficient boundary certificate and standard disk/conjugation mechanism; its explicit uniform d,Q estimates require a separate proof audit, not a new general perturbation theorem or repeated literature search.
GAP: Independently check L793's elementary majorant identity, pairwise separation, each boundary factor, strict Rouche inequality at non-strict coefficient bounds, leading coefficient, degree exhaustion, conjugation, positivity and the empty product when d=1.
REASON: Separate literature-only step493 approves this exact audit scope under unchanged source hypotheses; adequate inherited coverage is reused, and the audit itself remains unperformed.
SCOPE: Real polynomials of exact integer degree d>=1 with positive simple roots and consecutive ratios at least Q>1; real perturbations of degree at most d with every coefficient controlled. No optimality, same-Q output, actual-Xi comparison or growing-degree signs.

No source hypothesis has changed from the prior approved assessment.
The first assessment's discussion of complex pseudozeros permits only
the sufficient exclusion direction for real perturbations, which is
all L793 needs. Alexanderian's monic absolute-perturbation theorem
alone is not an all-coefficient relative theorem; use the cited Rouche
theorem and the all-coefficient certificate together as before.

The proposed audit imports the general theorems rather than reproving
them. Check the complete canonical proof in
`lemmas/L793-uniform-relative-coefficient-root-disks.md`, with h=(Q-1)/(Q+1)
and eta=h/2. Its explicit lower bound is a local specialization, not
a certified novelty assertion. Compare each needed source hypothesis
with the saved complete source evidence; a snippet or preview is not
a replacement for that evidence. Mathlib coverage remains unchecked.

Accept the finite input only if every boundary circle has the claimed
uniform factor and exactly one simple positive perturbed root under
all stated edge cases. Otherwise isolate the failed inequality or
hypothesis and preserve the producing proof as unaudited work.
This audit does not certify any actual residual meets the tolerance.

Main gap: actual-Xi all-degree mixed positivity. Essential input for
this audit is L793 and the above primary source cases; no other local
lemma is a premise of L793, so its DAG row is empty. Context L791/L792
and L778/L018/L021/L776 is needed only for any future actual-model use,
which still retains exact F_j=R_j through4, S=B R1, t_m,t_a,delta>0
and complete widths/analytic/software contracts. C792a and unaudited
C792b remain route evidence, not premises. Growing-degree model
existence/separation, actual residual bounds and signs remain open.
No cross-notebook theorem is used.

This nomination reuses ready coverage, but is newly written and has
not received its separate continuation approval. Routine audit routing
is standard/high, with no claim that this is a creative central mechanism.

## Separate approval — step493, 2026-11-05

The required separate literature turn is complete. The nomination-timing
statements above are historical and are superseded here: SPECIALIZE is
ready for precisely TARGET and SCOPE, with no additional review prerequisite.
This approves source coverage, not L793's proof or its explicit constant.

LITERATURE_REASON: The supervisor explicitly required separate approval of
the newly written audit continuation; no changed mathematical hypothesis
or fresh discovery search justified additional literature work. Direct
URLs were reopened to confirm the source cases, while the complete
step490 proof inspection and search/overlap comparison were reused.

Primary-source checks: Graillat--Langlois Theorem3 pp.6--7 and Corollary5
p.9 eq.(8) retain the weighted all-coefficient setting, including index n.
The source allows complex perturbations; only sufficient exclusion is
imported for the real subclass. Positive weights must be justified from
L793's hypotheses during the audit. Alexanderian Theorem2.2 pp.1--2
requires strict boundary domination and counts multiplicities. Its
Theorem3.2 p.3 is monic and absolute, so it cannot alone justify varying
leading coefficients or the relative norm. Theorem3.5 pp.4--5 uses real
coefficients and a multiplicity-one conjugation-invariant disk count;
its proof's word “p” for the conjugate root is a typo, since the displayed
identity is for q. The general Rouche theorem, rather than a silent
extension of Theorem3.2, is the authorized input. Arbitrary scales, varying
leading term and d=1 remain explicit local audit obligations. No new
inequality or specialization was proved in this approval.

Local overlap/failure comparison reuses the completed step490 assessment
and the scoped step489/492 histories. Universal/same-mesh stops do not
exclude mesh-losing finite certificates and are not reopened. No new
claim of novelty or Mathlib coverage is made. Mosier remains unread and
unnecessary; there is no essential source blocker.

Outcome STALLED: the approval repeats the adequate source decision and
repairs continuation readiness, rather than adding mathematical evidence.
The main gap, downstream residual-comparison use and accept/reject test
remain exactly those specified above. No lemma, script, PROOF or DAG was
changed. The next turn should perform the saved audit, not another source
approval. A central creative attempt still lacks an independently justified
model/separation/residual mechanism; this routine audit is not relabeled
creative to satisfy scheduling preferences.
