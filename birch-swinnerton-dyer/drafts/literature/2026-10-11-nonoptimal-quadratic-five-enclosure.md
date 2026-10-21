# Nonoptimal-model coefficient test — separate scope approval

TARGET: Produce a finite L027 quadratic-coefficient enclosure for E=[0,-1,1,-7820,-263580] at p=5 using audited L046 symbols and C=0, certifying non-CM, good ordinarity, Teichmuller residues and unit-root precision, testing n=2,3,4 with M=n+1 and stopping at the first strict bound min(n-1,M)>v_5(b).
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact discovery queries and inspected coverage in the 2026-10-06 primitive-error/finite-error and 2026-10-10 conductor-eleven p=7 enclosure/audit assessments; searched L027/L039/L042/L045/L046 and named 2026-10-11 transfer/production/audit records for the target equation, p=5, residual restrictions and duplicates; read ATTEMPTS/022--024. New queries included “Stein Wuthrich 11a2 5 p-adic L series modular symbol ordinary nonoptimal”, “site.math.mit.edu 18.783 isogenous endomorphism algebras complex multiplication” and “site:math.mit.edu/classes/18.783/2025 isogenous End”. No complete exact-target certificate was located; no novelty is inferred.
SOURCE_EVIDENCE: Reopened Stein--Wuthrich, Math. Comp. 82 (2013), Section 3 pp.1761--1766, Propositions 3.1/3.5, Corollary 3.3 and essential proofs, ordinary-root passage and multiplier, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6; Conrad, Hensel's Lemma, Theorem 4.1 printed p.6, undated live PDF, https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6; inspected Sutherland, MIT 18.783 Spring 2015 Lecture 13 (19 March 2015), Theorem 13.18 with proof and Corollary 13.20 pp.7--8, https://math.mit.edu/classes/18.783/2015/LectureNotes13.pdf#page=7, on 2026-10-11. Reused audited L039/L043/L045/L046 and their unchanged primary quotient/period coverage.
COMPARISON: Known ordinary finite-polynomial convergence/error control and audited L027 cover this enclosure without optimality, non-anomalous or residual-irreducibility hypotheses; L046 supplies the target's full normalized functional and denominator two, hence C=0 at five. Known isogeny invariance covers the non-CM prerequisite using L039 and L046. L042's numerical values and p=7 constants do not transfer.
GAP: The future attempt must record non-CM applicability and verify actual target good ordinarity, finite residues/root residuals, every symbol path and exact b with a strict L027 bound. No source guarantees success at n=2,3,4; rational points, Sha and complex-order comparison remain unresolved.
REASON: This separate literature-only step removes the changed-model/prime source gap and approves one bounded known-method reproduction with complete independent replay; no new lemma, coefficient evidence or rank-two inference is produced or authorized.
LITERATURE_REASON: The target changes the curve, normalization and prime from the existing p=7 production assessment; its p=5 use is outside that assessment's approved scope.
SCOPE: Only the exact TARGET above; model [0,-1,1,-7820,-263580], level 11, p=5, primitive untwisted trivial branch, total minimal real Neron period, kappa(gamma)=6, audited L046 F_E=phi and all-level C=0; n=2,3,4, M=n+1, non-CM and good-ordinary checks before ordinary coefficient inference, and complete independent replay. No extension to L026's arithmetic hypotheses, another curve/prime or a larger schedule.

Main gap: arbitrary analytic order at least two versus rational rank.
Intermediate target: one finite coefficient enclosure on the explicit
nonoptimal target using the full normalized functional already produced.
Downstream use: test L027's strict coefficient threshold after isogeny
transfer, including the prime five omitted by L043's earlier C=0
specialization. No rank inference from a quadratic coefficient alone is
permitted, and no central or lower-coefficient vanishing is assumed.

Essential inputs for the approved attempt: L027's complete enclosure and hypotheses;
L039 source arithmetic and full-relative presentation; L043 normalization
with its published optimality qualification; L045 common-form/period
transfer; L046's separately audited target minimality and all twelve
values. Existing L042 p=7 production and its assessment are method
comparisons, not numerical inputs at p=5. Their relevant source/proof
ranges and producer/verifier interfaces were inspected in this separate
review. No mathematical script was run or modified.

Unresolved finite obligations: record the cited non-CM application and
audited common-form normalization, verify good ordinarity at five before
using the ordinary measure, and certify every finite path, residue, unit
root and precision inequality. Approval of source coverage is not
execution of these checks. L046 proves C=0 at odd primes, but supplies
no coefficient or finite root/residue evidence.

Continuation test for the separately approved attempt: stop at the first certified strict
bound, or record the complete failed bounds after n=2,3,4 and park this
finite schedule. No success is predicted. A failure of an essential
arithmetic hypothesis stops the ordinary attempt before coefficient
calculation. Rational points, Sha and complex-order comparison remain
independent gaps even if the finite threshold succeeds.

## Primary hypotheses and essential cases

[Stein--Wuthrich, Section 3, pp.1761--1766](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6)
assumes non-CM curves, uses the total real Neron period, permits odd
good-ordinary primes and fixes the 1+p coordinate. Proposition 3.1 gives
coefficientwise convergence, Corollary 3.3 the adjacent monic divisor,
and Proposition 3.5 the adjacent coefficient bound. The character-coset,
divisibility and monic-divisor proof cases were read. Section 3.3 fixes
the unique unit root. Optimality concerns period recovery, not these
statements; non-anomalous reduction is not required. Proposition 3.7's
separate integrality result assumes irreducible E[p] and is unused here.
Retain (3.2)'s ordinary multiplier (1-alpha^(-1))^2, including any positive
valuation. Reuse L027's audited all-level-C/closed-lattice argument,
not the source's final two-depth tail constant or Lemma 3.6's incompatible
ordinary-root wording. No convergence theorem is reproved.

