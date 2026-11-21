# Step470 — approved tube and saddle audit, working record

Invocation target is exactly the SPECIALIZE target in
`drafts/literature/2026-11-05-uniform-moment-tube-saddle-audit.md`.
Supplied overview, DAG and assessment read; L787/L788 interfaces and
their proof qualifications inspected, with the named q-Pascal norm and
pointwise moment stops. Existing unfinished files are preserved.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
verify the kernel tubes, real initialization and analytic full-saddle
drift <=3/200 for k>=10^9, |z-k|<=k/20. Downstream use is L788 then
L787; this turn will not audit the saddle action, Taylor theorem, other
wedge gates, bounded k/r or any global sign claim. Continue only if all
required full-domain inequalities close without L788 as an input;
otherwise record the first failure and retain the conditional conclusions.

Primary v1 Section3 (5) and complete Lemmas3.1–3.3 inspected during
the audit. No ancillary file is used. The source's geometric estimate
needs 0<=nu<pi/8 and q<1, as already qualified by the ready assessment.

Working reductions to check:
- Phi_n/Phi_1 is bounded by a decreasing rational prefactor times
  exp(-pi(n^2-1)e^(4x)cos(4y)); n^4<=16^(n-1) gives the tube series.
  Use exact rational exponential partial sums at x0=0.3,0.35,0.4.
- On 0<u<=1, K(u)<2pi e^4<10^9, whether H is positive or not.
  On u>=1, H>0, H'>4H and K increases to infinity. Evaluate at
  log(k)/4 to get the upper bound. Do not assume H>0 all the way to 0.
- On the full radius1/20 disk, B0>300 permits the source derivative
  bounds with generous room. Check K''/k<60 independently.
- Complete radius1/25 circles stay in the small tube. Bound the map
  perturbation by 7*10^-15 k, then perform both Rouché comparisons.
  Exactly one zero counted with multiplicity gives simplicity; uniqueness
  patches local implicit functions on an open neighborhood of the closed
  z-disk. Construct log(Phi) with its positive real normalization.

The first scalar run mistakenly tested the larger tube against 11/10^13;
L788 (4) actually requires 11/10^12. The computed rigorous bound is
<6.548*10^-12, so this was a harness transcription failure, not a failure
of the approved source claim. The failed certificate is retained as
`scripts/complex-moment-audit/tube-saddle-470-initial-threshold-error.json`.
The required threshold in the script is corrected to the actual L788
threshold; the source's smaller-tube bounds pass without any adjustment.

Completed: the canonical proof is
`lemmas/L789-uniform-kernel-tube-and-saddle-audit.md`; 25 exact scalar
checks pass in `scripts/complex-moment-audit/tube-saddle-470.json`.
Both Rouché comparisons also hold on |z-k|<51k/1000, resolving the
closed-disk boundary continuation. L788's conditional premise is now
explicitly restricted to the covered small strip; its proof is unchanged.
Classification is REPRODUCTION: local verification of source claims,
not a new sign theorem. The next Taylor target is only proposed, with
REVIEW_REQUIRED coverage; no new target was derived or approved here.
