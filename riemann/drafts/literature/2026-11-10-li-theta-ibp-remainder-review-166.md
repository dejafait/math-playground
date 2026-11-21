# Actual-theta integration by parts for the regularized remainder — source comparison

TARGET: Test whether theta-specific integration by parts using K=2A''-A/2 can certify L966(16) for all n>=1; use the complete n=2 and n=3 identities as a bounded test and retain every boundary, even-block and h=64*9^n term.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step167 completed bounded exact-target and Li/theta, Bell/cumulant, resolvent and integration-by-parts searches; read the primary DLMF rule and improper-integral conditions, Biane-Pitman-Yor Proposition2.1 and Section2.3, and the relevant Nuttall Section4 cases. Reused prior adequate scope comparisons; no inspected match for L966(16), and no novelty inference.
SOURCE_EVIDENCE: NIST DLMF1.4.16 and1.4.22-23, version1.2.8; Biane-Pitman-Yor, Bull.AMS38(4)(2001),435-465, Proposition2.1/(2.13), Sections2.1-2.3/(2.8)-(2.24), pp438-441; Nuttall author det3CAEXP_2.pdf, Sections4.2-4.6, pp12-14, compared with saved step391 assessment. Coffey2007 remains abstract-only after403, without an imported theorem.
COMPARISON: Standard integration by parts licenses a transfer only with its endpoints and convergence checks; it supplies no sign. Biane-Pitman-Yor supplies a probability/cumulant formulation and positivity of the first two unregularized Li coefficients, not the h-dependent rational comparison. Nuttall's conditional cumulant/index mechanism does not control this Bell numerator. Local L242/L044/L046 exclude generic positivity shortcuts.
GAP: Construct or obstruct a common boundary-compensation rule for the entire L966(15) numerator after coordinatewise transfer from K to its test factors; no such rule or R_n<=N_n bound is known from this review. All-n closure and sufficient regularization scope remain independent unpaid steps.
REASON: Approve one bounded mathematical exploration of the unchanged target using the audited new numerator: retain all boundary faces, even blocks and h terms in the complete n=2,3 transfers, then seek or refute one common compensation rule. This authorizes an attempt, not a sign theorem or a reproof of the representation.
LITERATURE_REASON: L966's new complete rational numerator changes the observable beyond both the representation-only coverage and step391's determinant compensation target; essential comparison of the proposed inequality mechanism was REVIEW_REQUIRED at turn start.
SCOPE: Actual L019-L020 K and A, actual Xi, integer n>=1, b=1/4 and h=64*9^n, all multiplicities and algebraic squares. One tensor integration-by-parts/face-compensation attempt with complete n=2 and n=3 tests; no positive Stieltjes premise, RH, ordinate replacement, or parameter extension is covered.

## Completed source review — step167

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target remains exactly TARGET above.
A compensated inequality for L966(16) would sign this prescribed
regularized observable and could support a later Li-margin comparison.
It would not resolve the separate mismatch between prescribed eta(n)
and L964's supplied-margin-dependent eta. No actual negative Li
coefficient or off-line zero has been produced.

### Primary coverage and limits

