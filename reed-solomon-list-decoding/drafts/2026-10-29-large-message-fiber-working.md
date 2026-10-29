# Large repeated-message fiber — bounded mathematical attempt

The invocation-start EXPLORE assessment is
`drafts/literature/2026-10-29-large-message-fiber-propagation.md`.
The exact target is whether a message attained at more than 272 auxiliary
points forces full-sheet constancy. This is one attempt on that target;
the direct-rank, one-point, reflection, translation and general-incidence
stops in ATTEMPTS/109–114 remain preserved.

## Scope and test

Use L030's distinct actual labels and precisely the full-sheet hypotheses
restated in L138, over either K=E or K=F. No translation inclusion,
auxiliary degree bound, injectivity or coefficient-span restriction is
assumed. The main gap is arbitrary-center 67/68 safety. A positive fiber
implication could isolate high multiplicity, but would not establish
existence of a large fiber, small-fiber rigidity, retention or RS transfer.

The bounded test is a complete propagation proof, or a permitted complete
full-sheet counterassignment with a fiber of size greater than 272.
An incomplete patch or a set satisfying only combinatorial necessary
conditions is not a counterassignment. If inconclusive, record the exact
remaining implication and stop this attempt.

## Reasoning checkpoint

Subtract the putative repeated quadratic g from every message and from
the corresponding line values. Let S be its zero-message fiber. A selected
direction line meeting S has zero value at its own actual label. Thus an
off-fiber point can lie on at most two such lines: three would give three
distinct roots of its nonzero quadratic. The root theorem is imported
from Conrad, *Counting Roots of Polynomials*, Theorem 1 and Lemma 2,
pp. 1–2, as precisely cited in the assessment; the zero and nonzero
constant cases must be retained.

This is a necessary closure property, not yet the desired size bound.
The current question is whether the seven-class closure property, or the
remaining off-fiber quadratic equations, forces a proper S to have at
most 272 points. No conclusion has yet been established.

## Finite propagation test planned

For a subset of auxiliary points, activate every selected-direction line
meeting it. Whenever a point lies on three active lines, add that point
and activate its seven lines. Every addition is forced inside an actual
equality fiber by the imported root theorem. This uses auxiliary affine
translations and common nonzero scalar dilations only to normalize seeds;
those maps preserve the seven direction classes, not the actual labels.
The closure rule is label-independent because the labels are distinct.

A fiber of size greater than 272 has a pair on a direction-16 line.
Normalize that pair to A=(0,0), B=(-16,1). Every further fiber point C
must have a proper closure of {A,B,C} if the fiber is proper. Enumerate
all C and retain complete nonpercolating closures. If fewer than 273
possible C remain, this proves the target. If more remain, test whether
the same closure constraints give a useful bound after one further
conditioning point; do not confuse the exceptional union with a closed
set or a feasible assignment.

A propagation trace may terminate once 411 lines have been activated.
Indeed, in a proper closed set an exterior point has at least five
inactive incident lines. Pick one such line L of direction t. Each of
its 137 exterior points lies on at most two active lines, and every
active line of another direction meets L once. Hence M-m_t<=274,
where M is the total number of active lines and m_t<=136 because L
is inactive. Therefore M<=410. This stopping certificate is a direct
count for this closure rule, not an imported percolation theorem.

The enumeration is a diagnostic until its complete relevant certificate
is inspected and the logical reduction is recorded. It proves no
full-sheet counterassignment even if many exceptional seeds remain.

The complete fixed-pair enumeration reports 7538 exceptional third
points, versus the required at-most-272 bound. The largest proper
three-seed closure has size six. This does not bound the union of
exceptional points and does not refute the fiber implication.
`scripts/finite-support/large-fiber-pair-summary.json` records that
failed threshold and the full trace paths.

One refinement remains within the same propagation attempt. For each
selected direction normalize two collinear fiber points to parameters
0 and 1. Compute all exceptional third parameters r. A further pair
r,s in that line must have nonpercolating triples {0,r,s} and {1,r,s}.
Put an edge between r,s only when both tests survive. A certified
coloring with at most six colors bounds a proper fiber's occupancy
on that direction line by eight, including the normalized pair.
If the bound eight holds for all seven directions, write m_t for the
number of active lines of direction t and s for fiber size. Then
m_t>=s/8. On any active direction-t line with r<=8 fiber points,
the other six classes contribute six active intersections at each
fiber point and at most one at each of the remaining 137-r points.
Thus sum_(j!=t) m_j<=137+5r<=177, so 6s/8<=177 and s<=236.
This would settle the approved 272 implication. Failure of the
finite occupancy certificate leaves the original target open.

## Completed result and preserved failures

The uniform bound eight did not pass: the seven certified line bounds
are 7,8,10,14,10,6,7. Keeping these unequal bounds instead gives a
proper-fiber cap of 243. The complete proof, source qualification,
normalization argument and certificate specification are canonical in
[L139](../lemmas/L139-large-message-fiber-forces-full-sheet-constancy.md).
The target implication is therefore supported by this finite proof;
separate critical audit remains pending. This is no RS resolution or
novelty certification, and the small-fiber and transfer gaps remain.

The verifier checked every one of the 959 collinear traces, all graph
edges and all color classes, as well as every one of the 18769 records
of the unsuccessful arbitrary-third-point diagnostic. Its complete
record is `scripts/finite-support/large-fiber-certificate-verification.json`.
The failed 7538-versus-272 and uniform-eight tests remain explicitly
recorded in the certificates and L139; neither is used as a successful
bound. No further closure search was run after the sufficient count
and complete verification passed.

The newly proposed critical audit has a separate REVIEW_REQUIRED
assessment. No audit approval or mathematical audit is claimed in this
research step. ATTEMPTS/109–114 remain preserved, and no stopped route
is reopened by the conditional fiber restriction alone.
