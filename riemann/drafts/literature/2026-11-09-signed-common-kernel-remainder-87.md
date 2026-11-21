# Signed common-kernel remainder: completed source comparison

TARGET: Assess a signed common-kernel telescoping bound for integral_4^8 exp(E/10)|v(E)-v_p(E)|dE below 8.935649629627030e-35, using L938's unchanged polynomial and exact 34-row cancellations.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step88 compared L938(3)-(18), L947's endpoint/error construction, complete C947b, direct-density notes68, assessment85 and the shared-parameter Taylor assessment; new exact-object, signed-convolution, telescoping, divided-difference and Taylor-remainder searches are recorded below. No matching numerical theorem was inspected; failed searches establish no novelty.
SOURCE_EVIDENCE: NIST DLMF1.4.12 and1.4.35-37, including C^(n+1) hypothesis and both complete remainder forms; Makino and Berz, Taylor Models and Other Validated Functional Inclusion Methods, author PDF (2003), Definitions1-2 pp383-384 and Theorems1-2 with proofs pp390-391; de Boor, Divided Differences (2005), Section9 pp63-64, formula52 and its induction argument. Reuse assessment85's positive beta, exponential and Bernstein coverage, and L938's full-kernel/finite-polynomial inputs.
COMPARISON: Taylor's complete remainder and cancellation-preserving polynomial organization are known. They permit a later first-order common-kernel perturbation test with a uniformly paid second-order remainder; no source guarantees its signed-response norm or the required margin. Genocchi-Hermite represents a univariate divided difference, not this weighted signed simplex product. C947b's stopped rowwise linear allowance is preserved.
GAP: Derive and certify the complete first-variation response of the unchanged 34-row density, justify beta/Fubini reduction including faces, pay the full second-order allowance and bound the absolute response before integrating in E. None is calculated here. Compact polynomial negative mass, outer tail and global joins remain separate.
REASON: Primary statements cover one bounded specialization of known calculus and exact beta integration, rather than an automatic signed-convolution import. This changes the representation of the leading error while retaining full epsilon; source approval does not establish the target inequality or any new lemma.
LITERATURE_REASON: The new target changes the mathematical input from a rowwise absolute product allowance to a joint signed common-kernel replacement remainder; existing sources do not cover that difference.
SCOPE: One later REPRODUCTION proof attempt, after separate approval: first-order perturbation about unchanged p, full second-order Taylor remainder, exact signed response followed by the fixed beta-weighted coefficient bound described below; keep all34 rows,twelve factors,factorials,M_0^12,degree256,257 nodes,theta8,precision200,grid10^-120,tilt1/10,[4,8]. No new kernel, epsilon reduction, mesh refinement, outer-tail work or density sign assumption.
COVERED_TARGET: Test the complete weighted kernel-replacement budget on [4,8] using the exact signed first-variation response about L938's unchanged p and a full second-order Taylor remainder, requiring a total below 8.935649629627030e-35.

## Original nomination, preserved

The paragraphs below describe the REVIEW_REQUIRED state at nomination.
The completed step88 comparison following them supersedes that gate;
no research calculation has been invoked here.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The immediate intermediate issue is whether the signed
kernel-replacement remainder can fit the existing positive primitive
margin, after the scalar envelope was shown inadequate. Its plausible
downstream use is one paid component of a future B_4 certificate;
this does not supply that certificate or an RH route by itself.

The precise source-review test is to inspect applicable primary
theorems for the *complete* common-kernel replacement error, including
all higher replacement terms and integrable singular faces. A
first-variation identity alone, signed scalar-integral cancellation
without absolute-density control, or a sampled cancellation is not
enough. A method may use a signed integral representation or exact
finite-polynomial organization, but its hypotheses and actual
uncontrolled remainder must be compared with this target. Do not
assume either formula exists or that its sign/norm is favorable.

Reuse assessment85's primary beta, exponential and convex-basis
statements rather than repeat browsing. Search the exact signed
convolution/remainder claim, stronger results and obstructions. Compare
specifically with notes68's existing instruction to preserve polynomial
coefficient cancellation: that instruction does not establish a smaller
kernel-replacement allowance. The new issue is cancellation in the
replacement error itself, not the already exact v_p computation.

C938a's global row-ratio stop, L940's global Schur-concavity failure,
the full-field screen and its subsequent conditioned failure remain
evidence at their stated scopes. No reopening of those assertions is
proposed. C947b remains the canonical scalar-envelope stop; neither
it nor these historical failures bans a separately justified signed
remainder theorem. No cross-notebook input is nominated.

