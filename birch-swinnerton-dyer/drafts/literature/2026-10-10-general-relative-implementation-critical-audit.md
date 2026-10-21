# Executable relative evidence — critical-audit coverage approved

TARGET: Critically audit L038's parameterized N=1 and N=15 reflection/T_2 certificates and independent checker against the complete relative-lattice/operator contract.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready construction and implementation assessments; read all three general-relative programs, scoped history/109--111 and ATTEMPTS/022--024. Reopened Stein's exact online presentation/path/Hecke and reflection passages for the new code-to-contract comparison; no broad novelty search or new audit execution.
SOURCE_EVIDENCE: Stein 2007 equation (3.2.1), Propositions 3.10--3.11, Theorem 3.13 and Section 3.4.1, plus online v0.1 equations (11)--(12)/Remark 1.43; retained Cremona corrected second edition Propositions 2.2.1--2.2.2 pp.15--16 and Sergeraert arXiv:2411.02422v1 Sections 2,3.1,4,6--7/Theorem 1. The source-to-check comparison and URLs are below; prior SageMath 10.8 coverage is optional, not an executable dependency.
COMPARISON: Known theorem domains and audited L038 cover both structural levels and the full geometric operators. The actual builder uses custom reversible diagonal equivalence and the independent checker reconstructs finite domains and geometry; its correctness and the full artifacts still require a separate audit, not a citation-only import.
GAP: Perform the full instance/checker audit, including completeness before comparisons, strict types, inverse ordering, empty shapes, path identification and saturated descent; coverage approval and existing report summaries do not verify this evidence anew or prove universal software soundness.
REASON: The new executable evidence was outside the completed construction audit; this comparison now approves one bounded SPECIALIZE/REPRODUCTION audit without reopening unchanged source blockers or rejecting completed production.
LITERATURE_REASON: Changed executable object: newly produced general-relative programs and certificates require source-to-implementation scope comparison before their first separate critical audit.
SCOPE: N=1 and N=15, weight two, trivial character, P={2}; inspect the complete retained evidence and independent checker, with specific repairs to those instance checks if needed. No new levels, general software termination/soundness theorem, arithmetic eigenvalues, eigenline, cutoff, runtime bound or BSD assertion.

The completed startup action was: Assess essential source and implementation
coverage for a critical audit of L038's parameterized N=1 and N=15
reflection/T_2 certificates. The TARGET above is the now-approved next
research action; this literature-only turn did not execute it. Reused the
preexisting assessments in
`drafts/literature/2026-10-09-general-relative-certificate-implementation.md`
and `drafts/literature/2026-10-08-general-relative-construction-critical-audit.md`.
The original REVIEW_REQUIRED draft correctly withheld approval when these
programs had not been compared with the source contract. That pending
decision is superseded by this dated comparison; the completed production
and its pending audit remain intact. No new mathematics was derived.

Essential inputs: canonical L038 (including the new executed-specialization
section), L029's column and reflection conventions, and precisely the
three scripts and two full certificates/reports under
`scripts/general-relative/`. L037 is only the downstream line-termination
use; no elliptic eigenvalues or dimension-one kernel are part of this test.
The old fixed-level code is a comparison, not an input. Independent
arithmetic supply, q, normalized denominators/coefficient production,
rational membership, divisible Sha and complex-order comparison remain
open. No cross-notebook input is requested. Mathlib coverage remains not
checked. No critical-audit success is claimed by this assessment.

## Exact source domains and reuse

