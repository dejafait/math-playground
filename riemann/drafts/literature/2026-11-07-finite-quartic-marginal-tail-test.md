# Finite quartic ferromagnet marginal — tail discriminator nomination

TARGET: Test whether every fixed finite zero-field quartic ferromagnet with a nonzero nonnegative linear observable X satisfies P(X in [t,t+1])>=c exp(-C(1+t)^4) for all sufficiently large t, and compare this threshold with L019 to decide whether its law can equal K(|u|)/(2M_0).
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped finite-quartic/hidden-site/marginal-tail searches found no matching local result; exact external quartic-marginal lower-bound and polynomial-potential/Gibbs-tail searches found no adequate matching theorem. Failed searches establish no novelty. Source evidence and queries are in the completed block-spin review.
SOURCE_EVIDENCE: Simon-Griffiths CMP33(1973),145-164, Section2 definitions, Theorem1 and complete proof pp148-151, Theorem3 and proof pp151-152, Theorem4 and proof pp152-153 inspected in the primary author PDF; Aizenman arXiv:2112.04248v3 Section9.1/(9.1)-(9.7) identifies finite quartic graphs. L019-L021 read for the full theta law. No inspected source states the selected lower bound or theta comparison.
COMPARISON: Known construction/Lee-Yang theorems explain why this model class is relevant if realized. They do not show actual-theta realization or decide the marginal-tail test. This elementary class analysis differs from L876's operator and the GHS determinant; no reproof of Lee-Yang or quartic Ising approximation is needed.
GAP: Establish the interval-mass lower bound with model-dependent positive constants, including dimension one and a single nonzero observable weight, and rigorously compare the full-theta tail. Neither bound nor mismatch is proved by this assessment.
REASON: An independently testable prerequisite replaces unparameterized GS realization and repeated source access. It can decide whether exact finite-quartic hidden-site fitting warrants work, while leaving dimension-growing GS limits open. Newly written ready coverage needs separate approval next turn.
SCOPE: One bounded analytic calculation for each fixed model, uniformly in t only. No fitted moments, numerical tail matching, arbitrary-spin or infinite-dimensional extension, or all-degree sign claim.

Main gap: L030-L032/C032a actual-Xi mixed positivity. The intermediate
target is exactly TARGET. Downstream use: screening a concrete class
which could admit Lee-Yang transfer if it represented the theta law.
An obstruction would end exact finite-class fitting, not solve RH. A
failure of the bound must specify the failing model or hypothesis;
it is not itself a theta realization.

Fix n>=1. The vector phi in R^n has normalized Lebesgue density
proportional to

    exp(-sum_i a_i phi_i^4 - sum_i b_i phi_i^2
        + sum_(i<j) J_ij phi_i phi_j),

with every a_i>0, every b_i finite real, and every J_ij>=0 finite.
There is no field or singular constraint. Set X=sum_i w_i phi_i with
finite w_i>=0, not all zero. Proposed c,C>0 and onset t_0 may depend
on every model parameter and n,w. No constants are assumed uniform
across models. The lower bound itself is the unproved target.

Essential input IDs: L019 supplies the complete K tail envelope;
L020-L021 identify its normalized even law and entire transform. The
new finite-model interval bound and comparison are unproved. L030-L032/
C032a are the downstream gap, not established positivity premises.
No cross-notebook input is proposed. Source scope is recorded in the
completed block-spin assessment and its
[primary PDF](https://math.caltech.edu/SimonPapers/47.pdf). Continuous
zero-coupling cases should not be silently attributed to a theorem
worded for positive couplings; no such applicability deduction is
required as an input to the interval-mass calculation itself.

Continuation/abandonment test: establish or refute the bound and carry
out the full-theta comparison in one attempt. If equality is excluded,
close exact fixed finite-quartic fitting; do not sweep parameters to
evade the result. If inconclusive, preserve the precise failed estimate
and require a new independently testable idea before extending it.
Neither outcome controls dimension-growing limits, other site laws,
approximation-level transform convergence or Xi mixed signs. Finite
moments and weak convergence alone supply no signed conclusion.

This is a standard analytic calculation, not a central creative attempt
or a novelty claim. The EXPLORE nomination was written during a
literature-only turn and requires separate supervisor approval before
invocation. A later proof should cite standard construction and fully
document its interval/tail argument canonically. Full matching Mathlib
coverage is unchecked.
