# Coverage assessment: rounded-endpoint critical audit

TARGET: Critically audit L453's rounded-endpoint sign for every sufficiently large real height, including ceiling jumps, all sectors, the changed Mellin kernel and the pinned external-input qualification.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-statement searches and primary inspections in the rounded-endpoint height and Littlewood/endpoint audit assessments; searched named local sector statements, recent rounded-endpoint histories and four endpoint failure records. Read L453 in full and compared its actual scope with those assessments. No fresh external retrieval, exhaustive-search or originality claim.
SOURCE_EVIDENCE: Reused Csordas 1309.0055v2 Definition 1.2, Theorem 3.5, Lemma 3.6 and Theorem 3.7; Wagner 2108.01827v2 shifted-class definition and Theorems 1.2/1.4; Wang–Yang institutional manuscript equations (1.1)–(1.4) and Theorem 1.3, pp. 1–4; Titchmarsh (1986) Theorem 14.2 and proof pp. 336–337 and Section 14.3 pp. 338–339, as inspected in saved assessments. Reused pinned September 30, 2026, Theorem 1.1 and its recorded qualifications; compared L452 (1), C452a's completed audit, C294b's hypotheses/proof opening and L303's full identity proof.
COMPARISON: Unchanged sources supply known mechanisms and audited analytic/normalization interfaces, not a literal rounded-index theorem. L453 explicitly writes the changed-domain derivation, allowing a separate correctness audit without new discovery or reproof of the external theorem. Endpoint and fixed-h asymptotic conclusions cannot simply be invoked on its enlarged band.
GAP: Independently check L453 on r−1≤2n≤r+2, then its ceiling specialization, all boundaries and constants, Γ(2n+1) normalization, complete relative/additive errors and one real-height onset. This review supplies coverage, not a correctness verdict.
REASON: The completed L453 proof requires audit scope comparison beyond the prior attempt authorization. That comparison is complete; no essential source gap remains for this bounded conditional audit. Full external manuscript/import-closure verification remains outside scope.
SCOPE: Exactly the written L453 proof and stated local interfaces, including its two-sided h=5 neighborhood and every-height quantifiers; no theorem extension, lower-index sign or external-input certification.
LITERATURE_REASON: The completed changed-exponent proof and its audit continuation were outside previous attempt/audit scopes; existing source coverage is reused rather than repeating broad searches.

## Relevance and source reuse

The main gap is global mixed positivity; the smaller-index segment also
remains uncovered. The intermediate target is a separate correctness
verdict on L453. Success would validate its one-index-per-height input
for later comparison with the logarithmic witness range, leaving the
initial segment, bounded exterior heights and RH unresolved.

This completes the saved coverage-review request. TARGET now names the
ensuing mathematical audit; SPECIALIZE permits REPRODUCTION. It neither
approves the mathematical conclusion nor performs that audit this turn.

