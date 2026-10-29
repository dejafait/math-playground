# Zero-selected disk energy: completed source comparison

TARGET: Review Jensen/Carleson estimates for a zero-selected energy saving Q_epsilon(T)=o(T(log T)^2) in L474 cells containing a pair with epsilon<d_j log T<=1.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact zero-selected/zero-conditioned energy, weighted second moments near off-line zeros, Bergman/Carleson sampling and near-line density searches found no inspected matching theorem; narrow local searches reused L471's loss, L474 and the prior discrete-moment comparison. Queries and primary passages are recorded below; this is not an exhaustive search or a novelty claim.
SOURCE_EVIDENCE: Tao, 246B Notes 1 (2020), Theorem 2 (3)--(6) and proof; Luecking (1983), Lemma 1 and Proposition 1, pp. 656--659, including the sufficient-embedding proof; Simonic arXiv:1910.08274v2 Theorem 1, pp. 1--2; reuse L474 Sections 1--4/6, L471 definitions/Section 4, L018 and L465 Sections 1--2. Primary Dirichlet-factor energy formulas remain unread leads, not imports.
COMPARISON: Jensen controls logarithmic zero data and Carleson gives bounded norm embeddings under geometric measure hypotheses, not an actual-Xi selected-energy little-o. The inspected density theorem counts zeros without amplitude weights at the same microscopic scale. L474 supplies only O(T(log T)^2); no checked source removes its leading scale on selected cells.
GAP: The correlation between actual off-line pair selection and squared disk energy is unproved. Neither shrinking selected energy, an applicable vanishing embedding nor a weighted zero-density estimate is available from the inspected statements; the target itself is not refuted.
REASON: Park the generic Jensen/Carleson-plus-continuous-moment implementation after this theorem-level mismatch. Preserve Q_epsilon as an open target and nominate a different finite-factor Dirichlet-energy mechanism for separate source review, without deriving an identity or approving mathematics this turn.
LITERATURE_REASON: The target changes from auditing a uniform small-displacement bound to exploiting the energy of cells selected by actual nonreal zeros; the existing assessment excludes complementary mass and supplies no weighted selection estimate.
SCOPE: Literature-only comparison for the fixed microscopic annulus epsilon<d_j log T<=1, with epsilon fixed in (0,1); no estimate for d_j log T>1, individual signs or RH is requested or assumed.

## Exact proposed quantity and relevance

Put L=log T and use L471's P_T, gamma_j, d_j and A, and L474's
half-open cells C_k and centers c_k. Let K_epsilon(T) be the set
of distinct cells containing gamma_j for at least one j in P_T
with epsilon<d_j L<=1. Define, without claiming a bound,

    Q_epsilon(T)=sum_(k in K_epsilon(T))
         [sup_(|z-c_k|<=8/L) |Xi(z)|/A(c_k)]^2.

Seek Q_epsilon(T)/(T L^2) -> 0 as T -> infinity for each fixed
0<epsilon<1; no uniform rate in epsilon is currently proposed.
The potential downstream use is an improved norm input for L474's
cell aggregation on this annulus. The sector d_j L>1, the full
L471 mass criterion and pointwise first/higher signs remain independent
gaps. Even a positive result here would not resolve RH.

The proposed mechanism uses zero-selection information in the local
norm itself, potentially through Jensen-type zero counts and weighted
analytic sampling. It does not repeat the already successful cubic
factor calculation or replace the quotient by -Z/q. No particular
Jensen/Carleson theorem is yet asserted to apply, and occupancy
sparsity is a missing assertion rather than an allowed assumption.

## Bounded source and continuation test

Search the exact selected-norm statement, weighted zero-conditioned
mean squares, stronger analytic sampling results and known obstacles.
Inspect primary hypotheses and relevant cases before proposing an
application. Reuse the already covered finite-factor, gamma and Bettin
tools; do not re-audit L474 or reopen the ordinary fourth-moment test.
Check local duplicates narrowly for this norm-selection mechanism.

Continue only if a source supplies the needed selection saving or the
comparison identifies a concrete, independently testable new constraint
on selected energy beyond the global O(T L^2) norm. A bounded future
test would distinguish that constraint from compatible concentrated
energy in occupied cells; any abstract model must state exactly which
actual-Xi constraints it retains. Neither a bare count of selected
cells nor a generic holomorphic countermodel settles the actual target.
If the comparison only reproduces the full-scale bound or requires
RH/unproved sparse occupancy, park that implementation and record the
specific missing input. No mathematical test is approved in this file.

Essential local inputs: L474, L471, L018 and L465. No cross-notebook
input. Full matching Mathlib coverage is unknown. A genuinely creative
attempt may be nominated after this missing source comparison, with
its obstruction and bounded test explicit; the present task is source
review, not a creative proof attempt by relabeling.

## Completed comparison, 28 October 2026

The proposal and its bounded test above are retained as the original
scope. This section records the completed review; no bound has been
derived and no lemma or mathematical script was changed.

### Jensen: exact hypotheses and mismatch

