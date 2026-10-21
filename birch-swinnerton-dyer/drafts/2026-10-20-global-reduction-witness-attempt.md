# Fixed global reduction witness attempt — step 377

The approved target is exactly the bounded good-prime test in
`drafts/literature/2026-10-20-Q-minus-four-P-global-reduction-witness.md`
(SPECIALIZE, present at invocation start). Essential mathematical inputs
are L030's exact integral minimal model and discriminant 389, Silverman
III Algorithm 2.3 and VII Proposition 2.1. L096 is the existing audited
local comparison, not an input to the global obstruction calculation.
No saturation or Sha premise is used.

Plan: enumerate primes increasingly in 11..500 excluding 389. At each
prime enumerate the entire finite curve and save every multiplication-
by-seven chain, its branches and inverse witnesses, including duplicate
images. Replay independently after a short-Weierstrass translation and
also by sequential scalar additions. Compute Q-[4]P with full chains.
Stop at the first replayed nonmembership in the full image; otherwise
record bounded inconclusiveness without extending the cap.

The desired downstream use is a nonzero global quotient representative
for the already known local congruence. No zero-log point, complete
Selmer-kernel identification, uniform certificate production or general
rank/order comparison is supplied by such a witness. Prior order-route
stops and unfinished artifacts are preserved.

Initial state before calculation: no prime tested and no result claimed.

Completed calculation: the first witness is 23, after full tests at
11,13,17,19. Complete independent replay passes all finite evidence.
The proof, full table, qualifications and reproduction commands are
canonical in L097; no mathematical failure occurred. The fixed target
is complete, with separate critical audit still pending. Further scope
requires separate approval as recorded in PROGRESS.md.
