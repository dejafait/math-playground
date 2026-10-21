# Translated-pole centered second moment — completed source comparison

TARGET: Assess whether the centered second moment of L102's full translated-pole class distribution can certify a uniform fiber bound at T.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches covered prescribed-coefficient second moments/collisions, Hayes-class variance, split polynomials, subset products and shifted-subgroup energy; queries and inspected primary passages are recorded below, reusing prior L102 and correlated-cubic assessments.
SOURCE_EVIDENCE: Inspected Tao 245C Notes 2 (2009-04-06), Section 2 Lemma 17, Theorem 21 finite-group cases and Corollary 22; Gao 2203.06729v5 definitions (1)–(2), Proposition 2 and Theorem 3 with proofs, and Theorem 2 hypotheses; Macourt–Shkredov–Shparlinski 1701.06192v2 Theorem 1.2, Lemma 2.4 with proof and Corollary 4.1; Lai–Marino–Robinson–Wan 1910.05894v2 moment definition and Proposition 1 with proof.
COMPARISON: Standard finite-group energy tools support a centered collision reduction using L102, but no inspected theorem bounds its 67-subset energy at the finite threshold. Shifted-subgroup multiplicative energy, additive power-sum moments and random-polynomial factorial moments concern different quantities. Prior failed allowances do not lower-bound this V.
GAP: Exact mean comparison, specialized normalization, ordered collision/overlap decomposition and a sufficient quantitative bound remain mathematical obligations; no rigorous threshold obstruction was located in the inspected sources.
REASON: Primary coverage permits one bounded specialization of standard energy identities to L102 with an exact threshold diagnostic; no effective bound, mathematical advance or novelty is claimed.
SCOPE: Only L102's pole 3, 67-subset distribution over the full E^2 times E^*, Q=65537, H=<19139> of size 1024, ambient F=F_(Q^28), degree<64 and every m>=1; centered collision reduction and one threshold diagnostic, without a new character theorem, changed pole, absolute-sieve retuning or projective transport.
LITERATURE_REASON: Changed target from literal projective transport to centered collision energy; the existing ready transport and pointwise-sieve assessments did not cover this estimate.

## Preserved target and relevance

The main gap remains arbitrary-center safety at 67/68 agreements and
the 955–957 bracket. This target concerns only L102's family. A uniform
fiber bound would exclude that family as a threshold witness, leaving
arbitrary centers and the ABF-model comparison unresolved. L103 supplies
stop evidence, not a premise for a moment bound.

Use E=F_65537, H=<19139>, F=F_(65537^28), k=64, every m>=1 and
T=65537^28/2^128. L102 defines N(a,b,c) on E^2 times E^*. Preserve
C=binomial(1024,67), D=(65537-1)*65537^2 and the proposed test

    V = sum_(a,b in E, c in E^*) (N(a,b,c)-C/D)^2,
    V <= (T-C/D)^2, subject to C/D<T.

No bound, specialized identity, positive mean gap or finite threshold
comparison is proved in this literature turn. Empty labels stay in the
sum. The full group cannot be replaced by E^2 times H. Neither uniformity
nor an actual large fiber is assumed. The concrete intermediate target
for a later turn is the exact centered collision reduction, its overlap
classes and quantitative requirement, followed by one rigorous diagnostic.

## Completed review — step 387

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; EXPLORATION.
This fills source coverage for a bounded test, without mathematical
progress beyond the inspected sources. Search failure is not evidence of
novelty or nonexistence of stronger results. No lemma, mathematical script,
certificate or candidate solution was produced. The newly ready assessment
requires separate supervisor approval before a mathematical invocation.

The local check read L102's dictionary, full Fourier normalization and
stopped allowance, its construction/audit assessments, the fixed-pole
working note and histories 379–380, ATTEMPTS/085–086, C012a's fixed-field
statement and the pinned simultaneous-list definition. For the energy
comparison it read L017's energy proof, L018's elimination and small-
difference cases, ATTEMPTS/007–008 and the ready correlated-cubic assessment.
The earlier fixed-pole discovery is reused. L099/L100 and L103 remain
comparisons or stop evidence, not new mathematical inputs.

### Discovery and primary-source comparison

Queries included `"prescribed coefficients" "second moment" finite
fields polynomials subsets`, `"Hayes" "variance" polynomials`,
`"subset products" "multiplicative subgroup" translated energy`,
`finite fields subset sum product prescribed elementary symmetric
coefficients counting Gao moment`, `shifted multiplicative subgroup
higher multiplicative energy Shkredov 2017`, `prescribed coefficients
completely split polynomials multiplicative subgroup character sums`,
`"prescribed coefficients" "collision" polynomials finite fields`,
`"split polynomials" "variance" finite fields`, and `"subset products"
finite abelian group Fourier variance`. Several searches returned
unrelated material; those hits supply no theorem evidence.

