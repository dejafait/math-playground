# A different one-sided loss test — source nomination1164

TARGET: Assess source coverage for the negative-symbol compression test ||Q N_- Q||<beta at C750m's fixed b,T,P64, with N_- defined from (beta-Psi)_+ and the full odd pole.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1165 completes the exact-target/terminology search and primary comparison below, reusing1160/1162 and the793/789/806/821 failure comparisons. No inspected theorem supplies the fixed joint clipped-symbol bound; no novelty inference. Queries and primary leads are recorded in 2026-11-16-sine64-negative-symbol-source-working-1165.md.
SOURCE_EVIDENCE: Zhu2608.24827v2 Theorem1.1/(4), Lemma3.1, Lemma6.1/proof/following paragraph and11.1/(16), https://arxiv.org/html/2608.24827v2 ; Teschl GSM99 2009 Theorem3.1/(3.20)-(3.21), pp90-91, and Section6.3 pp139-141, Lemmas6.9/6.10, Corollary6.11/(6.21), https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf . Contrast Israel-Mayeli2301.09616v2 Theorems1.1/1.4 and Nicola-Tilli2207.08624v2 Theorem1.1/(1.3), as detailed below.
COMPARISON: Standard bounded-symbol order and complete squared-kernel machinery cover a later specialization on the unchanged H,Q. Neither they nor the stronger concentration results certify its constant. The symmetric stop is inapplicable to this one-sided loss; unweighted spectral projectors and Gaussian-window localization do not identify its prescribed compression.
GAP: Ready source machinery leaves the local order specialization, actual projected kernel, complete quantitative enclosure or decisive lower witness, and strict comparison with beta to one later mathematical attempt. No norm, inequality for R, complement floor, coupling or head sign is established1165.
REASON: A bounded source review admits a concrete standard-method test without an unknown inverse or external spectral floor. Completed1165 is literature-only EXPLORATION/REPRODUCTION; the newly ready continuation requires the supervisor's separate approval before execution.
LITERATURE_REASON: The new target introduces a nonlinear negative-part Fourier multiplier and its compression, outside the earlier SPECIALIZE gate for the full symmetric K norm; exact source scope and complete quantitative bounds need separate review.
SCOPE: Fixed b=log101/2, T=2pi exp(A+2), beta=2-1/T, all35 prime powers, arbitrary complex H, unchanged P64 and Q. No spectrum sweep, changed support, changed cutoff, new head assembly, source floor or RH premise.
COVERED_TARGET: Test whether ||Q N_- Q||<beta at C750m's fixed b,T,P64 using a complete projected-kernel enclosure or a rigorous complementary lower witness, retaining the joint clipped comb and full odd pole.

## Exact proposed object and source test

Use C750m's notation, including its negative Fourier convention, and
s(x)=sinh(x/2). The proposed N_- is specified by the quadratic expression

    integral_(-T)^T max{beta-Psi(t),0}|F_f(t)|^2 dt/(2pi)
        +2|<f,s>|^2.

This defines the object to assess, not a proved estimate or a new lemma.
It must not be confused with the spectral negative part of K, nor may
a nonlinear positive-part operation be assumed to commute with spatial
compression. Retain the full jointly evaluated prime comb inside Psi;
replacing it with A before taking the positive part would be a different,
unapproved loss. Both parities and complex coefficients remain required.

The proposed mathematical threshold after source approval is a rigorous
complete upper bound nu for ||Q N_- Q|| with nu<beta. First the review
must check the claimed operator-order route from this loss to a lower
bound on QRQ, and identify a complete, computable compression estimate
that does not silently omit sine modes or Fourier tails. No such route
is proved here. Search the exact statement, standard negative-part
multiplier terminology, stronger results and known obstructions; inspect
the necessary primary theorem hypotheses and proof cases. Reuse the
audited full endpoint/core/kernel and normalization where applicable.

Continue to one separately gated mathematical attempt only if that
comparison can be made precise without an unknown spectral floor or
inverse. A matching known theorem should be imported, not rederived.
A future proved lower witness >=beta would stop this loss certificate;
an upper estimate >=beta alone would only fail to certify it. An
inconclusive enclosure must retain that distinction. Do not increase64,
change T, assemble the finite head or infer that the original form has a
negative direction. No new mathematical test on N_- was executed1164.

## Three mechanisms compared

