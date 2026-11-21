# Two-site theta coefficient control — completed review1920

TARGET: Review coverage for independent cubic and quartic coefficient control at fixed degree d>=4 in nu_(a,b)=(mu_0+delta_a+delta_b)/3, a<b, after affine normalization, with a first local test at d=4 and (a,b)=(0,1).
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact/rank/range and stronger moving-site searches; compared C028q/r/s and grid413, Fourier435, quartic-field98 and scalar-only1919. Queries, inspected sources and unread leads are in drafts/literature/2026-11-20-two-site-theta-source-notes-1920.md. No matching standardized-zero-moment rank theorem was found; no novelty claim.
SOURCE_EVIDENCE: Reuse1908's arbitrary-site Uvarov Theorem3.1/proof and DLMF mixed-zero reads. Newly read Gautschi2004 Section2.1.1 Theorem2.1,(2.1.1)-(2.1.3),pp52-54,statement/full proof; Castillo--Rafaeli ETNA44(2015),Theorem2.2 and exterior proof cases; Dimitrov arXiv:1501.07235v1,Theorem2/Corollary3/full proof; Castillo--Costa--Rafaeli preprint17-43,Corollary3.5/proof and Section4.2. Primary links and exact scopes are in source-notes1920.
COMPARISON: Known arbitrary-site modification and moment-determinant formulas cover coefficient construction, not empirical cubic/quartic rank or actual-target inclusion. Exterior-site monotonicity does not apply on support R; the apparent unrestricted2015 claim has a documented later source objection and is not imported. Earlier stops concern different objects.
GAP: The identified specialization is one fixed d=4 Jacobian certificate at sites(0,1). Mixed moments0,...,7 require only even base orders0,2,4,6, covered by L917 at lambda=0 under L037. Rank, image inclusion, actual matching, higher degrees and full cost remain unproved. Full matching Mathlib coverage unchecked.
REASON: The changed two-observable target now has source coverage for a bounded finite calculation; the monotonicity shortcut is excluded. No new lemma or Jacobian is derived here. The exact calculation is nominated in review1920 for separate next-turn approval.
SCOPE: Full theta probability, two distinct real sites with fixed positive unit masses, monic orthogonal polynomials and equally weighted centered zero moments. Only the d=4,(0,1) local test is nominated; no general rank/range claim or sweep.

Completion1920: full source comparison and input qualifications are in
[source-notes1920](2026-11-20-two-site-theta-source-notes-1920.md).
No mathematical result is asserted by this review. The next calculation
is specified in review1920 and needs separate approval. The original
prospective reasoning below is preserved as history, not active scope.

## Preserved nomination1919

The main gap is actual-Xi all-degree positivity, with C028b's equivalent
H_d=o(d) unpaid. Here mu_0 is exactly C028q's full even theta probability;
q_d is the monic orthogonal polynomial of the stated positive mixed
measure. The proposed invariants are centered equally weighted zero
moments M_3/M_2^(3/2) and M_4/M_2^2, not moments of the measure or
Gauss-weighted moments. Affine normalization matches the actual mean
and variance, with reflection allowed as in C028q/r. The question is
local independent control of the two remaining invariants, with the
possible downstream use of removing the next coefficient residual.

The prospective bounded test is the determinant of their Jacobian in
the two site locations at d=4, (a,b)=(0,1). Continue only with a justified
nonzero certificate or an informative structural degeneracy; do not
turn a zero-containing enclosure into a rank claim or perform a parameter
sweep. This is a proposed test for the source reviewer, not a computed
formula or an approved research task. That reviewer may replace it if a
known obstruction or duplicate settles it. Even nonzero rank proves
only local openness; the actual coefficient pair must separately lie
in the relevant image before matching could follow. Higher-degree
control, lower residuals, norms and full cost remain independent gaps.

Essential local inputs for later assessment: L019/L021, L025/L027,
C028a/b/q/r/s, and L917/audit197 only if saved moment boxes are used.
Retain L037's library hypothesis whenever that input is invoked.
For degree4 the reviewer must identify all moment orders and arithmetic
coverage actually required, rather than assume the four-moment H
certificate covers a new Gram-matrix or Jacobian calculation.

Before approving mathematics, search exact and stronger multi-site
Uvarov coefficient/zero-moment rank or range results, and check the
primary theorem hypotheses and proof cases needed for the finite
two-site system. Reuse1908's adequate modification/zero-theorem reads;
do not substitute exterior-support attraction or fixed-site mass limits
for location variation on support R. Wilkins1944 is still an unread
lead from1908, not an imported skewness/kurtosis theorem.

No justified creative full-residual mechanism is ready yet. This
nomination prepares independent feasibility coverage; it does not label
a finite rank specialization creative to fill a scheduling target.
