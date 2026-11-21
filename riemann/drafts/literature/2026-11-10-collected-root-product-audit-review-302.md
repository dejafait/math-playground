# Collected root-product decay — separate audit nomination

TARGET: Audit C999a's full-vector cutoff correspondence, fixed-radius root-pair bound and normalized coefficient recovery for its claimed all-n decay, without extending to arithmetic errors.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed review299 theorem comparison, review300 approved fixed-radius scope, and review297 exact definitions; step302 reviewed C999a's statement and proof structure only to nominate this separate audit. No new proof audit or new theorem search is represented as completed.
SOURCE_EVIDENCE: Pinned Mathlib https://github.com/leanprover-community/mathlib4/blob/428aa8288d061ec3ae75c1b85ac178e2cb9def23/Mathlib/Analysis/Polynomial/MahlerMeasure.lean — Polynomial.mahlerMeasure_le_sqrt_sum_sq_norm_coeff, Polynomial.mahlerMeasure_mul, Polynomial.mahlerMeasure_C_mul_X_add_C; Akhtari-Vaaler https://arxiv.org/pdf/1810.12413v1 (1.10)-(1.12), pp2-3; reused Macdonald1995 https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf I.2 (2.2),(2.4),(2.10)-(2.11'), pp19-24; Hardy-Ramanujan1918 https://ramanujan.sirinudi.org/Volumes/published/ram36.html (1.32), Section2.3; Ramaré2009 https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf Section2/(12)-(18)/Lemma4. Complete prior inspected cases: reviews297/299/300; direct Mahler and Fourier statements reopened in step303.
COMPARISON: Existing source coverage supplies the analytic/formal tools with repeated/circle roots and finite torus normalization; it does not independently validate C999a's assembly, length projection, threshold or all-n quantifiers. This audit uses those tools at unchanged hypotheses.
GAP: Check every load-bearing step of C999a(3)-(11), especially full-variable projection before coefficient recovery, actual-degree root factorization and uniformity through degree drops; accept, repair or reject the exact conclusion with explicit evidence.
REASON: C999a is a relevant unaudited formal input; its independent conceptual audit is bounded and does not depend on the parked arithmetic interface. No additional literature is needed unless the proof invokes a hypothesis outside the reused coverage.
SCOPE: Formal T_n/C_n of review297 and C999a only, n>=1, both ordered partition families, all factorials, full exponent vectors and length cutoff, r=2 fixed. Newly written ready continuation; next-turn approval is separate from step302's completed source review. No arithmetic substitution, alternative radius, new representation or RH estimate is authorized.

The main gap remains L030-L032/C032a actual-Xi positivity and
L966/L968 signed forcing. C999a's claimed coefficient-cost input
could support later exact arithmetic work only under a new,
adequately assessed signed interface. Review301 completed in step302
parks automatic arithmetic payment on the inspected source contracts.
That source limit does not invalidate or verify the formal result.

The exact claim to audit is, for rho=sqrt(3)/2 and partition count p,

    0<C_n<=2n(2n-1)p(2n)rho^n, n>=1,
    C_n->0, limsup log(max(1,C_n))/n=0.

Import the source tools already assessed in
2026-11-10-collected-root-product-bound-review-299.md and
2026-11-10-collected-root-product-specialization-review-300.md.
That coverage includes complex-polynomial Landau/L2 with no monicity,
integrality or zero-free-circle condition; multiplicativity; the
linear-factor formula with nonzero slope; the characteristic-zero
formal logarithm/Newton identities; normalized finite Fourier
recovery in arbitrary finite dimension; and partition growth with
an existential all-index constant. No general source theorem is to
be reproved. Full matching Mathlib coverage of C999a is unknown;
the three supporting Mahler implementations are recorded matches.

Check the following as one conceptual proof audit, not as separate
quota-bearing tasks:

- Full-vector coefficient correspondence from F_Y=log E_Y through
  P_n=2n[t^(2n)]F_Y+n^2([t^n]F_Y)^2, including all ordered splits,
  positive lengths, factorials, the projection |ell|<=n and n=1.
- Specialization to each y with |y_j|<=1; constant term1, actual
  degree0/1 and higher degrees, reciprocal-root multiplicities,
  formal logarithms, and P_n=p_n^2-p_(2n).
- Fixed-radius factorial-series majorant, Landau applied to E_y(2t),
  product of max factors, the two-root contraction and its strict
  threshold. Circle roots, repeated roots and degree drops may not
  be excluded by an unstated continuity or labeling assumption.
- Normalized Fourier recovery applied before monomial projection,
  partition support count and every n-dependent factor; positivity
  of at least one retained coefficient; existential all-n constants
  and the stated limsup with max(1,C_n).

Continue only if the complete proof establishes the exact bound and
its quantifiers. A mathematical error must be isolated and either
repaired under this existing scope or explicitly left unresolved;
finite diagnostic checks cannot substitute for the proof. Stop if
repair needs new source hypotheses or a new mechanism, saving the
failure and nominating its own REVIEW_REQUIRED continuation. A
successful audit certifies a local specialization of known tools,
not novelty or an RH candidate. No reason exists to rerun an
unchanged finite script merely to repeat its already recorded pass.

Essential inputs: C999a's canonical full proof, review297 exact
T_n/C_n, and source contracts in reviews299/300. L998/L999 and
stops296/299 are contrasts, not premises. L984(H), actual arithmetic
norms and correlations, Laguerre reconstruction, compensation,
prime powers, endpoints, both complements and regulator/infinite-zero
control remain unresolved and outside this audit. No cross-notebook
input. The audit is conceptual rather than creative; no new central
mechanism is invented to bypass the missing arithmetic coverage.


## Source-link recovery and separate approval — step303

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; repair discoverability and confirm unchanged source scope, without repeating the mathematical attempt or expanding its target.

On 10 November 2026 reopened the pinned Mathlib source above and located
all three named declarations. Landau applies to arbitrary complex
polynomials; multiplicativity includes zero factors; the linear formula
requires nonzero slope. These are supporting results, not a matching
C999a theorem. Circle roots and multiplicities impose no added exclusions.
No Lean replay was performed. Reopened Akhtari–Vaaler v1, pp2-3,
(1.10)-(1.12): Haar measure has total mass one, dimension is any positive
integer, and the finite set must contain the Fourier support. The
ordering-vector assumption of Theorem1.2 is not an assumption of these
Fourier formulas and that stronger theorem is not imported.

Reuse the completed formal algebra, partition-growth and arithmetic
source comparisons from reviews297/299/300; their hypotheses and this
audit target have not changed. Their direct primary URLs are now included
in SOURCE_EVIDENCE. No new source access barrier was found. Recorded
stops299/302 concern the balanced witness and automatic arithmetic
payment, respectively; neither verifies nor prohibits this formal audit.
The approval is SPECIALIZE for precisely the saved TARGET and SCOPE.
No proof of C999a was audited, no threshold recomputed, and no new
mathematical result established. The next research turn should perform
the complete audit already specified, classified REPRODUCTION. This is
a source-link/process repair, honestly STALLED mathematically, not a
new advance or renewed exploration budget.
