# Prime-shift interior cusp transport — source comparison

TARGET: Assess literature coverage for isolating the leading interior cusp at a prime-power translate of a nonzero endpoint trace under L516's complete signed nullvector equation, without assuming the other translated terms are smooth.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched logarithmic-Laplacian interior/Schauder/Dini regularity, logarithmic-Schrodinger fundamental solutions, translation-coupled zero-order kernels, and prime/cusp/Weil combinations; checked the local Weil assessments and recorded raw-adjoint, Abel, support and pole stops. No matching one-image signed equation theorem was located; this is not a novelty claim.
SOURCE_EVIDENCE: Inspected Chang-Lara–Saldana arXiv:2208.12841v3 Theorems 1.1–1.2, 4.12, Lemma 4.14 and proof, Corollaries 4.15–4.17 and bootstrap proof, Sections 5.1.2 and 6(1); Biswas et al. arXiv:2608.07315v1 Theorems 1.1–1.2 and Theorem 3.4 cutoff proof; Feulefack arXiv:2310.02481v2 Section 3/Theorem 3.1 and arXiv:2112.08783v2 Proposition 1.2/Section 5; Sikic–Song–Vondracek Section 3 introduction and Theorem 3.2 proof's use of Lemma 3.1; paper 67 v1 (3.1)–(3.6) and Theorem 2.4.
COMPARISON: The sharper regularity theorems require regularity of the complete forcing that L513–L519 do not establish; their cutoff proofs do not remove rough atomic translates. The newer Holder theorem assumes dimension at least two. The original unshifted geometric-stable Green theorem assumes d>alpha and thus does not apply at d=1,alpha=2. None supplies the requested coefficient or smaller remainder.
GAP: The pointwise leading profile and o(V(t)/log(1/t)) remainder under every signed translate remain unproved. The simple application of existing sharper regularity is unsupported. A finite localized high-frequency inverse test may investigate this difference without importing an unshifted whole-line Green kernel or assuming interior smoothness.
REASON: Essential theorem-level comparison is now performed. Park the automatic regularity/bootstrap and unshifted-Green implementations; nominate a bounded direct inverse test as unproved mathematics, subject to separate approval of its new continuation assessment. No mathematical derivation, source reproof or cusp theorem was produced in this literature turn.
SCOPE: Fixed L516 complete common measure, c=log(2pi), interval (0,ell) below 2A, assumed normalized real nullvector, L513/L515 physical traces and bounded data. Consider one interior prime-power shift d=log(n), avoiding coincidence with a reflected endpoint image. Retain nu_rho, every cutoff-equality atom and the full signed pole. Do not assume smoothness at other translated points, a spectral gap, full positivity, or trace vanishing.

## Nomination at turn start (preserved; review completed below)

### Relevance and bounded test

The main gap remains actual-Xi all-degree positivity. In the Weil
route, trace vanishing and an eigenvalue-relative signed arithmetic
bound remain missing. A precise propagation rule for a nonzero
endpoint trace could make it possible to test the compatibility of
the interior singularities forced by distinct prime shifts. No such
compatibility argument, contradiction or flux bound is presently
known here. The one-shift expansion would only be an intermediate
input; it is not itself a positivity criterion or proof of RH.

Review logarithmic pseudodifferential boundary/interior regularity,
finite-measure translation perturbations, stronger matching results,
and obstructions to localizing the other translated forcing terms.
Retrieve exact primary hypotheses and the proof cases governing
the remainder. A formal division by the high-frequency logarithmic
symbol is not enough. No assumption that all other shifted copies
are smooth may be inserted to obtain a leading term.

The discriminating target is one local expansion with a controlled
smaller remainder at an isolated first endpoint image, under the
actual full equation. Continue only if source coverage identifies
a rigorous way to separate the other translated contributions, or
supports a bounded mathematical test that can decide this separation.
If the required remainder already presupposes unproved interior
regularity or the sought trace cancellation, record that obstruction
and park this version. Do not approve an infinite propagation or
arithmetic cancellation mechanism from a formal local profile.

Essential inputs for any later attempt are L513, L515, L516 and
L518; L519 clarifies what continuity alone supplies. Nullvector
existence, the retained full-Weil identification, nonzero trace as
a test hypothesis, and the local separation/remainder are unresolved.
The raw-adjoint, Abel and pole-capacity stops remain evidence against
their respective implementations. There is no cross-notebook input;
matching Mathlib coverage is unchecked. This file nominates a target
for source review only, without deriving or approving mathematics.

## Completed primary comparison, 2026-10-30

The review concerns exactly the supplied target. Actual-Xi all-degree
positivity is the main gap; within this route, vanishing of nullvector
traces and the eigenvalue-relative signed arithmetic estimate are missing.
An interior transport law could later test compatibility of prime images;
it would not by itself prove either missing statement.

