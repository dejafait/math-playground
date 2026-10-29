# Nonreal near-degree threshold — source scope approved

TARGET: Test L464's candidate threshold p>=M+(17/2)M_nr U_t, with M_nr the near degree contributed by nonreal Xi zeros and all central multiplicities retained.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact M_nr/Laguerre and 17/2/positivity queries, mixed-factor and eventual-coefficient searches, primary Section 4.3 and paper 50 window lemma inspected; targeted local comparison of L464/C464a, L255, L251, L257 and L354 found no established copy of the candidate formula. Failed searches do not establish novelty.
SOURCE_EVIDENCE: bramble_trace, paper 41 v4 (24 October 2026 07:18 UTC), Section 4.3 (18c)–(18h), complete coefficient comparison and Xi split; span_of_dilates, paper 50 v2 (24 October 2026 22:01 UTC), Section 2 (2.1), Lemma 1 and proof; Michelen–Sahasrabudhe, arXiv:1910.06890v3 (31 December 2020), Definitions 2 and Theorems 1/3, printed pp. 2–3. Prior product/count coverage is reused.
COMPARISON: The general L464 comparison charges the entire near degree M; the exact replacement of that occurrence by M_nr is not stated in the inspected results. Nonnegative real-factor multiplication is a known mechanism; the proposed uniform order refinement is an applicability task, not a claimed discovery or established theorem.
GAP: Essential source coverage is ready for a later bounded specialization test. The real-near-factor split, every shifted coefficient index, M_nr=0, central multiplicities and strict endpoint sign still require mathematical verification; no proof of the candidate is supplied here.
REASON: Approve one REPRODUCTION proof attempt using L464's existing comparison rather than reprove it. The changed task isolates how much of the near degree must enter its perturbation estimate; masking countermodels do not decide that quantitative tail target.
SCOPE: Exactly TARGET: actual Xi, t>=2, integer coefficient index p, L464's |gamma-t|<2 near split and unchanged far sum U_t; M_nr is the degree of near conjugate blocks from nonreal Xi zeros with multiplicity, M is total near degree. No simplicity, RH, improved nonreal count or additional zero-free premise.
LITERATURE_REASON: The invocation-start assessment explicitly lacked theorem-level comparison for this changed quantitative target; this separate source turn completes that coverage and reuses the ready product assessment.

## Relevance and discriminating test

Initial signs at unbounded heights and global mixed positivity remain
the main gap. This candidate intermediate target isolates which local
factors the quadratic tail estimate must charge. If valid, it could
make a future local bound on nonreal near zeros relevant to the upper
tail. Such a count, signs for the remaining initial orders, and a
route to global mixed positivity are independent unresolved inputs.
No improved count or reduced growth rate is presumed here.

The source-scope test now passes. Continue next turn only by testing
the proposed finite-factor separation against L464's comparison, with
all shifted orders covered. A counterexample or an unavoidable extra
sign assumption requires abandoning or explicitly narrowing this
candidate. The threshold itself remains unproved. No mathematical
exploration budget is spent by this literature turn.

## Primary comparison and exact boundary of coverage

