# Cluster-enclosure detector — source review1256

TARGET: Review a quantitative L032 cluster detector on a zero-centered disk, a real interval and a conjugate pair of disjoint off-axis disks, seeking explicit degree and coefficient bounds for Q(q)<=-1 from support enclosures and total mass, without separation inside clusters.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for constructive/quantitative Runge approximation, explicit degree on unions of disks and pole-moving proofs located Schönlein, Burkill and Boas. Read the primary theorem/proof cases below; reused reviews157/381, L032/L895 and the named cluster stops. No exact enclosure-to-Q bound was found; no novelty inference.
SOURCE_EVIDENCE: Boas, Math618 notes (29April2016), Section4/4.1 pp26-28; Burkill, Lectures on Approximation by Polynomials (TIFR1959), concluding Runge section TheoremA and pole-moving lemma pp60-62; Schönlein DOI10.1007/s00498-023-00364-3 Section2.2 Theorem3/Steps1-4 pp258-263; Sete-Liesen arXiv1502.07633v2 Theorems2.1/2.3, equations2.6-2.7 pp3-5. Precise links, hypotheses and qualifications below.
COMPARISON: Standard Runge and its finite pole-chain proof cover the analytic approximation tools without internal node separation. They do not state the requested degree/coefficient/full-Q certificate. Schönlein's printed direct finite formulas have unresolved convergence, sign and quadrature comparisons and are not imported. L895 and the finite Li observable do not supply the changed specialization.
GAP: A quantitative geometric construction, explicit degree and coefficient bounds, real symmetry and complete summable-node Q error remain unproved. Actual-Xi support, a nonreal cluster and all-degree signs remain separate. No enclosure witness has been derived.
REASON: Essential source coverage now supports one later specialization of the standard finite Cauchy/pole-chain construction. Recompute its constants for this geometry rather than reprove Runge qualitatively or import suspect printed constants. This is tool approval, not approval of the missing detector proof; the newly covered continuation receives separate next-turn approval.
SCOPE: Exactly nomination1255's support and mass data, boundaries/multiplicities included, no separation within a disk and no exact cluster count. Covers the finite Runge pole-chain construction and its degree/coefficient/full-Q accounting only; no Li conversion, general support, height-only cutoff or actual-Xi signing mechanism.
COVERED_TARGET: Construct a collision-tolerant L032 cluster detector under nomination1255's support and mass hypotheses using finite Runge pole chains, with explicit degree and coefficient bounds and the complete inequality Q(q)<=-1.
LITERATURE_REASON: The enclosure-only support geometry is outside the ready exact-node and earlier two-window assessments; its essential constructive approximation coverage was explicitly REVIEW_REQUIRED at turn start. Reuse earlier adequate comparisons instead of repeating their searches.

## Gap and conditional target

The main gap remains L030-L032/C032a actual-Xi algebraic-square
positivity in every degree. The intermediate target is an effective
negative detector from cluster enclosures. Its plausible use is a later
finite logarithmic-coefficient certificate robust to coalescing nodes.
That use still requires actual support/mass data and actual signs.

Retain nomination1255 verbatim as the original question. For clarity,
the data are a conjugation-invariant nonzero multiset with multiplicity,
sum_j |beta_j|<=A<infinity; 0<r_0<B; Im(w)>r_1>0; E_0 the union of
the closed zero-centered r_0 disk and [-B,B]; E_+ and E_- the closed
r_1 disks centered at w and conjugate(w). The three sets are pairwise
disjoint and lie in |z|<=B. Every node lies in their union and E_+
contains a node. Repeated locations and boundary nodes are allowed.
No individual locations, multiplicities or internal separation are given.

The later result sought is an explicitly constructed real polynomial,
with degree and coefficient-l1 bounds expressed solely in these data,
whose complete algebraic-square form is <=-1. A finite formula or
specified terminating recurrence is acceptable; an unspecified onset or
unbounded search with no quantitative control is not. No stronger input
representation is silently assumed: numerical implementation would need
certified representations of the parameters, whereas the present target
asks for mathematical expressions in the supplied parameters.

