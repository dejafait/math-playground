# Compensated prime-cutoff tail — working checkpoint, step226

Approved target: X_n=exp(10000*(n+1)^4), all integers n>=2 and
real Y>=X_n, full prime-power terms. Reuse review224 SPECIALIZE.
No S_f identification or signed finite-head control is assumed.

Provisional calculation to check before canonicalizing: set k=n+1,
U=10000*k^4, V=sqrt(U)=100*k^2. For u>=1 the global Laguerre
coefficients suggest |L|<=2^n*u^(n-1) and
|L'-L|<=k*2^n*u^(n-1). Johnston-Yang then gives
|R(x)|<=10*x*u^2*exp(-4*sqrt(u)/5).
Finite Abel summation should yield R(Y)f(Y)-R(X)f(X)-int_X^Y R*f',
where f(x)=L(log(x))/x. Both endpoint terms must be retained.
The provisional uniform bound is
10*2^n*V^(2*k)*(2+5*k*V)*exp(-4*V/5).
Its logarithm is bounded by 10+14*k-76*k^2<=-70*k^2 for k>=3.

Remaining checks: exact coefficient and derivative inequalities;
Abel compensation and full jump conventions; decreasing boundary
envelope and the all-Y integral; elementary constant certification.
This checkpoint is unfinished reasoning, not a verified lemma.

Completion: the checks above were discharged in the canonical
lemmas/L981-explicit-compensated-prime-laguerre-cauchy-tail.md.
This provisional checkpoint is preserved as working history; use
the canonical proof for the final statement and qualifications.
