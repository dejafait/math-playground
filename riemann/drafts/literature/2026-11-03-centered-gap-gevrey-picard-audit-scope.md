# Source reuse for the weighted centered-gap Picard audit

TARGET: Critically audit L703's uniform Gevrey kernel estimate, weighted convergence to the same prescribed-center Picard limit, and compatible fixed r,w,c satisfying the weighted norm and L702 smallness condition.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact weighted-profile search and local duplicate/stop comparison in drafts/literature/2026-11-03-centered-gap-gevrey-profile-scope.md (step 141); the audit changes neither the exact profile nor the weight, support, anchor or smallness hypotheses and adds no theorem target.
SOURCE_EVIDENCE: Reuse step 141's inspected proofs; direct primary URLs reaccessed 2026-11-03: Lev v3 https://arxiv.org/html/2007.09930v3#S4.SS3 (Lemmas 4.2--4.3); Mourrat--Weber https://sites.math.northwestern.edu/~auffing/papers/MourratWeber.pdf (Section 2.1 p.2405, Propositions 23--24 pp.2472--2473); Dasgupta--Ruzhansky https://backoffice.biblio.ugent.be/download/8585191/8585192 (Theorem 2.3(R) pp.761--762, forward proof pp.771--773); Groechenig https://arxiv.org/pdf/math/0611174v1 (Lemmas 2.1(a), 4.1, PDF pp.3--5). See access collation below and step 141 for reading limits.
COMPARISON: These sources cover all tools used for the already-assessed specialization; none is asserted to contain the exact anchored weighted conclusion. L703's applicability and parameter-dependence arguments now require independent conceptual scrutiny, not a fresh general regularity theorem.
GAP: Audit the common derivative-to-Fourier constants, r*|v-u| majorant, weighted absolute summation/source-limit identification, exact reflected data, unchanged Y-ball iterates, order of C/r/w/c choices and the final smallness interface; L703 remains unaudited pending this check.
REASON: Step 143 repairs the supervisor-reported missing direct source URL using accessible primary texts, retaining SPECIALIZE and the exact audit target. Coverage suffices for the bounded audit; this process repair neither verifies L703 nor changes its mathematical scope.
LITERATURE_REASON: Supervisor recovery explicitly requires direct source URLs in the ready audit assessment; this turn repairs traceability and rechecks access rather than repeating discovery or attempting the audit.
SCOPE: Only L703 (1)--(14), with L694's exact operator and iteration, L696 Section 2's prescribed center and L702 Section 2/audit's unweighted constant B. Preserve Gevrey-2 selection at the outset, one positive exponent and width fixed before n, real shifts, cap 1/8, anchor and unit masses. No finite-response, charge, H/support or Xi conclusion.

The exact target is a conceptual audit, not another derivation. The
startup assessment for step 142 already scoped the uniform nonlinear
estimate, same-limit identification and simultaneous choices. L703
uses only those tools and proves only that application difference.
No fresh external browsing is needed for this nomination; the complete
prior primary-source comparison, stronger unanchored Kargaev
comparison and optional inaccessible Kargaev--Volberg lead are reused.
The optional lead has not become an essential premise.

The critical claims to inspect are the following parts of the canonical
proof, without treating its successful write-up as verification:

1. The common Cauchy bounds for h_s, product derivative estimate (3),
   and uniform application of the imported Fourier theorem in (4),
   including complex values, the zero mode and real |s|<=1.
2. The exact parameter derivative of E_m, its removable value at
   zero, and preservation of r*|v-u| and the k-m index in (5).
3. Weighted summation (6), compatibility with Lev's distributional
   operator, and the uniform convolution constant for every
   0<=c<=delta/2. Finite weighted norms alone are not contraction.
4. L702's B must stay independent of C,r,w. The prescription must
   be the actual reflected Q_w, with Psi used only on its prescribed
   bands. The local analytic multiplier and extension by zero in
   (11) must establish regularity without assuming global Gevrey Psi.
