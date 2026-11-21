# Gaussian explicit-formula source comparison1555

18 November 2026. Literature only, for the exact target in assessment1554.
This records source coverage, not a new formula, sign proof or independent
audit of C032s. No lemma or mathematical script is changed.

## Primary statements and proof cases inspected

Andres Chirre and Felipe Goncalves, *Bounding the log-derivative of the
zeta-function*, Math. Z. 300 (2022), 1041–1053,
[Proposition5](https://link.springer.com/article/10.1007/s00209-021-02820-9).
Read the full statement and Fourier convention. For an even h analytic
on |Im z|<=1/2+epsilon with decay O((1+|z|)^(-1-delta)), epsilon,delta>0,
it states

    sum_rho h((rho-1/2)/i)
      = 2*h(i/2) - log(pi)*hat(h)(0)/(2*pi)
        + integral_R h(r)*Re psi(1/4+i*r/2) dr/(2*pi)
        - sum_(n>=2) Lambda(n)*hat(h)(log(n)/(2*pi))/(pi*sqrt(n)),
    hat(h)(y)=integral_R h(r)*exp(-2*pi*i*r*y) dr.

The zeros here are all nontrivial zeros, including complex ordinates;
RH is not a hypothesis of this proposition. Other estimates in the
paper assume RH and are not inputs. Its reference4 points to Lemma8
of Carneiro–Chirre–Milinovich.

E. Carneiro, A. Chirre and M. B. Milinovich, *Bandlimited approximations
and estimates for the Riemann zeta-function*,
[arXiv:1710.10362v1, 28 October2017](https://arxiv.org/pdf/1710.10362),
Lemma8, printed pp9–10: read the entire statement and its citation proof.
It includes both pole evaluations, both Fourier signs in the prime
sum, the gamma integral and -log(pi) term. It additionally states
real-valuedness on the real axis. The proof cites Goldston–Gonek Lemma1
and Iwaniec–Kowalski Theorem5.12; their proofs were not newly read.
The publisher URL found first served only a one-page abstract; the
arXiv v1 above supplied the theorem. Do not conflate versions.

Nicholas G. Polson, *On Hilbert's 8th Problem*,
[arXiv:1708.02653v24, 11 September2026](https://arxiv.org/html/1708.02653v24),
Section4.3/(3), Definition5.1, Lemma5.2, Theorem5.4/(7), Corollary5.5,
Lemmas6.1–6.2: read statements and complete proofs in those ranges.
Here W is the half-sum over all zeros and

    W(u)=exp(u/4)+A(u)-P(u),
    A(u)=integral_R exp(-u*r^2)*m(r) dr/(4*pi),
    m(r)=Re psi(1/4+i*r/2)-log(pi),
    P(u)=sum_(n>=2) Lambda(n)*exp(-(log n)^2/(4*u))
                          /(2*sqrt(pi*u)*sqrt(n)).

The contour proof separates rational residues, gamma terms and prime
terms; it shifts each prime term before summing, not the divergent
critical-line Dirichlet series. Lemma5.2 uses counting and Gaussian
domination for complex-zero differentiation. Lemma6.2 bounds P and its
first three derivatives for 0<u<=1/100 by
100*u^(-k-1/2)*exp(-kappa/u), kappa=(log2)^2/8. Its proof controls the
four derivative polynomials and a convergent n^(-7) tail. Lemma6.1's
digamma proof separates the Binet integral at r/4. These are preprint
inputs, not independently certified constants. Corollary5.5 is an
asymptotic, not the requested weighted sign theorem.

Alain Connes, *Heat Expansion and Zeta*,
[arXiv:2402.13082v1, 20 February2024, author PDF](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
Section2/(4)–(12), pp4; Section3/(13)–(24), pp5–8; Section4/(25), p8.
Read the Mellin hypotheses, exact archimedean regularization, Gaussian
transform, subtraction argument, Taylor remainder proof and complete
prime estimate. Theorem1.1 and the real-spectrum reading assume RH;
only the analytic input formulas are relevant here. The regularized
kernel is

    r(x)=exp(x/2)/(exp(x)-exp(-x))-1/(2*x),

with removable value 1/4 at zero (Lemma3.1). Equation(17) keeps the
subtracted integral on (0,2), the full r integral and the tail (2,infinity).
Equation(25) includes all prime powers. Its bound on the undifferentiated
prime contribution does not bound its derivative. Lemma3.2's remainder
constants are existential, so no compact numerical sign follows by
truncating its asymptotic series.

## Applicability and work that remains

C032j's z_rho=(rho-1/2)/i and multiplicity convention match the explicit
formula. Pairing rho with 1-rho and using evenness identifies the
all-zero sum with twice C032j's positive-ordinate sum. Off-line zeros
at one positive ordinate still contribute separately; do not divide
those conjugate contributions again. C032j's exclusion of ordinate
zero is retained. Thus Polson's W normalization matches local H;
Connes's all-zero spectral normalization has twice that mass.

The elementary Gaussian transform needed for this specialization is
already displayed in Polson Theorem5.4's proof and Connes(13), with
their distinct Fourier conventions. Use one convention consistently.
The gamma contribution already accounts for trivial zeros. An added
trivial-zero series would double count them; the evaluations at +/-i/2
must also remain present. No prime-term sign after weighting or
differentiation has been proved in this review.

For analytic differentiation reuse Haslinger, *Complex Analysis*,
Theorem2.39, pp67–68, [primary PDF](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
whose full statement/proof coverage is recorded in assessment1536's
separate approval1537 and C032m's source paragraph. It requires an
integrable dominator on each parameter disk and then permits
differentiation under the integral. This is coverage of the tool, not
a dominator for the new integrands. Research must verify the actual
zero-sum, gamma-integral and prime-series hypotheses uniformly on a
neighborhood of [1/10000,1/200]. Alternatively it may apply the cited
explicit formula directly to the required polynomial-Gaussian test,
checking its strip hypotheses and transform. No differentiation of
an asymptotic remainder or extension of an existential constant is
licensed. Exact effective bounds for the weighted expression are
the remaining mathematical task, not an essential unread source.

## Search, overlap and decision

Queries included `Riemann zeros Gaussian explicit formula heat trace
monotonicity sqrt t`, `Guinand Weil explicit formula Gaussian test
function gamma logarithmic derivative theorem`, `Connes heat trace
zeta zeros small time asymptotic Gaussian explicit formula`,
`"sqrt" "heat trace" "zeta" monotonicity`,
`"Riemann" "heat trace" "monotonicity"`, the exact bandlimited paper
title, and `"Polson" "2026" "Corollary 5.5"`.
No inspected matching weighted-monotonicity theorem was found; that
is not evidence of novelty. A GitHub summary for *computing_rh* claims
derivative signs of H; the underlying book/proofs were not inspected
and are not inputs or a source of the required weighted sign.

Read C032j and the full C032s proof, assessment1552/source-notes1552,
attempt1554 and history1554. Narrow searches in Levy/heat/032/Sra
assessment and attempt paths found no prior inspected Connes/Guinand
comparison closing this target. No sibling notebook was read.
C032s's counting envelope fails as recorded; the formula decomposition
offers different cancellation information without erasing that stop.
H>=0 and H'<=0, even if imported, are not a matching statement about
(sqrt(u)*H(u))'. The reverse-order and full-cancellation stops persist.

DECISION SPECIALIZE: import the named exact formulas and covered
analytic tools, then attempt only the missing uniform weighted sign.
Do not reprove Guinand–Weil. Any new archimedean inequality must be
proved explicitly as the identified specialization, with all pole,
prime and remainder terms included. A uniform strict negative bound
on the closed interval passes; a positive K' refutes only this sufficient
test. A failed bound or grid decides neither K' nor D. Refuting actual
density ordering requires a rigorously negative D in C032s(3).

This closes essential source coverage, not the sign or main gap.
Full matching Mathlib coverage remains unknown and was not checked.
No central creative continuation follows from these source identities:
they do not supply full J_eta cancellation or Xi realization.
