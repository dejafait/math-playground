# Genus-two Cassels–Tate pairing test — source comparison

TARGET: Test whether two classes from L145's surviving supported witness subspace have certified Selmer membership and a nonzero Cassels–Tate pairing relevant to the rank bound.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared ATTEMPTS/038,045,052,062–064, L138/L139/L145 and the existing support/local-image assessments; searched genus-two Cassels–Tate algorithms, nonsplit two-torsion, Shukla–Stoll odd-degree methods and exact coefficient variants 67760/76835. Found Fisher–Yan's general algorithm and author code; no inspected exact-instance pairing was found. Failed searches do not establish novelty.
SOURCE_EVIDENCE: Fisher–Yan author PDF dated 14 September 2023, 49 pages: equations (1)–(2) p.2, Section 2.3 pp.10–11, Definition 2.7 and construction pp.13–14, Section 3 pp.18–20, Theorem 3.5/complete proof pp.21–24, Remark 3.6, Theorem 3.9/complete proof p.25, Theorem 3.20/Remark 3.21 pp.30–31, Definition 3.22/Lemma 3.23 and Proposition 3.24/Lemma 3.25 discussion pp.31–33, Section 4 steps (i)–(x)/Remark 4.1 pp.34–35 and Theorem 4.4/complete proof pp.36–37; author genus2ctp.m interfaces and single-pair branch, plus demo.m; Yan arXiv:2109.08258v1 introductory/setup hypotheses. Reused inspected Stoll membership, support and local-image results named below.
COMPARISON: Fisher–Yan covers arbitrary Weierstrass Galois action and supplies a single-pair formula, without requiring a complete supported-group basis as a theorem hypothesis. It requires two actual Selmer classes, compatible covering models, a rational twisted-Kummer point and certified liftable local points. Yan's full-rational-two-torsion shortcut is inapplicable. No source computes this instance or supplies the missing classes/point.
GAP: Instance membership at 3 and 5, exact odd-to-sextic class transport, compatible covering models, a suitable rational twisted-Kummer point, the evaluation function and its complete finite-place certificate remain uncomputed. The witness coefficient space is neither a Selmer basis nor proved globally independent. General method coverage is ready; execution and nonzero value are unestablished.
REASON: Completes the separate source gate for the unchanged target. Approves one bounded application of published descent/pairing methods, beginning with the missing membership conditions; no new lemma, mathematical script, pair evaluation or rank claim is made in this literature turn.
LITERATURE_REASON: Essential primary hypotheses and evaluation formulas for this new global pairing mechanism were unread at invocation start; the prior local and reverse-isogeny assessments did not cover them.
SCOPE: Exactly TARGET on the fixed L138 Jacobian, L139 supported norm kernel and L145's 39-witness coefficient space after its accepted filters; membership at 3 and 5, one compatible pair and conditional one-value evaluation by Fisher–Yan. No enlarged global box, complete unit/class computation, full pairing matrix, backend availability sweep, renewed fixed-image refinement or point classification.

## Intended bounded target and downstream use

Use the actual genus-two J=Jac(B) from L138, its supported ambient
space from L139, and the fixed 39-witness coefficient space used in
L140/L141/L145. The candidate subspace is the inverse image of the
accepted real, 11-adic and dyadic images in that finite coefficient
space. No assertion that it exhausts the supported group, or lies in
the two-Selmer group, is made.

The prospective discriminating test is one pair of represented classes:
first authenticate membership in the precise domain of a sourced
Cassels–Tate pairing, then test for a nonzero value. A useful nonzero
value would have to exclude Mordell–Weil classes or improve the rank
bound by a precisely cited theorem. The size of any improvement is not
claimed here. The present bound 5+c<=7 still misses the sufficient bound
one by six; even an improvement leaves independent point-control,
integer-recovery and other-signature gaps.

This separate literature turn inspected those hypotheses and essential
proof/evaluation cases. General source coverage is now ready for a later
mathematical invocation; no candidate pair was selected or evaluated.
Import the existing algorithm rather than reprove it. Do not apply a
pairing on Sha or a Selmer group to an arbitrary supported norm-square
class. The entry gate remains actual membership, especially at 3 and 5.

Continue only with a precise, applicable formula and a bounded membership
and nonzero-value test on the saved space. If the source requires missing
global data that cannot be independently supplied within a bounded test,
or the proposed pairing reduces to an already stopped identity, record
that obstruction and select a materially different target. A zero value
on one pair would not establish global vanishing.

## Recorded stops and unresolved inputs

