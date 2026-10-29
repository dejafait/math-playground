# L461 witness-cutoff critical audit: source-scope assessment

TARGET: Critically audit L461's conditional c>3/16 negative-witness cutoff, including logarithm domains, whole-strip growth, all-height anchor positivity and ceiling quantifiers.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged construction assessment's exact-statement searches and inspected primary passages; compared L461's full text with L005, L018, L266, L320's strip proof, L452's logarithm proof, L322's stated obstruction, the external register and the prior attempt history. No changed theorem premise or new search for originality is needed.
SOURCE_EVIDENCE: Reused Titchmarsh second edition (1986), Theorem 14.2 and proof pp. 336–337, especially (14.2.5)–(14.2.6), and pinned September 30 Theorem 1.1 plus its logarithmic-control lemma as inspected in the construction assessment. Refreshed DLMF 5.11.1/5.11.3 sector and complex-remainder coverage, and inspected 5.11.9 including its uniformity for bounded real parts and both height signs.
COMPARISON: Classical sources cover the logarithm interpolation and gamma asymptotics; they do not state L461's changed-domain, all-height, central-zero-safe cutoff. L266 supplies the general witness comparison, L320 the prior strip method, and L452 only a narrower derivative conclusion. The later audit must verify L461's specialization and quantifiers; no direct theorem import or correctness verdict suffices.
GAP: Mathematical audit remains pending for the fixed logarithm neighborhoods, both exponential signs, damping limits, compact-height anchor, narrowed zero width, all epsilon losses and parameter/ceiling order. Essential source coverage for that exact audit is available; no source blocker remains.
REASON: Separate comparison of the newly nominated audit scope now maps every stated obligation to assessed source mechanisms or canonical local inputs. Approve one critical audit as REPRODUCTION, conditional on the retained external premise; no new result is proved in this literature turn.
SCOPE: The exact TARGET only, for L461's fixed 3/8<eta<R<1/2 and epsilon>0, all real centers including central zeros, existential constants, and c>3/16; exclude auditing the external manuscript/import closure or proving any coefficient signs.
LITERATURE_REASON: The invocation-start audit assessment was REVIEW_REQUIRED; construction coverage did not preapprove this separate critical audit. This turn supplies that missing scope comparison and reuses adequate literature rather than reopening the external theorem audit.

## Main gap, downstream use and decision test

The main gap is still the initial low-index signs at unbounded heights
and all-degree mixed positivity. The intermediate target is a critical
audit of L461, whose conditional smaller witness segment could reduce
the signs needed for a later exclusion argument. It supplies no signs.
Continue to that audit because the needed theorem cases are covered.
Abandon approval of the stated cutoff if the audit finds a missing
logarithm neighborhood, uncontrolled strip interior, vanishing anchor,
unabsorbed loss, or height/displacement-dependent constant where a
uniform one is claimed. Record a precise failure rather than infer a
verdict from this source review. No such mathematical verdict is made here.

## Reused sources and precise applicability boundaries

The [construction assessment](2026-10-24-fixed-half-plane-witness-cutoff-coverage.md)
records exact-statement and stronger-result searches, full primary
passages, and scoped duplicate/failure checks. Its target and external
assumptions have not changed. Those searches are reused, not claimed
as fresh searches or an exhaustive novelty check.

Titchmarsh, *The Theory of the Riemann Zeta-function*, second edition
revised by D. R. Heath-Brown (1986), [Theorem 14.2 and proof,
printed pp. 336–337](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173),
assumes RH. The construction assessment actually inspected the
Borel–Caratheodory and three-circles proof and both subpower signs
in (14.2.5)–(14.2.6). That inspection is reused. The printed theorem
does not apply under a 7/8 premise by substitution. Checking the
changed-domain proof is essential application work, justifying a
REPRODUCTION audit rather than a direct IMPORT classification.
The PDF opened again; OCR searches for the theorem/equation labels
failed. The screenshot endpoint supplied no additional readable proof
evidence in this turn; neither retrieval is counted as a new inspection
of the proof. Adequate prior passage coverage remains available.

The [DLMF 5.11 source](https://dlmf.nist.gov/5.11) was inspected again
on 2026-10-25: 5.11.1/5.11.3 use a closed sector away from the negative
real axis, and section (ii) supplies complex remainder bounds.
Equation [5.11.9](https://dlmf.nist.gov/5.11.E9) explicitly gives the
vertical gamma modulus asymptotic at both signs of infinity, uniformly
for bounded real parts. This is direct source coverage for the
fixed-strip gamma input already cited in L461, not a new lemma or a
proof of its particular powers. Compact heights still need the local
continuity/nonvanishing argument; an asymptotic alone does not cover them.

The [external-input register](../../foundations/2026-10-quasi-riemann-input.md)
and construction assessment retain September 30 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`: strict Re(s)>7/8,
pole at one allowed, boundary unexcluded. Reuse their inspected pinned
theorem and logarithmic-control lemma, without a new external proof
or import-closure audit. The latter lemma is about Hecke functions and
regularized Dedekind zeta; its mechanism is corroboration, not a direct
Riemann-zeta anchor theorem. No stronger Liu boundary is used.

## Exact obligations reserved for the mathematical audit

Read the full canonical L461 argument, using L005, L018, L266, L320
and L452 as its mathematical inputs. The source/local comparison gives
the following audit scope, without certifying any application:

- L005 and the classical logarithm mechanism: check the neighborhood
  beyond the outer disk, pole exclusion at large heights, Euler-log
  normalization only right of one, fixed radius gaps and both signs
  after exponentiation. L452's derivative conclusion at Re(s)>=63/64
  cannot itself cover the new anchors near Re(s)=7/8.
- L018, L320 and Stirling: check the entire completed-function strip,
  preliminary growth before maximum modulus, the branch of the power,
  both vertical boundaries, and the order Y to infinity then damping
  to zero. The later complex-circle estimate must retain a+/-Im(y).
- L018 and the retained premise: check every-height anchor positivity,
  including a=0; every completed prefactor and the compact minimum
  must be justified. Retain b<=3/8<eta strictly and exclude endpoints.
- L266: use its general F comparison rather than its specific exterior
  theta anchor. Check the hypotheses and full ceiling bound, d_0>=0
  at central zeros, all powers in the ratio R-eta+4epsilon, and the
  order of choosing eta,R,epsilon before constants and varying height.
  Test B_c independence from displacement and central multiplicity.

L320's c>1/4 result is a prior cutoff, not a duplicate of this claim.
L322's recorded stop fixes exterior anchors eta>1/2; it does not ban
the changed-domain test. The construction assessment inspected its
complete obstruction; this turn checked its stated scope and the prior
attempt's preservation of that stop. The old central-denominator failure
is addressed by the general L266 interface, whose application remains
an audit obligation. C460b is motivation only; no band proof or
cross-notebook input is needed.

The audit must retain the pinned strict Re(s)>7/8 premise, allowed
pole, locally unaudited external manuscript/import closure, fixed
3/8<eta<R<1/2 and epsilon>0, all-real-height anchor positivity,
independence of B_c from displacement and central multiplicity, and
the absence of claims at eta=3/8 or c=3/16. Signs, bounded-height
sign coverage, global mixed positivity and realization remain open.

Full matching Mathlib coverage and supporting complex-analysis API
names remain unchecked; absence is not asserted. The source coverage
is sufficient for the exact saved audit target as SPECIALIZE, with
later classification REPRODUCTION. This changes the pending coverage
decision, not L461 or its audit status. A newly ready assessment receives
separate supervisor approval before the later critical audit. No lemma,
mathematical script, DAG edge or PROOF.md argument was changed.
