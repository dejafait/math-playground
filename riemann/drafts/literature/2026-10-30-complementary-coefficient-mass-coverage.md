# Complementary coefficient mass — completed source comparison

TARGET: Assess coverage for certifying C_N=sum_{m>N}|beta_m|m^(-sigma)h_ell0(m) at L497's fixed corner by grouping through H=160N and bounding the remaining positive channels, against .301408572679396256667379418689.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the finite-support and grouped-resultant assessments; targeted search of their working notes, prefix history and scripts/heat Python/Markdown found no matching complementary-moment implementation. New web queries recorded below supplied no relevant theorem; no novelty inference follows. Charge-approval, tail-approval and direct numerical high-zero-tail stops were checked for scope.
SOURCE_EVIDENCE: Retrieved Planat arXiv:2609.37164v2 (7 October 2026), primary HTML Section 6.6 and PDF pp.22-23: exact definitions, equations (40)-(41), both cases and complete proof of Lemma 6.7, Proposition 6.8's table and complete computational proof, followed by its handoff correction. Reused inspected equation (44), p.26, from the grouped-resultant assessment; no source producer or supplementary ledger verified.
COMPARISON: The source gives the entire finite-channel formula needed for a fixed-corner upper certificate and reports the stronger full M_160<.999577540. L497 verifies only the prefix. Reproduction must replace the source's variable denominator by the specified rational ell0 and enclose every edge coefficient and both moment cases; the source decimals are feasibility evidence, not certified local bounds.
GAP: No local grouped-edge or complete tail enclosure yet exists. Essential implementation obligations are H<exp(ell0), exhaustive signed grouping through H, safe split floors, outward Euler-moment subtraction and total error below the available budget. Charges and collision exclusion remain independent gaps.
REASON: Missing exact source coverage is now supplied without deriving a new result. SPECIALIZE covers only the fixed-corner reproduction below; a separate next-turn approval of its new exact-target assessment precedes calculation. No lemmas or mathematical scripts changed.
SCOPE: Fixed t=.16836, x=6000284561421.5, N=691004, primes p<=307, L496's exact sigma and rational ell0=24.18022820120389, H=160N=110560640. All finite decimals are exact. No time/height transport, derivative claim, charge certificate or endpoint is covered.
LITERATURE_REASON: The new complementary quantity lies outside the ready prefix scope; its essential unread details were the exact clipped-tail parameters, large-divisor moment case and computational conventions. Prior overlap and failure comparisons were reused.

## Source extraction and applicability

