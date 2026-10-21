# Retained marked Tate-coordinate specialization — working record

Step 206 uses the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-marked-tate-coordinate-bridge.md`.
The main gap is original finite B>=A and actual input/action/pilot/
essentiality. The exact intermediate target is the marked compatibility
of L056's kappa and power isogeny placing gamma(Q) on a neighboring
canonical section over unchanged N. Its use is one local cusp-marking
prerequisite, independently of compatible splitting and full selected data.

Inputs: L053,L056,L057, with their retained L055,L051,L045,L048,L054
hypotheses. Preserve the changed r=q_0, fixed pointed uniformization,
global versus completed fields, actual maps and all seven sections.
The step-204 draft, step-205 primary coverage and ATTEMPTS/027,030
were inspected. No existing result establishes this marked identity;
the old exact-curve and full-multiplication stops remain in force.

Before the longer comparison: Conrad's rigid section 3.1 and Corollary
3.2.7 supply the actual generic fiber of the formal polygons, functorially
for the sections and formal power map. The intended test is to compute
their multiplicative quotient coordinates, then compare the resulting
isomorphism with kappa, rather than identifying formal-annulus and
Weierstrass coordinates by notation. The origin alone does not compute
the section. Any overlap formula must be inspected without silently
dropping inverses. A neighboring section up to orientation passes;
an arbitrary nonzero index, abstract Phi or valuation alone fails.

If this bounded specialization remains unresolved, preserve its exact
obstruction and park the dependent route for an independently testable
target. No new general comparison theorem is to be derived here.

## Imported comparison and actual-map obligations

Reuse [Conrad, Modular curves and rigid-analytic spaces, author PDF](https://math.stanford.edu/~conrad/papers/genpaper.pdf),
section 3.1, Theorems 3.1.5–3.1.6, equation (3.1.4), printed
pp.15–19, and Corollary 3.2.7, pp.22–23. These supply the functorial
rigid fiber of the SAME formal polygons and the proper-completion
comparison with their algebraizations. Hypotheses hold: N is complete
discretely valued, R=O_N is noetherian, 0<|r|<1, and the polygons
are proper of finite type over R. The (r)-adic and maximal-ideal
topologies agree since ord_R(r)>0. Import these general theorems.

For the actual maps reuse [Conrad, Arithmetic moduli of generalized
elliptic curves, July 18, 2006 author version](https://math.stanford.edu/~conrad/papers/kmpaper.pdf),
section 2.5, (2.5.1)–(2.5.3), Example 2.5.1 and Theorem 2.5.2
with its contraction proof, pp.17–18. L056 fixes

    gamma alpha = kappa^(-1) a_N h_N.

Here h_N(P)=tau_r(beta), beta^7=r, and Q=alpha(P). The two
step-204 point identities remain the test; Phi cannot replace them.
The prior representative check requires no enlargement of N:
sigma(beta)/beta=r^m for sigma in G_N by rationality of P and the
exact Tate kernel, while its seventh power is 1. Thus r^(7m)=1,
m=0 by valuation, and algebraic beta lies in N. This is reused
step-204 reasoning, not fresh progress.

## The annular coordinate test

The following is a candidate coordinate calculation, NOT a proved
comparison with the actual polygons. On G_m^an/r^(7Z), take

    |r|^(i+1) <= |z| <= |r|^i,  i=0,...,6,
    x_i=z/r^i,  y_i=r^(i+1)/z,  x_i y_i=r.

The boundary transitions forced by these formulas are

    x_(i+1)=1/y_i=x_i/r,
    y_(i+1)=r y_i.

They are defined where y_i, respectively x_(i+1), is a unit and
preserve the annulus relation. For i=6 use the lift with index 7;
replacing z by z/r^7 brings it to index 0. Thus wraparound is the
quotient equivalence and introduces no additional unit. The section
(x_i,y_i)=(1,r) represents [r^i]. Increasing i while keeping the
annular coordinates fixed multiplies z by r: this is one step.

For source parameter r and target parameter r^7 the annular power
formula (x_i,y_i)->(x_i^7,y_i^7) would give

    z'=(r^7)^i x_i^7=(r^i x_i)^7=z^7.

This respects the period groups. For n=1 use the rotation quotient
of an n>1 polygon, as required in the source, rather than treating
a self-glued annulus as one embedded formal affine chart. The
formulas commute with this quotient: rotation by r becomes rotation
by r^7 after powering. In these MODEL coordinates beta therefore
maps to beta^7=r, the expected neighboring-section representative.

What remains unverified is that this is the coordinate realization
of (3.1.4) for L056's ACTUAL sections, with normalization matching
the fixed tau and kappa. Equation (3.1.4) gives the rigid quotient
via gluing but does not print these coordinate pullbacks. Functoriality
alone does not identify an arbitrarily supplied atlas with the fixed
one. These computations cannot yet be substituted into the actual
algebraic-map identity. Neither sufficient point identity is proved.

## Diagnostic on the unusable extracted overlap

The companion paper's web text on p.17 renders the overlap as
Y_i=X_(i+1), X_i=Y_(i+1). Taken LITERALLY, this cannot give
the stated proper seven-gon. Reduce x_i y_i=r modulo r. The
branches with coordinates y_i and x_(i+1) are affine lines, whose
punctured lines the literal swap identifies by the same coordinate.
The two maps from Spec k[[t]] given by

    (x_i,y_i)=(0,t),  (x_(i+1),y_(i+1))=(t,0)

agree on Spec k((t)) but specialize to distinct nodes. The nodes
belong to none of the boundary-torus overlap opens, so remain
distinct after gluing. This violates uniqueness in the valuative
criterion for separatedness: these branches have doubled origin.
For the candidate inverse transition the second generic coordinate
would instead be t^(-1), so this particular obstruction disappears.

This rejects the literal extraction, NOT Conrad's theorem, its
actual polygon or IUT. It neither determines the missing typography
nor validates a repaired formula. No primary-source error is asserted.
It is a failed verification inside this attempt, not a new canonical
theorem or an IUT counterexample.

## Access, outcome and limits

Reinspected only the approved primary passages. The rigid theorem
text remains accessible. Screenshot calls returned citation text
without inspectable images; the alternate web interface explicitly
reported screenshots unavailable. One direct download failed DNS.
The previously assessed IAS DR scan's VII.1.1 and VII.1.14 locators
were revisited, but yielded no usable exact overlap formula. No new
literature search or extra general theorem was used. Retain step 205's
author-version/journal-byte and native odd-level qualifications.
An access failure does not show the mathematical identity is false.

Outcome: EXPLORATION, REPRODUCTION. The candidate-atlas computation
and separatedness diagnostic pinpoint the missing comparison, but
no actual neighboring-section identity is established. This is the
second unproductive mathematical attempt on this mechanism, counting
step 204; the source review did not reset that count. Park it.
Reopening needs a verified actual-chart comparison or a materially
different normalization test, not another abstract group, valuation,
origin-only or repeated source-access audit.

L053,L056,L057 and their audits remain unchanged. No lemma, DAG edge
or mathematical script is added. PROOF is unchanged because no new
input is adopted. Full matching Mathlib coverage is not checked.
Original finite B>=A and actual input/action/pilot/essentiality,
the cusp label, compatible splitting and full selected/theta data
remain open. The independent compatible-splitting predicate can be
assessed without this label; its coverage is REVIEW_REQUIRED and
no splitting is inferred here.
