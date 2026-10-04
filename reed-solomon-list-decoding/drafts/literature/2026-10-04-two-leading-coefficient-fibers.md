# Two fixed coefficients at one further agreement level: completed assessment

TARGET: Determine whether fixing the X^(k+1) and X^k coefficients of degree-(k+2) root products yields an unsafe list at A=k+2 on the order-1024 subgroup of F_65537 inside F_{65537^28}, for the four pinned rates and every m>=1.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched two prescribed leading coefficients, moment subset sums and multiplicative-subgroup joint fibers; read the primary construction, general counting framework and moment theorems listed below. Reused adequate A=k+1 coverage without reopening parked source failures.
SOURCE_EVIDENCE: Inspected Ben-Sasson-Kopparty-Radhakrishnan Section 1.3 and Proposition 3.4; Li-Wan arXiv:0708.2456v1 Section 5, p. 15; Gao arXiv:2105.12845v3 Section 2, Proposition 1 and Theorem 1, and Section 4's Theorems 4 and 5; Lai-Marino-Robinson-Wan arXiv:1910.05894v2 Theorems 1, 9 and 10 and Section 3 equation (4). Version and applicability details follow; a newer publisher lead has unread mathematical statements.
COMPARISON: Joint leading-coefficient classes, scalar root-subset correspondence and coefficient collisions are known. Gao's general formula permits arbitrary scalar evaluation sets, but its explicit two-coefficient estimates require a subfield domain. The moment paper distinguishes counts from positivity and has additional domain and quantitative hypotheses. No inspected theorem supplies the complete pinned interleaved threshold claim or an exact largest joint fiber on this proper subgroup.
GAP: Specialize the known collision method to roots in the fixed subgroup and coefficients in its prime subfield; verify strict degree, signs, distinct words and simultaneous agreement, then compare the certified list with the ambient 65537^28/2^128. Exact largest fibers and the sharp boundary remain unresolved.
REASON: Approve one bounded mathematical reproduction of the known two-coefficient construction and collision averaging, with only domain, interleaving and effective-threshold differences derived locally. No local joint-fiber inequality, attained count or threshold comparison is established in this literature turn.
SCOPE: The unchanged TARGET on H of order 1024 in F_65537 inside F_{65537^28}, k=512,256,128,64, epsilon*=2^-128, m>=1 and closed simultaneous column-Hamming balls at A=k+2. Covers the joint coefficient/common-center correspondence and elementary collision averaging using the coefficient field. Does not approve uniform fibers, exact subgroup formulas, application of subfield-only estimates to H, new character-sum estimates, other agreement levels, general upper bounds or ABF26 retrieval.
COVERED_TARGET: Verify the two-coefficient/common-center correspondence at A=k+2 on the fixed order-1024 subgroup, with strict degree less than k and simultaneous agreement for every m>=1.
COVERED_TARGET: Test the two-coefficient collision averaging certificate against 65537^28/2^128 at the four pinned rates on the fixed order-1024 subgroup.
LITERATURE_REASON: A=k+2 adds a second elementary symmetric coefficient constraint; the saved subgroup subset-sum theorem covers one sum, and the needed joint-fiber comparison is not yet assessed.

## Gap, downstream use and continuation test

The successful proper-subgroup application is recorded in
[C012a](../../lemmas/C012a-proper-subgroup-zero-sum-certificate.md).
It excludes the k+1-agreement radius for this instance, leaving the grid
radius with k+2 agreements as a concrete unresolved comparison with the
same threshold. The proposed intermediate target could exclude that next
radius with one attained list. It would still leave the worst-case upper
bound and the general sharp boundary unresolved.

The previous certificate has more than 2^322 candidates at A=k+1, against
an ambient threshold below 2^321. Those recorded values do not transfer to
A=k+2. The new issue is a second fixed coefficient, with the domain, field
and metric unchanged. The
[previous assessment](2026-10-03-root-product-one-more-agreement.md)
does not itself cover this changed agreement level. Its one-sum theorem
cannot simply be applied twice to assert a joint count.

