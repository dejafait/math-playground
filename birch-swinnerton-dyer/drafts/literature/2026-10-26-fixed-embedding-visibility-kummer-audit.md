# Fixed-embedding visibility — conditional Kummer test coverage

TARGET: Audit whether visibility of every compatible Sha component under one fixed embedding E into J over Q forces an integral strict Selmer class into the rational Kummer image, without assuming finite Sha.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The three-mechanism discovery review searched visibility/Tate-module rationality and checked the exact published fixed-embedding finiteness paragraph against pointwise visualization; its queries and failure comparisons are recorded in 2026-10-26-strict-selmer-geometric-rationality-discovery.md.
SOURCE_EVIDENCE: Agashe--Stein, JNT 97 (2002), Section 1.1 equation (1.1) and following finiteness paragraph p.173, Proposition 1.3 and splitting-extension proof pp.173--174; L005's complete integral inverse-limit Kummer proof and L006's conditional rank application read in step 509.
COMPARISON: The published source already proves fixed-embedding visibility finite with no finite-Sha premise; the only proposed difference is its applicability to a compatible p-power tower and L005's Kummer quotient, retaining the same embedding at every level.
GAP: Verify the finite-exponent/transition argument and the integral-to-rational Kummer passage; existence of a fixed embedding for the actual tower, nonzero strict-class production and comparison with complex order are not covered.
REASON: A bounded known-source audit can isolate a concrete geometric sufficient condition without repeating the generic height/Bockstein obstructions or claiming uniform geometric production.
SCOPE: E/Q has good reduction at p>=5; J/Q is an abelian variety with a fixed closed embedding i:E->J; one integral inverse-limit Selmer class has Sha components c_n in Sha(E/Q)[p^n] satisfying p*c_(n+1)=c_n, all killed by the map on H^1 induced by that same i. No assertion that such i exists is approved.

## Canonical sources and hypotheses

The precise input and source proof inspection are recorded in Section 2
of [the discovery assessment](2026-10-26-strict-selmer-geometric-rationality-discovery.md).
Citation: Agashe--Stein, *Visibility of Shafarevich--Tate Groups of Abelian
Varieties*, JNT 97 (2002), 171--185, Section 1.1, equation (1.1) and the
following paragraph, printed p.173,
[published offprint](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf#page=3).
Use only its number-field, fixed-embedding finiteness statement.
The construction theorem's extra local hypotheses are unnecessary because
no use of Theorem 3.1 is proposed. Proposition 1.3 is a contrast, not a
source of a fixed embedding for the entire tower.

The local mathematical inputs for the proposed specialization are L005
(its Kummer sequence, transition conventions and strict-class threshold)
and, only for the conditional rank-two downstream use, L006 with every
auxiliary, residual, nonvanishing and coefficient-field hypothesis.
No independent analytic-order-to-Selmer theorem is added.

## Bounded audit contract; no proof performed in this source turn

Check the class is integral before forming its compatible Sha tower;
if starting with a rationalized class, explicitly justify one scalar
clearing denominators in the specified inverse limit. Check the same
embedding and fixed finite visible subgroup contain every c_n, with
transitions multiplication by p. Inspect every quantifier in any use of
a finite exponent, then check the exact Kummer conclusion and the
nonzero/strict hypotheses required for the rank application. Distinguish
vanishing of the Tate-module obstruction of this class from finiteness
of all p-primary Sha.

The decisive comparison is **one fixed embedding for all n**, versus
**an embedding depending on n**. Do not infer a uniform exponent from
individual finiteness. Do not invoke an inverse-limit surjectivity or
uniform ambient construction that has not been justified. No search for
actual generalized-Kato geometry, new visibility theorem, coefficient
descent, mathematical script or fixed-curve computation is in scope.

Continue if the conditional inference follows with these exact hypotheses;
otherwise record its failed transition or missing hypothesis. A passed
audit is a known-source specialization and a sufficient-condition result,
not construction of a nonzero Kummer class, progress beyond the sources,
or a BSD candidate. Preserve the current absence of a fixed-embedding
producer. Any such producer needs separate source review.

This ready continuation was written in step 509; its separate approval
belongs to the next invocation. It does not retroactively gate the
completed discovery review. Mathlib coverage of the full source theorem
and proposed specialization: **not checked**.