1. **Zero-order regularity.** Chang-Lara–Saldana, *Classical solutions
   to integral equations with zero order kernels*,
   [arXiv:2208.12841v3](https://arxiv.org/html/2208.12841v3),
   3 October 2022: the spaces preceding Theorem 1.1 require locally
   1-log-Holder forcing in Y; X has interior exponent 1+alpha.
   Theorem 1.2 covers log(1+|xi|^2), with zero exterior data on bounded
   Lipschitz domains satisfying a uniform exterior ball condition.
   Theorem 4.12 assumes bounded, locally Dini u, translation invariance,
   uniform ellipticity, 1-regularity and the weighted 1-log forcing norm.
   Corollary 4.16 gives a smaller gain alpha from beta-log data, beta<=1.
   Lemma 4.14's cutoff proof, (4.13)–(4.14), controls tails through
   differences of the regular kernel. The bootstrap in Corollary 4.17
   keeps the forcing's 1-log norm. Section 6(1) explicitly asks for a
   full one-log gain from alpha-log data. These are regularity estimates,
   not a signed asymptotic expansion. The forcing assumption has not
   been checked for the full L516 equation; inserting it is not allowed.

2. **Newer stronger-looking result.** Biswas–Roy–Sen–Sharma,
   *Holder regularity and Harnack inequality for the logarithmic
   Laplacian*, [arXiv:2608.07315v1](https://arxiv.org/html/2608.07315v1),
   7 August 2026, Theorems 1.1–1.2: n>=2, weak solution in V with the
   stated boundedness/tail conditions, and f in C^{0,kappa}, 0<kappa<1.
   Their improvement has modulus r^kappa/|log r|^beta. Section 3,
   Theorem 3.4, (3.18)–(3.19), handles the off-diagonal tail by kernel
   derivative bounds. The proof of Theorem 1.2 also invokes positivity
   of rho_n for n>=2. This does not authorize the n=1 case, a purely
   logarithmic forcing modulus, or smoothing of the atomic translates.
   This is a scope comparison, not an independent audit of that paper.

3. **Green-kernel lead and essential restriction.** Sikic–Song–
   Vondracek, *Potential theory of geometric stable processes*,
   Probab. Theory Relat. Fields **135** (2006), 547–575,
   [author-hosted primary text](https://web.math.pmf.unizg.hr/~vondra/geostb_rev.pdf),
   Section 3, manuscript pp.8–11 (PDF indices 7–10). The section assumes
   d>alpha before introducing the transient Green potential. Theorem 3.2
   gives its near-zero asymptotic. Its proof applies Lemma 3.1 with
   large-time exponent gamma=alpha/2<d/2; the restriction is used,
   not just omitted from the theorem's short display. This excludes
   direct specialization to d=1,alpha=2. No recurrent-dimensional
   unshifted Green theorem has been imported.

4. **Related PDE presentations are not a replacement remainder.**
   Feulefack, *The fractional logarithmic Schrodinger operator:
   properties and functional spaces*,
   [arXiv:2310.02481v2](https://arxiv.org/html/2310.02481v2),
   16 October 2023, Section 3/Theorem 3.1, cites the preceding
   Theorem 3.2 for the first Green asymptotic; its displayed proof
   treats s=1/2 and then 0<s<1. No signed, killed-interval translation
   remainder is stated. The earlier *The logarithmic Schrodinger
   operator and associated Dirichlet problems*,
   [arXiv:2112.08783v2](https://arxiv.org/html/2112.08783v2),
   25 December 2021, Proposition 1.2 and Section 5, addresses an
   unshifted whole-line Poisson kernel and uses parameterwise Bessel
   expansions inside its integrals. Neither text is imported as a
   justified one-dimensional local inverse estimate here. In particular,
   no claim is made that its stated whole-line formula resolves the
   original primary theorem's transience restriction. A cutoff or
   positive resolvent and a proved remainder are separate work.

5. **Existing Weil result and duplicates.** bramble_trace,
   *Boundary traces and support variation for localized Weil operators*,
   [paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67),
   27 October 2026, (3.1)–(3.6), keeps the same full measure as L516.
   Theorem 2.4 compares adding one atom at its activation boundary,
   with simple eigenvalue and parity assumptions. It supplies no
   interior pointwise transport coefficient. L518 concerns the raw
   renewal-density adjoint, not an expansion of u. The local support,
   generic-pole and Abel stops concern different reductions and remain
   evidence against those implementations only. Searches found no
   duplicate of the finite inverse test in the checked Weil files.

## Decision and limits

This is an informative source-scope NEGATIVE: the direct regularity
and unshifted-Green shortcuts fail their applicability check. It is
not an impossibility theorem for the cusp target, the actual operator,
or RH. The original scale and coefficient remain conjectural. No
primary theorem checked supplies the complete target; no novelty follows.

The next bounded test is specified in
`drafts/literature/2026-10-30-weil-first-prime-image-inverse-test-coverage.md`.
That assessment is newly written and needs separate approval next turn.
It asks whether finite localization/inversion can retain all translated
forcing and prove the missing remainder, rather than assuming it. Its
mathematical remainder estimates are the proposed research, not an
essential unread theorem being treated as available. No Green asymptotic
from the excluded hypotheses is required as an input.

Uninspected general microlocal and nonlinear regularity leads are not
being cited or assumed. Full matching Mathlib coverage is unchecked.
No cross-notebook theorem is used. No change to the main argument,
lemmas, DAG or mathematical scripts is warranted by this source review.
