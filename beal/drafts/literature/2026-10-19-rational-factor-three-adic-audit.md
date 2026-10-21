# L099 critical application audit — coverage approved

TARGET: Independently audit L099's two primitive three-adic lifts and its reconstruction of both complete L095 systems.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the unchanged exact-system searches and source comparisons in 2026-10-19-rational-factor-three-adic-realization.md; read L099, full L095 including its independent audit, the local attempt, history 335 and ATTEMPTS/046. These records contain no completed independent L099 audit.
SOURCE_EVIDENCE: Reopened Zabradi, Notes for the course p-adic methods in arithmetic, 29 June 2022, Lemma 2.3 and Theorem 2.4 with their complete proofs, printed p.4 (PDF index 3); compared foundations/17-local-power-hensel-inputs.md and L095 identity (4) with the claimed L099 inputs.
COMPARISON: The inspected Hensel theorem supplies the lifting method but neither the two numerical hypotheses nor the scaled reconstruction; independent verification of this explicit specialization remains necessary. No new theorem or general cube-root surjectivity is needed.
GAP: Independently verify the substituted polynomials, both exact seed errors and derivatives, strict lifting hypotheses, nonzero primitive coordinates and both common-tuple reconstructions; no such audit is completed here.
REASON: Essential theorem and dependency coverage is sufficient for the stated bounded audit; EXPLORE authorizes checking the specialization without certifying its correctness or originality.
LITERATURE_REASON: The newly written L099 needs separate audit coverage approval; this turn compares its actual dependencies with ready source coverage rather than repeating the earlier discovery searches.
SCOPE: Exactly TARGET over Z_3 using L095, L099, foundations/17-local-power-hensel-inputs.md and the existing three-lifts certificates; elementary exact arithmetic, polynomial identities, valuations and the inspected Hensel criterion only.

## Source comparison and precise scope

The completed review answers the saved request to assess source and
dependency coverage. The TARGET above is the resulting approved next
audit, not a claim that this review performed that audit.

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, 29 June 2022,
[author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
Lemma 2.3 and Theorem 2.4, printed p.4, were inspected again on
2026-10-19. For integral f and alpha, the theorem requires an error
zero modulo p^n and a chosen partial derivative of valuation k with
0 <= 2k < n. It gives an exact integral root congruent to alpha
modulo p^(n-k). Its proof iterates the preceding one-variable lifting
lemma while keeping other coordinates fixed; that lemma preserves
the derivative valuation at each lift. These are cited inputs, with
no reproof proposed. The PDF identifies its date and author on p.1.

L099 claims the one-variable case p=3, n=3, k=0 after fixing m,a
and substituting C in terms of u. The theorem covers this method;
the audit must establish the claimed integrality, actual errors,
derivatives and congruences independently. Clark's Newton theorem and
unit decomposition remain available background, not essential new
inputs. The cube coordinate is fixed, so no theorem asserting all
three-adic units are cubes is required or available from this source.

Audited L095 supplies the full displayed Q,H and polynomial identity
(4), including both scales and converse qualifications. The audit
needs its identity evaluated over Z_3, not an application of its
positive-integer converse to local coordinates. Check system I with
N=C and system II with N=5C, retaining the defining C relation before
differentiation. Verify the claimed derivative scales, cancellation
of 5^11, and one shared lifted u in both equations. Check nonzero
m,u,a,A,B,C, local pair primitivity, B,C units and the permitted
nonunit A. Positivity and coprimality at other primes are outside the
local claim. L093's global algebra theorem is upstream context of
L095, not an extra theorem needed to audit these local identities.

## Evidence inventory and duplicate/failure check

Read L099's full proof and L095's full independent audit. The original
generator `scripts/rational-factor/check_three_lifts.py` was inspected
without execution to locate the stored evidence. The certificate
inspector located both system records, complete surviving-triple
arrays, exact seed errors and derivatives, residue records, scales,
Hensel parameters, checks and failures in
`scripts/rational-factor/three-lifts-certificate.json`. It also located
both rows and failures in
`scripts/rational-factor/three-lifts-identity-crosscheck.json`.
These schema previews establish evidence locations only. No numerical
value, check total or proof is independently certified by this review.
An initial root pointer `/` was rejected; the valid default root
preview was used only for this inventory.

The later audit must inspect complete load-bearing fields and
independently reconstruct the arithmetic; existing pass flags and
810-triple previews do not suffice. To certify L099's ancillary search
counts, replay the full finite domain and compare complete stored
lists, retaining zero cube residues. For the existence proof, check
the exact errors and derivatives, all H coefficients and both scales;
finite residue survival alone cannot establish existence. The existing
cross-check file is supporting evidence, not an independent critical
application audit. No mathematical scripts were run or written here.

Reuse the realization assessment's bounded search and primary Putz
comparison unchanged. Its coefficient-one scope has not moved; the
special three-adic rows remain outside that scope. No new global
exclusion or novelty conclusion follows. History 335, the completed
local attempt and ATTEMPTS/046 record construction and the retirement
of standalone three-adic exclusion, while expressly leaving this
audit pending. L096 is contrast at eleven only. The rational octic
factorization and arithmetic-backend parks are not reopened.

## Main gap, use and continuation test

The main gap is integer elimination of L095's two rational-factor
systems within ordered (3,5,11), with other algebra factors and other
Beal signatures independently unresolved. The intermediate target is
correctness of L099's exact local existence claims. A successful audit
would secure the reason to stop standalone three-adic nonexistence
and direct later work toward global compatibility; it would supply
no integer solution or signature exclusion.

Coverage test met: the inspected theorem and audited polynomial
identity supply all essential methods within this scope. Approve one
separate proof/arithmetic audit. Its acceptance test is that both full
specializations, strict hypotheses, complete relevant arithmetic and
primitive reconstructions pass. A failed scale, derivative, error or
nonzero-coordinate check requires isolating the defect and repairing
within scope or parking the affected claim. Do not increase search
precision or undertake a new local classification in this audit.

Mathlib coverage of the full systems and supporting declarations remains
not checked; unknown coverage is not an absence claim. This literature
review adds no lemma, arithmetic certificate or mathematical result.
