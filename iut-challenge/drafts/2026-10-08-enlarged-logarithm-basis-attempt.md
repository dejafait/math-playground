# Enlarged logarithm basis — calculation checkpoint

Gate: the supplied SPECIALIZE assessment
`drafts/literature/2026-10-08-enlarged-complete-logarithm-lattice.md`.
Exact target: compute a complete Z_3-basis of the ordinary unit-logarithm
image in L=Q_3(zeta_20,pi), pi^27=3. Main gap remains original finite
B>=A and actual input/action/pilot compatibility. A certified local shell
could support a later separately reviewed action/radius calculation;
admissibility and all original-IUT bridges remain unresolved.

Preserved inputs: L030's audited field model and scalar-transport stop;
L016's all-unit filtration and tail method only. ATTEMPTS/023 and
history/083 have been checked. No existing new-field basis was found in
the target's inspected records. SymPy is unavailable; no installation
or source blocker is needed for exact elementary integer arithmetic.

Plan within the approved target: theta=zeta_20^4, Phi_5(theta)=0.
Verify irreducible separable reduction, then use coordinates
theta^a pi^r (0<=a<4, 0<=r<27). Include log(1+theta^a pi^j) for
every a and 1<=j<=13, together with all 108 columns of pi^14 O_L.
Use terms k=1,...,242 and prove the entire remaining series lies in
pi^14 O_L. Replace finite sums only by exact coordinate congruences.
Integer column normal form of the matrix after multiplication by nine
will track unimodular transformations and their inverses. Full identities
G W=B and B E=G must hold, with integral W/E and rank 108.

Continue if field identification, complete unit coverage, all tails and
both span inclusions succeed. A failed column/tail stops the proposed
certificate and is preserved; it does not refute existence of a basis
or an IUT theorem. No O_U-stability of the image is assumed.

The initial checkpoint preceded computation. Completed outcome:
[L031](../lemmas/L031-enlarged-complete-logarithm-lattice-basis.md)
gives the exact rank-108 basis, complete unit coverage and infinite-tail
proof. `scripts/cyclotomic-log/enlarged-basis.json` stores all exact
coordinates and both integral span certificates; the saved-evidence
verification recomputes all 5,616 congruences and checks every entry of
both span identities, with zero failures. Tail actual/required: 108/14.
Basis determinant valuation is 4; minimum field valuation is -2.
This is REPRODUCTION of the approved known methods, not an IUT solution
or certified mathematical novelty. A separate critical audit remains
unfinished; action/radius and all original-IUT bridges remain independent.
