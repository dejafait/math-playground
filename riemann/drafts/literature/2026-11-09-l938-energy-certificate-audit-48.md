# L938 independent audit: completed source comparison

TARGET: Review source coverage for an independent conceptual audit of L938's fixed-energy representation and 32-cell certificate, including the repaired endpoint arithmetic, without refining the test.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step49 reused step46/47 exact-object, duplicate and failed-route searches; added primary-source searches for root-node versus extrema-node Chebyshev interpolation and Kronecker coefficient recovery, and inspected the essential statements/proof cases below. No originality inference.
SOURCE_EVIDENCE: Inspected DLMF1.14.30–31 https://dlmf.nist.gov/1.14#E30 ; 5.12.1 https://dlmf.nist.gov/5.12#E1 ; 5.5.1/5 https://dlmf.nist.gov/5.5#E5 ; 1.9.30 https://dlmf.nist.gov/1.9#E30 ; 1.10.6–7 https://dlmf.nist.gov/1.10#E6 ; 18.3.1–2 https://dlmf.nist.gov/18.3#E1 ; Trefethen ATAP author excerpt Theorems4.1–4.2/proofs https://people.maths.ox.ac.uk/trefethen/ATAP/ATAPfirst6chapters.pdf ; Harvey arXiv:0712.4046 section3/3.1 Proposition5 p7 https://arxiv.org/pdf/0712.4046 ; Python3.13 Decimal methods https://docs.python.org/3.13/library/decimal.html#decimal.Decimal.copy_negate . Prior Bhaskar–Song v3 coverage reused.
COMPARISON: Known integration, Laurent coefficients, beta/gamma identities and arithmetic contracts cover audit methods, not the actual certificate. Trefethen's inspected aliasing theorem uses extrema nodes; Harvey's integer result assumes nonnegative coefficients and leaves signed details unchecked. L938's root-node and signed-extraction specializations need independent proof/code review, not blanket citation.
GAP: Independent validation of L938's analytic specialization, finite algebra, node enclosures, signed integer production and complete cell endpoints remains undone. No essential external source is blocked. The 17 uncertain cells and global crossing premise are unchanged.
REASON: Separate source comparison is complete for a bounded conceptual audit. Known methods support checking the existing local proof obligations without new sign experiments or another unchanged literature search; this approves an audit, not L938's correctness.
LITERATURE_REASON: Startup REVIEW_REQUIRED target introduced singular-endpoint, root-node/Laurent and signed-integer implementation claims beyond the prior density-test assessment; only those missing method comparisons were added.
SCOPE: The exact COVERED_TARGET is ready for REPRODUCTION conceptual audit. Preserve degree256, 257 nodes, theta cutoff8, precision200 and 32 original cells; no parameter endpoint, crossing refinement or substitute normalization. Full/supporting Mathlib coverage remains unchecked.
COVERED_TARGET: Independently audit L938's fixed-energy representation and corrected 32-cell certificate, including singular endpoints, root-node interpolation and exact-integer production, without refining the test.

## Nomination context, preserved

The following paragraphs record the original audit obligations, not a
completed audit. Step49's source comparison and decision are below.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. L938 supplies a fixed-density formulation for one finite
H2 determinant, not its global sign. A valid full crossing bound and
independent endpoint signs might support finite-degree contact exclusion;
other degrees, tangencies, initialization, realization and global
continuation remain independent gaps.

Essential local inputs for the later audit are L019, L037, L058, L874,
L917 and L938. Check the exact 34 coefficients and M_0^12 normalization,
all 12 factor masses and factorials, origin regularity, nonzero density,
absolute exponential moments, even analytic extension and ellipse bound,
root-node interpolation error, full theta tail, integer beta integrations,
and the saved complete cell endpoints. The numerical claims retain
L037's Decimal/exponential implementation contracts. The rational
consistency checker does not independently replay the node computations
or large polynomial production; those limitations must stay explicit.