ATTEMPTS/064 now has an accepted saturation proof. ATTEMPTS/062 stops
the exact same-coordinate split-isogeny shortcut; ATTEMPTS/063 stops the
norm-trivial mixed coefficient filter at 3. The narrow summary in
ATTEMPTS/038 records cancellation in a different five-probe reciprocity
envelope; that historical proof was not imported or reread here. Any
new proposal must distinguish its actual domain and pairing from those
mechanisms. Existing finite Weil-pairing coverage is not a Cassels–Tate
assessment. These searches do not establish originality.

Essential continuation inputs are L138/L139/L140/L141/L145 and, for
comparison of stopped mechanisms, L142/L143/L144/L146. The full witness
and local-image evidence is in
`scripts/pair-genus-two/two-adic-filter-certificate.json`, with accepted
audit `scripts/pair-genus-two/two-adic-filter-audit.json`. Global
unit/class generation, membership of proposed classes in the necessary
Selmer group and all pairing-specific hypotheses remain unresolved.
No cross-notebook theorem is proposed. Full matching Mathlib coverage
is not checked. Only the bounded scope specified above is approved.

## Primary imports, hypotheses and essential cases

The principal source is T. Fisher and J. Yan, *Computing the
Cassels–Tate pairing on the 2-Selmer group of a genus 2 Jacobian*,
[author manuscript](https://www.dpmms.cam.ac.uk/~taf1000/papers/genus2ctp.pdf),
dated 14 September 2023, accessed 2026-10-28. The author file has **49**
pages; its numbering is used here. The separate
[arXiv:2306.06011v1 record](https://arxiv.org/abs/2306.06011v1) is dated
9 June 2023 and lists 48 pages. Do not transfer page numbers between
versions. The repository's accepted-version metadata is not the source
of the statements imported here.

**Domain and rank use.** Equations (1)–(2), p.2, and Section 3,
equation (40), pp.18–19, put the pairing on Sel^2(J/k), via Sha(J/k)[2],
for a genus-two Jacobian over a number field with its principal
polarization. Its radical contains J(k)/2J(k); the source identifies
the radical with the image of Sel^4. No finiteness of Sha is needed
for the rank upper bound from containment. The finiteness qualification
in Remark 3.3, p.20, concerns the stronger rank-parity statement and
must not be silently imported. For a computed pairing matrix M on the
full Selmer group, the familiar bound is

    rank J(k) <= dim Sel^2(J/k) − dim J(k)[2] − rank M.

The author's demo.m, lines 117–129 at access, explicitly subtracts the
even torsion dimension and matrix rank. Using a restriction to a
certified subgroup requires only a lower bound on the rank of the full
pairing, not a declaration that the subgroup exhausts Sel^2. A future
application must write that finite-dimensional linear-algebra argument
and its embedding in L145's ambient upper bound; it was not carried
out here. A nonzero pair alone does not determine the full pairing.

**Alternation qualification.** Section 2.3, Lemma 2.4 with its cocycle
description p.10, and Lemma 3.1 p.19 are the precise imports: the
canonical class c_can is represented using a Weierstrass point and
the pairing satisfies <x,x+c_can>=0. The general pairing need not be
alternating. L138 already provides a rational Weierstrass point, so
the rational-Weierstrass specialization is available; authenticate
c_can=0 when using it to claim a rank-two contribution from a nonzero
off-diagonal value. This c_can is unrelated to L139's integer c<=2.
No source requires all of J[2] to be rational for the general method.

**Coefficient representation.** Section 2.3, equations (20)–(23),
pp.10–11, distinguishes actual Selmer classes, the fake quotient by
c_can, and representatives (xi,m) with N(xi)=m^2 modulo
(r*nu^2,r^3*N(nu)). The sextic algebra has dimension six; L138's odd
algebra has dimension five and no scalar quotient. They must not be
identified by dropping a coordinate. Section 4 step (i), p.34, explicitly
recommends doing descent on a degree-five model when a rational
Weierstrass point is available and then transporting back to degree
six. L138 supplies the exact curve isomorphism and an existing sextic
W^2=11(T^2−4)Q4(T), so no new curve needs inventing. Correct transport
of the actual cohomology classes, including norm-root signs, is still
instance work; a curve isomorphism alone is not a saved class map.

**Construction and formula.** Definition 2.7, equation (29), p.13,
and equations (30)–(31)/construction pp.13–14 give covering models as
pairs of six-variable quadratic forms. The construction requires a
three-dimensional isotropic subspace, with the determinant choice
matching m. Its source proof uses local Selmer membership and the
quadratic-form Hasse principle; supported norm-square data alone do
not justify this construction. Remark 2.9 explains the Brauer–Severi
obstruction outside that domain. This is not a reproof or a new local
obstruction.

Theorem 3.5, pp.21–24, starts with eps,eta in Sel^2, a rational point
P on the eta-twisted Kummer surface, and its lift to J_eta over
k(sqrt(a)). It constructs phi:J_eps -> J_(eps+eta) and a rational
function g with

    div(g)=phi^*H_(eps+eta)+iota_eps^*(phi^*H_(eps+eta))−2H_eps,
    <eps,eta> = sum_v (a,g(P_v))_v in F_2.

Here P_v is on J_eps(k_v), avoiding zeros and poles. Remark 3.6(iii)
allows evaluation on K_eps only with a certified local lift. The
complete proof identifies the quadratic splitting cocycle, its divisor
lift, and the resulting quaternion algebra. A constant coefficient
Hilbert product or the mere existence of K_eps(k_v) is not this test.
If the rational Kummer point lifts rationally, the pairing with eta is
zero; the source treats this case before the theorem. Rational Kummer
points are not guaranteed to exist by Selmer membership.

Theorem 3.9 with its proof, p.25, gives
g=Phi_(eps,eta)(x;P;h)/x1^2. Theorem 3.20, p.30, expresses the twisted
form as a trace from the degree-ten partition algebra. Remark 3.21,
pp.30–31, warns that its square-root relation alone is insufficient
for general Galois action. The systematic choices in Definition 3.22,
Lemma 3.23, Proposition 3.24 and Lemma 3.25, pp.31–33, are needed;
the simplifying S6 example is not an applicable assumption on this
1,1,4 branch pattern. Use the complete published construction or its
author implementation, retaining all choices and exact identities.

**All-place certificate.** Theorem 4.4 with complete proof,
pp.36–37, assumes an integral sextic and a set containing infinity and
every prime dividing 2*f6*disc(f). At an omitted place the covering
model H must be integral, a a unit, and the numerator quadratic of g
integral with at least one unit coefficient. Then the contribution is
zero. Its proof uses an odd unramified extension, liftable smooth
residue points avoiding the numerator, and Hensel lifting. Thus the
pairing place set is **not automatically** L138's descent-support set:
denominators, content and primes of a must be checked and included.
All retained contributions require strict square/valuation precision
and actual local lifting, including at 2 and infinity.

## Reused membership coverage and available implementation

Reuse Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, Acta Arith. 98 (2001), 245–277,
[DOI 10.4064/aa98-3-4](https://www.impan.pl/shop/en/publication/transaction/download/product/83397):
Proposition 4.2 and Lemmas 4.1,4.3–4.4, p.250–251, characterize the
odd-model Selmer group by the actual local Jacobian images and give
local dimensions. Proposition 4.6 and Corollary 4.7, pp.252–253,
identify the valuation condition outside the sufficient support.
Section 6, Lemmas 6.1/6.3 and trace/norm generation pp.267–272 cover
degree-at-most-two divisors, branch and nonintegral cases. These exact
passages/proofs were inspected in the reused assessments
`2026-10-25-pair-genus-two-odd-model-support.md`,
`2026-10-26-pair-eleven-adic-filter.md` and
`2026-10-27-pair-two-adic-kummer-filter.md` in this directory. Their
scope matches this unchanged odd model; no repeat browsing is needed.

Consequently membership of particular supported classes can be
certified without proving generation of the global supported group:
all required local memberships and the outside-support valuation
argument must be supplied. Accepted L140/L141/L145 cover infinity,
11 and 2. No current result authenticates membership at 3 and 5 for
the surviving witness products. L144 is a scalar-quotient, norm-trivial
slice for a different map and cannot fill either missing odd-model
condition. The prior local-image algorithms apply to those new places,
but their actual factorization, square-class maps and complete images
must be certified before rejecting any candidate.

The [author's paper page](https://www.dpmms.cam.ac.uk/~taf1000/papers/genus2ctp.html)
links the [public implementation](https://github.com/TomAFisher/Cassels-Tate-pairing--Genus-2).
Read the live
[genus2ctp.m](https://raw.githubusercontent.com/TomAFisher/Cassels-Tate-pairing--Genus-2/main/genus2ctp.m)
header (February 2024), TwoDescentGenus2 interface lines 380–386,
TwoSelmerElementsGenus2 lines 439–444, exact local checking lines
1095–1158, CasselsTatePairingGenus2 contract lines 1362–1365 and its
single-pair hint branch lines 1466–1525; also
[demo.m](https://raw.githubusercontent.com/TomAFisher/Cassels-Tate-pairing--Genus-2/main/demo.m)
lines 0–41,117–129,191–205. These are mutable URLs with access date
2026-10-28, not pinned or locally executed software. A later import
must save/version the source actually used and independently verify
the exact outputs.

The single-pair branch accesses precisely the models for eps, eta and
eps+eta and a supplied rational point on K_eta. It does not certify
that arbitrary submitted models represent Selmer classes. Its comment
describes use over small quadratic fields; applicability of that code
path over Q should be checked before direct execution. The theorem
itself is over number fields and needs no extension of Q here. The
paper's Remark 4.1 recommends full-Selmer input for searching among
twists, but this is a practical recommendation, not a theorem requiring
a full basis for one evaluation. It cannot be used to justify an
unbounded full descent in this target.

The demo starts with SetClassGroupBounds("GRH"); do not adopt that
setting as an unconditional certificate. Neither a usable local Magma
installation nor a runtime bound was established here. Historical
ATTEMPTS/045 and /052 preserve backend blockers in other number
fields. Do not repeat software probes or substitute a remote service,
API key, conditional class bounds or guessed Selmer input. Local
membership calculations can proceed independently using the accepted
exact arithmetic techniques; a blocked pairing implementation is a
stopping point for this bounded attempt.

## Comparison, test limits and decision

Yan, [arXiv:2109.08258v1](https://arxiv.org/pdf/2109.08258), introductory
and setup passages pp.1–3, explicitly assumes full rational two-torsion
for its formula. L139's dimension one does not meet that assumption.
Fisher–Yan removes it; there is no reason to pass to the full splitting
field merely to use the older formula. The Shukla–Stoll odd-degree
approach is an alternative lead: the retrieved 2022 workshop material
and author research listings did not supply an inspected general
proof/implementation for this instance. No theorem from that lead is
imported, and failure to locate one is not a nonexistence claim.

ATTEMPTS/038 uses fixed global coefficient probes; ATTEMPTS/062 tests
exact same-coordinate point lifting; L143 concerns coefficient
representation; ATTEMPTS/063 and /064 saturate specific local images.
None is the torsor-dependent evaluation in Theorem 3.5. Their stops
remain binding on their own constructions; they do not prove this
pairing nonzero or zero. A zero pairing on one selected pair would not
reestablish any global redundancy claim.

Bound the next attempt to the 39 existing witness columns and their
linear combinations. First construct the missing 3- and 5-adic maps
and intersect their membership conditions with the saved real/11/2
coefficient kernel. Do not enumerate 2^39 coefficient vectors or claim
their formal kernel dimension is a global-class dimension. Reuse local
square-class/dimension saturation, with at most 200000 disk/divisor
tests per place, depth 64 and rational coefficient size 8192 bits;
failure to close within these caps leaves membership unresolved and
does not reject a class. Save complete evidence and print only actual
versus required bounds, failures and artifact paths.

If this supplies an eligible pair, select at most one pair and record
its coefficient masks, exact representatives and all-place membership
evidence. Attempt the three compatible covering models and one
K_eta rational-point search of projective multiplicative height at
most 100 and at most 200000 candidate tuples. Preserve any failure
before expanding effort. No independent
global basis, rational point on a torsor, Kummer point, or compatible
transport is assumed. No new source gate is needed for the general
published methods above, but an unlisted mathematical mechanism does
need one. Stop if construction cannot be certified with the available
exact machinery; do not turn this into a backend recovery attempt.

Only with those inputs ready, compute one Theorem 3.5 value and its
full omitted-place certificate, retaining the non-S6 normalization
cases. Continue toward the rank gap only if the authenticated value
or another informative obstruction justifies it. A nonzero value could
improve an upper bound but would still leave point control, integer
recovery and other exponent signatures open. No improvement is claimed
in this assessment. If no pair or Kummer point is reached within the
fixed test, record the precise obstruction and choose an independently
testable target rather than simply enlarge searches.

This is a known-method specialization, not an approved claim of new
mathematics. It does not justify labeling the next computation creative
merely because Cassels–Tate was not previously attempted here. Full
matching Mathlib coverage for the pairing and explicit algorithm is
not checked; no availability or absence claim is made.

## Target-statement source check

On 2026-10-28 the nominated AMS endpoint again returned HTTP 403.
[Mauldin's accessible primary statement](https://sites.math.unt.edu/~mauldin/beal.html)
was read and again gives positive integer bases and exponents, all
exponents greater than two, and a prime common to the three bases.
It matches GOAL.md, including unit bases and absence of a height bound.
No assertion about the inaccessible current AMS page or prize rules is
made. This leaves the recorded mathematical target unchanged.
