# Appell single-entry calculation — step775, preserved working checkpoint

Completed: the exact entry formula and a strictly negative interval are
canonical in `lemmas/C040a-reciprocal-power-appell-production-entry-stop.md`.
Full evidence: `scripts/central-jacobi/appell-production-entry-775.json`,
31 checks, no failures. The chosen production-TP construction stops;
an independent audit is pending. The notes below preserve the initial
reasoning and unpaid checks as they stood before the calculation.

Approved target: assessment773's P_(2,0), with no other minor or degree test.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Downstream use: Sokal Theorem2.14 would propagate full production TP to
zeroth-column Hankel TP; a negative entry falsifies that sufficient hypothesis.

Theorem2.19, F=M,G=t, gives A=1 and Z=M'/M, with ordinary z_j.
Writing M=1+m_1 t+m_2 t^2/2+m_3 t^3/6+O(t^4), formal division gives
[t^2]Z=m_3/2-3m_1 m_2/2+m_1^3. Thus the target is
P_(2,0)=m_3-3m_1 m_2+2m_1^3, m_j=S_(j+2)/S_2.
This expression still needs finite-matrix indexing and interval checks.

L776 and L040 give e_j=4^j a_j/a_0, not gamma_j/a_0.
Read L778's complete coefficient evaluator/tail proof and audit ranges;
read L791's Cauchy interface and step478 evaluator/hash comparison.
Need inspect complete coefficients0-5 and relevant saved checks/failures,
then add E_G/1600^j at every j, normalize, apply Newton through S_5,
and certify only the displayed entry against zero. Analytic/software
contracts remain explicit premises. No new evaluator or sweep authorized.

Continuation/abandonment: negative upper endpoint closes the chosen Appell
production criterion; nonnegative lower endpoint retires this diagnostic;
a zero-containing interval is inconclusive. No RH or all-degree conclusion.
No calculation outcome yet. Existing unfinished work is preserved.
