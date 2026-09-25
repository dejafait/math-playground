# 2026-09-24 — Cyclotomic characteristic specialization audit

Preserved the existing local edits, the finite-descent obstruction, and
changes outside this notebook. Rechecked the Clay page and Wiles statement;
the recorded rank-assertion scope is unchanged. The
[saved draft](../drafts/2026-09-24-iwasawa-specialization-audit.md) states the
gap, intermediate target, downstream use, and discriminating test before
the proof was completed.

The test examined the checkpoint's proposed passage from characteristic
order to base-field Selmer dimension under good-ordinary control. The
[arithmetic sources](../foundations/03-cyclotomic-control.md) supply control
and cotorsion, while explicitly distinguishing complete reducibility. This
is an audit of a standard issue, not a claim of a new general theorem.

[L002](../lemmas/L002-characteristic-order-specialization-defect.md) proves
the exact specialization defect and combines it with the base Kummer
sequence. Matching characteristic ideals admit different even specialized
dimensions, including with exact abstract control. Thus the achieved bound
is rank <= Selmer corank <= characteristic order; the required equality
still needs both defects to vanish and a separate analytic-order comparison.
No elliptic-curve realization of the model examples is claimed.

Decision: stop the characteristic-ideal-only exact-rank inference, preserving
its [failure record](../ATTEMPTS/002-characteristic-order-rank-inference.md)
and useful upper bound. The main BSD gap is not closed. The reason to turn
to arithmetic heights is now precise: a height criterion could control
the invariant-to-coinvariant map and hence the module defect, which scalar
characteristic data cannot determine. This does not assume either height
nondegeneracy or finite Sha.

The proof was checked by localizing at (T), identifying the residue field
and specialized quotient, computing both explicit modules, and checking
the direction of the dual control map and the direct-limit Kummer maps.
Finite control errors vanish only after tensoring with Q_p. No numerical
or elliptic-curve computations were needed. The Kummer calculation uses
the standard exact sequence directly; finite-tower countermodels play no
role in its proof. The DAG retains both nodes.

The documentation checker passed with two nodes and no edges using
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`.
The whitespace check also passed. Structural validation does not verify
the mathematical argument.

Completed step BSD-2026-09-24-002-iwasawa-specialization-audit is NEGATIVE.
Exploration turns without an advance or informative negative result remain
0 of 3. There is no candidate proof or disproof of the main target.
