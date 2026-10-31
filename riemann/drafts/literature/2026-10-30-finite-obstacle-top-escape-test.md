# Finite-obstacle top-boundary envelope cost: calculation nomination

TARGET: Test whether L504's exponential growth envelope gives a bounded top-boundary escape cost on expanding rectangles with the H_a obstacle removed.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed searches, exact-class comparison and stopped-route checks in 2026-10-30-finite-rectangle-negative-part-barrier.md; no additional browsing or novelty claim. The proposed target isolates that review's uncovered finite-domain escape rate.
SOURCE_EVIDENCE: Schmidt, Partial Differential Equations I, version 2026-01-15, Sections 2.4, 2.6 and 2.10, pp. 22--23, 36--37 and 62--67, with the statements and proof cases inspected in the parent assessment; Lefevre--Queffelec Proposition 1.7 and Theorem 1.8; L504 definitions and its Fourier growth/weight-conversion arguments.
COMPARISON: Known finite Dirichlet comparison and Harnack theory supply the tools, but do not directly evaluate this top-data cost. A separated-variables comparison and a fixed compact Harnack chain are proposed for an elementary specialization; no reproof of the general source theorems is needed or authorized.
GAP: Quantify the top contribution below for fixed T and R as H grows, retaining the obstacle and constants. No boundedness or divergence has been proved. Actual negative-part growth, real-axis kernel control, H_a existence and Xi transfer are separate.
REASON: This is an independently testable residual allowed by the completed barrier review, rather than another qualitative unbounded-domain maximum-principle invocation. The SPECIALIZE scope is newly nominated; supervisor approval next turn must precede the calculation.
SCOPE: Only the prescribed exponential-envelope top contribution on the finite polygonal domains below. Classification REPRODUCTION; no general H_a inequality, admissible counterexample, arbitrary outer-cost optimization, source reproof or creative central mechanism.

## Exact future test, not a mathematical conclusion

Use L504 notation. Fix R>0 and one real T>exp(1); set a,b,B,lambda
as there, and retain A_R from its weight conversion. For H>max(B,1),
put X_H=H^2+a+B+2 and define

    O=[-a,a] times [b,B],
    Omega_H=((-X_H,X_H) times (0,H)) minus O.

On the top boundary define the continuous function chi_H to be 1 for
|x|<=X_H/2 and 2-2|x|/X_H for X_H/2<|x|<=X_H. Let h_H have top
datum chi_H and zero datum on every other boundary component, including
the obstacle. The tapers make the prescribed data continuous at the
outer corners. Justify existence, uniqueness and 0<=h_H<=1 by the
cited bounded-domain theory, explicitly checking the exterior cones
at the inner corners. No unbounded-domain Dirichlet theorem is assumed.

The quantity to test is

    J_H=2R A_R exp(2pi R H) integral_0^b exp(-lambda y)
                         [h_H(a,y)+h_H(-a,y)]dy.

This is a proposed lower portion of the top-envelope cost after
normalizing by M, not a lower bound on the actual negative part of f.
Check its relation to L504's ambient-bandwidth envelope rather than
assuming an admissible function attains that envelope. No new
inequality is asserted by defining J_H.

Seek either a proved upper bound for J_H/a as H->infinity, or a
rigorous demonstration that it is unbounded already for fixed T,R.
A candidate quantitative test is comparison with a vertical corridor
strictly to the right of O, followed by Harnack transfer through a
fixed compact region below O to a closed subinterval of the side
gap. Choose the corridor width before sending H to infinity and track
all resulting constants. Derive any separated harmonic comparison
explicitly; do not claim it is printed in Schmidt. Do not presume its
decay beats, or fails to beat, exp(2pi R H).

Source links and inspected proof cases are retained in the
[completed parent assessment](2026-10-30-finite-rectangle-negative-part-barrier.md).
The primary Dirichlet/Harnack source is
[Schmidt's January 2026 notes](https://www.math.uni-hamburg.de/home/schmidt/lectures/PDE.pdf).
Only their finite-domain statements are prospective inputs. Full
matching Mathlib coverage is unchecked.

An unbounded J_H would stop the majorant that substitutes L504's
uniform exponential envelope on the outer boundary and then removes
it along these truncations. It would not rule out a finite-height
optimization, a more precise function-dependent boundary estimate,
another exhaustion, or the original Q bound on H_a. A bounded J_H
would still leave the other outer terms, bottom kernel and uniformity
in T unresolved. These qualifications are essential downstream limits.

Continue only after source-scope approval and only for this one
finite-domain calculation. Record any proof in a canonical lemma if
a useful statement is established, preserving the earlier stops.
If no rigorous bound or informative obstruction emerges, save the
partial comparison and reassess without repeating qualitative theory.
