# Equality normalization degree — mathematical working record

2026-10-13, step 258. RESEARCH / REPRODUCTION, proof_attempt, under
the pre-existing SPECIALIZE assessment
drafts/literature/2026-10-13-equality-normalization-generic-degree.md.

The main gap is universal primitive Hodge-class realization. The bounded
target is generic degree one for L098, potentially useful for reconstruction.
The test is to justify the punctured normalization cover, its Galois deck
action on the actual source, and preservation of the actual two-form, then
apply the known Picard bound. Any failed bridge stops this mechanism.

Inputs inspected: L098 including its step-256 audit; L095's full raw-form
calculation and audit; L065 as methodology only; the older ready degree
assessment and L062's general exterior-sign calculation; the rank-four
scope in L025/L044/L071 and foundations/05. ATTEMPTS/061's second-order
stop is preserved. Existing notebook changes are left in place.

Saved reasoning before the full write-up: write N for the normalization
of W, T for the full finite preimage of m_0 in N, and V=N minus T.
The actual factor h is finite surjective; h^{-1}(V)=U. Relative
differentials and normal-target unibranchness give finite etaleness on U.
Every connected finite-etale cover of U extends across the finite set in
smooth B and is trivial by the K3 fundamental-group theorem. Hence a
connected Galois refinement of U over V is U itself. Deck transformations
extend through the normalization in C(B); no purity at singular points
of N is used. On U the actual ordered KS pairing is minus L095's raw
integral, so the coarse Mukai pullback is a fixed nonzero multiple of
sigma_B. The extended deck group is therefore symplectic. A nonidentity
element would require Picard rank at least nine, against four retained.

This is a proof plan until the complete canonical application is written.
F existence, integrated split germs, original-image separation,
reconstruction and transport are independent unresolved assumptions/gaps.
No mathematical script or numerical certificate is needed.

Resumed completion, 2026-10-13: preserve the above unfinished plan.
The extension argument will identify the actual finite normal B with
the integral closure of N in C(B), so every deck field automorphism
extends uniquely over the full finite exceptional set. Purity is used
only for covers of U extending to the smooth source B. For the form
comparison, use L098's actual KS representative and L095 (7)--(9):
the unnormalized integral of Tr(alpha_v wedge alpha_w) wedge sigma_1
equals 4pi^2 gamma_R(v,w). The printed coarse Serre-trace normalization
differs by a single fixed nonzero scalar. The earlier sentence about
the minus sign refers to the normalized ordered pairing; the degree
test needs only this nonzero comparison, not a new metric sign claim.
Full reasoning will be canonical in L099; no form on the exceptional
coarse point or initial Galois assumption is being introduced.

Completion: the full conditional proof is now canonical in
lemmas/L099-equality-normalization-generic-degree-one.md. It gives
generic degree one and identifies B with the normalization, pending
separate critical audit. The known Picard constraint is decisive;
no numerical certificate or mathematical script was used. This
working plan is retained as unfinished-work history, not a second
proof or current continuation record.
