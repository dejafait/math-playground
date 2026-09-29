# Paired-state transition test, 2026-09-27

## Scope and decision test

The saved SPECIALIZE assessment in
[the prior review](literature/2026-09-26-current-target.md) covers this
exact target. The shared rules, local goal and checkpoint, whole overview,
DAG, relevant L002/L010/L011 proofs, earlier screen, and recorded failures
were read before calculation. Existing unfinished literature work is
preserved. Standard inverse arithmetic and the coalescence identity are
imported as documented there; the remaining test couples the block-depth
offset with both original starting thresholds.

Universal eventual descent is still the main gap. The intermediate target
is whether the pair z=4y+1 at indices r-2 and r-1 can have compatible
earlier histories that each stay above their own start. An invariant
preserving those thresholds could support restricted suffix rigidity.
An admissible pair violating rigidity would stop that repair. Even a
positive answer would leave fixed-start depth bounds and other block
types unresolved. A larger finite screen alone is not the desired result.

## Reasoning saved before the main test

Write the two starting thresholds as A_0 and B_0 and retain the full
tails from L011. In a simultaneous backward step the state indices
remain one apart. When the earlier coordinate reaches index zero, the
other coordinate still requires one inverse to reach its own start.

From z=4y+1 with y=1 modulo 3, the predecessor of z is
H(z)=(32y+7)/3. If 9 divides 2y+1, this predecessor is divisible by 3
and cannot have a preceding allowed block. Thus at a first merge with
r>=4 the only predecessor of y is v=(4y-1)/3, giving H(z)=8v+5.
Both histories require a predecessor of v, so v cannot be 0 modulo 3.
These are preliminary arithmetic observations; the main test must still
track positivity, exact block types, and every original-threshold
inequality. No all-depth implication or complete candidate is asserted.

The planned computation specializes the existing exact affine-word
machinery to this pair. It will use integer congruences and inequalities,
and independently check any decisive witness by shortcut iteration.

## Completed calculation

[L012](../lemmas/L012-paired-backward-transitions.md) proves the additional
forced companion block, the five inverse choices at (8v+5,v), and the
general affine transition and interval test. The two starts remain
independent. When simultaneous reversal reaches the earlier history's
start, the companion history still needs one inverse. Forgetting this
last inverse would test histories of unequal depth.

The [paired checker](../scripts/paired-state/check_pairs.py) starts from
the exact two tail families in L011, solves both inverse congruences,
and retains every endpoint inequality relative to its own start. Its
[saved output](../scripts/paired-state/result.json) records:

| Depth | Coupled classes before the extra inverse | Equal-depth classes tested | Surviving non-descending pairs |
| --- | ---: | ---: | ---: |
| 2 | 2 | 6 | 0 |
| 3 | 6 | 24 | 0 |
| 4 | 10 | 32 | 0 |
| 5 | 44 | 118 | 0 |
| 6 | 204 | 614 | 0 |
| 7 | 784 | 2,040 | 0 |
| 8 | 2,324 | 6,010 | 0 |
| 9 | 8,342 | 20,702 | 0 |
| 10 | 25,064 | 62,682 | 0 |
| 11 | 82,510 | 196,468 | 0 |

The checker independently iterates all 17,688 selected class realizations
through depth eight, plus 154 realizations of the five-row transition
table. Each class test covers its complete nonnegative integer parameter
range by exact inequalities; the independent forward realizations check
the implementation only. There is no endpoint-height cutoff.

An initial run reached depth 11 and hit the 250,000-node limit while
constructing depth 12. The saved command deliberately ends at completed
depth 11. No result is inferred about a partially constructed depth.

An auxiliary diagnostic reused the earlier `classify` and `overlap`
functions, appending each of the four letters only to nonempty
non-descending prefix classes. It completed depths 7–12 with respectively
1,658; 5,505; 18,801; 66,675; 232,267; and 834,821 admitted word classes,
and found no distinct-suffix overlap. Prefix pruning is justified because
a violation relative to the initial value persists in every longer
history. This in-memory traversal was interrupted while preparing depth
13; no conclusion uses its unfinished work. It was a diagnostic for
choosing the more explicit paired calculation and supplies no all-depth
claim. The archived checker above is the step's reproducible test.

## Assessment and route decision

The arithmetic rules are a reproduction/specialization of the inverse
machinery screened in the prior review. They expose another necessary
contraction but do not give the required bound on earlier compensation.
The sought all-depth invariant, a reduction preserving both starting
thresholds, and an admissible counterexample all remain missing. The
achieved finite depths do not meet that threshold. No candidate proof
or disproof of Collatz appeared.

Outcome: EXPLORATION. Two consecutive exploration turns have now been
used, counting the prior literature review. Increasing the search depth
would retain the same unresolved passage and rapidly growing class
count, so that continuation is stopped. The alternative to screen is a
linear invariant in the paired states and their suffix minima. This
would retain information about earlier contractions and has a possible
route to an estimate valid at every depth. No such invariant is assumed
or derived here. Its changed target has a REVIEW_REQUIRED assessment;
the third exploration turn must complete the assessment and a
continuation/stop decision. The exact current action is in PROGRESS.md.

## Mathlib

Full paired-state statement and supporting library results: **not
checked**. L012 contains the full elementary specialization proof and
retains Rozier's named supporting results and direct link. The prior
assessment records the distinction from the missing two-start descent
theorem. No claim of novelty or absence from Mathlib is made.
