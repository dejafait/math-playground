# L099 — Fixed-H independent-net pair obstruction

## Hypotheses

Let F=F_(97^20) and let H be the order-sixteen subgroup of F_97^*:

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96}.

Use the triangle notation and both-zero projected support definition of
L065. In particular P={a,b,c}, the three singleton pairs Y_0,Z_0,W_0
are disjoint, their union S_0 has six labels, all nine labels are
distinct, and V=H minus (P union S_0) has seven labels. Assume the
three monic quadratics Y_2,Z_2,W_2 with these respective root pairs are
linearly independent. For the approved recovery target, normalized
weights are rational and gated as in L059; the projected obstruction
below does not use weights, parameters or full-weight gates.

## Conclusion

There are no two distinct both-zero projected supports K,L contained
entirely in V. Consequently two entirely-V both-zero supports cannot
have simultaneous full-weight recoveries at distinct eligible scalars
under the approved hypotheses, in any admissible original finite chart.

This is a fixed-H result with explicit dependence on the complete exact
finite certificates below. It sharpens L065's upper bound of two projected
entirely-V supports to one for independent pair quadratics at this H.
It proves no bound on isolated recoveries, no uniform triangle twelve
bound and no challenge resolution. Its separate critical audit on
2026-10-17 found no mathematical defect in this scope.

## Proof

### Exact finite predicate imported from L065

Import L065's equivalence: a four-subset K disjoint from P is both-zero
if and only if its monic quartic f_K belongs to the net

    N=span{Z_2 W_2, Y_2 W_2, Y_2 Z_2}.

L065 supplies the full interpolation proof, including cancellations and
the distinction between projected membership and restored recovery.
No recurrence, shortening or distance theorem is reproved here. The
primary inputs to that classification remain the precise Hall,
Marquez-Corbella–Pellikaan and Chojecki citations recorded in L065; the
present additional input is the fixed-H finite calculation.

The net depends only on the unordered partition of S_0 into its three
pairs. Permuting pair names or swapping roots within a pair leaves it
unchanged. Thus it suffices to examine all C(16,6)*15=120,120 unordered
partitions of six H labels into three pairs. The shared labels P can
be postponed: a candidate quartic entirely in V has its four roots in
the ten-label set H minus S_0. If two such quartics belong to the same
V, the union of their distinct root supports has size at most seven.

Subgroup scaling is the only label symmetry used. For h in H, replace
every root x by hx. For a monic polynomial f of degree d this sends
f(X) to h^d f(X/h). It preserves independence of the three quadratics,
membership in their product net, distinctness and support union sizes.
Every scaling orbit has a representative whose least label is 1: scale
any singleton label to 1. The lexicographically least scaled partition
must have that property. The least of the six partitions obtained by
scaling each singleton root to 1 is therefore an exact canonical
representative of the orbit. No projective transformation or arbitrary
permutation of H labels is assumed to preserve moments.

### Complete producer and independent coefficient replay

Reproduce from this notebook directory:

```bash
python3 scripts/triangle-recovery/independent_net_pair.py
python3 scripts/triangle-recovery/verify_independent_net_pair.py
```

The producer saves every representative's quadratic determinant and all
210 lexicographically ordered four-subsets of its ten-label complement,
with all three six-singleton evaluation residuals. Its complete artifact
is `scripts/triangle-recovery/independent-net-pair.json`. The initial
8,000-representative cap is not reached: enumeration finishes all 7,532
representatives. Negative conclusions here rely on the complete replay,
not on this cap or the original survivor-only output.

The separate verifier imports no producer functions. It explicitly
generates all 120,120 raw partitions, normalizes each by its six singleton
roots and checks equality of the entire representative set against the
producer. It checks quadratic independence by Gaussian elimination,
rather than the producer's determinant expression. The orbit histogram
is 7,483 orbits of size sixteen and 49 of size eight; indeed
7,483*16+49*8=120,120. There are 7,420 independent representatives and
112 dependent ones; only the independent ones are in this conclusion.

For each independent representative the verifier constructs the three
product polynomials n_0=Z_2W_2, n_1=Y_2W_2, n_2=Y_2Z_2 explicitly by
coefficient multiplication. If y,z,w are one chosen root from each
respective pair, define, for every tested quartic f,

    A=f(y)/n_0(y), B=f(z)/n_1(z), C=f(w)/n_2(w).

