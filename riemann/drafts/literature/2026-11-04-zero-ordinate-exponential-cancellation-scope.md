# Oscillatory zero-ordinate input — completed comparison

TARGET: Assess whether unconditional theorems in Garunkstis--Sourmelidis--Steuding arXiv:2505.14228 give S(T,tau)=sum_{T<gamma<=2T} exp(-i*tau*log(gamma))=o(T log T), with zero multiplicities uniformly for T<=tau<=2T, and identify the remaining real-part-weight and sign-transfer gaps for actual-Xi witnesses.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact arXiv/title and unconditional ordinate-sum searches, followed theorem/referral structure, and checked Selberg S(t) moments as a stronger-input comparison. Scoped local duplicates/failures and saved signed-count/charged-block assessments checked; no matching local dyadic specialization found. No novelty inference.
SOURCE_EVIDENCE: Garunkstis--Sourmelidis--Steuding 2505.14228v1 (20 May 2025), Theorems 1--3/Corollary 1 pp.1--3, complete Section 2 pp.3--5 and Section 3 pp.5--8 including K1--K7/endpoints. Chirre--Quesada-Herrera 2006.08503v2 (6 October 2021), conventions p.1 and unconditional Selberg restatement (1.4) p.2, reference [24]/Theorems 6--7. Original Selberg proof not retrieved. Exact citations/limits below.
COMPARISON: Theorem 1 has O(|tau| log^2 x) error, inadequate in the nominated band. Theorem 2 concerns complex zero nodes, while its pure-ordinate Corollary 1 assumes RH. Section 2's Stieltjes identity plus the standard unconditional Selberg moment offers a separate specialization; no dyadic bound is derived here.
GAP: Localize the identity to (T,2T], estimate uniformly in tau, and justify multiplicities/endpoints. A scalar estimate still leaves beta weights, smaller windows, analytic costs, paid positive margins and initial signs unresolved.
REASON: New theorem-level evidence rules out direct use of the RH corollary and supplies standard inputs for a separate elementary specialization. Newly written continuation coverage requires supervisor approval next turn; no mathematical invocation or original cancellation theorem.
LITERATURE_REASON: New primary lead had essential unread theorem/proof cases; source coverage, rather than a quota, required this review.

## Relevance and source-level decision

The main gap is actual-Xi mixed positivity and initial Laguerre signs.
The intermediate target is exactly TARGET. A paid signed witness remainder
is a plausible downstream use; no witness realization, margin or sign
transfer is assumed. Direct import fails the exact hypothesis test.
This is source-scope evidence, not a counterexample or a proof that the
desired sum cannot be small.

