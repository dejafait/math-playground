# L103 — Degree partitions of the rational-factor complement

## Hypotheses

Let A,B,C be positive integers with A^3+B^5=C^11 and gcd(A,B,C)=1.
Let E=Q[t]/((3t²+t+1)^5(1−5t)−B^5/C^11), as in L093.
Assume E has a rational direct factor, equivalently the branch reduced
in L095. Write E≅Q×F, retaining the entire degree-ten complement F.

## Conclusion

There is exactly one rational field component in E. Every number-field
component of F is totally imaginary. In decreasing order and with
multiplicities, the degrees of these components belong to

    (10), (8,2), (6,4), (4,4,2).

More precisely, the whole two-adic algebra of F and its necessary
compatible global degree partitions are:

| Two-adic component degrees of F | Global degree partitions retained |
| --- | --- |
| (10) | (10) |
| (5,3,2) | (10), (8,2) |
| (4,4,2) | (10), (8,2), (6,4), (4,4,2) |

These are an exhaustive necessary covering from the stated real and
two-adic premises. No entry is asserted realizable by a global algebra
or a primitive integer solution. In particular F is not assumed a field.

## Proof

L093 makes E finite étale of degree eleven and gives
E⊗R≅R×C^5. The Q component already contributes the unique R factor.
Thus F⊗R≅C^5. Each field K in the finite product decomposition of F
has no real embeddings; its degree is twice its number of conjugate
pairs and is therefore positive and even. A further Q component would
contribute another R factor, which is impossible. This also proves
uniqueness of the rational component, independent of its presentation.
L095 identifies precisely which original integer branch is under
consideration; none of its unsolved power equations is presumed empty.

At two the Q component contributes Q2. Each of the three entire
products in L093 has exactly one degree-one component. Removing it
leaves, respectively, U10, U5×U3×U2, or U4×U4×U2, where Ud is the
unramified extension of Q2 of degree d. Both degree-four positions are
retained. Cancellation here is justified by uniqueness of decomposition
of a finite étale algebra into fields, not by selecting arbitrary roots.

For completeness, if F=∏Ki is its global field decomposition, then
Ki⊗Q2 is a nonempty product of its completions, with total Q2-dimension
[Ki:Q]. Equivalently the primitive global idempotents decompose into
disjoint nonempty sets of primitive local idempotents after base change.
Consequently every whole local field component belongs to exactly one
Ki. Its degree cannot be split between two Ki. All local degrees must
therefore be grouped in nonempty blocks, whose sums are the global
field degrees. Every sum must be even by the real argument above.
This uses the standard completion decomposition theorem for number
fields and additivity of vector-space dimension.

A single local component of degree ten admits just one grouping, giving
(10). For three labeled local components, every set partition is either
one block, a pair and a singleton (three choices of singleton), or three
singletons. Thus there are exactly five groupings before testing parity.
For degrees (5,3,2), their block sums are, in that order,

    (10); (5,5), (7,3), (8,2); (5,3,2).

Only (10) and (8,2) have all sums even. In particular the two odd
components must be in the same global field, rather than interpreted
as separate global fields. For the labeled degrees (4a,4b,2), the same
five groupings have block sums

    (10); (6,4), (6,4), (8,2); (4,4,2).

All pass parity. The repeated (6,4) retains both assignments of the
labeled degree-four positions; forgetting labels only after the test
gives exactly the displayed covering. These cases exhaust all local
types and all their groupings. Repeated isomorphic field factors are
not discarded, and no condition of global field realization is inferred.