[Conrad, Theorem 4.1, printed p.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6)
requires f in Z_p[X], x in Z_p and |f(x)|_p<|f'(x)|_p^2. It gives
the unique nearby root and exact distance |f(x)/f'(x)|_p. L027 already
contains the simple-root applications to X^2-tX+p and X^(p-1)-1;
the future finite checks at five use X^2-tX+5 and X^4-1. No numerical
root or residue is computed by this review.

[Sutherland, Spring 2015 Lecture 13, Theorem 13.18, p.7](https://math.mit.edu/classes/18.783/2015/LectureNotes13.pdf#page=7)
states isogeny invariance of rational endomorphism algebras; its proof
and Corollary 13.20's endomorphism-rank statement were inspected. Apply
over an algebraic closure of Q to L046's audited Q-rational isogeny,
with L039's geometric non-CM result. This supplies the known prerequisite
test for the later application, not a new CM criterion or equality of
integral endomorphism rings. No degree-prime-to-p hypothesis enters this
characteristic-zero application. L045/L046 already identify the common
normalized newform and full-relative total-period transfer; retain their
audits and published source-optimality qualifications without reproof.

## Exact finite implementation obligations

Bind complete L039 structural/dual evidence, L043 normalization and its
audit, and L046's certificate and separate audit. L046's producer stores
the target equation/invariants and twelve values in transfer.target_values,
with common_denominator=2, rather than the old L041 schema. Reconstruct
F_E=phi from the actual three-dimensional quotient coordinates and
check every generator value. Hashes and success flags alone do not
replace complete relevant upstream evidence.

L042's producer/verifier is methodology only: its p=7, gamma=8, source
equation, Delta=-11^5, scale 1/5, denominator ten, six residue classes
and L041 schema all require changing. Future artifacts belong in a fresh
scripts/conductor-eleven/quadratic-five/ directory; preserve existing
bytes. No producer was executed during this interface comparison.

First certify the target's good reduction from L046's own minimal-model
invariants and an exhaustive target point count at five, including
infinity. Distinct replay must enumerate the target equation itself.
Report t=6-#E(F_5) and require 5 not dividing t; no source point-count
rows or reduction of the degree-five map may substitute. Record the
cited non-CM application before invoking the ordinary enclosure.

At each n save all four integers 1<=w<5^n with w=d mod 5, w^4=1 mod
5^n and unit derivatives. Supply exact rational unit u=t mod 5, residual
v_5(u^2-tu+5)>=M=n+1 and unit derivative. Use L027's least-positive
residues w*6^j mod 5^n and both S(r/5^n), S(r/5^(n-1)); retain all
j=0,...,5^(n-1)-1, every binomial(j,2) and zero terms. Required terms
are 4*5^(n-1). Save all ordered oriented paths, determinant-one lifts,
Gamma_0(11) reductions, raw vectors, full quotient coordinates and
L046 evaluations. Distinct replay reconstructs every finite input and
the complete rational sum independently of saved aggregates. Apply
L027's existing limiting bound without changing period or multiplier,
discarding large-j summands, or assuming a_0=a_1=0.

## Duplicates, exclusions and bounded decision

L033 and L042 certify other model/prime pairs; targeted local searches
found no completed enclosure on this nonoptimal model at five. The new
web search returned software examples and unrelated leads, not an
inspected exact-target certificate. Search snippets are not certificates.
The earlier discovery assessment supplies the known stronger general
finite-polynomial method; lack of an exact-instance match implies no
novelty. ATTEMPTS/022--024 park conditional repetition without input
production and the uniform twist-source blocker. Actual audited L046
inputs make this finite downstream test independently discriminating;
those stops and the uniform-source blocker remain parked.

L026 separately requires residual surjectivity, a non-anomalous prime
and other arithmetic/residual-family, central-vanishing and sign premises.
They are outside this approval. In particular the rational degree-five
isogeny prevents silently assuming residual surjectivity at five. A
successful quadratic certificate alone gives neither p-adic order two,
rational rank two, Sha finiteness nor complex order. No such inference
or new obstruction theorem is attempted here.

Require complete replay and N=min(n-1,M)>v_5(b), with v_5(0)=infinity;
stop at the first success. Failed prerequisites park the ordinary attempt
with evidence retained. If n=2,3,4 all fail, retain every actual/required
bound and reassess before extending the schedule. An enclosure containing
zero establishes neither vanishing nor nonvanishing. Full matching and
supporting Mathlib coverage remain not checked; unknown is not absence.

The original proposal was REVIEW_REQUIRED. Step
BSD-2026-10-11-153-nonoptimal-five-enclosure-source-approval separately
completes SPECIALIZE coverage for the unchanged TARGET, permitting
REPRODUCTION in a later research turn. No lemma, mathematical script,
new arithmetic result or coefficient is produced here.

The current [Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
still links [Wiles's official statement](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
Its printed p.2 rank assertion and separate Remark 1 refinement were
rechecked on 2026-10-11 and agree with foundations/01. Target scope is
unchanged. An initial retrieval at the incorrect /2022/06/ URL failed;
the current page's actual /2022/05/ link was successfully followed.
