# Periodic second-order spatial truncation: source comparison

TARGET: Assess whether periodic second-order spatial truncation can modify L582's path to a C2 stationary law with paired jet norm at most ell^2 while preserving all 147 L473 tolerances.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the scalar assessment, L582's proof and C582a's restricted stop; searched periodic higher-order Lipschitz truncation, second-order truncation with C2 regularity, and the precise FJM Proposition A.2. Read the primary statements and essential cases below. No inspected result covers the complete target; this is not a novelty claim.
SOURCE_EVIDENCE: Irving, DOI 10.1007/s10231-025-01547-2, Proposition 2.10, (2.45)--(2.62); Friesecke--James--Mueller, CPAM 55 (2002), Proposition A.2(ii), pp.1498--1503, (A.5),(A.9)--(A.35) and final regularity paragraph; Schiffer, Calc. Var. 64, 30 (2025), Definition 1.1, Lemma 2.2 and Lemma 4.5; Hunter, Notes on PDE, revised 2014, Theorems 1.28, 3.19 and 3.24, with finite-p smoothing proof. Primary links and qualifications below.
COMPARISON: FJM supplies stronger tail-localized modification-set control than Irving's displayed global-energy bound, but its second-order conclusion remains W^{2,infinity} with prescribed traces. Its C1 upgrade explicitly concerns the first-order clause. Neither that result nor Schiffer's conditional torus property supplies this periodic C2 paired law or its 147 moment losses.
GAP: A period-uniform derivative-consistent extension, subsequent C2 smoothing with support margin, and weighted losses on the union of the bad phase set and its lag-one translate remain unproved. The actual-Hardy weighted fourth loss is not supplied by L473's O(ell^4) full fourth norm.
REASON: Essential source comparison is now complete for a bounded conditional extension/loss test, not for asserting truncation of the actual path. Park the direct theorem-import claim; the refined mathematical continuation is assessed separately in 2026-10-31-periodic-whitney-weighted-reduction.md and needs the supervisor's separate approval.
SCOPE: H real on a common eventual ray, ell=log H fixed, both lags 0 and 1, ordinary derivatives through two, all 21 second and 126 fourth tolerances with the four tight signed odd expectations distinguished. Positive clipping, realization of nu_H and actual-Xi transfer remain independent.

## Exact interface and duplicate/failure check

Use L582's specified quintic closure, H real on one eventual ray,
ell=log H, L=H ell and P=L+1. L473 (2) requires O(1) errors in
ordinary second entries and O_m(ell^3) in all fourth entries. At each
lag its signed value/first-derivative and first/second-derivative
expectations instead have absolute bounds O(H^(-2/3)/ell) and
O(H^(-2/3)/ell^3). These are not absolute-product moments.

L582 already gives C2 periodic stationarity and all these tolerances,
with only C H^(1/6) support. C582a obstructs normalized scalar
composition uniformly over compatible bridges, not spatial modification
of L582. The scalar assessment already explains why full Hardy fourth
norms do not quantify saturation losses; its arithmetic-source assessment
is reused, including Bui--Hall Proposition 3's unaudited proof. No new
arithmetic estimate or global stationary-law import is attempted here.

## Primary source evidence

