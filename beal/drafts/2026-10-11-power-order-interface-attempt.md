# Power-order sufficient interface — bounded proof attempt

Approved target: Prove the sufficient power-order certificate interface for L045, including the exact extension of (11,k-8)R and a rational-lattice verification specification.

Prior coverage: drafts/literature/2026-10-11-global-eleven-order-extension-certificate.md (SPECIALIZE; exact COVERED_TARGET). Reuse inspected sources; no new literature, witness search or mathematical script is needed.

Main gap: unconditional global emptiness of surviving (3,4,11) branches and the other residual signatures. Intermediate target: sound verification of a supplied power-order identity. Downstream use: certify u=0 and retire the eleven valuation obstruction, without implying point or integer existence. Continue if all places and exact lattice operations suffice; abandon this interface if missing maximal-order data, R-ideal inverses or restricted-search completeness become necessary.

Saved reasoning: L041 orders the three maximal primes by residues 8,2,10. At P1 the orders of 11 and k-8 have minimum 1; at P2 and P3, k-8 is a unit. Away from eleven, 11 is a unit. Thus JO_K=P1. A full-rank rational lattice stable under multiplication by k is a fractional R-ideal. Extension of products follows by denominator clearing and integral product preservation. The proposed identity gives (alpha)=P1*(AO_K)^5*(5O_K)^e; its rational five factor is principal, yielding [P1] in 5Cl(K), stronger than u=0. No A inversion in R is used.

Verifier plan: exact power-basis coordinates modulo L033's monic degree-twelve polynomial; rational nonsingular basis B for A; integral entries of B^(-1)TB test k-stability. Generate J by columns of 11I and T-8I. Generate products using all pairwise generator products, principal alphaR by multiplication matrix, and scale by rational 5^e. Compare full lattices after common denominator clearing, with certified HNF or explicit integral coordinate maps in both directions. Rank, determinant or norm equality alone is insufficient.

Inputs: L033, L041, audited L045; L044 supplies the downstream filter already stated in L045. Preserve ATTEMPTS/013 and ATTEMPTS/025. Witness existence, arbitrary five-prime freedom, other-place compatibility and integer-power lifting remain unresolved. No cross-notebook input.
