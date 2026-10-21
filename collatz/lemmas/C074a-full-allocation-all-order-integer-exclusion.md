# C074a — Full-allocation all-order integer exclusion

## Hypotheses

Keep exactly L055's complete 25 indexed pairs J_i,H_i, 0<=i<=24.
Let b_i be nonnegative integers with sum b_i=9250245, and attach
a_i=2+18b_i to indexed row i. Let pi be any permutation of
{0,...,24}. Require real junctions s_0,...,s_25 with s_25=s_0,
s_k>=540/11 and, for every chronological position 0<=k<=24,

\[
s_{k+1}=2^{-a_{\pi(k)}}\left(G_{\pi(k)}s_k-Q_{\pi(k)}\right)+23/11,
\qquad G_i=(27/16)^{J_i}(3/2)^{H_i},
\quad Q_i=(12/11)(3/2)^{H_i}+1,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{2}
\]

These are L051's endpoint/domain/non-strict own-input J conditions,
with each allocated tail attached to its outgoing indexed pair.
Logarithms are natural. Put n_k=s_k-23/11. No H guard, seed,
minimum location, distinguished large-tail row, actual-word, parity,
residue, exact-valuation or primitive/count-ray premise is assumed.

## Conclusion

No such tuple has every unshifted junction n_0,...,n_24 integral,
for any allocation and any cyclic presentation of the intact indexed rows.
More precisely, if q is the unique chronological position with pi(q)=0,
then every tuple satisfying (1)–(2) has n_q nonintegral. This does not
assert nonintegrality of each junction or of a predetermined chronological n_0.

