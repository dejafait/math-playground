# Shifted Gaussian primitive evaluation: source review1572

18 November 2026. Literature only, for the exact TARGET in assessment1571.
No shifted formula, remainder bound or new lemma is proved here. This
is local source coverage, not mathematics beyond the checked sources.

## Purpose and bounded decision

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The intermediate target is sharper C032m E/O evaluation for unchanged
dictionary1570, uniformly in sigma in[1,2], without zero coordinates.
Downstream this could enable the fixed variation2 certificate test;
it supplies neither full cancellation nor unsmoothed realization.

Read C032m's complete proof, C032q's definitions/cone interface,
C032t's exact-formula/differentiation sections, assessment1570,
source-notes1555, calculation1571 and targeted stop/history1571 passages.
The old bound above999/1000 missed the required residual below1/2.
Its box optimum is not an actual-kernel lower bound. Its disk tail
below10^-100 does not pay the primitive/finite-divisor uncertainty.
Those recorded conclusions were reused, not recomputed or audited.

Continue if general source coverage leaves an explicit application
to prove; stop an unsuccessful specialization at its precise failing
interchange or effective estimate. Do not increase dictionary size,
frequency, order, variation budget or grids in response. No inspected
source already supplies the requested effective evaluator.

## Primary statements and essential source cases

**Chirre and Goncalves.** *Bounding the log-derivative of the
zeta-function*, Math. Z.300(2022), 1041-1053,
[Proposition5, p.1044](https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf).
Read the whole proposition and Fourier convention in publisher PDF and
article text. It requires even analytic h on
|Im z|<=1/2+epsilon, epsilon>0, with
|h(z)|=O((1+|z|)^(-1-delta)), delta>0, in the strip.
It does not require real values on R or RH. It sums
h((rho-1/2)/i) over complex nontrivial zeros, retaining the gamma
integral, pole evaluations combined by evenness, log(pi) correction
and every prime power. Its Fourier convention is exp(-2*pi*i*x*y).
It cites reference4, Lemma8; no separate proof is given there.
RH-dependent estimates elsewhere are not imported. This is a general
identity, not a uniform error theorem for the present primitives.

**Carneiro, Chirre and Milinovich.** *Bandlimited approximations and
estimates for the Riemann zeta-function*,
[arXiv:1710.10362v1, 28 October2017](https://arxiv.org/html/1710.10362v1#S2),
Lemma8, printed pp.9-10. Read the whole statement and citation proof.
It has the strip-decay hypotheses and additionally requires real
values on R; both Fourier signs and both pole evaluations remain.
Its full proof cites Goldston-Gonek Lemma1 and Iwaniec-Kowalski
Theorem5.12. Those upstream proofs were not newly read. A future
application must check reality or use Proposition5 as stated.

**Connes.** *Heat Expansion and Zeta*,
[arXiv:2402.13082v1, 20 February2024, author PDF](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
Section2, equations(4)-(9), printed p.4. Read all Mellin hypotheses
and those formulas: smooth f on positive reals, O(x^delta) at zero,
O(x^(-1-delta)) at infinity, some delta>0. Equation(5) uses complex
zeros, both pole integrals and all local terms. Equations(7)/(9)
keep subtraction inside the archimedean integral, before/after
F=x^(1/2)f. The Gaussian transform(13), p.5, and previously inspected
subtraction, remainder and prime cases in Sections3-4 are covered by
notes1555. The spectral rewriting(11) assumes RH and is excluded.
An unshifted asymptotic remainder is not an effective shifted-primitive
bound; no differentiated or shifted remainder is imported.

For integration reuse Haslinger, *Complex Analysis*, Theorem2.39,
pp.67-68, [primary text](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
whose complete statement/proof coverage is retained in C032m.
Each parameter disk needs an integrable holomorphic-integrand majorant.
C032m checks that requirement for its original R, not for new
prime-side terms or arbitrary transformations of its spatial integral.

## Remaining specialization obligations (not proved here)

The sources settle availability of an unconditional general identity.
They do not make evaluation effective automatically. Research must:

1. Specify the even zero-variable tests and prefactors for the shifted
   Gaussian. Check strip decay uniformly in width and along needed
   primitive paths, with neighborhoods when differentiating. Use
   C032m's normalization and preserve multiplicity, positive-ordinate
   pairing and the zero-ordinate exclusion. Real-valuedness must be
   checked when choosing the Lemma8 version.
2. Justify each exchange for zero sums, prime sums and the subtracted
   archimedean integral. A fixed-shift Gaussian envelope need not
   dominate integration over the whole spatial half-line. Do not
   separate divergent subtraction terms or add trivial zeros already
   accounted for by the gamma contribution.
3. Recover E/O with zero initial values and the exact removable
   quotient at w=+/-ix, including the origin and imaginary-axis
   primitive paths. A principal value would be a different integral.
   C032m's qualitative tail limit supplies no computable tail rate.
4. Produce evaluable uniform errors for discarded prime powers,
   archimedean tails, noncompact primitive tails and finite numerical
   approximations; state cutoffs for which those errors tend to zero.
   Existential constants and differentiated asymptotics do not suffice.
   Large cancellation between known terms requires absolute precision.
5. Leave another minimax solve for a later concrete target. Any final
   certificate still pays coefficient amplification and covers all
   closed width cells. An evaluator alone proves neither residual<1/2
   nor an actual-dictionary obstruction.

Hence SPECIALIZE is justified for a bounded analytic attempt importing
the exact identity and existing integration tools. Reproving the general
explicit formula would add no needed input. Effective uniform primitive
bounds remain unproved; success and computational practicality are unknown.

## Search, duplicates, access and limits

Queries: `"Gaussian" "explicit formula" "shifted" zeros rigorous
computation`; `"Guinand" "Weil" "Gaussian" "error" computation zeros`;
the exact Chirre-Goncalves title with `"Proposition 5"`;
`"Guinand" "Gaussian" "primitive" zeta explicit formula`;
`"Gaussian" "explicit formula" "interval arithmetic" zeta`;
`"smoothed" "zero" "Gaussian" "Guinand" error bounds`.
Snippets, numerical examples and repository claims were leads only.
Additional numerical trace-formula and twisted-Gaussian prime-sum
leads remain unread and are not essential inputs to the proposed
application of the inspected exact identity. No failed search establishes
novelty or absence of a theorem.

Narrow local searches covered discovery-notes1570, audit-notes1557 and
stop/history1571. Generic separation/discretization coverage is reused
through assessment1570; first-odd and finite-width stops retain their
scopes. No sibling proof was read. The d-nb mirror timed out; the
publisher supplied Proposition5. Shell DNS retrieval of Connes failed;
the web tool supplied the source theorem/formulas and page renders.
Neither failure is a remaining source blocker.

Retain C032m/q and calculation1571's actual-divisor, multiplicity,
strip/counting, zero-ordinate exclusion, through100 finite-zero,
first-zero/tail, heat and fixed-v1 qualifications. The standard formula
does not independently certify these other inputs. No unprovided zero
coordinates, density, moments or global profile signs are introduced.
Full matching Mathlib coverage is unchecked/unknown. Full J_eta=0,
unrestricted variation, positive output, H_d=o(d), S_F=0 and unsmoothed
Xi realization remain open. No complete candidate is asserted.
