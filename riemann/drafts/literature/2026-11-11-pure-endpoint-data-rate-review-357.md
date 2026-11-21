# Pure-endpoint data-rate test — source nomination

TARGET: Assess source coverage for the theta=1 pure-endpoint complete-response lower-rate test at gamma=2, requiring a rate rho>13/64 and paid endpoint and other-branch errors.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate literature-only step358 reused reviews344/345/347's exact-family search and scoped failures; newly searched analytic endpoint-weight/Bessel integral asymptotics and modified-Bessel large-order complex-argument terminology. Inspected the primary DLMF statements below; no matching complete-response lower-rate theorem was identified and no originality is inferred.
SOURCE_EVIDENCE: Reused Vanlessen https://arxiv.org/pdf/math/0504604v2 (29 August 2005), Theorem2.4(b),Proposition3.31,Theorem3.32,Proposition5.1/(5.5)-(5.6), with audited C997e/o; newly read https://dlmf.nist.gov/2.4#iii and #iv, (2.4.10)-(2.4.16), https://dlmf.nist.gov/10.32#E2, and https://dlmf.nist.gov/10.41#iii with (10.41.3),(10.41.7)-(10.41.8). Reused review347's inspected Cauchy, complex Gaussian and dominated-convergence proof contracts.
COMPARISON: Standard saddle tools and exact holomorphic amplitudes cover a bounded fixed-theta specialization; the Bessel identity and large-order expansion concern a plain scalar endpoint transform and do not dispose of the nonconstant exact amplitudes or competing response. C997o removes the former domain gate. C997m's large-theta estimates are not imported at theta=1.
GAP: The later attempt must verify the fixed saddle's nondegeneracy and dominant real part, nonzero limiting amplitude, both vertical endpoint costs and outer pieces, the other Laguerre branch, normalization and every complete remainder on the same exponential scale, then compare the resulting rate with 13/64. None is newly proved here.
REASON: Essential source coverage is now ready for the exact bounded test below; only its local quantitative hypotheses and response comparison remain mathematical work. SPECIALIZE authorizes that later attempt, not its conclusion. This changed ready continuation requires separate supervisor approval next turn.
LITERATURE_REASON: The saved theta=1 pure-endpoint rate target was REVIEW_REQUIRED; its complete-response scope and possible scalar-Bessel shortcut had not been compared, although general tools were ready. No repeated domain audit or blocked-source retry was needed.
SCOPE: Integer n>=2,delta=1/8,J=[15/8,17/8],nu_n from C997n(1),theta=1,gamma=2; complete C997c(1) response with both slope endpoints,both Laguerre branches,both beta signs,both short intervals and K's -1. Fixed parameters before n; no actual zeta-zero realization.
COVERED_TARGET: Test C997n(4) at theta=1 and gamma=2 using C997o's fixed domain, proving a complete pure-endpoint lower rate rho>13/64 with nonzero leading term and paid endpoint and competing-response errors, or record an informative obstruction.

The proposed later mathematical discriminator is exactly C997n(4):
find some fixed rho>13/64 and an unbounded integer subsequence with
|H_n^+(2;nu_n)|>=exp(rho*n), or identify a rigorous obstruction to the
proposed asymptotic. Failure to prove that lower bound is inconclusive.
Together with the audited C997n(3), success would stop only the fixed
theta=1,lambda=A/128 compensated subfamily; it would not settle RH or
the general point bridge. No rate or saddle inequality is derived here.

Reuse the already inspected primary bulk contracts and the duplicate
comparisons in reviews345/347/350. Before any calculation, compare the
exact pure-endpoint integral with standard terminology and stronger
known results, and inspect the relevant theorem hypotheses and proof
cases of any essential new asymptotic tool. Do not repeat the fixed-lens
audit or retrieve primary passages without a concrete scope need.
If the elementary Cauchy/Gaussian tools already inspected suffice,
record precisely why, including nondegeneracy, contour branches,
endpoints, a common asymptotic scale and every competing response term.
No previously unpaid nonvanishing or dominance claim becomes an input.

The previously nominated stationary point is the one in review350,

    s=delta^2*beta/(1+sqrt(1+delta^2*beta^2)), beta=1/8+i,

