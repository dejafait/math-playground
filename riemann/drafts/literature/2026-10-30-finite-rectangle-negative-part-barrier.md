# Nomination: finite-rectangle negative-part barrier

TARGET: Review a negative-part maximum-principle test on the upper half-plane with the H_a rectangle removed, targeting Q_a(f)<=C_R a M(f) with explicit outer-boundary costs.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for subharmonic half-plane growth, finite-obstacle harmonic measure and the exact bandlimited rectangle-positive class; inspected the primary statements and proof cases below. Reused the parent Runge/positive-Poisson assessments and clipped/two-height/slow-dilation stops. No matching uniform Q bound identified; no novelty claim.
SOURCE_EVIDENCE: Lefevre--Queffelec, A Primer, and Beyond, on Composition Operators on the Unit Disk, publisher excerpt, Proposition 1.7 and Theorems 1.8/1.11, printed pp. 4--8; Schmidt, Partial Differential Equations I, version 2026-01-15, Sections 2.4/2.6/2.10, printed pp. 22--23, 36--37, 62--67; ABR second edition, corrected 2020 PDF, Theorem 7.26 and proof, pp. 158--159.
COMPARISON: Finite-domain comparison and continuous Dirichlet data are covered. The inspected unbounded-domain principles require boundedness or a positive superharmonic growth dominator and a little-o condition, neither supplied by L504's exponential envelope. Positive half-plane representation retains a term at infinity and is not a representation of the negative part outside a rectangle.
GAP: No uniform real-axis kernel estimate or finite-obstacle escape-cost bound was found. A precise top-boundary envelope residual is nominated separately for a later calculation; its divergence or boundedness is not established here. The original Q inequality remains open.
REASON: Essential comparison/growth coverage was missing for the unchanged nominated review. This literature-only step resolves its theorem-scope questions and makes the escape issue independently testable without deriving or approving a new inequality.
SCOPE: Completed source comparison only. No new lemma, mathematical script, H_a construction, unrestricted detector bound, Xi transfer or creative proof attempt. The separate continuation assessment is newly written and requires next-turn source-scope approval.

## Exact proposed test, with unresolved assumptions

Use L504 definitions with fixed R>0 and T>exp(1). The proposed target is
an estimate uniform in T and f in H_a, using only its stated smooth
Fourier support, evenness, reality and continuum rectangle lower bound.
The needed eventual threshold is Q_a(f)<=C_R a M(f). H_a existence,
unrestricted costs and actual-Xi realization are not assumed settled.
No cross-notebook result is involved.

The prospective object is the negative part max(0,-Re f) in the upper
half-plane outside the positive rectangle [-a,a] times [b,B]. A future
argument would need a valid subharmonic comparison on finite truncations
with horizontal height H>B and vertical sides at +-X, X>a. It would
separately bound the bottom contribution by the real-axis weighted norm
and account for every remaining outer-boundary contribution before any
limit. The available absolute growth input is L504's (20) at ambient
bandwidth R, together with N<=A_R M. Whether these data are sufficient
is precisely the test, not a premise. No vanishing escape term, global
boundedness, extension of positivity to a strip, uniform Schwartz seminorm
or unproved interchange is allowed.

Retrieve primary theorem hypotheses and the relevant proof cases for
subharmonic comparison in a half-plane with a finite obstacle, especially
the Phragmen--Lindelof/growth conditions at infinity. Reuse the earlier
ABR positive-Poisson comparison rather than repeating broad duality or
qualitative Runge searches. Compare any candidate theorem with the
nonzero exponential-type growth and the moving finite geometry. The
bounded result sought from the review is either exact usable coverage
for one subsequent escape-cost test or a documented obstruction to this
specific majorant method. An unread theorem title is insufficient.

