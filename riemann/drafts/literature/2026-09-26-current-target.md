# Endpoint weighted fourth-moment literature assessment

TARGET: Test M_N(N^(-1/8))=o(1) from L351 at the exact dilation 1, using a fourth-moment bound for C_N under the weight w_N(ν)w_N(μ)/W_N²; the sufficient fourth-moment threshold is o(N^(-1/2)).
CHECKED: 2026-09-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Searches on 2026-09-26 for Dirichlet-polynomial discrete fourth moments, weighted rational-ratio sampling, lacunary sums with Fourier-decaying measures, and 2025–2026 large-value estimates; Guth–Maynard Lemma 11.6 is the closest inspected statement, but no full weighted match was found.
SOURCE_EVIDENCE: Guth–Maynard, arXiv:2405.20552v2 (2026-04-07), Theorems 1.1/1.6, §1.2, (7.2), Lemmas 8.3 and 11.5–11.7, especially Lemma 11.6 and proof pp. 41–42, https://arxiv.org/pdf/2405.20552v2; Tan–Zhou, arXiv:2409.03331v1, Theorem 1.8 p. 8, https://arxiv.org/pdf/2409.03331v1; Matomäki–Teräväinen, arXiv:2403.13157v1, Theorem 1.2/Remark 1.3 p. 2, https://arxiv.org/pdf/2403.13157v1; Chen–Gupta–Li, arXiv:2507.08296v2 (2026-07-27), Theorem 1.1 pp. 1–2, https://arxiv.org/pdf/2507.08296v2.
COMPARISON: Guth–Maynard bounds an unweighted fourth moment on a dyadic rational grid, with additive-energy and T^(1/2), T^ε losses; the notebook needs its maximum-coefficient weights on all ratio differences with N samples spanning T comparable to exp(8N). Metric lacunary results do not provide the missing atomic weighted estimate. L351's O(1/N) dilation average is insufficient at dilation 1.
GAP: Bound the complete weighted fourth moment at the prescribed a_n by o(N^(-1/2)), including every ratio collision, unequal numerator/denominator scales, tails, and explicit losses on the N scale; no checked theorem supplies this estimate.
REASON: The essential Guth–Maynard lead has now been read at theorem and proof level. Retain the exact saved target for bounded exploration of the weighted specialization; cite covered grid results, and do not infer success from separation, additive energy alone, or an almost-everywhere statement. No target estimate or novelty claim is established by this review.

## Scope and relevance

This completes the literature-only review of the unchanged TARGET above.
No new estimate is derived here. The earlier migration assessment left the
Guth–Maynard theorem unread; the source comparison below replaces that gap.
The full overview, DAG, local goals, checkpoint, L349–L351, the relevant
earlier obstruction statements, and the saved Gram assessment were inspected.
There were no pre-existing changes inside this notebook; changes elsewhere
in the shared repository were preserved.

The immediate gap is L350's deterministic sampling condition at the actual
endpoint heights. The proposed intermediate target is the fourth moment

\[
 \sum_{\nu,\mu\in F}\frac{w_N(\nu)w_N(\mu)}{W_N^2}
       |C_N(\omega_\nu-\omega_\mu)|^4=o(N^{-1/2}),
 \qquad C_N(x)=\frac1N\sum_{n=N}^{2N-1}e^{ia_nx}.
\]

Here all notation, including the maximum over n in w_N, is exactly that
of L351. Its equal-frequency contribution B_N/W_N² is already O(1/N).
The sufficient threshold and its Markov implication for
M_N(N^(-1/8)) are the saved target in the
[previous assessment](../../ATTEMPTS/2026-09-26-endpoint-mellin-width-gram-test.md),
not a new result of this review.

Plausible downstream use: L351 (17) would give H_N(1)=o(1), and L350
would then give a vanishing discrete relative mean. Exceptional sampled
indices would still need control. The actual endpoint assembly needs a
positive arithmetic margin exceeding (1+2n)²exp(−2n/256) at every
prescribed pair. Remaining low Laguerre indices also remain unresolved.
Neither this moment target nor its successful proof alone would resolve RH.

## Search record

Queries included:

- `Guth Maynard New large value estimates Dirichlet polynomials theorem 1.1 1.2 fourth moment`
- `"Dirichlet polynomials" "discrete fourth moment"`
- `"Guth" "Maynard" "weighted" "fourth" "lacunary"`
- `lacunary exponential sums fourth moment discrete measure logarithms rationals geometric progression`
- `lacunary sequences discrepancy Fourier decay measure theorem Pollington Velani Zafeiropoulos Zorin`
- `"large value estimates" "Dirichlet polynomials" 2026 2025 arxiv`
- `"A Large Values Estimate for Dirichlet Polynomials" Heath Brown pdf`

