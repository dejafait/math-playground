# Reflected two-fiber compatibility — conic construction test

This is one bounded mathematical attempt on the unchanged target in
`literature/2026-10-28-two-parallel-fiber-cyclic-matchings.md`, whose
EXPLORE assessment was supplied at startup. The prior reflected
construction and its unresolved general cycle equations remain in
`2026-10-28-two-parallel-fiber-working.md`; they are not replaced.
The local PROOF.md and DAG were supplied before L030 and the relevant
working record, ATTEMPTS/111 and history/540 were read. No new external
theorem, cross-notebook input or source refresh is needed for this
special case within the approved scope.

## Gap, target and bounded test

The main gap is arbitrary-center 67/68 safety. The intermediate target
is a permitted pair of rank-two fibers satisfying all six matchings.
A witness would eliminate this reduced obstruction; it need not extend
to the full sheet or resolve retention or RS transfer. Failure of a
subconstruction does not establish uniform two-fiber impossibility.

Keep the saved reflection ansatz, initially a=64, h=1, K=E, with actual
anchors 1,-1. Test the one-parameter family

\[
R_w(X)=[1+t_w(X-1)]^2-1,
\qquad S_z(X)=R_{-z}(-X).
\]

Its coordinates in the saved notation are
V_w=t_w^2 and U_w=2t_w(1-t_w). Thus all six loop vertices must have
t_w in {0,1}. For an edge {w,v}, its equality factors into

\[
\big((t_w+t_v)X+t_v-t_w\big)
\big((t_w-t_v)X+2-t_w-t_v\big)=0.
\]

All arithmetic in these formulas is in E; auxiliary indices remain in
F_137. No field identification is made. The factorization will be
checked directly. The complete matching still requires a nonanchor
root in H for each nonloop edge, with different antipodal pairs on
different edges, and a nonzero affine minor after assignment.

First test every binary assignment on the six loop vertices using the
already justified even-polynomial and two-equal-neighbor propagation.
If any case survives, retain its exact domains and test actual subgroup
compatibility, including label distinctness, within a recorded finite
search bound. A complete permitted witness or an exact obstruction to
this conic family is decisive for the subconstruction. A bounded search
failure is not impossibility. A third inconclusive mathematical attempt
requires reassessing this mechanism rather than rerunning it.

This checkpoint is saved before the finite tests. No witness or
obstruction is asserted here; the general reflection problem is open.

## Exact reduction used in the search

Write t=t_w and s=t_v. The coefficients of
R_w(X)-R_v(-X), in descending order, are

\[
t^2-s^2,\qquad 2(t+s-t^2-s^2),\qquad (t-s)(t+s-2).
\]

Multiplying the two displayed linear factors gives these three
coefficients, including when either factor is constant or zero. There
is no division by t+s or t-s, so those degeneracies are retained. With
x in H minus {1,-1}, put m_x=(1-x)/(1+x). Each factor vanishes exactly
when, respectively,

\[
s=t m_x\quad\hbox{or}\quad s=1+(1-t)m_x.
\]

The denominator 1+x is nonzero. These are the complete permitted
neighbor candidates, not a sample. For t=s=0 or t=s=1 the difference
polynomial is identically zero; every permitted pair is available. If
t=s is neither 0 nor 1, the difference is 4t(1-t)X and has no root in
H. Thus the zero-polynomial case must not be handled by division or
discarded. The search retains it and allocates its labels last.

At a loop, R_w(x)-R_w(-x)=4t_w(1-t_w)x. Characteristic 65537 is odd
and x is nonzero, so t_w is 0 or 1. These parameters give the even
polynomials 0 and X^2-1. An edge between the two different even values
has no nonanchor root. If a vertex has two neighbors with the same
even value, its polynomial agrees with that even polynomial at two
distinct actual labels and at the anchor 1. The degree-at-most-two
root bound therefore forces that value at the vertex as well. This
uses global label distinctness; using the same label twice would not
justify the rule. It is the prior propagation rule with an extra
restriction justified by this particular conic, not a renewed claim
that the six unrelated even values in ATTEMPTS/111 suffice.

For a vertex adjacent to parameters 0 and 1, respectively, the complete
possible parameter sets are

\[
D_0=\{0\}\cup\{2/(1+x):x\in H\setminus\{1,-1\}\},
\quad
D_1=\{1\}\cup\{(1-x)/(1+x):x\in H\setminus\{1,-1\}\}.
\]

The certificate enumerates these sets exactly. Both have 1023 elements;
their intersection consists of
6865, 8103, 14174, 23084, 28943, 32150, 33388, 36595, 42454,
51364, 57435, 58673 in E. This small domain is a necessary condition
only. Distinct root pairs and the other graph edges remain constraints.

