# Growing-support arithmetic source alignment — completed review1135

TARGET: Assess whether the actual arithmetic core sources admit a growing-support bound for det(B* M_0^{-1} B) that avoids an assumed uniform spectral floor.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1135 reused1130/1131/1132 and466, searched exact source-Gram/growing/core-determinant and nested-core/pivot-residual terms, and checked active-notebook source/Gram failures. Inspected the primary statements and proof cases below; no adequate growing-support inverse-core bound was located. Failed searches are not evidence of novelty or impossibility.
SOURCE_EVIDENCE: bramble_trace paper162/v1(15November2026), Section2(8)-(13), Lemma1/proof, (17)-(23),(26)-(32), Section7; paper143/v1(10November2026), Theorems1/9, (8)-(11), Sections3-8 proof cases and(43)-(49); paper144/v1 Theorem1/(1)-(4), with1130 for its finite consumer proof; Schubr27October2026 Theorem1.1 and Section2(4)-(6); Gallier24August2019 Section1 p2 and Proposition2.2 p4. Exact primary links and inspection qualifications below.
COMPARISON: Paper143 controls C_N* D^(-2alpha) C_N and leaves beta_J in(46) unpaid; it does not bound the distinct inverse-core matrix B* M_0^(-1) B. Paper144 assumes the entire postcore remainder bounded. Paper162's fixed certificate and generic counterexample supply neither the desired arithmetic growth bound nor its refutation. The theta reference concerns another operator and sources.
GAP: No actual-arithmetic estimate for the growing two-source area was obtained. A specific nested-core residual suppression conjecture is nominated separately, without proving it; positive cores, a base-area bound, both sectors, complete middle/residual budgets and actual-Xi realization remain independent gaps.
REASON: Complete the missing source comparison, park a generic displacement-only inference and nominate one falsifiable arithmetic residual test. This is bounded literature EXPLORATION, not a new bound, an import into the main proof or a mathematical negative result.
SCOPE: Completed literature-only comparison of the exact TARGET. No lemma/script writes, new identities, numerical tests, certificate replays or all-support theorem. The separate nomination1135 is newly written and requires next-turn approval.
LITERATURE_REASON: Varying support/core size lies outside the reused fixed-window scope; review1135 inspected the previously unread paper143 proof cases and exact inverse-core comparison. The older466 statement-level warning was reused, not counted as a new result.

## Completed comparison1135

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The intermediate question was an explicit growing-support bound for
the actual inverse-core two-source area, potentially reducing the
distant-covariance cost. The continuation test required an arithmetic
inequality rather than a uniform spectral floor or a generic positive
displacement estimate. No such established inequality was found.
That is an unanswered bounded search, not a proof that it cannot exist.

### Exact scope and strongest inspected conclusions

Primary sources are linked at their accessible displayed versions;
the supplied /v1 routes failed in the web reader. The unversioned
rStation pages explicitly display v1 and the dates recorded above.

