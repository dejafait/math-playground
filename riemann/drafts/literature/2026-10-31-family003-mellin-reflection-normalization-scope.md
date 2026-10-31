# Full-frequency Mellin reflection: source gate

TARGET: Audit family 003's full-frequency Mellin reflection normalization and constant-term removal, retaining L547's canonical cusp construction and the stated coefficient-size and finite Gauss bounds.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Target-specific local searches found no completed analytic audit; finite-cusp and phase assessments are reused. Exact Mellin/constant-term/cubic-theta queries, source comparisons and the negative ATTEMPTS search are recorded in drafts/audits/2026-10-31-family003-mellin-reflection-source-notes.md. The manuscript claims the target already; no novelty is asserted.
SOURCE_EVIDENCE: Family003 commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, build/paper.tex 1551–1678, 1782–1934, 2139–2260 and eq:pointwise-mellin-tail with its proof; DR arXiv:2109.07463v3 Section 5, (5.1), (5.6)–(5.16), Lemma 5.2 proof opening, (5.43)–(5.60) including Lemma 5.3 and all Proposition 5.1 proof cases; DLMF 10.43.19, 10.25.3, 10.30.2, 10.29.5 and 5.11.9 were inspected at the exact hypotheses below.
COMPARISON: DR's twisted functional equation requires unit Fourier support and does not directly cover this target. Its raw automorphy/cusp expansions and the Bessel Mellin theorem supply standard inputs. Family003 explicitly treats all frequencies by reduced cusps, a first horizontal derivative and direct/reflected Mellin integrals. L547 covers the finite construction only; verifying that analytic application is a justified conditional reproduction, not a new transform or a direct import of DR's restricted theorem.
GAP: The sources now cover a bounded fixed-arithmetic-data audit, but exact chain-rule/scalar normalization, termwise operations, both endpoint estimates, entire continuation, strip growth and the contour shift remain unverified locally. L547 review, coefficient/Gauss bounds, marked expansion, uniform/global closure and Xi signs remain independent qualifications.
REASON: Essential previously unread analytic proof cases have been retrieved. SPECIALIZE prepares the unchanged target for separate next-turn approval and conceptual audit; no analytic implication was derived in this literature-only turn. Reproving theta theory is unnecessary; directly citing the full claimed proposition would bypass the retained-premise check.
SCOPE: Fixed S,L, base character and each finite arithmetic choice; all original Fourier frequencies, including nonunit h_0 and zero local frequencies, all three raw cusps, r=1 and full original dual support. Retain L547's finite construction (independent review pending), the stated coefficient/Gauss bounds and whole-index conventions. Growth constants may depend on arithmetic data. Exclude new uniform arithmetic bounds, kernel seminorm estimates, marked expansion proofs, hybrid norms, global closure and actual-Xi signs.

## Inspected primary results and comparison

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, 30 September 2026,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`prop:completed-reflection`, `eq:reflection-translated-theta`,
`eq:reflection-direct-mellin`, `eq:reflection-reflected-mellin` and
the complete continuation/contour argument at 2206–2260, claim the
entire target for fixed arithmetic data. The source's profile V and
every logarithmic derivative vanish faster than every power at both
ends; this is essential to its shifted Mellin contour.

Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), 14 May 2024:

- (5.1), (5.6), (5.9), (5.15)–(5.16): unrestricted action and raw
  expansions. F_1 has constant (3^(5/2)/2)v^(2/3); F_19,F_10 have
  none. Conjugate coefficients use bar(d_j(-mu)). These inputs do
  not assume GRH or unit Fourier support.
- Lemma 5.2 and Corollary 5.1 assume a primary period r and a periodic
  twist whose finite Fourier transform is supported on units modulo r.
  Their proofs use this restriction to invert the frequency. They
  cannot be applied directly to the retained masks.
- Lemma 5.3, (5.45), gives the Mellin gamma factors for Re(s)>1,
  integer angular order ell, with its absolute-convergence proof.
  Proposition 5.1 retains the preceding twist assumptions. Its ell=0
  residue at 5/6 and ell!=0 entire case, including the constant-term
  corrections in (5.52), (5.56)–(5.57), were read separately. Do not
  import its entire case without verifying the full-frequency application.

NIST DLMF, version 1.2.8 (15 September 2026),
[10.43.19](https://dlmf.nist.gov/10.43.E19) states
the Mellin transform of K_nu with Re(w)>|Re(nu)|.
[10.25.3](https://dlmf.nist.gov/10.25.E3) gives its large-argument
decay on sectors away from the cut;
[10.30.2](https://dlmf.nist.gov/10.30.E2) its small-argument form
for Re(nu)>0;
[10.29.5](https://dlmf.nist.gov/10.29.E5) its integer derivatives
via the modified-cylinder convention; and
[5.11.9](https://dlmf.nist.gov/5.11.E9) the gamma asymptotic uniform
for bounded real parts. The required Bessel arguments are positive
real and nu=1/3. The derivative convention must be respected, rather
than substituting K into an I-normalized recurrence without its signs.

## Separate audit permitted by this scope

The source record gives exact displayed normalizations and the
remaining checks. Use ordinary dominated convergence, Mellin inversion,
the identity theorem and maximum modulus as standard named analytic
inputs; check their hypotheses rather than treating a formal series
identity as analytic continuation. The bounded test is to reproduce
the claimed fixed-data implication with every cusp/frequency present.
Any failed interchange, uncancelled zero term or inconsistent scalar
must remain a recorded obstruction. Neither a numerical scalar check
nor a unit-frequency-only argument passes this test.

Essential local inputs are L547, L546 and L541's retained analytic
reflection premise. The source's completed reflection conclusion must
not be used to prove that premise. A successful audit could justify
this portion of L541's input, while independent retained assumptions
and actual-Xi positivity remain unresolved. This is source coverage
for a later REPRODUCTION audit, not a completed proof. Mathlib matching
coverage has not been checked. No lemma or mathematical script was
written or modified in this review.