This reproduces the partition method of P. H. C. Putz, *Enumeration of
local and global étale algebras applied to generalized Fermat equations*,
VU thesis (2024), version of record, DOI
[10.5463/thesis.832](https://doi.org/10.5463/thesis.832), notation printed
p.8 and **Proposition 5.24 and its complete proof, printed p.170**
([primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf),
PDF indices 14 and 176). The source's proposition is stated only for
its coefficient set C. We do not import that statement at coefficient
one: its proof groups local degrees and uses the real signature, and
those precise premises are available at coefficient one from audited
L093. The proof above supplies the finite grouping explicitly and
specializes further to L095's global rational-factor branch. It neither
uses nor transfers Propositions 5.25–5.27, their coefficient-dependent
tables, database exclusions or discriminant comparisons. L094 is not
an input. This is REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-19-rational-factor-complement-degree-partitions.md`,
not a claim of progress beyond the checked partition method.

Both L095 integer systems, complete field identification,
discriminant-compatible products, fiber realization and all other
residual Beal signatures remain unresolved. A separate critical
application audit of this specialization is recorded below.

### Independent critical application audit — 2026-10-20

Verdict: **PASS without correction**, for the necessary covering only.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-complement-degree-partitions-audit.md`.
This audit independently checks the transfer and every labeled grouping;
it supplies no stronger covering, field realization or integer exclusion.

The hypotheses and parameter are identical in L093, L095 and this lemma:
positive primitive A^3+B^5=C^11, s=B^5/C^11, and the entire quotient
by phi(t)−s. In particular 0<s<1 ensures etaleness, including any
unit-base case permitted by the hypotheses. L095's audited equivalence
identifies a global rational root with a rational direct factor and with
the two stated integer systems. The present argument assumes that global
factor; the rational component at two alone would not supply it.

Reinspection of Putz's version of record, notation printed p.8 and the
complete Proposition 5.24 proof printed p.170, confirms that its degree
argument uses the real signature and the local degree types from
Propositions 5.18 and 5.20. The coefficient restriction belongs to the
published proposition. Here those two premises instead come from L093's
audited coefficient-one application. No coefficient-dependent local table
or terminal elimination is used. The source's refinement convention
groups local parts to obtain global parts, in exactly the direction used
above. Its published statement is not directly imported at coefficient one.

For the cancellation check, the rational field contributes one real
embedding, exhausting the one-dimensional real factor of E tensor R.
Every remaining component therefore has zero real embeddings, rather than
merely an even number of them. Its degree is positive and even. A second
rational component is impossible. Over Q2 the base change of the global
rational component is a field of degree one; in a finite product of fields
it must be a single primitive factor. Each of L093's three products has
exactly one such factor. Cancelling it leaves all and only the local
factors displayed in the statement, including both copies of degree four.

Independently, let e_i be a global primitive idempotent of F. Its image
in each local field is either zero or one. Orthogonality and sum one
assign each local field to exactly one e_i. The assigned set is nonempty:
K_i tensor Q2 has positive dimension [K_i:Q]. This also proves that its
assigned degrees sum to [K_i:Q], with no splitting of a local field and
no loss of an isomorphic repeated factor. Thus all that is needed is the
following complete set-partition check. Labels a,b,c denote positions,
even when their degrees coincide; vertical bars separate blocks.

| Local degrees | Labeled blocks | Sorted block sums | All even? |
| --- | --- | --- | --- |
| (10) | a | (10) | Yes |
| (5,3,2) | abc | (10) | Yes |
| (5,3,2) | a\|bc | (5,5) | No |
| (5,3,2) | b\|ac | (7,3) | No |
| (5,3,2) | c\|ab | (8,2) | Yes |
| (5,3,2) | a\|b\|c | (5,3,2) | No |
| (4,4,2) | abc | (10) | Yes |
| (4,4,2) | a\|bc | (6,4) | Yes |
| (4,4,2) | b\|ac | (6,4) | Yes |
| (4,4,2) | c\|ab | (8,2) | Yes |
| (4,4,2) | a\|b\|c | (4,4,2) | Yes |

Exhaustiveness follows by the number of blocks: for three labels there
is one one-block partition, three two-block partitions (specified by
their singleton), and one three-block partition. For one label there is
one partition. All eleven required labeled cases are therefore checked;
eight pass parity and three fail, with no discrepancy from the original
proof. Forgetting labels after these tests yields precisely the four
listed global degree partitions and precisely the per-local-type table.
The two assignments yielding (6,4) remain distinct before that step.

These finite checks are fully displayed, so no mathematical script or
numerical sampling is needed. Unramifiedness in L093 is imported, not
independently recomputed. No L094 discriminant input enters this audit.
The direct mathematical inputs remain L093 and L095. The result remains
REPRODUCTION of the assessed method; the audit confirms existing local
progress without establishing progress beyond the sources checked.

## Mathlib

Full matching coverage of this specialization and supporting completion
declarations: **not checked**. No absence or formal-verification claim
is made. The standard finite-étale product and number-field completion
decompositions are used as mathematical inputs as explained above.
