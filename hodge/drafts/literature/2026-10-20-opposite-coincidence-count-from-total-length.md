# Ordered coincidence count from total normalization length — source assessment

TARGET: Bound the number of ordered opposite coincidences in terms of L138's fixed parameters using the residue-value map at each normalization fibre.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched normalization delta invariant number branches delta >= r - 1 singularity; Stacks finite algebra semilocal Chinese remainder residue fields normalization; and exact Chinese-remainder, finite-semilocal and length/residue-field variants; followed primary curve references to their underlying algebra statements.
SOURCE_EVIDENCE: Read Stacks 10.15.4 (00DT), 10.52.3 (00IV), 10.52.6 (00IY), 37.42.1 (0BSR, first-proof residue-surjection case), 53.16.1 (0C1V), 53.16.3 (0C1X), and 33.40.6 (0C43), live HTML on 2026-10-20; exact links and hypotheses below. Reuse L120/L121/L137/L138's finite-map and fixed-bound coverage.
COMPARISON: Chinese remainder supplies the dimension-independent residue surjection; the inspected delta/branch theorems concern dimension one and cannot be imported as surface theorems. The remaining actual quotient specialization and finite-partition count are elementary applications, not a new general algebra theorem.
GAP: Write the local quotient factorization and its length comparison, then bound the total ordered reduced count for arbitrary fibre partitions using L138; no count formula or new lemma is established in this literature turn.
REASON: Essential primary coverage is now sufficient for one bounded mathematical specialization; no further discovery search or reproof of Chinese remainder is needed.
SCOPE: The unchanged hypothetical L071/L118 kernel, L120's finite birational unramified normalization, L121's finite reduced off-diagonal scheme and L137/L138's original fixed embedding; no normality, CM property, collision existence or minimal-defect equality.

## Primary statements and inspected cases

The sources are the live Stacks Project HTML versions retrieved on the
CHECKED date, with stable tags fixing the cited results.

- [Lemma 10.15.4, Chinese remainder (00DT)](https://stacks.math.columbia.edu/tag/00DT):
  for any commutative ring and finitely many pairwise comaximal ideals,
  the quotient by their product is the product of the quotients; distinct
  maximal ideals meet the comaximality hypothesis. Read the full proof,
  including the construction of preimages of arbitrary residue tuples.
  It has no dimension, normality, smoothness or completeness hypothesis.
- [Lemma 37.42.1 (0BSR)](https://stacks.math.columbia.edu/tag/0BSR):
  the theorem concerns an integral ring map, finitely many primes over a
  selected prime and finite maximal separable residue subextensions.
  Read its statement and the first proof's finite-discrete-fibre case:
  it explicitly uses 00DT to obtain the surjection from the fibre algebra
  to the product of its residue fields. Only that cited proof case is
  needed; the subsequent etale splitting conclusion is unnecessary here.
- [Lemma 10.52.6 (00IY)](https://stacks.math.columbia.edu/tag/00IY):
  an R-module annihilated by a maximal ideal has length equal to vector
  dimension over the residue field. Read the statement and proof.
  [Lemma 10.52.3 (00IV)](https://stacks.math.columbia.edu/tag/00IV)
  gives length additivity for every short exact sequence of R-modules;
  read the induced-filtration proof. These are the applicable tools for
  a quotient killed by the image-point maximal ideal.
- [Lemma 53.16.1 (0C1V)](https://stacks.math.columbia.edu/tag/0C1V)
  assumes a one-dimensional reduced Nagata local algebra over a separably
  closed field with that residue field. It bounds delta below by the
  branch number minus one, and describes the equality completion.
  Followed its inequality reference to
  [Lemma 33.40.6 (0C43)](https://stacks.math.columbia.edu/tag/0C43):
  this also explicitly assumes dimension one; read its strict-henselization
  proof. Neither statement is a dimension-two import.
- [Lemma 53.16.3 (0C1X)](https://stacks.math.columbia.edu/tag/0C1X)
  concerns reduced one-dimensional algebraic schemes over an algebraically
  closed field. Its equivalence characterizes minimal delta by multicross
  singularities. Read the proof's equal-residue gluing calculation and
  its tangent-squishing distinction. It supplies context for the standard
  terminology, not a minimal-defect assertion for the present image.

Also inspected Stacks 10.52.8 (00J0), finite length under maximal-ideal
nilpotence, and 10.52.4 (00IW), the converse nilpotence assertion.
They add no needed hypothesis: L138 already supplies finite length.
Search hits on curve delta semicontinuity (arXiv:2107.07012,
2101.01784), a plane-curve analytic paper and MathOverflow were leads
only; their full papers were not inspected or used as theorem evidence.
No claim of novelty follows from these searches.

## Applicability and remaining specialization

Use A=O_{Z,z} and the actual finite A-algebra
C=(nu_*O_B)_z. Its fibre is finite, and its maximal ideals over the
closed point correspond to the normalization preimages. All residue
fields are C (the complex numbers). These are exactly the finite-map
and residue hypotheses needed for the cited Chinese-remainder proof
case; no product decomposition of the uncompleted semilocal algebra
is asserted. The source B is not to be confused with this algebra C.

The research step should import 00DT directly, then check the image
of A in the residue tuple space and factor evaluation through the
actual module C/A into the quotient by diagonal constants. This
factorization and the ensuing length comparison must be written in
the canonical proof, retaining A-linearity and the residue-field
module action. There is no reason to reprove 00DT or to apply a
one-dimensional delta theorem to this surface.

The remaining global task is a finite combinatorial comparison between
fibre cardinalities and ordered distinct pairs, using L121's actual
reducedness and L138's total length. It must include singleton fibres,
empty collisions and arbitrary multiple fibres. No optimized partition
bound, count identity or specialized inequality is proved here. The
scope is narrow enough that the inspected general tools and ordinary
finite-sum arithmetic cover the proposed calculation; an unrelated
stronger geometric lower bound remains uncovered.

## Duplicates, obstructions and decision test

Targeted local searches found no completed ordered-count conversion
in the opposite/normalization assessments or L120--L129. L125 and
L129 control particular local defects or upper bounds; neither is the
proposed lower comparison and global count. L138's existing regularity
coverage is reused without another regularity search.

ATTEMPTS/070 and audited L122 refute equality with branch number minus
one under the selected local geometric properties. That failure does
not supply a failure of a lower comparison. ATTEMPTS/073's missing
coherent vanishing and ATTEMPTS/078's uncontrolled middle-Hom Euler
term remain parked. This target uses L138's independent upper control
and needs none of those assumptions; it does not reopen their proofs.

The main gap is universal primitive Hodge realization. Essential local
inputs are L120, L121, L137 and L138 under the hypothetical L071/L118
F; no F or collision existence is known. The intermediate target is
one uniform ordered-count upper bound. A possible downstream use is
to constrain collision configurations and L136's middle-Hom Euler term;
L136 is a downstream comparison only, not an input to the count proof.
Even a successful count supplies no contradictory lower bound, cycle
or transverse transport.

Continue if the actual quotient factorization and reduced count give
a fixed bound for every finite fibre partition. Abandon this conversion
if it requires minimal gluing, uncontrolled scheme multiplicities,
normality, CM, vanishing or a middle-Hom Euler upper bound. A numerical
value for ell,k,N is not required for the stated fixed-parameter target.
The known algebra tools suffice for a REPRODUCTION specialization;
this assessment does not certify originality of any future result.
Full matching Mathlib coverage is not checked. No lemmas, mathematical
scripts, DAG or argument overview were changed in this literature turn.
