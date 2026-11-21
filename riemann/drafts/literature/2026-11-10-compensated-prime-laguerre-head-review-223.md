# Compensated prime-power Laguerre route — completed source comparison

TARGET: Assess whether a compensated Laguerre prime-power sum supplies a one-sided subexponential upper bound for S_f(n), with n-uniform cutoff control.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step224 searched Li coefficients/Laguerre/prime sums, unconditional and cutoff variants, and the exact Bombieri-Lagarias title; reused reviews200/203/204/219/221 and the L976/L977 stops. No inspected source supplied the desired signed bound. A seemingly quantitative Dirichlet-L cutoff lead is explicitly retracted. Queries, access limits and inspected passages are recorded below; no novelty inference.
SOURCE_EVIDENCE: Lagarias AIF57(2007), DOI10.5802/aif.2311, Definition4.3/(4.5), Lemma4.4/(4.8), p1709 eta display after(4.13), Thm2.4(2)/(2.21) pp1702-1703, AppendixA pp1737-1738; https://www.numdam.org/item/10.5802/aif.2311.pdf ; arXiv math/0404394v4 Section4 eta display. Bombieri-Lagarias1999 author PDF recovered but unreadable extraction and unavailable images; original convergence proof not inspected. Omar-Ouni-Mazhouda2011 DOI10.1112/S1461157010000215, retraction notice and Section2/(2)-(6), pp142-143, inspected; no theorem imported from it.
COMPARISON: Lagarias gives a fixed-j compensated eta moment, matching L977's Laurent convention, and a regularized Laguerre test-function interpretation. Neither inspected passage supplies n-uniform cutoff control or independent one-sided arithmetic cancellation. The advertised Dirichlet cutoff lead concerns primitive conductor q>1 and is retracted, so it cannot pay the zeta target. L968's one-sided criterion and L980's exact arithmetic split remain the downstream context, not sign premises.
GAP: No inspected theorem establishes S_f(n)<=C_epsilon exp(epsilon*n) for every epsilon>0 with constants independent of n. The original moment proof remains uninspected; fixed-index citation is not uniformity. An independent Cauchy-tail target can be reviewed directly from a PNT remainder without relying on that inaccessible proof, while leaving the finite statistic unsigned.
REASON: Stop direct source payment by the located cutoff lead and do not repeat the blocked original-proof extraction. Preserve the signed target as unpaid. Nominate a separately reviewable finite-cutoff Cauchy estimate, whose truth and quantitative scale can be tested independently of RH and the S_f identification; no estimate is derived or approved here.
SCOPE: Literature comparison only; actual zeta, integer n>=2, ordinary L977/L980 eta convention and all zero orders. EXPLORE does not certify the proposed P_n identity, a uniform remainder or a sign mechanism. No RH, simplicity, head sign or uniform exchange is assumed.
LITERATURE_REASON: The nominated signed arithmetic target was REVIEW_REQUIRED and lay outside review221's residual audit. Exact compensation, source scope and uniform-cutoff coverage required this comparison; no repeat of the parked Coffey2007 search was made.

The original nomination below is preserved. Its requests and pending-source
language describe the pre-step224 proposal, not an additional active action.

This is a proposed observable, not an established identity or bound.
For a finite prime-power cutoff X>1, consider the candidate expression

    P_n(X)=sum_(2<=m<=X) Lambda(m)/m * L_(n-1)^(1)(log m)
           -integral_1^X L_(n-1)^(1)(log x) dx/x,

where L_(n-1)^(1) is the usual generalized Laguerre polynomial.
The next review must verify its exact relation, if any, to the
nonalternating S_f of L980, including compensation and convergence.
No interchange of X tending to infinity with n tending to infinity
is authorized by the displayed candidate. Do not use the conflicting
alternating formula (4.13) to choose the convention.

The desired downstream threshold is a one-sided bound
S_f(n)<=C_epsilon*exp(epsilon*n) for every epsilon>0, with each
C_epsilon independent of n. This is a proposed target, not an input.
L980 identifies the actual weak head H_n=lambda_n(sqrt(n)); its
unresolved lower control is the reason to examine the arithmetic
side. Even an exact formula for P_n would supply no such bound by
itself. The connection to a whole-Li criterion must retain L980's
error and L968's already sourced detection threshold.

