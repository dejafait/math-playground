# Single-extension contact calculation, step2128

The gate-approved target and prior assessment are
`drafts/literature/2026-11-21-single-extension-contact-review-2126.md`.
Inputs are L058 and L874. Main gap: actual-Xi all-degree mixed
positivity, L030-L032/C032a. This is one bounded finite-premise test,
not an actual-theta realization or a global continuation argument.

Working calculation, to be checked before reporting: import
Curto-Fialkow (1991), Theorem 3.1 for S_2>0. Its representing measure
for S_2,...,S_7 is supported on the real roots of
p(x)=c_0+c_1 x+c_2 x^2, since integral p^2=c^T H_2 c=0.
For atoms t with masses w_t, the suspected L874 contraction is

    Phi = 8 sum_t w_t t p'(t)^2 (w_t-t^2).

The candidate obstruction is S_k=2 for k=2,...,8 and
c=(-1,1,0), giving Phi=16 rather than the required Phi<=0.
H_3 is the rank-one matrix with all entries 2. S_1 cancels at
contact. This is generic data, not actual-theta coefficients.
The S_2=0 branch should follow by successively zeroing rows of the
positive H_3, giving S_2,...,S_7=0 and Phi=0. Check all details.

Continuation test: exact positive flux stops finite-premise signing;
do not increase the extension degree or assert an actual counterexample.
Actual-family realizability/sign, initialization, equality, and global
and all-degree closure remain independent. No new source review or
mathematical assumption has been approved in this working note.

## Completed handoff

The suspected identity, zero-mass branch and both null-degree cases
were established in canonical C874b; the eight-case exact certificate
has zero failures. The example flux is 16 against the required upper
bound zero. Full proof/citation and qualifications are canonical in
`lemmas/C874b-single-extension-contact-flux-obstruction.md`.
Independent audit remains pending. The finite-premise-only route is
parked; actual-theta signing is unresolved. See PROGRESS.md for the
sole current continuation and its separate review gate.
