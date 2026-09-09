# Goal

Produce a complete, checkable informal proof of the Riemann hypothesis:

Every non-trivial zero of the Riemann zeta function ζ(s) has real part 1/2.

## Success criteria

STATUS in PROGRESS.md may become PROVED only if ALL of the following hold:

1. There is a single main argument in PROOF.md that starts from standard, named theorems (no original “well-known facts” that are actually RH-equivalent).
2. Every lemma is stated with hypotheses, conclusion, and a proof or a precise citation (book + theorem number, or a standard named theorem).
3. The argument does not assume the conclusion, does not hide an equivalent form of RH as a lemma, and does not rely on numerical evidence, “it is plausible”, or an unstated interchange of limits.
4. A dedicated section named “Known traps checked” lists the usual collapse points and explains why this write-up is not one of them.
5. A dedicated section named “What a Lean check would need” lists the exact statements to formalize later. Do not write Lean now.

If the argument only proves a weakening, STATUS stays IN_PROGRESS and the weakening is recorded under “Partial results”.

## Known traps (do not treat these as a proof of RH)

- Assuming the explicit formula plus “error too small” without a proved zero-free region stronger than what is already known.
- Weil / explicit-formula positivity arguments that smuggle RH-equivalent positivity.
- Interchanging sums, products, or contours without a dominated or compact estimate.
- “All computed zeros lie on the line, therefore all zeros do.”
- Claiming a proof of Li’s criterion, Robin’s inequality, Lagarias, or Nyman–Beurling without proving the criterion itself in full strength.
- Using the prime-number theorem with an error term that already encodes RH.
- A “new contour” that is the same as a standard contour plus an estimate equivalent to a zero-free strip.

## Working rules

- After every attempt, append a dated entry to PROGRESS.md and keep PROOF.md as the current best write-up.
- Prefer a lemma DAG: small claims, then a short assembly.
- If an attempt dies, write WHY IT FAILS in one paragraph. Do not delete failed attempts; move them to ATTEMPTS/.
- Do not claim PROVED to please the user. A wrong RH proof is worse than no proof.
- Do not use an API key. If rate-limited, stop cleanly.

