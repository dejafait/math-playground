# Full raw cusp coefficient bound — source comparison

TARGET: Assess L548's raw cubic-theta coefficient bound (3) on all three cusp supports, including shared n,b primes, primes in S and every ramified exponent.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched cubic theta coefficients squarefree and the exact 27*3^(k/6) envelope; checked family003 cusp/Mellin/coefficient assessments, source and critical notes, relevant histories and ATTEMPTS terminology. Existing local audits retain this premise; L547 (9) already gives the identities. Other manuscript variants, expositions and analogues were leads only. Detailed record: drafts/audits/2026-10-31-family003-full-cusp-coefficient-source-notes.md.
SOURCE_EVIDENCE: Read DR arXiv:2109.07463v3 (14 May 2024), (5.7)–(5.16), Appendix A rows 1,19,10, Section 2 (2.1)–(2.3) and normalization (1.7)–(1.8); pinned OpenAI TeX commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a 1806–1854, including its full cubic-only norm/shift argument and explicit -2 case. Reused prior finite-ring unit-shift coverage; upstream Hasse/Patterson proofs remain unaudited.
COMPARISON: DR lists all raw coefficient and otherwise-zero cases with primary c,d and squarefree c, without (c,d)=1 or S-exclusion; its norm input is all-primary and includes inert primes. The pinned manuscript already asserts the exact envelope and intermediate magnitudes. Known sources cover the needed inputs; the remaining work is a local application check, not new theta or Gauss theory. L548's good-sextic conversion alone does not cover this wider domain.
GAP: Essential coverage is complete for a separate reproduction audit of the three conjugate cusp functions, every unit and ramified case, cubic unit shifts at all primary squarefree moduli including 1, shared n,b factors and primes in S, and the constant 27. L548 (3) is not discharged in this literature-only turn; arithmetic uniformity and actual-Xi signs remain open.
REASON: The changed full raw domain required essential coverage beyond the ready good-squarefree normalization scope. Primary case statements now support a bounded application audit without reproof of theta theory; newly prepared research coverage requires separate next-turn gate approval.
SCOPE: L548 (3) only, for its three unmasked raw cusp coefficient functions, k>=-4 and primary nonzero n,b with n ideal-squarefree; retain L547's audited cusp identification and all zero cases. Permit citation of DR's all-primary norm and finite-ring unit-shift scaling. Exclude theta/Hasse source-proof audits, new finite Gauss identities, arithmetic-uniform closure and Xi signs.

Essential local interfaces are L548 (2)–(4), L547 (9), and their
raw-import paragraphs. Prior canonical-cusp and Mellin coverage is
reused. The inspected primary sources are
[DR Sections 5.1–5.2 and Appendix A](https://arxiv.org/html/2109.07463v3)
and the
[pinned TeX, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
No upstream theta proof is certified by this review. No cross-notebook
input is used. The complete locator map, domain comparison, search limits,
Mathlib qualifications and later test are in
[the source notes](../audits/2026-10-31-family003-full-cusp-coefficient-source-notes.md).

The pinned source claims magnitudes 3^(k/6+8/3)|b| and
3^(k/6+3)|b| for tau, and 9|b| at k=-4 for tau_1,tau_2.
These have not been derived or independently checked here. The later
application must compare each source case with 27*3^(k/6)|b|,
including n=1, all unit/sign/zero cases and excluded primal primes,
using the ordinary cubic symbol rather than extending sextic symbols
to the prime above 2. A missing case, extra mask or stronger required
constant prevents discharge.

A successful specialization would remove a coefficient-size premise
from the conditional reflection/tail route; independent arithmetic
and actual-Xi gaps remain. No concrete central creative mechanism
follows from size coverage alone. A separate actual-Xi realization
or sign mechanism with a discriminating test is needed before such
a nomination. No lemma, script, DAG or PROOF change was made here.
