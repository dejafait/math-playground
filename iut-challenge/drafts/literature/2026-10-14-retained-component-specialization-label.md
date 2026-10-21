# Retained cusp label through component specialization — source scope ready

TARGET: Test whether L053's Q translates L056/L057's retained seven-cycle by one adjacent component, using Tate isogenies, split-node resolution and contraction over unchanged N.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 211 searched Tate component specialization, generalized-elliptic contractions and split-node resolution; compared L053,L056,L057 and ATTEMPTS/031 with steps 204/206. Exact queries, discarded leads and inspected cases: drafts/2026-10-14-retained-component-specialization-source-review.md.
SOURCE_EVIDENCE: Direct sources: https://johncremona.github.io/papers/component.pdf ; https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf ; https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf ; https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf ; https://arxiv.org/pdf/1511.07475v2 ; https://math.stanford.edu/~conrad/papers/kmpaper.pdf . Read Cremona section 2.1 theorem/proof pp.2–3; Tate's Isogenies theorem/proof pp.16–17 and differential identity p.15; Liu 2006 Example 8.3.53 pp.365–367, Lemma 10.3.21 pp.513–514 and Corollary 10.3.25 p.515; Conrad 2015 Proposition 3.7, Theorems 3.10,5.4; Cesnavicius arXiv:1511.07475v2 section 3.2.1 and polygon actions; reused/reinspected Conrad 2006 Theorem 2.5.2. Full citations/hypotheses/version qualifications are in the source review.
COMPARISON: Known inputs cover algebraic representative power isogenies, component homomorphisms, resolution of split thick nodes and uniquely specified contractions. Their actual-map specialization is distinct from the parked atlas mechanism; the retained component order, contraction and translation action still require proof, and no native label is imported wholesale.
GAP: Match the source algebraic isogeny with the actual power map; identify the retained model as the relevant regular-model contraction, track its origin and marked strict transforms, and verify cyclic order and translation equivariance before using L057's c. No adjacent-component identity is established by this assessment.
REASON: Essential general source coverage is now inspected; a bounded known-method specialization can test the local label without the unverified atlas. No new mathematics was derived in this literature-only turn; the ready continuation remains subject to separate supervisor approval.
SCOPE: The retained component-specialization/contraction mechanism using the actual maps and split-node models over unchanged N; REPRODUCTION only. General results are imported, not reproved. Excludes guessed formal gluing, arbitrary generator relabeling, field enlargement, arbitrary finite-map extension, global selected/theta data and original finite B>=A.
COVERED_TARGET: Test whether L053's Q translates L056/L057's retained seven-cycle by one adjacent component, using Tate isogenies, split-node resolution and contraction over unchanged N.

Step 211 completes the source comparison. The detailed evidence and exact
unproved specialization obligations are in
`drafts/2026-10-14-retained-component-specialization-source-review.md`.
No component identity or native label is asserted. The completed L058
audit remains independent and unchanged. A newly written ready
continuation receives separate approval on the next turn.

Retain L053,L056,L057, inherited L045,L048,L051,L054,L055, and
the audited local L058 result as context. Keep E_0/Q,
F=Q(zeta_60,E_0[30]),K_glob=F(E_0[7]),Omega,u,w,H subset N,
M>=max(M_tors,31),changed q_0 in Q_3 with v_3(q_0)=30,
the fixed pointed Tate isomorphism, actual alpha,psi,gamma,0_B and
Q=alpha(P). Q is defined using beta^7=q_0 as in L053. The native
map c:Z/7Z -> V is L057's actual cover comparison, not a chosen
generator relabeling. K_glob=N, q_0=3^30 and c(1)=plus-or-minus Q
are not premises.

The possible downstream use is the local native cusp label. The
discriminating test is whether inspected source theorems identify
specialization of Q on one of the two components adjacent to 0_B
in the actual retained seven-cycle and identify its translation action
with the corresponding graph rotation. The model can have thick nodes:
minimal regular components and the seven retained components must not
be conflated. Check contraction, markings and the origin, not merely
an isomorphism of cyclic component groups. If the only available
application still assumes the unverified marked atlas of ATTEMPTS/031,
record that exact obstruction and abandon this formulation rather than
repeat the coordinate attempt. No source formula is guessed.

Original finite B>=A, global selected/theta compatibility and actual
input/action/pilot/essentiality remain independent even if this target
eventually succeeds. Full matching Mathlib coverage is not checked.

## Step 212 — recovery repair, no new mathematical coverage

The TARGET now matches the saved Next action verbatim; it was already
listed as COVERED_TARGET in step 211. Direct source URLs have been added
to SOURCE_EVIDENCE. This is a field repair within the same mathematical
scope, not approval of a newly uncovered target. On 2026-10-14 the
Cremona author PDF, Conrad 2015 author PDF and Cesnavicius versioned
arXiv PDF were accessible again. Rechecked Cremona section 2.1's
valuation homomorphism and its positive, negative and half-period cases,
Conrad Proposition 3.7's henselian normal-proper contraction hypotheses
and Theorem 5.4's smooth-locus identification, and Cesnavicius section
3.2.1's finite-locally-free subgroup and unique contraction conditions.
Their applicability limits remain exactly those recorded above and in
the detailed step-211 source record. Other inspected source coverage is
reused, not claimed newly retrieved. Liu's mirror provenance and
Conrad's cited BLR proof qualification remain explicit.

LITERATURE_REASON: Supervisor recovery requires direct source URLs in
the ready assessment; no additional discovery or mathematical work is
needed for this repair. Outcome STALLED records no new theorem, source
coverage or evidence about adjacency. The next turn can attempt the
existing bounded SPECIALIZE target after the supervisor's gate check.