A later mathematical step should import the scalar statements below,
verify their applicability and test the two-coefficient collision
certificate separately at each rate using exact arithmetic. Continue an
unsafe-radius claim only where a certified count strictly exceeds
65537^28/2^128. An inconclusive lower certificate should stop that
certificate's application for the rate and preserve the unresolved fiber
question; it does not establish safety or rule out another coefficient
pair. A valid upper bound for all joint fibers could exclude this
construction without settling other centers. No such comparison is made
here. Worst-case upper bounds, the complete boundary and the parked ABF26
comparison remain later gaps.

## Primary statements inspected and reused

**Known coefficient collisions.** Ben-Sasson, Kopparty and Radhakrishnan,
[Subspace Polynomials and List Decoding of Reed-Solomon Codes](https://www.math.utoronto.ca/swastik/rsld.pdf),
author-hosted eight-page manuscript without a recovered revision identifier.
Rechecked Section 1.3, printed p. 3, and Proposition 3.4, p. 6. The former
partitions monic degree-T root polynomials over F_N by coefficients above
degree K and obtains a common-pivot family of at least
binomial(N,T) N^(-(T-K-1)) elements. The latter turns a root-rich family
whose differences from one pivot have degree at most K into a scalar
received-word list. These are full-field statements. Restricting roots to
H, using the coefficient field separately from the ambient field, and
matching K to strict message degree are still local applicability checks.
The additive-subspace lower bound is not imported as a smooth-domain result.

**The two coefficients already occur in the scalar dictionary.** Li and
Wan, [On the subset sum problem over finite fields, arXiv:0708.2456v1](https://arxiv.org/pdf/0708.2456v1),
2007-08-18, Section 5, printed p. 15. Rechecked the passage following
Theorem 5.1: for an arbitrary D and a monic degree-(k+d) received
polynomial, maximal-root agreement is equivalent to distinct roots in D
with its first d elementary symmetric coefficients prescribed. The first
two displayed constraints are the subset sum and the pairwise-product sum.
Here d is degree excess, not interleaving width. This provides general
construction coverage; the manuscript's quantitative count treats one
sum and does not supply the requested joint-fiber size.

**A general count, with narrower explicit formulas.** Gao,
[Counting polynomials over finite fields with prescribed leading coefficients and linear factors, arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3),
2022-11-10. Read the introductory scalar correspondence, Section 2,
Proposition 1 and Theorem 1, equations (7)-(8), and Section 4's domain
restriction and Theorems 4 and 5. Proposition 1 gives Q^ell leading-
coefficient classes over F_Q. Theorem 1 expresses counts for arbitrary D
through distinct tuples and leading-coefficient matching; it does not
evaluate the maximum class size on H. The factors use X+x_j, so a later
application must check signs rather than copy a root convention. Section
4 assumes D is a subfield: Theorem 4 additionally requires its cardinality
to be an even power of the odd characteristic; Theorem 5 retains the
subfield hypothesis. Neither explicit formula is a theorem on H. Version
3 repairs a missing quadratic character in Section 4.1; older formulas
are not used. This source supports the known mechanism, not the entire
interleaved statement.

**Moment subset sums and their limitations.** Lai, Marino, Robinson and
Wan, [Moment subset sums over finite fields, arXiv:1910.05894v2](https://arxiv.org/html/1910.05894v2),
2019-10-19. Read the moment-count definition, Theorems 1 and 9, and the
large-subset passage of Section 3 through equation (4) and Theorem 10.
Their moment number is not interleaving width; M counts ordered distinct
tuples and N unordered subsets, with M=s! N. Theorem 1 decides positivity
for images of monomials or Dickson polynomials. Equation (4) is a
quantitative character-sum/sieve estimate, while Theorem 10 concludes
positivity subject to its small-character-sum and subset-size conditions.
Positivity alone cannot meet the ambient list threshold. Their domain is
a full polynomial image, which may include zero; deleting zero to obtain
H requires justification. No condition or error estimate is evaluated on
the fixed instance here, and none is imported as a uniform joint-fiber
claim. Collision averaging is independently testable and needs no such
estimate.

## Applicability and redundancy decision

The closest checked results cover the scalar mechanism, with Gao's
arbitrary-D identity providing the more general coefficient-count
framework. A citation alone does not check extension-field messages,
simultaneous columns for every width, or the effective cryptographic
threshold. A later proof is warranted only for those differences and the
prescribed-domain collision application. Import the cited facts; do not
reproduce their generating-function or distinct-coordinate sieves.

The count's coefficient field and the threshold's ambient field must
remain distinct. A largest collision class supplies one common center,
not a union of lists around different centers. A collision argument need
not identify an explicit maximizing coefficient pair; it also does not
give exact fibers or their uniformity. Keep unordered subsets distinct
from the tuple counts in the sources. The source degree convention,
nonzero root product, strict degree cancellation, evaluation injectivity
and remaining zero rows must all be checked in the mathematical step.

L012 and C012a settle A=k+1 only; this is not a duplicate application of
their one-coefficient counts. The earlier field-polynomial transfer,
unfiltered Riccati and simple-zero source failures address different
mechanisms and remain preserved. No essential unread source blocks the
approved construction/averaging test. This decision neither asserts an
unsafe k+2 radius nor claims novelty from an unsuccessful theorem search.

## Search record and unread leads

Queries used for the changed scope:

- `Reed Solomon list decoding two prescribed leading coefficients multiplicative subgroup subset sum moments`
- `subset sums two moments multiplicative subgroups finite fields elementary symmetric coefficients`
- `counting polynomials prescribed leading coefficients arbitrary subset Reed Solomon degree k+2`
- `"Subspace Polynomials and List Decoding" "coefficients"`
- `"moment subset" "multiplicative subgroup" two`
- `"two" "coefficients" "multiplicative subgroup" Reed Solomon`
- `"subset" "two" "moments" "subgroup" finite fields`
- `"Some new results on the second moment k-subset sum"`
- `"subset sums" "two prescribed" "subgroup"`

The primary Gao and moment texts supplied theorem statements; snippets
and secondary pages were not inputs. Gao's references identify the earlier
Zhou-Wang-Wang full-field distance-distribution formulas, whose original
statements remain unread. The moment paper points to Nguyen's 2019
dissertation and Li-Wan's *Counting polynomial subset sums*; those works
were not read in this review and are not counting inputs.

A new lead, Zhang-Zheng-Wang-Yuan,
[Some new results on the second moment k-subset sum problem over finite fields](https://doi.org/10.1016/j.ffa.2026.102877),
was found through the publisher's abstract and section previews. The
publisher lists a January 2027 issue; no earlier publication date is
asserted here. Direct reading failed and the previews omit essential
mathematical expressions, so its formulas and hypotheses remain unread.
It is not relied upon, and novelty relative to it is not assessed. It is
not essential to the ready collision test. The PMC rendering of the older
moment article returned a browser check; readable versioned arXiv text
resolved that access gap. PDF screenshot requests returned references
without visible images; readable PDF text and HTML supplied the passages
actually inspected.

The [prize website](https://proximityprize.org/) was checked on 2026-10-04:
the four rates, constant-width list challenge and epsilon* times ambient
field threshold remain displayed. Its statement is marked preliminary.
This does not recover ABF26 or remove the pinned model's qualifications;
the independent fixed-instance target remains unchanged.

## Completed review

Outcome: EXPLORATION; STEP_KIND: LITERATURE; classification:
NOVELTY_UNCHECKED. The missing joint-coefficient scope comparison is now
complete for the bounded SPECIALIZE test. A later mathematical application
should be classified REPRODUCTION. No local bound, candidate center,
joint-fiber count, numerical threshold test or new proof was produced.
Exploration turns used remain 0/3; literature spends no calculation budget.
No advance beyond the checked literature or complete candidate is claimed.

## Mathlib

Full two-coefficient/common-center statement for the pinned interleaved
instance: **not checked**. Formal coverage of the named coefficient-class,
collision and moment-count results: **not checked**. Supporting elementary
symmetric coefficient, finite-field/subfield and root results: **not
checked**. The direct primary links above give scalar supporting results,
without asserting a full matching library theorem. The pinned ArkLib
definitions are **present** as recorded in the model; they fix conventions
and do not establish this target.
