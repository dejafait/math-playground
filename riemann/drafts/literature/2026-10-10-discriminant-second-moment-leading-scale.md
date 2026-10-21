# Complete discriminant second moment — proposed leading-scale test

TARGET: Determine whether the complete actual normalized discriminant satisfies H^(-1) integral_[H,2H] Delta(t)^2 dt = beta (log H)^4 + o((log H)^4) with a fixed beta>0, retaining every physical projection and full response tail.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for shifted twisted fourth moments, unequal-orientation fourth products, Hardy carrier harmonics and mixed zeta moments; inspected Hughes–Young's primary theorem and essential cancellation cases, Bui–Hall's derivative mechanism and Pliego's primary definitions to reject a terminology mismatch. Narrow L366/L368/L370/L381/L383/L389 and relevant assessment/failure searches found no completed exact discriminant-square asymptotic.
SOURCE_EVIDENCE: Hughes–Young, arXiv:0709.2345v2, Theorem 1.1, (11)–(17), remarks, Proposition 2.1 proof, (46)–(58) and combination after (58), pp. 3–11; Bui–Hall arXiv:2304.05178v1 Theorem 3, Proposition 3, (7), Sections 5 and 7; Pliego arXiv:2211.11450v1 (1.5), Theorems 1.1–1.2 and arXiv:2210.15321v1 (1.2). Primary links and precise qualifications below; local full-tail and two-factor contour inputs inspected separately.
COMPARISON: Hughes–Young supplies balanced shifted fourth moments with fixed rational twists, beyond L389's unweighted upper bound; Bui–Hall supplies ordinary Hardy-jet conversion and fourth-moment control. Neither states this complete discriminant asymptotic or signs its coefficient. Existing two-factor carrier contours are tools for comparison, not matching four-factor results.
GAP: A bounded source search found no adequate full match. The exact physical expansion, every nonzero carrier contribution, full-tail transfer, sharp endpoints and leading-coefficient noncancellation remain mathematical obligations; no beta or new bound is established.
REASON: Approve one later bounded proof attempt from the inspected shifted-moment, reflection, contour and complete-tail tools; import their known statements unchanged and test the unmatched four-factor projection first. No inaccessible theorem is being assumed, and failure of this test must stop the proposed moment certificate.
SCOPE: The exact TARGET only, fixed actual F_0,G,A, ordinary jets through order two, all sufficiently large real H and sharp [H,2H]; fixed finite heads before height limits, full tails afterward. No growing twist, derivative order, RH, phase independence or imported four-factor carrier estimate.
LITERATURE_REASON: The target changed from an O(log^4 H) upper bound to an exact positive leading coefficient; shifted finite-twist fourth products and four-factor physical projection cases were essential new comparison cases, not covered by L389's prior assessment.

The main gap remains actual-theta global mixed positivity. This
intermediate target tests whether the log^4 cost of L389's complete
square integral reflects its exact arithmetic structure or just its
absolute estimates. Its downstream use is deciding whether refining
that full-second-moment method can improve the negative-set proportion
without additional distributional input. A positive leading coefficient
would not show that the actual negative-set bound is optimal or small;
an upper bound on a moment is not a lower bound on a sign-set size.

The proposed inputs are L366 (the fixed actual F_0,G,A and complete
response jets), L370 (the zero-safe polynomial), L388 (the negative
first mean for comparison) and now audited L389 (the finite upper
budget). Any more detailed carrier or mixed-moment input must be
identified and assessed before use. Only ordinary derivatives through
order two, the same sharp [H,2H] and fixed actual functions are proposed.
No RH, simplicity, noncoincidence, independent phases, eventual D sign,
positive-part estimate or common-zero bound is available or assumed.

A potential new source lead is an unconditional fourth moment with
fixed Dirichlet twists and small complex shifts. It is an unread lead
here. The existing unweighted Bui–Hall theorem cannot simply be called
a twisted-moment theorem. A source review must retrieve exact twist,
shift and error hypotheses and relevant proof cases, compare ordinary
jet differentiation and full-tail passage, and check recorded failures.
Import a matching known conclusion if one exists; no novelty follows
from the narrow local comparison. This proposal does not reopen the
parked sharp-Hardy access, rational-grid sampling or common-free
localization routes, and does not require recovery of corrupted Conrey
coefficients already unnecessary for L389.

