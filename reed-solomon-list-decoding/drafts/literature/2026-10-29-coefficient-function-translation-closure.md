# Coefficient-function translation closure — proposed bounded test

TARGET: Test whether the seven full-sheet directional constancies force U=span_K{1,a_0,a_1,a_2} to be invariant under both unit translations of F_137^2, for every permitted C,sigma and K=E or F.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed directional-Fourier assessment records finite-characteristic, variable-coefficient and coefficient-function translation searches, with no matching closure theorem found; scoped searches in the full-sheet and fiber working records and ATTEMPTS/109–112 found no prior translation-module closure test. A failed search does not establish novelty.
SOURCE_EVIDENCE: Reuse the actual primary readings in 2026-10-29-directional-fourier-annihilator.md: EKL (2017), Proposition 2.6/full proof, pp. 309–310, https://ems.press/content/serial-article-files/44351 ; GGI arXiv:math/0310169v1, Theorem B/full proof and equality discussion, PDF pp. 3–4, https://arxiv.org/pdf/math/0310169v1 . No source asserts the proposed closure.
COMPARISON: EKL supplies cyclic-module factors over either finite coefficient field, and GGI permits arbitrary-field translation modules of functions. They neither identify a generated translate module with U nor force variable-label equations to preserve U. Proving precisely that missing bridge would give a new way to use the ready algebraic tools without positivity or a full-minor import.
GAP: Prove both uniform translation inclusions from the original equations, or give an exact allowed assignment whose U is not preserved. Arithmetic of the nontrivial cyclic factor degrees and any downstream annihilator or collapse implication remain to be verified, rather than assumed as a source import.
REASON: This is a concrete closure mechanism at the remaining full-sheet coefficient gap, distinct from residual-rank solving, reflected two-fiber extension and the stopped design-matrix import. One bounded creative attempt is proposed; no closure result, new lemma or calculation is supplied by this literature turn. This newly written continuation awaits separate supervisor approval.
SCOPE: q=137,T={16,64,70,102,112,118,121},E=F_65537,F=F_(65537^28),H=<19139> of order 1024,k=64; arbitrary 61-core C and bijection sigma as in L030, K=E or F, repeated quadratics and every full-sheet constancy. No presumed action on message images, affine labels, generic labels, new characteristic or retention/RS transfer.

## Exact unproved assertion

Use the L135 hypotheses preceding its coefficient-span-two assumption:
sigma maps (T times F_137) disjoint union four dummies bijectively to
H minus C. Put x_(t,y)=sigma(t,y). For each P=(u,v) in F_137^2,
write g_P(X)=a_0(P)+a_1(P)X+a_2(P)X^2 in K[X]. For all t,y,
g_P(x_(t,y)) is constant on u+tv=y. Repeated polynomials are allowed;
no coefficient-span restriction is imposed.

Regard U=span_K{1,a_0,a_1,a_2} as a space of functions on the auxiliary
sheet. For e_1=(1,0) and e_2=(0,1), define (tau_e f)(P)=f(P+e),
using addition only in the auxiliary domain. The proposed assertion is
tau_(e_i) U subset U for i=1,2. It is not a premise and is not proved.
In particular, do not infer it by translating the constraints and
silently translating or fixing the x_(t,y) labels.

## Relevance, downstream obligations and bounded decision

The main gap is arbitrary-center 67/68 safety. The proposed closure
could allow cyclic-module dimension restrictions to force constant
coefficients, or a common annihilator usable with C137a. This is a
possible downstream application, not an established conditional theorem
in this review. A future attempt must explicitly check the relevant
ord_137(|K|) for BOTH K, the module argument and any scalar-extension
or descent step it uses. No large-characteristic cutoff or Fourier-minor
nonvanishing is assumed. The seven label-dependent constraints, rather
than a preexisting representation of messages, must supply closure.

The concrete positive test is to prove a_j(P+e_i) belongs to U for all
j=0,1,2 and i=1,2 under every permitted labeling. A negative test is a
fully specified allowed C,sigma, all g_P satisfying every directional
constancy, and an exact witness tau_(e_i)a_j outside U. A partial
assignment or example with arbitrary labels outside H minus C does
not pass that test. An unresolved closure implication after one bounded
attempt is EXPLORATION, not a negative theorem or a license to increase
the old reflection search budget. Save partial reasoning first.

The new mathematical obstruction is translating across the indexed
evaluation levels while keeping the small function span fixed. Merely
rewriting the 74528-row residual system in a character basis does not
meet the test. ATTEMPTS/109–112 and the design-matrix import obstruction
remain preserved. Retention, compatible laws and RS transfer remain
independent gaps even if the local program succeeds.

Essential local inputs are L030's labeling setup and the exact
constancies restated in L135; C137a/L137 provide possible downstream
geometry, not a closure premise. No cross-notebook input. Full matching
and supporting Mathlib coverage are not checked. Existing source
qualifications on the July ABF statement and L137 remain in force.
No mathematics beyond the inspected sources is established here;
POTENTIALLY_NEW would describe a later attempted bridge, not certified
originality. The next task and routing live only in PROGRESS.md.
