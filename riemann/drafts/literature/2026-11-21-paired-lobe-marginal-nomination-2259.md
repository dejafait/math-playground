# Nonnegative paired-lobe marginal: source review completed2260

TARGET: Assess joint log-concavity of a proposed nonnegative Tuck paired-lobe density as a marginal route to first-zero-removal log-concavity under review2256's kernel hypotheses.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact density/alternating-translates/difference/log-concavity searches and bounded local duplicate/failure checks; no matching theorem or obstruction identified. Actual queries and read limits: drafts/literature/2026-11-21-paired-lobe-source-notes-2260.md .
SOURCE_EVIDENCE: Reopened Tuck2006 pp133-135 equations(1)-(4), https://doi.org/10.1017/S0004972700047511 ; Prekopa1973 introduction and Theorems6-8/full proofs6-7 pp342-343, https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf ; newly inspected Boyd--Vandenberghe2004/2009 Sections3.5.1-2 pp104-106, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf ; reuse2257/2254/2249 calculus coverage.
COMPARISON: Tuck proves sine positivity; Prekopa requires joint log-concavity rather than supplying it for this density. Boyd--Vandenberghe supplies a Hessian criterion and warns of sum nonclosure. None of these inspected sources settles the paired difference-series or the first-zero restriction.
GAP: Convergence, positivity, the marginal identity and joint curvature remain unproved specializations. No source-derived obstruction or new density identity is claimed; the review identifies one fixed analytic directional-curvature test with ordinary tools covered.
REASON: The source comparison is complete for a bounded test, not a generic theorem. Nominate the fixed root-linked quartic log-cosh family in notes2260; its root alignment and strict curvature sign require a later approved mathematical attempt. No novelty follows from search misses.
LITERATURE_REASON: Completed review changes scope from the ready fixed quartic audit to the previously uncovered nonnegative marginal mechanism, including its joint-density and discrete-summation requirements.

## Completion2260

The nomination below is preserved as the pre-review record. Its unproved
claims remain unproved. Source coverage and one concrete continuation
are now recorded in [notes2260](2026-11-21-paired-lobe-source-notes-2260.md).
Outcome EXPLORATION: a new comparison/test nomination, without a new
mathematical sign, identity or theorem. Newly prepared continuation
coverage receives a separate supervisor approval next turn. No lemma
or mathematical script was changed or run.

## Exact nomination, with all mathematical claims unproved here

Retain review2256's hypotheses: K is even, positive and smooth on R,
(log K)''<0 everywhere, and for every m>=0 and B>0,
exp(B|u|)|K^(m)(u)| tends to0 at both infinities. Let x be the least
positive real zero of its half-line cosine transform, if one exists;
allow arbitrary multiplicity. Write a=pi/x. The density to assess is

    H_(K,x)(u,v) = sin(xv) sum_(j>=0)
        [K(u+v+2ja)-K(u+v+(2j+1)a)],
    u>=0, 0<v<a.

This displayed expression is a proposed object for source comparison,
not a proved representation or a claim of joint log-concavity. Review
whether a known theorem gives joint log-concavity in the continuous
variables(u,v), or a known obstruction excludes it under exactly the
stated hypotheses. Discrete summation is not automatically a
log-concavity-preserving operation. Convergence, nonnegativity, the
identity G_x(u)=x integral_0^a H_(K,x)(u,v)dv and the hypotheses of
any marginal theorem must all be justified in later authorized work,
rather than inferred from the word 'pairing'. The first-zero condition
must not be used as an unexplained curvature premise.

## Relevance and bounded continuation test

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. A genuine marginal comparison could address the missing
first-zero-to-curvature bridge; it would still leave actual-K
hypotheses, repeated strictness and the all-degree interface open.
This is a sufficient-condition nomination: a counterexample to joint
log-concavity of H would reject this representation-based mechanism,
not necessarily the original preservation statement or RH.

First perform one bounded exact-statement/stronger-theorem/obstruction
review, including the actual Tuck pairing proof and applicable
Prekopa marginal hypotheses. Search the notebook for duplicates of
this density before selecting a mathematical test. Continue only if
a precise theorem or one concrete, independently testable Hessian or
two-point inequality is identified with adequate source coverage.
An obstruction, unsupported discrete-mixture step, or dependence on
the desired invariant itself stops that mechanism in its assessed
scope. No generic proof, parameter search, numerical retuning or
new lemma is authorized by this nomination.

This is source preparation for a possible distinct central comparison
mechanism, not a protected creative proof attempt yet. No bounded
creative test with ready coverage has been established. Full matching
Mathlib coverage is unchecked. Essential continuation inputs are
review2256's exact kernel hypotheses and notes2257/2254's primary
comparisons; C919s supplies only the completed fixed negative test,
not a premise about this proposed density. No cross-notebook input.
