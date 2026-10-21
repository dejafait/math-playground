# Complete quartic response: retain the two quadratic-flow outputs

Approved target and review: the unchanged complete quartic response in
`drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md`.
The main gap remains the interacting reflected comparison and the
continuum/infrared construction. Within L212's exact joint retraction,
test the co-closed-input summand j_(i,2)(z_2(tau)). This is not the
original forest-input summand and no termwise transfer is proposed.

Seek O(N^3) for its covariance with the actual r=sum z^T A z. This
would remove one independent obstruction to cubic boundedness of the
remaining complete flow response; convergence, the nested z_3 term,
the derivative-of-cubic correction and endpoint convergence would
remain. Continue only if the estimate retains s=0, s=tau, all boundary
rows and the signed covariance tilt. Abandon an argument replacing
every E_s by H_s or assigning smoothness to a rough tilted column.

Duplicate/failure check: L011 specifies this term but gives no mesh
bound; L189 estimates a cubic integrand, not this quadratic output
square; L212 permits the present co-closed input only as part of its
complete signed identity. L022 and ATTEMPTS/010 forbid transfer of
the isolated forest polynomial. C212a,b control different corrections.
ATTEMPTS/039 and 043 are global energy estimates for other polynomials.

Work in progress: write grad S_3(y)=C^T w_2(y)+V(y,Cy), retaining the
complete plaquette words. Positive full-spectrum bounds suggest
||w_2(H_s z)||_(L4;ell2)<=C/(s+a^2) and
||V(H_s z,C H_s z)||_(L4;ell2)<=C a/(s+a^2)^(3/2).
Use C E_t C^T and C E_t, whose norms are respectively
O(min(1,a^2/t)) and O(min(1,a/sqrt(t))). Initial times then give
O(N) for ||C z_2||_(L4;ell2); final times give only O(log(eN)).
The signed whitened-residual bound would multiply the differentiated
quadratic output by O(N), producing O(N^3) for its response. Verify
all powers, both quadratic input derivatives and the Gaussian factor
1/2 before accepting this as a result. A cubic bound is not a limit.

Completed: [C212c](../lemmas/C212c-two-quadratic-flow-response-cubic-bound.md)
proves the full O(N^3) response bound, including both flow endpoints,
using operator energy estimates in place of the proposed output-row
estimate. It also bounds every contribution outside [0,delta]^2 by
O_delta(N^2 log(eN)); the initial/initial square remains bounded at
cubic scale but has no proved limit or uniform delta-removal bound.
All correlations and the single-polynomial Gaussian factor 1/2 remain.
No mathematical script was needed. This is a local reproduction using
existing action, heat and Gaussian estimates; the other complete flow
terms, their joint response, endpoint limits and compensation remain.
