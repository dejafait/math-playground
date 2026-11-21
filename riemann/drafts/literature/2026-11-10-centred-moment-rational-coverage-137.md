# Rational interval route — source comparison completed in step138

TARGET: Assess source coverage for a dependency-free rational interval certification of the two natural-index walls and all 151 complete-support M32<81/4 leaves in Planat–Raymond v1 Theorem 3.3.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched rational interval arithmetic/exact Taylor integration/certified elementary functions and NIST logarithm/exponential/arctangent series; inspected the primary sources and package scope below; reused step135 for the unchanged moment theorem and searched the centred-moment assessments, histories and saved evaluator for duplicates/failures.
SOURCE_EVIDENCE: Daumas–Lester–Munoz arXiv:0708.3721v1 Sections II-A/C/D/E and III, Propositions 1/4/6/8/9/10/12 and Listing 1; NIST DLMF 3.1(ii–iii), 3.5.1–3/6–8, 4.2.19, 4.6.1–4, 4.24.3 and 4.45(i); official Python fractions documentation; certivl README and LeanCert integral-bound documentation inspected online 2026-11-10.
COMPARISON: Standard rational interval inclusion, convergent elementary series and quadrature with explicit remainder cover the changed arithmetic mechanism; none supplies a completed dependency-free replay of this 151-leaf certificate. This is reproduction of the source's stated bound, with implementation and finite applicability checks remaining.
GAP: Specialize and verify series truncation, outward endpoint operations, square-root enclosures, integral endpoint uncertainty and quadrature derivative bounds; execute every closed-wall/leaf inequality and establish acceptable cost. Neither a numerical maximum nor any of the 909 unexecuted gates is certified by this review.
REASON: The existing Arb dependency is unavailable. Inspected primary algorithms provide a materially different executable route without retrying installation; their specialization is prepared for a separate next-turn approval, not performed in this literature turn.
SCOPE: Same rectangle, natural support, 151-leaf recurrence and threshold as the step135 assessment and L960 step136 reduction; rational endpoint arithmetic and certified real quadrature only, with no global Newman or Xi-positivity claim.

## Gap, reuse and prior failures

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is the unchanged complete-support M32<81/4
premise of L960. Its plausible use is one positive-time collision-exclusion
input; other analytic, stable-model, global and zero-time premises remain
independent. The exact domain and cases are in the step135 assessment;
the analytic reduction is canonical in L960, “Partial independent audit
… (step136)”. Both were read locally and reused. The recorded source
theorem states precisely the desired bound, but the independent replay is
unfinished. Reproduction is justified by its unrefereed computer-assisted
status, not novelty.

Steps 136–137 stopped at missing flint, not a failed inequality. Their five
exact gates and 909 unexecuted gates remain unchanged. Scoped local searches
found no completed rational replacement. Preserve the existing script,
certificate and runtime evidence. The ATTEMPTS filename glob had no match;
relevant failure evidence was read in the centred-moment histories and
runtime continuation note. No installation or mathematical script ran here.

## Primary algorithm coverage and qualifications