The first-pass script/certificates and exact failure are preserved under
`scripts/heat/actual-h2-energy-cell-first-pass-48.*`,
`scripts/heat/actual-h2-energy-cell-polynomial-first-pass-48.json`, and
`scripts/heat/actual-h2-energy-cell-first-pass-failure-48.json`.
They are invalid evidence, not alternative sign certificates. A repair
at the identical fixed budget does not authorize numerical refinement.

Continue to a separately approved conceptual audit only if the known
inputs cover the exact implementation and the repaired record supports
the claims. Otherwise identify the missing hypothesis or source precisely.
An audit may validate or correct the record; it may not seek a new
alternating triple by changing the experiment. L915/L916/L922/L937
retain their original scoped stops. No cross-notebook input is proposed.

## Step49 source comparison — 9 November 2026

This is literature-only work on the saved TARGET. Read all of L938 to
identify its source scope, L037, L019 and L058's domination argument;
inspected relevant producer/checker ranges and the interval primitives.
Reused step46/47's L874/L917 conventions and finite-log comparison.
No mathematical producer/checker was executed. The intermediate target
is independent validation of this fixed representation/certificate.
It could retain an input for parameter zero-counting, conditional on a
future full crossing bound and independent endpoint signs. The main
L030–L032/C032a positivity gap and other degrees remain open.

### Primary inputs actually inspected and limits

Sources below were inspected on 9 November 2026; DLMF references mean
its online numbered equations on that date.