This is a local RESEARCH/REPRODUCTION assembly under the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-full-allocation-all-order-integer-assembly.md`.
It combines audited inputs and claims no originality beyond the inspected
sources. The separate critical audit below found no defect. Both positive
rational witnesses and Attempts 026–031 remain valid. Actual-word transfer,
other pair tables, unrestricted cycles, entry, divergence and universal
eventual descent remain outside this conclusion; this is not a Collatz candidate.

## Proof

### Rigidity and the selected cut

The indexed pairs, nonnegative integer allocation, full budget, attached
tails, arbitrary permutation, real lower domain, all 25 endpoints and
own-input non-strict J guards are exactly L074's hypotheses. Thus its
audited conclusion applies: pi is a rotation of the literal order
0,1,...,24. We use this cyclic-order conclusion, without assuming a
given minimum location or identifying any distinguished tail.

Because pi is a permutation, there is a unique q in {0,...,24} with
pi(q)=0. Since the cyclic order is literal, for every 0<=i<=24,

\[
r_i=(q+i)\bmod25,\qquad \pi(r_i)=i.
\tag{3}
\]

Set r_25=q, t_i=s_{r_i} for 0<=i<=25, and
m_i=t_i-23/11. In particular t_25=t_0 and m_0=n_q.
The map i -> r_i on {0,...,24} is a bijection, so every original
input appears once in this rotation. Indexed allocations b_i and tails
a_i remain attached to row i; we do not rotate the tails independently
of the pairs or reinterpret b_i as a chronological allocation.

### Every endpoint and own-input guard survives

For each 0<=i<=24, r_(i+1)=r_i+1 modulo 25. If r_i<24,
original edge r_i has output s_(r_i+1)=t_(i+1). If r_i=24,
its output is s_25=s_0=t_(i+1). In both cases its outgoing row
is pi(r_i)=i by (3), so (1) becomes

\[
t_{i+1}=2^{-a_i}(G_i t_i-Q_i)+23/11,
\qquad 0\le i\le24.
\tag{4}
\]

Explicitly, the old closing edge, from position 24 to position 0,
occurs at new position i=24-q. The new closing edge, at i=24,
is the old edge from q-1 to q, with positions interpreted modulo 25.
For q=0 these are the same closing edge. For q>0 the old closing
edge is an interior edge and the new closing edge is old edge q-1.
Thus neither cyclic cut omits an equation, including when a closing
tail is 2 or junction values coincide.

Original guard r_i in (2), paired with its unchanged own input, is

\[
4J_i\log2\le\log t_i+\log(11/4),\qquad 0\le i\le24.
\tag{5}
\]

Every t_i>=540/11, including t_25 by closure. The allocation remains
the same nonnegative integer vector b_i of total 9250245, with the
same a_i=2+18b_i. Expanding G_i and Q_i in (4) gives exactly
C073a's literal endpoints, both subtractive terms and the final shift.
Equations (5) give exactly its non-strict own-input guards. We have
therefore matched every C073a hypothesis, including all endpoints,
the domain and closure, without importing the extra H/seed or count
conditions of L051 or L055's particular witness allocation.

### Unshifted integrality at the tested cut

C073a's audited stronger conclusion says that the literal starting
unshifted coordinate is nonintegral. For the matched tuple t that
coordinate is exactly

\[
m_0=t_0-23/11=s_q-23/11=n_q.
\tag{6}
\]

Consequently n_q is nonintegral. If all original unshifted junctions
were integral, n_q would be integral, a contradiction. Rotating real
junctions never substitutes shifted integrality for this premise.
There is no need to claim that any other individual n_k is nonintegral.

C073a already handles the exhaustive support split, both last-pair
boundary allocations, unique survivor roots and their different
unshifted integer numerators. Those audited conclusions are imported;
no affine theorem, residue evaluation or endpoint uniqueness argument
is reproved here. The underlying standard input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only formal chronological affine composition and the fixed-point formula
for nonempty words with nonzero denominator enter the audited inputs.
Their fixed counts and positive Lambda retain that denominator
qualification. The present specialization needs only the explicit
rotation and exact hypothesis match above, not an integer-itinerary
or actual-word converse.

C063a and C067a are narrower survivor-allocation assemblies, not direct
inputs to this proof. The two rational witnesses remain feasible because
their tested unshifted roots are nonintegral. No real-subsystem exclusion
or stopped permutation-prime diagnostic is asserted or restarted.

### Separate critical audit — 2026-10-17, step 273

The prior SPECIALIZE assessment
`drafts/literature/2026-10-17-full-allocation-all-order-integer-critical-audit.md`
authorizes this RESEARCH/REPRODUCTION audit. The verdict is no defect in
the stated full-simplex all-order integer exclusion. This verifies the
local assembly of audited inputs; it supplies no new exclusion beyond
that assembly and no originality claim beyond the inspected sources.

**Exact rigidity invocation.** L074 has the identical 25 indexed pairs,
nonnegative integer b_i, sum 9250245, attached tails 2+18b_i, arbitrary
permutation pi, real lower domain, closure, endpoint equation and
non-strict own-input J inequality. Its definitions of G_i and Q_i are
identical to (1). No additional premise is needed to use its cyclic-order
conclusion. In particular its proof's choice of a minimum is not a premise
of C074a, and this assembly does not use its stronger minimum-normalized
conclusion. L055 supplies the complete indexed pair table, not its
particular tail allocation or witness guards; L051 supplies the stated
endpoint and J conventions, not its other system assumptions.

**All occurrences and both cuts.** Cyclic literal order means there is
c in {0,...,24} such that pi(k) is the representative of c+k modulo 25.
The unique q=pi^(-1)(0) therefore satisfies c+q=0 modulo 25. For each
i=0,...,24, pi((q+i) mod 25) is the representative of i, hence exactly
i. Translation modulo 25 is injective on these 25 indices: equality
of two images implies 25 divides their difference, whose absolute value
is at most 24. It is therefore bijective. Coincident real values of
different junctions do not affect this statement about occurrences.

For i=0,...,24, the successor r_(i+1) is the representative of r_i+1
modulo 25, including r_25=q. If r_i<24, the original output is
s_(r_i+1)=t_(i+1); if r_i=24, it is s_25=s_0=t_(i+1).
Thus each original edge gives (4), and the bijection shows that all
25 edges are used once. Since 0<=q<=24, the unique i in this range
with r_i=24 is 24-q. The new closing edge i=24 starts at
r_24=(q-1) mod 25 and ends at q. When q=0, old edge 24 is also
the new closing edge. When q=24, old edge 24 becomes new edge 0,
and old edge 23 becomes new edge 24. For every intermediate q,
old edge 24 is interior and old edge q-1 closes the rotated tuple.
These cases verify both cuts without dropping or duplicating an equation.

At r_i the outgoing label is i, so its tail is a_i=2+18b_i,
not a_(r_i). This distinction retains the original indexed allocation
even when the chronological starting row changes. It also retains tails
equal to 2, including either closing tail. No row is selected by tail size.

**Complete C073a match.** The rotated tuple has t_25=t_0 and every
t_i>=540/11. Its pairs and allocation vector are unchanged, with the
same nonnegative integer entries and total. Expanding Q_i in (4) yields
the two subtractive terms -(12/11)(3/2)^H_i and -1 inside the tail
factor, followed by +23/11, exactly as in C073a. The outgoing row i's
original inequality at r_i gives (5), with the same natural logarithm,
same non-strict sign and same own input t_i. Hence every literal premise
of C073a holds, including its closing equation. Neither theorem asks for
H guards, a seed, a minimum, a primitive/count ray or an actual itinerary.
All logarithms are defined by the retained positive lower domain.

**Tested coordinate and scope.** C073a's canonical conclusion and its
separate audit expressly give nonintegrality of the literal starting
unshifted coordinate, rather than only an existential failure of
integrality somewhere. Here that coordinate is t_0-23/11=s_q-23/11=n_q.
Thus C074a's stronger conclusion follows, and an all-integral original
tuple contradicts it. The argument makes no inference from integrality
of s_q, or from integrality of a predetermined chronological n_0 when
q differs from zero. It asserts no nonintegrality of every individual
junction and uses no affine-closure converse.

The imported C073a audit retains the exhaustive allocation split,
endpoint uniqueness and the distinct survivor numerator obstructions.
Those established inputs are not reproved or independently recomputed
in this reindexing audit. Their primary affine citation and nonempty-word,
positive-Lambda/nonzero-denominator qualifications above remain unchanged.
The direct mathematical uses remain L051's definitions, L055's table,
L074 and C073a, as recorded in the DAG. No new dependency, mathematical
script or change to the assembled argument is required. Full matching
Mathlib coverage remains unchecked as stated below.

The two rational witnesses and Attempts 026–031 remain valid: real
feasibility and stopped modular diagnostics are not contradicted by
nonintegrality at the identified cut under the complete guard system.
Actual-word transfer still requires separate scope review and work;
other pair tables, unrestricted cycles, entry, divergence and universal
eventual descent remain unresolved. This is not a complete Collatz candidate.

## Mathlib

Full matching theorem coverage is unchecked; no formal verification is
claimed. The inherited assessment records supporting
`padicValRat.defn`, `padicValInt_dvd_iff` and
`Rat.num_or_den_zero_padicVal` in
[PadicVal.Basic at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
with prime, nonzero and reduced-pair coprimality qualifications. This
assembly uses C073a's existing nonintegrality conclusion and finite
cyclic reindexing, with no new valuation input. Unknown full coverage
is not evidence of absence.
