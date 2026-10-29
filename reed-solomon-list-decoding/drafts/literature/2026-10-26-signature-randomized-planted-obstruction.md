# Signature-randomized planted-obstruction source assessment

TARGET: Assess whether signature-randomizing L131's right map can preserve S1–S4 while admitting cross-packed subfamilies of size at least 1532496 on each side.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six targeted discovery queries compared prescribed random bijections, planted alteration and random-injection packing; inspected primary statements are identified below. Scoped local comparison used L130/L131/L133, the threshold-retention, mixed-core supersaturation and independent-translation assessments, ATTEMPTS/106–108 and history/518. No inspected source gives this conditioned finite retention assertion; no novelty claim follows.
SOURCE_EVIDENCE: Reuse Alon–Spencer, The Probabilistic Method, third edition (2008), Theorem 3.2.1 and full proof pp. 29–30 through the prior threshold-retention assessment; newly read Kamcev–Sudakov–Volec arXiv:1601.02271v2 Section 2 and Theorem 2.2 p. 5, Appendix A pp. 16–17, and Lu–Szekely (2007) Theorems 1 and 2, pp. 4 and 9. Product-space sampling and alteration are standard inputs; no local-lemma conclusion is applied.
COMPARISON: Part-respecting random injections cover the signature-partition sample-space framework, and finite averaging plus endpoint deletion cover the general method. They do not give instance-specific conditional conflict probabilities, protected-endpoint loss bounds or balanced retention. L130's unconditioned seven-subset law is inapplicable without a fresh count; L133 concerns only the ordered map.
GAP: Establish the exact signature-conditioned image laws and simultaneous per-side deletion bounds while protecting S1–S4. The deterministic protected-right conflicts and random protected-left conflicts must be included before any favorable-map claim. No such count, loss bound or existence result is established in this source review.
REASON: Essential comparison is now complete for one bounded alteration specialization on the unchanged finite model. It is ready for separate next-turn approval, not a completed construction or a mathematical attempt in this turn.
SCOPE: Only the fixed L131 left map, independently uniform right signature-class bijections with d_0 mapped to a, and one witness-protecting first-moment deletion test; no other maps, LLL application, rank forcing, marginal law or RS transfer is approved by this assessment.

LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked coverage for the changed conditional distribution and protected deletion. This turn resolves that specific gap rather than repeating L130's ready unconditioned review.

## Exact scope and relevance

Use L030/L131's q=137, T, actual subgroup labels, K,a,b,C,C',
p=0 and r=Z-16. Keep L131's left bijection and its distinguished
image sigma(16,1)=b. Replace its right ordered matching by a uniformly
chosen bijection in each membership-signature class for
(B_p,B_r) and (S3 minus C', S4 minus C'), conditional on sigma'(d_0)=a.
This proposed finite space preserves the two designated right graph
images by definition; its packing and retention consequences are
unknown. All source comparisons must retain this exact conditioning.

The proposed construction seeks retained families containing S1,S2 on
the left and S3,S4 on the right, each of size at least 1532496, with
every pair of distinct full supports intersecting in at most 63 points.
The prospective bounded test is an exact expectation-and-protected-
deletion calculation. The comparison below supplies source coverage;
the mathematical counting and its separate invocation remain pending.
Do not import L130's uniform seven-subset probability under changed
conditioning, or assume that a favorable map protects the four supports.

The main RS safety gap and bracket 955–957 remain open. Success would
show that large retention and local/two-core packing can coexist with
an actual-label common-center obstruction, clarifying the insufficiency
of these restrictions for RS realization. It would not force a witness
in every large pair, give a universal cap or disprove RS safety. Failure
of one expectation bound need not refute existence; record exact losses
and stop unless a materially refined mechanism is justified.

Essential local inputs are L030, L031 as imported in audited L131,
L130, L131 and audited L133. Preserve ATTEMPTS/103–108: this neither
reopens the ordered-map threshold instance nor assumes its packing.
No cross-notebook theorem or Mathlib matching result is asserted;
full/supporting Mathlib coverage is not checked. No new mathematics
has been derived in this review.

