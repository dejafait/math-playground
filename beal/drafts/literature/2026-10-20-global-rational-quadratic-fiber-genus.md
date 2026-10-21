# Global rational/conjugate-pair fiber locus — source comparison

TARGET: Compute the normalization genera of the non-diagonal fiber locus with one rational root and a conjugate pair over Q(sqrt(−3)) for phi(t)=(3t²+t+1)^5(1−5t).
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-polynomial, rational-root/quadratic-factor and fiber-product/genus searches found no inspected classification matching this fixed-field incidence target; compared L093/L095/L104 and ATTEMPTS/045–046; inspected primary monodromy, genus and algorithm sources below.
SOURCE_EVIDENCE: Putz (2024), Section 5.2 p.165 and equation (5.2) p.168; Jones arXiv:1209.5169v1 Theorem 1.1 p.1 and covering comment 5 p.2; Milne LEC v2.21 Theorems 3.1/21.3 pp.27/130–131; Stacks 58.6.2, 53.8.2, 53.12.2/4 and 53.18.2; Magma V2.29 Global Geometry, Genus/ArithmeticGenus.
COMPARISON: Standard finite-cover monodromy and Riemann–Hurwitz cover the method; fixed quadratic-field marking, actual ramification, components and induced cycle counts remain a specialization, not a theorem already supplying the requested genera.
GAP: Verify the fixed-field model and its comparison with the distinct-root triple cover, determine actual geometric monodromy and every component, and certify all ramification sums; no genus, rational-point classification or power lifting is established here.
REASON: Essential coverage is available for a bounded exact proof/calculation without a class-group or normalization backend; approve only this unchanged target's specialization, subject to separate next-turn approval required by the invocation.
SCOPE: Exactly TARGET, including verification of the marked fixed-field model and all geometric components, by ramification/monodromy and finite permutation arithmetic; no rational-point search, integer elimination, class-group computation or other quadratic field.
LITERATURE_REASON: The startup REVIEW_REQUIRED target lacked inspected global-curve, component and normalization-genus coverage; this turn supplies those essential primary hypotheses.

## Gap, use and existing stops

The main gap is integer elimination in both L095 systems and compatibility
of all global factors. The intermediate target is the normalization
geometry of the rational-plus-minus-three incidence locus. Its downstream
use is choosing a rational-point method before new global arithmetic.
Genus alone excludes neither rational points nor primitive integers.

Inputs remain L093, audited L095, audited L103/L104 and audited L105.
L095's two power tests, positivity and primitivity remain additional
arithmetic restrictions. L104 supplies necessary field candidates only.
ATTEMPTS/046 and L105 stop standalone exclusion at seven, not global
compatibility. ATTEMPTS/045's independent class-backend park is preserved.
The relevant quadratic assessments contain no global genus computation.
No sibling notebook was read.

## Primary coverage actually inspected

