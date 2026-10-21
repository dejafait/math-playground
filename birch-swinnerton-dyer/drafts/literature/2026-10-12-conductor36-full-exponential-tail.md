# Fixed coupled plan with the full exponential tail — source approval

TARGET: Assess replacing the coupled T_5 plan's dyadic tail majorant by certified rational enclosures of Wuthrich's full exponential tail, with all saved points and absolute occurrence weights fixed, to test cutoff 4860 and normalized two-sided tail width 2^-38 within 1000000 terms.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused L049/L051 assessments; searched Wuthrich Numerical modular symbols tail exponential; compared the coupled assessment, L054 error convention and ATTEMPTS/026--028. Search results establish neither a matching workload certificate nor novelty.
SOURCE_EVIDENCE: Reopened Wuthrich arXiv:1608.06423v2 (23 March 2017), Section 3 equation (2), Lemma 4 and complete proof, printed pp.6--7; reopened NIST DLMF 4.2.19--4.2.22, accessed 2026-10-12. Reused audited L049 finite-function construction and L051 real Taylor/positive attenuation audit with their precise citations.
COMPARISON: The full exponential tail is explicit in Wuthrich's proof; rational exponential containment and weighted interval propagation are covered by L049/L051. The missing part is the saved 98-point workload certificate, not a new analytic estimate. L054's dyadic failure does not imply failure of this bound.
GAP: No full-exponential feasibility calculation has been performed; certify every rational radius and uncombined occurrence width, then compare all 72 rows, cutoff and distinct terms with fixed thresholds.
REASON: Approve finite known-method specialization on unchanged geometry, not a tail reproof or BSD claim; the sources suffice for the exact planning test below.
LITERATURE_REASON: Changed full-exponential convention was outside the prior fixed-dyadic assessment; this review supplies its missing theorem comparison and rational-enclosure scope.
SCOPE: Tail planning only for E=[0,0,0,0,1], N=36, saved L054 solution, all points and uncombined absolute occurrence weights, and independent audited L051 positive total-period lower bound. No Fourier sums, recovery, transports or signed-error cancellation.
COVERED_TARGET: Implement and independently replay full-exponential-tail planning on L054's fixed 98 points and uncombined absolute occurrence weights, testing all 72 normalized two-sided tail widths <=2^-38 with cutoff <=4860 and total distinct terms <=1000000.

## Gap and primary source comparison

The main gap remains rank E(Q)=m(E) for arbitrary analytic order m(E)>=2.
The intermediate target is a bounded tail plan for the full conductor-36
relative integration table. Passing could support a later finite-sum
certificate; it supplies neither that table nor coefficients, rational
points, Sha finiteness or a complex-order comparison. CM excludes L027.
The requested review TARGET is preserved; COVERED_TARGET is its single
executable continuation. No new mathematics or calculation is performed.

