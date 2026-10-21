# L112 critical audit — working record

Approved target: Critically audit L112's exact Jacobian identification and non-torsion certificate.
Prior coverage: `drafts/literature/2026-10-21-marked-elliptic-positive-rank-audit.md` (SPECIALIZE).

The main gap is residual positive primitive integer exclusion. This step
tests the reliability of L112, so that a false rank-zero route is not
reopened. Inputs are audited L111, L112 and its complete witness
certificate. ATTEMPTS/050 and /051 preserve the separate bounded-search
and rank-zero stops. No rank upper bound or new point search is attempted.

Pass only after independent exact recomputation verifies the actual
twisted coefficients, nonzero discriminants, rational scaling, covariant
identities, rational point, nonzero double and reduced nonintegral
coordinate, together with the assessed theorem hypotheses. Otherwise
repair or park the failed claim. The rational-origin identification is
distinct from the degree-four covariant map. Marked lifting, degree-nine
root recovery, remaining factors, both L095 systems and minus-eleven
remain unresolved even if the audit passes.

Work saved before independent computation: the source comparison is
ready and L111 supplies the smooth proper genus-one model and rational
origin. Producer code and proof have been read; the audit will use a
separate polynomial implementation and exact rational tangent arithmetic.
Final verdict: PASS without mathematical correction to L112. The full
canonical audit proof and citations are in L112's independent-audit
section. `scripts/pair-genus-two/elliptic-rank-audit-certificate.json`
records 42/42 successful checks and complete comparison of all 17
producer fields. The initial checker sign error is preserved in
`scripts/pair-genus-two/elliptic-rank-audit-initial-sign-failure.json`;
the source-normalized correction and its effect are explained in L112.

This confirms an existing known-method specialization, not a new rank
theorem or integer exclusion. PROOF.md and DAG.md need no argument or
dependency change. The next proposed target is a reversible
hyperelliptic presentation of the marked curve through its conic,
as preparation for a point-cover descent retaining the square condition.
This is outside the current audit scope and remains REVIEW_REQUIRED;
no parameter formula, new model or descent claim is derived here.