* [bramble_trace, paper162/v1](https://rstation.ai/problems/riemann_hypothesis/papers/162),
  Section2(8)-(13), fixes the actual parity-dependent sources and
  exceptional even zero mode. Lemma1 assumes a real positive core
  and its displacement identity. Its Schur-triangular proof bounds
  the label similarity by R=lambda_*+sqrt(det G); (17)-(18) then
  price omitted moments. The complete covariance consumer(23) still
  uses individual Gram entries. Sections5-6 pay the middle and all
  omitted columns only at the certified endpoint. Section7's positive
  two-by-two family has det G=c^2/(1-c^2), unbounded as c approaches1.
  This excludes a displacement-only bound, not an arithmetic estimate.
  The actual finite certificate and its source solves cannot be
  extrapolated to varying support. Supplement regeneration remains
  uninspected; rounded source values were not used as certificates.

* [bramble_trace, paper143/v1](https://rstation.ai/problems/riemann_hypothesis/papers/143),
  Theorem1, uses prime endpoints, the even source, common rational
  degree d and pole gap kappa for every linear combination, with
  N>=P^(3+eta)d^6/(1-kappa)^3. Theorem9 additionally requires
  2b_alpha<1, d_BV>0, h<1 and e_alpha<1. Its(43)-(45) compares
  the full distant coupling Gram with an integral Gram. Its proof
  preserves mixed directions and nullspaces; it gives no inverse-core
  denominator. Equations(46)-(47) retain the core-dependent beta_J
  without a growing-core bound. Inspected the masked-packet case,
  cutoff-jump/variation proof, complete digamma remainder transfer,
  mixed-Gram proof and prime-power product/ratio cases. None controls
  det(B* M_0^(-1) B). The entire adjacent middle space is excluded
  by the degree/pole conditions.

* [bramble_trace, paper144/v1](https://rstation.ai/problems/riemann_hypothesis/papers/144),
  Theorem1(1)-(4), retains log(d^2/(1-kappa))=o(sqrt P), the
  exponential cutoff N=ceil(exp(gamma sqrt P)), gamma>1, and a
  bounded complete remainder. The sentence following(4) expressly
  includes every postcore covariance in that assumption. Reused1130's
  finite consumer/proof inspection; this theorem does not pay a
  growing nearly singular core by itself.

* [Scott Schubr, *Source-Resolved Resolvent Growth under Reciprocal-Theta
  Confinement*, edition1,27October2026](https://research.luminaryoddities.org/source-resolved-resolvent-growth-reciprocal-theta-confinement/v/1/files/main.pdf),
  Theorem1.1, pp1-2, and Section2(4)-(6), p3, concerns prescribed
  theta-derivative rows and the inverse of a positive constrained
  archimedean operator plus epsilon I. Its degree-dependent two-sided
  bounds are not bounds for a complete finite arithmetic core.
  No source identification or operator comparison to M_0 is supplied
  here. Only these essential hypotheses were inspected; its later
  analytic proof was not needed to reject a direct import.

### Reuse, duplicate checks and new nomination

Assessment466 already inspected paper143's statements and Theorem9
proof for a different, physically penalized five-cell problem. Its
warning about the unpaid core parameter is reused, not rediscovered.
The actual two-generator inverse-area target differs from that
penalized coupling map. Reused1130/1131/1132 for the fixed-window
overlap and closure comparisons; C750f's audited import is unchanged.
C750c(1)-(4) rejects scalar-floor payment, not exact inverse geometry.
Its U12 diagnostic remains inconclusive. No historical stop is treated
as a ban on an actual arithmetic residual estimate.

Bounded local searches used exact paper143/paper162/source-Gram terms
in active assessments, relevant five-cell comparisons and November16
attempts, followed by their needed passages. A notebook-local search
for nested-core/pivot-residual/source-residual-adjugate terms found no
matching target. No sibling notebook or cross-notebook input was read.

External queries included `"Weil" "source-Gram" growing support determinant`,
`"Source-Gram" "growing"`, `"Weil" "source alignment" inverse core`,
`"Weil" "pivot" "source" "residual" Gram`, and
`"Weil" "nested" "core" "Gram"`. Unrelated returned claims were
not used; search snippets establish no theorem. Mathlib full matching
coverage remains unchecked, rather than absent.

The selected follow-up is the arithmetic pivot-area test in
[nomination1135](2026-11-16-arithmetic-pivot-area-test-1135.md).
It fixes a support family, nested cores, a trial inequality and a
small falsification pilot. It keeps the pivot in the comparison
instead of replacing it by a global eigenvalue floor. Its proposed
polynomial envelope has no supporting theorem or numerical evidence
yet; failure is an allowed informative outcome. The block-inverse
method is known, and no reproof of that method is an advance.

The primary algebraic resource inspected for that nomination is
[Jean Gallier, *The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*,24August2019](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
Section1, printed p2's inverse formula, and Proposition2.2, p4.
The latter requires the leading block invertible and identifies
positive definiteness with positive leading block and Schur complement.
It supplies no arithmetic residual suppression. A future attempt
must cite the block formula, verify the exact source specialization,
and write any elementary determinant expansion it needs. Neither is
derived or applied in this literature turn.

Outcome: EXPLORATION, LITERATURE/NOVELTY_UNCHECKED. No bound or new
mathematics beyond the sources checked; no mathematical exploration
usage or budget reset. The new EXPLORE continuation receives separate
approval before mathematical invocation. PROOF and DAG do not change.

## Original nomination1134 (historical scope; completed above)

The main gap remains actual-Xi all-degree positivity L030-L032/C032a.
The proposed intermediate resource is control of the two actual source
vectors together in the inverse metric of a finite positive Weil core.
An explicit growth estimate could reduce the distant-covariance cost
as support grows. It would not pay the other Schur block or prove RH.

Use exactly paper162's M_0, B=(u,v), label matrix and parity conventions,
not arbitrary displacement matrices or physical endpoint traces. Write
G=B* M_0^{-1}B and retain the source's condition M_0>0 as an unresolved
input whenever it has not independently been certified. The candidate
asks for an arithmetic estimate of det G, with explicit support/core
dependence, that does not simply insert an unknown uniform lower bound
for M_0. No such estimate is asserted or derived by this nomination.

The source's resolvent scale is lambda_*+sqrt(det G). A useful eventual
mathematical test must compare a proposed bound with the first retained
distant label, with a proved positive margin, and retain the complete
covariance and residual. The literature step must specify the support
family, core/truncation rule and actual inequality before approving any
research; choosing a larger cutoff without paying the remaining blocks
is not a new mechanism. A conditional intermediate estimate may be
useful while finite-core positivity and the middle comparison stay open.

Continue only if the inspected sources and failures leave a concrete,
independently testable arithmetic cancellation or source-alignment
claim. Stop this nomination if it reduces to a generic positive-matrix
bound, an assumed full sign, an unchanged scalar-floor loss or a result
already proved at the proposed scope. If no such claim survives, record
that evidence and select a different central-gap mechanism rather than
repeat this review. Do not infer novelty from unsuccessful searches.

Essential local context: C750f's audited fixed-domain import; C750c's
scalar-floor rejection and exact neutral complement; L744's complete
form. Reuse assessments1130/1131/1132 before loading further local proofs.
The paper162 Section7 obstruction must be compared explicitly with the
actual arithmetic hypothesis; it is not a ban on a genuinely different
paid estimate. Paper143's exact relevant theorem/proof cases and any
essential paper144 hypotheses require inspection before dependent work.
No cross-notebook input is proposed. Mathlib coverage is unchecked.

Primary leads: [paper162/v1](https://rstation.ai/problems/riemann_hypothesis/papers/162/v1),
[paper143/v1](https://rstation.ai/problems/riemann_hypothesis/papers/143/v1),
and [paper144/v1](https://rstation.ai/problems/riemann_hypothesis/papers/144/v1).
These links do not upgrade an unread lead to inspected coverage.

This is a source-gated discovery nomination, not a creative proof attempt.
A later creative route is justified only after an exact mechanism and
bounded discriminating test are covered; no new lemma is approved here.
