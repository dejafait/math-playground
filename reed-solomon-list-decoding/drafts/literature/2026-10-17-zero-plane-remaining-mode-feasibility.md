# Remaining modes and moment signs — full-domain feasibility scope approved

TARGET: Determine whether L084's equality parametrization admits nonnegative eight/eight moments satisfying all 53 remaining original modes on L076's full domain with t78=s.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 297 compared L084/L083/L078, the ready equality and fixed-seven-point inequality assessments, and ATTEMPTS/052–053,060–066; searched joint parametric feasibility, SDP weak duality, exact rational certification and the specific RS/Schrijver completion terminology. Fresh primary sources and unread leads are distinguished below; no duplicate full-domain verdict was found, without a novelty inference.
SOURCE_EVIDENCE: Reuse foundations/04,09,10,12 and the step-295 equality assessment's Schrijver/Sano/Polak/Ye/Goemans coverage. Freshly read Vandenberghe–Boyd (1996) Sections 1.1 (1)–(6), 3.1 (27)–(32), Theorem 3.1 and its following counterexample; Kolmogorov–Naldi–Zapata arXiv:2405.13625v3 Sections 3–4 hypotheses, Algorithm 4.1, Lemma 4.1/proof, Definition 4.2, Theorem 4.3 and complete proof. Precise citations, limits and comparison-only leads appear below and in foundations/10.
COMPARISON: Standard affine-LMI feasibility and weak-duality certification cover a joint test before nonlinear equality elimination; L084 supplies the complete equality parametrization for checking the result. A fixed-parameter LP alternative does not decide existence over three varying parameters. General SDP theory supplies neither these coefficients' verdict nor guaranteed rational certificates or strict separation on a singular face.
GAP: Perform one bounded joint full-domain feasibility attempt, retaining all 85 original domain rows, 45 moment signs and 81 modes (the 28 selected equalities and 53 remaining inequalities), and certify any conclusion in original/raw coordinates. No coefficient calculation, witness, new separator or verdict is supplied by this review.
REASON: The essential known-method coverage is sufficient for one REPRODUCTION calculation on exactly TARGET; specialize the affine block formulation and exact certificate checks without reproving general theorems. No essential source blocker remains.
LITERATURE_REASON: The saved continuation adds all moment signs and remaining inequalities while varying three column parameters; the prior ready review covered only signed equalities, and the older Farkas review fixed the column. This separate gate compares the missing joint feasibility scope and singular-certificate limitations.
SCOPE: Exactly L076's original full domain with t78=s, L075's unchanged dictionary, L084's complete equality solution space, original pairs and included-anchor five/six/seven/eight modes; no scalar upper rows, other anchors, new base/pairs or global feasibility.

Step 296 proposed this continuation without approving or testing it.
Step 297 supplies its separate literature approval. No new mathematical
result, coefficient calculation, optimization run or completion is claimed.
The step-296 result and its pending dedicated critical audit are preserved.

Essential inputs: L021,L053,L073,L075,L076,L078,L079,L081,L082,L083,L084;
foundations/09,10 with foundations/04,12 qualifications; complete
zero-plane-positive-mode-compatibility-{results,verification}.json and
their step-290,292,294 upstream certificates/recipes. Keep original rho,
p8, pairs, seven-column RREF/completion, all 500 types/3000 presentations,
36 forced and 45 free entries, 90 weighted kernel equations, singular
and empty mode ranges, coherent normalization and full anchor. L084's
arithmetic verification is complete; its separate critical proof review
remains pending, as do ancestor reviews outside their imported scope.

Potential use: decide this included-anchor joint matrix prescription or
find a relevant obstruction on its whole zero plane. Passing would park
only this diagnostic; exclusion would concern this pair/base/family only.
Scalar upper rows, other anchors, global moments, other pairs/bases and
RS realization remain independent gaps. The main boundary is unchanged.

## Main gap, intermediate use and prior failures

The main gap is arbitrary-center safety at 67/68 agreements; the finite
bracket remains 955–957. The intermediate target is simultaneous
feasibility of this one included-anchor prescription on the necessary
zero plane. A passing assignment would park this joint PSD diagnostic
and could support a separately assessed scalar or other-anchor test.
A whole-domain exclusion would park this pair/base/column family only.
Neither outcome proves RS safety or unsafety.