**Transfer calculus.** [NIST DLMF1.4.16](https://dlmf.nist.gov/1.4.E16)
is the ordinary integration-by-parts rule. Apply it first on finite
intervals with differentiable factors and integrable derivatives.
[1.4.22-23](https://dlmf.nist.gov/1.4.v) defines improper integrals by
endpoint limits and distinguishes absolute convergence. Read the rule
and surrounding integral conditions; online version1.2.8, released
15 September2026, inspected10 November2026. These are tools, not an
inequality for signed test factors. The future attempt must verify
the limits of every boundary expression and integrability of every
transformed term. Repeated coordinate transfers require control of
faces and their intersections as well as the interior. L019-L020
already give the actual differential identity, the nonzero origin
derivative and a justified single-cosine transfer. No new transfer
identity is derived in this review.

**Probability and cumulants.** Biane, Pitman and Yor,
[*Probability laws related to the Jacobi theta and Riemann zeta
functions, and Brownian excursions*](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf),
Bull.AMS38(4)(2001),435-465, DOI10.1090/S0273-0979-01-00912-0.
Read pp438-441: the theta/Mellin integration by parts, density
normalization, Proposition2.1, and the complete Section2.3 cumulant
argument. For its specific positive random variable Y, (2.13) gives
E(Y^s)=2xi(s), all complex s. For L=log(1/Y), (2.21)-(2.24)
express the ordinary Li coefficients through its cumulants; Jensen
and variance prove the first two signs. This is not an all-order
cumulant sign theorem. Nor does it estimate L966's additional
denominator or distant h-resolvent. No transformation from that law
to a new Q_eta formula is asserted. A positive probability law
alone cannot replace the missing signed comparison.

**Iterated-tail alternative, reused.** The completed step391 assessment,
`2026-11-04-actual-theta-signed-compensation-review.md`, remains
adequate for Nuttall's determinant target and the Csordas-Varga
weighted-moment scope. Rechecked [Nuttall's author copy](https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf),
Sections4.2-4.6, pp12-14: repeated upper-tail integration uses positive
Mellin parameters; the range is k>=r-1+ceil(m/2), conditional on
reverse regularity. Conjecture1 and exceptional indices remain.
This does not imply the two-point Bell-partition comparison. No
new audit or import of the underlying Karlin theorem is claimed.

**Access and unused leads.** Coffey, J.Approx.Theory146(2)(2007),
267-275, [DOI10.1016/j.jat.2006.10.006](https://doi.org/10.1016/j.jat.2006.10.006),
remains abstract-only; the publisher page returned403 in this step.
Do not impute theorem hypotheses or a sign certificate to it. Direct
import is parked. Its access is not essential to the independent
calculus test, and the next attempt cannot claim originality. Search
hits for Planat's growth-theorem kernel, theta square constructions
and second-level kernel concavity are uninspected leads here; none
is used as an input. No repeated retrieval of the earlier blocked
PDF or mathematical dependence on its content is prescribed.

### Exact comparison and bounded next attempt

Read L966 through its representation and scope, and L019-L020 in
full. Read L242/L044/L046 as obstruction comparisons, and the exact
step391 assessment/ATTEMPTS stop. The full L966 numerator contains
n+1 factors at b and h after denominators are cleared. Its signed
partition and h-subtraction are part of the target, not error terms
that may be discarded. The prior determinant source stop remains
valid evidence for that route; the new numerator is the materially
different input here.

The proposed mechanism is coordinatewise use of the known differential
identity on this full numerator, followed by regrouping the resulting
origin-face contributions with the signed interior terms. L020's
existing cosine transfer and the distinguished value b=1/4 motivate
this question; they do not establish any new boundary compensation.
Constructing a sign-preserving regrouping, rather than doing routine
differentiation, is the mathematical task. No particular regrouping
has yet passed even the bounded test.

For n=2 and n=3 write the complete symmetrized numerator before any
transfer; then compute the transferred interior and every surviving
origin face, keeping the exact d_k and h=64*9^n. Establish the relevant
boundary limits and absolute convergence. Require an exact identity
check before discussing signs. Test one explicit common grouping
on the entire orthant with all its faces, or give a rigorous integrated
bound. A finite numerical preview is not a certificate.

Continue only if the grouping has a proved sign/bound at both test
orders and an identified all-n structural mechanism with its remaining
assumptions stated. Retire this particular grouping if a retained term
defeats its proposed payment, the transfer simply returns the original
unpaid inequality, or it needs unknown Xi signs. An explicit violating
point defeats a pointwise rule, not the integrated inequality. Even
successful low-order certificates do not prove all-n positivity.
Unproductive transfer algebra alone does not justify another attempt.

Essential continuation inputs are L019-L020 and L966, with L024/L026
underlying the latter and L964 giving conditional downstream relevance.
L242/L044/L046 are contrasts only. No cross-notebook input is used.
Full matching Mathlib coverage is unknown; no library theorem is
asserted to provide the missing sign.

### Search record and outcome

Queries included `Riemann Li theta integration by parts`, the exact
Coffey theta-Laguerre title with pdf, `Li coefficients regularized theta
Bell polynomials inequality`, `Riemann xi theta kernel logarithmic
derivatives integration by parts inequalities`, `Li coefficients theta
inequality cumulants`, `Riemann resolvent Li positivity theta`, `xi Li
theta Bell Coffey`, `Li coefficients integration by parts theta`,
`Li coefficients beta eta theta`, `Li theta Bell polynomials
inequalities`, and `Biane Pitman Yor probability laws Jacobi theta
Riemann zeta Li cumulants 2001 pdf`. Exact and standard-term searches
found no inspected theorem giving the requested comparison; they
do not establish absence or novelty.

Bounded local searches covered the named compensation assessment/stop,
the November9-10 Li/theta assessments and attempt/history references,
and exact Biane/Pitman/Yor terms in literature, foundations and
ATTEMPTS. The latter hits concerned other authors/results; no adequate
saved assessment of this probability-law source was found. The older
representation assessment was reused for product/chain calculus and
the recorded Coffey access limit. No sibling notebook was inspected.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. This completes
coverage for one bounded attempt under the unchanged TARGET, not a
mathematical advance or discovery. No lemma, mathematical script,
DAG edge or PROOF argument is changed. The next turn should perform
the mathematical test; additional browsing needs a changed essential
hypothesis or source, not another repetition of this assessment.

## Original nomination — step166, retained as history

The following nomination records the read status before step167;
the completed review and current decision above supersede that status.

### Relevance and precise decision test

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is a theta-specific certificate for the exact
comparison R_n<=N_n, using the now-audited L966 numerator. Even success
would leave the independent question of sufficient regularization scope:
the prescribed eta(n) is not L964's supplied-margin-dependent eta.

The candidate mechanism is integration by parts with the actual identity
K=2A''-A/2 applied to the full symmetrized multiple integral in L966(15).
This names a direction for source assessment, not a derived identity.
It must retain all terms at zero, including those involving A'(0), and
justify each boundary limit at infinity. A boundary contribution cannot
be silently declared zero. A positive-density argument alone is excluded.

The bounded prospective test is to write the complete n=2 and n=3
transformed identities and test a proposed common compensation rule
on the entire positive orthant, with its boundary terms. Continue only
if the source comparison yields a specific rule whose signs or integrated
bounds can be proved and whose structure offers an all-n argument.
Reject that particular rule if a retained contribution defeats its
claimed estimate, or if it requires unknown Xi signs. Low-index success
alone is not an all-n result; low-index sign certificates are not the goal.
Failure of a pointwise certificate need not refute the integrated inequality.

### Inputs, comparisons and unread leads at nomination

Essential local inputs for a later attempt: L019-L020 for the actual
kernel and decay; L966 for the exact coefficients, Bell partitions,
positive denominators and h term; L964 for the conditional downstream
detector relevance. L024/L026 underlie the audited representation.
L242/L044/L046 are obstruction comparisons, not positivity premises.
No new zero-free region, positive Stieltjes measure, model-law realization,
or cross-notebook theorem is proposed.

The specific recorded stop is
`ATTEMPTS/2026-11-04-actual-theta-product-compensation-source-limit.md`.
It parks unsupported compensation of the D_(r,r-1) edge integral after
L766 and cites restricted moment/cumulant theorems. Preserve its evidence.
The new input here is the explicit two-point rational observable and
complete Bell-partition numerator of L966; this is not permission to
repeat the earlier source search without comparing the exact hypotheses.
Its linked source assessment,
`drafts/literature/2026-11-04-actual-theta-signed-compensation-review.md`,
is an unread lead in this step and should be inspected narrowly next.
The next review must retrieve essential primary statements/proof cases
before deciding whether any candidate actually applies.

The nested-threshold and finite-quartic stops concern excluded finite-law
realizations. They offer no positive input for this direct actual-theta
inequality and are not reopened. The unread Coffey paper is not silently
treated as essential coverage or as a theorem supplying the comparison.

No new lemma, calculation or mathematical script for this continuation
has been written. Full Mathlib coverage of the proposed certificate is
unknown. A genuinely new compensation construction could later merit
proof_attempt/creative routing, but its precise mechanism and essential
source coverage must first be established in a separate turn.
