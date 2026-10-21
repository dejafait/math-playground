# Complete H-scalar enclosure attempt

STEP_ID: YM-20261011-156-h-enclosure
Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Main gap: interacting ultraviolet control; immediate comparison is
K_(i,oo)+4 gamma D_i. Intermediate target: complete rigorous enclosures
of L129's h_D,h_X,h_A by two-dimensional interval integration. Their
magnitudes feed L128's actual physical contractions, while xi and the
five other coefficients remain independent unresolved inputs.

The selected test is interval integration over the entire normalized
angle square, rather than assuming bounded second derivatives at its
continuous but potentially nonsmooth corner. Reuse L127's integer
interval implementation. L129 supplies exact integrands and corner
bounds; monotonicity of 2-2cos(theta) supplies endpoint cell ranges.
Continue if full interval sums distinguish useful scalar bounds; abandon
this particular grid if interval inflation cannot meet a stated width
threshold. No actual-probe sign or compensation is assumed.

Existing exact angle reduction and h_X positivity are imported, not
rederived. ATTEMPTS/033--035 reject tensor-deletion shortcuts and are
preserved. No duplicate scalar enclosure was found in the narrow local
search. This is within the unchanged ready complete other/other target.
Essential inputs: L129 L128 L127; L124 and L084 fix assembly/reference.
No new literature is needed. Mathlib coverage remains not checked.

Saved before numerical certification. Planned exact inclusion: use
scaled-integer intervals on every angle cell, enclose the one corner
cell by L129(4), and average cell intervals with exact rational weights.
The full certificate will retain every node, cell and aggregate.

Completed: L130 proves 1/5<h_D<3/10, 1/10<h_X<1/6 and
-7/20<h_A<-1/4. Canonical proof:
lemmas/L130-other-other-h-scalar-enclosures.md. The full-cell inclusion
requires no smooth midpoint estimate; the exact arithmetic audit replays
513 endpoints, 262144 cells and all three aggregate bounds without
failures. Achieved interval widths are below 0.071, 0.023 and 0.051,
against containing thresholds 0.1, 1/15 and 0.1. The complete integer
certificate and audit are under scripts/combined-ward-response/ with
names h-scalar-enclosure-certificate.json and h-scalar-enclosure-audit.json.
No actual-probe response or complete compensation is evaluated.

Continuation within the unchanged approved comparison: contract and
evaluate L128(6)--(7)'s xi without deleting either mixed K_f orientation
or its projection factors. Start with the complete primary local formula
in L128 section 3 and L123's canonical hypotheses/proof as necessary;
any reduced integral needs its own complete corner/error justification.
Use L130's H bounds and L127's tau bound in later actual physical
contractions, retaining the nonzero anisotropy and antisymmetric jet.
Essential inputs L128 L123 L118 fix xi; L130 L129 L127 L126 L125
L120 retain the other transverse-H data. L124 L097 L098 L101 L104
L107 retain E,ax,-Q,G,R, and L084 L070 L079 L080 L082 fix the
reference and its qualifications. No sign, zero xi, physical-mode
cancellation or compensation is assumed. Continue on a complete scalar
formula/enclosure; abandon an inference based only on parity of an
undifferentiated or omitted orientation. Other heat contractions,
complete comparison, finer scales/logarithm, other jets, matching,
interacting reflected error <=c_box/2, continuum axioms, reflection
positivity, infrared control and finite positive mass remain open.
The assessment and exact Next action remain unchanged; no new
literature assessment or new target is approved in this research step.
