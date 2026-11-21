# Simultaneous conjugate-pair orbital response — coverage1213

TARGET: Determine whether an absolute C bounds |E_(k,bvec)(x)|<=C*x*sum_l b_l^2 for every finite m>=1, n>=2m, 0<=k<n and D_bvec=diag(a+i*b_1,a-i*b_1,...,a+i*b_m,a-i*b_m,r,...,r), with a,r,x>0, real b_l and x*sum_l|b_l|<=1/4, using simultaneous block-orientation comparison; prove an explicit uniform C or a rigorously unbounded normalized-defect family with separate rank normalizers.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed source review1213 reuses1204/1208/1209, checks the named local orbital records/stops, and searches the changed joint-orientation/uniform-pair-count scope; exact queries and primary comparisons are in drafts/working/2026-11-17-multipair-orbital-source-review-1213.md. No matching bound or violating family was located; no novelty inference.
SOURCE_EVIDENCE: Inspected Olshanski2013 Corollary3.2 p1017 https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf ; McSwiggen1712.03995v4 Theorem1/(2)/continuation pp2-4,10 https://arxiv.org/pdf/1712.03995v4 ; Collins--Sniady math-ph/0402073v1 Propositions2.2-2.3,Corollary2.4/(9)-(12),Proposition2.5 pp4-6 https://arxiv.org/pdf/math-ph/0402073v1 ; Leake--Vishnoi2004.07403v1 Definition2.2,Theorems4.2/4.5/7.7 and limiting discussion pp8-9,11,29-30 https://arxiv.org/pdf/2004.07403v1 ; Novak2203.10746v1 (1.2)/Theorem1.2 pp2,6 https://arxiv.org/pdf/2203.10746v1 . Reuse C030l/m/n and1204/1209's Sra v3/other asymptotic comparisons; reading and access qualifications are in working1213.
COMPARISON: C030n covers m=1 only. Nested real-array order and exact complex HCIZ identities do not state the joint response bound. Standard Haar polynomial moments cover whole-block orientation integration, while the real gradient oracle is computational and complex nonvanishing retains bounded-field small-coupling hypotheses. None supplies the required nonlinear derivative estimate at unrestricted real contrast.
GAP: A uniform-in-m joint observable/gradient estimate, together with the full-window real nonvanishing justification and separate normalizers, remains unproved. General real parts/backgrounds, actual-Xi scales, all-degree signs and realization remain independent.
REASON: Separate comparison1213 completes essential source coverage for exactly TARGET and permits one later bounded simultaneous-block attempt. Import standard orbital/moment identities by precise citation if used; derive only the missing response control. No new result, counterexample, positivity formula or mathematical approval is asserted in this literature turn.
SCOPE: Finite m>=1,n>=2m, common pair real part a and common remaining rate r; all signs of b_l and a-r, a=r, n=2m, zero phases and rank endpoints. Whole-block orientation under the real reference and C030l comparison are assessed; no complex stochastic order or disjoint-corner independence. Full matching Mathlib coverage unchecked; no cross-notebook input.
LITERATURE_REASON: The invocation-start target changes the approved single-pair scope to arbitrarily many pairs and was REVIEW_REQUIRED. This turn supplies the missing joint-scope comparison while reusing adequate earlier coverage; the next default is mathematics.

## Completed source gate1213

The initial nomination below is preserved as historical motivation.
This completed comparison supersedes its pending-review language;
TARGET and all endpoint/normalization obligations remain unchanged.
Full queries, precise primary hypotheses, applicability differences,
unread optional leads and access qualifications are in
[source review1213](../working/2026-11-17-multipair-orbital-source-review-1213.md).

Olshanski's strict-row statement is a nested leading-corner law;
C030l supplies the already established real-field/weak-row extension.
It does not order all disjoint corners simultaneously. Collins--Sniady's
Corollary2.4 permits finite Haar polynomial orientation moments without
subblock independence. It does not state the needed uniform nonlinear
gradient bound. No such moment specialization or bound was derived here.
Leake--Vishnoi's real-field evaluation oracle and Novak's restricted
complex nonvanishing theorem do not close that gap. The general HCIZ
formula is an imported identity, not a reason to reprove orbital theory.

No inspected source settles the exact bound or refutes this small-phase
family. EXPLORE authorizes one later attempt at the unchanged target:
an explicit absolute C, or a rigorous unbounded normalized-defect
family. Partial uniform estimates may be useful; an m-dependent bound
alone leaves the decision unresolved. Essential inputs are C030l/m/n
and the precisely cited orbital/Haar results actually used. Full-block
2m=n, closed-window nonvanishing, zero phases and the physical derivative
with a,r,bvec fixed require explicit treatment. No joint formula,
complex order, common denominator or Xi realization is assumed.

