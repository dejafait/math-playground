# Global Hermite sparse dual: source-review working record

Literature-only step, 2026-10-31. No mathematical construction or
coefficient computation is authorized in this step.

The supplied target is the complete-polynomial dual obstruction at
unbounded L564 cutoffs. Main gap: actual-Xi all-degree positivity.
L566's four-coefficient stop and L565's diagonal-CD stop were checked
in their canonical statements, local assessments and attempt records.
They do not decide this changed global constraint. Existing unfinished
work is preserved.

New inspected source coverage:

- Vandenberghe–Andersen, *Chordal Graphs and Semidefinite Optimization*,
  DOI 10.1561/2400000006, section 10.1, pp. 356–357: general sufficient
  image-closedness criterion (Rockafellar, *Convex Analysis*, Theorem
  9.1), nullspace(A) intersect C={0}, for a closed convex cone C;
  sparse-PSD/completion duality and Theorem 10.1. Reuse the parent's
  inspected Theorem 9.2 and singular-pivot cases; no generic reproof.
- MOSEK *Modeling Cookbook* 3.4.0, section 8.2, Lemma 8.3 and full
  three-alternative proof: feasible, limit-feasible but infeasible, or
  strictly certified infeasible. Lemma 8.2 includes PSD self-duality.
  Its proof distinguishes separation from the closure of A(K).
- Papp–Yildiz, arXiv:1712.01792v3, Proposition 1.1 and section 6,
  Propositions 6.1–6.2: unrestricted/weighted SOS dual matrix maps.
  These hypotheses use complete degree spaces, so they are comparison
  results, not an automatic import for fixed Hermite pair subspaces.

Closedness of this specific polynomial image is NOT established here.
The cited sufficient criterion can be checked during a separate
mathematical specialization. A directly verified negative functional
is sufficient without assuming image closedness; completeness of the
separator alternative needs that check. No separator or actual sign
has been derived.

Searches include exact Hermite/sparse/dual/Gram queries, Romik with
semidefinite/discriminant terms, and stronger general SOS, binomial
square/factor-width/DSOS/SDSOS terminology. No inspected primary result
supplies the actual coefficient family or a uniform negative dual
value. The primary factor-width/binomial-square lead was subsequently
inspected; exact scope and the completed bounded continuation are in
`literature/2026-10-31-hermite-global-sparse-dual-review.md`.
Failed Boyd and NSF PDF retrievals are
nonessential: the exact conic alternative and sufficient closedness
criterion are accessible in the sources above. Shell curl has no DNS
access; no API key or paid service was used.

Continuation must test all allowed squares and the COMPLETE D(P_N),
retain the distinction between a fixed finite cutoff and an unbounded
family, and justify every approximation. Failure to find a separator
is not a feasibility certificate. Full Gram matching, uniform signs,
zero-compatible Xi transfer, multiplicities and higher forms remain.