First reuse the relevant arithmetic literature assessments; narrowly
screen local Li/prime-Laguerre records for this exact compensated
observable and any existing stop. Follow the primary source's
eta-moment reference for the fixed-index limit, then seek stronger
uniform statements and known obstructions. Do not repeat a general
Li bibliography search or the parked Coffey2007 access route. Its
theta-Laguerre source blocker is not a ban on independent arithmetic
targets, but an unavailable identity cannot be used as a premise.

The bounded discriminating test for the review is whether the sources
provide a quantitatively specified signed prime statistic and a
cutoff remainder that can be controlled without RH, with a concrete
intermediate estimate left to test. A formula alone, an equivalent
restatement of Li positivity, real-circle Fejer positivity at complex
nodes, or an assumed RH-strength prime-number error does not pass.
If only those are available, record the precise obstruction and
choose a materially different independently testable target. Do not
derive or approve new mathematics in the review turn.

L976's absolute inverse-envelope stop, L977's contour-majorant stop
and review200's real-phase limitation remain intact. This nomination
proposes keeping signed arithmetic cancellation; it claims neither
that it works nor that no previous source treats it. Essential local
context is L013/L018 and L977-L980; L968 is the downstream criterion,
not a positivity premise. Load L976 only for its exact recorded
obstruction if the source comparison reaches coefficient envelopes.

No justified creative proof target is ready yet. Prioritize finding
an independent sign mechanism in this bounded comparison, and use
proof_attempt/creative only if a subsequent approved target genuinely
has one with a decisive test. Otherwise do not relabel an identity
specialization creative. Mathlib coverage of the proposed statement
is unchecked and unknown. No result is added to the DAG.

## Completed comparison — step224, 10 November 2026

The main gap is unchanged: actual-Xi positivity in L030-L032/C032a,
or sufficient signed Li control through L968. The intermediate target
was an independent upper estimate for the compensated arithmetic
observable, with a uniform cutoff. It could help only if cancellation
were estimated rather than renamed. The bounded source test failed
to locate an admissible payment: an identity alone does not pass,
and the apparently quantitative cutoff lead below cannot be imported.
This is a source-selection negative, not a mathematical impossibility
theorem for the observable or a refutation of RH.

### What the primary sources actually supply

[Lagarias, published pp1708-1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21)
defines eta by (4.5) and uses the nonalternating binomial sum (4.8).
The unnumbered display after (4.13) states, for each fixed integer j>=0,

    eta_j = (-1)^j/j! * lim_(N->infinity)
        [sum_(m<=N) Lambda(m)(log m)^j/m
         -(log N)^(j+1)/(j+1)].

