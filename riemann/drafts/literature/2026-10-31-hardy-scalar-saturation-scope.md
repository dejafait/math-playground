# Smooth scalar saturation: completed source comparison

TARGET: Assess source coverage for smooth scalar saturation of L582 that preserves L473's paired moment tolerances and enforces paired jet norm at most (log H)^2.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched scalar/Sobolev composition, higher-order Lipschitz truncation, Hardy derivative moments and large derivatives; inspected Bourdaud's chain-rule theorem, Irving's truncation proposition and relevant proof cases, Curran's joint-moment theorem, and Phung's Hermite statements/formula. No inspected theorem supplies the full target; no originality inference follows.
SOURCE_EVIDENCE: Bourdaud arXiv:2401.16987v1 Sections 1--3.1.2, Theorems 1--2; Irving DOI 10.1007/s10231-025-01547-2, Proposition 2.10, (2.45)--(2.61); Curran arXiv:2106.00165v1, Theorem 1 and Proposition 1, pp.1--2, Hardy conversion pp.5--7; Phung DOI 10.4171/ZAA/1612, Theorems 2.1--2.2, pp.253--254. Reuse L582's closure audit and L473's arithmetic coverage, with their unaudited-source qualifications.
COMPARISON: Smooth composition retains derivative factors; finite-p composition bounds do not certify hard jet support. Higher-order Lipschitz truncation is a spatial extension operation, not scalar saturation, and supplies neither this periodic C2 law nor all paired moment errors. The inspected Hardy moment results do not give the necessary amplitude-conditioned derivative bounds and nonlinear loss estimates.
GAP: Full saturation of the specified L582 path remains unresolved. A bounded bridge-modification test can instead determine whether its available moment tolerances and coarse jet bound alone suffice for scalar cutoffs normalized by phi_H'(0)=1; it cannot settle the prescribed Hardy path or arbitrary scalar maps.
REASON: Coverage supports the restricted obstruction test below using established Hermite interpolation and the classical chain rule; no essential inaccessible theorem is needed for that test. Park direct certification of full scalar saturation from the current estimates. No bridge modification or new mathematical result is derived in this literature-only review.
LITERATURE_REASON: The startup target was REVIEW_REQUIRED: nonlinear scalar composition and deterministic derivative support lie outside the ready L582 closure/audit scope. This is its first source comparison, not additional literature on the ready audit.
SCOPE: Retain H real on one eventual ray, ell=log H fixed, period P=H ell+1, both lags 0 and 1, ordinary derivatives through two, L473's exact 21 second/126 fourth tolerances and uniform constants. Full actual-path saturation is unproved; only the following restricted generic-certification test has ready coverage. Positive clipping, exact nu_H realization and Xi transfer are independent.
COVERED_TARGET: Test a unit-bridge modification of L582 that retains all 147 L473 tolerances and O(H^(1/6)) jet bounds but defeats paired (log H)^2 support after every C2 scalar cutoff with phi_H(0)=0 and phi_H'(0)=1.

## Gap, intended use and review result

The main gap remains actual-Xi signs at unbounded heights and all-degree
positivity. The intermediate support target would strengthen L582's
stationary changed marginal toward a bounded derivative-consistent law.
Even success would leave positive clipped mass and actual-Xi transfer
open. This review establishes source scope, not feasibility or an
impossibility theorem for scalar saturation of the specified g_H.

Keep the exact tolerances: ordinary second errors O(1); at both lags,
absolute value/first and first/second moments O(H^(-2/3)ell^(-1)) and
O(H^(-2/3)ell^(-3)), respectively; every fourth error O_m(ell^3).
The hard bound is the Euclidean norm of all six lagged coordinates,
not an amplitude bound or a high-probability estimate. Constants and
onsets must be common on an eventual ray, not along selected heights.

## Inspected primary results

