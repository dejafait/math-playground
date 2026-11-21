# Direct actual-density enclosure: source comparison

9 November 2026. Literature only. No new lemma, derivative-error formula,
root enclosure, quadrature calculation or mathematical script is produced.
The matching assessment is
[the direct-density scope](2026-11-09-l938-direct-density-crossing-scope-67.md).

## Object, relevance and existing evidence

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is strictly upward crossings of L938's actual
fixed density on the closed energy interval [1/4,4]. A certified compact
crossing statement could contribute to the already assessed Laplace
zero-count route; it would leave other energies, contacts, parameter
endpoint signs, degrees, initialization, realization and continuation open.
The step46 assessment is reused for downstream scope, not as a crossing
theorem. No new zero-free-region claim or cross-notebook input is used.

Read L019's actual K; L938's full 34-row table, (5)–(18), singular factors,
analytic ellipse, coefficient errors and exact beta-integration argument;
L940 through its arithmetic-average definition and factorial convention;
L942 through (3)–(7) and the dominated-differentiation/face discussion.
This is source-scope comparison, not an independent audit of these lemmas.
All twelve labelled factors, factorials, M_0^12 and the positive energy
prefactor must remain. L938's polynomial construction has no spatial
tail for these compact energies. Its actual-kernel approximation error
still includes the full theta tail and rounded interpolation coefficients.

The step63 divergence source notes and step67 candidate-stop/history were
checked. That candidate's rigorous negative residual rejects that field
only. C938a's global ratio-order stop, L940's Schur-concavity stop and the
recorded L941 constraint are not obstructions to direct integrated signs.
L938's certified negative and positive cell masses establish neither
pointwise exclusion nor derivative signs. The unrelated shared-parameter
H2 Taylor assessment was checked as a duplicate: it encloses det H2 in
lambda on a small panel, not v in energy. No result from it is imported.

## Primary sources actually inspected