5. C,r are selected before w and the final c. Decreasing c after
   choosing w must preserve q_c<=1/4; no width-uniform positive
   exponent or small weighted-data norm may be silently required.
6. The original Y-ball iterates must be invariant and converge in
   A_c to the same Y fixed point, preserving support and real
   coefficients. Check (2), the target weight comparison and (14).
   The final gap and counting masses must use the same e.

Accept only if these claims follow from the cited hypotheses with
the stated quantifiers. Otherwise isolate a concrete failing estimate,
unpaid parameter dependence or changed prescription. Any repair or
stronger target outside this scope requires a new assessment. The
L695 absolute-cost and L702 endpoint-only stops are preserved, and
matching Mathlib coverage remains unverified. No RH candidate exists.

The audit should use the ready cited proofs and canonical local proof;
no numerical script is necessary for these analytic assertions. A
completed audit may confirm or repair this local specialization but
must not count importing the general Gevrey tools as a new discovery.

## Direct-source access collation (step 143)

All four URLs in SOURCE_EVIDENCE returned their primary text through
web access on 2026-11-03. This supplements, rather than replaces,
the detailed hypotheses and proof-case assessment of step 141.

- Lev, *An example concerning Fourier analytic criteria for translational
  tiling*, arXiv:2007.09930v3, 27 September 2021: rechecked Section 4.3,
  Lemmas 4.2--4.3, (4.4)--(4.12). The fixed Hermitian cutoff has
  b<l<1/2; the parameter difference estimate assumes varphi'(0)=0
  and real u,v in [-1,1]. Zero frequency, integration by parts and
  the parameter-integral case are explicit. Polynomial coefficient
  decay with constants depending on derivative order is not the
  uniform Gevrey bound being audited. Published reference remains
  Rev. Mat. Iberoam. 38 (2022), 1975--1991, DOI 10.4171/RMI/1318.
- Mourrat--Weber, *Global well-posedness of the dynamic Phi4 model
  in the plane*, Ann. Probab. 45 (2017), 2398--2476, DOI
  10.1214/16-AOP1116: rechecked Appendix Propositions 23--24 and
  their complete proofs, pp.2472--2473. Product stability requires
  theta>=1; Fourier decay requires compact support and Gevrey
  bounds. The final exponent choice depends on the derivative-bound
  constant. Step 141's Section 2.1 cutoff reading is reused; no
  width-uniform exponent or nonlinear regularity theorem is imported.
- Dasgupta--Ruzhansky, *Gevrey functions and ultradistributions on
  compact Lie groups and homogeneous spaces*, Bull. Sci. math. 138
  (2014), 756--782, DOI 10.1016/j.bulsci.2013.12.001: rechecked
  Definition 2.1 and Theorem 2.3(R), pp.761--762. For s>0 on a
  compact Lie group, the Roumieu constants are existential, with
  coefficient decay for all irreducible representations. Step 141's
  forward-proof reading pp.771--773 is reused. The s=2 circle
  specialization remains covered; family-uniform constants still
  require L703's own justification.
- Groechenig, *Weight Functions in Time-Frequency Analysis*,
  arXiv:math/0611174v1, 7 November 2006 (published Fields Institute
  Communications 52 (2007), 343--366): rechecked Lemma 4.1 and
  the complete discrete proof, PDF pp.4--5. It supplies the weighted
  convolution norm inequality for submultiplicative weights on Z^d;
  use d=1. Step 141's Lemma 2.1(a) weight comparison is reused.
  This tool does not establish that the nonlinear operator has a
  common weighted coefficient majorant.

No new exact-match search or novelty claim is made. The earlier local
duplicate comparison (L694/L696 unweighted construction, L702 smallness)
and failure comparison (L695 absolute cost, L702 endpoint-only stop)
are reused unchanged. The inaccessible optional Kargaev--Volberg lead
remains unread and nonessential. Full matching Mathlib coverage remains
unverified. No lemma or mathematical script is changed in this repair.