- [DLMF1.14.30–31](https://dlmf.nist.gov/1.14#E30): read the convolution
  definition, product identity and piecewise-continuity condition.
  Reuse step46's singular-f_0 warning. Audit the explicit simplex
  domination and Tonelli/Fubini justification; the displayed theorem
  alone does not cover that endpoint.
- [DLMF5.12.1](https://dlmf.nist.gov/5.12#E1): read Euler's beta integral
  and Re(a),Re(b)>0 condition. The proposed k_i+1/2 parameters, and
  k_i+l_i+1/2 after polynomial expansion, have nonnegative integer
  indices and lie in that domain. Repeated integration, Jacobians and
  factorials still need audit. Read the gamma recurrence
  [5.5.1](https://dlmf.nist.gov/5.5#E1), duplication formula
  [5.5.5](https://dlmf.nist.gov/5.5#E5), including exclusion of
  nonpositive integer 2z, and factorial values
  [5.4.1](https://dlmf.nist.gov/5.4#E1). These support the half-integer
  factors, not the saved polynomial or its masses.
- [DLMF1.9.30](https://dlmf.nist.gov/1.9#E30): read Cauchy's formula and
  its analytic-interior/continuous-boundary hypotheses. More directly,
  [1.10.6–7](https://dlmf.nist.gov/1.10#E6) gives Laurent coefficients
  on circles strictly inside an analytic annulus, with absolute
  compact convergence. Read those hypotheses and formulas. Use the
  annulus formulation for the Joukowski pullback; analyticity at w=0
  is not supplied. Audit even continuation, the square-root branch,
  ellipse interior/neighborhood and the claimed bound10^9 separately.
- [DLMF18.3.1–2](https://dlmf.nist.gov/18.3#E1), including both diagonal
  sums, supplies root-grid discrete orthogonality and the constant-mode
  normalization. It does not validate interval node evaluations.
  Trefethen, *Approximation Theory and Approximation Practice*, author
  first-six-chapter excerpt, Theorems4.1–4.2 and full proofs,
  printed pp25–27 (PDF pp28–30), was read at the
  [author URL](https://people.maths.ox.ac.uk/trefethen/ATAP/ATAPfirst6chapters.pdf).
  It treats the extrema grid. Its result cannot replace the local
  root-node signed/zero-alias proof unchanged. Audit that specialization,
  (13)'s summation constant and coefficient errors. Chapter8 is outside
  the excerpt and was not imported. Demanet's MIT note returned 404
  on direct retrieval: an optional unread lead, since the inspected
  Laurent/orthogonality inputs suffice to audit the local argument.
- David Harvey, *Faster polynomial multiplication via multipoint
  Kronecker substitution*, J.Symbolic Comput.44(10) (2009),1502–1510,
  DOI10.1016/j.jsc.2009.05.004,
  [14-page arXiv preprint](https://arxiv.org/pdf/0712.4046), section3 and
  section3.1, Proposition5, printed p7: read the full standard case.
  It assumes equal-length nonnegative inputs of at most b bits, with
  product width controlled by 2b+ceil(log2 L), and explicitly leaves
  signed coefficients unchecked. This covers the known method, not
  L938's balanced-digit implementation. Audit its own absolute
  coefficient bound, packing, sign restoration, carry extraction,
  unequal lengths and final carry. Modular evaluations alone remain
  sanity checks. No multipoint or complexity claim is needed here.
- [Python3.13 Decimal documentation](https://docs.python.org/3.13/library/decimal.html#decimal.Decimal.copy_negate),
  retrieved as 3.13.18: read copy_negate/copy_abs, exp,
  next_minus/next_plus, Context-method equivalence and context minus.
  Context-free exact sign copying and correctly rounded half-even
  exponentiation are documented; neighbor methods specify the context.
  These support the conditional contract and repair's intended semantics,
  not a verified Python build or whole-expression enclosure. Audit
  call sites, three explicit contexts, flags and conversions; retain
  library correctness as an assumption. The original producer's Python
  version has not been identified by this review.

Reused the step46 Bhaskar–Song v3 Definition3/Theorem4/full-proof
comparison without reopening it. Nonzero continuous density, finite
sign variation and explicit absolute exponential domination remain
required before zero counting. No zero-count theorem is invoked here.
No standard source theorem was reproved. Full/supporting Mathlib
coverage is unchecked, not asserted absent.

### Saved evidence and bounded audit decision

Read the saved checker summary completely with the JSON inspector:
969 reported checks, no recorded failures, negative indices0–1,
positive2–14, uncertain15–31, and no alternating triple. It explicitly
excludes independent node/polynomial production replay. Reading this
report is not verification; the later audit must inspect complete
relevant evidence before accepting those claims.

Read the complete selected first-pass `reported_lower_minus_required`
value: a positive rational. Preserve this invalid endpoint as an audit
regression obligation. The read-only producer diff contains exactly
the two documented substitutions of copy_negate for ambient Decimal
endpoint negation. This supports the recorded repair scope, not any
first-pass enclosure. Read the interval class to identify the actual
contracts; the old quadrature theorem is not coverage for the new
singular integration.

Reused step46/47's exact-object duplicate/failure comparisons and read
the fixed-test ATTEMPTS record. L915/L916/L922/L937 retain their scoped
stops. No inspected duplicate supplies this certificate, and failed searches do
not establish novelty. New queries included `Chebyshev interpolation
zeros first kind analytic Bernstein ellipse aliasing theorem root nodes`,
`site.dlmf.nist.gov Chebyshev interpolation zeros aliasing Cauchy integral
formula`, and `David Harvey faster polynomial multiplication via
multipoint Kronecker substitution 2009 signed coefficients base`.
Only the inspected primary texts above support this comparison.
No cross-notebook input was used.

Continue with the exact COVERED_TARGET: independently audit every
load-bearing analytic claim and the complete corrected certificate,
or identify a precise defect and its effect on L938's conclusions.
Replay must keep the original budget, preserve original evidence and
save separate audit artifacts. No new cells, larger degree, precision
sweep, endpoint experiment or substitute normalization is covered.
If a claim fails, qualify or correct it instead of seeking replacement
signs. No essential source blocker remains; correctness is still pending.

Outcome EXPLORATION: completed new method coverage and explicit hypothesis
comparisons, with a ready conceptual audit but no new mathematical input,
obstruction or advance toward global positivity. This literature turn
is NOVELTY_UNCHECKED; the covered audit uses REPRODUCTION. No lemma,
mathematical script, DAG edge or PROOF argument was changed.
