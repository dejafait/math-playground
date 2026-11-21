# Shifted balanced-semiprime source comparison1451

18 November 2026. Literature only. This completes nomination1450's exact
TARGET; no determinant transformation, new coefficient estimate or
arithmetic asymptotic is derived. Main gap: L030--L032/C032a actual-Xi
all-degree positivity. The intermediate question is whether a primary
shifted-correlation theorem pays C020l(5) at O(Bq^2). Such a payment
could support the frozen fourth moment, leaving the independent
transfers listed below unresolved.

## Scope, reuse and search

Read C020l in full, including audit1450. Reused source-notes1418's BCR
Section3.2 and Bettin--Chandee Theorem1 comparisons, review1447's
prime-versus-zeta exclusions, and stops1431/1437/1446. Also read
stops1419/1426/1428 and working1419 to distinguish the proposed
determinant test from the previously stopped mixed source-ratio
implementation. The local search covered the named Jensen assessments
and attempts, not other notebooks. No cross-notebook input is used.

Queries actually issued:

- `"balanced semiprimes" correlations shifted`
- `Evans correlations almost primes theorem shifted E2 products primes`
- `shifted convolution balanced primes products primes correlation asymptotic weights`
- `"correlations" "semiprimes" "balanced" theorem`
- `"Correlations of almost primes" balanced factors weights 2025 2026`
- `"products of two primes" "correlations" "X" balanced`
- `"shifted convolution" "prime" "prime" "bilinear" semiprime`

Search results were discovery only. The primary theorem read is below.
Unrelated numerical semiprime patterns, conditional prime hypotheses,
function-field formulas and secondary summaries are not evidence.
The thesis and talk hits were not read and supply no theorem here.
This bounded search establishes neither novelty nor global absence.

## Inspected primary statements and essential proof cases

