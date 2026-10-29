# Displacement-weighted actual-Xi negative mass — bounded attempt coverage

TARGET: Test a zero-safe displacement-weighted conjugate-pair majorant for N(T) against the o(T(log T)^3) threshold.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the bounded exact-negative-part, first-sign, zero-window and Hardy-moment search completed in 2026-10-27-actual-xi-negative-part-mean-coverage.md; no matching weighted negative-mass theorem was established. This is not a novelty certification.
SOURCE_EVIDENCE: Direct primary sources reopened 2026-10-27: https://arxiv.org/html/1309.0055v2 Definition 1.1 and Proposition 2.2/proof (2.3); https://rstation.ai/problems/riemann_hypothesis/papers/50 displayed v2 Section 2 Lemma 1/proof; https://arxiv.org/html/2304.05178v1 (1), Theorem 3 and Proposition 3; https://rstation.ai/problems/riemann_hypothesis/papers/41 displayed v4 Theorems 3–4 and Section 8.6. Local coverage reuses L018, L251 and L465 Sections 1 and 5; L024's complete product proof was read in this repair.
COMPARISON: The pair identity and sign windows are known and must be cited, not rediscovered. Ordinary moments and existing window density do not state a displacement-weighted integrated majorant with a little-o saving; the proposed difference is its zero-safe application and summation for actual Xi.
GAP: Preserve cancellation of apparent pair denominators by the actual Xi factors before estimating; determine whether the resulting weighted contributions admit a strict asymptotic saving without a new zero-weighted moment assumption. No majorant or such saving is established.
REASON: The separate literature-only recovery review supplies direct source URLs and confirms the existing EXPLORE scope for one bounded creative test at the fixed initial-sign gap; no majorant or saving has been proved. The mechanism differs from scalar barriers, finite polynomial closure, coarse count/gap compensation and growing-order mean approximation.
LITERATURE_REASON: Supervisor recovery required direct primary-source URLs in this ready assessment; this repairs citation completeness using the existing comparison, without launching another discovery search or changing the target.
SCOPE: Same A(t) and N(T) as the completed assessment, real T>=2; actual-Xi conjugate zeros gamma±id with 0<d<1/2, multiplicity counted; ordinary derivatives. No RH, simplicity, positive lower displacement, external half-plane premise, independence or unproved arithmetic moment is available.

## One proposed test, not an established majorant

The main gap is all-height initial signs and global mixed positivity.
The intermediate target remains N(T)=o(T(log T)^3), not RH. Its possible
use is quantitative control of exceptional first-sign mass. Converting
small mass into exclusion of individual negative heights, controlling
higher initial indices and proving global mixed positivity would remain
unresolved even if this target succeeded.

Import the known pair kernel from the primary citation in the completed
assessment. Attempt to majorize the negative part by pair contributions
only inside their negative windows, keeping Xi(t)^2/A(t)^2 attached to
each term until the pair factors are canceled. Work with entire divided
factors, including repeated conjugate pairs and real central zeros;
avoid division by Xi on its real zero set. The arithmetic question is
whether the retained dependence on d can be summed at a saving over
T(log T)^3. No desired displacement power or zero-derivative estimate
is assumed. A local kernel computation alone is only reproduction.

Continue only with a proved summation saving or an explicit, quantified
missing weighted estimate tied to the proposed majorant. If known
moments/density lose that saving, record the actual versus required
scale and stop this implementation; do not rerun the old coarse-count
countermodel. Do not presume that negativity accompanies every off-line
zero: L251 already warns against that implication. Boundary windows
intersecting [T,2T], multiplicities, infinite-product passage and the
gamma gauge must be accounted for. If a needed theorem lies outside
this assessed source scope, save the partial attempt and mark the new
target REVIEW_REQUIRED instead of importing it from memory.

No proof is undertaken in preparing this assessment. Full matching
Mathlib coverage is unchecked. No theorem from another notebook is used.

## Separate source-scope review, 27 October 2026

Direct retrieval succeeded for all four URLs in SOURCE_EVIDENCE. This
repairs the reported process defect; it does not strengthen the earlier
search result. The assessment remains EXPLORE, not an import of the
proposed bound. No new mathematics was derived in this review.

- [Csordas v2](https://arxiv.org/html/1309.0055v2), Definition 1.1
  and Proposition 2.2/proof (2.3): the class has a nonpositive quadratic
  exponential, strip zeros and inverse-square summability. The literal
  proposition assumes f(0) nonzero and a zero-free vertical interval of
  width greater than two. The finer pair-sign condition is in its proof.
  Use that cited identity only off the real zeros; extending the intended
  majorant there remains part of the saved test, not an imported theorem.
- [Paper 50 v2](https://rstation.ai/problems/riemann_hypothesis/papers/50),
  Section 2, (2.1), Lemma 1 and its complete proof: all coefficients are
  nonnegative under the non-strict window exclusion for every right-side
  zero. The displayed product retains central multiplicity and passes
  coefficients by local uniform convergence. This covers localization,
  including equality, but supplies no amplitude-weighted integral.
- [Bui–Hall v1](https://arxiv.org/html/2304.05178v1), (1), Theorem 3
  and Proposition 3: the inputs are signed fixed-derivative moments and
  a shifted fourth moment uniform for shifts O(1/log T). Proposition 3's
  proof is explicitly omitted by the authors. No zero-indexed weight or
  clipped negative part appears in these statements. Retain the prior
  assessment's distinction between source theorem and independent audit.
- [Paper 41 v4](https://rstation.ai/problems/riemann_hypothesis/papers/41),
  Theorem 3 (7d), Theorem 4 and Section 8.6 (63a)–(63e): the fixed-order
  mean remainder has no vanishing factor in height; typical-height
  positivity requires diverging orders. Its proof explicitly separates
  complementary arcs and the Xi gamma gauge. This does not cover the
  proposed fixed-order weighted saving.

The complete L024 proof confirms the available locally uniform product,
with multiplicities, without reality of zeros. Reusing it in the proposed
integrated bound still requires the application checks above. The recorded
failure `ATTEMPTS/2026-09-27-count-and-gap-first-sign-test.md` was reread:
its count/gap countermodel stops those assumptions alone, not the new
actual-Xi amplitude-weighted question. The completed comparison retains
the L251 masking and endpoint mean-square warnings. Neither literature
review nor this repair establishes novelty or full Mathlib coverage.