Continue only if source comparison identifies a precise applicable
estimate or a bounded independent test for a complete signed remainder
below the stated margin. Abandon this nomination if it merely renames
the stopped unsigned estimate, leaves an unbounded remainder, or
requires unproved density signs. A source review may itself end
without a ready mathematical target. Persistent blockage requires
another independently testable mechanism, not repeat approvals.

The next turn is literature_comparison, standard/high. A creative
attempt is not yet justified: there is no source-assessed signed
remainder construction with a discriminating finite test, nor an
effective global join. If comparison identifies one relevant to the
central gap, nominate its bounded test and escalation separately.
This nomination contains no new mathematical result. Mathlib coverage
of the proposed full estimate is unchecked, not declared absent.

## Completed comparison — step88, 9 November 2026

Outcome EXPLORATION, classification NOVELTY_UNCHECKED. This is method
coverage and a concrete application test, not a proved error saving or
a result beyond the sources inspected. No lemmas or mathematical
scripts are written. The TARGET at the top is preserved verbatim.

### Read inputs, overlap and scope of the old stop

Read L938's exact table and (3)-(18), including labelled-factor
normalization, positive half-integer beta parameters, analyticity,
full uniform epsilon, and exact signed polynomial integration. Read
L947's hypotheses, endpoint bounds and complete weighted-error
decomposition, and all of C947b. No coefficient certificate is needed
for this source comparison and none is claimed verified anew.

C947b's allowance is between 3.265161739633638e-32 and
3.265161739633639e-32, against the required 8.935649629627030e-35.
That is an upper-allowance failure, not a lower bound on the actual
replacement error. Direct-density notes68 already demand cancellation
in v_p; that demand alone does not improve the replacement error.
The new test would combine the coefficients of its leading response
before taking absolute values. It must not revert to summing the
34 absolute row errors and call that a signed method.

The local shared-parameter Taylor assessment was read as an exact
method/duplicate comparison. It concerns det H2 on a lambda panel,
not the absolute energy-density replacement error here. Its primary
calculus coverage is reusable; its application bounds are not inputs.
The ratio, Schur and full-field stops remain contrasts at their saved
scopes; no rejected density-order or vector-field assertion is reopened.
L939's eventual positivity remains ineffective for the outer join.

### Primary statements and limits