[Stein, *Modular Forms, a Computational Approach*, GSM 79, AMS, 2007](https://wstein.org/books/modform/stein-modform.pdf),
equation (3.2.1), p.40; Propositions 3.10--3.11, pp.42--43;
Theorem 3.13, p.44; Section 3.4.1, pp.47--48, are the retained imports.
Reopened the [online v0.1 weight-two chapter](https://wstein.org/books/modform/modform/weight_two.html)
at Propositions 3.10--3.11 (both path-reduction proofs), Theorem 3.13
and the good-prime endpoint formula. Positive N includes both specified
levels. The presentation imposes all two/three-term relations and removes
torsion. The first path proof includes formal infinity convergents;
the second treats denominator zero. The operator requires a prime not
dividing N and the entire prime-plus-one sum. Theorem 3.13's omitted
injectivity proof is still an unread Manin lead, not an extra premise:
import the stated theorem without claiming a topological reproof.

Reopened [Stein online v0.1, General Modular Symbols](https://wstein.org/books/modform/modform/modular_symbols.html),
equations (11)--(12) and Remark 1.43, under normalization by diag(-1,1).
L029 already specializes this at weight two to geometric reflection,
the negative of Stein's star. The checker must identify the endpoint map
and preserve orientation; an involution identity alone does not do so.
No sign theorem is reproved in this source review.

Reused the previously inspected [Cremona, corrected second edition,
Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Propositions 2.2.1--2.2.2, pp.15--16, for primitive-pair unit orbits,
coprime lifts and Gamma_0(N) equivalence at composite levels. Reused
[Sergeraert, arXiv:2411.02422v1, 4 November 2024](https://arxiv.org/html/2411.02422v1),
Sections 2,3.1,4,6--7 and Theorem 1, including rectangular/zero-tail
cases and its proof, for finite integer diagonalization with unimodular
witnesses. Divisibility-ordered Smith form is not required by L038.
The coefficient-growth qualification remains; no practical bound follows.
Original Kannan--Bachem remains unread and unnecessary here.

The SageMath 10.8 P1List and transformation-output smith_form manuals
remain inspected implementation alternatives in the prior assessment.
The current code imports neither Sage nor a normal-form library. Their
availability, version behavior and internal correctness are therefore
not new essential coverage gaps. L038's audited coordinate algebra is
reused; the custom log and witness implementation still needs review.
Precise named imports suffice; redoing their theorem proofs would not
address the executable gap. Mathlib full matching/support coverage remains
not checked, which is not evidence of absence.

## Source-to-check obligations for the next audit

Read the three programs completely for coverage comparison; this does
not certify their soundness. The following maps the existing contract
to the actual code and states what the later audit must adjudicate.

| Contract and input | Executable location | Later audit obligation |
| --- | --- | --- |
| Complete cosets/lifts, Cremona and L038 | builder `build/lift`; checker `replay/lookup` | Independent primitive-pair/unit partition, list lengths before zip, every SL2 lift and Gamma_0 lookup; explicit level-one identity branch. |
| Complete Manin relations, Stein Theorem 3.13 | `relation_convention`, `actions`, `A` | All 2s rows and 3s lookups, exact right-action S/R3 convention, every repeated-index multiplicity. |
| Unimodular equivalence, Sergeraert and L038 | builder `diagonalize`; checker `elementary`, unimodular replay | Strict integer types, operation arity/bounds, signs and transpose conventions, grouping and inverse order, full UAW=D and both inverse products, all pivots/zero tail. |
| Integral saturation/coordinates, audited L038 | checker integral saturation, shape-tagged `M` | Exact K,Q,Pi,head, complete integral decomposition and every generator coordinate; d=0 shapes must survive transpose and multiplication. |
| Oriented path identification, Stein Proposition 3.11/L038 | builder `chain/path`; checker `chain/path/lookup` | Every reduced signed/infinite endpoint, determinant-one segment, start/end orientation, adjacency and telescoping, raw sums and full original paths; do not trust a shared continued-fraction algorithm. |
| Full geometric J and good-prime T2, L029/Stein | endpoint maps and checker entire operator loop | Exact complete maps and all three T2 paths for each generator; full Z,Y, every source/saturated image, B=YQ and BPi=Y. |

The checker has its own shaped matrix operations and elementary-matrix
replay and imports no builder. Independence of code does not eliminate
a shared mathematical mistake; the contract/source comparison and full
evidence review are essential. Supplementary commutation/involution and
eight existing mutations cannot replace that review. Inspect the complete
rejection evidence where used; its bounded preview was only orientation.

The metadata inspected through the prescribed JSON inspector records
(s,r,d)=(1,1,0) and (24,19,5), removed torsion order one, respectively
5/120 paths and 6/501 segments, matching recorded actual/required counts,
and empty failure lists. Direct certificate hashes match report hashes.
These checks identify the objects and report domains only; neither full
certificate arithmetic nor checker correctness was reverified here.
Both retained instances have unit pivots, so they do not exercise
nontrivial torsion removal; neither covers r=0. This limits general
software claims, not source coverage for these two specified instances.

The source-notes artifact records code/certificate hashes for the later
audit. Require full inspection/replay of load-bearing evidence rather than
infer correctness from displayed operators, counts or empty failures.
Audit failures require a precise repair and complete affected replay before
downstream use. A missing essential theorem domain requires REVIEW_REQUIRED
coverage rather than expanding the mathematical target in the audit turn.

## Relevance and decision

The main gap remains rank E(Q)=m(E) for arbitrary m(E)>=2. This approval
is local source-to-implementation progress, not progress beyond the checked
known algorithms. The independently testable intermediate target is the
first critical audit of actual finite structural certificates, potentially
supporting L037/L029 line production independently of q. Continue only if
the full evidence meets every contract obligation after any specific repair;
abandon downstream reliance on an instance if its geometry or descent fails
without repair. Repeated failure requires reassessing the mechanism.
ATTEMPTS/022--024 bar repeating conditional audits as production, not this
first audit of new produced evidence. Persistent twist-source blockers stay
parked. The remaining independent arithmetic/BSD assumptions listed above
are unchanged. STATUS remains IN_PROGRESS; no candidate exists.
