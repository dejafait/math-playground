# Step526 working checkpoint: count-bounded pole cancellation

Approved target: Test C744t whole-contour propagation with a count-bounded pole product, a horizon-independent full-complement bound, and paid division on Gamma.

Prior SPECIALIZE coverage: `drafts/literature/2026-11-11-cluster-pole-product-test-525.md`; reuse the completed step525 comparison. Main gap: actual-Xi positivity. Intermediate use: remove the isolated-pole-chain certificate from a qualified two-cell detector length, leaving independent signs and global assembly open.

Work in progress, not yet an audited result. Let t0=Im(p), let U be the closed rectangle delta/4<=Re(s)<=2, |Im(s)-t0|<=1, and include every distinct zero with |Re(z)-t0|<=2 in P(s)=product((s-iz)/4). The degree is at most N=ceil(A(T+2)log(e(T+2))). On U, each factor has modulus <1 because sqrt((5/2)^2+3^2)<4. Exterior poles have distance >1 from U. Tentatively |P G|<=S (internal terms cost 1/4, external terms cost 1), so |P(G-J_H)|<=M=S+4C/delta under fixed-window nonnegativity. The full exterior is retained and holomorphic on a padded neighborhood with imaginary half-width 3/2.

Tentative propagation: rho=delta/32, n=ceil(1/rho), lambda=1/2-rho, Q=S/lambda. Connect 1+it0 to finitely many centers on Gamma by n equal steps; enlarged radius-4rho disks lie in U. Use ceil(2pi r/rho) centers, whose endpoint rho disks cover Gamma. Three circles gives sup_Gamma |P(G-J_H)|<=M^(1-2^(-n))(Q exp(-lambda H))^(2^(-n)). C744t's all-pole boundary clearance pays |P|>=(d/4)^N=:eta. Target beta=alpha eta/(2R); M>=S>=alpha>beta. Proposed H_*=[max(0,log(Q/M))+2^n log(M/beta)+1]/lambda, K_*=max(2,1+ceil(H_*/ell)). Division then gives the strict unweighted contour threshold.

Still to check before canonical recording: every closed-domain/neighborhood and count endpoint, multiplicity versus distinct factors, cover and step count, log signs and integer horizon, and exact strict-budget/energy quantifiers. No numerical certificate or independent positivity is claimed. Stop if any essential clearance, product, infinite-tail or H-dependent cost cannot be paid. No script is needed for these symbolic inequalities.

Completion note: the full proposed derivation, including those checks and renamed product lower bound mu (to avoid the bump's eta notation), is now canonical in `lemmas/C744u-count-bounded-pole-product-two-cell-length.md`. It is a qualified symbolic length, pending a separate conceptual audit. The draft above is retained as the pre-completion reasoning checkpoint, not a second canonical proof.
