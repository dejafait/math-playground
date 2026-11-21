# Cluster-enclosure polynomial detector — nomination1255

TARGET: Review a quantitative L032 cluster detector on a zero-centered disk, a real interval and a conjugate pair of disjoint off-axis disks, seeking explicit degree and coefficient bounds for Q(q)<=-1 from support enclosures and total mass, without separation inside clusters.
CHECKED: 2026-11-17
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Scoped local searches for quantitative L032 detectors, witness degree, node separation, cluster witnesses, Runge degree and Faber-Walsh found L895, review157, review381 and different contour/cluster observables. Read L032/L895 in full and review157 in full; read the opening scope of review381 and the matched cluster nominations. No complete external theorem comparison for this new target was performed; no novelty inference.
SOURCE_EVIDENCE: L032/L895 provide the existing exact-node interpolation proofs. Review157 records Palojarvi arXiv:1807.01506v2 https://arxiv.org/pdf/1807.01506v2 Theorem3.1 as a different Li observable. Review381 records Sete-Liesen arXiv:1502.07633v2 https://arxiv.org/pdf/1502.07633v2 Theorems2.1/2.3 and Calvi https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf Theorems1.9/1.17/1.18 as approximation tools; their complete statements/proof cases for this geometry have not been inspected here. They are leads or reusable source notes, not approved inputs for the proposed bound.
COMPARISON: L895 requires exact distinct head locations and its constants contain inverse separations. Review157 leaves the height/deviation-only bound unpaid and parks automatic Li-to-mixed transfer. The new conditional target supplies a support geometry and total mass instead, allows arbitrary collisions within each disk, and asks for a single negative direction, not a multipair inertia count or a height-only bound. Existing band approximation and inverse-Blaschke cluster targets concern different kernels and errors.
GAP: Essential quantitative polynomial-approximation hypotheses, construction, degree and coefficient bounds, and full summable-node error accounting are uncovered. No cluster witness or obstruction has been derived. Actual-Xi support enclosures, a nonreal cluster, and actual-Xi all-degree signs remain separate unproved data.
REASON: A different, independently testable detection gap remains after the audited fixed-Grunsky stop. Coverage must be assessed in a separate literature-only step before mathematics. This nomination does not reopen the fixed ansatz, an automatic spin import or a blocked source retrieval.
SCOPE: Review only the conditional support-enclosure problem below. No height-only cutoff, off-line zero existence, actual-Xi sign, general univalence construction, new lemma or mathematical script is approved.

## Proposed bounded problem, not a result

The main gap is L030-L032/C032a actual-Xi Q(q)>=0 in every degree.
The independent intermediate gap is robustness of a conditional negative
detector when only cluster enclosures, rather than individually separated
node locations, are supplied. A bounded degree and coefficient norm could
make a later logarithmic-coefficient certificate usable near coalescing
zeros. It cannot supply the missing actual signs or prove RH.

For a later mathematical target, propose the following explicit data.
The nonzero multiset (beta_j) is conjugation invariant with multiplicity
and sum_j |beta_j|<=A<infinity. Supply 0<r_0<B, a center w with Im(w)>0,
and r_1>0. Let E_0 be the closed disk |z|<=r_0 together with the real
interval [-B,B], and let E_+ and E_- be the closed disks of radius r_1
centered at w and conjugate(w). Require E_+,E_- to be disjoint from
each other and from E_0, all three sets to lie in |z|<=B, and
Im(w)>r_1. Every node is in E_0 union E_+ union E_-, and at least one
node lies in E_+. These are supplied hypotheses, including the full
support enclosure; no actual-Xi realization is asserted. Boundary
nodes are included. No exact cluster count or separation between
distinct nodes in a single disk is supplied. Repeated nodes are allowed.

Ask whether these data permit an explicitly constructed real polynomial
q, with a computable degree bound D and coefficient l1 bound C depending
only on A,B,r_0,r_1,w and their stated geometric separations, such that
the full algebraic-square sum Q(q)<=-1. A bound on approximation error
must account for every node and its multiplicity, including the disk
accumulation at zero. No partial-sum or floating-point evidence suffices.
An existence theorem with no effective D,C is a useful comparison but
does not finish this proposed quantitative target. No approximation
recipe, error inequality or negative-witness proof is derived here.

The test is conditional and narrower than height/deviation-only
detection: unknown other nonreal head clusters are not allowed outside
the specified support. A successful one-direction detector would not
count each colliding copy as an independent negative direction. Actual
use requires separately paying the support and mass inputs, then
L024/L025/L030's normalization. L032/L895 are the essential existing
local inputs; L018/L026 fix actual-Xi interpretation only. There is no
cross-notebook input. Full Mathlib coverage is unchecked.

## Three mechanisms considered for continuation

1. The fixed linear Grunsky deficit is now independently audited in
   C030y/audit1255 and is incompatible already at degree five. Preserve
   stop1253. More degree or a renamed ansatz supplies no new mechanism.
2. A direct positive-spin realization of the theta law lacks a specified
   new construction. Reuse the November7 block-spin assessment and
   stops97/98: L896 excludes the stated fixed finite quartic class,
   while varying-dimensional limits remain unproved. No new input
   justifies another automatic Lee-Yang/GHS search.
3. The selected cluster-enclosure detector changes the objective to
   conditional, collision-tolerant polynomial detection. L895 already
   pays exact-head detection; review157's Li conversion does not pay
   this enclosure-only target. The new discriminating hypothesis is
   geometric separation of compact sets, not separation of locations
   inside a cluster. The theorem-level comparison remains incomplete.

This comparison selects a different gap; it does not claim that the
third mechanism has been source approved. Review approximation sources
and their exact hypotheses/proof cases before any construction. Reuse
review381's existing source notes if applicable; do not repeat generic
searches or import fixed-function asymptotic rates as explicit constants.

Continue only if source coverage provides a concrete finite-degree
construction or a precise, independently testable obstruction under
these data. Park this quantitative formulation if the only tools require
unpaid internal node separation or yield no effective degree/norm
information. Preserve informative weaker conclusions with their actual
hypotheses; do not announce a height-only bound or a new zero-free region.
An adequate assessment may approve a later bounded specialization,
but this REVIEW_REQUIRED nomination approves none.

No justified creative central signing mechanism emerged from the
bounded audit. Its blocker is a theta-specific algebraic-square sign
estimate, not a lack of further equivalent criteria. This conditional
detection tool is not labeled creative to meet scheduling preferences.
Next routing is literature_comparison, standard/high; a subsequent
research purpose must follow the actual theorem comparison.
