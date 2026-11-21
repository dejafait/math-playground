# Off-line Li tail displacement — proposed specialization

TARGET: Bound the total absolute difference between actual conjugate-paired Li tail terms and K_n(gamma)=2-2*cos(2*n*arctan(1/(2*gamma))) over gamma>sqrt(n) by O(sqrt(n) log n), without RH.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step215's direct-tail review214 searched Li truncation/zero-counting/asymptotics; additional exact Li tail/critical-line, real-parts/arctan approximation and truncation-error queries found no inspected matching displacement theorem. The November10 Li/zero duplicate screen found the ordinate-only equality warning in review158, not this error estimate. Bounded search only; no novelty claim.
SOURCE_EVIDENCE: Primary statements, hypotheses and relevant proof cases are recorded in completed review214: Hasanalizade-Shen-Wong2107.06506v1 Corollary1.2/(1.5), Section2/(2.1)-(2.3), corollary proof; Arias de Reyna author version31Jan2011 Theorem1/proof pp.4-5 and normalization pp.1-3; DLMF4.6.1/domain. L018 and L977 read; L968's audited threshold read. Reuse review158's inspected prohibition on exact ordinate-only replacement.
COMPARISON: Known counting and elementary logarithm tools cover the inputs, and the real-ordinate model is standard. They do not state the required uniform off-line displacement bound. Specialize only this difference, independently of the suspect contour proof; no reproof of the counting theorem, Li criterion or model asymptotic is justified.
GAP: Establish a uniform estimate for arbitrary 0<beta<1 at gamma>sqrt(n), sum the errors absolutely with multiplicities and justify the cutoff convention. No bound has been derived or verified in this assessment.
REASON: A precise independently testable part of the original residual is now identified with accessible essential inputs. New continuation written in a literature-only turn; separate next-turn approval is required before invoking research.
SCOPE: Fixed actual zeta; integer n>=2; all positive-ordinate zeros beta+i*gamma counted with orders, even when ordinates coincide; every 0<beta<1 allowed; conjugates paired once; complementary tail gamma>sqrt(n) to the weak finite cutoff; O-constant independent of n. No RH, simplicity, improved strip, finite zero list or finite-sum sign assumed.

## Source record

Use [the completed source comparison](2026-11-10-symmetric-zero-tail-residual-review-214.md)
for exact citations, versions, inspected cases and source-access limits.
The primary counting citation is
[Hasanalizade-Shen-Wong, Corollary1.2/(1.5), p.2](https://arxiv.org/pdf/2107.06506v1#page=2).
The model citation is
[Arias de Reyna, Theorem1 and proof, pp.4-5](https://personal.us.es/arias/56-2RHB.pdf#page=4).
The elementary principal-logarithm series is
[DLMF4.6.1](https://dlmf.nist.gov/4.6.E1).
Only a counting-growth consequence is needed for this subtarget; the
stronger logarithmic counting error is available for a later residual
assembly. Constants need not be effective.

## Proposed target, not a result

For each entry rho=beta+i*gamma in the positive-ordinate multiset define

    A_n(rho)=2*Re[1-(1-1/rho)^n],
    K_n(gamma)=2-2*cos(2*n*arctan(1/(2*gamma))).

Test whether there is a finite C independent of n such that

    sum_(rho: gamma>sqrt(n)) |A_n(rho)-K_n(gamma)|
        <=C*sqrt(n)*log n                     (n>=2).

The sum is over zero entries, not distinct heights. This is the exact
meaning of the TARGET field, not a conditional claim that the inequality
holds. A proof must supply the full convergence argument. An elementary
uniform estimate may first be tested for arbitrary beta in (0,1), but
the final sum is for actual zeta, with its counting bound. Avoid assuming
the logarithmic remainder stays small after multiplication by n unless
its bound is explicit throughout gamma>sqrt(n). The comparison is to
the exact arctangent phase; no n/gamma phase replacement is authorized
or needed here.

## Relevance, bounded test and remaining gaps

The main gap remains L030-L032/C032a all-degree positivity and L966
signed forcing. This intermediate bound would pay the part of a direct
tail argument which sees off-line real parts. It could then be combined,
after a separate assessment where needed, with a truncated Stieltjes
estimate and the ordinary arithmetic decomposition to seek the corrected
residual in review214. Its possible downstream benchmark is L968's
whole-Li lower bound at every positive exponential rate.

Continue only if the stated O(sqrt(n)*log n) error follows uniformly
without assuming the wanted signs or deleting any zeros. Stop the
proposed comparison if the actual uniform bound or summation exceeds
that threshold; preserve an informative failure rather than silently
enlarging it. Do not add a second mechanism in this attempt.

An exact all-degree ordinate-only identity would be a different,
RH-equivalent claim identified in review158. The proposed error is
restricted to a growing tail. Actual low-height contributions remain
untouched. Even success leaves the pointwise truncated model estimate,
constant matching, endpoints in a full residual assembly, and especially
the growing finite-zero sum's sign unresolved. The model's l2 error
cannot be imported as the desired pointwise polynomial error.

Essential local context: L018 for strip/conjugation/multiplicities;
L977 for the corrected sign and conventions; L968 for the downstream
threshold. L975's ordinary germ is normalization context; L976 and
L977's horizontal failure are stop evidence, not positive premises.
No cross-notebook input is used. No full matching Mathlib theorem has
been checked; availability is unknown.

Recommended actual mathematical task after separate approval: calculation,
standard/high. This is a standard asymptotic specialization, not a new
central sign mechanism. No creative escalation is justified while the
independent sign of the growing finite-zero sum remains unsupported.