[Daumas, Lester and Munoz, v1, 28 August 2007](https://arxiv.org/html/0708.3721),
Sections II–III (PDF pp.2–6), gives rational sqrt/pi/exp/log bounds and
inclusion/comparison results. Proposition 9 excludes zero divisors;
Proposition 12 requires nonnegative sqrt and positive log inputs.
Proposition 6 gives positive exp enclosures for every real argument:
alternating sums on [-1,0], integer-power reduction below -1, reciprocals
above 0. Listing 1 uses Machin's identity with 1/5 and 1/239. Do not
transcribe the displayed atan sum starting at i=1 or the log reciprocal
branch without reversed endpoint roles: the inspected HTML has apparent
formula inconsistencies. No PVS proof replay or source-code audit was done.
The propositions provide coverage, not verification of a new port.

Use independent [NIST arctangent series, 4.24.3](https://dlmf.nist.gov/4.24.E3),
whose first term is z, and the standard alternating-series remainder theorem
for real arguments in [0,1]. Machin's identity is the cited named identity,
not a new lemma. The implementation must document lower/upper parity.

[NIST logarithm series, 4.6.4](https://dlmf.nist.gov/4.6.E4), states
log z=2(w+w^3/3+w^5/5+...), w=(z-1)/(z+1), for Re z>=0, z!=0.
Only positive real z is needed. The future specialization may use exact
power-of-two range reduction and geometric-series comparison to bound the
omitted tail. It must give the finite rational remainder bound and its range
canonically before trusting output; neither a bound nor a parameter choice
was derived here. This avoids the suspect reciprocal-log display and slowly
converging alternating log2. The alternative series 4.6.1–3 and
[NIST range-reduction discussion](https://dlmf.nist.gov/4.45) were inspected.

For exp, [NIST 4.2.19](https://dlmf.nist.gov/4.2.E19) independently gives
the everywhere convergent factorial series. The named real alternating
remainder theorem and the paper's reduced-domain method cover finite
enclosures; the port must preserve positivity before reciprocation.
For sqrt, Proposition 1 gives Newton rational bounds for x>=0; exact
square-comparison bisection is another standard implementation option.
No floating function value may be promoted to a certified exact input.

[NIST 3.1(ii–iii)](https://dlmf.nist.gov/3.1) covers interval operations,
outward endpoint rounding, exclusion of zero divisors and rational arithmetic.
[Python's fractions reference](https://docs.python.org/3/library/fractions.html)
(online Python 3.15.2 documentation) supports rational numerator/denominator
construction. Use integer/string inputs; Fraction(float) preserves the
binary float, not the intended decimal. Fixed-denominator outward rounding
is allowed if its endpoint inequalities are proved. Denominator growth is
an unresolved cost risk, not an established mathematical obstruction.

## Definite integral: covered substitute for erfi

[NIST DLMF 3.5.6–8](https://dlmf.nist.gov/3.5#ii), citing Davis and
Rabinowitz (1984), pp.57–58, gives composite Simpson quadrature for
f in C^4[A,B], even subdivision count m and h=(B-A)/m, with
E=-(B-A)h^4 f^(4)(xi)/180 for some A<xi<B. Its absolute bound
requires a proved supremum enclosure for the fourth derivative.
Trapezoidal formulas 3.5.1–3 require C^2 and their own derivative bound;
they were inspected but are not needed for the proposed continuation.
No periodic or exponential convergence claim is imported.

The saved reduction already identifies the tail as the real integral of
(u-kappa) exp(a*u^2/4-B*u) over [log K,log U]. Apply the cited rule
there instead of subtracting erfi values. Future work must handle uncertain
endpoints (for example by an affine map to a fixed interval), verify
smoothness and supply rational derivative enclosures for every parameter
interval. No derivative formula, mesh, error constant, gate or performance
bound was derived here. Both auxiliary integral positivity gates still need
certified evidence.

## Existing implementations and feasibility comparison

The inspected [certivl README](https://github.com/vince-gonzalez/certivl#what-is-in-it)
limits its standard-library-only part to algebraic operations; its listed
transcendental functions use mpmath. It does not supply the required
dependency-free exp/log/integration implementation. Its code and error
proofs were not inspected or imported.
[LeanCert's integral documentation](https://docs.leancert.io/python/proving/integrals/)
distinguishes polynomial equality from nonpolynomial interval bounds and
describes fixed-partition checking. It is a scope lead, not an audited local
executable or a matching Mathlib theorem. Other hits (including pyintval
and elementary-function implementation papers) remain unread leads, not
essential inputs. No failed search establishes novelty.

The comparison supports bounded specialization: every required scalar
function and finite quadrature has inspected standard coverage, so an
unavailable special-function library is not essential. Precision, mesh size,
interval dependency and cost remain unknown. Continue only on rigorous
success for both walls and every closed leaf, with the maximum of certified
upper endpoints strictly below 81/4. Stop on a bad enclosure, unresolved gate
or infeasible cost. No midpoint preview, selected leaf or source PASS label
meets that test.

The exact next target and bounded contract are in
`2026-11-10-centred-moment-rational-replay-138.md`, for separate approval next
turn. Step138 changed no lemma, mathematical script, DAG edge or argument.
Mathlib full coverage remains unchecked; no cross-notebook input is used.
No justified central creative mechanism emerged from this arithmetic review.
