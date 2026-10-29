# Critical audit of the fixed split-isogeny specialization

2026-10-26, step 511. The pre-existing SPECIALIZE gate is
`literature/2026-10-26-marked-split-isogeny-kernel-audit.md`.
This is a bounded conceptual proof audit of L142, not a new descent.

The main gap is point control for the residual primitive Beal systems.
The intermediate target is correctness of L142's two embedded finite
Q-Galois kernels, G's normalization, and its exact same-T redundancy
claim. These can support a separately assessed joint descent on quotient
classes. Accept only if the branch-module identifications, actual norm
maps, rational Abel basepoint, and all rational exceptional fibers hold;
otherwise record the precise correction. No improved rank bound or
point sufficiency is presumed.

Starting inputs are L110, L111, L113, L127 and L138. The saved source
comparison supplies Docking Lemmas 4.1/5.3 and Proposition 5.4 Case II,
Bruin Proposition 2.2, and Schaefer Section 2. ATTEMPTS/062 supplies
the narrow stopped shortcut. Existing changes are preserved, including
unfinished L108; no cross-notebook input is used.

Checkpoint before detailed verification: the potential pitfalls are
confusing the two three-dimensional permutation modules, replacing
the quartic fiber class by 2O_E, using F's connecting map on G's target,
or assuming that a rational Jacobian lift is a curve point. The audit
will check the actual divisor embeddings and involution identities.
Full mixed descent, local/global images, and Beal recovery remain open.

## Completed audit

The complete verification is canonical in
[L142](../lemmas/L142-marked-split-isogeny-kernels.md), under
“Separate critical instance audit — 2026-10-26”. It accepts the two
embedded kernels, their Q-action, G's two norm coordinates, the rational
basepoint and every rational same-T exception, without a correction.
The reverse-kernel size was also checked against deg([2])=64 and
deg(F)=8, rather than relying only on a list of candidate generators.
The check is finite and conceptual; no mathematical script was used.

This is ADVANCE only as completion of the independent verification of
a relevant existing input, classified REPRODUCTION. It is not progress
beyond the cited kernel theory and gives no rank gain. The bound remains
rank Jac(B)(Q)<=7+c<=9 against the sufficient bound one. The old exact
same-T shortcut stays stopped in ATTEMPTS/062. No correction to the
argument or direct inputs was needed, so PROOF.md and DAG.md are
unchanged. The prospective audit sentence in PROOF.md is superseded by
this completed canonical audit and the current checkpoint.

The next proposed target concerns representation of G-connecting
classes by quartic square classes on weaker class data. That scope was
expressly excluded from the current assessment. Its new assessment is
REVIEW_REQUIRED: no cohomological lifting criterion or representability
claim has been proved or approved in this turn. A creative mixed
exclusion is not yet justified because both faithful representation and
nonredundancy against separate quotient conditions are unresolved.
