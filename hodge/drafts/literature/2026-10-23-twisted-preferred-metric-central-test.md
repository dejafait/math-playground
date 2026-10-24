# Twisted central pairing — preferred connection metric

TARGET: Test L149's central orthogonality at every actual split parameter using the twisting-line metric dual to L094's Hermite–Einstein metric on L.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched hyperholomorphic harmonic Serre-duality/Hermitian-pairing/split-weight terminology and Nahm-transform cohomology-jump/direct-image terminology; inspected Verbitsky's primary operator and harmonic-action statements/proofs and BBHR's IT hypotheses/proof cases; compared L094, L113, L146, L148, L149 and ATTEMPTS/060/063/066/067/086.
SOURCE_EVIDENCE: Verbitsky, alg-geom/9307008v1 (29 July 1993), Section 4, Proposition 4.2, Theorem 4.1 and Corollary 4.3, PDF pp. 13–16; Bartocci–Bruzzo–Hernandez Ruiperez (1998), Definition 2, Section 3.3 Lemmas 1–2 and Theorem 3, printed pp. 244–246; reuse the inspected BGS/Demailly coverage in the October 23 two-sided-bound and curvature assessments.
COMPARISON: The real-adjoint harmonic action applies to L094's split connection and actual KS plane; it does not assert L149's projected-weight orthogonality. Choosing the dual connection metric makes a comparison with that adjoint product a well-posed specialization, unlike the arbitrary weighted product parked in ATTEMPTS/086.
GAP: Establish or refute the exact relation between the positive KS plane's Serre annihilator and the negative KS plane's Hermitian orthogonal complement for this preferred metric; metric compatibility, both weight projections and the natural central identification must be checked explicitly.
REASON: Approve only this later preferred-metric test as a REPRODUCTION specialization of known harmonic tools; no central vanishing or new theorem is established by this source review. A newly written continuation remains subject to the supervisor's separate approval turn.
LITERATURE_REASON: Recovery requires a different target after the three-exploration sequence; the previous arbitrary-metric assessment explicitly excluded choosing a preferred metric, so this changed hypothesis needs separate comparison.
SCOPE: Hypothetical L071 equality F, identical marked K3 factors/common metric, integral c_1(F)=0, ch_2(F)=-14e_1-21e_2-tau_D, fixed k=(-4,-2,1,2), G=F tensor p_1^*L^{-1}, and finite possibly empty Z; replace only the auxiliary twisting-line metric by the dual of the fixed Hermite–Einstein line metric used in L094. Keep the holomorphic family and ordinary sheaf M unchanged.

## Relevance and bounded test

The main gap is universal primitive rational Hodge realization. The
intermediate target is the central pairing for this one distinguished
metric. Its plausible downstream use is to supply the cancellation needed
for a later bounded-curvature and connection-extension attempt on L147's
actual rank-24 image. Those downstream conclusions are not approved or
proved here. Neither F nor a nonempty split set is known to exist.

At an arbitrary selected z in Z, retain L146's actual classes p_i,q_i
and L149's spaces P_z and J_z. Test whether J_z is precisely the
Hermitian orthogonal complement of P_z for the preferred twisted
harmonic product. Continue only on an actual comparison establishing
that equality uniformly in the choice of split parameter. A failure of
the projected-weight comparison parks this mechanism; a calculation in
an abstract complex or a single illustrative tangent plane is insufficient.
If Z is empty the local assertion is vacuous. Success would leave the
original arbitrary metric and the proposed scalar-variation question open.

## Primary theorem comparison

[Verbitsky, *Hyperholomorphic bundles over a hyperkähler manifold*,
alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1#page=13),
Section 4: read the parallel-real operator setup, Proposition 4.2 proof,
Theorem 4.1 proof, and Corollary 4.3. The commutator proof uses a
Hermitian holomorphic connection for all three induced structures;
the Laplacian identities give the real SU(2) action on harmonic
cohomology, quaternionic in degree one. Its applicable coefficient is
L094's real adjoint bundle. No real structure on G is supplied by
choosing the preferred line metric. The remaining specialization must
pass through the two adjoint weights and compare their products with
the actual twisted product. The cited theorem alone does not state
the desired orthogonality.

[Bartocci–Bruzzo–Hernandez Ruiperez, *A hyperkahler Fourier transform*,
Differential Geometry and its Applications 8 (1998), 239–249](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6):
Definition 2 requires the parity vanishing at every parameter. Section
3.3 assumes it before the twistor direct-image argument; Lemmas 1–2 and
Theorem 3 produce a quaternionic instanton under that hypothesis. The
split endpoint jump recorded in the October 12 assessment remains.
This theorem is therefore no automatic whole-base extension theorem here.

The general spectral and Chern tools need no new proof. Reuse
[the two-sided-bound assessment](2026-10-23-twisted-harmonic-metric-two-sided-bounds.md)
for BGS III Section 1(b)–(c), Theorem 3.5/Lemmas 3.6–3.8, and
[the curvature assessment](2026-10-23-twisted-harmonic-metric-curvature.md)
for Demailly V.12/V.14. The former admits any fixed smooth positive
coefficient metric, including the newly specified one; the latter's
arbitrary-metric cancellation was not proved. Do not transfer a bound
between metrics or replace the natural derived-fibre comparison.

## Duplicates, failures and choice of mechanism

Three mechanisms were compared. Arbitrary scalar perturbations would
need actual-family nonvanishing and control of changing harmonic
representatives; the saved proposal contains neither. It is parked,
without calling a zero first variation invariance. Preferred-metric
comparison instead tests compatibility within an already supplied real
harmonic space. Automatic twistor/direct-image extension still encounters
the IT failure above and ATTEMPTS/063/066's surface metric-extension gap.
The preferred-metric test is selected; the other two are not continuations.

L113's adjoint Serre/Hermitian frame identity is a ready comparison,
not the desired twisted statement. L094/L095 supply the actual quaternionic
KS geometry. L134/L145/L146 identify both actual weights and the
incoming/outgoing maps; L146/L148 fix the natural central comparison.
L147/L096 retain the ordinary image and finite possibly empty Z.
L149's criterion remains pending critical audit and is not used to claim
a curvature conclusion in this source review. No matching preferred-metric
test was found in the scoped local records; this is not a novelty claim.

The general source statements are imported, with only the stated
weight/product specialization left for research. The original weighted
expression and all stops remain intact. No scripts or lemma files are
changed. Full matching Mathlib coverage is not checked. F, nonempty Z,
extension, positivity, a split-set bound, reconstruction, transport and
the universal Hodge target remain unresolved. No cross-notebook input
is proposed.

Queries actually used: `hyperholomorphic line bundle K3 Hermitian Einstein
harmonic Serre duality quaternionic Nahm transform`; `Verbitsky
hyperholomorphic bundles Theorem 2.27 real structure harmonic forms`;
`hyperholomorphic harmonic Serre duality Hermitian pairing split line
bundle weights`; `Nahm transform cohomology jumping hyperholomorphic
direct image surface polystability`. Other search hits remain unread
leads and supply no mathematical input. No failed retrieval is retried.
