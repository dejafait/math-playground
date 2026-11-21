# Suzuki causal realization: conceptual-audit scope

TARGET: Critically audit L740's finite-window generator domain, full transform identification, parameter-zero strong limit and reflected norm identity in the original L2 norm.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact Suzuki causal/generator, finite-interval fractional-integral and bounded-perturbation searches in the step-270 assessment and the separately approved step-271 realization assessment; the operator, parameter ranges and source hypotheses are unchanged. No new discovery search or novelty claim is made.
SOURCE_EVIDENCE: Reuse Suzuki https://arxiv.org/pdf/1907.07302v2 Thm1.2,(1.1),(1.10),Prop3.2,(3.13)-(3.15); Carvalho-Neto–Fehlberg https://arxiv.org/pdf/2108.02291v2 Thms22,27,28 (p=2 only), both domain proof directions pp.23-27; Schnaubelt https://iana.math.kit.edu/downloads/iana3/schnaubelt/Skripten/evgl-skript.pdf (19 March 2026), Thm3.4 pp.74-76; DLMF https://dlmf.nist.gov/5.9.E13. Step 272 rechecked the exact domain statement and digamma identity while applying this coverage.
COMPARISON: Generation and the logarithmic domain are known inputs. L740 specializes them via an explicit bounded perturbation and a weighted measure algebra used only for identification; the independent task is to verify that specialization, including its original-norm reflection, not to reprove the source theorems or test an energy sign.
GAP: L740 has a written proof but no separate conceptual audit of domain equivalence, endpoint trace, complete scalar/rational/arithmetic terms, convolution/compression, transform uniqueness and the strong limit. Total dissipativity and Xi signs remain outside this audit.
REASON: The analytic identifications are load-bearing for any later energy mechanism. Their sources and hypotheses lie within the previously assessed scope, so reuse is adequate; a separate critical audit of the new proof is justified before relying on it.
SCOPE: Exactly L740 on complex unweighted L2(0,L), 0<L<infinity, theta>=0 for the constructed semigroup and theta>1 for identification with Suzuki. No all-window sign, quantitative contraction, RH-equivalent positivity, new energy witness or p=infinity extension is approved.

This continuation received separate literature approval in step 273, based
on unchanged source coverage. No mathematical audit is claimed completed
in either step 272 or step 273. The construction itself was performed under
`2026-11-04-suzuki-causal-generator-realization.md`, saved and separately
approved before that step. This assessment adds no new mathematical
derivation or source theorem.

Use the full canonical `lemmas/L740-suzuki-finite-window-causal-generator.md`,
L018's completion and L618's kernel/support/Euler-series setup. The
earlier source reviews already read both p=2 domain proof directions,
bounded-perturbation generation and Suzuki's reflected support cases.
The small-window square-order and direct-Hankel-composition stops remain
contrasts, not mathematical inputs. No cross-notebook read is needed.

The critical checks are whether the logarithmic-integral domain has
exactly the claimed left trace and no added trace on f, whether the
digamma scaling and both rational terms give the stated q and scalar,
and whether absolute convergence justifies the full measure exponential,
Laplace uniqueness and finite-window homomorphism. Check the distinction
between strong convergence at zero, any unproved norm convergence, and
the reflected zero-parameter limit on the active/inactive decomposition.
These are a conceptual audit of an analytic realization, not an
arithmetic replay or a candidate-RH review.

Pass only if every identity and domain claim follows in the original
norm from these hypotheses. Repair any concrete defect in the canonical
proof and report its effect; if an essential global multiplier or a
changed target norm is required, preserve the failed identification.
Do not use a structural checker as evidence of analytic correctness.
No creative signed target is nominated yet: an independent favourable
total-form estimate has not been identified. After the audit, bounded
discovery of one exact signed discriminator has priority over repeated
routine audits, subject to its own coverage.

Full Mathlib coverage remains not checked. No LITERATURE_REASON is
needed for step 272: it was the approved mathematical specialization,
and source passages were read only to apply the existing assessment.


## Separate scope approval, step 273 (2026-11-04)

LITERATURE_REASON: The supervisor requires separate approval of this newly saved audit assessment. This source-only step checks the new proof's scope against the already inspected inputs; it does not repeat discovery or execute the audit.

Read the complete L740 to identify its source uses, and reused the detailed
step-270 comparison and step-271 direct-source approval. Rechecked the
following primary statements at their direct URLs above:

- Carvalho-Neto–Fehlberg v2, Theorems 27–28, printed pp.22–23:
  the finite-interval fractional-integral family and the exact logarithmic
  absolute-continuity/Lp-derivative criterion, including -psi(1) in (12).
  Use only p=2, X=complex scalars and endpoints 0,L. The prior reading of
  both proof directions, pp.23–27, is reused. The excluded p=infinity
  density issue remains excluded; no new source proof is supplied.
- Suzuki v2, Theorem 1.2 and (1.10)–(1.13), printed pp.2–3:
  theta>1, real continuous causal kernel, growth O(exp(x/2)), and transform
  on Im(z)>1/2. Rechecked (3.15)'s printed p.8 support warning: the
  untruncated output need not be L2. Prior Proposition 3.2 and support/Fubini
  proof-case coverage is reused. There is no imported parameter-zero
  continuous-kernel assertion or full-line unweighted multiplier theorem.
- Schnaubelt, 19 March 2026, Theorem 3.4, printed pp.74–76:
  A is a C0 generator and B is bounded on X; D(A+B)=D(A), with
  original-norm bound M exp((omega+M||B||)t). The theorem's equivalent
  norm inside its proof does not supply original-norm contraction.
  The prior proof reading is reused; the statement and norm-return case
  were directly rechecked.
- DLMF 5.9.13: the principal-log digamma/Laplace identity was directly
  rechecked. Its positive-real-part scope is unchanged; applying its
  shift and scale is part of the later audit, not a result of this turn.

The exact-family searches and duplicate comparison from step 270 remain
adequate: no target hypothesis or technique has changed. Checked the two
local ATTEMPTS records for direct parameter descent and square order.
The former lacks an applicable compressed composition identity; the latter
has a negative small-window witness. Neither is the proposed causal-domain
audit, and neither is reopened. This review establishes no novelty.

Decision: retain SPECIALIZE and approve exactly TARGET for the next
research turn, classified REPRODUCTION. The source statements cover its
imports, while the full transform, weighted-measure compression, endpoint
representative and reflection remain local proof obligations to audit.
Reading L018/L618 in full is deferred to that audit; this scope approval
neither validates those inputs nor certifies L740. No source access blocker
or missing essential source coverage was found. Full Mathlib coverage
remains unknown. There is no new mathematical evidence, so the checkpoint
honestly records STALLED for this separate approval rather than ADVANCE.

Pass/repair/fail threshold remains the one above. A favourable total-form
estimate in the original norm, uniform over windows, is still unidentified;
this blocks a justified creative signed target pending the essential audit.
No lemma, mathematical script, DAG or PROOF change was made.