Michel Planat, *Collective Contraction in the de Bruijn–Newman Heat
Flow: Off-Zero Logarithmic Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.6](https://arxiv.org/html/2609.37164v2#S6.SS6),
[PDF pp.22-23](https://arxiv.org/pdf/2609.37164v2), is the primary input.
The HTML formulas and full PDF text of these pages were inspected.
The formulas below transcribe the source, rather than supply a new proof.
Its proof is finite splitting at dq=T and the finite Euler-product
moment expansion. The inherited global assembly is not imported.

In (40), w_q=exp(t*log(q)^2/4)*q^(-sigma), r_p=w_p,
r_d=product_(p|d) r_p and a_m=beta_m*m^(-sigma), with every
squarefree supported divisor d|m satisfying 1<=m/d<=N included.
The source groups 2<=m<=H, with N<m<=H the entire grouped edge.
It uses unweighted absolute values in this range only because H<T.
Above H, (41) retains all positive channels r_d*w_q*h(dq) with
1<=q<=N and dq>H; it does not stop the divisor sum at H or T.
The empty divisor d=1 is part of the finite expansion. The total
support is finite, but its full 63-prime expansion is not a proposed
enumeration strategy.

Lemma 6.7 uses positive ell, T=exp(ell), H<T and the prefix moments

    A(y)=sum_(1<=q<=min(N,max(0,floor(y)))) w_q,
    B(y)=sum_(1<=q<=min(N,max(0,floor(y)))) w_q*log(q).

In particular A(0)=B(0)=0 and B(1)=0. The lemma is stated in the
source's H<T context; it must not be used as a formula for arbitrary
H>T. For each squarefree supported d<=T set

    q0=min(N,floor(H/d)), qc=min(N,floor(T/d)).

Its exact positive-channel contribution for dq>H is

    r_d * ( A(qc)-A(q0)
      + (2/ell)*(log(d)*(A(N)-A(qc))+B(N)-B(qc))
      - (A(N)-A(qc)) ).

Thus the unit-weight part includes q0<q<=qc, and the logarithmic
part includes qc<q<=N. Both endpoints are included exactly as in
the displayed floors. At dq=T either weight expression agrees.
Clipping at N includes channels with qc=N and hence no logarithmic
part. In this d<=T case qc>=1; the d>T case is handled separately
below. These cases cannot be replaced by an unclipped integral or
an asymptotic tail.

For the other case the source defines

    R=product_(p in P)(1+r_p),
    Rlog=R*sum_(p in P) (r_p/(1+r_p))*log(p),
    R_>T=R-sum_(d<=T) r_d,
    Rlog_>T=Rlog-sum_(d<=T) r_d*log(d),

where the enumerated d are squarefree over P. Its complete d>T
contribution is exactly

    (2/ell)*(A(N)*Rlog_>T+B(N)*R_>T)-A(N)*R_>T.

The source explicitly permits dropping the final negative term for
an upper bound. Retaining it requires the correct lower enclosure
on the subtracted positive quantity. Residual moments are nonnegative
mathematically, but cancellation in their numerical subtraction still
requires outward intervals. These two cases cover every divisor;
enumerating only d<=H without its remainder would omit channels.

The next reproduction uses ell=ell0, the exact rational in L497,
rather than the source's height-dependent separator expression.
Lemma 6.7 is an algebraic finite-sum identity for this parameter.
The necessary numerical prerequisite H<exp(ell0) must be checked
locally, and h_ell0 must be retained until that check. The source
reports the slightly weaker separator floor 24.18022820120347 and
exp(ell_hat)>=31720474772. This explains applicability and expected
scale; neither number is a local interval certificate for exp(ell0).
L496 supplies ell>ell0 for subsequent resultant interpretation,
with its imported base-phase qualification. The finite sum itself
requires only the specified rational parameter, as in L497.

## Reproduction requirements and bounded decision test

Use complete signed coefficients before absolute values for N<m<=H,
without presuming coefficient positivity. The source's Proposition 6.8
reports 1189962 nontrivial squarefree channels through H, but a local
enumerator must verify its own completeness rather than import that
count. The source seeds elementary functions at 256 and 384 MPFR bits,
then uses outward binary64 signed convolution with fast-math and
contraction disabled. Its later description distinguishes the small
MPFR wrapper from historical MPFI calculations. None of these choices
is mandatory: rigorous integer/rational intervals or another justified
directed backend can reproduce the same mathematical quantity.

Split-floor decisions involving exp(ell0) must be enclosed. An interval
straddling an integer threshold cannot be rounded to a guessed index;
refine it or bound the disputed channels with a justified upper rule.
Every supported divisor in the chosen enumerated region needs a
completeness certificate, and the rest needs full Euler moments.
The memory/runtime strategy is not verified here; block processing is
permitted only with a proof that every retained output receives all its
divisors. The source archive is not needed to define the task, and its
unverified accessibility is not an essential source blocker.

The requested quantity C_N includes grouped coefficients above N;
the computable source certificate consists of the full grouped edge
through H and an upper bound for all remaining positive channels.
It is a majorant of C_N, not an equality with the grouped complement.
L497's certified prefix must not be added twice. Compare the complete
complement upper bound with .301408572679396256667379418689. Only a
strict upper bound below that value passes the proposed test. A partial
edge, sampled divisor set, dual-precision agreement, favorable source
decimal or an interval crossing the threshold does not pass it.

Proposition 6.8 reports edge .274932959, tail .026053154 and full
M_160<.999577540. Those are evidence that this fixed method is worth
one reproduction attempt, not a proven local error allowance. No
complement or combined bound has been calculated in this review.
If an upper certificate is too large, identify whether the loss is
grouping, moments or interval width; that alone is not a lower-bound
obstruction to C_N or a failure of RH. Continuation needs a quantified
repair; a second identical source approval does not repair the bound.

## Duplicates, failures and remaining limits

The finite-support assessment's stronger-result comparison is reused.
Queries `"2609.37164" "prefix-sum" tail` and `"Planat" "grouped corner"
coefficients` returned unrelated listings, which were not used as
theorem evidence. Targeted searches in the grouped-resultant and prefix
working/history records and scripts/heat Python/Markdown found no
matching complementary-moment implementation. This is a scoped
duplicate check, not evidence of originality or global absence.

The direct numerical high-zero-tail stop concerns an existential zero
height cutoff, not this finite divisor-channel sum. Charge/tail approval
stops concern repeating unchanged reviews. The repaired handoff in
Planat p.23 withdraws an old block-multiplicity margin; neither that
margin nor transport is needed for the single fixed-corner test.
Energy, inverse-gap and collective-landing obstructions remain with
their prior scopes. No new actual-Xi structural input justifies a
creative central proof target from this review.

The next-target assessment records ready source scope but is newly
written: its separate approval belongs to the next invocation. No
research is authorized within this literature-only step. A future
successful full mass still leaves L497's critical audit, strict reserve
above L495's two charges, H1, uniform transport, finite interior
collisions, other positive times and zero time unresolved. Matching
Mathlib coverage is not checked and remains unknown. This is local
source coverage, with no claim beyond the inspected method.

## Original nomination (historical; superseded by this comparison)

The main gap remains actual-Xi all-degree positivity. This intermediate
source review prepares a possible full coefficient-budget input for the
collision route. It does not certify the full budget or either charge.
The fixed inputs are L494's normalization/domain, L495's exact beta_m,
L496's exact sigma and ell0, and L497's prefix endpoints. Specifically
use t=.16836, x=6000284561421.5, N=691004 and primes p<=307; every
finite decimal is rational. The proposed grouping cutoff is H=160N.
The complement is a sum over all remaining nonzero coefficients of
the finite product; it is not truncated at H. Beyond H one would use
only a justified upper bound on all omitted positive channels.

The relevant source locations are
[Planat v2, Section 6.6](https://arxiv.org/html/2609.37164v2#S6.SS6)
and [the PDF](https://arxiv.org/pdf/2609.37164v2). They were already
inspected at theorem/proof-case level in the prior assessment. Reuse
that adequate coverage: the next review needs the exact tail formula,
parameter restrictions, clipped moment definitions and ledger conventions
for this different quantity, and a narrow duplicate/failure comparison.
It must not repeat the completed prefix, phase or charge approvals.
No source archive or producer is assumed accessible or correct.

The continuation test is to identify a rigorous computable bound for
all grouped-edge and complementary channels at this corner. If coverage
and a feasible complete enclosure support comparison with the stated
remaining unit budget, authorize only that fixed-corner reproduction.
If the tail estimate is too large, identify the precise loss before
choosing a changed cutoff or mechanism; no favorable source decimal
or partial subset upper sum may stand in for the whole complement.
Source inaccessibility must be recorded as such, not as a mathematical
failure. No complementary bound has been derived in this nomination.

L497's internal consumer checks every row, but its new proof/code still
await a separate critical audit. Base-phase/saddle imports retain their
qualifications; Mathlib matching coverage is unknown. Even a verified
full mass below one leaves the strict margin above L495's two charges,
uniform transport, interior collisions, other times and zero time open.
The current prefix reproduction supplies no new actual-Xi structural
inequality justifying a creative central attempt. Preserve the existing
energy, inverse-gap, contraction and charge-approval route stops.
