# Surviving witness span: source comparison and bounded protocol

TARGET: Assess a bounded exact test whether L147's 31 saved surviving kernel generators all lie in span{epsilon,eta_class}, or certify one Selmer class outside that span.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L138/L139/L147/L148, ATTEMPTS/065–066, histories 531/533/535 and the ready branch-annihilator assessment; web queries on Selmer square classes/Trager, Stoll Proposition 4.2 and Trager Theorem 2.2 found no usable instance computation. General algorithms cover the changed finite domain; no novelty inference follows from these searches.
SOURCE_EVIDENCE: Reused 2026-10-28-pair-branch-annihilator-test.md, including its inspected rational-factor fallback; checked primary Stoll (2001) Section 4 pp.249–253, Lemma 4.1, Proposition 4.2, Proposition 4.6 and Corollary 4.7, and Trager (1976) pp.219–221, setup, Theorems 2.1–2.3, Lemma 2.4, Corollary 2.5 and both algorithms against the changed scope. No new pairing theory is required.
COMPARISON: Stoll supplies the full product-square-class and all-place membership interface; Trager supplies a complete square decision for every nonzero quartic ratio. L148 covers three branch comparisons, not these 31 generator images. Only authenticated products and at most 124 instance comparisons remain, with no global-basis or covering assumption.
GAP: Essential source coverage is complete for this finite test; all new products, square decisions and containment/outside-class claims remain uncomputed and require later exact replay and critical review. Practical completion within the work caps is not guaranteed.
REASON: Specialize the cited interface and algorithm to the saved domain rather than reprove them. This closes a changed-scope source gate, not a mathematical dimension, pairing or rank gap.
LITERATURE_REASON: The supplied next target was REVIEW_REQUIRED because its domain changed from three fixed branch comparisons to all 31 saved coefficient-kernel generators; this turn checks that extension and its certification/stop rules while reusing ready theory.
SCOPE: The saved ordered kernel and 39 witnesses only, in L138's full Q×K group; comparison with the four products of L147's epsilon and eta_class. No new witnesses, global basis, covering search, pairing computation or point control.
COVERED_TARGET: Test by at most 124 certified full-product square-class comparisons whether L147's 31 saved surviving kernel generators all lie in span{epsilon,eta_class}, stopping at the first certified class outside that span or complete containment.

## Proposed scope and relevance

The main gap remains point control with rank J(Q)<=2+c<=4, and then
marked/integer recovery and the other Beal signatures. The proposed
intermediate test concerns only L147's saved 31-dimensional coefficient
kernel on the fixed 39 witnesses, using its authenticated complete local
conditions. Its mathematical image need not have dimension 31 or exhaust
Selmer. The reference global classes are the exact epsilon and eta_class
of L147, with masks 165 and 132102; L148 identifies epsilon with the
nonzero rational branch class and accepts zero pairing on their span.

For each saved kernel generator, comparison with the four reference-span
classes would give at most 124 global square-class comparisons in the full
Q×K group. The protocol below specifies a complete exact decision method,
including rational components, field irreducibility, positive-root
certificates, conclusive nonsquare witnesses and a bounded failure policy.
No nonsquare conclusion may follow from a failed numerical root proposal.
No such comparison is performed in this literature-only review.

If every generator is certified inside the known span, the tested witness
image has no new pairing input; any resulting whole-witness consequence
must be justified later. If one generator is certified outside, it supplies
an independently testable third class for later rational-radical/pairing
work, not a nonzero pairing or a rank improvement. Stop upon that first
certified outside class or complete the full containment certificate; an
unresolved comparison stays unresolved. Do not enlarge the witness pool,
renew ATTEMPTS/065's covering box, probe backends, or assume eta_class is
nonrational. Preserve unfinished L108 and all earlier stop evidence.

This is a ready standard-method test, not a creative-mathematics
designation. A genuinely new central mechanism has not been justified by
the fixed-pair audit alone; this narrow changed-scope gate must not be
presented as creative progress or as proof that such mechanisms are
unavailable. No cross-notebook input is proposed. Full matching Mathlib
coverage is not checked. The newly ready continuation receives the
supervisor's separate next-turn approval; this completed source review
does not execute it.

