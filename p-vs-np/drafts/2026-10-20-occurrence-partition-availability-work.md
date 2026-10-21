# Occurrence-partition availability work — step 369

Approved target: test the exact L087 occurrence pairs against L094's
oriented-block cutoff. Prior SPECIALIZE coverage is
`drafts/literature/2026-10-20-occurrence-pair-oriented-block-availability.md`.
No renewed source discovery is needed. Attempts 018/030 remain separate.

Main gap: unrestricted SAT decision/separation. Intermediate target:
availability of the supplied logarithmic oriented partition. A positive
result could connect L094 to L087's conditional burden; a negative family
would stop this availability route, without obstructing other witnesses.

Saved candidate, not yet established: take two runs of positive unit
clauses (x_1),...,(x_n), then opposing units (z),(NOT z), and apply L087's
unchanged appended u/v gadget and stable occurrence grouping. Every old
variable occurs exactly twice. Within either x-run, consecutive occurrence
names are first copies of distinct groups, or second copies of distinct
groups. Their positions in the grouped order have equal parity and are
distinct, so cannot be adjacent, even allowing reversal. This suggests
2(n-1) forced cuts and at least 2n-1 blocks. Must finish the partition
argument, unsatisfiability/endpoint reception and a concrete complete
original-M encoding bound before recording a result.

Continue if the complete encoding grows polynomially in n and these
forced cuts exceed floor(log₂ M) for an explicit infinite range. Abandon
this candidate if stable grouping, copy identity or full encoding defeats
that comparison. L094's supplier itself and the independent representation
and SAT gaps are not being tested. No witness availability is assumed.

## Completed attempt

L095 now contains the complete forced-cut proof, exact unsatisfiable
family with q=2n+6 occurrences, retained gadget, dense tester reception
and a concrete full original record encoding. Its all-size comparison is
b>=2n-1 versus M<2^16(n+2)^3, with strict failure for n=2^t, t>=6.
No mathematical script or finite calculation is required for this analytic
argument. The original candidate checkpoint above is retained as unfinished
reasoning saved before completion; it is not the current proof record.

Outcome NEGATIVE for universal partition availability, using known unsigned
adjacency reasoning with local occurrence/encoding specialization. Stop
that availability route in Attempt 031, subject to separate critical audit.
There is no claim of a new general theorem, certified originality, witness
hardness or a P versus NP resolution. Full proof/citations and unknown
Mathlib coverage are canonical in L095. Its only direct mathematical input
is L087; L094 is the application whose promise is being tested, not an
input witness construction. Attempts 018/030 and all prior work remain.
