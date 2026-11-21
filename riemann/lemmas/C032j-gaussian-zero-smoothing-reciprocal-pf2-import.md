# Corollary C032j: Gaussian zero smoothing loses reciprocal PF2 (cited result)

## Hypotheses

Use the actual completion Ξ(z)=ξ(1/2+iz) of L018. Let Z+ be the
multiset of nontrivial zeta zeros ρ=β+iγ with γ>0, counting
multiplicity, and put zρ=γ-i(β-1/2). Fix σ>0 and set

    Gσ(w)=(4πσ)^(-1/2) exp(-w²/(4σ)),
    pσ(x)=(1/2) Σ_(ρ∈Z+) [Gσ(x-zρ)+Gσ(x+zρ)],
    H(t)=Σ_(ρ∈Z+) exp(-t zρ²),
    Hσ(t)=∫_R exp(-t x²)pσ(x) dx,
    ℓσ(t)=Hσ(t)/t,
    Bσ(s)=∫_0^∞ (1-exp(-st))ℓσ(t) dt,   s≥0.

The external mathematical inputs are Sra's two fixed-v1 preprints
cited below, applied to the actual zeta zeros, including their proved
finite-zero and zero-counting inputs. No hypothesis that all zρ are
real, that H is completely monotone, or that pσ is nonnegative is made.
The variance of Gσ on R is 2σ; σ is its half-variance, not its standard
deviation. Here Bσ is the exponent of the smoothed laws, not the
unsmoothed logarithm log(ξ(1/2+√s)/ξ(1/2)).

## Conclusion

The source constructions define a probability law νσ on [0,∞) with
Laplace transform exp(-Bσ(s)), and a probability law μσ on R with
characteristic function exp(-Bσ(ω²)). For every c>0,

    ∫_[0,∞) exp(cu) dνσ(u)=∞,
    ∫_R exp(c|x|) dμσ(x)=∞.

Neither measure admits a log-concave probability density; neither
admits a Pólya frequency density of any integer order m≥2. The
one-sided density convention, if a density is considered, is zero
extension to the negative half-line. These conclusions hold for every
σ>0. They do not assert that a density exists for either law.

This prevents using these laws as a PF2-preserving replacement for
the unsmoothed reciprocal laws. It does not exclude signed corrections,
other transforms, or every transfer to L030; it proves no sign for the
unsmoothed Q in L030-L032/C032a.

## Proof

This is a citation-based application, not a reproof of the tail or
probability-law arguments. The primary result is Suvrit Sra,
*Some positivity properties of Riemann Xi under smoothing*,
[hexagon:2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1),
first release 11 November 2026, Theorem 4.1 and its full proof,
printed p.9. The definitions are (1.1), Definition 2.1, (2.2) and
Section 4 (printed pp.2–3,9). Check its hypotheses as follows.

1. L018 gives precisely the source normalization and the map
   ρ↦zρ, preserving multiplicities. For positive ordinates Re(zρ)>0,
   so this selects one member of each ± pair in L024. A pair off the
   line with common positive ordinate contributes both zρ and its
   conjugate, with their own multiplicities. There is no extra
   halving of those two terms. The factor 1/2 is exactly the factor
   in source (1.1); it accounts for the two translates ±zρ. The
   source's actual-zero inputs also exclude ordinate zero.
2. Gσ is the source's Gaussian in Section 3.1, printed p.5.
   It is entire, even, real on R and a probability density there.
   Its complex modulus is
   |Gσ(x+iy)|=exp(y²/(4σ))Gσ(x). Consequently it obeys
   Definition 2.1's bound Cσ(Y)/(1+x²)² on each |y|≤Y:
   one can take Cσ(Y)=exp(Y²/(4σ)) sup_x (1+x²)²Gσ(x),
   which is finite by Gaussian decay. This elementary substitution
   checks admissibility; it is not a new smoothing estimate.
3. Import H(t)>0 for all t>0 from Sra,
   *On some positivity properties of the Riemann Xi function*,
   [hexagon:2610.00584v1](https://hexagonmath.org/pdf/2610.00584v1),
   first release 20 October 2026, Theorem 1.1, printed p.2.
   Its H in (1.2) is the sum defined here, with precisely Z+ and zρ
   above. Its finite-zero input is verification through height 100
   and a retained real zero with ordinate in (14,15), together with
   its stated strip/counting inputs (Section 2.1, printed p.3).
   This theorem is imported as published in the preprint; the
   retained-zero proof coverage in assessment884 is reused, without
   claiming fresh verification of those external inputs.
4. Proposition 3.1, equations (3.2)–(3.3), of the smoothing preprint,
   printed pp.5–6, supplies, for t>0,

       Hσ(t)=H(t/(1+4σt))/√(1+4σt)>0.

   Thus both Hσ≥0 and Hσ not identically zero in Theorem 4.1 hold.
   The last sentence of that theorem's proof also gives
   pσ(0)=H(1/(4σ))/√(4πσ)>0, consistently with this normalization.
   We do not replace Hσ≥0 by the stronger unproved pσ≥0.
5. The sums, integrals and laws here are the ones constructed in
   the smoothing source: Lemma A.4 (printed pp.13–14) provides
   convergence and the entire profile; Proposition A.7 and its
   hypotheses/proof (printed pp.16–17) provide the Bernstein
   exponent with Lévy density ℓσ and no drift or killing.
   Section 4 defines νσ as Law(Sσ), E exp(-sSσ)=exp(-Bσ(s)),
   and μσ as Law(√(2Sσ)G), with independent standard normal G.
   These are not assumed to be the unsmoothed reciprocal laws.

All hypotheses of the admissible-kernel case of Theorem 4.1 now
match. Apply its two exponential-moment conclusions and its
log-concavity/PFm conclusions directly. No limiting operation at
σ=0, uniform width bound, numerical certificate or new asymptotic
calculation is needed. In particular no conclusion about the
unsmoothed endpoint follows from this import. ∎

The theorem and prerequisite positivity are preprint inputs. This
checks their applicability, not their source-wide correctness or an
independent verification of their proofs. The full relevant statement
and proof of Theorem 4.1 were inspected; no stronger conclusion from
a later version is substituted. Independent initialization, singular
contacts, identification, realization and all-degree signs remain open.

## Mathlib

Full matching coverage has not been checked and is unknown. No
Mathlib theorem is used as a substitute for either cited preprint.
Supporting Gaussian/probability APIs have not been assessed here.
