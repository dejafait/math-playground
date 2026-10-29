# Step 539 — endpoint-only shared-spine lift (working checkpoint)

The supplied whole overview/DAG and the unchanged ready assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md` were read first.
The exact approved target is its TARGET; no source refresh or new target
assessment is needed for this bounded incidence-template test.

Main gap: uniform worst-case P versus NP is unresolved. The local gap is
a uniformly linear scalar chain in the unary F_r fourth-comparison sector.
A successful primitive could precede general F and mixed-letter work;
neither of those gaps, nor actual reception or full resources, is solved.

Targeted reads: L110 §§4,21; L115 §§1–6; L118 §§1–5;
L119 §§4–5; L120 §2; L121 §§1–4; Attempts 053–055 and history 538.
Existing notebook changes are preserved. L119's elementary-companion
restriction, L120's all-placement restriction and L121's compulsory
partial-register restriction are not imposed in this attempt.

## One specified mechanism, before calculation

For r=N=2^k and the N-edge x path G_N, retain just independent copies
of F_N G_N and G_N F_N, sharing fresh source s and sink t. Add one
2N-edge pure-x spine d_0,...,d_(2N-1),t, with constants s->d_0 and
d_N->t. Keep all operand occurrences and product connectors, renaming
internal vertices by branch. This uses two copies of each operand,
one explicit delay spine, and no partial-transform registers.

Each endpoint branch accepts P=x^N(1+x)^N; the spine accepts
x^N+x^(2N)=P on the dyadic fixture. Their F₂ sum is P. This semantic
observation is only motivation, not an accepting scalar map.
Test the common-target lift A->Q<-B with arbitrary scalar rows across
both copies and the spine, including zero rows where equations permit.
No elementary reverse companion, invertibility or unit-row condition
is imposed. In particular output-dead components may be projected away.

First specify and check complete matrices at N=4. The useful threshold
is map support plus 2g(Q)<=C*S with one universal C and S=16N+20.
If the literal lift admits maps, examine the dyadic family for forced
support before cancellation fixtures or arbitrary G. Stop this template
on a complete failed equation or a proved superlinear count; otherwise
retain a precise unfinished map and one discriminating continuation.
No full chain or support bound has yet been established.

This checkpoint preserves the construction before potentially lengthy
equation work. Full proofs, if obtained, belong in a canonical lemma;
complete finite evidence belongs under scripts/batched-incidence/.

## Completed disposition

Canonical result: `lemmas/L122-parallel-endpoint-spine-support-obstruction.md`.
The literal N=4 maps pass every boundary/transition equation; their common
target charge is 329 with S=84. For all dyadic N=2^k, however, arbitrary
A->Q maps have at least 2(3^k-2^k) forced entries. Arbitrary Q->A maps
have at least 3^k. Both restrictions allow scalar sums and zero rows.
Thus support/S is unbounded in either orientation, despite 2g(Q)<=3S.
This is a new local negative for the parallel template, not a new general
automata theorem or a failure of all endpoint-only lifts.

The script `scripts/batched-incidence/check_endpoint_spine.py` checks
complete equations/counts at N=1,2,4,8,16 and saves all graph/map data in
`scripts/batched-incidence/output-539/endpoint-spine.json`. Full N=4 input,
maps/products and forced-coordinate evidence were inspected. Its finite
expanded maps are diagnostic, not a free coefficient oracle; the symbolic
lower bound applies to every map independently of their construction.
No partial register set or polynomial edge was introduced.

Stop Attempt 056 before cancellation/general-G extension. Preserving
independent endpoint branches preserves the very prefix/residual functions
that force binomial coordinates. Any continuation through this obstruction
must change those functions, for example through actual cross-copy graph
incidences and an explicitly checked invariant-kernel projection. Such
maps are not yet supplied. Current routing and the sole next action are
recorded only in PROGRESS.md.
