# Fixed known-point local-seven certificate — critical-audit coverage

TARGET: Critically audit L081's fixed local-seven nondivisibility certificate and full-local-group applicability proof for P=(0,0).
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target discovery, local duplicate/failure comparison and inspected primary evidence in 2026-10-18-known-point-local-seven-test.md; read complete L081 and history/307 to compare the actual new certificate and audit obligations. No new external search or certificate replay was performed.
SOURCE_EVIDENCE: Silverman, The Arithmetic of Elliptic Curves, second edition (2009), III Algorithm 2.3 pp.53–54, VII Propositions 2.1–2.2 pp.188–191, IV Lemma 6.3(b) and Theorem 6.4 pp.131–132, with author errata dated 2022-10-13; prior inspected statements and relevant proof cases cover the unchanged hypotheses and exact audit scope below.
COMPARISON: Known reduction, parameter, strict-radius logarithm and group-law results cover the mathematical mechanism; the separate audit must verify the actual finite certificate and its applicability, including the translated short model and full-local-group passage. No inspected source supplies that instance audit, and no novelty is claimed.
GAP: Coverage is ready; full fresh replay, distinct exact evidence and critical review remain unperformed. All L026 premises, D=D_div, strict rational directions and arbitrary-curve rank comparison remain independent.
REASON: Comparing the newly written L081 with the already inspected theorem hypotheses supplies the separate source gate for this changed audit target; no new mathematical mechanism or essential unread source is introduced.
SCOPE: Only L081 on y^2+y=x^3+x^2-2x, P=(0,0), p=7, W=[13]P and depth one; complete saved evidence, group-law exceptions, both formal filtrations and full-group division. No changed point, prime, depth, broader descent application or upstream re-audit.
LITERATURE_REASON: The new critical-audit target was REVIEW_REQUIRED after step 307; this turn compares its actual obligations with ready primary coverage rather than repeating source discovery.

## Relevance and reuse

The main gap remains rank E(Q)=m(E) for arbitrary m(E)>=2. The
intermediate target is a reliable fixed local nondivisibility certificate,
not a rank bound. Its plausible downstream use is a local Kummer witness
in a separately assessed application of L062, provided every L026 premise
and the finite-quotient exponent are independently established. Removing
the divisible Sha defect and comparing arbitrary complex orders remain
unresolved even after a successful audit.

The prior assessment's discovery queries and overlap comparison are reused
unchanged. Its Sage exact-model example at three, seven-adic ratios for a
different point and Wuthrich's approximation-lattice plots do not certify
this fixed value. L034's published basis is unnecessary here. The earlier
scalar-transfer/interface failures in ATTEMPTS/033 and /034 and repeated
approval failure in /042 are retained: this audit checks newly produced
finite evidence and must not restart those mechanisms. History/307
explicitly distinguishes successful production/replay from critical audit.
No historical stop is interpreted as a global prohibition.

## Primary hypotheses matched to audit obligations

Reuse Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, second
edition, GTM 106, Springer (2009), DOI 10.1007/978-0-387-09494-6.
The prior assessment records complete inspected statements and relevant
proof cases, their page locators and the source-access qualifications.
This turn reads that evidence rather than claiming a fresh source read.

- [III Algorithm 2.3, pp.53–54](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=71): all identity, inverse, chord and tangent branches are covered. Audit every actual denominator, scalar label and coordinate, and the translation X=x+1/3, Y=y+1/2 used by the independent verifier. That translation and its inverse must be checked against the original equation and line/negation conventions; on-curve output alone is insufficient. No general group-law reproof is needed.
- [VII Proposition 2.1, pp.188–190](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204): complete discretely valued field, perfect residue field and minimal integral equation; the good-reduction case uses the entire local group. L030 supplies the exact minimal equation and L033 the good reduction and complete group order 13. Review the use of the exact reduction sequence and the treatment of a hypothetical division point outside its kernel. Do not silently substitute a formal-subgroup assertion for a full-group assertion.
- [VII Proposition 2.2, p.191](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=207): the inverse parameter -x/y identifies the reduction kernel with the formal group on the maximal ideal. Audit the projective reduction and the nonzero ordinate at W; the parameter is undefined at the original P and must not be evaluated there. Check the filtration conventions in L081 against this identification.
- [IV Lemma 6.3(b) and Theorem 6.4, pp.131–132](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150): the formal group is over the valuation ring of a characteristic-zero complete discretely valued field and the integer radius satisfies r>v(p)/(p-1). The prior assessment covers Q_7 with v_7(7)=1 and both r=1,2. Audit compatibility of the same logarithm on both filtrations, its valuation estimate and the use of injectivity/surjectivity in the asserted multiplication-subgroup equality. No truncated numerical logarithm is needed.

The [author errata, 13 October 2022](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf),
entries for pp.130–133 and 185–191, were inspected in the prior assessment.
They qualify unrestricted convergence in IV.6.3(a) and restore reduction
notation. The approved audit uses the strict radius of IV.6.3(b)/6.4;
it must not import the erroneous unrestricted wording. The prior source
record does not claim exhaustive errata coverage across all printings.

These are imported known results. The audit needs only the fixed-instance
applicability review and independent finite checks, not reproof of the
general theorems. Reading the existing argument for coverage approval is
not a passing mathematical audit of it.

## Approved bounded audit and decision test

Essential inputs are complete L081, L030's exact minimal equation and
L033's full reduction order, plus the complete saved evidence under
`scripts/known-point-seven-307/`. Preserve the five binary rows, all
thirteen sequential additions, full rational coordinates and valuations,
projective reduction, original verifier failure and repaired verifier.
L034 independence and L062 are not mathematical premises of this audit.

The later research turn may fully replay the existing finite instance,
inspect all relevant evidence, and supply distinct exact evidence for the
valuation or line identities. Require all five scalar-chain branches,
every sequential addition and every exceptional-case exclusion to agree.
Check reduced fractions, all numerator/denominator valuations and the
projective equation/reduction. Review both filtration arguments, the
hypothetical full-group division point, and multiplication by 13 on the
quotient killed by seven. Review the preserved verifier sign repair and
its actual detection; it is not a malformed-certificate rejection test.
Distinct exact checking supplements full replay, rather than replacing it.

Continue only if the complete evidence and imported hypotheses support
exactly the stated local nondivisibility conclusion. A broken identity,
missing branch or invalid radius/full-group passage requires a named
failure with original evidence preserved; it does not establish the
opposite branch, rank zero or a BSD counterexample. Stop at this fixed
point and depth. A repair or application outside this scope needs another
assessment. A successful audit must retain all global limitations.

## Mathlib and classification

Full matching result and supporting formal-logarithm/radius, Weierstrass
and reduction coverage remain not checked; no absence is inferred.
The approved research classification is REPRODUCTION under SPECIALIZE:
a finite audit of known-method specialization, with no claim of progress
beyond the inspected theory. This literature turn establishes readiness,
not a new lemma, new computation or a passing audit.