Natalie Evans, *Correlations of almost primes*, Math. Proc. Cambridge
Philos. Soc. **174** (2023), 301--344, first published 9 June 2022,
DOI [10.1017/S0305004122000251](https://doi.org/10.1017/S0305004122000251).
Read the [publisher's complete primary HTML](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/correlations-of-almost-primes/08F8E4E4C36F68ED6DDA373CCAF7A221),
Theorems1.1/1.3/3.2, Definition3.1, Sections4--5,6.1--6.2 and9's
relevant cases. Source length is denoted Y here, avoiding notebook X.

Theorem1.1 fixes epsilon>0, A>3 and
log^(19+epsilon)Y<=H<=Y log^(-A)Y. It counts E2' with one factor in
(P,P^(1+delta)], delta fixed sufficiently small; P=log^(17+epsilon)Y
when H<=exp((log Y)^(epsilon^3)), otherwise
P=exp((log log Y)^2). Its normalized correlation is asymptotic to
S(h) times the squared E2' density outside O(H log^(-eta)Y) shifts,
eta=eta(epsilon)>0. Definition3.1 uses weight log p2; Theorem3.2 gives
main term S(h)Y(sum_(P<p<=P^(1+delta))1/p)^2 and error
O(Y log^(-eta)Y), with that exceptional set. Theorem1.3 instead counts
all E2, requires exp((log Y)^(1-epsilon))<=H<=Y log^(-A)Y and allows
O(H log^(-D)Y) exceptions for fixed D>0.

Section4 treats diagonal and off-diagonal terms separately, with
dyadic splitting in its second H case; Section5 retains the singular
series. Section6.2 separates principal and nonprincipal characters.
Section9 reduces to typical smaller factors, imposes
H>=P2 log^(C+D)Y in (9.2), and retains diagonal cost
Y P log Y/(H log P) in (9.3). No arbitrary balanced weighted version
is stated.

These are source statements and inspected proof features, not results
imported for our coefficients. No underlying source theorem is
reproved or independently certified here. The apparent theorem-number
typo in Section9's opening does not replace its actual heading or
Theorem1.3 statement.

## Exact comparison and decision

1. **Support.** C020l requires both source primes in the same
[sqrt(X)/10,sqrt(X)/5] window, on both sides of the difference.
Evans Theorem1.1's P is prescribed and is not a free parameter to set
to sqrt(X). Its unbalanced family cannot simply replace this support.
Theorem1.3 is a statement about all E2 and its full density. It is
not an asymptotic for an arbitrary subfamily; subtracting an unspecified
complement or appealing to positivity does not recover our signed
balanced subfamily. Section9's typical-factor deletion is made on the
source's unrestricted counting scale, not on C020l's weighted budget.

2. **Equation and gcd cases.** The inspected correlation is n,n+h.
C020l has prs-p'r's'=h with unequal s,s'<=L^4 and four individual
tapers. Substituting n=prs changes the arithmetic function and its
congruence restrictions. The theorem supplies no uniform family with
these multipliers, no associated local main terms, and no summed
error over their gcd strata. Shared source primes and shared small
factors therefore remain part of an applicability argument. No claim
that a particular stratum is empty or negligible is proved here.

3. **Weights and kernel.** The source's indicator/logarithmic weights
are prescribed. C020l's r_s, complex E_p(Z), reciprocal square-root
factors and W_X(log(l/k)) remain necessary. The latter includes
exp(ic xi), not just an additive shift weight depending on h.
Partial summation would require a weighted uniform statement and its
variation costs; it is not justified by quoting an unweighted count.
The original logarithmic near cutoff cannot be replaced by its larger
integer-width envelope when evaluating a main term.

4. **Main term and total error.** Evans's singular-series main term
does not vanish by the theorem. No cancellation of its hypothetical
analogue against W_X has been supplied. Nor does an almost-all-shifts
formula pay the exceptional shifts under our signed, nonconstant
weights. There is consequently no legitimate total error expression
for this target to compare numerically or asymptotically with Bq^2.
The actual source error above must not be reported as an O(Bq^2)
error after summing over s,s',h. Even arbitrarily strong logarithmic
precision on the wrong support does not settle this applicability gap.
This rejects the direct import before any unsupported aggregate bound
is made; it does not prove the desired sum is large.

The completed bounded comparison is EXPLORE, not IMPORT or SPECIALIZE.
Access succeeded; there is no essential inaccessible theorem being
assumed. Further browsing of the same Evans statements is not the next
step. The explicit support/equation/weight mismatches stop that import.
This is new source-scope evidence and a route decision, not progress
beyond known mathematics or a disproof of the frozen moment.

## Bounded handoff and its limits

Nominate one gcd-resolved additive-character test of the **original**
C020l(5) near determinant. Its precise target and source limits are in
assessment1451. The materially different object is the already audited
high-height finite moment, not C020c's stationary rational mixed
channel stopped in1419. Neither the old f2 modulus theorem nor the
inverse-phase estimate is automatically applicable. Actual moduli,
coprimality and weight separation must be exposed, not guessed from
s,s' being small. No completion to unrestricted divisor coefficients,
pointwise saddle deletion or absolute-neighbor budget is authorized.

The test is useful only if it supplies a quantitative signed payment,
a source-compatible transformed sum with a quantified remaining cost,
or an informative obstruction to this specific implementation. A finite
identity alone does not meet the continuation test. Stop at the first
unpaid zero-mode or nonzero-mode term if its full cost cannot be placed
against Bq^2; preserve the residual and reassess rather than repeat
regrouping. This nomination proves none of these transformations.

Essential inputs: C020l(1)--(15) with audit1450; C019p's absolute-alpha
convolution and C019y/C019z's integer-d scales/heat facts. Preserve fixed
Z in J, all four unshifted tapers, all source pairs and their common
factors, both orientations, and the translated kernel. Uniform near
payment, two own heat times, shifted intervals, distinct-pair transfer,
motion, real denominator, signed numerator, E_P and actual-Xi transfer
remain unresolved. Full matching Mathlib coverage is unchecked.

No justified central creative mechanism is supplied by this source
comparison: a paying signed-arithmetic/all-degree-Xi link remains absent.
The bounded nomination is established-route development and receives
separate approval next turn. No lemma, mathematical script, PROOF or
DAG edit is part of this literature step.
