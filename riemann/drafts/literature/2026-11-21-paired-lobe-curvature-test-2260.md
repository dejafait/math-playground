# Root-linked paired-lobe curvature test: prepared coverage2260

TARGET: Test whether the specified quartic log-cosh perturbation family, aligned to its least cosine zero, gives H H_uu-H_u^2>0 at u=v=a/4 and thereby refutes generic joint log-concavity of the paired-lobe density.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed2260 exact paired-density/alternating-translates/difference and log-cosh/first-zero searches; no matching theorem or counterexample identified in inspected sources. Local2257/2254/2249, C919s and L049/L050 compared; full queries/read limits in drafts/literature/2026-11-21-paired-lobe-source-notes-2260.md .
SOURCE_EVIDENCE: Tuck2006 pp133-135 equations(1)-(4), https://doi.org/10.1017/S0004972700047511 ; Prekopa1973 Theorems6-8/proofs6-7 pp342-343, https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf ; Boyd--Vandenberghe Convex Optimization2004/2009 Sections3.5.1-2 pp104-106, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf ; reuse2249/2254/2257 dominated convergence/differentiation and named intermediate value theorem as used in C919s.
COMPARISON: Standard Hessian criterion covers the proposed obstruction test, not its sign. Pairing positivity and nonnegative marginal theorems give no closure theorem for H. The base quartic marginal's negative curvature at1 does not settle this distinct root-linked density mechanism.
GAP: All family admissibility and derivative tails, exact least-zero alignment, uniform derivative-series bounds, density positivity and strict determinant sign are unpaid. The fixed small-rho family is a proposed analytic test, with no derived perturbation estimate or generic conclusion in2260.
REASON: A concrete test of the unproved joint-density premise is independently discriminating and uses inspected standard tools; no theorem found settles it. A positive determinant rejects only this sufficient mechanism, while a nonpositive value cannot prove generic preservation or RH. Search misses are not originality evidence.
SCOPE: Only the exact family, parameter interval, point, asymptotic regime and stopping test below; no parameter search, numerical retuning, alternate kernel or generic preservation proof.

Full source comparison, source qualifications and the preserved hypothesis
set appear in [notes2260](2026-11-21-paired-lobe-source-notes-2260.md).
This file is newly prepared continuation coverage; separate supervisor
approval must precede mathematical execution. It is not an approval of
previously uncovered mathematics derived in the same turn: none was derived.

Use only the following proposed family:

    V_{rho,a}(t)=t^4+t^2+rho^(3/2)[
       log cosh((t-3a/2)/rho)+log cosh((t+3a/2)/rho)],
    K_{rho,a}(t)=exp(-V_{rho,a}(t)),
    0<rho<1, 2/3<=a<=7/10.

The exact density to test is

    H(u,v)=sin(xv) sum_{j>=0}
       [K(u+v+2ja)-K(u+v+(2j+1)a)], u>=0, 0<v<a,
    x=pi/a.

Seek a proof, for sufficiently small positive rho, of an eligible a in
the fixed interval with x its least positive cosine zero and a strictly
positive value of H H_uu-H_u^2 at the fixed interior point u=v=a/4.
These are proposed requirements, not established facts. No formula for
the specialized determinant or its asymptotics is supplied in this review.

C919s's base quartic first-zero result may be used with its explicit
CPython/Fraction/libmpdec contracts. Do not rerun or retune that closed
certificate. Establish stability/earlier-zero exclusion under the new
family by uniform real-variable bounds and the named intermediate value
theorem; do not assume differentiability at rho=0 or a root branch.
Supply every-derivative/every-exponential admissibility, local uniform
summable derivative bounds for H, positivity and the determinant sign.
No actual-Xi hypothesis or simple-zero premise is granted for the new
family. Any claimed simplicity is an additional proof obligation.

Continue only if those hypotheses and a strict positive determinant can
be proved for this fixed family. A rigorously nonpositive value tests
only this family/point. Failure of alignment, derivative domination or
sign resolution stops this one attempt, without changing the exponent,
location or point. An obstruction rejects joint log-concavity of this
representation only; the marginal identity need not be proved to reject
the proposed joint-density sufficient premise. A positive marginal route
still needs that identity and all Prekopa hypotheses. Actual-Xi
applicability, repeated strictness and all-degree positivity stay open.

Recommended proof_attempt/creative: the unproved root-linked curvature
comparison is a different analytic mechanism from the closed fixed
marginal quadrature. The bounded test is precisely the displayed
determinant under the fixed small-rho family; no mathematical execution
has occurred. Full matching Mathlib coverage remains unchecked.
