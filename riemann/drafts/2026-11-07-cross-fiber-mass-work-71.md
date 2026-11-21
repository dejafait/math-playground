# Simple-fiber crossing mass — working checkpoint, step71

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-07-cross-fiber-mass-variation.md`; the exact
approved target is its COVERED_TARGET. This is one mathematical attempt,
not another source review. Supplied startup files and the assessment
were used directly. Existing notebook changes are preserved.

Main gap: L030–L032/C032a all-degree actual-Xi mixed positivity.
Intermediate target: the signed leading mass change for a fixed smooth
real radial bump across one simple off-diagonal G-zero fiber, with the
full Jacobian retained. A negative leading term could exclude that
contact from local minimizers, conditional on their existence; a
positive leading term stops the tested direction as a lowering device.
Zero leading coefficient would leave the sign unresolved. Other
contacts, graph/minimizer existence and compactness, sharp bounds,
higher signs and Xi transfer remain independent gaps.

Inputs read: L847's full form, density and compact-homotopy proof;
L879's hypotheses, phase-line conclusion and full relevant
variation/contact proof including its audit; L882's conditional
simple-fiber hypotheses/conclusion (optional, not used to assert
existence). Checked the attempt65 and attempt69 stops, and searched
the named stationarity/finite-descent assessments and L878 for overlap.
The supplied assessment already compares the scalar crossing theorem
and complex-modulus model. No new external theorem is being imported.

## Partial reasoning saved before completing the estimate

Work conditionally near a simple off-diagonal contact of G(z1).
L879 gives a clean local fiber z1(alpha,y)=zeta and Q=lambda*s with
s real. With x=y1-alpha, s=x*h and h(0,y)!=0. Write
a=partial_1 u1 on the fiber. For v=(chi,0), the first density
variation p=conjugate(lambda)*dot Q satisfies

    p(0,y)=h(0,y)*chi(0,y)/(a(y)+i).

Thus its imaginary trace is -h(0,y)*chi(0,y)/(1+a(y)^2), nonzero
where the bump trace is nonzero. The full Jacobian derivative is

    dot J=-(partial_2 u2)*partial_1 chi
          +(partial_1 u2)*partial_2 chi-i*partial_1 chi.

It vanishes from the trace formula only because F=0 there; away from
the fiber it must remain in p. L879's divergence identity should give
zero integrated linear variation, by splitting into the two half
rectangles and using Q=0 on their common boundary. The anticipated
coefficient of t^2 log(1/|t|), including normalized integration, is

    (2*pi)^(-2) integral |h(0,y)|*chi(0,y)^2/(1+a(y)^2)^2 dy.

Still to verify at this checkpoint: compact choice of the rectangle,
uniform preservation of J!=0 and external zeros; the zero linear term;
and an O(t^2) integrated error for the actual nonlinear Q_t. Proposed
estimate: replace Q_t by Q+t*dot Q with a uniform O(t^2) modulus
error, split |x|<=K|t| from its complement, and use the second-order
modulus expansion only on the complement. This is an application
estimate, not an invocation of the scalar real-kink theorem. No sign
claim is accepted yet.

## Completion

The saved pending estimate was completed in
[L887](../lemmas/L887-simple-fiber-radial-crossings-increase-mass.md).
It retains the full nonlinear density and proves the positive
logarithmic coefficient with an O(t^2) integrated error through
both signs of t. This supplies a scoped NEGATIVE for the lowering
attempt. The proof has not received an independent audit. The
canonical file contains all hypotheses, estimates and qualifications;
the earlier partial reasoning above is retained as a checkpoint,
not a second proof or an extra active continuation.
