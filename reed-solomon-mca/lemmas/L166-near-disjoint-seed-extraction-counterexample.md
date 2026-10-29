# L166 — Counterexample to S-marked near-disjoint four-edge extraction

## Hypotheses

Use the fixed ambient parts

    S={1,8,12,18,22,27,33},
    J={47,50,64,70,75,79,85,89,96}.

The proposed implication concerns every family of m distinct four-sets,
12<=m<=14, each with two labels in each part, with pairwise intersection
size at most one and every integer coordinate degree at most four.
Isolated labels are explicitly allowed. No coding realization or
extension to sixteen actual supports is assumed.

## Conclusion

That implication does **not** force four edges with exactly one
singleton pairwise intersection in S and the other five intersections
empty. The twelve-edge family below satisfies every incidence premise
and has no such four edges. This refutes only this unconditional
extraction mechanism, not uniform twelve-row geometric exclusion or
the grand MCA challenge. It neither refutes C152a nor changes L165.

Classification: POTENTIALLY_NEW under the prior EXPLORE assessment
`drafts/literature/2026-10-26-near-disjoint-seed-extraction-review.md`.
This means that the bounded source comparison did not supply this
specific witness; no certified originality is claimed. A separate
critical audit on 2026-10-26 passes at exactly the stated incidence scope.

## Proof

Define E={A_1,...,A_12} by the following complete table. Each row denotes
the union of its displayed S pair and J pair.

| i | A_i intersection S | A_i intersection J |
|---|---|---|
| 1 | 1,12 | 47,50 |
| 2 | 1,18 | 64,70 |
| 3 | 1,22 | 75,79 |
| 4 | 1,27 | 85,89 |
| 5 | 8,12 | 79,89 |
| 6 | 8,18 | 75,85 |
| 7 | 8,22 | 47,70 |
| 8 | 8,27 | 50,64 |
| 9 | 12,22 | 64,85 |
| 10 | 12,27 | 70,75 |
| 11 | 18,22 | 50,89 |
| 12 | 18,27 | 47,79 |

Let S'=S minus {33}. The twelve S pairs are precisely all pairs of S'
except {1,8}, {12,18}, {22,27}. In particular they are distinct, each
of the six labels in S' has degree four, and 33 has degree zero.
Distinct S pairs also make all twelve four-sets distinct. The parts
are disjoint, so each row is a four-set with exactly two labels in
each part, and m=12 is within the required interval.

All displayed J pairs are distinct. Each active J label belongs to
exactly the following three rows; the corresponding three S pairs
partition S', as can be checked directly in the full table:

| J label | Row indices |
|---|---|
| 47 | 1,7,12 |
| 50 | 1,8,11 |
| 64 | 2,8,9 |
| 70 | 2,7,10 |
| 75 | 3,6,10 |
| 79 | 3,5,12 |
| 85 | 4,6,9 |
| 89 | 4,5,11 |
| 96 | none |

Thus J degrees are three for these eight active labels and zero for
96. All coordinate degrees are at most four. To check linearity, two
different rows share at most one S label because their S pairs are
distinct, and at most one J label because their J pairs are distinct.
If they share a J label, the second table says their S pairs are
disjoint. Therefore their total intersection always has size at most
one. This verifies all incidence premises without a search-completeness
claim or an imported classification theorem.

Suppose four rows had the requested pattern. Their eight incidences
with S would have exactly one coincidence, involving exactly two rows:
every other pair is disjoint and the only intersection is a singleton
in S. A third row containing that singleton would create another
nonempty pairwise intersection. Hence their S union would have exactly
8-1=7 distinct labels. But every row in E uses only S', of size six.
This contradiction proves that no four rows have the requested pattern.
One witness at m=12 suffices to refute the universal 12–14 claim; no
claim about the strengthened m=13 or m=14 cases is needed or made.

### Exact computational corroboration and scope

The short proof above is complete on the displayed finite tables.
It requires no external mathematical theorem. The bounded constructor
and independent replay additionally save the entire evidence:

```bash
python3 scripts/near-disjoint-extraction/search.py
python3 scripts/near-disjoint-extraction/verify.py
```

`scripts/near-disjoint-extraction/counterexample.json` contains all twelve
rows, all sixteen coordinate degrees, all 66 pair intersections and all
495 four-subset records. The constructor found the witness after 13
search nodes, within its 1,000,000-node bound. This is a witness search,
not an exhaustive census of families. `verification.json` in the same
directory records a separate column-based reconstruction of every
saved pair and four-subset record. Actual/required values are m=12
in [12,14], maximum degree 4<=4, zero target patterns, and maximum
four-row S-union size 6<7. Both runs report no failures. The replay
reads all relevant evidence, rather than relying on a certificate
preview. Same-step replay is not the later separate critical audit.

### Separate critical audit, 2026-10-26

The later audit transcribed both proof tables independently and checked
every original hypothesis, without importing the constructor or its
verifier. All sixteen coordinate degrees are: four at
1,8,12,18,22,27; zero at 33; three at
47,50,64,70,75,79,85,89; zero at 96. Every active J incidence triple
partitions the six active S labels. Distinct S and J pairs, together
with that partition property, exclude every possible two-coordinate
intersection. The complete saved rows, degrees, all 66 pair records,
all 495 four-subset records and the prior verification summary agree
with this independent reconstruction.

For an additional independent target test, let d_x count occurrences
of coordinate x among any four selected rows. The number of S-marked
pair intersections, counted with multiplicity, is
sum over x in S of binomial(d_x,2); the corresponding J total is defined
in the same way. For linear rows the requested pattern is equivalent
to S total one and J total zero. If the S total is one, exactly one
S multiplicity is two and all other positive S multiplicities are
one; a multiplicity at least three contributes at least three, and
two double occurrences contribute at least two. Since the total S
incidence is eight, the union then has exactly seven labels. This
proves the counting necessity without presuming the absence of target
subsets or silently discarding triple intersections. The audit's
multiplicity predicate agrees with the direct six-intersection
predicate for all 495 subsets; all fail the pattern and their maximum
S-union size is six. No search-completeness claim is involved.

```bash
python3 scripts/near-disjoint-extraction/audit_l166.py
```

The complete independent certificate is
`scripts/near-disjoint-extraction/l166-critical-audit.json`, including
all reconstructed intersections, all four-subset multiplicities and
1,091 individual checks, with an empty failure list. Actual/required
values remain m=12 in [12,14], degree 4<=4 and union bound 6<7.
The audit verifies the limited counterexample, not a stronger theorem
or a contribution beyond the bounded sources checked. The historical
13-node construction is not needed for its mathematical conclusion.

L152 and C152a are comparison inputs only, not premises: this witness
still has disjoint pairs. L165 is motivation only. No quotient maps,
field arithmetic, full weights, charts, actual events or syndrome
constraints enter this proof. An abstract incidence witness need not
extend to L086's sixteen degree-four supports or be an actual E_2
family; those stronger questions remain unresolved here. Consequently
this is an informative negative result for the specified extraction,
not a disproof of the coding problem or a new radius bound.

## Mathlib

Full matching coverage of this explicit finite counterexample:
**not checked**. Supporting finite-set and counting results:
**not checked**. No absence or formal verification is claimed. The
proof uses only the complete displayed witness and elementary set
counting; no general known theorem is reproved.
