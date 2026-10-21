# Conductor-36 structural instance audit — coverage approved

TARGET: Critically audit L038's saved N=36, P-empty relative presentation and reflection certificate, including full coset coverage, integral saturation, generator coordinates and every oriented path.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: BSD-187 reused the ready N=1,15 executable audit and N=36 production assessments; searched their exact scopes, L038/L029 and history/175,176,185,186 for this instance and prior audits; inspected the changed N/P domain and relevant producer/checker branches. No duplicate completed N=36 structural audit was found in these records; no novelty is inferred.
SOURCE_EVIDENCE: Reopened Stein online v0.1 Propositions 3.10--3.11 (both path proof cases), Theorem 3.13 (statement and both relation cases), equations (11)--(12)/Remark 1.43, and Cremona corrected second edition Propositions 2.2.1--2.2.2 pp.15--16 with coset proof; reused the prior inspected Sergeraert v1 normal-form coverage and audited L038 coordinate algebra. Precise citations and qualifications below.
COMPARISON: Known sources cover positive composite N, full relative integral symbols modulo all torsion, signed/infinite paths and geometric reflection. Unchanged builder/checker hashes and their empty-P branches preserve the prior witness contract; existing N=36 production replay is the object to audit, not a completed critical audit or proof of universal software correctness.
GAP: Separately inspect and replay the entire N=36 certificate/checker contract and add an independent identity or targeted evidence rejection; no theorem citation alone verifies its saved finite entries.
REASON: This comparison removes the essential source-scope gate for one fixed structural audit that can support a later full normalized generator table, without addressing arbitrary-curve rank equality.
LITERATURE_REASON: Newly proposed N=36/P-empty critical-audit object lies outside the ready N=1,15/P={2} instance scope; source-to-contract comparison was essential before execution.
SCOPE: Only saved L038-relative-v1 N=36/P=[] presentation and geometric J, weight two/trivial character; complete cosets, all relations and torsion saturation, all integral coordinates and base/reflection paths. No Hecke operator, eigenline, analytic computation, generator-table recovery or universal software theorem.

## Sources and applicability

Reuse `drafts/literature/2026-10-10-general-relative-implementation-critical-audit.md`
and `drafts/literature/2026-10-12-conductor36-full-generator-recovery.md`.
The former approved a different finite instance audit; the latter approved
production of this domain but did not critically audit it. BSD-186's
REVIEW_REQUIRED proposal correctly left this source comparison pending.
This approval supersedes that gate only; earlier completed work stands.