**Composition.** Gérard Bourdaud, *The higher order chain rule in Sobolev
spaces*, [arXiv:2401.16987v1](https://arxiv.org/html/2401.16987v1),
Sections 1--3.1.2, equations (1)--(5),(8)--(12), Theorems 1--2.
Inputs are A-dot^m_p=W-dot^{m,p} intersect W-dot^{1,mp}, finite p>=1,
m>=2, and phi' in W^{m-1}_{E_p}, with E_p uniformly local Lp.
Composition stays in that space; its chain rule permits a null-set
modification generally. Both smooth-generator proof cases, fewer-than-m
and m derivative factors, were inspected. These finite-p conclusions
do not certify deterministic second-jet support.

For C2 scalar functions the classical second-order Faà di Bruno rule,
recalled in Section 1, reads

    (phi o g)' = phi'(g) g',
    (phi o g)'' = phi''(g) (g')^2 + phi'(g) g''.

Only this classical identity is needed for the C2 periodic-path test.
No global Sobolev theorem on R is applied to a nonintegrable periodic
function. The derivative factors remain; no new estimate is proved.

**Derivative truncation is a different operation.** Christopher Irving,
*Partial regularity for minima of higher-order quasiconvex integrands
with natural Orlicz growth*, Ann. Mat. Pura Appl. (2025),
[DOI 10.1007/s10231-025-01547-2](https://doi.org/10.1007/s10231-025-01547-2),
[full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259811/),
Proposition 2.10, (2.45)--(2.61), was inspected. Its input is
q in W_0^{k,Phi}(B_R;R^N), with Phi an N-function satisfying Delta_2 and
nabla_2. It supplies a W_0^{k,infinity} modification with kth derivative
bounded by C lambda, controlled integral energy, and a modification-set
measure estimate. The proof first zero-extends and rescales; its good
set uses maximal functions of all derivatives through k. It constructs
Taylor jets on a closed good set and extends them with boundary jets.
This is not a scalar map of q's value. Periodic boundary conditions,
C2 regularity and the required paired fourth losses are not supplied.
No adaptation or source-proof audit is attempted. Friesecke--James--
Mueller Proposition A.2, cited there for k=2, remains an unread lead;
it is unnecessary for the independent Hermite test.

**Actual Hardy tails.** Michael J. Curran, *Upper bounds for fractional
joint moments of the Riemann zeta function*,
[arXiv:2106.00165v1](https://arxiv.org/pdf/2106.00165v1), definitions
and Theorem 1 on pp.1--2, Proposition 1 and its Holder reduction on p.2,
and the Hardy conversion in the twisted-moment proof, pp.5--7, were
inspected. Unconditionally, for 1<=k<=2, 0<=h<=1, the integral over
[T,2T] of |Z|^(2k-2h)|Z'|^(2h) is O(T(log T)^(k^2+2h)); the analogous
zeta bound also holds. This theorem involves Z and Z', not Z'', and
neither prescribes paired lags nor conditions derivative sizes on
small amplitude. It is not the missing hard-support or nonlinear
fourth-loss theorem. Its arithmetic proof remains unaudited.

Reuse L473 (6),(9)--(10) and L582's fixed-order pointwise imports; do not
redo their source assessments. Bui--Hall v1 Introduction and Section
4.2's Proposition 3 were consulted only to compare their scope with
the changed operation. Their ordinary second/fourth data and fixed-order
pointwise upper bounds do not state amplitude-conditioned pointwise
control of the composed jet or the required weighted tail losses.
In particular an untruncated fourth norm bound is not a quantified
fourth-moment truncation error. No stronger Hardy tail estimate has
been established by this search. This is a limitation of inspected
coverage, not a claim that no stronger theorem exists.

**Ready interpolation input for an obstruction test.** Van Manh Phung,
*Continuity and Convergence Properties of Integral Means of Bojanov--Xu
Interpolation*, Z. Anal. Anwend. 37 (2018), 251--268,
[DOI 10.4171/ZAA/1612](https://doi.org/10.4171/ZAA/1612),
[publisher PDF](https://ems.press/content/serial-article-files/35980),
Theorems 2.1--2.2, pp.253--254, were inspected at their full statements
and interpolation formula. Distinct real nodes with positive
multiplicities and supplied derivatives determine a unique polynomial
of degree below the total multiplicity; Theorem 2.2 supplies its basis.
Fixed nodes with value/first/second data fall within this input.
Endpoint and interior jet prescriptions are therefore within its
standard interpolation scope. A later attempt must still compute the
operator bound and moment comparison for its chosen data; neither
follows quantitatively from existence alone. This is a specialization
of a known theorem, not a reason to reprove interpolation or claim a
new general composition obstruction.

## Search, duplicates and access qualifications

Queries included `higher order Lipschitz truncation second order Sobolev
composition scalar truncation derivatives bounded`; `Nemytskii
composition Sobolev second derivative smooth truncation chain rule
bounded derivatives`; `Bourdaud composition operators Sobolev spaces
survey 2023 chain rule`; `Hardy Z function derivatives large values at
zeros lower bound derivative maximum unconditional`; and `Hardy
derivatives moments upper bounds Z(t) high moments`. Exact statement,
standard superposition terminology and stronger derivative-truncation
operations were compared. No inspected result directly decides the
full Hardy saturation target or the precise bridge-localized test.

The general Nemytskii paper DOI 10.1016/j.na.2021.112576 returned 403;
search-result excerpts are not theorem evidence. Bourdaud's primary
chain-rule paper is accessible and suffices for the restricted test.
An attempted Curran HTML v2 URL returned 404; the inspected PDF v1
supplies the cited statement and cases. Blanc's large-derivative search
lead assumes RH, and no theorem from it is imported. Ivić's
large-values paper was discovery only, not an inspected zero-slope
obstruction. These leads do not establish failure at actual Hardy zeros.
No essential inaccessible source blocks the nominated test.

Narrow local checks covered L582/L473, the ready periodic-closure and
stationary-path assessments, the paired-Hardy assessments, and the
stationary-process/exact-law stops. The saved scalar-saturation
nomination had no completed test. The Laplace/global-polynomial
saturation stops concern other operations; they do not ban this one.
L581 excludes the exact corrected nu_H extension, whereas the proposed
test changes a periodic bridge and a marginal. Preserve those stops.
No cross-notebook result is used. Full matching Mathlib coverage for
this saturation target is unchecked; no absence claim is made.

## Restricted continuation, pending separate approval

Use only L582, L473's exact tolerances and imported norm inputs,
Phung's fixed-node Hermite theorem and the classical chain rule.
Keep L582's actual Hardy segment, period, endpoints and all joins;
permit a different C2 bridge only on [L,L+1], L=H ell. Test a fixed
interior jet prescription at bridge coordinate 1/2: value and first
derivative zero, second derivative 2 ell^2. This is proposed test data,
not a constructed function or proved conclusion. Do not alter L582's
canonical specified quintic or attribute the modification to it.

The test must certify, or fail to certify, a uniform O(H^(1/6)) bound
through order two, all 21/126 tolerances for the modified periodic law,
and failure of the paired ell^2 support for every C2 phi_H with
phi_H(0)=0, phi_H'(0)=1. Check a positive-measure set of phases for
each phi_H: a single exceptional phase is insufficient for a statement
about probability support. All four tight odd moments require their
absolute periodic cancellation, not generic O(1) error estimates.
No cutoff or bridge formula is calculated in this source turn.

Success would show that the retained moment data and coarse pointwise
scale alone cannot justify this normalized scalar-cutoff method
uniformly over compatible bridges. It would not refute saturation of
the original specified L582 path, exclude maps with a different slope
at zero, preserve positive clipping, or prove anything about actual-Xi
signs. Failure of this particular bridge test is not evidence that
saturation works. Stop this test if its joins, operator bound, any
moment tolerance or positive-measure support comparison fails; retain
the exact failed requirement rather than weakening the target.

The full actual-path mechanism remains parked pending amplitude-
conditioned derivative information and quantitative nonlinear moment
losses, or a materially different argument. Higher-order spatial
truncation remains unapproved here. No justified central creative
nomination emerges: this bounded generic-certification test is routine
specialization and supplies no new mechanism for clipped positivity or
actual-Xi signs. No lemmas/, scripts/, DAG or PROOF edits are warranted
by this literature result.
