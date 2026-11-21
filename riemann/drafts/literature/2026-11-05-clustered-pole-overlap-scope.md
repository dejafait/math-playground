# Clustered-pole conditioning and effective overlap — source assessment

TARGET: Assess whether a clustered-pole contour estimate for L834 can avoid inverse individual zero-gap losses and certify an effective onset overlapping the verified-height PF range at fixed k=6002.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step671 searched exact reciprocal-Xi/6002 conditioning, clustered-pole divided differences, inverse-Vandermonde residue cancellation and meromorphic Toeplitz error bounds; checked the named local fixed-shift, hybrid and interpolation assessments. Primary de Boor statements and proofs were inspected; no actual-Xi overlap bound was found in the inspected sources. Queries and access qualifications below; no novelty inference.
SOURCE_EVIDENCE: Carl de Boor, Divided Differences, Surveys in Approximation Theory 1 (2005), 46–69, Proposition25/(24)–(26) pp.53–54, Proposition35/Definition37 pp.58–59, Example9/(41)–(42) p.60, and (49)–(52) with their derivations pp.62–64, https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf and https://arxiv.org/pdf/math/0502036v1 ; Beck et al. Section8.1 Theorem8.1.5/full proof https://complexanalysis.org/web/sec_residue-thm.html ; Michałowski 2607.16795v1 Section1.2 https://arxiv.org/html/2607.16795v1#S1.SS2 ; reuse L834/L832's qualified primary inputs as detailed below.
COMPARISON: Known interpolation formulas retain analytic coupling and include confluent nodes; they do not bound the actual Q_r^(-1)E_r. De Boor's sampled-data norm (42) retains reciprocal node-polynomial derivatives. The inspected sector source states m+1<=pi H, so PF6001 is conservative; it supplies neither strictness nor an effective pole-ray onset. No complete overlap is imported.
GAP: The unpaid specialization is an exact relative-matrix representation and explicit bound retaining P, F/P, all contour constants and r-dependence; then actual bounds must make the relative threshold below1 at a rank overlapping a separately justified finite-PF cutoff. No such representation, numerical constant, onset or overlap is proved in this review.
REASON: Adequate standard coverage supports one bounded Newton-Hermite cancellation test on the actual analytic remainder, rather than a second fixed-k existence proof or arbitrary nodewise-error estimate. Its success remains open; replacing C by another unknown finite constant fails. Newly ready continuation requires separate next-turn approval.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target newly requires clustered-residue conditioning and quantitative overlap coverage. Existing duality, coefficient expansion, finite-height and sector assessments are reused; only the missing interpolation interface and the source's explicit cutoff statement were inspected.
SCOPE: Completed literature-only step671; no derivation, lemma, mathematical script, computed onset or expanded local PF theorem. SPECIALIZE covers only the bounded test below, not an asserted cancellation or all-rank sign theorem. A basis change alone is not a creative central mechanism.
COVERED_TARGET: Test whether Newton-Hermite coordinates remove inverse individual pole-gap factors from L834's relative error bound at fixed k=6002, retaining explicit contour constants and r-dependence and stating the overlap test against m+1<=pi H.

## Original step670 nomination — retained scope

Essential inputs are L834 and L018/L021/L776/L832 under their actual-Xi
hypotheses. Fix k=6002; retain L834's F, p_j, R, Q_r and E_r. The main gap
is still all-degree mixed positivity. The intermediate purpose is an
effective connection between an unbounded-rank ray and an independently
verified finite-order region. That would close a gap on this ray only;
growing shifts, other minors and RH would remain open.

The proposed mechanism is to keep the finite pole polynomial
P(z)=prod_(j=1)^k(1-z/p_j) and the analytic factor F(z)/P(z) together
inside a contour or divided-difference representation, instead of taking
separate absolute bounds for both inverse Vandermonde matrices. This is
a proposal, not a derived cancellation identity or an estimate. Distinct
verified poles may be grouped for the estimate, but multiplicities may
not be silently changed. No positive sign for the residual is assumed.

Review quantitative interpolation/divided-difference bounds, clustered
residue expansions and their Toeplitz determinant applications. Retrieve
the exact hypotheses and relevant proof cases before judging coverage;
distinguish generic identities from bounds on this actual F. Check exact
statement overlap and known obstructions. The previously indexed
fifteen-shift exposition is a lead only; its uninspected certificates are
not required inputs. Do not repeat a persistent access loop.

Continuation test: identify a precisely stated, independently payable
bound for the relative matrix error, or a similarity transform of it,
whose quantitative inputs could yield a threshold below1 for every
r>=r_* with r_* no larger than a separately justified finite-PF cutoff
plus1. A cutoff stronger than the stated PF6001 must first be justified
from its source hypotheses; neither maximality nor strict finite signs
are assumed. All contour suprema, residual values and other constants
must remain explicit obligations. Merely replacing C by another unknown
finite constant, assuming an unproved gap lower bound, or rediscovering
the unpaid hybrid ratio fails the test and parks this overlap mechanism.

