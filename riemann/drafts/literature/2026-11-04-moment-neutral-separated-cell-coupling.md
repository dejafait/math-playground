# Moment-neutral separated cells: completed source comparison

TARGET: Assess whether zero exponential moments permit a summable energy-normalized large-separation bound for the complete causal inter-cell coupling, retaining every prime-power shift.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 279 searched Weil separated-support/zero-exponential-moment coupling, Suzuki localized forms, Weil semiboundedness, and translated Weil Toeplitz sequences; then Wiener finite-measure atom detection. Read the mandatory October baseline and narrowly compared the support-enlargement, signed-pole, causal-realization and neutral-tail stops. No exact beta_m estimate was located; this bounded search does not establish novelty.
SOURCE_EVIDENCE: Suzuki 2206.03682v4, pinned PDF, Thm1.1(1)-(2), (1.2)-(1.3), complete Section2.2, Lemma2.1/proof and Sections3.1-3.5/Prop3.1; Suzuki 2606.09096v3 Thm1.1 and (2.5)-(2.10); Cuny-Eisner-Farkas BUW-IMACM18/22 (4 January 2019), Thm1.1 and Prop2.6(a)-(b)/complete proof. Reuse audited L740/L741 and Zhu Cor6.3 for local energy only. Precise links, version discrepancy and unread leads are recorded below.
COMPARISON: No inspected source supplies energy-normalized summable remote coupling. The full smooth Weil pairing has a zero-side representation; Wiener's theorem instead detects nondecay for Fourier coefficients of measures with atoms. This identifies an essential discrete-spectrum obstruction to test, even under RH, before seeking decay. Its neutral-cell specialization is not proved here.
GAP: Identify the complete large-window smooth causal pairing with the source Weil pairing, realize a nonzero neutral profile, and verify the finite atomic spectral measure and its lattice aliases under RH. No nonsummability, RH equivalence, unconditional lower witness or all-window bound is established by this comparison.
REASON: Park attempts to prove the summable upper bound until the newly located atom-detection obstruction has been tested. A bounded conditional lower-witness specialization is now concrete and independently testable; source theorem import is not a proof of that specialization. Historical stops remain qualified rather than global bans.
SCOPE: Source comparison for exactly the proposed beta_m; its definition and threshold below are unchanged. The separate next assessment covers only a conditional recurrence diagnostic, not a summable upper estimate, off-line-zero exclusion, global semiboundedness or positivity.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage was essential for the changed separation and moment constraints. This turn supplies it and changes the proposed direction; it does not repeat the ready finite-window audit.

## Original proposed test, preserved with no assertion of its truth

Put ell=log(3)/2. Let f and g be nonzero complex smooth functions
compactly supported in (0,ell), each satisfying both conditions

    integral_0^ell exp(x/2) f(x) dx = 0,
    integral_0^ell exp(-x/2) f(x) dx = 0,

and the same conditions for g. E_ell is the complete diagonal energy
identified in L741, whose strictly positive lower bound supplies the
denominator. For each integer m>=2 put L_m=(m+1)ell and let tau_m g
denote the translate of g into (m ell,(m+1)ell). Use L740's actual
generator on that encompassing interval and, initially only for these
smooth functions, set

    H_{L_m}(f,tau_m g)
      = -( <A_{L_m}f,tau_m g> + <f,A_{L_m}tau_m g> )/2,
    beta_m = sup |H_{L_m}(f,tau_m g)| / sqrt(E_ell(f) E_ell(g)).

This defines a question; no formula for beta_m or new estimate is
derived in step 278. The proposed intermediate threshold is
sum_{m>=2} beta_m < infinity with an explicit tail bound. The source
review must first decide whether this is a useful independent target
or simply conceals unknown zero-free control. It must retain all
continuous and prime-power contributions before taking an absolute
value. It may not assume that neutral moments cancel atomic errors,
that a smooth prime density equals the discrete measure, or that
an unweighted pointwise comb bound improves after projection.

