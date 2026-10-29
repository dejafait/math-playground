# Pair Jacobian real-place filtering — source approval

TARGET: Test whether the real-place Kummer condition strictly improves L139's rank upper bound, using the exact real local image and a finite certified set of supported global sign witnesses.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the pair-rank and supported-dimension assessments; checked L135's signature proof, L136's complete-box interface, L137's seven indices, L138's actual maps, L139 and ATTEMPTS/050,059–061. Searched Stoll real-image/signature terminology and exact coefficient 76835 with Kummer/Jacobian; no inspected exact-instance sign certificate was identified. Daniels–Lozano-Robledo–Wallace supplies a stronger general signature comparison, not this product-algebra calculation.
SOURCE_EVIDENCE: Stoll, Acta Arith. 98 (2001), DOI 10.4064/aa98-3-4, Section 4 pp.249–250, Lemma 4.8 and its entire proof/sign paragraph p.254, Section 6 Lemma 6.1 and its complete proof p.268; Daniels–Lozano-Robledo–Wallace, author-hosted 31-page RankBounds.pdf, Section 2.2 p.8 and Proposition 2.25 with hypotheses and relevant proof p.12, accessed 2026-10-26. Exact links and qualifications below.
COMPARISON: Real-image generation and signature filtering are known. The inspected stronger prime-degree field bound does not directly apply to L138's Q times quartic algebra. L139 is unfiltered; L136's T-supported elements can supply a fixed subset of global sign witnesses after the required even-valuation filter, but neither their relevant signs nor codimension has been certified.
GAP: Certify the actual root/embedding order, the full real local image, support and signs of the fixed witness subset, and its quotient-image rank; then justify any induced bound. No full global sign-image, Selmer, rank determination or point classification is covered.
REASON: The missing primary real-image coverage and bounded execution protocol are now supplied. Import the general theorem and perform only this fixed-instance specialization in a later research turn; no mathematics is executed in this review.
LITERATURE_REASON: The invocation's REVIEW_REQUIRED target lacked exact real-image generation, dimension and embedding coverage; this supplies those missing cases while reusing ready descent and S-Kummer assessments.
SCOPE: Exactly TARGET for the unchanged L138 odd model over Q and L139 supported norm kernel, using L135–L138 arithmetic. At most the 182 existing L136 accepted elements plus five fixed rational elements, with the filters and caps below; no enlarged box, new units, backend, p-adic image or point search.

## Proposed bounded target and relevance

Use L135's real-root information, L137's full finite support and ordinary
class bound, L138's actual odd model and transported quartic field, and
audited L139's supported norm kernel. The main gap remains exclusion of
residual primitive Beal solutions. A certified positive codimension from
one local place would improve the baseline for later filtered descent;
it need not reach rank one or solve the independent point and lift gaps.

The test compares the exact real Kummer image with signs of finitely many
explicitly certified supported global classes. Standard rank-nullity
permits a positive rank of their quotient images to bound the imposed
codimension from below. A witness subset need not generate the full global
sign image for that purpose. No local image, witness sign, codimension or
improved rank bound is computed in this source review.

Continue this finite test only if its exact hypotheses and support
certificates are available. Accept a strict improvement only with a
positive certified codimension; if the fixed witnesses give none, record
their insufficiency without concluding that the real filter is trivial.
Compare any resulting rank upper bound with one. Do not enlarge a failed
witness search silently or reopen backend, relation-box or point searches.

Reuse `2026-10-20-pair-jacobian-rank-bound.md` and
`2026-10-26-pair-supported-norm-dimension.md` for adequate general
coverage; inspect only the essential missing real-place theorem and
proof cases. ATTEMPTS/061 ends the dimension-only shortcut, not descent
with local conditions. The older marked-octic curve-point sign tests
concern a different map and cannot substitute for this Jacobian image.
No cross-notebook input is used. Full filtered descent, rational
points, marked and degree-nine/integer recovery, both L095 systems and
other signatures remain unresolved. Full matching Mathlib coverage is
not checked. No new mathematics is derived in this assessment.

## Primary theorem and essential proof cases

Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, Acta Arith. **98** (2001), 245–277, DOI 10.4064/aa98-3-4,
[publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83397).
Read the odd-degree setup and map on pp.249–250 and Lemma 4.8, its
complete proof and following sign paragraph on p.254. For monic squarefree
odd-degree f, with g=(deg(f)-1)/2, put m_infinity equal to the number of
irreducible factors over R (complex pairs count as quadratic factors).
The lemma states dim J(R)/2J(R)=m_infinity-1-g; its image is generated by
delta(P-infinity) for P in C(R), and the value is constant on each real
component. At nonbranch finite points its coordinates are signs of
x(P)-r at real roots r. Complex factors have trivial square-class group.

The proof invokes Schaefer, *Computing a Selmer group of a Jacobian using
functions on the curve*, Math. Ann. **310** (1998), 447–471, Proposition
2.5 for dimension; this reference was not separately retrieved. Generation
uses Stoll's Lemma 6.1, p.268 (read in full), and J(C)/2J(C)=0; constancy
uses continuity into a discrete group. Import the published Lemma 4.8
itself, without reproof or reliance on an unread Schaefer passage.

The general theorem is sufficient. The additional work is exact-instance
certification, not a new real-image theorem. Avoid branch evaluations by
using interior x-values on the allowed real intervals. The single odd
infinity has trivial image. Check that the span obtained agrees with the
lemma's dimension; a smaller sample span is not a complete local image.

## Stronger results, duplicates and failures

