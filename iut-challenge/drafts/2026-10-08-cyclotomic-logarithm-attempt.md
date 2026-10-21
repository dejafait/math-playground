# Cyclotomic logarithm scalar transport — preserved working checkpoint

Approved target: determine whether log(O_{KU}^times)=O_U log(O_K^times)
for K=Q_3(pi), pi^27=3, U=Q_3(zeta_20). Coverage is the unchanged
SPECIALIZE assessment `drafts/literature/2026-10-08-cyclotomic-base-change-logarithm.md`.
The original finite B>=A and actual input/action/pilot compatibility remain the main gap.

Proposed exact witness: x=log(1+zeta_20 pi). Extend L016's separator
phi=3c_0-(31/3)c_1+9c_15-9c_18 U-linearly. L016 proves phi(J) subset Z_3
on the complete J, so phi(O_U J) subset O_U without assuming stability
of the new logarithm image. The special k=1 and k=27 logarithm terms
contribute (zeta_20^27-31zeta_20)/3. Obligations still to finish here:
prove every remaining term has integral phi value, control the convergent
infinite series, and show the numerator is nonzero modulo 3. Reduction
of zeta_20 has order 20 by the imported prime-to-3 torsion theorem.

Continuation test: valuation -1 of phi(x), versus required >=0 on O_U J,
would disprove equality and stop naive transport. A failed separator
would leave the identity undecided; it would not justify a new target in
this step. L016's complete coverage, rather than sampled old units, is
essential. No complete new-field log lattice, packet admissibility,
action/radius transport, global realization, pilot transport or essential
IUT flaw is established by this test. Result not yet claimed at checkpoint.

Completed outcome: the obligations above are now discharged in canonical
L030, with exact finite checks in `scripts/cyclotomic-log/scalar-transport.json`.
The identity fails by a genuine logarithm witness. The text above preserves
the pre-completion checkpoint; it is not the current status record. The
negative result stops naive scalar transport and is queued for separate
critical audit before any further changed-field use.
