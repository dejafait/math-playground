# Frozen five-node calculation2204: working checkpoint

Gate: reuse the supplied step2203 SPECIALIZE assessment, whose covered
target is the exact frozen five-node calculation. No new source work.
Main gap: actual-Xi all-degree algebraic mixed positivity L030-L032/C032a.
Target: all integer shifts r>=4 at degree2, versus one negative prescribed
cubic-times-monomial witness with 4<=r<=1000. Success obstructs a generic
inference from this restricted family; it does not realize the model in Xi.

Inputs: C919e after the explicit checks 57/4 in [14,29/2], 21 in
[41/2,43/2], 25 in [49/2,51/2]. Use the finite algebraic normalization
of L030, not its actual-Xi hypotheses. Both conjugate representatives
occur once; no zeta census, theta signs or Decimal contract is imported.

Planned bound, not yet established: D=diag(1,200,40000), b=4/2601,
h4=b^8/700000000 from C919e; bound both complex terms at Re alpha=101
by t4=2*101^(-20)*(1+40000/101^4+1600000000/101^8).
Check h4>t4 exactly; extend using the ratio 101^(-4)/b^2<1.
Then form P from the three real beta nodes and search the frozen integer
range using rational-complex algebraic squares. Correct CPython integer
and Fraction arithmetic is an explicit computational assumption.

Stop on an exact failed condition, exhaustion, or failure of this bound;
the latter is inconclusive about positivity. Do not move nodes, enlarge
the range or change the witness. Preserve full exact evidence on disk.
Actual-Xi realization, shift removal and all-degree signs remain open.

Completed2204: both frozen conditions pass under the stated arithmetic
assumption. Canonical proof is C919i; exact certificate is
`scripts/h2-head/five_node_2204.json`. The witness exponent is158.
The pre-calculation plan above is preserved as working history, not an
additional proof. Independent critical audit remains pending.
