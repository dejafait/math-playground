# Full-action half-plane Poisson transfer — completed source comparison

TARGET: Test whether half-plane Poisson representation at a=-R combines L679's mass, L678's ray bound and L674's point attenuation to exclude L679-feasible actions for all sufficiently large n for each fixed C, without imposed zeros or open-domain positivity.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 62 searched bounded harmonic half-plane Poisson uniqueness, signed boundary/positive-arc norm estimates and rational angular-action variants; exact queries, primary reading, scoped duplicate/failure checks and unused leads are recorded below. No inspected theorem settles the exact full-action exclusion; this is not a novelty claim.
SOURCE_EVIDENCE: Axler--Bourdon--Ramey, Harmonic Function Theory, second edition (Springer 2001), author-hosted PDF retrieved 2026-11-02: Theorem 7.5 p.148, Theorem 7.3 and proof p.147, kernel and integrability pp.145--146, Corollary 2.2 and proof p.32, with Theorem 2.1 and proof p.31. Reused L679's audited mass, L678's independently audited unrestricted auxiliary estimate and prior Herglotz assessment; L674 Section 2 remains a verification obligation.
COMPARISON: The primary bounded-harmonic theorem covers signed continuous boundary data without an open-domain sign hypothesis. It supplies the representation tool, not boundedness of the full action or its proposed quantitative contradiction. L677/L678 exclusions require a zero and a finite ansatz; L674's Herglotz lower bound requires open-domain positivity. None settles the unchanged target.
GAP: Verify all full-action harmonicity, closed-half-plane continuity and global boundedness hypotheses for each fixed n and psi; verify L674's parameter-point bound independently; compare the Poisson-weighted L679 mass and complete signed complement uniformly for each fixed C. No such application or comparison is proved in this literature step.
REASON: Essential primary representation coverage is now sufficient for one bounded attempt on the unchanged target; no essential source is blocked. Import the cited representation and uniqueness results, justify their exact applicability, and test the family-specific mass/attenuation mechanism rather than reprove general potential theory.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED because the unrestricted full-action mechanism lacked a primary boundary representation theorem and its infinity/uniqueness hypotheses; this step fills that essential gap.
SCOPE: Exactly TARGET, with the complete L666 kernel, arbitrary complex normalized L2 preimages and L679's fixed-C quantifiers. Covers a later attempt to verify full-action applicability, audit the point attenuation used and test the signed weighted comparison. No imposed zero, finite ansatz, extra positivity domain, cone/H/support/Xi bridge or global RH conclusion is authorized as an assumed input.

## Completed comparison — 2 November 2026, step 62

### Primary theorem and essential proof cases inspected

