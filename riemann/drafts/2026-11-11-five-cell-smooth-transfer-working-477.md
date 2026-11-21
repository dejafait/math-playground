# Exact-neutral smooth transfer — working record, step477

Target: Establish form-norm approximation of every exactly cell-neutral even sum of modes0-83 by even cell-interior smooth tests satisfying the original ten five-cell moments exactly.

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-11-11-five-cell-exact-neutral-smooth-transfer-475.md`.
This is one REPRODUCTION proof attempt, not a positivity calculation.
The main gap remains L030-L032/C032a actual-Xi positivity. The proposed
domain transfer could connect finite neutral tests to the smooth class;
middle/cell interactions, distant couplings, odd signs and all-window
positivity remain independent unpaid gaps.

Inputs read: L744(6)/(8); C744b(1)/(2) and its exact reflection law;
C744c Section2; C744e's accepted step466 closure audit; L743(9)-(10)
and its accepted complex-moment audit. The supplied assessment records
Suzuki Section3.2 and Hofer-Wysocki-Zehnder Lemma2.12. No additional
source review is needed. The C744g fixed-half-energy failure and its
accepted audit were checked; no threshold or reservoir is retuned.

Unfinished construction, saved before completing the proof:

- Center the five cells on (-a,a), a=5log(3)/4. Use a real even
  cutoff vanishing near all six boundaries, not just the two endpoints.
  For the finite cosine sum, prove the removed function has L1 norm
  O(epsilon) and uniformly bounded zero-extension variation, including
  its two endpoint jumps. Split its Fourier integral at 1/epsilon.
- Use L743's fixed smooth two-moment inverse on each cell, including
  the physical factor exp(sigma ell/4). Its finite collection of smooth
  basis functions must have finite logarithmic Fourier norm; the L2
  inverse bound by itself is insufficient.
- Reflection permutes output (j,sigma) to (4-j,-sigma), without
  conjugation. For symmetric output d, use (Hd+reflection(Hd))/2.
  Verify its ten moments exactly and its form-norm bound.
- Correct the cutoff residual, which must tend to zero in the physical
  ten-dimensional norm. Prove convergence in a positive shift of the
  complete L744(6) energy and hence energy convergence.

Pass only if compact cell-interior support, even complex parity, exact
ten-moment cancellation and full form convergence all hold. A missing
boundary term, merely L2-small correction, or approximate neutrality
fails. No new general density theorem or complete sign is being sought.

Completed in canonical C744h: squared logarithmic/form error
O_f(epsilon log(1/epsilon)), correction norm O_f(epsilon), and exact
ten-moment cancellation. The argument does not identify whole domains.
This note retains the initial plan; the full proof and qualifications
are in `lemmas/C744h-five-cell-exact-neutral-smooth-form-approximation.md`.
Separate conceptual audit remains pending.
