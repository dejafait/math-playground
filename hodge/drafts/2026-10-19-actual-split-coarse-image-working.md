# Actual split coarse-image comparison — mathematical working note

2026-10-19, step 408. RESEARCH / proof_attempt / REPRODUCTION under the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-19-actual-split-coarse-image-comparison.md`.

Main gap: universal primitive rational Hodge realization; the conditional
kernel F is also unconstructed. Approved intermediate target: identify the
ordinary reduced analytic image of one actual equality-family source germ
with its full-stabilizer harmonic quotient image. Downstream use: transfer
L132's actual invariant restrictions to L097's specified coarse space.
Continue only if actual family isomorphisms give ordinary quotient descent
and equality of the two pullback kernels. Weak normalization, pointwise
orbit equality without invariant-sheaf descent, and a formal chart do not
meet the target. Do not infer degree two or a nonempty split locus.

Pre-existing active-notebook changes are preserved, including L043 and all
untracked artifacts. Relevant inputs inspected: L097/L098 hypotheses and
placement/finite-map proofs, L103 full-group and ordinary-quotient tools,
L132 actual-family comparison and determinant normalization, ATTEMPTS/063.

Attempt plan, not yet a proof: take an H-Gieseker Quot Luna slice T with
its actual analytically semiversal family and quotient germ M. Let K be
the complete harmonic integrability germ with its actual family and full
G=(C*)^2 action. Semiversality in both directions gives base maps with
family isomorphisms, but these base maps need not be equivariant. Descend
their composites with quotient maps by proving restricted G-invariance
from actual family isomorphisms, then use ordinary invariant sheaves.
Check both inverse identities only on reduced quotient germs. Finally
retain the actual alpha:(B,z)->K and compare kernels in O_{B,z}; keep all
other preimages of the split coarse point out of this one-source kernel.

Outstanding technical check: quotient descent must use sufficiently small
invariant/saturated representatives and local invariant extension. The
H-Gieseker openness theorem must cover the whole reduced harmonic family
near E, not just the actual equality subfamily. No h/H semistability
equivalence for arbitrary nearby sheaves is assumed.

Applicability check completed during the proof attempt: reconsulted the
already assessed primary statements, not a new literature search.
Greb–Toma Theorem 2.9 applies to flat analytic families with the fixed
integral H and gives a semistable representative of the entire harmonic
family. Proposition 2.17 supplies the actual analytic Quot-slice family.
Buchdahl–Schumacher Definition 1, Theorems 1–3 and Section 5.2 retain
ordinary invariant-function descent on saturated representatives. For
non-equivariant base maps, extend only their quotient composites by
F(gx)=F(x); endpoint family isomorphisms give independence on overlaps.
The quotient composites, rather than base maps, are invariant.

Both inverse identities reduce to actual bundle isomorphisms: on K use
the small-slice isomorphism/orbit theorem; on T use the canonical
Gieseker classifying map. Equality on points becomes equality of maps
only because both quotient germs are explicitly reduced. Retaining the
actual alpha then gives equality of homomorphisms to O_{B,z}, hence
pullback kernels. Full details are being saved in canonical L133.

Completed: canonical L133 records the conditional ordinary reduced germ
isomorphism and one-source image-kernel equality, with full hypotheses,
primary citations, reduction and saturation checks. This is a known-tool
specialization, not progress beyond the checked sources. DAG and PROOF
now contain only the corresponding dependency row and short assembly/trap
updates. A separate critical audit is registered as REVIEW_REQUIRED;
no local-degree, kernel-existence or universal-Hodge claim is made.