S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*,
second edition, Graduate Texts in Mathematics 137, Springer (2001),
ISBN 978-0-387-95218-5. The [author's edition page](https://axler.net/HFT.html)
links the [complete primary text](https://axler.net/HFT.pdf#page=152).
Read Theorem 7.5 (printed p.148; PDF index 152), Theorem 7.3
and its entire proof (p.147), kernel/integrability discussion
(pp.145--146), and Corollary 2.2 with its entire proof (p.32),
including Theorem 2.1 and proof (p.31).

Theorem 7.5 represents a continuous bounded function on the **closed**
upper half-space, harmonic inside, by its boundary Poisson integral.
In two dimensions the kernel is h/[pi*((s-t)^2+h^2)], h>0.
Bounded boundary data suffice for absolute integrability; unweighted
L1 data, positivity and a separately prescribed limit at infinity
are unnecessary. Theorem 7.3 proves boundary continuity by a local/tail
split. Corollary 2.2 supplies uniqueness by odd reflection and Liouville;
without boundedness, the zero-boundary function h prevents uniqueness.
Thus holomorphy alone is insufficient. These are imported results,
not new notebook lemmas.

### Applicability obligations retained for mathematics

The source permits a rotation/translation to Re(a)<x. A later proof
must give that identification and its evaluation and measure
normalizations explicitly. Verify harmonicity of Re A from full-action
holomorphy, continuity at every finite boundary point, and a bound on
the entire closed left half-plane for each fixed n and psi. A bound
only on compact subsets, only on the segment, or only on the boundary
is not itself the imported hypothesis. Uniformity in n of that
qualitative bound is not a source requirement; the later quantitative
comparison must nevertheless retain all n-dependent costs. Any infinity
argument must use the complete kernel and the j=0 factor. Do not
identify angular L2 regularity of psi with a Hardy norm of the
parameter action without proof.

L674 Section 1 already gives compact differentiation bounds and
holomorphy outside |a|<=tau. Those recorded statements locate the
relevant argument; they do not independently verify its global
half-plane boundedness or its Section 2 attenuation. Section 2's
parameter-circle argument, including denominators, monotonicity and
normalized Cauchy--Schwarz, must be checked before using it. Do not
import Section 3's Herglotz lower bound, which needs the forbidden
extra open-domain sign. No action formula at -R or new asymptotic
inequality is derived in this source review.

L679's mass uses normalized theta measure after its stated tangent
change, whereas the half-plane theorem uses Lebesgue boundary
measure with the Poisson weight. A later proof must compare those
actual measures, keep the closed-segment endpoints, and pay the
signed complement using the entire two rays. The point bound must
be compared with the real-part lower estimate without assuming a
real action or symmetry. Continue only if this yields the stated
fixed-C, all-sufficiently-large-n contradiction; otherwise name the
precise hypothesis, error or rate failure. This remains a test,
not a consequence certified by this assessment.

### Exact local duplicate and failure comparison

Read L666 Section 2/(6); L674 hypotheses and Sections 1--4;
L678 hypotheses, Sections 1--3 and its Section 7 ray-bound audit;
L679 hypotheses, conclusion and source/growth scope. Reused the
ready mass and rational assessments rather than refreshing their
source searches. Read the exact stop records
`ATTEMPTS/2026-11-02-positive-real-parameter-disk-cost-stop.md`,
`ATTEMPTS/2026-11-02-full-degree-polynomial-arc-cost-stop.md`, and
`ATTEMPTS/2026-11-02-repeated-exterior-pole-rational-cost-stop.md`.

L678 (1) and its Cauchy--Schwarz form (14) are unrestricted kernel
estimates; its exclusion (2) additionally uses its rational ansatz
and prescribed zero. L677's polynomial/zero exclusion is likewise
class-specific. L679 supplies the separately audited conditional mass
without either ansatz. L674 supplies an unaudited point-attenuation
argument and a distinct positive-real-domain stop. The present proposed
mechanism uses signed boundary representation of the actual action,
not the finite rational geometric-series identity or a Herglotz
extension with added signs. These historical stops remain valid within
their scopes and do not prohibit this different bounded test.

### Search record and comparison limits

External queries executed:

- `Axler Bourdon Ramey Harmonic Function Theory bounded harmonic upper half space Poisson Theorem 7.5 pdf`
- `Poisson integral half plane bounded harmonic function uniqueness signed boundary Hardy space`
- `"half-plane" "Poisson" "bounded" harmonic boundary segment positive negative mass`
- `"Poisson" "harmonic" "positive" "boundary arc" "norm" half plane lower bound`
- `"rational" "Poisson" "positive arc" "L2" separator`
- `"angular" "action" "Poisson" "half-plane" Blaschke`

The standard representation above is adequate coverage for its tool.
Searches for stronger sign/mass statements did not identify an exact
full-product rate theorem. Do not infer originality or impossibility
from these bounded searches. General modified-Poisson growth results,
positive-half-plane representations, Hardy-space discussions and other
returned leads were not inspected and are not imported; the bounded
continuous theorem makes them nonessential to the present attempt.
The combined product-specific exclusion remains unproved. No new
lemma, mathematical script, action realization or source-exceeding
result is established in this turn.

### Mathlib

Searched `site:leanprover-community.github.io/mathlib4_docs Poisson harmonic half plane`
and inspected [Harmonic.Constructions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Harmonic/Constructions.html).
`AnalyticAt.harmonicAt_re` is supporting coverage for the real part of
an analytic function; it does not supply the half-plane representation
or the quantitative exclusion. Full matching Mathlib coverage is not
established by this scoped check; no absence claim is made.

## Preserved nomination (written before this source review)

The following prospective language records the original uncovered
nomination. Current readiness and obligations are the fields and completed
comparison above; no mathematical proof is added by changing readiness.

## Intended scope and relevance

Retain exactly L679's q>=1, n=12q+3, tau=(n-1)/n,
x=-5/4, R=11/8, complete L666 kernel including j=0 and 1/u,
normalized complex L2 pairing, A_n(x)=1, fixed real C,
||psi_n||_2<=exp(n/100)*n^C, and nonnegative real trace on the
entire closed segment x+i[-9/20,9/20]. No prescribed zero,
finite degree, repeated-pole form, reflection symmetry or additional
positivity domain may be imposed.

The main gap is actual-Xi all-degree mixed positivity. This proposed
intermediate test concerns the unresolved general angular separator
route. An exclusion could change that route decision; it would not
disprove RH, establish Xi realization, or settle original unit-residue
H, cone or support claims. These remain independent gaps.

Essential prospective input IDs are L666 (6), audited L679,
L678 (1), and L674 Section 2. The review must distinguish L678's
ansatz-independent kernel estimate from its ansatz-dependent
exclusion. L674 has not had an independent audit; its elementary
parameter-point estimate is a verification obligation, not a newly
approved result in this nomination.

## Bounded proposed mechanism and test

Investigate a Poisson representation of Re A_n on Re(a)<x, with
boundary line Re(a)=x and evaluation at -R. Primary coverage must
identify the boundedness, boundary continuity, integrability and
behavior at infinity actually required. Check these for the full
angular integral, rather than using a finite-mode surrogate or
holomorphy alone. Do not assume segment positivity extends to an
open domain.

The proposed bounded test is whether the resulting weighted central
mass can be compared with the complete complementary boundary and
the parameter-point bound uniformly for every fixed C. Continue
only if the exact transfer yields a rigorously quantified asymptotic
budget contradiction. Otherwise identify the failed theorem
hypothesis, missing uniform estimate or nondecisive rate and stop
this mechanism or refine it with materially new evidence. No part
of this transfer or its conclusion is derived here.

## Duplicate and failure comparison to complete next turn

The nomination read L674's hypotheses and Sections 1--4, L678's
hypotheses, auxiliary bound and factor-bound passage, and the three
exact ATTEMPTS records in the preceding mass assessment. Existing
finite-degree and repeated-pole exclusions require an exact zero;
the positive-real-domain exclusion requires an extra open-domain
sign. They neither prove nor refute this proposed implication.
L678 already uses a Poisson kernel for a finite rational
transformation; merely renaming that argument would not be a new
test. The substantive proposal is a representation of the
unrestricted full action itself with its actual boundary trace,
removing those ansatz restrictions.

The next literature step must search exact and stronger results and
relevant local records, inspect a primary half-plane Poisson theorem
with its essential proof cases, and decide readiness honestly.
This nomination does not certify novelty or approve mathematics.
Prior stops remain preserved. Matching Mathlib coverage is unchecked.

If approved, the intended purpose is proof_attempt / creative:
the obstruction is transferring segment-only positive mass to the
paid parameter point despite uncontrolled signs outside the segment.
The decisive bounded evidence is a uniform cost contradiction for
full actions or an exact obstruction to that transfer. The separate
source gate takes precedence over this recommendation.