[Wuthrich, Numerical modular symbols for elliptic curves,
arXiv:1608.06423v2, equation (2), Lemma 4 and proof,
printed pp.6--7](https://arxiv.org/pdf/1608.06423v2) concerns the associated
normalized elliptic newform at an interior point z=x+iy, y>0.
Its statement gives a sufficient cutoff via T(y,epsilon); the complete
proof explicitly bounds the omitted terms n>H by

    B_H(y)=exp(-2*pi*H*y)/(exp(2*pi*y)-1)
          =q^(H+1)/(1-q), q=exp(-2*pi*y), H>=0.

The proof uses global |a_n|<=n, citing [13, Lemma 2.9], not finitely
checked coefficients. No non-CM, semistability, unitary-cusp or period
hypothesis enters this proof. Real error is bounded by complex modulus.
The later divisor-bound improvement is outside the target. The practical
rounding algorithm is not an interval certificate and is not imported.
No reproof of the analytic theorem is needed.

[NIST DLMF 4.2.19--4.2.22](https://dlmf.nist.gov/4.2#iii) gives exponential
series, addition, real positivity and modulus. Standard Taylor's theorem
with Lagrange remainder is already assessed in the audited L051 source
review. Reuse its exact polynomial interval evaluation at negative real
arguments and explicit outward remainder. No library correctness theorem
is required or asserted.

## Applicability and approved finite certificate

L054's balanced transports have y=1/|C| for C!=0 and y=1 otherwise;
thus rational 0<y<=1 lies within L051's audited attenuation domain.
Replay must verify this at every saved point. Use its Machin pi brackets,
degree-160 real exponential Taylor polynomial at w=-2*pi*y in [-8,0],
recorded remainder 3^8*8^161/161!, and outward rational arithmetic.
Require 0<q_lower<=q_upper<1. Refine pi, degree and outward precision
by L049's assessed method if needed, recording every remainder and
operation. A decimal approximation does not suffice.

Apply ordinary positive rational interval multiplication and division to
the imported q^(H+1)/(1-q) formula, with complete power replay and
strictly positive denominator brackets. Its upper endpoint is
q_upper^(H+1)/(1-q_upper); its lower endpoint uses q_lower. These are
enclosures of the source majorant itself. The lower endpoint is not a
lower bound on true analytic error. This is applicability of existing
interval arithmetic, not a new mathematical tail lemma. Outward rounding
must not shrink an upper radius.

Retain L054's independent Omega_lower and uncombined occurrence rule:

    width_g_upper=(2/Omega_lower) sum_occurrences |w_j| B_j_upper.

Caching or signed cancellation must not reduce the weights. L054's
rho=2^-38 Omega_lower/(2 W_max), W_max=22/3, remains a sufficient
uniform primitive allocation; report actual row bounds regardless.
Test every point at H=4860 first. If all rows pass, certified H_j<=4860
may be selected (uniform 4860 is permitted), with full distinct-term sum
checked against 1000000. Minimal cutoffs are optional; claims of
minimality require predecessor evidence. Infinity is exact zero.
No coefficient beyond 4860 is needed to validate the global tail.

Continue only with all 72 upper widths<=2^-38, max H<=4860,
sum distinct H<=1000000 and zero complete-replay failures. Save full
rational certificates, actual/required counts, failures and paths.
A row's lower enclosure for the source-majorant width at all H=4860
exceeding 2^-38 is an exact stop witness on this fixed geometry.
Straddling brackets require refinement within the approved scope;
failure to separate them is inconclusive. Failure of the sufficient
uniform rho allocation alone does not rule out all allocations.
No such threshold comparison was calculated in this literature turn.

## Reuse, duplicates, failures and qualifications

Inspected L049's tail/finite-function ranges, L051 attenuation/tail/audit
ranges and L054 hypotheses, balanced points and absolute-weight section.
Reused ready assessment
`drafts/literature/2026-10-11-nonunitary-reduced-phase-critical-audit.md`
and the coupled assessment's source evidence. ATTEMPTS/026--027 preserve
geometry workload failures; ATTEMPTS/028 and history/180 preserve the
dyadic cutoff obstruction. None gives this fixed workload's certified
full-exponential test. The analytic estimate and arithmetic mechanism
are known; only finite specialization is approved. Additional search
results were discovery leads, not imported mathematical inputs.

Essential inputs: L038 saved N=36 presentation/72 generators/144 endpoints;
audited L049 full-tail identities; L050 minimal curve/conductor; audited
L051 positive total period and attenuation; L053 representatives; L054
coupled solution, 98 points and full occurrence weights. No cross-notebook
input. L052 clearing integer 24 is downstream only. N=36 structural,
L053 and L054 instance critical audits remain pending. Passing tail
planning leaves new finite sums, signed period division, integer isolation,
table relations and separate audits unresolved. It is not an integration
interval or a BSD candidate. Uniform coefficient production, rational
directions, Sha and complex-order comparison remain missing.

Mathlib: full matching workload theorem and supporting interval/Taylor
formalization were not checked. Unknown coverage is not evidence of absence.