The exact discrete-moment search led to Guth–Maynard's internal lemma,
which is substantially closer to the target than its headline large-value
theorem. The measure search led to a theorem allowing real lacunary
sequences. The later-source search led to the character extension below
and the reverse zero-density implication. Searches with the notebook's
more specialized combination of weights and frequencies supplied no exact
match. This is bounded discovery, not evidence of originality.

## Inspected sources

### Guth–Maynard: the closest fourth-moment statement

Larry Guth and James Maynard, *New large value estimates for Dirichlet
polynomials*, [Annals publication record](https://annals.math.princeton.edu/2026/203-2/p06).
The text read was [arXiv v2, 7 April 2026](https://arxiv.org/pdf/2405.20552v2),
with its [HTML mathematical text](https://arxiv.org/html/2405.20552v2).
Inspected: Theorems 1.1/1.6 (pp. 1, 4), §1.2 (p. 5), the separated-set
setup in §3, (7.2), Lemma 8.3, and Lemmas 11.5–11.7; the complete proof
of Lemma 11.6 was read (pp. 41–42).

For R(v)=Σ_(t∈W)|v|^(it), E(W)=#{|t₁+t₂−t₃−t₄|≤1}, and a separated
set W in an interval of length T, [Lemma 11.6](https://arxiv.org/pdf/2405.20552v2#page=41)
gives, for M≥1,

\[
 \sum_{k,l\sim M}|R(k/l)|^4
 \lessapprox |W|^4M+M^2E(W)+E(W)^{3/4}|W|T^{1/2}M.
\]

The paper's ≲≈ allows C_εT^ε for every fixed ε>0. Its proof groups
differences into unit bins and uses Heath-Brown's estimate (Theorem 1.6).
Lemma 8.3 instead integrates over v. Theorem 1.1 counts separated large
values of ordinary Dirichlet polynomials with bounded coefficients.

### Tan–Zhou: a real-lacunary metric theorem

Bo Tan and Qing-Long Zhou, *Quantitative Diophantine approximation and
Fourier dimension of sets: Dirichlet non-improvable numbers versus
well-approximable numbers*, [arXiv v1, 5 September 2024](https://arxiv.org/pdf/2409.03331v1#page=8).
Read the introduction's measure setup and Theorem 1.8, p. 8.
For a positive real lacunary sequence, a fixed probability measure μ on
[0,1] with |μ̂(t)|≪(log |t|)^(-A), A>2, and the stated shrinking targets,
it gives a counting asymptotic with error
O(Ψ(N)^(1/2)(log(Ψ(N)+2))^(3/2+ε)) for μ-almost every x.
This addresses real, not just integer, frequencies, but requires the
Fourier-decay hypothesis. It does not assert the notebook's weighted
fourth moment. The inspected version is the preprint; journal-version
changes were not compared.

### Two adjacent large-value results

Kaisa Matomäki and Joni Teräväinen, *A note on zero density results
implying large value estimates for Dirichlet polynomials*,
[arXiv v1, 19 March 2024, Theorem 1.2 and Remark 1.3, p. 2](https://arxiv.org/pdf/2403.13157v1#page=2).
The theorem bounds the size of the large-value set for ordinary sums
Σ_(M<m≤M′)m^(-1-it), with T^ε≤M≤T^(1/2)/2, in terms of zeta
zero-density estimates. The remark treats Möbius/prime variants with a
different error. These are inspected statements, not an import of a
zero-density hypothesis. They give no asserted estimate for the present
weighted ratio-pair distribution at a_n.

Bin Chen, Vishal Gupta and Yung Chi Li, *Large Value Estimates for
Dirichlet Polynomials with Characters and Zero Density of Dirichlet
L-Functions*, [arXiv v2, 27 July 2026, Theorem 1.1, pp. 1–2](https://arxiv.org/pdf/2507.08296v2#page=1).
Read the full statement and the following q=1 comparison. It counts
separated pairs (t,χ) for bounded-coefficient Dirichlet polynomials of
length at least (qT)^(2/3). For q=1 in the indicated range it recovers
the Guth–Maynard bound. Adding characters does not supply the missing
weight transfer or remove its height dependence. No claim is made about
uninspected internal refinements of this paper.

## Applicability and threshold comparison

The following comparisons concern the notebook's definitions; they are
not new estimates or applications of the cited inequalities.

1. **Use the correct variables.** For comparison with the ratio moment,
   the source's W would be {a_n: N≤n<2N}, of cardinality N; it is not
   the notebook's scalar W_N. Its samples have large gaps, as already
   recorded in L351 (15). The ratio arguments are (qu)/(pv) for
   ν=(p,q), μ=(u,v). These are the products already grouped in L351 (9).
   Thus a dismissal based only on the nonseparation of log-rational
   arguments would miss the closest known result: the dual source setup
   separates the height samples.
2. **The required measure differs.** The notebook uses all reduced
   frequency pairs with weights w_N(ν)w_N(μ)/W_N² and all numerator/
   denominator scales. The source grid statement alone provides no
   estimate for that distribution. The maximum in w_N must be retained;
   neither independent random phases nor uniform counting of ratios is
   an established replacement. L351 (9) supplies a positive grouped
   majorant, but its weighted fourth-moment cost has not been evaluated.
3. **The two asymptotic parameters differ.** The actual sample formula
   places their diameter at order exp(8N), while the requested saving is
   a power of N. The height losses in the displayed source bound cannot
   silently be absorbed into N^ε. A bound with unspecified subpower loss
   in the height variable is insufficient to certify this logarithmic
   saving. No substitution ε=ε(N) is justified without controlling its
   constants. A small additive-energy estimate, even if established,
   would leave the other terms and the weight transfer to check.
4. **Metric hypotheses remain unproved.** L351's weights describe an
   N-dependent countable atomic distribution on log-rational differences.
   No Fourier-decay estimate for that distribution is recorded. The
   metric theorem cannot be used by substituting an unrelated measure,
   and it does not control these atoms through a Lebesgue exceptional
   set. L351's own O(1/N) dilation average and H_N(0)=1 already warn
   against a pointwise inference from a small exceptional measure.

Known achieved scale: the collision contribution is O(1/N), which is
smaller than the sufficient o(N^(-1/2)) fourth-moment threshold. Missing
scale: the remaining weighted pairs at exactly dilation 1. No inspected
external result supplies a bound for them at that threshold. Failure of
a direct citation is not a lower bound for the actual moment.

## Reuse, prior failures, and continuation test

L344–L345 already reject the tested fixed-order derivative certificates
in the sample index and stationary dual. L346 tests an unweighted
full-support norm with the older normalization; L347–L348 test weighted
norm separation with diverging mass. L349–L350 change that mass and
variation budget. None proves the current fourth-moment target false.
The current intermediate question is therefore distinct, but those old
certificates should not be repeated under a new name. Extending finite
zero-exclusion certificates would not address this sampling gap.

Decision: retain the exact TARGET for bounded exploration. Reuse the
known rational-grid moment by citation wherever its hypotheses actually
fit. Any specialization must identify and justify the weighted ratio
distribution, scale decomposition, tails, and explicit dependence on
sample count and height. Reproving the unweighted lemma would add no
needed input.

The discriminating test is the complete normalized fourth-moment budget:
continue this implementation only if it reaches o(N^(-1/2)), or if a
proved intermediate estimate isolates a concrete remaining contribution
with a credible way to meet that threshold. If the best justified budget
still contains an uncontrolled height loss on nonnegligible weight, stop
that implementation and reassess; do not claim that the target is false.
No low-energy specialization, tail bound, or new collision calculation
is performed in this literature turn.

This review uses one consecutive unresolved exploration turn, out of
three. It is EXPLORATION: the source comparison is now adequate to guide
the saved test, but neither a new mathematical input nor an informative
mathematical obstruction has been established. A later result meeting
the target would go beyond the conclusions checked here; originality
has not been established. No target theorem is imported or reproduced.

## Access boundaries and Mathlib

The essential Guth–Maynard source is fully accessible in the version
cited above. The Oxford accepted-manuscript download returned an error;
the arXiv text resolved access to the theorem and proof. The original
[Heath-Brown 1979 paper](https://doi.org/10.1112/jlms/s2-20.1.8)
was followed, but its PDF link returned a bibliographic landing page.
Its original proof was not read. The present comparison uses the explicit
statement in Guth–Maynard and their own proved Lemma 11.6; it does not
assert a sharper version of Heath-Brown's estimate. Any attempt to improve
that input's hidden losses would need a separate source assessment.
Survey, seminar, and search-summary leads were not used as theorem
evidence. The full-target search is not exhaustive.

Mathlib coverage of the full target: **not checked**. Existing supporting
Euler-product and reciprocal-series references remain in L349–L351 with
their qualifications, including
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re)
and
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These links were not rechecked and are supporting inputs only, not a
match for the weighted discrete moment.
