# Quartic target: contract the full cubic derivative before estimating

Approved target: Determine whether L011's complete quartic probe-jet response kappa_0(f_(i,2),r_0) has a finite a^3-scaled limit for both actual L010 probes.
Reuse the unchanged EXPLORE assessment
`drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md`.

The main gap is the interacting reflected error <=c_box/2 and the
continuum/infrared construction. This bounded attempt tests the response
of dF_(i,3)(z)[b(z)] in L212. A subcubic estimate would leave just the
two-flow initial square and the cubic endpoint at cubic scale; their
limits and compensation would still require separate work.

Duplicate/failure check: current quartic drafts, C212a--f and histories
252--258 retain this derivative as uncontrolled. L191--L193 estimate a
different derivative with W=P db[t]; their complete Gaussian contractions
and prefix estimates are reusable inputs, not a preproved result here.
L022/ATTEMPTS/010 forbid isolated forest transfer. ATTEMPTS/039--045
concern other contraction orders and do not ban this test. The supplied
primary assessment covers the unchanged complete target; no new source
coverage or originality claim is needed.

Saved before completion: use the ambient full-link cubic formula with
E_s=exp(-s C^T C/a^2), retaining E_s b rather than H_s b. In its two
short placements, contract the smooth external Gaussian under covariance
S_lambda first. With h_l=S e_l and k_l=M e_l, differentiating this
contracted quadratic expectation should give the linear field

    X_l=db(z)[k_l]+d^2b[h_l,t], t=2SAz.

This is L192's field before P. The remaining quadratic covariance
derivative can be placed on either of its two linear legs because
(2SA)S=S(2SA)^T=M. No covariance derivative is lost. L192's explicit
pre-projection count gives ||X_l||_G<=C p(l) N^(9/2). Although E_s
does not damp gradients, ||E_s||<=1 and ||C E_s||<=C a/sqrt(s+a^2)
are sufficient for its polarized action inequality. This suggests
O(N^(5/2) log(eN)) after integrating the whole time interval.

The external placement is a product of two centered two-color quadratic
polynomials. Differentiate their two cross covariances on the b side,
giving the existing smooth-output db[t] estimate. The final observable
derivative has the same contracted X_l, with both other heat times tau.
Check the exact factors, all color pairings, final-endpoint regularity,
and applicability of the ambient cubic formula before accepting a bound.

Continue if these complete contractions and full-spectrum bounds close
below N^3. Abandon this estimate if it requires E_s b=H_s b, a smooth
rough tilt, missing boundary rows, or an unbounded zero-time interchange.
Keep the two independent cubic-scale limits, both probes, correlated
prefixes, upper jumps, constant modes and residual subtractions.

Completed: [C212g](../lemmas/C212g-cubic-probe-derivative-response-subcubic.md)
proves the full derivative correction is O(N^(5/2)log(eN)) in response,
so its cubic-scaled limit is zero for both probes. It differentiates
the two retained Gaussian covariances once each, and keeps E_s rather
than H_s on the nonlinear direction. The pre-projection L192 estimate
and C E_s bound suffice; the gradient field itself is never damped.
The complete quartic response is now O(N^3) and differs from the joint
two-quadratic-flow plus cubic-endpoint response by
O(N^(5/2)log(eN)). Its limit remains open. Verification is analytic,
with no mathematical scripts or numerical evidence.

Outcome ADVANCE / RESEARCH / REPRODUCTION; actual task proof_attempt.
This is local progress from the existing estimates, not a claim beyond
checked sources. Mathematical EXPLORATION usage remains zero. Continue
the unchanged covered complete target using L010 L011 L018 L181 L182
L186 L189 L191 L192 L193 L212 C212a--g. The two retained responses may
require a joint limiting argument; no separate convergence, compensation,
smooth rough tilt or endpoint interchange is assumed. The next test
must control their cubic-scale approximation errors while retaining
the full spectrum, both probes, both subtractions and pinned endpoints.