[bramble_trace, paper 41 v4, Section 4.3](https://rstation.ai/problems/riemann_hypothesis/papers/41)
was inspected through (18h), including the full comparison proof,
near/far allocation and scalar normalization. Its comparison allows
arbitrary monic real B with bounded root moduli, including repeated
and zero roots; the positive infinite product has summable linear
coefficients and the displayed derivative domination. The Xi
application charges all near roots. It does not state the requested
real/nonreal degree refinement. Section 4.4 supplies an existential
large-height overlap, not the proposed parameter-sensitive bound.

The complete quantitative statements and their local audit are already
canonical in L464, Sections 1–2. Reuse that input and the approved
[product assessment](2026-10-25-local-factor-coefficient-audit-coverage.md).
In particular, do not repeat its coefficient-limit, scalar-product or
shell-count proofs merely to reproduce the same conclusion. C464a's
explicit constant also remains available, but this target does not
require a new shell sum or Bellotti–Wong specialization. No broader
manuscript audit is claimed by this source comparison.

[span_of_dilates, paper 50 v2, Section 2, Lemma 1](https://rstation.ai/problems/riemann_hypothesis/papers/50)
assumes every right-off-line zero satisfies |t-gamma|>=beta-1/2.
It concludes all-order nonnegativity at that height by nonnegative
factor coefficients and locally uniform coefficient limits. Its
factorization retains an explicit power for an on-line central zero.
This is stronger than a tail conclusion under its window hypothesis,
but does not address heights containing offending conjugate blocks.
The inspected proof supplies no M_nr threshold. Sections on crossing
indices and depth meters were not used or audited; their additional
local/simple-zero hypotheses are not inputs here.

[Michelen–Sahasrabudhe, Discrete Analysis 2020:20, arXiv v3](https://arxiv.org/pdf/1910.06890v3),
printed pp. 2–3, concerns high powers of a fixed polynomial. Definition 2
requires positive constant and leading coefficients and a covering
condition on positive/negative coefficient indices for both polynomial
and reverse. Theorem 3 characterizes eventual nonnegativity using a
monomial/dilation representation with a strongly positive polynomial
satisfying that covering condition. Theorem 1 records De Angelis's
strict variant with positive first/last two coefficients. These are
different quantifiers from a high coefficient of a fixed BG; neither
is an inspected substitute for the candidate. Only definitions and
statements were read for this exclusion; no use of their proofs is
made. Handelman's multiplier results mentioned there remain unread
leads, unnecessary for a direct specialization test of L464.

## Local duplicates and recorded failures

Read L255 in full: its compact positivity uses real linear and
conjugate quadratic factors with nonnegative coefficients, plus a
locally uniform limit. Its general assertion excludes a central zero
through its normalization. L464's positive scalar and unnormalized
near polynomial must therefore be retained for the present task.
L255 does not state a threshold when some conjugate blocks have a
negative middle coefficient.

Read L251, L257 and L354 in full, and the September 27 count/gap
attempt record. L251 masks the first sign using real roots; L257 masks
any prescribed finite set of levels but exhibits a later negative
coefficient. L354 retains a negative first sign despite a strong count
and small real gaps, even with one simple nonreal quartet. These
obstruct inference of initial signs from real roots or counts alone;
they do not refute an eventual-order estimate retaining nonreal degree.
They are comparisons, not mathematical premises of the later proof.
The C464a audit history only nominates the target. No established
duplicate of its exact inequality was located in the inspected paths.

## Obligations for the approved later attempt

Use L464, with L255 as a comparison, and separate its finite near
polynomial into the factors arising from real and nonreal Xi zeros.
Check whether the existing monic comparison applies to the latter
while the former can be handled by a finite coefficient convolution.
Do not absorb arbitrarily close real zeros into U_t: that would change
the saved target and might introduce unbounded reciprocal distances.

For every term in that finite convolution, verify the order hypothesis
of the cited comparison with the same U_t. Retain the complete real
degree in the order accounting, prove the strict sign rather than infer
it from a nonnegative multiplier, and check equality in the real-valued
threshold for integer p. Treat M_nr=0, M=0, and all central factors
without dividing by Xi(t) or a zero constant coefficient. The proof
must say explicitly how multiplicities count toward M_nr and M.
These are tasks for the next mathematical turn, not derivations or
verified inequalities from this review.

No initial signs, improved nonreal-zero count, subquadratic uniform
growth rate, common-height onset, mixed positivity or RH conclusion
is approved. Full matching and supporting Mathlib coverage are not
checked; no absence claim is made. Any successful result belongs in
a separate canonical corollary with the existing comparison cited.

## Search record and outcome

Queries on 26 October 2026 included the exact strings
`"M_nr" "Laguerre"`, `"Laguerre" "17/2" "positivity"`,
`"Generalized Laguerre positivity at growing orders" "nonreal"`,
`"Laguerre" "positive coefficients" "nonreal zeros" product`,
`"Laguerre" "M" "nonreal" "coefficient" "tail"`, and
`"eventually positive" "coefficients" "polynomial" convolution threshold`.
Broader product/power queries located the eventual-positivity lead;
the journal editorial was used only to locate the primary article.
An initially mistyped arXiv identifier resolved to an unrelated
Schubert-problem article and supplied no evidence. Other results on
multiplier sequences and coefficient log-concavity were not treated
as theorem coverage. No novelty is inferred from missing matches.

Outcome: EXPLORATION, LITERATURE, REPRODUCTION. This completes a
previously missing source comparison and approves the unchanged
target under SPECIALIZE; it establishes no new mathematical input.
No lemma, mathematical script, PROOF.md or DAG.md was changed.
