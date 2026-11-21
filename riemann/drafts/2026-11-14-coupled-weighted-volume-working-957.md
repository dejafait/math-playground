# Coupled stopped density — working957

Approved target: assessment955, separately approved at step956. One
proof attempt in the original flat raw flow, with the exact common
bidisk data and the full real-parameter complex determinant.

Partial reasoning saved before the endpoint and determinant checks:
write F=q^2 exp(-H), f=(-2/q+H_q,H_z), and A(v)=overline((D^2S)v)
as a real 4 by 4 variational matrix. The singular part has real
eigenvalues 2/|q|^2,0,0,-2/|q|^2; the background real operator norm
is at most M_2. Hence the top-two eigenvalue sum should be at most
2/|q|^2+2M_2. The source compound-volume bound would then give
growth for real tangent two-area V. Since dot F=-||f||^2 F,
the weighted growth coefficient is bounded above by
2M_2-2/|q|^2+4|H_q|/|q|-|H_q|^2-|H_z|^2
<=2M_2+M_1^2. This bound is independent of a singular cutoff.

Remaining checks in this attempt: justify |det_C J|<=V for the
two real tangent columns without a Lagrangian or nonvanishing
complex-determinant assumption; verify the real symmetric-matrix
convention and apply the cited compound theorem only on survivors;
prove finite-lifetime endpoints including simultaneous q=0 and
|z|=L; prove joint Borel zero extension and the full class-uniform
measurable-set quantifier. Candidate envelope is C(T_0)r^2, with
C=exp((2M_2+M_1^2)T_0-Re H(0,0)+M_1 sqrt(a^2+b^2)).

C466r and C466q are comparison controls, not premises. Stops927,
932,941,947,948 retain their scopes. No metric normalization,
signed integral, homology, endpoint payment, all-order signs or
actual-Xi conclusion follows. No independent audit is claimed.

Completed in C466s, whose canonical proof supplies the determinant
comparison, singular cancellation, simultaneous endpoint cases and
measurable-set quantifiers. The proposed envelope above is obtained
for every finite T_0. This working record preserves the intermediate
reasoning; it is not an additional canonical proof or an audit.
