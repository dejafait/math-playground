# Global deformation germ reducedness — completed source comparison

TARGET: Assess whether the fixed-determinant Kuranishi germ of F must be reduced under L181's exact rank-two K3-product hypotheses.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 616 performed the bounded exact/stronger-result and obstruction queries recorded below; reused the step-540 formality assessment and step-615 local failure screen, and read L116/L181 hypotheses and the relevant ATTEMPTS/094,/096 passages. No matching full-germ reducedness theorem or exact-family counterexample was established; this is not a novelty claim.
SOURCE_EVIDENCE: Inspected Verbitsky alg-geom/9307008v1 (29 July 1993), Section 6, Theorems 6.1–6.3 and the intervening reduction convention, PDF pp.22–24; Theorem 7.1 and its local-family implication/(7.3)–(7.4), PDF pp.26–28. Inspected Miyajima, Publ. RIMS 25 (1989), 301–320, Definitions 1.1,1.5–1.7, Theorem 1/Lemma 1.7, Proposition 2.3(2), Theorem 3 and proof, Proposition 4.2 and its slice comparison, pp.303–307,312,314–319, DOI 10.2977/prims/1195173613. Rechecked Meazzini–Onorati 2509.03180v1, Definition 5.1/Remark 5.3, Theorem 5.5 and entire proof, p.20; Bottini 2608.24860v1, Theorem 1.1 for scope only.
COMPARISON: Verbitsky's Spl(F) is explicitly the reduction before the local-cone and hyperkähler statements. Miyajima's analytic/algebraic and connection comparisons retain possible nilpotents. The product-applicable Meazzini–Onorati theorem supplies formality, not reducedness. None supplies the proposed full determinant-fixed assertion, even with L181's retained obstruction input.
GAP: Reducedness and nonreducedness of this exact germ remain undecided. No determinant-slice comparison, local-ring calculation, new t bound or exact-family counterexample is proved. L182's separate audit also remains pending.
REASON: New primary source-scope evidence changes the route: park reducedness-only exclusion unless materially new geometric input is supplied. EXPLORE records the bounded unmatched search, not permission to assume reducedness or repeat the same search. Resume independent, already covered L163 critical-audit work; no research is performed here.
SCOPE: Keep the full L181 family on the identical marked K3 product, locally free product-polystable rank-two F, integral c_1=0, full ch=2-14e_1-21e_2-tau_D+62P, common metric/triple/forms/hyperholomorphic connection, charge-21 restriction stability, actual j,r,a,J,Phi_1 and full W over finite possibly empty reduced Z; H^0(X,End_0(F))=0 from L116 and even 0<t<=38. Fix determinant; do not replace the germ by its reduction or assume smoothness or section integrability.

LITERATURE_REASON: The changed target concerns the actual global deformation germ's nilpotent structure, essential coverage absent from the ready cubic and product-formality assessments. L181's injective obstruction provides a new discriminating input, while L182 closes the universal-cubic route. Reuse formality coverage; inspect only genuinely needed reducedness results and their hypotheses.

## Invocation-start nomination and downstream use (preserved)

The main unresolved target is uniform primitive Hodge realization;
existence of the hypothetical equality kernel is independently open.
The new intermediate question is whether the determinant-fixed
deformation germ of this particular F is reduced as an analytic germ
or scheme, with its deformation-theoretic structure retained. A positive
answer could make L181's injective quadratic obstruction restrictive
enough to force t=0. That bridge, including its precise obstruction
map and local-ring consequences, is proposed for later justification;
no local-ring calculation is performed now. Even a successful t>0
exclusion would leave t=0, F existence, other stable types, transport
and algebraic-cycle realization unresolved.

Essential local inputs for assessing applicability are L116, L163,
L181 and L182. Preserve the actual global determinant-fixed group,
not a deformation space of a surface restriction. Trace-free
infinitesimal automorphisms vanish by L116; whether and how a cited
stable/simple-bundle theorem applies must be justified under the
polystability hypothesis, not silently strengthened. Keep stacks,
semiversal bases and coarse moduli germs distinct, and record which
one carries the proposed reducedness assertion.

The new evidence motivating this proposal is L181's full injective
bracket, not hyperholomorphicity alone. The older mixed-eigenspace
assessment correctly parks vanishing inferred from formality. It
also records an obstructed hyperholomorphic example, so generic
smoothness or unobstructedness is not an admissible substitute for
the narrower question. No theorem about reducedness has been imported.

## Bounded review and continuation test

Search exact terminology for reduced Kuranishi germs of simple
rank-two hyperholomorphic bundles on compact hyperkähler products,
stronger reducedness results, and nonreduced examples with matching
rank/base/connection hypotheses. Retrieve primary theorem statements
and the proof cases needed to decide whether nilpotents are retained.
Reuse the existing product-formality source assessment rather than
repeat that search. Its cited passages are leads for this changed
question until checked for the needed claim.

Continue only if a primary theorem covers reducedness of the full
germ under the retained hypotheses, or supplies a concrete separately
testable geometric criterion in this family. An exact-family
counterexample is informative negative evidence. If results merely
describe a quadratic cone, the underlying point set, the reduction
by definition, an irreducible base, or smooth K3 surface moduli,
record the precise difference and park reducedness-only exclusion.
Do not infer it from formality or spend another mathematical turn
rewriting cubic/trace identities. This review authorizes no proof or
new mathematical script. Full matching Mathlib coverage is not checked.

## Completed review — step 616, 2026-10-29

