# Shift-zero Jacobi matching — completed source assessment

TARGET: Assess the shift-zero specialization of Holland's exact four-coefficient matching system (51)–(52) for degree five, including positive-root parameter conditions and rigorous actual-moment inputs, before a bounded feasibility test.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step474 compared the exact fixed system, broader hypergeometric root regimes and validated Taylor-jet methods; reused step473 wedge and step430 ball-evaluation coverage. Queries and inspected primary passages below; no novelty inference.
SOURCE_EVIDENCE: Holland 2608.08682v1 (1)–(4),(34)–(40),(49)–(52),(57),(66)–(74), Lemmas2.1/5.3/6.2 with proofs; Martinez-Finkelshtein–Morales–Perales 2309.10970v3 Propositions2.7/2.17, Theorem3.1/proof, Theorem4.7/proof, Table2 and Proposition4.15(ii)/factorization; DLMF18.5.7/18.3.1/18.2(vi); archived Arb2.23.0 acb_poly Gamma/Zeta-series contracts and reused step430 integration/ball assessment.
COMPARISON: Known matching identities and validated evaluation support a conventional finite test, not a central existence import. Broader known positive-root regions preclude interpreting failure of Holland (57) as nonfeasibility. Actual parameters and root simplicity still need certificates.
GAP: No numerical gamma(0..4) enclosure or actual central solution is imported. A bounded calculation must certify input balls, nonsingular denominators, exact-system existence and model roots, or report a qualified obstruction/inconclusive outcome; residual and growing-degree signs remain outside scope.
REASON: Essential source coverage is complete for one fixed n=0,d=5,D=B_J/2 test using known methods. No reproof of convolution, orthogonality or validation theorems is justified; a citation does not supply the actual numerical data.
LITERATURE_REASON: Changed hypothesis to n=0 and a particular finite matching system; the completed wedge comparison does not cover its feasibility or rigorous coefficient certificates.
SCOPE: Completed literature-only source gate. Covers the separately nominated fixed finite feasibility calculation, not central hyperbolicity, an all-degree mechanism, root scans in other families or a manuscript audit.

The original nomination below is preserved as the reviewed question.
Step474 completes its source coverage; it performs no calculation. The
new calculation continuation requires separate next-turn approval. Reuse
the completed polynomial-wedge comparison rather than repeat searches.

Essential inputs: L019/L021 for actual moments, and L776's coefficient
definition only. Use gamma(j)=8*4^j*j!*a_j. At n=0 candidate data are
R_j=gamma(j)/gamma(0), q_k=R_(k+1)^2/(R_k R_(k+2)).
The first stage (37)–(38) has an eventual positivity proof using q0>1
and 1<q1<2-1/q0; do not assume these centrally. Next fix D=B_J/2 and
solve (52) for A,B,C. Retain degree-dependent Jacobi root hypotheses,
not scalar positivity alone; retrieve precise preservation statements
if a finite-free theorem is needed.

L564 was inspected for triage only: its Hermite-tail result is not a
ready certificate for five gamma values. Identify existing rigorous
moment enclosures or assess a standard validated method. A decimal
table or arbitrary-precision approximation is insufficient.

Plausible use: decide whether the comparison family has an admissible
central starting model before investing in a residual multiplier or
degree-dependent replacement. No actual input root signs are assumed.
Success proves no new small-degree sign, uniform degree control,
prescribed-constant margin or RH.

Continue only to a bounded certified degree-five feasibility test once
essential coverage is complete. Record a parameter/root obstruction
if the fixed model fails; do not silently vary D, degree or family.
Missing growing-degree signed control blocks creative routing; the
first calculation would be conventional specialization. Mathlib
coverage is unchecked. No cross-notebook input is requested.

## Completed source comparison — step474, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is feasibility of the specified central comparison model. Its use is to
reject an inadmissible starting representation early or identify one
admissible finite model before considering a residual multiplier. Neither
outcome resolves growing-degree signs or the prescribed-primitive gap.

### Exact system and scope

