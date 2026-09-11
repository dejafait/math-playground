# Additive-character checkpoint — 2026-09-14

Use L188's exact J_(u,r) and coprime r restriction. Off the congruence,
Q((m²+r)/u) is undefined. Choose Q(floor((m²+r)/u)) explicitly;
on the congruence this agrees with the original. Keep gcd(m,u)=1.
Insert u^(-1) sum_(a mod u) exp(2πia(m²+r)/u).
The zero mode has a crude O_epsilon(N^(3+epsilon)) bound, which is
not o(Nh). Thus the precise remaining condition is E_N=-Z_N+o(Nh),
not E_N=o(Nh) unless Z_N=o(Nh) is independently proved.

Checkpoint: verify finite orthogonality, conjugate pairing, all support
cutoffs, and the zero-mode exponent; then store the lemma and regression
script. These draft claims are not yet proved DAG inputs.

Completed: L189 proves the identity, conjugate pairing, zero-mode bound,
and the exact conditional cancellation criterion. Its extension-dependence
calculation prevents treating the zero mode as automatically negligible.
The finite signed regression checks passed; no decay claim was promoted.
