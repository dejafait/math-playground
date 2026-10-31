# L487 critical-audit scope — source coverage approved

TARGET: Independently audit L487's full quartic heat collision-energy certificate on t in [0,1/100], replaying root signs, external flux, internal-interface balance, collision regularity, scaled-energy derivative and terminal Gronwall obstruction; repair any failed claim locally.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-energy/collision searches and duplicate/failure comparison in drafts/literature/2026-10-30-backward-heat-negative-energy-coverage.md and direct-source recovery in drafts/literature/2026-10-30-polynomial-heat-energy-obstruction.md; read full L487 and its recorded failed mechanism solely to identify audit obligations. No new discovery search or mathematical audit was performed.
SOURCE_EVIDENCE: Reused inspected primary-source coverage: Alber, PDE 2, revised 10 June 2018, Lemma 5.2/Theorem 5.3, pp. 90--92, https://www2.mathematik.tu-darmstadt.de/~alber/pde_2.pdf ; Brezis--Ponce, Comm. Contemp. Math. 10 (2008), Theorem 7.1 and proof, pp. 1234--1236, https://sites.math.rutgers.edu/~brezis/PUBlications/198journal.pdf ; standard named real analytic implicit function theorem and integral Gronwall inequality. Exact hypotheses and limitations are below.
COMPARISON: Known tools cover smooth polynomial truncation, external normal traces, simple-root continuation and absolutely continuous scalar comparison. They do not evaluate this energy, prove its sign regions, remove internal interfaces or establish its derivative asymptotic. Auditing that finite specialization is justified; reproving general source theorems is unnecessary.
GAP: Certificate correctness remains unaudited: replay every parameter inequality, complete root/sign counts, zero external flux, nonzero internal-interface balance, collision absolute continuity and analytic derivative-ratio argument. Actual-Xi realization and signed mass control remain outside coverage.
REASON: This separate literature turn approves the nominated exact audit by comparison with ready coverage. No essential unread source remains for the finite audit; scope approval is process progress only, not a new mathematical result.

SCOPE: Independent finite-polynomial proof audit and local repair of L487 only; no new family, actual-Xi mechanism, infinite-domain energy estimate or collision-exclusion theorem.

## Separate scope approval, 2026-10-30

LITERATURE_REASON: The preceding research turn nominated this exact audit with REVIEW_REQUIRED. This turn compares that changed scope with inspected tools; it does not refresh unchanged coverage or repeat discovery.

The completed source-review target was: “Review source coverage for an
independent critical audit of L487's quartic heat collision-energy
certificate, including root signs, internal-interface terms and the
terminal Gronwall obstruction.” Approval is now given for the TARGET
above; certificate correctness still needs a separate research turn.

These comparisons reuse primary statements and essential proof cases
actually inspected in the polynomial assessment. No new source fetch
was needed, and no unread lead is an input.

- Alber's Lemma 5.2/Theorem 5.3 apply on a bounded open set to
  u in W^{1,p}, 1<=p<infinity, giving positive-part regularity and weak
  derivative 1_{u>0} partial_j u, with the a.e. zero-level qualification.
  The recorded bounded-approximation and zero-level proof coverage
  suffices for smooth polynomial spacetime functions. It does not
  establish every-time differentiation of this energy by itself.
- Brezis--Ponce Theorem 7.1 applies to u in W^{2,1}(Omega). The
  recorded boundary cases give partial_n(u_+)=partial_n u for u>0,
  zero for u<0, and min(partial_n u,0) for u=0, a.e. on the boundary.
  Smooth polynomial spatial slices satisfy the regularity hypothesis.
  This is external trace coverage; internal interfaces of {q<0} remain
  separate. L487 claims direct collar vanishing and interval integration,
  both still to be checked. No W^{2,1} regularity of u_+ is inferred.
- The standard real analytic implicit function theorem requires a
  nonzero derivative in the root variable. Verify it for every claimed
  cubic root away from t=0 and both scaled roots at r=0. Applying it
  directly to a colliding double root is invalid. Analytic primitives
  and the Leibniz integral rule cover the energy formulas only after
  root simplicity and the endpoint identities have been checked.
- The standard integral Gronwall inequality requires a nonnegative
  absolutely continuous scalar function, zero initial value and an
  a.e. upper differential bound with an integrable upper coefficient.
  Check time orientation, absolute continuity through t=0 and local
  essential boundedness there. Differentiating an unspecified error
  term is insufficient: replay the claimed exact analytic scaled-energy
  identity before accepting the derivative asymptotic.

No reused theorem verifies this exact quartic certificate. Direct finite
algebra and energy replay are the identified specialization, not a reason
to reprove general truncation or comparison theorems. Keady's
positive-solution result remains a contrast: its positivity hypothesis
through the relevant interval is not supplied at the terminal collision.
The recorded L469 and L126/L128 stops concern different mechanisms and
do not ban this audit or restore the generic comparison. No new overlap
or novelty conclusion is asserted.

The intended later audit is a finite algebra/root/energy replay, not a
subtle actual-Xi analytic limit. It should check all t in [0,1/100],
including the terminal double roots, and distinguish vanishing
moving-endpoint terms in time differentiation from the nonvanishing
internal terms in integration by parts. A numerical preview is
insufficient. L487 claims no theta representation and has no direct
notebook mathematical input. L058/L018 are structural comparisons;
L471/L486 explain relevance only; L469 and L126/L128 are distinct
obstructions, not premises.

Mathlib full matching coverage is unchecked. The possible conclusion
is only the generic comparison obstruction, never actual-Xi multiple
zeros, signed negative-mass saving or RH. This file does not authorize
a new actual-Xi mechanism or a new lemma.

Continuation test: continue if complete replay supports every certificate
claim. Repair or qualify any failed claim and reassess the obstruction
if a load-bearing condition fails. Do not restart the generic bounded
comparison without a materially new input. A creative actual-Xi target
still lacks a discriminating additional actual-Xi hypothesis or mechanism.
