# Fixed CM analytic enclosure specialization

TARGET: Prove a fixed CM analogue of L027 for y^2=x^3+1 at p=7 using Balakrishnan--Muller--Stein Proposition 2.9 and L056's exact symbols, retaining the primitive normalization and finite-error bound without L004.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact queries, primary comparisons, duplicate search and failure review in drafts/literature/2026-10-13-cm-quadratic-enclosure-scope.md; no separate mathematics was performed for this continuation.
SOURCE_EVIDENCE: Balakrishnan--Muller--Stein, Math. Comp. 85 (2016), Section 2.1 pp.987--990 and Section 2.2 pp.991--993, Proposition 2.9 with complete proof and equations (2.4), (2.6)--(2.9), https://wstein.org/papers/mcom3029.pdf#page=10; Stein--Wuthrich Lemma 3.2, Corollary 3.3 and Proposition 3.5 pp.1763--1765, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=7; L027 and L028's relevant full precision/orientation proofs inspected.
COMPARISON: The general-newform source covers convergence and the same coefficient bounds without excluding CM; L052 supplies its running differential-scale-one premise. Fixed applicability and reuse of L027's elementary bookkeeping remain to be written.
GAP: No canonical CM specialization, actual finite coefficient or nonvanishing exists; L004's non-CM implication and the independent arithmetic/complex-order gaps remain outside this target.
REASON: A fixed analytic corollary documents the changed source input before executable coefficient work; reprove no measure theorem and generalize no arithmetic rank implication.
SCOPE: Fixed minimal y^2=x^3+1, N=36, p=7, t=-4, total real Neron period, primitive untwisted trivial branch, kappa(gamma)=8; exact S(r)=F({infinity,r}) from L056, denominator 12 and C=0, n>=2, rational unit u congruent t modulo 7 with residual valuation at least M>=1.

Reuse [the completed source comparison](2026-10-13-cm-quadratic-enclosure-scope.md)
without additional browsing unless a hypothesis or essential input changes.
This assessment is newly written after the literature comparison and
receives separate supervisor approval next turn. No research was run.

The main gap is arbitrary-curve rank equality for analytic order >=2.
The intermediate target is the fixed conditional analytic enclosure
v_7(a_2-b)>=min(n-1,M), where b is L027's complete finite-polynomial
expression, not an evaluation. A later bounded coefficient calculation
would test min(n-1,M)>v_7(b). Neither nonvanishing nor termination
is approved here.

Essential inputs: L027's monic-division, uniform-tail and root-precision
bookkeeping; L028's orientation identity (5); audited L038 N=36 full
integral domain; L050's minimal model/newform; L051's total-period
contract; L052's optimal degree-one differential scale and complete
seven-point count; audited L056 exact full-relative functional and
denominator 12. L004/foundations/05 are scope contrasts only, not
arithmetic inputs to the CM corollary. No cross-notebook input.

Cite Proposition 2.9 rather than silently remove Stein--Wuthrich's
standing hypothesis. Verify optimality and the running c_A=1 using
L052, total-period normalization and S(r)=F({infinity,r}); a reverse
path requires negation without changing the table. State good ordinary
eligibility and uniform C=0. Reuse L027's precision proof while leaving
its original non-CM statement unchanged, retaining zero polynomials,
the closed-lattice limit, all binomial terms, the root residual class
and unit derivative. A fixed canonical corollary may grant n,u,M:
no numerical finite sum or mathematical script is part of this target.

Continue if the full bound follows with these inputs and no unstated
period or analytic hypothesis. Otherwise preserve the attempt and
isolate the failed source/application step. Uniform useful coefficients,
lower vanishing, rational directions, divisible/full Sha and
complex-order comparison remain missing. No full matching Mathlib
coverage is checked; retain that qualification in the corollary.
Classification is REPRODUCTION of known precision bookkeeping.
