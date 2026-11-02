# Conditional periodic Whitney reduction: proposed mathematical scope

TARGET: Test a periodic k=2 Whitney truncation of L582 under explicit paired bad-set energy budgets O(1) and O(ell^3), including C2 smoothing and six-jet support at most ell^2.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed 2026-10-31-periodic-spatial-truncation-scope.md records the exact searches, duplicate comparison, primary statements and extension/boundary cases. That review found no inspected theorem for this periodic paired interface; no originality is inferred.
SOURCE_EVIDENCE: FJM (2002), https://onlinelibrary.wiley.com/doi/10.1002/cpa.10048 and https://dept.aem.umn.edu/~james/research/Publications_Files/PDF/73.pdf, Proposition A.2(ii), pp.1498--1503, (A.5),(A.9),(A.11)--(A.35), prior full reading reused; Irving (2025), https://pmc.ncbi.nlm.nih.gov/articles/PMC12259811/, Proposition 2.10; Hunter (revised 2014), https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf, Theorems 1.28, 3.19, 3.24 and proof. Current access and exact reuse limits are recorded below.
COMPARISON: Classical higher-order truncation and finite-p smoothing cover the techniques. The difference to test is a periodic extension with constants independent of P and quantitative paired polynomial losses; no general homogeneous A-free truncation theorem is silently applied to an inhomogeneous jet constraint.
GAP: Construct the period-uniform bounded weak jet and then a C2 periodic path while retaining all ordinary second/fourth budgets and the four tiny signed odd expectations; no actual-Hardy bad-set estimate or positive clipped mass is assumed proved.
REASON: The source review isolates an independently testable conditional reduction. A reproof of FJM is unnecessary; only the missing periodic/full-jet specialization and smoothing/loss interface may be developed. Separate literature-only recovery has now checked the direct source references and approved this unchanged bounded scope for a subsequent research invocation; no result is established by that approval.
SCOPE: L582's real H on a common eventual ray, ell=log H, P=H ell+1, ordinary derivatives through two, lags 0 and 1, L473 (2) in full; absolute constants and onset uniform in H and P. Explicit additional weighted budgets below are conditional inputs, not consequences of L473 (10).

## Exact bounded test, with proposed rather than established assumptions

Let g be the specified L582 path and write

    V_g(s)=(g^(j)(s+r))_(r=0,1; j=0,1,2),
    a(s)=|g(s)|+|g'(s)|+|g''(s)|.

Use the centered maximal function of the periodic extension,

    M_P a(s)=sup_{rho>0} (1/(2rho)) integral_(s-rho)^(s+rho) a(t) dt.

The proposed reduction seeks one sufficiently large absolute A, fixed
before H varies, at lambda=ell^2/A. Set on R/PZ

    E={s: M_P a(s)>lambda},
    E_pair={s: s in E or s+1 in E}.

Allow the following **additional hypotheses**, with constants independent
of H (normalized integrals over one period):

    (1/P) integral_E_pair (|V_g(s)|^2+lambda^2) ds=O(1),
    (1/P) integral_E_pair (|V_g(s)|^4+lambda^4) ds=O(ell^3).

Test whether a periodic Whitney extension on the complement of E gives
a W^{2,infinity} path h, agreeing with g and g' there and with each
weak derivative through two bounded by C lambda for one absolute C.
It must not lose a factor of P in lower derivatives, silently enlarge
E without controlling its weighted budgets, or impose incompatible
mean/trace data. The desired C2 (or smoother) periodic output is then
to have paired norm <=ell^2, preserve every L473 (2) tolerance, and
give the four tiny signed odd expectations exactly zero. All of these
are targets for a later proof, not conclusions of this assessment.

