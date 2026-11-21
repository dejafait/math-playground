# Audit continuation: collective corrected-carrier floor

TARGET: Audit L745's complete-energy floor for arbitrary finite separated corrected-carrier spans, checking the coefficient norm, collective correction and logarithmic deficit uniformly in carrier count and maximum frequency.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact fixed-K,w,chi,Delta scope and completed search/comparison in 2026-11-04-collective-corrected-carrier-span.md and the invocation-start approved 2026-11-04-collective-corrected-carrier-span-specialization.md; no new search or novelty claim.
SOURCE_EVIDENCE: Montgomery--Vaughan, Hilbert's inequality (1974), Theorem 2 (1.6)/Corollary 2 (1.8), pp.74-75, proof p.82, https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf ; author-hosted Multiplicative Number Theory II, G.3/G.14, printed pp.399/422, https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf ; reuse audited L744 (3)/(6)-(8)/(12)-(13), including the DLMF 5.11.2 and 5.11(ii) inputs at https://dlmf.nist.gov/5.11.E2 and https://dlmf.nist.gov/5.11#ii . These sources were inspected in the prior recorded assessments; no new retrieval is claimed.
COMPARISON: The statement and techniques remain within the approved specialization. L745 imports the known continuous mean-square bound; only its weighted/corrected application and bounded logarithmic deficit are local. The integral-kernel estimate is justified explicitly by Cauchy--Schwarz, not attributed unproved to the finite-matrix theorem.
GAP: The written L745 proof has not received a separate conceptual audit. Its source scope does not supply low-frequency signs, moment-complement or cross-block control, arbitrary profiles, or support-uniform positivity.
REASON: Reuse ready coverage for an independent check of this new local proof before treating the entire trial space as paid. This newly written continuation requires separate supervisor approval; it neither approves its own correctness nor authorizes a broader mechanism.
SCOPE: Exactly L745's fixed K,w,chi and Delta>=Delta0; finite arbitrary-complex coefficient vectors; both carrier signs; |t_r|>=T; no upper carrier bound or fixed cardinality. No RH-conditional L742 or source positivity computation.

This assessment was proposed in step 292 and separately approved for
source scope in literature-only step 293; the proof audit remains undone.
The source versions, primary theorem hypotheses, proof cases and prior
queries remain in the two parent assessments named above. Step 292
wrote L745 without independently certifying it. The approved future
audit classification is REPRODUCTION; its purpose is conceptual_audit.

Check all quantifiers in L745 (3), not just single modulations. In (4),
verify the interval where |w|>=alpha, the translation of the imported
complex-coefficient inequality, and Delta0=4*pi/U. In (5)-(8), check
both signs in the separated inverse-fourth-power sum, the collective
H2 bound, and the threshold before squaring the lower norm estimate.

In (9)-(16), check the global lower bound for m, the bounded nonnegative
deficit, the moving inner interval |xi|<T-sqrt(T), and all constants in
the separated row sum and integrated Fourier tail. Pay particular
attention to measure dxi/(2*pi), carrier sets extending arbitrarily
far in both directions, the finite-to-infinite positive majorants,
and the deficit seminorm triangle inequality. No uniform bound for
the full positive logarithmic energy is allowed to enter implicitly.

Finally check the denominator in (17), its O(T^-1/2) error, the exact
complex-linear cancellation of both poles and the full prime-power
arithmetic payment. The direct local input is audited L744; its
provenance L740, L741 and L743 may be read only where a necessary
normalization or domain question remains. Do not use L745 as an
independently established premise in auditing itself.

Pass only if the exact uniform floor follows without cardinality,
maximum carrier, growing-support or unpaid-sign hypotheses. Repair a
real error canonically or record a precise failure if it cannot be
repaired within scope. Even a pass does not sign the low-frequency
block or complementary tests. The generic-source and prime-only stops
remain in force in their original scopes. Full matching Mathlib
coverage remains unchecked; no formal verification is claimed.


## Separate source-scope approval: step 293

LITERATURE_REASON: The supervisor requires separate approval of the
new step-292 audit continuation. This review checks its source scope;
it does not repeat the mathematical specialization or audit its proof.

Reused the completed searches and primary-source comparisons in the two
parent assessments. Read their exact theorem/hypothesis and failure
comparisons, L745's hypotheses/conclusion and coefficient-normalization
setup, and L744's hypotheses and complete-energy normalization through
(6). Read the two recorded ATTEMPTS scope stops named below. No changed
hypothesis, independent uncovered theorem, or new novelty claim emerged.

On 4 November 2026 reopened the author-hosted 1974 primary paper at the
URL in SOURCE_EVIDENCE. Rechecked Theorem 2/Corollary 2 on printed
pp.74-75 and the complete Section 4 proof passage on p.82. The finite
real separated frequencies and complex-coefficient scope match the
proposed audit. Reuse the previously inspected displayed constants;
this turn's extracted equations alone are not a new verification of them.
The two-form proof confirms that no upper-frequency or cardinality
hypothesis is being imported. G.3/G.14 and DLMF coverage remain reused
from the parent assessments, with their recorded limitations.

Decision: SPECIALIZE is approved for exactly TARGET and SCOPE above.
The source interval theorem covers the normalization input; L744 supplies
the inherited fixed-window energy, symbol and correction inputs. The
weighted synthesis application, collective correction and deficit
estimates remain proof obligations for the separate conceptual audit.
No integral-kernel theorem is imported from finite-matrix G.3, and no
summation of individual Rayleigh bounds is authorized. No reproof of
the external mean-square theorem is needed.

The generic-source scope stop in
ATTEMPTS/2026-11-04-joint-energy-generic-source-scope-stop.md and the
prime-only stop in
ATTEMPTS/2026-11-04-neutral-prime-only-rayleigh-saving-stop.md remain
unchanged. This bounded trial-space audit does not reopen their rejected
direct imports. L740/L741/L743 are provenance inputs only when a domain
or normalization issue needs resolution; L742 is not an unconditional
input. Full matching Mathlib coverage remains unchecked.

The continuation test is unchanged: accept only a complete-energy
floor with coefficient normalization and vanishing deficit uniform in
all finite both-sign carrier sets at fixed K,w,chi,Delta. A hidden
cardinality, maximum-carrier, growing-support or unpaid-sign assumption
requires canonical repair within scope or a precise failure report.
Low-frequency signs, complements and coupling remain independent gaps.
This source approval repeats adequate coverage and is honestly STALLED
as mathematical progress; it removes the procedural gate, not a proof
gap. No lemmas, mathematical scripts, DAG or PROOF edits were made.
