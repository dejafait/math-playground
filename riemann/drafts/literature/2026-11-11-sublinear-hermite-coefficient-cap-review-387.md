# Sublinear Hermite coefficient admissibility — source coverage completed

TARGET: Determine whether C997w's specific Hermite coefficients satisfy sum_(j=0)^n |A_(j,n)|<=exp(sqrt(n)) for all sufficiently large n, or prove an eventual violation from their prescribed upper-node jets.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step388 searched polynomial higher-derivative Bernstein bounds, complex-power differentiation, Hermite coefficient norms and prescribed-derivative coefficient bounds; inspected Jain p215 (1.1)-(1.2), DLMF4.7.10-11/4.2.28-30/4.6.7/1.2.6, and scoped local contrasts. Queries, inspected cases and unread leads are recorded below; no exact-family cap theorem was identified or novelty inferred.
SOURCE_EVIDENCE: V. K. Jain, An improved inequality for k-th derivative of a polynomial, Glasnik Matematicki 35(55) (2000), 215-219, p215 (1.1)-(1.2), https://web.math.pmf.unizg.hr/glasnik/35.2/35(2)-03.pdf ; NIST DLMF v1.2.8 (2026-09-15), 4.7.11 and 4.2.28-30; reused Calvi coverage in review381 and C997w(1),(5)/step387, C997s Hypotheses.
COMPARISON: Known finite-degree Bernstein bounds control every derivative order up to the degree on the complex unit circle, without zero-location or fixed-order hypotheses; DLMF gives exact complex-power derivatives. They cover the tools for the prescribed-jet test, but neither source compares this n-dependent Hermite family with exp(sqrt(n)). C997r concerns different coefficients and supplies no norm premise.
GAP: The later attempt must justify the branch specialization, select an available jet order below ell, relate its size to the original coefficient norm and establish an eventual comparison with the cap. No specialized inequality, rate, cap decision or capped E_n bound is proved here. Full matching Mathlib coverage remains unchecked.
REASON: Essential coverage is now sufficient for one bounded specialization/reproduction after separate approval of this changed assessment. Exact finite-degree inputs avoid any unproved uniform fixed-order asymptotic. The present literature turn imports source coverage only and derives no new result.
SCOPE: Only C997w's fixed polynomial p_n, original monomial coefficients A_(j,n), upper interpolation node b and multiplicity ell, compared with C997s's original coefficient cap. No universal all-polynomial obstruction, modified coefficients, lower bound for capped E_n, or actual-Xi assertion.

## Purpose and bounded continuation

The main gap remains L030-L032/C032a actual-Xi positivity, L966/L968
forcing and unpaid L984(H). The accepted uncapped result controls exact
band-null action but does not pay approximate leakage. Knowing whether
this particular construction satisfies the original cap determines
whether its residual estimate can be used directly with C997s's capped
objective, or whether a different cap-respecting approximation mechanism
is necessary. It cannot by itself settle any actual-Xi condition.

The proposed test uses the upper-node derivative matching already
prescribed in C997w(5) to examine the original coefficient norm. Review
known complex polynomial derivative/coefficient inequalities and their
growing-order hypotheses, as well as the precise complex-power derivative
formula and any stronger directly applicable result. Do not derive the
new inequality or its asymptotic rate in the review turn. The present
nomination supplies no such computation and does not approve itself.

Acceptance of the cap requires the actual eventual upper bound in
TARGET. Rejection requires an eventual lower bound exceeding that cap;
a positive lower exponential rate would suffice but is not asserted.
A large upper bound or a finite numerical violation decides neither.
If this prescribed-jet test cannot decide either direction in one
covered attempt, record the unresolved inequality and park that test.
A violation would stop use of these coefficients under this cap, not
the accepted uncapped theorem or the full band family.

Essential inputs: C997w's definitions and audited residual, C997s's
coefficient cap. C997r is a scope contrast only; do not treat its Taylor
norm lower bound as a mathematical input for p_n. The prior paid-leakage
generators' n=32 failures remain scoped and are not a primal lower bound.
No cross-notebook input is proposed.

Unresolved beyond this target: alternative capped constructions,
paid-leakage costs, C997a(8), selected/both-sign transfer, assay and
reconstruction, complements/regulators, L993, L984(H), L966/L968 forcing
and actual-Xi signs. This is a routine admissibility specialization,
not a creative central-gap attempt. A new cap-respecting construction
has not been justified by the residual audit alone; this concrete
untested cost is the immediate blocker to reusing its successful family.

## Completed literature-only comparison — step388

11 November 2026. The nomination above is preserved as prospective
work; its statement that coverage was pending describes the nomination,
not the completed source decision. No cap calculation was performed.

### Primary finite-degree inputs