Periodizing a whole-space W^{2,p} theorem by cutting off a long period
is not an approved shortcut: the cutoff and restored data must be
estimated. Finite-p periodic convolution is an assessed smoothing
technique, but its weak derivative bounds, two-lag polynomial errors,
support margin and single eventual ray still need proof. Use a support
margin before smoothing; do not assume convergence in W^{2,infinity}.
An H-dependent smoothing radius is allowed if the final constants and
onset are uniform. No numerical height or effective radius is sought.

## Inputs, downstream use and stop test

Essential local inputs are L582 and L473 (1)--(2),(6),(9)--(10), with
all retained arithmetic-import qualifications. C582a is a contrast
limiting scalar composition, not an input supplying extension or losses.
The parent assessment gives exact primary theorem hypotheses and the
source proof cases needed for this adaptation. Full proofs of FJM's
cited Ziemer results remain imports, not independent audit targets.

Continue only if the periodic construction has P-independent constants
and a complete comparison of all 147 entries under the displayed
budgets. An informative failure must identify a concrete periodic jet
compatibility obstruction or a specific missing uniform estimate; an
absent matching theorem is not a counterexample. A partial result
should state exactly which part (extension, smoothing, or moment loss)
was proved, rather than adding an unsupported complete lemma.

If successful, this would isolate explicit actual-Hardy exceptional-set
estimates sufficient for hard support while preserving derivative
consistency. Those weighted estimates are unresolved: the imported
O(ell^4) full fourth norm supplies no asserted O(ell^3) loss here.
Positive clipping, realization of L473's particular law and actual-Xi
signs remain independent. This is development of an established method,
not a central creative RH mechanism. Matching Mathlib coverage has not
been checked; no cross-notebook input is used.

## Separate direct-source gate review (2026-10-31)

This is a source-reference repair, not another search for a new theorem.
The target, proposed hypotheses, decision EXPLORE and stop test are unchanged.
The parent assessment's inspected proof cases and duplicate/failure comparison
are reused; no additional arithmetic import or new mathematical derivation
is made. Source coverage is adequate to attempt the specialization, not to
assert its conclusion.

- FJM: [published article and bibliographic record](https://onlinelibrary.wiley.com/doi/10.1002/cpa.10048),
  CPAM 55 (2002), 1461--1506; [author PDF](https://dept.aem.umn.edu/~james/research/Publications_Files/PDF/73.pdf).
  The journal record was opened this turn. The PDF and two author-host
  variants returned fetch errors; shell retrieval failed DNS. No fresh
  full-text read is claimed. The parent assessment already records reading
  A.2(ii), pp.1498--1503 and its essential cases, so this transient access
  failure creates no essential unread theorem for the unchanged target.
  Retain its prescribed zero traces, bounded Lipschitz domain, finite p,
  boundary density condition (A.5), domain-dependent constants and
  W^{2,infinity} conclusion. No period-uniform or C2 conclusion is imported.
- Irving: [primary full text, Proposition 2.10](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259811/),
  DOI 10.1007/s10231-025-01547-2, version of record 2025. Reopened the
  proposition and good-set/jet/boundary argument (2.45)--(2.53); the
  parent reading of the remaining extension cases (2.54)--(2.62) is reused.
  The N-function Delta_2/nabla_2 conditions and zero boundary jets remain
  essential. This supports the truncation technique, not the periodic
  full-jet bound or paired losses.
- Hunter: [author notes, revised 18 June 2014](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
  Theorems 1.28 (printed p.12), 3.19 (p.55), 3.24 and proof (p.59).
  Reopened weak-derivative commutation and finite-p approximation proof;
  the parent inspection of Theorem 1.28 is reused. In particular 3.24
  requires finite p and whole-space Sobolev integrability. Periodic
  adaptation, support margin and polynomial comparison remain the
  approved research tasks, with no W^{2,infinity} density claim.

No new independent proof audit of these sources or their cited Ziemer
inputs is claimed. Matching Mathlib coverage remains not checked. This
repair supplies direct URLs in the ready assessment itself; it does not
resolve any of the conditional Hardy budgets, 147 tolerances, positive
clipping or actual-Xi signs.
