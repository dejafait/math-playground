# Robin even-quartic test — step 69 working record

Invocation-start coverage: the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
The exact prescribed-node full residual is the only approved target.
Existing L681 audit changes and all unfinished files are preserved.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
multiply L681's Robin kernel by exp[-n*(c2*z^2+c4*z^4)], with real
c2,c4, and test a complete contour estimate at rate strictly above 1/100.
Such a positive quadrature could support discrete-sign transfer to -R;
unit-residue H, support, realization and actual-Xi signs remain separate.

Inputs read: L666 (6), L673 exact nodes, L672 Section 3's full series
error justification, L681 (1)--(11) and separate audit, and L680's
parameter-circle argument as already verified in L681. No new external
theorem is required beyond the residue theorem cited precisely in L681.

Duplicate/failure screen: step 43's connected quartic search used
L673's finite-polynomial kernel, not L681's Robin kernel. It was
inconclusive, with no global quartic obstruction. The new Robin decay
-20*pi*max(Re z,0)/27 and exact residues supply the material change.
The first test here is an exact convex combination of boundary costs
that eliminates both multiplier coefficients. Numerical tuning alone
would not reopen the parked old search or prove an obstruction.

Continue on a complete strict-rate bound, a quantified useful improvement,
or a rigorous obstruction to this sufficient contour estimate. If only
a finite screen fails, record EXPLORATION rather than impossibility.
This paragraph was the pre-calculation checkpoint; the completed result
is recorded below.

## Completed attempt

Outcome NEGATIVE. The full proof is canonical in
[C681a](../lemmas/C681a-robin-quartic-fixed-rectangle-obstruction.md).
The three-point convex certificate eliminates both coefficients exactly;
its lower endpoint is -18972432971/2500000000000. A first stronger requested
threshold -7/1000 failed; the retained certificate proves the sufficient
obstruction threshold -1/125 instead. All 13 checks pass, including exact
rational-power cross-checks of every selected finite series. The finite-n
integrand bound excludes a uniform absolute estimate with rate above
1/100 on the fixed rectangle for all real coefficient sequences.

No parameter search, sampled norm or contour-integral lower bound is used.
The kernel/contour scope distinguishes this result from step 43's old
inconclusive search. L681's approximation and all independent main-goal
gaps remain unchanged. The next test is direct continuous residual norm
enclosure with the unmodified Robin weights, retaining signed cross terms;
the exact current action and routing are only in PROGRESS.md.
