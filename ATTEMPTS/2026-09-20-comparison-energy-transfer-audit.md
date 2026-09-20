# Comparison energy proof: transfer audit

Date: 2026-09-20

Outcome: park direct transfer of L053–L054 to the theta transform. This reviews existing proofs and their applicability; it does not prove that a different spectral construction is impossible. No new lemma is introduced.

## Required mechanism and downstream use

The main gap remains nonnegativity of every actual reciprocal-zero mixed form, or an independent exclusion of every nonreal Ξ zero. The proposed alternative needs, at each Ξ zero z, a nonzero half-line function Y satisfying a closed equation -(pY′)′+qY=z²wY with real coefficients, p,w positive, a positive energy numerator, finite integrals, and a vanishing boundary form. Multiplication by conjugate(Y) would then make z² a positive real energy quotient. L018 would translate real z into RH. Merely obtaining a real quotient would still require excluding negative z²; positivity in L054 handles that issue for its own transform.

## What was checked

L053 obtains its equation from the exact identity k_xx-e^(2x)k=k_tt for k=exp(-e^x cosh t). The integration in t has zero boundary contributions, including k_t(x,0)=0. Its asymptotic proves the solution is nontrivial, not merely decaying. L054 uses G(z)=0 to get Y(0)=0; its proved decay kills the boundary at infinity. Thus both boundary terms in the energy integration vanish. The integrals of |Y′|², e^(2x)|Y|² and |Y|² converge, and the last is nonzero. No gap was found in this zero-reality argument. The additional bound z²/4>7 concerns G alone and is unnecessary for the proposed transfer.

L019 instead defines the actual theta kernel by K=2A″-A/2, where A(u)=e^(u/2)ψ(e^(2u)). This is an identity in the integration variable u. It is not the closed equation in an auxiliary half-line variable x and spectral parameter z used by L053. The proof does not identify the theta transform with G, nor construct a new family with the required equation. Positivity and decay of K do not provide that identification.

The boundary calculation is already explicit in L020: with J(z)=∫₀∞A(u)cos(zu)du, it gives Ξ(z)=1/2-2(z²+1/4)J(z). At an actual Ξ zero this imposes (z²+1/4)J(z)=1/4, not J(z)=0. In particular neither factor can vanish. The constant comes from A′(0)=-1/4. Dropping it to imitate the comparison Dirichlet condition changes the transform. Using K directly retains Ξ as a boundary value, but the required auxiliary equation, nontrivial solution, and energy boundary estimates have still not been supplied. These are distinct obligations; the boundary issue for J is not an impossibility result for a construction based on K.

## Redundancy, threshold, and decision

L055 and L057 already show why the established generic comparison properties cannot transfer zero reality to other positive kernels. Another such counterexample would add nothing. Their scope does not encompass every consequence of the exact theta transformation. This audit tests the specific proposed use of the existing energy proof rather than extending those counterexamples.

The achieved energy bound is z²/4>7 for zeros of G. The required conclusion is z²>0 for every zero of actual Ξ. No bound for those zeros follows from the comparison estimate, and no actual mixed positivity beyond the recorded finite tests has been obtained. The main RH gap is unchanged, and no candidate or rigorous off-line zero is produced.

**WHY IT FAILS.** The successful comparison proof needs an exact differential identity, nontriviality, and compatible boundary conditions for the same transform. The actual theta representation supplies neither the auxiliary eigenvalue equation nor the comparison boundary condition for J; its nonzero boundary contribution is essential. Consequently the current transfer has no justified energy quotient for Ξ. Park it unless an explicit actual-theta family and closed positive self-adjoint equation are supplied. This decision leaves open other spectral approaches and all arguments exploiting additional theta arithmetic.