**Irving.** Christopher Irving, *Partial regularity for minima of
higher-order quasiconvex integrands with natural Orlicz growth*, version
of record (2025), [DOI](https://doi.org/10.1007/s10231-025-01547-2),
[primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259811/),
Proposition 2.10 and (2.45)--(2.62). For an N-function
phi in Delta_2 intersect nabla_2 and q in W_0^{k,phi}(B_R;R^N), it
asserts q_lambda in W_0^{k,infinity}, with kth derivative <=C_1 lambda,
phi-energy <=C_2 times the original kth energy and
phi(lambda)|{q!=q_lambda}| <=C_2 integral phi(|D^k q|).
Constants have the dependencies stated there. Read zero extension and
unit-ball rescaling, all-order maximal good set (2.48), Taylor jets
(2.50)--(2.52), boundary decay (2.53)--(2.56), and extension/energy
cases (2.57)--(2.62). Zero boundary jets are used essentially; matching
periodic traces is a different interface. The displayed conclusion does
not assert continuity of the kth derivative. The proof's line invoking
Ziemer prints W_0^{1,infinity} and a derivative of q; do not treat that
line as stronger regularity or an independent audit of the proposition.

**FJM, resolving the inherited unread lead.** G. Friesecke, R. D. James
and S. Mueller, *A theorem on geometric rigidity and the derivation of
nonlinear plate theory from three-dimensional elasticity*, Comm. Pure
Appl. Math. 55 (2002), 1461--1506,
[DOI](https://doi.org/10.1002/cpa.10048),
[author's published PDF](https://dept.aem.umn.edu/~james/research/Publications_Files/PDF/73.pdf),
Proposition A.2(ii), pp.1498--1503. For finite 1<=p<infinity, bounded
Lipschitz S and closed Gamma subset boundary S satisfying (A.5),
H^{n-1}(B(x,r) intersect Gamma)>=c r^{n-1}, input u in W^{2,p}(S)
has u=Du=0 on Gamma. Output u_lambda in W^{2,infinity}(S) has the
same traces, norm <=C(p,S)lambda, and (A.9)

    lambda^p |{u_lambda!=u}|
      <= C(p) integral_{a>=lambda/2} a^p,
    a=|u|+|Du|+|D^2u|.

Read maximal-set localization (A.11)--(A.15), boundary case
(A.19)--(A.23), closed-jet extension and variable-radius mollification
(A.24)--(A.35). Its final paragraph upgrades clause (i) to C1;
clause (ii) has no corresponding C2 assertion. The fixed-input limit
(A.10) is not a uniform H-family estimate at lambda~ell^2.
The MPI preprint download failed, but the published PDF was accessible;
this lead is no longer source-blocked. Ziemer's cited full extension
theorem remains an unread proof dependency, unnecessary for using FJM's
stated theorem as an import; no source-proof audit is claimed.

**Torus comparison.** Stefan Schiffer, *A-free truncation and higher
integrability of minimisers*, Calc. Var. 64, 30 (2025), published
6 December 2024, [version of record](https://doi.org/10.1007/s00526-024-02855-w),
Definition 1.1, Lemma 2.2 and Lemma 4.5 inspected. Property TP is an
assumption on a homogeneous constant-coefficient differential constraint,
with bounded torus output and changes confined to a maximal bad set.
It is not a general theorem for the inhomogeneous jet consistency
relations between g,g',g''. Lemma 4.5 instead imposes zero boundary
traces and cites FJM; the displayed bad-set formula has a u/v notation
mismatch and is not used here as a corrected quantitative input. The
minimizer higher-integrability theorems are inapplicable without a
variational minimality premise for L582, which is absent.

**Smoothing support.** John K. Hunter, *Notes on Partial Differential
Equations*, revised 18 June 2014,
[author PDF](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
Theorems 1.28 (p.12), 3.19 (p.55), 3.24 and proof (p.59), inspected.
They give local finite-Lp mollifier convergence, weak-derivative
commutation, and finite-p Sobolev approximation. Periodic convolution,
uniform jet support and paired polynomial losses are the necessary
specializations to test, not asserted conclusions of Theorem 3.24 on
R^n. In particular do not apply its global integrability premise to
a nonzero periodic function on R or demand W^{2,infinity} norm density.

The Stony Brook Sobolev notes surfaced and were read at Theorem 5.1.1
and surrounding approximation statements, but are not used: their
displayed p=infinity convergence claims would need qualification.
Hunter's finite-p statements supply the assessed smoothing input.

## Decision, missing estimate and bounded continuation

No citation alone gives the original target. In particular:

- Periodic g is not an input with zero value and first-derivative traces
  on a ball. Subtracting a boundary interpolant and restoring it would
  require estimates for the restored part; its support cannot be ignored.
- Controlling D^2 alone on an interval of length P does not state a
  P-independent bound for g and g'. All three orders at both lags matter.
- Bad-set measure and full energy do not state the required signed
  paired moment errors. The four tiny odd bounds must retain their
  periodic integration-by-parts mechanism, not an O(1) error substitute.
- Neither a fixed-function tail limit nor L473's full O(ell^4) fourth
  bound provides an O(ell^3) loss on an H-dependent exceptional set.

These are missing applicability steps, not a proof of failure for the
actual Hardy path. The bounded continuation isolates periodic extension
and smoothing **conditionally** on explicit weighted bad-phase budgets;
its exact proposed assumptions and stop test are in
`2026-10-31-periodic-whitney-weighted-reduction.md`. No adaptation,
new inequality or counterexample is derived in this literature turn.

Queries included `periodic higher order Lipschitz truncation`,
`second order Lipschitz truncation C2 periodic`,
`Friesecke Proposition A.2 W2`, `periodic Lipschitz truncation higher
derivatives`, and `Hunter PDE Sobolev mollification Theorem`.
Search snippets and unrelated PDE abstracts were not theorem evidence.
Matching Mathlib coverage is unchecked. No cross-notebook input.

Successful support enforcement would repair one missing L582 interface;
positive clipping and actual-Xi signs would remain open. This source
review supplies no justified central creative mechanism: its concrete
continuation is development of a classical truncation method.
