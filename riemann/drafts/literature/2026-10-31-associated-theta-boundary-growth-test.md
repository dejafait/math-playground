# Proposed exact associated-theta boundary-growth discriminator

TARGET: Test whether delta*A(i(pi/4-delta)) tends to +infinity as delta tends to zero from above for the exact first associated theta kernel, retaining every theta mode, and compare only with radial O(delta^(-1)) boundary models.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed exact-theta discovery assessment records searches for Tuck/theta positivity, associated-kernel singularities and the pi/4 boundary, together with targeted local associated/theta duplicate searches; no matching limit theorem was identified. This bounded negative search does not establish novelty.
SOURCE_EVIDENCE: Read E. O. Tuck, On positivity of Fourier transforms, Bull. Austral. Math. Soc. 74 (2006), 133–138, pp.135–137 (5)–(13), https://doi.org/10.1017/S0004972700047511 ; reused the Csordas associated-kernel assessment and L233/L234; read L239's full actual-k strip argument. The exact radial limit is not asserted by any inspected source.
COMPARISON: Tuck excludes the bounded shifted-origin case and separately discusses integrable boundary singularities and a simple-pole model. L239 controls only closed smaller strips; the September complex-saddle attempt concerns a moving-frequency, proportional-degree integral. Neither provides the proposed radial limit. The new test concerns the exact correlation rather than a finite truncation or a reciprocal density.
GAP: Establish or refute the stated radial divergence, including the analytic meaning of A at every interior argument used. No boundary trace, uniform contour limit, nearest-singularity classification, Fourier sign or stronger-singularity criterion is covered.
REASON: A bounded source-applicability test can eliminate an unjustified low-order boundary ansatz before investment in a new positivity mechanism. Use known closed-strip bounds; derive only the missing radial estimate after separate approval. No reproof of theta modularity, Fourier identities or a published positivity theorem is needed.
SCOPE: Exact kernel and first associated function below; a one-sided radial-growth discriminator at i*pi/4 only. Newly saved coverage requires separate approval next turn. It does not authorize proving a Tuck positivity specialization, a horizontal boundary theorem or RH.

## Exact proposed mathematical target

Use L019's actual kernel on u>=0 and L239's holomorphic continuation
k to |Im z|<pi/4, including its exact modular evenness. For complex z
in that strip the proposed associated continuation is

    A(z)=integral_R s^2 k(s+z) k(s-z) ds.

Any attempt must first justify absolute convergence and holomorphy from
the closed-substrip domination, including all real shifts on compact z
sets. The target then asks whether, with 0<delta<pi/4,

    lim_(delta->0+) delta*A(i(pi/4-delta)) = +infinity.

Reality and positivity of the integrand on the radial path must be
justified from conjugation, rather than assumed for complex integrals.
This definition and limit are proposed targets, not new proved facts.

The meaningful threshold is failure of a radial O(delta^-1) bound.
An optional stronger estimate may be recorded only if proved and needed;
no exponent is claimed here. It suffices to obtain an explicit lower
bound on a specified real-s region with an absolutely bounded full theta
tail. A positive summand alone is not a lower bound for the squared
modulus of a complex sum. Constants and the onset of any first-mode
dominance must be justified; no raw even finite-theta approximation at
the origin or interchange of radial and truncation limits is authorized.

## Use, stopping test and limitations

The main gap is all-degree actual-Xi signs at unbounded heights. L233
gives the relevant first-level Fourier identity in the notebook's exact
normalization. If Tuck's contour criterion applied to this A, it could
address that first level; it would still leave higher degrees open.
The discriminator only tests low-order boundary models before such an
application. A successful growth bound would be an obstruction to those
models, not a positive sign result or a new RH bound.

Continue once with the stated radial estimate, using the exact theta
series and L239's already-proved strip continuation. Stop the low-order
ansatz if the limit is proved; if refuted, record the precise counterbound
and assess horizontal boundary hypotheses separately. An inconclusive
bound gets no automatic larger search. Any repeated attempt needs a
materially improved estimate or an identified competing region.

Radial divergence alone does NOT rule out arbitrary integrable horizontal
boundary traces, singularities elsewhere on the line, subtraction schemes,
regularized transforms or methods for stronger singularities. Conversely
its failure does not supply any of Tuck's monotonicity/convexity hypotheses.
No use of the different scaled zeta function on Tuck p.138 is proposed.

L560/L562, C567a and L569 are screened contrasts; they are not mathematical
premises for this growth test. L233 supplies the downstream first-sign
interpretation; L019 and L239 supply the exact kernel input. No source
requires RH, simplicity or zero-free boundary signs for this target.
Matching Mathlib coverage is not checked, not asserted absent. Classify
an eventual routine analytic specialization honestly; a positive outcome
would not certify originality. No mathematical attempt has yet occurred.