Outcome NEGATIVE / LITERATURE / REPRODUCTION; actual task
literature_comparison. The new evidence is an explicit primary
reduction convention and comparisons that preserve possible nilpotents.
This changes the route, not the mathematical bound. No theorem proving
or disproving this family's reducedness is claimed. No lemmas or
mathematical scripts change; PROOF.md and DAG.md need no alteration.
The historical nomination above is retained; its pending-review routing
is superseded by this completed comparison.

### Primary scope and essential proof cases

M. Verbitsky, *Hyperholomorphic bundles over a hyperkähler manifold*,
[alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993: Section 6 distinguishes the full coarse stable-deformation
space in Theorem 6.1 from its reduction Spl(F), immediately afterwards
(PDF p.22). Theorems 6.2 and 6.3 concern Spl(F). The proof implication
after Theorem 7.1 constructs a family from harmonic inputs of zero
Yoneda square; (7.3)–(7.4) give its recursion (PDF pp.26–28).
Section 9's opening and tangent-sheaf argument also use Spl(B).
Thus the cited statements do not assert that the full moduli germ is
reduced. Even granting the stable-bundle hypothesis would not remove
this distinction. No upgrade of the given polystability is made here.
This is a scope qualification to the reused formality source notes,
not a reproof or a claim that the reducedness assertion is false.

K. Miyajima, *Kuranishi Family of Vector Bundles and Algebraic
Description of the Moduli Space of Einstein-Hermitian Connections*,
Publ. RIMS **25** (1989), 301–320,
[DOI](https://doi.org/10.2977/prims/1195173613),
[primary PDF](https://ems.press/content/serial-article-files/42477).
Theorem 1 treats bundles on a compact complex manifold. Definition 1.1
uses the generated equation ideal; Lemma 1.7 compares ideals, not just
zero sets (pp.303,306–307). Proposition 2.3(2)'s proof uses Artinian
bases (p.312). Theorem 3 compares the analytic and algebraic simple-bundle
moduli over a projective manifold, retaining nonreduced structures;
its proof uses local universal families and GAGA (pp.314–315).
Proposition 4.2's Kähler connection comparison likewise retains them:
the slices carry the same equations (pp.316–319). These comparisons
do not eliminate nilpotents or prove a determinant-fixed slice reduced.
L116 records the trace-free automorphism vanishing relevant to simplicity;
no further stability or fixed-determinant identification is inferred.
J-STAGE follow-up requests timed out; the publisher's EMS copy resolved
access, so no essential source blocker remains.

F. Meazzini and C. Onorati, *Deformations of twisted sheaves and
formality results*,
[2509.03180v1, Section 5](https://arxiv.org/html/2509.03180v1#S5),
3 September 2025, Definition 5.1, Remark 5.3, Theorem 5.5 and full proof
(PDF p.20): the compact hyperkähler base need not be irreducible.
A metric projectively hyperholomorphic locally free twisted bundle
has formal endomorphism Dolbeault DG Lie algebra. The proof verifies
derivations, the two differential identities and the strong differential
lemma. The retained product metric/triple, trivial twist and actual
hyperholomorphic connection match that scope. Neither the conclusion
nor these proof cases assert reducedness. No new trace-free formality,
determinant-slice theorem or local-ring specialization is derived.
The irreducible-base 2022 theorem in the reused assessment is not
silently extended to the product.

A. Bottini,
[2608.24860v1](https://arxiv.org/html/2608.24860v1),
25 August 2026, Theorem 1.1, was rechecked only for its conclusion:
a nonzero tangent-bundle Yoneda square on a Kum_2-type fourfold.
This rank-four irreducible-base singularity statement is neither
an exact-family counterexample nor a nonreducedness theorem.
The prior assessment retains its separate proof-case notes.

### Discovery, overlap and decision

Queries actually run were `Verbitsky hyperholomorphic bundles "reduced"
deformation Kuranishi`, `hyperholomorphic bundle moduli "non-reduced"
Kuranishi`, `"Kuranishi" "reduced" "hyperkähler" bundles`,
`"hyperholomorphic" "moduli" "reduced"`, `"hyperholomorphic"
"nonreduced"`, `"hyperholomorphic" "non-reduced"`,
`"hyperholomorphic" "reduced" deformation germ rank two`,
`"K3" "product" "bundles" "nonreduced"`, `"hyperholomorphic"
"nilpotent" moduli`, `"Kuranishi Family of Vector Bundles" Miyajima
theorem 3`, `"hyperholomorphic" "moduli" "nilpotents"`,
`"hyperholomorphic" "reducedness"`, and `"hyperholomorphic"
"reduced scheme"`. Search hits concerning Charles's thesis/paper,
Higgs moduli and deformations of underlying manifolds were discovery
leads only, not theorem inputs. No snippet or failed search establishes
reducedness, its failure or originality. No claim of exhaustive
literature coverage is made.

The exact target was full-germ reducedness, not merely the formal
quadratic presentation already assessed. The distinction above is
new source evidence for parking this route. L181's injective bracket
and L182's claimed redundancy are unchanged; no additional bound on
t or s follows from this review. ATTEMPTS/094's cyclicity stop and
ATTEMPTS/096's formal-witness limitation remain in force. Reopening
requires a materially new, applicable geometric assertion retaining
the full germ and fixed determinant, with an independent test.

The independent pending L163 audit has unchanged, invocation-preexisting
SPECIALIZE coverage in
`2026-10-25-adjoint-factor-cup-critical-audit.md`; its exact TARGET is
reused in PROGRESS.md. Its original unknown-t scope is retained rather
than replacing a premise by L181's later bound. This is a recommendation
for the next mathematical turn, not an audit result. It could validate
or repair a load-bearing positivity input for L180–L182, while leaving
F existence, t=0, other stable types, transport and cycles unresolved.
Full matching Mathlib coverage remains not checked.