## Primary sources and precise applicability limits

Reuse the actual primary inspection in
`2026-10-26-threshold-retention-ambient-overlap.md`: Noga Alon and
Joel H. Spencer, *The Probabilistic Method*, third edition, Wiley,
2008, ISBN 978-0-470-17020-5, Theorem 3.2.1 and its complete proof,
printed pp. 29–30 (PDF pp. 48–49),
[book PDF](https://math.bme.hu/~gabor/oktatas/SztoM/AlonSpencer.ProbMethod3ed.pdf).
For a graph with n vertices, nd/2 edges and d>=1, its displayed bound
is alpha(G)>=n/(2d). Its proof averages sampled vertices minus
surviving edges and removes an endpoint per remaining edge. Import
finite averaging and this deletion principle, without reproving the
general theorem. The displayed independence bound supplies neither
balanced retention nor a guarantee that designated vertices survive.
Repeated endpoints can reduce deletion losses; independence of edge
events is unnecessary for expectation. The old assessment's Markov
input is available but no joint probability estimate is presumed here.

Nina Kamcev, Benny Sudakov and Jan Volec, *Bounded colorings of
multipartite graphs and hypergraphs*,
[arXiv:1601.02271v2](https://arxiv.org/pdf/1601.02271v2), 26 October
2016; published European J. Combin. 66 (2017), 235–249,
[DOI](https://doi.org/10.1016/j.ejc.2017.06.023).
Section 2 and Theorem 2.2, printed p. 5, consider disjoint parts
X_i,Y_i with |X_i|<=|Y_i| and independently uniform injections
X_i -> Y_i. Canonical events prescribe partial part-respecting maps;
joining events whose prescribed domains or images intersect gives a
negative dependency graph. Appendix A, Theorem A.1 and proof,
pp. 16–17, uses conflicting partial maps, part-preserving symmetry
and partitioning by the image of a fixed domain. These passages were
read, but no negative-dependency or local-lemma conclusion is imported.
Only the stated sampling framework is needed for the proposed
first-moment test. Use the disjoint signature classes as parts and
remove the fixed d_0,a pair first; equality of their remaining sizes
is supplied by L131's table. This identifies the appropriate standard
framework, not a computed block-image law or retention bound.

Linyuan Lu and Laszlo Szekely, *Using Lovasz Local Lemma in the space
of random injections*, Electron. J. Combin. 14(1) (2007), R63,
[journal PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r63/pdf/),
published 7 September 2007. Read Section 2's canonical-event definition
and Theorem 1, printed p. 4, and Section 4's Theorem 2 and full
packing proof, p. 9. Theorem 1 treats uniform unrestricted injections
and conflict of partial maps. Theorem 2 assumes two r-uniform
hypergraphs with m_i edges, each edge meeting at most d_i others,
n>=max{|V(H_1)|,|V(H_2)|}, and
(d_1+1)m_2+(d_2+1)m_1 < binom(n,r)/e. It supplies embeddings with
edge-disjoint images. It does not prescribe our signature classes,
protect our four supports or supply a deletion budget. No encoding or
verification of that inequality is present, so this stronger packing
result is excluded, not applied. The product-space source follows
this reference and addresses its unrestricted-space limitation.

No literature theorem inspected proves the desired finite assertion.
An original proof of a general alteration or injection theorem is
unnecessary; the justified specialization is exact conditional counting
and checking protected losses in this one finite model. Optional LLL
methods would require a separately assessed event encoding and bounds.

## Search, duplicates and recorded failures

Discovery queries on 2026-10-26:

- `"random bijections" "alteration" prescribed`
- `"random injections" "canonical events" Lu Szekely 2007`
- `"planted" "alteration" "packing" probabilistic method`
- `"Bounded colorings of multipartite graphs and hypergraphs" pdf`
- `"planted" "protected" "alteration" combinatorics random permutation`
- `"packing" "prescribed" "random injections"`

The directly relevant primary matches were the two injection papers
above. A Lu–Mohr–Szekely survey and a thesis were discovery leads
only; their theorems are not inputs. Unrelated planted-model and
stochastic-optimization hits supplied no coverage. The publisher DOI
open returned 403; the pinned primary arXiv v2 supplied the relevant
statement and appendix, so this is not an essential source blocker.
Search failure establishes no novelty.

Read L130's conditional-space, averaging and deletion proof; L131's
entire construction and separate audit; and L133's hypotheses,
conclusion and matching setup. The latter audit acceptance is supplied
by history/518 and the startup checkpoint; no enumeration was repeated.
L030's model and L131's audited use suffice for the local polynomial
packing input; no moment extension or new rank calculation is needed.
Scoped searches covered the recent assessments and working notes.

L130 removes the left b-star and deletes right conflicts without
protecting S3/S4. L131 establishes the four fixed supports but disclaims
survival at large retention. L133 closes its ordered right map as a
threshold example. ATTEMPTS/106 concerns retention-to-star overlap;
ATTEMPTS/107 concerns only a synchronized witness cover; ATTEMPTS/108
concerns the fixed-map conflict matching. None establishes a loss
estimate for the signature-randomized distribution. The earlier
supersaturation and independent-translation source comparisons remain
adequate for their separate targets and are reused, not reopened.

## One bounded mathematical test, pending separate approval

Keep TARGET exactly. Begin with L130's left family omitting b, using
L131's unchanged left map and keeping its p,r indices distinguished.
The following is proposed bookkeeping to justify in the research turn,
not a proved deletion bound:

1. Count all left supports conflicting with fixed S3 or S4 and consider
   deleting those left endpoints. Verify S1 and S2 survive this rule.
   Report the eligible left size and actual remaining deletion budget;
   L130 records the initial 2552584 and margin 1020088 over 1532496.
2. Sample the right map in the four signature classes, with fixed
   d_0->a removed. L131 records the remaining class sizes 949,6,6,1.
   For every relevant right polynomial, account for its occupancy in
   all classes, including the singleton, and derive its exact image
   probabilities by counting bijection completions. Keep the small
   classes and p,r cases; do not replace them by a uniform seven-subset.
3. Account for right conflicts with protected S1/S2, then propose
   deletion of right endpoints for the remaining conflicts. Establish
   that no step deletes S3/S4. Include all conflicts on actual labels,
   not just matching auxiliary columns; verify the distinct-support
   condition. One scalar right-loss majorant may combine the protected-
   left losses and remaining edge count, but its validity and exact
   expectation still need proof.
4. Compare the deterministic left loss and one joint right-loss bound
   against their respective budgets. L130 records the right initial
   size 2571353 and budget 1038857. Averages for two separately
   favorable random events do not certify a common map. Justify the
   finite averaging and integer rounding for the chosen single bound,
   and verify all four survivals and full cross-packing together.

Continue only if this calculation rigorously certifies both retained
sizes >=1532496 and protection of S1–S4 for the same allowed map,
or gives a new decisive obstruction to this specific mechanism.
If its sufficient budget fails, preserve the exact failed inequality
and stop this first-moment deletion route; that alone does not refute
existence. No automatic enlargement to LLL, other maps or shift scans.
Any refinement must name new input and a discriminating test.

The plausible downstream use is a packed large-retention example
already containing an actual-label common-center obstruction, showing
why those local conditions cannot guarantee RS realizability. This
does not negate universal witness forcing, prove an RS cap, prescribe
marginal laws or improve the 955–957 bracket. These independent gaps
remain explicit. This is a standard alteration specialization; the
review does not justify labeling its counting as a creative universal
RS mechanism. No lemma or mathematical script was changed, and no
expectation, loss or new mathematical result was derived this turn.
