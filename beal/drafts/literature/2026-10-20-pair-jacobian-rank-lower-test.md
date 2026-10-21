# Pair Jacobian — independent rank-threshold test

TARGET: Test whether rational divisor classes on L110's Jacobian certify Mordell–Weil rank at least two.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-sextic/Putz and rank-backend comparisons; searched Stoll/Schaefer Kummer independence, torsion and Magma rank-lower-bound terminology and exact coefficient variants; inspected primary passages and relevant local pair assessments/failure records without finding an exact-instance rank certificate.
SOURCE_EVIDENCE: Read Stoll (2001), equation (1.1), Section 4 and Lemmas 4.1/4.3; Müller author-hosted notes, Lemmas 1.17–1.18 and Section 2.4 through Proposition 2.7; Stoll (2025), Section 2; Magma named search/height/torsion/rank interfaces; Conrad Hensel Theorem 2.1 and its uniqueness proof; Lynn's Euler-criterion proof, all accessed 2026-10-20.
COMPARISON: Known Kummer maps and the Mordell–Weil quotient formula provide a torsion-aware rank-lower certificate without complete Selmer/class/unit arithmetic; no source inspected supplies the required classes, local detector matrix or this Jacobian's rank.
GAP: In a separate research turn verify an odd-degree model, obtain exact rational curve points or quadratic Mumford divisors, certify a two-torsion allowance and a localized Kummer-image dimension exceeding that allowance by at least two; search failure gives no upper bound.
REASON: Essential coverage now supports this unchanged target using bounded exact polynomial/rational/modular arithmetic; import the general theorems and test the instance without re-proving them or reopening the parked complete-descent backend.
LITERATURE_REASON: The saved lower-bound target was REVIEW_REQUIRED and explicitly outside the previous upper-bound assessment; torsion, divisor evaluation and an executable certificate required this separate comparison.
SCOPE: Only the unchanged rank-at-least-two diagnostic using the bounded point/divisor and localized Kummer test below; no complete rank, full independence classification, saturation, Chabauty run, height algorithm or rational-point completeness is approved.

## Relevance and existing inputs

Inputs: audited L109 and L110, L110's exact sextic and its original s,z
maps; the completed upper-bound review is
`drafts/literature/2026-10-20-pair-jacobian-rank-bound.md`.
No new curve model, rational point list or divisor class is assumed.

The main gap is positive primitive integer exclusion in residual Beal
signatures. Here the intermediate target is rank at least two on the
necessary pair image in ordered (3,5,11). It would obstruct the usual
strict rank-versus-genus Chabauty threshold, not prove point emptiness.
Global rational-point classification, marked lifting, degree-nine root
recovery, remaining factors, both L095 integer systems and minus-eleven
would remain unresolved. L110's independent audit is complete; its
overview's older pending-audit wording is not a new mathematical gap.

## Imported certificate inputs

[Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Acta Arith. 98 (2001), 245–277, DOI 10.4064/aa98-3-4:
Section 4, pp.249–251, assumes squarefree monic integral odd-degree f.
Lemma 4.1 makes the norm-square Kummer map natural and injective on
J(K)/2J(K); Lemma 4.3(1) evaluates a nonbranch point as x(P)−theta.
Lemma 4.3(3) gives dim J(K)[2]=m_K−1 for the number of irreducible factors.
Its proof refers to Schaefer; that theorem is imported, not re-proved.
The Mordell–Weil quotient identity behind equation (1.1), p.245, is
dim J(Q)/2J(Q)=rank J(Q)+dim J(Q)[2]. Consequently a detected image
dimension d and certified upper allowance t for dim J(Q)[2] give the
sufficient lower bound d−t. The threshold is d−t>=2, not d>=2.
All rational even-order torsion is covered by this allowance, including
order-four classes; odd torsion contributes zero to this quotient.
Neither a Selmer upper bound nor assumed Sha parity is used.
L110 has rational Weierstrass points (2,0),(−2,0), so the source's
odd-degree interface is available after a verified Q-change of model.
No such transformation or factor count is computed here.

[Jan Steffen Müller, Rational points on Jacobians of hyperelliptic curves](https://uol.de/f/5/inst/mathe/personen/steffen.mueller/ohrid_proceedings.pdf),
author-hosted 32-page notes, Lemmas 1.17–1.18, PDF pp.5 and Section 2.4,
PDF pp.9–11: odd-degree Mumford coordinates use a monic polynomial a,
deg b<deg a, and a dividing f−b². They represent D−deg(a) infinity,
and reduced representatives have deg a<=g. For support disjoint from
the branch divisor the Kummer value is (−1)^deg(a) a(theta).
Proposition 2.7 has kernel 2J(k); Remark 2.8 warns that even-degree
models can have a larger kernel. Thus do not apply the odd-degree
formula directly to L110's sextic. The inspected proof/formulas retain
non-rational conjugate points via rational divisors; searching only
individual curve points would miss these classes. Restrict this bounded
test to squarefree a with gcd(a,f)=1; exceptional branch evaluations
are unnecessary for these candidates. Quadratic divisors need not split
over Q, and splitting is not a validity condition.

[Keith Conrad, Hensel's lemma](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf),
Theorem 2.1, PDF pp.1–3, gives a unique Z_p root above a simple root of
an integral polynomial modulo p; the proof verifies every successive
lift and uniqueness. For an odd prime and unit evaluation, residue square
characters are legitimate local detectors. The selected coordinates
use only simple linear residue roots, so no extension-field backend is
needed. A zero evaluation must be omitted, never labeled a nonsquare.
[Ben Lynn, Number Theory — Quadratic Residues](https://crypto.stanford.edu/pbc/notes/numbertheory/qr.html)
proves Euler's criterion: nonzero residues have square character given
by exponent (p−1)/2. This is exact finite arithmetic.

[Stoll, Determining the rational points on a curve of genus 2 and
Mordell–Weil rank 1](https://mathe2.uni-bayreuth.de/stoll/papers/rank1.pdf),
author manuscript dated September 29, 2025, Section 2, PDF pp.3–4,
distinguishes point-search lower bounds, Selmer upper bounds and
saturation. It explains the missing-generator and class-group issues.
Only this background comparison is used; its later conditional
termination assertions are not premises of the lower-bound test.

## Height alternative and implementation limits

[Magma Handbook, Jacobians over Number Fields or Q](https://docs.magma-maths.org/ArithmeticGeometry/HyperellipticCurves/jacobians-number-fields.html),
entries Points/RationalPoints, TwoTorsionSubgroup, TorsionBound,
HeightPairingMatrix, Regulator, ReducedBasis and RankBounds, documents
both Jacobian search and independence via heights or J(Q)/2J(Q).
Its regulator is zero for dependent free classes. However a positive
printed decimal determinant does not provide explicit certified error
intervals here. Height-based execution is therefore not selected.
TorsionBound's finite reductions are upper bounds, not evidence that
a searched point has infinite order. These interfaces were inspected,
but no Magma run is claimed. The earlier local-backend absence and
unestablished public-calculator submission route are reused unchanged.

## One bounded executable test, reserved for research

The following is a future certificate specification, not a calculation
or instance-specific theorem proved in this review. Standard-library
Python integers, fractions, isqrt, polynomial division/gcd, modular
exponentiation and F2 row reduction suffice; no new backend is required.

1. Verify an inverse Q-change from the sextic using (2,0) to a monic
   integral odd-degree genus-two model g. Keep both models and all scaling
   constants. This is a computational interface change only; retain
   L110's original s,z and import L109/L110 rather than altering them.
2. Search the original curve at reduced T=m/n with n>0 and
   max(|m|,n)<=500, checking the homogeneous sextic for an exact integer
   square. Also enumerate monic quadratic a=T²+a1*T+a0 with integer
   |a0|,|a1|<=25 and b=b1*T+b0 with integer |b1|<=500; determine b0
   from the coefficient equations for a dividing f−b², including the
   b1=0 case. This finite divisor box imposes no bound on b0 beyond those
   equations. Keep only squarefree a prime to f, verify exact divisibility,
   and use D−2(2,0). These two parts form one bounded generator search.
   Transport each candidate to the odd model and reverify its coordinates.
   For this detector retain only columns whose odd-model Mumford
   polynomial is prime to g; discard branch-supported columns rather
   than applying an exceptional formula without its separate verification.
3. Use only odd primes p<=101 with degree preserved and squarefree g
   modulo p. Complete finite-field factorization bounds the rational
   factor count from above (Gauss's lemma); use Lemma 4.3(3) to obtain
   an explicit two-torsion upper allowance t. If this bound is coarse,
   retain it honestly. No irreducibility or exact torsion dimension for
   this instance is presumed. No full rational torsion computation is
   required. A tighter t is useful but is not silently assumed.
4. At simple linear residue roots of g, evaluate the signed Mumford
   polynomial and its nonzero square character. Select one common set
   of coordinates valid for every retained column, excluding denominator
   primes and zero evaluations. Concatenate characters across primes,
   form the exact F2 matrix and certify rank d by pivots and a nonzero
   minor or complete row reduction. All columns must come from the same
   fixed rational classes. This is a projection of localized Kummer
   images; no assertion of exhaustive local images is needed. Its
   dimension is a lower detector only. Do not fill undefined entries
   with zero bits or choose inconsistent per-column coordinates.
5. Print actual d,t,d−t and required d−t>=2, every rejected or failed
   check, search bounds/completion and artifact paths. Save full model
   maps, candidate divisors, exact remainders, finite factorizations and
   irreducibility checks, root/square-character tables and row operations
   under scripts/pair-genus-two/ for complete replay. A certified lower
   bound does not on its own identify two particular independent free
   generators; do not claim that stronger output without its evidence.

Continue this mechanism only if d−t>=2, or if the bounded attempt finds
a specific new class/detector defect with a discriminating correction.
If the search/detector cap ends below threshold, record the actual
certificate and park this bounded test; this proves neither rank<2 nor
dependence of the candidates. Do not repeat the same box or merely
increase its cap without a materially new reason. Preserve the parked
upper-bound computation and the unused rigorously bounded-height option.

## Search scope, duplicates and qualifications

Queries included `genus 2 Jacobian rational points independence modulo 2
torsion Stoll Kummer rank lower bound`, `Magma handbook genus 2 Jacobian
independent points height pairing IsLinearlyIndependent RankBounds`,
and exact variants `"275T" "704T" curve Jacobian`,
`"1034" "3388" "2288" hyperelliptic`, `"11(T" "52T" "Jacobian"`.
No adequate exact-instance theorem appeared in the inspected results;
unrelated hits are not mathematical evidence and failed searches do not
prove novelty. The earlier Putz-file/sextic comparison is reused rather
than repeated. Schaefer's original 1995 paper was an abstract-level lead;
the imports above rely on the inspected numbered Stoll/Müller statements.
Other twist-independence and canonical-height papers surfaced as leads
but were not read or used to approve a height algorithm.

Local comparison used the two pair-rank assessments, L110's statement,
drafts/2026-10-20-explicit-pair-model-critical-audit.md,
history/381 and the relevant ATTEMPTS/032 and 045 search passages.
The old elliptic/unit obstruction concerns another Jacobian/base field;
its dimensions cannot become a lower bound here. The class backend stop
does not obstruct these finite detector computations. No cross-notebook
input is used. L108's unfinished reasoning is preserved. Mathlib coverage
of the full lower-certificate workflow was not checked; no absence is
asserted. This turn supplies coverage and an executable specification,
not a new lemma, rational class, rank value or advance beyond the sources.