Downstream use: a successful positivity-sensitive Q bound could support
the detector cost route; a failure would rule out only this barrier test.
Neither settles actual-Xi signs or RH. Continue only with an explicitly
controlled real-axis kernel and outer-boundary cost, or a precise new
quantitative residual that a separate mathematical turn can test. If
coverage supplies only bounded harmonic functions, whole-strip positivity
or qualitative representation, park the mechanism on that evidence and
choose another target. Matching Mathlib coverage is unchecked.

At nomination this assessment was REVIEW_REQUIRED. The completed review
below supersedes that source status, without certifying a new subharmonic
or detector inequality. Quantitative positivity/cost control is still
missing for a genuinely new central construction.

## Completed source review, 2026-10-30

LITERATURE_REASON: The exact target changes the stopped linear residual
and slow-dilation questions to a negative-part comparison on a domain
with a finite obstacle; its essential growth-at-infinity hypotheses had
not been inspected. This is not repeat browsing of an already ready test.

The main gap remains actual-Xi all-degree positivity, especially initial
signs at unbounded heights. The intermediate target is the unchanged Q
bound above. A usable bound could inform detector costs; a rigorously
failed envelope comparison would eliminate only that certificate. No
H_a realization or arithmetic transfer is assumed. The continuation
test requires quantified boundary costs, rather than a qualitative
maximum principle.

### Searches, overlap and source access

Queries actually used included `site.axler.net Harmonic Function Theory
Phragmen Lindelof half space subharmonic growth`, `subharmonic half plane
Phragmen Lindelof harmonic measure exponential growth obstacle maximum
principle`, `subharmonic Phragmen Lindelof half plane u(z) o(|z|) theorem
notes pdf`, `rectangle harmonic measure Dirichlet problem exterior cone
condition Perron lecture notes pdf`, `"entire" "positive real part"
"rectangle" "exponential type"`, `"bandlimited" "subharmonic" "harmonic
measure"`, `"harmonic measure" "compact obstacle" "half-plane" infinity`,
and `"subharmonic" "finite obstacle" maximum principle`.

Read L504's hypotheses, (1)--(10), complete supplementary proof (19)--(20)
and separate audit; parent Runge and positive-class assessment passages;
clipped, two-height and slow-dilation failure records; and the latest
slow-dilation history. The existing ABR 6.13(a)/6.15 comparison is reused,
not presented as new coverage. These records contain no finite-domain
top-boundary envelope calculation. They do not exclude the H_a bound.
No sibling notebook or cross-notebook input was read.

The Jaming CoursHA2022 PDF and IISc half-plane notes were leads only:
individual theorem/proof retrieval timed out or was restricted. No
hypothesis or conclusion is imported from them. Schmidt supplies the
needed general-domain growth comparison and finite Dirichlet theory,
so these access failures are not essential source blockers. Search
snippets, secondary pages and unread cone/growth papers are not evidence
for the desired estimate. No originality is inferred from this search.

### Inspected statements and relevant proof cases

