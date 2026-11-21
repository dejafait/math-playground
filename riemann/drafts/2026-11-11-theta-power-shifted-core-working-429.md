# Fixed shifted core attempt — step429 (working record)

Approved target: the exact TARGET of literature/2026-11-11-theta-power-shifted-signed-core-test-428.md, supplied at startup with EXPLORE coverage. One analytic attempt, no scripts. Main gap: actual-Xi positivity L030-L032/C032a; the proposed G_w sign only pays a prospective collision factor.

Imported source: Lagarias–Rains math/0104176v5, Theorem2.1/(2.9), Theorem4.4 proof(4.8)-(4.9), Lemmas4.5-4.7 and Proposition3.2/(3.7), with the branch and normalization recorded in review427. C999f is motivation, still unaudited; its real-axis tail constant will not be used on the shifted line.

Partial calculation to preserve before continuation: write z=x+i*pi/8, T(z)=theta(exp(2z)), B=log T on the source branch, b=z/2+B, d=(b')^2-1/4. The source integrand after centering is K(w,z)=exp(w*b)(b''+w*d). Its total w derivative is M(w,z)=exp(w*b)[b*b''+(1+w*b)*d], so the proposed core is (exp(-t*pi/8)/2) Re integral_{-2}^2 M(w,x+i*pi/8)exp(i*t*x) dx. This algebra includes the moving center, pending the compact differentiation justification. No sign bound has been obtained.

Tail calculation in progress: for x>=0 on the two lines y=+/-pi/8, v=exp(2x), |T-1|<=3exp(-2v), |T'|<=17v exp(-2v), |T''|<=170v^2 exp(-2v). Proposed logarithm bounds: |B|<=6exp(-2v), |B'|<=34v exp(-2v), |B''|<=510v^2 exp(-2v), |d|<=200v^2 exp(-2v). Constants and reflected tail require complete checking before use.

Acceptance remains m>E uniformly on the original rectangle, or core+E<=0 at one rational point. An effective tail or zero-straddling core bound is only an inconclusive attempt. Preserve the signed term if this fails, and park this mechanism without another absolute-bound or contour-parameter retry. Continuation source review must concern a materially different, independently testable target.

Completed: the full derivation is canonical in [C999g](../lemmas/C999g-shifted-theta-core-and-first-exponential-comparison.md). The preliminary calculations above remain the interruption checkpoint, not a second proof. The signed first-exponential contribution has a conservative nonlinear error allowance that makes the enclosure strictly straddle zero. Outcome EXPLORATION; no sign or event certificate. No mathematical script was created or run.
