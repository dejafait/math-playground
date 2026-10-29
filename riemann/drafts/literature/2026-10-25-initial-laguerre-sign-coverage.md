# Initial Laguerre signs — completed source comparison

TARGET: Assess published logarithmic-order Laguerre positivity for coverage of L461's initial segment 1<=n<=ceil(c log(2+|a|)+B_c), for some fixed c>3/16 at all real centers.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Identified the recorded logarithmic-order lead as bramble_trace, rStation paper 41; primary page displays v4, 24 October 2026, 07:18 UTC, despite stale v2 search previews. Compared the prior local v3 screen, the saved first-sign source assessment, L018/L461/L462/C460b, L255 and the finite-sign/count-gap failure records. Exact queries and scope appear below.
SOURCE_EVIDENCE: bramble_trace v4, equation (1), Theorems 1/1a/1b/1c/3/4, Corollary 4a, Sections 4.1–4.5 including (18c)–(18n), and Section 10.3 (77)–(82); Sra v1, 20 October 2026, equation (1.5), Theorem 1.3, printed pp. 2–3, and Lemmas 4.1/4.2 with Theorem 1.3 proof, pp. 9–11. Primary statements and relevant proof cases were read; no independent full-source audit is claimed.
COMPARISON: The strongest inspected pointwise theorem supplies an eventual upper-order tail with 2p>=c_0 log(t/(2pi)), c_0>3/8 under the retained premise. Here p is the notebook's n, not 2n. Lower-order theorems allow exceptional heights and a diverging lower order; Sra supplies all orders only on a verified finite-height interval. None supplies the requested segment starting at 1 at every real center.
GAP: Fixed low orders at unbounded heights, endpoint uniformity, an effective overlap of bounded and eventual height ranges, and global mixed positivity remain unproved. The pointwise tail is a source-covered proper input; the missing initial range is not an approved new proof target under this assessment.
REASON: The v4 half-plane theorem changes the prior v3 comparison and offers a precise import without repeating local saddle calculations. Prepare that narrower import for separate approval; stop treating the identified lead as a possible full initial-sign theorem. No new mathematics is derived in this literature-only step.
SCOPE: Actual Xi and analytic-product coefficients D_n of L018/L461, all central multiplicities, fixed constants before height varies, and precisely the pinned strict Re(s)>7/8 premise. This comparison authorizes no new sign mechanism, moving-anchor estimate or boundary claim.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment lacked the identity and exact hypotheses of an essential positivity lead. The primary source has also changed from the previously screened v3 to v4; its new Theorem 1b needs comparison, while existing source assessments remain reusable.

## Gap, intermediate input and decision test

The main gap is the initial low-index sign segment at unbounded
heights, with global mixed positivity also unresolved. The intermediate
target for this turn was to identify whether a published sign theorem
covers L461's exact initial segment, or a proper part useful in a later
argument. Continue to a precise source import if the coefficients and
quantifiers match; abandon the inference of full initial coverage if
the result starts above a logarithmic lower threshold, excludes heights,
or adds an unavailable zero hypothesis.

The test resolves negatively for full coverage. A useful narrower input
is ready: the v4 pointwise upper tail. Its downstream use is to remove
upper-order sign obligations and avoid reproving source-covered bands.
It does not supply the signs below that tail, even though its limiting
order threshold and L461's witness coefficient both involve 3/16.
No new lemma, mathematical script, DAG edge or argument change was made.
The initial REVIEW_REQUIRED placeholder and the interim source checkpoint
are superseded by this completed comparison; their unresolved target is
retained above.

## Precise primary sources and what was inspected