No estimate has been derived in step670. If the review finds a concrete
new cancellation mechanism and adequate coverage, it may nominate a
separately approved bounded proof attempt with the correct purpose
routing. A creative label is not warranted by a basis change alone.
At present the missing quantitative theorem and actual-Xi bounds block
such a nomination. Full matching Mathlib coverage is unchecked.
No cross-notebook theorem is used.

## Completed source comparison — step671, 5 November 2026

The main gap remains actual-Xi all-degree mixed positivity. The single
reviewed intermediate purpose is to make the fixed-k=6002 pole-ray
estimate quantitatively comparable with a finite-PF range. This could
close the rank gap on this one ray; growing shifts and all other unpaid
minors would remain independent. This review supplies source coverage
for a test, not a mathematical advance beyond those sources.

### Primary coverage and its limits

Carl de Boor, *Divided Differences*, Surveys in Approximation Theory
**1** (2005), 46–69, author article dated 21 December 2004,
[author PDF](https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf),
[arXiv:math/0502036v1](https://arxiv.org/pdf/math/0502036v1), supplies
the following precisely limited tools. The author copy notes a June2005
correction to Corollary30; that corollary is not used here. Reuse the
prior polynomial/function-data assessment in
`2026-11-04-exact-projection-similarity-review.md`; the contour and
sampled-data norm passages were newly inspected for this target.

Section4, (24)–(26), Proposition25 and its full proof, pp.53–54,
represent multiplication modulo the node polynomial in the Newton
basis. The node matrix is lower bidiagonal with the nodes on its
diagonal and ones below it; polynomial functions of it contain the
corresponding divided differences. The proof first uses distinct
nodes, then Proposition21 continuity permits repeated nodes. This is
polynomial algebra: an arbitrary holomorphic matrix-functional-calculus
estimate must not be silently ascribed to Proposition25.

Section7, Proposition35 and its proof, Definition37 and Example8,
pp.58–59, extend divided differences to functions with the Hermite
derivative data required by node multiplicities. In particular the
nonzero-node restriction in (38), and the exclusion of nodes in (39),
must be respected for reciprocal functions. These inputs permit finite
Hermite interpolation of analytic factors; they do not already identify
L834's error matrix with a multiplication matrix.

Example9, (41)–(42), p.60, gives the distinct-node residue expression
and the norm of the divided-difference functional on continuous
sampled data. That norm is the sum of the absolute reciprocals of
the node-polynomial derivatives. Thus the source does not supply
the desired gap-free control from independent bounded node values.
Any proposed improvement must use the actual analytic coupling of
the values, not regard them as arbitrary independent perturbations.
This distinction was absent from the original scope, and is material
to the continuation's error model. No new impossibility theorem is
derived from it here.

Section9, (49)–(51) and the complete Cauchy-formula derivation,
pp.62–63 (PDF pp.17–18), give the Newton interpolation formula with
its contour remainder and divided-difference contour coefficients.
The stated setup has f holomorphic in a disk and the contour in that
disk enclosing the relevant interpolation sites and evaluation point;
the sites must not lie on the contour or in the stated intervening
annulus. The formula uses the whole node polynomial on the contour,
instead of separate simple-node residues. It is an exact identity,
not a quantitative bound for this Xi or a relative determinant estimate.
The Genocchi-Hermite formula (52), p.64 (PDF p.19), and its induction
from the two-node integral were also read. It uses derivatives on the
node simplex; its usefulness requires control of those derivatives.
Neither continuity at confluence nor this representation provides a
small constant, especially at order6002. No general interpolation
theorem needs reproof in the proposed application.

For any contour rearrangement, reuse and reconfirm Matthias Beck,
Gerald Marchesi, Dennis Pixton and Lucas Sabalka, *A First Course in
Complex Analysis*, online Section8.1,
[Theorem8.1.5 and full proof](https://complexanalysis.org/web/sec_residue-thm.html).
The theorem assumes a simple positively oriented closed contour in a
simply connected domain, analyticity on it and in its interior except
for finitely many isolated singularities. The proof removes disjoint
small circles and retains every residue. It justifies tracking all
singularities, not dropping the origin when negative powers appear.
A disk version of de Boor's formula cannot be applied to a function
with an unremoved pole at zero inside that disk. A future application
must choose an admissible disk/contour or explicitly account for
every extra residue and boundary component. No such representation
has been derived this turn.

Wojciech Michałowski, *An explicit uniform cubic wedge for consecutive
Toeplitz minors of the Riemann xi-coefficients*, 18 July2026,
[arXiv:2607.16795v1, Section1.2](https://arxiv.org/html/2607.16795v1#S1.SS2),
explicitly states the sector consequence for m+1<=pi H and the
conservative displayed rank cutoff floor(pi H)-1. The complete
short sector paragraph, including its zero-image formula, strict
angular bound and verified-height restriction, was read. This is
coverage for a later applicability argument, not a new local PF
theorem. Retain the genus-zero product, positive constant, real
finite products, compact-limit argument and polynomial-sector
hypotheses precisely recorded in L832. Its Platt–Trudgian height
and Katkova TheoremB reading remain adequate; the original Schoenberg
proof remains unread as qualified there. The sector conclusion is
nonnegative, not strict, and the source's unrelated cubic-wedge theorem
and certificates are not imported. Any chosen integer cutoff beyond
6001 must first be justified under those exact hypotheses. In
particular source coverage for a larger cutoff is not proof that
L834's eventual ray reaches it.

Reuse L834's audited actual simple-pole packet, real signed determinant,
finite reciprocal-minor duality and meromorphic coefficient expansion.
Primary inputs remain Platt–Trudgian 2004.09765v1 Theorem1/Section2,
Böttcher–Widom math/0604009v1 Theorem2.1/Corollary2.3, and
Flajolet–Sedgewick2003 TheoremIV.7/(22), with the precise versions,
proof cases and links in `2026-11-05-fixed-shift-reciprocal-pole-test.md`.
No rereading or reproof of their unchanged coverage is required.

### Searches, overlap and source blockers

Queries used: `Carl de Boor Divided differences 2005 contour integral
bound analytic clustered nodes`; `Toeplitz determinant meromorphic
generating function clustered poles relative error zeros divided
differences`; `"clustered" "poles" "divided differences" error bound
contour`; `"inverse Vandermonde" "residues" Toeplitz determinant`;
`"reciprocal" "xi" "6002" "poles"`; `"Toeplitz determinants"
"meromorphic" quantitative error bound poles`; `"divided differences"
"clustered poles" contour error estimates`; and `"Riemann"
"reciprocal" "Toeplitz" "pole" conditioning`. These searches do
not establish novelty or a global absence result.

Read L834's actual-pole, principal-part, factorization, error and audit
passages and L832's hypotheses, sector and finite-product passage.
Compared step659's preserved unpaid determinant ratio, step667's
fixed-winding versus fixed-shift comparison, and the existing de Boor
projection-weighting review. The latter checks a different fixed pair
and supplies no 6002-dimensional estimate. The earlier small-cluster
Pick assessment concerns inverse-Blaschke detectors, not this relative
matrix; its target is not reopened. These are local comparisons only.

Bultheel's 1985 meromorphic-Toeplitz article reappeared in search, but
step667 records repeated access/proof-reading failures. Its essential
formulas remain uninspected; no download or screenshot loop was
repeated. The fifteen-shift exposition likewise remains overlap
evidence only, with its uninspected certificate packet excluded.
Neither source is essential to the bounded interpolation test below.
New search-only leads on mixed-characteristic-function residue
inversion and merging Fisher–Hartwig singularities are not imported:
no theorem/proof comparison with the actual entire F was completed.
No claimed RH resolution found in search is treated as theorem evidence.

### Separate bounded mathematical continuation

SPECIALIZE covers the single COVERED_TARGET above after separate
approval. Fix the actual F, p_j, R, Q_r and E_r of L834 and k=6002.
Use P(z)=prod(1-z/p_j) and the actual quotient F/P, retaining its
removable values. Seek an exact Newton/Hermite representation of
the relative error or a genuine similarity transform of it, before
taking absolute values. Track basis orientation and invertibility,
the signed residues, all factors of P and F/P, negative powers,
contour geometry and every r-dependent term. Scaling must not
introduce unrecorded inverse node-gap factors. Repeated-node source
coverage is a device for estimates; actual multiplicities remain those
proved in L834. This paragraph proposes a test, not an identity.

Success for that intermediate test means an explicit bound for the
specified matrix norm using named contour/analytic data, without
inverse individual pole gaps; it must state the remaining numerical
obligations and the inequality needed for overlap. Ultimately the
bound must be <1 for every r>=r_* and a separately justified finite-PF
cutoff must cover through r_*-1. A crude transformed bound may fail
without the matrix being singular or its determinant being negative.
Another unnamed finite C, the old hybrid ratio or mere coefficientwise
smallness fails the test and parks this proposed cancellation route
pending materially new input. Do not repeat fixed-k existence,
neighboring shifts or an unbounded precision/radius search.

Actual contour suprema and lower bounds for F/P, effective separation
of the packet from its complement, the explicit relative threshold
and the cutoff specialization remain unproved. Internal individual-gap
loss and packet-to-complement separation are different obligations;
the former's removal would not pay the latter. Other mixed signs,
growing shifts and RH remain open even if overlap on this ray succeeds.
This is difficult development of a standard interpolation route, not
an approved creative central mechanism. The missing actual quantitative
bound is the blocker to claiming more. No lemma or mathematical script
was written; PROOF/DAG remain unchanged. Mathlib full matching coverage
is unchecked, with no assertion of absence. No cross-notebook input.