1. The full symmetric ||QKQ|| budget is now audited and stopped by
   C750m(4)-(5). Sharper symmetric tails or a new finite head cannot
   change its exact positive witness. This mechanism is retired.
2. A signed resolvent or energy-weighted Schur comparison could retain
   positive energy, but requires an effective positive reference/inverse.
   The relative-dilation1140 and fixed97 stops remain; the inspected
   shifted-Schur806 stop also warns that a complement cannot fix an
   inadequate retained diagonal. No new reference inverse is proposed.
3. The selected explicit negative-symbol loss avoids charging the large
   positive deviation that stopped1162. Its complete compression is an
   independently testable object without a nominated inverse. Its price
   is discarding positive energy, so its effectiveness is wholly open.
   This is a standard-method candidate, not a creative mechanism claim.

The earlier120-mode absolute-complement stop793 loses a separate full
delay/pole budget at half-width1; it does not inspect this joint clipped
symbol at log101/2. Modulus stop789 rules out Q(|f|)<=Q(f), which this
nomination does not assume. The positive/negative parts found in
resolvent assessment821 concern function lattices and positivity
improvement, not this Fourier-symbol operation. Those distinct stops
remain preserved. This limited local comparison is not novelty evidence
or a completed literature assessment.

Essential prospective inputs: C750m for the exact fixed form, projection
and accepted domain/kernel audit; L744(6),(8) for normalization/symbol
bounds. C750f is comparison only, with no imported external floor.
The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
Even a successful complementary floor would leave coupling, retained
head positivity, all-support signs and Xi transfer unresolved. Its
plausible downstream use is to decide whether a one-sided finite-window
enclosure deserves further work after the symmetric certificate stop.

No justified creative all-support mechanism is ready: the signed resource
needed to bridge finite windows to actual-Xi positivity is still missing.
This source nomination is not relabeled creative to meet a scheduling
preference. Recommend literature_comparison, standard/high; no additional
audit or source refresh of C750m is requested. The next gate is deliberately
REVIEW_REQUIRED. Mathlib matching coverage remains unchecked. No
cross-notebook theorem, source-access retry or supervisor-state edit.

## Completed source comparison1165 — 16 November 2026

The preceding nomination is preserved as the historical pre-review scope.
The current decision above supersedes its statements that coverage is
unassessed. No mathematical test or new lemma is performed here.

### Primary theorem coverage