## Primary approximation coverage

H. P. Boas, [Class Notes, Math618: Complex Variables II](https://haroldpboas.gitlab.io/courses/618-2016a/notes2016.pdf),
updated 29 April2016, Section4's named Runge theorem p26 and Section4.1
pp27-28 (PDF indices25-27): compact K, f holomorphic on a neighborhood
of K; rational uniform approximation with prescribed poles in each
bounded complementary component, and polynomial approximation when
there are no such components. The neighborhood need not be connected.
Read the finite-cycle Cauchy/Riemann-sum proof, including grid-edge
points, and the pole-pushing proof. It explicitly requires
|z_0-z_1|<dist(z_1,K) for one geometric-series move, handles poles in
bounded versus unbounded complementary components separately, and
finishes the latter with a Taylor expansion outside a containing disk.
The source charges uniformity through separation from the cycle but
gives no final degree or coefficient formula. Before application the
later proof must verify the no-hole geometry and construct a separated
analytic neighborhood; a mere drawing or generic density assertion
does not pay those steps. This is the compact-set theorem to use,
rather than a theorem requiring f on one connected simply connected
domain across the three components.

J. G. Burkill, [Lectures on Approximation by Polynomials](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr16.pdf),
TIFR1959, concluding section1, TheoremA pp60-62 and unnamed lemma p61
(PDF indices63-65). The lemma assumes a simple arc from z_0 to z_1
disjoint from compact K and a rational function with only possible pole
z_0. It supplies uniform approximation by rational functions with only
possible pole z_1. Read the whole lemma and polynomial-completion case:
take 2d=dist(arc,K), subdivide with successive distances <=d, and
truncate the Laurent expansion of the entire current pole polynomial
at each move. Errors are allocated over the finite chain. TheoremA
then moves poles beyond a containing disk and truncates a Taylor series.
This explicitly includes higher-order poles generated by earlier moves;
repeatedly applying a simple-pole formula without accounting for those
powers is insufficient. Burkill leaves truncation orders unspecified.
Use the cited construction as a known tool; developing effective orders,
coefficient norms and a geometric chain is the proposed specialization,
not a claimed new proof of Runge or a completed bound.

M. Schönlein, [Polynomial methods to construct inputs for uniformly
ensemble reachable linear systems](https://link.springer.com/article/10.1007/s00498-023-00364-3),
MCSS36 (2024),251-296, published online7 September2023,
Section2.2 Theorem3/Steps1-4 pp258-263. Read all four steps in HTML
and checked the relevant displayed formulas in the publisher PDF text.
The theorem assumes compact K with connected complement and f
holomorphic on a neighborhood. Its finite formulas are not imported:
Step2 prints M=floor(6pi/(epsilon delta^2 L N)), while its error bound
is N delta^2 L/(2pi M). Step3's series and logarithms require
delta_kl<alpha, absent from its stated choice |b|>2eta; the kernels
also change from 1/(w-z) to 1/(z-w). Step4 uses further truncation
comparisons. These unresolved source comparisons block copying its
constants; no repaired theorem or new counterexample is asserted.
The primary standard chain proof above avoids making this one-move
construction an essential input.

O. Sete and J. Liesen, [Properties and examples of Faber-Walsh
polynomials](https://arxiv.org/pdf/1502.07633v2), version2,
manuscript dated12 May2022, Theorems2.1/2.3 pp3-5 and(2.6)-(2.7).
Reuse review381's assessment; checked these statements and coefficient
formulas for the changed geometry. The compact pieces must be mutually
exterior, simply connected and nonpoint. For a fixed analytic function,
the series has root convergence factor1/rho determined by its maximal
single-valued extension to Green-level interiors. The conformal map,
admissible-center constants, level separation and finite coefficient
bounds are not supplied for this geometry. This is a stronger rate
comparison, not an effective detector import. Walsh's original proof
was not newly inspected; no assertion depends on treating its
asymptotic constants as explicit.

## Duplicates, failures and search limits

Read L032/L895 in full. L895's inverse separations concern distinct
exact head locations; its complete mass/error accounting remains useful,
but does not bound enclosure-only conditioning. Multiplicity is mass,
not an independent negative direction. Review157's inspected Palojarvi
Theorem3.1 is a different Li zero sum; reuse that comparison without a
new search or automatic Li-to-mixed transfer. Review381's Calvi
Hermite remainder covers finite specified interpolation nodes, not the
required enclosure construction; its primary theorem was not newly
reproved. No internal interpolation grid has been proposed here.

The local cluster-search matches include the minimum-norm exact-recovery
stop for L646 and angular-grouping stop for L647; read their short
ATTEMPTS records. Those concern Blaschke/energy observables and their
particular normalization or grouping classes. Neither is a general ban
on cluster approximation, and neither pays this beta^2 polynomial form.
C030y's audited fixed-Grunsky stop and the spin-realization stops97/98
remain preserved as compared in nomination1255; no reopening occurs.

Queries actually used included `constructive Runge theorem quantitative
polynomial approximation explicit degree compact connected complement
Cauchy integral pole moving`; `quantitative Runge theorem polynomial
approximation union disks explicit degree bounds`; and `Runge theorem
proof move pole path distance geometric series lecture notes`. Local
searches used cluster/enclosure/Runge/Mergelyan and the exact new source
title/DOI against the active assessments, foundations and failure records.

The UCI Viaclovsky2023 notes failed retrieval at both host variants;
the modern TIFR URL returned404, but the older official TIFR URL above
provided the entire relevant section. These are resolved/nonessential
access limits. Calvi's PDF was accessible but no new content beyond
review381 was used. The Saff survey, multiplier-universality article,
disjoint-segment amplification paper and other search hits are unused
leads, not inspected inputs. Search snippets establish none of the
imported mathematics. Mathlib coverage of the complete quantitative
detector is unchecked; no theorem's absence is asserted.

## Decision and separate continuation

SPECIALIZE covers the standard finite Cauchy/pole-chain tools, while
leaving the actual quantitative detector open. A later attempt should
retain all components, the accumulation at zero, algebraic rather than
modulus squares, conjugation/multiplicity and the full summable tail.
It must construct the neighborhood/cycle/chains from the geometry and
pay uniform truncation orders and coefficient growth, including higher
pole powers. Merely citing Runge's existence statement fails the target.
No polynomial recipe or new error inequality is proved in this review.

Continue this specialization only with explicit finite bounds and a
full Q<=-1 certificate, or a precise informative obstruction to that
construction. If a chain requires unpaid geometric data, or constants
depend on unknown locations or internal separation, preserve that failure
and park that construction. A failed absolute estimate is not a proof
that every enclosure detector fails. Finite sampling and asymptotic
root rates do not meet the test. No actual-Xi conclusion follows.

Essential local inputs for the later proof are L032/L895 and L030's
form normalization; L024/L025 and L018/L026 are needed only for any
subsequent Xi interpretation. Their actual data and all-degree signs,
theta signing, realization and initialization remain unresolved. There
is no cross-notebook theorem input. A successful bound would be a local
quantitative specialization of known approximation, not certified
original mathematics or progress beyond the sources checked.

The sole newly covered action is the COVERED_TARGET above. Its separate
next-turn approval is required before research; it is proposed as
proof_attempt/development. No justified new central signing mechanism
emerged: the theta-specific sign input remains missing, so this known-tool
specialization is not labeled creative to satisfy a scheduling preference.
No lemmas, mathematical scripts, PROOF or DAG were changed.
