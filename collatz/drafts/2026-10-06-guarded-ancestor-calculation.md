# Guarded ancestor calculation — working record

Approved target: every positive n=290 modulo 729 with actual
W(2,3)=(OOEO)^2 O^3 E^2 and an odd endpoint has a positive
p=20 modulo 27, p<n, with T^t(p)=n for 1<=t<=12.
Coverage at invocation: SPECIALIZE in
`drafts/literature/2026-10-06-guarded-residue290-ancestor-cover.md`.

Main gap: universal eventual descent. A cover could exclude this guarded
subclass at the fixed least residue-20 root by L014. Other cylinders,
prefix entry and compensation remain independent gaps. The target has
no least-root assumption and no assertion of nonemptiness.

Plan: import finite parity coding from L020 and inverse semantics from
Sodelin, L4 sections 1–5 as cited in the assessment. Impose the endpoint
bit as well as every W input bit, intersect by CRT with the ternary
cylinder, and enumerate all legal positive inverse branches through
depth twelve at each tested root. Preserve every affine offset through
integer arithmetic. Stop at a fully guarded uncovered root; do not
increase the horizon. A screen without a complete tree is unfinished.

Completed: [L030](../lemmas/L030-guarded-residue290-depth12-cover-refutation.md)
gives the fully guarded uncovered root n=3616859, with actual odd
endpoint 8690267. The complete positive inverse tree through twelve
steps has seven residue-20 hits, all larger than the original root.
Its only below-root endpoints have residues 4, 14 and 9 modulo 27.
The required cover is therefore false at its stated horizon; stop
this exact cover. There is no horizon enlargement or Collatz disproof.

Full arithmetic certificate:
`scripts/guarded-ancestor/depth12_certificate.json`.
Reproduce with `python3 scripts/guarded-ancestor/check_depth12.py`.
Complete relevant values were inspected with the shared JSON inspector
at `/witness/tree/level_values`, `/witness/forward_states`, `/coding`,
`/witness/tree/residue20_hits` and `/witness/tree/below_root_nodes`,
using `--full` for each selected load-bearing field.

Classification: RESEARCH / NEGATIVE / REPRODUCTION; actual task:
calculation. This is local finite evidence from specialized known
machinery, not a claim of mathematical originality. L020 is the only
local mathematical input, for coding; external inverse semantics are
cited precisely in L030. Least-root results motivate downstream use
but are not assumptions of the negative test. A separate critical
audit will inspect the guards and exhaustiveness; its coverage must
be approved before invocation. Universal descent, other cylinders,
prefix entry and compensation remain unproved.