1. P. H. C. Putz, *Enumeration of local and global étale algebras applied
   to generalized Fermat equations*, VU thesis (2024), version of record,
   [DOI 10.5463/thesis.832](https://doi.org/10.5463/thesis.832),
   [primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf),
   **Section 5.2 p.165 and equation (5.2) p.168** (PDF indices 171,174).
   These identify this precise Belyi map and its discriminant's branch
   support. Reused the previously inspected Proposition 5.26 comparison
   in the quadratic assessment: its special coefficients and stronger
   local conditions do not cover coefficient one. No fixed-field incidence
   classification is imported. The derivative needed for a future
   ramification check is already in L095; none was newly calculated here.

2. Gareth A. Jones, *Primitive permutation groups containing a cycle*,
   [arXiv:1209.5169v1](https://arxiv.org/pdf/1209.5169v1), **Theorem 1.1,
   p.1**: Jordan's theorem requires a primitive finite permutation group
   containing a prime-length cycle with at least three fixed points and
   concludes containment of the alternating group. Comment 5, p.2,
   describes covering monodromy and local cycle types. The cited books,
   Dixon–Mortimer Theorem 3.3E and Wielandt Theorem 13.9, were not separately
   read. The retrieved PDF has a v1 label dated 24 September 2012 and an
   internal date 27 November 2024; record that discrepancy. Only Theorem
   1.1 is needed, not classification-dependent Theorem 1.2. Its hypotheses
   must be checked on the actual map next turn. No monodromy group for
   phi is asserted in this review.

3. J. S. Milne, *Lectures on Étale Cohomology*, **v2.21, 22 March 2013**,
   [author's PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf),
   **Theorem 3.1 p.27 and Theorem 21.3 pp.130–131**. They identify finite
   étale covers with finite fundamental-group sets and, for nonsingular
   complex varieties, finite analytic covers. Read Theorem 21.3's
   statement and three-step proof sketch, including fiber-product full
   faithfulness and extension across a smooth compactification. Import
   these results by citation. Apply after removing branch values, not
   directly to an unreduced singular affine intersection.

4. **Stacks Project, Theorem 58.6.2**, statement and proof,
   [tag 0BND](https://stacks.math.columbia.edu/tag/0BND): for a connected
   scheme and a geometric point, the fiber functor identifies finite
   étale covers with finite fundamental-group sets. This supplies the
   component/orbit and fiber-product framework. Transitivity on several
   distinct roots must be proved, not inferred from a transitive root
   action alone.

5. **Stacks Project, Lemmas 53.12.2 and 53.12.4**,
   [tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B), statements and
   differential calculation, including the characteristic-zero case:
   smooth proper curves, a generically étale map and full constant fields
   equal to the base give Riemann–Hurwitz; tame different multiplicities
   equal ramification indices minus one. Work componentwise over an
   algebraically closed characteristic-zero field and retain infinity.
   The relation between cycle lengths and local ramification still needs
   an applicability explanation; a guessed passport is insufficient.

6. **Stacks Project, Lemma 53.8.2**,
   [tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6), statement and
   cohomology-base-change proof, preserves genus under field extension
   for proper dimension-one schemes with H0 equal to the base.
   **Lemma 53.18.2**, [tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0),
   including its component/function-field proof, preserves geometric
   genus on reduction and normalization. Check constant fields and
   distinguish individual genera from their sum on a disconnected curve.

7. **Magma Handbook V2.29, 3 August 2026, Global Geometry**,
   [official documentation](https://magma.maths.usyd.edu.au/magma/handbook/text/1468),
   entries Genus, GeometricGenus, GenusViaArithmeticGenus, ArithmeticGenus
   and the cusp example: normalization genus requires an integral curve;
   arithmetic genus of the unnormalized projective scheme is different.
   This is an alternative method, not an executed certificate. A narrow
   PATH check found no magma, sage or Singular; python3 is present.
   Shell retrieval of the thesis failed DNS, but the web tool supplied
   its primary text, so essential source access is not blocked. No API
   key, paid service, installation or calculator submission was used.

## Proposed model specification and bounded authorization

The research attempt must first specify the marking. With a fixed symbol
w satisfying w²=−3, propose rational coordinates (r,u,v), s=phi(r), and
coefficient equations

    F0(r,u,v)+w F1(r,u,v) = phi(u+v w)−phi(r),  w²=−3,
    F0=F1=0,
    v*((r−u)²+3v²)*phi(r)*(phi(r)−1) != 0.

These are unexpanded instructions for constructing and verifying a model,
not a proved equivalence or a computed curve. Verify both directions
between its rational points and a rational root with a disjoint conjugate
pair generating the specified field. Keep the full degree-eight remainder
of the fiber without imposing an unproved global field type. Take the
reduced closure of the open locus before normalization; unsaturated
homogenization can retain unwanted diagonal components.

The sign of v records a choice of quadratic embedding. Explain the
involution v -> −v and its relationship to the unmarked quadratic-factor
locus. A quotient parametrizing arbitrary quadratic factors does not alone
impose discriminant square class −3. Do not substitute that quotient's
genus for the fixed-field marked cover's genus without justification.

The preferred method is to verify this model's base change against the
three-distinct-root fiber product, determine geometric components from
actual monodromy and apply the cited genus formula to induced permutations.
Jordan may be used only after checking its hypotheses. Elementary model,
primitivity and transitivity arguments require full applicability proofs
in the research step; no reproof of Jordan or Riemann existence is needed.
The finite arithmetic budget is a 1000-label cap for the distinct-root
action; verify exhaustion and sizes before trusting a certificate. This
proposed method needs no numerical analytic continuation or class backend.

Continue if the marked-model equivalence and a complete component/genus
certificate follow from exact ramification and finite arithmetic within
that bound. If monodromy, model equivalence or component descent cannot
be justified in the bounded attempt, save that exact obstruction and stop.
Do not report a sampled genus or switch silently to an unavailable package.
High genus alone is neither an abandonment theorem nor an emptiness proof.
The minus-eleven branch, larger fields and retained integer tests remain
independently open.

Queries included the exact polynomial and its factors with quadratic,
genus, Galois and rational root; Putz with generalized Fermat; fiber
product genus polynomial monodromy Fried; and Jordan primitive group
prime cycle. Broader two-map fiber-product and genus-growth results were
leads only; abstracts and snippets were not used as matching theorems.
No inspected source supplied this target's genera or rational points.
Failed search establishes no novelty. Reuse this coverage unless a
specific hypothesis changes or source gap appears. Mathlib is not checked.

Completed step: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. No lemma,
mathematical script, genus, monodromy group or Beal candidate was produced.
This new SPECIALIZE assessment is ready for separate next-turn approval
required by the invocation; its mathematical specialization has not run.
