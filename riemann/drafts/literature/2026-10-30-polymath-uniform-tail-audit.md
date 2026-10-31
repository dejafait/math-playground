# Polymath compact positive-time tail — audit coverage

TARGET: Audit Polymath v2 Theorem 1.5(i)–(ii) for a common real/simple zero tail of F on 0<a<=lambda<=b<=1/8, checking multiplicity, equations (102)–(104), and uniform thresholds.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed KKL/Polymath comparison in drafts/literature/2026-10-30-positive-time-uniform-high-zero-tail.md; narrow heat lemma/failure searches found local-to-global limitations but no matching uniform-tail import. No further source search is needed for this exact audit.
SOURCE_EVIDENCE: Polymath arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 and https://arxiv.org/pdf/1904.12438v2 ; Theorem 1.5(i)–(ii), pp.9–10; Proposition 9.1(i) and Lemma 9.2 with proofs, pp.56–59; localization/count proof, pp.59–60, equations (102)–(104). Prior detailed evidence: drafts/heat/2026-10-30-positive-time-high-zero-source-review.md. Direct HTML access and relevant statement/proof passages reconfirmed on 2026-10-30; this is source-gate repair, not the mathematical audit.
COMPARISON: The published theorem provides absolute-constant localization and a complex-disk count for 0<t<=1/2 without assuming t>Lambda. The proposed step audits and specializes known mathematics; no originality or full-manuscript audit is intended.
GAP: Verify the multiplicity-one winding count from (102)–(103), the potentially insufficient displayed O(|y| log x_n) error in (104), complete high-zero exhaustion, x/n threshold compatibility, reflection, and one threshold on each compact interval after t=4lambda, x=2z.
REASON: A common tail could remove escape to infinity from L126/L128's positive-time use; a coarse circle estimate cannot simply be promoted to a strict Rouche inequality. This precise source concern justifies a local replay, rather than reproving established asymptotics.
SCOPE: A single conceptual proof audit and necessary routine specialization only. Accept Proposition 9.1(i), Lemma 9.2, and the source's cited global strip bound as named inputs; no new saddle estimate, endpoint claim, all-positive-time extension, finite-collision exclusion or full RH argument. L018/L019/L058 fix normalization; L126/L128 identify downstream limitations.

## Bounded test

Check whether the holomorphic two-term approximation and phase relation
(102)–(103) provide a strict, time-uniform count on the small complex
circles, rather than relying solely on the coarse (104) display. Verify
that every sufficiently high zero belongs to a disk counted once with
multiplicity and that thresholds in x and n can be made common for
4a<=t<=4b<=1/2. Retain all constants as existential absolute constants;
no numerical onset has been extracted.

If that audit succeeds, a later canonical local import may record the
restricted common real/simple tail. If it fails, preserve the exact
comparison/quantifier obstruction without declaring the published theorem
false. Neither result excludes finite collisions or controls a down to zero.
Full Mathlib coverage is unchecked. The separate literature recovery on
2026-10-30 reconfirmed source access and supplied the missing direct URLs;
the target, SPECIALIZE decision and bounded mathematical test are unchanged.

## Direct-source recovery record

Reopened the primary HTML version above, specifically Theorem 1.5 and its
absolute-constant convention, Proposition 9.1(i), Lemma 9.2 and the proof
of parts (i)–(ii). The count proof invokes the argument principle after
(104); exhaustion uses the global strip and nearest phase center. This
confirms the source scope already recorded, without resolving the coarse
error concern. No further discovery search or KKL retrieval was needed.
No new theorem, specialization proof or independent source audit is claimed.
