# Fixed scalar Q_6 count — independent audit coverage approved2062

TARGET: Independently audit C029y's exact scalar Q_6 two-real-root certificate, including all odd coefficients, N=6 weights, every Sturm division, terminal nondegeneracy and variation signs, without changing the fixed input bounds.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Approval2062 reuses completed assessment2059/comparison2058 for the unchanged finite polynomial; searches for primary Sturm signed-remainder statements located Coste2002 Section1.1. Read its real-coefficient hypotheses, theorem, proof cases and whole-line conclusion; no novelty search or output-root calculation claimed.
SOURCE_EVIDENCE: Kuznetsov2008 https://doi.org/10.4153/CMB-2008-055-0 equations(4)/(13) pp563/566, Proposition4.1 p567 and Jensen-weighted family pp568–569 supply the finite conventions already inspected in assessment2059. C029n Section1 supplies exact coefficients and elementary pi/sqrt(2) enclosure proof; C029q Hypotheses supplies normalization. Classical Sturm theorem is the imported real-root-count theorem. Coste2002 Section1.1, Theorem1.1 pp5–6 and Proposition1.4 p7 provide the explicit real-coefficient Sturm count; direct source and inspected scope below. The finite certificate is in C029y, not these sources.
COMPARISON: The same finite input-condition screen remains inside assessment2059's source scope. The additional work is an independent exact-arithmetic reconstruction/replay and proof audit; no new partial-biorthogonality or all-N theorem is proposed. Literature does not supply or verify this explicit Q_6 count.
GAP: C029y's new coefficient reconstruction, interval long-division inclusion argument, complete signed remainder chain, nonzero terminal constant and infinity variations have not received separate independent audit. Its two-real-root conclusion is a finite negative diagnostic only.
REASON: Separate literature approval2062 completes theorem-level audit coverage for the unchanged target; the bounded audit is now ready under SPECIALIZE. No coefficient, division or root-count replay was performed in this approval.
SCOPE: The single exact N=6 scalar polynomial and fixed 60-place rational input bounds only; all odd entries, scalar factors and own-degree Jensen weights retained. Independent reconstruction or exact enclosure replay is permitted. No U_N output-root count, degree sweep, new analytic transfer, or coefficient modification is covered.

The nomination in step2061 reused prior primary-source comparison.
Separate approval2062 below supersedes its pending-approval status,
without changing TARGET, DECISION, SCOPE or the completed calculation.
The mathematical audit itself remains pending.

Audit essential inputs: C029n exact finite coefficient formulas and
elementary input bounds; C029q finite normalization; C029y full proof;
`scripts/pollaczek/actual_scalar_q6_2061.py` and its complete JSON
certificate. Independently check every coefficient and rational weight,
the derivative, all five signed divisions including both top cancellations,
degree sequence 6,...,0, all required nonzero signs, gcd/square-free
inference, and variations 4 and2. A preview or matching floating roots
does not verify these claims. Save full audit evidence under
scripts/pollaczek/ and report any exact disagreement; do not silently
repair the original certificate or hide its failures.

Continue only if these checks justify the exact count and finite scope;
otherwise identify the failed coefficient, enclosure, sign or logical
step, preserve the original evidence and qualify the stop decision.
Separate analytic moment identity, integrability/Chebyshev matching,
uniform Q_N/index control, initialization, degree drops, weighted
convergence/upstream[9] and Xi transfer remain unresolved regardless of
the audit outcome. No cross-notebook input; Mathlib matching unchecked.


## Separate source approval2062 (2026-11-21)

LITERATURE_REASON: The supervisor requires separate approval of the new
continuation. Supply the previously unnamed exact Sturm source and check
its real-coefficient scope, while reusing the ready finite-family comparison.

Queries: `site.dlmf.nist.gov Sturm theorem polynomial remainders` and
`Sturm theorem real polynomials signed remainder sequence theorem primary
lecture notes`. Inspected sources, rather than search snippets:

- Michel Coste, *An Introduction to Semialgebraic Geometry*, October2002,
  [course notes](https://users.fmf.uni-lj.si/cimpric/courses04/seminar/SAG.pdf),
  Section1.1 pp5–7. Theorem1.1 assumes a nonconstant real polynomial
  without multiple roots, starts with P,P', uses negative Euclidean
  remainders, and counts roots between endpoints which are not roots.
  Zeros in the sign list are omitted. The proof on p6 treats crossings
  of P separately from crossings of an intermediate remainder; the
  latter have opposite-sign neighbours and preserve variation.
  Theorem1.2 covers distinct roots with multiplicities present, but is
  unnecessary if the proposed terminal-constant check succeeds.
  Proposition1.4 p7 gives the total distinct-real-root count from the
  two infinity variations using leading signs and degrees. This is
  explicitly over R, so transcendental coefficients are permitted.
- Kuznetsov2008, [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf),
  equation(13) p566, Proposition4.1 p567 and Jensen multipliers p568
  reread; equation(4) comparison reused from assessment2059. Proposition4.1
  is sufficient all-real scalar input to all-real Pollaczek output, not
  a partial-node theorem or this explicit root certificate.
- [Mathlib Sturm.Sequence documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Sturm/Sequence.html),
  inspected module scope and Main results: `Polynomial.sturmSeq`,
  `sturmSeq_cons`, `zero_notMem_sturmSeq`, `dvd_of_mem_sturmSeq` support
  algebraic sequence properties. The module explicitly contains only
  algebraic properties; its introductory mention of root counting is
  not a formal root-count theorem supplied by this file. Full matching
  Q_6 theorem and root-count coverage elsewhere remain unchecked.

The local comparison read C029y's entire proof, C029n's coefficient
formulas/Section1 opening, C029q's normalization, assessment2059 and its
recorded failure distinctions, and stop2061. This was scope inspection,
not independent verification of the saved numbers or program. No new
lemma, mathematical script or certificate was written or run.

Approval: SPECIALIZE is adequate for independent arithmetic reconstruction
and enclosure replay of this one fixed input. Coste supplies the theorem;
the audit must establish every finite hypothesis and all signs itself.
A rational-coefficient-only algorithm must not be substituted silently
for the actual real polynomial. Fixed-bound interval evaluation must
include the true signed-remainder chain, not merely produce some chain
inside coefficient intervals. Exact canceled leading terms need their
algebraic identities; interval containment of zero alone cannot justify
deletion. A failed denominator or leading sign ends certification at the
stated bounds and must be reported, rather than triggering a sweep.

The downstream use is validation or correction of a finite route stop:
only a fully replayed count below four sustains this N=6 baseline's stop.
Even success leaves all analytic/uniform and Xi gaps listed above open.
No reproof of Sturm or new transfer argument is warranted. No source
blocker remains for the exact saved audit, and no independently supported
creative mechanism is nominated by this narrow approval.