Recommended next routing: proof_attempt/creative, deep_research/max.
The precise obstruction is a joint orientation/gradient payment with
cost sum b_l^2 and no pair-count loss, where sequential single-pair
payment encounters complex laws. This addresses an unpaid finite
reference ingredient toward the main all-degree Xi sign gap. Its
bounded decisive test is exactly the absolute-C versus divergent
normalized-defect alternative in TARGET. Independent Xi transfer and
realization gaps remain. No further literature cycle is proposed
without a changed hypothesis or a specific essential unread input.

## Definitions and mathematical purpose

Use probability Haar on U(n). For a rank-j orthogonal projection P_j,
define Z_(j,bvec)(x) by integrating
exp(-x*tr(D_bvec*V*P_j*V^*)), and define G_(j,bvec)=-Z'/Z
where nonzero. Differentiation holds a,r,bvec fixed. Set

    E_(k,bvec)=(G_(k+1,bvec)-G_(k,bvec))
                   -(G_(k+1,0)-G_(k,0)).

The reference bvec=0 retains all 2m real entries a, not just two.
Each rank and reference has its own normalization. At n=2m there
are no r entries. A proof must justify reality/nonvanishing on the
whole stated window before using logarithmic derivatives. For the
normalized-defect test take sum_l b_l^2>0; zero phases must be handled
as endpoint cases. No proof or numerical test is performed here.

The main gap is actual-Xi all-degree positivity in L030-L032/C032a.
C030n, now audited, pays a single conjugate-pair perturbation in a
restricted family. The proposed target isolates the next independent
obstruction: whether many correlated phases admit a total cost controlled
by their sum of squares without a loss growing with the pair count.
A positive result could supply an ingredient for a summed finite
reference perturbation; it would not verify the real-reference source
hypotheses, unequal pair real parts, arbitrary remaining backgrounds,
actual zero data, degree/time transfer, theta signing or graph realization.

## Proposed mechanism and bounded decision

Investigate simultaneous orientation averaging inside the distinguished
2m-dimensional block under the positive real reference law, together
with C030l's real-array comparison. The desired new ingredient is a
joint observable/gradient estimate whose cost is controlled by
sum_l b_l^2 with no m-dependent loss. This is a proposed mechanism,
not an asserted identity, inequality or approved theorem application.
The comparison for a leading proper corner does not automatically
cover all disjoint two-dimensional corners jointly; n=2m also needs
its own treatment. No sequential use of C030n under a complex weight,
independence of compressed blocks, common normalizer, or complex
stochastic order is available.

The discriminating test is an explicit absolute C valid for the entire
saved family, or a rigorous sequence with unbounded
|E_(k,bvec)|/(x*sum_l b_l^2). Fixed-m bounds or finite samples would
leave that test unresolved. Preserve partial estimates if one bounded
attempt is inconclusive; do not rebrand an unchanged failed mechanism.
This nomination does not extend C030n or invoke this test now.

The prior stops1117/1181/1193/1200/1107 and overlap884 retain their
recorded scopes. They neither supply the missing joint estimate nor
prohibit its independent finite-family test. Source coverage should
reuse1204 and1208/1209 for overlap, then check the changed pair-count
hypotheses and relevant simultaneous HCIZ/flag comparison results.
Uninspected source leads are not inputs.

## Routing after the source gate

The immediate next turn is literature_comparison, standard/high, for
the exact TARGET. It must decide IMPORT, SPECIALIZE, EXPLORE or a
specific source limitation before research. If a ready assessment
supports this genuinely joint mechanism rather than a known theorem
application, nominate proof_attempt/creative, deep_research/max.

Proposed future escalation: C030n does not pay a growing collection
of pairs because intermediate tilted laws would be complex. Uniform
control of the joint response is relevant to the unpaid pair-summation
step toward all-degree positivity. The bounded test is precisely the
absolute-C versus divergent normalized-defect decision above. Any
m-dependent loss must be exposed. If sources already cover the target,
import/specialize them and route by actual mathematical difficulty
instead of labeling reproduction creative.

Only source coverage blocks that possible creative attempt. The
completed audit1212 is unaffected by this REVIEW_REQUIRED continuation;
no derivation and approval of uncovered mathematics occurs this turn.