V. K. Jain, *An improved inequality for k-th derivative of a polynomial*,
Glasnik Matematicki 35(55) (2000), 215–219,
[journal PDF](https://web.math.pmf.unizg.hr/glasnik/35.2/35(2)-03.pdf),
p215, (1.1)–(1.2), states, for a complex polynomial of degree d,
R>0 and integer 1<=k<=d,

    max_(|z|=R)|p^(k)(z)|
        <= d(d-1)...(d-k+1) R^(-k) max_(|z|=R)|p(z)|.

Read the complete relevant derivation: (1.1) is Bernstein's first
 derivative bound; (1.2) follows by successive application as the degree
 decreases. It is exact at every finite degree and order, with no hidden
 constant depending on k. No real-coefficient or zero-location condition
 is imposed. The sharper sampled-value Theorem1.1 on p216 was inspected
 in statement only and is unnecessary; its proof is not used. Initial
 PDF redirects failed; the journal-host PDF subsequently opened. No
 essential access blocker remains.

NIST *Digital Library of Mathematical Functions*, served version1.2.8,
release15 September2026, [4.7.10–11](https://dlmf.nist.gov/4.7.E11),
with complex exponent A and positive integer k, gives

    (d/dz)^k z^A = A(A-1)...(A-k+1) z^(A-k).

Read also [4.2.28–30](https://dlmf.nist.gov/4.2.E28): powers use
exp(A log z), analytic off the principal cut, and their modulus includes
the exponential of minus Im(A) times the chosen argument. A branch
must be fixed consistently. These identities are finite-order exact
formulas; A and k may be selected separately at each degree. They do
not assert any uniform asymptotic for that selection.

Rechecked [4.6.7](https://dlmf.nist.gov/4.6.E7) and
[1.2.6](https://dlmf.nist.gov/1.2.E6): the binomial expansion is valid
for any complex exponent and |z|<1, with falling-product coefficients.
These support local Taylor coefficients; the derivative formula above
already supplies the required input, so no tail theorem is needed.
Reuse Calvi's Hermite construction and repeated-node proof cases from
review381, rather than repeat its source search or reprove interpolation.

### Applicability and the remaining specialization

C997w supplies a degree-at-most-n complex polynomial, a unit-modulus
upper node b, its explicitly fixed holomorphic branch and derivative
matching through order ell-1. Bernstein is available for each positive
jet order not exceeding both the actual degree and ell-1; lower-degree
or constant cases must be handled explicitly if they arise. The future
attempt may use the standard elementary triangle comparison of the
circle supremum with the original monomial coefficient l1 norm. That
comparison must be written out in the mathematical attempt, along with
any replacement of the actual degree by its upper bound n.

The branch in C997w is defined on a rotated half-plane. Applying the
power formula requires tracking that branch near b, not substituting an
unjustified global principal-power identity. The derivative data are
prescribed by C997w(5), so this route does not require estimating the
whole Hermite coefficient expansion or excluding cancellations between
its two summands. The actual lower-bound comparison, the choice of
order, treatment of m's ceiling and finite exceptions, and any eventual
threshold remain mathematical work for a later approved attempt.

This is SPECIALIZE rather than IMPORT: the known formulas do not decide
the stated cap, and their growing-order specialization has not been
evaluated here. Import the general theorems by citation; reprove only
the necessary elementary norm comparison and family-specific estimates.
No fixed-order asymptotic or complex Stirling remainder is assumed.
If an attempt instead requires an unassessed asymptotic theorem, obtain
coverage before using it. Full matching Mathlib availability is unchecked;
no absence claim or formalization dependency is made.

### Search, overlap and limits

External queries actually issued: `polynomial higher derivative Bernstein
inequality unit circle n! (n-k)! Erdelyi`; `site.dlmg.nist.gov complex
powers derivatives` (mistyped domain, not useful evidence);
`site.dlmf.nist.gov differentiation powers falling factorial binomial
theorem`; `"Hermite interpolation" "coefficient norm" complex power`;
`"prescribed derivatives" "coefficient" "Bernstein" polynomial norm`.
The useful derivative search led to the primary Jain paper; direct DLMF
reads supplied the exact formulas. General Hermite searches returned
Hermite-Pade and numerical interpolation leads, not an inspected theorem
for this family. Those leads remain unread and are not evidence of a
matching result or of novelty. Stronger Bernstein variants involving
root constraints cannot be invoked without additional root hypotheses;
none are supplied for p_n. The unconditional bound is sufficient tool
coverage for the proposed one-attempt test.

Read C997w's definitions and construction through (7), C997s's cap and
objective, and C997r's hypotheses/conclusions. Reused review381's Calvi
proof notes and review367's DLMF scope. C997r's centered Taylor norm
obstruction concerns a different polynomial; ATTEMPTS entry372 records
only finite paid-leakage generator failures. Neither decides this target.
The balanced two-center review382 concerns an uncapped residual and
explicitly excludes coefficient-cap conclusions. No duplicate result
for this specific admissibility test was found in these scoped records.
No inference of originality follows from these searches.

The same exact TARGET is ready for separate next-turn approval, followed
by one RESEARCH/REPRODUCTION attempt if approved. Acceptance, rejection
and parking tests remain those in the nomination. No new lemma,
mathematical script, DAG edge or PROOF change was made. All main-goal
and transfer limitations listed above remain unresolved.