ATTEMPTS/052–053 record that a signed equality pass can precede a
remaining-mode rejection at one fixed seven-distance column. That ready
assessment is reused for fixed-parameter LP certification, not extended
to parameter variation by assertion. ATTEMPTS/060,062,064 reject three
different eight-distance points; 061,063,065 stop the respective old
weights as family exclusions. L083 confines any completion to t78=s;
L084 and ATTEMPTS/066 stop equality-only exclusion there. These do not
settle the combined 45-sign/53-mode target. The new attempt must solve
one joint model, rather than repeat isolated-point separator searches.

## Known results and specialization limits

Reuse Schrijver, DOI 10.1109/TIT.2005.851748, Proposition 5 (44)–(47),
Theorem 1 (51), III.A (52)–(59), III.B (64), printed pp.5–7;
Sano, DOI 10.1007/s44146-026-00231-y, Section 2 Corollary 2.2,
Theorem 2.6 and Lemma 2.7; Polak arXiv:1703.05171v1 Sections 1.1–1.2;
Ye October 2017 Theorem 1.11 p.13, Section 1.5.1 pp.23–24 and Section
2.3 opening p.42; and Goemans's 19 September 2001 MIT Lecture 3,
Theorems 1 and 3, pp.1–2. Their precise URLs, inspected proof cases
and qualifications are already in foundations/04,09,10,12 and the
ready step-295 assessment. This turn reuses those inspections. The
mixed-layer and whole-kernel contracts remain qualified imports, not
newly audited premises. No source theorem requires a representing
measure for this ordinary slice; no actual-label symmetry is added.