Harris B. Daniels, Álvaro Lozano-Robledo and Erik Wallace, *Bounds of the
rank of the Mordell–Weil group of Jacobians of Hyperelliptic Curves*,
JTNB **32** (2020), 231–258, DOI
[10.5802/jtnb.1120](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.1120/).
The inspected version is the [31-page author manuscript](https://hdaniels.people.amherst.edu/RankBounds.pdf),
with printed p.12 Proposition 2.25 (do not transfer this numbering to the
journal without checking). It refines Stoll's bound with unit signatures,
narrow class information and valuation conditions. Its hypotheses require
f to define a totally real number field of odd prime degree p. Here the
degree-five algebra is Q times a degree-four field, so this proposition
cannot be directly imported. Section 2.2, printed p.8, additionally assumes
a totally real Galois field of prime degree greater than two. Neither that
assumption nor its ordinary/narrow-class comparisons may be silently
substituted for L137's ordinary localized class bound. This source confirms
that the general signature method is known; no originality is claimed.

The reused rank assessment already covers Stoll's global descent setup;
the supported-dimension assessment covers the S-Kummer and norm section.
L135 isolates the four alpha roots in (-48,-47), (-34,-33), (-4,-3),
(20,21). L138 fixes eta=-907500/(alpha-50) and the rational root 9075.
These are existing input data, not new root calculations. L136 certifies
182 complete valuation vectors for its accepted box, but these are
T-supported, not all automatically S-supported. L137 identifies S within
that factor base by indices {1,26,27,28,29,30,31}. No sign conclusions are
contained in those class computations.

ATTEMPTS/059–060 stop the fixed relation-rank and localization tests;
ATTEMPTS/061 stops only the unfiltered dimension shortcut. ATTEMPTS/050
parks an unsuccessful bounded divisor detector. None computes this real
Jacobian image or prohibits the present filter. The marked-octic support
assessment's real point-image discussion concerns a different map with a
scalar quotient. Reusing it here would lose the odd-degree Jacobian
conventions. Unfinished L108 and all saved arithmetic remain intact.

## Fixed later execution protocol

1. Reuse L138's G, H, eta map and maximal-order identification, L135's
   isolating intervals, L136's audited full accepted valuation records and
   L137's seven support indices. Bind the entire relevant source records
   and hashes before using them. The JSON schema preview read this turn
   establishes no arithmetic; the later calculation must consume complete
   relevant values. Do not rerun the relation box or upstream audits.
2. Start with exactly the 182 accepted L136 elements b=sum a_i b_i.
   Retain an element precisely when each valuation at a T-prime outside
   the seven S-indices is even; outside T the certified valuations are
   zero. Odd valuations at excluded primes disqualify the element.
   Append the five fixed elements -1,2,3,5,11 of K. No further candidate
   construction, relation combinations or box enlargement is authorized.
   Duplicates and square classes giving zero rows may be retained.
3. For each retained b use L139's existing kernel identification
   b -> (N(b)^(-1),b). Certify the signed norm, not the old absolute ideal
   norm; record its rational sign and support using the complete ideal
   valuations/norm formula. Certify all four signs in the actual alpha
   embeddings by rational interval evaluation of the stated integral
   basis polynomials. Do not assume T-supported implies S-supported,
   positivity, unit completeness or a narrow-class bound.
4. Transport those embeddings through the exact eta map. Isolate/order
   all five roots of G, including 9075, with disjoint rational intervals
   and a saved coordinate permutation. Use that same ordering for local
   point signs and global pair signs. Start with L135's four intervals;
   permit at most 64 rational bisections per alpha root (256 total), with
   exact g evaluations and polynomial interval arithmetic. A zero midpoint
   is handled explicitly. Certify every retained element's sign and all
   needed root-order separations, or report a cap failure without a bound.
5. In the ordered root gaps choose exact rational interior samples and
   evaluate G exactly; use the gaps with G>0 and the odd infinity to
   determine the span prescribed by Lemma 4.8. Positive G permits real y;
   no rational point or rational square root is required. Verify complete
   interval coverage, the theorem's dimension, and the norm parity of
   every sign row. Encode positive as 0 and negative as 1, with no scalar
   quotient and no branch-zero sign substituted.
6. Compute the rank of the fixed global sign rows modulo that complete
   real local-image span. Apply standard finite-dimensional rank-nullity
   to L139's ambient group only after support and signs pass. Seek a
   certified positive codimension and the consequent rigorous rank upper
   bound. Compare it with one, and keep the unknown ordinary class
   contribution c explicit. Zero quotient rank ends this witness test;
   it does not establish a zero full restriction map. Positive rank is
   partial progress, not a complete descent or point classification.

Further caps: at most 187 candidate rows, five sign coordinates, matrices
of at most five rows and 192 columns including local generators, and 4096
bits for exact rational numerators/denominators. Record actual and required
bounds, full sign/support/elimination evidence and every failed condition
in certificates under scripts/pair-genus-two/ in the later research turn.
An independent replay must check the complete selected evidence and the
quotient rank. No backend or finite-place calculation is licensed.

Queries actually used include `Stoll Implementing 2 descent real image
signs Lemma 4.9 4.10`, `hyperelliptic real Kummer signs descent Jacobian`,
`Stoll 2-descent real image 4.4`, `76835 Jacobian real descent`,
`real Kummer 76835`, and `hyperelliptic real signatures Stoll Jacobian rank`.
Unrelated search hits are not inputs. A missing exact-instance hit is not
evidence of novelty. Full matching Mathlib coverage is not checked; reuse
the previous assessments' supporting algebra references without asserting
that they contain a full real-Jacobian descent theorem.

The source gate is ready for this unchanged Next action. This completes
one literature comparison only: no lemma, mathematical script, new local
image, witness enumeration, filtered dimension or rank improvement was
produced. The stronger-source comparison changes no existing proof.
