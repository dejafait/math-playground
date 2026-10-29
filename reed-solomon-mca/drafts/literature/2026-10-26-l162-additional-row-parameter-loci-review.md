# Additional-row loci on the audited L162 family — completed scope review

TARGET: Determine the exact rank-one parameter loci on L162's projective family for every additional original row whose support meets each of its four supports in at most one point.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused arbitrary-field coverage from the L162 audit and the saved complete-loci assessment; compared L109's map definition, L162's hypotheses and explicit family, L158's three different quadruples, L112's homogeneous/gcd method, ATTEMPTS/050 and /052, and histories 503/505. Focused external queries and inspected passages are recorded below; no source supplies the requested indexed loci.
SOURCE_EVIDENCE: Reuse Kostrikin–Manin, Linear Algebra and Geometry, 1997 paperback, Chapter 1 Theorem 3.12 pp. 20–21 and sections 6.2–6.9 pp. 44–46, and the saved projective coverage. Freshly inspect Milne, Fields and Galois Theory, Kea Books 2022, section 1.8 p. 6 and Proposition 2.17 p. 34, including their full Euclid/Bezout and field-extension proofs, in the current 199-page FT0.pdf. Inspect Winkler, Computer Algebra WS 2019/20, section 2.1 Theorem 2.1.2 printed p. 5 (statement and algorithm only).
COMPARISON: Arbitrary-field rank/minor tools and polynomial gcd/Bezout identities cover the algebraic method, including extension-field common roots. L112 already uses exact projective gcd certificates on different kernels; L158 classifies three other quadruples; neither supplies additional-row loci for L162. The remaining work is a finite original-label specialization, not a new general rank-locus theorem.
GAP: Reconstruct every eligible original row, certify its entire parameter locus on the fixed family and remove every rank-zero point. No eligible-row count, polynomial coefficient, locus or twelve-row conclusion is computed in this review.
REASON: Essential source coverage is adequate for one SPECIALIZE / REPRODUCTION calculation; importing the general tools cannot replace the actual original-map computation and completeness certificates.
LITERATURE_REASON: The saved additional-row target was REVIEW_REQUIRED and differs from the completed L162 audit; this turn checks its new polynomial-locus obligations while reusing unchanged linear/projective coverage.
SCOPE: Exactly L109's product-defined quotient maps, L162's S/J, original label order and vectors, E the algebraic closure of F_97; exclude labels 35,522,477,566 and require support intersection at most one with each of their four supports. Field-valued parameter sets only; no scheme, coding or descent conclusion.

## Relevance and decision test

The main gap is uniform twelve-row exclusion. This intermediate target
asks which further eligible original rows hold on one audited infinite
family. A complete answer could test whether that family contributes to
many-row compatibility; it says nothing about other four-row solutions.
Continue only with a complete, checkable exact-locus certificate for every
eligible row, including whole-family and empty cases, both endpoints,
extension-field roots and rank-zero removal. Stop an incomplete method
and record the specific failed completeness obligation. No anticipated
empty locus or finite-locus bound is assumed.

## Reused and freshly inspected primary coverage

A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*, Gordon
and Breach 1997 paperback, ISBN 90-5699-049-7, Chapter 1 Theorem 3.12
pp. 20–21 and sections 6.2–6.9 pp. 44–46:
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
The existing reading record in
`drafts/literature/2026-10-26-l162-critical-audit-review.md` supplies
arbitrary-field linear algebra and projective normalization. Reuse it;
no classification of pencils or generic intersection theorem is needed.

