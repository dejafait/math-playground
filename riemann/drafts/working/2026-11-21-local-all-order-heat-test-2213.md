# Fixed-model heat attempt2213: saved reasoning

Gate: unchanged EXPLORE assessment2212. Main gap: actual-Xi mixed
positivity L030-L032/C032a. Only the frozen L029 diagnostic is attempted.

Let A=1599/16, R=1601/16 and lambda_n=10000*pi^2*(n+1/2)^2.
The proposed identity is

    (-1)^k H_F^(k)(t)=25^k exp(-25t)
       +2 Re((A+5i)^k exp(-(A+5i)t))
       +sum_(n>=0) lambda_n^k exp(-lambda_n*t).

For k>=1 retain n=0. Since 3<pi<4,
22500<lambda_0<40000 and exp(-lambda_0*t)>2499/2500
throughout 0<t<=10^-8. The absolute pair contribution is at most
2 R^k < 2*101^k. Relative to the retained term it is less than
(5000/2499)*(101/22500)^k <=202/22491<1/100.
For k=0 the pair is positive because 0<5t<1<pi/2.

Still to write/check: fixed-order normal convergence on complex compact
subsets of Re(t)>0, all simple zero classes, conjugate reality,
summability of beta=alpha^-2 for L032, precise source import and scope.
No finite grid, tuning, Xi realization or global CM claim is used.
This is partial saved reasoning, not an independently audited result.

Completed later in this same step: the full argument and applicability
checks are canonical in C029z. Independent audit remains outstanding;
this saved pre-completion reasoning is retained as working evidence.
