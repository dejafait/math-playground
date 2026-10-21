# Plateau response: bounded quantitative attempt, 2026-10-18

Target: Assess whether L216's complete plateau response differs from a^(-3)P_i by O(N^(5/2) log(eN)^2) for both actual probes.

Prior gate: `drafts/literature/2026-10-18-plateau-action-quantitative-remainder.md`, SPECIALIZE, saved before this invocation. Actual task: proof_attempt; classification REPRODUCTION.

Main gap: interacting reflected error <=c_box/2, continuum axioms and finite positive mass. This component rate could join L215 and the separate L230 estimate; independent component and interacting gaps remain.

Initial saved reasoning, before completion: retain L216(1),(2),(15) exactly. Put C_(j,N)=a A_<j. Import L224(2)--(5),(10)'s audited signed dipole decomposition, coefficient rate and energy cutoff method, but replace its fixed source buffer by a lattice radius R. For traversal sources at distance >=4R from each transverse face, test energy projection error O(R^(-3/2)) using the cutoff potential. Compare the finite C pairing with its full-grid extension using the uniform energy form bound. Freeze its signed dipole coefficients using their O(a) value error, Lipschitz variation and the finite weighted l2 energy moment. This should cost O(a) independently of R. The complementary collar has normalized absolute cost O(R/N), retaining all normal end rows. R=ceil(sqrt(N)) would meet normalized O(N^(-1/2)) if these estimates close.

Initial obligations: full-grid form extension and bilinear freezing for two distinct traversal dipoles; boundary-supported traversal values; raw a^(-2)U mode normalization for both actual probes, all cuts and omitted labels; C^1 limiting integrand and quadrature with the cumulative upper tail.

Continue only if the complete finite-N response bound is <=C_i N^(5/2)log(eN)^2 with summable mode dependence. Stop this transfer if its actual energy/collar or modal dependence misses that threshold; a weak norm upper bound is not signed growth. No scripts or numerical evidence are needed. Essential inputs: L008 L025 L028 L042 L065 L101 L214 L215 L216 L222 L224. The known raw-loop and upper-pin failures are preserved; no rough prefix or upper forest pin is extended smoothly.

Completed disposition: [L231](../lemmas/L231-plateau-action-quantitative-remainder.md) is the canonical proof. Its uniform normalized error is C_i[(R+1)/N+R^(-3/2)+a], and R=ceil(sqrt(N)) proves O(N^(5/2)) for the unscaled remainder. All initial obligations are addressed there, pending a separate critical audit. This draft preserves the pre-work checkpoint; it is not a second proof or current next-action record. No attempt was abandoned and no negative artifact is needed.