The same display is legible in [arXiv math/0404394v4, Section4](https://arxiv.org/html/math/0404394v4#S4).
The sum has full terms through integer N; no half-weight prime-power
endpoint is specified. The pole compensation is explicit. No rate
uniform in j or n accompanies that display. The conflicting alternating
remark (4.13) remains excluded by the L977 audit. These observations
fix the source contract; they do not establish the proposed combined
P_n formula, exchange its limits, or supply its sign.

[AppendixA, pp1737-1738](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=50)
gives Li test functions using L_(n-1)^(1)(-log x), a value n/2 at x=1,
and reciprocal cutoffs in the covariance form. It explicitly discusses
cancellation of divergent local contributions. This is not the
uncompensated trace form, nor a positivity theorem for these test
functions without RH. Its x=1 convention is not a justification for
half-weighting the unrelated prime cutoff N above.

For downstream use, reuse L980's imported arithmetic split, including
its +1 pole term and ordinary undivided normalization, and L968's
precise [Lagarias Thm2.4(2)/(2.21)](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=15).
That theorem requires every epsilon>0 and a constant uniform over
all indices. It cannot be paid by a fixed-index prime limit, a fixed
positive exponential rate, or a finite list of arithmetic signs.
No new equivalence proof is performed in this review.

### Original-reference access and the misleading uniform lead

Following the eta-moment reference reached E. Bombieri and J.C. Lagarias,
*Complements to Li's criterion for the Riemann hypothesis*, J. Number
Theory77(1999),274-287, DOI10.1006/jnth.1999.2392,
[author PDF](https://websites.umich.edu/~lagarias/doc/bombieri.pdf).
The PDF is reachable, but its text extraction is encoded as unreadable
glyphs. Screenshots of PDF pages2-4 and8 returned image placeholders,
not inspectable images; the alternate Michigan address failed and the
publisher PDF returned403. A local download also failed DNS resolution.
Thus no original numbered theorem or convergence proof was inspected.
Lagarias2007 remains a precise primary statement citation for the fixed
moment; this review does not falsely mark the 1999 proof as read.
Do not repeat this extraction route without materially new access.

The search also found S. Omar, R. Ouni and K. Mazhouda, *On the zeros
of Dirichlet L-functions*, LMS J. Comput. Math.14(2011),140-154,
[publisher PDF and retraction notice](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CF36DD3B48E5378D26C5EBB93FEA9A61/S1461157010000215a.pdf/on-the-zeros-of-dirichlet-dollarldollar-functions.pdf).
The notice says the retraction prevents use of incorrect mathematical
results. Section2, pp142-143, (2)-(6) was read: Theorem1 assumes a
primitive character of conductor q>1. Its subsequent cutoff argument
uses a Laguerre estimate stated only for x in [0,4(n+alpha)], then
claims a bound for an infinite tail. Neither that argument nor its
final cutoff estimate is imported. No claim is made that every result
in the retracted paper is false or that its cited polynomial bound
is false; that bound's original proof was not inspected. In particular
the paper supplies no certified zeta compensation or n-uniform bound.
This newly located exclusion changes the source-selection decision.

### Reuse, search scope and continuation

Queries included `Li coefficients Laguerre prime sum eta Bombieri
Lagarias`, `Laguerre S_2(n) Coffey primes bound`, the exact 1999 title
with PDF/Theorem3 qualifiers, and `Li coefficients prime Laguerre
unconditional` / `Li coefficients Laguerre cutoff remainder`.
The first theorem-number search was a discovery query, not an
assertion that the unread 1999 statement has that number. Generic
course pages, numerical reports, snippets and recent claimed RH
reductions were not theorem inputs. This was a bounded comparison,
not an exhaustive bibliography or novelty certification.

The duplicate/failure comparison reused reviews200 (real-circle
Fejer scope),203 (parked Coffey2007),204 (conditional coefficient
asymptotic),219/221 (completed residual sources), and the canonical
L977/L980 contracts. ATTEMPTS' step205 direct-source-payment and
step210 every-delta-envelope stops remain intact. L976's exact
Pringsheim obstruction is not an obstruction to a compensated
finite statistic; its proof was not reloaded or extended.

The separately nominated Cauchy-tail question needs only differences
P_n(Y)-P_n(X), so it does not require importing the inaccessible
moment proof or identifying the limit with S_f. Its downstream use
would be a controlled finite-cutoff interface for later signed
arithmetic work. It leaves the value and sign of that finite statistic
unpaid. A valid continuation must provide an explicit X_n and a
bound uniform in all Y>=X_n and n>=2, with the jump convention intact.
Abandon the chosen envelope if it cannot meet that threshold; mere
fixed-n convergence is not success.

The existing October baseline and external-input register were read
before this nomination. They contain stronger fixed-half-plane
information, not an already approved psi-error specialization for
this target. A future review must compare its exact applicability;
this turn derives no prime error from nonvanishing. A classical
unconditional PNT remainder may suffice for a nonoptimal cutoff,
without making an optimality or strongest-known-input claim.

A new primary lead is Daniel R. Johnston and Andrew Yang, *Some explicit
estimates for the error term in the prime number theorem*,
[arXiv:2204.01980v2, 20 April2022](https://arxiv.org/abs/2204.01980v2)
and [published Theorem1.1](https://www.sciencedirect.com/science/article/pii/S0022247X23004638).
The indexed theorem statement advertises a full-x psi error, but its
primary proof cases have not been retrieved, and its Laguerre-tail
specialization is unassessed. It is a lead for the next assessment,
not a new mathematical input certified here. The separate nomination
is REVIEW_REQUIRED. No justified creative sign mechanism is ready:
absolute-tail control would be an established-tool specialization.
Mathlib coverage of the proposed combined identity and uniform
estimate is unchecked/unknown. No lemmas, scripts, DAG edges or
PROOF assembly were changed.
