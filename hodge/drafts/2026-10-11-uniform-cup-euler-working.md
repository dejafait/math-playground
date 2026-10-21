# Uniform determinant cup/Euler attempt — working checkpoint

2026-10-11, step 228. RESEARCH / REPRODUCTION under the unchanged
SPECIALIZE assessment for the exact uniform stable-fibre target.
Existing notebook changes and earlier stops are preserved.

Main gap: universal primitive rational Hodge realization. Intermediate
target: a uniform necessary Euler condition on the changed-sign common
kernel; downstream use: remove correction pairs before kernel construction.
Continuation test: both actual image concentrations/preservation, perfect
section forms and same-class cup comparisons must hold. Failure of any
bridge stops or narrows the claim. Independent kernel existence and
transport gaps remain.

Inputs inspected: L071's full character, every-fibre polystability and
exact split-charge lattice; L090's coefficient square-zero and actual
restriction/trace method; L091's arbitrary-rank base-change/preservation
and trivial-part method. ATTEMPTS/042/043/051/057/058 were compared.
No essential missing source scope or cross-notebook input is used.

Provisional derivation to write canonically: charges m,n>=5 with
mn=6 mod 12 and neither in {14r^2} make all fibres stable, with odd
cohomology dimensions m-4 and n-4. Both images are actual polystable
bundles. Their perfect symmetric forms restrict perfectly to global
sections by eliminating both cross blocks with stable-Hom vanishing.
If V=H^1(X,F) has positive dimension, the same-vector polynomial test
and L090's actual maps contradict square-zero. Thus V=0. For either
image E, self-duality gives chi(E)=2 dim(V)-h^1(E), while single-row
Leray gives chi(F)=-chi(E). Negative chi(F) forces dim(V)>0.
L071 rewrites chi(F)=((m-12)(n-12)-18)/6. Therefore the strict region
(m-12)(n-12)<18 is excluded. Equality does not force a section.

Completed canonically in
[L092](../lemmas/L092-uniform-stable-fibre-euler-cup-exclusion.md).
The proof includes both actual maps, arbitrary-dimensional section
forms, the strict region, an infinite admitted family and the six
equality pairs. This working checkpoint is retained as reasoning
history, not a current status or a critical audit. No mathematical
script was needed for the exact symbolic equalities. Separate
critical audit remains pending; no complete Hodge candidate is claimed.
