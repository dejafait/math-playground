# L052 — A fifteen-support profile survives tau=1 incidence recentering

## Hypotheses

Work on the abstract label set V={0,...,15}. A tau=1 triple means
three distinct four-sets with union size nine and intersection size one.
Its uniquely distinguished pair has intersection {h,d} of size two;
the third set meets that pair's union B only at h. Define its universal
support to be the symmetric difference of the distinguished pair.
Among the other sets, a d-tag means a set meeting B exactly at d.
These are incidence definitions only, not recovery equations.

Consider the following family of fifteen four-sets. Its first three are

    A_0={10,11,12,13}, A_1={10,11,14,15}, A_2={0,1,2,10}.

The other twelve have form {tag} union S, with three triples per row:

| tag | first S | second S | third S |
| --- | --- | --- | --- |
| 12 | {1,3,4} | {2,5,6} | {7,8,9} |
| 13 | {0,5,7} | {2,3,8} | {4,6,9} |
| 14 | {0,3,9} | {1,6,7} | {4,5,8} |
| 15 | {0,6,8} | {1,5,9} | {2,4,7} |

No field labeling, parameters, error weights or syndrome pencil is
assumed. In particular V is not being identified with H.

## Conclusion

All fifteen supports are distinct. Every label has degree at most four.
Exactly one support pair has intersection size two, namely A_0,A_1;
every other pair has intersection size zero or one. Exactly one
unordered tau=1 triple occurs, namely {A_0,A_1,A_2}. For it h=10,
d=11 and B={10,...,15}; its universal support {12,13,14,15} is absent.
Its twelve other supports are nonuniversal and none is d-tagged.

For every pair meeting in two labels, every other support meets its
six-label union in at most one label. Thus this family obeys the
support-only six-coordinate affine-lift condition, coordinate-capacity
condition, and conditional two-d recentering test used in this attempt.
It shows that those incidence conditions alone cannot force twelve
nonuniversal supports to enter L051's two-d branch by choosing another
tau=1 triple. This is a negative result about that proposed implication,
not a counterexample to L043's uniform eleven target or an actual MCA
construction. No claim of originality beyond the checked sources is made.

## Proof

Put O={0,...,9}. Within each row of the table the triples are disjoint;
their omitted labels are respectively 0,1,2,3. Across all twelve triples
and W={0,1,2}, no unordered pair of O-labels repeats. This is a complete
finite check from the displayed table: the thirteen triples give 39
distinct pairs, and the six absent pairs are

    {0,4}, {1,8}, {2,9}, {3,5}, {3,6}, {3,7}.

Each triple contributes its three distinct pairs, so this check includes
all 39 occurrences, not only the six absent pairs. Equivalently, one
can list the three pairs in each of the thirteen displayed triples and
verify that none occurs in another row or in W. Hence two triples in
different rows meet in at most one label, and each meets W in at most
one label. Their explicit entries also show that all triples differ.

Two additional supports in the same row meet exactly at their common
tag, because that row's outside triples are disjoint. Two from different
rows have distinct tags and meet in at most one outside label by the
pair check. Each meets A_2 in at most one label, since it avoids 10 and
its outside triple meets W in at most one. Each meets exactly one of
A_0,A_1 at its tag and is disjoint from the other. Finally A_0,A_1 meet
at {10,11}, and both meet A_2 exactly at 10. This proves the complete
pair-intersection assertion and distinctness of the fifteen supports.

Counting the explicit entries gives degree four at every O-label except
3, which has degree three. Labels 10 and 11 have degrees three and two;
each of 12,13,14,15 has degree four (one original support and its three
tagged supports). The total is 60, as required for fifteen four-sets,
against capacity 64. Every additional support meets B once. A_2 meets
B once at 10. Because A_0,A_1 is the only pair meeting twice, these
checks prove the six-coordinate condition for every applicable pair.

For completeness any three four-sets with union nine and common
intersection of size one have pair-intersection sum four: inclusion
and exclusion gives 9=12-sum |A_i intersect A_j|+1. All three pair
intersections are nonempty; therefore their sizes are 2,1,1, with a
unique size-two pair. In this family that pair must be A_0,A_1.
A tau=1 third support must contain one of {10,11}, meet B only there,
and use three outside labels. Only A_2 has that property: the twelve
tagged supports avoid both 10 and 11. Thus the tau=1 triple is unique,
including all choices of reordering the three errors. Its third support
selects h=10 and d=11. Its symmetric difference is absent, and all
twelve additional supports meet B in one of {12,13,14,15}. The
nonuniversal count is twelve and its d-tag count is zero, below the two
required for the conditional exclusion. This completes the proof.

The supplementary exact search is reproduced by
`python3 scripts/simultaneous-recovery/recenter_incidence.py` and saves
`scripts/simultaneous-recovery/recenter-incidence-result.json`.
It searches a restricted disjoint-triple-class construction; its negative
search branch is not a general nonexistence theorem. The conclusion
above uses the displayed positive witness only. The independent check
`python3 scripts/simultaneous-recovery/verify_recenter_incidence.py`
reads that witness and explicitly checks all 105 pairs and all 455
unordered triples, saving
`scripts/simultaneous-recovery/recenter-incidence-verification.json`.
It finds pair-intersection counts 21,83,1 at sizes 0,1,2, respectively;
the only tau=1 triple is the one proved above, and all triple unions
have size at least nine. It reports no failures. The complete relevant
certificate values were inspected, not only previews.

### Scope of the recentering application

This paragraph explains relevance rather than supplying mathematical
inputs to the abstract construction. For an actual twelve-candidate
pencil, L043's relaxed converse and L010's weighted bound give at least
fifteen finite sparse parameters, excluding every lower-weight error.
At a tau=1 triple of those actual errors, L041 gives its nonzero
shortened-kernel coefficient and all normalized triple gates; L042–L043
then apply in the unchanged original finite chart. In a chosen family
of m actual errors, removing its three base errors and an occurring
universal error leaves m-3-u nonuniversal parameters, where u is zero
or one. For m=15 this is twelve only if u=0, and eleven if u=1.
For m=16 it is at least twelve in either case. L051 needs at least two
distinct d-tag parameters as well. A support-only argument must track
both conditions, rather than assert preservation of twelve under every
recentering. L052's family has m=15 and u=0 but lacks the second condition
at its only available triple. The actual recovery equations could still
exclude every fixed-H labeling of this family; none is tested here.

## Mathlib

Full matching coverage and supporting finite-set results: not checked.
No absence claim is made. The proof is the explicit finite construction
and complete incidence verification above, with no imported theorem
or standard result reproved.
