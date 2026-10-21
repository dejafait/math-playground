# 2026-10-04 — regulator response working calculation

The saved scratch calculation below was completed in L366; its canonical proof is in lemmas/L366-gaussian-regulator-response-and-coupled-remainder.md. This snapshot is retained, not an additional proof or current checkpoint.

Target and source gate: the exact COVERED_TARGET in drafts/literature/2026-10-04-gaussian-regulator-response.md, SPECIALIZE, is reused. No new literature is needed. Existing changes are preserved.

Gap: L357 controls absolute Fourier error, not error divided by L358's gamma envelope. Test the proposed second-order bound with two frequency derivatives; a successful approximation still leaves a signed arithmetic margin and higher Laguerre levels unproved. L365 stops a different fixed-regulator global-sign certificate and is not reopened.

Working calculation (not yet a recorded lemma): with s=1/4+iξ/2, Mellin inversion of S_ε has integrand Γ(z)(πε)^(-z)ζ(2s+2z). Shift from Re z=1 to -5/2. The moving pole z=1/2-s cancels L358's complete beta subtraction. The three gamma residues give ζ(2s), -πεζ(2s-2), and (πε)^2ζ(2s-4)/2. The left-line integral should be O(ε^(5/2)(1+|ξ|)^5), using reflection, absolute right-half-plane Dirichlet convergence, and gamma decay in the contour variable. The coupled condition turns this into O(ε²(1+|ξ|)^4). Cauchy on negative-real-part zeta disks supplies log^j factors; the external gamma factor has relative derivatives O(log^j(2+|ξ|)).

The proposed response is G=p Re[(s-1)Λ(2s-2)]=-p Re[ξ_c(5/2+iξ)/(5/2+iξ)], where Λ(w)=π^(-w/2)Γ(w/2)ζ(w) and ξ_c(w)=w(w-1)Λ(w)/2. Check the sign, normalization, contour horizontal bounds, and differentiation before promoting. No sign or RH candidate is claimed.
