# Finite coefficient-conditioning attempt — 9 November 2026

Approved target and prior SPECIALIZE coverage:
drafts/literature/2026-11-09-gcd-coefficient-conditioning-reproduction.md.
Only the unchanged finite Q and L737's finite inversion are in scope.
The source comparison found exact manuscript overlap; this is reproduction.
The signed dyadic pilot remains parked. No mathematical script is needed.

Before completing the canonical write-up: let y_m=sqrt(phi(m))B_m.
The inverse is A_(n,m)=1_(n|m)mu(m/n)sqrt(n/phi(m)). Use its
absolute matrix K and positive weights h_n=n^(-1/2). The weighted row
sum is sum_(k<=N/n)|mu(k)|sqrt(nk/phi(nk))/k. The weighted column
sum is sqrt(m/phi(m))sum_(k|m)|mu(k)|. For delta=epsilon/4,
bound sqrt(m/phi(m))<=A_delta m^delta, tau(m)<=D_delta m^delta,
and H_N<=H_delta N^delta. Thus R<=A_delta H_delta N^(2delta),
S<=A_delta D_delta N^(2delta), and the squared inverse norm is at
most A_delta^2 H_delta D_delta N^(4delta). Pending final write-up:
justify A_delta including the Rosser-Schoenfeld exception and 1,2;
retain complex-vector domination; check inversion direction and constants.

Bounded acceptance test: both weighted sums must be uniform in N>=2,
and the product must have exponent epsilon, not an unsquared-norm
exponent. Failure of either test stops the claimed specialization.
This finite estimate can help compare L925's arithmetic margins with
coefficient-norm errors, but supplies no such analytic comparison itself.
Main gap: actual-Xi all-degree mixed positivity L030-L032/C032a.

Completed: the full finite argument and scalar allowances are canonical
in lemmas/L926-finite-gcd-subpower-coefficient-conditioning.md. Both
weighted sums have exponent 2delta; their product has exponent
4delta=epsilon. Small indices and the totient exception are included.
This records a source-covered reproduction, not an independent audit.
The new audit continuation is saved for separate next-turn approval.
