# Critical logarithmic gcd bound — working checkpoint, step228

The invocation-start SPECIALIZE assessment is
drafts/literature/2026-11-09-logarithmic-gcd-row-sum-review.md; its
COVERED_TARGET is the sole mathematical task. Reuse its inspected Tao
Theorem13; no new source campaign or claim of originality is needed.
Read L737 (5)–(11), its separate audit, and the step226 pilot stop.
Existing changes throughout this active notebook remain untouched.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: F_(2 log N)(c)>=-C Q(c), with one absolute C
for every integer N>=2 and arbitrary complex c. A sharper arithmetic
main-term norm could inform later observer-length choices; coefficient
conditioning, charged moment errors, realization and signed transfer
remain independent gaps. Continue only on a proof uniform in every
cutoff/vector; park this mechanism if the correction or Schur remainder
fails. The finite pilot remains parked and is not proof evidence.

Partial reasoning saved before canonical write-up: choose a nonnegative
absolute M for the upper side of Tao's first-Mertens estimate. For a
prime power p^k, the denominator difference is exactly
1/phi(p^k)-1/p^k=1/(p^k*(p-1)). Summing the nonnegative correction
over k gives log p/(p-1)^2; comparison with
4*sum_(n>=2) log n/n^2 gives an absolute finite bound. The intended
row constant is C0=M+3 log 2+2. With ell=log N, unchanged weighted
rows/columns should give ||K||<=sqrt(ell*(ell+C0))<=ell+C0/2.
Use the full complex cross term in L737 (6) and kappa>=0 to reach
the target. Check all real cutoffs, empty rows, c=0 and Q>0 before
claiming completion. No numerical test, new moment input or Xi sign
is involved. Canonical proof and final outcome still pending.

## Completed attempt

The full argument is now canonical in
lemmas/L924-critical-logarithmic-gcd-uniform-lower-bound.md. It supplies
the requested constant C_*=M+3 log 2+2, uniform in N,d,c; no step of
the above intended bound failed. Q>0 uses only L737's existing finite
inversion. All full proofs remain in that lemma rather than this note.
No numerical certificate or mathematical script is needed for the
exact finite argument. Separate audit is pending, with source reuse
prepared in the audit assessment; no new creative mechanism or RH
claim is inferred. The outcome is local ADVANCE / REPRODUCTION.