with positive-real-part square root. This is an existing proposal, not
a new stationary-phase computation. Read only the needed C997o domain
statement and canonical proof ranges when assessing its use. Essential
later inputs are C997n(1)-(4), C997o's audited exact-amplitude domain,
C997e(4),(15)-(16), C997c(1),(5), and C997m(2) for retention. L997 is
used through the existing complete-response contracts. C997i's degree
restriction and C997m's theta>=Theta_0,lambda>=A leakage restriction
must retain their scopes; a historical stop is not a global ban.

Main gaps remain L030-L032/C032a actual-Xi positivity, L966/L968 signed
forcing and unpaid L984(H). The point bridge, selected/both-sign
transfer, C997a(8), original assay/reconstruction, signed recovery,
complements, regulators and L993 remain open. Matching Mathlib coverage
is unchecked and unknown. No cross-notebook input or RH candidate.
The source review must separately approve a subsequent mathematical
target; this nomination does not authorize uncovered mathematics.

## Separate source comparison — step358, 11 November 2026

The preceding nomination is historical. This separate source turn
assesses its unchanged rate question and nominates only the exact
COVERED_TARGET above. No saddle inequality, lower rate, nonvanishing
claim or new mathematical lemma was derived during this review.

### Discovery and inspected source scope

Queries were `"asymptotic" "integral" "(1-x^2)" "analytic" "Bessel"`,
`"Laguerre" "endpoint" "Gaussian" "compensated" asymptotic integral`,
and `site.dlmf.nist.gov modified Bessel integral (1-t^2) large order
complex z Debye`. Reused the exact-family queries recorded in review344
rather than repeating them. New search hits were leads, not theorem
evidence. No matching complete-response result was found in the sources
actually inspected; that is neither an exhaustive search nor novelty.

NIST DLMF live pages were read on 11 November 2026; this turn did not
independently verify their release identifier. Read the following
hypotheses and cases, not just snippets:

- [Sections2.4(iii)-(iv)](https://dlmf.nist.gov/2.4#iii),
  (2.4.10)-(2.4.16), assume analytic phase/amplitude along the path
  except possibly at its ends, local convergent expansions, absolute
  uniform convergence at the far endpoint and a strict real-phase
  gap away from the contributing point. The parameter lies on a ray
  or sector of width less than pi; local power branches are fixed by
  the path direction. The interior-point discussion splits at that
  point: nonstationary contributions cancel in the two expansions;
  a simple stationary point gives (2.4.15), with leading coefficient
  (2.4.16) and a specified square-root branch. An exact steepest path
  is unnecessary. These statements do not supply our contour dominance
  or nonzero amplitude. The displayed theorem uses a fixed amplitude;
  it is not an automatic uniform theorem for our n-dependent amplitudes.
- [Equation10.32.2](https://dlmf.nist.gov/10.32#E2) expresses I_nu(z)
  by the integral of (1-t^2)^(nu-1/2)*exp(zt) over [-1,1], with
  Re(nu)>-1/2 and complex z. It covers the scalar endpoint transform,
  but the complete packet has nonconstant holomorphic amplitudes and
  a second oscillatory branch. Removing those factors is not licensed.
- [Section10.41(iii)](https://dlmf.nist.gov/10.41#iii), with
  (10.41.3),(10.41.7)-(10.41.8), supplies large-positive-real-order
  expansions for I_nu(nu*z), uniformly in closed sectors strictly
  inside |arg(z)|<pi/2. Fractional powers continue from the positive
  real axis. This is stronger than a fixed-order Bessel asymptotic,
  but still concerns a scalar special function. No weighted-amplitude
  comparison or cancellation bound for our complete response follows
  merely by citing it. No Debye estimate is used in this turn.

Olver's book pages and Boyd's error-bound papers referenced by DLMF
were not newly read and are not new imported proof inputs. The Bessel
search hits outside these inspected pages also remain unread leads.
They are nonessential: the already inspected elementary limit proof
contracts permit an attempt without a growing-order special-function
theorem. Pritsker-Varga's access failures from review344 remain parked.

### Reuse, applicability and the difference still to prove

Reuse review347's complete inspection of Vanlessen v2, printed
pp5-7,32-34,39: alpha=2>-1, Q=x with positive leading coefficient,
N=n+1 and beta_N=4N. Read C997e(4),(15)-(16) and C997o's hypotheses,
conclusion and domain qualification. The exact two-branch identity and
holomorphic O(1/n) amplitude convergence are available on C997o's
fixed U, including the entire nominated rectangle K, uniformly for
real u in [0,2]. The n>=63 containment certificate is not an effective
asymptotic onset. No enlarged lens, variable parameter or continued
real-axis remainder is being assumed. The general Riemann-Hilbert
theorem should be cited, not reproved.

Reuse review347's inspected DLMF1.9.29-31/1.10.1-3 Cauchy and local
series contracts, DLMF7.7.3 complex Gaussian formula, and Axler,
*Measure, Integration & Real Analysis*, author version12 June2026,
Theorem3.31 pp92-93 (finite- and infinite-measure proof cases), with
the complex extension after6.22 p157. These require analyticity on
the deformation, an integrable majorant after rescaling, almost-
everywhere convergence and a quadratic coefficient with positive
real part for the Gaussian integral. They suffice to justify a
leading-term specialization with uniformly converging exact amplitudes
once the local phase and domination estimates are supplied. Such a
direct local limit is needed to pay the amplitude dependence and
complete-response errors; it is not a reproof of a general saddle
theorem. No higher-order asymptotic expansion is needed for the target.

Read C997m(11)-(12) for the complete-response separation and its
(15)-(21) proof for the precise large-theta restrictions. C997n(1)-(4)
specifies the pure-endpoint comparison and the paid correction.
C997c(1),(5) retains the full lower interval in original variation.
All these contracts are reused with their hypotheses; replacing the
real weight in an exact response and charging its terms remains part
of the subsequent mathematical proof, not a conclusion of this review.

The later bounded attempt must establish, rather than assume:

1. The nominated stationary point is simple, its local logarithm
   exponentiates to the integer endpoint polynomial, and a central
   contour through it has a strict Gaussian real-part bound.
2. The limiting minus amplitude from C997e is nonzero at that point;
   the complex Gaussian branch and the original N_n normalization
   give a nonzero coefficient. Nonvanishing near c=2 from the
   large-theta argument does not automatically cover a fixed point.
3. Both vertical endpoint segments and all horizontal outer pieces
   are bounded below the same leading exponential scale. Endpoint
   zeros on the real axis do not erase vertical segment costs.
4. The plus Laguerre branch is smaller on the deformed contour, or
   any same-scale contribution is explicitly combined without an
   assumed lack of cancellation. Both beta signs, both short intervals
   and K's -1 remain in the response; the known original-TV remainder
   must be compared with the achieved leading scale.
5. The resulting COMPLETE lower logarithmic rate strictly exceeds
   13/64 on an unbounded integer subsequence. An isolated numerical
   saddle value, scalar transform or upper bound does not establish it.

These are explicit mathematical tests, not missing external theorems.
If any fails, record the failed hypothesis or new obstruction; an
unpaid estimate alone is inconclusive. No successful asymptotic, new
rate inequality or analytic nonvanishing is asserted in this assessment.

### Duplicates, stops and decision

Reused reviews344/345/347/355's C997f/g/i/l comparisons and
failures340/341. C997i requires actual degree<=n and its stated
large-A regime; C997m's leakage uses theta>=Theta_0,lambda>=A.
Neither proves the nominated theta=1,lambda=A/128 stop. Read the
strong-taper ATTEMPTS record347 and its step349 audit annotation;
retain that stop on its actual scope. No stopped parameter regime
is reopened. C997o repairs only domain coverage; C997n pays only
the correction. Neither closes the present lower-rate gap.

SPECIALIZE is ready for one later REPRODUCTION attempt using the
standard tools above; a citation alone does not decide the prescribed
complete response. The exact COVERED_TARGET is the sole proposed
continuation, subject to the supervisor's separate approval. This
source review is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, not
mathematical progress beyond those sources. No essential source is
blocked; more browsing without a changed hypothesis is unwarranted.
No justified new central creative mechanism was developed here;
the prepared continuation is established-route development.

Success would stop only this fixed compensated subfamily through
C997n(3)-(4), retaining C997m(2)'s target retention. All main and
independent gaps listed in the nomination remain unpaid. Matching
Mathlib coverage is unchecked and unknown. No cross-notebook input,
new lemma, mathematical script, DAG edge, PROOF.md change or RH
candidate is involved.
