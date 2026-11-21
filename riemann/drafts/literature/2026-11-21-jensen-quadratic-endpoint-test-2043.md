# Fixed N=6 Jensen/quadratic compatibility test — prepared continuation2043

TARGET: Test at N=6 whether R_6=J_6((1+4t^2)A_8)-(1+4t^2)J_6(A_8) has zero p_2,p_3,p_4 coefficients, using C029m's exact u_0,...,u_8 and fixed C029n enclosures, and verify J_6((1+4t^2)A_8)=T_6.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact-target review2043 in 2026-11-21-jensen-quadratic-endpoint-review-2042.md searched Kuznetsov/Jensen/quadratic, Pollaczek intertwining/boundary and diagonal commutator terminology; compared C029n/q/r/s/t and completed local-sign/evolution/inverse assessments. No matching actual-coefficient cancellation theorem or completed duplicate was found; no originality claim.
SOURCE_EVIDENCE: Kuznetsov, Canadian Mathematical Bulletin51(4)(2008),561-569, (2)/(4), p563, (9)/(10), p564, (13), p566 and weighted discussion pp568-569, https://doi.org/10.4153/CMB-2008-055-0 ; exact passages and complete relevant coefficient-conversion proof inspected in review2043. C029m gives the full family; C029n supplies the normalization and fixed rational-enclosure proof. No asymptotic or auxiliary hyperbolicity theorem is needed.
COMPARISON: Known identities permit finite coefficient formation, but do not give the three required cancellations. The test differs from the failed metric, affine residual and fixed inverse tests. Citation suffices for the basis and coefficient formulas; an actual-coefficient compatibility certificate is the identified remaining task.
GAP: No R_6 coefficient or finite numerator equality has been certified. Even a pass supplies no signed index effect, auxiliary hyperbolicity, degree-uniform estimate or RH transfer.
REASON: Test one finite necessary condition before investing in an endpoint-only signed-defect mechanism. A single certified nonzero bulk coefficient rejects this ansatz at N=6; a pass merely keeps the compatibility question open.
SCOPE: Prepared during literature-only review2043, requiring separate next-turn approval under the supervisor gate before execution. Only the fixed N=6, q=1+4t^2, actual u_0,...,u_8, original Jensen weights and existing 60-decimal enclosures are covered. No calculation was performed in preparing this file.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity;
the relevant conditional branch C029m still needs an eventual Hermite
negative index at most one. The proposed intermediate target is a
finite coefficient compatibility condition, potentially prerequisite
to a later endpoint-only signed-defect argument. This possible use
does not assume such an index argument exists.

Use C029m's p_k and u_k, retaining all odd terms. Put

    q(t)=1+4t^2,
    A_8(t)=sum_(k=0)^8 u_k p_k(t),
    w_k=6!/((6-k)!6^k) for 0<=k<=6,
    J_6[p_k]=w_k p_k for k<=6, J_6[p_k]=0 for k>6,
    R_6=J_6(q A_8)-q J_6(A_8).

The threshold, fixed before computation, is

    R_6 in span_R{p_0,p_1,p_5,p_6,p_7,p_8}.

Verify the finite numerator identification J_6(q A_8)=T_6 against
C029m's full beta_k from source(4). Do not substitute the source's
a_k or Proposition4.2's damped coefficients for u_k. Equation(10)
explains their distinction and is not permission to add an unproved
finite affine correction. For bottom indices use recurrence(2)
directly rather than an undefined negative-index polynomial.

Use the constant S=sin(pi/8)/sqrt(2)>0 of C029n. Its existing
half-angle reduction permits working with u_k/S, beta_k/S and R_6/S
in Q(sqrt(2))[pi]. A zero or nonzero assertion is unaffected by this
fixed positive normalization. Use the same Bernoulli convention and
u_0,...,u_8 source formula; C029n's exact table reaches B_18. No
coefficient fitting, N-dependent normalization or precision increase.

Construct all expressions by finite exact arithmetic. Independently
compare the multiplication obtained from source(9) with multiplying
the polynomials built from source(2), including k=0,1. Save every
normalized u_k, basis polynomial, weight, q A_8 coefficient, both
terms of R_6, its full coefficient vector and the numerator-identity
residual. Check the numerator equality exactly in the stated field.
For each of p_2,p_3,p_4 record an exact-zero certificate if it vanishes
formally. For a nonzero coefficient expression at pi,sqrt(2), use
C029n's unchanged rational intervals and exact interval Horner
arithmetic to separate its value from zero; a nonzero formal polynomial
alone does not prove its value at these constants is nonzero.

Save a complete certificate and reproduction script under
scripts/pollaczek/, with all rational endpoints and failures. Print
only actual/required bounds, conclusion, failures and artifact paths.
Inspect the complete relevant values, not just a preview, before
reporting a sign. A normalized coefficient interval strictly above or
below zero is decisive against the threshold. Three certified zeros
constitute only a finite pass. An interval containing zero without
exact cancellation is inconclusive. A failed numerator identification
is a normalization/implementation failure, not evidence against RH.
Stop after this one fixed test: no degree sweep, root count, precision
campaign, fitted correction or uniform-sign derivation is covered.

C029m and C029n are essential inputs; C029q/r/s/t are failure contrasts,
not premises. Auxiliary hyperbolicity, signed effects, all-degree and
actual-degree control, initialization, and the analytic weighted limit
including upstream[9] remain unresolved. No cross-notebook theorem or
double-zero assumption is used. Mathlib full matching coverage is
unchecked. A later established finite result belongs in a canonical
lemma with full proof and qualifications; no lemma is written now.

Suggested execution routing after source approval: calculation,
standard/high. The operations and enclosure method are established;
the task is not a creative uniform-sign proof attempt.