The [rounded-endpoint assessment](2026-10-23-rounded-endpoint-height-coverage.md)
records inspected primary statements and proof cases of
[Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2),
[Wagner, arXiv:2108.01827v2](https://arxiv.org/html/2108.01827v2), and
[Wang–Yang, institutional manuscript, pp. 1–4](https://cfc.nankai.edu.cn/_upload/article/files/81/18/f83d37e449ebaf1b2f4141fa59be/9323c2fc-4d6a-4610-a747-1bd985a7be41.pdf).
Their conclusions respectively retain positive definiteness as a premise,
shift the derivative order, or concern coefficient indices. None of the
inspected statements supplies L453's unshifted height-linked sign. Their
saved comparisons remain adequate; no unread lead is treated as evidence.

The [Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
records direct inspection of Titchmarsh, second edition revised by
D. R. Heath-Brown (1986), [Theorem 14.2 and proof, pp. 336–337](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173),
and [Section 14.3, pp. 338–339](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=174).
The printed theorem assumes RH. L452's separately audited fixed-disk
specialization supplies the changed-hypothesis bound; no literal import
of that printed conclusion is allowed. Only L452 (1), uniform on
63/64≤Re(s)≤2 at sufficiently large positive height, is available for the
changed parameters. Its paired-parameter (2) and the L331 saddle cannot
substitute for L453's kernel argument.

The [external register](../../foundations/2026-10-quasi-riemann-input.md)
pins OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
to commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Retain strict
Re(s)>7/8, the allowed pole at 1 and the unaudited full manuscript/formal
import closure. The audit is conditional on this cited input; it is not
an independent certification, boundary exclusion or RH proof.

## Exact audit coverage and exclusions

L453 was read in full, including its Mathlib qualifications. The prior
attempt assessment records complete inspection of L288/L299–L304 and
relevant L269/L295/L330 and C294b mechanisms. The
[coupled-endpoint audit coverage](2026-10-22-coupled-endpoint-margin-critical-audit.md)
and C452a's completed canonical audit supply the normalization reference.
Reuse these inspections. The following are subsequent audit obligations,
not conclusions proved by this literature review.

- Section 1: check saddle existence/uniqueness, exact ceiling inequalities,
  jump heights and conversion to the full r−1≤m=2n≤r+2 proof band.
  Check bounds on that band before restricting to the ceiling curve;
  h may be below 5. Require one common real-height onset.
- Sections 2–3: test discrete mass and strict cutoff tails, exact summand
  algebra and Jacobian, uniform amplitude derivatives, clipped Fresnel
  patches and every rectangular edge/corner term. L288's h>5 limiting
  square and L299/L300's m=r conclusions are not imports at changed
  parameters; L453's written replacements require independent review.
- Sections 4–5: check polynomial derivatives at zero, retained curvature
  saving, both same-sign strips, mixed-sector stationary contributions,
  absolute integrability and limiting boundary terms. C294b ends at h=5;
  L453 explicitly rechecks its proof up to h=21/4. Audit that recheck
  rather than invoking C294b outside its hypotheses.
- Sections 6–7: check reflection and the factorial multiplier against
  C452a, the six-region partition and reality. L303 covers the scalar
  inversion/Fubini mechanism, not the changed kernel as a theorem.
  Audit Γ(m+1), exponent −m−1, c=1/2+2/r, σ=1+2/r, exact integral one,
  bounded absolute mass, uniform Stirling estimates and complete tails.
- Section 8: retain both shifted heights in L452 (1), integrated relative
  variation and reciprocal bounds only at σ>1. Compare the full Mellin
  tail with B first, then the additive error with the polynomial margin.
  Test O(r^(−1/6)) and one onset without a positive-kernel assumption or
  a modulus-square substitution away from v=0.

The scoped duplicate check identifies L453 as the completed extension,
L330 as its known conditional comparison mechanism and C452a only as
the paired specialization. Four inspected failure records preserve
[coefficientwise freezing](../../ATTEMPTS/2026-09-24-endpoint-saddle-freezing-test.md),
[automatic positive Mellin averaging](../../ATTEMPTS/2026-09-24-endpoint-mellin-test.md),
[old derivative envelopes](../../ATTEMPTS/2026-09-24-endpoint-logarithmic-derivative-test.md), and
[fixed-r/unit-phase positivity](../../ATTEMPTS/2026-09-24-endpoint-liouville-phase-test.md)
stops. These are not global bans on the changed coupled domain. Retain
their quantifiers; no failure is erased by an unproved extension.

Continue only if every essential identity, boundary estimate and uniform
constant supports the claimed relative error and positive margin on the
entire ceiling domain. A failed normalization, coverage, convergence or
onset check requires precise correction/qualification and preservation
of the failure; do not infer a negative actual coefficient.

Essential inputs are L453, audited L452 (1) and C452a, with
L269/L288/C294b/L295/L299–L304/L330 for inherited mechanisms.
External trust remains qualified; smaller indices, bounded exterior
heights, global mixed positivity and selected-law/regulator gaps remain
independent. Full matching Mathlib coverage is not checked; supporting
entries and an external Lean artifact are not a matching theorem or a
locally verified build. No lemma, mathematical script, DAG edge or main
argument is changed by this source review.
