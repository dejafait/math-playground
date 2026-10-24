# Step 408 — uniform all-order assembly working note

The approved target is to assemble L094 with C093a for d=6,...,33.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-22-uniform-all-order-real-exclusion-assembly.md`.
Completed startup comparison: read both full canonical statements/proofs
and completed audits, L055's complete table, C089a's normalization and
strict-guard audit, and Attempt 032. The same d, full integer simplex,
lower domain, endpoints and non-strict J guards match. No numerical
rerun or upstream theorem reproof is warranted.

Planned proof: drop only H for L094, use only its rotation conclusion,
choose the unique original position z carrying indexed row0, and put
rho_i=(z+i) mod25, x_i=s_(rho_i), x_25=x_0. Show pi(rho_i)=i;
the cyclic successor identity transports every endpoint, including
old closing edge i=24-z and new closing edge old k=(z-1) mod25.
Both guard operands then match by equality, preserving strict H.
The indexed b_i are unchanged, not permuted as chronological entries.
Invoke C093a only after the entire normalized hypothesis set matches.

Continue if this occurrence bijection covers all 25 edges and both
own-input guard signs; otherwise narrow or reassess before reliance.
No minimum/seed, integer junction, primitive count, realization or
failed full C077a premise is available. Actual-word transfer and
universal eventual descent remain independent. The likely downstream
use is a later separately assessed actual-word exclusion.

This note saves unfinished reasoning, not an audit verdict or theorem.