Primary: Jonathan Holland, [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
9 August 2026. Reuse step473 for the wedge and eventual signed estimates.
This step inspected the finite matching cases: Lemma2.1, Lemma5.3 and
Lemma6.2, with their complete algebraic proofs; definitions (1)–(4),
(34)–(40), (49)–(52), (57), (66)–(74) and the Jacobi identity before (75).
Those identities require finite nonzero coefficient ratios and parameters;
Lemma6.1's eventual existence proof supplies no n=0 solution.

Retain gamma(j)=8*4^j*j!*a_j, R_j=gamma(j)/gamma(0) and
q_k=R_(k+1)^2/(R_k R_(k+2)). First form T,A_J,B_J,S_J by (37)–(38),
checking every division and the required positive parameters with actual
input enclosures. Fix D=B_J/2, exactly as nominated. Solve (52), k=0,1,2,
for positive A,B,C, and use S=B R_1. Lemma6.2 then matches indices 0..4;
its conclusion is conditional on an exact solution, not small residuals.
The model is the degree-five polynomial (69). No value at index5 is
needed to pose this representation prerequisite; it would be needed to
compare its remaining coefficient to the actual Jensen polynomial.

### Root hypotheses and stronger known coverage

A. Martinez-Finkelshtein, R. Morales and D. Perales,
[*Real roots of hypergeometric polynomials via finite free convolution*,
arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3), 2 May 2024;
IMRN 2024(16),11642–11687. Pin the PDF: its printed date is 3 May 2024,
whereas the HTML rendering displays an inconsistent August2026 date.
A guessed v4 HTML URL failed; the abstract identifies v3 and its PDF is
accessible. This is not a persistent source blocker.

Read Propositions2.7 (printed p.11) and 2.17 with its mesh proof (p.15),
Theorem3.1/full coefficient proof (p.15), Theorem4.7/full factorization
proof (p.26), Table2 (p.23), and Section4.4's factorization (75),
Proposition4.15 and Table5 (p.33). In this source n denotes polynomial
degree, so substitute n=5, not shift zero. Their modified hypergeometric
polynomial differs from the ordinary one by the nonzero denominator
Pochhammer factor; B,D>0 makes this harmless for roots. Positive variable
rescaling in Holland (69)/(74) likewise preserves root signs/simplicity.
No result from the asymptotic free-probability sections is used.

Proposition2.7(iii) preserves nonnegative real roots, and Proposition2.17
preserves logarithmic mesh for positive-rooted factors. Thus simplicity
requires a strictly separated factor; it cannot follow from parameter
positivity alone. Theorem3.1 identifies the parameter concatenation.
These are cited inputs; no new convolution proof is proposed.

For the classical orthogonality regime use [DLMF18.5.7](https://dlmf.nist.gov/18.5.E7),
[Table18.3.1](https://dlmf.nist.gov/18.3#T1) and
[18.2(vi)](https://dlmf.nist.gov/18.2#vi): alpha,beta>-1 give simple
zeros in (-1,1). Holland's Jacobi identity sets alpha=V-1 and
beta=U-V-d. At d=5 the applicability checks are V>0 and U>V+4;
for its two factors these read A>B+4 and C>D+4, with B,D>0.
These are sufficient conditions for that classical proof, not necessary
conditions for positive roots. Holland's stronger (57) additionally
pays for localization and derivative estimates; do not require it merely
to pose a finite positive-root test.

There is broader known coverage. Proposition4.15(ii), via (75) and
Table2, gives positive roots when denominator parameters are positive
and each paired numerator exceeds its denominator by d-2. At degree5
this is A>B+3 and C>D+3 (with the corresponding parameter permutations
also allowed). Its statement alone is not a simple-root certificate.
Table2 also records discrete numerator-minus-denominator cases, some
with repeated roots; Remark4.1/(60)–(61) expressly exhibits them.
Consequently failure of A>B+4, C>D+4 or (57) is not a disproof of
feasibility. No uninspected complete parameter classification is assumed.
For the bounded test below, direct five disjoint positive sign brackets
for (69) can certify simplicity without importing a broader classification.

### Rigorous actual-coefficient inputs

Reuse the ball semantics, Johansson integration/Cauchy method and exact
normalization assessment in
[step430](2026-11-04-actual-fredholm-fixed-pair-norm-test.md), especially
its primary-source section. Its saved polynomial approximation is not
silently treated as five exact a_j enclosures. L564 likewise supplies no
ready five-moment certificate for this problem. No certificate is replayed
or numerical input accepted in this literature-only turn.

A direct validated method is available independently of these saved data.
[Arb2.23.0 acb_poly documentation](https://arblib.org/acb_poly.html),
Gamma function and Zeta function sections, was read including
acb_poly_gamma_series, acb_poly_zeta_em_bound, _zeta_cpx_series and
acb_poly_zeta_series. These generate enclosed ordinary Taylor
coefficients, including Euler–Maclaurin truncation error. At s=1/2+z,
use the standard completion s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2,
with Hurwitz parameter1 and deflate=0, to length9. The expansion center
is away from the zeta and gamma poles; pi^(-s/2) uses real log(pi).
Extract the even coefficients and multiply the coefficient of z^(2j)
by j! to obtain gamma(j), j=0..4. This is the source/local Taylor
normalization, not raw moments or Stieltjes constants. Odd coefficients
are a parity check; their enclosure need not be the exact zero ball.
Finite series arithmetic determines coefficients through degree8 without
an omitted-function-tail claim at nonzero z. An implementation must
record its installed version, use actual enclosure arithmetic, retain
rounding errors and print outward endpoints. No wrapper availability or
precision success has been checked. If unavailable, the already assessed
Cauchy/ball integration method is the source-covered fallback; ordinary
mpmath values or decimal tables are not certificates.

### Bounded continuation and decisive evidence

One conventional calculation may produce five coefficient balls, test
(37)–(38), and, if admissible, attempt one finite solution of the fixed
(51)–(52) system. Use a rational parameter box and invertible rational
preconditioner, with an interval-certified self-map and derivative norm
strictly below1; the standard Banach fixed-point theorem supplies exact
existence/uniqueness in that box. Bounds must hold for the actual data
throughout their enclosing input intervals, including the dependent D.
A small floating residual or a successful unvalidated solver is no proof.
For an admissible solution, check the classical Jacobi/convolution
hypotheses above or enclose the polynomial at endpoints of five disjoint
positive intervals with opposite signs. The intermediate value theorem
and exact degree5 then give five distinct positive roots. This is only
model-root certification, not actual Jensen-root certification.

Bound the work: at most three increasing coefficient precisions and one
candidate parameter box with at most two refinements; no family, degree
or D changes. A strict interval failure of an obligatory first-stage
parameter condition stops that specified construction. An excluded
solution box stops only that box. Failure of a sufficient root regime
or inability to validate a solver is inconclusive, never a global
nonexistence claim. Preserve all balls, residuals, denominators, bounds,
failures and selected root evidence in a full later certificate. This
turn runs no mathematical script and proves no such specialization.

Searches: Holland four-coefficient Jacobi xi matching; Holland Jensen
Jacobi 2608.08682; Riemann xi Taylor coefficients rigorous computation
Arb gamma Jensen polynomial; Jensen degree five xi hyperbolicity.
Exact-system searches gave no independent central solution; that is not
novelty evidence. Narrow local searches checked the step379/385/473
assessments and prescribed-primitive stop; they did not locate a prior
fixed-D central certificate. The finite-free source supplies stronger
root regimes, not actual-Xi coefficient matching. Known low-degree
hyperbolicity, reused at the earlier assessment's scope, does not give
this particular representation. Planat and unrelated search hits were
not used. No full manuscript or numerical implementation audit is claimed.
Mathlib full matching coverage remains unchecked. No cross-notebook input,
new lemma, calculation, mathematical script, PROOF or DAG change.