J. S. Milne, *Fields and Galois Theory*, Kea Books 2022,
[author's PDF](https://www.jmilne.org/math/Books/FT0.pdf), accessed
2026-10-26: section 1.8 printed p. 6 (PDF page 16) gives Euclid's
algorithm and Bezout identity over a field, with its remainder and
back-substitution argument. Proposition 2.17 printed p. 34 (PDF page 44)
and its complete proof establish invariance of polynomial gcd under any
field extension, using divisibility and that identity. These hypotheses
include F_97 and its algebraic closure. This supports certificates over
the base field without restricting common zeros to base-field points.
The current PDF has 199 pages; older local review page offsets differ.
Use theorem numbers and printed pages rather than copying those offsets.
The saved complete-loci review
`drafts/literature/2026-10-19-active-rank19-complete-loci-review.md`
already assessed the same algebraic tools and multiple-root cases.

F. Winkler, *Computer Algebra*, WS 2019/20, section 2.1 Theorem 2.1.2,
printed p. 5, [course PDF](https://www3.risc.jku.at/education/courses/ws2021/ca/2-GCD.pdf):
read its field hypothesis, nonzero-input algorithm and Bezout output.
Its proof is referred to the 1996 book and was not read here; Milne's
inspected proof is the imported justification. The all-zero polynomial
case must be handled separately, not passed through a nonzero-input
algorithm. No Magma installation or black-box verification is assumed.

## Local overlap and failures

L112's complete projective Plucker test already retains homogeneous
coefficients, polynomial divisibility and Bezout certificates plus a
direct infinity check. Its particular gcd and endpoint answers concern
other kernels and must not transfer. L158's hypotheses/conclusion and
source comparison concern three different quadruples (sizes 2,2,0),
not restrictions of L162's fixed family. L156/L157's saved assessments
supply general factor/image tools; they do not evaluate this family.
ATTEMPTS/050 stops three constructions; ATTEMPTS/052 and audited L162
stop unconditional four-row finiteness. Additional-row restriction is a
different test; neither failure bans it or establishes its answer.

## Approved calculation obligations, not derived results

Use L162's two displayed linear representatives and each original Q_j.
For the resulting four-by-two image matrix, retain all entries and all
six two-by-two minors in homogeneous parameter coordinates. Apply the
cited rank criterion and certify exact rank one by separately testing
that the entries are not all zero. L162 supplies the underlying plane
and parameter injectivity; do not assume an additional row is nonzero.
Use one explicitly declared affine chart, exact polynomial divisibility
and Bezout witnesses for its common-root computation, and a direct
homogeneous check of its missing endpoint. Include the other endpoint
in the chart test. Preserve identically zero systems and repeated roots;
an irreducible base-field factor still has algebraic-closure roots.
Root-set descriptions by exact polynomials are permissible if complete;
base-field samples and previews are insufficient. Certify rank-zero
removal on every component, including a whole-line case.

The enumeration must retain original labels and the four separate
support-intersection predicates, without symmetry reduction. Save full
certificates and a bounded summary; an independent reconstruction should
check coverage, map products, all coefficients, gcd witnesses and rank
zero. This approves the method's scope; it computes none of those data.
No general theorem requires reproof. Matching Mathlib coverage for this
indexed result is not checked; unknown availability is not absence.

## Search record and limits

Queries on 2026-10-26 included `site.stacks.math.columbia.edu rank matrix
minors determinantal ideals`, `site.csd.uwo.ca polynomial gcd common roots
algebraically closed field Euclidean algorithm`, `"matrix pencil" "rank
one" "projective line" minors finite field`, and `"Reed Solomon" "rank one"
"parameter" "minors" correlated agreement`. They supplied no matching
indexed theorem. Search results for a complex/real pencil paper, theses,
FLINT, MathWorld and a linear algebra text were leads only, not imported
theorems. Followed the primary Winkler passage and Milne theorem/proof;
reuse the earlier adequate coding and linear/projective comparisons.
Failed search establishes no novelty. This review neither refreshes the
unread ABF challenge definition nor needs it for the isolated map test.

Essential continuation inputs are L109's actual formula and audited L162.
No L159–L161 classification or census is a premise. Twelve-row exclusion
outside this family, second-pair extraction, coding weights/chart and
locator gates, arbitrary representation, challenge identification and
sharp radius remain open. Keep the finite coding field q=97^20 and all
inherited L104/L151 qualifications separate from this closure-valued test.