1. Fredrik Johansson, *Numerical integration in arbitrary-precision ball
   arithmetic*, arXiv:1802.07942v1 (22 February 2018), Sections 2, 2.1,
   3.2, printed pp.2–4,6
   ([primary paper](https://arxiv.org/pdf/1802.07942v1)).
   Read the full algorithm, error-bound hypotheses and singular-endpoint
   cases. It integrates a univariate complex segment; the evaluator must
   enclose the function and reject nonanalytic complex input when asked.
   Gaussian error control needs a complex ellipse bound. Requested
   tolerances do not guarantee achieved accuracy: the returned radius
   is the evidence. Unbounded endpoints need manual truncation and
   separately justified omitted-tail bounds. The paper does not turn
   an eleven-dimensional singular simplex into an automatically certified
   integral or pay signed cancellation. Direct nested quadrature would
   need additional chart, endpoint and propagated-error work. It is not
   selected for this bounded attempt; no benchmark implies feasibility.

2. FLINT v3.3.1, `doc/source/arb_calc.rst`, subdivision-based root-finding
   contract, lines 102–149, and callback definition, lines 26–39
   ([versioned documentation](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/arb_calc.rst));
   complete `src/arb_calc/isolate_roots.c`, lines 16–171
   ([versioned implementation](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/arb_calc/isolate_roots.c)).
   Read all exclusion, isolation, budget-exhaustion and endpoint cases.
   The routine requires genuine interval evaluations; unknown regions
   remain in the output. A range excluding zero is discarded; opposite
   nonzero endpoint signs plus a derivative interval excluding zero
   certify one simple root. Multiple roots and subdivision-endpoint
   roots need care. For this target, positive derivative coverage of
   every unresolved closed interval suffices without asserting existence
   of a root there; endpoint roots must still be covered. This is a
   proposed specialization of the standard mean-value/interval method,
   not a proved certificate or a new root-isolation theorem.

   Also inspected FLINT 3.7.0-dev's generated-2026-11-09 algorithm page,
   Lemmas 1–2, Algorithm 1, Theorems 3–4 and proofs, and its matching API:
   [algorithm](https://flintlib.org/doc/algorithms/ball-arithmetic/real-root-isolation.html),
   [API](https://flintlib.org/doc/arb_calc/isolate_roots.html).
   Those pages disclose partial LLM generation. Consequently the
   versioned older contract and complete implementation above provide
   corroborating primary evidence; no Newton convergence-factor theorem
   or implementation guarantee is needed or imported. The modern
   integration API was read for comparison only. A failed `partition.c`
   URL is a nonessential lead, not a source blocker: its routine is not
   required by the proposed local enclosure algorithm.

3. NIST DLMF, inspected live 9 November 2026:
   [18.9.21](https://dlmf.nist.gov/18.9#E21), Chebyshev derivative identity;
   [18.14.4](https://dlmf.nist.gov/18.14#E4), ultraspherical bound for
   -1<=x<=1 and parameter lambda>0; and
   [1.9.30–31](https://dlmf.nist.gov/1.9#E31), Cauchy integral/derivative
   formulas, including continuity on the contour and analyticity inside.
   These are standard supporting inputs for analytic derivative control.
   The bound in 18.14.4 is not stated for an arbitrary complex ellipse.
   Cauchy cannot differentiate a bound known only on the real interval.
   A later specialization must specify the correct polynomial family,
   affine energy rescaling, full derivative-series majorant, interpolation
   aliases and coefficient-rounding contribution. No new constant or
   specialized inequality is derived here. L938 already supplies the
   full-kernel analytic domain and coefficient majorant, so their use
   needs an application proof, not a new literature search.

The exact beta integral for positive half-integer parameters and finite
signed polynomial integration are reused from L938, with its DLMF
citations and stated arithmetic contracts. They are not new results.
The source gaps are effective application bounds and final signs,
not missing essential method statements. Full/supporting Mathlib
coverage for the proposed certificate is unchecked, not declared absent.

## Discovery and comparison

Queries included `validated numerical integration convolution algebraic
endpoint singularities interval arithmetic Taylor models`, `Johansson
rigorous high precision computation integrals 2018 Arb integration
holomorphic`, `certified root isolation interval arithmetic derivative
sign exclusion real functions interval Newton`, `"signed convolution"
"theta" "density" crossing`, `"L938" "density" "theta"`,
`"signed convolution" "upward" "crossing"`, `validated convolution
algebraic singularity polynomial beta integral rigorous`, and
`"Chebyshev" "derivatives" "Bernstein ellipse" rigorous error bounds
convolution`. Exact-label queries were supplemented by standard method
terms rather than treated as adequate theorem discovery alone.

Results supplied the primary numerical methods above, generic Taylor
model/validated integration work and unrelated convolution/algebraic
geometry papers. No matching actual-theta crossing theorem was inspected;
this is not evidence of novelty or absence. Petras's original paper and
the Trefethen book/search extracts remain unread optional leads, not
imported theorems. Johansson's inspected algorithm and existing L938
analytic machinery suffice for the selected scope. Earlier Laplace
and divergence source assessments retain their own qualifications.

## Fixed later test and application obligations

Nominate one later REPRODUCTION attempt, after separate approval of the
completed assessment. Keep the exact saved TARGET. Prefer L938's existing
degree256 rational kernel polynomial and exact beta-integrated signed
coefficient representation to a new multidimensional quadrature program.
Retain its original theta cutoff, interpolation coefficient grid and
arithmetic contract; exact rational polynomial evaluation may be used.
Do not regenerate a more accurate kernel or fit another field after a
failed margin. Reuse saved coefficients only after checking their input
identity and complete load-bearing certificate fields. This literature
turn has not inspected or verified the large coefficient certificate.

The later work must establish pointwise error bounds for v-v_p and
v'-v_p' from the actual kernel and its first derivative. It may specialize
the inspected analytic/Chebyshev inputs and L938's beta integration,
including the derivative of E^17. The existing integrated error (17)
cannot be differentiated as an inequality. Differentiating an approximate
polynomial gives its derivative, not an enclosure of the actual derivative.
If any positive rescaling is used for stability, explicitly retain its
derivative and justify the sign transfer at actual zeros. No rescaling
identity is established here, and no new normalization may change v.

Preserve all signed coefficient cancellation before forming final error
intervals. Independently bound every discarded kernel, derivative,
coefficient-rounding and arithmetic contribution. A pointwise error
floor must be compared with the achieved sign margin, not with a cell
mass or a requested precision. Unproved constant bounds stop the test.

For one bounded coverage attempt, start with the whole closed [1/4,4]
and allow only dyadic bisection to depth12, at most 8191 examined
intervals. Each leaf must have a rigorous v-range excluding zero, or
a rigorous v'-range lying strictly above zero. Keep all undecided leaves,
including both outer endpoints and shared subdivision endpoints. No
sampled signs, isolated polynomial roots or root count without a full
error margin certify the actual density. Stop earlier if a rigorous
pointwise error comparison already blocks this fixed implementation.

A complete certified cover is evidence for this compact crossing claim
only. Any remaining leaf, unpaid derivative error or prohibitive exact
evaluation is an honest scoped failure/inconclusive result, not a
counterexample, not a reason to increase budgets, and not a global ban
on direct integration. A claim of failure of the crossing assertion
would need an actual zero with a nonpositive actual derivative, which
this literature turn has not supplied. Save full certificates and report
actual/required margins and unresolved leaves in the later attempt.