1. P. Lefevre and H. Queffelec, *A Primer, and Beyond, on Composition
   Operators on the Unit Disk*, publisher excerpt ISBN 9781009388894,
   [Section 1.2, pp. 4--8](https://assets.cambridge.org/97810093/88894/excerpt/9781009388894_excerpt.pdf).
   Proposition 1.7(ii) preserves subharmonicity under the maximum of two
   subharmonic functions. Theorem 1.8 requires bounded open Omega,
   subharmonic v bounded above, and limsup v<=m at every boundary point;
   then v<=m. Theorem 1.11 permits any proper open subset of C, retaining
   boundedness above and the boundary limsup hypothesis. Read both proofs:
   the bounded case uses a maximizing sequence and the mean inequality;
   the unbounded case subtracts a small logarithmic barrier and uses a
   finite global supremum to choose the outer radius. There is no
   exponential-growth exception in this statement. The finite-domain
   theorem permits holes; the negative part need not be C^2.

2. T. Schmidt, *Partial Differential Equations I*, winter terms 2018/19
   and 2025/26, [version 15 January 2026](https://www.math.uni-hamburg.de/home/schmidt/lectures/PDE.pdf).
   Section 2.4, pp. 22--23, gives comparison on bounded domains and a
   growth variant: a positive superharmonic v tending to infinity at
   the exceptional point allows u^+/v->0 there, with the other boundary
   limsups controlled. The proof applies comparison to u-epsilon v.
   Section 2.6, pp. 36--37, bounds max_K h by C(K,Omega) min_K h for
   nonnegative harmonic h, compact nonempty K in connected Omega; read
   the ball estimate and finite-chain proof. Section 2.10's main theorem,
   p. 66, solves continuous Dirichlet data uniquely on bounded domains
   whose boundary points are regular. Read the Perron replacement proof,
   pp. 63--64, boundary-barrier argument, pp. 64--66, and Remark (2),
   p. 67: exterior cones suffice. The cone extension is stated with a
   proof outline, not fully proved there. No uniform moving-domain
   constant or rate of escape is asserted.

3. S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*, second
   edition, Springer 2001, [corrected PDF dated 17 July 2020](https://www.axler.net/HFT.pdf),
   Theorem 7.26, pp. 158--159. A positive harmonic function on the whole
   upper half-space has representation `P_H(mu)(x,y)+c y`, with mu a
   positive Borel measure and c>=0. Read the proof separating the
   transformed boundary measure's atom at the distinguished point from
   the remaining measure; this atom produces c y. This does not supply
   a negative-part majorant or a finite-obstacle representation. It
   explicitly retains information at infinity. The earlier ball-Poisson
   comparison remains subject to its original domain restriction.

### Applicability and bounded decision

Use the closed obstacle O=[-a,a] times [b,B], with T>exp(1), B>b>0.
L504's smooth Fourier representation makes Re f harmonic and continuous.
The source maximum-of-subharmonics property covers the proposed
negative part; continuity of H_a's stated lower bound covers the
obstacle boundary. These are applicability checks, not a derived Q
estimate. Bounded rectangular truncations have polygonal boundaries,
with an exterior cone even at each obstacle corner; continuous boundary
data therefore lie within the stated Dirichlet theory. Piecewise
constant top data at the outer corners should instead be replaced by
continuous tapers. A C^2-only maximum principle cannot be applied to
the negative part without its generalized version.

L504 (20), at ambient bandwidth R, supplies the positive exponential
envelope 2R A_R exp(2pi R y) M(f). It does not supply boundedness on the
whole exterior domain, a superharmonic dominator with the required
little-o quotient, or a uniform Schwartz seminorm as the domain moves.
Consequently the inspected unbounded theorems cannot simply remove the
outer boundary. This is a missing-hypothesis comparison, not proof that
an admissible f attains its envelope. A logarithmic modulus estimate
would concern a different quantity from the linear negative part.

No source inspected gives the required bottom kernel bound against K,
whose zero at 0 cannot be handled by pointwise division. The audited
N<=A_R M remains available for a genuine real-axis L-infinity kernel
bound. All side and top contributions must still be included. In
particular, a function-specific fixed-height Schwartz limit does not
by itself yield uniformity over H_a and T.

Decision: park direct deletion of the outer boundary. Nominate exactly
one finite-domain envelope-cost test in
`drafts/literature/2026-10-30-finite-obstacle-top-escape-test.md`.
It has enough standard inputs for a separate scope approval and later
calculation, but no outcome is claimed now. Continue that test only if
it yields an actual bound or an informative obstruction to this
envelope-based majorant; otherwise stop this certificate and reassess.
The original H_a inequality, bottom kernel, actual-Xi realization and
all-height signs remain unresolved. Full matching Mathlib coverage was
not checked; the search hit for complex Phragmen--Lindelof is only a
lead and does not establish this subharmonic obstacle estimate.