[Garunkstis--Sourmelidis--Steuding v1](https://arxiv.org/html/2505.14228v1),
*The Lindelof Hypothesis for Zeta Zero Ordinates*, Theorem 1, gives an
unconditional formula with error O(|tau| log^2 x). Theorem 2 instead uses

    I(x,y,tau) = sum_{x<=gamma<y} (gamma+i(1/2-beta))^(-i tau),

for comparable x,y>=2 and 0<=tau<<x log x. Its two cases meet at
c x log 2, fixed 0<c<1; the larger-tau case is a stationary-phase prime
sum. The pure-ordinate Corollary 1 explicitly assumes RH. Theorem 3
equates a supplied exponent A in [0,1/2] for G(1/2+it) with a sum-error
estimate; it does not assert a better unconditional A.

The relevant Section 2 proof uses the total count, the smooth
Riemann--von Mangoldt term, f'(u)=O(u^(-2)), and (8), namely integration
by parts for integral u^(-i tau) dS(u). Its endpoint term and integral
i tau integral S(u)u^(-1-i tau) du must both be kept. Its final pointwise
estimate can be compared with a standard moment input.

Section 3's residues retain zero orders. The stationary-phase K1--K7
cases and its endpoint-shifting paragraph were inspected. Display (11)
states a log-derivative bound without a good-height qualification.
That arbitrary-height argument is not independently certified here;
the proposed continuation avoids it.

The [published version](https://doi.org/10.1007/s11139-025-01208-1) is
Ramanujan J. **68**, article 57, published 16 September 2025.
Only abstract/metadata/references were accessible; no identity with its
published proof is asserted. Screenshot requests failed; readable HTML
and PDF text supply the evidence, not a visual-verification claim.

## Standard moment input, exact citation and limits

Selberg, *Contributions to the theory of the Riemann zeta-function*,
Arch. Math. Naturvid. **48** (1946), no.5, 89--155, Theorems 6--7,
is the original citation for the standard unconditional second moment.
Its exact statement was inspected in
[Chirre--Quesada-Herrera, arXiv:2006.08503v2](https://arxiv.org/html/2006.08503v2),
Section 1.2, (1.4), PDF p.2:

    integral_0^X |S(u)|^2 du
      = X/(2 pi^2) log log X + O(X sqrt(log log X)), X -> infinity.

Section 1.1, p.1 defines the argument along 2 -> 2+it -> 1/2+it,
averaged at jumps, and counts all strip zeros with their orders and
half weight at an endpoint. The unconditional statement is (1.4);
that paper's own Theorem 1 is RH-dependent and is excluded.

The original Selberg proof was not retrieved or independently checked.
This is an import of a named standard theorem by precise citation,
with its hypotheses pinned down by an explicit modern restatement,
not a claim to have read the original. A reproof is unnecessary for
the elementary application; only the moment upper bound is needed.
The next step must localize before applying it. No Cauchy--Schwarz
estimate, dyadic little-o result or new lemma is derived in this turn.

L467's hypotheses/conclusion and closed-endpoint argument were read;
its unit shells retain every multiplicity and coincident ordinate.
Reuse the assessed Brent--Platt--Trudgian Lemma 2/count conventions in
`2026-10-07-signed-count-oscillation-comparison.md`. The published author
offprint's first-page endpoint and multiplicity conventions were also
checked. Its monotone nonnegative-test lemmas do not apply directly
to a complex exponential. L018 is relevant only to later Xi transfer.

## Comparisons, recorded failures and bounded search

Reused `2026-11-01-charged-block-bad-height-measure.md` for Simonic
1910.08274v2 Theorem 1/Section 4.5. Reopened its statement/conventions
and (73)--(75), including the microscopic band and endpoint paragraph.
These are density inputs, not the parked uniform unit-height census.
They may inform future beta-weight removal; no replacement is derived
or selected here. The existing charged-union failure is preserved and
is not a general ban on other applications.

Queries included `"2505.14228" "unconditional"`, `"zero ordinates"
"exponential sums" unconditional cancellation gamma tau`,
`"Gonek" "Graham" "Lee" "Lindelof" ordinates`, and
`Selberg S(t) second moment integral log log T theorem unconditional`.
Gonek--Graham--Lee's primes paper, Fujii's fixed-tau theorem,
general-sequence papers and improved G bounds remain unread leads.
Snippets are not theorem inputs. GSS itself distinguishes Fujii's
fixed parameter from the desired uniformity. No exhaustive absence
or originality claim follows from these searches.

## Continuation and abandonment test

The separate elementary calculation is specified in
`2026-11-04-zero-ordinate-selberg-specialization.md`, pending separate
supervisor approval. Continue only if the localized identity, standard
moment and endpoint inputs establish the exact uniform threshold
without RH, Lindelof, simplicity or a typical-height restriction.
Otherwise preserve the failed estimate and stop that specialization.
Beta-dependent weights, smaller-window transfer, paid analytic costs,
positive margins and initial signs remain independent gaps.

Full matching Mathlib coverage is **not checked**. Outcome:
NEGATIVE / LITERATURE / NOVELTY_UNCHECKED: new hypothesis mismatch and
route evidence, no mathematical count advance. PROOF/DAG unchanged.

## Original nomination retained

## Purpose and bounds of the nomination

The main gap is actual-Xi mixed positivity and initial Laguerre signs.
A usable signed zero-sum cancellation estimate could support a witness
remainder estimate without replacing the signed sum by an absolute local
count. This is only a plausible downstream use. Dyadic-to-local transfer,
real-part-dependent weights, analytic costs, the witness's positive margin
and initial signs remain independent unresolved questions. No realized
witness is proposed here, and this nomination is not a new mathematical
claim or a claimed creative advance.

In the proposed sum gamma ranges over positive ordinates of nontrivial
zeta zeros with orders; separate zeros sharing an ordinate remain separate
terms. T and tau are real, T tends to infinity and T<=tau<=2T. The little-o
is uniform in this whole band. No typical-height, fixed-tau, average-tau,
RH or Lindelof substitute meets this target. The registered fixed strip
and its source qualifications may be retained as context but may not be
silently substituted for a stronger theorem hypothesis. L018 supplies
only the Xi zero correspondence if a later witness application uses it;
L467 supplies an existing total-count comparison, not cancellation.
No new local lemma is an input to this nomination.

Inspect the primary theorem statements and the relevant unconditional
proof case first; follow only essential references. Retain the paper's
actual version and theorem/page numbers. Compare any stronger theorem
before proposing a reproof. The abstract alone approves no research.
Continue only with a hypothesis-matched import/specialization or a
bounded documented gap. If the uniform band is not covered, state the
actual range and stop that proposed application; do not call noncoverage
a counterexample. If the source is inaccessible, park it and select a
source-covered independent mathematical test rather than repeat access
loops. No mathematical script or lemma is authorized by this nomination.
Full matching Mathlib coverage is unchecked.
