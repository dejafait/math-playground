# Bounded quadratic values — scoped source approval

TARGET: Determine whether any S-unit value theta²+a theta+b with integers |a|,|b|≤8 has square rational norm, passes L118 and L122, but fails L119.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact octic coefficients with quadratic terminology, hyperelliptic quadratic elements/descent, and two-cover S-unit terminology; compared L124, C124b audit assessment, history/441,443,445,447,449,451 and ATTEMPTS/052–054. No inspected source answers this 289-value instance; this bounded search makes no novelty claim.
SOURCE_EVIDENCE: Reused ready Milne ANT v3.08 and Bruin–Stoll arXiv:0803.2052v2 coverage from the bounded-linear assessment; directly retrieved the primary even-degree map, localization/norm/scalar instructions and principal-ideal norm statement. Read L114/L115 hypotheses, L118/L119/L122 exact image conventions, L119 exact theta transports and L124 support/localization method.
COMPARISON: Known elementwise support/norm and localization methods apply without a linear-representative restriction. The missing work is exact evaluation of this fixed quadratic family against existing point-image sets; no class backend or new descent theorem is required.
GAP: Separately certify eligibility and norm for the 289 values and exact real/dyadic/five-adic membership for eligible norm-square rows, including value-dependent cancellation and strict precision bounds. No row was calculated in this review.
REASON: Essential coverage is now adequate for a separate REPRODUCTION calculation; import the methods and existing complete images, retaining all instance certification obligations below.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes the finite family and adds joint five-adic comparison beyond the assessed linear products and fixed relation.
SCOPE: Exactly TARGET, individual values only, in L115's unchanged entire degree-eight field and L114's one rational-scalar quotient; no products, larger bounds, global basis or rational-point completeness.

## Gap, relevance and bounded decision

The main Beal gap remains residual positive primitive integer
nonexistence. In this marked branch, complete supported arithmetic and
rational/integer point control are missing. The intermediate target is
one actual supported norm-square class passing the real and dyadic
images but failing the five-adic image. It could certify an additional
necessary restriction on global classes after those two filters.
A positive result would not establish a complete supported group,
rational-point control or an integer exclusion.

The later calculation must either supply an exact witness or exhaust
all 289 individual values and stop this family if there is none.
Incomplete localization or eligibility is an unfinished attempt, not
negative evidence. There is no authorization to enlarge the box or
search products in that step. This literature turn executes no search
of mathematical values and proves no new lemma.

## Primary source comparison

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. 78 (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008. Inspected Section 2 p.3 and Section 6 pp.12–13,
ad 7, ad 12, ad 16 and Remark 6.1. These give the even-degree norm
fiber, localization of algebra elements, common-scalar projection and
certified sign warning. Reuse the complete local proof-case coverage
of Sections 4–5, Lemma 4.4 and LocalImage in the ready assessments for
L118/L119/L122; no local image is being recomputed here. These methods
concern arbitrary nonzero algebra elements, so the quadratic form of
the trial representative changes instance evaluation, not the theorem.
The characteristic-zero, squarefree even-degree hypotheses hold by
L114/L115; the actual leading coefficient remains 3025=55². Bad
reduction at two and five is retained; no good-reduction shortcut is
invoked. A trial class is not asserted to be a point image.

J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Propositions 2.4/2.6 pp.26–28, norm definition and Proposition
2.19/Corollary 2.20 pp.31–32, and Proposition 4.1(c) pp.68–69.
Directly retrieved the integrality criterion and principal-ideal norm
statement, retaining its non-Galois case; reuse the complete supporting
proof reading recorded in the bounded-linear and small-global-witness
assessments. These cover polynomial integrality, exact multiplication
norms and ideal-valuation support tests. No reproof is needed.

The broad searches returned Bruin–Stoll and unrelated elliptic/Jacobian
software examples, not a theorem evaluating this family. Queries were
`"hyperelliptic" "two-cover descent" "quadratic" "S-units"`,
`"Bruin" "Stoll" "0803.2052"`,
`"275" "2860" "6930" "quadratic"`, and
`"hyperelliptic" "quadratic elements" "descent"`.
Only the primary sources above supply mathematical inputs. Search hits
for software and unrelated curves remain unread leads, not evidence
of an instance result. Full matching Mathlib coverage is not checked;
unknown coverage is not absence. The later calculation is REPRODUCTION
of known methods, not a certified originality claim.

## Separate calculation obligations

Use essential inputs L114, L115, L118, L119, L122, L124 and C124b.
Reuse L124's established integrality-away-from-S argument and the
imported integral-ring closure theorem; explicitly check their
application to these polynomial values before inferring support from
norm. Use all maximal primes above {2,3,5,11}. Do not confuse an S-unit
subfamily with the full supported square-class group, whose S-class
two-torsion is still unknown. Certify nonzero values using L115 before
forming a norm or a square class.

Enumerate the exact box without a gcd or squarefree restriction on
(a,b). Store exact reduced rational norms from multiplication in the
full field; track the nonmonic leading coefficient and every denominator.
Eligibility must be decided for every row; support stripping must be
justified by integrality outside S. Test the rational norm as an exact
positive square. The known norm fiber is 3025 Q*², not a changed twist.

For remaining rows evaluate all eight ordered real embeddings with
certified signs, refining root intervals as needed. Retain simultaneous
sign reversal and compare L118's actual four classes. Evaluate the same
element in both L122 quartic factors and all three L119 factors using
the specified exact theta, and quotient each product by ONE common
base scalar. Compare actual image sets, not their spans. L119's
norm-admissible labels are {1,beta,alpha,alpha*beta}, with point image
{1,alpha}; preserve this corrected convention.

The previous linear error bounds do not automatically cover quadratic
cancellation. Supply symbolic transport or new value-specific error
bounds for each evaluated polynomial. If approximants are used, prove
the error relative to the nonzero evaluated value lies strictly in the
square neighborhood: greater than 8 in L122's normalized quartic
valuation, greater than zero in each odd-residue L119 factor. Adapt
precision if needed; a zero approximant is not an exact zero. Reuse
existing complete square-class tables with their established sufficient
precision, rather than infer labels from sampled residues. Save full
row evidence and meaningful independent replay for any claimed witness
or exhaustion; report failures rather than silently dropping rows.

These are obligations for the separate research step, not newly derived
bounds or identities. No mathematical program or lemma is modified here.

## Duplication, failures and remaining limitations

L124's earlier linear-generated subgroup does not enumerate this box.
Some trial values may repeat already tested classes; classify such rows
using existing certificates rather than claim new witnesses. The known
mask-17 relation C124b must remain trivial in the scalar quotient; do
not retest it as a putative obstruction. ATTEMPTS/054 stops only that
fixed removal test. ATTEMPTS/053 records a real-rejected witness and
therefore does not provide the required additional five-adic pruning.
ATTEMPTS/052's backend route stays parked: this explicit-element test
uses no class-group backend. A historical stop is not a global ban.

Full units/S-class two-torsion, other supported classes, surviving-cover
points, degree-nine root recovery, compatible remaining factors, both
L095 integer systems and the minus-eleven branch remain unresolved.
Known rational infinity points survive; even complete failure of this
bounded family would not decide the global mechanism or Beal.