Three distinct parameters give an affine-rank-two coefficient image:
the determinant of the two differences in (U,V) coordinates equals
2(t_j-t_i)(t_k-t_i)(t_k-t_j). This identity uses the formulas for U,V
above and characteristic different from two. Conversely, fewer than
three distinct parameters cannot have affine dimension two. Reflection
and index negation preserve affine dimension. The search still checks
an actual minor rather than relying on the existence of an unspecified
nonzero solution of the general cycle system.

## Complete boundary test and bounded compatibility search

The script `scripts/finite-support/two_fiber_conic_compatibility.py`
writes `scripts/finite-support/two-fiber-conic-compatibility.json`.
For a=64 the six loop vertices, in increasing order, are
10, 80, 85, 127, 128, 131. All 64 binary assignments are tested by the
two exact propagation rules. Six give a contradiction, two force one
constant family, and 56 remain unresolved. These counts do not exclude
the conic family. In particular, the search does not infer that the
unresolved cases are realizable.

Among the unresolved three-zero/three-one cases, the script selects
one with the largest number of forced vertices, breaking ties by its
binary mask. This is mask 11: the loop parameters in the above order
are 1,1,0,1,0,0. Propagation additionally forces parameter zero at
vertices 29,32,125. No other boundary assignment receives a coefficient
search in this step.

For that boundary case, exact finite-domain search uses seed 541137
and a fixed limit of 8192 candidate-parameter trials. It selects the
unassigned vertex of smallest current domain, intersects domains with
the complete neighbor sets above, and backtracks over root-pair choices
on edges whose endpoints are assigned. A nonzero edge consumes one
previously unused antipodal pair. Identically zero edges consume no
pair during search: after the search, they can be assigned distinct
unused pairs. This postponement is legitimate for a complete assignment
because all 408 edges together require fewer than the 511 available
nonanchor pairs; it does not supply missing nonzero edge roots.

This is a bounded search, not an exhaustive decision procedure for the
boundary case. Candidate trials, the trace, all boundary propagation
events, complete parameter domains at the two even values, the best
partial assignment and its edge checks are retained in the certificate.
The finite search stops at its prescribed limit and is not enlarged
after seeing the result.

## Result and verification

The search uses all 8192 trials and reaches a partial assignment on
70 of the required 137 vertices. The induced nonloop graph has
164 of the required 408 edges: 158 have selected distinct nonanchor
antipodal pairs, and six have identically zero matching polynomials.
The script assigns six additional unused pairs to these zero edges,
then six unused individual labels to the loops. It checks every induced
original matching in both orientations, directly evaluating the
quadratics rather than merely rechecking the factored equations.

All 334 induced original matchings pass, using 334 distinct transverse
labels in H minus {1,-1}; the required complete count is 822. Both
anchor constancies hold on all assigned polynomials. The (U,V) points
at vertices 29,10,0 are (0,0),(0,1),(47306,62308), with difference
determinant 18231 modulo 65537, which is nonzero. Thus the two partial
images have affine dimension two. There are 67 unassigned vertices and
488 missing original matchings. No claim is made that this partial
assignment extends, and no full core/bijection witness is claimed.

Verification failures: none. The complete selected assignment and all
164 edge checks were inspected, followed by the full summary, rank
minor, exhaustive replay flags and empty failure list using the shared
JSON inspector. A partial rank-two image, even with valid assigned
labels, does not meet the approved target. The search trace is evidence
of the recorded finite search, not a certificate of impossibility.

Reproduction:

```bash
python3 scripts/finite-support/two_fiber_conic_compatibility.py
```

## Outcome, reassessment and Mathlib

Outcome EXPLORATION, actual task type calculation. This is the third
consecutive mathematical exploration (538,540,541), with no reset.
The general two-fiber question and even this conic subconstruction
remain undecided. No canonical lemma, new source import, mathematical
novelty, improvement to 955–957 or progress beyond the checked sources
is claimed. PROOF.md and DAG.md are unchanged. Mathlib full or
supporting coverage was not checked; no absence claim is made.

Park this reflected compatibility search, preserving its partial
assignment and the more general cycle equations. Raising the same
budget or renaming the conic parameterization is not a new mechanism.
ATTEMPTS/112 records this stop without turning a bounded failure into
an impossibility statement; ATTEMPTS/109–111 remain intact.

For the independent direction selected after reassessment, only the
hypotheses/conclusions of audited L135 and L137 and the explicit scope
restriction in the old common-cubic assessment were read. The proposed
span-two consequence of their common-line conclusion concerns the full
sheet, not completion of these two fibers. That assessment expressly
did not cover span-two impossibility. The proposed target is therefore
saved as REVIEW_REQUIRED for a separate source comparison, with no
derivation or approval of that new claim in this step. Span three,
retention, arbitrary compatible laws and RS transfer remain unresolved.