[Stein, Modular Forms, a Computational Approach, GSM 79 (2007)](https://wstein.org/books/modform/stein-modform.pdf),
equation (3.2.1), p.40, Propositions 3.10--3.11, pp.42--43, and
Theorem 3.13, p.44, are precise presentation/path imports. Reopened
[online v0.1 weight-two chapter](https://wstein.org/books/modform/modform/weight_two.html)
on 2026-10-12: positive N, primitive pairs modulo units, integral path
generation, both Manin relation types and removal of all torsion.
The path proofs include formal infinity convergents and denominator zero.
The presentation proof verifies both relation types and cites Manin
Section 1.7 for injectivity. Import the stated theorem; that original
proof remains unread and no topological reproof is claimed. N=36 is
within the stated domain, without squarefree or non-CM restrictions.

[Cremona, Algorithms for Modular Elliptic Curves, corrected second edition
(1997), Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Propositions 2.2.1--2.2.2, pp.15--16, give the unit-orbit/right-coset
criterion and coprime lifts at general N. Reopened the full coset
criterion proof and lift statement, including endpoint order
{b/d,a/c}. Composite-level enumeration must retain every primitive pair,
not just a field-projective list. No absolute-homology restriction from
Cremona's surrounding discussion is used to replace Stein's relative module.

[Stein online v0.1 General Modular Symbols](https://wstein.org/books/modform/modform/modular_symbols.html),
equations (11)--(12), Remark 1.43, require normalization by diag(-1,1)
and display the convention sign. Gamma_0(N) satisfies that hypothesis;
L029 already identifies geometric J as negative star at weight two.
Endpoints retain order. J squared equal to identity cannot establish
that sign or identify the correct endpoint action by itself.

Reuse [Sergeraert, About the Kannan--Bachem algorithm,
arXiv:2411.02422v1, 4 November 2024](https://arxiv.org/html/2411.02422v1),
Sections 2,3.1,4,6--7 and Theorem 1, as actually inspected in the ready
2026-10-10 assessment. Rectangular, arbitrary-rank diagonal equivalence
with unimodular witnesses suffices; divisibility-ordered pivots are not
required. Coefficient growth gives no practical runtime bound. No new
normal-form theorem or proof is needed. L038's existing coordinate and
saturation argument is reused, not rederived. Original Kannan--Bachem
and Manin proofs remain unread leads, not additional essential premises.
Mathlib full matching/support coverage remains not checked.

## Exact finite audit contract

Essential mathematical inputs are L038's general construction/coordinate
proof and saved instance, and L029's orientation convention. L037 is a
downstream use only; L049--L055 supply no structural premises. No
cross-notebook input. The exact executable objects are
`scripts/conductor36-table/presentation.json`, its
`presentation_verification.json`, and
`scripts/general-relative/build_certificate.py` / `verify_certificate.py`.
Both programs import only standard-library helpers, not each other.

Read the producer's domain/coset/operator branches and verifier's domain,
saturation and full operator branches for scope comparison. P=[] leaves
exactly J; it removes all Hecke paths/commutation tests without removing
base paths, reflection paths or saturated descent. The programs' SHA-256
values match the prior complete code reading: producer
`414dee8b0124fa708e22a6f1cf609bfb961f7281929bc267e167614a98890f85`,
verifier `3829bd972ac9d213aea5e983580aa0f801f4b0dbd8564c95e0410de856ae4596`.
Certificate hash is
`aaeb1c9f4e25bfd62aa17e7719e6142c087f801033f7fb4ee2a7431dc298a5e4`;
saved report hash is
`6408d132cb0c799d9c8bb51307e7dc6e6051f2e14cffbf5cc368c8390a963039`.
These identify retained objects, not verification outcomes.

Selected complete /inputs, /summary, /required and /failures values were
read with the prescribed inspector. The report describes 864 assignments,
72 cosets, 144 relations, 216 relation lookups, (s,r,d)=(72,59,13),
torsion order one, 287 row/172 column operations and their inverses,
144 paths, 144 source images, 59 saturated images and 72 generator
reconstructions. L038 records 626 segments. These remain production
claims requiring full replay; no preview or empty failure list verifies
arithmetic. Unit pivots do not test general nontrivial torsion removal.

The next audit must check all primitive-pair/unit partitions and SL2
lifts before comparisons; every S/R3 relation including multiplicities;
strict integral types, matrix shapes, full UAW=D, zero tail and both
inverse products/log orders; K,Q,Pi,head and integral decomposition;
every generator coordinate; every reduced signed/infinite endpoint,
determinant-one segment, Gamma_0 lookup, adjacency and telescoping;
and complete J endpoint identification, raw sums, source/saturated
annihilation and B=YQ, BPi=Y. Require complete evidence inspection/replay,
plus a discriminating independently reconstructed identity or targeted
corruption rejection, with original bytes preserved. Supplementary
involution alone is insufficient. No critical audit was executed here.

## Relevance, failures and decision

Main gap: rank E(Q)=m(E) for arbitrary analytic order at least two.
Intermediate target: this independently testable finite structural audit.
Plausible use: remove the supplied-domain qualification for a later
full conductor-36 normalized generator table. Continue only on complete
zero-failure coverage/replay and the discriminating check; repair or
narrow the structural claim on failure rather than relying downstream
on it. Source approval is local known-method progress, not a new result
beyond checked sources and not a BSD candidate.

Scoped history/175--176 and 185--186 distinguishes production and geometry
review from this pending structural audit. ATTEMPTS/026's direct workload
stop and ATTEMPTS/028's dyadic cutoff stop concern analytic schedules,
not finite structural validity; preserve both and ATTEMPTS/025--027.
The full normalized table, sums, signed division and isolation remain
unfinished. CM still excludes L027; uniform coefficients, rational
membership, Sha and complex-order comparison remain open.
