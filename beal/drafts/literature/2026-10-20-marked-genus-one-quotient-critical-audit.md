# Critical-audit coverage for the marked genus-one quotient

TARGET: Critically audit L111's marked twist, degree-two genus-one quotient, rational origin and normalized lifting interface.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target construction search in 2026-10-20-marked-pair-genus-one-quotient.md; compared L111 in full, L110's model and completed audit passages, L109's normalized lifting proof, history/385 and ATTEMPTS/050; checked Stacks curve-map, finiteness, genus and elliptic-definition sources against the audit obligations.
SOURCE_EVIDENCE: Reused inspected Bruin arXiv:math/0408069v2 Section 2.2 pp.4–5 and Docking arXiv:2108.09564v2 Section 2/Table 1 Case II p.4; directly read Stacks 53.2.6/0BY1 statement and extension proof, 53.2.4 in 0BXX with its finite-fiber proof, 53.12/0C1B characteristic-zero ramification discussion and Lemmas 53.12.1–4, and 105.2/072J definition.
COMPARISON: The known split-cover projections and standard smooth-curve theorems cover the audit method; they do not certify this instance's square multiplier, inverse fields, component, degree, proper charts, origin or rational fibers. No new general theorem or Prym reproof is required.
GAP: Independent verification of every essential L111 instance claim and complete relevant arithmetic evidence remains unperformed; rational-point completeness and integer exclusion are outside this audit.
REASON: Essential source coverage is now adequate for the unchanged audit target; source readiness permits a separate research audit but is not a passing audit or a new mathematical result.
LITERATURE_REASON: The nominated audit was REVIEW_REQUIRED; this turn approves its exact scope using reusable construction coverage and explicit primary support for the proper-map finiteness and ramification obligations.
SCOPE: Exactly TARGET over Q with audited L109/L110, their exact original s,z and L111's saved producer/certificate; includes independent arithmetic replay and smooth proper finite/infinity charts, but excludes point enumeration, ranks, other twists, degree-nine recovery and integer elimination.

## Gap, use and bounded decision

The main gap is residual positive primitive integer exclusion, here in the
rational-factor branch of ordered (3,5,11). The intermediate target is a
critical verification of L111, not another quotient construction. A reliable
genus-one necessary image could support later rational-point methods while
retaining the marked lifting condition. Neither that use nor an elliptic
origin supplies integer exclusion.

Continue this construction only if the independent audit verifies the exact
marked Q-form, both field compositions, geometric component, degree two,
genus one, proper charts, rational origin and full lifting interface. If a
claim fails, record its specific failure and repair or park that construction;
a source-level analogy or a passing producer report cannot substitute for
the check. No audit is performed in this literature-only step.

## Source comparison and applicability

Reuse the detailed construction assessment
`2026-10-20-marked-pair-genus-one-quotient.md`, including its actual queries,
source versions, theorem passages and distinction between inspected results
and unread leads. Its exact-polynomial and standard-terminology searches
remain applicable: this audit changes no curve, marking or hypotheses.
No repeated broad search is needed and no originality is inferred.

Bruin, *The arithmetic of Prym varieties in genus 3*, Compositio Math.
144 (2008), 317–338, DOI 10.1112/S0010437X07003314,
[arXiv:math/0408069v2](https://arxiv.org/pdf/math/0408069v2), Section 2.2,
pp.4–5, construction before Proposition 2.2 and its proof, supplies the
split even-factor cover and actual projections. Docking, *2-infinity-Selmer
rank parities via the Prym construction*, J. Number Theory 265 (2024),
208–225, DOI 10.1016/j.jnt.2024.06.009,
[arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2), Section 2 and
Table 1 Case II, p.4, explicitly treats the genus-two quadratic–quartic
case and leaves a constant-twist ambiguity. Those inspected passages are
reused, not freshly retrieved. Neither chooses the present marked twist.
The genus-three-base theorem and rank-parity conclusions are unnecessary.

Direct primary retrieval on 2026-10-21:

- [Stacks Theorem 53.2.6, 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
  statement and proof: field maps in transcendence degree one correspond
  to nonconstant maps of normal proper curves; the proof extends across
  the nonsingular source. The audit must first establish the correct
  field inclusion and inverse identifications over Q.
- [Stacks Lemma 53.2.4, Section 53.2](https://stacks.math.columbia.edu/tag/0BXX):
  a map from a proper scheme of dimension at most one to a separated
  target is finite if every one-dimensional component has nonconstant
  image. Its proof uses properness and finite fibers. Audit smoothness,
  properness, integrality and nonconstancy before applying it; an affine
  formula or an alleged involution alone does not establish finiteness.
- [Stacks Section 53.12, 0C1B](https://stacks.math.columbia.edu/tag/0C1B):
  Riemann–Hurwitz requires smooth proper curves, the stated constant-field
  condition and a finite separable function-field extension. In
  characteristic zero the ramification contribution uses e−1 with residue
  degrees; after geometric base change count every branch, including
  infinity. Lemma 53.12.1 identifies the generic etaleness hypothesis.
- [Stacks Section 105.2, 072J](https://stacks.math.columbia.edu/tag/072J):
  the elliptic definition requires smooth proper genus-one fibers and a
  section. Over Q a verified rational smooth point supplies the section;
  no assertion about generators, rank or rational-point completeness follows.

L109's already audited local-normalization proof supplies the even-order
unit-residue interface for D -> B. It is an established input here, not
an inference from the distinct map D -> E. Exact chart calculations are
necessary specialization checks because no cited theorem supplies the
present coefficients or boundary residues. Reproving the general Prym,
Riemann–Hurwitz or curve-extension theorems is neither required nor useful.

## Independent audit specification

Inputs are L109, L110, L111, `scripts/pair-genus-two/marked_quotient.py`
and its complete `marked-quotient-certificate.json`. L110's completed
audit is canonical despite older pending language in the overview.
Read all load-bearing certificate values rather than relying on a preview
or its reported check count. Independent arithmetic must not merely reuse
the producer's arithmetic classes; preserve its original evidence.

Check the existing claimed square multiplier against L110's exact v²=z,
both inverse field compositions, nonzero denominators as functions and
transport of original s. Verify independent square classes over Qbar(T)
before assigning a geometric component or quotient degree. Distinguish
the involution fixing R from the marked deck involution over B.
Check smooth finite and infinity charts, their gluing and proper coverage,
and the separability and branch counts needed for genus. Independently
check the proposed origin and every boundary value used to exclude rational
infinity or T=−2 points. Check ramified fibers scheme-theoretically, not by
two-sign counting when h=0. Compare the claimed normalized boundary residue
with L110 and retain all zeros/poles of the affine multipliers through
proper models. Any repaired result needs its full canonical proof and
qualifications; structural or arithmetic replay alone is not proof.

## Duplicates, failures and limits

L111 is the existing construction to verify, not a new lemma to duplicate.
History/385 records its reported arithmetic success and corrected Python
coercion failure. That repaired implementation failure is not a failed
twist or a mathematical obstruction. ATTEMPTS/050 exhausted a bounded
Jacobian rank detector; this audit does not enlarge its caps or reopen it.
L108's unfinished boundary decomposition and all backend, direct-scaling
and standalone-local stops remain preserved.

Unresolved assumptions after coverage approval: L111's independent validity;
E(Q) completeness; lifting marked points through the degree-nine incidence
map to recover a rational distinguished root; compatible remaining factors;
both L095 simultaneous integer systems; and the minus-eleven alternative.
No cross-notebook input is used. Full matching and supporting Mathlib
coverage were not checked; no absence or formal verification is claimed.
