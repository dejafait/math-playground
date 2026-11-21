# One-sided average test — working checkpoint, step238

10 November 2026. Approved target: review236, unchanged SPECIALIZE
scope. Main gap: actual-Xi positivity and an independent arithmetic
bound. No arithmetic payment or RH conclusion is asserted here.

Candidate argument, not yet a completed or independently audited proof:
L981 and the fixed-index part of L982 give
|sum_(k=2)^n S_f(k)-(n-1)A_n(X_n)|<=2T,
T<=2exp(-630), by fixed-k limits followed only by finite sums.
L980's exact split lambda_k=S_infty(k)-S_f(k)+1 and unconditional
smooth trend then transfer the proposed every-epsilon upper bound
to every-epsilon lower bounds for c_n=sum_(k=2)^n lambda_k.

Set H(z)=2xi(1/(1-z)), H(0)=1. Voros(32) gives log H's local
coefficient lambda_n/n, so the candidate cumulative germ is
F(z)=[z H'(z)/H(z)-lambda_1 z]/(1-z)=sum_(n>=2)c_n z^n.
Under a hypothetical off-line zero, reflection supplies rho with
Re rho>1/2 and mapped w=1-1/rho of modulus<1. A nearest mapped
zero w_* should give F a simple pole of residue m w_*/(1-w_*),
for any positive multiplicity m. The positive segment maps to s>=1,
where xi is positive. For epsilon with R<exp(-epsilon)<1, adding
D_epsilon*(exp(epsilon)z)^2/(1-exp(epsilon)z) should give nonnegative
coefficients without removing the pole or positive-axis regularity.
Pringsheim would contradict that configuration.

Remaining checks before promotion: exact cutoff constants, finite
prefixes, ordinary normalization, existence of a positive minimum
radius, pole noncancellation, and identity of the continued germ.
Success would only establish a standard sufficient criterion;
afterward stop criterion reformulation without independent payment.
Canonical proofs and old stops remain unchanged at this checkpoint.

## Completion pointer

The reasoning above is preserved as the intermediate checkpoint.
The completed conditional proof, qualifications and precise citations
now reside in L984. Its cutoff transfer, coefficient direction,
finite radius, multiple-zero residue and same-germ positive-axis
extension are written there in full. This draft is not a second
canonical proof and supplies no additional mathematical claim.
The implication remains unaudited, and (H) remains unpaid.
