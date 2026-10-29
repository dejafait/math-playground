# Lemma 466: imported finite-height all-order Laguerre nonnegativity

## Hypotheses

Let Ξ(z)=ξ(1/2+iz) be the actual Riemann Xi function of L018. For real t and integer n≥0 put

D_n(Ξ;t)=[y^(2n)] Ξ(t+iy)Ξ(t−iy)
 = Σ_{j=0}^{2n} (−1)^(n+j) Ξ^(j)(t)Ξ^(2n−j)(t)/(j!(2n−j)!).

The coefficient is an entire Taylor coefficient in the complex variable y. This is the convention used in L255; L255's positivity result is not an input here.

## Conclusion

For every real t with |t|≤3·10^12−1/2 and every integer n≥0,

D_n(Ξ;t)≥0.

This includes the two interval endpoints and centers t at zeros of Ξ, with arbitrary multiplicity. It asserts nonnegativity only. No simplicity, external fixed-half-plane theorem or large-order tail onset is assumed.

## Proof

This is a specialization of two cited theorems, not an independent reproduction of their proofs.

Suvrit Sra, *On some positivity properties of the Riemann Xi function*, v1, 20 October 2026, [versioned primary PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf), Theorem 1.3, printed p. 3, states: if T>1/2 and every nontrivial zeta zero β+iγ with 0<γ≤T has β=1/2, then L_n(Ξ;x)≥0 for every integer n≥0 and |x|≤T−1/2. The theorem includes multiple central zeros; its relevant proof cases are Lemmas 4.1–4.2 and the proof of Theorem 1.3, printed pp. 9–11.

The source's (1.1), printed p. 1, defines the same ξ and Ξ as L018. Its (1.5), printed p. 2, defines L_n with coefficient (−1)^(n+j) binom(2n,j)/(2n)!. Since binom(2n,j)/(2n)!=1/(j!(2n−j)!), this is exactly D_n above. There is no rescaling of t or doubling of n. In particular n=0 is included. The cited theorem is stated for the unnormalized coefficients, including central zeros; applying it does not require division by Ξ(t). We import that multiplicity case from the source rather than infer it from L255's nonzero-center argument.

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to 3 times 10^12*, [arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1), Theorem 1, printed p. 2, verifies RH up to height H=3,000,175,332,800. Their Section 2, p. 2, explains the interval-arithmetic and Turing-method verification that counts all zeros in the range. Set T=3,000,000,000,000=3·10^12; then H−T=175,332,800>0. Consequently every nontrivial zero with 0<γ≤T is on the critical line. This is the zero hypothesis of Sra's theorem, and T>1/2. Substitution gives exactly the claimed closed interval and all n≥0. The source conclusion already includes negative x; no additional height assumption is required for negative centers.

The closed endpoints are part of Theorem 1.3, not a limiting extension of an open-interval assertion. In its proof, p. 11, the nonreal Xi zeros a+ib satisfy |a|>T and |b|<1/2. Thus for every |t|≤T−1/2, including equality, |t−a|≥|a|−|t|>1/2>|b|. This is the zero-exclusion condition of the source's Lemma 4.2. The negative endpoint obeys the same estimate.

For the central-multiplicity case, Lemmas 4.1–4.2, pp. 9–11, pass coefficients through locally uniform grouped products on compact complex y-disks, without dividing by the center value. The final paragraph of the theorem proof writes Ξ(z)=(z−t)^m g(z), g(t)≠0. Its product identity is Ξ(t+iy)Ξ(t−iy)=y^(2m)g(t+iy)g(t−iy). Accordingly the coefficients below m vanish, and those at n≥m are the source's nonnegative Laguerre coefficients of g at index n−m and center t; removing the real central factor preserves the nonreal-zero exclusion condition. This checks applicability at every central multiplicity, including n=0. No simplicity or strict-positivity conclusion is needed. These are checks of the cited proof cases, not a separate product theorem. ∎

Qualification: this is a citation-based import relying on Sra v1 Theorem 1.3 and the published computational theorem as mathematical inputs. The critical application audit of 25 October 2026 checked normalization, closed endpoints, coefficient limits and central multiplicities, and corrected an earlier erroneous decimal specialization T=3,000,000,000. The proof now uses T=3·10^12 consistently with its conclusion. This notebook has not independently audited Sra's full manuscript or rerun Platt–Trudgian's computation. No new mathematical discovery is claimed. The conclusion does not establish signs outside the interval, an effective overlap with C465a's existential onset, or global mixed positivity and RH.

## Mathlib

Not checked. Availability of a full matching theorem, including the certified finite-height premise and all-order central-zero conclusion, is unknown. No Mathlib formalization is asserted. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