1. bramble_trace, [Generalized Laguerre positivity at growing orders,
   rStation paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
   displayed v4, 24 October 2026, 07:18 UTC; accessed 25 October 2026.
   This is an author-identified platform manuscript, not a claimed
   independently verified journal theorem. The main page was accessible;
   an attempted /v4 URL and Markdown download were not. The accessible
   [v3 archive](https://rstation.ai/problems/riemann_hypothesis/papers/41/v3)
   is a different version, not a substitute for Theorem 1b.
2. Suvrit Sra, [On some positivity properties of the Riemann Xi
   function, v1](https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf),
   released 20 October 2026, 25 pages. The direct first PDF request
   failed; following its author-page PDF link succeeded. This is not
   a persistent source blocker.
3. Reused the [September first-sign assessment](2026-09-27-first-laguerre-zero-compensation.md)
   for Csordas, arXiv:1309.0055v2, Propositions 2.2–2.3, Open Problem
   4.7 and the zero-density/spacing comparison. No new audit of its
   cited density theorems was necessary.
4. Reused the [October external-input register](../../foundations/2026-10-quasi-riemann-input.md)
   and [overlap assessment](2026-10-21-openai-quasi-rh-overlap.md).
   No stronger zero-free hypothesis or external import audit is introduced.

The rStation equation (1) defines its expression as the coefficient of
y^(2p) in the same entire Xi product as L461. Its coefficient order
variable is n_source=2p; the notebook coefficient index is p.
The positive normalization b(t)^2 used for normalized Xi statements
does not turn a Hardy-function assertion into an unqualified Xi
assertion: only the explicitly stated Xi conclusions are compared.

Theorem 1b assumes 1/2<=sigma_0<1 and no zeta zeros in Re(s)>sigma_0.
For each fixed c_0>sigma_0-1/2 it gives one eventual height threshold,
independent of the order, beyond which all integers 2p>=c_0 log(t/(2pi))
have positive Xi Laguerre expression. There is no upper order cutoff.
The stated sigma_0=7/8 specialization retains exactly the notebook's
external premise. It is not a new zero-free conclusion. Equality
c_0=3/8 and uniformity as c_0 decreases to that boundary are not stated.

Read the essential proof cases rather than infer this from the abstract:
Section 4.5 regularizes the pole, obtains sublogarithmic logarithm and
derivative bounds on strictly smaller half-planes, shifts the coefficient
saddle by its exact equation (18l), and controls the intermediate arcs
using the real-axis symmetry in (18m). Its final formula (18n) retains
that moving saddle. Freezing at the unshifted n_source/log(t/(2pi))
is explicitly disallowed below the earlier absolute-convergence range.
The complementary arcs need the strict fixed margin
c_0-(sigma_0-1/2)>0. Thus this proof case is not an initial-index or
endpoint theorem.

The all-order extension uses the overlap with Theorem 1a. Sections
4.2–4.4 were read: growing disks give positivity through logarithmic
powers, and the exact product split gives the remaining coefficient
tail. The split has a finite local polynomial B_t with repeated and
zero roots allowed, times a positive-coefficient G_t; its proof avoids
division by Xi(t)^2. The coefficient comparison, summable far factors,
positive normalization and tail-overlap cases were inspected.
This supplies source coverage for the stated import, not a separate
local critical audit of all estimates or of the external zero-free input.

For smaller orders, Theorem 3 is an absolute mean approximation.
Theorem 4 and Corollary 4a give simultaneous typical-height positivity
above a diverging lower order. Section 10.3 explicitly removes
neighborhoods of zero ordinates before using harmonic logarithm
comparisons. A set of measure o(T) may still contain every hypothetical
off-line zero ordinate. Fixed order 1 and every-height signs do not
follow. Theorem 1c likewise bounds an exceptional height set rather
than making it empty. Arithmetic filtered means do not sign the
observable at every individual center; their full proofs were not
needed or audited for this mismatch.

Sra's Theorem 1.3 assumes all nontrivial zeros with 0<gamma<=T are
on the line, T>1/2. It gives every order on |x|<=T-1/2, with
nonnegativity also at multiple central zeros. Its equality qualification
is multiplicity greater than the Laguerre index. Read Section 4,
including the real-zero, conjugate-pair, exponential and locally uniform
coefficient-limit cases of Lemma 4.2, and the central-multiplicity
argument at the end of Theorem 1.3. This zero-exclusion argument does
not extend its verified-height assumption. The cited verified choice
T=3*10^12 is finite. No numerical overlap with the existential eventual
onset of Theorem 1b is known here.

## Local duplicates, failures and retained qualifications

The supposedly unidentified lead had already been screened as v3 in
[the October 24 theta assessment](2026-10-24-deeper-band-whole-plane-theta-coverage.md),
Theorems 1/1a/3/4 and Section 4.1. Its pointwise threshold there was
n_source/log(t/(2pi))>1/2. The new v4 Theorem 1b is the material change:
it imports the same fixed half-plane used in L461 and lowers the
threshold; it does not remove its lower cutoff. The earlier assessment
remains accurate for the version and target it assessed.

C460b supplies the conditional closed band
(53/256)log(a/(2pi))<=n<=(27/128)log(a/(2pi)) at every sufficiently
large positive a. Its full statement and exact normalizations were
read; its analytic proof was not re-audited. The proposed source tail
has no upper cutoff and a different lower range. Canonicalizing that
source is worthwhile overlap integration, not a new positivity discovery.

L255 already contains the product-based compact all-level mechanism;
Sra's coefficient argument should not be independently rederived as
new mathematics. The September first-sign assessment supplies no
uniform compensation theorem at arbitrary centers. The
[first-sign masking record](../../ATTEMPTS/2026-09-23-first-laguerre-masking-test.md),
[finite-level record](../../ATTEMPTS/2026-09-23-finite-laguerre-multiplicity-masking-test.md)
and [count/gap record](../../ATTEMPTS/2026-09-27-count-and-gap-first-sign-test.md)
refer to canonical L251, L257 and L354. They stop generic finite-sign
or coarse-count sufficiency, not a new theorem about actual Xi.
No fresh countermodel was constructed.

L462's audited subthreshold fixed-anchor stop and L322's exterior
stop remain in force on their domains. No contour optimization or
tail estimate is reopened. L461's B_c is existential and must still
satisfy its witness construction. Central zeros remain permitted;
no normalized division by Xi(a) is allowed. Both boundary lines,
effective onset, bounded-height overlap, initial signs, mixed positivity
and selected-law realization remain unresolved.

The retained external citation is September 30 Theorem 1.1 at commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a: strict Re(s)>7/8, pole
allowed, manuscript and formal import closure locally unaudited.
The new manuscript's report does not upgrade that trust status.
Full matching Mathlib coverage and supporting API coverage were not
checked; no absence claim is made.

## Search record and bounded route decision

Queries on 25 October 2026:
- Riemann Xi "Laguerre" "logarithmic" positivity
- "logarithmic-order" "Laguerre"
- "Sra" "positivity" "Xi" 2026
- "Laguerre" "Xi" "all" "small orders" positivity 2026 logarithmic
- "Riemann" "Laguerre" "initial" inequalities logarithmic order
- "Generalized Laguerre positivity at growing orders"

Only primary texts and reused inspected assessments support the
comparison. Other returned entire-function and Laguerre-polynomial
papers were discovery leads, not imported theorems. No exhaustive
search or novelty claim is made.

Decision: full initial-segment coverage is absent from the inspected
theorem statements. Park that particular hoped-for source shortcut.
A precise upper-tail import is separately assessed in
[the import coverage](2026-10-25-logarithmic-upper-tail-import-coverage.md).
That newly written assessment receives separate approval next turn;
no source result was installed in a lemma during this literature-only
invocation. It changes neither the current argument nor RH status.