Plausible downstream use: control the remote interactions of the
moment-neutral part in a spatial block argument. Even summability
would not prove the full block form positive. The two complementary
moment directions, their mixed terms, adjacent-cell interactions and
the required final margin would remain unresolved. No global sign
conclusion is part of the proposed intermediate target.

## Gate and discriminating test

Reuse the exact L740 and L741 inputs. Before proposing any new
arithmetic estimate, read the local baseline
2026-10-21-openai-quasi-rh-overlap.md and
../../foundations/2026-10-quasi-riemann-input.md as required by GOAL.md;
do not infer a stronger zero-free region from them. Compare narrowly
with 2026-10-30-weil-support-enlargement-coverage.md and
2026-10-30-weil-pole-resolvent-flux-coverage.md. The retained stops
are not global bans, but any overlap or equivalent positivity
requirement must be made explicit.

The next source review should locate primary theorem hypotheses for
the signed arithmetic coupling and its logarithmic energy normalization,
or document the uncovered difference. Continue to a separately gated
creative attempt only if an independently testable cancellation estimate
or rigorous lower-witness test is identifiable without assuming RH,
large-window positivity or unproved prime discrepancy. If the proposed
summability merely restates an unpaid zero-free assertion, or only an
already stopped absolute-mass bound is available, park this version.
No new mathematical script, lemma or certificate is authorized by this
nomination itself.

The potential creative obstruction is precise: local kappa<=1 does
not control accumulated remote prime-power couplings. A bounded later
attempt would test whether the two moment constraints materially change
the energy-normalized remote bound, or construct a rigorous obstruction
to that change, while retaining the actual arithmetic measure. This
would concern the central sign gap, rather than another audit of local
realization. Essential coverage is missing now. Mathlib coverage of
this proposed estimate is unchecked.

## Completed comparison, 4 November 2026, step 279

The main gap remains unconditional actual-Xi positivity. The proposed
intermediate threshold is still sum beta_m < infinity with an explicit
tail. Its possible downstream use is remote interaction control; the
complementary moment directions, adjacent blocks and final margin would
still be unpaid. No calculation of beta_m was performed in this turn.

### Primary inputs and their exact limits

[Suzuki, *Aspects of the screw function corresponding to the Riemann
zeta-function*, arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4),
Theorem 1.1, printed pp.1-2, gives the transform of Psi only for
Im(z)>1/2 and the zero expansion (1.3), including multiplicity and
nonreal ordinates. Section 2.2, p.7, uses Hadamard factorization and
absolute convergence before identifying transforms. Sections 3.1-3.5,
pp.9-11, give the compact-smooth Weil pairing, its derivative bridge
in Proposition 3.1 and its distributional interpretation. Lemma 2.1,
p.9, prevents a nonzero entire function of exponential type from
vanishing at all zero ordinates. Those complete short proof passages
were inspected. The PDF has arXiv stamp 30 May 2023 and internal date
31 May 2023; the served HTML instead displays 24 August 2026. Use the
pinned PDF, whose relevant statements and locators were cross-checked.