All denominators are nonzero because the six roots are distinct.
Evaluation at y kills n_1,n_2; evaluation at z kills n_0,n_2; evaluation
at w kills n_0,n_1. Thus any representation of f in N has exactly these
coefficients. Membership is equivalent to all five coefficients of
f-A n_0-B n_1-C n_2 vanishing. This test is exact, not a numerical
approximation. It also shows that allowing coefficients in F rather
than F_97 does not introduce more members with prime-field f.

For all 7,420*210=1,558,200 quartics, the verifier saves these three
coefficients and all five coefficient residuals. It also recomputes all
producer evaluation residuals, checks every residual row and confirms
agreement of the coefficient and evaluation membership tests. The full
replay is `scripts/triangle-recovery/independent-net-pair-verification.json`;
`support_row_encoding` specifies the lexicographic root-support order
and `[net coefficients, five coefficient residuals]` row format.

The complete counts are:

| Number of candidate quartics | Independent representatives |
| --- | ---: |
| 0 | 7,267 |
| 1 | 152 |
| 2 | 1 |

There are 154 retained support occurrences altogether. Of the 1,558,046
rejected quartics, 1,542,100 have a nonzero constant residual coefficient
and the other 15,946 have their first nonzero residual at degree one.
The only representative with two candidates is

    Y_0={1,22}, Z_0={33,64}, W_0={75,96}.

Its complete candidate list is

    K={8,18,79,89}, L={12,27,70,85}.

These supports are disjoint, with union size eight. The verifier checks
every pair of retained supports; its full pair-union histogram consists
of exactly this one size-eight union, and zero unions of size at most
seven. Both complete failure arrays are empty. The summary, complete
failure array and entire two-candidate list were inspected, alongside
execution of the verifier on every relevant row. A bounded preview is
not used as evidence of completeness.

### Transfer to the approved recovery target and limitations

If distinct entirely-V both-zero supports K,L existed, L065 would put
both quartics in the net. Scaling to the canonical singleton partition
would preserve net membership and their union size at most seven. The
complete calculation above excludes precisely this event. This proves
the conclusion.

No actual recovery pair was constructed or tested after restoration:
the projected obstruction already rejects every possible pair under
these hypotheses. Consequently zero fourth weights, singular restored
matrices, rational scalar gates, distinctness of scalars and original
infinity exclusions cannot rescue such a pair. This argument does not
drop those gates to assert existence; it proves nonexistence before
them. It assumes neither |M|=13 nor equality-only L086/L098. Dependent
quadratics are explicitly outside the result, and no bound on their
projected candidates is inferred. The computation is specific to this
H and must not be generalized to other smooth domains or characteristics.

The two programs use different partition generation and membership
tests but share Python integer arithmetic and the fixed prime field;
this is not a formal verification. The separate audit below retains
this shared-arithmetic limitation. The
ready EXPLORE assessment is
`drafts/literature/2026-10-16-independent-net-two-recovery-attainability.md`.
The result is local progress beyond the conclusions recorded in that
assessment, without a certified originality claim. No full recovery
count, global error improvement or challenge qualification is supplied.

### Separate critical audit (2026-10-17, step 265)

The audit read this entire proof, L065 including its canonical audit,
and both complete programs. It reused the approved source comparison in
`drafts/literature/2026-10-16-independent-net-pair-critical-audit.md`.
The sole direct mathematical input remains L065's exact projected net
classification. Its interpolation proof and nonzero singleton pivots
apply without equality, rational weights or a rational original chart.
No new recurrence, shortening or distance theorem is imported or reproved.

**Complete reduction and extension fields.** Every singleton partition
has six distinct roots and three unordered pairs. Root swaps and pair
permutations preserve precisely the span being tested; this does not
assert symmetry of any restored-weight equations. For h in H, the
invertible coefficient map f(X) -> h^d f(X/h) on degree-at-most-d
polynomials sends each monic pair quadratic to its scaled-root quadratic.
For d=4 it sends each product to the corresponding product, so preserves
membership; for d=2 it preserves quadratic independence. Labels remain
in H, and all support cardinalities and intersections are unchanged.