1. NIST DLMF, live inspected 9 November 2026,
   [1.4.35-37](https://dlmf.nist.gov/1.4#E35), requires
   f in C^(n+1)[a,b]. It gives the degree-n Taylor polynomial and
   both Lagrange and integral forms of the full remainder. For the
   proposed first-order application, a uniform second-derivative
   bound must cover the whole interpolation parameter interval.
   [1.4.12](https://dlmf.nist.gov/1.4#E12) supplies Leibniz's rule.
   These known theorems cover all higher terms, not merely an
   asymptotic first variation. They give no favorable numerical norm.

2. Makino and Berz, *Taylor Models and Other Validated Functional
   Inclusion Methods*, IJPAM 4(4) (2003),
   [author PDF](https://www.bmtdynamics.org/pub/papers/TMIJPAM03/TMIJPAM03.pdf),
   printed pp383-384, Definitions1-2; pp390-391, Theorems1-2 and
   their complete proofs. This version has 78 PDF pages, printed
   379-456; the previously inspected publisher copy has different
   pagination after these sections. A model requires pointwise
   inclusion and C^(n+1) regularity. Multiplication pays discarded
   polynomial terms, both polynomial/remainder products and the
   remainder product. Finite composition preserves inclusion when
   defined on the entire enclosing range. Scaling order does not
   guarantee sharp range bounds. Reuse the local assessment for
   arithmetic qualifications; no COSY theorem validates Python.

3. Carl de Boor, *Divided Differences*, Surveys in Approximation
   Theory 1 (2005), 46-69, author manuscript dated 21 December 2004,
   [primary author copy](https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf),
   Section9, pp63-64, (52), including the nested-simplex definition
   and induction from the first-difference integral. The integrand
   is an nth derivative evaluated at a convex combination of scalar
   nodes. Our integrals contain twelve kernel values at different
   energies and row-dependent half-integer weights. A simplex shape
   alone does not identify these integrals as a divided difference.
   No such identification or extra saving is imported.

Positive beta integration and polynomial convex-basis bounds are
reused from assessment85 and L938, without another discovery search.
These supporting sources suffice to attempt a specialized complete
response estimate. They supply neither its actual constant nor B_4.
Full and supporting Mathlib coverage of that estimate is unchecked.

### Proposed specialization and obligations, not a derivation

Use the interpolation from p to the full k=K(sqrt(.)) as the scalar
Taylor variable. Apply the known first-order theorem to the complete
34-row density expression, not separately signed scalar integrals of
v-v_p. The later proof must establish the required regularity by
finite product expansion and beta domination. Taylor models apply to
the smooth kernel amplitudes; they are not applied directly to the
singular factors at a simplex face. Retain all positive beta weights
and justify Fubini/differentiation for the absolute majorants.

For the first variation, nominate integrating the eleven unchanged
polynomial factors exactly while leaving the one kernel residual
unevaluated. Combine all rows and labelled positions in that response
before absolute bounding. Only the already proved full residual
bound epsilon may be used: no favorable residual sign, stochastic
independence between its evaluations, or differentiated epsilon bound
is available. Establish the response identity in the research step;
this review does not assert a specialized formula or its norm.

Separately bound the full second-order remainder uniformly over the
interpolation parameter. All twelve positions and all mixed/higher
replacement terms must be covered by Taylor's exact remainder, using
the existing amplitude and epsilon bounds with beta integrability.
Derive the actual combinatorial constant there, rather than assuming
that higher terms are negligible because epsilon is small. Prove
absolute error control for each E before the weighted integration;
cancellation only after integrating in E is inadequate.

Fix one finite response-norm test: use the existing sixteen energy
quarter-cells on [4,8], one normalized residual-energy interval [0,1],
and factor an explicitly proved common positive integrable beta
weight before polynomial bounding. Preserve the exact signed
polynomial coefficients, use the common Bernstein-basis coefficient
absolute bound, and integrate the weight exactly. Its degrees are
those forced by the unchanged p; no degree truncation is permitted
without paying the discarded part. Use the existing exponential
majorant exp(4/5), with its enclosing arithmetic. The common weight,
all affine powers and factorials must be derived, including endpoints;
ordinary unweighted polynomial bounds cannot absorb a divergent face.

First establish and compare the second-order allowance. Continue to
the response coefficient work only if that allowance is below the
margin. The decisive test is the sum of the certified first-order
norm allowance, the complete higher-order allowance and arithmetic
errors strictly below 8.935649629627030e-35. An oversized upper bound
or infeasible exact coefficient calculation stops this fixed test;
neither refutes the actual target. No mesh, precision, kernel, tilt
or split adjustment is authorized. A partial identity with an unpaid
norm is unfinished reasoning, not an accepted bound.

Even a successful replacement budget supplies only one necessary
component of the earlier sufficient B_4 certificate. The actual
polynomial negative part and tail beyond8 remain unpaid; the bound
need not leave enough reserve for them. Head/global variation,
parameter signs, other degrees, initialization and realization remain
open. The main all-degree mixed-positivity gap is unchanged.

### Discovery record and routing

Queries included `signed convolution product telescoping remainder
total variation cancellation multilinear approximation error`,
`"signed convolution" "approximation" "total variation"`,
`"convolution" "telescoping" "signed measures" error`,
`divided differences convolution exponential functions error bounds
Hermite Genocchi simplex integral`, `Taylor theorem Banach space
integral remainder Frechet derivative bounded multilinear polynomial
lecture notes`, `"Taylor models" "remainder" "polynomial" Berz
Makino 1998`, `"theta" "signed convolution" "remainder"`, and
`"Hankel determinant" "kernel" "first variation" error`.

Search leads included discrete Kornya-Presman/Poisson approximation,
exponential divided-difference algorithms, Banach Taylor notes and
generic validated-integration methods. These are unread leads, not
theorem inputs; none of their snippets establishes applicability.
The inspected sources listed above, together with reused coverage,
are the entire mathematical source basis. No novelty inference is made.
There is no essential source-access blocker for this bounded test.

The later work is REPRODUCTION of standard Taylor/beta methods in a
changed representation. A difficult proof-development route is
appropriate for the response reduction and singular-weight accounting;
this is not a creative central-gap mechanism. The blocker to a
justified creative nomination remains the missing effective global
join and actual all-degree sign input. Neither the elapsed creative
schedule nor this finite calculation licenses inventing that bridge.
Separate next-turn approval of the newly completed scope is required
before research. No mathematical exploration allowance was spent by
this literature-only step.
