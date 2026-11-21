# Paired orbital infinitesimal response — working checkpoint1206

One mathematical attempt under the pre-existing EXPLORE assessment1204,
separately approved in1205. The supplied overview/DAG were read; C030l,
the completed complex-source comparison1204, and the named prior-stop
records were consulted. Existing notebook changes are preserved. The
oversized initial scoped git-status output is not exhaustive evidence.

Main gap: L030-L032/C032a all-degree actual-Xi positivity. Target: the
absolute uniform two-real-level b^2 response bound in assessment1204.
Possible use: a signed perturbation of C030l's finite real reference.
Test: establish a uniform constant or a rigorously unbounded family;
a coefficient formula alone does not settle that test. Finite-b bounds,
arbitrary background rates, pair summation and Xi transfer stay separate.

## Partial reasoning saved before the main estimate

Write Q=V P_j V*, S=Q_11+Q_22, T=Q_11-Q_22 and u=x(a-r).
Then tr(D_b Q)=r*j+(a-r)S+i*b*T, 0<=S<=2 and |T|<=1.
The swap of coordinates 1,2 preserves Haar measure and S, and negates T.
Consequently the separately normalized quotient Z_(j,b)/Z_(j,0) is
E_(j,u) cos(x*b*T), where E_(j,u) uses density proportional to exp(-u*S).
For each finite parameter choice this is real and positive near b=0.
Compactness bounds all derivatives on compact parameter sets.

With m_j(u)=E_(j,u) T^2, the formal Taylor/differentiation calculation gives

    lim_(b->0) (G_(j,b)-G_(j,0))/(x*b^2)
      = m_j(u)+(u/2)m_j'(u),
    m_j'(u)=-Cov_(j,u)(S,T^2).

These identities still require the full local remainder argument in the
canonical proof. The adjacent-rank response is the difference of these
expressions, with each rank retaining its own normalizer. Bounded T alone
does not bound u*m_j'(u) uniformly. Pursue that precise remaining estimate;
no claimed response bound or unbounded family at this checkpoint.

Source reuse: the ready assessment already compared complex HCIZ and
nonvanishing results; no further search is warranted for the unchanged
target. C030l is the real-reference context, not a complex-law input.
Stops1117/1181/1193/1200/1107 and overlap884 retain their prior scopes.
No cross-notebook input. Full matching Mathlib coverage unchecked.

## Completed attempt

The bounded test has a positive answer, with absolute constant 2/3;
the full proof is canonical in
[C030m](../../lemmas/C030m-two-level-infinitesimal-orbital-phase-bound.md).
Its single-rank response is bounded by 1/3. The proof averages the
U(2) orientation, scales the real contrast into the projection's top
row, and applies C030l's established positive tilted corner comparison.
Translation of the top row retains separate normalization and bounds
the change of each corner eigenvalue. Increasing test functions then
bound the derivative of the expected squared gap. No complex order is
assumed. This is one coherent response test, not a general corner-law
reproof or an extension to unequal background rates.

Meaningful checks included local analytic differentiation at fixed
rates, both contrast signs, zero contrast, n=2, j=0,n, the monotone
test-function extensions, and the explicit n=2 sine quotient giving
responses +/-1/3. No numerical sample or mathematical script was needed.
Independent conceptual audit is pending; finite-b control and Xi
transfer are not established. Classification POTENTIALLY_NEW reports
only that assessment1204 did not locate a matching theorem.

Outcome: ADVANCE as a restricted intermediate input toward the signed
reference mechanism. This changes the response test from unresolved
to a proved bounded claim pending later review, not the main RH gap.
The main argument assembly in PROOF.md is unchanged: no all-degree
or actual-Xi inference has been added. The DAG records only C030l as
the direct local input. No stop record is required for this successful
bounded attempt; all prior stops and unfinished work are preserved.