Continue only if the full second-moment scale can be tested with
adequate unconditional source coverage and controlled complete tails.
In a later approved calculation, retain signed terms before deciding
whether the leading coefficient is positive or cancels. If an essential
twist/projection case or tail estimate is inaccessible, record that
specific blocker and park the dependent calculation rather than assume
it. No expression for beta, new bound or conclusion about its sign is
derived in this proposal. Global positivity, total pencil margin,
eventual discriminant sign, actual common-zero upper counts, low
indices, heights above forty and endpoint margins remain unresolved.

Full matching Mathlib coverage is not checked. The text above records
the original proposal and its unresolved obligations. The separate
source comparison below now approves a bounded attempt, not the
asymptotic, a coefficient sign, or an extension of L389's conclusion.

## Separate source comparison — 2026-10-10, step 44

This is a LITERATURE turn. No physical expansion, coefficient
calculation, new lemma or mathematical script was produced. The main
gap and downstream use remain those of the original proposal: test the
cost of the complete second-moment method, without inferring an optimal
negative-set measure or any RH consequence.

### Primary input and its qualifications

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. **641** (2010), 203–236,
[arXiv:0709.2345v2](https://arxiv.org/pdf/0709.2345v2), Theorem 1.1,
pp. 4–5, evaluates (16), with two positive-height and two negative-height
shifted zeta factors. The rational twist has coprime positive h,k,
hk<=T_Y^(2/11-epsilon). All four complex shifts are O(1/log T_Y).
The weight is smooth and nonnegative, supported in [T_Y/2,4T_Y], with
|w^(j)| bounded by constants times T_0^(-j) for every fixed j and
T_Y^(1/2+epsilon) << T_0 << T_Y. Its complete six-term expression
(17), including the finite Euler factors (12)–(15), has error
O(T_Y^(3/4+epsilon)(hk)^(7/8)(T_Y/T_0)^(9/4)).

Inspected the holomorphy remark following (17), Proposition 2.1's
contour/reflection proof, the diagonal pole cases (46)–(57), and
Proposition 4.1/(58) with their subsequent combination. The auxiliary
residues cancel between diagonal and off-diagonal contributions; the
six-term total must be used before specializing coincident shifts.
No diagonal-only formula or termwise differentiation of singular
pieces is imported.

The theorem is unconditional. Fixed heads produce fixed positive
integer twists; their reduced h,k eventually meet its size condition.
Smooth brackets with fixed relative transition width meet its support
and derivative conditions, with T_Y chosen at the height scale. These
are hypothesis comparisons, not a completed sharp-endpoint transfer.
Keeping a cutoff fixed while taking H to infinity is essential: this
review licenses no growing-cutoff error summation. Slow carrier
amplitudes still require explicit derivative bounds. The gamma phase
is not a slow weight permitted by this theorem.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1), 11 April 2023,
Theorem 3 and its defining asymptotic, Proposition 3 in Section 4.2,
(7), Sections 5 and 7, supply the unweighted complex-shift formula and
ordinary Hardy derivative mechanism. Reused the already inspected
fixed-order upper bounds in L389; checked the complex-shift Cauchy
discussion in Section 5 directly. This is supporting coverage for
orders zero through two, not a theorem for physical Delta. Their
Theorem 4 cites stronger twisted coverage, but its longer-polynomial
range is unnecessary for fixed heads; this review relies on the
directly inspected Hughes–Young theorem instead.

No reproof of either moment theorem is justified. A later proof must
cite them precisely and establish the family-specific conversions,
including factors of i for ordinary height derivatives and derivatives
of all envelope and response factors. Cauchy differentiation must act
on a holomorphic total with uniform complex-shift error; it cannot act
on a real-shift asymptotic alone.

### Full physical projection: the unmatched case

Read L366 (1)–(2), L368 (3)–(7), L370 (1)–(8), L389's physical-jet
conversion and polynomial budget, L381 Sections 3–4 and the relevant
contour audit, and L383 Section 3. These fix the actual functions,
complete right-line derivative series and common envelope. L370's
polynomial includes zeros of either function and retains the entire
envelope curvature; its normalized correction cannot be discarded
without a square-integral estimate.

The real response is a real projection of its complex carrier, rather
than its modulus. The exact square must therefore be expanded before
deciding which projected products match Theorem 1.1. L381 and L383's
height rectangles handle two critical-line factors. They do not state
the four-factor estimate needed here; their bounds and endpoint cases
may not be cited as if the number of factors were immaterial. Whether
nonzero harmonics contribute at log^4 H scale, vanish below that scale,
or defeat this certificate is the first research question. This review
does not establish their exact list, neglect them, invoke independent
phases or treat them as permitted Hughes–Young weights.