## Primary source applicability and overlap

Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, Acta Arith. 98 (2001), 245–277,
[publisher PDF, DOI 10.4064/aa98-3-4](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Section 4, pp.249–253, Lemma 4.1, Proposition 4.2 and Corollary 4.7:
the odd-degree representation is the norm kernel in L*/L*²; membership
uses local Kummer images and outside-support valuations. L138 supplies
the monic integral squarefree quintic, rational infinity, irreducible
quartic factor, exact Q×K identification and discriminant supported at
2,3,5,11. L147 supplies the complete images there and at infinity and
authenticates the entire formal kernel. Later execution must check each
product's bindings, support, norm-square property and zero local
quotients before importing the membership criterion. Equality is in both
components modulo squares, without scalars. Stoll's full Selmer algorithm
needs ambient generation; this finite test does not establish it.

Barry M. Trager, *Algebraic Factoring and Rational Function Integration*,
SYMSAC '76, pp.219–226,
[primary scan, pp.219–221](https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA11/TragerFactor.pdf):
the setup assumes characteristic zero, a finite simple field extension,
basic polynomial arithmetic and complete base-field factorization.
Theorem 2.2 recovers complete factors by gcds from a squarefree norm;
Theorem 2.3, Lemma 2.4 and Corollary 2.5 justify integer shifts. The
`sqFr_norm` and `alg_factor` algorithms are on p.221. Each nonzero
quartic ratio uses U²−b over the same certified K, a squarefree input
in characteristic zero. The number of inputs changes no hypothesis.
Reuse the ready assessment's inspected AFP Kronecker completeness
fallback for rational factors. No new square-test theorem or software
installation is needed. Algorithmic termination gives no guarantee of
finishing under the execution caps below.

Queries on 2026-10-28 were `"Selmer" "square classes" "Trager"
hyperelliptic`, `"Implementing 2-descent" "Proposition 4.2"`, and
`"Trager" "Theorem 2.2" "squarefree" factorization`. Search results
were not theorem evidence. Primary statements and relevant factorization
proof cases were directly accessible. Ready coverage is reused rather
than expanding the search into unrelated descent theory. No unread lead
is essential, and no originality claim follows.

L147/history 531 establish the kernel/interface, not its global image
dimension. L148/histories 533/535 decide only the fixed branch comparisons
and fixed-span vanishing. ATTEMPTS/065 stops one raw covering box;
ATTEMPTS/066 stops the pair containing the rational branch. Neither
decides this containment test. The SymPy import failure recorded in
history 533 remains practical evidence: do not assume a backend works.
No probing, installation or box enlargement is authorized here.

## Bounded execution and exact certificates

1. Bind the accepted L147 certificate, verification and audit, L138 model
   and order, and L148 references through their recorded hashes. Use
   `scripts/pair-genus-two/odd-membership-35-certificate.json` at
   `/all_conditions/kernel`, in saved order, and the original 39 columns
   in `two-adic-filter-certificate.json` at `/witnesses`. The inspector
   preview used here locates the schema only; it verifies no vector.
   Execution must inspect all exact inputs, verify all 31 masks, column
   ordering/ranges and their zero combinations of every local quotient
   column, and reproduce reference masks 165 and 132102. Missing bindings
   stop the calculation rather than change its domain.

2. Form each exact product in Q×K using the identified order basis,
   retaining its rational factor. Check nonzero components, norm square,
   support inherited from the authenticated columns and all local
   membership conditions; import Stoll's criterion above. Relations
   among columns are allowed. Do not identify mask independence with
   global independence or normalize by arbitrary rational scalars.

3. Compare with reference classes in order 1, epsilon, eta_class,
   epsilon*eta_class by componentwise ratios. For the rational component
   use sign and exact integer square tests on reduced numerator and
   denominator, saving roots or strict consecutive-square bounds. A
   certified nonzero full localization also proves inequality, as in
   L147; use full coordinates, not the vanished image-quotient masks.
   Local agreement cannot certify global equality.

4. A displayed quartic root must square exactly to b modulo A. Numerical
   proposals only suggest roots. Otherwise use Trager on U²−b, saving
   the shift, resultant, squarefree gcd certificate, complete rational
   factorization with irreducibility evidence, recovered gcds, inverse
   shift and complete recovered factorization. A negative decision needs
   complete irreducibility evidence or a conclusive nonsquare witness,
   such as the certified negative real evaluation used in L148. A
   product identity or failed root search is insufficient. Equality
   requires roots in both Q and K. Import the algorithm; do not reprove it.

5. The domain is at most 31×4=124 comparisons. One certified equality
   puts a generator in the reference span. Four certified inequalities,
   plus its verified Selmer membership, give the first outside-class
   witness: stop there. Containment needs an equality for every saved
   generator. This concerns only their image; no full Selmer generation,
   rationality modulo Kummer, nonzero pairing or rank improvement follows.
   Any whole-image consequence must be explicitly justified in the later
   result rather than assumed in this source review.

6. Allow at most shifts s=0,...,31 per Trager call and, if the ready
   Kronecker fallback is needed, 100000 divisor/interpolation candidates
   per comparison. Retain domain bounds and full tested evidence. These
   are work caps, not sufficient mathematical bounds. On exhaustion,
   unavailable complete rational-factor evidence or another certificate
   failure, save that comparison as unresolved. It cannot support an
   outside claim unless another conclusive witness settles it. Continue
   only within the fixed domain; absent a decisive outside witness or
   complete containment, report partial evidence. Do not renew the caps,
   add witnesses or probe backends during the step.

7. Save full products/certificates and an independent exact replay on
   disk; print outcomes, actual/required counts, caps, failures and paths.
   Replay reconstructs products from authenticated source columns and
   checks every root, nonsquare witness, norm and local membership used,
   not just producer booleans. A later separate critical audit remains
   necessary for a claimed outside class or complete containment.

A certified outside generator could supply a third independent class
relative to the accepted reference span for later radical/pairing work.
Certified containment retires this fixed witness image as a source of
another class. An unresolved test proves neither. Global generation,
eta_class modulo rational Kummer, other pairing values, coverings and
point control remain open. Source readiness supplies no new central
creative mechanism and does not undo either recorded stop.
