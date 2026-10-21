# Full-fiber image equality — critical audit coverage

TARGET: Critically audit L040's full-fiber image equality, checking the degree-eleven point, all scalar valuation cases and exceptional charts.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L040's complete proof with the primitive-five comparison and fixed-one/fixed-two assessments, the relevant L034-L036 and L038 interfaces, history/101-102 and ATTEMPTS/012; located primary coprime lifting, strict-ball root uniqueness and finite-extension valuation statements. This is an audit-specific source comparison, not a new exact-image theorem search or a novelty claim.
SOURCE_EVIDENCE: Re-inspected Milne ANT v3.08 Theorem 7.33, Lemmas 7.34-7.35, existence proof and Remark 7.36, printed pp.121-123, Proposition 7.31 and proof p.120, Theorem 7.38 and proof p.123, Corollary 7.42 and Remark 7.43 p.124; Clark ANT II Theorem 1.79 p.58. Reused inspected FNS June 10, 2019 Section 7.2 equation (7.4), Schaefer-Stoll Section 5 and local common-witness coverage as qualified below.
COMPARISON: Standard results cover repeated coprime blocks, root uniqueness over either complete field and the normalized value group; the necessary map identity, degree-generation argument and same-point image inference are explicit local audit obligations, not conclusions imported from these sources.
GAP: No essential theorem coverage is missing for this exact audit; the all-scalar specialization, certificate identities, affine generation and exceptional-chart applicability still require independent mathematical verification.
REASON: Separate approval of the newly proposed critical audit is now justified by matching its actual hypotheses to reusable primary coverage; no reproof of general local-field theory or new mechanism is authorized.
SCOPE: Exactly the saved L040 critical audit, using L034-L036, L038-L040 and the complete relevant degree-obstruction certificate; retain every scalar case, whole-fiber isomorphism and descent-class collision. No new local scalar search, image list, global intersection or signature exclusion.
LITERATURE_REASON: The supervisor requires separate coverage approval of the newly written L040 audit target; the new obligations concern universal degree generation, repeated coprime blocks and uniqueness over Q5 and U_11, beyond the earlier fixed-scalar audits.

## Relevance and bounded review

Main gap: global emptiness of the surviving Beal signatures, including all
five surviving twists for ordered (3,4,11). Intermediate target: independent
verification of L040's claimed equality I_pow=I_fiber. Its downstream use
is a reliable stopping decision for the additional primitive-scalar filter
at five; even a correct equality supplies neither a class list nor global
emptiness. The continuation test is a complete justification of the
all-scalar equality, or a precise failed inference/identity to correct.
An incomplete audit must withhold the affected conclusion rather than
report integer exclusion. This review only approves coverage, not equality.

The prior primitive-five comparison assessment approved deciding the
image comparison; it did not independently audit its completed new proof.
History/102 records that distinction. History/101 audits L039 alone.
ATTEMPTS/012 records the claimed equality stop pending audit; preserve it
and ATTEMPTS/008-011. Repeating nonemptiness, scalar-domain construction,
constant-norm compression or generic encoding cannot perform this audit.
No cross-notebook input is used. No duplicate independent L040 audit was
found in these targeted records. Historical stops are scope-specific.

## Primary coverage and what was actually read

J. S. Milne, [Algebraic Number Theory v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 7.33 and Remark 7.36, printed pp.121-123: over a complete DVR,
a monic polynomial with a product of relatively prime monic residue
factors has the corresponding monic lifted factors. Re-read the full
relevant proof: Lemma 7.34 gives strict coprimality, Lemma 7.35 gives
uniqueness, and the successive corrections preserve the prescribed
factor degrees. Squarefreeness inside each block is not a hypothesis.
Proposition 7.31, p.120, and its proof give unique lifting of a simple
residue root. Theorem 7.38, p.123, and its proof cover the unique extended
absolute value and completeness of a finite separable extension.
Corollary 7.42 and Remark 7.43, p.124, give degree ef and value group
(1/e)Z for the extension of the base normalized valuation. These inputs
apply to the fields in the audit; the explicit block identities, derivative
conditions and use of L038's unramified factor remain to be verified.

Pete L. Clark, [Algebraic Number Theory II](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page author-hosted version retrieved 2026-10-08, revision date
unidentified, Theorem 1.79, printed p.58: for a complete valued field,
integral polynomial and integral approximate root r, the strict inequality
|G(r)|<|G'(r)|^2 gives a unique root in |w-r|<|G'(r)|, with the stated
exact error. Re-read the entire numbered statement; this version does
not print a proof of 1.79. It is imported as a named theorem, with Milne's
simple-root proof also inspected. The audit must check polynomial
integrality and the strict inequality in each field and compare roots
in the same uniqueness ball. No requirement that the whole polynomial
be monic or separable is added. No new Hensel proof is needed.

Reuse the source inspection in
[the fixed-one assessment](2026-10-08-full-fiber-at-one-local-algebra.md)
and [the primitive-five comparison](2026-10-08-primitive-five-full-fiber-image-comparison.md):
Freitas-Naskrecki-Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. 156 (2020), 77-113,
[final manuscript June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25-27, equation (7.4), supplies the modular polynomial.
A fresh web open of this URL returned an internal error this turn; no
new FNS retrieval is claimed, and the unchanged recorded primary
inspection remains adequate. L034's canonical exact map and pole/chart
arguments are audit inputs. FNS's Q2 square-class results and
GRH-dependent Selmer computations do not decide this Q5 equality.

Reuse [the fixed-two audit assessment](2026-10-08-fixed-two-nonemptiness-critical-audit.md)
for Schaefer-Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS 356 (2004), 1209-1231, June 13, 2001 manuscript Section 5 pp.8-10
and Section 9: the connecting map and good-divisor interpretation are
already inputs through L033-L035, including exceptional descent values.
Foundation 17 and L036 supply the independently proved common-scalar
domain and its unit-root citations; L038 supplies the entire A and L039
supplies nonemptiness. No reproof or generalization of descent is needed.
Full matching or supporting Mathlib coverage remains not checked.

## Exact next-turn obligations

The continuation must independently test the affine-fiber generation
claim after projecting a whole-fiber isomorphism to U_11, then the
claimed degree of x using the curve equation and tower law. It must
check that L034's polynomial identity is necessary at every finite point,
including the removable chart, without treating its quotient as a
universal exceptional-fiber presentation. Check both residue products
and coprimality from complete exact coefficients; internal multiplicities
must remain, and both lifted block degrees must be accounted for.

For every nonintegral scalar, audit the reciprocal polynomial, its
coefficient integrality and derivative, the uniqueness comparison over
both fields, and the nonzero reciprocal-root condition. Then audit all
remaining valuation cases, exact unit evaluations, noncancellation and
value-group normalization. No finite precision or sampled scalars can
replace the universal reasoning. Read complete selected load-bearing
values in scripts/full-fiber-image-comparison/degree-obstruction-certificate.json;
its 15 reported checks are evidence to inspect, not proof by preview.

Finally compare L035's exact image quantifiers with L036's domain,
retaining the same scalar, point, every isomorphism and class collisions.
Check the exceptional descent point and removable chart and the cited
L039 nonemptiness. Source coverage is ready for this bounded REPRODUCTION
audit; correctness is pending. No global basis, GRH, rank, Sha, precision
cutoff, global integer witness or complete class list is assumed. All
five global twist problems and infinitely many signatures remain open
in this notebook.
