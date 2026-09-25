# 2026-09-25 — Fixed-slack differential interpolation

Read the required instructions, whole overview, DAG, existing changes,
relevant proofs, and the recorded failed transfer. Preserved unfinished
work and rechecked the prize statement and September 5 TR26-169 source.
The [focused audit](../drafts/2026-09-25-fixed-slack-interpolation.md)
saved the proposed rank comparison before completing the proof.

[L006](../lemmas/L006-fixed-slack-differential-interpolation.md) supplies
the missing interpolant with order and total derivative-variable degree
constant at fixed slack and X-degree O_gamma(n). It proves the fixed-shape
rank estimate directly, including padding, rounding, arbitrary
characteristic, and the degree/multiplicity step. The source's optimized
derivative order was unnecessary for this test.

[C006a](../lemmas/C006a-fixed-slack-list-certificate.md) assembles the
resulting polynomial list bound in large characteristic and its explicit
sufficient field condition. It handles k-1<r separately. This is ADVANCE;
exploration turns are 0/3. The fixed-slack interpolation gap is removed,
but the required sharp boundary under the weaker field-existence proviso
remains open. STATUS stays IN_PROGRESS, with no complete target candidate.

The proof includes exact checks of the local cutoff, vanishing binomial
coefficients, padding ceilings, and the closed-ball floor identity.
No sampling or algebraic-computation script was needed. The proof overview
and source qualification now reflect the established partial certificate.
The new DAG inputs were reviewed against the actual proofs.

Because interpolation works over every field while the cover fails on
large Frobenius solution spaces, the next direction tests agreement
filtering on that concrete obstruction. Further optimization of the
already adequate fixed-slack rank estimate would not address that gap.

The required
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with seven nodes and five edges, with bytecode writes disabled to
keep shared infrastructure read-only. Its first run treated raw Hasse
notation as Markdown links; formatting those expressions as mathematics
resolved the documentation errors. `git diff --check -- .` passed.
Structural validation does not certify mathematical correctness.