The basic analytic tools for investigating this difference are already
available: exact reflection, controlled gamma ratios and holomorphic
height contours, with L320's fixed-strip growth and small derivative
circles. An extension to four factors would need its own complete
proof and endpoint estimates. EXPLORE permits testing that missing
estimate; it does not import it or guarantee its truth. If such a test
requires an essential unread theorem outside this coverage, stop
dependent work and record the precise missing source for review.

L368 (5) supplies the absolute tails through order two on Re s=5/2.
L389 supplies uniform fourth-moment upper budgets for the full physical
critical jets. These are adequate inputs to attempt a norm transfer
after evaluating fixed heads. A later proof must bound the complete
tail error in the square integral uniformly in large H before taking
the head limit; pointwise tail convergence alone is insufficient.
No tail-transfer inequality or limiting coefficient is proved here.
Sharp endpoint control likewise remains an application obligation.
Nonnegativity of the full Delta square may be used for bracketing;
signed expanded terms require their own justified transfer.

### Search, duplicate and failure comparison

Queries included `Hughes Young twisted fourth moment zeta function
small shifts theorem 1.1`, `Bui Hall 2304.05178 Theorem 3 fourth moment
derivatives Hardy Z`, `zeta unbalanced fourth moment`, `zeta mixed
moments 3,1`, `zeta third power conjugate moment asymptotic`,
`Hardy fourth moment theta exponential twisted`, `zeta unbalanced
moments`, `zeta unequal powers mean moment`, and `zeta mixed fourth
moment phase`. Search hits alone were not theorem evidence; unrelated
web results and nonprimary summaries were not used.

Javier Pliego's *Twisted mixed moments of the Riemann zeta function*,
[arXiv:2211.11450v1](https://arxiv.org/pdf/2211.11450v1), (1.5) and
Theorems 1.1–1.2, concerns a height-scaled Dirichlet polynomial and
two zeta factors at distinct height multiples, with additional
restrictions and a conditional case. His *Mixed moments of the
Riemann zeta function*,
[arXiv:2210.15321v1](https://arxiv.org/pdf/2210.15321v1), (1.2),
also defines a three-factor statistic at scaled heights. Reading these
definitions rejects them as direct coverage for the present
same-height four-factor projections; their full proofs were not needed
or inspected. These are terminology mismatches, not obstructions to
the proposed asymptotic.

Local comparison found only L389's absolute upper bound and L388's
first mean for this actual Delta. The previous moment applications in
L381/L386/L387 concern two-factor statistics, not this square. No
duplicate exact beta calculation was found in the searched paths.
Read the sharp-Hardy source stop in
`ATTEMPTS/2026-10-10-parked-sharp-hardy-source-and-recovery.md` and
reused the negative-set assessment's grid and sign-localization
comparisons. Hughes–Young is a different accessible source, not an
access retry or implicit import of the parked Das–Pujahari theorem.
No discrete grid, common-free localization or uniform return route is
reopened. Neither the bounded search nor the failure to find a direct
statement certifies novelty.

### Approval and discriminating test

Approve exactly TARGET for one later bounded proof attempt, using
EXPLORE because the full physical projection has no adequate matching
theorem in the checked sources. Preserve signed terms and full tails.
First determine whether the actual expansion can be evaluated with
the balanced theorem plus proved bounds for every unmatched carrier
term at the required scale. Continue to coefficient evaluation only
when that reduction is justified. A positive beta requires a rigorous
noncancellation argument for the complete coefficient, not positivity
of an isolated diagonal or the fact that Delta squared is nonnegative.

Abandon this implementation if a necessary retained term has no
controlled contribution at log^4 H scale, if the full tail cannot be
transferred, or if the complete coefficient cancels. Preserve the
achieved result or obstruction and distinguish it from a disproof of
the moment target. This attempt does not require the unrelated
positivity, common-zero or pencil-margin gaps to be resolved.

Essential continuation inputs are L366, L368, L370, L388 and audited
L389; L320/L381/L383 supply only their stated strip and contour tools.
All unmatched four-factor estimates, endpoint transfers, complete-tail
limits and beta>0 are unresolved. No RH, simplicity, noncoincidence,
independent phases, eventual D sign or common-count assumption is
authorized. Full matching Mathlib coverage is not checked; supporting
complex-analysis facts are not a matching moment theorem. Any later
successful application belongs in a canonical lemma with Hypotheses,
Conclusion, Proof and Mathlib, rather than in this assessment.
