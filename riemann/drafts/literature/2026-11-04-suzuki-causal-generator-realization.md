# Suzuki: finite-window causal generator realization

TARGET: Construct the finite-window causal C0-semigroup corresponding to Suzuki's kernels on L2(0,L), identify its generator domain and arithmetic/archimedean splitting, and verify its reflected relation to K_theta[L/2] without asserting dissipativity.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The step-270 generator-energy review searched exact Suzuki generator/causal/semigroup terms and finite-interval Riemann–Liouville terminology, and checked parameter-descent, construction and screw stops; no exact matching realization theorem was located. This is bounded coverage, not a novelty claim.
SOURCE_EVIDENCE: Primary statements and proof cases from step 270 reused; direct URLs verified in step 271: https://arxiv.org/pdf/1907.07302v2 (1.1),(1.10)–(1.13), Proposition 3.2,(3.13)–(3.15); https://arxiv.org/pdf/2108.02291v2 Thms 22,27,28 (p=2); https://iana.math.kit.edu/downloads/iana3/schnaubelt/Skripten/evgl-skript.pdf (19 March 2026), Thm 3.4; https://dlmf.nist.gov/5.9.E13. Source locations and scope are recorded below.
COMPARISON: Known fractional-integral generation and bounded perturbations cover the proposed functional-analytic method. The remaining specialization must identify the complete Xi transform, actual finite-window domain, arithmetic translations and reflection; none is claimed proved by this assessment.
GAP: Establish the actual finite-window realization down to theta=0, with explicit finite-L bounded perturbation control and the original unweighted norm. No window-uniform bound, total dissipativity or RH implication is covered.
REASON: This bounded prerequisite could make an energy comparison meaningful; merely differentiating a scalar transform does not. Reproof of fractional-integral generation, Suzuki kernel construction or L618's compact norm bound is unnecessary; only applicability and the actual-operator identification are justified work.
SCOPE: Real theta>=0, 0<L<infinity, complex L2(0,L), with Suzuki identification required for theta>1 where his complete continuous kernels are established. Retain distributional identity terms, causal support, lower-endpoint trace, finite-window compression and reflection. Import only the p=2 fractional-integral theorem, not the printed p=infinity extension.

Step 271 separately reviewed this coverage and repaired its missing direct
source URLs. SPECIALIZE is retained for the exact TARGET only; no
specialization has been executed. The controlling prior source review is
`2026-11-04-suzuki-generator-energy-source-scope.md`.

Use L018's completion and L618's actual operator setup; L739 is only a
contrast explaining why the old square-order argument is closed. There
is no cross-notebook input. For each fixed finite L, test the causal
integral operator with kernel K_theta(x-y) for y<x. Seek a C0 extension
to parameter zero and an explicit closed generator by the cited
logarithmic Riemann–Liouville generator and bounded perturbations.
Check the claimed domain in L2, all scalar identity contributions,
all rational completion terms, every arithmetic delay and the endpoint
conditions. Then verify the reflected identification with the original
operator on its active interval; treat its inactive subspace explicitly.
The reflection is not a semigroup identity for K_theta[t].

The discriminating test is equality with the complete Suzuki transform
for theta>1 together with finite-L perturbation bounds and a justified
parameter-zero strong limit. Record a failure if domain, kernel
identification or original-norm control does not pass. One coherent
construction attempt suffices; do not add an energy or all-window
positivity attempt to it. Finite-L generation alone would be local
progress by known-source specialization, not a new discovery or RH.

The independent future gap remains the signed total-generator estimate
in the original norm uniformly over L; no favourable arithmetic bound,
RH, innerness or contraction is assumed. Success here should nominate
one separately assessed signed discriminator, only if one is justified.
Failure must preserve the domain/identification obstruction and choose
a materially different target. Mathlib full coverage is not checked.


## Direct-source approval and recovery, step 271

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment; this separate literature-only turn verifies the cited sources and repairs that process issue without extending the target.

The exact-family search and proof-case assessment from step 270 are reused;
no additional broad discovery search is needed. The two local Suzuki
attempt records (parameter-descent source limit and small-window square-order
stop) were checked. Neither supplies a causal generator or rules out this
bounded realization target. The square-order stop remains in force.

- [Suzuki, *Integral operators arising from the Riemann zeta function*,
  arXiv:1907.07302v2, 6 March 2020](https://arxiv.org/pdf/1907.07302v2):
  rechecked printed p.3, Theorem 1.2 and (1.10)–(1.13), and p.8,
  (3.15) and its support qualification. The continuous complete kernel
  requires theta>1; the transform uses Im(z)>1/2. The reflected formula
  explicitly allows an output outside full-line L2. Earlier inspection
  of Proposition 3.2 and (3.13) is reused, not represented as a new proof.
- [Carvalho-Neto–Fehlberg Júnior, *The Riemann–Liouville fractional integral
  in Bochner–Lebesgue spaces I*, arXiv:2108.02291v2, 5 December
  2021](https://arxiv.org/pdf/2108.02291v2): rechecked printed pp.19,22–23,
  Theorems 22,27,28. Import only the scalar complex p=2, finite-interval
  statements. The domain criterion is absolute continuity of the
  logarithmic integral and an L2 derivative; (12) retains the scalar
  -psi(1) contribution. Reuse step 270's inspection of both domain
  directions, pp.23–27, including zero endpoint trace and strong-limit
  case. The printed p=infinity assertion remains excluded because the
  smooth-density argument does not justify it. This is not an import
  of a Suzuki realization.
- [Schnaubelt, *Evolution Equations*, 19 March
  2026](https://iana.math.kit.edu/downloads/iana3/schnaubelt/Skripten/evgl-skript.pdf):
  rechecked Theorem 3.4's hypothesis on printed p.74; reuse the complete
  statement and proof inspection on pp.74–76 from step 270. A bounded
  perturbation of a C0 generator retains its domain and yields a growth
  estimate, not a zero-loss contraction estimate. The actual finite-L
  boundedness remains to be demonstrated in the specialization.
- [NIST DLMF, equation 5.9.13](https://dlmf.nist.gov/5.9.E13): rechecked
  the digamma logarithm/Laplace-integral identity, with principal log
  and Re(z)>0 as in the reused source review. It is an input to a later
  specialization; no shifted/scaled Xi formula is derived here.

Decision: the URL/access issue is repaired; retain SPECIALIZE. There is
no new mathematical evidence and no changed route conclusion. L018 and
L618 remain essential local inputs; L739 is contrast only. Their detailed
proofs need not be reloaded for a URL repair. Full Mathlib coverage remains
not checked. No lemma, script, DAG or argument change is warranted.