Canonical partitions are sorted internally and then sorted by pairs.
Their first entry is the least root. Since residues are represented by
1,...,96, an orbit minimum must contain 1: scaling any root to 1 gives
a partition lexicographically smaller than every partition without 1.
The scalings that produce 1 are exactly the inverses of the six roots.
Thus the producer's minimum over all sixteen scalings and the verifier's
minimum over six inverse-root scalings agree, including nontrivial
stabilizers. Neither assumes all orbits have size sixteen.

The producer's recursive matching generator chooses the mate of the
least remaining root at each stage. The verifier chooses the first mate
in five ways, then the mate of the least of the four remaining roots in
three ways; the last pair is forced. Each produces every unordered
matching exactly once. Enumerating all six-subsets therefore gives
binom(16,6)*15=120120 distinct raw partitions. The full set equality
against the producer, not just the cardinality, checks orbit coverage.
The replay's orbit sizes sum to 7483*16+49*8=120120.

In the membership test, evaluation at the first root of each pair kills
two product polynomials and leaves the third nonzero. The coefficient
vector is therefore forced over any extension field. Since the quartic
and all pivots lie in F_97, that vector lies in F_97. Every residual
coefficient is tested, in ascending degree order from zero through four.
The separate six-node barycentric test uses S'(x) as denominator; all
its factors are nonzero. L065's interpolation identity proves equivalence
of its three pair sums with net membership. Thus the coefficient and
evaluation tests agree mathematically, as well as on every executed row.
Gaussian elimination independently checks each quadratic independence
flag. Rank below two is impossible for distinct monic quadratics with
disjoint root pairs; the 112 rank-two representatives are outside the
stated conclusion, not silently rejected independent cases.

**Complete execution and artifact comparison.** Both reproduction
commands above were run to successful exit without optimization disabling
Python assertions. The producer completed 7532 representatives below its
8000 cap, found no witness and executed no restored-weight branch.
Its unused L064-related weight helpers and the restriction to union size
exactly seven in that branch are not proof inputs. The verifier separately
checks every retained support pair and excludes every union of size at
most seven, covering smaller unions as well.

The verifier regenerated all 1558200 quartics, all three evaluation
residuals and all five coefficient residuals per quartic, and compared
every producer row, including rejected rows. It checked the complete
retained-support table and every retained pair. All counts in the proof
were reproduced: 7267 empty candidate lists, 152 singleton lists and one
two-support list, hence 154 retained occurrences. Rejections total
1542100+15946=1558046. The entire two-support list and its sole size-eight
union were inspected. Both complete failure arrays are empty; the
success verdict relies on completed assertions and mathematical review,
not on those arrays being initialized empty.

Pre-replay SHA-256 hashes and sizes were saved in
`drafts/2026-10-17-independent-net-pair-audit-before.json`. Both programs
and both complete regenerated certificates match those hashes and sizes
exactly. The additional audit record
`scripts/triangle-recovery/independent-net-pair-critical-audit.json`
retains the comparisons, complete summary and entire exceptional pair.
It also checks the literal H against the producer, multiplicative closure
and inverses, all producer counters, the 112 dependent representatives,
and the sum of raw orbit sizes. This record supplements the full replay;
a bounded JSON preview is not the evidence for unchecked rows.

**Transfer and verdict.** For any original shared triple P, two entirely-V
supports have union at most seven. Scaling carries them into the complete
candidate table for the scaled singleton partition with the same union
size. The sole possible candidate pair instead has union eight, which
leaves only two of the ten complement labels for P. Three distinct shared
labels cannot be chosen. This is a necessary-condition exclusion before
any weight or finite-chart gate; dropping those gates is never used to
assert existence. L065's existing uniqueness of an eligible scalar per
both-zero support remains available when using the support bound in a
parameter count, but no further parameter bound is derived in this audit.

No theorem, program, numerical bound or direct dependency required repair.
The audit validates the existing computational input; it does not add a
stronger theorem or claim originality. The two execution paths share
Python integer arithmetic and the fixed field, with no formal certificate
checker. The uniform triangle count, isolated-recovery interaction and
challenge qualifications remain unresolved. This canonical verdict
supersedes older pending-audit prose in the unchanged overview.

## Mathlib

The full matching fixed-H finite obstruction and its computational
certificates are **not checked** in Mathlib. Polynomial interpolation,
finite-field linear algebra and the underlying L065 classification are
supporting inputs, with coverage qualifications retained there. No
absence claim, Lean verification or formal certificate checker is claimed.