[Teschl, GSM99, 2009 author version](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorem3.1, printed pp90-91 (PDF101-102), applies to a projection-valued
measure and bounded Borel functions. Equation(3.21) represents pairings
by scalar integrals; its proof handles simple functions, uniform extension
and bounded pointwise convergence. This supplies symbol order before
compression, not commutation of nonlinear functions with compression.
Section6.3, printed pp139-141 (PDF150-152), (6.8)-(6.18),(6.21),
Lemmas6.9/6.10 and Corollary6.11 cover square-integrable kernels,
complete basis sums, bounded left/right factors and domination of the
operator norm. Their kernel expansion, singular-value approximation,
Parseval and ideal proofs were inspected completely. These theorems
supply a complete projected-kernel test, not an effective sine64 constant.

[Zhu2608.24827v2](https://arxiv.org/html/2608.24827v2),
Theorem1.1/(4), Lemma3.1 and Lemma6.1 with its proof and following
paragraph supply the already assessed reduction, envelope and odd-pole
sign. Reuse C750m's accepted normalization/core audit, full comb and
source radius b. Section11.1/(16) provides transforms, with the local
convention and normalization checked in C750m. Its numerical results,
Legendre decay and model zero tails supply no bound here. No source
spectral floor is imported and no general theorem needs reproof.

### Stronger-result and failure comparison

Exact and terminology queries are in the working note. No result found
in that bounded search matched this fixed clipped digamma/prime symbol
plus pole and the prescribed Q. This is not evidence of novelty.

[Israel and Mayeli2301.09616v2](https://arxiv.org/html/2301.09616v2),
14December2023, Section1.1.1 Theorems1.1/(1.4)-(1.6),1.4, concern
eigenvalue clustering for products of spatial and frequency projections.
Theorem1.1 assumes the unit hypercube and a compact coordinate-wise
symmetric convex frequency set contained in the unit ball, dilated by
r>=1, with epsilon in(0,1/2). Theorem1.4 specializes to cubes and
r>=2pi. These are not weighted clipped-symbol estimates in a prescribed
Dirichlet-sine complement. Eigenvalue decay in a spectral basis does not
control this Q without an additional comparison. No theorem or proof
from that paper is imported. The first guessed v3 URL returned404;
the authoritative abstract identified v2 and its theorem statements
were read successfully, so there is no essential access blocker.

[Nicola and Tilli2207.08624v2](https://arxiv.org/pdf/2207.08624v2),
4November2022, pp2-4, (1.1)-(1.3),(1.6), Theorem1.1 and Corollary1.2,
give norm bounds for Gaussian short-time-Fourier localization V*FV.
The theorem assumes a phase-space Lp symbol, 1<=p<infinity, with
L-infinity cap A and Lp cap B, requiring finite A for p=1. The
local object instead uses ordinary Fourier restriction on a fixed
spatial interval and a separate odd rank-one pole. No identified
unitary equivalence transfers the sharp constants. These inspected
hypotheses rule out a direct import; its proof is not used.

Reused local comparison:793 controls a different absolute loss at
half-width1;789 obstructs modulus contraction of functions;806 has
an inadequate retained diagonal at a different shift;821's positive
parts belong to a function lattice. None evaluates this loss. C750m's
audited positive witness stops a symmetric norm only. These are
contrasts, not mathematical inputs to a new estimate.

### Admitted mathematical specialization and bounded test

For the exact COVERED_TARGET, use C750m Sections1-2 and L744(6),(8),
with its fixed parameters and all35 terms. The object remains the
quadratic expression at the start of this assessment. The finite
frequency interval makes the proposed scalar clip bounded; s is in
the fixed spatial L2 space. Thus the bounded-symbol and kernel
theorems cover the intended objects without an unproved reference
inverse. This is an applicability comparison, not its quantitative
evaluation or a proof of its proposed order bound.

The later attempt must apply symbol order on the Fourier space
first, transport quadratic forms by zero extension/Fourier transform,
and then compress. It must check the proposed comparison of R with
the loss, using C750m(2)'s full complex pole decomposition; no equality
with the spectral negative part of K is licensed. Do not assume that
taking positive parts commutes with P or Q. The accepted E>=R comparison
and its closed-domain scope can be reused, not rederived as a new result.

A complete computable upper test is Teschl's L2 norm of the entire
projected spatial kernel on (-b,b)^2 after its actual formula has
been justified. P64 is finite and exact; project both kernel variables
with correct conjugations and retain the complete square. This method
accounts for all omitted sine modes without an unchecked infinite
row sum. It requires enclosure of every frequency contribution in
[-T,T] and the projected odd pole. The scalar positive-part map is
continuous and Lipschitz, so enclosures need not classify every zero
of beta-Psi. Any shortened frequency integral must carry a rigorous
bounded-multiplier remainder; no truncation is free. An unprojected
finite kernel bound proves existence only, not the strict target.
This identifies a complete test; no kernel formula, enclosure or
error constant is derived in this literature turn.

Start with analytic feasibility before costly quadrature over the
very large T. A single rigorously evaluated unit vector in the unchanged
QH is also an admissible necessary test of this positive loss. Such a
witness may be a complementary sine or an explicitly projected test;
it does not enlarge the retained head. If it gives expectation>=beta,
stop this sufficient certificate. If a complete upper enclosure gives
nu<beta, retain the resulting complementary resource for a later
separately reviewed coupling/head question. An upper estimate>=beta
or an enclosure straddling beta is inconclusive; park this bounded
attempt without retuning, head assembly or a negative-Weil inference.

The purpose is to assess one-sided complementary feasibility after
the symmetric stop. All-support signs, coupling, retained-head
positivity and actual-Xi transfer remain unresolved. No justified
creative central mechanism is available: a signed resource surviving
window extension is missing. This standard specialization is not
relabeled creative. Mathlib matching coverage remains unchecked.

New ready continuation: the exact COVERED_TARGET above, SPECIALIZE /
REPRODUCTION, recommended calculation/standard/high after the separate
supervisor approval of this newly written scope. That approval must
reuse this completed comparison, not repeat discovery or perform the
calculation early. No essential source remains blocked. No lemmas/,
mathematical scripts/, PROOF or DAG changes were needed1165.
