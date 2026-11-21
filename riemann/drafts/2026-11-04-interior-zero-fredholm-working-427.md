# Interior-zero Fredholm specialization — working record, step427

One RESEARCH/proof_attempt on the unchanged SPECIALIZE target in
`literature/2026-11-04-interior-zero-fredholm-norm-compression.md`.
The supplied source assessment is reused; no further literature is needed
for its conditional representation/error scope. Intended classification:
REPRODUCTION, not a new rational-Hankel theorem.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
an exact original-l2 finite-matrix representation of L776's correction
and a fully conditional approximation budget. A later certified bound
strictly below one could pay L776 for one admissible pair. Other orders,
available radii, tied zero moduli and the full positivity assembly remain
unresolved. L776 is independently unaudited.

Local checks: read L776, L018/L021, the step425/426 working records,
step425 history and the shifted-boundary ATTEMPTS record; searched the
specific Fredholm assessments for duplicates and prior stops. The shifted
inverse-boundary sign and L775 modulus stops do not supply a norm bound
or prohibit the present independent conditional interface.

Saved before lengthy derivation: write G(Rz)=P(z)F(z), P monic of degree
k=r-1. Test whether the exact log normalization gives phi_-=z^(-k)P
and phi_+=F. Only the negative Laurent part of c=z^k F/P should be
rational. For a pole alpha of multiplicity m, its principal-part
coefficients should factor B=H(tilde c) through columns
v_(alpha,p)(i)=binom(i-1,p) alpha^(i-1-p), 0<=p<m, with entries
understood as normalized derivatives when i-1<p. Track the bilinear
transpose by W=conj(V), then use polar decomposition for the full
product, without a Gram inverse.

The error proof must keep conditional circle bounds on F and 1/F,
explicit radii, coefficient/zero-data errors and finite matrix norm
roundoff. A coefficient-only approximation is insufficient. Continue
only with exact norm equality and finite paid operator errors; otherwise
record the defect and park this proposal. No actual zero calculation,
norm<1 test, creative growing-order estimate or RH claim is in scope.

Derivation checkpoint: the log normalization gives phi_-=z^(-k)P and
phi_+=F. The negative part of c is its finite sum of principal parts.
The confluent block has C_(p,q)=d_(p+q+1) for p+q<m, zero otherwise;
W=conj(V) converts V C V^T to V C W*. Polar decomposition gives the
original norm from both Gram square roots, including singular supports.

For an effective conditional budget, keep the rational approximate B
untruncated and truncate only the positive b coefficients. Then U_hat
has finitely many rows, while Y_hat's Gram entries are derivatives of
(alpha beta)^r/(1-alpha beta). Pole/derivative enclosures bound B-B_hat
on an inner circle, hence in Hilbert–Schmidt norm. Cauchy bounds on an
outer circle and finite coefficient errors bound H(b)-H(b_hat). Pay
delta_b ||B_hat|| + ||H(b_hat)|| delta_B + delta_b delta_B. A separate
certified finite-matrix singular-value error is still required. Full
proof and all constants are being assembled; no actual norm bound has
been evaluated.

Completed: the full proof, precise citations, finite matrices and all
conditional errors are canonical in L777. Its representation/budget test
passes at the level of a written known-theorem specialization; independent
critical audit remains pending. No new source assessment, actual enclosure
data or mathematical script was produced. The next invocation reuses the
unchanged assessment and target for a conceptual audit of this construction,
rather than treating the local interface as an actual norm<1 estimate.
