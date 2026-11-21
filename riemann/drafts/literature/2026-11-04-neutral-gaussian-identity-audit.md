# Source coverage: conceptual audit of the Gaussian identity

TARGET: Critically audit L753's complex neutral Gaussian identity on each fixed [0,T], checking reflected conjugation, both poles, Fourier normalization, complete zero/gamma/prime-power majorants and two right derivatives at zero before any sign use.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-statement/stronger-result searches and duplicate comparison in 2026-11-04-neutral-gaussian-flow-discovery.md and the ready domain-differentiation assessment; searched the Gaussian assessments/history and fixed-sine stop, then read L753 in full and the relevant L018/L024/L744 statements and proof ranges.
SOURCE_EVIDENCE: Directly read https://arxiv.org/html/2403.17803v1#S2.SS2 Lemma 4 and its proof attribution, Section 2.1 Fourier convention; https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf printed pp.128-130, Proposition 5.3/Theorem 5.4 and proofs (revision 2014-06-18); https://dlmf.nist.gov/5.11.E2 and https://dlmf.nist.gov/5.11#ii sector condition and complex remainder paragraph, all on 2026-11-04.
COMPARISON: The unconditional strip formula, Schwartz heat theorem and digamma remainder cover the named external inputs; they do not certify L753's particular weighted moments, reflected-conjugate square, Fourier scaling or complete differentiated majorants. Those are the bounded later audit obligations, not new source prerequisites.
GAP: Independent verification of every applicability step in L753 remains; source coverage is adequate for that audit, but no sign, unbounded-time control or uniformity over initial data is covered.
REASON: Audit the written analytic bridge before relying on it in a prospective differential sign mechanism; import the standard theorems and scrutinize their specialization rather than reprove them or approve L753 from its own conclusion.
SCOPE: Conceptual audit of L753 only, for fixed compact complex f satisfying both exact exponential moment conditions and fixed finite T>0, with right derivatives at zero; no new sign derivation, positivity import or finite-window generator extension.
COVERED_TARGET: Assess coverage for a critical audit of L753's complex neutral Gaussian identity, checking reflected conjugation, both poles, full prime-power domination and two right derivatives at zero before any sign use.
LITERATURE_REASON: The newly written L753 proof requires separate audit-scope approval; reuse existing discovery and inspect the primary normalization, endpoint and gamma hypotheses needed for this concrete proof, without renewed sign-route discovery.

## Completed source comparison, step 328

The COVERED_TARGET records the exact coverage question at invocation.
The TARGET now names its single mathematical continuation. This review
approves source scope only; it performs no independent proof audit and
establishes no new lemma. The honest outcome is literature EXPLORATION,
not a mathematical advance or an informative sign obstruction.

The main gap is unconditional complete neutral Weil positivity. The
intermediate target is validation of L753's identity and differentiated
limits, potentially usable in a later differential comparison. An
independent starting sign and a useful backward comparison remain open.

### Primary statements and essential proof cases actually read

