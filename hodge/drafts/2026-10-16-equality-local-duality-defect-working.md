# Local duality defect calculation — saved reasoning

2026-10-16. Approved target: determine the exact local duality sequence
in L108's conditional (14,21) family. Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-15-equality-local-duality-defect-sequence.md`.
The main gap remains primitive Hodge realization; a useful consequence
would control w+q in L108. Independent F existence, metric extension,
semistability and transport gaps remain.

Inputs read: corrected L108's full pairing, torsion-free argument and
signed budget, its audit, ATTEMPTS/066, and relevant hypotheses of
L071/L095/L097/L100. Immediate source notes/history contain no prior
defect sequence. Preserve all existing changes.

Calculation awaiting final verification: at R=O_{B,z}, write M=A_1,z,
W=A_2,z and D=RHom_R(-,R). Actual cup/trace duality should give
C[2] ~= DC, normalized to L108's form on the puncture. Torsion-free M
has projective dimension at most one; W has Ext only in degree two.
The contravariant spectral sequence therefore has only M^* in (0,-1),
Ext^1(M,R) in (1,-1), and W^dagger=Ext^2(W,R) in (2,-2).
Its only possible differential is d_2:M^* -> W^dagger. The resulting
sequence should be

    0 -> M -> M^* -> W^dagger -> W -> Ext^1(M,R) -> 0.

The first map must be identified with the actual extended symplectic
form composed with M -> E, rather than inferred from abstract
self-duality. Hom(M,R)=E^* and Ext^1(M,R)=Q^dagger by the hull
sequence. If the map identification holds, this gives

    0 -> Q -> W^dagger -> W -> Q^dagger -> 0,

hence q_z <= w_z, with no upper bound from lengths alone.

Discriminating local model to check: over C[x,y]_(x,y), take the
Koszul cochain complex for (x^n,y), in degrees 0,1,2, plus a free
rank-fifty symplectic module in degree one. It should have M free,
Q=0, W=R/(x^n,y) of length n and residue-field Betti ranks (1,52,1),
with the same symmetric degree-two derived pairing and a perfect
alternating middle form. This tests only duality/cohomology constraints,
not L095's actual derivative or global geometric realization.
Continue only for defect control or a precise further map test;
otherwise park the duality-only numerical bound. No result is yet
claimed by this working checkpoint.

Completed: canonical L109 proves the displayed sequence using the
actual normalized cup/trace adjoint and the dual truncation triangle;
the hyper-Ext positions independently check the shifts. Its first
map is compared with L108's hull form on the puncture and then over R.
This yields q_z<=w_z. The full Koszul model calculation, including
pairing signs, length n and derived dimensions (1,52,1), is in L109.
It proves no upper bound follows from these duality/cohomology data,
without purporting to retain the actual KS constraints of F. Park
the duality-only numerical route; preserve all earlier work. A separate
critical audit is the sole next target, pending literature approval.