Fresh primary input: Lieven Vandenberghe and Stephen Boyd,
*Semidefinite Programming*, SIAM Review 38(1) (March 1996), 49–95,
DOI 10.1137/1038003,
[author-hosted published PDF](https://web.stanford.edu/~boyd/papers/pdf/semidef_prog.pdf).
Read Sections 1.1 (1)–(6), pp.49–51; 3.1 (27)–(32), pp.63–64,
including the complete trace proof; Theorem 3.1 and its following
finite-gap example, pp.64–65. Affine symmetric LMIs define a convex
feasibility problem; scalar affine inequalities can be diagonal blocks.
The trace argument certifies bounds without strict feasibility. Theorem
3.1 instead has strict-feasibility hypotheses, and its proof is referred
elsewhere; neither that theorem nor those unread references are needed
for the proposed certificate check. No exact-solver guarantee is imported.

The intended specialization uses the original affine symmetric mode
blocks, with the old base fixed and the common column and new moments
variable. L083 already records the affine cross vectors, constant old
blocks and quadratic generalized-Schur bounds. Reconstruct and check
these original blocks before invoking the joint model. L084's complete
parametrization is the established translation for later verification.
Do not infer convexity of the polynomially substituted (q,h) description
from the convexity of the original affine-LMI description. Do not use a
fixed-point LP theorem as a quantifier-elimination theorem for all q.
No local coefficient identity or new convexity lemma is proved here.

Stronger certification comparison: Vladimir Kolmogorov, Simone Naldi
and Jeferson Zapata, *Certifying solutions of degenerate semidefinite
programs*, [arXiv:2405.13625v3](https://arxiv.org/pdf/2405.13625v3),
25 April 2025, Sections 3–4, pp.6–9: hypotheses P nonempty and maximum
rank r>0, Algorithm 4.1, Lemma 4.1 and proof, Definition 4.2, Theorem
4.3 and complete proof. Its isolated-solution certification needs
proximity to a maximum-rank feasible solution and valid column choices;
the proof uses a local face and an invertible subsystem. These premises
are not known here. The theorem supplies no feasibility verdict from
an arbitrary approximate point. The opening irrational-solution warning
also precludes assuming rational rounding must succeed. Its algebraic
algorithm is a comparison, not imported for execution in this attempt.
An initial v2 HTML lead used different theorem numbers; all references
here use the inspected v3 PDF, not the HTML's inconsistent date line.

Other leads inspected only at statement level: Klep–Schweighofer,
[arXiv:1207.1691v1](https://arxiv.org/pdf/1207.1691v1), Section 4.3,
Corollary 4.3.1, Definition 4.3.2 and Theorem 4.3.3, pp.16–17,
give a stronger nonlinear infeasibility-certificate framework. Its
supporting proofs were not fully inspected and no SOS algorithm or
completeness claim is imported. Ramana/facial-reduction references in
Vandenberghe–Boyd remain unread leads. The UCLA duality-report URL
returned an access error; it is nonessential to the inspected trace
argument. No persistent source blocker is being used to delay mathematics.

Grone–Johnson–Sa–Wolkowicz's Proposition 2/Theorem 7 comparison in
foundations/10 is unchanged: unrestricted free-entry completion does
not enforce this moment dictionary, and no chordality application is
available. General and supporting Mathlib coverage for joint exact SDP
certification is not checked; unknown availability is not absence.

## One bounded research contract and stopping test

Use all three parameters (t56,t63,t69) on the exact plane t78=s and
all 45 original z variables for one joint affine-LMI feasibility model.
Retain all 85 original factors, every raw moment sign, and every original
mode. Keep the selected 28 rows through the full PSD constraints; use
L084's equations and z=P(q)+N*h to check any recovered solution. They
must not be replaced by a sample, a parameter box or endpoint segment.
All full-key, range, empty-mode and full-anchor contracts above remain
part of the model and its exact verification.

Allow one numerical conic feasibility run with an iteration cap recorded
before execution, followed by one exact certificate-reconstruction and
verification pass. Numerical computation only proposes candidates. Use
available local tools without credentials, paid services or new dependencies
requiring approval. No arbitrary big-M bounds may restrict the full-domain
model; no unrestricted nonconvex search or repeated point scan is approved.
Removing fixed zero directions is allowed only with a checked congruence
preserving the entire original problem; a guessed numerical kernel is
insufficient. A local formulation error must be repaired before interpreting
solver output, and no assertion of Slater or exact attainment is permitted.

Accept a rational feasible assignment only after checking all 85 domain
rows, 45 signs, 28 selected original equalities and 53 remaining modes,
all forced entries, original/raw scaling and every inherited range/key
identity. Retain all 81 original inequalities in the verification.
A fixed rational column chosen solely to reconstruct this joint candidate
may use the already assessed finite LP method; failure at that rounded
point says nothing about the full plane. No rational witness is promised.

Alternatively accept exclusion only from an exact original-coordinate
certificate valid for the entire domain, such as PSD trace multipliers
with all variable coefficients cancelled and a strictly contradictory
constant, retaining domain/sign multipliers and plane equalities with
their correct orientations. Verify every coefficient and PSD/sign
condition; supply the translation from any reduced coordinates. A
separator at a sampled point is insufficient. Weak duality certifies a
found certificate, not its existence. Do not infer a general SDP Farkas
alternative from the earlier LP source.

If neither certificate is reconstructed within this one bounded attempt,
save the model, proposed data, failed residuals and precise obstruction;
report EXPLORATION (or STALLED if there is no new evidence), rather than
feasibility or infeasibility. Reassess a concrete failure before another
attempt; algebraic certification or new facial reduction needs its own
separate assessment if selected. A pass parks only this diagnostic; a
certified exclusion parks only this family. Independent global, other-anchor,
scalar-upper and RS gaps remain.

Search queries on 2026-10-17: “Vandenberghe Boyd semidefinite programming
feasibility weak duality strict feasibility 1996 pdf”; “parametric quadratic
linear inequalities semidefinite feasibility Schur complement”; “Reed
Solomon zero plane completion Schrijver”; “semidefinite programming rational
feasible irrational exact certificates”; and “Schrijver parametric completion
constant weight”. Primary theorem text, not snippets, supports the imports.

Step 297 is LITERATURE / REPRODUCTION, outcome EXPLORATION: a new scope
comparison and bounded test are recorded, with no mathematical advance or
novelty claim. Mathematical exploration usage remains 0/3. No lemma,
mathematical script, PROOF.md or DAG.md is changed by this approval.