[Cuny, Eisner and Farkas, *Wiener's lemma along primes and other
subsequences*, BUW-IMACM 18/22, 4 January 2019](https://imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2018/imacm_18_22.pdf),
Theorem 1.1, printed p.1, concerns a **finite complex Borel measure**
mu on the unit circle, with muhat(n)=integral z^n dmu(z). It states

    lim (1/N) sum_{n=1}^N |muhat(n)|^2
        = sum_{a an atom} |mu({a})|^2.

The proof mechanism is explicit in Proposition 2.6(a)-(b), printed
pp.5-6: product-measure Fubini and dominated convergence, with the
ergodic case selecting coincident atoms. Both the complex-measure
case and the converse cases were read; PDF conjugation must be kept
despite text-extraction loss. No probability normalization, contraction
of the causal semigroup, or prime-indexed sampling theorem is needed.
This standard theorem is imported by citation, not reproved here.

[Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
Theorem 1.1 and Sections 2.3-2.5, retains all prime powers and the
polar and archimedean terms. Its localized lower bounds depend on
the interval; they are not global bounds or decay statements. Its
self-adjoint Weil operator must remain distinct from L740's causal
generator. L741's audited identity is at its stated finite window;
applying the smooth identity to encompassing intervals L_m still
requires checking the coefficients. No global temperedness assertion
or critical-line logarithmic-derivative multiplier is used here.

### Route comparison and unresolved specialization

These sources make a fixed-profile **lower-witness** diagnostic more
appropriate than starting with a uniform decaying majorant. Under RH
the zero-side pairing is a candidate source of an atomic spectral
measure; Wiener detects persistent coefficients if the complete cell
pairing really has that representation and an atom survives. This is
a proposed application, not a derivation of it or a counterexample.
The conditional assumption RH may be used only for this diagnostic,
never as an input to unconditional positivity. Such a conditional
failure, if proved, would challenge the chosen sufficient decay
mechanism even in its intended favorable case; it would not disprove RH.

The required local checks are precise: smooth neutral-profile existence,
the full geometric-to-zero-side normalization on each L_m, convergence
of the smoothed zero measure, and aggregation of all ordinates having
the same lattice phase. One cannot assume distinct phases, omit any
prime-power contribution, or apply Wiener to off-unit-circle phases
when RH is not assumed. No choice of a rightmost zero is authorized.
The conditional diagnostic is nominated in the separate
[lower-witness assessment](2026-11-04-neutral-cell-wiener-lower-witness.md).
It needs a separate approval next turn. No new lemma is established.

The mandatory [October baseline](2026-10-21-openai-quasi-rh-overlap.md)
and [external register](../../foundations/2026-10-quasi-riemann-input.md)
do not supply this recurrence specialization or eliminate possible
off-line zeros. No classical estimate is treated as a present barrier
to the newer fixed-half-plane inputs. The support-enlargement and
signed-pole comparisons concern respectively eigenvalue-relative
crossing and a resolvent numerator; they do not test this discrete
translation question. The neutral-tail stop concerns a different
Selberg-Mobius unit-ball normalization. Realization, composition and
square-order stops are preserved without repeating their audits.

### Searches, unread leads and decision threshold

Queries included “Weil form separated supports zero exponential
moments prime sums off diagonal coupling”, “Suzuki Weil quadratic
form semibounded Riemann hypothesis lower bound exponential moments”,
“Weil exponential moments summable”, “Weil off-diagonal neutral”,
“Weil form translated test functions almost periodic zeros coupling
Riemann hypothesis”, and “Wiener lemma Fourier coefficients complex
measure circle sum atoms squared theorem pdf”. Exact moment-neutral
queries often returned unrelated results; those are not evidence of
absence. No covering beta_m theorem was found in the inspected sources.

Bergen, *The Truncated Weil Form as a Toeplitz Sequence*, IMM Paper 14,
[DOI 10.5281/zenodo.20684022](https://doi.org/10.5281/zenodo.20684022),
was located through a secondary bibliographic record. Its claimed
box-basis boundedness/RH equivalence is an **unread lead**, not an
import or verified duplicate. The primary record, DOI and record API
were inaccessible. That source is nonessential to the independently
available Suzuki/Wiener diagnostic and is parked; no further access
retry is scheduled. A search snippet about a semibounded criterion
also supplies no inspected theorem and is not used.

Continue with the separately gated conditional diagnostic only if the
complete fixed-profile pairing and a nonzero atomic coefficient can
be justified. A proved positive Cesaro mean square parks the original
summable-beta route in that conditional scope. If the representation
or surviving atom fails, record the failure instead of claiming
nonsummability; a new decay attempt requires a refined mechanism and
its own gate. Unconditional beta_m behavior remains open. Matching
Mathlib coverage of the new specialization is unchecked. This is
source-level route evidence, not progress beyond the cited mathematics.
