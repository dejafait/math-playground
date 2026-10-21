# Lower-threshold postspell calculation

The ready SPECIALIZE assessment
`drafts/literature/2026-10-04-sharp-postspell-final-halving.md`
matches the exact target invoked for this research turn and is preserved
unchanged. No further literature search was needed. The calculation
reproduces inspected affine and parity machinery, then specializes the
original-root inequality below the source's sufficient threshold.

The gap is universal descent at the hypothetical least nonconvergent
residue-20 root. The intermediate target is a sharp guarded single-word
criterion below e(J,H), with possible downstream use as a stricter
necessary tail bound. The discriminating test was an actual descending
lower-tail excursion, retaining residue, all input parities and positive
offsets. Neither all-root prefix entry nor control of later compensation
was a prerequisite or a conclusion. L019 already covers a>=J+H;
L005's complete-block words have different conventions. No stopped
bounded-window, ancestor-cover or paired-invariant route was reopened.

[L020](../lemmas/L020-sharp-postspell-descent-and-lower-halving-bound.md)
records the full proof. With its A,C,D, descent is exactly
(2^D-A)n>C. For fixed parameters, actual descending residue-20
realizations exist if and only if 2^D>A; the first positive CRT root
need not descend unless the positive offset is also paid. In the saved
rectangle, the ten a=20 cases all satisfy 2^D-A>C, so every positive
actual root descends. At a least root this gives v_2(z)<20 instead of
the previous v_2(z)<38. All 110 a=2 triples have 2^D<A and are ruled
out as descending excursions for every positive root.

The explicit J=11,H=10 family in L020 has exactly twenty final halvings,
fits the older L014–L018 arithmetic restrictions, and satisfies the
weaker L019 bound for that prefix. Thus the strengthening changes a
real conditional exclusion, rather than merely improving an asymptotic
slope in an unrealizable word. It does not assert that any test start
is bad, or that older prefix bounds at other times are all satisfied.

Reproduction command from this directory:

```bash
python3 scripts/sharp-postspell/check_sharp.py
```

The saved `scripts/sharp-postspell/result.json` reports PASS for 120
parameter triples, 360 exact CRT replays, ten uniformly descending
lower-tail triples, and three members of the exact-tail witness family.
The program compares a branch-composed offset with the closed formula,
checks each input parity and residue, and retains the strict inequality.
Finite checking supports transcription and the witness; the all-root
claims follow from L020's inequalities and the cited coding theorem.

Outcome: ADVANCE, classification REPRODUCTION. This is relevant local
progress from a sufficient threshold to exact guarded arithmetic and a
stronger conditional bound, without a claim beyond the checked
literature. No complete candidate appears. The remaining cases can
still grow: the a=2 obstruction persists. Further enlarging this finite
rectangle would not establish entry or a global progress measure.
The proposed next direction is original-root compensation across two
actual residue-20 excursions, allowing the first to grow and the second
to contract. That changed concatenation scope has a pending assessment;
no derivation of it is attempted in this turn. Historical route stops
and exploration counters are preserved.