1. Tao, [245C Notes 2: The Fourier transform](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
   2009-04-06, Section 2 Lemma 17, Theorem 21 and Corollary 22.
   Read orthogonality, both finite-abelian-group completeness arguments,
   and Parseval with probability Haar measure. These apply to any
   function on L102's finite abelian unit group, without a distribution
   hypothesis. Import them, checking conversion to unnormalized sums.
   The elementary finite-sum norm comparison supports the proposed
   sufficient-test framework once the positive mean gap is verified.
   No specialized proof is given here. The source does not estimate
   the subset energy.
2. Gao, [Asymptotic distributions of the number of zeros of random
   polynomials in Hayes equivalence class over a finite field,
   2203.06729v5](https://arxiv.org/html/2203.06729v5), 2024-01-07,
   definitions (1)–(2), (5)–(6), Proposition 2 (15)–(16), Theorem 3
   (17)–(19), including generating-function/coefficient-extraction proofs.
   Arbitrary domains avoiding the modulus zeros are allowed. Reuse
   L102's specialization: source q=65537, modulus (X-3)^3, t=3, ell=0,
   k=64, j=67, domain H and residual degree zero. Its factorial moments
   count roots of a random polynomial within a class, rather than
   variance of subset counts across classes. Theorem 2 assumes the full
   complement domain and ell>=1 and is asymptotic; it cannot replace a
   finite proper-H variance estimate.
3. Macourt, Shkredov and Shparlinski, [Multiplicative Energy of Shifted
   Subgroups and Bounds On Exponential Sums with Trinomials in Finite
   Fields, 1701.06192v2](https://arxiv.org/html/1701.06192v2), 2017-10-17,
   Theorem 1.2, Section 2 Lemma 2.4 with its collinearity proof, and
   Section 4.1 Corollary 4.1 with its reduction to Theorem 1.2.
   For a subgroup G of F_p^* and nonzero lambda, the corollary bounds
   E^times(G+lambda)-|G|^4/p with three size-dependent error branches
   and unspecified absolute constants. This counts product-equal
   quadruples, not 67-subset collisions retaining two nilpotent-unit
   coordinates. No transfer or explicit finite constant for our test
   is supplied. This is comparison evidence only, not an upper
   certificate or a lower obstruction for V.
4. Lai, Marino, Robinson and Wan, [Moment subset sums over finite
   fields, 1910.05894v2](https://arxiv.org/html/1910.05894v2), 2019-10-19,
   Section 1 definition of N_k(D,b,m), Section 2 Proposition 1 and proof;
   reuse the prior correlated-cubic assessment for its Section 3 sieve.
   Its moments prescribe additive power sums. Proposition 1 assumes a
   polynomial f of degree m with p not dividing m and a monomial-image
   domain D={x^n} with (n+1)^2<=q. It bounds an incomplete additive
   character sum, not mixed product/reciprocal subset collision energy.
   No assertion that the inverse translated domain is such an image,
   or that a multiplicative condition may be dropped without changing
   the centered baseline, is approved.

The Li–Wan weighted sieve and complete character estimate remain covered
at their exact primary passages in the prior L102 assessment; no repeated
browsing or reproof is needed. They do not themselves estimate the sum of
squared subset Fourier coefficients. No essential unread theorem is used
in the bounded reduction below. Search-only leads about short-interval
polynomial variance, random subset-product covering and full-field two-
power-sum formulas were not inspected as theorem inputs and supply no
approved estimate.

### Duplicate/failure comparison and bounded continuation

ATTEMPTS/085 stops L102's absolute allowance, with U/T in (4780,4781).
ATTEMPTS/086 stops its literal projective transport to L099. Neither
bounds the actual V from below. L017 instead involves 66-subsets and a
complete residual root, with signed energy J_3-J_2/Q. ATTEMPTS/007 stops
its unsigned cycle-norm estimate. L018 eliminates that residual pair and
ATTEMPTS/008 stops one generic quadratic-root allowance. Those are not
L102's residue-class dictionary and cannot be numerically transferred.
They warn against losing the centered cancellation or mistaking failure
of an upper allowance for a lower bound on actual energy.

The unchanged TARGET permits one mathematical turn after separate approval:

- Start from L102's entire-list dictionary and full G, W_chi. Check
  C/D<T by exact arithmetic. Derive the centered Parseval and ordered
  subset-pair forms with all D factors. Keep every empty label and
  every nonprincipal character type; import the cited identities.
- If common subset factors are canceled, justify their invertibility
  modulo (X-3)^3 and count common-subset choices exactly. Check the
  diagonal and every small symmetric-difference case before assuming
  a residual collision condition. These are tasks, not results here.
- Compare any rigorous centered bound with exactly (T-C/D)^2. Keep
  the principal subtraction, exceptional cases and ordered/unordered
  factors. A nonnegative raw collision count does not permit dropping
  a negative centering term from a lower certificate.
- Do not repeat L017's L2 triangle estimate, L018's generic two-root
  allowance, or L102's pointwise envelope with renamed constants.
  An exact overlap reduction may help even when a bulk collision
  estimate remains independent and unresolved; identify its required
  scale rather than presenting the reduction as a bound.

Continue on a quantitatively discriminating bound or exact reduction
identifying a new remaining estimate. A valid upper certificate at the
proposed threshold would exclude this family for every m via L102, while
leaving arbitrary centers unresolved. A rigorous lower bound exceeding
the threshold abandons this sufficient test only; it does not imply a
fiber above T. An insufficient upper allowance stops that allowance,
not the actual moment. If only a formal reduction and unresolved bulk
collisions result, report EXPLORATION and charge the existing budget.
Source readiness neither makes success likely nor renews that budget.

Essential inputs are L102, C012a and foundations/02. L001 is used through
L102, not independently rederived. Prior fixed-pole and correlated-cubic
assessments and ATTEMPTS/007–008,085–086 are comparisons; L103 is stop
evidence only. No cross-notebook input is proposed. Arbitrary-center
safety, the actual fiber maximum and the ABF comparison remain open.
Full/supporting Mathlib coverage is not checked; no absence is inferred.
This literature turn spends no mathematical exploration turn: 1/3 remains.
