# L100 independent audit — coverage approved

TARGET: Independently audit L100's two-adic lifts and both complete-system reconstructions.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the unchanged exact-system discovery and primary Putz comparison in 2026-10-19-rational-factor-two-adic-solvability.md; read full L100, full L095 with its independent audit, the original generator, history 339 and ATTEMPTS/047. These records leave the independent L100 audit pending.
SOURCE_EVIDENCE: Zabradi, Notes for the course p-adic methods in arithmetic, 29 June 2022, Lemma 2.3 and Theorem 2.4, printed p.4 (PDF index 3), statements and complete proofs reopened; compared foundations/17-local-power-hensel-inputs.md and audited L095 identity (4) with every method used in L100.
COMPARISON: The primary Hensel theorem and audited integral identity cover all methods needed; neither source certifies L100's numerical specialization, uniqueness argument or common-tuple reconstruction. No new external theorem is essential.
GAP: Independently verify all coefficients, seed errors, derivatives, strict bounds, uniqueness, nonzero primitive coordinates and both scaled reconstructions; this review does not perform that verification.
REASON: Essential method coverage is ready for one separate bounded critical audit; EXPLORE permits checking this specialization without a correctness or originality claim.
LITERATURE_REASON: The newly written L100 requires separate audit coverage approval; compare its actual claims with ready sources rather than repeat signature-wide discovery.
SCOPE: Exactly TARGET over Z_2 using L095, L100, foundations/17-local-power-hensel-inputs.md and existing two-lifts evidence; elementary exact arithmetic, valuations, polynomial identities and the cited Hensel criterion only.

## Review completed and primary input

This answers the saved coverage-review request. TARGET now names the
separate approved audit; that audit has not been performed here.

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, 29 June 2022,
[author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
Lemma 2.3 and Theorem 2.4, printed p.4, were reopened on 2026-10-19.
The theorem requires an integral polynomial and integral seed, vanishing
modulo p^n, with one derivative of valuation k and 0<=2k<n. It gives
an exact root congruent modulo p^(n-k). Its proof repeatedly applies
the one-variable lemma with other coordinates fixed; the lemma retains
the derivative valuation. Neither statement excludes p=2. Import this
result by citation; no reproof is needed.

L100 claims two one-variable applications with p=2, n=5, k=0 after
fixing m=u=1 and C. Those claimed hypotheses remain audit obligations.
Clark's Newton theorem is reusable background, not an essential further
input. No square-root or fourth-root surjectivity is needed. Uniqueness
is a separate elementary polynomial-factor argument in L100 and must
be checked, rather than attributed to Zabradi's existence statement.

## Dependency and evidence comparison

Audited L095 supplies full Q,H and identity (4). Evaluating that
integral identity over Z_2 requires no positive-integer converse or
additional Putz theorem. In I retain N=C and its defining C equation;
in II retain N=5C, both occurrences of 5^11, and its defining C equation.
The same fixed C and B must survive lifting a. Audit the cancellation,
not just each equation separately. L093 is upstream context, not an
additional source needed for these local identities. No global rational
root, algebra classification or integer solution is claimed.

Read the full original generator
`scripts/rational-factor/check_two_lifts.py` without execution.
The inspector preview of `/lift_records` in
`scripts/rational-factor/two-lifts-certificate.json` locates two full
26-field seed records: coefficients, errors, derivatives, valuations,
scales, shared coordinates, identity sides and reconstructed residuals.
The generator also identifies both complete residue lists under
`/residue_domains`. This is an evidence inventory only; no preview or
stored pass flag establishes arithmetic correctness in this review.

The later audit must independently reconstruct all H coefficients used,
exact errors and derivatives (including the full system-II error),
modulo-64 valuation certificates, strict actual/required bounds and
both original-equation reconstructions. Check the stated disk roots,
uniqueness, nonzero m,u,a,A,B,C, auxiliary primitivity, odd A,B and
v_2(C)=1. Positivity and coprimality at other primes are outside scope.
If retaining the ancillary full-domain claims, replay both entire
768-triple lists and their full primitive-pair domains, including zero
coordinate residues, and compare all records, counts and failures.
Finite residues support the arithmetic but do not prove exact existence.
No mathematical generator was run or mathematical script written here.

## Duplicate/failure check and relevance

The realization assessment already records exact equation, coefficient,
rational-factor and two-adic searches and primary Putz scope. Reuse it:
the target systems and source hypotheses are unchanged. Putz's necessary
algebra list does not decide these witnesses and is not an input to
L100's construction. L095's independent audit and its working record
were inspected; they secure the identity, not this new specialization.
History 339 and ATTEMPTS/047 expressly leave L100's audit pending.
L096 and L099 concern different primes and do not duplicate this audit.
Preserve the distinct stops ATTEMPTS/043,045,046,047; none is reopened.

The main gap remains zero positive primitive integer solutions of both
L095 systems within ordered (3,5,11), with other algebra types and Beal
signatures independently open. The intermediate target is reliability
of L100's local existence claims. A successful audit secures retirement
of standalone two-adic exclusion and supports directing later work to
global compatibility; it does not advance beyond the checked general
lifting methods or supply integer elimination.

Coverage test met: all essential methods are covered. Approve one
separate bounded audit. Continue only if both complete specializations,
strict hypotheses, uniqueness and primitive reconstructions survive
independent checking. A failed constant, scale, bound or logical step
requires isolating and repairing or qualifying the affected claim;
it does not imply global exclusion. Do not expand the prime, precision
or local-classification target. Integer lifting and cross-prime
compatibility remain unresolved even on a pass. Mathlib coverage of
the full systems and supporting declarations remains not checked.