Read Terence Tao, *246B, Notes 1: Zeroes, poles, and factorisation of
meromorphic functions*, 23 December 2020,
[Theorem 2, (3)--(6), and its finite-factor proof](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/).
It assumes meromorphy near a closed disk and a center which is neither
a zero nor a pole; zeros and poles are counted with multiplicity.
The proof removes finitely many factors and applies harmonic mean
value, first avoiding boundary zeros by perturbing the radius.
For holomorphic functions (6) expresses a logarithmic boundary mean
as the central log modulus plus radial zero weights.

Xi is holomorphic, but its cell center may be a real zero. One must
remove that zero or change center before invoking this version.
More fundamentally, its conclusion is logarithmic, whereas Q_epsilon
uses squared suprema. No amplitude-weighted selection theorem occurs
in this passage. Converting a log mean to the required upper bound
on selected squared suprema is an additional, unproved step. This
is a statement comparison, not a counterexample to the Xi target.

### Carleson: bounded embeddings and missing smallness

Read Daniel Luecking, *A technique for characterizing Carleson measures
on Bergman spaces*, Proc. Amer. Math. Soc. 87 (1983), 656--660,
[author-uploaded primary text](https://www.researchgate.net/publication/243061671_A_technique_for_characterizing_Carleson_measures_on_Bergman_spaces),
DOI 10.1090/S0002-9939-1983-0687635-6. Lemma 1 uses measurable
neighborhoods, bounded overlap geometry, locally comparable weights,
a submean estimate and a local measure bound. Proposition 1 treats
weighted Bergman spaces on the unit ball, p>0, weight
(1-|z|)^beta with beta>-1: the box measure bound characterizes bounded
embedding. Inspected its sufficient-direction proof and Lemma 1's
Fubini argument, pp. 656--659; the converse invokes earlier work.
The AMS PDF returned 403, but the author-uploaded article was readable.

This theorem does not assert small embedding constants or identify
Xi-selected measures. Applying a fixed-disk theorem across moving
rectangles would require domain and uniformity checks. Moreover,
evaluations at the zeros themselves are zero and are not disk suprema.
L474's already proved submean/overlap argument is the applicable
bounded estimate. No vanishing measure condition is verified here.
Thus this source supplies no missing asymptotic factor.

### Unweighted near-line density does not cover the energy weight

Read Aleksander Simonic, *Explicit zero density estimate for the Riemann
zeta-function near the critical line*,
[arXiv:1910.08274v2, Theorem 1, printed pp. 1--2](https://arxiv.org/pdf/1910.08274v2#page=2).
For T>=H_0=3.0610046*10^10 and 1/2<=sigma<=0.831 it gives
N(sigma,2T)-N(sigma,T)<=a T^(1-(sigma-1/2)/4)log T
+b log^2 T+c log T log log T+d log T,
with a=10395.2, b=1.104, c=0.173, d=0.51; N uses beta>sigma.
Its introduction also records improvements of the constant exponent.
This is an unweighted count. Its exponent depends on the product
(sigma-1/2)log T, so a fixed microscopic displacement supplies no
vanishing factor in the stated leading bound. No substitution or new
zero-density estimate is proved here. Even a stronger count alone
would still need control of energy concentration in selected disks.
Dyadic clipping and cell endpoints would also need an application
argument; none is imported from this theorem into a lemma.

### Searches, reuse and decision

Queries included `Riemann zeta zeros weighted second moment near zeros
off critical line Carleson measure`, `Jensen Carleson embedding theorem
zeros analytic functions sampling Bergman measure`, `Selberg zero
density estimate sigma 1/2 log T N sigma T`, `zeta Carleson zeros`,
`zeta zeros weighted second moment unconditional`, and `zeta zero-selected
energy`, together with exact Luecking/Jensen source-title searches.
The prior zero-conditioned assessment and source notes already inspect
Kirila's RH-dependent positive discrete moments and the unconditional
reflected bilinear moment of Durkan--Hughes--Pearce-Crump. Reuse their
scope; neither matches Q_epsilon. Search results alone were not used
as theorem coverage. No novelty or universal impossibility follows.

Read the relevant canonical L474, L471 definitions/ordinary-moment
loss, L018 and L465 normalization ranges. Local searches for selected
energy, Jensen/Carleson and Dirichlet-factor energy found no matching
active result; the older Gaussian-response discriminant assessment
concerns arithmetic twists, not this zero-selected norm. Existing
cluster compensation and ordinary-moment/finite-law stops are retained.

The original continuation test is not met by an applicable saving.
Park direct bounded sampling plus Jensen/counting as an implementation,
without declaring Q_epsilon false or banning other uses of those tools.
A genuinely different lead is energy change under removing finite
inner factors, rather than bounding the supremum on each selected disk.
Carleson (1960), DOI 10.1007/BF01162477, and Richter--Sundberg (1991),
DOI 10.1307/mmj/1029004388, were located, but their primary formulas
and needed proof cases were not retrieved: Springer offered a paywall,
Project Euclid a service challenge, and GDZ exposed a catalog shell.
These are unread leads; no formula is credited from a survey or snippet.
The separate nomination states the exact new comparison and its stop
test. These first access failures are not a persistent blocker and do
not authorize repeated access-only turns. No Mathlib matching theorem
was checked, and no cross-notebook input was used.
