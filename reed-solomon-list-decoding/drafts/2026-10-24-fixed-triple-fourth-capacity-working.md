# Fixed-triple fourth-order calculation — working record

Approved target: Assess fourth-order Boolean/cardinality capacity for A={0,...,67}, B={0,...,62,68,...,72}, C={0,...,62,73,...,77} at L112's unchanged assignment.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-fixed-triple-fourth-cardinality-capacity.md`.
The main gap is arbitrary-center 67/68 safety. This test may reject a
stronger fourth-order extension of this one assignment, independently
of PSD. Pass/straddle parks this test; no refinement or other triple.

## Specialization saved before enumeration

Import Laurent PNA-R0108 Section 3.1 (11)–(12), Lemma 2(ii),
pp.5–6, as recorded in foundations/15. For four distinct variables,
write m(S)=rho*b(S) for nonempty proper S, m(empty)=1, and
m(ABCD)=rho*q. Here b(singleton)=1, b(pair)=c_distance,
and b(triple) is the L114 prescribed product/zero value. For each
ones-set S the atom divided by rho is

    sum_(S subset J subset W) (-1)^|J\S| m(J)/rho.

Thus the exact lower candidates for q are zero, the six
`b(S+i)+b(S+j)-b(S)` for |S|=2, and
`4-sum_pairs b+sum_triples b-1/rho`. The exact upper candidates
are the four triple moments and the four
`1-sum_(pairs containing a) b+sum_(triples containing a) b`.
Their maximum/minimum give [L,U]; all 16 atoms, including the empty
ones-set, occur. This is elimination of one scalar coordinate in an
imported finite inversion theorem, not a reproof of that theorem.

Import Raghavendra–Tan arXiv:1110.1064v1 Section 3 p.8 through
foundations/13,15. Multiplying its triple-all-ones conditional equation
by H*m(ABC), including a zero conditioning event homogeneously, gives
sum_D m(ABC union D)=N*m(ABC). Dividing by rho>0 gives
sum_D q_D=N*z, z=b(ABC)=x5^3>0. The three repetitions D=A,B,C
each have q_D=z. Hence distinct D require sum_D q_D=(N-3)z.
No factorial division occurs. Separate intervals can meet this one
row exactly iff the required value belongs to their weighted sum
interval, without implying a shared system for other fixed triples.

The regions indexed by membership masks 0,...,7 have sizes
`[946,5,5,0,5,0,0,63]`. Enumerate nonnegative occupancies k_j
bounded by these sizes with sum 68, multiplicity product binom(size,k).
Distances to A,B,C are 68 minus the occupancy sums in the respective
membership bits. Stabilizer permutations within each region preserve
all distances, hence the explicit product prescription and raw moments.
The sum of all multiplicities must be H. Repeated supports each have
one occupancy and multiplicity one; null distances are retained.

Plan one complete enumeration and an independent reconstruction.
Certify smaller marginal atoms as well as every fourth-atom candidate.
If all distinct intervals simplify to [0,min four triples] throughout
the original box, compare a lower enclosure of the total upper capacity
with an upper enclosure of (N-3)z. A strict pass is a one-row extension
pass only. No solve, changed box, PSD, measure or RS claim.

## Completed bounded step

L121 contains the canonical proof and full certificate references.
The complete enumeration has 13,214 occupancies and 5,729 types;
all smaller atoms and all sixteen fourth-atom conditions pass, including
323 null occupancies and three repetitions. The constructor and
independent verifier pass 396,970 and 117,635 checks, with zero failures.
The exact total-capacity/required ratio is in
(93301984669,93301984670), so the one-row common-factor construction
passes. Park this diagnostic without another triple or refinement.
Independent arithmetic reconstruction is complete; dedicated critical
proof review is pending. The scoped documentation checker passes.
