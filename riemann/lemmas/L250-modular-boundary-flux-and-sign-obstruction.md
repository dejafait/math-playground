# Lemma 250: modular boundary flux and a wrong-sign boundary term

**Hypotheses.** Let A and K be the actual theta functions of L019, and define the entire functions

H(z)=∫₀∞ A(u)cosh(√z u)du,   F(z)=∫₀∞ K(u)cosh(√z u)du,

where the square-root expressions are interpreted by their power series. Put q=2z−1/2, y=Im z, and W_F(z)=Im(F′(z) conjugate(F(z))). By L020, F(z)=Ξ(i√z).

**Conclusion.** The exact modular integration-by-parts identity and its flux decomposition are

F(z)=1/2+qH(z),

W_F(z)= (1/2)Im F′(z) −4y|H(z)|² + |q|² Im(H′(z) conjugate(H(z))).

There exist δ>0 and η>0 such that for every 0<t<δ and 0<ε<η, at z=−t+iε the boundary contribution (1/2)Im F′(z) is strictly positive. The constants can be chosen so that ε²<t+1/2 and F(z)≠0 throughout this rectangle. Thus the modular boundary contribution does not have the nonpositive sign required for a termwise proof of W_F≤0, even inside the fine-resolution region. This does not assert that the total flux is positive.

**Proof.** L019 bounds A, A′, A″, and K by an integrable superexponential function after multiplication by any fixed exponential or polynomial. On compact z sets, the power-series kernels and all fixed z derivatives admit exponential-polynomial majorants in u. This follows either directly from the series or from the entire even function cosh(wu) with w²=z, bounding |w| on the compact set and removing its apparent singularity at w=0 by the series. Consequently H and F are entire, and differentiation and the following integrations by parts are justified. If C(u)=cosh(√z u), then C(0)=1, C′(0)=0, and C″=zC. Boundary terms at infinity vanish. Hence

∫₀∞ A″C du=−A′(0)+zH(z).

The exact modular derivative A′(0)=−1/4 and K=2A″−A/2 from L019 give F=1/2+qH. This is the representation already present in L020 after changing variables; it is not a new representation theorem.

Differentiation gives F′=2H+qH′. Expanding F′ conjugate(F) gives

H+(q/2)H′+2 conjugate(q)|H|²+|q|²H′ conjugate(H).

The imaginary part of the first two terms is (1/2)Im F′; that of the third is −4y|H|². This proves the flux identity without division by F, including at its zeros. Where F≠0 it gives Im(F′/F)=W_F/|F|².

For the sign test, the entire series and positive K give

F″(0)=(1/12)∫₀∞u⁴K(u)du>0,   F(0)=∫₀∞K(u)du>0.

These are finite by L019. Write c=F″(0)>0. Continuity supplies a disk about zero on which Re F″>c/2 and F≠0. Since F′ is real on the real axis, integration along a vertical segment in that disk yields the exact identity

Im F′(−t+iε)=∫₀ε Re F″(−t+is)ds > cε/2.

Choose δ and η positive so that all these segments lie in the disk, and choose η<1/2. Then ε²<1/4<t+1/2, and the boundary contribution exceeds cε/4>0. No numerical estimate or assertion about unknown zeros is used. ∎

The required bound is the total W_F≤0 at every upper-half-plane point, together with exclusion of its nonreal zeros. This identity supplies a negative explicit bulk term but a positive boundary term on a proved actual-theta region. The remaining comparison would have to bound |q|² Im(H′ conjugate(H)) by 4y|H|²−(1/2)Im F′. Neither the modular boundary value nor the algebra above proves that comparison. The local rectangle is already far from the possible nonreal poles allowed by localization; its role is to disprove a proposed termwise sign assignment, not to challenge RH or determine the hard-region total sign.

**Mathlib.** Not checked: coverage of the full flux identity, parameter integration, and supporting integration-by-parts and continuity facts was not checked. No matching theorem is asserted. L019 supplies the mathematical theta input; its underlying modular identity is the named Poisson-summation input in L016. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
