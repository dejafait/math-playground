# Split connection removal — bounded applicability attempt

2026-10-16, step 326, completed; superseded by the canonical proof in
`lemmas/L114-split-harmonic-connection-smooth-removal.md`, pending a
separate critical audit. Approved exact target: Test smooth
extension of L113's actual harmonic Chern connection across each split
point on L111's holomorphic bundle M. Prior assessment:
`drafts/literature/2026-10-16-split-harmonic-connection-removability.md`
(SPECIALIZE). No new source assessment is needed for this attempt.

Main gap: universal primitive rational Hodge realization. Intermediate
target: the actual connection extension, potentially useful for a later
normal-bundle stability test. Existence of F, |Z|, reconstruction and
transport remain independent gaps. Continue only after verifying the
whole Hermitian tangent comparison, ASD, compact-simple group scope and
holomorphic inverse extension; stop or narrow if any fails.

Inputs read: L100's actual slice comparison and normalization;
L108's full relative-Ext descent and actual metric splitting;
L111's hypotheses/local freeness; L112's exact natural harmonic metric;
L113's hypotheses and curvature/energy passage. ATTEMPTS/063/066/067
do not already supply removal and remain preserved. No cross-notebook
input is used.

Proof plan awaiting canonical write-up: the local stable Quot family
and F differ by a base line (relative Hom and evaluation); hence the
whole relative Ext is holomorphically the tangent pullback. HE
uniqueness on stable fibres identifies their End metrics, giving a
fixed positive harmonic normalization factor. Chern uniqueness gives
the pulled-back Levi--Civita connection. Natural quaternionic chart
transitions preserve the parallel antiunitary J, producing Sp(25).
Hyperholomorphic tangent curvature pulls back to type (1,1) for every
source structure, hence ASD in real dimension four. Bianchi implies
differential Yang--Mills. Parker 8.1 with zero particle/mass and L113
then removes each puncture. Smooth ASD extension is integrable; apply
Hartogs to both holomorphic isomorphism matrices and their inverse
identities to identify the extension with M and transfer its metric.

No semistability or cardinality claim is part of this attempt. The
canonical proof must retain original metrics, all fifty tangent
directions, curved base and compact-simple Sp(25), and both inverse
matrices; a smooth gauge extension alone is insufficient.
