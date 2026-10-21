# Minimal factor existence — working checkpoint

Approved target: rank-two locally free bundles with c_1=0, c_2=5 or 6,
slope-stable at L044's exact real ample h. Assessment saved before this
invocation: literature/2026-10-05-minimal-survivor-stable-factor-existence.md
(SPECIALIZE). Main Hodge gap and global product/transport gaps remain open.

Inputs being applied: L044's ample h and L052's integral perpendicular
lattice Zk, k^2=-14; Yoshioka math/9907001v2 Theorem 0.1,
Corollary 0.3 and Lemma 1.5; Ellingsrud–Lehn alg-geom/9704016v1
Theorem 1; O'Grady (2022) Section 3.

Attempt in progress: v_c=(2,0,2-c), square 4c-8, ell=2.
Yoshioka's half-square threshold is 4, met at c=5,6.
Primitive c=5 and nonprimitive c=6 must be treated separately.
For a stable torsion-free E, B=E** is a stable bundle with
c_2(B)=c-t>=4 by the section/dual-section Euler argument.
Coarse stable dimensions are 4c-6 and 4(c-t)-6; relative length-t
Quot contributes 3t, hence defect bound 4c-6-t.
Need to justify parameterization on local moduli charts consistently.

Endpoint caution: O'Grady's a=4c full wall set includes k^perp at h,
since k^2=-14 lies in [-24,0). It is incorrect to place h in an
open full a-chamber. Locally this is the only full wall through h.
Choose rational H and rational rays approaching h in one adjacent
chamber. Chamber stability gives endpoint semistability by continuity.
For a saturated equality-slope rank-one subsheaf, l=rk and
c=length(Z)+length(W)-l^2 forces r=0 for c=5,6; l=0 would
already violate strict stability at H. Need to write this passage fully.

Continuation test: complete both the positive-dimensional stable-locus
and strict defect-codimension arguments, then exclude equality slopes
at the real endpoint. Abandon automatic existence from these imports
if the stable locus, dimension accounting or chamber endpoint fails;
failure of this argument is not a nonexistence theorem.

Completed in the canonical [L053 proof](../lemmas/L053-minimal-survivor-stable-factor-existence.md).
Both values satisfy the existence test; the full-wall endpoint caution
was retained. This is archived reasoning, not the current checkpoint.