1. E. Carneiro and M. B. Milinovich, *On Littlewood's estimate for the
   modulus of the zeta function on the critical line*,
   [arXiv:2403.17803v1](https://arxiv.org/html/2403.17803v1#S2.SS2),
   26 March 2024, Section 2.2 Lemma 4. The full statement assumes
   analyticity on |Im z|<=1/2+epsilon and uniform decay
   O((1+|z|)^(-1-delta)), with epsilon,delta>0. It imposes no
   evenness or RH hypothesis. Read both pole evaluations, the complex
   ordinates, gamma/scalar terms and infinite von Mangoldt sum. Section
   2.1 uses exp(-2pi i x xi). The entire printed proof is an attribution
   to Iwaniec--Kowalski, *Analytic Number Theory* (2004), Theorem 5.12;
   that book proof remains unread. Import Lemma 4 itself. The neighboring
   RH-dependent Lemma 5 supplies no input. L753 Sections 2 and 4 must
   still satisfy this theorem's strip and normalization conditions.

2. J. K. Hunter, *Notes on Partial Differential Equations*,
   [revision 18 June 2014](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf#page=134),
   printed pp.128-130 (PDF pages 134-136). Read the endpoint convention,
   Proposition 5.3 and Theorem 5.4 with their full proofs: seminorm
   difference quotients, the Fourier ODE, induction in time derivatives
   and Gaussian inversion. Schwartz data give smooth Schwartz-valued
   evolution up to zero, multiplier exp(-t|k|^2) and the normalized heat
   kernel. The initial setup is real; L753 explicitly applies it to
   real and imaginary parts. The source gives no exponential-weight
   endpoint theorem and no Weil-form contraction. L753 Sections 1 and
   3 must supply the weighted and arithmetic applicability work.

3. NIST [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) and
   [5.11(ii)](https://dlmf.nist.gov/5.11#ii), accessed 4 November 2026.
   Read the sector |arg z|<=pi-delta, the digamma expansion, and the
   complex remainder paragraph: the first omitted term is multiplied
   by sec^(2n+1)(arg z/2). This covers the cited type of input in
   L744(8). The later audit needs only its logarithmic growth bound,
   including bounded frequencies, rather than a new effective estimate.

### Exact audit obligations and source limits

The following are checks of already written claims, not derivations
performed or accepted here:

- L753(5)-(8): weighted continuity and differentiated Fubini, including
  zero; Hunter's unweighted theorem alone cannot pay these steps.
- L753(9)-(11): holomorphic reflected conjugation at complex ordinates,
  both pole products and derivatives, and uniform strip bounds.
- L753(12)-(16): doubled heat time, spatial derivative factors and a
  summable majorant for every prime power, uniformly down to zero.
- L753(17)-(18) and final comparison: all Fourier constants and signs,
  real-valuedness, translation and compact initial normalization.

The source formula has no finite arithmetic cutoff. It is applicable
only after the test satisfies its hypotheses; its citation cannot
replace verification of the displayed local bounds or differentiated
interchanges. Standard Fourier inversion/convolution, Gaussian
integration, dominated convergence and the fundamental theorem of
calculus are the permitted named elementary inputs. No reproof of the
explicit formula or heat theorem is needed. No essential source is
blocked; no new discovery search is justified by this unchanged family.

## Inputs, duplicate checks and decision test

Use L753 in full, L018's zero correspondence and symmetry, L024's
reciprocal-square summability, and L744(6) only for the compact
initial normalization (L744(8) also supplies its gamma growth bound).
The prior SPECIALIZE assessment is
`drafts/literature/2026-11-04-neutral-gaussian-domain-differentiation.md`;
the original source comparison is
`drafts/literature/2026-11-04-neutral-gaussian-flow-discovery.md`.

L753's full text and L744 through (8), plus L018 and L024, were read for
this scope comparison. Reuse the discovery assessment's documented
distinction from Xi deformation, causal L740 and RH-dependent Suzuki
norm identities. Step 327 contains the local specialization, not its
independent audit; the domain assessment and step 326 cover its inputs,
not an independent verification of the new write-up. No duplicate
completed L753 audit was located in the targeted Gaussian records.

The source-coverage discriminator is met: the named external inputs are
accessible and cover the hypotheses needed to scrutinize every listed
claim. SPECIALIZE authorizes a separate REPRODUCTION conceptual audit.
The later audit succeeds only if all j=0,1,2 bounds and interchanges hold
on [0,T] without an unpaid tail or pole. On failure, preserve the exact
counterestimate or missing hypothesis and repair or narrow L753 before
sign use. Do not substitute a compact positive-time cutoff, ordinary L2
contraction, or real-zero assumption. No mathematics is audited here.

This is not renewed discovery and does not claim new mathematics.
The independent starting sign and useful backward comparison remain
unresolved. Preserve the L751/L752 absorption stop. No justified
creative sign target is nominated merely to satisfy routing cadence.
Full matching Mathlib coverage remains unchecked.

## Preserved request history

Step 327 created this file as REVIEW_REQUIRED with the COVERED_TARGET
above. Step 328 completed that separate source comparison and nominated
the TARGET audit. The prior derivation and its unaudited status are
preserved; this change is not a sign result or a certification of L753.
