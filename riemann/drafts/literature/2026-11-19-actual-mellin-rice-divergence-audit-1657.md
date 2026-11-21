# Critical audit scope: actual-E Rice divergence

TARGET: Audit C048k's finite Rice normalization and absolute-divergence conclusion on Re(s)=-1/4 for each fixed d>=3, checking the Lambert branch rate, two-sided remainder, gamma normalization and retained contour edges.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse approved assessment1656 and source-notes1656's exact Jensen/Mellin/Rice searches and duplicate comparison; this target audits the resulting fixed-line calculation without extending its scope. No new search or originality claim.
SOURCE_EVIDENCE: Flajolet--Sedgewick TCS144(1995),101--124, Section2 Lemma1/(6)--(7), pp104--105, Section4 Theorem2/proof pp110--111, https://algo.inria.fr/flajolet/Publications/FlSe95.pdf ; DLMF5.5.5 https://dlmf.nist.gov/5.5.E5 and5.11.9 https://dlmf.nist.gov/5.11.E9 ; primary hypotheses and proof cases already inspected in source-notes1656. Local C048a/C048j audited contracts and L828 Section2/L829 definitions are the remaining inputs.
COMPARISON: Same actual E, c=-1/4 and fixed d>=3 as approved assessment1656. Finite Rice and gamma asymptotics are imported; C048k supplies the normalization and actual weighted-growth specialization. Review requires checking those derivations, not importing a new source theorem or a full-contour identity.
GAP: Independent verification of the completed C048k specialization is pending; no unbounded-contour formula, conditional-integral failure, moving-degree bound, sign or RH claim is included.
REASON: Separate literature approval1658 confirms adequate reused coverage for this exact conceptual audit; no essential unread theorem is identified. The mathematical audit remains unperformed and is the next research step.
SCOPE: Exact TARGET only, REPRODUCTION; approved by literature-only step1658 without extending hypotheses or techniques. No new interpolation or signed bridge, no calculation at other lines, and no reopening of L829's finished derivative diagnostic.
LITERATURE_REASON: The invocation-start gate explicitly requires separate approval of the newly saved assessment1657; this turn checks that coverage rather than repeating external discovery on a ready target.

## Review contract

Read C048k's full proof and compare its exact inputs, rather than
treating its asymptotic rate or residue formula as an audited premise.
Essential mathematical inputs are L019/L021's K and moments, C028b's
gamma/J definitions, C048a's I normalization and principal W bounds,
C048j's full relative bound, and only L828 Section2's unconditional
construction as instantiated in L829. Their source records were read
in step1657; reuse them with the exact qualifications.

The decisive checks are E(k)=gamma_k/gamma_0 and the positive
rectangle orientation; p=s+1/2; applicability of C048j on both tails;
U/log t->1 and V->pi/2 from w exp(w)=2p/pi without argument wrapping;
the sign and size of Re(p/w); use of |I/S-1| tending to zero for a
lower bound; the gamma argument 1/4+it and exponent +pi|t|/2; and
the fixed-d polynomial denominator. Check compact-line continuity
and whether the conclusion distinguishes absolute divergence from
conditional or regularized integrals. No script or numerical probe
is necessary for this analytic audit.

Acceptance would retain only the fixed absolute-opening stop. An
invalid lower bound or normalization requires a precise correction
or withdrawal of that stop, with unfinished reasoning preserved.
No outcome establishes actual-Xi signs or C028b's height condition.
Mathlib coverage for the full specialization remains unchecked.

## Separate source-coverage approval1658 — 19 November2026

Reused the complete primary read record in
2026-11-19-mellin-jensen-contour-source-notes-1656.md and the approved
2026-11-19-mellin-rice-vertical-viability-1656.md. The former records
the finite analytic-contour hypotheses and both growth-dependent
Theorem2 proof cases, the published/prepublication pagination distinction,
and DLMF's bounded-real-part uniformity sentence. No new browsing is
needed for the unchanged sources and scope. Their recorded searches,
L718 comparison and distinct actual Cauchy-circle route are reused;
no duplicate-search failure is a novelty claim.

Located step647's precise integer-interface record in
2026-11-05-direct-mellin-laguerre-interpolation-scope.md, section
"Integer interface: source applicability, not a new lemma". The number
647 here denotes that completed November5 step, not the unrelated
November12 reference-construction nomination with a 647 filename suffix.
Only the integer-interface paragraph is relevant; its product-class
and Laguerre source theorems are not inputs to the present audit.

Compared the scope of C048k's stated claims against C048a/C048j's
hypotheses and conclusions, L829's definitions, and L828 Section2
(5)--(6). This is a coverage check, not verification of their proofs
or of C048k's deductions. L828's entire-continuation construction must
remain separate from its subsequent representation-conditioned
zero-free assertions. C048j supplies the actual I/S relative contract;
it supplies neither the reciprocal-gamma normalization nor a completed
Rice opening. No essential theorem beyond the recorded finite Rice,
duplication and vertical gamma inputs is needed for the proposed audit.

Decision remains SPECIALIZE with the exact TARGET unchanged and ready
for a separate REPRODUCTION conceptual audit. Acceptance still requires
every normalization, branch, lower-bound and retained-edge check in
the review contract above. No audit conclusion, new lemma, mathematical
calculation or advance beyond the checked sources is claimed. This
approval repeats an existing adequate source decision, so its honest
STEP_OUTCOME is STALLED rather than a mathematical advance or new
negative result. Return to mathematics next; do not schedule another
source approval without a changed essential hypothesis or unread input.
